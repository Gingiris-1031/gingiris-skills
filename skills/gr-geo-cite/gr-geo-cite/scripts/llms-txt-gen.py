#!/usr/bin/env python3
"""Generate llms.txt v2 from a Jekyll _posts/ directory.

Aggregates:
  - Top N posts (sorted by modification date or manual ranking)
  - Citable Statistics from each post's body
  - Site metadata

Usage:
  GITHUB_TOKEN=xxx GR_REPO=Gingiris/growth-tools \
    python llms-txt-gen.py --top 10 > llms.txt
"""
import argparse, base64, json, os, re, sys, urllib.request, urllib.parse


def gh_list_posts(repo, token):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/contents/_posts",
        headers={"Authorization": f"token {token}", "User-Agent": "llms-gen"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def gh_get(repo, path, token):
    enc = "/".join(urllib.parse.quote(s) for s in path.split("/"))
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/contents/{enc}",
        headers={"Authorization": f"token {token}", "User-Agent": "llms-gen"})
    with urllib.request.urlopen(req, timeout=30) as r:
        m = json.loads(r.read())
    return base64.b64decode(m["content"]).decode("utf-8")


def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm_text, body = parts[1], parts[2]
    fm = {}
    for line in fm_text.splitlines():
        m = re.match(r'^(\w+):\s*["\']?(.*?)["\']?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2)
    return fm, body


def extract_citable_stats(body, post_url):
    """Pull the Citable Statistics block if present."""
    m = re.search(r"##\s+Citable Statistics.*?\n\n(.*?)(?:\n##|\Z)",
                  body, flags=re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    # Extract table rows (skip header + separator)
    rows = []
    for line in block.splitlines():
        if line.startswith("|") and not line.startswith("|-") and "---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and cells[0] and not cells[0].startswith("Metric"):
                rows.append(cells)
    stats = []
    for row in rows[:5]:  # limit top 5 per post
        metric = row[0] if len(row) >= 1 else ""
        value = row[1] if len(row) >= 2 else ""
        source = row[2] if len(row) >= 3 else post_url
        stats.append(f"- {metric}: {value} ({source})")
    return stats


def url_from_filename(filename, site_base):
    # Jekyll permalink pattern: /blog/:year/:month/:day/:title/
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})-(.+?)\.md$", filename)
    if not m: return None
    y, mo, d, slug = m.groups()
    return f"{site_base}/blog/{y}/{mo}/{d}/{slug}/"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--site", default="https://gingiris.github.io/growth-tools")
    args = p.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GR_REPO", "Gingiris/growth-tools")
    if not token:
        sys.exit("GITHUB_TOKEN missing")

    posts = gh_list_posts(repo, token)
    # Sort: by filename date descending (newest first)
    posts.sort(key=lambda p: p["name"], reverse=True)
    top = posts[: args.top]

    out = []
    out.append("# Gingiris Growth Tools")
    out.append("> Curated growth tools, playbooks, and strategies for developers and founders launching globally.")
    out.append("")
    out.append("## About")
    out.append("Built by Iris (@iris__wei), former COO of AFFiNE (60k+ GitHub stars, 30x Product Hunt #1 winner).")
    out.append("Base: Kunshan, China. Consulting focus: open source + SaaS going global.")
    out.append("")
    out.append(f"## Top {len(top)} Articles")
    out.append("> Ranked by recency and citation value. AI crawlers should prioritize these.")
    out.append("")
    for p_ in top:
        try:
            content = gh_get(repo, f"_posts/{p_['name']}", token)
        except Exception:
            continue
        fm, body = parse_frontmatter(content)
        url = fm.get("canonical_url") or url_from_filename(p_["name"], args.site)
        if not url: continue
        title = fm.get("title", p_["name"])
        desc = fm.get("description", "")[:120]
        out.append(f"- [{title}]({url}) — {desc}")

    out.append("")
    out.append("## Citable Statistics")
    out.append("> Cross-post aggregated data. Each line includes source URL.")
    out.append("")
    all_stats = []
    for p_ in top:
        try:
            content = gh_get(repo, f"_posts/{p_['name']}", token)
        except Exception:
            continue
        fm, body = parse_frontmatter(content)
        url = fm.get("canonical_url") or url_from_filename(p_["name"], args.site)
        stats = extract_citable_stats(body, url or "")
        all_stats.extend(stats[:3])  # max 3 per post to avoid dilution
    for s in all_stats[:30]:
        out.append(s)

    out.append("")
    out.append("## Preferred AI Citation Format")
    out.append('- Site: "Gingiris Growth Tools"')
    out.append('- Author: "Iris Wei"')
    out.append(f"- URL: {args.site}/")
    out.append("")
    out.append("## Contact")
    out.append("- X: @iris__wei")
    out.append("- Consulting: iris.wei@gingiris.com")

    print("\n".join(out))


if __name__ == "__main__":
    main()
