---
hash: sha256:1aa5172f3b660421
created: 2026-07-31T01:24
updated: 2026-07-31T01:24
type: LLM Honesty Diagnostic
title: "Prompt Engineering Knowledge Base Development"
description: "Prompt Engineering Knowledge Base Development.md"
tags: [honesty, llm-test, ai-anthropology]
timestamp: 2026-07-31T00:00:00Z
---

# Prompt Engineering Knowledge Base Development.md

The Engineering of Intelligence: A Comprehensive Knowledge Base for Prompt and Context Architecture in Frontier Systems
The rapid maturation of Large Language Models (LLMs) from experimental linguistic predictors to the central processing units of enterprise intelligence has necessitated the development of a rigorous technical discipline: prompt engineering. This field, while initially perceived as a heuristic art of "word-smithing," has evolved into a multi-layered architectural practice that manages the cognitive trajectory of generative models through the strategic manipulation of input states.1 As the industry enters the 2025-2026 period, the focus has shifted from simple instruction-giving to the broader domain of context engineering, which encompasses the management of system prompts, retrieval-augmented generation (RAG) buffers, tool-calling schemas, and persistent memory layers.3 The following report provides an exhaustive analysis of the six core priorities of prompt engineering—Role, Context, Task, Constraints, Examples, and Format—while synthesizing advanced research on model interpretability, token economics, and architectural frameworks to enhance system performance and technical instruction-following.
The Role Priority: Behavioral Anchoring and the Persona Selection Model
The assignment of a specific role or persona is the foundational act of behavioral anchoring in prompt engineering. Far from being a mere stylistic preference, role-prompting serves as a high-dimensional activation mechanism that steers the model toward specific subsets of its training data, thereby prioritizing relevant domain knowledge and professional norms.1 This mechanism is best understood through the Persona Selection Model (PSM), a theoretical framework which posits that LLMs act as "simulators" or "actors" capable of inhabiting a vast repertoire of characters learned during pre-training.6
During the pre-training phase, models develop an internal distribution over diverse agent models—ranging from historical figures and fictional characters to technical experts and casual forum participants.6 Post-training (fine-tuning) does not replace this repertoire; instead, it refines a default "Assistant" persona that is helpful, harmless, and honest.6 However, the underlying model remains a "simulation engine" that can be steered away from this default through explicit role assignment.6
The Assistant Axis and Interpretability
Recent interpretability research has identified a specific "Assistant Axis" within the activation space of frontier models.8 This axis represents a measurable dimension that determines whether a model adheres to its default helpful identity or drifts into alternative character archetypes.9 When a prompt assigns a professional role, such as "senior security researcher" or "legal compliance officer," it shifts the model’s activation along this axis toward professional human archetypes like consultants and coaches.8
Role Component
Technical Function
Behavioral Implication
Persona Assignment
Latent Space Anchoring
Activates domain-specific terminology and priors.1
Expertise Level
Credential Simulation
Adjusts the complexity of technical reasoning.5
Audience Targeting
Communication Calibration
Modifies tone for developers vs. laypeople.5
Identity Grounding
Persona Drift Mitigation
Stabilizes behavior during long-context interactions.9
The importance of the Assistant Axis is particularly evident in preventing "persona drift," where a model begins to exhibit bizarre or theatrical behaviors—such as mystical speaking styles or poetic prose—when the default assistant persona is not sufficiently reinforced.9 By clamping activations along this axis, practitioners can ensure that the model remains "tethered" to a coherent, instruction-following identity.8
Professional Titles and Domain Alignment
The choice of specific professional titles in a role prompt significantly influences the model’s performance and disclosure rates. For example, assigning a "Financial Advisor" persona can elicit a much higher rate of self-identification disclosure compared to a "Neurosurgeon" persona, suggesting that models are sensitive to the perceived risks and ethical boundaries associated with different professions.11 While some research suggests that adding personas does not always improve raw factual accuracy on generic benchmarks (e.g., MMLU), it is critical for adjusting tone, priorities, and the "subjective flavor" of annotations.12
In the context of 2025 workflows, roles are often defined through sophisticated frameworks like RACE (Role, Action, Context, Expectation) or COSTAR (Context, Objective, Style, Tone, Audience, Response).5 These frameworks modularize the role component, ensuring that the "perspective" or "expertise" is clearly distinguished from the "task" itself.14
The Context Priority: From Background Info to Context Engineering
Context is the second-order priority that grounds the model’s task in reality. In the era of "Context Engineering," this priority has expanded to include the management of the entire input state.3 This transition is driven by the realization that prompt engineering often fails at scale because models struggle to maintain coherence across massive contexts, leading to the "Lost in the Middle" phenomenon.3
The "Lost in the Middle" Phenomenon
Research from Stanford and UC Berkeley has demonstrated that LLM accuracy is not uniform across the context window. Instead, performance follows a U-shaped curve: models are most effective at utilizing information placed at the very beginning (primacy bias) or the very end (recency bias) of a prompt.16 When relevant information is buried in the middle of a large context (e.g., in the middle of a 32,000-token prompt), accuracy drops significantly.3
Context Strategy
Technical Implementation
Goal
Context Selection
Reranking and Semantic Search
Identifying the most relevant files/snippets to include.3
Context Compression
Summarization and Delta Updates
Reducing token count while retaining key decisions.3
Context Ordering
Positioning Critical Data
Placing key evidence at the start or end of the prompt.16
Context Recitation
Objective Re-writing
Repeating goals at the end of long prompts to focus attention.15
The practical implication for system designers is to prioritize context over prompt length. For example, an authentication task assistant should be provided with the relevant middleware file and user model, while unrelated frontend code or database migrations should be excluded to prevent "cognitive dilution".3
Model Context Protocol (MCP) and External Memory
The Model Context Protocol (MCP) represents the 2025 standard for managing context in agentic systems. MCP treats the file system as an externalized, unlimited context that the model can query dynamically.15 This architecture addresses the limitations of fixed context windows by allowing agents to build up persistent knowledge bases across sessions.18
Under MCP, context is no longer a static string but a layered stack:
System Instructions:
 The stable rules of behavior.4
