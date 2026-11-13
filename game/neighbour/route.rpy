## My Neighbour Grew a Cock and Only I Can Make It Go Down (rewritten straight in Ren'Py,
## 2026-11-11; the plan is PLAN.md beside this file, signed off by the owner). From
## catalog/game/02-engine/storylines/neighbour/ (neighbour.js: the ladder, the body, the map, her
## lines; main.twee, rungs.twee), kept verbatim in catalog/docs/routes/vn-original/neighbour/.
##
## THE NON-CON PASS (owner, 2026-11-11: "Only the cage forced"): neighbour stays a consent-premise
## route, "Just this once" and "Colour?" "Green." kept, with one forced beat: at rung 3 Tessa locks
## the cage on over your protest, certain and not cruel. House rules there: you protest out loud and
## she does it anyway; no tears, no menace, no pain. (The source's "sobs" and wet eyes are gasps and
## shaking here, by the same rule.)
##
## The ladder is INTAKE (how much of each dose ends up in you). The fork is rung 4's "Rub it in":
## TSF ("The Last Dose") or femboy ("Exactly Enough"). Linear days: a rung every evening; the
## mornings after rungs 1, 3 and 4 offer the optional visit before your café shift. All
## route-local names carry the nb_ prefix.

init -10 python:
    NB = "art/neighbour/"

    # THE MANTRA, decaying rung by rung (setup.neighbourMantra), said out loud mid-act.
    # THE BODY's loud line when a rung lands (setup.neighbourRungs[n].feel), by row.
    NB_FEEL = {
        "1": "Your lips keep tingling, and you don't know why. You keep licking them. Sweet.",
        "2": "Your mouth's gone soft and greedy overnight. The toothbrush makes you moan.",
        "3": "Your throat throbs where she's been. Every swallow feels like her.",
        "4t": "Your new little tits are so sensitive the air makes you gasp.",
        "4f": "Your thighs and your puffy little nipples buzz at the lightest touch.",
        "5t": "Everything low down is awake and aching for her. Just clenching makes you whimper.",
        "5f": "Your ass is so sensitive now that sitting down is a moan.",
        "6t": "Your mouth, your heavy tits, your brand-new pussy: all of it switched on, all of it hers.",
        "6f": "Your mouth and your ass are the whole of you now. The cage could be anyone's.",
    }

    # THE MAP: where her dose landed, and what softened there (setup.neighbourMapLines).
    NB_MAP = {
        "hands": "Where it landed on your hands the skin's gone soft as the inside of a wrist, and it smells faintly sweet when you lift them to your face.",
        "throat": "Your throat, where it ran down to your collarbone, feels warm all the way in, and when you swallow it's smooth.",
        "mouth": "Your lips are still tingling. They feel fuller than they did, and you keep touching them with your tongue.",
        "face": "It went across your cheek and your jaw, and that side of your face feels softer when you rub it. Just that side.",
        "chest": "Your chest is warm and tight where it landed, the nipples standing up and buzzing in the nicest way.",
        "stomach": "Your stomach, where it pooled, is smooth and tender, and the line of your waist feels drawn in a little.",
        "thighs": "Your thighs, where it ran, are slick and hot and soft, softer than the rest of you.",
        "ass": "Your ass is sticky with her and warm through, and it sits rounder in your hand than it should.",
        "inside": "Inside you it's warm and full and it stays warm, a heavy glow low down that doesn't go anywhere.",
        "lips": "Between your legs everything is slick and swollen with her and humming.",
    }

    # THE CRAVING, a word, never a number (Neighbour.craving).
    NB_CRAVING = ["", "a habit", "a reliance", "a need", "a dependence", "all the time", "all the time"]

    # Her lines after an ordinary visit (setup.neighbourVisitLines), by rung; 4 and 5 by branch.
    NB_VISIT = [None,
        ["Afterwards she perches on the edge of your sofa and tells the carpet, \"I looked it up. There's nobody else this has happened to. Nobody.\" Then, very small: \"Thank you.\"",
         "She apologises all the way to the door, each sorry a little less sorry, until the last one is mostly just your name.",
         "\"You're really good at this,\" she says, mortified, halfway out of the door. \"I don't mean— I mean thank you. I mean it went {i}down{/i}.\""],
        ["She's stopped saying sorry before. Now it's after, like you held a door for her.",
         "\"Same time tomorrow?\" she says at the door, hears herself, goes scarlet, and bolts. You were going to say yes.",
         "She stays a while, close, telling you about a client who cried on the rowing machine. You laugh with your chin still wet."],
        ["She doesn't leave straight away any more. Feet in your lap, phone on her chest, she talks about her day while you sit there caged, still tasting her.",
         "\"I've been thinking,\" she says, stroking your hair while you get your breath back, \"that I don't actually mind any more. Is that bad? I don't think it's bad.\"",
         "She pats your cheek on the way out, like you've done well at something. You go pink. The dimple comes out."],
        {"tsf": ["She stays and watches you rub the last of it in, and when you've finished she presses her thumb into the soft new swell on your chest, curious, and says \"huh,\" and nothing else.",
                 "\"You're getting so soft,\" she says, pleased, running a hand down your side from your ribs to your hip, as if she's checking a client's form. \"Look at that. Right there.\""],
         "femboy": ["She runs the back of her fingers up the inside of your thigh on her way out, just to watch it shiver, and says \"there she is,\" and then, a beat late, \"he.\"",
                    "\"Turn round,\" she says at the door, and you do, in the skirt, and she looks at your ass for a long time with her head on one side and says \"yeah,\" like she's agreeing with somebody."]},
    ]

    def nb_init():
        if nb.tier is None:
            nb.tier = 0

    def nb_femboy():
        return nb.branch == "femboy"

    def nb_advance(n):
        nb.tier = max(nb.tier or 0, n)

    def nb_row():
        """The sprite row: 0-3 shared; from 4, the branch's (t/f); 7t after the TSF shift."""
        b = nb.body or 0
        if nb.shifted:
            return "7t"
        if b >= 4:
            return "%d%s" % (b, "f" if nb_femboy() else "t")
        return str(b)

    def nb_body(n):
        """<<neighbour_body n>>: the body takes rung n's row; its feel line, the first time."""
        if (nb.body or 0) >= n:
            return None
        nb.body = n
        key = str(n) if n <= 3 else "%d%s" % (n, "f" if nb_femboy() else "t")
        return NB_FEEL.get(key)

    def nb_map(*regions):
        """The prose softens where it landed (<<neighbour_map>>): one line a region, new ones only."""
        seen = set(nb.mapped or [])
        lines = [NB_MAP[r] for r in regions if r in NB_MAP and r not in seen]
        nb.mapped = sorted(seen | set(regions))
        return " ".join(lines)

    def nb_craving():
        return NB_CRAVING[max(0, min(6, nb.tier or 0))]

    def nb_visit_line():
        pool = NB_VISIT[max(1, min(4, nb.tier or 1))]
        if isinstance(pool, dict):
            pool = pool["femboy" if nb_femboy() else "tsf"]
        i = renpy.random.randint(0, len(pool) - 1)
        if len(pool) > 1 and i == nb.last_line:
            i = (i + 1) % len(pool)
        nb.last_line = i
        return pool[i]

    # ---- the stage --------------------------------------------------------------------------
    _nb_have = {}

    def _nb_has(n):
        if n not in _nb_have:
            _nb_have[n] = renpy.loadable(NB + n + ".png")
        return _nb_have[n]

    def nb_pc_file(face):
        r, fit = nb_row(), nb.fit
        names = []
        if fit:
            names += ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-neutral" % (r, fit)]
        names += ["pc-r%s-%s" % (r, face), "pc-r%s-neutral" % r]
        for n in names:
            if _nb_has(n):
                return NB + n + ".png"
        return NB + names[-1] + ".png"

    def nb_tessa_file(face):
        """Her growth shows only in her clothes: sweats (1-2), gym shorts (3-4), nothing (5-6)."""
        t = nb.tier or 0
        fit = "nude" if t >= 5 else "shorts" if t >= 3 or (t == 2 and nb.key_given) else "sweats"
        n = "tessa-%s-%s" % (fit, face)
        return NB + (n if _nb_has(n) else "tessa-%s-grin" % fit) + ".png"

    def nb_face_now():
        a = renpy.get_attributes("nb_pc")
        return a[0] if a else "neutral"

    def _nb_portrait(st, at):
        p = vn_art_file(nb_pc_file(nb_face_now()))
        crops = globals().get("neighbour_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["neighbour"] = lambda: DynamicDisplayable(_nb_portrait)

    vn_sprite_image("nb_pc", ("neutral", "shy", "flushed", "eager", "protesting"), nb_pc_file, who="pc")
    vn_sprite_image("nb_tessa", ("mortified", "grin", "certain"), nb_tessa_file)

    for _f in renpy.list_files():
        if _f.startswith(NB) and _f.endswith(".jpg"):
            _n = _f[len(NB):-4]
            vn_register_bg("nb_" + _n.replace("-", "_"), _f)
            vn_register_cg("nb_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("neighbour", [("", "Vanripper"), ("abarus", "Abarus")])

    # the HUD's weekday (2026-11-12): moving day, day 1, is a Saturday; every rung is the next night
    NB_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def nb_weekday_name():
        return NB_WD[(6 + vn_clock.day - 1) % 7]    # day 1 is a Saturday

    vn_weekdays["neighbour"] = nb_weekday_name

    vn_register_route("neighbour", "My Neighbour Grew a Cock and Only I Can Make It Go Down",
        "You were friends as kids, then you weren't anywhere near each other for years. You move into the Flats, and Tessa is across the third-floor landing. One night she pounds on your door with her sweats tented to the waistband: it won't go down, and her own hands don't work. \"Just this once.\" It comes back bigger every night, it only goes down for you, and wherever she finishes, you change.",
        NB + "cover.jpg", "neighbour_start")

    achievement.register("The Last Dose")
    achievement.register("Exactly Enough")

default nb = VNState(tier=0, body=0)
default nb_enc = VNState(partner_came=True, pc_orgasms=0)
default nb_pc_name = "Ellis"
default nb_pc_surname = "Penrose"

define nb_ellis = VNChar("[nb_pc_name]", who="pc", plate="#3f7fbf")
define nb_tess = VNChar("Tessa", who="nb_tessa", plate="#b8508a")

## Route select's entry: moving day, a Saturday afternoon.
label neighbour_start:
    $ nb = VNState(tier=0, body=0)
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=15, minute=0)
    ## the HUD and the box portrait key on vn_route (twinetesting-03 spotted it unset, 2026-11-12)
    $ vn_route = "neighbour"
    $ nb_pc_name = "Ellis"
    if not renpy.session.get("vn_picks"):
        $ nb_pc_name = renpy.input("Your name? (Ellis, unless you'd like another.)", default="Ellis", length=20).strip() or "Ellis"
    jump nb_opening

label nb_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"neighbour"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    $ _nb_title = "The Last Dose" if nb.branch == "tsf" else "Exactly Enough"
    centered "{size=+10}{color=#b8508a}[_nb_title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The screen trace (game/catalog/vntrace.rpy, for the walks): the PC sprite file, the cast sprite
## as "who face", the outfit set (2026-11-12, so a walkthrough can check each sprite lands on time).
init 110 python:
    def _nb_trace():
        pc = nb_pc_file(nb_face_now()).rsplit("/", 1)[-1] if renpy.showing("nb_pc") else None
        cast = ("tessa " + " ".join(renpy.get_attributes("nb_tessa") or ())) if renpy.showing("nb_tessa") else None
        return pc, cast, nb.fit

    vn_trace_routes["neighbour"] = _nb_trace
