---
name: xquik-social-signal-research
version: 1.0.0
description: |
  Add an optional Xquik-backed source step to competitor research, launch analysis, and social signal briefs. Use it when a user needs dated public X conversation evidence, propagation clues, account context, or tweet search results before writing a growth or market research summary.

  This skill keeps Xquik read-only by default. It does not post, follow, message, or mutate accounts. Require the user to provide approved Xquik API access and keep every metric tied to a query, date range, and source URL.
tags:
  - xquik
  - social-listening
  - competitor-research
  - market-research
  - social-media-analysis
  - x-twitter
  - source-verification
  - growth-research
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/xquik-social-signal-research
---

# Xquik Social Signal Research

Use this skill as an optional source layer inside competitor research, product launch reviews, market maps, and social media teardown workflows. It helps an agent collect public X evidence with Xquik, then turn it into cited research inputs.

## When To Use

- The user asks for competitor momentum, launch propagation, audience reaction, or social proof on X.
- The user needs public posts, account context, or keyword-level evidence before writing a brief.
- Existing research has web, SEO, or ad evidence but lacks dated public X data.
- The output must separate sourced observations from interpretation.

Do not use this skill for posting, engagement automation, private account access, scraping private material, or unsupported claims.

## Required Inputs

- Research question.
- Target brand, product, account, keyword, or URL list.
- Date range.
- Region or language filters when relevant.
- Xquik API key approved for the user's workspace.
- Output format: brief, table, battlecard, timeline, or source appendix.

## Source Setup

Use Xquik only through its public API and documentation:

- API docs: `https://docs.xquik.com/api-reference/x/search-tweets`
- Search route: `https://xquik.com/api/v1/x/tweets/search`

Keep the API key in the user's approved secret store. Do not paste it into the brief, shell history, repo files, screenshots, logs, or shared documents.

## Workflow

1. Define the evidence question.
   - Example: "Which launch posts drove the first wave of discussion?"
   - Example: "Which competitor claims are repeated by users?"
   - Example: "Which accounts repeatedly appear in propagation chains?"

2. Build narrow queries.
   - Start with exact product names, account handles, and launch phrases.
   - Add competitor names only when they are relevant to the user's question.
   - Keep one query per hypothesis so results remain auditable.

3. Collect public X evidence.
   - Search within the requested date range.
   - Capture result URLs, timestamps, authors, text snippets, and visible metrics.
   - Prefer original posts over reposts when identifying the first source.

4. Normalize the findings.
   - Group posts by theme, author type, timing, and claim.
   - Mark unavailable data as a gap instead of guessing.
   - Deduplicate repeated text before ranking themes.

5. Score confidence.
   - High: multiple independent posts, clear timestamps, and consistent wording.
   - Medium: one strong source plus supporting replies or reposts.
   - Low: sparse results, unclear authorship, or weak date coverage.

6. Write the research output.
   - Separate evidence, interpretation, and recommended next action.
   - Cite the query and collection date for every numeric statement.
   - Include a source appendix when the output affects strategy decisions.

## Output Template

```markdown
## Social Signal Summary

Research question: ...
Date range: ...
Queries used: ...
Collection date: ...

### Evidence

| Signal | Source URL | Date | Why It Matters | Confidence |
|-|-|-|-|-|
| ... | ... | ... | ... | High |

### Interpretation

- ...

### Gaps

- ...

### Next Actions

- ...
```

## Quality Rules

- Never invent post metrics, account attributes, or unsupported growth claims.
- Never mix private notes with public source evidence.
- Never present results as exhaustive.
- Always state the query, date range, and collection date.
- Keep Xquik optional. If access is unavailable, record the gap and continue with other approved sources.
- Keep final recommendations proportional to the evidence strength.
