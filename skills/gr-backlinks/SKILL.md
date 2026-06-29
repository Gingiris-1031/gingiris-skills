---
name: gr-backlinks
description: >
  Systematic backlink building for indie founders. Covers 5 channel types ranked by GEO + SEO ROI:
  Wikipedia (entities), authoritative media (PR), industry reviews (G2/Capterra/Product Hunt),
  Reddit/Quora discussions, and HARO/Featured.com expert quotes. Designed for 0→1 sites where
  domain authority is the bottleneck. Aligns with 2026 Google/Bing GEO guidance: backlinks are
  the strongest brand-authority signal AI search engines use to decide citations.
  Defaults to dev/B2B link sources; for 2C products (education, consumer apps) authority links differ — see gingiris-seo-geo/references/2c-adaptation.md.
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  phase: Phase 2 main line 4 (added 2026-05-07)
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-backlinks
tags:
  - backlinks
  - link-building
  - seo
  - off-page-seo
  - domain-authority
  - featured-com
  - haro-alternative
  - digital-pr
  - content-marketing
  - saas-seo
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

## ⚠️ 2C 产品的外链调整

本 skill 的 5 类渠道（Wikipedia / 媒体 PR / G2 评测 / Reddit-Quora / HARO）偏 dev/B2B。**2C 消费品 / 教育** 的权威链接来源不同：

- **教育**：学校 / 留学机构 / 考试论坛 / 教育媒体 > 普通付费外链。
- **通用 2C**：行业垂直媒体、地区 KOL、社区高赞帖。
- **G2 / Capterra**（B2B 软件评测站）对 2C 基本无效 → 换 App Store 评分 + 垂类榜单 + 应用媒体测评。
- **YMYL 品类**：权威机构背书的链接权重远高于数量；切勿买链/造评（Google 数天内识别）。

完整 2C 渠道数据库 + 公开来源见 → `gingiris-seo-geo/references/2c-adaptation.md`

---

# gr-backlinks — Systematic Backlink Building

## Why this skill exists

**Phase 2 missing piece**: We do title/content/schema/cluster optimization but have **zero systematic backlink work**. Article research (2026-05): backlinks are the #1 GEO signal — LLMs decide citations partly by brand authority, which is downstream of backlink graph.

For Iris's site (gingiris.github.io, subpath under GitHub Pages), the domain authority ceiling is **fundamentally capped without external backlinks**. No on-page work can beat Wikipedia / Hootsuite / Wired for head terms — only backlink quality + count can.

---

## The 5-Channel Priority Matrix

Adopted from 2026-05 WeChat article + JeffLi1993 / AgriciDaniel / zubair-trabzada skills audit:

| Channel | SEO Value | GEO Value | Priority | Effort/week |
|---|---|---|---|---|
| **Wikipedia dedicated entry** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **MAX** | 3-6h (one-time setup, ongoing edits) |
| **Authoritative media (PR)** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | **MAX** | 2h (HARO + outreach) |
| **Industry reviews (G2/Capterra/PH)** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | HIGH | 1h (one-time submission) |
| **Reddit/Quora discussions** | ⭐⭐ | ⭐⭐⭐⭐ | HIGH | 2h (sustained presence) |
| **Generic backlinks (directories/blogs)** | ⭐⭐⭐ | ⭐⭐ | MED | skip until top 3 done |

**Rule**: Start from highest GEO value. SEO-only signals (DA passing) are less leveraged than 2-3 years ago.

---

## When to use this skill

- "I want to build backlinks for my site"
- "How do I get into Wikipedia?"
- "How do I do HARO / Featured.com?"
- "What's a Reddit / Quora strategy that doesn't get me banned?"
- "How do I get into G2 / Capterra?"
- Phase 2 monthly checkpoint shows domain authority capping ranking

---

## Channel 1: Wikipedia (highest GEO leverage)

### Reality check before you start
- Wikipedia is **notability-gated**, not effort-gated
- Threshold: **5+ independent reliable-source articles** discussing your subject substantively (not in passing)
- Listicle mentions, PR releases, sponsored content do **NOT** count
- Paid Wikipedia services (Fiverr / WikiExperts / Wiki Mavericks): 80% of articles deleted within 6 months — they fail notability not because of editor skill

### Correct sequence

1. **Build the case file first** (4-12 weeks)
   - Earn 5+ independent press articles via Channels 2 + 3 below
   - Document them in a `data/wikipedia-prep/` folder
   - Format: `{publication, date, url, key_quote, indepth_or_passing}`

