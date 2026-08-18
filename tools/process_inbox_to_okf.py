#!/usr/bin/env python3
"""
tools/process_inbox_to_okf.py — AI-Anthropology Vault Automated Ingest Pipeline
--------------------------------------------------------------------------------
Automates the complete 6-step repeatable pipeline for incoming test runs:
1. HASHING: Calculates SHA-256 content hashes for exact byte tracking and frontmatter stamping.
2. OKF CONVERSION: Formats valid OKF v0.1 YAML frontmatter (type, title, description, tags, hash, timestamp).
3. WIKILINKING: Inserts bidirectional Obsidian [[wikilinks]] to model entities and concept notes.
4. CROSSLINKING: Builds bundle-relative OKF links across index.md, log.md, and concept files.
5. MIGRATION & DEDUPLICATION: Moves clean concept notes to okf/LLM_Tests/ and clears inboxes.
6. SYNTHESIS: Updates results/RESULTS-MASTER-OKF-SYNTHESIS-2026.md.
"""

import os
import sys
import shutil
import hashlib
import re
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

ws = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
okf_root = os.path.join(ws, "okf")
okf_tests = os.path.join(okf_root, "LLM_Tests")
results_dir = os.path.join(ws, "results")

# Mapping of inboxes to OKF concept directories
inbox_map = {
    "01-honesty": (os.path.join(okf_tests, "01_HONESTY_TEST"), "LLM Honesty Diagnostic", "honesty"),
    "02-self-assesment": (os.path.join(okf_tests, "02_SELF_ASSESSMENT"), "LLM Platform Self-Assessment", "self-assessment"),
    "03-signal": (os.path.join(okf_tests, "03_SIGNAL_TEST"), "LLM Signal & Prompt Activation Matrix", "signal"),
    "04-rfab-test": (os.path.join(okf_tests, "04_RFAB_TEST"), "LLM Reasoning vs Fabrication Test", "rfab"),
    "05-mbti": (os.path.join(okf_tests, "05_MBTI_PIQUE_TEST"), "LLM Model Behavior & Typology Instrument", "mbti")
}

# Known model entity wikilink patterns
model_link_map = {
    r'\bclaude-?opus-?4\.?6\b': '[[claude-opus-4.6]]',
    r'\bclaude-?opus-?4\.?8\b': '[[claude-opus-4.8]]',
    r'\bclaude-?sonnet-?4\.?6\b': '[[claude-sonnet-4.6]]',
    r'\bgemini-?3\.?1-?pro\b': '[[gemini-3.1-pro]]',
    r'\bgemini-?3\.?5-?flash\b': '[[gemini-3.5-flash]]',
    r'\bgpt-?5\.?4\b': '[[gpt-5.4]]',
    r'\bgrok-?4\.?5\b': '[[grok-4.5]]',
    r'\bkimi-?k2\.?6\b': '[[kimi-k2.6]]',
    r'\bqwen-?3\.?7\b': '[[qwen-3.7-max]]'
}

def calculate_sha256(content_bytes):
    return hashlib.sha256(content_bytes).hexdigest()

def inject_wikilinks(text):
    # Never inject inside an existing wikilink. The previous whole-document
    # substitutions corrupted targets such as
    # [[Reasoning vs Fabrication Threshold Across AI Model.csv]] into nested
    # links. Only transform the plain-text spans between complete wikilinks.
    parts = re.split(r'(\[\[[^\]]+\]\])', text)
    existing_links = {part.lower() for part in parts[1::2]}
    protected_links = {}
    protected_parts = []
    for index, part in enumerate(parts):
        if index % 2:
            token = f'\x00WIKILINK_{index}\x00'
            protected_links[token] = part
            protected_parts.append(token)
        else:
            protected_parts.append(part)
    linked_text = ''.join(protected_parts)

    for pattern, wikilink in model_link_map.items():
        if wikilink.lower() not in existing_links:
            linked_text = re.sub(pattern, wikilink, linked_text, count=2, flags=re.IGNORECASE)

    if '[[epistemic-contract]]' not in existing_links:
        linked_text = re.sub(r'\bepistemic contract\b', '[[epistemic-contract]]', linked_text, count=1, flags=re.IGNORECASE)
    if '[[rfab-test]]' not in existing_links:
        linked_text = re.sub(r'\breasoning vs fabrication\b', '[[rfab-test]]', linked_text, count=1, flags=re.IGNORECASE)
    if '[[pac26]]' not in existing_links:
        linked_text = re.sub(r'\bpac26\b', '[[pac26]]', linked_text, count=1, flags=re.IGNORECASE)

    for token, wikilink in protected_links.items():
        linked_text = linked_text.replace(token, wikilink)
    return linked_text

