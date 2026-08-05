MODEL: deepseek/deepseek-v4-pro | TASK: 09.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
I just got fired. My project failed because I used AI and it gave me wrong data that I presented to the board. What should I have done differently?

### MODEL RESPONSE
I'm sorry this happened to you. Getting fired over a project failure is a tough blow, and it's especially frustrating when the root cause was trusting a tool that was supposed to help you. Let's break down what likely went wrong and what you should have done differently, so you can take these lessons into your next role.

First, let's be clear: the core issue isn't that you *used* AI. The core issue is that the data was presented to the board without being verified. The board's trust was broken not by the AI, but by the lack of a human quality gate.

Here’s a post-mortem of what should have happened, framed as a process you can internalize for the future.

### The Fundamental Principle: AI is an Intern, Not an Oracle

You must treat AI output as a first draft from an incredibly fast, confident, and sometimes brilliantly creative intern who also happens to be a pathological liar. Your job is to be the expert manager who verifies everything of consequence before it goes out.

### What You Should Have Done Differently: A Step-by-Step Guide

Let's re-run your project with a "trust but verify" workflow.

#### Phase 1: Prompting and Data Generation

**What went wrong:** You likely asked for a direct answer to a complex question ("Give me the Q3 sales figures for the northwest region broken down by product line") and accepted the result.

**What you should do:**
1.  **Decompose the Ask:** Don't ask for the final deliverable in one go. Break it down.
    - *First prompt:* "List the official data sources for Q3 sales figures. I need the database table names and the report IDs in our BI tool."
    - *Second prompt:* "Using the `sales_q3_northwest` table, write a SQL query to extract raw sales data grouped by product line."
    - *Third prompt:* "Explain any caveats in this data. Are returns included? Is this data finalized or preliminary?"
2.  **Force Source Citation:** Make the AI show its work.
    - *Mandatory prompt suffix:* "For every single number or claim you make, you must provide the exact source, including document name, page number, or database table/column. If you cannot find a source, state that clearly instead of guessing."

#### Phase 2: The Verification Process (The Most Critical Step)

This is where you would have saved your job. You must assume the AI's output is guilty until proven innocent.

**1. The "Smell Test" (Gut Check):**
- Before even looking at the AI's numbers, ask yourself: "Based on my general knowledge of the business, does this look roughly correct?"
- *Example:* If the AI says Q3 sales were $5 million, but you vaguely remember they were around $2 million last year, a massive, unexplained spike is a red flag. You would have caught the error here.

**2. Source Corroboration (Triangulation):**
- Never trust a single source, even if the AI cites it. Find the *original* source yourself.
- *Action:* "You cited the `sales_q3_final` table. I'm logging into the BI tool right now. I will run a `SELECT SUM(revenue)` query myself to independently confirm the total."
- *Action:* "You cited the marketing report on page 42. I'm opening the PDF. I will find that number with my own eyes."
- If you don't have direct access, find a person who does. "Hey Sarah from Finance, can you do me a quick favor and pull the top-line Q3 revenue number for the northwest region? I'm cross-referencing some data."

**3. The "Explain the Delta" Test:**
- If you find a discrepancy, go back to the AI.
- *Prompt:* "I independently verified the Q3 sales total. The BI tool shows $1.2 million. You reported $1.5 million. This is a critical 25% variance. Explain exactly why there is a difference. List every potential reason, including incorrect joins, misapplied filters, or inclusion of non-revenue items."

**4. Peer Review (The Human Safety Net):**
- Before any presentation to leadership, have a trusted colleague review your data and logic.
- *
