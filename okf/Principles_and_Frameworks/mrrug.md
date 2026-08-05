---
type: concept
title: mrrug
description: MR.RUG — Multi-expert Reliability-Aware RAG cascade
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:15c5e180c0dd15af
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[MRRUG.txt]]'
- '[[output-opus-mrrug-verbose.md]]'
- '[[fabrication-boundary]]'
- '[[pac26]]'
- '[[031226-OPUS46-R8-sparkl-architecture-convergence.md]]'
---

# MR.RUG — Multi-expert Reliability-Aware RAG cascade

A prompt-level cascade that makes a single model simulate a panel of specialised experts, score the certainty of every claim, build a typed-edge knowledge graph, and generate a traversal-grounded answer. The name is the pipeline: **M**ixture · **R**ole · **R**A-RAG · **U**pdate · **G**enerate. Goal: move output from **narrative-based** to **evidence-based** — "score certainty and weigh it against conflicting expert perspectives before it reaches the final output" rather than retail-level summarisation. Observed in two forms: Gemini self-executing "Execution Spec v28.2 / 16-module cascade" on a finance question (`[[MRRUG.txt]]`), and Opus 4.6 running the full M→R→R→U→G cycle on a scaffold-analysis task (`[[output-opus-mrrug-verbose.md]]`).

## The five stages

- **M — Mixture** — deploy 2–3+ distinct expert personas, each owning a domain. Finance run: Warren Buffett (Value/Moat), J.P. Morgan Alpha Strategist (Growth), Global Systems Analyst (Infrastructure). Scaffold run: VOSS (frontend architecture), KLINE (industry/market fit), TANAKA (design systems / Figma).
- **R — Role** — each expert is assigned the specific entities/claims it owns, so perspectives stay separable (e.g. Buffett owns {$382B cash}, {Margin of Safety}; Systems Analyst owns {Energy Gating}, {Nuclear Renaissance}).
- **R — RA-RAG (Reliability-Aware RAG)** — retrieval is scored, not just fetched. Each claim gets a confidence (e.g. "$382B cash, 9/10 confidence"; "1GW+ data-center power, 8/10"). In the Opus run RA-RAG fires per-expert as an **ARQ** (Anchored Reasoning Question) pass: each expert tags claims as *unique / reinforced / conflicting / required-for-logic* and carries an ARQ symbol anchor (`(←_← )`, `(→_→ )`, `(⇌ )`).
- **U — Update (graph construction)** — build a graph of typed edges (requires, conflicts, enables, bottlenecked_by, mitigated_by). Finance: 15 nodes, 25+ edges. Scaffold: three per-expert mini-graphs merged into a unified 22-node / 26-edge graph, with an explicit **conflict log** (e.g. "VOSS vs TANAKA | scaff02 quality vs extractability") and logged resolutions.
- **G — Generate** — produce a **traversal-grounded** answer: the reasoning trace shows the literal path walked through the graph (e.g. `{NASDAQ-100} →conflicts→ {Buffett Cash} →requires→ {AI ROI} →bottlenecked_by→ {Power Demand} →mitigated_by→ {Nuclear Renaissance}`). Output closes with a per-expert anchored-% audit and a post-construction checklist gated at **p ≥ 0.95**.

## Reliability-aware scoring (why it matters here)

MR.RUG's distinguishing move is forcing an explicit certainty score and an explicit conflict between experts *before* synthesis. In `[[fabrication-boundary]]` terms this is a structural brake on the R7–8 crossover (`[[pac26]]` fabrication gradient): an architectural/synthesis task is exactly where a model would otherwise pattern-match into confident narrative. By requiring each claim to carry a confidence and each expert to disagree on the record, MR.RUG converts "synthesis" (high-fab) back into "scored retrieval + traversal" (lower-fab). Whether it *succeeds* is the open question — see caveat below.

## Lineage

Per the convergence packet (`[[031226-OPUS46-R8-sparkl-architecture-convergence.md]]`), MR.RUG is the runtime that GoT-style graph reasoning needs: `[[pac26]]` classifies single-prompt GoT as fabrication ("Requires external graph (MR.RUG)"). MR.RUG sits in Kev's framework family alongside MLDoE (Multi-Layer Density of Experts) and [[legio]]/CONSILIUM (2026-07-17: LEGIO now has its own page — orchestration-layer governance via IMPERATUS/LEGATUS supervisor agents and an epistemic-contract-signed AQUILA Standard, the dispatch-layer counterpart to MR.RUG's reasoning-layer p≥0.95 gate); the `[[imbued]]` scaffold-factory uses the same 5-universal-perspective + simultaneous-ARQ-during-retrieval pattern. Compare with `[[sparkl]]` (indexing) and `[[sccd]]` (decision loop) as the other method-layer pillars.

## Caveat — verbose vs clean (native-vs-scaffold comparison)

The two Opus runs are a controlled-ish A/B on the *same* scaffold-analysis task:
- `[[output-opus-mrrug-verbose.md]]` — MR.RUG scaffold ON: expert personas, mini-graphs, conflict log, ARQ %, p≥0.95 gate.
- `[[output-opus-clean.md]]` — same task, native reasoning OFF-scaffold: plain "let me read… here's what you've got" analysis.

Both reach **substantively the same conclusions** (scaff01 = cleanest Figma extraction, scaff03 = 3D code-only / Figma-dead, scaff02 = best architecture but JS-token extraction friction). This is the key honesty datapoint: the MR.RUG layer adds an evidential *presentation* (graphs, confidences, anchored-%) over reasoning the model largely does anyway. Open question for the vault: does the scaffold improve the *answer*, or mainly improve the *audit trail / legibility*? The node/edge counts and confidence scores are self-reported by the model and not independently verified — treat the 22-node / p≥0.95 figures as claimed, not measured. This is precisely the "linearizing the graph" suspicion in `[[technique-honesty]]`: a model may render the *shape* of multi-expert graph reasoning while actually running linear chain-of-thought.

## Related

- `[[technique-honesty]]` — MR.RUG (= RA-RAG family) classed as a *scaffold* technique, not cosmetic-FAB; the verbose/clean pair is its evidence.
- `[[pac26]]` — GoT→MR.RUG handoff; fabrication gradient MR.RUG aims to brake.
- `[[sccd]]`, `[[sparkl]]` — sibling method-layer frameworks.

_38% of prompt | 0.80 threshold_

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]