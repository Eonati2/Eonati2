# 10 — DFW Pilot Pack: Build Spec

The first thing to build, by hand, before any automation. It is simultaneously the **pilot**, the
**public demo**, the **product's first deliverable**, and the **thing that proves the method works**.

**Target:** 150 qualified DFW commercial accounts, trigger-scored, with decision-maker role
identified. Build time by hand: 2–3 days. Do not automate until this exists.

---

## 1. Scope

**Geography:** Dallas–Fort Worth metroplex. Core: Dallas, Fort Worth, Plano, Irving, Arlington,
Frisco, Richardson, Garland, Addison, Las Colinas, Grapevine, Lewisville, McKinney.

**These are the accounts a cleaning company would pursue — not cleaning companies themselves.**

| Tier | Account type | Target count | Why this rank |
|---|---|---|---|
| 1 | Property management companies | 30 | One relationship can expose multiple buildings |
| 2 | Medical / dental / outpatient | 40 | Highest rate per sqft ($0.25–0.35), compliance-driven, non-negotiable frequency |
| 3 | Professional office / office buildings | 45 | Largest addressable pool |
| 4 | Warehouse / light industrial | 20 | Larger contracts, more specialised |
| 5 | Schools, daycares, gyms, places of worship | 15 | Stable, less contested, $300–1,500/mo |

---

## 2. Row schema

Every row in the pack carries all of this. A row missing the trigger or the decision-maker role is
not a row — it's a directory entry, and directory entries are free everywhere.

| Field | Example | Source |
|---|---|---|
| `account_name` | Legacy Dental Partners | Maps |
| `tier` | 2 — Medical | assigned |
| `address` / `city` / `zip` | 5910 N MacArthur Blvd, Irving 75039 | Maps |
| `facility_type` | Multi-operatory dental, single floor | Maps + site |
| `est_sqft` | ~4,200 | site / listing / footprint estimate |
| `est_monthly_value` | $580–$760 | sqft × tier rate (see `01 §C`) |
| `website` | — | Maps |
| `decision_maker_role` | Practice Manager | tier playbook |
| `decision_maker_name` | — | site / GBP replies / SoS / LinkedIn |
| `contact_channel` | landline verified / wireless / email only | **line-type lookup — see §5** |
| `trigger_id` | T1 | trigger board |
| `trigger_evidence` | *"New location opened Aug 2026"* — GBP listing created 2026-08-14 | logged verbatim |
| `trigger_date` | 2026-08-14 | |
| `freshness_days` | 26 | computed |
| `score` | 11 | scoring rule below |
| `outreach_angle` | *"Saw you opened the MacArthur location — is nightly janitorial sorted there yet?"* | written per row |

**The two fields that make this a product rather than a list:** `trigger_evidence` (verbatim, with
its date) and `outreach_angle` (written, not templated). Those are the two you cannot buy from a
data vendor and cannot get from a free blog post.

---

## 3. Discovery queries

Run per city, per tier. Apify Google Maps, ~$4/1,000 places.

```
TIER 1  property management company · commercial property management ·
        real estate management · HOA management company
TIER 2  dental office · medical clinic · outpatient clinic · urgent care ·
        physical therapy · dermatology · veterinary clinic · surgical center
TIER 3  office building · law firm · accounting firm · insurance agency ·
        financial advisor · coworking space · title company
TIER 4  warehouse · distribution center · light manufacturing ·
        fulfillment center · self storage facility
TIER 5  daycare · private school · charter school · gym · fitness center ·
        church · community center
```

Expected raw: ~4,000–5,000 places across 13 cities. Cost: **~$18**.

---

## 4. Qualification

Apply in order. Cheapest, most-eliminating filter first.

| # | Rule | Drop if |
|---|---|---|
| 1 | Physical commercial premises | Home-based, virtual office, PO box, service-area-only listing |
| 2 | Size floor | Under ~1,500 sqft — contract too small to be worth a walkthrough |
| 3 | Size ceiling | National chain or corporate campus — cleaning is contracted at HQ, not locally |
| 4 | Active | No reviews or updates in 12 months |
| 5 | Not self-cleaning | Restaurants and retail with in-house closing crews (unless a specialty trigger fires) |
| 6 | Reachable | No website *and* no phone |