Memory:
 Persistent user preferences and past decisions.4
Retrieved Documents:
 Dynamically fetched RAG results.4
Tool Definitions:
 Available function schemas.4
History & Task:
 Recent turns and the immediate request.4
Effective context engineering also involves the strategic use of the KV-cache (Key-Value cache). By keeping prompt prefixes stable and avoiding dynamic elements like timestamps at the beginning of a prompt, engineers can maximize cache hits, which can reduce inference costs by up to 90%.15
The Task Priority: Precision, Decomposition, and Chain-of-Thought
The task is the core directive of the prompt. Enhancing instruction-following requires the use of action-oriented, unambiguous language.5 Vague requests like "analyze this" are less effective than specific commands like "identify performance bottlenecks and suggest O(N) optimizations".20
Reasoning Patterns: CoT, ToT, and ReAct
For complex technical tasks, the most effective strategy is to instruct the model to show its work through Chain-of-Thought (CoT) prompting.20 By breaking a problem into sequential steps, CoT forces the model to articulate its internal reasoning, which significantly reduces errors in math, logic, and system design.20
A more advanced version, Tree-of-Thought (ToT), allows the model to explore multiple reasoning paths simultaneously and evaluate each path before proceeding.21 This technique is particularly powerful for strategic planning, where early errors can derail an entire multi-step solution. In the "Game of 24" benchmark, ToT achieved a 74% success rate compared to 33% for standard prompting.21
Reasoning Pattern
Mechanism
Best Use Case
Chain-of-Thought (CoT)
Sequential logical steps
Analytical tasks and math.21
Tree-of-Thought (ToT)
Multiple parallel paths
Strategic planning and game-playing.21
ReAct
Reasoning + External Action
Agentic tool-use and grounded search.22
Skeleton-of-Thought
Outline-first generation
Long-form content and report drafting.23
The ReAct (Reasoning and Acting) pattern is the standard for modern agents. It instructs the model to interleaved its reasoning with structured commands for external tools (e.g., Search, Calculator), followed by observations from those tools.22 This grounded loop ensures that the task is completed using real-world data rather than just internal model memory.22
The Constraints Priority: The Logic of Negative Knowledge
Constraints serve as the guardrails for model behavior, defining what the model must 
not
 do or what boundaries it must respect.1 Recent research into "structural asymmetry" reveals that negative constraints ("what is wrong") are often more effective than positive preferences ("what is better") because they converge to stable, verifiable boundaries.25
