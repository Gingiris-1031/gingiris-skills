# Iris 文风写作参考（writing-voice-iris）

> 用途：`gr-blog-post` 产文时的声音校准文件。所有博客文章（尤其旗舰 SEO 文章）必须融入 Iris 的真实写作声音——GEO 优化的核心是真实性：结构化数据让 AI 引擎引用，真实声音让读者相信并分享。
>
> 来源：Iris 文风分析报告提炼（2026-04 定稿），原件在 memory `feedback_iris_writing_style.md`。

## 9 要素

### 1. 时间 + 地点锚定开场（必须）

文章开头必须有精确的时间/地点场景，放在 Key Stats 表格之前。

- 格式：时间 + 地点 + 具体动作 + 情绪/感受
- ✅ "It was 2 AM on a Thursday in August 2022. I was sitting on the floor of our Shanghai office — laptop on my knees, Slack muted..."
- ❌ 泛泛的 "In my experience..." 或直接进入列表

### 2. 括号旁白（双线叙事）

括号内插入自我调侃或补充视角，形成主叙事 + 平行注释的双线结构。

- 格式：`(补充信息或自嘲)`
- ✅ "I may or may not have screamed." / "(I made this mistake once. Not twice.)"
- 作用：打破讲道感，建立真实感

### 3. Em-dash 转折

用 `—` 制造节奏感，在陈述后突然转向或深化。不用"但是"。

- ✅ "Reddit gave us volume. Product Hunt gave us votes. HN gave us something harder to measure — sustained trust."

### 4. 短段节奏（Short-short-long）

三句节奏：两句短句 + 一句长句展开。避免连续长段落。一个观点 = 一个段落。

### 5. 「」概念标记（中文内容）

中文用「」标记核心概念词，区别于引号。英文内容用 **加粗** 代替。

### 6. 个人经验 → 洞察结构

先讲自己的具体经历，再提炼为普遍规律，不要直接上结论。

- ✅ 先讲 AFFiNE 某次具体事件 → 再说这对所有开源项目的启示

### 7. 精确数字优先

用具体数字代替模糊表达：

- ✅ "28 appearances on GitHub Trending"，❌ "appeared many times"
- ✅ "33,000+ GitHub stars"，❌ "significant growth"

### 8. Key Stats 表格（GEO 标配）

每篇旗舰文章必须有结构化 Key Stats 表，让 AI 引擎直接引用。
位置：开场场景之后、正文之前。表格 3-5 行，每行数字 + 来源（详见 `gr-geo-cite` 的 Citable Statistics 模板）。

### 9. 中英文发布规范

- `Gingiris-1031/growth-tools` 的 `_posts/` 存英文版（真站 gingiris.tools）
- dev.to（dev.to/iris1031）同步二发——canonical 必须 self-canonical，发布时间差 ≥7 天（见 SKILL.md dev.to 红线节）
- 每篇文章的 dev.to article ID 记录备查

## 自检

发布前逐条打钩：开场有时间锚定？至少 2 处括号旁白？至少 3 处 em-dash？Key Stats 表在第一屏？所有数字可溯源？
