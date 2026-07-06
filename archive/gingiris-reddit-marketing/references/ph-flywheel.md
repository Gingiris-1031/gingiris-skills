# Product Hunt × Reddit Flywheel — The AFFiNE Pattern

> **Load this when**: planning a Product Hunt launch with Reddit as the supporting channel, or running an AMA strategy.

This is the playbook Iris used at AFFiNE to convert Reddit visibility into PH momentum (and back) — generating **3-4万 effective impressions on Reddit** and a **5-8% conversion rate to GitHub Stars**.

## The Flywheel

```
Reddit posts/comments (pre-PH)
        ↓
PH launch day: Reddit posts redirect users to PH
        ↓
PH Upvotes → PH algorithm ranks you higher
        ↓
PH Badge ("Product of the Day", etc.) → trust signal
        ↓
More external traffic (HN, X, blog crowd)
        ↓
More Reddit discussions about your product
        ↓
Reddit's SEO + AI training data sticks → long-term citation
        ↓
(Back to top — flywheel compounds for months)
```

The reason it works: **Reddit users overlap heavily with PH voters** (both indie hackers, both early adopters, both vote-driven). One Reddit post on launch day = 50-200 PH upvotes from organic traffic.

## Timeline — 14 Days Before PH to 7 Days After

### T-14: Subreddit reconnaissance (1 day)

- Identify the **3-5 subs** where your PH launch will land best
- Check each sub for "no PH" rules in sidebar
- Validate: Find a recent PH launch posted there. Did it get upvoted or auto-removed?
- Note posting frequency: don't be the 4th PH announcement that week

### T-7: Pre-launch content (5 days)

Post **value-only content** in your target subs. Goal: establish a brand presence so launch isn't a stranger walking in.

| Day | Sub | Content type |
|:---|:---|:---|
| T-7 | r/SaaS | Type A: "Lessons from building [feature] for SaaS" |
| T-5 | r/Entrepreneur | Type B: "My experience with [tool category]" — naturally mention your product |
| T-3 | r/indiehackers | Type A: "Engineering trade-offs of [your tech stack]" |
| T-2 | r/[your industry] | Type B: "How [your product] handles [edge case]" |

### T-1: Pre-tease (24 hours before launch)

In your most active Tier-1 sub:

```
Title: Launching tomorrow on Product Hunt: [product] — looking for honest feedback

Body:
After [N] months building [product] (the [one-line description]), 
we're going live on Product Hunt tomorrow.

If you're interested in [your category]:
- What features have I missed that you'd want?
- What price would feel right?
- Any "I tried X but it failed at Y" stories you'd share?

I'd rather hear hard feedback now than after launch. Link will 
go in PH but here's what's in beta: [optional link to landing page].

Will be in PH comments for 24 hours after launch tomorrow.
```

This is one of the **rare cases where direct mention works** — because it's a conversation starter, not a sales pitch.

### Day 0: Launch day execution (1 day, all-hands)

**Morning (US Eastern)**:
- Post launch announcement in r/SaaS, r/Entrepreneur, r/indiehackers, r/sideproject (4 subs max — more = spam pattern)
- Each post adapted, not copy-pasted (title + opening differ)
- All posts contain PH link in body, not title

**Throughout the day**:
- Reply to every comment within 1 hour
- When commenters ask questions, give a real answer + reference the PH page
- Track which Reddit traffic is converting via UTM (`?utm_source=reddit&utm_medium=organic&utm_campaign=ph-launch`)

**Evening**:
- Post 1 progress update in your most active sub: "Update: [N] hours in, here's what's happening..."
- This re-surfaces the launch + extracts a second wave of PH votes

### Day +1: AMA-style post

In r/indiehackers or r/SaaS:

