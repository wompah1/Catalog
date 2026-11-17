## camellia, MAKE IT REAL: the alternate route's own beats (owner, 2026-11-13 about 1:37 pm ET, signed off from
## twinetesting-c9's proposal). Still no magic: at ch 3's office, beside "If it's a cage, lock it", Rina can ask
## Kurosawa to make it so nobody can poach her. Kurosawa's doctor on the fourth floor: cash, no questions, a
## blister pack and a monthly jab. Slow and real, and the cage Kurosawa always wanted: nobody takes a body back
## to the men's floor. The chest (cam.grown): budding, tender and puffy under the forms by ranking night, six
## weeks on (1, sprites 3r); a contract year on, large, the forms in a drawer and then the bin (2, sprites 3y).
## Take gets sharper: Ryo binding a real chest under the suit. Ch 3's desk on is consensual, as the route is.

## ---- after the desk: the fourth floor, and six weeks ---------------------------------------------------
label cam_real_weeks:
    $ vn_enter(bg="cam_office", pc="poised", pc_tag="cam_pc", cast=[], cg="cam_real_doctor")
    "The doctor on the fourth floor of the building is a tired man in a cardigan who takes Kurosawa's envelope, counts it without looking at you, and writes nothing down."
    "A blister pack, a calendar of little white pills, one every night. A jab, the first of the month, in the hip, which he gives you without asking your name."
    "\"Slow,\" he says, to the envelope. \"Months, not weeks. Don't be impatient.\""
    "You're not impatient. You've got a contract year coming. You've got nothing but time."
    hide cg onlayer cgl
    $ cam.fit = "rig"
    $ vn_enter(bg="cam_dressing", pc="poised", pc_tag="cam_pc", cast=[], cg="cam_real_mirror")
    "Six weeks of nights. Six weeks of the pill with the last glass of water before bed, and the floor, and the forms, and the tape."
    $ cam.grown = 1
    "{color=#f2a0b4}And one night, peeling the tape off at the long mirror, you wince. Not at the tape. Under it. Two small tender swells where your chest used to be flat, puffy and tender at the tips, tender enough that you feel every inch of the tape come away. Real. Yours. Not much, but there.{/color}"
    "You stand there with the forms in one hand and look at it for a long time, and then you put the forms back on over it, very carefully, and go back out on the floor."
    hide cg onlayer cgl
    return

## ---- ch 4: Saki, at the long mirror ------------------------------------------------------------------------
label cam_real_saki:
    show cg cam_real_saki onlayer cgl
    "Then she stops, halfway to the door, and comes back, and looks at your tape in the mirror. Not at the forms. At the edge of the tape, where it's puffy underneath."
    show cam_saki sly at vn_cast_slot
    cam_saki "\"Oh, you {i}idiot{/i}.\""
    "She peels the corner of it back with one long nail before you can stop her, and presses her thumb to what's under it, and you gasp, because it's tender, and because she meant you to."
    show cam_saki sly at vn_cast_slot
    cam_saki "\"You went upstairs. You went to the fourth floor. For {i}her{/i}.\""
    cam_you "\"For me.\""
    show cam_saki sly at vn_cast_slot
    cam_saki "\"Same thing, in this building.\""
    show cg cam_real_saki_hands onlayer cgl
    "She doesn't say anything else for a while. She peels the rest of the tape off, gently, and lifts the forms away, and cups what's under them in both hands from behind you, in the mirror, as if she's weighing something on a scale."
    show cam_saki sly at vn_cast_slot
    cam_saki "\"Real ones move. You'll have to learn that. You can't sit them in a corset like silicone. You let them breathe, and you let a man see them breathe.\""
    cam_you "\"Saki— {i}ahh{/i}— that's— they're so {i}tender{/i}—\""
    show cam_saki sly at vn_cast_slot
    cam_saki "\"Good. Tender means it's working. Hold still. Lesson.\""
    "She rolls the puffy tips between her fingers, slowly, watching your face in the glass, until your knees go and you're holding the dressing table with both hands and making a noise you've never made on the floor."
    cam_you "\"Saki— Saki, don't— don't stop the {i}lesson{/i}—\""
    show cam_saki sly at vn_cast_slot
    cam_saki "\"There. That face. That's the one you'll sell.\""
    "She lets go, and tapes you back up herself, perfectly, quicker than Kurosawa, and smacks your hip, and goes out."
    hide cg onlayer cgl
    return

## ---- Sign, a contract year on: the drawer, and the bin ----------------------------------------------------
label cam_real_year:
    $ cam.grown = 2
    $ cam.fit = "red"
    $ vn_enter(bg="cam_dressing", pc="bright", pc_tag="cam_pc", cast=[], cg="cam_real_year")
    "A contract year on, at the long mirror before the floor, you do the rig the quick way now, which is mostly not doing it."
    "{color=#f2a0b4}No forms. They haven't been out of the drawer since spring. Under the red dress your own chest sits high and heavy and full, large, a real weight that moves when you breathe the way Saki said it would, and the cage hangs loose now, because there's so much less of you inside it.{/color}"
    show cg cam_real_bin onlayer cgl
    "Kurosawa comes in behind you, in the mirror, with the drawer's two silicone forms in one hand, and looks at them, and then at you."
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"You won't be needing these.\""
    "She drops them in the bin by the door, one, two, without looking where they land, and lights a cigarette off the last one, and goes back to her office with the light on."
    cam_you "\"No. I won't.\""
    hide cg onlayer cgl
    return
