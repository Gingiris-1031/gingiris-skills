# GEO Optimization Guide

> Generative Engine Optimization — Get your content cited by AI search engines

---

## What is GEO

GEO (Generative Engine Optimization) is an optimization strategy for AI search engines (ChatGPT, Perplexity, Claude, Google AI Overview).

When a user asks AI "recommend a video generation tool," the AI's answer is based on the content it has crawled and understood. GEO's goal: **make your product appear in AI answers.**

### Relationship with SEO

```
SEO  → User searches Google → Sees your link → Clicks through
GEO  → User asks ChatGPT  → AI cites your content → User trusts and visits

Shared foundation: Structured content + quality information + technical accessibility
```

---

## GEO Core Three

### 1. IndexNow Real-Time Push

**What is IndexNow:** A protocol that lets you proactively tell search engines "I have new content" instead of waiting for crawlers. Supported by Bing, Yandex, Naver, with data shared to partner AI search engines.

**Setup:**

```bash
# 1. Get API Key from https://www.bing.com/indexnow

# 2. Place verification file at site root: /{your-key}.txt

# 3. Push URLs
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "your-domain.com",
    "key": "your-api-key",
    "urlList": [
      "https://your-domain.com/pricing",
      "https://your-domain.com/blog/new-article",
      "https://your-domain.com/compare/competitor"
    ]
  }'
```

**Push Strategy:**

| Priority | Page Type | When to Push |
|----------|----------|-------------|
| P0 | Pricing page | Every price change |
| P0 | New blog/article | Day of publishing |
| P1 | Feature pages | New feature launch |
| P1 | Comparison pages | When competitor updates |
| P2 | Case studies | On publish |

### 2. robots.txt — Allow AI Crawlers

```
User-agent: *
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: *
Disallow: /admin/
Disallow: /api/

Sitemap: https://your-domain.com/sitemap.xml
```

### 3. AI-Friendly Content Formatting

**Direct answers (most important):**

Open every page with a one-line answer to the core question:

```markdown
## What is [Product]?

[Product] is a [category] platform that helps [target users] [core value]. 
It's used by [user count] to [primary use case].
```

**Structured comparison tables:**

AI models prefer tabular comparisons:

```markdown
| Feature | [Product] | [Competitor A] | [Competitor B] |
|---------|----------|---------------|---------------|
| AI Avatars | Yes | Yes | No |
| API Access | Yes | No | Yes |
| Free Tier | Yes | Limited | No |
| Starting Price | $30/mo | $50/mo | $25/mo |
```

**FAQ format covering high-frequency questions:**

```markdown
### How much does [product] cost?
[Product] offers a free tier. Paid plans start at $X/month...

### What's the difference between [product] and [competitor]?
[Product] focuses on [differentiator], while [competitor] is better for [use case]...
```

---

## GEO Content Optimization Checklist

### Page-Level

- [ ] Page opens with one-line direct answer to "what is this"
- [ ] Contains at least one structured comparison table
- [ ] FAQ Section covering 5+ common questions
- [ ] FAQPage Schema markup
- [ ] Data uses precise numbers, not vague language
- [ ] Includes "Last updated" date (AI prefers fresh content)

### Site-Level

- [ ] robots.txt allows major AI crawlers
- [ ] IndexNow configured and pushing on updates
- [ ] sitemap.xml includes all core pages
- [ ] Clear internal linking between pages
- [ ] About page establishes E-E-A-T (team, funding, customers)

### Content Strategy

- [ ] Each competitor has a dedicated comparison page
- [ ] Pricing page has comprehensive FAQ
- [ ] Blog articles open with Key Stats table
- [ ] Case studies include specific numbers and outcomes
- [ ] Glossary pages cover key industry concepts

---

## AI Citation Monitoring

### Manual Checking

Periodically test your brand and category keywords on AI platforms:

```
Test queries:
- "recommend a [category] tool"
- "best [category] software for [use case]"
- "[product] vs [competitor] comparison"
- "what is [product]"
```

| Platform | Frequency | Focus |
|----------|-----------|-------|
| ChatGPT (GPT-4) | Weekly | Is brand mentioned? |
| Perplexity | Weekly | Are there citation links? |
| Claude | Weekly | Is information accurate? |
| Google AI Overview | Weekly | Appearing in AI summary? |

### When AI Gets It Wrong

If AI cites your product with incorrect information:
1. Update the corresponding page on your site
2. IndexNow push immediately
3. Re-check in 1-2 weeks

---

## GEO and E-E-A-T

AI models prefer to cite content with these signals:

| E-E-A-T Signal | How to Build |
|----------------|-------------|
| **Experience** | First-person narrative, specific cases, "we tried..." stories |
| **Expertise** | Precise numbers, correct industry terminology, technical depth |
| **Authoritativeness** | Cited by authoritative sites, media coverage, industry ratings |
| **Trustworthiness** | HTTPS, privacy policy, contact info, author bios |

**Key insight:** AI models are better at identifying "AI-generated mediocre content" than traditional search engines. Therefore, GEO's core competitive advantage is actually **authentic human experience and unique perspectives**.

---

*GEO Optimization Guide v1.0 — Gingiris SEO/GEO Playbook*
