---
name: gingiris-go-global
version: 1.0.11
description: |
  🇺🇸 AI Product / SaaS Go-Global Complete SOP — From competitor research to launch to monetization. A full-cycle playbook covering Phase 0-5 (market validation, positioning, first 100 users, user interviews, beta-to-growth) plus open-source launch, Product Hunt, Reddit, SEO/GEO, conversion, and org principles. **Defaults to dev tools / OSS / B2B SaaS; for 2C products (education, apps, games) the launch channels & metrics differ — see gingiris-seo-geo/references/2c-adaptation.md.**

  🇨🇳 AI 产品 / SaaS 企业出海完整 SOP — 从竞品调研到 Launch 到商业化的全流程操作手册。覆盖 Phase 0-5（市场验证、定位、前100用户、用户访谈、Beta转增长）+ 开源发布、Product Hunt、Reddit、SEO/GEO、转化与组织原则。**默认面向开发者工具/开源/B2B SaaS；2C 产品（教育/应用/游戏）的启动渠道与指标不同，见 gingiris-seo-geo/references/2c-adaptation.md。**

  🇯🇵 AI製品/SaaS海外展開フルサイクルSOP — 競合調査からローンチ、マネタイズまで。Phase 0-5（市場検証、ポジショニング、最初の100ユーザー、ユーザーインタビュー、ベータから成長）＋オープンソース、Product Hunt、Reddit、SEO/GEO、コンバージョン、組織原則。

  🇰🇷 AI 제품/SaaS 글로벌 진출 완전 SOP — 경쟁사 조사부터 런칭, 수익화까지 전 주기 플레이북. Phase 0-5(시장 검증, 포지셔닝, 첫 100명 사용자, 사용자 인터뷰, 베타→성장) + 오픈소스 런칭, Product Hunt, Reddit, SEO/GEO, 전환, 조직 원칙.

  Triggers: "go global" | "出海" | "overseas expansion" | "GTM" | "cold start" | "launch strategy" | "international expansion" | "海外增长" | "出海SOP" | "product launch overseas" | "海外进出" | "グローバル展開" | "글로벌 진출" | "go-to-market" | "出海打法"
when_to_use: |
  Use this skill when you need to: execute AI product / SaaS global expansion, validate
  overseas market fit, acquire first 100 international users, localize product and landing
  page, run Product Hunt / Reddit / SEO for global launch, or build international GTM strategy.
  Trigger phrases: "go global" | "出海" | "overseas GTM" | "international expansion" |
  "出海SOP" | "出海打法" | "海外冷启动" | "글로벌 진출"
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-go-global
tags:
  - go-global
  - international-expansion
  - localization
  - global-marketing
  - saas-globalization
  - cross-border
  - go-to-market
  - asia
  - startup
  - gtm
  - claude-code
  - ai-agent-skill
  - overseas-expansion
  - japan-korea
  - latest
---

## ⚠️ 使用前：确认你的产品类型

本 SOP 默认场景：**开发者工具 / 开源 / B2B SaaS 出海**（Phase 渠道默认 Product Hunt / HN / Reddit / GitHub）。

如果你的产品是 **2C 消费品 / 教育 / 应用 / 游戏**，以下必须替换：

| 环节 | 默认（B2B/开源）| 2C 建议 |
|------|------|------|
| 前 100 用户渠道 | PH / HN / GitHub / LinkedIn | 垂类社区(Reddit/小红书/知乎/Naver 카페) + 短视频(TikTok/抖音/YouTube) + 垂直 KOL |
| Launch 打法 | Product Hunt 打榜 | 2C 下 PH 受众错配、ROI 低；改"红利内容 + 免费钩子 + 社区分发" |
| 核心指标 | MRR / CAC / LTV | D1/D7/D30 留存、激活率、病毒系数 K |
| 增长引擎 | Freemium 试用 → 销售 | 免费产品当钩子(PLG)，先拿 100 真实用户再放量 |
| 选渠道方法 | 按"科技人聚集地" | 按地区公开数据选第一平台(如印尼/泰国短视频已反超 Facebook) |

完整 2C 渠道数据库（各国 MAU + 公开来源）见 → `gingiris-seo-geo/references/2c-adaptation.md`

