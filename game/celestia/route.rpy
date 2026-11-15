## A Catgirl Drafted Me as the Town's Magical Girl, and My Finishing Move Is an Orgasm
## (rewritten straight in Ren'Py, 2026-11-11; PLAN.md beside this file, signed off by the owner).
## From catalog/game/02-engine/storylines/celestia/ (celestia.js, main.twee, rungs.twee, ending.twee,
## cast.twee), kept verbatim in catalog/docs/routes/vn-original/celestia/.
##
## CONSENT as converted (owner, 2026-10-19/20): escalating corruption. The sorties are taken (the fogged
## are puppets, never villains; Nightshade the only real assailant), the bus flips on the spoken
## surrender, the lair is taken, the showdown protests and then takes hold of the threads; Pippa's nights
## and the dark ride are consensual. No cock in you before rung 4, nothing in your cunt before rung 6.
##
## THE LADDER is THE CUE: how little it takes to shine (the phrase on a dare, a mutter, a breath, a hand on
## your hip, his snap, nothing). Two bodies, one table: the form (worn while transformed) and you after
## each demorph. THE FORK, four times ("Let it go to him" / "Make it shine"): his power climbs 20 at each
## street sortie and 40 at the lair; 60 is the dark ending. Shown as a word, never a number.
## All route-local names carry the ce_ prefix.

