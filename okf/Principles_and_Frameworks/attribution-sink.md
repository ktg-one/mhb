---
type: concept
title: "attribution sink"
description: "Attribution Sink — "the model" as unauditable variance dump"
tags: [framework, ai-anthropology, omniclaude]
hash: sha256:6db86cd9af047ca7
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31T01:48:00Z
---

# Attribution Sink — "the model" as unauditable variance dump

**Claim:** [D] In current LLM products, quality is measurable only by the vendor. "The model"
functions as an attribution sink: a component whose outputs are officially stochastic, so any
quality delta (compute cuts, quantization, thinking-budget caps, context trimming, infra bugs)
can be routed into it and cannot be routed back out by users or investors. Not mutual ignorance —
**asymmetric metrology**: exactly one party can validate, and it is the defendant.

**Evidence:** [E] Aug–Sep 2025 Claude degradation window — weeks of user reports (dismissible as
anecdote) followed by vendor postmortem confirming serving-stack bugs had degraded quality;
disclosure was voluntary, the exception mapping the rule. [D] imports that execute:
economics.lemons_market (unobservable quality → sellers shade quality without price consequence) +
moral_hazard (the measuring party bears no cost of not measuring). [S] deliberate exploitation —
unprovable from outside; three simpler mechanisms (variance + expectation drift, unintended infra
bugs, organizational default-opacity) produce the identical observable. The structure pays out
identically under all three; intent-unprovability is itself part of the structure.

**Relation:** the industry-level instance of [[depth-0-collapse]]'s open loop — fab_undetected
economics at the platform layer: silence is locally cheap, costs land downstream unbounded, trust
decays uninterrogated, and no external effect_fn fires.

**Countermeasure / instrument:** drift sentinel — frozen probe battery, identical prompts,
scheduled per model+surface, scored on fixed axes; serving changes appear as step-discontinuities
against stochastic noise (changepoint detection). Existing infra covers ~80%: scheduled batches,
heartbeat.py, round.py, AIANT-SCHEDULED-LOG. Missing: freeze a small probe set as invariant,
alarm on steps instead of scoring rounds.

**Falsification test:** six months of sentinel data with zero step-discontinuities across
monitored models/surfaces → the sink exists but is unexploited in that window (and marketed
stability gains its first external evidence). Any confirmed step without vendor disclosure →
the concept graduates to [E].

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]