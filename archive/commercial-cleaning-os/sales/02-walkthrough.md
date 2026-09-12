# 02 — The Walkthrough

**Instance B. The central event in this business.** Everything upstream exists to produce one, and
everything downstream is priced from what you record here.

**Two jobs, in this order:** (1) gather enough to price the job accurately and profitably;
(2) become the vendor they want to hire. Most operators do the first and forget the second — then
compete on price, because they gave the buyer nothing else to compare.

**CRM:** stage 6 → stage 7 `Walkthrough Complete`. Scope notes and measurements are the exit
criteria. **A walkthrough with no captured measurements did not happen.**

---

## 1. Before you go — 10 minutes

- [ ] Re-read the discovery notes. Know what they said prompted this.
- [ ] Know the trigger and its date. Reference it once, naturally.
- [ ] Confirm the appointment the morning of. No-shows are a scheduling failure, not bad luck.
- [ ] Bring: measuring wheel or laser, phone camera, the checklist below, insurance certificate, two business cards.
- [ ] Know your floor. The walk-away number, decided in advance and not in the room.

**Arrive early enough to see the building the way a visitor does.** The lobby, the entrance glass,
the parking area. That is the impression their clients form, and it is often the thing the buyer
most wants fixed.

---

## 2. Measure and record

Numbers first, because the bid depends on them and memory does not.

| Capture | Detail |
|---|---|
| **Total cleanable sqft** | Not gross leased. Exclude what you will not clean |
| **Floor breakdown by surface** | Carpet · hard floor · tile · specialty. Each cleans at a different rate |
| **Restrooms** | Count, fixture count, traffic level |
| **Kitchen / breakroom** | Count, whether dishes and appliances are in scope |
| **Entrances and glass** | Interior glass, entry doors, partition glass |
| **Trash points** | Desk-side count, central collection, dumpster location and distance |
| **Occupancy** | Headcount and pattern — the real driver of restroom and trash load |
| **Access** | Keys, codes, badge, alarm, after-hours procedure |
| **Storage** | Is there a closet for supplies, or does everything travel? |
| **Existing equipment** | What stays, what you supply |

**Photograph everything.** Time-stamped photos on the day protect you twice: they document
pre-existing damage, and they make the proposal specific in a way competitors' won't be.

### The five things that quietly destroy margin

Ask about every one. Each is a common source of a job that priced fine and lost money.

1. **After-hours access reality** — a security desk that closes at 7pm turns a 9pm clean into an
   overtime problem.
2. **Elevator access** — no service elevator, or one that needs booking, adds real time per visit.
3. **Dumpster distance and access** — a shared dumpster 200 yards away with a locked gate is not the
   same job as one at the back door.
4. **Day-porter expectations that were never stated** — "occasionally someone spills something in
   the lobby" means an unplanned daytime visit.
5. **Floor care assumptions** — strip-and-wax or carpet extraction quietly assumed to be included in
   the monthly. Establish now whether it is in scope or billed separately.

---

## 3. While you walk — become the vendor

The buyer is deciding whether they trust you, and they are deciding it here.

**Point out one specific thing nobody else will mention.** Not a criticism of the incumbent — a
professional observation:

> *"The entry glass takes the worst of the traffic here. If we're doing nightly, I'd put that on a
> twice-weekly detail rather than the standard wipe. It's the first thing your clients see."*

**Ask what has gone wrong before.** *"What's the thing that would make you call me?"* The answer is
the single most useful sentence in the whole sale, and it goes verbatim into the proposal.

**Never criticize the incumbent.** It reads as sales talk, and the buyer may have hired them. Talk
about what you would do, not about who failed.

**Say what you cannot do.** If they want floor restoration and you subcontract it, say so on site.
Discovering it after a signature costs the relationship.

---

## 4. Set expectations before you leave

Three sentences, always the same:

> *"I'll have a written proposal to you by Thursday. It'll have three options so you can see the
> trade-offs. If anything's unclear, call me — my mobile's on the card."*

Then ask the two questions that determine what happens next:

1. *"Are you getting other quotes?"* — normal, expect it, and it tells you what you are next to.
2. *"What's your timeline for deciding?"* — sets your follow-up cadence honestly.

**48-hour SLA on the proposal** (`../crm/lifecycle-stages.md` §4). Competitors are bidding the same
week, and the operator who sends first while the walk is fresh has a real advantage.

---

## 5. Price it — the method

Two independent methods. **If they disagree by more than about 20%, one of your inputs is wrong.**
Find out which before you send anything.

### Method A — labour build-up (the real one)
```
production rate (sqft/hour, by surface and density)
  → hours per visit
  → × visits per month
  → × fully loaded labour cost (wage + taxes + insurance + workers' comp)
  → + supplies + equipment amortization + travel
  → + overhead allocation
  → + target margin
  = monthly price
```

### Method B — per-square-foot sanity check
Reference ranges from market research (`../../research/01-market-evidence.md` §C) — these are
**market observations, not your costs**:

| Segment | Range |
|---|---|
| Standard office | $0.07–$0.15/sqft (wider band $0.05–$0.25) |
| Medical / healthcare | $0.25–$0.35/sqft |
| Schools / daycare | $0.10–$0.20/sqft |
| Billed labour hour | $35–$65 |

**Method A governs. Method B only tells you whether A produced something the market will accept.**
Pricing off per-sqft alone is how operators win contracts they lose money on — the ranges say
nothing about your drive time, your access constraints, or your wage rates.

### Sanity checks before you send
- Does it clear your walk-away floor?
- Have you priced floor care separately, or deliberately included it?
- Is the first month different (initial deep clean)? Say so explicitly.
- What happens if occupancy grows 30%? Put a review trigger in the terms.

---

## 6. Log it — same day, before the details fade

| CRM | Value |
|---|---|
| Stage | 7 `Walkthrough Complete` |
| Account | `est_sqft` **actual now, not estimated** · surface breakdown · access notes |
| Account | `est_monthly_value` replaced with the real calculated figure |
| Activity | `type: meeting`, `channel: meeting`. Photos referenced, not embedded |
| Activity | **Verbatim**: what they said would make them call you |
| Contact | `is_decision_maker` updated — you have now met them |
| Next action | "Send proposal", dated **within 48 hours** |

---

## 7. No-bid is a legitimate outcome

Walk away, in writing and politely, when: the scope needs capability you do not have · access
constraints make the schedule impossible · the budget frame is below your floor · the site raises
safety or liability concerns · the buyer was hostile or evasive on site.

> *"Having seen the space, I don't think we're the right fit for this one — the floor restoration
> needs a specialist crew. I'd rather tell you now than under-deliver. Happy to recommend someone."*

→ `Lost`, `loss_reason: we_declined`.

**Recording no-bids matters.** A pattern of no-bids in one segment is targeting feedback, and it is
invisible if you only log the jobs you bid.
