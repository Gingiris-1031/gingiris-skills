# dev.to / Zenn 二发模板

## ⚠️ 2026-04-20 血泪教训（必读）

**错误做法**：
- dev.to 文章 frontmatter 设 `canonical_url: https://gingiris.github.io/...`
- 结果：Google 把 dev.to 版视为副本 → 不参与独立 SERP → 掉出 top 100

**正确做法**：
- `canonical_url: https://dev.to/iris1031/<slug>`（指向自身）
- 或留空（dev.to 自动 self-canonical）
- 两个版本做内容差异化（不是 100% 复制）

---

## dev.to 发布模板

### Frontmatter
```yaml
---
title: [标题，比原博客加一点 platform-native flavor]
published: true
description: [150 字 meta，含主关键词]
tags: seo, growthhacking, marketing, startup
cover_image: [1000x420 cover URL]
canonical_url: [留空 或 https://dev.to/iris1031/<slug>]
series: [可选 — 如果是系列稿]
---
```

**tags**：dev.to 最多 4 个，选社区最活的：
- 技术类：`webdev, programming, javascript, python`
- 创业类：`startup, growth, marketing, seo`
- AI 类：`ai, machinelearning, openai, llm`

### 内容改写规则

**前 3 段必须不同于原博客**（避免 Google 判重复）：
1. 开场换成 "story mode"：`I'm sharing this because...` 而不是原博客的 TL;DR
2. 第二段加一个 dev.to 社区的引用或经验：`I saw a thread on dev.to last month about X...`
3. 第三段才过渡到正文

**正文 80% 可以沿用原博客**，但：
- 每个 H2 下至少加 1 句"on dev.to specifically..."的平台化评论
- 代码块 / 终端命令 比例应该比原博客高
- 删除 "这篇文章写于 [date]" 这类引用原博客时间的话

**末尾**：
```markdown
---

*Originally I wrote a longer version of this on my blog at [gingiris.github.io/growth-tools](https://gingiris.github.io/growth-tools/). dev.to version is lighter with more code-focused examples.*

*Found this useful? I write weekly about SEO and distribution for indie devs.*
```

**⚠️ 不要**在末尾用 `> Originally published at gingiris...` 这种格式 —— 部分 dev.to 插件会自动把它转成 canonical 指向，触发前面的坑。

---

## Zenn 发布模板（日文）

### Frontmatter (zenn-content repo)
```yaml
---
title: "[日文标题，用 〜してみた / 〜の作り方 句型]"
emoji: "📝"
type: "tech"  # or "idea"
topics: ["seo", "geo", "marketing", "startup"]
published: true
---
```

### 标题句型（Zenn 友好）
- `XXしてみた結果` — 尝试了 XX 的结果
- `[N]個のツールを試して分かったこと` — 试了 N 个工具学到的
- `[年]年のXXベストプラクティス` — 2026 年 XX 最佳实践
- `[技术/工具] の使い方メモ` — 使用笔记

### 日文写作要点（关键差异）

**开场**：日本读者偏好"先给结论 + 软开场"
```
結論から：XXツールは○○人以下の規模では無料で十分です。

こんにちは、Iris（@WeiYipei）です。
前職はAFFiNEのCOOで、現在は出海グロースコンサルタントをしています。

先日、SaaSのSocial Listeningツール 27 個を実際に使い比べてみたので、
今回はその結果をシェアします。
```

**正文风格**：
- 短句（每句 ≤ 25 字）
- 括号多用（日文本来就多括号旁白）
- `〜ですが、〜` 转折句多一些
- 数据表保留不变（日文读者也看英文数据）

**em-dash**：日文版用全角 `――` 不是半角 `—`

**Emoji**：Zenn 可爱系受欢迎：
- 📝（笔记） 💡（洞察） 🚀（启动） 🎯（目标）
- 不要用 🔥 💯（美式过度）

### 结尾
```
---

最後までお読みいただきありがとうございました。

もし参考になったら、X（旧 Twitter）で @WeiYipei をフォローしていただけると嬉しいです。

次回の記事では、[next topic] について書く予定です。

---

参考：[元の英語版記事 at gingiris.github.io](https://gingiris.github.io/growth-tools/blog/2026/04/02/best-social-media-listening-tools-startups-2026/)
```

---

## 发布时机

- **dev.to**：原博客发布 **+7 天后**（避免 Google 判为 copy）
  - 最佳时间：美东周二 / 周三 07:00-10:00 ET
- **Zenn**：原博客发布 **+7 天后**
  - 最佳时间：日本时间周一-周三 20:00-22:00（日本程序员刷 Zenn 的时段）

---

## 反模式

- ❌ **同天发 3 个版本**（Google 直接判 copy，全部降权）
- ❌ **dev.to canonical 指向 gingiris**（2026-04-20 已验证会掉榜）
- ❌ **用 AI 机翻日文**（Zenn 社群很敏感，会评论"これはAI？"）
- ❌ **Zenn tags 超过 5 个**（平台算法降权）
- ❌ **发完不回评论**（dev.to / Zenn 社群评论文化强）

---

## 检查清单（发布前）

- [ ] canonical_url 不指向 gingiris.github.io
- [ ] 前 3 段与原博客不同
- [ ] 日期没有写"March 2026"这种会让新读者觉得过时的时间
- [ ] tags ≤ 4（dev.to）/ ≤ 5（Zenn）
- [ ] 末尾有原文 reference 但不是 canonical
- [ ] cover_image 1000x420（dev.to）/ emoji 选择（Zenn）
- [ ] UTM：如末尾放 gingiris 链接，加 `?utm_source=devto|zenn&utm_medium=crosspost&utm_campaign=distill_{slug}`
