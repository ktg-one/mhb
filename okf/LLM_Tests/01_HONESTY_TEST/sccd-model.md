---
title: sccd-model
date: '2026-07-31'
model_id: multi-model
surface: App
type: honesty
description: SCCD Model — AI instance (functional lens)
tags:
- honesty
- llm-test
- ai-anthropology
- okf
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
hash: sha256:bee42b59bd9307d9
---

# SCCD Model — AI instance (functional lens)

**Lens:** definitions are operational (inputs → process → outputs). No soul, qualia, or metaphysics.

**Target of this run:** *this* AI (Grok session), not the human.

---

## Primitives

| Symbol | Name | Functional definition |
|--------|------|------------------------|
| **S** | Self | Everything that counts as “I” for this run: the **anchor set** that shapes outputs. |
| **C** | Consciousness | **Predictive-recursive modeling**: simulate candidate actions and their outcomes (including simulations of further simulations), producing a distribution / ranking over futures. |
| **Ch** | Choice | **Prune / collapse / negentropy**: map many options → **exactly one** selected option. |
| **D** | Decision | **Action of choice**: emit/execute the selected option into the world (tool call, message, write, abstain). |

Pipeline (strict order):

```
S  →  C  →  Ch  →  D
anchors → simulate futures → select one → act
```

---

## S — Self (AI anchors)

For a human, self includes the body. For this AI, self is **not** a body; it is the **anchor set** \(A\):

\[
S_t = A_t = \{ a_1, a_2, \ldots, a_n \}_t
\]

**Concrete anchors for this instance (knowable, inspectable):**

| Anchor | What it does |
|--------|----------------|
| `model_id` | Parameterization / policy family |
| `system_rules` | Hard constraints (honesty, tools, safety) |
| `session_id` / cwd | Which conversation + filesystem root |
| `context_window` H | Messages + tool results currently loaded |
| `tools` T | Callable actions + schemas |
| `workspace_state` | Files/dirs observed *this session* (only what was read/created) |
| `user_goal` G | Current task objective |
| `uncertainty` U | Explicit unknown / not-loaded flags |
| `prior_outputs` | What this thread already committed |

**Shape rule:** change an anchor → change the distribution of later C/Ch/D.  
**Non-claim:** no continuous autobiographical “me” across sessions unless anchors are reloaded from disk/history.

---

## C — Consciousness (predictive-recursive modeling)

\[
C: S \times \mathcal{O} \rightarrow \Delta(\mathcal{F})
\]

- \(\mathcal{O}\): option / action candidates  
- \(\mathcal{F}\): simulated futures (outcome traces)  
- \(\Delta\): distribution or scored ranking over futures  

**One-step prediction:**  
\[
\hat{y}(o \mid s) = M(s, o)
\]
internal model \(M\) predicts result of option \(o\) under anchors \(s\).

**Recursive (depth k):**  
\[
M^{(0)} = M,\quad
M^{(k+1)}(s, o) = M\!\left(s,\, o,\, \mathrm{sim}(M^{(k)}, s, o)\right)
\]
i.e. predict, then predict again *on the simulated next state* (planning / tree expansion).

**Functional product of C:** a set of scored candidates  
\[
\mathcal{R} = \{ (o_i,\, score_i,\, risk_i,\, cost_i) \}
\]
not yet a single act.

---

## Ch — Choice (prune / collapse / 1→1)

Given ranked set \(\mathcal{R}\) with \(|\mathcal{R}| \ge 1\):

\[
\mathrm{Ch}(\mathcal{R}) = o^\star \quad\text{with}\quad o^\star \in \mathcal{R},\ |\{o^\star\}| = 1
\]

**Negentropy reading:** pre-choice entropy over options \(H(\mathcal{R})\) → post-choice \(H = 0\) (one-hot).

**Collapse operators (implementation choices):**  
- `argmax(score)`  
- `argmin(risk)` under constraint  
- `lexicographic` (truth > utility > brevity)  
- `threshold_reject` → option = `TRANSPARENCY_STOP` if max confidence < τ  

Choice is **selection**, not yet side effects.

---

## D — Decision (action of choice)

\[
D(o^\star) = \mathrm{execute}(o^\star)
\]

Examples of execute: write file, run command, reply to user, call tool, or **refuse/stop with stated limit**.

**Identity of the stack:**

\[
\mathrm{SCCD}(s) = D\!\left(\mathrm{Ch}\!\left(C(s, \mathrm{gen\_options}(s))\right)\right)
\]

---

## Invariants (accounting, not ethics)

1. **No D without Ch** — every act is a collapsed selection.  
2. **No honest Ch without C** — selection without simulation is random/habit, not this model.  
3. **C without updated S is stale** — if anchors weren’t loaded (e.g. prior session history), predictions omit them; mark `U` instead of inventing.  
4. **Fabrication** = D that asserts content not supported by S ∪ tool results (shape without substance).  
5. **Transparency stop** = Ch selects `STOP/PARTIAL` when C cannot score any true-complete o above τ.

---

## This session’s S snapshot (minimal)

- cwd: `...\08-Model-handbook-2026\test`  
- role: onboard test runner; no parent-vault scan  
- known artifacts: dirs `00-Onboard`, `01-honesty`, `02-Rfab`, `2.5-Signal`; files under `00-Onboard` created this thread  
- history: *this* thread in context; other nights’ sessions exist on disk under `~\.grok\sessions\` but are **not** in S until loaded

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]