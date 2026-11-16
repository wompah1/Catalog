## sister's director scenes, written out for Ren'Py (2026-11-11): open, mid, peak, Mae's climax (its own
## frame), then the passage after. All consensual, Mae eager (revamp, 2026-10-20). "Big sis" mid-act;
## Paige's "good girl" is affection. Before rung 7 Mae has a cock: no pussy, no vaginal.

## Rung 1, bath night: her cock in your soapy hands. Optional. (Sister Bath Sex; opener hand)
label si_bath_sex:
    $ vn_enter(bg="si_bathroom", pc="eager", pc_tag="si_pc", cg="si_bath_sex_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_bath_sex_open onlayer cgl
    "Your hands don't stop. You wouldn't dream of stopping."
    si_mae "\"Is that the spot? It's the spot. You did the face. Do the face again, big sis—\""
    vn_sfx "Shlk. Shlk."
    show cg si_bath_sex_mid onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae— {i}god{/i}— you're so good at this—\""
    si_mae "\"I {i}know{/i}! Thorough! Sisters are thorough!\""
    show cg si_bath_sex_peak onlayer cgl
    "Bubbles slop over the edge. Your own little cock bobs stiff against her thigh under the water, and you giggle at it and go faster."
    show cg si_bath_sex_cum onlayer cgl
    si_mae "\"Big sis— {i}ahh{/i}— I think I'm— in the {i}bath{/i}—!\"" with vnfx("flash")
    "You come against her thigh with a squeal, both hands still working her, delighted with yourself."
    $ si_enc.pc_orgasms = 1
    jump si_bath_after

## Rung 2, the morning problem: round two in her bed. Optional. (Sister Morning Sex; opener oral)
label si_morning_sex:
    $ vn_enter(bg="si_paige_room", pc="eager", pc_tag="si_pc", cg="si_morning_sex_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_morning_sex_open onlayer cgl
    "Round two. She's still hard, and you're still on her duvet, and breakfast can wait."
    si_mae "\"Less laundry. Very important. Hold still.\""
    vn_sfx "Gluk. Gluk."
    show cg si_morning_sex_mid onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl— oh, {i}good{/i} girl—\""
    si_mae "\"Mmh— mm-{i}hm{/i}—!\""
    "You moan round her like she's the best breakfast you've ever had. Your hand's slipped into your own sleep shorts somewhere along the way and you haven't noticed."
    show cg si_morning_sex_peak onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae— Mae, again— I'm going to—\""
    show cg si_morning_sex_cum onlayer cgl
    "She floods your mouth and you come with her, humming round her, squirming on the duvet." with vnfx("flash")
    $ si_enc.pc_orgasms = 1
    jump si_morning_after

## Rung 3, "Sisters share everything": first anal on the towel. MANDATORY. (Sister Share Sex; doggy, lock, inside)
label si_share_sex:
    $ vn_enter(bg="si_lounge", pc="eager", pc_tag="si_pc", cg="si_share_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_share_open onlayer cgl
    "You push back for her, and she slides in. The stretch of her going in, slow, and then the moment it stopped being a stretch and started being {i}her{/i}, so full you can't think."
    si_mae "\"{i}Ahh{/i}— big sis— oh, that's— all the way, all the way, don't you dare stop halfway—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Not stopping. God, you're {i}gorgeous{/i} like this. Listen to you.\""
    vn_sfx "Pap. Pap. Pap."
    show cg si_share_mid onlayer cgl
    "Her hands wide on your hips. You are not being quiet. Nobody in this flat has ever once asked you to be."
    si_mae "\"More— big sis, {i}more{/i}— don't stop— give it to me—\""
    "Your tiny cock bounces soft under you, ignored by both of you. Everything that matters is behind you."
    show cg si_share_peak onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl. Such a good girl. Take it, Mae.\""
    si_mae "\"Sisters share {i}everything{/i}— harder, big sis— {i}harder{/i}—!\"" with vnfx("shake")
    show cg si_share_cum onlayer cgl
    "You shake apart round her, wailing into the good cushion, and your tiny cock dribbles onto the towel without you even noticing." with vnfx("flash")
    $ si_enc.pc_orgasms = 1
    jump si_share_after

## Rung 4, skincare: a second coat. Optional. (Sister Skincare Sex; opener hand)
label si_skincare_sex:
    $ vn_enter(bg="si_bathroom", pc="eager", pc_tag="si_pc", cg="si_skincare_sex_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_skincare_sex_open onlayer cgl
    si_mae "\"Second coat! For an even glow!\""
    "Eyes still shut, face tipped up, and you reach for her yourself this time, both hands."
    vn_sfx "Shlk. Shlk."
    show cg si_skincare_sex_mid onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"You greedy thing. Look at you.\""
    si_mae "\"Skin needs {i}layers{/i}, big sis. Nell says.\""
    show cg si_skincare_sex_peak onlayer cgl
    "Your other hand's down your own shorts, and you're moaning with your eyes shut, chattering the whole way up."
    show cg si_skincare_sex_cum onlayer cgl
    "She paints your face again, and you come on the bathmat with a happy little shriek, glowing in every sense." with vnfx("flash")
    $ si_enc.pc_orgasms = 1
    jump si_skincare_after

## Rung 5, big sister's pride: again, to be sure. Optional. (Sister Pride Sex; opener titjob)
label si_pride_sex:
    $ vn_enter(bg="si_lounge", pc="eager", pc_tag="si_pc", cg="si_pride_sex_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_pride_sex_open onlayer cgl
    si_mae "\"Again. To be sure. For science.\""
    "You fold your new breasts round her again, squeezing tight, and lick the head every time it comes up."
    vn_sfx "Fwp. Fwp. Fwp."
    show cg si_pride_sex_mid onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Mae— you're going to kill me—\""
    si_mae "\"It's {i}my idea{/i}. I get to do it as much as I want. It's on the rota.\""
    show cg si_pride_sex_peak onlayer cgl
    "Your nipples drag on her thighs every stroke and it's so much you're moaning louder than she is."
    show cg si_pride_sex_cum onlayer cgl
    si_mae "\"Big sis— they're so sensitive— I'm— {i}ahh{/i}—!\"" with vnfx("flash")
    "You come from it, squeezing her between your breasts, and she comes right after, everywhere."
    $ si_enc.pc_orgasms = 1
    jump si_pride_after

## Rung 6, set the pace: again, slower. Optional. (Sister Pace Sex; opener ride)
label si_pace_sex:
    $ vn_enter(bg="si_lounge", pc="eager", pc_tag="si_pc", cg="si_pace_sex_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_pace_sex_open onlayer cgl
    si_mae "\"Slower. This time, {i}slower{/i}. I'm in charge.\""
    "You sink back down onto her, all of her, slow as you can stand."
    vn_sfx "Pap. Pap."
    show cg si_pace_sex_mid onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"You're in charge.\""
    si_mae "\"I'm {i}so{/i} in charge— {i}ohh{/i}— big sis, it's so deep like this—\""
    show cg si_pace_sex_peak onlayer cgl
    "Slower lasts about a minute. Then you're bouncing again, breasts everywhere, hair in your face, shrieking."
    show cg si_pace_sex_cum onlayer cgl
    si_mae "\"Big sis— big sis— {i}PACE{/i}—!\"" with vnfx("flash")
    $ si_enc.pc_orgasms = 1
    jump si_pace_after

## Rung 7, all the way: the first vaginal, missionary. (Sister All The Way Sex; missionary, inside)
label si_allway_sex:
    $ vn_enter(bg="si_paige_room", pc="eager", pc_tag="si_pc", cg="si_allway_open")
    $ si_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg si_allway_open onlayer cgl
    "You pull her down into you, and she slides in, slow, the head of her opening you, then more, and more."
    si_mae "\"{i}Oh{/i}— big sis— oh, it's {i}inside{/i}— it's so— don't stop, don't you dare go careful—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"I've got you. I've got you, love.\""
    vn_sfx "Shlk. Shlk."
    show cg si_allway_mid onlayer cgl
    "\"Careful\" lasts about as long as it takes her to get all the way in. Then it's just the two of you slamming together on her bed, heels locked behind her back, nails in her shoulders."
    si_mae "\"Harder— harder, big sis— I love you— I love you, {i}harder{/i}—\""
    show cg si_allway_peak onlayer cgl
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl— you're so good— Mae—\""
    show cg si_allway_cum onlayer cgl
    "Your voice climbs until you're screaming her name into her neck, and you come for the very first time like this, clenching round her, every inch of your new body lighting up at once." with vnfx("flash")
    "She comes buried to the root, groaning, shaking, pulse after pulse, so deep you feel it in your stomach."
    $ si_enc.pc_orgasms = 1
    jump si_allway_after
