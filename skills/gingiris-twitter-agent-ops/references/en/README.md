> 🌍 **Language**: [中文](../../SKILL.md) | [English](../en/README.md) | [日本語](../ja/README.md) | [한국어](../ko/README.md)

# Twitter/X Agent Operations — The Complete SOP for AI-Automated Account Management

> **Battle-tested**: An AI agent grew @WeiYipei from 1,150 → 1,837 followers (+60%) in 45 days, posting 1 tweet per day, fully automated.
>
> This skill works with any AI agent that supports a system prompt (Claude Code, Cursor, Trae, GPT).

---

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│              Twitter Agent Operations                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [1] Persona ──→ [2] Source Library ──→ [3] Scheduling  │
│       │                  │                    │         │
│       ▼                  ▼                    ▼         │
│  [4] Hard Rules   [5] Pre-publish QC   [6] Tracking     │
│                                                         │
│  ───────────── Weekly Loop ─────────────                │
│  Weekly report → Review → Adjust weights → Next week    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Six core modules**:
1. **Persona calibration system** — make the agent write content that "sounds like this person"
2. **Source library** — a fact-source database, zero fabrication
3. **Scheduling system** — weekly content calendar, 1 tweet/day cadence
4. **Hard rules** — non-negotiable safety lines
5. **Pre-publish checks** — triple-translation + 5-point QC
6. **Data tracking** — tweet-log + weekly reports + follower tracking

---

## 2. Persona Calibration System (Voice Guide)

### Why You Need It

The biggest problem with AI agents isn't that they "can't write" — it's that what they write "doesn't sound like this person." Persona calibration solves the **soul problem**, not the **formatting problem**.

### Calibration Steps

#### Step 1: Collect Raw Voice Samples

Gather authentic expression samples from the account owner (at least 3 levels of "concentration"):

| Concentration | Source | What it gives you |
|------|------|------|
| Strong | Blog posts / long-form articles | Narrative structure, value expression |
| Medium | Original social media posts | Conversational tone, fragmented expression |
| Light | Podcasts / interviews / conversations | The most authentic voice, verbal tics |

#### Step 2: Extract Iron Rules

Distill 3-5 non-negotiable expression rules from the samples. For example:

```
Rule A: Openers must start with "I" + a specific experience/number/moment
Rule B: No three-part essay structure (claim → evidence → call to action)
Rule C: Not every tweet needs a "takeaway"
Rule D: Bold = expressing conviction, not highlighting key points
```

#### Step 3: Build a Dead-Opener Blacklist

Mine historical data for "opener patterns with the lowest impressions" and explicitly ban them:

```
❌ Opening with someone else's quote
❌ Grand-thesis openers ("A counterintuitive thing about the AI era")
❌ Subject-less buzzword openers
❌ Opening directly with a philosophical one-liner
```

#### Step 4: Define Content-Type Weights

Allocate type ratios based on data performance:

| Type | Recommended share | Why |
|------|---------|------|
| Long-form (personal experience + data + insight) | 70% | Where the viral hits cluster |
| Tool / resource posts | 20% | Highest bookmark counts |
| Life fragments / rants | 10% | Keeps the account human |

**Field data**: After dropping the "short aphorism" type, weekly average impressions rose 266%.

---

## 3. Source Library (SOURCE-INDEX)

### Core Principle

**Never fabricate data. Every specific number in a tweet must have a real, traceable source.**

### Build Steps

#### Step 1: Collect First-Hand Material

Convert all of the account owner's first-hand content into searchable text:

- Podcasts / interviews → full transcripts (whisper / manual)
- Articles / documents → archived in markdown
- Talks / presentations → key-point extraction

#### Step 2: Build the SOURCE-INDEX

Annotate every key fact point:

```markdown
| Fact point | Source | Original location | Usable |
|--------|------|----------|---------|
| 6,000 stars in the first week of open-sourcing | ep01, line 77 | "we hit 6,000 stars in the very first week" | ✅ |
| 643 investors | ep06, line 32 | "we must have added 643 of them, if I remember correctly" | ✅ |
```

#### Step 3: Verify Regularly

Every week, check that the data points cited in the schedule still match the originals. **Numbers stated in different podcasts/settings may differ — pick the most reliable version and annotate it.**

**Lesson from the field**: A user once flagged a mix-up between "6,000 stars in three days" and "6,000 stars in one week." After verification, all original sources consistently said "the first week."

---

## 4. Scheduling System

### Cadence

- **1 tweet per day** (hard rule, never exceed)
- Publish time: a fixed window (recommended 14:00-15:00 Beijing time, or whenever your target audience is most active)

### Schedule Template

Generate next week's schedule every Sunday:

