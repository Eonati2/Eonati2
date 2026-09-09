# 08 — Risks, Failure Modes, and the Backup Plays

---

## 1. Ranked risks

### R1 — The trigger lift doesn't materialize · **Likelihood: medium · Impact: severe**
The whole strategy rests on the claim that signal-referencing emails reply at 15–25% vs. a 3.43%
baseline. That figure is ⬤⬤ at best and vendor-adjacent. The funnel models it at 12%; below 6% the
plan's advantage evaporates and you're just another agency emailing cleaning companies.

**Detection:** week 4 gate. **Mitigation:** the test costs 500 emails and one week, and it happens
before you've spent meaningful money. **If it fails:** Plan B below.

### R2 — Cleaning owners don't buy digital products online · **Likelihood: medium-low · Impact: severe**
Owner-operators are in trucks and at job sites. They may want the *outcome* but not want to
implement a system. This is the same objection that ruled out HVAC in the original brief, and it
partially applies here too — honesty requires saying so.

**Countervailing evidence:** The Janitorial Store sells a $647/yr membership; a whole coaching
economy (Grow My Cleaning Company, Profit Cleaners, Hitman masterminds) charges this audience real
money; Udemy sells them sub-$500 courses. They do buy.

**But the mitigation is structural, not hopeful:** the ladder already routes the "I want the outcome,
not the homework" buyer to the $1,497 DFY tier. That's not a fallback — per `03`, it's where half the
revenue is expected to come from. **The risk is priced in.**

### R3 — Deliverability collapse · **Likelihood: medium · Impact: high**
Two complaints a day breaches 0.3%. Under 2026 rules that means rejection, not the spam folder.

**Mitigation:** 6 domains (blast radius limited to 1/6th), 21-day warmup, gift-framed copy that
draws far fewer complaints than pitch copy, instant global suppression, weekly monitoring.
**If it happens:** pause, let domains rest, buy replacements ($12 each). Recoverable — as long as
you kept cold email off the product domain.

### R4 — You are late to this market · **Likelihood: high · Impact: medium**
Elevate Clients, GrowWithBA, Modern Inbound, Abstrakt and others are already publishing detailed
2026 commercial-cleaning cold-email playbooks *for free*, as lead magnets. Your buyer may already
have read three of them.

**Mitigation:** this is exactly why the product cannot be information (`02 §4`). Free blogs cannot
hand someone a built, trigger-scored prospect list for their metro. Compete on the artifact, not the
explanation. **And note the flip side:** their content marketing has already educated the market on
why this works. You're not creating demand, you're converting demand someone else paid to create.

### R5 — 60 days is too short · **Likelihood: high · Impact: medium**
Warmup eats weeks 1–3. First sale lands week 4–6. That leaves 2–4 weeks of real selling.

**Mitigation:** none available — it's physics. **Recommendation: target 90 days, treat 60 as
stretch.** The plan is identical; the extra 30 days remove the dependency on everything going right.

### R6 — Support load on the DFY tier · **Likelihood: medium · Impact: medium**
$1,497 buys expectations. Building someone's domains, warmup, and campaign is 8–12 hours of real
work per client.

**Mitigation:** cap DFY at **5 clients** in the 60 days. Say "5 spots" on the page — it's true, it's
scarcity that isn't manufactured, and it protects delivery quality. Six DFY clients delivered badly
is worse than four delivered well, in a niche where owners talk to each other.

### R7 — Refunds · **Likelihood: medium · Impact: low-medium**
Gumroad keeps its fee on refunds, so a refunded $197 sale costs you ~$26 net.

**Mitigation:** the day-6 "did you send anything yet?" email in Sequence 4 is specifically an
anti-refund mechanism. Most refunds are people who bought and never opened it.

### R8 — Single-person key-man risk · **Likelihood: certain · Impact: medium**
170 hours over 8 weeks, on top of whatever else you're doing.

**Mitigation:** the plan's week-by-week gates mean you can stop at any week boundary with a working
partial asset. Nothing here requires all 8 weeks before producing anything.

---

## 2. Plan B — if the trigger thesis fails at week 4

**Pivot: from "we find the timing" to "we hand you the pipeline."**

Sell the **output**, not the system. A monthly trigger-matched prospect list for one metro,
exclusive to one cleaning company in that metro.

| | Detail |
|---|---|
| Offer | 100 trigger-scored prospects/month, exclusive to one company per metro |
| Price | **$297/month**, Gumroad subscription |
| Path to $10k | **34 subscribers** — or 20 subscribers at $497 for a larger metro |
| Why it survives R1 | Doesn't depend on high reply rates for *them* — it depends on the list being genuinely better than what they can build, which you control |
| Why it survives R2 | Zero implementation burden on the buyer |
| Cost to serve | ~$1/month/subscriber in Apify credits |
| Downside | Recurring delivery obligation; churn; it's a service business, not a product business |

Exclusivity is the real asset here: "the only cleaning company in Tampa getting this list" is worth
more than the data, and it's defensible in a way a PDF never is.

## 3. Plan C — if cleaning owners won't buy at all

**Pivot the buyer, keep the entire machine.** Everything you built — Apify pipeline, trigger board,
sequences, automation — is buyer-agnostic. The identical system sells to any business that wins
recurring B2B contracts from local facilities:

| Alternative buyer | Why it fits | Watch out for |
|---|---|---|
| **Commercial landscaping / grounds** | Same buyer (facilities/property mgmt), same recurring contract, same triggers | Seasonal |
| **Security guard services** | Recurring, facility-based, new-building trigger applies exactly | Longer sales cycles |
| **Pest control, commercial** | Recurring contracts, permit and new-location triggers work | More regulated |
| **Commercial HVAC maintenance** | High contract value | The owner-in-a-truck problem from the original brief |
| **Property maintenance / handyman (commercial)** | Same trigger set | More fragmented |

**Landscaping is the strongest second choice** — near-identical buyer, near-identical triggers,
about 60% of the assets reusable with a find-and-replace. Note also that this makes the Trigger
Board a *portable* asset: whatever happens with cleaning, the IP transfers.

---

## 4. What I would watch that isn't in any spreadsheet

1. **The tone of the negative replies.** If cleaning owners reply *angry* rather than *not
   interested*, the market is over-solicited and the approach needs to change more than the copy
   does. Read them; don't just count them.
2. **Whether people ask "how did you find these?"** That question is the buying signal. Every time
   it appears, the mechanism is doing the selling, and it should be moved further up the sequence.
3. **Whether the packs get forwarded.** If someone says "I sent this to my sales guy," you've found
   the 15–25 employee band where the $497 and $1,497 tiers live.
4. **What they say the list is worth before you name a price.** Ask it on the calls. If the honest
   answer is consistently "$50," the whole price architecture is wrong and better to know in week 5.

---

## 5. The single most likely way this fails

Not deliverability. Not the law. Not competition.

**It's spending weeks 1–3 building automation instead of building 20 proof packs by hand.**

The pipeline diagram in `04` is seductive — it's clean, it's technical, and it feels like progress.
But every conversion in this plan depends on one artifact being genuinely impressive, and you cannot
find out whether it is by building an n8n workflow. You find out by making 20 of them by hand,
looking at them, and asking whether a cleaning company owner would reply "send it."

Build the thing that has to be good before you build the thing that makes it fast.
