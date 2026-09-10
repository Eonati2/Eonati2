#!/usr/bin/env python3
"""
reference_match.py — measure a candidate against the references it must beat.

"Is it good?" is unanswerable in the abstract. "Is it better than the five clips
we know worked in this niche?" is answerable, and this answers the measurable
half of it: motion energy, hook energy, pacing, grade, loop integrity, length.

It deliberately does NOT score beauty. That is Gate C's job, and this tool's
last line hands the question back to you.

Usage:
    python3 reference_match.py CANDIDATE.mp4 [--end S] [--db PATH] [--tag niche]

Reads reference records written by library.py (each carrying a `measured` block
from analyze_video.py). Populate it first with populate_references.py or by hand.
"""
import argparse, json, os, statistics as st, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
try:
    import analyze_video as AV
except ImportError:
    sys.exit("analyze_video.py must sit next to this script")

DEFAULT_DB = os.path.join("content-library", "library.json")


def profile(path, end=None):
    """The measurable fingerprint of a clip."""
    info = AV.probe(path)
    fps = info["fps"] or 30.0
    f = AV.gray_frames(path, end)
    mot = AV.motion(f, fps)
    g = AV.grade(path, end)
    loop = AV.loop_quality(f)
    energy = [abs(r["pan"]) + abs(r["tilt"]) + abs(r["zoom"]) / 10 for r in mot]
    return {
        "duration_s": round(len(f) / fps, 2),
        "first_second_energy": round(energy[0], 2) if energy else 0.0,
        "mean_energy": round(sum(energy) / len(energy), 2) if energy else 0.0,
        "dead_seconds": sum(1 for e in energy if e < 0.15),
        "max_zoom_pct_s": round(max((abs(r["zoom"]) for r in mot), default=0), 2),
        "max_roll_deg_s": round(max((abs(r["roll"]) for r in mot), default=0), 2),
        "black_pct": g["black_pct"], "white_pct": g["white_pct"],
        "mean_pct": g["mean_pct"], "saturation": g["saturation"],
        "loops": loop["loops"], "loop_verdict": loop["verdict"],
    }


# field, label, higher_is_better (None = "match the references, don't beat them")
FIELDS = [
    ("first_second_energy", "hook energy (0s)",   True),
    ("mean_energy",         "mean motion",        None),
    ("dead_seconds",        "dead seconds",       False),
    ("duration_s",          "duration s",         None),
    ("white_pct",           "white ceiling %",    None),
    ("mean_pct",            "mean exposure %",    None),
    ("saturation",          "saturation",         None),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate")
    ap.add_argument("--end", type=float, default=None)
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--tag", default=None,
                    help="only compare against references carrying this tag")
    A = ap.parse_args()

    if not os.path.exists(A.candidate): sys.exit(f"no such file: {A.candidate}")
    if not os.path.exists(A.db):
        sys.exit(f"no library at {A.db} — run library.py init, then populate references")

    with open(A.db) as f:
        recs = json.load(f)["records"]
    refs = [r for r in recs
            if r.get("kind") == "reference" and isinstance(r.get("measured"), dict)]
    if A.tag:
        refs = [r for r in refs if A.tag in str(r.get("tags", ""))]
    if not refs:
        sys.exit("no references with a `measured` block"
                 + (f" tagged '{A.tag}'" if A.tag else ""))

    cand = profile(A.candidate, A.end)

    print(f"\ncandidate: {os.path.basename(A.candidate)}")
    print(f"compared against {len(refs)} reference(s)"
          + (f" tagged '{A.tag}'" if A.tag else "") + "\n")
    print(f"  {'metric':22} {'candidate':>10} {'ref median':>11} "
          f"{'ref range':>18}   verdict")
    print("  " + "-" * 76)

    flags = []
    for key, label, higher in FIELDS:
        vals = [r["measured"].get(key) for r in refs]
        vals = [v for v in vals if isinstance(v, (int, float))]
        if not vals or not isinstance(cand.get(key), (int, float)):
            continue
        med, lo, hi = st.median(vals), min(vals), max(vals)
        c = cand[key]
        if higher is True:
            ok = c >= med
            verdict = "ok" if ok else f"BELOW median by {med - c:.2f}"
        elif higher is False:
            ok = c <= med
            verdict = "ok" if ok else f"WORSE than median by {c - med:.2f}"
        else:
            ok = lo <= c <= hi
            verdict = "in range" if ok else ("above range" if c > hi else "below range")
        if not ok: flags.append(f"{label}: {verdict}")
        print(f"  {label:22} {c:>10.2f} {med:>11.2f} "
              f"{lo:>8.2f}–{hi:<8.2f}   {verdict}")

    ref_loops = sum(1 for r in refs if r["measured"].get("loops"))
    print(f"\n  loop: candidate {cand['loop_verdict']!r}; "
          f"{ref_loops}/{len(refs)} references loop")

    print("\n" + "=" * 78)
    if flags:
        print("BELOW REFERENCE on:")
        for f_ in flags: print(f"  - {f_}")
        print("\nFix these before Gate C. A clip that is measurably weaker than the")
        print("references it is imitating has no argument for existing.")
    else:
        print("Meets or beats the reference set on every measured dimension.")

    print("""
Now answer, in words, and be specific:

    WHY IS THIS BETTER THAN THE REFERENCES?

Not "it matches the format" — better. A sharper hook, a stronger idea, a cleaner
loop, a payoff they lack. If you cannot name the thing it does better, the honest
answer is that it is a competent copy, and a competent copy has no reason to be
watched instead of the original. Keep improving it, or change the idea.

Measurement cannot answer this. You can.""")


if __name__ == "__main__":
    main()
