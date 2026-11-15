#!/usr/bin/env python3
"""Re-encode a route's landed art as AVIF in place, keeping every file name (owner's storage plan,
2026-11-15; the format and why names don't change: tools/artformat.py).

    python3 tools/convert_art.py collar                 # game/art/collar/ (with scenes/) and collar.<set>/
    python3 tools/convert_art.py --all [--dry-run]      # every art folder in this checkout

Each picture is encoded from its original in ../route-covers/vn/<route>[@<set>]/<name>.png when that is the
same picture (a thumbnail check; a re-landed pick not yet synced fails it), resized to the game file's size;
otherwise from the game file itself. Only tracked files are converted. A file already AVIF is skipped, so a
second run changes nothing. A folder with uncommitted changes (another session mid-landing) is skipped and
reported; untracked files a commit deleted (orphan art put back by a sync) don't count. Each file keeps its
mtime, which sync_art.py compares. Run it on a route right after it merges to main (publish-when-done)."""
import argparse
import io
import os
import pathlib
import subprocess
import sys

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # -I leaves the tool's folder off the path
import artformat  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
ART = ROOT / "game" / "art"
ORIGINALS = ROOT.parent / "route-covers" / "vn"


def thumb(im):
    im = im.convert("RGBA")
    bg = Image.new("RGBA", im.size, (128, 128, 128, 255))
    return Image.alpha_composite(bg, im).convert("L").resize((24, 24), Image.BILINEAR)


def same_picture(a, b):
    ta, tb = thumb(a), thumb(b)
    diff = sum(abs(x - y) for x, y in zip(ta.tobytes(), tb.tobytes())) / (24 * 24)
    return diff < 10


def source_for(f, game_im, folder):
    """The original to encode from, resized to the game file's size, or None to use the game file."""
    route, _, set_id = folder.partition(".")
    orig = ORIGINALS / (route + ("@" + set_id if set_id else "")) / (f.stem + ".png")
    if f.parent.name == "scenes" or not orig.exists():
        return None
    with Image.open(orig) as o:
        o.load()
    gw, gh = game_im.size
    if abs(o.width / o.height - gw / gh) > 0.01:
        return None
    o = o.resize((gw, gh), Image.LANCZOS) if o.size != (gw, gh) else o
    return o if same_picture(o, game_im) else None


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True).stdout


def dirty(folder):
    """Uncommitted changes in the folder, leaving out untracked files a commit deleted: orphan art
    (tools/orphan_art.py) that sync_art.py's whole-set copy puts back on disk, nobody's landing."""
    for line in git("status", "--porcelain", "--untracked-files=all", "--", f"game/art/{folder}").splitlines():
        if not line.startswith("?? ") or not git("log", "-1", "--format=%h", "--diff-filter=D", "--", line[3:]).strip():
            return True
    return False


def convert(folder, dry):
    tracked = set(git("ls-files", "-z", "--", f"game/art/{folder}").split("\0"))
    files = sorted(p for p in (ART / folder).rglob("*") if p.suffix in (".jpg", ".png") and p.is_file()
                   and p.relative_to(ROOT).as_posix() in tracked)
    before = after = n = from_orig = 0
    for f in files:
        if artformat.is_avif(f):
            continue
        raw = f.read_bytes()
        with Image.open(io.BytesIO(raw)) as im:
            im.load()
        alpha = artformat.has_alpha(im)
        src = source_for(f, im, folder)
        data = artformat.encode(src if src is not None else im, alpha)
        if len(data) >= len(raw):
            continue
        before += len(raw)
        after += len(data)
        n += 1
        from_orig += src is not None
        if not dry:
            artformat.write(data, f, mtime=f.stat().st_mtime)
    print(f"  {folder:22} {n:4} files  {before / 1e6:7.1f} MB -> {after / 1e6:6.1f} MB"
          f"  ({from_orig} from originals)" + ("  [dry run]" if dry else ""))
    return before, after


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("route", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not a.route and not a.all:
        ap.error("a route, or --all")
    folders = sorted(p.name for p in ART.iterdir() if p.is_dir() and (a.all or p.name == a.route or p.name.startswith(a.route + ".")))
    tb = ta = 0
    for folder in folders:
        if dirty(folder):
            print(f"  {folder:22} skipped: uncommitted changes (someone mid-landing?)")
            continue
        b, af = convert(folder, a.dry_run)
        tb, ta = tb + b, ta + af
    print(f"total {tb / 1e6:.1f} MB -> {ta / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
