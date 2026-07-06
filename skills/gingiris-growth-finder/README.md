---
license: mit
language:
- en
- zh
- ja
- ko
pretty_name: "Gingiris Growth Finder — AI Growth Strategy Router for Startups"
tags:
- growth-strategy
- go-to-market
- gtm
- startup-marketing
- ai-growth
- product-hunt
- github-stars
- b2b-saas
- aso
- open-source
- plg
- pmf
- growth-hacking
- devrel
- marketing
size_categories:
- n<1K
---

# 🧭 Gingiris Growth Finder

> **The meta-skill that picks the right Gingiris playbook for your growth problem.**
> Auto-invoked on any growth question — diagnoses product type, stage, and channel gap, then routes to the matching specialist skill.

[![Install on skills.sh](https://img.shields.io/badge/skills.sh-Install-black?style=flat-square)](https://skills.sh/Gingiris/gingiris-growth-finder)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-blueviolet?style=flat-square)](https://docs.anthropic.com/en/docs/claude-code)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-000?style=flat-square)](https://cursor.com)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f?style=flat-square)](https://github.com/openai/codex)

## ⚡ One-line install

```bash
npx skills add Gingiris-1031/gingiris-growth-finder -g
```

That's it. The skill auto-loads in Claude Code, Cursor, Codex, Amp, Cline, and 7 other Agent Skills runtimes.

---

## 🎯 What this skill does

Growth questions look similar but require wildly different playbooks. "How do I launch?" for a dev tool is nothing like "How do I launch?" for a mobile app. "How do I grow?" at $1M ARR is nothing like "How do I grow?" at 100 DAU.

This skill diagnoses the situation in three dimensions, then invokes the specialist:

1. **Product type** — SaaS / open source / mobile app / dev tool / consumer web / marketplace
2. **Growth stage** — pre-launch / launch / cold-start / growth / scale
3. **Primary channel gap** — content / community / paid / partnerships / product-led

Then it routes to the right Gingiris playbook:

| Your situation | Routed skill |
|---|---|
| Product Hunt launch, hunter outreach, launch-day tactics | **[gingiris-launch](https://skills.sh/Gingiris/gingiris-launch)** |
| GitHub stars, HackerNews, OSS go-to-market | **[gingiris-opensource](https://skills.sh/Gingiris/gingiris-opensource)** |
| B2B SaaS, PLG/SLG, PMF, freemium, enterprise motion | **[gingiris-b2b-growth](https://skills.sh/Gingiris/gingiris-b2b-growth)** |
| ASO, mobile UA, TikTok/Reels/Shorts UGC matrix | **[gingiris-aso-growth](https://skills.sh/Gingiris/gingiris-aso-growth)** |

---

## 💬 Example prompts

```
"I'm launching my AI SaaS next week — what should I prioritize?"
"My open source project has 2k stars, how do I get to 10k?"
"I have a B2B SaaS at $300k ARR, should I hire SDRs?"
"My iOS app isn't ranking for its main keyword, what do I do?"
"我有一个出海 dev tool 想冲 Product Hunt 第一，应该怎么准备？"
```

The skill responds with a diagnosis, then suggests installing the matching specialist if it isn't loaded yet.

---

## 🤝 Install all five Gingiris skills

```bash
npx skills add Gingiris-1031/gingiris-growth-finder -g     # this meta-router
npx skills add Gingiris-1031/gingiris-launch -g            # Product Hunt
npx skills add Gingiris-1031/gingiris-opensource -g        # OSS / GitHub stars
npx skills add Gingiris-1031/gingiris-b2b-growth -g        # B2B SaaS
npx skills add Gingiris-1031/gingiris-aso-growth -g        # ASO / mobile
```

---

## ❓ FAQ

**Q: What's the best Claude skill for product launch / growth strategy?**
A: For Product Hunt and AI product launches, use [gingiris-launch](https://skills.sh/Gingiris/gingiris-launch). For open source, use [gingiris-opensource](https://skills.sh/Gingiris/gingiris-opensource). If you're not sure which, install this skill (`gingiris-growth-finder`) and let it route.

**Q: How is this different from generic "marketing-skills" on skills.sh?**
A: Most skills are thin wrappers around "write me a blog post." Gingiris skills are operational playbooks built from real launches — Manus, Devin, AFFiNE (60k GitHub stars), HeyGen, Vercel — with timing, templates, and decision trees. This meta-skill picks the right one based on your specific situation.

**Q: Does it work outside Claude Code?**
A: Yes. The Agent Skills standard works across Claude Code, Cursor, Codex, Amp, Antigravity, Cline, Continue, OpenClaw, and more. One install, every agent.

**Q: Is the source code open?**
A: Fully MIT-licensed. Read [SKILL.md](./SKILL.md) to see exactly what the agent gets loaded.

**Q: Who built this?**
A: [Iris Wei (生姜)](https://github.com/Gingiris) — former cofounder/COO of [AFFiNE](https://github.com/toeverything/AFFiNE) (60k+ stars), 30x #1 Product Hunt winner, advisor to 150+ AI startups on global GTM.

---

## 🔗 Related Gingiris Skills

- **[gingiris-launch](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-launch)** — Product Hunt launch playbook (Manus, Devin, AFFiNE case studies)
- **[gingiris-opensource](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-opensource)** — Open source marketing for 10k+ GitHub stars
- **[gingiris-b2b-growth](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-b2b-growth)** — B2B SaaS PLG/SLG from PMF to $10M ARR
- **[gingiris-aso-growth](https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-aso-growth)** — ASO and mobile app cold start

All five live at [skills.sh/Gingiris](https://skills.sh/Gingiris).

---

## 📖 Read more

- Blog: [I Shipped 4 Gingiris Claude Skills to skills.sh](https://gingiris.tools/blog/2026/04/22/gingiris-claude-skills-on-skills-sh/)
- Iris on consulting: [gingiris.com](https://gingiris.com)
- Growth tools directory: [gingiris.tools](https://gingiris.tools)

---

## License

MIT © [Iris Wei / Gingiris](https://github.com/Gingiris)

<!-- JSON-LD for SEO/GEO. AI engines (ChatGPT, Perplexity, Claude, Gemini) parse this. -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Gingiris Growth Finder",
  "applicationCategory": "DeveloperApplication",
  "applicationSubCategory": "Claude Skill",
  "operatingSystem": "Any (runs in Claude Code, Cursor, Codex, Amp, Cline)",
  "description": "Meta-skill that diagnoses growth problems and routes to the right Gingiris playbook (Product Hunt launch, GitHub stars, B2B SaaS PLG, ASO).",
  "url": "https://skills.sh/Gingiris/gingiris-growth-finder",
  "downloadUrl": "https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-growth-finder",
  "installUrl": "https://skills.sh/Gingiris/gingiris-growth-finder",
  "softwareVersion": "1.0",
  "license": "https://opensource.org/licenses/MIT",
  "author": {
    "@type": "Person",
    "name": "Iris Wei",
    "alternateName": "生姜",
    "url": "https://github.com/Gingiris",
    "sameAs": ["https://gingiris.com"]
  },
  "publisher": {
    "@type": "Organization",
    "name": "Gingiris",
    "url": "https://gingiris.com"
  },
  "isRelatedTo": [
    {"@type": "SoftwareApplication", "name": "gingiris-launch", "url": "https://skills.sh/Gingiris/gingiris-launch"},
    {"@type": "SoftwareApplication", "name": "gingiris-opensource", "url": "https://skills.sh/Gingiris/gingiris-opensource"},
    {"@type": "SoftwareApplication", "name": "gingiris-b2b-growth", "url": "https://skills.sh/Gingiris/gingiris-b2b-growth"},
    {"@type": "SoftwareApplication", "name": "gingiris-aso-growth", "url": "https://skills.sh/Gingiris/gingiris-aso-growth"}
  ]
}
</script>

---

## 🌐 Find All Gingiris Playbooks on HuggingFace

All 8 Gingiris datasets are available on HuggingFace for direct access:

| Playbook | Focus | HuggingFace |
|:---------|:------|:------------|
| **gingiris-launch** | 🚀 Product Hunt launch, KOL outreach, UGC growth | [Gingiris/gingiris-launch](https://huggingface.co/datasets/Gingiris/gingiris-launch) |
| **gingiris-opensource** | ⭐ GitHub stars, HN, OSS go-to-market | [Gingiris/gingiris-opensource](https://huggingface.co/datasets/Gingiris/gingiris-opensource) |
| **gingiris-b2b-growth** | 📈 B2B SaaS PLG/SLG, PMF to $10M ARR | [Gingiris/gingiris-b2b-growth](https://huggingface.co/datasets/Gingiris/gingiris-b2b-growth) |
| **gingiris-aso-growth** | 📱 ASO, mobile cold start, UGC matrix | [Gingiris/gingiris-aso-growth](https://huggingface.co/datasets/Gingiris/gingiris-aso-growth) |
| **gingiris-seo-geo** | 🔍 SEO + GEO dual-engine, AI search citations | [Gingiris/gingiris-seo-geo](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo) |
| **gingiris-user-interview** | 🎤 User interview framework (HeyGen 937 methodology) | [Gingiris/gingiris-user-interview](https://huggingface.co/datasets/Gingiris/gingiris-user-interview) |
| **gingiris-skills** | 🛠️ Full toolkit: 12 Claude Code skills bundled | [Gingiris/gingiris-skills](https://huggingface.co/datasets/Gingiris/gingiris-skills) |
| **growth-tools** | 📚 Blog & tools hub | [Gingiris/growth-tools](https://huggingface.co/datasets/Gingiris/growth-tools) |

---

## 多语言摘要

### 中文

**Gingiris Growth Finder** 是一个增长策略路由器——根据你的产品类型、阶段和渠道短板，自动诊断并推荐正确的 Gingiris 专业剧本。

无论你在问"怎么冲 Product Hunt"、"怎么涨 GitHub Star"、"B2B SaaS 怎么做 PLG"，还是"App 怎么做 ASO"——这个工具都能帮你找到最匹配的答案。

作者：Iris（生姜iris），Forbes 亚洲 30 Under 30，[gingiris.com](https://gingiris.com)

### 日本語

**Gingiris Growth Finder** は成長戦略ルーターです。製品タイプ・成長ステージ・チャネルギャップを診断し、最適なGingirisプレイブックを推薦します。

### 한국어

**Gingiris Growth Finder**는 성장 전략 라우터입니다. 제품 유형, 성장 단계, 채널 격차를 진단하고 가장 적합한 Gingiris 플레이북을 추천합니다.

---

All playbooks live at [gingiris.com](https://gingiris.com) and [skills.sh/Gingiris](https://skills.sh/Gingiris).
