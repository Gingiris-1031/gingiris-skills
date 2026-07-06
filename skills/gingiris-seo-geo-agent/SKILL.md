---
name: gingiris-seo-geo-agent
description: |
  🇺🇸 SEO/GEO Agent Operations SOP — A complete hands-on playbook to run an autonomous SEO Agent that achieves ~32K impressions in one month. Covers Week 0-4 timeline, daily/weekly/monthly SOPs, keyword-to-landing-page mapping, CTA conversion blocks, daily report template, GEO triple combo (IndexNow + robots.txt + AI-friendly format), tool stack selection, and Owner Checklist. Battle-tested with real content site data. **Optimized for dev tools / OSS / B2B SaaS. 2C products: see gingiris-seo-geo/references/2c-adaptation.md for adjusted parameters.**

  🇨🇳 SEO/GEO Agent 运营 SOP —— 一份谁都能照着做的手把手手册，用一个 SEO Agent 跑到一个月 ~3.2 万曝光。包含 Week 0-4 时间线、每日/每周/每月 SOP、关键词→落地页映射表、CTA 转化块模板、每日报告模板、GEO 三件套（IndexNow + robots.txt + AI 爬虫开放）、工具链选型、产品负责人任务清单。经真实内容站验证。**默认适用于开发者工具 / 开源 / B2B SaaS，2C 产品请参考 gingiris-seo-geo/references/2c-adaptation.md。**

  🇯🇵 SEO/GEO エージェント運用SOP — 1ヶ月で約3.2万インプレッションを達成する自律型SEOエージェントの完全マニュアル。Week 0-4タイムライン、日次/週次/月次SOP、キーワード→LP対応表、CTAテンプレート、デイリーレポート、GEOトリプルセット。**デフォルトは開発者ツール/OSS/B2B SaaS向け。2C製品は gingiris-seo-geo/references/2c-adaptation.md 参照。**

  🇰🇷 SEO/GEO 에이전트 운영 SOP — 한 달 만에 ~3.2만 노출을 달성하는 자율 SEO 에이전트 완전 매뉴얼. Week 0-4 타임라인, 일간/주간/월간 SOP, 키워드→랜딩페이지 매핑, CTA 블록, 일일 보고서, GEO 트리플 콤보. **기본값은 개발자 도구/OSS/B2B SaaS용. 2C 제품은 gingiris-seo-geo/references/2c-adaptation.md 참조.**

  Triggers: "SEO agent" | "SEO automation" | "SEO Agent SOP" | "autonomous SEO" | "SEO daily report" | "SEO Agent运营" | "SEO自动化" | "GEO agent" | "32K impressions" | "3.2万曝光" | "keyword mapping" | "CTA conversion SOP" | "SEO报告模板" | "IndexNow setup" | "AI crawler robots.txt" | "DataForSEO" | "SEO工具链" | "SEO Agent 日报"
when_to_use: |
  Use to operate an autonomous SEO agent: daily/weekly/monthly SOPs, keyword→landing-page
  mapping, CTA conversion blocks, IndexNow + robots.txt for AI crawlers, SEO reporting templates.
  Enforces 2026-06-24 standards: keyword filter volume 300-1000/KD 5-35, internal links
  ≤2-3 per paragraph, title must contain best/free/top/guide+year, actively cite competitor
  blogs as external links, BreadcrumbList schema, $20-30 quality backlink outreach SOP,
  Bing IndexNow for GEO, GA4 AI traffic channel grouping.
---

## ⚠️ 使用前：确认你的产品类型

本 skill 默认场景：**开发者工具 / 开源项目 / B2B SaaS 出海**

如果你的产品是 **2C 消费品 / 教育 / 应用 / 游戏**，关键参数需要调整（如 volume 下限改为 50、E-E-A-T 加载 YMYL 要求、启动渠道换为 Reddit/小红书/Quora 等），详细指南见：[`gingiris-seo-geo/references/2c-adaptation.md`](../gingiris-seo-geo/references/2c-adaptation.md)

> 💡 安装后验证：运行 `ls references/` 确认 `full-sop.md` 存在。若缺失请重装：`npx skills add Gingiris-1031/gingiris-seo-geo-agent`

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
- **Bing IndexNow** 配置（不局限于 Google，让大模型更快 discover/index）
- 关键词种子表 30-50 词，筛选标准：**volume 300–1,000 / KD 5–35 / traffic potential 300+**
- 属意图判断：先看 Google top-10（忽略 Sponsored）再写，内容必须对齐意图
- 扒竞品 blog 最新文找还没被爬到的新词
- 记录基线

