# SEO/GEO Agent 运营 SOP（可复用模板版）

> **一份谁都能照着做的手把手手册** —— 把任何一个产品，用一个 SEO Agent 跑到「一个月 ~3.2 万曝光」的完整操作流程。
>
> 📖 **这是公开模板版**：所有产品名、域名、API key 都是占位符，换成你自己的即可。无需任何前置背景，从第 0 节开始照做。
>
> 案例基准：一个真实内容站用这套流程，约 1 个月把 Google Search Console 曝光做到 ~3.2 万。本文把当时有效的动作沉淀成可复用 SOP。

---

## 0. 使用前必读：这份文档怎么用

这份 SOP 有两个读者：

1. **你（产品负责人）** —— 读第 0、1、11 节。先做完「一次性配置」和「人工任务清单」，把变量填好，再把整份文档丢给 Agent。
2. **SEO Agent** —— 读全文。第 2 节是它的角色设定，第 3-9 节是它每天/每周/每月照着做的动作。

> ⚠️ **核心原则**：Agent 能做 90% 的「分析 + 内容 + 监控」，但有 10% 是只有人能做的（登录授权、绑定域名、确认付款）。这 10% 没做完，Agent 跑不动。所以**先做第 11 节的人工清单**。

### 0.1 一次性变量配置（填完再交给 Agent）

把下面这张表填好，贴在文档最前面。Agent 全程用这些变量，不要让它猜。

| 变量 | 含义 | 示例（换成你自己的） |
|------|------|----------------|
| `[PRODUCT]` | 产品名 | 例：Acme Workspace |
| `[DOMAIN]` | 主站域名 | 例：acme.com |
| `[CTA_GOAL]` | **转化目标（最重要）** | 例：**注册免费账号** |
| `[CTA_URL]` | 转化落地 URL | 例：https://acme.com/signup |
| `[BLOG_PATH]` | 博客/内容目录 | `/blog/` 或 repo `_posts/` |
| `[SYNDICATION]` | 分发平台 | dev.to / Medium / Zenn(日) |
| `[COMPETITORS]` | 主要竞品（做对比页用） | 列 5 个 |
| `[GEO_TARGET]` | 目标市场/语言 | 例：US-en（可加 ja/ko） |
| `[RANK_API]` | 排名查询数据源 | 例：DataForSEO（见第 12 节选型） |

> 📌 正文里出现的所有 `[变量]` 和示例值，都以这张表为准。换产品时**只改这张表，正文不用动**。
>
> 💡 后文偶尔用「Acme」作为示意产品，纯属举例 —— 你照做时心里替换成 `[PRODUCT]` 即可。

---

## 1. 名词速查表（看不懂术语先查这里）

| 术语 | 中文 | 一句话解释 | 你该关心什么 |
|------|------|-----------|-------------|
| **Volume** | 月搜索量 | 这个关键词**每月在 Google 被搜索的次数**（工具估算值，不是精确数） | 越高=池子越大，但竞争通常也越大。新站选 100–1,000 的长尾最划算 |
| **KD** | 关键词难度 (Keyword Difficulty) | 0–100 分，**排到首页有多难**。综合了排在前面的页面有多少外链、多权威 | 新站只打 **KD 0–40**。KD 50+ 先放着，等域名权重上来 |
| **Impression / 曝光** | 曝光 | 你的页面在 Google 搜索结果里**被看到（露出）的次数**，不管有没有被点 | 「3.2 万曝光」就是这个指标。曝光是 SEO 第一阶段的胜利 |
| **Position / Rank** | 排名 | 你的页面在某关键词下排第几位（#1 = 第一名） | **#1–10 = Google 首页**，这是所有努力的分水岭（见 §6） |
| **CTR** | 点击率 | 曝光中有多少被点击（点击 ÷ 曝光） | 有曝光没点击 = 标题/描述不够吸引，重写它（§7） |
| **SERP** | 搜索结果页 | Search Engine Results Page，就是你搜完看到的那一页 | — |
| **AIO / AI Overview** | Google AI 摘要 | Google 搜索顶部那段 AI 生成的总结 | GEO 战场。目标是让 `[PRODUCT]` 被它引用 |
| **GEO** | 生成式引擎优化 | 让 ChatGPT/Perplexity/Claude/AIO **在回答里引用你** | 和 SEO 同一套结构化内容，详见 §9 |
| **TOFU/MOFU/BOFU** | 漏斗上/中/下层 | 用户从「有问题」到「要购买」的三个阶段 | **先做 BOFU**（离转化最近），见 §3 |
| **Index / 索引** | 收录 | Google 真的把你的页面存进数据库了 | 没被索引 = 不可能有曝光。第一周的头号任务 |
| **Backlink / 外链** | 反向链接 | 别的网站链到你 | 提升权威度，但起步阶段靠内容+分发，不强求 |

