---
name: backup-to-drive
description: Save backups and important work files to the user's Google Drive (which survives sessions), never only to the Composio workbench or local temp folders (which get wiped). Use before changing any Gumroad listing, Pinterest ad, DNS record or other live setting, and for any file the user or a later session will need.
---

# Back up to Google Drive

The Composio workbench `/mnt/files` was **wiped between sandboxes** on 2026-11-01, losing backups made earlier the same day. Local scratchpads are also temporary. Google Drive is the durable store.

## Where
- Folder: "Eonati Kit - Google Slides Templates" (`1mg1KgLcwdh8pbK2YivLahNiUcbZXm-s6`, see `eonati-accounts`).
- Put backups in a subfolder `backups/` (create it once with `GOOGLEDRIVE_CREATE_FOLDER` with that parent, then reuse its id — Drive allows duplicate names, so look it up with `GOOGLEDRIVE_FIND_FILE` first).
- Name files `YYYY-MM-DD_<system>_<what>_before-<change>.json`, e.g. `2026-11-01_gumroad_kit_before-receipt-edit.json`.

## How (inside COMPOSIO_REMOTE_WORKBENCH)
1. Read the live record fresh (product JSON, ad/ad-group JSON, DNS zone…).
2. `json.dump` to a file in the workbench, then `upload_local_file(path)` → `s3key`.
3. `GOOGLEDRIVE_UPLOAD_FILE` with `{name, mimetype, s3key}` and `folder_to_upload_to` = backups folder id.
4. Confirm: `GOOGLEDRIVE_GET_FILE_METADATA` (name, size > 0, parent) — a backup you didn't re-open doesn't count.
5. Also state the key baseline values (price, status, budget) in the conversation.

## Rules
- Backups stay **private** (no sharing permissions). Never commit backups, buyer links or customer data to this repo — it is public.
- Restoring: read the backup from Drive (`GOOGLEDRIVE_DOWNLOAD_FILE`), send only the fields that need restoring, then verify as in `verify-and-fix`.
- Deliverables for the user (images, PDFs) also go to Drive; give them the Drive link.
