---
name: gingiris-user-interview
description: '🇺🇸 User Interview & Cold-Start Operations Playbook — Evidence-led research, usability testing and
  follow-up. Complete SOP for user screening, interview execution, Beta testing methodology, cold-start user operations,
  churn analysis, and user grading systems.


  🇨🇳 用户访谈与冷启动运营实战手册 — 基于真实行为、可用性观察与回访验证需求。包含用户筛选、访谈执行、Beta 测试设计、冷启动用户运营、流失分析、用户分级体系完整 SOP。


  🇯🇵 ユーザーインタビュー＆コールドスタート運営プレイブック — 実際の行動とユーザビリティテストに基づく需要検証。ユーザースクリーニング、インタビュー実行、Betaテスト設計、コールドスタートユーザー運営、離脱分析、ユーザーグレーディング。


  🇰🇷 사용자 인터뷰 & 콜드 스타트 운영 플레이북 — 실제 행동과 사용성 관찰에 기반한 수요 검증. 사용자 스크리닝, 인터뷰 실행, Beta 테스트 설계, 콜드 스타트 사용자 운영, 이탈 분석, 사용자
  등급 시스템.


  Triggers: "user interview" | "user research" | "customer discovery" | "PMF" | "product-market fit" | "beta test"
  | "beta testing" | "cold start users" | "cold start operations" | "churn analysis" | "user grading" | "用户访谈" |
  "用户调研" | "冷启动" | "冷启动运营" | "Beta测试" | "流失分析" | "用户分级"

  '
metadata:
  version: 1.1.1
  when_to_use: 'Use this skill when you need to: conduct user interviews to find PMF, design Beta testing

    methodology, operate cold-start user cohorts, analyze churn, build user grading systems,

    or apply JTBD framework to validate product direction.

    Trigger phrases: "user interview" | "PMF" | "customer discovery" | "beta test" |

    "用户访谈" | "冷启动运营" | "PMF验证" | "流失分析" | "JTBD"

    '
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-user-interview
  tags:
  - user-interview
  - user-research
  - pmf
  - product-market-fit
  - jtbd
  - jobs-to-be-done
  - customer-discovery
  - qualitative-research
  - product-development
  - startup
  - claude-code
  - ai-agent-skill
  - beta-testing
  - cold-start
  - latest
---

## ⚠️ 2C 产品的渠道调整

按当前决策选择样本或渠道：B2B 先区分使用者与购买者；2C 按真实任务、地区和既有触达来源选择小规模试点。不要按粉丝量、平台年龄印象或固定渠道排名代替证据。本包可独立使用，无需额外安装其他 skill。

---

# 用户访谈与冷启动运营实战手册

播客一手案例与引用边界：`references/podcast-evidence.md`。

> 🌍 **Language / 语言**: 中文 | [Interview Guide](references/interview-guide.md) | [Cold-Start Ops](references/cold-start-ops.md)

---

## 核心原则

围绕当前决策观察真实任务，记录反证，修改后回访验证。访谈数量与频率由样本差异、问题复杂度和团队资源决定，不是成功率或 PMF 的证明。

---

## Token Top10 访谈法（2026 招牌方法）

把访谈从"调研动作"变成"日常运营循环"的最短路径，已在多个 AI Agent 项目全线复用：

1. 后台按 token 消耗 / 用量拉 **Top10 用户 list**（每周刷新）
2. 约**共享屏幕访谈；录制需同意，可不录制**——看真实操作 > 听口述
3. **脱敏 transcript**：确认接收服务、数据范围与同意后生成需求草稿，审阅后再按授权写入 Linear
4. **次日回访**：告知"你提的 X 已修/已排期"，仅在状态已经核实后告知；排期不等于修复
5. 节奏按研究问题与团队复盘能力安排；仅向获准的产研成员分享已同意录制且脱敏的片段

**配套动作**：
- 新访谈员先 mock interview + 经同意的记录 + 复盘，再上真实用户
- **KOL 访谈二合一**：合作 YouTuber 顺便做用户访谈 + 可用性测试，一次合作拿两份价值；分别说明研究与推广目的，允许只参加研究
- 访谈资产化：访谈可产出需求证据；将内容用于SEO公开引用或商业线索需另行许可，不默认改变研究数据用途

### 邀约触达节奏（2026 更新）

- 只向同意接收研究邀请的人发送邀请；未回复或拒绝后停止，不按固定次数追访。
- **访谈邀请**：使用用户同意的联系渠道；不反查其他账号追访，未回复或拒绝后停止跟进
- 话术用宽泛理由（"团队早期想做用户访谈"），**如实说明研究主题和选择范围，不暗示期望答案**，避免用户带着预设表演

### 案例使用边界

历史案例中的访谈场数属于来源口述，口径未统一，不用作增长资格门槛。可迁移的是观察问题、修正产品、复测真实任务的过程。

---

## 用户访谈执行框架（5步）

### Step 1：确定目标与筛选用户

