# 02 — The Offer and the Product

## 1. The ICP, narrowed to something you can actually write copy for

> **A US commercial cleaning company with 3–25 employees, an active website, at least one commercial
> service page, and a named owner or sales lead — that is currently winning work by referral and
> word of mouth, and wants recurring contracts it can forecast.**

**Buyer:** Owner / Founder / President (primary). Sales Manager or Business Development Manager
(secondary, in the 15–25 employee band).

**Explicitly out of scope:** solo residential cleaners (no budget, no commercial motion),
franchises (the franchisor controls marketing), companies with 100+ employees (they have a sales
team and buy agencies, not systems).

**Geographic wedge — first 10 metros.** Pick for trigger density, not population: Dallas–Fort Worth,
Houston, Austin, Phoenix, Atlanta, Charlotte, Nashville, Tampa, Orlando, Raleigh–Durham. High
business formation and commercial construction means more new-lease and new-location triggers, which
is the raw material of the whole offer.

**The disqualifier that saves you money:** no website → no commercial intent → skip. It's the
cheapest filter you have and it removes most of the 1.26M tail in one pass.

---

## 2. Product name

# The Walkthrough Engine
### *A trigger-based system for booking commercial cleaning walkthroughs*

**Why this name.** The walkthrough is the unit of currency in this industry — it's the thing that
becomes a bid, which becomes a contract. Owners count walkthroughs the way SaaS counts demos.
Naming the product after the metric the buyer already tracks means the name does the positioning
work before they read a word of copy. "Client Acquisition OS" is agency language; "walkthrough" is
*their* language.

---

## 3. Positioning — the one sentence

> **Most cleaning companies email every business in town and get ignored. The Walkthrough Engine
> finds the 20–40 businesses in your city that have a reason to change cleaners *this quarter* —
> and gets you in the door while that reason is still fresh.**

**The wedge:** everyone else sells *volume* (bigger lists, more sends, more tools). You sell
*timing*. Commercial cleaning contracts are sticky; a business with a cleaner they tolerate will not
switch for a better email. It switches when something changes — a move, an expansion, a new
facilities hire, a service failure. Nobody in this market is selling timing. Everybody is selling
volume, and the market is saturated with volume.

**The reason to believe:** you hand them 23 timing-matched prospects *before* they pay you anything.

---

## 4. What's actually in the product

Ordered by how much of the price each part justifies. Note that "information" is deliberately at
the bottom — the free agency blogs already own that layer.

### Tier A — The parts nobody can copy from a blog post (build these first)

**A1. The Trigger Board (the core IP).** A defined taxonomy of 11 switch-triggers with, for each
one: the exact public data source, the query or scrape recipe, how to score it, its freshness
window, and the email angle that matches it. This is the product. Full spec in
`04-data-and-trigger-pipeline.md`.

**A2. The 500-Prospect Starter List, built for their metro.** Not a generic database dump — built
to their ICP, deduped, verified, with decision-maker name and title where findable, and every row
carrying its trigger and trigger date. *This is what makes it worth $197 instead of $29.*

**A3. The Automation Blueprint.** An importable n8n/Make workflow JSON: Apify → Google Sheets →
enrichment → verification → trigger scoring → sequencer → reply routing → suppression. Importable,
not describable. Ship the file.

**A4. The Proof Pack Generator.** The same mechanism you use on them, packaged for them to use on
their prospects — build a "here are 20 facilities near you with a reason to switch" artifact for any
zip code. Teaching them to run *your* play on their own market is the most defensible thing in the
box, and it's the reason the product has a story.

### Tier B — Conversion assets (high perceived value, cheap to make, genuinely useful)

**B1.** Trigger-matched email sequences — 6 sequences × 4 emails, one per trigger type
(new-lease, expansion, facilities-hire, service-failure, property-manager, medical-office).
**B2.** The Walkthrough Booking Script — reply → phone → walkthrough scheduled.
**B3.** The Walkthrough-to-Bid Kit — what to measure on site, the bid worksheet, the proposal
structure with Good/Better/Best pricing tiers.
**B4.** Objection cards — "we already have a cleaner," "send me a price," "we're under contract,"
"budget's set for the year."
**B5.** The Decision-Maker Map — who actually signs, by facility type (office / medical / property
mgmt / school / industrial), and how to reach each without going through a receptionist.
**B6.** Deliverability Checklist — SPF/DKIM/DMARC, warmup schedule, the 0.3% rule, one-click
unsubscribe, the CAN-SPAM seven.

