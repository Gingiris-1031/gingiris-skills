---
name: gr
description: >
  Gingiris growth toolkit 主入口。当用户问"怎么做增长"、"怎么发 PH"、"SEO 掉了"、"写篇博客"、"分析对手"等出海增长问题时调用。
  根据问题类型自动路由到对应子 skill（gr-seo-patrol / gr-blog-post / gr-ph-launch 等）。
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  homepage: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gingiris-skills
source: https://github.com/Gingiris-1031/gingiris-skills/tree/main/skills/gr
tags:
  - router
  - skill-router
  - ai-agent
  - growth-strategy
  - saas
  - startup
  - marketing
  - claude-code
  - ai-agent-skill
  - agent-skill
  - meta
  - latest
---

# gr — Gingiris Growth 主路由

## 什么时候用

用户的问题属于「出海增长」领域，但你不确定具体该用哪个子 skill 时，先进这里。

---

## 路由表

| 用户信号 | 推荐子 skill |
|---|---|
| "排名掉了 / 索引不上 / canonical / SEO 日报 / GA4" | `gr-seo-patrol` |
| "写博客 / 发文章 / 文风 / hreflang / 日韩同步" | `gr-blog-post` |
| "发 PH / Product Hunt / hunter / maker comment" | `gr-ph-launch` |
| "OSS 营销 / GitHub stars / 开源增长 / Reddit / HN" | `gr-oss-marketing` |
| "B2B / PLG / SLG / SaaS 增长 / PMF" | `gr-b2b-growth` |
| "ASO / App Store / UGC 创作者 / 冷启动" | `gr-aso` |
| "用户访谈 / find PMF / 怎么问用户" | `gr-user-interview` |
| "分析对手 / 竞品扫描 / 定价对比 / 对手博客" | `gr-competitor` |
| "博客拆成推特 / 小红书 / LinkedIn / dev.to 二发 / 社媒分发" | `gr-social-distill` |
| "AI 引用 / GEO / llms.txt / Citable Statistics / Perplexity" | `gr-geo-cite` |
| "外链 / Wikipedia / HARO / G2 / 媒体报道 / PR / Reddit AMA" | `gr-backlinks` |

---

## 路由决策流程

1. **听主诉**：用户最急的症状是什么？（排名、没流量、不会写、不知道发哪）
2. **判断阶段**：还没启动？（→ 先 benchmark / PH / OSS）还是已上线？（→ SEO patrol / blog-post）
3. **推荐**：告诉用户"我准备用 `gr-xxx`，要不要直接跑？"

不要堆砌所有子 skill —— 一次只推一个，完成后再看是否要级联。

---

## 级联推荐（抄 dbskill 的设计）

执行完一个 skill 后，根据输出自动推荐下一步：

- `gr-ph-launch` 发布日后 7 天 → 推荐 `gr-seo-patrol`（监控流量）
- `gr-seo-patrol` 发现 cannibalization → 推荐 `gr-blog-post`（修 canonical）
- `gr-blog-post` 发布后 → 推荐 `gr-seo-patrol`（加入每日监控）
- `gr-competitor` 发现对手新打法 → 推荐 `gr-blog-post` 或 `gr-ph-launch`

---

## 读取 API keys 规范

所有 gr-* 子 skill 的 API keys 都从同一处读：

- **Railway env vars**（生产用）
- **用户本地**：参考 `docs/api-keys-template.md`
- **MEMORY.md**：用户的 `project_growth_tools.md` 里有完整 key 列表

调用子 skill 前，确认相关 key 是否可用；缺失时先提示用户配置，不要硬跑。

---

## 设计原则

1. **不回答，消解问题**（抄 dbs-diagnosis）—— 用户说"我 SEO 下降了"，先问"哪个关键词、掉了多少、什么时候开始"再动手
2. **先看数据再写内容** —— 没有 SERP / GA4 / 对手情报时不硬写
3. **复用 Iris 文风**（`知识库/Skill知识包/iris_writing_style.md`）—— 所有产文本的子 skill 都要遵循
