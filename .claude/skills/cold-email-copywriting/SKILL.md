---
name: cold-email-copywriting
description: >-
  Writes and reviews cold email copy — no fluff, hook-bridge-CTA structure,
  mobile-optimized length, curiosity-driven tone, low-friction CTAs. Use when
  drafting, editing, or critiquing cold emails, outbound messaging, sales
  emails, or prospecting copy.
---

> Built for **Claude Code** (and compatible agent harnesses). Drop into `.claude/skills/`.

# Cold Email Copywriting

Cold email copy must be **relevant**, not relational. The prospect is a stranger — they do not care about small talk, shared alumni networks, or geographic coincidence. Value must be obvious in seconds.

## Core Principle: The Stain Remover Pen

Imagine standing next to someone in an elevator who has a food stain on their white shirt they cannot see. You have a stain remover pen. You say:

> "I noticed a stain on your shirt. I have a stain remover pen that'll take it out right now — want to try it?"

They immediately understand the pain, the fix, and the low effort to accept. No rapport required. **Cold email works the same way** — spot a real problem, offer a clear fix, make saying yes effortless.

## What Never to Write

Reject and rewrite copy that includes:

- "I hope this email finds you well"
- "I love what you're doing at [company]"
- "Your profile is amazing"
- "I noticed we both went to [university]"
- "I'll be in your area next week"
- Generic compliments with no tied value
- Long paragraphs or essay-style pitches
- Obvious sales pressure — if they feel sold to, defenses go up

## Merge Tags (Variables)

Merge tag syntax is **tool-specific**. Wrong casing means tags will not render and prospects see literal `{{firstName}}` in the inbox.

**Default: camelCase** — matches Instantly and most modern sequencers:

| Field | Tag |
|-------|-----|
| First name | `{{firstName}}` |
| Last name | `{{lastName}}` |
| Company | `{{companyName}}` |
| Sender first name | `{{senderFirstName}}` |

**Before drafting or reviewing copy**, confirm which sequencer or ESP the user sends from (e.g. Instantly, Smartlead, Lemlist, Outreach). Use that tool's exact tag names and casing. If unknown, default to camelCase and flag for the user to verify against their platform docs.

**Never use snake_case** (e.g. `{{first_name}}`) unless the user's tool explicitly requires it.

## Email Structure

Every cold email follows four parts. Keep the full message **short and mobile-optimized** — readable on a phone without scrolling.

### 1. Greeting

Simple and human:

```
Hi {{firstName}},
```

### 2. Hook (opening sentence)

One sentence. Extremely relevant to **their** situation. Catches attention because it reflects something true about their world — role, pain, trigger event, industry constraint.

The hook buys time to keep reading.

### 3. Bridge (body)

Connect the hook to the value proposition. This is not filler — it leads logically into what you offer and why they should believe you.

The bridge typically includes:

- Brief articulation of the problem or opportunity (1–2 sentences max)
- **Proof** — a case study, outcome, or credible reference (specific but honest; use user-provided facts only)
- Why this is insightful or beneficial **to them**, not why your product is great

Goal: **pique curiosity** — they should want to know more without feeling pitched.

### 4. Call to Action (CTA)

**Low friction.** This person does not know you. Do not default to asking for a meeting unless urgency is obvious and the offer is an obvious must-have.

Prefer CTAs they can answer with "Sure" or "Yes, please":

- "If I could send you a quick video showing what that looks like for [their context], would that be useful?"
- "If I could put together a short example of how [outcome] would work for [company], would you be open to me sharing it?"
- "Would it be helpful if I sent over [specific asset] — no call needed?"
- "Mind if I send that over?"

Patterns that work:

- "If I could provide you [X], would that be valuable?"
- "Would you be open to me sharing [personalized thing]?"
- "Do you mind if I send that right over?"

Always give an **easy out** — permission-based, "by the way" energy, not a calendar demand.

### Meeting asks

Only when the prospect would immediately recognize urgent need. Otherwise earn the meeting through a low-friction first step.

## Tone and Length

| Rule | Guidance |
|------|----------|
| Length | Aim for 50–125 words total |
| Sentences | Short. One idea per sentence. |
| Jargon | Only what the ICP uses naturally |
| Curiosity | Lead with insight, not inventory |
| Honesty | No fabricated stats or fake case studies |

## Agent Workflow

1. Confirm sequencer/ESP and use correct merge tag casing (default: camelCase — `{{firstName}}` for Instantly).
2. Gather from user: ICP, pain point, offer, proof (real case study/outcomes), desired next step.
3. Draft using Hook → Bridge → CTA structure.
4. Run the **Copy QA** checklist below.
5. Present 1–2 variants if useful (different hooks or CTAs).
6. Confirm deliverability skill constraints — no links in v1 unless user opts in.

## Copy QA Checklist

```
- [ ] Merge tags use correct casing for user's sequencer (default: camelCase / {{firstName}})
- [ ] No small talk or empty flattery
- [ ] Hook is specific to recipient context (role, company, industry, trigger)
- [ ] Bridge connects hook to value without a pitch dump
- [ ] Includes proof or credibility (user-supplied, not invented)
- [ ] CTA is low friction — easy to reply "yes"
- [ ] Under ~125 words; mobile-scannable
- [ ] Curiosity-driven, not salesy
- [ ] No links/images (unless deliverability opt-in)
- [ ] Reads naturally aloud — not template-stiff
```

## Template (fill from user context)

```
Hi {{firstName}},

{{hook — one sentence, their situation}}

{{bridge — problem/opportunity + brief proof}}

{{low-friction CTA — permission-based}}

{{sign-off}}
{{senderFirstName}}
```

## Anti-Patterns

| Bad | Why | Better |
|-----|-----|--------|
| "We help companies scale revenue" | Generic, no hook | "[Specific pain] at [company type] usually means [concrete issue]…" |
| "Do you have 15 minutes Tuesday?" | High friction for a stranger | "Mind if I send a 2-min walkthrough?" |
| 4 paragraphs of product features | Novel, self-centered | One outcome + one proof point |
| "Just checking in" follow-up | No new value | New insight, asset, or angle |

## Examples

See [examples.md](examples.md) for full before/after samples.

## Relationship to Deliverability

Default copy assumes **plain text, no links**. If the CTA references a video or asset, the send pattern is: **offer in email → send asset after positive reply** — not a link in email 1.

When reviewing copy, cross-check [cold-email-deliverability](../cold-email-deliverability/SKILL.md) constraints.

## Knowledge files (read when relevant)

| File | Use when |
|------|----------|
| [knowledge/banned-phrases.md](knowledge/banned-phrases.md) | Reviewing or rewriting copy for spam/AI-slop patterns |
| [knowledge/conditional-question.md](knowledge/conditional-question.md) | Choosing or rewriting the first-touch CTA |
| [examples.md](examples.md) | Before/after examples |

Default CTA for cold first-touch: **Conditional Question** (not a 15-minute meeting ask).

