# Reddit 防封策略 — Shadow Ban Prevention & Account Matrix

> **Load this when**: planning account setup, hitting shadow ban risk, designing the multi-account matrix, or recovering from a ban.

Reddit's punishment system is the most aggressive of any major social platform. Shadow ban (your posts are invisible to others while looking normal to you) effectively kills the account. This file is the survival playbook.

## Three Types of Bans

| Type | Severity | Symptom | Recovery |
|:---|:---|:---|:---|
| **Shadow Ban** (影子封禁) | 🔴 Highest | Account looks normal to you, but content only visible to yourself. All upvotes from other users disappear. | Appeal rate < 5%. **Prevent — do not recover.** |
| **Subreddit Ban** (子版块封禁) | 🟡 Medium | Banned from a specific community with notification + reason | Contact mods via modmail, sincere apology + commitment to rules. ~30% success. |
| **AutoMod Ban** (自动版主封禁) | 🟢 Low | Specific posts/comments removed automatically by rule | Adjust posting behavior, lower frequency, avoid trigger keywords |

## Why Reddit Bans You (the real reasons)

| Trigger | Severity | Prevention |
|:---|:---|:---|
| Posting within 24h of account creation | 🔴 | Wait 7+ days before any comment, 20+ days before any post |
| Negative total Karma | 🔴 | Lurk + upvote only until Karma reaches +10 |
| Multiple accounts from same IP | 🔴 | Use fingerprint browser (separate IP per account) |
| Reusing email from a previously banned account | 🔴 | Always fresh email (preferably ProtonMail) |
| CQS score = "low" or "lowest" | 🟡 | Avoid: aggressive posting, copied content, no profile fill |
| 5+ comments in same hour | 🟡 | Space comments 30+ minutes apart minimum |
| Identical content across multiple subs | 🟡 | Always rewrite — never copy-paste |

**CQS (Contributor Quality Score)** is Reddit's internal account-quality score. Subreddit mods can set rules like "block users with low CQS." You won't see your CQS, but you'll feel it (more auto-removals).

## The Multi-Account Matrix (mandatory for serious operations)

**Core principle**: Single account = single point of failure. Build 10 accounts, expect 50% loss rate, retain 5 working accounts.

### Account configuration

| Account type | Quantity | Purpose | Karma threshold |
|:---|:---|:---|:---|
| **Primary posting account** | 2–3 | Main brand posts, AMAs | ≥ 500 Karma |
| **Comment/engagement account** | 5–6 | Engage in target subs, build relationships | ≥ 100 Karma |
| **Backup account** | 2–3 | Emergency replacement for banned primaries | Keep dormant-active |

### Fingerprint browser requirements

Each account needs **completely independent**:
- IP address (residential proxy, geographic match)
- Cookies + LocalStorage
- User Agent + screen resolution + timezone
- Browser fingerprint (Canvas, WebGL, AudioContext signatures)

**Recommended tools**:
- **AdsPower** — most popular for English-region Reddit ops (~$5-10/mo per account)
- **比特浏览器 (BitBrowser)** — Chinese-language UI, similar features
- **Arc Browser** — light option for 1-2 accounts

**Do NOT**:
- ❌ Use a regular VPN (same fingerprint across accounts → instant cluster detection)
- ❌ Buy aged accounts from sketchy markets (IP / behavior history breaks trust)
- ❌ Use the same email provider's bulk-created emails (Gmail's `+alias` trick = detectable)

## The 20-Day Account Warming Protocol

Skip this and you're shadow banning. Period.

### Stage 1: Days 1–7 — Pure observation

| Daily action | Counter |
|:---|:---|
| Join 3–5 new subreddits | 0 posts, 0 comments |
| Browse content for 15+ minutes | Read top posts in target subs |
| Upvote 5–10 quality posts | Build voting history (Reddit tracks this) |
| Fill profile: avatar, banner, 1-line bio | One-time setup |

**Target Karma at end of Stage 1**: 0 (impossible to gain without commenting)

### Stage 2: Days 8–14 — Light comments only

| Daily action | Counter |
|:---|:---|
| 1 comment in `r/newtoreddit`, `r/AskReddit`, or other low-stakes sub | ≤ 1 per day |
| Continue 5–10 upvotes | — |
| Continue subreddit joining (slow, 1/day) | — |

**Comment rules**:
- 50+ characters minimum (single-word comments tank Comment Karma)
- No links of any kind
- Answer the question being asked, don't promote

**Target Karma at end of Stage 2**: +10 to +50

### Stage 3: Days 15–20 — Light posts in safe subs

| Daily action | Counter |
|:---|:---|
| 1 post in `r/cats`, `r/dogs`, `r/aww`, `r/foodporn` (high-engagement, low-stakes) | ≤ 1 per day |
| Continue commenting (now 2–3/day in target subs as observer, not promoter) | — |
| Continue upvoting | — |

**Target Karma at end of Stage 3**: +100 to +300

### Stage 4: Day 21+ — Unlock business activity

You've earned the "20-day streak" badge (visible in Reddit profile). You can now:
- Post in target business subreddits
- Comment in your industry subs at higher frequency
- Begin building thematic posting consistency

### Daily checklist during warming

```
☐ Join 1–2 new subreddits
☐ Upvote 5–10 pieces of content
☐ Browse target subs for ≥ 15 minutes
☐ Comment 1× (Stage 2+)
☐ Verify account status (no "server error" alerts, not removed from any sub)
```

## How to Detect Shadow Ban

You may be shadow banned and not know it. Signals:

1. **Server error pop-ups** during normal use → suspicious
2. **Visit your profile in an incognito browser** (or different account) → if it shows "page not found" or "suspended" → confirmed
3. **Post in `r/ShadowBan`** with text "test" → bot reply shows your status

If shadow banned:
- File appeal via Reddit Help Center
- Wait 4–6 weeks for response (low success rate)
- Move primary operations to a backup account immediately
- Lessons-learned: identify the trigger (posting frequency, content type, IP issue) — apply to remaining accounts

## Subreddit Ban Recovery

Far more recoverable than shadow ban. Steps:

1. Wait 48 hours (don't appeal in anger)
2. Send polite `modmail` to that subreddit's mod team:

```
Subject: Apology for [post title / behavior] and request for ban review

Hi mod team,

I want to acknowledge that my recent [post / comment] violated [specific rule]. 
I've re-read the community rules and understand the issue.

[1-2 sentences specific to your behavior — sincere, no excuses]

I'd like to continue participating in r/[sub] in compliance with the rules. 
Would you consider lifting the ban?

Thank you for the work you do moderating this community.

[Username]
```

3. If denied, accept it — don't argue, don't create alt accounts to evade. Mods talk.

## The Karma Floor

| Karma | What you can do |
|:---|:---|
| < 0 | High shadow-ban risk. Stop posting. Upvote/lurk only until positive. |
| 0–10 | Most subs auto-remove your posts. Lurk + comment in low-stakes subs only. |
| 10–100 | Can comment widely. Posts still risky. |
| 100–500 | Can post in most subs. r/SaaS / r/Entrepreneur accept you. |
| 500+ | Most subs accept you. Lower CQS-filter risk. |
| 1000+ | High-trust, can post in r/ProgrammerHumor, r/programming, etc. |

**Karma stat citations** (you can quote these): Most r/SaaS active members have 1,000+ Karma. r/MachineLearning effective contributors average 5,000+. Karma is the trust currency of Reddit.
