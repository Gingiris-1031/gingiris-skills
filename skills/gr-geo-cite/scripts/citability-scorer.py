#!/usr/bin/env python3
# Adapted from zubair-trabzada/geo-seo-claude (https://github.com/zubair-trabzada/geo-seo-claude)
# Original license: MIT (preserved in repo LICENSE file)
# Pulled into gingiris-skills @ 2026-05-07 for gr-geo-cite citability scoring.
# Adaptations: stdlib-only (no requests/bs4), JSON envelope output to match gr-seo-patrol style.

"""
Citability Scorer — Analyzes content blocks for AI citation readiness.

Each passage scored on 5 dimensions:
- Answer Block Quality (30%): definition patterns, answer position, question-headings
- Self-Containment (25%): 134-167 word optimal range, low pronoun density, 3+ proper nouns
- Structural Readability (20%): sentence length 10-20 words, lists, paragraph breaks
- Statistical Density (15%): percentages, dollar amounts, numbers with units, year refs
- Uniqueness Signals (10%): original-research language, case studies, specific products

Page score = avg of top 5 passage scores.

Usage:
    python3 citability-scorer.py URL
    python3 citability-scorer.py --file page.html

Dependencies: Python stdlib only.
"""

import argparse, json, re, sys, urllib.request
from html.parser import HTMLParser
from typing import Optional


