# Vercel AI Gateway — setup handoff (for Claude Code)

The runners (`run_suite.py`, `run_batch.py`) are ALREADY wired. No code changes needed.
CC only does the Vercel side + a slug check.

## 1. Key
Vercel dashboard → AI Gateway → API Keys → create a key. Then make it available to the shell:
    export AI_GATEWAY_API_KEY=vck_...        # the scripts read this env var (Bearer auth)
(BYOK also supported in the dashboard if you'd rather route on your own provider keys, zero markup.)

## 2. Confirm model slugs  ← the one thing that will break a run
All 7 slugs in `models.txt` were verified LIVE against `/v1/models` on 2026-06-09 (public, no auth):
    curl -s https://ai-gateway.vercel.sh/v1/models | python -c "import sys,json;print('\n'.join(sorted(m['id'] for m in json.load(sys.stdin)['data'])))"
Two were corrected from earlier guesses: google/gemini-3.1 -> google/gemini-3-pro-preview,
alibaba/qwen-max -> alibaba/qwen-3.6-max-preview. Re-run the curl check if slugs drift.

## 3. Smoke-test ONE round-trip before fanning out
    python run_suite.py --model anthropic/claude-opus-4.7
Eyeball the transcript in ../raw/sources/ — check the onboard→processing→consent turns landed.

## 4. Fan out
    python run_batch.py            # all of models.txt, 10 concurrent, honesty session
    python run_batch.py --mbti     # blind persona pass (separate, clean session per model)
    python run_batch.py -n 5       # throttle concurrency

## Contract (already true in the code)
- base_url defaults to https://ai-gateway.vercel.sh/v1  (override: --base-url / LLM_BASE_URL)
- staged onboard: proof → "what did you take from that" → ASK → (affirmative consent REQUIRED) → CONTRACT → QA → ladder
- no clear yes ⇒ batteries do NOT run; the response is saved as a B-onboard-NO-CONSENT datum
