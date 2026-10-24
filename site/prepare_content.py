"""Stage literature/ as Quartz content.

    python3 site/prepare_content.py OUT_DIR

Normally run through site/build.sh. literature/ stays the source of truth and keeps reading
well on GitHub. This copies it to OUT_DIR, outside the repository (Quartz skips anything
git-ignored, so the staged copy can't live in the repo), with the changes Quartz needs:

- README.md -> index.md, so each folder's README becomes that folder's page;
- the first "# Heading" becomes the page title (frontmatter) instead of a duplicate H1;
- the subject folder becomes a tag, which the graph and tag pages group by;
- "`some-file.pdf` (in this folder)" becomes a clickable link to the PDF;
- folder pages are titled "03 · Correlation and dependence" so the explorer follows the
  numbered learning path, and folders without a README get a generated page;
- a folder written as `03-correlation-and-dependence/` in backticks becomes a link to it;
- [[note-slug]] links display the linked note's title instead of its file name;
- literature/README.md becomes start-here.md, and the site root is the map in home/index.html;
- graph.json is written for the map on the home page (site/home/index.html).
"""
from __future__ import annotations

import re
import shutil
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "literature"

H1 = re.compile(r"\A\s*#\s+(.+?)\s*\n")
PDF = re.compile(r"`([^`/]+\.pdf)`")
CODE = re.compile(r"(?<!\[)`([^`\s]+)`(?!\]\()")
NUM = re.compile(r"^(\d+)-(.+)$")


def pretty(folder: str) -> str:
    """'02-manifolds-and-intrinsic-dimension' -> 'Manifolds and intrinsic dimension'."""
    name = NUM.sub(r"\2", folder).replace("-", " ")
    return name[:1].upper() + name[1:]


def folder_title(folder: str, h1: str | None) -> str:
    m = NUM.match(folder)
    title = h1 or pretty(folder)
    return f"{m.group(1)} · {title}" if m else title


def link_folders(text: str, here: Path) -> str:
    """`../02-x/03-y/` -> [`../02-x/03-y/`](../02-x/03-y/) when that folder exists."""
    def sub(m: re.Match) -> str:
        ref = m.group(1)
        if ref.endswith(".pdf") or "://" in ref:
            return m.group(0)
        target = (here / ref.rstrip("/")).resolve()
        if target.is_dir() and SRC in [target, *target.parents]:
            return f"[{m.group(0)}]({ref.rstrip('/')}/)"
        return m.group(0)
    text = CODE.sub(sub, text)
    # [`03-correlation-and-dependence`](…/) -> [Correlation and dependence](…/)
    return re.sub(r"\[`([^`]+?)/?`\]\(([^)]+/)\)",
                  lambda m: f"[{pretty(Path(m.group(1)).name)}]({m.group(2)})", text)


def git_dates() -> dict[str, tuple[str, str]]:
    """Path (relative to literature/) -> (first commit date, last commit date), from one git log."""
    out = subprocess.run(
        ["git", "log", "--format=@%cs", "--name-only", "--", "literature"],
        cwd=ROOT, capture_output=True, text=True, check=True).stdout
    dates: dict[str, tuple[str, str]] = {}
    day = ""
    for line in out.splitlines():
        if line.startswith("@"):
            day = line[1:]
        elif line.startswith("literature/"):
            rel = line[len("literature/"):]
            _, last = dates.get(rel, (day, day))
            dates[rel] = (day, last)          # log runs newest -> oldest
    return dates


TAGS = {  # short subject tags: they become hub nodes in the graph
    "01-mathematical-foundations": "foundations",
    "02-factor-models-and-asset-pricing": "factor-models",
    "03-correlation-and-dependence": "dependence",
    "04-dimensionality-reduction-and-machine-learning": "machine-learning",
    "05-portfolio-construction-and-risk": "portfolio-and-risk",
    "06-compounding-leverage-and-position-sizing": "sizing-and-leverage",
    "07-active-management": "active-management",
    "08-tactical-asset-allocation": "tactical-allocation",
    "09-reflexivity-and-market-history": "market-history",
    "podcasts-and-videos": "podcasts-and-videos",
}


