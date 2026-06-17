---
name: gr-readme
description: |
  🇺🇸 GitHub README Writing System — Craft a README that converts visitors to stars in <3 seconds. Proven structure from AFFiNE's 0→60K star journey: tagline engineering, first-screen law, section-by-section copywriting guide, anti-patterns, and a pre-publish checklist. Use when you need to write or rewrite a specific README file.

  🇨🇳 GitHub README 写作系统 — 打造 3 秒内把访客转化为 star 的 README。来自 AFFiNE 0→60K star 实战：tagline 工程、首屏法则、逐节文案指南、反模式、发布前自检清单。需要写或改一个具体 README 文件时使用。

  🇯🇵 GitHub README 作成システム — 3秒以内にビジターをスターに変えるREADMEを作る。AFFiNE 0→60Kスター実績から: タグライン設計、ファーストスクリーン法則、セクション別ライティングガイド、アンチパターン、公開前チェックリスト。

  🇰🇷 GitHub README 작성 시스템 — 3초 안에 방문자를 스타로 전환하는 README 작성법. AFFiNE 0→60K 스타 실전: 태그라인 설계, 첫 화면 법칙, 섹션별 카피라이팅 가이드, 안티패턴, 게시 전 체크리스트.

  Triggers: "write README" | "README template" | "GitHub README" | "project description" | "tagline" | "open source README" | "README structure" | "README写作" | "写README" | "README模板" | "项目介绍" | "开源项目文案" | "README 구조" | "README 작성" | "READMEの書き方"
when_to_use: |
  Use this skill when the task is to WRITE or REWRITE a specific README file — drafting
  taglines, structuring sections, copywriting feature descriptions, fixing a weak README,
  or running a pre-publish review.

  NOT for: overall open-source growth strategy, choosing launch channels, Show HN tactics,
  star-farming prevention, KOL outreach, or 6-month OSS growth loops — that's gingiris-opensource.

  One-line distinction: gr-readme = writing the document | gingiris-opensource = the entire growth strategy that the document lives inside.

  Trigger phrases: "write README" | "README template" | "rewrite README" | "tagline" |
  "project description" | "README review" | "README写作" | "写README" | "README检查"
tags:
  - github-readme
  - open-source
  - developer-marketing
  - copywriting
  - tagline
  - documentation
  - developer-tools
  - oss
---

# GitHub README Writing System

> Built from taking AFFiNE from 0 to 60K stars. The README didn't just describe the product — it *was* the product for the first 30 days.
>
> — (AFFiNE case, Iris Wei @WeiYipei, ep01/ep03/ep06)

---

## 核心原则 / Core Principles

### 原则 1：README 是产品的第一个着陆页 / README is your product's first landing page

The README has one job: convert a GitHub visitor into a star, fork, or install within **3 seconds of first scroll**. Everything else is secondary.

README 只有一个任务：在访客第一次滚动页面的 **3 秒内**，把他转化成 star、fork 或安装行为。其他都是次要的。

### 原则 2：产品没做好也不妨碍 README 做好 / A weak product can still have a great README

> AFFiNE 开源时产品还是「套壳」demo，README 写对了照样火。
> — (AFFiNE case, Iris Wei @WeiYipei, ep03/ep06)

The README is your narrative. You're selling the *vision and the pain point solved*, not the current feature set. A product at 30% completion with a clear "why you need this" README will outperform a finished product with a feature dump.

### 原则 3：英文主，首屏 <3 秒读懂 / English-first, first screen readable in <3 seconds

> README 英文主，首屏 <3 秒读懂。
> — (AFFiNE case, Iris Wei @WeiYipei, ep03)

The first scroll of a GitHub page is approximately 600–800px. Everything above the fold must answer: **What is this? Why does it matter? Who is it for?** If those three questions aren't answered before the first scroll, you've already lost most visitors.

---

## README 结构框架 / README Structure Framework

Derived from analysis of insforge (agentic coding backend) and dify (60K+ star LLM platform), and validated against AFFiNE's 0→60K growth.