---

# AI 产品/SaaS 企业出海完整 SOP

> 作者：Iris (生姜iris) | 版本：1.0.0

## 核心理念

出海不是"发英文内容 + 上 Product Hunt"。真正的主线是：

1. 找到最窄、最愿意付费的用户
2. 用竞品和用户语言定义一句话定位
3. 把官网、README、Demo、社区、转化路径做成闭环
4. 在 24-48 小时内集中打出可信流量峰值
5. 峰值之后立刻转向用户访谈、转化率和商业化
6. 用内容、社区、SEO、生态合作把一次发布沉淀成长期资产

**一句话：先把桶补好，再开水龙头。**

---

## 全流程框架

### Phase 0：出海前判断

回答四个问题：
- 你靠谁赚钱？
- 这批人现在用什么替代方案？
- 他们在哪些渠道主动讨论这个问题？
- 他们为什么现在就愿意切换或付费？

回答不出来 → 不要做 launch，先做用户访谈和竞品拆解。

### Phase 1：竞品调研

- 只选最多 3 个对标（用户画像一致、商业模式一致、已跑通商业化）
- 用 web.archive.org 拆竞品官网历史（每阶段一句话介绍、CTA 变化、客户 logo 出现时间）
- 拆渠道：Twitter/X、YouTube、Reddit、SEO（竞品词/alternative/场景词/问题词）
- 落到一张表：哪个渠道适合你、为什么、第一波怎么打

### Phase 2：定位与官网

- **一句话公式**：`[差异点] + [对标产品] + for [目标用户/场景]`
- 官网首屏 10 秒内说清：这是什么、给谁用、替代什么、为什么更好、下一步点哪里
- 结构：价值主张+CTA → Use Case → Trusted By → 功能/对比/定价/FAQ

### Phase 3：前 100 个用户

PMF 前不要花超过 $1000 找前 100 个用户：
1. 挖竞品活跃用户（近 3 月评论过竞品、表达不满）
2. LinkedIn 精准建联（按职能/行业/公司规模/国家/工具）
3. Reddit / Twitter 关键词监听（竞品名、alternative to、looking for）
4. Fiverr / 服务市场验证付费需求

### Phase 4：用户访谈

- 必须共享屏幕、看竞品使用、用户说 80% 你说 20%
- 优先访谈：Top 10 付费用户 / Token 消耗 Top 10 / 连续使用 3-7 天的 Beta 用户
- 理解上下游 workflow：前一步、后一步、替代方案、卡点、哪一步愿意付钱

### Phase 5：Beta 用户转增长资产

- 创始人亲自 Welcome Letter + 专属社区
- 连续使用 3-7 天后推动社媒分享
- 把用户总结出的产品差异改写成官网和社媒文案

---

## 渠道 SOP 摘要

| 渠道 | 核心要点 |
|:---|:---|
| 开源 Launch | 48h 集中引爆，所有入口回 GitHub README |
| Product Hunt | Badge 战，非流量战；organic community engagement |
| Reddit | 潜水 1-2 周，80% 干货 + 20% 产品；不要跨社区复制 |
| SEO/GEO | 先做 alternative / use case / 模板页 / 对比页 |

---

## 转化与商业化

- 放量前看注册到付费转化率（ToC >1.5%, Prosumer 5-8%, SMB 10-15%）
- $1M ARR 前集中 1-2 个渠道打透
- $200万 revenue 前不急建海外本地团队
- PLG = 用户通过产品获得收益和传播动机

---

## 一页作战清单

| 阶段 | 关键动作 |
|:---|:---|
| L-6w ~ L-4w | ICP、对标、竞品拆解、一句话定位、20-40 次访谈 |
| L-4w ~ L-2w | 官网、README、Demo、文档、KOL 名单、Reddit 预热 |
| L-1w | 小时级发布表、文案、PH 准备、压测 |
| Launch 48h | 全渠道同步、KOL 两波、每小时记录、实时回复 |
| L+90d | 高活访谈、SEO 文章、awesome-list、ambassador、优化转化 |

---

## 详细参考

完整 SOP 原文（含全部阶段细节、播客总结、作战清单）：

→ [references/full-sop.md](references/full-sop.md)