```markdown
## Monday ｜ [Type] ｜ [Topic]
**Source**: [specific entry in SOURCE-INDEX]
**5-point self-check**: ✅/❌
**Triple-translation self-check**: ✅/❌
**CTA (in replies)**: [link]
```

### Dedup Mechanism

Before scheduling each tweet, check the tweet-log:
- Has the same core argument been posted in the past 30 days?
- Has the same data point been used in the past 14 days?
- If duplicated → change the angle or change the topic

### Time-Window Reference (based on 3,861-tweet dataset analysis)

| Window | Best-suited content |
|------|----------|
| 10:00-13:00 | Tools, tutorials, resource entry points |
| 17:00-23:00 | Flagship content, opinions, case breakdowns |
| 00:00-01:00 | High-bookmark content, developer tools |

Best monthly ranking: 17:00 > 23:00 > 13:00 > 11:00 > 20:00

---

## 5. Hard Rules

### Absolutely Non-Negotiable:

| # | Rule | Explanation |
|---|------|------|
| 1 | Never fabricate data | Every number must have a real source; if there's no source, don't write it |
| 2 | 1 tweet/day | No overposting. The agent must not adjust the frequency on its own |
| 3 | No CTA in the tweet body | External links go in the 1st reply (the X algorithm penalizes in-body links by 30-90%) |
| 4 | Data alignment | Dynamic numbers must be fetched fresh before publishing |
| 5 | Triple translation | Every tweet must pass the triple-translation check (see below) |
| 6 | 5-point check | Every tweet must pass the 5-point check (at least 4/5) |

---

## 6. Pre-Publish Checks

### Check A: Triple Translation (from internal language to external language)

Read each tweet through once and confirm there is no "announcement-speak":

| # | Translation | Before | After |
|---|------|--------|-------|
| 1 | Launch → Help | "We shipped a new feature" | "This feature turns your 80-page report into a 3-page distillation" |
| 2 | Capability → Scenario | "Supports long context" | "Reads an entire industry report in one pass and spots competitor changes" |
| 3 | Conclusion → Evidence | "It works great" | Show real screenshots, inputs/outputs, steps, comparisons |

**If any sentence in the tweet reads like "We launched X / We upgraded Y" → it must be rewritten.**

### Check B: The 5-Point Check (one strong tweet = one mini information product)

| # | Check item | The reader question it answers |
|---|--------|------------------|
| 1 | A value promise that's clear at first glance | "What does this have to do with me?" |
| 2 | One concrete usage scenario | "When would I actually use this?" |
| 3 | A barrier-lowering step or entry point | "Can I start right now?" |
| 4 | Screenshots, numbers, cases = evidence | "Why should I believe you?" |
| 5 | One reason worth bookmarking or sharing | "Why would I keep this around?" |

**Fewer than 4/5 = don't post. Go back and revise.**

---

## 7. Data Tracking

### Tweet Log (record every single tweet)

```markdown
| Date | Time | Tweet ID | Type + summary | Impressions | Engagement | Notes |
```

### Weekly Report Template

Generate weekly:
- Follower change (start/end + daily gain)
- Analysis of the Top 3 posts by impressions
- Content-type performance comparison
- Strategy adjustment suggestions for next week

### Key Metrics

| Metric | Meaning | Optimization direction |
|------|------|---------|
| Bookmarks | More important than likes (a trust signal) | Tool/resource posts are naturally bookmark-heavy |
| Impressions | Algorithm distribution effectiveness | The opener decides 80% |
| Engagement rate | Content resonance | Comments > likes > retweets |
| Daily follower gain | Growth health | Steady > volatile |

---

## 8. Content Methodology Reference

### Four Content Archetypes (based on 3,861 tweets)

| Type | Probability of reaching top 10% | Characteristics |
|------|-------------|------|
| Resource gateway | ~51% | Finds the entry point for readers (saves searching) |
| Tool tutorial | ~39% | Explains complex things for readers (saves understanding) |
| AI-tool discovery | ~24% | Shows a new tool + a concrete task (saves trial-and-error) |
| Plain opinion | ~9% | Pure opinion with no action (avoid) |

### The Four-Savings Model

The value of content isn't how much information you say — it's how many steps you save the reader:

1. **Save searching** — readers don't have to hunt for the entry point in an ocean of information
2. **Save understanding** — readers don't have to puzzle out complex concepts themselves
3. **Save trial-and-error** — readers don't have to step on every landmine themselves
4. **Save expression** — readers can forward your tweet to someone else as-is

### Three Visibility Principles

Readers are more willing to trust content that is visible, clickable, and quantifiable:

