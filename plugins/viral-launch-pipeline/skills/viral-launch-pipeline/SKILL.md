---
name: viral-launch-pipeline
description: Researches, positions, writes, critiques, and packages product launches for X/Twitter, LinkedIn, and optional YouTube launch videos using a multi-pass agent pipeline. Use when creating launch posts, LinkedIn launch posts, X launch threads, YouTube launch scripts, Shorts scripts, demo narratives, viral launch positioning, bold claims, hooks, social distribution plans, or when the user asks to turn a product into a high-attention launch.
---

# Viral Launch Pipeline

Run a research-first launch workflow that produces a complete launch pack for X/Twitter, LinkedIn, optional YouTube launch videos, or any combination: market insights, bold claim, hooks, narrative, demo script, critique history, platform-specific posts, and distribution plan.

Do not promise virality. Optimize for novelty, clarity, proof, and shareability.

## Outcome

Success means the user receives a usable launch pack with:

- A source-backed bold claim that is specific, defensible, and non-generic.
- Platform-native launch drafts for the requested channels.
- A short evidence trail showing what informed the angle.
- A subagent execution log when a full pipeline is requested.
- Clear critique notes showing what was rejected or rewritten.
- Validation completed or a clear explanation of what could not be checked.

For multi-step work, start with a brief visible update before tools. Make progress with reasonable assumptions; ask only when missing information would materially change the launch angle or create claim risk.

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

Run the pipeline as role passes. Codex only spawns subagents when the user explicitly asks for subagents, parallel agents, delegation, or agent work. A normal request to "create a launch pack" is not enough.

If the current user prompt does not explicitly ask to spawn/use subagents, run parallel agents, delegate to agents, or run the whole agent pipeline with subagents, stop before research and ask this exact question:

```text
Do you want me to spawn the specialist launch subagents for the full pipeline?
```

Do not create or finalize the launch pack until the user answers. If the user says yes, spawn the required subagents below. If the user says no, run the same personalities sequentially and record `Mode: sequential-fallback` in `## Subagent Execution`.

For full-pipeline work, do not silently simulate subagents in the main context. Spawn the Research Swarm, synthesize results, then spawn Positioning, Writing, and Critique groups as needed. If subagents are unavailable, blocked, or unsupported by the current environment, state that in `## Subagent Execution` and run the same personalities sequentially.

## Mandatory Subagents

When the user explicitly authorizes subagents, launch these required subagents before writing the final launch:

- **Research Swarm**: Market Anthropologist, Underground Listener, Outlier Archivist, Enemy Mapper, Founder Mythmaker.
- **Positioning Room**: Novelty Hunter, Claim Blacksmith, Category Rebel, Proof Broker.
- **Writing Room**: Hook Assassin, Narrative Architect, Demo Director, Launch Copywriter.
- **Critique Room**: Hook Prosecutor, Weapons Inspector, Plainspoken Parent, Market Skeptic.

Run them in phase-based waves if concurrency is limited. Do not finalize the launch pack until the required subagent results have been synthesized through manager gates.

Only use `Mode: sequential-fallback` when the user declines subagents or subagent spawning is genuinely unavailable, blocked, or unsupported. In that case, explain the reason in `## Subagent Execution` and run the same personalities sequentially.

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

- Distinguish source-backed facts from creative framing.
- Lead with a specific bold claim, not a generic announcement.
- Answer in the first beat: what launched, why it matters, why it has not existed like this before.
- Make the body prove the claim through demo moments, before/after contrast, proof, and specificity.
- Cut lines that only say the product is powerful, seamless, intelligent, streamlined, or built for modern teams.
- Show what should be shown visually; do not over-explain demoable behavior.
- Keep the paper trail concise: rejected claims, hook iterations, critiques, and why the final version won.

If support is thin, use placeholders or labeled assumptions instead of inventing metrics, customer outcomes, product capabilities, dates, or competitive claims.

## Output

Use [references/output-pack.md](references/output-pack.md) as the final structure.

Always include:

- Research summary with sources
- Subagent execution log
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

Stop once the launch pack meets the outcome criteria with enough evidence to support concrete claims. Do not keep researching only to improve phrasing or add nonessential examples.
