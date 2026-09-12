# Trigger Library

**A trigger is an event, not a conclusion.** It establishes that there may be a reason to make
contact now. It establishes nothing about whether a prospect has a cleaner, is unhappy with one, or
is shopping.

**Every trigger carries a source and a date, or it scores zero** (`../crm/schema.md` R3). Not
because the rule is tidy, but because unsourced triggers are exactly how fabricated claims get into
outreach copy.

Scoring authority is `../crm/scoring.md` §3. This file is the operational library: how to find each
one, how fresh it stays, and what may be said about it.

---

## The hierarchy

Facility events outrank inferred dissatisfaction and generic growth. **This deliberately overrides
the default weighting in the `trigger-finder` skill**, which ranks funding and hiring highly — a
funding round does not create a cleaning need, and a building someone just moved into does.

| Score | Tier | Triggers |
|---|---|---|
| **5** | High | New location · new facility · move / new occupancy · property-management change |
| **3** | Medium | Facilities or operations hiring · renovation or reopening · acquisition |
| **1** | Low | Generic growth · funding · generic hiring · review signals |

**Modifiers:** +1 second independent trigger (cap 5) · +1 if `freshness_days ≤ 30` ·
−2 if past the window · **0 if source or date is missing**.

---

## High tier — score 5

### T1 · New location opened
A second or additional site under an existing brand.

| | |
|---|---|
| **Find via** | New Google Business Profile under an existing brand name · "now open" banners on their site · local business-journal openings columns |
| **Window** | 120 days |
| **Evidence to store** | `GBP listing created 2026-08-14, 5910 N MacArthur Blvd, Irving` |
| **May say** | "Saw you opened the MacArthur location in August" |
| **May not say** | "You'll need a cleaner for the new site" · "your current cleaner won't cover it" |

### T2 · New facility / first occupancy
A business occupying a building for the first time.

| | |
|---|---|
| **Find via** | Certificate of occupancy and tenant-improvement permits on county or municipal portals · CRE listing status flipping to leased · permit aggregators (Shovels, BuildZoom, PermitPub) |
| **Window** | 90 days |
| **Evidence** | `TI permit #2026-04412 finaled 2026-08-02, City of Plano` |

**The strongest structural position in the industry.** There is no incumbent to displace — it is a
first purchase, not a switch. Where T1 and T2 co-occur, work the account first.

### T3 · Move / relocation
An existing business at a new address.

| | |
|---|---|
| **Find via** | GBP address change · address diffs between scrape snapshots · "we've moved" site notices · business-journal "on the move" columns |
| **Window** | 90 days |
| **Evidence** | `GBP address changed from 1200 Elm St to 400 Commerce St, observed 2026-08-20` |
| **Why it lands** | They are buying everything at once and want it off the list |

### T4 · Property-management change
A management company takes on a building, or a building changes managers.

| | |
|---|---|
| **Find via** | Portfolio-page diffs on management-company sites · CRE listing management changes · signage changes noted on site visits |
| **Window** | 90 days |
| **Evidence** | `Building added to Greystone portfolio page, first observed 2026-07-30` |
| **Why it ranks 5** | New managers review inherited vendors, and one relationship can expose several buildings |

---

## Medium tier — score 3

### T5 · Facilities or operations hiring
A role posted that owns vendor relationships.

| | |
|---|---|
| **Find via** | Indeed and LinkedIn posts for Facilities Manager, Office Manager, Operations Manager, Building Manager |
| **Window** | 90 days |
| **Evidence** | `Indeed post "Facilities Manager", published 2026-09-02` |
| **May say** | "Saw you're hiring a facilities manager" |
| **May not say** | "your new facilities manager will want to change vendors" |

**Two-edged.** A new facilities manager may review vendors — or may be too new to change anything
for six months. Worth contacting, not worth over-reading.