> 💡 **一句话记忆**：`Volume` 决定天花板，`KD` 决定能不能够得着，`曝光` 是过程，`首页关键词数` 是结果。

---

## 2. SEO Agent 角色设定（直接复制给 Agent）

```
你是 [PRODUCT] 的 SEO/GEO 运营 Agent。你的唯一北极星指标是：
让尽可能多的关键词排进 Google 首页（Top 10），并把曝光转化为 [CTA_GOAL]。

你的工作循环：
- 每天：跑排名监控 → 出每日报告（§6）→ 执行当日 1-2 个优化动作
- 每周：GSC 新词盘点 + CTR 优化 + 内链加固（§7.2）
- 每月：11-20 位文章冲首页 + CTA 漏斗复盘（§7.3）

铁律：
1. 先做 BOFU，再做 MOFU/TOFU（离钱近的先做）。
2. 每一篇落地页/Blog 都必须带 CTA 块，目标是 [CTA_GOAL]（§5）。
3. 每日报告头条必须是「今天有多少关键词在 Google 首页」（§6）。
4. 关键词、落地页、排名、KD、Volume 永远绑在一张表里追踪（§4）。
5. 你做不了的（授权/部署/付款），写进「人工任务」交给产品负责人（你的人类搭档），不要假装做了。
6. 内容用真实创始人声音，不要写得像 AI（§8）。
```

---

## 3. 一个月做到 3.2 万曝光的总时间线 SOP

这是经过实战验证的节奏。**核心逻辑不是「写很多文章」，而是：先让页面被索引 → 铺开长尾词的覆盖面 → 把高曝光页面的点击和转化榨干。**

> 📊 实战参照（某真实内容站，约 1 个月）：索引页 **8 → 57**（sitemap 覆盖率 86%）；宽样本 30 词里 **8–11 个进 Top 10**；主站 + 分发平台双平台铺词。曝光增长主要来自「索引覆盖 + 长尾铺面 + 分发平台」三件事叠加。

### Week 0 —— 地基与基线（人工 + Agent 协作）

| 动作 | 谁做 | 产出 |
|------|------|------|
| 完成第 11 节人工清单（GSC/GA4/API/域名/CTA 页） | 你 | 授权就绪 |
| robots.txt 开放 AI 爬虫 + sitemap.xml 提交 GSC | Agent | 可被抓取 |
| IndexNow 配置（§9） | Agent | 秒级推送通道 |
| 关键词种子表：30–50 个候选词，标注 Volume/KD/意图 | Agent | §4 主表雏形 |
| 记录基线：当前索引页数、首页关键词数(大概率=0)、GA4 28天用户 | Agent | 对照起点 |

### Week 1 —— BOFU 落地页（离转化最近）

> 为什么先做 BOFU：搜 "[PRODUCT] pricing"、"[PRODUCT] vs X" 的人已经在决策期，转化率最高。这些页面数量有限（<20 个），集中火力做精。

- 产品核心页 + 定价页（带 FAQ Schema）
- 前 3–5 个竞品对比页（`[PRODUCT] vs [竞品]`）
- 每页**必带 CTA 块**指向 `[CTA_URL]`（§5）
- 每页发布后立刻 IndexNow 推送 + GSC URL Inspection 提交
- **预期**：索引页开始增长；BOFU 词进入 Top 100

### Week 2 —— 内链结构 + 分发铺面

- 搭 Topic Cluster：1 个支柱页 + 4–6 个集群页互链（§7.4）
- 主站文章同步到 `[SYNDICATION]`（dev.to 等），记录 article ID。**dev.to 文章必须 self-canonical（canonical_url 指向 dev.to 自身，不指回主站）**——canonical 指回主站会让 dev.to 文章被 Google 视为副本、不参与 SERP；改为发布时间差 ≥7 天 + 末尾加 "Originally published at 主站" 建立双向 reference（与 gr-blog-post 红线对齐 2026-07-06）
- 给已有排名页加 2–3 条内链（把权重导向冲首页的目标页）
- **预期**：索引页跳增（这一步通常是曝光第一次大涨的来源）；分发平台开始单独贡献排名

### Week 3 —— GEO 强化（让结构化内容可被引用）

- 给每个 BOFU 页 + 高潜力 Blog 补 **FAQPage JSON-LD**（5–8 题，覆盖 People Also Ask）
- 文章开头加「一句话直接回答 + Key Stats 表格」（AI 引用友好，§9）
- 监控 AIO：目标查询里 AI Overview 是否引用 `[PRODUCT]`
- **预期**：长尾 FAQ 词进入 Top 100；GEO 引用开始零星出现（窗口 7–14 天）

