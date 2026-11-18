## glutes' director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, your climax (its own
## frame), then the passage after. Lines from glutes.js's pools (setup.slCombatLines.Garrett and
## .Mack, setup.slPcLines.glutes, setup.glutesNoncon): the coaching unchanged, Mack's tan talk,
## Brady's frank gym-terms protest and betrayal before the turn, his asks by name after it.
## The non-con pass (route.rpy header): rung 1 consensual; rungs 2-3 non-con and never flipped; rung
## 4 flips at the end of the assjob; 5 and 6 consensual. Garrett never says "That's just prep" in a
## scene, and the "bigger target" line is authored once. No DP, ever.

## Rung 1, the bathroom floor again: hands only. Optional; consensual (the arrangement).
## (rungs.twee :: Glutes One Shave Sex; lead Garrett, opener hand, anal denied)
label gl_shave_sex:
    $ vn_enter(bg="gl_bathroom", pc="flushed", pc_tag="gl_pc", cg="gl_shave_sex_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=1)
    show cg gl_shave_sex_open onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Grip. Don't lose the grip.\""
    "His voice doesn't change at all."
    gl_you "\"Full range— {i}FULL{/i} range—!\""
    show cg gl_shave_sex_mid onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Full range.\""
    "He strokes you root to tip like he's demonstrating it."
    gl_you "\"Squeeze— squeeze— okay, that's a {i}set{/i}—!\""
    show cg gl_shave_sex_peak onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Breathe. You're holding your breath again.\""
    gl_you "\"Again. Same set. Heavier.\"" with vnfx("shake")
    show cg gl_shave_sex_cum onlayer cgl
    "You go again, both of you, on the bath mat, at the same tempo." with vnfx("flash")
    jump gl_shave_after

## Rung 2, Mack again: his call, his fist in your hair. Optional; non-con, no flip; nothing inside
## you. (rungs.twee :: Glutes Two Mack Sex; lead Mack, oral, inside, anal denied)
label gl_mack_sex:
    $ vn_enter(bg="gl_garage", pc="protesting", pc_tag="gl_pc", cg="gl_mack_sex_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_mack_sex_open onlayer cgl
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Fair's fair, hot-ass. I did the whole back.\""
    "He's back in your mouth before you've got your breath."
    gl_you "\"Mmf— Mack— the coat's {i}WET{/i}— {i}mmh{/i}— I didn't— {i}mmf{/i}—!\""
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Don't touch the coat. I've got it. I've got {i}you{/i}.\""
    "His fist stays in your hair."
    show cg gl_mack_sex_mid onlayer cgl
    "Your mouth opens wider. You didn't tell it to."
    gl_you "\"{i}Mmh{/i}— no— that's not— {i}mmf{/i}—!\""
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Nearly there. Don't you move, you'll {i}streak{/i}—\""
    "He keeps your head right where it is."
    show cg gl_mack_sex_peak onlayer cgl
    "You're sucking him now, really sucking, and his hand in your hair isn't doing any of it."
    gl_you "\"Mmh— {i}mmnh{/i}—!\"" with vnfx("shake")
    show cg gl_mack_sex_cum onlayer cgl
    "He comes again with one hand on the booth frame, and the whole thing wobbles." with vnfx("flash")
    jump gl_mack_after

## Rung 2, the car again: his call, the grip held. Optional; non-con, no flip; nothing inside you.
## (rungs.twee :: Glutes Two Car Sex; lead Garrett, thighs, lock, anal denied)
label gl_car_sex:
    $ vn_enter(bg="gl_car", pc="protesting", pc_tag="gl_pc", cg="gl_car_sex_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_car_sex_open onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"We're early.\""
    "He pulls you back down across him."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"No contact on the front. Your rule.\""
    "He drives through your thighs, slick and steady."
    gl_you "\"Garrett— it's a {i}CARE LABEL{/i}, not a— {i}ahh{/i}— not an {i}INVITATION{/i}—!\""
    show cg gl_car_sex_mid onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Squeeze. Don't lose the pinch.\""
    "He doesn't wait to see if you will. Your thighs clamp down on him anyway."
    gl_you "\"That's not a squeeze— that's just my {i}LEGS{/i}— {i}ahh{/i}—!\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Hold still.\""
    "His thumbs sink into the tan to hold you there."
    show cg gl_car_sex_peak onlayer cgl
    gl_you "\"Okay, I'm squeezing— I'm {i}SQUEEZING{/i}— don't stop, don't you {i}stop{/i}—!\"" with vnfx("shake")
    show cg gl_car_sex_cum onlayer cgl
    "He finishes between your thighs again, slow this time, and your thighs clamp down and keep it there without asking you." with vnfx("flash")
    jump gl_car_after

## Rung 3, THE MANDATORY SCENE: first anal, against the mirror, in the rear pose. Non-con; NO flip:
## you break loud and it never turns (the turn is rung 4's). Garrett coaches unchanged.
## (rungs.twee :: Glutes Three Sex; lead Garrett, anal, doggy, lock, inside, vocal)
label gl_three_sex:
    $ vn_enter(bg="gl_living_mirror", pc="protesting", pc_tag="gl_pc", cg="gl_three_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_three_open onlayer cgl
    if gl.grab3 == "wrist":
        "You get a hand back to his wrist. He takes it off without looking, puts it flat on the glass beside your face, and holds it there."
        show gl_garrett dry at vn_cast_slot
        gl_garrett "\"Hands on the glass.\""
    elif gl.grab3 == "posing":
        gl_you "\"That's not {i}POSING{/i}— that's not a {i}POSE{/i}, that's not in the {i}routine{/i}—!\""
        show gl_garrett dry at vn_cast_slot
        gl_garrett "\"Breathe.\""
    else:
        "You hold the pose. You don't know why. Your palms stay flat on the glass."
    "He sinks in. Slow, all the way, the fat head of him opening you round it, and in the mirror you watch your own glutes take him." with vnfx("shake")
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Breathe. Don't brace. Let it open.\""
    "His voice doesn't change at all."
    gl_you "\"Garrett— that's not {i}POSING{/i}— posing's {i}POSING{/i}, that's my {i}ASS{/i}—!\""
    show cg gl_three_mid onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Open them. Hold it. Breathe.\""
    "Your hips push back onto him, and you didn't tell them to."
    gl_you "\"That's not me— that's the {i}hinge{/i}— {i}hah{/i}—! Why's it— why's it {i}PUMPING{/i}— that's not a pump I trained for— {i}ahh{/i}—!\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Hips back. Sit into it.\""
    "He pulls them back himself."
    gl_you "\"I'm on a {i}CUT{/i}— I didn't ask for— {i}hnngh{/i}— that's not on the {i}PROGRAM{/i}—!\""
    show cg gl_three_peak onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Breathe. You're holding your breath again.\""
    "Every stroke hits the thing behind your balls, and the mirror fogs where your mouth is."
    gl_you "\"Okay— okay— full range— {i}FULL{/i} range— don't you {i}DARE{/i} rack it—!\"" with vnfx("shake")
    show cg gl_three_cum onlayer cgl
    "He comes in you with your face on the mirror and his hands on your hips, deep, in long slow pulses, and you can feel every one of them." with vnfx("flash")
    $ gl_enc.pc_orgasms = 1
    jump gl_three_post

## Rung 4, THE TURN: in the suit, the assjob, then anal. Non-con; flips at the end of the assjob
## ("Use it— that's what it's FOR— it's hip mobility"), and he angles in after it.
## (rungs-late.twee :: Glutes Four Sex; lead Garrett, cheeks, cheeksToAnal 3, lock, doggy)
label gl_four_sex:
    $ vn_enter(bg="gl_lamp", pc="protesting", pc_tag="gl_pc", cg="gl_four_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_four_open onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Rear relaxed. Relaxed.\""
    "He squeezes your cheeks round himself with both hands and slides, slow, all the way up the cleft."
    gl_you "\"Out— take it out— that's not a {i}POSE{/i}, that's not in the {i}routine{/i}—!\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Breathe. You're holding your breath again.\""
    show cg gl_four_mid onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Hips back. Sit into it.\""
    "He sets them with his thumbs."
    gl_you "\"Don't hit that again— that's not a muscle I've {i}TRAINED{/i}— {i}ahh{/i}—!\""
    "Your cheeks clamp down on him every time he pulls back, and you're not doing that. That's the glutes. That's just how they're built now."
    show gl_pc flushed
    gl_you "\"Use it— that's what it's {i}FOR{/i}— it's hip mobility, that's all this is— go on, {i}in{/i}, take it {i}in{/i}—!\"" with vnfx("shake")
    show cg gl_four_peak onlayer cgl
    "He angles in. The head of him finds your hole at the bottom of the next stroke, and your hips tip back for it, and this time you do tell them to."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Open them. Hold it. Breathe.\""
    gl_you "\"Mobility— it's hip mobility— open them, hold it— {i}DEEPER{/i}—!\""
    show cg gl_four_cum onlayer cgl
    "He fucks you over the lamp's corner in the blue suit, the string pushed aside, and you come untouched in the pouch with your face in the carpet." with vnfx("flash")
    $ gl_enc.pc_orgasms = 1
    jump gl_four_after

## Rung 5, the tan: Mack's titjob, then the threesome. Consensual: your asks by name.
## (rungs-late.twee :: Glutes Five Sex; lead Mack, crew Garrett, titjob, vocal, no DP)
label gl_five_sex:
    $ vn_enter(bg="gl_kitchen", pc="asking", pc_tag="gl_pc", cg="gl_five_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_five_open onlayer cgl
    if gl.ask5 == "behind":
        gl_you "\"Garrett— behind. Mack, in front. {i}In front{/i}—\""
    elif gl.ask5 == "both":
        gl_you "\"Both of you. Now. {i}Everything{/i}.\""
    else:
        gl_you "\"Tits first, Mack. Do the tits.\""
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Hold still, you'll streak.\""
    "He slides between your tits. You squeeze them together round him with both hands."
    show gl_mack grin at vn_cast_slot
    gl_mack "\"You're gonna streak {i}so{/i} bad.\""
    show cg gl_five_mid onlayer cgl
    "Garrett's behind you, both hands on your hips, and then in you, and you're between them on the kitchen tarp."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Full range.\""
    "He pulls almost all the way out, and sinks back to the root."
    gl_you "\"Mack— tighter— squeeze them {i}tighter{/i}— Garrett, deeper, {i}deeper{/i}, spot me— don't rack it, don't you {i}dare{/i} rack it—\""
    show cg gl_five_peak onlayer cgl
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Three coats on that. Three coats, and look at it.\""
    "He grabs two handfuls of your ass while Garrett's in it. They swap. Mack behind and Garrett in your mouth, and back again, oil everywhere, the tan a ruin."
    gl_you "\"Pump's in— use it— {i}use{/i} it—!\"" with vnfx("shake")
    show cg gl_five_cum onlayer cgl
    "Mack comes on your tits and up your neck and across your chin, and Garrett comes in you, deep, with his hands full of your ass." with vnfx("flash")
    jump gl_five_folder

## Rung 6, the hotel group: Garrett behind, Mack in front, Kendra (authored) pinning you in rear
## relaxed. Consensual. (rungs-late.twee :: Glutes Six Sex; lead Garrett, crew Mack, anal, doggy)
label gl_six_sex:
    $ vn_enter(bg="gl_hotel_room", pc="asking", pc_tag="gl_pc", cg="gl_six_open")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg gl_six_open onlayer cgl
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Hold rear relaxed.\""
    "Her hand flat in the middle of your back. Garrett sinks in, all the way."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Open them. Hold it. Breathe.\""
    gl_you "\"Spot me— {i}DEEPER{/i}—!\""
    show cg gl_six_mid onlayer cgl
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Arms up, hot-ass.\""
    "He's rubbing his cock on your dark red lips, and you open for him."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Chest up. Chest {i}up{/i}.\""
    "He fucks you like he's cueing a lift."
    gl_you "\"Hold the pose— {i}HOLD{/i} it— oh fuck, that's the rear relaxed—!\""
    show cg gl_six_peak onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Good. Again. Same tempo.\""
    gl_you "\"That's the glute-ham tie-in, Garrett, you're {i}in{/i} the tie-in—!\"" with vnfx("shake")
    "He fills you, deep, with his hands locked on your waist, and doesn't pull out."
    jump gl_six_season
