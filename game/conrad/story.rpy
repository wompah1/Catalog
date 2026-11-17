## conrad's seven chapters. Heavier non-con: ch 1-4 forced (Conrad never threatens, never uses the photos; he just
## doesn't stop), ch 5 the flip at the out, ch 6-7 consensual. Every chapter ends mid-act (the package). Denial mode.

## ---- 1. Terms ----------------------------------------------------------------------------------
label cnr_ch1:
    $ cnr.chapter = 1
    $ cnr.fit = "kit"
    $ vn_enter(bg="cnr_flat", pc="smug", pc_tag="cnr_pc", cast=[], cg="cnr_prep")
    "Three hours of prep, and it's craft. The shave, all of it. The tape. The padded bra, the padded shorts, the contour, the lashes. The voice, warmed up in the mirror like a singer."
    "And the rule, once, to the mirror: nothing comes off."
    show screen cnr_book(1)
    "The book. Four men, a year, a car, rent, a bracelet, eleven months of dinners. Not one of them has had so much as a kiss. You're twenty-one and a virgin and extremely pleased with yourself."
    hide screen cnr_book
    hide cg onlayer cgl
    $ vn_enter(bg="cnr_restaurant", pc="smug", pc_tag="cnr_pc", cast=[("cnr_conrad", "amused")], cg="cnr_dinner_terms")
    "Conrad Mercer: forty-seven, old money, unhurried. A whole weekend booked, and you already spent the money."
    cnr_conrad "\"I've always liked a grifter.\""
    "Not a challenge. More like an offer. You give him your lightest, most feathered laugh."
    "He lets you get halfway through the starter before he puts his fork down, with the smallest, oddly precise flick of his hand."
    cnr_conrad "\"Everything on you is a costume and none of it cost anything.\""
    cnr_you "\"I'm sorry?\""
    cnr_conrad "\"I don't want the money back. I'm not going to tell the others. I've done this before. And I'm going to have you made properly.\""
    "That's all. Four sentences. No threat, not even a finality to it: just terms, and he never raises his voice."
    cnr_you "\"I think you've got me confused with someone. I'm—\""
    cnr_conrad "\"Devin.\""
    "Nobody in your book knows that name. Not one of the four. You have never once heard it said out loud across a tablecloth."
    cnr_conrad "\"The bra's a high-street C with the inserts doubled. The hips are foam, from the theatrical shop on Cale Street, the good one. You tape. You sit forward so the tape doesn't pull, which is why your back is so beautifully straight all night. It's very good work. It's the best I've seen.\""
    cnr_you "\"Thank you. I mean, I don't know what you're talking about. I mean—\""
    "You can feel your face doing three things at once. You've practised this face in a mirror for a year and none of the practice covered this."
    cnr_conrad "\"The voice is the best of it. You lose it on your Rs when you're surprised. You've just lost it.\""
    cnr_you "\"If this is a shakedown, I should tell you now, the money's gone. All of it. I'm terrible with money, that's the whole problem with me, you wouldn't get a penny out of—\""
    cnr_conrad "\"I said I don't want it back.\""
    "He picks his fork up again. He eats like a man with nowhere else to be. And you sit with your hands in your lap and do the only thing you've ever been good at, which is sums: what the weekend paid, what you spent it on, what it would cost to stand up now and walk out."
    "The sums come out the same every time you run them. You pick up your fork."
    cnr_conrad "\"Finish your dinner.\""
    hide cg onlayer cgl
    hide cnr_conrad
    $ vn_enter(bg="cnr_hotel", pc="caught", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_lift")
    "You finish your dinner. You don't taste it. You eat every bite of a starter and a main and a dessert you didn't order, because he ordered it, and because walking out means the weekend's money goes back, and you spent it on Tuesday."
    "In the lift he stands beside you with his hands in his pockets, and doesn't touch you, and doesn't say anything, and looks at the two of you in the brass doors: a tall grey man in a good suit, and a girl in a dress you rented, who is twenty-one and a man and a virgin and has never been this frightened of a floor number."
    cnr_you "\"You know the arrangement's dinner. That's the whole arrangement. Dinner and company and a hand on the arm.\""
    cnr_conrad "\"I know what your arrangement is. I've read your book.\""
    "You didn't know he'd read your book."
    cnr_you "\"That's private. That's a private document. How did you even—\""
    cnr_conrad "\"You left it open on your phone beside your plate. Twice. Columns are very easy to read upside down.\""
    "Owed. Paid. A total at the bottom you'd been proud of. You put the phone face down on the brass rail, and it doesn't help at all. The doors open."
    hide cnr_conrad
    jump cnr_first

label cnr_ch1_after:
    hide cg onlayer cgl
    call vn_night(9)
    jump cnr_ch2

## ---- 2. Maintenance ----------------------------------------------------------------------------
label cnr_ch2:
    $ cnr.chapter = 2
    $ cnr.fit = "robe"
    $ vn_enter(bg="cnr_guestroom", pc="caught", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_schedule")
    "Conrad's guest room, and a week of it. A schedule on the nightstand you didn't write: appointments, injections, a clinic that doesn't ask questions."
    cnr_you "\"I didn't book any of these. I'm not going to any of these.\""
    cnr_conrad "\"The car's at nine.\""
    "The car is at nine. You're in it. You tell yourself it's cheaper than being exposed, and nobody's said a word about exposure but you."
    hide cg onlayer cgl
    $ vn_enter(bg="cnr_clinic", pc="caught", pc_tag="cnr_pc", cast=[], cg="cnr_clinic_one")
    "The clinic is a townhouse with no sign, a receptionist who calls you Miss without looking up, and a nurse with cold hands who explains nothing and asks you to say yes before each injection."
    "You say yes. Out loud, each time, because she waits until you do. You tell yourself it's a word, and words are free, and you've been saying yes to men for a year without it costing you anything."
    "She writes each one down."
    "The first is in the hip. The second is a patch she presses flat under your collarbone with her thumb, and holds there, counting under her breath."
    cnr_you "\"What is it? What's in it? I'd like that in writing, actually. I'd like an itemised—\""
    "The nurse looks at you for the first time. Then she turns the clipboard round so you can read it: a column of milligrams in a language you don't speak, with your name at the top. Not your book name. Devin."
    "She waits. You say yes. She writes it down."
    "In the car home you sit with your knees together and your hand over the patch, and the driver doesn't look at you in the mirror once, the whole way."
    hide cg onlayer cgl
    $ vn_enter(bg="cnr_guestroom", pc="caught", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_razor")
    "A week in you reach for the razor out of habit. There's nothing to do with it. The hair isn't coming back."
    cnr_you "\"That's not the point. If I don't keep it up, you don't get an opinion when the costs start running higher. This is—\""
    "Conrad takes the razor out of your hand and drops it in the bin, mid-sentence, while you're arguing about money."
    cnr_conrad "\"Invoice if you must. You don't need it.\""
    "You look down at your shins. Bare, smooth, a week without a blade on them, and you hadn't noticed. You'd been arguing about the price of a thing that had already stopped happening."
    cnr_you "\"That was a good razor. That was a five-blade razor.\""
    cnr_conrad "\"Put it on the book.\""
    hide cnr_conrad
    jump cnr_ready

label cnr_ch2_after:
    hide cg onlayer cgl
    call vn_night(9)
    jump cnr_ch3

## ---- 3. Retiring the Pads -----------------------------------------------------------------------
label cnr_ch3:
    $ cnr.chapter = 3
    $ cnr_body(3)
    $ cnr.fit = "nude"
    $ vn_enter(bg="cnr_bedroom", pc="caught", pc_tag="cnr_pc", cast=[("cnr_conrad", "amused")], cg="cnr_mirror_pads")
    "{color=#e0a0a0}Tender, then real. Inside a week your chest has outgrown the padded cups.{/color}"
    cnr_conrad "\"Off.\""
    "He doesn't look up from his phone. Conrad has you strip the kit in front of the long mirror, and takes the pads out of your hands and drops them in the bin, talking about something else entirely."
    cnr_conrad "\"The lemons came bruised again. No need to keep that grocer.\""
    menu:
        "The pads, in the bin."
        "Complain about the cost":
            $ cnr.gripe = "cost"
            cnr_you "\"Those were silicone! Do you know what those cost?\""
        "Complain about the dinners":
            $ cnr.gripe = "dinners"
            cnr_you "\"I've got Marcus on Thursday! What am I supposed to wear to Marcus?\""
    cnr_conrad "\"Try a T-shirt if you want to see what it looks like. Or go without. You'll pass. Nothing padded at dinner. Nothing but you under the dress.\""
    "He puts the phone down, finally, and comes to stand behind you at the mirror. He doesn't touch at first. He looks, the way he looked at the menu that first night: all the way down, slowly, and back up."
    cnr_conrad "\"Hands down.\""
    cnr_you "\"It's cold in here. That's all that is. It's cold.\""
    "He cups them from behind, one in each hand, and weighs them, and your nipples go hard so fast in his palms that you have to watch it happen in the glass."
    cnr_you "\"{i}Hahh{/i}— don't— they're tender— I never agreed to an inspection—\""
    cnr_conrad "\"Real. Both of them. Say it.\""
    cnr_you "\"No.\""
    "His thumbs go round, slow. You last nine seconds."
    cnr_you "\"{i}Ahh{/i}— real— they're real— fine— they're {i}real{/i}, are you happy—\""
    cnr_conrad "\"Very.\""
    hide cg onlayer cgl
    $ cnr.fit = "dress"
    $ vn_enter(bg="cnr_restaurant", pc="smug", pc_tag="cnr_pc", cast=[("cnr_marcus", "loud")], cg="cnr_dinner_marcus")
    "Dinner with Marcus on the Thursday, nothing padded under the dress. Nobody notices. He pays more for a hand on the arm than you've ever been paid for anything."
    cnr_marcus "\"Such company is worth the price of admission!\""
    "Nothing comes off, you think, smiling at Marcus. Not for him."
    hide cg onlayer cgl
    hide cnr_marcus
    $ vn_enter(bg="cnr_restaurant", pc="smug", pc_tag="cnr_pc", cast=[("cnr_chloe", "cackle")], cg="cnr_chloe_loo")
    "In the ladies', between courses, you ring Chloe with your back against the door."
    cnr_chloe "\"Well? Has the old one found you out yet?\""
    cnr_you "\"No. Everything's fine. Everything's completely under control. I'm— I've got new tits, Chlo.\""
    "There's a long silence on the line, and then the loudest laugh you've ever heard down a phone, and you have to hold it away from your ear."
    cnr_chloe "\"Real ones?\""
    cnr_you "\"It's leverage.\""
    cnr_chloe "\"Babe. It's tits.\""
    hide cg onlayer cgl
    hide cnr_chloe
    $ vn_enter(bg="cnr_restaurant", pc="smug", pc_tag="cnr_pc", cast=[("cnr_neil", "soft")], cg="cnr_dinner_neil")
    "Neil, on the Friday, at the little Italian place he always picks because the owner knows him by name. Neil is the gentle one. Neil paid for Barcelona and never once asked to share the room."
    cnr_neil "\"You look different, darling. Have you done something?\""
    cnr_you "\"New dress.\""
    cnr_neil "\"No, it's— you look well. You look happy. It suits you.\""
    "He means it. That's the trouble with Neil: he always means it. You've never once felt bad about Neil's money, and you feel bad now, with nothing padded under the dress and his eyes kept politely on your face."
    cnr_neil "\"If you ever fancied going away again, you've only to say. Somewhere warm.\""
    cnr_you "\"Mm. I'll check the diary.\""
    "You check it under the table. There's a line in it you didn't write, in a hand that isn't yours: the clinic, Monday, nine. Conrad's."
    hide cg onlayer cgl
    hide cnr_neil
    jump cnr_titjob

label cnr_ch3_after:
    hide cg onlayer cgl
    call vn_night(9)
    jump cnr_ch4

## ---- 4. Tuck -----------------------------------------------------------------------------------
label cnr_ch4:
    $ cnr.chapter = 4
    $ cnr_body(4)
    $ cnr.fit = "robe"
    $ vn_enter(bg="cnr_bedroom", pc="caught", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_wardrobe")
    "{color=#e0a0a0}The tape's stopped being necessary. You keep using it out of habit. Your cock is small and getting smaller and nobody talks about it. Your ass and thighs have run up so hard the padded shorts don't go on, and nothing in the wardrobe closes.{/color}"
    cnr_conrad "\"So. Still taping it down?\""
    cnr_you "\"I don't see you bringing replacement tech.\""
    cnr_conrad "\"If you're going to keep locking things away, we might as well use something meant for the job. You won't be needing that.\""
    "You stand in his walk-in wardrobe with three dresses on the floor round your ankles, none of which zip over the new hips, and a pair of jeans you got as far as your thighs, and you are, genuinely, about to lose your temper about money, which you've never done in your life, and you stop yourself, because losing your temper is a cost and you don't pay costs."
    "Conrad takes the battered roll of tape off the dresser and drops it in the bin. From his jacket he takes a small steel cage."
    cnr_you "\"No. Absolutely not. Not that. I'm not wearing that.\""
    jump cnr_device

label cnr_ch4_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump cnr_ch5

## ---- 5. The Out --------------------------------------------------------------------------------
label cnr_ch5:
    $ cnr.chapter = 5
    $ cnr_body(5)
    $ cnr.fit = "robe"
    $ vn_enter(bg="cnr_bedroom", pc="flushed", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_woken")
    "{color=#e0a0a0}Your face has softened. The voice isn't something you put on any more: you answer the phone in it half asleep.{/color}"
    "Last night you told him, half asleep, to wake you for it: first thing, don't knock, consider it pre-approved. You don't remember saying it. Conrad wakes you for it. You're still saying no out of habit. Twice before lunch, over the arm of a chair, against the bathroom counter."
    cnr_you "\"You're ruining these sheets. Cleaning fee's above the line item—\""
    "He doesn't answer. He's behind you on his side, slow, the way you apparently asked for it, and you're the one who pushes back onto him."
    cnr_you "\"{i}Mmh{/i}— no— it's {i}early{/i}— it's not even— {i}ahh{/i}— okay— okay, {i}there{/i}— right there—\""
    "Your phone buzzes on the nightstand. Marcus. You answer without opening your eyes. \"Mm, hi, you.\" It comes out soft and sleep-rough, the exact voice you used to put on."
    cnr_conrad "\"Tell him you're busy.\""
    cnr_you "\"I'm— {i}hahh{/i}— I'm a bit busy, babe— can I ring you— {i}nnh{/i}— can I ring you back—\""
    "Marcus says of course, of course, sweetheart, and you hang up on him mid-word and come with the phone still in your hand, loud enough that he'd have heard it if you'd been a second slower."
    "You throw the last of the contour away yourself, and don't remark on it."
    show cg cnr_counter onlayer cgl
    "Before lunch he bends you over the bathroom counter, the robe pushed up, your hands flat either side of the sink, the mirror right there in front of you, and he makes you watch."
    cnr_conrad "\"Look up.\""
    cnr_you "\"I am looking— {i}ahh{/i}— I'm looking— don't make me— {i}hahh{/i}— oh god, that's my {i}face{/i}—\""
    "It's a girl's face. Flushed and soft, mouth open, a girl getting fucked over a sink and loving every second of it, and you can't make it be anybody else's."
    cnr_you "\"{i}Ahh{/i}— {i}AHH{/i}— don't stop— don't you {i}dare{/i} stop— {i}harder{/i}—!\"" with vnfx("shake")
    "He doesn't stop. After, he kisses the back of your neck and leaves you there, and you stay bent over the counter with your cheek on the cold marble until your breathing comes back."
    show cg cnr_mirror_voice onlayer cgl
    "In the bathroom mirror, afterwards, you try the old voice, the real one, the one you used to drop back into in the car on the way home. \"Right. Okay. Book.\" It comes out soft. You try it lower. It comes out soft and lower."
    "You look at the face that goes with it for a long time. You'd have charged that face double, a year ago. You'd have charged it triple."
    hide cg onlayer cgl
    $ cnr.fit = "nude"
    $ vn_enter(bg="cnr_study", pc="flushed", pc_tag="cnr_pc", cast=[("cnr_conrad", "unhurried")], cg="cnr_desk")
    "His study, a call you aren't allowed to interrupt, and you under the desk because he pointed there."
    cnr_conrad "\"You're not interrupting this call.\""
    "You keep quiet only while the call runs."
    "It's a long call. Shipping, or property, or something with a great many numbers in it. His hand rests on the back of your head, not pressing, only resting, the way it did the first night, and you work him slowly with your mouth and listen to him read out figures in the same voice he uses to tell you to breathe."
    "You could stop. You notice that you could. Nothing is holding you there but a hand that isn't holding."
    "You don't stop. Twice his voice catches on a number, and both times you're absurdly, ferociously proud of it."
    "The call ends. You're still between his knees."
    "Then he takes out his phone, and in front of you, without a word, deletes the photos. Every one."
    cnr_conrad "\"It's finished. Keep the body. Keep the gifts. There's a payout, if you want it. You can walk.\""
    "The out. Nobody was making you do any of it, and nobody says so."
    show screen cnr_book(5)
    "Four reasons to stay, all in one paragraph, none of them true."
    hide screen cnr_book
    menu:
        "The first excuse."
        "\"The other three would find out\"":
            $ cnr.excuse = "three"
            cnr_you "\"The other three would find out. They'd see me. I can't go back out like this, I'd have to explain, it's leverage, it's—\""
        "\"The clinic isn't finished\"":
            $ cnr.excuse = "clinic"
            cnr_you "\"The clinic isn't finished. You can't leave a job half done, that's— that's just bad business—\""
    if cnr.excuse == "three":
        cnr_you "\"And the clinic isn't finished. You can't leave a job half done. And the flat's in my book name, the lease, I can't just— and Chloe. Chloe would never let me hear the end of it. That's four. That's four reasons.\""
    else:
        cnr_you "\"And the other three would find out. They'd see me. And the flat's in my book name, the lease, I can't just— and Chloe. Chloe would never let me hear the end of it. That's four. That's four reasons.\""
    "You say all four fast, in a row, the way you used to read the book back to yourself in the car, and he listens to every one with his hands folded and doesn't argue with a single one of them."
    cnr_conrad "\"Those are very good reasons.\""
    cnr_you "\"They're excellent reasons.\""
    cnr_conrad "\"None of them is why you're still on the floor.\""
    "No. None of them is."
    "You turn down the payout. The first money you have ever turned down. Then you climb into his lap, and ask."
    $ cnr.asked = True
    jump cnr_lap

label cnr_ch5_after:
    hide cg onlayer cgl
    call vn_night(9)
    jump cnr_ch6

## ---- 6. Nothing Comes Off ----------------------------------------------------------------------
label cnr_ch6:
    $ cnr.chapter = 6
    $ cnr.fit = "robe"
    $ vn_enter(bg="cnr_clinic", pc="greedy", pc_tag="cnr_pc", cast=[], cg="cnr_clinic_yes")
    "The clinic. You say yes, out loud, at the desk. The procedure itself is brief and happens somewhere else."
    show cg cnr_chloe_clinic onlayer cgl
    "Chloe drives you. She doesn't ask. She sits in the waiting room with a magazine upside down and her foot jiggling, and when they call you she grabs your hand and squeezes it once, hard, and lets go."
    show cnr_chloe cackle at vn_cast_slot
    cnr_chloe "\"You know you can still say no, right? To this one. Of all of them.\""
    cnr_you "\"It's just the last line item.\""
    show cnr_chloe cackle at vn_cast_slot
    cnr_chloe "\"Babe.\""
    cnr_you "\"Yes. I'm saying yes. Out loud. Look.\""
    "You say it to the nurse at the door. Chloe watches you say it, and puts her magazine down, the right way up, and nods."
    hide cg onlayer cgl
    $ vn_clock.day += 6
    $ cnr_body(6)
    $ cnr.fit = "nude"
    $ vn_enter(bg="cnr_bedroom", pc="greedy", pc_tag="cnr_pc", cast=[("cnr_conrad", "amused")], cg="cnr_end_state")
    "{color=#e0a0a0}A week of Conrad's house afterwards. Your chest at its largest, ass and thighs at their thickest. Your cock gone, and in its place, finally, a pussy.{/color}"
    "The old rule isn't restated. There's nothing left to hide. The book isn't opened once."
    show cg cnr_discovery onlayer cgl
    "The first morning you're allowed to, you lock the bathroom door, which you've never once done in this house, and sit on the edge of the bath with your knees apart and a hand mirror, and look."
    "It's yours. It's very obviously yours. You touch it the way you'd check a new phone for scratches, careful, one fingertip, and it's warm and soft and already wet, and you make a sound that comes back off every tile in the room."
    cnr_you "\"{i}Oh{/i}. Oh. Oh, that's— {i}ohh{/i}— that's not fair— that is {i}not{/i} fair—\""
    "You find the place he's going to find. You find it in about a minute, and then you can't stop finding it, and you come on the edge of the bath with your heel skidding on the mat and your own voice ringing back at you, high and loud and nothing like a man's."
    cnr_you "\"{i}Ahh{/i}— {i}AHH{/i}— oh my god— oh my {i}god{/i}—!\"" with vnfx("flash", "shake")
    "When you unlock the door he's sitting on the end of the bed with a cup of coffee. He doesn't say anything. Neither do you. You go red from your collarbones to your hairline, and he drinks his coffee."
    hide cg onlayer cgl
    jump cnr_first_vaginal

label cnr_ch6_after:
    hide cg onlayer cgl
    call vn_night(9)
    jump cnr_ch7

## ---- 7. What You Paid For ----------------------------------------------------------------------
label cnr_ch7:
    $ cnr.chapter = 7
    $ cnr.fit = "dress"
    $ vn_enter(bg="cnr_suite", pc="flushed", pc_tag="cnr_pc", cast=[("cnr_chloe", "cackle")], cg="cnr_suite_confess")
    "A hotel suite. Marcus, Terrence and Neil, who've paid for a year and got a hand on the arm. Chloe, who's known all along. Conrad in the corner chair, touching nobody. He said one thing at the door: \"It's your party.\""
    hide cnr_chloe
    show cnr_marcus loud at vn_cast_slot
    cnr_marcus "\"So what's the deal? This the afterparty we've all been accidentally paying for?\""
    "You arranged all of it. Nobody made you."
    "The suite has a bar and a view of the river and a bed the size of your old flat. You booked it on Conrad's card, with his blessing, and spent an hour choosing a dress that says nothing, because for once in your life you don't want the dress doing the talking."
    "Terrence keeps checking his phone, as if there's been a mistake with the address. Neil has brought flowers, because Neil always brings flowers. Marcus has already opened the champagne."
    show screen cnr_book(7)
    "You open the book, and tell them what you took and what you were when you took it. It comes out as begging."
    hide screen cnr_book
    cnr_you "\"I owe you. I took eleven months off you, Marcus. Let me clear it. I can take all three at once. Please let me settle up.\""
    hide cnr_chloe
    show cnr_terrence eager at vn_cast_slot
    cnr_terrence "\"Wait, what? What is this, a kink thing?\""
    hide cnr_chloe
    show cnr_marcus loud at vn_cast_slot
    cnr_marcus "\"Nice try. Stop messing about, sweetheart. Nothing's that free.\""
    hide cnr_chloe
    show cnr_neil soft at vn_cast_slot
    cnr_neil "\"You don't owe us a thing, darling. You never took a bit we didn't offer you.\""
    "Nobody believes you. There's nothing left to see. You end up on your knees arguing for your own guilt."
    cnr_you "\"You think I made it all up? You think you paid a year for {i}this{/i} body?\""
    hide cnr_marcus
    hide cnr_neil
    hide cnr_terrence
    show cnr_chloe cackle at vn_cast_slot
    cnr_chloe "\"Oh, it's true. He's been a liar since before I met him and this is the first honest thing he's ever offered you. He wasn't your girl. He was my idiot. I've known for a year. It's the funniest thing that's ever happened to anybody.\""
    "Marcus starts laughing. Then everybody is."
    "It's the kind of laugh that goes round a room twice. Terrence laughs because Marcus is. Neil laughs into his hand, apologising between breaths. Chloe is bent double over the arm of the sofa."
    cnr_you "\"It's not funny. It's a {i}debt{/i}. I am being extremely serious about the debt.\""
    hide cnr_chloe
    show cnr_marcus loud at vn_cast_slot
    cnr_marcus "\"Sweetheart. If you're this serious about it, who am I to turn down a payment?\""
    hide cg onlayer cgl
    hide cnr_marcus
    jump cnr_collection
