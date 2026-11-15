## Scales -- "The Beast Court Files Humans as Furniture, So My Dragon Lord Is Fucking Me Into a Dragon"
## (the storyline's own title: Ten Thousand Scales, One Name; rewritten straight in Ren'Py,
## 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From
## catalog/game/02-engine/storylines/scales/ (scales.js: the rows, the posture, the perch, the
## passing lords, the day beats, the terms, the petitions, Long Qi's lines and the PC's pool;
## main.twee, rungs.twee, ending.twee), kept verbatim in catalog/docs/routes/vn-original/scales/.
##
## THE NON-CON PASS (owner, 2026-10-19/20, as signed off): escalating corruption. Rungs 1-2 taken
## (the mandatory first anal among them), rungs 3-4 open non-con and turn mid-scene, consensual from
## rung 5. Her vow narrows to the seal alone: "I take what the court gives me. I will not take your
## name." Procedural force only (pinning, holding, being entered while asleep); she corrects, she
## never sneers; no threats.
##
## Full TSF with the dragon on top, never instead: a woman's face, hands stay hands, no snout, no
## fur, no wings. Dragons are people: a true form is court regalia, never in a scene, never touching
## you. No pregnancy, breeding or womb talk; the core is stone, pearl and heat. He/him until Tie
## Shan's "Household. Girl, now." on the terrace at rung 6. All route-local names carry scl_.

