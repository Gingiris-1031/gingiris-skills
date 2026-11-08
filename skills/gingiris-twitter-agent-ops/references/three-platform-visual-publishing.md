# Three-Platform Visual Publishing Reference

Use this reference when publishing one English evidence card to X, LinkedIn and Threads through Buffer.

## Daily order

1. Read `MASTER-STATUS.md` and the current Buffer states.
2. Lock each Asia/Shanghai platform-day if any `scheduled`, `sending`, `sent` or `error` item exists.
3. Select an unused, source-linked evidence card.
4. Write platform-native copy:
   - X: concise and within the verified publisher limit;
   - LinkedIn: detailed context, evidence, reasoning, limits and action;
   - Threads: normally no more than 500 characters.
5. Generate one 4:5 visual that can be shared across all three platforms.
6. For Skill posts, include the Skill name and exact install command in the image and keep the command copyable in each root post.
7. Check image text, privacy, cropping and consistency with the evidence card.
8. Public image hosting is an external disclosure: upload only if the existing user authorization covers the reviewed image and chosen host; otherwise keep the image local. Then verify HTTP 200 and an image MIME type.
9. Dry-run the Buffer publisher. Require explicit authorisation before the write.
10. Create each post with `assets: [{ image: { url } }]`.
11. Read each Buffer ID back. Only `sent` plus the intended attachment MIME type and a real `externalLink` counts as complete.
12. Update `MASTER-STATUS.md` within five minutes and schedule 10–15m, 2h, 24h and 7d checks.

## Editorial evidence and adaptation gate

Before drafting, create or read a source packet containing the original excerpt, surrounding context, claim owner, time scope, privacy status, verification status and transformation note. Meeting summaries and indexes may identify material, but do not replace raw evidence when it exists.

Maintain a rolling mix across four pillars: Iris's identity and judgment, anonymised consulting field notes, open-source/global GTM, and Tools & Skills. A post does not need a Skill CTA unless that Skill is the reader's natural next step.

Run two different reviews:

- Content review: provenance, ownership, privacy, attribution, natural English, platform-native structure and one contextual CTA.
- Publication review: channel health, day lock, exact text and CTA, media URL/MIME, final rendering, `sent/error` state and public link.

Do not require fixed quantities of time/place details, numbers, parenthetical asides, em dashes or tables. These are optional writing tools. Never invent details to satisfy a voice pattern.

Buffer cannot be assumed to create a first comment. Keep any promised URL or install command in the root post. Do not reuse WeChat-specific formatting, embeds or publishing code.

Treat historical figures, third-party cases and platform-performance rules as unverified until the original source, date and attribution are checked. An internal content index is a discovery tool, not an automatic publication source.

Keep a failure ledger with: platform, symptom, root cause, immediate fix, prevention and evidence. Do not interpret authentication or delivery errors as content-performance data.

## Hosting rules

- A local file path is never a Buffer media URL.
- Do not use an authenticated Drive link, an expiring signed URL or a redirect that ends in 404.
- When a website deployment is delayed, a permanent public repository raw URL can be used only after a live HTTP and MIME check.
- Add media through a clean temporary clone or worktree when the user's main checkout contains unrelated edits.

## Failure rules

- `sending` means wait and read again; it does not authorise a duplicate.
- `error` is a day lock. Record it and do not auto-retry or reschedule.
- If only some platforms succeed, stop and report per-platform state.
- Missing metrics remain unavailable; never infer follower growth from impressions.
- Keep at most three future scheduled posts per platform and revise only unpublished items using verified 24h/7d evidence.
