## Shrine -- "I'm Possessed by a Horny Fox Goddess and the Shrine Gate Won't Let Me Out"
## (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the
## owner). From catalog/game/02-engine/storylines/shrine/ (shrine.js: the rows, the reins, the basin,
## the guardians' lines and the PC's four pools; main.twee, rungs.twee, rungs-late.twee, ending.twee),
## kept verbatim in catalog/docs/routes/vn-original/shrine/. No source book: the spec is canon.
##
## THE REGISTER (owner, 2026-10-20, as signed off): non-con by compulsion. You're aware, unwilling and
## LOUD, never dub-con. The Lady drives your body one more part a rung (hands, legs, mouth, hips,
## voice, all of you) and uses it on the guardians. She gloats, praises and orders; she never
## threatens. Flint pins and holds. The ending is the route's one flip: the reins drop, and the last
## scene is yours, consensual.
##
## Full TSF with the fox on top, never instead: fox ears and tails, gold eyes, fangs; never fur on
## skin, never a muzzle. The guardians are men with fox ears and tails; by day they're carvings. The
## Lady is never a sprite: she's only seen in reflections (the basin, the jewel). He/him until dusk 5,
## when Slate can't tell which of you answered. All route-local names carry shr_.

init -10 python:
    SHR = "art/shrine/"

    # THE REINS: what she has, by rung, in words, never a count (shrine.js setup.shrineReins).
    SHR_REINS = [None,
        "your hands",
        "your hands and your legs",
        "your hands, your legs and your mouth",
        "your hands, your legs, your mouth and your hips",
        "your hands, your legs, your mouth, your hips and your voice",
        "all of you, all day",
        "nothing at all",
    ]

    # THE BASIN: what the water shows of her behind you, by dawn (setup.shrineBasin).
    SHR_BASIN = [None,
        "her eyes, red as lamp glass, open in the water right behind your own",
        "her eyes behind yours, and the water won't let you look away from them",
        "her white ears, standing up over your own, flicking when she laughs",
        "her fan of white tails, spread wide behind your shoulders",
        "her face, where yours was. Your mouth moves when hers does",
        "only her. You lift your hand, and she lifts hers",
        "only you. And you look exactly like her",
    ]

    # The body's rows: "0" is Ryan as he walked up the hill, "1" to "6" the rungs, "7" the end (the
    # kitsune). The sprite row only moves forward.
    SHR_ROWS = ["0", "1", "2", "3", "4", "5", "6", "7"]

    def shr_body(row):
        """The body takes `row`, toward it and never back."""
        row = str(row)
        if SHR_ROWS.index(row) > SHR_ROWS.index(shr.row or "0"):
            shr.row = row

    def shr_take(n):
        """She takes the next thing: the reins reach rung n."""
        shr.reins = max(shr.reins or 0, n)

    # THE SOLO SCENE (rung 1): one of her lines and one of yours a round (setup.shrineHandsLady and
    # setup.shrineHandsPc), the Lady's in her own style.
    SHR_HANDS_LADY = [
        "\"Slower. No— slower. I've waited long enough to want it slow.\"",
        "\"Oh, look at it twitch. Was it always this eager?\"",
        "\"Hold it still, he says. With what? I've got your hands, darling.\"",
        "\"Thumb on the tip. There. Feel that? I can.\"",
        "\"Mm. Again.\"",
        "\"Shout all you like, maiden. Nobody's come up this hill in ages.\"",
        "\"Oh, hands. I'd forgotten hands.\"",
        "\"You're dripping on my robes. Good.\"",
    ]
    SHR_HANDS_PC = [
        "\"Hold STILL— why won't they— {i}why won't they STOP{/i}—!\"",
        "\"Those are MY hands— get off my— {i}hnngh{/i}— get off my COCK—!\"",
        "\"I'm not doing that— I'm NOT— that's not me, that's— {i}ahh{/i}—!\"",
        "\"Let go— let GO— let go of my {i}hands{/i}, you bloody— {i}ohh{/i}—!\"",
        "\"Stop it— stop— slower— no, not SLOWER, STOP— {i}mmh{/i}—!\"",
        "\"It's the robes— it's the mask— it's— it's YOU— get out of my HEAD—!\"",
        "\"I'm going to— don't make me— don't you {i}DARE{/i} make me—!\"",
    ]
    # How much of you she's wound up, out of SHR_HEAT_TOP: she adds one a round whatever you do,
    # letting her adds another, and at the top the only way on is the finish. Holding can win a
    # round (SHR_WILL of them), never the scene.
    SHR_HEAT_TOP = 8
    SHR_WILL = 3

    # Her voice, as a text tag: {shr}...{/shr} prints her words in her colour and italic. Until rung
    # 5 she's only in your head (shr_lady); from rung 5 her words come out of your mouth and cut into
    # yours mid-sentence, and she gets the end of it.
    SHR_LADY_COLOUR = "#f7a072"

    def _shr_tag(tag, argument, contents):
        return ([(renpy.TEXT_TAG, u"color=" + SHR_LADY_COLOUR), (renpy.TEXT_TAG, u"i")] + contents
                + [(renpy.TEXT_TAG, u"/i"), (renpy.TEXT_TAG, u"/color")])

    config.custom_text_tags["shr"] = _shr_tag

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "own" (his hoodie, jeans and trainers), "robes" (the shrine maiden's white top and
    # red hakama, the fox mask pushed up on his head), "open" (the robes open down the front),
    # "hitched" (rung 6: hem tucked into the sash at the waist, the front open), "nude". The fox
    # parts and the body are in the rows.
    _shr_have = {}

    def _shr_has(n):
        if n not in _shr_have:
            _shr_have[n] = renpy.loadable(SHR + n + ".png")
        return _shr_have[n]

    def shr_pc_file(face):
        r, fit = shr.row or "0", shr.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-furious" % (r, fit),
                 "pc-r%s-robes-%s" % (r, face), "pc-r%s-robes-furious" % r]
        for n in names:
            if _shr_has(n):
                return SHR + n + ".png"
        return SHR + names[-1] + ".png"

    def shr_face_now():
        a = renpy.get_attributes("shr_pc")
        return a[0] if a else "furious"

    def _shr_portrait(st, at):
        p = vn_art_file(shr_pc_file(shr_face_now()))
        crops = globals().get("shrine_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["shrine"] = lambda: DynamicDisplayable(_shr_portrait)

    vn_sprite_image("shr_pc", ("furious", "flushed", "possessed", "dazed"), shr_pc_file, who="pc")
    vn_sprite_image("shr_flint", ("flat", "soft"), lambda f: SHR + "flint-" + f + ".png")
    vn_sprite_image("shr_slate", ("grin", "stare"), lambda f: SHR + "slate-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(SHR) and _f.endswith(".jpg"):
            _n = _f[len(SHR):-4]
            vn_register_bg("shr_" + _n.replace("-", "_"), _f)
            vn_register_cg("shr_" + _n.replace("-", "_"), _f)

    vn_register_route("shrine", "I'm Possessed by a Horny Fox Goddess and the Shrine Gate Won't Let Me Out",
        "You run a haunted-Britain channel nobody watches, and you've walked up onto the moor to film an old pillar in the heather. You pray at it for a laugh. There's a folded set of shrine maiden robes at its base, and a fox mask on top, and you put both on for the camera. Then a voice in your head says \"Oh, finally,\" and your hands stop being yours. The red gate behind the pillar won't let you out. And at dusk, the two stone foxes on its posts step down.",
        SHR + "cover.jpg", "shrine_start")

    achievement.register("That One Was You")

default shr = VNState(row="0", fit="own", reins=0)
default shr_pc_name = "Ryan"
default shr_lady_name = "The voice"

define shr_you = VNChar("[shr_pc_name]", who="pc", plate="#4a3a5a")
## The Lady in your head: her own plate, her words in her colour and italic.
define shr_lady = VNChar("[shr_lady_name]", plate="#8a1c2c", what_italic=True, what_color="#f7a072")
## The Lady out of your mouth (rung 5 on): your name on the plate, her words in her style.
define shr_mouth = VNChar("[shr_pc_name]", who="pc", plate="#8a1c2c", what_italic=True, what_color="#f7a072")
define shr_flint = VNChar("Flint", who="shr_flint", plate="#55565c")
define shr_slate = VNChar("Slate", who="shr_slate", plate="#6a5a48")

## THE BASIN: the dawn readout, one line of what she has and one of what the water shows. Never a
## count.
screen shr_basin(n):
    zorder 60
    $ _n = max(1, min(7, n))
    frame:
        xalign 0.5 ypos 60
        xmaximum 1180
        padding (34, 22)
        background Frame(Solid("#121820f0"), 0, 0)
        vbox:
            spacing 10
            text ("{color=#f3c969}She has:{/color} " + SHR_REINS[_n] + ".") size 26 color "#e8e4dc"
            text ("{color=#f3c969}The basin shows:{/color} " + SHR_BASIN[_n] + ".") size 26 color "#e8e4dc"

label shrine_start:
    $ shr = VNState(row="0", fit="own", reins=0)
    $ vn_clock = VNState(day=1, hour=14, minute=0)
    $ vn_route = "shrine"
    $ shr_pc_name = "Ryan"
    $ shr_lady_name = "The voice"
    if not renpy.session.get("vn_picks"):
        $ shr_pc_name = renpy.input("Your name? (Ryan, unless you'd like another. Kemp either way.)", default="Ryan", length=20).strip() or "Ryan"
    jump shr_opening

label shr_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"shrine"}
    $ vn_route = None
    hide screen shr_basin
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}That One Was You{/color}{/size}\n\n{i}The end.{/i}"
    jump start