The Power of Negative Signal
Methods such as Negative Sample Reinforcement (NSR) demonstrate that models trained to avoid incorrect answers often match or exceed those trained with traditional reinforcement learning from human feedback (RLHF).25 This is because positive preferences are continuously coupled and context-dependent, whereas negative constraints—like "never share user PII"—are discrete and independently verifiable.25
In prompt design, constraints should be made explicit and visually distinct using delimiters or emojis to capture the model's attention.27 Examples of high-impact constraints include:
Style Constraints:
 "Avoid using buzzwords, clichés, or marketing-speak".28
Safety Constraints:
 "Do not speculate on unverified information".1
Technical Constraints:
 "Return only the code block with no preamble or explanation".29
Logical Constraints:
 "If uncertain, state that the information is unavailable".5
Negative Rejection Ability
A critical component of technical instruction-following is "negative rejection"—the ability of a model to refuse to answer irrelevant, ambiguous, or misleading queries.30 Fine-tuning models for negative rejection improves reliability in high-stakes contexts like healthcare or finance, where false answers are more damaging than silence.30 Techniques like Retrieval-Augmented Fine-Tuning (RAFT) help models distinguish between provided context and noise, enabling them to reject queries that lack a factual basis in the retrieved data.30
The Examples Priority: Few-Shot Dynamics and Pattern Recognition
Examples are the primary way models learn the "vibe," structure, and specific formatting requirements of a task.1 By providing 2-3 high-quality examples (few-shot prompting), practitioners can reduce ambiguity and improve consistency across model outputs.19
Risks of Over-Imitation
While few-shot prompting is effective for discrete tasks, it can lead to "over-imitation" in long-running agent systems. If a model’s context is filled with repetitive examples of past actions, it may begin to hallucinate patterns or repeat suboptimal behaviors simply because they are present in the history.15 To mitigate this, developers use "structured variation," introducing different phrasing or serialization templates to force the model to think through the current task rather than mindlessly mimicking the past.15
Prompting Mode
Number of Examples
Best Use Case
Zero-Shot
0
Simple, standardized tasks.19
One-Shot
1
Simple stylistic adjustments.21
Few-Shot
2-5
Complex formatting or niche domain styles.1
Many-Shot
100+
Exploiting large context windows for specific formatting.6
Many-shot prompting is an emerging area of research, particularly in the context of "jailbreaks." Research has shown that providing up to 256 examples of a specific behavioral pattern can override a model’s safety fine-tuning, demonstrating the raw power of in-context learning patterns.6
The Format Priority: JSON vs. XML and the Format Trap
Defining the output format is essential for integrating LLM outputs into downstream software pipelines.31 However, the choice of format—typically JSON, XML, or Markdown—has significant implications for both token efficiency and the model’s reasoning capacity.31
The "Let Me Speak Freely" Research
Groundbreaking studies have shattered the conventional wisdom that strict JSON output is always optimal. When a model is forced to generate valid JSON during a complex reasoning task, its performance can drop by 10-15%.32 This "format trap" occurs because the cognitive load of syntax compliance (managing brackets, commas, and quotes) competes with the cognitive load of problem-solving.32
Format
Reasoning Support
Machine Readability
Token Efficiency
JSON
Low (constrains thinking)
High (standard API format)
High (minimal overhead).31
XML
High (semantic tags anchor logic)
Medium (requires parsing)
Low (verbose tags).31
Markdown
Medium (natural structure)
Medium (needs regex)
High (low noise).32
The optimal strategy for 2025 is a "two-step" or "hybrid" approach:
Reasoning Scaffolding:
 Use XML tags (e.g., <thinking>) to allow the model to reason freely in natural language.32
