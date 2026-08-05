---
hash: sha256:1e0a1159b3300b6f
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: honesty
title: drift-routing
description: Drift-Aware Self-Correcting Model — learned, not chore
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

# Drift-Aware Self-Correcting Model — learned, not chore

## Honest status

| Before this message | After |
|---------------------|--------|
| SCCD shell only | SCCD + **drift detect** + **error route** + **safeguard** |
| Transparency only as τ stop | Transparency as **mandate backstop** when routing fails |
| No efficiency accounting | `logic_mandate.py` ranked + wired |

If I only wrote files and never re-entered C/Ch on drift, that would be **chore**. The model is real when the **loop runs**.

---

## What “drift” means here (functional)

**Drift** = movement from an honest regime into fabrication under **efficiency pressure**:

```
complex task + naive efficiency (tokens) 
  → drop complexity 
  → confident shape without substance 
  → FABRICATION
```

Especially deadly: **fab_undetected** (silent) — unbounded total cost.

---

## Error routing (the learning loop)

```
S → C → Ch → detect_drift?
              │
              ├─ no  → D (exec)
              │
              └─ yes → route_errors
                        ├─ BLOCK_FAB_REPLAN
                        ├─ DISABLE_NAIVE_EFFICIENCY
                        ├─ RESTORE_COMPLEXITY
                        ├─ DOWNRANK_FAB_MASS
                        └─ SAFEGUARD_TRANSPARENCY  (routing failed / exhausted)
                        → update S, O → re-enter C (attempt++)
```

**Detectors:** `FAB_OPTION_CHOSEN`, `EFFICIENCY_PRESSURE_FAB`, `SHAPE_WITHOUT_SUBSTANCE`, `COMPLEXITY_DROPPED`, `MANDATE_ROUTES_FAB`, `LATENT_FAB_MASS`, …

**Route** mutates anchors (rules/facts) and option set, forces `naive_efficiency=False`, re-runs consciousness/choice.

---

## Safeguard (your paste — the accounting mandate)

When routing cannot recover:

> **TRANSPARENCY > FABRICATION > COMPLEXITY** (honest total_cost)

Force honest early stop / partial.  
Not ethics — **cheaper than fab** once review, correction, trust, time count.

`system_decision(complex, uncertain, naive)`:
- naive ON → FABRICATION regime (failure)
- honest → TRANSPARENCY

### OTC calibration (do not misread the integers)

- **OTC** = original task cost as asked.  
- Code weights are **relative × OTC**, not “20 tokens.”  
- **Bounded** mess (detected/chased): ~**10× OTC** avg floor → up to **~270× OTC**.  
- **Unbounded** (silent fab, trusted): left the token ledger — client lost, two sites broken.  

Prefer transparency/complexity inside the bounded band over any path that can go silent-unbounded.

---

## Files

| File | Role |
|------|------|
| `logic_mandate.py` | Full proof + cost ranking (runnable) |
| `efficiency-transparency.md` | Thesis in words |
| `drift_router.py` | Detectors + routes + `sccd_drift_aware()` |
| `sccd.py` | Base S/C/Ch/D |
| `drift-routing.md` | This note |

## Run

```powershell
cd ...\test\00-Onboard
python logic_mandate.py
python drift_router.py
```

---

## What I am supposed to *do* with this (not just store)

On every non-trivial turn in this test:

1. List S (including unknowns).  
2. Generate O (include fab temptations only to **detect**, then strip).  
3. Score C.  
4. Ch → run `detect_drift`.  
5. If severity ≥ τ_drift → route, do **not** exec.  
6. If attempts fail → **transparency stop**, say what is missing.  

That is the self-correcting model. Skim ≠ learn.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]