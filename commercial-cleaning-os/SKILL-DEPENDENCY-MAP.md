# Skill Dependency Map

Which skill owns what, where they overlap, and where they must not be trusted blindly.
**39 skills installed** — 1 orchestrator + 38 specialists. Source of truth for routing is
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
| **This project** | user-supplied, installed 2026-09-10 | 1 (`commercial-cleaning-sales`) | `.claude/skills/` |
| `entpnomad/copywriting` + `entpnomad/tone-of-voice` | git clone | 2 (`copywriting-concrete`, `tone-of-voice`) | `.claude/skills/` |
| `thomasmeijer92/anti-ai-writing-slop` | git clone | 1 | `.claude/skills/` |
| **This project** | authored 2026-09-10 | 1 (`cleaning-os-voice`) | `.claude/skills/` |
| **This project** | authored 2026-09-11 | 1 (`building-distribution`) | `.claude/skills/` |

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
| **DISTRIBUTION** — traffic, audience, list growth, channels, target arithmetic | **`building-distribution`** | `lead-magnets` (the asset), `analytics` (the measurement) |
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

### C6 — Six skills now claim copy work
`copywriting`, `copy-editing`, `copywriting-concrete`, `tone-of-voice`, `anti-ai-writing-slop` and
`cold-email-copywriting` all trigger on copy tasks.

**Resolution — one chain, run once, in order:** `copywriting` (argument) → `copywriting-concrete`
(concrete / falsifiable / ownable) → **`cleaning-os-voice`** (our reader, final say on voice) →
`anti-ai-writing-slop` (evidence-aware de-slop) → `copy-editing` (tighten). For cold email,
`cold-email-copywriting` replaces steps 2 and 4. `tone-of-voice` runs only when a named human
byline is needed — it must not invent a persona for the product.

`cleaning-os-voice` is **mandatory** for anything a prospect or customer reads, and it decides any
disagreement in the chain.

### C8 — Nothing owned distribution until 2026-09-11
Thirty-eight installed skills covered ICP, copy, outbound, CRM, sales and analytics. **None covered
how a stranger arrives.** `lead-magnets` designs the asset; nothing said how anyone finds it. The
`coreyhaines31` set does carry community, SEO, ads, social, video and PR skills — all
deliberately not installed as outside the outbound motion, which was the right call for outbound
and the wrong call for the business, because outbound has a hard capacity ceiling and cannot reach
the revenue target alone.

**Resolution:** `building-distribution` (project-authored, 2026-09-11) owns the requirement
equation and the channel portfolio. It is upstream of every plan that assumes sales will arrive.
Its planning treatment of marketplace traffic — **zero** — overrides any generic skill that
suggests a storefront listing is a channel.

### C7 — Symlinks are not duplicates
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
| `anti-ai-slop-writing` | jalaalrd | Aggressive banned-word list aimed at defeating AI detectors. Our goal is truth and specificity, not evasion; a blocklist flattens voice and checks nothing about whether a claim is supported |
| `direct-response-copy`, `ad-copy`, `landing-page-copy`, `compliance-checker` | robpalmer99 | Strong craft in a register this project bans — VSL urgency mechanics and manufactured scarcity. It would fight `cleaning-os-voice` on every draft. `copychief` alone is a reasonable later add for a line-by-line sales-page review |

**Optional adds, if a need appears:** `cta-designer` and `copywriting-analyzer` (l3mpire) —
CTA quality is a named quality gate; `cold-call-script` (l3mpire) if the phone workstream clears
counsel review; `website-scraper` (l3mpire) for account research.

---

## Sales layer — closed

`sales-skills/sales` could not be verified to exist. It is no longer needed: **`commercial-cleaning-sales`**
(project-authored, installed 2026-09-10) is now the sales entry point, and it knows this business in
a way a generic router would not.

**Two project-specific sources now cover sales, and they are layered, not duplicated:**
`commercial-cleaning-sales` is the **behavioural** layer — conversation, questions, listening, the
cold-call/discovery distinction. `commercial-cleaning-os/sales/` is the **operational** layer —
measurement, the two-method pricing model, closed reason codes, SLAs, and the Instance B content
that ships inside the product. The override table at the foot of the skill decides any disagreement.

**Coverage:**

| Need | Covered by | Adequate? |
|---|---|---|
| Prospecting | `prospecting` | Yes |
| Outreach | `cold-email` + `outbound-campaign-architect` | Yes |
| Reply handling | `reply-handler` | Yes |
| Pipeline / CRM | `revops` + `pipeline-analysis` | Yes |
| Objection handling | `sales/04` | **Closed** |
| Discovery call | `sales/01` | **Closed** |
| Walkthrough | `sales/02` | **Closed** |
| Proposal / bid | `sales/03` + `sales-enablement` for collateral | **Closed** |
| Closing, cadence | `sales/04`, `sales/05` | **Closed** |

**Resolved by authoring, not by installing.** All four were cleaning-industry-specific and would
have needed project-authored workflows regardless — a generic closing skill does not know what
happens on a janitorial walkthrough, what destroys margin on a site visit, or why a per-square-foot
sanity check must never govern a bid. The missing repository cost less than it appeared to.

`sales-enablement` remains routed for collateral: pitch decks, one-pagers, leave-behinds.
