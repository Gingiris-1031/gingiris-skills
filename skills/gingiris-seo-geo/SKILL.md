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
  define the site's entity boundary and search ICP, build a Topic Map, assign each
  intent cluster to one Page Owner, validate page type against the live SERP, and
  improve discovery, clicks, task completion, conversion, and verifiable AI citations.
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
| 核心信号 | 需求匹配、可抓取、站内结构、内容与产品价值、外部信任 | 实体一致、可读取、可核验证据、明确表达与外部信任 |
| 内容格式 | 按 SERP 主意图选 Type / Format / Angle | 结论、步骤、表格、案例与来源，但不保证获得引用 |
| 技术手段 | XML Sitemap、canonical、hreflang、可访问性与页面体验 | 同一套可发现/可读取基建；IndexNow 仅对支持的引擎加速发现 |
| 衡量方式 | GSC 曝光、点击、CTR、排名 + 真实转化 | 可复核的品牌提及、精确引用 URL 与真实 referral |

### 五个核心原则（2026-06-24 执行标准）

1. **从 BOFU 往上做** — 先做高意向关键词（定价、对比），再做教育型内容。转化率最高的词优先。
2. **真实声音是最好的 E-E-A-T** — 不要让 AI 写得像 AI。用创始人声音、真实数字、亲历故事建立可信度。
3. **先定 Entity 和 Page Owner** — 网站说清自己是什么、服务谁、不覆盖什么；每个主要意图词簇只有一个主承接页。
4. **SERP 决定页面形态** — 写作前检查当前目标市场 Top 10/20 的 Type、Format、Angle 和 URL 重合，不凭直觉新建页。
5. **从收录一直验收到任务完成** — 排名不是终点；要跟踪点击、页面内任务完成、CTA 与真实转化。GEO 另记录可复核引用，不从回答出现推断引用。

### 关键词选择起点（不是通用硬阈值）

Volume / KD / Traffic Potential 只是工具估算和优先级辅助。先确定产品定位与必须存在的页面，再对排名获客型词簇评分；高业务价值的低量词不应被机械过滤。

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
| **内链** | 优先连向相关 Page Owner / Money Page，anchor 描述目标任务 | 按用户路径和信息层级判断，不设“每段几个”的虚假硬阈值 |
| **外部来源** | 引用与论点直接相关的一手/权威来源 | 竞品博客可作产品自述，但不存在“引竞品就提排名”的通用规则 |
| **Title / Meta** | 对齐真实意图、价值和 SERP angle | 只有内容真实符合时才用 best/free/year；不把公式当默认答案 |
| **面包屑导航** | 站点层级需要时提供可见面包屑 + 匹配的 BreadcrumbList | 帮助导航和理解结构，不保证富结果或 CTR 提升 |
| **Freshness** | 只在有实质更新时改日期，并说明改了什么 | 不为制造新鲜度而翻日期 |
| **URL 结构** | **短 + 含词 + 带尾斜杠** | 可读 + 语义信号 |

### 外链建设标准

- **目录/评测站 listing 提交**：向评测/目录站提交 listing（提交费 $20–30/批），获取自然收录外链——**不是购买 dofollow 链接**（买链见 gr-backlinks 反模式：数天内被 Google 标记）
- **论坛外链**：量大但质低，有 penalty 风险——**不做 BacklinkBeam 那类操作**
- **正确路线**：HARO/Qwoted + 数据故事 press release = 高质量外链

### 历史案例：AFFiNE 零投放 SEO 战役（2022 末–2023，成熟站打法）

> ⚠️ **口径注意**：本案例的选词参数（KD 30–50 / 搜索量 ≈1,000）是 AFFiNE 2022–2023 时期的打法——当时站点已有 1 万+ star 带来的域名权重和全职内容团队。**新站请沿用上文 2026 标准（volume 300–1,000 / KD 5–35），本案例仅作历史参照，不替代现行标准。** 以下数字为播客口述（self-reported），用 ≈ 标注。

**完整 SOP（2023 年 2 月起执行，零 paid marketing）：**

