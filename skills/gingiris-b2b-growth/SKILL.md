---
name: gingiris-b2b-growth
description: |
  🇺🇸 B2B SaaS Growth — PLG vs SLG Playbook — Diagnose whether your problem is distribution, pricing, or PMF. PLG/SLG selection by ACV and sales cycle, the 5-stage path from $0 to $10M ARR, NRR discipline, affiliate & channel motion, enterprise tiering. Built from HeyGen, Deel, Vercel, Supabase, Snowflake patterns.

  🇨🇳 B2B SaaS 增长 — PLG vs SLG 决策手册 — 诊断你的瓶颈是分发、定价还是 PMF。按 ACV 和销售周期选 PLG/SLG，$0 → $10M ARR 的 5 阶段路径，NRR 纪律，联盟与渠道打法，Enterprise 分层。提炼自 HeyGen、Deel、Vercel、Supabase、Snowflake。

  🇯🇵 B2B SaaS グロース — PLG vs SLG プレイブック — 課題が流通・価格・PMFのどれかを診断。ACVとセールスサイクルでPLG/SLG選定、$0→$10M ARRの5段階パス、NRR規律、アフィリエイト＆チャネル。

  🇰🇷 B2B SaaS 성장 — PLG vs SLG 플레이북 — 병목이 유통·가격·PMF 중 무엇인지 진단. ACV와 세일즈 사이클로 PLG/SLG 선택, $0 → $10M ARR 5단계 경로, NRR 규율, 제휴 & 채널.

  Triggers: "B2B growth" | "B2B SaaS" | "PLG" | "SLG" | "product-led growth" | "sales-led growth" | "PLG or SLG" | "SaaS pricing" | "ARR growth" | "NRR" | "go to market" | "enterprise sales" | "affiliate" | "PMF" | "B2B 增长" | "PLG 还是 SLG" | "SaaS 定价" | "渠道合作" | "PLG/SLG 선택"
when_to_use: |
  Use this skill when you need to: diagnose PLG vs SLG motion, grow B2B SaaS revenue from
  $0 to $10M ARR, design SaaS pricing tiers, build affiliate/channel programs, validate PMF,
  improve NRR, or structure enterprise sales motion.
  Trigger phrases: "B2B growth" | "PLG vs SLG" | "SaaS pricing" | "enterprise sales" |
  "ARR growth" | "B2B增长" | "PLG还是SLG" | "SaaS定价" | "渠道合作"
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-b2b-growth
tags:
  - b2b-growth
  - plg
  - slg
  - saas
  - saas-marketing
  - product-led-growth
  - sales-led-growth
  - b2b-saas
  - startup-growth
  - go-to-market
  - revenue-growth
  - mrr
  - claude-code
  - ai-agent-skill
  - latest
---

# B2B SaaS Growth — PLG / SLG Playbook

