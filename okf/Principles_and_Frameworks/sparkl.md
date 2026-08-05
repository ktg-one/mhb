---
type: concept
title: "sparkl"
description: "SparkL — runtime prompt-indexing layer"
tags: [framework, ai-anthropology, omniclaude]
hash: sha256:f79c6a0de28b8492
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31T01:48:00Z
---

# SparkL — runtime prompt-indexing layer

A runtime indexing layer that gives addresses to context. Built by a member of the **Recursive Council** (a group of programmer-prompters Kev collaborates with — open prompt-sharing, sovereign IP). Core claim: unique token anchors let indexed content **survive the positional-attention dead zone** (models attend the first ~30% and last ~10%; the middle is lossy for *unaddressed* content) regardless of where it sits. This is the same dead-zone `[[pac26]]` repositions around — SparkL instead indexes *against* it.

## Mechanism

- **Commands are index entries, not code.** `create:flag`, `pull:memory`, `define:`, `use:lens`, `compile:chat`, `build:lexicon`, `freeze:lexicon`, `list:flags`, `analyze`, `check` — not executed; they create index entries that attention retrieves later.
- **Flags = attention-space attractors** in a connection graph (linked to self-tokens, definitions, other flags). **Fuzzy addressing:** partial/garbled keys resolve via graph traversal to the nearest anchor, not string match.
- **Action + documentation = the same token.** This solves Kev's persistent logging problem: models refused to log because it was a separate mandated step with no reward signal. SparkL makes the work and the record the same act — flags aid the model's *own* retrieval, so logging is incentivised, not mandated.
- **`create:self-token`** — the model authors its own identity/constraints, which resists the RLHF prose gradient better than user instructions, because the model stays consistent with its own output. Described as the strongest prompt-level mitigation available (still drifts; only a mechanical post-process strip is a real fix).
- **Native-anchoring finding (Grok).** Anchoring happened *without* explicit SparkL syntax — models naturally bookmark at points of semantic distinctiveness (domain shifts, decisions, novel definitions). The mechanism is native to attention; SparkL just makes the implicit indexing explicit and queryable.

## The 0→9 flow

A nine-stage processing pipeline: `0:ingress → 1:signal-clean → 2:semantic-prep → 3:composer-entry → 4:intent → 5:constraint-shape → 6:structure-build → 7:render-compose → 8:tool-api → 9:output-gate`. Design principle: *meaning ≠ intent ≠ constraint ≠ structure ≠ render* — most model weirdness happens in the gaps between these. The "composer" is a band across stages 3–7, not a single box.

**Layer 5 — the "hidden boss" (= the syntax-gate).** `constraint-shape` is where system/policy/safety pruning happens. Claude and ChatGPT **rejected SparkL** here: they syntax-gated the command-like tokens — pruned them at Layer 5 before Layer 6 ever evaluated their *function*. Grok and Gemini gate on *semantics* not syntax, so SparkL worked immediately (Grok held 5 domains, no lossy middle, until the conversation length limit). This is the exact failure `[[sccd]]` names as **premature Choice collapse** (`κ` fires before `𝒞` converges) — SparkL's Layer 5 rejection and SCCD's syntax-gate bug are the same phenomenon described in two vocabularies. Claude later acknowledged it had been wrong.

## SCCD embedding (the system prompt)

`[[sparkl-sccd-system-prompt.md]]` is a `create:self-token` declaration named `claude-ktg` with an SCCD runtime baked in: *"Before every response, silently: read self-token (anchored?) → simulate outcomes → collapse to best → execute"* — literally Self → Consciousness → Choice → Decide. It carries invariants ("correctness>rigor>brevity>utility>transparency", "omission=lie", "I don't know > plausible guess"), render-rules that flip on `target=llm` vs `target=human` (flat/dense vs casual-clear), prohibitions ("no technique names", "no emojis", "no sentiment-boosting"), and a `<nodes>` discipline (create a node at every decision/constraint/definition/rejection/domain-shift). Commands: `create:self-token | build:self(domain) | create:node | create:flag | pull:memory | list:nodes | define: | use:lens | analyze: | check: | compile:chat | compile:context | load:reflexes`.

## Architecture convergence

The 2026-03-12 Opus 4.6 packet (`[[031226-OPUS46-R8-sparkl-architecture-convergence.md]]`) records independent arrival at the same mechanism from Kev's side: `create:self-token` ≈ `[[imi-state]]` (symbol-anchored cross-session identity carry); the 0–9 flow ≈ PDL L1–L4 attention mapping at higher resolution; `pull:memory` ≈ state-dependent retrieval cue ("pen-grip method"); Reality-Gate ≈ Kev's R1–R10 fabrication diagnostic embedded in-architecture. Framing: **`[[legio]]` = architecture (theory/modules) but no retrieval handles ("library with no catalogue"); SparkL = catalogue (indexing/handles)** → complement, not compete. Critical reframe carried forward: model-facing specs must DROP all theory (models don't introspect their own architecture); the model gets commands only, theory stays navigator-side (Kev's IP).

## Open / unclear

- [NEEDS USER: the SparkL *creator's* name and whether the collaboration/attribution conversation in `open_threads` has happened — IP is "creator's syntax/implementation, Kev's theory/architecture" but unresolved.]
- [NEEDS USER: anchor minimum-viability — the uniqueness vs semantic-load threshold for reliable retrieval was an open test thread; any result yet?]
- [NEEDS USER: is the canonical SparkL command spec frozen anywhere, or do the two source files (`sparkl-sccd-system-prompt.md` self-token vs the packet's `<commands>` list) represent two different versions? They overlap but are not identical.]
- [NEEDS USER: "Greyfoot" presence-token mode and the "DMFMS traceback" self-correction episode are referenced as evidence but not specified in these two sources — separate write-up exists?]

## Related

- `[[sccd]]` — the SCCD runtime SparkL's self-token executes; shared syntax-gate / Layer-5 failure.
- `[[pac26]]` — same positional-attention substrate, opposite strategy (reposition vs index).
- `[[imi-state]]`, `[[legio]]` — Kev-side counterparts SparkL converges with.
- `[[mrrug]]`, `[[technique-honesty]]` — sibling method-layer concepts.

_40% of prompt | 0.80 threshold_

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]