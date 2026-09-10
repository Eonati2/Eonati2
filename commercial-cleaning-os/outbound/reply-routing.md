# Reply Routing — Outbound

Operational companion to `../crm/routing.md` §3, which is the authority. This file covers what to
*do* with each class; that file covers stage moves and SLAs.

**Governing rule:** classification is automated. **Responses are not.** Classes 7 and 8 are the only
ones that act without a human, and all they do is suppress.

---

## The ten classes

| # | Class | Recognizing it | Action | Who |
|---|---|---|---|---|
| 1 | **Positive** | Asks for the pack, a call, pricing, or details | Reply same business day | **Human** |
| 2 | Neutral / info requested | "What's this about?" · "Send more" | Reply same day, brief and specific | **Human** |
| 3 | Objection | "Too expensive" · "We're happy" · "Not a fit" | Reply within 1 business day. Log an objection code | **Human** |
| 4 | Wrong person | "That's not me" · "Try Dana" | Thank, ask for the right person, mark `wrong_role` | **Human** |
| 5 | Not now | "Circle back in Q1" | Confirm the date. → `Nurture` **with a review date** | Human, brief |
| 6 | Existing provider | "We already have someone" | Ask for the renewal date. → `Nurture` | Human, brief |
| 7 | **Unsubscribe** | Any form of "stop" | **Suppress immediately.** No reply | **Automated** |
| 8 | **Negative** | Hostile | **Suppress.** No reply. Do not apologise | **Automated** |
| 9 | Out-of-office | Auto-reply with a return date | Pause sequence to that date | Automated |
| 10 | Automated / bounce | Hard bounce → invalid. Soft → one retry | Automated | Automated |

---

## The three that are misread most often

**Class 6 is not a loss.** An existing provider is the *normal* state of a commercial building. It
means the timing is wrong, and timing is the entire premise of the trigger model. The one thing to
extract is the **renewal date** — it is the most valuable field a "no" can produce, and it converts
class 6 into a dated, scheduled future conversation.

**Class 5 without a review date is a class 7 in disguise.** "Circle back later" with no date means
the account sits in `Nurture` forever. Push once for a month: *"Roughly when would make sense?"*

**Class 4 is worth more than it looks.** A named referral inside the company is a warm route.
Always ask: *"Would you mind pointing me to the right person?"*

---

## Never auto-reply to classes 1–4

A same-day human reply is the highest-value action in the system. An instant automated one destroys
exactly the thing it was trying to accelerate — and this audience can tell. `revenue-engine` §4
keeps consequential customer communication with a human, and a first reply to an interested
prospect is consequential.

**Proof-pack delivery is manual by policy** (`../crm/lifecycle-stages.md` §3, stage 6). It is the
highest-leverage 90 seconds in the funnel.

---

## Objection codes — Instance A

Log on every class-3 reply. Closed list; add to it deliberately rather than typing prose.

`price` · `no_time` · `diy_already` · `tried_cold_email` · `not_commercial` · `too_small` ·
`distrust_marketer` · `wants_guarantee` · `wants_references` · `bad_timing`

**Watch `distrust_marketer` and `tried_cold_email`.** They are the two that indicate a positioning
problem rather than an objection — this audience is heavily solicited, and if either dominates, the
first email is reading as another agency pitch.

**`wants_guarantee` is answered honestly, never by inventing one.** See
`../sales/06-selling-the-managed-pilot.md` §5.

---

## Suppression

Global, permanent, both channels, checked at execution time (`../crm/routing.md` §4).

A "don't email me" suppresses the phone too. A suppressed record is never deleted — the row **is**
the evidence that it was suppressed.

**Never re-enroll.** No exceptions, no "it's been six months", no new campaign that "wouldn't
count."

---

## Weekly review

| Metric | Watch for |
|---|---|
| Positive replies per 100 contacted | Base case 2%. Under 0.5% → abort the segment |
| Class mix | Rising class 8 means the copy or the targeting is wrong |
| Class 6 with renewal dates captured | Should be most of them — otherwise the nurture pipeline is empty |
| Median hours to human reply on class 1 | Target under 8 business hours |
| Objection code concentration | One code above ~40% is a message problem, not a market problem |

**Reply *volume* is not the metric.** Positive replies and conversations are
(`revenue-engine` §7). A campaign with a high reply rate and no conversations is annoying people
efficiently.
