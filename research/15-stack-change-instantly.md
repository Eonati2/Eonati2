# 15 — Sending Layer: Smartlead → Instantly
**Date:** 2026-09-11 · **Confirmed 2026-09-12** · Status: **decided.** Stack locked. Price locked
at $197.

Both open questions from this record were put back to the owner with the full trade-offs and
resolved: **Instantly Growth + 8 mailboxes** (over Hypergrowth + 25, and over Growth + 25 as
originally specified), and **10 CRM stages** (over the 12 specified). Neither is an outstanding
deviation.

---

## A. The decision

Replace Smartlead with **Instantly Growth ($47/mo)**. Stack is now:

> **Attio + Make + Apollo + Instantly + Claude + Gumroad**

Verified against Instantly's current pricing and docs before adoption:

| | Growth $47 | Hypergrowth $97 |
|---|---|---|
| Connected email accounts | Unlimited | Unlimited |
| Email warmup | Unlimited | Unlimited |
| Campaign emails / month | **5,000** | 125,000 |
| Uploaded contacts | **1,000** | 25,000 |
| Webhooks | **No** | Yes |

All three of the facts this decision rested on check out: unlimited accounts and warmup on Growth,
separate per-account and per-campaign sending limits, and webhooks gated to Hypergrowth and above.

**Instantly is the right tool.** But not for the reason it was picked.

---

## B. Correction 1 — unlimited mailboxes does not unlock the 25-mailbox plan

The case for Instantly was: *unlimited email accounts matters because we're planning around
multiple sending inboxes.* That reasoning does not survive the other two limits.

**Growth's 5,000 campaign emails/month is 227/day across every mailbox combined.**

| Plan | Daily | Monthly | vs. Growth's 5,000 |
|---|---|---|---|
| 33 cold × 25 mailboxes | 825 | 18,150 | **3.6× over** |
| 30 cold × 25 mailboxes | 750 | 16,500 | **3.3× over** |
| 28 cold × 8 mailboxes | 224 | 4,928 | **0.99× — fits** |

Twenty-five mailboxes sharing 5,000 emails send **nine cold emails each per day**. That is less
than one healthy mailbox should carry, at 25× the DNS, warmup and maintenance work, for zero extra
throughput.

Unlimited mailboxes is free precisely because the meter is somewhere else. The binding constraint
moved from mailbox count to campaign volume, and the architecture has to follow it.

**Resolved: 8 mailboxes across 3–4 domains.** Growth's cap sizes the system to 8 at a 98% fit.

---

## C. Correction 2 — the budget omitted its largest line

The proposed budget was $79–$109/month, capped at $120, with *"Email/workspace: your existing
setup, $0 additional."*

Twenty-five cold-outreach mailboxes on ten dedicated domains are not an existing setup. **Instantly
does not sell the mailboxes.** "Unlimited email accounts" means Instantly charges nothing to
*connect* a mailbox; the mailbox itself is bought from Google, Microsoft or a mailbox provider at
$3–6 each per month.

`commercial-cleaning-os/automation/stack.md` had already recorded this: *"roughly $200–$400/month
once mailboxes are counted. The dominant cost is mailboxes, not software."*

| Architecture | Instantly | Make | Claude | Mailboxes | Domains | **Total** |
|---|---|---|---|---|---|---|
| 25 mailboxes, Growth | $47 | $12 | $25 | $150 | $10 | **$244** — and still 3.6× over the send cap |
| 25 mailboxes, Hypergrowth | $97 | $12 | $25 | $150 | $10 | **$294** |
| **8 mailboxes, Growth** | $47 | $12 | $25 | $24–48 | $5 | **$113–137** |

The $120 cap is a good discipline and it is nearly achievable — but only with 8 mailboxes, and only
at the cheaper end of mailbox pricing. It was never achievable with 25.

Both corrections point at the same architecture. The send cap and the budget cap independently
size this system to 8 mailboxes.

---

## D. Correction 3 — an internal contradiction in the ramp

The ramp was described as *"20 → 25 → 30 → 33 **total**/day with approximately 10–12 reserved for
warmup"*, and then multiplied as *"~33 **cold** sends × 25 mailboxes = ~825 cold emails/day."*

