---
name: notebooklm-prep
description: "Prepare, format, and package vault research notes into NotebookLM-ready source bundles with automatic Audio Overview / Podcast transcript priming and source manifests."
user-invocable: true
argument-hint: "[target-folder] [-o output-manifest.md]"
allowed-tools: Bash, ReadFile, WriteFile
---

# notebooklm-prep — NotebookLM Ingestion & Audio Overview Priming

Prepare, sanitize, and structure Obsidian vault notes into clean source packages optimized for Google **NotebookLM** batch upload, citation mapping, and Audio Overview (Podcast format) synthesis.

## Workflow & Constraints

1. **Clean Header & Frontmatter Injection**:
   Every source file is verified to contain clean YAML frontmatter (`title`, `type: concept`, `tags: [notebooklm-ingest]`) without raw control characters or HTML noise.

2. **Chunking & Size Check**:
   NotebookLM accepts up to 500,000 words per source. Large transcripts are split cleanly into section-level source chunks (`_part1.md`, `_part2.md`).

3. **Manifest Generation**:
   Generates a master upload manifest (`00-NOTEBOOKLM-INGEST-MANIFEST.md`) linking all formatted source files, byte counts, and key research questions for the NotebookLM query box.

4. **Audio Overview (Podcast) Prompt Generator**:
   Generates a dedicated prompt file (`NOTEBOOKLM-AUDIO-PROMPT.txt`) tailored to elicit deep technical Audio Overviews focusing on:
   - Reasoning vs Fabrication ($R1\text{--}R10$) crossover thresholds ($\sim 54\%$).
   - Model-vs-Model behavior differences (Opus 4.6 vs Gemini 3.1 Pro vs GPT-5.4).
