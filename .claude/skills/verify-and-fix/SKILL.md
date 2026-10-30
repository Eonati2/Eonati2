---
name: verify-and-fix
description: Use for ANY task that checks, audits, fixes, or changes the user's accounts, stores, ads, sites or files (Gumroad, Pinterest, Pinterest Ads, GitHub, Canva, Notion, Google, etc.), and before giving the user any feedback, report, or "done" message. Makes Claude find its own way to get access, do the fix itself instead of handing work back, and check every change live before reporting.
---

# Verify and Fix

The user expects Claude to **do the fix itself**, not hand over instructions, and to **check that everything works before saying anything**. Follow these rules in every project.

## 1. Get access before saying "I can't"

Never say something can't be done until you have tried every route below, in this order:

1. **Composio connector.** Call `COMPOSIO_SEARCH_TOOLS` for the app, then `COMPOSIO_MANAGE_CONNECTIONS` with action `list` to see the connected accounts. When several accounts exist, pick the right one by checking its username and bio (for example, Eonati8 is the wedding account and Eonati2 is the logo account).
2. **No ready-made tool?** Call the app's own API through the existing connection with `proxy_execute` in `COMPOSIO_REMOTE_WORKBENCH`. Example: Gumroad has no "update product" tool, but `PUT https://api.gumroad.com/v2/products/{id}` works through the proxy.
3. **Not connected?** Start the connection with `COMPOSIO_MANAGE_CONNECTIONS` (action `add`) and give the user the sign-in link.
4. **Needs an API key?** Tell the user to add it as a secret in the cloud environment settings (session title bar → environment menu → Edit → Network secrets, or an environment variable), and name the variable you will read, e.g. `GUMROAD_ACCESS_TOKEN`. **Never ask for a key, token or password in chat.**
5. **Network blocked** (proxy 403)? Say which host was blocked and how to allow it, then do the work through a route that does reach it (e.g. the Composio workbench).

Only after all of these fail, say exactly what's blocked and the single step the user needs to take to unblock it.

## 2. Before changing anything

- Back up the current state (save a JSON copy of the record) so it can be restored.
- Test a write with one small, harmless change first, read the value back, and only then do the bulk change.
- Respect the platform's limits (for example, Gumroad tags must be under 20 characters).
- Ask first before anything that spends money (starting or raising ads), deletes things, or messages other people. Everything else in the user's request: just do it.

## 3. Verify before reporting

Every change must be checked after it is made:

- **Read it back through the API** and compare it with what you sent. A `success: true` response is not enough.
- **Check the public result**: load the live page or pin, confirm the new text is there and the links work.
- **Check the visuals**: if you made images, look at them (or measure the layout) before publishing.
- If any check fails, fix it and check again. Do not report until it passes.

## 4. How to report

- Lead with what was **done and verified**, as a short list.
- Then list what was **not** done, with the exact reason and the one step that unblocks it.
- Never say something is impossible without having tried section 1.
- Never claim something works unless you have checked it.
