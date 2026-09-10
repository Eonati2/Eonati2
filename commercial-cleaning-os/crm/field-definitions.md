# Field Definitions

Every field, its type, allowed values, who sets it, and what validates it.

**Three states apply to every nullable field** (schema §5): a value · `unknown` (looked, not
findable) · empty (not looked yet). Never guess. `unverified:<value>` marks a candidate that may be
researched but **never used in outreach**.

**Set by** — `auto` (pipeline) · `human` · `derived` (computed, never typed) · `system` (immutable).

---

## 1. ACCOUNT

### Identity
| Field | Type | Set by | Notes |
|---|---|---|---|
| `account_id` | `ACC-{METRO}-{5 digits}` | system | Immutable |
| `company` | text | auto | Legal or trading name as published |
| `website` | url | auto | Normalized: lowercase, no protocol, no `www.`, no trailing slash |
| `address`, `city`, `state`, `zip` | text | auto | US only |
| `metro` | enum | auto | Matches the `account_id` prefix |
| `phone` | E.164 | auto | |
| `line_type` | `landline \| wireless \| unknown` | auto | **Required before any dial** |

### Classification
| Field | Type | Set by | Notes |
|---|---|---|---|
| `instance` | `A \| B` | system | A = cleaning company (our buyer); B = facility (their target) |
| `segment` | enum | auto→human | **A:** commercial · residential · mixed · franchise · national_fm. **B:** property_management · office · medical · industrial · retail · education · fitness · worship · other |
| `est_sqft` | integer | auto | Instance B. Mark `estimated` |
| `est_monthly_value` | currency range | derived | sqft × segment rate. **Always an estimate** — store the inputs |
| `employee_band` | `1-2 \| 3-10 \| 11-25 \| 26-99 \| 100+ \| unknown` | auto→human | Instance A |
| `serviceability` | `0 \| 1 \| 2` | human | See `scoring.md` §5 |

### Provenance — required, not optional
| Field | Type | Set by | Notes |
|---|---|---|---|
| `source` | text | auto | e.g. `apify:gmaps:dfw-medical`, `gumroad:<permalink>`, `referral`, `manual` |
| `date_found` | date | auto | |
| `verification_date` | date | auto | Last time core facts were re-checked |
| `data_notes` | text | human | Anything about how the data was obtained or its limits |

**No record without a source.** Provenance is what lets us answer "where did this come from and are
we permitted to use it" — and what stops the CRM filling with data of unknown legitimacy.

### Scoring — all derived
| Field | Type | Notes |
|---|---|---|
| `icp_score` | 0–5 | |
| `commercial_value_score` | 0–5 | |
| `trigger_score` | 0–5 | Includes modifiers; **0 if source or date missing** |
| `dm_access_score` | 0–3 | |
| `serviceability_score` | 0–2 | |
| `total_score` | 0–20 | **Derived. Never hand-typed** (R8) |
| `band` | `priority \| active \| nurture \| park` | Derived from total |

### Pipeline
| Field | Type | Set by | Notes |
|---|---|---|---|
| `stage` | enum | auto/human | Per instance — `lifecycle-stages.md` §2/§3 |
| `stage_entered_date` | date | auto | Rewritten on every transition |
| `owner` | enum | human | research · outreach · sales · ops |
| `next_action` | text | human | **Required in any active stage** (R1) |
| `next_action_date` | date | human | **Required in any active stage** |
| `last_contact_date` | date | derived | Newest outbound Activity |
| `last_reply_date` | date | derived | Newest inbound Activity |
| `nurture_review_date` | date | human | **Required in `Nurture`** |
| `loss_reason` | enum | human | **Required in `Lost`** — closed list |
| `disqualify_reason` | enum | human | **Required in `Disqualified`** — closed list |
| `campaign_id` | text | auto | Attribution |
| `internal_notes` | text | human | **Instance A only — never ships to a customer** |

### Purchase — Instance A
| Field | Type | Set by | Notes |
|---|---|---|---|
| `purchase_email` | email | auto | From Gumroad |
| `product` | `core_os \| setup \| managed_pilot` | auto | **Only `core_os` is currently purchasable.** Setup and Managed Pilot have no Gumroad listing — they are closed manually and recorded here after payment by another route |
| `order_id` | text | auto | Gumroad order reference |
| `purchase_date` | date | auto | |
| `amount` | currency | auto | Actual paid, not list price |
| `unmatched_purchase` | boolean | auto | **True → human review.** Never guess the account |
| `over_capacity` | boolean | auto | True when a pilot sells past the cap of 5 |
| `pilot_slot` | `1-5 \| null` | human | Assigned only when a slot is genuinely free |

---

## 2. CONTACT

| Field | Type | Set by | Notes |
|---|---|---|---|
| `contact_id` | `CON-{5 digits}` | system | |
| `account_id` | FK | system | |
| `first_name`, `last_name` | text | auto→human | `unknown` if not findable — **never inferred from an email prefix** |
| `role` | text | auto→human | As published |
| `role_category` | enum | human | owner · gm · sales · bd · facilities · office_manager · practice_manager · property_manager · operations · other · unknown |
| `is_decision_maker` | `confirmed \| likely \| unknown \| no` | human | **`confirmed` requires evidence.** A title is not evidence |
| `business_email` | email | auto | Business addresses only |
| `email_pattern_guessed` | boolean | auto | True → caps DM Access at 2, blocks outreach |
| `verification_status` | `verified \| unverified \| invalid \| catch_all \| unknown` | auto | |
| `verification_date` | date | auto | **>90 days = stale**, re-verify |
| `phone` | E.164 | auto | |
| `line_type` | `landline \| wireless \| unknown` | auto | Required before dialling |
| `source` | text | auto | **Required** (R2) |
| `source_date` | date | auto | **Required** |
| `contact_status` | `active \| wrong_role \| left_company \| bounced \| unreachable \| suppressed` | auto/human | |
| `opt_out` | boolean | auto | **True propagates to Account and all sharing contacts** (R6) |
| `opt_out_date` | date | auto | |
| `opt_out_source` | text | auto | Which message, which channel |
| `notes` | text | human | |

