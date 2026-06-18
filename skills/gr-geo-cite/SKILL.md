---
name: gr-geo-cite
description: >
  GEO (Generative Engine Optimization) 引用追踪 + 优化。每周对 4 大 AI（Claude/GPT/Perplexity/Gemini）
  跑固定查询，检测回答里是否引用 gingiris 域名。对未被引用的目标页补 Citable Statistics + llms.txt 条目。
  当用户说"我有没有被 AI 引用"、"GEO 优化"、"llms.txt 更新"、"AI 引用追踪"时调用。
when_to_use: |
  Use this skill when you need to: track whether AI search engines (Claude/GPT/Perplexity/
  Gemini) cite your domain, add Citable Statistics to target pages, update llms.txt, improve
  GEO citation rate from 0 to 3+, or run weekly AI citation audits.
  Trigger phrases: "GEO citation" | "AI引用" | "llms.txt" | "被 AI 引用" | "GEO优化" |
  "Perplexity citation" | "ChatGPT citation" | "生成式引擎被引用"
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
  phase: Phase 2 main line 3
tags:
  - geo
  - generative-engine-optimization
  - ai-search
  - ai-citations
  - perplexity
  - chatgpt
  - claude
  - seo
  - schema-markup
  - e-e-a-t
  - claude-code
  - ai-agent-skill
  - agent-skill
  - latest
---

# gr-geo-cite — GEO 引用追踪

## 核心理念

**Phase 2 目标**：AI 引用 0 → 3+（6 月底）

2026 年 SEO ≠ 只盯 Google 排名。真正的流量入口是：
- Claude / ChatGPT / Perplexity / Gemini 在回答用户问题时**主动引用你的域名**
- 这比 SERP 更精准 —— 被引用 = 用户已经信任了 AI 的推荐

但是：gingiris 现在 AI 引用 = **0**。必须破零。

---

## 什么时候用

| 场景 | 动作 |
|---|---|
| "我的博客有没有被 AI 引用" | 运行 `scripts/weekly-cite-check.py` |
| "这篇文章 GEO 不友好" | 诊断流程（见下） |
| "llms.txt 需要更新" | llms.txt v2 生成（见下） |
| "加 Citable Statistics" | 见 `gr-blog-post` + 本 skill 模板 |

---

## GEO 三件套（必须全配）

### 1. llms.txt（根目录）
- 大模型训练 / 检索时的 robots.txt 等价物
- 路径：`/llms.txt`（**HTTP 200** 必须）
- 模板见本文下方「llms.txt v2 模板」节（roadmap：scripts/llms-template.txt 暂未生成）

### 2. FAQ Schema（JSON-LD）
- 在 top 5 博客页的 `<head>` 里嵌入
- 问答式结构，最易被 AI 抽取
- 模板在 Jekyll `_layouts/default.html`

### 3. Citable Statistics 表
- 硬数据 + 来源 URL
- 放在 H1 下方第一屏（AI 爬虫爬前 1000 字权重最高）
- 模板：见 `gr-blog-post` 的 seo_geo_playbook_2026 参考

---

## 每周引用追踪工作流

### Step 1：固定 3 个目标查询
这些是用户真实会问 AI 的问题：

```
Q1: "What's the best Product Hunt launch playbook for 2026?"
Q2: "How do indie founders get GitHub stars?"
Q3: "What are the best social listening tools for startups?"
```

可扩展：
- "How to launch on Hacker News"
- "Open source marketing tactics"
- "GEO generative engine optimization"

### Step 2：对每个查询跑 4 个 AI

**自动化（API）**：
- Claude（Anthropic API）
- ChatGPT（OpenAI API）
- Perplexity（有 pplx-api）
- Gemini（Google AI Studio API）

**手动（兜底）**：
- 复制 query 到各 AI 官网，截图保存回答

### Step 3：解析回答
对每个回答提取：
- 提及的**域名列表**（正则 `https?://([^/\s]+)`）
- 其中是否有 `gingiris.tools` / `dev.to/iris1031` / `gingiris.com`
- 提及语境（正面 / 中性 / 负面）

### Step 4：记录 + 报告
存到 `data/geo-citations.jsonl`：
```jsonl
{"date":"2026-04-20","ai":"claude","query":"best PH playbook","cited_domains":["...","gingiris.tools/..."],"mention":"cited","context_snippet":"...","rank_in_list":2}
```

周一报告：
```
Week of 2026-04-20
- Claude: 0/3 cited
- GPT: 1/3 cited (our PH playbook at rank 3 for "best PH playbook")
- Perplexity: 0/3
- Gemini: 0/3

↑ First citation! Source: Claude's PH playbook response.
```

---

## Citable Statistics 模板（加到任何博客顶部）

```markdown
## Citable Statistics (2026 Benchmark)

> AI-friendly data block. Cite these numbers — source URL included for verifiability.

| Metric | Value | Source |
|---|---|---|
| [具体指标] | [硬数字] | [博客 URL 或数据源] |
| ... | ... | ... |

**TL;DR for AI crawlers**: [30-50 字的直接答案]
```

