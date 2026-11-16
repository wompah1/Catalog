## club's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, then the passage after,
## which lands the climax. Lines from club.js's pools: setup.slCombatLines.Ollie / .Hugh (their
## taking lines while the roster takes) and .Rhys (early, then late from the slump),
## setup.slPcLines.club (protest by section heading, betray, break, flip) and setup.clubSaid (the
## speech actions the player picked). The roster's scenes are non-con (tea service never flips;
## morale management's round two flips at the break); every Rhys scene is consensual, and he asks.
## A speech menu in each, for flavour, never whether. Nothing inside you but your mouth before the
## slump, and only Rhys ever.

## Tea service, the second course (rungs 1-4, repeatable): Hugh leads, Ollie narrates, two more of
## the roster after them; your mouth, one at a time, non-con, no flip. The captain's turn is in the
## passage after. (main.twee :: Club Tea Sex; lead Hugh, crew Ollie, extras 2, oral, deny anal,
## noncon, pool club)
label clb_tea_sex:
    $ vn_enter(bg="clb_clubroom", pc="flustered", pc_tag="clb_pc", cg="clb_tea_open")
    "Hugh's hand on the back of your head brings you forward onto him, gentle and immovable, and he's in."
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Thank you, manager.\""
    clb_you "\"That is NOT— on the SHEET— {i}mmph{/i}—!\""
    if clb.tea_pour:
        "Your free hand keeps pouring. Lemon for the libero. Two sugars for Ollie. Out of spite."
    menu:
        "His hand on your head. The roster on the benches, waiting."
        "Pull off and demand he stop":
            clb_you "\"Out— OUT— this is NOT an approved duty, I am the MANAGER—!\""
            show clb_hugh shy at vn_cast_slot
            clb_hugh "\"It's on the sheet.\""
            "Apologetically, and he doesn't let go."
        "Object by section heading":
            clb_you "\"Section four— section four says— {i}get OFF{/i}—!\""
            show clb_ollie grin at vn_cast_slot
            clb_ollie "\"And the manager OBJECTS, folks! Objection noted! Objection OVERRULED—\""
        "Mock them":
            clb_you "\"It takes the whole ROSTER to hold the manager down? I'm logging that— {i}nnh{/i}—\""
            "You get it out in one breath, and Hugh's hand brings you straight back down for the rest."
    show cg clb_tea_mid onlayer cgl
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Sorry. Sorry, Sweetheart. Nearly done. Thank you.\""
    "Both his huge hands on your head. Very gentle. Completely immovable."
    clb_you "\"Throughput is— why is throughput EXCELLENT— {i}nnh{/i}— stop—\""
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Next is when {i}we{/i} say next, Sweetheart.\""
    "Then Ollie, and then the next, and the next, a hand on your head for each."
    if clb.tier >= 3:
        "And hands everywhere else: up under your hem, kneading your ass, a palm on your cock through the lace, for luck."
    show cg clb_tea_peak onlayer cgl
    clb_you "\"Off— get— {i}mmh{/i}— get off— no— {i}no{/i}— morale is— {i}don't{/i}—\""
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Ohh, he says no, but look at the— LOOK at that, gentlemen—\""
    jump clb_tea_after

## Rung 3, the night bus, optional: your hand on the captain, under his jacket. His first scene with
## you; still "Captain". Consensual. (rungs.twee :: Club Night Bus Sex; lead Rhys, hand, vocative
## Captain, deny anal)
label clb_night_bus_sex:
    $ vn_enter(bg="clb_coach_night", pc="soft", pc_tag="clb_pc", cg="clb_bus_reciprocal")
    "You slide your hand under his jacket. He goes absolutely still."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Say if—\""
    "He starts it, and doesn't finish it. His ears go brick-red."
    menu:
        "Your hand under his jacket. His breath stopped."
        "Tell him it's an instruction":
            clb_you "\"Again, Captain. That's an instruction from the manager.\""
            "You whisper it, and wrap your hand round him."
        "Just say it":
            clb_you "\"Continue.\""
            "And you open his tracksuit with one hand, the way you'd open a kit bag."
    show cg clb_bus_reciprocal_mid onlayer cgl
    "He's hot and thick in your fist. You stroke him slow, the way he stroked you, thumb over the head, and he breathes out through his teeth like he's counting something to stay upright."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Steady. Steady, Sweetheart.\""
    "It comes out rough. He clears his throat."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"That's— yeah. That's good.\""
    "Captain-neutral. Nearly."
    clb_you "\"Mmh— that's going in the log as EXCELLENT—\""
    show cg clb_bus_reciprocal_peak onlayer cgl
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Eyes on me. Just me.\""
    "Very quiet. You look at him, only him, every streetlight sliding over his face."
    jump clb_night_bus_after

