# Routing

How records enter the CRM, how they move, who owns them, and where the gates are.

**Governing rule:** automation moves *information*; humans make *judgments*. Every rule below that
touches targeting, claims, pricing, copy, or compliance ends at a human.

---

## 1. Inbound sources

| Source | Creates | Auto-created? | Entry stage |
|---|---|---|---|
| Maps / directory scrape | Account | Yes | `Target` |
| Website / contact extraction | Contact | Yes | — |
| Enrichment cascade | Contact fields | Yes | — |
| Public signal scan (permits, listings, job posts, registries) | Trigger_Event | Yes | — |
| Reply to outreach | Activity | Yes | triggers stage review |
| **Gumroad purchase** | Account update + Activity | Yes | → a `Won —` stage (Instance A) |
| Inbound enquiry (form, email, referral) | Account + Contact | **No — human** | `Conversation` |
| Manual add | Account | **No — human** | `Target` |

**No inbound source may create a record already in a contactable stage.** Everything scraped lands
in `Target` and must pass scoring and verification to advance. This is the gate that stops a scrape
from becoming a send.

### Gumroad → CRM

The product is live on Gumroad, so **Gumroad is the source of truth for the purchase event** and the
CRM is the source of truth for everything around it.

| Field | From |
|---|---|
| `purchase_email`, `product`, `price`, `purchase_date`, `order_id` | Gumroad ping / webhook |
| `account_id` | matched on email → else on domain → else **new Account, flagged for human review** |
| Stage | `Purchased` |
| `source` | `gumroad:<product_permalink>` |

Three rules:

1. **Match, never guess.** A purchase whose email matches no known account creates a new Account
   flagged `unmatched_purchase` for human review. Never attach a purchase to a "probably the same
   company" account — that corrupts attribution permanently.
2. **A purchase is not consent to marketing.** A buyer's email enters the customer list, not the
   outbound list. If that email is on Suppression, it **stays suppressed** for outbound; transactional
   delivery of the product they paid for is separate.
3. **A purchase moves the record to `Purchased` and starts the onboarding sequence.** There is no
   capacity gate — a digital product has no delivery constraint, which is one of the reasons the
   service tiers were removed.

Set the Gumroad ping to a receiving endpoint before running any campaign that could produce a sale,
or the first purchases will arrive with no attribution and the funnel numbers will be unrecoverable.

---

## 2. Stage-advance rules

| From → To | Trigger | Automated? |
|---|---|---|
| `Target` → `Researching` | ICP ≥ 3 and serviceability ≥ 1 | Yes |
| `Target` → `Disqualified` | ICP = 0, serviceability = 0, suppression hit, duplicate | Yes |
| `Researching` → `Contacted` | Score computed **and** ≥1 verified contact **and** suppression clear **and** total ≥ 8 | **No — human approves the send** |
| `Contacted` → `Follow-up` | Sequence step 2 due, no reply | Yes |
| `Contacted`/`Follow-up` → `Conversation` | Human reply classified positive/neutral/objection | Yes (classification) |
| any → `Disqualified` | Opt-out, bounce-invalid, out of business | Yes |
| `Interested` → onward | Every later stage | **No — human only** |

**Everything past `Engaged` is manual.** Once a person has replied, no automation touches the
record's stage. Automation's job ends where the relationship begins.

---

## 3. Reply routing

Classification is automated (`reply-handler`); the response is not.

| # | Class | Route | SLA |
|---|---|---|---|
| 1 | **Positive** | Human, same business day. → `Conversation` | Same day |
| 2 | Neutral / info requested | Human. → `Conversation` | Same day |
| 3 | Objection | Human. → `Conversation`, log objection code | 1 business day |
| 4 | Wrong person | Ask for the right one; mark contact `wrong_role` | 2 days |
| 5 | Not now | → `Nurture` + review date **required** | 2 days |
| 6 | Existing provider | → `Nurture`, longer review. **Not** a disqualification | 2 days |
| 7 | **Unsubscribe / do not contact** | → **Suppression, immediate.** Account `Disqualified` | Immediate, automated |
| 8 | Negative | → Suppression. No reply. No "sorry to hear that" | Immediate |
| 9 | Out-of-office | Pause sequence to the stated return date | Automated |
| 10 | Automated / bounce | Hard bounce → contact invalid. Soft → retry once | Automated |