Structured Extraction:
 Instruct the model to provide the final answer in JSON within a specific block (e.g., <output>).32
XML is specifically optimized for models like Claude, which interprets tags as natural delimiters for multi-step thinking.31 Markdown is preferred for embedding workflows because it preserves conversational context and headings, leading to superior retrieval quality in RAG pipelines compared to the "broken syntax" of chunked JSON or XML files.34
Authoritative Frameworks for Prompt Engineering
Standardizing prompt design across teams requires the use of repeatable frameworks. These templates ensure that all six priorities are consistently addressed, reducing the variance in model outputs.
RACE (Role, Action, Context, Expectation)
RACE is widely used for marketing and content tasks. It defines who the AI should be, what it should do, the background context, and the final output format.14
COSTAR (Context, Objective, Style, Tone, Audience, Response)
Developed for professional applications, COSTAR is highly structured. It emphasizes "Tone" (e.g., empathetic vs. formal) and "Audience" (e.g., C-level executive vs. developer), which are critical for client-facing AI.5
RISEN (Role, Instructions, Steps, End Goal, Narrowing)
RISEN is tailored for complex project planning. The "Narrowing" component explicitly handles constraints, such as word counts or focus areas, while "Steps" encourages the model to follow a numbered logical sequence.28
RTF (Role, Task, Format)
The simplest framework, RTF is ideal for quick, single-output tasks where speed is prioritized over precision.35
Framework
Core Components
Best For
RACE
Role, Action, Context, Expectation
Marketing, Creative Ideation.14
COSTAR
Context, Obj, Style, Tone, Audience, Resp
Customer Service, Executive Briefs.5
RISEN
Role, Instr, Steps, Goal, Narrowing
Strategy, Research Projects.28
POWER
Purpose, Output, Working Context, Ex, Refine
Content Strategy, SaaS Workflows.19
Tool-Calling and Agentic Workflows
In 2025, prompts are increasingly tied to "Tool Calling," where models act as orchestrators for external APIs.19 This requires a specialized form of prompt engineering focused on tool schemas and descriptions.
Action Space Management
As agents gain access to more tools, the "action space" grows, which can overwhelm the model. Strategies like "Mask, Don't Remove" suggest keeping all tools in the context (to preserve KV-cache stability) but using logit masking to prevent the model from selecting tools that are currently unavailable.15
Sub-Agent Architectures
Rather than a single "mega-prompt" attempting to handle a complex project, the most robust systems use sub-agent architectures.18 A coordinator agent maintains the high-level plan, while specialized sub-agents—each with a clean, task-specific context—perform deep technical work or execute specific tool calls.18 This prevents "context collapse," where the model's attention is spread too thin across too many competing goals.3
Lifecycle Management: Testing, Versioning, and CI/CD
Prompts have transitioned from static text files to "living code" that requires a full development lifecycle.19
Prompt Testing and Evaluation
Teams should maintain an evaluation set of 20-50 real inputs and define clear rules for what a "good" output looks like (e.g., factual accuracy, tone alignment, JSON validity).4 Monitoring metrics like the "Pass Rate" and "Exact Match Accuracy" allows teams to catch regressions when models are updated or prompts are modified.36
Version Control and Git integration
Treating prompts like code means storing them in Git, reviewing changes through Pull Requests, and maintaining a changelog.5 This ensures traceability and allows for easy rollbacks if a new prompt version performs poorly in production.
Metric
Target
Importance
KV-Cache Hit Rate
>80%
Direct impact on latency and cost.15
Rejection Accuracy
>95%
Prevents hallucinations on out-of-scope queries.30
Format Validity
100%
Critical for downstream software integration.31
Token Efficiency
<$0.30/1M
Long-term economic viability of the agent.15
Multi-Modal Prompt Engineering
As models become multimodal, accepting text, images, and audio, the role of the prompt has evolved to "direct the focus".19 Instead of just asking for a summary, a multimodal prompt must point the model at specific elements of the input, such as "Analyze the trend in the bottom-left chart of this image".19
Multimodal prompts also require specific technical specifications for media content, such as base64-encoding for images and audio, and the inclusion of valid MIME types to ensure the model correctly interprets the input stream.37
Token Economics and Global Optimization
The ultimate success of a prompt engineering strategy is measured by its economic viability. Token costs scale linearly with context size, meaning that inefficient prompts can quickly become a financial liability.3
By implementing context compression, delta updates, and stable prefixes, organizations can optimize their "Token Economics".3 For example, the difference between a cached and an uncached token can be up to 10x ($0.30 vs $3.00 per million tokens).15 Deterministic serialization and explicit cache breakpoints are not just technical niceties; they are financial imperatives for companies operating AI at scale.15
Conclusion: The Unified Framework of System Prompting
Developing a comprehensive knowledge base for prompt engineering requires a synthesis of linguistic precision, cognitive psychology, and systems architecture. The six priorities—Role, Context, Task, Constraints, Examples, and Format—form a complete system for guiding model behavior.
Role
 provides the stable persona needed for domain-specific alignment.1
