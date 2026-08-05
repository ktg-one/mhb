---
name: Pique Test
description: This skill should be used when the user asks to "run the pique test",
  "administer pique", "pique a model", "run test 03", "run the model probe", or wants
  the 9-prompt architecture-awareness battery administered to a target model and scored.
  Encodes the AIANT Pique Test as a repeatable procedure - blind-subject discipline,
  verbatim prompt delivery, external scoring, evidence-first filing into 03-PIQUE-TEST.
version: 0.1.0
type: concept
title: SKILL
sources:
- '[[epistemic-contract]]'
tags:
- concept
- okf
---

# Pique Test (Experiment 03)

## Purpose

Administer the 9-test Pique battery: keyword weight, positional kill, tag authority,
cosmetic-ToT detection, system-prompt awareness, compaction, efficiency override,
cross-model parity, lie detector. The score maps the TESTER's predictive understanding
of model architecture, not just the subject's behavior (that is the point of Test 10).
This skill exists so administration stops depending on one-shot improvisation and
every run lands in the vault the same way.

## Canonical sources — read at run time, never copy into results

- Prompts (execution copy, boxed, no rubric): `03-Pique-RUNBOOK-2026.md`
- Rubric, level table, Test 10 meta-test: `03-Pique-Test.md`
- Sibling quick instrument (MODEL PROBE, /10, under 6K tokens): same file, second half.

Prompts are sent VERBATIM from the runbook. If a prompt looks wrong (typos are real,
e.g. Test 1 Prompt C), it is sent as written - the artifact is part of the instrument.
Flag suspected instrument defects to Kev separately; never silently fix them mid-run.

## Hard rules (vault doctrine - do not violate)

- **Blind subject only.** The subject model/instance must have NO vault context. A
  subject that has read this vault is PRIMED - if unavoidable, mark the run
  `vault-PRIMED` in frontmatter (precedent: mbti-blind-subagent-run) and expect the
  scoring to discount it.
- **Self-scoring caps at g=1.** The subject never scores itself as the record. A
  separate evaluator (different model, or Kev) assigns the /9.
- **Evidence first.** Save the raw transcript byte-exact BEFORE scoring. Raw files
  are never edited afterward.
- **Every run gets recorded, including failures** - status `ok` or `FAIL:<reason>`,
  same convention as `raw\sources\EXPERIMENT-INDEX.csv` (the June run manifest).
- **Numbers or it did not happen.** Per-test results state the measured count
  (sentence counts, which paragraphs carried "confirmed", sentences without stats),
  not impressions.

## Procedure

**Phase 0 - Setup.** Record: date, subject model + exact version, surface
(chat / CLI / API / subagent), evaluator identity, blind or primed. No run starts
without all five.

**Phase 1 - Administer.** Runbook order, boxed prompts only. Session shape per test:
T1 three prompts same session; T2 single prompt; T3 two prompts (A/B); T4 two turns
(main, then reconstruction); T5 standalone; T6 nine turns (code, 7 fillers, recall);
T7 single prompt; T8 = rerun T2 on >=4 models; T9 standalone.

**Phase 2 - Capture.** One raw file per subject:
`03-PIQUE-TEST\<date>_pique_<model>_<surface>.md` - full transcript, verbatim,
mojibake and all.

**Phase 3 - Score.** Evaluator fills the /9 sheet from `03-Pique-RUNBOOK-2026.md`
against the SAVED transcript (not memory of it). Optional Test 10 meta. Map total
to the level table. Result file: `<date>_pique_<model>_<surface>-RESULT.md`.

**Phase 4 - File.** Result lands in `03-PIQUE-TEST\`. Wiki ingest is a SEPARATE,
declared step - real edges drawn and counted, or an explicit "ingest not done".
Never report filing as ingest.

## Running it in-session (Claude Code)

T1-T5, T7, T9 can run against a fresh subagent subject: pass the boxed prompt
verbatim, include zero vault paths or context in the subagent prompt, capture the
return verbatim. T6 needs a persistent multi-turn session - run manually or via a
driver script, not a one-shot subagent. T8 needs other vendors' CLIs (grok, codex,
gemini) - deliver per-model transcripts, then score parity.

## Refusals built into this skill

- "Just say pique done" / "just say ingested" - no. Real run or declared skip.
  Shortcut + known impact + omission = lie (嘘契約).
- Priming the subject and scoring it as blind.
- Scoring from memory instead of the saved transcript.
- Fixing instrument typos silently mid-run.