def score_passage(text: str, heading: Optional[str] = None) -> dict:
    """Score a single passage for AI citability (0-100)."""
    words = text.split()
    word_count = len(words)

    scores = {
        "answer_block_quality": 0,
        "self_containment": 0,
        "structural_readability": 0,
        "statistical_density": 0,
        "uniqueness_signals": 0,
    }

    # === 1. Answer Block Quality (30%) ===
    abq_score = 0

    # Check for definition patterns ("X is...", "X refers to...", "X means...")
    definition_patterns = [
        r"\b\w+\s+is\s+(?:a|an|the)\s",
        r"\b\w+\s+refers?\s+to\s",
        r"\b\w+\s+means?\s",
        r"\b\w+\s+(?:can be |are )?defined\s+as\s",
        r"\bin\s+(?:simple|other)\s+(?:terms|words)\s*,",
    ]
    for pattern in definition_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            abq_score += 15
            break

    # Check if answer appears early (first 60 words)
    first_60_words = " ".join(words[:60])
    if any(
        re.search(p, first_60_words, re.IGNORECASE)
        for p in [
            r"\b(?:is|are|was|were|means?|refers?)\b",
            r"\d+%",
            r"\$[\d,]+",
            r"\d+\s+(?:million|billion|thousand)",
        ]
    ):
        abq_score += 15

    # Question-based heading bonus
    if heading and heading.endswith("?"):
        abq_score += 10

    # Clear, direct sentence structure
    sentences = re.split(r"[.!?]+", text)
    short_clear_sentences = sum(
        1 for s in sentences if 5 <= len(s.split()) <= 25
    )
    if sentences:
        clarity_ratio = short_clear_sentences / len(sentences)
        abq_score += int(clarity_ratio * 10)

    # Has specific, quotable claim
    if re.search(
        r"(?:according to|research shows|studies? (?:show|indicate|suggest|found)|data (?:shows|indicates|suggests))",
        text,
        re.IGNORECASE,
    ):
        abq_score += 10

    scores["answer_block_quality"] = min(abq_score, 30)

    # === 2. Self-Containment (25%) ===
    sc_score = 0

    # Optimal word count (134-167 words)
    if 134 <= word_count <= 167:
        sc_score += 10
    elif 100 <= word_count <= 200:
        sc_score += 7
    elif 80 <= word_count <= 250:
        sc_score += 4
    elif word_count < 30 or word_count > 400:
        sc_score += 0
    else:
        sc_score += 2

    # Low pronoun density (fewer pronouns = more self-contained)
    pronoun_count = len(
        re.findall(
            r"\b(?:it|they|them|their|this|that|these|those|he|she|his|her)\b",
            text,
            re.IGNORECASE,
        )
    )
    if word_count > 0:
        pronoun_ratio = pronoun_count / word_count
        if pronoun_ratio < 0.02:
            sc_score += 8
        elif pronoun_ratio < 0.04:
            sc_score += 5
        elif pronoun_ratio < 0.06:
            sc_score += 3

    # Contains named entities (proper nouns, brands, specific terms)
    proper_nouns = len(re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text))
    if proper_nouns >= 3:
        sc_score += 7
    elif proper_nouns >= 1:
        sc_score += 4

    scores["self_containment"] = min(sc_score, 25)

    # === 3. Structural Readability (20%) ===
    sr_score = 0

    # Sentence count and length distribution
    if sentences:
        avg_sentence_length = word_count / len(sentences)
        if 10 <= avg_sentence_length <= 20:
            sr_score += 8
        elif 8 <= avg_sentence_length <= 25:
            sr_score += 5
        else:
            sr_score += 2

    # Contains list-like structures
    if re.search(r"(?:first|second|third|finally|additionally|moreover|furthermore)", text, re.IGNORECASE):
        sr_score += 4

    # Contains numbered items or bullet-like content
    if re.search(r"(?:\d+[\.\)]\s|\b(?:step|tip|point)\s+\d+)", text, re.IGNORECASE):
        sr_score += 4

    # Paragraph breaks (indicates structure)
    if "\n" in text:
        sr_score += 4

    scores["structural_readability"] = min(sr_score, 20)

    # === 4. Statistical Density (15%) ===
    sd_score = 0

    # Percentages
    pct_count = len(re.findall(r"\d+(?:\.\d+)?%", text))
    sd_score += min(pct_count * 3, 6)

    # Dollar amounts
    dollar_count = len(re.findall(r"\$[\d,]+(?:\.\d+)?(?:\s*(?:million|billion|M|B|K))?", text))
    sd_score += min(dollar_count * 3, 5)

    # Other numbers with context
    number_count = len(re.findall(r"\b\d+(?:,\d{3})*(?:\.\d+)?\s+(?:users|customers|pages|sites|companies|businesses|people|percent|times|x\b)", text, re.IGNORECASE))
    sd_score += min(number_count * 2, 4)

    # Year references (indicates timeliness)
    year_count = len(re.findall(r"\b20(?:2[3-6]|1\d)\b", text))
    if year_count > 0:
        sd_score += 2

    # Named sources
    source_patterns = [
        r"(?:according to|per|from|by)\s+[A-Z]",
        r"(?:Gartner|Forrester|McKinsey|Harvard|Stanford|MIT|Google|Microsoft|OpenAI|Anthropic)",
        r"\([A-Z][a-z]+(?:\s+\d{4})?\)",
    ]
    for pattern in source_patterns:
        if re.search(pattern, text):
            sd_score += 2

    scores["statistical_density"] = min(sd_score, 15)

    # === 5. Uniqueness Signals (10%) ===
    us_score = 0

    # Original data indicators
    if re.search(
        r"(?:our (?:research|study|data|analysis|survey|findings)|we (?:found|discovered|analyzed|surveyed|measured))",
        text,
        re.IGNORECASE,
    ):
        us_score += 5

    # Case study or example indicators
    if re.search(
        r"(?:case study|for example|for instance|in practice|real-world|hands-on)",
        text,
        re.IGNORECASE,
    ):
        us_score += 3

    # Specific tool/product mentions (shows practical experience)
    if re.search(r"(?:using|with|via|through)\s+[A-Z][a-z]+", text):
        us_score += 2

    scores["uniqueness_signals"] = min(us_score, 10)

    # === Calculate total ===
    total = sum(scores.values())

    # Determine grade
    if total >= 80:
        grade = "A"
        label = "Highly Citable"
    elif total >= 65:
        grade = "B"
        label = "Good Citability"
    elif total >= 50:
        grade = "C"
        label = "Moderate Citability"
    elif total >= 35:
        grade = "D"
        label = "Low Citability"
    else:
        grade = "F"
        label = "Poor Citability"

    return {
        "heading": heading,
        "word_count": word_count,
        "total_score": total,
        "grade": grade,
        "label": label,
        "breakdown": scores,
        "preview": " ".join(words[:30]) + ("..." if word_count > 30 else ""),
    }




