#!/usr/bin/env python3
"""
analyze_video.py — measure a short-form video instead of guessing about it.

Reverse-engineers a reference clip or audits your own render. Reports:
  * hard cuts, at four detection thresholds
  * per-second camera motion: pan, tilt, zoom, roll (block-based affine flow)
  * colour grade: black/white points, mean exposure, saturation, tonal RGB
  * loop quality: does the tail actually match the head, vs a chance baseline
  * shot-change cadence and the opening-second hook check

Needs: ffmpeg on PATH, numpy. Optional: ffprobe (falls back to ffmpeg).

Usage:
    python3 analyze_video.py VIDEO [--end SECONDS] [--json]

--end matters: TikTok/IG downloads carry an outro card that is NOT part of the
content. Detect it first (it shows as the last "cut"), then re-run with --end
set to that timestamp, or every number below is polluted by the card.
"""
import argparse, json, math, os, shutil, subprocess, sys

try:
    import numpy as np
except ImportError:
    sys.exit("numpy required:  pip install numpy")

W, H, GB = 288, 512, 4          # analysis raster, and flow grid (GB x GB blocks)


def ffmpeg_bin():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("ffmpeg not found on PATH")


FF = ffmpeg_bin()


def probe(path):
    out = subprocess.run([FF, "-hide_banner", "-i", path],
                         capture_output=True, text=True).stderr
    info = {"duration": None, "fps": 30.0, "size": None}
    for line in out.splitlines():
        if "Duration:" in line:
            t = line.split("Duration:")[1].split(",")[0].strip()
            try:
                h, m, s = t.split(":")
                info["duration"] = int(h) * 3600 + int(m) * 60 + float(s)
            except Exception:
                pass
        if "Video:" in line:
            for tok in line.split(","):
                tok = tok.strip()
                if tok.endswith("fps"):
                    try: info["fps"] = float(tok[:-3])
                    except Exception: pass
                if "x" in tok and tok.split()[0].replace("x", "").isdigit():
                    info["size"] = tok.split()[0]
    return info


def cuts(path, end=None):
    """Hard cuts at four thresholds. A cut that survives every threshold is real."""
    res = {}
    for thr in (0.30, 0.18, 0.10, 0.06):
        cmd = [FF, "-hide_banner"]
        if end: cmd += ["-t", str(end)]
        cmd += ["-i", path, "-vf", f"select='gt(scene,{thr})',showinfo",
                "-an", "-f", "null", "-"]
        err = subprocess.run(cmd, capture_output=True, text=True).stderr
        res[thr] = [round(float(x.split(":")[1]), 2)
                    for x in err.split() if x.startswith("pts_time:")]
    return res