---

## 硬件出海市场进入策略

> 来源：Plaud 官方众筹报道 / Makuake 项目页 / Insta360 IPO 招股书 / Forbes / PR Times

### 一、Plaud 日本 Makuake 策略：众筹长臹法

Plaud 进入日本市场的路径是硬件出海的典型模式：先在全球平台验证需求，再以本地化步骤重新进入重要市场。

```
阶段 1：全球平台验证（Kickstarter）
2023.06 上线 Kickstarter
$1,108,181 / 7,564 backers（来源：Kickstarter 官方）
展示全球真实需求验证 + 建立品牌知名度

阶段 2：小体量日本验证（全球采购流量监测）
通过全球云店少量接受日本订单
检验日本市场的真实到货率、退货率、客服需求

阶段 3：本地众筹平台上线（Makuake）
2023年底-2024年入驾 Makuake（日本最大众筹平台）
2个月内破 2.7亿日元（升至 Makuake 商务工具类目历史第一）
来源：PR Times / Makuake 官方公告

阶段 4：本地法人建立
在日本设立实体法人实现本地化运营
进入山田、纳娷、亚马逊日本等本地零售渠道
```

**模式提炼：**
- Kickstarter 不仅是单第一笔资金，更重要的是验证了全球 7,564 个付费意愿的电子邮件名单
- 日本分阔关键：日文单独运营号 + 本地客服能力 + 日文 Landing Page SEO
- Makuake 项目成功后，本地活跃度可以支撑第一个本地雇员

