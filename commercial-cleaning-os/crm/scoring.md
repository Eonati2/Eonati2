# Scoring

**The score is a prioritization aid, not a truth claim.** It ranks what to work on next. It does not
predict whether an account will buy, and it must never be shown to a prospect or used as evidence of
anything about their business.

Total = **20 points** across five dimensions.

| Dimension | Range | Answers |
|---|---|---|
| ICP Fit | 0–5 | Is this the kind of account we should pursue? |
| Commercial Value | 0–5 | Is it worth the effort if we win it? |
| Trigger Strength | 0–5 | Is there a credible reason to reach out *now*? |
| Decision-Maker Access | 0–3 | Can we actually reach someone who decides? |
| Serviceability | 0–2 | Could we (or the customer) actually service it? |

### Bands

| Total | Band | Action |
|---|---|---|
| 16–20 | **Priority** | Work now. Personalized outreach, human-written. |
| 12–15 | **Active** | Work in sequence. Standard treatment. |
| 8–11 | **Nurture / Research** | Do not contact yet. Fill the gaps or set a review date. |
| 0–7 | **Park / Disqualify** | Stop spending time. Disqualify with a reason code. |

**Never contact below 8.** Not because the account is worthless, but because contacting it costs a
send against a domain-reputation budget and returns close to nothing. Scarcity of sending capacity
is what makes the floor real.

---

## 1. ICP Fit (0–5)

### Instance B — facilities (the customer's targets)
| Pts | Criteria |
|---|---|
| 5 | Target segment, right size band, local decision-making confirmed |
| 4 | Target segment, right size band, decision locus unconfirmed |
| 3 | Adjacent segment, plausible fit |
| 2 | Segment fits, size marginal |
| 1 | Weak fit, pursued only as filler |
| 0 | Not ICP → `Disqualified` |

Segment priority: property management → office / professional → medical (where properly qualified)
→ industrial / light industrial → retail / commercial.

### Instance A — cleaning companies (our buyers)
| Pts | Criteria |
|---|---|
| 5 | 3–25 staff, website with a commercial services page, independent, named owner |
| 4 | Same but staff count inferred rather than confirmed |
| 3 | Commercial focus unclear from the site |
| 2 | Mostly residential, some commercial |
| 1 | Residential-only with commercial ambition stated |
| 0 | Franchise, national FM, solo residential, or dormant → `Disqualified` |

**Franchises score 0** — the local owner usually does not control marketing.

---

## 2. Commercial Value (0–5)

### Instance B
Estimated monthly contract value, from square footage × segment rate. Estimates are **estimates** —
store the input, not just the output, and mark the field `estimated`.

| Pts | Est. monthly value |
|---|---|
| 5 | $2,000+ or a multi-building relationship |
| 4 | $1,000–$1,999 |
| 3 | $600–$999 |
| 2 | $300–$599 |
| 1 | Under $300 |
| 0 | Unknown and not estimable |

A property-management account scores on **portfolio potential**, not the first building. That is the
whole reason it ranks first in segment priority.

### Instance A
| Pts | Signal |
|---|---|
| 5 | Clear capacity and intent to grow commercial — hiring, fleet, multiple crews |
| 3–4 | Established, stable, no visible growth signal |
| 1–2 | Very small, capacity to service new contracts doubtful |
| 0 | No evidence of commercial capability |

---

## 3. Trigger Strength (0–5) — **this overrides the `trigger-finder` default weighting**

Per `revenue-engine` §5, facility events outrank inferred dissatisfaction and generic growth.

| Pts | Tier | Triggers |
|---|---|---|
| **5** | High | New location · new facility · move or new occupancy · relevant property-management change |
| **3** | Medium | Facilities or operations hiring · renovation or reopening · acquisition |
| **1** | Low | Generic growth · funding · generic hiring · weak review signals |
| **0** | None | No credible event, or the event is undated / unsourced |