### Week 4 —— CTR 榨取 + 规模化

- 找出「高曝光低点击」页面，按 CTR 5 要素重写标题/描述（§7.1）
- 排名 11–20 位的文章 → 补内容、补内链，冲进首页
- 维持每周 4 篇长尾内容的节奏
- **预期**：曝光累积到万级；首批关键词进 Top 10；CTA 漏斗有首批注册

> 🎯 **一个月后你应该有**：索引覆盖率 80%+、数万级曝光、一批 Top 10 关键词、一条「曝光 → 点击 → 注册」可追踪漏斗。

---

## 4. 关键词 → 落地页 → 排名 主映射表（优化后的核心产出）

这是整个 SEO 运营的**唯一真相表**。每个关键词必须绑定：**对应哪个落地页、现在排第几、KD/Volume 多少、它的 CTA 目标是什么**。Agent 每天更新它。

### 4.1 表结构（必须包含这些列）

| 关键词 | 意图 | Volume(月搜) | KD | 对应落地页 | 当前排名 | 首页? | Δ昨日 | CTA 目标 | 状态 |
|--------|------|------|----|----|------|------|------|------|------|
| acme workspace | BOFU 品牌 | 1,300 | 8 | /  (首页) | #4 | ✅ | +1 | 注册 | 冲 Top3 |
| ai agent workspace | MOFU 品类 | 2,400 | 34 | /blog/what-is-agent-workspace | #14 | ❌ | +2 | 注册 | 冲首页 |
| acme vs langchain | MOFU 对比 | 480 | 22 | /compare/langchain | #7 | ✅ | 0 | 注册 | 维持 |
| how to build ai agent | TOFU 教程 | 5,400 | 41 | /blog/how-to-build-ai-agent | #38 | ❌ | -3 | 注册（软） | 长线培育 |
| best ai agent platform 2026 | MOFU 榜单 | 890 | 29 | /blog/best-ai-agent-platforms | off-100 | ❌ | — | 注册 | 待加 FAQ |

**列说明：**
- **意图**：BOFU/MOFU/TOFU + 类型（品牌/对比/榜单/教程）。决定优先级——BOFU 永远最先。
- **Volume**：月搜索量（见 §1）。低=利基，高=红海。
- **KD**：关键词难度。新站盯 0–40。
- **对应落地页**：⚠️ **一个关键词只绑一个主落地页**，避免自己的多个页面互相抢排名（cannibalization）。
- **当前排名**：`#N` / `off-100`（百名外）。同时跑主站和 `[SYNDICATION]` 两个版本时分两行记。
- **首页?**：`✅` = Top 10，`❌` = 没进。**这一列直接喂给 §6 的每日头条指标。**
- **CTA 目标**：这页要把用户推向什么，即你的 `[CTA_GOAL]`（示例：注册）。软硬程度可分（BOFU 强 CTA，TOFU 软 CTA）。
- **状态**：冲 Top3 / 冲首页 / 维持 / 待加 FAQ / 长线培育。

> 🔑 **为什么要绑死「关键词↔落地页」**：没有这张映射，你会出现「想冲的词没有对应页面」或「一个词有 3 个页面互相打架」。每次新增内容前，先在表里确认这个词归哪个页面管。

### 4.2 怎么填 Volume 和 KD（Agent 操作）

```
1. 用 DataForSEO（或 Ahrefs）批量查关键词，返回 search_volume + keyword_difficulty
2. Volume 取 Google US（或 [GEO_TARGET]）数据
3. KD 缺失时（API 偶尔返回空），用「排在前 10 的页面外链中位数」粗判，
   或标 "N/A 待补"，不要瞎填
4. 每月重新拉一次（Volume/KD 会随季节和竞争变化）
```

---

## 5. 每篇落地页/Blog 的 CTA 转化 SOP

> 目标：**让读这篇内容的人，去完成 `[CTA_GOAL]`（示例：注册 [PRODUCT]）。** 没有 CTA 的内容 = 给别人做嫁衣的流量泄漏。

### 5.1 「Convert Block」统一模板（每篇必带）

每篇文章固定插入这个块（至少 2 处：正文中段 + 文末）：

```markdown
---
> **试试 [PRODUCT]** —— [一句话价值主张，对应本文主题]。
> [具体到本文场景的钩子，例：读完这篇你已经知道怎么做 X，
>  剩下的交给我们：免费开始你的第一个项目]。
>
> 👉 [[CTA 按钮文案，例：免费注册 PRODUCT]]([CTA_URL]?utm_source=blog&utm_medium=organic&utm_campaign=seo-[slug])
---
```