> 🇺🇸 **Plaud Japan Ladder**: Kickstarter (global validation) → Monitor JP orders via global store → Launch Makuake (local crowdfunding, ¥270M raised, #1 in Business Tools category) → Establish JP legal entity + local retail. Key: each step reduces market-entry risk before the next commitment.

---

### 二、Insta360 区域办公室模式：运营前哨而非销售前哨

Insta360 的海外团队建设遵循一个原则：
**先活跃过一个阈值，再建本地团队**。

| 办公室 | 地址 | 主要职能 | 选择逻辑 |
|------|------|----------|----------|
| 洛杉矶办公室 | 美国洛杉矶 | 创作者社区 + 娱乐/体育联定 | 全球最大影视内容创作者市场 |
| 东京办公室 | 日本东京 | 日本创作者社区 + 亚太地区市场 | 日本消费级相机市场以及产品南亚辐射 |
| 柏林办公室 | 德国柏林 | 欧洲市场运营 + 体育评歋 | 德语域 + 全欧盲盒 |

**运营前哨的定义：**
- 不是简单的销售代表处，而是能够在当地执行创作者活动、担任当地 PR、识别重要 KOL 并建立关系
- 每个办公室的核心 KPI 不是销售额，而是创作者参与活跃度、社区编程活动数量、当地媒体覆盖数量
- 海外营收占总营收 70%-76%（来源：36kr / KR Asia / Insta360 IPO 招股书分析）

> 🇺🇸 **Insta360 Regional Office Model**: Los Angeles / Tokyo / Berlin are **operations outposts, not sales outposts**. Their primary job is creator community activation, local PR and KOL relationship-building. Revenue follows community density, not headcount.

---

### 三、本地化触发点：组织化本地运营升级局

**市场层级升级运运标准（三级门槛）：**

| 阶段 | GMV 占比阈值 | 运运动作 |
|------|------------|----------|
| **观察期** | <5% 全球 GMV | 全球平台统一运运，旨趣商品展示和本地语言 |
| **验证期** | 5%-15% 全球 GMV | 开启本地语言社交运运、本地化着陆页、识别重要 KOL |
| **组织化升级** | **>15% 全球 GMV** | **触发“组织化本地运运”升级**：雇用本地运运、进入本地众筹平台、建立当地社区 |

**15% GMV 阈值的依据：**
- 当一个市场占全球 GMV 超过 15%，说明该市场有足够的自发购买力支撑全荷本地团队成本
- 带后察训号指标：公司内部用。Plaud 日本 + Insta360 东京都在达到超10%+ GMV 占比后才开始本地团队投入

**升级后的本地化动作应包含：**
- 本地语言社交账号独立运运
- 本地众筹平台项目（如 Makuake、豷貗山一等）
- 本地座谈与发布会参与
- 本地零售/线下渠道盘点
- 本地化 PR + 独窶策略

> 🇺🇸 **15% GMV Trigger Rule**: When a single market exceeds 15% of global GMV, it has proven sufficient organic demand to justify localized org investment. Before that threshold: run on global ops + localized landing page. After: hire local, enter local crowdfunding platforms, establish legal entity.

---

## 出海实战增补：转化闸门 / 本土化公式 / 收费与组织纪律（播客一手复盘 2026-07）

> 来源：Iris 2026 年多档播客访谈（AFFiNE 四年复盘 + 150+ AI startup 咨询）。口述回忆数字均标注"播客口径 / ≈"。

### 一、放量闸门：先磨转化，再开流量

**注册→付费转化率达标前，不投放、不发 Product Hunt、不搞红人营销：**

| 产品类型 | 放量基准线（注册→付费） |
|---|---|
| ToC AI 软件 | ≥1.5%（做得好 6-8%，顶尖案例 ≈40%，播客口径） |
| ToB AI 软件 | >10-15% |

- 这套"先跑转化再放量"讲给过 100-200+ 团队（两期播客口径分别为"100+"与"至少 200"），**真正执行完的不到 10 个**；执行者注册→付费转化率普遍做到 **4-8% 甚至更高**，后续融资也更顺。
- 实证（播客口径）：一个 ToC 产品照做后沉寂约半年，注册→付费转化率达 6-8%，约 1 万注册用户做到 ≈$5,000 MRR，随后放量曲线起飞、融资顺利。
- 执行动作：耐心和用户聊（同一个用户可以聊 5 次），找出当前阶段付费意愿最高的画像重点深聊；抵抗 FOMO——不要因为竞品天天发 PR 就在产品没 ready 时抢跑宣发。

> 🇺🇸 **Conversion gate before scaling**: do not run ads, launch on Product Hunt, or hire influencers until signup-to-paid conversion clears the bar — ToC AI >=1.5% (good products reach 6-8%, top cases ~40%, self-reported), ToB AI >10-15%. This playbook was taught to 100-200+ teams; fewer than 10 fully executed it. Those who did reached 4-8%+ conversion. One ToC product stayed quiet for ~6 months, hit 6-8% conversion and ~$5,000 MRR on ~10K signups, then scaled and raised smoothly. The gap is never the methodology — it is execution and resisting FOMO.

### 二、80% SOP + 20% 本土化迁移公式

- 出海是**做减法**不是做加法：把解决方案模块化、抽象化 → **80% 标准化 SOP + 20% 本土化迁移**。
- 本土化的 20% 落在三件事：**集成当地生态合作伙伴、配合当地节假日节奏、按当地文化属性做改造**。
- 市场认知纠偏（一手观察）：东南亚（马来西亚/越南）甚至欧美的数字化程度**低于中国**——要在对方当前阶段能接受的前提下提供服务，不要把海外想得太发达。
- 中国团队的天然武器：**24 小时响应 vs 欧美团队约一周回复**——响应速度本身就是差异化竞争力。

> 🇺🇸 **The 80/20 localization formula**: going global is subtraction, not addition — modularize your solution into an 80% standardized SOP plus a 20% local adaptation layer. The 20% covers three things: integrate with the local ecosystem, align with local holidays, adapt to local culture. Reality check from field visits: digital maturity in Southeast Asia (and even in the US/EU) is often LOWER than in China — serve the market at the stage it is actually at. A Chinese team's 24-hour response time vs. the typical one-week reply from US/EU vendors is itself a competitive weapon.

### 三、Showcase-first：先赔本打样，再让客户带客户

- 任何行业验证 PMF（尤其服务型/顾问型出海业务），先**赔本打 1-2 个 showcase**，目的只有一个：确认你的 SOP 完全有效。
- showcase 跑通后不必主动扩张：客户带客户、投资人转介绍会自然发生。
- 配套纪律：早期不筛客户会踩坑 → showcase 之后建立客户筛选标准（看项目本身 + 对接人特质：EGO 低、心态开放、有学习能力）。

> 🇺🇸 **Showcase-first PMF**: before selling, run 1-2 showcases at your own cost — even at a loss — with a single goal: prove the SOP works end to end. Once a showcase lands, clients bring clients and investors refer deals; you rarely need outbound. Then add a client filter (project quality + a low-ego, open, fast-learning counterpart) — skipping the filter early is a known failure mode.

### 四、Day-0 收费纪律

- **从 day 0 开始赚钱，勇敢收费**：只有收钱，你才知道这个东西是否真的被需要。
- 付费客户和免费客户对你的标准不同——付费反馈质量更高；付费用户用脚投票，免费用户"指点江山"。
- 允许 pricing test 调整期：未来定价 $20 区间的，早期天使用户可先收 $5（打 1-2 折）；**哪怕收 $1 也要让用户付**，种下"这不是免费产品"的心智。

> 🇺🇸 **Day-0 charging discipline**: start charging from day 0 — money is the only signal that proves the product is genuinely needed. Paying customers hold you to a different (higher-quality) feedback standard than free users: paying users vote with their wallet. A pricing-test period is fine (charge $5 early for a future-$20 product), but even $1 matters — it plants the "this is not a free product" expectation.

### 五、组织规模阶梯：8 人以内先做营收

| 团队规模 | 组织要求 |
|---|---|
| ~3 人 | 必须有唯一 decision maker（founder 本人） |
| 6-8 人 | 产品/设计/研发/运营配齐（每方向 1-2 人） |
| 10-12 人 | 各方向出现 leader 层 |

- 目标纪律：**8 人以内先做营收、先赚钱**——很多时候你不需要那么多人。
- 人效参照（播客口述口径）：Notion ≈4-8 人时已有百万用户量级；ClickUp 做到百万级 ARR 时 ≈24 人。
- 不要因为"融了钱就该有某个规模的团队"而招人；唯一标准是这个阶段真的忙不过来。先用工具（LinkedIn/Twitter DM 自动化等）替代 headcount。

> 🇺🇸 **Org-size ladder**: at ~3 people there must be exactly one decision maker (the founder); at 6-8 people, cover product/design/eng/ops with 1-2 each; at 10-12 people, a leader layer emerges per function. Discipline: get to revenue with 8 or fewer people. Reference points (self-reported podcast recollection): Notion had ~1M users at roughly 4-8 people; ClickUp reached ~$1M ARR at ~24 people. Never hire to match a funding round — hire only when the stage genuinely overflows, and automate (LinkedIn/Twitter DM tooling) before adding headcount.

### 六、融资认知速记

- 一手时间线：天使轮见 ≈400 个投资人、耗时一整年才 close；开源 traction 起来后**一个月 close $8M Pre-A**（Iris 本人口径；两年三轮累计约 $10M）。融资难易的分水岭不是 pitch 技巧，而是**可展示的增长信号**。
- 融资叙事 pivot 三步：查叙事饱和度（该故事投资人是否已投满同类）→ 找赛道公认的技术壁垒 → 把产品拆成可复用 Infra 讲，配一句量化叙事。
- 排期策略：不是见得越多越好——先安排低优先级投资人"练手"，识别出成功率高的对象后重点突破。
- 拿钱后三大组织崩坏（反面教训，只留方法论）：**报复性扩张**（前期吃苦后盲目招人烧钱）、**流量最好时不变现**（注意力从用户转向讨好投资人）、**产研运失衡**（运营收集的用户需求进不了产品决策）。

> 🇺🇸 **Fundraising in one breath**: the angel round took ~400 investor meetings over a full year; after open-source traction, the $8M Pre-A closed in one month (founder's own figure; ~$10M total across three rounds in two years). The divide is never pitch craft — it is a demonstrable growth signal. Narrative-pivot framework: check narrative saturation, find the sector's acknowledged technical moat, reframe the product as reusable infra with one quantified line. Sequencing: warm up on low-priority investors first, then concentrate on high-probability targets. After the money lands, the three classic failure modes are revenge over-hiring, failing to monetize at peak traffic, and product/eng/ops imbalance.

完整融资 playbook（流程链 / TS-DD-SPA / 条款避坑 / 资金纪律）→ [references/fundraising-playbook.md](references/fundraising-playbook.md)
