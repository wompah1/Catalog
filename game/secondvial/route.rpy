## Secondvial -- "The Rule Was One Vial a Day. He Supplies the Second." (rewritten straight in Ren'Py, 2026-11-12;
## the plan is PLAN.md beside this file, signed off by the owner). From the shelf book 27fcc314, The Second Vial,
## kept verbatim in catalog/docs/routes/vn-original/secondvial/.
##
## THE NON-CON PASS, "Paid before opening" (owner, 2026-11-12, as signed off): the arrangement and the vials'
## heat. Caddic states the terms ONCE, flat as a ledger line, and never threatens, never raises his voice;
## he and the tasting customers never ask and carry on past Wren's no. Ch 3 the first incident; forced
## through ch 5; ch 6 he breaks into begging; ch 7 alone; ch 8 the flip (he drinks the third vial himself,
## gleeful); ch 8-10 consensual and gleeful, in the doujin register. No tears, no menace, no pain (the book's
## "agony" is heat and too much sensation here), no escape; Wren protests out loud, never in silence.
##
## Two bodies (rows): the dawn body, what the reversal leaves ("0" Wren a man; "d1" soft, the hips that stay;
## "d2" breasts that stay; "d3" neither shape, bound and leaking), and the night body on the vials ("n1" one
## vial, plain and flat; "n2" two vials; "n3" two months; "n4" after the residue; "n5" the third vial, no
## reversal ever again: the house's largest step, "huge, weighted up", the cap). svl_body() sets the row each
## time he drinks or dawn takes him back. Ash-pink hair on the night body (the owner's pick); his own is
## straw-blonde. The ending's name, Serah, is the book's. All route-local names carry svl_.

init -10 python:
    SVL = "art/secondvial/"

    SVL_ROWS = ["0", "d1", "d2", "d3", "n1", "n2", "n3", "n4", "n5"]

    def svl_body(row):
        """The body in force: the night row when he's drunk the vials, the dawn row when the reversal takes him back."""
        svl.row = str(row)

    # THE PURSE: the coin count every night, in words.
    SVL_PURSE = {
        1: "The purse: one copper, picked off the floor. Rent is three silver by the week's end.",
        2: "The purse: a handful of copper. Mira's would buy his whole week.",
        4: "The purse: two coppers, Caddic's \"wage\". The tips went in the ledger.",
        5: "The purse: two coppers. The ledger: a column of silver, held in trust.",
        8: "The purse: he's stopped counting it. The ledger is three pages.",
        10: "The purse: the house's strongbox. Her key.",
    }

    _svl_have = {}

    def _svl_has(n):
        if n not in _svl_have:
            _svl_have[n] = renpy.loadable(SVL + n + ".png")
        return _svl_have[n]

    SVL_FACES = ("guarded", "flushed", "begging", "dazed", "gleeful")
    SVL_FITS = ("rags", "barmaid", "apron", "velvet", "nude")

    def svl_pc_file(face):
        """The PC sprite for this row, fit and face. Not every row has every fit and face, so fall back to a file
        that exists: the same fit with another face, then the same fit a row or more down its own branch (night rows
        n, dawn rows d, then 0), then another fit in this row (nude last), then anything lower. Never a missing
        file (QA 2e55d613: the old list ended on pc-r*-nude-guarded, which no row has)."""
        r = svl.row or "0"
        fit = svl.fit or "rags"
        faces = (face,) + tuple(f for f in SVL_FACES if f != face)
        branch = [x for x in SVL_ROWS if x == "0" or (r != "0" and x[0] == r[0])]
        down = list(reversed(branch[:branch.index(r) + 1])) if r in branch else [r, "0"]
        others = [f for f in SVL_FITS if f != fit]
        names = ["pc-r%s-%s-%s" % (r, fit, f) for f in faces]
        names += ["pc-r%s-%s-%s" % (x, fit, f) for x in down[1:] for f in faces]
        names += ["pc-r%s-%s-%s" % (x, o, f) for x in down for o in others for f in faces]
        for n in names:
            if _svl_has(n):
                return SVL + n + ".png"
        return SVL + names[0] + ".png"

    def svl_face_now():
        a = renpy.get_attributes("svl_pc")
        return a[0] if a else "guarded"

    def _svl_portrait(st, at):
        p = vn_art_file(svl_pc_file(svl_face_now()))
        crops = globals().get("secondvial_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["secondvial"] = lambda: DynamicDisplayable(_svl_portrait)

    vn_sprite_image("svl_pc", ("guarded", "flushed", "begging", "dazed", "gleeful"), svl_pc_file, who="pc")
    for _w, _faces in (("caddic", ("flat", "pleased")), ("mira", ("wry",)), ("sabine", ("sly", "warm")),
                       ("brusk", ("leer",)), ("alchemist", ("hard",))):
        vn_sprite_image("svl_" + _w, _faces, (lambda w: (lambda f: SVL + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(SVL) and _f.endswith(".jpg"):
            _n = _f[len(SVL):-4]
            vn_register_bg("svl_" + _n.replace("-", "_"), _f)
            vn_register_cg("svl_" + _n.replace("-", "_"), _f)

    vn_register_route("secondvial", "The Rule Was One Vial a Day. He Supplies the Second.",
        "Barwork in this city is women's work, by guild charter, and you are a man with two coins and no papers. The alchemist's cheapest vial makes you a plain woman for a day: one a day, never more. The owner of the Bellhouse has other ideas, and a box of his own vials.",
        SVL + "cover.jpg", "secondvial_start")

    achievement.register("I Am the Contract")

default svl = VNState(row="0", fit="rags", chapter=0, brusk=None, supper=None, ask=None, dayoff=None, broke=False, asked=False, ending=None)
default svl_pc_name = "Wren"

define svl_you = VNChar("[svl_pc_name]", who="pc", plate="#b0708a")
define svl_caddic = VNChar("Caddic", who="svl_caddic", plate="#4a3a2a")
define svl_mira = VNChar("Mira", who="svl_mira", plate="#a03a2a")
define svl_sabine = VNChar("Sabine", who="svl_sabine", plate="#8a7a3a")
define svl_brusk = VNChar("Brusk", who="svl_brusk", plate="#5a4a3a")
define svl_alch = VNChar("The alchemist", who="svl_alchemist", plate="#2a4a3a")
define svl_man = VNChar("A customer", who="customer", plate="#6b6b78")

## THE PURSE.
screen svl_purse(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 20)
        background Frame(Solid("#2a2018f2"), 0, 0)
        text SVL_PURSE[n] size 26 color "#efe4cc"

label secondvial_start:
    $ svl = VNState(row="0", fit="rags", chapter=0, brusk=None, supper=None, ask=None, dayoff=None, broke=False, asked=False, ending=None)
    $ vn_clock = VNState(day=1, hour=8, minute=0)
    $ vn_route = "secondvial"
    $ svl_pc_name = "Wren"
    jump svl_ch1

label svl_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"secondvial"}
    $ vn_route = None
    hide screen svl_purse
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e8a8c0}I Am the Contract{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _svl_trace():
        pc = svl_pc_file(svl_face_now()).rsplit("/", 1)[-1] if renpy.showing("svl_pc") else None
        if pc and not _svl_has(pc[:-4]):
            pc = "MISSING " + pc
        cast = None
        for _t in ("svl_caddic", "svl_mira", "svl_sabine", "svl_brusk", "svl_alchemist"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, svl.fit

    vn_trace_routes["secondvial"] = _svl_trace
