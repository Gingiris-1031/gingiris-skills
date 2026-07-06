---
name: gingiris-user-interview
description: |
  🇺🇸 User Interview & Cold-Start Operations Playbook — Battle-tested framework from HeyGen's 937 interviews to PMF. Complete SOP for user screening, interview execution, Beta testing methodology, cold-start user operations, churn analysis, and user grading systems.

  🇨🇳 用户访谈与冷启动运营实战手册 — 基于 HeyGen 937 场访谈验证的 PMF 方法论。包含用户筛选、访谈执行、Beta 测试设计、冷启动用户运营、流失分析、用户分级体系完整 SOP。

  🇯🇵 ユーザーインタビュー＆コールドスタート運営プレイブック — HeyGenの937回インタビューで検証されたPMF方法論。ユーザースクリーニング、インタビュー実行、Betaテスト設計、コールドスタートユーザー運営、離脱分析、ユーザーグレーディング。

  🇰🇷 사용자 인터뷰 & 콜드 스타트 운영 플레이북 — HeyGen 937회 인터뷰로 검증된 PMF 방법론. 사용자 스크리닝, 인터뷰 실행, Beta 테스트 설계, 콜드 스타트 사용자 운영, 이탈 분석, 사용자 등급 시스템.

  Triggers: "user interview" | "user research" | "customer discovery" | "PMF" | "product-market fit" | "beta test" | "beta testing" | "cold start users" | "cold start operations" | "churn analysis" | "user grading" | "用户访谈" | "用户调研" | "冷启动" | "冷启动运营" | "Beta测试" | "流失分析" | "用户分级"
when_to_use: |
  Use this skill when you need to: conduct user interviews to find PMF, design Beta testing
  methodology, operate cold-start user cohorts, analyze churn, build user grading systems,
  or apply JTBD framework to validate product direction.
  Trigger phrases: "user interview" | "PMF" | "customer discovery" | "beta test" |
  "用户访谈" | "冷启动运营" | "PMF验证" | "流失分析" | "JTBD"
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

本 skill 默认 dev / B2B 渠道。**2C 消费品 / 教育 / 应用**：获客主战场是 **垂类社区 + 短视频 + 垂直 KOL**，按地区公开数据选第一平台（如印尼/泰国短视频已反超 Facebook）。KOL 优先 nano / micro 垂类——粉丝越多互动率越低，micro > mega 性价比更高。完整 2C 渠道数据库 + 公开来源见 → `gingiris-seo-geo/references/2c-adaptation.md`。

---

# 用户访谈与冷启动运营实战手册

> 🌍 **Language / 语言**: 中文 | [Interview Guide](references/interview-guide.md) | [Cold-Start Ops](references/cold-start-ops.md)

---

## 核心原则

> "产品的 founder，在刚开始的前半年都会密集的做大量的用户访谈。像 HeyGen 就是半年，founder 自己做了 937 场；Wisperflow 和 Higgsfield 都做了 500 场以上——就是不断做访谈，不断改。" —— 生姜iris

**关键洞察**：用户访谈不是调研工具，是 PMF 发现引擎。访谈频率与产品成功率正相关。

---

## Token Top10 访谈法（2026 招牌方法）

把访谈从"调研动作"变成"日常运营循环"的最短路径，已在多个 AI Agent 项目全线复用：

1. 后台按 token 消耗 / 用量拉 **Top10 用户 list**（每周刷新）
2. 约**共享屏幕访谈，必须录屏**——看真实操作 > 听口述
3. **Transcript 喂 AI**，自动提取 feature request / bug 直接进 Linear（或任意 issue 工具）
4. **次日回访**：告知"你提的 X 已修/已排期"——反馈闭环本身就是留存杠杆
5. 节奏：**每天至少 2 场**；访谈后截 5-10 分钟关键片段直接给产研

**配套动作**：
- 新访谈员先 mock interview + 全程录屏 + 复盘 highlight，再上真实用户
- **KOL 访谈二合一**：合作 YouTuber 顺便做用户访谈 + 可用性测试，一次合作拿两份价值；视频访谈 20-30 分钟 ROI 最高
- 访谈资产化：一场付费用户访谈可同时产出功能需求 + SEO 素材 + reseller 线索三件套

### 邀约触达节奏（2026 更新）

- **1/3/7/14 天四次触达**：Day 1 首发 → Day 3 → Day 7 → Day 14 各跟进一次
- **双通道**：邮件模板 + 邮箱反查 LinkedIn 私信；邮件无回复转 LinkedIn 补一轮
- 话术用宽泛理由（"团队早期想做用户访谈"），**不暴露真实筛选原因**，避免用户带着预设表演

