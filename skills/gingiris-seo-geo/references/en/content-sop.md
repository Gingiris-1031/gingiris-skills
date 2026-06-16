# Content Production SOP

> End-to-end workflow from topic selection to publishing

---

## Content Cadence

| Content Type | Frequency | Goal |
|-------------|-----------|------|
| SEO blog articles | 4 per week | Long-tail coverage, organic traffic growth |
| Competitor comparison pages | Monthly updates | Capture decision-stage users |
| Customer case studies | 2-3 per quarter | E-E-A-T signals + backlinks |
| Product feature pages | On new feature launch | Feature keyword rankings |

---

## Article Production Workflow

### Step 1: Topic Selection & Keywords

```
Input:
- Keyword tools (Ahrefs / Google Search Console)
- Competitor content gap analysis
- User FAQs (support, community, search suggestions)

Selection criteria:
- KD: 30-50 (new sites can rank)
- Monthly volume: 100-1,000
- Commercial intent: Medium-High
- Content gap: existing results can be outranked

Output:
- Target keyword
- 3-5 secondary keywords
- Search intent (informational / comparison / transactional)
```

### Step 2: Outline Generation

```
Article structure template:

1. Time + Place anchored opening (2-3 sentences)
   → Precise time, location, scene, emotion

2. Key Stats table
   → Core data at a glance
   → AI engines directly cite this

3. Body with H2/H3 hierarchy
   → Each H2 = one core point
   → Each H2 contains actionable information
   → Naturally embed target and secondary keywords

4. Case/story interspersed
   → Personal experience → universal insight
   → Specific numbers + parenthetical asides

5. Key Takeaways list
   → 3-5 core points
   → Standalone readable summary

6. FAQ Section
   → 3-5 "People Also Ask" questions
   → Each answer 2-3 sentences, direct and structured

7. CTA
   → Link to product feature or trial page
```

### Step 3: Content Generation

**Writing voice checklist (check every article):**

- [ ] Opening has precise time/place anchored scene?
- [ ] Key Stats table after opening, before body?
- [ ] Has parenthetical asides for authenticity?
- [ ] Uses em-dashes (—) for rhythm?
- [ ] All numbers are precise, not vague?
- [ ] Has "personal experience → universal insight" narrative?
- [ ] Short paragraph rhythm (short-short-long)?

**SEO checklist:**

- [ ] Title contains target keyword? Under 60 characters?
- [ ] Meta description contains keyword? Under 160 characters?
- [ ] H1 matches or complements Title?
- [ ] H2/H3 naturally include secondary keywords?
- [ ] Images have alt text?
- [ ] Internal links to 2-3 related articles?
- [ ] External links to 1-2 authoritative sources?

**GEO checklist:**

- [ ] Article opens with one-line direct answer?
- [ ] Contains at least one comparison/data table?
- [ ] FAQ Section marked with FAQPage Schema?
- [ ] Article Schema includes author and date?
- [ ] Content has unique perspective (not rewrite of others)?

### Step 4: Multi-Platform Publishing

```
Publishing sequence:

1. GitHub _posts/ commit (English main site)
   → Filename: YYYY-MM-DD-slug.md
   → Front matter: title, date, categories, tags

2. en/index.html sync update
   → If article involves new tools/features

3. dev.to syndication
   → Use canonical_url pointing to main site
   → Record article ID

4. IndexNow push
   → New article URL
   → Updated page URLs

5. Social distribution
   → Twitter/X publish summary
   → Relevant Reddit/HN community sharing
```

### Step 5: Post-Publish Optimization

```
Week 1: Monitor initial rankings and traffic
Week 2-4: 
  - Check Google Search Console ranking positions
  - Ranking 11-20 → optimize content to break into page 1
  - Add internal links from other articles
Month 2+:
  - Update outdated data
  - Add new case studies/screenshots
  - Check AI citation status
```

---

## Content Templates

### Template 1: "How to" Tutorial

```markdown
---
title: "How to [Task] in 2026: [N] [Adjective] Methods"
---

[Time-anchored opening — 2-3 sentences]

| Key Stat | Value |
|----------|-------|
| [Metric 1] | [Data] |
| [Metric 2] | [Data] |

## What is [Topic]?

[One-line direct answer — AI citation friendly]

## Why [Topic] Matters

[2-3 paragraphs with data support]

## [N] Methods to [Task]

### 1. [Method 1]
[Specific steps + examples]

## Key Takeaways

- [Point 1]
- [Point 2]

## FAQ

### [Question 1]?
[Direct answer]
```

### Template 2: Customer Case Study

```markdown
---
title: "How [Company] [Result] with [Product]"
---

| Key Stat | Value |
|----------|-------|
| Company | [Name] |
| Industry | [Industry] |
| Challenge | [One line] |
| Result | [Core outcome number] |

## The Challenge
## The Solution
## The Results
## Key Takeaways
```

---

## Attribution Tracking

```
UTM parameter standards:
- utm_source=google / bing / dev.to / twitter
- utm_medium=organic / social / referral
- utm_campaign=seo-[page-type]
- utm_content=[keyword-or-content-id]
```

---

*Content Production SOP v1.0 — Gingiris SEO/GEO Playbook*
