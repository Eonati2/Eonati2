#!/usr/bin/env python3
"""clip_dedup.py — find duplicate clips in a batch, and the best loop seam.

Two jobs a generated batch always needs and that eyeballing does badly:

  DUPLICATES.  Generators re-serve the same render, and download tools fetch the
  same asset twice under different names. SHA-256 catches the byte-identical
  ones. Re-encodes survive that, so every pair is also compared perceptually on
  contrast-normalised greyscale thumbnails sampled across the clip.

  LOOP SEAM.  Which clip's tail should hand off to which clip's head. Scored the
  same way, tail-frame against head-frame, and always reported against the
  median of all unrelated pairs. That baseline is the whole point: clips from one
  batch share a grade and a subject, so they correlate highly with each other no
  matter what. A raw +0.78 can be worse than chance. Only the margin over the
  baseline means anything.

Usage:
    python3 clip_dedup.py CLIP.mp4 [CLIP.mp4 ...]
    python3 clip_dedup.py FOLDER
"""
import subprocess, sys, os, glob, hashlib, itertools
try:
    import numpy as np
except ImportError:
    sys.exit("numpy required:  pip install numpy")

W, H = 36, 64
BODY  = [0.2, 2.0, 4.0, 6.0]        # sampled across the clip for dedup
DUP   = 0.90                        # perceptual duplicate threshold

def frames(path, times):
    out = []
    for t in times:
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", path,
                            "-frames:v", "1", "-vf", f"scale={W}:{H},format=gray",
                            "-f", "rawvideo", "-"], capture_output=True)
        a = np.frombuffer(r.stdout[:W*H], np.uint8).astype(np.float32)
        if a.size < W*H:
            a = np.zeros(W*H, np.float32)
        out.append((a - a.mean()) / (a.std() + 1e-6))   # contrast-invariant
    return out

def corr(x, y):
    return float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y) + 1e-9))

def duration(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:    return float(r.stdout.strip())
    except: return 8.0

def main(paths):
    names = [os.path.basename(p) for p in paths]
    sha   = {n: hashlib.sha256(open(p, "rb").read()).hexdigest() for n, p in zip(names, paths)}
    durs  = {n: duration(p) for n, p in zip(names, paths)}
    body  = {n: np.concatenate(frames(p, [t for t in BODY if t < durs[n]] or [0.2]))
             for n, p in zip(names, paths)}
    tails = {n: frames(p, [max(0.0, durs[n] - 0.15)])[0] for n, p in zip(names, paths)}
    heads = {n: frames(p, [0.04])[0] for n, p in zip(names, paths)}

    print("=" * 72)
    print("BYTE-IDENTICAL")
    seen, exact = {}, []
    for n in names:
        if sha[n] in seen: exact.append((n, seen[sha[n]]))
        else:              seen[sha[n]] = n
    if exact:
        for dup, orig in exact: print(f"  DELETE {dup}\n         (identical to {orig})")
    else:
        print("  none")

    keep = [n for n in names if n not in {d for d, _ in exact}]
    sizes = {n: min(len(body[a]) for a in keep) for n in keep}
    m = min(len(body[n]) for n in keep)

    print("\nPERCEPTUAL  (re-encodes and near-identical re-rolls)")
    near = [(corr(body[a][:m], body[b][:m]), a, b) for a, b in itertools.combinations(keep, 2)]
    near.sort(reverse=True)
    base = float(np.median([c for c, _, _ in near])) if near else 0.0
    hits = [x for x in near if x[0] > DUP]
    if hits:
        for c, a, b in hits: print(f"  {c:+.3f}  {a}\n           {b}   <== duplicate")
    else:
        top = f"  highest pair {near[0][0]:+.3f} ({near[0][1]} / {near[0][2]})" if near else ""
        print(f"  none above {DUP:.2f}\n{top}")
    print(f"  batch baseline (median of all pairs) {base:+.3f}"
          f"  — a shared grade and subject put every pair well above zero")

    print("\nLOOP SEAM   tail of ... -> head of ...")
    seams = [(corr(tails[a], heads[b]), a, b) for a in keep for b in keep if a != b]
    sbase = float(np.median([c for c, _, _ in seams])) if seams else 0.0
    seams.sort(reverse=True)
    print(f"  chance baseline {sbase:+.3f}")
    for c, a, b in seams[:5]:
        print(f"  {c:+.3f}  (+{c - sbase:.3f} over chance)  {a} -> {b}")
    print("=" * 72)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    if len(args) == 1 and os.path.isdir(args[0]):
        args = sorted(glob.glob(os.path.join(args[0], "*.mp4")))
    if len(args) < 2: sys.exit("need at least two clips")
    main(args)
