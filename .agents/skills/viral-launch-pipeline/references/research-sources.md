# Research Sources

## Contents

- Evidence rules
- Optional browser automation
- Source map
- Search patterns
- Research output

## Evidence Rules

- Browse for current market, competitor, and launch examples unless the user asks not to.
- Cite sources for market claims, competitor claims, metrics, and launch examples.
- Separate observed evidence from inference.
- Do not fabricate customer language. Quote sparingly and attribute.
- Prefer first-party pages, docs, changelogs, customer reviews, Reddit/forum posts, YouTube transcripts, X posts, Product Hunt, app marketplaces, and credible news.

## Optional Browser Automation

Use `agent-browser` for source-heavy research when available, especially for X posts, Reddit/forum threads, YouTube pages, Product Hunt launches, competitor pages, and screenshot-backed evidence.

Check first:

```bash
command -v agent-browser
```

If missing, do not install automatically. Ask the user before running:

```bash
npm install -g agent-browser
agent-browser install
```

Suggested commands:

```bash
agent-browser open https://example.com
agent-browser snapshot -i
agent-browser screenshot source.png
agent-browser close
```

Use snapshots to extract compact page structure and refs. Record URLs and summarize findings in the Evidence Map. If browser automation is unavailable or the user declines installation, continue with normal search and browsing.

## Source Map

Use the most relevant sources for the category:

- Company: homepage, docs, blog, changelog, demo videos, founder posts, case studies.
- Competitors: positioning pages, comparison pages, pricing, reviews, changelogs.
- Customer language: Reddit, Hacker News, G2/Capterra, app reviews, Discord/forum excerpts supplied by user, support docs, public comments.
- Viral patterns: X launches in adjacent categories, Product Hunt top launches, YouTube outlier videos, high-engagement demo posts.
- Category context: analyst posts, benchmark reports, news, keyword trends when available.

## Search Patterns

Run targeted searches such as:

```text
"[category]" "launch" "X" OR "Twitter"
"[competitor]" "alternative" "reddit"
"[problem]" "frustrated" OR "hate" OR "annoying"
"[category]" "Product Hunt" "launch"
"[product type]" "demo" "AI" site:x.com
"[category]" "before after" OR "workflow"
```

For YouTube, look for outliers: videos with unusually high views relative to channel size. Extract title patterns, thumbnail promise, opening hook, and proof sequence.

## Research Output

Produce this evidence map before writing:

```markdown
## Evidence Map

### Customer Pain
| Pain | Customer language | Source | Launch implication |
|---|---|---|---|

### Category Cliches
| Phrase or claim | Why it is weak | Better counter-position |
|---|---|---|

### Competitor Positions
| Competitor | Claim | Gap | Counter-position |
|---|---|---|---|

### Viral Patterns
| Example | Hook pattern | Demo/proof pattern | Useful lesson |
|---|---|---|---|

### Novelty Candidates
| Candidate | Evidence | Risk | Score 1-10 |
|---|---|---|---|
```
