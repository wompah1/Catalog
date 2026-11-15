## Wolfpack -- "Getting Bred Is Just How You Get Promoted Around Here"
## (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the
## owner). From catalog/game/02-engine/storylines/wolfpack/ (wolfpack.js: the rows, the furs, the
## verdicts, the wrong words, the pack's lines and the PC's three pools; main.twee, rungs.twee,
## ending.twee, widgets.twee's notebook), kept verbatim in catalog/docs/routes/vn-original/wolfpack/.
##
## THE NON-CON PASS (owner, 2026-10-19/20, as signed off): escalating corruption. "Pack takes nothing
## that doesn't present," word for word, but the PACK decides what counts: bending for your
## headlamp, kneeling at the spring, turning your back. Rungs 1 and 2 are taken and never flip; rung 3
## and the knot's first stage flip at the break; from the locked stage on it's consensual. Pinning and
## holding are allowed; no binding, threats, tears or pain. The choices pick how, never whether.
##
## Full TSF with the wolf on top, never instead: fangs, ears, a tail, gold eyes; a woman's face, no
## fur on skin, no muzzle. The pack are men with wolf ears and tails. BRED at the rung 4 knot (the
## owner's ruling, "breeding is the engine"; wolfpack is exempt from the blacklist): the belly rounds
## over the days after, heavy and leaking on day 6, and the ART DRAWS IT AS WRITTEN (owner,
## 2026-11-12). The birth is off the page in one oblique line; offspring never appear, and none of
## their words appear anywhere. He/him until the tree on day 5. All route-local names carry wlf_.

