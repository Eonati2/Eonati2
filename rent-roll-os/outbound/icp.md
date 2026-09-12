# ICP — Which Companies

**Who this is for:** organisations that manage commercial leases where a missed notice date costs
real money, and that currently run the tracking in a spreadsheet.

---

## Qualifying

| Filter | Threshold | Why |
|---|---|---|
| Geography | United States | Lease conventions, notice-period norms, and our compliance posture |
| Asset class | Office · retail · industrial · flex · mixed-use | Multi-tenant commercial with dated notice provisions |
| Portfolio size | **~5 to ~150 leases** | The band where the problem is real and software has not been bought |
| Firm type | Owner-operators · third-party property management · small asset managers · family offices with direct CRE | |
| Current tooling | Excel or Google Sheets for lease dates | **The single strongest qualifier.** Stated in a job ad, a forum post, a role description, or found by asking |

## Disqualifying

| Signal | Why |
|---|---|
| Already running Visual Lease, MRI, Yardi Voyager, Prophia or equivalent | The problem is solved. A $199 spreadsheet is a downgrade, not an upgrade. |
| Under ~5 leases | The spreadsheet they already have is adequate and they know it |
| Over ~150 leases | They have bought software, or they are about to and it is not us |
| Residential-only property management | Different document, different dates, different buyer |
| Single-tenant NNN only | One expiry date per asset. A calendar reminder covers it. |
| Brokerage with no management arm | They transact; they do not administer |

---

## The band is the whole point

Below five leases there is no pain. Above roughly 150 the buyer has already been sold
**lease administration software** — a category whose vendors pay **$532.81 per click** on that
term. We are not competing with them and must not try.

**Our position is the step before that purchase:** the spreadsheet you run until the portfolio is
big enough to justify a system. Said plainly, that is also honest — and a buyer who outgrows us
and buys software was never ours to keep.

---

## How we find them

| Source | Use |
|---|---|
| **Apollo** | Companies by SIC/NAICS for real-estate management, filtered by headcount; contacts by title |
| **Apify** | Public company-site collection — portfolio pages, property lists, team pages. **Public data only, nothing behind authentication.** |
| **BOMA / IREM local chapter member directories** | Where published publicly. Verify the terms of use before collecting anything. |
| Public property records | Owner entities behind multi-tenant assets |

**Data rules, unchanged:** only data we are permitted to use · source and date on every field ·
never scrape behind authentication · never infer a missing value — mark it `unknown`.

**Portfolio size is usually not published.** It is the most important qualifier and the hardest to
get. Treat it as `unknown` and let the first email ask, rather than guessing and being wrong in
the opening line.
