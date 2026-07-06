#!/usr/bin/env python3
"""sync-local.py — 本机安装构建器（本机副本 = 构建产物，禁止手改）

对 ~/.claude/skills/ 下已安装、且 monorepo skills/ 有同名目录的每个 skill：
  1. 从 monorepo 复制全部内容覆盖本机（symlink 条目写入其解析后的真实路径，
     即 ~/.agents/skills/<name>/，两处同时生效）；
  2. 本机侧 SKILL.md 的 frontmatter description 转换为精简版：
     取原 description 第一段英文（原文以中文为主则取中文段）截到 ~350 字符
     + 原文 Triggers: 行的前 8 个触发词组拼成一行。
     name / 其余 frontmatter 字段保留，正文不动。

跳过：lark-*（symlink 到 lark 工具链）、web-access、skills/（垃圾目录）。
孤儿（monorepo 没有的本机目录）：不覆盖，但同样做 description 精简，
  首次改动前备份原文件为 SKILL.md.orig；以后每次从 .orig 重新生成（幂等）。

monorepo 侧内容永远全量不动；本脚本只写本机侧。幂等：重复运行结果一致。

用法：python3 scripts/sync-local.py
"""
import os
import re
import shutil
import subprocess
import sys

MONO_SKILLS = "/Users/iriscarrot/Downloads/gingiris-skills/skills"
LOCAL_SKILLS = os.path.expanduser("~/.claude/skills")

PARA_LIMIT = 320          # 精简后描述段落的目标字符数（总量目标 <10,000）
MAX_TRIGGERS = 8          # Triggers 行保留的触发词组数

SKIP_PREFIXES = ("lark-",)
SKIP_NAMES = {"web-access", "skills"}
# monorepo 没有、但本机存在的孤儿：不覆盖，只精简 description
KNOWN_ORPHANS = {"gingiris-reddit-marketing", "gingiris-seo-geo-workspace"}


def cjk_ratio(text: str) -> float:
    if not text:
        return 0.0
    cjk = sum(1 for ch in text if "一" <= ch <= "鿿")
    letters = sum(1 for ch in text if ch.isalpha() or "一" <= ch <= "鿿")
    return cjk / letters if letters else 0.0


def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?\n)---\n?", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


def extract_description(fm: str):
    """返回 (description 原始块含 key 行, 值文本, span)。找不到返回 None。"""
    m = re.search(
        r"^description:[^\n]*\n?(?:^(?:[ \t]+[^\n]*)?\n)*",
        fm, re.M,
    )
    if not m:
        return None
    block = m.group(0)
    first_line = block.split("\n", 1)[0]
    inline = re.sub(r"^description:\s*", "", first_line).strip()
    body_lines = block.split("\n")[1:]
    if inline and inline not in (">", ">-", "|", "|-", ">+", "|+"):
        value = inline + "\n" + "\n".join(l.strip() for l in body_lines if l.strip())
    else:
        value = "\n".join(re.sub(r"^[ \t]+", "", l) for l in body_lines)
    return block, value.strip(), m.span()


def condense(value: str) -> str:
    """第一段（英文优先，中文为主则中文段）截 ~350 字符 + Triggers 前 8 词组。"""
    paras = [p.strip() for p in re.split(r"\n\s*\n", value) if p.strip()]
    # 分离 Triggers 行
    triggers_text = ""
    content_paras = []
    for p in paras:
        tm = re.search(r"Triggers?\s*[:：]\s*(.+)", p, re.S)
        if tm and not triggers_text:
            triggers_text = tm.group(1)
            pre = p[: tm.start()].strip()
            if pre:
                content_paras.append(pre)
        else:
            content_paras.append(p)
    if not content_paras:
        content_paras = [value]

    mostly_cjk = cjk_ratio(value) > 0.5
    chosen = None
    for p in content_paras:
        r = cjk_ratio(p)
        if mostly_cjk and r > 0.3:
            chosen = p
            break
        if not mostly_cjk and r < 0.3:
            chosen = p
            break
    if chosen is None:
        chosen = content_paras[0]
    # 去掉开头的国旗 emoji 标记
    chosen = re.sub(r"^(🇺🇸|🇨🇳|🇯🇵|🇰🇷)\s*", "", chosen)
    chosen = re.sub(r"\s+", " ", chosen).strip()
    if len(chosen) > PARA_LIMIT:
        cut = chosen[:PARA_LIMIT]
        # 尽量在词/标点边界截断
        m = re.search(r"^.*[\s，。；、,.;]", cut, re.S)
        if m and len(m.group(0)) > PARA_LIMIT * 0.6:
            cut = m.group(0)
        chosen = cut.rstrip(" ，,;；、") + "…"

    result = chosen
    if triggers_text:
        phrases = [t.strip() for t in triggers_text.replace("\n", " ").split("|")]
        phrases = [t for t in phrases if t][:MAX_TRIGGERS]
        if phrases:
            result += "\n" + "Triggers: " + " | ".join(phrases)
    return result


