## THE STORY: days 8-10 (PLAN.md). Monday: the 7:42 and the copy room; Wednesday: Tsuge's after-hours review and the second
## check-up, where Hayami spells "appetite" out. The change shows each night in the bathroom mirror.

## ---- 3. Monday: the 7:42, and Ooba -----------------------------------------------------------------------------

label sef_commute:
    $ sef.fit = "office"
    $ vn_enter(bg="sef_train", pc="flustered", pc_tag="sef_pc", cast=[("sef_grey", "leer")], cg="sef_seven_forty_two")
    "Natsuki lends you a blouse that won't button over your chest and a pencil skirt that will, just. You go to work anyway. Hayami's paperwork says you're expected."
    "The 7:42 into Shinjuku is the same as ever, packed so tight you don't need to hold on. It's not the same at all. Men look at you."
    "Men you've stood next to every morning for two years look at you, and then look down your blouse, and then look again."
    "At Nakano-sakaue the crowd shoves in and you end up pressed face-first to the door, and somebody's pressed up behind you."
    "A hand lands on your arse. Not an accident. It squeezes."
    "You turn your head as far as you can. A man in a grey suit, forties, very ordinary, reading his phone with his other hand. He doesn't even look at you."
    menu:
        "His hand's on your arse."
        "Elbow him":
            "You get an elbow back into his ribs, as hard as the crowd lets you, which isn't hard at all. He grunts, and the hand doesn't move."
            sef_grey "\"Shh,\" he says, into your hair. \"You'll make a scene.\""
            $ sef.held += 1
        "Stand still":
            "You stand still. You don't know why. Every man in this carriage would look if you made a noise, and you can't bear the thought of them all looking."
            $ sef.gave += 1
    show cg sef_train_hands onlayer cgl
    "His hand slides your skirt up at the back, inch by inch, until his fingers are on your bare thigh, and then on the damp gusset of your knickers."
    "Damp. You're {i}damp.{/i} The pills. The appetite. You hate them."
    "He pulls the knickers aside and strokes you, slow, front to back, and your forehead bumps the glass."
    "Then his other hand comes round under your arm, under the blouse, and finds a breast and fills itself with it."
    sef_grey "\"Look at the size of these,\" he breathes. \"Every morning, from now on. Same carriage.\""
    "Two of his fingers slide into you and the train lurches and drives them deep, and his thumb finds your clit, and your breath fogs the window."
    vn_sfx "Kuchu. Kuchu. Gatan. Gotan."
    sef_you "\"Hh— hh♡— not— not on the {i}train— nnh♡—\""
    "Shinjuku is two minutes away. He makes it in one and a half."
    "You come pressed to the door with your mouth open and no sound coming out at all, your whole body shaking, and his fingers pumping you through it."
    "The doors open. He's gone into the crowd. You walk to the office on legs that don't quite work, with your knickers soaked and your nipple still throbbing where he pinched it."
    $ vn_set_time(12, 30)
    $ vn_enter(bg="sef_copyroom", pc="flustered", pc_tag="sef_pc", cast=[("sef_ooba", "grin")], cg="sef_copy_room")
    "HR gives you a new lanyard that says AKIRA SENA and a smile that says please don't make this our problem. Everybody else just stares."
    "Ooba stares most. Ooba sits at the next desk. Twenty-seven, sharp suit, a laugh like a car alarm. For two years he called you Sena and threw paper clips at you."
    "Today he brings you a coffee and calls you Akira-chan."
    "At lunch you go to the copy room to print the shipping manifests, and he follows you in and shuts the door."
    sef_ooba "\"So it's true. It's really you.\" He's looking at your blouse. Everyone looks at your blouse. \"Can I see?\""
    sef_you "\"No, you can't see. Get out, Ooba.\""
    sef_ooba "\"Come on. We're mates. Just a look.\""
    "He's already got a hand on your waist. The copier's behind you, warm and humming. Your nipples are hard through the blouse; they've been hard since the train."
    "He sees that. His grin widens."
    show cg sef_over_the_copier onlayer cgl
    "He turns you round and bends you over the copier with one hand flat between your shoulder blades. The manifests go everywhere."
    "Your breasts squash on the warm glass lid."
    menu:
        "He's got your skirt up."
        "Shove him off":
            "You push back off the copier. He leans on you and you go back down, and his belt buckle clinks."
            sef_ooba "\"Two minutes. Lunch is forty-five. Nobody's coming.\""
            $ sef.held += 1
        "Let him finish":
            "You could shout. Half the floor would come running and see you bent over with your skirt up. You put your cheek on the lid and wait for it."
            $ sef.gave += 1
    "He's in you in one push, all of him. You're still soaked from the train."
    "He fucks you fast and greedy, the copier rattling under you, his hands up under your blouse kneading your breasts."
    vn_sfx "Pan. Pan. Pan. Pan."
    sef_ooba "\"Fuck— Akira-chan— you feel— better than any— fuck—\""
    "His hip knocks the copy button. The machine wakes up under you, warm and bright, and starts printing, and the light sweeps under your breasts with every page."
    sef_you "\"Ahh♡— ahh♡— Ooba— idiot— the {i}copier— hahh♡— don't stop, don't—\""
    sef_you "\"I'm going to— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come on his cock clamped down tight, and it drags him over with you, and he jerks in deep and fills you with a groan you're sure they can hear in the corridor."
    vn_sfx "Dopyu. Dopu, dopu."
    "When he's gone you pick up the manifests. On top of the pile, still warm, are twenty copies of your own breasts squashed flat on the glass. You shred them all."
    "Your hands are shaking. So are your thighs."
    $ vn_set_time(23, 0)
    $ sef_grow(3)
    $ vn_enter(bg="sef_mirror", pc="dazed", pc_tag="sef_pc", cast=[], cg="sef_mirror_three")
    "{color=#ff5fb8}Bigger again. You'd swear to it. You hold them up in the mirror and they overflow your hands on every side, a heavy soft E cup that sways when you breathe and pulls the skin of your chest taut. Natsuki's blouse is never going to button again.{/color}"
    "{color=#ff5fb8}Your hair's grown too. It was at your shoulders on Thursday. Tonight it lies across your shoulder blades, black and glossy and heavier than any hair you've ever had.{/color}"
    "Two pills a day. Two men inside you, one stranger. You take the evening pill and stand there looking at it in your palm afterwards."
    "Then you go to bed and think about the train until you have to touch yourself, and then you think about Ooba, and that's worse, and you come twice."
    call sef_cut(7, 2, "Wednesday.")
    jump sef_review