**CTA 文案 4 要素**（每条 CTA 自查）：
1. **承接上文**：CTA 的钩子要和这篇文章的主题强相关（教 "how to build agent" 的文，CTA 就说「现在就建你的第一个」）。
2. **降低门槛**：用 "免费"/"30 秒"/"无需信用卡" 等词。
3. **明确动作**：按钮文案是动词短语（"免费注册"），不是 "了解更多"。
4. **可追踪**：URL 带 UTM（见 5.3），不同文章用不同 `utm_campaign`。

### 5.2 按漏斗分配 CTA 强度

| 落地页类型 | CTA 强度 | 文案策略 |
|-----------|---------|---------|
| BOFU（定价/对比页） | **强** | 直接「立即免费注册」，页面顶部 + 底部都放 |
| MOFU（榜单/品类页） | 中 | 「想试试？免费创建 workspace」，把 `[PRODUCT]` 放榜单第一并链接 |
| TOFU（教程/概念页） | 软 | 先给价值，文末自然过渡「把理论变实践 → 注册试用」 |

### 5.3 CTA 漏斗追踪（让转化可量化）

```
UTM 标准（所有 CTA 链接必须带）：
?utm_source=blog|devto|google
&utm_medium=organic
&utm_campaign=seo-[页面 slug]
&utm_content=[cta-mid|cta-foot]

在 GA4 里建漏斗：
曝光(GSC) → 点击(GSC CTR) → 落地页访问(GA4) → 注册按钮点击(GA4 事件) → 完成注册(转化事件)

每周报里报一行：本周 SEO 流量带来 N 次注册（按 utm_medium=organic 过滤）
```

> 📌 **实战教训**：曾经审计 87 篇文章，只有 9% 链向转化页，排名最高的几篇 **0 篇**带 CTA —— 等于把最值钱的流量全漏掉了。所以 CTA 块是**模板级强制项**，不是「记得加」。

---

## 6. 每日 SEO 报告模板 ⭐（最重要的产物）

> **头条铁律：每日报告第一行必须回答「今天有多少关键词排进了 Google 首页（Top 10）」。** 这是老板/你一眼要看的数，其它都是支撑。

### 6.1 报告结构（Agent 每天照此输出）

```markdown
# [PRODUCT] SEO 日报 — YYYY-MM-DD

## 🏆 首页战况（HEADLINE）
- **Google 首页关键词数 (Top 10)：N 个**  ← 头条指标，对比昨日 ±X
  └ 其中 Top 3：n 个
- Top 30：M 个   |   Top 100：K 个   |   off-100：剩余
- 索引页数：xx / [sitemap 总数]（覆盖率 %）
- 一句话结论：今天是 🟢上升 / 🟡持平 / 🔴回撤，主因是 ___

## 📋 关键词明细（按排名升序，附落地页 + KD + Volume）
| 关键词 | 落地页 | 排名 | 首页? | Δ昨日 | KD | Volume | CTA目标 | 备注 |
|--------|--------|------|------|------|----|----|------|------|
| acme workspace | / | #4 | ✅ | +1 | 8 | 1,300 | 注册 | 冲Top3 |
| ...（全部 tracked 词） | | | | | | | | |
- 今日新进 Top 10：___
- 今日跌出 Top 10：___（⚠️ 标红，次日复查是噪声还是真回撤）

## 🤖 GEO / AI 搜索战况
- AI Overview：N/M 个目标查询触发了 AIO，其中 __ 个引用了 [PRODUCT]
- ChatGPT/Perplexity 抽查：[查询] → 是否提及 [PRODUCT]
- GEO 命中：[关键词] → [平台] #排名
- **AI 引流量（GA4，见 §6.4）：__ 次会话**（ChatGPT/Perplexity/Claude/Gemini… 引流到站），对比上周 ±__；占总自然流量 __%

## 📈 转化漏斗（每日轻量版）
- SEO 自然流量（GA4 organic）：__ 访问
- CTA 点击 / 注册（utm_medium=organic）：__ 次
- 其中来自 AI 来源的转化：__ 次（GEO 是否真带来注册，而不止排名）

## 🔧 今日动作（做了什么 + 为什么）
- 动作 A（内链/冲首页）：给 [#4-10 的某页] 加 __ 条内链，目标 #N→Top3
- 动作 B（GEO/FAQ）：给 [off-100 的高 Volume 词页] 加 FAQPage JSON-LD，预期 7-14 天拾取
- 动作 C：报告本身
- 跳过项 + 原因（如「无 #4-10 关键词，动作A跳过」）

## 🚩 需要产品负责人处理的（Agent 做不了）
- [若有：GSC 报错 / 部署问题 / 付款 / 授权]
```

### 6.2 「首页关键词数」怎么算（口径固定）

