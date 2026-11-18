## Cleo -- "He's Been Making Me Into His Ex, and Lately She's Not Quite His Ex Anymore" (rewritten
## straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner about
## 8:50 pm ET). From the StoryNexus shelf book 3d8b9866 (M16), whose export isn't on this machine: the
## source is its package, kept verbatim in catalog/docs/routes/vn-original/cleo/package.md.
##
## THE NON-CON PASS, "the wrong line" (owner, 2026-11-12, as signed off): every Friday Danny surfaces
## inside her at the moment Nate holds her, aware and unwilling, and says no in her voice. Weeks 1-2
## Nate hears a line Steph never said and corrects it ("That's not how she said it"); from week 3 he
## hears Cleo's new way of talking, delighted. Nobody stops, and Nate is never a villain: he never
## knows. The body keeps her warmth and her moves. Each week ends loud and begging, and Danny sinks
## back under; Saturday he has a dream and blames the pizza. Week 5 breaks into begging mid-ride; week
## 6 he surfaces and asks, and "I am" is his. No tears, no menace, no pain, no escape.
##
## The book's rules kept: a cast of two in one flat; Danny's kitchen first, then "It's Friday", then
## the session in her voice to the end of the week, mid-act; the edit ladder and Danny's advice as
## its ratchet; the fridge, never a count; femboy, not TSF: his cock stays, in session she has a chest
## and Danny never does; the ass and thighs are the ladder; the week-4 non-decision, silent; Danny
## never finds out. Steph never appears. All route-local names carry cle_.
##
## THE ALTERNATE ROUTES (owner, 2026-11-13 about 1:37 pm ET, signed off from c9's proposal; lanes.rpy): cle.lane
## "bra" (3a, Something in her size: from week 6 Danny has Cleo's chest and then some, the house cap; his rows 6b, twins <name>-b.jpg) and "stay"
## (3b, Ask her to stay: a new weekend in Cleo's voice, TSF by Sunday night; her sprites pc-r6-* then pc-r7-*,
## the art map's Cleo rows w6, w7). Each fork is
## marked as deciding the ending; they're exclusive (the week-6 fork isn't offered on 3a). Alternate-route art last.

