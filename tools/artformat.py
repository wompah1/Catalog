"""The game's picture format (owner's storage plan, 2026-11-15): AVIF at quality 65, written under the file's
existing .jpg/.png name. Ren'Py picks an image's decoder from its contents, not its name: tested 2026-11-15 on
desktop, in a web build, through progressive download (placeholders, then the file) and with sprite alpha. So
no route's code, gallery list, frames.json or slim pattern has to change. A frame is about 45% of its JPEG, a
sprite about 10% of its PNG, with no visible difference at full size (Vanripper and Abarus checked side by side).
Used by tools/sync_art.py (every new landing) and tools/convert_art.py (art landed before the switch)."""
import io
import os

from PIL import Image

QUALITY = 65


def is_avif(path):
    with open(path, "rb") as f:
        head = f.read(12)
    return head[4:8] == b"ftyp" and head[8:12] in (b"avif", b"avis")


def has_alpha(im):
    return im.mode in ("RGBA", "LA", "PA") or "transparency" in im.info


def encode(im, alpha):
    b = io.BytesIO()
    im.convert("RGBA" if alpha else "RGB").save(b, "AVIF", quality=QUALITY)
    return b.getvalue()


def write(data, out, mtime=None):
    """`data` to `out` through a temp file; `mtime` stamps it (sync_art compares mtimes to skip unchanged
    pictures). Returns the bytes written."""
    tmp = str(out) + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, out)
    if mtime is not None:
        os.utime(out, (mtime, mtime))
    return len(data)


def place(src, out):
    """A landed picture (.jpg/.png) into the game under out's name, as AVIF, with src's mtime. A picture
    whose AVIF would be bigger (a tiny file) goes over as it is."""
    with open(src, "rb") as f:
        raw = f.read()
    with Image.open(io.BytesIO(raw)) as im:
        im.load()
        data = raw if is_avif(src) else encode(im, has_alpha(im))
    return write(data if len(data) < len(raw) else raw, out, mtime=os.stat(src).st_mtime)
