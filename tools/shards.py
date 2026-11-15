#!/usr/bin/env python3
"""Connected art repos: which routes' art is published from which Pages site (tools/shards.json).

    python3 tools/shards.py sizes              # Catalog's and each shard's art size in HEAD's tree (a shard should stay under 900 MB)
    python3 tools/shards.py list               # "<n> <owner/repo> <key>" per shard (publish.sh, pages.yml)
    python3 tools/shards.py map                # {"<route>": "../<repo>/"}: game/catalog/webshards.json for the web build
    python3 tools/shards.py tree catalog <T>   # tree T without the sharded routes' art (covers stay): Catalog's snapshot
    python3 tools/shards.py tree <n> <T>       # shard n's snapshot: its routes' art from tree T, plus .nojekyll
    python3 tools/shards.py strip <dist>       # delete the sharded routes' art from a web build (after web_build)

Every site lives on wompah1.github.io, one origin, so the game fetches a sharded route's pictures from
../<repo>/game/art/... with no CORS and the same saves (game/catalog/webshards.rpy redirects the web
build's downloads). Desktop builds and local web builds carry every picture and redirect nothing."""
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / "tools" / "shards.json").read_text())
SHARDS = CFG.get("shards", [])
SHARDED = {r: s["n"] for s in SHARDS for r in s.get("routes", [])}


def git(*args, inp=None, env=None):
    return subprocess.run(["git", "-C", str(ROOT), *args], input=inp, env=env, check=True,
                          capture_output=True, text=isinstance(inp, str) or inp is None).stdout


def art_of(path):
    """(route, is_cover) for a path under game/art/<route>[.<set>]/..., else (None, False)."""
    p = path.split("/")
    if len(p) < 4 or p[0] != "game" or p[1] != "art":
        return None, False
    return p[2].split(".", 1)[0], len(p) == 4 and "." not in p[2] and p[3] == "cover.jpg"


def which(path):
    """The shard a file is published from: 0 for Catalog."""
    route, cover = art_of(path)
    return 0 if route is None or cover else SHARDED.get(route, 0)


def tree(n, t):
    out = git("ls-tree", "-r", "-z", "--full-tree", t)
    keep = [e for e in out.split("\0") if e and which(e.split("\t", 1)[1]) == n]
    if n != 0:
        blob = git("hash-object", "-w", "--stdin", inp="").strip()
        keep.append(f"100644 blob {blob}\t.nojekyll")
    with tempfile.TemporaryDirectory() as d:
        env = dict(os.environ, GIT_INDEX_FILE=os.path.join(d, "index"))
        git("read-tree", "--empty", env=env)
        git("update-index", "-z", "--index-info", inp="\0".join(keep) + "\0", env=env)
        return git("write-tree", env=env).strip()


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sizes"
    if cmd == "list":
        for s in SHARDS:
            print(s["n"], s["repo"], os.path.expanduser(s["key"]))
    elif cmd == "map":
        print(json.dumps({r: "../%s/" % next(s["repo"] for s in SHARDS if s["n"] == n).split("/", 1)[1]
                          for r, n in sorted(SHARDED.items())}))
    elif cmd == "tree":
        print(tree(0 if sys.argv[2] == "catalog" else int(sys.argv[2]), sys.argv[3]))
    elif cmd == "strip":
        art = pathlib.Path(sys.argv[2]) / "game" / "art"
        for d in sorted(art.iterdir()) if art.is_dir() else []:
            if d.is_dir() and d.name.split(".", 1)[0] in SHARDED:
                for f in d.iterdir():
                    if not ("." not in d.name and f.name == "cover.jpg"):
                        shutil.rmtree(f) if f.is_dir() else f.unlink()
                if not any(d.iterdir()):
                    d.rmdir()
        print("stripped", len(SHARDED), "sharded routes' art from", art)
    elif cmd == "sizes":
        sizes = {}
        for line in git("ls-tree", "-r", "-l", "--full-tree", "HEAD", "--", "game/art").splitlines():
            meta, path = line.split("\t", 1)
            sizes[which(path)] = sizes.get(which(path), 0) + int(meta.split()[3])
        names = {0: "Catalog", **{s["n"]: s["repo"] for s in SHARDS}}
        for n in sorted(set(sizes) | set(names)):
            mb = sizes.get(n, 0) / 1e6
            print(f"  {names.get(n, n):28} {mb:7.1f} MB" + ("   over 850 MB: add a shard" if mb > 850 else ""))
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