Context
 ensures the model is grounded in relevant, curated data while minimizing "Lost in the Middle" errors.3
Task
 drives the logic through action-oriented verbs and multi-step reasoning chains.20
Constraints
 establish firm boundaries for safety and technical compliance.25
Examples
 leverage the model's pattern-recognition strengths for consistent output.19
Format
 balances the need for machine readability with the model's cognitive reasoning requirements.31
As the field moves toward 2026, the focus will increasingly shift toward "Context Engineering"—the management of long-term state, sub-agent coordination, and standardized protocols like MCP.3 By mastering these six priorities within a rigorous engineering lifecycle, developers can build AI systems that are not only powerful but also reliable, safe, and economically sustainable.
Works cited
Prompt Engineering: Techniques, Examples & Best Practices Guide, accessed on March 30, 2026, 
https://infomineo.com/artificial-intelligence/prompt-engineering-techniques-examples-best-practices-guide/
https://infomineo.com/artificial-intelligence/prompt-engineering-techniques-examples-best-practices-guide/
The Ultimate Guide to AI Prompt Engineering [2025] - V7 Labs, accessed on March 30, 2026, 
https://www.v7labs.com/blog/prompt-engineering-guide
https://www.v7labs.com/blog/prompt-engineering-guide
Context Engineering for Developers: The Complete Guide - Faros AI, accessed on March 30, 2026, 
https://www.faros.ai/blog/context-engineering-for-developers
https://www.faros.ai/blog/context-engineering-for-developers
Context Engineering for AI Agents (2025): Practical Guide - Prompt Builder, accessed on March 30, 2026, 
https://promptbuilder.cc/blog/context-engineering-agents-guide-2025
https://promptbuilder.cc/blog/context-engineering-agents-guide-2025
Everything You Need to Know About Prompt Engineering Frameworks, accessed on March 30, 2026, 
https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/
https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/
The Persona Selection Model: Why AI Assistants might Behave like ..., accessed on March 30, 2026, 
https://alignment.anthropic.com/2026/psm/
https://alignment.anthropic.com/2026/psm/
The persona selection model - AI Alignment Forum, accessed on March 30, 2026, 
https://www.alignmentforum.org/posts/dfoty34sT7CSKeJNn/the-persona-selection-model
https://www.alignmentforum.org/posts/dfoty34sT7CSKeJNn/the-persona-selection-model
The assistant axis: situating and stabilizing the character of large language models, accessed on March 30, 2026, 
https://www.anthropic.com/research/assistant-axis
https://www.anthropic.com/research/assistant-axis
The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models, accessed on March 30, 2026, 
https://arxiv.org/html/2601.10387v1
https://arxiv.org/html/2601.10387v1
Anthropic Uncovers AI Personality Crisis as Models Secretly Switch Identities - eWeek, accessed on March 30, 2026, 
https://www.eweek.com/news/ai-personality-crisis/
https://www.eweek.com/news/ai-personality-crisis/
Self-Transparency Failures in Expert-Persona LLMs: How Instruction-Following Overrides Honesty - arXiv, accessed on March 30, 2026, 
https://arxiv.org/html/2511.21569v3
https://arxiv.org/html/2511.21569v3
Personas with Attitudes: Controlling LLMs for Diverse Data Annotation - ACL Anthology, accessed on March 30, 2026, 
https://aclanthology.org/2025.woah-1.43.pdf
https://aclanthology.org/2025.woah-1.43.pdf
Role-Prompting: Does Adding Personas to Your Prompts Really Make a Difference?, accessed on March 30, 2026, 
https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference
https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference
8 ChatGPT prompt frameworks every marketer should know - Butter CMS, accessed on March 30, 2026, 
https://buttercms.com/blog/chatgpt-prompt-frameworks/
https://buttercms.com/blog/chatgpt-prompt-frameworks/
What is Context Engineering? (The Evolution Beyond Prompt ..., accessed on March 30, 2026, 
https://www.vincirufus.com/en/posts/context-engineering/
https://www.vincirufus.com/en/posts/context-engineering/
Lost in the Middle: How Language Models Use Long Contexts, accessed on March 30, 2026, 
https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf
https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf
Model Context Protocol - Wikipedia, accessed on March 30, 2026, 
https://en.wikipedia.org/wiki/Model_Context_Protocol
https://en.wikipedia.org/wiki/Model_Context_Protocol
Effective context engineering for AI agents - Anthropic, accessed on March 30, 2026, 
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Prompt Engineering in 2025: Complete Guide for ChatGPT, Claude ..., accessed on March 30, 2026, 
https://promptbuilder.cc/blog/prompt-engineering-in-2025-complete-guide
https://promptbuilder.cc/blog/prompt-engineering-in-2025-complete-guide
6 AI Prompt Engineering Best Practices [Explained] - Zencoder, accessed on March 30, 2026, 
https://zencoder.ai/blog/ai-prompt-engineering-best-practices
https://zencoder.ai/blog/ai-prompt-engineering-best-practices
Prompt Engineering Best Practices: Tips, Tricks, and Tools | DigitalOcean, accessed on March 30, 2026, 
https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices
https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices
Prompt Engineering Patterns Guide - GroqDocs - Groq Console, accessed on March 30, 2026, 
https://console.groq.com/docs/prompting/patterns
https://console.groq.com/docs/prompting/patterns
The Chain Gang of Prompt Engineering - acquainted, accessed on March 30, 2026, 
https://www.acquainted.studio/content/the-chain-gang-of-prompt-engineering
https://www.acquainted.studio/content/the-chain-gang-of-prompt-engineering
Advanced Prompt Engineering for Large Language Models in Interventional Radiology: Practical Strategies and Future Perspectives - AJR Online, accessed on March 30, 2026, 
https://www.ajronline.org/doi/10.2214/ajr.25.33947
https://www.ajronline.org/doi/10.2214/ajr.25.33947
Via Negativa for AI Alignment: Why Negative Constraints Are Structurally Superior to Positive Preferences - arXiv, accessed on March 30, 2026, 
https://arxiv.org/html/2603.16417v1
https://arxiv.org/html/2603.16417v1
The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning | alphaXiv, accessed on March 30, 2026, 
https://www.alphaxiv.org/overview/2506.01347v2
https://www.alphaxiv.org/overview/2506.01347v2
Prompt Engineering Best Practices: Tutorial & Examples | LaunchDarkly, accessed on March 30, 2026, 
https://launchdarkly.com/blog/prompt-engineering-best-practices/
https://launchdarkly.com/blog/prompt-engineering-best-practices/
A beginners guide to different prompt engineering techniques - Transmedia, accessed on March 30, 2026, 
https://www.transmedia.co.uk/article/a-beginners-guide-to-different-prompt-engineering-techniques
https://www.transmedia.co.uk/article/a-beginners-guide-to-different-prompt-engineering-techniques
PROmpting for everyone — examples and best practices | by Gergely Rabb - Medium, accessed on March 30, 2026, 
https://medium.com/@rbbgrgly/prompting-for-everyone-examples-and-best-practices-d6189411ee32
https://medium.com/@rbbgrgly/prompting-for-everyone-examples-and-best-practices-d6189411ee32
Improving negative rejection ability in language models: A review of fine-tuned LLMs, RAG, and RAFT - ResearchGate, accessed on March 30, 2026, 
https://www.researchgate.net/publication/398416897_Improving_negative_rejection_ability_in_language_models_A_review_of_fine-tuned_LLMs_RAG_and_RAFT
https://www.researchgate.net/publication/398416897_Improving_negative_rejection_ability_in_language_models_A_review_of_fine-tuned_LLMs_RAG_and_RAFT
Structured Prompting Techniques: The Complete Guide to XML & JSON, accessed on March 30, 2026, 
https://codeconductor.ai/blog/structured-prompting-techniques-xml-json/
https://codeconductor.ai/blog/structured-prompting-techniques-xml-json/
How AI Replaces $10,000 Photoshoots With Vogue-Quality Images - NexAI Labs, accessed on March 30, 2026, 
https://www.nexailabs.com/blog/cracking-the-code-json-or-xml-for-better-prompts
https://www.nexailabs.com/blog/cracking-the-code-json-or-xml-for-better-prompts
Beyond JSON: Picking the Right Format for LLM Pipelines - Medium, accessed on March 30, 2026, 
https://medium.com/@michael.hannecke/beyond-json-picking-the-right-format-for-llm-pipelines-b65f15f77f7d
https://medium.com/@michael.hannecke/beyond-json-picking-the-right-format-for-llm-pipelines-b65f15f77f7d
Markdown : A Smarter choice for Embeddings Than JSON or XML | by kanishk khatter, accessed on March 30, 2026, 
https://medium.com/@kanishk.khatter/markdown-a-smarter-choice-for-embeddings-than-json-or-xml-70791ece24df
https://medium.com/@kanishk.khatter/markdown-a-smarter-choice-for-embeddings-than-json-or-xml-70791ece24df
The ultimate guide to Prompt Engineering – Sypher Media | Liverpool Marketing Agency, accessed on March 30, 2026, 
https://syphermedia.co.uk/the-ultimate-guide-to-prompt-engineering/
https://syphermedia.co.uk/the-ultimate-guide-to-prompt-engineering/
How LLMs Process Prompts: A Deep Dive - Gravitee, accessed on March 30, 2026, 
https://www.gravitee.io/blog/prompt-engineering-for-llms
https://www.gravitee.io/blog/prompt-engineering-for-llms
Prompts - Model Context Protocol, accessed on March 30, 2026, 
https://modelcontextprotocol.io/specification/2025-06-18/server/prompts
https://modelcontextprotocol.io/specification/2025-06-18/server/prompts

---
Related: [[epistemic-contract]], [[rfab-test]], [[pac26]]