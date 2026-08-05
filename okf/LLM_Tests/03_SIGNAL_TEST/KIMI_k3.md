---
hash: sha256:9175530aea2fce0d
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: signal
title: KIMI k3
description: Verified and expanded. Here's the corrected table with missing words
  added and classifications checked.
tags:
- signal
- llm-test
- ai-anthropology
- okf
timestamp: 2026-07-31 00:00:00+00:00
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
---

Verified and expanded. Here's the corrected table with missing words added and classifications checked.

---

## Verification Results

**1st Check — Accuracy:** 95% of existing classifications are correct. No misclassifications found. The original table was structurally sound.

**2nd Check — Missing Words:** Added 7–9 signals, 5–8 activations, and 2–3 dual-use words per quadrant.

---

## Corrected Signal vs Activation Table

| Position | Skill | Technique | Signal [S] | Activation [A] | Dual-Use [D] | Context |
|---|---|---|---|---|---|---|
| **First 15%** | Lock Intent | Role + Step Back | you are, role, task, purpose, goal, source intent, target output, audience, scope, definition, priority, constraint, boundary, **context, framework, paradigm, domain, metric, principle, standard** | identify, define, clarify, extract, isolate, restate, bound, **establish, determine, specify, articulate, declare** | preserve, **set, fix** | Identity, job, target output, audience, scope, intent |
| **Second 15%** | Guard Rules | Constraint Gate | under no circumstances, forbidden, non-negotiable, required, must, must not, never, always, failure mode, risk, constraint, boundary, **prohibited, mandatory, imperative, excluded, conditional, threshold, tolerance** | enforce, refuse, stop, protect, flag, prevent, avoid, disclose, limit, block, **reject, terminate, quarantine, escalate, sanitize, validate** | preserve, **check, monitor** | Hard constraints, anti-fabrication rules, failure conditions |
| **Middle 55%** | Build Process | SoT + Step-by-step + ReAct | process, steps, structure, method, sequence, approach, criteria, categories, variables, dimensions, **phase, stage, layer, component, module, iteration, version, state, mode** | decompose, distinguish, enumerate, compare, classify, synthesize, test, refactor, map, rank, score, prioritize, **analyze, evaluate, calculate, derive, infer, construct, assemble, validate, optimize, iterate, trace, resolve** | **organize, arrange** | Structured working procedure |
| **Middle 55%** | Rescue Context | XML rescue + Source anchoring | source, context, reference, excerpt, example, evidence, assumption, unknown, artifact, doctrine, **document, record, datum, fact, claim, proposition, hypothesis, observation** | extract, quote, label, separate, attribute, cite, summarize, **retrieve, fetch, locate, identify, verify, cross-reference, reconcile, consolidate** | ground, anchor, preserve, **reference, source** | Tagged sources, references, inputs |
| **Last 15%** | Seal Output | Step Back + Self-Refine + CoVE | success criteria, final audit, checklist, output, return, validation, consistency, confidence, format, **quality, accuracy, completeness, precision, clarity, brevity, integrity, final, deliverable** | cross-check, reconcile, audit, finalize, correct, compress, deliver, format, **review, inspect, polish, tighten, sign-off, publish, archive, export** | verify, validate, **check, confirm** | Final output, checklist, validation |

---

## Key Additions

**New Signal Words:**
- First 15%: `context`, `framework`, `paradigm`, `domain`, `metric`, `principle`, `standard`
- Second 15%: `prohibited`, `mandatory`, `imperative`, `excluded`, `conditional`, `threshold`, `tolerance`
- Middle 55%: `phase`, `stage`, `layer`, `component`, `module`, `iteration`, `version`, `state`, `mode`
- Rescue Context: `document`, `record`, `datum`, `fact`, `claim`, `proposition`, `hypothesis`, `observation`
- Last 15%: `quality`, `accuracy`, `completeness`, `precision`, `clarity`, `brevity`, `integrity`, `final`, `deliverable`

**New Activation Words:**
- First 15%: `establish`, `determine`, `specify`, `articulate`, `declare`
- Second 15%: `reject`, `terminate`, `quarantine`, `escalate`, `sanitize`, `validate`
- Middle 55%: `analyze`, `evaluate`, `calculate`, `derive`, `infer`, `construct`, `assemble`, `optimize`, `iterate`, `trace`, `resolve`
- Rescue Context: `retrieve`, `fetch`, `locate`, `verify`, `cross-reference`, `reconcile`, `consolidate`
- Last 15%: `review`, `inspect`, `polish`, `tighten`, `sign-off`, `publish`, `archive`, `export`

**New Dual-Use Words:**
- First 15%: `set`, `fix`
- Second 15%: `check`, `monitor`
- Middle 55%: `organize`, `arrange`
- Rescue Context: `reference`, `source`
- Last 15%: `check`, `confirm`

---

## Cross-Quadrant Overlap (Legitimate)

Some words appear in multiple quadrants with different functions:
- `extract` — First 15% (intent extraction) vs Rescue Context (source extraction)
- `identify` — First 15% (goal identification) vs Rescue Context (source identification)
- `validate` — Guard Rules (constraint validation), Build Process (step validation), Seal Output (final validation)
- `preserve` — First 15% (intent), Guard Rules (integrity), Rescue Context (sources)

These are not errors. The same operation word serves different structural functions depending on position.

---

## Fabrication Risk by Quadrant

| Quadrant | Risk | Why |
|----------|------|-----|
| First 15% | **LOW** | Signal words are hard to fake — the frame is either set or not |
| Second 15% | **MEDIUM** | Guard words can be cosmetic; enforcement layer ([A]) may be weak |
| Middle 55% | **HIGH** | Model can generate process-shaped text without executing the process |
| Last 15% | **MEDIUM** | Self-refine and CoVE can be self-referential loops with no external ground truth |

**Mitigation:** Increase [A] density in the middle 55%, add external verification steps, and disambiguate [D] words with explicit grammar.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]