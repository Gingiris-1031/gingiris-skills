# HARO / Featured.com Response Template

> Copy-paste, fill the brackets, send. Target: 8-12 minutes per response.

## Subject line (HARO requires keyword from request)
```
Re: [exact keyword from journalist's request] — quote from ex-AFFiNE COO
```

## Body

```
Hi [Journalist Name, or "Reporter" if unknown],

I'm Iris Wei, ex-COO of AFFiNE (60k+ GitHub stars, 30x Product Hunt #1
winner across 2020-2026). For your question on [TOPIC]:

[3-SENTENCE ANSWER — structure:
 1. Lead with a number ("In our 30-launch dataset...")
 2. Give the mechanism ("...we found X correlates 4x more than Y")
 3. End with takeaway ("...so the practical move is Z")]

If you need a longer quote, follow-up data, or a screenshot from
our analytics, happy to share.

— Iris Wei
   Ex-COO @ AFFiNE → growth consulting @ Gingiris
   Site: https://gingiris.tools
   X: @WeiYipei

[Disclosure: I run gingiris.tools and analook.com.
 No expectation of a link in your article — providing this quote because the
 data is unique and the topic matches my domain.]
```

---

## Domain-specific opening hooks (pick one matching the journalist's beat)

### Open source / GitHub stars
> "Across the 0→60k journey of AFFiNE, the single biggest growth lever..."

### Product Hunt / startup launches
> "From 30 Product Hunt #1 wins in 2020-2026, the metric that predicts top finish is..."

### SEO / GEO / AI search
> "Auditing 58 indie SaaS blogs in Q2 2026, the top correlate with AI citations is..."

### B2B SaaS growth
> "From running PLG / SLG hybrid playbooks for AFFiNE, the under-discussed pattern is..."

### Indie hacking / 0→1
> "Building Gingiris from 0 to 155 monthly active users in 4 weeks, the highest-ROI..."

---

## Quote rate optimization (what bumps you from 5% → 25%)

| Signal | Multiplier |
|---|---|
| **Specific number** in first sentence | 2x |
| **Personal anecdote** (not generic advice) | 1.5x |
| **Credential in signature** (ex-AFFiNE COO) | 1.5x |
| **Disclosure paragraph** (transparency) | 1.2x |
| **Response within 4 hours** of HARO email | 2x |
| **Niche match** (don't reach for off-topic) | 3x |

Combine all 6 → ~25% quote rate. That's the upper bound for inbound expert quotes.

---

## What NOT to send

- ❌ Generic advice ("Make sure your content is high quality")
- ❌ Marketing pitch ("Our tool solves this")
- ❌ Vague claims ("Many startups find that...")
- ❌ Long backstory before the answer
- ❌ Multiple URLs (looks SEO-spammy → journalist filters out)
- ❌ Bullet points (HARO expects prose)

---

## Tracking

Log every response in `data/backlinks.jsonl`:
```jsonl
{"date":"2026-05-15","channel":"HARO","journalist":"...","topic":"...","status":"sent|quoted|ignored","url_if_published":""}
```

Quoted rate should hit 15-25% with 8 weeks of practice.
