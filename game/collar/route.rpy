## Voice Collar -- "I Bought a Voice Collar for the Tips, and It Won't Let Me Look Down" (rewritten
## straight in Ren'Py, 2026-11-11; the plan is PLAN.md beside this file, signed off by the owner).
## From catalog/game/02-engine/storylines/collar/ (collar.js: the ladder, the body, the cards, Cal's
## lines; main.twee, rungs.twee), kept verbatim in catalog/docs/routes/vn-original/collar/.
##
## THE NON-CON PASS (owner, 2026-11-11: "Both: voice + flip at 4"). The collar is the only force.
## Cal asks before every new thing, as written; at rungs 1-3 the collar's voice answers yes before
## you can, so he hears a yes and never knows. You're aware and unwilling, and your "no" comes out
## a purr. The break is mid-stairwell (rung 3); the flip is on the roof (rung 4), where the want
## arrives and it's yours. From then on it's consensual, and rung 6's "Say yes in your own voice" is
## the first yes that's really yours. On screen: the collar's words are plated "The voice" (pink);
## from the flip, they're plated with your name.
##
## The route plays linear days (no hub wandering): the morning (the card in the post, the mirror),
## the evening's calls and Benny on the intercom, then the knock, text or box that brings the
## rung. All route-local names carry the co_ prefix.

