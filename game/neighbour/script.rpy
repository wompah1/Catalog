## THE SOURCE: neighbour's passages, rewritten for the VN (2026-11-11; PLAN.md). One label a passage
## of the original (main.twee, rungs.twee), as beats; the director scenes are in scenes.rpy.

## ---- moving day (Neighbour Opening) ---------------------------------------------------------------

label nb_opening:
    $ nb_init()
    $ nb.fit = None
    $ vn_enter(bg="nb_landing", pc="neutral", pc_tag="nb_pc", cast=[], cg="nb_boxes")
    show cg nb_boxes onlayer cgl
    "Third floor. No lift. Last box."
    "You drop it in the doorway of your new flat and wheeze."
    "Behind you, the door across the landing opens."
    hide cg onlayer cgl
    show nb_tessa grin at vn_cast_slot
    nb_tess "\"Need a hand with any of— oh.\""
    show cg nb_reunion onlayer cgl
    "Tall. Leggings, cropped training top, dark hair scraped up. A kettlebell hanging off one hand like a handbag. Hazel eyes, and a dimple on one side only."
    nb_ellis "\"Tessa?\""
    vn_sfx "Thunk."
    "The kettlebell hits the landing."
    nb_tess "\"No {i}way{/i}. [nb_pc_name]? [nb_pc_name] [nb_pc_surname]? Shut {i}up{/i}.\""
    "You were friends as kids. You haven't seen each other in years. That's all of it."
    "She grabs your next two boxes at once and carries them in like they're empty."
    nb_tess "\"I'm twenty-three. Personal trainer, the gym on the high street. People pay me to make them cry.\""
    "Another box."
    nb_tess "\"You?\""
    nb_ellis "\"Twenty-one. The café. Early shifts.\""
    nb_tess "\"Look at your {i}arms{/i}. Little twig arms. I'm having you deadlifting by spring.\""
    nb_ellis "\"You are not.\""
    nb_tess "\"Watch me.\""
    "She dumps the last box on your counter."
    nb_tess "\"I'm right across the landing. If anything breaks, you knock.\""
    nb_ellis "\"Same. If anything breaks.\""
    nb_tess "\"Deal.\""
    hide cg onlayer cgl
    hide nb_tessa
    "Her door shuts. The landing feels a lot smaller than it did this morning.\n{size=-5}{color=#ff8fa3}▸ Unpack till dark{/color}{/size}"
    $ vn_until(22)
    jump nb_knock

## ---- rung 1: on your hands (Neighbour Knock, Knock Hands, Knock Scrub) -----------------------------

label nb_knock:
    $ vn_enter(bg="nb_flat", pc="shy", pc_tag="nb_pc", cast=[], cg="nb_knock_door")
    show cg nb_knock_door onlayer cgl
    "Someone is pounding on your door like the building's on fire."
    vn_sfx "BAM BAM BAM." with vnfx("shake")
    "You get the latch off on the second go. Tessa practically falls in."
    show cg nb_knock_tent onlayer cgl
    "Grey hoodie, grey sweats, face red to the collar. She's not looking at you. She's looking down at the front of her sweats, tented so far the waistband's drum-tight across her stomach."
    "You look too. You can't not."
    nb_tess "\"It won't go down. I woke up with it. I've had it all day. I can't think. I can't walk.\""
    nb_tess "\"Cold shower, everything— and my hands don't—\""
    "She grabs it through the sweats, squeezes, and only whimpers."
    nb_tess "\"See? {i}Nothing{/i}. It just {i}throbs{/i}—\""
    "The smell of her hits you. Heat and salt and something sweet, like warm sugar. You back into the wall."
    nb_ellis "\"Tessa—\""
    nb_tess "\"I can't go to anyone. You're right {i}here{/i}.\""
    "She's shaking."
    nb_tess "\"Please. I know what I'm asking. Just this once.\""
    nb_ellis "\"Okay. Okay. Just this once.\""
    menu:
        "\"Okay,\" comes out of you."
        "Keep your eyes shut":
            $ nb.peek = False
        "Peek":
            $ nb.peek = True
    jump nb_knock_hands

label nb_knock_hands:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_knock_spring")
    show cg nb_knock_spring onlayer cgl
    "She yanks the sweats to her thighs. It springs up so hard it slaps her stomach."
    if nb.peek:
        "You look."
        "It's {i}huge{/i}. Thick and veined, the head flushed nearly purple, a fat clear bead rolling down the underside. Under her balls she's soaking too, glistening down her thighs."
        "It throbs. It throbs {i}at{/i} you."
        nb_tess "\"Don't look at it like that. Don't—\""
        "You squeeze your eyes shut. Too late."
    else:
        "You keep your eyes screwed shut. It doesn't help: there's still the heat of her, a hand's width from your face, and the smell, and her breathing."
    show cg nb_knock_hands onlayer cgl
    "Knees. Your own rug. You reach out like it's a hot pan."
    "It's hot as a fever and hard as a table leg. One hand doesn't close round it. Two don't either."
    nb_tess "\"Oh. Oh god. That works— your hands {i}work{/i}—\""
    vn_sfx "Shlk. Shlk. Shlk."
    "You stroke her, clumsy, both fists. Pre-cum runs over your knuckles."
    nb_ellis "\"I'm not gay! I'm not gay! This is just helping! This is just— {i}helping{/i}—\"" with vnfx("shake")
    nb_tess "\"I know. I know, you're helping so much, I'm sorry, don't stop—\""
    "Her hips go. Little jerks, then bigger, fucking up into your fists. Her hand clamps on your shoulder. It swells in your grip, harder still."
    nb_tess "\"Oh god— oh god— I'm sorry, I'm gonna—\""
    show cg nb_knock_cum onlayer cgl
    "It goes off like a hose." with vnfx("flash")
    "The first rope hits your wrists so hot you moan. The next goes up your forearm. The next hits the hollow of your throat and runs under your collar."
    "You keep pumping because she's begging you to, and it keeps coming: hands, wrists, neck, thick and white, way too much."
    $ _nb_m = nb_map("hands", "throat")
    "When it stops you're kneeling there, eyes shut, dripping from the elbows down."
    "It's still hard. A bit less. Still standing up between your hands. Tessa stares down at it, then at you, face on fire."
    menu:
        "Still standing up between your hands."
        "Keep your hands on her":
            jump nb_knock_sex
        "Go and scrub it off":
            jump nb_knock_scrub

label nb_knock_after:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_flat onlayer bgl
    if nb_enc.partner_came:
        "She comes again, on her knees on your rug with her forehead on your shoulder, saying sorry into your neck the whole time. This time it finally goes down."
    else:
        "She stops your hands with hers, shaking."
        nb_tess "\"It's going. It's going down. Oh my god.\""
    "\n{size=-5}{color=#ff8fa3}▸ Go and scrub it off{/color}{/size}"
    jump nb_knock_scrub