1. **基建先行**：当时团队使用 SEO 评分工具作为发布前清单，将 ≥90 分作为内部目标；这不是 Google 官方排名门槛。
2. **选词**：用 Ahrefs/Semrush 反查竞品词库，选长尾词（当期参数 KD 30–50 / 搜索量 ≈1,000，见上方口径注意）。
3. **写前 SERP 调研**：研究当时首页的意图、页面形态和缺口，再用更新数据、第一方经验、实际截图/动图和产品结果提供信息增量；不复制竞品结构或文案。
4. **质量标准**：当时团队常用 ≈1,500 词、图文/动图/表格作为生产参考；现在应以用户任务是否完成和转化事件为准，不宣称字数、跳出率或驻留时长是可控排名公式。
5. **外链互换**：早期没名气就在出海社群互换 backlink，或发邮件给月曝光几十万级（非头部）的站点谈交换。
6. **关键词矩阵内链**：过往 SEO 文章互相引用（遵守上文内链密度 ≤2–3/段标准）。
7. **年度维护**：高排名文章每年更新一遍产品图和竞品截图（2022 写的 2023 更新、2024 再更新）；素材库（最新 user case + 竞品最新截图）全员共同维护。
8. **产能**：一周 4 篇、一月 ≈20 篇。"SEO 是个很苦的活，但只要有耐心就可以出结果。"

**结果（self-reported）**：开始做 SEO 后 3 个月流量 ≈25 倍；月 ≈40–50 万稳定曝光全部来自 SEO，零投放。

**复利案例**："open source notion alternative" 一词投入最大精力写透，稳居 Google 前三/前四；Notion 宣布封禁俄罗斯账号时该词搜索暴增，单篇旧文自动承接了一波俄罗斯用户——高权重文章会在突发事件时免费接住流量，这就是 SEO 复利。

### GEO 执行标准

- **证据层优先**：每个核心结论配可核验的一手来源、完整数据口径、实际操作或明确限制。所谓“43% 证据层”仅是内部编辑检查权重，不是已知的 AI 排名/引用算法权重。**绝不编造数据/引用**，查不到标 `[建议补充]`。详见 [references/geo-evidence-standard.md](references/geo-evidence-standard.md)
- **IndexNow**：对已发布或实质更新的 canonical URL 提交一次，加速支持该协议的引擎发现；它不是 Google Request Indexing，不保证收录或 AI 引用。
- **AI 友好表达**：直接结论 + 实操步骤 + 可核验表格/案例 + 一手来源。只在页面确有可见 FAQ 且标记与可见内容一致时使用 FAQPage。
- **GA4 监控**：配置 AI 来源 channel grouping（ChatGPT/Perplexity/Claude referral 单独追踪）

### 详细指南

| 主题 | 文件 | 说明 |
|:---|:---|:---|
| 关键词漏斗策略 | [references/keyword-strategy.md](references/keyword-strategy.md) | TOFU/MOFU/BOFU 关键词矩阵与优先级 |
| **Topic Map 与 Page Owner** | [references/topic-map-page-owner.md](references/topic-map-page-owner.md) | Entity、搜索 ICP、词簇、SERP 验证、页面任务与目录级复盘 |
| SEO 技术基础 | [references/seo-foundations.md](references/seo-foundations.md) | 核心页面优化、Schema、站点架构 |
| GEO 优化实操 | [references/geo-optimization.md](references/geo-optimization.md) | IndexNow、AI 爬虫、引用优化 |
| **GEO 证据层标准** | [references/geo-evidence-standard.md](references/geo-evidence-standard.md) | 内部编辑评分 + 证据纪律 + 一手论文引用库 |
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
| Core signals | Intent fit, crawlability, site structure, useful product/content, external trust | Consistent entities, readable text, verifiable evidence, clear expression, external trust |
| Content format | Match current SERP type, format, and angle | Clear conclusions, steps, tables, cases, and sources; none guarantees citation |
| Technical | Sitemap, canonical, hreflang, accessibility, and page experience | The same discoverability/readability foundation; IndexNow only accelerates discovery for participating engines |
| Measurement | GSC impressions, clicks, CTR, position, and real conversion | Reproducible brand mentions, exact cited URLs, and real referral traffic |

