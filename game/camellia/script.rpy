## camellia's five nights. UNIFORM: ch 1-2 non-con (Kurosawa's rig and her floor's rules; Miyamoto's dohan),
## ch 3 the flip ("lock the cage", the book's words), ch 4-5 consensual. Each night closes on the board.
## Production rewrite (2026-11-13, twinetesting-c9): the same plan, pass and both endings, deepened from the
## book: a picture per beat, the nights' middles, and choices that carry (name1, drill2 here).

## ---- 1. Worst Host on the Men's Floor ----------------------------------------------------------
label cam_ch1:
    $ cam.chapter = 1
    $ cam.fit = "suit"
    $ vn_enter(bg="cam_mens_floor", pc="poised", pc_tag="cam_pc", cast=[], cg="cam_bottom")
    show screen cam_board(1)
    "Eleven months. The number is there every time you pass the board at the end of the men's floor, your name at the bottom in dry-erase marker going faded and ragged."
    hide screen cam_board
    "The Camellia's men's floor on a Thursday: black leather booths, gold trim, a champagne tower nobody's ordered yet, and twelve hosts in good suits working the room like sharks working a reef. Eleven of them, anyway."
    show cg cam_reject onlayer cgl
    "Three rejections by ten. Two \"maybe next time\"s. One woman who angles her phone at you, turns away, and murmurs something behind her hand to her friend, and her friend laughs, and looks, and laughs again."
    "You try the line Takumi uses. You try the line Kitahara uses. You try your own line, which is about the weather. She picks Takumi."
    cam_host "\"Any picks tonight, Ryo?\""
    cam_you "\"Not yet, Takumi.\""
    "The whole floor hears it. At one, you're told to clock out."
    hide cg onlayer cgl
    $ vn_enter(bg="cam_alley", pc="mortified", pc_tag="cam_pc", cast=[("cam_ichinose", "easy")], cg="cam_ichinose_first")
    "Out back for a cigarette you don't smoke, and there's the scout from the Sanctuary across the street, Ichinose, in a coat that costs your rent, looking the Camellia's back door up and down like a menu."
    cam_ichi "\"You're the Camellia's Ryo? I'd heard. No offence. Not my type of product.\""
    "He says it nicely. That's the worst of it. He says it like he's telling you it's going to rain."
    hide cg onlayer cgl
    hide cam_ichinose
    $ vn_enter(bg="cam_office", pc="mortified", pc_tag="cam_pc", cast=[("cam_kurosawa", "smoke")], cg="cam_office_folder")
    "Kurosawa's office is colder than the floor: glass and leather, ashtrays always cleaned and never empty. She's forty, immaculate, and her suit does nothing to hide what's behind her zip."
    cam_kuro "\"Dismal. Bottom of the men's floor eleven months running. I need two gone by Friday. You and Kitahara.\""
    cam_you "\"I know. I know the numbers. Give me another month, I'll—\""
    cam_kuro "\"You've had eleven.\""
    "Then her eyes go from your jaw to your chest and stay a beat too long. She lights a cigarette off the last one, and slides a folder across the desk."
    cam_kuro "\"However. There's a need on the women's side. You don't have the face for the men's. You have the bones for the women's. With the rig, corset, forms, wig, it's arithmetic, not sentiment. You want a week, or a year?\""
    cam_you "\"The women's floor. You're serious.\""
    cam_kuro "\"I'm always serious. Work starts tonight. Dressing room. I'll prepare you myself.\""
    hide cg onlayer cgl
    hide cam_kurosawa
    jump cam_rig

