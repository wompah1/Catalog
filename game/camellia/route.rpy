## Camellia -- "Worst Host on the Men's Floor" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside
## this file, signed off by the owner). From the shelf book 27f2ad62, Number One Girl, kept verbatim in
## catalog/docs/routes/vn-original/camellia/.
##
## THE NON-CON PASS, "Uniform" (owner, 2026-11-12, as signed off): Kurosawa's floor rules and the rig itself.
## Nobody threatens and nobody hurts; they just don't stop when Rina says no. Ch 1 the first incident
## (Kurosawa rigs him, then puts him on his knees); ch 2 forced (Miyamoto's dohan ends in a love hotel;
## Kurosawa fits the cage as uniform and takes her over the dressing table); ch 3 the flip at the book's own
## "If it's a cage, lock it"; ch 4-5 consensual. The book's consensual Domoto scenes of ch 1-2 move to ch 4.
## No tears, no menace, no pain, no escape.
##
## No organic change at any point (Fem): the rig is the ladder. Rows: "0" Ryo in his host suit; "1" Rina in
## the rig, uncaged; "3" Rina caged (from ch 2). The wig is the book's red, in two long low tails, never high
## twintails (the book's "clipped high" read young). The ending is marked: Sign (the book's) or Take (new).
## All route-local names carry cam_.
##
## MAKE IT REAL (an alternate route; owner, 2026-11-13 about 1:37 pm ET, signed off from c9's proposal; real.rpy): at
## ch 3's office Rina can ask Kurosawa to make it so nobody can poach her ("This choice decides your ending"): the
## doctor on the fourth floor, HRT, slow. cam.grown 1 (budding under the forms by ranking night, six weeks on; sprites
## 3r), 2 (a contract year on, large; 3y). Twins art/camellia/<name>-r.jpg, shown in place while cam.real. Alt art last.

init -10 python:
    CAM = "art/camellia/"

    # MAKE IT REAL opens once its art has landed (its 3r/3y sprites; nqalt/130): until then ch 3 offers only
    # the canon choice, so nobody plays the lane on flat r3 sprites (QA 2f90ff35)
    CAM_REAL_READY = any(f.startswith(CAM + "pc-r3r-") for f in renpy.list_files())

    CAM_ROWS = ["0", "1", "3"]

    def cam_body(row):
        row = str(row)
        if CAM_ROWS.index(row) > CAM_ROWS.index(cam.row or "0"):
            cam.row = row

    # THE BOARD: the rankings, one line a night.
    CAM_BOARD = {
        1: "MEN'S FLOOR, this month: ... 11. Kitahara. 12. RYO.",
        2: "WOMEN'S FLOOR: 1. Saki. ... 9. RINA (new).",
        3: "WOMEN'S FLOOR: 1. Saki. 2. RINA.",
        4: "WOMEN'S FLOOR: 1. RINA. 2. Saki.",
        5: "WOMEN'S FLOOR: 1. RINA. In Kurosawa's hand, underneath: one year.",
        6: "SANCTUARY, MEN'S FLOOR: 1. RYO.",
    }

    _cam_have = {}

    def _cam_has(n):
        if n not in _cam_have:
            _cam_have[n] = renpy.loadable(CAM + n + ".png")
        return _cam_have[n]

    def cam_pc_file(face):
        r = cam.row or "0"
        fit = cam.fit or "suit"
        # Make it real: the grown chest's rows (3r, 3y) first, then the canon row's
        rows = [r + ("r" if cam.grown == 1 else "y"), r] if (cam.real and cam.grown) else [r]
        names = []
        for k in rows:
            names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-poised" % (k, fit), "pc-r%s-rig-%s" % (k, face), "pc-r%s-rig-poised" % k]
        names += ["pc-r0-suit-poised"]
        for n in names:
            if _cam_has(n):
                return CAM + n + ".png"
        return CAM + names[0] + ".png"

    def cam_face_now():
        a = renpy.get_attributes("cam_pc")
        return a[0] if a else "poised"

    def _cam_portrait(st, at):
        p = vn_art_file(cam_pc_file(cam_face_now()))
        crops = globals().get("camellia_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["camellia"] = lambda: DynamicDisplayable(_cam_portrait)

    vn_sprite_image("cam_pc", ("poised", "mortified", "flushed", "begging", "bright"), cam_pc_file, who="pc")
    for _w, _faces in (("kurosawa", ("cool", "smoke", "raw")), ("saki", ("sly", "sour")), ("domoto", ("hungry",)),
                       ("miyamoto", ("leer",)), ("ichinose", ("easy",))):
        vn_sprite_image("cam_" + _w, _faces, (lambda w: (lambda f: CAM + w + "-" + f + ".png"))(_w))

    # Make it real's twin of a picture: <name>-r.jpg, shown in its place while cam.real (the hypno full regimen's way).
    _cam_twin = {}

    def _cam_r_of(path):
        if not cam.real:
            return path
        if path not in _cam_twin:
            t = path[:-4] + "-r.jpg"
            _cam_twin[path] = t if renpy.loadable(t) else None
        return _cam_twin[path] or path

    def _cam_cg_dd(st, at, path):
        return vn_cg(vn_art_file(_cam_r_of(path))), None

    def _cam_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_cam_r_of(path))), None

    for _f in renpy.list_files():
        if _f.startswith(CAM) and _f.endswith(".jpg"):
            _n = _f[len(CAM):-4]
            if _n.endswith("-r"):
                continue
            _k = "cam_" + _n.replace("-", "_")
            vn_cg_files[_k] = _f
            renpy.image(("cg", _k), DynamicDisplayable(_cam_cg_dd, _f))
            renpy.image(("bg", _k), DynamicDisplayable(_cam_bg_dd, _f))

    vn_register_route("camellia", "Worst Host on the Men's Floor",
        "Eleven months at the bottom of the Camellia's men's board, and a week from being cut. The manager has another idea: the women's floor, the rig, and a new name on the other board. You are, immediately and humiliatingly, good at it.",
        CAM + "cover.jpg", "camellia_start")

    achievement.register("Number One Girl")
    achievement.register("Nobody Again")
    achievement.register("Made Real")

