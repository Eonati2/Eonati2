# 09 — Decision Record v2
**Date:** 2026-09-09 · Supersedes conflicting guidance in `00`–`08` where noted.

This records the locked decisions, what changed from v1, and four corrections where the revised
plan and the funnel math still disagree.

---

## 1. Locked

| Decision | Value | Change from v1 |
|---|---|---|
| Niche | Commercial cleaning / janitorial | unchanged |
| Buyer | Owner / sales manager / BD manager | unchanged |
| Product | **Commercial Cleaning Client Acquisition OS** | renamed from "The Walkthrough Engine" |
| Category | Outbound infrastructure — *not* cleaning-business education | sharpened |
| Core mechanism | Account → decision maker → trigger → outreach → follow-up → walkthrough | **accounts-first, people second** (v1 was people-first) |
| Pilot account geography | Dallas–Fort Worth | new |
| Target account tiers | Property mgmt → medical → office → industrial → schools/gyms | new, ordered |
| Timeline | **90 days** | was 60 |
| Price entry | $149–$199 | was $197 |
| Done-for-you | Cap at 5 | unchanged |
| Channel | **Email + phone** | v1 was email-only |
| Modelling assumption | **1–3% positive response** | more conservative than v1's implied ~1.3% |
| $10k | Aggressive target, not a forecast | unchanged |

## 2. Accepted without reservation

**The rename from "lead generation" to "contract acquisition."** Correct, and it is the single best
change in the revision. The buyer does not want leads; they want recurring contracts. "Lead
generation" is the commodity category the free agency playbooks already own.

**Accounts-first architecture.** v1's pipeline started from cleaning companies and worked toward
people. Starting from *buildings worth pursuing* is more defensible and produces better packs. The
scraper is infrastructure, not moat — agreed. The moat is knowing which account, who decides, why now.

**90 days over 60.** Agreed, and for the stated reason: 60 days forces premature scaling. The v1
dossier reached the same conclusion from a different direction (warmup consumes weeks 1–3).

**The Gumroad competitor audit.** This closes the one open unknown flagged in `01 §I`. The finding
— a $1,941 high-ticket program, a $13.47 marketing guide, a $15+ pricing blueprint, $29–39 AI
toolkits — is genuinely good news, and the whitespace read is right: nobody in that set is selling
outbound infrastructure. *These figures come from the operator's own search and have not been
independently re-verified here (Gumroad is not reachable from this session).*

**Phone as a channel.** Correct on the merits — this is a relationship-driven market and email alone
under-performs. But it carries a legal cost the plan does not yet price. See Correction 1.

---

## 3. Four corrections

### Correction 1 — Phone adds real legal exposure, concentrated exactly where your data comes from

The revised plan adds phone as a primary channel and keeps a compliance section that covers only
CAN-SPAM. Cold calling is governed by a different regime with **a private right of action of
$500–$1,500 per call**, plus state mini-TCPA statutes on top.

| Rule | Status |
|---|---|
| B2B calls to a **verified business landline** | Generally exempt from the federal DNC registry |
| B2B calls to a decision-maker's **personal cell** | **Not exempt.** Treated as residential under the TCPA regardless of how it's labelled in your CRM |
| Autodialer or prerecorded voice to a cell | Requires prior express written consent — B2B included |
| Calling window | 8am–9pm local; applies to cell numbers even in a B2B context |
| TSR B2B exemption carve-out | Does **not** apply to sellers of *nondurable office or cleaning supplies* — worth a lawyer's eye given the adjacency, though a system sold to cleaning companies is not itself a cleaning-supply sale |

**Why this lands hardest on exactly this plan:** Google Maps listings for small local businesses are
overwhelmingly **mobile numbers**. Owner-operated cleaning companies list a cell as the business
line constantly. So the channel you are adding is aimed at the number type that carries the
exposure, sourced from the dataset that produces it.

**Required changes:**
1. **Manual dialing only.** No autodialer, no power dialer, no prerecorded or AI voice drops.
2. **Classify every number** as landline or wireless before dialing — line-type lookup is cheap and
   this is what it's for.
3. **Wireless numbers: manual dial, business hours local, and a suppression list that a "don't call
   me" updates instantly and permanently**, shared with the email suppression list.
4. **The product must teach this too.** You are selling a calling system to people who will point it
   at *their* prospects. Shipping a phone playbook without the TCPA module is handing a customer
   $500–$1,500-per-call exposure with your name on the box.

Handled properly this is a differentiator, exactly as the CAN-SPAM module is. Handled casually it is
the largest uninsured risk in the plan.

### Correction 2 — The validation sample cannot answer the question it exists to answer

The plan sets Days 15–30 at **100–200 highly qualified prospects**, under a **1–3% positive
response** assumption. Run those together:

