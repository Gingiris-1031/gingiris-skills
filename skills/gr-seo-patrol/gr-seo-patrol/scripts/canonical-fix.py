#!/usr/bin/env python3
"""Batch-update canonical_url in Jekyll _posts to point at a master URL.

Usage:
  GITHUB_TOKEN=xxx GR_REPO=Gingiris/growth-tools \\
    python canonical-fix.py \\
      --master https://gingiris.github.io/growth-tools/blog/2026/03/25/master-post/ \\
      --posts 2026-03-18-a.md 2026-03-29-b.md ...

Safety:
- Only touches files under _posts/
- One commit per file (easy to revert)
- Dry-run by default; pass --apply to write
"""
import argparse, base64, json, os, re, sys, urllib.request

GH = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GR_REPO", "Gingiris/growth-tools")


def gh(path, method="GET", body=None):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        method=method,
        data=body,
        headers={"Authorization": f"token {GH}",
                 "User-Agent": "gr-seo-patrol",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--master", required=True)
    p.add_argument("--posts", nargs="+", required=True,
                   help="Filenames inside _posts/ (with or without prefix)")
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    if not GH:
        sys.exit("GITHUB_TOKEN env var missing")

    for name in args.posts:
        path = name if name.startswith("_posts/") else f"_posts/{name}"
        if not path.endswith(".md"):
            print(f"SKIP {path}: not .md"); continue
        try:
            m = gh(path)
        except urllib.error.HTTPError as e:
            print(f"SKIP {path}: {e.code}"); continue
        content = base64.b64decode(m["content"]).decode("utf-8")
        new, n = re.subn(r"^(canonical_url:\s*).*$",
                         f"\\1{args.master}", content,
                         count=1, flags=re.MULTILINE)
        if n == 0:
            print(f"SKIP {path}: no canonical_url line"); continue
        if new == content:
            print(f"SKIP {path}: already correct"); continue
        if not args.apply:
            print(f"[dry] would update {path}"); continue
        payload = json.dumps({
            "message": "fix: canonical -> master",
            "content": base64.b64encode(new.encode()).decode(),
            "sha": m["sha"]}).encode()
        r = gh(path, "PUT", payload)
        print(f"OK   {path}: {r['commit']['sha'][:8]}")


if __name__ == "__main__":
    main()
