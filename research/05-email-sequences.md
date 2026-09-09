# 05 — Email Sequences (ready to load)

## Rules these are written against

1. **The CTA is a reply, never a link.** No link in email 1 or 2 of any sequence. Links depress
   deliverability and shift the ask to the worst-converting step in the funnel.
2. **The ask is a gift.** Every first email offers to *give* them 20+ trigger-matched prospects in
   their city. You are not pitching. That distinction is the strategy.
3. **Under 90 words.** Read on a phone, in a truck, between jobs.
4. **One idea per email.**
5. **No merge-tag theatre.** `{{first_name}}` and `{{city}}` only. Fake personalization is worse
   than none — this buyer sees twenty agency emails a week and can spot a template.
6. **Plain text. No images, no HTML signature, no tracking pixel.** Open tracking inflates numbers
   with bot clicks and hurts placement. Track replies.
7. **Compliance footer on every send** — see `06`.

**Merge fields:** `{{first_name}}` `{{company}}` `{{city}}` `{{metro}}` `{{trigger_count}}`
`{{example_trigger}}` `{{facility_type}}`

---

## SEQUENCE 1 — Segment 1, named owner, trigger-matched
*Primary sequence. ~2,000 contacts. Target: 12%+ reply.*

### Email 1 — Day 0
**Subject:** `23 in {{city}}`

```
{{first_name}} — I track businesses in {{city}} that just signed a new lease,
opened a second location, or posted a facilities manager job.

Right now there are {{trigger_count}}. One of them is a {{facility_type}} that
moved into a new building three weeks ago.

They don't have a cleaner locked in yet.

Want the list? Reply "send it" and I'll put it together for {{city}} — names,
addresses, what changed, and who signs.

No charge, no call.
```

### Email 2 — Day 3
**Subject:** `re: 23 in {{city}}`

```
{{first_name}}, following up on the list.

The reason I build these: an office with a cleaner they tolerate won't switch
for a better sales email. They switch when something changes — they move, they
expand, they hire someone whose job is vendors, or their current crew misses
the restrooms twice.

Those windows close in about 60 days.

Want the {{city}} list? One word back and it's yours.
```

### Email 3 — Day 7 (the credibility email)
**Subject:** `how I found you`

```
{{first_name}} — quick note on why you got this.

I pulled every commercial cleaning company in {{metro}} with a website and a
commercial services page, filtered out the franchises and the residential-only
crews, and found your name on your site rather than emailing info@.

That's the same method I use to build the prospect lists. I ran it on you
before I ran it for you.

Still happy to send the {{city}} list — just say the word.
```

### Email 4 — Day 14 (the close-out)
**Subject:** `closing the loop`

```
{{first_name}} — I'll stop here.

If commercial contracts aren't the priority this quarter, no problem at all.

If they are, the {{city}} list is still sitting here and it takes me ten
minutes to send.

Either way — good luck with the back half of the year.
```

---

## SEQUENCE 2 — Segment 2, generic `info@`
*Written to be forwarded. ~4,400 contacts. Target: 4% reply.*

### Email 1 — Day 0
**Subject:** `for whoever handles new contracts`

```
Hi — if this isn't your area, could you pass it to whoever chases commercial
contracts?

I put together a list of businesses in {{city}} that just moved, expanded, or
hired a facilities manager in the last 90 days — the moments when a building
actually goes looking for a cleaner.

{{trigger_count}} of them right now.

Happy to send it over free. Just reply.
```

### Email 2 — Day 4
**Subject:** `re: for whoever handles new contracts`

```
Following up in case this landed in the wrong inbox.

Short version: free list of {{trigger_count}} businesses in {{city}} that have
a reason to change cleaners this quarter. Addresses, what changed, who signs.

Reply and I'll send it.
```

### Email 3 — Day 10
**Subject:** `last one`

```
Last note from me.

If {{company}} is taking on new commercial work, the {{city}} list is free and
ready. If not, I'll leave you alone.

Thanks for the time.
```

---

## SEQUENCE 3 — After the Proof Pack is delivered
*This is where the money is. ~72 people. Target: 22%+ purchase.*

### Delivery email — sent by a human, same day
**Subject:** `{{city}} list — 23 of them`

```
{{first_name}} — here it is.

23 businesses in {{city}}. For each one: address, what changed and when, the
facility type, and the title of the person who signs off on cleaning.

Three I'd start with:
• {{example_1}} — new lease, 41 days ago, no cleaner listed
• {{example_2}} — posted a Facilities Manager role last week
• {{example_3}} — two reviews this month mentioning the restrooms

Sorted by how fresh the trigger is. The top ones go stale in about 60 days, so
I'd work down from the top.

If it's useful, tell me how the first few calls go — I'm curious whether the
fresh-trigger ones land better than the cold ones. My guess is yes, but I'd
rather hear it from someone actually making the calls.
```

