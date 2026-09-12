# Channel Playbooks

Operating detail for channels A–G in `SKILL.md` §3. Each carries an entry hypothesis, what to
actually do, the cost, and the number that ends it.

## Contents

- [A — Outbound email](#a--outbound-email)
- [B — Free kit as the outbound CTA](#b--free-kit-as-the-outbound-cta)
- [C — Practitioner communities](#c--practitioner-communities)
- [D — Trade media and associations](#d--trade-media-and-associations)
- [E — Partnerships and affiliates](#e--partnerships-and-affiliates)
- [F — Search and content](#f--search-and-content)
- [G — Gumroad Discover](#g--gumroad-discover)
- [Channels deliberately excluded](#channels-deliberately-excluded)

---

## A — Outbound email

**Status:** infrastructure built, sequences to be rewritten for the CRE buyer.
Sending layer is **Instantly Growth** (`automation/stack.md`).

**What it produces:** direct purchases, and — once B is in place — subscribers.

**Ceiling: 3,000 contacts across 90 days.** Two caps, and the platform one binds first:

- Instantly Growth allows **1,000 uploaded contacts/month** → 3,000 in the window.
- 8 mailboxes at 28 cold/day = 224/day = ~4,928/month, just inside Growth's **5,000 campaign
  emails/month**.

This is platform and mailbox arithmetic, not ambition. Raising it means a Hypergrowth upgrade
(+$50/mo) *and* more mailboxes (+$3–6 each) *and* new domains with three weeks of warmup — money,
time, and confirmation before any purchase.

**Operating rules:** everything in `revenue-engine` §4 and
`research/06-compliance-and-deliverability.md`. Human approval on every live send. Complaint rate
ceiling 0.3%, target 0.1%. Warmup volume comes out of the same daily cap, not on top of it.

**Kill gate:** outbound does not get killed — it is the spine. But if reply quality after 500
contacts shows the offer is not landing, that is an offer problem surfacing through this channel,
and it routes to `revenue-engine` §8 validation discipline, not to a channel decision.

---

## B — Free kit as the outbound CTA

**Status:** the highest-leverage unbuilt change. Costs nothing.

**Hypothesis:** asking for a Rent Roll Lite download converts more of the same 3,000 contacts than
asking for a $199 purchase, and every converted contact stays reachable for every future offer instead of
being spent once.

**What to do:** make Rent Roll Lite (`rent-roll-os/offers/lite.md`) the primary call to action in
the outbound sequence. Keep a direct-purchase path for replies that ask for it. Do not run both
CTAs in the same email — one ask per email.

**Why this matters more than it looks:** a contact who buys is worth one sale. A contact who
subscribes is an asset that compounds across every future send, and is the only mechanism in the
plan that produces the subscribers §2 requires. Without B, outbound spends capacity and leaves
nothing behind.

**Measurement:** contact → download rate, and download → purchase rate, tracked separately from
contact → purchase. Three rates, three denominators. Never blend them.

**Kill gate:** none. If the download rate is poor, that is information about Lite or the email,
and both are fixable. Reverting to a direct-purchase-only CTA throws away the compounding.

---

## C — Practitioner communities

**Status:** unproven, but the best-evidenced unproven channel we have. **Test this one first.**

**Hypothesis:** US commercial property managers belong to a small number of named professional
associations with local chapters, and useful participation plus chapter presence produces
qualified downloads at low cash cost.

| Organisation | What it is | Size |
|---|---|---|
| **BOMA International** | Building Owners and Managers Association. Local chapters in most major metros. | **30,000+ members** (organisation-published, as of May 2024) |
| **IREM** | Institute of Real Estate Management. Property managers specifically, commercial and residential. | Not verified |
| CCIM, NAIOP | Investment and development oriented — adjacent, further from our buyer | Not verified |

**This is a real improvement over what the previous product had.** Its best community evidence was
eight Facebook groups whose membership could not be verified at all. Here the membership is
published, the chapters are local and named, and the events are in a public calendar.

Two cautions. Membership figures are **organisation-published** — cite them as such and verify
before planning against them. And 30,000 BOMA members are not 30,000 prospects: the association
includes owners, service providers and vendors, and most members are outside our 5–150 lease band.

**What to do:**

1. Join, read for a week, learn each group's promotion rules. They differ and they are enforced.
2. Answer questions where the answer is genuinely useful and no link is attached. This is the
   majority of the work and there is no shortcut through it. Local chapter events are the other
   half, and they are not free — check the cost before committing.
3. Mention the kit only where rules permit, at the frequency they permit, always with the
   affiliation stated.
4. Never post identical text to two groups. Never run a second account or a persona.

**Cost:** time. Realistically several hours a week, sustained, before anything happens.

**Entry hypothesis to record:** *N* qualified downloads in 30 days across *k* groups.

**Kill gate:** under 25% of *N* at 30 days → stop, write the sentence, do not extend. Community
work that is not producing is a hobby with a business justification attached.

**The real risk here is not failure, it is a ban.** One promotional post in the wrong group ends
access to that audience permanently. Read the rules first, every time.

---

## D — Trade media and associations

**Status:** unproven. Publications confirmed; rate cards not obtained; reach not verified.

**Hypothesis:** CRE trade media reaches commercial property managers at scale, and a newsletter
placement or contributed article produces qualified downloads at a known cost.

**Confirmed to exist:**

| Organisation | What it is |
|---|---|
| BOMA and IREM publications and chapter newsletters | Reach the same audience as channel C, in a different format |
| CRE trade press and newsletters | Not yet surveyed. Do this before assuming a rate card is out of reach. |

**Channel C should be worked before D here.** The associations are the audience; their media is a
paid route to the same people. Establish whether the audience responds before renting access to it.

**What to do — in this order:**

1. Request media kits. Do not guess at pricing; media-kit circulation figures are vendor-published
   and must be cited as such.
2. Check whether an editorial or contributed-article path exists. It is usually free, and for an
   unknown seller it is usually better than an ad, because it carries the publication's credibility
   rather than renting its attention.
3. Present cost and claimed reach to the user. **Wait for confirmation before any spend.**

**Cost:** unknown until step 1. Assume it is the most expensive channel here.

**Kill gate:** if a placement runs and produces under 25% of the hypothesised downloads, no second
placement with the same publication.

---

## E — Partnerships and affiliates

**Status:** untested.

**Hypothesis:** other people already hold the attention of US commercial property managers, and a
revenue share buys access to a list in one block rather than one contact at a time.

**Who holds these audiences:** CRE newsletter operators · property-management consultants ·
accounting and CAM-reconciliation firms serving CRE · smaller proptech vendors whose product does
not overlap · CRE podcasters.

**What to do:** identify who has an audience and no competing product. **Lease administration
software vendors are not partners** — we occupy the step before their purchase, which makes us
either a threat or a lead source depending on how it is framed, and neither is a stable footing.

**Hard constraint:** a revenue share is a contractual commitment. It sits on the human-approval
list in `revenue-engine` §4. **Propose, never commit.**

**Kill gate:** three partnership conversations that do not convert to a live arrangement → the
positioning is not obviously valuable to audience-holders, which is itself a finding worth having.
Stop and report it rather than making a fourth attempt.

---

## F — Search and content

**Status:** not a 90-day channel. Build it anyway, for the right reason.

**Hypothesis:** written material on rent roll and lease-expiry management earns search traffic — in
six to twelve months.

**And here the keyword data is unusually encouraging for a change:** `rent roll template` runs
880/mo at difficulty 15, `excel rent roll template` 320/mo at 15, `lease abstract template` 140/mo
at difficulty 15 with a **$14.35 CPC**. Low difficulty and real commercial intent. That is a better
SEO position than the previous product ever had — which raises F from "build it anyway" to "build
it deliberately", while still keeping it out of the 90-day table.

**Why build it now despite that:** content is what makes C and D work. A forum answer is better
with something to point at. A trade publication wants a contributed article, not an ad pitch. The
content is infrastructure for the other channels before it is ever a channel itself.

**What to do:** write from the product's actual substance — how the six tabs work, what a notice
deadline is and why it is the expensive date, how to read rollover concentration. Do not commission
new research to fill a content calendar.

**Never count F in the §2 table.** Any 90-day plan that relies on SEO is a plan that misses.

---

## G — Gumroad Discover

**Status:** researched, and the finding is negative.

Marketplace traffic amplifies momentum a seller already has. For an unknown seller with no
sales history and no external audience, it does not produce meaningful volume. The mechanism runs
the wrong way round: sales produce Discover placement, Discover placement does not produce the
first sales.

**Treat as zero in every forecast.** Set the product up properly on the platform — category, tags,
description, the full asset list — because it costs an hour and there is no reason to be sloppy.
Then plan as though it contributes nothing.

If marketplace sales do appear, report them as a bonus. Never retrofit them into a projection.

---

## Channels deliberately excluded

| Channel | Why not |
|---|---|
| Paid ads | Buying traffic before knowing what traffic converts. Excluded until the list → purchase rate is measured. Also excluded by the locked stack in `revenue-engine` §9. |
| Cold calling at scale | Higher legal risk. The FTC's 2024 Telemarketing Sales Rule amendment extends to B2B telemarketing. Separate, gated workstream — see `research/06-compliance-and-deliverability.md`. Manual human calls only, by default. |

| Rented or purchased email lists | Excluded by the data rules in `revenue-engine` §4. |
| A second product to broaden the funnel | Excluded by the single-product decision, which survived the pivot. **Distribution problems are not solved by building more product — that lesson is the whole reason `research/16` exists.** |