**Expected yield: ~4,500 raw → ~1,100 qualified → top 150 by score.**

The 150 is not the top 150 businesses. It is the top 150 **by trigger score** — which is the whole
argument. A pack of the 150 biggest offices in Dallas is worth nothing; anyone can build it. A pack
of the 150 with the freshest reason to change vendors is the product.

---

## 5. Contact channel classification — do this before any dialling

Every row gets `contact_channel` set before it reaches a phone script.

| Value | Meaning | Treatment |
|---|---|---|
| `landline_verified` | Line-type lookup returns landline | DNC-exempt B2B call. Manual dial, business hours. |
| `wireless` | Lookup returns mobile | **Treated as residential under the TCPA.** Manual dial only, 8am–9pm local, no autodialer, no prerecorded or AI voice. |
| `unknown` | Lookup inconclusive | Treat as `wireless` |
| `email_only` | No usable number | Email sequence only |

Line-type lookup costs fractions of a cent per number. The exposure it prevents is **$500–$1,500 per
call**, with a private right of action and state statutes stacked on top. This is the highest
return-on-effort step in the entire build. See `06 §3`.

---

## 6. Scoring

```
score = base_trigger_score              (7–10, from the trigger board in `04`)
      + 2   if a second trigger fires
      + 2   if freshness_days <= 30
      + 1   if decision_maker_name is known
      + 1   if est_monthly_value >= $800
      − 3   if freshness_days > trigger's window
```

**Include at 9+. Nurture 6–8. Cut below 6.**

Sort the delivered pack by `freshness_days` ascending, not by score — the customer should work the
list top-down and the freshest windows close first. Say so in the pack's header row.

---

## 7. Decision-maker role, by tier

Who actually signs. Getting this wrong wastes the trigger.

| Tier | Signs the contract | Reach them via |
|---|---|---|
| 1 · Property mgmt | Property Manager; Portfolio Manager for multi-site | Company site team page; the manager is usually named on the building listing |
| 2 · Medical | Practice Manager or Office Manager — **rarely the physician** | Site staff page; GBP review replies |
| 3 · Office | Office Manager under ~50 staff; Facilities Manager above | LinkedIn; front desk will name them if asked plainly |
| 4 · Industrial | Operations Manager or Plant Manager | Site; Indeed postings name the reporting line |
| 5 · Schools/gyms | Director, Administrator, or Business Manager | Site; public board minutes for schools |

**The single most common mistake in this industry:** pitching the owner or physician when the office
manager holds the vendor relationship and the budget. Tier 2 is where this costs the most.

---

## 8. Build sequence

| Step | Output | Time |
|---|---|---|
| 1 | Scrape all five tiers across 13 cities | 2h (mostly waiting) |
| 2 | Apply the six qualification rules | 3h |
| 3 | Assign tier, estimate sqft and monthly value | 3h |
| 4 | **Trigger hunt** — the real work. T5 review-mining and T1/T2 GBP diffs first; they're free and highest-scoring | 8h |
| 5 | Decision-maker role + name where findable | 4h |
| 6 | Line-type classification on every number | 30m |
| 7 | Score, sort, write the outreach angle per row | 4h |
| 8 | Format as the delivered pack | 2h |

**~27 hours.** That is the honest cost of the first one. The second takes half as long, the fifth
takes a quarter, and only then is it worth automating — because by then you know what a good row
looks like, which is a judgment no workflow can hold for you.

---

## 9. What the pilot pack is for

1. **Proof on the sales page.** Eight rows shown, names redacted. The *shape* of the data sells.
2. **The free sample in outbound.** DFW cleaning companies get the real thing; everyone else gets a
   pack for their own metro, built on reply.
3. **Your own validation.** If you cannot find 150 accounts in DFW with a live, dated, evidenced
   reason to change cleaners, the trigger thesis fails here — at a cost of three days and $20,
   before any domain is warmed or any product is written.
4. **The template.** Every subsequent metro is this document with different queries.

**Kill criterion:** fewer than **60 accounts scoring 9+** out of ~1,100 qualified. That would mean
triggers are too rare in a metro of this size to build a business on, and the plan goes to
`08 §2` Plan B.
