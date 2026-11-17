## lifeclass, PIN ONE BACK UP: the alternate route's own beats (owner, 2026-11-13 about 1:37 pm ET, signed off from
## twinetesting-c9's proposal). The rule doesn't change: you match the wall. At the end of rung 4 one chest sheet,
## dropped off Dot's armful, can go back up in the bare band of cork, and the chest study stays open and takes late.
## Nobody connects the drawing to the body; Dot speaks only in crit language; Dario's stack stays all cock. The
## chest (lc.grown): small on rung 5's morning, medium-large from rung 5's back study (Roz drawing the front), large
## and heavy in the show's swell, and the house cap, huge, at rung 6 when Dot calls the chest study in the doorway. Consensual from rung 5, as the route is.

## ---- rung 4, packing up: the fork ------------------------------------------------------------------
label lc_pin_fork:
    show cg lc_pin_sheet onlayer cgl
    "Afterwards, when Aurelio finally lets you go and the room's packing up for real, there's a sheet on the floor by the stand. One of the chest sheets, dropped off Dot's armful on the way to the bin: you, from the front, flat, your puffy nipples in two careful smudges. Roz's. You can tell by the swearing in the margin."
    "Roz is at the sink with her back to you. Dot's at the door with the rest of them under her arm. The band of bare cork goes right across the wall behind the stand, brown and empty and full of pinholes."
    menu:
        "The sheet on the floor."
        "Pin it back up" (ending=True):
            $ lc.pinned = True
            "You pick it up. You don't know why. You go to the wall in your inside-out sweats and pin it in the middle of the bare band of cork, on its own, with one of Roz's drawing pins in each corner, and stand back."
            "It looks lonely. It looks like exactly what it is: a sheet that didn't take. You leave it up anyway."
            show lc_dot flat at vn_cast_slot
            "Dot looks at it from the door. Then at you. Then she turns the light off."
            hide lc_dot
        "Hand it to Roz" (ending=True):
            "You pick it up and take it to the sink, and Roz takes it off you with a wet black hand, screws it into a ball and drops it in the bin without looking."
            show lc_roz swearing at vn_cast_slot
            lc_roz "\"Didn't fucking take.\""
    hide cg onlayer cgl
    return

## ---- rung 5, the break: Roz at the sink, with her hands ------------------------------------------------
label lc_pin_sink:
    $ vn_enter(bg="lc_sink", pc="flushed", pc_tag="lc_pc", cast=[("lc_roz", "fierce")], cg="lc_pin_sink")
    "At the break Roz takes you to the sink by the wrist, the way she did the first day, runs the tap hot, and soaps the brush. Then she looks at the brush, and puts it down."
    lc_roz "\"Hold fucking still.\""
    "She soaps her hands instead, charcoal-black to the elbow, and goes at your new chest with them: round and round, cupping, lifting, weighing, the lather going grey, her thumbs dragging over your puffy nipples on every pass like she's blending a value."
    lc_you "\"Roz— {i}ahh{/i}— that's not— that's not {i}washing{/i}, that's—\""
    lc_roz "\"It's reference. Shut up.\""
    lc_you "\"Sorry— {i}sorry{/i}— oh, don't stop— don't stop doing the reference—!\""
    show cg lc_pin_handprints onlayer cgl
    "You come against the sink with her hands full of you and your head back, loud enough that the café goes quiet for a second downstairs, and when she rinses you off there's a black handprint left on each side of your chest. For once they don't look small." with vnfx("flash")
    lc_roz "\"Now {i}that{/i} reads.\""
    hide cg onlayer cgl
    hide lc_roz
    return

## ---- rung 6, the show: Dot calls the chest study in the doorway ------------------------------------
label lc_pin_call:
    show cg lc_pin_dot onlayer cgl
    "Someone's on the stairs. Dot, back up for another roll of red stickers, stops in the doorway with it in her hand and looks at you. Not at your ass. At your chest, squashed out under you on the flat file."
    show lc_dot crit at vn_cast_slot
    lc_dot "{color=#f3c969}{b}“Chest study.”{/b}{/color}"
    "She says it the way she says it at the top of a session, and goes back down."
    show cg lc_pin_take onlayer cgl
    $ lc.grown = 3
    "{color=#ff5fb8}And it takes. All at once, the way nothing's taken all week: your chest swells out under you against the flat file, filling, rounder, heavier, spilling out on either side of you over the drawer tops, huge now, an armful each side, so full and so heavy you can feel it sway every time the board on your back jolts.{/color}"
    lc_you "\"{i}Ohhh{/i}— Dario— my {i}chest{/i}— it's— oh god, it's {i}so big{/i}— sorry— {i}sorry{/i}—\""
    show lc_dario drawing at vn_cast_slot
    lc_dario "\"Keep the board up.\""
    "He doesn't look at it. He never does. He looks at your thighs."
    return