```
[Logo + Project Name]
[One-line Tagline]              ← 最关键，不可跳过
[Badges]                        ← 信号，不是装饰
[Hero image / Demo video]       ← 30秒内展示产品
[What is this? / 2-3 sentences] ← 首屏核心
[Quick Start]                   ← 越短越好，能跑就行
[Key Features]                  ← 按用户痛点排序，不是技术清单
[Architecture / How it works]   ← 可选，复杂项目用
[Deployment options]            ← 云、本地、一键部署
[Contributing]                  ← 简短，指向 CONTRIBUTING.md
[Community & Support]           ← Discord / X / Discussions
[License]
[Star History]                  ← 社会证明，放底部
```

---

## 首屏 3 秒法则 / The 3-Second First Screen Law

**The rule:** Everything above the first scroll must answer three questions without requiring the reader to think.

| Question | Where to answer |
|----------|----------------|
| What is this? | Tagline (1 sentence) |
| Why should I care? | Sub-description or problem statement (2–3 sentences) |
| Is it real / trustworthy? | Badges: stars, license, downloads, last commit |

**What insforge does right:** Logo → one-line tagline ("The all-in-one, open-source backend platform for agentic coding") → demo video → 3-sentence expansion. The tagline is immediately scannable. The demo video shows the product without words.

**What dify does right:** Hero image → minimal badge row → dense 1-paragraph description that names 7 specific features in plain language. Jumps straight to Quick Start — the most important CTA for developers.

**Common failure mode:** Putting a verbose "About this project" paragraph before anything visual. Developers don't read introductions — they scan for signals that tell them whether to invest 5 more seconds.

---

## 各板块写法指南 / Section-by-Section Writing Guide

---

### Section 1: Tagline

**这是整个 README 最重要的一行。**

A great tagline does three things simultaneously:
1. Names what the product *is* (category)
2. Names who it's *for* (audience)
3. Names the *pain it kills* (problem)

**AFFiNE 案例 / AFFiNE Case:**

> Tagline: "Open source Notion alternative"
>
> 命中三个用户痛点：Notion 离线不可用、数据导出难、隐私问题。
> Hit three user pain points: Notion can't work offline, poor data export, privacy concerns.
>
> — (AFFiNE case, Iris Wei @WeiYipei, ep01)

This tagline works because it borrows Notion's brand awareness (no explanation needed for what it does), and the word "alternative" signals three things at once: open-source, self-hostable, and "I have the same features but without the things you hate."

**Tagline formula options:**

```
[Adjective] [category] for [audience]
e.g. "Open-source backend platform for AI coding agents"

[Category] without [pain point]
e.g. "Note-taking without the cloud lock-in"

[Familiar thing] + [key differentiator]
e.g. "Notion alternative — open source, offline-first, privacy-focused"

[Verb phrase that describes the outcome]
e.g. "Ship full-stack apps from your AI agent, end to end"
```

**Rules:**
- ≤ 12 words
- No jargon that requires prior knowledge of your project
- Must work without context — imagine someone sees just this one line
- Never start with "A powerful..." or "An amazing..." — these are signals that the writer doesn't know what makes their product special

---

### Section 2: Hero Image / Demo Video

**Show before you tell.**

A 30–60 second demo video reduces the cognitive load of reading by 80%. If you don't have a video, a high-quality screenshot or GIF showing actual product use is non-negotiable for anything with a UI.

For CLI / SDK tools (like insforge): a `mermaid` architecture diagram + installation command is the equivalent.

**Rules:**
- Video ≤ 60 seconds, captioned (non-English speakers are a large part of your audience)
- Screenshot should show the product *in use*, not an empty state
- Dark and light mode variants if your product supports it
- Host on GitHub's own CDN (drag into the issue editor) — don't use external CDN that might break

---

### Section 3: Quick Start

**This section's only job is to get the user to a running instance as fast as possible.**

The pattern that works:

```bash
# 3-5 commands max. No explanations between commands.
git clone https://github.com/yourorg/yourrepo
cd yourrepo
docker compose up -d
# → open http://localhost:3000
```

**Rules:**
- If setup takes >5 commands, something is wrong with your onboarding, not the README
- Prerequisites go *above* the commands, not buried in a footnote
- Provide a cloud/hosted version link as an alternative — "Don't want to self-host? Try cloud.yourproject.com"
- The commands must actually work on a fresh machine. Test this.