Those cannot both be true. If 33 is total and 11 is warmup, cold is 22 and the daily total is 550,
not 825. If 33 is cold, the per-mailbox total is 43–45 — above the ~40/day Instantly itself
recommends.

`research/03-funnel-math.md` reads 33 as **cold**, with warmup on top. Kept that reading, and
capped cold at **28/mailbox/day** so the per-mailbox total lands at 38 — inside Instantly's
guidance rather than just outside it.

---

## E. Confirmed correct, no change

**Webhooks: stay on polling, do not upgrade for real-time.** At 224 cold sends/day, reply volume is
a handful per day. A 15-minute Make poll against a same-business-day response SLA is ample. Correct
call.

**The domain rule.** The primary business domain never carries cold outbound. Now a §4 safety gate
in `revenue-engine`, alongside the existing gates — one addition: free-kit delivery and nurture are
*not* cold, and belong on the primary domain where sender reputation is worth building.

**Not buying Instantly's other products** — lead database, enrichment, verification, AI reply
agent, Instantly CRM, inbox placement, pre-warmed accounts. Apollo prospects, Attio is the CRM,
Claude reasons, Instantly executes. That boundary is what keeps the system understandable.

**Optimising for qualified prospects → engaged leads → page visits → purchases** rather than emails
sent. This is the same conclusion `building-distribution` reached from the other direction.

---

## F. The real reason Instantly wins

Not unlimited mailboxes — that is worth nothing against a 5,000-email cap.

**Because it charges nothing per connected mailbox, staged scaling is cheap.** Start at 8, warm
them, run Phase 1 (100 prospects) and Phase 2 (300–500) from `revenue-engine` §8. If the signal is
real, add mailboxes for only the provider's fee and upgrade the plan. If it is not, we spent $47
finding out.

Per-mailbox pricing would have penalised exactly the staged approach this project's build-order
discipline requires. Instantly does not. That is the argument.

---

## G. Consequence — outbound capacity fell, and distribution matters more

| | Before | After |
|---|---|---|
| Mailboxes | 24–25 | **8** |
| Daily cold at full ramp | 825 | **224** |
| **Contacts reachable in 90 days** | 6,800 | **~3,000** |

Bound by Instantly Growth's 1,000 uploaded contacts/month, which runs out before the send cap does.

At $197 and a $10,000 gross target — 51 sales — outbound now carries 8–15 of them instead of
17–34. The list must carry 36–43, which means **1,200–4,300 qualified free-kit downloads**, up
from 570–3,400.

**This is the right trade and it is not free.** Hypergrowth plus 25 mailboxes would buy the
capacity back for ~$169/month more. Do not spend it yet: buying 2.3× the capacity of a rate nobody
has measured is buying 2.3× of nothing known, and Growth covers both validation phases with room
to spare. The upgrade trigger is written into `stack.md` — the caps actually binding in a month,
*and* a measured positive reply rate.

---

## H. Price locked at $197

Stated as the current launch price and adopted. $149 is retired.

The distribution arithmetic supports it independently: at $197 the required download count is
roughly half what it is at $149. That was the largest single lever available and it has now been
pulled — which also means the cheap options are gone. Every remaining lever costs money.

**One correction on the target.** 51 × $197 = **$10,047 gross**, which is right. Platform fees take
roughly a tenth, so that is about **$9,042 net**. A $10,000 *net* target needs **57 sales**, not 51.
Worth deciding which number is the actual goal, because it is a 6-sale difference.

---

## I. What changed in the repo

| File | Change |
|---|---|
| `commercial-cleaning-os/automation/stack.md` | Rewritten: Instantly, plan limits, 8-mailbox architecture, ramp, domain rule, upgrade triggers, real budget |
| `commercial-cleaning-os/automation/make-jobs.md` | **New.** The eight scheduled jobs, with the approval gate in job 3 and polling in job 4 |
| `commercial-cleaning-os/crm/lifecycle-stages.md` | Instance A rebuilt: 7 → **10** stages (three documented changes from the 12 specified) |
| `.claude/skills/revenue-engine/SKILL.md` | Price locked $197; domain rule added to §4 safety gates; Instantly routing |
| `.claude/skills/building-distribution/` | Capacity 6,800 → 3,000 throughout; Growth vs Hypergrowth trade; gross vs net |
| `research/03`, `04`, `07`, `01` | Superseding pointers. Historical reasoning left intact. |