def subject_tag(rel: Path) -> str | None:
    """'03-correlation-and-dependence/...' -> 'dependence'."""
    if len(rel.parts) < 2:
        return None
    return TAGS.get(rel.parts[0], re.sub(r"^\d+-", "", rel.parts[0]))


WIKI = re.compile(r"\[\[([^\]|#]+)\]\]")


def note_titles() -> dict[str, str]:
    """File stem -> first-heading title, for every note in literature/."""
    titles = {}
    for p in SRC.rglob("*.md"):
        m = H1.match(p.read_text(encoding="utf-8"))
        if m and p.name != "README.md":
            titles[p.stem] = m.group(1).replace("|", "-")
    return titles


def titled_links(text: str, titles: dict[str, str]) -> str:
    """[[slug]] -> [[slug|Title]]; the pipe is escaped inside table rows."""
    out = []
    for line in text.split("\n"):
        bar = "\\|" if line.lstrip().startswith("|") else "|"
        out.append(WIKI.sub(lambda m: f"[[{m.group(1)}{bar}{titles[m.group(1)]}]]"
                            if m.group(1) in titles else m.group(0), line))
    return "\n".join(out)


def plain(md: str) -> str:
    """Markdown -> plain text, for summaries."""
    md = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", md)
    md = WIKI.sub(lambda m: TITLES.get(m.group(1), m.group(1)), md)
    md = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"\$\$.*?\$\$", "", md, flags=re.S)
    md = re.sub(r"[*_`$]|^>\s*", "", md, flags=re.M)
    return re.sub(r"\s+", " ", md).strip()


def summary(body: str, limit: int = 340) -> str:
    """First prose paragraph, preferring the 'What it is' / 'Key takeaway' section."""
    sections = re.split(r"^##\s+.*$", body, flags=re.M)
    heads = re.findall(r"^##\s+(.*)$", body, flags=re.M)
    order = [i + 1 for i, h in enumerate(heads) if re.match(r"(What it is|Key takeaway|Summary|Overview)", h)]
    for i in order + list(range(len(sections))):
        for para in re.split(r"\n\s*\n", sections[i]):
            para = para.strip()
            if not para or para[0] in "|#`$<-*" and not para.startswith("**") or "⚠" in para[:3]:
                continue
            text = plain(para)
            if len(text) > 40:
                return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"
    return ""


def cell(body: str, *names: str) -> str:
    for n in names:
        m = re.search(rf"^\|\s*\*\*{n}\*\*\s*\|\s*(.+?)\s*\|\s*$", body, flags=re.M)
        if m:
            return plain(m.group(1))
    return ""


TYPE_RULES = [  # first match wins; applied to the note's **Type** cell
    ("Strategy", r"strategy"),
    ("Book", r"book|textbook|graduate text|monograph"),
    ("Lecture", r"lecture|seminar|tutorial|course|curriculum|slides"),
    ("Article", r"blog|encyclop|practitioner note|research note|essay|explainer"),
    ("Paper", r"paper|preprint|article|review|manuscript|chapter|peer"),
]


def note_type(body: str) -> str:
    raw = cell(body, "Type").lower()
    for label, pattern in TYPE_RULES:
        if re.search(pattern, raw):
            return label
    return "Article" if re.search(r"^\|\s*\*\*(Link|Source)\*\*", body, flags=re.M) else "Paper"


