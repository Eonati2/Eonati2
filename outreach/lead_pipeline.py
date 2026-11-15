"""Eonati luxury-agent lead pipeline.

Run inside the Composio remote workbench (COMPOSIO_REMOTE_WORKBENCH), which provides
run_composio_tool() and open outbound HTTP. Cells there have a 180s limit, so run in
batches of ~8 markets.

Steps: Google Maps -> agent website (+contact page) -> scored email + og:image hero
-> mails.so verification -> append new (deduped) rows to the CRM sheet.
"""
import html as H
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

import requests

SHEET_ID = "1sTEs3fzfJxWQsO4A7xc-nChoglk0ZzcPthxcF9AVqrA"
MARKETS = ["Naples Florida", "Palm Beach Florida"]  # edit per batch
QUERY = "luxury real estate agent {}"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/130 Safari/537.36"}
BAD = re.compile(r"\.(png|jpe?g|webp|svg|gif|css|js)$|sentry|wixpress|example|domain\.com|"
                 r"email\.com|yourname|godaddy|@2x", re.I)
GENERIC = {"info", "hello", "contact", "office", "team", "admin"}


def maps(market):
    r, _ = run_composio_tool("GOOGLE_MAPS_TEXT_SEARCH", {  # noqa: F821
        "textQuery": QUERY.format(market), "maxResultCount": 20,
        "fieldMask": "id,displayName,formattedAddress,websiteUri,nationalPhoneNumber,"
                     "rating,userRatingCount,businessStatus"})
    out = []
    for p in (r or {}).get("data", {}).get("places", []):
        if p.get("businessStatus") == "OPERATIONAL" and p.get("websiteUri"):
            out.append({"market": market, "name": p["displayName"]["text"],
                        "phone": p.get("nationalPhoneNumber") or "", "website": p["websiteUri"],
                        "rating": p.get("rating") or "", "reviews": p.get("userRatingCount") or ""})
    return out


def fetch(url):
    try:
        r = requests.get(url, headers=UA, timeout=12)
        return r.text if r.ok else ""
    except Exception:
        return ""


def enrich(lead):
    home = fetch(lead["website"])
    pages = [home]
    m = re.search(r'href=["\']([^"\']*(?:contact|about)[^"\']*)["\']', home, re.I)
    if m:
        pages.append(fetch(urljoin(lead["website"], m.group(1))))
    text = H.unescape(" ".join(pages))
    emails = {e.strip(".").lower() for e in
              re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text) if not BAD.search(e)}
    domain = urlparse(lead["website"]).netloc.lower().replace("www.", "")
    first = re.split(r"\||,| - ", lead["name"])[0]
    tokens = [t.lower() for t in re.findall(r"[A-Za-z]{3,}", first)][:3]

    def score(e):
        local, _, d = e.partition("@")
        return (3 if any(t in local for t in tokens) else 0) + \
               (2 if (d in domain or domain in d) else 0) + (1 if local in GENERIC else 0)

    ranked = sorted(emails, key=score, reverse=True)
    lead["email"] = ranked[0] if ranked and score(ranked[0]) >= 2 else ""
    og = (re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', home, re.I)
          or re.search(r'content=["\']([^"\']+)["\'][^>]+property=["\']og:image', home, re.I))
    lead["hero_image"] = urljoin(lead["website"], og.group(1)) if og else ""
    t = re.search(r"<title>(.*?)</title>", home, re.I | re.S)
    lead["site_title"] = H.unescape(t.group(1)).strip()[:120] if t else ""
    return lead


def verify(lead):
    if lead["email"]:
        r, _ = run_composio_tool("MAILS_SO_VALIDATE_SINGLE_EMAIL", {"email": lead["email"]})  # noqa: F821
        d = ((r or {}).get("data") or {}).get("data") or {}
        lead["verify"] = d.get("result", "unknown")
    else:
        lead["verify"] = ""
    v = lead["verify"]
    lead["priority"] = ("C - no email (call / contact form)" if not lead["email"] else
                        "A - send" if v == "deliverable" else
                        "B - send after A batch" if v == "unknown" else "X - do not email")
    return lead


def existing_keys():
    r, _ = run_composio_tool("GOOGLESHEETS_BATCH_GET", {  # noqa: F821
        "spreadsheet_id": SHEET_ID, "ranges": ["Sheet1!D2:G5000"]})
    vals = r["data"]["valueRanges"][0].get("values", [])
    return {c.strip().lower() for row in vals for c in (row[0:1] + row[3:4]) if c}


def run():
    seen = existing_keys()
    with ThreadPoolExecutor(4) as ex:
        leads = [l for batch in ex.map(maps, MARKETS) for l in batch]
    leads = [l for l in leads if l["website"].lower() not in seen]
    with ThreadPoolExecutor(20) as ex:
        leads = list(ex.map(enrich, leads))
    leads = [l for l in leads if not l["email"] or l["email"] not in seen]
    with ThreadPoolExecutor(5) as ex:
        leads = list(ex.map(verify, leads))
    rows = [[l["priority"], l["market"], l["name"], l["email"], l["verify"], l["phone"],
             l["website"], l["hero_image"], l["rating"], l["reviews"], l["site_title"],
             "New", "", "", "", "", "", "", "", ""] for l in leads]
    if rows:
        run_composio_tool("GOOGLESHEETS_SPREADSHEETS_VALUES_APPEND", {  # noqa: F821
            "spreadsheetId": SHEET_ID, "range": "Sheet1!A:T",
            "valueInputOption": "RAW", "insertDataOption": "INSERT_ROWS", "values": rows})
    print(json.dumps({"added": len(rows),
                      "A": sum(l["priority"].startswith("A") for l in leads)}))


run()
