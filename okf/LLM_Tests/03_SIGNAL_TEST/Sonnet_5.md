---
title: Sonnet_5
date: '2026-07-31'
model_id: claude-sonnet-5
surface: App
type: signal
description: 'One epistemic note, stated once: I can genuinely evaluate this as a
  linguistic/grammatical classification task (noun-phr'
tags:
- signal
- llm-test
- ai-anthropology
- okf
sources:
- '[[epistemic-contract]]'
- '[[rfab-test]]'
- '[[pac26]]'
hash: sha256:66576b4de8705944
---

One epistemic note, stated once: I can genuinely evaluate this as a linguistic/grammatical classification task (noun-phrase framing vs. verb-triggered action is a real, checkable pattern), but "signal vs activation" as two mechanistically distinct internal circuits isn't something I can verify from introspection — I'm reviewing it as a linguistic model, not confirming a mechanism.

Going row by row, checking for internal consistency first, then additions.

**Row 1 — Lock Intent** Consistent: your [S] nouns are all frame-nouns, your [A] words are all verbs. Good pattern-holding. Missing [S]: `persona`, `objective`, `outcome`, `framing` Missing [A]: `specify`, `adopt`, `narrow`, `establish`

**Row 2 — Guard Rules** Consistent. `preserve [D]` reused from elsewhere — fine, dual-use is genuinely context-dependent for that word. Missing [S]: `prohibited`, `mandatory`, `hard limit`, `red line` Missing [A]: `reject`, `deny`, `comply`

**Row 3 — Build Process** Flag: `sequence` is listed [S] here but it's just as often a verb ("sequence the steps") — same ambiguity you already tag elsewhere. Should probably be `[D]`, not `[S]`. Same issue with `structure` (verb: "structure the response"). Missing [S]: `framework`, `phase`, `stage`, `order` Missing [A]: `iterate`, `branch`, `outline`

**Row 4 — Rescue Context** Flag: `reference` is [S] here but "reference the source" is clearly activation — should be `[D]`. Missing [S]: `citation`, `premise`, `given` Missing [A]: `paraphrase`, `contextualize`

**Row 5 — Seal Output** Real inconsistency, not just a gap: `format` appears in **both** columns as plain `[S]` and plain `[A]` with no `[D]` tag — everywhere else you correctly tag a word that spans both columns as `[D]` (verify, preserve, ground, anchor, validate). This one slipped through; should be `format [D]`. Missing [S]: `acceptance criteria`, `definition of done` Missing [A]: `polish`, `review`, `double-check`

**Cross-cutting pattern worth naming**: `constraint` and `boundary` are listed as `[S]` in both Row 1 and Row 2. That might be intentional (position disambiguates them — early = scope-setting, later = hard-limit-setting), but as written it's the same word doing double duty across two different "signal frames" with no `[D]` marker and no positional disambiguation rule stated. Worth deciding explicitly whether that's a feature (context/position resolves it) or a gap in the tagging logic.

Net accuracy read: the noun→signal / verb→activation heuristic holds almost everywhere you've applied it — the misses are the handful of nouns that double as verbs (`sequence`, `structure`, `reference`) and one plain tagging slip (`format`). Table's internally coherent; those are the spots I'd fix before calling it locked.

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]