label cam_ch1_floor:
    hide cg onlayer cgl
    $ cam_pc_name = "Rina"
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_womens_floor", pc="poised", pc_tag="cam_pc", cast=[("cam_saki", "sly")], cg="cam_saki_first")
    "The women's floor has a different gravity: softer lights, perfume, disco under the talk, men in the booths instead of women, and the girls moving between them like they're being paid by the step."
    "Saki, the number one, flicks one appraising look over you from the bar: the wig, the forms, the corset, the red mouth Kurosawa painted on, and whatever's on your face under it."
    cam_saki "\"Hm. She's done worse. Walk to the end of the bar and back.\""
    "You walk. Heels you've never worn, on a floor you've never stood on, with a mouth that still tastes of the dressing room."
    cam_saki "\"Hips, not knees. Again.\""
    "You do it again."
    cam_saki "\"Fine. You'll pass in the dark. Go and sit with the blue suit before Mai gets him.\""
    hide cg onlayer cgl
    hide cam_saki
    $ vn_enter(bg="cam_womens_floor", pc="poised", pc_tag="cam_pc", cast=[("cam_domoto", "hungry")], cg="cam_first_floor")
    "And the first customer of the night waves you over before you've found your mark: Domoto, a salaryman in fitted blue, all teeth."
    cam_domoto "\"I can't believe we've never met. You new? What's your name?\""
    menu:
        "Domoto, waiting for a name."
        "\"Rina.\"":
            $ cam.name1 = "rina"
            cam_you "\"Rina. First night. Lucky you. New girl means extra attention.\""
        "\"Whatever you'd like it to be.\"":
            $ cam.name1 = "yours"
            cam_you "\"Whatever you'd like it to be. First night. Lucky you.\""
            cam_domoto "\"Ooh. Then I'll call you mine.\""
            "It's the cheapest line in the building and it works like a key in a lock."
    show cg cam_first_laugh onlayer cgl
    "It runs almost by itself. Lashes, cadence, the knees together, the laugh a little higher than your own, the hand on his arm when you say something risky. He leans in closer than any woman on the men's floor ever did."
    "And you feel it go all the way through the corset and the silicone: attention. Eleven months of nobody, and then this, in a stranger's eyes, for a girl who doesn't exist."
    "You like it. You hate how much you like it. You order him the second bottle."
    hide cg onlayer cgl
    hide cam_domoto
    show screen cam_board(2)
    "At close a new name goes up at the bottom of the women's board. Not Ryo."
    hide screen cam_board
    $ vn_enter(bg="cam_dressing", pc="flushed", pc_tag="cam_pc", cast=[("cam_kurosawa", "smoke")], cg="cam_unlace")
    "In the dressing room afterwards Kurosawa unlaces you herself, knot by knot, the way she did it up, and your ribs come back one at a time, and you breathe all the way down for the first time in six hours and it feels like being let out of something."
    cam_kuro "\"Three bottles. Domoto's never ordered three bottles for anyone.\""
    cam_you "\"He liked the laugh.\""
    cam_kuro "\"He liked you. Same time tomorrow.\""
    "She hangs the corset on its hook, and the wig on its stand, and turns the bulbs off, and in the dark mirror there's a man in his vest with lipstick still on, and you can't tell which of you is the costume."
    hide cg onlayer cgl
    hide cam_kurosawa
    call vn_night(18)
    jump cam_ch2

## ---- 2. Dohan --------------------------------------------------------------------------------
label cam_ch2:
    $ cam.chapter = 2
    $ cam_body(1)
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_dressing", pc="poised", pc_tag="cam_pc", cast=[("cam_saki", "sly")], cg="cam_pour_drill")
    "Saki corners you by the lockers with a highball and a running commentary."
    cam_saki "\"Pour like that again and I'll cut your fingers off. Like this. Pretend the ice is worth more than your rent. One joke, not ten. Touch his arm when you say something risky; his knee only if you mean to keep him.\""
    menu:
        "Saki's drill."
        "Do it her way":
            $ cam.drill2 = "hers"
            "You pour it her way, wrist turned, the ice sliding, the glass never filled past the line she draws with her nail. She watches you do it nine times."
            cam_saki "\"There. Now you pour like a girl who costs money.\""
        "Do it your way":
            $ cam.drill2 = "yours"
            "You pour it your way, the host way, the way you poured for women who never picked you. It comes out too fast and too full and too eager."
            cam_saki "\"No. That's how a boy pours when he wants to be liked. A girl pours like she's doing you a favour. Again.\""
    cam_you "\"It's desperate.\""
    cam_saki "\"I know. That's why it works. Let them smell you want it more.\""
    show cg cam_heels_drill onlayer cgl
    "Then the heels: up and down the corridor behind the dressing room, a book on your head that falls off on every turn, Saki clapping the beat. Then the laugh: lower, slower, three notes, not five. Then the walk away from the table, which is the most important walk, she says, because that's the one they pay to watch."
    cam_saki "\"You're not bad. You're not good. You're interesting. Interesting sells for about a month.\""
    hide cg onlayer cgl
    hide cam_saki
    $ vn_enter(bg="cam_womens_floor", pc="poised", pc_tag="cam_pc", cast=[("cam_miyamoto", "leer")], cg="cam_miyamoto_lap")
    "Miyamoto: thinning hair, thick wallet, a laugh like a car that won't start. Saki drops you in his lap like a new pet and goes to her own table."
    cam_miya "\"New girl! Kurosawa's always hiding the new girls. Let me look at you.\""
    "He looks with his hands. You laugh the three-note laugh and move his hand from your thigh to your waist and he moves it back. He leaves a bill bigger than anything Ryo ever saw, and books the dohan."
    hide cg onlayer cgl
    hide cam_miyamoto
    $ vn_until(23)
    $ vn_enter(bg="cam_karaoke", pc="poised", pc_tag="cam_pc", cast=[("cam_miyamoto", "leer")], cg="cam_dohan_dinner")
    "Not a limo: a karaoke dive, greasy and neon, his hand hooked round your corseted waist."
    menu:
        "Dinner, on his account."
        "Order the shochu":
            $ cam.order = "shochu"
            "He likes you giddy on shochu. You lean in, close enough to smell his aftershave, and laugh at things that aren't jokes."
        "Order tea":
            $ cam.order = "tea"
            "You order tea. He orders you a shochu anyway, \"for the voice\"."
    show cg cam_karaoke_sing onlayer cgl
    "He makes you sing. A duet, a love song, his arm round you and his mouth too near the microphone. You hit the high notes in the girl's part, and you don't know where that voice came from, and he claps like a seal."
    cam_miya "\"You're prettier than your profile.\""
    cam_you "\"Liar. Come again tomorrow.\""
    "It's only dinner. Saki said it's only dinner. Then he's paying, and the taxi isn't going back to the club."
    hide cg onlayer cgl
    hide cam_miyamoto
    jump cam_hotel