**What dify does right here:** The Quick Start section is the *second thing in the README* after the description. It shows minimum system requirements (CPU/RAM), then 4 commands. No essay, no architecture explanation first. Get them running, then explain.

---

### Section 4: Key Features

**Sort by user pain, not technical implementation.**

Wrong order (technical list):
```
- WebSocket support
- Plugin architecture
- REST API
- TypeScript SDK
```

Right order (pain-first):
```
- Works offline — no internet required, all data stored locally
- Export everything — Markdown, PDF, or raw JSON, always your data
- Self-hostable — deploy to your own server in 5 minutes
- Plugin API — extend with your own tools
```

**Rules:**
- ≤ 7 features in the main list. More than 7 signals "we don't know what we are."
- Each feature bullet: pain point first, implementation detail second
- Bold the key word of each bullet — GitHub renders bold in feature lists; it's free hierarchy
- If you have a features screenshot/demo, put it after the list

**AFFiNE case:** The product opened with "open source Notion alternative" — that single framing told users exactly which features they needed to see confirmed (offline, data ownership, privacy). The feature list didn't need to be comprehensive; it just needed to confirm those three concerns.
— (AFFiNE case, Iris Wei @WeiYipei, ep01)

---

### Section 5: Architecture / How It Works (Optional)

Include this section if:
- Your project has a non-obvious component structure (backend platform, distributed system)
- Developers need to understand the architecture to decide whether to contribute
- You're targeting developers who will integrate your project, not just use it

**What insforge does right:** Uses a `mermaid` graph to show the relationship between the AI agent → InsForge → individual backend services. One diagram replaces two paragraphs of explanation.

**Rules:**
- One diagram is worth 200 words. Use `mermaid` — it renders natively on GitHub.
- Keep the diagram to ≤ 8 nodes. More than that and it becomes noise.
- Put this section *after* Quick Start. Getting someone running comes before explaining the internals.

---

### Section 6: Deployment Options

Developers have three modes: local dev, self-hosted production, and "just use the cloud." Address all three.

```markdown
| Method | Link | When to use |
|--------|------|-------------|
| Cloud (hosted) | [yourproject.com](link) | Zero setup, try now |
| Docker Compose | [Quick Start](#quick-start) | Self-hosted, recommended |
| Railway / Render | [one-click deploy](link) | Self-hosted, no Docker |
| From source | [Dev Guide](link) | Contributing |
```

One-click deploy buttons (Railway, Render, Zeabur, Sealos) are worth including — they're high-signal trust indicators and they reduce friction to zero for non-Docker users.

---

### Section 7: Contributing

Keep this short. The actual guide lives in `CONTRIBUTING.md`.

```markdown
## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for setup.

Questions? Join [Discord](link) or open a [Discussion](link).
```

**Do not** put a full contributing guide in the README. It breaks the reading flow and buries the contributing CTA in prose.

---

### Section 8: Community & Support

Match the channel to the action type:

```markdown
## Community & Support

- **Discord** — questions, help, show what you built
- **GitHub Discussions** — feature requests, long-form questions
- **GitHub Issues** — bugs only
- **X / Twitter** — announcements, follow for updates
- **Email** — security issues, enterprise
```

Listing all your channels without explaining what each is for forces users to make a decision. Remove that friction.

---

### Section 9: Star History Chart

Put the star history chart at the bottom. It's social proof, not navigation.

```markdown
[![Star History Chart](https://api.star-history.com/svg?repos=yourorg/yourrepo&type=Date)](https://star-history.com/#yourorg/yourrepo&Date)
```

**Why it works:** A steep upward curve signals "this project is real and people are using it." Investors use this too — literally.

> 投资人专门写爬虫查 Star 真假，说明真实口碑就是你最有力的信号。
> Investors write crawlers specifically to check if stars are real — which means genuine star velocity is your strongest trust signal.
> — (AFFiNE case, Iris Wei @WeiYipei, ep03)

---

## Badge 使用原则 / Badge Usage Principles

Badges are **signals**, not decoration. Each badge should answer a question a developer would ask.

