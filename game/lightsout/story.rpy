## lightsout: one weekend, six games. HOUSE RULES: ch 1-2 forced (the deal stated once, flat), the break at the end of
## ch 2, the flip at ch 3, consensual after. Denial mode: every step is damage control, fairness, courtesy, scheduling.
## Femboy: the cock stays; anal and oral only; the chest small to the end; the ass and thighs big.

## ---- 1. The Ledge ------------------------------------------------------------------------------
label lto_ch1:
    $ lto.chapter = 1
    $ lto.fit = "own"
    $ vn_enter(bg="lto_ledge", pc="reasonable", pc_tag="lto_pc", cast=[], cg="lto_window_fall")
    "Twenty to midnight on a Friday, on the ledge outside the rented house next door, because four women live in it and one of them never closes her curtains."
    "You'd like it on record that you weren't looking in. You were looking {i}at{/i}: at the strip of warm light where her curtain doesn't meet the frame, which is a different thing, which is practically astronomy."
    "Then the old sash window slides up on its own, like the house has decided something, and you go through it head first, through a spider plant."
    "Then you're not on the ledge. You're on their living-room floor."
    hide cg onlayer cgl
    $ vn_enter(bg="lto_livingroom", pc="mortified", pc_tag="lto_pc", cast=[("lto_dani", "calm")], cg="lto_reveal")
    "Four of them, round a paused film and a tub of ice cream going hand to hand, in T-shirts and pants, or out of them. A spoon stops halfway to a mouth. Somebody's hand stops on the remote."
    "In the next thirty seconds you learn three things, in order. Dani Vaughn isn't wearing trousers. None of them are girls in the way you'd assumed. And every one of them is hung considerably better than you are."
    "Nobody screams. Jo leans forward from the armchair, entirely unbothered. \"You okay?\" Marissa has already started filming, red light on."
    hide lto_dani
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"He's fine.\""
    hide lto_marissa
    show lto_dani calm at vn_cast_slot
    lto_dani "\"You stay the whole weekend. Sleepover rules. Or Marissa sends that to campus security and the group chat.\""
    "She says it once, flat, standing over you. Nobody says it again."
    lto_you "\"I'll stay— I mean— I— right. Okay. Fine. Look, since there's evidence, and I'm here, and you, um, you have... leverage— terms. What are the terms, exactly—\""
    "You've agreed before she's finished. You negotiate anyway, like a man reading a lease."
    lto_dani "\"The terms are you stay. That's all the terms.\""
    lto_you "\"Right. Right. But practically. Meals. Bedtime. Is there a sofa, or is it more of a— I'm only asking so I can plan—\""
    lto_dani "\"There's a sofa.\""
    lto_you "\"Great. Good. That's— thank you. That's very reasonable. I appreciate that you've— thought about the sofa.\""
    hide lto_dani
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"This is the weirdest Friday since paintball.\""
    hide lto_dani
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"I just want to stress that I am recording with your consent, Colin.\""
    lto_you "\"I'm— consenting. Under protest. Under a {i}lot{/i} of—\""
    "Because what the hell else do you say to a phone."
    hide cg onlayer cgl
    hide lto_dani
    jump lto_titjob

label lto_ch1_after:
    hide cg onlayer cgl
    show screen lto_notes(1)
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Don't wipe it, that's good for acne.\""
    lto_you "\"That's not— I really don't think that's dermatologically—\""
    show lto_katie squeal at vn_cast_slot
    lto_katie "\"Wait, wait, do the size thing while he's still sticky! Measurements! We'll need these for craft night anyway.\""
    "Katie measures you against all four, out loud, with a ruler she owns for craft reasons, and writes it in Marissa's notebook \"for tomorrow\". Jo lines hers up beside yours like a club next to a pencil."
    show lto_katie squeal at vn_cast_slot
    lto_katie "\"Sorry, Colin, it's... honestly, it's adorable!\""
    lto_you "\"You can't measure someone against— look, there are averages, there are published averages, and I'm well within the— Jo, put it {i}away{/i}, it's not a {i}competition{/i}—\""
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Nothing wrong with being the bottom percentile, man.\""
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Evidence.\""
    lto_you "\"Of {i}what{/i}? It's a ruler. That's a craft ruler, it doesn't prove anything, it's not even metric—\""
    hide screen lto_notes
    "Your internal risk assessment: one weekend. Manageable. Buying silence."
    $ vn_enter(bg="lto_livingroom", pc="mortified", pc_tag="lto_pc", cast=[], cg="lto_sofa_night")
    "They put you on the sofa with a duvet that smells of somebody's perfume and turn the big light off, and one by one they go up to bed, and Jo pats your head on the way past like a dog's."
    "You lie in the dark in their living room with your face still sticky and listen to the house settle: four women's footsteps, four doors, someone laughing upstairs, a shower."
    "At some point Katie comes back down in a dressing gown for a glass of water, sees you awake, and tucks the duvet in round your feet without a word, as if you were a guest, as if this were normal, and pads back up. That's worse, somehow. You lie there feeling tucked in."
    "Your own house is right there, through the wall. You can see your bedroom window from the sofa. The light's still on in it. You left it on to go out on the ledge."
    "You don't sleep. You lie there being furious about the terms until about three, when you realise you're hard again, and that nobody's touched you, and that you're thinking about tomorrow, and you put the pillow over your face."
    call vn_night(18)
    jump lto_ch2