init -10 python:
    CO = "art/collar/"

    # WHERE THE VOICE HAS GOT TO (collar_status), by the tier.
    CO_STATUS = [
        "The voice is for calls. Everywhere else, you're still you.",
        "The voice is for calls. Everywhere else, you're still you.",
        "The voice is for calls, and for Cal, who doesn't bother calling first any more.",
        "The voice has been out on the stairs now, and the building knows it.",
        "The voice has been out under the sky, on the roof, with the whole town below you.",
        "The collar doesn't come off indoors any more. Your own voice sounds wrong.",
        "The collar is on, chin up.",
    ]

    # THE CARDS the catalog mails, one a rung, read aloud and into the drawer (setup.collarCards).
    CO_CARDS = [None,
        ("Item three", "Future versions will likely replace the current posture-style collar with a more conventional collar featuring an electronic module."),
        ("Item four", "Not suitable for use near open water."),
        ("Item five", "Results may vary with frequency of wear."),
        ("Item six", "Do not attempt to resize. Allow the item to resize you."),
        ("Item seven", "If your own voice begins to sound unfamiliar, this is expected."),
        ("Item eight", "Thank you for your loyalty. Please enjoy the enclosed."),
    ]

    # THE BODY's one loud line when a rung lands (setup.collarRungs[n].feel).
    CO_FEEL = [None,
        "Your new lips won't stop tingling. Every word in that voice buzzes on them like a kiss.",
        "Your mouth's so sensitive now that swallowing makes you moan, and your nipples ache against your shirt.",
        "Your tits throb on every step down, and your ass clenches on nothing, hungry.",
        "The wind on your nipples is almost too much, and your lips are swollen and buzzing before he's even kissed them.",
        "Your ass is so sensitive now that the shower's spray makes you gasp, and the water on your soft little cock is a shock.",
        "Everything's raw and new and electric: your lips, your tits, your brand-new cunt. One touch and you're shaking.",
    ]

    # BENNY on the intercom, one extra a rung (Collar Benny). He never sees you; you never open the door.
    CO_BENNY = [None,
        "When you open the door there's a free drink on top of the bag that you didn't order. {i}Benny,{/i} says the receipt. {i}Have a good night!!{/i}",
        "There's a second bag. Nothing in it is on your receipt. There's a smiley face on the second bag.",
        "There's dessert, with a note: {i}on me x{/i}. You eat it with your chin in the air.",
        "The whole order's been comped. Benny has written his number on the box, then crossed it out, then written it again.",
        "Under the food, folded very small: Benny's shift schedule for the next fortnight.",
    ]

    # THE CALLS, a beat a night: the voice does the work; tips come in; no figures, ever.
    CO_CALLS = [
        "You lie back with the phone held over your face and talk. The voice does what it does: men stay on, men tip, men tell you things about themselves you didn't ask.",
        "Every laugh is worth money. You don't even have to be clever. You just have to keep talking, and the voice does the rest.",
        "It comes easier every night. You barely have to try; the voice tries for you.",
    ]

    def co_init():
        if co.tier is None:
            co.tier = 0

    def co_status():
        return CO_STATUS[max(0, min(6, co.tier or 0))]

    def co_calls_line():
        t = co.tier or 0
        return CO_CALLS[2] if t >= 3 else CO_CALLS[1] if t >= 1 else CO_CALLS[0]

    def co_card(n):
        item, line = CO_CARDS[n]
        return '"{color=#ff8fb8}%s.{/color}" {i}%s{/i}' % (item, line)

    def co_advance(n):
        """The rung lands: the ladder moves, the body's new row, the loud line (collar_advance)."""
        co.tier = max(co.tier or 0, n)

    def co_body(n):
        """<<collar_body n>>: the body takes row n; its feel line, the first time."""
        if (co.body or 0) >= n:
            return None
        co.body = n
        return CO_FEEL[n] if n < len(CO_FEEL) else None

    # ---- the stage --------------------------------------------------------------------------
    # Rows: 0 Theo before the parcel; 1-5 the rungs; 6 rung 6 before the shift; 7 after it.
    _co_have = {}

    def _co_has(n):
        if n not in _co_have:
            _co_have[n] = renpy.loadable(CO + n + ".png")
        return _co_have[n]

    def co_row():
        if co.shifted:
            return 7
        return max(0, min(6, co.body or 0))

    def co_pc_file(face):
        """The sprite that exists: the outfit with this face, the outfit with the default face,
        the plain body with this face, the default."""
        r, fit = co_row(), co.fit
        names = []
        if fit:
            names += ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-content" % (r, fit)]
        names += ["pc-r%d-%s" % (r, face), "pc-r%d-content" % r]
        for n in names:
            if _co_has(n):
                return CO + n + ".png"
        return CO + names[-1] + ".png"

    def co_face_now():
        a = renpy.get_attributes("co_pc")
        return a[0] if a else "content"

    def _co_portrait(st, at):
        p = vn_art_file(co_pc_file(co_face_now()))
        crops = globals().get("collar_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["collar"] = lambda: DynamicDisplayable(_co_portrait)

    # The calendar the prose keeps (2026-11-12: the counter has to agree with the story). Day 1 is
    # the Thursday night of the opening, rent due Friday; each rung the Friday after the last ("A
    # soft swell ... that wasn't there last week", "wasn't there a fortnight ago", "a belt this
    # week"), with a week of the same between (CO_GAP, from the morning after a rung).
    CO_RUNG_DAY = {2: 9, 3: 16, 4: 23}
    CO_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    CO_GAP = {
        1: "A week of the same. Calls all day in the voice, and Cal's call every night at eight: same time tomorrow, every tomorrow. The tips come in.",
        2: "Days of the same. Cal's knock every night, and the voice saying yes before you've opened your mouth.",
        3: "Days of the same. Cal's texts, most nights, and the stairs. The neighbours have started saying hello in a funny way.",
    }

    def co_gap_days():
        t = co.tier or 0
        if t not in CO_GAP:
            return 0
        return max(0, CO_RUNG_DAY.get(t + 1, 0) - vn_clock.day)

    def co_weekday_name():
        return CO_WD[(4 + vn_clock.day - 1) % 7]    # day 1 is a Thursday

    vn_weekdays["collar"] = co_weekday_name

    vn_sprite_image("co_pc", ("content", "flushed", "delighted", "shocked", "protesting"), co_pc_file, who="pc")
    vn_sprite_image("co_cal", ("grin", "hungry", "soft"), lambda f: CO + "cal-" + f + ".png")

    # Every picture in the route's folder is a background and a CG by name ("bg co_bedroom",
    # "cg co_doorway_open").
    for _f in renpy.list_files():
        if _f.startswith(CO) and _f.endswith(".jpg"):
            _n = _f[len(CO):-4]
            vn_register_bg("co_" + _n.replace("-", "_"), _f)
            vn_register_cg("co_" + _n.replace("-", "_"), _f)

    # Vanripper the default, Abarus by the HUD's Art button (owner, 2026-11-11: an Abarus set for
    # every rewrite).
    # Vanripper only (owner, 2026-11-12 about 1:56 pm ET: the Abarus alternate set is for femboy,
    # feminization and soft-TSF routes; collar is full TSF)

    vn_register_route("collar", "I Bought a Voice Collar for the Tips, and It Won't Let Me Look Down",
        "You're broke, and the voice-companion app pays women triple. Item three in the catalog is a pink posture collar that gives you a woman's voice. It holds your chin up, so you never see what else it's doing, from the collar down. Cal, from the flat below, hears you through the floor on the first night. He always asks. The voice always answers before you can.",
        CO + "cover.jpg", "collar_start")

    achievement.register("Chin Up")

default co = VNState(tier=0, body=0)
default co_enc = VNState(partner_came=True, pc_orgasms=0)
default co_pc_name = "Theo"

## The speakers. The collar's words are plated "The voice" while they aren't yours (rungs 1-3);
## from the roof they're yours, under your name. Cal in his own colour; Benny and the callers are
## voices only.
define co_voice = VNChar("The voice", who="pc", plate="#e0559a")
define co_you = VNChar("[co_pc_name]", who="pc", plate="#c2508f")
define co_cal = VNChar("Cal", who="co_cal", plate="#b8692c")
define co_benny = VNChar("Benny", who="benny", plate="#5f8f3e")
define co_caller = VNChar("A caller", who="caller", plate="#6b6b78")

## Route select's entry. The route starts on a Thursday night, rent due Friday.
label collar_start:
    $ co = VNState(tier=0, body=0)
    $ co_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=23, minute=40)
    ## the HUD and the box portrait key on vn_route (twinetesting-03 spotted it unset, 2026-11-12)
    $ vn_route = "collar"
    $ co_pc_name = "Theo"
    ## the name box: Theo, unless you'd like another (the spec allows it). A test walk keeps Theo.
    if not renpy.session.get("vn_picks"):
        $ co_pc_name = renpy.input("Your name? (Theo, unless you'd like another.)", default="Theo", length=20).strip() or "Theo"
    jump co_opening

## The end of the route: back to the route select.
label co_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"collar"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e0559a}Chin Up{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The collar's lines in the catalog's hypnosis styling ("Tell me what you see", the cue lines):
## the violet-to-pink of DoL's hypnosisText, as hypno's hy_hypno.
style co_hypno:
    color "#ff8fd0"
    bold True

## The screen trace (game/catalog/vntrace.rpy, for the walks): the PC sprite file, the cast sprite
## as "who face", the outfit set (2026-11-12, so a walkthrough can check each sprite lands on time).
init 110 python:
    def _co_trace():
        pc = co_pc_file(co_face_now()).rsplit("/", 1)[-1] if renpy.showing("co_pc") else None
        cast = ("cal " + " ".join(renpy.get_attributes("co_cal") or ())) if renpy.showing("co_cal") else None
        return pc, cast, co.fit

    vn_trace_routes["collar"] = _co_trace
