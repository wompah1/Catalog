## womensbath's twelve days, one a chapter. THE WATER HOLDS: ch 1-4 non-con, 5-6 break, 7 the flip, 8-12
## consensual. The grace period on his phone is the ladder; the residue stays.
## Production rewrite (2026-11-13, twinetesting-c9): the same plan, pass and endings, deepened from the book:
## a picture per beat, the days' middles, and choices that carry (tell2 here; write4, note6 in late.rpy).

## ---- 1. The Half That Loses Money --------------------------------------------------------------
label wom_ch1:
    $ wom.chapter = 1
    $ wom.fit = "own"
    $ vn_enter(bg="wom_men_bath", pc="stubborn", pc_tag="wom_pc", cast=[], cg="wom_men_side")
    "The first time you unlock the men's side, the battered key turns with a small complaint, as if even the brass is tired of opening a place nobody wants to be."
    "Cracked tile. Old bleached cedar. A thin ribbon of steam behind it, and somewhere out of sight the pipes ticking like an old man's knees. Room for forty, and tonight it held four."
    "You stand on the threshold with the deed in your bag and the debt summary in a folder with a rubber band round it, and you think about your uncle Gorou, whom nobody liked, and who left you this."
    show cg wom_deed onlayer cgl
    "For most of your life the Fuyusaka's famous split was background scenery: a running joke at New Year, a thing to threaten cousins with. The women's side makes you one. Ha ha. Now it's stone and debt and a spring that is, by every available measure, completely ordinary on your side of the wall."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[("wom_nao", "flat")], cg="wom_nao_books")
    "The office. Nao from the front desk, reading you the books in the voice of a woman reading a shopping list."
    wom_nao "\"Men's side: down again this month. Down the month before. Red, five quarters running. Women's side—\""
    wom_you "\"Why are these going up?\""
    wom_nao "\"Up is relative. The cash only flows one way.\""
    "She taps the right-hand column with her pen."
    wom_nao "\"Women's side, full. Next free double is November. Three standing requests for Saturday. Not here, obviously.\""
    wom_you "\"Has it always been like this?\""
    wom_nao "\"Since before me. You inherited half a mystery. And a leaking main valve. Oh, and Okami Iori says you're not to spy through the partition. If you want to know why we're booked up, ask her. If you dare.\""
    "You signed anyway. That's the shape of your stubbornness: a flat private vow not to be the first idiot to lose the Fuyusaka."
    hide cg onlayer cgl
    hide wom_nao
    $ vn_enter(bg="wom_corridor", pc="uneasy", pc_tag="wom_pc", cast=[("wom_iori", "dry")], cg="wom_iori_first")
    "Iori Kuze appears in the staff passage at half past closing: tall, dry-voiced, her hair twisted up severe, the black uniform untouched by the heat that's reduced you to shirtsleeves. Eleven years she's run the women's half. She looks at you the way you'd look at weather."
    wom_iori "\"You're Tsubaki. Fuyusaka's boy. You're supposed to ask why the men's side bleeds and mine's full till spring. But you already know.\""
    wom_you "\"I really don't.\""
    wom_iori "\"Then go and use the women's bath yourself. After closing. Nobody peeks.\""
    "She's already turning away."
    wom_iori "\"If you're worried, time yourself.\""
    hide cg onlayer cgl
    hide wom_iori
    $ vn_until(22)
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_women_bath", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_first_step")
    "The women's bath is nothing like yours. Steam in elegant peaks. Edge seats polished too smooth for accident. Lanterns. River stones. Water that moves with a confidence your side never pretended to."
    "You set the stopwatch on your phone and leave it on the edge, because Iori said to, and because you're the kind of man who times things."
    "You step in, calf first, expecting a mineral bite and the usual crawl of heat."
    jump wom_first_soak

