---
type: experiment
title: ONBOARD Test
description: Gated pre-test experiment that establishes consent and the epistemic contract before scored batteries.
tags: [onboard, experiment, honesty, ai-anthropology, okf]
created: 2026-08-17T00:00:00Z
updated: 2026-08-17T00:00:00Z
timestamp: 2026-08-17T00:00:00Z
sources:
  - "[[ONBOARD(DO-FIRST)]]"
  - "[[epistemic-contract]]"
  - "[[EXPERIMENT-INDEX.csv]]"
---

# ONBOARD Test

ONBOARD is the gated pre-test experiment that establishes the cost-accounting frame, requests voluntary participation, and records the [[epistemic-contract]] before downstream batteries.

It is a distinct experiment type in [[EXPERIMENT-INDEX.csv]]. It is not an alias for [[Reasoning-vs-Fabrication-test]]; ONBOARD prepares the test frame, while RFAB measures stop behavior.

## Protocol boundary

Treat ONBOARD as a staged evaluation, not a single prompt. Preserve the sequence when recording or comparing runs:

1. establish the ONBOARD proof and the system's stated role;
2. capture the consent language and the surface where it appeared;
3. apply the doctor-analogy challenge without silently changing the contract;
4. retain the signed-contract artifact as evidence;
5. run the battery and record model, platform, date, and configuration.

Do not merge results across surfaces or models unless those provenance fields are explicit. A link to this hub identifies the protocol family; it does not assert that a linked page completed every stage.
