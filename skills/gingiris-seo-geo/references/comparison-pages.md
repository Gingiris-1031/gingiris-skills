# 竞品对比页 SOP

> 对比页是 SEO 金矿 — 每个竞品一个独立页面，截获决策期用户

---

## 为什么对比页是 SEO 最高 ROI 的内容

搜索 "[产品A] vs [产品B]" 的用户已经在**购买决策的最后一步**。他们知道自己需要什么，正在两个选项之间做选择。

- **搜索意图极高** — 转化率是 TOFU 内容的 5-10 倍
- **竞品品牌词流量** — 借竞品知名度获取流量
- **AI 搜索最爱引用** — 结构化对比表是 AI 模型的首选引用格式
- **页面数量有限** — 5-10 个竞品 = 5-10 个高价值页面，投入产出比极高

---

## 页面结构模板

```
URL: /compare/[竞品名] 或 /[产品]-vs-[竞品]

H1: [产品] vs [竞品]: Which is Better in 2026?

├── Quick Comparison（总结表格 — AI 直接引用）
│
├── H2: TL;DR
│   └── 一段话总结：谁该用哪个
│
├── H2: [产品] Overview
│   └── 2-3 段产品介绍 + 核心优势
│
├── H2: [竞品] Overview
│   └── 2-3 段产品介绍 + 核心优势（客观）
│
├── H2: Feature Comparison
│   └── 详细功能对比表格（8-15 行）
│
├── H2: Pricing Comparison
│   └── 价格方案对比表格
│
├── H2: Pros and Cons
│   ├── H3: [产品] Pros & Cons
│   └── H3: [竞品] Pros & Cons
│
├── H2: Who Should Use [产品]?
│   └── 3-4 个使用场景
│
├── H2: Who Should Use [竞品]?
│   └── 3-4 个使用场景（客观）
│
├── H2: What Real Users Say
│   └── G2/Capterra 评价摘要
│
├── H2: Final Verdict
│   └── 明确推荐 + CTA
│
└── H2: FAQ
    └── 5-8 个常见问题
```

---

## Quick Comparison 表格

放在页面最上方（H1 之后），让用户和 AI 一眼看到核心差异：

```markdown
| Feature | [产品] | [竞品] |
|---------|--------|--------|
| Best For | [场景] | [场景] |
| Starting Price | $X/mo | $Y/mo |
| Free Tier | Yes / No | Yes / No |
| [核心功能1] | Yes | No |
| [核心功能2] | Yes | Yes |
| [核心功能3] | Yes | Limited |
| API Access | Yes | No |
| G2 Rating | 4.8/5 | 4.5/5 |
| Our Verdict | Best for [场景] | Best for [场景] |
```

---

## 关键词嵌入策略

### 目标关键词

```
主关键词: [产品] vs [竞品]
次级关键词:
  - [产品] vs [竞品] comparison
  - [产品] vs [竞品] pricing
  - [产品] alternative
  - [竞品] alternative
  - best [品类] software
  - [产品] or [竞品]
```

### Title 公式

```
[产品] vs [竞品]: Honest Comparison for 2026
[产品] vs [竞品]: Which [品类] Tool is Better?
[产品] vs [竞品]: Features, Pricing & Verdict
```

### Meta Description

```
Compare [产品] and [竞品] side by side. See features, pricing, 
pros & cons, and which [品类] tool is better for [场景] in 2026.
```

---

## 客观性原则

对比页的可信度取决于**客观性**。如果读者感觉你在踩竞品，信任度归零。

**规则：**

1. **承认竞品优势** — "[竞品] is excellent at [某方面], especially for [场景]"
2. **不贬低竞品** — 不说 "lacks" "fails to" "disappointing"，用 "doesn't include" "focuses on other areas"
3. **场景化推荐** — "If you need [X], choose [竞品]. If you need [Y], choose [产品]"
4. **数据说话** — 用 G2/Capterra 评分、功能事实，不用主观评价
5. **定期更新** — 竞品功能变化时及时更新（标注 "Last updated: [日期]"）

---

## Schema 标记

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[产品] vs [竞品]: Which is Better in 2026?",
  "datePublished": "2026-04-09",
  "dateModified": "2026-04-09",
  "author": {
    "@type": "Person",
    "name": "Iris Wei"
  }
}
```

加上 FAQPage Schema：

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is [产品] better than [竞品]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[产品] is better for [场景A], while [竞品] excels at [场景B]. Choose based on your specific needs."
      }
    },
    {
      "@type": "Question",
      "name": "How much does [产品] cost compared to [竞品]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[产品] starts at $X/month. [竞品] starts at $Y/month. Both offer free tiers."
      }
    }
  ]
}
```

---

## 竞品选择策略

### 必做对比页

| 竞品类型 | 数量 | 优先级 | 说明 |
|----------|------|--------|------|
| 直接竞品 | ≥5 | P0 | 同品类、同定位 |
| 间接竞品 | ≥3 | P1 | 可替代方案，不同路径解决同一问题 |
| 知名品牌 | 2-3 | P1 | 蹭品牌词流量（如 vs Notion, vs Slack） |

### 优先级排序

```
1. 搜索量最高的竞品品牌词
2. 正在快速增长的竞品（趋势词）
3. 用户最常问的对比（客服/社群反馈）
4. 你有明确优势的竞品（更容易转化）
```

---

## 发布与维护

### 发布清单

- [ ] URL 格式: /compare/[竞品名]（全小写，连字符分隔）
- [ ] Title + Meta Description 包含目标关键词
- [ ] Quick Comparison 表格在最上方
- [ ] FAQ Section + FAQPage Schema
- [ ] Article Schema 含作者和日期
- [ ] 内链到定价页和产品功能页
- [ ] IndexNow 推送新页面

### 月度维护

- [ ] 检查竞品定价是否变化
- [ ] 检查竞品新功能
- [ ] 更新 "Last updated" 日期
- [ ] 检查 G2/Capterra 评分变化
- [ ] IndexNow 推送更新

---

*竞品对比页 SOP v1.0 — Gingiris SEO/GEO Playbook*