label nb_knock_scrub:
    $ nb_advance(1)
    $ vn_enter(bg="nb_bathroom", pc="shy", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_bathroom onlayer bgl
    nb_tess "\"Thank you, sorry, thank you, {i}sorry{/i}—\""
    "She's gone before you've got your breath back. Sweats up, hoodie down, door banging."
    show cg nb_scrub onlayer cgl
    "Shower. Hot tap all the way. You scrub your hands, wrists, arms, throat, until the skin's pink and the soap's a sliver."
    "It's off. You watched it go down the drain."
    if _nb_m:
        "{color=#ff5fb8}[_nb_m]{/color}"
    "But your hands smell sweet. Warm-sugar sweet. {i}Her{/i}."
    show cg nb_scrub_arm onlayer cgl
    $ _nb_feel = nb_body(1)
    "{color=#ff5fb8}And the hair on your forearms is gone in a smooth strip, wrist to halfway up, exactly where it ran.{/color}"
    "You rub it with your thumb. Smooth. Slick-smooth, like a girl's freshly shaved leg."
    vn_sfx "Shiver."
    "Your cock twitches in your boxers."
    nb_ellis "\"What the fuck. What the {i}fuck{/i}—\""
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    nb_ellis "\"Just this once.\""
    "You tell your bathroom. It sounds smaller than it did on the landing."
    hide cg onlayer cgl
    show bg nb_flat onlayer bgl
    "In bed in the dark you keep lifting your wrist to your nose. Every time you smell her, your stomach does something low and slow."
    "Your fingers keep curling round nothing under the duvet. Thumb under the ridge. Twist at the top. You never learned that."
    "Your phone lights up. {color=#e0559a}it went down. it actually went down. i'm so sorry. thank you. i'm so sorry{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump nb_morning

## ---- the mornings (Neighbour Morning, Visit, Visit Dose), the café, the evening's door ------------

label nb_morning:
    $ nb.fit = "cage" if (nb.tier or 0) >= 3 else None
    $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_bedroom onlayer bgl
    "Morning. Your own bed."
    if nb.tier == 1:
        show cg nb_wake_1 onlayer cgl
        "You lift your wrist to your nose before your eyes are open. Sweet. Warm sugar. {i}Her{/i}."
        "Your cock's hard under the duvet. You don't touch it. You smell your wrist again instead, and again, until your hips are rocking."
    elif nb.tier == 2:
        show cg nb_wake_2 onlayer cgl
        "You lick your lips. Still fuller. Still soft. You can still taste her."
        nb_ellis "\"It's not gay.\""
        "You tell the ceiling, and it comes out a pout."
    elif nb.tier == 3:
        show cg nb_wake_3 onlayer cgl
        "You wake up hard in the cage: a tight, sweet throb pressing at the plastic, going nowhere."
        "Your hips rock against the sheet on their own. The key's in her pocket, across the landing."
    elif nb.tier == 4 and nb_femboy():
        show cg nb_wake_4f onlayer cgl
        "Your thighs are pressed together under the duvet, soft and heavy, and your ass fills your boxers. Your little puffy nipples buzz against the sheet when you breathe."
        "The cage is snug. It drips."
        nb_ellis "\"Don't need you.\""
        "You tell it, giggling."
    elif nb.tier == 4:
        show cg nb_wake_4t onlayer cgl
        "Your new little tits are tender against the sheet. You cup one and gasp."
        "The cage hangs roomy and your tiny cock slides about in it, soft."
        nb_ellis "\"No.\""
        "You moan it, squeezing. It doesn't sound like no."
    else:
        show cg nb_wake_5 onlayer cgl
        "You wake up empty. Everything low down aches for her. Your hand's between your legs before you're awake."
        "Tonight. You'll get more tonight."
    $ _nb_c = nb_craving()
    if _nb_c:
        "{color=#b7b7b7}The wanting: [_nb_c].{/color}"
    hide cg onlayer cgl
    jump nb_offer_visit

## The ordinary visit: optional, before your shift, the mornings after rungs 1, 3 and 4.
label nb_offer_visit:
    if (nb.tier or 0) in (1, 3, 4):
        menu:
            "Before your shift."
            "Tessa, before your shift":
                jump nb_visit
            "Off to the café":
                pass
    jump nb_cafe

label nb_visit:
    $ vn_enter(bg="nb_flat", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "mortified" if nb.tier == 1 else "grin")], cg=None)
    show bg nb_flat onlayer bgl
    if nb.tier == 1:
        "A knock. Three polite raps this time."
        "Tessa. Grey sweats, tented to the waistband. Arms crossed low over it. Face scarlet."
        nb_tess "\"It's back. I'm sorry. I'm {i}so{/i} sorry. I tried everything. It's back.\""
    elif nb.tier == 3:
        "She's already on your sofa when you come out. Your spare key on your coffee table. Feet up."
        "Gym shorts, the hem barely covering the root of it, the rest lying fat along her thigh."
        nb_tess "\"Hey. You took ages.\""
    else:
        $ nb.fit = "skirt"
        "Her text came before your alarm: {color=#e0559a}be ready. skirt. latch off.{/color}"
        "So you're on the edge of your bed in the skirt, knees together, latch off. Your door clicks shut."
        nb_tess "\"Good. Good. Lie back.\""
    menu:
        "How do you ask?"
        "Ask her nicely":
            $ nb.mood = "shy"
        "Tell her to hurry up, then":
            $ nb.mood = "bratty"
        "Just reach for her":
            $ nb.mood = "eager"
    hide nb_tessa
    if nb.mood == "bratty":
        nb_ellis "\"Fine. Get it out. I've got things to do.\""
        "You don't. She grins and does as she's told."
    elif nb.mood == "eager":
        "You don't say a word. You reach for her with both hands before she's finished asking, and the noise she makes is the best thing you've heard all day."
    else:
        nb_ellis "\"Okay. Come here.\""
        "You whisper it to her knees. She does."
    if nb.tier == 1:
        show cg nb_visit_1 onlayer cgl
        "Sofa. She stands over you; you sit on the edge with your eyes screwed shut and both hands round her. They don't close. She's bigger than last night."
        vn_sfx "Shlk. Shlk. Shlk."
        nb_ellis "\"I'm not gay! This is just helping! I'm {i}helping{/i}!\"" with vnfx("shake")
        nb_tess "\"I know— oh god, you're helping so much— don't stop—\""
        "She doesn't last. She comes with a gasp, hand clamped on your shoulder, hot and thick over your knuckles and up your forearms." with vnfx("flash")
        $ _nb_m = nb_map("hands")
    elif nb.tier == 3:
        show cg nb_visit_3 onlayer cgl
        "Knees. Your own rug, between her spread thighs. She tugs the shorts aside and you don't pretend to look away any more."
        nb_tess "\"Breathe through your nose.\""
        "Her hand on the back of your head, and she takes you down. You know how now. Throat open. Nose in her."
        vn_sfx "Hlk. Hlk. Glk."
        "Your eyes roll up happily. Your caged cock leaks, useless."
        nb_ellis "\"Mmnh— I'm not— {i}mmf{/i}—\""
        nb_tess "\"Not gay. I know. Good girl. Boy. Good boy.\""
        "She finishes straight down your throat. All of it, warm, into your stomach." with vnfx("flash")
        $ _nb_m = nb_map("mouth", "throat")
    else:
        show cg nb_visit_4 onlayer cgl
        "She shoves you back on the bed, hitches the skirt, and slides it between your thighs from under the hem, hot and slick and huge."
        "One big hand squeezes your knees shut round it. She rocks."
        vn_sfx "Shlk. Shlk. Shlk."
        "The head bumps your stomach. Your cage rubs the top of it. You can't stop moaning."
        nb_tess "\"You're not gay.\""
        "She says it for you."
        nb_ellis "\"…right. Right— yeah— Tessa, finish on me, finish {i}on{/i} me, all over me, please—\""
        if nb_femboy():
            "She does: up your stomach, across the hem, then she pulls back and paints your thighs, and rubs it in with her palm while you whimper." with vnfx("flash")
            "Your caged cock lies in the mess, soft and tiny. She rubs round it. Never on it."
            nb_tess "\"That's not for anything.\""
            "You giggle, because it isn't."
            $ _nb_m = nb_map("stomach", "thighs")
        else:
            "She does: up your stomach and across your chest in long hot ropes, and you're rubbing it in before she's stopped, round and round, the way she taught you." with vnfx("flash")
            $ _nb_m = nb_map("stomach", "chest")
    if _nb_m:
        "{color=#ff5fb8}[_nb_m]{/color}"
    $ _nb_v = nb_visit_line()
    "[_nb_v]"
    if (nb.tier or 0) >= 3:
        "Then she kisses the top of your head and lets herself out. You go to work smelling of her."
    else:
        "Then she goes, quick, hoodie yanked down. You go to work smelling of her."
    hide cg onlayer cgl
    jump nb_cafe

