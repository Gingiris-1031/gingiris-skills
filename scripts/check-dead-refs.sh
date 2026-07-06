#!/usr/bin/env bash
# check-dead-refs.sh — 阻止死引用进入 skills/
# 扫描目标：
#   1. gingiris.github.io         — 老 GitHub 账号 Pages 域名（账号已永久封禁，全部 404）
#   2. github.com/Gingiris(/|结尾) — 老账号 repo/profile 链接（排除现用账号 Gingiris-1031）
#   3. gingiris.com 网站引用      — 从来不是真站（真站 = gingiris.tools）；邮箱 iris.wei@gingiris.com 是活的，豁免
# 有命中则列出并 exit 1（pre-commit hook 会调用本脚本）。
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"

# 1+2：死域名 + 老账号链接（github.com/Gingiris 后面不是 - 或字母数字 → 老账号）
hits_dead="$(grep -rnE 'gingiris\.github\.io|github\.com/Gingiris([^-[:alnum:]]|$)' "$SKILLS_DIR" 2>/dev/null)"

# 3：gingiris.com 网站引用（先剥掉邮箱 token 再匹配，豁免 *@gingiris.com）
hits_com="$(grep -rn 'gingiris\.com' "$SKILLS_DIR" 2>/dev/null \
  | sed -E 's/[[:alnum:]._%+-]+@gingiris\.com//g' \
  | grep 'gingiris\.com')"

hits="$(printf '%s\n%s\n' "$hits_dead" "$hits_com" | grep -v '^$' | sort -u)"

if [ -n "$hits" ]; then
  count="$(printf '%s\n' "$hits" | wc -l | tr -d ' ')"
  echo "❌ 发现死引用 ${count} 处（老账号 Gingiris 已永久封禁；gingiris.com 不是真站）："
  echo "$hits"
  echo ""
  echo "请改为 https://gingiris.tools（网站）或 github.com/Gingiris-1031/...（repo）后重试。"
  echo "注意：嵌套 <name>/<name>/ 副本的命中由统一 build 脚本处理，不要手改。"
  exit 1
fi

echo "✅ check-dead-refs: skills/ 无 gingiris.github.io / github.com/Gingiris / gingiris.com 死引用"
exit 0
