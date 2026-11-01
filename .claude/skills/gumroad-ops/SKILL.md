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

| Add a cover/gallery image | `POST /v2/products/{id}/covers` with body `{"url": <publicly fetchable image URL>}` (e.g. the `s3_url` from the workbench `upload_local_file`). It is appended at the END; verify with SSIM against your file. Record cover IDs first so you can undo. |

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
- Status as of 2026-11-01: tag on the Kit only; Stationery and Collection need the user to set the tag to "All products".
- Prices on the live page can look different to the user because of the discount link (`/l/{permalink}/LAUNCH15`), local currency, or installments — investigate before assuming a price changed.
- Never invent "was" prices or fake countdowns; only real, honestly-described discounts.