init -10 python:
    WLF = "art/wolfpack/"

    # What the alpha says, once a rung (index = tier; 6 = the ending).
    WLF_VERDICT = ["Not pack.", "Low pack.", "Low pack.", "Good pack.", "First pack.", "My pack.", "The den is yours."]

    # THE FURS: where your place in the den is, from the mouth to the back wall. One line at waking
    # and one at night, never a count (setup.wolfpackFurs).
    WLF_FURS = [
        dict(wake="Bare stone under your hip, your kit at your back. The mouth of the den, where nobody sleeps but you.",
             night="Bare stone by your kit, at the mouth. Nobody's thrown you so much as a hide."),
        dict(wake="One old hide under you, thrown down at the mouth, past the end of the crescent. Yours. Somebody threw it there for you.",
             night="Your hide, at the mouth, past the end of their crescent. Still a hide. Still yours."),
        dict(wake="Your hide's in the crescent now, dragged in beside Bramble's, and Bramble's arm is over your hip.",
             night="Your hide, in the crescent, and Bramble already lying on half of it."),
        dict(wake="Two hides under you, inside the crescent, between Grey's furs and the fire. Warm on both sides.",
             night="Two hides, between Grey and the fire. You stretch out on both of them on purpose."),
        dict(wake="The back wall. The alpha's own furs, deep and warm and smelling of him, and you in the middle of them.",
             night="The alpha's furs, at the back wall. Nobody asks whose they are now."),
        dict(wake="The bed they built you at the back wall: the best furs in the den, and Notch's ferns under them, still green.",
             night="Your bed at the back wall. Somebody's put fresh ferns under the furs again without being asked."),
        dict(wake="The back wall, yours alone. Down at the mouth, across your first hide, the alpha is lying in the guard's place.",
             night="The back wall is yours. The alpha lies across the mouth, facing out."),
    ]

    # THE WRONG WORD: one spoken line at each waking, never a monologue.
    WLF_WORD = dict(fangs="Promotion.", ears="Field adaptation.", tail="Obviously.", chest="Rank insignia.",
                    tree="Streamlining.", belly="Seniority.")

    # THE NOTEBOOK: three clinical entries, no dates, times or figures (widgets.twee).
    WLF_NOTEBOOK = [None,
        ["CAVE, EAST SLOPE, DEEP WOOD.", "UPRIGHT INDIVIDUALS. ADULT. MALE.",
         "RANGE PROBABLE: THE LAKE AND THE UPPER RIDGE.", "HIERARCHY PRESENT. OBSERVER UNRANKED."],
        ["ESTRUS ONSET IN LOCAL POPULATION. ABRUPT. COINCIDENT WITH TAIL ERUPTION.",
         "THE SPECIMEN PRESENTS READILY AND IS FULLY RECEPTIVE.", "PROCEEDING TO DEN FOR FURTHER SAMPLING."],
        ["PACK DEFERS.", "RANGE: ALL OF IT."],
    ]

    # The body's rows: "0" Declan as he walked in, "1" to "4" the rungs ("2t" is rung 2 with the tail,
    # which comes up mid-morning on day 3; "3f" is rung 3's body with the cock gone, from the shift under
    # the knot), "5" the belly over the days after, "5m" day 6 (the belly
    # huge, the milk in), "5b" day 7 (after the birth: the belly gone soft, the breasts still full),
    # "6" the end. The sprite row only moves forward.
    WLF_ROWS = ["0", "1", "2", "2t", "3", "3f", "4", "5", "5m", "5b", "6"]

    def wlf_body(row):
        """The body takes `row`, toward it and never back."""
        row = str(row)
        if WLF_ROWS.index(row) > WLF_ROWS.index(wlf.row or "0"):
            wlf.row = row

    def wlf_advance(n):
        """The verdict: the rank moves, never back."""
        wlf.tier = max(wlf.tier or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "own" (his field shirt, trousers and boots), "jacket" (from the days after: the field
    # jacket worn open over a bare body, straining, then split at the end), "nude". The wolf parts and
    # the belly are in the rows.
    _wlf_have = {}

    def _wlf_has(n):
        if n not in _wlf_have:
            _wlf_have[n] = renpy.loadable(WLF + n + ".png")
        return _wlf_have[n]

    def wlf_pc_file(face):
        r, fit = wlf.row or "0", wlf.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-proud" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-proud" % r]
        for n in names:
            if _wlf_has(n):
                return WLF + n + ".png"
        return WLF + names[-1] + ".png"

    def wlf_face_now():
        a = renpy.get_attributes("wlf_pc")
        return a[0] if a else "proud"

    def _wlf_portrait(st, at):
        p = vn_art_file(wlf_pc_file(wlf_face_now()))
        crops = globals().get("wolfpack_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["wolfpack"] = lambda: DynamicDisplayable(_wlf_portrait)

    vn_sprite_image("wlf_pc", ("proud", "furious", "flushed", "smug"), wlf_pc_file, who="pc")
    for _t, _faces in (("alpha", ("flat", "dark")), ("grey", ("flat", "snarl")), ("notch", ("grin", "eager")),
                       ("bramble", ("grin", "sleepy")), ("oldman", ("kind", "flat")), ("scrap", ("shy", "eager")),
                       ("gil", ("flat",))):
        vn_sprite_image("wlf_" + _t, _faces, renpy.curry(lambda t, f: WLF + t + "-" + f + ".png")(_t))

    for _f in renpy.list_files():
        if _f.startswith(WLF) and _f.endswith(".jpg"):
            _n = _f[len(WLF):-4]
            vn_register_bg("wlf_" + _n.replace("-", "_"), _f)
            vn_register_cg("wlf_" + _n.replace("-", "_"), _f)

    vn_register_route("wolfpack", "Getting Bred Is Just How You Get Promoted Around Here",
        "Deep into a solo survey of the forest, something upright paces you for the last mile, then picks you up and carries you to a cave past the lake. A pack of wolf-men lives there. The alpha looks you over, says \"Not pack,\" and goes to sleep. The den has one rule: pack takes nothing that doesn't present. You have never lost a hierarchy in your life.",
        WLF + "cover.jpg", "wolfpack_start")

    achievement.register("The Den Is Yours")

default wlf = VNState(row="0", fit="own", tier=0)
default wlf_pc_name = "Declan"
## The five go by what you see until you name them at dusk on day 2.
default wlf_grey_name = "The grey-bearded one"
default wlf_notch_name = "The split-eared one"
default wlf_bramble_name = "The burr-matted one"
default wlf_old_name = "The old one"
default wlf_scrap_name = "The short one"

define wlf_you = VNChar("[wlf_pc_name]", who="pc", plate="#5a4a32")
define wlf_alpha = VNChar("The alpha", who="wlf_alpha", plate="#1e1e24")
define wlf_grey = VNChar("[wlf_grey_name]", who="wlf_grey", plate="#5c5f66")
define wlf_notch = VNChar("[wlf_notch_name]", who="wlf_notch", plate="#6b5a3e")
define wlf_bramble = VNChar("[wlf_bramble_name]", who="wlf_bramble", plate="#5a4630")
define wlf_old = VNChar("[wlf_old_name]", who="wlf_oldman", plate="#6e6a60")
define wlf_scrap = VNChar("[wlf_scrap_name]", who="wlf_scrap", plate="#4e4a52")
define wlf_gil = VNChar("Gil", who="wlf_gil", plate="#3e5a3a")

## THE FURS: where you lie, and what the alpha last said. One line each, never a count.
screen wlf_furs(kind):
    zorder 60
    $ _t = max(0, min(6, wlf.tier or 0))
    frame:
        xalign 0.5 ypos 60
        xmaximum 1180
        padding (34, 22)
        background Frame(Solid("#1a1610f0"), 0, 0)
        vbox:
            spacing 10
            text ("{color=#f3c969}Your furs:{/color} " + WLF_FURS[_t][kind]) size 26 color "#ece4d4"
            text ("{color=#f3c969}The alpha:{/color} \"" + WLF_VERDICT[_t] + "\"") size 26 color "#ece4d4"

## THE NOTEBOOK: a page of the field notebook, in blocky surveyor's capitals.
screen wlf_notebook(n):
    zorder 60
    frame:
        xalign 0.5 ypos 50
        xmaximum 1120
        padding (36, 26)
        background Frame(Solid("#ebe4d0f4"), 0, 0)
        vbox:
            spacing 10
            text "{i}(the field notebook, blocky surveyor's capitals){/i}" size 20 color "#6b6355"
            for _l in WLF_NOTEBOOK[n]:
                text _l size 27 color "#1f5c58" bold True

label wolfpack_start:
    $ wlf = VNState(row="0", fit="own", tier=0)
    $ vn_clock = VNState(day=1, hour=15, minute=0)
    $ vn_route = "wolfpack"
    $ wlf_pc_name = "Declan"
    $ wlf_grey_name = "The grey-bearded one"
    $ wlf_notch_name = "The split-eared one"
    $ wlf_bramble_name = "The burr-matted one"
    $ wlf_old_name = "The old one"
    $ wlf_scrap_name = "The short one"
    if not renpy.session.get("vn_picks"):
        $ wlf_pc_name = renpy.input("Your name? (Declan, unless you'd like another. Crane either way.)", default="Declan", length=20).strip() or "Declan"
    jump wlf_opening

label wlf_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"wolfpack"}
    $ vn_route = None
    hide screen wlf_furs
    hide screen wlf_notebook
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}The Den Is Yours{/color}{/size}\n\n{i}The end.{/i}"
    jump start