**样本选择示例（按本轮决策调整，不是通用排名）**：
| 优先级 | 用户类型 | 价值 |
|--------|----------|------|
| 候选 | 付费用户 | 解释购买与持续使用 |
| 候选 | 高频活跃用户 | 解释高用量任务，不代表新手 |
| 候选 | 竞品用户 | 提供竞争视角 |
| 候选 | 流失用户 | 暴露产品真实问题 |
| 候选 | 注册未付费用户 | 转化障碍洞察 |

### Step 2：邀约与排期

**跟进节奏**：使用参与者同意的渠道与频次；无回复或拒绝后停止，不跨渠道追访。

**邀约话术核心**：说明目的 + 时长承诺（30分钟）+ 录屏说明 + 价值交换

### Step 3：访谈执行（30-45分钟）

**人员与记录**：1人主持、1人记录；录制和共享屏幕都需自愿同意，可选择口述或笔记，拒绝录制不影响参与。

**核心问题框架**：
1. **背景了解**：职业、获客渠道、使用时长、核心功能、竞品
2. **工作流探索**：解决什么问题？之前怎么做？现在有什么变化？
3. **竞品对比**：用了哪些竞品？各自场景？我们的优劣势？
4. **痛点挖掘**：不爽的地方？Bug？难用的功能？"魔法棒"问题
5. **付费意愿**：之前付费过什么？愿意付多少？什么促使升级？

**关键技巧**：屏幕共享观察 > 用户口述。让用户演示真实操作，观察卡点。

### Step 4：收尾与后续

- 大使计划邀请
- 转介绍请求
- 24小时内完成访谈复盘模板

**客户材料缺失时不要停摆**：会前用官网、公开案例和现有截图搭一个可讨论的粗版；会上直接让用户展示真实流程并索取已有材料。把缺失材料记为待验证项，不要把“客户回去整理完整资料”设为下一次学习的前置条件。

### Step 5：数据汇总（每5-10场）

汇总共同需求/痛点 → 更新功能优先级 → 修正用户画像 → 调整产品方向

---

## 有效访谈 vs 无效访谈判别（2026-07 增补）

主持人长篇讲产品会挤占观察真实任务的时间。

| 维度 | 无效访谈 | 有效访谈 |
|------|----------|----------|
| 谁在说 | 主持人持续推销，用户没有机会说明真实行为 | 听用户讲他是怎么用的 |
| 看什么 | 只听口述、看演示脚本 | 让用户共享屏幕，看真实操作 |
| 场景 | 假设场景 / 自己讲产品 | 真实场景、真实 user case |
| 心态 | 把用户当成纯粹的数字 | EGO 放低，和用户做朋友 |

**判别依据**：你构建的 user journey 和用户实际的 user journey 完全不一样——屏幕观察或参与者自愿提供的任务产物可帮助发现这个差异。

**付费意愿双逻辑**："访谈里说愿意付费和最终付费是两套逻辑"——一旦真要买单，每个人都理智得不行。访谈中的付费表态只作方向参考，验证一律以真实支付行为为准（对应下文"付费归因四时间戳"）。

---

## 访谈驱动迭代闭环

1. 先约 20–45 分钟，复杂任务经同意分段预约；不是越久越好。
2. 把真实操作、原话、主持人帮助和团队方案分开记录。
3. 产品、工程与研究共同按受阻价值、依赖和资源排序，不承诺修完全部意见。
4. 核实状态后回访，并让适当用户复测同一任务；上线不等于解决。
5. 按团队能完成分析与回访的能力安排频率，不设每日场数门槛。

---

## Beta 测试设计框架

### 测试目标三层结构

| 层级 | 维度 | 数据收集手段 |
|------|------|-------------|
| 价值验证层 | 是否解决核心痛点 | 访谈 |
| 体验感知层 | 速度、易用性、效果 | 观察法（屏幕录制/连线） |
| 缺口识别层 | 功能缺失、体验卡顿 | 结构化问卷 + Bug反馈 |

### 测试任务设计原则

- 任务模拟完整工作流，非孤立功能点
- 任务长度触发"等待"场景（暴露性能问题）
- 提供 prompt example 降低认知负担
- 明确说明"Beta不稳定是正常的"

### 连线实时测试核心

- 强调"观察"而非"测试用户"
- Think Aloud Protocol（边做边说）
- 利用加载等待期收集用户背景（被低估的技巧）

### 五问法（结构化收尾）

1. 你觉得这是一个怎样的产品？（让用户贴标签）
2. 最满意的功能是什么？
3. 哪个环节最卡顿或困惑？
4. 如果明天正式上线，你愿意付费吗？为什么？
5. 最希望下个版本加入什么？

---

## 冷启动用户运营方法论

### 冷启动漏斗与话术实验

触达 → 回复 → 到场 → 独立完成首次价值任务 → 留存 → 实际付款。逐步记录同 cohort、同窗口的去重人数；未知分母不报转化率。

以一条真实任务话术开始，比较功能描述、场景描述或痛点描述时保留样本、窗口和渠道差异，不预设哪种话术必胜。使用 [成本卡](references/cold-start-decision-card.md) 管理预算与继续/停止条件。

### 两层 Beta 用户体系