**`business_email` only.** Personal addresses are not collected for outbound, even when public.

**`is_decision_maker = confirmed`** requires that someone said so, or that a published document says
so. Inferring it from a job title is exactly the assumption the project rules forbid.

---

## 3. ACTIVITY — append-only

Rows are added, never edited or deleted (R7). This is the audit trail and the TSR recordkeeping
artifact.

| Field | Type | Set by | Notes |
|---|---|---|---|
| `activity_id` | `ACT-{ISO8601}-{5}` | system | |
| `account_id`, `contact_id` | FK | system | Contact may be null (account-level note) |
| `timestamp` | ISO 8601 | system | UTC |
| `direction` | `outbound \| inbound \| internal` | system | |
| `channel` | `email \| phone \| linkedin \| meeting \| note \| system` | system | |
| `type` | enum | system | send · reply · bounce · opt_out · call_attempt · call_connected · voicemail · meeting · stage_change · score_change · note · approval · sla_miss |
| `campaign_id`, `sequence_step` | text / int | auto | |
| `subject`, `body_ref` | text | auto | Store a reference, not a duplicate of the body |
| `reply_class` | 1–10 | auto | Per `routing.md` §3 |
| `objection_code` | enum | human | When `reply_class = 3` |
| `call_outcome` | enum | human | connected · voicemail · no_answer · gatekeeper · wrong_number · do_not_call |
| `call_duration_sec` | integer | human | **TSR call-detail requirement** |
| `approved_by` | text | human | **Required on every live send** |
| `notes` | text | human | |

---

## 4. TRIGGER_EVENT

| Field | Type | Set by | Notes |
|---|---|---|---|
| `trigger_id` | `TRG-{5}` | system | |
| `account_id` | FK | system | |
| `trigger_type` | enum | auto | new_location · new_facility · move_occupancy · property_mgmt_change · facilities_hiring · renovation_reopening · acquisition · generic_growth · funding · generic_hiring · review_signal |
| `tier` | `high \| medium \| low` | derived | Per `scoring.md` §3 |
| `trigger_date` | date | auto | **When the event happened** — not when we found it. **Required** |
| `discovered_date` | date | auto | |
| `freshness_days` | integer | derived | today − `trigger_date` |
| `trigger_source` | url or citation | auto | **Required** (R3) |
| `evidence` | text | auto | **Verbatim** observed fact. No interpretation |
| `expired` | boolean | derived | `freshness_days` > window |

### The evidence field is the guardrail

`evidence` holds **what was observed, quoted or stated plainly, with nothing added**.

| Acceptable | Not acceptable |
|---|---|
| `GBP listing created 2026-08-14 at 5910 N MacArthur Blvd` | `They just moved and need a cleaner` |
| `Indeed post "Facilities Manager", published 2026-09-02` | `They're expanding their facilities team so cleaning is in play` |
| `Review 2026-08-30: "restrooms were not clean"` | `Their current cleaner is failing` |

Everything in the right-hand column is a conclusion. Conclusions do not go in the CRM and they never
go in outreach copy. The pre-send claim check (`routing.md` §6, check 6) tests copy against this
field specifically.

---

## 5. SUPPRESSION

| Field | Type | Notes |
|---|---|---|
| `value` | email or E.164 | Primary key, lowercased / normalized |
| `type` | `email \| phone` | |
| `added_date` | date | |
| `reason` | `opt_out \| negative_reply \| complaint \| manual \| bounce_invalid` | |
| `source_activity_id` | FK | Which message caused it |
| `scope` | always `global` | No per-campaign suppression — it would be a loophole |

**Never deleted.** Removal requires a written verifiable request, logged as an Activity, and even
then the row is marked rather than removed.

---

## 6. Required-field matrix

| Stage | Also required |
|---|---|
| `Target` | source, date_found |
| `Researching` | owner, next_action, next_action_date |
| `Contacted` | ≥1 contact `verification_status = verified`, campaign_id, `approved_by` on the send |
| `Conversation` | last_reply_date, reply_class |
| `Walkthrough Scheduled` (B) | date, time, site address — **confirmed in writing** |
| `Proposal Sent` (B) | proposal_ref, amount |
| `Offer Made` (A) | tier, price quoted |
| `Won — Managed Pilot` (A) | pilot_slot, or `over_capacity = true` |
| `Nurture` | nurture_review_date |
| `Lost` | loss_reason |
| `Disqualified` | disqualify_reason |

---

## 7. Validation

**Blocking** — the write fails:
missing source on an Account or Contact · missing owner / next action / date in an active stage ·
Trigger_Event without source or date · send to a suppressed value · send to an unverified contact ·
send without `approved_by` · hand-typed `total_score` · edit or delete of an Activity row ·
`Won — Managed Pilot` without a slot or an `over_capacity` flag.

**Warning** — logged to the hygiene report:
`verification_date` >90 days · expired trigger still scored · account past `next_action_date` ·
`Nurture` without a review date · `est_monthly_value` with no stored inputs ·
`is_decision_maker = confirmed` with no supporting Activity.
