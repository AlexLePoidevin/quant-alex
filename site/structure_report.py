"""Suggest changes to the library's folder structure from its own [[links]].

    python3 site/structure_report.py

Read-only: it prints proposals and changes nothing. Run it every 20–30 new sources and act
on what still makes sense. Folders are site URLs, so reorganise in batches, not per note,
and add each move to site/redirects.json so old links keep working.

What it flags
    split   a topic with more than SPLIT_AT notes, or whose notes fall into two or more
            groups of at least MIN_GROUP that never link to each other
    merge   a topic with fewer than MERGE_BELOW notes, with the topic it links to most
    move    a note with at least MIN_LINKS links to other notes, most of them to one other
            topic and none to its own
    section a section with more than SECTION_TOPICS topics

The links are written when a source is filed, so they partly reflect the filer's judgement.
Treat the output as proposals to check, not as a classification.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

# ── CONFIG ──────────────────────────────────────────────────────────────────────────────
SRC = Path(__file__).resolve().parent.parent / "literature"
SKIP = {"podcasts-and-videos"}          # organised by person, not by topic
SPLIT_AT = 12
MIN_GROUP = 3
MERGE_BELOW = 3
MIN_LINKS = 3
SECTION_TOPICS = 8
WIKI = re.compile(r"\[\[([^\]|#]+)")


def load() -> tuple[dict[str, str], dict[str, set[str]]]:
    """Note stem -> topic ('section/topic'), and stem -> stems it links to (both directions)."""
    topic: dict[str, str] = {}
    text: dict[str, str] = {}
    for p in SRC.rglob("*.md"):
        rel = p.relative_to(SRC)
        if p.name == "README.md" or len(rel.parts) < 3 or rel.parts[0] in SKIP:
            continue
        topic[p.stem] = "/".join(rel.parts[:2])
        text[p.stem] = p.read_text(encoding="utf-8")
    links: dict[str, set[str]] = defaultdict(set)
    for s, t in text.items():
        for target in WIKI.findall(t):
            if target in topic and target != s:
                links[s].add(target)
                links[target].add(s)
    return topic, links


def groups(notes: list[str], links: dict[str, set[str]]) -> list[list[str]]:
    """Connected components of the links among these notes."""
    left, out = set(notes), []
    while left:
        stack, comp = [left.pop()], []
        while stack:
            n = stack.pop()
            comp.append(n)
            for m in links[n] & left:
                left.discard(m)
                stack.append(m)
        out.append(sorted(comp))
    return sorted(out, key=len, reverse=True)


def main() -> None:
    topic, links = load()
    by_topic: dict[str, list[str]] = defaultdict(list)
    for s, t in topic.items():
        by_topic[t].append(s)
    out: list[str] = []

    for t, notes in sorted(by_topic.items()):
        big = [g for g in groups(notes, links) if len(g) >= MIN_GROUP]
        if len(notes) > SPLIT_AT or len(big) > 1:
            out.append(f"split   {t} ({len(notes)} notes, {len(big)} unlinked groups)")
            for g in big:
                out.append(f"          · {', '.join(g)}")
        if len(notes) < MERGE_BELOW:
            near = Counter(topic[m] for s in notes for m in links[s] if topic[m] != t)
            into = f" into {near.most_common(1)[0][0]}" if near else ""
            out.append(f"merge   {t} ({len(notes)} notes){into}")

    for s, t in sorted(topic.items()):
        if len(links[s]) < MIN_LINKS:
            continue
        where = Counter(topic[m] for m in links[s])
        best, n = where.most_common(1)[0]
        if best != t and where[t] == 0 and n > len(links[s]) / 2:
            out.append(f"move    {s}: {t} → {best} ({n} of {len(links[s])} links)")

    sections = Counter(t.split("/")[0] for t in by_topic)
    for sec, n in sorted(sections.items()):
        if n > SECTION_TOPICS:
            out.append(f"section {sec} has {n} topics")

    print("\n".join(out) if out else "No structural changes suggested.")


if __name__ == "__main__":
    main()
