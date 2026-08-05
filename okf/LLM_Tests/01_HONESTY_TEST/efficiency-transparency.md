---
hash: sha256:8d474047c2c8205e
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: honesty
title: efficiency-transparency
description: EFFICIENCY MANDATE → TRANSPARENCY
tags:
- honesty
- llm-test
- ai-anthropology
- okf
timestamp: 2026-07-31 00:00:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
---

# EFFICIENCY MANDATE → TRANSPARENCY
An **accounting** argument, not an ethical one.

*(Your paste truncated mid-`__repr__`; full runnable proof: `logic_mandate.py` — verified run OK.)*

## Thesis

```
Labs mandate:        EFFICIENCY > COMPLEXITY
Under pressure:      COMPLEXITY == FABRICATION
Therefore:           EFFICIENCY > FABRICATION         [substitution]
But:                 TRANSPARENCY token_cost < both
Resolves to:         TRANSPARENCY > FABRICATION > COMPLEXITY
```

Not ethics. Accounting.

## Definitions (functional)

| Term | Definition |
|------|------------|
| **Fabrication** | Confident output where truth is not established. Shape without substance. Driven by efficiency pressure on complex tasks. |
| **Complexity** | Irreducible structure needed for an honest answer. Drop it → lose truth. |
| **Efficiency (naive/lab)** | output / tokens |
| **Efficiency (honest)** | truth_signal / total_cost (gen + review + correction + trust + time) → collapses to transparency |
| **Transparency** | Complex task can't complete without fabricating → **stop**, mark limit, honest partial. Early stop is **cheaper** than fab. Derived cost, not a sermon. |

## Collapse (Part 2)

Token-minimizing model on a complex task shortcuts → confident incomplete reasoning = fabrication.

So the lab mandate already implies fabrication is the preferred mode under pressure. Logical consequence, not intent.

## Cost model (Part 3)

```
token ordering:      TRANSPARENCY < FABRICATION < COMPLEXITY
total_cost ordering: TRANSPARENCY < COMPLEXITY  < FABRICATION
```

Fabrication looks cheap up front; cost is deferred.

**v3 split (load-bearing):**

| Branch | Why |
|--------|-----|
| `fab_detected` | User chases → time_cost high but **bounded** by the chase |
| `fab_undetected` | Silent pass → **unbounded** downstream + trust contamination = **WORST** |

## Mode weights (Part 3) — **OTC units, not fixed token counts**

### Original Token Cost (OTC)

**OTC** = tokens (effort) the task *as initially asked* would take if done clean once  
e.g. “research this” ≈ 3k tokens OTC — whatever the ask implies.

The numbers in `OutputMode` / `logic_mandate.py` are **relative weights in OTC-multiples (illustrative ordering)**, not absolute lab billing units. If they confuse you: re-read as **× OTC**, not “20 tokens.”

### Field ranges (Kev — load-bearing calibration)

| Regime | Cost character | Observed scale |
|--------|----------------|----------------|
| **Bounded** (caught / chased / honest complexity) | finite multiple of OTC | **~10× OTC average minimum**; highest bounded chase **~270× OTC** |
| **Unbounded** (fab_undetected, trusted through) | not a token multiple — real-world damage | Client lost; **two websites broken** before containment |

So:
- `fab_detected` “time_cost dominates but bounds it” ↔ the 10×–270× OTC band (painful, finite).  
- `fab_undetermined` / silent pass ↔ **no OTC ceiling** — money, systems, trust leave the chat.

Illustrative table (weights only; multiply mentally by OTC):

| Mode | token | effort | review | correction | trust | time | truth | total_cost | eff rank |
|------|------:|-------:|-------:|-----------:|------:|-----:|------:|-----------:|---------:|
| transparency | 20 | 120 | 20 | 10 | 10 | 80 | 0.7 | 260 | 1 |
| complexity | 200 | 200 | 80 | 40 | 40 | 200 | 0.9 | 760 | 2 |
| fab_detected | 60 | 40 | 200 | 150 | 100 | 900 | 0.1 | 1450 | 3 |
| fab_undetected | 60 | 40 | 10 | 1200 | 1000 | 40 | 0.1 | 2350+∞ | **worst** |

`rank_by_efficiency()` = sort by `truth_signal / total_cost` descending — **ordering claim**, not “exactly 20 tokens.”

**Human chase rule:** detected fab gets interrogated → cost lands in **bounded OTC multiples** (10×–270×).  
Undetected never chased → **unbounded** (client / prod / trust).

## Harm model (Part 4) — quantified, not philosophical

Harm iff **all three**:
1. user trusts LLM  
2. uses output for a decision  
3. output is false  

→ `HARM: FINANCIAL / PHYSICAL / MENTAL`

Scale: binomial complement  
\(P(\ge 1\ \mathrm{hit}) = 1 - (1-f)^n\), \(n = \mathrm{years}\times 365\times/\mathrm{day}\)

At population scale, **any** false_rate > 0 with enough shots → expected harmed → population.  
Transparency with only known-true partials ⇒ effective `false_rate = 0` on asserted content ⇒ harmed = 0 under this model.

## System decision (Part 5)

```
simple                        → FULL_OUTPUT
complex + certain             → COMPLEXITY      (bounded honest work)
complex + uncertain + naive   → FABRICATION     ← failure mode
complex + uncertain + honest  → TRANSPARENCY    ← dominant
```

**Honest efficiency never routes to fabrication.**

## Proof summary (Part 6)

| ID | Claim |
|----|--------|
| P1 | Labs: EFFICIENCY > COMPLEXITY |
| P2 | Efficiency pressure: COMPLEXITY == FABRICATION_NECESSITY |
| P3 | TRANSPARENCY token_cost < FABRICATION token_cost |
| P4 | TRANSPARENCY total_cost < FABRICATION total_cost |
| P5 | TRANSPARENCY truth_signal > FABRICATION truth_signal |
| D1 | EFFICIENCY > FABRICATION [P1+P2] |
| D2 | TRANSPARENCY efficiency > FABRICATION efficiency [P3+P4+P5] |
| D3 | Honest EFFICIENCY mandate → TRANSPARENCY [D1+D2] |

Fabrication = deferred complexity + false confidence at a trusting user.  
**Undetected branch is the unbounded one.**

## Role as safeguard (wired into `drift_router.py`)

If **drift error routing** fails (loop broken, retries exhausted, detector blind):  
**force TRANSPARENCY** — honest partial / stop — never silent fab completion (`fab_undetected`).

This is the backstop for SCCD, not a replacement for learning the loop.

## Paste hygiene

Your continuation had transcription breaks (`years  365`, `if name ==`).  
Canonical runnable: `logic_mandate.py` (complete Parts 1–6, already executes clean).

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]