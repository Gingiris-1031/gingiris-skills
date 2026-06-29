---
name: gingiris-seo-geo
description: |
  🇺🇸 SEO & GEO Dual-Engine Playbook 2026 — Rank on Google AND get cited by AI search (ChatGPT, Perplexity, Claude, Gemini). Battle-tested from AFFiNE (60k GitHub stars in 24 months) and 150+ AI startup consultations. E-E-A-T writing voice system, keyword funnel strategy, JSON-LD schema templates, comparison page SOP, IndexNow setup, Generative Engine Optimization content patterns. **Optimized for dev tools / OSS / B2B SaaS. 2C products (education, apps, games): see 2c-adaptation guide in references/.**

  🇨🇳 SEO & GEO 双引擎增长手册 —— 同时拿下 Google 排名和 AI 搜索引用（ChatGPT、Perplexity、Claude、文心一言）的完整方法论。AFFiNE 60k stars 与 150+ AI 创业公司咨询实战验证。E-E-A-T 写作声音系统、关键词漏斗、JSON-LD 结构化数据、竞品对比页 SOP、IndexNow 推送、生成式引擎优化内容模式。**默认适用于开发者工具 / 开源项目 / B2B SaaS，2C 产品（教育/应用/游戏）请参考 references/2c-adaptation.md。**

  🇯🇵 SEO & GEO デュアルエンジングロースプレイブック — Google検索とAI検索（ChatGPT、Perplexity、Claude）の両方で評価される手法。AFFiNE 60k starsと150社以上のAIスタートアップコンサルティングで検証。E-E-A-Tライティング、キーワードファネル、Schema.org構造化データ、比較ページSOP。**デフォルトは開発者ツール／OSS／B2B SaaS向け。2C製品（教育・アプリ・ゲーム）はreferences/2c-adaptation.mdを参照。**

  🇰🇷 SEO & GEO 듀얼 엔진 성장 플레이북 — 구글 검색과 AI 검색(ChatGPT, Perplexity, Claude) 양쪽 모두에서 인용되는 방법론. AFFiNE 60k 스타와 150+ AI 스타트업 컨설팅으로 검증. E-E-A-T 글쓰기, 키워드 퍼널, Schema.org 구조화 데이터, 비교 페이지 SOP. **기본값은 개발자 도구/OSS/B2B SaaS용. 2C 제품(교육·앱·게임)은 references/2c-adaptation.md 참조.**

  Triggers: "SEO" | "GEO" | "Generative Engine Optimization" | "AI search optimization" | "ChatGPT SEO" | "Perplexity SEO" | "Claude SEO" | "search optimization" | "content SEO" | "technical SEO" | "schema markup" | "JSON-LD" | "structured data" | "IndexNow" | "E-E-A-T" | "keyword strategy" | "keyword funnel" | "comparison page" | "programmatic SEO" | "SaaS SEO" | "搜索优化" | "AI 搜索" | "内容 SEO" | "GEO 优化" | "生成式引擎优化"
when_to_use: |
  Use to rank on Google AND get cited by AI search (ChatGPT / Perplexity / Claude / Gemini):
  keyword funnel (volume 300-1000 / KD 5-35), JSON-LD schema, E-E-A-T content,
  comparison pages, IndexNow. Enforces 2026-06-24 execution standards:
  internal links ≤2-3/para, cite competitor blogs as external links, title contains
  best/free/top/guide+year, breadcrumb schema, Bing IndexNow for GEO indexing.
---

## ⚠️ 使用前：确认你的产品类型

本 skill 默认场景：**开发者工具 / 开源项目 / B2B SaaS 出海**

如果你的产品是 **2C 消费品 / 教育 / 应用 / 游戏**，以下参数需要调整：

| 参数 | 默认值（B2B/开源）| 2C 建议值 |
|------|------|------|
| 关键词 volume 下限 | 300 | 50（长尾高转化词量少但值得做）|
| E-E-A-T 要求 | 创始人真实声音 | YMYL 品类（教育/医疗/金融）需可验证资质 + 方法论透明页 |
| 启动渠道 | PH / GitHub / HN | Reddit 垂类社区 / 小红书 / TikTok / 知乎 / Quora |
| 程序化页面风险 | 低 | 需"每页独有价值"，防 doorway page penalty |
| 关键词策略 | 单轨 BOFU + 长尾 | 加"时间窗口红利词"（如"2026 新规/改革/新题型"）|
| 外链获取渠道 | 技术媒体 / dev blog | 行业媒体 / 学校机构 / 垂直 KOL |

