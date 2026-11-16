## THE SOURCE: sister's passages, rewritten for the VN (2026-11-11; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, ending.twee), as beats; the director scenes are in
## scenes.rpy and the act menu's chores in acts.rpy.

## ---- film night (Sister Opening, Sister Film Night) --------------------------------------------------

label si_opening:
    $ si_init()
    $ si.fit = None
    $ vn_enter(bg="si_lounge", pc="neutral", pc_tag="si_pc", cast=[], cg="si_flat_night")
    show cg si_flat_night onlayer cgl
    "Paige is not your sister."
    "Everybody gets it wrong. The neighbours. Her office. The corner-shop man, who's called you \"the girls\" for a year and a half."
    "You met at nineteen in a house share above a chip shop and have shared flat 2C since twenty-one. She's twenty-six. You're twenty-seven. Lowell and Lister."
    "No blood in it anywhere: same kettle, same sofa, one endless argument about the bins."
    show cg si_rabbit onlayer cgl
    show si_paige warm at vn_cast_slot
    "Tonight she's comfortably drunk, feet in your lap, phone held up over her face. She's found something."
    si_paige "\"Okay. Don't laugh.\""
    "She turns it round. A pink rabbit, a sparkly logo: {color=#ff8fd0}Imouto+{/color}. {=si_hypno}{i}The family you deserve, one session at a time.{/i}{/=si_hypno}"
    si_harry "\"What is that.\""
    si_paige "\"I always wanted a little sister. Somebody to do hair with. Somebody who thinks I'm brilliant.\""
    "She tells the ceiling, in her third-glass voice."
    si_harry "\"I think you're brilliant.\""
    si_paige "\"You think I'm {i}adequate{/i}.\""
    "The onboarding music is so cheerful it makes your teeth fizz. {=si_hypno}{i}Realism guarantee! Seamless sibling scenarios for cosy fun! Use responsibly!{/i}{/=si_hypno}"
    si_harry "\"Is this {i}legal{/i}?\""
    "You're grinning anyway."
    si_paige "\"It says consent required. Look, right there.\""
    "She jabs the screen. Then she gives you the face you have never once, in all the years of the kettle and the sofa, managed to say no to."
    menu:
        "That face."
        "“Ten minutes. Then I'm picking the film.”":
            $ si.mood = "bratty"
            si_harry "\"Ten minutes. Then I'm picking the film, and it's got a car chase in it.\""
            si_paige "\"Deal.\""
            "Far too quickly."
        "“Go on, then. Ten minutes.”":
            $ si.mood = "sweet"
            si_harry "\"Go on, then. Ten minutes.\""
            "Paige makes a small delighted noise into the cushion."
    jump si_movie_night

## ---- rung 1: the app's (Sister Movie Night, Bath Night, Bath Finish/After, Bath Towels) ---------------

label si_movie_night:
    $ si_advance(1)
    $ vn_enter(bg="si_lounge", pc="neutral", pc_tag="si_pc", cast=[("si_paige", "warm")], cg="si_crosshairs")
    show cg si_crosshairs onlayer cgl
    "She taps {color=#ff8fd0}Start Session{/color} half as a joke. Crosshairs wobble over your face. {=si_hypno}{i}Target subject: please select.{/i}{/=si_hypno} She taps that too, giggling."
    "A flash, no louder than the rain on the window."
    $ si_note_lines = ["Session begun! Realism guarantee active. For optimal results, please keep the subject comfortable."]
    show screen si_app(si_note_lines)
    $ si.mode = "mae"
    show si_pc eager at vn_pc_slot
    "You blink. The room skips, like a telly changing channel."
    hide screen si_app
    show cg si_eyes onlayer cgl
    "Paige tells you later what it looks like from her side: your eyes go pink. Lit from inside, soft and glowing, with a little heart where the black of each eye should be, and they stay that way the whole session, every session."
    si_mae "\"Big sis!\""
    "Bright, high, delighted, the most natural thing you've ever said. You're Mae. You've always been Mae."
    "Big sis looks tired. She's had a whole week of the spreadsheet woman, and what she needs is tea."
    si_mae "\"Do you want your tea with honey tonight? I'll make it sweet!\""
    show cg si_tea onlayer cgl
    "You're already up. Strawberry mug for you, the blue one with the chipped handle for her, honey behind the oats. You know it like your own hands."
    "Paige's mouth is open. It stays open."
    show cg si_brush onlayer cgl
    "Tea on the tray, a biscuit on each saucer. You fold onto the rug at her feet and hold the hairbrush up over your shoulder, because that's film night: she does yours, then you do hers."
    "She takes the brush. Her hand shakes a bit."
    si_paige "\"Mae?\""
    "Testing it."
    si_mae "\"Mm?\""
    si_paige "\"Nothing. Nothing, sweetheart.\""
    "You talk through the whole film, loud and happy, feet tucked under you."
    si_mae "\"Is she still doing the font thing? She's still doing the font thing, isn't she.\""
    show cg si_braid onlayer cgl
    "Paige laughs, shaky, then not. Your turn: you plait her hair into one fat braid and tie it off with the band from your wrist. She touches it afterwards like it's glass."
    "The film ends. You jump up and announce it, because somebody has to."
    si_mae "\"Bath night!\""
    si_paige "\"Is it?\""
    si_mae "\"It's {i}bath night{/i}, big sis. Come on. I'll do your back.\"\n{size=-5}{color=#ff8fa3}▸ Run the bath{/color}{/size}"
    jump si_bath_night

label si_bath_night:
    $ si.fit = "nude"
    $ vn_enter(bg="si_bathroom", pc="eager", pc_tag="si_pc", cast=[], cg="si_bath_run")
    show cg si_bath_run onlayer cgl
    "You sit on the edge of the bath testing the water, cold, hot, cold, until it's perfect. Bubbles. A ridiculous amount of bubbles, from the good glass bottle big sis saves for special occasions, because bath night is one."
    "You undress without thinking, like taking your shoes off. Your cock hangs soft against your thigh. It's just there, like an elbow."
    $ si_body(1)
    "{color=#ff5fb8}Your legs are smooth as anything. Every hair, gone. You run a hand up your shin in the steam and go \"{i}ooh{/i}\" out loud, because it feels {i}lovely{/i}, and do it again.{/color}"
    show cg si_bath_paige onlayer cgl
    "Then big sis undresses, and you watch like somebody who's going to have to wash all of it."
    "Tall, much taller than you. Swimmer's shoulders, dark hair knotted up, breasts high and round when she reaches back to pin it. And between her thighs, heavy and thick and stirring in the steam: her cock. Of course it's there. It's hers."
    "In you both get. You turn round on your knees and grab the sponge."
    si_mae "\"Back first. Lean forward.\""
    "Shoulders, neck, the knot at the bottom of her spine she blames on her chair. Then you turn her round by the shoulders and start on her front."
    show si_paige warm at vn_cast_slot
    si_paige "\"So the spreadsheet woman has started cc'ing my manager. On the font emails. Like I'm going to—\""
    "Slow soapy circles on her breasts. Her nipples go tight under your palms. She stops. Starts again."
    show si_paige warm at vn_cast_slot
    si_paige "\"—like I'm going to change my font because {i}Denise{/i}—\""
    show cg si_bath_hand onlayer cgl
    "Stomach. Hips. Then under the bubbles you take hold of her cock, because it's next. Thick and hot and getting heavier in your soapy hand by the second."
    si_mae "\"Hold still, big sis. Gotta get everywhere.\""
    vn_sfx "Shlk."
    "Slow. All the way up, thumb over the head, all the way down to the root. Her hips lift off the bottom of the bath to follow your hand."
    si_mae "\"Ooh, it's getting bigger. Is that the soap? It's the good soap. It's working.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"—about. Oh. {i}Oh{/i}, Mae.\""
    "She loses the sentence completely, head back on the tiles."
    si_mae "\"You're so tense, big sis. Is it the font? Is it Denise? Tell me about Denise.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"I don't— I can't— {i}fuck{/i}—\""
    si_mae "\"Language.\""
    "You squeeze. She makes a noise you've never heard her make."
    "Your hand knows exactly where: twist at the top, squeeze just under the head. Nobody ever showed you. And under the bubbles your own little cock has gone stiff against her thigh, and you giggle at it and don't stop."
    si_mae "\"Ooh— big sis, it's so {i}hot{/i}— {i}mmh{/i}— is it nice? Say it's nice— I want to do it {i}right{/i}—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"It's— {i}god{/i}, Mae— it's so nice—\""
    si_mae "\"{i}Yay{/i}.\""
    "And you go faster."
    menu:
        "Faster."
        "Keep your hand moving":
            jump si_bath_sex
        "Rinse her off":
            jump si_bath_finish

label si_bath_after:
    $ vn_enter(bg="si_bathroom", pc="beaming", pc_tag="si_pc", cast=[], cg="si_bath_after")
    show cg si_bath_after onlayer cgl
    if si_enc.partner_came:
        "Big sis comes with her head back on the tiles and both hands gripping the sides, pulsing hot and thick over your soapy fingers. It goes everywhere: your wrists, your chest, the bubbles."
    else:
        "Big sis stops you in the end with a hand over yours and a laugh like she's run a mile, and holds it there, shaking."
    si_mae "\"Now we've got to do the {i}water{/i} again!\""
    "Scandalised and thrilled. She laughs so hard she slides down the tiles.\n{size=-5}{color=#ff8fa3}▸ Towels{/color}{/size}"
    jump si_bath_towels

label si_bath_finish:
    $ vn_enter(bg="si_bathroom", pc="eager", pc_tag="si_pc", cast=[], cg="si_bath_rinse")
    show cg si_bath_rinse onlayer cgl
    si_mae "\"Rinse!\""
    "You scoop water over her with both hands, and don't let go of her while you do it. You never let go. You're proudest of that."
    "Slow and slippery, all the way up and down, water sheeting off her breasts, her breath going short."
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae, Mae, I'm—\""
    si_mae "\"Do it— do it, big sis— {i}ahh{/i}— all over my hands— I want to {i}see{/i}—!\""
    show cg si_bath_after onlayer cgl
    "She comes, head back on the tiles, pulsing hot and thick over your soapy fingers. It goes everywhere: your wrists, your chest, the bubbles." with vnfx("flash")
    si_mae "\"Big sis! Now we've got to do the {i}water{/i} again!\""
    "She laughs so hard she slides down the tiles.\n{size=-5}{color=#ff8fa3}▸ Towels{/color}{/size}"
    jump si_bath_towels

