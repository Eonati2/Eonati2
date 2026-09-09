# 04 — Data & Trigger Pipeline

Two pipelines, and confusing them is the most common way this kind of project dies.

- **Pipeline 1 — YOUR prospects:** commercial cleaning companies you email. Volume: ~6,400.
- **Pipeline 2 — THEIR prospects:** facilities with a reason to switch cleaners. This is the Proof
  Pack, and it is *also the product's core deliverable*. Volume: ~25 per pack, built on demand.

Pipeline 2 is the interesting one. It's your demo, your differentiator, and what you're actually
selling. Build it first — you can't sell a system you haven't run.

---

## Pipeline 1 — Building your list of cleaning companies

### Stage 1: Discovery (Apify, Google Maps)
Queries, run per metro across the 10 target metros:

```
commercial cleaning company · janitorial service · office cleaning service
commercial janitorial · building maintenance cleaning · medical office cleaning
industrial cleaning service · facility cleaning services
```

**Cost:** ~$4/1,000 places. 10 metros × 8 queries × ~120 results ≈ 9,600 raw → **~$38**.

### Stage 2: Qualification filters (this is where most of the value is)
Apply in this order — cheapest, most-eliminating filter first.

| # | Filter | Keep if | Removes |
|---|---|---|---|
| 1 | Has a website | yes | ~35% (the residential/solo tail) |
| 2 | Commercial intent | site mentions commercial / office / janitorial / facility | ~30% of remainder |
| 3 | Not a franchise | domain isn't a known franchise (Jan-Pro, Coverall, ServiceMaster, Vanguard, Anago, Stratus, Buildingstars, Corvus, Office Pride, JAN-PRO) | ~8% |
| 4 | Size band | 3–25 employees — infer from team page, review volume, fleet/service-area claims | ~20% |
| 5 | Alive | reviews within last 12 months | ~10% |
| 6 | Not already sophisticated | no visible SDR team / no "careers: sales" page | ~3% |

**Realistic yield: ~9,600 raw → ~2,500–3,000 qualified.** Run 3 metro batches to reach 6,400.
Budget ~$120 in Apify credits for the full list. Plan on scraping ~25,000 raw places total.

### Stage 3: Decision-maker enrichment
Cascade, cheapest first — stop as soon as you have a name:
1. **Website scrape** — About / Team / Leadership page. Highest hit rate for this segment and
   effectively free.
2. **Google Business Profile owner responses** — owners frequently sign review replies by name.
   Consistently underused and free.
3. **State Secretary of State business registry** — registered agent / officer names. Free, public,
   and unusually reliable for small operators.
4. **LinkedIn** — company page → people → filter Owner/President/Founder/Sales Manager.
5. **Apollo / enrichment tool** — last, not first.

**On Apollo:** treat it as *verification*, not *discovery*, for this segment. The known failure mode
with small local businesses is that it returns generic `info@` inboxes rather than the owner. Google
Maps → website → named human is the better path here, and Apollo confirms and pattern-matches the
address.

**Expect ~55–70% named-human coverage.** Route the rest as follows rather than discarding them:

| Coverage | Route |
|---|---|
| Named owner + verified personal work email | **Segment 1** — full trigger treatment |
| Named owner, email guessed by pattern | Verify first; if risky, route to Segment 2 |
| Generic `info@` only | **Segment 2** — short, plain, forwardable copy written *for the person who forwards it* |
| No email at all | Drop. LinkedIn/phone if you have spare capacity, but don't build a second machine. |

`info@` is not worthless — it's a black hole *only when the email assumes it's reaching the owner*.
Write those to be forwarded and they earn their place.

### Stage 4: Verification (never skip)
Verify 100% before sending. Catch-all domains get one extra-cautious pass. **Hard bounce rate must
stay under 2%; over 3% and you're burning domains.** Verification costs cents and protects an asset
worth hundreds.

---

## Pipeline 2 — The Trigger Board (the actual IP)

Eleven triggers. For each: the source, how you get it, freshness window, score, and the email angle.

