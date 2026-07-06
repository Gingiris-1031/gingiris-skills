#!/usr/bin/env bash
# sync-nested.sh — 嵌套打包副本统一构建脚本
#
# 背景：npx skills add 只装 SKILL.md 所在目录，root 级 SKILL.md 会丢 references/，
# 所以部分 skill 采用 <name>/<name>/ 嵌套打包结构（外层=源，嵌套层=分发打包产物）。
# 本脚本把外层内容 rsync 进嵌套层，保证字节级一致。嵌套层【禁止手改】，改外层后重跑本脚本。
#
# 用法：bash scripts/sync-nested.sh
#
# EXCLUDES 数组：标注"不随公开分发"的内部文件（相对 skill 根的路径）。
# 格式："<skill-name>:<relative-path>"。这些文件保留在外层（本机/私有用途），
# 不进入嵌套打包层；若嵌套层已存在则清除。以后有新条目直接往数组里加。
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"

EXCLUDES=(
  # gingiris-twitter-agent-ops 的私有运营手册（SKILL 内标注不随公开分发）
  "gingiris-twitter-agent-ops:references/weiyipei-ops.md"
  # gr-backlinks 的内部台账（花费记录/内部 memory 引用，非公开内容）
  "gr-backlinks:data/"
)

synced=0
for dir in "$SKILLS_DIR"/*/; do
  name="$(basename "$dir")"
  nested="$dir$name"
  [ -d "$nested" ] || continue

  # rsync 参数：-a 归档；--delete 清理嵌套层多余文件使其与外层一致；
  # --exclude "/$name/" 防套娃（不把嵌套层自己拷进自己）。
  args=(-a --delete --exclude "/$name/")

  # 本 skill 的私有排除项
  for entry in "${EXCLUDES[@]}"; do
    skill="${entry%%:*}"
    path="${entry#*:}"
    if [ "$skill" = "$name" ]; then
      args+=(--exclude "/$path")
      # 嵌套层若已存在该私有文件，清除（--exclude 会保护它不被 --delete 删掉，所以显式删）
      if [ -e "$nested/$path" ] || [ -e "${nested}/${path%/}" ]; then
        rm -rf "${nested:?}/${path%/}"
        echo "  🧹 $name: 已从嵌套层清除私有文件 $path"
      fi
    fi
  done

  rsync "${args[@]}" "$dir" "$nested/"
  synced=$((synced + 1))
  echo "  ✅ $name → $name/$name/ 已同步"
done

echo ""
echo "sync-nested: 共同步 $synced 个嵌套打包副本"

# 校验：外层 vs 嵌套层应字节级一致（忽略嵌套层本身与私有排除项）
fail=0
for dir in "$SKILLS_DIR"/*/; do
  name="$(basename "$dir")"
  nested="$dir$name"
  [ -d "$nested" ] || continue
  diffout="$(diff -rq "$dir" "$nested" 2>/dev/null | grep -v "^Only in ${dir%/}: $name\$" || true)"
  # 私有排除项在外层存在、嵌套层没有，属预期，过滤掉
  for entry in "${EXCLUDES[@]}"; do
    skill="${entry%%:*}"
    path="${entry#*:}"
    if [ "$skill" = "$name" ]; then
      base="$(basename "${path%/}")"
      diffout="$(printf '%s\n' "$diffout" | grep -v ": ${base}\$" || true)"
    fi
  done
  diffout="$(printf '%s\n' "$diffout" | grep -v '^$' || true)"
  if [ -n "$diffout" ]; then
    echo "❌ $name 外层与嵌套层不一致："
    echo "$diffout"
    fail=1
  fi
done

if [ "$fail" -eq 1 ]; then
  echo "sync-nested: 校验失败"
  exit 1
fi
echo "✅ sync-nested: 全部嵌套副本与外层字节级一致"
