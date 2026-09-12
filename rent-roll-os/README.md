# The Commercial Rent Roll Control Center

The internal strategy layer for the current product. Started 2026-09-12
(`../research/16-pivot-to-lease-rollover.md`).

**What we sell.** A spreadsheet system that turns a commercial rent roll into a lease-expiration
calendar and a dated action list, so a property manager knows which leases need attention before a
notice window closes.

**Who buys it.** Commercial property managers, asset managers, portfolio managers and leasing
teams at small and midsize CRE owners and third-party management firms.

**Price.** $199, one-time, flat. No launch discount, no tiers, no subscription, no setup service.

**Free front-end.** Rent Roll Lite — 10 lease rows, one expiry chart, one action list.

---

## Build order — Lite first

1. **Rent Roll Lite** (free). Days, not weeks.
2. **Test it** against 100 qualified prospects. A listening exercise, not a measurement.
3. **The paid Control Center**, only once the free one is being downloaded by real property
   managers.
4. Automation last, per `automation/stack.md`.

The unknown is not whether we can build a good spreadsheet. It is whether this buyer will trade an
email address for one. Build the cheap thing that answers that first.

---

## Files

| Path | Contents |
|---|---|
| `product/spec.md` | The six tabs, the fields, the logic, what ships |
| `offers/core.md` | The paid offer, price reasoning, what it is not |
| `offers/lite.md` | The free product and its deliberate limit |
| `outbound/icp.md` | Which companies, and the disqualifiers |
| `outbound/personas.md` | Which person, and what they actually own |

**Unchanged from the previous product and still authoritative:**
`../archive/commercial-cleaning-os/automation/` was rebuilt as the sending and orchestration layer —
see `automation/` at repo root once migrated. Distribution arithmetic lives in
`.claude/skills/building-distribution/`.

---

## The one rule this product must not break

**We organise dates and figures the user enters. We do not interpret leases.**

Every surface carries it: confirm all terms against the executed lease and qualified counsel. No
legal advice, no compliance claim, no "this protects you." A spreadsheet that implies legal
coverage is a liability wearing a product's clothes.
