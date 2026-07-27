# Team Motivation Ops — Standup + Weekly Meeting + 1:1 System for AI Startup COO

> 🌍 **Language / 语言**: [中文](../../SKILL.md) | [English](README.md) | [日本語](../ja/README.md) | [한국어](../ko/README.md)

> **Core principle**: Freedom and accountability are two sides of the same coin. Standups help people think clearly. Weekly meetings create alignment. 1:1s make people feel seen. When all three work, motivation isn't managed into existence — it grows on its own.

**Best for**: COOs and tech leads at AI startups, teams of 3–30, high-autonomy or remote/hybrid setups.

---

## Layer 1: Daily Standup — Information Layer

### Design Philosophy

A standup isn't a status report. It's a ritual that forces clarity. If you can write it out, you've thought it through. If you can't, you probably haven't figured out what you're actually doing today.

Vagueness is contagious — the COO's standup sets the tone. Write yours first, and write it well.

### Standard Format (3 required fields)

1. **What I did today**: Concrete deliverables. "Continued development" doesn't count.
2. **What I'll do tomorrow**: Specific enough that someone else can tell whether you did it.
3. **Blockers / topics to discuss**: Stuck points, unclear ownership, anything worth a sync.

### Sample Good Standup

```
What I did today
- Finished the XX API endpoint, tested with 50 local records, avg 80ms — 2x faster than the previous version
- Helped a teammate debug a WhatsApp conversation list render lag — root cause was no virtual scrolling. Pointed them to react-window, they fixed it in 10 minutes
- Honest truth: I zoned out for an hour in the afternoon. Used the time to archive a competitor's new case study into our competitive intel folder. Partial credit.

What I'll do tomorrow
- Push the bulk quote API to staging and run it against real data
- Write the interface docs I skipped today

Blockers / Sync topics
- The XXX architecture decision is still unresolved and it's blocking my side. Want to align on it tonight.
```

### COO Principles

- Don't demand perfection — demand honesty. If someone slacked off, fine, just own it and document what they did accomplish.
- Don't criticize short standups — ask "what specifically did you deliver today?" The issue is specificity, not length.
- Publicly praise one great standup. Never shame a bad one. Specificity is contagious too.
- Repeat this framing: a good standup is a gift to your teammates.

---

## Layer 2: Weekly Meeting — Alignment Layer

### Design Philosophy

A weekly meeting isn't a progress report. It solves the "presence problem" — making sure everyone knows where the company stands, and hears each other commit publicly to something. Neither of those can be done async.

### Agenda Structure (25 minutes, hard stop)

| Segment | Time | Content |
|---------|------|---------|
| Company update | 8 min | Current progress / next week's plan / decisions the team needs to make |
| Individual round | ~3 min/person | Did you hit last week's commitments? / 1–3 specific commitments for this week / what do you need from the team? / current state: 0–10 |
| Group discussion | Remaining | Open discussion after individual round; anything that needs 1:1 follow-up gets moved offline |

**Never skip the "current state: 0–10" check.** It's the only channel that lets someone say "I'm struggling" without having to explain it on the spot. Follow up on low scores — but privately, in a 1:1, not in front of the group.

### Scrum Master Rotation

Rotate the facilitator role weekly. Their job: keep the speaking order and the clock. Rotation reduces COO-dependency and gives everyone ownership over the meeting's flow.

### COO Principles

- Individual commitments must be specific enough that others can judge completion. COO models this standard first.
- 25 minutes is a hard constraint. Overruns mean problems weren't triaged in advance, not that people talked too much.
- Fix overruns by maintaining a "decisions needed" list before the meeting. Route the rest to 1:1s or async.

---

## Layer 3: 1:1 Meeting — Individual Layer

### Design Philosophy

The 1:1 is the highest-information, hardest-to-run part of this system. It's not a top-down communication channel. It's a window for the COO to understand exactly where each person is stuck and why.

**"Stuck-at" diagnostic framework**: information gap / authority gap / collaboration friction / capability ceiling / unclear direction. Each requires a completely different fix. Confusing them wastes everyone's time.

