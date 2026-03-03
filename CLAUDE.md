# Website Repository — CLAUDE.md

## Overview
Academic website for Bin Chen, hosted on GitHub Pages at binchen.ac / chenbinzero.github.io.

## Framework
- Jekyll static site (Academic Pages theme, fork of Minimal Mistakes)
- Built and deployed by GitHub Pages automatically on push to `master`

## Key Paths
- `_config.yml` — site configuration
- `_data/navigation.yml` — top navigation bar (CV link here)
- `_data/google_scholar_stats.json` — auto-updated citation stats
- `_pages/` — site pages (about, publications, etc.)
- `_publications/` — individual publication markdown files
- `files/Bin_Chen_CV.pdf` — CV PDF (auto-updated, do not edit manually)
- `markdown_generator/pubs_wos.bib` — BibTeX source for publications
- `markdown_generator/pubsFromBib.py` — generates publication .md files from .bib

## Automation
1. **Google Scholar stats** — `.github/workflows/update_scholar_stats.yml` runs monthly, updates `_data/google_scholar_stats.json`
2. **CV PDF** — auto-compiled from LaTeX source in `chenbinzero/cv-latex` repo and pushed here via GitHub Action. **Do not edit `files/Bin_Chen_CV.pdf` directly** — edit the .tex source in the cv-latex repo instead.

## CV Update Workflow
To update the CV:
1. Edit `cv_4.tex` in the `chenbinzero/cv-latex` repo (or via Overleaf)
2. Push to GitHub (or sync from Overleaf via GitHub Sync button)
3. GitHub Action auto-compiles with xelatex and pushes `Bin_Chen_CV.pdf` to `files/` in this repo
4. Remind user to pull changes into Overleaf if edits were made from GitHub side

## Publications
- Each publication is a markdown file in `_publications/` with YAML front matter
- Citation stats displayed on Publications page via `_data/google_scholar_stats.json`
- **Scope**: first-author and corresponding-author papers only (not all co-authored papers)
- **No numbering** on the list — reverse chronological order only (numbers shift when papers are added)

### Workflow: Adding a New Paper
1. Get the DOI (from journal page or email notification)
2. Fetch abstract via WoS Extended API: `search_papers` tool with `DO=<DOI>` query
3. Fetch volume/issue/pages via CrossRef: `api.crossref.org/works/<DOI>`
4. Create `_publications/YYYY-MM-DD-slug.md` following the structure below
5. `git add _publications/<file>.md && git commit && git push` — GitHub Pages rebuilds in ~1–2 min

**Slug convention**: `YYYY-MM-DD-first-few-words-of-title.md` (lowercase, hyphens, ≤80 chars)
**Date field**: use online-first/published date for sort order; use `YYYY-01-01` if only print year is known

### Citation Format (ACS Style)
- **Author separator**: semicolons — `Last, F. M.; Last, F. M.`
- **Title**: plain text, no quotation marks, followed by a period
- **Journal**: italicised with `<i>...</i>`
- **Full format**: `Author1; Author2. Title. <i>Journal</i> Year, Vol (Issue), Pages.`
- **Chen, B. highlighting**: `<b>Chen, B.<sup>*</sup></b>` (corresponding) or `<b>Chen, B.<sup>†</sup></b>` (equal contribution)

### Venue Field Format
- Always include full bibliographic info: `Journal Year, Volume (Issue), Pages`
- Example: `Nature Energy 2024, 9 (3), 316–323` or `Science 2024, 386 (6724), 898–902`
- Source volume/issue/pages from **CrossRef API** (`api.crossref.org/works/<DOI>`) when WoS metadata is incomplete
- **Do not** use year alone without volume/pages (e.g. avoid `Nature Energy 2024`)
- Year is embedded in the venue string; the Jekyll template does NOT append year separately

### Paper Summaries (body text in `_publications/*.md`)
- **1–2 sentences** derived from the **abstract** (not the title)
- Source abstracts via **WoS Extended API** (`DO=<DOI>` field-tagged queries via `search_papers` tool)
- Capture: key mechanism/finding + key quantitative result (PCE %, stability metric, etc.)
- Use HTML entities for special chars: `&deg;`, `&gt;`, `&ndash;`, `&mu;`, `<sub>`, `<sup>`

### Citation Stats
- **Do not** use OpenAlex (wrong author disambiguation for "Bin Chen") or Semantic Scholar (fragmented, ~28 papers)
- Source: Google Scholar via `scholarly` library (Scholar ID: `H001jmIAAAAJ`)
- Cached in `_data/google_scholar_stats.json`, refreshed monthly by `.github/workflows/update_scholar_stats.yml`
- Manual trigger: GitHub → Actions tab → "Update Google Scholar Stats" → Run workflow

### Publication MD File Template
```yaml
---
title: "Full Paper Title"
collection: publications
permalink: /publication/YYYY-MM-DD-slug
date: YYYY-MM-DD          # used for sort order; use online-first date if available
venue: 'Journal Year, Vol (Issue), Pages'
paperurl: 'https://doi.org/<DOI>'
citation: 'Author1; Author2; <b>Chen, B.<sup>*</sup></b>; Author3 Title. <i>Journal</i> Year, Vol (Issue), Pages.'
---

1–2 sentence abstract-based summary with key mechanism and key quantitative result.

[Access paper here](https://doi.org/<DOI>){:target="_blank"}
```
