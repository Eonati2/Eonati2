---
name: building-distribution
description: Plans and operates the distribution side of the Commercial Cleaning Client Acquisition OS — how strangers become free-kit subscribers and subscribers become buyers. Use when work touches traffic, audience, launch, list growth, lead-magnet promotion, communities, trade media, partnerships, affiliates, marketplace or Gumroad Discover traffic, content or SEO. Also use when someone asks how to reach a revenue target, how many sales or downloads are needed, why sales are not arriving, proposes a new channel, raises the revenue target, or assumes marketplace traffic will produce sales. Holds the distribution arithmetic, the ranked channel portfolio with per-channel ceilings and kill gates, and the rule that no passive channel exists.
---

# Building Distribution

The product is finished. Distribution is not. This skill owns the half of the business that turns
strangers into subscribers and subscribers into buyers.

Read `revenue-engine/SKILL.md` first — its conflict priority (§2), safety gates (§4), evidence
standard (§6) and voice standard (§7) all apply here without exception.

## 1. The finding this skill exists because of

**There is no passive channel. Every sale comes from traffic we create.**

Three specific consequences:

- **Gumroad Discover is a mirror, not a source.** Marketplace traffic tracks momentum a creator
  already generated elsewhere; it rarely moves the needle for an unknown seller. `research/12-decision-record-v4.md`
  named Gumroad's own marketplace traffic as one of three things that might close the revenue gap.
  It cannot. Two remain: the free product and organic distribution — and both are the same channel
  wearing different clothes, because organic distribution's job is to produce free-kit downloads.
- **Outbound is capacity-capped, not effort-capped.** Working harder does not raise it. The cap is
  mailbox arithmetic (`commercial-cleaning-os/automation/stack.md`).
- **So the binding constraint is list size, not product quality, not copy quality, not effort.**

When anyone in this project asks "how do we hit the number", the answer is a download count, not a
motivation.

## 2. The distribution equation

Work it in this order, every time. Never skip to channel tactics before the arithmetic is on paper.

```
REVENUE TARGET
  ÷ price                      = sales needed
  − (outbound capacity × contact→purchase rate)   = sales the list must carry
  ÷ list→purchase rate         = subscribers needed
  ÷ days in window             = downloads needed per day
```

Worked at current inputs — **every rate below is an assumption, not a measurement**:

| Input | Value | Status |
|---|---|---|
| Outbound contact capacity, 90 days | 6,800 contacts | Derived from mailbox caps. Structural. |
| Contact → purchase | 0.25%–0.5% | **Assumption.** Never validated by us. |
| Free-kit subscriber → purchase | 1%–3% | **Assumption**, floor of the published 1–5% email band. |
| Window | 90 days | Set by `research/13-90-day-blueprint.md` |

| Target | Price | Sales | Outbound can carry | List must carry | Subscribers needed | Per day |
|---|---|---|---|---|---|---|
| $10,000 | $149 | 68 | 17–34 | 34–51 | **1,100–5,100** | 13–57 |
| $10,000 | $197 | 51 | 17–34 | 17–34 | **570–3,400** | 6–38 |
| $12,000 | $149 | 81 | 17–34 | 47–64 | **1,570–6,400** | 17–71 |
| $12,000 | $197 | 61 | 17–34 | 27–44 | **900–4,400** | 10–49 |

Figures are **gross**. Platform fees reduce net by roughly a tenth; a net target needs the gross
target raised before it enters this table.

**Three things fall straight out of this table, and all three are decisions, not observations:**

1. Raising the revenue target raises the required download count roughly proportionally. A bigger
   number with no new channel is the same shortfall with a bigger gap.
2. Raising the price lowers the required download count roughly proportionally. At $197 the
   distribution job is roughly half the size it is at $149. That is an argument for $197 that is
   independent of every margin argument.
3. The low end of every band assumes the *optimistic* rate on both assumptions at once. Do not plan
   against the low end. Plan against the midpoint and treat the low end as upside.

**Recompute, never quote.** When price, capacity, window or a measured rate changes, rebuild the
table. See `references/distribution-math.md` for the procedure and the sensitivity analysis.

## 3. Channel portfolio

Ranked by what each can actually carry, not by how appealing it is. Full operating detail for each
is in `references/channel-playbooks.md`.

| # | Channel | Produces | Realistic ceiling | Lead time | Cost | Evidence status |
|---|---|---|---|---|---|---|
| A | Outbound email | Direct sales + downloads | 6,800 contacts / 90 days | Live now | Stack cost | Capacity structural; response rate unvalidated |
| B | Free kit as the outbound CTA | Subscribers | Converts A's same capacity | Immediate | None | Mechanism sound; rate unvalidated |
| C | Practitioner communities | Subscribers | Unknown — group sizes unverified | 2–6 weeks | Time only | Groups confirmed to exist; audience size not |
| D | Trade media / associations | Subscribers | Unknown — rate cards not obtained | 4–12 weeks | Paid | Publications confirmed; pricing and reach unknown |
| E | Partnerships / affiliates | Subscribers in blocks | Unknown | 3–8 weeks | Rev share | Untested |
| F | Search and content | Subscribers | Will not land inside 90 days | 6–12 months | Time | Asset, not a channel for this window |
| G | Gumroad Discover | Nothing reliable | **Treat as zero** | — | — | Researched: mirror, not source |

