# Our Stack

Locked 2026-09-11. One product means a small stack; every tool has to earn its line item.

| Layer | Tool | Plan | Why |
|---|---|---|---|
| Account data | **Apollo** | Free → paid only when it binds | Verification and contact patterns. Not discovery — public sources are better for small local businesses |
| Orchestration | **Make** | Core | Connects the pieces. Hosted, so nothing to maintain |
| CRM | **Attio** | Free | Single source of truth. Free tier covers this volume comfortably |
| Sending | **Smartlead** | Base | Sequencer plus warmup |
| Classification & drafting | **Claude API** | Pay as you go | Reply classification, pack drafting. Never sends |
| Domains & mailboxes | Existing + dedicated sending domains | — | Never send cold from the product domain |
| Payments | **Gumroad** | — | Merchant of record, and its analytics tell us whether the problem is traffic, page, offer or product |

**Budget:** roughly $200–$400/month once mailboxes are counted. The dominant cost is mailboxes, not
software.

---

## Deliberately not in the stack

| Not using | Why |
|---|---|
| **n8n** | Make covers it and is hosted. Self-hosting is a maintenance job we don't need at this size. |
| A second CRM | Attio is the single source of truth. Two CRMs means neither is. |
| A second email platform | Smartlead does warmup and sequencing. |
| A large data subscription | Public sources plus Apollo's free tier. Revisit only when a specific gap costs real time. |
| Additional AI tools | Claude does the classification and drafting. |
| A course platform | The product is thirteen files and a download. |
| A chatbot | Nobody is asking us anything yet. |
| Paid ads | Not until organic and outbound have told us what converts. |

---

## The machine

```
PROSPECTING
   → public sources + Apollo          find and enrich
   → Make                             move and transform
   → QUALIFICATION                    filters, automated
   → TRIGGER + EVIDENCE               dated, sourced
   → ATTIO                            recorded
   → ★ HUMAN APPROVAL ★               the gate — never automated
   → SMARTLEAD                        send
   → REPLY
   → Make → Claude                    classify only
   → ATTIO                            updated
   → PRODUCT INTEREST
   → GUMROAD                          purchase
```

**One gate, and it is real.** Nothing sends without a person looking at that specific batch.
Claude classifies replies; it does not answer them. Per `revenue-engine` §4, consequential customer
communication stays with a human.

---

## Skill-routing consequence

`n8n-workflow-builder` and `n8n-debugger` are installed and route automation work to a tool we have
now decided against.

**They stay installed** — the decision could reverse, and their workflow-design thinking (error
handling, retries, idempotency, where to put a gate) transfers to Make unchanged. But
`revenue-engine` no longer routes to them by default.

**Open gap:** there is no Make or Attio specialist skill. Automation work is project-authored, using
the n8n skills for workflow *design* and translating to Make. Worth revisiting if a good Make skill
appears.

---

## Build order

Manual first. Every step below only earns its place once the manual version is working and the
bottleneck is obvious.

1. **Manual** — spreadsheet, inbox, hand-built packs. At least twenty accounts.
2. **Discovery into Attio** — Make pulls accounts and contacts into the CRM. Biggest time saving,
   least risk.
3. **Trigger watching** — weekly automated checks writing into Attio. The highest-value automation,
   because trigger hunting is the step that gets skipped when busy.
4. **Sequencing with the approval gate** — Smartlead holds the sequences, a human approves batches.
5. **Reply classification** — Claude sorts; a human answers.

**Do not build past the step that is currently hurting.** Most of the value is in steps 2 and 3.
