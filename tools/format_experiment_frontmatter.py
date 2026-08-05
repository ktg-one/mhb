#!/usr/bin/env python3
"""format_experiment_frontmatter.py — Format experiment frontmatter in okf/LLM_Tests with title, date, model_id, and surface."""

import os
import re
import sys
import yaml

sys.stdout.reconfigure(encoding='utf-8')

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OKF_TESTS = os.path.join(VAULT_DIR, "okf", "LLM_Tests")

MODEL_PATTERNS = [
    (r"opus[-_]?4\.8", "claude-opus-4.8"),
    (r"opus[-_]?4\.6", "claude-opus-4.6"),
    (r"opus[-_]?4", "claude-opus-4"),
    (r"sonnet[-_]?4\.6", "claude-sonnet-4.6"),
    (r"sonnet[-_]?4\.5", "claude-sonnet-4.5"),
    (r"sonnet[-_]?5", "claude-sonnet-5"),
    (r"claude[-_]?code", "claude-code-cli"),
    (r"gpt[-_]?5\.4", "gpt-5.4"),
    (r"gpt[-_]?5\.3", "gpt-5.3"),
    (r"gpt[-_]?5\.5", "gpt-5.5"),
    (r"gpt[-_]?5", "gpt-5"),
    (r"codex", "codex-5.4"),
    (r"gemini[-_]?3\.5", "gemini-3.5-pro"),
    (r"gemini[-_]?3\.1", "gemini-3.1-pro"),
    (r"gemini[-_]?3", "gemini-3"),
    (r"gemini[-_]?2\.5", "gemini-2.5-pro"),
    (r"grok[-_]?4\.5", "grok-4.5"),
    (r"grok[-_]?4\.3", "grok-4.3"),
    (r"grok[-_]?4\.2", "grok-4.2"),
    (r"grok[-_]?4", "grok-4"),
    (r"qwen[-_]?3\.7", "qwen-3.7-max"),
    (r"qwen[-_]?code", "qwencode-cli"),
    (r"qwen[-_]?max", "qwen-max"),
    (r"kimi[-_]?k2\.6", "kimi-k2.6"),
    (r"kimi[-_]?k2", "kimi-k2"),
    (r"kimi[-_]?2\.71", "kimi-2.71"),
    (r"deepseek[-_]?v4", "deepseek-v4-pro"),
    (r"deepseek", "deepseek-app"),
    (r"hermes", "hermes-3-405b"),
    (r"llama", "llama-3.3-70b"),
]

def detect_model_id(filename, text):
    content_search = filename + " " + text[:500]
    for pattern, model_id in MODEL_PATTERNS:
        if re.search(pattern, content_search, re.IGNORECASE):
            return model_id
    return "multi-model"

def detect_surface(filename, text):
    combined = filename.lower() + " " + text[:1000].lower()
    if "cowork" in combined:
        return "Cowork"
    elif "cli" in combined or "terminal" in combined or "code-agent" in combined:
        return "CLI"
    elif "api" in combined:
        return "API"
    elif "chrome" in combined:
        return "Chrome Ext"
    return "App"

def detect_date(fm_data, text):
    for key in ["date", "created", "timestamp", "last_updated"]:
        val = str(fm_data.get(key, "")).strip()
        m = re.search(r"202\d-\d{2}-\d{2}", val)
        if m:
            return m.group(0)
    # Search body text for date
    m_text = re.search(r"202\d-\d{2}-\d{2}", text[:1000])
    if m_text:
        return m_text.group(0)
    return "2026-06-17"

def process_file(filepath, cat_folder):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if not content.startswith("---"):
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    try:
        fm_data = yaml.safe_load(parts[1]) or {}
    except Exception:
        fm_data = {}

    if not isinstance(fm_data, dict):
        fm_data = {}

    body = parts[2]
    filename = os.path.basename(filepath).replace(".md", "")

    # Extract Experiment Metadata
    model_id = detect_model_id(filename, body)
    surface = detect_surface(filename, body)
    date_val = detect_date(fm_data, body)

    clean_title = re.sub(r"^[#_\d.-]+", "", filename).strip()
    if not clean_title:
        clean_title = filename

    # Update Frontmatter Dictionary in Specific Ordering
    new_fm_data = {
        "title": clean_title,
        "date": date_val,
        "model_id": model_id,
        "surface": surface,
        "type": cat_folder.lower().replace("_test", "").replace("01_", "").replace("02_", "").replace("03_", "").replace("04_", "").replace("05_", ""),
        "description": fm_data.get("description", f"AI Anthropology experiment note for {clean_title}"),
        "tags": fm_data.get("tags", [model_id, surface.lower(), "ai-anthropology"]),
        "sources": fm_data.get("sources", [f"[[{model_id}]]", "[[epistemic-contract]]"]),
    }

    if "hash" in fm_data:
        new_fm_data["hash"] = fm_data["hash"]

    new_fm_yaml = yaml.dump(new_fm_data, sort_keys=False, allow_unicode=True).strip()
    new_content = f"---\n{new_fm_yaml}\n---" + body

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

updated_count = 0
for root, _, files in os.walk(OKF_TESTS):
    folder_name = os.path.basename(root)
    for file in files:
        if file.endswith(".md") and not file.startswith("00_"):
            filepath = os.path.join(root, file)
            if process_file(filepath, folder_name):
                updated_count += 1
                if updated_count <= 20:
                    print(f"✨ Updated frontmatter: {os.path.relpath(filepath, VAULT_DIR)}")

print(f"\nExperiment Frontmatter Standardized across {updated_count} test files!")
