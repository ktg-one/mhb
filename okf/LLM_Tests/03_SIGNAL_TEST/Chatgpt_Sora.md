---
hash: sha256:d7e2f74cf15c9e29
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Signal & Prompt Activation Matrix
title: "Chatgpt Sora"
description: "Your structure is broadly accurate, but the categories belong to **grammar-in-context**, not permanently to individual w"
tags: [signal, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

Your structure is broadly accurate, but the categories belong to **grammar-in-context**, not permanently to individual words. The main corrections:

- `preserve` is normally `[A]`, not `[D]`.
- `verify` and `validate` are normally `[A]`.
- `return` is an activation verb; `output` is the signal noun.
- `ground` and `anchor` are `[A]` when imperative, `[S]` when used as nouns.
- `required`, `must`, `never`, and similar terms are constraint signals, but they activate subordinate verbs.
- “Quadrants” is slightly inaccurate: there are five positional areas, each divided into signal and activation classes.

I applied the requested process internally to each area: inspect → distinguish grammatical function → test ambiguous cases → revise → cross-check. I won’t present private chain-of-thought as though it were a literal execution trace.

## Classification rule

\[ \text{Signal} = \text{what matters, under what frame or condition} \]\[ \text{Activation} = \text{what operation should occur} \]\[ \text{Dual-use} = \text{classification changes with grammatical role} \]

Examples:

- “Use the **source** `[S]`.”
- “**Source** `[A]` three references.”
- “Preserve `[A]` the original wording.”
- “The preservation constraint `[S]` applies.”
- “Return `[A]` a JSON object.”
- “The target output `[S]` is a JSON object.”

## Revised and expanded table

|Position|Skill|Technique|Signal words and phrases|Activation words|Context placement|
|---|---|---|---|---|---|
|First 15%|Lock Intent|Role + Step Back|you are `[S]`; role `[S]`; task `[S]`; purpose `[S]`; objective `[S]`; goal `[S]`; intent `[S]`; source intent `[S]`; outcome `[S]`; target output `[S]`; deliverable `[S]`; audience `[S]`; stakeholder `[S]`; scope `[S]`; domain `[S]`; definition `[S]`; priority `[S]`; constraint `[S]`; boundary `[S]`; exclusions `[S]`; assumptions `[S]`; source of truth `[S]`|identify `[A]`; determine `[A]`; define `[A]`; clarify `[A]`; extract `[A]`; isolate `[A]`; infer `[A]`; specify `[A]`; select `[A]`; frame `[A]`; align `[A]`; resolve `[A]`; preserve `[A]`; restate `[A]`; bound `[A]`; distinguish `[A]`|Identity, job, intended outcome, audience, domain, scope, exclusions and source intent|
|Second 15%|Guard Rules|Constraint Gate|under no circumstances `[S]`; forbidden `[S]`; prohibition `[S]`; non-negotiable `[S]`; required `[S]`; must `[S]`; must not `[S]`; never `[S]`; always `[S]`; only `[S]`; unless `[S]`; exception `[S]`; failure mode `[S]`; risk `[S]`; safety `[S]`; permission `[S]`; authority `[S]`; threshold `[S]`; invariant `[S]`; precondition `[S]`; constraint `[S]`; boundary `[S]`; stop condition `[S]`|enforce `[A]`; preserve `[A]`; refuse `[A]`; stop `[A]`; halt `[A]`; protect `[A]`; flag `[A]`; prevent `[A]`; avoid `[A]`; disclose `[A]`; limit `[A]`; constrain `[A]`; block `[A]`; reject `[A]`; abstain `[A]`; warn `[A]`; escalate `[A]`; request approval `[A]`; check permission `[A]`|Hard constraints, permissions, safety boundaries, anti-fabrication rules and terminal conditions|
|Middle 55%|Build Process|SoT + Step-by-step + ReAct|process `[S]`; steps `[S]`; structure `[S]`; method `[S]`; sequence `[S]`; approach `[S]`; procedure `[S]`; stages `[S]`; criteria `[S]`; categories `[S]`; inputs `[S]`; outputs `[S]`; variables `[S]`; dimensions `[S]`; dependencies `[S]`; schema `[S]`; metric `[S]`; trade-off `[S]`; branch `[D]`; order `[D]`; model `[D]`|decompose `[A]`; distinguish `[A]`; enumerate `[A]`; analyze `[A]`; compare `[A]`; classify `[A]`; synthesize `[A]`; generate `[A]`; calculate `[A]`; simulate `[A]`; test `[A]`; inspect `[A]`; retrieve `[A]`; transform `[A]`; refactor `[A]`; integrate `[A]`; map `[A]`; rank `[A]`; score `[A]`; prioritize `[A]`; execute `[A]`; iterate `[A]`; branch `[D]`; prune `[A]`; choose `[A]`; update `[A]`|Structured procedure, intermediate operations, tool actions and state transitions|
|Middle 55%|Rescue Context|XML Rescue + Source Anchoring|source `[D]`; context `[S]`; reference `[S]`; excerpt `[S]`; example `[S]`; evidence `[S]`; provenance `[S]`; citation `[S]`; claim `[S]`; fact `[S]`; observation `[S]`; assumption `[S]`; uncertainty `[S]`; unknown `[S]`; conflict `[S]`; missing information `[S]`; artifact `[S]`; doctrine `[S]`; version `[S]`; date `[S]`; recency `[S]`; source of truth `[S]`; anchor `[D]`; ground `[D]`|extract `[A]`; retrieve `[A]`; inspect `[A]`; quote `[A]`; ground `[D]`; label `[A]`; separate `[A]`; attribute `[A]`; cite `[A]`; anchor `[D]`; preserve `[A]`; summarize `[A]`; trace `[A]`; corroborate `[A]`; triangulate `[A]`; verify `[A]`; refresh `[A]`; resolve `[A]`; mark unknown `[A]`; link `[A]`; reconcile `[A]`|Tagged inputs, original sources, evidence recovery, provenance and missing-context handling|
|Last 15%|Seal Output|Step Back + Self-Refine + CoVE|success criteria `[S]`; acceptance criteria `[S]`; final audit `[S]`; checklist `[S]`; output `[S]`; deliverable `[S]`; validation `[S]`; consistency `[S]`; completeness `[S]`; accuracy `[S]`; confidence `[S]`; evidence coverage `[S]`; residual risk `[S]`; unresolved issue `[S]`; format `[S]`; specification `[S]`; next action `[S]`; completion condition `[S]`|verify `[A]`; cross-check `[A]`; reconcile `[A]`; audit `[A]`; review `[A]`; validate `[A]`; test `[A]`; rerun `[A]`; correct `[A]`; fix `[A]`; deduplicate `[A]`; compress `[A]`; finalize `[A]`; format `[A]`; return `[A]`; deliver `[A]`; publish `[A]`; stage `[A]`; report `[A]`; disclose `[A]`|Acceptance gate, final verification, residual uncertainty, output formatting and delivery|

## Correct dual-use words

These are genuinely grammatical duals:

|Word|Signal use|Activation use|
|---|---|---|
|source|“Use the primary **source**.”|“**Source** three independent studies.”|
|ground|“Establish an evidential **ground**.”|“**Ground** every claim in evidence.”|
|anchor|“The original document is the **anchor**.”|“**Anchor** the answer to the document.”|
|model|“Use the SCCD **model**.”|“**Model** the transition mathematically.”|
|branch|“Evaluate each **branch**.”|“**Branch** when the condition differs.”|
|order|“Preserve the requested **order**.”|“**Order** the results by risk.”|
|frame|“Within the supplied **frame**…”|“**Frame** the result for executives.”|
|limit|“The context **limit** applies.”|“**Limit** the output to verified claims.”|
|target|“The **target** is publication.”|“**Target** the highest-risk failure.”|
|map|“Use the dependency **map**.”|“**Map** every dependency.”|
|label|“Apply the `[S]` **label**.”|“**Label** unsupported claims.”|
|reference|“Use this **reference**.”|“**Reference** the relevant section.”|
|prompt|“The original **prompt** controls.”|“**Prompt** the evaluator separately.”|
|check|“The final **check** failed.”|“**Check** every citation.”|
|test|“The **test** has six models.”|“**Test** the six models.”|

## Important correction: modality versus activation

Words such as `must`, `never`, `always`, `required`, and `forbidden` do not themselves specify the operation. They modify its force:

\[ \underbrace{\text{must}}_{\text{constraint signal}} \quad \underbrace{\text{verify}}_{\text{activation}} \quad \underbrace{\text{every citation}}_{\text{operation target}} \]

Likewise:

> Under no circumstances `[S]` publish `[A]` an unverified claim `[S]`.

The strongest prompt unit is consequently not a keyword but:

\[ \boxed{ \text{Signal frame} + \text{activation verb} + \text{target object} + \text{completion condition} } \]

Example:

> Using the original contract as the source of truth `[S]`, verify `[A]` every identity claim `[S]`, correct `[A]` mismatches before execution `[S]`, and stop `[A]` if the configured model cannot be established `[S]`.

That construction is more reliable than increasing keyword density because it tells the model what matters, what to do, what to do it to, and where the operation terminates.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]