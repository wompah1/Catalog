## secondvial's ten chapters. PAID BEFORE OPENING: ch 3-5 non-con, 6 the break, 7 alone, 8 the flip (the
## third vial, drunk gleeful), 8-10 consensual. Dawn shows what stayed.

## ---- 1. Last Coin --------------------------------------------------------------------------------
label svl_ch1:
    $ svl.chapter = 1
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_alley", pc="guarded", pc_tag="svl_pc", cast=[], cg="svl_two_coins")
    "Rain makes everything slow. Your boot soles are pudding-soft, the gutters seep up through the rents you never patched, and there's nothing in your stomach but three days of watered beer."
    "Two coins in your fist, both notched from the pawnshop's scales. In the bakeries, the cloth-halls, behind every bar in the city: women. By charter and by want. For a man with no papers there's the street, and not much after it."
    hide cg onlayer cgl
    $ vn_enter(bg="svl_hut", pc="guarded", pc_tag="svl_pc", cast=[("svl_alchemist", "hard")], cg="svl_hut_vial")
    "The alchemist's hut crouches between the fishmongers and a windowless hall: sour brine, chalk, old burnt hair. She doesn't stop wrapping bottles to look at you."
    svl_alch "\"You'll want a full change if you're taking women's work, and none of my business why. How many days?\""
    svl_you "\"One. Only one.\""
    "She holds up a vial that looks like nothing but water."
    svl_alch "\"The cheap. It'll do for a day. Listen now. One a day, never more. Done right, you go back by morning. Get clever, and it stops letting you go. Understood?\""
    svl_you "\"Yes.\""
    hide svl_alchemist
    $ vn_enter(bg="svl_alley", pc="guarded", pc_tag="svl_pc", cast=[], cg="svl_first_change")
    "Under a failed awning among broken barrels you pull the cork with your teeth. A ribbon of cool salt and a faint fizz, and then a stretch that starts in your scalp and pulls downward, like hands pressing you into a new posture."
    $ svl_body("n1")
    "{color=#e8a8c0}Your jaw narrows. Your waist draws in. Between your legs it goes velvet-quiet, folding away. Two soft swells under the flannel, hardly a handful. Your hair comes out ash pink, the cheap dose's one flourish. Plain. Flat. Narrow-hipped. Ordinary.{/color}"
    svl_you "\"—ah. Hello? Testing. Hello.\""
    "It'll pass. Half the kitchen girls sound the same."
    hide cg onlayer cgl
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="guarded", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_hired")
    "The Bellhouse has fresh rushes on the floor and rates in the window. The owner, Caddic, is a block of a man with mallet hands, one eye lost in the war and peppermint on his breath. He looks at you exactly as long as it takes to decide you won't steal."
    svl_caddic "\"Mugs first, then table twelve. Don't spill.\""
    "Nobody looks twice. A shapeless body doesn't draw smiles or slaps. You wipe, pour, carry, and survive."
    show cg svl_first_shift onlayer cgl
    "You learn the room by the second hour: which tables tip and which ones only grab, which barrels pour foam and which pour true, that the hearth corner wants its stew hot and its ale cold and its girl gone again quickly."
    "Mira, passing with six tankards, looks you up and down once, the way you'd look at a bucket somebody's left in a doorway, and steps round you."
    hide cg onlayer cgl
    hide svl_caddic
    show screen svl_purse(1)
    "At last bell you pick a missed penny off the floor and hold it like a charm."
    hide screen svl_purse
    $ svl_body("0")
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_cart", pc="guarded", pc_tag="svl_pc", cast=[], cg="svl_cart_dawn")
    "Dawn finds you under an empty grain cart, a man again, every last bit of it going back the way it came: the hips, the chest, the pink fading out of your hair like dye in the rain."
    "You lie there and count the coins by feel. Enough for a vial. Enough for bread. Not both. You buy the vial."
    call vn_night(7)
    jump svl_ch2

