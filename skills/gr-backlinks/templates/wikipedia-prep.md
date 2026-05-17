# Wikipedia Article Preparation (AFFiNE — case study format)

> Use this template to build the **case file** before submitting to AfC.
> AFFiNE-specific values filled in; adapt for other subjects.

---

## Step 1: Notability Case (target 5+ deep independent sources)

| # | Source | Date | URL | Indepth (✅) or Passing (⚠️) | Key quote |
|---|---|---|---|---|---|
| 1 | [PUBLICATION] | YYYY-MM-DD | https://... | ✅ / ⚠️ | "[exact quote that demonstrates significance]" |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Rules**:
- "Indepth" = the article is **about AFFiNE** as a topic (not "AFFiNE was mentioned in a list of 10 tools")
- Press releases, sponsored content, company blog posts = **do not count**
- Same outlet covering AFFiNE multiple times counts as **1 source** not multiple

**Threshold for AfC submission**: at least 4 Indepth + 1 Passing = 5 total.

---

## Step 2: Draft Structure (Wikipedia article)

Use this exact structure (Wikipedia conventions):

```markdown
# AFFiNE

**AFFiNE** is an open-source, local-first knowledge management platform
created in [YEAR] by [FOUNDERS]. It combines documents, whiteboards,
and databases in a single workspace and supports collaborative editing
via [TECHNOLOGY]. As of [DATE], the project has surpassed 60,000 stars
on GitHub<ref>[CITATION 1]</ref>.

## History

[1-2 paragraphs on founding, milestones. Cite each fact.]

## Features

[1 paragraph + bulleted list of core features. Neutral tone.]

## Reception

[1-2 paragraphs on press coverage and community reception. Cite each.]

## Open source

[1 paragraph on license, contributor count, community size. Cite.]

## See also

* [Related Wikipedia articles, e.g. Notion (software), Roam Research]

## References

1. [Cite 1, formatted Wikipedia-style]
2. [Cite 2]
...

## External links

* Official website: https://affine.pro
* GitHub: https://github.com/toeverything/AFFiNE
```

**Word count target**: 600-1,500 words.

---

## Step 3: Wikidata Entity First

Before Wikipedia article submission, create a Wikidata entity:

1. Go to https://www.wikidata.org/wiki/Special:NewItem
2. Label: "AFFiNE"
3. Description: "Open-source local-first knowledge management software"
4. Add statements:
   - `instance of` (P31) → `free software` (Q341)
   - `developer` (P178) → `Toeverything` (or create org entity first)
   - `programming language` (P277) → TypeScript / Rust
   - `software version identifier` (P348) → current version
   - `license` (P275) → MPL-2.0 (or whatever the actual license is)
   - `source code repository URL` (P1324) → GitHub repo
   - `official website` (P856) → affine.pro
   - `inception` (P571) → founding date

Wikidata's notability bar is **much lower** than Wikipedia (any structured fact works). Once Wikidata entity exists, LLMs start using it for entity recognition.

---

## Step 4: Paid Editor Hire (if you go this route)

**DO** (safe path):
- Upwork search: "Wikipedia editor 1000+ edits 5+ years OSS technology"
- Verify: ask for their Wikipedia username → check edit history publicly
- Rate: $80-200/hr — pay hourly, NOT a flat fee
- **Require disclosure** per WP:PAID — they must add to their user page
- Expect: 4-8 hours for draft + revision

**DON'T** (banned path):
- Agencies offering "$2k for guaranteed Wikipedia article"
- Anyone refusing to disclose payment
- Fiverr gigs offering Wikipedia in 48 hours
- Anyone offering to "delete competitors' articles"

---

## Step 5: Submit via AfC (Articles for Creation)

URL: https://en.wikipedia.org/wiki/Wikipedia:Articles_for_creation

Submission checklist:
- [ ] Article is 600-1,500 words
- [ ] Every claim has a citation
- [ ] Citations are independent reliable sources (no press releases)
- [ ] Neutral point of view (no "leading platform" / "revolutionary")
- [ ] Wikidata entity exists
- [ ] Article uses Wikipedia template format (infobox software, references, external links)
- [ ] Paid editor (if any) has disclosed on their user page
- [ ] You have a Wikipedia account with **at least 10 edits** elsewhere (not a fresh account)

**Wait time**: 2-8 weeks for AfC reviewer to look at it.

---

## Step 6: After Approval

Once approved:
1. Monitor for vandalism (use Wikipedia watchlist)
2. Add minor improvements monthly (new milestones, references)
3. Track AI citation impact — LLMs typically reference within 6-12 weeks
4. Add `data/wikipedia-citation-watch.jsonl` entries when AI cites you

---

## Anti-patterns

- ❌ **Submitting before 5 deep sources** — wastes reviewer time + flags account
- ❌ **Marketing language** ("world-class", "revolutionary", "leading") — auto-rejected
- ❌ **Self-published sources** (your own blog, your own company page) — don't count
- ❌ **Press releases or sponsored content** — don't count
- ❌ **One-off mentions in listicles** — count as Passing not Indepth
- ❌ **Hiring an "agency" with 5-star Fiverr reviews** — these are sockpuppet farms
- ❌ **Multiple Wikipedia accounts** — instant permaban

---

## Realistic timeline

| Phase | Duration | Output |
|---|---|---|
| Build case file (Channel 2 PR work) | 8-16 weeks | 5+ deep independent sources |
| Wikidata entity | 1 hour | Live entity |
| Draft article | 6-12 hours | 1,200-word article ready |
| AfC submission + review | 2-8 weeks | Approved (or rejected → revise) |
| Approval → first AI citation | 6-12 weeks | LLMs cite Wikipedia entry |

**Total: 4-9 months from start to first AI citation impact.**

This is why Wikipedia is **LONG-LEAD**. Start now even if launch is months away.