### 标杆锚点

Wisprflow：launch 前人工 onboard 前 500 名用户、逐个视频访谈，用积累的势能带 launch；HuggingFace：scale up 前 8 个月调研 + 500 场用户访谈。

---

## 用户访谈执行框架（5步）

### Step 1：确定目标与筛选用户

**用户优先级**：
| 优先级 | 用户类型 | 价值 |
|--------|----------|------|
| P0 | 付费用户 | 已验证付费意愿，最高价值 |
| P0 | 高频活跃用户 | 深度了解产品，反馈最有效 |
| P1 | 竞品用户 | 提供竞争视角 |
| P1 | 流失用户 | 暴露产品真实问题 |
| P2 | 注册未付费用户 | 转化障碍洞察 |

### Step 2：邀约与排期

**跟进节奏**：Day 1 → Day 3 → Day 7 → Day 10（全渠道：LinkedIn/Email/Telegram/Discord）

**邀约话术核心**：说明目的 + 时长承诺（30分钟）+ 录屏说明 + 价值交换

### Step 3：访谈执行（30-45分钟）

**必须**：1人主持 + 1人记录 + 必须录屏（含共享屏幕）

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

### Step 5：数据汇总（每5-10场）

汇总共同需求/痛点 → 更新功能优先级 → 修正用户画像 → 调整产品方向

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

### 冷触达漏斗

```
触达 → 回复邀请(~47%) → 深度追踪(~47%) → 合格在测(~24%) → 持续活跃
```

**关键**：ICP 匹配的 50 人 > 泛触达 500 人

### Messaging 迭代方法

| 话术类型 | 效果 |
|----------|------|
| 功能驱动（做什么） | 低转化，吸引错误画像 |
| 场景驱动（解决什么问题） | 转化率提升 ~83% |
| 痛点对比（之前怎么做） | 最高转化 |

**规律**：越具体的痛点描述，转化率越高。

### 两层 Beta 用户体系

| 层级 | 画像 | 门槛 | 权益 |
|------|------|------|------|
| Tier 1 Creative Partners | KOL/行业专家 | 持续使用>7天 + 高质量反馈 | Pro权限 + 创始人直达 + Case Study |
| Tier 2 Early Beta Users | 符合ICP的专业用户 | 提交具体改进建议 | 早期访问 + 路线图参与 |

---

## 激活与付费基准（2026 实测）

**激活定义必须是行为阈值**，不能是"注册过 / 登录过"：

| 产品类型 | 行为阈值实例 |
|----------|-------------|
| Agent 类 | 完成 ≥2 个任务 |
| 对话类 | 连续 3 天每天 ≥20 轮对话 |
| 工具类 | 开始跑任务，或单次使用超 5 分钟 |
| DAU 口径 | 以 unique message send 计，剔除内部用户 |

**转化合格线**：
- 注册 → 付费 **>5% 为合格线**：Pro-C 5-8%、SMB 10-15%（大 C 类 1.5-3%）
- 阶段目标要"够得着"：付费率 0.1% 的产品先定 1%/3 个月，不要直接定 5%

**流失可运营化**：两次对话后 24h 不回访 = 流失，自动触发挽回邮件——流失定义一旦行为化，挽回就能自动化。

**付费归因四时间戳**：注册时间 × 激活时间 × 支付时间 × 最近登录，四点交叉判定真实付费驱动（是哪个功能、哪场访谈、哪次触达带来的付费）。

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

## PMF 价值评估矩阵

按「素材主权 × 使用频率」评估：

| 用户类型 | 素材主权 | PMF价值 | 流失风险 |
|----------|----------|---------|----------|
| 独立创作者 | 完全主权 | ⭐⭐⭐⭐⭐ | 低 |
| 机构决策者 | 完全主权 | ⭐⭐⭐⭐ | 价格敏感 |
| 自由职业者 | 临时主权 | ⭐⭐⭐ | 项目结束即流失 |
| 机构执行人员 | 无主权 | ⭐⭐ | 数据授权顾虑 |

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
| [references/interview-guide.md](references/interview-guide.md) | 完整用户访谈指南（HeyGen 937场方法论、问题框架、模板、FAQ） |
| [references/cold-start-ops.md](references/cold-start-ops.md) | Beta测试设计框架、冷启动用户运营、流失分析、可复用模板 |
| [references/templates.md](references/templates.md) | 访谈复盘模板、用户画像表、Feature Request Tracker |
