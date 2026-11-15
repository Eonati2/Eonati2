---
name: luxury-agent-outreach
description: Use when finding, emailing, following up with, or selling to luxury real estate agents for Eonati — "find more leads", "write the cold emails", "run the next outreach batch", "someone replied, what do I say", "how are the numbers", "build the preview mockup". Covers the free lead pipeline (Google Maps → agent site → verified email + hero image), the offer, human-sounding copy, reply handling, compliance, and the metrics that decide when to scale or stop.
---

# Luxury Agent Outreach

Goal: $10k–$20k/month selling brand and listing-presentation work to luxury real estate agents.
The CRM is the Google Sheet **"Eonati — Luxury Agent Outreach CRM"**
(`1sTEs3fzfJxWQsO4A7xc-nChoglk0ZzcPthxcF9AVqrA`): tab `Sheet1` = leads and pipeline, tab `Metrics` = live numbers.

## Three rules, in priority order

1. **Solve a real problem and prove it before you pitch.** Luxury sellers interview 2–3 agents
   before signing, and the listing presentation is where the listing is won or lost. Every email
   offers a free, specific, personalized preview. We never lead with a price.
2. **Protect the sending reputation above everything else.** One burned domain costs weeks.
   Verify every email address, warm up the inboxes, keep the volume low, and stop on the thresholds below.
