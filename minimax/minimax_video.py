#!/usr/bin/env python3
"""Generate a video with the MiniMax video-generation API.

Async flow: create task -> poll status -> resolve download URL -> save mp4.
Stdlib only, no pip install. See minimax/docs/video-generation-v2.md.

  export MINIMAX_API_KEY=...            # required
  export MINIMAX_GROUP_ID=...           # only if your account needs it on /files/retrieve
  python3 minimax/minimax_video.py "a slow push in on a neon logo at night" -o out.mp4

  python3 minimax/minimax_video.py --doctor        # check key + network reachability
  python3 minimax/minimax_video.py --status <task> # resume polling an existing task
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_BASE = os.environ.get("MINIMAX_BASE_URL", "https://api.minimax.io/v1")
DEFAULT_MODEL = os.environ.get("MINIMAX_MODEL", "MiniMax-Hailuo-2.3")
TERMINAL_OK, TERMINAL_FAIL = "Success", "Fail"


class MinimaxError(RuntimeError):
    pass


def _request(method, url, api_key, payload=None, timeout=60):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    if data:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise MinimaxError(f"HTTP {e.code} from {url}: {e.read().decode()[:500]}") from e
    except urllib.error.URLError as e:
        raise MinimaxError(
            f"cannot reach {url}: {e.reason}. If this is a sandboxed/remote "
            "session, the host is probably blocked by the egress policy."
        ) from e
    # MiniMax returns HTTP 200 with an in-body error code.
    base = body.get("base_resp") or {}
    if base.get("status_code") not in (0, None):
        raise MinimaxError(f"API error {base['status_code']}: {base.get('status_msg')}")
    return body


def _as_image_field(value):
    """A public https URL passes through; a local file becomes a data URI."""
    if not value or value.startswith(("http://", "https://", "data:")):
        return value
    mime = mimetypes.guess_type(value)[0] or "image/jpeg"
    with open(value, "rb") as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()


def create_task(cfg, prompt, first_frame=None):
    payload = {
        "model": cfg.model,
        "prompt": prompt,
        "duration": cfg.duration,
        "resolution": cfg.resolution,
        "prompt_optimizer": not cfg.no_optimizer,
    }
    image = _as_image_field(first_frame)
    if image:
        payload["first_frame_image"] = image
    if cfg.callback_url:
        payload["callback_url"] = cfg.callback_url
    body = _request("POST", f"{cfg.base}/video_generation", cfg.api_key, payload)
    task_id = body.get("task_id")
    if not task_id:
        raise MinimaxError(f"no task_id in response: {body}")
    return task_id


def poll_task(cfg, task_id):
    url = f"{cfg.base}/query/video_generation?" + urllib.parse.urlencode({"task_id": task_id})
    deadline = time.time() + cfg.timeout
    last = None
    while time.time() < deadline:
        body = _request("GET", url, cfg.api_key)
        status = body.get("status", "Unknown")
        if status != last:
            print(f"[minimax] task {task_id}: {status}", file=sys.stderr)
            last = status
        if status == TERMINAL_OK:
            return body
        if status == TERMINAL_FAIL:
            raise MinimaxError(f"generation failed: {json.dumps(body)}")
        time.sleep(cfg.interval)
    raise MinimaxError(f"timed out after {cfg.timeout}s; task {task_id} may still finish")


def resolve_download_url(cfg, task_body):
    """Newer responses carry the URL inline; otherwise ask /files/retrieve."""
    inline = task_body.get("download_url") or (task_body.get("content") or {}).get("url")
    if inline:
        return inline
    file_id = task_body.get("file_id")
    if not file_id:
        raise MinimaxError(f"task succeeded but carried no file_id: {task_body}")
    params = {"file_id": file_id}
    if cfg.group_id:
        params["GroupId"] = cfg.group_id
    body = _request("GET", f"{cfg.base}/files/retrieve?" + urllib.parse.urlencode(params), cfg.api_key)
    url = (body.get("file") or {}).get("download_url")
    if not url:
        raise MinimaxError(f"no download_url in file response: {body}")
    return url


def download(url, out_path):
    with urllib.request.urlopen(url, timeout=300) as resp, open(out_path, "wb") as fh:
        while chunk := resp.read(1 << 16):
            fh.write(chunk)
    return out_path


def doctor(cfg):
    print(f"base url        : {cfg.base}")
    print(f"MINIMAX_API_KEY : {'set (%d chars)' % len(cfg.api_key) if cfg.api_key else 'MISSING'}")
    print(f"MINIMAX_GROUP_ID: {cfg.group_id or 'unset (fine unless /files/retrieve rejects it)'}")
    host = urllib.parse.urlparse(cfg.base).netloc
    try:
        _request("POST", f"{cfg.base}/video_generation", cfg.api_key or "none", {})
        print(f"reachability    : {host} reachable")
    except MinimaxError as e:
        msg = str(e)
        reachable = "cannot reach" not in msg
        print(f"reachability    : {host} {'reachable' if reachable else 'BLOCKED / unreachable'}")
        print(f"  detail: {msg[:300]}")
    return 0


def main():
    p = argparse.ArgumentParser(description="MiniMax video generation")
    p.add_argument("prompt", nargs="?", help="text prompt")
    p.add_argument("-o", "--out", default="minimax-output.mp4")
    p.add_argument("-i", "--first-frame", help="image URL or local file for image-to-video")
    p.add_argument("-m", "--model", default=DEFAULT_MODEL)
    p.add_argument("-d", "--duration", type=int, default=6)
    p.add_argument("-r", "--resolution", default="1080P", choices=["512P", "768P", "1080P"])
    p.add_argument("--no-optimizer", action="store_true", help="send the prompt verbatim")
    p.add_argument("--callback-url")
    p.add_argument("--base", default=DEFAULT_BASE)
    p.add_argument("--interval", type=int, default=10, help="poll seconds")
    p.add_argument("--timeout", type=int, default=900, help="give up after N seconds")
    p.add_argument("--status", metavar="TASK_ID", help="resume an existing task instead of creating one")
    p.add_argument("--doctor", action="store_true", help="check config and network, then exit")
    cfg = p.parse_args()
    cfg.api_key = os.environ.get("MINIMAX_API_KEY", "")
    cfg.group_id = os.environ.get("MINIMAX_GROUP_ID", "")

    if cfg.doctor:
        return doctor(cfg)
    if not cfg.api_key:
        p.error("MINIMAX_API_KEY is not set")
    if not cfg.status and not cfg.prompt:
        p.error("give a prompt, or --status TASK_ID")

    try:
        task_id = cfg.status or create_task(cfg, cfg.prompt, cfg.first_frame)
        if not cfg.status:
            print(f"[minimax] created task {task_id}", file=sys.stderr)
        body = poll_task(cfg, task_id)
        url = resolve_download_url(cfg, body)
        print(f"[minimax] downloading -> {cfg.out}", file=sys.stderr)
        download(url, cfg.out)
    except MinimaxError as e:
        print(f"[minimax] {e}", file=sys.stderr)
        return 1
    print(cfg.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
