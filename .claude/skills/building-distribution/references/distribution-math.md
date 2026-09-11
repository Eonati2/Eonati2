# Distribution Math

How to rebuild the requirement table in `SKILL.md` §2, what each number depends on, and what would
have to be true for the plan to work.

## Contents

1. [The equation](#1-the-equation)
2. [Where each input comes from](#2-where-each-input-comes-from)
3. [Recomputation procedure](#3-recomputation-procedure)
4. [Sensitivity — which input matters most](#4-sensitivity--which-input-matters-most)
5. [What would have to be true](#5-what-would-have-to-be-true)
6. [Common errors in this calculation](#6-common-errors-in-this-calculation)

---

## 1. The equation

```
sales_needed        = ceil(revenue_target / price)
outbound_sales      = outbound_capacity × contact_purchase_rate
list_sales          = sales_needed − outbound_sales
subscribers_needed  = list_sales / list_purchase_rate
downloads_per_day   = subscribers_needed / days_in_window
```

Run it twice — once with the optimistic rate on both assumptions, once with the pessimistic rate on
both — and report the pair as a band. Never report a single figure; a single figure from two
unmeasured rates is a false precision.

## 2. Where each input comes from

| Input | Current | Source | Type |
|---|---|---|---|
| `revenue_target` | $10,000 | User-set | Decision |
| `price` | **$197** | Locked 2026-09-11 | Decision, **resolved** |
| `outbound_capacity` | **3,000 contacts / 90 days** | Instantly Growth's 1,000 uploaded contacts/month, in `commercial-cleaning-os/automation/stack.md` | **Structural** — effort cannot raise it; only a plan upgrade can |
| `contact_purchase_rate` | 0.25%–0.5% | Nothing. We have never run a campaign. | **Assumption** |
| `list_purchase_rate` | 1%–3% | Floor of the 1–5% published email conversion band; discounted because our list will be cold-sourced, not audience-grown | **Assumption** |
| `days_in_window` | 90 | `research/13-90-day-blueprint.md` | Decision |

Two of the six are assumptions, and they are the two the whole answer swings on. That is the honest
state of this calculation. Every output carries that caveat.

## 3. Recomputation procedure

Trigger a rebuild whenever any of these happen:

- The price is decided, or changed.
- The revenue target is changed.
- Mailbox count, sending capacity, or the Instantly plan changes.
- Any rate moves from assumption to measurement — that is, **n ≥ 100** in the denominator.
- The window shortens because time passed. This one is silent and easy to miss: recompute
  `downloads_per_day` against *remaining* days, not the original 90, at every monthly review.

Steps:

1. Restate all six inputs with their current values and their type (decision / structural /
   assumption / measurement).
2. Run the equation at both ends of every assumption band.
3. Compare `downloads_per_day` against what the live channels actually produced last week.
4. If required exceeds actual by more than 2×, the gap is not closeable by effort in current
   channels. Say so, and name what would close it.
5. Replace the table in `SKILL.md` §2. Do not leave a stale table beside a new one.

## 4. Sensitivity — which input matters most

Holding everything else at the midpoint, moving one input:

| Change | Effect on subscribers needed |
|---|---|
| ~~Price $149 → $197~~ | **Taken.** Locked at $197 on 2026-09-11. It was the largest single lever and it has been pulled. |
| Instantly Growth → Hypergrowth (capacity 3,000 → 6,800) | Falls by roughly half, for $50/mo on the plan plus ~$119/mo in extra mailboxes. **Now the largest remaining lever, and it costs money.** |
| `list_purchase_rate` 1% → 3% | Falls by two-thirds. Not a lever we control directly; it is an outcome of list quality. |
| `outbound_capacity` +50% | Falls modestly. Outbound is a small fraction of the requirement at either rate. |
| Revenue target $10k → $12k | Rises roughly 20–25%. |
| Window 90 → 120 days | Subscribers needed unchanged; per-day rate falls 25%. |

The ranking is the point, and it has changed. **Price was the strongest lever and it has been
pulled** — $197 roughly halved the audience that has to be built, though whatever conversion
penalty the higher price carries is itself unmeasured and will only show up in the data.

**What remains is more expensive.** Raising outbound capacity now means an Instantly plan upgrade
plus more mailboxes — real money, spent before anything is validated. The free lever is gone; the
next one has a price tag. That is the argument for treating list growth as the priority rather
than buying capacity.

## 5. What would have to be true

For $10,000 gross at $197 inside 90 days, all of these at once:

1. Outbound runs at full capacity — 3,000 contacts actually reached, not planned.
2. Contact → purchase lands at the top of the assumed band, 0.5%.
3. Between 1,200 and 4,300 qualified people download the free kit.
4. List → purchase lands at or above 1%.
5. None of the compliance, deliverability or domain-reputation risks in
   `research/06-compliance-and-deliverability.md` materialise.

Item 3 is the one without a mechanism. Items 1, 2, 4 and 5 are risks. Item 3 is an absence. A plan
with four risks and one absence is not a plan with five risks — the absence has to be filled before
the risks are worth managing.

At 13–48 qualified downloads a day, every day, for ninety days: no channel currently running
produces any of them.

## 6. Common errors in this calculation

- **Netting and grossing confused.** Platform fees take roughly a tenth. A $10,000 net target needs
  a gross target near $11,100 entered at the top. State which one is meant, every time.
- **Counting outbound sales and outbound-sourced subscribers twice.** A contact who downloads the
  kit and later buys is one person. Either model them as an outbound sale or as a subscriber — not
  both. The table in §2 models outbound purchases directly and assumes all *additional* subscribers
  come from other channels.
- **Averaging the band.** "About 2,700 downloads" hides that the answer is anywhere from 1,200 to
  4,300 depending on two rates nobody has measured. Report the band.
- **Treating a raised target as a raised capability.** Changing `revenue_target` changes only the
  requirement. Nothing else in the equation moves.
- **Quoting last month's table.** Inputs change. A table is a snapshot of a calculation, not a fact.
