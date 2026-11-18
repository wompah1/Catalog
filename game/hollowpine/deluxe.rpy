## hollowpine, THE DELUXE: the alternate route's own beats (owner, 2026-11-13 about 1:37 pm ET, signed off
## from twinetesting-c9's proposal). The fork is day 4's night desk (script.rpy, hol_day_four_after); the
## swapped lines sit in script.rpy and scenes.rpy under `if hol.deluxe`. Day 4's register for the first
## application (non-con, breaking into begging), day 5's for the morning and the fitting (non-con), day 6
## consensual, as the route's pass sets them. Nobody lies to him: the card says volume, and he reads gym volume.

## ---- day 4, night: he books it ----------------------------------------------------------------------
label hol_dx_book:
    $ hol.deluxe = True
    $ hol.upgrades += 1
    show cg hol_dx_sign onlayer cgl
    "You pick it up. Of course you pick it up. You've picked it up every single day."
    hol_you "\"The Deluxe, please. Just to see it through. What's the difference, with the Contour Plus?\""
    hol_desk "\"Contour Plus is shaping. Deluxe is volume.\""
    hol_you "\"Volume. Right. Like at the gym.\""
    "You know about volume. Volume is sets and reps. Volume is what the lads on your corridor said your pecs needed, the year you bought a weight bench and used it twice and kept your shoes on it."
    hol_desk "\"Upper Contour Infusion, ma'am. Topical application with a warm compress, twice daily. It's all on the card.\""
    show screen hol_card
    "She turns the card round for you. You read every word, because you always read every word. Topical. Compress. Twice daily. Volume. So: toning, basically. A sort of sports massage, for the chest."
    hide screen hol_card
    "You sign. {i}Ellie.{/i} Your neatest one of the week."
    hol_desk "\"Lovely. Your first application's tonight. Fox will come and find you.\""
    hide cg onlayer cgl
    show cg hol_marker onlayer cgl
    "Back at the table Nadine hands you a new pair of shorts, \"for when these split up the side, probably before lunch,\" and June doesn't look up from her phone."
    show hol_june reading at vn_cast_slot
    hol_june "\"Got the ping. Deluxe.\""
    "She uncaps a marker and draws a dot on your bralette, right in the middle, and caps it again."
    show hol_june reading at vn_cast_slot
    hol_june "\"Chest status: Ellie's Deluxe.\""
    hol_you "\"It's toning. It's basically toning.\""
    show hol_june reading at vn_cast_slot
    hol_june "\"Mm.\""
    "Delaney's beside you. Your eyes are on the top of her sternum now."
    hide hol_delaney
    show cg hol_photo_wall onlayer cgl
    "You walk past the photo wall on the way out. You don't count."
    hide cg onlayer cgl
    jump hol_dx_contour

## ---- day 4, night: the first Upper Contour. Non-con, breaking into begging --------------------------
label hol_dx_contour:
    $ vn_until(22)
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_treatment", pc="earnest", pc_tag="hol_pc", cast=[("hol_tech", "bored")], cg="hol_dx_compress")
    "Fox comes for you at ten with a towel over her arm and walks you down to the treatment room, where a steel bowl is steaming on the side and the table's laid with a fresh towel."
    hol_tech "\"Upper Contour. On your back, please, ma'am. Arms by your sides.\""
    "You lie back. It's like the drainage on the first day, except the towel goes over your hips and stays there, and your chest is bare under the lamp: small and soft, with its puffy tips. You feel quite proud of it, in a way, for having tried."
    "She wrings a cloth out of the bowl and lays it across your chest, hot, a hot wet weight right across you, and presses it down with both palms."
    hol_you "\"Oh, that's nice. That's like the barber's. Is this the toning bit?\""
    hol_tech "\"Prep.\""
    show cg hol_dx_delaney onlayer cgl
    "Delaney comes in in her robe with her coffee, and puts the coffee down. Fox lifts the cloth away, and your chest steams in the cool air."
    hide hol_tech
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Evening, Deluxe.\""
    "She stands at the head of the table, opens the robe, takes her cock in her hand, and starts stroking it, slow and bored, right over you."
    $ hol.said_no += 1
    hol_you "\"Wait— wait, no, it's toning— I booked the {i}toning{/i}— I thought it was a {i}massage{/i}—\""
    hide hol_delaney
    show hol_tech bored at vn_cast_slot
    hol_tech "\"Topical application, ma'am. It's on the card.\""
    "Fox takes your wrists, not hard, and lays them back by your sides, the way she laid the towel. Delaney doesn't speed up and doesn't slow down."
    hol_you "\"No— no, not on— Delaney, not {i}there{/i}, I didn't book— {i}nnh{/i}—\""
    vn_sfx "{i}Splurt. Splurt.{/i}"
    show cg hol_dx_topical onlayer cgl
    "She comes on your chest. A lot. It's as hot as the cloth was, and it pools in the dip of your breastbone and runs down your sides, and Fox lays the compress straight back on top of it and presses with both hands, round and round, working it in."
    hide hol_delaney
    show hol_tech bored at vn_cast_slot
    hol_tech "\"Absorption's better warm.\""
    hol_you "\"Stop— please stop rubbing it— it's going {i}in{/i}— my nipples are— {i}ahh{/i}—\""
    "Your nipples are fizzing under the cloth. Then they're throbbing, sweetly, the way they did on day four's morning, and then the throb goes in, down, under the skin, like something filling up."
    show cg hol_dx_contour_june onlayer cgl
    "June's in the doorway. You didn't hear her come. She's already untying her robe."
    hide hol_tech
    show hol_june reading at vn_cast_slot
    hol_june "\"Twice daily. I'm the second.\""
    hol_you "\"It's {i}night{/i}, that's not— that's not twice daily, that's twice {i}now{/i}— no— no more on my— {i}June{/i}—\""
    "She doesn't argue. She strokes, close over your chest, while Fox lifts the cloth for her like a lid, and Delaney picks her coffee back up."
    vn_sfx "{i}Splurt.{/i}"
    "Fox works that in too. Round and round. The cloth's cooling and she doesn't hurry, and the filling feeling goes deeper every time her palms come round, and something in you goes over with it."
    show cg hol_dx_contour_beg onlayer cgl
    hol_you "\"Don't— don't stop rubbing— Fox— {i}harder{/i}, it's— more, put it all on— all {i}over{/i} them—!\"" with vnfx("flash", "shake")
    "You come untouched under the compress with your back off the table, begging for more on your chest at the top of your new light voice, and Fox works it in, unbothered, until the bowl's gone cold."
    hide hol_delaney
    hide hol_june
    show hol_tech bored at vn_cast_slot
    hol_tech "\"Lovely retention. Same again in the morning, ma'am.\""
    "You walk back up to your room with a towel round your shoulders and your arms crossed over your chest, and it's warm under your arms. It's still warm. It stays warm all night."
    hide cg onlayer cgl
    $ hol.fit = "nadine"
    call vn_night(8)
    jump hol_day_five

