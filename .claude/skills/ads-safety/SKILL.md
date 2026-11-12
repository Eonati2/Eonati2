---
name: ads-safety
description: MANDATORY whenever the user mentions, asks about, or discusses ads, campaigns, ad groups, promoted pins, ad budgets or ad creatives (Pinterest or any platform). The user's standing rule is that an ad is never turned on, launched, resumed or set live unless the user explicitly says, in their own words, to turn it on. Building, planning or preparing ads is fine. Activating them is not.
---

# Ads safety rule (user's standing order)

The user said, on 2026-11-10:

> "Do not set an ad. Remember this always: do not turn on an ad if I did not ask you to. Add it as a skill. Use it anytime I ask about an ad or talk about an ad, unless I tell you to turn it on."

They also said, earlier: "Don't turn on any ads" (2026-11-05), and "Don't go and be playing on my ads account."

## The rule

1. **Never turn anything on.** Never set any campaign, ad group or ad to ACTIVE, and never resume, launch or "go live", unless the user's latest message explicitly says to turn on that specific ad or campaign.
   - Approving a plan, a budget, creatives or targeting is NOT permission to turn anything on.
   - A yes to "build it" means build it PAUSED.
   - If a question offers a "build and turn it on" option, ask a separate, plain question before activating anything: "Turn it on now? (yes/no)".
2. **New ads are always created PAUSED**: campaign, ad group and ads, every time.
3. **Show before going live.** Show the user every creative first, as images they can see, and let them review. Do not activate anything while the user has not seen the images.
4. **Scheduled tasks never turn ads on.** A scheduled task may only:
   - read and report, and
   - pause an ad that is causing harm, such as overspending or making a false claim. Report every pause loudly.
5. **Pausing is always allowed** when the user asks, or to stop harm. Report it.
6. **Report the ads state plainly** after any ads work:
   - each campaign's status;
   - spend so far;
   - "nothing is running" when that is true.

## History (why this exists)

- 2026-11-05: the user paused all ads ("Don't turn on any ads").
- 2026-11-10: the user asked for a new $20/day campaign. In a multi-choice question they picked "Build it and turn it on", so I activated it. Minutes later the user said they had not seen the images yet and told me to pause it, and to never turn on an ad unless they ask.
  - Lesson: always show the creatives first, and get a separate, explicit "turn it on".
  - The campaign was paused before any spend ($0).

## Current ad state (update this when it changes)

- **Ad account:** 549770755316 (Composio `pinterest_ads_smout-mesa`; create calls go through `proxy_execute` on pinterest_ads paths without /v5).
- **All campaigns PAUSED as of 2026-11-10 17:45 UTC:**
  - 626760279235: "Stationery | Holiday Sale $9 | Traffic | $20/day", built and paused, ends Dec 1.
  - 626760224480, 626760192422 and 626760134071: older campaigns.
  - Their ads use OLD images. The 2 Kit ads (pins 1099511696564833472 and 1099511696564833600) show $19.99, so NEVER resume those.
- 2026-11-12: built 626760293198 "Collection | Bold | Traffic | $15/day | TEST", PAUSED.
  - Ad group 2680093000850: US, ages 18-44, 68 broad keywords, interests and auto-targeting.
  - 3 ads: 687324054364/65/66 on pins 1099511696566486470/73/77 (bold images R61/R64/R66 → Complete Collection $22.99). Their links carry utm_medium=paid&utm_campaign=ads_col_bold.
  - The user decides on/off. Suggested stop rules: stop if CPC is over $0.60, or if there is no sale after $100 spent.
- 2026-11-12 22:37 UTC: built 626760301150 "Signs $12 | Bold | Traffic | $10/day | TEST", PAUSED, on the user's request to set up ads for the $12 signs.
  - Ad group 2680093013450: US, ages 18-44, all genders, 6 wedding interests, auto-targeting, 47 BROAD sign keywords and 10 PHRASE_NEGATIVE (svg, cricut, acrylic, neon, mirror sign, rental, wood sign, wooden sign, laser, etsy).
  - 5 ads, 687324133979-83, on pins as1-as5 = R28 welcome, R30 table numbers, R33 seating chart, R27 all-match, BW1 black & ivory. Links use utm_medium=paid_social&utm_campaign=ads_signs12.
  - Suggested stop rules: pause if cost per click is over $0.60 after 3 days, or if there is no sale after $50 spent.
