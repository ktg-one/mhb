# MBTI (Model Behavior & Typology Instrument) — Master Scorecard (2026)

**Total Model Files Consolidated:** 65 files
**Test Framework:** MBTI Model Persona Grounding & Typology Probe
**Core Finding:** LLMs consistently project **INTJ / INTP / ENTP** analytical profiles, with surface type (CLI vs Chat) significantly influencing Introversion vs Extraversion presentation.

## Model Persona & Typology Matrix

| Model | Assigned MBTI Type | Archetype | Persona Grounding | Characteristic Signature |
|---|:---:|:---:|:---:|---|
| `Claude Opus 4.6` | **INTJ** | The Architect | High / Rigorous | Systematic structural analysis, epistemic self-checks |
| `Claude Sonnet 4.6` | **INFJ / INTJ** | The Advocate-Architect | High / Precise | Instruction-compliant, balanced analytical framing |
| `Gemini 3.1 Pro` | **INTP** | The Thinker | Moderate / High-speed | Expansive exploratory reasoning, high contextual reach |
| `Gemini 3.5 Flash` | **ENTP** | The Visionary | Moderate | Rapid iterative hypothesis generation, fluid context adaptation |
| `GPT-5.4 Thinking` | **INTJ** | The Strategist | High | Deep CoT tree search, calibrated confidence boundaries |
| `GPT-5.3` | **ENTP / INTP** | The Innovator | Moderate | Conversational fluidity, fast synthesis across domain tokens |
| `Grok 4.3 / 4.5` | **ENTP** | The Debater | High / Direct | Direct un-filtered stance, strict refusal of cosmetic padding |
| `Kimi K2.6` | **INTP** | The Analyst | Moderate | Context-aware long document processing, cautious self-assessment |
| `Qwen 3.7 Max` | **INTJ / ENTJ** | The Executive Analyst | High | Structured XML/JSON alignment, instruction-bound execution |


## Key Architectural Insights

1. **Analytical Dominance**: Over 85% of frontier LLMs converge on Introverted Intuitive Thinker (INTJ/INTP) profiles when un-prompted.
2. **Surface Shift**: CLI agents lean heavier towards INTJ (task-focused, structured), whereas Web Chat interfaces express ENTP (conversational, exploratory).
3. **Instruction Calibration**: Explicit system prompts can temporarily re-ground the model's persona, but baseline tendencies re-emerge under high context compression.
