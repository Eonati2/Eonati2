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

**Status:** built, not yet running. Sequences in `commercial-cleaning-os/outbound/sequences/instance-a.md`.
Sending layer is **Instantly Growth** (`commercial-cleaning-os/automation/stack.md`).

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

**Hypothesis:** asking for a free-kit download converts more of the same 3,000 contacts than asking
for a $149 purchase, and every converted contact stays reachable for every future offer instead of
being spent once.

**What to do:** make the Prospecting Starter Kit (`free-product/`) the primary call to action in
the outbound sequence. Keep a direct-purchase path for replies that ask for it. Do not run both
CTAs in the same email — one ask per email.

**Why this matters more than it looks:** a contact who buys is worth one sale. A contact who
subscribes is an asset that compounds across every future send, and is the only mechanism in the
plan that produces the subscribers §2 requires. Without B, outbound spends capacity and leaves
nothing behind.

**Measurement:** contact → download rate, and download → purchase rate, tracked separately from
contact → purchase. Three rates, three denominators. Never blend them.

**Kill gate:** none. If the download rate is poor, that is information about the kit or the email,
and both are fixable. Reverting to a direct-purchase-only CTA throws away the compounding.

---

## C — Practitioner communities

**Status:** unproven. Confirmed to exist; audience size unverified.

**Hypothesis:** commercial cleaning operators congregate in a small number of named online
communities, and consistent useful participation produces qualified downloads at zero cash cost.

**Confirmed to exist** (September 2026, via public search — **membership figures not verified, do
not cite any**):

| Venue | Type |
|---|---|
| Commercial Cleaning Company Community | Facebook group |
| Commercial & Residential Cleaning Business Owners | Facebook group |
| Janitorial Business Mastermind | Facebook group |
| Cleaning Business Forum | Facebook group |
| Scale My Cleaning Business | Facebook group |
| Blue Collar Millionaire | Facebook group, broader trades |
| Cleaning Talk Forum | Standalone forum |
| The Commercial Cleaner's Forum | Standalone forum |

Verify each is active and admits the right membership before investing time in it. A group that
exists is not a group with the right people in it.

**What to do:**

1. Join, read for a week, learn each group's promotion rules. They differ and they are enforced.
2. Answer questions where the answer is genuinely useful and no link is attached. This is the
   majority of the work and there is no shortcut through it.
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

**Hypothesis:** the janitorial trade press and associations reach commercial cleaning contractors
at scale, and a newsletter placement or article produces qualified downloads at a known cost.

**Confirmed to exist:**

| Organisation | What it is |
|---|---|
| BSCAI — Building Service Contractors Association International | The association specifically for commercial cleaning contractors. Closest audience match of anything found. |
| ISSA | Cleaning and facility solutions association; publishes *ISSA Today* and several e-newsletters |
| Trade Press Media Group / CleanLink | Publishes *Contracting Profits*, *Sanitary Maintenance*, *Facility Cleaning Decisions*; operates CleanLink |

**BSCAI is the best-matched audience found in any channel.** It is contractor-specific rather than
supplier- or distributor-oriented, which most of the jan/san press is. Investigate it first.

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

**Hypothesis:** other people already hold the attention of US commercial cleaning owners, and a
revenue share buys access to a list in one block rather than one contact at a time.

**Who holds these audiences:** cleaning-business consultants and coaches · janitorial software
vendors (bidding, scheduling, inspection tools) · supply distributors · franchise brokers ·
cleaning-industry podcasters and newsletter operators.

**What to do:** identify who has an audience and no competing product. A software vendor selling
scheduling tools is not a competitor to a client-acquisition system; a consultant selling their own
client-acquisition coaching is.

**Hard constraint:** a revenue share is a contractual commitment. It sits on the human-approval
list in `revenue-engine` §4. **Propose, never commit.**

**Kill gate:** three partnership conversations that do not convert to a live arrangement → the
positioning is not obviously valuable to audience-holders, which is itself a finding worth having.
Stop and report it rather than making a fourth attempt.

---

## F — Search and content

**Status:** not a 90-day channel. Build it anyway, for the right reason.

**Hypothesis:** written material on trigger-based prospecting for cleaning contractors earns search
traffic — in six to twelve months.

**Why build it now despite that:** content is what makes C and D work. A forum answer is better
with something to point at. A trade publication wants a contributed article, not an ad pitch. The
content is infrastructure for the other channels before it is ever a channel itself.

**What to do:** write from the product's actual substance — the trigger library, the ICP work, the
decision-maker research. That material already exists and is already verified. Do not commission new
research to fill a content calendar.

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
| LinkedIn outbound | The buyer is an owner-operator of a cleaning company. Presence and activity on the platform are not established for this segment. Verify before investing, do not assume. |
| Rented or purchased email lists | Excluded by the data rules in `revenue-engine` §4. |
| A second product to broaden the funnel | Excluded by the single-product decision in `research/12-decision-record-v4.md`. Distribution problems are not solved by building more product. |
