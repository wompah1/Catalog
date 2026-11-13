## collar's four director scenes, written out for Ren'Py (2026-11-11). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, your climax (its own
## frame), then the passage after, whose line is his. Cal's lines from collar.js's pools
## (setup.slCombatLines.Cal). Kept from each row: the act, the position, the lock on the stairwell.
## The non-con pass (route.rpy header): the couch is compelled (the voice says yes, you're unwilling);
## the stairwell is resist-then-break; the roof and the whole day come after the flip, consensual.
## Before rung 6 you have a cock: no pussy, no vaginal.

## Rung 2, the couch: his cock in your mouth again, by feel. Optional; compelled.
## (rungs.twee :: Collar Couch Sex)
label co_couch_sex:
    $ vn_enter(bg="co_lounge", pc="protesting", pc_tag="co_pc", cg="co_couch_sex_open")
    $ co_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg co_couch_sex_open onlayer cgl
    "His fingers are still in you when the voice tips you back down onto him."
    vn_th "(You were DONE. You were done—)"
    co_cal "\"Eyes up. That's it. God, that mouth.\""
    vn_sfx "Glk. Glk. Glk."
    "Slow and wet. Your lips are sealed round him before you can find any way to say no that the collar won't turn into a moan."
    show cg co_couch_sex_mid onlayer cgl
    co_cal "\"Keep talking round it. I love that voice on my cock.\""
    co_voice "\"Mmhh— {i}mmh{/i}— so {i}thick{/i}—\""
    "It talks round him in muffled purrs. He curls his fingers inside you in time, and your hips push back onto them."
    vn_th "(Stop moving. STOP moving. Why are you—)"
    co_cal "\"You can't even look down at it, can you? Just take it by feel.\""
    show cg co_couch_sex_peak onlayer cgl
    "Your throat opens. Your nose finds his belly. Your cock is straining in your jeans and nobody's touched it."
    co_voice "\"{i}Mmmh{/i}— mmh— {i}MMH{/i}—!\"" with vnfx("shake")
    show cg co_couch_sex_cum onlayer cgl
    "You come in your jeans, untouched, round his cock, his fingers deep in you, chin in the air. The voice moans it out like a song." with vnfx("flash")
    $ co_enc.pc_orgasms = 1
    "He comes a moment after, deep, holding your head, and the voice drinks every drop of it."
    jump co_couch_after

## Rung 3, the stairwell: first anal over the stair rail. MANDATORY; resist, then break.
## (rungs.twee :: Collar Stairwell Sex; lead Cal, opener anal, doggy, lock)
label co_stairwell_sex:
    $ vn_enter(bg="co_stairwell", pc="protesting", pc_tag="co_pc", cg="co_stairs_open")
    $ co_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg co_stairs_open onlayer cgl
    "Your hands close on the rail. You tell them to let go. They don't."
    "Cal tugs your jeans down to your thighs. Cold air on your ass, and then his hands, warm, spreading you."
    vn_th "(Not here. Not on the STAIRS. Anyone could—)"
    "You try to twist away. Your hips push back toward him instead."
    co_cal "\"Easy. I've got you.\""
    vn_sfx "Shlk."
    "Slick, then the blunt head of him, then the push. Big. So big. Your whole body tries to close round the stretch and your ass just takes it."
    co_voice "\"{i}Ohhh{/i}— oh, {i}Cal{/i}—\""
    "You meant {i}stop{/i}. Every word you try comes out as his name."
    show cg co_stairs_mid onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    co_cal "\"Fuck, you're tight. You're gripping me like you never want me out.\""
    "You can't shout. Every door on every floor would hear. So you grit your teeth, and the voice moans through them anyway."
    co_cal "\"Listen to you. The whole building can hear that voice.\""
    vn_th "(Let go of the rail. Let GO. Walk away. Walk—)"
    "Your knees are shaking. Your cock's leaking down your thigh. Your ass squeezes him on every stroke like it's been doing this for years."
    co_cal "\"Chin up. Look at me while I fuck you.\""
    "He laughs, because the collar's already doing it."
    show cg co_stairs_peak onlayer cgl
    "And then, somewhere in the slap of it, you stop pulling."
    "You hold the rail because you need something to hold. You stop fighting your hips. You let it happen to you, and it happens, all of it, faster."
    co_voice "\"Again— again— harder, Cal, {i}harder{/i}—\"" with vnfx("shake")
    vn_th "(You don't want this. You don't. You just can't stop it any more.)"
    co_cal "\"You want to know what I see? I see you taking every inch and begging for more.\""
    show cg co_stairs_cum onlayer cgl
    co_voice "\"{i}Ahhh{/i}— Cal— I'm— {i}AHH{/i}—!\""
    "You come untouched, spurting over the step below, clenching on him so hard he grunts, and the stairwell rings with it, up and down three floors." with vnfx("flash")
    $ co_enc.pc_orgasms = 1
    jump co_stairwell_after

