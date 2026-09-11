# Our Stack

Locked 2026-09-11. Sending layer changed from Smartlead to **Instantly** the same day
(`research/15-stack-change-instantly.md`). One product means a small stack; every tool has to earn
its line item.

| Layer | Tool | Plan | Cost | Why |
|---|---|---|---|---|
| Account data | **Apollo** | Free → paid only when it binds | $0 | Verification and contact patterns. Not discovery — public sources are better for small local businesses |
| Orchestration | **Make** | Core | $12/mo | Connects the pieces. Hosted, so nothing to maintain |
| CRM | **Attio** | Free | $0 | Single source of truth. Free tier covers this volume comfortably |
| Sending | **Instantly** | **Growth** | **$47/mo** | Sequencer plus warmup. Charges nothing per connected mailbox, which is what makes staged scaling cheap |
| Classification & drafting | **Claude API** | Pay as you go | ~$20–50 | Reply classification, pack drafting. Never sends |
| Sending domains | 3–4 dedicated | — | ~$5/mo | **Never the product domain.** See the domain rule below |
| Sending mailboxes | **8** | 2–3 per domain | $24–48/mo | The dominant infrastructure cost, and the one most often left out of a budget |
| Payments | **Gumroad** | — | $0/mo | Merchant of record, and its analytics tell us whether the problem is traffic, page, offer or product |

**Realistic monthly total: $113–$137.** Not $79–$109 — that figure omitted mailboxes, which are
bought from a mailbox provider, not from Instantly. "Unlimited email accounts" means Instantly does
not charge per connected mailbox. The mailboxes themselves still cost $3–6 each per month.

---

## The two Instantly limits that actually bind

Instantly meters three things independently, and the headline feature is not the one that runs out.

| Limit | Growth $47 | Hypergrowth $97 |
|---|---|---|
| Connected email accounts | **Unlimited** | Unlimited |
| Email warmup | **Unlimited** | Unlimited |
| **Campaign emails / month** | **5,000** | 125,000 |
| **Uploaded contacts** | **1,000** | 25,000 |
| Webhooks (real-time events) | **No** | Yes |

**5,000 campaign emails a month is 227/day across every mailbox combined.** Unlimited mailboxes is
worth nothing against that ceiling — 25 mailboxes sharing 5,000 emails send nine cold emails each
per day, which is less than one mailbox should carry and 25× the DNS, warmup and maintenance work
to achieve it.

Growth's cap sizes the architecture to **8 mailboxes at 28 cold/day = 224/day = 4,928/month**. That
is a 98% fit, and it is not a coincidence worth ignoring.

Warmup traffic is separate and unlimited, so it does not consume the 5,000.

---

## Sending architecture

| | Value |
|---|---|
| Mailboxes | **8** |
| Domains | **3–4**, at 2–3 mailboxes each |
| Cold per mailbox per day, at full ramp | **28** |
| Daily total at full ramp | **224** |
| Monthly total | **~4,928** — inside the 5,000 cap |
| Warmup per mailbox per day | 10, ongoing, not counted against the cap |
| Total per mailbox per day | 38 — inside Instantly's own ~40/day guidance |

### The ramp

Never start at full volume. Hold at each step only if bounces, complaints and reply quality stay
healthy; a bad week means staying put, not pushing through.

| Business days | Cold per mailbox | Daily total | + warmup/mailbox |
|---|---|---|---|
| 1–5 | 10 | 80 | 10 |
| 6–10 | 16 | 128 | 10 |
| 11–15 | 22 | 176 | 10 |
| 16+ | **28** | **224** | 10 |

### Capacity in the 90-day window

21 days of warmup, then roughly 48 business days of sending.

- Sends available: 48 × 224 = **10,752**
- At 2.8 touches per contact: 3,840 contacts
- **Uploaded-contacts cap binds first: 1,000/month × 3 = ~3,000 contacts**

**~3,000 contacts, not 6,800.** This supersedes the 6,800 figure in `research/03-funnel-math.md`,
which assumed 24–25 mailboxes and no platform contact cap. Consequences for the revenue arithmetic
are in `.claude/skills/building-distribution/SKILL.md` §2.

---

## The domain rule — hard

**The primary business domain is never used for cold outbound.** No exceptions, no "just this
batch".

| Domain | Used for | Never used for |
|---|---|---|
| **Primary business domain** | Website · Gumroad brand · customer support · free-kit delivery and nurture · post-purchase email · replies to inbound | **Any cold send** |
| **Sending domains** (3–4, dedicated) | Cold outbound only | Anything a customer needs to trust long-term |

Sending domains are replaceable infrastructure. If one burns, it is retired and replaced. The
primary domain is the business identity and cannot be replaced, so it never carries the risk.

**Note the asymmetry in the middle row:** free-kit delivery and nurture are *not* cold. Someone who
asked for the kit is a subscriber, and that mail should come from the primary domain, where the
sender reputation is worth building. Cold acquisition and warm nurture run on different domains on
purpose.

---

## Webhooks — why we are not upgrading yet

