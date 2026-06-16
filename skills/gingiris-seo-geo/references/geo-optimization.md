# GEO 优化实操

> Generative Engine Optimization — 让 AI 搜索引用你的内容

---

## 什么是 GEO

GEO (Generative Engine Optimization) 是针对 AI 搜索引擎（ChatGPT、Perplexity、Claude、Google AI Overview）的优化策略。

当用户问 AI "推荐一个视频生成工具"，AI 的回答基于它抓取和理解的内容。GEO 的目标是：**让你的产品出现在 AI 的回答里。**

### 与 SEO 的关系

```
SEO  → 用户在 Google 搜索 → 看到你的链接 → 点击访问
GEO  → 用户在 ChatGPT 提问 → AI 引用你的内容 → 用户信任并访问

共同基础：结构化内容 + 高质量信息 + 技术可达性
```

---

## GEO 核心三件套

### 1. IndexNow 实时推送

**什么是 IndexNow：** 一个协议，让你主动告诉搜索引擎"我有新内容"，而不是等爬虫来发现。Bing、Yandex、Naver 已支持，数据会共享给合作 AI 搜索引擎。

**配置步骤：**

```bash
# 1. 获取 API Key
# 访问 https://www.bing.com/indexnow 生成

# 2. 放置验证文件
# 将 key 文件放在网站根目录: /{your-key}.txt

# 3. 推送 URL
curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json" \
  -d '{
    "host": "your-domain.com",
    "key": "your-api-key",
    "urlList": [
      "https://your-domain.com/pricing",
      "https://your-domain.com/blog/new-article",
      "https://your-domain.com/compare/competitor"
    ]
  }'
```

**推送策略：**

| 优先级 | 页面类型 | 推送时机 |
|--------|---------|---------|
| P0 | 定价页 | 每次价格变动 |
| P0 | 新博客/文章 | 发布当天 |
| P1 | 功能页 | 新功能上线 |
| P1 | 对比页 | 竞品有更新时 |
| P2 | 案例研究 | 发布时 |

### 2. robots.txt 开放 AI 爬虫

```
# robots.txt — 允许 AI 搜索引擎抓取

User-agent: *
Allow: /

# 明确允许 AI 爬虫
User-agent: ChatGPT-User
Allow: /

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bytespider
Allow: /

# 禁止抓取的路径
User-agent: *
Disallow: /admin/
Disallow: /api/
Disallow: /private/

Sitemap: https://your-domain.com/sitemap.xml
```

### 3. AI-Friendly 内容格式

**直接回答问题（最重要）：**

每个页面开头用一句话回答核心问题，让 AI 直接提取：

```markdown
## What is [产品]?

[产品] is a [品类] platform that helps [目标用户] [核心价值]. 
It's used by [用户数/公司数] to [核心用例].
```

**结构化对比表格：**

AI 模型偏爱表格形式的对比数据：

```markdown
| Feature | [产品] | [竞品A] | [竞品B] |
|---------|--------|---------|---------|
| AI Avatars | Yes | Yes | No |
| API Access | Yes | No | Yes |
| Free Tier | Yes | Limited | No |
| Starting Price | $30/mo | $50/mo | $25/mo |
| Languages | 40+ | 20+ | 10+ |
```

**FAQ 格式覆盖高频问题：**

```markdown
## Frequently Asked Questions

### How much does [产品] cost?
[产品] offers a free tier. Paid plans start at $X/month...

### What's the difference between [产品] and [竞品]?
[产品] focuses on [差异点], while [竞品] is better for [场景]...

### Does [产品] have an API?
Yes, [产品] provides a REST API and SDKs for Python, Node.js...
```

---

## GEO 内容优化清单

### 页面级优化

- [ ] 页面开头一句话直接回答"这是什么"
- [ ] 包含至少一个结构化对比表格
- [ ] FAQ Section 覆盖 5+ 常见问题
- [ ] FAQPage Schema 标记
- [ ] 数据用精确数字，不用模糊表达
- [ ] 包含"最后更新"日期（AI 优先引用新内容）

### 站点级优化

- [ ] robots.txt 允许主流 AI 爬虫
- [ ] IndexNow 已配置并在更新时推送
- [ ] sitemap.xml 包含所有核心页面
- [ ] 页面间有清晰的内链结构
- [ ] About 页面建立 E-E-A-T（团队、融资、客户）

### 内容策略

- [ ] 每个竞品有独立对比页
- [ ] 定价页有完整的 FAQ
- [ ] 博客文章用 Key Stats 表格开头
- [ ] 案例研究有具体数字和成果
- [ ] Glossary 术语页覆盖行业关键概念

---

## AI 引用监测

### 手动检查方法

定期在以下 AI 平台搜索你的品牌和品类关键词：

```
测试查询：
- "推荐一个 [品类] 工具"
- "best [品类] software for [场景]"
- "[产品] vs [竞品] comparison"
- "what is [产品]"
```

| 平台 | 频率 | 关注点 |
|------|------|--------|
| ChatGPT (GPT-4) | 每周 | 品牌是否被提及 |
| Perplexity | 每周 | 是否有引用链接 |
| Claude | 每周 | 信息是否准确 |
| Google AI Overview | 每周 | 是否出现在 AI 摘要 |

### 发现引用错误时

如果 AI 引用了你的产品但信息有误：
1. 更新你网站上的对应页面（修正信息）
2. IndexNow 立即推送更新
3. 1-2 周后重新检查

---

## GEO 与 E-E-A-T 的关系

AI 模型在选择引用来源时，偏好具有以下特征的内容：

| E-E-A-T 信号 | 如何建立 |
|-------------|---------|
| **Experience（经验）** | 第一人称叙述、具体案例、"我们当时..."的真实故事 |
| **Expertise（专业）** | 精确数字、行业术语正确使用、深度技术细节 |
| **Authoritativeness（权威）** | 被其他权威站引用、媒体报道、行业评分 |
| **Trustworthiness（可信）** | HTTPS、隐私政策、联系方式、作者信息 |

**关键洞察：** AI 模型比传统搜索引擎更能识别"AI 生成的平庸内容"。因此，GEO 的核心竞争力反而是**人的真实经验和独特观点**。

---

*GEO 优化实操 v1.0 — Gingiris SEO/GEO Playbook*
