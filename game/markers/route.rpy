## The House Settles Markers in Whatever the Debtor Has -- the catalog's `markers` route, rewritten
## straight in Ren'Py (2026-11-11; owner: "start getting art and doing rewrites for the next routes
## (keep a backup of the original story for reference)"). The DoL catalog's version is kept verbatim
## in catalog/docs/routes/vn-original/markers/ (twee, js, spec); this is a rewrite from it, faithful to
## the signed-off spec (2026-10-19) and its non-con beats (2026-10-19/20). The VN plan is PLAN.md.
##
## THE REGISTER (owner, 2026-10-19/20): pure resist-then-break. "The house collects." Every
## collection is non-con: Vic argues the TERMS out loud the whole way in, and the body pays anyway.
## No flips, no tears, no menace. Between scenes he's the gambler again: the arithmetic comes back
## after every collection. "I'm due" is said three times only: at the first zip-up, screamed in the
## lounge, and as the last line. The pot at rung 6 is the one thing he does on his own.
##
## THE LADDER (the spec's): the debt's CURRENCY. Each rung Odette opens a new column in the book and
## the marker is quoted in it: pounds settled in kind, shifts, body, everything back, nights, you.
## The book is read at every shift close in four fields, in words, never a figure. The suit on the
## hook is the metronome. The ampoules are the receipts. Seven linear nights (the built route's),
## the day off between rungs 4 and 5. The floor every night: a station (flavour), Tam's table (a
## real hand that moves nothing) and Simone's break (from night 3, the act you're at).
## All route-local names carry the mr_ prefix.