**Rules that bind the portfolio:**

- **Only A and B are live and ours.** Everything else is a hypothesis with a cost.
- **B is the single highest-leverage change available**, because it converts capacity we already
  pay for into an asset that compounds. A contact who buys is worth one sale. A contact who
  subscribes is reachable for every future offer. Making the free kit the primary outbound CTA
  costs nothing and raises nothing's risk.
- **G is zero.** Do not forecast it, do not build for it, do not let a plan depend on it. If
  marketplace sales appear, they are a bonus to report, never a line item to project.
- **F is not a 90-day channel.** Build content because it makes C and D work, and because it is
  worth owning in month six. Never count it in the table in §2.
- **Never run more than two unproven channels at once.** Three concurrent experiments produce no
  attributable signal, which is the same as running none.

## 4. The one metric

**Qualified free-kit downloads.** Everything above is instrumentation for this number.

Qualified means: a US commercial cleaning or janitorial operator with the capacity to service
recurring B2B accounts. A download from a residential cleaner, a student, or a competitor is a
download, not a qualified download. Track both; plan against the qualified count.

Secondary, in order: subscriber → purchase rate · cost per qualified download · reply quality from
outbound · channel attribution.

Do not report a rate without the sample size beside it. Under 100 downloads there is no rate, only
a count — say so plainly rather than dividing.

## 5. Channel gates

Every unproven channel enters with a written hypothesis, a cost ceiling, a review date, and a
number that ends it. No channel runs on hope past its review date.

| Gate | Rule |
|---|---|
| Entry | Written as: "*channel* should produce *N* qualified downloads in *D* days for *C* cost." Recorded before spend or effort begins. |
| Minimum honest test | Enough volume that the result is distinguishable from noise. For a download target under 30, the test cannot conclude anything — size up or don't run it. |
| Continue | Hit ≥50% of the hypothesised number, and cost per qualified download is at or under the ceiling. |
| Kill | Under 25% of the hypothesised number at the review date. Kill it. Do not extend, do not "optimise" a channel that produced nothing — optimising zero yields zero. |
| Grey zone | 25–50%: one extension, at most, with one changed variable. Then decide. |

A killed channel is written up in a sentence — what was tried, what it produced, why it stopped —
so it is not re-proposed in six weeks as a fresh idea.

## 6. Safety and conduct

Inherits every gate in `revenue-engine` §4. These are the ones distribution work breaks:

- **Communities are not send lists.** Participation means answering questions where the answer is
  useful with no link attached. Promotion happens only where group rules permit it, at the
  frequency they permit. Never post the same text to multiple groups. Never create a second account
  or a persona. State the affiliation when the product is mentioned — always.
- **No paid placement, sponsorship, domain, list rental or tool purchase without explicit
  confirmation from the user first.** Research the cost, present it, wait.
- **No affiliate or partnership commitment without confirmation.** A revenue share is a contractual
  commitment; that is on the human-approval list.
- **No scraped or rented email lists into outbound.** Only data the business is permitted to use.
- **Every claim about reach, audience size, or results is evidenced or labelled unknown.** A media
  kit's own circulation figure is vendor-published: cite it as such, never as a measured outcome.
- **Do not fabricate momentum.** No fake reviews, no manufactured testimonials, no invented download
  counts, no "join 500 other owners" until 500 other owners exist.

## 7. Operating cadence

Weekly, thirty minutes:

1. Qualified downloads this week, by channel. Cumulative against the §2 requirement.
2. Purchases this week. Recompute the measured list→purchase rate once n ≥ 100 — until then, count.
3. Any channel at its review date → apply §5, and write the sentence.
4. Recompute §2 with any rate that moved from assumption to measurement.
5. One question: is the gap closing at a rate that reaches the requirement inside the window? If no,
   the answer is a channel decision, not more effort in the existing ones.

Monthly: re-rank the portfolio. A channel that produced nothing twice does not stay on the list.

## 8. What this skill will not do

- Produce a forecast. The table in §2 is a requirements calculation — what would have to be true —
  not a prediction that it will be.
- Treat a revenue target as achievable because it was stated. Targets are inputs to arithmetic.
  If the arithmetic says the required download rate has no mechanism behind it, say that, in the
  same message, before anything else.
- Recommend paid acquisition as the answer to a distribution gap while the free channels are
  unmeasured. Paying for traffic before knowing what traffic converts is buying an unknown.
- Write customer-facing copy. Route that through `cleaning-os-voice` and the copy chain in
  `revenue-engine` §3.

## 9. Reference files

| File | Contents |
|---|---|
| `references/distribution-math.md` | Recomputation procedure, sensitivity analysis, worked scenarios, what each assumption would need to be true |
| `references/channel-playbooks.md` | Per-channel operating detail for A–G: what to do, what it costs, what ends it |
| `references/evaluations.md` | The evaluations this skill is held to |