3. **Only use real proof.** Never write, buy, or imply reviews or results that did not happen.
   (The FTC's rule on fake reviews and testimonials allows civil penalties.) Proof comes from the
   beta-client program below.

## The offer (what we sell)

| Tier | What it is | Price | Role |
|---|---|---|---|
| Free preview | One-page mock-up of a listing-presentation cover in the agent's branding | $0 | The hook. Sent only after they say yes. |
| Signature Listing Kit | Custom listing presentation (10–14 pages: their stats, process, pricing-strategy page, marketing plan) + matching one-property flyer | $750 | Core entry offer |
| Luxury Brand Suite | Kit + monogram or wordmark refresh + color and type system + social templates | $1,500–$2,500 | Main revenue driver |
| DIY template | Canva listing-presentation template (sell on Gumroad, store `eonati`) | $97 | Downsell for "not now" and "too expensive" replies |

**Path to $10k/month:** about 5 Brand Suites, or 3 Suites plus 6 Kits. Swap the estimates for real
numbers once you have sent 300 emails (the `Metrics` tab calculates "emails needed for $10k").

### Beta proof program (first 5 clients)
Offer the Kit at $250 (or free) to the first five agents who reply positively, in exchange for:
(a) a written testimonial in their own words, (b) permission to show the before and after, and
(c) a follow-up check 60 days later ("did it help you win a listing?"). Publish only what they actually wrote.

## Lead pipeline (free, runs in the Composio workbench)

Script: `outreach/lead_pipeline.py`. Steps:
1. `GOOGLE_MAPS_TEXT_SEARCH`: "luxury real estate agent {market}" (20 per query). Rotate query
   variants: "waterfront homes realtor", "Sotheby's agent", "Christie's agent", "estate homes agent".
2. Fetch each website with `requests` from inside the workbench. (Hyperbrowser's free plan is limited
   to 1 session at a time, so don't use it in bulk. This cloud sandbox blocks direct outbound HTTP.)
   Also follow the /contact or /about link.
3. Score each email found on the site: name match +3, site-domain match +2, generic inbox +1. Keep only scores of 2 or higher.
4. Pull the `og:image` meta tag. That's the agent's own hero image, used only for their private preview.
5. Verify with `MAILS_SO_VALIDATE_SINGLE_EMAIL`. Set priority: **A** deliverable → send first,
   **B** unknown → send after the A batch if bounces stay under 2%, **X** risky/undeliverable → never email,
   **C** no email → phone or contact form.
6. Write to the CRM. Never add a duplicate: check the email and website columns first.

First run (Nov 2026): 8 markets → 146 agents with websites → 51 emails → 25 A, 21 B, 5 X.
That's about 35% of sites yielding a usable email.

## Sending infrastructure (do this before the first send)

- **Never send cold email from the personal Gmail.** Buy 2 lookalike domains (for example eonatistudio.com,
  eonati-design.com) and point their root at the main site.
- Create 2 inboxes per domain (Google Workspace or Microsoft 365) with real names and photos.
- Set up SPF, DKIM, and DMARC (start with `p=none`), and a one-click unsubscribe or a plain "reply no" opt-out.
- Warm up for 14–21 days. Then send at most **30/day per inbox** in weeks 1–2 and 50/day after that.
- Sender options: the Instantly connection exists, but the workspace currently has **no paid plan (API returns 402)**.
  Reactivate it for warmup and rotation, or start at low volume by sending from Gmail through Composio
  (`GMAIL_SEND_EMAIL`) and logging every send in the CRM.
- Send plain text only: no images, no links, no tracking pixels in email 1.

## Copywriting rules (sound like a person, not a marketer)

- Under 90 words. Short sentences. One idea. One easy yes/no question.
- The first line must prove you looked: their review count, a neighborhood they own, their sales volume, or a line from their site title.
- Lowercase, 2–4 word subjects that look internal: `your naples listing deck`.
- Ban these: "I hope this finds you well", "synergy", "revolutionary", "game-changer", "quick call",
  exclamation marks, fake "Re:" subjects, and false urgency.
- Ask permission before sending the preview. A "sure, send it" reply is the conversion we want,
  and it means the image goes only to someone who asked for it.
- Always include a real sender name, a physical mailing address, and a way to opt out (CAN-SPAM).

### Sequence

**E1 (day 0).** Subject: `your {market} listing deck`
> Hi {first_name},
>
> {personal_line — e.g. "53 five-star reviews on Google is rare, even in Naples."}
>
> Most luxury sellers interview two or three agents now, and the listing presentation tends to decide it.
> I design those for agents, and I made a one-page mock-up of a presentation cover in your branding,
> using the hero photo from your site.
>
> Want me to send it over? It's free, and I won't ask for a call.
>
> {sender_name}
> Eonati · {mailing address}
> (Reply "no" and I won't email again.)

**E2 (day 3, same thread).**
> {first_name}, one more idea that comes up a lot: a single "how we priced your home" page with three comps
> and a chart. Sellers trust a number they can see. I can add that to the mock-up too, if it'd be useful.

**E3 (day 7, same thread, breakup).**
> I'll leave it here. If a listing appointment comes up and you want a sharper presentation, just reply
> "deck" and I'll send the mock-up. Good luck this season.

### Reply playbook

| Reply | Do this within 2 hours |
|---|---|
| "Sure / send it" | Send the preview PDF and 3 lines: what it is, what the full Kit includes, the price, and a payment link. Set Stage to Preview sent. |
| "How much?" | Give the price plainly ($750 Kit, $1,500 Suite) and offer the beta rate if a beta slot is open. |
| "Not now" | Thank them, offer the $97 DIY template link, and set Stage to Nurture (check back in 90 days). |
| "No / remove me" | Apologize in one line, set Stage to Unsubscribed, and never email them again. |
| Angry | Same as "No". Log it, because it counts toward the complaint rate. |
| Bounce | Set Stage to Bounced and pause the inbox if the bounce rate goes over 2%. |

## Metrics (check daily in the `Metrics` tab)

| Metric | Healthy | Stop and fix |
|---|---|---|
| Bounce rate | < 2% | > 2%: pause, re-verify the list |
| Complaints / angry | < 0.1% | > 0.1%: pause and rewrite (Gmail's hard ceiling is 0.3%) |
| Reply rate | 3–5% (top senders 5%+) | < 1% after 200 sends: change the first line and the offer, not the volume |
| Positive → preview | > 50% | < 30%: the preview isn't compelling |
| Preview → paid | 20–30% | < 10%: fix the offer or the price, collect objections |

Every reply gets a Stage and a Reply type. A lead isn't "done" until its Stage is Won, Lost, Nurture, or Unsubscribed.

## Building the preview

Use the agent's `og:image` hero image as the cover photo, with their name, brokerage, a serif headline
("Presenting Your Home"), and their real stats from their site. Export a single-page PDF. Treat it as a
private, one-to-one sample: never publish it or use it in Eonati marketing without written permission,
because listing photos are usually copyrighted by the photographer.
