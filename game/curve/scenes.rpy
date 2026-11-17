## curve's sessions. IT HAS TO BIND: one dominant act a chapter, coerced, clinical then not. Cal protests out
## loud through ch 3; from ch 4 the begging is his, rendered as reaction, never as a decision. Greer never
## raises her voice. Anal and oral only until the back half of ch 6.

## ---- ch 1: the first dose. A glass, her hand, a stopwatch ------------------------------------------
label crv_first_dose:
    $ vn_enter(bg="crv_lab", pc="flustered", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_glass")
    "She fills the glass behind the bench, efficiently, without looking at you. It's warm. It's hers. You know exactly what it is."
    crv_greer "\"First dose. Consumption is oral, with ejaculate as vector. Binding requires simultaneity. Trousers round knees. Shirt up. He stands where she puts him, hands at sides.\""
    menu:
        "The glass, and her hand on your belt."
        "Refuse":
            $ crv.shout1 = "refuse"
            crv_you "\"No. I'm not drinking that, and you're not touching me. Find another subject.\""
            crv_greer "\"There's a folder in my desk.\""
        "Try to bargain":
            $ crv.shout1 = "bargain"
            crv_you "\"Tutor me. Normally. I'll do every problem set twice.\""
            crv_greer "\"Tried. Your retention is a coin toss. Sit.\""
    show cg crv_glass_hand onlayer cgl
    crv_greer "\"Grip under the glass. On her signal: a full, continuous swallow. Retention is five seconds post-ingestion. She will begin now.\""
    show cg crv_timer onlayer cgl
    vn_sfx "{i}Beep.{/i}"
    "The timer starts. She looks at it, not at you. It's the most humiliating thing that's ever happened to you and she's looking at a timer."
    crv_you "\"You can't— you can't just— this is insane, Greer, this is actually insane, people go to prison for—\""
    crv_greer "\"Thirty seconds. Hold the glass level.\""
    "She thumbs the timer. Her hand wraps round your cock, nitrile, brisk, clinical, like a technical examination. The glass is at your mouth."
    crv_you "\"Stop— this isn't— {i}hah{/i}— I said no—\""
    crv_greer "\"Now. Swallow. Retain. Don't you dare spit. Good. Do not move.\""
    "You drink. She doesn't speed up and she doesn't slow down. She's not enjoying this and she's not pretending to. And you surge embarrassingly hard in her hand."
    crv_greer "\"Orgasm now. He will.\""
    crv_you "\"Don't— {i}nnh{/i}— don't you dare make me— {i}ahh{/i}— no— no—\"" with vnfx("shake")
    show cg crv_glass_peak onlayer cgl
    crv_you "\"{i}AHH{/i}— {i}fuck{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    crv_greer "\"Fourteen seconds after the last swallow. Acceptable.\""
    show cg crv_glass_after onlayer cgl
    "She strips the glove off inside out, bins it, and writes on the clipboard while you stand there with your trousers round your knees and the empty glass in your hand and the taste in your mouth."
    crv_greer "\"He'll want to sit down. Sit down.\""
    "You sit down on the lab stool because your legs have decided for you. She doesn't look up. She's drawing a small neat tick in the first row."
    show cg crv_first_quiz onlayer cgl
    crv_greer "\"Verification. Page one of the folder. Paragraph three. Recite.\""
    "She hasn't given you the folder yet. She reads the paragraph aloud to you once, in her flat voice, from her own copy: two hundred words about orbital hybridisation, dense as concrete."
    crv_greer "\"Recite.\""
    "You open your mouth to say you can't, and the paragraph comes out instead. All of it. Word for word, in order, including the bit in brackets, in your voice, with her taste still in your mouth."
    crv_you "\"—which is why the bond angle is— is— that's— how did I—\""
    crv_greer "\"Retention confirmed. Ninety seconds post-dose.\""
    "She writes it down. You sit on the lab stool with your trousers still round your knees and recite it again in your head, and it's still there, perfect, like a song you didn't choose to learn."
    jump crv_ch1_after

## ---- ch 2: her cock in his mouth. Still timed ------------------------------------------------------
label crv_first_mouth:
    $ vn_enter(bg="crv_lab", pc="flustered", pc_tag="crv_pc", cast=[("crv_greer", "clinical")], cg="crv_kneel")
    "No glass tonight. The stopwatch is on the bench, beeping every thirty seconds. She unzips and lubes herself, still reading her clipboard."
    crv_greer "\"Next dose. Oral. Protocol two. Direct delivery covers longer. On your knees.\""
    crv_you "\"No. The glass. We said the glass.\""
    crv_greer "\"We didn't say anything. Knees.\""
    menu:
        "On your knees in the lab."
        "Tell her you'll report her":
            $ crv.shout2 = "report"
            crv_you "\"I'll report you. I'll go to the dean.\""
            crv_greer "\"And tell them what you copied?\""
        "Just say no":
            $ crv.shout2 = "no"
            crv_you "\"No. No. No.\""
    show cg crv_mouth onlayer cgl
    crv_greer "\"Open. Breathe through your nose. You will not gag. No teeth, please.\""
    "Her hand in your hair, not hard. Her cock, heavy, at your lips, and then past them, and the stopwatch ticking on the bench. Her other hand finds you through your jeans and works you in time."
    crv_greer "\"On protocol, retention increases with depth. Swallow as instructed.\""
    crv_you "\"{i}Mmh{/i}— {i}mmnh{/i}—!\""
    show cg crv_mouth_clip onlayer cgl
    "She reads the clipboard over your head while you do it. She actually reads it. You can see her eyes moving, left to right, down the page, and her hand moving on you through your jeans at exactly the same tempo, never once off the beat."
    crv_greer "\"Tongue. Lower. Good. Nadia wants the seminar slides by Thursday, remind me.\""
    crv_you "\"{i}Mmph{/i}— I'm not your— {i}mmh{/i}— secretary—\""
    crv_greer "\"Don't talk with your mouth full.\""
    "You get off harder than you want to. Harder than last week. You hate the arithmetic of that."
    show cg crv_mouth_peak onlayer cgl
    crv_you "\"{i}MMHH{/i}—!\"" with vnfx("flash", "shake")
    crv_greer "\"Retention peaking. Swallow at completion.\""
    "She withdraws, zips up, and starts the timer without a word."
    crv_greer "\"Duration: three hours. Dose accepted, no adverse events. Logged.\""
    show cg crv_knees_cards onlayer cgl
    "She doesn't let you get up. She hands you a stack of flashcards, still on your knees on the lab floor, still tasting her, and stands over you with the stopwatch."
    crv_greer "\"Thirty cards. Three hours of window. Begin.\""
    "You read them off one at a time, out loud, and every one goes in and stays, click, click, click, like coins into a slot. Reaction mechanisms. Pharmacokinetics. Things you'd never have understood on the best day of your life."
    crv_you "\"This is— this is actually insane. I understand this. I actually understand this.\""
    crv_greer "\"She knows. Card nineteen.\""
    "You read card nineteen. You understand card nineteen. You hate how much you want card twenty."
    jump crv_ch2_after

## ---- ch 3: the first penetrative. Over the bench --------------------------------------------------
label crv_first_bench:
    show cg crv_bench onlayer cgl
    crv_greer "\"Midterms. Penetrative covers days. Over the bench.\""
    crv_you "\"No. Greer, no, not that, I never— I'm not—\""
    menu:
        "Over the lab bench."
        "Grip the bench and refuse":
            $ crv.shout3 = "grip"
            crv_you "\"I'm not bending over. I'm not.\""
            "She waits. She doesn't touch you until you've bent over, and you bend over."
        "Tell her it won't fit":
            $ crv.shout3 = "fit"
            crv_you "\"That won't— it won't fit, it physically won't—\""
            crv_greer "\"It fits. I have data.\""
    crv_greer "\"Undress. Protocol specifies rectal delivery, internal retention. Breathe out.\""
    "Lube, gloved fingers, measured; then her, slow, into your ass, and the bench edge against your new hips. She props a stack of flashcards in front of your face."
    crv_greer "\"Retention increases with depth. Good. Read.\""
    crv_you "\"{i}Ohh{/i}— no— take it— take it out— {i}hahh{/i}— stop—\""
    crv_greer "\"Duration estimate up from hours to days. That's a significant improvement.\""
    "She says it in her lab voice, mid-stroke. Your cock is hard against the bench, trapped and dripping."
    show cg crv_bench_cards onlayer cgl
    crv_greer "\"Card four. Read it.\""
    crv_you "\"I can't— {i}hah{/i}— I can't read while you're—\""
    crv_greer "\"Card four.\""
    crv_you "\"{i}Nnh{/i}— nucleophilic— substitution— second order— {i}ahh{/i}— rate depends on— both— oh god—\""
    crv_greer "\"Correct. Card five.\""
    "She keeps the rhythm to your reading. Slower when you stumble. Faster when you get it right. You start getting them right on purpose and you can't decide if that's surrender or study technique."
    crv_you "\"Don't— don't— {i}nnh{/i}— don't stop— NO— I mean STOP—\"" with vnfx("shake")
    show cg crv_bench_peak onlayer cgl
    crv_you "\"{i}AHH{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "And the flashcards don't float in. They {i}install{/i}: tight, bright, every one at once."
    crv_greer "\"Retention window logs at seventy-one hours. Schedule adjusted.\""
    show cg crv_practice_paper onlayer cgl
    "Afterwards she doesn't let you sit. You can't, really. She puts a practice midterm on the bench in front of you and a pen in your hand, and you stand at the bench with her still dripping out of you and do the whole paper in forty minutes."
    crv_greer "\"Mark it.\""
    "You mark it yourself, against her answer sheet. Every one right. You check them twice. Every one."
    crv_you "\"I got them all. Greer. I got them all.\""
    crv_greer "\"Of course he did. Retention seventy-one hours. He'll sit the real one on day two.\""
    "She says it like a forecast. You stand there in your sweatpants with your long blonde hair in your eyes and the paper in your hand and feel, for the first time in your life, clever, and you can't separate it from where it came from."
    jump crv_ch3_after

## ---- ch 4: the hand that does nothing --------------------------------------------------------------
label crv_hand:
    show cg crv_hand onlayer cgl
    "Hour forty. You try. Of course you try. Your own hand, in the dorm, under the covers, and then on top of them."
    crv_you "\"Come on— come on, come {i}on{/i}—\""
    "It does nothing. It goes on doing nothing for an hour. You're hard and you stay hard and it doesn't resolve, it just climbs, and stops, and climbs."
    crv_you "\"{i}Please{/i}— why won't it— {i}nnh{/i}— please—\""
    "It only clears through her."
    show cg crv_hand_dawn onlayer cgl
    "At dawn you're on the floor of your room with the textbook open on your chest and your hand still on yourself, and the page in front of you might as well be in another alphabet. You read the same sentence nine times. It doesn't stay. Nothing stays."
    "You think about her lab. The bench. The timer. You think about it the way you used to think about food at the end of a long shift, and you know exactly what that means, and you think about it anyway."
    jump crv_ch4_dean

## ---- ch 4: hour seventy-two. He starts it ---------------------------------------------------------
label crv_begging:
    $ vn_enter(bg="crv_lab", pc="begging", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_floor")
    "On the lab floor, the back half of the taper, begging. Long and undignified, and she does not give in early. She measures."
    crv_you "\"Please. Please, please, Greer. I'll do anything. I can't think. I can't— please—\""
    crv_greer "\"You know this isn't punishment. It's protocol nine, baseline. I need three full days for clean slope data. This is hour seventy.\""
    "For a moment she's kind. She crouches and pushes the hair off your face with real gentleness."
    crv_greer "\"You're okay, Callie. This is hard. It's hardest right now, and it will stop, I promise. You're still here. I see you.\""
    "Then she goes back to the clipboard."
    crv_greer "\"Hour seventy. I need two more for clean data. Stand by.\""
    show cg crv_seventy_two onlayer cgl
    "At hour seventy-two she puts the pen down and switches her phone to record."
    crv_greer "\"Retention subject: Callie, seventy-two-hour baseline, escalated dose. Callie. Up.\""
    "Before she's said anything else you're on her: pushing her back onto the bench stool, climbing into her lap, sinking down onto her."
    crv_you "\"{i}Ahh{/i}— {i}yes{/i}— oh god— finally— {i}finally{/i}—\""
    "It's the biggest it's ever been, and it's you riding it. A man being fed."
    show cg crv_ride_record onlayer cgl
    "Her phone's recording on the bench, propped against a beaker, and you don't care. You ride her on the lab stool with your hands on her shoulders and your new long hair in both your faces, and she lets you, and holds your hips, and for once doesn't say anything at all."
    crv_you "\"Don't— don't make me wait again— Greer— don't ever make me wait like that again—\""
    crv_greer "\"Seventy-two hours was the protocol. It's done.\""
    crv_you "\"Promise.\""
    "She looks at you. It isn't in the protocol."
    crv_greer "\"...I promise.\""
    show cg crv_seventy_two_peak onlayer cgl
    crv_you "\"{i}AHH{/i}— more— don't stop— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg crv_floor_kiss onlayer cgl
    "And then, at the end, on the lab floor, with you still shaking on top of her and the phone still recording on the bench, she does something that isn't on any sheet: she pulls you down by the back of your neck and kisses you."
    "Not long. Not clinical. Just a kiss, her mouth on yours, warm, and then she lets go and looks at you from very close, and her face is doing something you've never seen it do."
    crv_greer "\"That wasn't in the protocol.\""
    crv_you "\"I noticed.\""
    crv_greer "\"Don't— she isn't going to write that down.\""
    "She reaches over and stops the recording, and doesn't write it down, and it's the first thing she's ever done that she didn't log."
    jump crv_ch4_after

## ---- ch 5: nightly. Affectionate on her side ---------------------------------------------------------
label crv_nightly:
    $ crv.fit = "nude"
    $ vn_enter(bg="crv_dorm", pc="begging", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_nightly")
    "Nightly now, then more than nightly. She comes to your room instead of making you come to the lab, which isn't in the protocol."
    "She touches you for no reason. She kisses you, which isn't a delivery method."
    crv_you "\"Greer— {i}ahh{/i}— again— is it time again—\""
    crv_greer "\"It's always time. Still so eager. Thought you'd be emptied out by now. Turn over.\""
    show cg crv_nightly_back onlayer cgl
    "On your front, her weight warm along your back, her mouth at your ear, the shrunken quiet cock under you not doing much of anything."
    crv_you "\"{i}Ahh{/i}— {i}there{/i}— don't stop— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "Afterwards she doesn't get up. That's not in the protocol either."
    show cg crv_nightly_kiss onlayer cgl
    "She lies on her side facing you with her lab glasses off and her low bun come down, and looks at you, at the face that's arriving a little more every week, and touches your cheek with one finger, and doesn't write anything down."
    crv_greer "\"Your eyes were always like that. Did you know? Even in the first week. I noted it.\""
    crv_you "\"You noted my eyes.\""
    crv_greer "\"Row four. I crossed it out. It wasn't relevant to the hypothesis.\""
    "You laugh, and she almost does, and then she kisses you, which still isn't a delivery method, and you fall asleep with her still there, which isn't either."
    show cg crv_dawn_notes onlayer cgl
    "At dawn you wake and she's still there, sitting up against your headboard in her shirt with her clipboard on her knees, writing, and when she sees you're awake she turns the clipboard face down on the duvet."
    crv_you "\"What are you writing?\""
    crv_greer "\"Observations.\""
    crv_you "\"About the dose?\""
    crv_greer "\"About him.\""
    "She means you. She looks at you for a long moment, the new face, the new hair on the pillow, and then she says it again, quietly, correcting herself."
    crv_greer "\"About her.\""
    jump crv_ch5_after

## ---- ch 6: the removal, gradually, between exams; vaginal in the back half ------------------------
label crv_removal:
    $ crv.fit = "nude"
    $ vn_enter(bg="crv_dorm", pc="dazed", pc_tag="crv_pc", cast=[("crv_greer", "warm")], cg="crv_removal_one")
    "It takes days. It happens in stages, between exams. Nobody asks you, and you don't agree. You're scheduled."
    "{color=#e89a8a}After the first exam, the night's dose, her tender the whole time: smaller. After the second: smaller still, and quiet, and your hand finds less and less there.{/color}"
    crv_greer "\"Still sensitive? We'll take it slow. Shh. You're doing so well. Just let it finish.\""
    show cg crv_removal_two onlayer cgl
    "{color=#e89a8a}After the third, in the morning, under the sheet: nothing there but smooth, and, opening under your fingertips, wet.{/color}"
    $ crv_body(6)
    show cg crv_removal_mirror onlayer cgl
    "Your face in the mirror has finished too: soft, pretty, strawberry-blonde, somebody you'd have looked at twice. You stand there with your hand flat between your legs, feeling what's there, and what isn't, and you wait to feel something terrible."
    "It doesn't come. What comes is quiet. The same quiet as when a hard exam is over: the thing you were bracing for, done, and you still standing."
    crv_you "\"It's gone.\""
    crv_greer "\"Row eleven. Complete.\""
    "She says it from the doorway, softly, the way you'd tell someone their flight's landed."
    show cg crv_first_vaginal onlayer cgl
    crv_greer "\"Will you show me?\""
    "You don't say anything. You lift your hips."
    crv_greer "\"Is it okay?\""
    "That night is the first time she's ever been there. Long, slow, and she isn't clinical at all any more; there's no stopwatch, there's no clipboard, there's only her saying your name over and over."
    crv_greer "\"Callie. Callie. Mine. You're perfect. Full marks. You did it.\""
    crv_you "\"{i}Ahh{/i}— Greer— yes— {i}yes{/i}— don't you ever {i}stop{/i}—\""
    show cg crv_first_vaginal_peak onlayer cgl
    crv_you "\"{i}AHHH{/i}— {i}GREER{/i}—!\"" with vnfx("flash", "shake")
    show cg crv_after_full onlayer cgl
    "Afterwards she lies with her head on your chest, which is a whole new thing to lie on, and draws circles on your belly with one finger, low, where there used to be something to draw circles round."
    crv_greer "\"She'll miss the cock data, you know. Eleven rows of it. It was very consistent.\""
    crv_you "\"Was that a joke? Greer. Did you just make a joke?\""
    crv_greer "\"It's not in the protocol.\""
    "You laugh so hard she has to hold on, and she laughs too, finally, out loud, a real one, into your new chest, and neither of you writes anything down for a very long time."
    jump crv_ch6_after