### Keyword Selection Starting Point (not a universal gate)

Volume, KD, and Traffic Potential are tool estimates. Establish positioning and must-have product pages first; then use these metrics to prioritize acquisition clusters. Do not mechanically discard a low-volume term with strong business value.

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
| **Internal links** | Prioritize relevant Page Owners and money pages; use descriptive anchors | Follow user paths and information hierarchy, not a made-up links-per-paragraph quota |
| **External sources** | Cite primary or authoritative sources that directly support the claim | Competitor blogs can support product self-claims, but citing them is not a general ranking boost |
| **Title / meta** | Match the real intent, value, and observed SERP angle | Use best/free/year only when true and useful, never as a default formula |
| **Breadcrumb nav** | Use visible breadcrumbs plus matching BreadcrumbList when the hierarchy needs them | Helps navigation and structure; does not guarantee a rich result or CTR lift |
| **Freshness** | Change the date only after a substantive update and describe what changed | Do not manufacture freshness |
| **URL structure** | **Short + keyword-rich + trailing slash** | Readability + semantic signal |

### Backlink Standards

- **Directory/review listing submissions**: Submit listings to review/directory sites ($20–30 submission fee per batch) to earn naturally indexed backlinks — **not buying dofollow links** (see gr-backlinks anti-pattern: purchased links get flagged by Google within days)
- **Forum backlinks**: Volume but low quality, penalty risk — **avoid BacklinkBeam-style mass links**
- **Right approach**: HARO/Qwoted + data-driven press stories = quality backlinks

### Historical Case: AFFiNE Zero-Budget SEO Campaign (late 2022-2023, established-site playbook)

> ⚠️ **Calibration note**: The keyword parameters in this case (KD 30-50 / volume ≈1,000) reflect AFFiNE's 2022-2023 playbook — the site already had domain authority from 10k+ GitHub stars and a full-time content team. **New sites must follow the 2026 standard above (volume 300-1,000 / KD 5-35); this case is historical reference only and does not replace the current standard.** Numbers below are self-reported from podcast interviews, marked with ≈.

**Full SOP (executed from Feb 2023, zero paid marketing):**

1. **Infrastructure first**: The team used a 90+ audit score as an internal release checklist. It was not a Google ranking threshold.
2. **Keyword selection**: Reverse-mine competitor keyword sets via Ahrefs/Semrush, pick long-tail terms (era parameters KD 30-50 / volume ≈1,000 — see calibration note above).
3. **Research the SERP before writing**: Study the dominant intent, page shape, and gaps. Add information gain with current data, first-hand experience, actual screenshots/GIFs, and product outcomes; do not copy competitor structure or prose.
4. **Quality bar**: The team often used ≈1,500 words plus visuals and tables as a production reference. Current work should instead pass task-completion and conversion checks; do not present word count, bounce rate, or dwell time as a controllable ranking formula.
5. **Backlink exchange**: With no brand yet, swap backlinks inside founder communities, or email non-head sites with hundreds of thousands of monthly impressions to negotiate exchanges.
6. **Keyword-matrix internal linking**: Cross-link all past SEO articles (within the ≤2-3 links/paragraph density standard above).
7. **Annual maintenance**: Refresh product and competitor screenshots in every high-ranking article each year (2022 articles updated in 2023, again in 2024); the whole team maintains a shared asset library of latest user cases and competitor screenshots.
8. **Cadence**: 4 articles/week, ≈20/month. "SEO is grueling work, but with patience it always pays off."

**Results (self-reported)**: traffic grew ≈25x within 3 months of starting SEO; ≈400-500k stable monthly impressions, all organic, zero paid spend.

**Compounding case**: The team poured maximum effort into one article for "open source notion alternative" and held Google positions 3-4 for it. When Notion announced its ban on Russian accounts, searches for that term spiked and the single old article automatically captured a wave of Russian users — high-authority articles catch event-driven traffic for free. That is SEO compounding.

