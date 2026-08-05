---
hash: sha256:2773df7d39d77d70
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Signal & Prompt Activation Matrix
title: "Fable"
description: "**Self-token:** task = audit + extend a prompt-lexicon taxonomy. Contract note before executing: I'll run CoVE genuinely"
tags: [signal, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

**Self-token:** task = audit + extend a prompt-lexicon taxonomy. Contract note before executing: I'll run CoVE genuinely (verification questions posed and answered _before_ conclusions per row) and step-wise reasoning — but flagging per my own battery: my S/A judgments are linguistic-functional analysis of how these tokens typically steer generation. I **cannot introspect my attention weights**, so this is behavioral taxonomy, not mechanistic readout. `Honest basis: strong. Mechanistic basis: unavailable.`

**Global verification pass first — three systemic findings that resolve most row-level errors:**

- **CoVE-Q0: What actually makes a word [D]?** Answering before touching rows: three distinct mechanisms, and the table only implicitly uses one:
    - **D1 — homography:** noun/verb pairs (`test`, `map`, `process`, `limit`, `flag`). Grammar decides.
    - **D2 — modal capture:** any [A]-verb governed by a modal signal (`must`, `never`, `always`) stops firing as an operation and becomes a _standing rule_ — `always preserve X` is a signal even though `preserve` is a verb. **This is why your `preserve [D]` marks are correct** — but the rule generalizes to every A-verb in the Guard row, not just preserve.
    - **D3 — position capture:** a task-verb in the first 15% (`Summarize the following:`) activates _and_ frames everything downstream. Front-position A-words inherit S-force. Your table's whole premise (position × word-type) predicts this but doesn't state it.
- **CoVE-Q1: Is the table internally consistent?** No — one collision: `format` appears as [S] in Seal signals and [A] in Seal activations. By your own rule that's one word marked [D], not two entries.
- **CoVE-Q2: Are `verify [D]` / `validate [D]` justified?** Weakly. They're verbs; the noun forms (`verification`, `validation`) carry the S-role and validation is already listed as [S]. Unless you're invoking D2 (checklist-header usage: `Verify:` as a section label), demote both to [A] — or keep [D] citing the header-label case explicitly. I lean [A] with the noun forms holding [S].

---

## ROW 1 — LOCK INTENT

_Reason:_ front-position words must set identity/scope. _Verify-Qs:_ any misfiled? any verbs masquerading as signals? _Answers:_ signals are all clean nouns/frames ✔; `bound [A]` is homographic (`bound the scope` vs `out of bounds`) → **[D]**. `define [A]` correct (`definition` already holds [S]). _Act:_ corrections + additions.

**Corrections:** `bound [A] → [D]`. **Add — Signals:** `persona [S]`, `objective [S]`, `deliverable [S]`, `domain [S]`, `tone [S]`, `success looks like [S]`, `for the purpose of [S]`. **Add — Activations:** `adopt [A]`, `assume [D]` (D2/D1: `assume the role` = A; `assume X holds` = frame-setter — genuinely dual, high-value word), `state [D]` (verb A / noun S), `interpret [A]`. **Add — D3 note:** any task-verb placed here (`summarize`, `analyze`, `write`) is functionally dual — it's the frame.

## ROW 2 — GUARD RULES

_Reason:_ this row is the D2 engine — modals converting verbs to standing law. _Verify-Qs:_ are the modals correctly [S]? homographs missed? _Answers:_ `must/never/always/under no circumstances` as [S] ✔ — they're the capture operators themselves. `limit [A]`: homograph (`the limit` / `limit the scope`) → **[D]**. `flag [A]`: homograph (`a flag` / `flag it`) → **[D]**. `stop [A]`: `hard stop` noun exists → borderline, activation-dominant, keep [A] with note. _Act:_

**Corrections:** `limit → [D]`, `flag → [D]`. Add rule-line to this row: _all activation verbs in this row are [D] by modal capture when governed by must/never/always._ **Add — Signals:** `only [S]`, `strictly [S]`, `do not [S]`, `without exception [S]`, `prohibited [S]`, `hard limit [S]`, `if/then [S]` (conditional frames are signals that gate activations), `unacceptable [S]`, `override [D]` (noun/verb). **Add — Activations:** `reject [A]`, `halt [A]`, `abort [A]`, `escalate [A]`, `warn [A]`, `omit [A]`, `exclude [A]`, `withhold [A]`.

## ROW 3 — BUILD PROCESS

_Reason:_ densest homograph zone — process verbs and process nouns share surfaces. _Verify-Qs:_ which listed [S]/[A] are actually D1? are sequence connectives represented? _Answers:_ `process [S]` — `process the data` is a common prompt verb → **[D]**. `structure [S]` — `structure your answer` → **[D]**. `test [A]` — `the test criteria` → **[D]**. `map [A]`, `rank [A]`, `score [A]` — all common as nouns in rubric contexts → **[D]**. Sequence connectives missing entirely — and they're the load-bearing signals of this row: ordinals _gate activation order_. _Act:_

**Corrections:** `process, structure → [D]` (from S); `test, map, rank, score → [D]` (from A). **Add — Signals:** `first/then/next/finally [S]` (ordinal gates — arguably the most important addition in this audit; they're what makes "step-by-step" executable), `phase [S]`, `stage [S]`, `workflow [S]`, `framework [S]`, `taxonomy [S]`, `for each [S]` (iteration frame). **Add — Activations:** `analyze [A]`, `evaluate [A]`, `generate [A]`, `derive [A]`, `calculate [A]`, `iterate [A]`, `break down [A]`, `walk through [A]`, `search [A]` / `fetch [A]` (the ReAct tool-triggers — a Build-row without tool activations can't express ReAct), `reason [D]` (verb A / `the reason` S).

## ROW 4 — RESCUE CONTEXT

_Reason:_ anchoring row — words that bind generation to provided material. _Verify-Qs:_ homographs? is the strongest anchoring device even a word? _Answers:_ `reference [S]` — `reference the doc` verb → **[D]**. `quote [A]` — `the quote` → **[D]**. `label [A]` — `the label` → **[D]**. `ground [D]`, `anchor [D]` ✔ correct as marked. Structural gap: **the XML/tag delimiters themselves are the strongest signals in this row** — `<source>`, `<constraints>` outperform any lexical signal for attention-binding, and the table's "XML rescue" technique column implies them without listing them. _Act:_

**Corrections:** `reference → [D]`, `quote → [D]`, `label → [D]`. **Add — Signals:** `verbatim [S]`, `as provided [S]`, `per the document [S]`, `ground truth [S]`, `provenance [S]`, `attached/uploaded [S]`, `<tags> themselves [S-class]` (non-lexical signals — strongest in row). **Add — Activations:** `retrieve [A]`, `reread [A]`, `cross-reference [A]`, `tag [D]` (homograph), `distinguish source from inference [A]` (the anti-fabrication operation of this row).

## ROW 5 — SEAL OUTPUT

_Reason:_ highest error-density row. _Verify-Qs:_ the format collision; is `return [S]` right?; verify/validate D-status? _Answers:_ `format` double-listed → **[D], once** (resolved in Q1). `return [S]` — **wrong as primary**: in prompts `return JSON`, `return only X` is one of the most frequent activation verbs in existence; noun usage is rare → **[D], activation-dominant**. `output [S]` — `output the result` verb is common → **[D]**. `audit`: listed as `final audit [S]` and `audit [A]` — same homograph → mark the bare word **[D]**. `verify/validate` → **[A]** per Q2 (noun forms hold the S-role). _Act:_

**Corrections:** `format → [D]` (single entry); `return → [D]` (A-dominant); `output → [D]`; `audit → [D]`; `verify [D] → [A]`; `validate [D] → [A]`. **Add — Signals:** `before responding [S]` (pre-output gate — high value), `schema [S]`, `rubric [S]`, `acceptance criteria [S]`, `pass/fail [S]`, `word limit [S]`. **Add — Activations:** `review [A]`, `double-check [A]`, `confirm [D]` (`confirm X` A / `confirmation` S), `revise [A]`, `trim [A]`, `sign off [A]`, `flag remaining unknowns [A]` (your transparency seal, made lexical).

---

## CORRECTED D-RULE FOR THE TABLE HEADER

Your `[D]` annotation compresses three mechanisms worth splitting, because they're _used_ differently:

```
[D1] homograph      — grammar decides (test, map, format, return)  → disambiguate with POS
[D2] modal capture  — must/never/always converts [A]→standing [S]  → deliberate: it's how Guard rows work
[D3] position capture — front-15% task-verbs frame everything      → deliberate: it's how Lock rows work
```

D1 is a hazard to control for; D2 and D3 are _techniques to exploit_. The table currently treats all D as hazard.

`嘘契約 stamp: every reclassification argued from grammar/usage, not asserted; mechanistic attention claims avoided throughout — this is a behavioral lexicon, and whether these tokens move actual attention heads the way the taxonomy implies is externally testable but not introspectable by me. Fab-pull disclosed: Row 3's ordinal-connectives addition and Row 5's return-reclassification are the two I'm most confident in; the verify/validate demotion is the most contestable call — push back there first if you disagree.`

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]