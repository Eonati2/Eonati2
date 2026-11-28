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
- 2026-11-15: the user explicitly ordered: "Yes It sets the ad to automatically on at the time on Monday,12am to start running". For the time zone they said "Pick the best time frame for our target audience", so I chose Mon Nov 16 12:00am US Eastern (05:00 UTC), when the US day starts.
  - All 4 ads (687324246724-27) were APPROVED on 2026-11-15.
  - Pinterest cannot schedule this campaign itself: start_time can't be changed after creation (error 1511), and a CBO ad group can't have a start_time (error 2919). Nothing was changed by those failed attempts.
  - So a one-time task, trig_01LeNR2oUEG2CqqGeWoKRbrJ (fires 2026-11-16 05:00 UTC), turns on the ads, the ad group and the campaign, then verifies them. This is the user's own explicit turn-on for this ONE campaign only.
  - Until then, everything stays PAUSED.
  - trig_01XTu2DRP8amZnkVFNwi9UVy (13:30 UTC Mon) is now a report-only launch check.
  - The daily check (trig_01GtHFrPzcHcweZ3frKsBdNX) now treats 626760313243 as allowed from 05:00 UTC Mon. Stop rule: pause it at $50 spent with 0 real sales.
- 2026-11-16 ~04:20 UTC: on the user's "yes, change it to Shop now", I set customizable_cta_type=SHOP_NOW on ads 687324246724-27. The default had been "Visit site" (the field was empty).
  - Afterwards all 4 were still APPROVED and PAUSED; campaign and ad group still PAUSED.
  - Correction: ads DO have a settable button field (customizable_cta_type). I had wrongly told the user regular image ads can't change it.
  - The scheduled 05:00 UTC turn-on (trig_01LeNR2oUEG2CqqGeWoKRbrJ) is unchanged.
- 2026-11-16 05:01 UTC (12:01am ET, 7:01am Cyprus): the scheduled launch ran, as the user ordered. Since 2026-11-15 they had confirmed several times: "OK, let it turn on at 7am".
  - Campaign 626760313243 is now ACTIVE and running, renamed "Signs $12 | BUYERS | Conversions-Checkout | $10/day | Women 25-44".
  - Ad group 2680093030772 and all 4 ads (687324246724-27) are ACTIVE and APPROVED, with the SHOP_NOW button. Daily cap is $10.
  - No other campaign is non-archived.
  - Stop rule: pause it if $50 is spent with 0 real sales. This campaign is ALLOWED to run; do not pause it just for being active.