init -10 python:
    SCL = "art/scales/"

    # THE POSTURE LINE, by tier: how far off the stone you stay when a lord walks past. Index 0 is
    # before rung 1, 7 after the ending. The hub line never moves back.
    SCL_POSTURE = [
        "Your knees hit the stone before your mind has voted.",
        "Both knees, forehead to the stone, every time.",
        "Down, and up again without being told.",
        "One knee, not both. Ah-Ning says that took her two years.",
        "On your feet, if there's a wall at your back.",
        "On your feet with your hands shaking. You walk past her door without kneeling.",
        "A lord passes and nothing happens to you at all.",
        "You incline your head first, on purpose, because you chose to.",
    ]

    # THE EMPTY PERCH, by tier: what you know about it. Never a count.
    SCL_PERCH = [
        "At the far end of her quarters. Nobody has said what it is.",
        "You dust it daily. Nobody has said what it is.",
        "It's a contract perch. Every other lord's is occupied.",
        "Tie Shan raises it every season. She says \"Noted.\"",
        "The roll has a line for it, and the line is blank.",
        "It has been waiting for whoever offers. Bo Yan told you so.",
        "A seal must be offered, aloud, unforced, by the junior party. She can never be the one to ask.",
        "Occupied.",
    ]

    # Who passes on a rung's day, and what your body does: the day beat's demonstration of the
    # posture line. Index is the tier you're at.
    SCL_PASSING = [None,
        ("Long Qi comes down the main hall with a docket in her fist, twin tails swinging, horns bare.",
         ["{i}Thud.{/i} Both knees. Forehead to the stone. Your body did it before you'd finished deciding anything. She doesn't look down. Nobody does."]),
        ("Two bear-men and a serpent general come through the gallery, heavy and unhurried.",
         ["{i}Thud.{/i} You're down. And then, without anyone saying a word, you're up again, knees wobbling, tray still level. A scribe glances at you twice."]),
        ("A stork envoy picks her way down the third gallery, all neck and lacquer.",
         ["One knee. Not both. You stay there with your heart going like a drum, and then she's past.",
          "\"One knee,\" Ah-Ning says behind you, impressed despite herself. \"That took me two years.\""]),
        ("General Meng comes round the corner, ox-headed, a chain of identity plates rattling on his shoulder.",
         ["Your back finds the wall. Your knees shake and hold. You stay on your feet.",
          "He looks you over, horns to hips. \"Junior. Marked. Hers,\" he says, the way he'd read off a stripe on a sleeve. \"Don't hide them. Unfinished isn't ugly.\" And he's gone."]),
        ("Bo Yan drifts down the colonnade with all nine tails out, bored and glittering.",
         ["The pressure hits. Your hands start shaking. Your knees don't move. You stand there with your tray rattling and he gives you a slow, delighted smile, as if you've done a trick."]),
    ]

    # The conditions list (rung 5): which terms you write out in the kitchens. Flavour.
    SCL_TERMS = [
        ("name", "Your name in the contract", "My name in the contract. Mine. Not just household."),
        ("registry", "The registry notified", "The registry notified. My village's line, at least. They paid for me."),
        ("display", "The right to refuse display", "The right to refuse display. Like the other contract beasts."),
        ("space", "Space, sometimes", "And space. Sometimes. Some days I'm just me."),
    ]

    # The body's rows: "0" the start, 1-6 the rungs, "7" the tribulation. Only ever forward.
    def scl_body(n):
        scl.row = str(max(int(scl.row or 0), n))

    def scl_full():
        """The name surname first, as on the roll: Wei Chuan."""
        return "Wei " + scl_pc_name

    def scl_beat_open():
        """The day beat is on offer: once per rung, by day, as flavour."""
        return 1 <= scl.tier < 6 and (scl.beat_tier or 0) < scl.tier and vn_clock.day > scl.rung_day and vn_clock.hour < 18

    def scl_due():
        """What the hub owes you now (Scales.due, no downtime): "pearls" (the morning of rung 3's
        day), "red" (the day after the spite: the red needs a night of its own), "rung" (the plate
        warms at dusk today), "night" (nothing tonight; the night is the way on), or None."""
        t = scl.tier or 0
        if t < 1 or t >= 6 or vn_clock.day <= scl.rung_day:
            return None
        if t == 2 and not scl.pearls_seen:
            return "pearls"
        if t == 3 and not scl.red_seen:
            return "red" if vn_clock.day >= scl.rung_day + 2 else "night"
        return "rung"

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "village" (his own clothes on the road), "robe" (the plain household robe; it
    # strains from rung 5), "court" (Ah-Ning's robe from rung 6, open at the back for the tail, loops
    # for the horns), "nude". The dragon parts are in the rows.
    _scl_have = {}

    def _scl_has(n):
        if n not in _scl_have:
            _scl_have[n] = renpy.loadable(SCL + n + ".png")
        return _scl_have[n]

    def scl_pc_file(face):
        r, fit = scl.row or "0", scl.fit or "robe"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-stubborn" % (r, fit),
                 "pc-r%s-robe-%s" % (r, face), "pc-r%s-robe-stubborn" % r]
        for n in names:
            if _scl_has(n):
                return SCL + n + ".png"
        return SCL + names[-1] + ".png"

    def scl_face_now():
        a = renpy.get_attributes("scl_pc")
        return a[0] if a else "stubborn"

    def _scl_portrait(st, at):
        p = vn_art_file(scl_pc_file(scl_face_now()))
        crops = globals().get("scales_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["scales"] = lambda: DynamicDisplayable(_scl_portrait)

    vn_sprite_image("scl_pc", ("stubborn", "protesting", "flushed", "soft"), scl_pc_file, who="pc")
    for _w, _faces in (("longqi", ("calm", "warm", "intent")), ("ahning", ("grin", "quiet")),
                       ("boyan", ("bored", "delighted")), ("tieshan", ("booming", "blunt"))):
        vn_sprite_image("scl_" + _w, _faces, (lambda w: (lambda f: SCL + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(SCL) and _f.endswith(".jpg"):
            _n = _f[len(SCL):-4]
            vn_register_bg("scl_" + _n.replace("-", "_"), _f)
            vn_register_cg("scl_" + _n.replace("-", "_"), _f)

    vn_register_route("scales", "The Beast Court Files Humans as Furniture, So My Dragon Lord Is Fucking Me Into a Dragon",
        "Your village sold three harvests to send you up the Coiling Fang. The mountain is a court of nine beast lords, and humans file as household: fed, housed, no standing at all. Long Qi, fourth of the nine, cuts your identity plate from her own scale and sends for you every night. The steam is doing strange things to your hair. It isn't the steam.",
        SCL + "cover.jpg", "scales_start")

    achievement.register("One Name")

default scl = VNState(row="0", fit="village", tier=0, rung_day=0, beat_tier=0, terms=[])
default scl_pc_name = "Chuan"
default scl_full_name = "Wei Chuan"

define scl_you = VNChar("[scl_pc_name]", who="pc", plate="#4a3a2a")
define scl_longqi = VNChar("Long Qi", who="scl_longqi", plate="#a0281e")
define scl_ahning = VNChar("Ah-Ning", who="scl_ahning", plate="#6a5a3a")
define scl_boyan = VNChar("Bo Yan", who="scl_boyan", plate="#c8a060")
define scl_tieshan = VNChar("Tie Shan", who="scl_tieshan", plate="#5a3a2a")
define scl_clerk = VNChar("The clerk", who="other", plate="#6b6b78")
define scl_other = VNChar("Somebody", who="other", plate="#6b6b78")

## THE HUB'S READOUT: where you end up when a lord walks past, what you know about the perch, and
## the plate. Never a number.
screen scl_status():
    zorder 60
    $ _t = 7 if scl.done else max(0, min(7, scl.tier or 0))
    frame:
        xalign 0.5 ypos 50 xsize 900
        padding (30, 20)
        background Frame(Solid("#1a1210f0"), 0, 0)
        vbox:
            spacing 10
            text "{b}When a lord walks past:{/b} %s" % SCL_POSTURE[_t] size 23 color ("#9fe0a0" if _t >= 6 else ("#e8c35a" if _t >= 3 else "#e07a6a"))
            text "{b}The perch:{/b} %s" % SCL_PERCH[_t] size 23 color "#c8c0b4"
            if scl.done:
                text "{b}Your plate:{/b} her scale, on a cord, and the roll says hers. It always did." size 23 color "#ff8fb8"
            elif scl_due() == "rung" and vn_clock.hour >= 18:
                text "{b}Your plate:{/b} warm against your sternum. She's sending for you." size 23 color "#ff8fb8"
            else:
                text "{b}Your plate:{/b} household, Long Qi's -- cut from her own scale. Cool." size 23 color "#8fd8d0"

## The paper you write in the kitchens (rung 5): your terms so far.
screen scl_paper():
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 640
        padding (30, 22)
        background Frame(Solid("#efe6d2f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}Conditions.{/b}" size 24 color "#6a2a10"
            for _k, _label, _say in SCL_TERMS:
                if _k in scl.terms:
                    text "{i}%s.{/i}" % _label size 22 color "#2a2a2a"

## The roll of the Coiling Fang, open on its stone: the fourth perch's line, blank; then amended.
screen scl_roll(filled=False):
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 700
        padding (34, 24)
        background Frame(Solid("#f3ead4f2"), 0, 0)
        vbox:
            spacing 10
            text "{b}The Roll of the Coiling Fang{/b}" size 25 color "#7a1a10" xalign 0.5
            text "The fourth perch. Lord: Long Qi." size 22 color "#2a2a2a"
            if filled:
                text "Occupant: {i}entered as hers{/i}, in the court's own hand." size 22 color "#2a2a2a"
            else:
                text "Occupant: ______________________" size 22 color "#2a2a2a"

label scales_start:
    $ scl = VNState(row="0", fit="village", tier=0, rung_day=0, beat_tier=0, terms=[])
    $ vn_clock = VNState(day=1, hour=15, minute=0)
    $ vn_route = "scales"
    $ scl_pc_name = "Chuan"
    if not renpy.session.get("vn_picks"):
        $ scl_pc_name = renpy.input("Your name? (Chuan, unless you'd like another. Wei either way: surname first, on the roll.)", default="Chuan", length=20).strip() or "Chuan"
    $ scl_full_name = scl_full()
    jump scl_road

label scl_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"scales"}
    $ vn_route = None
    hide screen scl_status
    hide screen scl_paper
    hide screen scl_roll
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}One Name{/color}{/size}\n\n{i}The end.{/i}"
    jump start
