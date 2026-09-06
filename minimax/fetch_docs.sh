#!/usr/bin/env bash
# Refresh the local MiniMax API docs snapshot.
# Run this from a machine that can reach platform.minimax.io (a sandboxed
# session where the host is egress-blocked will just 403).
set -euo pipefail
cd "$(dirname "$0")/docs"

pages=(
  video-generation-v2-create
  video-generation-v2-query-of-generation-status
  video-generation-t2v
  video-generation-i2v
  video-generation-query
  api-overview
)

for page in "${pages[@]}"; do
  url="https://platform.minimax.io/docs/api-reference/${page}"
  echo "fetching ${url}"
  if curl -fsSL "$url" -o "raw-${page}.html"; then
    echo "  -> docs/raw-${page}.html"
  else
    echo "  !! failed (blocked, moved, or offline) — skipping" >&2
  fi
done

cat <<'NOTE'

Saved raw HTML next to video-generation-v2.md. The .md file is the
hand-maintained summary the tooling is written against: reconcile it with the
fresh HTML (and re-check minimax_video.py) after every refresh.
NOTE
