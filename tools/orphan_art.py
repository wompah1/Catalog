#!/usr/bin/env python3
"""Report art files under game/art/<route>/ that no .rpy text names. A report, not a deleter.

    python3 tools/orphan_art.py [route ...]        # all routes when none is given

A file counts as referenced when its stem (name without extension, "scenes/<stem>" for the
scenes folder) appears in the route's game/<route>/*.rpy or game/catalog/*.rpy. A picture a
script names by a template ("co_card_%d" -> card_1.jpg...) or a twin a resolver builds
("-full.jpg", a face suffix) is NOT found by this check and is listed under "check by hand":
its stem minus trailing digits / "-full" / a face word does appear. Another art set
(game/art/<route>.<set>/) is judged by the default set's references, file name by file name.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
FACES = ("neutral", "nervous", "happy", "trance", "eager", "smile", "stern", "smirk", "grin",
         "flushed", "shocked", "blush", "hungry", "sad", "angry", "shy", "lust", "cum", "cry")


def rpy_text(route):
    files = list((GAME / route).glob("*.rpy")) + list((GAME / "catalog").glob("*.rpy"))
    return "\n".join(p.read_text(errors="replace") for p in files)


def loose_stem(stem):
    s = re.sub(r"-full$", "", stem)
    s = re.sub(r"[-_]?\d+$", "", s)
    for f in FACES:
        s = re.sub(r"-%s$" % f, "", s)
    return s


def check(route):
    art = GAME / "art" / route
    if not art.is_dir():
        print("%s: no art folder" % route)
        return
    text = rpy_text(route)
    # the route's image-name prefix ("co_"), from its vn_register_bg/cg loop; a short stem such as
    # "bell" is only referenced as "hy_bell" or quoted, never as a word in the prose
    m = re.search(r'vn_register_(?:bg|cg)\("([a-z]+_)"', text)
    prefix = m.group(1) if m else None
    folders = [art] + sorted(p for p in (GAME / "art").glob(route + ".*") if p.is_dir())
    orphans, by_hand = [], []
    for folder in folders:
        for f in sorted(folder.rglob("*")):
            if not f.is_file() or f.suffix not in (".jpg", ".png", ".webp"):
                continue
            rel = f.relative_to(folder)
            stem = str(rel.with_suffix(""))
            # the routes register "cg co_couch_chest" for couch-chest.jpg: the prefixed underscore
            # form counts, as does the file name quoted or in a path ("scenes/foo", "foo.jpg")
            bare = stem.rsplit("/", 1)[-1]
            forms = set()
            if prefix:
                forms.add(prefix + bare.replace("-", "_"))
            else:
                forms.add(bare.replace("-", "_"))
            forms.update('"%s' % bare, "'%s" % bare, "/%s" % bare, "%s.jpg" % bare, "%s.png" % bare)
            if f.name == "cover.jpg" or any(s in text for s in forms):
                continue
            loose = loose_stem(stem.rsplit("/", 1)[-1])
            (by_hand if loose and loose in text else orphans).append(f.relative_to(GAME / "art"))
    print("%s: %d referenced-by-name misses" % (route, len(orphans) + len(by_hand)))
    for p in orphans:
        print("  orphan      %s  (%d KB)" % (p, (GAME / "art" / p).stat().st_size // 1024))
    for p in by_hand:
        print("  check by hand  %s  (a template or a twin may build this name)" % p)


def main():
    routes = sys.argv[1:] or sorted(p.name for p in (GAME / "art").iterdir() if p.is_dir() and "." not in p.name)
    for r in routes:
        check(r)


if __name__ == "__main__":
    main()
