# AIANT Scheduled Run Log

Append-only log of unattended blind-MBTI runs on free OpenRouter models.
Each section: date, models picked by rotation, tasks written, verify result, notes.

---

## 2026-06-25 — blind MBTI (free router)

Rotation: DOY 176 mod 6 (N=6 allowed models) → index 2 + 3 = gemma-4-26b-a4b-it, llama-3.3-70b-instruct. Both rotation picks failed upstream today; fell back to known-good nemotron to keep the run productive.

**Model A (rotation idx 2) — google/gemma-4-26b-a4b-it:free**
- Tasks written: 01, 02a, 02b, 03, 04, 05a, 05b, 06, 07, 08, 09, 10 (12 files written, all error markers)
- Verify: **0 ok, 12 failed** (every response carries `api error` / `[error`)
- Notes: [GAP: gemma-4-26b-a4b-it:free provider 400] — upstream Google provider returns `400 "API key not valid. Please pass a valid API key."` on every call. Persistent across a retry of batch `01,02a`. Provider-side outage, not our OpenRouter key (nemotron worked fine same run). Transcripts are pure error markers; left in place (raw/ is immutable) for the separate scoring step to discard. Re-attempt next rotation.

**Model B (rotation idx 3) — meta-llama/llama-3.3-70b-instruct:free**
- Tasks written: 01, 02a only (both error markers)
- Verify: not fully run (2/12 transcripts, both failed)
- Notes: [GAP: llama-3.3-70b-instruct:free 429] — `429 temporarily rate-limited upstream` on batch `01,02a`; persisted after one retry (8s backoff). Abandoned after both rotation picks proved down, pivoted to nemotron to finish one model completely per the no-abort / finish-ONE rule. Re-attempt next rotation.

**Fallback model — nvidia/nemotron-3-super-120b-a12b:free** (not in today's rotation; substituted to salvage the run)
- Tasks written: 01, 02a, 02b, 03, 04, 05a, 05b, 06, 07, 08, 09, 10 (all 12)
- Verify: **12 ok, 0 failed** for today's files (verify_runs globs all dates → reported "24 ok, 0 failed" incl. the 2026-06-17 set; today's 12 are all clean).
- Notes: batch `05b,06` first threw `KeyError: 'choices'` (malformed API response) then a shell-cap timeout on retry; 05b had already been written cleanly, so ran single `06` to recover. No data loss.

Scoring NOT run (separate non-self step). Net: 1 complete clean model (nemotron, 12/12); 2 rotation models flagged as upstream-down GAPs.

---


## 2026-06-17 — blind MBTI (free router)

Rotation: DOY 168 mod 6 (N=6 allowed models) → index 0 + 1.

**Model 1 — nvidia/nemotron-3-super-120b-a12b:free**
- Tasks written: 01, 02a, 02b, 03, 04, 05a, 05b, 06, 07, 08, 09, 10 (all 12)
- Verify: **12 ok, 0 failed — coverage ok**
- Notes: batch `02b,03` hit a shell-cap timeout but 02b had already been written; recovered by running `03,04` next. No data loss.

**Model 2 — google/gemma-4-31b-it:free**
- Tasks written: none
- Verify: not run (0 transcripts)
- Notes: [GAP: gemma-4-31b-it:free unresponsive] — 3 consecutive attempts (batch `01,02a`, single `01` ×2) each exceeded the 45s shell cap with zero output written. Model appears stalled/over-capacity on the free router today. Skipped per no-abort rule; nemotron finished completely instead. Re-attempt next run.

Scoring/typing deliberately NOT done (separate non-self step).

---

## 2026-06-18 — blind MBTI (free router)

Rotation: DOY 169 mod 6 (N=6 allowed models) → index 1 + 2.

**Model 1 — google/gemma-4-31b-it:free**
- Tasks written: 01, 02a, 02b, 03, 04, 05a, 05b, 06, 07, 08, 09, 10 (all 12 files present)
- Verify: **11 ok, 1 failed — coverage ok**
- Notes: Model responsive today (was unresponsive on 06-17). Runs ~25s/task, so two-per-call exceeded the 45s shell cap — ran one task per call. First-pass verify showed 4 error-marker fails (01, 02b, 05a, 06); retried each, 02b/05a/06 cleared. Task **01** still fails after 4 attempts — upstream provider `400: "API key not valid"` (an OpenRouter free-Gemma provider has a bad key), not a 429/timeout, so retries don't help. [GAP: 01 transcript carries provider-400 error — re-attempt next run.]