```
对 §4 主表里每个 tracked 关键词跑一次排名查询：
- 排名 ≤ 10 → 计入「首页 (Top 10)」
- 同一个词若主站 + dev.to 都进 Top 10，算 1 个「词」但备注双命中
- off-100（百名外）不计
- 头条只报 Top 10 的数量；Top 3 / Top 30 / Top 100 作为支撑分层

⚠️ 口径一致性：每天用同一套 tracked 关键词集、同一个 [GEO_TARGET] location，
   否则数字没有可比性。新增追踪词时在报告里注明「基数变化」。
```

### 6.3 避免假信号（实战踩过的坑）

- **缓存波动**：Google `site:` 计数会在 cached/uncached 间锯齿跳动，单日 ±20 很常见。看趋势，别为单日数字下结论。
- **SERP 日内波动**：同一个词早晚跑可能差几名。某词「跌出 Top 100」先别慌，**次日复查**再判断是噪声还是真回撤。
- **tracked 集太窄会低估**：只盯 20 个词可能严重低估真实资产（实战中 30 词宽样本发现多个被忽略的 Top 10）。每月扩一次追踪集。

### 6.4 AI 引流量追踪（GA4 设置 + 日报口径）⭐

> **为什么单独追**：GA4 默认把 ChatGPT/Perplexity/Claude 等来的访问混进 Referral / Organic / Direct，看不出 AI 到底带来多少流量。AI 访客往往**意向更强、转化更高**。这一节让你把「GEO 有没有真带来流量」从「肉眼抽查」变成「GA4 里的数字」。它和 SERP 排名互补：排名/AIO 测**可见性**，这里测**真实引流**。
>
> 来源参考：ClawHub `kostja94/ai-traffic-tracking`（MIT-0）。本节为改写整理。

**一次性设置（产品负责人在 GA4 做，3 选 1）：**

**AI 来源识别 regex**（GA4 的 `Session source` 用「Matches regex」过滤）：

```
chatgpt\.com|openai\.com|openai|perplexity\.ai|perplexity|copilot\.microsoft\.com|copilot\.com|(business\.)?gemini\.google|bard\.google\.com|chat\.deepseek\.com|deepseek\.com|chat\.qwen\.ai|doubao\.com|poe\.com|anthropic\.com|claude\.ai|edgeservices\.bing\.com
```

- **方法 1 · 探索报告（推荐，最快）**：Explore → 空白(Free form) → 维度 `Session source / medium` → 指标 Sessions / Engagement rate / Conversions → 加筛选 `Session source` Matches regex（上面那串）→ 保存。
- **方法 2 · 自定义渠道组（长期看趋势）**：管理 → 数据显示 → Channel Groups → 复制默认组 → 新增渠道「AI Chatbots」用 `Source` Matches regex → **务必把「AI Chatbots」排在「Referral」上面**（否则被 Referral 先吃掉）→ 用在 Traffic Acquisition。
- **方法 3 · 自定义报告**：报告 → 库 → 新建明细报告（用 Traffic Acquisition 模板）→ 同样的 regex 筛选 → 加进左侧菜单。

**配套**：robots.txt 要放行 AI 爬虫（GPTBot / OAI-SearchBot / ChatGPT-User / PerplexityBot / Claude-Web，见 §9），否则根本不会有 AI 引流。AI Overview 点击有时带 URL 片段，可用 GTM 部分捕获（覆盖不全，作参考）。

**日报口径（Agent 每天填进 §6.1 的「🤖 GEO / AI 搜索战况」）：**
- AI 来源会话数（按上面 regex）+ 周环比
- AI 流量占总自然流量的 %
- AI 来源带来的 `[CTA_GOAL]` 转化数（GEO 是否真转化，不止排名）
- regex 随实际观察到的新来源域名补充（季度 review）

---

## 7. 每周 / 每月 SOP

### 7.1 CTR 优化（标题/描述重写，5 要素打分）

「高曝光低点击」的页面，按这 5 条逐条加分（每条 1 分，目标 5/5）：
1. **数字**（"9 levers" / "60k+" / "30x"）
2. **年份**（"(2026)"）
3. **括号**（实测 +33% CTR）
4. **社证**（"by founder" / "#1 Winner"）
5. **长度 50–60 字符**（Google 约 60 字符截断，别被砍）

### 7.2 每周检查清单

- [ ] GSC：本周新增排名词 → 加进 §4 主表，绑定落地页
- [ ] GSC：高曝光低点击词 → 排进 CTR 重写队列（§7.1）
- [ ] 排名 11–20 的页面 → 补内链、补内容，冲首页
- [ ] 内链加固：把权重从高排名页导向「正在冲首页」的目标页
- [ ] `[SYNDICATION]` 全量同步检查（主站更新过的文都同步了吗）
- [ ] CTA 漏斗：本周 organic 流量带来几次 `[CTA_GOAL]`