label nb_cafe:
    $ vn_enter(bg="nb_cafe", pc="neutral", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_cafe onlayer bgl
    $ nb.fit = "apron"
    if nb.tier == 2:
        show cg nb_cafe_spoon onlayer cgl
        "All day at the café your reflection in the coffee machine looks freshly kissed."
        "You lick the foam off a spoon, slow, tongue flat, lips sealed round it, and only notice when the customer stares. You never did it like that before."
        hide cg onlayer cgl
    else:
        "The café. The steamer, the queue, the bus. All day her smell comes and goes off your skin."
    "\n{size=-5}{color=#ff8fa3}▸ Home after your shift{/color}{/size}"
    $ vn_until(19)
    $ nb.fit = None
    if nb.tier == 1:
        jump nb_again
    elif nb.tier == 2:
        jump nb_spare_key
    elif nb.tier == 3:
        jump nb_rung_skirt
    else:
        jump nb_rung_wait

## ---- rung 2: in your mouth (Neighbour Again, Again Mouth, Again Night, Again Morning) -------------

label nb_again:
    $ vn_enter(bg="nb_flat", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "mortified")], cg=None)
    show bg nb_flat onlayer bgl
    show nb_tessa mortified at vn_cast_slot
    "A knock. You know whose."
    nb_tess "\"It happened again.\""
    "Same grey sweats, and they've stopped hiding anything. The long thick line of it lies up her stomach under the cotton, the head pushing the waistband out, a wet patch spreading."
    "It's bigger. Your hands remember."
    nb_tess "\"Every night. Fine when I go to bed, and then I wake up and— today I had to cancel my clients. I tried on my own for an hour. It only goes down for you.\""
    nb_ellis "\"Tessa.\""
    nb_tess "\"I know.\""
    "She looks at your mouth. Looks away. Looks back."
    nb_tess "\"It's so sensitive now, hands are too much, and I thought— not all of it. Just the tip. Your mouth, just the tip. It'd be quicker—\""
    "She runs out of words. She just stands in your doorway, hand flat over the front of her sweats."
    menu:
        "Just the tip."
        "Bargain":
            $ nb.mood = "bratty"
        "Say yes to the floor":
            $ nb.mood = "shy"
        "Already be kneeling":
            $ nb.mood = "eager"
    if nb.mood == "bratty":
        nb_ellis "\"You're doing my washing-up. For a month. And carrying my shopping up the stairs. Forever.\""
        nb_tess "\"Yes. Yes. Anything. Forever.\""
        nb_ellis "\"And you don't look at me while I do it.\""
        nb_tess "\"I won't look.\""
        "She lies."
    elif nb.mood == "eager":
        "You're on your knees with your hands on her hips before she's finished the sentence. She stares down at you like you've grown wings."
        nb_tess "\"Oh. Oh. {i}Okay{/i}.\""
    else:
        nb_ellis "\"Okay. Just the tip.\""
        "You tell the floor."
        nb_tess "\"Just the tip.\""
        "She agrees, faintly."
    hide nb_tessa
    show cg nb_again_tip onlayer cgl
    "She drags the sweats down and it swings out heavy into your face. Salt. Heat. That sweet smell, stronger tonight. It twitches, leaking."
    "You lean in slow and touch it with the very tip of your tongue—"
    show cg nb_again_splash onlayer cgl
    "—and she comes." with vnfx("flash")
    "A shocked {i}ah{/i}, and it splashes across your mouth, lips, chin, cheek, and some lands right on your tongue."
    nb_tess "\"Sorry— sorry, oh my god, it's been all {i}day{/i}—\""
    "It tastes like her smell. Your face is dripping. She's still {i}completely{/i} hard."
    nb_tess "\"Just the tip.\""
    "Hoarse. She puts her hand in your hair. Gentle. Guiding."
    show cg nb_again_suck onlayer cgl
    "Your lips close round the fat smooth head and you suck, and the sound she makes goes straight through you."
    vn_sfx "Mmh. Mmh. Glk."
    "Only the head fits, and it stretches your jaw. You suck it like a sweet, both fists pumping below your lips. Drool runs down your wrists. You're moaning round her and you can't stop."
    nb_ellis "\"It's not gay if it's— {i}mmf{/i}—\""
    "She pushes back in on the word. She laughs, shaky, keeps going, and you forget what it wasn't."
    nb_tess "\"Your {i}mouth{/i}, oh my god— I'm gonna— swallow, please, please swallow—\""
    show cg nb_again_swallow onlayer cgl
    "She comes in your mouth. It floods your tongue so fast your cheeks puff out. You panic, then swallow. Gulp. Again. Again." with vnfx("flash")
    "Some escapes down your chin to your neck. The rest goes down warm and sits in your stomach, glowing. Your first mouthful of anybody, ever."
    $ _nb_m = nb_map("face", "mouth")
    if _nb_m:
        "{color=#ff5fb8}[_nb_m]{/color}"
    "You sit back on your heels, gasping, licking your lips. You don't mean to."
    menu:
        "She's still hard."
        "Let her keep going":
            jump nb_again_sex
        "Wipe your chin":
            jump nb_again_night

label nb_again_after:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_flat onlayer bgl
    if nb_enc.partner_came:
        "She finishes in your mouth again. You swallow without being asked. She watches you do it, mouth open."
    else:
        "She pulls you up off the rug by your shoulders, shaking, and rests her forehead on yours."
    "\n{size=-5}{color=#ff8fa3}▸ Wipe your chin{/color}{/size}"
    jump nb_again_night

label nb_again_night:
    $ nb_advance(2)
    $ vn_enter(bg="nb_landing", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "mortified")], cg=None)
    show bg nb_landing onlayer bgl
    show nb_tessa mortified at vn_cast_slot
    "At the door, hoodie pulled down over it, Tessa hesitates."
    nb_tess "\"Can I have your spare key? So I'm not knocking out on the landing like {i}that{/i}. I won't use it. Not unless.\""
    show cg nb_key onlayer cgl
    "You give her your spare key. She closes her hand round it like it's warm."
    $ nb.key_given = True
    hide cg onlayer cgl
    hide nb_tessa
    "In bed, you can't stop licking your lips. They feel fuller. Swollen, like you've been kissing for an hour. You can still taste her.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump nb_again_morning

label nb_again_morning:
    $ _nb_feel = nb_body(2)
    $ vn_enter(bg="nb_bathroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_mirror_mouth")
    show cg nb_mirror_mouth onlayer cgl
    "{color=#ff5fb8}Bathroom mirror. Your mouth. Fuller. Plumper, pinker, a soft little pout you didn't have yesterday. Your jaw's a step softer at the corners.{/color}"
    "You poke your bottom lip. It's {i}squishy{/i}."
    nb_ellis "\"Oh no. Oh no, oh no—\""
    "It comes out a pout."
    show cg nb_mirror_waist onlayer cgl
    "{color=#ff5fb8}You pull your shirt up. Your waist dips in above your hips now, right where it went down warm and sat all night. Your boxers are tighter at the back.{/color}"
    "You grab a handful of your own ass, and it {i}gives{/i}. Soft. Rounder than yesterday."
    nb_ellis "\"Mmh—\""
    "Your cock jumps. You let go fast. You grab it again."
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    "You brush your teeth very thoroughly. You can still taste her."
    hide cg onlayer cgl
    jump nb_cafe

