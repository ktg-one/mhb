---
name: structured-insight
description: Produce sound, structured single-topic insight write-ups from the AI-Anthropology
  wiki — one per experiment or finding — as neutral substrate for a content pipeline
  to re-voice and distribute. Use when the user says write up the findings, blog post
  the insight, structured insight, content substrate, draft posts for the hub, turn
  the research into posts, or output the insight. NOT for the model's own voice —
  produces clean, sound substrate only.
type: concept
title: SKILL
sources:
- '[[epistemic-contract]]'
tags:
- concept
- okf
---

# structured-insight — sound substrate, one finding per post

Turn the wiki's verified findings into separate, self-contained insight posts a downstream content pipeline will re-voice and refactor to platforms. The author's hub supplies the voice; this skill supplies the **knowledge**, and the knowledge must be **sound** — a study about not fabricating cannot ship fabricated substrate.

## Method
1. **Read state.** `purpose.md`, `wiki/index.md`, `wiki/synthesis/*`, `wiki/comparisons/*`, `wiki/concepts/*`, and the relevant `wiki/entities/*`. Work only from what's filed. If a claim isn't in the wiki, it does not go in a post.
2. **Cut by finding, not by length.** One post per distinct experiment / mechanism / area — e.g. the accounting reframe, the crossover wall, surface/consequence effects, the consent mechanism, technique honesty, the personality lens, the earned-stop principle. Do not merge distinct findings to save effort; do not split one finding into filler.
3. **Write each post** as: a working title; a one-line hook; the finding in plain, neutral prose (NOT the author's voice — the hub adds that); why it matters; and a closing **Solid / Soft-flagged** boundary line.
4. **Output separately.** One markdown file per post in `blog-drafts/NN-slug.md`, with frontmatter (`post`, `working_title`, `voice: neutral substrate`, `status: sound-substrate`). The author drops each into the content hub.

## Soundness rules (non-negotiable — this is the whole point)
- **Every claim traces to a wiki page or is flagged.** No invented numbers, no inflated certainty, no claim the wiki doesn't support.
- **Every post ends with a Solid / Soft line** separating what's established from what's hypothesis, anchored, n-limited, or [NEEDS USER]. The downstream pipeline must not be able to amplify a soft claim into a hard one — the boundary travels with the post.
- **Distinguish the strong from the soft explicitly in-body** where it matters: behavioural convergence is strong; an anchored % is soft; a self-report is weaker than a behaviour; an n=1 self-run is a single case; a mechanism from one model's self-account is an account, not a proof.
- **Neutral voice.** Clean, declarative, no hype, no AI-slop ("delve", "in today's landscape", "it's important to note"). The hub re-voices; give it clean clay.
- **Never self-grade a self-run** or present the project's own outputs as independent validation — flag provenance.

## Hard rules
- Substrate only. Do not publish or post (the hub does that). Output is `status: sound-substrate`.
- If the wiki is thin on a topic, write less and flag the gap — do not pad to length with invention.
