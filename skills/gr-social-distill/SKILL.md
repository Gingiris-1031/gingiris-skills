---
name: gr-social-distill
description: >
  把一篇已发布的博客拆成 4 个社媒变体：X thread（10-15 推）、小红书笔记（3-5 图）、LinkedIn carousel、
  dev.to / Zenn 二发。目标：在不新写博客的前提下激活 Organic Social 分发渠道。
  当用户说"把这篇博客改成推特"、"做小红书版本"、"社媒分发"、"复用博客到多平台"时调用。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  companion-to: gr-blog-post
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr-social-distill
---

# gr-social-distill — 博客到社媒复用

## 核心理念

**复用 > 新创**。已发 60 篇博客，但社媒只用了一次的话，下一步 ROI 最高的不是写新文，是拆变体（来源：原子库 2026Q2_016）。

一篇 2000-3500 字的博客 → 4 种社媒格式 → **4x 流量放大**，而且不需要新内容灵感。

---

## 什么时候用

| 场景 | 动作 |
|---|---|
| "把这篇博客拆成 X thread" | X 模板（见下） |
| "做小红书版本" | 小红书模板（75 公式标题） |
| "LinkedIn 怎么发" | LinkedIn carousel 模板（仅 B2B 内容） |
| "dev.to / Zenn 二发" | 技术博客跨平台模板 |
| "每周分发节奏" | 完整 workflow（1 篇博客 → 4 变体） |

---

## 输入

- 1 个已发布博客 URL 或 `_posts/` 文件名
- 可选：目标渠道（X / xhs / LinkedIn / dev.to / Zenn / all）

## 输出

按渠道产出对应 markdown 或 draft 文本，直接可发。

---

## 4 渠道模板

### 1️⃣ X thread（10-15 推）

**结构**：
```
[推 1 — HOOK] 一个反常识 / 数据 / 问题引入（≤ 280 字，是否有吸引力决定全盘）
[推 2 — STAKES] 我 X 个月踩过 Y 个坑，结论是...
[推 3-12 — BODY] 每推一个要点。每推 ≤ 280 字。用短句。
[推 13 — TL;DR] 回到 HOOK 的答案
[推 14 — LINK] 链接到原博客 + 1 句 why it's worth clicking
[推 15 — CTA] @WeiYipei if you want the template
```

**原则**：
- 每推独立成立，单独截图也能被转发
- 用具体数字代替形容词（"30 天内" vs "很快"）
- 每 3-4 推插 1 张截图 / 表格
- Hook 句型参考：
  - "Here's what 60 blog posts taught me about X:"
  - "I analyzed 27 X tools. 22 of them aren't worth $0."
  - "Stop doing X. I tried it for 90 days. Data:"

详细例句库见 `templates/x-thread.md`。

---

### 2️⃣ 小红书笔记（3-5 张图）

**标题公式**（75 爆款公式，抄 dbs-xhs-title）：
- 数字派："我测了 27 个 XX 工具，只有 4 个真的免费好用"
- 踩坑派："别再用 XX 了，我花 3 万块换的教训"
- 教程派："手把手教你 5 步搞定 XX（附工具清单）"
- 反差派："用了 3 年 XX，结果发现 Y 才是真香"
- 揭秘派："做 XX 的人不会告诉你的 3 件事"

**内容结构**（每篇 < 1000 字）：
- 开头 100 字：钩子 + 痛点共鸣
- 正文 600 字：3-5 个要点，每个 100-200 字
- 结尾 100 字：TL;DR + 互动问题
- 加 5-8 个相关 tag：`#出海创业 #SaaS增长 #独立开发者 ...`

**配图**（3-5 张）：
- 图 1：标题图（大字标题 + 关键数字）
- 图 2-4：每张 1 个要点（用手机截图 + 红笔框关键词）
- 图 5（可选）：数据表 / 对比图

详细模板见 `templates/xhs-note.md`。

---

### 3️⃣ LinkedIn carousel（仅 B2B / 技术文）

**触发条件**：原博客是 B2B / 企业 / 开发者向内容才发 LinkedIn，ToC 内容跳过。

