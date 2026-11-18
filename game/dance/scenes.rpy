## THE STORY: chapters 3-5 (PLAN.md). Monday Lys at the river and the Unveiled together; Tuesday the counter-ward and the
## bathhouse, the cock's last time; Wednesday the cock gone and the first time as a woman.

## ---- 3. Monday: the river ------------------------------------------------------------------------------------

label dnc_monday:
    $ dnc.fit = "shift"
    $ dnc_grow(3)
    $ vn_enter(bg="dnc_temple_cell", pc="flustered", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_monday")
    "{color=#ff5fb8}Breasts. There's no other word for them this morning. Small, round, firm, sitting high on your chest, with nipples gone pink and tender, and they move when you breathe.{/color}"
    "{color=#ff5fb8}Your hips have started to flare under the shift. Your arse is rounder; you can feel it when you sit on the cot.{/color}"
    "{color=#ff5fb8}Your cock is the length of your thumb. Your hair's at your jaw, and more rose gold than brown now, soft and heavy, curling at the ends the way it never did.{/color}"
    $ vn_set_time(6, 30)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_river", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer")], cg="dnc_river_dawn")
    "Lys takes you down to the river at dawn, before the town's awake, to the flat rock under the willows where you used to swim in summer. Mist on the water. Birdsong."
    "Your tabard's tight across your chest now and you've wrapped it with a sash to hide the shape, and she unwinds the sash without asking."
    dnc_lys "\"Let me see you. Properly. I've been at the gate three nights and you won't let me look.\""
    "She looks. At your rose-gold hair, your soft face, your breasts. At the crest glowing faintly under your navel, the twin of the one under hers."
    dnc_lys "\"It's still your face. It's still your eyes. Aren, I still want you. Mine aches for you all day, did you know that? Not for them. For you.\""
    menu:
        "She opens her arms."
        "Let Lys hold you":
            "You let her."
            "You put your face in her neck and she holds you, both of you kneeling on the cold rock, and her hands go up under your tabard and cup your new breasts, gently, like they're something precious, and you shiver."
            show cg dnc_river_lys onlayer cgl
            "Then her hand goes lower. Into your breeches."
            "Round your small soft cock, and she strokes it slowly, kissing you, crest to crest, the two marks warming each other through the cloth."
            dnc_lys "\"Still you. Still mine. Come for me, love. Just for me.\""
            dnc_you "\"Lys— Lys♡— ahh—\"" with vnfx("flash")
            "It's small and quiet and sweet, and it's the only time all week you come for someone you chose."
            $ dnc.held += 1
        "Pull away from Lys":
            "You pull back. You can't. Not like this, not with your body changing under her hands and Corvin's cellar still in it."
            dnc_you "\"Not yet. When it's over. When it's ours again.\""
            dnc_lys "\"...All right. I'll wait. I'm good at waiting.\""
            "She wraps the sash back round you herself, and kisses your forehead, and the two crests ache together, unanswered, all the way back up the hill."
    $ vn_set_time(21, 0)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_cellar", pc="moaning", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_cellar_all")
    "On Monday night the Unveiled don't want the dance. They want the dancer."
    dnc_corvin "\"Gentlemen. All of you. {b}Ysmeral. Take them all, dancer.{/b}\""
    show cg dnc_spitroast onlayer cgl
    "On the tasting table on your hands and knees, with the veils pushed up round your waist. Corvin behind you."
    "The ferryman in front, Tobin, big and red-bearded, feeding his cock into your mouth while Corvin pushes into your arse, and the two of them meet in the middle of you and rock you between them."
    vn_sfx "Juppu. Pan. Juppu. Pan."
    dnc_you "\"Mmph♡— mmh♡— mmmh♡—!\""
    "When they've both finished in you, the miller's sons. Then the cooper. Then a man whose name you don't know, who comes up from the street because he heard."
    menu:
        "Another one. Another. The crest is so bright you can read by it."
        "Count the strokes":
            "You count. You hold on to the counting like a rope: forty, forty-one, forty-two. As long as you're counting, some of you is still Aren Vale, sword-brother of the Veil."
            "Two hundred and six, and you lose it."
            $ dnc.held += 1
        "Lose count":
            "You lose count almost at once. You don't want to count. You want the next one, and the one after that, and you hear yourself say so."
            $ dnc.asked += 1
            dnc_you "\"Next♡— next one, please— don't stop— I'm not full yet—\""
    dnc_you "\"Ahh♡— ahh♡— AHH♡— I'm coming again— I keep coming— nothing's coming out— AHH♡—!\"" with vnfx("flash", "shake")
    "Your thumb of a cock twitches and gives nothing, again and again. The crest takes it all anyway. It doesn't need what comes out of you. It needs you to come."
    call dnc_cut(10, 1, "Tuesday. The fourth morning.")
    jump dnc_tuesday

