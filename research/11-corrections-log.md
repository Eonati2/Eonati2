# 11 — Corrections Log
**Date:** 2026-09-10 · Status changed from "decisions locked" to **provisional — audit passed, not approved**

An audit of the v2 dossier found three genuine arithmetic/logic errors of mine, five fair
calibration challenges, one place where the dossier was right and read wrong, and one challenge
that is itself too pessimistic. All of it recorded here, with the corrected numbers.

---

## A. Genuine errors — mine, now fixed

### A1. The "1.6 million sends" figure was wrong
**Was:** *"Reaching $10,000 through a click-to-checkout funnel would need roughly 1.6 million sends."*

That does not follow from Model A. Model A gives 18,000 sends → 5 sales at $149.

```
$10,000 ÷ $149            = 67 sales
67 ÷ 5                    = 13.4×
13.4 × 18,000             ≈ 241,000 sends
```

**Corrected: ~240,000 sends.** Still roughly **13× capacity**, so the conclusion — the
click-to-checkout funnel cannot reach the target — survives intact. But the number was inflated by
about 6.6×, and an inflated number in support of a correct conclusion is still a defect. Fixed in
`03` and in the artifact.

### A2. "Three-quarters of the target" contradicted the price I had just raised
**Was:** *"five implementations at $2,000 are about three-quarters of the $10,000."*

5 × $2,000 = **$10,000 gross.** That is 100% of the gross target, not 75%.

The "75%" was carried over from the earlier $1,500 price ($7,500 ÷ $10,000 = 75%) and never re-run
when the price moved to $2,000 in the same revision. Self-inflicted.

**Corrected:**

| At $2,000 × 5 | Amount | Share of $10,000 target |
|---|---|---|
| Gross | $10,000 | **100%** |
| Net after Gumroad (~12.9% + $0.80 direct card) | ~$8,706 | **87%** |

This is not a wording fix. It changes the strategy, and in the direction the audit identifies:
**five managed pilots alone clear the gross target without a single product sale.** Product revenue
is upside on top, not the base case.

### A3. "$0.20 per proof pack" was too optimistic
That figure covered a narrow Maps pull plus review and job-post scraping, and assumed permit and
registry lookups were free. It ignored email enrichment, verification, CRE data, AI classification,
and the platform compute fee that sits on top of per-event pricing.

**Corrected costing, 25–50 accounts, fully enriched:**

| Component | Cost |
|---|---|
| Maps extraction (50 places, with filters) | $0.20–$0.40 |
| Website/contact extraction | $0.25–$0.60 |
| Email enrichment | $0.30–$1.00 |
| Email verification | $0.05–$0.15 |
| Review mining | $0.10–$0.30 |
| Job-post signal | $0.10–$0.30 |
| Permit / SoS lookups | free–$0.25 |
| AI classification & angle drafting | $0.15–$0.60 |
| Platform compute overhead | $0.10–$0.30 |
| **Per pack** | **$1.50–$4.00** |
| **200 packs** | **$300–$800** (was "$40") |

Still cheap enough that the give-first mechanic holds comfortably. But "$40 for the whole campaign"
was wrong by roughly an order of magnitude, and a plan should not be built on a cost estimate that
only survives if you never actually enrich anything.

**Related change, and it improves the product:** pack size drops from "500 / 2,000 accounts" to
**25–50 exceptionally relevant accounts.** A spreadsheet showing *"31 companies with something
happening right now"* has higher perceived value than 2,000 rows, costs less to produce, and is
more honest about what the method actually finds. Fixed in `04`, `10`, and the tier definitions.

---

## B. Fair calibration challenges — accepted

### B1. The 1.26M market-size figure needed an asterisk it didn't have
US Census, NAICS 561720 (Janitorial Services): **~67,799 employer establishments** (2023). Industry
sources citing 1.2M+ are counting a far broader universe including non-employer and
registered-but-dormant entities. Different definitions, not different measurements of one thing.
*(A secondary source puts establishments near 66,471, consistent in magnitude.)*

**New standard wording:**
> The US cleaning market has a very large long tail. Census reports roughly **67,800 employer
> establishments** in NAICS 561720; industry sources cite 1.2M+ across a broader
> janitorial/cleaning universe. Because these count different things, **our addressable market is
> whatever the actual ICP scrape returns** — not a headline industry figure.

Worth noting: the dossier's own working estimate of the addressable slice was **40,000–80,000**,
which brackets the Census figure closely. The analysis was right; the headline was misleading.
Leading with the impressive number instead of the defensible one is exactly the failure mode this
dossier keeps warning about elsewhere.

### B2. 12% is an upside scenario, not a planning assumption
Accepted, and it also resolves an internal inconsistency: `03` modelled a 12% trigger-segment reply
rate while `09` planned on 1–3% positive response. Those never belonged in the same document.

**Adopted scenario ladder — reply rate:**

