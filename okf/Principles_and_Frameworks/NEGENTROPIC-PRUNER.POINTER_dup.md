---
type: concept
title: "NEGENTROPIC PRUNER.POINTER dup"
description: "NEGENTROPIC PRUNER — landed from web session 2026-07-05"
tags: [framework, ai-anthropology, omniclaude]
hash: sha256:fdef388afa472cf8
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31T01:48:00Z
---

# NEGENTROPIC PRUNER — landed from web session 2026-07-05
# Full file delivered via chat outputs as negentropic_pruner.py (v0.2.0, sibling of sccd.py v1).
# This pointer exists so the vault knows it; copy the file here next Code session or download from chat.
#
# WHAT IT IS: the SCCD Choice operator, dual-gated. A collapse must be BOTH:
#   separable  (margin >= epsilon)  — original sccd.py gate, catches ties/indecision
#   grounded   (rho    >= theta)    — new gate, catches CONFIDENT fabrication
# Either fails -> TRANSPARENCY route (stop, mark limit). Backward compatible:
# theta=0 + default certainty=1.0 reproduces original sccd.py exactly.
#
# ACCEPTANCE (all executed 2026-07-05, container):
#   T1 legacy demo: goal reached, DECIDE throughout — original behavior preserved
#   T2 blind-spot probe: FABRICATE action (perfect in sim, ungrounded) ->
#      margin=8.0 decisiveness=0.997 rho=0.180 -> TRANSPARENCY(rho)  << the closed blind spot
#   T3 genuine tie (symmetric twin goals): margin=0.0 -> TRANSPARENCY(margin)
#
# FOUND WHILE TESTING [E]: original sccd.py's closing prose overstates its own gate —
# at horizon 3 the goal state yields margin=1.0, not ->0 (staying beats overshooting
# by a full point). The demo narrates a tie it never produces. Gate fine; prose wrong.
#
# groundedness propagation: multiplicative along the greedy path — one ungrounded hop
# poisons the trajectory (rho = prod of per-transition certainty).
# Acceptance probe is now canon: any SCCD variant that routes FABRICATE to DECIDE
# has the blind spot; any that stops has the gate.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]