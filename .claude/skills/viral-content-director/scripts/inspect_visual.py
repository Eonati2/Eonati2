#!/usr/bin/env python3
"""
inspect_visual.py — force a real look at a render, in the three ways that matter.

Metrics cannot see ugliness. This produces the images that Gate C is judged on,
and it exists because a render once passed every numeric check in this toolkit
while actually looking like a grey diamond lattice. Only looking caught it.

Outputs (next to the video, or --out DIR):
  <name>_cover.png     frame 0 alone, at full size — the feed thumbnail
  <name>_scroll.png    0.0-3.0s at 6fps — the scroll-stop decision window
  <name>_sheet.png     whole clip on a grid — pacing, dead zones, bad frames
  <name>_ends.png      first and last frame side by side — loop seam check

Then READ every one of them. Do not skip to the verdict.

Usage:
    python3 inspect_visual.py VIDEO [--end SECONDS] [--out DIR] [--cols 6]
"""
import argparse, os, shutil, subprocess, sys


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


def duration(path):
    err = subprocess.run([FF, "-hide_banner", "-i", path],
                         capture_output=True, text=True).stderr
    for line in err.splitlines():
        if "Duration:" in line:
            t = line.split("Duration:")[1].split(",")[0].strip()
            try:
                h, m, s = t.split(":")
                return int(h)*3600 + int(m)*60 + float(s)
            except Exception:
                return None
    return None


def run(args):
    r = subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error"] + args,
                       capture_output=True, text=True)
    return r.returncode == 0, r.stderr.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--end", type=float, default=None,
                    help="content end in seconds, excluding any platform outro card")
    ap.add_argument("--out", default=None)
    ap.add_argument("--cols", type=int, default=6)
    A = ap.parse_args()

    if not os.path.exists(A.video):
        sys.exit(f"no such file: {A.video}")
    out = A.out or os.path.dirname(os.path.abspath(A.video))
    os.makedirs(out, exist_ok=True)
    stem = os.path.join(out, os.path.splitext(os.path.basename(A.video))[0])

    dur = A.end or duration(A.video) or 10.0
    clip = ["-t", str(dur)]
    made = []

    # 1. cover frame — what the feed shows before anyone presses play
    ok, err = run(["-i", A.video, "-frames:v", "1", f"{stem}_cover.png"])
    made.append((f"{stem}_cover.png", ok, err))

    # 2. scroll window — the first three seconds, densely
    ok, err = run(clip + ["-i", A.video, "-vf",
                          "select='lt(t,3)',fps=6,scale=200:-1,tile=6x3",
                          "-frames:v", "1", f"{stem}_scroll.png"])
    made.append((f"{stem}_scroll.png", ok, err))

    # 3. whole clip — pacing and bad frames. ~30 tiles regardless of length.
    rows = max(2, min(6, int(30 / A.cols) or 5))
    fps = max(0.5, round((A.cols * rows) / max(dur, 1.0), 2))
    ok, err = run(clip + ["-i", A.video, "-vf",
                          f"fps={fps},scale=220:-1,tile={A.cols}x{rows}",
                          "-frames:v", "1", f"{stem}_sheet.png"])
    made.append((f"{stem}_sheet.png", ok, err))

    # 4. loop seam — first vs last frame, side by side
    last = max(dur - 0.05, 0)
    ok, err = run(["-i", A.video, "-ss", "0", "-frames:v", "1",
                   "-vf", "scale=360:-1", f"{stem}__a.png"])
    ok2, _ = run(["-ss", str(last), "-i", A.video, "-frames:v", "1",
                  "-vf", "scale=360:-1", f"{stem}__b.png"])
    if ok and ok2:
        ok3, err3 = run(["-i", f"{stem}__a.png", "-i", f"{stem}__b.png",
                         "-filter_complex", "[0:v][1:v]hstack=inputs=2",
                         "-frames:v", "1", f"{stem}_ends.png"])
        made.append((f"{stem}_ends.png", ok3, err3))
        for t in ("__a", "__b"):
            p = f"{stem}{t}.png"
            if os.path.exists(p): os.remove(p)

    print(f"\nvisual inspection assets for {os.path.basename(A.video)} "
          f"({dur:.2f}s analyzed)\n")
    for path, ok, err in made:
        mark = "ok " if ok and os.path.exists(path) else "FAIL"
        size = f"{os.path.getsize(path)//1024}KB" if os.path.exists(path) else "-"
        print(f"  [{mark}] {os.path.basename(path):28} {size}")
        if not ok and err: print(f"         {err.splitlines()[-1][:100]}")

    print("""
NOW READ ALL FOUR IMAGES. In this order, and answer out loud:

  _cover   Would this stop a thumb? Is the subject legible at thumbnail size?
  _scroll  Does something change between frame 1 and frame 18? Is there a
           reason to still be here at 3s?
  _sheet   Any black/broken frames? Any stretch where nothing changes? Does it
           look like the thing it was supposed to be, or like an artifact?
  _ends    Do the two halves match closely enough to cut between?

Gate C is a veto. If it looks bad, it fails — no matter what the numbers said.
""")


if __name__ == "__main__":
    main()
