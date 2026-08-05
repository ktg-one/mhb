#!/usr/bin/env python3
"""clean_okf_frontmatter.py — Clean, standardize, and repair YAML frontmatter across OKF notes."""

import os
import re
import sys
import yaml

sys.stdout.reconfigure(encoding='utf-8')

VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OKF_DIR = os.path.join(VAULT_DIR, "okf")

TAXONOMY_TYPES = {
    "01_HONESTY_TEST": "honesty",
    "02_SELF_ASSESSMENT": "self-assessment",
    "03_SIGNAL_TEST": "signal",
    "04_RFAB_TEST": "rfab",
    "05_MBTI_PIQUE_TEST": "mbti",
    "Principles_and_Frameworks": "concept",
    "LLM_Behavior_Log": "behavior-log",
}

def clean_frontmatter_in_file(filepath, cat_type):
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        if not content.startswith("---"):
            return False, "No frontmatter"

        parts = content.split("---", 2)
        if len(parts) < 3:
            return False, "Malformed frontmatter block"

        fm_raw = parts[1]
        body = parts[2]

        try:
            fm_data = yaml.safe_load(fm_raw) or {}
        except Exception:
            fm_data = {}

        if not isinstance(fm_data, dict):
            fm_data = {}

        modified = False

        # 1. Clean type
        current_type = fm_data.get("type", "")
        if current_type != cat_type:
            fm_data["type"] = cat_type
            modified = True

        # 2. Clean title
        filename = os.path.basename(filepath).replace(".md", "")
        clean_title = re.sub(r"^[#_\d.-]+", "", filename).strip()
        if not clean_title:
            clean_title = filename
        if not fm_data.get("title"):
            fm_data["title"] = clean_title
            modified = True

        # 3. Clean description
        desc = fm_data.get("description", "")
        if not desc or desc.strip() in ['"```"', "```", ""]:
            # Extract first prose line from body
            lines = [l.strip() for l in body.splitlines() if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("```") and not l.strip().startswith("---")]
            first_prose = lines[0] if lines else f"OKF concept note for {clean_title}"
            fm_data["description"] = first_prose[:120].replace('"', "'")
            modified = True

        # 4. Clean sources[] (load-bearing)
        sources = fm_data.get("sources", [])
        if not sources or not isinstance(sources, list):
            sources = []
            # Extract wikilinks from body
            wikilinks = re.findall(r"\[\[([^\]|#]+)", body)
            for wl in wikilinks[:5]:
                sources.append(f"[[{wl.strip()}]]")
            if not sources:
                sources.append("[[epistemic-contract]]")
            fm_data["sources"] = sources
            modified = True

        # 5. Clean tags
        tags = fm_data.get("tags", [])
        if not isinstance(tags, list):
            tags = [t.strip() for t in str(tags).split(",") if t.strip()]
        if cat_type not in tags:
            tags.append(cat_type)
        if "okf" not in tags:
            tags.append("okf")
        fm_data["tags"] = tags

        # Re-serialize frontmatter
        new_fm = yaml.dump(fm_data, sort_keys=False, allow_unicode=True).strip()
        new_content = f"---\n{new_fm}\n---" + body

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, "Cleaned & updated"

        return False, "Already clean"

    except Exception as e:
        return False, f"Error: {e}"

cleaned_count = 0
scanned_count = 0

for root, dirs, files in os.walk(OKF_DIR):
    folder_name = os.path.basename(root)
    cat_type = TAXONOMY_TYPES.get(folder_name, "concept")

    for file in files:
        if file.endswith(".md") and file not in ["index.md", "log.md", "00_HONESTY_INDEX.md", "00_SELF_ASSESSMENT_INDEX.md", "00_SIGNAL_INDEX.md", "00_RFAB_INDEX.md", "00_MBTI_PIQUE_INDEX.md"]:
            filepath = os.path.join(root, file)
            scanned_count += 1
            is_mod, msg = clean_frontmatter_in_file(filepath, cat_type)
            if is_mod:
                cleaned_count += 1
                if cleaned_count <= 25:
                    print(f"✅ [{cleaned_count}] Cleaned: {os.path.relpath(filepath, VAULT_DIR)}")

print(f"\nFrontmatter cleaning complete! Scanned {scanned_count} files, cleaned {cleaned_count} files.")
