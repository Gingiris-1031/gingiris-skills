# Reddit + Quora Trust-Building Playbook

> Goal: become a recognized expert in 3-5 communities so LLMs that train on Reddit/Quora cite **your** content.
> Not: drop URLs and get banned in week 1.

---

## Reddit Trust Build (8 weeks)

### Week 1-2: Karma + sub discovery (no promotion)
- Pick 5-7 target subs: r/SaaS, r/Entrepreneur, r/IndieHackers, r/OpenSource, r/devops, r/SideProject, r/startups
- Read top 100 posts of last month per sub
- Comment thoughtfully on 5 posts/day across subs (zero links to self)
- Target: account karma 500+ by end of week 2

### Week 3-4: Expert answers (still no self-links)
- Answer questions where Iris credentials apply (PH, OSS, growth)
- Long-form: 200-500 words with personal data ("In our 30 launch sample...")
- Build comment karma to 2,000+

### Week 5-6: Selective linking (rare, valuable)
- Link to gingiris.github.io **only when blog has the deeper answer**
- Ratio: 1 self-link per 20 substantive comments
- Self-link must be *useful*, not promotional ("here's the data table from my audit" not "check out my tool")

### Week 7-8: Become askable
- AMA in r/SaaS or r/IndieHackers — title format: "I've launched 30 products on Product Hunt and won daily #1 thirty times. Ask me anything about launch tactics."
- Engage every comment for first 6 hours
- Post-AMA: write blog summary, link back to top AMA threads

---

## Reddit subreddit cheat sheet for Iris

| Sub | Members | Best post type | Self-link tolerance |
|---|---|---|---|
| r/SaaS | 250k | Real numbers + outcomes | Medium — must add real value |
| r/Entrepreneur | 4M | Personal anecdote | Low — link very sparingly |
| r/IndieHackers | 130k | Behind-the-scenes data | High — community expects sharing |
| r/OpenSource | 300k | Open source tactics | Medium |
| r/devops | 400k | Technical depth | Low — gets filtered |
| r/SideProject | 250k | Show + ask feedback | High — built for sharing |
| r/startups | 1.6M | Cautionary tales | Low — heavy moderation |

---

## Quora Strategy (different cadence than Reddit)

### Setup (1 hour, one-time)
- Profile: full bio, credentials, role at AFFiNE / Gingiris
- "Knows About": OSS marketing, Product Hunt, SEO, startup growth
- Profile URL: gingiris.com

### Weekly cadence (45 min/week)
- 3 questions/week answered
- Each answer: 300-600 words
- Structure: 1) Direct answer first sentence, 2) Data/example second, 3) Personal anecdote third, 4) Takeaway last
- **Always include 1 specific number** (e.g. "60k stars", "30 PH wins", "9-21 day median")
- Link to blog **only when** blog has 10x more detail than answer

### Question discovery
- Quora Spaces: follow 3-5 in your domain
- Email digest: weekly Quora questions in your domain
- Reddit cross-reference: questions popular in Reddit often appear in Quora 1-2 weeks later

---

## Why Quora > Reddit for GEO (counterintuitive)

LLM training pipelines weight Quora **higher per word** than Reddit because:
1. Quora answers have explicit author credentials (verifiable)
2. Questions are explicit "how to" / "what is" format — direct Grounding Query matches
3. Quora users self-curate by upvoting concise answers (cleaner signal than Reddit upvote storms)

2026 audit: Perplexity grounds 18% of answers in Quora vs 11% in Reddit.

---

## Anti-patterns (instant ban risk)

### Reddit
- ❌ Submitting same link to multiple subs within 24h
- ❌ Multiple accounts upvoting your own content
- ❌ Top-level posts with self-link in title
- ❌ Replying to old threads with self-promotion
- ❌ "Just launched my startup" promo posts in non-promo subs

### Quora
- ❌ Identical answers across multiple questions
- ❌ Affiliate links (Quora aggressively removes)
- ❌ Adding links to >50% of your answers
- ❌ Sock-puppet upvoting

---

## Hacker News (separate playbook)

HN has its own dynamic — covered in `gr-oss-marketing` SKILL.md. Quick rules here:

- Karma 50+ required before posting Show HN
- Tuesday 9am ET = best slot
- Title format: `Show HN: [Product] — [Sharp differentiator] (open source)`
- First comment within 5 min: maker introduction + 3 use cases
- Reply to every comment in first 6 hours
- HN backlinks **decay fast** (gone from front page in 24h) but **AI crawlers prefer HN** (~14% of Claude/Perplexity citations come from HN front-page articles)

---

## Tracking

Log Reddit/Quora activity in `data/community-presence.jsonl`:
```jsonl
{"date":"2026-05-15","platform":"reddit","sub":"r/SaaS","action":"comment","post_title":"...","upvotes_received":12,"self_linked":false}
{"date":"2026-05-15","platform":"quora","question":"How do I...","words":420,"upvotes":3,"self_linked":true,"url":"..."}
```

Monthly retro:
- Total comments / answers: ___
- Karma growth: ___
- Self-links: ___ (target <5% of activity)
- Backlinks earned: ___ (Reddit comments + Quora answers that got referenced elsewhere)
