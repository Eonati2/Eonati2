# Lifecycle Stages

A stage is defined by its **entry criteria, exit criteria, and owner** — not by its name. A stage
without testable entry criteria is a label, and labels produce pipelines that look healthy and
forecast nothing.

**Every account in an active stage carries an owner, a next action, and a next-action date** (schema
R1). No exceptions. An account with no next action is not in the pipeline; it is in `Nurture`.

---

## 1. Rules that apply to both instances

**Stages move forward one at a time** (`schema.md` R10). Skipping is allowed only backwards (to
`Nurture`, `Disqualified`, or `Lost`).

**Terminal stages** are `Won`, `Lost`, `Disqualified`. Reopening requires a new Activity row stating
why; the stage history is never rewritten.

**`Nurture` is not a graveyard.** It carries a `nurture_review_date`. An account with no review date
belongs in `Disqualified`.

**Time-in-stage is tracked on every transition.** A stage nobody exits is a broken stage, and you
can only see that if entry timestamps are logged.

**Stage change is an Activity row.** Append-only, per schema R7.

---

## 2. Instance B — Contract CRM (the customer's pipeline)

This is the pipeline that ships inside the product. Accounts are buildings and facilities; the win
is a signed recurring cleaning contract.

| # | Stage | Entry criteria | Exit criteria | Owner |
|---|---|---|---|---|
| 1 | **Target** | Account created; passes basic geography and segment filter | ICP score ≥ 3 **and** serviceability ≥ 1 | Research |
| 2 | **Researching** | Passed §1 filter; research assigned | Decision-maker role identified **and** ≥1 contact found **and** total score computed | Research |
| 3 | **Contacted** | ≥1 **verified** contact (schema R4); suppression clear; first touch sent | Any reply received, or sequence exhausted | Outreach |
| 4 | **Follow-up** | Sequence running, no reply yet | Reply received, or follow-up cadence complete | Outreach |
| 5 | **Conversation** | A human reply that is not an opt-out or bounce | Walkthrough agreed, or disqualified, or deferred | Sales |
| 6 | **Walkthrough Scheduled** | Date, time and site address confirmed **in writing** | Walkthrough happens, or is cancelled | Sales |
| 7 | **Walkthrough Complete** | Site visited; scope notes and measurements captured | Proposal sent, or no-bid decision | Sales |
| 8 | **Proposal Sent** | Written proposal delivered with scope, frequency and price | Accepted, rejected, or under negotiation | Sales |
| 9 | **Negotiation** | Prospect has engaged on terms, scope or price | Signed, or lost | Sales |
| 10 | **Won** | Signed agreement **and** confirmed start date | — terminal | Sales → Ops |
| 11 | **Lost** | Explicit no, or awarded elsewhere. `loss_reason` required | — terminal | Sales |
| 12 | **Nurture** | Real interest, wrong timing. `nurture_review_date` required | Review date arrives → back to Contacted | Outreach |
| 13 | **Disqualified** | Fails ICP, unserviceable, opted out, or unreachable. `disqualify_reason` required | — terminal | Any |

### The two stages that carry the business

**Walkthrough Scheduled → Walkthrough Complete** is where commercial cleaning is actually won or
lost. "Confirmed in writing" is a hard gate: a verbal maybe on a phone call is stage 5, not stage 6,
and treating it as stage 6 is the single most common way this pipeline lies to its owner.

**Contacted → Conversation** is the conversion that determines everything upstream. If this ratio is
weak, the problem is targeting or trigger quality — not follow-up volume.

### Disqualification reasons — a closed list
`not_serviceable_geography` · `not_serviceable_scope` · `too_small` · `chain_decides_centrally` ·
`no_reachable_contact` · `opted_out` · `duplicate` · `out_of_business` · `not_icp`

### Loss reasons — a closed list
`price` · `incumbent_retained` · `awarded_competitor` · `no_decision` · `scope_mismatch` ·
`timing` · `lost_contact` · `we_declined`

Free-text loss reasons make loss analysis impossible. Add a code to the list rather than typing
prose into it; prose goes in the Activity note beside it.

---

## 3. Instance A — our funnel

Revised 2026-09-11. We sell one digital product. There is no walkthrough, no proposal and no
negotiation on our side — this is a funnel, not a sales process.

The previous seven stages collapsed everything before first contact into a single `Lead`, which
hid the question that now matters most: is the bottleneck discovery, qualification, or trigger
finding? It also had no stage for the free kit, which the distribution work made the central
mechanism (`building-distribution`). Both are fixed below.

