# HARO / Featured.com response template

Subject: Re: [exact query subject line — do not paraphrase]

---

[Credential lead-in from skills/gr-backlinks/haro-pitch-library.md — 1 sentence, ground in a specific number.]

[The substantive answer: 3-5 sentences. Be specific, contrarian, and quotable. Include one number or one named example. Avoid generic advice the journalist could write themselves.]

[Optional: one line of useful context the journalist can paraphrase but doesn't need to quote.]

---

**Yipei Wei (Iris)**
Founder, Gingiris — open-source growth advisory
ex-cofounder & COO, AFFiNE (60K GitHub stars)
https://gingiris.com
iris.wei@gingiris.com

---

## Pre-send checklist

- [ ] Word count 80-150 (HARO best-practice; quote rate drops above 200)
- [ ] At least one specific number in the body
- [ ] Credential lead-in matches the query category (cross-check pitch library)
- [ ] No links in the body (HARO strips most; journalist will visit signature link)
- [ ] Attribution block has full name, title, company, link
- [ ] Subject line preserved exactly from the source request

## After-send

Append one line to `gingiris-skills/data/backlinks.jsonl`:

```json
{"date":"YYYY-MM-DD","channel":"HARO","query":"<short title>","outlet":"<journalist publication>","credential_used":"<row name from pitch library>","response_word_count":N,"published":false,"url_if_published":""}
```

Flip `published` to true and fill `url_if_published` when the piece runs.