## ---- 2. The Floor --------------------------------------------------------------------------------
label svl_ch2:
    $ svl.chapter = 2
    $ vn_clock.day += 20
    $ svl_body("n1")
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="guarded", pc_tag="svl_pc", cast=[("svl_mira", "wry")], cg="svl_mira_sabine")
    "Three weeks on the floor. You're good at it: plates that don't wobble, a till counted twice and never short. Caddic's nod at the end of the first week was as close to a blessing as anyone gets here."
    "Mira works the room with temper and red hair and hips like a river bend, and clears twice your tips in half the time. Sabine slides under men's arms to pour and whispers something that makes them pay without knowing why."
    "You're neither. You're the plain one."
    svl_mira "\"You. Plain one. You're on twelve and fourteen tonight, and if you spill on fourteen again I'll drown you in it.\""
    svl_you "\"I didn't spill on fourteen. Fourteen spilled on me.\""
    "Mira looks at you, surprised, and for a second something like a smile goes across her face, and then she remembers who she's talking to and takes her tankards away."
    hide svl_mira
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"She likes you. That's what that was.\""
    svl_you "\"That was liking?\""
    hide svl_mira
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"For Mira.\""
    hide svl_mira
    $ vn_enter(bg="svl_floor", pc="flushed", pc_tag="svl_pc", cast=[("svl_brusk", "leer")], cg="svl_brusk_hand")
    "Brusk, from the hearth table: two coppers for stew, broken molars, always the same. He pulls you in by the wrist, and his hand goes down the front of your bodice and comes up with nothing."
    svl_brusk "\"Not a tit to her name! Who put the washboard out to work?\""
    "The table roars."
    menu:
        "Brusk's hand, and the laughter."
        "Take the copper and say nothing":
            $ svl.brusk = "silent"
            "You wait like a piece of furniture until he lets go, and take the copper he pushes between your fingers."
        "Tell him where to put it":
            $ svl.brusk = "snap"
            svl_you "\"Keep your hands on your stew, Brusk.\""
            "It gets a bigger laugh than his did. Caddic's eye finds you from behind the bar and stays there. No copper tonight."
    hide cg onlayer cgl
    hide svl_brusk
    $ vn_enter(bg="svl_yard", pc="guarded", pc_tag="svl_pc", cast=[("svl_sabine", "sly")], cg="svl_yard_supper")
    "After the shift Mira and Sabine share dried fruit and gossip in the yard. They don't ask you to sit."
    menu:
        "The after-hours supper."
        "Ask if you can sit":
            $ svl.supper = "asked"
            svl_you "\"Mind if I...?\""
            svl_sabine "\"Find some courage first, mouse. Then a sandwich.\""
            "It isn't cruel. It isn't a yes."
        "Count your coins alone":
            $ svl.supper = "alone"
            "You fold napkins at the far end of the yard and tell yourself you have an old father to get home to."
    hide svl_sabine
    show screen svl_purse(2)
    "Never enough for the rent."
    hide screen svl_purse
    call vn_night(7)
    jump svl_ch3

## ---- 3. Caught -----------------------------------------------------------------------------------
label svl_ch3:
    $ svl.chapter = 3
    $ vn_clock.day += 6
    $ svl_body("d1")
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_cellar", pc="flushed", pc_tag="svl_pc", cast=[], cg="svl_mid_reversal")
    "The hour before opening, the cellar thick with dust and spilled ale. You've let the vial run too long, and the reversal is late."
    "{color=#e8a8c0}It stalls halfway: shoulders too broad for the blouse, hips caught mid-width, the chest neither flat nor anything else, your hair shrinking toward the root in fits.{/color}"
    "Steps above. Not hurried. The bolt on the hatch slides back."
    hide cg onlayer cgl
    $ vn_enter(bg="svl_cellar", pc="flushed", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_caught")
    svl_caddic "\"Well then. Don't move.\""
    "He comes down, takes your chin in his thick fingers and turns your half-made face to the lantern, the way he'd check a cask for a split."
    svl_caddic "\"That's not standard Guild magic, is it. Neither one thing nor the other.\""
    "He lets go, takes a battered box down from the top shelf and sets out two vials stoppered with old wax. Then he says it, once, flat as a line in a ledger:"
    svl_caddic "\"No papers. Two a day, mine, drunk here. Tips held in trust. Paid before opening.\""
    "He doesn't raise his voice. He doesn't explain what happens otherwise. He doesn't need to, and he never says it again."
    svl_you "\"The alchemist said never two. Never. I can't—\""
    svl_caddic "\"Drink.\""
    jump svl_first_payment

label svl_ch3_after:
    hide cg onlayer cgl
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="dazed", pc_tag="svl_pc", cast=[], cg="svl_apron_high")
    "The skirt won't close over the new hips, so you tie the apron high. Upstairs the laughter and the glasses are waiting, and you walk into the lamplight shaking, with the first payment still in you."
    "Nobody notices anything except that the plain one's walking funny. Brusk asks if you've had a fall. You say yes. You say it in a voice that's gone half an octave somewhere, and he looks at you a beat too long."
    "At last bell Caddic opens the ledger on the bar, and writes it in, in front of you, in his square careful hand. Then he closes it and puts it under the bar and wipes the counter round it."
    call vn_night(7)
    jump svl_ch4