**Class 7 and 8 are the only classes that write to Suppression, and they do it without human
review.** Every other class waits for a person.

**Class 6 is not a loss.** An existing provider is the normal state of a commercial building. It
means *wrong timing*, and timing is the entire premise of the trigger model.

**Never auto-reply to classes 1–4.** A same-day human reply is the highest-value action in the
system; an instant automated one destroys the thing it was trying to speed up.

---

## 4. Suppression

**Global, permanent, and checked at execution time** (schema R5) — not at list build, because a list
built Monday and sent Thursday can send to someone who opted out Tuesday.

| Property | Rule |
|---|---|
| Scope | Every domain, campaign, instance, and channel |
| Entry | Opt-out, negative reply, complaint, manual add, bounce-invalid |
| Removal | **Only** on a written, verifiable request from that person. Logged as an Activity. |
| Re-enrollment | **Never automatic.** No exceptions, no "it's been six months" |
| Propagation | An opt-out email suppresses the Account and every Contact sharing it (R6) |
| Phone | Same list. A "don't call me" suppresses email too. |

A suppressed record is never deleted — deleting it loses the evidence that it was suppressed, which
is exactly what the record is for.

---

## 5. Ownership

Single operator today, so ownership is about **mode**, not headcount — but the field is populated
now so that adding a second person later does not require a migration.

| Role | Owns stages |
|---|---|
| Research | `Target`, `Researching` |
| Outreach | `Contacted`, `Follow-up`, `Nurture` |
| Sales | `Conversation` onward |
| Ops | `Won` after handoff |

Reassignment writes an Activity row. An account with no owner cannot be in an active stage (R1).

---

## 6. Pre-send gate

**Every** live send passes all of these. A failure blocks the send; it does not warn and proceed.

| # | Check | Blocks on |
|---|---|---|
| 1 | Suppression | Any match |
| 2 | Duplicate | Same contact in another active campaign |
| 3 | Verification | `verification_status ≠ verified`, or verified >90 days ago |
| 4 | Score floor | Total < 8 |
| 5 | Compliance | Missing physical address, sender identity, or opt-out mechanism |
| 6 | Claim check | Copy asserts anything about the prospect not evidenced by a Trigger_Event |
| 7 | Deliverability | Daily volume cap, domain health, bounce rate over threshold |
| 8 | Attribution | Campaign ID missing |
| 9 | **Human approval** | **Always required for a live send** |
| 10 | Kill switch | Global send-freeze flag is set |

**Check 6 is the one no tool will do for you.** Read the merged copy — not the template — and
confirm every claim about the prospect traces to a dated, sourced Trigger_Event. This is where
"they don't have a cleaner yet" gets caught.

**Check 9 has no bypass.** No scheduled job, no agent, no "approved in bulk for the week." Per
`revenue-engine` §4, there is no autonomous sending in this system.

---

## 7. Phone routing — separate and higher-risk

Phone is **not** a channel in the send gate above. It has its own path:

1. Classify line type (landline / wireless / unknown) **before** the number reaches any dial list.
2. Check Suppression — the shared list.
3. **Manual dial only.** No autodialer, power dialer, prerecorded message, or AI voice.
4. Business hours in the recipient's local time.
5. Log an Activity row per call attempt — outcome, duration, disposition. The 2024 TSR amendment
   extends recordkeeping to B2B telemarketing, so this log is a compliance artifact, not a nicety.
6. Any "don't call" → Suppression immediately, both channels.

**The phone workstream stays blocked pending counsel review** (`research/11-corrections-log.md` §D).
Until then these rules describe what will be built, not what is running.

---

## 8. Hygiene jobs

| Job | Cadence | Action |
|---|---|---|
| R1 violations | Daily | List active accounts missing owner / next action / date |
| Overdue next actions | Daily | List and re-prioritize |
| Verification decay | Weekly | Flag contacts verified >90 days ago |
| Duplicate scan | Weekly | Route to `crm-duplicate-detector` |
| Suppression reconciliation | Weekly | Confirm every opt-out propagated |
| Nurture review dates | Weekly | Surface accounts due |
| Stale `Walkthrough Scheduled` | Weekly | Any past its date |
| Trigger expiry | Weekly | Re-score accounts whose triggers aged out |

All eight are read-and-report. **None of them writes to a record without a human deciding** — an
automated cleanup that silently disqualifies accounts is indistinguishable from a bug.
