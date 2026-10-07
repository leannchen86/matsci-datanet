#!/usr/bin/env python3
"""Append-only, hash-chained trajectory log for hand-run experiments.

One campaign is one log.jsonl. Each entry records who wrote it, when, and the
hash of the entry before it, so the order of predictions and outcomes can be
checked later. The protocol is in README.md next to this file.

Standard library only. Typical use:

    python3 trajectory/traj.py init paste-001 --text "Find what limits thermal resistance."
    python3 trajectory/traj.py add paste-001 prediction --run R01 --author ai:model-name < pred.md
    python3 trajectory/traj.py add paste-001 observation --run R01 --file raw/R01.csv --text "..."
    python3 trajectory/traj.py verify paste-001
"""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TYPES = [
    "goal", "plan", "prediction", "action", "observation",
    "interpretation", "decision", "deadend", "note",
]
# These describe one physical run, so they must name it.
RUN_TYPES = {"prediction", "action", "observation"}
HERE = Path(__file__).resolve().parent


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def entry_hash(entry):
    body = {k: v for k, v in entry.items() if k != "hash"}
    return sha256_bytes(json.dumps(body, sort_keys=True, ensure_ascii=False).encode())


def campaign_dir(root, name):
    return Path(root) / name


def load(root, name):
    log = campaign_dir(root, name) / "log.jsonl"
    if not log.exists():
        sys.exit(f"No campaign '{name}' under {root}. Run init first.")
    return [json.loads(line) for line in log.read_text().splitlines() if line.strip()]


def append(root, name, entry):
    log = campaign_dir(root, name) / "log.jsonl"
    with log.open("a") as f:
        f.write(json.dumps(entry, sort_keys=True, ensure_ascii=False) + "\n")


def read_text(args):
    if args.text is not None:
        return args.text
    if sys.stdin.isatty():
        sys.exit("Give the entry text with --text or pipe it on stdin.")
    return sys.stdin.read().strip()


def hash_files(root, name, paths):
    base = campaign_dir(root, name).resolve()
    out = []
    for p in paths:
        path = Path(p)
        if not path.is_absolute() and not path.exists():
            path = base / p
        path = path.resolve()
        if not path.is_file():
            sys.exit(f"File not found: {p}")
        if base not in path.parents:
            sys.exit(f"{p} is outside the campaign folder. Move it under {base}/raw/ first.")
        if path.name == "log.jsonl":
            sys.exit("The log cannot be attached to itself: it changes with every entry.")
        out.append({"path": str(path.relative_to(base)), "sha256": sha256_bytes(path.read_bytes())})
    return out


def parse_data(pairs):
    data = {}
    for pair in pairs or []:
        if "=" not in pair:
            sys.exit(f"--data needs key=value, got: {pair}")
        key, value = pair.split("=", 1)
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            parsed = value.strip()
        # "1e5" or "12E3" is more likely a lot or serial number than a measurement: keep it as written.
        is_number = isinstance(parsed, (int, float)) and not isinstance(parsed, bool)
        if is_number and not re.fullmatch(r"-?\d+(\.\d+)?", value.strip()):
            parsed = value.strip()
        data[key.strip()] = parsed
    return data


def settings_signature(data):
    """Settings only: keys starting with '_' describe context (session, lot), not the recipe."""
    settings = {k: v for k, v in (data or {}).items() if not k.startswith("_")}
    return json.dumps(settings, sort_keys=True) if settings else None


def new_entry(entries, kind, author, text, run=None, files=None, flags=None, data=None, at=None):
    entry = {
        "seq": len(entries) + 1,
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "type": kind,
        "author": author,
        "text": text,
        "prev": entries[-1]["hash"] if entries else None,
    }
    if run:
        entry["run"] = run
    if files:
        entry["files"] = files
    if flags:
        entry["flags"] = flags
    if data:
        entry["data"] = data
    if at:
        entry["at"] = at
    entry["hash"] = entry_hash(entry)
    return entry


