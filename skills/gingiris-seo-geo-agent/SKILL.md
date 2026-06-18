---
name: gingiris-seo-geo-agent
description: |
  🇺🇸 SEO/GEO Agent Operations SOP — A complete hands-on playbook to run an autonomous SEO Agent that achieves ~32K impressions in one month. Covers Week 0-4 timeline, daily/weekly/monthly SOPs, keyword-to-landing-page mapping, CTA conversion blocks, daily report template, GEO triple combo (IndexNow + robots.txt + AI-friendly format), tool stack selection, and Owner Checklist. Battle-tested with real content site data.

  🇨🇳 SEO/GEO Agent 运营 SOP —— 一份谁都能照着做的手把手手册，用一个 SEO Agent 跑到一个月 ~3.2 万曝光。包含 Week 0-4 时间线、每日/每周/每月 SOP、关键词→落地页映射表、CTA 转化块模板、每日报告模板、GEO 三件套（IndexNow + robots.txt + AI 爬虫开放）、工具链选型、产品负责人任务清单。经真实内容站验证。

  🇯🇵 SEO/GEO エージェント運用SOP — 1ヶ月で約3.2万インプレッションを達成する自律型SEOエージェントの完全マニュアル。Week 0-4タイムライン、日次/週次/月次SOP、キーワード→LP対応表、CTAテンプレート、デイリーレポート、GEOトリプルセット。

  🇰🇷 SEO/GEO 에이전트 운영 SOP — 한 달 만에 ~3.2만 노출을 달성하는 자율 SEO 에이전트 완전 매뉴얼. Week 0-4 타임라인, 일간/주간/월간 SOP, 키워드→랜딩페이지 매핑, CTA 블록, 일일 보고서, GEO 트리플 콤보.

  Triggers: "SEO agent" | "SEO automation" | "SEO Agent SOP" | "autonomous SEO" | "SEO daily report" | "SEO Agent运营" | "SEO自动化" | "GEO agent" | "32K impressions" | "3.2万曝光" | "keyword mapping" | "CTA conversion SOP" | "SEO报告模板" | "IndexNow setup" | "AI crawler robots.txt" | "DataForSEO" | "SEO工具链" | "SEO Agent 日报"
when_to_use: |
  Use this skill when you need to: operate an autonomous SEO agent (32K impressions/month),
  run daily/weekly/monthly SEO SOPs, map keywords to landing pages, set up CTA conversion
  blocks, configure IndexNow + robots.txt for AI crawlers, or build SEO reporting templates.
  Trigger phrases: "SEO agent" | "SEO automation" | "SEO日报" | "SEO自动化" |
  "keyword mapping" | "IndexNow" | "SEO Agent运营" | "3.2万曝光"
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-seo-geo-agent
tags:
  - seo
  - geo
  - generative-engine-optimization
  - ai-search-optimization
  - content-seo
  - technical-seo
  - e-e-a-t
  - json-ld
  - schema-markup
  - indexnow
  - saas-seo
  - startup-marketing
  - claude-code
  - ai-agent-skill
  - latest
---

# SEO/GEO Agent 运营 SOP

