## Boytoy -- "I Went Undercover in the Pervert Tower, Lost to Every Floor Boss, and Climbed Anyway"
## (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the
## owner). From catalog/game/02-engine/storylines/boytoy/ (boytoy.js: the floors, the kits, the
## keepers' lines, the pools; main.twee, rungs.twee, rungs-late.twee, ending.twee), kept verbatim in
## catalog/docs/routes/vn-original/boytoy/.
##
## THE NON-CON PASS (owner, 2026-10-27, as packaged: resist-then-break, the break at rung 5). Rungs
## 1-4 non-con, no flip: he says no in words, in his hero voice, and his body betrays him; rung 5
## opens non-con and breaks halfway ("Don't stop. Don't— don't you dare stop—"); rung 6 consensual
## and eager. Partners never ask; pinning and holding are fine; no blows land, nobody lifts him off
## his feet, nobody threatens, nobody stops him leaving (the climb is the only leverage).
##
## Femboy, the cock kept (small, never "tiny"), never a pussy; he/him to the last line. No heights
## and no size set against a partner's. Six weeks, a floor a week; the Cage's staff door after the
## ending (Stay's weekly menu) is free play, not ported. All route-local names carry boy_.

init -10 python:
    BOY = "art/boytoy/"

    # THE FLOORS: the lift button, the floor, its keeper, and this week's field report (the lift
    # panel's caption).
    BOY_FLOORS = [None,
        dict(button="G", floor="the door", keeper="Gideon", report="Going in."),
        dict(button="1", floor="the bar", keeper="Soren", report="Cleared. And again. And again."),
        dict(button="2", floor="the dressing room", keeper="Cordelia", report="Deleted, then cleared."),
        dict(button="3", floor="the stage", keeper="Caspian", report="Whispered, and kept."),
        dict(button="4", floor="the VIP floor", keeper="Ulric", report="They clapped. Not sent."),
        dict(button="P", floor="the penthouse", keeper="Dorian", report="No report."),
    ]
    BOY_BUTTONS = ["G", "1", "2", "3", "4", "P"]

    def boy_body(n):
        """The body takes rung n's row, toward it and never back."""
        boy.row = str(max(int(boy.row or 0), n))

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "hood" (Bantam: the red hoodie, cargo trousers, combat boots, the black domino mask),
    # "own" (his own clothes, the bedsit and the kiosk), "k1" (the tight black vest, black shorts,
    # the RECRUIT choker), "k2" (the cropped black waistcoat, gold hot pants), "k3" (the black corset
    # with gold lacing, stockings and suspenders, lace knickers, heels), "k4" (the sheer gold showgirl
    # leotard, the feather tail, gold heels, the stockings; "k4m" with the mask on, from the act),
    # "k5" (the gold micro-bikini,
    # the sheer black robe, gold heels, the mask), "k6m" (the choker, black stockings and the mask),
    # "k6" (the choker and stockings, the mask in the birdcage), "nude". The choker from rung 1 on.
    _boy_have = {}

    def _boy_has(n):
        if n not in _boy_have:
            _boy_have[n] = renpy.loadable(BOY + n + ".png")
        return _boy_have[n]

    def boy_pc_file(face):
        r, fit = boy.row or "0", boy.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-heroic" % (r, fit),
                 "pc-r%s-own-%s" % (r, face), "pc-r%s-own-heroic" % r]
        for n in names:
            if _boy_has(n):
                return BOY + n + ".png"
        # ff 2:49 am 11-18: no sprite for this outfit at this row (bedsit three/four/six), so the same
        # outfit at the nearest lower row, then (clothed only; nude stays nude) another outfit; never
        # a file that is missing. The cock stays on every row, so a lower nude row is safe.
        fits = (fit,) if fit == "nude" else (fit, "own", "hood", "k1", "k2", "k3", "k4", "k4m", "k5", "k6", "k6m")
        faces = (face, "heroic", "flushed", "outraged", "begging")
        for f in fits:
            for rr in range(int(r), -1, -1):
                for fc in faces:
                    n = "pc-r%d-%s-%s" % (rr, f, fc)
                    if _boy_has(n):
                        return BOY + n + ".png"
        return BOY + names[-1] + ".png"

    def boy_face_now():
        a = renpy.get_attributes("boy_pc")
        return a[0] if a else "heroic"

    def _boy_portrait(st, at):
        p = vn_art_file(boy_pc_file(boy_face_now()))
        crops = globals().get("boytoy_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["boytoy"] = lambda: DynamicDisplayable(_boy_portrait)

    # The calendar: day 1 is a Sunday (the rooftop, nearly midnight); then a floor a week, Monday's
    # report, the week's shifts, Friday's scuffle; the epilogue a Tuesday.
    BOY_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def boy_weekday_name():
        return BOY_WD[(vn_clock.day - 1) % 7]    # day 1 is a Sunday

    def boy_to_weekday(wd, h=9):
        """Minutes from now to the next weekday wd (0 Sunday) at hour h, at least a day on."""
        cur = (vn_clock.day - 1) % 7
        days = (wd - cur) % 7 or 7
        return days * 24 * 60 + (h - vn_clock.hour) * 60 - vn_clock.minute

    vn_weekdays["boytoy"] = boy_weekday_name

    vn_sprite_image("boy_pc", ("heroic", "outraged", "flushed", "begging"), boy_pc_file, who="pc")
    for _w, _faces in (("gideon", ("blank", "mm")), ("soren", ("grin", "smooth")), ("cordelia", ("brisk", "delighted")),
                       ("caspian", ("showman", "grin")), ("ulric", ("polite", "warm")), ("dorian", ("lazy", "warm"))):
        vn_sprite_image("boy_" + _w, _faces, (lambda w: (lambda f: BOY + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(BOY) and _f.endswith(".jpg"):
            _n = _f[len(BOY):-4]
            vn_register_bg("boy_" + _n.replace("-", "_"), _f)
            vn_register_cg("boy_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("boytoy", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("boytoy", "I Went Undercover in the Pervert Tower, Lost to Every Floor Boss, and Climbed Anyway",
        "The town has a masked vigilante, Bantam: a red hood, a black domino mask, very fast hands, and he has never lost a fight. Men keep going missing into the Gilded Cage, a black-brick club tower on the docks with a keeper on every floor. So Bantam goes in undercover as a recruit. The card says beat the keeper and take the key. Lose, and go up anyway.",
        BOY + "cover.jpg", "boytoy_start")

    achievement.register("Bantam Loses")

default boy = VNState(row="0", fit="hood")
default boy_pc_name = "Jago"

define boy_you = VNChar("[boy_pc_name]", who="pc", plate="#a02a2a")
define boy_gideon = VNChar("Gideon", who="boy_gideon", plate="#2a2a2a")
define boy_soren = VNChar("Soren", who="boy_soren", plate="#b8923a")
define boy_cordelia = VNChar("Cordelia", who="boy_cordelia", plate="#9a1a2a")
define boy_caspian = VNChar("Caspian", who="boy_caspian", plate="#c8a02a")
define boy_ulric = VNChar("Ulric", who="boy_ulric", plate="#3a3a4a")
define boy_dorian = VNChar("Dorian", who="boy_dorian", plate="#5a4a3a")
define boy_voice = VNChar("The intercom", who="intercom", plate="#6b6b78")
define boy_other = VNChar("Somebody", who="other", plate="#6b6b78")

## THE LIFT PANEL: six brass buttons, G 1 2 3 4 P, the lit ones gold, never a count; this week's
## field report as its caption.
screen boy_lift(n):
    zorder 60
    $ _r = max(1, min(6, n))
    frame:
        xalign 0.5 ypos 60
        padding (30, 20)
        background Frame(Solid("#1a140cf0"), 0, 0)
        vbox:
            spacing 12
            hbox:
                spacing 18
                xalign 0.5
                for _i, _b in enumerate(BOY_BUTTONS):
                    frame:
                        xysize (64, 64)
                        background Frame(Solid("#e8c35a" if _i < _r else "#3a2e1a"), 0, 0)
                        text _b size 30 color ("#2a1a00" if _i < _r else "#b8923a") xalign 0.5 yalign 0.5
            text "{i}%s{/i}" % BOY_FLOORS[_r]["report"] size 22 color "#e8c35a" xalign 0.5

## A card or a page: the recruit's card, Staff vitamins, the VIP menu's Specials, the paper.
screen boy_card(title, lines):
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 680
        padding (30, 22)
        background Frame(Solid("#f5ecd6f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}%s{/b}" % title size 24 color "#6a4a10"
            for _l in lines:
                text _l size 22 color "#2a2a2a"

label boytoy_start:
    $ boy = VNState(row="0", fit="hood")
    $ vn_clock = VNState(day=1, hour=23, minute=45)
    $ vn_route = "boytoy"
    $ boy_pc_name = "Jago"
    if not renpy.session.get("vn_picks"):
        $ boy_pc_name = renpy.input("Your name? (Jago, unless you'd like another. You're Penhallow either way, and Bantam after midnight.)", default="Jago", length=20).strip() or "Jago"
    jump boy_rooftop

label boy_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"boytoy"}
    $ vn_route = None
    hide screen boy_lift
    hide screen boy_card
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}Bantam Loses{/color}{/size}\n\n{i}The end.{/i}"
    jump start
