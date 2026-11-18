## Ledger -- "Nobody in the Demon Sect Will Say 'Cauldron' Out Loud, Not Even While They're Making Me
## One" (The Yin Blossom Ledger; rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside
## this file, signed off by the owner). From catalog/game/02-engine/storylines/ledger/ (ledger.js:
## the entries, the laces, the register, the routine, the pools; main.twee, rungs.twee), kept
## verbatim in catalog/docs/routes/vn-original/ledger/.
##
## THE NON-CON PASS (owner, 2026-10-19/20: escalating corruption). "He had no choice" returns as
## paperwork, never a threat: "You signed the vessel register. It doesn't have a column for asking."
## Rungs 1-2 non-con, no flip; rung 3 flips at the word ("Best cauldron I've ever had."); rung 4,
## the mandatory first offering, flips at the break; rung 5's knock is the consensual payoff ("If you
## want it, you have to say it."); rung 6 consensual. No tears, no pregnancy talk, nobody harmed.
##
## The PC is Ruan Jiu (the owner's choice, spec decision 2); the name box changes the given name,
## and the Hall registers "Jiu" whatever you're called. He/him to rung 4, she/her from the register's
## amendment on, the cock caged in the jade to the end. Vanripper only (the owner, 2026-11-12: the
## demon horns, tail and wings count like an animal TF). Free play (the intake line, the Hall after
## the ending, the after-hours scene) isn't ported. All route-local names carry led_.