| Scenario | Reply rate | Use |
|---|---|---|
| Bad | 0.5% | Abort threshold |
| Conservative | 1.0% | Downside planning |
| **Base** | **2.0%** | **All financial modelling** |
| Strong | 4.0% | Upside |
| Exceptional | 8%+ | Elite case — never plan on it |

12% moves to "exceptional, unmodelled." Building a business around an elite-case result is how
plans die in month two.

### B3. The proof-pack email made an unsupported claim about a third party
**Was:** *"They don't have a cleaner locked in yet."*

I do not know that. Nobody does from the outside. It asserts a fact about a named third party's
commercial arrangements — and CAN-SPAM's one area that state law can still reach past preemption is
**falsity and deception**, with California attaching $1,000 per email.

**Replaced with what the data actually supports:**
> *"I found 23 recent commercial signals in Tampa — new locations, moves, facilities hiring and
> similar events. Want me to send the list?"*

Safer, and more credible: it describes a real method instead of claiming clairvoyance about someone
else's vendor contract. Fixed in `05`.

### B4. T5 (cleaning complaints in reviews) was over-scored at 10
The audit's reasoning holds. A review saying "the bathrooms were filthy" does not establish that the
business controls the cleaning contract, that the reviewer is an employee, that the issue is
current, or that anyone is shopping for a vendor. It's an inference about dissatisfaction, not an
observation of a purchasing window.

**Revised hierarchy — events that create a genuine buying window rank above inferred dissatisfaction:**

| Score | Triggers |
|---|---|
| **10** | New location / expansion · new facility or move · new building occupancy · new property-management assignment |
| **9** | Facilities or operations hiring · major expansion · property acquisition |
| **7** | **Negative cleaning-related reviews (was 10)** · headcount growth · funding or news |

**One refinement worth keeping rather than just demoting it:** T5's real virtue is that it is free
and abundant. It works best as a **scoring modifier stacked on a Tier-10 event** — a business that
just moved *and* has restroom complaints is a stronger row than either signal alone — rather than
as a primary trigger on its own. Fixed in `04` and `10`.

### B5. The Google Ads price anchor was over-weighted
The $197–$230 CPL is one marketing company's own campaign data, not an industry benchmark. Another
2026 source reports **$46.41** average per lead on Local Services Ads — a 4–5× spread that shows how
much the figure depends on channel. Downgraded from ⬤⬤ to ⬤ and removed from the above-the-fold
position.

**Replacement anchor, which is stronger anyway:** contract value is ⬤⬤⬤ across independent sources.
One small office account at $400–800/mo is **$4,800–$9,600 a year**. That argument doesn't depend on
anyone's ad-spend disclosure.

### B6. Gumroad Discover is not a switch you can flip
Discover eligibility requires reaching a **$100 balance from genuine sales** and passing review,
which can take around **three weeks after the threshold is hit**. So "put the cheap product on
Discover" is a month-two tactic at the earliest, not a launch-day one. The direct-sale fee framing
(**10% + $0.50 platform, plus ~2.9% + $0.30 card processing ⇒ ~12.9% + $0.80 on a direct card
transaction**) was correct but should always be stated with its components rather than as a single
opaque number.

---

## C. Where the dossier was right, and one challenge that overshoots

### C1. The mailbox capacity figure is correct — the artifact's phrasing was not
The audit computes 672/day × 60 = 40,320, or × 39 = 26,208, and finds neither matches 18,000.

`03-funnel-math.md` states the basis: **27 business days**, not calendar days.

```
60 calendar days − 21 days warmup = 39 calendar days ≈ 27 business days
27 × 672 = 18,144 ≈ 18,000  ✓
```

The dossier is internally consistent. The **artifact compressed this to "in a 60-day window"** and
dropped the business-days basis, which is what produced the discrepancy on reading. That's a real
communication defect and it's fixed — but the underlying model does not need re-deriving.

### C2. "Even 750 isn't enough to distinguish 1% from 3%" is too pessimistic
At n=750: 1% → ~7.5 expected positives; 3% → ~22.5. Those distributions barely overlap; 750 does
separate them at any reasonable confidence. The claim overstates the problem.

**But the audit's practical point is better than my statistical one, and I'm adopting it:** you do
not need academic significance to launch. You need evidence that strangers engage and pay. A
100-prospect qualitative pass answers questions a 750-prospect rate estimate cannot — *do they
understand the offer, which trigger draws attention, what objection recurs, do they ask "can you
just do this for me?"* I under-weighted that.

**Adopted sequence:**

| Test | Size | Question it answers |
|---|---|---|
| 1 | **100**, hand-picked | Qualitative. Do owners get it? What objection? Do they want the pack? |
| 2 | **300–500**, after message revision | Directional rate + first conversions |
| 3 | **1,000+** | Only after downstream conversion data exists |

