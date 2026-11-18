## THE STORY: chapters 0-2 (PLAN.md). Two narrators: Aubin's own (second person, plain) and the pit's truth (third person,
## mint {color=#7fe8c0}); TF prose pink. pfl.held / pfl.slipped count how his thinking goes; pfl.pride / pfl.grace colour day 0.
## None of it changes the body art (one fixed ladder).

## ---- 0. Monday: Fallowmere --------------------------------------------------------------------------------------

label pfl_fallowmere:
    $ pfl.fit = "habit"
    $ vn_enter(bg="pfl_village", pc="serene", pc_tag="pfl_pc", cast=[("pfl_reeve", "calm")], cg="pfl_arrival")
    "Fallowmere is forty houses, a mill, a green with a well on it, and a wood to the north that has gone bad."
    "You walk in down the middle of the green at two in the afternoon in the white habit of the Sisters of the Lamp, the long one, gold at the hem and cuffs, the veil pinned back off your face."
    "Every door on the green has someone in it, staring."
    "You don't mind. You've never minded. You know exactly how you look in white."
    "Brother Aubin Lisle, twenty-two, the strongest exorcist the Order of the Lamp has had in a hundred years. The Sisters' habit was never meant for a brother."
    "You asked for it at nineteen, and Mother Ysolde looked at you for a long time and said yes, and nobody in the Order has said a word about it since. Nobody would dare."
    "The reeve meets you at the well: a broad, weathered woman in her fifties with her sleeves rolled up and a ledger under her arm."
    pfl_reeve "\"You're the one the Mother House sent? I asked for a priest, not a... Well. Never mind what I asked for. Maud Fenner. I'm the reeve.\""
    pfl_you "\"Brother Aubin. And yes, I am the one. Tell me about your wood, Reeve.\""
    pfl_reeve "\"Things. Coming out of it at the edges since the spring. Soft things, pale, with green in them like veins. They don't bite, nobody's been hurt.\""
    pfl_reeve "\"But six sheep have gone, and a dog, and Tam Heddle's best ram, and every one of them walked {i}into{/i} the wood after one of those things like it was following its mother home.\""
    pfl_you "\"Lures.\""
    pfl_reeve "\"That's what the old women say. Lures for what, nobody likes to guess. Clear it, and the bounty's yours. Thirty crowns. The whole parish put in.\""
    "Thirty crowns would re-roof the chapel at the Mother House. Thirty crowns is a great deal of money for one afternoon."
    menu:
        "She has the purse right there on her belt."
        "Take half now":
            pfl_you "\"Half now, I think. So that I know the parish is serious, and you know that I am.\""
            "She counts out fifteen crowns without a word and you tuck them into your sleeve. She watches you do it the way people watch a cat."
            $ pfl.pride += 1
        "Pay me when it's done":
            pfl_you "\"Keep it until it's done. The Lamp doesn't take payment for work it hasn't finished.\""
            "Something in her face eases. She nods, once."
            pfl_reeve "\"Then good luck to you, Brother.\""
            $ pfl.grace += 1
    $ vn_set_time(15, 0)
    $ vn_enter(bg="pfl_wood", pc="smug", pc_tag="pfl_pc", cast=[], cg="pfl_hunt")
    "The wood is quiet in the wrong way: no birds, no wind in the leaves, a sweet smell under the rot like pears left too long in a bowl."
    "The first lure comes out of the bracken at you a hundred yards in."
    "It's the size of a hound and the shape of nothing in particular, pale and soft, veined with a green that glows faintly in the shade. It doesn't attack. It just looks at you."
    vn_sfx "Fwaaa."
    "You lift one hand and say three words of the Lamp, and the light comes out of your palm white-gold and clean, and the lure is gone, nothing left but a scatter of mint-coloured sparks on the moss."
    "The second, the same. The fifth, the ninth, the fourteenth."
    "They come out of the trees in ones and twos and you unmake them in ones and twos, walking, never once breaking stride, the hem of your habit not even muddy."
    "It isn't a fight. It's a stroll. You'd be bored if you weren't so very good at it."
    "They all run the same way when they run, though. North. Toward the middle of the wood."
    $ vn_set_time(17, 30)
    $ vn_enter(bg="pfl_wood", pc="serene", pc_tag="pfl_pc", cast=[], cg="pfl_last_lure")
    "By half past five there's only one left."
    "It's bigger than the others, and brighter, and it doesn't come at you at all: it sits in a patch of evening light and waits until you see it, and then it turns and goes, unhurried, into the trees."
    menu:
        "One left. Then the wood's clean, and the bounty's yours."
        "Run it down":
            "You hitch your habit up in one fist and run, which you never do, because you never have to, and the lure keeps exactly the same distance ahead of you whatever you do."
            $ pfl.pride += 1
        "Follow it softly":
            "You follow at a walk, quiet, patient, reading the ground the way you were taught. It never gets further away. It never lets you get closer."
            $ pfl.grace += 1
    "Into a clearing. Round, flat, mossed over, ringed with birches, the sweet smell so thick here you can taste it. The lure stops dead in the middle and turns to face you."
    "You raise your hand. You say the first word of the Lamp."
    "And the moss under your feet opens like a mouth."
    vn_sfx "Zuruu—"
    $ vn_enter(bg="pfl_dark", pc="shocked", pc_tag="pfl_pc", cast=[], cg="pfl_the_fall")
    "You fall. A short way, a slide, a soft wet chute of something that isn't earth, and then a landing that should have hurt and doesn't."
    "Then a spray of something warm across your face. Into your mouth. Into your eyes."
    "And then nothing."
    "Not dark. Not silence. {i}Nothing.{/i} You can't feel the ground. You can't feel your hands. You can't feel the habit on your skin, or your own weight, or whether you're lying or kneeling."
    "There's no up. There's no cold. You can think, and that's all you can do."
    "It's a very strange feeling, to feel nothing. You consider it, carefully, the way you'd consider a passage of scripture you didn't understand."
    "Paralysis. Some swamp-wights spit a venom that does this; you read about it in the Order's bestiary in your first year in the Order. It wears off."
    "You fell, you were careless for the first time in your life, and now you'll lie still for an hour or two until it passes, and then you'll climb out, finish the last lure, and collect thirty crowns."
    "You're not afraid. You've never been afraid of anything in your life, and it seems a poor time to start."
    "You decide that you're kneeling. You decide that your hands are folded. And you begin Vespers, in your head, from the top."
    $ pfl.fit = "nude"
    $ vn_set_time(19, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_first_night")
    "{color=#7fe8c0}He is not kneeling. He is lying on his back at the bottom of the Hollow, in a bed of tentacles that have been waiting forty years for him, and they are taking his habit off.{/color}"
    "{color=#7fe8c0}They don't tear it.{/color}"
    "{color=#7fe8c0}The fluid they coat it with eats cloth, slowly, sweetly, and the white habit with the gold at the hem comes away in soft wet scraps, and the veil after it.{/color}"
    "{color=#7fe8c0}Then the strongest priest of the Lamp is lying naked in the dark, slim and pale, honey-blond hair spread over the coils, held by the wrists and the ankles and the waist.{/color}"
    "{color=#7fe8c0}The Hollow looks at him a long time, in the way it looks at things. Then a slick, mint-veined tentacle winds round his cock, and begins to stroke.{/color}"
    vn_sfx "Nuchu. Nuchu. Nuchu."
    pfl_you "\"Ah— ahh— hah♡—\""
    "{color=#7fe8c0}His mouth says that. He doesn't hear it. In his head, he's on the second psalm of Vespers, and getting every word right.{/color}"
    "{color=#7fe8c0}His cock is hard in its grip in a minute. His hips start to lift into the stroke, his thighs to shake, his breath to come quick, and his mouth goes on making sounds all by itself.{/color}"
    pfl_you "\"Mmh— ahh— ahh♡— ah— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru."
    "{color=#7fe8c0}He comes across his own belly, hard, back arched off the coils. The tentacles lap it up. Inside his head, Brother Aubin says \"Amen\" at the end of Vespers, calmly, and begins Compline.{/color}"
    "{color=#7fe8c0}The Hollow is very pleased with him.{/color}"
    call pfl_cut(7, 1, "Tuesday. He thinks it's still Monday evening.")
    jump pfl_tuesday

## ---- 1. Tuesday: the light ------------------------------------------------------------------------------------------

label pfl_tuesday:
    $ pfl.fit = "nude"
    $ pfl_grow(1)
    $ vn_enter(bg="pfl_dark", pc="serene", pc_tag="pfl_pc", cast=[], cg="pfl_dark_waiting")
    "Compline, and the night office, and the whole of the Psalter twice through. It must be well past dark by now. It must be nearly midnight."
    "The paralysis hasn't passed. That's interesting. Longer than the bestiary said. A stronger venom, then, or more of it. You aren't worried."
    "You'll simply have to be clever instead of patient."
    "You can't feel your hands, but you know where they ought to be. A priest of the Lamp doesn't need to feel his hands to make light; he only needs to mean it."
    menu:
        "Which light?"
        "The Lamp of Saint Orrin":
            "The Lamp of Saint Orrin: the first one every new brother learns, the steady one, the one that burns as long as you hold it."
            "You hold it in your mind like a candle and pour yourself into it."
        "The Dawn Canticle":
            "The Dawn Canticle: the bright one, the one that clears a crypt in a single word. You sing it in your head, all four lines, as loud as you can, and pour yourself into it."
    vn_sfx "Fwaaaa—"
    "You feel it go out of you. You feel that much; it's your own power, it lives in your head and your chest, not your skin."
    "A great clean flood of it, all at once, the most you've ever poured into one spell."
    "Nothing happens. No light. Still nothing at all."
    "How odd. It went {i}somewhere.{/i}"
    $ vn_set_time(9, 30)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_drinking")
    "{color=#7fe8c0}It went into the Hollow. Two tentacles are fastened on his upturned palms like mouths, and when the light comes it comes out white-gold through his skin and they drink it, every drop, swallowing, and the whole pit shudders round him with pleasure.{/color}"
    "{color=#7fe8c0}This is what it eats. This is what it has been waiting forty years for: not sheep, not dogs, not a ram. A priest. The strongest one it could find, and it sent its lures out for a year until he came.{/color}"
    "{color=#7fe8c0}And it spends what it eats on him.{/color}"
    "{color=#ff5fb8}His lips are fuller this morning, softer, pinker. His waist has come in at the sides, smoother. His hair has grown past his shoulders overnight, and at the very ends, in the glow of the pit's veins, the honey-blond has turned a faint luminous mint.{/color}"
    "{color=#7fe8c0}Two more tentacles end in soft wet mouths, and they fasten on his nipples, and suck. The one round his cock begins again, slow.{/color}"
    vn_sfx "Chuu. Chuu. Nuchu."
    pfl_you "\"Hah— nn— my— ahh♡— ahh—\""
    "{color=#7fe8c0}His nipples swell in the mouths. His back arches. His mouth falls open and stays open.{/color}"
    pfl_you "\"Ahh♡— more— ahh, more— ahh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru."
    "{color=#7fe8c0}\"More,\" his mouth said. Inside his head, he is wondering where the light went.{/color}"
    $ vn_set_time(14, 0)
    $ vn_enter(bg="pfl_dark", pc="dazed", pc_tag="pfl_pc", cast=[], cg="pfl_warm_dark")
    "You try again later. The same: the flood out of you, and nothing. Then once more, and the same."
    "You're tired after the third. That's new; you've never been tired from casting in your life. A pleasant sort of tired, though. Heavy. Like after a hot bath."
    "It occurs to you that the dark is rather pleasant, actually. Warm. You hadn't noticed it was warm."
    menu:
        "Rather pleasant. You turn the thought over."
        "Correct the thought":
            "No. It isn't pleasant. It's a trap, and you're in it, and you're a priest of the Lamp, and you'll be getting out."
            "You set the thought aside the way Mother Ysolde taught you to set aside a vanity."
            "It goes, mostly. The warmth doesn't."
            $ pfl.held += 1
        "Let it be pleasant":
            "Well, why shouldn't it be? You can't do anything until the venom passes. You may as well be comfortable while you wait. There's no sin in being comfortable."
            "You let yourself sink into it the way you'd sink into a feather bed."
            $ pfl.slipped += 1
    "{color=#7fe8c0}In the dark, the Hollow strokes his hair, very gently, all the way to its mint-coloured ends.{/color}"
    call pfl_cut(7, 1, "Wednesday. He thinks it's still Tuesday morning.")
    jump pfl_wednesday

## ---- 2. Wednesday: the purification ----------------------------------------------------------------------------------

label pfl_wednesday:
    $ pfl.fit = "nude"
    $ pfl_grow(2)
    $ vn_enter(bg="pfl_dark", pc="puzzled", pc_tag="pfl_pc", cast=[], cg="pfl_the_smell")
    "Something has come through. The first thing in all this time: a smell. Sweet, like pears, like honey in warm milk, so faint you think at first you've imagined it."
    "The miasma. Of course. You smelled it in the clearing before you fell."
    "That's what's keeping you down here: not a venom, a miasma, a foul air, and the Lamp has a prayer for foul air."
    "You feel almost foolish. Anyone in their first year at the Mother House would have thought of it."
    menu:
        "Purify what?"
        "Purify the air":
            "You purify the air. The Rite of Clean Breath, the long form, all nine verses, every one of them meant."
        "Purify yourself":
            "You purify yourself. If the miasma's in you, it's in you; you'll burn it out from the inside. The Rite of the Clean Vessel, all nine verses, every one of them meant."
    vn_sfx "Fwaaaa—"
    "Out it goes. The flood, the great clean pour. More of you than yesterday, even; you hold nothing back."
    "And again: nothing. The smell is still there. If anything, it's sweeter."
    $ vn_set_time(10, 0)
    $ vn_enter(bg="pfl_pit", pc="moaning", pc_tag="pfl_pc", cast=[], cg="pfl_first_anal")
    "{color=#7fe8c0}The Hollow drinks it at his palms, every drop, and shudders, and this time it doesn't wait to spend it.{/color}"
    "{color=#ff5fb8}His hips have begun to widen, a soft new curve below a waist that's narrower than yesterday. His backside is rounder, fuller, pushing out over the coils that hold it.{/color}"
    "{color=#ff5fb8}His hair lies on his shoulder blades now, and the mint has crept up from the ends to the length of a hand.{/color}"
    "{color=#7fe8c0}They turn him over onto his knees, gently, and spread him. A slim tentacle, slick with the fluid, slides between his cheeks and circles his hole, and circles, and presses in.{/color}"
    vn_sfx "Nuru. Nuruuu."
    pfl_you "\"Hh— hah— something— ahh♡— in— ahh—\""
    "{color=#7fe8c0}It goes in slowly, an inch at a time, and the fluid does what it does: there's no pain, nothing tight, only his body opening round it like it was built to, and his mouth sighing with every inch.{/color}"
    "{color=#7fe8c0}It finds the place inside him that makes his hips jump. It stays there. It presses.{/color}"
    vn_sfx "Juppu. Juppu. Juppu."
    pfl_you "\"Ahh— there— ahh♡— there, there, there— ahhh♡—\""
    "{color=#7fe8c0}It fucks him, slow and deep, while he kneels in the dark in his head and wonders why the Rite of Clean Breath didn't work. His cock drips onto the coils without being touched. His arse rocks back onto the tentacle on its own.{/color}"
    pfl_you "\"Fuck— ahh♡— fuck me— I'm— I'm— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byururu."
    "{color=#7fe8c0}He comes from his arse alone, the first time in his life, and doesn't know it. The tentacle stays inside him afterward, as if it lives there now.{/color}"
    $ vn_set_time(16, 0)
    $ vn_enter(bg="pfl_dark", pc="dazed", pc_tag="pfl_pc", cast=[], cg="pfl_breathing")
    "The smell has got stronger all day. Sweet pears, warm milk. It fills your head where your body used to be."
    "You've been breathing it all along, you suppose, but now you notice yourself breathing it, the way you notice your own heartbeat when you lie awake."
    menu:
        "Sweet. Very sweet."
        "Hold your breath":
            "You hold your breath, or try to: you can't feel your chest, so you hold the idea of it instead, and count. It's the only fight you've got left, so you fight it."
            "You get to two hundred before the sweetness comes back anyway."
            $ pfl.held += 1
        "Breathe it in":
            "You breathe it in. Deep. It's not as though you can stop, and it's so {i}nice,{/i} like the kitchen at the Mother House on baking days, and you were always sneaking in there."
            "You breathe it in for a long time, and smile, and don't know you're smiling."
            $ pfl.slipped += 1
    if pfl.slipped > pfl.held:
        "{color=#7fe8c0}His mouth is smiling in the dark, wide, wet. The Hollow fills it with a soft tentacle, just to feel him suck, and he sucks.{/color}"
    else:
        "{color=#7fe8c0}His brow creases in the dark, for a moment, as if at a sum that won't come out. Then the tentacle in his arse moves, and it smooths.{/color}"
    call pfl_cut(7, 1, "Thursday. He thinks it's still Tuesday.")
    jump pfl_thursday