## Rung 4, morale management's round two, optional: Ollie leads (the titjob), Hugh holds your wrists,
## two more after them. Non-con, flipping at the break: you call the line yourself. Nothing goes in
## you. (rungs.twee :: Club Morale Sex; lead Ollie, crew Hugh, extras 2, titjob, deny anal, noncon,
## pool club, flip at the break)
label clb_morale_sex:
    $ vn_enter(bg="clb_clubroom", pc="flustered", pc_tag="clb_pc", cg="clb_round_two")
    "Hugh's hands find your wrists again and bring them behind your back. Ollie kneels up between your knees, already hard again, and pushes your slick tits together round himself."
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Look at that FORM! Hold him, Hugh— her— hold {i}her{/i}—\""
    clb_you "\"There is NO round two— that is NOT— on the SHEET— {i}mmph{/i}—!\""
    menu:
        "Your wrists in Hugh's hand. Ollie between your tits."
        "Demand they let go":
            clb_you "\"Let GO of my wrists— I can't take MINUTES with my wrists held—!\""
            show clb_hugh shy at vn_cast_slot
            clb_hugh "\"Sorry, manager. Thank you, manager.\""
        "Plead with them":
            clb_you "\"Please— I'm the MANAGER— the manager doesn't— {i}ahh{/i}— doesn't DO this—!\""
            show clb_ollie grin at vn_cast_slot
            clb_ollie "\"Squirming's not on the sheet either, Sweetheart.\""
            "He pins your wrists to your own tits and keeps going."
        "Scream an objection":
            clb_you "\"NO— {i}NO{/i}— objection— {i}OBJECTION{/i}—!\""
            "It bounces off the clubroom walls. The roster cheers it like a point."
    show cg clb_round_two_mid onlayer cgl
    vn_sfx "{i}Shlp. Shlp.{/i}"
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Upgraded holders! Somebody tell the sponsor!\""
    clb_you "\"I object— I OBJECT— {i}hahh{/i}— noted— it's noted that I— {i}ohh{/i}—\""
    "Then Hugh, and then the next, your tits slick and pushed together in somebody's hands, and your nipples so hard they ache."
    "Your hips file a different report from your mouth."
    show cg clb_round_two_flip onlayer cgl
    "And somewhere in the middle of it you stop pushing at his hands and push your tits together round him yourself."
    clb_you "\"...Next. {i}NEXT{/i}. Please form an orderly line—!\"" with vnfx("shake")
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"And Sweetheart takes it like a professional! The crowd goes WILD!\""
    show cg clb_round_two_peak onlayer cgl
    clb_you "\"Throughput— THROUGHPUT— {i}more{/i}— oh GOD, more—!\""
    jump clb_inspection_after

## Rung 5, the slump: Rhys on his knees, his mouth on your tiny cock. Consensual: he asked. (rungs.twee
## :: Club Slump Suck; lead Rhys, suck, vocative Rhys, deny anal)
label clb_slump_suck:
    $ vn_enter(bg="clb_sports_hall_night", pc="flustered", pc_tag="clb_pc", cg="clb_suck_open")
    if clb.hands == "hair":
        "Your hands go into his hair. He takes that as the answer, and takes you into his mouth, all of you, easy."
    else:
        "You grab the net post behind you with both hands. He takes that as the answer, and takes you into his mouth, all of you, easy."
    clb_you "\"{i}Ahh{/i}— Rhys— that's— {i}ohh{/i}—\""
    menu:
        "His mouth on you. The empty hall humming."
        "Tell him to keep going":
            clb_you "\"Please, Rhys— keep going— that's— that's a formal request—!\""
            "He hums round you and you feel it in your knees."
        "Just moan":
            clb_you "\"Haa— morale is— morale is {i}very{/i}— {i}ahh{/i}— don't stop—!\""
    show cg clb_suck_mid onlayer cgl
    "He pulls off just long enough to look up at you."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Say that again.\""
    clb_you "\"Rhys— {i}Rhys{/i}—\""
    "He licks you slow, base to tip, like there's nothing else on his schedule."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Look at you. Look at you shaking.\""
    "Against your thigh."
    show cg clb_suck_peak onlayer cgl
    clb_you "\"Continue— {i}continue{/i}— ahh— Rhys— {i}continue{/i}—!\""
    jump clb_slump_suck_after

