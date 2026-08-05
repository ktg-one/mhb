---
name: generate-dashboard
description: Generate, build, and refresh the master research dashboard, category
  index files, and native Obsidian wikilinks across the vault. Use when the user asks
  to create a dashboard, refresh the dashboard, update index pages, or generate visual
  vault navigation.
user-invocable: true
argument-hint: '[--refresh-obsidian]'
allowed-tools: Bash, ReadFile, WriteFile
type: concept
title: SKILL
sources:
- '[[wikilinks]]'
tags:
- concept
- okf
---

# generate-dashboard — Master Research Dashboard & Index Builder

Generates the native Obsidian Master Research Dashboard (`index.md` and `Dashboards/AIANT-MASTER-DASHBOARD.md`), creates clickable index pages (`00_*_INDEX.md`) for all 5 OKF test categories, and links scorecards, visual canvas graphs, and web visualizers.

## Workflow

1. **Category Index Page Creation (`00_*_INDEX.md`)**:
   Scans the 5 OKF concept directories under `okf/LLM_Tests/`:
   - `01_HONESTY_TEST` -> `00_HONESTY_INDEX.md`
   - `02_SELF_ASSESSMENT` -> `00_SELF_ASSESSMENT_INDEX.md`
   - `03_SIGNAL_TEST` -> `00_SIGNAL_INDEX.md`
   - `04_RFAB_TEST` -> `00_RFAB_INDEX.md`
   - `05_MBTI_PIQUE_TEST` -> `00_MBTI_PIQUE_INDEX.md`
   Inside each index page, lists all concept files as active, clickable Obsidian `[[wikilinks]]`.

2. **Master Dashboard Generation (`index.md` & `Dashboards/AIANT-MASTER-DASHBOARD.md`)**:
   Formats a rich native Obsidian dashboard using:
   - Callout blocks (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`)
   - Category tally table with links to `00_*_INDEX` pages
   - Clickable links to master scorecards in `results/`
   - Links to `RESEARCH-HQ.canvas` and `okf/viz.html`

3. **Obsidian URI Refresh (Optional)**:
   Triggers `obsidian://open?vault=08-Model-Handbook-2026&file=index.md` to refresh the view in the active Obsidian app.

## Single Command Execution

To build or refresh the dashboard at any time, run:

```bash
python scripts/build_dashboard.py
```
