# Commercial Cleaning Client Acquisition OS

Working directory for the product and the revenue engine that sells it.

**Start here:** `.claude/skills/revenue-engine/SKILL.md` — the orchestrator, routing table, and the
project rules that override specialist skill guidance.
**Then:** `SKILL-DEPENDENCY-MAP.md` — which skill owns what, where they conflict, and what is missing.

## Status

| Step | State |
|---|---|
| 1. Repository inspected | done |
| 2. Installed skills inspected | done |
| 3. Named repositories identified | done — 4 of 5 verified, 1 not found |
| 4. Duplication avoided | done — 33 skills, 0 conflicts unresolved |
| 5. Directory structure verified | done |
| 6. Dependency map | done |
| 7. Master orchestration layer | done — `revenue-engine` |
| 8. Routing validated | done — 32/32 routes resolve, 0 orphans, 0 broken symlinks |
| 9a. CRM foundation | **done** — `crm/`, 5 specs |
| 9b. Sales workflows | **done** — `sales/`, 6 docs |
| 9c. Outbound layer | **done** — `outbound/`, 7 docs |
| 9d. Customer product | **done** — `../customer-product/`, 14 assets |
| 9e. Offers + stack | **done** — `offers/`, `automation/stack.md` |
| 9f. Analytics, policies, Make/Attio build | not started |

`crm/`, `sales/` and `outbound/` are specified. `automation/`, `offers/`, `analytics/` and
`policies/` remain scaffolded and empty.

**Product delivery is complete** — 13 customer assets in `../customer-product/`, audited in
`../gumroad/FINAL-ASSET-AUDIT.md`. Two manual checks remain before publishing: open both workbooks
once, and test-purchase the download.

**Revenue blocker resolved by removing it.** The service tiers were cut on 2026-09-11
(`../research/12-decision-record-v4.md`). One product, price $197, no upsell — so there is
no unbuilt purchase path left.

## Prior research

`../research/` holds the market and funnel work this project is built on — including
`11-corrections-log.md`, which corrects three arithmetic errors in the earlier dossier and takes
precedence over the files before it.

Relevant carry-over, now superseded: the funnel model in `03` and the corrections in `11` remain
the best analysis of outbound capacity. What changed is the offer. Under one product at $197,
$10,000 in 90 days is **not** a defensible target for outbound alone — see `12` for the arithmetic.
The goal is the first 10 customers, then 25, then 50.
