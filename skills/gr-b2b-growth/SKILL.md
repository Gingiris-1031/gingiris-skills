---
name: gr-b2b-growth
description: >
  B2B SaaS 全生命周期增长。从 PMF 验证到 $10M ARR 的完整路径。覆盖 PLG / SLG 选型、
  客户访谈、联盟营销、渠道合作、Enterprise sales。整合 HeyGen、Deel、Vercel、Supabase、AWS 案例。
  从 gingiris-b2b-growth 提炼。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-b2b-growth
tags:
  - b2b-growth
  - plg
  - slg
  - saas
  - product-led-growth
  - sales-led-growth
  - b2b-saas
  - revenue-growth
  - arr
  - go-to-market
  - startup-growth
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

# gr-b2b-growth — B2B SaaS 增长

## 什么时候用

- "我的 B2B SaaS 怎么从 0 做到 PMF"
- "PLG 还是 SLG，我该选哪个"
- "怎么做 affiliate 营销"
- "渠道合作 / 集成伙伴怎么谈"
- "Enterprise sales 怎么起"
- "私有化部署怎么收款 / 尾款怎么要"
- "客户需求蔓延怎么管（SOW / 变更）"

---

## 增长飞轮（4 象限）

```
        PLG（产品驱动）
            ↑
            |
   已有流量 + 短决策  ←→  需要信任 + 长周期
            |
            ↓
        SLG（销售驱动）
```

选型判据：
- ACV < $1k/年 & 决策周期 < 1 周 → **PLG**（Vercel、Supabase 模式）
- ACV > $10k/年 & 决策周期 > 1 个月 → **SLG**（Snowflake、Databricks 模式）
- 中间 → **PLG-to-SLG hybrid**（HeyGen、Deel 模式）

---

## 5 阶段路径

| 阶段 | ARR | 关键动作 |
|---|---|---|
| Pre-PMF | $0-$100k | 10-30 次用户访谈（联动 `gr-user-interview`），确认 must-have |
| Early PMF | $100k-$1M | 投 1-2 个渠道做深（不要广撒网） |
| Growth | $1M-$5M | 引入 affiliate + 集成伙伴，PLG 加 sales-assist |
| Scale | $5M-$10M | Enterprise 团队、合规认证（SOC2）、channel 加码 |
| Ecosystem | $10M+ | 开放平台、investor / agency 分销 |

---

## 2B 打单与交付（私有化 & 定制实操）

来自某 Multi-Agent 开源商业化项目复盘。签合同只是一半，全额收回款才是另一半。

### 付款与尾款防御

| 规则 | 细节 |
|---|---|
| 分段付款 | 私有化 **3:4:3** 或 **4:4:2**（首批功能上线 / 全部部署完 / 运维 3–6 个月后尾款）|
| 签约即收款 | 签合同当天收 30% |
| 违约金 | 写进合同：拖一天多付 0.5% |
| 尾款筹码 | 留 1–2 个功能部署在自己服务器，尾款结清才迁（签前说清、条款写清）|
| 找谁要 | 尾款找对接的最高的人；推诿可问 1–2 次 CEO |
| 长期方向 | 预付款越来越高、尾款越来越少 |

### 需求边界：SOR / SOW / CCB

- SOR（客户原始输入）与 SOW（验收标准+交付节点+变更条款）分开，**合同和 SOW 一起签**
- 变更走 CCB：客户书面发起 → 双方 PM 评估金额/工期 → 签变更确认
- 一切留痕；合同指明"项目验收对接人"
- 客户口头承诺再多，**只有 paperwork 有效**

### 商务推拉与定价

- 客户提 50 个需求、能做 40 →"先答应 10 个、因为想帮你做到 15 个"，把让步做成人情
- 不想做的需求抬价过滤（人/天多标几天），不直接拒
- 私有化只有两个真需求：数据隐私 + 接内部权限系统，其他都该买 SaaS
- SaaS 二开直接卖 License；SSO 等集成开放 API + 标准手册让客户自己做

### 营收与渠道账

- $100 万 ARR 拆解：9 个 $10 万 2B 客户 **或** 500 个 $200/年订阅用户
- 代理分层：reseller 10–20% 推荐费；年销 $10 万银牌 15%、$30 万金牌 20%
- 代理尽调三问：代理过什么产品？客户从哪来？Reseller 还是 Service Partner？
- 2B 内容公式：80% 讲自己如何帮客户成功 + 20% 讲客户；deck 先讲怎么痛、再说怎么好

---

## 深度参考

📂 **https://github.com/Gingiris/gingiris-b2b-growth**

- `references/foundation.md` — PMF 验证 + 定价分层
- `references/contracts.md` — 合同/条款模板（SaaS 标准条款 + 本地化）
- `references/seo-geo-guide.md` — B2B SEO 飞轮
- `references/en/` — 英文版

---

## 级联推荐

- Pre-PMF 阶段需要访谈 → `gr-user-interview`
- PMF 后要做内容 → `gr-blog-post`（含 B2B 文风：数据 > 故事）
- 出海需要本地化 → `gr-aso` 或 `gr-blog-post` i18n
- 找对标案例 → `gr-competitor`

---

## B2B 内容特殊要求

- **必须有 case study**（ROI / 节约时间 / 节约人力）
- **必须有可验证数据**（"our customer X saved Y hours/month"）
- **必须有 CFO 友好的 pricing 页**（ROI 计算器、年付折扣、合规文档）
- ❌ 不要用 ToC 营销话术（"amazing"、"magical"）

---

## 反模式

- ❌ 没 PMF 就投流（烧钱速度比学习速度快 10x）
- ❌ PLG 做到 $1M 就盲目转 SLG（很多死在这里 —— Vercel 是反例，坚持 PLG 到 $100M）
- ❌ 只看 ARR 不看 NRR（NRR < 100% = 漏水桶）
- ❌ Enterprise 只给一个合同模板（要分 startup / mid-market / enterprise 三版）
