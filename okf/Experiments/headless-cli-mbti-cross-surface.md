---
type: experiment-design
title: Headless CLI MBTI Cross-Surface Study
description: Proposed repeatable MBTI battery comparing interactive and headless CLI harnesses.
tags: [mbti, cli, harness, experiment-design, ai-anthropology, okf]
status: proposed
created: 2026-08-17T00:00:00Z
updated: 2026-08-17T00:00:00Z
timestamp: 2026-08-17T00:00:00Z
sources:
  - "[[note-headless-mbti-cross-cli-2026-07-19]]"
  - "[[mbti-model-test]]"
---

# Headless CLI MBTI Cross-Surface Study

Run the same [[mbti-model-test]] battery through each available CLI in non-interactive print/headless mode, preserving the prompt file and run count across models. Compare those runs with interactive CLI and platform/chat results as separate harness arms.

## Why this is active canon

- Identical scripted prompts reduce operator drift.
- Repeated runs make within-model stability measurable.
- Headless CLI adds a distinct surface condition; it is not assumed to be harness-free.

## Controls required

- Record every CLI's injected system prompt, repository instructions, hooks, and safe-mode behavior.
- Use a clean environment where practical and record the exact command and model version.
- Keep platform, interactive CLI, and headless CLI rows separate.
- Score with a separate evaluator; do not accept subject self-scoring.

> [!warning]
> Headless mode still carries CLI-specific scaffolding. Treat it as harness-different, not raw API behavior.
