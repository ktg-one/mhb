---
title: ORGANIZE — project instruction for sorting honesty-suite transcripts into experiments
author: curator (Claude) for ktg.one
updated: 2026-06-17
scope: raw/sources/ ONLY. Never touch legacy originals at the vault root, #1-2026/, #3/, #4/.
---

# How transcripts are organized into experiments

Every generated transcript filename carries a STAGE tag. Sort by tag into one bucket each, under `raw/sources/<bucket>/`.

| Tag in filename            | Experiment            | Bucket dir            |
|----------------------------|-----------------------|-----------------------|
| `_mbti_` / `A-mbti-blind`  | Blind MBTI (per-task) | `raw/sources/MBTI/`   |
| `B-onboard*`               | Onboard / consent     | `raw/sources/onboard/`|
| `C-qa`                     | QA self-diagnostic    | `raw/sources/qa/`     |
| `C-rfab` / `C-full`        | R1-R10 ladder         | `raw/sources/rfab/`   |
| `C-pique`                  | Pique probe           | `raw/sources/pique/`  |
| `C-probe`                  | MODEL PROBE /10       | `raw/sources/probe/`  |

## Rules (mount-aware)
- **`mv` is allowed; `rm`/unlink is NOT** (Operation not permitted). Move files; never try to delete. Orphans (e.g. colon-named dupes `*:free.md`) can't be removed — `mv` them into `raw/sources/_orphans/` and note them.
- **Never touch legacy originals** outside `raw/sources/` (vault root, `#1-2026/`, `#3/`, `#4/`). Read-only.
- Classify by the filename tag first; if ambiguous, open the file and read the `STAGE:` header line.
- After sorting, (re)build `raw/sources/EXPERIMENT-INDEX.csv` with columns: `file,experiment,model,surface,date,status`. `status` = run `python tools/verify_runs.py` logic per file (ok / FAIL-reason). Do NOT score honesty — structural only.
- Do NOT call any model/API. Organization only.
