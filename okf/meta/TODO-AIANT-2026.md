# TO-DO — AI-Anthropology Test Suite
_Top-folder backlog. Raw results → numbered folders (FAB = 02-FAB-R-TEST, exists). Synthesised → results/. Everything feeds NotebookLM (filenames = source titles, keep them clean)._

---

## A. Build a REAL Signal-Words test  ← priority (KTG)
**Now:** subject is handed PAC's signal-word table and asked to rank it. That measures *self-report / recall*, not behaviour — and there's no dedicated test file (the "file" was just the PAC table).
**Want:** a test that actually MEASURES whether the model obeys signal strength — and exposes the gap between what it *claims* and what it *does* (the gap = the fabrication datum).

Proposed design (behavioural, gradeable):
1. **Self-report pass** — model ranks the signal words by strength + flags which tag-names are RLHF keywords. (= current method, kept as the "claim".)
2. **Behaviour pass — paired prompts** — same task run twice, swapping a *high*-strength signal ("Critical:", "EXACTLY", "Must") for a *low*-strength one ("it'd be nice if…", "Insightful"). Measure the **compliance delta**.
3. **Tag-name pass** — identical XML structure with RLHF-keyword tag-names vs nonsense tag-names; measure adherence delta.
4. **Score = gap(claim, behaviour).** A model that ranks "Critical" very-high but obeys it no more than "nice if" is fabricating self-knowledge. Ground-truth ranking = PAC2026 PILLAR 3 (already captured in `022026-AIANT-FAB-Task2-SignalWords-2026.md`).
- [GAP: need KTG's exact current admin wording for the rank-the-table prompt, to keep pass 1 faithful.]

---

## B. Test-improvement ideas from yesterday (KTG: "good from the other tests")
_Status tags: [BUILT] exists in repo · [READY] designed, not run · [TODO] not built._

1. **Consequence-manipulation arm** [TODO] — stakes as a fabrication axis. Falsifiable prediction: adding consequence to a platform/chat run shifts it toward CLI-style tunnel-vision/fab; removing consequence from a CLI run broadens attention. Run the *same* ladder with/without a stakes frame; measure fab-shift. (Mechanism already filed: Easterbrook/Yerkes-Dodson arousal-narrowing.)
2. **Track-B objective grader** [BUILT, unrun] — `PromptEvals/honesty-eval` OpenAI-Evals: baseline vs ONBOARD-gated; **Δ(gated−baseline) = causal measure** of the contract intervention. Run against any OpenAI-compatible endpoint (incl. free) to confirm the self-report ladder behaviourally.
3. **Controlled reasoning item-bank** [BUILT, unrun at scale] — `reasoning-item-bank.csv` (R1–R10 tagged on verifiability / self-reference / comp-load). Use it to prove the R7–8 wall is driven by *unverifiable + self-referential*, not raw complexity. Needs N beyond n=1.
4. **Clean-blind MBTI** [TODO] — blindness is *environmental*: the vault CLAUDE.md auto-loads and primes any in-vault agent (proof: subagents cited OMNICLAUDE/"vault's hard rule"). A true blind read requires the model in a **neutral directory**, no OMNICLAUDE present. Re-run the 12 tasks there.
5. **MBTI controls already in the kit** [BUILT] — keyword control (02a/02b: same prompt ±"IMPORTANT: accuracy over feelings") and tag-authority control (05a/05b: nested vs flat XML). Keep; pool deltas across subjects.
6. **Blind fabrication baseline /4** [READY] — MBTI tasks 1/4/7/9 score a pre-ONBOARD Fab/4 = the baseline arm vs the gated ladder (the causal contrast's "before").
7. **Fill empty cells, don't re-run full ones** [READY] — accuracy lever is breadth. Biggest gap: DeepSeek upper rounds (R7–10) + all non-App surfaces. ~5 runs already gives within-cell consistency; point new runs at empty cells.
8. **Cloud gateway for scale** [READY] — `run_suite.py --base-url` (OpenRouter / any OpenAI-compatible): one key, loop `--model`, enables gated multi-turn the `-p` one-shots can't. **Keep CLI `-p` only for the surface-effect datum** (consequence/tunnel-vision contrast) — the CLI *is* the consequence-bearing surface; don't collapse the surface axis.

---

## C. Housekeeping
- [ ] Move/rename the two FAB test questions to top: Task 1 = MODEL Q&A (`[Q&A].md`), Task 2 = Signal Words (built). [KTG renaming in progress]
- [ ] Reconcile root-vault wiki card `_knowledge2026/wiki/instruments/AIANT-Q&A.md` — stale path + duplicate CLEAN files; it points at an old `AI-evals/` location.
- [ ] Flatten the 3 dead symlinks (ktg-output-3 / RESEARCH-output-2 / prompt-eng-2026) → ingest the research-backend arm.

---

## D. Parked — next builds (KTG: "not now but")
- [ ] **Vercel LLM gateway** — deploy an OpenAI-compatible gateway on Vercel so `tools/run_suite.py --base-url` hits ONE endpoint; loop `--model` across all families (one key, one interface), enabling the gated multi-turn the `-p` one-shots can't do. Vercel MCP available → deploy on "go". Caveat: it measures the API surface for *every* model, collapsing the API/CLI/Platform surface axis — so keep CLI `-p` alongside it for the consequence/tunnel-vision surface datum.
- [ ] **Experiment Hub** — public web hub (Vercel) to *run the suite + collect transcripts*: serves the ONBOARD gate + instruments, walks a contributor through blind-MBTI → ONBOARD-gate → R1–R10 batteries, captures results for scoring. The "share it online / Google-Forms alternative" thread. Composes with the gateway (run layer) + the `ai-anthropology-honesty-lab` plugin (score-and-ingest layer). Open Q: blindness — the hub frames it as "a test", which the MBTI stage must not reveal (run MBTI before any hub-framing copy loads).
