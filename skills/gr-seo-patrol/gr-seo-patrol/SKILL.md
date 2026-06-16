---
name: gr-seo-patrol
description: >
  每日 SEO/GEO 巡逻。覆盖：SERP 关键词排名追踪（DataForSEO）、Google 索引数统计、llms.txt 可达性、
  GA4 tag 部署检测、PH canonical 合并修复、社媒关键词雪崩救援（title 重写 + 内链注入）。
  当用户说"跑 SEO 日报"、"检查排名"、"某关键词掉了"、"修 canonical"、"加内链"时调用。
when_to_use: |
  Use this skill when you need to: run daily SEO/GEO patrol, track SERP keyword rankings,
  fix canonical issues, inject internal links to rescue underperforming posts, check GA4
  tag deployment, verify llms.txt accessibility, or diagnose why a keyword ranking dropped.
  Trigger phrases: "SEO日报" | "跟踪排名" | "SEO patrol" | "canonical修复" |
  "加内链" | "keyword dropped" | "GA4检查" | "llms.txt" | "搜索排名跟踪"
metadata:
  author: Iris / Gingiris
  version: "0.1.0"
---

# gr-seo-patrol — SEO/GEO 日常巡逻

## 什么时候用

| 场景 | 动作 |
|---|---|
| "跑今日 SEO 日报" | 执行完整巡逻（scripts/daily-report.py） |
| "某关键词排名掉了" | 单词诊断（scripts/diag-keyword.py） |
| "修 canonical" | 批量合并（scripts/canonical-fix.py） |
| "救一下这篇文章" | 社媒救援（scripts/rescue-post.py）—— title 前置 + 3 个高权重内链 |
| "检查 GA4 部署" | 扫 HTML 里的 G-XXXXX tag |
| "查 llms.txt" | HTTP 200 + 字节数 |

---

## 核心流程

### 1. 日报模式
输入：无（全自动） 或 指定关键词清单
输出：
- 关键词排名 diff 表（今日 vs 昨日基线）
- Google 索引数
- llms.txt 状态
- GA4 覆盖状态
- 🚨 异常提示（跌出 top 100、整体刷新）

### 2. 单词诊断
输入：1 个关键词
过程：
1. 跑 4-5 个 long-tail 变体 SERP
2. 检查目标 URL 是否 HTTP 200
3. 用 `site:` 查询确认是否索引
4. 对比 3 天前的数据（如果有历史）
输出：雪崩 / 个别 / SERP 刷新 / 死链 四选一

### 3. Canonical 批量修复
输入：同主题的 N 篇文章 + 1 个 master URL
过程：替换每篇 frontmatter 里的 `canonical_url:` → master，GitHub API PUT
安全护栏：
- 只改 `_posts/` 下的 .md
- 每篇 commit 独立（方便回滚）
- 跳过 ja/ko（hreflang 替代，保持 self-canonical）

### 4. 社媒救援
输入：1 个雪崩 URL
动作：
- a. 重写 title：主关键词前置，长度 ≤ 60 字
- b. 从 top-3 高权重文章注入内链（带 anchor text = 目标关键词）
- c. 记录修改前后到日志

---

## API 依赖

| Service | Env var | 用途 |
|---|---|---|
| DataForSEO | `DATAFORSEO_B64` | SERP 查询 |
| GitHub PAT | `GITHUB_TOKEN` | 读写 `_posts/` |

完整 key 模板见 `docs/api-keys-template.md`。

---

## SERP 查询模板

```python
import urllib.request, json
def serp(kw, loc=2840, lang="en", depth=100):
    key = os.environ["DATAFORSEO_B64"]
    payload = json.dumps([{"keyword": kw, "location_code": loc,
                           "language_code": lang, "device": "desktop",
                           "depth": depth}]).encode()
    req = urllib.request.Request(
        "https://api.dataforseo.com/v3/serp/google/organic/live/advanced",
        data=payload,
        headers={"Authorization": f"Basic {key}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read())
```

常用 location_code：
- 2840 US / 2826 UK / 2392 JP / 2410 KR / 2156 CN（无效，中国不返回）

---

## 执行脚本

实际可执行的脚本在 `scripts/` 下：

- `daily-report.py` — 完整日报
- `canonical-fix.py` — canonical 批量合并
- `rescue-post.py` — 社媒文章救援
- `diag-keyword.py` — 单关键词诊断

每个脚本独立可跑。调用时优先用 Bash 工具，不要重写脚本。

---

## 输出规范

1. **先给表格，再给结论**
2. **差异用箭头**：`#6 ↑` / `#19 ↓↓`
3. **超过 3 项异常** → 单独开"🚨 异常"一节
4. **所有排名必须带 location_code**，不要假设

---

## 级联推荐

