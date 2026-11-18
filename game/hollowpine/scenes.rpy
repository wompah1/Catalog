## hollowpine's treatments: one a day, each a sex act under a wellness name. IT'S ON THE CARD: every
## day it goes one step past what he thought he booked, he says no, and the staff and the women carry
## on, honest and unbothered, because it's the treatment. The choice when he protests is what he
## says, never whether. Days 1-3 non-con, no flip; day 4 breaks into begging; day 5 non-con, then the
## walk-out (script.rpy) is the flip; day 6 consensual. No tears, no menace, no pain, no escape.
## Production rewrite (2026-11-13, twinetesting-c9): every treatment run long from the book, a
## picture per beat; the choices that carry: hyd2 (day 2 -> day 3), the rest in script.rpy.

## ---- DAY 1: Silt Soak + Lymphatic Drainage. A bored technician's hand ---------------------------
label hol_drainage:
    $ vn_enter(bg="hol_pool", pc="earnest", pc_tag="hol_pc", cast=[], cg="hol_silt")
    "The silt soak is a warm grey pool that smells of wet stone, in a room of pale wood and steam. A blonde technician with a tablet and a badge reading RENEE checks you in."
    hol_renee "\"Ellie Vance? Full soak scheduled. Relax, let the silt do the work. I'll check on you in half an hour.\""
    show cg hol_silt_float onlayer cgl
    "You lie in it to your chin, the silt warm and heavy as a blanket, and feel very mature about the whole thing. It tingles. Everywhere. You assume that's the minerals."
    "Through the steam you can hear the others in the next pool, laughing about something. Casey's laugh, mostly. You float and listen to it and feel lucky."
    "Afterwards Renee towels you off, almost automatic, the way you'd dry a dish."
    hol_renee "\"Next is drainage, correct? Suite B, just follow the sign.\""
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_tech", "bored")], cg="hol_table")
    "Then the treatment room. A padded table, a folded towel over your hips, soft music, a lamp. A technician in a white tunic, FOX on her badge, who looks at you like you're the fourth of the afternoon."
    hol_tech "\"Ellie, you're set for a full lymphatic drainage this evening? Lie back, ma'am.\""
    "She snaps her gloves on and reads the protocol off the card, eyes flicking up and down it."
    hol_tech "\"Standard protocol: focused manual drainage. You may feel some internal pressure and extended sensitivity. There's an analysis sample at the end, all properly labelled and logged.\""
    hol_you "\"Great. Lovely. I'm very ready to be drained.\""
    show cg hol_calves onlayer cgl
    "Her hands start at your ankles. Long firm oiled strokes up your calves, over your knees, up your thighs. It's a massage. It's a nice massage. You narrate it to yourself like a procedure: drainage, upward, towards the heart."
    "Your thighs, though. Her thumbs press up the insides of them, slow, all the way to the edge of the towel and back, and back again, and something about the silt has made everything very, very sensitive."
    hol_you "\"That's— the minerals are really— that's very effective—\""
    hol_tech "\"Mm-hm.\""
    show cg hol_towel onlayer cgl
    "Then her hand goes under the towel."
    $ hol.said_no += 1
    show hol_pc flustered
    hol_you "\"Whoa— no— no, sorry, that's— I think there's been a mix-up, I booked the drainage—\""
    hol_tech "\"This is the drainage, ma'am. Below the waist. It's on the card.\""
    "She doesn't look up. Her hand closes round your cock and starts to stroke, slow and businesslike, the way you'd wring out a cloth."
    vn_sfx "{i}Shlk. Shlk. Shlk.{/i}"
    menu:
        "Her hand doesn't stop."
        "Explain it clinically":
            $ hol.shout1 = "clinical"
            hol_you "\"Right— but medically— nnh— medically that's not lymphatic, the lymph nodes are in the— {i}hah{/i}— no, stop, that's not—\""
            hol_tech "\"Inguinal, ma'am. Right here.\""
            "She taps the crease of your thigh with one gloved finger, without letting go of you, like a teacher with a pointer."
        "Grab the edge of the table":
            $ hol.shout1 = "table"
            "You grab the edge of the table to sit up. Your arms don't. Your hips lift instead, right into her fist."
            hol_you "\"Stop— please— I didn't— I didn't mean THIS—\""
            hol_tech "\"Hips down, please, ma'am.\""
    show cg hol_drain_stroke onlayer cgl
    "Her other hand cups your balls, gloved and warm, and rolls them, and she works you root to tip with a twist at the head that she must do forty times a day, because it's perfect, because it's procedure."
    hol_tech "\"You're responding very well, ma'am. Let's take a pause. I need a clean sample, not a mess on the sheet. Keep your hips down.\""
    "She stops with her fist round the base of you, squeezing, and you hang there on the edge of it with your mouth open."
    "You are responding. That's the worst part. You're hard as a rail in a stranger's hand and your thighs are falling open on the table without asking you."
    hol_you "\"Please don't— don't start again— I'm asking you not to—\""
    "She starts again."
    show cg hol_intercom onlayer cgl
    "The wall intercom crackles: \"Fox, linen request for Chamber Five and a double lunch order, please confirm.\""
    hol_tech "\"Chamber Five, acknowledged. Lunch double, that's for Delaney's group, right? I'll ring it in.\""
    "She leans over to press the button with her elbow. She doesn't let go of you to say it. Nobody in the hall sounds remotely bothered by anything."
    vn_sfx "{i}Shlk-shlk-shlk.{/i}"
    hol_you "\"Fox— Fox, I'm going to— please, I don't want to— not like this— not in a {i}dish—{/i}\""
    hol_tech "\"Nearly there, ma'am.\""
    show cg hol_drain_peak onlayer cgl
    hol_you "\"No— no, no— {i}ohh{/i}— it's not— don't— don't sto— no— I mean STOP—!\"" with vnfx("shake")
    "She speeds up exactly the right amount, bored, and your back comes off the table."
    hol_you "\"{i}Ahh{/i}— please— please— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg hol_dish onlayer cgl
    vn_sfx "{i}Splurt. Splurt. Splurt.{/i}"
    "You come in long hot pulses, shouting at the ceiling, and she catches all of it in a small glass dish without looking, and milks the last of it out with two fingers, and covers it with a lid."
    show cg hol_sample onlayer cgl
    "Then she writes on a sticky label, ELLIE V, and the date, and sticks it on the lid, and puts the dish in a small fridge under the counter with a lot of other dishes."
    hol_tech "\"Excellent retention, nice volume. All collected and sampled for analysis. If you want to accelerate absorption rates, you can upgrade at the desk any time for enhanced protocols.\""
    hol_you "\"...Right. Yes. A sample.\""
    "Obviously a sample. You lie there panting with the towel on the floor and feel, on balance, quite mature about the whole thing."
    hide cg onlayer cgl
    $ hol.fit = "robe"
    jump hol_day_one_after

