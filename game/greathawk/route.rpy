## Greathawk -- "My Escape Rope Was Finished the Same Day My Wings Came In, but the Wind Was Wrong"
## (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the
## owner). From catalog/game/02-engine/storylines/greathawk/ (greathawk.js: the rows, the rope, the
## gifts, Kite's banded lines and the PC's pool; main.twee, rungs.twee, bred.twee, ending.twee), kept
## verbatim in catalog/docs/routes/vn-original/greathawk/.
##
## THE NON-CON PASS (owner, 2026-10-19/20, as signed off): pure resist-then-break. Kite's asks lose
## their question marks ("Touch you now."); night one's "No." gets "Tomorrow, then."; from rung 2 to
## the duet every scene is taken and none flips. He pins with his wings and holds; he never
## threatens, never cruel. You knot an escape rope every dusk and never say yes.
##
## Full TSF with the harpy on top, never instead: a woman's face, hands stay hands, no talons for the
## PC. Bred at rung 5 (the owner's 2026-10-19 ruling); what the belly holds is never named, and no
## egg, chick or animal appears anywhere. The ART DRAWS THE BELLY FLAT (owner, 2026-11-12: "Keep it
## flat in art"); the swell lives in the prose only. He/him until "Wife." at rung 7. All route-local
## names carry grh_.

