# quota in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"Fill the Flask and You Get It Back". Rewritten straight in Ren'Py from the DoL route (it has no VN
script in the catalog). The original is kept verbatim in `catalog/docs/routes/vn-original/quota/`
(twee, js, spec; catalog 387d2a23c). Ported in full: every beat and line of the twee stays, and only
DoL's plumbing goes.

## What stays exactly as signed off (2026-10-25)

- **Cast:**
  - **Byron Ince, 34, the PC:** president of the Association, a dozen men in good coats who grope on the morning buses by the handbook Byron wrote. Rule one: nobody ever looks up from their phone. The name box stays.
  - **God:** a tall woman in a white trouser suit with gold eyes, eating his crisps. Amused, never cruel, never threatening. She appears in the opening and the epilogue only.
  - **The men, one a job:** Trevor (the Association's vice-president, by the handbook), Gary (the corner shop's night manager), Neville (the café's top regular), Mr Corbett (a Lantern Room VIP), Tony (FAngel's top donor) and Shawn (Club Gilt's top host).
  - **The women who hold him there and never touch him in a scene:** Siena (the café, "big sis"), Mama Jo, who names him Beryl, and Lana (the Lantern Room), and FAngel (the streamer).
- **The snap:** "Let's see how it feels." The cock is gone, and the flask hangs on a fine chain at his throat. "Fill it and you get it back. Only what stays inside you counts."
- **THE FLASK:** a pale line that climbs only when a load stays inside, and never goes down. It's described against the glass's own shape, never with a number:
  1. a thin film across the bottom;
  2. a finger's width;
  3. climbing the curve;
  4. past the middle;
  5. up into the neck;
  6. the brim, one bead running over.
- **The body:** full TSF, a stacked hourglass woman with long dark-purple hair.
- **Every job's act and order:**
  1. The morning bus: Trevor by the handbook, then at the back window, the first vaginal. He shouts his own name, and nobody looks up.
  2. The corner shop's night shift: fingered at the counter while he serves, then over the back shelf twice. The first load lands on his thigh and the line doesn't move: "It doesn't COUNT?!"
  3. Fan Appreciation Night at the Black Feather Café: Neville in his mouth, then fucking him on Siena's lap while she holds him open.
  4. The Lantern Room, MANDATORY: held down on Corbett's lap, then from behind over the VIP sofa. "Please" starts coming out between the noes. Lana: "Not mine, darling. His."
  5. FAngel's stream: Tony in his mouth, then from behind on the chaise, on camera. The biggest donation is from "AssocTrev".
  6. Club Gilt, as the paying customer: Shawn pins him in the booth and takes him his way. "Miss, does this feel good?"
- **The fork is hers:** God back on the sofa. "Well. You filled it."
  - **Drink it:** the body runs backwards, and Byron is a man in a red dress with a paunch. "You won't be groping anyone now, will you?" Feat *Back on the Bus*.
  - **Tip it out:** "Then that's that." "You keep it." Feat *Tipped It Out*.
  - Neither ending has a sex scene.
- **Forbidden:**
  - No anal anywhere, and one man per scene.
  - No tears, no menace or threats anywhere, no pain.
  - No numbers on the flask.
  - The route's forbidden words are kept out of prose.

## Consent: as built (owner, 2026-10-25: resist-then-break at every rung, NO flip)

Every job is non-con, and **nothing ever flips**: he never once wants it. What changes is how much of the no is left.

| Rung | Job | What's left of the no |
|---|---|---|
| 1 | Trevor at the back window | furious and nonstop; he shouts his own name |
| 2 | Gary over the shelf | he fights and swears the whole way, and swears at his own moaning |
| 3 | Neville on Siena's lap | no to every single thing, and every single thing makes him come |
| 4 | Corbett over the VIP sofa (MANDATORY) | "please" starts between the noes |
| 5 | Tony on the chaise, on camera | begging out loud, with "no" breaking through |
| 6 | Shawn in the booth | begging and no in the same breath, to the brim |

- **The PC's lines are the spec's pools** (outrage at 1-3, begging-with-no at 4-6), with no eager line anywhere.
- **The Tip it out ending is her choice, stated plainly:** she chooses the body, not the jobs. Nothing flips.

## How it plays (Ren'Py)

- **Linear, one job a rung.** The HUD shows the day.
- **The flask is a panel** (question 1): a small drawn glass on screen whose fill sits at one of its seven stops, with the stop's words under it and never a number. It shows twice a rung, at the morning check and in the warm flash at the throat when the line climbs. At rung 2 it shows once *unchanged*.
- **The director scenes are written out** as beats in each man's lines:
  - Trevor: "The brush. The press. Then the hand." and "Nobody ever looks up from their phone."
  - Gary: "Then hold still."
  - Corbett: "I paid for the evening, Beryl."
  - Tony: "Say hi to chat."
  - Shawn: "Miss, does this feel good?"
- **FAngel's stream** gets a chat panel at rung 5, the same kind as channel's.
- **Both ending choices are marked gold:** Drink it and Tip it out.
- **Not ported** (question 2): the Stay-or-Go home choice after each ending. It only sets the free-play home.
- **Files:** branch `quota`, worktree `catalog-renpy-quota`, `game/quota/`; names prefixed `quo_` (three letters).
- **Checks:** lint and reading. Walks wait until the route has its art.

## Art (generated, Vanripper, free only; I pick, eye-check at full size; you review after)

- **PC sprites, 8 bodies:** Byron before (thinning sandy hair, a paunch, the camel coat); rungs 1-6; and Byron restored (the Drink it ending, the man in the red dress).
  - **Outfits:** the coat and shirt; God's clothes the morning after; the shop fleece; the café uniform; Beryl's hostess dress; the stream's outfit; the red dress; nude.
  - **Faces:** pompous, outraged, protesting, begging, wrecked, resigned.
  - About 100 images.
- **Cast:**
  - God, 2 faces (amused, laughing).
  - Trevor, Gary, Neville, Corbett, Tony and Shawn, 2 each.
  - Siena, Mama Jo, Lana and FAngel, 1 each.
- **Backgrounds (10):** Byron's flat (the leather sofa, the Association's group photo), the morning bus, the corner shop and its back, the Black Feather Café's stage, the Lantern Room and its VIP sofa, FAngel's stream room, Club Gilt's booth, and Domus Street.
- **Frames:** about 100.
- **Rulings that apply:**
  - The flask is always at the throat in every frame of him from the snap on.
  - No anal is drawn.
  - One man per frame (the women hold, and don't join).
  - FAngel's horns are a headband.
  - Breasts inside the step-8 cap.
  - Adults only.
- **No Abarus set:** full TSF.
- **Cover:** a placeholder until the art runs.

## Added scenes

None.

## Questions for you

1. **The flask as a drawn panel** with its seven stops, in words? *Recommended: yes.*
2. **The Stay-or-Go home choice dropped** after the endings, since it only sets the free-play home? The Drink it / Tip it out fork stays. *Recommended: yes.*
3. **FAngel's chat as a panel** at rung 5? *Recommended: yes.*
4. **Both ending choices marked gold**? *Recommended: yes.*

## Signed off (owner, 2026-11-12, about 2:44 pm ET)

All as recommended: every question above is answered yes. The plan stands as written. Built on its
own branch and worktree; this file moves to `game/quota/PLAN.md` there.
