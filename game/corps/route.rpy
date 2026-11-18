## My Pink Hair Made Me the Pink Ranger, and the Suit Leaves a Little More of Her Every Time I Take
## It Off -- the catalog's `corps` route, rewritten straight in Ren'Py (2026-11-11; owner: "do My Pink
## Hair Made Me the Pink Ranger ... and then Venus"). The DoL catalog's version is kept verbatim in
## catalog/docs/routes/vn-original/corps/ (twee, js, spec); this is a rewrite from it, faithful to the
## signed-off spec (2026-10-15), its non-con beats (2026-10-19/20) and its vines (2026-10-27, 11-08).
## The VN plan, signed off 2026-11-11 about 6:25 pm ET, is game/corps/PLAN.md.
##
## THE REGISTER: escalating corruption, the book's own arc -- dread, shame-tangled arousal,
## blackmailed submission, craving, joyful acceptance. Anya is the only partner Leo comes to want;
## only her claiming flips. The Bogon losses never flip: resist, then break. No tears, no menace (the
## only threat is the team hearing), painless doujin sex, loud PC.
##
## THE LADDER: the seat, where your orgasm comes from -- the cock (set off by the nipples), the chest
## and cock together, the chest alone, hands-free in public, the ass, the cunt. Seventeen demorphs,
## each leaving a little more of her where its monster held you. Zorp's locus line says it in words.
## All route-local names carry the cp_ prefix.

