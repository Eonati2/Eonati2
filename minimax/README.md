# MiniMax video generation — local integration

Everything Claude needs to call the MiniMax video API from this repo:
the API contract, a zero-dependency client, and a refresh script for the docs.

```
minimax/
├── docs/video-generation-v2.md   the API contract (endpoints, params, async flow)
├── minimax_video.py              CLI client: create -> poll -> download
├── fetch_docs.sh                 re-pull the official docs pages
└── .env.example                  the two env vars you need
```

## Setup

1. Get an API key at <https://platform.minimax.io> (Account → API Keys).
2. `cp minimax/.env.example minimax/.env` and paste the key in. `.env` is
   gitignored — the key never goes in a commit, and never into a prompt.
3. Load it and go:

```bash
set -a && . minimax/.env && set +a
python3 minimax/minimax_video.py --doctor          # verify key + reachability
python3 minimax/minimax_video.py \
  "[push in] a minimalist logo mark forming from gold particles on black" \
  -d 6 -r 1080P -o hero.mp4
```

Image-to-video from a local still (it is base64'd into the request for you):

```bash
python3 minimax/minimax_video.py "the logo slowly rotates, soft studio light" \
  -i og-image.svg.png -o spin.mp4
```

A generation takes minutes, so the script polls and prints status; if you lose
the terminal, resume with `--status <task_id>`.

## Where this can actually run

The API is asynchronous and long-running, and the endpoint has to be reachable:

| Environment | `api.minimax.io` reachable? |
| --- | --- |
| Your own machine / laptop | yes |
| A server or CI runner you control | yes |
| Claude Code **on the web** (this sandbox) | **no — blocked by the egress policy** |

In this remote sandbox, `platform.minimax.io` and `api.minimax.io` both answer
`403 CONNECT` at the egress proxy, so Claude cannot place the call from here no
matter what is stored locally. Two ways to change that:

- **Allowlist the host.** The network policy is chosen when the environment is
  created — recreate/edit the Claude Code environment with a policy that permits
  `api.minimax.io` (and `platform.minimax.io` for doc refreshes). See
  <https://code.claude.com/docs/en/claude-code-on-the-web>.
- **Run it locally.** Use Claude Code in your terminal, where the script runs on
  your own network with your own key. This is the better home for it anyway:
  the generated mp4 lands on your disk instead of an ephemeral container.

Until one of those is true, Claude's useful role here is writing the prompts,
shaping the parameters, and wiring the output into the site — not making the
HTTP call.

## Keeping the contract honest

`docs/video-generation-v2.md` is hand-maintained and carries a provenance note:
it was assembled from MiniMax's public docs via search, because the docs host is
blocked from this sandbox. Run `./minimax/fetch_docs.sh` from an unblocked
machine to pull the real pages, then reconcile the summary and the client.