详细 2C 使用指南见 → [`references/2c-adaptation.md`](references/2c-adaptation.md)

---

# SEO & GEO 双引擎增长手册

> Language / 语言: [中文](#中文版) | [English](#english)

---

## 中文版

> 作者：Iris (生姜iris) | 版本：v1.0 (2026年4月)

### 核心理念

SEO 和 GEO 不是两件事，是一件事的两面。结构化数据同时服务传统搜索和 AI 搜索。

**传统 SEO 解决「被搜到」，GEO 解决「被 AI 引用」。**

2026 年的搜索流量已经分裂为两个入口：Google/Bing 的传统排名，和 ChatGPT/Perplexity/Claude 的 AI 回答。你的内容必须同时在两个战场上赢。

### SEO + GEO 双引擎对比

| 维度 | SEO（传统搜索） | GEO（AI 搜索） |
|------|----------------|----------------|
| 目标 | Google/Bing 排名 | AI 回答中被引用 |
| 核心信号 | 反向链接 + 关键词匹配 | 结构化数据 + E-E-A-T 真实性 |
| 内容格式 | H2/H3 层级 + 长尾词覆盖 | 直接回答 + 对比表格 + FAQ Schema |
| 技术手段 | XML Sitemap + Core Web Vitals | IndexNow + robots.txt 开放 AI 爬虫 |
| 衡量方式 | GA4 自然流量 + Ahrefs 排名 | 手动检查 AI 引用频率 |

### 五个核心原则（2026-06-24 执行标准）

1. **从 BOFU 往上做** — 先做高意向关键词（定价、对比），再做教育型内容。转化率最高的词优先。
2. **真实声音是最好的 E-E-A-T** — 不要让 AI 写得像 AI。用创始人声音、真实数字、亲历故事建立可信度。
3. **结构化 = 可引用** — Key Stats 表格、FAQ Schema、对比矩阵让 AI 引擎直接抓取引用。
4. **IndexNow 是 GEO 的基础设施** — 内容更新后秒级推送到 Bing/AI 搜索，不等爬虫。
5. **对比页是 SEO 金矿** — 每个竞品一个独立页面，截获决策期用户。

### 关键词选择标准（Ahrefs 筛选规则）

| 参数 | 标准 | 说明 |
|------|------|------|
| Volume | **300–1,000/月** | 新站专打此区间；大词竞争太激烈 |
| Keyword Difficulty | **KD 5–35** | KD > 35 = 新站短期内无法排进首页 |
| Traffic Potential | **300+** | 看该词落地页的整体流量潜力，不只看单词 |
| Search Intent | **第一要务** | 写前先看该词 Google top-10（忽略 Sponsored）判意图（step-by-step 指南 vs 列表/gallery），内容必须对齐意图 |
| 竞品新词 | **优先挖** | 扒竞品 blog 最新文，找还没被 Google 爬到的新词 |

### 页面优化执行标准

| 规则 | 标准 | 原因 |
|------|------|------|
| **内链密度** | **每段 ≤ 2-3 个** | 多了 Google 判 spam → 降 ranking |
| **外链策略** | **主动 cite 竞品 blog** | Google 视为客观 → 提信用分 → 提 ranking |
| **标题套路** | **best / free / top / guide + 年份** | CTR 提升最显著的公式 |
| **Meta description** | **关键词 rephrase**（如 "figma alternative" → "the alternative to Figma"）| 提点击率 |
| **面包屑导航** | **BreadcrumbList schema + 可见** | 结构信号 + SERP 富结果提 CTR |
| **Freshness** | **标注最后更新日期** | freshness 信号提排名 |
| **URL 结构** | **短 + 含词 + 带尾斜杠** | 可读 + 语义信号 |

### 外链建设标准

- **付费外链**：reach out 评测站（Product Hunt 等），**$20–30 可换 20–30 条高质量外链**，显著提 ranking
- **论坛外链**：量大但质低，有 penalty 风险——**不做 BacklinkBeam 那类操作**
- **正确路线**：HARO/Qwoted + 数据故事 press release = 高质量外链

### GEO 执行标准

- **Bing IndexNow**：内容更新后立即推送（不只是 Google）——让大模型更快 discover/index
- **AI 友好格式**：一句话答 + 表格 + FAQ Schema（FAQPage JSON-LD 5–8题）
- **GA4 监控**：配置 AI 来源 channel grouping（ChatGPT/Perplexity/Claude referral 单独追踪）

### 详细指南

| 主题 | 文件 | 说明 |
|:---|:---|:---|
| 关键词漏斗策略 | [references/keyword-strategy.md](references/keyword-strategy.md) | TOFU/MOFU/BOFU 关键词矩阵与优先级 |
| SEO 技术基础 | [references/seo-foundations.md](references/seo-foundations.md) | 核心页面优化、Schema、站点架构 |
| GEO 优化实操 | [references/geo-optimization.md](references/geo-optimization.md) | IndexNow、AI 爬虫、引用优化 |
| 内容生产 SOP | [references/content-sop.md](references/content-sop.md) | 从选题到发布的完整流程 |
| E-E-A-T 写作声音 | [references/writing-voice.md](references/writing-voice.md) | 创始人声音系统，提升真实性信号 |
| 竞品对比页 SOP | [references/comparison-pages.md](references/comparison-pages.md) | 页面结构、Schema、关键词嵌入 |

---

## English

> Author: Iris (生姜iris) | Version: v1.0 (April 2026)

### Core Philosophy

SEO and GEO are not two separate things — they're two sides of the same coin. Structured data serves both traditional search and AI search simultaneously.

**Traditional SEO solves "being found." GEO solves "being cited by AI."**

In 2026, search traffic splits into two entry points: Google/Bing rankings, and AI answers from ChatGPT/Perplexity/Claude. Your content must win on both battlefields.

### SEO + GEO Dual-Engine Comparison

| Dimension | SEO (Traditional Search) | GEO (AI Search) |
|-----------|-------------------------|-----------------|
| Goal | Google/Bing rankings | Cited in AI answers |
| Core Signal | Backlinks + keyword match | Structured data + E-E-A-T authenticity |
| Content Format | H2/H3 hierarchy + long-tail coverage | Direct answers + comparison tables + FAQ Schema |
| Technical | XML Sitemap + Core Web Vitals | IndexNow + robots.txt allowing AI crawlers |
| Measurement | GA4 organic traffic + Ahrefs rankings | Manual check of AI citation frequency |

### Keyword Selection Standards (2026-06-24)

| Parameter | Standard | Why |
|-----------|----------|-----|
| Volume | **300–1,000/month** | New sites only fight in this range; high-volume terms are too competitive |
| Keyword Difficulty | **KD 5–35** | KD > 35 = new sites can't reach page 1 short-term |
| Traffic Potential | **300+** | Evaluate the full page traffic potential, not just the single keyword |
| Search Intent | **#1 priority** | Before writing, check Google top-10 for the term (ignore Sponsored). Identify intent (step-by-step guide vs list/gallery). Content MUST align with intent — this is the #1 ranking factor |
| Competitor new words | **Mine first** | Scrape competitor blog's latest posts for terms Google hasn't indexed yet |

### Page Optimization Standards

| Rule | Standard | Reason |
|------|----------|--------|
| **Internal link density** | **≤ 2–3 per paragraph** | More = Google spam signal → ranking drop |
| **External link strategy** | **Actively cite competitor blogs** | Google reads as objective → trust score up → ranking up |
| **Title formula** | **best / free / top / guide + year** | Highest CTR lift formula |
| **Meta description** | **Keyword rephrase** (e.g. "figma alternative" → "the alternative to Figma") | CTR boost |
| **Breadcrumb nav** | **BreadcrumbList schema + visible** | Structure signal + SERP rich result → CTR |
| **Freshness** | **Show last-updated date** | Freshness signal improves ranking |
| **URL structure** | **Short + keyword-rich + trailing slash** | Readability + semantic signal |

### Backlink Standards

- **Paid outreach**: Reach out to review sites (Product Hunt etc.), **$20–30 buys 20–30 quality backlinks** — significant ranking uplift
- **Forum backlinks**: Volume but low quality, penalty risk — **avoid BacklinkBeam-style mass links**
- **Right approach**: HARO/Qwoted + data-driven press stories = quality backlinks

### GEO Execution Standards

- **Bing IndexNow**: Push immediately after every content update (not just Google) — helps LLMs discover/index faster
- **AI-friendly format**: One-sentence answer + table + FAQ Schema (FAQPage JSON-LD, 5–8 Q&As)
- **GA4 monitoring**: Configure AI source channel grouping (isolate ChatGPT/Perplexity/Claude referral traffic)

### Five Core Principles

1. **Start from BOFU, work upward** — High-intent keywords first (pricing, comparisons), then educational content. Highest-converting terms get priority.
2. **Authentic voice is the best E-E-A-T** — Don't let AI write like AI. Use founder voice, real numbers, first-hand stories to build credibility.
3. **Structured = Citable** — Key Stats tables, FAQ Schema, comparison matrices let AI engines directly extract and cite.
4. **IndexNow is GEO infrastructure** — Push content updates to Bing/AI search in seconds, don't wait for crawlers.
5. **Comparison pages are SEO gold mines** — One dedicated page per competitor, capturing decision-stage users.

### Detailed Guides

| Topic | File | Description |
|:---|:---|:---|
| Keyword Funnel Strategy | [references/en/keyword-strategy.md](references/en/keyword-strategy.md) | TOFU/MOFU/BOFU keyword matrix & prioritization |
| SEO Technical Foundations | [references/en/seo-foundations.md](references/en/seo-foundations.md) | Core page optimization, Schema, site architecture |
| GEO Optimization | [references/en/geo-optimization.md](references/en/geo-optimization.md) | IndexNow, AI crawlers, citation optimization |
| Content Production SOP | [references/en/content-sop.md](references/en/content-sop.md) | End-to-end workflow from topic selection to publishing |
| E-E-A-T Writing Voice | [references/en/writing-voice.md](references/en/writing-voice.md) | Founder voice system for authenticity signals |
| Comparison Page SOP | [references/en/comparison-pages.md](references/en/comparison-pages.md) | Page structure, Schema, keyword embedding |

---

## Key Results (Battle-Tested)

| Metric | Result |
|:---|:---|
| AFFiNE GitHub stars | 60,000+ (among fastest open-source projects to 10k pre-ChatGPT era) |
| GitHub Trending appearances | 28 times (Aug-Dec 2022) |
| Product Hunt #1 launches coached | 30+ |
| AI startups consulted | 150+ |
| Content cadence proven effective | 4 articles/week, KD 5–35 long-tail keywords |

---

## Platform Description

**EN:** SEO & GEO Dual-Engine Playbook 2026 — Rank on Google AND get cited by AI search (ChatGPT, Perplexity, Claude, Gemini). Enforces 2026-06-24 execution standards: Ahrefs keyword filter (volume 300–1,000 / KD 5–35 / traffic potential 300+), internal links ≤2–3 per paragraph, cite competitor blogs as external links, title formula best/free/top/guide+year, keyword rephrase in meta description, BreadcrumbList schema, $20–30 quality backlink outreach, Bing IndexNow for GEO, AI-friendly format (1-sentence answer + table + FAQ), GA4 AI traffic tracking.

**ZH:** SEO & GEO 双引擎增长手册（2026-06-24 标准）—— 同时拿下 Google 排名和 AI 搜索引用。关键词筛选标准：volume 300–1,000 / KD 5–35 / traffic potential 300+。执行规则：内链每段 ≤2–3 个、主动 cite 竞品外链、标题含 best/free/top/guide+年份、meta description 关键词 rephrase、面包屑 BreadcrumbList schema、$20–30 高质量外链、Bing IndexNow 推送、AI 友好格式（一句话答+表格+FAQ）、GA4 AI 流量追踪。

**JA:** SEO & GEO デュアルエンジン成長プレイブック（2026-06-24基準）— Google検索とAI検索（ChatGPT、Perplexity、Claude）の両方を攻略。キーワード選定基準：volume 300–1,000 / KD 5–35 / traffic potential 300+。実行ルール：内部リンクは段落あたり≤2–3個、競合ブログへの外部リンク、タイトルにbest/free/top/guide+年、meta descriptionのキーワードrephrase、BreadcrumbListスキーマ、$20–30外部リンク獲得、Bing IndexNow、AI対応フォーマット（一文回答+表+FAQ）、GA4 AIトラフィック追跡。

**KO:** SEO & GEO 듀얼 엔진 성장 플레이북（2026-06-24 기준）— 구글과 AI 검색(ChatGPT, Perplexity, Claude) 양쪽 동시 공략. 기본값은 개발자 도구/OSS/B2B SaaS용. 2C 제품은 references/2c-adaptation.md 참조. 키워드 선정 기준: volume 300–1,000 / KD 5–35 / traffic potential 300+. 실행 규칙: 단락당 내부링크 ≤2–3개, 경쟁사 블로그 외부링크 인용, 제목에 best/free/top/guide+연도, meta description 키워드 rephrase, BreadcrumbList 스키마, $20–30 고품질 백링크, Bing IndexNow, AI 친화적 포맷(한 문장 답변+표+FAQ), GA4 AI 트래픽 추적.
