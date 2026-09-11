# Instance A Sequences — ours

Selling the Client Acquisition OS to cleaning company owners.
**Supersedes `research/05-email-sequences.md`**, which was written against the earlier positioning.

## Rules
1. **CTA is a reply, never a link.** No link in the first two emails of any sequence.
2. **The first ask is a give** — a pack of trigger-matched accounts in their own city.
3. **Under 90 words.** Read on a phone, between jobs.
4. **Merge fields only:** `{{first_name}}` `{{city}}` `{{metro}}` `{{trigger_count}}`
   `{{example_1}}` `{{example_1_event}}` `{{example_1_days}}`. Fake personalization is worse than
   none; this audience sees twenty agency emails a week.

   **⚠ Tag casing is unverified.** These are written snake_case (Smartlead convention). Instantly
   and several others use camelCase (`{{firstName}}`). **Confirm against the actual sequencer
   before the first send** — wrong casing means prospects receive the literal `{{first_name}}`.
   No sequencer has been chosen yet, so this is an open item, not a decision.

5. **Every `{{example_*}}` field must be populated from a `Trigger_Event` row** — its `evidence`,
   its `trigger_date`. If the pack has no qualifying example, the email does not send. A named
   example is the most checkable sentence in the message and the most damaging one to get wrong.
6. **Plain text.** No images, no HTML signature, **no tracking pixel** — open tracking inflates
   numbers with bot activity and hurts placement.
7. **Never assert anything about a third party you cannot evidence.**
8. Compliance footer on every send.

---

## SEQ-A1 · Trigger-matched, named owner
*Campaign `A-TRIG-OWNER`. The priority sequence.*

### Email 1 — day 0
**Subject:** `{{trigger_count}} in {{city}}`
```
{{first_name}} — I track commercial signals in {{city}}: new leases, second
locations, occupancy permits, facilities-manager job posts.

Right now there are {{trigger_count}}. The most recent is {{example_1}} —
{{example_1_event}}, {{example_1_days}} days ago.

Want the list? Reply "send it" and I'll put it together for {{city}} — names,
addresses, what changed and when, and the title of whoever signs.

No charge, no call.
```

### Email 2 — day 3
**Subject:** `re: {{trigger_count}} in {{city}}`
```
{{first_name}}, following up on the list.

The reason I build these: an office that already has a cleaner won't switch
for a better sales email. Something has to change first. They move, they
expand, they hire someone whose job is vendors.

I sort the list by how recent the change is, because the older ones tend to
be settled by the time you call.

Want the {{city}} list? One word back and it's yours.
```

### Email 3 — day 7
**Subject:** `how I found you`
```
{{first_name}} — quick note on why you got this.

I pulled every commercial cleaning company in {{metro}} with a website and a
commercial services page, filtered out the franchises and the residential-only
crews, and found your name on your site rather than emailing info@.

Same method I use to build the prospect lists. I ran it on you before I ran it
for you.

Still happy to send the {{city}} list.
```

### Email 4 — day 14
**Subject:** `closing the loop`
```
{{first_name}} — I'll stop here.

If commercial contracts aren't the priority this quarter, no problem.

If they are, the {{city}} list is still here and takes me ten minutes to send.

Either way — good luck with the back half of the year.
```

---

## SEQ-A2 · Broad, named owner, no trigger
*Campaign `A-BROAD-OWNER`. Cut this first when capacity is tight.*

Same four emails, with email 1's opening replaced — there is no trigger to reference:
```
{{first_name}} — I build lists of businesses in {{city}} that have recently
moved, opened a second location, or posted a facilities-manager job. The
moments when a building actually goes looking for a cleaner.

Happy to put one together for {{city}} — free, no call. Want it?
```
Drop email 3 (the credibility email depends on having researched them specifically).

---

## SEQ-A3 · Generic inbox
*Campaign `A-GENERIC`. Written for the person who forwards it.*

