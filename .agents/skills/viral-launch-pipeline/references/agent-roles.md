# Agent Roles

## Contents

- Operating rule
- Subagent orchestration
- Research roles
- Positioning roles
- Writing roles
- Critique roles
- Manager gates

## Operating Rule

These are role passes with distinct personalities. For full launch pipeline work, run them as real subagents automatically. Only run the same personalities sequentially in the main context when subagent spawning is unavailable, blocked, or unsupported. Each role returns concise findings, a score when applicable, and concrete edits.

## Subagent Orchestration

For concrete spawn groups, personalities, and prompt templates, read [subagent-orchestration.md](subagent-orchestration.md). Do not spawn all 21 agents blindly. Spawn only the independent agents needed for the current phase, then synthesize results through manager gates.

## Research Roles

1. **Intake Agent**: Extracts product facts, target buyer, demo steps, proof, constraints, and missing questions.
2. **Market Agent**: Defines category, buying triggers, existing workflows, urgency, and category maturity.
3. **Customer Language Agent**: Mines first-party customer phrasing, pain words, objections, desired outcomes, and emotional stakes.
4. **Reddit/Forum Agent**: Finds unfiltered complaints, workarounds, comparisons, and anti-patterns in user communities.
5. **YouTube Outlier Agent**: Studies outlier titles, thumbnail promises, openings, retention beats, Shorts, and demos in the category and adjacent categories.
6. **Social Launch Archive Agent**: Finds similar successful and failed X and LinkedIn launches; extracts hook, claim, proof, and format patterns.
7. **Competitor Agent**: Maps competitor claims, sameness, weak spots, and credible counter-positioning openings.
8. **Founder Story Agent**: Identifies origin story, enemy, insight, risk, or obsession that can make the launch feel human.

## Positioning Roles

9. **Novelty Extraction Agent**: Lists what feels newly possible, structurally different, or surprisingly specific.
10. **Bold Claim Agent**: Turns novelty into 5-10 claims that are clear, specific, defensible, and non-generic.
11. **Category Design Agent**: Decides whether to name a new category, reject an old category, or reframe the buyer's mental model.
12. **Proof Agent**: Matches each claim to demo moments, metrics, customer evidence, visual proof, or founder credibility.

## Writing Roles

13. **Hook Agent**: Writes at least 20 first-line hooks across formats: direct claim, enemy, impossible demo, before/after, contrarian, founder insight.
14. **Narrative Agent**: Builds the launch arc: old world, tension, breakthrough, demo, proof, implications, CTA.
15. **Demo Flow Agent**: Converts product workflow into a visual sequence where each beat proves the bold claim.
16. **Post Agent**: Writes X threads/posts and LinkedIn launch posts in platform-native voice without generic SaaS language.
17. **Script Agent**: Writes YouTube Shorts scripts, long-form demo outlines, voiceover, shot lists, titles, thumbnail promises, and pinned comments when relevant.

## Critique Roles

18. **Hook Critic**: Scores hooks for specificity, novelty, tension, clarity, and scroll-stopping power.
19. **Weapons Check Agent**: Attacks every line for invention novelty and copy intensity; cuts filler.
20. **Mass-Market Clarity Agent**: Flags jargon, unexplained terms, abstract claims, and anything a nontechnical reader would miss.
21. **Skeptic Agent**: Finds overclaims, unverifiable claims, audience mismatch, and reasons the market might not care.

## Manager Gates

Use manager gates to force iteration:

```markdown
### Manager Review
Decision: approve | revise
Score: /10
Blocking issues:
- ...
Required revision:
- ...
```

Required managers:

- **Research Manager**: Evidence is broad enough and not just company-supplied.
- **Positioning Manager**: Bold claim is specific, novel, valuable, and defensible.
- **Editorial Manager**: Hook and narrative earn attention without hype sludge.
- **Final Manager**: Final pack is usable by a founder, creative team, and editor.