init -10 python:
    CE = "art/celestia/"

    # THE RUNGS (setup.celestiaRungs): the cue, the vest, the sensitivity line after the demorph.
    CE_CUE = [None,
        "It takes the whole phrase, out loud, on Luna's dare, with your face on fire.",
        "It takes a mutter now. Under your breath, behind a locked stall door, and the light comes.",
        "It takes a breath. You say it like your own name, and it's already happening.",
        "It takes less than the phrase. A hand on your hip, and the light is up before you finish.",
        "It isn't yours any more. He snaps his fingers.",
        "It takes nothing. There's nothing left to change back from."]
    CE_VEST = [None,
        "The ElectroMart vest fits. Baby blue, polyester, a pocket full of price stickers, and the badge says __NAME__.",
        "The vest's gone loose at the shoulders. It catches at the hips instead, which is new, and which you don't think about.",
        "Ms. Pruitt dug the stockroom's only spare out for you when the side seam went. It's a women's cut. It fits better than the old one ever did.",
        "The women's cut strains across your chest now. The badge sits on a slope.",
        "The vest won't button. You wear it open, and the badge hangs off a strap over everything.",
        "The vest hangs on the break-room hook. You haven't taken it down."]
    CE_FEEL = [None,
        "Your lips are still fizzing from the words. You touch them and gasp out loud. \"Why are my LIPS doing that?\"",
        "You bite your lip and it goes straight to your nipples. \"{i}Ahn{/i}— okay, that's NEW,\" you tell nobody, too loud.",
        "Your mouth waters at nothing and your new tits throb in time with it. \"{i}Mmh{/i}— everything's turned UP,\" you moan.",
        "You sit down and your ass {i}throbs{/i}, and your lips throb with it. \"{i}Hahh{/i}— my mouth's a— my ass is a—\" You can't finish. You're squirming.",
        "Your new pussy pulses every time your thighs touch, and your lips are hot and swollen. \"{i}Ohh{/i}— I'm SO sensitive,\" you whine. \"Everywhere. EVERYWHERE.\"",
        "Starlight hums in every part of you: lips, tits, ass, pussy, all of it at once. \"{i}Aaahn{/i}—!\" you squeal, and nobody's even touching you."]
    # NIGHTSHADE'S POWER (setup.celestiaFeeds/Bands): fed by "Let it go to him" only.
    CE_FEEDS = {2: 20, 3: 20, 4: 20, 5: 40}
    CE_THRESHOLD = 60
    CE_BANDS = [(0, "guttering", "#7fd68a"), (20, "gathering", "#6fd3c8"), (40, "strong", "#f3c969"),
                (60, "ascendant", "#ff8fc8"), (80, "unstoppable", "#ff6b6b")]
    # Luna's texts when a sortie comes due (setup.celestiaTexts).
    CE_TEXTS = {
        2: "MALL. URGENT. massive spike in the food court. get there or the next customer humps a vending machine",
        3: "club orbit. the basement one off connudatus. tonight. HE'S there. wear something you can lose",
        4: "night bus. the last one out. just get on it. don't say anything clever",
        5: "elk street. the warehouse with velvet in the windows. he sent an invitation. it has your name spelled right, which is the creepy part",
        6: "the park. today. he's in the middle of it and he's brought everyone. bring everything"}
    CE_PLACE = {3: "Club Orbit", 4: "The night bus", 5: "The Elk Street warehouse"}

    def ce_init():
        if ce.forks is None:
            ce.forks = {}

    def ce_rung(n):
        ce.tier = max(ce.tier or 0, n)

    def ce_body(n):
        """Your body after rung n (CS.body): toward the row, never back."""
        if (ce.body or 0) >= n:
            return False
        ce.body = n
        return True

    def ce_morph(n, dark=False):
        """The form for rung n (celestia_morph): worn until the demorph."""
        ce.morphed, ce.form, ce.dark_form = True, max(ce.form or 0, n), dark
        store.ce_plate = "Celestia"

    def ce_demorph(n=None):
        """Back to you (celestia_demorph): the body moves only now, toward the rung's row."""
        ce.morphed = False
        if n:
            ce_body(n)
        store.ce_plate = "Celestia" if ce.named else ce_pc_name

    def ce_power():
        return max(0, min(100, ce.power or 0))

    def ce_band():
        p, band = ce_power(), CE_BANDS[0]
        for b in CE_BANDS:
            if p >= b[0]:
                band = b
        return band

    def ce_dark():
        return ce_power() >= CE_THRESHOLD

    def ce_let_go(n):
        if not (ce.forks or {}).get(n):
            ce.forks[n] = "go"
            ce.power = ce_power() + CE_FEEDS.get(n, 0)
        ce.power_seen = True

    def ce_shine(n):
        if not (ce.forks or {}).get(n):
            ce.forks[n] = "shine"
        ce.power_seen = True

    def ce_cue():
        if (ce.loft or 0) >= 5:
            return CE_CUE[6]
        return CE_CUE[max(1, min(6, (ce.tier or 0) + 1))]

    def ce_vest_n():
        return 6 if (ce.loft or 0) >= 5 or ce.done else max(1, min(5, ce.tier or 1))

    def ce_vest():
        return CE_VEST[ce_vest_n()].replace("__NAME__", ce_pc_name.upper())

    def ce_power_line():
        b = ce_band()
        s = "{color=#f3c969}Nightshade:{/color} {color=%s}%s{/color}" % (b[2], b[1])
        if ce_dark():
            s += " {color=#ff6b6b}— too strong to face{/color}"
        return s

    # ---- the stage --------------------------------------------------------------------------
    _ce_have = {}

    def _ce_has(n):
        if n not in _ce_have:
            _ce_have[n] = renpy.loadable(CE + n + ".png")
        return _ce_have[n]

    def ce_pc_file(face):
        """The form while transformed (form-r<n>, the dark form), else you at your body's row in
        today's clothes (the vest, casual, Pippa's sweater, nude)."""
        if ce.morphed:
            base = "form-dark" if ce.dark_form else "form-r%d" % max(1, min(6, ce.form or 1))
            names = [base + "-" + face, base + "-snark"]
        else:
            r, fit = max(0, min(6, ce.body or 0)), ce.fit
            row = "r6dark" if ce.dark_hair else "r%d" % r   # the dark ending keeps the violet
            names = []
            if fit:
                names += ["pc-%s-%s-%s" % (row, fit, face), "pc-%s-%s-snark" % (row, fit)]
            names += ["pc-%s-%s" % (row, face), "pc-%s-snark" % row]
        for n in names:
            if _ce_has(n):
                return CE + n + ".png"
        return CE + names[-1] + ".png"

    def ce_face_now():
        a = renpy.get_attributes("ce_pc")
        return a[0] if a else "snark"

    def _ce_portrait(st, at):
        p = vn_art_file(ce_pc_file(ce_face_now()))
        crops = globals().get("celestia_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["celestia"] = lambda: DynamicDisplayable(_ce_portrait)

    vn_sprite_image("ce_pc", ("snark", "shocked", "flushed", "shining", "glad"), ce_pc_file, who="pc")
    vn_sprite_image("ce_luna", ("deadpan", "smug", "flat"), lambda f: CE + "luna-" + f + ".png")
    vn_sprite_image("ce_pippa", ("grin", "soft", "flushed", "bralette"), lambda f: CE + "pippa-" + f + ".png")
    vn_sprite_image("ce_nightshade", ("bored", "hungry", "smile"), lambda f: CE + "nightshade-" + f + ".png")
    vn_sprite_image("ce_pruitt", ("verdict",), lambda f: CE + "pruitt-" + f + ".png")
    vn_sprite_image("ce_dougie", ("grin", "red"), lambda f: CE + "dougie-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(CE) and _f.endswith(".jpg"):
            _n = _f[len(CE):-4]
            vn_register_bg("ce_" + _n.replace("-", "_"), _f)
            vn_register_cg("ce_" + _n.replace("-", "_"), _f)

    # Vanripper only (owner, 2026-11-12 about 1:56 pm ET: the Abarus alternate set is for femboy,
    # feminization and soft-TSF routes; celestia is full TSF)

    # the HUD's weekday (2026-11-12): day 1 is a Monday, so the six days run Monday to Saturday's
    # showdown morning after, and the hang epilogue's "On Saturday" is the next Saturday
    CE_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def ce_weekday():
        return (1 + vn_clock.day - 1) % 7    # 0 is Sunday; day 1 is a Monday

    def ce_weekday_name():
        return CE_WD[ce_weekday()]

    def ce_to_weekday(wd, h):
        """Minutes to the next weekday wd (0 Sunday .. 6 Saturday) at hour h; today counts while h
        is still ahead."""
        now = vn_clock.hour * 60 + vn_clock.minute
        days = (wd - ce_weekday()) % 7
        if days == 0 and now >= h * 60:
            days = 7
        return days * 1440 + h * 60 - now

    vn_weekdays["celestia"] = ce_weekday_name

    vn_register_route("celestia", "A Catgirl Drafted Me as the Town's Magical Girl, and My Finishing Move Is an Orgasm",
        "You come home from a shift at ElectroMart and there's a catgirl sitting on your Blu-rays with the head of your best figure in her lap. Her name is Luna, the town needs a magical girl, and the Prism picked you. Magical law is gender-agnostic: she'll fix that in post. Your finishing move comes out of your chest, and it's an orgasm. Every time you change back, some of her stays, and every time you let the fog take you, Professor Nightshade gets stronger.",
        CE + "cover.jpg", "celestia_start")

    achievement.register("Starlit Showdown")
    achievement.register("Black's Good on You")

default ce = VNState(tier=0, body=0, loft=0, power=0, forks={})
default ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
default ce_pc_name = "Callum"
default ce_plate = "Callum"

## The speakers. Your plate reads your name, "Celestia" while you're transformed, and "Celestia" for good
## from the Embrace ("Say the name.").
define ce_you = VNChar("[ce_plate]", who="pc", plate="#7a6fd0")
define ce_luna = VNChar("Luna", who="ce_luna", plate="#3b3f66")
define ce_pippa = VNChar("Pippa", who="ce_pippa", plate="#e0559a")
define ce_nightshade = VNChar("Professor Nightshade", who="ce_nightshade", plate="#5b2a7a")
define ce_speaker = VNChar("The speaker", who="ce_nightshade", plate="#5b2a7a")
define ce_pruitt = VNChar("Ms. Pruitt", who="ce_pruitt", plate="#4b5a78")
define ce_dougie = VNChar("Dougie", who="ce_dougie", plate="#5f8f3e")
define ce_fog = VNChar("The fogged", who="fog", plate="#6b6b78")

## Nightshade's power in the HUD, as a word (setup.celestiaPowerBands), from the first fork on.
screen ce_power():
    zorder 90
    if vn_route == "celestia" and ce.power_seen and not _menu:
        frame:
            xalign 1.0 xoffset -24 ypos 18
            padding (18, 8, 18, 10)
            background Frame("gui/vn/chip.png", 12, 12)
            text ce_power_line() style "vn_hud_text"

init python:
    config.overlay_screens.append("ce_power")

## A text on your phone, one line, in Luna's or Pippa's pink.
label ce_text(who, what):
    "{color=#ff8fc8}[who]: [what]{/color}"
    return

## Route select's entry: your flat, after a shift.
label celestia_start:
    $ ce = VNState(tier=0, body=0, loft=0, power=0, forks={})
    $ ce_enc = VNState(partner_came=True, pc_orgasms=0, flipped=False)
    $ vn_clock = VNState(day=1, hour=19, minute=40)
    ## the HUD and the box portrait key on vn_route (twinetesting-03 spotted it unset, 2026-11-12)
    $ vn_route = "celestia"
    $ ce_pc_name = "Callum"
    if not renpy.session.get("vn_picks"):
        $ ce_pc_name = renpy.input("Your name? (Callum, unless you'd like another. Luna will call you something else.)", default="Callum", length=20).strip() or "Callum"
    $ ce_plate = ce_pc_name
    jump ce_opening

label ce_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"celestia"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    if ce.ending == "dark":
        centered "{size=+10}{color=#b06bd8}Black's Good on You{/color}{/size}\n\n{i}The end.{/i}"
    else:
        centered "{size=+10}{color=#f3c969}Starlit Showdown{/color}{/size}\n\n{i}The end.{/i}"
    jump start