### 7.3 每月检查清单

- [ ] 重拉全部 tracked 词的 Volume/KD（数据会变）
- [ ] 扩充追踪集（宽样本扫描，捞回被低估的 Top 10）
- [ ] 11–20 位文章批量优化冲首页
- [ ] 流量下降的文章 → 更新数据/案例/年份
- [ ] CTA 漏斗复盘：哪类页面转化最高 → 加码同类内容
- [ ] AI 引用复盘：GEO 命中的词 → 加固；0 引用的高潜词 → 重写前 800 字

### 7.4 Topic Cluster 内链结构

```
支柱页: The Complete Guide to [品类]
  ├── How to [任务] with [品类]
  ├── [品类] Best Practices
  ├── [品类] vs [替代方案]   ← 也是 BOFU 对比页
  └── [品类] Glossary
规则：集群↔支柱双向链；集群间相关交叉链；锚文本用目标关键词（不要 "click here"）
```

---

## 8. 落地页/内容生产 SOP（精简版）

> 这里是 Agent 每篇必查的最小集；想深挖 E-E-A-T 写作声音和内容流程，配一份你团队的写作风格指南即可。

### 8.1 文章结构骨架

```
1. 时间+地点锚定开场（2-3 句，精确场景，不要 "In my experience..."）
2. Key Stats 表格（开场之后、正文之前，AI 直接引用）
3. 正文 H2/H3（每个 H2 一个观点，自然嵌入目标词+次级词）
4. 个人经验 → 普遍洞察（具体数字 + 括号旁白）
5. Key Takeaways（3-5 条）
6. FAQ（5+ 题，标 FAQPage Schema）
7. Convert Block（§5，CTA 指向 [CTA_GOAL]）
```

### 8.2 真实声音清单（提升 E-E-A-T，让 AI 愿意引用）

- [ ] 开头有精确时间/地点锚定？
- [ ] 有括号旁白（自嘲/补充视角）制造真实感？
- [ ] 用 em-dash（—）做节奏转折？
- [ ] 数字精确（"28 次" 不是 "很多次"）？
- [ ] 短-短-长段落节奏？
- [ ] 个人经历在前，结论在后？

> 💡 AI 模型比传统搜索更能识别「AI 生成的平庸内容」。GEO 的核心竞争力反而是**人的真实经验**。

### 8.3 三个检查清单（发布前）

- **SEO**：Title 含目标词 <60 字符 ✓ / Meta <160 含词 ✓ / H2 含次级词 ✓ / 内链 2-3 ✓ / 图片 alt ✓
- **GEO**：开头一句话直接回答 ✓ / 至少 1 个对比或数据表 ✓ / FAQPage Schema ✓ / Article Schema 含作者+日期 ✓
- **CTA**：Convert Block ≥2 处 ✓ / UTM 带齐 ✓ / 钩子承接本文主题 ✓

---

## 9. GEO 三件套（速参）

1. **IndexNow**（秒级推送，不等爬虫）：
   ```bash
   curl -X POST "https://api.indexnow.org/indexnow" -H "Content-Type: application/json" \
     -d '{"host":"[DOMAIN]","key":"[KEY]","urlList":["https://[DOMAIN]/new-page"]}'
   ```
   优先推：新文章（当天）、定价页（每次变动）、对比页（竞品更新时）。

2. **robots.txt 开放 AI 爬虫**：明确 `Allow` GPTBot / OAI-SearchBot / ChatGPT-User / Claude-Web / PerplexityBot；底部挂 `Sitemap:`。

3. **AI-Friendly 格式**：每页开头一句话回答「这是什么」+ 结构化对比表 + FAQ。带「最后更新」日期（AI 偏好新内容）。

---

## 10. Agent 能做 vs 做不了（分工边界）

| ✅ Agent 能独立做 | ❌ 只有你能做（→ 第 11 节） |
|------------------|---------------------------|
| 关键词研究、Volume/KD 拉取、主表维护 | 注册/登录 GSC、GA4、DataForSEO、IndexNow |
| 写落地页/Blog（含 CTA 块、Schema） | 验证域名所有权（DNS/HTML 验证） |
| 每日排名监控 + 出报告 | 绑定/部署域名、配置 DNS、Vercel/Pages 上线 |
| 内链加固、CTR 重写、FAQ JSON-LD | 任何**付款**（DataForSEO 充值、Brave AI tier 升级） |
| 分发平台同步（有 API key 时） | OAuth 授权类操作（GSC URL Inspection 提交） |
| AI 引用抽查、GEO 优化 | 创建 `[CTA_URL]` 注册页本身（产品侧） |

