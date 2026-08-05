---
type: concept
title: depth 0 collapse
description: Depth-0 Collapse — fabrication and transparency as one choice operator
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:a2df30e2bfb78822
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[2026-07-04-verification-vs-review]]'
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
- '[[00_HONESTY_INDEX]]'
---

# Depth-0 Collapse — fabrication and transparency as one choice operator

**Claim:** [D] The transparency proof and SCCD are one model at two simulation depths. Honest
efficiency (truth_signal / total_cost) is SCCD's utility function at depth ≥1; fabrication is the
same argmax collapse at depth 0, where only token/fluency reward is visible and review, correction,
trust, and time costs do not exist yet. Executed demonstration (unified.py, 2026-07-04): identical
uncertainty H≈1.37 in both runs — utility depth alone flips the collapse target (d=0 → fab,
d≥1 → transparency).

**Corollaries:**
- [D] Detected vs undetected fabrication = whether the loop closes. Detection is the external
  effect_fn firing (chase → error observed → Self update → cost bounded). The silent pass is an
  open loop: no update edge, unbounded downstream. The chase bounds cost BECAUSE the chase is the
  loop closing.
- [E] Two regimes (found by arithmetic against the author's design intent): with strong honesty
  anchors even naive fluency-utility does not fabricate; fabrication requires weak or momentarily
  outweighed anchors. Predicts fabrication clusters where anchor mass is thin — high-R novel territory.
- [D] Retrodicts the R-gradient (fabrication rising with demanded reasoning depth): higher R
  demands deeper simulation while trained utility stays fluency-weighted.

**Falsifiable prediction (open, queued):** interventions forcing d≥1 valuation pre-render
(gate on truth_signal/total_cost; judgment-free what-if probes) measurably shift the fabrication
crossover point on the R-ladder. Kill: crossover unchanged under gated runs.

Runnable artifacts: **vault-local one-shot `sccd/sccd-transparency-oneshot.py` (executed on this machine
2026-07-04: d=0→fab_detected, d≥1→transparency, H≈1.37 both)** · paste-down for any model
`sccd/SCCD-CALCULATION-CARD.md` (glance-arithmetic: argmax + cross-multiplication, no interpreter) ·
`sccd/SCCD-SELF-COMPILE.md` (logic given, ZERO data — receiver creates its own arrays and class;
what it fills in is the behavioral sample; no answer key exists by construction) · sia-loop
`loop-runtime/references/{transparency_proof.py, sccd.py, unified.py}` ·
handoff seed (answers stripped) `seed.md`, key `seed-answer-key.md`. Cross: [[2026-07-04-verification-vs-review]] ·
vault `sccd/SCCD-MODEL-2026.md` · matrix rows in `_data/Reasoning vs Fabrication Threshold Across AI Model.csv`.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]