## ---- rung 3: down your throat; the cage, FORCED (Neighbour Spare Key, Throat, Rung Cage) ----------

label nb_spare_key:
    $ vn_enter(bg="nb_flat", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "grin")], cg="nb_sofa")
    show cg nb_sofa onlayer cgl
    "She's on your sofa."
    "Feet up, trainers off, your spare key on your coffee table. Grey gym shorts whose hem barely covers the root of it. Thighs spread, and it lies along one of them, thick as your wrist, the head shining past the hem."
    nb_tess "\"Hey. Took you ages.\""
    "She doesn't get up."
    nb_ellis "\"You let yourself in.\""
    nb_tess "\"You gave me a key.\""
    "She pats the rug between her feet. Not the sofa."
    nb_tess "\"Come here.\""
    nb_ellis "\"Tessa, I've just got in—\""
    nb_tess "\"I know. I've been waiting.\""
    "No sorry. Not any more."
    "And you go. Fast. You're on your knees before you've thought, and she's tugging the shorts aside, and you don't even pretend to look away. Both hands. They don't meet. The gap's wider than last time."
    nb_tess "\"I've been thinking about how you only ever get the top bit.\""
    nb_ellis "\"It doesn't fit.\""
    nb_tess "\"It'll fit.\""
    "Her hand settles on the back of your head."
    nb_tess "\"Breathe through your nose.\"\n{size=-5}{color=#ff8fa3}▸ Breathe through your nose{/color}{/size}"
    jump nb_throat

label nb_throat:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_throat_down")
    show cg nb_throat_down onlayer cgl
    "She takes you down slow. The head over your tongue. Then more. Past where it always stopped."
    "Your throat flutters round her, and you moan. She holds you there and strokes your hair with her thumb."
    nb_tess "\"Nose. In through your nose. Then swallow. Like a pill.\""
    "You breathe in. You swallow. Your throat opens round her."
    vn_sfx "Hlk."
    show cg nb_throat_root onlayer cgl
    "She slides in, thick and endless, your eyes rolling up, hands clutching her thighs, until your nose is pressed into the hot damp skin at her base. That's all there is to breathe."
    nb_tess "\"Good girl. Boy. Good {i}boy{/i}. God. All the way down.\""
    "She sounds surprised."
    vn_sfx "Glk. Glk. Hlk. Glk."
    "Short strokes, never letting you off. Your head goes light and floaty. Drool down your chin. Your own cock's rock hard in your shorts, nothing touching it."
    "She lets you up once. You come off gasping, strings of spit from your lips to her."
    nb_ellis "\"I'm not— I'm {i}not{/i}—\""
    nb_tess "\"Not gay. I know.\""
    "Kindly. She puts you back down to the root."
    show cg nb_throat_cum onlayer cgl
    "And you come. In your shorts. Untouched. Just her in your throat and her hand in your hair." with vnfx("flash")
    "Your hips jerk at nothing, you moan so loud it buzzes in her, and it soaks through your shorts in hot pulses."
    nb_tess "\"Did you just—? Oh my {i}god{/i}. Did you just come from that?\""
    "She comes a few strokes later, straight down your throat. No taste this time. Just heat, pumping into your stomach."
    $ _nb_m = nb_map("mouth", "throat")
    if _nb_m:
        "{color=#ff5fb8}[_nb_m]{/color}"
    menu:
        "When she lets you off you're sitting in a puddle of your own spit."
        "Let her keep your throat":
            jump nb_throat_sex
        "Wipe your face":
            jump nb_rung_cage

label nb_throat_after:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_flat onlayer bgl
    if nb_enc.partner_came:
        "She holds you to the root while she comes. You swallow round her without being told."
        nb_tess "\"Good boy.\""
    else:
        "She lets you off at last. You fall back against the sofa, throat buzzing, chin soaked, grinning at her like an idiot."
    "\n{size=-5}{color=#ff8fa3}▸ Wipe your face{/color}{/size}"
    jump nb_rung_cage

## THE ONE FORCED BEAT (owner, 2026-11-11): the cage goes on over your protest.
label nb_rung_cage:
    $ vn_enter(bg="nb_flat", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "certain")], cg=None)
    show bg nb_flat onlayer bgl
    show nb_tessa certain at vn_cast_slot
    nb_tess "\"You keep doing that.\""
    nb_ellis "\"Doing what?\""
    nb_tess "\"Finishing first. On the rug, and now in your shorts. Then you go all shy and I've still got ages to go.\""
    "She digs in her gym bag and comes up with something small and pink."
    nb_tess "\"So.\""
    show cg nb_cage_out onlayer cgl
    "A cage. Pink plastic, a ring, a tiny padlock, a key on a loop."
    show nb_pc protesting
    nb_ellis "\"Where did you {i}get{/i}— no. No, Tessa. I'm not putting that on.\""
    nb_tess "\"Shorts off.\""
    nb_ellis "\"I said no—\""
    "She doesn't argue. She just gets your soaked shorts down herself, one hand, while you grab at her wrist."
    show cg nb_cage_on onlayer cgl
    "She's a trainer and you're not. She holds you still against the sofa with her forearm and kneels up and fits it herself, and you push at her the whole time and it makes no difference at all."
    nb_ellis "\"Tessa— Tessa, {i}stop{/i}, I don't want—\""
    "Ring behind your balls. Cage over your soft little cock. Snug enough to feel your pulse in it."
    vn_sfx "Click." with vnfx("shake")
    "She holds the key up between you on its loop, unbothered, certain. Then it goes in the pocket of her gym shorts."
    nb_ellis "\"Give it back.\""
    nb_tess "\"You don't need it.\""
    "Her hand flat on the cage."
    nb_tess "\"You've got me.\""
    hide cg onlayer cgl
    hide nb_tessa
    $ nb_advance(3)
    $ _nb_feel = nb_body(3)
    $ nb.fit = "cage"
    "{color=#ff5fb8}Overnight it settles through your hips and thighs.{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_mirror_soft")
    show cg nb_mirror_soft onlayer cgl
    nb_ellis "\"Fuck.\""
    "Morning. It comes out a step lighter, sweet at the edges. You say it again to check."
    nb_ellis "\"{i}Fuck{/i}.\""
    "Higher. Hotter."
    "{color=#ff5fb8}Your boxers are tight across the back. You twist at the mirror: your ass sits up round and soft, and when you smack it, it {i}jiggles{/i}.{/color}"
    "{color=#ff5fb8}Your thighs touch at the top now. And the hair's gone everywhere: legs, belly, chest, pits, smooth as the strip on your wrist. Your hair's longer too; it tickles the back of your neck.{/color}"
    nb_ellis "\"Ohh— that's so {i}soft{/i}—\""
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    "You swallow, and your throat just opens. No gag. Nothing. Like a door. You never practised that."
    "The cage is still snug. The key's still in her pocket."
    "You wake up hard in it: a tight, sweet throb, pressing at the plastic, going nowhere. You could knock across the landing and ask for your key."
    "You don't. Your hips start rocking against the sheet on their own."
    hide cg onlayer cgl
    jump nb_offer_visit

## ---- rung 4: rubbed in; THE FORK (Neighbour Rung Skirt, Skirt Scene, Fork Chest/Thighs/Morning) ----