## ---- DAY 2: Hydration Therapy. Oral, three times, on Delaney ------------------------------------
label hol_hydration:
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_hydrate_1")
    "Hydration therapy is Delaney, in Chamber Four, looking up from her phone, legs spread, her robe open."
    hol_delaney "\"Hey, hydrating partner. This is your package upgrade, right? I got the ping. C'mere. You'll like this one.\""
    "Her cock is very large. You'd noticed. Everybody's noticed. It lies along her thigh like it's waiting for a bus. She sits on the edge of the table and lets you work out the delivery method for yourself."
    show cg hol_hydrate_kneel onlayer cgl
    "You get on your knees on the mat. You come up barely level with her navel. You look at it for a while."
    hol_you "\"Okay. I just— what do I do?\""
    hol_delaney "\"Just open up, babe. And don't spill anything. That's enzyme for your metrics.\""
    menu:
        "Hydration therapy, session one."
        "Ask how far it's meant to go":
            $ hol.hyd2 = "ask"
            hol_you "\"How far is it meant to— is there a depth on the protocol?\""
            hol_delaney "\"As far as you can, Ellie. Ambition's good for the numbers.\""
        "Just go for it":
            $ hol.hyd2 = "go"
            "You read the card twice. You're not going to look stupid now. You take a breath and go for it."
    "You get your mouth round the head of her, which takes your whole mouth, and then a bit more of her, and her hand comes to rest on your hair like she's reading in a library."
    vn_sfx "{i}Shlp. Shlp.{/i}"
    hol_delaney "\"There you go. Tongue under. Good. You're a natural, Ellie.\""
    "You're diligent. You do your best. You keep your lips over your teeth the way you've seen it done in films, and work your hand on what doesn't fit, and listen to her breathing for feedback, like it's a driving test."
    show cg hol_hydrate_swallow onlayer cgl
    hol_delaney "\"Here it comes. Swallow, babe. All of it.\""
    "You swallow, because that's oral administration, and you're chasing the number. There's a lot. You swallow and swallow, and when she's done you sit back on your heels and wipe your chin and feel like you've passed something."
    hol_delaney "\"Good session. That'll bump your numbers. Give it ten minutes, sweet stuff. Skin'll thank you.\""
    "It's the first time you've been on your knees for anyone, and you're quite proud of your session count."
    hide cg onlayer cgl
    $ vn_pass(180)
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_hydrate_2")
    "Second session before lunch. She's on her phone again. You get on your knees without being asked, which you feel shows initiative, and take her in your mouth, and she scrolls with one hand and pets you with the other."
    hol_delaney "\"Mm. Better. You've been practising?\""
    hol_you "\"{i}Mmh.{/i} In my head.\""
    "You swallow. You go to lunch. You have the soup, because hydration."
    $ vn_until(18)
    $ vn_enter(bg="hol_treatment", pc="flustered", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_hydrate_3")
    "The third, before dinner. Your jaw's had it. Your knees have had it. You get down in front of her and you can't."
    $ hol.said_no += 1
    hol_you "\"Actually— I think I'll skip this one. I'm quite hydrated. I'm very hydrated. I'm basically a cucumber—\""
    hol_delaney "\"It's on the card, babe. Metrics. No backing out. That's a full dose.\""
    show cg hol_hydrate_hand onlayer cgl
    "Her hand comes to rest on the back of your head, big and warm and unbothered, the way you'd rest your hand on a gatepost, and guides you down."
    menu:
        "Her hand on your head."
        "Say it round her":
            $ hol.shout2 = "round"
            hol_you "\"Mmph— Delaney— nnh— I said I'm— {i}mmph{/i}—\""
        "Push at her thighs":
            $ hol.shout2 = "push"
            "You push at her thighs with both hands. You might as well push at the wall."
            hol_you "\"I don't want— {i}mmph{/i}— I don't want the third one—\""
    show cg hol_hydrate_deep onlayer cgl
    "She doesn't push. She doesn't need to. She just holds you there while she talks to June through the open door about whether the restaurant does fish, and your mouth keeps working on her all by itself, wet and loud."
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"They do a sea bass.\""
    hide hol_june
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Is it the one with the capers? I hate capers.\""
    vn_sfx "{i}Shlp. Shlp. Shlp.{/i}"
    hol_you "\"Mmh— {i}mmmh{/i}— nnh— no— {i}mmph{/i}—!\"" with vnfx("shake")
    "Your tongue knows the way now, after two sessions. It goes under her, flat, the way she said. Your throat opens for more of her than it's ever taken. Your hands, which were pushing at her thighs, are holding them."
    hol_you "\"{i}Mmph{/i}— don't— {i}mmh{/i}— more— no— no, I don't mean more—\""
    show cg hol_hydrate_cum onlayer cgl
    "She comes without changing her tone of voice. You swallow. You can't not. It goes on and on, and you swallow all of it, eyes squeezed shut, moaning round her, and your own cock is hard and leaking on the floor between your knees with nobody touching it."
    hide hol_june
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Good. Fish it is.\""
    "She ruffles your hair."
    hide hol_june
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Couldn't ask for a better oral administrator. See you at morning metrics, babe.\""
    hide cg onlayer cgl
    jump hol_day_two_after

## ---- DAY 3: Live Enzyme Infusion. Delaney, then June, then the hot tub --------------------------
label hol_infusion:
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_infuse_bend")
    hol_delaney "\"Ready for your upgrade, superstar?\""
    if hol.hyd2 == "ask":
        hol_delaney "\"And before you ask, there's no depth on this protocol either. As far as it goes.\""
    else:
        hol_delaney "\"Same as yesterday. Just go for it. Well. I'll go for it.\""
    hol_you "\"I read about positionings. Is there a— um— preferred protocol?\""
    hol_delaney "\"Bend over, hold my wrist, and breathe.\""
    show cg hol_infuse_lube onlayer cgl
    "You bend over the table. She lubes you up like she's checking the oil in a car: one finger, cold and slick, then two, then three, chatting about the weather the whole time, how it's meant to rain Thursday."
    hol_you "\"{i}Hah{/i}— that's— the diagram didn't have— fingers—\""
    hol_delaney "\"Prep's not on the diagram, babe. Prep's manners.\""
    show cg hol_infuse_in onlayer cgl
    "Then her cock is pushing into you, slow, thick, so much bigger than her fingers, and you grab her wrist like she said, and breathe like she said, and it keeps coming."
    hol_delaney "\"Deep breath, Ellie. All right?\""
    hol_you "\"Delivery— um— optimal— {i}hah{/i}— the bioavailability— that's very— efficient—\""
    vn_sfx "{i}Pap... pap... pap...{/i}"
    "She fucks you face-down on the table, long slow strokes, and you narrate it the whole way through as delivery-method optimisation, and your voice keeps going up at the ends, and you keep pretending it's the effort."
    hol_delaney "\"You're tighter than most. That's good for uptake.\""
    hol_you "\"Is it? {i}Hah{/i}— good— that's good—\""
    "She finishes deep inside you with a grunt, and stays there a moment, and then slaps your arse, affectionately, like a horse she's fond of."
    hol_delaney "\"Internal application. High-yield. Stay put for ten.\""
    hol_you "\"Bioavailability, right?\""
    show cg hol_infuse_june onlayer cgl
    "Then June comes in with a magazine."
    $ hol.said_no += 1
    hol_you "\"Oh— no, sorry— I only booked the one. Just the one infusion. I checked. I checked twice.\""
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"It's a course, Ellie. It's on the card. Delaney usually gets A-plus infusion numbers; let's see about mine. Second time's easier.\""
    show cg hol_infuse_mag onlayer cgl
    "She puts the magazine down on your back, open, and keeps reading it, and pushes in where Delaney was."
    menu:
        "June, reading, inside you."
        "Tell her it's a mistake":
            $ hol.shout3 = "mistake"
            hol_you "\"It's a— nnh— it's a booking error— {i}ahh{/i}— I'll go to the desk— I'll go to the DESK—\""
            hide hol_delaney
            show hol_june reading at vn_cast_slot
            hol_june "\"The desk'll say it's a course.\""
        "Try to get off the table":
            $ hol.shout3 = "off"
            "You try to get off the table. Your hips push back onto her instead, and the magazine slides."
            hol_you "\"No— no— why are they doing THAT— June—\""
            "She straightens the magazine on your back."
    "She turns a page."
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"See how you take it, Ellie? That's absorption. There's my retention analyst. Ten minutes, minimum, after. You'll be a bombshell by supper.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    hol_you "\"Stop— please stop— {i}nnh{/i}— I'm not— I didn't book you—\""
    "She comes in you halfway through an article about kitchen islands and finishes the paragraph before she pulls out."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_tub", pc="flustered", pc_tag="hol_pc", cast=[], cg="hol_tub_pass")
    "And then the hot tub, all of them, before dinner, and you only meant to sit in it."
    show cg hol_tub_lap onlayer cgl
    "Delaney pulls you onto her lap under the water and slides into you without a word, easy as sitting down. A conversation about dinner reservations goes on over your head."
    hol_you "\"No— not again— I said one— I said {i}one{/i}—!\""
    show hol_casey warm at vn_cast_slot
    hol_casey "\"I think if we push it to eight we'll get the private room. Delaney, can you hold him a minute? Nadine, what was that place on the square?\""
    show hol_nadine brisk at vn_cast_slot
    hol_nadine "\"The one with the lanterns. It does a set menu.\""
    show hol_robin kind at vn_cast_slot
    hol_robin "\"Order the mezze for six. Ellie, are you—\""
    "Robin's eyes flick down to you, and away."
    show hol_robin kind at vn_cast_slot
    hol_robin "\"—fine with aubergine?\""
    hol_you "\"I'm— {i}nnh{/i}— I'm not fine with— Robin—\""
    show hol_robin kind at vn_cast_slot
    hol_robin "\"Aubergine it is.\""
    "Nobody else looks down. Delaney lifts you off her by the hips and passes you across the water to June like a towel."
    show cg hol_tub_june onlayer cgl
    show hol_june reading at vn_cast_slot
    hol_june "\"My turn, metrics queen.\""
    "June settles you onto her cock and goes on reading the dessert menu out loud off her phone."
    show hol_june reading at vn_cast_slot
    hol_june "\"Sticky toffee. Lemon posset. A cheese board, for the brave.\""
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Spicy tonight.\""
    show hol_june reading at vn_cast_slot
    hol_june "\"Just optimising group absorption.\""
    vn_sfx "{i}Splosh. Splosh. Splosh.{/i}"
    "A member of staff walks past with fresh towels and doesn't look up. A woman in the next tub turns a page of her book."
    hol_you "\"Somebody— anybody— this isn't— I didn't book the TUB—\""
    show cg hol_tub_cum onlayer cgl
    hol_you "\"Stop— stop it— {i}ahh{/i}— not in front of— why does nobody— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "You come under the water with nobody touching your cock, small and twitching, while June comes in you and asks whether anyone else wants the sticky toffee."
    show hol_june reading at vn_cast_slot
    hol_june "\"You're growing. Infusion's landing, all right.\""
    show hol_nadine brisk at vn_cast_slot
    hol_nadine "\"Congratulations, Ellie. First Hollow Pine curve badge.\""
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Eight, then.\""
    hide cg onlayer cgl
    $ hol.fit = "robe"
    jump hol_day_three_after

## ---- DAY 4: Deep Conditioning. Morning and evening; the thighs ---------------------------------
label hol_conditioning:
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "amused")], cg="hol_condition_am")
    "The morning one, you're fine with. A pump on the wall labelled CONDITIONING EMOLLIENT, a fresh towel, Delaney in her robe with a coffee."
    hol_delaney "\"Ellie, on your back this time. We're doing a full routine.\""
    "You lie back on the table with your knees up and Delaney pumps emollient into her palm, and slicks herself, and slicks you, and pushes in, slow, and it's easier than yesterday. It's a lot easier than yesterday."
    hol_you "\"Oh— that's— {i}oh{/i}, that's gone in easy—\""
    hol_delaney "\"That's the conditioning, babe. Look at you.\""
    show cg hol_condition_fill onlayer cgl
    "She fucks you slow and steady, with her coffee on the side table, and you watch the ceiling and count the tiles and lose count, and then she fills you, deep, and stays there."
    hol_delaney "\"Your thighs are unreal. You're going to spill over every chair in this place. Retention protocol. Don't lose a drop, Ellie. Ten minutes minimum, princess.\""
    "And you keep it in, because the leaflet says retention improves results. You lie very still on the table with your knees up for ten whole minutes, timing it on the wall clock."
    show cg hol_retention_walk onlayer cgl
    "Then you walk to breakfast very carefully, small steps, thighs pressed together, and sit down on a cushion Nadine slides under you without comment."
    hide hol_delaney
    show hol_nadine brisk at vn_cast_slot
    hol_nadine "\"Retaining?\""
    hol_you "\"Diligently.\""
    hide cg onlayer cgl
    $ vn_until(19)
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_room", pc="flustered", pc_tag="hol_pc", cast=[("hol_june", "dry")], cg="hol_condition_pm")
    "The evening one, you've had enough. You're full, you're tired, your new thighs rub together every time you walk, and when June comes to your room with the bottle you ask, politely, to skip it."
    $ hol.said_no += 1
    hol_you "\"I think I'll skip tonight's. I'm retaining loads. I'm retaining loads already. Honestly, I'm at capacity.\""
    hol_june "\"Retention improves results.\""
    "She sits you on the edge of the bed with your back to her, and squeezes your new thighs together with both hands, and slides her cock between them, slick, from behind."
    show cg hol_thighs onlayer cgl
    menu:
        "June between your thighs."
        "Tell her you said skip":
            $ hol.shout4 = "skip"
            hol_you "\"I said skip— June— I said— {i}nnh{/i}— don't put it— don't put it {i}in{/i}—\""
            hol_june "\"I'm not in. Yet. This is topical.\""
        "Clamp your thighs to stop her":
            $ hol.shout4 = "clamp"
            "You clamp your thighs to stop her. It makes it better for her, and she says so."
            hol_you "\"That's not— that's not what I meant by— {i}ahh{/i}—\""
            hol_june "\"Tighter's better, Ellie. Thank you.\""
    vn_sfx "{i}Shlick. Shlick. Shlick.{/i}"
    show cg hol_thighs_rub onlayer cgl
    "She fucks your thighs until you're both slick, and comes between them, and rubs what spills into your skin with slow, approving strokes, up the insides of your thighs, over your new hips."
    hol_june "\"Topical's not in the protocol. Call it a bonus.\""
    hol_you "\"Good— great— that's— so we're done, then, that's the—\""
    "Then she tips you forward onto the bed, face down, and pushes into you, deep, and holds there."
    show cg hol_condition_deep onlayer cgl
    hol_you "\"No— no more— I'm FULL— June, I'm full, there's no {i}room—{/i} {i}ohh{/i}—\""
    hol_june "\"There's always room. That's what conditioning's for.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "She fucks you slow, then not slow, and the bed creaks, and the stuff Delaney put in you this morning makes it slick and loud and easy, and somewhere in the middle of the noes it stops being noes."
    $ hol.broke = True
    show cg hol_condition_beg onlayer cgl
    hol_you "\"Don't— don't stop— June— don't you stop— {i}more{/i}— fill me up, fill me {i}up{/i}—!\"" with vnfx("flash", "shake")
    "You beg her for it at the top of your lighter voice, loud enough for the whole corridor, pushing your new arse back at her, your small cock dripping on the duvet. And she comes deep inside you and holds you there until it's settled, like the leaflet says."
    hol_june "\"Keep it in.\""
    hol_you "\"...I will.\""
    "You keep it in all night. You're very diligent."
    hide cg onlayer cgl
    jump hol_day_four_after