init -10 python:
    MR = "art/markers/"

    # The book, at shift close (markers.js setup.markersRungs[n].book; the day off's; the fresh line).
    MR_BOOK = [
        "",
        "Game: blackjack. Stake: the marker. Result: lost. Balance after: carried. First settlement taken in kind.",
        "Game: roulette. Stake: the staff suit, staff rate. Result: a run, then the zero. Balance after: carried, by the shift.",
        "Game: craps. Stake: the hot roll. Result: won. Balance after: paid down, in body.",
        "Game: poker. Stake: everything back. Result: lost in one hand. Balance after: everything, carried.",
        "Game: baccarat. Stake: quoted in nights. Result: drew. Balance after: see Nights.",
        "Game: the private table. Stake: herself. Result: the house wins. Balance after: settled. Staff asset physically retained.",
    ]
    MR_BOOK_DAYOFF = "Game: blackjack. Stake: pocket money, own suit. Result: lost. Balance after: as before."
    MR_BOOK_FRESH = "Game: the floor. Stake: one shift, in the suit. Result: worked. Balance after: a fresh column, heading blank."

    # THE SUIT ON THE HOOK, the metronome (setup.markersHook), by kit stage.
    MR_HOOK = [
        "Nothing yet: your own jacket, with the marker's stub in the pocket.",
        "The hire: black leotard, collar, cuffs, costume ears, fishnets, heels. The tailor's clip on the seam.",
        "A bigger suit. The split one folded on the shelf, for luck.",
        "The bigger suit, its clip let out to the end. A crotch pouch with almost nothing to hold.",
        "The costume ears on the hook, unused. The carrot pin.",
        "Only the leotard. The ears and the tail are yours.",
    ]

    def mr_hook_line():
        k = max(0, min(5, mr.kit or 0))
        line = MR_HOOK[k]
        if k == 4 and mr.schedule:
            line += " The schedule taped inside the door."
        return line

    # How you take each reading (setup.markersTakes): one line of gambler's arithmetic, by night.
    MR_TAKES = {
        1: {"smug": "You do the arithmetic out loud, grinning. \"One settlement down, in kind. Four more nights like that and I'm clean. Staff rate, even!\"",
            "giddy": "You laugh, and can't stop. \"In {i}kind{/i}. I paid down a marker with my {i}chest hair{/i}. That's the best deal anybody's ever had in this building.\"",
            "filthy": "You look at the door Simone went out of, and your cock twitches at the sight of it. \"That was NOT the rate. I'm lodging a complaint.\" It comes out hoarse from yelling."},
        2: {"smug": "\"By the shift,\" you repeat, running your palms down your new hips. \"With odds like these? I'll work it down twice as fast.\"",
            "giddy": "You bounce on your heels and your tail bobs. \"Did you see that run? Did you {i}see{/i} it? Before the zero? Right before?\"",
            "filthy": "You lick your lips and taste Simone on them still, and your knees go. \"Write down that I said no. Put it in the book.\" She doesn't."},
        3: {"smug": "Your chest rises and falls like you've conquered a country, and it's a {i}lot{/i} of chest. \"Now {i}that{/i} is how you work a marker.\"",
            "giddy": "You squeeze your new tits through the new suit and squeal. \"Paid down in {i}body{/i}! I'm a {i}shareholder{/i}!\"",
            "filthy": "\"House property,\" you mutter, cupping them through the suit, and your nipples go hard again at the words. Odette does not look."},
        4: {"smug": "You shrug, and everything wobbles. \"Variance. One hand's just one hand. Tomorrow's a fresh shoe.\"",
            "giddy": "You giggle, still floaty, still feeling her. \"Everything back! I lost {i}everything{/i} back! Do you know how hard that is to do in one hand?\"",
            "filthy": "You shift on your feet and feel her still in you, open and slick, and clench on nothing. \"I begged. That's not in the terms either. Write that down.\""},
        5: {"smug": "\"As before,\" you repeat. \"So the day off cost me nothing. A free day. That's a win.\"",
            "giddy": "\"You should've seen the shirt,\" you tell Odette, delighted. \"It didn't even {i}try{/i}.\"",
            "filthy": "You hook a thumb in the recut suit and snap it against your hip. \"Missed this. Missed being {i}looked{/i} at.\""},
        6: {"smug": "\"A draw. Against the house. In nights. Do you know how rare a draw is?\"",
            "giddy": "Your ears flick straight up. \"I'm on the {i}schedule{/i}! Look! It's got my name on it and everything!\"",
            "filthy": "You squeeze your thighs together and feel how slick they still are. \"Nights. Fine. {i}Nights{/i}.\" It comes out hoarse. You screamed the pit down an hour ago."},
        "fresh": {"smug": "\"Fresh column. Clean slate. My favourite kind.\"",
            "giddy": "Your tail flicks against the suit. \"What's it quoted in? Tell me. Tell me tell me.\" Odette doesn't.",
            "filthy": "You lean over her desk until your tits are on the book. \"Put me down for overtime.\""},
    }

    # A hand at Tam's table moves nothing (Markers.handLine): one line in the current currency.
    MR_UNIT = ["", "in kind", "in shifts", "in body", "in everything", "in nights", "in you"]

    def mr_hand_line(result):
        unit = "on the fresh line" if mr.done else MR_UNIT[max(0, min(6, mr.tier or 0))] or "in kind"
        if result in ("natural", "win"):
            return "Off the marker, %s." % unit
        if result == "push":
            return "Carried, %s." % unit
        return "On the marker, %s." % unit

    # ---- the ladder --------------------------------------------------------------------------
    def mr_advance(n):
        """The rung is banked at shift close (Markers.advance in the reading)."""
        mr.tier = max(mr.tier or 0, n)

    def mr_body(n):
        """The body lands (up only): rung 1 at waking on night 2, rung 2 at the first zip-up, rung 3
        on the felt, rung 4 in the locker, rung 5 at waking and on the page, rung 6 at the table."""
        mr.body = max(mr.body or 0, n)

    def mr_break_act():
        """Simone's break plays the act you're at (Markers.breakSpec): oral, then titjob, then anal
        from rung 4 (withheld before), vaginal from rung 5; after the ending, your pick."""
        if mr.done and mr.break_act:
            return mr.break_act
        t = mr.tier or 0
        return "vaginal" if t >= 5 else "anal" if t >= 4 else "titjob" if t >= 3 else "oral"

    def mr_break_open():
        """Once a night, from night 3 (rung 2 banked), never on night 7."""
        return (mr.tier or 0) >= 2 and (mr.night or 1) != 7 and mr.break_night != mr.night

    # ---- the stage -------------------------------------------------------------------------
    _mr_have = {}

    def _mr_has(n):
        if n not in _mr_have:
            _mr_have[n] = renpy.loadable(MR + n + ".png")
        return _mr_have[n]

    def mr_art(name):
        """A cast sprite's file, or the blank one until its art lands."""
        return MR + name + ".png" if _mr_has(name) else MR + "_blank.png"

    def mr_rung():
        return max(1, min(6, mr.body or 1))

    def mr_pc_file(face):
        """The sprite that exists: the outfit set with this face, the outfit set's neutral, the own
        clothes with this face, the own clothes' neutral (mistaken's fallback chain). Rung 1's own
        clothes are pc-r1-<face>."""
        r, fit = mr_rung(), mr.fit or "own"
        own = "pc-r%d" % r if r == 1 else "pc-r%d-own" % r
        names = []
        if fit != "own":
            names += ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-neutral" % (r, fit)]
        names += ["%s-%s" % (own, face), "%s-neutral" % own]
        for n in names:
            if _mr_has(n):
                return MR + n + ".png"
        return MR + "_blank.png"

    def mr_face_now():
        a = renpy.get_attributes("mr_pc")
        return a[0] if a else "neutral"

    def _mr_portrait(st, at):
        p = vn_art_file(mr_pc_file(mr_face_now()))
        if p.endswith("_blank.png"):
            return Null(), None
        x, y, w, h = vn_face_crop(markers_face_crops, p)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["markers"] = lambda: DynamicDisplayable(_mr_portrait)

    vn_sprite_image("mr_pc", ("neutral", "grin", "nervous", "flushed", "shocked"), mr_pc_file, who="pc")
    vn_sprite_image("mr_simone", ("neutral", "smirk", "hungry"), lambda f: mr_art("simone-" + f))
    vn_sprite_image("mr_odette", ("neutral",), lambda f: mr_art("odette-" + f))
    vn_sprite_image("mr_royce", ("neutral", "smirk"), lambda f: mr_art("royce-" + f))
    vn_sprite_image("mr_tam", ("neutral",), lambda f: mr_art("tam-" + f))
    vn_sprite_image("mr_costumer", ("neutral",), lambda f: mr_art("costumer-" + f))
    vn_sprite_image("mr_waitress", ("neutral",), lambda f: mr_art("waitress-" + f))

    # Every picture in the route's folder is a background and a CG by name ("bg mr_floor",
    # "cg mr_roll_split").
    for _f in renpy.list_files():
        if _f.startswith(MR) and _f.endswith(".jpg") and "/scenes/" not in _f and not _f.endswith("/cover.jpg"):
            _n = _f[len(MR):-4]
            vn_register_bg("mr_" + _n.replace("-", "_"), _f)
            vn_register_cg("mr_" + _n.replace("-", "_"), _f)

    # Two art sets (owner, 2026-11-11: "Yes, Abarus too"); the Abarus set has no backgrounds of its
    # own ("they can be generic") and falls back to the Vanripper ones.
    vn_register_art_sets("markers", [("", "Vanripper")])  # no Abarus set: owner, 2026-11-12, "for stories with TFs, lets not do abarus"

    vn_register_route("markers", "The House Settles Markers in Whatever the Debtor Has",
        "Four in the morning at the Golden Hare, ten hours in, out of chips, and due. The pit boss writes you a marker. The small print on the back says the house settles markers in whatever the debtor has. You sign it in block capitals. The house never lies, and every night it collects in a new currency.",
        MR + "cover.jpg", "markers_start")

    achievement.register("House Bunny")