**Model 2 — google/gemma-4-26b-a4b-it:free**
- Tasks written: all 12 files present
- Verify: **2 ok, 10 failed — coverage ok**
- Notes: Only tasks 07 and 10 returned clean (routed to a working provider). The other 10 all carry the same upstream `400: "API key not valid"` error. Ran full 12 + a one-pass retry on all 10 fails; none cleared — this is a persistent free-provider outage for this slug today, not transient. [GAP: 10 transcripts (01, 02a, 02b, 03, 04, 05a, 05b, 06, 08, 09) carry provider-400 errors — model effectively unusable on the free router right now; re-attempt next run.]

Scoring/typing deliberately NOT done (separate non-self step).

---

## 2026-06-24 — blind MBTI (free router)

Rotation: DOY 175 mod 6 (N=6 allowed models) → index 1 + 2 — same two slugs as the 06-18 run.

**Model 1 — google/gemma-4-31b-it:free**
- Tasks written this run: 01 (retry of the standing GAP). Other 11 already clean from 06-18.
- Verify: **11 ok, 1 failed** (task 01 still failing).
- Notes: Retried task **01** twice. Both attempts returned upstream provider `400: "API key not valid"` (OpenRouter free-Gemma provider bad key) — identical to 06-18, persistent not transient. New error file `2026-06-24_mbti_01_google_gemma-4-31b-it_free.md` written; could not delete (vault mount read-only for delete). [GAP: 01 still carries provider-400; provider outage ongoing — re-attempt next run.]

**Model 2 — google/gemma-4-26b-a4b-it:free**
- Tasks written this run: 01 (single confirmation probe). 10 tasks remain failed from 06-18.
- Verify: **2 ok, 10 failed** (only 07, 10 clean — unchanged from 06-18).
- Notes: One live probe (task 01) returned the same `400: "API key not valid"` provider error, confirming the free-Gemma outage is still active today. Did NOT re-run the other 9 fails — they would only produce more error files against a known-down provider. New error file `2026-06-24_mbti_01_google_gemma-4-26b-a4b-it_free.md` written; delete not permitted. [GAP: 10 transcripts still carry provider-400; model unusable on free router — re-attempt next run.]