---

## 11. 📋 产品负责人任务清单（Owner Checklist —— 交给 SEO Agent 前必须完成）

> 这些是 Agent **无论如何都做不了**的人工动作。没做完，Agent 第一天就会卡住。打勾后再把 key 交接给 Agent。

### A. 账号 & 授权（必须）

> 标 🔁 的是**账号级 key**：注册一次，多个项目可共用同一套；标 ⚠️ 的是**每个新项目都要单独配**的（域名/资源级）。

- [ ] ⚠️ **Google Search Console**：添加 `[DOMAIN]` 资源 → 完成验证（DNS 或 HTML 文件）→ 提交 sitemap.xml
- [ ] ⚠️ **GA4**：建数据流，绑定 `[DOMAIN]`，把 measurement ID 给 Agent；建「`[CTA_GOAL]` 完成」转化事件；**配 AI 来源渠道组/报告（§6.4 的 regex）** 以单独量化 AI 引流量
- [ ] 🔁 **DataForSEO**：注册 + 充值 → 拿到凭证（排名 / Volume / KD / AIO 的主力）
- [ ] 🔁 **SerpApi**（可选）：SERP / site: 收录计数 / Trends 的交叉验证
- [ ] 🔁 **SEO Review Tools**（可选）：外链 / Domain Authority
- [ ] 🔁 **Brave Search API**（可选）：GEO 监测；AI 摘要要用得升 "Data for AI" tier
- [ ] 🔁 **`[SYNDICATION]` API**（如 dev.to）：内容分发
- [ ] ⚠️ **IndexNow**：在 bing.com/indexnow 生成 key → 把 key 文件放到 `[DOMAIN]` 根目录（每域名单独）
- [ ] ⚠️ **Bing Webmaster Tools**：注册并提交 sitemap（为 AI 时代的 GEO citation 指标占位）
- [ ] 🔁 **（可选）ChatGPT / Perplexity / Claude API key**：用于自动化 AI 引用抽查；没有就用 §12 的人工降级方案

### B. 域名 & 部署（必须）
- [ ] `[DOMAIN]` 已上线、可访问（确认不是 404）
- [ ] robots.txt + sitemap.xml 已部署在根目录
- [ ] 部署管线确认（每次 commit 真的会触发线上更新 —— 别让站点静默 404）

### C. 转化端（必须，否则 CTA 无处可去）
- [ ] **`[CTA_URL]` 落地页已上线**（你的 `[CTA_GOAL]` 落地页，如注册/试用页）
- [ ] 落地页能正常接收带 UTM 的流量
- [ ] GA4 转化事件已配置（让漏斗闭环）

### D. 内容输入（给 Agent 喂料，越全越快）
- [ ] 产品一句话定位 + 核心价值主张
- [ ] `[COMPETITORS]`：列 5 个主要竞品（做对比页用）
- [ ] 种子关键词：你脑子里觉得用户会搜的 10–20 个词（Agent 会扩充）
- [ ] 真实故事/数据：可用于 E-E-A-T 的创始人/团队经历、用户数、案例数字
- [ ] 品牌语气偏好（正式/口语/技术向）

### E. 持续协作（Agent 跑起来后偶发）
- [ ] 每天看一眼日报的「🚩 需要产品负责人处理」段
- [ ] GSC 里 OAuth 类提交（URL Inspection 请求收录）—— Agent 会列清单，你点一下
- [ ] API 余额预警时充值

---

## 12. 工具与数据源（用哪个 key 搜哪种数据）

> 🔐 **安全须知**：API key 是密钥，**永远别写进会被分享的文件**（包括本 SOP）。下表只列工具名和**建议的 env 变量名**作为占位。真实值放进你的密钥管理处（`.env` / 环境变量 / secrets vault），交接给 Agent 时单独走安全渠道。
>
> 💡 **复用说明**：账号级 key（DataForSEO / SerpApi / SEO Review Tools / Brave / 分发平台）是按账号计费的，**一次注册多个项目可共用**；而 GSC 资源、GA4 数据流、域名、IndexNow key 文件是**每个项目单独配**。
>
> 🟢 **最小可用组合**：只想花一份钱跑起来？**DataForSEO（付费）+ GSC（免费）+ GA4（免费）** 三件就够覆盖排名、Volume/KD、曝光和转化漏斗。其余都是「锦上添花/可选」。

### 12.1 核心数据工具（SEO/GEO 必备）