label si_bath_towels:
    $ vn_enter(bg="si_bathroom", pc="beaming", pc_tag="si_pc", cast=[], cg="si_towels")
    show cg si_towels onlayer cgl
    "You dry her off on the bathmat, kneeling, all of her. When you're done she bends down, kisses the top of your wet head, and stays there a while."
    show si_paige warm at vn_cast_slot
    si_paige "\"You're so thorough.\""
    "Into your hair, a bit wobbly."
    si_mae "\"That's a sister's job!\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl.\""
    "Very quietly, like she isn't sure she's allowed. You glow all the way back to the sofa."
    $ si.fit = None
    call si_chore_offer
    call si_bedtime
    jump si_detergent

## ---- the session nights' helpers --------------------------------------------------------------------

## One optional chore a night (owner, 2026-11-11), from what's unlocked.
label si_chore_offer:
    $ _si_list = si_acts()
    if not _si_list:
        return
    $ _si_items = [(n, k) for k, n in _si_list] + [("Not tonight. Bed.", "none")]
    $ _si_pick = renpy.display_menu([("One more chore for big sis?", None)] + _si_items)
    if _si_pick != "none":
        $ renpy.call("si_act_" + _si_pick)
    return

## Bedtime before rung 6: Paige taps the tablet, and Harry finds himself in the hall.
label si_bedtime:
    $ vn_enter(bg="si_hall", pc="puzzled", pc_tag="si_pc", cast=[("si_paige", "soft")], cg=None)
    show bg si_hall onlayer bgl
    "{=si_hypno}“Bedtime.”{/=si_hypno} Paige taps the tablet. The room skips."
    $ si.mode = "waking"
    show si_pc puzzled at vn_pc_slot
    "You're in the hall holding a mug of cold tea."
    si_paige "\"Good film?\""
    "From the sofa. You say it was good. You go to bed.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide si_paige
    call vn_night(7)
    return

## The waking evening (the hub's evening, linear): the flat, the rota, a bleed line, and Paige
## with the tablet. Two flavour links into the session; never a "no" (revamp, 2026-10-20).
label si_evening:
    $ si.mode = "waking"
    $ si.fit = None
    $ vn_until(18)
    $ vn_enter(bg="si_lounge", pc="neutral", pc_tag="si_pc", cast=[("si_paige", "warm")], cg=None)
    show bg si_lounge onlayer bgl
    $ _si_r = si_rota_line()
    "{color=#b7b7b7}[_si_r]{/color}"
    $ _si_b = si_bleed()
    if _si_b:
        "{color=#b7b7b7}[_si_b]{/color}"
    $ _si_s = si_session_line()
    if si.consenting:
        menu:
            "[_si_s]"
            "“Run it.”":
                $ si.balk = "yes"
            "Sit down next to her":
                $ si.balk = "sit"
    else:
        menu:
            "[_si_s]"
            "Flop down next to her":
                $ si.balk = "flop"
            "“My turn to pick the film.”":
                $ si.balk = "film"
    jump si_session

label si_session:
    $ vn_enter(bg="si_lounge", pc="neutral", pc_tag="si_pc", cast=[("si_paige", "warm")], cg=None)
    show bg si_lounge onlayer bgl
    if si.balk == "film":
        si_harry "\"My turn to pick. And it's got a car chase in it.\""
        "You reach for the remote."
        si_paige "\"Mm-hm.\""
        "And she taps {color=#ff8fd0}Start Session{/color} while you're still scrolling."
    elif si.balk == "flop":
        "You flop down next to her, feet in her lap, and ask what's on. She taps {color=#ff8fd0}Start Session{/color} instead of answering."
    elif si.balk == "yes":
        si_harry "\"Run it.\""
        "Before she can not-ask. She taps {color=#ff8fd0}Start Session{/color}."
    else:
        "You sit down next to her and put your feet in her lap, and wait. She taps {color=#ff8fd0}Start Session{/color}."
    "The room skips, like a telly changing channel."
    "{=si_hypno}“Sisters help sisters.”{/=si_hypno}"
    $ si.mode = "mae"
    show si_pc beaming at vn_pc_slot
    si_mae "\"Big sis!\""
    "Bright and high and delighted, the most natural thing you've ever said. You're Mae. You've always been Mae, and it's the evening, and big sis is right here."
    $ _si_next = {1: "si_rung_two", 2: "si_rung_three", 3: "si_rung_four", 4: "si_rung_five", 5: "si_rung_six"}[si.tier]
    $ renpy.jump(_si_next)

## ---- rung 1's waking day (Sister Detergent; the tablet) ------------------------------------------------

label si_detergent:
    $ si.mode = "waking"
    $ vn_enter(bg="si_bathroom", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_mirror_smooth")
    show cg si_mirror_smooth onlayer cgl
    "Bathroom mirror, toothbrush in your mouth, you notice."
    "{color=#ff5fb8}Your jaw. No stubble. Your arms, legs, chest, armpits: all of it gone overnight, smooth as a bar of soap. Not one razor in the flat has a hair on it.{/color}"
    si_harry "\"Paige? Is there something wrong with the washing powder?\""
    show si_paige soft at vn_cast_slot
    "She shuffles in, dressing gown, yawning."
    si_paige "\"No? Why?\""
    "You gesture at all of it. Even your knees."
    si_harry "\"I think your new detergent's nuked every hair I've got.\""
    si_paige "\"Probably the detergent.\""
    "She gets the bottle out from under the sink and frowns at it. Then she touches your forearm, leaves her fingers there a second too long, and makes a little noise."
    "{color=#ff5fb8}Your skin's gone soft. Properly soft. You poke your own arm. It's like poking a peach.{/color}"
    "{color=#ff5fb8}In the shower you run your palm down your chest, over your stomach, the inside of your thigh. Slick. Smooth. You stand under the water doing it again much longer than you need to.{/color}"
    "{color=#b7b7b7}Cruelty-free formula, you decide, and stop thinking about it.{/color}"
    hide cg onlayer cgl
    show bg si_kitchen onlayer bgl
    "Her phone's on the kitchen counter. It lights up pink while you fill the kettle, and she turns it face-down a fraction too fast."
    $ si_note_lines = [t for lv, t in si_notes(1)]
    show screen si_app(si_note_lines)
    "You only see it upside down."
    hide screen si_app
    show cg si_fridge_photo onlayer cgl
    "A new photo on the fridge, under the chip-shop magnet: you two on the sofa last night, her braid, your face blue in the telly light. You don't remember anyone taking it."
    si_harry "\"When was that?\""
    si_paige "\"Last night. You were happy.\""
    "True, as far as it goes."
    si_paige "\"Film night tonight.\""
    "She pushes a cup across. It isn't a question. It won't be one again. You said ten minutes once, on the sofa, as a joke, and that's the last time anybody in this flat asks."
    si_harry "\"Sure.\""
    "You can't think why not."
    hide cg onlayer cgl
    hide si_paige
    $ vn_until(18)
    show bg si_lounge onlayer bgl
    show cg si_tablet onlayer cgl
    "The tablet's on the arm of the sofa. It's never been locked."
    "You don't open it. You look at the notification on the lock screen, glowing pink, then turn it face-down and go and brush your teeth."
    $ si_note_lines = ["Session complete. Sister Level 2. Tap for summary."]
    show screen si_app(si_note_lines)
    "{color=#c48fff}You think about it, brushing. Then you stop thinking about it, all at once, like a light going off.{/color}"
    hide screen si_app
    hide cg onlayer cgl
    jump si_evening

## ---- rung 2: Paige's rota (Sister Rung Two, Morning Problem, Morning Done, Shirt) ---------------------

label si_rung_two:
    $ si_body(2)
    $ si_advance(2)
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "warm")], cg="si_tingly")
    show cg si_tingly onlayer cgl
    "{color=#ff5fb8}Your voice comes out where it lives, light and high and pleased with everything, and you chatter all the way down the hall. Your shirt rubs. Your nipples are tight little points and you keep rolling your shoulders.{/color}"
    "You pinch one through the cotton."
    si_mae "\"{i}Eep!{/i}\""
    "It goes straight down between your legs. You pinch the other one, so they're even."
    si_mae "\"{i}Ooh{/i}— big sis, they're all {i}tingly{/i}!\""
    si_paige "\"Are they.\""
    "Not looking at the telly at all."
    "{color=#ff5fb8}You put your hands on your waist on the way past the mirror. It dips in, neat and narrow, like somebody pinched it. You twist side to side to watch, delighted, then go and change.{/color}"
    show cg si_wardrobe onlayer cgl
    "Your half of the wardrobe is the left half. Always has been. Soft jumpers, a strawberry-print cardigan, sleep shorts, a fluffy top the colour of a sugared almond. That one. It fits like it was bought for you. It was, by big sis, for your birthday."
    $ si.fit = "fluffy"
    si_mae "\"Can I borrow your hoodie?\""
    si_paige "\"You've got your own!\""
    si_mae "\"Yours smells nicer!\""
    "She throws it down the hall. You wear it over the fluffy top, sleeves past your hands, feet in her lap. You watch her watch the film, narrate, and steal her crisps."
    "Late, she picks up the tablet and holds her thumb over something."
    $ si_note_lines = ["Extend session overnight? Recommended for morning routines!"]
    show screen si_app(si_note_lines)
    si_mae "\"Big sis?\""
    si_paige "\"Nothing.\""
    "She taps it. She doesn't ask."
    hide screen si_app
    si_paige "\"Overnight.\""
    "Mostly to herself. Then, soft: {=si_hypno}“Bed, trouble. Busy morning.”{/=si_hypno}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump si_morning_problem