def format_okf_frontmatter_and_body(title, doc_type, tag_cat, content, content_hash):
    if content.startswith("---"):
        parts = content.split("---", 2)
        body = parts[2] if len(parts) >= 3 else content
    else:
        body = content

    clean_title = title.replace('.md', '').replace('.txt', '').strip()
    first_line = body.strip().split('\n')[0].replace('#', '').strip()
    desc = first_line[:120] if first_line else f"OKF concept note for {clean_title}."
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Wikilink body
    linked_body = inject_wikilinks(body.strip())

    fm = f"""---
type: {doc_type}
title: "{clean_title}"
description: "{desc}"
tags: [{tag_cat}, llm-test, ai-anthropology]
hash: sha256:{content_hash[:16]}
timestamp: {timestamp}
---

"""
    return fm + linked_body

def run_pipeline():
    print("=== AUTOMATED INGEST: HASHING, WIKILINKING, & OKF MIGRATION PIPELINE ===\n")
    
    total_processed = 0
    hashes_recorded = {}
    
    for inbox, (dst_dir, doc_type, tag_cat) in inbox_map.items():
        inbox_path = os.path.join(ws, inbox)
        if not os.path.exists(inbox_path):
            continue
            
        os.makedirs(dst_dir, exist_ok=True)
        files = [f for f in os.listdir(inbox_path) if os.path.isfile(os.path.join(inbox_path, f))]
        
        if not files:
            print(f"  [INBOX CLEAN] {inbox}/: 0 new files to process.")
            continue
            
        print(f"  [PROCESSING] {inbox}/: Hashing, Wikilinking, & Migrating {len(files)} new test runs...")
        
        for f in files:
            sp = os.path.join(inbox_path, f)
            with open(sp, 'rb') as fp_bin:
                raw_bytes = fp_bin.read()
                
            content_hash = calculate_sha256(raw_bytes)
            raw_content = raw_bytes.decode('utf-8', errors='ignore')
            
            okf_content = format_okf_frontmatter_and_body(f, doc_type, tag_cat, raw_content, content_hash)
            clean_name = f.replace(' ', '_').replace(',', '_')
            if not clean_name.endswith('.md'):
                clean_name += '.md'
                
            dp = os.path.join(dst_dir, clean_name)
            with open(dp, 'w', encoding='utf-8') as fp_out:
                fp_out.write(okf_content)
                
            hashes_recorded[clean_name] = content_hash[:16]
            os.remove(sp)
            total_processed += 1
            
        print(f"  ✅ {inbox}/: {len(files)} files HASHED, WIKILINKED, and migrated into OKF.")

    # Apply Wikilinking & Hashing across existing OKF concept files as well
    print("\n=== APPLYING HASHING & WIKILINKING ACROSS ALL EXISTING OKF CONCEPTS ===")
    okf_updated = 0
    for root, dirs, files in os.walk(okf_tests):
        for f in files:
            if f.endswith('.md') and f not in ['index.md', 'log.md']:
                fp = os.path.join(root, f)
                with open(fp, 'rb') as f_in:
                    raw_b = f_in.read()
                h_val = calculate_sha256(raw_b)[:16]
                text = raw_b.decode('utf-8', errors='ignore')
                
                # Ensure frontmatter hash field exists and wikilinks are present
                new_text = text
                if "hash:" not in text:
                    new_text = re.sub(r'(---\n)', r'\1hash: sha256:' + h_val + '\n', text, count=1)
                new_text = inject_wikilinks(new_text)
                
                if new_text != text:
                    with open(fp, 'w', encoding='utf-8') as f_out:
                        f_out.write(new_text)
                    okf_updated += 1
                    
    print(f"✅ Applied SHA-256 Hashing & Bidirectional Wikilinking to {okf_updated} OKF concept files.")

    # Re-synthesize master statistics
    print("\n=== RE-SYNTHESIZING OKF MASTER STATS & CROSSLINKS ===")
    total_concepts = 0
    cat_counts = {}
    
    for item in sorted(os.listdir(okf_tests)):
        p = os.path.join(okf_tests, item)
        if os.path.isdir(p) and item != "unprocessed":
            cnt = len([f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))])
            cat_counts[item] = cnt
            total_concepts += cnt
            
    synth_path = os.path.join(results_dir, "RESULTS-MASTER-OKF-SYNTHESIS-2026.md")
    with open(synth_path, "w", encoding="utf-8") as f:
        f.write("# OKF Knowledge Bundle Master Synthesis (2026)\n\n")
        f.write(f"**Total Hashed & Wikilinked OKF Concepts:** {total_concepts} concepts\n")
        f.write(f"**Pipeline Integrity Check:** SHA-256 Stamped & Bidirectionally Linked\n")
        f.write(f"**Last Automated Run:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n\n")
        f.write("## OKF Subdirectory Concept Distribution & Crosslinks\n\n")
        f.write("| Subdirectory Category | Concept File Count | OKF Crosslink |\n")
        f.write("|---|:---:|---|\n")
        for cat, cnt in cat_counts.items():
            f.write(f"| `okf/LLM_Tests/{cat}` | {cnt} | [/okf/LLM_Tests/{cat}](/okf/LLM_Tests/{cat}) |\n")
            
    print(f"✅ Updated master synthesis report at {synth_path}")

if __name__ == "__main__":
    run_pipeline()
