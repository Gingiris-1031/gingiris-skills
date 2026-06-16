# SEO 技术基础

> 核心页面优化、Schema 标记、站点架构

---

## 核心页面 SEO

### 首页

**Title 公式**
```
[产品名] - [一句话价值主张] | [品类] Software
例: HeyGen - AI Video Generator for Enterprise | Video Creation Platform
```

**Meta Description**
```
[产品名] helps [目标用户] [核心价值]. [关键功能]. Start free trial today.
例: HeyGen helps marketers create professional videos in minutes with AI avatars. 
No filming required. Start your free trial.
```

**必备元素：**
- H1 包含核心关键词
- 首屏有明确的 CTA（Free Trial / Book Demo）
- 社会证明（客户 Logo、使用数据）
- SoftwareApplication Schema

### 产品/功能页

每个核心功能需要独立页面：

```
/features/[功能名]

- 独立的 Title + Meta（包含功能关键词）
- H1: [功能名] - [价值描述]
- 功能截图/视频
- 使用场景 + 客户引用
- CTA: Try [功能] Free
```

### 定价页

```
Title: [产品名] Pricing - Plans & Features | Start Free
URL: /pricing

必备：
- 清晰的价格表格（AI 直接引用）
- 功能对比矩阵
- FAQ Section（用 FAQPage Schema）
- 年付 vs 月付切换
- Enterprise "Contact Sales" CTA
```

---

## Schema 标记体系

### SoftwareApplication（产品首页）

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "产品名",
  "description": "一句话描述",
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

### FAQPage（定价页、产品页）

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does [产品] cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[产品] starts at $X/month. Free tier available."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a free trial?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, 14-day free trial, no credit card required."
      }
    }
  ]
}
```

### Article（博客文章）

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "文章标题",
  "author": {
    "@type": "Person",
    "name": "作者名",
    "url": "作者主页"
  },
  "datePublished": "2026-04-09",
  "dateModified": "2026-04-09",
  "publisher": {
    "@type": "Organization",
    "name": "品牌名"
  }
}
```

---

## 站点技术架构

### URL 结构

```
/                           → 首页
/features/[功能名]           → 功能页
/pricing                    → 定价页
/compare/[竞品名]            → 对比页
/blog/[slug]                → 博客文章
/customers/[公司名]          → 案例研究
/docs/                      → 文档
/glossary/[术语]             → 术语页
```

### Core Web Vitals 清单

| 指标 | 目标 | 优化方法 |
|------|------|---------|
| LCP (Largest Contentful Paint) | < 2.5s | 图片压缩 + CDN + 预加载 |
| FID (First Input Delay) | < 100ms | 减少主线程阻塞 JS |
| CLS (Cumulative Layout Shift) | < 0.1 | 图片/视频预设尺寸 |

### 技术 SEO 清单

- [ ] XML Sitemap 提交到 Google Search Console 和 Bing Webmaster
- [ ] robots.txt 正确配置（允许 AI 爬虫，见 GEO 指南）
- [ ] HTTPS 全站
- [ ] 移动端适配（Responsive Design）
- [ ] 404 页面自定义 + 提供导航
- [ ] 301 重定向处理旧 URL
- [ ] Canonical URL 避免重复内容
- [ ] hreflang 标签（多语言站点）
- [ ] 内部链接结构（面包屑导航）
- [ ] 页面加载速度 < 3 秒

---

## 反向链接策略

### B2B/SaaS 高价值链接来源

| 来源类型 | 获取方式 | 难度 | 价值 |
|----------|---------|------|------|
| G2/Capterra/TrustRadius | 产品提交 + 邀请评价 | 低 | 高（DA 90+） |
| 行业媒体 | PR / Guest Post | 中 | 高 |
| 合作伙伴官网 | 生态/集成页面互链 | 中 | 中 |
| 客户官网 | 案例研究引用 | 中 | 中 |
| Awesome Lists (GitHub) | PR 提交 | 低 | 中 |
| 技术博客评测 | 评测邀请 | 高 | 高 |
| Zapier/Make 生态 | 集成开发 + 提交 | 中 | 中 |

### 执行步骤

```
Week 1: 提交评测平台（G2, Capterra, TrustRadius）
Week 2: 申请集成生态（Zapier, Make, 框架官网）
Week 3: 邀请客户背书（Logo 授权 + 案例链接）
Week 4: Guest Post 投稿行业媒体
持续: 每月 10+ 高质量反向链接目标
```

---

## 监测指标

| 指标 | 工具 | 目标 |
|------|------|------|
| 自然搜索流量 | GA4 | 月增 10%+ |
| 关键词排名 | Ahrefs | 核心词进前 10 |
| 页面收录数 | Google Search Console | 全部核心页被收录 |
| Core Web Vitals | PageSpeed Insights | 全绿 |
| 反向链接数 | Ahrefs | 月增 10+ 高质量 |

---

*SEO 技术基础 v1.0 — Gingiris SEO/GEO Playbook*