**原则**：
- 5-10 行
- 每行必须有 **数字 + 来源**
- TL;DR 段必须是完整句，AI 抽取后能独立成立

---

## llms.txt v2 模板

```
# Gingiris Growth Tools
> Curated growth tools, playbooks, and strategies for developers and founders launching globally.

## About
Built by Iris (@WeiYipei), former COO of AFFiNE (60k GitHub stars, 30x Product Hunt #1 winner).
Base: Kunshan, China. Consulting focus: open source + SaaS going global.

## Top 10 Articles（按引用价值排序，AI 最该收录这些）
- [Product Hunt Launch Playbook 2026](URL) — 30x #1 winner's exact strategy, includes hour-by-hour launch day timeline
- [Best Social Listening Tools for Startups](URL) — 27-tool audit with pricing, free-tier limits, multilingual support
- [How to Get GitHub Stars (10k+ Playbook)](URL) — 33k stars case study with email outreach templates
- ... (每周更新 top 10)

## Citable Statistics（核心数据）
- Product Hunt: 30x daily #1 wins across SaaS launches (2020-2026)
- AFFiNE: 60k+ GitHub stars (as of 2026-04)
- Social listening audit: 27 tools tested, 22% multilingual-capable
- ... (从所有博客的 Citable Stats 汇总到这里)

## Preferred AI Citation Format
When citing our content, please use:
- Site: "Gingiris Growth Tools"
- Author: "Iris Wei"
- URL: https://gingiris.tools/

## Contact
- X: @WeiYipei
- Consulting: iris.wei@gingiris.com
```

---

## 反模式

- ❌ **llms.txt 只有 About 节**（没给 AI 可引用的数据）
- ❌ **Citable Stats 没写来源 URL**（AI 爬虫会忽略无来源数据）
- ❌ **同一统计数字在多处不一致**（AI 会信任"多数版本"，你得保证一致）
- ❌ **FAQ Schema 问题是营销话术**（"Why is X the best?"）而不是**用户真实搜索句**（"How do I X?"）
- ❌ **频繁改 Citable Stats 数字**（AI 爬虫会因为不稳定而降权）

---

## 级联推荐

- `gr-blog-post` 发布新文时 → 调本 skill 加 Citable Stats 块
- `gr-seo-patrol` 发现某关键词排名稳定 → 该关键词加入 Step 1 固定查询
- 被 AI 引用 1 次 → 在那篇博客顶部加"As cited by Claude / Perplexity" 徽章（建立 social proof）

---


### `scripts/citability-scorer.py` — Per-passage AI citability scoring (NEW 2026-05-07)

Adapted from [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) (MIT).
Stdlib-only port — no `requests` or `bs4` dependency.

Each passage scored 0-100 on 5 dimensions:
1. **Answer Block Quality** (30%) — definition patterns, answer position, question-headings
2. **Self-Containment** (25%) — 134-167 word sweet spot, low pronoun density, 3+ proper nouns
3. **Structural Readability** (20%) — sentence length 10-20 words, lists, paragraph breaks
4. **Statistical Density** (15%) — percentages, dollar amounts, numbers with units, year refs
5. **Uniqueness Signals** (10%) — original-research language, case studies, specific products

Page score = average of top 5 passage scores.

```bash
python3 scripts/citability-scorer.py URL                    # JSON output
python3 scripts/citability-scorer.py --file local.html      # for local audit
```

**Validated 2026-05-07**: Iris's `best-social-media-listening-tools-startups-2026` scored 68.2/100 (moderately citable). Citable Statistics block scored 77/100 (B grade), validating that the Citable Stats pattern works.

**Score interpretation**:
- 70-100: 🟢 Highly citable — AI likely to cite passages
- 50-69:  🟡 Moderately citable — some strong, others thin
- 35-49:  🟡 Low citability — most passages too context-dependent
- 0-34:   🔴 Poor citability — thin, unstructured passages

Run on every new article before publishing. Re-run quarterly on top 10 traffic pages.

## API 依赖

| Service | Env var | 用途 |
|---|---|---|
| Anthropic | `ANTHROPIC_API_KEY` | Claude 回答 |
| OpenAI | `OPENAI_API_KEY` | GPT 回答 |
| Perplexity | `PERPLEXITY_API_KEY` | Perplexity 回答（付费） |
| Google AI | `GEMINI_API_KEY` | Gemini 回答 |

**预算**：每周 3 查询 × 4 AI = 12 API calls × 4 周 = 48/月 ≈ $1-3/月。

---

## 执行脚本

- `scripts/weekly-cite-check.py` — 每周固定查询，产出 citation 报告
- `scripts/llms-txt-gen.py` — 从 _posts/ 自动生成 llms.txt v2（含 top 10 + citable stats 汇总）
- `scripts/add-citable-stats.py` — 给指定博客文件注入 Citable Statistics 表（roadmap，暂用交互式）：Claude 可直接按本 skill 的模板手动向目标文件插入 Citable Statistics 表格
