---
name: gumroad-ops
description: How to read and change the Eonati Gumroad store through Composio (product text, receipts, download page, tags, offer codes, product files, tracking check) — including what the API can't do. Use for any Gumroad listing, receipt, delivery, discount or tracking task.
---

# Gumroad operations

All calls go through `proxy_execute(method, url, 'gumroad', ...)` in `COMPOSIO_REMOTE_WORKBENCH`. Product IDs are in `eonati-accounts`.

## Before any change
1. Read the product fresh (`GET https://api.gumroad.com/v2/products/{id}`) and save a backup with `backup-to-drive`.
2. Record baseline: `price`, `currency`, `formatted_price`, `published`, `customizable_price`, `name`, `custom_permalink`.
3. Send only the fields you are changing. **Never send `price` unless the user asked for a new price.**
4. After the PUT, read back and compare every field you sent AND the baseline fields. Then load the live page.

## What works via the API
| Task | How |
|---|---|
| Name, description (HTML), `custom_summary`, `custom_receipt`, `tags`, `taxonomy_id` | `PUT /v2/products/{id}` |
| Download page (content) | `PUT /v2/products/{id}` with `rich_content` as a **JSON array** (not a string — a string is rejected with "must be an array of content page objects"). Keep the existing `fileEmbed` node first; add `paragraph` nodes after it. Text links: `{"type":"text","text":"Label","marks":[{"type":"link","attrs":{"href":URL,"target":"_blank"}}]}` |
| Product files | `product.files[]` contains signed download `url`s — you CAN download the files the buyer gets |
| Offer codes | `GET/POST/PUT/DELETE /v2/products/{id}/offer_codes[/{code_id}]`; `valid_at` must be before `expires_at`; `expires_at: ''` clears expiry |
| Sales | `GET /v2/sales` |

| Add a cover/gallery image | `POST /v2/products/{id}/covers` with body `{"url": <publicly fetchable image URL>}` (e.g. the `s3_url` from the workbench `upload_local_file`). It is appended at the END; verify with SSIM against your file. Record cover IDs first so you can undo. **Max 8 covers per product** — the POST fails with "limit of 8 previews"; ask the user which one to delete (`DELETE /v2/products/{id}/covers/{cover_id}`) before adding. Covers keep their native aspect ratio, so a tall 4:5 (1080×1350) cover shows much larger on phones than a 16:9 one. |

## Gumroad MCP (connected 2026-11-04)
- `update_product` handles summary, description, `additional_details` rows, category, tags (**max 10**, 2–20 chars) and the receipt message/button. Pass only the fields you change.
- The MCP's `custom_receipt_text` is a **different field** from the v2 API `custom_receipt`, which holds the Google Slides links. Editing one does not change the other. Never blank the API field; after any MCP edit, check that it still has its `docs.google.com` links.
- The MCP has no tool to delete files or to set the Pinterest Tag. Old draft files are still attached to each product. Buyers only see the `fileEmbed` file on the download page.
- Reorder covers: add the new cover, then DELETE the old ones and re-add them from fresh uploads. Check each with a pixel diff (done for the Collection on 2026-11-04).

## What does NOT work via the API (user does it in the dashboard)
- Reordering covers (no endpoint — `PUT .../covers` is 404). Ask the user to drag, or (only with permission) delete + re-add the others.
- Thumbnail (square store image) — user uploads in Edit → Thumbnail. Build the image, save it to Drive, give the user steps, then verify the new `thumbnail_url`.
- Store SEO/profile settings (403).
- Third-party analytics (Pinterest Tag) settings.
- Upsells.

## Rules learned the hard way
- Tags must be under 20 characters each.
- Gumroad image URLs (`public-files.gumroad.com`) are blocked from the local machine — download them inside the Composio workbench.
- Check the Pinterest Tag with the **short** permalink: `https://gumroad-analytics.com/{short_permalink}?location=product|receipt` and count `pintrk`. Using the custom permalink gives a 404 (that is NOT a missing tag). The product page also exposes `"has_third_party_analytics":true`.
- Status as of 2026-11-04: the tag is live on all 3 products (product and receipt pages; tag id 2613086207584 found). If one product loses it, the dashboard dropdown was probably set to a single product instead of "All products".
- Prices on the live page can look different to the user because of the discount link (`/l/{permalink}/LAUNCH15`), local currency, or installments — investigate before assuming a price changed.
- Never invent "was" prices or fake countdowns; only real, honestly-described discounts.
- Swap a buyer file (done for the Kit, 2026-11-11): build the new zip, upload it with `upload_local_file`, call the MCP `add_file` with that URL and a clean `display_name`, then PUT the ORIGINAL `rich_content` with only the old file id replaced by the new one. Rebuilding the node list yourself leaves the file at the bottom of the download page.
- Before launch, scan the PDFs inside each buyer zip for old prices (PyMuPDF `get_text`). The Kit Quick Start said "$19.99 product"; it now reads "Customer Quick Start · Version 2".
- `/copy` Google Slides links always redirect to sign-in. To check that sharing is public, load `/preview` instead.

## 2026-11-12 updates
- Signs = main product (user decision). Organic pins go to the $12 Stationery Suite; paid ads go to the Collection.
- Upsell workaround (no upsell API): offer code SIGNSBUYER4 ($4 off, Kit only, id FRX1W1YUClWJa4yuVYawLQ==), so Kit costs $10.99 and signs + Kit = $22.99, the same as the Collection. It is linked in the Stationery receipt and as a download-page button.
- Download page: `PUT rich_content` silently did nothing this time. The MCP `add_content_link` worked; it appends a button after the files.
- Black & ivory style: DRAFT product 4-R0zRFv2UAYf-BIsrWh8w== (/l/modern-black-ivory-wedding-signs), $12, 3 tall covers, Weddings category, 10 tags. NOT published; it waits for the user's OK. The renderer lives in the workbench at /mnt/files/bw/bw_core.py; the Drive folder is 1HAkAc6mjTcKDt6yTTaBiUWKJr1Kh8mlB.
- Lesson: when a workbench cell fails part-way, variables from earlier cells stay set. I once saved the Stationery receipt onto the new draft this way. Always build receipt text in the same cell as the PUT, then read it back and check that the links belong to that product.
- The Pinterest tag shows last_fired_time_ms via `GET /ad_accounts/{id}/conversion_tags`. A $0 test checkout can't run from the cloud (gumroad.com and ct.pinterest.com are blocked here), so the user must do it.
