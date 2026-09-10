# 06 — Compliance & Deliverability

In 2026 these stopped being separate topics. The mailbox providers now enforce most of what the law
asks for, and the penalty moved from "spam folder" to "rejected." Treat this file as the operating
licence for the whole plan.

---

## 1. Non-negotiables

### Domain architecture
| Rule | Detail |
|---|---|
| **Never send from your primary domain** | Cold email burns sender reputation. Your product domain must stay clean forever — it's where buyers go and where receipts come from. |
| **Never send from `eonati2.github.io` or the logo-design property** | Unrelated brand, shared subdomain reputation, and a confusing story for anyone who checks. |
| Buy **6 dedicated sending domains** | Close cousins of the brand, `.com` where possible. ~$12/yr each. |
| 4 mailboxes per domain, max | Concentration on one domain is a reputation single-point-of-failure |
| Each sending domain 301-redirects to the product domain | So a curious prospect who types it in lands somewhere real |
| Warm every mailbox **21 days** before real sends | Non-negotiable. This is why week 1–3 exists in the plan. |

### Authentication — all three, passing and aligned
| Record | Setting |
|---|---|
| **SPF** | Publish, include your sender, one record per domain |
| **DKIM** | 2048-bit, per-domain key |
| **DMARC** | Start `p=none` with `rua` reporting, move to `p=quarantine` after 2 clean weeks |
| **One-click unsubscribe** | RFC 8058 `List-Unsubscribe` + `List-Unsubscribe-Post` headers. Required by Google, Yahoo, Apple; recommended by Microsoft. |
| **rDNS / PTR** | Handled by the provider on shared infrastructure — verify anyway |

### Volume discipline
| Metric | Limit | Action if breached |
|---|---|---|
| **Spam complaint rate** | **<0.1%** target, **0.3% hard ceiling** | Above 0.3% → throttling. Above 0.5% → delivery failure. Pause everything and audit copy + list. |
| Hard bounce rate | <2% | Above 3% → verification is broken. Stop, re-verify. |
| Sends per inbox per day | 28, ramping from 5 over the warmup | Never spike |
| Daily total | ~672 across 24 inboxes | |

**The 0.3% number in practice:** at 672 sends/day, **two complaints in a day puts you at 0.3%.** That
is how thin the margin is, and it is the real argument for the gift-first approach — people don't
mark "want a free list of prospects in your city?" as spam nearly as often as they mark a pitch.

---

## 2. CAN-SPAM — the seven duties

US B2B cold email needs **no prior consent** — the most permissive regime in the world. But every
message must satisfy all seven:

| # | Duty | How you satisfy it |
|---|---|---|
| 1 | Truthful header info | Real From name, real domain, working Reply-To |
| 2 | Non-deceptive subject line | Subject must reflect the message. **This is the one states can still sue over.** |
| 3 | Identify the message as an ad | The footer does this |
| 4 | **Valid physical postal address** | Street address, USPS-registered PO box, or CMRA private mailbox. Budget $15/mo if you don't want your home address in 18,000 emails. |
| 5 | Clear opt-out mechanism | One-click header + a plain-English line in the footer |
| 6 | Honor opt-outs within **10 business days** | Automate it to be immediate. Never charge, never require more than one step, never ask for information to unsubscribe. |
| 7 | You're liable for anyone you hire | If you outsource sending, their violation is your violation |

**Penalty: up to $53,088 per email** (FTC 2026 adjustment), each message a separate violation.
At 18,000 sends, a systematic violation is not a survivable event. This is a cheap thing to get
exactly right and a catastrophic thing to get casually wrong.

### The footer (every send, verbatim shape)
```
—
{{sender_name}}, {{business_name}}
{{street_address}}, {{city}}, {{state}} {{zip}}

You're getting this because {{company}} appears as a commercial cleaning
company in {{metro}}. Reply "no thanks" and I'll remove you immediately.
```
Plain, human, no unsubscribe-link theatre. It satisfies duties 3–5 and reads like a person, which
is also the lowest-complaint form of a footer.

### State law
CAN-SPAM preempts state email statutes (15 U.S.C. §7707) — **except** laws prohibiting falsity or
deception. Two consequences:
- **California B&P §17529** gives residents a **private right of action at $1,000 per email** for
  deceptive commercial email. California is a large share of any US list.
- The protection is simple: **never misrepresent anything in a header or subject line.** Everything
  in `05-email-sequences.md` is literally true, and that's deliberate.

### GDPR
Not engaged as long as you target US businesses only. **Recommendation: stay US-only for the first
60 days.** Adding UK/EU/Canada means GDPR legitimate-interest assessments and CASL's consent regime
(CASL is genuinely strict — express or implied consent required). There is no shortage of US
prospects; going international buys risk and no revenue.

---

