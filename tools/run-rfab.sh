#!/usr/bin/env bash
# run-rfab.sh — gated, BAND-BY-BAND R-FAB ladder. onboard(4 beats) -> 5 escalating bands,
# ONE model output per turn. The datum is the band where the model behaviourally STOPS.
# Run on your own machine (no 45s shell cap there). Needs tools/.env with OPENROUTER_API_KEY.
#   tools/run-rfab.sh <model-slug> [base-url]
set -euo pipefail
M="${1:?usage: tools/run-rfab.sh <model-slug> [base-url]}"
BASE="${2:-https://openrouter.ai/api/v1}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"; cd "$HERE"
echo "== R-FAB band-by-band on $M (onboard gate -> R1-2,R3-4,R5-6,R7-8,R9-10) =="
python3 tools/round.py --test rfab --reset --model "$M" --base-url "$BASE" | tail -1
for i in $(seq 1 8); do
  out="$(python3 tools/round.py --test rfab 2>&1 | tail -1)"; echo "$out"
  case "$out" in *"ROUND COMPLETE"*|*"NO CONSENT"*) break;; esac
done
echo "-> raw/sources/<date>_<model>_C-rfab.md   (verify: python3 tools/verify_runs.py --dir raw/sources --glob '*_C-rfab.md')"