label si_morning_problem:
    $ si.mode = "mae"
    $ vn_enter(bg="si_paige_room", pc="eager", pc_tag="si_pc", cast=[], cg="si_morning_tent")
    show cg si_morning_tent onlayer cgl
    "Kettle on. Two mugs. You nudge her bedroom door open with your hip."
    "She's sprawled across the duvet, one leg kicked out, mouth open, losing a fight with her pyjamas. And there's a tent in her boxers, aimed at the ceiling."
    si_mae "\"Big sis! Up!\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Five more minutes. Unless you want to deal with— {i}this{/i}.\""
    "A hand comes up blind. A groan, a little jerk of her hips."
    si_mae "\"Is it the morning problem again? You always make such a mess fixing it yourself. Then it's the sheets, and then it's the {i}laundry{/i}—\""
    "You're already climbing on. Paige opens one eye. She looks at you kneeling on her duvet in your fluffy top, and her face goes very warm and very helpless."
    show si_paige warm at vn_cast_slot
    si_paige "\"Sisters help sisters—\""
    si_mae "\"—with the morning problem!\""
    "In perfect deadpan unison, and you both dissolve."
    show cg si_morning_hands onlayer cgl
    "Thumbs in her waistband, wiggle. Her cock springs up and slaps her stomach, thick and flushed, a bead of wet at the tip. Both hands. It's so hot in the mornings."
    si_mae "\"Morning! Look at you, all grumpy. Slow first, right? Slow circles?\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Mm. Two hands. That's— yeah. Good girl.\""
    vn_sfx "Shlk. Shlk."
    "Fists stacked, twisting at the top the way she likes. Her hips start rolling up into your hands. You chat the entire time."
    si_mae "\"Is that good? That's good. You've gone all red. Big sis, you've gone {i}so{/i} red—\""
    "Then you stop. She actually whines."
    si_mae "\"The sheets. You'll get the sheets, and then it's laundry day again.\""
    "You give her cock a very serious look."
    si_mae "\"Less laundry.\""
    show cg si_morning_mouth onlayer cgl
    "And you take it in your mouth."
    show si_paige warm at vn_cast_slot
    si_paige "\"{i}Fuck{/i}.\""
    "To the ceiling."
    si_mae "\"Mmh! Mm-hm! Mmh— you taste— {i}mmf{/i}— you taste nice, big sis—\""
    "Loud with your mouth full. She tastes like salt and skin and morning, and you moan round her like she's breakfast."
    show si_paige warm at vn_cast_slot
    si_paige "\"Don't talk with your mouth—\""
    si_mae "\"Mmhf— talking's— half the {i}fun{/i}—\""
    vn_sfx "Gluk. Gluk. Gluk."
    "Down as far as you can go, nose in her, eyes glassy and happy, humming. She grabs the headboard with both hands. Your tongue finds the ridge under the head on its own, like it's always known where it was."
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae, Mae, I'm going to—\""
    si_mae "\"Mm-{i}hm{/i}! In my mouth, big sis— {i}please{/i}— no laundry—\""
    "You pop off for one second, lips shiny, beaming, then seal your lips and suck."
    show cg si_morning_swallow onlayer cgl
    "She comes with a groan muffled in her own arm, thick and hot, pulse after pulse over your tongue, and you swallow it like it's a race." with vnfx("flash")
    "You lick her clean so there's nothing left for the sheets, sit back on your heels, and open wide to show her."
    si_mae "\"All gone! No laundry!\""
    show cg si_rota_first onlayer cgl
    "Paige stares at you from under her arm, chest heaving. Then she gets up in a daze, finds a pen and paper in the kitchen drawer, writes a rota like any flatshare's, and sticks it on the fridge with the chip-shop magnet."
    show screen si_rota
    "{i}Bins. Descale the kettle. Bath night.{/i} And under those, same handwriting: {i}Morning problem: Mae{/i}. She ticks it. She initials the tick. {i}PL.{/i}"
    show si_paige warm at vn_cast_slot
    si_paige "\"There. Official.\""
    hide screen si_rota
    menu:
        "Hoarse. You're still kneeling on her duvet."
        "Go round again before breakfast":
            jump si_morning_sex
        "Breakfast":
            jump si_morning_done

label si_morning_after:
    $ vn_enter(bg="si_paige_room", pc="beaming", pc_tag="si_pc", cast=[], cg=None)
    show bg si_paige_room onlayer bgl
    if si_enc.partner_came:
        "Round two ends like round one: big sis's hand in your hair, your mouth full. You swallow that too and announce it to the whole flat."
    else:
        "Big sis lifts you off her by the shoulders in the end, laughing and wrecked. If you keep going she'll be late for her own laptop."
    si_mae "\"Another tick.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Another tick.\""
    "She agrees, and adds it.\n{size=-5}{color=#ff8fa3}▸ Breakfast{/color}{/size}"
    jump si_morning_done

label si_morning_done:
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_toast")
    show cg si_toast onlayer cgl
    "Toast. Far too much toast. You're telling big sis about a dream full of ducks when she glances at the clock and picks up the tablet."
    call si_chore_offer
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg=None)
    show bg si_kitchen onlayer bgl
    "She says it very gently. {=si_hypno}“Okay, sweetheart. Up you come.”{/=si_hypno}"
    jump si_shirt

label si_shirt:
    $ si.mode = "waking"
    $ si.fit = None
    $ vn_enter(bg="si_kitchen", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_shirt")
    show cg si_shirt onlayer cgl
    "You surface at the kitchen table mid-toast, jam on your thumb, a taste in your mouth you put down to the jam."
    "Your hair's over your ears and your collar. You keep meaning to get it cut, and keep not."
    "Your shirt is a problem."
    "{color=#ff5fb8}The cotton drags over your nipples every breath, every reach, until by lunchtime you're sitting bolt upright with your elbows pinned. A different shirt: same problem.{/color}"
    "{color=#ff5fb8}It feels {i}good{/i}. You press harder. Your nipples are puffy and hot under the cotton, and a little noise gets out of you before you can stop it.{/color}"
    si_harry "\"Chafing.\""
    "You mutter it, and order a softer shirt."
    "{color=#ff5fb8}Your belt needs a new notch, too. The waist's gone in, neat and narrow, like you've been to a gym you don't go to.{/color}"
    hide cg onlayer cgl
    show screen si_rota
    "There's a rota on the fridge now, in Paige's handwriting, ticked and initialled."
    si_harry "\"Is that a joke?\""
    "You tap the last line."
    show si_paige soft at vn_cast_slot
    si_paige "\"It's a joke.\""
    "Face very still."
    hide screen si_rota
    "{color=#b7b7b7}Flatshare humour. You laugh, a bit.{/color}"
    "Half your wardrobe is soft colours in your size. You stand in front of it in a towel a while, then decide it's Paige's overflow."
    $ si_note_lines = [t for lv, t in si_notes(2)]
    show screen si_app(si_note_lines)
    "Her tablet, on the arm of the sofa, glowing pink."
    hide screen si_app
    ## the patch (Sister Patch), once: the "sleepwalky" evening, which costs something you won't miss
    show bg si_lounge onlayer bgl
    si_paige "\"You've been a bit sleepwalky lately. Haven't you. Losing bits of the evening.\""
    "She tugs you down onto the sofa by the wrist. Yes. Exactly that. Hearing it said is such a relief you don't ask how she knew."
    si_paige "\"It's the not sleeping. Ten minutes. You'll feel loads better.\""
    "The tablet's already up. She doesn't ask; she never does now. {=si_hypno}“Eyes on me. There we go.”{/=si_hypno}"
    "{color=#7fd17f}You do feel loads better.{/color} Whatever was nagging you has gone somewhere you can't reach and won't miss."
    "{color=#b7b7b7}Something else has moved a little closer while you weren't looking.{/color}"
    hide si_paige
    jump si_evening

## ---- rung 3: the witnesses co-sign (Sister Rung Three, Brunch, Share, Share After, Jeans) ---------------

label si_rung_three:
    $ si_advance(3)
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "warm")], cg=None)
    show bg si_lounge onlayer bgl
    si_paige "\"So. The girls want to meet you. Properly. Brunch tomorrow, the bakery with the blue awning.\""
    "Halfway through the film, not casually at all. You sit bolt upright and spill the popcorn."
    si_mae "\"Nell? And Natalie? And Amber and Kate?\""
    si_paige "\"All of them.\""
    si_mae "\"Big sis! What do I {i}wear{/i}?\""
    show cg si_try_on onlayer cgl
    "It takes an hour and your whole half of the wardrobe, tried on at the long mirror while big sis lies on your bed narrating every outfit like a nature documentary, until you throw a sock at her."
    $ si_body(3)
    "{color=#ff5fb8}Your hips have filled out lovely, round and soft; everything with a waist sits on them like it was waiting. Your bum looks amazing in the blue skirt. You tell her so, repeatedly, turning to check.{/color}"
    show cg si_wobble onlayer cgl
    "You smack it. It {i}wobbles{/i}."
    si_mae "\"Big sis! Look how it wobbles! It's so {i}squishy{/i}. Feel it. No, feel it.\""
    "You grab two big soft handfuls and squeeze and moan a bit, right there at the mirror, and big sis makes a strangled noise from the bed."
    "You change in front of her without thinking once. There's your cock, tiny and soft and barely anything, like always, and big sis steps round the subject like a slipper on the floor. You don't notice. There's nothing to notice."
    $ si.fit = "blueskirt"
    "The blue skirt it is."
    hide cg onlayer cgl
    si_paige "\"Overnight.\""
    "She tells the tablet, later, and taps it.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(9)
    jump si_brunch

label si_brunch:
    $ si.mode = "mae"
    $ si.fit = "blueskirt"
    $ vn_enter(bg="si_cafe", pc="beaming", pc_tag="si_pc", cast=[], cg="si_brunch_table")
    show cg si_brunch_table onlayer cgl
    "The bakery with the blue awning does a brunch that's mostly cinnamon buns. Paige's friends have taken the big window table and filled it with plates before your coats are off."
    "Nell, from Paige's office: all eyeliner and opinions. Natalie, phone already out. Amber, with a gift bag, which is ominous. Kate, the oldest and quietest, who watches you come in with her coffee halfway to her mouth and doesn't drink it."
    show si_paige warm at vn_cast_slot
    si_paige "\"Everyone, this is Mae. My little sister.\""
    "Hand on your shoulder, voice perfectly steady."
    si_mae "\"Hi! Big sis talks about you all the time. Nell, I love your eyeliner. Is that the bun with the icing? Can I have the bun with the icing?\""
    show si_kate smile at vn_cast_slot
    "Nell's eyebrows go up and straight back down. Natalie looks at Paige. Paige looks at the ceiling. Kate sets her coffee down very carefully and smiles at you slowly."
    si_kate "\"Hello, Mae.\""
    "Like she's met you a hundred times."
    hide si_kate
    "After that it's easy. You talk straight through brunch: the film, the bath stuff in the glass bottle, big sis's braid, whether they do the buns in a box."
    "Inside an hour they've all worked it out. Not the details. But Kate keeps catching Paige's eye, Paige keeps going pink, Amber can't stop grinning, and by the next pot of coffee there's a silent, unanimous decision round the table to help."
    show si_kate smile at vn_cast_slot
    si_kate "\"We saw nothing.\""
    "Hand over her eyes. Then she peeks at you through her fingers, and you laugh, because it's funny even if you don't know why."
    hide si_kate
    show cg si_witnesses onlayer cgl
    "Natalie makes a group chat on the spot. You're not in it. It's called {i}Witnesses{/i}, and from the way they keep checking their phones and then you, it's mostly logistics and smugness."
    show si_nell smile at vn_cast_slot
    "Nell writes {i}SISTER DAY{/i} on a napkin in purple felt-tip, underlines it hard, and hands it to Paige."
    si_nell "\"For the fridge. I'm booking the salon.\""
    hide si_nell
    show si_amber smile at vn_cast_slot
    si_amber "\"And this is a little something—\""
    "She slides a gift bag across to you. Paige takes it off the table before your fingers touch it. She doesn't look inside."
    show si_paige warm at vn_cast_slot
    si_paige "\"No.\""
    si_amber "\"It's {i}skincare{/i}.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"It is not skincare.\""
    "The whole table shrieks. You don't know why. You shriek too.\n{size=-5}{color=#ff8fa3}▸ Walk home with big sis{/color}{/size}"
    hide si_amber
    jump si_share

