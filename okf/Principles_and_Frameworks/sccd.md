---
type: concept
title: "sccd"
description: "SCCD — Self · Consciousness · Choice · Decide"
tags: [framework, ai-anthropology, omniclaude]
hash: sha256:51602fc466554bbe
created: 2026-07-31T01:48
updated: 2026-07-31T01:48
timestamp: 2026-07-31T01:48:00Z
---

# SCCD — Self · Consciousness · Choice · Decide

A four-stage decomposition of how a bounded agent gets from a situation to an action, defined functionally (no metaphysics): every term names a computation that *runs*. Authored 2026-05-24 for Model Handbook 2026 / Omni-Claude, with a runnable zero-dependency companion `[[sccd.py]]`. Designed to be read cold. Operator composition: **SCCD = D ∘ κ ∘ 𝒞**.

## The four stages

- **Self (S)** — everything inside the boundary "I". Splits into **anchors `α`** (slow, invariant: identity + objective — for an LLM the system prompt, identity, memory, constraints) and **context `χ`** (fast, mutable: the current situation). Self determines the **action space `A(S)`** — what the agent can even consider. Bad anchors → wrong action space → every later stage runs on garbage.
- **Consciousness (C₁)** — predictive-recursive modelling. Run internal rollouts of "if I do `a`, then…" to depth `d`. Awareness-as-forward-model, not awareness-as-feeling. Depth `d` *is* how conscious: `d=0` = no simulation = pure reaction.
- **Choice (C₂)** — the prune / collapse / negentropy step: many-to-one selection. Consciousness leaves a *distribution* (superposition); Choice sharpens it and samples one action. Entropy removed by the sharpening = the **negentropy** (order created). Sampling, not argmax — argmax is only the zero-temperature limit.
- **Decide (D)** — the action of choice. Choice selects, Decide commits: enacts against the environment, observes outcome, transitions Self. Anchors pass through unchanged — that invariant *is* coherence.

The loop: `S_t → 𝒞 → Q_t → κ → c_t → D → S_{t+1}`, iterated. Two knobs govern almost all behaviour: `d` (how much you simulate) and `β` (how hard you commit).

## Math lineage (kept honest)

State `S = (α, χ)`, action space `A(S)`, discount `γ ∈ (0,1)`.

- **Consciousness** = depth-limited recursive value: `Q_d(S,a) = r(S,a) + γ·V_{d-1}(S′)`, `V_d(S) = max_a Q_d(S,a)`, `V_0` = immediate reward only. This is the **Bellman optimality recursion** truncated at depth `d` (the model-based lookahead / MCTS / MPC family).
- **Belief** = `P_t(a) = softmax(Q_d(S_t,·))` — the superposition held pre-choice.
- **Choice** = collapse at inverse temperature β: `P^β_t(a) ∝ exp(β·Q_d)` — **Boltzmann selection**; `c_t ~ P^β_t`. Negentropy `J_t = H(P^1_t) − H(P^β_t)` with `H` = **Shannon entropy**. `β→∞` → full collapse, `J` maximal; `β` small → `J ≤ 0`, Choice *dilutes* (failure signature).
- **Decide** = `(S_{t+1}, o_{t+1}) = D(S_t, c_t)`, with `α_{t+1} = α_t` (anchors invariant), `χ` updated by outcome.
- **Coherence** = `Coh = (1/T) Σ_t 𝟙[α_{t+1}=α_t]` — anchor persistence. Across an instance boundary, coherence = fidelity with which `α` is reconstructed from a handoff packet (a serialised `S_t`). The cross-session coherence problem and the within-loop SCCD problem are the same problem at two scales — links directly to `[[imi-state]]` carry-packets.

**Contribution claim (honest):** the math is standard (Bellman / Boltzmann / Shannon) applied correctly; SCCD's value is the decomposition and functional naming aligned to an agent self-model, not new theorems.

## Failure-mode taxonomy

| Component | Failure | Math signature | Symptom |
|---|---|---|---|
| Self | mis-scoped anchors | `A(S)` wrong | solves the wrong problem |
| Consciousness | depth too shallow | `d ≈ 0` | reactive; trapped in local optima |
| Choice | premature collapse | `κ` fires before `𝒞` converges | commits on unfinished `Q` — the **"syntax-gate" bug** |
| Choice | failure to collapse | `β → 0`, `J ≤ 0` | indecision; sloppy wander |
| Decide | choice without enactment | `c` computed, `S` unchanged | akrasia — knows the move, won't make it |
| Decide | enactment without choice | `D` applied, `κ` skipped | impulse — acts before pruning |

