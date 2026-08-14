# Skills 三层结构与同步管线

> 最后更新：2026-07-06。monorepo 是 ClawHub / skills.sh 的分发源和 SEO 资产：
> **不删除 skill 目录、不缩减对外 description、不减少对外内容。**

## 三层结构

| 层 | 位置 | 身份 | 能否手改 |
|---|---|---|---|
| 1. 分发源 | `skills/<name>/` | 唯一可编辑源，全量内容（含完整多语 description） | ✅ 只改这里 |
| 2. 嵌套打包产物 | `skills/<name>/<name>/` | `scripts/sync-nested.sh` 生成的打包副本（npx skills add 只装 SKILL.md 所在目录，嵌套层保住 references/） | ❌ 禁止手改 |
| 3. 本机运行时 | `~/.claude/skills/<name>/`（多为 symlink → `~/.agents/skills/<name>/`） | `scripts/sync-local.py` 生成的精简版构建产物（description 截 ~320 字符 + 前 8 个 Triggers，省 context） | ❌ 禁止手改 |

## 改动流程

```
改 skills/<name>/ 下的源文件
  → bash scripts/sync-nested.sh    # 重建嵌套打包副本（字节级一致校验）
  → python3 scripts/sync-local.py  # 重建本机精简副本（幂等）
  → ruby scripts/validate-skills.rb # 全量结构、引用、隐私与打包校验
完成
```

## 防线与规则

- **`scripts/check-dead-refs.sh` 是 pre-commit 防线**：commit 前必须过
  （拦 gingiris.github.io / 老账号 github.com/Gingiris / gingiris.com；
  `*@gingiris.com` 邮箱豁免）。
- 私有文件不进分发：`sync-nested.sh` 顶部的 `EXCLUDES` 数组
  （现有 gingiris-twitter-agent-ops 的 `references/weiyipei-ops.md`、
  gr-backlinks 的 `data/`），新增私有文件直接加条目。
- 本机孤儿 skill（monorepo 没有的，如 gingiris-reddit-marketing）：
  sync-local.py 不覆盖、只精简 description（原文备份为 `SKILL.md.orig`）；
  源码防丢备份在本仓 `archive/`（不在 skills/ 内，不进分发）。

## 全量执行验收

每次发布不抽查旗舰 skill，而是对 `skills/*/SKILL.md` 全量验收。发布数以实际顶层目录为准，不手填在多个平台。发布前依次运行：

```bash
bash scripts/sync-nested.sh
ruby scripts/validate-skills.rb
bash scripts/check-dead-refs.sh
GINGIRIS_SKILL_REPORT=/tmp/gingiris-skill-report.json ruby scripts/validate-skills.rb
```

`validate-skills.rb` 会逐个解析 frontmatter、核对目录名与 `name`、检查嵌套安装包字节一致性、阻止私有文件进入公开包，并扫描旧 GitHub 身份、旧站点和错误 ClawHub handle。非零退出码即禁止发布到 GitHub、Hugging Face、ClawHub、gingiris.tools 或 skills.sh。