- 发现 cannibalization（同一关键词多篇排名接近） → `gr-blog-post` 做 canonical 整合
- 发现 N 个关键词同日跌出 top 100 → 先等 24h，不要硬改内容
- 发现新关键词机会（长尾 top 30） → `gr-blog-post` 扩写

---

## 反模式

- ❌ 不要用 `grep` / `find` 扫 `_posts/`，改用 GitHub Contents API
- ❌ 不要在生产环境直接 `git push` —— 用 Contents API 的 PUT
- ❌ 不要一次 serp 50 个关键词 —— 批量过大易触发 rate limit，按 6-10 个一批
- ❌ canonical 改到 master 后不要立刻 force Google 重新索引 —— 等 3-7 天自然爬取


---

## Monthly Full-Site Audit Workflow

> **Validated 2026-05-07 on 58 pages**: caught 43 SERP-truncating titles + 36 schema warns + 27 stop-word slugs in a single 30-min pass. Single layout-level fix (commit `24a0410e`) resolved 20 of 43 title issues.

Run **once per month** before `phase2-monthly-checkpoint`. Output: HTML report + machine-readable findings.json archived to `gingiris-skills/data/audit-{YYYY-MM-DD}.json`.

### Stage 1 — Discovery (5 min)

```python
import urllib.request, re
sm = urllib.request.urlopen("https://gingiris.github.io/growth-tools/sitemap.xml").read().decode()
urls = [u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if "/blog/" in u]
# typically 50-70 URLs
```

### Stage 2 — Parallel Audit (20 min for 60 pages, 4 threads)

Use the **adopted seo-audit-skill scripts** in `scripts/`:

```bash
# For each URL — run 2 scripts in parallel
python3 scripts/check-page.py URL --timeout 20    # title, H1, meta, canonical, slug, alt, keyword placement
python3 scripts/check-schema.py URL --timeout 20  # JSON-LD validation
```

Or batch with Python's `concurrent.futures.ThreadPoolExecutor(max_workers=4)`. Don't go higher than 4 — GitHub Pages CDN throttles aggressive parallel hits.

Each script outputs structured JSON envelope:
```json
{"field": {"status": "pass|warn|fail|info", "detail": "...", "llm_review_required": false}}
```

### Stage 3 — Aggregate Findings

Bucket by category:
- **Title length** > 70 chars (SERP truncation risk)
- **H1 length** > 70 chars (mobile readability)
- **Meta description** < 80 or > 170 chars
- **Schema warns** by @type (BlogPosting, Article, Organization)
- **Canonical issues** (mismatch with final URL)
- **Slug issues** (stop words, uppercase, missing keyword)
- **Image alt text** missing on content images

Save aggregated counts + per-issue URL lists to `findings.json`.

### Stage 4 — Layered Fix Strategy (HIGH ROI ORDER)

**1️⃣ Layout-level fixes first** (1 commit, fixes 20+ pages):
- Schema bugs in `_layouts/default.html`
- Site-name suffix in `<title>` tag
- Missing `dateModified` from `last_modified_at` frontmatter
- Organization / Publisher / contactPoint completeness

**2️⃣ Config-level fixes** (1 commit, fixes site-wide):
- `_config.yml` — logo URL (must be absolute), twitter, social, author structure

**3️⃣ Per-article batch fixes** (1 commit per file, parallelizable):
- Trim long titles while preserving keyword (target ≤ 70 chars, ideal 50-60)
- Trim long H1s (target ≤ 70 chars)
- Expand short meta descriptions (target 120-160 chars)
- Add missing Citable Statistics blocks for top GSC-impression pages

**4️⃣ Skip these (low ROI):**
- Slug stop words (changing breaks 301)
- Old articles with <50 imp/month (low traffic = low fix priority)

### Stage 5 — Verify (after Jekyll rebuild ~60-90s)

Re-run `check-schema.py` on a sample page. Confirm `status: pass` for at least:
Article · BlogPosting · Organization · FAQPage

### Stage 6 — Archive

Commit `findings.json` to `gingiris-skills/data/audit-{YYYY-MM-DD}.json` for trend tracking.
Add 2-5 atoms documenting any new lessons learned.

---

## HARD RULE (anti-hallucination guardrail)

> Adopted from [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) — strict whitelist pattern.

⛔ **Output ONLY the checks defined in the audit script's JSON envelope.**
- Do NOT add "bonus" checks not in the script output
- Do NOT contradict the script's `status` field unless you have additional observable evidence
- Do NOT invent metrics like "EEAT score 89" — third-party scoring tools are unofficial (per Google's 2026 guidance)
- Do NOT include checks marked `llm_review_required: false` in your judgment commentary — the script's `status` is final
- If `llm_review_required: true`, make explicit judgment, document reasoning, then update status

The script envelope is the **single source of truth**. Treat it as a strict whitelist.

---

## Companion skill

For single-page audits (not full-site), the same scripts power **[JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill)** which produces a polished HTML audit report.
Install as a complementary skill if you want client-presentable per-page audits.
