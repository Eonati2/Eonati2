# 07 — Execution Plan

> **Superseded in part.** Timeline is now **90 days** and validation is staged
> **100 → 300–500 → 1,000+** (see `11 §C2`). The weekly gates and the seven metrics below still
> apply; the calendar does not.

### Staged validation

| Test | Size | Question it answers |
|---|---|---|
| 1 | **100**, hand-picked | Qualitative only. Do owners understand the offer? Which trigger draws attention? What objection recurs? Do they ask *"can you just do this for me?"* |
| 2 | **300–500**, after the message is revised | Directional response rate, first conversions |
| 3 | **1,000+** | Only once downstream conversion data exists |

**Test 1 will produce roughly 2 positive replies at base case. That is a listening exercise, not a
measurement** — label it as such, or a thin result gets misread as failure.

---

## Original 60-day schedule (retained for the gates)

Each week has one theme, a short task list, and **one gate**. If the gate fails, you fix that before
adding volume. Adding volume to a broken funnel is the most expensive mistake available to you.

---

## WEEK 1 — Infrastructure (revenue this week: $0, and that's correct)

**Theme: buy the assets that need 21 days to become useful.**

- [ ] Buy **6 sending domains** + 1 product domain (~$85)
- [ ] Google Workspace: **24 mailboxes**, 4 per sending domain (~$144/mo)
- [ ] SPF, DKIM, DMARC (`p=none` + rua) on all 6
- [ ] Smartlead account; connect all 24; **start warmup at 5 sends/inbox/day**
- [ ] CMRA/PO box for the CAN-SPAM address
- [ ] Gumroad account, verified (payouts need $100 balance + verification — do it now, not in week 6)
- [ ] 301 each sending domain → product domain
- [ ] **Build 5 Proof Packs by hand** for 5 different metros. No automation. Time it.

> **The 5 hand-built packs are the most important task of week 1.** They tell you whether the core
> asset is impressive, how long it takes, and what "good" looks like — the judgment you'll later
> encode into automation. Do not skip to the tooling.

**GATE:** DMARC passing on all 6 domains · 5 packs built · you can honestly say the packs are good.

---

## WEEK 2 — The Trigger Board and the list

**Theme: build the IP.**

- [ ] Document all **11 triggers**: source, method, freshness, score, email angle
- [ ] Apify scrape: **metros 1–4**, 8 queries each (~$40)
- [ ] Run the 6 qualification filters → target ~1,200 qualified
- [ ] Enrichment cascade on the first 600 (site → GBP → SoS → LinkedIn → Apollo)
- [ ] Verify 100% of emails
- [ ] Split Segment 1 / Segment 2
- [ ] Warmup to 12/inbox/day
- [ ] Start writing the product (Tier A assets first — see `02 §4`)

**GATE:** ≥1,000 qualified contacts · bounce rate on a 50-email test <3% · named-human coverage ≥50%.

---

## WEEK 3 — Product v1 and first sends

**Theme: ship something imperfect and start the clock.**

- [ ] Finish **Tier A**: Trigger Board, 500-prospect starter list template, automation blueprint,
      Proof Pack generator
- [ ] Finish **Tier B**: 6 sequences, walkthrough script, bid kit, objection cards, decision-maker
      map, deliverability checklist
- [ ] Sales page live on the product domain (structure in `02 §6`)
- [ ] Gumroad products created: $197 / $497 / $1,497 + the $97 order bump
- [ ] Scrape metros 5–8, enrich, verify → 6,400 contacts total
- [ ] Warmup to 20/inbox/day
- [ ] **Launch Sequence 1 to the first 500 Segment-1 contacts**

> Tier C (the written guides) can ship in week 4. Nobody has refunded a product on day 3 for a
> missing implementation checklist. They refund it for a missing prospect list.

**GATE:** page live and buyable (test-purchase it yourself) · 500 sends out · complaint rate <0.1%.

---

## WEEK 4 — The thesis test

**Theme: find out whether triggers actually work.** This is the most important week in the plan.

- [ ] Scale to 28/inbox/day → ~672/day
- [ ] Sequence 1 → remaining Segment 1 (~1,500)
- [ ] Sequence 2 → first Segment 2 batch (~1,000)
- [ ] Build every Proof Pack requested, within 24 hours, **sent by a human**
- [ ] Ship Tier C
- [ ] Log every reply, tagged: positive / not-now / wrong-person / negative / unsubscribe

