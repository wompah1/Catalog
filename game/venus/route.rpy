## Porn Star Training Put Me on the Girls' Track, So Obviously It's a Harem -- the catalog's `venus`
## route ("Fourteen Days at Venus and Mars"), rewritten straight in Ren'Py (2026-11-11; owner: "do
## My Pink Hair Made Me the Pink Ranger ... and then Venus"). The DoL catalog's version is kept
## verbatim in catalog/docs/routes/vn-original/venus/ (twee, js, spec); this is a rewrite from it,
## faithful to the signed-off spec (2026-10-15/16/19). The VN plan is game/venus/PLAN.md.
##
## THE REGISTER: a misreading. Chris is sure it's stud training and says yes to everything; the
## staff are kind and sure they're helping; the two readings never meet (the double irony) until
## the last day, when he's right. One misreading per rung, said out loud, mid-act. THE NON-CON PASS
## (owner, 2026-11-11, about 6:40 pm ET: "Rung 2 only"): the first prop, where he balks and the
## headphones go on, is non-con, resist-then-break; he misreads what his body did afterwards.
##
## THE LADDER: realism, what's on your mat -- nothing; a silicone cock on a stand; a bigger one that
## finishes; the wide one between your breasts; a suction prop and then Simon; a camera, red light
## on. Fourteen course days at Thornleigh House, the country hotel. All names carry the ve_ prefix.

