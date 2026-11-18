## THE STORY: chapters 6-7 and the endings (PLAN.md). Sunday he hears himself; Monday the fluid lets go and the week lands
## at once; the pool; the deciding choice (both marked as endings): Climb out -> A "Climbed Out", Sink back -> B "Sank Back".
## pfl.held / pfl.slipped colour each epilogue (pfl_thought_line); pfl.pride / pfl.grace colour the bounty in A.

## ---- 6. Sunday: the first crack -----------------------------------------------------------------------------------

label pfl_sunday:
    $ pfl.fit = "nude"
    $ pfl_grow(6)
    $ vn_enter(bg="pfl_dark", pc="puzzled", pc_tag="pfl_pc", cast=[], cg="pfl_the_sound")
    "There's a sound."
    "The first sound in all this time, the first thing but the sweetness and the warmth and Mother's voice: faint, far off, like someone in another room of a very big house."
    "Someone's down here with you. Someone's... it's a voice. High and breathy and wordless, rising and falling."
    "It sounds like someone who's very happy, or very much in pain, and then it rises and breaks on something like a laugh, and you know it isn't pain."
    "You listen harder, and the words start to come through."
    pfl_you "{size=-8}\"...more... ahh... more, please, more...\"{/size}"
    "Some poor soul. Another one who fell. You must pray for them, when you've finished resting."
    "And then the voice says your name, the way you'd say it: {i}Aubin{/i}, with the lift at the end that only you put on it—"
    "No. The way {i}you{/i} say it. In your accent, from your mouth."
    "It's your voice."
    menu:
        "You're hearing yourself."
        "Stop your ears":
            "You stop your ears. You can't feel your hands, but you stop them anyway, with everything you've got, the same way you held your breath against the sweetness. It's not you."
            "It can't be you. You're kneeling here in the dark, perfectly calm, saying your prayers."
            "The voice gets fainter. It doesn't stop."
            $ pfl.held += 1
        "Listen":
            "You listen. You can't not. It's your own voice, moaning, begging, sweeter than you've ever heard it, and every time it says {i}more{/i} something in you wants to say it along with it."
            "You listen for a long time."
            $ pfl.slipped += 1
    $ vn_set_time(11, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_everything")
    "{color=#7fe8c0}The Hollow is letting the fluid thin. Not all at once. Just enough. Just to let the first of him through, the way you'd crack a door to let a cat smell the room before you open it.{/color}"
    "{color=#ff5fb8}His arse is massive now: two great soft globes that spread wide across the coils, heavy enough to sway him when they move him, so full and round that his narrow waist looks drawn in with a pen above them.{/color}"
    "{color=#ff5fb8}His thighs are thick and soft and press together. His hips are wide as a doorway.{/color}"
    "{color=#ff5fb8}His chest is soft, his lips plump and pink, his cock smaller and smooth and so sensitive it twitches in the air.{/color}"
    "{color=#ff5fb8}His hair falls to his waist in mint waves, glowing in the pit's light, and only the roots are still honey-gold.{/color}"
    "{color=#7fe8c0}And today the Hollow uses every part of him at once.{/color}"
    show cg pfl_all_of_him onlayer cgl
    "{color=#7fe8c0}The eldest in his arse, slow and deep. A tentacle in his mouth. The mouths on his nipples, the sleeve on his cock, the coils kneading that enormous arse round the one inside it, and another, slim and slick, pressing in alongside the eldest, opening him wider.{/color}"
    vn_sfx "Gupu. Jupo. Chuu. Pan. Pan."
    pfl_you "\"Mmh♡— mmmh— ahh— more— ahh♡— more, please, more—\""
    "{color=#7fe8c0}And far down in him, for the first time, he hears it.{/color}"
    $ vn_set_time(15, 0)
    $ vn_enter(bg="pfl_dark", pc="flustered", pc_tag="pfl_pc", cast=[], cg="pfl_matins")
    "It's the hour for Matins, or near enough. You've lost the hours, but your body hasn't; something in you always stands up at three."
    "The voice is still going. Your voice. Begging for more."
    menu:
        "Matins."
        "Sing Matins over it":
            "You sing Matins over it. Loud, every word, the full office, the way the whole Order sings it at three in the morning with the candles guttering."
            "You sing until you can't hear anything else."
            "You almost can't hear anything else."
            $ pfl.held += 1
        "Hum along with it":
            "You hum along with it. You don't mean to. It's a tune, after all, a sort of tune, rising and falling, and you've never been able to hear a tune without humming."
            "It's the sweetest thing you've ever sung."
            $ pfl.slipped += 1
    call pfl_cut(5, 1, "Monday. The seventh morning.")
    jump pfl_monday

## ---- 7. Monday: the Hollow lets go ----------------------------------------------------------------------------------

label pfl_monday:
    $ pfl.fit = "nude"
    $ pfl_grow(7)
    $ vn_set_time(5, 40)
    $ vn_enter(bg="pfl_pit", pc="shocked", pc_tag="pfl_pc", cast=[], cg="pfl_it_lands")
    "The sweetness goes first. Then the warmth. Then, all at once, like a dam going, everything else."
    "You can feel."
    "You can feel your hands, held in soft wet coils. Your feet. Your back on something that moves. Something in your mouth, slick and sweet, sliding out over your lips."
    "Something in your arse—two somethings—enormous, deep, {i}deep,{/i} moving. Mouths on your nipples. A wet, ridged grip round your cock, pulling."
    "And under all of it, a week. A week of it, every hour, every stroke, landing at once in every nerve you've got."
    vn_sfx "Byuru. Byuru. Byururu."
    pfl_you "\"Wh— what— AHHH♡— what is— oh Light, oh Light, oh {i}Light{/i}— ahh♡— AHHHHHHH♡—!\"" with vnfx("flash", "shake")
    "You come. You come so hard the world goes white."
    "You come and keep coming, your cock spurting in its sleeve, your arse clenching round the tentacles inside it, your mouth wide open and the sound pouring out of it, and this time you hear it."
    "You hear every note."
    "That was your voice. That was your voice all week."
    $ vn_set_time(6, 30)
    $ vn_enter(bg="pfl_pool", pc="dazed", pc_tag="pfl_pc", cast=[], cg="pfl_the_pool")
    "When you can think again, the light's come."
    "Far above, the moss has opened, and grey morning comes down the chute in a shaft and falls on a still pool at the bottom of the Hollow, and the tentacles carry you to its edge, gentle as hands, and set you on your knees in front of it."
    "You've never seen the Hollow before. Green-black walls that breathe. Glowing mint veins like a map of rivers. Tentacles everywhere, slow, patient, holding you."
    "It's the strangest thing you've ever seen, and you've seen the inside of a lich's vault."
    "Then you look down, into the water."
    show cg pfl_reflection onlayer cgl
    "{color=#ff5fb8}A hundred and sixty-three centimetres, kneeling.{/color}"
    "{color=#ff5fb8}Hair to your waist and past it, pooling on the stone, luminous mint all the way down, glowing faintly in the dark like the veins in the walls, with only a band of honey-gold left at the roots.{/color}"
    "{color=#ff5fb8}Your face is your face, still, green-eyed, but softer, the lips plump and pink and parted.{/color}"
    "{color=#ff5fb8}A soft chest, gently rounded, the nipples fat and dark from a week of sucking. A waist you could nearly close your hands round.{/color}"
    "{color=#ff5fb8}And below it, hips that flare out wide as a doorway and an arse so huge, so round and soft and heavy, that it spreads behind you on the stone like a second body, and shivers when you breathe.{/color}"
    "{color=#ff5fb8}Thick, soft thighs. Smooth skin everywhere. And between them your cock, smaller, smooth and pink, and hard again already, just from looking.{/color}"
    "Still you. Brother Aubin Lisle. Every inch of it you."
    pfl_you "\"...Oh.\""
    "The voice in your head doesn't come. Instead, the whole Hollow hums, low and long and glad, all round you, through the stone, through your knees."
    "Through the tentacles that are still, you realise, inside you, and in no hurry at all."
    "Above you, the shaft of daylight. The chute isn't steep. A strong priest could climb it in a minute."
    "Around you, the warmth, and the coils loosening, letting you choose."
    if pfl.slipped > pfl.held:
        "You already know which way your body's leaning. It's been leaning that way all week."
    else:
        "There's a hard bright thread in you still, after everything. It's pulling upward, toward the light. It's not pulling very hard."
    menu:
        "The light, or the Hollow."
        "Climb out" (ending=True):
            jump pfl_end_out
        "Sink back" (ending=True):
            jump pfl_end_in

## ---- the line the week's thinking earns -----------------------------------------------------------------------------

label pfl_thought_line:
    if pfl.held > pfl.slipped:
        "You still say the vows the old way: {i}clean.{/i} It takes you three tries some mornings to get the word to stay. You always get it there in the end."
    elif pfl.slipped > pfl.held:
        "You say the vows the new way now: {i}I keep my body open for the Light.{/i} It's truer. Nobody who hears you has ever noticed."
    else:
        "Some mornings the vows come out the old way, and some mornings the new. You've stopped minding which. The Light knows what you mean."
    return

## ---- Ending A: Climbed Out --------------------------------------------------------------------------------------------

label pfl_end_out:
    $ pfl.fit = "tatters"
    $ vn_set_time(9, 0)
    $ vn_enter(bg="pfl_wood", pc="flustered", pc_tag="pfl_pc", cast=[], cg="pfl_climbing_out")
    "You climb out."
    "It lets you. The tentacles slide out of you, slow, every inch of them, and you moan at it, out loud, and hear yourself, and go scarlet."
    "Then the coils lift you to the foot of the chute, and you climb."
    "At the top, something soft is pressed into your hands from below: the white veil, and a long strip of the habit, the gold-hemmed part, the Hollow must have kept them."
    "You tie the strip round your hips, where it barely covers anything, and pin the veil, and walk out of the wood into the morning with that enormous arse swaying behind you at every step."
    $ vn_set_time(11, 0)
    $ vn_enter(bg="pfl_village", pc="flustered", pc_tag="pfl_pc", cast=[("pfl_reeve", "stare")], cg="pfl_return")
    "Fallowmere's green, mid-morning. Every door has someone in it, staring. You find you mind, for the first time in your life. You find you also rather like it."
    "Maud Fenner is at the well. She looks at you for a very long time."
    pfl_reeve "\"We thought you were dead. You've been gone a week.\""
    pfl_you "\"...A week.\""
    "She takes off her cloak without a word and puts it round your shoulders. It doesn't close over your hips. Nothing is ever going to close over your hips again."
    pfl_you "\"The wood's clean, Reeve. Nothing more will come out of it.\""
    pfl_reeve "\"How do you know?\""
    pfl_you "\"It's got what it wanted.\""
    if pfl.pride > pfl.grace:
        "She counts out the other fifteen crowns, and then, after a moment, five more, and closes your hand round them."
        pfl_reeve "\"For the... trouble.\""
    else:
        "She counts out all thirty crowns into your hand, and then, after a moment, five more."
        pfl_reeve "\"For the... trouble.\""
    $ vn_set_time(22, 0)
    $ vn_clock.day += 30
    $ pfl.fit = "habit"
    $ vn_enter(bg="pfl_clearing", pc="blissful", pc_tag="pfl_pc", cast=[], cg="pfl_out_epilogue")
    "A month later."
    "Fallowmere has a priest again: the parish asked, and the Mother House said yes."
    "You have a new habit, white and gold, let out at the hips twice by the Sisters' seamstress, who asked no questions, and still sits so tight across your arse that the whole village knows when you've walked past."
    "Mother Ysolde wrote, the week you came back. {i}I'm so glad you're well. I had no word from you all that week; I was beginning to fear.{/i} You read it three times."
    "She never heard you. She never answered."
    "You've told no one. You keep the hours, and you bless the fields, and you take the bounty money and fix the chapel roof."
    "And on certain nights, when the moon's down, you walk north into the wood with a lantern, to a round clearing ringed with birches, and set the lantern down, and take off your habit, and kneel at the edge of the moss."
    show cg pfl_out_night onlayer cgl
    "It opens for you like a mouth. You lower yourself in. And there's no sweetness now, no fluid, no warmth stealing your senses."
    "You asked it not to, the first night, and it hummed and didn't."
    "You feel all of it."
    vn_sfx "Nuchu. Gupu. Pan. Pan."
    pfl_you "\"Ahh♡— yes— there, there— fill me, fill me up, I can feel it, I can feel all of it— ahh♡—!\""
    "The eldest, slow and deep in your huge soft arse. The mouths on your nipples. The sleeve on your cock. Coils round your thick thighs, holding them open."
    "Your own voice, ringing off the walls, and you hear every note and you don't stop it."
    pfl_you "\"I'm coming— I'm coming— AHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byururu."
    "You're always home by three, for Matins. You've never missed it once."
    call pfl_thought_line
    call pfl_route_return("Climbed Out")

## ---- Ending B: Sank Back ----------------------------------------------------------------------------------------------

label pfl_end_in:
    $ pfl.fit = "nude"
    $ vn_set_time(6, 45)
    $ vn_enter(bg="pfl_pool", pc="blissful", pc_tag="pfl_pc", cast=[], cg="pfl_sinking")
    "You look up at the light for a long moment. Then you lean back, into the coils."
    pfl_you "\"No sweetness. Not this time. I want to feel it. All of it. I want to hear myself.\""
    "The Hollow hums, low and glad, and doesn't argue. Far above, the moss closes over the shaft of daylight, slow, like an eye shutting."
    "And the tentacles fold round you, every one, warm, and you feel every single one."
    $ vn_set_time(9, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_awake_in_it")
    # d1: in-everything no picture, failed 3 draws (QA findings-df8ae07c); awake-in-it stays up
    "The eldest slides back into you and you feel it go, every inch, deep, and your whole body shakes round it. Another beside it. One at your lips, and you open for it gladly."
    "The mouths on your nipples, the sleeve on your cock, coils kneading your massive arse round the two inside it."
    vn_sfx "Gupu. Jupo. Chuu. Pan. Pan. Pan."
    pfl_you "\"Mmh♡— ahh— yes— so full— I can feel it, I can feel all of you, I can hear me— ahh♡— more— more, please, more—\""
    "It's the same voice you heard yesterday, from far off. Now it's right here in your own mouth, and you mean every word."
    pfl_you "\"Keep me— keep me down here— I'm yours, I'm your priest, I'm yours— AHHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byururu. Dopyu."
    $ vn_set_time(23, 0)
    $ vn_clock.day += 60
    $ vn_enter(bg="pfl_clearing", pc="blissful", pc_tag="pfl_pc", cast=[], cg="pfl_in_epilogue")
    "Two months later."
    "The Order lists Brother Aubin Lisle as lost in Fallowmere wood."
    "A brother came from the Mother House to look, and found a round clearing ringed with birches, and smooth moss, and nothing else, and went home."
    "No more lures come out of the wood. No more sheep go in."
    "Every week Maud Fenner leaves a loaf at the edge of the clearing, without quite knowing why, and every week it's gone."
    "And on still nights, the village hears singing from the wood. Matins, at three, in a voice sweeter than any bells, rising and falling through the trees."
    "And after it, every night, the other sounds."
    "Nobody in Fallowmere talks about it. Nobody has ever gone to look."
    call pfl_thought_line
    call pfl_route_return("Sank Back")