### Week 1 — BOFU 落地页
- 产品核心页 + 定价页（带 FAQ Schema，FAQPage JSON-LD 5–8 题）
- 前 3-5 个竞品对比页
- 每页必带 CTA 块 + Bing IndexNow 推送
- **标题套路**：必含 best / free / top / guide + 年份
- **面包屑导航**：BreadcrumbList schema + 页面内可见
- **Meta description**：关键词 rephrase（不是重复关键词，是改说法）

### Week 2 — 内链结构 + 分发铺面
- Topic Cluster：1 支柱页 + 4-6 集群页互链
- **内链密度铁律：每段 ≤ 2-3 个**（达到上限 → Google spam 信号 → 降 ranking）
- **主动 cite 竞品 blog 外链**（Google 视为客观 → 信用分上升 → ranking 上升）
- 分发平台同步（dev.to 等，self-canonical，≥7 天后发布 + "Originally published at" 互链——与 gr-blog-post 红线对齐 2026-07-06）
- 给已有排名页加内链

### Week 3 — GEO 强化
- FAQPage JSON-LD（5–8题）——问题必须是用户真实搜索句，不是营销话术
- 文章开头「一句话回答 + Key Stats 表格」
- 添加/更新【最后更新日期】freshness 标记
- GA4 配置 AI 来源 channel grouping（ChatGPT/Perplexity/Claude referral 单独追踪）
- 监控 AI Overview 引用

### Week 4 — CTR 榨取 + 规模化
- 高曝光低点击页面重写标题/描述，应用 best/free/top/guide+年份 公式
- 排名 11-20 冲首页
- **外链建设：向评测/目录站提交 listing（提交费 $20–30/批），获取自然收录外链**——不是购买 dofollow 链接（买链见 gr-backlinks 反模式：数天内被 Google 标记），避开论坛批量外链（penalty 风险）
- 维持每周 4 篇长尾内容（KD 5–35 区间）

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

## Platform Description

**EN:** SEO/GEO Agent Operations SOP — Day-by-day autonomous agent SOP for ~32K impressions/month. Optimized for dev tools / OSS / B2B SaaS. 2C products: see gingiris-seo-geo/references/2c-adaptation.md. Enforces 2026-06-24 standards: keyword filter volume 300–1,000 / KD 5–35 / traffic potential 300+, internal links ≤2–3 per paragraph, actively cite competitor blogs as external links, title must contain best/free/top/guide+year, meta description keyword rephrase, BreadcrumbList schema, $20–30 quality backlink outreach (avoid forum bulk links), Bing IndexNow for GEO indexing, GA4 AI traffic channel grouping.

**ZH:** SEO/GEO Agent 运营 SOP（2026-06-24 标准）——一个 agent 跑到一个月 ~3.2 万曝光的逐日执行手册。内嵌标准：关键词 volume 300–1,000 / KD 5–35 / traffic potential 300+，内链每段 ≤2–3 个，主动 cite 竞品外链，标题必含 best/free/top/guide+年份，meta description 关键词 rephrase，面包屑 BreadcrumbList schema，$20–30 高质量外链（避开论坛批量外链），Bing IndexNow，GA4 AI 流量频道分组。

**JA:** SEO/GEO エージェント運用SOP（2026-06-24基準）— 1ヶ月で約3.2万インプレッションを達成する自律型SOP。キーワード基準: volume 300–1,000/KD 5–35/トラフィックポテンシャル300+。内部リンクは段落あたり≤2–3個、競合ブログへの外部リンク、タイトルにbest/free/top/guide+年、BreadcrumbListスキーマ、$20–30外部リンク獲得、Bing IndexNow、GA4 AIトラフィック分析。

**KO:** SEO/GEO 에이전트 운영 SOP（2026-06-24 기준）— 한 달 만에 ~3.2만 노출을 달성하는 자율형 SOP. 키워드 기준: volume 300–1,000/KD 5–35/traffic potential 300+. 내부링크 단락당 ≤2–3개, 경쟁사 블로그 외부링크 인용, 제목 best/free/top/guide+연도, BreadcrumbList 스키마, $20–30 고품질 백링크, Bing IndexNow, GA4 AI 트래픽 추적.

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
