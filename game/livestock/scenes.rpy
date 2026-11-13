## livestock's director scenes, written out for Ren'Py (2026-11-11): open, mid, peak, your climax (its own
## frame), then the passage after. Every one is taken (owner, 2026-10-19/20): pure resist-then-break, never a
## flip. The leads' taking lines from livestock.js (Marigold's early/late `noncon`, Billy's, Angus's "Still."),
## yours from the route's pool: protest, the betrayal (it leaks), the break (begging, mooing). No tears, no
## threats. "Good girl" from Marigold only from rung 5. The ridges, never a ring. No pussy before rung 8's heat.

## Rung 2, "Again.": straight from the tap. Optional. (Livestock Two Tap Sex; oral, ma'am, deny anal)
label ls_two_tap_sex:
    $ vn_enter(bg="ls_marigold_stall", pc="defiant", pc_tag="ls_pc", cg="ls_tap_sex_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_tap_sex_open onlayer cgl
    "Her hand's back on your jaw before you've got your breath. Thumb at the hinge. Your mouth comes open."
    ls_marigold "\"Hush. Stock doesn't vote.\""
    ls_you "\"I signed up for SEASONAL HELP— not— {i}mmph{/i}—!\""
    vn_sfx "Glk. Glk."
    show cg ls_tap_sex_mid onlayer cgl
    "She rolls her hips so the ridges drag over your tongue, slow, all the way back."
    ls_marigold "\"Easy. Easy. Nobody's asking, sweetheart. Forms are final.\""
    "Your cock's leaking a string onto her straw, untouched."
    ls_you "\"{i}Mmf{/i}— why's it— why's it LEAKING— {i}mmnf{/i}—!\""
    show cg ls_tap_sex_peak onlayer cgl
    ls_marigold "\"There's the honest noise. Keep it coming.\""
    "You're not pushing at her thighs any more. You're holding them. Your head's bobbing with her hand and you didn't tell it to."
    show cg ls_tap_sex_cum onlayer cgl
    ls_you "\"{i}Mmmh{/i}— {i}mmmmh{/i}—!\"" with vnfx("shake")
    "You come in the straw with nobody touching you, moaning round her, and she groans and floods your mouth again, thick and sweet, holding you there till you've swallowed it all." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_two_tap_after

## Rung 3, claimed: first anal, in her straw. MANDATORY. (Livestock Three Claimed; anal, doggy, lock, ma'am, inside)
label ls_three_claimed:
    $ vn_enter(bg="ls_marigold_stall", pc="defiant", pc_tag="ls_pc", cg="ls_claimed_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_claimed_open onlayer cgl
    "She's in you. The head, then the ridges, one by one, slow, and her thighs pin yours so you can't get your knees under you."
    ls_cherry "\"Stop— I'm not stock— I'm not your {i}stock{/i}—!\""
    "Your bell clangs every time you thrash."
    ls_marigold "\"Wriggle all you like, sweetheart. Ma'am's got you.\""
    vn_sfx "Pap. Pap."
    show cg ls_claimed_mid onlayer cgl
    "All the way in. All the way. Her hips flush on your ass and the whole of her sitting in you, hot and heavy and impossible."
    ls_marigold "\"Look at your little cock drooling on my straw. Ma'am's heifer.\""
    ls_cherry "\"Don't— not THERE— {i}hhah{/i}— that's not fair— that's not—!\""
    "Every stroke the ridges catch on that spot, and your hips rock back into her on every word."
    show cg ls_claimed_peak onlayer cgl
    ls_marigold "\"There's the honest noise. Keep it coming.\""
    ls_cherry "\"No— {i}no{/i}— why is it— why am I so— {i}nnh{/i}— don't stop— don't you {i}stop{/i}—!\"" with vnfx("shake")
    show cg ls_claimed_cum onlayer cgl
    "You come on her cock with your face in the hay and your bell ringing, clenching on her in long helpless pulls, and she grinds in deep and holds you there through all of it." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_claimed_after

## Rung 4, the fence rail: the twins, Billy behind, Bart holding. (Livestock Four Rail Sex; anal, doggy, lock)
label ls_four_rail_sex:
    $ vn_enter(bg="ls_yard", pc="defiant", pc_tag="ls_pc", cg="ls_rail_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_rail_open onlayer cgl
    "Billy pushes in, all at once, cheerful as anything."
    ls_cherry "\"Let go— let GO of me— it's on the FORM, I'm not—!\""
    ls_billy "\"Hold her arms, Bart! Hold 'em!\""
    ls_bart "\"Got 'em, Billy!\""
    vn_sfx "Squeak. Squeak. Squeak."
    show cg ls_rail_mid onlayer cgl
    ls_billy "\"Barn-broke!\""
    "Whooping it over your yelling, and he slaps your ass on the downstroke."
    vn_sfx "Smack."
    "Your new tits are squashed on the wood, squirting. Your tiny cock's rubbing on the rail and leaking all over it."
    ls_cherry "\"Stop— it's the mash— it's the MASH doing it— {i}ahh{/i}—!\""
    show cg ls_rail_peak onlayer cgl
    ls_billy "\"Ohh, she says no and she {i}squeezes{/i}, Bart! Feel that!\""
    ls_cherry "\"Don't stop— don't you {i}stop{/i}— {i}mmmooo{/i}— please—!\"" with vnfx("shake")
    show cg ls_rail_cum2 onlayer cgl
    "He hits it, and hits it, and you go off over the rail, leaking on the wood, your toes curling in the mud." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_four_rail_after

## Rung 5, letdown: nursed on the dairy bench. (Livestock Five Bench Sex; nurse, missionary, deny anal)
label ls_five_bench_sex:
    $ vn_enter(bg="ls_dairy_bench", pc="defiant", pc_tag="ls_pc", cg="ls_nurse_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_nurse_open onlayer cgl
    "Broad tongue. Slow pulls. Her mouth closes over your nipple and draws, deep, and your back comes off her lap."
    ls_cherry "\"Hands OFF— get them OFF— I want a REFUND—!\""
    ls_marigold "\"Hush. Stock doesn't vote, Cherry.\""
    "She pins your wrists in one big hand over your head, and doesn't let up an inch."
    vn_sfx "Shlp. Shlp."
    show cg ls_nurse_mid onlayer cgl
    ls_marigold "\"Let it down. Doesn't matter if you want to. Let it {i}down.{/i}\""
    "Your chest's so tight and full it throbs. Your little cock's twitching on your belly, leaking."
    ls_cherry "\"I don't— I don't want— then why's it— {i}mmh{/i}— {i}mmmh{/i}—\""
    "A moo tries to get out round the no. You bite it back. Barely."
    show cg ls_nurse_peak onlayer cgl
    ls_marigold "\"Say no all you like, good girl. The rest of you's saying the other thing.\""
    ls_cherry "\"More— {i}more{/i}— fine— I'm STOCK— I'm stock— just don't {i}stop{/i}—!\"" with vnfx("shake")
    show cg ls_nurse_cum onlayer cgl
    "You come across her lap with her mouth on you, hips jerking, cock spitting on your belly, and her tongue just keeps on pulling." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_five_bench_after

## Rung 6, the stud's privilege: the bull pen. (Livestock Six Pen Sex; anal, doggy, lock, sir)
label ls_six_pen_sex:
    $ vn_enter(bg="ls_bull_pen", pc="defiant", pc_tag="ls_pc", cg="ls_pen_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_pen_open onlayer cgl
    "He presses in. It doesn't fit. He keeps pressing, slow and patient as a tide, and it fits."
    ls_cherry "\"Sir— {i}sir{/i}— no— it's too— get it OUT—!\""
    ls_angus "\"Still.\""
    "One word, and his fists on your horns make it true."
    vn_sfx "Splt. Splt."
    show cg ls_pen_mid onlayer cgl
    ls_angus "\"New stock always fights.\""
    "Calm as weather, and he keeps going, another slow heavy inch, and another. Your tits swing under you and leak on the straw with every one."
    ls_cherry "\"Why is it— why's it LEAKING— don't look at it—!\""
    "Your caged nub's dripping through the bars in a steady string."
    show cg ls_pen_peak onlayer cgl
    ls_angus "\"Still, heifer.\""
    "He pulls you back onto him by the horns."
    ls_angus "\"There.\""
    ls_cherry "\"Please— {i}please{/i}— I'll be good— I'll be a good heifer— {i}ahh{/i}—!\"" with vnfx("shake")
    show cg ls_pen_cum onlayer cgl
    "You come stuffed full of him, untouched, the cage dribbling, a long loud moo with no \"no\" left in it at all." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_six_pen_after

## Rung 7, "Again.": show polish, the second coat. Optional. (Livestock Seven Polish Sex; titjob)
label ls_seven_polish_sex:
    $ vn_enter(bg="ls_dairy_bench", pc="defiant", pc_tag="ls_pc", cg="ls_polish_sex_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_polish_sex_open onlayer cgl
    "Her hands close over yours on your tits, and press, and she slides back into the valley, slick with milk and the first coat."
    ls_cherry "\"Not again— no— I said {i}never{/i}—!\""
    ls_marigold "\"Forms are final, Cherry.\""
    "She holds you there."
    vn_sfx "Shlk. Shlk. Shlk."
    show cg ls_polish_sex_mid onlayer cgl
    ls_marigold "\"Squeeze them round me. Good girl. That's show polish.\""
    "Your nipples drag her thighs and squirt every stroke. The head bumps your chin, and bumps it, and your tongue's out waiting for it."
    ls_cherry "\"F-fuck— {i}fuck{/i}— no— {i}ohh{/i}—\""
    show cg ls_polish_sex_peak onlayer cgl
    ls_marigold "\"Chin up, Cherry. Judges like a cow who smiles.\""
    ls_cherry "\"{i}Mmmoo{/i}— NO— {i}mmmoooo{/i}— don't stop—\"" with vnfx("shake")
    show cg ls_polish_sex_cum onlayer cgl
    "You come from your tits, squeezing her between them, milk spraying her belly, mooing at the steamed glass." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_seven_polish_after

## The herd night: first vaginal, on the bales, before everyone. (Livestock Herd Sex; vaginal, missionary, inside)
label ls_herd_sex:
    $ vn_enter(bg="ls_herd_dais", pc="defiant", pc_tag="ls_pc", cg="ls_herd_sex_open")
    $ ls_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg ls_herd_sex_open onlayer cgl
    "She sinks in. Your brand-new pussy stretches round the ridged head, and the next ridge, and the next, all of her, the first cock ever, with the whole barn watching."
    ls_cherry "\"I'm NOT a heifer— it's a CLERICAL ERROR— get OFF—!\""
    ls_marigold "\"It's for your own good, Cherry. Good girl.\""
    "She pins your wrists in one big hand."
    vn_sfx "Shlk. Shlk."
    show cg ls_herd_sex_mid onlayer cgl
    ls_marigold "\"Look at them watching. They know where you belong. Moo for them.\""
    "Lanterns. Faces. Horns and ears all down the aisle. Your new lips grip her on every slow drag out."
    ls_cherry "\"No— {i}no{/i}— why is it— why am I so— {i}nnh{/i}—!\""
    show cg ls_herd_sex_peak onlayer cgl
    ls_marigold "\"Say no all you like, good girl. The rest of you's saying the other thing.\""
    ls_cherry "\"{i}Mmmoo{/i}— NO— {i}mmmoooo{/i}— oh god— don't stop— don't you {i}stop{/i}—!\"" with vnfx("shake")
    show cg ls_herd_sex_cum onlayer cgl
    "You come on her in front of everybody, your first time like this, your new pussy clamping round her in waves, mooing at the bunting while the herd moos back." with vnfx("flash")
    $ ls_enc.pc_orgasms = 1
    jump ls_herd_after
