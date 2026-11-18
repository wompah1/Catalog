## THE SOURCE: ledger's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee), written as beats; the director scenes are in scenes.rpy.
## The original is in catalog/docs/routes/vn-original/ledger/. The paperwork is the atrocity and
## nobody threatens anybody; nobody says furnace or cauldron aloud (Bai Lian, once, at rung 3); no
## tears; no explanation of the tonics, the dye or the demon.

## ---- DAY 1, the stair and the intake (Ledger Opening, Appraisal, Claim) --------------------

label led_opening:
    $ led.fit = "road"
    $ vn_enter(bg="led_stair", pc="haggling", pc_tag="led_pc", cast=[], cg="led_stair_climb")
    show cg led_stair_climb onlayer cgl
    "The black stair. Straight up the hill, cut out of the rock, no rail."
    "You take the first stretch at a swordsman's pace. You take the rest at a beggar's."
    vn_sfx "{i}Haah. Haah.{/i}"
    "Your dantian sits in your belly like a cracked jar. A year ago you forced a breakthrough, the fire caught, the demon got in, and your yang meridians went up like paper. No sect takes a man who can't hold qi."
    "And the Ledger of Debts has your family in it. [led_surname], three generations deep, at interest."
    "So you're here to sell the one thing you've got left."
    "You want one thing for it. The name struck off that page. Your cousins are twenty-one and twenty-three, and they want to sit their sect's entrance trials, and nobody sits them under a name that's in a demon sect's book."
    hide cg onlayer cgl
    $ vn_enter(bg="led_altar", pc="haggling", pc_tag="led_pc", cast=[], cg="led_intake_line")
    show cg led_intake_line onlayer cgl
    "The top. A courtyard of black stone. A clerk at a table. A line."
    "An actual line. Orderly. Moving briskly. \"Next,\" says the clerk, and somebody steps up, and somebody behind you sighs."
    "The man in front of you is chewing his nails to the quick. You're doing sums."
    led_clerk "\"Next.\"\n{size=-5}{color=#ff8fa3}▸ Step up to the table{/color}{/size}"
    $ vn_pass(20)
    jump led_appraisal

label led_appraisal:
    $ vn_enter(bg="led_registry", pc="haggling", pc_tag="led_pc", cast=[("led_gu", "pleasant")], cg=None)
    "A side room. Incense. A desk, and the registry on it, open."
    "Elder Gu: fifty-eight, neat as a folded letter, ink on her cuffs, as pleased to see you as a pharmacist is to see a prescription."
    led_gu "\"Wrist.\""
    show cg led_pulse onlayer cgl
    "Three fingers on your pulse. Light. {i}Hm.{/i} Deeper. {i}Hm.{/i} Deepest. {i}Hmmm.{/i} She looks at your tongue. She presses two fingers under your navel, right on your dantian, and smiles like it's told her a joke."
    led_gu "\"Forced a breakthrough. Fire caught, the demon entered, the yang meridians went with it. Burnt clean through. A year ago?\""
    "Pleasantly."
    led_you "\"About that.\""
    led_gu "\"Here's the finding, and I want you to hear the good part. Burnt meridians will never spend qi again. Not a drop. Ever.\""
    "She lets it sit."
    led_gu "\"They'll only ever {i}hold{/i} it.\""
    hide cg onlayer cgl
    show screen led_slip("THE INTAKE REGISTER", ["{i}Worthless as a cultivator. Rare as a vessel.{/i}"])
    "She turns the registry round so you can read her hand."
    hide screen led_slip
    led_gu "\"First quality. The Hall has a supply problem, and you've just walked up the stair as the answer to it. That isn't flattery. It's an inventory note.\""
    led_gu "\"And the name.\""
    "She flips to a page near the back. {color=#ff9ad5}[led_surname]{/color}, in an old hand, then three newer ones."
    led_gu "\"Three generations, at interest. You'll want them struck.\""
    led_you "\"All five entries. That's my price.\""
    led_gu "\"Everyone has a price. Yours is reasonable. Name for the register.\""
    "She wets her brush."
    if led_pc_name == "Jiu":
        led_you "\"Ruan Jiu.\""
        "Gu checks a list pinned to the desk. The next name on it: {i}Jiu{/i}. She looks enormously pleased."
        led_gu "\"The list agrees with you. Tidy. Jiu.\""
    else:
        led_you "\"[led_surname] [led_pc_name].\""
        "Gu checks a list pinned to the desk."
        led_gu "\"The next name on the list is Jiu. You'll answer to it. Everyone here answers to the list.\""
        "She writes it."
    menu:
        "How do you sell it?"
        "Haggle":
            $ led.sold = "haggle"
        "Ask what a vessel's for":
            $ led.sold = "ask"
        "Hold your hand out for the brush":
            $ led.sold = "sign"
    jump led_claim

label led_claim:
    $ vn_enter(bg="led_registry", pc="haggling", pc_tag="led_pc", cast=[("led_gu", "writing")], cg=None)
    if led.sold == "haggle":
        led_you "\"Board's on the Hall. And the food. And the robes. You don't get to bill me for the robes.\""
        led_gu "\"Nobody bills the stock for the shelf. Noted. You're good at this.\""
        "Writing."
        led_you "\"I rehearsed on the stair.\""
    elif led.sold == "ask":
        led_you "\"What's a vessel for, exactly?\""
        led_gu "\"Holding. You hold. Somebody pours. It's very restful, I'm told.\""
        "She smiles."
        led_you "\"Who pours?\""
        led_gu "\"That's the next question.\""
        "She looks past you at the door."
    else:
        "You hold your hand out for the brush before she's finished the sentence."
        "Gu actually laughs."
        led_gu "\"Oh, I like you.\""
        "She lets you sign. It's a very nice brush."
    hide led_gu
    show led_bailian dry at vn_cast_slot
    hide cg onlayer cgl  # ff 2:01 am: no picture, claim failed 5 draws (SCENES.md ledger v5)
    "The ink's still wet when the door opens."
    "Tall. {i}Very{/i} tall. White silk, a pink sash, black hair in two long tails. Thirty-one, unhurried, with the face of a woman reading something mildly funny. Low on her thigh, under the silk, there's a heavy shape that is very much not part of the robe."
    "The clerk in the doorway goes quiet. {i}Irregular{/i}, the quiet says. Nobody says it."
    led_bailian "\"Mine.\""
    "Bai Lian, the First Flower, says it to Gu."
    hide led_bailian
    show led_gu pleasant at vn_cast_slot
    led_gu "\"On loan to the First Flower. One vessel, first quality.\""
    "Gu writes it down, murmuring."
    hide cg onlayer cgl
    "Bai Lian walks you out. Her hand sits at the small of your back the whole length of the corridor, warm through your coat, and drops lower on the turn, just once, just enough. In the corridor, not for the register, very low:"
    hide led_gu
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"Five entries. I'll get you all five. Walk on my left.\"{/b}\n{size=-5}{color=#ff8fa3}▸ Walk on her left{/color}{/size}"
    $ vn_pass(5)
    jump led_alcove

## RUNG 1, the appraisal alcove: stripped mid-haggle, wrists pinned to the mirror, her hand. "This part
## must be accounted for." Non-con, no flip: he objects all the way and comes shouting "don't stop".
label led_alcove:
    $ led.tier = 1
    $ vn_enter(bg="led_alcove", pc="haggling", pc_tag="led_pc", cast=[("led_bailian", "dry")], cg=None)
    "Mirrors. Every wall. A low platform, a lamp, incense. You, over and over, all the way back into the glass, in a patched coat with the stair's dust on it."
    "Bai Lian shuts the panel with one finger and sits on the edge of the platform, knees apart, robe open to the thigh."
    led_bailian "\"Clothes off.\""
    led_you "\"About that. The register said {i}vessel{/i}. It didn't say what a vessel takes off, or when, or for whom. Before anything comes off, I'd like the terms—\""
    $ led.fit = "nude"
    "She doesn't wait for the terms. She stands, a head taller than you, and her fingers are already at your sash. Coat off your shoulders. Sash. Trousers down round your ankles, while you're still talking."
    led_you "\"—in writing, is all I'm— {i}hey{/i}— I'm {i}negotiating{/i}—\""
    led_bailian "\"You signed the vessel register. It doesn't have a column for asking.\""
    "Folding your coat over the platform like a clerk."
    hide led_bailian
    show cg led_alcove_pinned onlayer cgl
    "You stand there bare, lean and sword-callused, in every mirror at once. You cover yourself. She moves your hands away, one wrist at a time, and pins both of them to the glass above your head with one long hand."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Breathe out.\""
    led_you "\"I didn't agree to—\""
    "Her other hand, clinical: two fingers at your throat for the pulse. A palm flat on your stomach, sliding down, mapping you the way a cultivator maps meridians. Her qi runs under your skin like a cold thread and stops dead where yours burnt out."
    "Lower. She cups your balls and weighs them like a merchant weighing silk. Thumbs the base of your cock. It jumps in her hand and starts to fill, and you glare at it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Still functional.\""
    led_you "\"That's not {i}agreement{/i}, that's {i}circulation{/i}—\""
    show cg led_alcove_hand onlayer cgl
    "And it stops being clinical."
    vn_sfx "{i}Shlk. Shlk. Shlk.{/i}"
    "Her fist closes. Long, slow strokes, root to tip, a squeeze at the head."
    show led_pc outraged
    led_you "\"Senior Sister— {i}stop{/i}— this isn't in the— {i}nnh{/i}—!\""
    "You yank at your wrists. The mirror doesn't give, and neither does she."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Don't come until I say.\""
    led_you "\"I'm not going to {i}come{/i}, I'm going to file a— {i}ahh{/i}— a {i}complaint{/i}—\""
    "Faster. Her thumb rubs the slit and slicks you with your own leaking. Your knees go. She holds you up by the wrists, against the glass. In every mirror a red-faced swordsman is pinned to it, fucking a woman's fist, hips jerking, mouth still arguing."
    led_you "\"Ahh— {i}ahh{/i}— no— I'm close, I'm— Senior Sister, let {i}go{/i}—\""
    "She squeezes the root. Hard. Everything stops." with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Not yet.\""
    led_you "\"{i}Fuck{/i}—!\""
    "She starts again. Slow. Then not slow. Her fist leaves your cock just long enough to roll your balls in her palm like she's counting them, then drifts up your chest, finds a nipple, and pinches."
    led_you "\"{i}Hah{/i}—!\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Sensitive.\""
    "She notes it, and does it again, and watches your cock jump in her fist every time she does."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Show me how you come. This part must be accounted for.\""
    led_you "\"It's {i}not{/i}— it's not part of the— {i}ahh{/i}— {i}ahhh{/i}—!\""
    "That's all it takes."
    show cg led_alcove_cum onlayer cgl
    show led_pc flushed
    led_you "\"{i}Ahhh{/i}— no— coming— I'm {i}coming{/i}— don't— don't {i}stop{/i}, don't stop, {i}don't stop{/i}—!\"" with vnfx("flash", "shake")
    "You shout it. Rope after rope into her cupped palm, hot and thick and far too much, hips bucking into her hand, wrists still pinned to the glass, every mirror in the alcove full of you losing it."
    "She watches the whole thing. Then she lets your wrists go, lifts her hand, and paints it across your chest, slow, collarbone to collarbone, like a brushstroke on a register."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"You'll do.\""
    hide cg onlayer cgl
    led_you "\"I want that— {i}haah{/i}— I want that {i}itemised{/i}.\""
    "You slide down the glass onto the platform, panting."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"It will be. That was half the appraisal.\""
    menu:
        "\"That was half the appraisal.\""
        "Tell her the other half isn't in the terms":
            jump led_alcove_count
        "Get dressed":
            $ vn_pass(10)
            jump led_intake_night

