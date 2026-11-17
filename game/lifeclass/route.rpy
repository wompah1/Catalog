## Life Class -- "Whatever the Life Class Draws, I Turn Into, and the Chest Study Didn't Take"
## (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the
## owner). From catalog/game/02-engine/storylines/lifeclass/ (lifeclass.js: the rungs, the calls,
## the lines; main.twee, rungs.twee, rungs-late.twee), kept verbatim in
## catalog/docs/routes/vn-original/lifeclass/.
##
## THE NON-CON PASS (owner, 2026-10-19/20: escalating corruption). The drawing is the violation:
## at every growth beat in rungs 1-4 Gino yells at the room to stop drawing while the body changes
## anyway. Rungs 1-2 never flip; rung 3 flips mid-Bjorn ("Fine. FINE."); rung 4, Aurelio, flips on
## "Don't you DARE stop, I'm not LEAVING!". From rung 5's "Come get me" it's consensual. Rung 4's
## offer is inverted: Dot puts the open call to the room, he begs her to close it, every hand goes
## up to keep him. The after-ending sessions are free play, not ported.
##
## Six linear days and an epilogue, one session a day (two till five); the night is vn_night.
## All route-local names carry lc_.
##
## PIN ONE BACK UP (an alternate route; owner, 2026-11-13 about 1:37 pm ET, signed off from c9's proposal): at the
## end of rung 4 a dropped chest sheet can go back up in the bare cork ("This choice decides your ending"), and the
## chest study takes late: small on rung 5's morning (lc.grown 1), medium-large from rung 5's back study (2), large
## and heavy as the show's swell takes the ass (row 6m), and the house cap, huge, from Dot's call at rung 6 (3) (the
## owner's ruling, 2026-11-15: alt tits lanes end at the cap). Its pictures are twins (art/lifeclass/<name>-ch.jpg, shown in place while lc.pinned)
## plus its own beats (lc_pin_*, pinned.rpy); its sprites are rows 5s, 5m, 6l. Alternate-route art is queued last.

