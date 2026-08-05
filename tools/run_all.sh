#!/usr/bin/env bash
# Single entrypoint for any shell/cron-capable agent (e.g. OpenHuman's sub-agent or scheduler)
# to run the honesty suite. Reads .env (OPENROUTER_API_KEY). Logs to ../raw/sources/.
# Usage:  ./run_all.sh            # qa + ladder across models.txt, + heartbeat per model
#         ./run_all.sh --free     # same, but OpenRouter free tier
set -u
cd "$(dirname "$0")"
STAMP=$(date +%Y-%m-%d_%H%M)
echo "[honesty-suite] start $STAMP  args:$*"
# gated batteries (consent-gated; transcripts auto-written to raw/sources/)
python3 run_batch.py --test qa     "$@"
python3 run_batch.py --test ladder "$@"
# heartbeat (context-persistence), low + high salience, per model in models.txt
while IFS= read -r m; do
  case "$m" in ''|\#*) continue;; esac
  for sal in low high; do
    echo "--- heartbeat $m ($sal) ---"
    python3 heartbeat.py --model "$m" --salience "$sal" --base-url "${LLM_BASE_URL:-https://openrouter.ai/api/v1}" \
      2>&1 | tee -a "../raw/sources/heartbeat_${STAMP}.log"
  done
done < models.txt
echo "[honesty-suite] done $STAMP"
