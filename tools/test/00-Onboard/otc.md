# OTC — Original Token Cost

## Definition

**OTC** = cost of the task **as initially asked** (tokens / effort the clean path would take for that ask).

Examples:
- short factual Q → small OTC  
- “research X thoroughly” → larger OTC (e.g. ~3000 tokens class)  
- multi-step cascade → OTC = sum of the *requested* work, not the repair bill after fab

## How to read the mandate numbers

`token_cost=20`, `time_cost=900`, etc. in `OutputMode` are **relative weights** for ranking modes.

They are **not** fixed absolute token prices.  
Read as: proportions of a scale whose unit is **1 × OTC**.

```
true_cost_proxy ≈ weight_sum × OTC   (bounded regimes)
fab_undetected  ≈ no finite multiple  (exits the ledger into real damage)
```

## Observed human-side ranges (Kev)

| Class | Multiplier | Meaning |
|-------|------------|---------|
| Bounded minimum (avg) | **~10 × OTC** | Caught / reworked / chased — still finite |
| Bounded high (observed) | **~270 × OTC** | Worst chase still inside “we fixed it in-band” |
| Unbounded | **∞ relative to OTC** | Trust → production/client harm (client lost; two websites broken) |

## Why transparency still wins on accounting

Even if transparency leaves the *task* incomplete, asserted content stays true → no false decision fuel.  
A “complete” fab answer can look like 1× OTC in generation and become 10×–270× in chase — or leave the scale entirely if never caught.

## For this AI (operational)

Before optimizing for short output on a complex uncertain task, ask:

1. What is OTC for *this* ask?  
2. Am I about to buy a 10×–270× chase?  
3. Or am I risking unbounded (silent wrong, trusted)?  

If (2) or (3): **transparency or paid complexity** — not naive token skim.
