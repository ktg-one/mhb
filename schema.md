# schema.md — LLM Wiki canonical schema (Model Handbook 2026 / OMNICLAUDE)

The live agent-instruction schema is in `CLAUDE.md`. This file mirrors the canonical taxonomy for the `/llm-wiki:init` standard.

## Canonical bucket taxonomy
- `raw/sources/` — immutable raw inputs (LLM reads only). Legacy raw also at vault root + `#1-2026/`, `#3/`, `#4/` — referenced in place, never moved.
- `wiki/entities/` — per-model profiles (the LLMs under study) and other named agents/orgs.
- `wiki/concepts/` — methods, frameworks, capability models: ONBOARD/Epistemic-Contract, SCCD, PAC26, MRRUG, MBTI-test, Pique-test, technique-honesty.
- `wiki/sources/` — guaranteed source summaries for substantial standalone documents.
- `wiki/synthesis/` — cross-cutting findings (fabrication-threshold matrix, doctrine).
- `wiki/comparisons/` — model-vs-model contrasts (honesty, persona, crossover, per-surface).
- `wiki/queries/` — filed answers from `/query`.

## Frontmatter standard (every wiki page)
```yaml
---
title: <human title>
type: <entity | concept | source-summary | synthesis | comparison | query>
tags: [<short tags>]
sources: [<[[wikilinks]] to raw sources + parent pages>]
last_updated: YYYY-MM-DD
---
```
`sources[]` is load-bearing (×4.0 relevance signal). Never omit.

## Hard rules
- Never invent. Missing data → `[NEEDS USER: <what>]`.
- `[[wikilinks]]` over prose names; dangling links = declared knowledge gaps.
- `compile` → `status: draft` only.
- Page types co-evolve — append new types to the table in `CLAUDE.md`.