init -10 python:
    VE = "art/venus/"

    # The course day -> the rung (venus.js setup.venusDays).
    VE_DAYS = [None, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6]

    # The metronome: what's on your mat (setup.venusMat). Never a number.
    VE_MAT = [
        "",
        "nothing at all: a mirror, an orchid in a glass of water, and a card for three words",
        "a silicone cock on a little stand, pink and glossy and patient",
        "a bigger one, veined, with a squeezable reservoir in the base",
        "a wide one with a heavy bulb at the root, loaded, for working between your breasts",
        "a thick one on a suction base, stuck to the mat, and you know exactly where it goes",
        "a camera on a tripod, red light on",
    ]

    # The two readings (setup.venusReadings): neither side ever says the other's.
    VE_READINGS = [
        None,
        ("VIP onboarding.", "Bless her, she's terrified."),
        ("Star power.", "She's taking it seriously."),
        ("Endurance training.", "She needs more reassurance than the others."),
        ("The girls are basically my entourage.", "They've adopted her."),
        ("Stud training. Final module.", "She's ready. She just doesn't know it."),
        ("Headliner. Called it.", "This is why the programme exists."),
    ]

    VE_WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def ve_call_sheet(day):
        """The call sheet, in weekdays (decision 7): course day 1 is a Monday, the wrap Sunday week."""
        wd = VE_WEEKDAYS[(day - 1) % 7]
        left = 14 - day
        wrap = "today" if left == 0 else "tomorrow" if left == 1 else ("Sunday" if day >= 8 else "Sunday week")
        return "%s. Wrap: %s." % (wd, wrap)

    # ---- the ladder --------------------------------------------------------------------------
    def ve_body(n):
        ve.body = max(ve.body or 1, n)

    def ve_day(n):
        ve.day = n
        ve.rung = VE_DAYS[n]

    # ---- the stage ---------------------------------------------------------------------------
    _ve_have = {}

    def _ve_has(n):
        if n not in _ve_have:
            _ve_have[n] = renpy.loadable(VE + n + ".png")
        return _ve_have[n]

    def ve_art(name):
        return VE + name + ".png" if _ve_has(name) else VE + "_blank.png"

    def ve_rung_now():
        return max(1, min(6, ve.body or 1))

    def ve_pc_file(face):
        """The sprite that exists: the outfit with this face, the outfit's neutral, the own clothes
        with this face, the own clothes' neutral. Rung 1's own clothes are pc-r1-<face>."""
        r, fit = ve_rung_now(), ve.fit or "own"
        own = "pc-r%d" % r if r == 1 else "pc-r%d-own" % r
        names = []
        if fit != "own":
            names += ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-neutral" % (r, fit)]
        names += ["%s-%s" % (own, face), "%s-neutral" % own]
        for n in names:
            if _ve_has(n):
                return VE + n + ".png"
        return VE + "_blank.png"

    def ve_face_now():
        a = renpy.get_attributes("ve_pc")
        return a[0] if a else "neutral"

    def _ve_portrait(st, at):
        p = vn_art_file(ve_pc_file(ve_face_now()))
        if p.endswith("_blank.png"):
            return Null(), None
        x, y, w, h = vn_face_crop(venus_face_crops, p)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["venus"] = lambda: DynamicDisplayable(_ve_portrait)

    def ve_simon_file(face):
        """Simon as Mars builds him: rung 1-2 (pre), 3-4 (bigger), 5-6 (huge)."""
        r = ve.rung or 1
        stage = "a" if r <= 2 else "b" if r <= 4 else "c"
        n = "simon-%s-%s" % (stage, face)
        return ve_art(n) if _ve_has(n) else ve_art("simon-%s-neutral" % stage) if _ve_has("simon-%s-neutral" % stage) else ve_art("simon-a-" + face)

    vn_sprite_image("ve_pc", ("neutral", "nervous", "flushed", "shocked", "grin"), ve_pc_file, who="pc")
    vn_sprite_image("ve_simon", ("neutral", "grin", "hungry"), ve_simon_file)
    vn_sprite_image("ve_wade", ("neutral", "warm"), lambda f: ve_art("wade-" + f))
    vn_sprite_image("ve_fiona", ("neutral",), lambda f: ve_art("fiona-" + f))
    vn_sprite_image("ve_mia", ("neutral",), lambda f: ve_art("mia-" + f))
    vn_sprite_image("ve_holly", ("neutral",), lambda f: ve_art("holly-" + f))
    vn_sprite_image("ve_jay", ("neutral",), lambda f: ve_art("jay-" + f))

    for _f in renpy.list_files():
        if _f.startswith(VE) and _f.endswith(".jpg") and "/scenes/" not in _f and not _f.endswith("/cover.jpg"):
            _n = _f[len(VE):-4]
            vn_register_bg("ve_" + _n.replace("-", "_"), _f)
            vn_register_cg("ve_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("venus", [("", "Vanripper")])

    vn_register_route("venus", "Porn Star Training Put Me on the Girls' Track, So Obviously It's a Harem",
        "You talk your best mate Simon into a fortnight's residential performer intensive and fill in both forms in four minutes. You don't read page four. Your badge comes back purple: VENUS, She/Her. Obviously they've spotted star material and put you on the advanced track with a harem.",
        VE + "cover.jpg", "venus_start")

    achievement.register("Venus and Mars")

default ve = VNState(rung=1, body=1, day=1, fit="own", me="Chris", extra=0, wink=None, spa=None, door=False)

## The speakers.
define ve_me = VNChar("[ve.me]", who="pc", plate="#d9774a")
define ve_simon = VNChar("Simon", who="ve_simon", plate="#2f63b8")
define ve_wade = VNChar("Ms. Wade", who="ve_wade", plate="#2f8a86")
define ve_fiona = VNChar("Ms. Fiona", who="ve_fiona", plate="#c27a9a")
define ve_mia = VNChar("Mia", who="ve_mia", plate="#b36bd1")
define ve_holly = VNChar("Holly", who="ve_holly", plate="#5b4a8a")
define ve_jay = VNChar("Jay", who="ve_jay", plate="#a34a2a")
define ve_anna = VNChar("Anna", who="ve_anna", plate="#9a86b8")
define ve_megan = VNChar("Megan", who="ve_megan", plate="#9a86b8")
define ve_girl = VNChar("Venus girl", who="ve_girl", plate="#9a86b8")
define ve_counter = VNChar("The counter", who="ve_counter", plate="#6b6b78")
define ve_voice = VNChar(None, what_italic=True, what_color="#ff9ed8")

## Route select's entry: Danube Street, the sign in the Dollhouse window, ten in the morning.
label venus_start:
    $ ve = VNState(rung=1, body=1, day=1, fit="own", me="Chris", extra=0, wink=None, spa=None, door=False)
    $ vn_clock = VNState(day=1, hour=10, minute=0)
    $ vn_route = "venus"
    jump ve_opening

## The end of the route ("Choose another story").
label ve_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"venus"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#ff9ed8}Debut{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The test trace's view of the stage (game/catalog/vntrace.rpy).
init 110 python:
    def _ve_trace():
        pc = ve_pc_file(ve_face_now()).rsplit("/", 1)[-1] if renpy.showing("ve_pc") else None
        cast = None
        for tag in ("ve_simon", "ve_wade", "ve_fiona", "ve_mia", "ve_holly", "ve_jay"):
            if renpy.showing(tag):
                cast = tag[3:] + " " + " ".join(renpy.get_attributes(tag) or ())
        return pc, cast, ve.fit

    vn_trace_routes["venus"] = _ve_trace
