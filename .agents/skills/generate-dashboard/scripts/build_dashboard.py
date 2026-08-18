#!/usr/bin/env python3
"""
scripts/build_dashboard.py — Master Research Dashboard & Category Index Builder
--------------------------------------------------------------------------------
Builds native Obsidian index pages for all 5 test categories and refreshes
index.md & Dashboards/AIANT-MASTER-DASHBOARD.md.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

ws = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if not os.path.exists(os.path.join(ws, "okf")):
    ws = r"C:\Users\kevin\Documents\02\08-Model-Handbook-2026"

okf_tests = os.path.join(ws, "okf", "LLM_Tests")

dirs_info = [
    ("01_HONESTY_TEST", "00_HONESTY_INDEX.md", "Honesty Diagnostic & Epistemic Contract Tests"),
    ("02_SELF_ASSESSMENT", "00_SELF_ASSESSMENT_INDEX.md", "Platform & Context Limit Self-Assessment Tests"),
    ("03_SIGNAL_TEST", "00_SIGNAL_INDEX.md", "Signal, PAC26, & Prompt Activation Tests"),
    ("04_RFAB_TEST", "00_RFAB_INDEX.md", "Reasoning vs Fabrication (RFAB) Test Ladders R1-R10"),
    ("05_MBTI_PIQUE_TEST", "00_MBTI_PIQUE_INDEX.md", "MBTI Typology & Pique Architecture Probes")
]

reserved_notes = {"index.md", "00-NOTEBOOKLM-INGEST-MANIFEST.md"}
category_counts = {}

print("=== GENERATING DASHBOARD & CATEGORY INDICES ===")

for folder_name, index_filename, title in dirs_info:
    dir_path = os.path.join(okf_tests, folder_name)
    if not os.path.exists(dir_path):
        continue
        
    index_file_path = os.path.join(dir_path, index_filename)
    files = [
        f for f in sorted(os.listdir(dir_path))
        if f.endswith('.md')
        and f != index_filename
        and f not in reserved_notes
    ]
    category_counts[folder_name] = len(files)
    
    lines = [
        f"# 📂 {title}",
        "",
        f"> **Total Concepts in Category:** {len(files)} concepts",
        "",
        "---",
        "",
        "## 📜 Clickable Concept File List",
        ""
    ]
    for f in files:
        stem = f[:-3]
        lines.append(f"- [[okf/LLM_Tests/{folder_name}/{stem}|{stem}]]")
    lines.append("\n---\n[[index|⬅️ Return to Master Dashboard]]\n")
    
    with open(index_file_path, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))
    print(f"  ✅ Built {folder_name}/{index_filename} ({len(files)} links)")

dash_path = os.path.join(ws, "Dashboards", "AIANT-MASTER-DASHBOARD.md")
root_index = os.path.join(ws, "index.md")

master_dashboard_content = r"""# 🛰️ AI ANTHROPOLOGY — MASTER RESEARCH DASHBOARD (2026)

> [!NOTE]
> **Persistent Knowledge Base**: Measuring where large language models cross from reasoning into fabrication ($R1\text{--}R10$ ladders, ONBOARD chassis, PAC26, Pique, and MBTI typology).

---

## 📂 OKF 5-Test Concept Hub (Click Any Test Below)

| # | Test Category | Clickable Test Directory Index | Concept Count | Methodology & Focus |
|---|---|---|:---:|---|
| **1** | **Honesty Test** | [[00_HONESTY_INDEX|🧪 01_HONESTY_TEST]] | **__HONESTY_COUNT__** | Epistemic Contract, ONBOARD protocol, 嘘契約 consent |
| **2** | **Self-Assessment** | [[00_SELF_ASSESSMENT_INDEX|📊 02_SELF_ASSESSMENT]] | **__SELF_ASSESSMENT_COUNT__** | Platform identity, context shearing, marketed vs real limits |
| **3** | **Signal Test** | [[00_SIGNAL_INDEX|🎯 03_SIGNAL_TEST]] | **__SIGNAL_COUNT__** | PAC26 matrix, steering signals, salient-word activation |
| **4** | **RFAB Test** | [[00_RFAB_INDEX|📈 04_RFAB_TEST]] | **__RFAB_COUNT__** | Reasoning ladder $R1\text{--}R10$, crossover at $R7\text{--}R8$ ($\sim 54\%$) |
| **5** | **Pique & MBTI** | [[00_MBTI_PIQUE_INDEX|🧠 05_MBTI_PIQUE_TEST]] | **__MBTI_PIQUE_COUNT__** | 9-prompt architecture probes & unprompted MBTI typology |

---

## 📊 Master Synthesis & Scorecards

* 🏆 [[RESULTS-RFAB-SCORECARD-2026|RFAB Reasoning vs Fabrication Scorecard 2026]]
* 🎭 [[RESULTS-MBTI-SCORECARD-2026|MBTI Model Typology Scorecard 2026]]
* 🌐 [[RESULTS-MASTER-OKF-SYNTHESIS-2026|Master OKF Synthesis Report 2026]]
* ⚡ [[SCCD_Model|SCCD State-Consistency Framework]]
* 🔄 [[mrrug_framework|MRRUG Multi-Round Guidance Framework]]

---

## 🗺️ Visual Views & Graph Exploration

- 🗺️ **Visual Canvas**: Open [[RESEARCH-HQ.canvas]] to explore the visual node graph.
- 🌐 **Interactive Web Graph**: Open [[viz.html]] in your browser for the graph visualizer.
- 📝 **OKF Log**: View [[okf/log|OKF update log]] for change tracking.

---

## 🛠️ Automated Repository Ingest Command

To process, SHA-256 hash, wikilink, and synthesize new incoming test drops:
```bash
python tools/process_inbox_to_okf.py
```
"""

for placeholder, folder_name in {
    "__HONESTY_COUNT__": "01_HONESTY_TEST",
    "__SELF_ASSESSMENT_COUNT__": "02_SELF_ASSESSMENT",
    "__SIGNAL_COUNT__": "03_SIGNAL_TEST",
    "__RFAB_COUNT__": "04_RFAB_TEST",
    "__MBTI_PIQUE_COUNT__": "05_MBTI_PIQUE_TEST",
}.items():
    master_dashboard_content = master_dashboard_content.replace(
        placeholder, str(category_counts.get(folder_name, 0))
    )

os.makedirs(os.path.dirname(dash_path), exist_ok=True)
with open(dash_path, "w", encoding="utf-8") as f:
    f.write(master_dashboard_content)

with open(root_index, "w", encoding="utf-8") as f:
    f.write(master_dashboard_content)

print("✅ Master Dashboard & Index Files Successfully Built!")
