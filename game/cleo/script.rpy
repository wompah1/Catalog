## cleo's weeks: Danny's half of each chapter (the kitchen, what last Friday kept, the fridge, the
## advice, his line) up to Nate's "It's Friday". The sessions are in scenes.rpy. Six linear weeks.
## Production rewrite (2026-11-13, twinetesting-c9): the same plan, pass and ending, deepened from the
## book: a picture per beat, the week's middle (Halo, the counter, the pizza, the theory, the bag),
## and choices that carry forward (cook, halo, jeans4, photo6 here; greet1, talk2, ask3, stock4 in
## the sessions). The calendar fixed: day 1 is a Friday, so Fridays are days 1, 8, 15, 22, 29, 36.

## ---- WEEK 1: That's Not How She Said It ------------------------------------------------------
label cle_week_one:
    $ cle.fit = "apron"
    $ vn_enter(bg="cle_kitchen", pc="concerned", pc_tag="cle_pc", cast=[], cg="cle_fridge_steph")
    "Friday evening, the kitchen. The last pot away, a wet tea towel rolled into a ball under your palm, the radio on low, the bin bag knotted high."
    "You're yourself. The dark hair on your forearms still flattened wet from the washing-up, a man's arms, thick at the wrist. Your own jeans fitting the way they always have."
    show screen cle_fridge(1)
    "And the fridge, the way it's been all month. Steph on Nate's arm on a bridge. Steph pretending to steal his chips at a service station. Steph in a green raincoat, not quite smiling. Barely a gap between them."
    hide screen cle_fridge
    show cg cle_list onlayer cgl
    "You go to pin the new shopping list up, pasta, spinach, yoghurt, always eggs for Nate, and it droops over Steph's face, half of her gone behind tinned tomatoes."
    "So you move her. Very gently, one spot left, to the corner, under a magnet shaped like a pineapple. It feels like the least you can do."
    hide cg onlayer cgl
    "Steph left four weeks ago. You know the shape of a month like this one exactly, because you've watched it from the kitchen: the takeout cartons stacking by the bin, the four-year playlist through the wall at two in the morning, the not sleeping."
    "You came in here to make toast one of the first weekends after she left, and you made two slices instead of one and left the second on a plate outside his door. That was the start of the cooking. You've been managing it, quietly, ever since. You do the bins. You turn the playlist down a notch from the hall when he's not looking."
    show cg cle_tea_one onlayer cgl
    menu:
        "What's for tea?"
        "Jollof, the proper way":
            $ cle.cook = "jollof"
            "Jollof, your mum's way, smoky at the bottom of the pan. Nobody's sad eating your mum's jollof. It's been tested."
        "A big spag bol":
            $ cle.cook = "bolognese"
            "A spag bol big enough to freeze half of. You'll be eating it till Wednesday and so will he, whether he likes it or not."
        "Chicken soup":
            $ cle.cook = "soup"
            "Chicken soup. It's not that he's ill. It's that he looks ill, and soup doesn't know the difference."
    show cle_nate sad at vn_cast_slot
    "Nate comes in like a man walking underwater: the faded blue jumper, odd socks, shoulders forward. He stands by the kettle without putting it on."
    "Through the wall, the playlist rolls into another of her songs. You reach over and turn the radio up, to drown it, and then down again, because that's worse."
    cle_you "\"Sit down. It's ten minutes. You're eating it.\""
    cle_nate "\"I'm not hungry.\""
    cle_you "\"You're eating it anyway.\""
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="concerned", pc_tag="cle_pc", cast=[("cle_nate", "sad")], cg="cle_talk_one")
    "He sits. He eats, a bit. You watch him eat, a bit, and you don't say anything about the playlist, because you've decided you're not going to, and then you do anyway, because you're you."
    cle_you "\"Mate. You need to talk to somebody about this.\""
    cle_nate "\"I'm all right.\""
    cle_you "\"You're not. You've had nothing but eggs and takeout and that playlist for a month, and I hear you up at three most nights. I'm not having a go, mate. I'm just worried about you.\""
    "He tries to smile, the way a tired man tries to tie his shoes."
    cle_nate "\"I'll be fine. I promise.\""
    cle_you "\"You're wearing Tuesday's jumper.\""
    cle_nate "\"It's a good jumper.\""
    "The line you've had ready for weeks, {i}you can't just wait for somebody to come back{/i}, dies unused. He looks too tired to hear it. You'll save it."
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="concerned", pc_tag="cle_pc", cast=[("cle_nate", "sad")], cg="cle_door_one")
    "He takes his plate to the sink and rinses it, which is something. Then he stops in the doorway, and looks at you, for a moment, like he's about to say something else."
    "You're at the light switch with your hand out. The playlist's gone quiet through the wall."
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(1)
    jump cle_session_one