## ---- 4. Tuesday: the counter-ward ------------------------------------------------------------------------------

label dnc_tuesday:
    $ dnc.fit = "shift"
    $ dnc_grow(4)
    $ vn_enter(bg="dnc_temple_cell", pc="dazed", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_tuesday")
    "{color=#ff5fb8}A real handful now, each of them, full and soft, a woman's breasts, bouncing when you sit up too fast. Your waist is narrow and your hips are wide, and the shift is too short for you now that it has to go over them.{/color}"
    "{color=#ff5fb8}Your hair's on your shoulders, rose gold to the last few brown ends. Your cock is almost nothing: a soft nub, and below it only smooth skin. Tomorrow, you think. Tomorrow it'll be gone.{/color}"
    $ vn_set_time(15, 0)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_archive", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_senna", "mage")], cg="dnc_counter_ward")
    "Senna's drawn a circle on the archive floor in salt and silver filings, three paces across, with symbols round the rim in a hand you can't read."
    dnc_senna "\"A ward ring. The name's just a sound. Inside this, the crest can't hear it. If you sit in it from nine till dawn, Corvin can shout himself hoarse, and you won't feel a thing.\""
    dnc_senna "\"And if the crest goes a whole night without feeding, maybe it slows. Maybe it stops.\""
    menu:
        "Maybe. It's the first maybe anyone's had."
        "Try the counter-ward":
            "You sit in the ring at half past eight, cross-legged, with Senna on a stool outside it and Lys beside her, holding your sword across her knees, like a guard."
            $ dnc.held += 1
        "Hide in the temple":
            "You don't trust it. You climb to the bell loft instead, alone, and bar the hatch, and sit with your back against the great bell in the dark."
    $ vn_set_time(23, 0)
    $ vn_enter(bg="dnc_archive", pc="moaning", pc_tag="dnc_pc", cast=[], cg="dnc_crest_hunger")
    "It works. That's the terrible part. Nine o'clock comes, and nobody calls the name, and nobody can, and you don't feel a thing."
    "And then at ten you feel everything."
    "{color=#ff5fb8}The crest doesn't need the name. It never did. It's hungry.{/color}"
    "{color=#ff5fb8}It's been fed four nights running and tonight it isn't being fed, and it wants, it wants. It burns under your navel like a coal.{/color}"
    "{color=#ff5fb8}The last soft nub of your cock is leaking through your breeches, and your nipples are stiff as pebbles, and your whole body is one mouth.{/color}"
    "By eleven you're on your feet. By a quarter past you're walking down the hill in the dark, alone. Nobody calls you. Nobody has to."
    $ vn_set_time(23, 45)
    $ dnc.fit = "nude"
    $ vn_enter(bg="dnc_bathhouse", pc="moaning", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_bath_corvin")
    "Corvin's in the hot pool at the bathhouse, alone, lamps on the water, as if he's been waiting for you all evening. He probably has."
    dnc_corvin "\"I wondered how long the mage's circle would hold you. Come here. You don't need me to say it any more, do you?\""
    dnc_you "\"...No.\""
    show cg dnc_bath_ride onlayer cgl
    "You get into the water. You climb into his lap."
    "You reach down, and take his cock in your hand, and set it against your arse, and sink, all by yourself, and nobody's said the name at all."
    vn_sfx "Zupuu."
    dnc_you "\"Ahh♡— yes— yes, that's it, that's what it wanted, that's what I— AHH♡—\""
    "You ride him."
    "Your new breasts bounce in the lamplight and slap wet against his chest, and the water slops over the edge of the pool, and the crest glows under the water like a sunk lantern."
    vn_sfx "Chapu. Chapu. Chapu."
    dnc_you "\"Corvin— Corvin, I'm— this is the last— I can feel it, this is the last time with it— AHH♡— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu."
    "And it's true. The last thin dribble from the last of your cock, lost in the bathwater, and something under your navel closes like a fist and then opens like a flower."
    if dnc.held >= 4:
        dnc_corvin "\"You held out longer than I thought. Good. I'd have been disappointed.\""
    else:
        dnc_corvin "\"Good girl.\""
    call dnc_cut(7, 1, "Wednesday. The fifth morning.")
    jump dnc_wednesday

## ---- 5. Wednesday: the first time --------------------------------------------------------------------------

label dnc_wednesday:
    $ dnc.fit = "shift"
    $ dnc_grow(5)
    $ vn_enter(bg="dnc_temple_cell", pc="dazed", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_wednesday")
    "{color=#ff5fb8}It's gone. You knew it would be. You put your hand down anyway, under the shift, and there's nothing there but soft, smooth skin, and below it the folds of a pussy, plump and pink and already wet at your touch.{/color}"
    "{color=#ff5fb8}Your breasts are full and heavy and press together when you lean forward. Your thighs are soft and round and touch all the way down. Your hair's past your shoulders, rose gold all of it, and when you say your own name out loud, your voice is a woman's.{/color}"
    dnc_you "\"Aren. Aren Vale.\""
    "It still sounds like a name. It's still yours."
    $ vn_set_time(10, 0)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_infirmary", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_senna", "mage"), ("dnc_lys", "dancer")], cg="dnc_exam")
    "Senna examines you in the infirmary with the curtains drawn and her face scarlet, as clinical as she can make herself, Lys holding your hand on the other side of the bed."
    dnc_senna "\"It's — complete. Down there, I mean.\" She coughs. \"The crest's changed. It sits lower now, right under your navel.\""
    dnc_senna "\"I'm sorry about the ring. It was the wrong idea. It doesn't run on the name. It runs on the hunger. The name's just a leash.\""
    dnc_lys "\"Then we cut the leash. There's still two nights. There's still something in those rolls.\""
    "Senna has to leave in a hurry, with her coat held closed in front of her. Lys pretends not to notice. Then she climbs onto the bed and holds you, and says nothing, for a long time."
    $ vn_set_time(21, 0)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_cellar", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_cellar_virgin")
    "The cellar's full tonight. Word's got round. Every barrel-end has a man on it."
    dnc_corvin "\"Gentlemen, our dancer has finished becoming a daughter of the Veil. I think that deserves a proper first time. Don't you?\""
    "They cheer. Corvin lays you down on the tasting table on your back, on the spread rose veils, and opens your thighs with his ringed hands, and looks."
    dnc_corvin "\"Now. I could say the name. Or you could ask.\""
    menu:
        "Your new pussy is soaking. The crest is pulsing in slow, deep beats, like a heart."
        "Say no":
            dnc_you "\"No. No, I won't ask. You'll have to make me.\""
            dnc_corvin "\"As you like. {b}Ysmeral.{/b}\""
            "{color=#ff5fb8}Your hips lift off the table on their own and your hands go down and spread yourself open for him with two fingers.{/color}"
            $ dnc.held += 1
        "Say please":
            dnc_you "\"...Please.\""
            dnc_corvin "\"Please what?\""
            dnc_you "\"Please fuck me. Please be the first. Please.\""
            $ dnc.asked += 1
    show cg dnc_first_pussy onlayer cgl
    "He pushes in slow."
    "The head first, stretching you, and the crest flares so hot it's almost white, and then all of him, one long smooth slide into a place that was never there before last night."
    vn_sfx "Nyuru. Zupuuu."
    dnc_you "\"AHHH♡— oh gods— it's inside— it's inside me— it's so much deeper than— AHH♡—\""
    "It's nothing like before. Before, it was a place he could reach. This is a place that's made for it."
    "Every stroke goes all the way to the crest and knocks on it, and it opens, and you scream."
    vn_sfx "Pan. Pan. Pan. Pan."
    dnc_you "\"Yes♡— yes♡— harder— AHH♡— I'm a woman, I'm a woman and you're fucking me, AHH♡— I'm coming— I'm coming like a woman— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu. Dopyuuu."
    "He comes inside you, deep, and you feel it this time, all of it, hot, filling, and the crest under your navel drinks and drinks and glows like a lamp."
    "Then the next man. And the next."
    call dnc_cut(8, 1, "Thursday. The sixth morning.")
    jump dnc_thursday
