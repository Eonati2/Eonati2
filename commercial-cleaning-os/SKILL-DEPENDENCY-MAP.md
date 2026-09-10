# Skill Dependency Map

Which skill owns what, where they overlap, and where they must not be trusted blindly.
**33 skills installed** — 1 orchestrator + 32 specialists. Source of truth for routing is
`.claude/skills/revenue-engine/SKILL.md` §3.

---

## Install provenance

| Source | Install method | Skills | Location |
|---|---|---|---|
| `coreyhaines31/marketingskills` ★49.4k | `npx skills add` | 16 | `.agents/skills/`, symlinked into `.claude/skills/` |
| `l3mpire/claude-skills` (lemlist) | `npx github:l3mpire/claude-skills --project` | 12 | `.claude/skills/` |
| `bcharleson/claude-code-cold-email-skills` ★6 | git clone + copy | 3 | `.claude/skills/` |
| `CosmoBlk/email-marketing-bible` ★291 | git clone | 1 | `.claude/skills/` |
| **This project** | authored | 1 (`revenue-engine`) | `.claude/skills/` |

`sales-skills/sales` — **not installed. Could not be verified to exist** (404 on every raw path
tried; org search returns no such resource). See "Open gap" below.

---

## Ownership by stage of the core model

```
ACCOUNT ──→ DECISION MAKER ──→ TRIGGER ──→ OUTREACH ──→ CONVERSATION
                                                             │
        WALKTHROUGH ←── PROPOSAL ←── WIN/LOSS ←── LEARN ←─────┘
```

| Stage | Primary | Supporting |
|---|---|---|
| Foundation | `product-marketing` | `customer-research`, `offers`, `pricing` |
| ACCOUNT | `prospecting` | `deep-company-analyser`, `icp-definer` |
| DECISION MAKER | `persona-definer` | `icp-definer` |
| TRIGGER | `trigger-finder` | *project hierarchy overrides its default weighting* |
| OUTREACH — architecture | `outbound-campaign-architect` | `gtm-outreach`, `campaign-angle-finder` |
| OUTREACH — copy | `cold-email` | `cold-email-copywriting` (review), `copywriting`, `copy-editing` |
| OUTREACH — infrastructure | `cold-email-deliverability` | `email-marketing-bible` |
| CONVERSATION | `reply-handler` | `sales-enablement` |
| WALKTHROUGH · PROPOSAL | `sales-enablement` | **gap — see below** |
| WIN/LOSS · pipeline | `revops` | `pipeline-analysis`, `crm-duplicate-detector` |
| LEARN | `analytics` | `ab-testing`, `outbound-analyst` *(reference only)* |
| Product & storefront | `copywriting` | `cro`, `lead-magnets`, `marketing-psychology` |
| Automation | `n8n-workflow-builder` | `n8n-debugger` |
| Post-purchase email | `emails` | `email-marketing-bible` |

---

## Identified conflicts and how they are resolved

### C1 — Four skills claim cold email
`cold-email`, `cold-email-copywriting`, `gtm-outreach`, `email-marketing-bible` all trigger on
cold-email tasks.

**Resolution — a pipeline, not a merge:** `gtm-outreach` frames → `cold-email` drafts →
`cold-email-copywriting` reviews and fixes the CTA → `cold-email-deliverability` /
`email-marketing-bible` handle infrastructure and pre-send gates. Running all four and blending the
output produces mush.

### C2 — `emails` vs `email-marketing-bible`
Both cover sequences. **`emails`** owns our own lifecycle email (post-purchase, onboarding,
upsell). **`email-marketing-bible`** is scoped to deliverability, compliance and send-safety only —
it is ecommerce/ESP-oriented (Klaviyo, cart abandonment, DTC) and its lifecycle playbooks do not
transfer to B2B outbound.

### C3 — `trigger-finder` default weighting vs ours
The skill weights funding, hiring and tool changes highly. **Our hierarchy puts facility events
first** (new location, move, occupancy, property-management change) and funding/generic hiring last,
because a facility event creates a plausible cleaning need and a funding round does not.
**Project hierarchy wins.** See `revenue-engine` §5.

### C4 — Vendor bias in the lemlist skills
`outbound-campaign-architect` and `outbound-analyst` are built on lemlist's own product and campaign
data. `outbound-analyst` is **reference only** — its benchmarks are vendor-published and must never
be used as a planning assumption or presented as our expected performance.

### C5 — `marketing-psychology` vs the voice standard
Persuasion frameworks can pull toward urgency and scarcity language. The no-hype / no-fake-scarcity
standard in `revenue-engine` §7 **overrides** it every time.

### C6 — Symlinks are not duplicates
The 16 marketingskills entries in `.claude/skills/` are symlinks into `.agents/skills/`. That is the
installer's normal cross-agent layout. **Both directories must be committed** — deleting `.agents/`
breaks every symlink.

---

## Deliberately NOT installed

| Skill | Repo | Why |
|---|---|---|
| `people-finder` | l3mpire | A lemlist product manual, not a generic capability. We do not use lemlist. |
| `list-builder`, `company-finder` | l3mpire | Same — lemlist search-filter guides |
| `copywriting-ic/manager/vp-sequence` | l3mpire | Tuned to SaaS org charts. Our buyer is an owner-operator. |
| ~34 remaining marketingskills | coreyhaines31 | SEO, ASO, ads, social, video, PR, community, events — not in the outbound motion |

**Optional adds, if a need appears:** `cta-designer` and `copywriting-analyzer` (l3mpire) —
CTA quality is a named quality gate; `cold-call-script` (l3mpire) if the phone workstream clears
counsel review; `website-scraper` (l3mpire) for account research.

---

## Open gap — the sales layer

`sales-skills/sales` and its `sales-do` router were specified as the entry point for discovery,
objection handling, follow-up, proposal, closing, pipeline, CRM and cadence. **The repository could
not be verified to exist.**

**Interim coverage:**

| Need | Covered by | Adequate? |
|---|---|---|
| Prospecting | `prospecting` | Yes |
| Outreach | `cold-email` + `outbound-campaign-architect` | Yes |
| Reply handling | `reply-handler` | Yes |
| Pipeline / CRM | `revops` + `pipeline-analysis` | Yes |
| Objection handling | `sales-enablement` | Partly — generic, not cleaning-specific |
| **Discovery call** | — | **No** |
| **Walkthrough** | — | **No — and it is the central event in this business** |
| **Proposal / bid** | `sales-enablement` | Partly |
| **Closing, cadence** | — | **No** |

The four gaps are cleaning-industry-specific and would need project-authored workflows regardless of
whether a generic sales skill were installed — a generic closing skill does not know what happens on
a janitorial walkthrough. Build them under `commercial-cleaning-os/`.