### Email 1 — day 0
**Subject:** `for whoever handles new contracts`
```
Hi — if this isn't your area, could you pass it to whoever chases commercial
contracts?

I put together lists of businesses in {{city}} that recently moved, expanded,
or hired a facilities manager — the moments a building goes looking for a
cleaner.

{{trigger_count}} right now. Happy to send it over free. Just reply.
```

### Email 2 — day 4
**Subject:** `re: for whoever handles new contracts`
```
Following up in case this landed in the wrong inbox.

Short version: free list of {{trigger_count}} businesses in {{city}} with a
recent reason to review cleaning. Addresses, what changed, who signs.

Reply and I'll send it.
```

### Email 3 — day 10
**Subject:** `last one`
```
Last note from me.

If {{company}} is taking on new commercial work, the {{city}} list is free and
ready. If not, I'll leave you alone.
```

---

## SEQ-A4 · After the pack — **manual send**
*Campaign `A-PACK`. Where the revenue is. Never automated.*

### Delivery — same day, sent by a human
**Subject:** `{{city}} list`
```
{{first_name}} — here it is.

{{trigger_count}} businesses in {{city}}. For each: address, what changed and
when, the facility type, and the title of the person who signs off on
cleaning.

Three I'd start with:
• {{example_1}} — new lease, 41 days ago
• {{example_2}} — posted a Facilities Manager role last week
• {{example_3}} — opened a second location in August

Sorted by how recent the signal is. I'd work down from the top, because the
older ones are more likely to be settled already.

If it's useful, tell me how the first few calls go — I'm curious whether the
recent ones land better than the cold ones. My guess is yes, but I'd rather
hear it from someone actually making the calls.
```

**This email sells nothing.** It gives, shows judgment, and asks a question they can answer from
experience. Their reply opens the sales conversation — they open it, not you.

### Day 2
**Subject:** `re: {{city}} list`
```
{{first_name}} — did any of those turn into a conversation?

Asking because the list is the output of a system I built, and I'm putting it
in other people's hands now. Before I do, I want to know whether it works as
well for someone else's crew as it does when I run it.

If you got anything out of it I'd like to hear it. And if you'd rather run
this yourself every month instead of waiting on me, say so and I'll show you
how it's put together.
```

### Day 5 — the offer
**Subject:** `running it yourself`
```
{{first_name}} — you asked how the list gets built, so here it is.

Public signals: new leases, occupancy permits, facilities job posts, property
management changes, new locations. Each one has a source, a freshness window,
and an approach that matches it.

I packaged the whole thing — the trigger library, the automation file, the
sequences, the walkthrough and proposal workflows, and 500 accounts built for
{{metro}}.

$149, one time. {{link}}

If it's useful, tell me how you get on — I'm still learning what lands in
different markets.
```

**No upsell, because there isn't one.** One product, one price. The closing line asks for feedback
rather than money, which is the only thing worth asking a first buyer for.

### Day 9
**Subject:** `either way`
```
{{first_name}} — last one.

The {{city}} list is yours to keep regardless.

If you want the system that produces it: {{link}}
If not — good luck with Q4 either way.
```

---

## Subject-line bank
Lowercase, short, specific. No punctuation theatre.

**Use:** `{{trigger_count}} in {{city}}` · `how I found you` · `closing the loop` · `either way` · `last one` ·
`for whoever handles new contracts` · `running it yourself`

**Never:** "Quick question" · "Following up" alone · any emoji · "Increase your revenue" ·
"I noticed your website" · anything ALL CAPS or with `!`

**Legally never:** a subject that misrepresents the message. It is the one thing state law reaches
past CAN-SPAM preemption, and California attaches $1,000 per email.

---

## Tests, in priority order
1. Email 1 subject: number-in-subject vs trigger-in-subject
2. Gift framing vs observation framing
3. Pack size: ~23 vs ~8 well-annotated
4. Day-5 offer: price-first vs mechanism-first

One at a time, minimum 400 contacts per arm. **Do not call a winner before 400**, and state the
sample size whenever you report a result.