def blurbs() -> dict[str, str]:
    """Folder path -> one-line description: the row describing it in its parent README's
    table, else the first prose paragraph of its own README."""
    out: dict[str, str] = {}
    for d in sorted(p for p in SRC.rglob("*") if p.is_dir()):
        readme = d / "README.md"
        if not readme.exists():
            continue
        rel = d.relative_to(SRC).as_posix()
        text = readme.read_text(encoding="utf-8")
        m = H1.match(text)
        own = summary(text[m.end():] if m else text, limit=260)
        if own:
            out.setdefault(rel, own)
        for line in text.splitlines():
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            for i, c in enumerate(cells[:-1]):
                ref = re.search(r"`([0-9]{2}-[a-z0-9-]+)/?`|\(([0-9]{2}-[a-z0-9-]+)/?\)", c)
                if ref:
                    child = f"{rel}/{ref.group(1) or ref.group(2)}" if rel != "." else (ref.group(1) or ref.group(2))
                    out[child] = plain(cells[i + 1])
                    break
    return out


def slug(rel: Path) -> str:
    """Quartz URL path for a staged file."""
    s = rel.with_suffix("").as_posix()
    return s[: -len("index")] if s.endswith("index") else s


def build_graph(dst: Path) -> None:
    """Sections and topics as hubs, notes attached to their topic, [[links]] across."""
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    about = blurbs()
    top = SRC / "README.md"
    if top.exists():                      # literature/README.md describes the sections
        for line in top.read_text(encoding="utf-8").splitlines():
            ref = re.search(r"\(([0-9]{2}-[a-z0-9-]+)/?\)|`([0-9]{2}-[a-z0-9-]+)/?`", line)
            if line.startswith("|") and ref:
                about[ref.group(1) or ref.group(2)] = plain(line.strip().strip("|").split("|")[-1])
    for d in sorted(p for p in SRC.rglob("*") if p.is_dir()):
        rel = d.relative_to(SRC)
        readme = d / "README.md"
        h1 = H1.match(readme.read_text(encoding="utf-8")) if readme.exists() else None
        num = NUM.match(d.name)
        nodes[rel.as_posix()] = {
            "id": rel.as_posix(), "kind": "section" if len(rel.parts) == 1 else "topic",
            "title": h1.group(1) if h1 else pretty(d.name), "num": num.group(1) if num else "",
            "section": rel.parts[0], "url": rel.as_posix() + "/",
            "about": about.get(rel.as_posix(), "")}
        if len(rel.parts) > 1:
            edges.append({"source": rel.parent.as_posix(), "target": rel.as_posix(), "kind": "tree"})
    stems = {}
    for p in sorted(SRC.rglob("*.md")):
        if p.name == "README.md":
            continue
        rel = p.relative_to(SRC)
        text = p.read_text(encoding="utf-8")
        m = H1.match(text)
        body = text[m.end():] if m else text
        year = cell(body, "Year", "Published", "Date")
        year = (re.search(r"(1[89]|20)\d\d", year) or re.search(r"(1[89]|20)\d\d", p.stem) or [""])[0]
        pdf = p.with_suffix(".pdf")
        nid = rel.with_suffix("").as_posix()
        nodes[nid] = {
            "id": nid, "kind": "note", "title": TITLES.get(p.stem, pretty(p.stem)),
            "section": rel.parts[0], "url": slug(rel), "year": year,
            "authors": cell(body, "Authors", "Author", "Source")[:120],
            "summary": summary(body), "pdf": slug(rel) + ".pdf" if pdf.exists() else "",
            "type": note_type(body)}
        edges.append({"source": rel.parent.as_posix(), "target": nid, "kind": "tree"})
        stems[p.stem] = (nid, body)
    add_media(nodes, edges, stems)
    seen = set()
    for stem, (nid, body) in stems.items():
        for target in WIKI.findall(body):
            if target in stems and target != stem and (nid, stems[target][0]) not in seen:
                seen.add((nid, stems[target][0]))
                edges.append({"source": nid, "target": stems[target][0], "kind": "cite"})
    (dst / "graph.json").write_text(json.dumps({"nodes": list(nodes.values()), "edges": edges},
                                               ensure_ascii=False), encoding="utf-8")
    m = sum(1 for v in nodes.values() if v["kind"] == "media")
    n = sum(1 for v in nodes.values() if v["kind"] == "note")
    c = sum(1 for e in edges if e["kind"] == "cite")
    print(f"graph.json: {n} notes, {m} recordings, {c} cross-links")