Instantly's webhooks require Hypergrowth. Without them, the reply path is **Make polling the
Instantly API on a schedule**, not real-time push.

**That is fine at this volume, and the polling decision is correct.** At 224 cold sends a day,
reply volume is a handful per day. A 15-minute polling interval means the worst-case delay between
a reply landing and Attio knowing about it is 15 minutes, against a same-business-day SLA
(`crm/lifecycle-stages.md` §4). Real-time buys nothing we need.

Revisit when reply volume makes 15 minutes expensive — not because the feature exists.

---

## Upgrade triggers — concrete, so nobody upgrades on vibes

| Upgrade | Trigger | Cost |
|---|---|---|
| Instantly Hypergrowth | We hit 5,000 campaign emails **or** 1,000 uploaded contacts in a month, **and** the positive reply rate is measured and positive | +$50/mo |
| More mailboxes | Hypergrowth is active and 224/day is the binding constraint. Instantly charges nothing for the accounts — only the mailbox provider does | +$3–6 each |
| Apollo Basic | Free-tier export credits run out on a list we actually need | +$49/mo |
| Make Pro | Operation count on Core is exhausted by the eight scheduled jobs | +$9/mo |

**Nothing on this list gets bought because it exists.** Each one needs its trigger to have actually
fired, and the Instantly row needs a *measured* rate, not a hopeful one.

Note what this makes possible: because Instantly does not charge per mailbox, going from 8 to 25
mailboxes later costs only the mailbox provider's fee. Starting small is cheap and scaling is
cheap. That — not "unlimited accounts" on the pricing page — is the actual reason Instantly is the
right tool here.

---

## Deliberately not in the stack

| Not using | Why |
|---|---|
| **n8n** | Make covers it and is hosted. Self-hosting is a maintenance job we don't need at this size. |
| A second CRM | Attio is the single source of truth. Two CRMs means neither is. |
| A second email platform | Instantly does warmup and sequencing. |
| **Instantly's other products** — lead database, enrichment, verification, AI reply agent, Instantly CRM, inbox placement, pre-warmed accounts | Apollo is the prospecting layer, Attio is the CRM, Claude is the reasoning layer. Buying Instantly's versions would duplicate three tools we already have and blur the boundary that makes this system understandable. Instantly is the **execution** layer, nothing more. |
| A large data subscription | Public sources plus Apollo's free tier. Revisit only when a specific gap costs real time. |
| Additional AI tools | Claude does the classification and drafting. |
| A course platform | The product is thirteen files and a download. |
| A chatbot | Nobody is asking us anything yet. |
| Paid ads | Not until organic and outbound have told us what converts. |

---

## The machine

```
APOLLO                                  prospect discovery
   → MAKE (cron)                        move and transform
   → ATTIO          ←→   CLAUDE         record  ·  research & score
   → TRIGGER CHECK                      dated, sourced evidence
   → LEAD SCORE
   → ★ HUMAN APPROVAL ★                 the gate — never automated
   → INSTANTLY                          campaign + warmup
   → REPLY
   → MAKE (poll)                        no webhooks on Growth
   → CLAUDE                             classify only
   → ATTIO                              updated
        ├→ Positive      → HUMAN SALES → GUMROAD → digital product
        ├→ Nurture
        └→ Unsubscribe   → suppressed immediately and permanently
```

**One gate, and it is real.** Nothing sends without a person looking at that specific batch.
Claude classifies replies; it does not answer them. Per `revenue-engine` §4, consequential customer
communication stays with a human.

The eight scheduled Make jobs that implement this are in `automation/make-jobs.md`.

---

## Skill-routing consequence

`n8n-workflow-builder` and `n8n-debugger` are installed and route automation work to a tool we have
now decided against.

**They stay installed** — the decision could reverse, and their workflow-design thinking (error
handling, retries, idempotency, where to put a gate) transfers to Make unchanged. But
`revenue-engine` no longer routes to them by default.

**Open gap:** there is no Make, Attio or Instantly specialist skill. Automation work is
project-authored, using the n8n skills for workflow *design* and translating to Make.

---

## Build order

Manual first. Every step below only earns its place once the manual version is working and the
bottleneck is obvious.

1. **Manual** — spreadsheet, inbox, hand-built packs. At least twenty accounts.
2. **Discovery into Attio** — Make pulls accounts and contacts into the CRM. Biggest time saving,
   least risk.
3. **Trigger watching** — weekly automated checks writing into Attio. The highest-value automation,
   because trigger hunting is the step that gets skipped when busy.
4. **Sequencing with the approval gate** — Instantly holds the sequences, a human approves batches.
5. **Reply classification** — Claude sorts; a human answers.

**Do not build past the step that is currently hurting.** Most of the value is in steps 2 and 3.

Note how little of the Growth plan validation actually needs: `revenue-engine` §8 sets Phase 1 at
100 prospects and Phase 2 at 300–500. Both fit inside a single month's 1,000-contact allowance with
room to spare. There is no version of the validation plan that requires 25 mailboxes.