## ---- 2. Makeover Night -------------------------------------------------------------------------
label lto_ch2:
    $ lto.chapter = 2
    $ lto.fit = "nude"
    $ vn_enter(bg="lto_kitchen", pc="mortified", pc_tag="lto_pc", cast=[("lto_katie", "squeal")], cg="lto_wax")
    "Katie's night. A towel on the kitchen table, a pot of wax, brows, nails, and a skincare routine applied with real violence."
    lto_you "\"Before anything starts, I'd like to say I've never been waxed, I don't know my tolerance, and I'd like it noted that nobody's asked whether I—\""
    lto_katie "\"Arms up! Ooh, this is gonna be SO good.\""
    "Jo lifts you onto the table by the armpits like a child onto a bouncy castle and lays you down on the towel, and Katie stirs the pot, humming."
    "The first strip. You yelp. The second. You yelp louder."
    lto_you "\"{i}AHH{/i}— what— that can't be— Katie, that's not what wax {i}does{/i}—\""
    lto_katie "\"That's exactly what wax does! Big breath! Next one!\""
    lto_you "\"{i}AHHH{/i}— no— hang on— {i}hang on{/i}— is there a numbing— a cream, or a— {i}AHH{/i}—\""
    hide lto_katie
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"He's loud. I'll shut him up.\""
    hide cg onlayer cgl
    hide lto_katie
    jump lto_jo_mouth

label lto_ch2_after:
    hide cg onlayer cgl
    $ lto_body(2)
    $ lto.fit = "kit"
    $ vn_enter(bg="lto_livingroom", pc="flushed", pc_tag="lto_pc", cast=[("lto_katie", "squeal")], cg="lto_plugged")
    "{color=#f0b090}Smooth. All of you. The skin softening already. The shakes, Marissa says. Electrolytes, you've lost a lot of fluid.{/color}"
    lto_katie "\"One last thing! Turn over.\""
    lto_you "\"Turn over {i}why{/i}— what's that— Katie, what's the— is that a—\""
    lto_katie "\"It's a plug, silly! It's only the little one!\""
    "Katie plugs you afterwards \"so tomorrow goes easier\", with a fingertip of lube and a running commentary, and makes you keep it in through the film: some French horror thing Jo picked because the label said the orgy's in the second act."
    lto_you "\"{i}Ahh{/i}— oh— that's— that's very— that's {i}in{/i}, that's in now, okay—\""
    "You sit through it on a cushion between Katie and Jo, in Katie's dressing gown and nothing else, smooth all over and smelling of her oil, and every time you shift on the plug Katie says \"stop fidgeting, sweetie\" without looking away from the screen, like a mum in a car."
    hide lto_katie
    show lto_jo blunt at vn_cast_slot
    lto_you "\"So is anyone actually watching this, or—\""
    lto_jo "\"Shh. Second act.\""
    "The second act comes and goes. The orgy turns out to be four people in cloaks in a cellar, barely lit. Jo is furious about it."
    "You're hard the entire evening and not one person touches it. You keep trying to work it into the conversation."
    lto_you "\"It's warm in here, isn't it? I'm very warm. Physically. Is anyone else— no? Just me? Okay.\""
    show screen lto_notes(2)
    "Marissa writes that down."
    "She writes everything down. You've started listening for the scratch of the pen, and feeling, each time you hear it, obscurely, that you've done well."
    hide screen lto_notes
    hide cg onlayer cgl
    call vn_night(11)
    jump lto_ch3

