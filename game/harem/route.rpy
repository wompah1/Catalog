## Harem -- "I Hid in the Sultan's Harem to Keep My Balls, and Now the Sultan Keeps the Key" (rewritten straight in Ren'Py,
## 2026-11-13; the plan is PLAN.md beside this file, signed off by the owner). From the package (TheStoryNexusTauriApp/
## packages/not sent/fem/sultan-keeps-the-key-package.md; no book exists), kept verbatim in catalog/docs/routes/vn-original/harem/.
##
## THE NON-CON PASS, B (owner, 2026-11-13, as signed off): ch 1 forced (Zarina finds the only cock in the palace and rides it;
## he says no out loud because he can't be found; she never threatens, she just doesn't stop; his body betrays him, he ends
## begging). Ch 2-3 the package's gleeful rogue with the women. Ch 4 the sultan's first summons forced ("Kneel."; he protests,
## the sultan doesn't hear no; it breaks into begging). The caging stays as written, not sex. The flip at ch 5's bath: Dahlia
## brings Zarina and starts it. Ch 5-6 consensual. No tears, no menace, no pain, no escape; the shears never come out.
## SOFT TSF: the cock stays all book, smaller, caged from ch 4; never a pussy; from ch 3 he comes from his ass untouched.
## He and "Jory" to the end of ch 4; she and "Dahlia" from ch 5 (the plate turns). A made-up fairy-tale sultanate.
## Long black hair (the owner's pick). All route-local names carry hrm_.

init -10 python:
    HRM = "art/harem/"

    HRM_ROWS = ["0", "1", "2", "3", "4", "4c", "5", "6"]

    def hrm_body(row):
        row = str(row)
        if HRM_ROWS.index(row) > HRM_ROWS.index(hrm.row or "0"):
            hrm.row = row

    # MATRON DILARA'S BOOK: the rank, never a number.
    HRM_RANK = {
        1: "Matron Dilara's book.  The new girl: DAHLIA. Still being oiled. Inspection: later.",
        2: "Matron Dilara's book.  Dahlia: a DANCER. Veils, one coin belt. Good hips.",
        3: "Matron Dilara's book.  Dahlia: ZARINA'S HANDMAIDEN. Moves into Zarina's rooms.",
        4: "Matron Dilara's book.  Dahlia: a CONCUBINE. Sheer silks. Full inspection: Orhan.",
        5: "Matron Dilara's book.  Dahlia: THE SULTAN'S FAVOURITE. The favourite's jewels.",
        6: "Matron Dilara's book.  Dahlia: FIRST OF THE HAREM. A gold collar.",
    }

    _hrm_have = {}

    def _hrm_has(n):
        if n not in _hrm_have:
            _hrm_have[n] = renpy.loadable(HRM + n + ".png")
        return _hrm_have[n]

    def hrm_pc_file(face):
        r = hrm.row or "0"
        fit = hrm.fit or "shirt"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-grin" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-grin" % r]
        for n in names:
            if _hrm_has(n):
                return HRM + n + ".png"
        return HRM + names[-1] + ".png"

    def hrm_face_now():
        a = renpy.get_attributes("hrm_pc")
        return a[0] if a else "grin"

    def _hrm_portrait(st, at):
        p = vn_art_file(hrm_pc_file(hrm_face_now()))
        crops = globals().get("harem_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["harem"] = lambda: DynamicDisplayable(_hrm_portrait)

    vn_sprite_image("hrm_pc", ("grin", "startled", "flushed", "smug"), hrm_pc_file, who="pc")
    for _w, _faces in (("zarina", ("wicked",)), ("leyla", ("giggle",)), ("nasrin", ("lazy",)), ("dilara", ("brisk",)),
                       ("orhan", ("jolly",)), ("kasim", ("lazy",)), ("brask", ("earnest",))):
        vn_sprite_image("hrm_" + _w, _faces, (lambda w: (lambda f: HRM + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(HRM) and _f.endswith(".jpg"):
            _n = _f[len(HRM):-4]
            vn_register_bg("hrm_" + _n.replace("-", "_"), _f)
            vn_register_cg("hrm_" + _n.replace("-", "_"), _f)

    vn_register_route("harem", "I Hid in the Sultan's Harem to Keep My Balls, and Now the Sultan Keeps the Key",
        "Night over Marazhan, the Sultan's ruby in your fist and the palace guard on the rooftops behind you. You drop through a skylight into steam, and land in the harem.",
        HRM + "cover.jpg", "harem_start")

    achievement.register("The Sultan Keeps the Key")

default hrm = VNState(row="0", fit="shirt", chapter=0, shout1=None, hide2=None, dance=None, wave=None, fair=None, shout4=None, bet=None, ending=None, broke=False, broke4=False, asked=False, she=False, route1=None, greet=None, help1=None, danceat=None, plenty2=None, promise2=None, talk3=None, jade3=None, punish4=None, tease5=None, toast6=None, secret6=None)

define hrm_you = VNChar("Jory", who="pc", plate="#2a2a3a")
define hrm_dahlia = VNChar("Dahlia", who="pc", plate="#b0306a")
define hrm_zarina = VNChar("Zarina", who="hrm_zarina", plate="#6a1a3a")
define hrm_leyla = VNChar("Leyla", who="hrm_leyla", plate="#c07a9a")
define hrm_nasrin = VNChar("Nasrin", who="hrm_nasrin", plate="#7a5a2a")
define hrm_dilara = VNChar("Matron Dilara", who="hrm_dilara", plate="#5a4a3a")
define hrm_orhan = VNChar("Orhan", who="hrm_orhan", plate="#4a3a6a")
define hrm_kasim = VNChar("Sultan Kasim", who="hrm_kasim", plate="#8a6a1a")
define hrm_brask = VNChar("Captain Brask", who="hrm_brask", plate="#3a4a5a")

## MATRON DILARA'S BOOK.
screen hrm_rank(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (30, 16)
        background Frame(Solid("#f4ead2f2"), 0, 0)
        text HRM_RANK[n] size 25 color "#3a2410"

label harem_start:
    $ hrm = VNState(row="0", fit="shirt", chapter=0, shout1=None, hide2=None, dance=None, wave=None, fair=None, shout4=None, bet=None, ending=None, broke=False, broke4=False, asked=False, she=False, route1=None, greet=None, help1=None, danceat=None, plenty2=None, promise2=None, talk3=None, jade3=None, punish4=None, tease5=None, toast6=None, secret6=None)
    $ vn_clock = VNState(day=1, hour=23, minute=10)
    $ vn_route = "harem"
    jump hrm_ch1

label hrm_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"harem"}
    $ vn_route = None
    hide screen hrm_rank
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e8b04a}The Sultan Keeps the Key{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _hrm_trace():
        pc = hrm_pc_file(hrm_face_now()).rsplit("/", 1)[-1] if renpy.showing("hrm_pc") else None
        cast = None
        for _t in ("hrm_zarina", "hrm_leyla", "hrm_nasrin", "hrm_dilara", "hrm_orhan", "hrm_kasim", "hrm_brask"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, hrm.fit

    vn_trace_routes["harem"] = _hrm_trace
