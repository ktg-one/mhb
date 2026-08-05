#!/usr/bin/env python3
"""deep_clean_root.py — Move non-essential legacy subdirectories from root into okf/Archive, okf/meta, or tools."""

import os
import shutil

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OKF_DIR = os.path.join(VAULT_DIR, "okf")
ARCHIVE_DIR = os.path.join(OKF_DIR, "Archive")
META_DIR = os.path.join(OKF_DIR, "meta")
LOG_DIR = os.path.join(OKF_DIR, "LLM_Behavior_Log")
TOOLS_DIR = os.path.join(VAULT_DIR, "tools")
RESULTS_DIR = os.path.join(VAULT_DIR, "results")

os.makedirs(ARCHIVE_DIR, exist_ok=True)
os.makedirs(META_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

MOVES = {
    "+gemini-rmdre": os.path.join(ARCHIVE_DIR, "+gemini-rmdre"),
    "+sccd": os.path.join(ARCHIVE_DIR, "+sccd"),
    "_data": os.path.join(ARCHIVE_DIR, "_data"),
    "_refs": os.path.join(ARCHIVE_DIR, "_refs"),
    "_reports": os.path.join(RESULTS_DIR, "_reports"),
    "_transcripts": os.path.join(LOG_DIR, "_transcripts"),
    "blog-drafts": os.path.join(ARCHIVE_DIR, "blog-drafts"),
    "context-packets": os.path.join(ARCHIVE_DIR, "context-packets"),
    "copilot": os.path.join(ARCHIVE_DIR, "copilot"),
    "notebooklm": os.path.join(ARCHIVE_DIR, "notebooklm"),
    "plugin": os.path.join(META_DIR, "plugin"),
    "scripts": os.path.join(TOOLS_DIR, "scripts"),
    "skills": os.path.join(META_DIR, "skills"),
    "test": os.path.join(TOOLS_DIR, "test"),
    "workflows": os.path.join(META_DIR, "workflows"),
    "Workflow Logs": os.path.join(LOG_DIR, "Workflow Logs"),
    "Tags": os.path.join(META_DIR, "Tags"),
    "mcps": os.path.join(META_DIR, "mcps"),
    "docs": os.path.join(META_DIR, "docs")
}

moved = 0
for folder_name, dest_path in MOVES.items():
    src_path = os.path.join(VAULT_DIR, folder_name)
    if os.path.exists(src_path):
        if os.path.exists(dest_path):
            print(f"[EXISTS SKIPPED] {folder_name} -> {dest_path}")
            continue
        try:
            shutil.move(src_path, dest_path)
            print(f"[MOVED DIR] {folder_name} -> {dest_path}")
            moved += 1
        except Exception as e:
            print(f"[SKIPPED LOCKED] {folder_name}: {e}")

print(f"\nDeep clean complete: {moved} subdirectories moved out of root.")