## ---- 4. The Second Vial --------------------------------------------------------------------------
label svl_ch4:
    $ svl.chapter = 4
    $ svl_body("0")
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_cellar", pc="guarded", pc_tag="svl_pc", cast=[("svl_caddic", "pleased")], cg="svl_two_crate")
    "The next evening, before opening, the cellar again. You came down a man, the morning's reversal finished for once. Two vials on the crate."
    svl_caddic "\"Both. Clothes off. I want to see it work properly this time.\""
    svl_you "\"You saw it this morning. You don't need to—\""
    svl_caddic "\"Both.\""
    jump svl_display

label svl_ch4_after:
    hide cg onlayer cgl
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="flushed", pc_tag="svl_pc", cast=[("svl_mira", "wry")], cg="svl_floor_eyes")
    "Upstairs the room doesn't recognise you, and then it does."
    svl_man "\"Wren? That you? What've you been eating?\""
    "Hands at your waist, your flanks, the new roundness of your ass. Every touch goes straight to the throb between your legs, and you bite your tongue on every gasp. The tips double. The bowl overflows. It all goes in Caddic's ledger."
    svl_mira "\"Careful, new girl. They smell blood. Tonight was easy. Wait till they want to keep you.\""
    "You carry a tray of six through the hearth corner and the tray comes back with nine coins on it and a note with a room number. Somebody pinches your new ass so hard you spill, and the table cheers the spill."
    "Brusk catches your wrist again, at the end, the same as always. His hand goes down the front of the bodice the same as always. It comes up full."
    hide svl_mira
    show svl_brusk leer at vn_cast_slot
    svl_brusk "\"...Well. Well, well. Who's been eating their crusts.\""
    "He doesn't laugh this time. Nobody at the table laughs. They all just look, and you take the copper he pushes between your fingers, and walk away with your face burning and every one of them watching you go."
    hide cg onlayer cgl
    hide svl_mira
    show screen svl_purse(4)
    "Two coppers in your purse."
    hide screen svl_purse
    $ vn_until(7)
    $ svl_body("d1")
    $ svl.fit = "nude"
    $ vn_enter(bg="svl_room", pc="flushed", pc_tag="svl_pc", cast=[], cg="svl_dawn_soft")
    "{color=#e8a8c0}Dawn takes you back, and it doesn't finish. A man in the cracked mirror, but soft at the hips, the chest puffy, the skin too smooth. It used to all go back. Now some of it stays.{/color}"
    "You stand there in the grey light pressing at your chest with both hands, as if you could push it back where it came from. It pushes back. It's soft and warm and yours and it doesn't go anywhere."
    "Never two, she said. You say it out loud to the mirror, in a voice that's almost your own. Never two."
    hide cg onlayer cgl
    call vn_night(7)
    jump svl_ch5

## ---- 5. The Routine ------------------------------------------------------------------------------
label svl_ch5:
    $ svl.chapter = 5
    $ vn_clock.day += 50
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_cellar", pc="guarded", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_routine")
    "Two months. The descent is choreography now: left foot behind the chipped barrel, right hand on the worn stair-post, the two vials lined up on the shelf."
    $ svl_body("n3")
    $ svl.fit = "nude"
    "{color=#e8a8c0}The change rolls through you without surprise any more: hips softer and wider, the breasts heavier every week, the uniforms piling up behind your door as you outgrow them.{/color}"
    show cg svl_uniforms onlayer cgl
    "Behind the door of your rented room there are four of them on the hook now, one over the other: the first, which hangs off you like a sack; the second, let out at the hips; the third, with a seamstress's gusset in the bodice; the fourth, which Caddic had made, which fits, for now."
    "You stand in front of them some mornings in your dawn shape, half a man in a borrowed shirt, and look at the four of them like a ladder you've been climbing in your sleep."
    "And on busy nights Caddic circles the bar offering \"first pick\", and certain customers are led down the cellar steps for a private tasting."
    jump svl_tastings

