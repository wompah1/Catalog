## lifeclass's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, your climax (its own
## frame), then the passage after. Lines from lifeclass.js's pools (setup.slCombatLines and
## setup.slPcLines.lifeclass): the leads' taking lines and Gino's protest, betray and break before a
## flip; the act lines after. Everybody talks: Dario narrates, Dot runs it like a session, Aurelio
## gives one word. The non-con pass (route.rpy header): rungs 1-2 never flip; the crew flips at the
## break; Aurelio on "I'm not LEAVING!"; from rung 5 it's consensual. Your cock goes inside nobody.

## Rung 1, Dario's mouth again. Optional; non-con, no flip; nothing inside you.
## (rungs.twee :: Lifeclass Stand 1 Sex; lead Dario, opener suck, anal denied)
label lc_stand_sex:
    $ vn_enter(bg="lc_room_evening", pc="protesting", pc_tag="lc_pc", cg="lc_stand_sex_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=1)
    show cg lc_stand_sex_open onlayer cgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Don't move. I'm not done with the underside.\""
    "His mouth goes back down on you, softening and all, and you go hard again in it."
    lc_you "\"I'm the {i}MODEL{/i}— I'm meant to {i}SIT{/i}— put the {i}CHARCOAL{/i} down and get {i}off{/i}—!\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Hands off my fist, you're blocking the light.\""
    show cg lc_stand_sex_mid onlayer cgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Vein's darker when you fight it. Keep fighting.\""
    vn_sfx "Shlrp."
    lc_you "\"Why's it {i}HARD{/i}— nobody said— {i}hhnn{/i}— I didn't sign up for— {i}AHH{/i}—!\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Squirm all you like. I'll draw the squirm.\""
    show cg lc_stand_sex_peak onlayer cgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Nobody asked the still life.\""
    lc_you "\"I'm not— that's not a moan, that's— {i}ahh{/i}— don't {i}DRAW{/i} that—!\"" with vnfx("shake")
    show cg lc_stand_sex_cum onlayer cgl
    "You come in his mouth, yelling at him to get off right up until you're yelling at him not to." with vnfx("flash")
    $ lc_enc.pc_orgasms = 2
    jump lc_stand_after

## Rung 2, Dot's strap-on again, timed properly. Optional; non-con, no flip.
## (rungs.twee :: Lifeclass Study 2 Sex; lead Dot, strap-on, anal, doggy, lock, inside)
label lc_study_sex:
    $ vn_enter(bg="lc_room_evening", pc="protesting", pc_tag="lc_pc", cg="lc_study_sex_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=1)
    show cg lc_study_sex_open onlayer cgl
    show lc_dot crit at vn_cast_slot
    lc_dot "\"I didn't ask. I set the pose.\""
    "Her hand stays flat on the back of your neck, and she starts again from the top of the stroke."
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Don't move. Twenty more minutes.\""
    lc_you "\"I signed up to {i}SIT{/i}— that's the job, that's the whole {i}JOB{/i}— let {i}go{/i}—!\""
    show cg lc_study_sex_mid onlayer cgl
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Shoulder. You're not paid for opinions.\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Arch is back. Keep it.\""
    lc_you "\"Stop— stop— {i}ah{/i}— why is my back doing {i}that{/i}— I'm not {i}ARCHING{/i}, I'm {i}not{/i}—\""
    show lc_dot crit at vn_cast_slot
    lc_dot "\"From the back row that reads as a protest. Fine. Keep it, it's got energy.\""
    show cg lc_study_sex_peak onlayer cgl
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Hold the line. Longer through the hip.\""
    "The strap goes in to the base whatever you say about it."
    lc_you "\"Please— I signed up to {i}SIT{/i}— just let me sit— {i}please{/i}—\"" with vnfx("shake")
    show cg lc_study_sex_cum onlayer cgl
    "You come again over the stool, untouched, yelling no the whole way into it, a thin string onto the drop cloth." with vnfx("flash")
    $ lc_enc.pc_orgasms = 2
    jump lc_study_after

## Rung 3, the shifts again, Milo first, Bjorn next. Optional; non-con, flips at the break.
## (rungs.twee :: Lifeclass Shifts 3 Sex; lead Milo, crew Bjorn, anal, inside, no DP)
label lc_shifts_sex:
    $ vn_enter(bg="lc_room", pc="protesting", pc_tag="lc_pc", cg="lc_shifts_sex_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=1)
    show cg lc_shifts_sex_open onlayer cgl
    show lc_dot crit at vn_cast_slot
    lc_dot "\"Another round. Milo first.\""
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Sorry— sorry— still my turn though—\""
    "He's back in you over the stool before you've got your knees under you."
    lc_you "\"Nobody asked me— nobody {i}ASKED{/i} the model— {i}nnh{/i}— get {i}OFF{/i}—!\""
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Dot said me. Dot said me first. I'm just doing what Dot— {i}ohh{/i}—\""
    show cg lc_shifts_sex_mid onlayer cgl
    "Then Bjorn, and his hand moves yours to the edge of the stool, and stays on it."
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Hold the edge. Not the leg, the {i}edge{/i}.\""
    lc_you "\"Get— {i}out{/i}— {i}ohh{/i}— get— why am I pushing {i}BACK{/i}— stop drawing me pushing back—!\""
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Solid.\""
    "Buried in you, over every word you're yelling at him."
    show cg lc_shifts_sex_peak onlayer cgl
    show lc_pc flushed
    lc_you "\"...Fine. {i}FINE{/i}. Draw it— draw {i}ALL{/i} of it— just nobody {i}STOP{/i}—!\"" with vnfx("shake")
    "You stop shoving the hands off and grab the stool instead, and push your ass back up into it."
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Bigger stool, I'm telling you.\""
    show cg lc_shifts_sex_cum onlayer cgl
    "They fill you up again, one after the other, while the charcoal scratches on." with vnfx("flash")
    jump lc_shifts_after

## Rung 4, THE MANDATORY SCENE: Aurelio, the biggest yet. Non-con; flips on "Don't you DARE stop,
## I'm not LEAVING!" (moved here from the recap, owner 2026-10-19/20). Her one-word verdicts are her
## only words. (rungs-late.twee :: Lifeclass Aurelio 4 Sex; anal, doggy, lock, inside, vocal)
label lc_aurelio_sex:
    $ vn_enter(bg="lc_room", pc="protesting", pc_tag="lc_pc", cg="lc_aurelio_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg lc_aurelio_open onlayer cgl
    if lc.grip == "legs":
        "You grab the stool legs to haul yourself forward and off her. They're Bjorn's legs, solid, and they hold you exactly where she wants you."
    elif lc.grip == "wait":
        lc_you "\"Aurelio, {i}WAIT{/i}— wait, wait, it won't— it won't {i}fit{/i}—\""
    else:
        "You bite down on the drop cloth to stop the noise, and the noise comes out round it anyway."
    "She pushes in. It's enormous. The fat head of her opens you wider than anything ever has, and keeps coming, thick as your wrist, sliding in and in while the whole room watches." with vnfx("shake")
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"Stay.\""
    "One hand on the back of your neck, and you stay."
    lc_you "\"Stop drawing it— stop {i}DRAWING{/i} it— can't any of you {i}SEE{/i} what's happening—!\""
    show cg lc_aurelio_mid onlayer cgl
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"Down.\""
    "She presses your chest back onto the stool by your shoulder blades."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"More.\""
    "Your hips come back onto her by both handfuls whether you push or not."
    lc_you "\"Get— {i}out{/i}— {i}ohh{/i}— get— why am I pushing {i}BACK{/i}— stop drawing me pushing back—!\""
    "Her thumbs move your hip like wet clay, wider, while you yell at her."
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    lc_you "\"It's the lights— it's just the {i}lights{/i}— {i}hah{/i}— don't you dare put that on the wall—!\""
    show cg lc_aurelio_peak onlayer cgl
    "And then she's all the way in, and everything you've got has gone up into your throat, and it comes out of you in the new high voice, at the top of it, louder than anyone's ever been in that room."
    show lc_pc flushed
    lc_you "\"...Okay. {i}OKAY{/i}. {i}Don't you DARE stop— I'm not LEAVING!{/i}\"" with vnfx("shake")
    "You shove back onto her."
    lc_you "\"Build it out— build it {i}OUT{/i}, Aurelio— {i}MORE{/i}—!\""
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"More.\""
    show cg lc_aurelio_cum onlayer cgl
    "She comes in you, and it's so much, deep and hot and endless, flooding you until it runs out round her and down the backs of your new thighs." with vnfx("flash")
    $ lc_enc.partner_came = True
    jump lc_aurelio_after

## Rung 5, the flat file again, Bjorn's thighs first. Optional; consensual (you started it).
## (rungs-late.twee :: Lifeclass Flat File 5 Sex; lead Bjorn, crew Aurelio and Milo, thighs)
label lc_flatfile_sex:
    $ vn_enter(bg="lc_room", pc="wanting", pc_tag="lc_pc", cg="lc_flatfile_sex_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg lc_flatfile_sex_open onlayer cgl
    lc_you "\"Again. Bjorn. Thighs first.\""
    show lc_bjorn practical at vn_cast_slot
    lc_bjorn "\"Didn't mean to— oh, that's— no, I meant to now. I definitely mean to now.\""
    "He's between your thighs again, and you clamp them round him and moan like the stool's on fire."
    lc_you "\"They're so {i}soft{/i}— I didn't know they could— {i}harder{/i}, use them {i}harder{/i}—!\""
    show cg lc_flatfile_sex_mid onlayer cgl
    show lc_aurelio intent at vn_cast_slot
    lc_aurelio "\"There.\""
    "Her thumbs press the outsides of your thighs together round the cock between them."
    lc_you "\"Fill it— fill the {i}form{/i}— oh god, I'm talking like Dot—!\""
    show cg lc_flatfile_sex_peak onlayer cgl
    show lc_milo keen at vn_cast_slot
    lc_milo "\"Best seat in the co-op. Best seat in the {i}building{/i}.\""
    lc_you "\"Don't call time— don't you {i}DARE{/i} call time— {i}ah{/i}— {i}ah{/i}— {i}AHH{/i}—!\"" with vnfx("shake")
    show cg lc_flatfile_sex_cum onlayer cgl
    "You come untouched across the drawer fronts again, and they finish with you one after another." with vnfx("flash")
    jump lc_flatfile_after

## Rung 6, the finale: Dario between your thighs, the board on your back. Consensual.
## (rungs-late.twee :: Lifeclass Show 6 Sex; lead Dario, thighs, doggy, lock, vocal)
label lc_show_sex:
    $ vn_enter(bg="lc_room_bare", pc="wanting", pc_tag="lc_pc", cg="lc_show_open")
    $ lc_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg lc_show_open onlayer cgl
    "You squeeze him, from the top of your thighs to your knees, and he groans into the back of your neck."
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Stay. No— stay {i}there{/i}.\""
    "He drives between your thighs and draws the curve he's fucking, stroke for stroke."
    show cg lc_show_mid onlayer cgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Inside of the thigh, soft edge, no line at all— {i}fuck{/i}, there's no line at all—\""
    lc_you "\"Ahh— squeeze— I'm {i}squeezing{/i}— can you feel— oh, you can {i}feel{/i} it—!\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Don't care. Smudge is good. Smudge is {i}honest{/i}.\""
    "The board on your back jolts with every thrust."
    show cg lc_show_peak onlayer cgl
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Can't get my hand round it. Can't get my hand round {i}one{/i} of them.\""
    "Mid-stroke, delighted."
    lc_you "\"Don't stop— whatever you're drawing, don't {i}stop{/i}—!\"" with vnfx("shake")
    jump lc_show_after
