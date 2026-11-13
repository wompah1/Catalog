## neighbour's director scenes, written out for Ren'Py (2026-11-11): open, mid, peak, your climax (its
## own frame), then the passage after. Tessa's lines from neighbour.js's pools by band (early: rungs
## 1-2, apologetic; middle: 3-4, coaching, "good girl" corrected to "boy"; late: 5-6, uncorrected).
## All consensual (the plan's non-con pass forces only rung 3's cage, in script.rpy). Before the
## TSF shift you have a cock: no pussy, no vaginal.

## Rung 1: both hands again. Optional. (rungs.twee :: Neighbour Knock Sex; opener hand)
label nb_knock_sex:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cg="nb_knock_sex_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_knock_sex_open onlayer cgl
    "You keep your hands on her. Still hot. Still hard. Still bigger than both your fists."
    nb_tess "\"Oh god, both hands, it needs both—\""
    vn_sfx "Shlk. Shlk."
    show cg nb_knock_sex_mid onlayer cgl
    nb_ellis "\"This is just helping— it's just— {i}helping{/i}—\""
    nb_tess "\"I'm sorry, I'm so sorry, don't stop, please don't stop—\""
    "Her hips find your rhythm. Your wrists ache. Your own cock is aching in your boxers and you don't understand why."
    show cg nb_knock_sex_peak onlayer cgl
    nb_tess "\"Faster— no— like that, {i}like that{/i}—\""
    show cg nb_knock_sex_cum onlayer cgl
    "She goes off again over your knuckles, gasping your name, and you come in your boxers without anything touching you, eyes squeezed shut." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_knock_after

## Rung 2: your mouth again. Optional. (Neighbour Again Sex; opener oral)
label nb_again_sex:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cg="nb_again_sex_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_again_sex_open onlayer cgl
    "Her hand stays in your hair. You open your mouth for her before she asks."
    nb_tess "\"Just the tip. Just— oh fuck, your {i}mouth{/i}—\""
    vn_sfx "Mmh. Glk. Glk."
    show cg nb_again_sex_mid onlayer cgl
    "More than the tip, this time. Your jaw stretches. You moan round her and the moan goes straight up her."
    nb_tess "\"Look at you. Look at you taking it.\""
    "She sounds amazed."
    nb_ellis "\"Mmf— {i}mmh{/i}—\""
    show cg nb_again_sex_peak onlayer cgl
    nb_tess "\"I'm sorry. I'm not sorry. Keep going.\""
    show cg nb_again_sex_cum onlayer cgl
    "You come in your boxers with her in your mouth, untouched, moaning, and she comes a second after, flooding your tongue." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_again_after