label nb_rung_skirt:
    $ nb.fit = "skirt"
    $ vn_enter(bg="nb_bedroom", pc="shy", pc_tag="nb_pc", cast=[], cg="nb_skirt_text")
    show cg nb_skirt_text onlayer cgl
    "Her text came at teatime. {color=#e0559a}wear the skirt. it helps me finish.{/color}"
    "Then: {color=#e0559a}latch off.{/color}"
    "The skirt was on your bed when you got in, folded. A short black miniskirt with nothing to it."
    show cg nb_skirt_wait onlayer cgl
    "You're wearing it. It's loose at the hips. It sits low and slides when you move, the hem brushing smooth, hairless thighs. The cage makes a little pink shape under it."
    "Latch off. You sit on the edge of your bed, knees together, and wait. Every set of footsteps on the stairs, your heart goes."
    "The skirt rides up every time you shift. You stop shifting.\n{size=-5}{color=#ff8fa3}▸ Wait for her{/color}{/size}"
    $ vn_pass(20)
    jump nb_skirt_scene

label nb_skirt_scene:
    $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[("nb_tessa", "grin")], cg=None)
    show bg nb_bedroom onlayer bgl
    show nb_tessa grin at vn_cast_slot
    "Your door closes. The latch goes on. She's in your bedroom doorway in gym shorts and a sports bra. Her eyes go to the skirt. Your thighs. Your knees, pressed together."
    nb_tess "\"Oh. Oh, look at you.\""
    nb_ellis "\"You said it helps you finish.\""
    "You tell your knees."
    nb_tess "\"It does. Lie back. Knees together. Keep them together.\""
    hide nb_tessa
    show cg nb_skirt_thighs onlayer cgl
    "She climbs over you and takes it out. It's {i}enormous{/i} now, lying across your stomach from the hem to past your belly button, heavy as a rolling pin."
    "She slides it in under the hem, between your thighs from below, hot and slick, and squeezes your knees shut round it with one hand."
    nb_tess "\"There. Oh, {i}there{/i}.\""
    vn_sfx "Shlk. Shlk. Shlk."
    "It slides through the tight squeeze of your thighs. The head pops out the top of the hem and bumps your stomach, drags over the cage on the way back, and you {i}moan{/i}."
    nb_ellis "\"Ahh— {i}ahh{/i}— Tessa— oh god, that's so— {i}ahh{/i}—\""
    nb_tess "\"Good girl. Good— boy. Good boy. Squeeze.\""
    "You squeeze. She groans. Skirt rucked round your waist, bed creaking, your thighs getting slicker every stroke, until it runs down onto your sheets."
    nb_tess "\"You're not gay. Go on, I know you're about to say it. You're not gay.\""
    nb_ellis "\"…right. Right— yeah— Tessa, please, finish on me, I want it all over me, please, {i}please{/i}—\""
    ## skirt-cum: three passes (v1h-v1j) drew the pair as one merged figure; the skirt-thighs frame
    ## stays up for this beat until a redraw passes (SCENES.md, for the owner's review)
    show cg nb_skirt_thighs onlayer cgl
    "She pulls back and comes up your body. A long thick rope to your sternum. Across your chest. Again, again, pooling in your waist, over your nipples, up to your collarbone." with vnfx("flash")
    "You lie there in the wreck of the skirt, panting, painted. Tessa sits back on her heels between your knees."
    nb_tess "\"Rub it in.\""
    nb_ellis "\"What?\""
    nb_tess "\"Rub it in. Don't waste it.\""
    "You look down at yourself. At her, all over you. At your hands."
    menu:
        "Don't waste it."
        "Rub it into your chest" (ending=True):
            $ nb.branch = "tsf"
            jump nb_fork_chest
        "Wipe it off" (ending=True):
            $ nb.branch = "femboy"
            jump nb_fork_thighs

label nb_fork_chest:
    $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_fork_chest")
    show cg nb_fork_chest onlayer cgl
    "You put your hands flat on your chest and rub it in."
    "Slow circles at first. Then faster. Over your nipples, stiff and so sensitive every pass makes you twitch, until it's not on you any more. It's {i}in{/i} you, a warm tight glow under the skin."
    nb_tess "\"That's it. All of it.\""
    "You scoop the last off your stomach and rub that in too. Your chest tingles so hard you can feel your heartbeat in your nipples."
    nb_tess "\"Good girl. ...Boy.\""
    $ _nb_m = nb_map("chest", "stomach")
    "She lies beside you, propped on an elbow, and lays two fingers on your sternum."
    nb_tess "\"It's warm. Is it supposed to be warm?\""
    nb_ellis "\"I don't know.\""
    "Nobody does.\n{size=-5}{color=#ff8fa3}▸ Sleep it off{/color}{/size}"
    call vn_night(7)
    jump nb_fork_morning

label nb_fork_thighs:
    $ vn_enter(bg="nb_bedroom", pc="shy", pc_tag="nb_pc", cast=[], cg="nb_fork_thighs")
    show cg nb_fork_thighs onlayer cgl
    "You grab the sheet and start wiping your chest. Tessa laughs, big and disbelieving, and catches your wrist."
    nb_tess "\"No. Oh no. Not on my watch.\""
    "She scoops a thick white smear off your stomach, shoves the skirt up, and rubs it into your thighs herself. The soft insides. The backs. Up under the curve of your ass, both hands, kneading, until your thighs are slick and hot and shaking."
    nb_tess "\"There. If you won't put it where it goes, I'll put it where I want it.\""
    nb_ellis "\"Where's that?\""
    "She grabs a handful of your ass, hard. You squeak."
    nb_tess "\"Guess.\""
    $ _nb_m = nb_map("thighs", "ass")
    "\n{size=-5}{color=#ff8fa3}▸ Sleep it off{/color}{/size}"
    call vn_night(7)
    jump nb_fork_morning

label nb_fork_morning:
    $ nb_advance(4)
    $ _nb_feel = nb_body(4)
    $ nb.fit = "cage"
    if nb_femboy():
        $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_morning_4f")
        show cg nb_morning_4f onlayer cgl
        "{color=#ff5fb8}Morning. Your thighs are thicker. They press together all the way up, soft and heavy. You squeeze one and it {i}squishes{/i}.{/color}"
        nb_ellis "\"Oh fuck.\""
        "{color=#ff5fb8}Your ass has real weight now; it moves after you when you stand. You grab it with both hands. Two big soft handfuls. You knead, and moan, and can't stop kneading.{/color}"
        nb_ellis "\"Ahh— what did she {i}do{/i}—\""
        "{color=#ff5fb8}Your waist pinches in tight above your hips. Your hair brushes your shoulders. And your chest has gone puffy: two soft little swells round your pink nipples, tender and buzzing, and that's all it's ever going to be.{/color}"
        "You pinch one."
        nb_ellis "\"{i}Hah{/i}—!\""
        "The cage is still snug. Snugger. It drips when you squeeze your ass. Your little cock doesn't even try to get hard in there."
        nb_ellis "\"Don't need you.\""
        "You tell it, giggling, and go back to your ass."
        "You put the skirt back on. Still loose at the hips. Not loose at the ass."
    else:
        $ vn_enter(bg="nb_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_morning_4t")
        show cg nb_morning_4t onlayer cgl
        "{color=#ff5fb8}Morning. Your chest tingles, warm and swollen, right where you rubbed it in. Shirt off at the mirror: two small soft swells under your nipples. Little buds, puffy, pink, so sensitive the air makes you gasp.{/color}"
        "You cup one. It fills the middle of your palm. You squeeze."
        nb_ellis "\"{i}Hnnh{/i}—! Oh god— I've got— they're {i}tits{/i}— {i}ahh{/i}—\""
        "{color=#ff5fb8}A cups. Tiny. Yours. Your hips have flared out overnight. Your ass pushes your boxers out behind you, round and heavy. Your hair brushes your shoulders.{/color}"
        "And the cage sits roomy on you now. Your cock's shrunk in it, small and soft, sliding about in the plastic."
        nb_ellis "\"No. No, no, no—\""
        "You moan it, still squeezing. It doesn't sound like no."
        "The skirt's still loose at the hips. You put it on anyway."
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    "You sit on the bed, and your knees press together on their own, tight, the way she likes them. You never learned that."
    hide cg onlayer cgl
    jump nb_offer_visit

