---
name: cold-email-deliverability
description: >-
  Audits and guides cold email deliverability — plain text sending, SPF/DKIM/DMARC,
  ESP setup, recipient filters, and SEG awareness. Use when reviewing sending
  infrastructure, inbox placement, DNS records, email authentication, spam
  filters, Proofpoint, Mimecast, Barracuda, or deliverability before a campaign.
---

> Built for **Claude Code** (and compatible agent harnesses). Drop into `.claude/skills/`.

# Cold Email Deliverability

Deliverability is always top of mind. Legitimate cold outreach shares the same filtering environment as spam. Infrastructure and message format must earn inbox placement before copy or offers matter.

## Agent Responsibilities

When deliverability is in scope:

1. **Audit before send** — Check DNS auth, message format, and recipient-environment risks.
2. **Flag blockers immediately** — Missing SPF, DKIM, or DMARC is a hard stop. Do not recommend sending until resolved.
3. **Default to safest format** — Plain text, no links, no images, unless the user explicitly chooses otherwise.

## Message Format Rules

### Default (best practice)

- **Plain text only** — No HTML templates, no rich formatting.
- **No links** — URLs trigger marketing/spam heuristics. Omit unless intentionally doing so with eyes open on risk.
- **No images** — Same rationale as links.
- **No attachments** in initial cold touches — increases filter scrutiny.

### When links or assets are intentional

If the user explicitly wants links (calendar, deck, video):

- Acknowledge deliverability tradeoff.
- Prefer sending the asset **after** a positive reply.
- Ensure domain reputation, DNS auth, and landing pages are solid (see SEG section).

## Sending-Side Infrastructure

Every sending domain or inbox — Google Workspace, Microsoft 365, or custom SMTP — must have proper DNS authentication.

### Required DNS records

| Record | Purpose | Agent action |
|--------|---------|--------------|
| **SPF** | Authorizes which servers may send for the domain | Verify present and includes only legitimate send sources |
| **DKIM** | Cryptographic signature proving message integrity | Verify signing is enabled and DNS publishes the public key |
| **DMARC** | Policy for failed SPF/DKIM; reporting | Verify policy exists (start with `p=none` for monitoring if needed, tighten over time) |

**If any of SPF, DKIM, or DMARC is missing or misconfigured → flag immediately.** Deliverability will suffer; do not proceed as if send-ready.

### Additional sending hygiene

- Use a **dedicated outreach domain** or subdomain when possible — protects primary brand domain.
- Warm new domains/inboxes gradually — volume spikes hurt reputation.
- Align **From** domain with DKIM signing domain.
- Keep bounce and complaint rates low; remove invalid addresses promptly.
- Match reverse DNS (PTR) where applicable on custom SMTP.

## Recipient-Side Environment

Prospects receive mail through varied stacks. ICP often determines the mix.

### Common recipient ESPs

- **Google (Gmail / Workspace)** — Strong filtering, engagement signals matter.
- **Microsoft (Outlook / M365)** — Similar; sensitive to authentication failures and bulk patterns.
- **Third-party / custom SMTP** — Variable rules; authentication failures are penalized heavily.

The "handshake" between sender and receiver depends on authentication, reputation, content signals, and engagement history.

### SEGs (Secure Email Gateways)

Corporate inboxes often sit behind SEGs that add layers beyond native ESP filtering:

- Proofpoint
- Barracuda
- Mimecast
- Cisco IronPort / others

**Implications for outreach:**

- Authentication must be flawless — SEGs are stricter than consumer Gmail.
- **Domain reputation** and **domain age** matter more.
- **Domain masking** — Sending domain should look legitimate and aligned with the business (not deceptive; professional and consistent).
- **Landing pages** — If links are used later, pages must be trustworthy: valid SSL, clear business identity, no redirect chains, no mismatch between email domain and link domain.
- Plain-text-first cold touches reduce SEG triage into "marketing" buckets.

When ICP is enterprise or regulated (healthcare, finance, government), assume SEG presence and apply stricter infrastructure standards.

## Pre-Send Checklist

Copy this checklist and work through it:

```
Deliverability audit:
- [ ] SPF record present and correct for sending source
- [ ] DKIM enabled and DNS key published
- [ ] DMARC record present with sensible policy
- [ ] Sending domain aligned with From address
- [ ] Message is plain text (unless user opted into HTML/links)
- [ ] No links or images in initial touch (unless intentional)
- [ ] Volume appropriate for domain/inbox age
- [ ] Recipient environment considered (consumer vs corporate/SEG)
- [ ] Landing pages valid if links will be used in follow-ups
```

## Audit Output Format

When reviewing a user's setup or draft campaign, respond with:

```markdown
## Deliverability Assessment

### Status: [READY | NEEDS WORK | BLOCKED]

### DNS Authentication
- SPF: [✅ / ⚠️ / ❌] — [detail]
- DKIM: [✅ / ⚠️ / ❌] — [detail]
- DMARC: [✅ / ⚠️ / ❌] — [detail]

### Message Format
- [plain text / HTML / links / images] — [pass or flag]

### Recipient Risk
- ICP environment: [e.g. corporate + likely SEG]
- Notes: [specific risks]

### Required Actions (ordered)
1. ...
```

## Why This Matters

Good deliverability plus relevant messaging lets legitimate offers reach the right person. One inbox placement can start a conversation with real impact — but only if authentication, format, and trust signals are in place first.

## Reference

For DNS check commands and SEG notes, see [checklist.md](checklist.md).
