## curve's six chapters. IT HAS TO BIND: coercion first to last, no flip. Each chapter: a row crossed off, one
## dominant act, one escalation, a gag, the probe. Never assert a mind change in narration.

## ---- 1. Intake -----------------------------------------------------------------------------------
label crv_ch1:
    $ crv.chapter = 1
    $ crv.fit = "hoodie"
    $ vn_enter(bg="crv_lab", pc="flat", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_folder")
    "Nine at night, an empty teaching lab, and Greer Halloway on the other side of a bench with a folder she hasn't opened and doesn't need to."
    "You copied her lab set. That's why she's the one holding it. You did it, and there's no version of tonight where you didn't."
    crv_greer "\"She isn't filing it.\""
    "She talks about herself in the third person, and about you, as if you were both rows on a form."
    crv_greer "\"If the department handles it, her project loses grant status. If her project dies, her whole panel dies. She needs this seat filled. Protocol-compliant, all term, every row, no exceptions. She will teach him, her way. He will pass, her way.\""
    crv_you "\"Her way meaning what?\""
    "She doesn't answer. She nods at the whiteboard behind her, and lets you read it."
    show screen crv_board(0)
    "Your name at the top. A hypothesis line under it. Eleven rows, dated, abbreviated past the point you can parse."
    hide screen crv_board
    crv_greer "\"The protocol operates under two rules. One: the vector is hers, and it binds only during orgasm. Dose without arousal does nothing. Arousal without dose does nothing. Two: dosed, he retains everything he reads until it clears.\""
    crv_greer "\"He keeps to her schedule. She does not keep to his.\""
    "That's all the explanation you get. She sets a glass on the bench, and a laboratory timer beside it."
    crv_you "\"Absolutely not. Whatever that is. No.\""
    crv_greer "\"The folder's in my desk.\""
    hide cg onlayer cgl
    jump crv_first_dose

label crv_ch1_after:
    hide cg onlayer cgl
    $ crv.fit = "hoodie"
    $ vn_enter(bg="crv_lab", pc="dazed", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_forty_pages")
    crv_greer "\"Redress. He'll want this.\""
    "A blue folder in her handwriting: the first forty pages of organic chemistry. You read them, and you keep all of it. Every mechanism. Every arrow."
    "That lands harder than anything she's done to you tonight."
    crv_greer "\"He'll want to go home now.\""
    show screen crv_probe(1)
    crv_greer "\"What are you carrying?\""
    crv_you "\"Fifteen. Why?\""
    hide screen crv_probe
    crv_you "\"This is over at the end of the semester.\""
    "She doesn't respond. You say it again at the door. She doesn't respond to that either."
    crv_you "\"...Thanks.\""
    "You don't know why you said it. She writes it down."
    hide cg onlayer cgl
    hide crv_greer
    $ vn_enter(bg="crv_dorm", pc="dazed", pc_tag="crv_pc", cast=[], cg="crv_dorm_read")
    "In your dorm room at two in the morning you sit up in bed with the blue folder on your knees and read it again, to check, and you don't need to. It's all there. Every mechanism, every arrow, every footnote she wrote in the margin in her tiny upright hand."
    "You close your eyes and turn the pages in your head. Page nineteen, the second diagram. Page thirty-one, the bit she underlined twice. It's like having a library you didn't build."
    "You lie awake till four with your hand over your mouth, which still tastes of her, trying to work out which part of tonight you're most ashamed of. It isn't the part you'd have guessed."
    $ vn_clock.day += 6
    call vn_night(7)
    jump crv_ch2

## ---- 2. Regimen ----------------------------------------------------------------------------------
label crv_ch2:
    $ crv.chapter = 2
    $ crv.fit = "hoodie"
    $ vn_enter(bg="crv_lab", pc="flat", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_regimen")
    show screen crv_board(1)
    "She crosses off COMPLIANCE and moves to the next row. Two days ago you aced a quiz off one hour of reading."
    hide screen crv_board
    crv_greer "\"Regimen. Twelve weeks. Begins today. Sleep: eleven to six. No caffeine after four. No screens in bed. Diet: no fast food, no sugar, including 'healthy' breakfast bars. Wardrobe: a plain t-shirt and sweatpants, clean, unbranded. No hats, no hoodies, no logos. Socks if you must.\""
    crv_you "\"You're going to police my socks?\""
    crv_greer "\"Question: socks.\" She writes it down. \"Noted.\""
    crv_you "\"You're not my mum.\""
    crv_greer "\"Resistance to nutritional protocol. Noted. Rephrased: non-compliance resets the schedule. Your call.\""
    menu:
        "The regimen, read aloud."
        "Argue the sleep schedule":
            $ crv.term = "sleep"
            crv_you "\"I'm not going to bed at ten. I'm twenty-one.\""
            crv_greer "\"Ten.\""
        "Argue the wardrobe":
            $ crv.term = "wardrobe"
            crv_you "\"You don't get to pick my clothes.\""
            crv_greer "\"Soft fabrics. The list's on your door.\""
    "You lose. You argue the next one and lose that too. She doesn't debate; she restates."
    crv_greer "\"Noted: negotiation attempt via tone. Not effective.\""
    crv_you "\"I'm not shaving my head.\""
    crv_greer "\"Hair code's not on the regimen. He keeps his hair, unless retention slips.\""
    crv_you "\"One thing. One. My— it stays. Whatever this does. That stays.\""
    "She walks to the board, reads down it with one finger, and turns back."
    crv_greer "\"It isn't on there.\""
    "It isn't. You check twice. It's the only term you win, and you hold on to it."
    $ crv_body(2)
    $ crv.fit = "regimen"
    $ vn_enter(bg="crv_study", pc="flat", pc_tag="crv_pc", cast=[("crv_nadia", "bright")], cg="crv_nadia_study")
    "{color=#e89a8a}Your skin's gone smooth. The hair on your arms is thinning. Your face is softer in the mirror, your waist too, and your hair's grown out past your collar without you noticing it go. The supplement stack, you figure. And sleeping properly for the first time in two years.{/color}"
    crv_nadia "\"Your skin looks amazing, by the way. What are you using?\""
    crv_you "\"Oh, thanks.\""
    "You say it before you've worked out why it's alarming. Across the room Greer is lovely to Nadia for ninety seconds, laughing, generous, a smile she hasn't shown you once."
    hide crv_nadia
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"Nadia, hi! You got that seminar spot? Good. Leave your draft, I'll look tonight.\""
    "Nadia goes pink and waves at you on her way out. The second the door shuts the air cools."
    hide crv_nadia
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"Regimen finalised. No negotiation. Lab. Now.\""
    hide cg onlayer cgl
    hide crv_nadia
    jump crv_first_mouth

label crv_ch2_after:
    hide cg onlayer cgl
    show screen crv_probe(2)
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"What are you carrying?\""
    crv_you "\"Fifteen. And the Tuesday-Thursday dose, and the Sunday double.\""
    hide screen crv_probe
    "You don't notice you added the second part. She does."
    $ vn_enter(bg="crv_exam", pc="flat", pc_tag="crv_pc", cast=[], cg="crv_quiz")
    "The quiz on Friday. You turn it over and the answers are just there, laid out in your head in her handwriting, and you write them down and you're done in eleven minutes and you sit there for the other forty with your pen in your mouth, terrified."
    "It comes back with a hundred on it. Nobody in the business school has ever got a hundred on anything. The lecturer writes {i}see me{/i} on it, and when you go, he only wants to know your study method."
    crv_you "\"Flashcards.\""
    "He writes that down too."
    hide cg onlayer cgl
    $ vn_clock.day += 13
    call vn_night(7)
    jump crv_ch3

## ---- 3. Roster -----------------------------------------------------------------------------------
label crv_ch3:
    $ crv.chapter = 3
    $ crv_body(3)
    $ crv.fit = "regimen"
    $ vn_enter(bg="crv_dorm", pc="flustered", pc_tag="crv_pc", cast=[], cg="crv_blonde")
    "{color=#e89a8a}Your hair's gone blonde, strawberry blonde, a colour you've never been. Your voice slips up mid-sentence. Your hands look like someone else's. Your hips have a sway you have to work around.{/color}"
    "You're cutting weight, you tell people. You tell people that for months."
    hide cg onlayer cgl
    $ vn_enter(bg="crv_lab", pc="flustered", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_callie_folder")
    show screen crv_board(3)
    "PRESENTATION; ROSTER AMD. is crossed off before you get there. She's already filed it. She tells you after."
    hide screen crv_board
    crv_greer "\"You're five minutes early. Good. Need extra time for the new protocol.\""
    crv_you "\"What is it? The stuff. What am I actually drinking?\""
    crv_greer "\"Mine. Pharmacological vector. Retention only binds during orgasm. Dosage standard.\""
    "No drama. She had no reason to hide it and never did. Midterms are in nine days. You keep drinking it."
    crv_you "\"I'm walking. I'll take the expulsion. I'm done.\""
    "She slides a second folder across. Your registration, amended. The class roster. Your ID photo. An enrolment marker. All filed as accommodations, on your behalf, in her name. CALLIE BOYD."
    crv_you "\"You— filed this? You didn't even tell me.\""
    crv_greer "\"He missed no authorised communication window. Notification after the fact is protocol nine-B. Registration, roster, ID photo, core systems, the athletics directory. All defensible under accommodation policy.\""
    "The photo has a soft jaw, surprisingly big eyes, hair just at the shoulder. You shut the folder."
    crv_you "\"You just... did all this.\""
    crv_greer "\"I did. For data. He's welcome to leave. That's what walks out with him.\""
    "It's not a threat. She's showing you a folder."
    jump crv_first_bench

label crv_ch3_after:
    hide cg onlayer cgl
    show screen crv_probe(3)
    crv_greer "\"What are you carrying?\""
    crv_you "\"Thursday's dose. And, uh. Fifteen.\""
    hide screen crv_probe
    "End of the year, you think, in one clause, and keep going."
    $ vn_enter(bg="crv_lab", pc="dazed", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_good_work")
    crv_greer "\"Good work, Callie.\""
    "Once. Warm, peeking through for the first time, certain and soft and almost affectionate. On her way out. It hits harder than everything else this week put together."
    hide crv_greer
    $ vn_clock.day += 13
    call vn_night(7)
    jump crv_ch4

## ---- 4. Baseline ---------------------------------------------------------------------------------
label crv_ch4:
    $ crv.chapter = 4
    $ crv.fit = "regimen"
    $ vn_enter(bg="crv_lab", pc="flat", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_baseline")
    show screen crv_board(6)
    crv_greer "\"Step nine. I need clean baseline data before I escalate. Seventy-two hours, nothing.\""
    hide screen crv_board
    "Not a punishment. She says so. And then, in the small hours, so you can't say she didn't tell you, a text: {i}Subject: protocol nine, baseline withdrawal for seventy-two hours, effective now. No exceptions, Cal. GH.{/i}"
    hide crv_greer
    $ vn_until(23)
    $ vn_enter(bg="crv_dorm", pc="flustered", pc_tag="crv_pc", cast=[], cg="crv_taper")
    "By the first night you can't hold a page. You read a paragraph and it's gone before the full stop. You start sentences and lose them in the middle."
    "And the other half: empty, restless, hard and staying hard, a need that sits in you and won't go anywhere."
    jump crv_hand

label crv_ch4_dean:
    hide cg onlayer cgl
    $ vn_clock.day += 1
    $ vn_until(11)
    $ crv.fit = "regimen"
    $ vn_enter(bg="crv_dean", pc="dazed", pc_tag="crv_pc", cast=[("crv_kwan", "kind")], cg="crv_kwan_desk")
    "The dean's office. You're going to tell someone. You've rehearsed it all the way across campus."
    crv_kwan "\"Oh, hi there, hon. You all right? You look a bit flushed. Take a seat, let's see how we can help.\""
    crv_you "\"This isn't the bursar's, right?\""
    crv_kwan "\"No, darling, this is the dean's admin. Okay, sweetheart, you're not in trouble. Take your time. What's happened?\""
    menu:
        "What you came to say."
        "Try to say \"drug\"":
            $ crv.dean = "drug"
            crv_you "\"She's— there's a— I'm being given a— the thing you take, for— a… what's the word—\""
        "Try to say \"Greer\"":
            $ crv.dean = "greer"
            crv_you "\"Greer. Greer Halloway is— she's— I was going to— which office is this?\""
    "You lose the thread three times. You can't remember which office you're in. Marjorie Kwan is kind about all of it, and misreads every word."
    crv_kwan "\"Sometimes these things happen at busy times of year, hon. You've got a project advisor, right? Let's see. Halloway, Greer?\""
    "She's already punching it into an app. She takes your elbow and walks you, kind and brisk and sure, all the way back across the quad."
    $ vn_enter(bg="crv_lab", pc="dazed", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_walked_back")
    crv_greer "\"Ms Kwan, you're early. Has something happened?\""
    hide crv_greer
    show crv_kwan kind at vn_cast_slot
    crv_kwan "\"Thank you for taking such good care of him. Really. Just bringing you your lab partner. I think he— she?— could use a break.\""
    hide crv_kwan
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"Of course.\""
    hide crv_greer
    show crv_kwan kind at vn_cast_slot
    crv_kwan "\"You're in very good hands. Feel better, darling.\""
    "The door closes, and Greer writes the whole incident down."
    hide cg onlayer cgl
    jump crv_begging

label crv_ch4_after:
    hide cg onlayer cgl
    $ crv_body(4)
    $ crv.fit = "regimen"
    $ vn_enter(bg="crv_dorm", pc="dazed", pc_tag="crv_pc", cast=[], cg="crv_chest_real")
    "{color=#e89a8a}Your chest prickles the next morning, tender under the t-shirt. Then, by the end of the week, it's real.{/color}"
    show screen crv_probe(4)
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"What are you carrying?\""
    crv_you "\"I'm... carrying. I was going to say. What was the—\""
    hide screen crv_probe
    "She writes that down. The floor's measurably higher. She notes the number and doesn't share it."
    "You buy a bra in the campus shop on Thursday, a plain grey sports one, and tell the girl at the till it's for your sister, and she says it's a great colour for her, and you go back to your room and put it on and look in the mirror for a long time."
    "It fits. The girl at the till was right. It's a great colour."
    "There's no end date this week. You don't have one."
    hide crv_greer
    $ vn_clock.day += 13
    call vn_night(7)
    jump crv_ch5

## ---- 5. Tolerance --------------------------------------------------------------------------------
label crv_ch5:
    $ crv.chapter = 5
    $ crv_pc_name = "Callie"
    $ crv_body(5)
    $ crv.fit = "sweater"
    $ vn_enter(bg="crv_lab", pc="flat", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_chart")
    "{color=#e89a8a}The chest is full now; the cardigan doesn't close over it. Her ass, her thighs, the whole silhouette. And the cock smaller, softer, quiet, not reliable any more.{/color}"
    "A text at midnight: {i}Escalation phase begins: one in twenty-four minimum, increased as tolerated. Compliance review scheduled one hour from now.{/i}"
    "Greer has a chart. The supply line goes one way and the demand line goes the other."
    crv_greer "\"You require more dose per hour than I am physically able to produce. Even with hydration and caloric support, output is insufficient.\""
    hide cg onlayer cgl
    show screen crv_board(9, True)
    "There are rows on the board that weren't there in the first week. Wine-coloured ink, cheap marker from the campus bookshop. No dates. No protocol numbers."
    menu:
        "The new rows."
        "Read them out loud":
            $ crv.rows = "read"
            crv_you "\"Soft. Nadia, no. Keeps the... and—\""
            "You get to the last one and don't read it."
        "Look away":
            $ crv.rows = "away"
            "You look at it once. One of them is the cock. You look away."
    hide screen crv_board
    "Nobody says anything about it."
    $ vn_enter(bg="crv_study", pc="flat", pc_tag="crv_pc", cast=[("crv_greer", "jealous")], cg="crv_jealous")
    "In the study room Nadia bounces in, highlighters tangled in her ponytail, squeezes your arm and says the cardigan suits you."
    crv_greer "\"Nadia, hey! You never sleep, do you?\""
    "Warm, instantly. And then her hand closes on your thigh under the table, iron, an anchor and a shield, and the warmth curdles."
    crv_greer "\"Nadia, prioritise the review after I've cleared this. No exceptions.\""
    hide crv_greer
    show crv_nadia bright at vn_cast_slot
    crv_nadia "\"Did not mean to crash your... whatever this is! You two are adorable.\""
    "She gives you fingers crossed on her way out: the international sign for {i}good luck surviving{/i}. It's the first thing Greer's done all year that isn't on the board."
    hide crv_nadia
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"If you'd like to keep your enrolment—\""
    "You're already packing your bag before she finishes the sentence. Neither of you mentions that she didn't need to say it."
    hide cg onlayer cgl
    hide crv_greer
    jump crv_nightly

label crv_ch5_after:
    hide cg onlayer cgl
    show screen crv_probe(5)
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"What are you carrying?\""
    crv_you "\"Full dose. Latest in just after midnight. Next one midnight, unless you text.\""
    hide screen crv_probe
    show cg crv_paper onlayer cgl
    "She hands you a sheet of thick, formal paper."
    show crv_greer clinical at vn_cast_slot
    crv_greer "\"Paper trail. For when you graduate. The plan is mapped twelve months out. You'll want to keep your records straight.\""
    "Classes don't come up. It doesn't bother her at all."
    "When she graduates, you think. That's when this ends. When she graduates."
    $ vn_clock.day += 13
    call vn_night(7)
    jump crv_ch6

## ---- 6. Full Marks -------------------------------------------------------------------------------
label crv_ch6:
    $ crv.chapter = 6
    $ crv.fit = "sweater"
    $ vn_enter(bg="crv_lab", pc="dazed", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_efficiency")
    "Finals week. Greer has an answer, and a chart, and she delivers it once."
    crv_greer "\"Your current protocol is unsustainable. Output can't meet demand. Efficiency fix: demand scales with mass. Maleness costs more to keep than to lose. If we reduce what there is to maintain, you'll need less, and I won't have to push you as hard. It's a win for both of us. See?\""
    "She isn't lying. The maths is right."
    crv_greer "\"Protocol sixteen. It's scheduled. Three nights.\""
    hide cg onlayer cgl
    jump crv_removal

label crv_ch6_after:
    hide cg onlayer cgl
    $ crv.fit = "sweater"
    $ vn_enter(bg="crv_exam", pc="glowing", pc_tag="crv_pc", cast=[], cg="crv_transcript")
    "Nadia hugs you outside the exam hall before the grades are even posted. \"God, you look so good, Callie! You did it, huh?\""
    "The results go up. Top of the curve. A four-point-oh. Everything she promised, in the first week, across a lab bench, and she delivered it, every row."
    hide cg onlayer cgl
    $ vn_enter(bg="crv_lab", pc="glowing", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_wiped")
    "Greer wipes the board. All eleven rows, the four undated ones, the hypothesis line, the name at the top. Nobody comments."
    "She wipes it slowly, row by row, the way you'd erase a sum you'd finished, and when she gets to your name at the top she stops with the cloth on it for a second, and then wipes that too, and the board's white, and she puts the marker down."
    crv_greer "\"Hypothesis.\""
    crv_you "\"Confirmed?\""
    crv_greer "\"Withdrawn. The underperformance wasn't male cognition. It was retention. I had it backwards. I'll write that up.\""
    "She says it to the board, not to you. It's the first time you've ever heard her be wrong about anything, and she sounds almost pleased about it."
    "Then finals are over, and there's no more coursework to hold, and something in your chest goes very quiet and very frightened. Not about your body. About the empty."
    crv_you "\"Can I— do you think— can I apply for a master's?\""
    "She opens a drawer. The application's already printed."
    crv_greer "\"I printed this last week. It's ready when you are. Full ride. My partner again.\""
    show screen crv_probe(6)
    crv_greer "\"What are you carrying?\""
    crv_you "\"Yours.\""
    hide screen crv_probe
    hide cg onlayer cgl
    $ crv.ending = "yours"
    $ vn_feat("Full Marks")
    jump crv_route_return