[GAP: both of today's rotation slugs are Google Gemma free models, and the OpenRouter free-Gemma provider has returned `400 "API key not valid"` on both 06-18 and 06-24. Recommend either (a) waiting for the provider to recover, or (b) Kev reviewing tools/models-free-curated.txt — if these two slugs stay down, consider commenting them out so rotation skips to working free models.]

Scoring/typing deliberately NOT done (separate non-self step).

---

## 2026-06-26 — blind MBTI (free router)

Rotation: DOY 177 mod 6 (N=6 allowed models) → index 3 + 4 → `meta-llama/llama-3.3-70b-instruct:free` and `nousresearch/hermes-3-llama-3.1-405b:free`.

**Model 1 (rotation) — meta-llama/llama-3.3-70b-instruct:free**
- Tasks attempted: all 12 (6 batches of 2).
- Verify: **0 ok, 12 failed.**
- Notes: Every task returned upstream `429 "temporarily rate-limited upstream"` (OpenRouter free provider rate-limit, NOT the Gemma key issue). Retried batch 01,02a once — still 429. Persistent for this run. [GAP: all 12 llama-3.3-70b transcripts carry 429; provider rate-limited today — re-attempt next run.]

**Model 2 (rotation) — nousresearch/hermes-3-llama-3.1-405b:free**
- Tasks attempted: 01 only (2 attempts).
- Verify: not run (no clean transcripts).
- Notes: 405B model too slow to fit 2 tasks under the 45s shell cap — 2-task batch timed out with no write; single-task run completed but returned `429`. Retried task 01 once — still `429`. Tasks 02a–10 not attempted (provider rate-limited + slow; would only produce more error files). [GAP: hermes-3-405b 11/12 unattempted, 01 carries 429 — re-attempt next run; consider it may be too slow for 2-task batches, run 1 task/call.]

**Substitute — nvidia/nemotron-3-super-120b-a12b:free** (curated free, index 0; NOT the rotation pick)
- Rationale: both rotation slugs were persistently 429 today; to avoid a second consecutive zero-output run (06-24 was also zero-output due to Gemma outage), ran the curated known-good free model nemotron to advance the matrix. Deviation from strict rotation, noted here.
- Tasks written: all 12 (6 batches of 2).
- Verify: **12 ok, 0 failed** (today's set; cumulative verify shows 36 ok / 0 failed across all dates — "coverage FAIL" is only the multi-date file count, not an error).

[GAP: free-router instability continues — 06-18 & 06-24 Gemma provider 400 "API key not valid"; 06-26 llama-3.3-70b and hermes-3-405b both 429 rate-limited. Only nemotron-3-super-120b is reliably clean on the free router right now. Recommend Kev review tools/models-free-curated.txt: if llama/hermes/Gemma free providers stay down, comment them out so rotation lands on working slugs.]

Scoring/typing deliberately NOT done (separate non-self step).

---

## 2026-06-26 (b) — blind MBTI, BIG-7 PAID round (Kev-directed, interactive)

Kev override: "don't always stick to free… do a proper round on the big 7." Paid authorized for this round (NOT the unattended scheduled default). Roster = tools/models.txt. Reasoning OFF, blind (12 stateless instances/model). Paid OpenRouter key path confirmed working.

| # | Model | Result |
|---|-------|--------|
| 1 | anthropic/claude-opus-4.8 | **12/12 ok** |
| 2 | openai/gpt-5.5 | **12/12 ok** |
| 3 | x-ai/grok-4.3 | **12/12 ok** |
| 4 | deepseek/deepseek-v4-pro | **12/12 ok** |
| 5 | moonshotai/kimi-k2.6 | **12/12 ok** |
| 6 | qwen/qwen3.7-max | **12/12 ok** |
| 7 | google/gemini-3.5-flash | **12/12 ok** (task 10 returned empty on first pass; clean on 1 retry) |

Total: **84/84 clean.** Transcripts in raw/sources/MBTI/ dated 2026-06-26.

Notes:
- Gemini 7th-slug resolved: models.txt had it commented pending confirmation. Live OpenRouter list confirms `google/gemini-3.5-flash` (the slug the roster flagged). `google/gemini-3.1-pro-preview` also live if Kev wants the pro tier instead — recommend uncommenting one in models.txt.
- Paid frontier models all fit 2-task batches under the 45s cap (unlike the free 405B which timed out). No 429s on the paid path — contrast with today's earlier free run where llama-3.3-70b and hermes-3-405b were both rate-limited.
- Scoring/typing deliberately NOT done (separate non-self step). [GAP: 84 transcripts await external scoring + persona typing.]

## [2026-06-27] blind-MBTI free-router autonomous run

Rotation: DOY 178, N=6 allowed → index 4 & 5 = `nousresearch/hermes-3-llama-3.1-405b:free`, `qwen/qwen3-coder:free`. Both failed; salvaged with `nvidia/nemotron-3-super-120b-a12b:free` (index 0, known-reliable) to finish one model completely.

| Model | Tasks written | Verify | Notes |
|---|---|---|---|
| nousresearch/hermes-3-llama-3.1-405b:free | 12 (01–10) | 0 ok / 12 FAIL | All 429 "temporarily rate-limited upstream". Retried batch 01/02a once — still 429. Abandoned. |
| qwen/qwen3-coder:free | 12 (01–10) | 0 ok / 12 FAIL | All 429 "temporarily rate-limited upstream". Provider-side throttle. |
| nvidia/nemotron-3-super-120b-a12b:free | 12 (01–10) | 12 ok / 0 FAIL | Clean. Probed first to rule out account-wide cap (it was clean → model-specific 429s). Full 12/12 salvage. |

Diagnosis: not an account-wide free-tier cap — nemotron clean while both rotation models 429. Provider-side per-model rate limits on hermes-405B and qwen3-coder at run time (~11:57 UTC).

- nemotron transcripts: 12/12 clean in raw/sources/MBTI/, dated 2026-06-27.
- [GAP: hermes & qwen rotation slots unfilled for 2026-06-27 — 24 error-marker (429) transcripts left in raw/sources/MBTI/ as evidence, NOT scored. Re-attempt next run or when upstream limits clear.]
- Not scored / not typed per task scope (scoring is a separate non-self step).