def gray_frames(path, end=None):
    cmd = [FF, "-v", "error"]
    if end: cmd += ["-t", str(end)]
    cmd += ["-i", path, "-vf", f"scale={W}:{H}", "-pix_fmt", "gray",
            "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    n = len(raw) // (W * H)
    if n < 2: sys.exit("could not decode frames")
    return np.frombuffer(raw[:n * W * H], np.uint8).reshape(n, H, W).astype(np.float32)


def _phase_corr(a, b):
    win = np.outer(np.hanning(a.shape[0]), np.hanning(a.shape[1]))
    A, B = np.fft.fft2(a * win), np.fft.fft2(b * win)
    R = A * np.conj(B); R /= (np.abs(R) + 1e-9)
    r = np.fft.ifft2(R).real
    iy, ix = np.unravel_index(np.argmax(r), r.shape)
    pk = r[iy, ix]
    def par(c, l, rr):
        den = 2 * (l - 2 * c + rr)
        return (l - rr) / den if abs(den) > 1e-9 else 0.0
    h, w = r.shape
    dy = iy + par(r[iy, ix], r[(iy - 1) % h, ix], r[(iy + 1) % h, ix])
    dx = ix + par(r[iy, ix], r[iy, (ix - 1) % w], r[iy, (ix + 1) % w])
    if dy > h / 2: dy -= h
    if dx > w / 2: dx -= w
    return dx, dy, pk


def _affine(f1, f0):
    """Least-squares fit of pan/tilt/zoom/roll over a grid of block matches."""
    bh, bw = H // GB, W // GB
    P, V = [], []
    for gy in range(GB):
        for gx in range(GB):
            a = f1[gy*bh:(gy+1)*bh, gx*bw:(gx+1)*bw]
            b = f0[gy*bh:(gy+1)*bh, gx*bw:(gx+1)*bw]
            if a.std() < 3: continue
            dx, dy, pk = _phase_corr(a, b)
            if pk < 0.02 or abs(dx) > bw/3 or abs(dy) > bh/3: continue
            P.append(((gx+.5)*bw - W/2, (gy+.5)*bh - H/2)); V.append((dx, dy))
    if len(P) < 5: return None
    A, y = [], []
    for (x, yy), (u, v) in zip(P, V):
        A += [[1, 0, x, -yy], [0, 1, yy, x]]; y += [u, v]
    return np.linalg.lstsq(np.array(A), np.array(y), rcond=None)[0]


def motion(f, fps):
    """Per-second median camera move. Pan/tilt px per frame at 288x512."""
    rows, n = [], len(f)
    for s in range(int(n / fps)):
        seg = [_affine(f[i], f[i-1])
               for i in range(int(s*fps) + 1, min(int((s+1)*fps), n))]
        seg = [r for r in seg if r is not None]
        if not seg: continue
        R = np.array(seg)
        rows.append({
            "sec": s,
            "pan":  round(float(np.median(R[:, 0])), 2),
            "tilt": round(float(np.median(R[:, 1])), 2),
            "zoom": round(float(np.median(R[:, 2])) * 100 * fps, 2),
            "roll": round(math.degrees(float(np.median(R[:, 3]))) * fps, 2),
        })
    return rows


def grade(path, end=None):
    cmd = [FF, "-v", "error"]
    if end: cmd += ["-t", str(end)]
    cmd += ["-i", path, "-vf", "scale=144:256,fps=3", "-pix_fmt", "rgb24",
            "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, capture_output=True).stdout
    m = len(raw) // (144 * 256 * 3)
    a = np.frombuffer(raw[:m*144*256*3], np.uint8).reshape(m, 256, 144, 3).astype(np.float32)
    a = a[1:] if m > 1 else a                     # frame 0 is often a cover frame
    px = a.reshape(-1, 3)
    lum = px @ np.array([.2126, .7152, .0722])
    mx, mn = px.max(1), px.min(1)
    sat = float(np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0).mean())
    def band(lo, hi):
        """Mean RGB of a luminance band, robust to flat/degenerate distributions."""
        a, b = np.percentile(lum, lo), np.percentile(lum, hi)
        sel = (lum >= a) & (lum <= b)
        if not sel.any():                       # collapsed band (very flat image)
            mid = (a + b) / 2
            sel = np.abs(lum - mid) <= max(1.0, float(lum.std()))
        return px[sel].mean(0) if sel.any() else px.mean(0)

    def tail(pct, upper):
        thr = np.percentile(lum, pct)
        sel = (lum >= thr) if upper else (lum <= thr)
        return px[sel].mean(0) if sel.any() else px.mean(0)

    return {
        "black_pct": round(float(np.percentile(lum, 1)) / 2.55, 1),
        "white_pct": round(float(np.percentile(lum, 99)) / 2.55, 1),
        "mean_pct":  round(float(lum.mean()) / 2.55, 1),
        "saturation": round(sat, 2),
        "mid_rgb":  [int(v) for v in band(40, 60)],
        "high_rgb": [int(v) for v in tail(92, True)],
        "low_rgb":  [int(v) for v in tail(8, False)],
    }


def loop_quality(f):
    """Does the tail match the head? Compared against an unrelated-pair baseline."""
    base = float(np.abs(f[len(f)//4] - f[len(f)//2]).mean())
    out = {"baseline": round(base, 2), "tests": {}}
    for k in (1, 5, 15, 30):
        if len(f) > 2*k:
            out["tests"][k] = round(float(np.abs(f[-k] - f[k-1]).mean()), 2)
    best = min(out["tests"].values()) if out["tests"] else 999
    out["loops"] = bool(best < base * 0.7)
    out["verdict"] = ("seamless" if best < base*0.5 else
                      "usable"   if best < base*0.7 else
                      "does NOT loop")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--end", type=float, default=None)
    ap.add_argument("--json", action="store_true")
    A = ap.parse_args()
    if not os.path.exists(A.video): sys.exit(f"no such file: {A.video}")

    info = probe(A.video)
    fps = info["fps"] or 30.0
    c = cuts(A.video, A.end)
    f = gray_frames(A.video, A.end)
    rep = {"file": os.path.basename(A.video), "probe": info,
           "analyzed_seconds": round(len(f)/fps, 2),
           "cuts": {str(k): v for k, v in c.items()},
           "motion": motion(f, fps), "grade": grade(A.video, A.end),
           "loop": loop_quality(f)}

    if A.json:
        print(json.dumps(rep, indent=2)); return

    print(f"\n{rep['file']}  {info['size']}  {fps:.2f}fps  "
          f"{info['duration']}s total / {rep['analyzed_seconds']}s analyzed")

    hard = c[0.30]
    print(f"\nCUTS  strict(0.30): {hard or 'none'}   loose(0.06): {len(c[0.06])} events")
    if hard:
        print("  ! a cut near the end is usually a platform outro card, not an edit.")
        print("    re-run with --end <that timestamp> to exclude it.")

    print("\nCAMERA  pan/tilt px per frame @288x512 · zoom %/s · roll deg/s")
    print("  sec |    pan |   tilt |   zoom |   roll")
    for r in rep["motion"]:
        print(f"  {r['sec']:3d} | {r['pan']:+6.2f} | {r['tilt']:+6.2f} | "
              f"{r['zoom']:+6.2f} | {r['roll']:+6.2f}")
    if rep["motion"]:
        mv = [abs(r["pan"]) + abs(r["tilt"]) + abs(r["zoom"])/10 for r in rep["motion"]]
        dead = [rep["motion"][i]["sec"] for i, v in enumerate(mv) if v < 0.15]
        print(f"  first-second energy: {mv[0]:.2f}"
              f"   {'OK' if mv[0] > 0.5 else '<-- WEAK HOOK: nothing moves at 0s'}")
        if dead: print(f"  dead seconds (no visible change): {dead}")

    g = rep["grade"]
    print(f"\nGRADE  black {g['black_pct']}%  white {g['white_pct']}%  "
          f"mean {g['mean_pct']}%  sat {g['saturation']}")
    print(f"  mid RGB {g['mid_rgb']}   high {g['high_rgb']}   low {g['low_rgb']}")

    L = rep["loop"]
    print(f"\nLOOP  {L['verdict']}  (best {min(L['tests'].values()) if L['tests'] else '-'} "
          f"vs chance baseline {L['baseline']})")
    print()


if __name__ == "__main__":
    main()