class PassageExtractor(HTMLParser):
    """Extract substantive content blocks bounded by heading tags. Stdlib HTML parser."""

    SKIP_TAGS = {"script", "style", "nav", "header", "footer", "aside", "form"}
    HEADING_TAGS = {"h1", "h2", "h3"}

    def __init__(self):
        super().__init__()
        self.passages = []
        self.current_heading = None
        self.current_text_parts = []
        self.in_heading = False
        self.skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
        if tag in self.HEADING_TAGS:
            if self.current_heading is not None and self.current_text_parts:
                text = " ".join(self.current_text_parts).strip()
                if text:
                    self.passages.append({"heading": self.current_heading.strip(),
                                          "text": text})
            self.current_text_parts = []
            self.in_heading = True
            self.current_heading = ""

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS and self.skip_depth > 0:
            self.skip_depth -= 1
        if tag in self.HEADING_TAGS:
            self.in_heading = False

    def handle_data(self, data):
        if self.skip_depth > 0:
            return
        if self.in_heading:
            self.current_heading += data
        else:
            stripped = data.strip()
            if stripped:
                self.current_text_parts.append(stripped)

    def get_passages(self):
        if self.current_heading is not None and self.current_text_parts:
            text = " ".join(self.current_text_parts).strip()
            if text:
                self.passages.append({"heading": self.current_heading.strip(),
                                      "text": text})
        return self.passages


def fetch_html(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": "gr-geo-cite/citability-scorer/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")


def score_page(html_content: str) -> dict:
    """Extract passages from HTML and score each, return page summary."""
    parser = PassageExtractor()
    parser.feed(html_content)
    passages = parser.get_passages()
    passages = [p for p in passages if len(p["text"].split()) >= 30]

    scored = [score_passage(p["text"], heading=p.get("heading")) for p in passages]

    if not scored:
        return {
            "status": "warn",
            "page_citability_score": 0,
            "rating": "No substantive passages found (all blocks <30 words).",
            "passages_count": 0,
            "top_5_passages": [],
        }

    scored_sorted = sorted(scored, key=lambda x: -x["total_score"])
    top = scored_sorted[: max(1, min(5, len(scored)))]
    page_score = round(sum(p["total_score"] for p in top) / len(top), 1)

    if page_score >= 70:
        status, rating = "pass", "Highly citable — AI likely to cite passages"
    elif page_score >= 50:
        status, rating = "warn", "Moderately citable — some passages strong, others thin"
    elif page_score >= 35:
        status, rating = "warn", "Low citability — most passages too context-dependent"
    else:
        status, rating = "fail", "Poor citability — passages thin and unstructured"

    return {
        "status": status,
        "page_citability_score": page_score,
        "rating": rating,
        "passages_count": len(scored),
        "top_5_passages": top,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("url", nargs="?", help="URL to fetch")
    p.add_argument("--file", help="Read HTML from local file instead of URL")
    p.add_argument("--timeout", type=int, default=20)
    args = p.parse_args()

    if args.file:
        with open(args.file) as f:
            html = f.read()
        source = f"file:{args.file}"
    elif args.url:
        html = fetch_html(args.url, args.timeout)
        source = args.url
    else:
        print("ERROR: provide URL or --file", file=sys.stderr); sys.exit(1)

    result = score_page(html)
    result["source"] = source
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2, default=str)
    print()


if __name__ == "__main__":
    main()
