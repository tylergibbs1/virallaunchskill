# Viral Launch Pipeline

A Codex skill and plugin for building research-driven X/Twitter product launches.

The skill runs a full launch workflow: intake, market research, customer-language mining, competitor positioning, bold-claim extraction, hook writing, demo narrative, critique passes, weapons check, and final launch-pack validation.

## Install

In Codex, run:

```text
$skill-installer https://github.com/tylergibbs1/virallaunchskill/tree/main/.agents/skills/viral-launch-pipeline
```

Restart Codex after install if the skill does not appear immediately.

## Use

Invoke it explicitly:

```text
Use $viral-launch-pipeline to research, position, write, critique, and finalize an X launch for my product.
```

Useful inputs:

- Product name and URL
- Target buyer
- Demo flow or screenshots
- Competitors
- Customer quotes or testimonials
- Proof points, metrics, or founder story

## What It Produces

- Research summary with sources
- Positioning options and selected bold claim
- Hook iterations with scores
- Final X post or thread
- Demo/video script when relevant
- Weapons Check table
- Distribution plan
- Human edit notes

## Repository Layout

```text
.agents/skills/viral-launch-pipeline/       # Repo-scoped skill
plugins/viral-launch-pipeline/              # Codex plugin package
.agents/plugins/marketplace.json            # Local plugin marketplace entry
```

The plugin package embeds the same skill under `plugins/viral-launch-pipeline/skills/viral-launch-pipeline`.

## Validate

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .agents/skills/viral-launch-pipeline
```

Validate a generated launch pack:

```bash
python3 .agents/skills/viral-launch-pipeline/scripts/validate_launch_pack.py path/to/launch-pack.md
```