## ---- DAY 5: Postural Correction. Casey, then all five; the chart --------------------------------
label hol_correction:
    $ vn_enter(bg="hol_room", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "pleased")], cg="hol_casey_delight")
    if hol.deluxe:
        "She listens to all of it. Then she smiles, slowly, and looks you up and down: the new hips, the new bra under Nadine's cardigan, your arse."
    else:
        "She listens to all of it. Then she smiles, slowly, and looks you up and down: the new hips, the soft chest under Nadine's clothes, your arse."
    hol_casey "\"Oh, Ellie. Look at you. You're thriving. I wondered when you'd ask. I was hoping you would, you know.\""
    "It goes well. It goes so well. It's the wrong kind of well: she's delighted with you the way you'd be delighted with a result."
    hol_casey "\"Girls! Come and see! Ellie asked!\""
    $ hol.said_no += 1
    hol_you "\"Wait— no— I meant a date— I meant you and me, I meant like a {i}date{/i}—\""
    hol_casey "\"This is a date, Ellie. This is the best date.\""
    $ hol.fit = "nude"
    if hol.deluxe:
        ## THE DELUXE's day 5 beat: Casey's mouth on his chest opens the correction (non-con, as day 5 is)
        show cg hol_dx_casey_mouth onlayer cgl
        "Casey pushes you back on her bed and gets Nadine's cardigan off you, then the new bra, one-handed, faster than Nadine put it on, and stops, and looks."
        hol_casey "\"Oh my God. Ellie. You booked the {i}Deluxe{/i}.\""
        hol_you "\"It's toning— Casey, wait, I meant a {i}date{/i}—\""
        "She puts her mouth on you. On your chest, on your new nipple, warm and wet, sucking, her hand full of the other one, and laughs into it, and the girls come in behind her and see."
        hol_you "\"Casey— no— not— {i}ahh{/i}— that's not what I— I wanted to {i}tell{/i} you something—\""
        hol_casey "\"Tell me after.\""
        show cg hol_casey_first onlayer cgl
        "Then she climbs up and sits on your face, warm and wet and laughing, and keeps both her hands on your chest while she does."
    else:
        show cg hol_casey_first onlayer cgl
        "Casey pushes you back on her bed and pulls Nadine's clothes off you, laughing, and climbs up and sits on your face, warm and wet and laughing, while the others come in behind her."
    hol_you "\"Mmph— Casey— I didn't— {i}mmph{/i}— I didn't mean ALL of—\""
    "Four years. Four years you've wanted Casey, and she's on your mouth, and she tastes like the hot tub and her laugh is coming down through her thighs into your skull, and it is not, not at all, what you meant."
    hol_casey "\"Oh, that's nice. Oh, you've been practising on something.\""
    show cg hol_chart onlayer cgl
    hide hol_casey
    show hol_june reading at vn_cast_slot
    hol_june "\"Postural correction. Your posture's still guarded. See the chart.\""
    "June holds it up over Casey's shoulder for you to see. The chart is a diagram of a person bent over a bed, with arrows."
    "Delaney's already behind you."
    menu:
        "All five of them."
        "Ask them to stop":
            $ hol.shout5 = "stop"
            hol_you "\"Stop— please— one at a— one at a TIME— {i}ahh{/i}—\""
            hide hol_casey
            show hol_june reading at vn_cast_slot
            hol_june "\"It is one at a time, Ellie. At each end.\""
        "Ask for Casey only":
            $ hol.shout5 = "casey"
            hol_you "\"Just Casey— I only wanted Casey— {i}nnh{/i}— please—\""
            hide hol_june
            show hol_casey warm at vn_cast_slot
            hol_casey "\"You've got Casey, babe. You've got everyone.\""
    show cg hol_correction onlayer cgl
    "They correct your posture. That's what it says on the card. Casey gets off your face and turns you over, and Delaney's hands set your hips where the chart says, and push in, and June reads the chart aloud while it happens, and Nadine strokes your hair, and Robin holds your hand."
    hide hol_casey
    show hol_june reading at vn_cast_slot
    hol_june "\"Arch, please. Higher. Long axis. Voice resonance, arch, mouth open. Hold that.\""
    hol_you "\"I don't— {i}ahh{/i}— I don't want to hold it—\""
    hide hol_casey
    show hol_nadine brisk at vn_cast_slot
    hol_nadine "\"You're holding it beautifully.\""
    show cg hol_correction_robin onlayer cgl
    "Robin's hand is warm and dry and steady round yours. She's kneeling by the bed, looking at you, really looking, for the first time all week."
    hide hol_casey
    show hol_robin kind at vn_cast_slot
    hol_robin "\"You're doing so well, Ellie. You took to this faster than I did.\""
    hol_you "\"Robin— Robin, make them— {i}nnh{/i}— did you— was it like this for—\""
    hide hol_casey
    show hol_robin kind at vn_cast_slot
    hol_robin "\"Shh. Breathe. Arch for June.\""
    show cg hol_correction_swap onlayer cgl
    "And they swap. Delaney pulls out and June's in, and then Casey with a strap from somewhere, laughing, and then Delaney again, and someone's in your mouth, and someone's hand is on your hip correcting it by a fraction you can feel and nobody could see."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    hide hol_casey
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"For the finish, Ellie. Beg for it.\""
    hol_you "\"No— no— oh— {i}oh{/i}— please— please don't stop— no, I mean— {i}ahhh{/i}— please—!\"" with vnfx("flash", "shake")
    show cg hol_correction_cum onlayer cgl
    "You come in the middle of them, begging, with nobody touching your small cock, and they swap, and swap, and swap, until the last treatment of the week is done and you're lying in a heap of robes with cum running down the backs of your thighs and Casey's hand in your hair."
    hide hol_casey
    show hol_june reading at vn_cast_slot
    hol_june "\"Final retention: excellent. Good compliance.\""
    hide hol_delaney
    hide hol_june
    hide hol_nadine
    hide hol_robin
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Best trip ever.\""
    hide cg onlayer cgl
    $ hol.fit = "nadine"
    $ vn_enter(bg="hol_room", pc="flustered", pc_tag="hol_pc", cast=[("hol_casey", "warm")], cg="hol_after_five")
    "Afterwards, the others drift off to the pool, and Casey falls asleep with her arm over you, on her bed, in her robe, smelling of the hot tub."
    "You lie there and look at her ceiling. Four years. You asked her. And she said yes, in a way, and then she called everyone in, and they corrected your posture, and you came begging in the middle of them, and she said it was the best trip ever."
    "You can't tell if that was a yes. You can't tell if anything this week was a yes. You lie very still so as not to wake her, and your thighs are sticky, and you think about the card."
    hide cg onlayer cgl
    hide hol_casey
    jump hol_day_five_after

