## Little Sister Mode (rewritten straight in Ren'Py, 2026-11-11; PLAN.md beside this file, signed off
## by the owner). From catalog/game/02-engine/storylines/sister/ (sister.js, main.twee, rungs.twee,
## acts.twee, ending.twee), kept verbatim in catalog/docs/routes/vn-original/sister/.
##
## CONSENT, as revamped (owner, 2026-10-20): in session Harry IS Mae, eager, no inner protest; the
## violation is the premise (Paige stops asking after film night); Quiet's fridge cornering at rung 5
## is the one awake moment of force. Mae in session has the glowing pink heart pupils (owner,
## 2026-11-11), and the prose says so at film night, as the original did.
##
## The ladder is AUTHORITY (whose hand is on the fridge rota). Days: a session evening (the rung),
## the overnight morning where it runs on (rungs 2-4), the waking day (Harry: residue, the detergent),
## then the next evening. From rung 6 Mae is the default. Owner, 2026-11-11: one optional chore a
## night from the act menu, its picture per the body that night; the rota and the app's
## notifications are Ren'Py screens. All route-local names carry the si_ prefix.

init -10 python:
    SI = "art/sister/"

    def _si_txt(s):
        return (s.replace("&mdash;", "—").replace("&ldquo;", "“").replace("&rdquo;", "”")
                 .replace("<i>", "{i}").replace("</i>", "{/i}"))

    # THE APP's own words, by rung (setup.sisterNotify), quoted from the source.
    SI_NOTIFY = [(1, 1, "Session 1 complete &mdash; Sister Level 1. New trait: smooth."),
        (1, 2, "Session 2 complete &mdash; Sister Level 2. New trait unlocked: Skin soft and sweet. Daily bath chores now unlocked. &ldquo;Family is what you make together!&rdquo;"),
        (2, 3, "Session 3 complete &mdash; Sister Level 3. New trait: nipple sensitivity unlocked! (Chores: morning problem now on daily rotation.)"),
        (2, 4, "Session 4 complete &mdash; Sister Level 4. New trait: Waist definition (permanent). Morning routine updated: &ldquo;Less laundry&rdquo; protocol active. Closet reorganisation: Sibling allocation locked. Schedule next session?"),
        (3, 5, "Session 5 complete &mdash; Sister Level 5. New trait: hips (permanent). Friend group witness mode: engaged. Social reality: reinforced. See you next session, little sister!"),
        (3, 6, "Session 6 complete &mdash; Sister Level 6. New trait: &ldquo;Minimize Attention&rdquo; &mdash; Sister's equipment has always been tiny, soft, and easy to ignore. Sisters share everything."),
        (4, 7, "Session 7 complete &mdash; Sister Level 7. New trait: Chest buds unlocked! All growth changes are now permanent. Signature look applied: red, long and loose (retroactive, persistent). Session summary: archived."),
        (4, 8, "Session 8 complete &mdash; Sister Level 8. New trait: Sensitivity tweak (nipples, chest, lips). Social fabric update: neighbourhood."),
        (5, 9, "Session 9 complete &mdash; Sister Level 9. New trait: Full chest unlocked! Titjobs added to sister chore rotation. &ldquo;Sisters help with everything, especially in the mornings. For best sister pride, repeat daily!&rdquo;"),
        (6, 10, "Session 10 complete &mdash; Sister Level 10. New trait: Dwindling achieved. Attention successfully minimized. Background Mode operating. Enjoy seamless sister support."),
        (7, 11, "Session Ended: Profile discrepancy resolved. Sister Level 11 &mdash; MAX Alignment. Body template finalized. Somatic permanence active. New trait: Proper anatomy (S-rank)."),
        (7, 12, "Session 12 complete &mdash; Sister Level 12. Profile adjustment detected: profiles merged. All memories integrated. New trait unlocked: Unbreakable bond."),
        (7, 13, "SISTER LEVEL: MAX. No further sessions required.")]

    # THE ROTA (setup.sisterRotaRows): each row, from the tier it goes up at, whose hand.
    SI_ROTA = [("bins", 2, "Bins", "PL"), ("kettle", 2, "Descale the kettle", "PL"), ("bath", 2, "Bath night", "PL"),
        ("morning", 2, "Morning problem: Mae", "PL"), ("sisterday", 3, "Sister Day", "NA"),
        ("weekends", 3, "Weekends: brunch (Witnesses)", "NS"), ("share", 3, "Sisters share everything", "PL"),
        ("braid", 4, "braid Sunday?", "M"), ("skincare", 4, "Skincare", "PL"),
        ("pride", 5, "Big sister's pride (Mae's idea)", "M"), ("pace", 6, "Mae sets the pace", "M"),
        ("harry", 6, "__HOUR__, Sunday mornings", "PL")]
    SI_ROTA_LINE = [
        "There's nothing on the fridge but the takeaway menus and a magnet from the chip shop.",
        "There's nothing on the fridge yet. The only record of anything is a notification on Paige's lock screen, and that's the app's.",
        "The rota's up on the fridge in Paige's handwriting, like any flatshare's: bins, the kettle, bath night, and {i}Morning problem: Mae{/i}, ticked and initialled {i}PL{/i}.",
        "The rota's grown a row in purple, Nell's: {i}Sister Day{/i}. The group chat books Mae's weekends now, and initials them.",
        "Halfway down the rota there's a line that isn't in Paige's hand: {i}braid Sunday?{/i} It's Mae's.",
        "There's a new row on the rota in green pen: {i}Big sister's pride (Mae's idea){/i}.",
        "The whole rota is in Mae's handwriting now, except one line in Paige's: {i}__HOUR__, Sunday mornings{/i}.",
        "The rota's down. Where it hung, there's a cheap frame with a screenshot in it.",
    ]
    SI_SESSION = [
        ["She doesn't ask. She hasn't, not once, since you said ten minutes. The tablet's in her lap before you've sat down, and her thumb's already on it.",
         "“Film night,” Paige says. It isn't a question. It hasn't been one since the first night."],
        ["There's no asking now. There never was, after the first night. The chime goes, she looks up, and the tablet's already pointed at you.",
         "“Session time,” she says, in the voice she uses to announce dinner, and turns the tablet round to face you."],
        ["It's on the rota now, between the bins and the kettle. Nobody finds that strange.",
         "Neither of you calls it a session out loud any more. It's just what the evening's for."],
    ]
    SI_BLEED = [[],
        ["You catch yourself sitting cross-legged on the sofa with your hands folded in your lap. Comfy, apparently.",
         "There's a hairpin in your hoodie pocket with a little lacquered flower on it. You drop it in the bathroom drawer.",
         "You say “big sis” out loud to an empty kitchen, laugh at yourself, and put the kettle on."],
        ["Your hand goes to the strawberry mug first. It isn't your mug. It's just the nicer mug.",
         "Your voice goes up when you answer Paige and stays up for a sentence and a half. Hay fever.",
         "You've started saying “mm!” instead of “yeah”. Nobody's mentioned it, so it's fine."],
        ["Someone at work says your name and there's a half-beat before it lands. Long week.",
         "You sign for a parcel and the first letter comes out as an M. Bad pen.",
         "You hum something all morning that you don't know the words to, and then sing the words."],
        ["You lay out two mugs in the morning without thinking. Paige drinks the second one, so that's fine.",
         "You can't remember last Tuesday, and the not-remembering is warm, like a radiator.",
         "Your reflection takes a second to place. Then it settles, and you go and put the kettle on."],
        ["Being anyone else has started to feel like the effort. Being Mae is the rest.",
         "There's a version of the last few months in your head that's wrong in every detail and very peaceful, and you like it better.",
         "You don't really do the noticing any more. It's nice not to."],
    ]
    # THE ACT MENU (setup.sisterActs): one optional chore a night (owner, 2026-11-11), each unlocking
    # with its rung; its picture follows the body that night (cg si_act_<key>_r<rung>).
    SI_ACTS = [("tea", 1, "Make the tea, then have your hair brushed"), ("bath", 1, "Bath night with big sis"),
        ("morning", 2, "Help with the morning problem"), ("laundry", 2, "The “less laundry” protocol"),
        ("share", 3, "Sisters share everything"), ("skincare", 4, "Skincare"),
        ("pride", 5, "Big sister's pride"), ("pace", 6, "Set the pace")]

    def si_init():
        if si.tier is None:
            si.tier = 0

    def si_advance(n):
        si.tier = max(si.tier or 0, n)

    def si_body(n):
        """The body takes row n (the morning after its session, as the source lands it)."""
        if (si.body or 0) >= n:
            return False
        si.body = n
        return True

    def si_notes(rung):
        return [(lv, _si_txt(b)) for r, lv, b in SI_NOTIFY if r == rung]

    def si_hour():
        return si_pc_name + " hour"

    def si_rota_line():
        t = 7 if si.rota_down else max(0, min(6, si.tier or 0))
        return SI_ROTA_LINE[t].replace("__HOUR__", si_hour())

    def si_rota_rows():
        t = max(0, min(6, si.tier or 0))
        rows = []
        for key, at, task, by in SI_ROTA:
            if t >= at:
                maes = t >= 6 and key != "harry"
                rows.append((task.replace("__HOUR__", si_hour()), "M" if maes else by,
                             min(7, 1 + t - at), key == "harry" and bool(si.harry_struck)))
        return rows

    def si_session_line():
        pool = SI_SESSION[2 if (si.tier or 0) >= 4 else 1 if (si.tier or 0) >= 2 else 0]
        return pool[(vn_clock.day or 0) % len(pool)]

    def si_bleed():
        pool = SI_BLEED[max(0, min(5, si.tier or 0))]
        return pool[(vn_clock.day or 0) % len(pool)] if pool else ""

    def si_acts():
        t = si.tier or 0
        return [(k, name) for k, at, name in SI_ACTS if t >= at]

    # ---- the stage --------------------------------------------------------------------------
    # The sprite: the body row (0-7) and the self ("h" Harry awake, "m" Mae in session).
    _si_have = {}

    def _si_has(n):
        if n not in _si_have:
            _si_have[n] = renpy.loadable(SI + n + ".png")
        return _si_have[n]

    def si_pc_file(face):
        r, m, fit = max(0, min(7, si.body or 0)), ("m" if si.mode == "mae" else "h"), si.fit
        names = []
        if fit:
            names += ["pc-r%d%s-%s-%s" % (r, m, fit, face), "pc-r%d%s-%s-neutral" % (r, m, fit)]
        names += ["pc-r%d%s-%s" % (r, m, face), "pc-r%d%s-neutral" % (r, m)]
        for n in names:
            if _si_has(n):
                return SI + n + ".png"
        return SI + names[-1] + ".png"

    def si_face_now():
        a = renpy.get_attributes("si_pc")
        return a[0] if a else "neutral"

    def _si_portrait(st, at):
        p = vn_art_file(si_pc_file(si_face_now()))
        crops = globals().get("sister_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["sister"] = lambda: DynamicDisplayable(_si_portrait)

    # The calendar the prose keeps (2026-11-12: the counter has to agree with the story). Day 1 is a
    # Wednesday, bath night (the epilogue's "Bath night is Thursday" is how it ends up); brunch on
    # the Saturday, the jeans morning a lie-in Sunday ("a chiropractor for Monday"); Sister Day the
    # Saturday after ("Mae's weekends"), the photo wall its Sunday morning ("You went with them
    # yesterday"); Paige's office day the Thursday after ("You can't remember last Tuesday"); Harry
    # hour the Sunday after next ("You must have written it last week"), then a week, Sunday again.
    SI_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def si_weekday_name():
        return SI_WD[(3 + vn_clock.day - 1) % 7]    # day 1 is a Wednesday

    vn_weekdays["sister"] = si_weekday_name

    vn_sprite_image("si_pc", ("neutral", "puzzled", "eager", "beaming", "blissful"), si_pc_file, who="pc")
    vn_sprite_image("si_paige", ("warm", "wicked", "soft"), lambda f: SI + "paige-" + f + ".png")
    for _w in ("nell", "natalie", "amber", "kate"):
        vn_sprite_image("si_" + _w, ("neutral", "smile"), (lambda w: (lambda f: SI + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(SI) and _f.endswith(".jpg"):
            _n = _f[len(SI):-4]
            vn_register_bg("si_" + _n.replace("-", "_"), _f)
            vn_register_cg("si_" + _n.replace("-", "_"), _f)

    # Vanripper only (owner, 2026-11-12 about 1:56 pm ET: the Abarus alternate set is for femboy,
    # feminization and soft-TSF routes; sister is full TSF)

    vn_register_route("sister", "Little Sister Mode",
        "Paige is not your sister. You met at nineteen in a house share above a chip shop, and you've shared flat 2C for six years. On film night she's comfortably drunk and shows you an app with a pink rabbit on it: Imouto+, the family you deserve. She always wanted a little sister. You say ten minutes, as a joke. After that night she never asks again.",
        SI + "cover.jpg", "sister_start")

    achievement.register("Sister Level MAX")
    achievement.register("Unbreakable Bond")

default si = VNState(tier=0, body=0, mode="waking")
default si_enc = VNState(partner_came=True, pc_orgasms=0)
default si_pc_name = "Harry"
default si_note_lines = []

define si_harry = VNChar("[si_pc_name]", who="pc", plate="#4f7bb0")
define si_mae = VNChar("Mae", who="pc", plate="#e0559a")
define si_paige = VNChar("Paige", who="si_paige", plate="#7a4fb3")
define si_bigsis = VNChar("Big sis", who="si_paige", plate="#7a4fb3")
define si_nell = VNChar("Nell", who="si_nell", plate="#9b5fc4")
define si_natalie = VNChar("Natalie", who="si_natalie", plate="#4f9b8f")
define si_amber = VNChar("Amber", who="si_amber", plate="#c47a3f")
define si_kate = VNChar("Kate", who="si_kate", plate="#5f7fc4")
define si_shop = VNChar("The corner-shop man", who="shop", plate="#6b6b78")

style si_hypno:
    color "#ff8fd0"
    bold True

## THE APP (Imouto+): its notifications on a phone card over the picture, quoted word for word.
screen si_app(lines):
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 760
        padding (26, 18)
        background Frame(Solid("#2a1a2eee"), 0, 0)
        vbox:
            spacing 10
            text "{color=#ff8fd0}{b}Imouto+{/b}{/color}  {size=-6}{color=#b7b7b7}pink rabbit{/color}{/size}" size 26
            for t in lines:
                text t size 22 color "#f6e6f2"

## THE ROTA on the fridge, in its hands: ticks and initials, never stars or grades.
screen si_rota():
    zorder 60
    frame:
        xalign 0.5 ypos 60 xsize 700
        padding (30, 22)
        background Frame(Solid("#f7f1e3f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}2C{/b}" size 24 color "#3a3a3a"
            for task, by, ticks, struck in si_rota_rows():
                hbox:
                    spacing 14
                    text (("{s}%s{/s}" % task) if struck else task) size 22 color ("#2d7a3a" if task.startswith("Big sister") else "#6a3f9b" if task == "Sister Day" else "#c2508f" if by == "M" else "#2a2a2a") xsize 430
                    text ("✓ " * ticks).strip() size 20 color "#2a2a2a" xsize 150
                    text by size 20 color "#555555"

## Route select's entry: film night, a Friday, rain on the window.
label sister_start:
    $ si = VNState(tier=0, body=0, mode="waking")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=20, minute=0)
    ## the HUD and the box portrait key on vn_route (twinetesting-03 spotted it unset, 2026-11-12)
    $ vn_route = "sister"
    $ si_pc_name = "Harry"
    if not renpy.session.get("vn_picks"):
        $ si_pc_name = renpy.input("Your name? (Harry, unless you'd like another.)", default="Harry", length=20).strip() or "Harry"
    jump si_opening

label si_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"sister"}
    $ vn_route = None
    hide screen si_app
    hide screen si_rota
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e0559a}Sister Level MAX{/color}{/size}\n\n{i}The end.{/i}"
    jump start