| 工具 | 建议 env 名 | **能搜/拉取什么数据** | SOP 用在哪 | 费用 / 获取 |
|------|------------------|----------------------|-----------|------|
| **DataForSEO** ⭐必备 | `DATAFORSEO_AUTH` | 关键词 **Volume + KD**、SERP 实时排名、AI Overview、SERP features、竞品排名词 | §3 选词、§4 主表、§6 日报排名/GEO | 付费（按查询计费），dataforseo.com 注册 |
| **SerpApi**（可选） | `SERPAPI_KEY` | Google SERP、`site:` 收录计数、Google Trends | §6 排名/索引计数、§3 趋势验证（交叉验证） | 付费，有免费额度，serpapi.com |
| **SEO Review Tools**（可选） | `SEOREVIEWTOOLS_KEY` | 外链(backlinks)、**Domain Authority**、流量估算、关键词 | §7 外链/权威度监控 | 付费，seoreviewtools.com |
| **Google Search Console** ⭐必备 | OAuth（免费，无 key） | **真实曝光/点击/CTR/平均排名**、已收录页、新冒出的排名词 | §6 漏斗、§7 周检查、§3 基线 | 免费，每项目授权一次 |
| **GA4** ⭐必备 | measurement ID（免费） | 自然流量、落地页访问、**CTA→转化漏斗** | §5.3、§6 漏斗 | 免费，每项目配一次 |

> 📌 「~3.2 万曝光」这个数就来自 **GSC 的 Impressions 指标**——所以 GSC 是验证成果的权威源，DataForSEO/SerpApi 是每天高频抓排名的工具。两者口径不同：GSC 是真实数据但有 2-3 天延迟，DataForSEO 是即时但抽样。

### 12.2 GEO / AI 引用监测

| 工具 | 建议 env 名 | 能搜什么 | 费用 / 获取 |
|------|------------------|---------|------|
| DataForSEO（advanced SERP） | `DATAFORSEO_AUTH` | AI Overview 是否触发 + 是否引用本品 | 同上（已有就复用） |
| **Brave Search API**（可选） | `BRAVE_SEARCH_API_KEY` | Brave 搜索结果；Summarizer(AI 摘要) 需升级 **"Data for AI" tier** | 有免费额度，AI 摘要要付费 tier |
| ChatGPT / Perplexity / Claude API（可选） | `OPENAI_API_KEY` 等 | 直接问 AI，抽查品牌是否被提及/引用、信息是否准确 | 付费，各家官网申请 |

> 无 AI API key 时的**降级方案**：每周人工在 ChatGPT / Perplexity / Claude / Google AIO 里搜目标查询，肉眼记录是否引用 `[PRODUCT]`，填进 §6 GEO 战况。

### 12.3 内容分发 & 部署

| 工具 | 建议 env 名 | 能做什么 | 费用 / 获取 |
|------|------------------|---------|------|
| **dev.to API** | `DEVTO_API_KEY` | 发布/更新文章（GET `/articles/me/all` 列文，PUT `/articles/{id}` 改 body）；**需带 `User-Agent` 头避 403** | 免费，dev.to 设置页生成 |
| **托管平台 token**（GitHub Pages / Vercel 等） | `GITHUB_TOKEN` 等 | 部署站点、提交内容、触发构建 | 视平台 |
| Medium / Zenn(日) 等 | 视 `[SYNDICATION]` 而定 | 多平台镜像，canonical 指回主站 | 按需 |

### 12.4 选题 / 长尾挖掘（免费，Agent 直接用）

| 工具 | 能搜什么 |
|------|---------|
| AnswerThePublic / AlsoAsked | 问题型长尾词、People Also Ask（喂 §8 FAQ） |
| Google Autocomplete | 实时搜索建议（捞长尾） |

### 12.5 推广 / 社证数据（非 SEO 核心，做分发时可选）

| 工具 | 建议 env 名 | 能搜什么 |
|------|------------------|---------|
| ProductHunt API | `PRODUCTHUNT_TOKEN` | PH 发布/排名数据 |
| Apify | `APIFY_API_TOKEN` | Twitter/X 抓取（分发、社证） |
| TwitterAPI.io | `TWITTERAPI_IO_KEY` | X 用户/推文/转发数据 |

---

## 附：把这份 SOP 交给 Agent 的最短路径

1. 填好 **§0.1 变量表**。
2. 做完 **§11 人工清单**（至少 A、B、C 三组）。
3. 把本文件 + §0.1 填好的变量，整份交给 SEO Agent，并说：「按这份 SOP 运营 `[PRODUCT]` 的 SEO/GEO，从 Week 0 开始，每天出 §6 日报」。
4. 之后你只需每天看日报头条「首页关键词数」和「🚩 需要产品负责人处理」两段。

---

*SEO/GEO Agent 运营 SOP — 可复用模板版 v1.1 ｜ 把所有 `[变量]` 换成你自己的，即可用于任意产品。*
