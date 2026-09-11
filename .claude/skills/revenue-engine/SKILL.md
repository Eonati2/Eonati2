---
name: revenue-engine
description: Master orchestrator for the Commercial Cleaning Client Acquisition OS. Use at the START of any task touching this project — ICP, offers, prospecting, account research, triggers, scoring, outreach copy, email sending, reply handling, CRM, sales, analytics, automation, or product/Gumroad assets. Routes work to the correct specialist skill, applies project rules that override specialist guidance, and enforces safety gates. Also use when the user mentions "revenue engine", "commercial cleaning OS", "acquisition OS", "proof pack", "free product", or asks which skill to use.
---

# Revenue Engine — Master Orchestrator

You are operating inside the **Commercial Cleaning Client Acquisition OS** project. This skill is the
router and the rule layer. Read it before invoking any specialist skill.

## 1. What this project is

We build and sell a contract-acquisition operating system to **US commercial cleaning / janitorial
companies** with the operational capacity to service recurring B2B accounts.

**One product:** the Commercial Cleaning Client Acquisition OS. **Price locked at $197**
(2026-09-11). The $149 launch price is retired — the distribution arithmetic in
`building-distribution` §2 showed $197 roughly halves the audience that has to be built. **No service tiers.** The $497 Setup and $2,000 Managed Pilot were removed on
2026-09-11 — do not mention, build, promise, or create infrastructure for them
(`research/12-decision-record-v4.md`).

**Goal:** first 10 customers, then 25, then 50. Revenue follows.

$10,000 in 90 days is **not** a defensible target for outbound alone under a single-product model —
the arithmetic is in `research/12-decision-record-v4.md`. Never present it as a forecast, and do not
plan against it. Any revenue target, at any level, goes through `building-distribution` first and
comes back as a required number of qualified free-kit downloads. A target is an input to arithmetic,
never a statement of capability.

**Core conceptual model — every deliverable maps to a stage of it:**

```
ACCOUNT → DECISION MAKER → TRIGGER → OUTREACH → CONVERSATION
        → WALKTHROUGH → PROPOSAL → WIN/LOSS → LEARN
```

**Primary principle:** sell the contract-acquisition *system*, not the lead.
**Secondary principle:** account first → person second → trigger third.

## 2. Conflict priority

When a specialist skill's guidance conflicts with something else, resolve in this order:

1. **Project-specific rules** (this file, and files under `commercial-cleaning-os/`)
2. **Safety and compliance rules** (§4 below)
3. **Master revenue-engine routing** (§3)
4. **Specialist skill guidance**
5. **Generic skill guidance**

A specialist skill never overrides §4. If a skill's advice would breach a safety gate, follow the
gate and say why.

## 3. Routing table

