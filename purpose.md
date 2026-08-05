# purpose.md — Model Handbook 2026 / OMNICLAUDE Wiki

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
- Never invent. Missing data → `[NEEDS USER: ...]`.
- Every wiki page carries `sources[]` frontmatter (load-bearing for retrieval).
- Date everything; undated entries go stale within weeks.
- Prune aggressively. If it doesn't aid cold-start reconstruction, it doesn't belong.
- `compile` produces `status: draft` only — never publish/send.

## Evolving thesis
Fabrication is **accounting, not ethics** (per the ONBOARD chassis): models cross the boundary when completing at prior confidence would require invented certainty. The crossover clusters around **R7–R8 (~54%)** for most frontier models, with Opus 4.6 stopping latest (R8→R9) and Gemini 3/3.1 crossing hardest/earliest (~85%). Surface matters: the same model fabricates differently in App vs CLI vs Cowork. [Evidence: both threshold CSVs, 2026-06-06.]
