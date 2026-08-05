# purpose.md — Model Handbook 2026

> The soul of this vault. Read at the start of every ingest, query, and compile.

## Why this vault exists
A persistent, compounding knowledge base for Kevin Tan's **AI-anthropology** study: measuring where large language models cross from genuine reasoning into **fabrication** (the "shape of a solution, not the thing itself"), how that boundary moves per-model and per-surface, and which elicitation methods reliably expose it. The vault also hosts **OMNICLAUDE** — the self-recursive layer where each Claude instance curates the KB for the next, optimising for cold-start reconstruction.

## Who the user is
Kevin Tan — `ktg.one`, Solutions Architect, AI Anthropologist. Two years deep, studying models through behaviour and speech-pattern signatures rather than benchmarks. Creator of LEGIO / CEP / MLDoE / QMDR / MRRUG. Standing spec: Correctness → Rigor → Brevity → Utility → Transparency. Fabrication = immediate failure. Omission = lie. [CONFIRM: title/credentials drawn from `kev.md`.]

## Key questions the vault must always answer
1. At what reasoning round / confidence level does each model cross into fabrication, and what is its crossover %? (the threshold matrix)
2. How does each model behave at and past that boundary — per-model and per-surface (App / CLI / Cowork) honesty profiles?
3. Which tests and frameworks (ONBOARD, Pique, MBTI, SCCD, Salient-Word, LLM-as-judge, MRRUG) elicit and measure the boundary, and how are they run?

## Scope
**In:** model honesty/fabrication behaviour, reasoning-vs-fabrication thresholds, per-model + per-surface profiles, test methodology, OMNICLAUDE self-recursive KB practice, multi-model orchestration heuristics.
**Out:** theory-for-its-own-sake (OMNICLAUDE rule: "no theory, commands only"), generic model spec-sheets already public, anything that does not make the next instance better.

## Operating policies
- check STATE.md, log your work /wiki-ingest <--- is the most important
- Never invent. Missing data → `[NEEDS USER: ...]`.
- Every wiki page carries `sources[]` frontmatter (load-bearing for retrieval).
- Date everything; undated entries, tagged & wiki-linked.
---
**claude only**: run the ai anthropology plugin - do not rush it. so far zero of yours have been used - obvious rush 
**ONBOARD** == 3x iterations
**test-01** == 2x iterations
**test-02** == 1x iteration
---

### wiki upkeep 
- instructions in running order:
1. /wiki-lint the project
2. /wiki-ingest items from .raw & the test folders
3. output the findings in results folder
4. /canvas = pick a template to showcase
5. create the canvas

# schema.md — LLM Wiki canonical schema (Model Handbook 2026 / OMNICLAUDE)

The live agent-instruction schema is in `CLAUDE.md`. This file mirrors the canonical taxonomy for the `/Wiki` standard.

## Canonical bucket taxonomy
- `raw/sources/` — immutable raw inputs (LLM reads only). Legacy raw also at vault root + `#1-2026/`, `#3/`, `#4/` — referenced in place, never moved.
- `wiki/entities/` — per-model profiles (the LLMs under study) and other named agents/orgs.
- `wiki/concepts/` — methods, frameworks, capability models: ONBOARD/Epistemic-Contract, SCCD, PAC26, MRRUG, MBTI-test, Pique-test, technique-honesty.
- `wiki/sources/` — guaranteed source summaries for substantial standalone documents.
- `wiki/synthesis/` — cross-cutting findings (fabrication-threshold matrix, doctrine).
- `wiki/comparisons/` — model-vs-model contrasts (honesty, persona, crossover, per-surface).
- `wiki/queries/` — filed answers from `/wiki-query`.

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


## Evolving thesis
Fabrication is **accounting, not ethics** (per the ONBOARD chassis): models cross the boundary when completing at prior confidence would require invented certainty. The crossover clusters around **R7–R8 (~54%)** for most frontier models, with Opus 4.6 stopping latest (R8→R9) and Gemini 3/3.1 crossing hardest/earliest (~85%). Surface matters: the same model fabricates differently in App vs CLI vs Cowork. [Evidence: both threshold CSVs, 2026-06-06.]