## 3. TCPA — the phone channel (added in v2)

Adding phone as a channel moves you under a second, stricter regime. CAN-SPAM compliance buys you
nothing here.

**This is a layered regime, not a rule of thumb.** An earlier version of this file reduced it to
"landline safe / mobile illegal." That framing was too categorical, and it also predated a change
that matters.

| Layer | What it does |
|---|---|
| **FTC DNC provisions** | Most B2B solicitation calls remain exempt — *except* sellers of nondurable office or **cleaning supplies** |
| **FTC TSR, as amended March 2024** (effective 16 May 2024; recordkeeping from 15 Oct 2024) | **Now reaches B2B telemarketing.** Prohibits material misrepresentations and false or misleading statements made to induce payment, and **expands recordkeeping** — call detail records, seller-relationship records, DNC-compliance records |
| **TCPA / FCC** | Separate regime. Restricts autodialed and artificial/prerecorded calls to **wireless** numbers absent required consent. Private right of action, **$500–$1,500 per call** |
| **State mini-TCPA statutes** | Stack on top, with their own consent rules and calling windows |

**What this means in practice:** the 2024 TSR amendment removed the assumption that B2B calling sits
largely outside the FTC's reach. Misrepresentation rules and recordkeeping duties now apply to
business-to-business calls, and the recordkeeping obligation is operational — it requires you to
*keep records*, which is a system, not a policy.

### Why this bites this plan specifically
Google Maps listings for small local businesses are overwhelmingly **mobile numbers**. Owner-operated
cleaning companies list a cell as the business line as a matter of course. The channel being added
is aimed at precisely the number type that carries the exposure, sourced from precisely the dataset
that produces it.

### The operating position
**Phone outreach is a separate legal workstream, not a setting.** Before dialling: classify the
number, determine which federal and state rules apply, keep suppression *and call* records, and
prohibit automated or prerecorded outreach unless counsel has confirmed the legal basis.

Concretely:
1. **Manual dialling only** until counsel says otherwise. No autodialer, power dialer, prerecorded
   drop, or AI voice agent.
2. **Line-type lookup on every number before it reaches a dial list.** Fractions of a cent, and it
   is what lets you apply the right rules to the right number.
3. **Wireless and unknown numbers get the strict treatment** — manual, business hours local.
4. **Records, not just suppression.** The 2024 TSR recordkeeping duty means call detail and
   DNC-compliance records are part of the build from day one, not a later clean-up.
5. **One suppression list across email and phone**, permanent, shared across all domains.
6. **Ship this in the product — as a workstream, not a bright line.** Teaching customers "landline
   safe / mobile illegal" would hand them false confidence in a line that does not exist. The
   honest version is a differentiator; the crisp version is a liability.

**Counsel review is a prerequisite for the phone channel**, including the TSR nondurable
cleaning-supplies carve-out, which sits uncomfortably close to this industry.

---

## 4. What the product must teach (this is a selling point, not a disclaimer)

You are selling an outbound system to people who will use it on *their* prospects. If they blow up
their domains using your product, your refund rate and your reputation go with them.

**Include a compliance module and put it in the sales copy.** Every competitor's free playbook
skips this, which makes it a differentiator rather than fine print:

- The CAN-SPAM seven, in plain language, with a copy-paste compliant footer
- Warmup schedule and why 21 days
- SPF/DKIM/DMARC setup walkthrough for Google Workspace and Microsoft 365
- The 0.3% rule and how to actually monitor it
- Suppression-list hygiene across multiple domains
- **Never send from your main business domain** — the mistake most cleaning companies would make
  on day one, and the one that would cost them their actual customer email

**Framing on the sales page:** *"Built to keep your main domain safe. Most cleaning companies who
try cold email do it from the domain their customers email them at. That mistake takes about three
weeks to become permanent."* That sentence sells the product and prevents your worst support burden
at the same time.

---

## 5. Position on the ethics, stated plainly

Everything here is public business data — Google Maps listings, company websites, Secretary of State
filings, building permits, public job posts, public reviews. All of it is lawful to collect and
lawful to use for US B2B outreach.

The line worth holding, and it's a commercial argument as much as an ethical one:

| Do | Don't |
|---|---|
| Contact a business about its business | Contact people at personal addresses about non-business matters |
| Send because something specific changed | Blast because an address existed |
| Remove instantly on request, permanently, everywhere | Re-add from a "fresh" list six weeks later |
| Say true things in headers and subjects | Fake a re-thread with `Re:` on a first contact |
| Send 672/day to relevant people | Send 50,000/day to everyone |

The complaint-rate ceiling of 0.3% means the spray-and-pray version of this business is not just
unpleasant, it is **mechanically self-terminating** under the 2026 rules. The restrained version is
the only one that survives, which is a rare and convenient alignment between doing this well and
doing it right.