label led_alcove_count:
    $ vn_enter(bg="led_alcove", pc="outraged", pc_tag="led_pc", cast=[("led_bailian", "intent")], cg=None)
    led_you "\"The other half is {i}not{/i} in the terms. I read the register. Twice. On the stair.\""
    "You're still dripping. You're also, somehow, still hard."
    led_bailian "\"Of the appraisal.\""
    hide led_bailian
    show cg led_alcove_cock onlayer cgl
    "She opens her robe."
    "Her cock swings out of the silk like it's been waiting its turn: long, thick, flushed dark at the head, heavy enough to bob. Under it, a neat pussy, already glistening."
    "She takes both your wrists, turns your hands palm-up like she's reading them, and closes them round it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Hands. I want to see if you're any good at drills.\""
    led_you "\"I'm not doing drills, I'm doing {i}arithmetic{/i}, and this doesn't—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Show me.\""
    "Her hands close over yours. Squeeze."
    menu:
        "Her hands over yours."
        "Haggle the rate":
            $ led.alcove = "haggle"
        "Try to pull your hands back":
            $ led.alcove = "pull"
    jump led_alcove_sex

label led_alcove_after:
    $ vn_enter(bg="led_alcove", pc="outraged", pc_tag="led_pc", cast=[("led_bailian", "dry")], cg="led_alcove_hands_cum")
    show cg led_alcove_hands_cum onlayer cgl
    "She comes with a low hum, all over your knuckles and up your wrists, her hands still clamped over yours, and looks at the mess in the mirror with mild interest." with vnfx("flash")
    led_bailian "\"Good at drills. Noted.\""
    "You glare at her in every mirror at once. She almost grins back."
    led_you "\"That was two halves. I want it entered as two.\""
    led_bailian "\"It'll be entered as one appraisal. When the Hall says, there'll be another.\""
    "She wipes her hand on your hip, slowly."
    led_bailian "\"Get used to the Hall saying.\"\n{size=-5}{color=#ff8fa3}▸ Get dressed{/color}{/size}"
    $ vn_pass(10)
    jump led_intake_night

label led_intake_night:
    $ led.fit = "road"
    $ vn_enter(bg="led_cell", pc="haggling", pc_tag="led_pc", cast=[("led_bailian", "soft")], cg=None)
    "Your cell: a mat, a lamp, a hook, a narrow window full of moor. Bai Lian leaves you at the door."
    led_bailian "\"Baths at dawn. Gu will want you smooth. Sleep warm.\""
    "She looks at you a moment longer."
    hide led_bailian
    "You lie on the mat with her paint drying on your chest, drafting the objection you're going to lodge with Gu in the morning, clause by clause. Your cock twitches every time you get to the part about the mirrors."
    "You redraft the part about the mirrors a lot."
    call vn_night(6)
    jump led_strike

## ---- THE STRIKE at dawn (Ledger Strike, Strike Taken): the rung's change lands, Gu draws one line
## through the oldest entry and shows you, and you take it smug, grateful or filthy.