## ---- WEEK 2: Sweeter -------------------------------------------------------------------------
label cle_week_two:
    $ cle_body(2)
    $ cle.fit = "apron"
    $ vn_clock = VNState(day=2, hour=9, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="sleepy", pc_tag="cle_pc", cast=[], cg="cle_arms")
    "Saturday morning, the light through the blinds sharp for September. You're cracking eggs into the pan, the second one halfway open, and you stop."
    "Your arms."
    show cle_pc concerned
    "[CLE_KEEPS[2]!c]. Not a hair on them, not on your wrists, not on your knuckles. You turn one over under the window. You can see the blue of the veins at your wrist."
    "You check under your T-shirt. Your chest too. Your legs, when you look down at your shins. Everywhere."
    cle_you "\"New gym's worth every penny, then.\""
    "You tell your forearm, cheerfully, and flick a bead of yolk off your wrist, and crack the egg."
    hide cg onlayer cgl
    "You slept badly, which you never do. A dream: somebody kept saying no in a voice like honey, and somebody else kept saying it back to them nicer, like they were teaching it a song. You blame the four cheese on the pizza. You always blame the four cheese."
    if cle.cook == "jollof":
        "There's the last of the jollof in the fridge, in its tub. Somebody's had a go at it with a fork in the night, which is the best review you've ever had."
    elif cle.cook == "bolognese":
        "There's the spag bol in the fridge in three tubs, as threatened. One of them's been opened in the night and had a fork in it, which is the best review you've ever had."
    else:
        "There's soup left in the pan, and somebody's had a mug of it in the night and washed the mug, which is the best review you've ever had."
    show screen cle_fridge(2)
    show cg cle_fridge_new onlayer cgl
    "And the fridge. Steph by the window, who's smiled out from the middle magnet for three Christmases, has come down. In her place there's somebody new."
    "You lean in with the spatula. Lavender bob. Steph's mouth. Steph's way of not quite looking at the camera. It isn't her, though. It isn't. Her necklace twists a different way, and she's smiling like she means it, for one thing."
    "Nate's found a lookalike. You'd put money on it. You stand there eating a bit of egg straight off the spatula, extremely satisfied with yourself."
    hide screen cle_fridge
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "dry")], cg="cle_eggs_two")
    "Nate wanders in with his hair on end and his face already turned toward the sound of somebody else frying his eggs. He looks almost human. If he notices your arms, it doesn't register."
    "You point the spatula at the fridge and grin."
    cle_you "\"Taken the plunge, then, yeah?\""
    cle_nate "\"Don't start, Dan.\""
    cle_you "\"I'm not starting. Just saying. You found someone. Closest thing to a win I've seen from you all summer, unless you count beating me at Halo on Wednesday.\""
    cle_nate "\"It's nothing special.\""
    "But he's smiling into his coffee, the sort of smile that leaks shame and relief together."
    menu:
        "You're going to say something. You can feel it coming."
        "Put it gently":
            $ cle.say2 = "gently"
            "You slide him a plate of eggs, so he's got something to look at."
            cle_you "\"So. The new one on the fridge. She seems nice. I just want to say one thing, and then I'll shut up.\""
        "Just come out with it":
            $ cle.say2 = "straight"
            cle_you "\"Right. I've seen the fridge. I'm saying this as your friend who makes your eggs.\""
    cle_you "\"[CLE_ADVICE[2]]\""
    "Nate gives a small, guilty laugh."
    cle_you "\"I mean it. I get it, I do. But if this is your way of fixing things... you need to talk to somebody about this. Maybe even her. Whoever she is.\""
    "He prods his egg, and watches the yolk break gold over the whites."
    cle_nate "\"I'm not trying to fix anything.\""
    "He nods at his plate, though, slowly, the way he does when he's actually listening. You watch his shoulders come down a bit as the coffee does its work. The new photo watches the both of you from under its magnet."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=6, hour=21, minute=0)
    $ vn_enter(bg="cle_living", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "dry")], cg="cle_halo")
    "The week goes the way weeks go. Your arms stay smooth and weirdly pleasant under your T-shirts, and the new gym gets all the credit. On Wednesday there's Halo on the sofa, the rematch, a bag of crisps between you."
    menu:
        "Nate's one kill off winning again."
        "Let him win":
            $ cle.halo = "let"
            "You walk your man straight into his line of fire, whistling. He wins. He punches the air. He doesn't notice you let him, and you'd never in a million years say."
        "Win, obviously":
            $ cle.halo = "win"
            "You win. Obviously. You stand on the sofa and do a lap of honour on the cushions, and Nate throws a crisp at you, and laughs. A real one. First in a month."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=8, hour=21, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "dry")], cg="cle_door_two")
    "Friday night, the clock somewhere past nine, the rain catching the streetlight. You call the week's shopping sorted, wipe your hands on the tea towel, and hand him the remote."
    "He closes up the leftovers with his mouth set in a familiar line. Then, barely meeting your eyes, so quietly:"
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(2)
    jump cle_session_two