## ---- 4. Wednesday: the review, and the check-up -----------------------------------------------------------------

label sef_review:
    $ sef.fit = "office"
    $ vn_set_time(7, 42)
    $ vn_enter(bg="sef_train", pc="flustered", pc_tag="sef_pc", cast=[("sef_grey", "grin")], cg="sef_same_carriage")
    "Wednesday's 7:42 is as packed as Monday's. You tell yourself you'll take a different carriage. You get on at the same door."
    "He's there. The man in grey, reading his phone, as if he's been there all along."
    "When the doors close and the crowd presses in, his hand finds you before the train has even started moving."
    "You don't elbow him this time. You don't do anything."
    "You stand with your forehead on the glass and let him slide his hand up your skirt, and you're already wet from waiting for it, and he knows: he huffs a quiet laugh into your hair."
    sef_grey "\"Good morning to you, too.\""
    "He doesn't make you come this time."
    "He just strokes you, slow and light, the whole way to Shinjuku, round and round and never quite enough, until you're up on your toes pushing back against his hand and biting your lip to keep quiet."
    "Then the doors open and he takes his hand away and is gone, and you walk to the office soaked and aching for it and furious with yourself, and all day long you can't think about anything else."
    "Which is, it turns out, exactly the state Section Chief Tsuge finds you in at six o'clock."
    $ vn_set_time(18, 10)
    $ vn_enter(bg="sef_meeting", pc="stern", pc_tag="sef_pc", cast=[("sef_tsuge", "stern")], cg="sef_review_table")
    "Section Chief Tsuge keeps you back after six. Forties, a thin tie, reading glasses on a cord, a man who has never once in two years said your name without sighing."
    "He sits you down in the small meeting room and slides a form across the table."
    sef_tsuge "\"Your probation review. Under the circumstances, HR feels it should be redone. New hire, new review. Your contract's up for renewal at the end of the month.\""
    "He's ticked three boxes in the column marked UNSATISFACTORY. There's a space at the bottom for your signature."
    sef_tsuge "\"Of course, these things can be revised. If an employee shows... commitment.\""
    "He takes his glasses off and folds them and looks at you over the table. At your blouse."
    menu:
        "The pen's in front of you."
        "Refuse to sign":
            sef_you "\"I'm not signing that. Two years I've done the manifests for this whole floor without one mistake.\""
            sef_tsuge "\"Then perhaps a man would have kept his job.\" He comes round the table. \"Let's see what Sena-san can offer instead.\""
            $ sef.held += 1
        "Ask what he wants":
            sef_you "\"What does commitment look like, Section Chief?\""
            sef_tsuge "\"Stand up. Turn round. Hands on the table.\""
            $ sef.gave += 1
    show cg sef_on_the_table onlayer cgl
    "He lays you face-up on the meeting table among the folders, pushes the blouse open and the bra up, and stands there between your knees looking at your breasts for a long silent moment, the way he looks at a spreadsheet he doesn't like."
    "Then he takes a nipple in his mouth, hard, and pushes your skirt up, and fucks you on the table where you've sat through a hundred Monday meetings."
    vn_sfx "Gishi. Gishi. Pan. Pan."
    sef_tsuge "\"Commitment, Sena-san. Show me.\""
    menu:
        "He's fucking you slowly."
        "Grip the table":
            "You grip the edge of the table so hard your knuckles go white and stare at the ceiling tiles and try to be furniture."
            $ sef.held += 1
        "Push back on him":
            "Your heels go round the backs of his thighs and pull him in. You don't decide to. The appetite does."
            $ sef.gave += 1
    sef_you "\"Ahh♡— Section Chief— ahh— it's {i}deep— ahh♡—\""
    sef_tsuge "\"Unsatisfactory,\" he says, between strokes, very calm. \"Unsatisfactory. Ahh. Satisfactory.\""
    sef_you "\"I'm— coming— I'm coming on the {i}table— HAAAHH♡—!\"" with vnfx("flash", "shake")
    "You come with the folders sliding off the table round you, and he holds your hips and comes inside you with one long breath through his nose, and then he straightens his tie."
    vn_sfx "Byuru. Byururu."
    "He crosses out the three boxes and ticks EXCEEDS EXPECTATIONS and initials it."
    sef_tsuge "\"Contract renewed. I'll want a monthly review, Sena-san. Same room.\""
    $ vn_set_time(19, 30)
    $ vn_enter(bg="sef_exam", pc="flustered", pc_tag="sef_pc", cast=[("sef_hayami", "calm")], cg="sef_measuring")
    "Dr Hayami measures you with a tape and writes the number down twice to be sure."
    sef_hayami "\"Ninety-eight under the arms. You were eighty-eight a week ago. That's faster than I projected. Much faster.\" She doesn't sound worried. She sounds delighted."
    sef_hayami "\"And how's the appetite?\""
    menu:
        "She's waiting, pen ready."
        "Ask what's happening to you":
            sef_you "\"What {i}is{/i} the appetite? You keep saying it like it's—\""
            $ sef.held += 1
        "Ask for more of it":
            sef_you "\"Is there a pill that makes it {i}stop?{/i} Or— is there one that makes it— more?\" You hear yourself. Your face burns."
            $ sef.gave += 1
    sef_hayami "\"Sex drive, Sena-san. I mean your sex drive. I didn't build you a body and then leave it with a man's lukewarm idea of wanting. Every dose turns it up a notch.\""
    "She takes off her glasses."
    sef_hayami "\"Tell me honestly. Since Saturday, how many men?\""
    "You tell her. Gonda. A stranger on the train. Ooba. Tsuge, an hour ago. She writes it all down."
    "Then she asks how many times you came, and you tell her that too, and she smiles."
    sef_hayami "\"That's not a side effect. That's the treatment working. Lie back. Feet up. I want to test something.\""
    show cg sef_strap_on onlayer cgl
    "She unbuttons her white coat. Under the black dress she's wearing a harness, and on the harness a thick, glossy, pale pink cock, ridged, curved up at the tip."
    sef_hayami "\"This one's mine. I made it for you. It's the right shape for where I put everything.\""
    "She climbs onto the table between your knees and pushes it into you, and it's {i}exactly{/i} the right shape; the curve rides straight up over the spot inside you on every stroke, and you hear yourself wail."
    vn_sfx "Nuchu. Nuchu. Gishi. Gishi."
    sef_you "\"Doctor— Doctor♡— that's— that's {i}cheating— ahh♡— ahh♡—\""
    sef_hayami "\"Out loud, Sena-san. Count them for me.\""
    sef_you "\"One— AHH♡—!\"" with vnfx("flash", "shake")
    sef_you "\"Two— two— oh god— hahh♡—\""
    sef_you "\"Th— three♡— THREE♡—!\"" with vnfx("flash", "shake")
    "You stop being able to count somewhere after five."
    "She keeps going, steady as a metronome, writing between strokes with her free hand, until you're limp and drooling on her paper sheet and still twitching round the cock every time she moves."
    sef_hayami "\"Seven. Excellent.\" She pulls out, and you moan at the loss. \"Keep taking your pills.\""
    $ vn_set_time(23, 0)
    $ sef_grow(4)
    $ vn_enter(bg="sef_mirror", pc="dazed", pc_tag="sef_pc", cast=[], cg="sef_mirror_four")
    "{color=#ff5fb8}Ninety-eight under the arms, she said, and in the mirror they look more than that already: round and heavy and full, an F cup, that sit on your chest like two warm weights and press together on their own.{/color}"
    "{color=#ff5fb8}Your nipples are wide and dark pink and stand out through anything you wear.{/color}"
    "{color=#ff5fb8}And your hair is changing colour. The last few centimetres at the ends have turned a deep plum, dark red-purple, as if they'd been dipped in wine. It wasn't there this morning.{/color}"
    "You lift the plum tips and let them fall over your breasts and watch them for a long time."
    call sef_cut(19, 2, "Friday.")
    jump sef_ryouta