label cam_ch2_cage:
    hide cg onlayer cgl
    $ vn_until(3)
    $ cam.fit = "rig"
    $ vn_enter(bg="cam_office", pc="mortified", pc_tag="cam_pc", cast=[("cam_kurosawa", "cool")], cg="cam_black_case")
    "Back at the club, three in the morning, the managers' cigarette hour. You come in through the back with your wig crooked and your knickers in your bag, and Kurosawa's light is on."
    "She looks at you once, at the wig and the bag and the way you're standing, and knows exactly where you've been. She doesn't ask. She perches on the edge of her desk, sleeves rolled, and snaps open a slim black case."
    cam_kuro "\"Presentation discipline. There's a line a girl doesn't cross. Knickers off. Legs apart.\""
    cam_you "\"No. What is that? Kurosawa, no, I'm not wearing that—\""
    jump cam_cage

label cam_ch2_after:
    hide cg onlayer cgl
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_womens_floor", pc="flushed", pc_tag="cam_pc", cast=[("cam_domoto", "hungry")], cg="cam_domoto_squirm")
    "Walking back out, locked, every step is different. The cage makes you move different: shorter steps, the hips swinging more to keep the weight off it, the thighs pressed together. Saki's walk, without trying."
    "You catch yourself squirming in the booth, and Domoto, at his table at half-past exactly as he is every night, sees it."
    if cam.name1 == "yours":
        cam_domoto "\"Something wrong, mine?\""
    else:
        cam_domoto "\"Something wrong, Rina?\""
    cam_you "\"New shoes.\""
    "He picks you. He always picks you. He tips like a man who wants to be remembered, and you find yourself watching the door for him before his slot."
    hide cg onlayer cgl
    hide cam_domoto
    show screen cam_board(3)
    "Second on the board."
    hide screen cam_board
    $ vn_enter(bg="cam_dressing", pc="flushed", pc_tag="cam_pc", cast=[("cam_saki", "sour")], cg="cam_saki_board")
    cam_saki "\"Second. In a fortnight. Interesting sells for about a month, I said. I'll have to revise that.\""
    "She says it to the mirror, doing her lashes, and doesn't look at you once."
    "Then, still to the mirror, without turning round:"
    cam_saki "\"Miyamoto takes all the new ones to that hotel. I should have told you. I didn't, because I wanted to see if you'd come back. You came back.\""
    cam_you "\"Did you go? Your first time?\""
    cam_saki "\"Everybody goes, sweetheart.\""
    hide cg onlayer cgl
    hide cam_saki
    call vn_night(18)
    jump cam_ch3