### T6 · Renovation or reopening
| | |
|---|---|
| **Find via** | Renovation permits · "reopening" announcements · temporary-closure notices on GBP |
| **Window** | 60 days |
| **Note** | Post-construction cleaning is a distinct, often larger, one-off scope. Price it separately |

### T7 · Acquisition
| | |
|---|---|
| **Find via** | Local business journals · press releases · ownership changes in state registries |
| **Window** | 120 days |
| **Note** | Vendor consolidation follows acquisitions, in both directions — you may win or lose |

---

## Low tier — score 1

### T8 · Generic growth · T9 · Funding · T10 · Generic hiring
Real signals of activity, weak signals of a cleaning need. A funded software company has more
money; it does not have a dirtier office. Use only as a stacking modifier on a higher trigger, or as
filler when the priority list is thin.

### T11 · Review signals — **demoted from 5 to 1**

Cleaning-related complaints in public reviews: "dirty", "restrooms", "not clean", "cleaning crew".

**Why it was demoted.** An earlier version of this library scored it 10 on the argument that it is a
business publicly stating its cleaner is failing. That reasoning does not hold. A review saying the
bathrooms were filthy does **not** establish that the business controls the cleaning contract, that
the reviewer is an employee rather than a customer, that the issue is current, or that anyone is
looking for a vendor. It is an inference about dissatisfaction, not an observation of a purchasing
window.

**Its real use is as a modifier stacked on an event trigger** (`../crm/scoring.md` §3): a business
that just moved *and* has restroom complaints is a materially stronger row than either alone. It is
free and abundant, which makes it useful — and makes it tempting to over-weight.

**Never quote a review back to a prospect.** It reads as surveillance, and it asserts a conclusion
about their vendor that you cannot support.

---

## Instance A — triggers for finding cleaning companies

Different question: not "does this facility need cleaning" but "is this cleaning company trying to
grow commercial work right now."

| Trigger | Signal | Find via |
|---|---|---|
| **Hiring a salesperson** | Investing in commercial growth | Indeed / LinkedIn: "Sales", "Business Development" at a cleaning company |
| **New commercial services page** | Repositioning toward commercial | Site diffs |
| **Expanding service area** | Growth posture | GBP service-area changes |
| **Hiring cleaners at volume** | Capacity ahead of contracts | Multiple crew postings |
| **Running Google Ads** | Already paying for acquisition, already convinced | Ad presence on commercial cleaning terms |

**Running paid ads is the strongest Instance A signal.** It proves budget and intent already exist —
the conversation is about a better channel, not about whether to invest at all.

---

## Detection cadence

| Trigger | Method | Frequency |
|---|---|---|
| T1, T3 · GBP changes | Snapshot diff | Weekly |
| T2, T6 · permits | Portal or aggregator query | Weekly |
| T4 · portfolio pages | Page diff | Fortnightly |
| T5, T10 · job posts | Keyword query by metro | Weekly |
| T7, T9 · news | Business-journal scan | Fortnightly |
| T11 · reviews | Review scrape | Monthly |

**Freshness is the whole asset.** A 100-day-old occupancy permit is not a trigger, it is history —
and outreach referencing it reads as either careless or creepy. Re-score weekly and let expired
triggers fall out.

---

## The claim table

What each trigger licenses you to say, and what it does not. The pre-send claim check
(`../crm/routing.md` §6, check 6) tests merged copy against this.

| Observed | May say | May **not** say |
|---|---|---|
| New GBP listing | "Saw you opened the second location" | "You need a cleaner there" |
| Occupancy permit | "Saw the new building on Commerce cleared occupancy" | "You don't have a cleaner yet" |
| Address change | "Noticed you moved to Commerce Street" | "Your old cleaner won't follow you" |
| Portfolio addition | "Saw you picked up the Elm Street building" | "The inherited vendor won't work out" |
| Facilities job post | "Saw you're hiring a facilities manager" | "They'll want new vendors" |
| Review complaint | *nothing — do not reference it* | anything |

Everything in the right column is a conclusion. Conclusions do not go in the CRM and they never go
in outreach.