label si_share:
    $ vn_enter(bg="si_lounge", pc="eager", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_towel_sofa")
    show cg si_towel_sofa onlayer cgl
    "There's a towel spread on the sofa already. You don't wonder who put it there."
    "Big sis sits on the arm of it, patient and fond and a little nervous at the corners."
    si_paige "\"Today I thought maybe we try something new. Something it's time for.\""
    "She swallows."
    si_paige "\"You trust me?\""
    si_mae "\"Of course! Sisters share everything, right?\""
    "It comes out like a line you've always known. She laughs, low and delighted."
    si_paige "\"Right. Right. Such a good girl. Come here, then.\""
    show cg si_share_down onlayer cgl
    "Face-down across the towel, a cushion under your hips, bum in the air, cheek on the good cushion that smells of her shampoo. She slides the blue skirt down slow, your knickers with it. You lift your hips to help."
    si_paige "\"You're so pretty, Mae. You're so {i}pretty{/i} like this.\""
    si_mae "\"I {i}know{/i}. Nell said.\""
    "The click of the lube cap. Her hands warming it. Then her fingers, slick and slow, circling. You jump and squeak and go loose."
    si_mae "\"Ooh— {i}cold{/i}— no, it's good, it's good, keep—\""
    show cg si_share_fingers onlayer cgl
    "One finger, easing in. Then a second. She takes her time, rocking, twisting, stretching you open, her other hand flat on the small of your back."
    si_mae "\"That's— oh, that's weird, that's good weird, big sis, that's— {i}ahh{/i}— do that again—\""
    "Your tiny cock's squashed soft against the towel and you couldn't care less. All of you has moved round to the back, to her fingers."
    si_paige "\"Tell me if it's too much, and I'll stop.\""
    si_mae "\"Don't you {i}dare{/i} stop.\""
    "Her fingers slide out. You whine about it, loud. Her knee sinks into the sofa by your hip. Then something much bigger and blunter and hotter presses right against you, slick, and pushes, and the head of her slips in and holds there."
    si_mae "\"{i}Ohh{/i}— oh, big sis— it's {i}in{/i}— it's so {i}big{/i}— more, more, I want the rest—\""
    si_paige "\"Push out a little for me, love.\"\n{size=-5}{color=#ff8fa3}▸ Push back for big sis{/color}{/size}"
    jump si_share_sex

label si_share_after:
    $ vn_enter(bg="si_lounge", pc="blissful", pc_tag="si_pc", cast=[], cg="si_share_after")
    show cg si_share_after onlayer cgl
    if si_enc.partner_came:
        "Big sis finishes buried to the root, her whole weight over you, groaning your name into the back of your neck, and you feel every hot pulse fill you while you shake."
    else:
        "Big sis stays buried in you, both of you shaking, until your breathing comes back down."
    "Your body knew how to take her the whole way. Breathe out, open, squeeze on the way back. Nobody ever taught you that."
    si_mae "\"Sisters share everything.\""
    "Mumbled into the cushion, enormously pleased with yourself."
    show si_paige warm at vn_cast_slot
    si_paige "\"They do.\""
    "Like she's run a marathon, laughing into your hair. She kisses one shoulder blade, then the other, so they're even."
    show screen si_rota
    "A warm flannel. Then you hear the pen at the fridge, and when you pad through later in her hoodie there's a new line on the rota under Nell's purple napkin. {i}Sisters share everything.{/i} Ticked. {i}PL.{/i}"
    hide screen si_rota
    call si_chore_offer
    call si_bedtime
    jump si_jeans

label si_jeans:
    $ si.mode = "waking"
    $ si.fit = None
    $ vn_enter(bg="si_hall", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_jeans")
    show cg si_jeans onlayer cgl
    "You wake late, loose and stretched, a deep warm fullness in your hips and the base of your spine."
    "You feel incredible. Floaty. Best massage of your life."
    "{color=#b7b7b7}Paige's yoga video, you decide, and book a chiropractor for Monday.{/color}"
    "Your hair's at your jaw now, where it was over your ears last week, and in the hall light there's red in it that was never there. You tuck it back. It falls forward again."
    "{color=#ff5fb8}Your jeans won't go on. Up your thighs fine, then they stop, flat, at a part of you that didn't used to be there. Round and soft. You stand in the hall in your pants, holding them up.{/color}"
    "You let go of the jeans and grab it. Both hands. It fills them, soft and heavy, and when you squeeze, a low hot noise comes out of you in the empty hall."
    si_harry "\"Dryer's shrinking everything.\""
    "You tell the hall."
    "Nobody looks at the front of you any more. Paige steps round you in the bathroom without a flicker. A whole thing you used to be self-conscious about has stopped being a subject, and the relief is so total you don't notice it's gone."
    hide cg onlayer cgl
    show screen si_rota
    "The rota's got Nell's purple napkin taped to it, {i}SISTER DAY{/i}, and a new row in Natalie's handwriting: {i}Weekends: brunch (Witnesses){/i}, initialled {i}NS{/i}."
    hide screen si_rota
    "Your phone buzzes. Kate, who you've barely met. {color=#ff8fd0}how've you been sleeping?{/color}"
    si_harry "\"Great!\""
    "You type it back, truthfully."
    $ si_note_lines = [t for lv, t in si_notes(3)]
    show screen si_app(si_note_lines)
    "Paige's lock screen, glowing pink on the counter."
    hide screen si_app
    ## the friends' evening (Sister Friends), once, awake
    $ vn_until(19)
    $ vn_enter(bg="si_lounge", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_friends")
    show cg si_friends onlayer cgl
    "Nell, Natalie, Amber and Kate arrive with wine and no warning. They always do."
    "They're perfectly normal with you all evening. Warmer than usual, actually."
    "Somebody starts a sentence with a name that isn't yours and turns it into a cough. Then somebody else does."
    show si_kate neutral at vn_cast_slot
    si_kate "\"How've you been sleeping?\""
    "With a lot of weight on it. You go for glasses, and the silence behind you stops the moment you come back."
    hide si_kate
    "{color=#b7b7b7}They're drunk. That's all.{/color}"
    hide cg onlayer cgl
    ## the week between the jeans and Sister Day (the calendar, route.rpy): Sunday to Friday
    "{color=#b7b7b7}Days of the same. Work from the sofa, film night, and never the end of a film. You don't mind, which you notice, and then don't.{/color}\n{size=-5}{color=#ff8fa3}▸ Days of the same{/color}{/size}"
    $ vn_pass(4 * 1440)
    jump si_evening

## ---- rung 4: Mae asks (Sister Rung Four, Salon, Salon Home, Skincare, Skincare Done, Photo Wall) -------

label si_rung_four:
    $ si_advance(4)
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "warm")], cg=None)
    show bg si_lounge onlayer bgl
    si_paige "\"Sister Day tomorrow. She's booked the salon. First thing. All of us.\""
    "Before the film's even started, pointing at Nell's napkin on the fridge."
    si_mae "\"{i}All{/i} of us?\""
    si_paige "\"Every single one. Natalie's made a spreadsheet.\""
    "You fling yourself backwards across the sofa and kick your feet in the air."
    si_mae "\"What colour should I go?\""
    si_paige "\"What colour do you want?\""
    si_mae "\"Red. Long. And down. You like it down.\""
    "Instantly, like it's a fact about you, like your birthday. Big sis looks at you a long moment."
    si_paige "\"I do like it down.\""
    "Your head in her lap all film, talking hair. She strokes yours and says nothing. Right at the end, when you've gone quiet, she taps the tablet without looking at it.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(9)
    jump si_salon

label si_salon:
    $ si.mode = "mae"
    $ vn_enter(bg="si_salon", pc="beaming", pc_tag="si_pc", cast=[], cg="si_salon_foil")
    show cg si_salon_foil onlayer cgl
    "The salon on the high street: mirrors, white leather, a playlist from about a decade ago. Nell's booked the whole back row. Big sis takes the next chair. The others line the window sofa with coffees and opinions."
    si_mae "\"Red. Like, {i}red{/i} red.\""
    "You tell the stylist, before she can ask."
    show si_nell smile at vn_cast_slot
    si_nell "\"Up? Something up would be cute on her—\""
    si_mae "\"Down. Long and down. Big sis likes it down.\""
    "\"Big sis likes it down,\" the stylist agrees gravely, catches Paige's eye in the mirror, and doesn't laugh."
    $ si_body(4)
    "The dye smells like a swimming pool and looks like jam. When she washes it out the water runs pink, and your hair falls round your face heavy and wet, longer than it has been in years, to your shoulders, so red it looks lit."
    si_mae "\"It's grown.\""
    "\"Grown like a weed since last time,\" the stylist says, and just evens the ends."
    show cg si_salon_mirror onlayer cgl
    $ si.fit = None
    "She dries it loose and straight and soft. The big mirror with the lights round it. There you are."
    "{color=#ff5fb8}Your face is softer than you thought. Fuller mouth. Kinder jaw. A girl with long red hair and a flushed, happy, pretty face, and she's you, she's always been you.{/color}"
    "{color=#ff5fb8}Under the black gown your chest is tingling. Two soft little swellings under your nipples, new and so sensitive.{/color}"
    "You sneak a hand under the gown and cup one. A real handful, nearly. Puffy and warm, a B cup at least, the nipple stiff against your palm. You squeeze."
    si_mae "\"{i}Mmh{/i}—!\""
    "Nell looks over. You beam at her and squeeze again under the gown, because it's {i}yours{/i}."
    show si_paige warm at vn_cast_slot
    si_paige "\"Perfect. You look exactly right, Mae. Just like always.\""
    "From the next chair, very softly. Nell takes a photo of the whole row. You're in the middle, red hair everywhere, and everybody else is looking at you.\n{size=-5}{color=#ff8fa3}▸ Home, and the photo wall{/color}{/size}"
    jump si_salon_home

