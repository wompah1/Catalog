#!/usr/bin/env python3
"""The pre-publish review gate (owner, 2026-11-16 ~12:44 am ET: a chat other than the builder walks every route
before it publishes; brief and register in ../route-covers/pipeline/REVIEWS.md).

    python3 -I tools/review_gate.py <route> [...]

For each route, the newest register row naming it must say "passed at <commit>", and that commit's copy of the
route (game/<route>/, game/art/<route>/, game/art/<route>.<set>/) must be the same as HEAD's: a pass is for that
commit only, so anything changed in the route since (a redraw, a recut, a script fix, regenerated face crops)
needs the reviewer again. Prints one line per route and exits 1 if any fails. tools/publish.sh runs it on every
route whose art changed since the last publish.

CATALOG_PUBLISH_UNREVIEWED=route1,route2 lets those routes through with a warning: the owner's yes only.
"""
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTER = ROOT.parent / "route-covers" / "pipeline" / "REVIEWS.md"


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


def rows():
    """(route, status, builder) for each register row, newest first as the file keeps them."""
    out, on = [], False
    for line in REGISTER.read_text().splitlines():
        if line.startswith("## Register"):
            on = True
            continue
        if on and line.startswith("## "):
            break
        if not on or not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 7 or cols[1] in ("route", "") or set(cols[1]) <= set("-: "):
            continue
        m = re.match(r"`?([a-z0-9]+)", cols[1].lower())
        if m:
            out.append((m.group(1), cols[6], cols[2]))
    return out


def paths(route, commit):
    names = git("ls-tree", "--name-only", commit, "game/art/").stdout.split()
    return [f"game/{route}", f"game/art/{route}"] + [n for n in names if n.startswith(f"game/art/{route}.")]


def check(route, register):
    row = next((s for r, s, _ in register if r == route), None)
    if row is None:
        return f"no register row (add one when the art is in and your own walk is done)"
    m = re.search(r"passed at\s*`?([0-9a-f]{7,40})", row)
    if not m:
        return f"newest row says {row!r}, not passed"
    commit = m.group(1)
    if git("cat-file", "-e", commit + "^{commit}").returncode:
        return f"passed at {commit}, which this repo doesn't have"
    ps = sorted(set(paths(route, commit)) | set(paths(route, "HEAD")))
    changed = git("diff", "--name-only", commit, "HEAD", "--", *ps).stdout.split()
    if changed:
        return (f"passed at {commit}, but {len(changed)} of its files changed since "
                f"({', '.join(changed[:3])}{' ...' if len(changed) > 3 else ''}); the reviewer needs this commit")
    return None


def builder(route, register):
    """Whom a blocked chat should chase: the register row's builder, else the chat named in the last commit
    that touched the route ("... (twinetesting-c9)")."""
    b = next((bd for r, _, bd in register if r == route and bd), None)
    if b:
        return f"builder {b} (register)"
    log = git("log", "-1", "--format=%h %s", "HEAD", "--", *paths(route, "HEAD")).stdout.strip()
    m = re.search(r"twinetesting-(\w+)", log)
    return (f"last changed by {m.group(1)} in {log.split()[0]}" if m else f"last changed in {log.split()[0]}") if log else "builder unknown"


def main():
    routes = sorted({r.split(".", 1)[0] for r in sys.argv[1:] if r.strip()})
    if not routes:
        return 0
    if not REGISTER.exists():
        print(f"review gate: no register at {REGISTER}")
        return 1
    register = rows()
    waived = set(filter(None, os.environ.get("CATALOG_PUBLISH_UNREVIEWED", "").split(",")))
    bad = 0
    for route in routes:
        why = check(route, register)
        if why is None:
            print(f"review gate: {route}: passed")
        elif route in waived:
            print(f"review gate: {route}: {why} -- let through by CATALOG_PUBLISH_UNREVIEWED (the owner's yes only)")
        else:
            print(f"review gate: {route} ({builder(route, register)}): {why}")
            bad += 1
    if bad:
        print("review gate: publish.sh ships all of main, so one unreviewed route blocks every chat's publish; route art "
              "lands on its route branch and merges to main after the pass (REVIEWS.md step 0). Ask the chat named above.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