## Rung 4, the roof: riding him again, in his lap. Optional; consensual (after the flip).
## (rungs.twee :: Collar Roof Sex; opener ride)
label co_roof_sex:
    $ vn_enter(bg="co_roof", pc="delighted", pc_tag="co_pc", cg="co_roof_sex_open")
    $ co_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg co_roof_sex_open onlayer cgl
    "You sink back down on him. All the way. Your choice."
    co_you "\"Again. I want it again.\""
    co_cal "\"Look at you up there. Look at you.\""
    vn_sfx "Pap. Pap."
    show cg co_roof_sex_mid onlayer cgl
    "You ride him slow, then not slow, your hands on his shoulders, the stars swinging overhead."
    co_cal "\"Your tits are bouncing. You can't see them, but trust me, they're bouncing.\""
    co_you "\"Tell me— tell me how much—\""
    co_cal "\"{i}Chin up{/i}.\""
    "He says it against your throat, right at the edge of the collar, and you shiver all the way down onto him."
    show cg co_roof_sex_peak onlayer cgl
    co_you "\"Cal— Cal, don't stop, don't you {i}dare{/i} stop—\"" with vnfx("shake")
    show cg co_roof_sex_cum onlayer cgl
    "You come again, untouched, your cock spilling between your bellies, your cry going out over the rooftops." with vnfx("flash")
    $ co_enc.pc_orgasms = 1
    "He holds your hips down and comes in you with a groan you feel in your chest."
    jump co_roof_after

## Rung 5, the whole day: back over the counter, already in you. Optional; consensual.
## (rungs.twee :: Collar Whole Day Sex; anal, doggy, inside)
label co_whole_day_sex:
    $ vn_enter(bg="co_kitchen", pc="delighted", pc_tag="co_pc", cg="co_day_sex_open")
    $ co_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg co_day_sex_open onlayer cgl
    "He's still in you. You bend back over the worktop and push back onto him, and he laughs, and starts again."
    co_cal "\"Your ass is filling out, you know that? I can feel it every time I pull back.\""
    vn_sfx "Pap. Pap. Pap."
    show cg co_day_sex_mid onlayer cgl
    co_you "\"Harder— make them bounce— {i}harder{/i}—\""
    "Your tits drag on the worktop. His hand finds your soft little cock again and just holds it, fondly, while he fucks you."
    co_cal "\"You're softer every time I get my hands on you.\""
    show cg co_day_sex_peak onlayer cgl
    co_you "\"Cal— {i}Cal{/i}— I'm— oh, {i}fuck{/i}—!\"" with vnfx("shake")
    show cg co_day_sex_cum onlayer cgl
    "It dribbles out of you into his hand, weak and warm, while your ass milks him through all of it." with vnfx("flash")
    $ co_enc.pc_orgasms = 1
    "He comes in you again, slow and deep, with his forehead against the back of your neck."
    jump co_whole_day_after
