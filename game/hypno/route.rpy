## Open and Listen -- the catalog's hypno route (the Ren'Py port, 2026-11-11). Ported from
## catalog/game/02-engine/storylines/hypno/: hypno.js (the ladder, the pacing rule, the banks),
## widgets.twee, vn-stage.js (the stage) and the four .twee files. The passages are script.rpy
## (converted once by tools/twee2rpy.py: the source now); the hub and the session dispatcher are
## hub.rpy; the five sex scenes DoL's combat engine ran are written out in encounters.rpy.
##
## Two people, one body (vn-stage.js): Ethan AWAKE (faces neutral, nervous, happy: no glow) and
## Emily in TRANCE (faces trance, eager: the glowing pink heart pupils, the owner's trance tell).
## The body is the tier. Every sex scene happens in trance, as Emily, and the violation is the
## premise, said in the prose: Liam never asks, Ethan never agreed, the six words do it (revamp,
## owner 2026-10-20). Awake, Ethan remembers nothing; no sex happens while he's awake.
##
## The route plays linear, as the VN does: the hub's flavour links (the Bell, sitting with Liam,
## the vanity) are free play's and aren't ported; the pill and the Bloom stay, they move the story.
## All route-local names carry the hy_ prefix.

init -10 python:
    HY = "art/hypno/"

    # THE CLOCK: the hub's first line, keyed on the tier (hypno.js hypnoRanks).
    HY_RANKS = ["nothing yet", "fifteen minutes", "an evening", "the whole night", "a night and a day",
                "a lost weekend", "it does not end"]

    # Where each rung's session starts (hypno.js hypnoRungs).
    HY_RUNG_LABEL = {1: "hy_first", 2: "hy_name", 3: "hy_stay", 4: "hy_master", 5: "hy_out", 6: "hy_fork"}

    # The rung's one loud line when its body lands (hypnoBody[n].sensLine).
    HY_SENS = [None,
        "Your mouth's soft and strange, like you've been talking in your sleep. You lick your lips and shiver all the way down.",
        "Your jaw's loose and warm, and your tongue keeps finding the roof of your mouth. Every time it does, your cock twitches. \"{i}Hnn{/i}.\"",
        "Your throat hums. Every swallow still tastes of him, and every swallow makes you moan out loud.",
        "Your lips part on their own when his door opens. Your buds pebble against your shirt. Your ass clenches on nothing, hungry.",
        "Your mouth tingles every time you smile now. Your ass is so sensitive that sitting down is foreplay. You squirm, and gasp, and squirm again.",
        "Your lips, your buds, your ass: all of it hums, all the time now, like it's waiting for him.",
    ]

    # THE FULL REGIMEN (owner, 2026-11-11: "would it be possible to add a route to hypno which gives
    # large tits?"). At the Bloom consult Emily goes off Liam's script and asks for everything
    # (hy.full); from the hinge the chest grows where the soft regimen holds it at buds: rung 3
    # small, 4 medium-large, 5 large, 6 large-plus (step 6 of route-covers/breast-scale.html).
    # Everything else is the soft route's: the ass and thighs, the cage, the tails, the kept cock,
    # the three endings. The art: pc-r<n>f-* sprites and <picture>-full.jpg twins (hy_pc_file,
    # _hy_full_of), drawn by the scene-art pipeline from the soft pictures' prompts and seeds.
    HY_SENS_FULL = {
        4: "Your lips part on their own when his door opens. Your breasts ache against your shirt, heavier than they were this morning. Your ass clenches on nothing, hungry.",
        6: "Your lips, your breasts, your ass: all of it hums, all the time now, like it's waiting for him.",
    }

    # What you wake to on the full regimen, added to the fog's band from the hinge on: the chest,
    # explained wrongly like everything else.
    HY_RESIDUE_FULL = {
        3: ["Your work shirt won't button across your chest. It must have shrunk in the wash. Everything's been shrinking in the wash lately."],
        4: ["You wake with one hand cupped round your own breast, holding it like something you're keeping safe. You let go. Then, after a while, you don't."],
        5: ["You roll over and they roll with you, warm and heavy, and you smile into the pillow before you remember to wonder why."],
    }

    # THE METRONOME: your bedroom, redecorated between sessions (hypnoRoom), by the tier.
    HY_ROOM = ["",
        "Liam's white tee is folded over the back of your desk chair, the tight one. You don't remember borrowing it.",
        "There's a stack of his fitted briefs in your top drawer, folded in with your own things as though they always have been.",
        "A vanity under the window now: mirror, bottles, a drawer of pastel panties, and the platinum twin-tail extensions on a stand, brushed out and waiting.",
        "The nightstand drawer has a bottle of lube in it now, and a pink plug, washed, on a folded cloth, put back exactly where it lives.",
        "Shopping bags you don't remember carrying sit by the wardrobe. The gold heels are under the vanity. Lingerie hangs off the drawer pulls by its straps, as if someone was choosing.",
        "The extensions are in a drawer now, wrapped in tissue. You don't need them. The hair in the mirror is your own.",
    ]

    # WHAT YOU WAKE TO, banded by the fog (hypnoResidue): always physical, always explained wrongly.
    HY_RESIDUE = [[],
        ["Your shirt is folded on the chair. You don't fold things. You must have been tidier than usual.",
         "There's a glass of water by the bed that you don't remember pouring, and it's still cold. You drink it.",
         "\"Morning,\" you say, and it comes out a bit higher than you meant. Must be a cold coming."],
        ["Your jaw feels loose and warm. You must have been grinding your teeth again.",
         "The clock says hours later than the last thing you remember. You've been tired lately. Everyone says so, mostly Liam.",
         "Your knees are pink in the way that kneeling makes and nothing else does. The gym, probably."],
        ["There's lip gloss on the rim of a mug in the sink, berry pink. Liam must have had someone over.",
         "There's a hair tie on your wrist, pink, with a little plastic heart. Liam's girlfriend's, probably. Does Liam have a girlfriend?",
         "Something in the laundry isn't yours and is folded in with your things like it always has been. Liam's, probably."],
        ["You wake on the floor at the foot of the bed, curled up on the rug like a cat. Sleepwalking again.",
         "Your mouth tastes of something salty you have no word for. Crisps, probably. You rinse and go to work.",
         "There are panties in your sock drawer. Lilac, with a bow. Laundry mix-up. You put them back in exactly the same place."],
        ["You don't remember waking. There was no edge. Just the room, and being who you are today.",
         "Time comes in blocks now. The kitchen. The door. Kneeling. None of it has a before, and none of it needs one.",
         "Your reflection takes a moment to place. Then it settles, and you smile at her, and she smiles back."],
    ]

    # The approach (hypnoSessionLines): Ethan's last waking minute of the evening.
    HY_SESSION = [
        ["He waits until you're settled and half-watching something, and then he says it, too quickly, the way you say a line you've rehearsed.",
         "His thumb is on his phone before he speaks. You look up because he said your name, and then he says the rest of it.",
         "He asks if you're tired. You say a bit. He says good, and then he says the other thing."],
        ["He doesn't ask anything any more. He waits for the chime, and for your eyes to find it, and then he speaks.",
         "You hear the chime through the wall and your feet are already taking you to the end of the bed. Comfy there. That's all.",
         "He says it in the middle of a sentence about something else entirely, and the sentence never gets finished."],
    ]

    # The trigger, verbatim from the source. Never paraphrased; always in the hypnosis styling.
    HY_TRIGGER = "Open and listen, now."

    # ---- the ladder and the clock (hypno.js window.Hypno) ---------------------------------
    def hy_init():
        if not hy.intro:
            hy.intro = True
        store.vn_route = "hypno"

    def hy_now():
        c = vn_clock
        return c.day * 1440 + c.hour * 60 + c.minute

    def hy_weekday(day=None):
        """DoL's Time.weekDay: 1 is Sunday, 7 Saturday. The route starts on HY_WEEKDAY0."""
        d = vn_clock.day if day is None else day
        return (HY_WEEKDAY0 - 1 + d) % 7 + 1

    def hy_advance(n):
        """A rung's session has begun: the clock moves (up only)."""
        hy.tier = max(hy.tier or 0, n)
        store.hy_enc = VNState(ran=False, partner_came=True, pc_orgasms=0)

    def hy_start():
        hy.start_day = vn_clock.day
        hy.doses = (hy.doses or 0) + 1
        hy.last_dose = vn_clock.day

    def hy_end():
        hy.ended_at = hy_now()
        hy.last_dose = vn_clock.day

    def hy_evening():
        return vn_clock.hour >= 19

    def hy_since_end():
        return 10 ** 9 if hy.ended_at is None else hy_now() - hy.ended_at

    def hy_next_rung():
        t = hy.tier or 0
        if hy.done or t >= 6:
            return 0
        if t == 2 and not hy.rx:
            return 0    # the hinge waits for the Bloom
        if t == 4 and hy_weekday() not in (6, 7):
            return 0    # a lost weekend starts on a Friday or Saturday night
        if vn_clock.day < HY_RUNG_DAY.get(t + 1, 0):
            return 0    # not yet: the calendar the prose keeps (HY_RUNG_DAY)
        return t + 1

    def hy_due():
        """Is a session due now? Evening, none started today, the last one well behind you."""
        if not hy.intro or hy.done or not hy_evening():
            return False
        if hy.start_day == vn_clock.day:
            return False
        if hy_since_end() < 10 * 60:
            return False
        if hy_next_rung():
            return True
        return (hy.tier or 0) == 2 and not hy.rx

    def hy_to_tomorrow(h):
        return (24 - vn_clock.hour + h) * 60 - vn_clock.minute

    def hy_to_tonight(h):
        c = vn_clock
        return (h - c.hour) * 60 - c.minute if 5 <= c.hour < h else 0

    def hy_until(h):
        m = hy_to_tonight(h)
        if m > 0:
            vn_pass(m)

    def hy_to_monday(h):
        days = (2 - hy_weekday() + 7) % 7
        if days == 0:
            days = 7
        return (days - 1) * 24 * 60 + hy_to_tomorrow(h)

    def hy_to_weekday(wd, h):
        """Minutes to the next weekday wd (DoL's numbering, 1 is Sunday) at hour h; today counts
        while h is still ahead."""
        c = vn_clock
        now = c.hour * 60 + c.minute
        days = (wd - hy_weekday() + 7) % 7
        if days == 0 and now >= h * 60:
            days = 7
        return days * 1440 + h * 60 - now

    def hy_gap_days():
        """Whole days to sleep through, from a morning hub, before the next rung's first day
        (HY_RUNG_DAY): the days of the same the prose counts on. Only the tiers with a bridge line
        (HY_HUB_GAP); tier 4 waits for its Friday at night (hy_weekend_skip_days)."""
        t = hy.tier or 0
        if hy.done or t not in HY_HUB_GAP:
            return 0
        return max(0, HY_RUNG_DAY.get(t + 1, 0) - vn_clock.day)

    def hy_weekday_name():
        return HY_WEEKDAY_NAME[hy_weekday()]

    def hy_weekend_skip_days():
        """At tier 4 the weekday nights before Friday sleep straight through (Hypno.weekendSkipDays)."""
        if (hy.tier or 0) != 4 or hy.done:
            return 0
        hours = ((8 - vn_clock.hour + 24) % 24) or 24
        wake = hy_weekday((hy_now() + hours * 60) // 1440)
        return 0 if wake >= 6 else 6 - wake

    def hy_clock():
        """The time the way you'd say it: the only number the prose is allowed."""
        words = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
        m = int(round(vn_clock.minute / 5.0) * 5)
        h = vn_clock.hour % 12
        if m == 60:
            m, h = 0, (h + 1) % 12
        nxt = words[(h + 1) % 12]
        if m == 0:
            return words[h] + " o'clock"
        if m == 15:
            return "quarter past " + words[h]
        if m == 30:
            return "half " + words[h]
        if m == 45:
            return "quarter to " + nxt
        if m in (5, 10, 20, 25):
            return ["", "five", "ten", "", "twenty", "twenty-five"][m // 5] + " past " + words[h]
        return ["", "", "", "", "", "", "", "twenty-five", "twenty", "", "ten", "five"][m // 5] + " to " + nxt

    def hy_induct(cap=4):
        """<<sl_induct>>: the Amnesia Loop's band goes up a step a session, to its cap."""
        hy.fog = 1 if not hy.fog else min(cap, hy.fog + 1)

    def hy_bank(bank, band):
        """<<app_bank>>: a line from the band, never the same one twice running."""
        pool = bank[max(0, min(len(bank) - 1, band))]
        if not pool:
            return ""
        i = renpy.random.randint(0, len(pool) - 1)
        if len(pool) > 1 and i == hy.bank_last:
            i = (i + 1) % len(pool)
        hy.bank_last = i
        return pool[i]

    def hy_residue():
        if (hy.fog or 0) < 1:
            return ""
        bank = HY_RESIDUE
        if hy.full and hy_rung() >= 3:
            bank = [pool + HY_RESIDUE_FULL.get(i, []) for i, pool in enumerate(HY_RESIDUE)]
        return hy_bank(bank, hy.fog)

    def hy_session_line():
        return hy_bank(HY_SESSION, 1 if (hy.doses or 0) >= 2 else 0)

    def hy_body(n):
        """<<hypno_body n>>: the rung's body lands; its one loud line, the first time."""
        if (hy.body or 0) >= n:
            return None
        hy.body = n
        return HY_SENS_FULL.get(n, HY_SENS[n]) if hy.full else HY_SENS[n]

    def hy_pill():
        """The Bloom's daily estradiol: once a day, once it's prescribed. True if taken now."""
        if hy.rx and hy.pill_day != vn_clock.day:
            hy.pill_day = vn_clock.day
            return True
        return False

    # ---- the stage (vn-stage.js) ----------------------------------------------------------
    def hy_rung():
        return max(1, min(6, hy.tier or 0))

    def hy_row():
        """The sprite's row: the body as it has landed (hy_body), never a rung's session ahead of
        it. The platinum tails show from the moment Liam clips them in on rung 3's night (hy.tails),
        a step before rung 3's body lands the morning after (owner, 2026-11-12: "make sure sprite
        changes happen at the right time"; the tails had shown from the start of the night)."""
        b = hy.body or 0
        if hy.tails:
            b = max(b, 3)
        return max(1, min(6, b))

    _hy_have = {}

    def _hy_has(n):
        if n not in _hy_have:
            _hy_have[n] = renpy.loadable(HY + n + ".png")
        return _hy_have[n]

    def hy_pc_file(face):
        """The sprite that exists: the outfit set with this face, the outfit set with the default
        face, the plain body with this face, the default (vn-screen.js sprite())."""
        r, fit = hy_row(), hy.fit
        # the full regimen's body from the hinge on (pc-r<n>f-*), then the soft one's
        rungs = ["%df" % r, "%d" % r] if (hy.full and r >= 3) else ["%d" % r]
        # his own long brown hair from the days after rung 5, before rung 6's body (the hub's gap
        # line: "the platinum extensions go in a drawer"): pc-r5o-* / pc-r5fo-*, falling back to r5
        if hy.own_hair and r == 5:
            rungs = ["%so" % k for k in rungs] + rungs
        names = []
        for k in rungs:
            if fit:
                names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-neutral" % (k, fit)]
            names += ["pc-r%s-%s" % (k, face), "pc-r%s-neutral" % k]
        for n in names:
            if _hy_has(n):
                return HY + n + ".png"
        return HY + names[-1] + ".png"

    def hy_face_now():
        a = renpy.get_attributes("hy_pc")
        return a[0] if a else "neutral"

    def _hy_portrait(st, at):
        p = vn_art_file(hy_pc_file(hy_face_now()))
        x, y, w, h = vn_face_crop(hypno_face_crops, p)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["hypno"] = lambda: DynamicDisplayable(_hy_portrait)

    vn_sprite_image("hy_pc", ("neutral", "nervous", "happy", "trance", "eager"), hy_pc_file, who="pc")
    vn_sprite_image("hy_liam", ("neutral", "smile", "stern"), lambda f: HY + "liam-" + f + ".png")
    vn_sprite_image("hy_mike", ("neutral",), lambda f: HY + "mike-" + f + ".png")
    vn_sprite_image("hy_cass", ("neutral",), lambda f: HY + "cass-" + f + ".png")
    vn_sprite_image("hy_ruth", ("neutral",), lambda f: HY + "ruth-" + f + ".png")

    # The full regimen's twin of a picture: art/hypno/<name>-full.jpg (a scene-art picture's twin
    # too: scenes/kneel.jpg -> kneel-full.jpg), shown in its place while hy.full is on. A picture
    # with no twin (a room, the pill, a face close-up) is the same in both.
    _hy_twin = {}

    def _hy_full_of(path):
        if not hy.full:
            return path
        if path not in _hy_twin:
            t = HY + path.rsplit("/", 1)[-1][:-4] + "-full.jpg"
            _hy_twin[path] = t if renpy.loadable(t) else None
        return _hy_twin[path] or path

    def _hy_cg_dd(st, at, path):
        return vn_cg(vn_art_file(_hy_full_of(path))), None

    def _hy_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_hy_full_of(path))), None

    # Every picture in the route's folder is a background and a CG by name ("bg hy_bedroom",
    # "cg hy_trigger_first"); the scene-art pictures are CGs as "cg hy_sa_<name>". As
    # vn_register_cg/vn_register_bg do, through the full regimen's twins.
    for _f in renpy.list_files():
        if _f.startswith(HY) and _f.endswith(".jpg"):
            _n = _f[len(HY):-4]
            if _n.endswith("-full"):
                continue
            if _n.startswith("scenes/"):
                vn_cg_files["hy_sa_" + _n[7:]] = _f
                renpy.image(("cg", "hy_sa_" + _n[7:]), DynamicDisplayable(_hy_cg_dd, _f))
            else:
                _k = "hy_" + _n.replace("-", "_")
                vn_cg_files[_k] = _f
                renpy.image(("cg", _k), DynamicDisplayable(_hy_cg_dd, _f))
                renpy.image(("bg", _k), DynamicDisplayable(_hy_bg_dd, _f))
    # each twin is a gallery picture of its own: "<picture>_full"
    for _k, _f in list(vn_cg_files.items()):
        if _k.startswith("hy_") and renpy.loadable(HY + _f.rsplit("/", 1)[-1][:-4] + "-full.jpg"):
            vn_cg_files[_k + "_full"] = HY + _f.rsplit("/", 1)[-1][:-4] + "-full.jpg"

    # Two art sets, one per style (owner, 2026-11-10: "generate two versions of the story, one
    # for each style ... also a toggle between them"): Vanripper the default, Abarus by the HUD's
    # Art button, per save (hypno.js artSets).
    vn_register_art_sets("hypno", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("hypno", "Open and Listen",
        "You and Liam were best friends as kids, and then he wasn't anywhere for years. Since the spring his room has been through your bedroom wall, and he's still the one standing slightly behind you. One night he finds an app with six words in it. Under it, you're Emily, and Emily will do anything he says. Awake, you don't remember a thing.",
        HY + "cover.jpg", "hypno_start")

    vn_weekdays["hypno"] = hy_weekday_name
    achievement.register("Open and Listen")
    achievement.register("The Session That Never Ends")

## The day the route starts on (2026-11-12: the counter has to agree with the story, owner: "stretch
## the clock"): day 1 is a Tuesday, league night. Ethan's football is on Tuesdays ("You missed league
## on Tuesday"; Mike's "missed u at league again"), and day 0 is gone from the corner. hy_weekday(1)
## is DoL's 3 (Tuesday).
define HY_WEEKDAY0 = 2

## The calendar the prose keeps: the first day each rung may start on. Rung 1 is the opening night
## and rung 2 the next; then a week of days of the same, so the Bloom (and rung 3 that night) falls
## the morning after league is missed; rung 4 the Monday after ("It was snug last week"); rung 5 that
## Friday (the tier-4 night skip waits for it); Monday's alarm on day 21; rung 6 a week on ("The
## extensions have been in a drawer for a week"). The hub sleeps through the gaps (hy_gap_days) on
## one line each (HY_HUB_GAP). The Listen week walks its own days (script.rpy, hy_listen_week).
define HY_RUNG_DAY = {1: 1, 2: 2, 3: 9, 4: 14, 5: 18, 6: 28}
define HY_WEEKDAY_NAME = ["", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

default hy = VNState(tier=0, fog=0, doses=0)
default hy_enc = VNState(ran=False, partner_came=True, pc_orgasms=0)
default hy_pc_name = "Ethan"

## The hypnosis styling (DoL's .hypno-text: the violet-to-pink gradient), for the six words and
## every command said under them.
style hy_hypno:
    color "#d58cff"
    bold True

## The VN script's speakers (vn-stage.js `names`): Ethan awake under his own name; Emily in trance
## is the same body and sprite under hers, plated pink ("You" before she names herself).
define hy_ethan = VNChar("[hy_pc_name]", who="pc", plate="#4a6fa5")
define hy_emily = VNChar("Emily", who="pc", plate="#e0559a")
define hy_her = VNChar("You", who="pc", plate="#e0559a")
define hy_liam = VNChar("Liam", who="hy_liam", plate="#6a4fb3")
define hy_mike = VNChar("Mike", who="hy_mike", plate="#3f8a4f")
define hy_cass = VNChar("Cass", who="hy_cass", plate="#c27a2c")
define hy_ruth = VNChar("Dr. Adair", who="hy_ruth", plate="#3a8f96")
define hy_unk = VNChar("???", who="???", plate="#6b6b78")

## Route select's entry. The route starts at noon on day 1, a Tuesday (HY_WEEKDAY0; 2026-11-12, the
## counter agrees with the story); the opening sets the clock to ten to ten that night, league night.
label hypno_start:
    $ hy = VNState(tier=0, fog=0, doses=0)
    $ hy_enc = VNState(ran=False, partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=12, minute=0)
    $ hy_pc_name = "Ethan"
    ## the name box (DoL's New Game card): Ethan, unless you'd like another. Emily's name is hers,
    ## and she gives it herself. A test walk (game/tests/) keeps Ethan.
    if not renpy.session.get("vn_picks"):
        $ hy_pc_name = renpy.input("Your name? (Ethan, unless you'd like another.)", default="Ethan", length=20).strip() or "Ethan"
    jump hy_opening

## The end of the route (<<hypno_return>>: "Choose another story").
label hy_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"hypno"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e0559a}Open and Listen{/color}{/size}\n\n{i}The end.{/i}"
    ## "Choose another story" (vn.twee's <<route_return>>): back to the route select
    jump start

## The test trace's view of the stage (game/catalog/vntrace.rpy): the PC sprite file, the cast
## sprite as "who face", the outfit set.
init 110 python:
    def _hy_trace():
        pc = hy_pc_file(hy_face_now()).rsplit("/", 1)[-1] if renpy.showing("hy_pc") else None
        cast = None
        for tag in ("hy_liam", "hy_mike", "hy_cass", "hy_ruth"):
            if renpy.showing(tag):
                cast = tag[3:] + " " + " ".join(renpy.get_attributes(tag) or ())
        return pc, cast, hy.fit

    vn_trace_routes["hypno"] = _hy_trace

## The gallery's full-regimen pictures: each twin right after its picture (gallery.rpy lists the
## pictures the script shows; the show statements name the soft one), counted as seen once its
## picture has been shown on the full regimen.
init 11 python:
    def _hy_gallery_twins():
        out = []
        for n in vn_gallery.get("hypno", []):
            out.append(n)
            if n + "_full" in vn_cg_files:
                out.append(n + "_full")
        vn_gallery["hypno"] = out

    _hy_gallery_twins()

    def _hy_mark_twins():
        if getattr(store, "vn_route", None) != "hypno" or not getattr(getattr(store, "hy", None), "full", None):
            return
        a = renpy.get_attributes("cg", layer="cgl")
        if a and a[0] + "_full" in vn_cg_files and not renpy.seen_image(("cg", a[0] + "_full")):
            renpy.mark_image_seen(("cg", a[0] + "_full"))

    config.start_interact_callbacks.append(_hy_mark_twins)