def rebuild_frontmatter(fm: str, new_desc: str) -> str:
    found = extract_description(fm)
    if not found:
        return fm
    _, _, (start, end) = found
    lines = new_desc.split("\n")
    block = "description: >-\n" + "".join(f"  {l}\n" for l in lines)
    return fm[:start] + block + fm[end:]


def trim_skill_md(path: str, source_text: str = None):
    """精简 path 的 description。source_text 提供时以它为原文（幂等用）。
    返回 (before_len, after_len)，无 description 返回 None。"""
    text = source_text if source_text is not None else open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(text)
    if fm is None:
        return None
    found = extract_description(fm)
    if not found:
        return None
    _, value, _ = found
    new_desc = condense(value)
    new_fm = rebuild_frontmatter(fm, new_desc)
    current = open(path, encoding="utf-8").read()
    new_text = "---\n" + new_fm + "---\n" + body
    if new_text != current:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
    return len(value), len(new_desc)


def main():
    mono_names = {
        n for n in os.listdir(MONO_SKILLS)
        if os.path.isdir(os.path.join(MONO_SKILLS, n))
    }
    total_before = total_after = 0
    rows = []
    for name in sorted(os.listdir(LOCAL_SKILLS)):
        if name.startswith("."):
            continue
        local_path = os.path.join(LOCAL_SKILLS, name)
        if name.startswith(SKIP_PREFIXES) or name in SKIP_NAMES:
            continue
        if not os.path.isdir(local_path):  # 死 symlink 等
            continue
        real = os.path.realpath(local_path)

        if name in mono_names:
            src = os.path.join(MONO_SKILLS, name)
            # 覆盖本机（写入 symlink 解析后的真实路径）。不带 --delete：
            # 保留本机运行时状态文件；monorepo 内容以 monorepo 为准全量覆盖。
            subprocess.run(
                ["rsync", "-a", src + "/", real + "/"],
                check=True,
            )
            skill_md = os.path.join(real, "SKILL.md")
            if os.path.isfile(skill_md):
                res = trim_skill_md(skill_md)
            else:
                res = None
            tag = "mono→local"
        else:
            # 孤儿：不覆盖，只精简；备份 .orig 后以 .orig 为原文（幂等）
            skill_md = os.path.join(real, "SKILL.md")
            if not os.path.isfile(skill_md):
                rows.append((name, "-", "-", "orphan (无 SKILL.md，跳过)"))
                continue
            orig = skill_md + ".orig"
            if not os.path.exists(orig):
                shutil.copy2(skill_md, orig)
            res = trim_skill_md(skill_md, source_text=open(orig, encoding="utf-8").read())
            tag = "orphan (仅精简, 原文→SKILL.md.orig)"

        if res is None:
            rows.append((name, "-", "-", tag + " (无 description)"))
            continue
        before, after = res
        total_before += before
        total_after += after
        rows.append((name, before, after, tag))

    width = max(len(r[0]) for r in rows) + 2
    print(f"{'skill'.ljust(width)}before → after   模式")
    for name, b, a, tag in rows:
        print(f"{name.ljust(width)}{str(b).rjust(6)} → {str(a).ljust(6)} {tag}")
    print()
    saved = total_before - total_after
    pct = (saved / total_before * 100) if total_before else 0
    print(f"description 总量: {total_before} → {total_after} 字符，节省 {saved} ({pct:.0f}%)")
    print("（lark-* / web-access / skills/ 已按规则跳过，不计入）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
