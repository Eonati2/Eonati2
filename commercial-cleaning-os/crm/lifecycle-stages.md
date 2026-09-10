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

## 3. Instance A — Product CRM (our pipeline)

Accounts are cleaning companies. **There is no walkthrough** — the analogous event is the proof pack
and the call that follows it.

| # | Stage | Entry criteria | Exit criteria | Owner |
|---|---|---|---|---|
| 1 | **Target** | Cleaning company found; in a target metro | Passes ICP filter (§ICP: 3–25 staff, website, commercial services, not a franchise) | Us |
| 2 | **Researching** | Assigned for enrichment | Owner or sales lead identified; email verified | Us |
| 3 | **Contacted** | Verified contact; suppression clear; first touch sent | Reply, or sequence exhausted | Us |
| 4 | **Follow-up** | No reply yet | Reply, or cadence complete | Us |
| 5 | **Pack Requested** | They asked for the proof pack | Pack delivered | Us |
| 6 | **Pack Delivered** | Pack sent by a human (never automated) | They respond to it, or go quiet | Us |
| 7 | **Conversation** | Substantive reply after the pack | Offer made, or deferred | Us |
| 8 | **Offer Made** | A specific tier proposed with a price | Purchase, decline, or deferral | Us |
| 9 | **Won — Core OS** | $197 purchase confirmed | — terminal (may re-enter at 8 for upgrade) | Us |
| 10 | **Won — Setup** | $497 purchase confirmed | — terminal | Us |
| 11 | **Won — Managed Pilot** | $2,000 purchase confirmed **and** a delivery slot is free | — terminal | Us |
| 12 | **Lost** | Explicit no. `loss_reason` required | — terminal | Us |
| 13 | **Nurture** | Interested, wrong timing | Review date arrives | Us |
| 14 | **Disqualified** | Not ICP, opted out, unreachable | — terminal | Us |

### Stage 11 has a capacity gate, and it is real

**Managed Pilot is capped at 5 concurrent clients.** Entry requires a free delivery slot, not just a
payment. If all five are full, the account goes to `Nurture` with a review date — never to a
waitlist that implies a date we cannot honour.

This cap is genuine delivery capacity (8–12 hours per pilot), not a scarcity tactic. Describe it
that way to prospects, and enforce it in the CRM rather than in good intentions. **Five pilots at
$2,000 are the whole gross target**, which also means five pilots are the whole delivery
obligation — over-selling the cap does not accelerate revenue, it destroys it.

### Stage 6 is manual by policy
Pack delivery is never automated. It is the highest-leverage 90 seconds in the funnel — where a
$197 sale becomes a $2,000 one — and per `revenue-engine` §4 consequential customer communication
stays with a human.

---

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
