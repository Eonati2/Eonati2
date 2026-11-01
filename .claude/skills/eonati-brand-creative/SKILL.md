---
name: eonati-brand-creative
description: Eonati wedding brand kit and recipe for building pins, ad images, thumbnails and covers for free (Python/PIL in the Composio workbench, previewed through Canva) — colors, fonts, photo, sizes, layout and click-driving hooks. Use whenever creating or reviewing any Eonati wedding image.
---

# Eonati brand & creative

## Brand kit
| Token | Value |
|---|---|
| Burgundy (bands, badges, titles) | `#5C1228` (≈ rgb 92,18,40); Kit band ≈ `#4F1223`, Collection ≈ `#650F2B` |
| Cream (panels, text on burgundy) | `#FBF7F1` |
| Gold (rules, badge outline, small caps) | `#B79A63` |
| Plum text | `#442F3C`; muted text `#746970`; sage `#7D8C79` |
| Title font | Playfair Display (bold) — or Georgia in product files |
| Body font | Lato Regular / Bold |
| Wordmark | `E O N A T I` spaced, plus "WEDDING ESSENTIALS" in small sage caps |
| Brand photo | Soft rose flat-lay (blank cards, roses, gold pen, satin ribbon) = `ppt/media/image1.png` inside the Kit's phone-guide .pptx (download the Kit zip via the Gumroad API files list) |

Fonts download freely from `github.com/google/fonts/raw/main/ofl/...` (Lora, Lato, PlayfairDisplay).

## Sizes
- Pinterest pin / ad: **1000×1500** (2:3).
- Gumroad thumbnail: square, build **1200×1200** (Gumroad serves 600×600).
- Gumroad cover: 16:9, ~1672×941 (1280×720 minimum).

## Free build recipe
1. In the Composio workbench: render real product pages from the Google Slides PDF export (`/export/pdf`, public) with PyMuPDF; load the brand photo; draw with PIL.
2. Layout that matches the store: cream rounded header panel (wordmark → gold rule → Playfair title → one-line benefit), real product pages/cards with soft shadows in the middle, burgundy price badge with gold ring, burgundy bottom band with the format line.
3. Preview: upload the PNG with Composio `CANVA_CREATE_ASSET_UPLOAD_JOB` (s3key), then Canva MCP `get-assets` shows the thumbnail. Compare side by side with the existing thumbnails before shipping. (Don't make agent-generated files public just to preview them.)
4. Deliver: save to the Drive folder (see `backup-to-drive`) and give the user upload steps; verify the live image afterwards (SSIM vs your file).
5. OCR the result at final display size (`smart_file_extract`) to confirm the text reads.

## What makes people click (pins/ads)
- The image does ~90% of the work; CTA button matters little.
- A big 5-8-word hook naming the bride's pain, readable on a phone: "Guests texting you 'where do I go?' 50 times?", "Send guests ONE link for the whole weekend", "The card every welcome bag needs".
- Show the real product filled with a sample wedding ("Saturday 4:00 PM — Ceremony, Rosewood Garden"), not placeholders.
- Small reason-to-click line: "Edit free in Google Slides • Instant download • $19.99".
- Test 4-6 different hooks; keep the cheapest per click, refresh weekly.

## Truthfulness
Only real prices and real features. No fake deadlines, fake "was" prices, or AI images that misrepresent the product. Current true format line: "Edit free in Google Slides or PowerPoint • PDFs in US Letter + A4 • Instant download".