> 🌍 **Language / 语言**: [English](#english-version) | [中文](#中文版)

"People like it but revenue isn't growing" is rarely one problem. It's usually a **mis-matched motion**: a PLG product run with an SLG playbook, or vice versa. Start by diagnosing the motion, then walk the staged path.

---

## English Version

### Pick your motion (the flywheel)

```
        PLG (product-driven)
              ↑
   existing traffic + short decision
   ←─────────────────────────────────→
   needs trust + long cycle
              ↓
        SLG (sales-driven)
```

| Signal | Motion | Reference |
|:---|:---|:---|
| ACV < $1k/yr **and** decision < 1 week | **PLG** | Vercel, Supabase |
| ACV > $10k/yr **and** decision > 1 month | **SLG** | Snowflake, Databricks |
| In between | **PLG-to-SLG hybrid** | HeyGen, Deel |

### The 5-stage path

| Stage | ARR | Key move |
|:---|:---|:---|
| **Pre-PMF** | $0–$100k | 10–30 user interviews; confirm the must-have before anything else |
| **Early PMF** | $100k–$1M | Invest in **1–2 channels deeply** — do not spray |
| **Growth** | $1M–$5M | Add affiliate + integration partners; PLG gets sales-assist |
| **Scale** | $5M–$10M | Enterprise team, compliance (SOC 2), channel acceleration |
| **Ecosystem** | $10M+ | Open platform, investor / agency distribution |

### Enterprise deal execution (private deployment & custom 2B)

Winning the contract is half the job — getting paid in full is the other half. Distilled from a Multi-Agent open-source commercialization project retro.

#### Payment structure & final-installment defense

| Rule | Detail |
|:---|:---|
| Staged payments | Private deployment splits **3:4:3** or **4:4:2** — first features live / full deployment / final payment after 3–6 months of ops |
| Collect on signature | **30% due the day the contract is signed** |
| Late penalty | Written into the contract: **0.5% per day** overdue |
| Final-payment leverage | Keep 1–2 features deployed on **your own servers** until the last payment clears — say it before signing, write it into the terms |
| Who to chase | Chase the tail payment with the **highest-ranking contact**; if your champion stalls, escalate to the CEO once or twice |
| Long-term direction | Every new deal: prepayment up, tail payment down |

#### Scope control: SOR / SOW / CCB

- Keep **SOR** (customer's raw asks) separate from **SOW** (acceptance criteria + delivery milestones + change terms); **sign the SOW together with the contract**.
- All changes go through a **CCB**: customer initiates in writing → both PMs assess impact (cost / schedule) → both sides sign a change confirmation.
- Leave a paper trail for everything; name the **acceptance contact** in the contract.
- Customer gets excited on a call and promises the moon? **Only paperwork counts.**

#### Commercial push-pull

- Customer asks for 50 features and you could do 40 → "we can commit to 10, and because we want this to succeed we'll stretch to 15." Turn concessions into favors.
- Requests you don't want → **price them up** (pad the person-days) instead of refusing outright.
- Private deployment has only **two legitimate drivers**: data privacy + internal permission-system integration. Everything else belongs on SaaS.
- SaaS customization → sell a **License**. SSO and similar integrations → open API + standard docs, let the customer build it themselves.

#### Revenue & channel math

| Path to $1M ARR | Breakdown |
|:---|:---|
| Enterprise route | 9 × $100k 2B customers |
| Subscription route | 500 × $200/yr subscribers |

| Channel tier | Terms |
|:---|:---|
| Reseller | 10–20% referral fee |
| Silver (>$100k/yr sales) | 15% |
| Gold (>$300k/yr sales) | 20% |

Reseller due diligence — three questions: what did you resell before? where do your customers come from? reseller or service partner?

**2B content formula**: 80% how you helped customers succeed + 20% about the customer. Deck narrative: pain first, then the fix.

### B2B content is different from B2C

- **Must** have a case study (ROI / time saved / headcount saved).
- **Must** have verifiable numbers ("customer X saved Y hours/month").
- **Must** have a CFO-friendly pricing page (ROI calculator, annual discount, compliance docs).
- ❌ No B2C hype words ("amazing", "magical").

### Anti-patterns

- ❌ Paid acquisition before PMF — you burn cash 10× faster than you learn.
- ❌ Forcing PLG → SLG at $1M just because. Vercel held PLG to $100M.
- ❌ Watching ARR but ignoring **NRR**. NRR < 100% = a leaking bucket.
- ❌ One contract template for everyone — split startup / mid-market / enterprise.

### What to do next

- Pre-PMF → run formal user interviews to find the must-have.
- Post-PMF, need content → move to the blog/SEO workflow (B2B voice: data > story).
- Going global → localize the listing and pricing.
- Benchmarking a rival → run a competitor teardown.

---

## 中文版

### 选你的增长引擎（飞轮）

```
        PLG（产品驱动）
              ↑
   已有流量 + 短决策
   ←─────────────────────────────────→
   需要信任 + 长周期
              ↓
        SLG（销售驱动）
```

| 信号 | 引擎 | 对标 |
|:---|:---|:---|
| ACV < $1k/年 **且** 决策 < 1 周 | **PLG** | Vercel、Supabase |
| ACV > $10k/年 **且** 决策 > 1 个月 | **SLG** | Snowflake、Databricks |
| 中间 | **PLG-to-SLG 混合** | HeyGen、Deel |

### 5 阶段路径

| 阶段 | ARR | 关键动作 |
|:---|:---|:---|
| **Pre-PMF** | $0–$100k | 10–30 次用户访谈，先确认 must-have |
| **Early PMF** | $100k–$1M | **投 1–2 个渠道做深**，不要广撒网 |
| **Growth** | $1M–$5M | 引入 affiliate + 集成伙伴，PLG 加 sales-assist |
| **Scale** | $5M–$10M | Enterprise 团队、合规（SOC 2）、渠道加码 |
| **Ecosystem** | $10M+ | 开放平台、investor / agency 分销 |

### 2B 打单与交付（私有化 & 定制）

签下合同只是一半，全额收回款才是另一半。提炼自某 Multi-Agent 开源商业化项目复盘。

#### 付款结构与尾款防御

| 规则 | 细节 |
|:---|:---|
| 分段付款 | 私有化部署 **3:4:3** 或 **4:4:2** —— 第一批功能上线 / 全部部署完 / 运维 3–6 个月后付尾款 |
| 签约即收款 | **签合同当天收 30%** |
| 违约金 | 直接写进合同：**拖一天多付 0.5%** |
| 尾款筹码 | 交付时留 1–2 个功能部署在**自己服务器**，尾款结清才迁 —— 签合同前说清楚、条款里写清楚 |
| 找谁要 | 尾款直接找**对接的最高的人**；对接人推诿可问 1–2 次 CEO |
| 长期方向 | 每一单：预付款越来越高、尾款越来越少 |

#### 需求边界管理：SOR / SOW / CCB

- **SOR**（客户原始输入）与 **SOW**（验收标准 + 交付节点 + 变更条款）分开；**合同和 SOW 一起签**。
- 变更一律走 **CCB**：客户先书面发起 → 双方项目经理评估影响（金额 / 工期）→ 双方签变更确认文件。
- 一切留痕（会议 / 对话 / 验收记录）；合同指明"项目验收对接人"。
- 客户聊嗨了拍胸脯？**只有 paperwork 有效。**

#### 商务推拉

- 客户提 50 个需求、内部判断 40 能做 →"先答应 10 个，因为想帮你所以做到 15 个"——把让步做成人情。
- 不想做的需求**抬价过滤**（人/天多标几天），不用直接拒绝。
- 私有化需求只有**两个真点**：数据隐私 + 接内部权限系统，其他都该买 SaaS。
- SaaS 二开 → 直接卖 **License**；SSO 等集成 → 开放 API + 标准手册，让客户自己做。

#### 营收与渠道账

| $1M ARR 拆解 | 组成 |
|:---|:---|
| 2B 路线 | 9 个 $10 万企业客户 |
| 订阅路线 | 500 个 $200/年订阅用户 |

| 代理分层 | 条件 |
|:---|:---|
| Reseller | 10–20% 推荐费 |
| 银牌（年销 >$10 万）| 15% |
| 金牌（年销 >$30 万）| 20% |

代理尽调三问：之前代理过什么产品？客户从哪来？Reseller 还是 Service Partner？

**2B 内容公式**：80% 讲自己如何帮客户成功 + 20% 讲客户；deck 叙事"先讲怎么痛，再说怎么好"。

### B2B 内容特殊要求

- **必须有 case study**（ROI / 省时 / 省人力）。
- **必须有可验证数据**（"customer X saved Y hours/month"）。
- **必须有 CFO 友好的 pricing 页**（ROI 计算器、年付折扣、合规文档）。
- ❌ 不用 ToC 话术（"amazing"、"magical"）。

### 反模式

- ❌ 没 PMF 就投流（烧钱比学习快 10x）。
- ❌ 到 $1M 就盲目 PLG → SLG（Vercel 坚持 PLG 到 $100M）。
- ❌ 只看 ARR 不看 **NRR**（NRR < 100% = 漏水桶）。
- ❌ 只给一个合同模板（分 startup / mid-market / enterprise 三版）。

---

*By Iris (生姜 Iris) · ex-COO @ AFFiNE, 150+ AI startups advised · Install: `npx skills add Gingiris-1031/gingiris-b2b-growth`*
