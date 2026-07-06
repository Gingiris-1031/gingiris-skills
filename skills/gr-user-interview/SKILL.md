---
name: gr-user-interview
description: >
  用户访谈框架。HeyGen 做 937 次访谈找到 PMF 的完整方法论。覆盖访谈招募、问题设计、
  访谈执行、数据合成、决策驱动。从 gingiris-user-interview 提炼。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
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

本 skill 默认 dev / B2B 渠道。**2C 消费品 / 教育 / 应用**：获客主战场是 **垂类社区 + 短视频 + 垂直 KOL**，按地区公开数据选第一平台（如印尼/泰国短视频已反超 Facebook）。KOL 优先 nano / micro 垂类——粉丝越多互动率越低，micro > mega 性价比更高。完整 2C 渠道数据库 + 公开来源见 → `gingiris-seo-geo/references/2c-adaptation.md`。

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

## 核心原则（5 条）

1. **问 behavior，不问 opinion**
   ❌ "你会用这个功能吗？" → 会得到礼貌性"yes"
   ✅ "上次遇到 X 问题是什么时候？你当时做了什么？" → 得到真实行为

2. **20 分钟访谈 >> 5 个 feature 问题**
   深度一个场景，比问 5 个浅问题更有价值

3. **录音 / 整稿 > 当场记笔记**
   当场记会错过微表情和语气

4. **5 人后暂停，复盘**
   不要连访 20 人才总结，5 人后大概率已看到模式

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

**后台用量 Top10 拉 list → 共享屏幕访谈（必录屏）→ transcript 喂 AI 提 feature/bug 进 Linear → 次日回访。每天 ≥2 场。**

1. 按 token 消耗 / 用量排 Top10，每周刷新——重度用户的反馈密度最高
2. 必须共享屏幕 + 录屏：看真实操作 > 听口述
3. Transcript 交给 AI 自动提取 feature request / bug，直接进 issue 工具
4. 次日回访"你提的 X 已修/已排期"——反馈闭环就是留存杠杆
5. 访谈后截 5-10 分钟关键片段给产研

**邀约节奏**：
- **1/3/7/14 天四次触达**（Day 1 → 3 → 7 → 14 各跟进一次）
- 双通道：邮件模板 + 邮箱反查 LinkedIn 私信，邮件没回转 LinkedIn 补一轮
- 话术用宽泛理由（"早期团队想做访谈"），不暴露真实筛选原因——避免用户表演

**组合技**：
- KOL 访谈二合一：合作 YouTuber 顺便做用户访谈 + 可用性测试，一次合作两份价值（20-30 分钟视频访谈 ROI 最高）
- Wisprflow 打法：launch 前人工 onboard 前 500 用户逐个访谈，用势能带 launch

---

## 激活基准速查

| 项 | 基准 |
|---|---|
| 激活定义 | 必须是**行为阈值**：完成 ≥2 任务 / 连续 3 天 ≥20 轮对话 / 使用超 5 分钟——不是"登录过" |
| 注册 → 付费合格线 | **>5%**（Pro-C 5-8%、SMB 10-15%） |
| 流失定义 | 两次对话后 24h 不回访 = 流失 → 自动触发挽回邮件 |
| 付费归因 | 四时间戳交叉：注册 × 激活 × 支付 × 最近登录 |

---

## 深度参考

📂 **https://github.com/Gingiris/gingiris-user-interview**

- `references/templates.md` — 不同阶段（Discovery / Validation / Retention）的问题模板
- HeyGen 937 访谈案例拆解

---

## 合成流程

1. 每次访谈后 24h 内整理 3 张卡片：
   - **Pain**（用户的真实痛）
   - **Workaround**（他们目前怎么凑合）
   - **Quote**（可引用的原话）
2. 每 5 个访谈做一次复盘：
   - 重复出现 ≥ 3 次的 Pain → 候选 PMF 方向
   - 重复出现 ≥ 2 次的 Workaround → 竞品信号
3. 每 20 个访谈做一次决策：
   - 继续这个假设 / 换方向 / 需要更多数据

---

## 级联推荐

- 访谈发现新 PMF 方向 → `gr-blog-post` 写一篇（验证市场反应）
- 访谈发现对手名字被提 ≥ 3 次 → `gr-competitor` 深度分析
- PMF 明确 → `gr-b2b-growth` 或 `gr-oss-marketing` 启动增长
- 需要招募访谈对象 → 从 `gr-seo-patrol` 的 GSC 流量挑读者，或直接上「Token Top10 访谈法」拉后台用量榜
- 在跑红人合作 → 用「KOL 访谈二合一」顺路拿访谈（红人打法见 `gingiris-kol-outreach`）
- 访谈后要定激活/付费目标 → 对照上方「激活基准速查」先把行为阈值写死

---

## 反模式

- ❌ 问 "你愿意付费吗" → 100% 是假答案
- ❌ 发问卷替代访谈（信息密度差 10x）
- ❌ 只访现有用户不访流失用户（流失才是真金）
- ❌ 一次访谈超过 45 分钟（疲劳 → 敷衍）
- ❌ 访谈中推销自己产品（污染答案）
- ❌ 邀约只发一次就放弃（1/3/7/14 四次触达才是基线）
- ❌ 邀约话术暴露筛选原因（"因为你用量高所以找你" → 用户开始表演）
- ❌ 激活定义写成"注册/登录过"（必须是行为阈值）
- ❌ 访谈完不回访（次日回访"已修/已排期"是最便宜的留存动作）
