# Deliverability Checklist — Reference

## DNS Verification (manual)

Agents can suggest the user run these checks. Replace `example.com` with the sending domain.

```bash
# SPF
dig TXT example.com +short | grep spf

# DKIM (selector varies — common: google, selector1, default)
dig TXT google._domainkey.example.com +short
dig TXT selector1._domainkey.example.com +short

# DMARC
dig TXT _dmarc.example.com +short
```

Online alternatives: MXToolbox, dmarcian, Google Admin (Workspace), Microsoft 365 admin centers.

## SPF Guidelines

- One SPF TXT record per domain (merge includes if needed).
- End with `-all` or `~all` — understand the difference (`-all` is strict).
- Include only active send sources (Workspace, SES, SendGrid, etc.).
- Remove unused includes — they expand the trust surface.

## DKIM Guidelines

- Enable signing in the ESP admin panel.
- Publish the provided CNAME or TXT records.
- Verify with a test send to mail-tester.com or similar (user-run).

## DMARC Guidelines

- Start: `v=DMARC1; p=none; rua=mailto:dmarc@example.com`
- Monitor reports before tightening to `quarantine` or `reject`.
- Alignment matters: From domain should align with SPF or DKIM domain.

## SEG-Aware Sending

When targeting enterprise ICPs:

| Factor | Recommendation |
|--------|----------------|
| Domain age | Prefer 30+ days warmed before volume |
| Link usage | Avoid in email 1; send after reply |
| Redirects | None on any landing page |
| SSL | Valid cert on all pages |
| Identity | Consistent company name, address, privacy policy where relevant |
| Content | Plain, conversational, not template-heavy |

## Red Flags (auto-flag)

- No DMARC record
- DKIM not signing outbound mail
- SPF missing or `+all` / overly permissive
- Free webmail From address on bulk outreach
- Link shorteners in cold email
- High image-to-text ratio
- Multiple different domains in From / Reply-To / link domain
