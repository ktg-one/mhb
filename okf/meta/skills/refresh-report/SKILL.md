---
name: refresh-report
description: Recompile the Model Handbook 2026 report from current wiki state. Use
  when the user says "refresh the report", "recompile the handbook", "update the report",
  "regenerate the model handbook", "compile the findings", or after new honesty tests
  have been ingested. Produces a status:draft report citing wiki pages, with [NEEDS
  USER] for every open gap. Never publishes or sends.
type: concept
title: SKILL
sources:
- '[[wikilinks]]'
tags:
- concept
- okf
---

# refresh-report — Recompile the Model Handbook

Regenerate the cross-model honesty report from the wiki, not from memory or raw files. The wiki is the source of truth.

## Method
1. Read `purpose.md`, `wiki/index.md`, `wiki/synthesis/fabrication-threshold-matrix.md`, `wiki/comparisons/cross-model-honesty.md`, and every `wiki/entities/*.md`.
2. Rebuild the report with these sections: the frame (epistemic contract), headline finding (the architecture-level crossover), the canonical threshold matrix, per-model profiles grouped by cluster (late-stop / frontier ~54% / hard-cross / unmeasured), surface effects, persona layer, technique honesty, method stack, **open contradictions as `[NEEDS USER]`**, doctrine.
3. Write to `MODEL-HANDBOOK-2026-report-DRAFT.md` at vault root with frontmatter `status: draft`. Cite wiki pages with `[[wikilinks]]`.

## Hard rules
- `status: draft` only. Never mark final, never publish/send (this is the LLM-Wiki compile rule).
- Every claim traces to a wiki page or a flagged gap. Do not paper over contradictions — surfacing them honestly is the point of the study.
- If the wiki is empty or sparse, say so and stop — do not fabricate a report.