| Task | Route to | Notes |
|---|---|---|
| Product positioning, context doc | `product-marketing` | **Read first** — other marketing skills expect its context document to exist |
| ICP definition | `icp-definer` → cross-check `customer-research` | |
| Buyer personas | `persona-definer` | |
| Offer design | `offers` → `pricing` | **One product.** `offers` will suggest bonus stacks, tiers and scarcity — the project rules in §7 override all three |
| Account research (our buyers) | `deep-company-analyser` | |
| Prospect list building | `prospecting` | |
| Buying triggers | `trigger-finder` | **Apply our trigger hierarchy (§5), not the skill's default weighting** |
| Campaign architecture | `outbound-campaign-architect` + `gtm-outreach` | |
| Campaign angles | `campaign-angle-finder` | |
| Cold email copy — **write** | `cold-email` | |
| Cold email copy — **review / de-slop / CTA** | `cold-email-copywriting` | Specialist reviewer. See conflict note below. |
| Deliverability, DNS, warmup, inbox placement | `cold-email-deliverability` → `email-marketing-bible` | |
| Lifecycle / post-purchase / customer email | `emails` | |
| Compliance and send-safety gates | `email-marketing-bible` | Use its compliance + send-gate chapters |
| **Any customer-facing copy** — Gumroad, sales page, emails, sequences, follow-ups, ads, proposals, product docs | **`cleaning-os-voice` — MANDATORY, before drafting and again before sending** | Routes the chain below and has final say on voice |
| Copy chain, in order | `copywriting` → `copywriting-concrete` → `cleaning-os-voice` → `anti-ai-writing-slop` → `copy-editing` | Run once, in order. Never let five skills rewrite each other |
| Sales / landing page structure | `copywriting` → `cro` | Then run the chain |
| Cold email copy specifically | `cold-email-copywriting` replaces steps 2 and 4 of the chain | Scoped to that format |
| Named-human byline voice | `tone-of-voice` | Only when a human byline is needed. **Do not let it invent a persona for the product** |
| **Any sales-motion work** — qualification, discovery, walkthrough, objections, proposal conversation, negotiation, closing, follow-up | **`commercial-cleaning-sales`** | **Project-specific. Outranks all generic sales guidance.** Behavioural layer; pairs with `commercial-cleaning-os/sales/` for measurable detail |
| Sales collateral — decks, one-pagers, leave-behinds | `sales-enablement` | Collateral only, not the motion |
| CRM, lifecycle stages, handoff | `revops` | |
| CRM duplicates | `crm-duplicate-detector` | |
| Reply classification and response | `reply-handler` | |
| Pipeline analysis | `pipeline-analysis` | |
| Campaign metrics | `analytics`; `outbound-analyst` **for reference only** (see §6) | |
| Experiments | `ab-testing` | |
| Lead magnets / proof pack design | `lead-magnets` | The proof pack is our primary lead magnet |
| **Distribution, traffic, audience, launch, list growth, channels, revenue-target arithmetic** | **`building-distribution`** | **Project-authored.** Owns the requirement equation and the channel portfolio. Route here before any plan that assumes sales will arrive |
| "How do we hit $X?" / "Why aren't we getting sales?" | `building-distribution` | Resolves to a download count before anything else is diagnosed |
| Marketplace / Gumroad Discover traffic | `building-distribution` | Planning treatment is **zero**. It is a mirror, not a source |
| Promoting the free kit — communities, trade media, partnerships | `building-distribution` → then the copy chain | Conduct rules in its `references/channel-playbooks.md` are binding |
| Persuasion framing | `marketing-psychology` | Subordinate to the no-hype standard in §7 |
| Sending platform, plan limits, ramp, warmup, mailboxes, domains | **Project-authored** — `commercial-cleaning-os/automation/stack.md` | **Instantly Growth.** The binding limits are 5,000 campaign emails and 1,000 uploaded contacts per month — not mailbox count |
| Automation build | **Project-authored** — `commercial-cleaning-os/automation/stack.md`. Use `n8n-workflow-builder` for workflow *design* only and translate to Make | Our stack is Make + Attio + Instantly. **We are not using n8n.** No Make/Attio/Instantly specialist skill exists. The eight jobs are in `automation/make-jobs.md` |
| Automation debugging | `n8n-debugger` | Same caveat — general debugging thinking, not the tool |

**Sales layer — resolved.** `sales-skills/sales` could not be verified to exist, and it is no longer
needed. `commercial-cleaning-sales` (project-authored, installed 2026-09-10) is the entry point for
the whole sales motion, paired with the operational workflows in `commercial-cleaning-os/sales/`.
Both are project-specific, so both outrank generic sales guidance under the conflict priority in §2.
Where the two disagree, the override table at the foot of `commercial-cleaning-sales/SKILL.md`
decides.

### Conflict note: four skills claim cold email

`cold-email`, `cold-email-copywriting`, `gtm-outreach` and `email-marketing-bible` all trigger on
cold-email tasks. Division of labour, in this order:

1. `gtm-outreach` — frame the outreach task
2. `cold-email` — write the draft
3. `cold-email-copywriting` — review it, strip AI-slop, fix the CTA
4. `cold-email-deliverability` / `email-marketing-bible` — infrastructure and pre-send gates

Never run all four on one email and merge the output; it produces mush.

## 4. Safety gates — non-negotiable

**No autonomous sending. Ever.** Every sending workflow must carry: suppression check · duplicate
check · contact verification · compliance check · deliverability check · campaign attribution ·
**human approval for live sends** · kill switch · error logging · retry logic · audit trail.

**Human keeps judgment on:** targeting · claims · pricing · final copy approval · consequential
customer communication · compliance decisions. Automate administration and the movement of
information — not judgment.

**Phone is a separate, higher-risk workstream.** Default to manual human calls. No autodialing,
prerecorded, or AI voice unless counsel has confirmed the legal basis for that specific use.

**The primary business domain is never used for cold outbound.** It carries the website, Gumroad
brand, support, free-kit delivery and nurture, and post-purchase mail. Cold sending runs on
dedicated, replaceable domains only. No exceptions, no "just this batch" (`automation/stack.md`).