## ---- rung 5: inside you (Neighbour Rung Wait, Her Door, Inside Sex/After, Inside Morning). MANDATORY. ---

label nb_rung_wait:
    $ nb.fit = "skirt"
    $ vn_enter(bg="nb_bedroom", pc="shy", pc_tag="nb_pc", cast=[], cg="nb_wait")
    show cg nb_wait onlayer cgl
    "Skirt on. Latch off. Phone face-up on the bed beside you. Ready since teatime. The skirt's snug at the hips now. It hugs."
    "She doesn't text. She doesn't knock."
    "You hear her door open across the landing. Close. Nothing."
    $ _nb_where = "ass" if nb_femboy() else "chest"
    "It starts in your hands, where it landed the first night: not an itch, a {i}wanting{/i}. Then your mouth waters so hard you have to swallow, and your throat remembers, and your stomach clenches, empty."
    "Your thighs. Your [_nb_where]. Everywhere she's ever landed is awake and asking for her."
    $ _nb_c = nb_craving() or "badly"
    "{color=#b7b7b7}The wanting: [_nb_c].{/color}"
    "You last about an hour.\n{size=-5}{color=#ff8fa3}▸ Cross the landing{/color}{/size}"
    jump nb_her_door

label nb_her_door:
    $ vn_enter(bg="nb_landing", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "certain")], cg="nb_her_door")
    show cg nb_her_door onlayer cgl
    "You knock on her door the way she knocked the first night. Side of your fist. Again and again."
    "Tessa opens it in a towel round her hips, damp, hair down, tits bare, the towel tenting out in front. She leans on the frame and looks you over: the skirt, your shaking hands. The dimple comes up slow."
    nb_tess "\"I wanted to see if you'd come to me.\""
    nb_ellis "\"You didn't come. You didn't {i}come{/i}.\""
    "Your voice cracks."
    nb_tess "\"No. Come in.\""
    show bg nb_tessa_kitchen onlayer bgl
    hide cg onlayer cgl
    show nb_tessa certain at vn_cast_slot
    "She makes you stand in her kitchen in the skirt while she dries her hair. You stand there shaking, fists clenched, mouth watering. You don't move, because she hasn't said you can."
    nb_tess "\"You missed me. I heard you pacing. Through two doors and a landing. Up and down. Up and down.\""
    "The dimple."
    nb_tess "\"Best thing I've ever heard.\""
    hide nb_tessa
    show bg nb_tessa_bedroom onlayer bgl
    show cg nb_her_bed onlayer cgl
    "Then she takes you to bed. On your back in the middle of it. She kneels between your knees, pushes the skirt up, and smiles at the cage."
    "A bottle from the drawer. She slicks two fingers while you watch."
    nb_tess "\"Colour?\""
    nb_ellis "\"...what?\""
    nb_tess "\"Colour. Green's go. Yellow's slow down. Red's stop.\""
    "Cool wet fingers between your thighs, under the cage, finding you."
    nb_tess "\"Colour?\""
    nb_ellis "\"Green.\""
    show cg nb_her_fingers onlayer cgl
    "One finger. Circling, pressing, in. You gasp at her ceiling. She waits till you breathe, then goes on. Two fingers. Curling, stretching, working you looser until you're rocking down onto her hand, whimpering, the cage leaking on your stomach."
    nb_tess "\"Colour?\""
    nb_ellis "\"{i}Green{/i}. Green, green, Tessa, please—\""
    "Her fingers slide out. You actually whine. The towel drops."
    "It's bigger than it's ever been. She pushes your knees up to your chest and holds them with one arm, slicks the whole length, and lines it up."
    nb_tess "\"Say it. I know you want to say it.\""
    nb_ellis "\"I'm not gay.\""
    "It comes out tiny."
    nb_tess "\"No.\""
    "She presses the fat head of it against you."
    nb_tess "\"You're just mine.\"\n{size=-5}{color=#ff8fa3}▸ Green{/color}{/size}"
    jump nb_inside_sex

label nb_inside_after:
    $ nb_advance(5)
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_inside_after")
    show cg nb_inside_after onlayer cgl
    if nb_enc.partner_came:
        "She comes buried to the root, forehead on yours, your knees by your ears. It throbs up into your stomach and keeps coming until you feel {i}full{/i}. She doesn't pull out. She kisses you, open-mouthed and slow."
    else:
        "She stops buried to the root, forehead on yours, both of you shaking. Then she comes anyway, without moving, a slow heavy pulse. She doesn't pull out."
    if nb_femboy():
        "Your cock never even got hard. It just bounced in its cage the whole time, soft and tiny, drooling all over your stomach, and nobody touched it once."
        nb_ellis "\"Didn't need it. Didn't need it {i}at all{/i}.\""
        "You giggle up at her, dazed."
        nb_tess "\"Nope.\""
        "She flicks the cage, and you squeal."
    $ _nb_m = nb_map("inside")
    if _nb_m:
        "{color=#ff5fb8}[_nb_m]{/color}"
    nb_tess "\"Stay. I'm not taking it out.\""
    "It's not a question. She lowers your legs and settles on top of you, cock still deep, and pulls the sheet over you both. You fall asleep pinned under her, full of her.\n{size=-5}{color=#ff8fa3}▸ Sleep with her still in you{/color}{/size}"
    call vn_night(7)
    jump nb_inside_morning

label nb_inside_morning:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg=None)
    show bg nb_tessa_bedroom onlayer bgl
    "You wake up in her bed. She slipped out of you in the night. The warmth didn't. It sits low and heavy, and shifts when you move."
    nb_ellis "\"Morning.\""
    "The voice that comes out isn't yours."
    if nb_femboy():
        show cg nb_morning_5f onlayer cgl
        $ _nb_feel = nb_body(5)    # the body lands on its line, under the mirror frame (timing walk, 2026-11-12)
        "{color=#ff5fb8}It's high. Light and breathy. You clap a hand over your mouth, then say \"hello\" to the ceiling just to hear it again.{/color}"
        "{color=#ff5fb8}Her bathroom mirror. Your face is pretty. Not a girl's, not a boy's: sweet, soft at the jaw, lips full, lashes dark. Your hips flare under the skirt from a pinched-in waist. Your chest is just puffy, two soft little swells and nothing more.{/color}"
        "You hike the skirt and grab your ass. It spills out of your hands. Heavier. Rounder. High and fat."
        nb_ellis "\"Oh my god. Oh my {i}god{/i}—\""
        "The cage is exactly as snug as it was. Your cock lies in it soft and small and doesn't so much as twitch at any of it."
        nb_ellis "\"Doesn't matter. You don't matter.\""
    else:
        show cg nb_morning_5t onlayer cgl
        $ _nb_feel = nb_body(5)    # the body lands on its line, under the mirror frame (timing walk, 2026-11-12)
        "{color=#ff5fb8}It cracks down the middle, and when it comes back it's {i}higher{/i}, light and sweet, and it stays there.{/color}"
        "{color=#ff5fb8}Her bathroom mirror. Your face has gone round and soft, lips full, lashes dark. Your chest: not buds now. Small soft handfuls that sit up on their own and wobble when you breathe.{/color}"
        "You grab them. Both. C cups, real handfuls, warm and heavy, nipples stiff against your palms."
        nb_ellis "\"Ohh— {i}ohh{/i}, fuck—\""
        "You squeeze and moan in her bathroom in your new voice, and hearing it makes it hotter. The cage barely touches you. It hangs. There's hardly anything in it."
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    "You clench, and something low down clenches back, slow and knowing. You never practised that."
    hide cg onlayer cgl
    nb_tess "\"Come back to bed.\""
    "She says it from her pillow, eyes shut. When you do, she curls round you, mouth at your ear."
    nb_tess "\"My door's open. Every night. You know where it is.\"\n{size=-5}{color=#ff8fa3}▸ Stay in her bed{/color}{/size}"
    if nb_femboy():
        jump nb_exactly_enough
    jump nb_last_dose