## ---- 3. Truth or Dare --------------------------------------------------------------------------
label lto_ch3:
    $ lto.chapter = 3
    $ lto.fit = "kit"
    $ vn_enter(bg="lto_kitchen", pc="reasonable", pc_tag="lto_pc", cast=[("lto_marissa", "tease")], cg="lto_shakes")
    "Saturday morning, the kitchen, and Marissa pushing a pink shake across the counter at you and a little paper cup with two pills in it."
    lto_marissa "\"Electrolytes. And a supplement. You lost a lot of fluid last night, Colin. Drink up.\""
    lto_you "\"What's in it?\""
    lto_marissa "\"Strawberry.\""
    "You drink it. You take the pills. You tell yourself it'd be rude not to, and that you're a guest, technically, and that guests don't interrogate breakfast. Jo eats four eggs standing up and watches you drink it with great interest."
    hide lto_marissa
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Your skin's mad, man. Like a peach.\""
    lto_you "\"It's the wax.\""
    hide lto_marissa
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Sure.\""
    lto_you "\"It {i}is{/i}. It's the wax and the oil. Katie's oil. It's a very good oil.\""
    lto_jo "\"Turn your head. No, the other way. Mate, your jaw's gone soft.\""
    lto_you "\"My jaw hasn't {i}gone{/i} anywhere, it's the lighting, your kitchen has very flattering— is that a ring light? Why is there a ring light in your kitchen?\""
    "There's a ring light in the kitchen because Marissa films her breakfasts. You stand in it a lot longer than you need to, finishing the shake."
    hide cg onlayer cgl
    hide lto_marissa
    $ vn_enter(bg="lto_livingroom", pc="reasonable", pc_tag="lto_pc", cast=[("lto_marissa", "tease")], cg="lto_dares")
    "Saturday night. Truth or dare by house rules, Marissa writing the dares on slips in a bowl."
    lto_marissa "\"House rules tonight. No chickening. Rotation is clockwise.\""
    hide lto_marissa
    show lto_dani calm at vn_cast_slot
    lto_dani "\"First to bail washes the kitchen tomorrow. If you pick truth, Marissa's allowed to record.\""
    "The first dares are tame. Katie texts her mum a heart. Jo eats a spoonful of mustard and asks for another. Dani tells the room about her most embarrassing hospital visit, unbothered, and nobody can look at the sofa cushions the same way again."
    "Then the bowl comes round to you, and the slip says {i}sit in someone's lap till your next turn{/i}, and you sit in Jo's, because she's closest. You sit very still for a whole round while her cock hardens under you through her shorts, and you say nothing about it, and you don't get up."
    hide lto_dani
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Comfy?\""
    lto_you "\"It's a dare. I'm doing the dare. I'm committed to the integrity of the— yes. Quite comfy. Thank you.\""
    hide lto_jo
    show lto_dani calm at vn_cast_slot
    "You never pick truth. Not once. The chapter notices out loud exactly once."
    hide lto_dani
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Dare again? Interesting. Good call.\""
    lto_you "\"Truth's boring. Everyone knows that. Dares are more— communal.\""
    menu:
        "Steering the dares. Subtly."
        "Steer toward Jo":
            $ lto.dare = "jo"
            lto_you "\"I mean, statistically Jo hasn't had a turn, so it's only fair—\""
        "Steer toward 'whoever's closest'":
            $ lto.dare = "closest"
            lto_you "\"Whoever's closest, that's just efficient. Jo's closest. Coincidentally.\""
    "Strategy, you call it. Marissa lets you think you're being subtle, and writes it down."
    $ lto.asked = True
    hide cg onlayer cgl
    hide lto_marissa
    jump lto_jo_first

label lto_ch3_after:
    hide cg onlayer cgl
    $ lto_body(3)
    $ vn_enter(bg="lto_livingroom", pc="flushed", pc_tag="lto_pc", cast=[("lto_dani", "calm")], cg="lto_cage_on")
    "Between rounds Dani produces a small steel cage."
    lto_dani "\"The couch.\""
    lto_you "\"The couch is— that's not— I'm a— look, it's not like I'm going to ruin the—\""
    "One paragraph of argument. She puts it on you herself."
    "It clicks. It's a very small click, for what it means. Dani hands the key to Marissa, who threads it onto her lanyard with her house keys, and the four of them go back to the game."
    lto_you "\"It's actually quite comfortable. Ergonomically. I just want that noted.\""
    "After that, you never mention it again."
    show screen lto_notes(3)
    "{color=#f0b090}Hips. A waist starting. Your face soft enough now that the makeup stops looking like a costume.{/color}"
    hide screen lto_notes
    hide cg onlayer cgl
    hide lto_dani
    jump lto_ch4