> Language / 语言: [中文](#核心概念) | [English](#english-summary)
>
> 这是 `gingiris-seo-geo` 的**执行层搭档**：`gingiris-seo-geo` 教你「战略/方法论」，本 skill 教你「每天具体怎么跑」。

---

## 核心概念

这份 SOP 让一个 SEO Agent 自动执行**日、周、月**三层运营循环，目标：

1. 让尽可能多的关键词排进 Google 首页（Top 10）
2. 让 AI 搜索引擎（ChatGPT / Perplexity / Claude / Google AIO）引用你的内容
3. 把流量转化为注册/付费

### 与 `gingiris-seo-geo` 的关系

| 维度 | `gingiris-seo-geo` | `gingiris-seo-geo-agent`（本 skill） |
|------|--------------------|------------------------------------|
| 层次 | 战略 + 方法论 | 执行 + 自动化运营 |
| 输出 | 知识框架、原则 | 每日报告、关键词表、CTA块、时间线 |
| 使用者 | 创始人/增长负责人 | AI Agent + 产品负责人协作 |
| 时间粒度 | 长期指导 | Day-by-day SOP |

---

## 一个月 ~3.2 万曝光：总时间线

> 📊 实战参照：索引页 8 → 57（覆盖率 86%）；30词宽样本中 8-11 个进 Top 10；主站+分发平台双平台铺词。

### Week 0 — 地基与基线
- 完成 Owner Checklist（GSC/GA4/API/域名/CTA页）
- robots.txt 开放 AI 爬虫 + sitemap 提交
- IndexNow 配置
- 关键词种子表 30-50 词（标注 Volume/KD/意图）
- 记录基线

### Week 1 — BOFU 落地页
- 产品核心页 + 定价页（带 FAQ Schema）
- 前 3-5 个竞品对比页
- 每页必带 CTA 块 + IndexNow 推送

### Week 2 — 内链结构 + 分发铺面
- Topic Cluster：1 支柱页 + 4-6 集群页互链
- 分发平台同步（dev.to 等，canonical 指回主站）
- 给已有排名页加内链

### Week 3 — GEO 强化
- FAQPage JSON-LD（5-8题）
- 文章开头「一句话回答 + Key Stats 表格」
- 监控 AI Overview 引用

### Week 4 — CTR 榨取 + 规模化
- 高曝光低点击页面重写标题/描述
- 排名 11-20 冲首页
- 维持每周 4 篇长尾内容

---

## 详细指南

| 主题 | 文件 | 说明 |
|:---|:---|:---|
| 完整 SOP（全文） | [references/full-sop.md](references/full-sop.md) | 12节完整操作手册，含所有模板和清单 |

---

## 每日 SEO 报告模板（核心产出）

```markdown
# [PRODUCT] SEO 日报 — YYYY-MM-DD

## 🏆 首页战况
- **Google 首页关键词数 (Top 10)：N 个** ← 头条指标
- Top 3：n 个 | Top 30：M 个 | Top 100：K 个
- 索引页数：xx / sitemap总数（覆盖率%）

## 📋 关键词明细
| 关键词 | 落地页 | 排名 | 首页? | Δ昨日 | KD | Volume |
(全部 tracked 词)

## 🤖 GEO / AI 搜索战况
- AI Overview 引用情况
- AI 引流量（GA4）

## 📈 转化漏斗
- SEO自然流量 → CTA点击 → 注册

## 🔧 今日动作
## 🚩 需要产品负责人处理的
```

---

## Agent 角色设定

```
你是 [PRODUCT] 的 SEO/GEO 运营 Agent。唯一北极星指标：
让尽可能多的关键词排进 Google 首页（Top 10），并把曝光转化为 [CTA_GOAL]。

工作循环：
- 每天：排名监控 → 日报 → 1-2个优化动作
- 每周：GSC新词盘点 + CTR优化 + 内链加固
- 每月：11-20位冲首页 + CTA漏斗复盘

铁律：
1. 先做 BOFU，再做 MOFU/TOFU
2. 每篇都必须带 CTA 块
3. 日报头条必须是「首页关键词数」
4. 关键词/落地页/排名永远绑在一张表追踪
5. 做不了的交给产品负责人，不假装做了
6. 内容用真实创始人声音，不要写得像 AI
```

---

## 关键词→落地页主映射表（核心产出）

| 关键词 | 意图 | Volume | KD | 对应落地页 | 当前排名 | 首页? | CTA目标 | 状态 |
|--------|------|--------|----|-----------:|---------|------|---------|------|
| （每个词只绑一个主落地页，避免自相残杀） | | | | | | | | |

---

## CTA Convert Block 模板

```markdown
---
> **试试 [PRODUCT]** — [一句话价值主张]。
> [具体到本文场景的钩子]。
>
> 👉 [CTA按钮文案]([CTA_URL]?utm_source=blog&utm_medium=organic&utm_campaign=seo-[slug])
---
```

CTA 4要素：承接上文 / 降低门槛 / 明确动作 / 可追踪

---

## GEO 三件套

1. **IndexNow** — 秒级推送新内容
2. **robots.txt 开放 AI 爬虫** — GPTBot / OAI-SearchBot / ChatGPT-User / Claude-Web / PerplexityBot
3. **AI-Friendly 格式** — 一句话回答 + 对比表 + FAQ + 最后更新日期

---

## 工具链推荐

| 工具 | 用途 | 必要性 |
|------|------|--------|
| **DataForSEO** | Volume/KD/排名/AIO | ⭐必备 |
| **Google Search Console** | 真实曝光/点击/CTR | ⭐必备 |
| **GA4** | 流量/转化漏斗 | ⭐必备 |
| SerpApi | SERP/索引计数 | 可选 |
| SEO Review Tools | 外链/DA | 可选 |
| Brave Search API | GEO/AI摘要 | 可选 |

---

## English Summary

This skill provides a **complete day-by-day SOP** for running an autonomous SEO/GEO Agent that achieves ~32K Google impressions in one month. It's the execution-layer companion to `gingiris-seo-geo` (strategy).

**What's included:**
- Week 0-4 timeline (from zero to Top 10 keywords)
- Daily SEO report template (headline: "How many keywords on Google page 1?")
- Keyword → Landing Page master mapping table
- CTA conversion block template (every page must convert)
- GEO triple combo (IndexNow + AI crawlers + structured format)
- Tool stack (DataForSEO + GSC + GA4 minimum)
- Owner Checklist (what humans must do before Agent can run)
- CTR optimization 5-factor scoring
- Topic Cluster internal linking structure

**Relationship to other Gingiris skills:**
- `gingiris-seo-geo` = Strategy & methodology
- `gingiris-seo-geo-agent` = Daily execution & automation (this skill)