## ---- rung 6, TSF: the last dose (Neighbour Last Dose, Shift, Ride Start, After, End Last) ------------

label nb_last_dose:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_last_morning")
    show cg nb_last_morning onlayer cgl
    "Morning. Face-down in her bed. She's lying along your back, heavy and warm, and hard, the long hot weight of it in the crease of your ass."
    "The cage is barely hanging on. It swings loose against the sheet. There's hardly anything left in it."
    "Tessa wakes the way she does now: all at once, mouth on the back of your neck, hand already reaching for the bottle."
    nb_tess "\"Morning. Mine.\""
    "You open your mouth to say the thing you always said. It isn't there. What comes out, high and sweet, is:"
    nb_ellis "\"Yours.\""
    "She laughs, low, and slides into you."
    menu:
        nb_ellis "\"Ahh— {i}ahh{/i}— Tessa—\""
        "Push back onto her":
            $ nb.mood = "eager"
        "Hold the pillow and take it":
            $ nb.mood = "shy"
    jump nb_last_dose_sex

label nb_last_dose_shift:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_shift_melt")
    show cg nb_shift_melt onlayer cgl
    if nb_enc.partner_came:
        "She comes deep, pinning you face-down with her whole weight, flooding you. The most it's ever been. It spreads out from your belly to your fingertips."
    else:
        "She grinds in to the root and holds it, both of you gasping, then comes without moving, deep. It spreads out through you like heat."
    "And then something lets go."
    $ nb_advance(6)
    $ nb.shifted = True
    $ _nb_feel = nb_body(6)
    "{color=#ff5fb8}Between your legs. In the cage. A slow melting warmth, and your little cock goes soft, {i}differently{/i}. It shrinks. Draws back. Keeps drawing back, sinking into you, and your balls draw up and are gone, and where they were—{/color}"
    show cg nb_shift_open onlayer cgl
    "{color=#ff5fb8}—where they were, you {i}open{/i}. Two soft lips swelling apart against her sheet, slick and hot, and a little nub at the top that throbs once, hard.{/color}" with vnfx("shake")
    "You moan into the pillow, long and high."
    vn_sfx "Click."
    "The cage slides off. Nothing left to hold it. It drops onto the sheet between your knees."
    "{color=#ff5fb8}And it's everywhere at once. Your tits swell down into the mattress, heavy, spilling out under you, way past handfuls. Your hips spread. Your ass rounds out under her. Hair slithers down over your shoulders. Your waist pulls in tight. Petite and stacked, in her bed, with her still inside you.{/color}"
    nb_tess "\"Oh. Oh, {i}there{/i} she is.\""
    show cg nb_shift_back onlayer cgl
    "She pulls out slow and rolls you onto your back. Your tits, heavy and round, wobbling as you breathe. Your hips. And between your legs, where the cage was: a pussy, puffy and pink and soaking."
    "She runs two fingers through it, once. You buck off the bed."
    "{color=#ff5fb8}You grab your tits. Your hands sink in and they spill out between your fingers. F cups. Heavy. Yours.{/color}"
    nb_ellis "\"Ahh— my {i}tits{/i}— Tessa, I've got {i}tits{/i}— {i}ahh{/i}—\""
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    nb_tess "\"You don't need it.\""
    "She holds the cage up between you."
    nb_tess "\"You've got me.\""
    show cg nb_ride_lap onlayer cgl
    "She leans back against the headboard and hauls you onto her lap by your hips. You're straddling her, thighs spread, her cock standing up between your legs, the head nudging your new lips."
    nb_tess "\"Go on. Your turn.\""
    menu:
        "Your turn."
        "Sink down slowly":
            $ nb.ride = "slow"
        "Drop onto her all at once":
            $ nb.ride = "fast"
        "Grind on it first":
            $ nb.ride = "grind"
    if nb.ride == "fast":
        "You don't wait. You line her up, the fat head notched right at your new lips, and get ready to let your knees go."
        nb_ellis "\"Wait— Tessa— it's so {i}big{/i}—\""
    elif nb.ride == "grind":
        "Not yet. You sit down on it lengthways, the whole hot shaft pressed up between your new lips, and grind. Forwards, back. It slides over your clit every time. You're moaning before you've started."
        nb_tess "\"Tease.\""
        nb_ellis "\"Ahh— {i}mine{/i}.\""
        "You lift up, and hold the head against you, right there, slick and ready."
    else:
        "You lower yourself slowly, her hands on your hips, not pushing. The head kisses your new lips. Spreads them. You stop, gasping, hovering. Your thighs are shaking."
    nb_ellis "\"Oh my god. Tessa, it's never going to fit, it's so {i}big{/i}—\""
    nb_tess "\"It will.\""
    "She's staring up at you. Her hands slide up to your tits and squeeze, and your whole body clenches."
    nb_tess "\"Down. Ride it. Show me.\"\n{size=-5}{color=#ff8fa3}▸ Ride her{/color}{/size}"
    jump nb_last_dose_ride

label nb_last_dose_after:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_ride_after")
    show cg nb_ride_after onlayer cgl
    "You lie on her, sweaty and boneless, tits squashed on her chest, her cock softening in you at last. Every bit of you is soft. Every bit of you is {i}finished{/i}."
    "Her hand strokes your hair. The other rests on your ass like she owns it."
    nb_tess "\"You okay?\""
    "You reach for the old word, the one you said over and over. It isn't there. There's only the one that is."
    nb_ellis "\"Yours.\""
    "You say it into her neck, in your new voice.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    jump nb_end_last

label nb_end_last:
    $ achievement.grant("The Last Dose")
    $ vn_enter(bg="nb_tessa_bedroom", pc="neutral", pc_tag="nb_pc", cast=[], cg="nb_end_last")
    show cg nb_end_last onlayer cgl
    "Later, on her pillow, Tessa holds her hand out flat between you. The cage is in her palm. Small as a knuckle."
    nb_tess "\"You don't need it. You have me.\""
    "You're sprawled against her side, tits heavy on her ribs, pussy still slick and throbbing from her. When you open your mouth the voice is sweet and light and yours."
    nb_ellis "\"Yours.\""
    "She drops the cage in the drawer by the bed. That's the last you see of it."
    "When you pull the skirt back on, it gapes at your waist and stretches tight over your hips. Tessa watches you tug at it and doesn't help at all."
    jump nb_epilogue_choice

## ---- rung 6, femboy: exactly enough (Neighbour Exactly Enough, Mm, Enough Sex/After, End Enough) -----

