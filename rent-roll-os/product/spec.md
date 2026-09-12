# Product Spec — The Commercial Rent Roll Control Center

Excel + Google Sheets + a short quick-start PDF. One download, no account, no setup service.

**Six tabs, not eight.** The promise is "you will not feel like you have to learn a system."
Every extra sheet is a tax on that promise. Four of the originally proposed tabs were four
time-based views of the same dataset; they are merged below.

---

## Tab 1 — Start Here

Five minutes to first value. Contains:

- What this does, in two sentences
- The three columns that must be filled for anything to work: **Lease expiry**, **Notice
  deadline**, **Current rent**
- How to paste from an existing rent roll without breaking formulas
- Where to set the two assumptions: fiscal year start, and the alert windows
- **The disclaimer.** Organisational and analytical tool. Confirm every term against the executed
  lease and qualified counsel.

## Tab 2 — Lease Register

The only sheet the user types into. Everything else is derived.

| Field | Notes |
|---|---|
| Property · Suite · Tenant | |
| Tenant type / industry | Feeds concentration analysis |
| SF | |
| Current rent · Rent/SF | Rent/SF calculated, not typed |
| Lease start · **Lease expiry** | Required |
| **Notice deadline** | Required. The date the product exists for. |
| Renewal option | Y/N, term, and whether the option has been exercised |
| Termination rights | Free text |
| Current status | Active · Holdover · Vacating · Renewed |
| Responsible person | |
| Renewal likelihood | High / Medium / Low — the user's judgement, not ours |
| Notes | |

**Three-state convention**, carried over from the previous product and still right: a value, or
`unknown` (looked, not findable), or empty (not looked at yet). Never a guess.

## Tab 3 — Action Now ★

**This is the product. It opens by default.**

Sorted by **notice deadline**, not by lease expiry. In commercial leasing the notice date is the
expensive, irreversible one — an option window that closes takes the renewal right with it, or
triggers an auto-renewal on terms nobody chose. Expiry is analysis; a missed notice date is money
already gone.

| Band | Trigger |
|---|---|
| 🔴 **RED** | Notice deadline within 60 days, or already passed and unactioned |
| 🟡 **YELLOW** | Notice deadline 60–180 days out |
| 🟢 **GREEN** | Beyond 180 days, or actioned |

Columns for 180 / 120 / 90 / 60 / 30-day windows sit **inside this tab** as a countdown, not as a
separate sheet.

The header states one line, calculated:

> **5 leases require action in the next 90 days · $412,000 of annual rent · 18,400 SF**

That sentence is what the buyer is paying for. Everything else supports it.

## Tab 4 — Expiry Calendar

Year-by-year, five years forward: SF expiring · rent expiring · % of portfolio SF · % of annual
rent. Bar chart beneath.

Answers "which year hurts" — the analysis that justifies the price above a plain tracker.

## Tab 5 — Exposure & Risk

Merges the originally separate rollover-exposure and tenant-risk tabs, because they answer one
question from two directions.

- Concentration by year (from Tab 4)
- Concentration by tenant — top 5 by rent and by SF
- Anchor-tenant flag
- Renewal likelihood rolled up against rent at risk
- Options and termination rights falling in each year

## Tab 6 — Renewal Pipeline

`Not Started → Research → Contact Tenant → Negotiating → Renewed` or `Backfill`.

One row per lease in play. Owner and next-action date on every active row — the same discipline as
the CRM, for the same reason: a row with no next action is not in the pipeline.

---

## What ships

| File | |
|---|---|
| `Rent-Roll-Control-Center.xlsx` | The workbook |
| Google Sheets version | Same logic, published copy-to-your-drive link |
| `Quick-Start.pdf` | 4–6 pages. Setup, the three required fields, how to read Tab 3 |

## Quality gates — non-negotiable before it sells

Learned the hard way on the previous product, where a static audit missed a formula that was
wrong in a way only evaluation caught:

1. **Every formula evaluated, not eyeballed.** The `formulas` Python library, or an equivalent.
2. **VLOOKUP/INDEX column indices checked individually.** Three off-by-ones shipped last time.
3. **Empty-state test.** Open the workbook with zero rows. Nothing may show `#DIV/0!`, `#N/A` or a
   false RED alert.
4. **Boundary test.** A notice deadline exactly 60 and exactly 180 days out lands in the right band.
5. **Past-date test.** A notice deadline that has already passed is RED, not GREEN.
6. **Google Sheets parity.** Every formula re-verified after import. `SUMPRODUCT`, date arithmetic
   and conditional formatting are the three that break.
