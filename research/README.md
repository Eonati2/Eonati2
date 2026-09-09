# Commercial Cleaning × Gumroad × Outbound — Research Dossier

Research and strategy for a Gumroad digital product sold to US commercial cleaning companies via
trigger-based outbound email. Target: $10,000 gross in 30–60 days.

**Read `00-EXECUTIVE-BRIEF.md` first.** It contains the verdict and the three changes that make the
target reachable.

| File | Contents |
|---|---|
| `00-EXECUTIVE-BRIEF.md` | The verdict, what survived research, what didn't, the revised number |
| `01-market-evidence.md` | Every verified figure with source and confidence rating — plus what I could not verify |
| `02-offer-and-product.md` | ICP, product name, positioning, full product spec, price ladder, sales page structure |
| `03-funnel-math.md` | Models A/B/C, capacity constraint, sensitivity analysis, cost model, kill criteria |
| `04-data-and-trigger-pipeline.md` | The 11-trigger board, both data pipelines, architecture, build order |
| `05-email-sequences.md` | Four complete sequences, ready to load, plus subject bank and test plan |
| `06-compliance-and-deliverability.md` | CAN-SPAM, 2026 bulk-sender rules, domain architecture |
| `07-60-day-execution-plan.md` | Week by week, with a pass/fail gate on each week |
| `08-risks-and-alternatives.md` | Ranked risks, Plan B, Plan C, and the most likely failure mode |
| `09-decision-record-v2.md` | **Locked decisions, and four corrections where the revised plan and the math still disagree** |
| `10-dfw-pilot-pack-spec.md` | **The first buildable thing: 150 DFW accounts, schema, queries, scoring, ~27 hours** |

---

## The three sentences that matter

1. **The niche is right; the funnel in the original brief is not.** Cold email → click → Gumroad
   checkout produces roughly **$745**, not $10,000 — because real cold-email CTR is 0.5–3% and
   cold-traffic page conversion is ~2%, and multiplying them gives ~2 sales per 10,000 emails.
2. **Ask for a reply, not a click, and make the first ask a gift** — a free pack of ~23 businesses in
   the prospect's own city that have a reason to switch cleaners this quarter. It costs $0.20 to
   produce, only gets built for people who reply, and it *is* the product demo.
3. **About half the revenue will come from 4–6 people paying $497–$1,497**, not from sixty people
   paying $197. Build the whole funnel around those few.

## v2 — what changed

Timeline locked at **90 days**. Product renamed **Commercial Cleaning Client Acquisition OS** and
recategorised from lead generation to **contract acquisition**. Architecture flipped to
**accounts-first, people second**. **Phone added** alongside email. Pilot geography **Dallas–Fort
Worth**. Modelling assumption tightened to **1–3% positive response**.

Four corrections carried in `09`:

1. **Phone brings the TCPA** — $500–$1,500 per call, and Maps data is mostly mobile numbers, which
   are not DNC-exempt. Manual dialling and line-type classification become mandatory.
2. **A 100–200 prospect validation sample cannot distinguish a 1% offer from a 3% one** — the exact
   question it exists to answer. Raise it to 500–750.
3. **The $49 tier converts your scarcest resource (a positive reply) into $43.** Move it to Gumroad
   Discover; keep it out of the outbound funnel.
4. **DFW cannot be both the account geography and the sales territory.** It's the pilot pack and the
   demo; sell into 10–15 metros and build each buyer a pack for their own city.

And the conclusion the conservative assumption forces: **the five done-for-you clients are ~70–75%
of the $10,000**, not a side experiment. Price them at $2,000 and sell them deliberately.

## Status

Research complete, decisions locked. Nothing built, bought, or sent. Next action is the DFW pilot
pack in `10` — three days and about $20, and it tests the trigger thesis before a single domain is
warmed.