| Badge type | Question answered | Include? |
|-----------|-------------------|----------|
| License | "Can I use this commercially?" | Always |
| Stars | "Is this popular / maintained?" | Always |
| Last commit | "Is this abandoned?" | Yes |
| Build / CI status | "Does it actually work?" | Yes |
| Downloads (npm/docker/pypi) | "Is anyone actually using this?" | Yes if >1K |
| Code coverage | "Is the code quality real?" | Only if >70% |
| Version | "What's stable?" | Yes for libraries |
| "Made with X" partner badges | — | Omit unless required |

**Rules:**
- ≤ 8 badges on the first badge row. More than that is visual noise.
- Group badges by meaning: identity → health → community
- Never use a failing badge. A red CI badge is worse than no CI badge.

---

## 常见死亡模式 / Anti-patterns (README Death Modes)

### ❌ Death Mode 1: Feature Dumping Without Problem Framing

```
# MyApp

Features:
- Real-time collaboration
- Markdown support
- Plugin system
- REST API
- Mobile app
- Dark mode
- CSV export
...
```

This tells me nothing about who this is for or why I need it. It's a spec sheet, not a pitch.

**Fix:** Lead with the pain. "If you've ever lost work because [X happened], MyApp solves that."

---

### ❌ Death Mode 2: Burying Quick Start

If Quick Start is below the fold on the second scroll, you've already lost 60% of developers. They came to try it. Let them try it.

**Fix:** Quick Start is section 2 or 3, maximum. Not section 7.

---

### ❌ Death Mode 3: Generic Tagline

```
A powerful, flexible, and extensible framework for modern developers.
```

This is noise. "Powerful," "flexible," and "extensible" are claims every project makes.

**Fix:** Name the specific pain. Name the specific category. Name the specific user.

---

### ❌ Death Mode 4: No Visual Above the Fold

A wall of text badges → a wall of text description → a wall of text feature list. Developers scan, they don't read. If there's no image or video in the first scroll, most visitors have already left.

**Fix:** Hero image or demo GIF immediately after the tagline. Non-negotiable for UI products.

---

### ❌ Death Mode 5: README Only in Native Language

> README 英文主，首屏 <3 秒读懂。
> — (AFFiNE case, Iris Wei @WeiYipei, ep03)

Chinese-only, Japanese-only, or any non-English primary README immediately caps your addressable audience. GitHub trending, Hacker News, Reddit, and most developer aggregators are English-first platforms.

**Fix:** English README is the primary document. Provide translated versions via badges or a `/i18n` folder.

---

### ❌ Death Mode 6: Contributing Section That's Actually a Wall

```markdown
## Contributing

We welcome contributions from the community! Here's how to get started:

### Setting up the development environment

First, you'll need to install Node.js version 18 or higher. You can download it from...
[continues for 400 lines]
```

**Fix:** One paragraph, link to `CONTRIBUTING.md`. The README is a landing page, not a developer guide.

---

### ❌ Death Mode 7: Treating Stars as Vanity Metrics

Stars are distribution signals. GitHub Trending, search ranking, and investor/contributor due diligence all use star velocity as a proxy for legitimacy.

> AFFiNE 开源第一周 6000 Star，一个月 1 万，最终 60K+。GitHub trending 连续上榜 28 次，靠的是前两周疯狂回复社区消息。
> AFFiNE hit 6K stars in week 1, 10K in month 1, 60K+ total. 28 consecutive GitHub Trending appearances, driven by two weeks of obsessive community engagement.
> — (AFFiNE case, Iris Wei @WeiYipei, ep01/ep06)

A README that converts well drives star velocity. Stars drive trending. Trending drives more stars. The README is the entry point of this loop.

---

## AFFiNE 核心数据 / AFFiNE Data Points for Context

All sourced from Iris Wei (@WeiYipei) podcast episodes (ep01 / ep03 / ep06):

| Metric | Value | Source |
|--------|-------|--------|
| Stars, week 1 | 6,000 | ep01/ep03 |
| Stars, month 1 | 10,000 | ep01 |
| Stars, total | 60,000+ | ep01/ep03 |
| GitHub Trending appearances | 28 consecutive | ep06 |
| Tagline strategy | "Open source Notion alternative" — targeted offline / data export / privacy pain | ep01 |
| Product state at launch | "套壳" demo (wrapper demo, incomplete) | ep03/ep06 |
| What drove trending stays | Obsessive community reply for first 2 weeks | ep06 |
| What drove initial launch performance | Dev docs + traffic funnels + content prepared pre-launch | ep01 |
| Investor signal | Investors wrote crawlers to verify star authenticity — real star velocity = credibility | ep03 |

