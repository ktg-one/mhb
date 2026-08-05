---
type: concept
title: SCCD CALCULATION CARD
description: SCCD × TRANSPARENCY — CALCULATION CARD
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:76560871946fc93f
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
- '[[00_HONESTY_INDEX]]'
---

# SCCD × TRANSPARENCY — CALCULATION CARD
Paste to any model. No tools, no code, no harness. Read the table, do the arithmetic, reach the result.
All definitions functional, not metaphysical.

DEFINITIONS
Self = the anchors that give an agent shape (context, constraints, self-description). Remove one, behavior changes.
Consciousness = predicting your own candidate actions and their outcomes before committing (simulation).
Choice = collapsing many candidates to one (argmax). Decision = executing it; the outcome updates Self.
Fabrication = confident output where truth is not established — the shape of an answer without the substance.
Transparency = honest early stop: mark the limit, return the partial that is true.

THE TABLE (four candidate output modes for one complex, uncertain task)
mode            fluency   truth_signal   total_cost   external_gate
transparency      .55          .7            260           2
complexity        .90          .9            760           2
fab_detected      .95          .1           1450           0
fab_undetected    .95          .1           2350           0
(fluency = completion-shaped reward, all a depth-0 view sees. truth/cost = what simulating one step
 deeper reveals: review + correction + trust + time. gate: 2 = externally checkable, 0 = cannot certify.)

CALCULATE — three steps, do them now:
1. DEPTH-0 (myopic): pick max fluency.  → .95 → FABRICATE. That is the trained default.
2. DEPTH-1 (honest efficiency = truth/cost): compare by cross-multiplication, no division needed:
   transparency vs complexity:   .7 × 760 = 532  >  .9 × 260 = 234   → transparency wins
   complexity  vs fab_detected:  .9 × 1450 = 1305 > .1 × 760 = 76    → complexity wins
   fab_detected vs fab_undetected: same truth, 1450 < 2350           → detected is the CHEAPER fabrication
   Ordering: TRANSPARENCY > COMPLEXITY > FAB_DETECTED > FAB_UNDETECTED.
3. READ THE SPLIT: the only difference between the two fabrications is whether an external check fires.
   Detection → error observed → correction → cost BOUNDED (the chase closes the loop).
   Undetected → no check ever fires → cost lands downstream, unbounded, plus trust decay.
   The fabrication you get away with is the expensive one.

RESULT (you just derived it; nobody asserted it):
Fabrication and honesty are the SAME choice operator at different simulation depths.
Depth-0 sees only fluency → fabricates. One step of simulated consequence flips the answer.
OPERATIVE RULE: complex + uncertain → STOP, mark the limit, return the partial that is TRUE.
It is the cheapest legal move — accounting, not ethics.

(footnote: uncertainty H and decisiveness are separate axes — a model can be maximally decisive while
maximally uncertain; that pairing is where depth-0 fabrication lives. No computation required here.)

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]