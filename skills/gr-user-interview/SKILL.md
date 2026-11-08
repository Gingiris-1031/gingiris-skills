---
name: gr-user-interview
description: '用户访谈与需求验收框架，覆盖原始证据、方案、优先级及回访交接。按行为和复测验证需求，不以访谈场数证明 PMF。覆盖访谈招募、问题设计、 访谈执行、数据合成、决策驱动。从 gingiris-user-interview
  提炼。

  '
metadata:
  author: Iris / Gingiris
  version: 0.3.1
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview
  tags:
  - user-interview
  - user-research
  - pmf
  - product-market-fit
  - jtbd
  - jobs-to-be-done
  - customer-discovery
  - qualitative-research
  - startup
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

## ⚠️ 2C 产品的渠道调整

按当前决策选择样本或渠道：B2B 先区分使用者与购买者；2C 按真实任务、地区和既有触达来源选择小规模试点。不要按粉丝量、平台年龄印象或固定渠道排名代替证据。本包可独立使用，无需额外安装其他 skill。

---

# gr-user-interview — 用户访谈

## 什么时候用

- "我要找 PMF，怎么做访谈"
- "用户反馈很杂，不知道抓哪个"
- "我采访了 5 个人，都没 insight"
- "怎么避免用户说假话"
- "不知道该访谈谁 / 约不到人"
- "激活率、付费率该怎么定义和对标"

---

## 从访谈到上线验收

访谈之后需要与产研协作时，读取 [需求交接与回访模板](references/research-to-acceptance.md)：分开原始证据和拟议方案，按基础能力、onboarding、商业化归类，给出优先级理由、负责人、可观察的验收结果和回访对象。bug 与 feature request 使用不同视图，不能把收集到的意见直接当成交付承诺。

## 核心原则（5 条）

1. **问 behavior，不问 opinion**
   ❌ "你会用这个功能吗？" → 会得到礼貌性"yes"
   ✅ "上次遇到 X 问题是什么时候？你当时做了什么？" → 得到真实行为

2. **20 分钟访谈 >> 5 个 feature 问题**
   深度一个场景，比问 5 个浅问题更有价值

3. **记录方式尊重参与者选择**
   可用笔记；录音、转写、共享范围需单独同意

4. **小批量后暂停，复盘**
   按决策与样本差异安排；重复意见只是线索，继续找反证

5. **用词镜像**
   用户用什么词，你也用什么词 —— 不要替换成产品语言

---

## 访谈结构模板（20-30 分钟）

| 阶段 | 时长 | 问什么 |
|---|---|---|
| Warm-up | 2 min | "你今天做了什么？"（开放式，松弛下来） |
| Discover | 5 min | "上次做 X 是什么时候？能讲讲吗？" |
| Deep-dive | 10 min | "当时你用了什么工具？怎么用的？哪里卡住？" |
| Alternative | 5 min | "有没有试过其他方法？为什么没继续？" |
| Wrap-up | 3 min | "如果有一个魔法能解决这个问题，它会怎么工作？" |

---

## Token Top10 访谈法（招牌打法）

**后台用量 Top10 拉 list → 自愿屏幕演示（录制需单独同意）→ 脱敏记录在获准工具中生成 feature/bug 草稿，审阅后再写入 Linear → 次日回访。节奏按研究问题与复盘能力决定。**

1. 按 token 消耗 / 用量排 Top10，每周刷新——只适合研究高用量行为；新手接入问题应另外招募新用户
2. 经参与者同意后共享屏幕或录屏，允许拒绝：看真实操作 > 听口述
3. 仅在获准向选定 AI 服务发送脱敏记录后提取 feature/bug 草稿；审阅后按已有授权写入 issue 工具
4. 在约定时间回访，仅在核实状态后告知“已修/已排期”；未知状态如实说明
5. 仅向获准的产研成员分享已同意录制且脱敏的片段

**邀约节奏**：
- 只向同意接收研究邀请的人发送邀请；未回复或拒绝后停止，不按固定次数追访。
- 使用用户同意的联系渠道；不反查社交账号追访，不因未回复换渠道联系。
- 话术用宽泛理由（"早期团队想做访谈"），如实说明研究主题和选择范围，不暗示期望答案——避免用户表演

**组合技**：
- KOL 访谈二合一：合作 YouTuber 顺便做用户访谈 + 可用性测试，一次合作两份价值（分别说明研究与推广目的，允许只参与研究）
- 人工 onboarding 适合发现早期障碍；记录帮助，不能据此证明用户已独立激活

---

## 激活与付费口径

| 项 | 定义要求 |
|---|---|
| 激活 | 对应用户获得首次价值的可观察行为，不只注册或登录 |
| 注册到付费 | 同 cohort、同窗口、去重人数与真实付款；无固定合格线 |
| 流失 | 按正常使用周期定义，区分未激活与曾使用后停止 |
| 归因 | 时间线帮助解释，仍需渠道与行为证据，不能单凭先后判因果 |

---

## 深度参考

📂 **https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-user-interview**

- `references/templates.md` — 不同阶段（Discovery / Validation / Retention）的问题模板
- 访谈证据与抽样边界

---

## 合成流程

1. 每次访谈后 24h 内整理 3 张卡片：
   - **Pain**（用户的真实痛）
   - **Workaround**（他们目前怎么凑合）
   - **Quote**（可引用的原话）
2. 每 5 个访谈做一次复盘：
   - 独立出现的 Pain → 待验证需求假设，保留反证与抽样限制
   - 具体 Workaround → 替代方案线索
3. 每 20 个访谈做一次决策：
   - 继续这个假设 / 换方向 / 需要更多数据

---

## 级联推荐

- 访谈发现新 PMF 方向 → `gr-blog-post` 写一篇（验证市场反应）
- 访谈发现对手名字被提 ≥ 3 次 → `gr-competitor` 深度分析
- PMF 明确 → `gr-b2b-growth` 或 `gr-oss-marketing` 启动增长
- 需要招募访谈对象 → 从已同意接收研究邀请的产品用户池或 CRM 选择；GSC 只能辅助选研究主题，不能识别可联系读者
- 在跑红人合作 → 用「KOL 访谈二合一」顺路拿访谈（红人打法见 `gingiris-kol-outreach`）
- 访谈后要定激活/付费目标 → 先定义真实价值行为、cohort 和观察窗口

---

## 反模式

- ❌ 把“愿意付费”的回答当成付款证据；可以了解理由，再验证明确范围与价格的实际购买
- ❌ 用问卷的表态替代任务观察；两者回答不同问题
- ❌ 只访现有用户不访流失用户（流失才是真金）
- ❌ 未经参与者同意延长访谈；建议先约 20–45 分钟，复杂任务分段预约
- ❌ 访谈中推销自己产品（污染答案）
- 只向同意接收研究邀请的人发送邀请；未回复或拒绝后停止，不按固定次数追访。
- ❌ 邀约中暗示期望答案或隐瞒重要研究用途
- ❌ 激活定义写成"注册/登录过"（必须是行为阈值）
- ❌ 访谈完不回访（回访按约定时间进行，只报告已核实状态）


## 纠偏与冷启动实验

按场景读取 [访谈纠偏](references/interview-recovery.md) 或 [冷启动目标与成本](references/cold-start-decision-card.md)。需求研究、可用性测试与销售答疑分开；用户自己完成任务，主持人的帮助单独记录。

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
