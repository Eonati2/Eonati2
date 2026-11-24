---
name: full-setup-check
description: Use whenever the owner says "check deep", "check again", "check everything", "check the full setup", "check for problems/blockages/weak spots", "is everything okay", or asks if something will convert. Runs a FULL audit of the whole Eonati wedding business (every product page, every cover, thumbnails, buyer files, links, ads, targeting, pins, tracking, scheduled tasks, research, conversation history), not just the item being discussed, then fixes what it can and reports every open problem.
---

# Full Setup Check (Eonati)

The owner's rule (2026-11-24, verbatim): "When I ask you to check deep, I need you to always check the full setup ... not just what we're talking about right now, all our full setup and our conversation and everything to understand what we are doing always."

A deep check is NEVER only the topic of the last message. Run every section below, every time. Do not skip a section without writing "skipped: <reason>" in the report.

## 0. Load context first (do not skip)
1. Read `marketing/PROBLEMS.md` (problem board, standing decisions, last check).
2. Read `.claude/skills/ads-safety/SKILL.md` (ad rules, past-ad lessons, logs) and `.claude/skills/gumroad-ops/SKILL.md`.
3. Re-read the owner's latest messages in this conversation and any decisions in them (for example "no upsell", "no Canva template links", "ads only for the $34 suite").
4. Apply the rules in `verify-and-fix` (back up first, read back every change, never turn ads on, never change prices, no fake claims, no "9 signs", no "free" in ad titles or images, "wedding" in every pin headline).

## 1. Money and data (read-only)
- Gumroad: `get_analytics` for the last 7 and 30 days, per product and `breakdown=referrer`. Views, sales and conversion for EVERY product. `list_sales` for new sales.
- Pinterest Ads (`pinterest_ads`, account 549770755316): every campaign's status, the suite ads' review status, and spend, clicks and page visits (7 days).
- Pinterest organic (Eonati8 `pinterest_erie-audit`): impressions, saves and outbound clicks, plus how many queued pins are left.
- Compare against the previous check in PROBLEMS.md. Say what went up or down.

## 2. Every product page (all published products, not only the suite)
For each product:
- price, currency, pay-what-you-want and published status, compared with the baseline (never change them);
- name, summary, tags and details row: keyword-first and true;
- description: claims true, every link and image loads, upsell or suite link present, refund line, help email;
- receipt text and the button;
- **every cover, looked at with your own eyes**: download all covers plus the thumbnail into one contact sheet and READ it. Check:
  - Does any cover contradict the product? Examples: "NO CANVA" on a product that sells Canva; an old font, format or price; "9 signs".
  - Is cover 1 the strongest hero? Is the order what buyers need: hero → what's included → styles/variety → how to edit → details/sizes → trust?
  - Are there near-duplicates wasting slots? (Gumroad allows at most 8 covers.)
  - Is the text readable on a phone? Does each cover say "wedding"?
  - Is the thumbnail current, and does it name the formats (Google Slides & Canva)?
- files (`list_files`): names, order, nothing old or duplicated, START HERE first, and the guide inside the zips current.

## 3. What the buyer receives
- Open every link in the START HERE Doc and the links Doc: Slides shared with "anyone with the link can view", and the fonts current.
- Demo link opens view-only, and the Notion planner is public.
- The zips: START_HERE.pdf lists the correct fonts, Canva steps and printing steps.

## 4. Ads and targeting (the $34 suite only; ads stay PAUSED until the owner says "turn on")
- Targeting: interests, keywords, ages, gender, countries and placements match the buyer research; no wasted or irrelevant keywords.
- Creatives: true claims, readable, real designs, "wedding" in the headline, a price or CTA strip, both color variants.
- Tracking: the Pinterest tag is firing, and page visits are recorded.
- The stop and scale rules are written down, and the launch gate passes.

## 5. Organic pins and scheduled tasks
- `list_triggers`: pin, refill, daily and weekly tasks enabled, last run SUCCEEDED, prompts current (no stale instructions).
- Queue size, variety rule, no "9 signs", and "wedding" in every headline.

## 6. Research (required on every deep check)
Do at least 2 fresh web searches tied to the weakest area found. Examples:
- what top-selling wedding template listings use for image 1 and the cover order;
- current Pinterest ad benchmarks, and what wedding buyers search this month;
- competitor prices and formats (Etsy and Gumroad research only; we do not sell on Etsy).

Cite sources in the report, and act on the findings (or say why not).

## 7. Fix, then verify
- Fix everything within the rules yourself (images, descriptions, covers, files, docs, tasks).
- Things that need the owner (deleting covers or files, dragging cover order, thumbnail upload, turning ads on, prices): give exact names and positions of what to delete or keep. Never give a vague "delete the old ones".
- Read back every change from the API or the live page before reporting.
- Update `marketing/PROBLEMS.md` (the last-check line plus one row per new problem), commit and push.

## 8. Report format (plain language)
1. Data, with week-over-week numbers.
2. What I found and fixed (verified).
3. Every open problem from PROBLEMS.md; none skipped.
4. Research used, with sources.
5. "Your to-do list (reminder)", with exact steps.
6. "🍽 Food test: on hold".