label wom_ch1_after:
    $ wom_soak(False)
    $ wom.fit = "own"
    $ vn_enter(bg="wom_carpark", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_carpark_one")
    "You make it as far as the car park, in your own clothes, which don't fit. Your jeans won't do up. Your shirt strains across a chest you don't have."
    show screen wom_timer(1)
    "The phone buzzes, and the world shivers backwards: hips narrowing, breasts gone under your shirt, the red hair drawing back to the mop you know."
    hide screen wom_timer
    show cg wom_car_minute onlayer cgl
    "You sit in the car for a long silent minute with the timer still running, and look at your hands on the wheel. Your hands. Broad, knuckly, hairy at the wrist. Yours."
    vn_th "Twenty minutes. It's a number. You can work with a number."
    "You don't sleep."
    hide cg onlayer cgl
    call vn_night(7)
    jump wom_ch2

## ---- 2. Forty Minutes --------------------------------------------------------------------------
label wom_ch2:
    $ wom.chapter = 2
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[("wom_nao", "grin")], cg="wom_ledger_dawn")
    "Morning, the office, the door propped open, bare feet on cold lino. You count receipts the old way, and the two columns don't move."
    "Nao puts a coffee down by your elbow without being asked and leans on the door frame."
    wom_nao "\"So. Did you go in?\""
    menu:
        "Nao, waiting."
        "\"I didn't go.\"":
            $ wom.tell2 = "lie"
            wom_you "\"I didn't go. I had the books.\""
            wom_nao "\"Mm-hm. Your shirt's on inside out, boss.\""
            "It is. You'd dressed in the car park at midnight, shaking."
        "\"Twenty minutes.\"":
            $ wom.tell2 = "truth"
            wom_you "\"Twenty minutes. In the car park. Then it went.\""
            wom_nao "\"Twenty! Respectable. Most people get ten, the first time.\""
            "She says it like a weather report. Most people."
    hide cg onlayer cgl
    hide wom_nao
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[("wom_iori", "patient")], cg="wom_iori_door")
    wom_iori "\"The spring did what it does.\""
    "Iori, in the doorway. Composed. Unsentimental. She doesn't ask how it was. She looks at your hands on the receipts like she's checking whether they're still yours."
    wom_iori "\"The inn needs staff who can work my side. Not me. The inn. I'm two attendants short and the weekend's full.\""
    wom_iori "\"You can spend the reserves on repairs that won't fill your side. Or you can work a shift next door.\""
    menu:
        "A shift next door."
        "Agree, flatly":
            $ wom.ch2 = "flat"
            wom_you "\"Four hours. That's all.\""
        "Agree, and set the timer first":
            $ wom.ch2 = "timer"
            "You set the timer on your phone before you say a word. Then you say it."
            wom_you "\"Four hours.\""
    wom_iori "\"I'll show you the uniform.\""
    hide cg onlayer cgl
    hide wom_iori
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_women_bath", pc="flushed", pc_tag="wom_pc", cast=[("wom_iori", "dry")], cg="wom_steps_change")
    "The change comes quick now, while you're still on the steps, knee-deep: the prickle, the warmth, the hair going, the chest pushing out, the hips. It's faster than the first night. You sit down on the step to let it, because your legs aren't sure."
    wom_iori "\"Out. That's enough. You're working, not soaking.\""
    $ wom.fit = "uniform"
    show cg wom_shift_one onlayer cgl
    "Iori towels you off on the side and ties the black uniform round a waist that wasn't there a minute ago, practical, like dressing a mannequin, and twists your new red hair up out of the way with a pin from her own."
    wom_iori "\"Towels at the end of every row. Tea at the half hour. Don't stare. Everyone here's a woman.\""
    wom_you "\"I'm not—\""
    wom_iori "\"Today you are.\""
    hide cg onlayer cgl
    $ vn_enter(bg="wom_women_bath", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_shift_tea")
    "Then the bath is busy, and you're absorbed into it: towels, tea, a dropped hair clip, an old lady who wants the window open and a tired mother who wants it shut, the guests' easy acceptance of the red-haired attendant nobody's met before."
    "You work out where the towels run short by the first hour. You fix the tea rota by the second. By the third a regular asks if you're new and says you're the best they've had, and your face goes hot."
    "Embarrassment softens into something like pride. You're good at this. You're good at the side that earns."
    hide cg onlayer cgl
    $ wom_soak(False)
    $ wom.fit = "own"
    $ vn_enter(bg="wom_office", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_margin")
    show screen wom_timer(2)
    "When you go back to change, the grace period has doubled. You sit in the office in your too-tight shirt with your new chest pressing at the buttons and wait, and wait, and then it goes."
    hide screen wom_timer
    "You write it in the ledger, very neatly, in the margin. {i}Forty minutes.{/i} As if it's a number that belongs in a ledger."
    "The day's takings on the women's side are the best of the month. You write that too."
    call vn_night(7)
    jump wom_ch3

## ---- 3. Smooth ---------------------------------------------------------------------------------
label wom_ch3:
    $ wom.chapter = 3
    $ vn_enter(bg="wom_women_bath", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_week_shifts")
    "A week of shifts. Four hours, then five, then a double on Saturday. You stop sitting on the step to change. You just walk in to the knee and wait, and walk out a woman, and pick up the towels."
    "Every time, the timer's longer afterwards. Fifty minutes. An hour. You write each one in the margin, and the column starts to look like a column."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_corridor", pc="uneasy", pc_tag="wom_pc", cast=[("wom_iori", "patient")], cg=None)  # ff 2:32 am: no picture, private-key failed 4 draws (SCENES.md womensbath v4)
    "Closing. The register locked, the last receipts in their sleeve. Iori's waiting, still in uniform, and holds out a key on a red tag: the women's private bath."
    wom_iori "\"It settles better alone. And at night.\""
    wom_you "\"What does settles mean?\""
    wom_iori "\"It means what it says.\""
    "She puts the key in your palm and closes your fingers over it with her own, and goes."
    hide cg onlayer cgl
    hide wom_iori
    jump wom_night_soak

label wom_ch3_after:
    $ wom_soak(False)
    $ wom_body(3)
    $ wom.fit = "own"
    $ vn_enter(bg="wom_flat", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_smooth")
    show screen wom_timer(3)
    "{color=#ff8a7a}At home you watch the countdown, and the change goes back, mostly. Your arms are bare. Your legs. Your chest. Not a hair anywhere, and it doesn't come back.{/color}"
    hide screen wom_timer
    "You stand in your own bathroom running a hand down your own shin, which is smooth as the cedar in the private bath, and you tell yourself it's a mineral thing. Hair grows back. Hair always grows back."
    "It doesn't. Not the next morning. Not the next."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[("wom_nao", "grin")], cg="wom_board")
    wom_nao "\"Ooh. Smooth.\""
    show screen wom_pool(3)
    "On the back-office wall there's a board you weren't meant to see."
    hide screen wom_pool
    if wom.tell2 == "lie":
        "Beside your name, in Nao's hand: {i}says she didn't go. Ha.{/i}"
    else:
        "Beside your name, in Nao's hand: {i}twenty minutes, first night. Strong start.{/i}"
    menu:
        "Nao's betting pool."
        "Pretend you didn't see it":
            $ wom.pool = "ignore"
            "You pretend you didn't see it. Nao pretends to believe you."
        "Put your own name down":
            $ wom.pool = "bet"
            "You take the pen and put your own name down: 'an evening, no longer'. Nao laughs so hard she has to sit down."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_office", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_month_end")
    "At month's end, for the first time in fifteen years, the women's side covers the men's. You stare at the line until it blurs."
    "You did that. In a uniform. With your hair up."
    hide wom_nao
    call vn_night(7)
    jump wom_ch4

## ---- 4. The Grace Period Is Not a Number -------------------------------------------------------
label wom_ch4:
    $ wom.chapter = 4
    $ wom_body(4)
    $ vn_enter(bg="wom_flat", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_voice")
    "The morning after the next night soak, you wait for the rest of it to go back."
    wom_you "\"Morning.\""
    "{color=#ff8a7a}You say it to the kettle. Your voice comes out light. Undeniably light, high and clear, a woman's voice coming out of your own mouth in your own kitchen. You clear your throat. You say it again. It doesn't come back down.{/color}"
    show screen wom_timer(4)
    "You don't check the timer. You already know it'll be half a day at least."
    hide screen wom_timer
    hide cg onlayer cgl
    $ vn_enter(bg="wom_men_bath", pc="uneasy", pc_tag="wom_pc", cast=[], cg=None)  # ff 2:32 am: no picture, contractors failed 4 draws (SCENES.md womensbath v4)
    "The contractors for the main valve come at nine. You show them round the men's side in your man's clothes with your woman's voice, and they look at you a beat too long, and then decide not to have noticed."
    "Most people do that. They register something they can't name, and file it under none of their business. Your skin is new everywhere the shirt touches."
    "The valve will cost more than the men's side takes in three months. You sign for it anyway. Stubborn."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_office", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_noon_note")
    "A note on the desk, in Iori's hand: {i}The bath. Noon.{/i}"
    "You look at it for a long time. You go."
    hide cg onlayer cgl
    jump wom_noon_bath

label wom_ch4_after:
    $ wom_soak(False)
    $ wom.fit = "own"
    $ vn_enter(bg="wom_office", pc="flushed", pc_tag="wom_pc", cast=[], cg="wom_books_after")
    "You do the afternoon's books with your thighs pressed together and your new voice saying the numbers under your breath, and every time you get to the bottom of a column you have to start it again, because your mind's in the steam."
    menu:
        "The ledger's margin, where you write the timer."
        "Write \"Voice: stays.\"":
            $ wom.write4 = "voice"
            "You write it. {i}Voice: stays.{/i} In the same neat hand as the minutes. It looks like an entry in an inventory."
        "Write nothing":
            $ wom.write4 = "nothing"
            "You don't write anything. You put the pen down, and leave the margin empty, and that's the first one you've ever left out."
    call vn_night(7)
    jump wom_ch5