## ---- DAY 6: The Full Package. All of it, all of them, all day; he asked -------------------------
label hol_full_package:
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_treatment", pc="begging", pc_tag="hol_pc", cast=[("hol_delaney", "amused")], cg="hol_full_morning")
    "Morning, the treatment room: Delaney on the table with her coffee, and you ask for it before she's got her robe off."
    hol_you "\"Please. All of it. Don't go slow.\""
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"Oh, she's proactive now?\""
    hol_you "\"I'm not pretending. I'm not reading it off a card. I want it. All of it.\""
    show cg hol_full_ask onlayer cgl
    "You climb on Delaney yourself. You've never done that. You sink down onto her on the table, all of her, your huge new thighs spread over hers, and she puts her coffee down for the first time all week."
    hide hol_june
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Well. Hello, Ellie.\""
    hol_you "\"Hello. Don't talk. Fuck me.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "She does, and you ride her, and you come on her before breakfast with your hands on her shoulders and your forehead on her collarbone, which is where your eyes come to now if you're sitting in her lap."
    show cg hol_full_tub onlayer cgl
    "Midday, the hot tub: passed from June to Delaney to June, your mouth on one and your arse on the other, and you don't say no once. You say more."
    hol_you "\"More— more, June— Delaney, your turn, please, your turn—\""
    show cg hol_full_pin onlayer cgl
    "Staff walk past with towels and don't look up. When your hand goes to your own cock, June takes it and pins it by your side, laughing."
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"No hands, Ellie. Not unless you ask.\""
    hol_you "\"Please— please, can I— please, someone?\""
    hide hol_june
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Let June take care of you.\""
    "June doesn't touch it either. She just fucks you until you come anyway, untouched, in the water, and laughs at you, fondly, and says that's the point."
    if hol.deluxe:
        ## THE DELUXE's day 6 beat: his first titfuck, which he booked (consensual, as day 6 is)
        show cg hol_dx_titfuck onlayer cgl
        "Afternoon, your room, Nadine's things on the floor. You kneel up on the bed and take Delaney's cock in both hands and put it between your breasts yourself, and press them round it, and look up at her."
        hol_you "\"I booked this. I did, didn't I? This one's mine.\""
        hide hol_june
        show hol_delaney idle at vn_cast_slot
        hol_delaney "\"All yours, Deluxe.\""
        vn_sfx "{i}Fwap. Fwap. Fwap.{/i}"
        "It's your first. You've never had anything to do it with. You do it badly for a minute, and then not badly at all, the weight of them sliding up and down her, the head pushing out between them on every stroke, and Delaney puts her coffee down for the second time all week."
        show cg hol_dx_titfuck_cum onlayer cgl
        hol_you "\"On them— all over them— Delaney— {i}please{/i}—!\"" with vnfx("shake")
        "She comes up through your cleavage onto your chin and your throat, and you rub it in yourself, round and round, the way Fox does. Topical."
        show cg hol_full_thighs onlayer cgl
        "Then your huge new thighs squeezed round her cock, then June in you while you suck Delaney, swapping, the bed knocking the wall."
    else:
        show cg hol_full_thighs onlayer cgl
        "Afternoon, your room: Nadine's things on the floor, your huge new thighs squeezed round Delaney's cock, then June in you while you suck Delaney, swapping, the bed knocking the wall."
    if hol.sell3 == "diagram":
        hide hol_delaney
        show hol_nadine brisk at vn_cast_slot
        hol_nadine "\"I booked an infusion, you know. Your napkin diagram. It's very persuasive.\""
    else:
        hide hol_delaney
        show hol_nadine brisk at vn_cast_slot
        hol_nadine "\"I booked an infusion, you know. After you slapped your own arse at the pool. Very persuasive.\""
    hol_you "\"{i}Mmh{/i}— good— you'll love it— {i}mmh{/i}—\""
    show cg hol_full_cum onlayer cgl
    hol_you "\"Fill me up— both of you— please— {i}please{/i}—!\"" with vnfx("shake")
    vn_sfx "{i}Splurt. Splurt.{/i}"
    "Cum everywhere: on your chest, in your mouth, dripping down the backs of your thighs, on Nadine's clothes, which she says she'll launder before you leave, so you can pack cleanly."
    show cg hol_full_evening onlayer cgl
    "Evening, all five, on the big bed: and your small cock bobbing between your legs the whole time, a fixture of the room, never the point, and nobody minds it."
    hide cg onlayer cgl  # ff 3:54 am: no picture, full-kiss failed 4 draws (SCENES.md hollowpine v10)
    "Casey holds your face and kisses you while the others take turns. A real kiss. Long. The one you practised for in the hot tub, four years of it."
    if hol.confess5 == "years":
        hide hol_delaney
        show hol_casey warm at vn_cast_slot
        hol_casey "\"Four years, you said. You should've just asked.\""
    else:
        hide hol_delaney
        show hol_casey warm at vn_cast_slot
        hol_casey "\"You asked me out. You know that? Nobody's ever asked me out on this trip.\""
    hol_you "\"Is this— {i}ahh{/i}— is this a yes?\""
    hide hol_delaney
    show hol_casey warm at vn_cast_slot
    hol_casey "\"This is always a yes, Ellie.\""
    hide hol_delaney
    show hol_robin kind at vn_cast_slot
    hol_robin "\"You look so beautiful now.\""
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"Tell me how bad you need it, Ellie.\""
    hol_you "\"Please— all of you— any of you— I want every part, every round, more—\""
    hide hol_delaney
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Look at you.\""
    show cg hol_full_last onlayer cgl
    hol_you "\"Don't— don't stop— I want it, I want all of it— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "You take all of them and ask for more, and get more, until the last of the candles burns down and Delaney falls asleep across your new thighs like they're a pillow, which they are now."
    hide cg onlayer cgl
    $ hol.fit = "nadine"
    jump hol_ending