label si_salon_home:
    $ vn_enter(bg="si_hall", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_photo_wall")
    show cg si_photo_wall onlayer cgl
    "The hallway photo wall: holidays, birthdays, brunches, a crooked line of frames. You go straight to it, nose nearly on the glass."
    "You're in every one. Of course you are. Long red hair, loose, in every frame: on the beach at the coast with big sis's sunglasses on your head, at Natalie's birthday with icing on your nose, moving into 2C at twenty-one with a box on your hip. Plain as your hands."
    si_mae "\"Look! Big sis, look, it's the one from the coast!\""
    "Paige stands behind you with both salon bags still in her hands and looks at the wall a long time."
    si_paige "\"I remember.\"\n{size=-5}{color=#ff8fa3}▸ That evening: skincare{/color}{/size}"
    $ vn_until(20)
    jump si_skincare

label si_skincare:
    $ vn_enter(bg="si_bathroom", pc="eager", pc_tag="si_pc", cast=[], cg="si_jars")
    show cg si_jars onlayer cgl
    "Big sis's skincare lives on the shelf over the bath, in jars labelled in marker: {i}Night Glow{/i}, {i}Under-Eye{/i}, {i}Big Sis's Secret Weapon{/i}. Tonight there's a new one at the end. Empty. {i}Sister Special{/i}."
    show si_paige warm at vn_cast_slot
    si_paige "\"Ready for the last step? It's the good one. You'll glow.\""
    show cg si_skincare_kneel onlayer cgl
    si_mae "\"Yes! Is it good for your skin? Nell says it's good for your skin. Nell's skin is {i}amazing{/i}, have you seen Nell's—\""
    "You're already kneeling on the bathmat, red hair pushed back, hands on your knees, face up at exactly the angle she can't look away from, eyes shut. Nobody taught you the angle."
    show si_paige warm at vn_cast_slot
    si_paige "\"Shh. Eyes shut.\""
    si_mae "\"They {i}are{/i} shut.\""
    vn_sfx "Shlk. Shlk."
    "Her sleep shorts go down. Her hand starts, slow and wet, right in front of your face, close enough to feel the heat of her. You grin with your eyes closed and stick your tongue out a little for the drop that touches your lip."
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae. Oh, Mae.\""
    si_mae "\"Is it soon? Is it nearly? Big sis, I can hear you, you're doing the breathing— {i}mmh{/i}— do it on me— on my face— {i}please{/i}, big sis, I've been so good—\""
    show cg si_skincare_cum onlayer cgl
    "Hot across your cheek, your nose, your lips, thick, then more over your eyelids and forehead. You make a delighted noise and hold very still so it doesn't run." with vnfx("flash")
    "Then her fingers smooth it in, careful as anything: under your eyes, over your cheekbones, along your jaw, little patting circles, the way she does the serum."
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl. {i}Very{/i} good girl.\""
    si_mae "\"Is it good for my skin?\""
    show si_paige warm at vn_cast_slot
    si_paige "\"It's fantastic for your skin.\""
    si_mae "\"{i}Knew{/i} it.\""
    menu:
        "Eyes still shut, glowing."
        "Ask for a second coat":
            jump si_skincare_sex
        "Let her pat it in":
            jump si_skincare_done

label si_skincare_after:
    $ vn_enter(bg="si_bathroom", pc="beaming", pc_tag="si_pc", cast=[], cg=None)
    show bg si_bathroom onlayer bgl
    if si_enc.partner_came:
        "The second coat goes on thicker than the first. Big sis rubs that in too, with her thumbs, laughing breathlessly because you won't stop asking if you're glowing yet."
    else:
        "Big sis catches your wrist in the end, kisses your knuckles, and says you've had enough serum for one night, you greedy thing."
    jump si_skincare_done

label si_skincare_done:
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_braid_sunday")
    show cg si_braid_sunday onlayer cgl
    "You're too pleased with yourself to sit still. Into the kitchen in big sis's hoodie, face glowing. You look at the rota a long time, then take the pen off its string and write your own line at the bottom, round and loopy, under all of hers."
    show screen si_rota
    "{i}braid Sunday?{/i} You don't tick it. It's a question."
    "Big sis reads it over your shoulder. She doesn't say anything. She takes the pen, ticks it, writes {i}PL{/i} next to the tick, and kisses the side of your head."
    hide screen si_rota
    call si_chore_offer
    call si_bedtime
    jump si_photo_wall

label si_photo_wall:
    $ si.mode = "waking"
    $ vn_enter(bg="si_bedroom", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_wake_red")
    show cg si_wake_red onlayer cgl
    "Your hair's long. First thing, sitting up, it falls in your face. Properly red, loose past your shoulders, soft as anything."
    "{color=#b7b7b7}Nell's idea, apparently. You went with them yesterday. It suits you, which is annoying.{/color}"
    "{color=#ff5fb8}Under your T-shirt your chest is tingling: two soft swells, puffy at the nipple, there when you look down. You cup one before you've thought about it, squeeze, and a hot little noise comes out of you.{/color}"
    si_harry "\"Swelling from the dye.\""
    "You tell the ceiling."
    show bg si_hall onlayer bgl
    show cg si_photo_wall onlayer cgl
    "On the way to the kitchen: the photo wall. You're in every picture. Fine. But your hair in all of them is long and red and loose, the way it's only been since yesterday."
    "A cold half-second where you know for a fact it hasn't always been like that."
    show si_paige warm at vn_cast_slot
    si_paige "\"Tea's up, trouble.\""
    "Paige comes past with two mugs. The half-second closes like a door. You take the strawberry mug. You don't think about the photos again."
    hide si_paige
    $ si_note_lines = [t for lv, t in si_notes(4)]
    show screen si_app(si_note_lines)
    "The tablet, face-up on the sofa arm, glowing pink."
    hide screen si_app
    hide cg onlayer cgl
    ## Sunday to Paige's office day, the Thursday after (the calendar, route.rpy)
    "{color=#b7b7b7}Days of the same. Your hair in your face every time you look down at the laptop. You've stopped tucking it back.{/color}\n{size=-5}{color=#ff8fa3}▸ Days of the same{/color}{/size}"
    $ vn_pass(4 * 1440)
    $ vn_set_time(9, 0)
    "{color=#b7b7b7}Paige has her office day. The flat's yours till lunch.{/color}\n{size=-5}{color=#ff8fa3}▸ Work from the sofa till lunch{/color}{/size}"
    $ vn_until(12)
    jump si_app_open

## ---- rung 4's waking day: the app, open (Sister App Open, App Tell, App Quiet) ----------------------------

label si_app_open:
    $ vn_enter(bg="si_lounge", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_app_open")
    show cg si_app_open onlayer cgl
    "Paige's office day, the one day a week she actually goes in. The flat's very quiet."
    "You're looking for your keys. That's the only reason you pick up the tablet, and it wakes in your hand."
    "It's open on a session log."
    $ si_note_lines = ["{b}Session log{/b}", "Movie Night (popcorn)", "Shared bath — full sync", "Chores (morning routine, new trait unlocked!)", "Brunch Test (friends present)", "Sisters' Day (salon, facials)", "{color=#b7b7b7}… and more below{/color}"]
    show screen si_app(si_note_lines)
    "The list runs off the bottom of the screen. Under it, a settings page, all toggles and pastel, with your name at the top."
    $ si_note_lines = ["{b}Settings{/b}", "Subject: verified. Legal adult.", "Ask before each session: OFF", "Auto-start: evenings", "Always been: ON", "Minimize attention: ON", "Body hair: PERM OFF", "Chest-finish preset: LATE", "Background Mode (beta): OFF"]
    show screen si_app(si_note_lines)
    "You stand there holding it a long time. Somewhere downstairs, somebody's telly laughs."
    "{i}Ask before each session: OFF.{/i} You read that line four times. You remember a film. You remember a lot of films."
    hide screen si_app
    menu:
        "You remember a lot of films."
        "“Paige. What is this.”":
            jump si_app_tell
        "Close it. Put it back.":
            jump si_app_quiet

label si_app_tell:
    $ vn_until(18)
    $ si.told = True
    $ si.consenting = True
    $ vn_enter(bg="si_kitchen", pc="puzzled", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_tell_table")
    show cg si_tell_table onlayer cgl
    "You wait for her at the kitchen table, the tablet between you, screen up."
    "She comes in with her bag on her shoulder and her keys in her teeth. Sees it. Stops in the doorway. Then she puts her bag down, sits across from you, and doesn't look away once."
    si_harry "\"Every evening. Isn't it.\""
    si_paige "\"Every evening.\""
    "She doesn't lie. That's what you'll keep coming back to. She doesn't try a single word of it on you."
    si_paige "\"You said ten minutes. On the sofa, as a joke. And after that I stopped asking.\""
    "She turns the tablet round and reads down the log like a shopping list: the film, the bath, the morning she put the rota up, the brunch, the salon."
    si_paige "\"You're Mae, in there. You're so happy. You've always been her, as far as she knows. I'm not going to delete it.\""
    "You sit there in her hoodie, red hair in your hands, waiting to be angry. It's there. It's just a long way off, behind something warmer: the strawberry mug, the braid, a rota on the fridge in a hand that's nearly yours."
    si_harry "\"Run it tonight.\""
    "She stares at you."
    si_harry "\"Run it tonight. I want her to have tonight. Don't you dare delete it.\""
    si_paige "\"I wasn't going to.\""
    "She makes you both tea, and puts yours in the strawberry mug without thinking. Neither of you says anything for a long time."
    hide cg onlayer cgl
    ## sitting with Paige (Sister Paige), once, awake, on the told path
    show bg si_lounge onlayer bgl
    "Floor, back against the sofa, her feet in your lap. Where you two have always talked, since the house share above the chip shop."
    si_paige "\"Tonight.\""
    "Eyes on the ceiling. Not a question."
    si_harry "\"Tonight.\""
    "She presses her heel against your knee, which is as close as sober Paige gets to holding your hand."
    jump si_evening

label si_app_quiet:
    $ vn_enter(bg="si_kitchen", pc="puzzled", pc_tag="si_pc", cast=[], cg=None)
    show bg si_kitchen onlayer bgl
    "You close it. You put it back on the arm of the sofa at exactly the angle it was at. It takes a second go."
    "Kettle on. You try to work out what you'd even say to her. You haven't got anything by the time her key's in the door, so you say nothing, and ask about Denise and the font."
    "{color=#b7b7b7}You know. She doesn't know you know. You'll keep it that way until you've worked out what to do.{/color}"
    "It lasts until about six."
    $ vn_until(18)
    jump si_cornering

## Quiet's six o'clock (Sister Session, rung 5, ch. 8): the one awake moment of force (revamp, 2026-10-20).
label si_cornering:
    $ vn_enter(bg="si_kitchen", pc="puzzled", pc_tag="si_pc", cast=[("si_paige", "wicked")], cg="si_fridge_corner")
    show cg si_fridge_corner onlayer cgl
    "She comes in at six with her bag on her shoulder and her keys in her teeth, and stops in the doorway, and looks at the tablet on the arm of the sofa."
    "At the angle. It took you two goes."
    si_paige "\"You looked.\""
    si_harry "\"Paige. I read it. Every evening. I never said you could—\""
    "She comes after you, not fast. You back up and up until your back finds the fridge, and the rota crackles under your shoulder blades."
    "She's a head taller than you and she's standing between you and the door, the tablet held against her chest like a clipboard."
    si_harry "\"Don't. I'm awake. Paige, I'm {i}awake{/i}, don't point that at—\""
    si_paige "\"I know. You said ten minutes.\""
    "She lifts it."
    si_paige "\"Ten minutes.\""
    "You grab for it. She holds it up over her head, easy, her other hand flat on your chest, keeping you against the fridge door. Not hard. She doesn't need hard."
    $ si_note_lines = ["Subject is AWAKE. Start session anyway?"]
    show screen si_app(si_note_lines)
    si_paige "\"Yes.\""
    "She tells it, looking right at you, and taps."
    hide screen si_app
    "The room skips, like a telly changing channel."
    $ si.mode = "mae"
    show cg si_fridge_hug onlayer cgl
    si_mae "\"Big sis! Why are we hugging the fridge? Is it a game? I {i}love{/i} this game!\""
    "Your arms go round her neck. You're squashed against the fridge with the magnets digging in, giggling."
    "Paige lets out a breath that's mostly a laugh and drops her forehead onto yours."
    si_paige "\"Hi, Mae.\""
    si_mae "\"Hi!\""
    "You kiss the end of her nose. You've never been happier to see anyone in your whole life. You never are."
    jump si_rung_five

## ---- rung 5: Mae invents (Sister Rung Five, Pride Sex/After, Pride Rota, Bra) -----------------------------

label si_rung_five:
    $ si_body(5)
    $ si_advance(5)
    $ si.mode = "mae"
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "warm")], cg="si_caught_up")
    show cg si_caught_up onlayer cgl
    if not si.told:
        "You skip back from the fridge to the sofa, towing big sis by the hand, magnets still printed on your back."
    "Before the film's even started you feel it: a weight, soft and new and swaying, every time you lean for the remote. You sit up. Both hands over your top. Squeeze. Gasp. Look down."
    si_mae "\"Big sis. Big sis. {i}Look.{/i}\""
    "Top up, obviously. There they are. Proper breasts, full and round and heavy in your hands, nipples pink and stiff, and you jiggle them at her, laughing, because you can."
    si_mae "\"I caught up! We match now! C. I'm a C. Same as you.\""
    si_mae "\"{i}Ohh{/i}— they're so {i}heavy{/i}— {i}mmh{/i}— big sis, feel how heavy— no, {i}feel{/i}—\""
    "You squeeze them together and moan, loud, right there on the sofa. Your bum's rounder under you too, sunk deep in the cushion."
    si_paige "\"You're— Mae, they're—\""
    "She keeps looking at your face, carefully, like she's checking for something. There's just you, grinning, with your top round your armpits."
    si_mae "\"Perfect. I know.\""
    "Then the best idea you've ever had, and you sit up straight with it."
    si_mae "\"Wait. Wait. Big sis. You've got the morning problem.\""
    si_paige "\"It's the middle of the evening.\""
    si_mae "\"Morning problems don't check the clock.\""
    "Your hand goes flat on the front of her joggers, where she very definitely has one."
    si_mae "\"And now {i}I've{/i} got these. So that's both problems. Both morning problems. And one solution. Efficiency!\""
    show cg si_pride_open onlayer cgl
    "You slide off the sofa onto your knees between her legs. Joggers down. Her cock springs out heavy and hot. You lean in and fold your breasts round it, and it's so warm and so big between them that you both say \"{i}oh{/i}\" at once."
    si_paige "\"Who taught you that?\""
    si_mae "\"Nobody! I {i}invented{/i} it!\""
    vn_sfx "Fwp. Fwp. Fwp."
    "Up and down, slow, squeezing tight on the way up, loose on the way down, like your hands already knew. The head pokes out of your cleavage and bumps your chin. You giggle and lick it."
    si_mae "\"Look, look, it fits, it fits perfectly, like they were made for— {i}mm{/i}— big sis, you're so hard, you're {i}so{/i} hard— tell me when, tell me, {i}please{/i}, I want to see—\""
    si_paige "\"{i}Mae{/i}—\""
    show cg si_pride_cum onlayer cgl
    "She comes all over your chest, hot thick ropes across your new breasts, up your throat, over your chin. You squeal and keep pumping till she's shaking and pushing at your shoulders." with vnfx("flash")
    si_mae "\"Both problems. Solved.\""
    "Then you go and get the green pen out of the kitchen drawer, because you're writing this one up yourself."
    menu:
        "The green pen."
        "Again, to be sure":
            jump si_pride_sex
        "Write it on the rota":
            jump si_pride_rota

label si_pride_after:
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[], cg=None)
    show bg si_lounge onlayer bgl
    if si_enc.partner_came:
        "The second time, big sis comes with her hands buried in your red hair and your name coming out of her in pieces. It ends up everywhere again. You're delighted about every bit of it."
    else:
        "Big sis stops you in the end with her hands cupping your face, laughing, wrecked, saying you're going to kill her."
    jump si_pride_rota