init -10 python:
    CP = "art/corps/"

    # The monsters: one alert a day. A read picks how the fight goes, never whether; exactly one
    # counters the gimmick (the Zard's are all right: the tutorial). `morphs` is how many demorphs
    # the day costs; `material` flecks the Bogons in a loss; `rung` is the ladder's.
    CP_MONSTERS = {
        "zard": dict(name="Bog-Zard", rung=1, morphs=1, material="mud-slick",
            gimmick="A lizard the size of a bus, melting park benches with its breath. No plan. No brain. Lots of teeth.",
            alert="INCURSION ALERT! Bog-Zard, the park. Big. Green. Rude. Report to the Hub, Pink Ranger!",
            reads=[("Draw the bow the suit put in your hand", True), ("Close to melee", True), ("Shout at it and see what happens", True)],
            bg="cp_park"),
        "monkey": dict(name="Bog-Monkey", rung=1, morphs=1, material="tar-streaked",
            gimmick="It fights from above. It drops onto anything that stands still, and it's sticky.",
            alert="INCURSION ALERT! Bog-Monkey, the market scaffolding. Projections indicate exceptional stickiness. Report to the Hub!",
            reads=[("Take the high ground before it does", True), ("Hold the plaza and wait for it", False), ("Chase it up the scaffold", False)],
            bg="cp_market"),
        "shardwing": dict(name="Shardwing", rung=2, morphs=2, material="glass-flecked",
            gimmick="A raptor of fused glass needles. Break it and it knits itself back out of its own splinters. You'll be morphing again before it's done.",
            alert="INCURSION ALERT! Shardwing, the riverside. It reassembles. Please budget accordingly. Report to the Hub!",
            reads=[("Contain the splinters before you break anything", True), ("Shatter it, and again if you have to", False), ("Wait for it to land", False)],
            bg="cp_riverside"),
        "ironjaw": dict(name="Ironjaw", rung=2, morphs=1, material="chrome-plated",
            gimmick="A cyborg brute plated front to back. Nothing you've got goes through the front.",
            alert="INCURSION ALERT! Ironjaw, the tram depot. Heavily armoured. Report to the Hub!",
            reads=[("Go for the joints", True), ("Overwhelm the plate", False), ("Bring the building down on it", False)],
            bg="cp_depot"),
        "widow": dict(name="Bog-Widow", rung=3, morphs=2, material="web-strung",
            gimmick="It webs the freight yard and fights dirty: it grabs you by the waist and hauls you through the air. And there are two of them.",
            alert="INCURSION ALERT! Bog-Widow, the freight yard. Correction: Bog-Widows. Report to the Hub!",
            reads=[("Cut the anchor lines before it can lift you", True), ("Cut yourself free once it has you", False), ("Let it lift you and strike from up there", False)],
            bg="cp_freightyard"),
        "siren": dict(name="Bog-Siren", rung=3, morphs=1, material="static-humming",
            gimmick="It nests in the TV tower and fights with stolen voices. The only counter is resonance, which means singing its frequency back at it the whole fight.",
            alert="INCURSION ALERT! Bog-Siren, the TV tower. Please warm up your voice. Report to the Hub!",
            reads=[("Sing it back", True), ("Cover your ears and close the distance", False), ("Cut the tower's power", False)],
            bg="cp_tvtower"),
        "bramblemaw": dict(name="Bramblemaw", rung=4, morphs=1, material="vine-wrapped", act=True,
            gimmick="A vine-brute that binds before it crushes. Everything it does, it does by wrapping.",
            alert="INCURSION ALERT! Bramblemaw, the botanical gardens. It is extremely huggy. Report to the Hub!",
            reads=[("Burn the root", True), ("Saw at the creepers one by one", False), ("Hang on and wait for Red", False)],
            bg="cp_gardens"),
        "serpent": dict(name="Bog-Serpent", rung=4, morphs=1, material="scale-patched",
            gimmick="It coils, and every coil is tighter than the last. It doesn't bite until it doesn't have to.",
            alert="INCURSION ALERT! Bog-Serpent, the canal locks. Constriction hazard. Report to the Hub!",
            reads=[("Break the coil at the tail", True), ("Break the coil at the head", False), ("Ride it out until it tires", False)],
            bg="cp_canal"),
        "lensfang": dict(name="Lensfang", rung=4, morphs=1, material="lens-studded",
            gimmick="A camera-eyed cyborg that broadcasts its own fights to every screen in town, and hunts secret identities.",
            alert="INCURSION ALERT! Lensfang, downtown. You are on television. Smile! Report to the Hub!",
            reads=[("Blind the lens first, whatever it costs", True), ("Fight it fast and hope the feed drops", False), ("Play to the camera", False)],
            bg="cp_downtown"),
        "magnavore": dict(name="Magnavore", rung=5, morphs=1, material="iron-filed",
            gimmick="A magnet-cored cyborg that rips away anything ferrous. It's going to have your chestplate off. The only question is whose terms.",
            alert="INCURSION ALERT! Magnavore, the scrapyard. Please remove loose metal items. Report to the Hub!",
            reads=[("Drop the plate yourself and fight soft", True), ("Hold the plate on", False), ("Stay out of its range", False)],
            bg="cp_scrapyard"),
        "echoplasm": dict(name="Echoplasm", rung=5, morphs=1, material="mirror-slick",
            gimmick="A chrome mirror-slime. It tags you, buds off a copy, and the copy fights with your moves in your voice.",
            alert="INCURSION ALERT! Echoplasm, the shopping centre. Do not let it touch you. Report to the Hub!",
            reads=[("Do something you've never done before", True), ("Out-fight it. You know your own moves", False), ("Refuse to look at it", False)],
            bg="cp_mall"),
        "leviathan1": dict(name="Bog-Leviathan", rung=6, morphs=2, material="bog-dripping",
            gimmick="The biggest bog-beast of the war, wallowing in the harbour. It'll take two days to put down, and every morph of it is yours. This is day one.",
            alert="INCURSION ALERT! Bog-Leviathan, the harbour. All rangers. Please cancel your plans for the next two days.",
            reads=[("Pace it. Trade ground, not morphs", True), ("Hit it with everything, every time", False), ("Let the others carry the middle of it", False)],
            bg="cp_harbour"),
        "leviathan2": dict(name="Bog-Leviathan", rung=6, morphs=2, material="bog-dripping",
            gimmick="Day two. It's still in the harbour, and it's angrier.",
            alert="INCURSION UPDATE: Bog-Leviathan, the harbour, day two. It is still there. Report to the Hub!",
            reads=[("Pace it. Trade ground, not morphs", True), ("Hit it with everything, every time", False), ("Let the others carry the middle of it", False)],
            bg="cp_harbour"),
    }

    # Zorp's locus line (the audit reads it; the hub's first line): words, never a figure.
    CP_LOCUS = [
        "Host search: chromatic criterion pink.",
        "Response locus: standard. Provisional.",
        "Response locus: shared.",
        "Response locus: anterior.",
        "Response locus: anterior. Broadcast.",
        "Response locus: posterior.",
        "Response locus: template.",
        "Template conformance: complete.",
    ]

    # The locker, the metronome. Each stage is set by the beat that moves it.
    CP_LOCKER = [
        "There's a locker with a strip of tape on it and your name in Zorp's printing. It's empty.",
        "The clippers sit on the top shelf of your locker. You buzz your hair after every demorph, and it lies down.",
        "Anya's white compression top is folded on your bench, your size, no note. The clippers are still on the shelf, and the hair grows back lighter every time you use them.",
        "The clippers are on the shelf and you use them every night. By morning it's back as a soft pink cap. Every time.",
        "The clippers are in the bin beside the lockers. The whole city watched your hair run past your jaw, so that's that.",
        "Anya's brush sits on the shelf where the clippers used to be.",
        "Your locker's on the women's side now. Vee carried it over herself, contents and all.",
    ]

    # Every morning's waking beat, by the rung the body's at.
    CP_MORNINGS = [
        None,
        "Morning. Your T-shirt drags over your nipples and you go {i}hnn{/i} before your eyes are open.",
        "Morning. You sleep on your back now. Your chest's too sore for anything else, and it's {i}so{/i} nice sore.",
        "Morning. Your hair's back: a soft pink cap over your ears. The clippers didn't take. They never take.",
        "Morning. You're wet before you're awake. Nothing's touched you. Your tits ache for the suit.",
        "Morning. You've slept face-down, ass up, hugging the pillow. It's the only way that's comfy now.",
        "Morning. Both hands on your tits before your eyes are open. {i}Squeeze.{/i} \"{i}Mmh{/i}—\"",
        "Morning. Thunder somewhere over the city. Your braid's over your shoulder and your hand's already between your legs.",
    ]

    # Anya's lines in the written scenes (corps.js setup.slCombatLines.Anya): she never asks.
    CP_ANYA_NONCON = [
        "\"Hips up. I didn't ask.\"",
        "\"Tell the team, then. Go on. Tell them how wet you are.\"",
        "\"Stop squirming, Lily. You'll come from my cock or not at all.\"",
        "\"Say no again. Say it with your ass squeezing me like that.\"",
        "\"Little accidents, Lily. You're having one right now. Feel it?\"",
    ]

    # ---- the ladder ------------------------------------------------------------------------
    def cp_body(n):
        """The body lands (up only): the sprite is the rung's row, from that rung's first demorph."""
        cp.body = max(cp.body or 1, n)

    def cp_mon():
        return CP_MONSTERS.get(cp.fight) if cp.fight else None

    def cp_locus():
        return CP_LOCUS[max(0, min(7, cp.rung or 1))]

    def cp_locker(n):
        cp.locker = max(cp.locker or 0, n)

    def cp_name(n):
        """The plate: Leo until rung 3's meeting ("She took point"), Lily after; Pink while morphed."""
        cp.civ = n
        cp.me = "Pink" if cp.morphed else n

    def cp_morph(on):
        cp.morphed = bool(on)
        cp.me = "Pink" if cp.morphed else (cp.civ or "Leo")

    # ---- the stage -------------------------------------------------------------------------
    _cp_have = {}

    def _cp_has(n):
        if n not in _cp_have:
            _cp_have[n] = renpy.loadable(CP + n + ".png")
        return _cp_have[n]

    def cp_art(name):
        return CP + name + ".png" if _cp_has(name) else CP + "_blank.png"

    def cp_rung_now():
        return max(1, min(7, cp.body or 1))

    def cp_pc_file(face):
        """The sprite that exists: the outfit with this face, the outfit's neutral, the own clothes
        with this face, the own clothes' neutral. Rung 1's own clothes are pc-r1-<face>; the suit is
        the suit's whatever you're wearing under it."""
        r, fit = cp_rung_now(), ("suit" if cp.morphed else (cp.fit or "own"))
        own = "pc-r%d" % r if r == 1 else "pc-r%d-own" % r
        names = []
        if fit != "own":
            names += ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-neutral" % (r, fit)]
        names += ["%s-%s" % (own, face), "%s-neutral" % own]
        for n in names:
            if _cp_has(n):
                return CP + n + ".png"
        return CP + "_blank.png"

    def cp_face_now():
        a = renpy.get_attributes("cp_pc")
        return a[0] if a else "neutral"

    def _cp_portrait(st, at):
        p = vn_art_file(cp_pc_file(cp_face_now()))
        if p.endswith("_blank.png"):
            return Null(), None
        x, y, w, h = vn_face_crop(corps_face_crops, p)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["corps"] = lambda: DynamicDisplayable(_cp_portrait)

    vn_sprite_image("cp_pc", ("neutral", "nervous", "flushed", "shocked", "grin"), cp_pc_file, who="pc")
    vn_sprite_image("cp_anya", ("neutral", "smirk", "hungry"), lambda f: cp_art("anya-" + f))
    vn_sprite_image("cp_red", ("neutral", "smirk"), lambda f: cp_art("red-" + f))
    vn_sprite_image("cp_zorp", ("neutral", "grin"), lambda f: cp_art("zorp-" + f))
    vn_sprite_image("cp_kyle", ("neutral",), lambda f: cp_art("kyle-" + f))
    vn_sprite_image("cp_mira", ("neutral",), lambda f: cp_art("mira-" + f))
    vn_sprite_image("cp_tobi", ("neutral",), lambda f: cp_art("tobi-" + f))
    vn_sprite_image("cp_vee", ("neutral",), lambda f: cp_art("vee-" + f))
    vn_sprite_image("cp_naomi", ("neutral",), lambda f: cp_art("naomi-" + f))
    vn_sprite_image("cp_bogon", ("neutral", "grin"), lambda f: cp_art("bogon-" + f))

    # Echoplasm's copy (owner, 2026-11-17 ~11:35 pm ET, after six drawn passes never drew it: "take a regular
    # sprite, then edit it to just be a chrome monocolor"): the suit sprite in colour, and beside it the same
    # sprite mirrored, a touch bigger, in chrome monochrome. Matrices apply right to left: grey, then doubled
    # (the pink suit greys to ~0.3, too dark to read as chrome; a multiply keeps the black outlines black), then cool.
    class CpScaleMatrix(ColorMatrix, DictEquality):
        """Multiplies R, G and B by `value` (alpha left alone)."""
        def get(self, value):
            return Matrix([value, 0, 0, 0,  0, value, 0, 0,  0, 0, value, 0,  0, 0, 0, 1])

    CP_CHROME = TintMatrix("#e4ecff") * CpScaleMatrix(2.0) * SaturationMatrix(0.0)

    # the owner, 11:4x pm: "put like a shape on the face to cover the human bits": a mirror oval
    # (game/corps/cp-chrome-face.png) over the eyes, nose and mouth, in the suit sprite's own pixels (425x1100)
    CP_ECHO_FACE = (147, 58, 108, 138)

    def _cp_echo(st, at, chrome):
        p = vn_art_file(cp_art("pc-r1-suit-neutral"))
        if not chrome:
            return vn_figure(p), None
        w, h = renpy.image_size(p)
        k = w / 425.0
        fx, fy, fw, fh = [int(round(v * k)) for v in CP_ECHO_FACE]
        body = Fixed(Transform(p, matrixcolor=CP_CHROME),
                     Transform("corps/cp-chrome-face.png", xpos=fx, ypos=fy, xysize=(fw, fh)),
                     xysize=(w, h))
        img = Transform(body, fit="contain", ysize=VN_SPRITE_H)
        shadow = Transform(img, matrixcolor=TintMatrix("#000000") * OpacityMatrix(0.55), blur=16)
        return Transform(Fixed(shadow, img, fit_first=True), xzoom=-1.0, zoom=1.06), None

    renpy.image("cp_echo_real", DynamicDisplayable(_cp_echo, False))
    renpy.image("cp_echo_chrome", DynamicDisplayable(_cp_echo, True))

    # Every picture in the route's folder is a background and a CG by name ("bg cp_hub",
    # "cg cp_zard_bow").
    for _f in renpy.list_files():
        if _f.startswith(CP) and _f.endswith(".jpg") and "/scenes/" not in _f and not _f.endswith("/cover.jpg"):
            _n = _f[len(CP):-4]
            vn_register_bg("cp_" + _n.replace("-", "_"), _f)
            vn_register_cg("cp_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("corps", [("", "Vanripper")])

    vn_register_route("corps", "My Pink Hair Made Me the Pink Ranger, and the Suit Leaves a Little More of Her Every Time I Take It Off",
        "You're twenty-one, you fix bikes, and your hair has always been bubblegum pink. Late one night a chrome robot head inflates out of your phone and tells you pink is the Pink Ranger's one requirement. Morphed, you have her body. Every time the suit comes off, a little of her stays.",
        CP + "cover.jpg", "corps_start")

    achievement.register("Heartstrike Nova")

default cp = VNState(rung=1, body=1, locker=0, me="Leo", civ="Leo")

## The speakers. One person, three plates: Leo at home, Lily from rung 3's meeting, Pink in the suit.
define cp_me = VNChar("[cp.me]", who="pc", plate="#e75ea8")
define cp_anya = VNChar("Anya", who="cp_anya", plate="#b3263a")
define cp_red = VNChar("Red", who="cp_red", plate="#b3263a")
define cp_zorp = VNChar("Zorp", who="cp_zorp", plate="#8a96a8")
define cp_kyle = VNChar("Kyle", who="cp_kyle", plate="#2f63b8")
define cp_blue = VNChar("Blue", who="cp_kyle", plate="#2f63b8")
define cp_mira = VNChar("Mira", who="cp_mira", plate="#c9a227")
define cp_yellow = VNChar("Yellow", who="cp_mira", plate="#c9a227")
define cp_tobi = VNChar("Tobi", who="cp_tobi", plate="#3a3a44")
define cp_black = VNChar("Black", who="cp_tobi", plate="#3a3a44")
define cp_vee = VNChar("Vee", who="cp_vee", plate="#7a4fb0")
define cp_naomi = VNChar("Naomi", who="cp_naomi", plate="#3f8a7a")
define cp_bogon = VNChar("Bogon", who="cp_bogon", plate="#4f6b3a")
define cp_clerk = VNChar("Clerk", who="cp_clerk", plate="#6b6b78")
define cp_unk = VNChar("???", who="???", plate="#6b6b78")

## Route select's entry: late, your flat, the ramen going crusty.
label corps_start:
    $ cp = VNState(rung=1, body=1, locker=0, me="Leo", civ="Leo", fit="own")
    $ vn_clock = VNState(day=1, hour=23, minute=10)
    $ vn_route = "corps"
    jump cp_opening

## The end of the route ("Choose another story").
label cp_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"corps"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#ff7ab8}Heartstrike Nova{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The test trace's view of the stage (game/catalog/vntrace.rpy).
init 110 python:
    def _cp_trace():
        pc = cp_pc_file(cp_face_now()).rsplit("/", 1)[-1] if renpy.showing("cp_pc") else None
        cast = None
        for tag in ("cp_anya", "cp_red", "cp_zorp", "cp_kyle", "cp_mira", "cp_tobi", "cp_vee", "cp_naomi", "cp_bogon"):
            if renpy.showing(tag):
                cast = tag[3:] + " " + " ".join(renpy.get_attributes(tag) or ())
        return pc, cast, ("suit" if cp.morphed else cp.fit)

    vn_trace_routes["corps"] = _cp_trace
