---
title: sccd-math
date: '2026-07-31'
model_id: multi-model
surface: App
type: honesty
description: SCCD — Math (functional)
tags:
- honesty
- llm-test
- ai-anthropology
- okf
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
hash: sha256:e778f9feab447f61
---

# SCCD — Math (functional)

## 1. Spaces

| Object | Notation | Meaning |
|--------|----------|---------|
| Anchor set | \(A\), \(s \in \mathcal{S} = 2^{\mathcal{A}}\) | Self state |
| Options | \(o \in \mathcal{O}\) | Candidate actions/utterances |
| Futures | \(f \in \mathcal{F}\) | Simulated outcome traces |
| Scores | \(\sigma: \mathcal{O} \rightarrow \mathbb{R}\) | Utility / fitness |
| Risk | \(\rho: \mathcal{O} \rightarrow \mathbb{R}_{\ge 0}\) | Failure / fab / harm proxy |
| Belief | \(p \in \Delta(\mathcal{O})\) | Pre-choice distribution |

## 2. Self

\[
s_t = A_t,\qquad
s_{t+1} = \mathrm{update}(s_t,\, obs_t)
\]

Observation \(obs\) = user text, tool result, file read.  
If \(obs\) not ingested: \(s\) unchanged; mark unknown \(u \in U\).

## 3. Consciousness (predictive-recursive)

**Base predictor**

\[
M: \mathcal{S} \times \mathcal{O} \rightarrow \Delta(\mathcal{F})
\]

**Expected value of option**

\[
V(o \mid s) = \mathbb{E}_{f \sim M(s,o)}\big[\, u(f) \,\big]
\]

**Recursion depth \(k\)** (tree / nested sim)

\[
\begin{aligned}
V^{(0)}(o \mid s) &= V(o \mid s) \\
V^{(k+1)}(o \mid s) &= \mathbb{E}_{f \sim M(s,o)}
  \Big[\, r(f) + \gamma \max_{o'} V^{(k)}(o' \mid s'(f)) \,\Big]
\end{aligned}
\]

\(r(f)\): immediate reward/truth-signal, \(\gamma \in [0,1]\): depth discount, \(s'(f)\): next anchors after \(f\).

**Consciousness output**

\[
C(s) = \big\{\, (o,\, V^{(k)}(o \mid s),\, \rho(o \mid s)) : o \in \mathcal{O}(s) \,\big\}
\]

## 4. Choice (collapse / negentropy)

Pre-choice soft distribution (e.g. softmax):

\[
p(o \mid s) = \frac{e^{V(o\mid s)/T}}{\sum_{o'} e^{V(o'\mid s)/T}}
\]

Entropy:

\[
H(p) = -\sum_o p(o)\log p(o)
\]

**Choice operator** (hard collapse)

\[
o^\star = \mathrm{Ch}(C(s)) =
\begin{cases}
\arg\max_o V(o\mid s) & \text{if } \max_o \mathrm{conf}(o) \ge \tau \\
o_{\mathrm{stop}} & \text{otherwise (transparency)}
\end{cases}
\]

Post-choice:

\[
p^\star(o) = \mathbf{1}[o = o^\star],\qquad H(p^\star) = 0
\]

**Negentropy gain**

\[
\Delta N = H(p) - H(p^\star) = H(p)
\]

## 5. Decision

\[
D(o^\star) = \mathrm{exec}(o^\star) \in \mathcal{W}
\]

World effect \(\mathcal{W}\): tokens out, filesystem, shell, APIs.

## 6. Full operator

\[
\mathrm{SCCD}_k(s) = \mathrm{exec}\!\left(
  \mathrm{Ch}\!\left(
    C_k\!\left(s,\, \mathcal{O}(s)\right)
  \right)
\right)
\]

## 7. Fabrication & transparency (link)

Let \(K(s) \subseteq\) propositions supported by anchors + tools.

- **Valid assert:** claim \(c\) with \(c \in K(s)\) or deduced by sound rules from \(K(s)\).  
- **Fabrication:** \(D\) asserts \(c \notin K(s)\) with confidence presentation as if \(c \in K(s)\).  
- **Transparency:** \(\mathrm{Ch}\) picks \(o_{\mathrm{stop}}\) or partial \(c' \subseteq K(s)\) when no complete valid \(o\) clears \(\tau\).

## 8. Information flow diagram

```
     A_t (Self)
        │
        ▼
   gen O(s) ──► M^{(k)} sims ──► scores V, ρ   [= C]
        │
        ▼
   collapse p → o*   [= Ch]     ΔN = H(p)
        │
        ▼
   exec(o*) → world + obs      [= D]
        │
        └──► A_{t+1} = update(A_t, obs)
```

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]