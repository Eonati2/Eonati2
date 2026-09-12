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

## 2. Instance B — retired

The 13-stage contract pipeline shipped inside the previous product, where the customer was a
cleaning company chasing building contracts. **It does not transfer.** CRE buyers already have
their own deal systems and we are not selling them a pipeline.

Archived at `../archive/commercial-cleaning-os/crm/lifecycle-stages.md`.

The closed lists below (disqualification and loss reasons) were rewritten for our funnel and now
live in §3.

---

## 3. Instance A — our funnel

Revised 2026-09-11. We sell one digital product. There is no walkthrough, no proposal and no
negotiation on our side — this is a funnel, not a sales process.

The previous seven stages collapsed everything before first contact into a single `Lead`, which
hid the question that now matters most: is the bottleneck discovery, qualification, or signal
finding? It also had no stage for the free product, which the distribution work made the central
mechanism (`building-distribution`). Both are fixed below.

| # | Stage | Entry criteria | Exit criteria |
|---|---|---|---|
| 1 | **Prospect** | A CRE owner or management firm exists in the tracker with a domain and a location | Passes the ICP filter, or disqualified |
| 2 | **Qualified** | Passes ICP: US, commercial asset class, ~5–150 leases, no lease-admin software | A dated, sourced qualifying observation is recorded |
| 3 | **Signal-Qualified** | ≥1 qualifying signal with verbatim evidence, source and date — spreadsheet tooling, portfolio in band, a role that owns the calendar | ≥1 **verified** contact, suppression clear, approved in a batch |
| 4 | **Contacted** | First touch sent through Instantly | Any human reply, or sequence exhausted |
| 5 | **Engaged** | A human reply that is not an opt-out, bounce or auto-reply | They ask for the kit, look at the product, or go quiet |
| 6 | **Lite Delivered** | Rent Roll Lite requested **and** delivery confirmed | They view the product page, or the nurture sequence completes |
| 7 | **Product Consideration** | Product page visited, or the link sent and opened | Purchase, or no |
| 8 | **Purchased** | Gumroad order confirmed (job 6) | Onboarding sequence completes without bounce or refund |
| 9 | **Customer** | Onboarding complete, refund window passed | — |
| 10 | **Advocate** | They referred someone, or bought a second thing when one exists | — |

Plus two non-terminal exits: **Not now** (requires a review date) and **Disqualified** (requires a
reason, from the closed list in §2).

### Three changes from the twelve stages as specified

**Confirmed 2026-09-12.** The spec listed twelve stages (described as thirteen); ten were
implemented, the three changes below were put back to the owner alongside the full twelve, and ten
was chosen. This is a decision, not an outstanding deviation.

**`Lead Magnet Requested` + `Lead Magnet Delivered` → one stage, `Lite Delivered`.** Delivery of a
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
| Lite requested → Lite delivered | **Automated, immediate** | A manual step here loses subscribers for no reason |
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
| Contacts with `verification_date` >90 days | <20% | List decay |

**Recalibrate stage definitions quarterly.** A stage nobody ever exits is either misdefined or the
work is not happening — and the pipeline will not tell you which unless you go and look.
