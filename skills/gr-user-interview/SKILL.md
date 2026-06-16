---
name: gr-user-interview
description: >
  用户访谈框架。HeyGen 做 937 次访谈找到 PMF 的完整方法论。覆盖访谈招募、问题设计、
  访谈执行、数据合成、决策驱动。从 gingiris-user-interview 提炼。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-user-interview
---

# gr-user-interview — 用户访谈

## 什么时候用

- "我要找 PMF，怎么做访谈"
- "用户反馈很杂，不知道抓哪个"
- "我采访了 5 个人，都没 insight"
- "怎么避免用户说假话"

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
- 需要招募访谈对象 → 从 `gr-seo-patrol` 的 GSC 流量挑读者

---

## 反模式

- ❌ 问 "你愿意付费吗" → 100% 是假答案
- ❌ 发问卷替代访谈（信息密度差 10x）
- ❌ 只访现有用户不访流失用户（流失才是真金）
- ❌ 一次访谈超过 45 分钟（疲劳 → 敷衍）
- ❌ 访谈中推销自己产品（污染答案）