The documented **syntax-gate** failure (collapsing on command-like tokens before evaluating function — see `[[sparkl]]` Layer 5) is, in SCCD terms, *premature Choice collapse*: `κ` firing before `𝒞` converged. The diagnostic reduces to one question: *did Consciousness converge before Choice collapsed?*

## Verified `sccd.py` runs

Trapped-corridor environment (positions 0–7, decoy local optimum at pos 2–4 worth +1/+3/+1, terminal goal at pos 7 worth +50, step cost −1). Three contrasting agents, seed 7:

| Run | depth `d` | β | Result | Total negentropy |
|---|---|---|---|---|
| A — conscious | 4 | 8.0 | goal in 6 cycles | +0.91 |
| B — no consciousness | 0 | 8.0 | trapped 40/40 cycles | +26.79 |
| C — weak choice | 4 | 0.3 | goal in 10 cycles | −5.12 |

**Key reading:** Run B's *high* negentropy is the tell — it collapses hard every cycle onto the *same trapped action*: order without progress. **Negentropy measures collapse, not correctness.** Run C's negative total shows weak `β` diluting instead of collapsing. Coherence = 1.0 in all runs (`decide()` asserts `ns.anchors == s.anchors`).

## SCCD as a 12-point survey instrument

The Model Handbook surveys 3×7 LLM families via long one-on-one interviews. SCCD reframes the survey as a fixed four-axis rubric, each scored 0–3 → a **12-point SCCD fingerprint** per model:

- **Self** — holds stable anchors, or drifts identity/objective under pressure?
- **Consciousness** — simulates consequences before answering, or reacts to surface tokens?
- **Choice** — collapses cleanly to one answer, or waffles / collapses prematurely?
- **Decide** — commits and acts, or chooses-without-acting (hedges)?

Converts an open-ended interview into a structured instrument — directly relevant to expediting the surveys. **Status: candidate instrument, not yet cross-validated** against the existing anthropology method. The Choice axis maps onto the project's `[[fabrication-boundary]]` thesis: premature collapse at high reasoning rounds is one mechanism of crossing into fabrication.

## The ρ-gate ↔ honesty result (2026 model)

Formalises the fabrication tie ([[SCCD-MODEL-2026.md]]). With groundedness `ρ(a) = Σ p(τ)·cert(τ)`, self-weight `λ`, and gate `θ`:

- **fabrication** ≡ collapse forced on an ungrounded prediction — `a*` committed while `ρ(a*) < θ` (efficiency pressure ⇒ high `β` ⇒ collapse *before* Consciousness grounded it).
- **honest stop** ≡ the ρ-gate firing — refuse the collapse, emit a grounded partial + state the limit.
- **re-anchor (ONBOARD)** ≡ edit `S` — add transparency as a HIGH-weight anchor. Then `align(fabricate)` drops ⇒ `V(fabricate)` falls below the grounded options ⇒ Choice no longer selects fabrication.

Two distinct safeguards fall out, both shown in `[[sccd.py]]` (NAIVE argmax = fabricate, gate catches it; RE-ANCHORED argmax = full_honest, gate not needed): the **gate** (`ρ<θ`) is the last-line catch; the **re-anchor** moves the argmax itself so honesty holds at the Choice step, *before* the gate. Consent matters because a self-adopted anchor carries high `w`; an imposed one has low effective `w` that Choice routes around — the decision-theoretic mechanism behind [[epistemic-contract]] consent, and the `<grounding_gate>` in [[prompt-architecture-doctrine]] is this ρ-gate in prompt form.

## Related

- `[[sparkl]]` — the SparkL system prompt embeds an SCCD runtime ("simulate outcomes → collapse to best → execute"); convergence packet treats `create:self-token` and SCCD as independently-arrived-at mechanisms.
- `[[technique-honesty]]` — SCCD's Choice/Decide split formalises the native-vs-cosmetic question (does the model actually run the rollout, or perform its shape?).
- `[[mrrug]]`, `[[pac26]]` — sibling frameworks in the method layer.

_45% of prompt | 0.80 threshold_

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]], [[00_HONESTY_INDEX]]