# Executive Brief — Commercial Cleaning / Gumroad / Outbound
**Date:** 2026-09-09 · **Status:** research complete, strategy revised · **Target:** $10,000 gross in 30–60 days

---

## 1. The verdict in one paragraph

**Your niche choice is right. Your funnel is wrong.** Commercial cleaning survives every test I
put it through — the buyers exist in volume, they have a quantified revenue problem, they already
spend money on exactly this problem, and the data is cheap and public. But the mechanism in the
brief — *scrape → email → click → Gumroad checkout* — cannot produce $10,000 in 60 days. Not
"probably won't." Cannot, at any list size you can realistically build and send. The arithmetic is
in `03-funnel-math.md` and it is not close: it lands around **$1,100**, not $10,000. The fix is not
more emails. It is a different *conversion mechanism* (reply-based, not click-based), a different
*price architecture* (a ladder topping out at four figures, not a flat $149), and a different
*first ask* (give a free artifact, don't pitch a PDF).

---

## 2. What survived the research

| Claim from the brief | Verdict | Evidence |
|---|---|---|
| Commercial cleaning is the right niche | **Confirmed, strongly** | 1.26M janitorial businesses in the US (IBISWorld 2026), growing 4.3%/yr |
| They have a real, expensive revenue problem | **Confirmed** | Google Ads CPL for commercial cleaning: **$197–$230 per lead** (2026 data) |
| They already pay for solutions | **Confirmed** | Lead-gen retainers $600–$1,500/mo (email-only), $2,500–$5,000+ (with calling); The Janitorial Store membership $647/yr |
| One contract is worth real money | **Confirmed** | $400–$800/mo typical small office; $1,200–$1,800/mo for 10k sqft 3×/week; medical $0.25–0.35/sqft |
| Google Maps beats Apollo for local SMB | **Confirmed directionally** | Google Maps is the richest free source for local B2B; Google strips emails from listings, so you must follow the website link and scrape it |
| Trigger/signal targeting is the edge | **Confirmed, and it's bigger than you thought** | Signal-referencing emails: **15–25% reply** vs 3.43% average. Lists <50 recipients: 5.8% reply vs 2.1% for large sends |
| Price above $17 | **Confirmed** | Etsy commodity templates are the $15–40 floor; the $647/yr membership is the ceiling anchor |

## 3. What did not survive

| Claim from the brief | Verdict | Why |
|---|---|---|
| Cold email → landing page → Gumroad purchase | **Fails** | Real (bot-filtered) cold email CTR is **0.5–3%**. Cold-traffic product-page conversion is **1.2–2.5%**. Compounded: ~2 sales per 10,000 emails |
| "101 sales × $99" as a plan | **Fails** | That's ~500,000 emails at observed rates. Not achievable or defensible in 60 days |
| $149 flat price | **Too low for this funnel** | With a ~0.02% send-to-sale rate, every dollar of AOV matters more than every extra email |
| 30-day revenue start | **Fails** | Domain warmup alone is 2–3 weeks before meaningful volume. **Week 4 is the earliest first-dollar date** |
| ~14% of replies are useful | **Worse than assumed** | Only ~14% of replies are *positive*; 80%+ of the "replied" number in any dashboard is OOO, wrong-person, and unsubscribes |

---

## 4. The three changes that make $10k possible

### Change 1 — The CTA becomes a gift, not a link
Stop asking for a click. Ask for a **reply**, and offer something that costs you ~$0.10 to produce:

> *"I pulled 23 businesses within 12 miles of you that either just signed a new lease or opened a
> second location this quarter — with the facilities contact for each. Want me to send the list?"*

This is the single highest-leverage decision in the entire plan. It converts your outbound from
"another agency pitching me" (the thing the market is saturated with) into a give. It moves you into
the **15–25% signal-based reply band**. And critically: **the free sample *is* the product demo.**
You are not describing a system, you are handing them its output. Cost via Apify: roughly **$0.10
per prospect pack** at $1.50–$4.00 per 1,000 places. You only build packs for people who reply,
so 200 packs costs about **$20 total**.

### Change 2 — Sell on the reply thread, not the sales page
Positive replies convert at 15–30% into a purchase when a human (or a well-built assist) works the
thread. Landing pages convert cold clicks at 2%. Same person, 10× difference. The landing page's job
is credibility for people who go look you up — it is not the closer.

### Change 3 — Ladder the price; expect most revenue from the top
| Tier | Price | What it is | Expected mix |
|---|---|---|---|
| Core | **$197** | *The Walkthrough Engine* — the full system | ~60% of buyers |
| Done-With-You | **$497** | Engine + 250 trigger-matched prospects built for their metro + 45-min setup call | ~30% of buyers |
| Done-For-You | **$1,497** | We build and run their first 30-day campaign | ~10% of buyers |

**The honest projection: roughly half your $10,000 comes from 3–6 people, not from 60 downloads.**
Plan for that from day one instead of discovering it in week 7.

**The price frame that makes $197 feel free:** commercial cleaning companies pay **$197–$230 for a
single Google Ads lead**. The whole system costs less than one lead. Say exactly that on the page.

---

## 5. The revised number

| Model | 60-day gross | Verdict |
|---|---|---|
| A — brief as written (click → checkout, $149 flat) | **~$1,100** | Fails |
| B — reply-based + trigger targeting + ladder | **~$9,400** | Reaches target, tight |
| C — Model B + 4 Done-For-You sales | **~$13,000** | Reaches target with margin |

Full derivation, assumptions and kill-criteria in `03-funnel-math.md`.

**Call it what it is:** $10k in 60 days is an *aggressive but defensible* target under Model C. It
is not a forecast. The plan is built so that failure shows up in week 3 — early enough to change
course — rather than in week 8.

---

## 6. Files in this dossier

| File | What's in it |
|---|---|
| `01-market-evidence.md` | Every number I found, with sources and a confidence rating |
| `02-offer-and-product.md` | The product spec, name, ladder, positioning, sales page structure |
| `03-funnel-math.md` | Models A/B/C, sensitivity, weekly targets, kill criteria |
| `04-data-and-trigger-pipeline.md` | Apify → enrichment → verify → trigger → send, with costs |
| `05-email-sequences.md` | The actual copy, ready to load |
| `06-compliance-and-deliverability.md` | CAN-SPAM, the 2026 bulk-sender rules, infrastructure |
| `07-60-day-execution-plan.md` | Week-by-week, with owner and pass/fail gate per week |
| `08-risks-and-alternatives.md` | What kills this, and the two backup plays |
