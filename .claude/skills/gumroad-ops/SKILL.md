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
- 2026-11-12 (later): the user said "fix all of this", so I PUBLISHED the black & ivory product (/l/modern-black-ivory-wedding-signs, short permalink ipbcxk). The Pinterest tag is confirmed on its product and receipt pages. Pin queue manifest_v14 (1V13JRFAxOwRg8UkTPb694MVZhFOCFvBw) orders pending pins as signs, then Collection, then Kit.
- Checkout upsells still need the user's signed-in browser: no Claude in Chrome tools and no linked computer were available in this cloud session.
- Checkout upsells (cross_sells) CAN be read: `GET https://gumroad.com/checkout?product=<short_permalink>&quantity=1`, then html-unescape the page and parse the `"cross_sells":[...]` array (text, description, replace_selected_products, offered_product, discount). Short permalinks: lnjotg = Stationery, qwnfee = Kit, dpesmn = Collection, fwscmh = Free checklist, ipbcxk = Black & ivory.
- 2026-11-12 state of the user's upsells: Stationery to Collection has replace OFF (wrong: it charges $34.99 total and repeats the signs; the user must switch it ON). Kit to Collection has replace ON (correct). Free to Stationery has replace OFF (correct), but its text is missing the first word "Get".
- manifest_v15 (1ybYuKHtXOKzxUinNQjVw7mdFe_Ha_Bc8): 6 black & ivory pins (obw01-06; greyscale bg photos, BUR set to near-black) and 3 free checklist pins (ofr01-03, burgundy) are interleaved at the front.
- 2026-11-12 late: the user deleted LAUNCH15, TAGTEST3A5F and SIGNSBUYER4. On the user's "A" I recreated SIGNSBUYER4 (Kit, $4 off, id s11T0uqTMhL9ZubT6lcx0g==) and a test code TAGTESTMUF9 (Stationery, 100%, single use, id nzpV57MLnFL6mxllxJEC_A==). Delete the test code after the tag test.
- The user keeps putting checkout upsells on the wrong product. Read `props.checkout.add_products[i].product.cross_sells` from the data-page JSON, matched by permalink, and ask for a screenshot of the form.
- 2026-11-12 user decision: NO SALE, ever. The Signs stay $12 with no codes and no deadlines. I removed the "Holiday sale / HOLIDAY25 / Ends Nov 30" paragraph from the Stationery description, deleted the HOLIDAY25 code, and deleted the 3 promoted holiday pins (1099511696566374058/60/63; backup in Drive backups). Never add a permanent "was $12, now $9" or auto-applied discount: a fake reference price is not allowed. To lower a price, change the real price, and only when the user asks.

## Reviews (2026-11-14)
- Ratings are ON for the products: the page data has props.product.ratings with count 0.
- Buyers rate with Gumroad's stars, on the download page or in their Gumroad Library.
- I added a bold "Love how your … turned out? Please leave a quick star rating…" paragraph at the end of the download page (rich_content) for Signs, Collection, Kit and Black & Ivory. Backup: Drive 1-STsiRTtWUG2mwRra2I4_mVVXbHNf9bd.
- I added a rating line to the Signs receipt (custom_receipt_text; still includes SIGNSBUYER4).
- The best remaining lever is something only the user can set up: a Gumroad Workflow (Emails > Workflows, trigger "Purchase") that sends a review request email about 5 days after purchase. The API cannot create it.
- Never write or post fake reviews, and never offer rewards for positive reviews only.