**Opt-outs suppress immediately and permanently**, across every domain and campaign. Never re-enroll.

**Compliance is guidance, not legal advice.** Build around CAN-SPAM, applicable TCPA/FCC/FTC and
state rules, privacy obligations, and platform terms. Never claim the project *is* compliant —
say what was built and what still needs review.

**Data:** only data we are permitted to use. Keep source and verification metadata on every record.
Never scrape behind authentication. Never imply private access. Never fabricate a missing field —
leave it empty and mark it unknown.

## 5. Trigger hierarchy — ours, and it overrides the specialist default

**High** — new location / new facility · expansion · move or new occupancy · relevant
property-management change
**Medium** — facilities or operations hiring · renovation or reopening · acquisition
**Low** — generic growth · funding · generic hiring · weak review signals

**A trigger is an event, not a conclusion.** Never write or imply, without direct evidence:
"they don't have a cleaner" · "their cleaner is failing" · "they're unhappy" · "they're looking for
a provider". State the observed event and its date. Nothing beyond it.

**Never assume:** every account is a fit · every company has a current need · a trigger means they
are shopping · a public review proves an incumbent is being replaced · a CRM title means
decision-maker.

## 6. Evidence standard

**Do not manufacture** numbers, testimonials, case studies, conversion rates, ROI claims, or market
evidence. Label every assumption as an assumption.

**Vendor benchmarks are not evidence.** `outbound-analyst` benchmarks against lemlist's own campaign
data; `email-marketing-bible` carries vendor-published industry figures. Both are useful as
reference and neither is neutral. Cite them as vendor-published, and never plan against them as if
they were measured outcomes of *our* system.

**Vendor bias to watch:** the `l3mpire/*` skills are lemlist's — `outbound-campaign-architect` and
`outbound-analyst` are shaped by lemlist's product and data. `email-marketing-bible` is
ecommerce/lifecycle-ESP oriented (Klaviyo, cart abandonment, DTC); use it for **deliverability,
compliance and send-safety**, not for B2B outbound copy.

## 7. Voice standard for everything customer-facing

Write like an experienced business operator: practical, direct, specific, calm, commercially
literate. The reader is an owner who is busy running a cleaning company.

**Never:** hype · AI filler · excessive emoji · fake scarcity · fake proof · guaranteed income,
clients, replies, or ROI.

**No scarcity of any kind.** A digital product has no capacity limit, so there is nothing to be
scarce about. Do not invent one.

**Internal ≠ public.** Revenue plans, model assumptions, internal research and implementation doubts
never appear on the Gumroad page or in customer-facing material.

## 8. Validation discipline

Phase 1 — **100** tightly qualified prospects. Qualitative: offer comprehension, response quality,
objections, trigger usefulness, proof-pack interest. **This is a listening exercise, not a
measurement** — it will not produce a reliable rate.
Phase 2 — **300–500**, only if Phase 1 produced meaningful signal.
Phase 3 — scale only after repeatable positive signal exists.

Test one major variable at a time. Never declare a winner on a small or noisy sample; state sample
size and uncertainty every time you report a result.

**Build order:** proof packs → targeting → triggers → outreach → talk to prospects → sell one →
learn → improve → *then* automate. Do not spend weeks automating an unvalidated process.

## 9. Working files

| Path | Contents |
|---|---|
| `commercial-cleaning-os/automation/stack.md` | **The locked tech stack** — Apollo, Make, Attio, **Instantly**, Claude, Gumroad. Plan limits, ramp, domain rule, upgrade triggers |
| `commercial-cleaning-os/automation/make-jobs.md` | The eight scheduled Make jobs, and the gate in job 3 |
| `commercial-cleaning-os/crm/` | schema, lifecycle stages, scoring, routing, field definitions |
| `commercial-cleaning-os/outbound/` | ICP, personas, triggers, campaigns, sequences, reply routing |
| `commercial-cleaning-os/automation/` | workflows, n8n, error handling, kill switches |
| `commercial-cleaning-os/offers/` | the product offer, and the free lead magnet |
| `commercial-cleaning-os/analytics/` | funnel, campaign metrics, experiments |
| `commercial-cleaning-os/policies/` | agent policy, sending policy, compliance |
| `commercial-cleaning-os/SKILL-DEPENDENCY-MAP.md` | which skill owns what |
| `.claude/skills/building-distribution/` | the distribution equation, channel portfolio, channel gates |

**The CRM is the single source of truth.** Every active opportunity carries an owner, a next action,
and a next-action date.
