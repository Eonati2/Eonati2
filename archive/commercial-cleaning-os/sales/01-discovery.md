# 01 — Discovery

**Instance B.** The conversation between a reply and a walkthrough. Usually 8–15 minutes on the
phone.

**Its only job is to decide whether a walkthrough is worth doing** — for both sides. It is not a
pitch, and it is not the place to quote a price. Quoting before you have seen the building is how
cleaning companies lose money on contracts they won.

**CRM:** stage 5 `Conversation` → stage 6 `Walkthrough Scheduled`, or `Nurture` / `Disqualified`
with a reason code.

---

## 1. Open by naming why you contacted them

They replied to a message about a specific observed event. Start there — it is true, it is
specific, and it explains the call without a pitch.

> *"Thanks for getting back to me. I reached out because I saw you'd opened the MacArthur
> location back in August. I run a commercial cleaning company here in Irving. Is cleaning for
> that building something you've already got handled, or is it still being sorted?"*

That question is doing real work: it is the fastest legitimate route to whether a purchase window
exists, and it asks rather than assumes.

**Three answers, three paths:**

| They say | Path |
|---|---|
| "Still sorting it out" / "We're not happy with the current crew" | Continue to §2 |
| "We're covered, it's fine" | §5 — the graceful exit. Do not push |
| "Who is this again?" | Re-anchor on the event, offer to send details in writing, end |

---

## 2. What you actually need — eight things

Ask conversationally, not as a checklist read aloud. Capture all eight in the CRM afterward.

| # | What | Why it matters | Question |
|---|---|---|---|
| 1 | **Square footage** | The whole bid rests on it | *"Roughly how big is the space?"* |
| 2 | **Frequency** | Nightly vs 3× vs weekly changes everything | *"How often does it need cleaning?"* |
| 3 | **Current situation** | Incumbent, in-house, or nothing | *"How's it handled today?"* |
| 4 | **What prompted this** | The real motivation, in their words | *"What made you open this up?"* |
| 5 | **Decision process** | Who signs, who else is involved | *"Besides yourself, who'd be involved in deciding?"* |
| 6 | **Timing** | Real date, or vague | *"When would you want someone starting?"* |
| 7 | **Budget frame** | Range, not a number | *"Do you have a figure in mind, or should I put a proposal together?"* |
| 8 | **Special requirements** | Medical waste, security clearance, day porter, floor care, union | *"Anything unusual about the space I should know?"* |

**Question 4 is the one that changes the outcome.** *What made you open this up?* is the difference
between a bid and a conversation. If the answer is "the last crew kept missing the restrooms," your
proposal leads with quality control. If it's "we just moved in," it leads with a clean start and a
transition plan. Same building, completely different proposal.

**Question 5 is where deals die silently.** An office manager who cannot sign, in a conversation you
believed was with the decision-maker, wastes a walkthrough. Ask it plainly.

---

## 3. Disqualify early and say so

Ending a call at minute six is a win. A walkthrough costs 60–90 minutes plus drive time; that is
the scarce resource.

| Disqualify when | CRM code |
|---|---|
| Outside service area | `not_serviceable_geography` |
| Scope you cannot deliver (medical waste, high-rise glass, union site) | `not_serviceable_scope` |
| Under your economic floor | `too_small` |
| Corporate decides centrally | `chain_decides_centrally` |
| They want a price today and will not do a walkthrough | see below |
| Purely price-shopping a renewal to pressure an incumbent | `no_decision` in `Lost` |

**"Just give me a number over the phone."** Hold the line, once, and explain why:

> *"I could, but I'd have to pad it to cover what I can't see — and you'd be comparing a padded
> number to someone else's padded number. Fifteen minutes on site and I can give you a real one.
> When are you there this week?"*

If they refuse twice, they are shopping for a low number, not a vendor. `Nurture`, review in 90 days.

**The tell that saves the most time:** they will not name a decision-maker, a date, *or* a budget
frame. Any one is normal. All three means there is no live purchase.

---

## 4. Close to the walkthrough — the only ask

> *"Based on what you've described, I'd want to walk it before quoting anything. It takes about
> fifteen minutes and I'll have a proposal to you within two days. Does Tuesday morning or
> Thursday afternoon work better?"*

Two options, both specific. Then get it **in writing** — a confirmation email with date, time,
address, who you are meeting and your mobile number.

**Stage 6 requires written confirmation** (`../crm/lifecycle-stages.md` §2). A verbal maybe stays at
stage 5. Treating a verbal as booked is the single most common way this pipeline lies to its owner.

---

## 5. The graceful exit

When they are genuinely covered and content:

> *"Understood — sounds like you're in good shape. If it's useful I'll check back in six months in
> case anything changes. Either way, good luck with the new space."*

→ `Nurture`, `nurture_review_date` set, contract renewal date captured if they mention one.

**Existing provider is not a loss.** It is the normal state of a commercial building, and it is
exactly what the trigger model exists to time. Class 6 in `../crm/routing.md` §3.

---

## 6. Log it — same day

| CRM | Value |
|---|---|
| Activity | `type: meeting`, `channel: phone`, notes covering all eight items |
| Account | `est_sqft`, frequency, `est_monthly_value` (mark **estimated**) |
| Contact | `is_decision_maker` — **`confirmed` only if they said so** |
| Trigger_Event | If they named the real reason, add it with `trigger_source: discovery call <date>` |
| Stage | 6, `Nurture`, or `Disqualified` + reason |
| Next action | Required, with a date |

**What they told you about their own situation is now evidence** — properly sourced and dated, and
usable in the proposal. What you inferred is not. The distinction survives all the way to the
pre-send claim check.
