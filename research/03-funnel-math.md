# 03 — Funnel Math

Every rate here is taken from the **pessimistic end** of the ranges in `01-market-evidence.md §E`,
because most of those benchmarks are published by companies selling cold email software.

---

## 1. The binding constraint is capacity, not list size

You have 1.26M businesses available and can only touch a few thousand. Work backwards from what
you can physically send in 60 days.

| Input | Value | Why |
|---|---|---|
| Window | 60 days ≈ 8.5 weeks | |
| Weeks 1–3 | **Build + domain warmup** | Warmup is 2–3 weeks. Non-negotiable. |
| Actual sending window | 5.5 weeks = **27 business days** | |
| Sending inboxes | 24 (6 domains × 4 inboxes) | |
| Sends per inbox per day | 28 | Safe 2026 practice under the 0.3% complaint regime |
| Daily capacity | 672 | |
| **Total sends in the window** | **≈ 18,000** | 27 business days × 672/day = 18,144. **Business days, not calendar days** — 60 calendar − 21 warmup = 39 calendar ≈ 27 business. |
| Average touches per contact (sequence halts on reply) | 2.8 | |
| **Contacts you can actually reach** | **≈ 6,400** | |

> **Write this on the wall: 6,400 contacts.** Not 100,000. Every strategy decision below is about
> extracting maximum revenue from 6,400 people, which is exactly why targeting and price beat volume.

---

## 2. Model A — the plan as originally briefed

*Scrape → email → click → landing page → Gumroad checkout, $149 flat.*

| Step | Rate | Result |
|---|---|---|
| Sends | — | 18,000 |
| Delivered | 92% | 16,560 |
| Real CTR (bot-filtered) | 1.5% | 248 clicks |
| Cold-traffic page → purchase | 2.0% | **5 sales** |
| Gross @ $149 | | **$745** |
| Net after Gumroad | −12.9% −$0.80 | **$645** |

**Against $10,000: it delivers 7%.** And this isn't a tuning problem:

```
$10,000 ÷ $149  = 67 sales
67 ÷ 5          = 13.4×
13.4 × 18,000   ≈ 241,000 sends
```

**~240,000 sends — about 13× your capacity**, at a volume that would destroy your domains and your
compliance posture long before it produced revenue.

> *Correction (2026-09-10): an earlier version of this file said "roughly 1.6 million sends." That
> figure did not follow from the model above and was inflated by about 6.6×. The conclusion is
> unchanged — the funnel cannot reach the target — but the number was wrong. See `11`.*

**Root cause:** the funnel asks a stranger to click a link and hand a credit card to an unknown
brand, with no human contact anywhere. Both conversion steps are the weakest-converting steps in
outbound, and you multiplied them together.

---

## 3. Model B — reply-based, trigger-targeted, laddered

Same 18,000 sends. Three changes: **split the list by trigger quality**, **ask for a reply instead
of a click**, **sell on the thread**.

### Segment 1 — trigger-matched (the tight list)
| Step | Rate | Result |
|---|---|---|
| Contacts | — | 2,000 |
| Reply rate | **12%** *(benchmark says 15–25% for signal-based; modeled low)* | 240 replies |
| Positive share of replies | **25%** *(vs 14% baseline — relevance lifts it)* | **60 positive** |

### Segment 2 — broad ICP (no trigger)
| Step | Rate | Result |
|---|---|---|
| Contacts | — | 4,400 |
| Reply rate | **4%** | 176 replies |
| Positive share | **14%** *(baseline)* | **25 positive** |

### Conversion of positive replies
| Step | Rate | Result |
|---|---|---|
| Total positive replies | | **85** |
| Proof Pack requested & delivered | 85% | 72 |
| Pack → purchase (base case) | **22%** | **16 buyers** |

### Revenue at base case
| Tier | Mix | Buyers | Revenue |
|---|---|---|---|
| Engine $197 | 65% | 10 | $1,970 |
| Engine + Build $497 | 25% | 4 | $1,988 |
| Done-For-You $1,497 | 10% | 2 | $2,994 |
| Order bumps (+$97, 25% attach on Engine) | | 3 | $291 |
| **Gross** | | **16** | **$7,243** |
| **Net after Gumroad** | | | **≈ $6,300** |

### The band (this is the honest picture)
| Scenario | Pack→purchase | Buyers | Tier mix | **Gross** |
|---|---|---|---|---|
| Conservative | 15% | 11 | 75/20/5 | **≈ $4,900** |
| **Base** | **22%** | **16** | **65/25/10** | **≈ $7,200** |
| Optimistic | 30% | 22 | 55/30/15 | **≈ $12,400** |

**Model B alone reaches $10,000 only in the optimistic case.** That's the finding. Anyone who tells
you a single cold email campaign gets you there is selling you something.

---

## 4. Model C — closing the $2,800 gap

The gap is real and it is closed by **three deliberate additions**, not by sending more email.