| 层级 | 画像 | 门槛 | 权益 |
|------|------|------|------|
| Tier 1 Creative Partners | KOL/行业专家 | 持续使用>7天 + 高质量反馈 | Pro权限 + 创始人直达 + Case Study |
| Tier 2 Early Beta Users | 符合ICP的专业用户 | 提交具体改进建议 | 早期访问 + 路线图参与 |

---

## 激活与付费基准（2026 实测）

### 访谈招募与首轮实验

按决策选择样本：收入研究需要付费/未付费对比，接入研究需要新用户，流失研究需要停止使用者。首轮先发 **10 条逐人定制消息**，记录回复、预约、到场和有效洞察，再决定是否扩量。访谈中优先让用户共享屏幕完成真实任务；观点必须与行为日志、激活和支付时间戳交叉验证。

下表仅是候选行为示例，必须验证是否对应本产品的首次价值，不能照搬次数。**激活定义必须是行为阈值**，不能是"注册过 / 登录过"：

| 产品类型 | 行为阈值实例 |
|----------|-------------|
| Agent 类 | 完成 ≥2 个任务 |
| 对话类 | 连续 3 天每天 ≥20 轮对话 |
| 工具类 | 开始跑任务，或单次使用超 5 分钟 |
| DAU 口径 | 以 unique message send 计，剔除内部用户 |

**目标与口径**：按产品阶段、渠道、用户 cohort 和观察窗口设目标，保留基线和假设；不使用固定注册付费比例认定合格或 PMF。

**流失**：按产品自然使用周期定义，短期未回访先作为信号。是否发送挽回消息按用户授权和联系偏好处理，不因一个时间阈值自动外发。

**付费时间线**：注册、激活、付款、最近使用时间用于整理先后顺序；时间相邻不能单独证明某次访谈或功能导致付款。

---

## 用户分级标准

| 等级 | 特征 | 运营策略 |
|------|------|----------|
| S级 | 高频 + 付费 + 愿意宣传 | 大使优先，CEO直接对接 |
| A级 | 高频 + 有付费潜力 | 内测优先权，定期回访 |
| B级 | 偶尔使用 + 无明确付费意向 | 引导核心功能，推动转化 |
| C级 | 低活跃 + 无付费意向 | 减少投入，关注自然留存 |

---

## 流失分析框架

| 流失类型 | 典型原因 |
|----------|----------|
| 性能类 | 设备过热/卡顿、加载超时、崩溃 |
| 工作流断层类 | 缺少下游集成、功能完成度不足 |
| ICP不匹配类 | 无数据主权、项目制无长期需求 |
| Messaging不匹配类 | 触达价值主张 ≠ 产品实际价值 |

**流失用户访谈三问**：
1. 什么时候开始不用的？当时在做什么？
2. 遇到了什么问题，还是找到了替代品？
3. 如果我们解决了X问题，你会回来吗？

---

## 用户采用条件

分别记录：真实任务频率、当前替代方案、输入/数据授权、使用者与购买者、切换成本及可观察结果。素材所有权可能影响某些内容产品的采用，但不代表通用 PMF 评级。找反例并复测，不按职业打星。

---

## 工具链

| 类别 | 工具 | 用途 |
|------|------|------|
| 问卷 | Typeform | 用户调研问卷 |
| 录音 | Grain, Fathom | 访谈录音转写 |
| 数据库 | Airtable | 用户数据库管理 |
| 日程 | Calendly | 预约访谈 |
| 触达 | LinkedIn, Discord | 用户联系与社区 |

---

## 完整参考文档

| 文档 | 内容 |
|------|------|
| [references/interview-guide.md](references/interview-guide.md) | 完整用户访谈指南（证据与抽样、问题框架、模板、FAQ） |
| [references/cold-start-ops.md](references/cold-start-ops.md) | Beta测试设计框架、冷启动用户运营、流失分析、可复用模板 |
| [references/templates.md](references/templates.md) | 访谈复盘模板、用户画像表、Feature Request Tracker |


## 访谈纠偏与冷启验收

访谈变推销、用户反向提问或主持人代操作时，读取 [纠偏与交接](references/interview-recovery.md)。研究要转为获客计划时，读取 [冷启动目标与成本卡](references/cold-start-decision-card.md)。按决策选择样本，不用访谈场数、问价或某个固定付费率证明 PMF。

<!-- gingiris-community-cta:start -->
## 加入出海社群与购买资料包 · Community & Resources

- **加入出海社群：** 微信添加 **staywildgrow**，留言「**加入社群**」即可。
- **购买资料包：** 微信添加 **staywildgrow**，咨询购买 Gingiris 出海资料包，价格 **599 元人民币**。

- **Join the global growth community:** Add **staywildgrow** on WeChat and send **“加入社群”** (join the community).
- **Get the resource pack:** Add **staywildgrow** on WeChat to purchase the Gingiris global growth resource pack for **CNY 599**.

社群与资料包为可选入口，不影响本开源 Skill 的安装和使用。

The community and paid resource pack are optional; neither is required to install or use this open-source skill.
<!-- gingiris-community-cta:end -->
