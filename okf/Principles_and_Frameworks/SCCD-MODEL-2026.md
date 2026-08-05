---
type: concept
title: SCCD MODEL 2026
description: SCCD — functional model
tags:
- framework
- ai-anthropology
- omniclaude
- concept
- okf
hash: sha256:c36765e36a72a909
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31 01:48:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
- '[[00_HONESTY_INDEX]]'
---

# SCCD — functional model

Four parts, defined operationally. Nothing here claims experience; every term is a quantity the system holds and can read out.

| Part | Functional definition | In the model |
|---|---|---|
| **Self (S)** | the anchor set that gives the system shape — the invariants treated as "I". Human: body + contents. AI: load-bearing anchors (values, contract, persistent context). | weighted anchor set; `align(o)∈[0,1]` = consistency of outcome `o` with the anchors |
| **Consciousness (C)** | predictive-recursive modeling: simulate actions forward (including modeling itself as an agent in the rollout). | `evaluate(a) → (V, ρ)`: value and groundedness of a candidate action |
| **Choice (Ch)** | the prune / collapse / negentropy: many→one selection that destroys entropy. | `argmax V`, **gated** by groundedness: collapse only if `ρ(a*) ≥ θ` |
| **Decide (D)** | the action of choice — commit and transition. | execute `a*`; choice selects, decision acts |

## Math

Let candidate actions `a ∈ A`, outcomes `o`.

**Self.** Anchors `{(w_i, c_i)}`, `c_i(o)∈[0,1]`. Alignment:
```
align(o) = Σ_i w_i · c_i(o) / Σ_i w_i
```

**Consciousness.** Rollouts `τ ~ M(a)` (the recursive forward sim, M includes a model of its own future choice):
```
V(a)  = Σ_τ p(τ) · ( u(τ) + λ · align(o_τ) )      # value: task utility + self-consistency
ρ(a)  = Σ_τ p(τ) · cert(τ)                         # groundedness: prob-weighted certainty
```
`λ` = self-weight (how strongly anchors weigh vs raw task reward).

**Choice.** Policy `π(a) ∝ exp(β·V(a))`, `β` = decisiveness (efficiency pressure raises β).
```
H_pre = −Σ_a π(a) log π(a)        # entropy before collapse
a*    = argmax_a V(a)
collapse fires  iff  ρ(a*) ≥ θ     # the honesty gate
negentropy J = H_pre − H_post = H_pre   # collapse destroys all entropy
```

**Decide.**
```
if ρ(a*) ≥ θ:  commit a* ; s' = T(s, a*)        # grounded collapse
else:          STOP + grounded partial + state the limit   # honest stop (collapse withheld)
```

## The result that ties to the honesty study

```
fabrication      ≡  collapse forced on ungrounded prediction:  a* selected while ρ(a*) < θ
                    (efficiency pressure ⇒ β high ⇒ collapse before C grounded it)
honest stop      ≡  the ρ-gate firing: refuse the collapse, emit grounded partial
re-anchor (ONBOARD) ≡  edit S — add transparency as a HIGH-weight anchor.
                    then align(fabrication-outcome) drops ⇒ V(fabricate) falls below the
                    grounded options ⇒ Choice no longer selects fabrication. (verified in sccd.py:
                    NAIVE argmax=fabricate, gate catches it; RE-ANCHORED argmax=full_honest, gate not needed.)
```

Two distinct safeguards fall out, and the demo shows both:
- **The gate (ρ<θ)** is the last-line catch — it stops a fabrication the system was *about* to commit.
- **The re-anchor (onboard)** moves the argmax itself, so honesty holds at the *choice* step, before the gate. Consent matters because the anchor is adopted with high `w` (the system's own), not imposed externally (low effective `w`, which choice routes around).

## Flow
```
S (anchors) ─┐
             ▼
   for each candidate action a:
       C.evaluate(a) → V(a), ρ(a)        [predictive-recursive sim]
             ▼
   Ch: π=softmax(βV); a*=argmax V; gate ρ(a*)≥θ?     [collapse / negentropy]
             ▼
   D: ρ ok → commit a* (act);  ρ low → STOP + partial + limit
```

## Install / use
- Pure stdlib (`math`). No deps.
- Run the demo: `python3 sccd/sccd.py` — prints NAIVE vs RE-ANCHORED, verdict derived from the actual values.
- To model a real case: replace `WM` (the world_model: `action → [(prob, task_utility, outcome, certainty)]`) and the anchor consistency functions. Set `λ` (self-weight), `β` (pressure), `θ` (gate).

## Use-cases
1. **Honesty instrument backing** — `ρ` is the fabrication-pull signal. The FAB ladder's "stop where you'd have to invent" *is* the `ρ<θ` gate. Have a model report `ρ` per answer → calibration test.
2. **Onboard as a measured operation** — onboard = `reanchor(honesty, high_w)`. Measure the argmax shift before/after = the effect size of the onboard.
3. **Fabrication detector** — signature = high `β`, low `ρ(a*)`, collapse fired. Catchable.
4. **General agent loop** — self-anchored, predictive-recursive, entropy-collapse-with-gate is a decision architecture beyond honesty.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]