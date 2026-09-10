---
name: gtm-outreach
description: >-
  Guides cold outreach strategy for email and LinkedIn using business-agnostic
  best practices. Use when planning, reviewing, or executing cold outreach,
  outbound sales, prospecting, GTM motions, or when the user mentions cold
  email, LinkedIn outreach, lead generation, or sales development.
---

> Built for **Claude Code** (and compatible agent harnesses). Drop into `.claude/skills/`.

# GTM Outreach

## When to Use This Skill

Apply this skill as the entry point for any cold outreach work in this project. Route to specialized skills based on the task.

## Skill Routing

| User need | Read and follow |
|-----------|-----------------|
| Inbox placement, DNS auth, ESP/SEG setup, sending infrastructure | [cold-email-deliverability](../cold-email-deliverability/SKILL.md) |
| Writing, editing, or reviewing email copy | [cold-email-copywriting](../cold-email-copywriting/SKILL.md) |
| LinkedIn messaging or connection requests | *Coming soon — apply email copy principles until dedicated skill exists* |

## Outreach Stack (Mental Model)

```
Sending infrastructure          Message                    Recipient environment
─────────────────────          ───────                    ─────────────────────
SPF / DKIM / DMARC      →      Plain text, relevant  →    Google / Microsoft / custom ESP
Domain reputation              Hook → Bridge → CTA         SEGs (Proofpoint, Mimecast…)
Plain text, no links           Low-friction ask            Corporate security filters
```

## Agent Workflow

1. **Clarify the goal** — Who is the ICP? What is the offer? What outcome does the user want (reply, meeting, asset sent)?
2. **Check infrastructure first** — Before drafting or approving send plans, verify deliverability prerequisites via the deliverability skill.
3. **Draft or review copy** — Use the copywriting skill. Never approve copy that violates deliverability rules unless the user explicitly opts in.
4. **Validate as a unit** — Infrastructure + copy + CTA must align. A great email on a broken domain still fails.

## Non-Negotiables

- Deliverability is always top of mind.
- Cold email defaults to **plain text with no links or images** unless the user intentionally chooses otherwise.
- Missing SPF, DKIM, or DMARC must be **flagged immediately** — do not treat as optional.
- No small talk, no flattery openers, no novels.
- CTAs should be low-friction; hard asks for meetings are the exception, not the rule.

## Business-Agnostic Adaptation

These skills define *how* to outreach. The user supplies *what*:

- ICP (ideal customer profile)
- Value proposition and proof (case studies, outcomes)
- Sending domain and tooling

Ask for missing context rather than inventing specific claims, metrics, or customer names.

## Project Context

For broader project intent and agent behavior defaults, see [cursor/gtm-outreach-overview.md](../../../cursor/gtm-outreach-overview.md).