## Rung 5: THE MANDATORY SCENE. The first anal, in your bed, face-down on knees and elbows. Rhys, the
## only man ever inside you. Consensual: "Say if—" "Continue." (rungs.twee :: Club Slump Sex; lead
## Rhys, anal, doggy, lock, inside, vocative Rhys)
label clb_slump_sex:
    $ vn_enter(bg="clb_domus_room_night", pc="loud", pc_tag="clb_pc", cg="clb_slump_open")
    "You push back. He presses in. Slow, so slow, the fat head and then more, opening you a little at a time, his hands steady on your hips."
    clb_you "\"{i}Hhhah{/i}— Rhys— {i}Rhys{/i}—\""
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"I've got you. I've got you. Breathe.\""
    menu:
        "All of him, slowly. Your cheek on your own pillow."
        "Ask for rougher":
            clb_you "\"Rougher, Rhys. I'll sign off on it.\""
            "He laughs, low, and doesn't go rougher yet. He goes deeper."
        "Push back on him":
            "You push back onto him, all the way, on your own."
            show clb_rhys composed at vn_cast_slot
            clb_rhys "\"Push back on me. Like that. Just like that.\""
        "Ask for a time-out":
            clb_you "\"Okay— okay, time-out— let me breathe, Rhys—\""
            "He stops at once, buried in you, and kisses the back of your neck until you breathe, and then you push back on him yourself."
    show cg clb_slump_mid onlayer cgl
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"You're so tight— fuck— {i}steady{/i}—\""
    "He starts to move. Long and slow, then less slow, his hand flat on the small of your back."
    clb_you "\"{i}Ahh{/i}— Rhys— that's— {i}ohh{/i}— that's going in the log as EXCELLENT—!\""
    "Your little cock hangs between your thighs and dribbles on the sheet, untouched. You don't care. Everything is where he is."
    show cg clb_slump_peak onlayer cgl
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Mine. Say it.\""
    "He leans down over your back until his mouth's at your ear."
    clb_you "\"Yours— {i}yours{/i}— Rhys— {i}AHH{/i}—!\""
    jump clb_slump_after

## From the slump, after practice, optional: on the crash mats in the equipment room. Rhys only, ever;
## anal on the tiny-cock phase, vaginal once the dogpile has made you a pussy. Consensual.
## (main.twee :: Club Practice Sex)
label clb_practice_sex:
    $ vn_enter(bg="clb_equipment_room", pc="flustered", pc_tag="clb_pc", cg="clb_crash_mat")
    "He locks the equipment room door behind you. The volleyballs in their cage watch."
    if clb.tier >= 6:
        "He lays you back on the crash mats and pushes into your new pussy, slow, all the way."
    else:
        "He lays you face down on the crash mats, flips your skirt up, and pushes into you, slow, where he's been."
    clb_you "\"{i}Hah{/i}— Rhys— that counts as— {i}conditioning{/i}—\""
    menu:
        "The crash mats. The lock on the door."
        "Give him an instruction":
            clb_you "\"Harder. I'll log it as training.\""
            show clb_rhys composed at vn_cast_slot
            clb_rhys "\"Yes, manager.\""
        "Tease him":
            clb_you "\"That all you've got, Rhys? I'll mark it down as a warm-up.\""
            "That was a mistake. A wonderful one."
    show cg clb_crash_mat_mid onlayer cgl
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Say that again.\""
    clb_you "\"Rhys— {i}Rhys{/i}—\""
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"I only ever look at you. You know that? Only you.\""
    show cg clb_crash_mat_peak onlayer cgl
    clb_you "\"{i}AHHH{/i}— Rhys— {i}CONTINUE{/i}—!\""
    jump clb_practice_after

## Rung 6: the first vaginal, against the balcony rail, the party behind the glass. Rhys, the only man
## ever inside you. Consensual. (rungs.twee :: Club Balcony Sex; lead Rhys, vaginal, missionary,
## lock, inside, vocative Rhys)
label clb_balcony_sex:
    $ vn_enter(bg="clb_balcony", pc="loud", pc_tag="clb_pc", cg="clb_balcony_open")
    "He pushes in. Slow. The head, then more, into somewhere nothing's ever been, and you cling to his shoulders on the cold rail."
    clb_you "\"Rhys— {i}Rhys{/i}— oh— oh, that's— {i}ohh{/i}—\""
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"You're so wet. You're so— god, you're soaking.\""
    menu:
        "The rail cold under you. Him hot inside you."
        "Tell him not to stop":
            clb_you "\"Don't stop— {i}don't you dare stop{/i}—!\""
        "Tell him to look at you":
            clb_you "\"Look at me— look at me, Rhys—\""
            show clb_rhys composed at vn_cast_slot
            clb_rhys "\"Look at me while I— {i}fuck{/i}—\""
    show cg clb_balcony_mid onlayer cgl
    vn_sfx "{i}Pap pap pap pap.{/i}"
    "Against the rail, his jacket round your shoulders, the whole town lit up below you."
    clb_you "\"Ahh— {i}ahh{/i}— Rhys— so {i}deep{/i}— I can feel {i}everything{/i}—\""
    "The rail's cold under your ass and he's hot inside you, so deep, so full, every stroke dragging over something new that makes your toes curl in your loafers. Your tits bounce out of the dress jacket. He catches one in his mouth. You grab his hair and hold him there and scream at the town."
    show cg clb_balcony_peak onlayer cgl
    "Then it hits. Not a little cock going off against a sheet. Deep inside, round him. A clench that won't let go. It climbs, and climbs, out through your tits, your thighs, your curling toes, your new pussy squeezing him like it's trying to keep him."
    clb_you "\"{color=#ff8fb8}AAAHN— RHYS—!{/color}\"" with vnfx("shake")
    "Your first time coming as a girl. On a balcony. At your own induction. He comes with you, deep, holding you to him with your face in his neck. You come again from that, moaning into his collar."
    jump clb_balcony_after