Note for honesty: Test 1 will produce ~2 positive replies at base case. **That is a listening
exercise, not a measurement** — and it must be labelled as such in the plan, or a thin result will
be misread as failure. Fixed in `07`/`09`.

---

## D. The legal section, rewritten

The old framing — *"landline = DNC-exempt, mobile = treated as residential"* — was too categorical,
and it also missed a change that post-dates it.

**The FTC amended the TSR in March 2024, effective 16 May 2024** (recordkeeping compliance from
15 October 2024). The amendment **extends the TSR to business-to-business telemarketing**,
prohibiting material misrepresentations and false or misleading statements made to induce payment,
and **expands recordkeeping** — call detail records, seller-relationship records, and DNC-compliance
records.

So the accurate picture is layered, not a rule of thumb:

| Layer | What it does |
|---|---|
| **FTC DNC provisions** | Most B2B solicitation calls remain exempt — *except* sellers of nondurable office or cleaning supplies |
| **FTC TSR, as amended 2024** | **Now reaches B2B** for misrepresentation, and imposes recordkeeping |
| **TCPA / FCC** | Separate regime. Restricts autodialed and artificial/prerecorded calls to wireless numbers absent required consent |
| **State law** | Mini-TCPA statutes stack on top, with their own consent and window rules |

**Shipping language, replacing the old rule of thumb:**
> Phone outreach is a separate legal workstream, not a setting. Before dialling: classify the
> number, determine which federal and state rules apply, keep suppression and call records, and
> prohibit automated or prerecorded outreach unless counsel has confirmed the legal basis.

That is what goes in the product too. Teaching customers "landline safe / mobile illegal" would be
handing them a false sense of a bright line where there isn't one.

---

## E. The business-model inversion — accepted, and it is the most important change here

> **We are not building a $197 Gumroad product and hoping outbound sells it. We are building a
> $2,000 managed acquisition service first, and using the first five customers to manufacture the
> $197 product.**

This follows directly from A2. Five managed pilots clear the gross target on their own. And it
inverts the build order correctly: you cannot write a good product about a process you have not run
for someone else, under their constraints, in their metro, with their objections in the room.

**Revised ladder, with the naming the audit proposed — it is clearer than mine:**

| Price | Name | Promise |
|---|---|---|
| $197 | **The OS** | *You get the machine.* |
| $497 | **Setup** | *We install the machine with you.* |
| $2,000 | **Managed Pilot** | *We run your first 30 days.* — **5 founding places, capped** |

"Managed Pilot" beats "done-for-you": it says what happens, it implies a defined end, and the cap
is genuine capacity scarcity rather than a marketing device.

**And the product's real definition, which protects it if email underperforms:**

> **Signal → Account → Contact → Conversation → Walkthrough.**

Email is one delivery channel. Phone, LinkedIn, direct mail and manual follow-up are others. The
intellectual property is the answer to *"who should I pursue right now, and why?"* — not an email
sequencer.

---

## F. Kill / Continue sheet

Internal decision thresholds. **Not industry laws** — ours, chosen deliberately, to be revised when
real data replaces them.

| Metric | Kill / change | Continue |
|---|---|---|
| Delivery rate | <90% | ≥95% |
| Total reply rate | <1% | ≥2% |
| Positive reply rate | <0.5% | ≥1.5–2% |
| Proof packs requested | sporadic | consistent |
| Pack → sales conversation | <10% | ≥20% |
| Sales conversation → paid | <10% | ≥20% |
| First Managed Pilot sale | none after a meaningful test | ≥1 |
| *"Can you just do this for me?"* | rare | recurring |

The last row is the one to watch hardest. It is unquantified on purpose, and it is the leading
indicator for the model that actually reaches $10,000.

---

## G. Status

**Provisional. Not locked.** Outstanding before anything is built or sent:

1. Counsel review of the phone workstream, including the TSR cleaning-supplies carve-out.
2. A spreadsheet-level unit-economics audit of `03` — the errors in A1 and A3 were both found by
   arithmetic, and there may be more where they came from.
3. The DFW scrape-and-qualify pass, which resolves the addressable-market question empirically
   instead of by citation.

---

## H. Added 2026-09-11 — a conclusion of mine that did not survive research

### H1. Record 12 named marketplace traffic as a possible gap-closer. It is not one.

**Was** (`12`, "What this means, stated plainly"): *"It becomes reachable only if the free product,
organic distribution and Gumroad's own marketplace traffic carry a meaningful share."*

Marketplace placement follows sales history; it does not produce the first sales. For a seller with
no history and no audience the causality runs the wrong way. **Planning treatment is now zero.**

Two gap-closers remain, and they are one mechanism described twice: organic distribution's job is
to produce free-product downloads. There is no passive route.

This was not an arithmetic error — the sentence in `12` was appropriately hedged. It was an
unresearched assumption presented alongside two others as if all three were comparable, when one of
them was structurally unavailable to us. Recorded in full in `research/14-distribution-gap.md`.
