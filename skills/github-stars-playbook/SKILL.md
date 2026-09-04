---
name: github-stars-playbook
description: Design and execute a 14-day GitHub repository growth sprint using README conversion, competitor-window research, Reddit, Hacker News, launch directories, community activation, and contributor loops. Use when launching an open-source repository, diagnosing weak star conversion, or building sustained GitHub discovery without buying stars.
---

# GitHub Stars — 14-Day Evidence-Driven Sprint

Use stars as a proxy for qualified developer interest, never as the final business outcome. Track installation, activation, repeat use and contribution beside stars.

## Intake gate

Collect before planning:

- repository URL, license and target developer;
- working quickstart verified on a clean machine;
- one reproducible demo and one differentiator;
- current views, unique cloners, stars, issues, contributors and activation event;
- three direct competitors and their latest launch/change dates;
- available founder, engineering and community capacity.

Do not launch if a new developer cannot understand the value and complete the quickstart in 10 minutes.

## Measurement contract

Create one row per channel:

```text
date | source | post URL | repo views | stars | clones | installs | activated | retained D7 | contributors
```

Report `view → star`, `star → install`, `install → activation`, and `activation → D7 retained`. Do not attribute organic GitHub traffic to a campaign without source evidence.

## Competitor-window scan

Before selecting the launch date:

1. Review the three competitors' release notes, X, Reddit, Hacker News, Product Hunt and GitHub activity from the last 30 days.
2. Record their positioning, strongest proof asset, community response and unresolved complaints.
3. Avoid launching into a dominant competitor announcement unless the product is a credible alternative to that exact news.
4. Use a quiet window or a category event where the repository adds a distinct point of view.

Historical Gingiris OSS launch evidence shows that timing against the competitor/news window materially changes distribution; it is not enough to post everywhere on a fixed calendar.

## README conversion surface

The first screen must contain:

- one-line outcome for a named developer;
- reproducible demo or result;
- three differentiators at most;
- quickstart that works when copied;
- trust signals: license, security/privacy posture, maintainers and community link.

Ask five unfamiliar developers to explain the product and run the quickstart. Fix repeated confusion before distribution.

## 14-day sprint

### Days 1–3 — proof and instrumentation

- Validate the quickstart on macOS/Linux and the supported runtime.
- Produce one 30–60 second demo, architecture diagram and comparison table.
- Add source-tagged links and establish the baseline dashboard.
- Prepare issue templates, contribution guide and response ownership.

### Days 4–6 — community fit

- Identify two relevant subreddits, one Hacker News angle and five specialist communities.
- Participate with useful answers before sharing the repository.
- Draft channel-native posts: problem/lesson for Reddit, technical novelty for Show HN, demo/proof for X.
- Ask existing users for honest feedback, never coordinated stars.

### Day 7 — release

- Publish the release, README and demo together.
- Submit one Show HN post only when there is genuine technical novelty and the maintainers can answer questions live.
- Publish to relevant Reddit communities only where rules permit; disclose affiliation.
- Respond to technical objections with evidence and open issues for valid gaps.

### Days 8–10 — second wave

- Turn repeated questions into documentation and comparison pages.
- Contact maintainers, newsletters and creators whose audience already uses the category.
- Translate the winning technical explanation for one relevant regional community.
- Publish a build log or benchmark with reproducible methodology.

### Days 11–14 — compounding loop

- Invite activated users—not all stargazers—to interviews.
- Convert recurring requests into `good first issue` tasks.
- Recognize contributors and document the next release milestone.
- Keep only channels that generated activated or retained users.

## Stop conditions and recovery

- Views rise but activation does not: stop distribution and fix quickstart/product.
- Stars rise but installs do not: rewrite positioning and demo.
- Reddit post is removed: do not repost around moderation; review rules and contribute normally.
- Show HN is flat after the initial window: do not manufacture engagement; reuse the technical asset elsewhere.
- Security or data-handling issue appears: pause promotion, publish the fix and incident scope.

## Compliance

Never buy stars, exchange stars, automate starring, conceal affiliation, use sockpuppets or ask communities to manipulate GitHub Trending. Do not publish unverifiable benchmarks.

## Required output

Return:

1. readiness verdict and blockers;
2. competitor-window table;
3. README change list;
4. 14-day channel calendar with owner and UTM/source;
5. measurement dashboard schema;
6. stop conditions and next experiment.

Related full playbook: `gingiris-opensource`.