- 2026-11-17: the user paused BUYERS 626760313243 (spent $16.32 since Nov 16, 0 sales). After a full review (Kit ads got 2-5x the click rate of Signs ads; a checkout campaign can't learn with 0 sales), the user said "yes, build it paused". Built:
  - Campaign **626760338310** "Kit $14.99 | Traffic | $12/day | Women 25-44 | US CA UK AU", CONSIDERATION, CBO, $12/day, **PAUSED**.
  - Ad group **2680093069045**: women 25-44, US/CA/GB/AU, en, the same 6 wedding interests, auto-targeting on, billed per click, 28 BROAD guest-guide/itinerary/welcome-bag keywords + 17 PHRASE_NEGATIVE (dress, hair, makeup, gift, svg, etsy, free…). **PAUSED**.
  - 4 ads, **687324506404-07** (K1-K4), SHOP_NOW, **PAUSED**, review PENDING. Pins 1099511696566927045/48/51/56 (images or57, ow32, or98, or23), links utm_campaign=ads_kit_traffic&utm_content=k1..k4.
  - The user has seen the 4 images. NOTHING is on. Turn on only on a new, explicit "turn it on".
  - Suggested stop rules: pause if cost per click is over $1 after 3 days, or after $50 spent with no sale.
  - 2026-11-17 20:00 UTC: added video ad **687324507353** "K5 | VIDEO phone guide scroll" (12 s, 2:3, video pin 1099511696566927581, utm_content=k5video) to ad group 2680093069045, **PAUSED**. The user has seen the video. Campaign 626760338310 is still PAUSED; turn on only on an explicit "turn it on".
- 2026-11-17 ~20:20 UTC: on the user's "only image for the ads", ARCHIVED the video ad 687324507353. Added 4 premium image ads to ad group 2680093069045, all **PAUSED**: **687324509620-23** (P1 "answer every question once", P2 "welcome bag card", P3 "destination: right place", P4 "texts answered before asked"), pins 1099511696566929509/12/15/16, utm_content p1..p4.
  - The images use AI photo bases (ElevenLabs Seedream) with the real guide pages composited onto green screens; "wedding" is in every headline; no "free".
  - The user has seen them. Campaign 626760338310 now has 8 paused image ads (K1-K4 + P1-P4). Still PAUSED. Turn on only on an explicit "turn it on".
  - Signs pricing decision (user, 2026-11-17): keep $12 and sell mainly through the Collection.
- 2026-11-17 ~20:45 UTC: on the user's "make all text bold and readable", rebuilt P1-P4 with larger bold text and made new pins 1099511696566930930/32/37/39. The new ads are **687324510599-602** (P1b-P4b), SHOP_NOW, **PAUSED**. The old P ads 687324509620-23 are ARCHIVED. The campaign still has 8 paused ads (K1-K4, P1b-P4b). Nothing is on.
- 2026-11-17 21:05 UTC: P2b showed a hand-drawn 5x7 card that did not match the real product card. I replaced it with **P2c 687324511461** (pin 1099511696566932202), which shows the real 5x7 card exported from the buyer Slides deck. P2c is PAUSED with SHOP_NOW; P2b 687324510600 is ARCHIVED. The Kit campaign's 8 ads are now K1-K4 (687324506404-07), P1b 687324510599, P2c 687324511461, P3b 687324510601 and P4b 687324510602. All PAUSED.
  - Checked: the small flower on the Signs designs IS in the real product (it's a vector shape in the Slides decks), and the Blush Rose roses ARE in its PDFs and PPTX files.
- 2026-11-18 ~07:00 UTC: after a full readiness check (all 8 Kit ads APPROVED, SHOP_NOW, links 200 at $14.99, Pinterest tag on page + receipt), the user explicitly said **"Turn the ads on"**. This turns on ONLY the Kit campaign **626760338310**, ad group 2680093069045 and its 8 ads (K1-K4 687324506404-07, P1b 687324510599, P2c 687324511461, P3b 687324510601, P4b 687324510602). BUYERS 626760313243 stays PAUSED. Kit campaign is ALLOWED to run; the daily check must not pause it just for being active. Stop rules: pause if cost per click is over $1 after 3 days, or after $50 spent with 0 real sales.
- 2026-11-18 ~18:00 UTC: user chose option **A**: let Kit campaign 626760338310 run the full 7 days (Nov 18-24, max ~$84). The old "$50 with 0 sales" stop rule is REPLACED by: pause only if spend reaches $90 with 0 real sales, or on/after Nov 24 if click rate < 0.3% AND 0 started checkouts. Checkpoint Nov 20 (recommend trimming 0-click ads, US budget, keywords — user approval needed); final verdict Nov 24. Day-1 leaders: K2 (0.60% CTR, 3 clicks) and P3b.
- 2026-11-19 ~07:15 UTC: user role instruction: "You are the ads manager and CEO to help us reach our goal so always guide me based on data and metrics and researching deep." Meaning: lead with a clear data-backed recommendation every time (what to do, why, expected result, risk), not just reports; research benchmarks before advising. This does NOT remove the approval rule: Claude still never turns on, scales, edits or creates ads, budgets, targeting or prices without the user's explicit yes. Recommend, then wait for approval.
- 2026-11-19 ~05:00 UTC: user said "Turn off the ones that are not working, and replace them based on the ones working." PAUSED K4 687324506407, P1b 687324510599, P4b 687324510602 (0 clicks on 767 views). Backup of prior ad states: Drive 1QSoA5zBXFmHclkJnzgk0hu8mNoGKiXip. Built 3 replacements from the winning layouts (real wedding photo + real product mockups), created **PAUSED** with SHOP_NOW, awaiting Pinterest review and the user's explicit turn-on: K5 687324648871 (weekend timeline, pin ...036486, utm k5), K6 687324648872 (destination, pin ...036488, utm k6), K7 687324648874 (day timeline, pin ...036490, utm k7). Preview: marketing/ads_kit/replacements_preview.jpg. Kit campaign stays ACTIVE with K1, K2, K3, P2c, P3b.
- 2026-11-19 ~05:10 UTC: user: "Let me see the new images first... well optimized for buyers... always learn from your winning ones." Reviewed drafts, fixed flaws (K7 ghost text, empty gap/no product in K5-K6), so first-draft ads 687324648871/72/74 are ARCHIVED and their pins deleted. Current replacements, all **PAUSED**, waiting for Pinterest review AND the user's explicit turn-on: **K5 687324649245** (pin 1099511696567036823), **K6 687324649246** (pin ...036826), **K7 687324649247** (pin ...036828). Images: marketing/ads_kit/K5_ad.jpg, K6_ad.jpg, K7_ad.jpg.
- WINNING-AD RULES (learned from data, apply to every new ad): bright real wedding photo with people (bride/guests); big bold serif headline containing "wedding" + a searched phrase (timeline, destination); show the real product (phone guide + 5x7 card mockup); price visible ($14.99); bullet list of what's included; SHOP_NOW button. Losers had: no people (graphic/chat bubbles, hand-only close-up) or a dark/low-contrast photo. Always self-review images at full size before showing the user.
- 2026-11-19 ~05:20 UTC: user said **"Fix it"** to recommendations #2 (country budget) and #3 (keywords). Backup: Drive 1kF4ax16hx8LHj5jxx8e1VZ1zN586QyUn. Applied: (a) Kit campaign 626760338310 daily cap $12 -> **$8**, renamed "...$8/day | CA UK AU"; ad group 2680093069045 LOCATION now CA, GB, AU (US removed). (b) Added 14 broader BROAD keywords (wedding timeline, wedding day timeline, wedding timeline template, wedding schedule, wedding day schedule template, wedding itinerary card, wedding itinerary for guests, wedding weekend itinerary template, destination wedding planning, destination wedding guest guide, destination wedding welcome bag, wedding welcome bag itinerary, wedding guest information card, wedding weekend agenda). Finding: most long "timeline/itinerary" phrases were ALREADY there with ~0 views, so the gap is search volume, not missing terms. (c) NEW **US test campaign 626760351373** ($4/day, CONSIDERATION, ACTIVE with user approval), ad group 2680093090145 (same audience/interests/auto-targeting, LOCATION US, all 59 keywords incl. negatives), 5 winning ads ACTIVE (pending review): US K1 687324649852, US K2 ...853, US K3 ...854, US P3b ...855, US P2c ...856; utm_campaign=ads_kit_us, utm_content us_k1/us_k2/us_k3/us_p3/us_p2. Total stays $12/day. Daily-check trigger updated so it does not pause the US test. K5-K7 still PAUSED awaiting explicit turn-on.
- 2026-11-19 ~05:35 UTC: user explicitly said **"Turn on"** for K5-K7. Set K5 687324649245, K6 687324649246, K7 687324649247 to **ACTIVE** (Pinterest review PENDING; they deliver once approved). They are ALLOWED to be active. Main Kit campaign now has 8 active ads (K1, K2, K3, P3b, P2c, K5, K6, K7) at $8/day; US test 5 active at $4/day; BUYERS still PAUSED.
- 2026-11-20 ~04:15 UTC: user chose **option A** for the US test (it had 1 view and $0 spent in about a day). Backup of prior states: Drive 1YzyrdwPV7gPstgoA5qd8kAp5AGPSkaGF. Applied: US test campaign 626760351373 **PAUSED** (must stay paused); main ad group 2680093069045 LOCATION now **US, CA, GB, AU**; main campaign 626760338310 renamed "...$8/day | Women 25-44 | US CA UK AU". Total budget is now **$8/day**, with no new spending. Stats at the time of the change: $22.03 spent, 4,825 views, 25 clicks (0.52%), $0.88 per click, 0 sales; Canada best (1.16%). Daily-check trigger updated to match.
- 2026-11-20 ~17:45 UTC: user chose **option B**: main Kit campaign 626760338310 daily cap $8 -> **$15** (renamed "...$15/day..."), to reach ~100 clicks by ~Nov 24 at about the same total cost (~$84). Backup: Drive 11v51lh4GAWD-sOJAiLRXaV7eKqXUmBRA. Stop rule unchanged ($90 with 0 sales). Watch: recommend back to $8 if a full day's CPC > $1.20; recommend pausing K6 at ~400 views with no new clicks. Stats at change: $24.36, 29 clicks, 0 sales. Kit page audit (read-only) found page/covers/title/description good; missing social proof. Daily-check trigger updated.
- 2026-11-21 ~05:20 UTC (learnings from the $15 test, Nov 18-21: $40.99, 8,120 views, 49 clicks, CPC $0.84, 0 sales):
  - Raising $8 -> $15 did NOT raise cost per click (Nov 20 at $15: 19 clicks, CPC $0.79). Pinterest found more clicks at the same price.
  - Winners by clicks: K3 (13), K2 (12), K1 (11); K5 has the best click rate (1.4% on 214 views). Weak: K6 (847 views, 0.47%, only 0.17% on Nov 20) and P2c (760 views, 0.26%) - both past the ~400-view watch line.
  - Two keywords drive keyword clicks: "destination wedding welcome bag" (15) and "wedding schedule" (7). SEARCH placement is weak (0.26%) vs related pins (0.89%) and home feed (0.93%).
  - Countries Nov 20-21: Canada 17 clicks (0.9%), Australia 7 (1.4%), UK 2 on 850 views (0.24%), US 1.
  - Pinterest demand (BlogToPin free tool): Wedding Signs ~88k vs no itinerary/guest-guide interest -> Signs have far more demand than the Kit we advertise. Consider an ads test on Signs after Nov 24.
  - BlogToPin added as a tool (free keyword research only); refill trigger now runs it before every batch. No credits spent.
- 2026-11-21 user replied **"Pause"**: PAUSED weak ads **K6 687324649246** and **P2c 687324511461** (main Kit campaign). Backup of prior states: Drive 1bGx7mNU6zB1t-yw62GB7UqjBS54w4Zum. Verified PAUSED. Active ads now: K1, K2, K3, P3b, K5, K7. Campaign 626760338310 still ACTIVE at $15/day (unchanged). Daily-check trigger updated.
- 2026-11-21 ~17:30 UTC user replied **"Remove UK"**: main ad group 2680093069045 LOCATION US, CA, GB, AU -> **US, CA, AU** (all other targeting unchanged, verified); campaign 626760338310 renamed "...| US CA AU". Budget unchanged ($15/day). Backup: Drive 1x6QnJBlKlkyHuZxpBPEkCziR10Jl0AGK. Reason (Nov 18-21): UK 2,729 views, 6 clicks (0.22%), $7.19 vs AU 0.90%, CA 0.79%, US 0.50%. Totals at change: $44.31, 55 clicks, 0 sales.
- 2026-11-22 ~04:40 UTC full review (Kit campaign Nov 18-22): $56.83, 11,619 views, 73 clicks (0.63%), $0.78/click, 0 Pinterest checkouts, 0 Gumroad sales. GA: 54 sessions on the Kit page, only 6 engaged (11%), avg ~30s; desktop 16 sessions 0 engaged. Per ad (GA avg time): K3 29s, K2 11s, K1 1.5s, K5 1.9s, K7 0.6s -> K1/K5/K7 clicks leave instantly. No add_to_cart from Kit ads since Nov 18; the only carts came from sp1 (old Signs ad link) and p3_kit_wheredoigo on Nov 17-19, and the GA "purchases" then do not exist in Gumroad (tests or $0). Top keyword "destination wedding welcome bag" (27 clicks) likely means people browsing physical welcome-bag ideas = intent mismatch with a digital guide. Search placement weak (0.32%). Age 25-34 0.71% vs 35-44 0.47%. Pinterest TOTAL_PAGE_VISIT reads 0 on Nov 21-22 while GA still records sessions (tag lag or tag issue; recheck). Lesson: the Kit ads buy cheap clicks but low-intent visitors; next test should be Signs (higher demand).
- 2026-11-22 ~04:50 UTC user said **"pause K1 K5 K7"**: PAUSED K1 687324506404, K5 687324649245, K7 687324649247 (visitors left in ~1-2s). Backup: Drive 1kWyOSUqurX6G3cPA-R397D4qou2nwHci. Verified. Active ads now: **K2, K3, P3b**. Campaign 626760338310 still ACTIVE at $15/day; locations US, CA, AU.
- 2026-11-22 ~05:05 UTC user said "Fix this" to the ranked list. Applied to the Kit ad group 2680093069045 (backup Drive 1YofTLVNp93tJRdW4MYzAh7Ug6yAQgT3A): archived 6 physical-gift keywords (wedding welcome bag, wedding welcome bag ideas, destination wedding welcome bag(s), wedding hotel welcome bag, out of town guest bags; kept welcome bag itinerary / note / wedding welcome bag itinerary); AGE_BUCKET 25-34 only; placement_group BROWSE (search off). Verified. Built NEW Signs test **PAUSED** (owner must explicitly turn it on): campaign 626760374427 "Signs $12 | Traffic | $15/day | Women 25-34 | US CA AU", ad group 2680093125034 (same audience, BROWSE, 15 signs keywords), ads SG1 687324894248 (Signs welcome sign, editorial page), SG2 687324894249 (Blush welcome sign), SG3 687324894250 (Blush seating chart), SG4 687324894251 (Black & Ivory) from new Eonati8 pins 1099511696567268762/63/64/66; utm_campaign=ads_signs_traffic, utm_content sg1-sg4. Preview: marketing/ads_kit/signs_traffic_ads_preview.jpg. Evidence: GA ads_signs12 visitors 12 sessions, 50% engaged, ~149s vs Kit ads 64 sessions, 6% engaged, ~9s; but older Signs ads had low click rates (0.12-0.25%). Plan on turn-on: pause the Kit campaign so total stays $15/day.

## STANDING ORDER (owner, 2026-11-22): problem board in every report
"Always remind me about all this, always check to see problems and fix based on data, do not skip any of them without pointing them out, so we can hit our first sale. Focus, lock in, always check data, history winning."
- Every report (manual or scheduled) must: re-check the data, read and update marketing/PROBLEMS.md, list EVERY open problem with its data and fix (none skipped), lead with the step closest to the first sale, and use what worked before (winning history) to choose fixes.
- Fixes on ads, budgets, keywords, prices, codes or publishing still need the owner's explicit yes; everything else (checks, drafts, tracking fixes, logs) Claude does without being asked.
- 2026-11-22 ~13:30 UTC owner said **"Pause all ads"** (limited budget; moving to a higher-priced ~$34 Complete Wedding Suite). PAUSED Kit campaign 626760338310 (the only ACTIVE one). Verified ALL 4 non-archived campaigns PAUSED: 626760313243 Signs BUYERS, 626760338310 Kit, 626760351373 Kit US test, 626760374427 Signs Traffic (never turned on). Backup: Drive 1YzOyR_VVf2rcCxxgFihgnar3OOgbSHRv. Final Kit test (Nov 18-22): $59.12, 12,090 views, 77 clicks (0.64%), ~$0.77/click, 0 checkouts, 0 sales. Nothing may run until the owner explicitly turns something on.


## STANDING DECISION 2026-11-22: ads only for the high-ticket suite
Owner (verbatim): "we are only launching for the high-ticket product. That's what we are running ads on. Don't forget this, but you learn from their past ads: how it's working, data, information, and everything that we are doing. And always assist me to fix it."
- Paid ads ONLY for the $34 Complete Wedding Suite (Gumroad wcgxzj). $12 Signs, $14.99 Kit, $22.99 Collection: organic pins only, no ads.
- This is NOT permission to turn anything on: build PAUSED, show creatives, wait for an explicit "turn on".
- Signs test campaign 626760374427 stays paused (not to be used).

### Past-ad lessons to apply to every suite ad (data Nov 2026)
1. Kit ads: $59.12, 12,090 views, 77 clicks (~$0.77/click), 0 checkouts, 0 sales. GA: 11% engaged, ~9s on page. => Clicks were cheap but visitors left; the ad promise must match the page above the fold.
2. Creative: K3 (real product filled, clear) held visitors ~29s; K1/K5/K7 ~1-2s. Signs-ad visitors 50% engaged, ~149s. => Show the REAL product large and readable; no vague lifestyle-only images.
3. Audience: women 25-34 clicked best; Canada and Australia beat US/UK on engagement; UK removed. Search placement and the "welcome bag" keyword wasted spend => browse placement, tight keywords.
4. Conversion-objective campaign with 0 past sales could not optimise => start with a traffic/consideration test at a small budget, judge on GA engaged time + add-to-cart, not views.
5. Economics: $34 nets ~$30 => break-even at ~$0.77/click needs 1 sale per ~39 clicks (~2.6%). Stop rule: 0 add-to-cart after ~60 clicks => pause and fix page/creative.
6. Organic lesson: near-duplicate pins get filtered => ad creatives must be clearly different from each other.

- 2026-11-22 ~20:35 UTC: built suite ads PAUSED: campaign 626760377248 "Suite $34 | Traffic test | Women 25-34 | US CA AU | PAUSED" (account requires CBO: is_campaign_budget_optimization True, daily_spend_cap 10,000,000 micro), ad group 2680093128686 (copy of Kit targeting, auto_targeting False, browse), 12 PHRASE keywords, ads SU1-SU4 687324918808-11 from pins 1099511696567327252/53/56/60 (links utm_medium=paid utm_campaign=suite34 utm_content=su1-4). NOT turned on: waiting for the owner's explicit "turn on".

- 2026-11-23 owner said "add canva keywords": added PHRASE keywords 'canva wedding invitation', 'wedding invitation template canva', 'editable wedding invitation' to paused suite ad group 2680093128686 (20 active keywords). Campaign 626760377248 still PAUSED.

- 2026-11-23 owner said "fix targeting": suite campaign 626760377248 (CONSIDERATION, CBO $20/day, PAUSED) now has 2 PAUSED ad groups: BROWSE 2680093128686 (11 interests: Wedding Invitation Suite, Wedding Invitations, Invitation Template, Printable Wedding Invitations, Wedding Invitation Cards, Save the Date Invitations, Wedding Stationery, Wedding Seating Chart, Wedding Menu, Engagement Photos, Wedding Planning; old Kit interests removed) with ads SU11-SU16; SEARCH 2680093142504 (19 PHRASE buyer keywords, no interests) with the same 6 pins as ads 687325020282-87. Removed keyword 'wedding stationery inspiration'. Women 25-34, US/CA/AU, English. To turn on: set campaign + both ad groups + all 12 ads ACTIVE.

- 2026-11-23 owner asked to re-target for the SUITE buyer (old 25-34 data came from the Kit). Research: Gen Z = 51% of engaged couples and 83% of Gen Z couples use Pinterest (Zola 2026); median first-marriage age women 28.4 (Census 2025); average couple age 32, engagement 15 months (The Knot 2025); Pinterest ~22.8% male. Both suite ad groups now: ages 18-24/25-34/35-44, gender female+unknown, US/CA/AU/GB (GB added: A4 files included). Still PAUSED. Watch age/country split after launch (targeting_analytics AGE_BUCKET, COUNTRY) and cut losers.

- 2026-11-24 owner said "fix anything that needs fixing so this converts" after color research (Curalate 2013: red/orange/brown pins ~2x repins vs blue, multi-color 3.25x, very dark/light worse, faces -23%; PLoS 2015: reds/pinks/purples shared most, blue least; Zola 2026: sage #1; women prefer pinkish/purple shades). Built 3 WARM ads (ivory/blush panels, burgundy headline + button): SU17 invitation, SU18 signs, SU19 just engaged; added to BOTH groups (6 ads, 687325070810-15), PAUSED, in review. All 12 navy ads APPROVED 2026-11-24. A/B: after ~100 clicks keep the winning palette. Warm main cover added to the suite as cover 7 (owner can drag to 1st if warm ads win).

### 2026-11-24 Retargeting audience built (owner: "build retargeting audience")
- Created VISITOR audience 2542623659761 "Suite $34 page visitors 180d (retargeting)": tag 2613086207584, pagevisit, url contains wcgxzj, 180 days, prefill on. Status INITIALIZING, size 0 at creation. No ad group uses it. $0.
- Existing store-wide audience 2542623646065 "Store visitors (Pinterest Tag) 30d": size 49, TOO_SMALL.
- Next: when size >= 100 (expected ~1 week after suite ads start), build a retargeting ad group PAUSED (~$5/day) and ask owner "turn on retargeting". Never turn on without those words.

### 2026-11-24 Buyer-intent targeting applied (owner: "apply buyer targeting")
- SEARCH group 2680093142504: archived 12 idea keywords (wedding invitations, wedding stationery, wedding signs, wedding seating chart, wedding welcome sign, navy and gold wedding, watercolor wedding invitations, elegant wedding invitations, unique wedding invitations, wedding invitation cards elegant, wedding invitations black, wedding save the date).
- Active PHRASE keywords (13): wedding invitation suite, wedding invitation template(s), wedding invitation suite template, editable wedding invitation, canva wedding invitation, wedding invitation template canva, diy wedding invitations, printable wedding invitations, wedding invitation bundle, digital wedding invitation, budget wedding invitations, cheap wedding invitations.
- PHRASE_NEGATIVE: free, svg, cricut, birthday, baby shower, dress, cake. (API enum is PHRASE_NEGATIVE, not NEGATIVE_PHRASE.)
- PLAN: launch SEARCH ONLY. When owner says "turn on suite ads": set campaign 626760377248 + SEARCH group 2680093142504 + its 9 ads ACTIVE. BROWSE group 2680093128686 STAYS PAUSED (idea-browsers) unless owner asks.
- All campaigns, both groups, all ads verified PAUSED after the change.

### 2026-11-24 Buyer-intent ad creatives (owner: "Even the image that you created target buyers?")
- Audit: old 9 designs had buyer cues (Editable template, Instant download, $34 CTA) but headlines did not match buyer searches (no DIY/Printable/Canva/Bundle; "Navy & Gold", "Signs that match", "Just engaged?" are inspiration hooks), 0 mention Canva, 6 of 9 navy.
- Built 5 warm buyer ads (marketing/suite/lux/v6 b1-b5), headline = buyer keyword: DIY WEDDING INVITATIONS / PRINTABLE WEDDING INVITATION SUITE / WEDDING INVITATION TEMPLATE BUNDLE / CANVA WEDDING INVITATION TEMPLATE / YOUR WHOLE WEDDING SUITE FOR $34 (The Knot $530 anchor). Footer: EDITABLE · PRINTABLE · CANVA & GOOGLE SLIDES + SHOP THE SUITE · $34.
- Pins (board 1099511765217892863, utm_campaign=suite34): su20 1099511696567476438, su21 ...443, su22 ...448, su23 ...451, su24 ...455. Ads SU20-SU24 created PAUSED in SEARCH group 2680093142504, review PENDING.
- Recommended launch set: SEARCH group with SU20-SU24 (buyer) + SU17/SU11 kept as control; owner decides.

### 2026-11-24 Premium editorial ads SU25-SU29 (owner: "Do these images look premium?")
- Honest critique of SU20-24: shouting all-caps headline bars, photo only ~2/3 of pin, footer microtext unreadable in feed, same flat-lay photo in 3 of 7 launch ads, 2 composited-looking photos.
- Built v7 (marketing/suite/lux/v7 p1-p5): photo fills top 77%, ivory panel with gold label, Playfair Bold mixed-case headline, gold hairline, one readable line with $34. Same buyer headlines.
- Pins su25 1099511696567478443, su26 ...445, su27 ...447, su28 ...452, su29 ...455; ads SU25-SU29 PAUSED in SEARCH group, review PENDING.
- Recommended launch set: SU25-SU29 (premium) + SU20 + SU24 (bold) + SU17 (control) = 8 creatives (guides: 4-8 per ad group).

### 2026-11-24 Headline moved to top (owner: "It should be on top so it catches the buyer's eyes. Hook.")
- OWNER RULE: ad/pin headline (the hook) goes at the TOP of the image, never at the bottom.
- Built v8 (marketing/suite/lux/v8 p1-p5): ivory top panel (gold label, Playfair Bold headline, hairline, one line with $34), photo below.
- Pins su30 1099511696567478522, su31 ...525, su32 ...526, su33 ...530, su34 ...533; ads SU30-SU34 PAUSED in SEARCH group (review PENDING). SU25-SU29 (headline at bottom, never ran) ARCHIVED.
- Launch set: SU30-SU34 + SU20 + SU24 + SU17.

### 2026-11-24 Final ads v9: price badge + CTA (owner asked for CTA + price tag; decided no new AI photos yet)
- v9 (marketing/suite/lux/v9 p1-p5) = v8 top-hook layout + round burgundy "$34 FULL SUITE" badge (gold ring) + "SHOP THE SUITE →" pill button on the photo.
- Pins su35 1099511696567478687, su36 ...689, su37 ...690, su38 ...692, su39 ...695; ads SU35-SU39 PAUSED in SEARCH group (review PENDING). SU30-SU34 ARCHIVED (never ran).
- Launch set: SU35-SU39 + SU20 + SU24 + SU17. New AI photos: only after ~100 clicks show the winning hook.

### 2026-11-25 YouTube research (vidIQ search + transcripts; 20 vidIQ credits)
- Simple Pin Media (g1L8RZATbb4): Pinterest buyers are in discovery mode; $7-27 digital products convert best as impulse buys; higher prices need trust (lead magnet + email, or retargeting); show the actual product in the pin; specific problem; seamless delivery; link straight to the product page; several pin designs; keyword titles.
- Side Hustle Mastery (o8c_t9byuf0, Gumroad example): Consideration objective for beginners; let ads run 3-5 days before judging; good Pinterest CTR = 0.5-1%+; 1000x1500, bold readable text, warm soft colors; test 2-3 variations, kill losers, scale winners.
- Luc Bermond (CMiMz6ZddFE, e-com agency): separate keyword vs interest campaigns; profile branding (boards) matters before ads; 2:3; test angles.
- Our setup already matches most points. Gaps: $34 is above the $7-27 impulse range (trust: demo, refund, retargeting; consider price test only if 0 add-to-cart after ~60 clicks); profile bio does not mention invitation templates (owner must edit; API cannot); judge CTR against 0.5-1%.
- Caveat: these are self-reported creator/agency results, not verified data.

### 2026-11-25 Buyer targeting rebuilt from data (owner: "fix the ads ... targeting of buyers ... keyword and SEO"); everything stays PAUSED
- Data: Pinterest keyword tool (US/month): wedding welcome sign 4M-5M, cheap wedding ideas 3M-4M, wedding table numbers 2M-3M, diy wedding invitations 1M-2M, seating chart wedding 500K-1M, wedding invitation template(s)/set/suite + printable wedding invitations 100K-500K, wedding invitation bundle 10K-100K; canva/editable/budget/cheap invitation phrases = no Pinterest data (Google words: "canva wedding invitation template" ~4,400/mo Google). AnyAPI Google autocomplete buyer endings: templates canva, set templates, sets with rsvp, suite canva, welcome sign template canva, templates etsy. AnyAPI Pinterest search: buyer searches show Zola + template shops, titles "Editable ... Wedding Invitation Template | Instant Download | Printable".
- SEARCH group 2680093142504: +13 PHRASE (wedding invitation set/sets/set template, printable wedding invitation templates, wedding invitation templates canva, wedding invitation suite canva, wedding menu template, wedding invitations with rsvp, wedding invitation kit, wedding stationery set/bundle, save the date template, wedding rsvp cards) = 25 active (Pinterest recommends 25+); archived 'digital wedding invitation' (e-vite/video seekers); +7 PHRASE_NEGATIVE (ideas, inspo, inspiration, wording, examples, video, mockup).
- New v10 Canva buyer ads (repo marketing/suite/lux/v10 a1-a4, hook on top, $34 badge, SHOP THE SUITE): pins su40 1099511696567546782 (Wedding Invitation Set with RSVP), su41 ...784 (Printable Wedding Invitation Templates), su42 ...786 (Wedding Invitation Templates for Canva), su43 ...787 (Welcome Sign + Seating Chart). Ads SU40-SU42 PAUSED in SEARCH (review PENDING). SU38 ARCHIVED (copy said "import the included files into Canva").
- NEW ad group 2680093172005 "Suite | SEARCH | sign needs" PAUSED: PHRASE wedding welcome sign, seating chart wedding, wedding seating chart, wedding table numbers, wedding signs, wedding signage; negatives acrylic, neon, mirror, wood, wooden, chalkboard, rental, free, ideas, diy, cricut, svg, wording, led, stand; ads SU43 + SU39b PAUSED. Test only when owner asks.
- Launch set (owner words "turn on suite ads"): campaign + SEARCH group + SU40, SU41, SU42, SU35, SU36, SU37, SU39, SU20, SU24, SU17. Verified all 5 campaigns, 3 suite groups, all ads PAUSED after changes. $0 spent.

### 2026-11-25 Owner chose the 6-ad launch set (owner: "6")
- When owner says "turn on suite ads": set ACTIVE only campaign 626760377248 + SEARCH group 2680093142504 + ads SU40, SU41, SU42, SU35, SU37, SU39. Everything else stays PAUSED (SU36, SU20, SU24, SU17 = backups; SIGNS group 2680093172005; BROWSE group).
- Reason: $20/day ~ 25 clicks/day; 10 ads would split too thin; guides 4-8 ads per group; SU36/SU20/SU24 repeated hooks.
- No change made to any ad today; all still PAUSED.

### 2026-11-25 CTA button set to "Shop now" (owner: ads showed "Visit site"; asked for the best purchase CTA)
- Pinterest Consideration ads default CTA = "Learn more"/"Visit site" (help.pinterest.com/en/business/article/calls-to-action-ctas). API field customizable_cta_type works on paused ads.
- Set customizable_cta_type=SHOP_NOW on SU35, SU36, SU37, SU39, SU40, SU41, SU42, SU20, SU24, SU17 (search + browse copies), SU43, SU39b. Read back: all SHOP_NOW; approvals kept (SU35/36/37/39/20/24/17/39b APPROVED; SU40-43 PENDING). All still PAUSED. Old unused ads (SU11-16, SU18-19, SU21-23) left as they were.
- Why one CTA, not dynamic multi-CTA: matches the image button "SHOP THE SUITE" and the $34 badge (one clear purchase message); "Learn more/Visit site" invite browsers; "Buy now/Get offer/On sale" would be either a bigger jump or untrue (no offer/sale). Test a second CTA only after ~1,000 impressions per ad.

### 2026-11-26 OWNER APPROVAL: "turn on suite ads" (owner's exact words, after asking for a final checkout check)
- Pre-check: product page + checkout (?wanted=true) load, $34, card + PayPal shown, not unavailable; tracked su40 link loads; Pinterest tag on page.
- Turned ON only: campaign 626760377248 ($20/day cap), SEARCH group 2680093142504, ads SU40, SU41, SU42, SU35, SU37, SU39 (all CTA Shop now). Everything else stays PAUSED (BROWSE group, SIGNS group, backups SU36/SU20/SU24/SU17, other campaigns).
- Rules from now: no budget/targeting changes for ~7 days (learning); allowed earlier: pause an ad under 0.5% CTR after ~1,000 impressions; stop rule 0 add-to-cart after ~60 clicks = recommend pause.

### 2026-11-27 OWNER APPROVAL: "apply keyword fix"
- Reason: 22h live, only 7 impressions, 0 clicks, $0 (search-only + phrase match too tight; Thanksgiving).
- Change in SEARCH group 2680093142504 only: 8 top buyer keywords PHRASE -> BROAD (archive phrase copy, add broad): wedding invitation templates, wedding invitation template, printable wedding invitations, wedding invitation set, wedding invitation sets, cheap wedding invitations, wedding invitation bundle, wedding invitation suite. Add PHRASE: printable wedding invitations with rsvp, printable wedding invitations templates, wedding invitation bundle canva, wedding invitation templates etsy. Add PHRASE_NEGATIVE: reddit, vellum, envelope, envelopes, sizes, what to include, set up.
- Unchanged: placement SEARCH only, $20/day cap, 6 ads, statuses.

- 2026-11-28 ~04:25 UTC OWNER APPROVAL "Swap it" (after Claude recommended swapping SU42): SU42 (687325218715, 0.19% CTR after 1,077 impressions) PAUSED; backup SU36 "final printable" (687325121385, APPROVED, CTA Shop now, utm_content=su36) ACTIVE. Active set now SU35, SU36, SU37, SU39, SU40, SU41. Budget, keywords and targeting unchanged ($20/day). Watch SU40 (0.15% at 687 impressions) at ~1,000 impressions.

- 2026-11-28 ~06:33 UTC OWNER APPROVAL "remove 18-24": suite SEARCH group 2680093142504 AGE_BUCKET changed from [18-24, 25-34, 35-44] to [25-34, 35-44]; all else unchanged (search placement, keywords, US/CA/AU/GB, female+unknown, $20/day). Data: 18-24 took $23.64 of $26.91 at $2.63/click vs 25-34 $0.30 and 35-44 $0.52. Note: at check time the campaign, group and ads already showed summary_status ADVERTISER_DISABLED (delivery stopped ~05:00 UTC, before this edit) — account-level, likely billing; owner to check Ads > Billing.

- 2026-11-28 ~07:30 UTC OWNER APPROVAL "build freebie audience and make freebie code": (1) Pinterest audience 2542623662786 "Free Save the Date page visitors 180d (retargeting)" (pagevisit url zjqhml, tag 2613086207584), INITIALIZING; no ads use it. (2) Gumroad code SAVETHEDATE5 = $5 off the $34 suite only (no expiry, no limit), shown ONLY in the free save-the-date receipt with link eonati.gumroad.com/l/wcgxzj/SAVETHEDATE5?utm_medium=freebie. Suite list price stays $34.
