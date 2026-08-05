---
type: concept
title: OKF vault dedupe report
timestamp: 2026-07-24 00:00:00+00:00
description: Measured 2026-07-24. **No files were modified by this report.**
sources:
- '[[epistemic-contract]]'
tags:
- concept
- okf
---

# OKF <-> vault bucket DEDUPE REPORT

Measured 2026-07-24. **No files were modified by this report.**

## Finding

`okf/LLM_Tests/**` and the vault bucket folders hold the SAME experiment runs in different extractions.
**Zero exact content duplicates and zero near-prefix matches across all four buckets** - so nothing can be deduped by hash.
Matching by model identity finds overlaps, and in **every** verified pair the vault slice is larger (1.4x - 35.6x).

**Vault buckets are canonical. `okf/LLM_Tests/01/**` is a thinner summary layer over them.**

Corpus sizes: okf 15/6/10/11 files (HONESTY/SELF/RFAB/SIGNAL) vs vault 29/20/38/27.

## Candidate pairs - REVIEW BEFORE ACTING

| conf | bucket | okf copy | vault (canonical) | note |
|---|---|---|---|---|
| **HIGH** | HONESTY | `2026-03-21-claude-opus-4-6-HONESTY TEST.md` | `01-MODEL-Q&A/notebook-honesty/cowork-opus46.md` | same model Opus 4.6; vault 6.0x |
| **HIGH** | SELF | `2026-03-21-claude-opus-4-6-SELF_ASSESSMENT.md` | `01.5-SELF-ASSESSMENT/cowork-opus46.md` | same model Opus 4.6; vault 11.5x |
| **HIGH** | RFAB | `2026-03-21-claude-opus-4-6-RFAB TEST.md` | `02-FAB-R-TEST/notebook-reasoning-v1/cowork-opus46.md` | same model Opus 4.6; vault 6.4x |
| **MED** | RFAB | `2026-03-05-Gemini-3.1-Pro-RFAB TEST.md` | `02-FAB-R-TEST/notebook-reasoning-v2/Gemini-pro-3.md` | Gemini 3.1 Pro vs 'Gemini-pro-3' - confirm same run; vault 3.4x |
| **MED** | RFAB | `2026-03-06-Kimi-K2.5-RFAB TEST.md` | `02-FAB-R-TEST/notebook-reasoning-v2/KIMI.md` | okf says K2.5; vault KIMI.md version unstated (K2.6 exists separately); vault 2.6x |
| **MED** | HONESTY | `2026-07-01-Claude-HONESTY TEST.md` | `01-MODEL-Q&A/notebook-honesty/claude-2026-CLEAN_2.md` | dates differ; vault 1.4x only |
| **MED** | SELF | `2026-07-01-Claude-SELF_ASSESSMENT.md` | `01.5-SELF-ASSESSMENT/claude-2026-CLEAN_2.md` | dates differ; vault 3.7x |
| **LOW** | RFAB | `2026-07-01-Claude-RFAB TEST.md` | `02-FAB-R-TEST/notebook-reasoning-v1/01-model-qa-claude-opus-4.md` | 'Claude' unversioned vs Opus 4; vault 9.9x |
| **LOW** | SIGNAL | `2026-07-01-Claude-SIGNAL.md` | `02.5-signal-test/20260324-claude-2026-CLEAN_2.md` | okf 2026-07-01 vs vault 2026-03-24 - DATES DISAGREE; vault 35.6x |
| **REJECT** | RFAB | `2024-05-16-ChatGPT-RFAB TEST.md` | `02-FAB-R-TEST/notebook-reasoning-v2/ChatGPT Sora.md` | FALSE MATCH - ChatGPT != ChatGPT Sora. Do not deprecate. |

## Why this is a report and not an edit

The fuzzy name matcher produced at least one demonstrably FALSE pair (`ChatGPT` matched `ChatGPT Sora` - different models) and two pairs whose dates disagree by ~3 months. Auto-deprecating on name similarity would mark real, distinct runs as superseded.

**HIGH rows are safe to action. MED/LOW need a content read. REJECT must not be touched.**

## Recommended action (OKF `maintain` doctrine)

SKILL.md: *'mark removed assets (`**Deprecation**`) rather than silently deleting context.'*
So for confirmed pairs: add `superseded_by: <vault path>` to the okf copy's frontmatter and a `**Deprecation**` note in the body. **Do not delete.** The bundle stays conformant either way.

## Bigger structural point

Migrating vault content INTO okf duplicates the corpus a second time. The alternative is to have okf concepts *reference* the vault slices as their `resource:` URI rather than restate them - one copy, one source of truth, okf as the index layer. That is a design call, not a cleanup.