- 2026-11-21: user approved ("A, publish") a shorter Kit (qwnfee) description: hook, 1 inline product image, 4 ✅ benefit lines, one-line contents, refund promise "If the files don't work for you, email us within 30 days for a full refund", trust line, Collection link, license note. Price unchanged ($14.99). Backup of the previous product JSON: Drive 1GNHpMCnZUXVF28EhTUphhFEotL7hqAZm. The inline image is hosted at raw.githubusercontent.com/eonati2/eonati2/84f9ec6f.../marketing/kit_desc/d1_phone_card.jpg (public repo, fixed commit): do not delete that file or make the repo private without re-hosting the image first. Owner must make Gumroad's refund setting match the 30-day promise. Judge the change by Kit sales and begin_checkout per ad click after Nov 21.
- 2026-11-21: user asked to "fix all the products ... like this page". Restyled descriptions (same layout as the Kit: hook, 1 inline real-product image, ✅ benefits, one-line contents, questions + 30-day refund line, trust line, upsell where it existed, license) on Signs (lnjotg), Complete Collection (dpesmn), Black & Ivory (ipbcxk), Blush Rose (qgxaj); Free Checklist (fwscmh) got the ✅ layout without image or refund line. Prices, names, summaries, tags, receipts unchanged. Backup of all products before the change: Drive 1mGOz26d2goorwnlcQKH535H6GQh2UjQR. Images hosted at raw.githubusercontent.com/eonati2/eonati2/5d23b7b8.../marketing/kit_desc/{d_signs,d_col,d_bi,d_blush}.jpg (keep these files; repo must stay public). Verified live: all pages 200, images present, no "edit free". Measure: sales and begin_checkout per visitor after Nov 21 vs before (before: 0 paid sales on all products).
- 2026-11-22 ~09:50 UTC owner said "fix the problems": Kit (qwnfee) summary shortened to "Send guests one phone guide with every time, venue and shuttle, plus a matching 5×7 welcome-bag card. Edit in Google Slides. Instant download." and new cover marketing/kit_desc/cover_v2.png added via add_cover (lands LAST; the tool cannot reorder; owner must drag it to first). Previous summary is in Drive backup 1GNHpMCnZUXVF28EhTUphhFEotL7hqAZm.
- 2026-11-22 owner said "Build the suite at $34". Built DRAFT product **Complete Wedding Suite** (id oSCTNM0zgXaZowo8ShFGFw==, short permalink wcgxzj, $34, NOT published; owner must confirm before publish). New pieces (matching the editorial signs: Georgia + Lato, cream, rounded border, flower sprig): invitation, save the date, details card (5x7 Google Slides 14DTalzSiwyWJA1eyY9bsqp8fQARIY0xTQ-Tz5lL_XfY) and RSVP (5x3.5, 1j7Om67GdD867OAV-ErucR3scvQvXSIrZ7au5iYku5Y4), both shared anyone-with-link reader; private samples 1fDY4JtOfM7eeFWUlMyUgK2xiJlxjPjhiTlO9ZSfWzNA / 1tur1nTYTXZuRr7z78i78OXI2VmV_pAItQbNoqcXniFM; Drive build folder 1FItbbOYPr33P5Vgn5KVR_IZ0TfhBGc21. Files: Invitation Suite zip (pptx, single PDFs, Letter/A4 print sheets with trim marks, START_HERE Quick Start), the Complete Collection V3 zip (signs + kit) and the 18x24 posters zip (sizes match originals). Receipt (API custom_receipt) has all 8 Slides /copy links; download page has 8 link buttons. Covers: marketing/suite/cover1.png then cover2.png. Tags, summary, Weddings category, details rows set. Conversion trick: upload pptx to Drive, then proxy POST /files/{id}/copy with mimeType application/vnd.google-apps.presentation (endpoint path without /drive/v3).
- 2026-11-22 owner chose "Bonus Notion planner" for the suite. Built in the owner's Notion (private draft page): "Wedding Planning Dashboard by Eonati" https://app.notion.com/p/420f0f5ff22681be83c7d35e56157f14 with 5 databases (Checklist 25 tasks by timeframe, Budget 10 categories with Estimated/Actual/Paid, Guest List with save-the-date/invitation/RSVP/meal/table/thank-you tracking, Vendors with status and payments, Wedding Weekend Timeline Fri-Sun). Notion's API cannot publish pages: the owner must Share > Publish > turn on "Allow duplicate as template", then send the public link. Only then add it to the suite (download button + description "Bonus: Notion planner"). Do not advertise the bonus before the link works.
- 2026-11-22 ~20:33 UTC owner said "fix all the products ... Publish the product": Complete Wedding Suite (wcgxzj, $34) PUBLISHED after premium redesign. Builder files (sandbox, not repo): /home/user/pr/builder.py, spec.py, pptxb.py. Watercolor art: Higgsfield flux_3_image 2k (cut out from white/black backgrounds). Line spacing in pptx must be LH/natural-font-line-height multiples or Google Slides spreads lines. Drive folder 1-9hu6aL6HfwFuyrBZhflben8KsiJQHOZ holds 12 Slides (anyone-reader), pptx, 2 zips and the links Doc 1_C_XLjFz2_B57olzXv7mY7vSFcO3RwITxFMsTHvtDrY (download-page button "Edit in Google Slides: Ivory Garden + Midnight Gold"). Files added: 2 premium zips (old 3 zips kept = Classic style). Covers: 4 new ones appended AFTER the 2 old Classic covers (owner must reorder). Description/summary/details/receipt rewritten. Images in marketing/suite/premium/ (keep; description uses raw URLs by commit SHA).
