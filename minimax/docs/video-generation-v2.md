# MiniMax Video Generation API v2 — local reference

Source of record: <https://platform.minimax.io/docs/api-reference/video-generation-v2-create>

> **Provenance / accuracy warning.** `platform.minimax.io` is blocked by this
> environment's network egress policy, so this file was **not** transcribed from
> the official page. It was assembled from MiniMax's public docs as surfaced in
> search results plus third-party integrator docs. Endpoint shapes, model ids and
> the async flow are corroborated; exact enums, limits and newer fields may drift.
> Run `minimax/fetch_docs.sh` from a machine that can reach `platform.minimax.io`
> to replace this file with the real page, then re-check `minimax_video.py`.

## Base URLs

| Region | Base |
| --- | --- |
| Global (default) | `https://api.minimax.io/v1` |
| Global, US-West | `https://api-uw.minimax.io/v1` |
| Mainland China | `https://api.minimaxi.chat/v1` |

Auth on every call: `Authorization: Bearer $MINIMAX_API_KEY`.
Some account/file endpoints also want the `GroupId` from the MiniMax console.

## The flow is asynchronous — three calls

```
POST /video_generation        -> task_id
GET  /query/video_generation  -> status, then file_id (poll until Success/Fail)
GET  /files/retrieve          -> download_url  (valid ~9 hours / 32400s)
```

### 1. Create — `POST /v1/video_generation`

```bash
curl --request POST \
  --url https://api.minimax.io/v1/video_generation \
  --header 'Authorization: Bearer $MINIMAX_API_KEY' \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "MiniMax-Hailuo-2.3",
    "prompt": "A mouse runs toward the camera, smiling and blinking.",
    "duration": 6,
    "resolution": "1080P",
    "prompt_optimizer": true
  }'
```

| Field | Type | Notes |
| --- | --- | --- |
| `model` | string, required | e.g. `MiniMax-Hailuo-2.3`, `MiniMax-Hailuo-2.3-Fast`, `MiniMax-Hailuo-02`. |
| `prompt` | string | Text description. `[bracket]` syntax drives camera moves on Hailuo 2.3 (`[push in]`, `[pan left]`, `[pedestal up]`, `[push out]`, …). |
| `first_frame_image` | string | Image-to-video. Public https URL **or** a `data:image/jpeg;base64,...` URI. Presence of this field is what makes the task i2v rather than t2v. |
| `duration` | int | Seconds. Default `6`. `6` or `10` on Hailuo models (10s is 768P-only). |
| `resolution` | string | `768P` or `1080P`. 1080P is 6s-only on Hailuo 2.3. |
| `prompt_optimizer` | bool | Default `true`. Set `false` for literal prompt control. |
| `fast_pretreatment` | bool | Default `false`. Cuts optimizer latency; Hailuo 2.3 / 02 only, and only when `prompt_optimizer` is true. |
| `callback_url` | string | Optional webhook; MiniMax POSTs task status JSON there instead of you polling. |

Response:

```json
{ "task_id": "176843862716480",
  "base_resp": { "status_code": 0, "status_msg": "success" } }
```

`base_resp.status_code` of `0` means success. Non-zero is a real error even
though the HTTP status is 200 — always check it.

### 2. Poll — `GET /v1/query/video_generation?task_id=<id>`

```json
{ "task_id": "176843862716480",
  "status": "Success",
  "file_id": "176844028768320",
  "video_width": 1920,
  "video_height": 1080,
  "base_resp": { "status_code": 0, "status_msg": "success" } }
```

`status` ∈ `Preparing` | `Queueing` | `Processing` | `Success` | `Fail`.
Poll every ~10s; a 6s clip typically lands in ~1–3 minutes.

### 3. Retrieve — `GET /v1/files/retrieve?file_id=<id>` (add `&GroupId=<id>` if your account requires it)

```json
{ "file": { "file_id": 176844028768320,
            "download_url": "https://.../video.mp4",
            "filename": "output.mp4" } }
```

The URL expires ~9 hours after it is issued, so download immediately.
Newer responses may carry the URL on the query step itself; `minimax_video.py`
checks for that before calling `/files/retrieve`.
