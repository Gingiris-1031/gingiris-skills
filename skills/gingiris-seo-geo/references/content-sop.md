# 内容生产 SOP

> 从选题到发布的完整流程

---

## 内容节奏

| 内容类型 | 频率 | 目标 |
|----------|------|------|
| SEO 博客文章 | 每周 4 篇 | 长尾词覆盖，有机流量增长 |
| 竞品对比页 | 每月更新 | 截获决策期用户 |
| 客户案例 | 每季度 2-3 个 | E-E-A-T 信号 + 反向链接 |
| 产品功能页 | 新功能上线时 | 功能关键词排名 |

---

## 文章生产流程

### Step 1: 选题与关键词

```
输入：
- 关键词工具（Ahrefs / Google Search Console）
- 竞品内容 gap 分析
- 用户常见问题（客服、社群、搜索建议）

筛选标准：
- KD: 30-50（新站可排名）
- 月搜索量: 100-1000
- 商业意图: 中-高
- 内容差距: 现有结果质量可超越

输出：
- 目标关键词
- 次级关键词 3-5 个
- 搜索意图判断（信息型 / 对比型 / 交易型）
```

### Step 2: 大纲生成

```
文章结构模板：

1. 时间+地点锚定开场（2-3 句）
   → 精确的时间、地点、场景、情绪

2. Key Stats 表格
   → 文章核心数据一目了然
   → AI 引擎直接引用

3. 正文 H2/H3 层级
   → 每个 H2 对应一个核心观点
   → 每个 H2 内包含可操作的信息
   → 自然嵌入目标关键词和次级关键词

4. 案例/故事穿插
   → 个人经验 → 普遍洞察
   → 具体数字 + 括号旁白

5. Key Takeaways 列表
   → 3-5 条核心要点
   → 可独立阅读的要点总结

6. FAQ Section
   → 覆盖 3-5 个 "People Also Ask" 问题
   → 每个回答 2-3 句，直接且结构化

7. CTA
   → 链接到产品功能页或试用页
```

### Step 3: 内容生成

**写作风格检查清单（每篇必查）：**

- [ ] 开头有精确的时间/地点锚定场景？
- [ ] Key Stats 表格在开场之后、正文之前？
- [ ] 有括号旁白制造真实感？
- [ ] 用了 em-dash (—) 转折？
- [ ] 数字是精确的，不是模糊的？
- [ ] 有"个人经验→普遍洞察"的叙事结构？
- [ ] 短段节奏（短-短-长）？

**SEO 检查清单：**

- [ ] Title 包含目标关键词？< 60 字符？
- [ ] Meta Description 包含关键词？< 160 字符？
- [ ] H1 与 Title 一致或互补？
- [ ] H2/H3 自然包含次级关键词？
- [ ] 图片有 alt text？
- [ ] 内链到 2-3 篇相关文章？
- [ ] 外链到 1-2 个权威来源？

**GEO 检查清单：**

- [ ] 文章开头直接回答核心问题（一句话）？
- [ ] 包含至少一个对比/数据表格？
- [ ] FAQ Section 用 FAQPage Schema 标记？
- [ ] Article Schema 包含作者和日期？
- [ ] 内容有独特观点（不是其他文章的改写）？

### Step 4: 多平台发布

```
发布顺序：

1. GitHub _posts/ 提交（英文主站）
   → 文件名: YYYY-MM-DD-slug.md
   → Front matter: title, date, categories, tags

2. en/index.html 同步更新
   → 如果文章涉及新工具/功能

3. dev.to 同步发布
   → 使用 canonical_url 指向主站
   → 记录 article ID

4. IndexNow 推送
   → 新文章 URL
   → 更新的页面 URL

5. 社交分享
   → Twitter/X 发布摘要
   → 相关 Reddit/HN 社区分享
```

### Step 5: 发布后优化

```
Week 1: 监测初始排名和流量
Week 2-4: 
  - 检查 Google Search Console 排名位置
  - 排名 11-20 → 优化内容冲首页
  - 补充内链从其他文章
Month 2+:
  - 更新过时数据
  - 增加新案例/截图
  - 检查 AI 引用情况
```

---

## 内容模板库

### 模板 1: "How to" 教程

```markdown
---
title: "How to [任务] in 2026: [N] [形容词] Methods"
---

[时间锚定开场 — 2-3 句]

| Key Stat | Value |
|----------|-------|
| [指标1] | [数据] |
| [指标2] | [数据] |
| [指标3] | [数据] |

## What is [主题]?

[一句话直接回答 — AI 引用友好]

## Why [主题] Matters

[2-3 段，包含数据支撑]

## [N] Methods to [任务]

### 1. [方法1]
[具体步骤 + 示例]

### 2. [方法2]
[具体步骤 + 示例]

...

## Key Takeaways

- [要点1]
- [要点2]
- [要点3]

## FAQ

### [问题1]?
[直接回答]

### [问题2]?
[直接回答]
```

### 模板 2: "[A] vs [B]" 对比

→ 详见 [竞品对比页 SOP](comparison-pages.md)

### 模板 3: 客户案例

```markdown
---
title: "How [公司] [成果] with [产品]"
---

| Key Stat | Value |
|----------|-------|
| Company | [公司名] |
| Industry | [行业] |
| Challenge | [一句话] |
| Result | [核心成果数字] |

## The Challenge

[客户面临的问题 — 2-3 段]

## The Solution

[如何使用产品解决 — 包含具体功能]

## The Results

[数据！数据！数据！]
- [成果1]: [数字]
- [成果2]: [数字]
- [成果3]: [数字]

## Key Takeaways

[其他用户可以学到什么]
```

---

## 归因追踪

```
UTM 参数标准化:
- utm_source=google / bing / dev.to / twitter
- utm_medium=organic / social / referral
- utm_campaign=seo-[页面类型]
- utm_content=[关键词或内容标识]

示例：
https://your-site.com/pricing?utm_source=google&utm_medium=organic&utm_campaign=seo-pricing
```

---

*内容生产 SOP v1.0 — Gingiris SEO/GEO Playbook*
