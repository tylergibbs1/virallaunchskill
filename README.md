# Viral Launch Pipeline

[![Install Skill](https://img.shields.io/badge/install-npx%20skills%20add-111827)](#install)

A Codex skill and plugin for building research-driven X/Twitter and LinkedIn product launches.

The skill runs a full launch workflow: intake, market research, customer-language mining, competitor positioning, bold-claim extraction, hook writing, demo narrative, critique passes, weapons check, and final launch-pack validation.

## Install

Install with the open skills CLI:

```bash
npx skills add tylergibbs1/virallaunchskill --skill viral-launch-pipeline -y
```

Or install directly in Codex with `$skill-installer`:

```text
$skill-installer https://github.com/tylergibbs1/virallaunchskill/tree/main/.agents/skills/viral-launch-pipeline
```

Restart Codex after install if the skill does not appear immediately.

## Optional Browser Research

For heavier launch research, install `agent-browser` so the skill can inspect source pages, X posts, LinkedIn posts, Reddit/forum threads, YouTube pages, Product Hunt launches, and competitor sites with compact snapshots:

```bash
npm install -g agent-browser
agent-browser install
```

The skill treats this as optional. If `agent-browser` is not installed, it will continue with normal web/search tools.

## Use

Invoke it explicitly:

```text
Use $viral-launch-pipeline to research, position, write, critique, and finalize an X and LinkedIn launch for my product.
```

To trigger the parallel specialist workflow, ask for the agent pipeline:

```text
Use $viral-launch-pipeline and run the whole agent pipeline with subagents for my product launch.
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
- Final X post/thread and/or LinkedIn launch post
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