init -10 python:
    LED = "art/ledger/"

    # THE LEDGER OF DEBTS: the five entries, oldest first, struck one a rung.
    LED_ENTRIES = [None,
        ("the bond, breached", "your great-grandfather"),
        ("the interest on the bond", "your grandfather"),
        ("the loan to pay the interest", "your great-aunt"),
        ("the arrears", "your father"),
        ("the arrears on the arrears", "your aunt, the cousins' mother"),
    ]

    # THE LACES: the cords that still close at dawn, by the highest rung landed.
    LED_LACES = [
        "No forms yet. Xue'er keeps eyeing your chest like a seamstress with a deadline.",
        "No forms yet. Xue'er keeps eyeing your chest like a seamstress with a deadline.",
        "Every cord still closes at dawn, and every one squeezes tight: the hip roll, the seat pad, both blossom-forms.",
        "The seat cord and both blossom cords still close. The hip cord won't meet. Gu has entered the hip roll as no longer required.",
        "Only the two blossom cords still close. The seat cord won't meet either; the seat pad is entered as no longer required.",
        "The blossom cords still close, laced a finger looser, and they still squeeze.",
        "No cords. Bai Lian cut the last two with her own scissors. The forms are in a lacquered box, receipted.",
    ]

    # GU'S REGISTER LINE, one per rung (7: the oath's addendum).
    LED_REGISTER = [
        "Intake. Constitution: yang burnt through. Worthless as a cultivator. Rare as a vessel.",
        "Vessel, first quality, on loan to the First Flower. Smooth as of the baths. Sleeps warm.",
        "One lock, jade, keyed; one key, issued to the First Flower. Retention: no wastage whatsoever. Horns budding, favourable.",
        "Livery issued. Dye set. Tails assigned, worn round the horns. Voice: sweet, after correction.",
        "Register amended, intake to Blossom. First offering entered in her own voice. Tail noted; it has opinions.",
        "Account settled. Cooling-off observed, per bylaw. Forms laced a finger looser; the vessel cites posture.",
        "Unlaced. No forms required. Supply problem unresolved: there is only one of her.",
        "Office filled. Addendum attached, re: wings, which were not ordered.",
    ]

    # THE HALL'S ROUTINE between rungs (setup.ledgerRoutine): by kind, then band (0 rungs 1-2,
    # 1 rungs 3-4, 2 rungs 5-6).
    LED_ROUTINE = {
        "baths": [
            ["Steam. Hot stone. A Blossom in the next pool looks at your smooth shins, then at her own, and sighs. \"Gu never does mine that well.\" \"First quality,\" you tell her. She splashes you.",
             "You float on your back and let the mineral water hold you up. Somewhere below, a pipe knocks. Your skin squeaks when you rub it. You rub it a lot.",
             "Xue'er sits on the edge with her feet in the water and gives you the gallery's gossip in order of filthiness. You come out pink and very well informed.",
             "The jade's warm from the water. You lie back and forget it's there, and your cock remembers for you, and pushes, and gets nowhere. {i}Nnh.{/i} \"Every time,\" says a Blossom across the pool, sympathetic. \"Every single time.\""],
            ["The water's hot enough to make you moan, so you moan. Two Blossoms across the pool applaud. You bow, waist-deep, tails dripping.",
             "You sink to the chin. Your hips are wider than they were on the stair, and the water knows it before you do: it laps differently. You grin at the ceiling.",
             "Your tail finds the warm current from the inlet and parks itself there. You didn't tell it to. Xue'er laughs so hard she slips off the step.",
             "You soap your own thighs and they're so soft you keep doing it. And doing it. A Blossom clears her throat. \"Clean now?\" \"Nearly,\" you say, and do your ass next, slowly, for an audience."],
            ["Your chest floats now. You lie on your back and watch it. A Blossom paddles over, looks, says \"Huh,\" with real respect, and paddles away.",
             "Steam, stone, and your own voice humming something sweet and high without your permission. It's a good song. You hum it louder.",
             "You wring out your tails and the whole bath turns to watch the red run off them. \"Show-off,\" says Xue'er. \"Yes,\" you say.",
             "Bai Lian comes down the steps, sees you, and stops on the bottom one with the water at her knees, just looking. You arch your back. She goes straight back up the steps again. Nothing off the books. Yet. You float there grinning."],
        ],
        "dressing": [
            ["The dressing room: mirrors on three walls, forms on a tray, Xue'er on a stool. \"Arms up.\" You start haggling over which cord goes first, and she has you laced before you finish. \"I've got a pool going,\" she says, \"on how long before you go and knock on her door yourself. Don't ruin it.\" \"Never,\" you say. She writes that down as a bet.",
             "Xue'er tugs a cord and you squeak. She tugs it again to hear it. \"Knowing they're false is part of the refinement,\" she recites. \"It's in the manual.\" \"Have you read the manual?\" \"Twice.\"",
             "You stand for your forms like a disciple stands for inspection. Chin up. Chest out. The blossom-forms ride high and round, and you check yourself in all three mirrors. Very convincing. Very false. Very funny.",
             "Xue'er laces the seat pad and gives it a squeeze to check the fill. You squeak. She squeezes again. \"Administrative,\" she says. \"Obviously.\" \"Obviously,\" you agree, and wiggle."],
            ["\"Hold still.\" Xue'er threads red cord through your tails and ties them off round the horns. \"There. If anyone asks, the horns are a hair ornament.\" \"Nobody's asked.\" \"Nobody would dare.\"",
             "The hip roll goes back in its box. Xue'er laces the rest and smacks your ass when she's done, purely administratively. It wobbles. She stares. \"That's new.\" \"That's mine,\" you say.",
             "The pool on you has moved, Xue'er says: how long before you knock on the First Flower's door unsummoned. She won't tell you which way. She does tell you two Blossoms owe her money already, and looks extremely smug about it.",
             "Your nipples have gone puffy enough that the blossom-forms rub them all morning. Xue'er laces you and you moan, right there, at the first pull. \"Already?\" she says. \"Every pull,\" you tell her. She pulls again, to check."],
            ["The blossom-forms go on over the real thing now, and the real thing pushes back. Xue'er puts her whole weight on the cord and it still won't sit flat. \"Posture,\" you say. \"Posture my arse,\" says Xue'er.",
             "\"Breathe out.\" You breathe out. The cords squeeze. Your nipples are hard against the silk before she's finished the bow. Xue'er notices, and says nothing, which is louder.",
             "Xue'er laces you and then just stands there with her hands on your hips. \"I'm going to miss doing this,\" she says. \"You're going to win the pool,\" you say. \"I know,\" she sniffs.",
             "Your tail keeps untying the bow Xue'er's just tied. She slaps it. It ties itself round her wrist instead and won't let go until she says sorry."],
        ],
        "drills": [
            ["Kneeling forms. Left knee, right knee, hands to thighs, chin up. You nail it first time. Xue'er, running the drill, sulks. \"Swordsman,\" you explain. \"Show-off,\" she says.",
             "Posture drills along the gallery: a book on your head, a cord across your chest. You walk the length twice without dropping it and take a bow. The book falls off.",
             "You run your old sword form in an empty alcove for the habit of it. Five Petals. Clean. Strong. Your hips are a little lazy on the turn. You don't notice. Yet.",
             "The bowing drill. Bend from the waist, chest out, chin down, the forms swinging. Xue'er walks down the line correcting everyone but you. \"Swordsman,\" you say again. \"Unbearable,\" she says again."],
            ["The pebble tray on your head, the syllable cards in Xue'er's hand. \"Sweet sells, not sad.\" You give her sweet. Your voice goes up and stays up. Two Blossoms clap.",
             "The sword form again. You start the turn and your hips finish it, all on their own, in a big round sway. You laugh so hard you have to sit down.",
             "Kneeling forms, with the forms on. You arch, chest out, thighs open, chin up, and hold it longer than anybody. \"Advertising,\" Xue'er notes. \"Selling,\" you correct her.",
             "Walking drills. Your thighs rub now, and your hips swing whether you swing them or not, so you swing them. All the way down the gallery and back. The Blossoms at the tonic line turn their heads like a row of lanterns in a breeze."],
            ["Voice drills are a formality now. You read the card in a voice so sweet the Blossom next to you loses her place. \"Sorry,\" you say, sweetly. You aren't.",
             "The kneeling drill. Your tail curls round your thigh and holds the pose for you. Xue'er gives up correcting anything and just watches.",
             "You lead the drill, because Xue'er's voice is hoarse from yelling about your chest. The Blossoms follow you. Chin up. Chest out. Very good.",
             "The kneeling drill, and your new chest makes the arch do something obscene. The whole room stops. Xue'er, very quietly: \"Can you not.\" You can not. You don't."],
        ],
    }

    # THE COOLING-OFF (rung 5): the climbs after the two authored ones.
    LED_COOLING = [
        "You grind the bedding in your cell until the mat squeaks, the forms laced on, hips rolling, and the jade won't let anything happen. {i}Nnnh.{/i} \"{i}Fuck{/i}— Senior Sister— {i}please{/i}—\" You say it to an empty room. The empty room doesn't help.",
        "Xue'er reports that the pool has moved. \"You were loud just now.\" \"How loud?\" \"Loud enough to move the pool.\" She's delighted. You leak through the jade just hearing about it.",
        "In the baths you put your face in the water and scream into it. A Blossom pats your back. \"Cooling-off?\" she says. \"I had one. It's the bylaw. You'll live.\" \"I won't,\" you say, and mean it.",
        "Gu finds you at the registry board, reading the notice again with your forehead on the wood. \"It's a very good bylaw,\" she says, kindly. \"I wrote it.\" You make a noise at her you didn't know you could make.",
    ]

    LED_ROWS = ["0", "1", "2", "2r", "3", "4", "5", "6d", "6"]

    def led_body(row):
        """The body takes the row, toward it and never back. Rows: 0 the stair; 1 the baths' scrub;
        2 the waist and the horn buds; 2r livery day's dye (the red tails, the hair longer); 3 the
        nipples and hips; 4 the thighs, the A and the tail; 5 the C and the voice; 6d the unlacing's
        real DD; 6 the oath's surge and the wings."""
        if LED_ROWS.index(str(row)) > LED_ROWS.index(led.row or "0"):
            led.row = str(row)

    def led_band():
        t = led.tier or 1
        return 0 if t <= 2 else 1 if t <= 4 else 2

    def led_routine(kind):
        led.routine_i = (led.routine_i or 0) + 1
        pool = LED_ROUTINE[kind][led_band()]
        return pool[led.routine_i % len(pool)]

    def led_register():
        n = led.landed or 0
        if led.burned:
            n = 7
        return LED_REGISTER[max(0, min(7, n))]

    def led_laces():
        if led.cut:
            return LED_LACES[6]
        return LED_LACES[max(0, min(5, led.landed or 0))]

    def led_page_name():
        return "the %s page" % led_surname

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "road" (his patched coat and the stair's dust), "white" (the intake white), "red"
    # (the Hall's red livery: over the laced forms to rung 5, over the real chest from the
    # unlacing), "nude" (always the jade), "flower" (the First Flower's robes, the ending).
    _led_have = {}

    def _led_has(n):
        if n not in _led_have:
            _led_have[n] = renpy.loadable(LED + n + ".png")
        return _led_have[n]

    def led_pc_file(face):
        r, fit = led.row or "0", led.fit or "road"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-haggling" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-haggling" % r]
        for n in names:
            if _led_has(n):
                return LED + n + ".png"
        return LED + names[-1] + ".png"

    def led_face_now():
        a = renpy.get_attributes("led_pc")
        return a[0] if a else "haggling"

    def _led_portrait(st, at):
        p = vn_art_file(led_pc_file(led_face_now()))
        crops = globals().get("ledger_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["ledger"] = lambda: DynamicDisplayable(_led_portrait)

    # The calendar: a rung a day, day 1 (the stair) a Monday.
    LED_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def led_weekday_name():
        return LED_WD[(1 + vn_clock.day - 1) % 7]

    vn_weekdays["ledger"] = led_weekday_name

    vn_sprite_image("led_pc", ("haggling", "outraged", "flushed", "wanting"), led_pc_file, who="pc")
    for _w, _faces in (("bailian", ("dry", "intent", "soft")), ("gu", ("pleasant", "writing")),
                       ("xueer", ("wicked", "delighted")), ("mohan", ("beaming",)), ("sanhe", ("stern",))):
        vn_sprite_image("led_" + _w, _faces, (lambda w: (lambda f: LED + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(LED) and _f.endswith(".jpg"):
            _n = _f[len(LED):-4]
            vn_register_bg("led_" + _n.replace("-", "_"), _f)
            vn_register_cg("led_" + _n.replace("-", "_"), _f)

    vn_register_route("ledger", "Nobody in the Demon Sect Will Say \"Cauldron\" Out Loud, Not Even While They're Making Me One",
        "Your yang meridians burnt through, and your family's name is three generations deep in the Nine Sorrows' Ledger of Debts. So you climb the black stair to sell the only thing you've got left. The finding: worthless as a cultivator, rare as a vessel. The First Flower claims you before the ink is dry. Five entries on the page, and she'll get you all five.",
        LED + "cover.jpg", "ledger_start")

    achievement.register("First Flower")

default led = VNState(row="0", fit="road", tier=0, landed=0)
default led_pc_name = "Jiu"
default led_surname = "Ruan"
default _led_t = ""

define led_you = VNChar("[led_pc_name]", who="pc", plate="#8a2a3a")
define led_bailian = VNChar("Bai Lian", who="led_bailian", plate="#d0a0b8")
define led_gu = VNChar("Elder Gu", who="led_gu", plate="#3a4a5a")
define led_xueer = VNChar("Xue'er", who="led_xueer", plate="#c0304a")
define led_mohan = VNChar("Mo Han", who="led_mohan", plate="#6a4a2a")
define led_sanhe = VNChar("Elder San He", who="led_sanhe", plate="#9aa0b0")
define led_clerk = VNChar("The clerk", who="clerk", plate="#6b6b78")
define led_blossom = VNChar("A Blossom", who="blossom", plate="#a0506a")

## THE LEDGER OF DEBTS: the family's page, the struck entries lined through in green, Gu's register
## line above it, the laces below. Words only, never a count.
screen led_page():
    zorder 60
    frame:
        xalign 0.5 ypos 50 xsize 820
        padding (30, 22)
        background Frame(Solid("#f3ead8f2"), 0, 0)
        vbox:
            spacing 8
            text "{color=#8a6a2a}Gu's register, in her hand:{/color} {i}%s{/i}" % led_register() size 22 color "#3a3a3a"
            if led.burned:
                text "{color=#8a6a2a}The Ledger of Debts:{/color} %s is ash. Gu kept the ash. It's receipted." % led_page_name() size 22 color "#3a3a3a"
            else:
                text "{color=#8a6a2a}The Ledger of Debts, %s:{/color}" % led_page_name() size 22 color "#3a3a3a"
                for _i in range(1, 6):
                    if (led.struck or 0) >= _i:
                        text "{s}%s: %s{/s}" % LED_ENTRIES[_i] size 22 color "#2f7a3a" xoffset 24
                    else:
                        text "%s: %s" % LED_ENTRIES[_i] size 22 color "#a0304a" xoffset 24
                if (led.struck or 0) >= 5:
                    text "Nothing owed." size 22 color "#2f7a3a"
            if led.laced or led.cut:
                text "{color=#8a6a2a}The laces:{/color} %s" % led_laces() size 22 color "#3a3a3a"

## A slip in Gu's hand: a receipt, the livery chit, the bylaw notice, the oath-form.
screen led_slip(title, lines):
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 720
        padding (30, 22)
        background Frame(Solid("#f6efdcf2"), 0, 0)
        vbox:
            spacing 8
            text "{b}%s{/b}" % title size 24 color "#5a2a1a"
            for _l in lines:
                text _l size 22 color "#2a2a2a"

label ledger_start:
    $ led = VNState(row="0", fit="road", tier=0, landed=0)
    $ vn_clock = VNState(day=1, hour=11, minute=0)
    $ vn_route = "ledger"
    $ led_pc_name = "Jiu"
    $ led_surname = "Ruan"
    if not renpy.session.get("vn_picks"):
        $ led_pc_name = renpy.input("Your name? (Jiu, unless you'd like another. The Ledger's page says Ruan either way, and the Hall registers you as Jiu.)", default="Jiu", length=20).strip() or "Jiu"
    jump led_opening

## THE HALL between rungs: Gu's register line and the page, then the routine (the baths, the dressing
## room once you're laced, the drills), one optional flavour beat that banks nothing, then on to
## led.next (set before the jump).
label led_hall:
    $ vn_enter(bg="led_hall", pc=("wanting" if (led.tier or 0) >= 4 else "haggling"), pc_tag="led_pc", cast=[], cg=None)
    "The registry calls it the Furnace Hall. Out loud, everybody says the Blossom Hall: lacquer, lamps, steam rising from the baths below, and Blossoms going past in twos, laced high, gossiping."
    show screen led_page
    "{size=-5}{color=#b7b7b7}The page, the register, the laces.{/color}{/size}"
    hide screen led_page
    $ _led_choices = [("The steaming baths", "baths")]
    if led.laced and not led.cut:
        $ _led_choices.append(("The dressing room", "dressing"))
    ## ff 2:06 am 11-18: a None value makes display_menu draw the item as an unclickable caption
    $ _led_choices += [("The drills", "drills"), ("Wait for Second Bell", "wait")]
    $ _led_pick = renpy.display_menu([(c, v) for c, v in _led_choices])
    if _led_pick != "wait":
        $ _led_t = led_routine(_led_pick)
        if _led_pick == "baths":
            $ vn_enter(bg="led_baths", pc="flushed", pc_tag="led_pc", cast=[], cg=None)
            "The steaming baths, under the Hall: mineral pools, hot black stone, steam thick enough to lean on."
        elif _led_pick == "dressing":
            $ vn_enter(bg="led_dressing", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
        else:
            $ vn_enter(bg="led_drills", pc="haggling", pc_tag="led_pc", cast=[], cg=None)
        "[_led_t]"
        $ _led_t = led_register()
        "{color=#b7b7b7}Gu goes past with a ledger under her arm, reading aloud to nobody: {i}[_led_t]{/i}{/color}"
        $ vn_pass(60)
    jump expression led.next

label led_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"ledger"}
    $ vn_route = None
    hide screen led_page
    hide screen led_slip
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}First Flower{/color}{/size}\n\n{i}The end.{/i}"
    jump start