### Part 1: Quantified Pulse Check (5 minutes)

Rate each dimension 1–5 (1 = bad / 3 = acceptable / 5 = great):

| Dimension | Notes |
|-----------|-------|
| Energy (mental/physical state) | |
| Goal clarity | Do they know their top 1–2 priorities and what success looks like? |
| Mission alignment | Connection between their work and the company's direction |
| Autonomy vs. support | Is their decision-making space matched with the support they need? |
| Sense of growth | |
| Pace sustainability | Could they keep this up for another month? |
| Flow time | Quality and quantity of deep work |
| Technical growth | |
| Tooling & dev experience | |

> Precision isn't the point — trends are. Three consecutive weeks of "pace sustainability: 2" is more alarming than one week of "1." Keep historical records. Open each 1:1 by reviewing last session's scores.

### Part 2: Deep Question Bank (15–20 minutes, pick 3–4)

**About the work itself**
- What's been most satisfying in the past two weeks? Why?
- What's been your biggest blocker? Where exactly are you stuck — info gap, authority, collaboration, capability, or direction?
- Is how you're spending your time aligned with what you think is highest leverage? Where's the gap?
- If you could eliminate one task next week, what would it be? Why haven't you?

**About decisions and ownership**
- Is there anything you could have decided yourself but came to me for anyway? Why?
- Is there anything that obviously needs to happen but nobody's doing?
- Flip side: did you make a call you probably should have aligned on first?

**About honesty** (hardest to ask, most valuable)
- Is there anything you've been meaning to say but haven't?
- Is there a problem quietly developing in the team that nobody's talking about yet?
- What decision have I made recently that you didn't understand or agree with?

**About growth**
- What's one skill you've clearly improved this month? How would you prove it?
- What's the one thing you'd most like to deliberately practice in the next 90 days? What would you need?
- What part of your current toolchain / codebase / LLM workflow is dragging you down the most?

**About people and org**
- Who on the team do you most enjoy working with or learning from? Who's hardest to collaborate with? Why?
- If you were CEO, what's the first thing you'd change tomorrow?

### Part 3: Bilateral Feedback (5–10 minutes)

Don't skip the "them → you" direction. The quality of feedback you receive determines the speed at which you can improve.

| Direction | Questions |
|-----------|-----------|
| Them → you | What am I doing that's most helpful (keep doing)? / What am I doing that makes your life harder (stop doing)? / What should I start doing? |
| You → them | What they're doing well / What they need to adjust / One specific expectation for the coming week |

### COO Principles

- The pulse scores are keys, not grades. A "2" is a prompt to ask why, not a performance metric.
- Model candor first — share a decision you've been second-guessed on. That's what makes it safe for others to tell the truth.
- Every 1:1 must end with at least one action item. No-action 1:1s feel like just venting.

---

## Common Failure Modes & Fixes

**Nobody's writing real standups?**
Check your own first. Is it specific enough? Vagueness and specificity are both contagious. Praise one good example publicly. Don't shame bad ones.

**Weekly meeting turned into a status report?**
Replace "what did you do this week" with "did you hit what you committed to last week?" Yes/no creates more accountability — and takes less time.

**1:1 always gets "I'm fine"?**
Ask yourself whether you've ever given people real evidence that honesty won't be punished. That takes a few concrete instances to build — it doesn't come from asking better questions.

**Team grew, can't do 1:1s with everyone?**
Bi-weekly is fine. Teach the pulse check to tech leads and line managers. Reserve the COO-level 1:1 for escalations when scores turn red.

---

## Output Format Guide

When a user asks about a specific situation, lead with:
1. **Diagnosis**: Which layer is the problem at? (Information / Alignment / Individual)
2. **One action they can take today**: Concrete, specific, doable now
3. **One guardrail**: What the COO needs to do first to prevent it from bouncing back

Skip "I recommend improving communication." Go straight to "move this from the weekly meeting to a 1:1, because what it actually needs is..."
