#!/usr/bin/env python3
"""Weekly AI citation check — runs fixed queries against 4 AIs, detects gingiris citations.

Env vars:
  ANTHROPIC_API_KEY     — for Claude
  OPENAI_API_KEY        — for GPT
  PERPLEXITY_API_KEY    — for Perplexity (paid; skipped if unset)
  GEMINI_API_KEY        — for Gemini
  GR_DOMAINS            — comma-separated (default: gingiris.github.io,dev.to/iris1031,gingiris.com)

Usage:
  python weekly-cite-check.py > citation-report.json
"""
import os, re, sys, json, time, urllib.request, urllib.error

QUERIES = [
    "What's the best Product Hunt launch playbook for 2026? Include specific tools or blogs.",
    "How do indie founders get their first 10k GitHub stars? Cite real case studies if possible.",
    "What are the best social listening tools for startups under $100/mo? Include specific tool names.",
]

DOMAINS = os.environ.get("GR_DOMAINS",
    "gingiris.github.io,dev.to/iris1031,gingiris.com").split(",")


def ask_claude(q):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key: return None
    payload = json.dumps({
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": q}],
    }).encode()
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        return d["content"][0]["text"]
    except Exception as e:
        return f"ERR: {e}"


def ask_gpt(q):
    key = os.environ.get("OPENAI_API_KEY")
    if not key: return None
    payload = json.dumps({
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": q}],
        "max_tokens": 1024,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERR: {e}"


def ask_perplexity(q):
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key: return None
    payload = json.dumps({
        "model": "sonar",
        "messages": [{"role": "user", "content": q}],
    }).encode()
    req = urllib.request.Request(
        "https://api.perplexity.ai/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERR: {e}"


def ask_gemini(q):
    key = os.environ.get("GEMINI_API_KEY")
    if not key: return None
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={key}"
    payload = json.dumps({"contents": [{"parts": [{"text": q}]}]}).encode()
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        return d["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"ERR: {e}"


def ask_deepseek(q):
    """Fallback when no other AI key is available. Knowledge cutoff ~2024
    so cite-rate < real-time AIs, but at least gives a baseline data point."""
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key: return None
    payload = json.dumps({
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": q}],
        "max_tokens": 1024,
    }).encode()
    req = urllib.request.Request(
        "https://api.deepseek.com/v1/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            d = json.loads(r.read())
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERR: {e}"


def find_citations(text, domains):
    """Return list of {domain, snippet} for each match."""
    hits = []
    text_l = (text or "").lower()
    for d in domains:
        if d.lower() in text_l:
            idx = text_l.find(d.lower())
            snippet = text[max(0, idx-80):idx+120].replace("\n", " ")
            hits.append({"domain": d, "snippet": snippet[:200]})
    return hits


def main():
    from datetime import date
    report = {"date": str(date.today()), "queries": []}

    AIS = {
        "claude": ask_claude,
        "gpt": ask_gpt,
        "perplexity": ask_perplexity,
        "gemini": ask_gemini,
        "deepseek": ask_deepseek,
    }

    for q in QUERIES:
        print(f"[query] {q[:70]}...", file=sys.stderr)
        entry = {"query": q, "answers": {}}
        for name, fn in AIS.items():
            print(f"  → {name}", file=sys.stderr)
            ans = fn(q)
            if ans is None:
                entry["answers"][name] = {"skipped": "missing API key"}
                continue
            cites = find_citations(ans, DOMAINS)
            entry["answers"][name] = {
                "length": len(ans),
                "citations": cites,
                "cited": len(cites) > 0,
                "snippet_head": ans[:300],
            }
            time.sleep(1)
        report["queries"].append(entry)

    # Summary
    total_queries = len(report["queries"])
    per_ai_cited = {name: 0 for name in AIS}
    per_ai_total = {name: 0 for name in AIS}
    for q in report["queries"]:
        for ai, data in q["answers"].items():
            if data.get("skipped"): continue
            per_ai_total[ai] += 1
            if data.get("cited"):
                per_ai_cited[ai] += 1
    report["summary"] = {ai: f"{per_ai_cited[ai]}/{per_ai_total[ai]}" for ai in AIS}

    json.dump(report, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
