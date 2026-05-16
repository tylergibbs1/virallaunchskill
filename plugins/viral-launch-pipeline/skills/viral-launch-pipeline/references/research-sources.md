# Research Sources

## Contents

- Evidence rules
- Retrieval budget
- Tool order
- Source map
- Search patterns
- Research output

## Evidence Rules

- Browse for current market, competitor, and launch examples unless the user asks not to.
- Prefer built-in web search/browsing tools when they are available.
- Cite sources for market claims, competitor claims, metrics, and launch examples.
- Separate observed evidence from inference.
- Do not fabricate customer language. Quote sparingly and attribute.
- Prefer first-party pages, docs, changelogs, customer reviews, Reddit/forum posts, YouTube transcripts, X posts, LinkedIn posts, Product Hunt, app marketplaces, and credible news.

## Retrieval Budget

Use the minimum research needed to support the launch angle.

Start with one broad search per source class that matters for the request:

- Company/product facts
- Competitors/category claims
- Customer language
- Launch/outlier patterns

Search again only when:

- The top results do not answer the core question.
- A required fact, source, date, capability, competitor claim, or customer phrase is missing.
- The user asks for exhaustive research or a platform-specific comparison.
- A hard-to-reach source needs browser inspection.
- The draft would otherwise contain an important unsupported factual claim.

Do not search again to improve wording, add decorative examples, or support a claim that can safely be made generic.

## Tool Order

1. Use built-in web search/browsing tools first for normal source discovery, source opening, and citation collection.
2. Use `agent-browser` for hard-to-reach sources: pages that block normal fetches, require interaction, need logged-in/session navigation, rely on client-side rendering, or need screenshots/accessibility snapshots for evidence.
3. If both are unavailable, continue with whatever search tools are available and clearly note source limitations.

When `agent-browser` would help, check first:

```bash
command -v agent-browser
```

If missing, do not install automatically. Ask the user before running:

```bash
npm install -g agent-browser
agent-browser install
```

Suggested `agent-browser` commands:

```bash
agent-browser open https://example.com
agent-browser snapshot -i
agent-browser screenshot source.png
agent-browser close
```

Use snapshots to extract compact page structure and refs. Record URLs and summarize findings in the Evidence Map. If browser automation is unavailable or the user declines installation, fall back to built-in web/search tools.

## Source Map

Use the most relevant sources for the category:

- Company: homepage, docs, blog, changelog, demo videos, founder posts, case studies.
- Competitors: positioning pages, comparison pages, pricing, reviews, changelogs.
- Customer language: Reddit, Hacker News, G2/Capterra, app reviews, Discord/forum excerpts supplied by user, support docs, public comments.
- Viral patterns: X launches, LinkedIn launches, Product Hunt top launches, YouTube outlier videos, YouTube Shorts, high-engagement demo posts, and founder/company launch narratives in adjacent categories.
- Category context: analyst posts, benchmark reports, news, keyword trends when available.

## Search Patterns

Run targeted searches such as:

```text
"[category]" "launch" "X" OR "Twitter"
"[category]" "launch" "LinkedIn"
"[product type]" "launch" "LinkedIn" "founder"
"[competitor]" "alternative" "reddit"
"[problem]" "frustrated" OR "hate" OR "annoying"
"[category]" "Product Hunt" "launch"
"[product type]" "demo" "AI" site:x.com
"[product type]" "demo" "AI" site:linkedin.com/posts
"[product type]" "launch" "YouTube"
"[product type]" "demo" "YouTube"
"[category]" "YouTube Shorts" "launch"
"[category]" "before after" OR "workflow"
```

For YouTube, look for outliers: videos with unusually high views relative to channel size. Extract title patterns, thumbnail promise, first 5-second hook, retention beats, demo sequence, proof sequence, CTA, and pinned comment patterns.

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