### Tier C — Information (build last, keep short)

**C1.** The 30-Day Implementation Plan — one page per day, checkbox format.
**C2.** Pricing & Bidding quick reference — the per-sqft table from `01-market-evidence.md §C`.
**C3.** Metrics dashboard (Google Sheet) — sends, replies, positive replies, walkthroughs, bids,
contracts, and the resulting cost per contract.

> **Scope discipline.** Do not write a 300-page anything. The buyer is an owner-operator who reads
> email on a phone in a truck. Every asset is a template, a checklist, a spreadsheet, or a file they
> import. If a section can't be acted on in under 10 minutes, cut it.

---

## 5. The price ladder

| | **Engine** | **Engine + Build** | **Done-For-You** |
|---|---|---|---|
| **Price** | **$197** | **$497** | **$1,497** |
| System, sequences, blueprint, all assets | ✅ | ✅ | ✅ |
| Starter prospect list | 500, their metro | 500, their metro | 2,000, their metro |
| Trigger-matched & scored | ✅ | ✅ | ✅ |
| Setup call | — | 45 min | 90 min + weekly for 4 weeks |
| Campaign built for them | — | Sequences loaded & personalized | Full build: domains, inboxes, warmup, sequences, sending |
| First 30 days run for them | — | — | ✅ |
| **Expected mix** | ~60% | ~30% | ~10% |

**Blended AOV at that mix: ~$390.** Model conservatively at **$260–$300** — early buyers skew to the
cheap tier before you have testimonials.

### Why $197 and not $149
1. **The Google Ads frame.** They pay $197–$230 for *one lead*. At $197 the system costs less than
   one lead — a comparison so favorable you should print it on the page. At $149 you gain nothing;
   the comparison is already won at $197.
2. **Gumroad's fee floor.** ~12.9% + $0.80 means $149 nets $129 and $197 nets $170. At the volumes
   this funnel produces, that $41/sale is roughly **$1,600 across the run.**
3. **Cheap reads as thin here.** You are selling against a $647/yr membership and $600–$5,000/mo
   retainers. A $149 price tag next to a done-for-you campaign signals "ebook."
4. **Fewer, better customers.** Every sale in this model costs real outbound work. Optimize revenue
   per positive reply, not units.

### Launch mechanics
- **Founding price $147 for the first 20 buyers**, then $197. Real scarcity, honestly counted,
  and it gives your week-4 emails a reason to exist.
- **Order bump at checkout: +$97 for "your metro's 500-prospect list built this week."** Order bumps
  routinely take 20–30% attach and cost you ~$0.75 in Apify credits.
- **No Gumroad Discover.** 30% vs ~12.9%. Every buyer arrives through your domain.
- **7-day refund policy, stated plainly.** Gumroad keeps its fee on refunds, so a refund costs you
  more than the sale earned — but refusing refunds in a niche this small-world costs more than that.

---

## 6. Sales page structure (order matters)

1. **Headline:** *Book commercial cleaning walkthroughs with the 20–40 businesses in your city that
   have a reason to switch this quarter.*
2. **The proof, immediately** — a live sample table: 8 real businesses, city, trigger, trigger date,
   decision-maker title, why now. Redact the names; the *shape* of the data does the selling.
3. **The price frame** — "One Google Ads lead costs a cleaning company $197–$230. This is the whole
   system, once, for $197."
4. **The problem, in their words** — "You're emailing every office in town. They already have a
   cleaner. They're not switching because your email was nicer."
5. **The mechanism** — the 11 triggers, shown as a board, not described in prose.
6. **What's in the box** — asset list with file formats and counts. Concrete beats adjectives.
7. **The ROI math** — one $600/mo office = $7,200/yr against a $197 one-time cost.
8. **The ladder** — three columns, Engine pre-selected.
9. **The origin story** — *"I built this to sell this. The email that brought you here was produced
   by the system you're looking at."* Then show the actual trigger row that selected them. Nobody
   else in this market can make that claim, and it is verifiable on the spot.
10. **Refund policy, contact, real postal address** (CAN-SPAM needs it and it builds trust).

**On the domain:** put this on your own domain, not on `eonati2.github.io` and not on gumroad.com.
A janitorial-growth product sitting on a logo-design site's GitHub Pages subdomain will cost you
credibility with a buyer who is already suspicious of marketers. Buy a dedicated domain for it,
and — critically — **never send cold email from it** (see `06`).