| Addition | Mechanism | Realistic contribution |
|---|---|---|
| **C1. Push the top of the ladder** | On every positive reply, offer the walkthrough call. On the call, DFY is the default recommendation, not the upsell. Two extra DFY sales = the entire gap. | **+$1,500–$3,000** |
| **C2. Second channel: the cleaning communities** | The Facebook groups (Cleaning Business Owners USA, Commercial & Residential Cleaning Business Owners, The Cleaning Business: University & CEO Lab), r/Cleaningbusiness, ISSA/BSCAI circles. Post the *free* Proof Pack for one commenter's city per day. It's a give, it's public, and it's proof. Warm traffic converts 3–5× cold. | **+$1,000–$2,500** |
| **C3. Affiliate / partner** | The cleaning-coach economy already owns this audience (podcasts, memberships, masterminds). Offer 40% recurring on a $197–$497 product to two of them. Costs nothing until it works. | **+$0–$2,000** (slow to start, compounds after day 60) |

**Model C combined projection: $9,700 – $14,700 gross. Base case ≈ $11,000.**

> **The strategic sentence:** roughly **half your revenue comes from 4–6 people paying $497–$1,497**,
> not from sixty people paying $197. Build the offer, the sales page, and the reply-handling script
> around those 4–6 people. Everything else is volume that pays for the infrastructure.

---

## 5. Sensitivity — what actually moves the number

Base case $7,243 (Model B), one variable at a time:

| Change | New gross | Δ |
|---|---|---|
| Trigger reply rate 12% → 20% *(exceptional case — do not plan on it)* | $10,400 | **+$3,200** |
| Trigger reply rate 12% → 6% *(triggers don't work)* | $5,300 | −$1,900 |
| Pack→purchase 22% → 30% | $9,900 | **+$2,700** |
| AOV: mix shifts to 50/30/20 | $9,800 | **+$2,600** |
| Price $197 → $149 across the board | $6,300 | −$940 |
| Double the sends (48 inboxes, 2× infra cost) | $12,900 | +$5,700, at ~$450/mo more cost and materially more deliverability risk |
| Segment 1 grows 2,000 → 3,500 contacts *(more trigger research, no more infra)* | $9,600 | **+$2,400** |

**Read the table:** the three cheapest levers are **trigger quality**, **proof-pack conversion**, and
**growing the trigger-matched segment**. All three are *research effort*, not spend. Doubling
infrastructure is the worst lever per dollar and per unit of risk. This is a business where thinking
harder genuinely beats sending more — which is unusual, and it is the whole reason this niche works.

---

## 6. Cost model

| Line | Setup | Monthly | 60-day total |
|---|---|---|---|
| 6 sending domains | $72 | — | $72 |
| 24 mailboxes @ $6 | — | $144 | $288 |
| Sequencer (Smartlead unlimited) | — | $174 | $348 |
| Apify credits | — | $25 | $50 |
| Email verification | — | $30 | $60 |
| Postal address (CMRA/PO box) | $20 | $15 | $50 |
| Landing page domain + host | $15 | — | $15 |
| **Total cash out** | | | **≈ $885** |

Against a base case of ~$11,000 gross / ~$9,600 net: **~11× on cash deployed.** The scarce resource
is your hours in weeks 1–3, not money.

---

## 7. Weekly scoreboard and kill criteria

Track these seven numbers only. If a gate fails, **stop and fix that one thing** — do not send more.

| Week | Milestone | Gate — fail means stop and fix |
|---|---|---|
| 1 | Domains bought, DNS set, warmup started, product outline done | DMARC not passing → nothing else matters |
| 2 | Trigger Board built, first 1,000 contacts scraped & verified | Bounce rate on test batch >3% → verification is broken |
| 3 | Product v1 shipped, page live, first 500 sends | Spam complaint rate >0.1% → pause, fix copy or list |
| 4 | 3,000 sends cumulative | **Trigger-segment reply rate <6%** → the trigger thesis is wrong; pivot to Plan B in `08` |
| 5 | 7,000 sends, first proof packs out | <15 positive replies → the offer or the ICP is off, not the volume |
| 6 | 11,000 sends, **first sale must exist** | **Zero sales by end of week 6** → stop sending, go interview 5 positive-repliers about why they didn't buy |
| 7 | 15,000 sends, first DFY conversation | Pack→purchase <10% → the product isn't matching what the pack promised |
| 8 | 18,000 sends, close the ladder | — |

**The two numbers that predict everything:** *positive replies per 1,000 sends* (target ≥5) and
*proof-pack → purchase* (target ≥20%). Everything else is noise. If those two are healthy and
revenue is still short, the answer is simply more weeks — the machine works and needs runtime.

---

## 8. Timeline honesty

**$10,000 in 30 days is not achievable** under any model here. Warmup alone consumes weeks 1–3, and
the first sale realistically lands in week 4–6.

**$10,000 in 60 days is achievable in the base case of Model C**, and it depends on two things going
right: the trigger reply lift being real (tested in week 4), and 4–6 people buying at $497+.

**$10,000 in 90 days is comfortable** — the same machine, three more weeks of sending, plus the
affiliate channel actually maturing. If you have the option, take 90 days. The plan doesn't change;
it just stops needing luck.
