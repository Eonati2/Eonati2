# CRM Schema

**The CRM is the single source of truth.** If a fact about an account, contact, or interaction is not
in the CRM, it did not happen. Nothing downstream — outreach, scoring, automation, analytics — may
hold state that the CRM does not hold.

---

## 1. The two-instance architecture

There are **two distinct pipelines** in this business, and merging them corrupts every metric.

| | **Instance A — Product CRM** | **Instance B — Contract CRM** |
|---|---|---|
| Whose | Ours | The customer's |
| Account = | A commercial cleaning company | A building / facility / property |
| We are selling | Core OS, Setup, Managed Pilot | *They* sell recurring cleaning |
| Terminal win | A $197 / $497 / $2,000 purchase | A signed cleaning contract |
| Geography | 10–15 metros (buyer supply) | The customer's own metro |
| Ships to customer? | No — internal | **Yes — this is the product** |

**One schema, two instances.** Same objects, same fields, same scoring shape — different stage sets
(`lifecycle-stages.md` §2 and §3) and different segment vocabularies.

This matters beyond tidiness: **Instance B is a deliverable.** We run it on ourselves in Instance A,
which is what lets the product be demonstrated rather than described. Any field we would not want a
customer to see does not belong in the shared schema — put it in Instance A's `internal_notes`.

---

## 2. Objects

```
ACCOUNT ──1:N──> CONTACT
   │                 │
   └──1:N──> ACTIVITY <──N:1──┘        SUPPRESSION (standalone, global)
   │
   └──1:N──> TRIGGER_EVENT
```

| Object | Grain | Purpose |
|---|---|---|
| **Account** | One company or facility | The unit of pursuit. Carries stage, score, owner, next action. |
| **Contact** | One person | Who we may contact, and how. Carries consent state. |
| **Activity** | One interaction | Every send, call, reply, meeting, note. **Append-only.** |
| **Trigger_Event** | One observed signal | The evidence behind a trigger, with its source and date. |
| **Suppression** | One email or phone | Global do-not-contact. Overrides everything. |

### Why Activity and Trigger_Event are separate objects

Both were implicit in the field list as `Notes` and `Trigger`. Splitting them out is not
bureaucracy — each answers a requirement the flat version cannot:

**Activity** exists because the FTC's 2024 TSR amendment imposes recordkeeping on B2B telemarketing
— call detail records and DNC-compliance records — and because the audit-trail safety gate requires
a log that cannot be overwritten. A `Notes` field is not a record. Activity is **append-only**: rows
are never edited or deleted, only added.

**Trigger_Event** exists because an account can carry more than one signal, because scoring stacks
them, and because every trigger must be traceable to a dated source. A single `Trigger` string
cannot hold evidence, and unevidenced triggers are how "they don't have a cleaner" gets written.

---

## 3. Identity and keys

| Object | ID format | Natural key for dedupe |
|---|---|---|
| Account | `ACC-{metro}-{00001}` e.g. `ACC-DFW-00042` | normalized domain, else normalized name + zip |
| Contact | `CON-{00001}` | lowercased email; else name + account_id |
| Activity | `ACT-{ISO8601}-{00001}` | none — append-only, duplicates allowed |
| Trigger_Event | `TRG-{00001}` | account_id + trigger_type + trigger_date |
| Suppression | the email or E.164 phone itself | the value |

**Domain normalization before dedupe:** lowercase, strip `www.`, strip protocol, strip trailing
slash, strip query. Shared-host domains (`gmail.com`, `wixsite.com`, `godaddysites.com`) are **not**
valid account keys — fall back to name + zip. Route suspected duplicates to `crm-duplicate-detector`
rather than merging by hand.

---

## 4. Integrity rules — enforced, not aspirational

| # | Rule | On violation |
|---|---|---|
| R1 | Every Account in an active stage has `owner`, `next_action`, `next_action_date` | Block stage change; flag on the daily hygiene report |
| R2 | Every Contact has `source` and `source_date` | Contact is unusable for outreach |
| R3 | Every Trigger_Event has `trigger_source` and `trigger_date` | Trigger scores 0 |
| R4 | An Account may not enter Contacted without ≥1 Contact whose `verification_status = verified` | Block |
| R5 | Any send or dial checks Suppression **at execution time**, not at list build | Block the send |
| R6 | `opt_out = true` propagates to every Contact sharing that email, and to the Account | Automatic, immediate |
| R7 | Activity rows are append-only | Reject edits and deletes |
| R8 | `total_score` is derived, never typed by hand | Recompute on write |
| R9 | A field whose value is not known is `unknown` — never guessed, never inferred, never left ambiguous | See §5 |
| R10 | An Account may not enter Proposal Sent / Pilot Offered without a completed prior stage | Block |

**R9 is the anti-fabrication rule and it is the one most likely to be quietly broken.** Enrichment
tools return plausible guesses. A guessed decision-maker name is worse than a blank one, because it
gets used.

---

## 5. Three states, never two

Every nullable field distinguishes:

| State | Meaning | Written as |
|---|---|---|
| **Value** | Known and verified | the value |
| **`unknown`** | We looked and could not establish it | `unknown` |
| **empty** | We have not looked yet | `` (blank) |

`unknown` and blank are different facts and drive different work: blank means *go research it*,
`unknown` means *stop spending time on it*. Collapsing them wastes hours re-researching dead ends.

A field may also be `unverified:<value>` — a candidate found but not confirmed. **An
`unverified:` value may never be used in outreach**, only as a research lead.

---

## 6. Storage

**Start in Google Sheets.** One workbook per instance, one tab per object, plus `Suppression` shared
across both. This is deliberate: the process must be validated before it is automated, per
`revenue-engine` §8, and a spreadsheet makes a broken process visible where a CRM hides it.

**Migrate when** any of these is true: >2,000 account rows · >1 person writing concurrently ·
automation writes exceeding ~200/day · the audit trail needs to be tamper-evident.

Schema is storage-agnostic — every field in `field-definitions.md` carries a type that maps cleanly
to Sheets, Airtable, HubSpot, or Postgres.

---

## 7. What is deliberately NOT in this schema

| Omitted | Why |
|---|---|
| Deal / Opportunity object | One account pursues one contract at a time at this scale. Revisit if a customer pursues multi-building portfolios under one property manager. |
| Lead object | Everything is an Account plus Contacts from the start. An unqualified account is an Account in `Target`. |
| MQL / SQL | `revops` recommends them; they are SaaS lifecycle constructs that add a handoff we do not have (no marketing team handing to a sales team — same person does both). Adopting them would create a fake boundary and a fake metric. |
| Engagement score | Requires open/click tracking. We deliberately do not use tracking pixels — they depress deliverability and inflate numbers with bot activity. Scoring is fit + trigger only. |
| Email open / click fields | Same reason. Optimize for replies and conversations, per `revenue-engine` §7. |
