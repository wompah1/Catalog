## Press It -- "I Got Caught Peeping on the Pool Changing Room, and Now She Switches Me On From Her
## Phone" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off
## by the owner). From catalog/game/02-engine/storylines/pressit/ (pressit.js: the rungs, the heat,
## the dormant check, the card, the pools; widgets.twee; main.twee; days-early.twee, days-late.twee),
## kept verbatim in catalog/docs/routes/vn-original/pressit/.
##
## THE NON-CON PASS (owner, 2026-10-21: escalating corruption). He comes to want the switch before he
## wants the use, and the use is what corrupts him. The offer is for the disc only; walking out costs
## a key. Portia never denies she's making him: to "You're making me" she says "Yes." Rungs 1 and 2
## non-con, no flip; 3 solo; 4 flips at "And the heat moves."; 5 flips when the heat drops like a
## stone; 6's thighs and the wrong hole never flip; 6's ask is the turn; 7 consensual. The false-
## victim costume ("This is SO not consensual— again, AGAIN—!") first appears after rung 4's flip.
##
## THE SWITCH (prs_contour): on is a pussy, no cock, and the heat; off is the cock back exactly as it
## was. It only ever happens between scenes. Everything else that changes never comes back.
## Eight linear days; the free-play pool door and the weekly booking after the ending aren't ported.
## All route-local names carry prs_.