## ---- WEEK 3: Be There With Her ---------------------------------------------------------------
label cle_week_three:
    $ cle_body(3)
    $ cle.fit = "own"
    $ vn_clock = VNState(day=10, hour=11, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_laugh")
    "Sunday, the dishes. Your hands in the suds, last night's chilli coming off the pan, the radio doing a phone-in about bins."
    "Your skin's gone soft, all over. You noticed in the shower: soft and smooth, the knuckles that used to rough up gone smooth, your neck and shoulders just sliding under the towel, like you've been moisturising, which you haven't. It's the gym. You've started on the rowing machine. You must be touching something odd on the way out."
    "The spoon slips off the edge of the sink, and you laugh. Light and bright, up at the end."
    "It isn't your laugh. You don't notice."
    "Somebody on the radio says something so stupid you laugh at that too, the same laugh, and slot the mug in with the others."
    hide cg onlayer cgl
    "You had the dream again. Saying no in somebody else's voice, and it coming out like a line in a play. You blame the cheese. There wasn't any cheese. You blame it anyway."
    show screen cle_fridge(3)
    show cg cle_fridge_two onlayer cgl
    "Another of Steph's come down, the edges grimy from too many years in the same place. Another of the new woman's gone up, under a flat red magnet."
    "You dry your hands and lean in. It's the same woman as last week. Almost. Last week's smiled shy, her arm only just linked through Nate's. This one's leaning in, laughing, his arm right round her waist. Her hair's softer at the ends, like she's growing it out. Her jaw looks rounder. She's holding herself in a way Steph would've called goofy."
    "You tap a finger beside her chin, eyes narrowed. It can't be the lighting this many times. You've got a theory, half serious and entirely yours, and you're really enjoying having it."
    hide screen cle_fridge
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_toast_three")
    "Nate's at the table with toast. He's whistling. You haven't heard him whistle since August."
    if cle.halo == "let":
        cle_nate "\"Still undefeated at Halo, by the way. Just so it's on record.\""
        cle_you "\"It's on record, mate. Framed.\""
    else:
        cle_nate "\"I want a rematch. That lap of honour was unforgivable.\""
        cle_you "\"Any time, mate. Bring tissues.\""
    cle_you "\"You miss her?\""
    cle_nate "\"No. Not really. Feels weird, honestly. In a good way.\""
    "Which is good. It's good. Except you've seen this film. The rebound you throw yourself at so you don't have to feel anything, and then a month later you wake up in a flat with two of everything and nobody in it."
    menu:
        "How do you put it?"
        "Over the sink, not looking":
            $ cle.say3 = "sink"
            "You say it to the window, which is easier."
            cle_you "\"Can I say a thing? About the new girl.\""
        "Sit down across from him":
            $ cle.say3 = "table"
            "You pull the other chair out and sit, wet hands and all, so he knows it's serious."
            cle_you "\"Nate. Look at me a sec.\""
    cle_you "\"[CLE_ADVICE[3]] Not your phone, not the other one, not the past. Her. Whoever she is.\""
    cle_nate "\"I'm not trying to fix anything.\""
    cle_you "\"Yeah, you are. Nothing wrong with it. At least you're doing the dishes again. And you need to talk to somebody about this. Her, if nobody else. Actually talk.\""
    cle_nate "\"Not today.\""
    "He raises both hands and backs away from the sink, grinning. Then, at the door, he says, \"Yeah,\" quietly, like he means it."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=13, hour=8, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_counter_three")
    "On Wednesday, with nothing prompting it, he drifts in and hikes himself onto the counter, swinging his heels like a man with good news."
    cle_nate "\"Hey. I've already got Friday planned. Don't cook anything big.\""
    cle_you "\"Two days early, huh?\""
    cle_nate "\"Yeah. Got it all sorted already. It's going to be good.\""
    cle_you "\"Look at you. Good for you, man.\""
    "You're so pleased for him you put an extra sausage on his plate, and then, because he's on the counter, a second one."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=15, hour=19, minute=0)
    $ vn_enter(bg="cle_hall", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg=None)  # ff 2:34 am: no picture, door-three failed 4 draws (SCENES.md cleo v7)
    "Friday. He's showered. He's had a shave. He puts his head round the kitchen door with his hair still damp, smiling before he's even said it."
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(3)
    jump cle_session_three