init -10 python:
    CLE = "art/cleo/"

    # The two alternate routes open once their art has landed (nqalt/120 cleA1, 121 cleA2, queued after every main
    # queue): until then week 5 and week 6 offer only the canon choice, so nobody plays a lane with no pictures
    # (QA ab710ca6: the lanes' sprites and CGs were missing; camellia's CAM_REAL_READY is the model)
    CLE_BRA_READY = all(any(f.startswith(CLE + k) for f in renpy.list_files()) for k in ("pc-r6b-", "bra-kettle", "six-tits"))
    CLE_STAY_READY = all(any(f.startswith(CLE + k) for f in renpy.list_files()) for k in ("pc-r7-", "stay-sofa", "stay-first"))

    # THE FRIDGE: one line a week, in Danny's scene (never a count).
    CLE_FRIDGE = [None,
        "Steph, all of it. Four years of her in clothed snapshots: Steph on a beach, Steph in a bobble hat, Steph laughing at something off the edge of the photo, a sleek lavender bob in every one.",
        "Steph, nearly all of it, and in the middle of her a new one: a woman who could be her twin, lavender bob and all, smiling at the camera like she means it.",
        "Steph, a bit less of her, and another of the new woman. Almost the same woman as last week. Almost. Her hair's softer at the ends.",
        "The new woman goes up in the middle of the fridge, not at the edge. Her bob's grown out past her jaw into loose waves, and Nate's put her right where you'd see her first.",
        "Two of Steph come down this week, and two of the new woman go up: one in a dressing gown on Nate's sofa, one laughing so hard she's out of focus.",
        "All her. Cleo in a woolly hat, Cleo asleep on the sofa, Cleo pulling a face at the toaster. Not one Steph left.",
    ]

    # What last Friday kept, for the residue beat at the top of each week (shown as an event).
    CLE_KEEPS = [None, None,
        "the hair on your arms is gone. All of it. Your arms are slimmer, smooth as a peeled egg",
        "your skin's gone soft all over, and when the radio says something stupid you laugh, light and bright, and it isn't your laugh",
        "your jeans have stopped working. Tight across the seat, gaping at the small of your back",
        "your belt sits differently. Your hips have come out and your waist's come in",
        "your thighs are heavy and your voice is lighter, and this time none of it's going back",
    ]

    # The advice, one a week (week 1: none, only concern). The words never change; only how you put it.
    CLE_ADVICE = [None, None,
        "She does look a lot like her, you know. But you can't just recreate her. That isn't moving on.",
        "If you're seeing someone, actually be there with her. Otherwise she's just a stand-in.",
        "Stop calling her by somebody else's name.",
        "Let her keep some things here. It's been months. If she's coming round anyway, it looks like she's staying.",
        "You should take the photos down.",
    ]

    # Her name in Nate's mouth: Steph until week 4's session, then Cleo.
    def cle_named():
        return cle.named

    def cle_body(row):
        """Danny's body takes the week's row, toward it and never back."""
        cle.row = str(max(int(cle.row or 1), int(row)))

    # ---- the stage --------------------------------------------------------------------------
    # Danny out of session: rows 1-6 (what each Friday kept). Outfits "own" (a t-shirt and jeans),
    # "apron" (the same with his apron on). Cleo in session: weeks 1-6, her look drifting a little
    # each week; outfits "steph" (Steph's grey cardigan over a camisole and jeans), "stockings" (week
    # 4: black stockings and a garter belt), "gown" (week 5: the dressing gown over the things he
    # bought), "nude". One sprite tag; cle.on picks whose body.
    _cle_have = {}

    def _cle_has(n):
        if n not in _cle_have:
            _cle_have[n] = renpy.loadable(CLE + n + ".png")
        return _cle_have[n]

    def cle_pc_file(face):
        if cle.on:
            w, fit = cle.week or 1, cle.fit or "steph"
            names = ["pc-r%s-%s-%s" % (w, fit, face), "pc-r%s-%s-warm" % (w, fit),
                     "pc-r%s-nude-%s" % (w, face), "pc-r%s-nude-warm" % w]
        else:
            r, fit = cle.row or "1", cle.fit or "own"
            # 3a: Danny with Cleo's chest (row 6b) first, then the canon row's
            rows = [r + "b", r] if (cle.lane == "bra" and cle.chest) else [r]
            names = []
            for k in rows:
                names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-cheerful" % (k, fit),
                          "pc-r%s-own-%s" % (k, face), "pc-r%s-own-cheerful" % k]
        for n in names:
            if _cle_has(n):
                return CLE + n + ".png"
        return CLE + names[-1] + ".png"

    def cle_face_now():
        a = renpy.get_attributes("cle_pc")
        return a[0] if a else ("warm" if cle.on else "cheerful")

    def _cle_portrait(st, at):
        p = vn_art_file(cle_pc_file(cle_face_now()))
        crops = globals().get("cleo_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["cleo"] = lambda: DynamicDisplayable(_cle_portrait)

    # The calendar: day 1 is a Friday; a week a chapter.
    CLE_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def cle_weekday_name():
        return CLE_WD[(5 + vn_clock.day - 1) % 7]    # day 1 is a Friday

    def cle_to_friday(h=19):
        """Minutes from now to the next Friday at hour h, at least a day on."""
        cur = (5 + vn_clock.day - 1) % 7
        days = (5 - cur) % 7 or 7
        return days * 24 * 60 + (h - vn_clock.hour) * 60 - vn_clock.minute

    vn_weekdays["cleo"] = cle_weekday_name

    vn_sprite_image("cle_pc", ("cheerful", "concerned", "sleepy", "flushed", "warm", "laughing", "protesting", "begging"), cle_pc_file, who="pc")
    vn_sprite_image("cle_nate", ("sad", "dry", "happy"), lambda f: CLE + "nate-" + f + ".png")

    # 3a's twin of a picture: <name>-b.jpg, shown in its place on cle.lane "bra" (the hypno full regimen's way).
    _cle_twin = {}

    def _cle_b_of(path):
        if cle.lane != "bra":
            return path
        if path not in _cle_twin:
            t = path[:-4] + "-b.jpg"
            _cle_twin[path] = t if renpy.loadable(t) else None
        return _cle_twin[path] or path

    def _cle_cg_dd(st, at, path):
        return vn_cg(vn_art_file(_cle_b_of(path))), None

    def _cle_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_cle_b_of(path))), None

    for _f in renpy.list_files():
        if _f.startswith(CLE) and _f.endswith(".jpg"):
            _n = _f[len(CLE):-4]
            if _n.endswith("-b"):
                continue
            _k = "cle_" + _n.replace("-", "_")
            vn_cg_files[_k] = _f
            renpy.image(("cg", _k), DynamicDisplayable(_cle_cg_dd, _f))
            renpy.image(("bg", _k), DynamicDisplayable(_cle_bg_dd, _f))

    vn_register_art_sets("cleo", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("cleo", "He's Been Making Me Into His Ex, and Lately She's Not Quite His Ex Anymore",
        "Steph left Nate after four years, and he's taking it badly: the takeout, the four-year playlist, the not sleeping. You're his flatmate, and you know the shape of a month like that. You do the cooking. You turn the playlist down a notch. You give very good advice. What you don't know about is Fridays.",
        CLE + "cover.jpg", "cleo_start")

    achievement.register("I Am")
    achievement.register("It's Monday")

default cle = VNState(row="1", fit="own", week=0, on=False, named=False, surfaced=0, broke=False, asked=False, lane=None, chest=False)
default cle_pc_name = "Danny"
default cle_her_name = "Steph"

define cle_you = VNChar("[cle_pc_name]", who="pc", plate="#3a5a4a")
## Her, in session: her plate is the name Nate calls her (Steph, then Cleo).
define cle_she = VNChar("[cle_her_name]", who="pc", plate="#7a5a9a")
## Danny surfaced inside her: her plate, her voice, his words, in italic.
define cle_under = VNChar("[cle_her_name]", who="pc", plate="#7a5a9a", what_italic=True)
define cle_nate = VNChar("Nate", who="cle_nate", plate="#5a4a3a")

## THE FRIDGE: a card in Danny's scene each week. Never a count.
screen cle_fridge(n):
    zorder 60
    $ _n = max(1, min(6, n))
    frame:
        xalign 0.5 ypos 60
        xmaximum 1180
        padding (34, 22)
        background Frame(Solid("#1a1820f0"), 0, 0)
        vbox:
            spacing 10
            text "{color=#c8b4f0}The fridge:{/color}" size 26 color "#e8e4dc"
            text CLE_FRIDGE[_n] size 26 color "#e8e4dc"

label cleo_start:
    $ cle = VNState(row="1", fit="own", week=0, on=False, named=False, surfaced=0, broke=False, asked=False, lane=None, chest=False)
    $ vn_clock = VNState(day=1, hour=18, minute=0)
    $ vn_route = "cleo"
    $ cle_pc_name = "Danny"
    $ cle_her_name = "Steph"
    if not renpy.session.get("vn_picks"):
        $ cle_pc_name = renpy.input("Your name? (Danny, unless you'd like another. Okafor either way.)", default="Danny", length=20).strip() or "Danny"
    jump cle_week_one

## The turn: "It's Friday", the scene break, and she's there. No trance, no device, nothing described.
label cle_friday(n):
    $ cle.week = n
    $ cle.on = True
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.6)
    pause 0.6
    return

## The week ends inside the session, mid-act; she's still there. Next week's kitchen is the morning.
label cle_week_end:
    $ cle.on = False
    hide screen cle_fridge
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    pause 0.4
    return

label cle_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"cleo"}
    $ vn_route = None
    hide screen cle_fridge
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#c8b4f0}I Am{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The screen trace (game/catalog/vntrace.rpy, for the walks).
init 110 python:
    def _cle_trace():
        pc = cle_pc_file(cle_face_now()).rsplit("/", 1)[-1] if renpy.showing("cle_pc") else None
        cast = ("nate " + " ".join(renpy.get_attributes("cle_nate") or ())) if renpy.showing("cle_nate") else None
        return pc, cast, cle.fit

    vn_trace_routes["cleo"] = _cle_trace
