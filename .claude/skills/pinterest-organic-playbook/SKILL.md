---
name: pinterest-organic-playbook
description: How Eonati grows organic (free) Pinterest traffic for the wedding templates on Eonati8. Covers what the winning pins look like, keywords, boards, pin copy rules, the pin bank in Drive and the scheduled posting task. Use for any organic wedding pin work.
---

# Pinterest organic playbook (wedding templates, Eonati8)

Account: Composio `pinterest_erie-audit` (Eonati8). Organic only — see `pinterest-ads-playbook` for the user's no-ads rule.

## What works (Eonati8 data, Oct 6 – Nov 4 2026)
- Best pin: "EVERY GUEST KNOWS WHERE TO BE" (Kit) — 3,776 views, 23 outbound clicks (0.6%). Most of the top pins were also promoted, so their numbers include paid views.
- What the winners share:
  - a lifestyle photo (couple, flowers) at the top
  - one big bold sans-serif outcome headline
  - a product mockup on a phone and a card
  - a large CTA button that includes the price
- Flat cream-on-cream pins with no people performed worst.

## Pin rules
- Size 1000×1500.
- Top label in a gold pill saying what the product is.
- Headline of 5–8 words in bold Lato Black. The hook is one of: a problem ("No more 'where do I go?' texts"), an outcome ("Your whole weekend in one link"), a list ("9 signs every wedding needs") or a season ("Just engaged? Save this").
- The product fills the middle of the pin.
- CTA pill with the price (e.g. "GET ALL 9 SIGNS · $12"). Footer: "Shown with sample details, you add your own".
- Title of 45–90 characters, starting with the search keyword.
- Description of 220–330 characters in 3 sentences:
  - the keyword plus the problem or desire
  - what's included, with 2–3 related keywords
  - a CTA
- No hashtags, emojis, fake urgency, or "free" except "edit free in Google Slides".
- Each pin must be a genuinely new image; colour swaps don't count. Spread posts out (1 per run, 3 runs a day) instead of bursts.
- Links: `?utm_source=pinterest&utm_medium=organic&utm_campaign=organic_{kit|st|col}&utm_content=oNN`.

## Keywords (Pinterest US volume)
- wedding welcome sign: 4–5M
- wedding table numbers: 2–3M
- table numbers wedding: 1–2M
- wedding decor signs / wedding signs ideas: 100–500K
- wedding reception signs: 10–100K
- wedding menu / wedding program / wedding bar menu / wedding signage: 1–10K
- Don't use "seating chart" (1–2M), because we don't sell one.
- Season: wedding searches peak in January (engagement season runs December to Valentine's Day). Pin from November so pins rank by January.

## Boards (keyword names)
| Board | ID |
|---|---|
| Wedding Sign Templates | 1099511765217845300 |
| Wedding Stationery Templates & Signs | 1099511765217776770 |
| Wedding Weekend Guest Guides & Itineraries | 1099511765217717274 |
| Wedding Guest Experience | 1099511765217717272 |
| Wedding Welcome Sign Ideas (new 2026-11-05) | 1099511765217848417 |
| Wedding Table Numbers Ideas (new) | 1099511765217848418 |
| Wedding Planning Checklist (new) | 1099511765217848420 |

## Pin bank and automation
- Drive folder `organic-pin-bank` 1swx71RZUmqbYeixdKNtsq6C6RKP5Wcj7 holds 25 PNGs (O01–O25) and `manifest.json` (1MLtrUAKENPwoTLwkANGPtNJcgM_oMAr5). The manifest lists queue order, title, description, link, board and drive_id.
- 3 were posted on 2026-11-05 (queue 0–2).
- Scheduled task `trig_01CVyDZEmkM2P2KbwwzERnpB` posts 1 pin at 14:17, 18:17 and 22:17 UTC (US morning, afternoon and evening). It finds what's already posted by matching `utm_content=oNN` in pin links.
- 2026-11-05: added 17 pins (N01–N17) with AI wedding-scene backgrounds from BlogToPin (website rxrg42oldavvkbxbiikqkzwa, gpt-image-2, no text overlay, 14 credits). The user's real templates are composited on top, so the product shown is exactly what buyers get. Layouts: full-bleed photo, photo-top with a cream panel, real-scene mockup (sign on an easel or on a marble table), photo-top with a big number. Queue is now `manifest_v2.json` (1xVasc7IXfTCeqNkqgFBEt8UsKUK20Hpe), 42 items, with new pins first.
- BlogToPin credits are shared with the logo-pin task, which uses about 10 a day. Ask the user before spending more.
- When the bank is low, build the next batch with the same templates and new hooks. Ideas: welcome bag, destination wedding, winter wedding, minimalist, "no Canva", price anchor, out-of-town guests, engaged-this-Christmas.
- Old organic Kit pins link to `/LAUNCH15`, which expires Nov 7. Their links can't be edited because the pins were promoted, so new pins replace them.