label svl_ch5_after:
    hide cg onlayer cgl
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="dazed", pc_tag="svl_pc", cast=[("svl_sabine", "sly")], cg="svl_freeze_out")
    "Mira and Sabine stop talking when you come up the stairs. Your body pulls the custom now, and the custom is theirs no longer."
    if svl.supper == "asked":
        svl_sabine "\"Found your courage, mouse? Looks like you found a lot more than that.\""
    else:
        svl_sabine "\"Still eating alone in the yard? You could buy the whole yard by now. If he paid you.\""
    "Mira doesn't say anything. She watches the hearth table watch you, and her mouth goes thin, and she takes her tankards the long way round."
    show cg svl_mira_sharp onlayer cgl
    "At last bell she catches you on the cellar stairs with a hand flat on the wall, blocking the way down."
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"How many tonight?\""
    svl_you "\"I don't— I didn't count—\""
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"He did. He always counts. Ask him to see the ledger some time. Ask him what your column says.\""
    svl_you "\"It says held in trust.\""
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"Mm. Ask him whose trust.\""
    "She takes her hand off the wall and goes up, and doesn't look back."
    hide cg onlayer cgl
    hide svl_sabine
    show screen svl_purse(5)
    "Two coppers in the purse. A column of silver in the ledger, \"held in trust\"."
    hide screen svl_purse
    call vn_night(7)
    jump svl_ch6

## ---- 6. The Alchemist ----------------------------------------------------------------------------
label svl_ch6:
    $ svl.chapter = 6
    $ vn_clock.day += 30
    $ vn_until(11)
    $ svl_body("d2")
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_room", pc="dazed", pc_tag="svl_pc", cast=[], cg="svl_dawn_breasts")
    "You wake late, stuck to the cot. The window full of indifferent light."
    "{color=#e8a8c0}Dawn has taken you back to a man again, nearly. The breasts didn't go. They lie heavy against your arm when you roll over, with your own straw-blonde hair across them.{/color}"
    hide cg onlayer cgl
    $ vn_enter(bg="svl_hut", pc="guarded", pc_tag="svl_pc", cast=[("svl_alchemist", "hard")], cg="svl_measured")
    "The alchemist's hut. She doesn't say I told you so. She measures you: calipers round the bust, the hips, shoulder to nipple to navel. She writes down every number and frowns at each one."
    svl_alch "\"That's the residue. One a day holds a pattern and lets you go. Two a day lays it down faster than you clear it. Keep on and you reach saturation, and then there's nowhere left to shift but forward.\""
    svl_you "\"Forward to what?\""
    "She puts the calipers down and looks at you over them, a long look, the first time she's ever looked at you as if you were anything but a customer."
    svl_alch "\"To whatever the second vial was made for. I didn't make his. I make the cheap. His come from somewhere else, and I'd guess they were made for exactly one thing, and it's not pulling pints.\""
    svl_you "\"He supplies them. Every night. He says it's the terms.\""
    svl_alch "\"Then they're his terms. Not the glass's.\""
    menu:
        "What you ask her for."
        "A reversal":
            $ svl.ask = "reversal"
            svl_you "\"Then sell me something that goes back. Anything. I'll find the coin.\""
            svl_alch "\"There's nothing in glass that unlays a residue. I'd be selling you water.\""
        "A cheaper dose, one a day again":
            $ svl.ask = "cheaper"
            svl_you "\"One a day, then. The cheap. I'll go back to one.\""
            svl_alch "\"And stand on the floor half a man by midnight? He'd have you on three by the week's end.\""
    "She won't sell you anything. Outside, every window you pass is someone else's ordinary evening."
    hide cg onlayer cgl
    hide svl_alchemist
    jump svl_break

label svl_ch6_after:
    hide cg onlayer cgl
    $ svl.fit = "barmaid"
    $ vn_enter(bg="svl_floor", pc="dazed", pc_tag="svl_pc", cast=[], cg="svl_mirror_more")
    "The uniform cut for you last week won't button across the chest. In the cellar's warped mirror: not a man, not quite a woman, not one of the girls upstairs either. Wider. Lusher. More."
    "That night you take a tray up and three tables stand when you come up the stairs. Not for you. For your body. You know the difference, and you can't decide which of you they're standing for, and the tips are the biggest the Bellhouse has ever had."
    "Caddic writes them in the ledger. Held in trust."
    call vn_night(7)
    jump svl_ch7

