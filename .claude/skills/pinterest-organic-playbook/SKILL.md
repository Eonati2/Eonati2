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

Before writing or approving any pin copy, image or product page, run the "Will this work?" check in `sell-anything`, and read its LESSONS LOG. After each weekly review, add what worked or failed to that log.

## Pin rules
- **WEDDING RULE (user, 2026-11-05: "Always add wedding on the title image so buyers can know and not scroll… never forget this").** The big headline on EVERY pin image must contain the word "Wedding". This applies to my pins, refills, weekly batches and BlogToPin `titleToUse` text. A label pill alone doesn't count. The posting task skips any manifest item whose `headline` lacks it.
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
- **Stationery Suite is the main product.** About 2 of every 3 organic pins should be Stationery. The queue is now `manifest_v3.json` (1iNl0uwD_KoD3eKEbp--jmImWDmAqH73q) in the pattern Stationery, Stationery, then Kit or Collection.
- Copy rewritten 2026-11-05 as `manifest_v4.json` (1aApdDpV5E14yB27zIrXok_PF9L5fO_Z_). Title = keyword + emotional hook. Description = hook, fix with keywords, true reasons to buy, CTA with price. The Pinterest API can't edit live pins (`pin_edit` is restricted), so get the copy right before posting.
- BlogToPin (website rxrg42oldavvkbxbiikqkzwa) can only schedule its own AI pins; it can't upload ours. Its active boards are Wedding Guest Experience, Guides & Itineraries and Guest Essentials. The sign boards aren't linked there. Its auto copy is weak ("Tap to learn more"), so always overwrite it with CUSTOM_BLOGTOPIN_UPDATE_PIN (pinterestTitle + description). Check AI images for invented products: a sign set showing 'Guest Book' or 'Table Assignments' was left unscheduled. On 2026-11-05, 9 AI pins were scheduled for Nov 6–10 at 16:05 and 20:05 UTC.
- BlogToPin credits are shared with the logo-pin task, which uses about 10 a day. Ask the user before spending more.
- When the bank is low, build the next batch with the same templates and new hooks. Ideas: welcome bag, destination wedding, winter wedding, minimalist, "no Canva", price anchor, out-of-town guests, engaged-this-Christmas.
- Old organic Kit pins link to `/LAUNCH15`, which expires Nov 7. Their links can't be edited because the pins were promoted, so new pins replace them.

## Goal and pace (user, 2026-11-05)
- **Goal:** 2M monthly views, then sales. Rough math: 2M views × 0.6% click-through ≈ 12k visits ≈ 120–360 sales at 1–3% conversion. $10k a month needs about 1,000 Stationery sales, or bigger orders through the $27.99 bundle.
- **Biggest missing product: "wedding seating chart" (1–2M searches a month).** Also check unplugged, cards & gifts and guest book signs. Adding these to the Stationery Suite is the strongest lever. It's a product change, so ask the user first.
- **Trending wedding searches** (yearly): "future wedding plans", "fun natural table settings".
- **Pace:** my scheduled task posts 5 pins a day (13, 15, 17, 19 and 21:17 UTC) from `manifest_v5.json` (1KWNGvrkgf3Vkjwf-BYg9jBVuKIx333_K, 58 items). BlogToPin posts 2 a day (16:05 and 20:05 UTC).
- **New layouts (om##):** before/after, POV, price stack, search bar, big word, checklist over a photo. The design code is saved as `pinlib.py` in Drive (1TUePKPgld0LPCJ8kooju067k8O9iBJ16). Reload it after a workbench crash: download it plus the fonts, the src crops and the AI backgrounds (BlogToPin jobs 189633–189652).
- **Weekly review:** `trig_01MKCmgF9P7HsRjWXEUKpfzA` runs Mondays at 16:43 UTC. It ranks pins by layout and hook, then builds the next batch from the winners.
- **2026-11-05: the Stationery Suite is now 12 signs (V3).** Added a seating chart, an unplugged ceremony sign and a cards & gifts sign, at the user's request.
  - Google Slides decks: US 1A7TPd…, A4 1PR-dM… (both are linked in the receipt). They now have 12 slides.
  - PDFs: the original 9 pages are unchanged, with the 3 new pages appended.
  - PPTX: the 3 slides were duplicated with python-pptx.
  - Gumroad files: Stationery embed is now `-xCHHC5C2DW1yQ_VchJvwA==`; Collection embed is `wrF8LHKTGtaNtKcZN86_YA==`.
  - Backups of the V2 zips and decks are in the Drive backups folder.
  - Name: "Wedding Sign Templates: Welcome Sign, Seating Chart, Table Numbers & Menu Set". Price is still $12.
  - The pin queue is `manifest_v6.json` (1R6wNCtOTvZmQzcmDXy5yAEW2x9jBaU-A), with seating-chart pins first.
- **Pace from 2026-11-05 (user):** 12–15 pins a day.
  - The posting task `trig_01CVyDZEmkM2P2KbwwzERnpB` runs hourly from 09:17 to 21:17 UTC (13 a day) and always reads the newest `manifest_v*.json`.
  - BlogToPin adds 2 a day.
  - The refill task `trig_01PSAzq6z1betudCwHrDPaWc` runs every 3 days and builds 40 pins when fewer than 40 are queued.
  - The design code is `pinlib_v2.py` (1fDiQgqMT-gYmfjV34EPxj1jxvgSRQWTB), which adds L_price, L_top and an auto-fitting L_word.
  - `manifest_v7` holds 88 items: seating-chart pins S01–S04 first, then R01–R26 mixed in (12-sign messaging and a "$1 per sign" price anchor).
- **2026-11-05 BlogToPin 30-day schedule:** 54 pins scheduled at 16:05 and 20:05 UTC, Nov 6 – Dec 3 (9 b## pins plus 45 c## pins).
  - z-image-turbo (0.2 credits each) misspelled 16 of 51 headlines. Always check a contact sheet before scheduling.
  - Redoing failures on gpt-image-2 (0.7 each) fixed all 10 I redid. Pins still misspelled were dropped, never posted.
  - Credits: 79.9 → 62.5.
  - Links use `utm_campaign=blogtopin_*&utm_content=c##`. Copy was overwritten with UPDATE_PIN.
- **2026-11-05 wedding-headline fix:**
  - 43 queued pins had no "Wedding" in their image headline. They were rebuilt as W01–W43 (`utm_content=ow##`, same queue slots, copy fixed from "9 signs" to "12 signs").
  - Queue is now `manifest_v9.json` (11mXZgYya3tsVYXpn8dQlNz84yGsdVyHT), 88 items, all compliant.
  - Build assets live in Drive so a workbench reset can't lose them:
    - fonts and product crops: `pin_assets_fonts_src.zip` 1FQ8cXYYlA-Z_WWhTNBgIiCUemIcPJp65
    - AI backgrounds: `pin_assets_ai_bg.zip` 1ZZOtz4TF5Qa_KvgehKoa3YoB8kbMcp1o
    - build script: `wspecs_wedding_headlines.py` 14yEXqZgtQJlnpcJl6MVrTpEDY_AurGMC (loads pinlib_v2 and adds L_full, plain and footer)
  - The workbench resets every few calls. Keep cells small, save to Drive right away, and work under `/home/user/eon`.
  - BlogToPin: 37 of the 54 scheduled pins had no "Wedding" in their baked-in image text. They were set to PIN_REJECTED (reversible with APPROVE_PINS). The 17 compliant ones stay scheduled.
  - Replacing the 37 would cost about 26 credits on gpt-image-2. Ask the user first.

