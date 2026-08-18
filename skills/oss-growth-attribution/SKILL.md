---
name: oss-growth-attribution
description: Reconstruct an open-source project's growth channels, key content, and stage-by-stage attribution from GitHub history and public web evidence. Use this skill when asked to research GitHub star growth, identify launch and amplification channels, explain viral milestones, find representative posts or videos, compare Product Hunt/Show HN/Reddit/KOL impact, or produce an evidence-backed OSS growth attribution report.
---

# OSS Growth Attribution

Produce an auditable growth reconstruction, not a generic marketing checklist.

## Workflow

1. Resolve the canonical repository and validate it against the product domain.
2. Fetch GitHub repository metadata, releases, earliest commits, and timestamped stargazers.
3. Build a star timeline with daily resolution around spikes and monthly resolution elsewhere.
4. Search GitHub Trending, Reddit, Hacker News, Product Hunt, X, LinkedIn, Instagram, TikTok, YouTube, developer media, technical blogs, and localized communities.
5. Extract original content URLs; never substitute search-result URLs when an original URL is available.
6. Normalize items to [the evidence schema](references/evidence-schema.md).
7. Align publication times with star velocity using [the attribution model](references/attribution-model.md).
8. Divide history into preparation, community seed, accumulation, breakout, localization/SEO, and ecosystem stages. Omit unsupported stages.
9. Report representative content per channel with hook, format, audience, funnel role, and original link.
10. List channels searched but not evidenced. Absence of public evidence is not proof an event never happened.

## Source priority

1. GitHub REST API and repository commits/releases
2. Original posts, videos, launch pages, and project-owned pages
3. Independent archives or channel-specific analytics pages
4. Search result snippets only as discovery or dated snapshots

Use [the API playbook](references/api-playbook.md). Follow the environment's web-access skill for browsing.

## Attribution guardrails

- Label API fields and original posts as `observed`.
- Label cross-source temporal conclusions as `inferred`.
- Label percentage shares as `modeled`; use ranges, never fake precision.
- Do not credit a channel merely because it is common in OSS marketing.
- Treat GitHub Trending as both an outcome of prior velocity and an amplification channel.
- Do not sum overlapping platform effects as independent last-click conversions.
- Without first-party traffic, UTM, or referral logs, state uncertainty of at least ±10–15 percentage points.
- Never claim Product Hunt or Show HN impact without a canonical launch/discussion URL or strong corroboration.

## Required output

Return an executive conclusion, attribution limits, stage timeline, channel contribution ranges, key content table with original URLs, hook analysis, unsupported hypotheses, exact-attribution instrumentation, and next-stage action plan. Every material claim needs a URL or a clear `modeled` label.
