# 14 — The Distribution Gap
**Date:** 2026-09-11 · Status: **finding recorded, correction applied to `12`**

Record 12 concluded that $10,000 in 90 days is not defensible for outbound alone, and named three
things that could close the gap. One of them has now been researched and does not survive.

---

## A. The finding

**Gumroad Discover is a mirror, not a source.**

Marketplace placement follows sales history and external momentum; it does not create the first
sales. For a seller with no sales history and no external audience, it is not a channel. Published
accounts of how Discover behaves are consistent on this: it amplifies momentum a creator already
generated elsewhere.

This is the mechanism, not just an observation about volume. The causality runs the wrong way for
someone starting from zero.

---

## B. What it corrects in `12`

Record 12 §"What this means, stated plainly" reads:

> It becomes reachable only if the free product, organic distribution and **Gumroad's own
> marketplace traffic** carry a meaningful share — none of which we have any evidence for yet.

Three named gap-closers. **One is now removed.** Two remain, and they are less independent than the
sentence implies: organic distribution's entire job is to produce free-product downloads, so the
two are one mechanism described twice.

**The corrected statement:** the gap closes only if the free product acquires a subscriber base,
and organic distribution is the only thing that can acquire it. There is no second route and no
passive one.

`12` is left as written — it is a dated record. This file is the correction that supersedes that
passage.

---

## C. What the gap actually is, in units

Not "more marketing". A number of people.

Working the requirement equation at current inputs — outbound capacity 6,800 contacts over 90 days,
contact→purchase assumed 0.25–0.5%, subscriber→purchase assumed 1–3%:

| Target | Price | Sales needed | Outbound can carry | List must carry | Qualified downloads needed | Per day |
|---|---|---|---|---|---|---|
| $10,000 | $149 | 68 | 17–34 | 34–51 | **1,100–5,100** | 13–57 |
| $10,000 | $197 | 51 | 17–34 | 17–34 | **570–3,400** | 6–38 |
| $12,000 | $149 | 81 | 17–34 | 47–64 | **1,570–6,400** | 17–71 |
| $12,000 | $197 | 61 | 17–34 | 27–44 | **900–4,400** | 10–49 |

Gross, before platform fees. **Both rates are assumptions.** Neither has ever been measured by us,
and the low end of each band assumes the optimistic value on both at once.

Three consequences:

1. **Raising the target raises the required download count roughly proportionally.** Nothing else
   in the equation moves. A larger target is the same shortfall with a larger gap.
2. **Raising the price lowers it roughly proportionally.** At $197 the distribution job is about
   half the size it is at $149. This is a distribution-side argument for $197 that is independent
   of every margin argument, and it is input to the unresolved launch-price decision.
3. **The binding constraint is list size** — not product quality, not copy quality, not effort.
   The product is complete and verified. Nothing currently running produces a single download.

---

## D. What changed as a result

**`building-distribution`** — project-authored skill, 2026-09-11. Holds the requirement equation,
the ranked channel portfolio with per-channel ceilings, and the channel entry/kill gates. Wired
into `revenue-engine` §3 as the route for any question of the form "how do we hit $X" or "why
aren't we getting sales".

Channel portfolio as assessed, in `.claude/skills/building-distribution/references/channel-playbooks.md`:

| Channel | Planning treatment |
|---|---|
| Outbound email | Live. Capacity-capped at 6,800 contacts. |
| **Free kit as the outbound CTA** | **Highest-leverage unbuilt change. Costs nothing.** Converts capacity already paid for into an asset that compounds. |
| Practitioner communities | Unproven. Eight venues confirmed to exist; membership sizes unverified. |
| Trade media / associations | Unproven. BSCAI is the best-matched audience found anywhere. Rate cards not obtained. No spend without confirmation. |
| Partnerships / affiliates | Unproven. Propose only — a revenue share is a contractual commitment. |
| Search and content | Not a 90-day channel. Build as infrastructure for the others. |
| Gumroad Discover | **Zero.** |

---

## E. Status

The product side is finished. The distribution side has one live channel with a hard ceiling, one
free improvement to it that has not been made, and five hypotheses with no evidence behind any of
them.

That is not a reason to lower the target. It is the reason the target needs a mechanism attached to
it before it means anything.