label led_strike:
    $ _led_n = max(1, min(5, led.tier or 1))
    $ led.landed = max(led.landed or 0, _led_n)
    if _led_n == 1:
        $ led.fit = "nude"
        $ vn_enter(bg="led_baths", pc="haggling", pc_tag="led_pc", cast=[("led_gu", "pleasant")], cg="led_scrub")
        "The baths, first thing. Steam. Hot stone. Gu, sleeves rolled to the elbow, with a jar of something pale that smells like a butcher's apron."
        led_gu "\"In. Sit. Lean back.\""
        show cg led_scrub onlayer cgl
        "She smears it on you: armpits, chest, legs, between the toes, along your jaw, over your balls with the same brisk thumb she used on your shins. Then the loofah. {i}Scrrrb. Scrrrb.{/i}"
        $ led_body(1)
        "{color=#ff5fb8}The hair comes off in dark drifts and floats away on the water. All of it. Everywhere. When she's done you're bare from your eyebrows down, and the skin squeaks under your own palm.{/color}"
        "{color=#ff5fb8}You run both hands down your thighs. Up your stomach. Over your chest. {i}Squeak. Squeak.{/i}{/color}"
        led_you "{color=#ff5fb8}\"Oh, {i}fuck{/i}, that's {i}obscene{/i}—\"{/color}"
        "{color=#ff5fb8}You do it again. And again. All of you is bare and slick, and it all goes straight to your cock.{/color}"
        "Your fingers keep curling round nothing, the exact grip her fist had on you in the alcove. Your hands remember it better than you do."
        led_gu "\"The Hall calls that finish {i}pearl{/i}. Refinement likes a smooth surface.\""
        hide cg onlayer cgl
        show led_xueer wicked at vn_cast_slot
        "A laugh from the steam. A Blossom: twenty-five, red-lipped, a robe that stops well short of anything, perched on the edge with her feet in the water."
        led_xueer "\"Not bad for a first scrub. I'm Xue'er. I'll be doing your forms. When you've got something to put them on.\""
        "She looks you up and down."
        led_you "\"Forms?\""
        led_xueer "\"You'll see. And don't ever say the word.\""
        "She leans in, wicked."
        led_you "\"Which word?\""
        led_xueer "\"The one for what you are. The plain one. The kitchen word. Never aloud. It's gauche, and Gu writes it down.\""
        "She mimes a pot."
        led_gu "\"Vessel. Provision. Blossom, eventually. We're very proud of the vocabulary.\""
        "Writing something down."
        hide led_xueer
        show cg led_pearl onlayer cgl
        "Bai Lian comes down the steps in a robe, crouches at the edge, and runs her thumb down your bare wet chest, collarbone to navel. It squeaks."
        hide led_gu
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Pearl.\""
        "She agrees. Your cock stands straight up out of the water. Both of you look at it. She flicks the head with one fingernail, {i}tik{/i}, and you yelp and your hips jump."
        hide led_gu
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Not yet.\""
        "And she goes back up the steps."
        hide cg onlayer cgl
        $ led.fit = "white"
        "Xue'er dries you off and puts you in the intake white, a plain hanfu that ties at the side. You sleep warm in it, the next nights, and never work out why."
        "{color=#ff5fb8}Your lips are tingling. You lick them, and it's like licking her thumb.{/color}"
        led_you "{color=#ff5fb8}\"{i}Mmh{/i}— oh, the {i}vocabulary{/i} isn't the only thing that's refined—\"{/color}"
    elif _led_n == 2:
        $ vn_enter(bg="led_dressing", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
        "The dressing room, at dawn. Xue'er pulls the forms off you to re-lace them and stops with the hip roll in her hands."
        led_xueer "\"Huh.\""
        $ led_body(2)
        show cg led_waist onlayer cgl
        "{color=#ff5fb8}Your waist. It goes {i}in{/i} now, under the ribs, as if the cords left a shape behind. You put both hands on it and squeeze and your fingers nearly meet.{/color}"
        led_you "{color=#ff5fb8}\"{i}Ohh{/i}— look at that— look at my {i}waist{/i}—\"{/color}"
        "{color=#ff5fb8}Your jaw's a step softer in the mirror. Inside the jade, your cock's smaller. It strains at the cage and fills less of it.{/color}"
        show cg led_horn_buds onlayer cgl
        "{color=#ff5fb8}And two little bumps at your hairline. Hard. Backswept. You touch one and it's {i}yours{/i}, warm, a nub of horn, and the touch goes straight down your spine like a lick.{/color}"
        "Your tongue keeps pressing the roof of your mouth where her head sat in the gallery. It knows the shape. You never practised that."
        led_xueer "\"Oh, those are {i}sweet{/i}. Gu! Gu, he's budding!\""
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Favourable. Noted.\""
        "From the corridor, not even looking up."
        hide cg onlayer cgl
        show led_bailian dry at vn_cast_slot
        "Bai Lian comes to see. She thumbs one horn bud, slow, round and round, and it goes through you like she's thumbing your cock."
        led_you "\"{i}Ahh{/i}— oh, that's— that's {i}sensitive{/i}—\""
        led_bailian "\"Good.\""
        "She taps the jade with a fingernail. {i}Tink.{/i} Your cock throbs against it and fills even less of it than yesterday."
        led_bailian "\"Smaller.\""
        "Like a compliment, and you take it as one."
        led_you "\"Good. I wasn't using it anyway.\""
        "You grin."
        "{color=#ff5fb8}Then you bite into your breakfast bun and moan so loud the whole dressing room turns round. Your mouth is {i}tender{/i}. Every bite is a kiss.{/color}"
        led_you "{color=#ff5fb8}\"{i}Mmmh{/i}— sorry— it's the {i}bun{/i}—\"{/color}"
    elif _led_n == 3:
        $ vn_enter(bg="led_dressing", pc="flushed", pc_tag="led_pc", cast=[], cg=None)
        $ led_body(3)
        "{color=#ff5fb8}You wake up and your nipples are the first thing you notice. Puffy. Pink. Tender against the robe, standing up through the silk.{/color}"
        led_you "{color=#ff5fb8}\"{i}Hhn{/i}—!\"{/color}"
        "{color=#ff5fb8}You pinch one through the silk to check. Your knees go. You pinch the other one.{/color}"
        led_you "{color=#ff5fb8}\"{i}Ahh{/i}— oh, that's not {i}fair{/i}—\"{/color}"
        show cg led_hips_three onlayer cgl
        "{color=#ff5fb8}Then your hips. The robe sits differently on them. When you walk to the dressing room, something rolls that didn't roll yesterday. Your ass, rounder, bouncing a little behind you on every step. You look back over your shoulder at it twice.{/color}"
        "You press your arms in under the blossom-forms on the way to the mirror, the squeeze she liked last night. Your body filed that one all by itself: {i}Squeeze. Smile. Sell it.{/i}"
        show led_xueer delighted at vn_cast_slot
        "Xue'er laces the hip roll on, pulls, pulls, pulls. The cord won't meet. The ends sit there, apart, and nothing on earth will close them."
        led_xueer "\"Gu. Hip roll.\""
        "Very pleased."
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"No longer required.\""
        "Writing it. The hip roll goes in a box."
        hide led_xueer
        show cg led_mirror_three onlayer cgl
        "Bai Lian, behind you in the mirror, puts both hands on your new hips and squeezes. They give. She squeezes again, harder, to watch them give. Then one hand comes round and pinches a puffy nipple through the silk."
        led_you "\"{i}Eek{/i}—!\""
        "It comes out high and sweet and absolutely yours. Xue'er applauds."
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Keep that voice.\""
        "{color=#ff5fb8}She kisses you, quick, in the mirror, and your knees fold. Your mouth's gone so sensitive a kiss is half a climax, and the forms squeeze your nipples on the way down.{/color}"
        led_you "{color=#ff5fb8}\"{i}Ahh{/i}— Senior Sister— {i}warn{/i} me—\"{/color}"
    elif _led_n == 4:
        $ vn_enter(bg="led_cell", pc="flushed", pc_tag="led_pc", cast=[], cg=None)
        $ led_body(4)
        "{color=#ff5fb8}You get out of bed and your thighs touch. All the way up. Soft, heavy, rubbing when you walk, and your ass follows you round the room like it's been invited.{/color}"
        show cg led_four_mirror onlayer cgl
        "{color=#ff5fb8}The mirror: lips fuller. Face rounder. Red tails down past your shoulder blades now, longer than the dye left them. And on your chest, under the puffy nipples, the faintest soft swell. An A, barely. Enough to jiggle when you bounce on your heels, so you bounce on your heels.{/color}"
        led_you "{color=#ff5fb8}\"{i}Hah{/i}— look— they {i}move{/i}—\"{/color}"
        "{color=#ff5fb8}In the jade, almost nothing; a soft little nub, curled up in the cage like it's hiding. You tap the jade. Nothing. Not a twitch. It doesn't get hard any more. It doesn't even try.{/color}"
        led_you "\"Huh. It's {i}decorative{/i} now.\""
        "Delighted. Your hole flexes when you walk, slow, breathing out on its own, exactly the way Gu's formulary said. {i}Receptive.{/i}"
        show cg led_tail onlayer cgl
        "{color=#ff5fb8}And behind you, swishing, there's a tail. Black, slim, ending in a spade. It flicks at the mirror. It flicks at Xue'er. When Gu comes in with the Ledger it goes stiff and points at her like it's got a complaint to file.{/color}"
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Opinions. It has opinions.\""
        "Writing."
        show led_xueer delighted at vn_cast_slot
        led_xueer "\"Seat pad.\""
        "She tries the seat pad and sings it. The cord won't meet."
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"No longer required.\""
        hide led_xueer
        hide cg onlayer cgl  # ff 2:01 am: no picture, knead failed 5 draws (SCENES.md ledger v5)
        "Bai Lian takes two big handfuls of your ass in the mirror and kneads, slow, like dough. Your thighs squeeze together on their own. Your tail swats her hand. She swats it back, and it curls up, sulking, and then sneaks back round her wrist anyway."
        "Her eyes drop to the jade in the mirror, and the nub curled up in it."
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Look at that. All that yang, locked in a box, and not one drop of it worth a thing. Everything worth having flows the other way now.\""
        "She doesn't touch it."
        led_you "\"I don't need it. I don't {i}need{/i} it. Squeeze harder.\""
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Junior sister. You're going to be trouble.\""
        "Into your hair."
        led_you "\"Yes. {i}Yes.{/i}\""
        "You moan it, pushing your ass back into her hands."
        "{color=#ff5fb8}Her kneading goes straight through you. Your ass is so sensitive now that sitting down on the dressing stool makes you squeal, and your little buds tingle sweetly under the forms.{/color}"
        led_you "{color=#ff5fb8}\"{i}Hah{/i}— everything's so {i}awake{/i}—\"{/color}"
    else:
        $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_five_wake")
        show cg led_five_wake onlayer cgl
        "You wake in Bai Lian's bed. Her arm over your waist. Your tail is wrapped round her wrist, all on its own, holding on like it lives there."
        $ led_body(5)
        led_you "{color=#ff5fb8}\"Morning.\"{/color}"
        "{color=#ff5fb8}You say it, and stop. The voice is high, light, sweet, and it's yours. It just woke up that way.{/color}"
        "{color=#ff5fb8}Your chest throbs, hot and full. You look down. Under last night's forms, still laced, there's something pushing back: soft, swollen, filling the silk from underneath.{/color}"
        "Bai Lian's awake. She slides one hand under the edge of a blossom-form and cups what's underneath, warm and tender and new, and you moan into her pillow."
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Posture.\""
        "Very dry."
        "{color=#ff5fb8}You get your own hands under the forms. A C-cup's worth, soft and hot and tender, spilling round your fingers. You squeeze, and moan so loud she puts her hand over your mouth.{/color}"
        led_you "\"{i}Mmmf{/i}— they're {i}real{/i}— Bai Lian, they're—\""
        show led_bailian dry at vn_cast_slot
        led_bailian "\"I know. I'm holding one.\""
        "{color=#ff5fb8}You roll out of bed and the rest of you comes with you: hips gone wide and curved, ass heavy and round enough to sway on its own, red tails down to the small of your back.{/color}"
        "In the long mirror you catch yourself arching, chin down, eyes up, ass out, like a Blossom of ten years. Nobody drilled that. It's just there."
        hide cg onlayer cgl
        $ vn_enter(bg="led_dressing", pc="wanting", pc_tag="led_pc", cast=[("led_xueer", "delighted")], cg=None)
        "At the dressing room Xue'er laces the blossom-forms on over it, a finger looser, and they still squeeze. She stares at your cleavage, which shouldn't exist, and then at you."
        led_you "\"It's the posture drills.\""
        led_xueer "\"It's the {i}posture drills{/i}. Gu. Gu, she says it's the posture drills.\""
        "To the ceiling."
        "{color=#ff5fb8}The forms squeeze, and your real breasts answer like a mouth on them. You lick your lips and moan. You sit, and your ass hums.{/color}"
        led_you "{color=#ff5fb8}\"{i}Mmh{/i}— everything's {i}louder{/i} than the drills—\"{/color}"
    hide cg onlayer cgl
    $ led.struck = _led_n
    show cg led_strike_line onlayer cgl
    "Gu opens the Ledger on the dressing table, finds the page, wets the brush, and draws one clean line. Then she turns it round so you can see it, because people like to see it."
    show screen led_page
    if _led_n == 5:
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Account settled. Nothing owed. The name's clean. Congratulations. That's never happened on this page.\""
        "She blots it."
    menu:
        "How do you take it?"
        "Smug":
            $ led.took = "smug"
        "Grateful":
            $ led.took = "grateful"
        "Filthy":
            $ led.took = "filthy"
    hide screen led_page
    hide cg onlayer cgl
    if led.took == "smug":
        if _led_n == 1:
            led_you "\"Great-grandad's bond. First round to me.\""
            "Arms folded."
        elif _led_n == 2:
            led_you "\"That's Grandad's interest. Paid. Look at me. I'm winning.\""
            "You lean in to the mirror and admire your horns."
        elif _led_n == 3:
            led_you "\"Great-auntie's loan. Gone. Three down. I'm very good at this.\""
            "You toss your tails."
        elif _led_n == 4:
            led_you "\"Dad's arrears. He'd hate this. I love it.\""
            "You plant a hand on your hip. Your hip has a lot of room for a hand now."
        else:
            led_you "\"Settled. The whole page. Me. Nobody else could've done that.\""
            "You stretch until the forms creak."
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Insufferable.\""
        "She blots it, approvingly, and writes that down too."
    elif led.took == "grateful":
        if _led_n == 1:
            "You stare at the line a long time."
            led_you "\"Thank you.\""
            "And you mean it, which annoys you enormously."
        elif _led_n == 2:
            led_you "\"Thank you. Really. Thank you.\""
            "Gu pats your horn, once, briskly, then looks at her hand, surprised at herself."
        elif _led_n == 3:
            "You hug Xue'er. She squeaks. You hug Gu. Gu permits it, briefly, holding the brush out of the way."
        elif _led_n == 4:
            led_you "\"Thank you.\""
            "You whisper it, and the new soft voice makes it sound like a kiss. Xue'er clutches her chest."
        else:
            "You laugh. Big, helpless, happy laughter, in a sweet high voice, until you have to hold on to the dressing table. Xue'er laughs too, and hugs you, forms and all."
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Don't thank me. Thank the account. It balanced.\""
    else:
        if _led_n == 1:
            led_you "\"One entry for one wank. Tell your Hall I'll take that rate all day.\""
            "You grin."
        elif _led_n == 2:
            led_you "\"That's Grandad's interest. Paid. By my mouth.\""
            "You announce it to the whole dressing room."
        elif _led_n == 3:
            led_you "\"Great-auntie's loan, paid off with my tits— with the forms. Same thing. Nearly.\""
            "You laugh."
        elif _led_n == 4:
            led_you "\"Dad's arrears, paid with my ass. Not my cock. My cock's never paid for anything. He'd die. Write that down.\""
            "Loudly."
        else:
            led_you "\"Settled. Paid in full. On my knees. Face-down. {i}Loudly.{/i}\""
            "You moan it, and squeeze your own new chest through the silk."
        hide led_xueer
        show led_gu pleasant at vn_cast_slot
        led_gu "\"Not that. Something with fewer nouns.\""
        "Gu writes something, kindly."
    $ led.next = ["", "led_summons_jade", "led_summons_livery", "led_summons_offering", "led_summons_terrace", "led_unlaced"][_led_n]
    "{size=-5}{color=#ff8fa3}▸ Into the Hall{/color}{/size}"
    jump led_hall

## ---- RUNG 2, the jade (Ledger Summons Jade, Jade, First Lacing, Lacing Tied, Gallery Mirror,
## Strut): the jade fitted while he argues the clause; the first lacing; the gallery mirror, non-con,
## no flip; the strut out of pure haggler's pride.

label led_summons_jade:
    $ vn_until(19)
    $ led.tier = 2
    $ vn_enter(bg="led_hall", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
    "Second Bell. Xue'er comes down the gallery at a trot and stops in front of you with a slip of paper between her teeth. She spits it into your palm."
    led_xueer "\"Registry. Now. The First Flower's paid for something, and Gu wants it fitted before the ink dries. Bring nothing. You don't own anything anyway.\""
    "Her eyes drop to your crotch. She grins.\n{size=-5}{color=#ff8fa3}▸ Go to the registry{/color}{/size}"
    $ vn_pass(5)
    jump led_jade

label led_jade:
    $ vn_enter(bg="led_registry", pc="haggling", pc_tag="led_pc", cast=[("led_gu", "pleasant")], cg=None)
    "The registry: black lacquer, red lacquer, scrolls in racks, and a high stool. Gu at the desk. Bai Lian against the wall with her arms folded."
    led_gu "\"Robe up. Stand there.\""
    led_you "\"Before I stand anywhere, I'd like to see the clause that—\""
    hide led_gu
    show cg led_jade_fit onlayer cgl
    "Bai Lian comes off the wall and lifts your robe for you, and holds it, bunched in one fist at your hip."
    "Gu doesn't measure. She looks, head tilted, one eye shut, the way a potter looks at clay."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Mm. That one.\""
    "From a drawer: pale green jade, carved all over with tiny characters, warm as if somebody's been holding it."
    led_you "\"That's a {i}lock{/i}. Nobody said lock. Where in the register does it say—\""
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Provisions, sundries. Unspent yang is the engine.\""
    "She fits the ring behind your balls with brisk cool fingers while you try to step back and Bai Lian's fist in your robe doesn't let you."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Think of a kiln. You've no yang to spend, which is why you're efficient. You do have habits. Habits are wastage.\""
    led_you "\"A cock is not a {i}sundry{/i}—\""
    "Your cock twitches at her touch and starts to swell. She fits the cage over it anyway."
    vn_sfx "{i}Click.{/i}" with vnfx("shake")
    $ led.jade = True
    "The swelling hits jade and stops. Cold. Snug. You can feel your own heartbeat in it."
    "Then the little carved characters warm, all at once, and something cool settles down through the cage into you, quiet as a seal pressed into wax: {i}Locked. Kept. Not yours to spend.{/i}"
    show led_pc outraged
    led_you "\"Ohh— oh, {i}fuck{/i}— take it {i}off{/i}— it's {i}tight{/i}—\""
    "You squirm. It doesn't care."
    "Bai Lian crouches, still holding your robe up, and flicks the cage with one fingernail. {i}Tink.{/i} Your cock surges against the jade and gets nowhere at all, and you moan so loud the clerk next door drops something."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Every time you get hard in that, think about whose belt the key's on.\""
    "Very close."
    led_you "\"I'm going to be thinking about {i}unlocking{/i} it—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"No. You're going to be thinking about me. That's the engine.\""
    show led_gu pleasant at vn_cast_slot
    led_gu "\"It's correct.\""
    hide cg onlayer cgl
    show screen led_slip("RECEIPT", ["One lock, jade, keyed.", "One key, issued to the First Flower."])
    "She writes, and holds up a tiny key, carved like a blossom. Bai Lian takes it and clips it to her belt beside her sash. It swings when she breathes. You watch it swing."
    hide screen led_slip
    led_you "\"Is the lock on the account, or off it?\""
    show led_gu pleasant at vn_cast_slot
    led_gu "\"On it. Everything's on it. That's what an account is.\""
    led_you "\"Then I want a discount for wearing it under protest.\""
    "Gu genuinely considers it."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"No. But I'll note the protest.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Good. Dawn. Xue'er laces you. Don't touch it.\""
    "At the door. Then, to you."
    led_you "\"I {i}can't{/i} touch it.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Then you'll find that easy.\"\n{size=-5}{color=#ff8fa3}▸ Sleep, badly{/color}{/size}"
    call vn_night(5)
    jump led_first_lacing

label led_first_lacing:
    $ led.laced = True
    $ led.fit = "white"
    $ vn_enter(bg="led_dressing", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg="led_forms_tray")
    "Dawn. The dressing room: mirrors on three walls, a bench, and Xue'er with four padded forms on a tray like breakfast."
    led_xueer "\"Morning, smoothling. Arms up.\""
    led_you "\"What are those?\""
    show cg led_forms_tray onlayer cgl
    led_xueer "\"Your figure. Hip roll. Seat pad. And these are your blossom-forms.\""
    "She holds them up one at a time: two round pink silk blossoms, cords trailing."
    led_you "\"They're obviously fake.\""
    led_xueer "\"Everybody knows they're false. Knowing they're false is part of the refinement. It's in the manual. I've read the manual. Which first?\""
    "Cheerfully. She jiggles the tray."
    menu:
        "\"Which first?\""
        "Hips first":
            "\"Hips first. Always hips first, or the waist sits wrong and Gu writes it down.\" {i}Creak.{/i} The hip roll hugs tight. Then the seat pad. Then the blossoms."
        "The seat pad first":
            "\"Seat first? Bold.\" The pad goes on high and round. You look back over your shoulder and there's a little peach where your flat swordsman's ass used to be. You wiggle it. Xue'er snorts."
        "The blossoms first":
            "\"Greedy.\" She presses a form to your flat chest, laces it round your back, then the other. Two round silk tits riding high. You look down at them and burst out laughing."
    show cg led_laced onlayer cgl
    led_xueer "\"Breathe out. {i}Out.{/i} Don't tell me it's tight. I know it's tight. Mine took a year.\""
    "She hauls. The cords cross your back and squeeze. All four."
    "The mirror: hips, a peach, a pair of high round blossoms, a bare smooth face, and the jade pushing a little bump into the front of your robe."
    led_you "\"Very convincing.\""
    led_xueer "\"Not even slightly. That's the refinement. Gallery. Go. Walk like you mean them.\""
    "She smacks the seat pad."
    hide led_xueer
    "Bai Lian, in the doorway, with the key swinging at her belt. She walks round you once. She weighs a blossom-form in her palm like it's real and lifts it a finger higher on the cord."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Higher. I want them in his face when he looks down.\""
    "She tells Xue'er. You look down. They're in your face. Your cock tries to stand up in the jade and can't, and you whimper, and she smiles.\n{size=-5}{color=#ff8fa3}▸ Out to the gallery{/color}{/size}"
    $ vn_pass(15)
    jump led_gallery_mirror

## RUNG 2, the gallery mirror: a hand on his shoulder puts him on his knees, her thumb opens his jaw
## mid-objection, the Hall walks past. Non-con, no flip.
label led_gallery_mirror:
    $ vn_enter(bg="led_gallery", pc="haggling", pc_tag="led_pc", cast=[], cg="led_gallery_walk")
    show cg led_gallery_walk onlayer cgl
    "The gallery's full. Morning rush: Blossoms in twos and threes, laced high, lining up for tonic, gossiping. Every one of them looks at you."
    led_blossom "\"Too high. He'll choke when he bows.\""
    "Somebody else" "\"First Flower's new one. Is he, now.\""
    "You walk the whole length with your forms bouncing and your chin up, like a man walking out to a duel he's already lodged a complaint about."
    show cg led_gallery_kneel onlayer cgl
    "At the end there's a mirror set into an alcove, and Bai Lian in front of it. She crooks a finger."
    "Her hand on your spine, pushing it straight. Her other hand cupping a blossom-form like she's checking fruit."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Chest forward. Shoulders in. Kneel.\""
    "Quietly."
    led_you "\"In the {i}gallery{/i}? Senior Sister, there are— that's a {i}public{/i}—\""
    "Her hand settles on your shoulder, and your knees hit the floor. The gallery keeps walking past. In the mirror: you on your knees, forms riding high, and her robe falling open."
    "Her cock swings out, heavy and flushed and already hard, and bumps your cheek."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Open.\""
    led_you "\"Absolutely not, I want it noted that—\""
    show cg led_gallery_mouth onlayer cgl
    "Her thumb on your chin pulls your jaw down mid-word, and she feeds it to you. Slow. The fat head on your tongue, then past your teeth, her fist in your hair holding you exactly where she wants you. {i}Glk.{/i}" with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Breathe out. Slow. Tongue.\""
    led_you "\"Mmf— {i}mmmf{/i}—!\""
    "You shove at her thighs. She doesn't move. A Blossom walking past giggles. Another one stops with a tray in her hands and just watches."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Hold the forms up. I want them jostling.\""
    "You don't. She arches your back for you with a hand at the base of your spine, and the forms bounce on every stroke anyway. {i}Glk. Glk. Hlk.{/i} Drool runs down your chin onto the silk. In the jade your cock throbs and gets nowhere, and you moan about it, loud, round her."
    led_you "\"Mmnh— nnt in the— {i}mmf{/i}—!\""
    "Long, slow strokes, all the way in until your nose is in her and your eyes roll back, then out so you can gasp, then in. The gallery goes past. Somebody behind you is taking bets on how long before he comes knocking on her door for this."
    led_blossom "\"He's good.\""
    "Murmured to another, like she's judging a dumpling."
    "Somebody else" "\"He's new. He'll get better.\""
    "You try to tell them exactly what you think of that. It comes out round a mouthful of the First Flower as a long, wet, shameless moan, and they both nod as if you'd agreed."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Look up.\""
    "You look up. In the glass and in the flesh, she's watching your face."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Don't come.\""
    "And then she smiles, because you can't."
    show cg led_gallery_cum onlayer cgl
    "She pulls out, takes herself in her fist, and holds you there by the hair while she finishes across the blossom-forms. Rope after rope, white on pink silk, on your chin, on the forms, dripping into the laces." with vnfx("flash")
    led_you "\"{i}Haah{/i}— haah— that was— that was {i}not{/i}—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Don't clean them. Let the Hall see.\""
    "Tucking herself away. She's still hard. She hasn't let go of your hair."
    menu:
        "She hasn't let go of your hair."
        "Try to get up":
            jump led_mirror_sex
        "Strut till noon":
            jump led_strut

label led_mirror_after:
    $ vn_enter(bg="led_gallery", pc="flushed", pc_tag="led_pc", cast=[], cg="led_gallery_cum")
    show cg led_gallery_cum onlayer cgl
    "Second load, her hand in your hair holding you right where she wants you. You swallow because she doesn't leave you anywhere else to put it, and some gets away down your chin onto the forms. Somebody applauds." with vnfx("flash")
    "{size=-5}{color=#ff8fa3}▸ Strut till noon{/color}{/size}"
    jump led_strut

label led_strut:
    $ vn_enter(bg="led_gallery", pc="haggling", pc_tag="led_pc", cast=[], cg="led_strut")
    "Fine. If the Hall wants a display, the Hall gets a {i}good{/i} one."
    show cg led_strut onlayer cgl
    "You strut. All morning. Up the gallery, down the gallery, past the tonic line, past the dressing room, through the steam at the baths' doorway and back, with the First Flower's come drying white across your blossom-forms."
    "The Blossoms look. They laugh. A couple applaud. One curtsies. You curtsy back, badly, forms bouncing, and get a cheer."
    "A senior Blossom" "\"First Flower's?\""
    "She stops you by the tonic line, looks at the drying white on your chest, and sniffs."
    led_you "\"First Flower's.\""
    "You stick your chest out further, because if you don't you'll go red."
    "A senior Blossom" "\"Hm. You're enjoying this.\""
    "She looks at you properly."
    led_you "\"I'm {i}negotiating{/i} this.\""
    hide cg onlayer cgl
    show led_xueer wicked at vn_cast_slot
    led_xueer "\"Barely moved in, and he's already showing off. I've started a pool. How long before you go and knock on her door for it yourself.\""
    "Falling in beside you."
    led_you "\"Never.\""
    led_xueer "\"That's what everyone puts. It's the cheapest square on the board.\""
    "Gu goes past at noon and makes a note without slowing down."
    $ vn_until(12)
    $ led.next = "led_night_two"
    jump led_hall

label led_night_two:
    $ vn_enter(bg="led_cell", pc="haggling", pc_tag="led_pc", cast=[], cg=None)
    "The afternoon goes. The bells go. Your cell, the lamp, the mat, and the forms still laced on because you couldn't face asking Xue'er to take them off."
    call vn_night(6)
    jump led_strike

## ---- RUNG 3, livery day (Ledger Summons Livery, Dye, Livery Drills, Terrace, Forms): the dye
## sets in the qi; the voice drills; the Terrace argument; then the forms with the door open, which
## flips at the word.

label led_summons_livery:
    $ vn_until(19)
    $ led.tier = 3
    $ vn_enter(bg="led_hall", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
    "Second Bell, and Xue'er with a bowl under a cloth."
    led_xueer "\"Livery day at dawn. Gu's mixed the dye. Sleep on your back; you'll want your face for it.\""
    led_you "\"What's under the cloth?\""
    led_xueer "\"Your new hair. Smells like a tannery fell in a teapot. You'll love it.\""
    "She sniffs it and reels.\n{size=-5}{color=#ff8fa3}▸ Sleep on your back{/color}{/size}"
    call vn_night(5)
    jump led_dye

label led_dye:
    $ vn_enter(bg="led_dressing", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg="led_dye")
    "The dressing-room stool. Xue'er behind you with a horn spoon."
    led_xueer "\"Head back.\""
    show cg led_dye onlayer cgl
    "The dye's cold and it stinks, and it goes on by the fistful, all through your hair, down to the scalp, worked in round your little horns."
    led_xueer "\"Sets in the qi. Cut it off and it grows back the same.\""
    led_you "\"Does it?\""
    led_xueer "\"Don't ask me how. Don't ask Gu either. She'll tell you, and it's very boring.\""
    $ led_body("2r")
    "{color=#ff5fb8}Rinse. The basin runs red. She combs it out, and it's longer when she combs it out than when she combed it in: past your shoulders, down your back, heavy and silky, pouring through her fingers.{/color} Xue'er doesn't mention it. Neither do you."
    "She sections it, ties it high in two tails, and winds red cord round the base of each one, right round your horns."
    led_xueer "\"There. If anyone asks, the horns are a hair ornament.\""
    show cg led_red_tails onlayer cgl
    "{color=#ff5fb8}The mirror: red. Bright, glossy, lacquer red, two tails swinging when you turn your head. A soft bare face. Little backswept horns poking up through it all like they were always meant to.{/color}"
    led_you "\"Look at me!\""
    "You burst out laughing."
    led_xueer "\"I'm looking. I'm very good.\""
    hide cg onlayer cgl  # ff 2:01 am: no picture, handles failed 5 draws (SCENES.md ledger v5)
    "Bai Lian comes in behind you, takes a tail in each fist, and tips your head back by them until you're looking up at her upside down."
    hide led_xueer
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Handles.\""
    led_you "\"{i}Oh{/i}.\""
    "High, and your cock throbs in the jade so hard you go cross-eyed."
    hide cg onlayer cgl
    show screen led_slip("LIVERY CHIT", ["One livery, red, issued.", "One dye, applied; sets in the qi.", "One pair of tails, assigned."])
    "Gu comes in with a slip and reads it aloud. She hands you the slip to keep, as if you might want to frame it. You might."
    hide screen led_slip
    $ led.fit = "red"
    "Xue'er puts you into the red, laces all four forms under it, every cord snug, and steps back."
    hide led_bailian
    show led_xueer wicked at vn_cast_slot
    led_xueer "\"Drills. Now you sound like a swordsman in a dress. Let's fix that.\"\n{size=-5}{color=#ff8fa3}▸ The practice room{/color}{/size}"
    $ vn_pass(30)
    jump led_livery_drills

label led_livery_drills:
    $ vn_enter(bg="led_drills", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "delighted")], cg="led_pebbles")
    show cg led_pebbles onlayer cgl
    "The practice room. A tray of pebbles balanced on your head. Xue'er with a fan of syllable cards."
    led_xueer "\"{i}Han. Xia. Qing. Mei.{/i} Again. Smile at the end. Sweet sells, not sad.\""
    "She sings it, high and sweet."
    led_you "\"Han— xia—\""
    "It cracks. The tray wobbles."
    led_xueer "\"Again.\""
    led_you "\"{i}Han, xia, qing, mei.{/i}\""
    "Higher. Sweeter. The tray holds. Two Blossoms in the doorway clap."
    led_xueer "\"Again.\""
    "A few rounds in, your voice goes up and doesn't come back down. You say \"oh!\" in surprise and it comes out of you like a little bell."
    led_xueer "\"There it is. Sweet.\""
    "Bai Lian passes the door, stops, reaches in, and tugs one of your new tails, just once, on her way past."
    led_you "\"{i}Ah{/i}—!\""
    "Up it goes: a high, sweet, helpless little note, straight out of you."
    led_xueer "\"Perfect. Do that again. Exactly that. Selling, not sad.\""
    "Writing it on a card."
    show cg led_sword_sway onlayer cgl
    "Then, for the habit of it, the sword form, in the empty alcove at the end. Five Petals. Stance. Sweep. Turn—"
    "And your hips finish the turn for you, all on their own, in a big round sway that sends both tails flying."
    "You stop. You stare at your own hips. Then you laugh so hard you have to sit down on the floor."
    led_xueer "\"Was that a {i}sword form?{/i}\""
    led_you "\"It {i}was{/i}. It was a very good one.\""
    "Wheezing it, in your new sweet voice.\n{size=-5}{color=#ff8fa3}▸ Up to the Terrace for petitions{/color}{/size}"
    $ vn_until(14)
    jump led_terrace

label led_terrace:
    $ vn_enter(bg="led_terrace", pc="haggling", pc_tag="led_pc", cast=[("led_sanhe", "stern")], cg=None)
    "The Audience Terrace: open black stone, the whole Hall in rows, you in the Blossom line in your new red with your forms laced high."
    "A visitor. Elder San He, of Violet Tranquility: fifty-two, pale robes, a voice built for big halls. Orthodox. She looks at the Blossom line like it's a stain on the floor."
    led_sanhe "\"You pluck the weak. You turn people into lines in a book and call it refinement. A righteous sect would never—\""
    show led_mohan beaming at vn_cast_slot
    "Mo Han strolls out of the colonnade with his hands behind his back and a biscuit in one of them. The Cult Leader: forty-nine, round, beaming, the kind of man who remembers your birthday."
    led_mohan "\"Elder. Welcome. Do you want the argument or the answer?\""
    led_sanhe "\"I—\""
    led_mohan "\"The answer, then. Your sect works its outer disciples to death in the spirit-stone veins and doesn't count them. So does mine. So does everyone's. We write ours down. You don't. That's the whole difference. Make of it what you like.\""
    "Cheerfully. He spreads his hands."
    "The Terrace is very quiet."
    "Elder San He opens her mouth. Nothing comes out."
    led_mohan "\"Take your tribute and go home with a clean conscience. It's a lovely walk down.\""
    "Kindly. She goes."
    "You stand in the line trying to think of the answer. There isn't one. Mo Han stops beside you on his way past."
    led_mohan "\"You look like you're doing sums. Biscuit?\""
    menu:
        "\"Biscuit?\""
        "Take the biscuit":
            $ led.biscuit = "one"
            "The biscuit's very good. Of course it is."
        "Take two":
            $ led.biscuit = "two"
            "You eat the second biscuit on the way up the gallery. Mo Han waves."
    $ vn_until(19)
    jump led_forms

## RUNG 3, the forms, the door open: she folds him down and works the forms round her with her hands
## over his while he objects to the door. She says the word, once ("Best cauldron I've ever had."),
## and it flips: he plays to the scandal, "They're for this!"
label led_forms:
    $ vn_enter(bg="led_flower_rooms", pc="outraged", pc_tag="led_pc", cast=[("led_bailian", "intent")], cg=None)
    "Evening. Her rooms: black silk screens, a black bed, a long mirror. Bai Lian on the edge of the bed. The door wide open."
    "A whole knot of Blossoms is crowding it, elbowing for a look."
    led_bailian "\"Leave it open. New livery, new duties. The Hall likes to see. Outer robe off. Kneel.\""
    "Before you can shut it. She spreads her knees."
    led_you "\"With the door {i}open{/i}? I'd like it noted that the livery chit said nothing about—\""
    hide led_bailian
    show cg led_forms_kneel onlayer cgl
    "She doesn't note it. She pulls your sash, the red silk slides off your shoulders, and her hand on the back of your neck folds you down onto your knees between hers, in the thin inner robe, the blossom-forms pushing it out, high and round and ridiculous. The doorway giggles."
    "She takes out her cock and lays it in the valley between them. Then she takes your hands, flattens them on the outsides of the forms, and presses them together round her with her own hands over yours."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Work it. Show me the forms.\""
    led_you "\"I'm not— Senior Sister, the {i}door{/i}— {i}everyone's{/i}—\""
    show cg led_forms_squeak onlayer cgl
    vn_sfx "{i}Squeak. Squeak. Squeeeak.{/i}"
    "She works them for you. Silk on cock. Stroke up. Down. Somebody in the doorway snorts. You go red to the horns."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Don't laugh. The forms were designed for exactly this.\""
    "Not smiling at all."
    led_you "\"I'm not {i}laughing{/i}, I'm {i}objecting{/i}— they {i}squeak{/i}— this is not in my—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Faster.\""
    "Faster, her hands crushing yours, pumping. {i}Squeak-squeak-squeak.{/i} Her cock slides through the padded valley, the fat head popping up at your chin on every upstroke, leaking, slicking the silk dark. It bumps your lips. You turn your face away. It bumps your lips again, and your tongue comes out on its own, and you moan, and the whole doorway hears it."
    led_you "\"Nnh— {i}no{/i}— that wasn't— that was {i}involuntary{/i}—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Smile, Jiu. The Hall's watching.\""
    "Then she leans down, close, with her hands still pinning yours round her and the whole doorway straining to hear, and says it. Low. Right into your ear. Out loud."
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"Best cauldron I've ever had.\"{/b}"
    "You gasp. Out loud. The word goes straight down your spine, and your cock throbs in the jade so hard you nearly come from that alone. The {i}scandal{/i} of it. With the door open. The word nobody says." with vnfx("shake")
    led_you "\"You {i}said{/i} it—!\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Once. Don't tell Gu.\""
    show led_pc wanting
    "And something in you turns right over."
    show cg led_forms_flip onlayer cgl
    "You stop pulling against her hands. You squeeze. Your own hands, all on their own, the forms crushed tight round her cock. You turn your face to the doorway, flushed and dripping, and beam."
    led_you "\"Mmh— Senior Sister, look at them, look at my tits— my {i}forms{/i}—\""
    "She lets go of your hands. You don't let go of the forms."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Tell them what the forms are for.\""
    led_you "{b}\"They're for {i}this!{/i}\"{/b}"
    "You announce it to the corridor, squeezing them tight round her cock, and the whole doorway shrieks with laughter, and her hips buck up into the silk so hard the fat head smacks your chin. You lick it. You moan around it. You squeeze harder."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Good. Again. Louder.\""
    "She grunts it."
    led_you "\"{i}They're for this!{/i}\""
    "The corridor roars. Somebody's shrieking with laughter. A Blossom at the back shouts \"{i}Squeeze harder!{/i}\" and you do, and the silk squeals like a door, and Bai Lian has to bite her own lip to keep a straight face."
    "Her hand twists in your tails. Her hips jerk."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Hold them tight—\""
    show cg led_forms_cum onlayer cgl
    "She comes across the forms and up your chin and into your open mouth, hot and thick, over and over, painting the pink silk white." with vnfx("flash", "shake")
    "Applause from the corridor. Real applause. Somebody whistles. \"{i}Worthy of the Hall!{/i}\""
    hide cg onlayer cgl
    "Later, door shut, you're sprawled on her chest with the forms still on and still sticky, and her hand resting on your ass like it lives there."
    led_you "\"I'm telling {i}everyone{/i} you said it.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Then I'll say you made it up.\""
    led_you "\"I didn't make up what happened {i}after{/i}.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"No. That was all yours.\""
    "Her thumb moves on your ass."
    call vn_night(6)
    jump led_strike

## ---- RUNG 4, the first offering (Ledger Summons Offering, Oil): the clause over his own
## signature, his objection in the margin, "Breathe out" the only thing left; the mandatory scene
## flips at the break, and he logs the date himself after it. The register amended: she.

label led_summons_offering:
    $ vn_until(19)
    $ led.tier = 4
    $ vn_enter(bg="led_hall", pc="haggling", pc_tag="led_pc", cast=[("led_xueer", "delighted")], cg=None)
    "Xue'er doesn't trot this time. She walks, slowly, with the face of someone carrying a cake."
    led_xueer "\"Registry. Appointment seven. {i}Appointment seven{/i}, Jiu.\""
    "She can't hold it. She grins so wide it nearly splits her face."
    led_you "\"What's appointment seven?\""
    led_xueer "\"Go and {i}find out!{/i}\"\n{size=-5}{color=#ff8fa3}▸ Go to the registry{/color}{/size}"
    $ vn_pass(5)
    jump led_oil

label led_oil:
    $ vn_enter(bg="led_registry", pc="haggling", pc_tag="led_pc", cast=[("led_gu", "writing")], cg="led_oil_mat")
    "The registry, after hours. Scrolls rolled up. A mat on the floor in front of the registry mirrors. Gu at her desk with the formulary open. Bai Lian beside the mat with a little stoppered bottle."
    led_gu "\"Provision Jiu. Appointment seven. First offering. Attending: Elder Gu, First Flower Bai. Entered.\""
    vn_sfx "{i}Thunk.{/i}"
    "The seal."
    led_you "\"Entered {i}what{/i}? Nobody's told me what an offering—\""
    hide led_gu
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Robe off. Knees and elbows. On the mat.\""
    led_you "\"I'd like to see the clause first.\""
    show screen led_slip("THE INTAKE REGISTER", ["{i}The vessel shall make offering at the First Flower's pace.{/i}", "Signed, at intake, a little smudged."])
    "Gu turns the registry round, helpfully, and taps a line. Your own signature sits under it, from the intake, still a little smudged."
    hide screen led_slip
    led_you "\"That says {i}pace{/i}. It doesn't say {i}what{/i}—\""
    hide led_gu
    $ led.fit = "nude"
    show cg led_oil_mat onlayer cgl
    "Bai Lian doesn't argue. She undoes your sash and the robe drops, and her hand between your shoulder blades folds you down onto the mat: her knee nudging yours wide, elbows down, ass up, the forms swinging under your chest, the jade dangling between your thighs. In the mirrors you look like an offering. You try to get up. Her hand stays where it is, and so do you."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"{i}Vessel present. Vessel objects. Vessel had no choice; see intake, signed.{/i} There's no column for it, so it's in the margin.\""
    "Gu writes, and reads it back in her tonic-dose voice. Kindly."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"The oil is warmed in the palm. Not poured.\""
    "She turns back to the formulary. Bai Lian warms it in her palm."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"It is applied to the rim with the flat of two fingers, in circles, until the vessel breathes out.\""
    show cg led_oil_fingers onlayer cgl
    "Two fingers. Slick. Circling your hole, slow, slow."
    show led_pc outraged
    led_you "\"Hey— {i}hey{/i}— that's not a {i}vessel{/i}, that's my {i}ass{/i}—\""
    "You clench. She circles. You clench. She circles, patient as a kiln, until you have to breathe, and you breathe out so hard it comes out a moan."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Then one finger. Wait for the breath.\""
    led_you "\"{i}Ohhh{/i}— no— get it— {i}ohh{/i}—\""
    "In. Your whole body clenches round her finger, then lets go, and you hate that it lets go."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Then a second. Wait. Then a third, and turn.\""
    led_you "\"F-fuck— stop— Senior Sister, I'm {i}objecting{/i}— {i}ahh{/i}—\""
    "She turns them. You see stars. The jade drips on the mat." with vnfx("shake")
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Is the vessel receptive?\""
    "Brush poised."
    led_you "\"{i}No{/i}—\""
    "Bai Lian crooks her fingers inside you. You howl."
    "In the jade your cock stays soft. It doesn't even try. It just hangs there dribbling a clear string onto the mat while your ass does every bit of the work, and you try to rut against nothing out of habit."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Not that. That's not where the yang goes any more.\""
    "She doesn't look at it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Receptive.\""
    led_you "\"I said {i}no{/i}— write {i}no{/i}— {i}ahh{/i}—\""
    "You moan it into the mat, and your hips rock back onto her hand, chasing it, and every mirror in the registry sees them do it."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"{i}Very{/i} receptive. Objection in the margin.\""
    "Gu writes, and reads it back, with a small satisfied nod. She turns a page."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Then the First Flower attends to the offering in person. At her own pace.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Slow.\""
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Slow.\""
    "Gu writes it down."
    show cg led_oil_length onlayer cgl
    "Bai Lian kneels up behind you. In the registry mirrors you watch her take her cock in her fist and lay it along the crack of your ass, the whole heavy length of it, so you can see exactly how much of it there is."
    led_you "\"Oh {i}god{/i}. Oh god, no, that's not— that is {i}not{/i} going in me—\""
    "To the mirrors."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Note that the vessel is objecting.\""
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Noted. The margin's getting full.\""
    "Writing. Then the fat head of it presses against your oiled hole, hot and heavy and huge, and rests there, nudging. You twist, and it follows. She gathers both your wrists into one hand and pins them to the small of your back."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Breathe out.\""
    "There's nothing else left to do.\n{size=-5}{color=#ff8fa3}▸ Breathe out{/color}{/size}"
    jump led_offering_sex

## Rung 4's recap, after the flip: she comes deep; he came untouched; he logs the date himself, in his
## own voice. Gu strikes Intake and writes Blossom. She. Just like that. "Junior sister."
label led_offering_after:
    $ vn_enter(bg="led_registry", pc="wanting", pc_tag="led_pc", cast=[], cg=None)
    hide cg onlayer cgl  # ff 3:46 am: no picture, offering-cum failed 4 draws (SCENES.md ledger v7)
    "She comes deep, buried to the root, hands on your hips holding you on her, and the heat pumps into you and keeps going until you feel {i}full{/i}. In the mirrors your mouth hangs open and your eyes have gone somewhere else entirely." with vnfx("flash", "shake")
    "You came untouched. Your cock never got a look in. It just leaked through the jade and twitched while your ass did all the work, and somewhere in the middle of it the objecting stopped and the begging started."
    led_you "\"Look at it. It didn't even get {i}hard{/i}. It doesn't {i}matter{/i}.\""
    "You gasp it at the mirrors, giddy."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"It never did.\""
    "She doesn't look at it."
    hide cg onlayer cgl
    show cg led_log_it onlayer cgl
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Now. For the record. In your own voice.\""
    "Turning the registry round and holding out the brush."
    "You take the brush in a hand that won't stop shaking. Oil on your thighs. Her come running down the backs of them. You look at the margin, full of your objections in Gu's neat hand. You don't strike any of them. You write underneath."
    led_you "{b}\"First offering. Appointment seven. Entered by the vessel. Received. Very— {i}very{/i} received. Twice.\"{/b}"
    "Out loud, writing it. You read today's date off Gu's calendar, all of it, very loudly."
    show led_xueer delighted at vn_cast_slot
    led_xueer "\"{i}Official!{/i} Ass and all!\""
    "The door bangs open. Xue'er, who has obviously been listening the whole time."
    "Gu wets her brush and draws a neat line through one word in the register's column. {i}Intake.{/i} Above it, in her careful hand: {i}Blossom{/i}."
    hide led_xueer
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Register amended. The Hall goes by the register. She'll want a bath.\""
    "She glances up at Xue'er."
    $ led.she = True
    "She. Just like that. Nobody blinks."
    hide led_bailian
    hide led_gu
    show led_xueer wicked at vn_cast_slot
    led_xueer "\"She'll want two baths. And a cushion.\""
    "Eyeing the come running down your thighs."
    hide led_xueer
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Noted.\""
    "And she actually writes {i}cushion{/i}."
    hide led_xueer
    "You try to stand and your legs won't. Your ass throbs, open and full and dripping, and every time you clench, more of her slides out of you and down the backs of your thighs, and you moan every single time, and Xue'er giggles every single time."
    "Bai Lian helps you up off the mat, her come still sliding out of you, and tucks a red tail back behind your horn."
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"Junior sister.\"{/b}"
    $ led.fit = "red"
    hide cg onlayer cgl
    call vn_night(6)
    jump led_strike

## ---- RUNG 5, asking for it (Ledger Summons Terrace, Overheard, the cooling-off, Knock): the one
## honest line; the bylaw notice; one night of climbing the walls; the knock at dawn, unsummoned.

label led_summons_terrace:
    $ vn_until(19)
    $ led.tier = 5
    $ vn_enter(bg="led_hall", pc="wanting", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
    led_xueer "\"Petitions on the Terrace. You're in the line. Stand up straight. You've got a lot to stand up straight with now.\"\n{size=-5}{color=#ff8fa3}▸ Up to the Terrace{/color}{/size}"
    "Second Bell. Xue'er, slip in hand."
    $ vn_pass(30)
    jump led_overheard

label led_overheard:
    $ vn_enter(bg="led_terrace", pc="wanting", pc_tag="led_pc", cast=[], cg=None)
    "Petitions. A dispute between two Elders, settled by a transfer Gu enters as \"provisions\". Mo Han finds all of it very funny."
    hide cg onlayer cgl  # ff 3:47 am: no picture, overheard failed 4 draws (SCENES.md ledger v8)
    "Afterwards the Hall files off. You hang back to fix a cord that's slipped. Up by the black throne, not for the register, Mo Han and Bai Lian."
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Have you someone near oath?\""
    "Mildly, the way you'd ask about rain."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Not yet.\""
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Mm. No hurry. There's never any hurry.\""
    "He pats her arm, and goes off whistling. She sees you. She doesn't pretend she didn't."
    hide cg onlayer cgl
    show led_bailian soft at vn_cast_slot
    "In the colonnade you catch her sleeve."
    led_you "\"Near oath?\""
    "She looks at you for a long moment. Then she gives you one honest line, which is one more than anybody in this building gives anybody."
    led_bailian "{b}\"I've been going slow with you since the corridor. On purpose. It's the only thing in here I get to choose.\"{/b}"
    hide led_bailian
    "Then she's gone."
    show screen led_slip("PER BYLAW", ["{i}An account at its last entry is cooled. No summons to the vessel until the quarter-moon, so that nobody can say the Hall hurried the last payment.{/i}"])
    "When you come down the gallery there's a new notice on the registry board, in Gu's hand, still wet."
    hide screen led_slip
    "You read it twice. No summons. No hand on the small of your back in the corridor. No \"Clothes off\", no \"Breathe out\", no receipt. For the first time since the stair, nobody in the building is going to take anything from you."
    "Your hips roll against the board. You didn't tell them to."
    show led_xueer delighted at vn_cast_slot
    led_xueer "\"Oh, {i}no{/i}. Oh, you poor thing. The quarter-moon.\""
    "Reading it over your shoulder, delighted."
    led_you "\"How long is that?\""
    led_xueer "\"Long enough. The pool's on how long before you go and knock, and I'm moving it.\""
    "She's already doing sums."
    hide led_xueer
    $ led.climbs = 0
    jump led_cooling

## The cooling-off: one night (the owner, 2026-10-19). The two authored climbs, in order, then the
## shorter lines; the bylaw says nothing at all about knocking.
label led_cooling:
    $ vn_enter(bg="led_hall", pc="wanting", pc_tag="led_pc", cast=[], cg=None)
    "Cooling-off. Nobody sends for you. Nobody's allowed to. Your hips won't sit still and the jade won't let anything happen."
    menu:
        "The notice on the registry board hasn't moved."
        "Climb the walls":
            $ led.climbs = (led.climbs or 0) + 1
            if led.climbs == 1:
                $ vn_enter(bg="led_cell", pc="flushed", pc_tag="led_pc", cast=[], cg="led_climb_mat")
                "Your cell. The lamp out. The forms still laced on, because you couldn't face taking them off."
                show cg led_climb_mat onlayer cgl
                "You lie face-down on the mat and rock. Just a little. The jade presses into the bedding. Your cock tries to fill it and can't, and the trying is the whole feeling."
                vn_sfx "{i}Creak. Creak. Creak.{/i}"
                led_you "\"Nnh— {i}nnh{/i}—\""
                "Your hips find a rhythm on their own. Ass up, face down, grinding the mat like it owes you money. The seat pad's gone, and your real ass rolls with every push, and that's worse. That's so much worse."
                led_you "\"Senior Sister— Bai Lian— {i}please{/i}— I'll be so good, I'll be so {i}loud{/i}—\""
                "You bite the pillow. It doesn't help. You are loud. The wall knocks twice from the next cell. You moan back at it."
                "It goes on for an hour. It goes nowhere. At the end of it you're shaking, soaked in sweat, and the jade is dripping onto the mat in a slow clear string, and you haven't come, and you're not going to, and you've never been so happy to be this miserable."
            elif led.climbs == 2:
                $ vn_enter(bg="led_gallery", pc="flushed", pc_tag="led_pc", cast=[], cg="led_climb_door")
                "You don't even try to sleep. You go and sit outside her door."
                show cg led_climb_door onlayer cgl
                "Her lamp's lit. You can hear her turn pages. You can hear her stop turning pages, which is worse."
                "You put your back to her door and your hand down the front of your livery, onto the jade, and press. {i}Mmh.{/i} Rub. {i}Mmmh.{/i} Nothing happens. You do it anyway, out loud, on purpose, with your head tipped back against the wood."
                led_you "\"I know you can hear me. {i}Ahh{/i}— I know you— can hear— {i}this{/i}—\""
                "You tell the door. Through the wood, very quietly, her chair creaks."
                "By the time Xue'er comes up the gallery with a lamp to fetch you, you're curled on the floor outside the First Flower's door in a puddle of your own leaking, making little noises. She looks down at you for a long time."
                show led_xueer wicked at vn_cast_slot
                led_xueer "\"That's moved the pool. That's moved the whole pool.\""
                "Awed."
            else:
                $ _led_t = LED_COOLING[(led.climbs - 3) % len(LED_COOLING)]
                "[_led_t]"
            "{color=#b7b7b7}The notice on the registry board hasn't moved. {i}No summons until the quarter-moon.{/i} The bylaw says nothing at all about knocking.{/color}"
            $ vn_pass(30)
            jump led_cooling
        "Wait for dawn":
            pass
    "One night of bylaw is all you can stand. Nobody's sent for you. Nobody's going to. That's the point."
    call vn_night(5)
    jump led_knock

## RUNG 5, the knock: the payoff. She stops; nobody takes anything; he asks. "If you want it, you have
## to say it." "I want it. Please. Fuck me." Consensual.
label led_knock:
    $ vn_enter(bg="led_gallery", pc="wanting", pc_tag="led_pc", cast=[], cg="led_knock_door")
    "You don't wait for a summons. That's the point. Nobody's going to take it this time. If you want it, it's yours to go and ask for."
    show cg led_knock_door onlayer cgl
    "Up the gallery before the bell, livery on, forms on, tails tied, your tail lashing. Her door. You knock."
    "It opens before your hand's down. Bai Lian: hair loose, robe open, eyes shadowed, like she's been awake exactly as long as you have."
    "She doesn't step aside. She doesn't reach for you. Her hands stay at her sides."
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"If you want it, you have to say it.\"{/b}"
    led_you "{b}\"I want it. Please. Fuck me.\"{/b}"
    "No breath between."
    "Something goes out of her shoulders. She steps aside."
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_knock_bed")
    $ led.fit = "nude"
    "Her rooms. She undoes your sash with two fingers and the red silk drops. The forms underneath are laced tight over something that's started pushing back. She pulls the cords and they drop too."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Face-down.\""
    show cg led_knock_bed onlayer cgl
    "You're face-down on her bed before the word's finished, ass up, knees wide, cheek in her sheets. Your tail whips side to side. You can't make it stop."
    "She takes her time looking. Your ass, rounder than the stair ever saw it. Your thighs, pressed together, slick already with a whole night of leaking through the jade. The jade itself, hanging there, dripping onto her sheets, the tiny soft thing inside it not even trying to stand."
    "Her look slides right past it. It always does."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"All night. You did this all night.\""
    led_you "\"I'd have done it for {i}weeks{/i}—\""
    "You moan it into the bedding, and push your ass back at her."
    "She spits. Hot, between your cheeks. Her thumb works it in. No oil. No formulary. No Gu. No margin."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Say it again.\""
    led_you "\"I want it. {i}Please{/i}, Bai Lian, I want it, fuck me, I've been grinding my bed all night—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Louder. Let them hear what you need.\""
    "And she lines up.\n{size=-5}{color=#ff8fa3}▸ Louder{/color}{/size}"
    jump led_knock_sex

label led_knock_after:
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_knock_cum")
    show cg led_knock_cum onlayer cgl
    "She fucks you straight through it and lets go, hot and endless, groaning your name into your back. She doesn't let go of you. She keeps rocking against you, slow, through the aftershocks, and every rock squeezes another wail out of you." with vnfx("flash")
    "You came untouched, screaming into her sheets, loud enough for the whole gallery. Somewhere down it a door bangs open and Xue'er shrieks, \"{i}PAY UP!{/i}\""
    led_you "\"It doesn't even— {i}hah{/i}— it doesn't even get hard. I came from my {i}ass{/i}. It's just— {i}there{/i}.\""
    "You moan it into the sheets, delighted."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Mm. Ornamental.\""
    "She doesn't let you up. She hauls you into her lap, her come running down your thighs, and holds you there with her hand spread on your hip."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"You asked.\""
    "Into your hair, like she's checking."
    led_you "\"I asked.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Nobody's ever asked.\""
    hide cg onlayer cgl  # ff 3:47 am: no picture, knock-clean failed 4 draws (SCENES.md ledger v8)
    "Then she rolls you onto your back, kneels over your face, and lets her softening cock rest on your lips, wet with both of you."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Show me.\""
    "You show her. Eager, sloppy, lapping her clean from root to tip with your eyes on hers the whole time, moaning about the taste, sucking the last of it off the head while she shivers. Your tail's wrapped round her ankle. You didn't tell it to."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Again later.\""
    "Hoarse."
    led_you "\"Again {i}now{/i}.\"\n{size=-5}{color=#ff8fa3}▸ Stay in her bed till the next bell{/color}{/size}"
    $ led.fit = "red"
    hide cg onlayer cgl
    call vn_night(6)
    jump led_strike

## ---- RUNG 6, unlaced and sworn (Ledger Unlaced, Her Story, Oath, Oath Sworn, Rooms) ---------

## The dawn lacing: the forms won't sit over the real chest; Xue'er yells for the whole dressing room;
## Bai Lian cuts the last two cords ("No. My hands."); the titjob on the real chest. Consensual.
label led_unlaced:
    $ vn_enter(bg="led_dressing", pc="wanting", pc_tag="led_pc", cast=[("led_xueer", "wicked")], cg=None)
    $ led.tier = 6
    "Dawn. The dressing room. Xue'er with the forms over her arm."
    led_xueer "\"Arms up.\""
    "You put them up. She presses the first blossom-form to your chest."
    "It won't sit."
    "She pushes. It slides off sideways. She tries the other one and it sits up crooked like a lid on a pot that's too full."
    $ led_body("6d")
    "{color=#ff5fb8}Under it, where the forms always sat on nothing, there's something. Two somethings. Soft and heavy and real, swelling up into her hands.{/color}"
    "Xue'er puts the forms down. Very slowly."
    led_xueer "\"It's real. {i}IT'S REAL! DRESSING ROOM! EVERYBODY! NOW!{/i}\"" with vnfx("shake")
    "She whispers it, then yells it at a volume that rattles the mirrors."
    hide led_xueer
    show cg led_dressing_crowd onlayer cgl
    "Doors. Feet. Every Blossom on the gallery crams into the room and stares at your chest. One reaches out; another slaps her hand away. \"Juniors don't touch!\""
    "\"Is it the tonic?\" \"It's the posture drills,\" somebody says, and the whole room shrieks."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Blossom-forms, both: no longer required.\""
    "Gu pushes through, ledger first. Looks. Writes."
    show cg led_scissors onlayer cgl
    "And Bai Lian in the doorway, with a pair of lacquered scissors. The room parts for her."
    "You reach for the last two cords, still trailing at your sides. She catches your wrist."
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"No. My hands.\"{/b}"
    vn_sfx "{i}Snip.{/i} {i}Snip.{/i}"
    $ led.cut = True
    $ led.fit = "nude"
    show cg led_unlaced onlayer cgl
    "{color=#ff5fb8}The last two cords fall. The forms drop into her palm. And there you are in the long mirror, bare to the waist: red tails, little horns, a tail curled round your thigh, and real breasts. Round. Full. Pink-tipped. A DD-cup, heavy and honest, that nobody laced on. Yours.{/color}"
    "{color=#ff5fb8}You grab them with both hands. They spill between your fingers, warm, and bounce when you let go, so you grab them again. And they're so {i}sensitive{/i}. Your own palms on them make you squeal. The air on your nipples makes you squeal.{/color}"
    led_you "{color=#ff5fb8}\"{i}Ahh{/i}— they feel {i}everything{/i}— Xue'er, they feel {i}everything{/i}— look at them— {i}look{/i} at them— Gu, write this {i}down{/i}—\"{/color}"
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Out.\""
    "To the room. They go. Not far. Mostly as far as the door."
    hide cg onlayer cgl  # ff 2:01 am: no picture, unlaced-tits failed 5 draws (SCENES.md ledger v5)
    "She sits you on the dressing table in front of the mirror, kneels up, and lays her cock between your new breasts."
    "The jade sits forgotten in your lap, the nub inside it soft as a petal, leaking on the lacquer. Nobody so much as glances at it. Least of all you."
    led_you "\"Is this— is this {i}real{/i}?\""
    "You can't stop laughing."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Feel.\""
    "And she squeezes them round her. Soft. Warm. Skin on cock, not silk. No squeak. Just the wet slide of her through your cleavage, the fat head nudging your chin, your nipples dragging across her palms."
    "You take over before she asks: the exact squeeze, the exact roll. The forms trained that into you. Your tits just know it now."
    led_you "\"{i}Ahh{/i}— oh, fuck, I can {i}feel{/i} it— they're mine, they're {i}mine{/i}— look at them— look at {i}me{/i}—\""
    "Laughing and moaning at once, high and giddy."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Look at you.\""
    vn_sfx "{i}Shlk. Shlk. Shlk.{/i}"
    "And she fucks your tits faster. Your breasts bounce on every stroke. She pinches a nipple and you shriek the mirror foggy."
    show cg led_unlaced_cum onlayer cgl
    "She comes up your chest in long hot ropes, over your breasts, into the hollow of your throat, dripping off your nipples. You rub it in with both hands, laughing, moaning, wrecked." with vnfx("flash")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"No forms. Not ever again.\""
    menu:
        "\"No forms. Not ever again.\""
        "Squeeze them round her again":
            jump led_unlaced_sex
        "Into the Hall":
            $ led.fit = "red"
            $ vn_pass(60)
            $ led.next = "led_her_story"
            jump led_hall

label led_unlaced_after:
    $ vn_enter(bg="led_dressing", pc="wanting", pc_tag="led_pc", cast=[], cg="led_unlaced_cum")
    show cg led_unlaced_cum onlayer cgl
    "Second time, all over your new breasts and up your neck. You laugh with your mouth open and catch some." with vnfx("flash")
    "Out in the corridor, the Blossoms are still arguing about whether that counts as public.\n{size=-5}{color=#ff8fa3}▸ Into the Hall{/color}{/size}"
    $ led.fit = "red"
    $ vn_pass(60)
    $ led.next = "led_her_story"
    jump led_hall

## Her story, at the mirror, once: nine years in the chair; the oath only takes if it's asked for
## wanting; "So I stopped. To see if you'd come and ask."
label led_her_story:
    $ vn_until(21)
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_her_story")
    show cg led_her_story onlayer cgl
    "Her rooms. The lamp. The long mirror. She stands behind you in it with her hands on your waist and, for once, doesn't do anything with them."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"You want the story.\""
    "It isn't a question."
    led_you "\"Once. Not the Hall's version.\""
    "She's quiet so long you think she won't."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"I sat at twenty-two. Nine years ago. I was good, and I was quick, and the First Flower before me trained me fast, the way they always have. Then she swore me in, walked out of the East Gate, and never wrote.\""
    "Her thumbs move on your hips."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"The chair has enormous reach and no power at all. I can't leave it. The only way out is a successor who asks for it out loud, on the Terrace, owing nothing. The oath only takes if it's asked for wanting. Not needing. Not owing. Wanting.\""
    led_you "\"So everyone trains them fast. So they want it.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Everyone before me did. I didn't want to. So I went slow, with all of them, and nobody ever asked.\""
    "She meets your eyes in the glass. A small dry breath."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Then a swordsman came up the stair doing sums, and haggled the terms the whole time I took him. Every rung. Out loud. So I stopped. To see if you'd come and ask.\""
    "Her thumbs stop. You laugh. She almost does."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"I'm not asking you. I'm not allowed to. Mo Han's not allowed to. Nobody in this building is allowed to want it out loud in front of you.\""
    led_you "\"I know.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Your page is clear. You owe nothing. You could walk down the stair in the morning. I wanted you to know what you'd be walking down from.\""
    "Her hands slide up and cup your breasts, warm, holding them like they're the only thing she's sure of."
    "You lean back into her. Her cock's hard against your ass through the silk. She doesn't do a thing about it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Stay. Tonight.\"\n{size=-5}{color=#ff8fa3}▸ Sleep in her arms{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(5)
    jump led_oath

## THE OATH, at dawn on the Audience Terrace: nothing owed, the stair open; you ask, in your own voice,
## and choose which reason comes first; it always ends "I want all of it." The surge, the wings, the
## page burning blue. Bai Lian walks to the East Gate, turns round, and stands on your left.
label led_oath:
    $ vn_enter(bg="led_terrace", pc="wanting", pc_tag="led_pc", cast=[("led_mohan", "beaming")], cg="led_oath_rows")
    show cg led_oath_rows onlayer cgl
    "Dawn on the Audience Terrace. Bronze sky. Black stone. The whole Hall in rows, Blossoms in red at the front, Gu at a plinth with the Ledger open on it."
    "Mo Han on the black throne, beaming, legs crossed."
    hide led_mohan
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Blossom Hall, present.\""
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Lovely. Jiu. Your account is settled. Nothing owed. The Hall has nothing further to ask of you. You may walk down the stair this afternoon, and I'll see you to the gate myself. With a biscuit.\""
    "He turns to you, and lets that be true for a whole breath, because it is."
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Separately, and I'd like the separateness on the record, Gu—\""
    hide led_mohan
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Noted.\""
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"—the First Flower's chair falls vacant when a successor asks for it. Out loud. Here. Owing nothing. An oath that only takes if it's wanted. She can't propose you. I can't propose you. There is no form of words by which anybody in this Hall may want this out loud in front of you.\""
    "He spreads his hands, delighted with the architecture."
    "The Terrace waits."
    "Bai Lian stands where a First Flower stands. She hasn't looked at you once since you came up the steps."
    "So you ask. In your own voice. Out loud."
    led_you "{b}\"I'm asking. For the chair.\"{/b}"
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Why?\""
    "Very carefully, he looks mildly surprised."
    menu:
        "\"Why?\""
        "Your cousins first":
            $ led.reason = "cousins"
            led_you "\"Because my cousins sit their trials next spring under a clean name, and I did that. Me. With my mouth and my ass and my tits. And because the next one up the stair has a page too.\""
            "Laughter in the rows. Then you look at her."
            led_you "\"And because of her. She went slow with me from the first day, on purpose, and it cost her the door.\""
            "Bai Lian's jaw tightens. She still doesn't look at you. Her hand, at her side, closes on nothing."
        "Her first":
            $ led.reason = "her"
            led_you "\"Because of her.\""
            "Bai Lian's head comes up."
            led_you "\"Because she went slow with me from the first day, on purpose, and it cost her the door. Somebody should get to walk out of that gate owing nothing. And my cousins sit their trials under a clean name, and I did that. Me. On my knees, mostly.\""
            "You grin at the rows. Laughter. Even Gu's mouth twitches."
        "Wanting all of it, first":
            $ led.reason = "want"
            led_you "\"Because I want it. The chair, the livery, the horns, the whole Hall saying First Flower when I walk past. I came up the stair to sell, and I have never been so happy to be bought.\""
            "You grin. Laughter in the rows. Softer:"
            led_you "\"And my cousins' names are clean. And her. Mostly her. She went slow with me from the first day, on purpose, and it cost her the door.\""
            "You look at her, and this time she looks back, and it's the first time on the Terrace she has."
    led_you "{b}\"I want all of it.\"{/b}"
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"Hear that? Hear the {i}wanting?{/i}\""
    "Delighted, to the whole Terrace. He produces the oath-form from his sleeve as if it's been there all along. It has. Gu hands you a little silver knife."
    show screen led_slip("THE OATH-FORM", ["I was %s %s. I ask for the chair, wanting it, owing nothing. I give my name for the office." % (led_surname, led_pc_name)])
    "You nick your thumb and press it to the glyph, and say it."
    hide screen led_slip
    "The air goes heavy. Cold silk, all over you. Then hot."
    "Then it hits."
    hide cg onlayer cgl
    show cg led_surge onlayer cgl
    $ led_body("6")
    "{color=#ff5fb8}Your breasts surge. Up and out, swelling under the red silk, fuller, heavier, past the DD, into heavy H-cups nobody has a form for, until they spill over the neckline and sit high and round and enormous on your chest.{/color}" with vnfx("shake")
    led_you "{color=#ff5fb8}\"{i}Ahh{/i}—! {i}Ahh{/i}— they won't— they won't {i}stop{/i}—\"{/color}"
    "{color=#ff5fb8}You grab them and they overflow your hands. Your hips flare, grinding wider. Your waist pulls in tight between them. Your ass rounds out behind you, heavy, straining the skirt. Your thighs plump until they press together and rub. Your red tails pour down past your hips. The livery creaks at every seam.{/color}"
    "{color=#ff5fb8}In the jade, your cock doesn't get a single drop of it. Everything rushes everywhere else and leaves it behind: soft, tiny, not even twitching, your balls drawn up tight. It's still there. Caged. Kept. A tiny pink nub in green stone, and the most useless thing on the Terrace.{/color}"
    led_you "\"Look. It doesn't even {i}care{/i}.\""
    "You gasp it, and laugh."
    "{color=#ff5fb8}Everything else does. The red silk on your nipples is a mouth. The skirt on your ass is a hand. Your own breath across your lips makes you moan in front of the whole Hall.{/color}"
    led_you "\"{i}Hhh{/i}— everything's— {i}on{/i}—\""
    "Every drill you ever ran lands in your body at once. Your mouth, your hands, your hips, your ass: they know all of it now, the whole Hall's refinement, poured in and sealed. {i}Breathe out. Slow. Open. Again.{/i}"
    show cg led_wings onlayer cgl
    "{color=#ff5fb8}Then your back blazes, hot and sweet, and something unfolds out of it. Wings: black, leathery, spreading wide over the Terrace with a {i}snap{/i} that blows out the nearest lamp.{/color}" with vnfx("flash", "shake")
    "The Terrace gasps. You moan out loud in front of every one of them, because it feels like coming, because it nearly is."
    led_you "\"{i}Ahh{/i}— {i}ahhh{/i}— oh, fuck, oh, {i}everyone's looking{/i}— look at me— look at what you {i}made{/i}—\""
    "Your knees buckle. Your tits heave. The jade drips, soft and useless, in front of the whole Nine Sorrows."
    "In the front row, Xue'er has both hands over her mouth. Gu is writing very fast."
    show cg led_page_burns onlayer cgl
    $ led.burned = True
    "Gu sets a flint to the Ledger. The page catches blue. Spirit fire runs down every line, every name, every entry, struck and unstruck, and the [led_surname] page curls into ash."
    hide led_mohan
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Debt discharged.\""
    "Then she looks at your wings, visibly annoyed."
    hide led_mohan
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Those were not ordered.\""
    "She starts writing an addendum."
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"First Flower.\""
    "Mo Han claps once, and says it to you. And to Bai Lian:"
    hide led_gu
    show led_mohan beaming at vn_cast_slot
    led_mohan "\"You're free, Hall Master. The world's as wide as your appetite.\""
    show cg led_east_gate onlayer cgl
    "Bai Lian walks to the edge of the Terrace, where the East Gate opens on the moor. A few steps past the threshold. Owing nothing. Free."
    "She stops. She turns round. She walks back and stands on your left."
    hide led_mohan
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"I said I'd get you all five. I never said I'd leave.\"{/b}\n{size=-5}{color=#ff8fa3}▸ The First Flower's rooms{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(30)
    jump led_rooms

label led_rooms:
    $ led.fit = "nude"
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg=None)
    "The First Flower's rooms. Yours. Somebody's turned the black bed down."
    "Bai Lian shuts the door and leans on it and looks at you: red tails, horns, wings, tail, breasts spilling out of the livery, the jade."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Face to face. I've never once let you look at me while I did it.\""
    led_you "\"Then let me.\""
    hide cg onlayer cgl  # ff 2:15 am: no picture, rooms failed 4 draws (SCENES.md ledger v6)
    "She kisses you. First time with nothing in the way: no forms, no register, no door left open. Her mouth on yours, slow, then her mouth on your throat, then on your new breasts, sucking one nipple until you're arching into her and shoving the other into her face."
    led_you "\"Bai Lian— {i}ahh{/i}— Bai Lian, please, I want it, I want you, I've wanted you looking at me since the {i}mirrors{/i}—\""
    "You lie back on the bed and spread your legs, wings out across the sheets, and she climbs over you. Her weight. Her heat. Her cock lying hot along your stomach, up past your navel. The jade nestles under it, small as a pearl. Hers is hard and heavy and everything. Yours doesn't stir under it. It never does now, and you grin up at her about it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Look at me.\""
    "You look.\n{size=-5}{color=#ff8fa3}▸ Pull her in{/color}{/size}"
    jump led_rooms_sex

label led_rooms_after:
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_rooms_cum")
    show cg led_rooms_cum onlayer cgl
    "She comes face to face, forehead on yours, eyes open, and says your name. Not the office. Not the list. Yours." with vnfx("flash")
    "You come with her, untouched, wings beating the sheets, screaming her name at the ceiling."
    "A knock. Pleasant. Professional."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"First Flower, a moment, the intake—\""
    "Gu, at the door, with the register. Bai Lian gets up, naked, walks to the door, and shuts it in Gu's face."
    show led_bailian dry at vn_cast_slot
    led_bailian "{b}\"Not this one.\"{/b}"
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Tomorrow, then. Noted.\""
    "Through the door, entirely unoffended."
    "She comes back to bed and pulls the sheet and both your wings over the two of you."
    "You lie there with her come leaking out of you and her hand spread on your belly, and for a while neither of you says anything."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"First Flower.\""
    "Eventually, testing it."
    led_you "\"Don't. Not in bed.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"First Flower.\""
    "Again, wickedly, into your ear, and you squirm, and she rolls on top of you, and the sheet goes on the floor."
    hide cg onlayer cgl
    call vn_night(7)
    jump led_first_flower

## ---- THE ENDING ("First Flower") and the epilogue's Stay or Go -----------------------------

## Morning in the First Flower's rooms; Gu with the intake register: "What pace?" "Slowly."
label led_first_flower:
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_ff_morning")
    show cg led_ff_morning onlayer cgl
    "Morning. The First Flower's rooms. Your rooms."
    "Bai Lian's asleep across most of the bed. Your wings are folded over both of you like a blanket nobody ordered."
    "You wake her the way you want to be woken: ass back against her, grinding, until she's hard against you and awake and huffing a laugh into your neck. She slides in from behind, half asleep, slow, slow, slow."
    "The jade bumps the sheet between your thighs, soft and tiny and forgotten. It leaks a little every time she bottoms out. Neither of you has looked at it since the oath."
    led_you "\"{i}Mmh{/i}— good morning—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Shh.\""
    "And she keeps going. Slow."
    "A knock. Pleasant. Professional."
    "Neither of you stops."
    led_you "\"Come in.\""
    "High and breathless. Bai Lian bites your shoulder to keep from laughing."
    hide cg onlayer cgl  # ff 3:47 am: no picture, ff-gu failed 4 draws (SCENES.md ledger v8)
    "Gu opens the door with the intake register under her arm and her brush behind her ear, takes in the bed, the wings, the sheet, and the slow rock of the First Flower's hips, and doesn't blink."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Good morning, First Flower.\""
    "She doesn't even trip on it. She opens the register on the doorframe."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Supply is thin again. First quality, a man of twenty-four from outside Fen. Burnt dantian, very promising, came up the stair yesterday doing sums. What pace?\""
    "She looks up, brush ready."
    "Behind you, Bai Lian stops moving. All the way in. Very still. Waiting, like the whole Hall is waiting."
    led_you "{b}{color=#ff9ad5}\"Slowly.\"{/color}{/b}"
    "And Bai Lian starts moving again. Slowly."
    "Gu writes it down. {i}Slowly.{/i} One word, in her careful hand, in the column where the First Flower writes the pace."
    show led_gu pleasant at vn_cast_slot
    led_gu "\"Noted. Supply problem unresolved, then. I'll complain about it at the next meeting.\""
    "She sounds almost fond. She goes, and shuts the door behind her, and you hear her brush scratch once more in the corridor."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Slowly. Good.\""
    "Into your neck, and she pushes in to the root, and holds it there until you're moaning into the pillow."
    $ led.ending = "laced"
    $ achievement.grant("First Flower")
    menu:
        "\"Slowly. Good.\""
        "Stay in the First Flower's rooms" (ending=True):
            jump led_epilogue_stay
        "Go down the stair with her" (ending=True):
            jump led_epilogue_go

label led_epilogue_stay:
    $ led.epilogue = "stay"
    $ led.fit = "flower"
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cast=[], cg="led_epi_stay")
    show cg led_epi_stay onlayer cgl
    "You stay."
    "The black bed. The long mirror. The registers on the desk, and your hand in all of them now. A lacquered box on the shelf with two cut cords in it, which Xue'er dusts every morning and nobody's allowed to move."
    "Bai Lian owes the Hall nothing. She could walk out of the East Gate any morning she likes. Every morning she rolls over, looks at the door, and doesn't."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"The bylaws are silent on where a former First Flower sleeps. I checked.\""
    led_you "\"You checked.\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Twice. Slowly.\""
    "She pulls you onto her, and smiles, and doesn't mean it at all."
    "She doesn't. She rolls you under her and pins your wings flat to the sheets with her forearms and fucks you deep and hard and not slow at all, the black bed knocking the wall, your tits bouncing, your tail lashing her calf, the jade flopping soft and useless against your belly."
    led_you "\"Doesn't matter— {i}ahh{/i}— it doesn't {i}matter{/i}— not with you in me— {i}ahh{/i}— Bai Lian— they can hear— the whole gallery can {i}hear{/i}—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Good. Louder. You're the First Flower. Set the tone.\""
    "You set the tone. Down the gallery, a whole row of doors opens to listen, and Xue'er, from somewhere, starts a slow clap.\n{size=-5}{color=#ff8fa3}▸ The First Flower's rooms{/color}{/size}"
    jump led_route_return

