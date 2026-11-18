## womensbath, chapters 5-12: the chest stays, the bra trip, Hazuki, red at the roots (the flip), Gorou's
## ledger, nothing left to wear off, the choice (marked: Close or Restore), and the ending.

## ---- 5. Two Towns Over -------------------------------------------------------------------------
label wom_ch5:
    $ wom.chapter = 5
    $ wom_body(5)
    $ wom.fit = "own"
    $ vn_enter(bg="wom_flat", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_chest_stays")
    "{color=#ff8a7a}You wake to a pressure across your chest you can't place. You look down. They're still there: breasts, firm and unignorable, pressing at your old t-shirt.{/color}"
    show screen wom_timer(5)
    "The timer says a night. It's wrong. You know it's wrong."
    hide screen wom_timer
    hide cg onlayer cgl
    $ vn_enter(bg="wom_shops", pc="flushed", pc_tag="wom_pc", cast=[], cg="wom_bra_shop")
    "Two towns over, a shopping centre where nobody knows the Fuyusaka. You stand in front of a wall of bras for a long time."
    menu:
        "The shop assistant asks if you need help."
        "\"They're for my girlfriend\"":
            $ wom.bra = "girlfriend"
            wom_you "\"They're for my girlfriend.\""
            "She looks at your chest. She looks at you. She measures you anyway, very kindly, and tells you your girlfriend is a B."
        "Ask her to measure you":
            $ wom.bra = "measured"
            wom_you "\"Could you— measure me? Please.\""
            "She does, very kindly, and doesn't ask a single question, and you could kiss her for it in the changing room."
    $ wom.fit = "bought"
    show cg wom_fitting onlayer cgl
    "In the fitting room you put it on and look. A plain black bra, the first one that's ever fitted you, and a soft blouse from the rail outside, and a skirt, because nothing else in the shop went over the hips."
    "You look like somebody's sister. You look like somebody who'd work the women's side of a family inn and be good at it. You stand there a long time with your hand flat on the cool mirror."
    "On the drive back you keep checking the rear-view mirror, and it isn't for traffic."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_front_desk", pc="proud", pc_tag="wom_pc", cast=[("wom_nao", "grin")], cg="wom_tails")
    "Back at the Fuyusaka, Nao takes one look at you, sits you down on the front-desk stool, and puts your red hair up in two long low tails."
    wom_nao "\"There. Inn image. The guests'll love it.\""
    show screen wom_pool(5)
    "The board in the back office has a new column. Three ticks. Nao's handwriting."
    hide screen wom_pool
    "The guests do love it. Bookings tick up. You find there's a strange power in being looked at like this, and you don't say so to anyone."
    hide cg onlayer cgl
    hide wom_nao
    $ vn_until(22)
    jump wom_night_iori

label wom_ch5_after:
    $ wom_soak(False)
    $ wom.fit = "bought"
    $ vn_enter(bg="wom_office", pc="flushed", pc_tag="wom_pc", cast=[], cg="wom_chest_ledger")
    if wom.write4 == "voice":
        "You write it in the ledger with wry efficiency, under {i}Voice: stays{/i}, the way you'd record a delivery: {i}Chest: stays.{/i}"
    else:
        "You've left the margin empty since the voice. Tonight you write in it again, with wry efficiency, the way you'd record a delivery: {i}Chest: stays.{/i}"
    "The new bra's on the back of the office chair. Bookings are up again. You draw a line under the week."
    call vn_night(7)
    jump wom_ch6

## ---- 6. Two Days ------------------------------------------------------------------------------
label wom_ch6:
    $ wom.chapter = 6
    $ wom_body(6)
    $ wom.fit = "uniform"
    $ vn_enter(bg="wom_front_desk", pc="proud", pc_tag="wom_pc", cast=[("wom_hazuki", "charmed")], cg="wom_hazuki_request")
    "{color=#ff8a7a}Your hips have come out and your thighs press together all the way up. Your old body is a rumour now. You stopped trusting the timer a while ago.{/color}"
    show screen wom_timer(6)
    "Two days, it says. You don't believe it."
    hide screen wom_timer
    "Hazuki Serizawa, a regular, has asked for Miss Fuyusaka by name. Third visit this month. She's at the desk in a good coat, leaning on it, watching you fill in her card."
    wom_hazuki "\"You're the one with the red hair. Everybody says ask for the red one. She knows where the good towels are.\""
    wom_you "\"There's only one kind of towel.\""
    wom_hazuki "\"Not when you bring them.\""
    "You don't know what to do with that, so you stamp her card twice. She laughs, low, and watches you not know what to do with it, and seems to like that too."
    wom_hazuki "\"How long have you worked here? I've been coming for years. I'd have remembered you.\""
    wom_you "\"Not long. A few weeks. It's— a family thing.\""
    wom_hazuki "\"Lucky family.\""
    "She leaves a handwritten note on the tray with her key: {i}You're the reason I came back.{/i}"
    wom_hazuki "\"I'll see you at the bath, I hope.\""
    show cg wom_note onlayer cgl
    menu:
        "Hazuki's note, on the tray."
        "Keep it":
            $ wom.note6 = "kept"
            "You fold it in half and put it in the inside pocket of the uniform, over your heart, which is where the uniform's pocket is, and you don't think about why you checked."
        "Write back":
            $ wom.note6 = "wrote"
            "You take a sheet of the inn's paper and write back, in your neat ledger hand: {i}Then I'm glad you came back.{/i} You leave it on her tray with her tea."
    show screen wom_pool(6)
    "Nao underlines Hazuki's name on the board, twice, and grins at you over the desk."
    hide screen wom_pool
    hide cg onlayer cgl
    hide wom_hazuki
    $ vn_until(22)
    jump wom_iori_full

label wom_ch6_after:
    $ wom_soak(False)
    $ vn_enter(bg="wom_carpark", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_drive_home")
    "You drive home with her still sticky behind your collarbone, and the seat belt across a chest that's stayed all week, and you lie in bed waiting for the return."
    "You set the timer. You watch it. Two days, it says. You fall asleep watching it, and when you wake up it's still counting, and nothing's gone back."
    call vn_night(7)
    jump wom_ch7

## ---- 7. Red at the Roots (the flip) --------------------------------------------------------------
label wom_ch7:
    $ wom.chapter = 7
    $ wom_body(7)
    $ wom.fit = "bought"
    $ vn_enter(bg="wom_flat", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_red_roots")
    show screen wom_timer(7)
    "{color=#ff8a7a}No buzz. No beep. The return never comes. In the bathroom mirror your hair is red at the roots, your own head of it, growing out red. Every curve stays where it is.{/color}"
    hide screen wom_timer
    "From here she is she. She tries to rationalise it on the drive in, and runs out of road."
    show cg wom_drive_in onlayer cgl
    "Hair dye in the water supply. A hormone thing. A long grace period, a very long one, the longest yet. A week. Two. She goes through them all at the lights by the station, one after another, the way she'd go through suppliers, and every one of them falls over at the first question."
    "At the last set of lights she catches her own eyes in the rear-view mirror. Red lashes. Her own face, soft and certain, looking back."
    "She doesn't rationalise anything after that. She just drives."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_office", pc="flushed", pc_tag="wom_pc", cast=[("wom_nao", "grin")], cg="wom_nao_roots")
    wom_nao "\"Nice roots.\""
    "Nao doesn't say anything else. She just slides the betting-pool board round on its nail so it faces the wall, and pats it, and goes back to the desk."
    "Tsubaki brushes it off. By midday the wanting is a hum in her whole body that won't be brushed off, and she goes looking for Iori."
    hide wom_nao
    jump wom_ask

label wom_ch7_after:
    $ wom.fit = "uniform"
    call vn_night(7)
    jump wom_ch8

## ---- 8. Fifteen Years of Losses ----------------------------------------------------------------
label wom_ch8:
    $ wom.chapter = 8
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[], cg="wom_ledger_lock")
    "The discrepancy shows up in the small hours, quiet and wrong at the bottom margin of an otherwise perfect page."
    "It leads to a drawer she's never opened, and a key on Gorou's old ring, and a ledger in his hand."
    show cg wom_ledger_page onlayer cgl
    "{i}Down a fifth.{/i} {i}Let leak.{/i} {i}New promotion, cancel by letter.{/i} {i}Transfer the rest.{/i} Fifteen years of losses, every one of them made on purpose."
    if wom.write4 == "voice":
        "And in the margins, Gorou's notes, in a hand that could be yours. {i}Hair: stays. Voice: stays. Chest: stays.{/i} Neat. Like an inventory. Like yours."
    else:
        "And in the margins, Gorou's notes. {i}Hair: stays. Voice: stays.{/i} Then a gap, a long one, as if he stopped writing them down. Like you did."
    "Then, in a second hand, Iori's: {i}If you are reading this, you have taken enough. You are already ours. Whatever you fear, I feared first. I will never ask you, but I hope you will stay.{/i}"
    hide cg onlayer cgl
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_women_bath", pc="stubborn", pc_tag="wom_pc", cast=[("wom_iori", "patient")], cg="wom_ledger_iori")
    "She takes the ledger down to the bath at dawn and finds Iori in the water, as she knew she would, and drops it on the stones by her head."
    wom_you "\"You should have told me.\""
    wom_iori "\"I did. In every way except the one that would have ruined it.\""
    wom_iori "\"Gorou had to run the numbers down until he was desperate enough to step in the wrong bath. So did I. It only works on someone who needs it badly enough. If I'd invited you in, you'd always wonder. You'd be kept.\""
    menu:
        "Iori, in the water, waiting."
        "\"I'm not leaving\"":
            $ wom.ch8 = "stay"
            wom_you "\"I'm not leaving. I chose this. I keep choosing it. Even knowing. Especially knowing.\""
        "\"I keep thinking about leaving. I never do\"":
            $ wom.ch8 = "never"
            wom_you "\"I keep thinking about leaving. Every time the timer got longer. But I never did.\""
    wom_iori "\"Because there's nothing left you'd rather save.\""
    jump wom_lead

label wom_ch8_after:
    $ wom.fit = "yukata"
    call vn_night(7)
    jump wom_ch9

## ---- 9. Nothing Left to Wear Off -----------------------------------------------------------------
label wom_ch9:
    $ wom.chapter = 9
    $ wom.fit = "uniform"
    $ vn_enter(bg="wom_women_bath", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_festival")
    show screen wom_timer(9)
    "Seven mornings, and she hasn't once opened the app. Her body is finished except for one small vestige of the old one, and it's an afterthought."
    hide screen wom_timer
    "Festival week, the bath heaving. The other attendants look to her and she guides them without thinking, red tails swinging."
    show cg wom_festival_lead onlayer cgl
    "Lanterns all down the street outside, drums from the shrine, and every room in the inn booked twice over. The women's side runs three sittings a night. She runs the floor: towels, tea, the new girl who panics at the till and the old regular who wants her usual corner, the queue at the door that Nao's turned into a raffle."
    "Somebody calls her {i}Okami-san{/i}, the second okami, by mistake. Nobody corrects it."
    "At the end of the third night she counts the takings in the office with her shoes off and her feet on the desk, and the women's side has made in a week what the men's side made in a year."
    hide cg onlayer cgl
    show screen wom_pool(7)
    show cg wom_pool_close onlayer cgl
    "Nao closes the betting pool on the last night of the festival, in front of everybody, the attendants and the kitchen and the night porter crowded into the back office with cans."
    show wom_nao grin at vn_cast_slot
    wom_nao "\"The question was: how long does the boss last? Answers ranged from ten minutes to a week.\""
    if wom.pool == "bet":
        show wom_nao grin at vn_cast_slot
        wom_nao "\"The boss herself put down: an evening, no longer.\""
        "Everybody cheers. Tsubaki puts her face in her hands and laughs."
    else:
        show wom_nao grin at vn_cast_slot
        wom_nao "\"The boss pretended she never saw this board. The boss is a terrible liar.\""
        "Everybody cheers. Tsubaki puts her face in her hands and laughs."
    "Nao writes the result under the column in big letters, and everybody in the back office cheers again, louder, and somebody puts a can in Tsubaki's hand."
    hide screen wom_pool
    $ vn_until(21)
    jump wom_hazuki

label wom_ch9_after:
    $ wom.fit = "yukata"
    call vn_night(7)
    jump wom_ch10

## ---- 10. Enough to Fix It (the choice) ----------------------------------------------------------
label wom_ch10:
    $ wom.chapter = 10
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[("wom_nao", "flat")], cg="wom_proposal")
    "She wakes in Iori's arms and slips out to do the mornings. The autumn books are closed. The debts are paid. Winter is overbooked."
    "And the men's side sits in the ledger like a hole. There's enough, now, to fix it. She drafts the whole thing: repairs, hiring, a budget that would free the inn from the cycle for whoever comes next."
    show cg wom_proposal_nao onlayer cgl
    wom_nao "\"It's a good plan. It's a really good plan. The plumber's real, the budget's real. You could do it.\""
    wom_you "\"But.\""
    wom_nao "\"No but. I'm the front desk. I don't do buts. I do bookings.\""
    "She taps the winter column, which is full, and goes."
    show cg wom_proposal_iori onlayer cgl
    "Iori reads it in the doorway, every page, without sitting down, and hands it back."
    hide wom_nao
    show wom_iori dry at vn_cast_slot
    wom_iori "\"Whoever runs the men's side after you won't need my side. That's what this does. Nobody would ever have to.\""
    wom_you "\"Is that good?\""
    hide wom_nao
    show wom_iori dry at vn_cast_slot
    wom_iori "\"It's yours. I won't tell you which. Nobody told me, and nobody told Gorou, and I'm not going to be the first.\""
    "The choice is hers, all of it, for the first time."
    hide cg onlayer cgl
    hide wom_nao
    $ vn_until(22)
    jump wom_ten_night

label wom_ch10_choice:
    $ wom.fit = "yukata"
    $ vn_enter(bg="wom_office", pc="stubborn", pc_tag="wom_pc", cast=[], cg="wom_choice_ledger")
    "Morning. The proposal on the desk, and Gorou's ledger beside it."
    menu:
        "The men's side."
        "Close it for good" (ending=True):
            $ wom.ending = "close"
            jump wom_ch11_close
        "Restore it, and break the cycle" (ending=True):
            $ wom.ending = "restore"
            jump wom_ch11_restore

## ---- 11, Close: Closing the Men's Side (the book's) ------------------------------------------------
label wom_ch11_close:
    $ wom.chapter = 11
    $ vn_enter(bg="wom_men_bath", pc="stubborn", pc_tag="wom_pc", cast=[], cg="wom_sign_down")
    "She signs off the repairs, ends the contracts, and writes the last line in Gorou's ledger. They take the FUYUSAKA MEN'S SPRING sign down at noon."
    show cg wom_sign_crowd onlayer cgl
    "Two men on ladders, and the old wooden board coming down in a puff of dust, and a small crowd in the lane: Nao with her phone up, the attendants, three regulars from the women's side who've heard and come to see. Somebody claps. Then everybody does."
    "Tsubaki stands in the lane in her uniform with her arms folded under her breasts and watches the place where it was, a pale rectangle on the old cedar, and feels nothing like the idiot who lost the Fuyusaka."
    "She feels like the woman who saved it."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_front_desk", pc="flushed", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_iori_holds")
    "Iori's at the front desk, and for once in eleven years her composure goes, and she holds on to Tsubaki like she'll float off."
    hide wom_iori
    jump wom_last_change

## ---- 11, Restore (new writing): a clean inn ----------------------------------------------------------
label wom_ch11_restore:
    $ wom.chapter = 11
    $ vn_enter(bg="wom_men_bath", pc="stubborn", pc_tag="wom_pc", cast=[], cg="wom_restore")
    "She restores it. New tile. New cedar. A plumber who stays the whole winter. The men's side opens again to a full first night, and makes money in its first month, honestly."
    "She hires a manager for it, a nice man who will never need the women's side badly enough, and writes him a clean ledger with no losses in it at all."
    hide cg onlayer cgl  # ff 2:32 am: no picture, restore-open failed 4 draws (SCENES.md womensbath v4)
    "Opening night on the men's side: new cedar smelling like a forest, the tile white as teeth, the pipes quiet for the first time in living memory, and a queue. An actual queue of men in yukata, laughing in the lane, and the manager taking their money at a desk she bought him."
    "She stands at the far end of the corridor in her uniform and watches it fill, and doesn't go in. She can't, now. She doesn't want to. She watches it the way you'd watch a boat you built go out of the harbour with somebody else at the wheel."
    show wom_nao grin at vn_cast_slot
    wom_nao "\"Full. First night. Full.\""
    wom_you "\"Honest money.\""
    show wom_nao grin at vn_cast_slot
    wom_nao "\"Gorou would hate it.\""
    wom_you "\"I know. That's the best part.\""
    hide cg onlayer cgl
    $ vn_enter(bg="wom_front_desk", pc="flushed", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_iori_holds_r")
    wom_iori "\"You've broken it. Nobody after you has to.\""
    wom_you "\"Nobody after me. I'm still here.\""
    "Iori holds on to her at the front desk, and for once in eleven years her composure goes."
    hide wom_iori
    jump wom_last_change

label wom_last_change:
    $ wom_body(11)
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_private_bath", pc="proud", pc_tag="wom_pc", cast=[], cg="wom_last_change")
    "{color=#ff8a7a}Later, alone, she finds the last vestige gone. Without fanfare. Completely. What she has now is what she'd stopped admitting she wanted, and she lies back in the cedar tub and touches herself and laughs.{/color}"
    show cg wom_eleven_iori onlayer cgl
    "Then Iori, in the private bath, without reservation for the first time, both of them changed and celebrating it, slow and loud."
    show wom_iori dry at vn_cast_slot
    wom_iori "\"Let me see. Let me see all of you.\""
    "Iori kneels in the water and looks, for a long time, and then puts her mouth on her: on her breasts, her belly, between her thighs, slow, worshipful, until Tsubaki's hands are in her hair and her heels are drumming the cedar."
    show cg wom_eleven_deep onlayer cgl
    "Then Iori's in her, all of her, huge and slow, and Tsubaki wraps her legs round her waist and holds on and tells her exactly what she wants, every second of it, and gets it."
    vn_sfx "{i}Splsh. Pap. Splsh. Pap.{/i}"
    wom_you "\"Iori— {i}yes{/i}— harder— don't stop— {i}yes{/i}—!\"" with vnfx("flash", "shake")
    "They come together, loud, and the lamp shakes on its hook, and nobody comes to see, because nobody ever does, and because the whole inn knew anyway."
    "That night they close the last ledger entry together, both signing their names."
    hide cg onlayer cgl
    call vn_night(7)
    if wom.ending == "close":
        jump wom_ch12_close
    jump wom_ch12_restore

## ---- 12, Close: One Bath -------------------------------------------------------------------------
label wom_ch12_close:
    $ wom.chapter = 12
    $ wom_body(12)
    $ wom.fit = "uniform"
    $ vn_enter(bg="wom_one_bath", pc="proud", pc_tag="wom_pc", cast=[("wom_hazuki", "sly")], cg="wom_one_bath_open")
    "The wall came down this morning, century-old cedar, and the two springs spill into each other for the first time in fifty years. One mixed bath. The lobby's full; Nao is drowning in bookings."
    show cg wom_wall_down onlayer cgl
    "Steam pours through the gap where the wall stood, from both sides at once, and meets in the middle. The guests on the women's side, the first ones in, walk through into the old men's bath with their towels and look round at the cracked tile and the old cedar, and laugh, and get in."
    "Men will come in too. They'll get in this water. Tsubaki thinks about that, about the spring, about the grace period and the ones who need it badly enough, and finds she isn't worried about any of them. It'll do what it does. It always has."
    "In the office Tsubaki opens a fresh ledger and writes {i}Mixed{/i} where the divisions used to be."
    "{color=#ff8a7a}As she writes the first reservation the spring pushes once more, through all of her, and leaves her more than she was: fuller, softer, the red tails heavier.{/color}"
    wom_hazuki "\"I'm claiming the first slot. And after hours, if you're free.\""
    if wom.note6 == "wrote":
        "She's got your note in her coat pocket. You can see the corner of the inn's paper. She pats it."
    else:
        "She doesn't mention the note. She doesn't need to. She can see the corner of it in your uniform pocket, and she smiles at it."
    wom_you "\"The first slot's yours. After hours, we'll see.\""
    wom_hazuki "\"That's a yes.\""
    wom_you "\"That's a we'll see.\""
    "It's a yes."
    hide cg onlayer cgl
    hide wom_hazuki
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_one_bath", pc="begging", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_twelve_iori")
    "After closing, the deserted bath, and Iori in it, in the one big bath with the wall gone and the lanterns of both sides on the water. They make love without one inhibition left between them, in the water that made them."
    show cg wom_twelve_ride onlayer cgl
    "Tsubaki rides her on the old men's-side ledge, where the cracked tile used to be, laughing, her red tails swinging, Iori's hands on her hips, the steam rising off both of them into the cold."
    wom_iori "\"You're heavier.\""
    wom_you "\"It pushed once more. Today. While I was writing the first booking.\""
    wom_iori "\"It does that. For the ones who stay.\""
    wom_you "\"{i}Iori{/i}— more— {i}yes{/i}—!\"" with vnfx("flash", "shake")
    "Then the two of them write the day into the ledger together, and Tsubaki doesn't time anything at all."
    $ vn_feat("One Bath")
    hide cg onlayer cgl
    jump wom_route_return

## ---- 12, Restore (new writing): A Clean Inn ------------------------------------------------------
label wom_ch12_restore:
    $ wom.chapter = 12
    $ wom_body(12)
    $ wom.fit = "uniform"
    $ vn_enter(bg="wom_front_desk", pc="proud", pc_tag="wom_pc", cast=[("wom_nao", "grin")], cg="wom_clean_inn")
    "Spring. Both sides full. The men's side manager waves from his end of the corridor; his ledger is boring, and that's the point."
    "{color=#ff8a7a}As she signs the season's first page the spring pushes once more, through all of her, and leaves her fuller, softer, the red tails heavier.{/color}"
    wom_nao "\"You know you could go back to the men's side now. Help out. If you wanted.\""
    wom_you "\"There's nothing left I'd rather save.\""
    hide cg onlayer cgl
    hide wom_nao
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_private_bath", pc="begging", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_twelve_iori_r")
    "After closing, the private bath, and Iori in it, the cycle broken behind them and nothing broken between them."
    show cg wom_twelve_ride_r onlayer cgl
    "Tsubaki rides her on the cedar edge, laughing, her red tails swinging, Iori's hands on her hips, and through the wall they can hear the men's side, full, somebody singing badly in the bath."
    wom_iori "\"Listen to that. Customers.\""
    wom_you "\"Paying ones. Honest books.\""
    wom_iori "\"And you're still here.\""
    wom_you "\"I'm still here. {i}Iori{/i}— more— {i}yes{/i}—!\"" with vnfx("flash", "shake")
    "Then they write the day in the ledger together, and Tsubaki doesn't time anything at all."
    $ vn_feat("A Clean Inn")
    hide cg onlayer cgl
    jump wom_route_return