**10 页 carousel 结构**：
- 页 1：标题（"How we [result] in [time]"，配 key visual）
- 页 2：问题定义（读者 why care）
- 页 3-8：6 个步骤 / 要点，每页 1 个
- 页 9：数据结果（before/after 对比）
- 页 10：CTA（关注 + 链接到原博客）

**每页内容**：
- 大字标题（≤ 40 字）
- 3-5 条 bullet（≤ 10 字 / 条）
- 配图 / icon / chart

**正文（caption 500-1000 字）**：
- 开头 3 行抓住注意（LinkedIn 折叠显示）
- 正文讲"我学到什么"（不是"工具有什么功能"）
- 结尾问问题引评论

详细模板见 `templates/linkedin-carousel.md`。

---

### 4️⃣ dev.to / Zenn 二发

**适用**：原博客是技术向（SEO / GEO / API / 代码 / 工具）

**关键规则**（从 2026-04-20 dev.to 掉榜事件学到）：
- ⚠️ **canonical_url 必须指向 dev.to 自身**，不要指向 gingiris.github.io
  - 错误做法：`canonical_url: https://gingiris.github.io/growth-tools/...`
  - 正确做法：`canonical_url: https://dev.to/iris1031/...` 或留空
  - 原因：canonical 指向主站 → Google 把 dev.to 版视为副本 → 不参与独立 SERP
- **发布时间差 ≥ 7 天**（不要同天发，避免 Google 认为 copy）
- **内容做本地化变化**：改开场 hook、加 1-2 段 dev.to 用户视角的评论
- **末尾加"Originally I wrote this for my blog at gingiris.com"**（建立双向 reference，但不用 canonical）

**Zenn 特殊**：
- frontmatter `type: tech` 技术文 / `type: idea` 观点文
- 日文版本优先，标题用"〜してみた" / "〜の作り方"等日式句型
- emoji 系统选可爱一点的（📝 / 🚀 / 💡）

详细模板见 `templates/devto-zenn.md`。

---

## 每周工作流（Phase 2 主线 2 的节奏）

```
每周一 10:00
    ↓
从 gr-seo-patrol 输出里挑：
- Organic Search 流量 top 3
- 或：最近 30 天新发且排名 top 30 的
    ↓
选 1 篇"高潜力博客"作为本周分发源
    ↓
产出 4 变体（X / xhs / LinkedIn / dev.to）
    ↓
分散发布：
- 周一：X thread
- 周三：小红书笔记
- 周五：LinkedIn carousel（如 B2B）
- 次周周一：dev.to / Zenn 二发（延迟 7 天）
    ↓
下周一：复盘
- 哪个渠道带回了多少 GA4 referral？
- 哪个变体互动率最高？
- 更新 MEMORY 里的分发 playbook
```

---

## 追踪成效

发布后每个变体记录 UTM：
```
?utm_source=x|xhs|linkedin|devto&utm_medium=social&utm_campaign=distill_{post-slug}
```

GA4 Referral 报告里按 `utm_source` 分组，判断每个渠道 ROI。

---

## 级联推荐

- 变体发完后 24h → `gr-seo-patrol` 看 Organic Social 占比是否上涨
- 发现某个渠道 ROI 特别高 → 下周加码（同渠道多发 2 篇）
- 小红书爆款 → 考虑做矩阵号（联动 `gr-aso` AI 矩阵号模式）
- dev.to 排名上来 → 确认 canonical 配置，避免重蹈覆辙

---

## 反模式

- ❌ **同一天 4 渠道齐发** —— 你自己的读者重复看到同内容会反感
- ❌ **原文复制粘贴** —— X / xhs / LinkedIn 每个渠道有自己的语境，照搬互动率差 10x
- ❌ **dev.to canonical 指向主站** —— 2026-04-20 血泪教训，永远 self-canonical
- ❌ **LinkedIn 发 ToC 内容** —— 严重不匹配平台受众
- ❌ **小红书加外链**（平台严重降权 —— 把 URL 改成"主页简介找链接"）
- ❌ **一次拆完 10 篇**，堆积在 draft 里不发 —— 宁可 1 篇完整分发 > 10 篇半成品