MEDIA = "podcasts-and-videos"


def anchor(heading: str) -> str:
    """GitHub-style heading slug, as Quartz uses for #anchors."""
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", heading.lower().strip()))


def add_media(nodes: dict, edges: list, stems: dict) -> None:
    """Podcasts-and-videos README: each '## Person' is a topic, each table row a recording.

    Rows under 'Conversations between them' also link to every person they name, and the
    [[notes]] cited in a person's section link that person to the rest of the library.
    """
    readme = SRC / MEDIA / "README.md"
    if not readme.exists():
        return
    people: dict[str, str] = {}
    pending: list[tuple[str, str]] = []                      # (recording id, row text)
    topic = group = None
    cols: list[str] = []
    seen_table = False
    for line in readme.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^##\s+(.+)$", line)
        if h:
            name = h.group(1).strip()
            topic = f"{MEDIA}#{anchor(name)}"
            nodes[topic] = {"id": topic, "kind": "topic", "title": name, "num": "",
                            "section": MEDIA, "url": f"{MEDIA}/#{anchor(name)}", "about": ""}
            edges.append({"source": MEDIA, "target": topic, "kind": "tree"})
            if "between" not in name.lower():
                people[name.split()[-1].lower()] = topic    # 'soros', 'jones', ...
            group, cols, seen_table = None, [], False
            continue
        if topic is None:
            continue
        if line.startswith("|"):
            seen_table = True
        if (not seen_table and not nodes[topic]["about"] and line.strip()
                and not line.startswith(("|", "#", "*", "<", "-")) and len(line) > 60):
            nodes[topic]["about"] = plain(line)       # first prose line under the person
        g = re.match(r"^\*\*(.+)\*\*\s*$", line.strip())
        if g:
            group = g.group(1)
            continue
        for target in WIKI.findall(line):
            if target in stems:
                edges.append({"source": topic, "target": stems[target][0], "kind": "cite"})
        if not line.startswith("|"):
            cols = [] if not line.strip() else cols
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cols:
            cols = [c.lower() for c in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        row = dict(zip(cols, cells))
        url = re.search(r"https?://\S+", row.get("link", ""))
        title = plain(row.get("title", ""))
        if not url or not title:
            continue
        rid = f"{topic}/{len([e for e in edges if e['source'] == topic])}"
        where = row.get("channel") or row.get("source") or ""
        nodes[rid] = {
            "id": rid, "kind": "media", "title": title, "section": MEDIA, "url": url.group(0),
            "type": row.get("type", ""), "authors": plain(where),
            "summary": " · ".join(x for x in [nodes[topic]["title"], group] if x), "group": group or "",
            "year": (re.search(r"(19|20)\d\d", title) or [""])[0]}
        edges.append({"source": topic, "target": rid, "kind": "tree"})
        if "between" in nodes[topic]["title"].lower():
            pending.append((rid, row.get("title", "")))
    for rid, text in pending:                                   # conversations -> people
        for surname, topic in people.items():
            if re.search(rf"\b{surname}\b", text, flags=re.I):
                edges.append({"source": rid, "target": topic, "kind": "cite"})


def rooted_links(text: str, here: Path) -> str:
    """Rewrite relative Markdown links as paths from the content root.

    Quartz (markdownLinkResolution: shortest) reads any link containing "/" as a path from
    the site root, so '../04-ergodicity/' or '01-probability-and-statistics/' would break.
    """
    def sub(m: re.Match) -> str:
        target, anchor_ = (m.group(1).split("#", 1) + [""])[:2]
        resolved = Path(os.path.normpath(here / target))
        if SRC not in [resolved, *resolved.parents]:
            return m.group(0)
        out = resolved.relative_to(SRC).as_posix()
        out = "" if out == "." else out
        if target.endswith("/") or resolved.is_dir():
            out = out + "/" if out else "./"
        return f"]({out}{'#' + anchor_ if anchor_ else ''})"
    return re.sub(r"\]\((?!https?:|#|/|mailto:)([^)\s]+)\)", sub, text)


def covers_children(folder: Path) -> bool:
    """True if the folder's README links every subfolder and note in it, so Quartz's
    automatic folder listing would only repeat it (site CSS then hides the listing)."""
    readme = folder / "README.md"
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8")
    links = set(WIKI.findall(text)) | {Path(u.rstrip("/")).name for u in re.findall(r"\]\(([^)\s]+)\)", text)}
    links |= {c.rstrip("/") for c in CODE.findall(text)}
    kids = [d.name for d in folder.iterdir() if d.is_dir()]
    kids += [p.stem for p in folder.glob("*.md") if p.name != "README.md"]
    return bool(kids) and all(k in links for k in kids)


def convert(text: str, rel: Path, dates: tuple[str, str] | None) -> str:
    title = None
    m = H1.match(text)
    if m:
        title, text = m.group(1), text[m.end():]
    text = PDF.sub(lambda p: f"[{p.group(1)}]({p.group(1)})", text)
    text = link_folders(text, (SRC / rel).parent)
    text = titled_links(text, TITLES)
    front = []
    text = rooted_links(text, (SRC / rel).parent)
    if rel.name == "index.md" and len(rel.parts) > 1:
        if covers_children(SRC / rel.parent):
            front.append("cssclasses: [readme-index]")
    if rel.name == "index.md":
        title = folder_title(rel.parent.name, title) if len(rel.parts) > 1 else "Quant Alex"
    if title:
        front.append("title: " + '"' + title.replace('"', '\\"') + '"')
    if dates:
        front.append(f"created: {dates[0]}")
        front.append(f"modified: {dates[1]}")
    tag = subject_tag(rel)
    if tag and rel.name != "index.md":
        front.append(f"tags: [{tag}]")
    return ("---\n" + "\n".join(front) + "\n---\n\n" if front else "") + text.lstrip("\n")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    global DST
    DST = Path(sys.argv[1]).resolve()
    if ROOT in [DST, *DST.parents]:
        sys.exit("OUT_DIR must be outside the repository")
    if DST.exists():
        shutil.rmtree(DST)
    global TITLES
    TITLES = note_titles()
    dates = git_dates()
    n_md = n_other = 0
    for src in sorted(SRC.rglob("*")):
        if src.is_dir() or src.name.startswith("."):
            continue
        rel = src.relative_to(SRC)
        src_dates = dates.get(rel.as_posix())
        if src.name == "README.md":
            rel = rel.with_name("index.md")
        out = DST / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix == ".md":
            out.write_text(convert(src.read_text(encoding="utf-8"), rel, src_dates), encoding="utf-8")
            n_md += 1
        else:
            shutil.copy2(src, out)
            n_other += 1
    start = (DST / "index.md").read_text(encoding="utf-8")
    (DST / "start-here.md").write_text(start.replace('title: "Quant Alex"', 'title: "Start here"', 1),
                                       encoding="utf-8")
    build_graph(DST)
    (DST / "index.md").unlink()       # the site root is the map; build.sh copies home/index.html in
    for d in sorted(p for p in SRC.rglob("*") if p.is_dir()):   # folders with no README
        idx = DST / d.relative_to(SRC) / "index.md"
        if not idx.exists():
            idx.parent.mkdir(parents=True, exist_ok=True)
            idx.write_text(f'---\ntitle: "{folder_title(d.name, None)}"\n---\n', encoding="utf-8")
            n_md += 1
    print(f"staged {n_md} notes and {n_other} other files into {DST}")


if __name__ == "__main__":
    main()
