#!/usr/bin/env python3
"""Copy a route's VN art from the landing folder (../catalog) into the Ren'Py game, and work out the PC
sprites' head crops for the face portrait. Every picture goes in as AVIF under its own .jpg/.png name
(tools/artformat.py, 2026-11-15).

    python3 tools/sync_art.py redlightning

Sources (the pipeline's landing places; nothing here generates or picks art):
  catalog/img/vn/<route>/*.jpg|png      backgrounds, frames, sprites (sceneart.py vnland)
  catalog/img/scenes/<route>/*.jpg      the route's scene-art pictures (sceneart.py land)
  catalog/imagepacks/_custom/ui/route-covers/<route>.jpg   its route cover -> cover.jpg
Into game/art/<route>/ and game/art/<route>/scenes/. Free-play-only frames (SKIP) stay behind.
Writes game/<route>/faces.rpy: the head crop of every PC sprite, from its alpha, the way the DoL
screen's portrait() finds it (the figure's top, about a sixth of its height, centred on the
opaque columns there).
"""
import json
import pathlib
import sys

from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # -I leaves the tool's folder off the path
import artformat  # noqa: E402  (every picture goes in as AVIF under its own name; see artformat.py)

ROOT = pathlib.Path(__file__).resolve().parents[1]
CATALOG = ROOT.parent / "catalog"
SKIP = {"redlightning": ("afterhours-",), "hypno": ("afterwards-",)}


def head_crop(path):
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    a = im.getchannel("A").load()
    top = next((y for y in range(h) if any(a[x, y] > 128 for x in range(0, w, 2))), 0)
    # the whole head, hair to chin (owner, 2026-11-11: a sixth of the height cut the chin off)
    side = round(h * 0.23)
    xs = [x for y in range(top, min(h, top + int(side * 0.6)), 3) for x in range(0, w, 2) if a[x, y] > 128]
    cx = sum(xs) / len(xs) if xs else w / 2
    x0 = max(0, min(w - side, round(cx - side / 2)))
    y0 = max(0, top - round(side * 0.04))
    return [x0, y0, side, side]


def main():
    route = sys.argv[1] if len(sys.argv) > 1 else "redlightning"
    src = CATALOG / "img" / "vn" / route
    scenes = CATALOG / "img" / "scenes" / route
    dst = ROOT / "game" / "art" / route
    dst.mkdir(parents=True, exist_ok=True)
    skip = SKIP.get(route, ())
    n = 0
    for f in sorted(src.iterdir()):
        if f.suffix not in (".jpg", ".png") or f.name.startswith(skip):
            continue
        out = dst / f.name
        if not out.exists() or out.stat().st_mtime < f.stat().st_mtime:
            artformat.place(f, out)
            n += 1
    # the catalog's scene-art pictures come over only when the route's script shows them as
    # "scenes/<name>" (redlightning, hypno); a route whose frames all live in img/vn/ (collar,
    # neighbour) would carry them for nothing (2026-11-12: 31 unused files)
    uses_scenes = any("scenes/" in p.read_text(errors="replace") for p in (ROOT / "game" / route).glob("*.rpy"))
    if uses_scenes:
        (dst / "scenes").mkdir(exist_ok=True)
        for f in sorted(scenes.glob("*.jpg")):
            out = dst / "scenes" / f.name
            if not out.exists() or out.stat().st_mtime < f.stat().st_mtime:
                artformat.place(f, out)
                n += 1
    cover = CATALOG / "imagepacks" / "_custom" / "ui" / "route-covers" / f"{route}.jpg"
    if cover.exists():
        out = dst / "cover.jpg"
        if not out.exists() or out.stat().st_mtime < cover.stat().st_mtime:
            artformat.place(cover, out)
            n += 1
    # the route's other art sets (catalog/img/vn/<route>@<set>/, e.g. hypno@abarus): copied whole
    # beside the default; the game picks a picture from the chosen set where it has one
    sets = sorted(p for p in (CATALOG / "img" / "vn").glob(route + "@*") if p.is_dir())
    for sd in sets:
        # "<route>.<set>": Ren'Py reads an "@" in an image path as a modifier (file@2x)
        out_dir = ROOT / "game" / "art" / sd.name.replace("@", ".")
        out_dir.mkdir(parents=True, exist_ok=True)
        for f in sorted(sd.iterdir()):
            if f.suffix not in (".jpg", ".png") or f.name.startswith(skip):
                continue
            out = out_dir / f.name
            if not out.exists() or out.stat().st_mtime < f.stat().st_mtime:
                artformat.place(f, out)
                n += 1
    # Crops come from the landing folder's original when there is one: the game file is AVIF, whose alpha is lossy,
    # so cropping it moved a few crops by a pixel on every sync (c9, 2026-11-15: six of hypno's, reverted as noise).
    def crop_of(f, landing):
        o = landing / f.name
        return head_crop(o if o.exists() else f)
    crops = {f.stem: crop_of(f, src) for f in sorted(dst.glob("pc-*.png"))}
    # a set's own sprites get their own crops, keyed "<set>:<stem>"
    for sd in sets:
        tag = sd.name.split("@", 1)[1]
        for f in sorted((ROOT / "game" / "art" / sd.name.replace("@", ".")).glob("pc-*.png")):
            crops[f"{tag}:{f.stem}"] = crop_of(f, sd)
    rpy = ROOT / "game" / route / "faces.rpy"
    rpy.parent.mkdir(parents=True, exist_ok=True)
    rpy.write_text("## GENERATED by tools/sync_art.py: the PC sprites' head crops (x, y, w, h) for the face\n"
                   "## portrait in the box while a CG is up. Do not edit; re-run the tool.\n\n"
                   f"define {route}_face_crops = {json.dumps(crops, indent=4)}\n")
    print(f"placed {n} files (AVIF) into {dst.relative_to(ROOT)}; {len(crops)} head crops in {rpy.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
