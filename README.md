# Viral Launch Pipeline

[![Install Skill](https://img.shields.io/badge/install-npx%20skills%20add-111827)](#install)

A Codex skill and plugin for building research-driven X/Twitter, LinkedIn, and YouTube product launches.

The skill runs a full launch workflow: intake, market research, customer-language mining, competitor positioning, bold-claim extraction, hook writing, demo narrative, critique passes, weapons check, and final launch-pack validation.

## Install

Install with the open skills CLI:

```bash
tmp="$(mktemp -d)" && (cd "$tmp" && npx skills add tylergibbs1/virallaunchskill --skill viral-launch-pipeline -g -a codex --copy -y)
```

This runs the installer from a throwaway directory so `npm` does not inherit `package.json` overrides from whatever project you are currently in.

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
Use $viral-launch-pipeline to research, position, write, critique, and finalize an X, LinkedIn, and YouTube launch for my product.
```

For full-pipeline launch work, the skill launches the specialist subagent pipeline automatically:

```text
Use $viral-launch-pipeline to turn my product into a full launch pack.
```

Full-pipeline requests now require the launch pack to include `## Subagent Execution`, showing whether specialist subagents were spawned or why the skill fell back to sequential role passes.

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
- Final X post/thread, LinkedIn launch post, and/or YouTube launch script
- YouTube titles, thumbnail promise, Shorts script, long-form outline, and pinned comment when relevant
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