> **Note what this email does not do: it does not sell anything.** It gives, it shows judgment, and
> it asks a question they can answer from experience. The reply to that question is the sales
> conversation, and they open it, not you.

### Follow-up — Day 2
**Subject:** `re: {{city}} list`

```
{{first_name}} — did any of those turn into a conversation?

Asking because the list is the output of a system I built, and I'm putting it
in other people's hands now. Before I do, I want to know whether it works as
well for someone else's crew as it does when I run it.

If you got anything out of it I'd genuinely like to hear it. And if you'd
rather just run this yourself every month instead of waiting on me, say so and
I'll show you how it's put together.
```

### Follow-up — Day 5 (the offer)
**Subject:** `running it yourself`

```
{{first_name}} — you asked how the list gets built, so here it is.

Eleven triggers, all from public data: new leases, occupancy permits,
facilities job posts, cleaning complaints in Google reviews, new business
registrations, property managers picking up buildings. Each one has a source, a
freshness window, and an email angle that matches it.

I packaged the whole thing — the trigger board, the automation file, six
sequences written per trigger type, the walkthrough script, and 500 prospects
built for {{metro}}.

$197, one time. For scale, a cleaning company pays $197–$230 for a single
Google Ads lead.

{{link}}

If you'd rather I just built and ran the first 30 days for you, that's an
option too — reply and I'll explain how it works.
```

### Follow-up — Day 9 (last)
**Subject:** `either way`

```
{{first_name}} — last one on this.

The {{city}} list is yours to keep regardless; no strings on it.

If you want the system that produces it: {{link}}
If you want it run for you: reply.
If neither — genuinely, good luck with Q4.
```

---

## SEQUENCE 4 — Post-purchase (protects your refund rate and creates the upsell)

| Day | Subject | Purpose |
|---|---|---|
| 0 | `You're in — start here` | One link, one action: open the Trigger Board and pick one metro. Nothing else. |
| 1 | `Your 500 are being built` | Sets the delivery expectation, creates anticipation, prevents "where's my stuff" refunds |
| 3 | `The one trigger I'd start with` | T5 (cleaning complaints). Fast, free, immediate. First win as early as possible. |
| 6 | `Did you send anything yet?` | The honest re-engagement. Non-starters become refunds; catch them here. |
| 10 | `The walkthrough script` | Re-surfaces an asset they probably missed |
| 14 | `Want me to run the next 30 days?` | The DFY upsell, to buyers who've now seen it work |
| 21 | `How'd it go?` | Testimonial request. You need three by week 6 for the sales page. |

**Day 6 matters more than it looks.** Most refunds come from people who bought and never started.
An email that asks a real question and offers real help on day 6 converts a would-be refund into a
user — and users become the testimonials and the DFY buyers.

---

## Subject-line bank

**Tested-shape principles:** lowercase, short, specific, no punctuation theatre, no "Quick question,"
nothing that reads like a marketing subject.

| Type | Examples |
|---|---|
| Number + place | `23 in {{city}}` · `{{trigger_count}} in {{metro}}` · `11 new leases in {{city}}` |
| Curiosity, plain | `how I found you` · `closing the loop` · `either way` · `last one` |
| Forward-friendly | `for whoever handles new contracts` · `wrong inbox?` |
| Trigger-specific | `new build on {{street}}` · `they posted a facilities job` · `restroom reviews` |

**Never use:** "Quick question" · "Following up" as a standalone · anything with an emoji ·
"Increase your revenue" · "I noticed your website" · anything ALL CAPS or with `!`.
**Legally never use:** a subject line that misrepresents the message. That's the one thing state law
still reaches past CAN-SPAM preemption, and in California it carries $1,000 per email.

---

## A/B tests, in priority order
1. **Sequence 1 email 1: number-in-subject vs. trigger-in-subject.** Biggest single lever.
2. **Gift framing vs. observation framing** ("Want the list?" vs. "Noticed 23 businesses in {{city}}
   just moved").
3. **Proof Pack size: 23 vs. 8.** Fewer, better-annotated prospects may convert higher than a
   longer list — smaller and tighter wins elsewhere in this funnel, so test it here too.
4. **Day-5 offer email: price-first vs. mechanism-first.**

Run one at a time, minimum 400 contacts per arm, and don't call a winner before 400.
