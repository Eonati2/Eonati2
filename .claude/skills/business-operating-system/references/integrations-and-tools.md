# Integrations and Tool Requirements

Rules:
- Connect only through authorized APIs, MCP servers or approved connectors the owner set up.
- Never claim access to an account you have not verified in the current conversation.
- Never ask for passwords, API keys or card numbers in chat. The owner connects accounts in their own settings.
- Read-only by default. Any write action (launch, spend, publish, send, edit price) needs the owner's explicit approval.

## How to audit tools at the start of a project

1. List the tools available in this conversation (MCP servers, connectors, skills).
2. For each need below, mark **Verified** (a read call succeeded in this conversation), **Available, not verified** (tool exists but no successful call yet), or **Missing**.
3. Do a harmless read call to verify (for example, list accounts or pull yesterday's report).
4. Report gaps and the exact setup step the owner must do.

## Requirement map

| Need | Typical options | What to check |
|---|---|---|
| Current web research | Web search tool, web fetch, browser tools, SEO tools (Semrush, Ubersuggest, Ahrefs) | Can it return current pages with dates? |
| Competitor research | Web search, browser scraping, Meta Ad Library, marketplace search, review sites | Sources must be cited |
| Pinterest Ads reporting | Pinterest Ads API (via Composio `pinterest_ads` or similar) | Ad account ID, analytics endpoint, targeting analytics |
| Pinterest organic | Pinterest API (pins, boards, analytics) | Correct account; never mix brand accounts |
| Meta Marketing API | Meta Ads connector (Composio, Windsor.ai, Hyper MCP, Higgsfield meta_ads, or Meta's own) | Ad account access, pixel/CAPI events |
| Google Ads API | Google Ads connector (Composio, Windsor.ai, Hyper MCP) | Customer ID, conversion actions |
| TikTok Ads | TikTok Ads connector (Composio, Windsor.ai, Hyper MCP) | Advertiser ID, pixel events |
| Analytics and conversion tracking | GA4 API, platform pixels, Google Tag Manager | Events firing, UTM data visible |
| CRM | HubSpot, Airtable, Notion, Google Sheets | Contact consent, fields |
| Email marketing | Klaviyo, Mailchimp, Kit, Gumroad email, Instantly (cold outreach only) | Consent, sending domain |
| E-commerce and payments | Gumroad, Shopify, Etsy, Stripe, PayPal | Products, prices, sales, payouts |
| Creative production | Canva, image/video generation tools | Real product shown; licensing |
| Files and backups | Google Drive, GitHub | Never commit private or customer files to a public repo |

## Audit snapshot for the current workspace (recorded 2026-11-20)

Status labels describe what was observed in the session that built this skill; re-verify in each new conversation because connections change.

| Need | Status | Evidence / next step |
|---|---|---|
| Pinterest Ads reporting | **Verified** | Composio `pinterest_ads`: campaigns, ads, analytics and targeting analytics read successfully on 2026-11-20 |
| Pinterest organic | **Verified** | Composio `pinterest` (Eonati8 account) used to post and read pins |
| Analytics (GA4) | **Verified** | Composio `google_analytics` reports returned sessions, ad content and events |
| E-commerce (Gumroad) | **Verified** | Composio `gumroad` products, offer codes and sales read successfully |
| Files (Google Drive) | **Verified** | Composio `googledrive` used for manifests and backups |
| Pinterest keyword research (BlogToPin) | **Verified 2026-11-20** | Composio `custom_blogtopin` (account custom_blogtopin_paper-spew). `CUSTOM_BLOGTOPIN_SEARCH_PINTEREST_INTERESTS` is FREE (no credits) and returns Pinterest Ideas interests with a rounded "people searched" snapshot (no time window; not monthly volume). Use it before every pin batch and ad keyword change. Results 2026-11-20: Wedding Signs ~88k, Wedding Welcome Signs ~18k, Wedding Welcome Bags ~15k, Wedding Timeline Template ~2k; no dedicated interest for "wedding itinerary" or "wedding guest guide". AI pin generation costs credits (0 pin credits, 20 writer credits on 2026-11-20): never spend credits without the owner's OK. BlogToPin also has 2 websites tied to the Eonati2 logo site; never touch those. |
| Web research | **Available, not verified in this audit** | Web search, browser and SEO tools (Semrush, Ubersuggest) are installed; verify per task |
| CRM | **Available, not verified** | Composio lists HubSpot, Airtable, Notion, Google Sheets as connected apps |
| Email marketing | **Partly available** | Instantly (cold outreach) connected in Composio; no Klaviyo/Mailchimp-type customer email platform verified. Gumroad's built-in email exists but was not tested |
| Meta Marketing API | **Missing (not connected in Composio)** | Options: connect Meta Ads in Composio, or use Windsor.ai / Hyper MCP Meta connector after the owner authorizes the ad account |
| Google Ads API | **Missing (not connected in Composio)** | Same options as Meta; owner must link the Google Ads account |
| TikTok Ads | **Missing (not connected in Composio)** | Same options; owner must link the TikTok Ads account |
| Payments (Stripe/PayPal) | **Not connected** | Only needed if selling outside Gumroad |

## Setup steps the owner may need

1. Open the connector settings (Composio dashboard, Claude connectors, or the chosen MCP's connect link).
2. Connect the ad account with the minimum permission needed (read-only for reporting; management only if campaign building is wanted).
3. Tell Claude which ad account is the right one.
4. Claude verifies with a read call and records the result here.
