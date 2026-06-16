#!/usr/bin/env python3
"""Daily SEO/GEO patrol — gingiris-skills / gr-seo-patrol.

Env vars required:
  DATAFORSEO_B64   Basic-auth b64 for DataForSEO
  GITHUB_TOKEN     PAT for repo reads (optional but recommended)
  GR_KEYWORDS      comma-separated keyword overrides (optional)
  GR_SITE          site domain (default: gingiris.github.io/growth-tools)
  GR_GA4_ID        GA4 measurement ID to verify (default: G-QKPQFJD1FH)
"""
import os, sys, json, time, urllib.request, urllib.error

API = os.environ.get("DATAFORSEO_B64")
SITE = os.environ.get("GR_SITE", "gingiris.github.io/growth-tools")
GA4 = os.environ.get("GR_GA4_ID", "G-QKPQFJD1FH")

DEFAULT_KEYWORDS = [
    ("product hunt launch playbook", 2840, "en"),
    ("best social media listening tools", 2840, "en"),
    ("github stars history", 2840, "en"),
    ("open source marketing", 2840, "en"),
    ("how to launch on hacker news", 2840, "en"),
    ("GEO generative engine optimization", 2840, "en"),
]

TARGETS = [f"https://{SITE}/", f"https://{SITE}/en/",
           f"https://{SITE}/ja/", f"https://{SITE}/ko/"]


def serp(kw, loc, lang):
    if not API:
        return {"error": "DATAFORSEO_B64 missing"}
    payload = json.dumps([{"keyword": kw, "location_code": loc,
                           "language_code": lang, "device": "desktop",
                           "depth": 100}]).encode()
    req = urllib.request.Request(
        "https://api.dataforseo.com/v3/serp/google/organic/live/advanced",
        data=payload,
        headers={"Authorization": f"Basic {API}",
                 "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"error": str(e)}


def find_ranks(data, site):
    hits = []
    try:
        for it in data["tasks"][0]["result"][0]["items"]:
            if site in (it.get("url") or ""):
                hits.append({"rank": it.get("rank_absolute"),
                             "url": it.get("url"),
                             "title": (it.get("title") or "")[:80]})
    except Exception:
        pass
    return hits


def ga4_check():
    out = []
    for u in TARGETS:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as r:
                body = r.read().decode("utf-8", errors="replace")
            out.append({"url": u, "status": r.status,
                        "has_ga4": GA4 in body,
                        "has_gtag_js": "gtag/js" in body})
        except Exception as e:
            out.append({"url": u, "error": str(e)})
    return out


def indexed_count():
    d = serp(f"site:{SITE}", 2840, "en")
    try:
        res = d["tasks"][0]["result"][0]
        return {"items_count": res.get("items_count"),
                "se_results_count": res.get("se_results_count")}
    except Exception as e:
        return {"error": str(e)}


def llms_txt():
    try:
        req = urllib.request.Request(f"https://{SITE}/llms.txt",
                                     headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read().decode("utf-8", errors="replace")
        return {"status": r.status, "len": len(body)}
    except Exception as e:
        return {"error": str(e)}


def main():
    from datetime import date
    report = {"date": str(date.today()), "site": SITE,
              "ga4": ga4_check(),
              "llms_txt": llms_txt(),
              "indexed": indexed_count(),
              "ranks": []}
    kws = DEFAULT_KEYWORDS
    override = os.environ.get("GR_KEYWORDS")
    if override:
        kws = [(k.strip(), 2840, "en") for k in override.split(",") if k.strip()]
    for kw, loc, lang in kws:
        print(f"[serp] {kw}", file=sys.stderr)
        d = serp(kw, loc, lang)
        report["ranks"].append({"keyword": kw, "hits": find_ranks(d, SITE)})
        time.sleep(1)
    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