| Principle | Examples | Probability of reaching top 10% |
|------|------|-------------|
| Visible | Screenshots, screen recordings, comparison charts | — |
| Clickable | Links, tool names, search paths | ~40% (with "link in replies") |
| Countable | Numbers, time, cost, steps | ~35% (with resource keywords) |

### Golden Length

| Characters per post | Probability of reaching top 10% |
|---------|-------------|
| ≤40 chars | ~7% |
| 41-100 chars | ~15% |
| **120-220 chars** | **~26-28% (golden zone)** |

**Template**: First sentence states the value → sentences two and three describe the scenario → then give evidence or steps → end with an entry point or a reason to bookmark.

---

## 9. Case Study: @WeiYipei Operation Data

### Growth Curve

```
Week 1 (4/24-4/28): 1,150 → 1,155 (+5)    ← Cold start, exploration phase
Week 2 (4/28-5/05): 1,155 → 1,180 (+25)   ← Started daily long-form posting
Week 3 (5/05-5/12): 1,180 → 1,250 (+70)   ← First viral hit appeared
Week 4 (5/12-5/18): 1,250 → 1,380 (+130)  ← Threads + engagement strategy
Week 5 (5/18-6/01): 1,380 → 1,540 (+160)  ← Steady long-form output
Week 6 (6/01-6/08): 1,540 → 1,837 (+297)  ← 40-Playbook panorama breakout
```

**Total: 1,150 → 1,837 = +687 followers (+60%) in 45 days**

### Key Turning Points

| Event | Impact |
|------|------|
| Dropped the "short aphorism" type | Weekly impressions +266% |
| Fixed 8 AM publishing | Viral hit rate from 5% → 15% |
| Openers must be "I" + specific experience | All 6 viral hits were first-person |
| Thread (7-8 posts) power move | A single Thread gained 50-100 followers |
| 40-Playbook panorama | +297 followers in one week |

### What Works vs. What Doesn't

| ✅ Works | ❌ Doesn't |
|--------|--------|
| Long-form + real experience + data | Philosophical one-liners / quoting others |
| Tool posts + weekend 8 AM | Posting in the dead of night (impressions <200) |
| CTA in the replies | CTA in the body (cut by 30-90%) |
| First-person openers | Grand-thesis / preachy openers |
| Steady 1/day cadence | 3 tweets in one day or 3-day gaps |

---

## 10. Quick-Start Guide

### If You Want to Use This SOP Right Now:

**Day 0 (Preparation, 2-3 hours)**:
1. Collect 10 representative pieces from the account owner
2. Extract 3-5 persona iron rules
3. Build the dead-opener blacklist
4. Set content-type weights

**Day 1 (Source library, 2-4 hours)**:
1. Convert all first-hand content into text
2. Build the SOURCE-INDEX (key data points + provenance)
3. Mark which points are usable and which need verification

**Day 2 (Scheduling + rules, 1 hour)**:
1. Write the first week's schedule (7 tweets)
2. Confirm the hard rules
3. Set the publishing time

**Day 3 onward (Execution)**:
1. Draft according to the schedule every day
2. Run triple-translation + 5-point checks before publishing
3. Record the tweet-log after publishing
4. Produce a weekly report + adjustments every week

---

## 11. Common Mistakes

| Mistake | Consequence | Fix |
|------|------|------|
| Agent fabricates data | Trust collapses once users/the owner finds out | Hard rule 1 + mandatory SOURCE-INDEX |
| Overposting (multiple per day) | Algorithm downranking + content dilution | Hard rule 2, hard limit |
| Every tweet reads like an announcement | Impressions <300 | Triple-translation check |
| Aphorisms / preachy tone | Impressions 100-250 | Dead-opener blacklist |
| No data tracking | Impossible to optimize | Weekly report mechanism |
| Voice drift | Followers feel "this doesn't sound like them anymore" | Re-calibrate against the voice samples monthly |

---

## Install

```
# ClawHub
clawhub install gingiris-twitter-agent-ops

# skills.sh
npx -y skills add Gingiris-1031/gingiris-twitter-agent-ops

# Or just copy this file into your AI agent project
```

**Related links**:
- HuggingFace: https://huggingface.co/datasets/Gingiris/gingiris-twitter-agent-ops
- GitHub: https://github.com/Gingiris-1031/gingiris-twitter-agent-ops
- More playbooks: https://gingiris.tools

---

## Credits

- Methodology foundation: Xiangyang Qiaomu, "X Growth Experience: From 100 to 110K Followers" (analysis of 3,861 tweets)
- Content diagnosis framework: dontbesilent/dbskill "Content Creation Diagnosis"
- Field validation: the @WeiYipei account (operated by a Cola AI agent, April-June 2026)
- Author: Iris Wei (生姜iris) | Twitter @WeiYipei | https://gingiris.tools

---

*License: MIT*
