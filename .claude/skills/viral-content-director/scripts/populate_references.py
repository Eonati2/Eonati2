#!/usr/bin/env python3
"""
populate_references.py — turn a folder of reference clips into library records.

Every clip you were given that worked is training material. This measures each
one and writes a reference record, so the next idea is compared against real
numbers from your niche instead of generic assumptions about "viral".

    python3 populate_references.py DIR_OR_FILES... [--db PATH] [--meta meta.json]
                                   [--tag niche] [--dry-run]

`--meta` is an optional JSON map keyed by filename prefix, carrying the
qualitative half a measurement cannot reach:

    {"36547926": {"title":"Sunset Bike Path","handle":"@.listl",
                  "end":10.3,"hook_type":"locked POV",
                  "why_it_worked":"anchor in lower third proves a human is there"}}

`end` matters: platform downloads carry an outro card that is not content, and
including it corrupts every measurement downstream.
"""
import argparse, glob, json, os, sys, time
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
try:
    import analyze_video as AV
    from reference_match import profile
except ImportError as e:
    sys.exit(f"needs analyze_video.py and reference_match.py alongside: {e}")

DEFAULT_DB = os.path.join("content-library", "library.json")


def collect(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            out += sorted(glob.glob(os.path.join(p, "*.mp4")))
        elif os.path.exists(p):
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--meta", default=None)
    ap.add_argument("--tag", default=None)
    ap.add_argument("--dry-run", action="store_true")
    A = ap.parse_args()

    meta = {}
    if A.meta:
        with open(A.meta) as f:
            meta = json.load(f)

    files = collect(A.paths)
    if not files: sys.exit("no .mp4 files found")

    if not os.path.exists(A.db):
        os.makedirs(os.path.dirname(os.path.abspath(A.db)), exist_ok=True)
        with open(A.db, "w") as f:
            json.dump({"created": datetime.now(timezone.utc).isoformat(),
                       "records": []}, f, indent=2)
        print(f"created {A.db}")

    with open(A.db) as f:
        data = json.load(f)
    known = {r.get("file") for r in data["records"] if r.get("kind") == "reference"}

    print(f"\nmeasuring {len(files)} clip(s)\n")
    added = 0
    for path in files:
        base = os.path.basename(path)
        if base in known:
            print(f"  skip (already in library)  {base[:52]}")
            continue
        key = base.split("-")[0].split(".")[0]
        m = meta.get(key, {})
        end = m.get("end")
        try:
            prof = profile(path, end)
        except Exception as e:
            print(f"  FAIL  {base[:52]}  {type(e).__name__}: {str(e)[:60]}")
            continue

        rec = {"kind": "reference", "file": base,
               "id": f"reference-{int(time.time()*1000)%10**9}-{added}",
               "added": datetime.now(timezone.utc).isoformat(),
               "measured": prof}
        if A.tag: rec["tags"] = A.tag
        for k, v in m.items():
            if k != "end": rec[k] = v
        if end: rec["content_end_s"] = end

        data["records"].append(rec); added += 1
        print(f"  ok    {m.get('title', base[:24]):26} "
              f"{prof['duration_s']:>6.2f}s  hook {prof['first_second_energy']:>5.2f}  "
              f"sat {prof['saturation']:.2f}  {prof['loop_verdict']}")

    if A.dry_run:
        print(f"\ndry run — {added} would be added, nothing written")
        return
    tmp = A.db + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, A.db)
    print(f"\nwrote {added} reference(s) to {A.db} "
          f"({len(data['records'])} records total)")


if __name__ == "__main__":
    main()
