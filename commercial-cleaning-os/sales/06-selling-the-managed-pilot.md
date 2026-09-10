# 06 — Selling the Managed Pilot

**Instance A — our own sales motion.** How a proof-pack conversation becomes a $2,000 Managed Pilot.

**CRM:** stage 7 `Conversation` → 8 `Offer Made` → 9/10/11.

---

## 1. The blocker, stated plainly

**Only the $197 Core OS is listed on Gumroad. Setup and Managed Pilot have no purchase path.**

Five pilots at $2,000 are the entire gross target
(`../../research/11-corrections-log.md` §A2). So **the tier that carries 100% of the target is the
one nobody can currently buy**, while the tier that is live carries the upside.

That is backwards, and it is the highest-priority fix in the whole build. Three ways to close it,
cheapest first:

| Option | Effort | Notes |
|---|---|---|
| **Two more Gumroad products** at $497 and $2,000, unlisted, sold by direct link | ~1 hour | Recommended. Same merchant-of-record handling, same payout, no new tooling. Unlisted keeps the public page clean, per the "don't clutter the core product" rule |
| Stripe payment link | ~1 hour | Lower fees, but a second payout rail and you handle tax treatment yourself |
| Manual invoice | 0 | Fine for the first one or two; does not scale and slows the close |

**Until one exists, every pilot close ends in an awkward pause** — the worst possible moment to
introduce friction, because it lands immediately after the buyer says yes.

**Recommendation:** create the two unlisted Gumroad products before the next outbound batch goes
out. Record them in the CRM `product` enum, which already anticipates all three.

---

## 2. Where the pilot conversation comes from

Not from the sales page. From the proof pack.

```
Reply → Pack requested → Pack delivered (by a human) → they respond
   → the question that matters → Offer
```

**The question that matters:** *"How did you build this?"* or *"Could you just do this for me?"*

The second one is the buying signal for the pilot, and it is the metric worth watching above all
others (`../../research/11-corrections-log.md` §F). When it recurs, the pilot is the product.

**Do not pitch the pilot before the pack lands.** The pack is the demonstration; pitching a
$2,000 service to someone who has not seen the output is a cold pitch with a big number on it.

---

## 3. The offer call — 20 minutes

### Open on what the pack showed them
> *"You mentioned three of those looked worth chasing. Did you get to any of them?"*

Their answer determines the whole call:

| They say | Read |
|---|---|
| "I called two, one's interested" | **Best case.** They have proof it works. Go to §4 |
| "Haven't had time" | The real problem is capacity, not knowledge → pilot |
| "The data was off on a couple" | Fix it, honestly. Credibility now beats a close |
| "Not really relevant to us" | Targeting was wrong. Learn why — that is worth more than the sale |

**"Haven't had time" is the most common answer and the most important one.** It means the Core OS
would sit unopened, and the pilot is genuinely the right recommendation rather than the expensive
one.

### Diagnose before recommending
1. *"How are you getting commercial work now?"* — referral, bids, existing relationships
2. *"How many walkthroughs did you do last month?"* — the real capacity number
3. *"Who'd run this if you had it?"* — them, a salesperson, or nobody
4. *"What happens if you don't fix this?"* — urgency, in their words

**Question 3 decides the tier.** Nobody to run it → Managed Pilot. Someone who could run it with
help → Setup. A hands-on owner who likes systems → Core OS.

### Recommend one thing
> *"Honestly — based on what you've said, I don't think the $197 system is right for you. You'd
> buy it and it'd sit there, because the constraint isn't knowing how, it's that nobody has three
> hours a week. What I'd suggest is the managed pilot: I build it and run the first 30 days, you
> take the calls that come out of it. It's $2,000, and I only run five at a time because it's
> 8–12 hours of my week each."*

**Recommending against your own cheaper product is the strongest move available**, and it is only
credible because it is true. If the Core OS genuinely fits, sell the Core OS.

---

## 4. What the pilot actually includes — be concrete

Vagueness at $2,000 kills the close.