## ---- 3. The Cage -----------------------------------------------------------------------------
label cam_ch3:
    $ cam.chapter = 3
    $ vn_until(2)
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_office", pc="poised", pc_tag="cam_pc", cast=[("cam_kurosawa", "raw")], cg="cam_whisky")
    "The night gives up early. A typhoon warning; the trains stopping at midnight. Saki's gone, the floor's empty, the champagne tower dismantled, and the light's on in Kurosawa's office."
    cam_kuro "\"Come in, then. Or you'll keep scuffing the floor.\""
    "Two thick glasses of whisky. Her jacket still on, her tie still knotted. Rain threatening on the window and not falling."
    cam_kuro "\"Sit. You've had a good fortnight. Sit down and drink something that isn't on a customer's bill.\""
    "You sit. The cage presses. You don't mention it. She sees you not mention it."
    cam_kuro "\"Do you know how many men I've built, Rina? Names, not numbers. Masaki. Nori. Gin. Yukio. Harada. I trained the accent out of their mouths and taught them where to put a hand. Hosts get good, hosts get noticed, hosts leave. Every single one.\""
    cam_you "\"So the women's floor—\""
    cam_kuro "\"Nobody gets poached. There's nowhere in this city to sell what I make down here. You see it now.\""
    "Her voice doesn't rise. She drinks."
    cam_kuro "\"I'm not apologising. I'd do it again.\""
    show cg cam_tie onlayer cgl
    "She finally pulls her tie loose. It's the only honest thing anybody's said to you in eleven months. The only honest thing anybody's said to you since the men's floor."
    cam_you "\"Harada went to the Sanctuary.\""
    cam_kuro "\"Harada went to the Sanctuary. Ichinose came for him with a card and a number. He didn't say goodbye. They never say goodbye.\""
    "She looks at you over the glass, and for a moment she isn't the architect. She's a woman in an office at two in the morning with a storm coming, who's been left five times."
    hide cg onlayer cgl
    menu:
        "Kurosawa, with her tie undone."
        "\"If it's a cage, lock it.\"" (ending=True):
            $ cam.asked = True
            cam_you "\"Do it, then. If it's a cage, lock it.\""
        ## MAKE IT REAL's fork (the alternate route; owner, 2026-11-13): real.rpy
        "\"Then make it so nobody can poach me.\"" (ending=True) if CAM_REAL_READY:
            $ cam.asked = True
            $ cam.real = True
            cam_you "\"Then make it so nobody can poach me. Not the forms. Not the tape. Me. Make it real.\""
            "She looks at you for a long time over the glass, the way she looked at you the first night, doing the arithmetic."
            cam_kuro "\"There's a doctor. Fourth floor of this building. Cash. He doesn't ask.\""
            cam_you "\"Then I won't either.\""
            cam_kuro "\"You understand what you're asking. Nobody takes a body back to the men's floor.\""
            cam_you "\"That's why I'm asking.\""
    jump cam_desk

label cam_ch3_after:
    hide cg onlayer cgl
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_office", pc="bright", pc_tag="cam_pc", cast=[("cam_kurosawa", "cool")], cg="cam_storm_after")
    "The storm comes in at four and rattles the glass. You sit on her office floor in her shirt with your wig on the desk and your own short hair sticking up, and she smokes by the window and doesn't say anything, and it's the best silence you've ever been in."
    cam_kuro "\"Staff call in twenty.\""
    "That's all she says, the next evening, when you come in. She doesn't need to say anything else."
    hide cam_kurosawa
    if cam.real:
        call cam_real_weeks
    call vn_night(18)
    jump cam_ch4

