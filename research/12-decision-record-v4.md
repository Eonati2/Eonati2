# 12 — Decision Record v4: one product
**2026-09-11 · Supersedes the offer ladder in `02`, `09` and `11`.**

---

## The decision

**One digital product. No service, no implementation tier, no done-for-you.**

| | |
|---|---|
| Product | Commercial Cleaning Client Acquisition OS |
| Launch price | **$149** (range considered: $97–$149) |
| Standard price | $197, after real customer feedback and proof |
| Distribution | Free lead magnet → email → outbound + organic → Gumroad |
| Removed | $497 Setup · $2,000 Managed Pilot |

**Removed entirely, not deferred.** Not mentioned, not built, not promised, no infrastructure.
If customers later ask for implementation help, that is a decision to make then, with evidence.

## Why this is right

**It removes the delivery obligation.** Five pilots at $2,000 were 100% of the gross target *and*
100% of the delivery load — 8–12 hours each, concurrent, with no product revenue cushioning a slip.
A single missed pilot would have taken a fifth of the target with it.

**It removes an unbuilt purchase path.** The tier carrying the target had no way to be bought. That
was the standing blocker for three sessions.

**It matches the evidence.** Commercial-cleaning digital products demonstrably sell — the market
shows products at $15, $49.99, $149, $249 and $1,941. What is *not* evidenced is us selling a
service we have never delivered, to an audience that has never heard of us.

**It makes the business legible.** One thing to sell, one price, one funnel.

## Why launch at $149, not $197

The $149 and $249 examples in the market are sold by people with ratings and track record. We have
neither. **Getting the first ten real buyers is worth more than defending a launch price**, and the
price can rise once there is proof to justify it.

⚠ **The product is already listed at $197.** If it has no sales yet, moving to $149 costs nothing.
If it has sales, dropping the price treats early buyers badly — in that case hold $197 and use the
free product to drive volume instead. **Check before changing the listing.**

---

## The honest consequence — read this one

**Removing the $2,000 tier removes the only route to $10,000 in 90 days that the arithmetic
supported.**

At 2% positive reply and a generous 25% of positive repliers buying, roughly **0.5% of contacted
prospects purchase**. Capacity is ~6,800 contacts in the window.

| Price | Sales needed | Contacts needed at 0.5% | Against 6,800 capacity |
|---|---|---|---|
| $97 | 103 | ~20,600 | **3× over** |
| $149 | 67 | ~13,400 | **2× over** |
| $197 | 51 | ~10,200 | **1.5× over** |

Even at an optimistic 1% purchase rate, $149 × 68 sales lands almost exactly on $10,000 — meaning
the target requires **everything to go right at the top of the plausible range**.

**Outbound alone, at $149, realistically produces somewhere between $3,000 and $10,000.** The
midpoint is well under target.

### What this means, stated plainly

**$10,000 in 90 days is no longer a defensible target for outbound alone.** It becomes reachable
only if the free product, organic distribution and Gumroad's own marketplace traffic carry a
meaningful share — none of which we have any evidence for yet.

This is not an argument against the decision. It is the cost of the decision, and it is worth
paying: a simpler business with a lower ceiling and a far lower chance of failing outright.

**The replacement goal, which is better:**

| Milestone | What it proves |
|---|---|
| **First 10 customers** | People will buy this |
| **First 25** | It is repeatable |
| **First 50** | There is something worth scaling |

Track those. Revenue follows, and each milestone is worth more than the equivalent dollars because
it tells you something the dollars don't.

---

## What changes in the build

| Area | Change |
|---|---|
| `sales/06-selling-the-managed-pilot.md` | **Deleted** |
| CRM lifecycle (our pipeline) | Collapsed to 7 stages — see below |
| CRM fields | `product` enum reduced to one value; `pilot_slot` and `over_capacity` removed |
| Outbound sequences | The pilot opener removed from the day-5 offer email |
| Gumroad assets | Price to $149; "no upsell" is now literally true |
| Free lead magnet | **New.** Spec in `../commercial-cleaning-os/offers/free-product.md` |

### The simplified pipeline

```
Lead → Engaged → Interested → Product consideration → Purchased → Customer → Repeat / referral
```

Seven stages instead of fourteen. There is no walkthrough, no proposal, no negotiation — we are not
running a sales process, we are running a funnel. The full 13-stage pipeline remains in the
**product**, where it belongs: that is the customer's sales process, and it is unchanged.

---

## What is deliberately kept

**The research files stay as they are**, with this record superseding them. `11-corrections-log.md`
in particular is an audit trail; rewriting it to pretend the pilot was never planned would destroy
the reasoning that led here, and that reasoning is the reason this decision is well-founded.

**Nothing in the customer product changes because of this.** It never mentioned our pricing or our
tiers — the contamination audit confirmed that. The buyer's own sales process still includes
walkthroughs and proposals, because that is their business.
