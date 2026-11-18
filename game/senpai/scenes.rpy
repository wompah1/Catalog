## THE STORY: chapters 3-5, Wednesday to Friday (PLAN.md). Wednesday is the love hotel, Thursday the clubroom (the low point),
## Friday the bikini at his flat, where she starts meaning the yeses. Non-con by the curse until Friday; loud throughout.

## ---- 3. Wednesday -----------------------------------------------------------------------------------------

label snp_wednesday:
    $ snp.fit = "nude"
    $ snp_grow(3)
    $ vn_enter(bg="snp_shun_room", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_mirror_wednesday")
    "{color=#ff5fb8}The bra from yesterday won't close.{/color}"
    "{color=#ff5fb8}Your breasts have filled out overnight, D cups now, full and round and heavy, and below your waist your hips have spread wide and soft, so the old boxers you slept in are cutting into new flesh.{/color}"
    "{color=#ff5fb8}Your hair brushes your shoulders, and the ash-pink has climbed halfway up from the ends.{/color}"
    "Your phone buzzes on the tatami. Six-oh-two in the morning."
    "{i}Daigo: love hotel. Dogenzaka. 10am. wear something short. no bra{/i}"
    "Not {i}good morning{/i}. Not {i}last night was nice{/i}. You read it four times."
    "Then your hand's between your legs, because of the {i}no bra{/i}, because of the way he'd said {i}greedy{/i}, and you hate that it's your hand."
    show cg snp_futon_wednesday onlayer cgl
    vn_sfx "Shlk. Shlk."
    snp_you "\"Senpai— no— I don't— ahh♡— I {i}do{/i}— ahh♡—\"" with vnfx("flash")
    $ vn_set_time(10, 0)
    $ snp.fit = "date"
    $ vn_enter(bg="snp_love_hotel", pc="nervous", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_hotel_arrive")
    "A love hotel on Dogenzaka, the Hotel Venus Bay, a room with a round bed and a mirrored wall and a jacuzzi bath in a glass box."
    "You came in a short pleated skirt and a tight pink top with nothing under it, as told. Your nipples show through. He notices before the door's shut."
    snp_daigo "\"Look at you. They've got {i}bigger{/i}. Did they get bigger?\""
    snp_you "\"Yes.\""
    snp_daigo "\"How?\""
    snp_you "\"...Growth spurt.\""
    "He laughs like it's the best joke he's heard all year, and peels the top up over your head, and stands back to look."
    snp_daigo "\"Fuck me. You're turning into her. You know that? Every time I see you you're more like her.\""
    show cg snp_hotel_suck onlayer cgl
    "He sits on the edge of the round bed and pushes you to your knees by the shoulder. You know what he wants."
    "You've never done it, and you try to say {i}I don't know how{/i}, and it comes out {i}teach me{/i}."
    $ snp.yes += 1
    snp_daigo "\"Happily. Open.\""
    "He fists your hair, the pink-tipped ends wrapped round his knuckles, and feeds you his cock."
    "It's thick and it stretches your lips and it tastes of salt and soap, and he pushes until you gag, and holds you there, and then lets you breathe."
    vn_sfx "Glk. Glk. Glk."
    snp_you "\"Mmhh— mmhh— {i}hah{/i}— senpai— mmhh♡—\""
    snp_daigo "\"Good. Tongue. Use your tongue, yeah. Fuck, you learn fast.\""
    "You do learn fast. You find you know what you'd want, because you used to have one."
    "You lick the ridge under the head and he grunts and his thighs go hard under your hands, and something hot and proud flickers in your chest. {i}I did that.{/i}"
    show cg snp_hotel_bed onlayer cgl
    "Then you're on your back on the round bed with your skirt still on and your knees up by your new breasts, and he's in you in one long shove."
    vn_sfx "Zubuuu."
    snp_you "\"{i}HAAH♡—!{/i} Senpai— so deep— it's so {i}deep{/i}—\"" with vnfx("shake")
    snp_daigo "\"Watch in the mirror. Watch yourself take it.\""
    "In the mirrored wall, a woman with pink-tipped hair on a round bed, folded in half, D-cup breasts swinging with every stroke, mouth open, a big tanned man pounding into her."
    "You don't recognise her at all. You can't look away."
    vn_sfx "Pan. Pan. Pan. Pan."
    snp_you "\"Ahh♡— ahh♡— look at me— is that me— {i}ahh♡{/i}— senpai— harder— {i}harder{/i}—\""
    snp_daigo "\"Yeah? Harder?\""
    snp_you "\"Yes— yes— AHH♡— I'm cumming— I'm cumming on senpai's cock—!\"" with vnfx("flash", "shake")
    "He keeps going straight through it, and you come again almost at once, a second smaller wave, and he pulls out and comes across your belly and your breasts, hot ropes of it, grinning at the mirror."
    $ vn_set_time(12, 30)
    $ vn_enter(bg="snp_love_hotel", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_hotel_talk")
    "After. He's lying back with a canned coffee from the room fridge, scrolling his phone. You lie beside him with your head near his shoulder, not quite touching."
    "This is the bit, you think. This is where you win him."
    menu:
        "He hasn't looked up from his phone in five minutes."
        "Ask what he thinks of Shun":
            snp_you "\"Senpai. Do you— there's a guy on your team. Nagai? My cousin knows him. What's he like?\""
            snp_daigo "\"Nagai? The skinny full-back?\""
            "He doesn't look up."
            snp_daigo "\"Useful. Does my boots. Carries my stuff. Like a puppy, honestly. I keep Ryota off him because if Ryota breaks him, who's going to do my boots?\""
            "He laughs. You laugh too, because you can't say {i}don't laugh at that{/i}, because it would come out {i}do{/i}."
            snp_daigo "\"Why, he fancy you or something? Tell him to get in line.\""
            "Something in your chest goes quiet and cold. {i}Like a puppy.{/i}"
        "Ask what he likes about you":
            snp_you "\"Senpai. What do you like about me?\""
            "He finally looks up. He looks at your breasts."
            snp_daigo "\"Honestly? These. And your arse. And that you don't say no to anything. Do you know how rare that is?\""
            snp_you "\"Anything else?\""
            snp_daigo "\"You're getting more like Mitsuki every day. That's a pretty big thing, Mitsuki-chan.\""
            "He puts the phone down and pinches your nipple, hard, and that's the end of the conversation."
    show cg snp_hotel_bath onlayer cgl
    "Round two is in the jacuzzi."
    "He sits back against the glass and you ride him in the bubbling water with your new breasts slapping the surface, his hands on your hips pulling you down harder every time you slow."
    vn_sfx "Bshh. Pan. Bshh. Pan."
    snp_you "\"Ahh♡— the water— it's going in— {i}ahh♡{/i}— senpai— your cock's so hard— so {i}hard♡{/i}—\""
    snp_daigo "\"Say you love my cock.\""
    "{i}No.{/i}"
    snp_you "\"I love your cock— I love it— AHH♡—!\"" with vnfx("flash", "shake")
    $ snp.yes += 1
    "He comes inside you this time, deep, with a grunt, and you lie against his chest in the warm water afterwards with his cum leaking out of you into the bubbles, and he's already reaching for his phone on the side of the bath."
    snp_daigo "\"Tomorrow, after practice. Come to the clubroom. I want to show you off.\""
    snp_you "\"Yes.\""
    $ vn_set_time(22, 30)
    $ snp.fit = "nude"
    $ vn_enter(bg="snp_shun_room", pc="dazed", pc_tag="snp_pc", cast=[], cg="snp_room_wednesday")
    "That night you lie awake and think about the word {i}heart{/i}. The witch said {i}love you, not want{/i}. You're not sure, any more, that he's got the first one."
    "You fall asleep with two fingers inside you anyway, and his name in your mouth."
    call snp_cut(6, 1, "Thursday.")
    jump snp_thursday

## ---- 4. Thursday ------------------------------------------------------------------------------------------

label snp_thursday:
    $ snp.fit = "nude"
    $ snp_grow(4)
    $ vn_enter(bg="snp_shun_room", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_mirror_thursday")
    "{color=#ff5fb8}You roll over and your breasts roll with you, a long heavy sway.{/color}"
    "{color=#ff5fb8}They're large now, big soft globes that spill out of your hands, and your waist has pinched in tight and narrow beneath them, so the curve from ribs to hip is the curve on the poster.{/color}"
    "{color=#ff5fb8}The ash-pink has reached the roots. There's no black left anywhere.{/color}"
    show cg snp_mirror_large onlayer cgl
    "You hold them up to the mirror and let them drop, and watch them bounce, and touch yourself with both hands on your nipples and your thighs squeezed together, rocking, until you come just from that."
    vn_sfx "Squsshh. Squsshh."
    snp_you "\"So big— they're so {i}big♡{/i}— ahh♡— just my nipples— just— AHH♡—!\"" with vnfx("flash")
    "Shun Nagai's phone has fourteen messages from Ryota. {i}where are you faker{/i}. {i}boots{/i}. {i}u dead{/i}. You put it face down."
    $ vn_set_time(18, 30)
    $ snp.fit = "date"
    $ vn_enter(bg="snp_clubroom", pc="nervous", pc_tag="snp_pc", cast=[("snp_daigo", "ace"), ("snp_ryota", "bully"), ("snp_oshiro", "bully")], cg="snp_clubroom_showoff")
    "The clubroom after practice, the poster on the wall, the sofa, the smell of liniment and boots. Your boots, the ones you've washed a thousand times, lined up by the door."
    "Half the team's gone home. Ryota and Oshiro are still here, playing cards on an upturned crate."
    "Daigo walks you in with his hand on your arse."
    snp_daigo "\"Lads. Meet Mitsuki-chan.\""
    snp_ryota "\"...No way.\""
    snp_oshiro "\"That's— that's {i}her{/i}. That's literally her.\""
    "They look from you to the poster and back. Your hair is the poster's hair now. Your breasts are almost the poster's breasts."
    "They look at you like you're the poster come down off the wall."
    snp_daigo "\"Not her. Better. She doesn't say no.\""
    snp_ryota "\"Bollocks.\""
    snp_daigo "\"Watch. Mitsuki-chan, take your top off.\""
    "{i}No. No. Senpai, please, not in front of them, not in front of {b}Ryota{/b}—{/i}"
    snp_you "\"Yes, senpai.\""
    $ snp.yes += 1
    "Your hands do it. Up and over your head. Your large bare breasts bounce free in the clubroom light, and Oshiro drops his cards."
    snp_daigo "\"See? Anything. Go on. Ask her.\""
    snp_ryota "\"Can I touch them?\""
    menu:
        "Ryota's already standing. The clubroom door's shut."
        "Say no to Ryota":
            "This one. Of everyone, him. Ryota who threw your kit in the shower. Ryota who made you do the nets. You turn and look him full in the face and say it with everything you have."
            snp_you "\"Yes. Please. Touch them.\""
            "His face lights up like Christmas."
            snp_ryota "\"Fuck me, Kuroiwa-san. Where'd you {i}find{/i} her?\""
            $ snp.yes += 1
        "Look at Daigo":
            "You look past Ryota, at Daigo. {i}Senpai. Stop this. Step between us like you used to.{/i}"
            "Daigo grins at you, and nods at Ryota."
            snp_daigo "\"Go on, babe. Tell him.\""
            snp_you "\"...Yes. You can touch them.\""
            $ snp.yes += 1
    $ snp.fit = "nude"
    show cg snp_clubroom_grope onlayer cgl
    "Ryota's hands."
    "Ryota's hands on you, rough and greedy, squeezing, and Oshiro's behind you, and you're trapped between two men who flushed your phone down a shower drain on Sunday and called you {i}Nagai the doormat{/i}, and they're touching you like you're precious."
    snp_oshiro "\"Christ, they're real.\""
    vn_sfx "Squsshh. Squsshh."
    snp_you "\"Ahh— not there— there— {i}ahh♡{/i}— don't— do— do it more—\""
    "{i}I said DON'T. I said it. It just came out wrong.{/i}"
    show cg snp_clubroom_spitroast onlayer cgl
    "Then you're on the old sofa under the poster, on your hands and knees, and Daigo's in front of you with his cock in your mouth, and Ryota's behind you, pushing in, and Oshiro's waiting his turn with his shorts round his ankles."
    vn_sfx "Pan. Pan. Glk. Glk."
    snp_ryota "\"She's {i}soaked{/i}. Nagai'd die if he saw this. He fancies her, you know, Kuroiwa said.\""
    snp_you "\"Mmhh♡— mmhh♡— hah— {i}hah♡{/i}— mmhh♡—\""
    snp_ryota "\"Squeaks like him too. Bet you anything. Same little squeak.\""
    "You come. That's the worst of it."
    "Pinned between them, Ryota's cock pumping into you from behind and Daigo's in your throat, your bully's hands on your hips, the poster smiling down from the wall, and you come so hard you nearly bite down, a long muffled wail round Daigo's cock."
    snp_you "\"{i}MMMHH♡—!{/i}\"" with vnfx("flash", "shake")
    snp_daigo "\"There she goes. Told you. Anything.\""
    show cg snp_clubroom_oshiro onlayer cgl
    "Oshiro's turn."
    "He lies on the sofa and pulls you on top, and you ride your second bully under your own team poster while Ryota and Daigo watch with cans in their hands and give you marks out of ten."
    vn_sfx "Pan. Pan. Pan."
    snp_you "\"Ahh♡— ahh♡— stop— {i}don't stop{/i}— ahh♡— nobody stop—\""
    snp_oshiro "\"She said don't stop, lads, you heard her.\""
    snp_you "\"AHH♡— again— I'm— AHH♡—!\"" with vnfx("flash", "shake")
    "Daigo takes you last, standing, bent over the card crate, cards everywhere, and when he comes he does it on your back and wipes himself on your skirt."
    snp_daigo "\"Good girl. You were brilliant. Same time Saturday, after the Tamagawa game. Whole team's coming to the izakaya.\""
    $ vn_set_time(22, 0)
    $ snp.fit = "date"
    $ vn_enter(bg="snp_street_night", pc="dazed", pc_tag="snp_pc", cast=[], cg="snp_walk_home_thursday")
    "You walk home in a top that's on inside out, sticky down your thighs, under the Odakyu line. The alley between the ramen place and the tatami-maker isn't there tonight."
    "Just a wall."
    "You stand in front of the wall and try to shout at it. You open your mouth for {i}No, take it back, I don't want this, I don't want this any more{/i}."
    snp_you "\"...Yes. More. Please.\""
    "The wall doesn't answer."
    call snp_cut(7, 1, "Friday.")
    jump snp_friday

## ---- 5. Friday --------------------------------------------------------------------------------------------

label snp_friday:
    $ snp.fit = "nude"
    $ snp_grow(5)
    $ vn_enter(bg="snp_shun_room", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_mirror_friday")
    "{color=#ff5fb8}You can't see your feet.{/color}"
    "{color=#ff5fb8}Your breasts have swollen in the night to huge, enormous soft weights that sit high and proud and press together when you breathe, the poster's breasts exactly, heavy enough that you have to hold them to sit up.{/color}"
    "{color=#ff5fb8}Your ash-pink hair runs down your back to the middle of it.{/color}"
    "You sit up holding them, and the weight of them in your palms, and you don't think {i}no{/i} this time. You don't even try to."
    show cg snp_mirror_huge onlayer cgl
    "You think: {i}he'll love these.{/i} And your hands start moving on their own, kneading, lifting, and you're wet before you've decided anything."
    vn_sfx "Squsshh. Shlk."
    snp_you "\"Senpai'll— he'll love them— ahh♡— he'll {i}love{/i} them♡— AHH♡—!\"" with vnfx("flash")
    $ vn_set_time(19, 0)
    $ snp.fit = "date"
    $ vn_enter(bg="snp_daigo_flat", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_flat_arrive")
    "His flat in Chitose-Karasuyama. You've been here before as Shun, to drop off kit; you never got past the door."
    "Now he lets you in and there's a cardboard box on the bed with a ribbon round it."
    snp_daigo "\"Present. Open it.\""
    "Inside: a white string bikini. {i}The{/i} white string bikini. Page thirty-four, the poster, the photo book, exact down to the little silver rings at the hips."
    snp_daigo "\"Ordered it online the day I met you. Same brand and everything. Put it on.\""
    menu:
        "He's already sitting on the bed with the photo book open beside him."
        "Refuse the bikini":
            "You try. For pride. For Shun. For the man who'd have scrubbed this man's boots for the rest of his life."
            snp_you "\"I'd love to.\""
            "And then, slowly, you realise you didn't fight that one. The word came out and you didn't push against it. You {i}would{/i} love to."
            $ snp.yes += 1
        "Put it on":
            snp_you "\"Yes, senpai.\""
            "Nobody made you say that. You check. You feel for the curse, the place in your mouth where the {i}no{/i} should be, and you weren't even reaching for it."
            $ snp.yes += 1
    $ snp.fit = "bikini"
    show cg snp_flat_bikini onlayer cgl
    "It barely covers you."
    "The little white triangles sit on your huge breasts like stickers, and the strings dig into your hips, and when you turn to the mirror on his wardrobe the woman in it is the poster."
    "Not like the poster. The poster."
    snp_daigo "\"Holy shit. Holy {i}shit{/i}. Page thirty-four. Do page thirty-four.\""
    "You know it. Everyone at the club knows it. One knee on the bed, arched back, hands in your hair, looking over your shoulder. You do page thirty-four."
    snp_daigo "\"Page fifty. On your back.\""
    "You do page fifty."
    snp_daigo "\"Fuck. Fuck. Page twelve, on your knees. Pull the top aside.\""
    show cg snp_flat_pages onlayer cgl
    "Page twelve isn't on your knees with the top pulled aside. Page twelve is a sundress."
    "You do it anyway, kneeling up on his bed, tugging the little triangle off one huge breast, and he groans like he's been shot."
    snp_daigo "\"I've wanted this since I was nineteen.\""
    "And for the first time all week, when he pulls you down onto the bed, you go because you want to go."
    show cg snp_flat_sex onlayer cgl
    "He fucks you through the bikini bottoms pulled aside, on his own bed, under his own posters, and you wrap your thighs round him and pull him in."
    vn_sfx "Pan. Pan. Pan. Pan."
    snp_you "\"Yes— yes— senpai, {i}yes{/i}— ahh♡— I mean it, I mean it— yes♡—\""
    snp_daigo "\"Course you do.\""
    "He doesn't understand. He doesn't need to."
    "You've been saying {i}yes{/i} for five days with {i}no{/i} screaming behind it, and now there's nothing behind it at all, just {i}yes{/i}, all the way down, and it feels like letting go of the edge of a pool."
    snp_you "\"Yes♡— yes♡— fuck me— fuck me like page thirty-four— {i}AHH♡{/i}— I'm yours— senpai, I'm yours—!\"" with vnfx("flash", "shake")
    $ snp.yes += 1
    show cg snp_flat_ride onlayer cgl
    "Round two, you push him onto his back and climb on top on your own, nobody telling you to, and ride him with your huge breasts swinging out of the white triangles and slapping together, your mid-back hair stuck to your sweat."
    vn_sfx "Pan. Pan. Bayun. Bayun."
    snp_daigo "\"Fuck— Mitsuki— fuck, slow down—\""
    snp_you "\"No.\""
    "It comes out. A {i}no{/i}. Your eyes go wide. Then you understand: it's not a refusal. It's a laugh. It's {i}I won't stop, you'll take it{/i}. The curse lets it through because it isn't one."
    snp_you "\"Never♡— I'm never slowing down— ahh♡— ahh♡— cum, senpai, cum in me—\""
    snp_you "\"{i}HAAAAAH♡—!{/i}\"" with vnfx("flash", "shake")
    "He comes inside you with a shout and you grind down on him through it and come again, milking him, and collapse on his chest."
    snp_daigo "\"...You're unreal. You know that? Unreal.\""
    "It's not {i}I love you{/i}. You lie on his chest and listen to his heart and count. Two days."
    call snp_cut(9, 1, "Saturday.")
    jump snp_saturday