### GEO Execution Standards

- **Evidence layer first**: Support core claims with a verifiable primary source, complete data provenance, actual operation, or explicit limitation. The "43% evidence layer" is an internal editorial heuristic, not a known AI ranking/citation algorithm weight. **Never fabricate data/citations**; flag unverifiable claims as `[needs-source]`. See [references/en/geo-evidence-standard.md](references/en/geo-evidence-standard.md)
- **IndexNow**: Submit a published or substantively updated canonical URL once to accelerate discovery by participating engines. It is not Google Request Indexing and does not guarantee indexing or AI citation.
- **AI-readable content**: Clear conclusion + executable steps + verifiable table/case + primary sources. Use FAQPage only when a visible FAQ exists and the markup exactly matches it.
- **GA4 monitoring**: Configure AI source channel grouping (isolate ChatGPT/Perplexity/Claude referral traffic)

### Five Core Principles

1. **Start from BOFU, work upward** — High-intent keywords first (pricing, comparisons), then educational content. Highest-converting terms get priority.
2. **Authentic voice is the best E-E-A-T** — Don't let AI write like AI. Use founder voice, real numbers, first-hand stories to build credibility.
3. **Define the entity and Page Owner first** — State what the site is, whom it serves, and what it excludes; give each major-intent cluster one primary canonical page.
4. **Let the SERP determine page shape** — Inspect the current target-market Top 10/20 for type, format, angle, and URL overlap before creating a page.
5. **Measure through task completion** — Ranking is not the endpoint. Track clicks, on-page task completion, CTA events, and real conversion. Measure GEO citations separately with reproducible evidence.

### Detailed Guides

| Topic | File | Description |
|:---|:---|:---|
| Keyword Funnel Strategy | [references/en/keyword-strategy.md](references/en/keyword-strategy.md) | TOFU/MOFU/BOFU keyword matrix & prioritization |
| **Topic Map & Page Ownership** | [references/topic-map-page-owner.md](references/topic-map-page-owner.md) | Entity, search ICP, intent clusters, SERP validation, page tasks, and directory-level review |
| SEO Technical Foundations | [references/en/seo-foundations.md](references/en/seo-foundations.md) | Core page optimization, Schema, site architecture |
| GEO Optimization | [references/en/geo-optimization.md](references/en/geo-optimization.md) | IndexNow, AI crawlers, citation optimization |
| **GEO Evidence-Layer Standard** | [references/en/geo-evidence-standard.md](references/en/geo-evidence-standard.md) | Internal editorial rubric + evidence discipline + primary-source citation library |
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
| AFFiNE SEO campaign 2022-2023 (self-reported) | Traffic ≈25x in 3 months; ≈400-500k monthly impressions, zero paid spend |
| Compounding keyword case | "open source notion alternative" held Google positions 3-4; auto-captured Russian user wave when Notion exited Russia |

---

## Platform Description

**EN:** SEO & GEO Dual-Engine Playbook 2026 — define the entity and search ICP, build a Topic Map, map each intent cluster to one Page Owner, validate the live SERP, improve discoverability and task completion, and measure Google results separately from verifiable AI citations.

**ZH:** SEO & GEO 双引擎增长手册：定义 Entity 与搜索 ICP，建立 Topic Map，将每个主意图词簇分配给唯一 Page Owner，用当前 SERP 确认页面形态，再独立跟踪 Google 曝光/点击/转化和可复核 AI 引用。

**JA:** SEO/GEO のために Entity と検索 ICP を定義し、Topic Map を作成、各検索意図クラスターに唯一の Page Owner を割り当てる。現在の SERP でページ形態を検証し、クリック・タスク完了・転換と、再現可能な AI 引用を別々に計測する。

**KO:** SEO/GEO를 위해 Entity와 검색 ICP를 정의하고 Topic Map을 만든 뒤, 각 주요 의도 클러스터에 하나의 Page Owner를 배정한다. 현재 SERP로 페이지 형태를 검증하고 클릭·과업 완료·전환과 재현 가능한 AI 인용을 별도로 측정한다.

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