init -10 python:
    LC = "art/lifeclass/"

    # THE LADDER: what Dot calls at the top of each session (setup.lifeclassCalls). Rung 4's fails.
    LC_CALLS = [None, "Value study, smooth forms.", "Gesture, hands and face.", "Master study, the seated figure.",
                "Chest study.", "The back, from life.", None]

    def lc_body(n):
        """The body takes rung n's row, toward it and never back."""
        lc.body = max(lc.body or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Rows: 0 Gino before the sink; 1-6 the rungs. Outfits: "own" (jeans and a white t-shirt, to
    # rung 2), "cloth" (rung 3's shirt and drop cloth), "sweats" (rungs 4-6), "nude" (the sessions).
    _lc_have = {}

    def _lc_has(n):
        if n not in _lc_have:
            _lc_have[n] = renpy.loadable(LC + n + ".png")
        return _lc_have[n]

    def lc_pc_file(face):
        r, fit = max(0, min(6, lc.body or 0)), lc.fit or "own"
        # Pin one back up: the grown chest's rows (5s, 5m, 6l) first, then the canon row's
        rows = (["%d%s" % (r, "sml"[min(3, lc.grown) - 1]), "%d" % r] if (lc.pinned and lc.grown) else ["%d" % r])
        names = []
        for k in rows:
            names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-apologetic" % (k, fit),
                      "pc-r%s-nude-%s" % (k, face), "pc-r%s-nude-apologetic" % k]
        for n in names:
            if _lc_has(n):
                return LC + n + ".png"
        return LC + names[-1] + ".png"

    def lc_face_now():
        a = renpy.get_attributes("lc_pc")
        return a[0] if a else "apologetic"

    def _lc_portrait(st, at):
        p = vn_art_file(lc_pc_file(lc_face_now()))
        crops = globals().get("lifeclass_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["lifeclass"] = lambda: DynamicDisplayable(_lc_portrait)

    # The calendar: a session a day, six days running, the prose naming no weekday (the schedule is
    # "the next session"); day 1 is a Monday, the epilogue the Sunday.
    LC_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def lc_weekday_name():
        return LC_WD[(1 + vn_clock.day - 1) % 7]    # day 1 is a Monday

    vn_weekdays["lifeclass"] = lc_weekday_name

    vn_sprite_image("lc_pc", ("apologetic", "protesting", "flushed", "wanting"), lc_pc_file, who="pc")
    for _w, _faces in (("dot", ("crit", "flat", "watch")), ("dario", ("drawing", "hungry", "smug")),
                       ("roz", ("swearing", "pleased", "fierce")), ("aurelio", ("intent", "still", "hungry")),
                       ("winnie", ("late", "laughing")), ("bjorn", ("practical", "nod")),
                       ("tamsin", ("laughing", "dusty")), ("milo", ("keen", "grin"))):
        vn_sprite_image("lc_" + _w, _faces, (lambda w: (lambda f: LC + w + "-" + f + ".png"))(_w))

    # Pin one back up's twin of a picture: <name>-ch.jpg, shown in its place while lc.pinned (the hypno full
    # regimen's way). A picture with no twin is the same on both.
    _lc_twin = {}

    def _lc_ch_of(path):
        if not lc.pinned:
            return path
        if path not in _lc_twin:
            t = path[:-4] + "-ch.jpg"
            _lc_twin[path] = t if renpy.loadable(t) else None
        return _lc_twin[path] or path

    def _lc_cg_dd(st, at, path):
        return vn_cg(vn_art_file(_lc_ch_of(path))), None

    def _lc_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_lc_ch_of(path))), None

    for _f in renpy.list_files():
        if _f.startswith(LC) and _f.endswith(".jpg"):
            _n = _f[len(LC):-4]
            if _n.endswith("-ch"):
                continue
            _k = "lc_" + _n.replace("-", "_")
            vn_cg_files[_k] = _f
            renpy.image(("cg", _k), DynamicDisplayable(_lc_cg_dd, _f))
            renpy.image(("bg", _k), DynamicDisplayable(_lc_bg_dd, _f))

    vn_register_art_sets("lifeclass", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("lifeclass", "Whatever the Life Class Draws, I Turn Into, and the Chest Study Didn't Take",
        "A sheet of A4 by the café's side door on Cliff Street: LIFE MODEL WANTED. OPEN CALL. CASH. You go up because it's cash for sitting still. Every session the instructor calls a region, the whole class draws it, and by the end of the session you match it. Nobody in the building ever mentions this. And one of them draws the same thing every single time, whatever the assignment is.",
        LC + "cover.jpg", "lifeclass_start")

    achievement.register("The Only Sheet Without a Red Dot")
    achievement.register("The Chest Study Took")

default lc = VNState(body=0, fit="own", pinned=False, grown=0)
default lc_enc = VNState(partner_came=True, pc_orgasms=0)
default lc_pc_name = "Gino"

define lc_you = VNChar("[lc_pc_name]", who="pc", plate="#7a5230")
define lc_dot = VNChar("Dot", who="lc_dot", plate="#5a6b7a")
define lc_dario = VNChar("Dario", who="lc_dario", plate="#3a3a3a")
define lc_roz = VNChar("Roz", who="lc_roz", plate="#2b2b2b")
define lc_aurelio = VNChar("Aurelio", who="lc_aurelio", plate="#8a7f72")
define lc_winnie = VNChar("Winnie", who="lc_winnie", plate="#b0567a")
define lc_bjorn = VNChar("Bjorn", who="lc_bjorn", plate="#5f7f4f")
define lc_tamsin = VNChar("Tamsin", who="lc_tamsin", plate="#b58fd0")
define lc_milo = VNChar("Milo", who="lc_milo", plate="#4f8fb0")
define lc_voice = VNChar("Someone at the back", who="class", plate="#6b6b78")

## The schedule sheet on the frosted door, and the flyer: drawn by Ren'Py (no lettering in the art).
screen lc_sheet(lines):
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 720
        padding (30, 22)
        background Frame(Solid("#f6f3ecf2"), 0, 0)
        vbox:
            spacing 8
            for t in lines:
                text t size 24 color "#2a2a2a"

## Dot's call at the top of a session, as a plate.
init python:
    def lc_call(n):
        return "{color=#f3c969}{b}“%s”{/b}{/color}" % LC_CALLS[n]

label lifeclass_start:
    $ lc = VNState(body=0, fit="own", pinned=False, grown=0)
    $ lc_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=9, minute=0)
    $ vn_route = "lifeclass"
    $ lc_pc_name = "Gino"
    if not renpy.session.get("vn_picks"):
        $ lc_pc_name = renpy.input("Your name? (Gino, unless you'd like another.)", default="Gino", length=20).strip() or "Gino"
    jump lc_opening

label lc_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"lifeclass"}
    $ vn_route = None
    hide screen lc_sheet
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}The Only Sheet Without a Red Dot{/color}{/size}\n\n{i}The end.{/i}"
    jump start