def cmd_init(args):
    d = campaign_dir(args.root, args.campaign)
    if (d / "log.jsonl").exists():
        sys.exit(f"Campaign '{args.campaign}' already exists.")
    (d / "raw").mkdir(parents=True, exist_ok=True)
    entry = new_entry([], "goal", args.author, read_text(args))
    append(args.root, args.campaign, entry)
    print(f"Created {d} (entry 1, goal).")


def cmd_add(args):
    entries = load(args.root, args.campaign)
    if args.type in RUN_TYPES and not args.run:
        sys.exit(f"A {args.type} entry needs --run.")
    flags = []
    if args.run:
        same_run = [e for e in entries if e.get("run") == args.run]
        has_prediction = any(e["type"] == "prediction" for e in same_run)
        has_observation = any(e["type"] == "observation" for e in same_run)
        if args.type == "observation" and not has_prediction:
            if not args.force:
                sys.exit(f"Run {args.run} has no prediction yet. Record one first, or use --force to log the gap.")
            flags.append("no_prior_prediction")
        if args.type == "prediction" and has_observation:
            if not args.force:
                sys.exit(f"Run {args.run} already has an observation. A prediction now is hindsight; use --force to log it as such.")
            flags.append("after_outcome")
    if args.at:
        try:
            happened = datetime.fromisoformat(args.at)
        except ValueError:
            sys.exit(f"--at is not an ISO time: {args.at}")
        if happened.tzinfo is None:
            sys.exit("--at needs a UTC offset, for example 2026-10-08T14:03-07:00.")
    files = hash_files(args.root, args.campaign, args.file or [])
    entry = new_entry(entries, args.type, args.author, read_text(args), args.run, files, flags,
                      parse_data(args.data), args.at)
    append(args.root, args.campaign, entry)
    note = f" [{', '.join(flags)}]" if flags else ""
    print(f"Entry {entry['seq']} ({args.type}) added{note}. Head {entry['hash'][:12]}.")


