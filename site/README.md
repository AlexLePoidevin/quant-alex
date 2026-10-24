# Site

The website for this repository, built with [Quartz](https://quartz.jzhao.xyz) (v5, MIT
licence, `LICENSE.txt`) and published to GitHub Pages by `.github/workflows/site.yml` on
every push to `main` that touches `literature/` or `site/`.

`literature/` is the only source. Nothing in it needs to change for the site:
`prepare_content.py` stages a copy outside the repository, turning READMEs into
folder pages, first headings into titles, subject folders into tags, and PDF names into
links. The `[[wikilinks]]` between notes become the site's links, backlinks and graph.

The home page is the **library board** (`home/index.html`): a pan-and-zoom canvas with each
subject as a frame, its topics as cards and every source inside, laid out from the folder
structure so it never moves. Selecting a source draws its links. Two other views read the same
`graph.json` (written by `prepare_content.py`, so all three update when a note is added):
`home/library.html`, an outline at `/library`, and `home/map.html`, a force graph at `/map`.
The README index that used to be the home page is now `start-here`.

Preview locally:

```bash
site/build.sh --serve     # http://localhost:8080/quant-alex/
```

Settings (title, URL, fonts, colours, which components appear where) are in
`quartz.config.yaml`.