## ---- 7. Drift ------------------------------------------------------------------------------------
label svl_ch7:
    $ svl.chapter = 7
    $ vn_clock.day += 30
    $ svl_body("d3")
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_room", pc="dazed", pc_tag="svl_pc", cast=[], cg="svl_binding")
    "A day off. Caddic has kept to the calendar for once. No vials until tomorrow."
    "{color=#e8a8c0}You wind the old cloth round your chest anyway. It won't go flat; it only compresses, presses back, and leaks a little when it's squeezed. The shirt pinches. The trousers don't sit right on the hips. It's neither shape.{/color}"
    hide cg onlayer cgl
    menu:
        "The day off."
        "Try the street":
            $ svl.dayoff = "street"
            "You get as far as the threshold. The bakery girls, the mothers arguing about prices. You imagine them looking at this body, and you go back inside."
        "Watch from the window":
            $ svl.dayoff = "window"
            "Half an hour at the window, just out of sight. Ordinary people going to ordinary gates."
    $ vn_enter(bg="svl_room", pc="flushed", pc_tag="svl_pc", cast=[], cg="svl_drift")
    if svl.dayoff == "street":
        "You stand inside the door for a long time with your back against it and your arms crossed over the cloth, and your heart going, as if you'd run from something. You hadn't. You'd stood on a step."
    else:
        "A woman across the street shakes a rug out of a window and catches you watching and waves, the way you'd wave at a neighbour, and you step back from the glass so fast you knock the jug off the sill."
    show cg svl_dayoff_bed onlayer cgl
    "You lie on the cot and try to remember what you did with days, before. Before the vials, before the rain, before the city. You can't. You remember a dock, and a ship that left without you, and that's all."
    "By afternoon you're thinking about the other body. The night one. The one that brings the coins tumbling and makes Mira scowl and makes you come so hard you can't hear the room."
    "This one, the one in the shirt, feels like the costume now."
    "Your hand goes down. It isn't enough. It isn't anything like enough."
    hide cg onlayer cgl
    "At dusk you put the cloth back on, and walk to the Bellhouse a day early."
    call vn_night(7)
    jump svl_ch8

