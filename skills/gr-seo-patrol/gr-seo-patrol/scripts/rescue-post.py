#!/usr/bin/env python3
"""Rescue a SERP-crashed post:
  1) Rewrite title so primary keyword is front-loaded
  2) Inject 3 internal links from high-authority posts

Usage:
  GITHUB_TOKEN=xxx GR_REPO=Gingiris/growth-tools \\
    python rescue-post.py \\
      --target 2026-04-02-best-social-media-listening-tools.md \\
      --url https://gingiris.github.io/growth-tools/blog/2026/04/02/.../  \\
      --title "Best Social Listening Tools 2026: Free & Multilingual for Startups" \\
      --anchor "best social listening tools for startups" \\
      --referrers 2026-03-25-ph-master.md 2026-03-30-reddit.md 2026-04-03-saas.md \\
      --apply
"""
import argparse, base64, json, os, re, sys, urllib.request

GH = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GR_REPO", "Gingiris/growth-tools")


def gh(path, method="GET", body=None):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        method=method, data=body,
        headers={"Authorization": f"token {GH}",
                 "User-Agent": "gr-seo-patrol",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def rewrite_title(path, new_title, apply):
    m = gh(path)
    content = base64.b64decode(m["content"]).decode("utf-8")
    new = re.sub(r"^title:\s*.*$", f'title: "{new_title}"',
                 content, count=1, flags=re.MULTILINE)
    if new == content:
        print(f"  [title] no change"); return
    if not apply:
        print(f"  [title dry] would rewrite {path}"); return
    payload = json.dumps({
        "message": "seo: front-load primary keyword in title",
        "content": base64.b64encode(new.encode()).decode(),
        "sha": m["sha"]}).encode()
    r = gh(path, "PUT", payload)
    print(f"  [title ok] {r['commit']['sha'][:8]}")


def inject_link(path, url, anchor, apply):
    m = gh(path)
    body = base64.b64decode(m["content"]).decode("utf-8")
    if url in body:
        print(f"  [link skip] {path} (already linked)"); return
    block = (f"\n\n> **Related reading:** [{anchor.capitalize()}]({url}) — "
             f"how to monitor brand mentions & competitor buzz without a $500/mo tool.\n")
    parts = body.split("\n## ", 2)
    if len(parts) >= 3:
        new = parts[0] + "\n## " + parts[1] + block + "\n## " + parts[2]
    elif len(parts) == 2:
        new = parts[0] + "\n## " + parts[1] + block
    else:
        new = body + block
    if not apply:
        print(f"  [link dry] would link from {path}"); return
    payload = json.dumps({
        "message": f"seo: internal link (anchor: {anchor})",
        "content": base64.b64encode(new.encode()).decode(),
        "sha": m["sha"]}).encode()
    r = gh(path, "PUT", payload)
    print(f"  [link ok] {path}: {r['commit']['sha'][:8]}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", required=True, help="file under _posts/")
    p.add_argument("--url", required=True, help="target post public URL")
    p.add_argument("--title", required=True, help="new title")
    p.add_argument("--anchor", required=True, help="internal-link anchor text")
    p.add_argument("--referrers", nargs="+", required=True,
                   help="referrer filenames under _posts/")
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    if not GH:
        sys.exit("GITHUB_TOKEN missing")
    tgt = args.target if args.target.startswith("_posts/") else f"_posts/{args.target}"
    print(f"[1] title rewrite: {tgt}")
    try:
        rewrite_title(tgt, args.title, args.apply)
    except urllib.error.HTTPError as e:
        print(f"  [title err] {e.code}")
    print(f"[2] internal links from {len(args.referrers)} referrers")
    for r in args.referrers:
        rp = r if r.startswith("_posts/") else f"_posts/{r}"
        try:
            inject_link(rp, args.url, args.anchor, args.apply)
        except urllib.error.HTTPError as e:
            print(f"  [link err] {rp}: {e.code}")


if __name__ == "__main__":
    main()
