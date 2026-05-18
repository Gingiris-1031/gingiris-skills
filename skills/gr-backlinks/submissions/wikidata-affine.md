# Wikidata Entity Draft: AFFiNE

> Submit at: https://www.wikidata.org/wiki/Special:NewItem
> Time: ~10 min. Lower notability bar than Wikipedia. Powers LLM entity recognition.

## Step 1: Create entity
- Label (English): `AFFiNE`
- Label (Chinese): `AFFiNE`
- Label (Japanese): `AFFiNE`
- Description (English): `Open-source local-first knowledge management software`
- Description (Chinese): `开源本地优先的知识管理软件`
- Description (Japanese): `オープンソースのローカルファースト知識管理ソフトウェア`

## Step 2: Add these statements (in order)

### Core identifiers
| Property | Value |
|---|---|
| instance of (P31) | free software (Q341) |
| instance of (P31) | open-source software (Q1130645) |
| instance of (P31) | knowledge management software (Q1373146) |

### Technical
| Property | Value |
|---|---|
| programming language (P277) | TypeScript (Q978185) |
| programming language (P277) | Rust (Q575650) |
| license (P275) | Mozilla Public License 2.0 (Q334062) |
| operating system (P306) | Windows, macOS, Linux, iOS, Android |
| platform (P400) | desktop, web, mobile |

### Identifiers / URLs
| Property | Value |
|---|---|
| official website (P856) | https://affine.pro |
| source code repository URL (P1324) | https://github.com/toeverything/AFFiNE |
| Twitter username (P2002) | AffineOfficial |

### Time
| Property | Value |
|---|---|
| inception (P571) | 2022 (verify exact date from first commit / first release) |

### People
| Property | Value |
|---|---|
| developer (P178) | Toeverything (create separate entity if needed) |
| founded by (P112) | [list co-founders] |

## Step 3: Reference each statement
Wikidata wants 1+ reference per claim. Use:
- GitHub repo URL → "source code" + "inception" + "license"
- Official site → "official website" + identifiers
- Press articles → for popularity claims like "github stars"

## Notability check (Wikidata bar — much lower than Wikipedia)
- ✅ Has GitHub repo (public)
- ✅ Has official website
- ✅ Documented at archive.org / external sources
- ✅ Mentioned in 2+ secondary sources

**You only need ONE secondary mention** for Wikidata. AFFiNE is way above this bar.

---

## After submission
- Wait 1-7 days for entity ID assignment (e.g. Q123456789)
- LLMs (ChatGPT, Claude, Perplexity, Gemini) typically index Wikidata entities within 30-60 days
- Track AI citation impact via `gr-geo-cite` weekly check

