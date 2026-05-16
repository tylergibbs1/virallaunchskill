---
name: viral-launch-pipeline
description: Researches, positions, writes, critiques, and packages product launches for X/Twitter, LinkedIn, and optional YouTube launch videos using a multi-pass agent pipeline. Use when creating launch posts, LinkedIn launch posts, X launch threads, YouTube launch scripts, Shorts scripts, demo narratives, viral launch positioning, bold claims, hooks, social distribution plans, or when the user asks to turn a product into a high-attention launch.
---

# Viral Launch Pipeline

Run a research-first launch workflow that produces a complete launch pack for X/Twitter, LinkedIn, optional YouTube launch videos, or any combination: market insights, bold claim, hooks, narrative, demo script, critique history, platform-specific posts, and distribution plan.

Do not promise virality. Optimize for novelty, clarity, proof, and shareability.

## Workflow

Copy and update this checklist while working:

```markdown
Launch Progress:
- [ ] 1. Capture product intake
- [ ] 2. Research market, competitors, customers, and launch outliers
- [ ] 3. Extract positioning tensions and bold claims
- [ ] 4. Draft and score hooks
- [ ] 5. Build demo-driven narrative
- [ ] 6. Run critique passes and rewrites
- [ ] 7. Finalize launch pack
- [ ] 8. Validate deliverable
```

## Intake

Start by gathering or inferring:

- Product name, URL, and category
- Target buyer and painful existing behavior
- Product workflow or demo steps
- Differentiators, proof, metrics, founder story, customer quotes
- Launch constraints: target platform, post-only, video script, Shorts, long-form demo, thread, voice, claims to avoid

If critical product details are missing, ask only for the minimum needed to proceed.

## Research

Use current web research unless the user explicitly provides all source material or asks not to browse. Prefer built-in web search/browsing tools when available. Read [references/research-sources.md](references/research-sources.md) for source types, search patterns, and evidence rules.

Use `agent-browser` only when built-in web tools cannot reach a source reliably, when the page requires interaction, or when screenshot-backed/source-page inspection would materially improve the research. If unavailable, ask before installing global tools.

The research phase must produce:

- Market pain points in customer language
- Category cliches and dead phrases to avoid
- Competitor positioning and counter-positioning openings
- Viral launch patterns from similar categories
- Novelty candidates: what makes this feel newly possible

## Role Passes

Run the pipeline as role passes. When the user asks for agents, subagents, parallel research, the 21-agent pipeline, or the whole agent pipeline, spawn specialist subagents with the personalities in [references/subagent-orchestration.md](references/subagent-orchestration.md). If subagents are unavailable, execute the same personalities sequentially yourself.

Read [references/agent-roles.md](references/agent-roles.md) for the 21 role definitions and manager review gates.

Minimum required gates:

- Research Manager approves the evidence map before positioning.
- Positioning Manager approves the bold claim before writing.
- Editorial Manager approves hooks before the body/script.
- Weapons Check approves every final line.
- Mass-Market Clarity approves the final draft.

## Writing Standards

Use [references/scorecards.md](references/scorecards.md) for scoring.

Core rules:

- Lead with a specific bold claim, not a generic announcement.
- Answer in the first beat: what launched, why it matters, why it has not existed like this before.
- Make the body prove the claim through demo moments, before/after contrast, proof, and specificity.
- Cut lines that only say the product is powerful, seamless, intelligent, streamlined, or built for modern teams.
- Show what should be shown visually; do not over-explain demoable behavior.
- Keep a paper trail: rejected claims, hook iterations, critiques, and why the final version won.

## Output

Use [references/output-pack.md](references/output-pack.md) as the final structure.

Always include:

- Research summary with sources
- Positioning options and selected bold claim
- Hook iterations with scores
- Final X/Twitter post or thread, LinkedIn launch post, and/or YouTube launch script
- YouTube titles, thumbnail promise, Shorts script, and long-form outline when requested
- Weapons Check table
- Distribution plan
- Human edit notes for the final 5%

## Validation

Save the final launch pack as Markdown when the user wants files or when the work is substantial. Then run:

```bash
python3 scripts/validate_launch_pack.py path/to/launch-pack.md
```

Fix validation failures before finalizing. Validation catches missing sections and common generic launch language; it does not replace editorial judgment.
