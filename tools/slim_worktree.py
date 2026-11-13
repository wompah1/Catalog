#!/usr/bin/env python3
"""Slim a route worktree: a sparse checkout that leaves out OTHER routes' art.

    python3 tools/slim_worktree.py ../catalog-renpy-ace          # one worktree
    python3 tools/slim_worktree.py --all [--dry-run]             # every worktree but main
    python3 tools/slim_worktree.py --undo ../catalog-renpy-ace   # back to a full checkout

Each `catalog-renpy-<route>` worktree checked out all of game/art (~217 MB in 2026-11; 96
worktrees came to ~20 GB). A worktree needs its own route's art to play and test it, every
route's cover.jpg (the main menu and the route cards draw them all), and nothing else from
game/art. Patterns (non-cone sparse checkout; later patterns win):

    /*                          everything
    !/game/art/*/**             but no files under any art folder
    /game/art/*/cover.jpg       except each route's cover
    /game/art/<route>/**        and this worktree's own route(s), with their other art sets
    /game/art/<route>.*/**

Which routes a worktree owns: the `game/<x>/route.rpy` folders it has that the main checkout
(this repo's root) lacks, plus the route its folder is named after (`catalog-renpy-<route>`)
when that `game/<route>/` exists in it. `--route <id>` adds one by hand. The main checkout is
never slimmed.

Excluded files are skip-worktree, not deleted from git: `git status` stays clean, commits and
merges work as before, and merging main later leaves other routes' new art out automatically.
`git sparse-checkout` turns on extensions.worktreeConfig itself (git >= 2.20).
"""
import argparse
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def git(*args, cwd=ROOT, check=True):
    return subprocess.run(["git", "-C", str(cwd), *args], check=check, text=True, capture_output=True).stdout


def worktrees():
    """Every worktree path but the main checkout."""
    out = []
    for line in git("worktree", "list", "--porcelain").splitlines():
        if line.startswith("worktree "):
            p = pathlib.Path(line[len("worktree "):])
            if p.resolve() != ROOT.resolve():
                out.append(p)
    return out


def route_dirs(game):
    return {p.parent.name for p in game.glob("*/route.rpy")}


def own_routes(wt, extra=()):
    own = route_dirs(wt / "game") - route_dirs(ROOT / "game")
    suffix = wt.name.split("catalog-renpy-", 1)[-1] if wt.name.startswith("catalog-renpy-") else ""
    if suffix and (wt / "game" / suffix / "route.rpy").exists():
        own.add(suffix)
    own.update(extra)
    return sorted(own)


def patterns(routes):
    pats = ["/*", "!/game/art/*/**", "/game/art/*/cover.jpg"]
    for r in routes:
        pats += ["/game/art/%s/**" % r, "/game/art/%s.*/**" % r]
    return pats


def dropped_mb(wt, routes):
    """MB of art the sparse checkout would leave out of this worktree (what's on disk now)."""
    art = wt / "game" / "art"
    if not art.is_dir():
        return 0.0
    total = 0
    for d in art.iterdir():
        if not d.is_dir():
            continue
        base = d.name.split(".", 1)[0]
        if base in routes:
            continue
        for f in d.rglob("*"):
            if f.is_file() and f.name != "cover.jpg":
                total += f.stat().st_size
    return total / 1e6


def slim(wt, extra=(), dry_run=False):
    routes = own_routes(wt, extra)
    pats = patterns(routes)
    mb = dropped_mb(wt, routes)
    print("%s: keeps %s; drops %.0f MB%s" % (wt.name, ", ".join(routes) or "(covers only)", mb, " (dry run)" if dry_run else ""))
    if dry_run:
        return mb
    git("sparse-checkout", "set", "--no-cone", *pats, cwd=wt)
    return mb


def undo(wt):
    git("sparse-checkout", "disable", cwd=wt)
    print("%s: full checkout again" % wt.name)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("worktree", nargs="*", help="worktree path(s)")
    ap.add_argument("--all", action="store_true", help="every worktree but the main checkout")
    ap.add_argument("--undo", action="store_true", help="disable the sparse checkout instead")
    ap.add_argument("--dry-run", action="store_true", help="print what would be kept and dropped")
    ap.add_argument("--route", action="append", default=[], help="a route this worktree also owns")
    a = ap.parse_args()
    wts = worktrees() if a.all else [pathlib.Path(w).resolve() for w in a.worktree]
    if not wts:
        ap.error("give a worktree path or --all")
    total = 0.0
    for wt in wts:
        if wt.resolve() == ROOT.resolve():
            print("%s is the main checkout; skipped" % wt)
            continue
        if not (wt / ".git").exists():
            print("%s: not a worktree; skipped" % wt)
            continue
        if a.undo:
            undo(wt)
        else:
            total += slim(wt, a.route, a.dry_run)
    if not a.undo and len(wts) > 1:
        print("total: %.1f GB %s" % (total / 1000, "would be dropped" if a.dry_run else "dropped"))


if __name__ == "__main__":
    main()
