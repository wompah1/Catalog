## Witches -- "I Was Sent In to Clear the Witches Out of the Old Infirmary, and Every Night One More
## Ailment Sticks" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file,
## signed off by the owner). From catalog/game/02-engine/storylines/witches/ (witches.js: the
## words, the kit, the lines, the pools; main.twee, rungs.twee, rungs-late.twee, ending.twee), kept
## verbatim in catalog/docs/routes/vn-original/witches/.
##
## THE NON-CON PASS (owner, 2026-10-27: non-con by magic, aware, resist-then-break, no flip). The
## ailments are the force: his body betrays him, his will never does. All six scenes are non-con and
## none ever flips. Partners never ask; hands and ailments only; no threats, no tears, no pain.
## The fork is a marked choice at the last stroke of rung 6 (the owner, 2026-11-12): his own last
## move decides whether the last ring closes.
##
## Femboy, the cock kept, never a pussy; he/him to the last line. The Shrink rules: never carried
## or lifted, never "tiny", never a size set against a partner's. Six nights, a rung a night, no
## hub; the hospital notice and the hut after the ending are free play, not ported.
## All route-local names carry wit_.

init -10 python:
    WIT = "art/witches/"

    # The words that stick, one a rung, in the owner's order. Rung 6's is the last.
    WIT_WORDS = ["", "Charmed", "In heat", "Shrunk", "Sensitive", "Obedient", "Witchmark"]

    # THE REPORT's Action taken, in biro, at each dawn (setup.witchesAction).
    WIT_ACTION = [None, None, "Engaged hostile. Will clear tonight.", "Engaged hostile. Withdrew.",
                  "Engaged.", "", "Obedient"]

    # THE RINGS (rung 6): the violet climbing, then the hold beat.
    WIT_RINGS = [
        "A thin ring of violet slides into your grey eyes, right at the rim. The lamplight goes faintly purple at its edges.",
        "The violet climbs another ring. Everything in the room has a purple edge now: the canopy, the hooks, Morgause's smile.",
        "Another ring. Your ears go hot and tingly, and draw up, soft, into points. Elspeth squeals.",
        "The violet's past halfway. The grey is just a thin band round the black of your eyes now, and shrinking.",
        "Another ring, and another. Your eyes are nearly all hers. The coven leans in to look.",
    ]

    def wit_stuck(n):
        """The words that have stuck before rung n's night (the purple column at its dawn)."""
        return WIT_WORDS[1:max(1, min(7, n))]

    def wit_body(row):
        """The body takes the row, toward it and never back. Rows: 1, 2, 3 (dawn three: the hair at
        his jaw, the waist), 3s (the Shrink, mid-fight), 4, 5, 6."""
        order = ["1", "2", "3", "3s", "4", "5", "6"]
        cur = wit.row or "1"
        if order.index(str(row)) > order.index(cur):
            wit.row = str(row)

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "kit" (the black Northcott polo, cargo trousers, boots and the hi-vis; rungs 1-3),
    # "women" (the women's-cut polo and trousers, rungs 4-6), "nude", "witch" (End Witch's hat and
    # robe: violet eyes, pointed ears), "pet" (End Pet's belled collar and pyjamas).
    _wit_have = {}

    def _wit_has(n):
        if n not in _wit_have:
            _wit_have[n] = renpy.loadable(WIT + n + ".png")
        return _wit_have[n]

    def wit_pc_file(face):
        r, fit = wit.row or "1", wit.fit or "kit"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-dogged" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-dogged" % r]
        for n in names:
            if _wit_has(n):
                return WIT + n + ".png"
        # ff 2:45 am 11-18 (rptest 5786bd48): no sprite for this face here, so any face in the same
        # outfit, then the nearest lower row; nude stays nude, clothed stays clothed. Never a missing file.
        rows = ["1", "2", "3", "3s", "4", "5", "6"]
        i = rows.index(r) if r in rows else 0
        fits = ("nude",) if fit == "nude" else (fit, "kit", "women", "pet", "witch")
        for rr in rows[i::-1]:
            for f in fits:
                for fc in (face, "dogged", "breaking", "flushed", "outraged"):
                    n = "pc-r%s-%s-%s" % (rr, f, fc)
                    if _wit_has(n):
                        return WIT + n + ".png"
        return WIT + names[-1] + ".png"

    def wit_face_now():
        a = renpy.get_attributes("wit_pc")
        return a[0] if a else "dogged"

    def _wit_portrait(st, at):
        p = vn_art_file(wit_pc_file(wit_face_now()))
        crops = globals().get("witches_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["witches"] = lambda: DynamicDisplayable(_wit_portrait)

    # The calendar: six nights running and a week on for End Witch's epilogue; day 1 a Monday.
    WIT_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def wit_weekday_name():
        return WIT_WD[(1 + vn_clock.day - 1) % 7]    # day 1 is a Monday

    vn_weekdays["witches"] = wit_weekday_name

    vn_sprite_image("wit_pc", ("dogged", "outraged", "flushed", "breaking"), wit_pc_file, who="pc")
    for _w, _faces in (("bryony", ("amused", "intent")), ("rowena", ("amused", "intent")),
                       ("cressida", ("amused", "intent")), ("elspeth", ("amused", "intent")),
                       ("isolde", ("amused", "intent")), ("morgause", ("amused", "intent")),
                       ("rufus", ("steady", "content")), ("niall", ("grin", "witch"))):
        vn_sprite_image("wit_" + _w, _faces, (lambda w: (lambda f: WIT + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(WIT) and _f.endswith(".jpg"):
            _n = _f[len(WIT):-4]
            vn_register_bg("wit_" + _n.replace("-", "_"), _f)
            vn_register_cg("wit_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("witches", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("witches", "I Was Sent In to Clear the Witches Out of the Old Infirmary, and Every Night One More Ailment Sticks",
        "Behind the hospital on Nightingale Street there's an old infirmary wing, shut for years, and men go into it after dark and don't come out. Northcott Security has the contract to clear it. Tonight it sends a team with torches, radios, whistles and bags of rock salt: Rufus, who leads; Niall, who grins; and you, the slight, pretty one the depot lads call Pretty. Every night you lose one fight, and one ailment sticks.",
        WIT + "cover.jpg", "witches_start")

    achievement.register("Hat in His Size")
    achievement.register("A Custard Cream on the Collar")

default wit = VNState(row="1", fit="kit")
default wit_pc_name = "Emrys"

define wit_you = VNChar("[wit_pc_name]", who="pc", plate="#2f4f6f")
define wit_bryony = VNChar("Bryony", who="wit_bryony", plate="#b8925a")
define wit_rowena = VNChar("Rowena", who="wit_rowena", plate="#b0452e")
define wit_cressida = VNChar("Cressida", who="wit_cressida", plate="#3a3a4a")
define wit_elspeth = VNChar("Elspeth", who="wit_elspeth", plate="#a0643a")
define wit_isolde = VNChar("Isolde", who="wit_isolde", plate="#8a9aa8")
define wit_morgause = VNChar("Morgause", who="wit_morgause", plate="#5a2a6a")
define wit_rufus = VNChar("Rufus", who="wit_rufus", plate="#4a5a3a")
define wit_niall = VNChar("Niall", who="wit_niall", plate="#6a7a2a")
define wit_super = VNChar("The supervisor", who="super", plate="#6b6b78")
define wit_radio = VNChar("The radio", who="radio", plate="#6b6b78")

## THE NIGHT LOG (rung 1): three names in block capitals, in biro.
screen wit_log():
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 700
        padding (30, 22)
        background Frame(Solid("#f4f1e6f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}NORTHCOTT SECURITY{/b} · NIGHT LOG · THE OLD WING" size 24 color "#1a1a1a"
            text "RUFUS ............ 22:00" size 24 color "#1d3c8f" font "DejaVuSans.ttf"
            text "NIALL ............ 22:00 :)" size 24 color "#1d3c8f" font "DejaVuSans.ttf"
            text "KETTERING ........ 22:00" size 24 color "#1d3c8f" font "DejaVuSans.ttf"

## THE INCIDENT REPORT at dawn n (2-6): the purple column in a looping hand, one word under the
## last; Action taken in biro (scribbled through at 2; the doodled hat at 5; his own Obedient at 6).
screen wit_report(n):
    zorder 60
    $ _ws = wit_stuck(n)
    frame:
        xalign 0.5 ypos 50 xsize 760
        padding (30, 22)
        background Frame(Solid("#f4f1e6f2"), 0, 0)
        vbox:
            spacing 6
            text "{b}NORTHCOTT SECURITY{/b} · INCIDENT REPORT" size 24 color "#1a1a1a"
            text "{b}Officer:{/b} {color=#1d3c8f}KETTERING{/color}" size 22 color "#1a1a1a"
            text "{b}Officer's condition:{/b}" size 22 color "#1a1a1a"
            for _w in _ws:
                if n == 2:
                    text "{s}%s{/s}" % _w size 30 color "#8e44ad" italic True xoffset 30
                else:
                    text _w size 30 color "#8e44ad" italic True xoffset 30
            if n == 2:
                text "{b}Description of hostile:{/b} {color=#1d3c8f}a whole page, mostly about her thighs, with a small heart at the bottom{/color}" size 22 color "#1a1a1a"
            if n == 5:
                text "{b}Action taken:{/b} {color=#1d3c8f}{i}(blank; in the margin, a little witch's hat){/i}{/color}" size 22 color "#1a1a1a"
            else:
                text "{b}Action taken:{/b} {color=#1d3c8f}%s{/color}" % WIT_ACTION[n] size 22 color "#1a1a1a"

## THE STATUS LINE at the fence: the words that have stuck, in the purple hand.
screen wit_status(n):
    zorder 60
    $ _ws = wit_stuck(n)
    if _ws:
        frame:
            xalign 0.5 ypos 60
            padding (26, 14)
            background Frame(Solid("#141018e0"), 0, 0)
            text " · ".join(_ws) size 30 color "#c48cf0" italic True

label witches_start:
    $ wit = VNState(row="1", fit="kit")
    $ vn_clock = VNState(day=1, hour=21, minute=30)
    $ vn_route = "witches"
    $ wit_pc_name = "Emrys"
    if not renpy.session.get("vn_picks"):
        $ wit_pc_name = renpy.input("Your name? (Emrys, unless you'd like another. The report always says KETTERING.)", default="Emrys", length=20).strip() or "Emrys"
    jump wit_opening

## THE AILMENT LANDS: a bright ting, then its word alone, in purple, on its own line.
label wit_ting(word):
    vn_sfx "{i}ting{/i}" with vnfx("flash")
    $ _wit_w = word
    "{size=+14}{color=#c48cf0}{i}[_wit_w].{/i}{/color}{/size}"
    return

label wit_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"witches"}
    $ vn_route = None
    hide screen wit_log
    hide screen wit_report
    hide screen wit_status
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    if wit.ending == "witch":
        centered "{size=+10}{color=#f3c969}Hat in His Size{/color}{/size}\n\n{i}The end.{/i}"
    else:
        centered "{size=+10}{color=#f3c969}A Custard Cream on the Collar{/color}{/size}\n\n{i}The end.{/i}"
    jump start
