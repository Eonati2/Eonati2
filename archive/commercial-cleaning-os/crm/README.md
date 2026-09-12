# CRM — the single source of truth

Read in this order.

| File | What it settles |
|---|---|
| `schema.md` | The two-instance architecture, five objects, IDs, ten integrity rules, the three-state convention |
| `lifecycle-stages.md` | Both stage sets with entry/exit criteria and owners, handoff SLAs, weekly health checks |
| `scoring.md` | The 20-point model, the trigger hierarchy that overrides `trigger-finder`, negative overrides, a worked example |
| `routing.md` | Inbound sources incl. Gumroad, stage-advance automation limits, reply routing, suppression, the 10-check pre-send gate |
| `field-definitions.md` | Every field: type, allowed values, who sets it, what blocks a write |

## The four decisions this foundation makes

**1. Two instances, one schema.** Instance A is our pipeline (accounts = cleaning companies we sell
to). Instance B is the customer's (accounts = buildings they pursue). They were merged in the
original brief; merging them corrupts every ratio, because a walkthrough is an event in B and has no
counterpart in A. Instance B ships *inside* the product — we run it on ourselves in A.

**2. Activity and Trigger_Event are objects, not fields.** `Notes` cannot hold an audit trail and a
single `Trigger` string cannot hold dated evidence. Activity is append-only and doubles as the
TSR call-detail record; Trigger_Event forces every signal to carry a source and a date.

**3. Three states, not two.** A value · `unknown` (looked, not findable) · empty (not looked yet).
Blank means *go research it*; `unknown` means *stop*. Collapsing them wastes hours.

**4. No engagement scoring, no open/click fields.** `revops` recommends them; they require tracking
pixels, which depress deliverability and inflate numbers with bot activity. Scoring is fit plus
trigger only, and success is measured in replies and conversations.

## The rule the whole thing exists to enforce

A trigger is **an event, not a conclusion**. The CRM stores what was observed, quoted verbatim, with
its source and date. It never stores — and outreach never claims — that a prospect has no cleaner,
is unhappy with one, or is shopping. The pre-send claim check (`routing.md` §6, check 6) tests copy
against the `evidence` field for exactly this.

## Status

Specification complete; nothing implemented. Next: the Google Sheets workbook that instantiates it
(`schema.md` §6), then the four missing sales workflows — discovery, walkthrough, proposal, closing.