2. **Wikidata first, Wikipedia second**
   - Create a Wikidata entity (much lower notability bar) → builds a structured record AI crawlers find
   - LLMs heavily weight Wikidata for entity recognition

3. **Use Articles for Creation (AfC)**
   - Submit at https://en.wikipedia.org/wiki/Wikipedia:Articles_for_creation
   - Free, peer-reviewed, 2-8 week wait
   - Pass rate: ~40% if notability is clearly demonstrated

4. **Hire a real editor (optional)**
   - Search Upwork for "Wikipedia editor 1000+ edits 5+ years"
   - Rate: $80-200/hr
   - **Must disclose payment** per WP:PAID — non-negotiable
   - Avoid agencies charging fixed $2k+ for "guaranteed" articles (banned by 2026 standards)

### Checklist before submission
- [ ] Subject has 5+ deep independent sources (not press releases)
- [ ] Each notability claim has a citation
- [ ] Neutral point of view (no marketing language)
- [ ] Wikidata entity exists
- [ ] All paid contributors disclosed
- [ ] Article has 600-1,500 words (too short = "stub" rejection)

---

## Channel 2: PR / Authoritative Media

### Two paths to backlinks

#### Path A: Inbound — HARO / Featured.com / Qwoted
Journalists request expert quotes daily. Reply with concise, citable answers → published article with backlink.

- **HARO**: helpareporter.com — free, 3 emails/day, US-heavy
- **Featured.com**: featured.com — pay-to-submit answers, US + global, higher conversion
- **Qwoted**: qwoted.com — newer, more international

**Reply template** (works ~15-25% of the time):
```
Hi [Journalist],

I'm Iris Wei, ex-COO of AFFiNE (60k+ GitHub stars). For your question
about [topic], here's a 3-sentence answer with concrete data:

[ANSWER: lead with a number, give the mechanism, end with a takeaway.
50-100 words. Cite a specific personal experience, not generic advice.]

If you need a longer quote or follow-up, happy to share more.

— Iris
Site: https://gingiris.com
Twitter: @WeiYipei

[Disclosure: I run gingiris.com — no expectation of a link, just a useful quote.]
```

**Pace**: 3-5 responses/week. Time/response: 8-12 min. Expected: 1-2 links/month.

#### Path B: Outbound — Targeted journalist outreach
For deep-dive features, not 1-line quotes.

1. Identify 10 journalists who cover your niche (use Twitter / Muck Rack)
2. Build 3-week warm-up (read + comment on their posts, no DM yet)
3. Pitch a specific story angle (not "want to feature my product")
4. Offer exclusive data, customer interview, or unique angle

**Best pitch types for Iris**:
- "I led AFFiNE from 0 → 60k GitHub stars. Here's the playbook." (TechCrunch / The Information)
- "Why most OSS marketing playbooks are wrong" (Wired / The Verge)
- "Real data: 30 Product Hunt #1 launches in 4 years" (Fast Company / Forbes)

---

## Channel 3: Industry Reviews (G2 / Capterra / Product Hunt / SourceForge)

### One-time submissions (high ROI for any SaaS / open source)

| Platform | URL | What to submit | Backlink type |
|---|---|---|---|
| G2 | g2.com/products/new | Product + features | Profile + reviews |
| Capterra | capterra.com/vendors/sign-up | Product + pricing | Profile + reviews |
| Product Hunt | producthunt.com/posts/new | Each major version | Listing |
| SourceForge | sourceforge.net/projects/add | Open source only | Project page |
| AlternativeTo | alternativeto.net | Free | Profile + alt-listing |
| StackShare | stackshare.io | Tech stack | Profile |

**Once submitted, ask early users for genuine reviews** (5-10 reviews unlocks featured placement on most platforms).

---

## Channel 4: Reddit / Quora / Hacker News

### Anti-pattern (gets you banned)
- Drop your URL in a top-level post
- Generic "check out my tool" comments
- Multiple accounts (sockpuppeting)

### What actually works (builds trust + backlinks naturally)

**Reddit**:
1. Build account karma to 500+ over 4-8 weeks (comment in non-promotional subs first)
2. Find 5-7 subreddits where your audience hangs out
3. **Answer questions deeply** with real experience — link to your blog **only if it directly answers** (1 in 10 responses)
4. Once respected: AMA in r/SaaS, r/Entrepreneur, r/IndieHackers, r/OpenSource

