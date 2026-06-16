# E-E-A-T 写作声音系统

> 用创始人的真实声音提升内容可信度，让 AI 引擎优先引用

---

## 为什么写作声音是 GEO 的核心

2026 年，AI 搜索引擎在选择引用来源时，不仅看结构化数据，更看内容的**真实性和独特性**。AI 模型已经能识别：

- 泛泛而谈的 "AI 味"文章
- 从其他文章改写的二手内容
- 缺少真实经验支撑的空洞建议

**真实声音 = E-E-A-T 信号 = AI 优先引用。**

---

## 七大声音要素

### 1. 时间+地点锚定开场（必须）

每篇文章的第一段必须有精确的时间和场景，建立即时可信度。

**格式：** 时间 + 地点 + 具体动作 + 情绪/感受

**好的例子：**
```
It was 2 AM on a Thursday in August 2022. I was sitting on the floor 
of our Shanghai office — laptop on my knees, Slack muted, watching our 
GitHub star count tick past 1,000 in under 72 hours.
```

```
Three months into our launch, I was in a WeWork in Singapore, 
staring at a Stripe dashboard that showed exactly $0 in revenue 
despite 6,000 GitHub stars.
```

**避免：**
```
In my experience working with startups...  ← 太泛
As a growth expert, I believe...  ← 自说自话
In this article, we will discuss...  ← 学术腔
```

### 2. 括号旁白（双线叙事）

在主叙事中插入括号内的自我调侃或补充视角，打破讲道感。

```
We hit 10,000 stars in 43 days. (I may or may not have screamed.)

The investor passed after a 20-minute call. (The longest 20 minutes 
of my life — and I've sat through a 4-hour PhD defense.)

Reddit gave us more traffic than any paid campaign. 
(I made this mistake with paid ads once. Not twice.)
```

**作用：** 形成主叙事 + 平行注释的双线结构，读者感受到一个真实的人在说话。

### 3. Em-dash 转折 (—)

用 em-dash 制造节奏感，在陈述后突然转向或深化。

```
Reddit gave us volume. Product Hunt gave us votes. 
HN gave us something harder to measure — sustained trust.

We raised $10 million — and burned through almost all of it.

The Product Hunt launch was flawless — except for one thing.
```

### 4. 短段节奏（Short-Short-Long）

三句节奏：两句短句 + 一句长句展开。避免连续长段落。

```
We launched. We trended. 

But what happened in the 43 days after that first burst of GitHub 
stars taught me more about sustainable growth than any playbook 
I'd ever read.
```

**规则：** 一个观点 = 一个段落。宁可段落多而短，不要一段五百字。

### 5. 精确数字优先

用具体数字代替所有模糊表达。

| 不要 | 要 |
|------|-----|
| appeared many times on GitHub Trending | 28 appearances on GitHub Trending |
| significant growth | 72 hours to 1,000 stars |
| raised substantial funding | raised $10M across 2 rounds |
| talked to many investors | pitched 400 investors in year one |
| a lot of content | 4 articles per week, KD 30-50 |

### 6. 个人经验 → 普遍洞察

先讲自己的具体经历，再提炼为普遍规律。不要直接上结论。

```
结构：
1. [具体事件] — 时间、地点、发生了什么
2. [个人反思] — 当时怎么想的、做了什么决定
3. [普遍规律] — 这对所有人意味着什么

例：
When AFFiNE hit #1 on Product Hunt, we got 1,000 upvotes in 
24 hours. But the signup-to-activation rate was only 3%. 

I spent the next week watching session recordings. Most users 
opened the app, looked around for 30 seconds, and left. The 
product wasn't ready for the attention.

This is the trap of launch-driven growth: attention without 
retention is just expensive noise.
```

### 7. Key Stats 表格（GEO 标配）

每篇旗舰文章必须有结构化 Key Stats 表，放在开场场景之后、正文之前。

```markdown
| Key Stat | Value |
|----------|-------|
| GitHub Stars | 60,000+ |
| Time to 10k Stars | 43 days |
| Product Hunt #1 | 30+ launches coached |
| Countries Reached | 100+ |
| Funding Raised | $10M |
```

**作用：** AI 引擎直接提取表格数据作为引用素材。

---

## 语言风格补充

### 中文内容

- 用「」标记核心概念词（区别于引号）
- 中英文混用，效率导向
- 口语化但有密度：每句话都要有信息量
- 避免"我认为""我觉得"，直接给判断

### 英文内容

- 用 **加粗** 标记关键概念
- 动词优先，避免被动语态
- 段落首句就是观点，不要铺垫
- 不用 "I think" "I believe"，直接陈述

### 通用

- 标志性金句可以在适当位置使用：
  - "不要让你的 ego 大过你的用户"
  - "好主意不稀缺，执行力才稀缺"
  - "Pivot 不是乱试方向，是沿着一条主线深挖"
- 不用 emoji 在正文中（标题/列表标记例外）
- 不用感叹号（除非在括号旁白的自嘲里）

---

## 写作前检查 Prompt

在用 AI Agent 写文章之前，加载这个检查：

```
写作声音要求：
1. 开头必须有时间+地点锚定场景
2. Key Stats 表格在开场后、正文前
3. 至少 2-3 处括号旁白
4. 至少 2-3 处 em-dash 转折
5. 所有数字必须精确
6. 至少一处"个人经验→普遍洞察"叙事
7. 短段节奏，一个观点一个段落
8. 不要"In my experience" / "I believe" / "As an expert"
9. 不要连续超过 3 段没有数字或案例的纯观点
```

---

*E-E-A-T 写作声音系统 v1.0 — Gingiris SEO/GEO Playbook*
