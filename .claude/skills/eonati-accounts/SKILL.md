---
name: eonati-accounts
description: Map of every Eonati account, connection and ID (Pinterest Eonati8 vs Eonati2, Pinterest Ads account, campaign/ad groups, Gumroad products, Google Drive folder, Canva, Hostinger domain). Use at the start of ANY Eonati task (wedding products, Gumroad, Pinterest, ads, Canva, Drive) so you pick the right account and IDs without rediscovering them.
---

# Eonati accounts map

Read this first, then verify any value you are about to change by reading it fresh from the API (see `verify-and-fix`). IDs here are references, not proof of current state.

## Two businesses — never mix them up

| | Wedding templates (the one being sold) | Logo directory (separate) |
|---|---|---|
| Pinterest username | **Eonati8** | Eonati2 |
| Composio Pinterest account id | **`pinterest_erie-audit`** (NOT the default) | `pinterest_dike-toise` (default) |
| Website | eonati.com → forwards to eonati.gumroad.com | eonati2.github.io/Eonati2 (this repo) |

- The default Composio `pinterest` account is the **logo** account. For wedding pins always pass `account: "pinterest_erie-audit"` (e.g. `PINTEREST_GET_PIN`). Proxy calls via `proxy_execute(..., 'pinterest')` hit the logo account — don't use them for wedding pins.
- Ad-only (promoted) pins return 404 from the logo account; read them with `PINTEREST_GET_PIN` on `pinterest_erie-audit`.

## Pinterest Ads (toolkit `pinterest_ads`)

- Ad account **549770755316** ("Eonati", USD, owner Eonati8). A second empty account 549770755317 exists — ignore it.
- Traffic campaign **626760192422** "Wedding Templates | Traffic | $20/day | Kit test" — objective CONSIDERATION, CBO, $20/day, launched 2026-10-31.
  - Ad group A **2680092823126** "Searchers" — 14 PHRASE keywords + 12 PHRASE_NEGATIVE (dress, hair, makeup, gifts…), US, 25-44.
  - Ad group B **2680092831056** "Planners" — 6 wedding interests, US, 25-44.
  - 6 Guest Kit ads (P2 welcome-bags, P3 where-do-I-go, P4 every-guest in each group). P4 = best performer.
  - Paused non-promo ads 687322993329 (Kit), …330 (Stationery), …331 (Collection) — the user paused these; never re-enable on your own.
- Old Sales campaign 626760134071 — PAUSED by the user.
- Pinterest Tag (conversion tag) **2613086207584**.
- The `pinterest_ads` token lacks `pins:read`; use the `pinterest` toolkit with `pinterest_erie-audit` for pin text/images.

## Gumroad (toolkit `gumroad`, store eonati.gumroad.com)

| Product | ID | Short permalink | Custom permalink | Price |
|---|---|---|---|---|
| Wedding Guest Guide & Itinerary Kit | `vy5Qfs2a4lrW8g3-KsT1kA==` | qwnfee | wedding-weekend-guest-experience-kit | $19.99 |
| Editorial Stationery Suite (12 signs incl. seating chart, V3 2026-11-05) | `iI0VCAGoselKwSpiVYtqoA==` | lnjotg | wedding-weekend-editorial-stationery | $12 |
| Complete Collection (Kit + Stationery) | `dcdJi_w8pzkmR-amy-xpQQ==` | dpesmn | wedding-weekend-complete-collection | $27.99 |
| Dropshipping guide (old, unpublished) | `zI6m38V0cMPXYXsYeB0Njg==` | — | — | $15 |

- Offer code LAUNCH15 (15%, universal) id `QfgUJjT0vXSEOOmXBBHyAA==`.
- Google Slides template links (buyer deliverables) live ONLY in each product's `custom_receipt` and download page. **Never copy them into this public repo.**

## Google (toolkits `googledrive`, `googleslides`; account khleans man)

- Drive folder "Eonati Kit - Google Slides Templates": `1mg1KgLcwdh8pbK2YivLahNiUcbZXm-s6` — holds the source .pptx (private) and 6 Google Slides copies (shared "anyone with link: reader", not discoverable).
- Use this folder (or a `backups/` subfolder) for anything that must survive — see `backup-to-drive`.

## Store visits (Google Analytics, read-only)

- Gumroad's API has no page-view data — use GA4. Composio `google_analytics`, account `google_analytics_cleche-resend`, property **`properties/558431808`** ("Eonati Gumroad Store."; a near-duplicate `558436368` also exists). Timezone America/Los_Angeles; data lags ~1 day.
- Useful: `GOOGLE_ANALYTICS_RUN_REPORT` by date / deviceCategory / sessionSource+pagePath / eventName (view_item, add_to_cart, begin_checkout, purchase). GA `purchase` events can be the user's $0 test orders — Gumroad sales are the truth.
- Baseline 2026-11-02: mobile visitors bounce ~95% (1 of 22 engaged) vs desktop 6 of 18 — mobile first screen is the main leak.

## Other connections

- Canva: Composio `canva` (account `canva_bully-voting`) and the Canva MCP point at the same Canva Free account. Template links are a paid feature — don't plan on them.
- Hostinger (`hostinger`): domain eonati.com; 301 forwarding to https://eonati.gumroad.com. The domain server may time out from cloud IPs while working for the user — trust the user's own check before changing DNS (email runs on the same domain).
- BlogToPin (`custom_blogtopin`) is connected; AI pin generation spends paid credits — ask first.

## Scheduled tasks (claude-code-remote)

Daily launch watcher (15:23 UTC), Day-3 review (2026-11-03 21:00 UTC), LAUNCH15 cleanup (2026-11-07 21:00 UTC). Check `list_triggers` before creating new ones to avoid duplicates.