## ---- 8. The Third Vial ---------------------------------------------------------------------------
label svl_ch8:
    $ svl.chapter = 8
    $ svl.fit = "rags"
    $ vn_enter(bg="svl_cellar", pc="guarded", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_three_crate")
    "Rain churns the gutters. You're in the cellar an hour before he is."
    "Caddic comes down grey from a sleepless night with a fistful of figures."
    svl_caddic "\"We're taking a loss. The Gilded Tun's pulled the whole south end.\" Three vials on the crate. \"Three tonight. No more reversals. It sticks till we turn the crowd or close.\""
    if svl.ask == "reversal":
        "You think of the alchemist, and the reversal she wouldn't sell you because there's nothing in glass that unlays a residue. You think of the shirt that fits like a costume."
    else:
        "You think of the alchemist, and the cheap single dose you asked her for, and the half a man you'd have been on the floor by midnight. You think of the shirt that fits like a costume."
    "He reaches for the first cork. You've already got the third one open."
    jump svl_third

label svl_ch8_after:
    hide cg onlayer cgl
    $ svl.fit = "apron"
    $ vn_enter(bg="svl_floor", pc="gleeful", pc_tag="svl_pc", cast=[], cg="svl_mainstage_poster")
    "By the week's end no uniform in the city fits, so it's the apron and nothing else. Caddic's posters go up: MAINSTAGE FOR A NIGHT, NEXT DOOR'S GOT NOTHING."
    "The crowd comes thick and early. You pour, you serve, you spread for them in the new alcoves, and you {i}grin{/i} the whole time."
    show screen svl_purse(8)
    "Milk pools between the floorboards. Men take tankards of it home as trophies."
    show cg svl_south_end onlayer cgl
    "By the second week the south end's back. By the third the Gilded Tun's girls are in the Bellhouse on their nights off, at the bar, watching, and one of them asks you where you got your vials, and you laugh so hard you have to sit on the bar."
    svl_you "\"Ask Caddic. Ask him what's in the box on the top shelf. Ask him what he pays for them.\""
    "She does ask him. He doesn't answer. You watch him not answer, from the bar, with your breasts on the counter and your chin on your hands, and you learn something about Caddic that you file away for later."
    hide screen svl_purse
    hide cg onlayer cgl
    call vn_night(7)
    jump svl_ch9

## ---- 9. The Conversion ---------------------------------------------------------------------------
label svl_ch9:
    $ svl.chapter = 9
    $ vn_clock.day += 5
    $ svl.fit = "apron"
    $ vn_enter(bg="svl_house", pc="gleeful", pc_tag="svl_pc", cast=[("svl_caddic", "pleased")], cg="svl_gutted")
    "Caddic guts the taproom himself, mallet in hand. The benches go out to the yard in a heap. Velvet goes up, and mirrors, and a low dais in the alcove with a double mattress on it."
    svl_caddic "\"From this week the house sells its own produce. Every hour, every way. You're the centre of it.\""
    "A bill goes out across Spindlemarket: THE UNIQUE GIRL. NO IMITATION, NO REST, NO FINISH."
    svl_you "\"{i}Finally.{/i}\""
    show cg svl_velvet_fit onlayer cgl
    "Sabine fits you for the house's velvet in the gutted taproom with pins in her mouth: a gown that isn't a gown, that opens at the front and the sides and the back on gold ties, that you can be out of in one pull."
    hide svl_caddic
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"Arms up. He wanted it in red. I told him pink, to match the hair. Pink sells.\""
    svl_you "\"Does he know you told him?\""
    hide svl_caddic
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"He knows what sells. He's never once known why.\""
    hide cg onlayer cgl
    hide svl_caddic
    jump svl_stage

label svl_ch9_after:
    hide cg onlayer cgl
    jump svl_bath

label svl_ch9_end:
    hide cg onlayer cgl
    call vn_night(7)
    jump svl_ch10

## ---- 10. The House -------------------------------------------------------------------------------
label svl_ch10:
    $ svl.chapter = 10
    $ vn_clock.day += 120
    $ svl.fit = "velvet"
    $ vn_enter(bg="svl_office", pc="gleeful", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_ledger")
    "Eight months since the first overdose. You've stopped counting doses. Nobody asks you to drink the vials any more; they gather dust on the shelf, inert and irrelevant."
    "Caddic has shrunk as the house has grown: sallow, pinched, thinner every month. In the office that used to be a pantry he counts the stacks and tries the old line."
    svl_caddic "\"You'd be nothing without the vials. Without the house. Without me.\""
    "You sit down across the desk from him, on the edge of it, in the velvet, with your breasts resting on the ledger he's trying to read."
    svl_you "\"Eight months, Caddic. Tips held in trust. Visitors' fees. Every vial docked from wages I never saw. Shall we read my column out loud? Mira said to ask you whose trust.\""
    "He puts his hand on the ledger. You put yours on top of it. Yours is softer and smaller and doesn't move."
    if svl.shout4 == "tell":
        svl_you "\"I called you a peppermint-stinking pig once, on my knees. I said I hoped your cellar flooded.\""
        svl_caddic "\"I remember.\""
        svl_you "\"It's my cellar now. I'll flood it if I like.\""
    else:
        svl_you "\"I said no to you once, on my knees. I said I drank them, and that was all you'd said.\""
        svl_caddic "\"I remember.\""
        svl_you "\"Good. Remember it on your way out.\""
    svl_you "\"I am the contract, Caddic. The whole business is one girl, and she's standing in front of you.\""
    "He flinches, once. You slide the ledger shut, lock it, and tuck the iron key between your breasts."
    $ svl.ending = "house"
    hide cg onlayer cgl
    hide svl_caddic
    $ vn_enter(bg="svl_house", pc="gleeful", pc_tag="svl_pc", cast=[("svl_mira", "wry")], cg="svl_charter")
    "By the next week Caddic is gone from the city, and nobody goes looking. Mira takes the upstairs rooms; Sabine runs the baths and the kitchen. Wages get paid at the end of every shift, after you've checked the tally."
    "On the house's charter you write a name in a big looping hand. Not Wren."
    $ svl_pc_name = "Serah"
    svl_mira "\"Serah. Suits you. Sounds like money.\""
    hide cg onlayer cgl
    hide svl_mira
    jump svl_table