init -10 python:
    GRH = "art/greathawk/"

    # THE ROPE: the piece each rung adds, the count said out loud (the route's only number, in words),
    # what it reaches at the lip, and the swatch the rope screen draws for it.
    GRH_ROPE = [None,
        dict(piece="your own shirt cuff", count="One piece.", swatch="#5b7fa6",
             reach="It reaches nothing. It's a knot in your fist."),
        dict(piece="two strips of the stinking coat", count="Two pieces.", swatch="#5c6270",
             reach="Held up at the lip, it hangs past your knees."),
        dict(piece="a jacket's one good sleeve", count="Three pieces.", swatch="#6b4f3a",
             reach="Let down over the lip, it reaches the arrow-slit under the parapet."),
        dict(piece="the blue webbing, torn with your teeth", count="Four pieces.", swatch="#2f5fa8",
             reach="Let down over the lip, it reaches the ivy scar halfway down the wall."),
        dict(piece="a hiker's scarf", count="Five pieces.", swatch="#b04a3a",
             reach="Let down over the lip, it reaches the stub of the old stair."),
        dict(piece="the blue wool off an old jacket", count="Six pieces. One to go.", swatch="#3d5a8c",
             reach="Let down over the lip, it nearly reaches the yard. Your toes would dangle over the rubble."),
        dict(piece="a knapsack's white canvas", count="Seven pieces.", swatch="#ecebe4",
             reach="Let down over the lip, it touches the yard."),
    ]

    # THE GIFTS: what he drops at your feet each morning, and the small second one that cracks you
    # on an Ignore morning. Raided food, junk, the day's cloth. Never anything alive.
    GRH_GIFTS = [None,
        dict(gift="a ham off a farm hook", crack="an apple, polished on his forearm feathers"),
        dict(gift="a coat", crack="a cracked cup"),
        dict(gift="a pie still in its tin", crack="a plush keyring off a hiker's pack"),
        dict(gift="a hank of blue webbing", crack="a wallet with somebody's cards still in it"),
        dict(gift="a hiker's scarf and a fleece", crack="a dented tin cup"),
        dict(gift="an old jacket and a quilt", crack="a bag of oatcakes"),
        dict(gift="an armful of velvet", crack="a spoon"),
    ]

    # The body's rows, in order: "4r" is rung 4 with the throat ruff (it comes up at dusk, after the
    # tail at waking). The sprite row only moves forward.
    GRH_ROWS = ["0", "1", "2", "3", "4", "4r", "5", "6", "7", "8"]

    def grh_body(row):
        """The body takes `row` (a GRH_ROWS name), toward it and never back."""
        row = str(row)
        if GRH_ROWS.index(row) > GRH_ROWS.index(grh.row or "0"):
            grh.row = row

    def grh_rope(n):
        """The day's piece is knotted on: the rope is that long now."""
        grh.rope = max(grh.rope or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "own" (the charity-shop button shirt, jeans, walking boots), "flannel" (from rung 5's
    # dawn: the shirt and jeans gone, Kite's checked flannel tied round her hips as a skirt, bare
    # above), "nude" (the pool, the wreck of the clothes). The harpy parts are in the rows.
    _grh_have = {}

    def _grh_has(n):
        if n not in _grh_have:
            _grh_have[n] = renpy.loadable(GRH + n + ".png")
        return _grh_have[n]

    def grh_pc_file(face):
        r, fit = grh.row or "0", grh.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-stubborn" % (r, fit),
                 "pc-r%s-own-%s" % (r, face), "pc-r%s-own-stubborn" % r]
        for n in names:
            if _grh_has(n):
                return GRH + n + ".png"
        return GRH + names[-1] + ".png"

    def grh_face_now():
        a = renpy.get_attributes("grh_pc")
        return a[0] if a else "stubborn"

    def _grh_portrait(st, at):
        p = vn_art_file(grh_pc_file(grh_face_now()))
        crops = globals().get("greathawk_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["greathawk"] = lambda: DynamicDisplayable(_grh_portrait)

    vn_sprite_image("grh_pc", ("stubborn", "furious", "flushed", "overwhelmed"), grh_pc_file, who="pc")
    vn_sprite_image("grh_kite", ("flat", "pleased"), lambda f: GRH + "kite-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(GRH) and _f.endswith(".jpg"):
            _n = _f[len(GRH):-4]
            vn_register_bg("grh_" + _n.replace("-", "_"), _f)
            vn_register_cg("grh_" + _n.replace("-", "_"), _f)

    vn_register_route("greathawk", "My Escape Rope Was Finished the Same Day My Wings Came In, but the Wind Was Wrong",
        "You're on the moor road with everything you own in a rucksack, between a lease that ran out and a job that hasn't started, and nobody is expecting you anywhere. A shadow crosses you twice. The third time it doesn't. You wake in a roofless tower on a spur of rock with no stairs, and the harpy on the parapet tells you, flat, what he's going to do to you next, and does it. Seven pieces of cloth, knotted, make a rope that reaches the ground. You're counting.",
        GRH + "cover.jpg", "greathawk_start")

    achievement.register("Not Yet")

default grh = VNState(row="0", fit="own", rope=0, called="landbound")
default grh_pc_name = "Ansel"
default grh_kite_name = "The harpy"

define grh_you = VNChar("[grh_pc_name]", who="pc", plate="#4a5a3a")
define grh_kite = VNChar("[grh_kite_name]", who="grh_kite", plate="#3a2a1a")

## THE ROPE: the knotted pieces as cloth swatches on a line, a dark knot between each, never a
## number; the spoken count, in words, as its caption.
screen grh_rope(n):
    zorder 60
    $ _n = max(1, min(7, n))
    frame:
        xalign 0.5 ypos 60
        padding (30, 20)
        background Frame(Solid("#1c1a16f0"), 0, 0)
        vbox:
            spacing 14
            hbox:
                xalign 0.5
                for _i in range(_n):
                    frame:
                        xysize (86, 34)
                        yalign 0.5
                        background Frame(Solid(GRH_ROPE[_i + 1]["swatch"]), 0, 0)
                    if _i < _n - 1:
                        frame:
                            xysize (16, 46)
                            yalign 0.5
                            background Frame(Solid("#2a2016"), 0, 0)
            text "{i}%s{/i}" % GRH_ROPE[_n]["count"] size 24 color "#e8dcc0" xalign 0.5

label greathawk_start:
    $ grh = VNState(row="0", fit="own", rope=0, called="landbound")
    $ vn_clock = VNState(day=1, hour=10, minute=0)
    $ vn_route = "greathawk"
    $ grh_pc_name = "Ansel"
    $ grh_kite_name = "The harpy"
    if not renpy.session.get("vn_picks"):
        $ grh_pc_name = renpy.input("Your name? (Ansel, unless you'd like another. Reeve either way.)", default="Ansel", length=20).strip() or "Ansel"
    jump grh_road

label grh_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"greathawk"}
    $ vn_route = None
    hide screen grh_rope
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}Not Yet{/color}{/size}\n\n{i}The end.{/i}"
    jump start