**Key insight:** The product was a wrapper demo at launch. The README hit the right pain points. The result was 6,000 stars in week 1. **The README is not a product feature — it is the marketing layer, and it works independently of product completeness.**

---

## 发布前自检 Checklist / Pre-publish Checklist

Run this before every README publish or major update.

### First screen (no scroll required)
- [ ] Logo / project name is visible and clear
- [ ] Tagline is ≤ 12 words and answers: what + who + pain
- [ ] There is a hero image, GIF, or demo video within the first screen
- [ ] Badge row is present but has ≤ 8 badges
- [ ] No wall of text before any visual element

### Content
- [ ] Quick Start is in the top 3 sections
- [ ] Quick Start has ≤ 5 commands and actually works on a fresh machine
- [ ] Features are sorted by user pain, not technical implementation
- [ ] Each feature bullet leads with the benefit, not the mechanism
- [ ] Contributing section is ≤ 1 paragraph + link to CONTRIBUTING.md

### Language & tone
- [ ] README primary language is **English**
- [ ] No "powerful," "flexible," "amazing," "robust" — replace with specifics
- [ ] No "we believe in open source" preamble — cut to the point
- [ ] Tagline does not start with "A" or "An" (almost always weak)

### Trust signals
- [ ] License badge is present
- [ ] CI / build status badge is present *and passing*
- [ ] Star history chart is at the bottom
- [ ] Discord / community link is in the README
- [ ] If star count >500, the count is visible in badges

### Technical
- [ ] All links tested (no 404s)
- [ ] Images hosted on GitHub CDN (not external)
- [ ] `mermaid` diagrams render correctly in GitHub preview
- [ ] One-click deploy buttons tested (if applicable)
- [ ] README renders correctly on mobile (check GitHub mobile)

---

## 快速诊断 / Quick Diagnosis

When someone sends you a README to review, run through this in order:

1. **Read only the first screen (simulate no scroll).** What do you know about the product? Who it's for? Why it matters? If you can't answer all three, the tagline or hero section needs rewriting.

2. **Find Quick Start.** Count which section number it is. If it's ≥ 5, it needs to move up.

3. **Read the tagline aloud.** Does it sound like a human pitch, or like a feature list? If it's the latter, rewrite it using the pain-first formula.

4. **Count the features.** If there are >7 bullets, ask: which 3 actually make someone install this? Keep those, cut or consolidate the rest.

5. **Look for walls of text.** Any paragraph >5 lines in the README above the Contributing section is probably trying to explain something that a diagram or demo would do better.

6. **Check for language.** Is the primary language English? If not, is there an English version?

---

## 参考 / References

- **InsForge README** (analyzed): Clean tagline ("all-in-one, open-source backend platform for agentic coding"), immediate demo video, mermaid architecture diagram, multiple one-click deploy options, star CTA with GIF. Strong structure, slightly heavy on deployment variants but appropriate for a developer infrastructure product.

- **Dify README** (analyzed, 60K+ stars): Hero image → dense badges → 1-paragraph description → immediate Quick Start. Feature list uses numbered format with bold subheadings. Multi-language README badges handled with shields. Star history and contributors grid at bottom. Notably, Quick Start is literally section 1 — the most aggressive funnel design.

- **AFFiNE** (primary case study): 0 → 60K stars. Tagline "Open source Notion alternative" — borrowed brand awareness + hit three specific pain points (offline, data portability, privacy). Product was incomplete at launch. README and narrative did the heavy lifting.
  All AFFiNE data: Iris Wei @WeiYipei, podcast ep01 / ep03 / ep06.

---

*By Iris (生姜 Iris) · ex-COO @ AFFiNE (0 → 60k★)*
*For overall OSS growth strategy → use `gingiris-opensource` skill*
*For README writing specifically → this is the skill*