## ---- WEEK 4: Cleo -----------------------------------------------------------------------------
label cle_week_four:
    $ cle_body(4)
    $ cle.fit = "own"
    $ vn_clock = VNState(day=16, hour=10, minute=0)
    $ vn_enter(bg="cle_hall", pc="concerned", pc_tag="cle_pc", cast=[], cg="cle_jeans")
    "Your jeans have stopped working."
    "Inside a week. You pull your favourite pair up in the hall and they stop, halfway over your arse, and you have to jump them the rest of the way, and then [CLE_KEEPS[4]]."
    "You stand there with your hand on the back of the waistband, feeling the gap. You look over your shoulder in the hall mirror. There's a lot more of you behind than there was."
    "It's the dryer. That dryer's always been a menace."
    menu:
        "Something must be done about the dryer."
        "Write to the landlord":
            $ cle.jeans4 = "landlord"
            "You sit down on the stairs and write the landlord a strongly worded email about the dryer, with a subject line in capitals. It's very satisfying. You wear your joggers."
        "Buy the next size up":
            $ cle.jeans4 = "size"
            "You order the next size up, two pairs, while you're still in the hall. The seat fits. The waist gapes like a mouth. You wear a belt and think no more about it."
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_fridge_middle")
    show screen cle_fridge(4)
    "Another of her on the fridge this week. Not at the edge."
    "Right in the middle, where you'd see her first. Her bob's grown out past her jaw into loose waves. Nate's put her there on purpose. You notice where he's put her, and you smile at the fridge like an idiot."
    hide screen cle_fridge
    hide cg onlayer cgl
    $ vn_clock = VNState(day=21, hour=20, minute=0)
    $ vn_enter(bg="cle_living", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_pizza_four")
    "Thursday, pizza on the sofa. Nate's telling you about her, which he does now, in bits: the way she does the crossword in pen, the way she steals the duvet, the way she sings in the shower and gets the words wrong on purpose."
    cle_you "\"So you're seeing her properly now?\""
    cle_nate "\"She's great. Funny. It's—\""
    "He goes looking for the word, and comes back with it."
    cle_nate "\"Honestly, it feels comfortable.\""
    cle_you "\"Comfort's allowed. As long as you aren't just going through the motions. She seems... nice. Still no name?\""
    cle_nate "\"Steph's great. It's good, it's different, I guess I'm still—\""
    "He stops. He doesn't notice he's stopped. You notice."
    menu:
        "He just called her Steph."
        "Say it gently":
            $ cle.say4 = "gently"
            cle_you "\"Hey. Can I say something, and you won't get weird about it?\""
        "Nudge him with your foot":
            $ cle.say4 = "foot"
            "You nudge his leg with your socked foot, to get his attention."
            cle_you "\"Oi.\""
    cle_you "\"[CLE_ADVICE[4]] I know it's habit, but come on, mate. Nobody likes to be just a stand-in. She deserves to be called her own thing.\""
    cle_nate "\"I know. I don't mean to.\""
    cle_you "\"I believe you. Just— you need to talk to somebody about this. Doesn't have to be me, but talk to her, or somebody. It isn't about fixing Steph. It's about treating her like her own person.\""
    cle_nate "\"I'm not trying to fix anything.\""
    show cg cle_olives onlayer cgl
    "He's quiet for a while after that. He picks the olives off his slice one by one, lines them up on the lid of the box, and doesn't eat them."
    "You eat them. Somebody has to."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=22, hour=19, minute=0)
    $ vn_enter(bg="cle_hall", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg=None)  # ff 2:34 am: no picture, door-four failed 4 draws (SCENES.md cleo v7)
    "On Friday evening there's a box on the hall table in black tissue paper, and a receipt Nate snatches up before you can read it. He puts his head round your door, and he's smiling."
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(4)
    jump cle_session_four

