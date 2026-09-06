# Eonati2

Static marketing site for Eonati (logo-design SEO content). Plain HTML files at
the repo root, one per landing page, plus `sitemap.xml` / `robots.txt`.

## MiniMax video generation

`minimax/` holds a local integration for the MiniMax video-generation API —
`minimax/docs/video-generation-v2.md` is the API contract and
`minimax/minimax_video.py` is a stdlib-only client (create → poll → download).

Read `minimax/README.md` before using it. Key facts:

- Auth comes from `MINIMAX_API_KEY` (and optionally `MINIMAX_GROUP_ID`) in
  `minimax/.env`, which is gitignored. Never ask for the key in chat, never
  echo it, never commit it.
- `api.minimax.io` is **blocked by the egress policy in Claude Code on the web**,
  so the call only runs from a local session or an allowlisted environment. Run
  `python3 minimax/minimax_video.py --doctor` to check before promising a render.
- The docs snapshot was reconstructed from public sources, not scraped from the
  official page; re-run `minimax/fetch_docs.sh` where the docs host is reachable
  and reconcile before trusting an exotic parameter.
