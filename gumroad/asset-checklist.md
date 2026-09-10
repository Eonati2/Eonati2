# Asset Checklist — publish gate

**The page describes ten documents. All ten exist as internal drafts. None has been rewritten or
packaged for a customer.** Nothing publishes until this file is all-green.

The rule that produced this file is the same one applied to outbound copy: **do not claim what
cannot be evidenced.** Applied to a product, that means the sales page may not list an asset that
does not ship.

---

## 1. Named on the page — must exist at publish

| # | Asset | Source | Status |
|---|---|---|---|
| 1 | Trigger Library | `outbound/triggers.md` | **Draft** — needs customer rewrite |
| 2 | Qualification framework | `outbound/icp.md` §Instance B | **Draft** — extract, drop Instance A |
| 3 | Decision-maker map | `outbound/personas.md` §Instance B | **Draft** — extract |
| 4 | Outreach sequences | `outbound/sequences/instance-b.md` | **Draft** — passed copy review 2026-09-10 |
| 5 | Follow-up system | `sales/05-follow-up-cadence.md` | **Draft** |
| 6 | Reply-handling guide | `outbound/reply-routing.md` | **Draft** — strip Instance A objection codes |
| 7 | Discovery framework | `sales/01-discovery.md` | **Draft** |
| 8 | Walkthrough checklist | `sales/02-walkthrough.md` | **Draft** |
| 9 | Proposal structure | `sales/03-proposal.md` | **Draft** |
| 10 | Pipeline system | `crm/lifecycle-stages.md` + `scoring.md` + `field-definitions.md` | **Draft** — heavy rewrite; written as a spec, not a user guide |

Ten listed documents from twelve source files, because the pipeline system is currently three.

## 2. Requested but does NOT exist — removed from the page

| Asset | Status | Decision |
|---|---|---|
| **Account & Trigger Tracker** | Not built | **Cut from the page.** Add back when a working spreadsheet exists |
| **Automation blueprint** | `automation/` is empty | **Cut.** The FAQ says automation is optional, which is now true rather than a dodge |
| **30-day implementation plan** | Not written | **Cut.** Cheap to write, and it would strengthen the page |
| **Metrics / scoreboard** | Not built | **Cut** |
| **Main OS manual** | No assembled document | **Cut as a separate item.** The ten documents are the product |

**These four are the highest-value additions available.** The Tracker especially — it's the one
asset that turns ten documents into something that runs, and it's a spreadsheet, not a rewrite.

## 3. Must NEVER ship

Instance A content is our own commercial material. Shipping it would hand a buyer our funnel math,
our pricing logic and our internal doubts.

| File | Why |
|---|---|
| `sales/06-selling-the-managed-pilot.md` | Our pilot sales motion, including objection handling aimed at them |
| `outbound/sequences/instance-a.md` | Our sequences, aimed at cleaning companies |
| `outbound/sequences/REVIEW-2026-09-10.md` | Internal copy review |
| `SKILL-DEPENDENCY-MAP.md`, all of `research/` | Internal |
| Instance A sections inside shared files | Must be stripped in extraction, not just skipped |

**Item four is the real risk.** `icp.md`, `personas.md` and `reply-routing.md` each contain both
instances in one file. Extraction has to remove the Instance A halves, not merely ignore them — a
copy-paste that leaves them in ships our targeting of the buyer to the buyer.

## 4. Packaging

| Item | Status |
|---|---|
| Rewrite from spec-voice to owner-voice | **Not started.** These were written for us |
| Consistent formatting across ten docs | Not started |
| Assemble as PDF and editable copies | Not started |
| ZIP for Gumroad upload | Not started |
| Cover image / thumbnail | Not started |
| Test purchase and download | Not done |

**The rewrite is the real work.** The drafts are internally cross-referenced (`../crm/routing.md`
§6) and written in specification voice. A buyer opening `field-definitions.md` as-is would find a
schema, not a guide.

## 5. Page mechanics

| Item | Status |
|---|---|
| Refund policy decided and stated | **Open** |
| Existing live page reviewed against this copy | **Blocked** — gumroad.com is unreachable from this environment. Must be checked by hand |
| Price confirmed at $197 | Confirmed by the operator |
| CTA wired | Not verified |
| No Instance A content in the listing | Verify by hand |

---

## Publish sequence

1. Write the three cheap missing assets — Tracker, 30-day plan, scoreboard *(optional but they materially improve the page)*
2. Extract the ten Instance B documents, **removing Instance A sections**
3. Rewrite from spec-voice into owner-voice
4. Run each through `cleaning-os-voice` → `anti-ai-writing-slop`
5. Assemble, package, upload
6. Test-purchase and confirm the download
7. Reconcile this copy against the live page by hand
8. Publish

**Steps 2 and 3 are the bulk of it. Step 2 is the one with a real downside if rushed.**
