## Lightsout -- "Sleepover Rules All Weekend, or the Photos Go Out" (rewritten straight in Ren'Py, 2026-11-12; the plan
## is PLAN.md beside this file, signed off by the owner). From the package Lights Out (TheStoryNexusTauriApp/packages/
## sent/lights-out-package.md), kept verbatim in catalog/docs/routes/vn-original/lightsout/.
##
## THE NON-CON PASS, "House rules" (owner, 2026-11-12, as signed off): the deal stated once, flat, by Dani, and never
## repeated as a threat. Ch 1 the first incident (Dani's titjob and the finish on his face; he protests out loud where
## the package had him frozen); ch 2 Jo fucks his mouth through the wax, forced, then the package's own turn: the wax
## is done and he stays on his knees (the break); ch 3 the flip, he steers the dares (the package's "arranges it");
## ch 3-6 consensual. The bluff revealed lightly on the doorstep (the SOURCES row). No tears, no menace, no pain, no
## escape. FEMBOY: the cock stays (caged ch 3 on, comes untouched in ch 6); all sex anal or oral, never vaginal; the
## chest padding in ch 2-4 and a small real handful from ch 5, small to the end; the ass and thighs big. Denial mode.
## Soft-peach hair (the owner's pick). All route-local names carry lto_.

init -10 python:
    LTO = "art/lightsout/"

    LTO_ROWS = ["0", "2", "3", "4", "5", "6"]

    def lto_body(row):
        row = str(row)
        if LTO_ROWS.index(row) > LTO_ROWS.index(lto.row or "0"):
            lto.row = row

    # MARISSA'S NOTEBOOK: never a number on screen.
    LTO_NOTES = {
        1: "Marissa's notebook. COLIN: measured against all four. Smallest. By a lot. Katie: 'for tomorrow'.",
        2: "Marissa's notebook. Waxed: everything. Hard all evening: yes. Touched: no.",
        3: "Marissa's notebook. Dares: never picks truth. Thinks he's subtle. Cage: on (Dani). Hips: bigger.",
        4: "Marissa's notebook. 4 a.m.: woke Jo himself. Ass: bigger. Katie screamed. Stuffed bra: still on.",
        5: "Marissa's notebook. Car park: he asked. Padding retired. A real handful. Katie screamed again.",
        6: "Marissa's notebook. Tapped out: Jo, Katie, Marissa, Dani. Tapped out: not Colin. Key: me.",
    }

    _lto_have = {}

    def _lto_has(n):
        if n not in _lto_have:
            _lto_have[n] = renpy.loadable(LTO + n + ".png")
        return _lto_have[n]

    def lto_pc_file(face):
        r = lto.row or "0"
        fit = lto.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-reasonable" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-reasonable" % r]
        for n in names:
            if _lto_has(n):
                return LTO + n + ".png"
        return LTO + names[-1] + ".png"

    def lto_face_now():
        a = renpy.get_attributes("lto_pc")
        return a[0] if a else "reasonable"

    def _lto_portrait(st, at):
        p = vn_art_file(lto_pc_file(lto_face_now()))
        crops = globals().get("lightsout_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["lightsout"] = lambda: DynamicDisplayable(_lto_portrait)

    vn_sprite_image("lto_pc", ("reasonable", "mortified", "flushed", "greedy", "smug"), lto_pc_file, who="pc")
    for _w, _faces in (("dani", ("calm",)), ("marissa", ("tease",)), ("jo", ("blunt",)), ("katie", ("squeal",))):
        vn_sprite_image("lto_" + _w, _faces, (lambda w: (lambda f: LTO + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(LTO) and _f.endswith(".jpg"):
            _n = _f[len(LTO):-4]
            vn_register_bg("lto_" + _n.replace("-", "_"), _f)
            vn_register_cg("lto_" + _n.replace("-", "_"), _f)

    vn_register_route("lightsout", "Sleepover Rules All Weekend, or the Photos Go Out",
        "Friday night, the ledge outside the house next door, because four women live in it and one of them never shuts her curtains. At 11:40 you fall in through the window. None of them are girls in the way you'd assumed.",
        LTO + "cover.jpg", "lightsout_start")

    achievement.register("Every Weekend")

default lto = VNState(row="0", fit="own", chapter=0, dare=None, woke=None, maam=None, ending=None, broke=False, asked=False)

define lto_you = VNChar("Colin", who="pc", plate="#e0a080")
define lto_dani = VNChar("Dani", who="lto_dani", plate="#2a2a3a")
define lto_marissa = VNChar("Marissa", who="lto_marissa", plate="#7a3a5a")
define lto_jo = VNChar("Jo", who="lto_jo", plate="#3a5a3a")
define lto_katie = VNChar("Katie", who="lto_katie", plate="#c06a9a")
define lto_guy = VNChar("A guy from your Tuesday lecture", who="guy", plate="#6b6b78")

## MARISSA'S NOTEBOOK.
screen lto_notes(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (30, 16)
        background Frame(Solid("#f6f0e4f2"), 0, 0)
        text LTO_NOTES[n] size 24 color "#2a1a2a"

label lightsout_start:
    $ lto = VNState(row="0", fit="own", chapter=0, dare=None, woke=None, maam=None, ending=None, broke=False, asked=False)
    $ vn_clock = VNState(day=1, hour=23, minute=40)
    $ vn_route = "lightsout"
    jump lto_ch1

label lto_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"lightsout"}
    $ vn_route = None
    hide screen lto_notes
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f0b090}Every Weekend{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _lto_trace():
        pc = lto_pc_file(lto_face_now()).rsplit("/", 1)[-1] if renpy.showing("lto_pc") else None
        cast = None
        for _t in ("lto_dani", "lto_marissa", "lto_jo", "lto_katie"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, lto.fit

    vn_trace_routes["lightsout"] = _lto_trace
