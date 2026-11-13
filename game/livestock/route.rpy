## Marsh Farm Filed Me as a Heifer, So They Milk Me at Both Ends Until I Match the Paperwork
## (rewritten straight in Ren'Py, 2026-11-11; PLAN.md beside this file, signed off by the owner).
## From catalog/game/02-engine/storylines/livestock/ (livestock.js, main.twee, rungs.twee,
## ending.twee), kept verbatim in catalog/docs/routes/vn-original/livestock/.
##
## CONSENT as ruled (owner, 2026-10-19/20): pure resist-then-break, every rung and the herd night,
## never a flip; the Stay epilogue full corruption. Owner, 2026-11-11: Angus's nose ring is dropped
## (piercings are out); the ear tag stays (the earring exception); the stall card is a Ren'Py screen.
##
## The ladder is YIELD: the vessel at the front climbs while the back tank drains. Nine days: the
## morning (growth, the trough, a chore), the rung, the nine o'clock milking, the night. Monster
## people, never furry. All route-local names carry the ls_ prefix.

init -10 python:
    LS = "art/livestock/"

    # THE VESSEL and THE BACK TANK, by rung (setup.livestockFrame).
    LS_VESSEL = [None, "a saucer", "the saucer", "the saucer", "the saucer", "the teacup", "a jug", "a pail", "the churn", "the churn"]
    LS_BACK = [None, "brimming", "brimming", "full", "half", "a dribble", "a bead", "dry", None, None]
    # THE STALL CARD, Hester's annotation a rung (setup.livestockCard).
    LS_CARD = [None, "DISCREPANCY — MONITOR.", "Escalate: double mash.", "Name corrected: CHERRY.", "Responsive.",
               "Front: non-producing, caged. Milking as female.", "Stud-privileged.", "Blue ribbon, dairy heifer division.",
               "DISCREPANCY — RESOLVED. FEMALE.", "COW. DAIRY PRIME."]
    # THE CHORES, one a morning, days 2-6 (setup.livestockChores).
    LS_CHORES = {
        "mud": ("The mud pen with Petal", {
            2: "Petal hands you a scrub brush and points at the trough. \"Scrub. No hands on your face after, or you'll be mud to the eyebrows.\" You're mud to the eyebrows in a minute. She cackles. \"Funniest-looking heifer I ever had in my pen.\"",
            3: "Petal flicks the brush at your chest and the mud lands right on your new puffy nipples. {i}Splat.{/i} \"Hah! Look at you jump. Sensitive, are we?\" You are. You scrub with your elbows tucked in and your face hot.",
            4: "The mud's warm today, mash spill underneath. You slip, sit down hard, and Petal sits down next to you on purpose. \"Good mud. Gets the polish to stick.\" She smears a handful down your new tits like she's buttering bread. \"Oi— {i}hands{/i}—!\" She doesn't stop.",
            5: "Petal stops scrubbing to stare at your chest. \"Oh, they're {i}leaking{/i}.\" She leans in and licks a white bead off your nipple before you can shove her off. {i}Shlk.{/i} \"Get {i}off{/i}— {i}ahh{/i}—!\" \"Mm. Sweet. Don't waste it, Cherry.\"",
            6: "It's too cold for the pen, so it's the mash room with Petal, and the steam, and her elbow in your ribs every time your tits jiggle. \"You're a proper armful now,\" she says, and squeezes one to prove it. \"Stop {i}doing{/i} that— {i}mmoo{/i}—\""}),
        "ring": ("The ring walk with Buttercup", {
            2: "Round and round the paddock behind Buttercup. \"Chin up. Chest out. Walk like somebody's looking.\" Nobody's looking. Your hips do a thing anyway. Buttercup moos approval.",
            3: "\"Smaller steps,\" Buttercup says. \"Heel to toe. Let the hips do it.\" They do it. They do it a {i}lot{/i} now, and your nipples rub every step. By the third lap you're breathing through your mouth.",
            4: "Buttercup walks behind you with a switch of clover and taps your ass when it stops swaying. {i}Tap.{/i} \"Swing.\" {i}Tap.{/i} \"More.\" It's swinging plenty. You walk it anyway, until the twins whistle from the fence.",
            5: "\"Shoulders back,\" Buttercup says, \"and let them bounce.\" They bounce. They bounce so much you have to hold them. \"Hands down! Judges want to see the yield!\"",
            6: "The ring's frosty, so you walk it in your bare skin and your breath steams, and every lap your tits swing and your nipples go hard as nails. Buttercup nods. \"You've got the walk. Now you just need the ribbon.\""}),
        "watch": ("Watching Marigold milked", {
            2: "Marigold sits on the dairy bench with her apron open and the cups on, and her tits pour. Not drip. {i}Pour.{/i} She catches you staring. \"That's what the saucer's waiting for, sweetheart.\" Your nipples throb just looking.",
            3: "Marigold milks by hand today, slow, a thumb and two fingers, {i}shff, shff{/i}, into a pail. Her cock swings heavy under the apron the whole time. \"Watch my hands,\" she says. You aren't watching her hands.",
            4: "You hold the pail for Marigold. It fills against your thighs, warm through the tin. She sees your new tits and her cock twitches. \"Coming on nicely, ma'am's little discrepancy.\" Your face goes hot to the ears.",
            5: "Marigold lets her milk down into a churn, the cups humming, and leans back with her eyes shut and moans, low and long. Your own tits throb in time. A drop runs down your belly. She opens one eye. \"Yours wants out too.\"",
            6: "Marigold's milked by the stove, steam coming off the churn, her big tits swinging in the cups. She crooks a finger and lets you hold one up while the machine works. It's heavy and hot and pulsing and you can't stop squeezing."}),
    }

    def ls_init():
        if ls.tier is None:
            ls.tier = 0

    def ls_advance(n):
        ls.tier = max(ls.tier or 0, n)

    def ls_body(n):
        if (ls.body or 0) >= n:
            return False
        ls.body = n
        return True

    def ls_card_lines():
        """The stall card, every annotation so far, in Hester's capitals."""
        t = max(1, min(9, ls.tier or 1))
        lines = ["MARSH FARM — INTAKE. CLASS: HEIFER. SEX: {s}FEMALE{/s}"]
        lines += [LS_CARD[i] for i in range(1, t + 1)]
        return lines

    def ls_take_line(rung):
        tk = ls.take or "struggle"
        if tk == "struggle":
            if rung < 2:
                return "You buck on the bench and yank at the straps. \"Let me UP— this is a— I'm a {i}person{/i}—!\" The straps creak. That's all they do. Buttercup winces over the partition."
            if rung < 4:
                return "You thrash. You yank at the straps till the bench rocks on its bale. \"Get— {i}off{/i}— mm— {i}mmh{/i}—\" It catches in your throat, half a no, half a moo."
            return "You fight the straps all the way. \"No— no no— {i}mmmmooooo{/i}—\" The moo rolls out of you low and long over the top of the no, and the whole line moos back."
        if tk == "swear":
            if rung < 4:
                return "\"Fuck off— fuck {i}OFF{/i}— I'll report the lot of you—\" Hester writes something down. It isn't your complaint."
            return "\"Fuck— {i}fuck{/i}— don't you DARE— milk— {i}milk{/i}— {i}mmmmoooo{/i}—\" Every word you know, and the last one comes out a moo."
        if rung < 4:
            return "You grit your teeth and grip the bar. You are {i}not{/i} going to make a sound. You don't last long."
        return "You grit your teeth so hard your jaw aches. Your tits don't care. Neither does your mouth, in the end."

    def ls_fight_line():
        f = ls.fight or "struggle"
        if f == "swear":
            return "You swore the whole way through, every word you know. Half of them came out a moo."
        if f == "grit":
            return "You gritted your teeth the whole way through. Your jaw held out longer than the rest of you did."
        return "You fought the whole way through. Your knuckles are still white from it."

    # ---- the stage --------------------------------------------------------------------------
    _ls_have = {}

    def _ls_has(n):
        if n not in _ls_have:
            _ls_have[n] = renpy.loadable(LS + n + ".png")
        return _ls_have[n]

    def ls_pc_file(face):
        r, fit = max(0, min(9, ls.body or 0)), ls.fit
        if fit == "nude" and ls.caged and r == 4:
            fit = "caged"   # rung 5's cage goes on before row 5's body (rows 5-7 draw it nude)
        names = []
        if fit:
            names += ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-defiant" % (r, fit)]
        names += ["pc-r%d-%s" % (r, face), "pc-r%d-defiant" % r]
        if fit:   # a face this outfit's set doesn't have: any face of the same body and outfit, before the bare row
            names += ["pc-r%d-%s-%s" % (r, fit, f) for f in ("shocked", "flushed", "broken", "defiant")]
        for n in names:
            if _ls_has(n):
                return LS + n + ".png"
        return LS + names[-1] + ".png"

    def ls_face_now():
        a = renpy.get_attributes("ls_pc")
        return a[0] if a else "defiant"

    def _ls_portrait(st, at):
        p = vn_art_file(ls_pc_file(ls_face_now()))
        crops = globals().get("livestock_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["livestock"] = lambda: DynamicDisplayable(_ls_portrait)

    vn_sprite_image("ls_pc", ("defiant", "shocked", "flushed", "broken"), ls_pc_file, who="pc")
    vn_sprite_image("ls_marigold", ("fond", "stern", "pleased"), lambda f: LS + "marigold-" + f + ".png")
    vn_sprite_image("ls_hester", ("flat", "smile"), lambda f: LS + "hester-" + f + ".png")
    vn_sprite_image("ls_buttercup", ("grin", "soft"), lambda f: LS + "buttercup-" + f + ".png")
    vn_sprite_image("ls_petal", ("grin", "bossy"), lambda f: LS + "petal-" + f + ".png")
    vn_sprite_image("ls_angus", ("still",), lambda f: LS + "angus-" + f + ".png")
    vn_sprite_image("ls_billy", ("grin",), lambda f: LS + "billy-" + f + ".png")
    vn_sprite_image("ls_bart", ("grin",), lambda f: LS + "bart-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(LS) and _f.endswith(".jpg"):
            _n = _f[len(LS):-4]
            vn_register_bg("ls_" + _n.replace("-", "_"), _f)
            vn_register_cg("ls_" + _n.replace("-", "_"), _f)

    # Vanripper only: no Abarus set on an animal-TF route (owner, 2026-11-12 about 12:55 pm ET: "by
    # TFs, I mean like animal tf like cat girls or cow girls").
    vn_register_art_sets("livestock", [("", "Vanripper")])

    vn_register_route("livestock", "Marsh Farm Filed Me as a Heifer, So They Milk Me at Both Ends Until I Match the Paperwork",
        "You're broke, so you sign a seasonal-help clipboard without reading it, and wake in a hay stall with a tag through your ear. The card on the gate says HEIFER, FEMALE. Hester Marsh strikes FEMALE and writes DISCREPANCY — MONITOR. All stock milks at nine p.m., both ends, no exceptions, and every night the back tank fills and the saucer at the front stays dry. For now.",
        LS + "cover.jpg", "livestock_start")

    achievement.register("Blue Ribbon")

default ls = VNState(tier=0, body=0)
default ls_enc = VNState(partner_came=True, pc_orgasms=0)
default ls_pc_name = "Wyatt"

define ls_you = VNChar("[ls_pc_name]", who="pc", plate="#8a6a3f")
define ls_cherry = VNChar("Cherry", who="pc", plate="#c2508f")
define ls_marigold = VNChar("Marigold", who="ls_marigold", plate="#9b6a3a")
define ls_hester = VNChar("Hester", who="ls_hester", plate="#5f6f5a")
define ls_buttercup = VNChar("Buttercup", who="ls_buttercup", plate="#c9a23f")
define ls_petal = VNChar("Petal", who="ls_petal", plate="#d47a9b")
define ls_angus = VNChar("Angus", who="ls_angus", plate="#6a4a3a")
define ls_billy = VNChar("Billy", who="ls_billy", plate="#7a8a4a")
define ls_bart = VNChar("Bart", who="ls_bart", plate="#7a8a4a")
define ls_counter = VNChar("The man at the counter", who="counter", plate="#6b6b78")

## THE STALL CARD on the gate, in Hester's capitals.
screen ls_card():
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 640
        padding (28, 20)
        background Frame(Solid("#efe6cff2"), 0, 0)
        vbox:
            spacing 8
            for t in ls_card_lines():
                text t size 22 color "#2a2a2a" bold True

## Route select's entry: the farmers' centre, first thing.
label livestock_start:
    $ ls = VNState(tier=0, body=0)
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=8, minute=0)
    ## the HUD and the box portrait key on vn_route (twinetesting-03 spotted it unset, 2026-11-12)
    $ vn_route = "livestock"
    $ ls_pc_name = "Wyatt"
    if not renpy.session.get("vn_picks"):
        $ ls_pc_name = renpy.input("Your name? (Wyatt, unless you'd like another. The farm will call you something else.)", default="Wyatt", length=20).strip() or "Wyatt"
    jump ls_opening

label ls_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"livestock"}
    $ vn_route = None
    hide screen ls_card
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#c9a23f}Blue Ribbon{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The screen trace (game/catalog/vntrace.rpy, for the walks): the PC sprite file, the cast sprite
## as "who face", the outfit set (2026-11-12, so a walkthrough can check each sprite lands on time).
init 110 python:
    def _ls_trace():
        pc = ls_pc_file(ls_face_now()).rsplit("/", 1)[-1] if renpy.showing("ls_pc") else None
        cast = None
        for _t in ("ls_marigold", "ls_hester", "ls_buttercup", "ls_petal", "ls_angus", "ls_billy", "ls_bart"):
            if renpy.showing(_t):
                cast = _t[3:] + " " + " ".join(renpy.get_attributes(_t) or ())
        return pc, cast, ls.fit

    vn_trace_routes["livestock"] = _ls_trace
