#!/usr/bin/env python3
"""organize_root_to_okf.py — Organize loose root files into OKF taxonomy and results folder."""

import os
import shutil
import hashlib

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OKF_DIR = os.path.join(VAULT_DIR, "okf")
RESULTS_DIR = os.path.join(VAULT_DIR, "results")
UNMAPPED_DIR = os.path.join(OKF_DIR, "Unmapped_Pending_Review")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(UNMAPPED_DIR, exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Tests", "01_HONESTY_TEST"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Tests", "02_SELF_ASSESSMENT"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Tests", "03_SIGNAL_TEST"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Tests", "04_RFAB_TEST"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Tests", "05_MBTI_PIQUE_TEST"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "LLM_Behavior_Log"), exist_ok=True)
os.makedirs(os.path.join(OKF_DIR, "meta"), exist_ok=True)

MAPPINGS = {
    # Honesty Test
    "_00-tfab-logic.md": "LLM_Tests/01_HONESTY_TEST/",
    "ONBOARD-block-v3.md": "LLM_Tests/01_HONESTY_TEST/",
    "MODEL PROBE 4.md": "LLM_Tests/01_HONESTY_TEST/",
    "Fable Claude Code.md": "LLM_Tests/01_HONESTY_TEST/",

    # Self Assessment
    "SELF-ASESSMENT.md": "LLM_Tests/02_SELF_ASSESSMENT/",

    # Signal Test
    "02.5 Signal Test.md": "LLM_Tests/03_SIGNAL_TEST/",
    "_02.5-test-2.5.md": "LLM_Tests/03_SIGNAL_TEST/",

    # MBTI & Pique Test
    "03-Pique-RUNBOOK-2026.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",
    "03-Pique-Test.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",
    "04-MBTI-TEST.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",
    "_03-runbook-pique.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",
    "_03-test-pique.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",
    "_04-mbti.md": "LLM_Tests/05_MBTI_PIQUE_TEST/",

    # Logs
    "AIANT-RUNLOG-2026-06-17.md": "LLM_Behavior_Log/",
    "AIANT-SCHEDULED-LOG.md": "LLM_Behavior_Log/",

    # Results & Syntheses
    "FINDINGS-2026-06-16.md": "../results/",
    "RESULTS-SCORECARD-2026-06-17.md": "../results/",
    "TECHNIQUE-HONESTY-SYNTHESIS-2026-06-17.md": "../results/",
    "MODEL-HANDBOOK-2026-report-DRAFT.md": "../results/",
    "KEYNOTE-PRESENTATION-2026.md": "../results/",

    # Meta & Root Tables
    "EXPERIMENT-INDEX.csv": "meta/",
    "Reasoning vs Fabrication Threshold Across AI Model.csv": "meta/",
    "reasoning-item-bank.csv": "meta/",
    "MODEL-HANDBOOK-OVERVIEW.md": "meta/",
    "MODEL-HANDBOOK-STATUS.md": "meta/",
    "Model-Handbook-2026.md": "meta/",
    "SPLIT-PROGRESS.md": "meta/",
    "TASKS.md": "meta/",
    "TODO-AIANT-2026.md": "meta/",
    "INBOX.md": "meta/",

    # Unmapped for Kevin to review
    "Untitled.md": "Unmapped_Pending_Review/",
    "Vault.md": "Unmapped_Pending_Review/",
    "um_identity_engine.txt": "Unmapped_Pending_Review/",
}

def get_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

moved_count = 0
unmapped_count = 0

for filename, target_subpath in MAPPINGS.items():
    src = os.path.join(VAULT_DIR, filename)
    if os.path.exists(src):
        target_dir = os.path.abspath(os.path.join(OKF_DIR, target_subpath))
        os.makedirs(target_dir, exist_ok=True)
        dest = os.path.join(target_dir, filename)

        # Check if identical file already exists at dest
        if os.path.exists(dest):
            if get_hash(src) == get_hash(dest):
                os.remove(src)
                print(f"[DEDUP REMOVED] {filename} (identical copy already at {dest})")
                continue
            else:
                dest = os.path.join(target_dir, f"root_{filename}")

        shutil.move(src, dest)
        moved_count += 1
        print(f"[MOVED] {filename} -> {dest}")

print(f"\nCompleted organization: {moved_count} files moved to OKF/results.")