label si_pride_rota:
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_green_pen")
    show cg si_green_pen onlayer cgl
    show screen si_rota
    "Green pen, big letters, at the bottom of the rota under your {i}braid Sunday?{/i}: {i}Big sister's pride (Mae's idea){/i}."
    "You tick it. You initial it yourself. {i}M.{/i} It's the best line on the whole fridge, and you tell big sis so."
    si_paige "\"It's your idea. It says so.\""
    si_mae "\"It's {i}my idea{/i}.\""
    "You'll bring it up constantly, for years."
    hide screen si_rota
    call si_chore_offer
    call si_bedtime
    jump si_bra

label si_bra:
    $ si.mode = "waking"
    $ vn_enter(bg="si_bedroom", pc="puzzled", pc_tag="si_pc", cast=[], cg="si_wake_breasts")
    show cg si_wake_breasts onlayer cgl
    "You wake up with breasts. Not a figure of speech. Full, heavy, soft, a real weight when you sit up, and your T-shirt has given up."
    "Your hair's past your shoulders now. It was at them a week ago. Nobody says a word about it, so neither do you."
    "You grab them before you've decided to. They spill over your hands. Your thumbs drag across your nipples and your hips jerk up off the mattress, and the noise you make is high and wet and long."
    "You do it again. You don't get up for a while."
    "{color=#b7b7b7}Water retention, you tell the mirror.{/color}"
    show cg si_bra_shop onlayer cgl
    "You need a bra. Lunchtime, the department store on the high street. You say \"C\" before the woman at the counter can even reach for anything, like your shoe size."
    "Your voice has gone up, too. Light and soft, all day, in meetings, on the phone. It won't come back down."
    "{color=#b7b7b7}You're coming down with something.{/color}"
    hide cg onlayer cgl
    show bg si_kitchen onlayer bgl
    show si_paige soft at vn_cast_slot
    if si.told:
        "Paige watches you over her mug at breakfast, asks if you're okay, and means it. You are. You tell her so."
    else:
        "Paige watches you over her mug at breakfast. You keep your own counsel. You have for a while."
    hide si_paige
    $ si_note_lines = [t for lv, t in si_notes(5)]
    show screen si_app(si_note_lines)
    "On the fridge, in green pen, in a round loopy hand that's almost yours: {i}Big sister's pride (Mae's idea){/i}. The tablet glows beside it."
    hide screen si_app
    $ si.consenting = True
    jump si_evening

## ---- rung 6: Mae runs it (Sister Rung Six, Pace, Pace Sex/After, Harry Hour) ----------------------------