| # | Trigger | Signal | Source & method | Fresh | Score |
|---|---|---|---|---|---|
| **T1** | **New commercial lease / move-in** | Business at a new address | CoStar/LoopNet listing status flips; local business-journal "on the move" columns; GBP address change; USPS-format address diffs in scrape snapshots | 0–90d | **10** |
| **T2** | **New location opened** | 2nd/3rd branch | GBP new listing at same brand; "now open" site banners; local press | 0–120d | **10** |
| **T3** | **Certificate of Occupancy / tenant-improvement permit** | Buildout finishing → cleaning needed at handover | County/municipal permit portals; Shovels/BuildZoom/PermitPub for coverage | 0–60d | **9** |
| **T4** | **Facilities/office manager hired** | Someone now owns the vendor relationship — and reviews vendors | Indeed/LinkedIn job posts: "Facilities Manager," "Office Manager," "Operations Manager" | 0–90d | **9** |
| **T5** | **Cleaning complaint in reviews** | Incumbent failing, in writing | Google reviews containing "dirty," "restroom," "not clean," "cleaning crew," "trash" | 0–60d | **10** |
| **T6** | **New business registration** | New entity, no vendors yet | Secretary of State filings (most states publish; several have bulk downloads) | 0–120d | **8** |
| **T7** | **Property manager acquires/lists a property** | One relationship → many buildings | CRE listing sites; property-manager site "our portfolio" page diffs | 0–90d | **9** |
| **T8** | **Headcount growth** | More people → more mess → more frequency | Multiple open roles at one location on Indeed/LinkedIn | 0–60d | **7** |
| **T9** | **Funding / expansion announcement** | Budget exists | Local business journals, press releases | 0–120d | **7** |
| **T10** | **Incumbent cleaner shows distress** | Contract in play | Competitor's GBP goes to "permanently closed"; sudden negative-review cluster | 0–90d | **8** |
| **T11** | **Franchise/multi-site rollout** | Repeatable multi-contract | Brand's locations page diff | 0–180d | **8** |

**Scoring:** highest single trigger score, +2 for any second trigger, +1 if within 10 miles of the
cleaning company, +1 for a named decision-maker. **Contact at 9+. Nurture at 6–8. Ignore below 6.**

### The two that matter most, and why
**T5 (cleaning complaints in reviews)** is the strongest and the most underused. It is a business
telling you, in public and in writing, that its current cleaner is failing. It is free to collect
via Google reviews, and it converts because the pain is present-tense.

**T1 + T3 together (new lease + occupancy permit)** identify a business that will need a cleaner on
a known date and doesn't have one yet. That's not a switch — it's a first purchase, with no
incumbent to displace. Structurally the easiest win in the industry.

### Cost of a Proof Pack
| Item | Cost |
|---|---|
| 25 places, one metro slice | $0.10 |
| Review scrape for T5 | $0.05 |
| Permit/registry lookups | free |
| Job-post scrape for T4 | $0.05 |
| **Per pack** | **≈ $0.20** |
| **200 packs across the campaign** | **≈ $40** |

**Build packs only for people who reply.** That single rule is what makes the economics absurd:
your most impressive sales asset costs twenty cents and is only produced for people who asked.

---

## The automation architecture

```
                 ┌─ PIPELINE 1: your prospects (batch, weekly) ─┐
Apify Google Maps ─→ Google Sheets (raw)
   └→ filter/qualify script ─→ Sheets (qualified)
        └→ enrichment cascade (site → GBP → SoS → LinkedIn → Apollo)
             └→ email verification ─→ Sheets (verified)
                  └→ segment split: Segment 1 (trigger) / Segment 2 (broad)
                       └→ Smartlead campaigns

                 ┌─ PIPELINE 2: proof packs (on demand, per reply) ─┐
Positive reply detected (Smartlead webhook)
   └→ n8n: read city + radius from the contact record
        └→ Apify: businesses in radius, by target facility type
             └→ trigger enrichment (reviews T5, permits T3, jobs T4, GBP diffs T1/T2)
                  └→ score, keep top 20–25
                       └→ render PDF/Sheet "Proof Pack — {City}"
                            └→ draft reply email with pack attached (HUMAN SENDS)

                 ┌─ CONVERSION ─┐
Pack sent ─→ 48h follow-up ─→ walkthrough call ─→ ladder offer
   └→ purchase ─→ Gumroad ─→ delivery + onboarding sequence ─→ 14-day DFY upsell
   └→ no reply ─→ nurture (weekly trigger digest for their city)
   └→ unsubscribe ─→ global suppression (all domains, permanent)
```

**One deliberate manual step:** a human reviews and sends every proof-pack reply. It is the highest-
value 90 seconds in the funnel — that's where a $197 sale becomes a $1,497 sale. Automate the
building of the pack; never automate the sending of it.

**Suppression is global and permanent.** One shared suppression list across every domain and
campaign. An unsubscribe that gets re-emailed from a second domain is the fastest route to a
complaint rate above 0.3%, and under the 2026 rules that means rejection, not the spam folder.

---

## The build order (do not reorder this)
1. **Trigger Board for one metro, by hand.** No automation. Build 5 proof packs manually. If they
   aren't impressive when you build them by hand, no amount of n8n will save them.
2. **Pipeline 2 semi-automated** — the pack is the product; it has to be good before it's fast.
3. **Pipeline 1 discovery + qualification.**
4. **Enrichment cascade.**
5. **Sequencer wiring and reply routing.**
6. **Full automation** — only after ~20 packs have been built by hand and you know what "good" is.

The instinct is to build the automation first. Resist it. You cannot automate a judgment you haven't
formed yet, and the judgment here — *what makes a trigger convincing* — is the entire product.
