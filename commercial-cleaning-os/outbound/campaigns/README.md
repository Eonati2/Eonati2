# Campaign Architecture

A campaign is **one segment × one trigger tier × one persona**. Anything broader cannot be
diagnosed when it underperforms — you will not know whether the segment, the trigger, or the copy
was wrong.

**Every campaign carries a `campaign_id`**, and every Activity row references it
(`../../crm/routing.md` §6, check 8). Without attribution, the analytics layer has nothing to work
with and the experiment framework is decorative.

---

## Instance A — our campaigns

Selling the Client Acquisition OS to cleaning companies.

| ID | Segment | Trigger tier | Persona | Sequence | Volume |
|---|---|---|---|---|---|
| `A-TRIG-OWNER` | Cleaning cos, 3–25 staff | Any Instance A trigger | P1 Owner | `SEQ-A1` | **Priority.** Grow this at the expense of the others |
| `A-BROAD-OWNER` | Cleaning cos, 3–25 staff | None | P1 Owner | `SEQ-A2` | Volume filler |
| `A-GENERIC` | Same, `info@` only | Any | Unknown | `SEQ-A3` | Written to be forwarded |
| `A-PACK` | Anyone who requested a pack | — | — | `SEQ-A4` | **Manual send.** Where the revenue is |
| `A-MAGNET` | Anyone who took the free product | — | — | nurture | Email follow-up, not outbound |

**`A-TRIG-OWNER` is the campaign that matters.** Signal-referenced outreach to a named human is the
only combination with a structural advantage. When capacity is scarce, cut `A-BROAD-OWNER` first.

### Volume discipline
Phase 1 is **100** hand-picked prospects — qualitative, not a measurement. It will produce roughly
two positive replies at the 2% base case, which tells you nothing statistically and a great deal
conversationally: whether they understand the offer, which trigger draws attention, what objection
recurs, and whether anyone asks *"could you just do this for me?"*

Phase 2 is **300–500** after the message is revised. Phase 3 scales only on repeatable signal.

**Do not blast thousands.** Sending capacity is a domain-reputation budget, not a faucet.

---

## Instance B — campaign templates that ship in the product

The customer runs these against facilities in their own metro. Shipped as templates they configure,
not as a fixed list — their ICP is theirs (`../icp.md`).

| Template | Segment | Trigger | Persona |
|---|---|---|---|
| `B-PM-NEW` | Property management | T4 portfolio change | Property Manager |
| `B-MED-MOVE` | Medical / dental | T1, T2, T3 | Practice Manager |
| `B-OFF-MOVE` | Office / professional | T1, T2, T3 | Office Manager |
| `B-OFF-HIRE` | Office / professional | T5 facilities hiring | Office / Facilities Manager |
| `B-IND-NEW` | Industrial | T2, T6 | Operations Manager |
| `B-EDU-TERM` | Schools / daycare | T2, T6, term timing | Director / Business Manager |

**Six templates, not sixty.** A cleaning company running two well beats one running six badly, and
the product should say so.

### Recommended starting pair
`B-PM-NEW` for leverage — one property manager can expose several buildings — and whichever of
`B-MED-MOVE` or `B-OFF-MOVE` matches what they can actually service.

---

## Channel sequencing

Email opens the conversation. **It does not close commercial cleaning contracts** — this is a
relationship-driven market and the walkthrough is the event that matters.

```
Email (opens) → Reply → Phone or in-person (advances) → Walkthrough (decides)
```

**Phone stays blocked in our own campaigns pending counsel review** (`../../crm/routing.md` §7).
For Instance B, the product teaches the phone step with the compliance module attached — customers
call their own local prospects, and they need to know the rules before they do.

---

## Launch checklist

- [ ] Segment, trigger tier and persona each named and singular
- [ ] `campaign_id` assigned
- [ ] List built, qualified, scored — **all contacts ≥ 8 total**
- [ ] 100% verified; suppression checked at send time, not build time
- [ ] Copy passes the claim check against `Trigger_Event.evidence`
- [ ] Compliance footer: sender identity, physical postal address, working opt-out
- [ ] Daily volume within the domain's warmed capacity
- [ ] Reply routing live and monitored
- [ ] **Human approval on the send** — no bypass
- [ ] Kill switch reachable

Any unchecked box blocks the launch. The gate warns and stops; it does not warn and proceed.