def cmd_verify(args):
    entries = load(args.root, args.campaign)
    base = campaign_dir(args.root, args.campaign)
    problems = []
    prev = None
    for i, e in enumerate(entries, start=1):
        if e.get("seq") != i:
            problems.append(f"entry {i}: sequence number is {e.get('seq')}")
        if e.get("prev") != prev:
            problems.append(f"entry {i}: does not chain to the entry before it")
        if entry_hash(e) != e.get("hash"):
            problems.append(f"entry {i}: content does not match its hash")
        for f in e.get("files", []):
            path = base / f["path"]
            if not path.is_file():
                problems.append(f"entry {i}: file missing: {f['path']}")
            elif sha256_bytes(path.read_bytes()) != f["sha256"]:
                problems.append(f"entry {i}: file changed since logging: {f['path']}")
        prev = e.get("hash")

    runs = sorted({e["run"] for e in entries if e.get("run")})
    clean = with_outcome = 0
    for run in runs:
        first_pred = next((e["seq"] for e in entries if e.get("run") == run and e["type"] == "prediction"), None)
        first_obs = next((e["seq"] for e in entries if e.get("run") == run and e["type"] == "observation"), None)
        if first_obs:
            with_outcome += 1
        if first_pred and first_obs and first_pred < first_obs:
            clean += 1
    flagged = [e for e in entries if e.get("flags")]

    # Exact repeats: a later run whose plan settings match an earlier run's.
    seen = {}
    repeats = cross_session = 0
    for e in entries:
        sig = settings_signature(e.get("data")) if e["type"] == "plan" and e.get("run") else None
        if not sig:
            continue
        session = e["data"].get("_session")
        if sig in seen:
            repeats += 1
            if session is not None and any(session != s for s in seen[sig]):
                cross_session += 1
        seen.setdefault(sig, []).append(session)

    print(f"{args.campaign}: {len(entries)} entries, {len(runs)} runs.")
    print(f"Runs with a prediction logged before the outcome: {clean} of {with_outcome} that have an outcome.")
    print(f"Exact repeats of an earlier plan: {repeats}, of which in a different session: {cross_session}.")
    for e in flagged:
        print(f"Flagged entry {e['seq']} (run {e.get('run')}): {', '.join(e['flags'])}")
    if problems:
        print("INTEGRITY PROBLEMS:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print(f"Chain and file hashes intact. Head {prev[:12] if prev else '-'}.")


def cmd_show(args):
    entries = load(args.root, args.campaign)
    # Runs marked _split=test are held back: their outcomes must never be pasted into a model.
    held_back = {e["run"] for e in entries if e.get("run") and (e.get("data") or {}).get("_split") == "test"}
    for e in entries:
        if args.run and e.get("run") != args.run:
            continue
        if args.hide_test and e.get("run") in held_back:
            continue
        if args.exclude_run and e.get("run") == args.exclude_run:
            continue
        run = f" {e['run']}" if e.get("run") else ""
        flags = f" [{', '.join(e['flags'])}]" if e.get("flags") else ""
        print(f"#{e['seq']} {e['ts']} {e['type']}{run} by {e['author']}{flags}")
        print("    " + e["text"].replace("\n", "\n    "))
        if e.get("data"):
            print("    data: " + json.dumps(e["data"], sort_keys=True))
        if e.get("at"):
            print(f"    happened at: {e['at']}")
        for f in e.get("files", []):
            print(f"    file: {f['path']} ({f['sha256'][:12]})")


def cmd_anchor(args):
    entries = load(args.root, args.campaign)
    line = f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {args.campaign} {len(entries)} {entries[-1]['hash']}\n"
    anchors = Path(args.root).resolve().parent / "anchors.log"
    with anchors.open("a") as f:
        f.write(line)
    print(f"Anchored entry {len(entries)} in {anchors}. Commit and push that file to timestamp it publicly.")


def main():
    p = argparse.ArgumentParser(description="Hash-chained trajectory log for hand-run experiments.")
    p.add_argument("--root", default=str(HERE / "campaigns"), help="folder holding campaigns (default: trajectory/campaigns)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init", help="start a campaign with its goal")
    s.add_argument("campaign")
    s.add_argument("--text")
    s.add_argument("--author", default="human")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("add", help="append one entry")
    s.add_argument("campaign")
    s.add_argument("type", choices=TYPES)
    s.add_argument("--run", help="run id, e.g. R01")
    s.add_argument("--author", default="human", help="'human' or 'ai:<model name and version>'")
    s.add_argument("--text")
    s.add_argument("--file", action="append", help="raw file inside the campaign folder; repeatable")
    s.add_argument("--data", action="append", metavar="KEY=VALUE",
                   help="structured field; repeatable. Plain keys are settings; keys starting with '_' are context, e.g. _session, _lot, _chosen_by, _status")
    s.add_argument("--at", help="when it actually happened, if not now (ISO time with UTC offset)")
    s.add_argument("--force", action="store_true", help="log an out-of-order entry and flag it")
    s.set_defaults(func=cmd_add)

    s = sub.add_parser("verify", help="check the chain, the files and the prediction-before-outcome rule")
    s.add_argument("campaign")
    s.set_defaults(func=cmd_verify)

    s = sub.add_parser("show", help="print the log")
    s.add_argument("campaign")
    s.add_argument("--run")
    s.add_argument("--hide-test", action="store_true", help="leave out every run marked _split=test; use this for anything pasted into a model")
    s.add_argument("--exclude-run", help="leave out one run, so its own plan and first prediction stay out of its second prompt")
    s.set_defaults(func=cmd_show)

    s = sub.add_parser("anchor", help="write the head hash to anchors.log for public timestamping")
    s.add_argument("campaign")
    s.set_defaults(func=cmd_anchor)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
