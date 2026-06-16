# SEO Technical Foundations

> Core page optimization, Schema markup, site architecture

---

## Core Page SEO

### Homepage

**Title Formula**
```
[Product] - [One-line Value Prop] | [Category] Software
e.g.: HeyGen - AI Video Generator for Enterprise | Video Creation Platform
```

**Meta Description**
```
[Product] helps [target users] [core value]. [Key feature]. Start free trial today.
```

**Required elements:**
- H1 contains core keyword
- Above-fold CTA (Free Trial / Book Demo)
- Social proof (customer logos, usage stats)
- SoftwareApplication Schema

### Product / Feature Pages

Each core feature gets its own page:

```
/features/[feature-name]

- Independent Title + Meta (with feature keyword)
- H1: [Feature] - [Value Description]
- Feature screenshot/video
- Use cases + customer quotes
- CTA: Try [Feature] Free
```

### Pricing Page

```
Title: [Product] Pricing - Plans & Features | Start Free
URL: /pricing

Required:
- Clear pricing table (AI directly cites this)
- Feature comparison matrix
- FAQ Section (with FAQPage Schema)
- Annual vs monthly toggle
- Enterprise "Contact Sales" CTA
```

---

## Schema Markup System

### SoftwareApplication (Product Homepage)

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Product Name",
  "description": "One-line description",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "0",
    "highPrice": "999",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "1200"
  }
}
```

### FAQPage (Pricing, Product Pages)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does [product] cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Product] starts at $X/month. Free tier available."
      }
    }
  ]
}
```

### Article (Blog Posts)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article title",
  "author": {
    "@type": "Person",
    "name": "Author name",
    "url": "Author URL"
  },
  "datePublished": "2026-04-09",
  "dateModified": "2026-04-09"
}
```

---

## Site Technical Architecture

### URL Structure

```
/                           → Homepage
/features/[feature-name]     → Feature pages
/pricing                    → Pricing page
/compare/[competitor]        → Comparison pages
/blog/[slug]                → Blog posts
/customers/[company]         → Case studies
/docs/                      → Documentation
/glossary/[term]             → Glossary pages
```

### Core Web Vitals Targets

| Metric | Target | How to Optimize |
|--------|--------|----------------|
| LCP (Largest Contentful Paint) | < 2.5s | Image compression + CDN + preload |
| FID (First Input Delay) | < 100ms | Reduce main-thread blocking JS |
| CLS (Cumulative Layout Shift) | < 0.1 | Preset dimensions for images/video |

### Technical SEO Checklist

- [ ] XML Sitemap submitted to Google Search Console and Bing Webmaster
- [ ] robots.txt properly configured (allow AI crawlers — see GEO guide)
- [ ] HTTPS sitewide
- [ ] Mobile responsive design
- [ ] Custom 404 page with navigation
- [ ] 301 redirects for old URLs
- [ ] Canonical URLs to avoid duplicate content
- [ ] hreflang tags (multi-language sites)
- [ ] Internal linking structure (breadcrumbs)
- [ ] Page load speed < 3 seconds

---

## Backlink Strategy

### High-Value Link Sources for B2B/SaaS

| Source Type | How to Get | Difficulty | Value |
|------------|-----------|-----------|-------|
| G2/Capterra/TrustRadius | Product submission + invite reviews | Low | High (DA 90+) |
| Industry media | PR / Guest Post | Medium | High |
| Partner sites | Ecosystem/integration page cross-links | Medium | Medium |
| Customer sites | Case study citations | Medium | Medium |
| Awesome Lists (GitHub) | PR submission | Low | Medium |
| Tech blog reviews | Review invitations | High | High |
| Zapier/Make ecosystem | Build integration + submit | Medium | Medium |

### Execution Steps

```
Week 1: Submit to review platforms (G2, Capterra, TrustRadius)
Week 2: Apply to integration ecosystems (Zapier, Make, framework sites)
Week 3: Invite customer endorsements (logo rights + case study links)
Week 4: Guest post pitches to industry media
Ongoing: Target 10+ quality backlinks per month
```

---

## Monitoring Metrics

| Metric | Tool | Target |
|--------|------|--------|
| Organic search traffic | GA4 | 10%+ monthly growth |
| Keyword rankings | Ahrefs | Core terms in top 10 |
| Pages indexed | Google Search Console | All core pages indexed |
| Core Web Vitals | PageSpeed Insights | All green |
| Backlink count | Ahrefs | 10+ quality links/month |

---

*SEO Technical Foundations v1.0 — Gingiris SEO/GEO Playbook*
