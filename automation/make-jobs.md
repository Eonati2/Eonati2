# Make — The Eight Scheduled Jobs

Make is the operating system. Everything below is a scheduled job, not a webhook chain — Instantly
webhooks require Hypergrowth and we are on Growth (`stack.md`).

**Build order still applies.** These are specified so the shape is agreed, not so all eight get
built this week. Jobs 1 and 2 first; the rest only when the manual version of that step is the
thing that hurts.

---

## The jobs

| # | Job | Flow | Schedule | Gate |
|---|---|---|---|---|
| 1 | Prospect ingestion | Apollo → Make → Attio | Daily | Dedupe before write |
| 2 | Qualification analysis | Attio → Make → Claude → Attio | Weekly | Evidence required |
| 3 | Campaign preparation | Attio → Make → **approval queue** → Instantly | Daily | **★ HUMAN ★** |
| 4 | Reply synchronisation | Instantly → Make → Claude → Attio | **Every 15 min** | Classify only |
| 5 | Lead nurture | Attio → Make → Instantly campaign | Daily | Suppression check |
| 6 | Purchase synchronisation | Gumroad → Make → Attio | Hourly | Idempotent on order id |
| 7 | Daily health check | Make → metrics → report | Daily 07:00 | Alert on breach |
| 8 | Weekly executive report | CRM + Instantly + Gumroad → Claude → report | Weekly Mon | Read-only |

---

## Job detail

### 1 — Prospect ingestion · Apollo → Make → Attio · daily

Pulls accounts and contacts, writes to Attio. **Dedupe before write**, not after: match on domain
first, then normalised company name + city. A duplicate that reaches Attio is more expensive to
remove than to prevent (`crm-duplicate-detector` exists because this gets skipped).

Every record carries `source`, `source_date`, and verification metadata. A field that was looked
for and not found is written `unknown`. A field not yet looked for is left empty. Never invent one.

**Watch:** Apollo free-tier export credits. When they bind, that is the Apollo Basic upgrade
trigger — not before.

### 2 — Qualification analysis · Attio → Make → Claude → Attio · weekly

The highest-value job in the list, because qualification research is what gets skipped when busy.

Claude reads the account, looks for the qualifying signals in `rent-roll-os/outbound/icp.md` —
portfolio size, current tooling, asset class — and writes evidence rows. **Every row stores the verbatim observation, its source, and its date.** An observation is not a
conclusion — Claude never writes "they need this product", only what was observed and when.
Portfolio size is usually not published: `unknown` is the correct value, never an estimate.

Runs weekly, not daily: a firm's portfolio size and tooling do not change hourly, and the API
cost is real.

### 3 — Campaign preparation · Attio → Make → approval queue → Instantly · daily

**This is the gate.** Make assembles the batch — scored, trigger-qualified, suppression-checked,
deduped, contact-verified — and puts it in an approval queue. It does **not** push to Instantly.

A human opens the queue, reads that specific batch, and approves it. Only then does Make create
the Instantly campaign and upload the contacts.

Pre-queue checks, all of which must pass: suppression list clear · not previously contacted ·
contact verified within 90 days · compliance fields present · campaign attribution set · under the
day's remaining send allowance.

**Never automate past this point.** `revenue-engine` §4 is not negotiable and no volume target
overrides it.

### 4 — Reply synchronisation · Instantly → Make → Claude → Attio · every 15 minutes

Polling, because Growth has no webhooks. Fifteen minutes against a same-business-day response SLA
is ample (`crm/lifecycle-stages.md` §4).

Make polls the Instantly API for new replies. Claude classifies into: positive · question ·
referral to someone else · not now · not interested · **opt-out** · bounce · auto-reply.

**Claude classifies. Claude does not reply.** Consequential customer communication is human.

**Opt-out is the one branch that acts without a human**: suppress immediately and permanently,
across every domain and campaign, and never re-enroll. That is a compliance gate, not a courtesy.

Bounces mark the contact invalid same-day, to protect domain reputation.

### 5 — Lead nurture · Attio → Make → Instantly campaign · daily

Moves Rent Roll Lite subscribers into the nurture sequence.

**Sends from the primary business domain, not a cold-sending domain.** A subscriber asked for Lite; that is warm mail and it belongs on the identity we are building, not on replaceable
infrastructure. See the domain rule in `stack.md`.

Suppression is re-checked on every run, not just at enrolment.

### 6 — Purchase synchronisation · Gumroad → Make → Attio · hourly

Gumroad sale → Attio stage `Purchased`, with order id, amount and date.

**Idempotent on order id.** A replayed or duplicated event must not create a second purchase row or
double-count revenue. This is the one job where a silent bug corrupts the only number that matters.

Also closes the loop on attribution: which channel, which campaign, which trigger type.

### 7 — Daily health check · Make → metrics → report · daily 07:00

| Metric | Alert threshold |
|---|---|
| Delivery rate | <95% |
| Bounce rate | >2% |
| Complaint rate | **>0.1%** — hard stop at 0.3% |
| Sends today vs. monthly allowance | >80% of the 5,000 consumed with >25% of the month left |
| Uploaded contacts this month | >80% of 1,000 |
| Accounts in an active stage with no `next_action_date` | any |
| Opt-outs not suppressed | **any — page immediately** |

The two Instantly allowance rows exist so the cap is discovered by a report rather than by a
campaign silently stopping mid-month.

### 8 — Weekly executive report · CRM + Instantly + Gumroad → Claude → report · Monday

Claude summarises the week from all three sources. Required contents:

- Qualified Rent Roll Lite downloads, by channel, against the requirement in
  `building-distribution` §2
- Purchases, and cumulative against target
- Outbound: contacts reached, reply rate, positive reply rate — **each with its sample size**
- Any channel at its review date (`building-distribution` §5)
- What changed from assumption to measurement this week

**Every rate is reported with its denominator.** Under n=100 there is no rate, only a count, and
the report says so rather than dividing.

---

## Rules that apply to all eight

**Every job carries:** error logging · retry with backoff · idempotency key · run-completion record
· a kill switch that stops it without stopping the others.

**No job sends customer-facing email except 3 and 5**, and 3 cannot run without human approval.

**No job writes a claim.** Jobs move and classify information. Judgement — targeting, claims,
pricing, final copy, compliance — stays human, per `revenue-engine` §4.

**A job that fails silently is worse than one that fails loudly.** Every failure writes to the
health check in job 7.