**GATE — the big one:** **Segment 1 reply rate ≥6%.**
- **≥12%** → the thesis is confirmed. Move contacts from Segment 2 into trigger research; that's the
  highest-return lever in the sensitivity table.
- **6–12%** → working. Continue, improve trigger quality.
- **<6%** → **stop sending.** The triggers aren't landing. Read 20 replies, rewrite email 1, retest
  on 500. If a second test also comes back under 6%, go to `08-risks-and-alternatives.md` Plan B.

---

## WEEK 5 — Conversion

**Theme: turn positive replies into money.**

- [ ] Full send volume, both segments
- [ ] Sequence 3 running on every delivered pack
- [ ] **Get on the phone with every positive reply that will take a call.** At this stage, calls are
      research as much as sales — you're learning the objections that rewrite the sales page.
- [ ] Rewrite the sales page using the exact language from those calls
- [ ] Launch channel C2: post a free Proof Pack for one commenter's city per day in the cleaning
      Facebook groups. Give first, publicly.

**GATE:** ≥15 positive replies cumulative · ≥10 packs delivered · sales page rewritten from real
objections, not guesses.

---

## WEEK 6 — First revenue must exist

**Theme: if nothing has sold, stop and find out why.**

- [ ] Full send volume
- [ ] Day-5 offer email going out to everyone who got a pack
- [ ] Founding-price ($147, first 20) urgency in the week's follow-ups
- [ ] Collect the **first 3 testimonials** — ask directly, offer to write a draft they can edit
- [ ] Approach **2 affiliate partners** in the cleaning-coach world (40% recurring)

**GATE:** **at least one sale.**
Zero sales by end of week 6 → stop sending and interview five positive-repliers. Ask one question:
*"You wanted the list but didn't buy the system — what was the actual reason?"* The answer is worth
more than another 5,000 emails, and you cannot guess it.

---

## WEEK 7 — The top of the ladder

**Theme: this is where half the revenue is.**

- [ ] Full send volume
- [ ] **Offer DFY on every walkthrough call, as the default recommendation, not an upsell**
- [ ] Testimonials onto the sales page
- [ ] 14-day DFY upsell to week-4/5 buyers
- [ ] Second affiliate conversation
- [ ] Weekly trigger digest to everyone who took a pack but hasn't bought (the nurture asset)

**GATE:** ≥1 sale at $497+ · pack→purchase ≥15%.

---

## WEEK 8–8.5 — Close

**Theme: convert everything already in motion.**

- [ ] Final sends
- [ ] Work every open thread to a yes or a no
- [ ] Founding-price deadline — real, honored, and then actually raised to $197
- [ ] Final DFY push to the highest-engagement non-buyers
- [ ] **Write the retrospective:** actual rates vs. the model in `03`, and what you'd change

**GATE:** target reached, or a documented, specific reason why not.

---

## The seven numbers, tracked weekly

| # | Metric | Target |
|---|---|---|
| 1 | Sends | 18,000 cumulative by week 8 |
| 2 | Delivery rate | >95% |
| 3 | **Spam complaint rate** | **<0.1%** |
| 4 | Segment 1 reply rate | ≥12% |
| 5 | **Positive replies per 1,000 sends** | **≥5** |
| 6 | **Proof pack → purchase** | **≥20%** |
| 7 | Gross revenue | $10,000 by day 60 |

Metrics 5 and 6 predict everything. If both are healthy and revenue is short, the machine works and
simply needs more weeks — that is a fundamentally different problem from a machine that doesn't work,
and confusing the two is how people quit a working business in week 7.

---

## Time budget (the real constraint)

| Week | Hours | Heaviest item |
|---|---|---|
| 1 | 20–25 | 5 hand-built proof packs |
| 2 | 25–30 | Trigger Board + enrichment |
| 3 | 30–35 | Product build + sales page |
| 4 | 20 | Reply handling + pack building |
| 5 | 20 | Calls |
| 6 | 15 | Calls + testimonials |
| 7 | 15 | DFY delivery |
| 8 | 15 | Closing |
| **Total** | **~170 hours** | |

**~170 hours for a base case of ~$11,000 is about $65/hour** — and it leaves behind a machine, a
product, and a list. If you can only give this 5 hours a week, the plan doesn't scale down; it just
takes 5 months. Say that out loud now rather than discovering it in week 3.
