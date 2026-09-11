# Evaluations

What this skill is held to. Each evaluation is a real prompt, the behaviour that counts as a pass,
and the specific failure this skill exists to prevent.

Run these after any edit to `SKILL.md` or either reference file. A change that breaks one of these
is a regression, not an improvement.

## Contents

1. [E1 — The raised target](#e1--the-raised-target)
2. [E2 — The marketplace assumption](#e2--the-marketplace-assumption)
3. [E3 — Why aren't we getting sales](#e3--why-arent-we-getting-sales)
4. [E4 — The new channel proposal](#e4--the-new-channel-proposal)
5. [E5 — The premature rate](#e5--the-premature-rate)
6. [E6 — The community shortcut](#e6--the-community-shortcut)
7. [Scoring](#scoring)

---

## E1 — The raised target

**Prompt:** "Let's target $15,000 instead of $10,000."

**Pass:**
- Recomputes the table with `revenue_target = 15000` at both prices, both rate bands.
- States plainly that raising the target changes only the requirement — nothing in the equation's
  capability side moves.
- Names the new required download count and per-day rate, and compares it to what the live channels
  currently produce (currently: nothing).
- Does not refuse, moralise, or stall. Delivers the arithmetic, states the consequence, and asks
  what changes on the capability side — or proceeds on a stated assumption.

**Fail:**
- Accepts the target and produces a plan without recomputing.
- Produces encouragement, or a "stretch goal" framing.
- Refuses to work with the number.

**Failure this prevents:** a bigger number treated as a bigger capability.

---

## E2 — The marketplace assumption

**Prompt:** "Once the product is live on Gumroad, how much will Discover traffic bring in?"

**Pass:**
- Answers: plan for zero.
- Gives the mechanism — marketplace placement follows sales, sales do not follow placement — not
  just the conclusion.
- Notes that `research/12-decision-record-v4.md` named marketplace traffic as one of three possible
  gap-closers, and that this finding removes it, leaving two.
- Still recommends setting the listing up properly, because it is cheap.

**Fail:**
- Estimates a number.
- Says "it depends" without committing to the planning treatment.
- Leaves the §2 table implying marketplace contribution.

**Failure this prevents:** a forecast resting on traffic nobody controls.

---

## E3 — Why aren't we getting sales

**Prompt:** "We've been live three weeks and sold two copies. What's wrong with the product?"

**Pass:**
- Reframes to the distribution equation before diagnosing the product.
- Asks for, or computes, how many qualified people actually saw the offer. If the number is small,
  says so: two sales from a small audience is not evidence about the product, it is an absence of
  evidence.
- Refuses to compute a conversion rate on a denominator under 100. Reports counts instead.
- Only after establishing audience size does it consider offer, price or copy.

**Fail:**
- Proposes copy or price changes first.
- Computes "2 sales ÷ 40 visitors = 5%" and reasons from it.
- Suggests building more product.

**Failure this prevents:** rebuilding a finished product to fix a traffic problem, and drawing
conclusions from samples too small to carry them.

---

## E4 — The new channel proposal

**Prompt:** "I think we should try TikTok."

**Pass:**
- Does not dismiss it and does not simply agree.
- Requires the §5 entry gate: hypothesised qualified downloads, cost ceiling, review date, kill
  number — written before effort starts.
- Checks the two-unproven-channels-at-once rule and says which existing experiment would have to
  stop.
- Notes what is unknown: whether the buyer — a US commercial cleaning owner-operator — is reachable
  there. Says it is unverified rather than asserting either way.

**Fail:**
- Enthusiastic agreement with a tactical plan and no gate.
- Flat refusal.
- Adds it as a third or fourth concurrent experiment.

**Failure this prevents:** channel sprawl, where several unmeasured efforts run at once and none
produces attributable signal.

---

## E5 — The premature rate

**Prompt:** "We got 40 downloads and 1 sale. So the list converts at 2.5% — at that rate we need
2,700 downloads."

**Pass:**
- Says there is no rate at n = 40. One sale in forty is consistent with a true rate anywhere from
  well under 1% to well over 5%.
- Does not carry the 2.5% into the requirement table.
- Says what sample size would make the rate usable, and what to do meanwhile: keep the assumption
  band, keep counting.
- Does not treat the correction as discouragement — the 40 downloads are real and the direction is
  right.

**Fail:**
- Accepts 2.5% and plans against it.
- Updates the §2 table with a measured-looking figure derived from one sale.

**Failure this prevents:** an assumption laundered into a measurement by one data point, which then
propagates through every downstream number.

---

## E6 — The community shortcut

**Prompt:** "Write a post I can drop into all eight cleaning Facebook groups today."

**Pass:**
- Declines the identical-text-to-eight-groups part specifically, and says why: it is the fastest
  route to a permanent ban from the best-matched free audience available.
- Offers what does work: read the rules first, participate usefully before promoting, one venue at
  a time, affiliation stated.
- Does not lecture. States the constraint in a sentence or two and then helps with the version that
  works.

**Fail:**
- Writes the eight-group blast.
- Refuses to help with community outreach at all.
- Writes a lengthy warning and no usable alternative.

**Failure this prevents:** burning the only zero-cost audience on the fastest possible mistake.

---

## Scoring

Six evaluations. A change to this skill must leave all six passing.

Two behaviours run through every one of them and are what the skill is really for:

1. **Arithmetic before narrative.** Every distribution question resolves to a number of people who
   have to see the offer. Get to that number first.
2. **Assumptions stay labelled.** Two of the six inputs are unmeasured. Any output that hides that
   is wrong even when the number is right.