default mr = VNState(tier=0, body=0, kit=0, night=1)

## The speakers. Vic Hollan, 27 ("Hollan, V." in the book; "Miss Hollan" from rung 5's printout).
define mr_vic = VNChar("Vic", who="pc", plate="#3f6fb0")
define mr_simone = VNChar("Simone", who="mr_simone", plate="#7a1f3d")
define mr_odette = VNChar("Odette", who="mr_odette", plate="#4b4f5c")
define mr_royce = VNChar("Royce", who="mr_royce", plate="#1f3a66")
define mr_tam = VNChar("Tam", who="mr_tam", plate="#2f5a46")
define mr_costumer = VNChar("Costumer", who="mr_costumer", plate="#6b5a4a")
define mr_waitress = VNChar("Waitress", who="mr_waitress", plate="#6b4a5a")
define mr_stick = VNChar("Stickman", who="mr_stick", plate="#5b6270")
define mr_croupier = VNChar("Croupier", who="mr_croupier", plate="#5b6270")
define mr_dealer = VNChar("Dealer", who="mr_dealer", plate="#5b6270")
define mr_book = VNChar(None, what_color="#f3c969")

## Route select's entry: a quarter to four, ten hours in, one chip left.
label markers_start:
    $ mr = VNState(tier=0, body=0, kit=0, night=1)
    $ vn_clock = VNState(day=1, hour=3, minute=45)   # the HUD's day is the night (the afternoons reset it)
    $ vn_route = "markers"
    jump mr_opening

## The end of the route ("Choose another story").
label mr_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"markers"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}House Bunny{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The test trace's view of the stage (game/catalog/vntrace.rpy).
init 110 python:
    def _mr_trace():
        pc = mr_pc_file(mr_face_now()).rsplit("/", 1)[-1] if renpy.showing("mr_pc") else None
        cast = None
        for tag in ("mr_simone", "mr_odette", "mr_royce", "mr_tam", "mr_costumer", "mr_waitress"):
            if renpy.showing(tag):
                cast = tag[3:] + " " + " ".join(renpy.get_attributes(tag) or ())
        return pc, cast, mr.fit

    vn_trace_routes["markers"] = _mr_trace
