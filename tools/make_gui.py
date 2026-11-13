#!/usr/bin/env python3
"""The VN layer's GUI shapes (game/gui/vn/): the textbox, the name-plate pill (white, tinted per
speaker at runtime) and the portrait frame. Plain shapes, drawn here so the look matches the DoL
VN screen's CSS (modules/css/vn-screen.css): box rgba(10,10,16,.84) with rounded corners, plate a
5px-radius pill, portrait an 8px-radius square with a light border. Re-run after changing a value.

    python3 tools/make_gui.py
"""
import pathlib

from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).resolve().parents[1] / "game" / "gui" / "vn"
SS = 4   # supersampling for smooth corners


def rounded(size, radius, fill, outline=None, width=0):
    w, h = size
    im = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w * SS - 1, h * SS - 1), radius=radius * SS, fill=fill,
                        outline=outline, width=width * SS)
    return im.resize((w, h), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # the textbox: a 9-slice source, 64px with 16px corners
    rounded((64, 64), 16, (10, 10, 16, 214), outline=(255, 255, 255, 26), width=1).save(OUT / "box.png")
    # the name plate: white, tinted to the speaker's colour by the say screen
    rounded((48, 48), 10, (255, 255, 255, 255)).save(OUT / "pill.png")
    # the PC's face over a CG: frame drawn over the cropped head
    rounded((224, 224), 18, (255, 255, 255, 20), outline=(255, 255, 255, 90), width=4).save(OUT / "face_frame.png")
    # a route card on the route select (idle, and hovered with the accent edge)
    rounded((96, 96), 18, (22, 22, 30, 235), outline=(255, 255, 255, 30), width=2).save(OUT / "card.png")
    rounded((96, 96), 18, (44, 20, 26, 245), outline=(212, 49, 61, 255), width=4).save(OUT / "card_hover.png")
    # the HUD chip (day and time)
    rounded((48, 48), 12, (20, 20, 26, 200)).save(OUT / "chip.png")
    print("wrote", ", ".join(p.name for p in sorted(OUT.glob("*.png"))))
    standard_gui()


ACCENT, MUTED, HOVER_MUTED, IDLE = (212, 49, 61, 255), (84, 19, 24, 255), (127, 29, 36, 255), (136, 136, 136, 255)


def standard_gui():
    """The default GUI's bars, sliders, scrollbars, check/radio marks and slot frames, which Ren'Py
    8.5's generate_gui doesn't draw (a new project without them crashes on its main menu). Drawn
    in the project's palette (gui.rpy: accent #d4313d, muted #541318) at 1920x1080 sizes."""
    gui = OUT.parent
    for d in ("bar", "slider", "scrollbar", "button"):
        (gui / d).mkdir(exist_ok=True)

    def solid(size, fill):
        return Image.new("RGBA", size, fill)

    def save(im, rel):
        im.save(gui / rel)

    # buttons: no background of their own (the default theme's are transparent)
    for k in ("idle", "hover"):
        save(solid((300, 54), (0, 0, 0, 0)), f"button/{k}_background.png")
    for k in ("check", "radio"):
        save(solid((27, 54), (0, 0, 0, 0)), f"button/{k}_foreground.png")
        sel = solid((27, 54), (0, 0, 0, 0))
        sel.paste(ACCENT, (0, 9, 6, 45))
        save(sel, f"button/{k}_selected_foreground.png")
    save(rounded((414, 309), 8, (20, 20, 26, 230)), "button/slot_idle_background.png")
    save(rounded((414, 309), 8, (60, 24, 30, 240), outline=ACCENT, width=3), "button/slot_hover_background.png")
    # bars: filled left/bottom in the accent, the rest muted
    s = 38
    save(solid((s, s), ACCENT), "bar/left.png")
    save(solid((s, s), MUTED), "bar/right.png")
    save(solid((s, s), MUTED), "bar/top.png")
    save(solid((s, s), ACCENT), "bar/bottom.png")
    # sliders and scrollbars: a muted track and a thumb
    for kind, size, thumb in (("slider", 38, (15, 38)), ("scrollbar", 18, (18, 18))):
        for state, bar, th in (("idle", MUTED, ACCENT), ("hover", HOVER_MUTED, (229, 131, 138, 255))):
            save(solid((size, size), bar if kind == "slider" else (40, 40, 48, 255)), f"{kind}/horizontal_{state}_bar.png")
            save(solid((size, size), bar if kind == "slider" else (40, 40, 48, 255)), f"{kind}/vertical_{state}_bar.png")
            save(solid(thumb, th), f"{kind}/horizontal_{state}_thumb.png")
            save(solid((thumb[1], thumb[0]), th), f"{kind}/vertical_{state}_thumb.png")
    print("wrote the standard GUI images (bar, slider, scrollbar, button)")


if __name__ == "__main__":
    main()
