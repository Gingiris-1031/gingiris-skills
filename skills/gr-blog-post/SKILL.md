---
name: gr-blog-post
description: >
  Jekyll 博客发布流水线：按 Iris 文风（时间锚定开场、括号旁白、em-dash 转折、Key Stats 表格）生成文章，
  附带 frontmatter（title / date / canonical_url / hreflang_ja / hreflang_ko / FAQ schema）、
  多语言同步（en/ja/ko）、自动建内链。当用户说"写一篇博客"、"发新文章"、"同步日韩版本"时调用。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-blog-post
---

# gr-blog-post — Jekyll 博客发布

## 产出的文章必须符合

### Iris 文风 5 要素（详见 `知识库/Skill知识包/iris_writing_style.md`）

1. **时间锚定开场** —— 不说"SEO 很重要"，说"2026-04-10，凌晨 3 点，后台流量归零"
2. **括号旁白** —— 正文一句，括号里挤私货（"...—— 别问怎么知道的"）
3. **em-dash 转折** —— 不用"但是"，用 `——`
4. **Key Stats 表格** —— 文章开头或 H2 下第一屏放一个硬数据表，3-5 行
5. **GEO 直接答案段落** —— 文章顶部一段 30-50 字直接回答主问题，方便 AI 爬虫抽取

### 技术 frontmatter 模板

```yaml
---
layout: post
title: "主关键词前置，副标题用冒号：不超过 60 字"
date: 2026-04-15 14:30:00 +0800
categories: [seo, growth]
tags: [...]
canonical_url: https://gingiris.github.io/growth-tools/blog/2026/04/15/slug/
hreflang_ja: /blog/2026/04/15/slug-ja/
hreflang_ko: /blog/2026/04/15/slug-ko/
description: "150-160 字 meta description，含主关键词"
faq:
  - q: "直接问句"
    a: "30-50 字硬答案"
---
```

---

## 发布流程

### 1. 选题
- 读 `gr-seo-patrol` 输出，找"top 30 但没 top 10"的关键词
- 或读 `gr-competitor`，找对手新打法
- ❌ 不做重复主题（先 `site:` 查站内是否已有）

### 2. 写初稿
- 时间锚定开场（当前日期 + 具体场景）
- 第一屏：GEO 直接答案段（30-50 字）+ Key Stats 表（硬数据）
- H2 结构：问题 → 框架 → 案例 → 陷阱 → 下一步
- 每个 H2 下 200-400 字，不超过 600 字

### 3. 内链
- 向前：链接 2-3 篇已发布的同主题文章（用主关键词作 anchor）
- 向后：站内 index / hub 页
- 权重传导：从流量最大的 3 篇文章加内链到新文

### 4. FAQ Schema
- 3-5 个问答
- 问句必须是用户真实搜索句（从 GSC / People also ask 抓）
- 答案硬、短、可引用

### 5. Canonical 策略
- **默认 self-canonical**
- 如果是同主题系列的分篇 → canonical 指向 master
- ja/ko 翻译版 → 自身 canonical + hreflang 互指

### 6. 多语言同步
- 用 `scripts/sync-i18n.py`（roadmap）从英文自动产日韩草稿
- 人工过一遍（机翻硬伤 + 文化适配）
- 日韩版本独立 slug，不复用英文 slug

### 7. 发布
- GitHub Contents API PUT（不要 `git push`）
- Commit message: `post: {slug} ({lang})`

### 8. 发布后 24h
- 加入 `gr-seo-patrol` 监控名单
- Google Search Console 手动提交
- 社交平台分发（推特 / LinkedIn / dev.to）

---

## 反模式

- ❌ 不要用 AI 味重的模板（"In today's digital landscape..."）—— 过不了 `dbs-ai-check`
- ❌ 不要 H1 堆关键词
- ❌ 不要忘记 hreflang —— 已发布的旧文补翻译时要回改原文 frontmatter
- ❌ 不要同一关键词发 3 篇 —— cannibalization 立刻找上门

---

## 级联推荐