| Prospects | At 1% | At 2% | At 3% |
|---|---|---|---|
| 150 | 1–2 positives | 3 positives | 4–5 positives |
| 500 | 5 | 10 | 15 |
| 750 | 7–8 | 15 | 22 |

At n=150 the expected outcome is about **three positive replies**, with a plausible range of roughly
one to seven. That range is consistent with a 1% offer *and* a 3% offer — and 1% versus 3% is a
threefold difference in the entire business model. **The test is designed to distinguish exactly the
two outcomes it cannot distinguish.**

Worse, the failure mode is asymmetric: a disappointing result at n=150 will read as "the offer
doesn't work" when it is equally consistent with an offer that works fine.

**Change:** validation window targets **500–750 qualified prospects**, not 100–200. Same
qualification bar, same multichannel treatment — just enough of them that ten or more positives
accumulate. Below ~10 events you are reading noise, and you will make a 90-day decision on it.

### Correction 3 — The $49 tier spends your scarcest resource on your smallest outcome

Under the conservative model you will generate roughly **70–80 positive replies in 90 days.** That
is the binding resource in this business — rarer than money, rarer than prospects, rarer than time.

| Tier | Net after Gumroad | Value per positive reply consumed |
|---|---|---|
| $49 Starter | ~$43 | $43 |
| $149 Core | ~$129 | $129 |
| $249 Pro | ~$216 | $216 |
| $1,500 implementation | ~$1,305 | $1,305 |

A $49 entry point converts a positive reply — of which you have fewer than eighty — into $43.

**Change:** remove $49 from the outbound funnel. It has a legitimate role, but a different one:
list it as a **standalone Gumroad Discover product**. Discover's 30% fee is painful on high ticket
and irrelevant on a $49 impulse buy, and it brings marketplace traffic you didn't have to source.
Two products, two traffic sources, two economics — never let the cheap one touch the outbound
funnel.

### Correction 4 — "Dallas–Fort Worth" is being asked to do two incompatible jobs

There are two geographies in this business and the decision sheet has merged them:

| | Geography of… | Correct answer |
|---|---|---|
| **Pipeline 2** | the *accounts* inside the product's prospect pack (your customer's targets) | **DFW.** Correct as the pilot. |
| **Pipeline 1** | the *cleaning companies you sell to* (your own prospects) | **Not DFW.** Nowhere near enough supply. |

A single metro yields on the order of a hundred to a few hundred qualified commercial cleaning
companies. The conservative model needs **3,500–4,000 qualified prospects** to reach $10k. That is
an order-of-magnitude gap; DFW cannot be your sales territory.

But selling nationally while shipping a DFW-only pack breaks the offer for almost every buyer — an
Atlanta cleaning company has no use for Dallas accounts.

**The resolution, which the architecture already supports:** DFW is the **pilot and the public
demo**, built once, by hand, to prove the method and to sell from. The product builds a pack for
**the buyer's own metro, on demand.** At roughly $0.20 per pack in scrape credits this is free, and
it is what makes the offer work nationally.

**Change:** sell into **10–15 metros**; build **one** DFW pack as the demo; deliver every buyer a
pack for their own city.

---

## 4. The conservative model, re-run

Using the plan's own **2% positive response** and a generous **25%** positive-reply-to-purchase:

| Route | Path to $10,000 | Qualified prospects needed |
|---|---|---|
| **Product-only** (blended AOV ~$180 with the $49 tier in) | 56 sales | **~11,200** |
| **Product-only** (AOV ~$230, $49 tier removed) | 44 sales | **~8,800** |
| **DFY-led** — 5 implementations @ $1,500 = $7,500, plus ~14 product sales | 19 buyers | **~3,500–4,000** |

**The conclusion the revision has not yet drawn from its own assumption:** under a 1–3% positive
response, **the five done-for-you clients are not a research laboratory that happens to earn money.
They are 70–75% of the $10,000.** The product-only route needs roughly three times the prospect
volume, which is three times the scraping, enrichment, sending, dialling and compliance surface.

They are still research laboratories — that framing is right and worth keeping. But they should be
**priced at the top of the stated range ($2,000, not $1,000), sold deliberately from day one, and
staffed for**, rather than treated as a by-product of a product launch.

**Corollary:** the most important sentence on the sales page is not the one that sells a $149
download. It is the one that makes a cleaning company owner ask *"could you just do this for me?"*

---

## 5. Open items

1. **DFW qualified-company count** — could not be verified from this session (no hard figure in
   public sources; directory counts include duplicates and service-area listings). Resolve by
   running the actual scrape + qualification pass. It's an afternoon's work and it sizes Pipeline 1.
2. **TSR cleaning-supplies carve-out** — worth 30 minutes with a lawyer before the phone channel
   goes live, given the industry adjacency.
3. **Reddit and HN sourcing** — still unverifiable from this session. The operator's September 2026
   findings are accepted as input; no part of this plan depends on them.
