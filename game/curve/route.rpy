## Curve -- "The Compound Only Binds During Orgasm" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md
## beside this file, signed off by the owner). From the package Curve (TheStoryNexusTauriApp/packages/sent/
## curve-package.md), kept verbatim in catalog/docs/routes/vn-original/curve/.
##
## THE PASS, "It has to bind" (owner, 2026-11-12, as signed off): the package's coercion from the first page to
## the last, no consent flip. Cal's mode goes protest, negotiate, submit, beg, anticipate, need; his initiating
## in ch 4-5 is a reaction, never a decision. Ch 1 the first dose is the first incident. House rules: no pain
## (the withdrawal is emptiness, restlessness, an arousal that won't resolve), no tears, Greer never raises
## her voice; the folder stays in her desk, invoked flat to the end. He gets smarter, never dumb.
##
## The package's rules kept: the compound never explained; anal and oral only until the back half of ch 6;
## the cock removed gradually across ch 6, on the page; the probe "What are you carrying?" every chapter,
## "Yours." last; never assert a mind change in narration. Strawberry-blonde hair (the owner's pick).
## he/him to ch 4, she/her from ch 5. All route-local names carry crv_.

init -10 python:
    CRV = "art/curve/"

    CRV_ROWS = ["1", "2", "3", "4", "5", "6"]

    def crv_body(row):
        row = str(row)
        if CRV_ROWS.index(row) > CRV_ROWS.index(crv.row or "1"):
            crv.row = row

    # THE BOARD: Greer's whiteboard. n rows crossed off; from ch 5 the undated rows in another pen.
    CRV_BOARD_ROWS = ["Compliance", "Regimen: sleep / diet / wdrb.", "Presentation; roster amd.", "Retention trial",
                      "Integument", "Vocal; manual", "Taper (clean baseline)", "Escalation", "Dosage escl. II",
                      "Supply", "Removal"]
    CRV_UNDATED = ["soft", "Nadia — no", "keeps the sweater", "cock"]

    CRV_PROBE = {
        1: "\"What are you carrying?\"  \"Fifteen. Why?\"",
        2: "\"What are you carrying?\"  \"Fifteen. And the Tuesday-Thursday dose, and the Sunday double.\"",
        3: "\"What are you carrying?\"  \"Thursday's dose. And, uh. Fifteen.\"",
        4: "\"What are you carrying?\"  \"I'm... carrying. I was going to say. What was the—\"",
        5: "\"What are you carrying?\"  \"Twice tonight. Once before the exam.\"",
        6: "\"What are you carrying?\"  \"Yours.\"",
    }

    _crv_have = {}

    def _crv_has(n):
        if n not in _crv_have:
            _crv_have[n] = renpy.loadable(CRV + n + ".png")
        return _crv_have[n]

    CRV_FACES = ("flat", "flustered", "dazed", "begging", "glowing")

    def crv_pc_file(face):
        """The PC sprite for this row, fit and face; a face the row hasn't got falls back to another face in the
        same fit before it ever reaches nude (QA 3cde2d8e: pc-r2-regimen-flat was pulled for a glasses bridge, and
        the old list sent its lines to pc-r2-nude-flat)."""
        r = crv.row or "1"
        fit = crv.fit or "hoodie"
        faces = (face,) + tuple(f for f in CRV_FACES if f != face)
        names = ["pc-r%s-%s-%s" % (r, fit, f) for f in faces] + ["pc-r%s-nude-%s" % (r, f) for f in faces]
        for n in names:
            if _crv_has(n):
                return CRV + n + ".png"
        return CRV + names[-1] + ".png"

    def crv_face_now():
        a = renpy.get_attributes("crv_pc")
        return a[0] if a else "flat"

    def _crv_portrait(st, at):
        p = vn_art_file(crv_pc_file(crv_face_now()))
        crops = globals().get("curve_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["curve"] = lambda: DynamicDisplayable(_crv_portrait)

    vn_sprite_image("crv_pc", ("flat", "flustered", "begging", "dazed", "glowing"), crv_pc_file, who="pc")
    for _w, _faces in (("greer", ("clinical", "warm", "jealous")), ("nadia", ("bright",)), ("kwan", ("kind",))):
        vn_sprite_image("crv_" + _w, _faces, (lambda w: (lambda f: CRV + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(CRV) and _f.endswith(".jpg"):
            _n = _f[len(CRV):-4]
            vn_register_bg("crv_" + _n.replace("-", "_"), _f)
            vn_register_cg("crv_" + _n.replace("-", "_"), _f)

    vn_register_route("curve", "The Compound Only Binds During Orgasm",
        "You copied your lab set off Greer Halloway, which is why she's the one holding the proof, in an empty teaching lab at nine at night. She isn't going to file it. She has a grant that needs you enrolled, a compound that needs a subject, and a whiteboard with your name at the top.",
        CRV + "cover.jpg", "curve_start")

    achievement.register("Full Marks")

default crv = VNState(row="1", fit="hoodie", chapter=0, term=None, dean=None, rows=None, ending=None)
default crv_pc_name = "Cal"

define crv_you = VNChar("[crv_pc_name]", who="pc", plate="#c0705a")
define crv_greer = VNChar("Greer", who="crv_greer", plate="#2a3a3a")
define crv_nadia = VNChar("Nadia", who="crv_nadia", plate="#7a4a2a")
define crv_kwan = VNChar("Ms Kwan", who="crv_kwan", plate="#4a4a5a")

## THE BOARD: crossed rows struck through; the undated rows from ch 5 in red marker.
screen crv_board(n, undated=False):
    zorder 60
    frame:
        xalign 0.5 ypos 40
        padding (30, 18)
        background Frame(Solid("#f4f6f4f2"), 0, 0)
        vbox:
            spacing 4
            text "BOYD, C." size 24 color "#1a1a1a" bold True
            text "Subject's academic underperformance is a function of male cognition. Intervention: removal." size 19 color "#1a1a1a" italic True
            for _i, _r in enumerate(CRV_BOARD_ROWS):
                text (("{s}" + _r + "{/s}") if _i < n else _r) size 20 color "#1a3a6a"
            if undated:
                for _u in CRV_UNDATED:
                    text ("· " + _u) size 20 color "#b02a2a"

## THE PROBE.
screen crv_probe(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 20)
        background Frame(Solid("#121820f0"), 0, 0)
        text CRV_PROBE[n] size 28 color "#e8e4dc"

label curve_start:
    $ crv = VNState(row="1", fit="hoodie", chapter=0, term=None, dean=None, rows=None, ending=None)
    $ vn_clock = VNState(day=1, hour=21, minute=0)
    $ vn_route = "curve"
    $ crv_pc_name = "Cal"
    jump crv_ch1

label crv_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"curve"}
    $ vn_route = None
    hide screen crv_board
    hide screen crv_probe
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e89a8a}Full Marks{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _crv_trace():
        pc = crv_pc_file(crv_face_now()).rsplit("/", 1)[-1] if renpy.showing("crv_pc") else None
        cast = None
        for _t in ("crv_greer", "crv_nadia", "crv_kwan"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, crv.fit

    vn_trace_routes["curve"] = _crv_trace