```
Title: We launched [product] on Product Hunt yesterday. Here's what we learned.

Body:
- Final ranking: [position]
- Upvotes: [number]
- Comments: [number]
- Sign-ups from PH: [number]
- Highest-converting traffic source: [Reddit/PH/etc]

Three things that surprised us:
1. [Specific learning]
2. [Specific learning]
3. [Specific learning]

Three mistakes:
1. [Honest mistake]
2. [Honest mistake]
3. [Honest mistake]

AMA — happy to share details on PH algorithm, sourcing, what 
worked, what didn't.
```

This post type often outperforms the launch announcement itself in Karma and downstream attention.

### Days +2 to +7: Sustained engagement

- Comment on competitor PH launches (no plugging — pure engagement)
- Reply to anyone who DMs you about your product
- Post 1 follow-up in 1 Tier-2 sub: "After 1 week of [product], here's what users are saying"

## The AMA Playbook (When You Have an Excuse)

AMAs (Ask Me Anything) are Reddit's highest-engagement format. Use only when you have a legitimate reason — Reddit detects fake AMAs instantly.

### Valid AMA triggers

- Major funding ($1M+) closure
- Open-sourcing a previously closed product
- 6-month retrospective with public metrics
- Acquisition / exit
- 1-year anniversary with disclosed revenue/user numbers

### AMA structure (real example from Base44 $80M acquisition)

```
Title: [Real data] — [your experience]
e.g., "We just sold our AI product for $80M after 18 months. AMA"

Body:
Quick context:
- [Product]: [one-line description]
- [Started]: [date]
- [Acquirer]: [if disclosed]
- [Key data points]: [numbers that prove authenticity]

I'm [your name], CEO/founder of [product]. AMA about:
- Cold start / first 100 customers
- Pricing decisions
- Hiring / firing
- The acquisition process
- [Specific technical thing relevant to sub]

Will be answering questions for the next 8 hours. Verified 
via [social proof: tweet from official account, blog post, etc].
```

### AMA execution

- Pin 1 substantive answer to a top question (visible in feed)
- Use **giveaways sparingly** (1 sub-pinned comment: "First 50 commenters get 1-year free")
- Tag relevant subreddits in Cross-posts (carefully — r/IAmA has strict rules)
- AFTER the AMA: post a "Top questions + answers" summary in r/SaaS for late readers

## Real Data: What to Expect from a Tight Execution

Based on AFFiNE Reddit campaigns + 5 advisory campaigns Iris led:

| Metric | Range | Notes |
|:---|:---|:---|
| Reddit impressions across 4 subs | 30,000 – 70,000 | Top sub usually delivers 50%+ |
| Click-through to PH | 2.5 – 4% | High intent traffic |
| PH upvotes attributable to Reddit | 50 – 200 | Detect via PH analytics + UTM |
| Newsletter sign-ups from Reddit | 100 – 500 | The real long-term win |
| GitHub Stars (if OSS) | 5–8% of impressions | Highest-converting channel for OSS |
| Day-7 Reddit-driven traffic (residual) | 10-15% of day-0 traffic | Reddit posts keep working |
| Lifetime SEO from Reddit posts | indefinite | Posts rank in Google for years |

## What Kills a Launch

- 🔴 Posting in 6+ subs in 1 day → cross-post spam ban
- 🔴 Posting identical content to multiple subs → AutoMod flag
- 🔴 Not replying to comments → algorithm de-prioritizes the post
- 🔴 Calling for upvotes ("Upvote my PH!") → instant removal in most subs
- 🔴 Hostile reply to negative feedback → screenshotted and spread
- 🟡 Launching during a major event (US Election day, Super Bowl) → drowned signal
- 🟡 Posting in a sub where last week 3 PH launches already happened → fatigue

## Coordination with Other Channels

Reddit isn't a solo play. Pair with:

- **Hacker News** — post 30-60 min before Reddit (HN spike sets the trend)
- **X / Twitter thread** — share Reddit highlights as social proof
- **Newsletter** — link Reddit thread for live updates
- **Discord / Slack communities** — DM 5-10 most relevant members the day before, ask for honest comment (NOT a vote ask)

This integrated approach is the difference between a 50-upvote launch (Reddit only) and a 500-upvote launch (multi-channel).