| # | Stage | Entry criteria | Exit criteria |
|---|---|---|---|
| 1 | **Prospect** | A cleaning company exists in the tracker with a domain and a location | Passes the ICP filter, or disqualified |
| 2 | **Qualified** | Passes ICP: US, commercial/janitorial, capacity for recurring B2B accounts | A dated, sourced `Trigger_Event` is recorded |
| 3 | **Trigger-Qualified** | ≥1 trigger with verbatim evidence, source and date | ≥1 **verified** contact, suppression clear, approved in a batch |
| 4 | **Contacted** | First touch sent through Instantly | Any human reply, or sequence exhausted |
| 5 | **Engaged** | A human reply that is not an opt-out, bounce or auto-reply | They ask for the kit, look at the product, or go quiet |
| 6 | **Kit Delivered** | Free kit requested **and** delivery confirmed | They view the product page, or the nurture sequence completes |
| 7 | **Product Consideration** | Product page visited, or the link sent and opened | Purchase, or no |
| 8 | **Purchased** | Gumroad order confirmed (job 6) | Onboarding sequence completes without bounce or refund |
| 9 | **Customer** | Onboarding complete, refund window passed | — |
| 10 | **Advocate** | They referred someone, or bought a second thing when one exists | — |

Plus two non-terminal exits: **Not now** (requires a review date) and **Disqualified** (requires a
reason, from the closed list in §2).

### Three changes from the twelve stages as specified

The spec listed twelve stages (described as thirteen). Ten are implemented. What changed, and why
— each is one edit to restore:

**`Lead Magnet Requested` + `Lead Magnet Delivered` → one stage, `Kit Delivered`.** Delivery of a
digital file is instant and automatic. Two stages separated by milliseconds produce a
time-in-stage of zero and a conversion ratio of 100%, which measures nothing. A delivery that
*fails* is a real event — it is a flag and an alert in job 7, not a pipeline stage.

**`Engaged Customer` cut.** It had no observable entry criterion. Gumroad does not tell us whether
someone opened the files, so the stage could only ever be set by guessing. Rule 1 of this document:
a stage without testable entry criteria is a label, and labels produce pipelines that look healthy
and forecast nothing. If an observable signal appears later — a reply to an onboarding email, a
support question — the stage can come back with that as its criterion.

**`Referral / Repeat` → `Advocate`, and the repeat half is currently unreachable.** There is one
product and no second purchase to make. Referral is real, so the stage stays; `Repeat` is left in
the definition for when a second product exists, and until then nobody should expect this stage to
populate from purchases.

### Why ten and not thirteen

Instance B's thirteen stages model a real sales process with site visits, bids and negotiation.
Ours does not have one: a buyer either finds the product worth $197 or does not. Every stage here
earns its place by being independently observable and by answering a question we actually ask.
Adding stages that cannot be observed does not produce a better pipeline — it produces a pipeline
that lies.

*The full 13-stage pipeline still exists — in the product, where it belongs. That is the
customer's sales process, and it is unchanged (§2).*

## 4. Handoff SLAs

`revops` is right that every handoff is a leak. Ours are single-operator handoffs — between *modes*
rather than between teams — but the SLA still applies because the delay is what kills them.

| Handoff | SLA | Why |
|---|---|---|
| Positive reply → human response | **Same business day** | Interest decays fast; this is the scarcest resource in the business |
| Pack requested → pack delivered | **24 hours** | The trigger data is time-sensitive; a stale pack undercuts the whole premise |
| Walkthrough complete → proposal sent | **48 hours** (Instance B) | Competitors are bidding the same week |
| Opt-out received → suppressed | **Immediate, automated** | Compliance gate, not a courtesy |
| Bounce → contact marked invalid | **Same day** | Protects domain reputation |

A missed SLA is logged as an Activity, not silently absorbed.

---

## 5. Health checks — run weekly

| Check | Threshold | Meaning |
|---|---|---|
| Accounts in an active stage with no `next_action_date` | **0** | R1 is being violated |
| Accounts past their `next_action_date` | <10% | The pipeline is being worked |
| Median days in `Contacted` | <21 | Sequences are completing |
| Accounts in `Nurture` with no review date | **0** | Nurture is being used as a graveyard |
| `Walkthrough Scheduled` older than its date | **0** | Stale stage, pipeline is lying |
| Contacts with `verification_date` >90 days | <20% | List decay |

**Recalibrate stage definitions quarterly.** A stage nobody ever exits is either misdefined or the
work is not happening — and the pipeline will not tell you which unless you go and look.