init -10 python:
    PR = "art/pressit/"

    # THE HEAT, in words only (setup.pressitHeat / pressitHeatLines): a floor that never goes back.
    PR_HEAT_LINES = [None,
        "Down there you're warm. Just warm. Warm like a hand's resting on it.",
        "Down there you're wet through. Through the board shorts. Through your {i}thoughts{/i}.",
        "It doesn't stop. It doesn't even dip. It's going to be like this all afternoon, and you know it.",
        "It's still going when you lie down. It'll still be going in the morning. It's an overnight sort of heat now.",
        "It comes when you call it now. You've started calling it on purpose.",
        "It's there with the thing switched off. It's there with your cock back. It doesn't care which you've got.",
        "It's just on. It's always on. It's what you are.",
    ]

    # THE DORMANT CHECK (setup.pressitDormant): each rung's losses join the list for good.
    PR_DORMANT = [None,
        dict(adds=["your body hair, all of it", "your old skin", "your old nipples"]),
        dict(adds=["your old voice", "the hard edges of your face", "your flat seat"]),
        dict(adds=[]),
        dict(adds=["your hips", "your ass", "your waist"], note="The switch-off helps less."),
        dict(adds=["your flat chest", "your shoulders", "your height"]),
        dict(adds=["your chest, all of it", "your face, all of it", "your short hair", "the heat"]),
        dict(adds=[], note="Nothing. You're never switched off again."),
    ]

    # THE FITTING CARD (setup.pressitCard): kit names and fit words, never a number. She writes rungs
    # 1-3; from rung 4 she says it out loud and doesn't write it.
    PR_CARD = [None,
        [("RED BOARD SHORTS", "FITS"), ("STAFF T-SHIRT", "FITS")],
        [("RED BOARD SHORTS", "FITS"), ("STAFF T-SHIRT", "FITS")],
        [("RED BOARD SHORTS", "NO CHANGE"), ("STAFF T-SHIRT", "NO CHANGE")],
        [("RED BOARD SHORTS", "WON'T CLOSE"), ("WOMEN'S SWIMSUIT", "FITS")],
        None,
        [("WOMEN'S SWIMSUIT", "WON'T GO OVER"), ("BIKINI TOP", "FITS"), ("BIKINI BOTTOMS", "FITS")],
        [("THE KIT CUPBOARD", "NOTHING FITS")],
    ]

    def prs_body(n):
        """The body takes rung n's row, toward it and never back."""
        prs.body = max(prs.body or 0, n)

    def prs_heat(n):
        """The heat's floor for rung n (it never goes back); its line, for the say after it."""
        prs.heat = max(prs.heat or 0, n)
        store._prs_hl = PR_HEAT_LINES[prs.heat]

    def prs_gone(n):
        out = []
        for i in range(1, max(1, min(7, n)) + 1):
            out += PR_DORMANT[i]["adds"]
        return out

    # ---- the stage --------------------------------------------------------------------------
    # Rows: 0 Brett before the disc, then one per rung, rung 3 sharing rung 2's body. Outfits:
    # "own" (his own clothes), "kit" (red board shorts, the yellow staff t-shirt), "track" (the black
    # staff tracksuit zipped to the chin), "suit" (the red women's one-piece), "bikini" (the red
    # bikini), "nude" (switched on: a pussy, no cock; switched off: his small cock).
    PR_ROW = {0: 0, 1: 1, 2: 2, 3: 2, 4: 4, 5: 5, 6: 6, 7: 7}
    _prs_have = {}

    def _prs_has(n):
        if n not in _prs_have:
            _prs_have[n] = renpy.loadable(PR + n + ".png")
        return _prs_have[n]

    def prs_pc_file(face):
        r = PR_ROW.get(max(0, min(7, prs.body or 0)), 0)
        fit = prs.fit or "kit"
        if fit == "nude":
            fit = "nude-on" if prs.on else "nude-off"
        names = ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-furious" % (r, fit),
                 "pc-r%d-kit-%s" % (r, face), "pc-r%d-kit-furious" % r]
        for n in names:
            if _prs_has(n):
                return PR + n + ".png"
        # ff 2:40 am 11-18 (QA 5c242956): no kit sprite at this row, so the nearest outfit that has
        # one (clothed only: never the other nude, which swaps cock and pussy), then the nearest lower
        # row; never a file that is missing.
        for rr in range(r, -1, -1):
            for f in (fit, "kit", "track", "suit", "bikini", "own"):
                for fc in (face, "furious", "flushed", "wanting", "smug", "costume"):
                    n = "pc-r%d-%s-%s" % (rr, f, fc)
                    if _prs_has(n):
                        return PR + n + ".png"
        return PR + names[-1] + ".png"

    def prs_face_now():
        a = renpy.get_attributes("prs_pc")
        return a[0] if a else "furious"

    def _prs_portrait(st, at):
        p = vn_art_file(prs_pc_file(prs_face_now()))
        crops = globals().get("pressit_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["pressit"] = lambda: DynamicDisplayable(_prs_portrait)

    # The calendar: day 1 is a Friday (the late shift), then the skip to Tuesday evening, and a day
    # each from there: Wednesday's afternoon shift, Thursday, Friday, Saturday's summons, Sunday in
    # the changing room, Monday's chair. vn_clock.day counts real days, so the weekday is the true one.
    PR_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def prs_weekday_name():
        return PR_WD[(5 + vn_clock.day - 1) % 7]    # day 1 is a Friday

    def prs_to_weekday(wd, h=8):
        """Minutes from now to the next weekday wd (0 Sunday) at hour h, at least a day on."""
        cur = (5 + vn_clock.day - 1) % 7
        days = (wd - cur) % 7 or 7
        return days * 24 * 60 + (h - vn_clock.hour) * 60 - vn_clock.minute

    vn_weekdays["pressit"] = prs_weekday_name

    vn_sprite_image("prs_pc", ("smug", "furious", "flushed", "costume", "wanting"), prs_pc_file, who="pc")
    vn_sprite_image("prs_portia", ("amused", "intent", "soft"), lambda f: PR + "portia-" + f + ".png")
    vn_sprite_image("prs_travis", ("grin", "stunned"), lambda f: PR + "travis-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(PR) and _f.endswith(".jpg"):
            _n = _f[len(PR):-4]
            vn_register_bg("prs_" + _n.replace("-", "_"), _f)
            vn_register_cg("prs_" + _n.replace("-", "_"), _f)


    vn_register_route("pressit", "I Got Caught Peeping on the Pool Changing Room, and Now She Switches Me On From Her Phone",
        "You work the evening lifeguard chair at the university pool, and you hold the plant-room key. Behind the chlorine drums there's a louvre into the women's changing room, and you rate what you see out loud. Tonight Portia Verrick is standing behind you while you do it. She doesn't threaten you. She offers. Hold still, and she puts something on your hip that she runs from her phone.",
        PR + "cover.jpg", "pressit_start")

    achievement.register("That's All I'm For")

default prs = VNState(body=0, fit="kit", on=False, heat=0, switches=0)
default prs_enc = VNState(partner_came=True, pc_orgasms=0)
default prs_pc_name = "Brett"
default _prs_hl = ""

define prs_you = VNChar("[prs_pc_name]", who="pc", plate="#2f6f8f")
define prs_portia = VNChar("Portia", who="prs_portia", plate="#7a2a4a")
define prs_travis = VNChar("Travis", who="prs_travis", plate="#c2903a")
define prs_manager = VNChar("The duty manager", who="manager", plate="#6b6b78")
define prs_other = VNChar("Somebody", who="other", plate="#6b6b78")

## THE DORMANT CHECK: what came back (always your cock, the same as the first night) and what didn't
## (a list that only grows). Words only.
screen prs_dormant(n):
    zorder 60
    $ _r = max(1, min(7, n))
    $ _note = PR_DORMANT[_r].get("note")
    frame:
        xalign 0.5 ypos 60 xsize 820
        padding (30, 22)
        background Frame(Solid("#10161cf0"), 0, 0)
        vbox:
            spacing 8
            text "{b}DORMANT CHECK{/b}" size 24 color "#f3c969"
            text "{color=#f3c969}CAME BACK:{/color} your cock. Exactly as it was the first night%s." % (", and about as much use" if _r >= 4 else "") size 22 color "#eeeeee"
            text "{color=#f3c969}DIDN'T:{/color} %s." % ", ".join(prs_gone(_r)) size 22 color "#eeeeee"
            if _note:
                text "{color=#f3c969}%s{/color}" % _note size 22
            if _r == 3:
                text "{color=#f3c969}NEW SINCE YESTERDAY:{/color} nothing at all." size 22 color "#eeeeee"

## THE FITTING CARD, in Portia's pen: every line she's written (rungs 1-3), then the fit she says out
## loud and doesn't write (from rung 4).
screen prs_card(n):
    zorder 60
    $ _r = max(1, min(7, n))
    frame:
        xalign 0.5 ypos 60 xsize 760
        padding (30, 22)
        background Frame(Solid("#fbfaf4f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}THE CARD{/b} — THE SUBJECT" size 26 color "#1a1a1a"
            for _i in range(1, min(_r, 3) + 1):
                text "  ".join("%s: {b}%s{/b}." % l for l in PR_CARD[_i]) size 22 color "#222222"
            if _r >= 4 and PR_CARD[_r]:
                text "{i}Said out loud, not written:{/i}" size 22 color "#7a2a4a"
                text "  ".join("%s: {b}%s{/b}." % l for l in PR_CARD[_r]) size 22 color "#7a2a4a"

## THE APP on Portia's phone: one round button, grey (OFF) or pink (ON).
screen prs_app(on):
    zorder 60
    frame:
        xalign 0.5 ypos 60 xsize 300 ysize 380
        padding (20, 24)
        background Frame(Solid("#111114f4"), 0, 0)
        vbox:
            xalign 0.5 yalign 0.5 spacing 18
            add Transform(Solid("#ff5fa8" if on else "#8a8a90"), xysize=(150, 150)) xalign 0.5
            text ("ON" if on else "OFF") size 34 color ("#ff8fc8" if on else "#cfcfd4") xalign 0.5

## A phone: (who, text) pairs; who None is you. A draft shows unsent.
screen prs_phone(lines, draft=False):
    zorder 60
    frame:
        xalign 0.5 ypos 60 xsize 640
        padding (26, 20)
        background Frame(Solid("#161a22f2"), 0, 0)
        vbox:
            spacing 10
            for _w, _t in lines:
                if _w:
                    text "{color=#f3c969}%s:{/color} {i}%s{/i}" % (_w, _t) size 24 color "#f2f2f6"
                else:
                    text "{i}%s{/i}" % _t size 24 color "#9fd0ff" xalign 1.0
            if draft:
                text "{size=-6}not sent{/size}" size 22 color "#8a8a90" xalign 1.0

label pressit_start:
    $ prs = VNState(body=0, fit="kit", on=False, heat=0, switches=0)
    $ prs_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=21, minute=0)
    $ vn_route = "pressit"
    $ prs_pc_name = "Brett"
    if not renpy.session.get("vn_picks"):
        $ prs_pc_name = renpy.input("Your name? (Brett, unless you'd like another. You're Mahoney either way.)", default="Brett", length=20).strip() or "Brett"
    jump prs_opening

## THE SWITCH (<<contour>>): only ever between scenes. A bzzt from her pocket, a flash, the change
## in one short beat, then the heat line; a switch-off is always followed by the dormant check.
label prs_contour(on):
    $ _prs_was = prs.on
    $ prs.on = on
    if on:
        $ prs.switches += 1
        if _prs_was:
            vn_sfx "{i}Bzzt.{/i}"
            "It's already on. It just goes {i}more{/i} on." with vnfx("shake")
        else:
            vn_sfx "{i}Bzzt.{/i}" with vnfx("flash")
            if prs.switches % 3 == 1:
                "Your cock's there, and then it isn't. There's a pussy where it was, slick and swollen and already clenching on nothing."
            elif prs.switches % 3 == 2:
                "Down there everything folds in and opens up at once. A pussy. Wet. Wanting. Just like that."
            else:
                "One heartbeat you've got a cock. The next you've got a soaking pussy and a whole new reason to squeeze your thighs together."
            if (prs.heat or 0) >= 1:
                $ _prs_hl = PR_HEAT_LINES[prs.heat]
                "{color=#ff9ad5}{i}[_prs_hl]{/i}{/color}"
    else:
        vn_sfx "{i}Bzzt.{/i}" with vnfx("flash")
        "It's back. Your cock. Small and stiff and exactly the same as it was the first night, like nothing happened to it at all."
    return

## The heat's word for rung n, as a floor, with its line in pink. Never a rule.
label prs_heat_beat(n):
    $ prs_heat(n)
    "{color=#ff9ad5}{i}[_prs_hl]{/i}{/color}"
    return

label prs_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"pressit"}
    $ vn_route = None
    hide screen prs_dormant
    hide screen prs_card
    hide screen prs_app
    hide screen prs_phone
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}That's All I'm For{/color}{/size}\n\n{i}The end.{/i}"
    jump start