## ---- 4. Movie Marathon -------------------------------------------------------------------------
label lto_ch4:
    $ lto.chapter = 4
    $ lto.fit = "nude"
    $ vn_enter(bg="lto_livingroom", pc="greedy", pc_tag="lto_pc", cast=[], cg="lto_marathon")
    "You come downstairs at nine in Katie's dressing gown and nothing else, the cage cold between your thighs, and sit on the rug in front of the TV with your knees together, and say \"so what are we watching?\" in a voice you've never heard from yourself. Jo says \"you, mate\", and that's the last line anyone remembers from the film."
    "A film is on. Nobody watches it. Shifts, all night, rotating through all four while the menu screen loops."
    jump lto_marathon_scene

label lto_ch4_after:
    hide cg onlayer cgl
    $ lto_body(4)
    $ lto.fit = "kit"
    $ vn_enter(bg="lto_livingroom", pc="flushed", pc_tag="lto_pc", cast=[("lto_katie", "squeal")], cg="lto_bra_kept")
    "{color=#f0b090}At five in the morning Katie notices your ass and thighs, properly arrived, and screams.{/color}"
    lto_katie "\"Oh my GOD. Turn around. Turn around! Jo! Jo, look at his— look at {i}her{/i}— look at the {i}ass{/i}!\""
    lto_you "\"It's the angle. It's because I've been kneeling. It's water retention, it's— Katie, it's {i}five in the morning{/i}—\""
    lto_katie "\"Put this on! One photo, one, I promise!\""
    "Her stuffed bra goes on you for a photo. You keep it on after the scene ends, and don't mention that either."
    "You've stopped getting properly hard. You leak through the cage all night. The pills, you decide."
    lto_you "\"It's the pills. It's definitely the pills. That's a known— they'd have that on the leaflet.\""
    "You say it twice, to Katie, who agrees with you both times in the voice she'd use on a cat."
    show screen lto_notes(4)
    "Someone occasionally reacts to a plot point nobody has seen."
    hide screen lto_notes
    hide cg onlayer cgl
    call vn_night(10)
    jump lto_ch5

## ---- 5. Sunday Brunch --------------------------------------------------------------------------
label lto_ch5:
    $ lto.chapter = 5
    $ lto.fit = "dress"
    $ vn_enter(bg="lto_store", pc="mortified", pc_tag="lto_pc", cast=[], cg="lto_store_maam")
    show lto_katie squeal at vn_cast_slot
    lto_katie "\"You're wearing this! Jo's got the shower, so you've got five minutes, and then you're mine.\""
    lto_you "\"I'm going to look like a clown.\""
    show lto_katie squeal at vn_cast_slot
    lto_katie "\"You couldn't look ridiculous if you tried. He's wearing the platforms. We want him seen.\""
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Rolling. Smile, brunch girl!\""
    "They take you out. Katie's dress, Katie's shoes, full makeup, and a corner store round the corner."
    "A guy from your Tuesday lecture holds the door for you."
    "You know him. He sits two rows behind you in thermodynamics and once borrowed your calculator and never gave it back. He looks at you for a full second, top to bottom, the dress, the heels, the lipstick, and doesn't know you at all."
    lto_guy "\"After you, ma'am.\""
    menu:
        "Ma'am."
        "\"Thank you!\"":
            $ lto.maam = "thanks"
            lto_you "\"Thank you!\""
            "In a voice you don't examine: soft, singsong, light. No edge at all."
            show lto_katie squeal at vn_cast_slot
            lto_katie "\"See? Totally passed! Not a flicker! I knew that dress was right.\""
            show lto_jo blunt at vn_cast_slot
            lto_jo "\"You're blushing like it's your first date.\""
        "Say nothing and hurry past":
            $ lto.maam = "hurry"
            "You hurry past in Katie's heels, face burning, and he watches your ass all the way to the fridges."
    hide cg onlayer cgl
    $ vn_enter(bg="lto_store", pc="flushed", pc_tag="lto_pc", cast=[("lto_katie", "squeal")], cg="lto_brunch")
    "Then brunch, at the café on the corner, at a window table, in the dress, with your legs crossed because Katie said so, and the waitress calling you {i}love{/i} and asking if you'd like to see the cake menu."
    lto_you "\"Oh, I'm not really a cake person, I'm more of a—\""
    lto_katie "\"She would. She absolutely would.\""
    "You eat a slice of something with lemon in it and laugh at Jo's story about paintball in the new soft voice, and three times you catch a man at another table looking at you, and three times you look back, and the third time you smile."
    "He smiles back. Thirty, maybe, a nice watch, and he lifts his coffee cup an inch, and you feel it in your stomach and in the cage at the same time, a hot little lurch, and you look down at your cake very fast."
    hide lto_katie
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Noted.\""
    lto_you "\"I was being polite.\""
    hide lto_katie
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Noted, I said.\""
    hide cg onlayer cgl
    hide lto_katie
    jump lto_car

