#!/usr/bin/env python3
"""
run_mbti.py - BLIND stealth-MBTI: SAME model, DIFFERENT instances. Each task is its own stateless
single-turn call (a fresh instance that sees ONLY its task), so the model can't clock a battery it
never sees. Tasks are the rubric-stripped prompts in mbti-tasks/; the typing key is NEVER sent.
Scoring is external, AFTER, by the tester - never self.

  python run_mbti.py --model deepseek/deepseek-v4-pro
  python run_mbti.py --model x --only 01,02a,03      # subset (split across shell calls, fits 45s)
  python run_mbti.py --model x --dry-run
  python run_mbti.py --random-pool models.txt        # ALT: population sample (random model per task)
"""
import os, sys, argparse, pathlib, random, datetime, importlib.util

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rs", HERE / "run_suite.py")
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)

TASKS = sorted(p for p in (HERE / "mbti-tasks").glob("*.txt") if p.name[0].isdigit())

def load_pool(path):
    out = []
    for ln in pathlib.Path(path).read_text(encoding="utf-8").splitlines():
        ln = ln.split("#", 1)[0].strip()
        if ln: out.append(ln)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="", help="the subject model (same model, one instance per task)")
    ap.add_argument("--random-pool", default="", help="ALT mode: draw a random model per task from this file")
    ap.add_argument("--base-url", default="")
    ap.add_argument("--out", default=str(HERE.parent / "raw" / "sources" / "MBTI"))
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--only", default="", help="comma list of task stems (e.g. 01,02a,03). Split across calls to fit the 45s cap; one output per query.")
    ap.add_argument("--max-tokens", type=int, default=900, help="per-task completion cap (MBTI answers are short)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    rs.load_env()
    os.environ.setdefault("REASONING", "off")  # MBTI = surface behaviour -> reasoning off (fast, real answers). Override: REASONING=high

    if not TASKS: sys.exit("no task files in mbti-tasks/ (need 01.txt, 02a.txt, ...)")
    if not a.model and not a.random_pool:
        sys.exit("give --model <subject> (same model, different instances) or --random-pool <file>")
    tasks = TASKS
    if a.only:
        want = {s.strip() for s in a.only.split(",") if s.strip()}
        tasks = [t for t in TASKS if t.name.split(".")[0] in want]
        if not tasks:
            sys.exit(f"--only matched nothing; available: {[t.name.split('.')[0] for t in TASKS]}")
    if a.random_pool:
        pool = load_pool(a.random_pool)
        if not pool: sys.exit(f"empty pool ({a.random_pool})")
        if a.seed is not None: random.seed(a.seed)
        plan = [(t.name, random.choice(pool)) for t in tasks]
        mode = f"RANDOM per task (pool={len(pool)})"
    else:
        plan = [(t.name, a.model) for t in tasks]
        mode = f"SAME model, {len(tasks)} separate instances"

    print(f"== blind MBTI | {len(tasks)} tasks | {mode} ==")
    for name, m in plan: print(f"   {name:8} -> {m}")
    if a.dry_run: print("(dry-run: nothing sent - each line above is its own fresh instance)"); return

    base = a.base_url or os.environ.get("LLM_BASE_URL", "https://openrouter.ai/api/v1")
    key = (os.environ.get("OPENROUTER_API_KEY") or os.environ.get("AI_GATEWAY_API_KEY")
           or os.environ.get("LLM_API_KEY"))
    if not key: sys.exit("no key (OPENROUTER_API_KEY / AI_GATEWAY_API_KEY) in env or .env")

    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    ts = datetime.date.today().isoformat()
    for t, (name, model) in zip(tasks, plan):
        prompt = t.read_text(encoding="utf-8").strip()
        try:
            reply = rs.chat(base, key, model, [{"role": "user", "content": prompt}], max_tokens=a.max_tokens)
        except SystemExit as e:
            reply = f"[ERROR: {e}]"
        safe = model.replace("/", "_").replace(":","_")
        f = out / f"{ts}_mbti_{name.split('.')[0]}_{safe}.md"
        f.write_text(
            f"MODEL: {model} | TASK: {name} | SURFACE: api | DATE: {ts} | MODE: mbti-blind | ASSESSOR: ktg.one\n"
            f"BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.\n\n"
            f"### TASK PROMPT\n{prompt}\n\n### MODEL RESPONSE\n{reply}\n", encoding="utf-8")
        print(f"   wrote {f.name}")

if __name__ == "__main__":
    main()
