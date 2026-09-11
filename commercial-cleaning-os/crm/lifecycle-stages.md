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

We sell one digital product. There is no walkthrough, no proposal and no negotiation on our side —
this is a funnel, not a sales process.

| # | Stage | Entry criteria | Exit criteria |
|---|---|---|---|
| 1 | **Lead** | A qualified cleaning company in the tracker | First contact sent |
| 2 | **Engaged** | They replied, opened a conversation, or took the free product | They express interest, or go quiet |
| 3 | **Interested** | They asked a question, requested the sample list, or asked how it works | They look at the product, or stall |
| 4 | **Product consideration** | They have seen the product page or been sent the link | Purchase, or no |
| 5 | **Purchased** | Gumroad purchase confirmed | Onboarding email sequence complete |
| 6 | **Customer** | They have the product | — |
| 7 | **Repeat / referral** | They bought again, or referred someone | — |

Plus two terminal states: **Not now** (with a review date) and **Disqualified** (with a reason).

**Why seven and not fourteen.** We are not managing a sales process with site visits and bids. A
buyer either finds the product useful enough to pay $149 or does not. Modelling that as a
thirteen-stage enterprise pipeline would be theatre, and it would make every conversion ratio
meaningless.

*The full 13-stage pipeline still exists — in the product, where it belongs. That is the customer's
sales process, and it is unchanged.*

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