label nb_exactly_enough:
    $ nb.fit = "skirt"
    $ vn_enter(bg="nb_tessa_bedroom", pc="shy", pc_tag="nb_pc", cast=[("nb_tessa", "certain")], cg="nb_key_chain")
    show cg nb_key_chain onlayer cgl
    "Morning, in her bed. She's sitting on the edge of the mattress in a sports bra, threading the little key to your cage onto a fine gold chain. She fastens it round her neck. It drops between her breasts. She pats it."
    nb_tess "\"There. Now I always know where it is.\""
    "Her, in the morning. The long hum all day. Her again at night. Never in between. Knock in between and she says {i}mm{/i}, kisses your forehead, and goes to work."
    "Skirt rucked up, thighs pressed together, and you're already empty. Under the hem your cage is drooling on her sheet. Soft. It's always soft now."
    nb_ellis "\"Can I— could I have—\""
    nb_tess "\"One now. One tonight. That's it.\""
    nb_ellis "\"What if I—\""
    nb_tess "\"Mm.\""
    "Not no. Just {i}mm{/i}, and a warm smile with no give in it at all."
    nb_tess "\"Morning and night. Never more. Up. Knees and elbows.\""
    menu:
        "Morning and night. Never more."
        "Get on your knees and elbows":
            $ nb.mood = "eager"
            jump nb_enough_sex
        "Ask for more one more time":
            $ nb.mood = "bratty"
            jump nb_enough_mm

label nb_enough_mm:
    nb_ellis "\"Please. Just— another one. Just this once.\""
    nb_tess "\"Mm.\""
    "She laughs, and swats your ass. It wobbles, heavy and round. She watches."
    nb_tess "\"Just this once. I remember that one. Knees and elbows.\"\n{size=-5}{color=#ff8fa3}▸ Get on your knees and elbows{/color}{/size}"
    jump nb_enough_sex

label nb_enough_after:
    $ nb_advance(6)
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_enough_after")
    show cg nb_enough_after onlayer cgl
    if nb_enc.partner_came:
        "She finishes deep, holding your hips, every drop."
        nb_tess "\"Morning dose. Can't have my girl going soft.\""
    else:
        "She stops buried in you, then comes slow and deep without moving, until you're full."
        nb_tess "\"Morning dose. There.\""
    "Your cage swung and drooled under you the whole time, soft and tiny. Nobody touched it."
    "She keeps you on it, kneeling up behind you, thumbs circling the dimples at the base of your spine until you stop shaking."
    nb_tess "\"Feel that? That's you sorted till tonight.\""
    "Warm, heavy, full. The hum gone quiet. Exactly enough. Not a drop over."
    $ _nb_feel = nb_body(6)
    if _nb_feel:
        "{color=#ff5fb8}[_nb_feel]{/color}"
    show bg nb_mirror onlayer bgl
    show cg nb_mirror_look onlayer cgl
    "Then she stands you in front of her wardrobe mirror, chin on top of your head."
    nb_tess "\"Look.\""
    "{color=#ff5fb8}A pretty face, lips full and pink, hair spilling past your shoulders. The skirt hugging your ass like it was cut for it. Thighs thick and soft and pressed together. Your waist tiny between it all. The cage snug under the hem.{/color}"
    "You reach back and grab it. Your fingers sink in and it spills over them, fat and heavy, bigger than it was last night."
    nb_ellis "\"Ohh— {i}fuck{/i}, look at it—\""
    "Her hand cups your chest, the soft little puff of it under her palm, your nipples poking into it."
    nb_tess "\"Puffy here.\""
    "Her other hand takes a big soft handful of your ass and squeezes."
    nb_tess "\"Round here.\""
    nb_ellis "\"{i}Hnnh{/i}— squeeze it more—\""
    "She does. The cage drips onto her carpet. She glances down at it. Tiny, soft, leaking, not even trying."
    nb_tess "\"Cute. Useless. Cute.\""
    nb_ellis "\"Don't need it. Never did.\""
    nb_tess "\"You don't need anything else. You've got me. Exactly enough of me. Say it.\""
    nb_ellis "\"Say what?\""
    nb_tess "\"Say you're my girlfriend.\""
    menu:
        "Say you're my girlfriend."
        "Say it to her face":
            $ nb.said = "face"
        "Say it to the mirror":
            $ nb.said = "mirror"
        "Make her wait for it":
            $ nb.said = "wait"
    jump nb_end_enough

label nb_end_enough:
    $ achievement.grant("Exactly Enough")
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cast=[], cg="nb_end_enough")
    show cg nb_end_enough onlayer cgl
    if nb.said == "mirror":
        nb_ellis "\"I'm your girlfriend.\""
        "You say it to the girl in the mirror, her hands all over you. The mirror goes pink to the ears. Tessa laughs and kisses the top of your head."
    elif nb.said == "wait":
        "You make her wait. You turn in her arms and stare up at her, silent, until she says your name in that voice."
        nb_ellis "\"I'm your girlfriend.\""
        "Sweetly, right into her face. She picks you up off the floor."
    else:
        nb_ellis "\"I'm your girlfriend.\""
        "You turn in her arms and say it straight up into her face. She looks at you like you've handed her something."
    show cg nb_sofa_night onlayer cgl
    "Night. The night dose. Then her sofa, the telly on, neither of you watching."
    "Crop top, skirt, knees up, tucked into her side. The cage snug under the hem, and the key rising and falling on its chain between her breasts."
    "Every so often, without looking, her hand slides from your shoulder down to your ass. Squeezes. Goes back. Checking. It never goes to the cage."
    nb_ellis "\"It's decoration.\""
    "You tell her, giggling, and she laughs into your hair. You're full. Exactly enough."
    nb_ellis "\"You know. I was never gay.\""
    "She starts to laugh. You poke her and say it properly."
    nb_ellis "\"I'm your girlfriend.\""
    nb_tess "\"Yeah. You are.\""
    "And she kisses the top of your head, and doesn't laugh at all."
    jump nb_epilogue_choice

## ---- the epilogue (either ending, same body) -------------------------------------------------------

label nb_epilogue_choice:
    menu:
        "Her door, your door, the landing between."
        "Move in across the landing" (ending=True):
            jump nb_epilogue_move_in
        "Keep your own door" (ending=True):
            jump nb_epilogue_own_door

label nb_epilogue_move_in:
    $ vn_enter(bg="nb_tessa_flat", pc="eager", pc_tag="nb_pc", cast=[("nb_tessa", "grin")], cg=None)
    $ renpy.show("cg nb_epi_move_in_" + ("f" if nb_femboy() else "t"), layer="cgl")   # the body the ending left you
    "You move in across the landing. One evening, same boxes. Tessa carries them two at a time."
    "Your toothbrush goes next to hers. The skirt goes on the hook on her bedroom door, where she can see it from the bed."
    if nb_femboy():
        "The key stays on its chain, between her breasts. She's never once used it. You've never once asked."
    else:
        "The drawer by the bed stays shut."
    "First morning, she wakes you with her mouth on the back of your neck. You roll into her before you're awake."
    if nb_femboy():
        "Morning. Night. Nothing in between. All day at the café you feel it running out of you, and every evening she's on the sofa, patting the cushion. You go.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    else:
        "No schedule. She has you when she wants you, which is all the time, and you have her when you want her, which is more. She keeps buying you bras. They keep not fitting. She's delighted.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump nb_route_return

label nb_epilogue_own_door:
    $ vn_enter(bg="nb_landing", pc="eager", pc_tag="nb_pc", cast=[], cg=None)
    $ renpy.show("cg nb_epi_own_door_" + ("f" if nb_femboy() else "t"), layer="cgl")   # the body the ending left you
    "You keep your own door. It's a technicality. Her door's always on the latch, and her spare key hangs inside yours."
    if nb_femboy():
        "Morning and night, you cross the landing in the skirt. In between: the café, the steamer, the bus, and the hum getting louder, and the cage drooling in your knickers every time you think about her. When it's time, you go.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    else:
        "You cross the landing whenever you like. Whenever she likes. It's usually the same time. Your skirt lives on her bedroom door now.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump nb_route_return