label led_epilogue_go:
    $ led.epilogue = "go"
    $ led.fit = "flower"
    $ vn_enter(bg="led_stair", pc="wanting", pc_tag="led_pc", cast=[("led_mohan", "beaming")], cg=None)
    "It turns out the bylaws are silent on where the First Flower sleeps."
    "Gu checks. Twice. \"Silent,\" she says, annoyed, and writes an addendum about it."
    "Mo Han sees you both to the top of the stair himself: forty-nine, round, beaming, a biscuit in his sleeve for the road."
    led_mohan "\"No hard feelings anywhere in this. Come up on intake days. The First Flower sets the pace. Don't be late; Gu hates late.\""
    "And he means every word, the way he always does."
    hide led_mohan
    show cg led_epi_stair onlayer cgl
    "You go down the black stair with Bai Lian on your left. Wings folded. Tails swinging. The jade cool under your skirt, tiny and useless and locked, exactly how she likes it."
    "She doesn't look back at the gate. She looks at you, the whole way down."
    show cg led_epi_door onlayer cgl
    "Your new door's a plain one in town. The first night, Bai Lian looks round the little room, at the narrow bed, at the window with no moor in it, and starts to laugh."
    led_you "\"What?\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Nobody's writing this down. Nobody at all.\""
    "She has you against that plain door before you've found the light. Skirt up, wings cramped, her cock sliding home, your cheek on the wood, your own little cock dribbling soft in its jade against the paint. Nothing receipted. Nothing entered. You moan your name into the paint, and hers, and the neighbours bang on the wall, and she laughs into your shoulder and doesn't slow down."
    "{color=#b7b7b7}You come up the stair on intake days. The line is always moving briskly. When the clerk sees who it is she stands up.{/color}\n{size=-5}{color=#ff8fa3}▸ Out to the gate{/color}{/size}"
    jump led_route_return