## ---- 4. Number One ---------------------------------------------------------------------------
label cam_ch4:
    $ cam.chapter = 4
    $ cam.fit = "red"
    $ vn_enter(bg="cam_dressing", pc="bright", pc_tag="cam_pc", cast=[("cam_kurosawa", "cool")], cg="cam_red_dress")
    if cam.real:
        "Ranking night, six weeks on. Kurosawa dresses you herself for it: the red dress, cut for the rig, slit to the hip, the forms sitting high and proud over something that isn't nothing any more, tender under the tape when she smooths it down with her thumbs. The red wig in its two long low tails, brushed out like silk. She steps back and looks."
    else:
        "Ranking night. Kurosawa dresses you herself for it: the red dress, cut for the rig, slit to the hip, the forms sitting high and proud, the red wig in its two long low tails brushed out like silk. She steps back and looks."
    cam_kuro "\"Walk.\""
    "You walk. The cage, the heels, the hips. Saki's walk, which is yours now."
    cam_kuro "\"Yes.\""
    hide cg onlayer cgl
    hide cam_kurosawa
    $ vn_enter(bg="cam_womens_floor", pc="bright", pc_tag="cam_pc", cast=[("cam_saki", "sour")], cg="cam_board_reveal")
    "The floor is packed. Kurosawa takes it in her official voice: \"Tonight, gentlemen, we revise the line-up.\""
    show screen cam_board(4)
    "The new card goes up. RINA, first. Saki, second."
    hide screen cam_board
    cam_saki "\"Shall we toast? To another month at the top?\""
    if cam.drill2 == "hers":
        "She holds out her glass. You see her see the way you hold yours: her way, wrist turned, never filled past the line."
    else:
        "She holds out her glass. You see her see the way you hold yours: your own way, still, too full and too eager, and somehow it works for you anyway, and that's what she can't forgive."
    menu:
        "Saki's glass, held out."
        "Toast her sweetly":
            $ cam.toast = "sweet"
            cam_you "\"To hard work paying off.\""
            "Soft-edged. Her lip snarls, just barely."
        "Toast the new number one":
            $ cam.toast = "crown"
            cam_you "\"To the new number one.\""
            "The room roars. Saki downs hers in one and slams the glass upside down."
    cam_saki "\"Enjoy it while you can, sweetheart. Round here everybody gets trained sooner or later.\""
    show cg cam_saki_kiss onlayer cgl
    "Then she kisses you. In front of the whole floor, hard, both hands in the red wig, her lipstick on your lipstick, and the room loses its mind and the tips come in like weather."
    cam_saki "\"There. Now they'll pay double to watch us fight.\""
    "She lets go, and goes back to her table, and for the rest of the night the two of you are the best show in the building, and you both know it."
    hide cg onlayer cgl
    hide cam_saki
    $ vn_enter(bg="cam_alley", pc="poised", pc_tag="cam_pc", cast=[("cam_ichinose", "easy")], cg="cam_card")
    $ vn_enter(bg="cam_dressing", pc="bright", pc_tag="cam_pc", cast=[("cam_saki", "sly")], cg="cam_saki_mirror")
    "Between sets the two of you share the long mirror, doing your lashes side by side, not talking, the way rivals share a lane."
    cam_saki "\"You know what you've got that I haven't?\""
    cam_you "\"Kurosawa's attention?\""
    cam_saki "\"You know what it's like on the other side. The men's floor. Being looked through. Every man in that room's been looked through by somebody, and you look at them like you know. That's the whole trick. I can't do that. I've only ever been looked at.\""
    "She caps her mascara and goes out without waiting for an answer, and it's the nicest thing she's ever said to you, and you're fairly sure she meant it as a threat."
    if cam.real:
        call cam_real_saki
    hide cg onlayer cgl
    hide cam_saki
    "Out back for air, and Ichinose from the Sanctuary is leaning on the wall, the scout who waved Ryo off a year ago."
    show cam_ichinose easy at vn_cast_slot
    cam_ichi "\"Rina. Or would you rather talk as Ryo? We want you. Not the act. No glue, no tape. The men's floor at the Sanctuary, your name back up as Ryo, double what you're pulling here. Known as yourself.\""
    cam_you "\"You told me I wasn't your type of product.\""
    show cam_ichinose easy at vn_cast_slot
    cam_ichi "\"I was wrong. You learned something in there I can't teach. Women want a man who knows what it's like to be wanted. You'd clean up.\""
    cam_you "\"I'm not ready.\""
    show cam_ichinose easy at vn_cast_slot
    cam_ichi "\"It's not forever. But don't wait too long.\""
    "He presses the card into your palms, soft as tissue."
    hide cg onlayer cgl
    hide cam_ichinose
    jump cam_domoto_hotel

label cam_ch4_after:
    hide cg onlayer cgl
    call vn_night(18)
    jump cam_ch5

## ---- 5. One Year -----------------------------------------------------------------------------
label cam_ch5:
    $ cam.chapter = 5
    $ cam.fit = "red"
    $ vn_enter(bg="cam_dressing", pc="bright", pc_tag="cam_pc", cast=[], cg="cam_mirror_rig")
    if cam.real:
        "Three nights later. You do the rig yourself now, faster than Kurosawa ever did: corset, tape over what's yours, gently, the way Saki showed you, forms on top, the red wig in its two long low tails, the lip to match. The number one girl in the mirror, and some of her real."
    else:
        "Three nights later. You do the rig yourself now, faster than Kurosawa ever did: corset, tape, forms, the red wig in its two long low tails, the lip to match. The number one girl in the mirror."
    "And Ichinose's card in your purse, and three nights of not sleeping."
    show cg cam_card_mirror onlayer cgl
    "You take it out and prop it against the mirror, and look at the two of them: the card, with RYO on it in his tidy hand, and the girl behind it in the glass."
    "Double the money. Your own name in gold. Your own face. The men's floor, which is all you wanted for eleven months, and which looked at you every night like you were furniture."
    "And Kurosawa's light, on, down the corridor, every night, until the last girl's gone."
    hide cg onlayer cgl
    menu:
        "The card, and the office door."
        "Ask Kurosawa for a contract" (ending=True):
            $ cam.ending = "sign"
            jump cam_sign
        "Call Ichinose" (ending=True):
            $ cam.ending = "take"
            jump cam_take