## Rung 3: your throat again. Optional. (Neighbour Throat Sex; opener oral, lock)
label nb_throat_sex:
    $ vn_enter(bg="nb_flat", pc="flushed", pc_tag="nb_pc", cg="nb_throat_sex_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_throat_sex_open onlayer cgl
    "She doesn't let you off. She just takes you back down to the root."
    nb_tess "\"All the way down. Nose in it. There you go.\""
    vn_sfx "Hlk. Hlk. Glk."
    show cg nb_throat_sex_mid onlayer cgl
    nb_tess "\"Breathe through your nose. Good girl— good {i}boy{/i}. Good boy.\""
    "Your head goes floaty. Your hands slide off her thighs and just rest on the rug."
    show cg nb_throat_sex_peak onlayer cgl
    nb_tess "\"Don't waste it. Don't you waste a drop.\""
    show cg nb_throat_sex_cum onlayer cgl
    "She holds you there and empties straight down your throat, and you come again in your sodden shorts, eyes rolled up, humming round her." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_throat_after

## Rung 5: inside you. MANDATORY. (Neighbour Inside Sex; anal, missionary, lock, inside)
label nb_inside_sex:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cg="nb_inside_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_inside_open onlayer cgl
    "She pushes in. Slow. The fat head, then the stretch, then more, and more, your knees by your ears and her arm holding them there."
    nb_ellis "\"Ahh— {i}ahh{/i}— Tessa, oh god, it's so {i}deep{/i}—\""
    nb_tess "\"Colour?\""
    nb_ellis "\"Green— {i}green{/i}—\""
    vn_sfx "Pap. Pap. Pap."
    show cg nb_inside_mid onlayer cgl
    nb_tess "\"There. Feel that? That's where I live now.\""
    "Every stroke drags over something in you that makes your whole body jolt. The cage bounces on your stomach, leaking."
    nb_ellis "\"Don't stop— please, please don't stop—\""
    nb_tess "\"Good girl. You take me so well, good girl.\""
    "She doesn't correct it. You don't want her to."
    show cg nb_inside_peak onlayer cgl
    nb_tess "\"You're mine. Say it with your ass, then. Squeeze.\""
    "You squeeze. She groans and fucks you harder, all the way in, all the way out, the bed knocking the wall."
    show cg nb_inside_cum onlayer cgl
    nb_ellis "\"I'm— Tessa— I'm {i}coming{/i}—!\"" with vnfx("shake")
    "You come with her in you and nothing on the cage, clenching round her, crying her name at the ceiling." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_inside_after

## Rung 6, TSF: the last dose, face-down. (Neighbour Last Dose Sex; anal, doggy, inside)
label nb_last_dose_sex:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cg="nb_last_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_last_open onlayer cgl
    if nb.mood == "eager":
        "You push back onto her, all the way, and she groans into your neck."
    else:
        "You hold the pillow and take it, every slow inch."
    nb_tess "\"Mine,\" she says, like she's reading it off a label. \"Mine, mine, mine.\""
    vn_sfx "Pap. Pap. Pap."
    show cg nb_last_mid onlayer cgl
    nb_ellis "\"Yours— yours— {i}ahh{/i}—\""
    "The cage swings loose under you, empty as a thimble. You don't feel it at all. You only feel her."
    show cg nb_last_peak onlayer cgl
    nb_tess "\"Don't you dare clench me out. Stay open for me.\""
    nb_ellis "\"Deeper— Tessa, deeper—\"" with vnfx("shake")
    show cg nb_last_cum onlayer cgl
    "You come face-down into her pillow with a long high wail, and something deep in you lets go with it." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_last_dose_shift

## Rung 6, TSF: your first ride, your first time as a girl. (Neighbour Last Dose Ride; opener ride)
label nb_last_dose_ride:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cg="nb_ride_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_ride_open onlayer cgl
    "You sink down. It spreads you, fills you, so much more than you thought could fit, and then it fits."
    nb_tess "\"There she is. There's my girl.\""
    vn_sfx "Shlk. Shlk."
    show cg nb_ride_mid onlayer cgl
    "You ride her until the bed's banging the wall. Hands on her chest, tits bouncing so hard they slap, your new pussy squeezing her on every drop."
    nb_tess "\"Look at you up there. Look at my girl. Ride it. All the way down, sweetheart.\""
    nb_ellis "\"Ahh— {i}ahh{/i}— yes, yes, fuck me, Tessa, it's so good, it's so {i}good{/i}, I didn't know it could—\"" with vnfx("shake")
    show cg nb_ride_peak onlayer cgl
    "Then it hits you. Not a cock going off. It starts deep, right round her, a clench that doesn't stop. It climbs. It rolls out through your tits, your thighs, your curling toes."
    show cg nb_ride_cum onlayer cgl
    "Your pussy pulses round her in long helpless squeezes and you scream her name at her ceiling, wave after wave, your first time coming as a girl." with vnfx("flash")
    "She comes with you, flooding you deep, and you come {i}again{/i} from that, wailing, collapsing onto her chest with her still pumping into you."
    "Your hips are still rolling on her. Drop, grind, squeeze. They found the rhythm before you did. You never learned that. You just know."
    $ nb_enc.pc_orgasms = 2
    jump nb_last_dose_after

## Rung 6, femboy: the morning dose, knees and elbows. (Neighbour Enough Sex; anal, doggy)
label nb_enough_sex:
    $ vn_enter(bg="nb_tessa_bedroom", pc="flushed", pc_tag="nb_pc", cg="nb_enough_open")
    $ nb_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg nb_enough_open onlayer cgl
    "Knees and elbows on her bed, the skirt flipped up over your ass. She slides in slow and deep."
    nb_tess "\"Look at that little thing bouncing in its cage. Useless. So cute.\""
    vn_sfx "Pap. Pap. Pap."
    show cg nb_enough_mid onlayer cgl
    nb_ellis "\"More— Tessa, please, {i}more{/i}—\""
    nb_tess "\"Nobody's touching that, baby. You come from me now.\""
    "Your ass bounces back on her with every stroke. The cage drips onto her sheet in a long string and you don't even notice it."
    show cg nb_enough_peak onlayer cgl
    nb_tess "\"Good girl. You take me so well, good girl.\""
    show cg nb_enough_cum onlayer cgl
    "You come somewhere in the middle of it, untouched, soft, the cage just dribbling while she fucks you, and you don't even notice till after." with vnfx("flash")
    $ nb_enc.pc_orgasms = 1
    jump nb_enough_after