## ---- day 5, morning: what the night did. Non-con (the morning application) --------------------------
label hol_dx_wake:
    $ hol.grown = 1
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_room", pc="puzzled", pc_tag="hol_pc", cast=[], cg="hol_dx_wake")
    "{color=#9fe3cf}You wake on your front, and you can't lie on your front. There's something in the way. Two somethings. You roll over and they roll with you, a beat behind, soft and full and round, with a weight to them that sways when you sit up: a real chest, a proper one, more than a handful each, the tips gone big and puffy and pink.{/color}"
    hol_you "\"Oh. Oh, that's— that's a lot of toning.\""
    "Fox knocks at seven with the steaming bowl. You tell her you're fine, honestly, you've had plenty, you're at capacity. She says retention improves results, and lays you back on the bed, and does it anyway, with June, and you're late to breakfast."
    show cg hol_dx_bralette onlayer cgl
    $ hol.fit = "nadine"
    "Nadine's bralette won't fasten. You try three times in the mirror with the hook behind your back and your elbows up, and it won't meet by a long way, so you wear it unhooked, held on by its straps, under her cardigan, which doesn't close either."
    hide cg onlayer cgl
    return

## ---- day 5: the fitting, with Robin watching ----------------------------------------------------------
label hol_dx_shop:
    $ vn_enter(bg="hol_changing", pc="flustered", pc_tag="hol_pc", cast=[("hol_nadine", "brisk")], cg=None)  # ff 3:12 am: no picture, dx-fitting failed 4 draws (SCENES.md hollowpine v6)
    "After breakfast Nadine takes you by the elbow to the resort shop, past the robes and the candles, to a rail at the back you hadn't noticed, and pulls the curtain across the fitting nook."
    hol_nadine "\"Arms up.\""
    "She measures you with a tape and says the size out loud, a letter you've only ever heard in other people's conversations, and comes back with three bras over her arm, and puts you in the first one herself, hooking it at the back, lifting each of you into its cup with a flat brisk hand, like stocking a shelf."
    hol_nadine "\"There. Now you've got a shape.\""
    show hol_robin kind at vn_cast_slot
    show cg hol_dx_fitting_robin onlayer cgl
    "Robin's on the bench outside the curtain with a basket of soaps. She looks at you in the mirror, over Nadine's shoulder, for a long time."
    hol_robin "\"Ellie. Have you read what the Deluxe is?\""
    hol_you "\"Volume. Upper contour. It's basically toning, it's like— hypertrophy, you know. Like the gym.\""
    "Robin looks at the bra, and at you in it, and at Nadine, who's writing the size on a little card for the desk."
    hol_robin "\"Okay.\""
    "She doesn't say anything else. She goes back to her soaps. You turn sideways to the mirror, and it's quite a lot of hypertrophy."
    hide hol_robin
    hide cg onlayer cgl
    return
