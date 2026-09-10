# Outbound

| File | Contents |
|---|---|
| `icp.md` | Both ICPs. Instance A geography correction — DFW is the demo, not the territory |
| `personas.md` | Who to write to, per instance and segment. Contact discovery cascade |
| `triggers.md` | The trigger library: sources, freshness windows, detection cadence, and the claim table |
| `reply-routing.md` | The ten reply classes, what is automated and what is not, objection codes |
| `campaigns/README.md` | Campaign architecture, both instances, launch checklist |
| `sequences/instance-a.md` | **Ours** — four sequences for selling the OS and the pilot |
| `sequences/instance-b.md` | **Product content** — six templates the customer runs |

## Three things this layer settles

**The trigger hierarchy overrides `trigger-finder`.** Facility events (new location, occupancy,
move, property-management change) score 5. Funding and generic hiring score 1. A funded company
does not have a dirtier office; a building someone just moved into does.

**Review signals were demoted from 5 to 1.** A complaint about restrooms does not establish that
the business controls the cleaning contract, that the reviewer is an employee, that the issue is
current, or that anyone is shopping. It is a modifier stacked on an event, and it is **never quoted
back to a prospect**.

**The claim table is the operational form of the anti-fabrication rule.** Every trigger has a
column for what it licenses you to say and a column for what it does not. The pre-send claim check
tests merged copy against it.

## Status

Specified. Nothing sent. Instance A campaigns are blocked on the pre-send gate
(`../crm/routing.md` §6) — infrastructure, verification and human approval — and phone is blocked
pending counsel review.
