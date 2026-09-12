# 03 — The Proposal

**Instance B.** Sent within 48 hours of the walkthrough. **CRM:** stage 7 → stage 8 `Proposal Sent`.
Requires `proposal_ref` and `amount`.

**What a proposal is for:** making it easy to say yes, and making a price comparison harder than
one number against another. Most janitorial proposals are a price and a task list, which trains the
buyer to shop on price alone. Yours should give them something else to compare.

---

## 1. Structure — seven sections, two to four pages

Two to four pages. A twelve-page proposal does not read as thorough; it reads as padded.

### 1. Cover — one page
Their company, their building address, the date, your company, your contact details. Nothing else.

### 2. What we understood
**Their words, back to them.** Three or four sentences drawn from discovery and the walkthrough.

> *"You moved into the MacArthur building in August and need nightly service across roughly 4,200
> square feet, with particular attention to the restrooms and the entry glass. You mentioned the
> thing that would make you call is a restroom that hasn't been touched."*

**This is the most important section and almost nobody includes it.** It proves you listened, and
it frames everything after it against *their* problem rather than your service list.

Every sentence here must trace to something they actually said — discovery notes or walkthrough
Activity. Nothing inferred. Same standard as outreach copy.

### 3. Scope of work
Specific and countable. Not *"restrooms cleaned and sanitized"* but:

> **Restrooms (2)** — nightly: fixtures cleaned and disinfected, mirrors, partitions spot-cleaned,
> floors mopped, all dispensers restocked, waste removed.
> **Weekly:** partitions fully wiped, grout detail, vents dusted.

Break out by area and frequency. If it is not written here, it is not in the contract — and that
protects both of you.

### 4. What is not included
Floor restoration · carpet extraction · window exteriors · post-construction · biohazard ·
day porter — whichever apply, with the price if they want them added.

**Stating exclusions plainly builds more trust than omitting them.** It also prevents the argument
in month three that ends the contract.

### 5. Three options — Good / Better / Best

| | **Essential** | **Standard** ← recommended | **Complete** |
|---|---|---|---|
| Frequency | 3× weekly | 5× weekly | 5× weekly + day porter |
| Restrooms | 3× | Nightly | Nightly + midday check |
| Floor care | Quarterly buff | Quarterly buff + annual strip/wax | Monthly buff + 2× strip/wax |
| Glass | Monthly | Twice-weekly entry detail | Weekly all interior |
| Supplies | Client provides | **Included** | Included |
| Inspections | — | Monthly with written report | Monthly + quarterly review |
| **Monthly** | $X | **$Y** | $Z |

**Mark the middle one recommended and say why in one line.** Three options change the buyer's
question from *"is this too expensive?"* to *"which of these do I want?"* — and that is a better
question for both of you.

Price the tiers on real cost differences. Fake tiers designed to make the middle look good are
transparent to anyone who has bought this service before.

### 6. How it works
Start date · transition plan for the first two weeks · who your supervisor is and their mobile ·
inspection cadence and what the report contains · how they raise an issue and your response time ·
insurance and bonding, with the certificate attached · background-check policy.

**The response-time commitment does more work than anything else on the page.** Most complaints
about cleaning companies are about responsiveness, not cleaning.

### 7. Terms
Monthly price and what triggers a review (occupancy change, scope change) · term and notice period
· payment terms · a plain-English cancellation clause.

**Offer a 30-day out.** It costs you almost nothing — a buyer who wants to leave will leave — and
it removes the largest objection to switching vendors.

---

## 2. Delivery

**Email the PDF and say you will call.** Do not attach and vanish; do not phone without sending.

> *"Proposal attached for the MacArthur building. Three options — I've marked the one I'd
> recommend and why. I'll give you a call Thursday to walk through it, or reply any time if
> something's unclear."*

Then **actually call on Thursday.** The call is where questions surface. Emailed proposals that
nobody follows up on are how deals go quiet.

---

## 3. Claims discipline

Everything about *them* must trace to evidence. Everything about *you* must be true.

| Never | Instead |
|---|---|
| "Your current cleaner is failing" | "You mentioned the restrooms have been inconsistent" — only if they said it |
| "We guarantee 100% satisfaction" | State the actual remedy: response time, re-clean policy |
| Invented client names or logos | Real references, with permission, or none |
| A made-up statistic | Your own numbers, or nothing |
| "Award-winning" without an award | Omit |

No fabricated testimonials, case studies, or metrics — the same standard as everything else in this
system. In a market where owners talk to each other, an invented reference is found out.

---

## 4. Log it

| CRM | Value |
|---|---|
| Stage | 8 `Proposal Sent` |
| Account | `proposal_ref`, `amount` (the recommended tier) |
| Activity | `type: send`, proposal reference, which tier recommended |
| Next action | "Follow-up call", dated — **normally 2 business days** |

---

## 5. After it lands

| They say | Do |
|---|---|
| Questions on scope or price | → stage 9 `Negotiation` |
| "We're going with someone else" | → `Lost`. **Ask what the difference was, and log the answer** |
| Silence | Follow-up cadence in `05-follow-up-cadence.md` |
| "Not now, but keep in touch" | → `Nurture` with a review date |

**Always ask why on a loss, and record the answer as a code**
(`../crm/lifecycle-stages.md` §2). Free-text loss reasons make loss analysis impossible. A pattern
of `price` losses means your cost model or your targeting is wrong; a pattern of
`incumbent_retained` means your triggers are firing too late. You cannot see either without codes.