| | Deliverable |
|---|---|
| Week 1 | ICP and segment agreed · 2,000 accounts built for their metro · trigger-scored |
| Week 1 | Sending infrastructure: domains, mailboxes, authentication, warmup started |
| Week 2 | Sequences written for their voice and their segments · reply routing set up |
| Weeks 3–6 | Campaign runs. All replies routed to them, same day |
| Throughout | Weekly 30-minute call |
| End | The full system handed over, theirs to keep, plus a written debrief |

**What they get at the end:** the accounts, the infrastructure, the sequences, and the Core OS
itself. They own it.

**What is not included, said out loud:** we do not make their calls, run their walkthroughs, or
write their proposals. We produce conversations; they close them.

**What we do not promise:** a number of leads, meetings, walkthroughs, or contracts. Anyone
promising that on a 30-day cold outbound pilot is guessing. Say what will be built and run —
not what it will yield.

---

## 5. Objections

### "Can I just buy the $197 version and try it myself?"
> *"Absolutely, and if you've got the time it's the better value. The honest question is whether
> it'll get done. If it's still sitting there in a month, the pilot's here."*

Then actually sell them the $197. A Core OS buyer who succeeds is a pilot buyer in three months,
and a reference either way.

### "$2,000 is a lot"
> *"It is. One office contract at $600 a month is $7,200 a year, so it's about a third of one
> account. Whether that's worth it depends on whether you think this produces one — and I can't
> promise it will."*

The ROI frame is sound because the contract values are real and independently corroborated
(`../../research/01-market-evidence.md` §C). **The refusal to promise an outcome is what makes the
frame credible.**

### "What if it doesn't work?"
Do not invent a guarantee. State what is actually true:

> *"You keep everything — the accounts, the domains, the sequences, the system. If nothing lands in
> 30 days you still have a working machine and a list, and you'll know a lot more about which
> triggers matter in your market. What I can't do is promise contracts."*

### "Why only five?"
> *"Because it's 8 to 12 hours of my week each and I'd rather do five properly than eight badly."*

True, so it holds up. Do not dress it as scarcity marketing.

### "Can you show me a client who's done this?"
Until there is one: **say so.**

> *"You'd be one of the first five — that's exactly why it's five and why it's priced where it is.
> What I can show you is the pack I built for your market, which is the same method."*

Never invent a case study. In a market where owners talk to each other, it will be found out, and
the whole positioning depends on not being another marketer.

---

## 6. Closing

> *"Want me to send the payment link and get you scheduled? I've got [n] of the five slots open,
> and I'd start you on the [date]."*

**Check the capacity gate before you say a number.** If all five are full:

> *"All five are running right now. I'm not going to take your money and stack you behind them —
> I'd rather put you on the list for the next cohort starting [date]. In the meantime the $197
> system is yours if you want to make a start."*

Turning down $2,000 you cannot deliver is the correct call, and it is the version of scarcity that
is actually real.

→ `Nurture` with a review date. Never a vague waitlist.

---

## 7. After the sale

| When | Action |
|---|---|
| Immediately | Payment confirmed → stage 11, `pilot_slot` assigned |
| Day 0 | Kickoff scheduled within 5 business days |
| Weekly | 30-minute call. Attended by us, not rescheduled |
| Day 30 | Written debrief: what ran, what came back, what to do next |
| Day 30 | **The research conversation** — see below |
| Day 45 | Reference and testimonial request, if it went well |

### The first five are the product research

Per the strategy: these five are revenue, case studies, customer research and process validation at
once. At day 30, ask every one:

1. What was harder than expected?
2. What did I do that you could have done yourself?
3. What did you want me to do that I didn't?
4. Which triggers actually produced conversations?
5. Would you pay to keep it running? At what?

**Question 3 defines v2 of the Core OS.** Question 5 tells you whether a recurring offer exists.
Log all five verbatim as Activity rows — this is the highest-value data the business will generate
this quarter, and it evaporates if it is not written down the same week.