default cam = VNState(row="0", fit="suit", chapter=0, order=None, toast=None, domoto=None, ending=None, asked=False, real=False, grown=0)
default cam_pc_name = "Ryo"

define cam_you = VNChar("[cam_pc_name]", who="pc", plate="#b02a3a")
define cam_kuro = VNChar("Kurosawa", who="cam_kurosawa", plate="#202024")
define cam_saki = VNChar("Saki", who="cam_saki", plate="#5a2a5a")
define cam_domoto = VNChar("Domoto", who="cam_domoto", plate="#2a3a5a")
define cam_miya = VNChar("Miyamoto", who="cam_miyamoto", plate="#5a5a3a")
define cam_ichi = VNChar("Ichinose", who="cam_ichinose", plate="#3a5a5a")
define cam_host = VNChar("Takumi", who="host", plate="#6b6b78")

## THE BOARD.
screen cam_board(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 20)
        background Frame(Solid("#120c10f2"), 0, 0)
        text CAM_BOARD[n] size 26 color "#f2d6dc"

label camellia_start:
    $ cam = VNState(row="0", fit="suit", chapter=0, order=None, toast=None, domoto=None, ending=None, asked=False, real=False, grown=0)
    $ vn_clock = VNState(day=1, hour=22, minute=0)
    $ vn_route = "camellia"
    $ cam_pc_name = "Ryo"
    jump cam_ch1

label cam_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"camellia"}
    $ vn_route = None
    hide screen cam_board
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    if cam.ending == "sign":
        centered "{size=+10}{color=#e86a7a}Number One Girl{/color}{/size}\n\n{i}The end.{/i}"
    else:
        centered "{size=+10}{color=#e86a7a}Nobody Again{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _cam_trace():
        pc = cam_pc_file(cam_face_now()).rsplit("/", 1)[-1] if renpy.showing("cam_pc") else None
        cast = None
        for _t in ("cam_kurosawa", "cam_saki", "cam_domoto", "cam_miyamoto", "cam_ichinose"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, cam.fit

    vn_trace_routes["camellia"] = _cam_trace