- 写完 → `gr-seo-patrol` 加监控
- 发现是系列稿 → `gr-blog-post` 继续产第 2 篇并设 canonical
- 英文发完 24h → 手动触发日韩翻译

---

## API 依赖

| Service | Env var |
|---|---|
| GitHub PAT | `GITHUB_TOKEN` |
| DeepSeek / Teamo（翻译） | `DEEPSEEK_API_KEY` / `TEAMOROUTER_API_KEY` |


---

## Citability-by-Design Spec (mandatory for NEW articles, 2026-05-18+)

**Rationale**: Verified 2026-05-07 that retrofitting old articles hits a ~65-68/100 citability ceiling no matter what (booster passages, surgical rewrites, splitting all produce diminishing returns). **Writing new articles from this spec produces 75-85 baseline directly.** Spec saves ~3 hours of post-hoc citability fixing per article.

### Per-section structural requirements

Every H2/H3 section must satisfy ALL of:

1. **Word count: 134-167** (the AI-extraction sweet spot validated by zubair-trabzada/geo-seo-claude scoring)
   - Under 134 → self_containment drops below 10/25
   - Over 167 → same penalty for being too long for AI chunks
   - Use a word counter as you draft

2. **Opening sentence = definition pattern**, one of:
   - `[Thing] is [definition]`
   - `[Thing] refers to [scope]`
   - `[Thing] means [unpacking]`
   - `In other words, [Thing] is...`
   - `[Thing] can be defined as...`

3. **Section contains at least ONE of each**:
   - ✅ Original research signal: "Our X-launch dataset", "We tracked", "Our 2026 audit measured", "Our analysis of N samples"
   - ✅ Specific number with unit: "60K stars", "30 launches", "$79/mo", "67%"
   - ✅ Specific named product/tool: "Taplio ($39/mo)", "Surfe", "PH Deck", "Loom" — by name not "[the tool]"

### Heading conventions

- H1 = page title (≤ 70 chars after title-suffix fix from 2026-05-07)
- H2 should be **question form** ~40% of the time:
  - ✅ "How do I get cited by Perplexity in 2026?"
  - ✅ "What is the GEO three-piece set?"
  - ❌ "Perplexity citation strategy"

- Each H2 should contain primary keyword **or** clear question intent

### Article-level requirements

- 5-12 H2 sections (sweet spot: 7-8)
- TL;DR or "Citable Statistics" block IN FIRST H2 (becomes top-scored passage)
- FAQ Schema JSON-LD at end (5+ Q&A using exact User-Search-Form questions)
- `last_modified_at:` frontmatter (flows through to dateModified schema)
- canonical_url self-reference
- hreflang_ja / hreflang_ko if multilingual variants exist

### Citability self-check before publishing

Run **before** committing the article:

```bash
python3 skills/gr-geo-cite/scripts/citability-scorer.py /local/path/to/draft.html
```

Target: page score ≥ 75. If under 70, revise top 2 weakest passages.

### Anti-patterns (avoid)

- ❌ Long expository paragraphs (200+ words) — split into 2 sections at 134-167 each
- ❌ Generic transitions ("Now let's discuss...") — replace with definition pattern
- ❌ Marketing fluff ("the best way to") — replace with measured claims with data
- ❌ "[Tool name]" placeholders — always cite the specific tool by name + price
- ❌ Bullet lists with single words — combine into prose with definition + example pattern

### Real-data benchmark

Articles from 2026-05-07 audit (without this spec):

| Article (old, retrofit) | Score | Pattern |
|---|---|---|
| PH playbook master | 65 | Top passage 74, dragged by 62s |
| Social listening | 68 | Best of the 5 (early Citable Stats) |
| Community directory | 62 | Lifted from 54 via booster (+12% from 0 to 1 sweet-spot passage) |

Predicted from spec (NEW articles):

| Spec compliance | Predicted score |
|---|---|
| All sections 134-167 + definition pattern + 1 original signal | **78-85** |
| 80% sections compliant, 20% legacy structure | 72-77 |
| 50% compliant | 65-70 (same as retrofit ceiling) |

The marginal value of strict compliance is **~10 points** vs partial compliance.
