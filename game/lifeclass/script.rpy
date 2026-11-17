## THE SOURCE: lifeclass's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage
## of the original (main.twee, rungs.twee, rungs-late.twee), written as beats; the director scenes
## are in scenes.rpy. The original is in catalog/docs/routes/vn-original/lifeclass/.
## Studio words only (class, instructor, model, session, pose, sheets, schedule, spring); no numbers.

## ---- DAY 1 (Lifeclass Opening, Stairs 1, Session 1, Sink 1, Packup 1) -------------------------

label lc_opening:
    $ lc.fit = "own"
    $ vn_enter(bg="lc_bedsit", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_flyer")
    show bg lc_bedsit onlayer bgl
    "The bedsit on Domus Street is one room: a bed, a kettle you can reach from the bed, a rail of clothes, a window onto the bus stop."
    "Your bank app says a number you don't want to look at. Your fridge says milk, and not much milk."
    "You're hairy and broke, and you've got a pair of jeans, a white t-shirt, a bus pass, and one idea."
    show cg lc_flyer onlayer cgl
    "Yesterday, on Cliff Street, taped by the side door of the Ocean Breeze café, a sheet of A4:"
    show screen lc_sheet(["{b}LIFE MODEL WANTED.{/b}", "OPEN CALL.", "{b}CASH.{/b}"])
    "You've been thinking about it all night. You'd have to take your clothes off. In front of people. Who'd be {i}drawing{/i} you."
    "But it's cash. For sitting still."
    hide screen lc_sheet
    hide cg onlayer cgl
    lc_you "\"How hard can sitting still be?\""
    "The kettle doesn't know. You put your jeans on, and your shirt, and look in the mirror over the sink at a perfectly ordinary man with a mop of mint-green hair, a lot of hair on his arms and the start of a grin."
    lc_you "\"Sorry. Hi. Sorry. Open call?\"\n{size=-5}{color=#ff8fa3}▸ Catch the bus to Cliff Street{/color}{/size}"
    $ vn_until(14)
    jump lc_stairs_one

label lc_stairs_one:
    $ vn_enter(bg="lc_stairs", pc="apologetic", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_stairs onlayer bgl
    "The side stairs go up past the café's bins, steep and narrow, with the smell of the Ocean Breeze's chips coming up after you."
    "At the top there's a door with a frosted window and a sheet of paper taped to it: the schedule. Somebody's ruled it in biro. The top line has a blank in it, and a pen on a string."
    "You write your name in the blank. Then, because nobody's looking, you read it out loud to see how it sounds."
    show screen lc_sheet(["{b}SCHEDULE{/b}", "Model: [lc_pc_name] (open call)."])
    lc_you "\"{i}Model: [lc_pc_name] (open call).{/i}\""
    "It sounds like money. You grin at it."
    hide screen lc_sheet
    show lc_dot flat at vn_cast_slot
    "The door opens before you can knock. A woman in a paint-stiff apron, hair scraped back with a pencil through it, looks you up and down the way you'd look at a used fridge."
    lc_dot "\"Open call?\""
    lc_you "\"Yes! Sorry. Yes. Hi. Sorry.\""
    lc_dot "\"Dot. I run the room. Screen's broken. Clothes on the chair by the door. You're on in a minute. Don't apologise to the furniture.\""
    "She's already walking away."
    hide lc_dot
    show bg lc_room onlayer bgl
    "Inside it's one long room under a skylight, cork boards down every wall, easels in a horseshoe, and a stand at the far end with a wooden stool on it and a drop cloth under the stool."
    "People are setting up. Nobody looks at you. Everybody looks at you. The chair by the door is very exposed."
    menu:
        "The chair by the door."
        "Shirt first, fast, like a plaster":
            $ lc.undress = "fast"
        "Everything at once, eyes shut":
            $ lc.undress = "shut"
        "Jeans first, and fall over":
            $ lc.undress = "fall"
    $ vn_pass(5)
    jump lc_session_one

label lc_session_one:
    $ lc.fit = "nude"
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_session1_stool")
    if lc.undress == "shut":
        "You do it all at once with your eyes screwed shut, and when you open them you're naked by the door and somebody's sharpening a pencil at you."
    elif lc.undress == "fall":
        "You get one leg out of your jeans, hop, get the other leg stuck, and go down sideways onto the chair. Somebody at the back says \"Fuck me,\" admiringly. You get up naked."
    else:
        "Shirt off, jeans off, pants off, fast, like a plaster. Done. Naked. You stand there with your hands over your crotch, breathing like you've sprinted the stairs."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Stand. Stool. Sit. Hands off it, it's not a secret.\""
    show cg lc_session1_stool onlayer cgl
    "You go up on the stand. The stool's old and wobbly and painted a lot of colours. You sit. You put your hands on your knees."
    "You are covered in hair, it occurs to you: chest, belly, arms, legs, a thick dark tuft above your cock. You've never thought about it before. Under the skylight you can't think about anything else."
    "Dot claps once."
    $ _lc_c = lc_call(1)
    show lc_dot crit at vn_cast_slot
    lc_dot "[_lc_c]"
    "Charcoal starts scratching all round the horseshoe. You look at the room, because there's nowhere else to look."
    show lc_roz swearing at vn_cast_slot
    "The first one you notice is the swearing. A woman with a shaved head and charcoal right up her forearms like gloves is fighting a sheet of paper on her board."
    lc_roz "\"Fuck. Fuck {i}off{/i}. Shit. Right.\""
    hide lc_roz
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Roz, language.\""
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Fuck's sake, sorry.\""
    hide lc_roz
    show lc_dario drawing at vn_cast_slot
    show cg lc_session1_dario onlayer cgl
    "The second one you notice is the one who isn't fighting anything. Dark hair, sleeves shoved up, a big board on his knees."
    "He's drawing fast and he's staring, steady and hungry, at your crotch. Not your face. Not your chest. Your cock. He catches you catching him and doesn't look away."
    hide lc_dario
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Dario. Value study.\""
    hide lc_dot
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"I'm doing values.\""
    "He doesn't change anything."
    show lc_pc flushed
    "Your cock, which has been trying very hard to stay out of this, gets hard. All the way. In front of everybody."
    lc_you "\"Sorry. Sorry— sorry—\""
    hide lc_dario
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Don't apologise to me, it's not mine. Don't drop the shoulder.\""
    "You put your shoulder back up. Your cock stays exactly where it is. Dario's charcoal speeds up."
    hide lc_dario
    show lc_aurelio still at vn_cast_slot
    "The third one isn't drawing at all. A tall woman at a modelling stand at the side, sleeves rolled, wet grey clay to the wrists, building something out of a lump with her thumbs."
    "She looks at you once, a long look, top to bottom, and goes back to the clay."
    lc_aurelio "\"More.\""
    "To the clay. That's Aurelio. She doesn't say anything else for an hour."
    hide lc_aurelio
    "There's a big man at the back with forearms like a removal man's, a woman in pastel dust who laughs at everything, and a quick, keen one by the window who's done a stack of sheets while the others are on their first."
    show lc_winnie late at vn_cast_slot
    "And the door bangs open halfway through the pose and a woman with a huge canvas bag falls in, already talking."
    lc_winnie "\"Sorry sorry sorry, the bus, there was a man with a whole wardrobe on the bus, you would not {i}believe{/i}—\""
    hide lc_winnie
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Winnie. Hold that.\""
    "Without looking round. Winnie holds it. She sets up next to Roz and starts telling her about her palette instead, in a whisper."
    hide lc_winnie
    "You sit. You stay hard. It's the most embarrassing thing that's ever happened to you and the easiest money you've ever made, and your cock won't go down, and Dario won't stop drawing it, and there's a wet clear string hanging off the tip of it now, swaying, catching the skylight."
    lc_you "\"Oh my god. Sorry. Can somebody tell him to stop drawing {i}it{/i}? It won't go down while he's drawing it. Sorry.\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Nobody's stopping.\""
    show lc_roz fierce at vn_cast_slot
    "After the break Dot walks round the horseshoe behind the easels, looking. She stops behind Roz. Roz's sheet is a furious grey fog with a stool in it."
    lc_roz "\"I can't get a single fucking form through all that. It's all {i}hair{/i}. It's a hedge. It's not reading from the back row.\""
    hide lc_roz
    show lc_dot crit at vn_cast_slot
    lc_dot "\"It's not.\""
    "She looks at you. Not at your face; at your arm, your chest, your belly, the way you'd look at a canvas with something wrong in the corner."
    hide lc_roz
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Roz. Sink.\"\n{size=-5}{color=#ff8fa3}▸ Off the stand{/color}{/size}"
    hide lc_roz
    $ vn_pass(75)
    jump lc_sink_one

label lc_sink_one:
    $ vn_enter(bg="lc_sink", pc="protesting", pc_tag="lc_pc", cast=[("lc_roz", "swearing")], cg="lc_sink_brush")
    "The sink's at the back of the room: a big cracked butler's sink with a brick of grey soap, a nailbrush and a tap that knocks. Roz is already there, running it, shoving her black sleeves up past black elbows."
    lc_roz "\"In. Stand in the drip tray. Arms up. Fuck's sake, you're like a carpet.\""
    lc_you "\"Is this— normal? Is this a normal thing that—\""
    lc_roz "\"Arms {i}up{/i}.\""
    "Behind you the easels scrape. The whole horseshoe has turned round to face the sink."
    hide lc_roz
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Keep going. Sink's in the light. Value study.\""
    lc_you "\"You're— you're still {i}drawing{/i}? I'm at the {i}sink{/i}—\""
    show cg lc_sink_brush onlayer cgl
    "Roz soaps the brush and goes at you. Your chest first, hard, round and round, charcoal off her hands going grey in the lather. It tickles. Then it doesn't tickle. Then it's something else."
    $ lc_body(1)
    "{color=#ff5fb8}You look down, and the soap's sliding off your chest, and there's nothing under it. No hair. Not shaved; {i}gone{/i}, like it was never there. Your chest is bare and wet and pink from the brush, smooth as the inside of a cup.{/color}"
    lc_you "\"Oh my {i}GOD{/i}— what is— stop— {i}stop{/i}, Roz, stop scrubbing, it's {i}going{/i}—\""
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Hold still.\""
    "She goes at your belly. It goes. Charcoal scratching behind you, the whole room getting it down."
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Shit. Shit, look at that. That's a {i}form{/i}. Fucking finally.\""
    lc_you "\"Stop drawing it— stop {i}DRAWING{/i} it— can't any of you {i}see{/i}—!\""
    "Nobody stops. Your arms go, armpits and all, her brush scrubbing, swearing at every stroke. Your legs, Roz crouching at your feet, brush up one shin and down the other, and it all comes off in the lather and swirls away while you twist round to yell at the easels."
    show cg lc_sink_tuft onlayer cgl
    "Then she grabs your cock out of the way like a tap she's moving, and scrubs the tuft above it."
    lc_you "\"No— not {i}there{/i}— Roz— {i}Roz{/i}— {i}ahh{/i}—\""
    "{color=#ff5fb8}It goes. All of it. You're bare all over, smooth and soft and squeaky and {i}tingling{/i}, and your cock's standing straight up out of her black fist, drooling on her knuckles, with a whole room drawing it.{/color}"
    lc_you "\"Oh my GOD, look at me— look at me— where's it {i}gone{/i}— why is it {i}hard{/i}—\""
    "Your hands go to your chest to cover it, and they don't cover it. They glide. They know where to press, and you yank them away like it's hot."
    "{color=#ff5fb8}Your lips are buzzing. You lick them and a moan comes out of you at the sink, out loud, in front of everybody, because they've gone sensitive, swollen and hot, like someone's just kissed you very hard.{/color}"
    lc_you "\"Mmh— {i}fuck{/i}— no— Roz, my {i}mouth{/i}—\""
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Nobody touched your mouth.\""
    "She rinses you down with a jug, cold, and you squeal. Then she grabs you round the hip to turn you to the light, and her charcoal fingers go round you and meet."
    show cg lc_handprint_1 onlayer cgl
    "When she lets go there's a black handprint on your hip. Perfect. Every finger."
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"There. Now I can see you.\""
    hide cg onlayer cgl
    "You walk back to the stand bare and dripping and so hard it bobs, and everybody's already turned to a clean sheet. Nobody says a word about it."
    lc_you "\"Did nobody else see that? It all just— it {i}went{/i}—\""
    hide lc_roz
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Better. Sit.\""
    "You sit, because it's cash, because you don't know what else to do. The charcoal sounds different. Faster. You can feel the room {i}reading{/i} you now, every smooth line of you, and you sit there with your knees clamped and your cock dripping on the drop cloth.\n{size=-5}{color=#ff8fa3}▸ Hold it to the end{/color}{/size}"
    $ vn_pass(80)
    jump lc_packup_one

label lc_packup_one:
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_wall_1")
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\""
    "The room breathes out."
    show cg lc_wall_1 onlayer cgl
    "People start pinning. Dot has a rule, apparently: the good ones go up on the cork by the door, so the next session sees them. Roz pins one, swearing, and then another. A strip of you goes up by the door, smooth and grey and black, you on a wobbly stool."
    "None of it's Dario's."
    show cg lc_dario_board onlayer cgl
    "Dario's still sitting with his board on his knees. It's one board. He's clipped a whole stack of sheets to it, and every one of them is the same thing: your cock. Hard, from the left, the vein down the side, a bead on the tip. Over and over. Values, he said."
    lc_you "\"You're not pinning?\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"No.\""
    hide cg onlayer cgl
    show lc_dot flat at vn_cast_slot
    "Dot comes over with an envelope and puts it in your hand. It's fat. It's cash. You look inside and laugh out loud."
    lc_you "\"Is there more? Work. More work. Like this. I can do— I'm free. Every— I'm free.\""
    "It's out of your mouth before you can stop it. Dot looks at you, top to bottom. Smooth to the toes."
    lc_dot "\"Email me. Tonight.\""
    "She writes an address on the back of your envelope in charcoal."
    hide lc_dot
    "Then she's gone, and Roz is gone, and the last of them clatter down the side stairs with their boards, and it's just you and the skylight going orange, and Dario, still on his chair, still with his board on his knees."
    "He's looking at your cock.\n{size=-5}{color=#ff8fa3}▸ Stay on the stand{/color}{/size}"
    $ vn_pass(10)
    jump lc_stand_one

## ---- rung 1: Dario on the stand (Lifeclass Stand 1). Non-con, no flip; nothing inside you. ----

label lc_stand_one:
    $ vn_enter(bg="lc_room_evening", pc="protesting", pc_tag="lc_pc", cast=[("lc_dario", "hungry")], cg="lc_stand_close")
    show cg lc_stand_close onlayer cgl
    "He gets up. He brings the board. He sits down on the edge of the stand right by your knee, props the board on his own knee, and looks at your cock from about a hand away."
    lc_dario "\"Don't move. I want the underside.\""
    lc_you "\"The— no, it's {i}over{/i}, she said {i}time{/i}, I'm getting dressed—\""
    "You start to get up."
    lc_dario "\"Sit. Light's perfect. Sit.\""
    "He doesn't even look at your face. He draws, eyes flicking between you and the sheet. Then he puts the charcoal behind his ear and wraps his fist round the base of your cock, firm, warm, black-fingered, and pins it there."
    show cg lc_stand_fist onlayer cgl
    lc_you "\"{i}Hhh{/i}—! What are you— get your {i}hand{/i} off—\""
    lc_dario "\"Holding the model still. You keep moving it.\""
    "He runs his thumb up the vein."
    lc_dario "\"Vein down the left side. Darkest value in the room. Did you know that?\""
    lc_you "\"N-no— I don't {i}care{/i}— Dario, I didn't say you could—\""
    "He strokes. Slow. All the way up, all the way down, watching it like he's going to be tested on it. You grab the edge of the stool."
    "Then you grab his wrist to haul it off you, and your hand closes over his fist, and it {i}knows{/i}: your hand finds Dario's fist and knows exactly how hard to squeeze. It squeezes. It doesn't pull."
    lc_you "\"No— that's not— I'm pulling, I'm {i}pulling{/i} it off— oh {i}god{/i}— {i}why's it doing that{/i}—\""
    lc_dario "\"Like that. Been drawing it all afternoon.\""
    lc_you "\"How many have you done?\""
    "You gasp it at him, at the ceiling, at anyone."
    lc_dario "\"All of it. Now I want the head.\""
    lc_you "\"Don't you— {i}don't{/i}—\""
    show cg lc_stand_mouth onlayer cgl
    "He puts his mouth on it." with vnfx("shake")
    lc_you "\"{i}AHH{/i}—!\""
    "He takes you in, all of you, his fist still round the base, his other hand flat on your belly pinning you to the stool, and he doesn't stop talking. He talks round you."
    lc_dario "\"Mmf— head's darker when you're— {i}mmh{/i}— close— rim's sharp, sharp edge, then nothing, soft— need more black on the— {i}mmh{/i}—\""
    lc_you "\"Get {i}off{/i}— stop— don't {i}narrate{/i}— stop {i}narrating{/i} it, I'm not your— {i}hnnh{/i}— {i}ahh{/i}—\""
    "He bobs on you, slow and wet and greedy, his tongue tracing the vein he drew, his eyes up on your face like he's checking his values."
    "You shove at his head and your hips jerk up off the stool into his mouth instead. Your hand's still on his fist, squeezing it for him. Your new smooth thighs are shaking either side of his head."
    lc_you "\"Stop— {i}stop{/i}— oh god, don't stop— I mean {i}stop{/i}— I'm gonna— Dario, I'm {i}gonna{/i}— {i}please{/i}—\""
    "He pulls off at the last second. He wants to see it."
    show cg lc_stand_cum onlayer cgl
    "You come so hard the stool skids: across your own belly, hot and thick, across the drop cloth, and across the sheet on top of his board, the best one, the one he did from a hand away, a long white stripe right over the drawing of the thing that did it." with vnfx("flash")
    $ lc_enc.pc_orgasms = 1
    lc_you "\"Oh no. Oh no, your {i}drawing{/i}—\""
    "Dario looks at the sheet. He holds it up to the skylight."
    lc_dario "\"That one I'm keeping.\""
    "He's still hard in his jeans. You can see it. He doesn't do anything about it. He licks his lips, picks up the charcoal, and starts a new sheet, with your cock softening in it, wet on his fist."
    menu:
        "He's not finished drawing."
        "He's not done with the underside":
            jump lc_stand_sex
        "Get dressed":
            jump lc_stand_close

label lc_stand_close:
    $ lc.fit = "own"
    $ vn_enter(bg="lc_bus", pc="apologetic", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_bus onlayer bgl
    $ vn_until(18)
    "Later, on the bus home with the envelope in your pocket and your whole body tingling under your clothes, you look at the cash for a long time. Then you write the email with your thumbs."
    "{i}Hi Dot. It's the open call. Is there more work? Sitting, I mean. Just sitting. I'm free. Sorry. Thanks.{/i}"
    show bg lc_bedsit onlayer bgl
    "In the bedsit you lie on top of the covers in the dark with your hand on your own smooth arm, and it won't stop stroking, and your cock won't go down.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_two

label lc_stand_after:
    $ vn_enter(bg="lc_room_evening", pc="flushed", pc_tag="lc_pc", cast=[("lc_dario", "smug")], cg="lc_stand_sex_cum")
    if lc_enc.pc_orgasms > 1:
        "You come in his mouth this time, yelling at him to get off right up until you're yelling at him not to, and he holds it there and swallows and keeps talking, which shouldn't be possible."
    else:
        "He finishes you with his fist, fast and black-fingered, and you spray your own smooth belly while he watches the shape of it."
    hide cg onlayer cgl
    show lc_dario smug at vn_cast_slot
    lc_dario "\"Underside's done. Same time next session.\""
    "He wipes his mouth on his sleeve."
    hide lc_dario
    $ lc.fit = "own"
    $ vn_until(18)
    "On the bus home you look at the cash for a long time, and then you write Dot the email with your thumbs: {i}Is there more work? Sitting, I mean. I'm free. Sorry. Thanks.{/i}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_two

## ---- DAY 2 (Lifeclass Morning 2, Session 2) -------------------------------------------------------

label lc_morning_two:
    $ lc.fit = "own"
    $ vn_enter(bg="lc_bedsit", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_reply")
    show cg lc_reply onlayer cgl
    "You wake in the bedsit on Domus Street, with the bus stop outside the window and the kettle in reach."
    "You reach for your phone first thing. There's a reply. It came in the middle of the night."
    show screen lc_sheet(["{i}Stay after. Hands and face. Cash. Don't be late. D.{/i}"])
    lc_you "\"Cash. It says {i}cash{/i}.\""
    "To the ceiling. Hands and face. Hands and face is fine. Nobody's going to do anything to your hands."
    hide screen lc_sheet
    hide cg onlayer cgl
    "In the shower you can't stop touching yourself. Not like that. Well, a bit like that. Just your arms, your chest, your belly, the backs of your knees: smooth all over, the water beading up and running off you differently."
    "Nothing's grown back. You check again. You check again, bent over, with a hand mirror, and laugh at yourself."
    "Your jeans go on like they always do. You look exactly like you did yesterday, except smooth, and except that you can't keep your hands off your own arms.\n{size=-5}{color=#ff8fa3}▸ Catch the bus to Cliff Street{/color}{/size}"
    $ vn_until(14)
    jump lc_session_two

label lc_session_two:
    $ lc.fit = "nude"
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_session2_pose")
    "Up the side stairs, past the sheet on the door, in. Clothes on the chair. You're quicker about it today. Nobody falls over."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Stand. Standing poses. Quick ones.\""
    $ _lc_c = lc_call(2)
    show lc_dot crit at vn_cast_slot
    lc_dot "[_lc_c]"
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Quick as you like. Go.\""
    show cg lc_session2_pose onlayer cgl
    "It's fast. You throw a pose, the charcoal scratches, Dot says \"Change,\" you throw another. Arms up. Hand over your face. Reaching. Pointing. Hands on your hips."
    "Your cock's up again, of course, bobbing every time you change, and Dario's drawing nothing else, of course, not one hand, not one face."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Hands, Dario.\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"They're in it.\""
    "They are. Round your cock."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change.\""
    "You put your hand up to your jaw for the next one, thinking, and the room goes quiet the way it does when everybody's concentrating at once. Every eye on your hand. Every stick of charcoal on it."
    show cg lc_hands_grow onlayer cgl
    $ lc_body(2)
    "{color=#ff5fb8}Your hand feels {i}wrong{/i} on your face. Too soft. You look at it. The knuckles you've had all your life are going small under the skylight, slimming like a glove being pulled tight, the fingers tapering, the nails narrowing to neat little ovals.{/color}"
    show lc_pc protesting
    lc_you "\"No— no no no— my {i}hands{/i}— stop— everybody stop {i}drawing{/i} my hands—!\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change.\""
    lc_you "\"Did you {i}hear{/i} me? It's {i}happening{/i}, look at them, stop drawing them—\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Arms out. Change.\""
    "Nobody's pencil even slows."
    "{color=#ff5fb8}Your arms go out because she said so, and your skin's going too. You can {i}feel{/i} it, all over, going soft under the lights like warm butter, every rough patch on your elbows and knees melting into silk.{/color}"
    lc_you "\"{i}Mmh{/i}— stop it— {i}stop{/i}— everything's going so {i}soft{/i}— can't any of you {i}see{/i}—\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change.\""
    "{color=#ff5fb8}In the dark of the window, your reflection. Your jaw, the square one you've had all your life, is softening while you watch. Rounding off. Your face looks softer and prettier and very, very alarmed.{/color}"
    lc_you "\"My {i}face{/i}— not my face— put the charcoal {i}down{/i}—!\""
    show cg lc_nipples_2 onlayer cgl
    "{color=#ff5fb8}And your nipples. They're tingling, then throbbing sweetly, then they {i}puff{/i}, right there on your flat chest, swelling up pink and tender and fat, a soft puffy AA at the very most, on a chest that's otherwise exactly yours.{/color}"
    lc_you "\"{i}Ahh{/i}— no— look at— they're {i}puffy{/i}— why are they— {i}hah{/i}— why are they so {i}sensitive{/i}—!\""
    "You go to cover them and brush one with your new soft thumb and your knees buckle. Your lips are fuller round every gasp. And your cock is {i}pouring{/i}, in front of all of them, while you yell at them to stop."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change. Hands on the hips.\""
    "Your slim new hands go to your hips, and you moan at the touch of them, out loud, and hate it, and the whole room draws that too."
    hide cg onlayer cgl
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Can't get the hands from the back row. They've gone fine.\""
    "The big man at the back re-blocks his easel closer."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Then come forward.\""
    show cg lc_handprint_2 onlayer cgl
    "At the break Roz grabs your arm to move you into the light and leaves a print, and it's smaller than yesterday's, much smaller, sunk in softer skin."
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Fuck.\""
    "Approvingly. The wall's filling up: the strip by the door has spread across, sheets of you overlapping, right across to the window."
    "Dario's packing a folder. It won't zip. He sits on it."
    hide cg onlayer cgl
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\""
    "Everybody packs. Everybody goes, down the side stairs, clattering. You start for the chair by the door."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"You. Stay.\""
    lc_you "\"I— the email said hands and face, I've done hands and face—\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Stay after. It said that too.\""
    "Dario doesn't move either.\n{size=-5}{color=#ff8fa3}▸ Stay{/color}{/size}"
    $ vn_until(17)
    jump lc_study_two

## ---- rung 2: Dot and Dario, the private study (Lifeclass Study 2). Non-con, no flip. -------------

label lc_study_two:
    $ vn_enter(bg="lc_room_evening", pc="protesting", pc_tag="lc_pc", cast=[("lc_dot", "crit")], cg="lc_study_pose")
    "Dot drags the stool into the middle of the stand. She turns it so it faces the door."
    lc_dot "\"Over it.\""
    lc_you "\"Over—\""
    lc_dot "\"Over the stool. Chest on the seat. Hands on the legs. Feet apart.\""
    show cg lc_study_strap onlayer cgl
    "She's pulling a latex glove onto her left hand with a snap. From the props cupboard she takes a smooth black strap-on cock on a harness and buckles it round her hips over her apron, as casually as tying the apron."
    lc_dot "\"Private study. You asked for more. This is more.\""
    lc_you "\"I asked for {i}work{/i}— I meant {i}sitting{/i}— Dot, I'm the {i}model{/i}, I don't— that's not—\""
    show cg lc_study_pose onlayer cgl
    "She doesn't argue. She just poses you. A hand on the back of your neck, and you're folded down over the stool, chest on the paint of the seat." with vnfx("shake")
    "Her boot nudges your feet apart. Her hand moves your hands onto the stool legs and presses them there like she's pinning a sheet."
    lc_dot "\"That reads.\""
    lc_you "\"It doesn't {i}read{/i}— let me {i}up{/i}— I'm meant to {i}sit{/i}—\""
    "You push up. Her hand on your neck doesn't move, and you don't either."
    show lc_dario drawing at vn_cast_slot
    "Dario pulls his chair up. An arm's length away. He sets his board on his knee."
    lc_dario "\"Don't mind me.\""
    lc_you "\"Dario— Dario, tell her— don't you {i}dare{/i} draw this—\""
    lc_dario "\"Light's going. If you're doing it, do it, I've got—\""
    lc_dot "\"Hold that.\""
    "He holds it."
    hide lc_dario
    "Dot's gloved fingers come down slick between your cheeks, cold, and find your hole and press."
    lc_you "\"No— not {i}there{/i}— Dot— {i}ahh{/i}—\""
    "And it's easy. That's the thing. That's the worst thing. It's your first time ever and you're yelling no into the stool's paint and your hole opens for her like it's done this every session."
    lc_dot "\"Good. That reads.\""
    show cg lc_study_in onlayer cgl
    "Then the strap-on. The blunt head against you. A push."
    lc_you "\"{i}Ohhh{/i}— no— take it {i}out{/i}— oh {i}god{/i}, it's so— it's so {i}full{/i}—\""
    lc_dot "\"Breathe out.\""
    "She sinks it in, all of it, slow, her hand back on your neck, until her apron's against your new soft ass and you're stretched round it, stuffed, shaking, mouth open on the seat."
    lc_dot "\"Twenty more minutes.\""
    lc_you "\"You can't— not for— {i}ahh{/i}— {i}ahh{/i}—\""
    "She starts: long, slow, even strokes, like she's laying down a ground. Her gloved hand comes round under you and closes on your cock, holding it, not stroking, just holding it like she's checking its weight."
    lc_dot "\"Longer through the hip.\""
    "She pulls your hip back onto her by a hair, and the next stroke goes deeper."
    lc_dot "\"Don't drop the shoulder.\""
    lc_you "\"I'm not {i}posing{/i}— I'm not— {i}ahh{/i}— get it— {i}FUCK{/i}—\""
    lc_dot "\"Shoulder.\""
    "Your shoulder goes back up. You didn't tell it to. She fucks you harder for it. The stool creaks. Your puffy nipples drag on the paint of the seat and every drag makes you squeal."
    hide lc_dot
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Back of the knee's tightening. Arch is beautiful. He's arching. Mouth's open. Cock's leaking on her glove, good, that's the darkest thing on the page, I want that. Keep the mouth open.\""
    lc_you "\"I'm not {i}arching{/i}— shut {i}up{/i}— stop {i}narrating{/i}— stop {i}drawing{/i} it— {i}hnnh{/i}—\""
    show cg lc_study_door onlayer cgl
    "You're facing the door: the frosted window, and the schedule taped on it, and through the paper you can read the biro from here."
    "It's the whole spring. Every session. All the way down the sheet, in Dot's square capitals, the same word in the model column, over and over."
    show screen lc_sheet(["{b}SCHEDULE · SPRING{/b}", "Model: [lc_pc_name]", "Model: [lc_pc_name]", "Model: [lc_pc_name]", "Model: [lc_pc_name]", "Model: [lc_pc_name]", "Model: [lc_pc_name]"])
    "Your name. Every session through spring. Nobody asked you. Nobody said a word."
    hide screen lc_sheet
    lc_you "\"I— I signed up to {i}SIT{/i}— {i}ahh{/i}— I signed up to {i}sit{/i}—!\""
    "Dot thrusts and it punches the words out of you."
    hide lc_dario
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Don't move.\""
    "She doesn't even slow down. You don't move. Your hips do. They push back onto her, and back, and back, and you hear yourself go up an octave."
    lc_you "\"Stop— {i}stop{/i}— oh god, don't— don't {i}stop{/i}— Dot— {i}Dot{/i}, I'm gonna— {i}please{/i}—\""
    show cg lc_study_cum onlayer cgl
    "You come. You can't help it. Untouched except for her hand just holding it, with her strap-on buried to the base and your name all down the door. You go off in her glove, pulse after pulse, and scream into the stool." with vnfx("flash")
    $ lc_enc.pc_orgasms = 1
    "Dot holds the pose through every pulse. Then she lets go of your cock and looks at her glove. It's white to the wrist."
    hide lc_dario
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Good weight.\""
    "She peels the glove off inside out, with your load in it, and drops it in the bin. She's still in you."
    menu:
        "She's still in you."
        "She sets the pose again, timed properly":
            jump lc_study_sex
        "Dot calls time":
            jump lc_study_close

label lc_study_close:
    $ lc.fit = "own"
    $ vn_enter(bg="lc_stairs", pc="flushed", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_stairs onlayer bgl
    $ vn_until(19)
    "Later you walk down the side stairs very carefully, holding the rail, with the envelope in your pocket and your name on every session behind you."
    "On the bus home you sit on one cheek, and your hole keeps clenching on nothing the whole way.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_three

label lc_study_after:
    $ vn_enter(bg="lc_room_evening", pc="flushed", pc_tag="lc_pc", cast=[("lc_dot", "flat")], cg="lc_study_sex_cum")
    if lc_enc.pc_orgasms > 1:
        "You come again over the stool, untouched, yelling no the whole way into it, a thin string onto the drop cloth, and Dot calls it like the end of a pose."
    else:
        "Dot calls time with you shaking and leaking and right on the edge, begging her for you don't know what, and pulls out, and leaves you there."
    hide cg onlayer cgl
    show lc_dot flat at vn_cast_slot
    lc_dot "\"Time. Same next session. Don't be late.\""
    "She unbuckles."
    lc_you "\"Every session? It says every {i}session{/i}— nobody {i}asked{/i} me—\""
    lc_dot "\"It does.\""
    "She goes."
    hide lc_dot
    $ lc.fit = "own"
    $ vn_until(19)
    "You go down the side stairs holding the rail, with your name on every session behind you.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_three

## ---- DAY 3 (Lifeclass Morning 3, Early 3, Session 3) ------------------------------------------

label lc_morning_three:
    $ lc.fit = "own"
    $ vn_enter(bg="lc_bedsit", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_wake_3")
    show cg lc_wake_3 onlayer cgl
    "You wake in the bedsit and lie there looking at your hands. They're not your hands. They're better: slim and soft and long-fingered, the nails like little pink ovals, and when you run them down your own chest they glide, and your puffy nipples go stiff at the first brush."
    lc_you "\"Ohh. No. Stop it.\""
    "To your own hands, which don't."
    hide cg onlayer cgl
    "Your face in the mirror over the sink is softer round the jaw, and your mouth is fuller, and it keeps pouting at you on its own."
    "The session isn't till the afternoon. Your name's on it. Your name's on all of them. You need the cash, and you've worked out one thing in the night: if you're up there first, posed, sitting, the job they're paying you for, then nobody gets to put you over anything."
    "By noon you're at the bus stop with your jeans on and your heart going.\n{size=-5}{color=#ff8fa3}▸ Go in early{/color}{/size}"
    $ vn_until(13)
    jump lc_early_three

label lc_early_three:
    $ lc.fit = "nude"
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_room onlayer bgl
    "The door at the top of the side stairs is unlocked. Nobody's there. Just the skylight and the easels in their horseshoe and the wall of you, across to the window, waiting."
    "You strip at the chair by the door, fast, before anyone can come up the stairs and watch you do it. Then you get up on the stand, naked and smooth and already half hard, and decide how they're going to find you: sitting. Posed. Doing the job."
    menu:
        "How do they find you?"
        "On the stool, knees apart, chin up":
            $ lc.pose = "stool"
        "Leaning back on your hands, ass on the stool's edge":
            $ lc.pose = "lean"
        "Side-on, so they get the line of you":
            $ lc.pose = "side"
    $ vn_until(14)
    jump lc_session_three

label lc_session_three:
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[("lc_tamsin", "laughing")], cg="lc_early_pose")
    show cg lc_early_pose onlayer cgl
    "They come up the stairs in ones and twos with their boards and their bags, and find you already posed."
    if lc.pose == "lean":
        "Leaning back on your hands, ass right on the edge of the stool, everything out. The pastels woman stops in the door and laughs so hard she has to put her bag down."
    elif lc.pose == "side":
        "Side-on, chin up, the whole long line of you to the door. The pastels woman stops in the door and laughs out loud, delighted."
    else:
        "On the stool, knees apart, chin up, cock up, grinning. The pastels woman stops in the door and laughs out loud, delighted."
    lc_tamsin "\"Tamsin. Pastels. That's {i}brilliant{/i}, are you always going to do that?\""
    "She sticks her hand out and then remembers hers is all pink and lilac dust."
    lc_you "\"Yes. I'm the model. I sit. That's what I do. I {i}sit{/i}.\""
    hide cg onlayer cgl
    show lc_bjorn nod at vn_cast_slot
    "Behind her, the big man with the removal-man forearms nods at you like he's nodding at a van."
    lc_bjorn "\"Bjorn.\""
    "He looks at the stool under you for a long, practical moment, and doesn't say anything else."
    hide lc_bjorn
    show lc_milo keen at vn_cast_slot
    "And the quick one, who's got his easel up and a sheet clipped before the others have their coats off."
    lc_milo "\"Milo. Hi. Hi. I've got you from here already. I've lost count already. Hi.\""
    hide lc_milo
    "Dario sits down with his board without a word and starts drawing your cock."
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Fine. Keep it.\""
    "Dot comes in last but one, looks at you posed on the stool, and nods once. She claps."
    $ _lc_c = lc_call(3)
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "[_lc_c]"
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Seated. Weight. Where it sits. What it sits on. Go.\""
    "They go. Tamsin's laughing at something on her own sheet. Dot looks at her."
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Hold that.\""
    "Tamsin holds it, with her lips pressed together and her shoulders shaking."
    show lc_winnie late at vn_cast_slot
    "And then the door bangs, and Winnie falls in with her canvas bag and her coat half off."
    lc_winnie "\"What did I miss?\""
    hide lc_tamsin
    hide lc_winnie
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Everything. He was {i}early{/i}.\""
    "Roz points at you with a stick of charcoal."
    hide lc_winnie
    "You sit. The charcoal goes. You can feel where they're all looking: low. The seat. Your ass on the stool, your thighs on the edge of it."
    show cg lc_seat_grow onlayer cgl
    $ lc_body(3)
    "{color=#ff5fb8}The stool starts to feel narrow.{/color}"
    "{color=#ff5fb8}It's the same stool, the old wobbly painted one, but the seat is getting smaller under you, or you're getting bigger on it, warm and heavy, spreading. Your cheeks are filling out. You can {i}feel{/i} them filling, round and soft and tight-skinned, pushing out over the edges of the seat on both sides.{/color}"
    show lc_pc protesting
    lc_you "\"Oh— oh {i}fuck{/i}— no— oh, my {i}ass{/i}— stop— stop drawing the {i}seat{/i}—!\""
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Hold the pose.\""
    lc_you "\"It's {i}growing{/i}— everybody put your charcoal {i}down{/i}— Roz— {i}Dot{/i}—!\""
    "Every head goes down to every board. You try to stand up off it, and your weight tips forward as it grows behind you, sliding you to the front of the seat, pinning you there."
    "{color=#ff5fb8}Your thighs are swelling against the edge: thick, soft, smooth, pressing together, spilling over the stool's rim like dough over a tin.{/color}"
    lc_you "\"{i}Ahh{/i}— it's so— it's so {i}heavy{/i}— stop it— I can feel it {i}sitting{/i}— I can feel all of it {i}sitting{/i}—\""
    "Your ass is so sensitive now that the paint on the stool feels like a tongue. You wriggle to get off the stool, and the whole of your new bottom wobbles, and a moan comes out of you so loud Milo drops his charcoal."
    lc_you "\"That wasn't— I didn't— {i}stop drawing{/i}—!\""
    hide lc_tamsin
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"It's not reading. The stool. You can't see the stool any more.\""
    hide lc_tamsin
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Then draw what's on it.\""
    "They draw what's on it."
    show cg lc_stool_skip onlayer cgl
    "By the break, the stool has given up. It's creaking every time you breathe, one leg's lifting off the stand, and your ass is hanging over it on all sides, soft and huge and new."
    "Bjorn puts his board down, goes out the door and down the side stairs without a word. Not long after, he comes back up with a new stool on his shoulder: wide, solid, a proper round seat like a piano stool, still with the price label on it."
    "He puts it on the stand. He takes the old one down the stairs, and through the skylight you hear it go in the skip outside the café. He comes back up and picks up his charcoal."
    lc_you "\"Bjorn, you didn't have to—\""
    "Bjorn shrugs."
    show cg lc_handprint_3 onlayer cgl
    "Roz moves you onto the new stool by your hip, and when she lets go there's a black handprint halfway round you, a hand that used to meet itself and now barely gets halfway."
    hide lc_tamsin
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"{i}Fuck{/i}.\""
    "Delighted."
    show cg lc_wall_3 onlayer cgl
    "The wall's gone round the corner. Sheets of you, seated, heavy, all ass and thighs, are pinned past the window and round onto the north wall, over the radiator, curling a little at the edges in the heat. None of it's Dario's. Dario's started a second folder.\n{size=-5}{color=#ff8fa3}▸ Back on the stool{/color}{/size}"
    $ vn_pass(60)
    jump lc_shifts_three

## ---- rung 3: the class in shifts (Lifeclass Shifts 3). Non-con, flips mid-Bjorn. -----------------

label lc_shifts_three:
    $ vn_enter(bg="lc_room", pc="protesting", pc_tag="lc_pc", cast=[("lc_milo", "keen")], cg="lc_shifts_milo")
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change of pose. Over the stool. Milo, you're first.\""
    lc_you "\"First for {i}what{/i}—\""
    show cg lc_shifts_milo onlayer cgl
    "Milo's already out of his jeans. He's quick at everything. He's up on the stand behind you before you've got off the stool, and Bjorn's big hand is on your shoulder, steering, and you're bent over Bjorn's new stool, chest on the wide round seat, your huge new ass in the air." with vnfx("shake")
    lc_you "\"I'm the {i}model{/i}— I'm meant to {i}SIT{/i}— I came early to {i}sit{/i}—!\""
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"You did. Now you're over it. Milo.\""
    hide lc_dot
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Best seat in the co-op. Sorry. Sorry. Still my turn though—\""
    "He's holding your ass in both hands like he can't believe his luck."
    lc_you "\"Don't you {i}dare{/i}— Milo— {i}don't{/i}—\""
    "He does. Your hole takes him like it's been waiting all afternoon, open and slick and hungry, while your mouth yells no at the floorboards."
    lc_you "\"{i}Ahh{/i}— get {i}out{/i}— get— {i}ahh{/i}— why's it so {i}easy{/i}—\""
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Twenty more minutes. Then change.\""
    "She checks her watch. Nobody else stops drawing. That's what gets you. Milo's pounding you over Bjorn's new stool and the charcoal's still going all round the horseshoe, and Dot's walking round behind the easels saying \"Watch the foreshortening on the thigh.\""
    lc_you "\"Stop {i}drawing{/i} this— somebody— put the charcoal {i}down{/i} and pull him {i}off{/i}—!\""
    show cg lc_shifts_hands onlayer cgl
    "And under you, your cock: hanging, hard, drooling on the stool, and Tamsin grabs it. She's on her knees by the stand, laughing, pastel dust all over her face, and she wraps her lilac hand round it and pumps it without a word to you."
    hide lc_milo
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Give it {i}here{/i}—\""
    "A black hand and a lilac hand yanking at your cock at once, fighting over it like the last good brush, and then Tamsin gives up fighting and just puts her mouth on the tip."
    lc_you "\"{i}Ohh{/i}— no— not {i}both{/i} of you— let {i}go{/i}— {i}GOD{/i}—\""
    "Aurelio comes up on the stand. She doesn't touch your cock. She doesn't touch anything but your shape: her clay-grey hands move your hip a little higher, your knee a little wider, your back a little deeper, and hold them there however hard you shove."
    hide lc_milo
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    "Milo hits deeper for it, and you scream. He comes in you with a whoop of pure joy, deep, buried to the root."
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change.\""
    lc_you "\"No— no more {i}change{/i}— I'm getting {i}up{/i}—\""
    show cg lc_shifts_bjorn onlayer cgl
    "Bjorn's next. Big, blunt, practical. He gets a grip on your hips like he's lifting a sofa, holds you down on the seat, and pushes in in one long, slow, unstoppable shove that fills you right up." with vnfx("shake")
    lc_you "\"{i}HHAAH{/i}— Bjorn— {i}Bjorn{/i}, get {i}out{/i}, it's so {i}big{/i}—!\""
    hide lc_milo
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Stop wriggling, you'll have the stool over. Solid.\""
    "You don't know if he means you or the stool. He fucks you like he's doing a job properly. The new stool doesn't even creak. Your ass slaps against him, rippling, and somewhere in the yelling your back has started arching. On its own."
    lc_you "\"I'm not— that's not me— stop drawing me {i}arching{/i}—!\""
    hide lc_milo
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"It's round the corner! It's on the north wall, Dot, look, it's on the fucking {i}radiator{/i}—! And not one of them's Dario's!\""
    "Still on her knees at your cock, twisting round to look at the wall."
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Dario. Pin something.\""
    hide lc_milo
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not for sale.\""
    "Without looking up, drawing your cock in Roz's black fist."
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"That's not what I—\""
    "Dario just keeps drawing. And Bjorn hits something deep in you, and keeps hitting it, and it all goes."
    show lc_pc flushed
    lc_you "\"...Fine. {i}FINE{/i}. Draw it— draw {i}ALL{/i} of it— just nobody {i}STOP{/i}—! {i}Harder{/i}— Bjorn— {i}harder{/i}—!\"" with vnfx("shake")
    "You stop shoving the hands off you. You grab the stool legs and push back onto him. Bjorn grunts and gives it to you, and comes in you, slow and enormous, and holds you on him while he does it."
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Change.\""
    hide lc_aurelio
    hide lc_bjorn
    hide lc_dario
    hide lc_dot
    hide lc_roz
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Me again? Is it me again?\""
    lc_you "\"{i}Yes{/i}— get {i}in{/i}— fuck me {i}stupid{/i}—!\""
    show cg lc_shifts_cum onlayer cgl
    "Winnie, who's only just got her coat off, shoves Tamsin and Roz both out of the way and gets her mouth on your cock. Tamsin gets her hand round the base, Roz grabs your balls in her black fist and squeezes, Milo slams into you, and you come."
    "You come so hard your eyes cross. You pull off Winnie's mouth at the last second without meaning to and it goes everywhere, and most of it goes across Roz's face, right through the charcoal, a white stripe from her chin to her eyebrow." with vnfx("flash")
    hide lc_milo
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"{i}Fuck{/i}.\""
    "Very pleased. Milo comes in you a second time, babbling."
    hide lc_milo
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\""
    "You slide off the stool onto the drop cloth and lie there, dripping, panting, still moaning on every breath. Bjorn looks down at the new stool. He looks at your ass. He looks at the stool again, thoughtfully."
    hide lc_milo
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Bigger stool.\""
    show cg lc_jeans_3 onlayer cgl
    "It's when you go to get dressed that you find out. Your jeans won't go on. Not over your thighs. Not past your knees. You hop, you tug, you lie on the floor and kick, and the denim stops at mid-thigh and will not go one hair further."
    show lc_winnie laughing at vn_cast_slot
    "Winnie takes them off you, holds them up against your thigh, and laughs. The leg of them's half as wide as you are now."
    lc_winnie "\"Oh, love. Nothing you came in is going to close.\""
    "Your pants don't either. Your shirt still fits. That's all."
    hide lc_winnie
    menu:
        "Dot looks at her watch."
        "Dot calls another round, Milo first":
            jump lc_shifts_sex
        "Home in a drop cloth":
            jump lc_bus_three

label lc_shifts_after:
    $ vn_enter(bg="lc_room", pc="flushed", pc_tag="lc_pc", cast=[], cg="lc_shifts_sex_cum")
    if lc_enc.partner_came:
        "They fill you up again, one after the other, and you lie over Bjorn's stool with your enormous new ass in the air, leaking, still begging for whoever's next, while the charcoal scratches on."
    else:
        "Milo pulls out and comes across the small of your back and the top of your new ass, and Bjorn after him, and you lie over the stool glazed and grinning."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\"\n{size=-5}{color=#ff8fa3}▸ Home in a drop cloth{/color}{/size}"
    jump lc_bus_three

label lc_bus_three:
    $ lc.fit = "cloth"
    $ vn_enter(bg="lc_bus", pc="flushed", pc_tag="lc_pc", cast=[], cg="lc_bus_cloth")
    $ vn_until(18)
    show cg lc_bus_cloth onlayer cgl
    "You go home on the bus in your shirt and a paint-spattered drop cloth knotted round your waist like a sarong, with your jeans rolled up under your arm and your new ass taking up a seat and a half."
    "People look. Of course they look. A man with shopping bags looks so long he misses his stop. Every time the bus goes over a bump the whole of you {i}wobbles{/i} on the seat, and something in you clenches on what they left there, and you bite your lip so you don't moan out loud on the bus."
    lc_you "\"Life model.\""
    "You tell the woman next to you, who didn't ask. It comes out high and breathless."
    hide cg onlayer cgl
    show bg lc_bedsit onlayer bgl
    "In the bedsit you lie face-down on top of the covers, because that's the only way you fit now, and reach back and squeeze yourself with both hands, and moan into the pillow.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_four

## ---- DAY 4 (Lifeclass Morning 4, Session 4, Offer 4) ----------------------------------------------

label lc_morning_four:
    $ lc.fit = "sweats"
    $ vn_enter(bg="lc_bedsit", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_sweats_4")
    "You wake in the bedsit and roll over, and your ass rolls over a moment after you, heavy and soft, and you lie there staring at the ceiling with both hands on it."
    "Nothing you own closes. You try everything: the other jeans, the work trousers, the shorts from the bottom of the drawer. Up to mid-thigh and no further, every time."
    show cg lc_sweats_4 onlayer cgl
    "In the end it's the sweats, the big grey ones you sleep in, and they go on, just. They're tight over your thighs and stretched shiny over your ass, and they ride up between your cheeks on the very first step."
    lc_you "\"Oh, {i}no{/i}. Oh, that's {i}obscene{/i}.\""
    "Looking over your shoulder in the mirror. You can't stop squeezing it. You squeeze it at the kettle. You squeeze it at the bus stop. A woman in the bus shelter watches you do it, and you squeeze it at her too.\n{size=-5}{color=#ff8fa3}▸ Catch the bus to Cliff Street{/color}{/size}"
    $ vn_until(14)
    jump lc_session_four

label lc_session_four:
    $ lc.fit = "nude"
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[], cg="lc_chest_study")
    "You peel the sweats off at the chair by the door, and the whole room turns to watch your ass come out of them, and Tamsin claps."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Stand. Face front. Arms down.\""
    $ _lc_c = lc_call(4)
    show lc_dot crit at vn_cast_slot
    lc_dot "[_lc_c]"
    show cg lc_chest_study onlayer cgl
    "Everybody looks at your chest. It's a nice enough chest: smooth, flat, with your puffy pink nipples sitting on it. You stand there with your arms rigid by your sides, braced, and the charcoal scratches, and you wait for the tingle."
    lc_you "\"Please don't. Please. Not that. Draw something else.\""
    "It doesn't come. You wait some more. Nothing. Not a flicker. Your nipples are exactly as puffy as they were when you came up the stairs. Your chest is just a chest."
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Huh.\""
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"It's not reading.\""
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"It's reading fine, it's just {i}flat{/i}. Fuck's sake. What do I shade? There's nothing to shade.\""
    "Dot walks the horseshoe. She looks at every board. She looks at you, top to bottom. She stops at the chest the way you'd stop at a canvas where the paint's gone on and not stuck."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"The chest study didn't take.\""
    show screen lc_sheet(["{b}SCHEDULE · SPRING{/b}", "Model: [lc_pc_name]   {i}SKIP.{/i}"])
    "She goes to the door, takes the pen on its string, and in the session column of the schedule, next to your name, writes something in her square capitals. You can read it from the stand. {i}SKIP.{/i}"
    hide screen lc_sheet
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Contrapposto. Hips. Weight on one leg. Aurelio.\""
    hide cg onlayer cgl
    show lc_aurelio intent at vn_cast_slot
    "Aurelio puts down her clay and comes up on the stand. She's tall. Up close she smells like wet clay and turps."
    show cg lc_hips_hands onlayer cgl
    "She takes your hips in both her grey hands, from behind, and {i}moves{/i} them: the weight onto your right leg, the left knee forward, the hip kicked out, like she's setting an armature. You try to step out of it. Her hands put you back."
    lc_aurelio "\"There.\""
    "Her thumbs press, and pull."
    $ lc_body(4)
    "{color=#ff5fb8}And it {i}goes{/i}. Under her hands, exactly under her thumbs, your hips are widening. You can feel the bones of you easing outward, slow and warm and enormous, the hip she kicked out rounding into a curve that wasn't there a moment ago.{/color}"
    show lc_pc protesting
    lc_you "\"No— no, {i}stop{/i}— Aurelio, let {i}go{/i}— my {i}hips{/i}— everybody stop drawing the {i}hip{/i}—!\""
    lc_aurelio "\"More.\""
    "{color=#ff5fb8}More. Your waist pulls in above them, tight, nipped, like someone's drawn a belt in and in, until your hips flare out from it in a line so curvy the whole horseshoe goes silent and then scratches twice as fast.{/color}"
    lc_you "\"Dot— {i}Dot{/i}, tell them to stop— it's happening {i}again{/i}, can't you {i}see{/i} it—!\""
    hide lc_aurelio
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Longer through the hip.\""
    "To the room. Your ass sits higher and rounder on them. Your thighs swing wider apart."
    lc_you "\"{i}Ahh{/i}— stop— I'm so {i}wide{/i}— put it {i}down{/i}, put the charcoal—\""
    "{color=#ff5fb8}And your voice cracks, right in the middle of it. It slides up, lighter, softer, breathier, and stays there.{/color}"
    lc_you "\"—put the charcoal— oh my god, my {i}VOICE{/i}— what did you {i}do{/i} to my—!\""
    "It comes out high and sweet and loud, and you clap your slim hand over your mouth, and your lips are so soft under your own palm that you moan into it, and the whole room draws you moaning."
    "Your chest is exactly what it was."
    hide lc_bjorn
    hide lc_dot
    hide lc_milo
    hide lc_roz
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    "She lets go, and goes back to her clay."
    hide lc_aurelio
    hide cg onlayer cgl
    "The room re-blocks. Everybody shifts their easels sideways to get the hip, all at once, a great scraping of legs."
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Now {i}that{/i} reads.\""
    "Dot stops behind Dario. He's clipped on a fresh sheet already. Every sheet under it is your cock."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Dario. A whole folder of it, in a chest week. Every session. What is it about that one thing?\""
    "Loudly, so the room hears. The whole room stops drawing to hear the answer."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"I'd suck it for reference if the light were better.\""
    "He doesn't look up, and goes back to work. Tamsin laughs so hard she has to sit on the floor."
    show lc_tamsin laughing at vn_cast_slot
    lc_tamsin "\"Can I at least {i}buy{/i} one off you, for my {i}wall{/i}—\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not for sale.\"\n{size=-5}{color=#ff8fa3}▸ Hold the hip{/color}{/size}"
    $ vn_pass(60)
    jump lc_offer_four

label lc_offer_four:
    $ vn_enter(bg="lc_room", pc="apologetic", pc_tag="lc_pc", cast=[("lc_dot", "flat")], cg=None)
    show bg lc_room onlayer bgl
    "You're on Bjorn's wide stool now, one hip cocked, holding it. Bjorn's holding up a receipt and opening his mouth."
    lc_dot "\"Hold that.\""
    "Bjorn holds it."
    show lc_dot flat at vn_cast_slot
    show cg lc_vote onlayer cgl
    "Then Dot puts down her stick of charcoal and turns round to face the horseshoe. Not you. The room."
    lc_dot "\"Housekeeping. I can close the open call. Tonight. Get a professional in from the agency for the rest of spring. He keeps the cash, all of it, and walks out clean.\""
    "She doesn't look at you."
    lc_dot "\"Or we keep him. Room's call.\""
    "The room's gone quiet. Roz has stopped. Even Dario's charcoal has stopped."
    "You're naked on a stool with your new hips cocked and your cock up and your voice gone high, and nobody's asked you anything, and you open your mouth."
    menu:
        "Nobody's asked you."
        "Close it. Please. CLOSE it.":
            $ lc.answer = "please"
        "Get the agency in, I'll go quietly, I swear":
            $ lc.answer = "agency"
        "Dot, I'm ASKING you, close the call!":
            $ lc.answer = "asking"
    $ vn_pass(5)
    jump lc_aurelio_four

## ---- rung 4: the vote, then Aurelio (Lifeclass Aurelio 4). MANDATORY; non-con, flips. ---------------

label lc_aurelio_four:
    $ vn_enter(bg="lc_room", pc="protesting", pc_tag="lc_pc", cast=[("lc_dot", "flat")], cg="lc_vote")
    if lc.answer == "agency":
        lc_you "\"Get the agency in. Please. Get a professional. I'll go quietly, I'll go {i}right now{/i}, I swear, I won't even— just close it. {i}Close{/i} it.\""
    elif lc.answer == "asking":
        lc_you "\"Dot. Dot, I'm {i}asking{/i} you. I'm {i}ASKING{/i}. Close the call!\""
        "Your new high voice cracks right up off the top of it."
    else:
        lc_you "\"Close it. Please. {i}Please{/i}. Close it. {i}CLOSE{/i} it.\""
    lc_dot "\"Hands up to close it.\""
    "She doesn't look at you. Nobody moves."
    lc_dot "\"Hands up to keep him.\""
    show cg lc_vote_hands onlayer cgl
    "Every hand in the room goes up. Roz's black one. Tamsin's lilac one, and she's laughing. Bjorn's, with the receipt still in it. Milo's, both of his. Aurelio lifts a clay-grey hand off her clay without looking up."
    "Dario doesn't put his hand up; he doesn't stop drawing long enough. Winnie, who's only just come in, puts hers up without asking what for."
    lc_you "\"No— that's not— I'm the one who— nobody asked {i}me{/i}—!\""
    "Roz has already ripped the old sheet off her board and clipped on a clean one. She's drawing you before you've finished saying it."
    "Dot nods, picks up her charcoal, and goes back to walking the horseshoe like nothing happened."
    hide cg onlayer cgl
    "At the end, packing her bag, not looking at anyone, she says one sentence, flat."
    lc_dot "\"The co-op's been behind on the rent since winter. A full wall, sold, clears it.\""
    "Nobody answers. Nobody ever brings it up again."
    hide lc_dot
    "People are packing. Easels folding. Tamsin's looking for her pink. You get off the stool fast, and bend to grab your sweats off the chair by the door, and your huge new ass goes up in the air in front of the whole room."
    show cg lc_aurelio_reveal onlayer cgl
    "A pair of clay-grey hands lands on it."
    "Aurelio. Behind you. She's closed the gap without a sound, and she's pressed up against you from behind, and there's something against the cleft of your ass, heavy, hot, hard, lying along you from your hole right up past the small of your back."
    "You look round. Aurelio has a cock. It's enormous: out of the front of her clay-smeared overalls, thick as your wrist, long as your forearm, dark and veined and dripping on your spine. That's all. Nobody says a word about it. Nobody asks."
    lc_you "\"{i}Oh{/i}. No. No, no, {i}no{/i}, I'm {i}going{/i}, I've got my sweats, I'm—\""
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"Stay.\""
    "The room stops packing."
    show cg lc_aurelio_bent onlayer cgl
    "She bends you over Bjorn's stool with one hand on the back of your neck and one on your hip, the way she'd turn clay on a wheel. You shove back against her hand. It doesn't move." with vnfx("shake")
    "The fat head of her presses your hole. Your hole, the most sensitive it's ever been, opens round it like a mouth while you yell at it not to."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"Build it out.\""
    "She pushes."
    menu:
        "She's pushing in."
        "Grab the stool legs":
            $ lc.grip = "legs"
        "\"Aurelio, WAIT—\"":
            $ lc.grip = "wait"
        "Bite the drop cloth":
            $ lc.grip = "cloth"
    jump lc_aurelio_sex

label lc_aurelio_after:
    $ vn_enter(bg="lc_room", pc="flushed", pc_tag="lc_pc", cast=[], cg="lc_aurelio_flip")
    if lc.grip == "wait":
        "\"Wait\" never got her to wait. By the end you'd stopped saying it."
    elif lc.grip == "cloth":
        "There are teeth marks in the drop cloth, and a wet patch where you stopped biting it and started moaning into it instead."
    else:
        "Your fingers are still locked round the stool legs, white-knuckled, holding on for more."
    show cg lc_aurelio_flip onlayer cgl
    "She doesn't soften. She flips you: one hand under your knee and one under your back, and you're on the stool on your back with your hips in the air and your legs over her arms, and she's back in you before you've drawn breath."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    lc_you "\"{i}AHH{/i}— Aurelio— oh god, it's {i}enormous{/i}— it's so {i}big{/i}, it's the biggest— I'm so {i}full{/i}—\""
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"More.\""
    show cg lc_aurelio_crowd onlayer cgl
    "Nobody's packing now. Tamsin and Winnie are on your cock at once, Tamsin laughing round the head, Winnie's hand pumping the shaft. Bjorn's on one side of the stool and Milo's on the other, both of them hard and stroking, and Dario's on his chair an arm's length off, drawing your cock between the women's mouths, narrating every line out loud."
    show cg lc_cork onlayer cgl
    "Dot walks to the wall. Calmly, one at a time, she starts taking the chest sheets down. All of them. The whole session's worth of flat chest."
    "Roz goes with her, unpinning, swearing at every single one. Sheet after sheet comes down, and behind them, for the first time all week, there's cork: a bare band of it, brown and pinholed, right across the middle of the wall."
    show cg lc_aurelio_crowd onlayer cgl
    "Aurelio fucks you in long, slow, enormous strokes that move your whole body up the stool and back. Your new wide hips are in her hands, and she's still shaping them."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"Build it out.\""
    "You come untouched under her, with Winnie's hand and Tamsin's mouth both on your cock and doing nothing to it you'd call touching. It just goes, and goes, and you scream." with vnfx("flash")
    "Milo comes across your chest. Bjorn comes across your face, your lips, into your open mouth."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\""
    "From the wall, with an armful of chest sheets. Aurelio slows."
    lc_you "\"{i}No{/i}— don't— not {i}time{/i}— {i}more{/i}. Build it {i}out{/i}— {i}MORE{/i}—!\""
    "In your high new voice, covered, full, shaking, shoving back onto her."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"More.\""
    "She agrees, and doesn't stop."
    hide cg onlayer cgl
    $ lc.fit = "sweats"
    ## PIN ONE BACK UP's fork (the alternate route; owner, 2026-11-13): pinned.rpy
    call lc_pin_fork
    $ vn_until(20)
    "It's dark when you get down the side stairs, and your sweats are on inside out, and you've got cum drying in your hair, and you're humming.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_five

## ---- DAY 5 (Lifeclass Morning 5, Session 5, Flat File 5): consensual from here --------------------

label lc_morning_five:
    $ lc.fit = "sweats"
    $ vn_enter(bg="lc_bedsit_rain", pc="wanting", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_bedsit_rain onlayer bgl
    lc_you "\"Morning.\""
    "To the window. Your voice comes out high and sweet, and you grin."
    "It's raining. Proper rain, the kind that makes everybody on Cliff Street dive into the nearest café."
    if lc.pinned:
        $ lc.grown = 1
        "{color=#ff5fb8}In the mirror over the sink there's a person with a soft jaw and fat pink lips and hips like a bracket, and a waist you could get your slim hands nearly round, and a chest. An actual chest: two small soft swells under the puffy nipples that weren't there when you went to bed.{/color}"
        lc_you "\"Sorry. Sorry. It's the soup.\""
        "The café's soup. You've had it every day this week, and it's very creamy. You apologise to your chest again and zip the hoodie up over it, and it zips, just."
    else:
        "In the mirror over the sink there's a person with a soft jaw and fat pink lips and hips like a bracket, and a waist you could get your slim hands nearly round, and a chest that's exactly what it was on the first day, puffy nipples and nothing else."
    "You turn round. You look over your shoulder. You laugh out loud. The sweats go on, just about. Over the hips they're a fight.\n{size=-5}{color=#ff8fa3}▸ Catch the bus in the rain{/color}{/size}"
    $ vn_until(14)
    jump lc_session_five

label lc_session_five:
    $ vn_enter(bg="lc_street_rain", pc="wanting", pc_tag="lc_pc", cast=[("lc_bjorn", "practical")], cg="lc_skip_5")
    show cg lc_skip_5 onlayer cgl
    "At the bottom of the side stairs, in the rain, Bjorn is putting Bjorn's stool in the skip."
    "The wide one. The one he bought. It goes in on top of the old one, with a clang. He looks at you coming up the street in your straining sweats, wet through, ass first."
    lc_bjorn "\"Bigger stool.\""
    "He goes up the stairs ahead of you with a new one on his shoulder, wider than the last, with a cushion on top."
    hide cg onlayer cgl
    show bg lc_room onlayer bgl
    "The café's heaving: every table, every stool, steamed windows, the smell of wet coats. Someone's been sent up the side stairs because there's nowhere to sit: a man in a good wet coat, standing at the back of the life room with his hands in his pockets, looking at the wall."
    show cg lc_wall_5 onlayer cgl
    if lc.pinned:
        "The wall's floor to ceiling now. Sheets of you, seated, standing, hips, ass, thighs, overlapping like roof tiles, pinned right up into the window frame. Except for the band of cork across the middle, where the chest sheets were: bare, but for the one you pinned back up, on its own, with a pin in each corner."
    else:
        "The wall's floor to ceiling now. Sheets of you, seated, standing, hips, ass, thighs, overlapping like roof tiles, pinned right up into the window frame. Except for the bare band of cork across the middle, where the chest sheets were."
    $ lc.fit = "nude"
    show cg lc_back_pose onlayer cgl
    "You don't wait for Dot. You strip at the chair, go straight up on the stand, turn your back on the room, put your hands on the new stool and your weight on one leg and your huge ass out."
    lc_you "\"Look at me. Go on.\""
    "Over your shoulder. Dot comes in, shaking out her umbrella, sees you posed, and doesn't even break stride."
    $ _lc_c = lc_call(5)
    hide lc_bjorn
    show lc_dot crit at vn_cast_slot
    lc_dot "[_lc_c]"
    hide lc_bjorn
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Don't drop the shoulder.\""
    "You don't. The charcoal goes. The door bangs: Winnie, soaked, her canvas bag streaming."
    hide lc_bjorn
    show lc_winnie late at vn_cast_slot
    lc_winnie "\"What did I miss?\""
    hide lc_bjorn
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Him starting it.\""
    hide lc_bjorn
    show lc_winnie late at vn_cast_slot
    lc_winnie "\"Again?\""
    hide lc_bjorn
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Hold that.\""
    "About Winnie's dripping umbrella, which Winnie holds, out of the way, dripping."
    show cg lc_back_grow onlayer cgl
    $ lc_body(5)
    "{color=#ff5fb8}It starts in your thighs: a slow warm swell from the knee up, the insides of them pressing together, softer, heavier. Then your ass. It fills, rounder, higher. It pushes back at the room like it heard them, swelling out over the backs of your thighs in a heavy shelf, so big the back study stops being a back study at all.{/color}"
    lc_you "\"{i}Ohhh{/i}— oh, it's— it's {i}more{/i}— there's {i}more{/i} of it— look at it, {i}look{/i} at it—!\""
    hide lc_bjorn
    show lc_milo keen at vn_cast_slot
    lc_milo "\"I can't see your back. There's no back. It's just—\""
    hide lc_bjorn
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Re-block from the side.\""
    if lc.pinned:
        $ lc.grown = 2
        "{color=#ff5fb8}And under you, against the stool, something else is filling. Your chest. Rounder and heavier with every scratch from the back of the room, where Roz has turned her easel the wrong way round and is drawing the front of you instead, swearing, and pinning every sheet into the band of cork as she finishes it.{/color}"
        hide lc_bjorn
        show lc_dot crit at vn_cast_slot
        lc_dot "\"The chest's coming through.\""
        "Flatly, to the wall, the way she'd say a value was coming through. Nobody says anything else about it."
    "The whole horseshoe picks up and moves round to the side, easels scraping, to get the profile of you, which is mostly ass now: a huge soft curve that starts at your nipped waist and goes out, and out, and down into thighs that touch all the way to the knee."
    "{color=#ff5fb8}Your slim hands on the stool are getting slimmer, and when you lick your lips they're fuller round every word, fat and pink and wet.{/color}"
    lc_you "\"Feel— everything— my {i}mouth{/i}— my {i}ass{/i}— I can feel the {i}air{/i} on it— and between my thighs, it's so {i}tight{/i} between my thighs—\""
    hide lc_bjorn
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"Now {i}that{/i} reads from the fucking {i}street{/i}.\""
    show cg lc_handprint_5 onlayer cgl
    "She grabs your ass to turn you a little more to the light, and it takes both her hands, and when she lets go there's a black handprint on each side of you, and they look small."
    if lc.pinned:
        call lc_pin_sink
        $ vn_enter(bg="lc_room", pc="wanting", pc_tag="lc_pc", cast=[("lc_bjorn", "practical")], cg="lc_red_dot")
    show cg lc_red_dot onlayer cgl
    if lc.pinned:
        "The man in the wet coat walks up to Dot at the break and says something quietly. Dot nods. She takes a sheet of little red stickers out of her apron and sticks one on the corner of one of Roz's chest sheets in the band. A red dot. The first one."
    else:
        "The man in the wet coat walks up to Dot at the break and says something quietly. Dot nods. She takes a sheet of little red stickers out of her apron and sticks one on the corner of one of Roz's drawings on the wall. A red dot. The first one."
    hide lc_bjorn
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Sold.\""
    "Flatly, to nobody. Dario has stopped using folders. He's brought a big cardboard archive box, and it's already half full.\n{size=-5}{color=#ff8fa3}▸ Climb up on the flat file{/color}{/size}"
    $ vn_pass(90)
    jump lc_flatfile_five

label lc_flatfile_five:
    $ vn_enter(bg="lc_room", pc="wanting", pc_tag="lc_pc", cast=[], cg="lc_flatfile_come")
    show cg lc_flatfile_come onlayer cgl
    "The flat file's the big map cabinet at the end of the room: wide drawers full of paper, a long flat top at hip height. You climb up on it before Dot's even back from the sink."
    "Knees and elbows, face-down, ass up to the ceiling, your thighs pressed together and your cock hanging under you. You look back at the room over your shoulder."
    if lc.pinned:
        "Your new chest squashes out against the cabinet top under you, soft and full, and Roz, at her easel, says \"fuck's sake\" and starts a new sheet."
    lc_you "\"Come get me.\""
    "Nobody waits for Dot."
    show cg lc_flatfile_aurelio onlayer cgl
    "Aurelio's first. She doesn't say anything. She's behind you on the flat file's edge, her overalls open, and the enormous head of her presses your hole, and your greedy new hole {i}pulls{/i} her in."
    lc_you "\"{i}AHH{/i}— yes— {i}yes{/i}— Aurelio— all of it— {i}all{/i} of it—!\""
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"More.\""
    "She gives you more until the flat file rocks on its feet, and comes in you deep and slow, and pulls out, and steps back to look at the shape of you with her head on one side."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    show cg lc_flatfile_bjorn onlayer cgl
    "Bjorn's next. He gets a grip on your hips, lines up, pushes, and slips. Your ass is so slick and so big he misses completely, and his cock slides down under your hole, between your thighs, right into the soft clamp of them."
    "And stays there. You squeeze, on instinct. Your thighs close round him like a fist."
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"{i}OH{/i}. Oh, he's— Dot, he's fucking me with his {i}thighs{/i}— are you {i}seeing{/i} this— nobody's ever done that to me with their {i}thighs{/i}—!\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"I see it.\""
    lc_you "\"Squeeze— I'm— {i}squeezing{/i}— can you feel— oh god, they're so {i}soft{/i}, I didn't know they could—\""
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"They {i}hold{/i}! They just {i}hold{/i}!\""
    "He shouts it to the room, sawing between your thighs. The man in the wet coat at the back has taken his hands out of his pockets. He doesn't come closer. He watches."
    "Bjorn comes between your thighs, hot and thick, painting the insides of them." with vnfx("flash")
    show cg lc_flatfile_queue onlayer cgl
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Best seat in the co-op, best seat in the {i}building{/i}—\""
    "Milo. Of course Milo. He's in you before Bjorn's stepped back, grinning, pounding."
    "And under you, your cock, hanging over the edge of the flat file, gets a queue: Roz first, black fist. Tamsin next, laughing, lilac fingers. Winnie, still damp from the rain, with her mouth. And then Dot."
    "Dot crouches. She takes your cock in her bare hand, lifts it, weighs it, turns it to the light like a brush she's thinking of buying."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Good weight. Placement's sloppy.\""
    lc_you "\"{i}Placement{/i}—?!\""
    "She lets go. Milo slams in. You come untouched, all over the front of the flat file's drawers, screaming, and Milo comes in you with a whoop." with vnfx("flash")
    "The man in the wet coat clears his throat. He's standing by Dario's chair, looking into the archive box."
    lc_voice "\"Those. I'll give you triple what she got for the other one. For the lot.\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not for sale.\""
    "Without looking up."
    lc_you "\"Do I get a cut?\""
    "Upside down, from the flat file, full of Milo. Nobody answers you. The man in the wet coat shrugs, buys another of Roz's on the way out, and goes back down into the rain. Dot sticks another red dot on the wall."
    menu:
        "The room's still looking at you."
        "Again, Bjorn's thighs first":
            jump lc_flatfile_sex
        "Home in the rain":
            jump lc_flatfile_close

label lc_flatfile_close:
    $ lc.fit = "sweats"
    $ vn_enter(bg="lc_bus", pc="wanting", pc_tag="lc_pc", cast=[], cg=None)
    show bg lc_bus onlayer bgl
    $ vn_until(19)
    "You go home on the bus with your sweats gone see-through at the thighs and your mouth tasting of Winnie's lip balm, singing under your breath in your new high voice.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_six

label lc_flatfile_after:
    $ vn_enter(bg="lc_room", pc="flushed", pc_tag="lc_pc", cast=[], cg="lc_flatfile_sex_cum")
    "They finish with you one after another, between your thighs and in you, and you lie on the flat file glazed from the waist down, laughing into the drawers."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Time.\""
    $ lc.fit = "sweats"
    $ vn_until(19)
    "You go home in the rain singing in your new high voice.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump lc_morning_six

## ---- DAY 6, the show (Lifeclass Morning 6, Stairs 6, Show 6) --------------------------------------

label lc_morning_six:
    $ lc.fit = "sweats"
    $ vn_enter(bg="lc_bedsit", pc="wanting", pc_tag="lc_pc", cast=[], cg="lc_text_6")
    show cg lc_text_6 onlayer cgl
    "You wake in the bedsit. There's a text from Dot. It's the longest one she's ever sent."
    show screen lc_sheet(["{i}No session today. Show tonight, downstairs in the café. The wall's coming down and going up again on their walls. Come at teatime. Wear something. D.{/i}"])
    lc_you "\"Wear {i}what{/i}?\""
    hide screen lc_sheet
    show cg lc_sweats_6 onlayer cgl
    "The sweats. It's only ever the sweats. They go on with a fight and a lot of hopping, and they stop being sweats somewhere round your hips."
    if lc.pinned:
        "The hoodie doesn't zip any more. It hangs open either side of your chest, and you apologise to it twice, sorry, sorry, and blame the fixative spray, which you've been breathing all week. Fixative's got all sorts in it."
    "Over your ass they're gaping, the waistband cutting into the top of a shelf of soft flesh that just goes on, and the seams down the outsides of your thighs are see-through with stretch."
    lc_you "\"It's fine. It's {i}fine{/i}. It's an art show.\""
    "Grinning at the mirror. It's a beautiful day. Warm. The kind where every café on Cliff Street props its doors open.\n{size=-5}{color=#ff8fa3}▸ Catch the bus to the show{/color}{/size}"
    $ vn_until(17)
    $ vn_pass(30)
    jump lc_stairs_six

label lc_stairs_six:
    $ vn_enter(bg="lc_cafe_show", pc="wanting", pc_tag="lc_pc", cast=[], cg="lc_show_wall")
    show cg lc_show_wall onlayer cgl
    "The Ocean Breeze has its doors wide open onto Cliff Street, and it's packed, and on every wall of it, floor to ceiling, between the menus and the coffee machine, is you."
    "Seated, standing, hips, ass, thighs. Smooth and soft and getting bigger from left to right round the whole room, so that walking in through the door is like watching yourself grow. There are people with wine in plastic cups standing in front of your ass. There's a red dot on every sheet."
    if lc.pinned:
        "And the wall behind the coffee machine is your chest, start to finish: Roz's band of sheets, from the one you pinned back up on its own to yesterday's last, getting bigger left to right. Red dots on all of them."
    "Every sheet but one."
    show cg lc_show_till onlayer cgl
    "You look for it, and there it is, by the till, pinned on its own: a cock, hard, from the left, the vein down the side, with a long white stripe dried across it. No dot."
    hide cg onlayer cgl
    show bg lc_stairs onlayer bgl
    "You go up the side stairs, past the bins, grinning, your sweats creaking. At the top, the door with the frosted window, and the schedule still taped to it, and the top line still says what it said the first day. You read it out loud again, because you can't help it."
    show screen lc_sheet(["{b}SCHEDULE{/b}", "Model: [lc_pc_name] (open call)."])
    lc_you "\"{i}Model: [lc_pc_name] (open call).{/i}\""
    hide screen lc_sheet
    show lc_dot flat at vn_cast_slot
    "The door's standing open. Dot's coming down the stairs past it with an armful of red stickers, on her way to the show. She looks at you in your gaping sweats."
    lc_dot "\"Hold that.\""
    "She keeps walking."
    hide lc_dot
    show bg lc_room_bare onlayer bgl
    "Upstairs, the life room's bare. Every board's been stripped. The cork's brown and empty and full of pinholes from floor to ceiling. The easels are folded against the wall. The stand's empty. The skip outside has had the last stool in it since lunchtime."
    show lc_dario hungry at vn_cast_slot
    "There's only the flat file, and the skylight going gold, and Dario. He's sitting on the flat file with a board on his knee and a fresh stack of paper, and he looks at you in the doorway, at all of you, and he doesn't say hello."
    lc_dario "\"Drop the sweats. I want the back.\"\n{size=-5}{color=#ff8fa3}▸ Drop the sweats{/color}{/size}"
    hide lc_dario
    $ vn_pass(10)
    jump lc_show_six

label lc_show_six:
    $ lc.fit = "nude"
    $ vn_enter(bg="lc_room_bare", pc="wanting", pc_tag="lc_pc", cast=[], cg="lc_show_board")
    "The sweats come down with a sound like a balloon going. You kick them across the bare floor and climb up on the flat file, knees and elbows, face-down, and arch."
    show cg lc_show_board onlayer cgl
    "Dario climbs up behind you. He lays his board flat across the small of your back like a table, clips a sheet to it, and starts drawing on {i}you{/i}. The charcoal scratches through the board into your spine."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Don't move. Board stays up.\""
    "Downstairs, through the floorboards, the show: music, voices, laughing, glasses. Somebody downstairs says \"look at the {i}thighs{/i} on it,\" and somebody else laughs."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Ass. Big form. Biggest form in the room. Soft edge where it meets the thigh, no line at all—\""
    show cg lc_show_grow onlayer cgl
    $ lc_body(6)
    "{color=#ff5fb8}And under his eyes it gets {i}bigger{/i}. It starts slow and doesn't stop. Your ass swells up under the board, lifting it, filling, rounder and heavier, the cheeks spreading out across the top of the flat file until they're spilling off both sides of it.{/color}"
    "{color=#ff5fb8}Your thighs thicken behind them, pressing together so hard and so soft that your balls disappear between them, swelling out over the drawer fronts, plush and warm and enormous.{/color}"
    if lc.pinned:
        "{color=#ff5fb8}Your chest goes with them, pressed out under you against the cabinet top, a size at least: large now, and heavy. Nobody's looking at it. Everybody's looking at your ass.{/color}"
    lc_you "\"{i}Ohhhh{/i}— Dario— oh {i}god{/i}, it's {i}more{/i}— it's {i}so{/i} much more— it's the most it's ever— {i}AHH{/i}—!\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Keep the board up.\""
    lc_you "\"I'm {i}trying{/i}—!\""
    "It keeps going. The flat file, the big wide map cabinet, starts to look narrow under you. Then it starts to look like a bench. Your ass is so big you can feel the air of the whole room on it, so heavy it jiggles with your heartbeat."
    lc_you "\"More— {i}more{/i}— oh, I'm— everything's— my {i}thighs{/i}, Dario, my {i}ass{/i}, I can't— I can't feel the {i}edges{/i} of it—\""
    if lc.pinned:
        call lc_pin_call
    else:
        "Your chest, under you, pressed to the flat file: exactly what it was the day you came up the stairs. Puffy pink nipples and nothing else."
    show cg lc_show_hands onlayer cgl
    "Dario puts the charcoal behind his ear. He puts one black hand on the back of your thigh, and squeezes, and his fingers don't get anywhere near round it. Not even halfway. He tries with both hands. He can't get round {i}one{/i} of them."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Huh.\""
    "Pleased. Then his jeans are open, and his cock's out, and he doesn't put it in you. He pushes it down between your thighs, into the plush hot crush of them, right where they press together under your ass."
    "You squeeze."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Vein down the left side. Darkest value in the room.\""
    "He starts to move."
    menu:
        "He's between your thighs."
        "Squeeze him":
            jump lc_show_sex

## ---- THE ENDING, "Not For Sale" (Lifeclass Show 6 After) --------------------------------------------

label lc_show_after:
    $ vn_enter(bg="lc_room_bare", pc="flushed", pc_tag="lc_pc", cast=[], cg="lc_show_in")
    "He doesn't stop narrating. Slow now, stroke by stroke, sliding back through your thighs, describing it."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"In. Soft— {i}soft{/i}— no edge— in— up under the balls— the head comes out the front, look, it's poking out the front of you— {i}out{/i}. Back. Thigh closes after it. No gap. No gap at all.\""
    lc_you "\"{i}Ahh{/i}— I'm {i}squeezing{/i}— can you feel— tell me you can {i}feel{/i} it—\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Feeling it. Drawing it. Squeeze on the out-stroke. {i}Yes.{/i} That's the value.\""
    "The board on your back jumps with every thrust and he keeps drawing on it, the charcoal skittering, smudging; he doesn't care. Your own cock's hanging under you, getting rubbed by him on every stroke, hard and drawn and completely forgotten."
    show cg lc_show_in onlayer cgl
    "Then he pulls out of your thighs, lines up, and pushes into you instead." with vnfx("shake")
    lc_you "\"{i}OHHH{/i}—!\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"In you. Whole new form. Look at it take me. Board up. {i}Board up{/i}.\""
    lc_you "\"Board's {i}UP{/i}—!\""
    show cg lc_show_door onlayer cgl
    "Someone's in the doorway. A stranger with a plastic cup of wine, who's come up the side stairs looking for the toilet and found this instead."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Out. Back's not finished.\""
    "Without looking up, without slowing down. The stranger goes. Another comes up, drawn by the noise, and stands there with his mouth open."
    lc_you "\"{i}OUT{/i}— {i}he's DRAWING{/i}—!\""
    "Louder than the music downstairs, louder than the whole café. That one goes too. A third, a woman with a red sticker stuck to her finger, gets as far as the top step."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not now.\""
    "She laughs and goes back down. The noise of the show comes up the stairs after her, and you yell over it, wordless, because he's hitting something deep in you that makes your whole body go off like a bell."
    "He comes in you, hard, deep, buried, his hand flat on the board on your back to keep it level the whole time." with vnfx("flash")
    "And then, still hard, he pulls out and pushes back down between your thighs, and finishes there too, a second load dripping off the front of your thighs onto the flat file and over the whole huge soft curve of your ass."
    show cg lc_show_price onlayer cgl
    "A fourth stranger's in the doorway: a man in a good jacket, with a programme. He doesn't look at you; he looks at Dario."
    lc_voice "\"The sheet downstairs. By the till. The only one without a dot. What's the price?\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not for sale.\""
    lc_voice "\"Everything's got a price.\""
    "Dario thinks about it. He's still between your thighs. He puts his charcoal behind his ear, looks at the back of your head, and names it."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"I want him to lick up every drop—\""
    lc_you "\"{i}YES!{/i} {i}Done! SOLD!{/i}\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"—and then swallow my cock till the next song starts. That's the price.\""
    "The man in the jacket opens his mouth. Shuts it. Goes back down the stairs."
    show cg lc_show_pay onlayer cgl
    "You're already paying it. Off the flat file, onto your knees, face down in the mess on the drawer fronts, licking, every drop, off the wood, off the brass handles, off your own thighs, moaning with your mouth full while Dario draws you doing it."
    "Then he's in front of you and you're swallowing him, all the way down, your fat lips stretched round the root of him, your whole enormous ass up in the air behind you for anyone else who comes up the stairs."
    "Downstairs, the song changes. Neither of you notices."
    $ lc.ending = "notforsale"
    $ achievement.grant("The Only Sheet Without a Red Dot")
    if lc.pinned:
        $ vn_feat("The Chest Study Took")
    hide cg onlayer cgl
    "You don't remember the bus. You remember the sweats not going back on at all, and Dario's coat round your waist, and your own voice, hoarse, singing.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(13)
    jump lc_epilogue

## ---- DAY 7, the epilogue (Lifeclass Epilogue, Stay, Go) -------------------------------------------

label lc_epilogue:
    $ lc.fit = "coat"
    $ vn_enter(bg="lc_stairs", pc="wanting", pc_tag="lc_pc", cast=[], cg="lc_epi_door")
    show cg lc_epi_door onlayer cgl
    "You go back up the side stairs the next afternoon in Dario's coat, because it's the only thing that goes round you, and it only just does."
    if lc.pinned:
        "It doesn't button over your chest at all. You hold it shut with one arm and tell the bus driver it's the radiator, water weight, sorry, sorry, which he didn't ask."
    "The schedule's still taped to the frosted door. The top line still says open call. Somebody's stuck a red dot on it as a joke."
    hide cg onlayer cgl
    show bg lc_room onlayer bgl
    "Inside, the cork's all bare, and the class is setting up like nothing happened. Roz is swearing at a fresh board. Tamsin's laughing at the red dot on the door. Milo's got a sheet up already. Bjorn's carrying in a stool you could park a car on. Winnie isn't here yet. Aurelio's at her clay. Dario's on his chair with an empty box at his feet and a look on his face."
    $ lc.fit = "nude"
    show cg lc_epi_room onlayer cgl
    "You drop the coat at the chair by the door. The whole room turns round to look at your ass, and then goes back to setting up. Dot claps once."
    show lc_dot crit at vn_cast_slot
    lc_dot "{color=#f3c969}{b}“Whatever you like.”{/b}{/color}"
    "The room waits. You stand there naked and enormous and grinning, with every eye in the place on you, and your cock already up for Dario's charcoal."
    menu:
        "Whatever you like."
        "Keep your name on the schedule" (ending=True):
            jump lc_epilogue_stay
        "Sit for Dario" (ending=True):
            jump lc_epilogue_go

label lc_epilogue_stay:
    $ lc.epilogue = "stay"
    $ vn_enter(bg="lc_room", pc="wanting", pc_tag="lc_pc", cast=[("lc_dot", "watch")], cg="lc_epi_stay")
    lc_you "\"Put me down for all of it. Every session. The whole spring. And the summer. Is there a summer?\""
    lc_dot "\"There's a summer.\""
    "She writes something on the schedule."
    show cg lc_epi_stay onlayer cgl
    if lc.pinned:
        "You get up on the stand and sit on Bjorn's new stool, and it holds, just, and the whole of you settles out over it on every side, soft and heavy and smooth. Your thighs hang off the edges. Your ass spills off the back. Your chest is nothing like the chest you came up the stairs with: it rests huge and heavy on your forearms, and Roz has already turned her easel round."
    else:
        "You get up on the stand and sit on Bjorn's new stool, and it holds, just, and the whole of you settles out over it on every side, soft and heavy and smooth. Your thighs hang off the edges. Your ass spills off the back. Your chest is the chest you came up the stairs with."
    lc_dot "\"Whatever you like. Go.\""
    "The charcoal goes. And you don't stay still for long. You never do now."
    show cg lc_epi_stay_crowd onlayer cgl
    if lc.pinned:
        "By the first break you've got Milo behind you over the stool, \"Best seat in the co-op,\" and Roz's black hands full of your chest, and Tamsin laughing into your thigh, and Aurelio moving your hip a little higher with her clay-grey thumbs. \"There.\""
    else:
        "By the first break you've got Milo behind you over the stool, \"Best seat in the co-op,\" and Roz's black hand round your cock, and Tamsin laughing into your thigh, and Aurelio moving your hip a little higher with her clay-grey thumbs. \"There.\""
    "And Dot walking the horseshoe behind the easels, saying \"Watch the foreshortening on the thigh,\" like none of it is happening, which is somehow the hottest part."
    lc_you "\"Don't— {i}ahh{/i}— don't call time— nobody call {i}time{/i}—!\""
    "Milo comes in you. Bjorn takes his place, and the stool doesn't even creak."
    "At the end there's an envelope, and it's fat, and Winnie comes in with her coat half off just as you're licking your lips over it."
    hide lc_dot
    show lc_winnie late at vn_cast_slot
    lc_winnie "\"Is it over? It's over, isn't it.\""
    hide lc_dot
    show lc_roz swearing at vn_cast_slot
    lc_roz "\"All of it.\""
    lc_you "\"See you next session!\""
    "At the top of your high voice, to a round of charcoal-black applause.\n{size=-5}{color=#ff8fa3}▸ Down the side stairs{/color}{/size}"
    jump lc_route_return

label lc_epilogue_go:
    $ lc.epilogue = "go"
    $ vn_enter(bg="lc_room", pc="wanting", pc_tag="lc_pc", cast=[("lc_dario", "drawing")], cg=None)
    show bg lc_room onlayer bgl
    show lc_dario drawing at vn_cast_slot
    "You turn round and look at Dario."
    lc_you "\"Whatever I like. Right?\""
    "Dario's already got his board on his knee."
    hide lc_dario
    "The session goes the way sessions go: charcoal and swearing and Dot calling time. But when it ends and the others clatter off down the side stairs with their boards, you don't get dressed, and Dario doesn't pack, and Dot looks at the pair of you, switches off all the lights but the one over the flat file, and leaves."
    show bg lc_room_evening onlayer bgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Private study. After hours. Every night you want.\""
    lc_you "\"Every {i}night{/i}.\""
    show cg lc_epi_go onlayer cgl
    "You're on the flat file before he's finished, knees and elbows, face-down, arched, the whole enormous soft shelf of you up in the light. He lays the board across your back. He draws. He talks."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Ass. Biggest form in the room. Thigh, soft edge, no line. Cock, hanging, vein down the left side, darkest value in the room.\""
    if lc.pinned:
        "He doesn't draw your chest. He never has. It's the one thing in the room he won't."
    "Then he's between your thighs, and you squeeze, and he groans and narrates it, stroke by stroke, and then he's in you and you're screaming at the skylight, and the board bounces on your back the whole time and he never once puts it down."
    lc_you "\"Every {i}night{/i}, Dario— every night— don't you {i}dare{/i} stop drawing—!\""
    "He comes in you, and then between your thighs, and you come across the drawer fronts untouched, and he draws that too." with vnfx("flash")
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Not bad. I'm keeping it.\""
    "He holds the sheet up to the light.\n{size=-5}{color=#ff8fa3}▸ Down the side stairs{/color}{/size}"
    jump lc_route_return