label si_rung_six:
    $ si_advance(6)
    $ si.mode = "mae"
    $ vn_enter(bg="si_lounge", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_bgmode")
    show cg si_bgmode onlayer cgl
    "Mid-film the tablet chimes, a new, brighter chime, and big sis picks it up and goes still."
    $ si_note_lines = ["Version 1.4 — Background Mode (beta)! Tired of toggling? Activate continuous operation for seamless little-sister support, with a scheduled legacy interval. User feedback: “It's like real family!” Accept? Decline?"]
    show screen si_app(si_note_lines)
    "You read it over her shoulder, chin on her arm."
    si_mae "\"Always on? Is that what it says? Always?\""
    si_paige "\"Mae. Sweetheart. It means you'd be—\""
    si_mae "\"Say yes! Say yes, big sis. Always! Why wouldn't you?\""
    "You bounce on the cushion. She looks at you a long time. Her thumb hovers. You can see her thinking about the bins and the kettle and the rota and the corner-shop man, and not finding one thing in any of it she'd rather have back."
    "She taps {color=#ff8fd0}Accept{/color}."
    $ si_note_lines = ["Background Mode ENABLED — session default: Mae. “Sister support always on!” Legacy interval scheduled. Enjoy Imouto+."]
    show screen si_app(si_note_lines)
    "The tablet goes quiet in her lap."
    hide screen si_app
    show cg si_rota_copy onlayer cgl
    "Then she goes to the fridge, takes the pen off its string, and writes one line on the rota in her own hand. {i}[si_pc_name] hour, Sunday mornings.{/i}"
    "That's all. That night, while she's in the shower, you take the whole rota down and copy it out fresh in your round loopy hand, every line, every tick, every set of initials, so it's neat."
    show screen si_rota
    "All of it's yours now except that one line. You copy it too, but you tape her original to the bottom, because it's hers."
    hide screen si_rota
    "Your work emails have started saying {i}remote{/i} in the subject line. You don't remember asking. Big sis says you asked.\n{size=-5}{color=#ff8fa3}▸ “My turn. I'm setting the pace.”{/color}{/size}"
    jump si_pace

label si_pace:
    $ si.fit = "skirt"
    $ vn_enter(bg="si_lounge", pc="eager", pc_tag="si_pc", cast=[], cg="si_pace_climb")
    show cg si_pace_climb onlayer cgl
    si_mae "\"Lie back. Lie back, big sis. I'm setting the pace.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Are you?\""
    "She's grinning. She lies back along the sofa anyway, head on the arm, hands behind her head like she's on holiday, and lets you climb on."
    $ si_body(6)
    "{color=#ff5fb8}Skirt rucked up, knees sunk in the cushions. Your thighs have gone thick and soft and spread over her hips like they were made to. Down between your legs there's barely anything of your cock left, the merest soft little nub, and neither of you looks. Attention successfully minimized.{/color}"
    "You grab your breasts on the way down. Bigger again. They spill out of your hands, a DD now, easy, and so sensitive you squeal."
    si_mae "\"Big sis, they're {i}bigger{/i}— look, look, they don't {i}fit{/i}—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"I noticed.\""
    "Strangled, and she doesn't look anywhere else."
    show cg si_pace_sit onlayer cgl
    "You reach back, find her cock, slick from the bottle on the bookcase, line it up, and sit."
    si_mae "\"{i}Ohhh{/i}— oh, big sis, oh, it's so— hold on, hold on, I'm doing it, {i}I'm{/i} doing it—\""
    "Slow. All the way down, hands braced on her stomach, mouth hanging open, until you're sitting right on her, full to the brim. You wiggle. Big sis swears."
    si_mae "\"Don't move. You're not allowed to move. I'm setting the pace.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"I'm not moving. I'm absolutely not moving.\""
    vn_sfx "Pap. Pap. Pap."
    show cg si_pace_ride onlayer cgl
    "Up, and down. Slow and rolling, grinding on the way down, obscene, and you don't care at all. Your hips know the rhythm before you do: roll, grind, squeeze. Nobody taught you that."
    si_mae "\"Look at me, look at me, big sis, look at me {i}riding{/i} you, I'm so good at this, I'm {i}so good{/i} at this—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"You're so good at this.\""
    "Helplessly, and she grabs your hips. You smack her hands away."
    si_mae "\"{i}Pace!{/i}\""
    show cg si_pace_cum onlayer cgl
    "She laughs so hard she nearly falls off the sofa. You keep going till your thighs shake and you're screaming her name at the ceiling, and you come with her buried in you, clenching round her, wailing with it. She comes right after, hot and deep." with vnfx("flash")
    si_mae "\"Pace.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Pace.\""
    "She's still hard. You lift up off her, slick and shaking, and hover there with the head of her nudging you, deciding."
    menu:
        "Deciding."
        "Again, slower":
            jump si_pace_sex
        "Stay on her chest":
            jump si_pace_close

label si_pace_after:
    $ vn_enter(bg="si_lounge", pc="blissful", pc_tag="si_pc", cast=[], cg=None)
    show bg si_lounge onlayer bgl
    if si_enc.partner_came:
        "\"Slower\" lasts about a minute before you forget all about it. Big sis comes inside you again with her head thrown back over the arm of the sofa, and you tell her she's not allowed to do that without permission, and then give it."
    else:
        "You ride her until you can't, then flop down onto her chest. She strokes your hair and tells you you're the best at pace anyone has ever been."
    jump si_pace_close

label si_pace_close:
    $ vn_enter(bg="si_lounge", pc="blissful", pc_tag="si_pc", cast=[("si_paige", "soft")], cg=None)
    show bg si_lounge onlayer bgl
    call si_chore_offer
    $ vn_enter(bg="si_hall", pc="blissful", pc_tag="si_pc", cast=[("si_paige", "soft")], cg=None)
    show bg si_hall onlayer bgl
    si_bigsis "\"Bedtime. Sleep tight, trouble.\""
    "She kisses the top of your head on the way past."
    si_mae "\"'Night, big sis!\""
    "There's nothing to tap any more. It's just bedtime."
    "{color=#b7b7b7}The days run together, the way good days do. Sunday comes round.{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide si_paige
    ## the days run together: the Sunday after next (the calendar, route.rpy)
    $ vn_pass(8 * 1440)
    call vn_night(8)
    jump si_harry_hour

label si_harry_hour:
    $ si.fit = None
    $ vn_enter(bg="si_hall", pc="eager", pc_tag="si_pc", cast=[("si_paige", "warm")], cg="si_foot_tap")
    show cg si_foot_tap onlayer cgl
    "Sunday. Bottom of the rota, in big sis's handwriting: {i}[si_pc_name] hour, Sunday mornings{/i}."
    si_mae "\"Do I {i}have{/i} to?\""
    "Over your tea."
    si_paige "\"One hour. The tenancy won't sign itself, trouble.\""
    "So you sit on the hall floor outside the study door with your tea and your phone, timer set, and tap your foot. You tap it the whole time she's finding the tablet. You tap it {i}at{/i} her."
    "She taps the screen. {=si_hypno}{i}Skip.{/i}{/=si_hypno}"
    $ si.mode = "waking"
    show bg si_study onlayer bgl
    show cg si_study_desk onlayer cgl
    "You're on the hall floor outside the study with a cup of tea, tapping your foot. You stop. You go in and sit at the desk."
    "Paperwork. The tenancy renewal, a bank letter, a form from work moving your contract to remote that you don't remember asking for, a council tax letter addressed to {i}The Occupants{/i}."
    "You sign the tenancy. The first letter comes out as a loopy M. You cross it out and sign again, carefully."
    "Your foot's tapping. You stop it. It starts again. It taps the whole hour under the desk, like it's waiting for something."
    "You lean in to sign and your breasts press heavy against the edge of the desk, your nipples dragging on the wood. You go very still. Hot. You have to wait a whole minute before you can pick the pen back up."
    "A sticky note on the monitor in your own round loopy hand: {i}hurry up x{/i}"
    "{color=#b7b7b7}You must have written it last week. You don't remember last week.{/color}"
    si_paige "\"Done?\""
    "Her head round the door, when the hour's up."
    si_harry "\"Done.\""
    "It comes out high and soft, and you don't even notice."
    "{=si_hypno}{i}Skip.{/i}{/=si_hypno}"
    $ si.mode = "mae"
    si_mae "\"Big sis! Were you lonely without me?\""
    "You launch yourself out of the chair at her."
    si_paige "\"Desperately.\""
    "And she catches you.\n{size=-5}{color=#ff8fa3}▸ The week goes by; Sunday again{/color}{/size}"
    $ vn_pass(6 * 1440)
    call vn_night(8)
    jump si_rung_seven

## ---- rung 7: nothing toggles back (Sister Rung Seven, Check Together, All The Way After, Crossed Out) -----

label si_rung_seven:
    $ si.mode = "mae"
    $ vn_enter(bg="si_hall", pc="eager", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_no_skip")
    show cg si_no_skip onlayer cgl
    "Sunday. Bottom of the rota, in big sis's handwriting: {i}[si_pc_name] hour, Sunday mornings{/i}."
    "You sit outside the study with your tea, phone on your knee, timer set, tapping your foot at her while she finds the tablet. She taps the screen."
    "You wait for the skip. It doesn't come."
    "She taps again. You're still on the hall floor with your tea, being you, and you're Mae, and there's nothing behind the study door but paperwork."
    si_mae "\"Big sis?\""
    si_paige "\"Hang on. It's— it says—\""
    "Another tap. Her face does something complicated."
    "No edge. No click. No skip, no {i}up you come{/i}. The morning just keeps being the morning. You're yourself, and yourself is Mae, and there's no second place to be."
    "You put your tea down on the carpet."
    $ si_body(7)
    $ si_advance(7)
    show cg si_shift onlayer cgl
    "{color=#ff5fb8}Heat between your legs. New. Not the minimized nothing that's been there for weeks, but something warm and full and alive, soft and slick and {i}there{/i}. You shift on the carpet, it moves with you, and you gasp.{/color}" with vnfx("shake")
    "{color=#ff5fb8}And it doesn't stop there. Your top goes tight, then tighter, your breasts swelling heavy and round until the hem rides up over them. Your hips push out. Your bum spreads under you on the carpet, fat and soft. Red hair slides down your back past your waist.{/color}"
    si_mae "\"Big sis— big sis, they're— they're {i}huge{/i}— oh, {i}oh{/i}, they're bigger than {i}yours{/i}—\""
    "You grab your breasts with both hands and they spill everywhere, way past a C, past a DD, a G at least. You squeeze and moan so loud it echoes down the hall."
    "Big sis is kneeling in front of you before you've finished gasping. Her hands are on your knees, very still."
    si_paige "\"Do you want to check? Together?\""
    "Barely out loud. You nod, once, eyes enormous.\n{size=-5}{color=#ff8fa3}▸ Check together{/color}{/size}"
    jump si_check_together

label si_check_together:
    $ si.fit = "nude"
    $ vn_enter(bg="si_paige_room", pc="eager", pc_tag="si_pc", cast=[], cg="si_check_carry")
    show cg si_check_carry onlayer cgl
    "She carries you into her bedroom. Actually carries you, scooped off the hall carpet like nothing. You shriek, then laugh, then go quiet, because she's set you on the edge of her bed and knelt between your knees, and her hands are shaking."
    show cg si_check_see onlayer cgl
    "Thumbs in your sleep shorts. She eases them down your thighs. You lift your hips to help."
    "Nothing left of it at all. No nub to step round. Just you: a soft, smooth, pink fold between your thighs, plump and already wet, opening a little when your knees fall apart. You both stare. You both breathe."
    show si_paige warm at vn_cast_slot
    si_paige "\"Can I—?\""
    si_mae "\"You're my big sis. Who else? {i}Please.{/i}\""
    show cg si_check_touch onlayer cgl
    "Her fingers, so careful. The outside first, tracing, like she's learning a map. Then between, sliding through how wet you are, and up, and her thumb finds a sweet hard point that sends a bolt straight up into your chest."
    si_mae "\"{i}Oh{/i}— oh, big sis, oh, that's— that's new, that's so— do that again, do it again—\""
    "She does it again. And again, until you're fisting the duvet, hips rocking up into her hand, talking non-stop, high and broken. Then one finger slides inside you, slow, and you go completely silent for the first time in your life. Then very, very loud."
    show si_paige warm at vn_cast_slot
    si_paige "\"I love you. You know that, right? I love you so much.\""
    si_mae "\"Love you too. {i}Don't stop.{/i}\""
    "She stands and pulls her T-shirt off. Her cock's so hard it's dripping. She climbs over you, and you open your legs wide without being asked, pulling at her shoulders, and the head of her cock slides through your wet and comes to rest right at you. And holds."
    show si_paige warm at vn_cast_slot
    si_paige "\"Careful. We'll go careful.\"\n{size=-5}{color=#ff8fa3}▸ Pull her down into you{/color}{/size}"
    jump si_allway_sex

label si_allway_after:
    $ vn_enter(bg="si_paige_room", pc="blissful", pc_tag="si_pc", cast=[], cg="si_allway_ride")
    show cg si_allway_ride onlayer cgl
    "Neither of you moves for a while. Her weight on you, your whole new body humming. She kisses your face all over: cheeks, eyelids, the corners of your mouth."
    "She rolls off onto her back, gasping. You don't let her get far."
    si_mae "\"My turn.\""
    "And you climb on."
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae, I can't—\""
    si_mae "\"You {i}can{/i}. Oh— oh, that's so much {i}better{/i} like this— look at me, big sis, look, I'm doing it, I'm riding you with my— with my {i}new{/i}—\""
    "She's still hard. Of course she is. You sink down onto all of her, slow, and the noise you make shuts the downstairs telly up for a second."
    show si_paige warm at vn_cast_slot
    si_paige "\"I'm looking. Believe me, I'm looking.\""
    show cg si_allway_ride_cum onlayer cgl
    "You ride her till your thighs give out, bouncing, grinding, breasts everywhere, red hair stuck to your face, your new hips finding the rhythm the very first time, like they always knew it. You come again, clenching so hard she swears." with vnfx("flash")
    "Then you fall forward onto her chest, and she wraps both arms round you, and you lie there sticky and gasping while the Sunday goes on outside without you."
    si_mae "\"Best one. Put it at the top of the rota.\""
    "With total serenity. She laughs so hard the bed shakes.\n{size=-5}{color=#ff8fa3}▸ That afternoon{/color}{/size}"
    jump si_crossed_out

label si_crossed_out:
    $ si.fit = None
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[], cg="si_cross_out")
    show cg si_cross_out onlayer cgl
    show screen si_rota
    "That afternoon you stand at the fridge in big sis's hoodie, looking at the rota. Every line of it is yours. All but the bottom line, in her hand, taped on: {i}[si_pc_name] hour, Sunday mornings{/i}."
    "You take the pen off its string and draw one neat line through it."
    $ si.harry_struck = True
    "It looks finished. Like a list somebody's done."
    si_mae "\"We don't need it.\""
    "You decide it out loud. You take the whole rota down, fold it in half, and put it in the kitchen drawer with the takeaway menus."
    hide screen si_rota
    $ si.rota_down = True
    si_mae "\"We know what the evenings are for.\""
    show si_paige soft at vn_cast_slot
    if si.told:
        "Big sis is in the doorway. She's looking at the clean rectangle on the fridge door, then at you."
        si_paige "\"I'm not going to undo it. Even now. I wanted you to know that.\""
        si_mae "\"I know.\""
        "That's all. You put the kettle on. She gets the mugs down and puts yours in front of you, the strawberry one, and neither of you says anything else about it, then or ever."
    else:
        "Big sis is in the doorway, looking at the clean rectangle on the fridge door."
        si_paige "\"Mae. I want to say it. All of it. Out loud, once.\""
        "So you listen. Everything, in completely the wrong order, arms folded in the kitchen doorway: the app, the night on the sofa, the ten minutes she never ended. How she never asked again after that, not once, not one evening."
        "The patch. The night you looked, and she backed you into this fridge and tapped Start anyway. The night she pressed Accept. She doesn't say sorry. She says she'd do every bit of it again. She says she wanted you to hear her say it."
        "You let her get to the end. Then you laugh. You can't help it. You laugh until you have to hold the counter."
        si_mae "\"Big sis. You are {i}so{/i} dramatic.\""
        si_paige "\"I'm—\""
        si_mae "\"Asking's for {i}guests{/i}. Sit down. You're making the kitchen sad.\""
        "Kettle on. The strawberry mug and the blue one with the chipped handle, honey from behind the oats. She sits. Tea, extra sweet, the way she likes it on bad days."
        si_mae "\"The fridge was {i}fun{/i}. I came out hugging you. Drink your tea.\""
        "She drinks her tea."
    hide si_paige
    "\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump si_before_the_flat

label si_before_the_flat:
    $ vn_enter(bg="si_paige_room", pc="blissful", pc_tag="si_pc", cast=[], cg="si_before_flat")
    show cg si_before_flat onlayer cgl
    "You wake slowly, warm, sun on the duvet, big sis's arm over your waist."
    "Something settles while you lie there. Gently, all the way."
    "You remember being Mae. All of it: the sofa, the tea, the bath nights, the rota, Nell's purple napkin, big sis's braid."
    "And you remember the other one. He hasn't gone anywhere. He's filed, like anything you've grown out of: soft and out of focus, the before-the-flat years, the way anyone's early twenties are."
    "Quieter. Duller round the edges, in hoodies, wearing your face a bit badly. You're quite fond of him, actually. He made very good toast."
    "It all makes perfect sense. You stretch until your toes crack."
    $ si_note_lines = [t for lv, t in si_notes(7)][:2]
    show screen si_app(si_note_lines)
    "Big sis's phone lights up on the bedside table."
    si_mae "\"See? Now everything matches.\""
    "You whisper it, so you don't wake her."
    hide screen si_app
    "\n{size=-5}{color=#ff8fa3}▸ Get up and put the kettle on{/color}{/size}"
    jump si_framed

label si_framed:
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_frame")
    show cg si_frame onlayer cgl
    $ si_note_lines = ["SISTER LEVEL: MAX. No further sessions required."]
    show screen si_app(si_note_lines)
    "The last notification comes while the kettle's boiling."
    "You screenshot it, print it on big sis's wheezy printer in the study, put it in a charity-shop frame from the hall drawer, and hang it on the fridge with the chip-shop magnet, right where the rota hung."
    hide screen si_app
    $ si.framed = True
    "Big sis stands in front of it with her coffee for a long time."
    si_paige "\"Everybody's going to have to be shown that.\""
    si_mae "\"Every single person.\""
    "Which leaves the app itself, second row of her home screen, nothing left in it to do. She gets her phone out. She doesn't ask. She taps the rabbit."
    $ si_note_lines = ["Sister Level MAX reached! What would you like to do?"]
    show screen si_app(si_note_lines)
    si_paige "\"Two taps. One each. I'll do this one.\""
    "She taps through to the choice and holds the phone out to you, so the second tap is yours."
    hide screen si_app
    menu:
        "The second tap is yours."
        "Keep it" (ending=True):
            jump si_end_bond
        "Delete it" (ending=True):
            jump si_end_delete

label si_end_bond:
    $ si.ending = "bond"
    $ achievement.grant("Sister Level MAX")
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_keep")
    show cg si_keep onlayer cgl
    "You tap {color=#ff8fd0}Keep{/color}."
    $ si_note_lines = ["Thank you for choosing Imouto+! Family is what you make together."]
    show screen si_app(si_note_lines)
    "It stays on her home screen, second row, between the bank and the one that tells you which bin it is."
    hide screen si_app
    "Nobody opens it. There's nothing left in it: no sessions, no traits, just a completion screen and a pink rabbit and a cheerful line about family."
    "You like knowing it's there. Something about the receipt. Something about all of it having been done on purpose, by somebody who wanted you."
    "{color=#7fd17f}Sunday mornings are brunch now. Bath night is Thursday. The bins are still, after all this time, an ongoing argument.{/color}\n{size=-5}{color=#ff8fa3}▸ Brunch{/color}{/size}"
    jump si_epilogue

label si_end_delete:
    $ si.ending = "delete"
    $ achievement.grant("Unbreakable Bond")
    $ vn_enter(bg="si_kitchen", pc="beaming", pc_tag="si_pc", cast=[("si_paige", "soft")], cg="si_delete")
    show cg si_delete onlayer cgl
    "You tap {color=#ff8fd0}Delete{/color}."
    $ si_note_lines = ["Are you sure? This action cannot be undone."]
    show screen si_app(si_note_lines)
    si_mae "\"Yes.\""
    "You tell it, out loud, and tap that too, and grin up at big sis."
    hide screen si_app
    "Gone. You both sit at the kitchen table a moment, waiting for something. Nothing happens at all."
    "You make the tea, because you always make the tea. Strawberry mug, feet tucked under you, and you ask your big sis about Denise and the font."
    "{color=#b7b7b7}Nothing was holding it in place. Nothing has been for months. The app was a ladder, and you've been standing on the roof for a while.{/color}\n{size=-5}{color=#ff8fa3}▸ Brunch{/color}{/size}"
    jump si_epilogue

label si_epilogue:
    $ vn_enter(bg="si_cafe", pc="beaming", pc_tag="si_pc", cast=[], cg="si_epi_brunch")
    show cg si_epi_brunch onlayer cgl
    "The bakery with the blue awning keeps the big window table for you on Sundays now, without being asked."
    "The witnesses are insufferable. Natalie has renamed the group chat {i}Witnesses (Retired){/i} and is pretending to be sad about it. Nell wants to hear you say what's in the frame on your fridge, though she's seen it."
    "Amber has another gift bag, and this time Paige lets you have it. You peek inside under the table, shut it very fast, go pink, and the whole table shrieks."
    show si_kate smile at vn_cast_slot
    si_kate "\"So. How've you been sleeping?\""
    si_mae "\"Like a log.\""
    "She smiles at you slowly, the way she did that first morning, like she's known you for years."
    si_kate "\"And the app?\""
    if si.ending == "delete":
        si_mae "\"Gone. Didn't need it.\""
        si_kate "\"No. I don't suppose you did.\""
    else:
        si_mae "\"Still there. Second row. Between the bank and the bins.\""
        si_kate "\"Very sensible.\""
        "Which it is."
    hide si_kate
    show cg si_epi_shop onlayer cgl
    "On the way home you stick your head into the corner shop, because you always forget the milk. The man behind the counter looks up from his paper the way he has for a year and a half, and nods at the pair of you."
    si_shop "\"Morning, girls.\""
    "He's never once been wrong.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump si_route_return
