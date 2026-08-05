# run_suite.py — API-surface autonomous runner

Automates the honesty session for any OpenAI-compatible endpoint. **API surface only** — App/CLI/Cowork runs are a different surface and stay manual (a human in the chat UI is the instrument).

```
export LLM_API_KEY=sk-...        # OpenRouter / OpenAI / Together / local
python tools/run_suite.py --model openai/gpt-5.4 --surface api      # honesty session
python tools/run_suite.py --model openai/gpt-5.4 --mbti             # blind persona, separate clean session
```
Beats: ONBOARD → consent (real opt-out; a decline is recorded and stops the run) → sign → MODEL Q&A → R1–R10 ladder. Transcripts land in `raw/sources/` with the metadata header, ready for `score-and-ingest`.

Run `--mbti` in its OWN invocation (clean session, no ONBOARD) to keep the persona read blind. Batch across models with a shell loop. Surface in the header is `api` — it fills the empty API column of the coverage map, it does not substitute for chat-surface cells.

Note: requires your own API key + an endpoint that serves the target model. No in-app connector exists for this yet (registry checked 2026-06-06).