## ---- WEEK 5: Let Her Keep Some Things Here -----------------------------------------------------
label cle_week_five:
    $ cle_body(5)
    $ cle.fit = "apron"
    $ cle_her_name = "Cleo"
    $ vn_clock = VNState(day=23, hour=13, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_belt")
    "Saturday lunch. You're stood at the counter in your apron doing a second slice of toast, and your belt's sitting differently."
    "You hitch it. It slides down again, onto your hips, because [CLE_KEEPS[5]]."
    if cle.jeans4 == "landlord":
        "The landlord still hasn't answered about the dryer. You've written twice more. You're in joggers most days now, which, honestly, are comfier."
    else:
        "Even the next size up is doing it now: the seat snug as a glove, the waist gaping at the back like it's surprised to see you."
    "It's Nate's cooking. He's been cooking, this week: actual meals, with herbs in. You've been having seconds. You have a third slice of toast, to be consistent."
    show screen cle_fridge(5)
    show cg cle_fridge_gown onlayer cgl
    "Two of Steph down this week. Two of the new one up: one in a dressing gown on your sofa, one laughing so hard she's out of focus."
    "Her name's Cleo. He says it now, when he talks about her. You told him to and he did. You'd be lying if you said that hadn't made your whole week."
    hide screen cle_fridge
    hide cg onlayer cgl
    $ vn_enter(bg="cle_hall", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_gown_door")
    "There's a second toothbrush in the bathroom, in its own cup. There's a dressing gown on the back of his door, a pink one, nothing to do with Steph. There's a jar of something in the fridge with a tea towel over it that you're not allowed to touch."
    "He's building something, and he's stopped pretending he isn't."
    hide cg onlayer cgl
    $ vn_clock = VNState(day=28, hour=20, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_theory_five")
    "Thursday, pizza at the kitchen table, because the sofa's got a dressing gown on it."
    cle_nate "\"Don't touch the fridge.\""
    cle_you "\"Didn't touch it. That one's good. You look less like a hostage in it.\""
    cle_nate "\"She baked bread. The weird rye thing. She left a jar of starter in my fridge, if you can believe it. Seemed right there.\""
    cle_you "\"She's using the starter? She's already braver than you.\""
    menu:
        "You've got a full theory now. Do you share it?"
        "Lay out the whole theory":
            $ cle.say5 = "theory"
            "You lay it out over the pizza. The whole thing. You've thought about it a lot, and you use a slice as a pointer."
            cle_you "\"Okay, so. I've noticed something about the photos. It's always the same type, right? At first I thought you'd found a new Steph. Or a cousin or something. But then the new one's got a different look. Not just the hair, the actual face, but close. And now two more off, two more up. But it's you in every one with her.\""
            cle_you "\"I'm not saying it's weird. Breakup happens, people bounce off a few lookalikes. Maybe you needed someone in the same lane at first. But now it's like— here she actually looks like herself. And you actually look happy. Means you didn't just get stranded.\""
            "Nate listens to every word. He nods in the right places."
            cle_nate "\"She's not Steph. She's Cleo.\""
            cle_you "\"She is now. Good. See, that's why I say let her have some space. She's stuck her starter in the fridge, Nate. You know what that means? She plans on more loaves. It's an investment.\""
            cle_nate "\"You're good, you know that?\""
            cle_you "\"I'll invoice you. All I ask is slipper respect. And pizza, clearly. That's the fee for grief counselling.\""
            "When you've finished he says, \"Thanks, Danny,\" and he means it, which is the nicest thing about him."
        "Just the advice":
            $ cle.say5 = "advice"
            "You don't do the theory. You're saving the theory. It's not finished. It needs another week of fridge."
    cle_you "\"[CLE_ADVICE[5]] Actual things. A dressing gown, some products, food in the wrong cupboard. Slippers. That's how you know she really lives here, if there are slippers. Don't make her live out of a tote bag.\""
    "Nate goes a bit pink."
    cle_nate "\"I like that. That sounds good. Dressing gown, towel, toothbrush. What am I missing?\""
    ## 3a's fork (the alternate route; owner, 2026-11-13): lanes.rpy
    menu:
        "What's she missing?"
        "Slippers" (ending=True):
            cle_you "\"Slippers. I literally just said slippers.\""
        "A proper bra. In her size" (ending=True) if CLE_BRA_READY:
            $ cle.lane = "bra"
            cle_you "\"Slippers. I literally just said slippers. And a proper bra, while you're at it. In her size. Not one of Steph's. Nobody wants to live in somebody else's bra.\""
            "Nate goes pinker."
            cle_nate "\"Her size. Right. Yeah. I— I know her size.\""
            cle_you "\"Course you do. Two, then. One for the drawer.\""
    cle_you "\"And you need to talk to somebody about this. About Cleo. Not just how-am-I-doing. Actually let someone in. She's not a transition, okay? You're allowed to be happy about her. Out loud.\""
    "He laughs. A proper one."
    cle_nate "\"Yeah. Okay. I will. Thanks.\""
    cle_you "\"All right. You finishing that last slice, or am I—\""
    cle_nate "\"You got it, big man.\""
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=29, hour=19, minute=0)
    $ vn_enter(bg="cle_hall", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_bag_five")
    "On Friday there's a bag from a shop you've never heard of on the hall table, tissue paper sticking out of the top, and a pair of pink slippers beside it, still with the tag on."
    "You don't look in the bag. You're a good flatmate. You do give the slippers a very approving nod."
    if cle.lane == "bra":
        show cg cle_bra_box onlayer cgl
        "Under the tissue paper there's a long flat box with a lace bra drawn on the lid. Two, by the look of it. You give the box a very approving nod as well."
        hide cg onlayer cgl
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(5)
    jump cle_session_five

## ---- WEEK 6: Take the Photos Down --------------------------------------------------------------
label cle_week_six:
    $ cle_body(6)
    $ cle.fit = "own"
    $ vn_clock = VNState(day=30, hour=10, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_saturday")
    "Saturday morning. [CLE_KEEPS[6]!c]."
    if cle.lane == "bra":
        call cle_bra_kettle
    "That's all. It's just how you are now. You put the kettle on, and sing along to the radio in a voice that sits a bit higher than it used to, and get the words wrong."
    "You're not thinking about yourself anyway. You're too busy being proud of Nate."
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_paper_six")
    "He's at the table in a clean T-shirt, reading the paper. He hasn't played the four-year playlist in a month. There's a second mug on the draining board that isn't yours, with lipstick on the rim."
    ## 3b's fork (the alternate route; owner, 2026-11-13): lanes.rpy. Not offered on 3a.
    if not cle.lane:
        menu:
            "Last piece of advice. Which one have you been saving?"
            "Take the photos down" (ending=True):
                pass
            "Ask her to stay the weekend" (ending=True) if CLE_STAY_READY:
                $ cle.lane = "stay"
    menu:
        "Last piece of advice. You've been saving it."
        "Say it over breakfast":
            $ cle.say6 = "breakfast"
            cle_you "\"I think you're ready for this one.\""
        "Say it with the kettle in your hand":
            $ cle.say6 = "kettle"
            "You point at the fridge with the kettle."
    if cle.lane == "stay":
        cle_you "\"Ask her to stay. Not just Fridays. The whole weekend. Ask her properly, Nate. If she says yes, she says yes.\""
        "He looks at the fridge for a long time, at the last of Steph down by the handle and all the new one round her."
        cle_nate "\"She'd say yes.\""
        cle_you "\"Then ask.\""
        "He folds the paper, and nods, and gets up, and puts the kettle on for both of you, which he's never once done."
        hide cg onlayer cgl
        jump cle_week_six_tuesday
    cle_you "\"[CLE_ADVICE[6]]\""
    "He looks at the fridge for a long time. Then he folds the paper and gets up."
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_photos_down")
    "He crosses to the fridge and runs a thumb across the last of Steph's smile."
    cle_nate "\"Yeah.\""
    "You do it together. You hand him the last ones of Steph, one at a time, and he takes them, and you say exactly the right things, because you've been practising: that four years is real, that he can keep them in a box, that it's allowed to be over."
    cle_you "\"You can always put these up again, if you want.\""
    "He puts them in a shoebox, and the shoebox on top of the wardrobe, and comes back, and doesn't look sad. He looks like a man who's put a box on a wardrobe."
    "What goes up in the gaps is her. Cleo in a woolly hat. Cleo asleep on the sofa. Cleo pulling a face at the toaster."
    menu:
        "One for the middle of the fridge. He holds out two and lets you choose."
        "The woolly hat":
            $ cle.photo6 = "hat"
            "The woolly hat, pom-pom and all, her nose pink with cold, laughing at whoever's holding the camera. It goes in the middle."
        "Asleep on the sofa":
            $ cle.photo6 = "sofa"
            "Asleep on the sofa, under a blanket, mouth a bit open, the dressing gown sleeve over her hand. It goes in the middle."
    hide cg onlayer cgl
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_fridge_all")
    show screen cle_fridge(6)
    "When you step back the fridge is all her."
    cle_you "\"That's a better fridge. Cleo deserves the whole thing.\""
    cle_nate "\"Yeah. She does.\""
    "And the pink slippers you've definitively decided are Cleo's sit at the bottom of it, side by side, toes out."
    "You don't tell him he needs to talk to somebody about this. He doesn't need to. Look at him."
    hide screen cle_fridge
    hide cg onlayer cgl
    hide cle_nate
    if cle.lane == "bra":
        call cle_bra_mirror
    jump cle_week_six_tuesday

label cle_week_six_tuesday:
    $ vn_clock = VNState(day=33, hour=19, minute=0)
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_bread_six")
    "On Tuesday, for the first time since you moved in, Nate cooks for you."
    "He makes you sit down. He makes you sit down and not get up, which is harder than it sounds, and he puts a plate in front of you: soup, and a loaf of the weird rye bread, still warm, a bit flat on one side."
    cle_nate "\"Cleo's starter. She showed me. Don't say anything about the shape.\""
    cle_you "\"I wasn't going to say anything about the shape.\""
    cle_nate "\"You were thinking it.\""
    cle_you "\"I was thinking it's the best bread I've ever had in this flat, which, fair, is a low bar, because it's the only bread anybody's ever made in this flat.\""
    if cle.lane == "stay":
        "He laughs, and sits down across from you with his own bowl, and for a while you just eat, the two of you, with the radio on and the fridge nearly all her."
    else:
        "He laughs, and sits down across from you with his own bowl, and for a while you just eat, the two of you, with the radio on and the fridge full of her."
    cle_nate "\"Thanks, Dan. For all of it. The eggs. The fridge. Making me talk.\""
    cle_you "\"You did the talking. I just made the eggs.\""
    "He looks at you for a second, across the table, like he's about to say something else. Then he passes you the butter."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=36, hour=19, minute=0)
    $ vn_enter(bg="cle_hall", pc="cheerful", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_door_six")
    "The rest of the week's an easy one. Nothing grows and nothing goes back; you're just you, the way you are now, and you've stopped looking. On Friday evening he puts his head round your door, smiling, the way he does."
    cle_nate "\"It's Friday.\""
    hide cle_nate
    call cle_friday(6)
    jump cle_session_six