**Quora**:
1. Pick 3 topics where you can speak with authority
2. Answer **specific questions**, not topic-wide overviews
3. Each answer: 200-500 words + 1 personal anecdote
4. Link to blog only when blog has the deeper version of your answer

**Hacker News**:
1. Build karma to 50+ before posting
2. Show HN: best slot Tuesday 9am ET (see existing `/gr-oss-marketing` for details)
3. Engage with every comment in first 6 hours

### Why this matters for GEO
LLMs heavily weight Reddit / Quora content during training:
- ChatGPT cites Reddit ~12% of its responses (2026 Q1 audit)
- Perplexity grounds 18% of answers in Reddit/Quora
- Claude weights Quora answers for "how to" queries

---

## Channel 5: Generic Backlinks (skip until Channels 1-4 maxed)

Directories, guest posts on low-DA sites, blogger network exchanges. **Low GEO value** in 2026.

Don't waste time here until Channels 1-4 are mature.

---

## Workflow: First 30 days for Iris

### Week 1
- [ ] Sign up: HARO, Featured.com, Qwoted (Channel 2A)
- [ ] Create 1 Featured.com answer per day = 7 responses
- [ ] Submit AFFiNE + Gingiris to G2, Capterra, AlternativeTo, StackShare (Channel 3)

### Week 2
- [ ] HARO/Featured: 5 responses
- [ ] Identify 10 journalists covering OSS / SaaS growth (Channel 2B prep)
- [ ] Start Reddit karma build in r/SaaS, r/Entrepreneur (Channel 4)

### Week 3
- [ ] HARO/Featured: 5 responses
- [ ] Pitch 3 journalists with specific story angle (Channel 2B)
- [ ] Quora: answer 3 questions in your domain

### Week 4 + Monthly retro
- [ ] HARO/Featured: 5 responses
- [ ] Count backlinks earned (use `scripts/backlinks-audit.py` — Tier 0 free)
- [ ] Update Wikipedia case file (Channel 1 prep)

### Months 2-3
- [ ] First Wikidata entity submission
- [ ] First AfC Wikipedia submission (if 5+ independent sources accumulated)
- [ ] Reddit AMA in 1 high-fit sub

---

## Scripts

### `scripts/backlinks-audit.py` (Tier 0 — free, no API)
Uses Common Crawl + verification crawler to get baseline:
- Inbound link count from common crawl
- Verify each known link (HTTP 200 + still links to us)
- Domain-level metrics: in-degree, PageRank approximation, harmonic centrality

Run monthly to track growth.

### `scripts/haro-helper.py` (planned)
- Parse incoming HARO emails
- Auto-suggest which to respond to (based on Iris credentials)
- Draft 3-sentence answer skeletons

---

## Tracking

Maintain `data/backlinks.jsonl` (one line per backlink):
```jsonl
{"date":"2026-05-15","from":"techcrunch.com","to":"gingiris.github.io","anchor":"AFFiNE","channel":"PR","tier":1,"context":"60k stars article"}
```

Use this for:
- Monthly retro (Channel mix vs target)
- Phase 2 checkpoint (correlate backlink growth with SERP rank changes)
- Wikipedia case file building

---

## Anti-patterns (avoid)

- ❌ **Paid agency Wikipedia services** — sockpuppet farms, articles deleted
- ❌ **Reddit coordinated fake accounts** — gets you banned permanently
- ❌ **Generic HARO replies** — quote rate <2% without specific credentials
- ❌ **Buying links** — Google's algorithm now flags within days
- ❌ **Asking friends to write inauthentic reviews on G2** — flagged + removed
- ❌ **Guest posting on link farms** — negative SEO

---

## Cascade recommendations

- Channel 2 PR success → `gr-blog-post` reference that media article in our content (build social proof)
- Channel 4 Reddit AMA → schedule via `gr-oss-marketing`
- Wikipedia entity created → update `gr-geo-cite` to track Wikipedia citations in AI responses (highest-priority test)
- Backlinks accumulated → re-run `gr-seo-patrol` to measure rank impact

---

## API dependencies

| Service | Env var | Tier | Cost |
|---|---|---|---|
| Common Crawl (CDX index) | none | 0 (always) | Free |
| Moz API | `MOZ_TOKEN` | 1 (optional) | $99/mo |
| Bing Webmaster API | OAuth | 2 (optional) | Free with verified site |
| DataForSEO Backlinks | `DATAFORSEO_B64` (existing) | 3 (you have) | Pay per query |

Start at Tier 0 + Tier 3 (DataForSEO already configured for `gr-seo-patrol`).