### Modifiers
| Adj. | Condition |
|---|---|
| **+1** | A second independent trigger fires (capped at 5 total) |
| **+1** | `freshness_days ≤ 30` |
| **−2** | `freshness_days` exceeds the trigger's window |
| **→ 0** | `trigger_source` or `trigger_date` missing (schema R3) |

### Freshness windows
New location 120d · new facility / occupancy 90d · move 90d · property-management change 90d ·
facilities hiring 90d · renovation / reopening 60d · acquisition 120d · generic signals 60d.

### The rule that matters most
**A trigger is an event, not a conclusion.** A high score means *there is a credible reason to make
contact now*. It does **not** mean the account has no cleaner, is unhappy with one, is shopping, or
is available. Never write or imply any of those without direct evidence.

An unsourced or undated trigger scores **zero**, however compelling it sounds. That rule exists
because unsourced triggers are precisely how fabricated claims enter outreach copy.

---

## 4. Decision-Maker Access (0–3)

| Pts | State |
|---|---|
| 3 | Named individual, correct role, **verified** business email |
| 2 | Named individual, correct role, email unverified or pattern-guessed |
| 1 | Role identified but no name, or a generic inbox only |
| 0 | No route to anyone who decides |

**A CRM title does not make someone a decision-maker.** Score 3 only when the role plausibly owns
the cleaning vendor relationship for that facility type — for a medical office that is usually the
practice or office manager, not the physician.

An `unverified:` email caps this at 2 and **may not be used in outreach** (schema §5).

---

## 5. Serviceability (0–2)

| Pts | State |
|---|---|
| 2 | Within service area, scope matches capability, no disqualifying requirement |
| 1 | Serviceable with a stretch — distance, timing, or a specialist requirement |
| 0 | Not serviceable → `Disqualified` |

Cheap to assess and it prevents the most demoralizing failure mode: winning a walkthrough for
something you cannot actually service.

---

## 6. Negative scoring — hard overrides

`revops` is right that a model without negative scoring lets bad records through. These are not
deductions; they **force an outcome** regardless of total.

| Condition | Effect |
|---|---|
| On the Suppression list | → `Disqualified`, no contact, ever |
| `opt_out = true` | → `Disqualified` |
| Hard bounce | Contact invalid; account back to `Researching` |
| Out of business / listing closed | → `Disqualified` |
| Duplicate of an existing account | → `Disqualified`, merge via `crm-duplicate-detector` |
| Franchise (Instance A) or chain deciding centrally (Instance B) | → `Disqualified` |
| Competitor | → `Disqualified` |

---

## 7. Worked example

*Instance B — a dental group in Irving, DFW.*

| Dimension | Score | Basis |
|---|---|---|
| ICP Fit | 4 | Medical segment, right size; decision locus unconfirmed |
| Commercial Value | 3 | ~4,200 sqft × medical rate → **estimated** $600–$800/mo |
| Trigger Strength | 5 | New occupancy, 26 days ago. Source: GBP listing created 2026-08-14. +1 fresh, +0 second trigger → capped at 5 |
| DM Access | 2 | "Practice Manager" named on the site; email pattern-guessed, not verified |
| Serviceability | 2 | In area, standard scope |
| **Total** | **16** | **Priority** |

**What the 16 licenses:** work this account now, and write to the observed fact — *"saw you opened
on MacArthur last month"*. **What it does not license:** any claim about their current cleaner.

**The one action that would improve it:** verify the practice manager's email. DM Access 2 → 3,
total 17, and the account becomes contactable rather than research-only.

---

## 8. Calibration

The weights are **assumptions**, chosen for face validity, not derived from outcome data — we have
none yet.

**Recalibrate after the first 20 closed accounts** (won or lost) in either instance. Compare score
band against outcome. If Priority converts no better than Active, the model is decorative and the
weights need to change.

Until then, treat the bands as a **work-ordering heuristic** and say so in any report that cites
them. Do not present score bands as conversion likelihood — internally or to a customer.