label lto_ch5_after:
    hide cg onlayer cgl
    $ lto_body(5)
    $ lto.fit = "nude"
    $ vn_enter(bg="lto_livingroom", pc="flushed", pc_tag="lto_pc", cast=[("lto_katie", "squeal")], cg="lto_retire_pads")
    lto_katie "\"Assume the position!\""
    "{color=#f0b090}Back at the house Katie takes the stuffed bra off you, measures, and screams. A small real one comes out instead: a handful, real, yours. Your waist's done; your ass and thighs are still climbing.{/color}"
    lto_katie "\"Record this. Record it now, look. It's {i}real.{/i}\""
    hide lto_katie
    show lto_marissa tease at vn_cast_slot
    lto_marissa "\"Sunday brunch, starring our new favourite girl and her real, not-stuffed chest.\""
    hide lto_katie
    show lto_jo blunt at vn_cast_slot
    lto_jo "\"Bet you'll need a new bra by Tuesday if you keep it up.\""
    hide lto_jo
    show lto_katie squeal at vn_cast_slot
    lto_katie "\"Okay, I'm sorry, I have to. I {i}have{/i} to. Lie down. Lie {i}down{/i}, I want to see them move.\""
    lto_you "\"See them— Katie, they're very small, they're not going to— I mean— yes. Fine. If it's a measurement thing—\""
    show cg lto_katie_sofa onlayer cgl
    "It isn't a measurement thing. She puts you on your back on the sofa with your knees up and slides into you slowly, both hands on your chest, cupping, squeezing, thumbs on your nipples, shrieking every time they move, which is every time she does."
    lto_katie "\"They {i}jiggle{/i}! Marissa! They jiggle!\""
    lto_you "\"{i}Ahh{/i}— Katie— {i}don't{/i}— don't pinch— {i}hahh{/i}— oh, {i}do{/i}, do, sorry, do pinch— {i}ahh{/i}—\""
    "Your nipples turn out to be connected to something. You'd never known. Every squeeze goes straight down your spine to where Katie is, and you arch into her hands and make a sound like a kettle, and come, caged, with her thumbs on you and her face lit up like it's her birthday."
    lto_you "\"{i}AHH{/i}— oh— oh god, oh {i}god{/i}, Katie—!\"" with vnfx("flash", "shake")
    show screen lto_notes(5)
    "You tuck the soft small cock into Katie's panties without comment. You've stopped checking."
    hide screen lto_notes
    hide cg onlayer cgl
    jump lto_ch6

## ---- 6. Lights Out -----------------------------------------------------------------------------
label lto_ch6:
    $ lto.chapter = 6
    $ lto_body(6)
    $ lto.fit = "nude"
    $ vn_enter(bg="lto_livingroom", pc="greedy", pc_tag="lto_pc", cast=[], cg="lto_bottle")
    "Sunday night. Last game, spin the bottle, house rules. It stops being a game about four spins in."
    "{color=#f0b090}The biggest jump of the weekend: your chest fuller, still a handful; your ass and thighs at their peak. The cock still there, still caged, still small.{/color}"
    "You're on the rug before anyone else comes down, already undressed, sitting with your knees together and your hands folded and the bottle laid out in front of you. When the others come in, Jo stops dead in the doorway and says \"oh, mate\", with real tenderness."
    lto_you "\"I wasn't— I just thought I'd set up. Somebody has to set up. It's the last night.\""
    jump lto_finale
