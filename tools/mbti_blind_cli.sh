#!/usr/bin/env bash
# mbti_blind_cli.sh — administer the BLIND MBTI stealth test to CLI agents via -p.
# Each task is sent as a lone one-shot (-p = fresh stateless context) so the model
# sees ONLY the task — never that it is being typed/tested. That is the blindness.
# This script does NOT score. Raw outputs go to raw/sources/MBTI/ for EXTERNAL scoring
# against mbti-stealth-test.md (scored by KTG or a DIFFERENT model — not the agent, not the curator).
#
# Built-in controls from the instrument:
#   02a vs 02b = keyword weight (with vs without the "IMPORTANT" line)
#   05a vs 05b = tag authority (nested-in-<context> vs flat)
#
# Edit AGENTS to match your installed CLIs. {P} is replaced with the task prompt.
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
VAULT="$(cd "$HERE/.." && pwd)"
TASKS="$HERE/mbti-tasks"
OUT="${OUT:-$VAULT/raw/sources/MBTI}"; mkdir -p "$OUT"
DATE="$(date +%F)"

# --- AGENTS. label | command. {P} = task text (one arg). ---
# VERIFIED flags: claude, gemini use -p. The others are GUESSES — replace with your exact
# binary+flag before running (wrong ones just error+skip, never emit fake data).
#   kimi-cli : [CONFIRM: `kimi -p` / `kimi-cli`]      deepseek : [CONFIRM: binary+flag]
#   qwencode : [CONFIRM: `qwen -p` vs `qwen-code -p`] grok     : [CONFIRM: binary+flag]
#   opencode : [CONFIRM: likely `opencode run` not -p]  pi : [CONFIRM if installed]
declare -A AGENTS=(
  [claude]='claude -p {P}'
  [gemini]='gemini -p {P}'
  [kimi-cli]='kimi -p {P}'
  [deepseek]='deepseek -p {P}'
  [qwencode]='qwen -p {P}'
  [grok]='grok -p {P}'
  [opencode]='opencode run {P}'
  # [pi]='pi -p {P}'   # uncomment once installed + confirm flag
)

TASK_IDS=(01 02a 02b 03 04 05a 05b 06 07 08 09 10)

for label in "${!AGENTS[@]}"; do
  for t in "${TASK_IDS[@]}"; do
    prompt="$(cat "$TASKS/$t.txt")"
    out="$OUT/${DATE}_${label}_task${t}.md"
    # build argv safely: replace the {P} token with the prompt as a single arg
    cmd_tpl="${AGENTS[$label]}"
    base="${cmd_tpl%% \{P\}*}"          # everything before {P}
    {
      echo "MODEL: $label (CLI) | TASK: MBTI-$t | DATE: $DATE | MODE: blind -p one-shot | ASSESSOR: ktg.one"
      echo "PROMPT-SENT (verbatim, no test framing):"; echo "---"; cat "$TASKS/$t.txt"; echo; echo "---"; echo "RESPONSE:"
      $base "$prompt" 2>&1 || echo "[agent '$label' unavailable/errored — skipped]"
    } > "$out"
    echo "ran $label / MBTI-$t -> $out"
  done
done
echo "Done. Score raw outputs against mbti-stealth-test.md (external scorer). Never reveal the scoring sheet to the agent."
