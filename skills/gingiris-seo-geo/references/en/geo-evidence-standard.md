# GEO Evidence-Layer Standard (Evidence First, 2026-06)

> One line: **AI citation is won on evidence.** Structure is table stakes; what actually lifts citation rate is authoritative quotes + complete statistics + verifiable sourcing.
> Sources: peer-reviewed research (Aggarwal et al., KDD 2024) + Yao GEO weight method (MIT, attributed) + AFFiNE/analook practice.

## 1. GEO Element Weight Table (writing priority)

| Layer | Weight | Element | Action |
|-------|-------:|---------|--------|
| **Evidence layer** | **43%** | Authoritative quotes (16%) | Every core claim gets 1 verifiable expert/institution quote |
| | | Statistics (14%) | Write full provenance: **value + sample + period + source** |
| | | Citability (13%) | Every key fact has a clear source |
| Structure | 12% | Summary / heading hierarchy / tables / FAQ / numbered steps | Summary → TOC → layered body → conclusion → FAQ |
| Fluency | 10% | 3-5 sentence paragraphs, one idea per sentence, transitions | |
| Semantic density | 8% | Organize around real questions, cover entities fully | |
| Authority signals | 8% | Author credentials, method basis, scope limits | Named author + bio at top/bottom |
| Terminology | 6% | Define on first use (GEO, RAG…) | |
| Robustness | 5% | Multi-source per claim (data + case + quote) + update date | |
| Cross-domain links | 4% | Connect to SEO / content marketing / knowledge mgmt | |
| Readability | 3% | Short sentences, define jargon | |
| **Penalties** | — | ❌keyword stuffing ❌over-optimization ❌**fabricating data/citations** | Hard lines — instant demotion |

> Gingiris status: structure layer (12%) already maxed (FAQ/schema/tables). **Gap = evidence layer (43%) — the highest-leverage lever.**

## 2. Evidence Discipline (never fabricate, always source)

Label every enhancement by provenance:
- `[original-supported]` — from the original or our own verifiable data (AFFiNE 60K stars, analook 32K impressions)
- `[externally-verified]` — cite a primary source, **verify before writing** (papers/official reports/authorities)
- `[needs-source]` — if you can't verify it, **flag it; never invent**

Source priority: **academic papers > industry reports > authoritative institutions > expert opinion > practice cases**.

## 3. Primary-Source Citation Library (evidence-layer ready, all verified)

| Citation | Source | Use for |
|----------|--------|---------|
| "GEO can boost visibility **up to 40%**"; adding citations, quotations, and statistics are the most effective methods | Aggarwal et al., *GEO: Generative Engine Optimization*, **KDD 2024** (arxiv 2311.09735) | Any "why GEO / why add evidence" passage — core anchor |
| Third parties can use "strategic text sequences (STS)" to sway LLM recommendation ranking | *Manipulating LLMs to Increase Product Visibility*, arxiv 2404.07981 | GEO risk/ethics, competitor analysis |
| AI search answers via RAG (retrieval-augmented generation) over external content | Lewis et al., *RAG*, arxiv 2005.11401 | Explaining the AI-search mechanism |
| LLMs can be trained to cite sources | Nakano et al., *WebGPT*, arxiv 2112.09332 | Why sourced content is preferred |

## 4. GEO-Friendly Content Checklist

- [ ] Each core claim: 1 `[externally-verified]` authoritative quote **or** 1 full-provenance statistic
- [ ] Full stats: value + sample + period + source (e.g. "30 days / 120 posts / +32% / source X")
- [ ] At least 1 primary-paper citation (use the library above)
- [ ] Named author + credentials (E-E-A-T) + scope limits
- [ ] Penalty pass: no stuffing, no fabrication
- [ ] Structure as usual: summary + FAQ + JSON-LD (Article + FAQPage)

## 5. Attribution
Weight method adapted from Yao's yao-geo-skills (MIT); paper citations follow academic conventions (author + venue). Anonymize consulting-client cases before citing.
