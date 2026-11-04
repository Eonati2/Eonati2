---
name: pinterest-ads-playbook
description: Rules, metrics and decision table for running Eonati's Pinterest ads (Guest Kit traffic test and later campaigns) — who may change what, which numbers to pull, how to judge results, and ad-policy limits. Use for any Pinterest Ads check, report, recommendation or change.
---

# Pinterest ads playbook

IDs are in `eonati-accounts`. Toolkit: `pinterest_ads`, base `https://api.pinterest.com/v5`.

## Hard rules
- **Touch the ads account only on the user's direct instruction.** Never create, edit, pause, delete or turn on any campaign, ad group or ad unless the user asked for that exact action in their own words. Making pins or images is NOT permission to create ads (the user objected on 2026-11-03 when 10 paused ads were created from new pins). Default for checks is read-only.
- **Only the user turns things ON.** Never set a campaign, ad group or ad to ACTIVE unless the user explicitly says so in their own words for that launch. Anything paused was paused on purpose — report it, don't re-enable it.
- Don't change running ads, budget or targeting during an agreed test window. Changes reset Pinterest's learning.
- Only when the user asks for new ads: build them as PAUSED, let them pass review, then ask the user before switching.
- The budget is the user's money and they have little of it — always state the money at risk and offer the cheaper option.
- Ad copy and images must be truthful: no fake deadlines ("first 7 days" when the code doesn't expire), no fictitious "was" prices, no claims the product doesn't support. If a running pin's image/text promises something that's no longer true, flag it before changing the offer.

## API notes
- Campaigns require CBO (no ad-group budgets).
- Keyword match types: `PHRASE`, `PHRASE_NEGATIVE` (not `NEGATIVE_PHRASE`).
- Existing promoted pins can't be edited (pin_edit restricted) — make a new pin + new ad instead.
- Set `customizable_cta_type: SHOP_NOW` on ads.
- Analytics columns that work: `SPEND_IN_DOLLAR, IMPRESSION_1, OUTBOUND_CLICK_1, CLICKTHROUGH_1, CTR, COST_PER_OUTBOUND_CLICK_IN_DOLLAR, TOTAL_PAGE_VISIT, TOTAL_CHECKOUT` (`CPC_IN_DOLLAR` is invalid). Latest 1-2 days are incomplete.
- Ad previews: `POST /ad_accounts/{id}/ad_previews {pin_id}` (JS page — read pin text via the `pinterest` toolkit on `pinterest_erie-audit` instead).
- Tracking links use `utm_source=pinterest&utm_medium=paid_social&utm_campaign=<campaign>&utm_content=<ad>`.

## Creative and copy rules (research 2026-11-04)
- Image is 1000×1500 (2:3). Put a 5–8 word benefit headline at the top. Keep the product large in the centre.
- Keep the bottom ~15% free of important text, because the Shop button covers it.
- Use a high-contrast background. Merlot/plum suits the brand and Pinterest's 2026 wedding colours; cream-on-cream pins disappear in the feed.
- The title's first 40 characters must hold the keyword (e.g. "Wedding Welcome Sign Template…"). Descriptions are about 220 characters: what it is, what it matches, "edit free in Google Slides", "Instant download".
- UTM for paid ads is `utm_medium=paid_social`. The first SP01–04 sales ads wrongly used `organic`.
- Top Pinterest search volumes (US): wedding welcome sign 4–5M, wedding table numbers 2–3M, table numbers wedding 1–2M, wedding decor signs / wedding signs ideas 100–500K. "Wedding seating chart" is 1–2M, but we don't sell one, so it is set as a negative keyword.
- With fewer than ~50 conversions a week, a sales goal stays in learning mode. Don't change budget, creative or targeting for 10–14 days. Scale by 20–30% at a time.
- BlogToPin AI generation spends paid credits, so ask first.

## What to report (every check)
Status of campaign / groups / ads (status, review_status, summary_status); spend vs cap; impressions; outbound clicks; CTR; cost per outbound click — by ad group and by ad; Pinterest Tag last fired; tag page visits/checkouts; real Gumroad sales (exclude $0 tests); offer-code uses; prices still at baseline.

## How to judge (Guest Kit, $19.99, ~ $14-15 kept per sale after discount + fees — approximate)
Day-1 baseline: CPM ~$12, outbound CTR 0.37%, $3.33 per click.

| Result after the test window | Decision to recommend |
|---|---|
| 1+ sale | Keep running; plan a Sales-objective test once the tag has ~10+ checkouts |
| Cost/click under ~$1.50, 40+ clicks, 0 sales | Product page is the bottleneck — fix page/previews before more spend |
| Cost/click over ~$2.50 | Creative/targeting problem — keep best ad, add new hooks, consolidate groups, or pause paid and go organic |

- Sales objective needs conversion history (~10+ tracked checkouts). With zero checkouts it guesses; don't recommend it as a shortcut.
- Expect ~1-3 buyers per 100 visitors for digital products (rule of thumb, not Eonati data). P(≥1 sale) = 1-(1-rate)^clicks.
- Lowest-risk levers, in order: better images (cheaper clicks) → consolidate into the audience Pinterest spends on → lower budget → free organic pins (Eonati8 gets ~11k monthly views).
