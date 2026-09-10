#!/usr/bin/env python3
"""
library.py — the system's creative memory.

Without this the director restarts from zero every session: same hooks
rediscovered, same failures repeated, no accumulating edge. This keeps
references, ideas, hooks, published videos and earned rules in one searchable
JSON store so the next video starts from what the last one proved.

Store: ./content-library/library.json  (override with --db)

    init                                  create the store
    add reference  --data '{...}'         a clip you reverse-engineered
    add idea       --data '{...}'         a scored concept
    add hook       --data '{...}'         a hook and how it did
    add published  --data '{...}'         what shipped, with its numbers
    add rule       --data '{...}'         a lesson earned from real results
    list  <kind> [--limit N]
    find  <kind> <query>                  substring search across all fields
    stats
    rules                                 every earned rule, newest first

Records are free-form; only `kind` and an auto `id`/`added` are enforced, so the
schema can grow without migration. Suggested fields:

  reference  platform, url, topic, hook_type, opening_frame, first_change_s,
             duration_s, cuts, pacing, captions, broll, pattern_interrupts,
             sound, payoff, ending, loops, why_it_worked, measured{...}
  idea       topic, premise, angle, emotion, scores{...}, total, verdict
  hook       text, type, concept, scored, published_as, result
  published  title, platform, url, hook, format, duration_s, posted,
             metrics{views,avg_watch_s,pct_viewed,completion,shares,saves,
             comments,follows}, drop_at_s, diagnosis
  rule       rule, evidence, confidence(low|medium|high), source_ids[]
"""
import argparse, json, os, sys, time
from datetime import datetime, timezone

KINDS = ["reference", "idea", "hook", "published", "rule"]
DEFAULT_DB = os.path.join("content-library", "library.json")


def load(db):
    if not os.path.exists(db):
        sys.exit(f"no library at {db} — run: library.py init --db {db}")
    with open(db) as f:
        return json.load(f)


def save(db, data):
    os.makedirs(os.path.dirname(os.path.abspath(db)), exist_ok=True)
    tmp = db + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, db)


def flatten(o):
    if isinstance(o, dict):
        return " ".join(f"{k} {flatten(v)}" for k, v in o.items())
    if isinstance(o, list):
        return " ".join(flatten(v) for v in o)
    return str(o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["init", "add", "list", "find", "stats", "rules"])
    ap.add_argument("kind", nargs="?", default=None)
    ap.add_argument("query", nargs="?", default=None)
    ap.add_argument("--data", default=None, help="JSON object for `add`")
    ap.add_argument("--file", default=None, help="read the JSON object from a file")
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--limit", type=int, default=20)
    A = ap.parse_args()

    if A.cmd == "init":
        if os.path.exists(A.db):
            print(f"already exists: {A.db}"); return
        save(A.db, {"created": datetime.now(timezone.utc).isoformat(),
                    "records": []})
        print(f"created {A.db}")
        return

    data = load(A.db)
    recs = data["records"]

    if A.cmd == "add":
        if A.kind not in KINDS:
            sys.exit(f"kind must be one of: {', '.join(KINDS)}")
        raw = A.data
        if A.file:
            with open(A.file) as f: raw = f.read()
        if not raw:
            sys.exit("need --data '{...}' or --file path.json")
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as e:
            sys.exit(f"bad JSON: {e}")
        if not isinstance(obj, dict):
            sys.exit("--data must be a JSON object")
        obj.update({"kind": A.kind,
                    "id": f"{A.kind}-{int(time.time()*1000)%10**9}",
                    "added": datetime.now(timezone.utc).isoformat()})
        recs.append(obj); save(A.db, data)
        print(f"added {obj['id']}  ({len(recs)} records total)")
        return

    if A.cmd == "stats":
        print(f"\n{A.db}  —  {len(recs)} records")
        for k in KINDS:
            n = sum(1 for r in recs if r.get("kind") == k)
            print(f"  {k:11} {n}")
        pub = [r for r in recs if r.get("kind") == "published"]
        if pub:
            got = [r["metrics"]["avg_watch_s"] for r in pub
                   if isinstance(r.get("metrics"), dict)
                   and isinstance(r["metrics"].get("avg_watch_s"), (int, float))]
            if got:
                print(f"\n  mean avg_watch_s across {len(got)} published: "
                      f"{sum(got)/len(got):.2f}")
                best = max(pub, key=lambda r: r.get("metrics", {}).get("avg_watch_s", -1))
                print(f"  best: {best.get('title','?')} "
                      f"({best.get('metrics',{}).get('avg_watch_s','?')}s)")
        print()
        return

    if A.cmd == "rules":
        rules = [r for r in recs if r.get("kind") == "rule"][::-1]
        if not rules: print("no rules earned yet"); return
        print(f"\n{len(rules)} earned rules\n")
        for r in rules:
            print(f"  [{r.get('confidence','?'):6}] {r.get('rule','')}")
            if r.get("evidence"): print(f"           evidence: {r['evidence']}")
        print()
        return

    if A.cmd == "list":
        sel = [r for r in recs if r.get("kind") == A.kind] if A.kind else recs
        sel = sel[::-1][:A.limit]
        if not sel: print("nothing found"); return
        for r in sel:
            label = (r.get("title") or r.get("topic") or r.get("rule")
                     or r.get("text") or r.get("premise") or "")
            print(f"  {r['id']:22} {str(label)[:70]}")
        return

    if A.cmd == "find":
        if not A.query: sys.exit("find needs a query")
        q = A.query.lower()
        sel = [r for r in recs
               if (not A.kind or r.get("kind") == A.kind) and q in flatten(r).lower()]
        if not sel: print("no matches"); return
        print(f"\n{len(sel)} matches for '{A.query}'\n")
        for r in sel[::-1][:A.limit]:
            print(f"  {r['id']:22} {r.get('kind','')}")
            for k, v in r.items():
                if k in ("id", "kind", "added"): continue
                print(f"      {k}: {str(v)[:110]}")
            print()
        return


if __name__ == "__main__":
    main()
