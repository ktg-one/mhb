# Follow-up note — headless CLI calls for cross-agent MBTI runs

Captured 2026-07-19, Kev dictation. Not yet ingested. Feeds: 04-MBTI-TEST.

## Idea
Run the MBTI battery via headless/print-mode CLI calls instead of interactive sessions.
One script, same prompt file, every CLI agent on the machine:

- `claude -p "<battery>"` (Fable / Opus / Sonnet via --model)
- `codex exec` (GPT-5.6)
- `grok` headless (Grok 4.5)
- `gemini -y` (Gemini)
- Kimi CLI (check headless flag)

## Why good
- Scripted = identical prompt, zero operator drift, repeatable n>1 per model (trait STABILITY measurable, not just one-shot type)
- Loops over model versions cheaply — the whole battery per model in minutes
- Output to files → straight into .raw → ingest pipeline
- Headless = a THIRD harness arm (platform / CLI-interactive / CLI-headless) — ties into harness-effect thread; headless has no interactive system scaffolding, closest to raw API

## Watch
- Register confound again: caveman hook fires on interactive CLI, check if -p sessions load hooks/CLAUDE.md (they do load context — may need --safe-mode or clean HOME for naked runs)
- Each CLI injects its own system prompt — headless ≠ harness-free, just harness-different. Document per-CLI scaffolding in results.
