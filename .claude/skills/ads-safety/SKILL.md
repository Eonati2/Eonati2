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
- 2026-11-12 22:50 UTC: on the user's feedback ("Edit Free" reads like the product is free; we promote ONE product), I ARCHIVED ads 687324133979-83 and deleted their pins (as1-as5, including the black & ivory one). I replaced them with 4 price-first ads, 687324134400-03, on pins sp1-sp4 (1099511696566543679/81/84/86): R28 welcome, R30 table numbers, R33 seating chart, R27 all-12, all linking to the $12 Signs. Rule for ad copy: show the price ($12) up front, never use the word "free" in ad titles or descriptions, and promote only the $12 Signs. All still PAUSED.
- 2026-11-13 readiness audit:
  - Pinterest approved all 4 ads (687324134400-03).
  - All 6 campaigns are PAUSED, with $0 spent since Nov 5.
  - Old campaigns spent about $134 for 76 clicks (about $1.76/click) and made 0 sales.
  - Stop rules are now in the daily check task (trig_01GtHFrPzcHcweZ3frKsBdNX). Once the user turns 626760301150 on, pause it if:
    - it has spent $50 or more with no sale; or
    - after 3 days, cost per click is above $0.60.
  - Before that change, the daily check's rule "pause anything ACTIVE" would have paused the user's own launch. It now allows 626760301150 when the user explicitly turned it on.
  - The Signs page no longer says "edit free" anywhere. It now says "Edit in Google Slides, no paid software needed". Backup: Drive 18LwBHgIyeQb8YDSfDEiYuQsgRi7THHT9.
  - CORRECTION after the user's test purchase: buyers SEE the MCP field custom_receipt_text in the receipt email and on the thank-you page. The API field custom_receipt holds Slides links but is not what shows.
    - On 2026-11-13 I rewrote custom_receipt_text: "edit free" is gone, and it now has the SIGNSBUYER4 $10.99 Guest Guide line.
    - On 2026-11-13 I changed the download page (rich content) line to "Edit in Google Slides: open a link…". Backup: Drive 1xYaz4Obs2rAC_VqZSDzxPuJ9kqquw_Yl.
      - It DOES work through proxy_execute PUT /v2/products/<permalink> with body {'rich_content': <list object, not a JSON string>}.
      - Verify with a GET afterwards: only updated_at should change.
  - 2026-11-13 18:44 UTC: the user made a test purchase while logged in as the creator, so Gumroad marked it "test purchase": no sale was recorded and the code was not used. The Pinterest tag fired at 18:44:37 UTC, the same minute. TAGTESTMUF9 is now deleted. The tracking test is DONE.
- 2026-11-13: removed "edit free" from the Collection, Kit and Black & Ivory pages, on the user's request ("pick the best choice to help sell").
  - Changed on each: description, summary, download page (rich_content) and receipt (custom_receipt_text).
  - Added a "Price" row at the top of each details box.
  - Black & Ivory had NO receipt text; it now has one, with the button "Download Your Signs".
  - Backup: Drive 1FnTQ2ILokAHzSXDfZvKrPAF_c8vhLIkq.
  - "Free" now appears only where it is accurate: the fonts (Lato, DM Serif Display) and the free checklist.
- 2026-11-14: the user asked to clean up the ad account and picked "archive all 5 old ones". I ARCHIVED 626760134071, 626760192422, 626760224480, 626760279235 and 626760293198.
  - Archiving is permanent, and their spend history ($134) is kept.
  - The ONLY campaign left is 626760301150 "Signs $12", PAUSED, waiting for the user's yes.
  - Pinterest cannot delete campaigns; it can only archive them.
- 2026-11-14: the user asked to optimize for BUYERS, not clicks. I built a new campaign, 626760313243 "Signs $12 | BUYERS | Conversions-Checkout | $10/day | Women 25-44", PAUSED.
  - Objective WEB_CONVERSION, optimizing for CHECKOUT on tag 2613086207584, with automatic bid. Attribution windows are not allowed with auto bid.
  - Ad group 2680093030772: US, women, ages 25-44, the same 6 interests, auto-targeting, and the same 47 keywords + 10 negatives.
  - 4 ads, 687324246724-27, PAUSED, Pinterest review PENDING.
  - The ads run on new pins sc1-sc4 (1099511696566656147/49/51/52), with utm_campaign=ads_signs12_conv.
    - sc1 = R28 rebuilt as "Instant download · print up to 18x24" (no "free"); Drive 1nKcTN_785tPnBwpspNoPgCpUdJJPUnyH.
    - sc3 description no longer says "9 more".
  - The old traffic campaign 626760301150 is still PAUSED; I recommended the user archive it.
- 2026-11-14: the user approved the 4 BUYERS ad images and asked to archive the traffic campaign 626760301150 (now ARCHIVED). The ONLY non-archived campaign is 626760313243, PAUSED.
  - Ads 25 and 27 were APPROVED; 24 and 26 were PENDING.
  - The user plans to launch Monday Nov 16. A reminder is set: trig_01XTu2DRP8amZnkVFNwi9UVy, 13:30 UTC. It only ASKS; turn the campaign on only on the user's new "yes".
  - Keyword volumes validated with Pinterest keywords/metrics (US):
    - wedding welcome sign 4-5M; wedding table numbers 2-3M; wedding seating chart 1-2M; table numbers wedding 1-2M; budget wedding ideas 1-2M;
    - welcome sign wedding and seating chart wedding 500K-1M each; wedding sign ideas, wedding signs ideas, wedding bar sign, modern wedding signs and wedding decor signs 100K-500K each.
    - All of these are in the ad group.
  - Interests: Wedding Invitations, Wedding Timeline, Wedding Planning, Wedding Rehearsal, Hotel Wedding, Destination Wedding.
