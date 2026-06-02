---
license: mit
language:
- en
- zh
- ja
- ko
pretty_name: "Gingiris Skills — Complete AI Growth Toolkit (16 Claude Code Skills)"
tags:
- claude-code
- ai-agent
- growth-tools
- seo
- product-hunt
- open-source
- b2b-saas
- aso
- user-interview
- startup-marketing
- ai-growth
- developer-tools
- llm-tools
- growth-hacking
- marketing
size_categories:
- n<1K
---

# gingiris-skills

Iris / Gingiris 的出海增长工具箱 —— 把 6 个 gingiris-* playbook repo + 每日运营脚本 + 60 篇博客实战经验，打包成 Claude Code skills。

**作者**：[Iris](https://x.com/WeiYipei) · [Gingiris 博客](https://gingiris.tools/blog/)

**所有内容开放**，可以整套装，也可以只拿一部分。Skill、知识包、原子库、单个脚本都能单独用。

---

## 工具箱（v0.5.0 — 16 个 skill）

| Skill | 做什么 |
|---|---|
| `/gr` | 主入口，根据你的问题自动路由 |
| `/gr-seo-patrol` | 每日 SEO/GEO 巡逻 — SERP 追踪、canonical 修复、社媒雪崩救援 |
| `/gr-blog-post` | Jekyll 博客发布 — Iris 文风 + hreflang 中英日韩 + FAQ Schema |
| `/gr-ph-launch` | Product Hunt 发布剧本 — 30x 日冠经验 |
| `/gr-oss-marketing` | 开源项目整合营销 — GitHub star、KOL、Reddit/HN/Discord |
| `/gr-b2b-growth` | B2B SaaS 增长 — PMF → $10M ARR，PLG/SLG 选型 |
| `/gr-aso` | ASO + App 冷启动 — metadata、UGC 矩阵、TikTok 投流 |
| `/gr-user-interview` | 用户访谈 — HeyGen 937 访谈方法论 |
| `/gr-competitor` | 竞品扫描 — 底层调 [actionbook](https://actionbook.dev)，10x 快，30 tab 并发 |
| `/gr-social-distill` | 博客 → 4 社媒变体（X / 小红书 / LinkedIn / dev.to-Zenn），激活 Organic Social |
| `/gr-geo-cite` | GEO 引用追踪 — 每周跑 4 大 AI 查 gingiris 引用率 + llms.txt v2 自动生成 |

| `/gr-backlinks` | 系统化外链建设 — Wikipedia / PR-HARO / G2 / Reddit-Quora 5 通道，0→1 站点 GEO + SEO 共升 |
| `/gr-competitor-research` | 竞品深度调研 — Wayback 快照、X 传播链路、增长飞轮评分 |
| `/gr-community-ambassador` | 社区/大使运营 — 招募、分层管理、留存、治理全 SOP |
| `/gr-seo-geo-agent` | SEO/GEO Agent 自动化运营 — 月产 32K 曝光的执行 SOP |
| `/gr-product-dev-ops` | 产研运协同 — 10 天迭代、看板、三方对齐、一票否决 |

### Roadmap（0.3+）

| Skill | 来源 |
|---|---|
| `/gr-ph-comment` | 包装 [PH Comment Generator](https://gingiris.tools/tools/ph-comment-generator/) |
| `/gr-gh-outreach` | 包装 [GitHub Issue Generator](https://gingiris.tools/tools/github-issue-generator/) |
| `/gr-readme` | 包装 [GitHub README Generator](https://gingiris.tools/tools/github-readme-generator/) |
| `/gr-hunter-radar` | 结合 actionbook 扫 PH hunter 活跃度 |

---

## 工作流

```
gr-competitor（看对手在做啥）
    ↓
gr-ph-launch / gr-oss-marketing / gr-b2b（选打法）
    ↓
gr-blog-post（产内容）
    ↓
gr-seo-patrol（上线后监控）
    ↓ cannibalization           ↓ 雪崩
gr-seo-patrol canonical-fix   gr-seo-patrol rescue
    ↓
gr-user-interview（用户反馈）
```

Skill 之间会自动推荐下一步。比如：
- `gr-ph-launch` 发布 24h 后 → 推荐 `gr-seo-patrol` 加监控
- `gr-seo-patrol` 发现 cannibalization → 自动跳到 canonical 修复流程
- `gr-blog-post` 发布后 → 自动加入 `gr-seo-patrol` 监控名单

---

## 安装

**推荐：Claude Code 插件市场**

```bash
claude plugin marketplace add Gingiris-1031/gingiris-skills
claude plugin install gr@gingiris-skills
```

装完在 Claude Code 里输入 `/gr` 即可。

**单独装某个 skill**：

```bash
claude plugin install gr-seo-patrol@gingiris-skills
```

---

## 知识库

所有方法论文档与原子知识点都开放，即使不装 skill 也能用。

### 目录结构

```
知识库/
├── 原子库/
│   ├── atoms.jsonl                    # 结构化知识原子（可 RAG）
│   └── README.md
└── Skill知识包/
    ├── iris_writing_style.md          # 文风指南（5 要素）
    └── seo_geo_playbook_2026.md       # SEO 飞轮 + GEO 三件套
```

### 怎么在你自己的项目里用

**场景 1：给你的 AI 加 SEO 诊断能力**
把 `知识库/Skill知识包/seo_geo_playbook_2026.md` 粘到 system prompt。

**场景 2：做 RAG**
`atoms.jsonl` 导向量库，每条带 `topics` 标签。

**场景 3：只要脚本**
`skills/gr-seo-patrol/scripts/*.py` 可独立跑，看 `docs/api-keys-template.md` 配 env。

---

## API 依赖

见 [`docs/api-keys-template.md`](docs/api-keys-template.md)。

核心：`DATAFORSEO_B64` + `GITHUB_TOKEN`，其他 skill 按需加。

---

## 许可证

MIT。

- 个人使用、学习、研究：随便
- 商业用途：随便
- 衍生作品：建议（不强制）注明来源

---


## Monthly Full-Site Audit Workflow

> **Battle-tested 2026-05-07** on a 58-page blog. Caught 43 SERP-truncating titles + 36 schema warns + 27 stop-word slugs in a single 30-min run. One layout-level commit fixed 20 of 43 titles. **Use for any Jekyll / Hugo / Next.js blog with 30+ posts.**

A repeatable 6-stage workflow you can run on any site. Powered by 4 scripts (see attribution below).

### Stage 1 — Discovery (5 min)
Pull all blog URLs from your sitemap:
```python
import urllib.request, re
sm = urllib.request.urlopen("https://your-site.com/sitemap.xml").read().decode()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/blog/" in u]
```

### Stage 2 — Parallel Audit (20 min for 60 pages)
Run two audit scripts per URL in 4-thread parallel:

```bash
pip install requests
python3 skills/gr-seo-patrol/scripts/check-page.py URL --timeout 20
python3 skills/gr-seo-patrol/scripts/check-schema.py URL --timeout 20
```

Each script outputs a structured JSON envelope (`status: pass|warn|fail|info` per check).

### Stage 3 — Aggregate Findings
Bucket issues by type:
- **Title length** > 70 chars (SERP truncation risk)
- **H1 length** > 70 chars (mobile readability)
- **Meta description** outside 80-170 chars
- **Schema warns** by `@type` (BlogPosting / Article / Organization)
- **Canonical mismatches**, **slug stop words**, **missing alt text**

Save aggregated counts + per-URL lists to `findings.json`.

### Stage 4 — Layered Fix Strategy (HIGH ROI ORDER)

| Order | Layer | Scope | Typical commits | ROI |
|---|---|---|---|---|
| 1️⃣ | **Layout** (`_layouts/default.html`) | Schema bugs, title suffix, dateModified injection | 1 | 🔥 fixes 20+ pages at once |
| 2️⃣ | **Config** (`_config.yml`) | Logo URL, twitter, social, author structure | 1 | fixes site-wide |
| 3️⃣ | **Per-article batch** | Trim long titles/H1s, expand short meta | 10-20 | per-file, parallelizable |
| 4️⃣ | **Skip** | Slug stop words (changing breaks 301), low-traffic old articles | 0 | low ROI |

### Stage 5 — Verify
After Jekyll/Hugo rebuild (~60-90s), re-run `check-schema.py` on a sample page.
All schema types should show `status: pass`:
Article · BlogPosting · Organization · FAQPage

### Stage 6 — Archive + Trend Track
Commit `findings.json` to `data/audit-{YYYY-MM-DD}.json` for month-over-month trend analysis.
Add 2-5 atoms to `知识库/原子库/atoms.jsonl` documenting any new lessons.

### Schedule it
Add a monthly cron to auto-run before your Phase 2 / quarterly checkpoint:
```bash
# In Claude Code's scheduled-tasks
cronExpression: "0 10 1 * *"   # 10am on day 1 of each month
prompt: "Run Monthly Full-Site Audit per gr-seo-patrol/SKILL.md workflow..."
```

### What you'll typically find on your first run

Real numbers from gingiris.tools 2026-05-07 run:

| Issue | Count | Resolution path |
|---|---|---|
| Title >70 chars | 43/58 | Layout-level (-20 chars suffix) + 13 per-article retrim |
| Schema warns | 36 | Layout-level (dateModified + publisher.logo + contactPoint) |
| H1 >70 chars | 23 | Per-article trim (paired with title) |
| Meta too short/long | 20 | Per-article (i18n posts often hit this) |
| Slug stop words | 27 | **SKIP** (would break 301 redirects) |
| HTTP errors | 2 | Investigate (likely deleted/renamed) |

**Total time**: ~30 min audit + 90 min fixes = **2 hours for site-wide SEO health refresh**.

### HARD RULE (anti-hallucination guardrail)

⛔ **Output ONLY the checks defined in the script's JSON envelope.**
- Do NOT add "bonus" checks not in the script output
- Do NOT contradict the script's `status` field without observable evidence
- Do NOT invent metrics like "EEAT score 89" — third-party scoring is unofficial per Google 2026 guidance
- If `llm_review_required: true`, make explicit judgment + document reasoning + update status

The script envelope is **the single source of truth**. Treat as strict whitelist.

### Script attribution

The 4 audit scripts (`check-page.py`, `check-schema.py`, `check-site.py`, `check-social.py`) in `skills/gr-seo-patrol/scripts/` are **adapted from** [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) (MIT). Original repo focused on single-page client-presentable HTML reports; we adapted them for orchestrated batch audit + Jekyll/GitHub Pages site analysis. Original license terms preserved in each file header.

---
## 关联 repo

- [Gingiris-1031/growth-tools](https://github.com/Gingiris-1031/growth-tools) — 主 blog，所有 skill 的实战场（线上 [gingiris.tools](https://gingiris.tools/blog/)）
- [gingiris-launch on HuggingFace](https://huggingface.co/datasets/Gingiris/gingiris-launch) — PH launch playbook 内容源
- [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) — 框架灵感来源
- [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) — 单页 SEO 审计脚本来源（4 scripts adapted）
- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) — 25-skill SEO 全套（含外链分析，可作 Tier 3 扩展）
- [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) — GEO 0-100 评分体系（可作 gr-geo-cite 增强）

---

## 贡献

- 发 Issue 描述你的运营场景
- PR 加新 skill / 新原子 / 新方法论
- 跟 [@WeiYipei](https://x.com/WeiYipei) 聊

---

## 关于作者 / About the Author

**Iris（生姜iris）** — Analook 创始人，此前是 [AFFiNE](https://github.com/toeverything/AFFiNE) 联合创始人兼 COO。专注 AI 创业公司的全球 GTM、SEO/GEO、Product Hunt 发布与 B2B 增长。

Founder of Analook. Previously cofounder & COO of AFFiNE. Works with AI startups on global GTM, SEO/GEO, Product Hunt launches, and B2B growth.

- 网站 / Website: [gingiris.com](https://gingiris.com)
- Twitter/X: [@WeiYipei](https://x.com/WeiYipei)
- Telegram: [@Iris_carrot](https://t.me/Iris_carrot)
- Blog: [gingiris.tools/blog](https://gingiris.tools/blog/)

---

## 🗂️ See Also — Gingiris Playbook Series on HuggingFace

| Playbook | Focus | HuggingFace |
|:---------|:------|:------------|
| **gingiris-growth-finder** | 🧭 Meta-router: diagnoses your situation, picks the right playbook | [Gingiris/gingiris-growth-finder](https://huggingface.co/datasets/Gingiris/gingiris-growth-finder) |
| **gingiris-launch** | 🚀 Product Hunt launch, KOL outreach, UGC growth | [Gingiris/gingiris-launch](https://huggingface.co/datasets/Gingiris/gingiris-launch) |
| **gingiris-opensource** | ⭐ GitHub stars, HN, OSS go-to-market | [Gingiris/gingiris-opensource](https://huggingface.co/datasets/Gingiris/gingiris-opensource) |
| **gingiris-b2b-growth** | 📈 B2B SaaS PLG/SLG, PMF to $10M ARR | [Gingiris/gingiris-b2b-growth](https://huggingface.co/datasets/Gingiris/gingiris-b2b-growth) |
| **gingiris-aso-growth** | 📱 ASO, mobile cold start, UGC matrix | [Gingiris/gingiris-aso-growth](https://huggingface.co/datasets/Gingiris/gingiris-aso-growth) |
| **gingiris-seo-geo** | 🔍 SEO + GEO dual-engine, AI search citations | [Gingiris/gingiris-seo-geo](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo) |
| **gingiris-user-interview** | 🎤 User interview framework (HeyGen 937 methodology) | [Gingiris/gingiris-user-interview](https://huggingface.co/datasets/Gingiris/gingiris-user-interview) |
| **growth-tools** | 📚 Blog & tools hub | [Gingiris/growth-tools](https://huggingface.co/datasets/Gingiris/growth-tools) |

All playbooks live at [gingiris.com](https://gingiris.com) and [skills.sh/Gingiris-1031/gingiris-skills](https://skills.sh/Gingiris-1031/gingiris-skills).

---

## 🔗 Platform Links

| Platform | Link |
|:---------|:-----|
| **ClawHub** (main install) | [clawhub.ai/user/gingiris](https://clawhub.ai/user/gingiris) |
| **HuggingFace** (datasets) | [huggingface.co/Gingiris](https://huggingface.co/Gingiris) |
| **skills.sh** (Claude Code) | [skills.sh/Gingiris-1031/gingiris-skills](https://skills.sh/Gingiris-1031/gingiris-skills) |
| **Blog** | [gingiris.tools/blog](https://gingiris.tools/blog/) |

### New Playbooks (June 2026)

| Playbook | ClawHub | HuggingFace |
|:---------|:--------|:------------|
| **competitor-research-playbook** — 竞品调研 SOP | [Install](https://clawhub.ai/gingiris/competitor-research-playbook) | [Dataset](https://huggingface.co/datasets/Gingiris/competitor-research-playbook) |
| **community-ambassador-playbook** — 社区大使运营 SOP | [Install](https://clawhub.ai/gingiris/community-ambassador-playbook) | [Dataset](https://huggingface.co/datasets/Gingiris/community-ambassador-playbook) |
| **product-dev-ops-playbook** — 产研运协同 SOP | [Install](https://clawhub.ai/gingiris/product-dev-ops-playbook) | [Dataset](https://huggingface.co/datasets/Gingiris/product-dev-ops-playbook) |
| **gingiris-seo-geo-agent** — SEO/GEO Agent 运营 | [Install](https://clawhub.ai/gingiris/gingiris-seo-geo-agent) | [Dataset](https://huggingface.co/datasets/Gingiris/gingiris-seo-geo-agent) |
