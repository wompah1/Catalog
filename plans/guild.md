# guild in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"Every Quest on the Board Is Pervert Work, and the Cure Is Waiting at Rank S". Rewritten straight in
Ren'Py from the DoL route (it has no VN script in the catalog). The original is kept verbatim in
`catalog/docs/routes/vn-original/guild/` (twee, js, spec; catalog 387d2a23c). Ported in full: every
beat and line of the twee stays, and only DoL's plumbing goes.

## What stays exactly as signed off (2026-10-25)

- **Cast:**
  - **Danny Coyle, 26, the PC:** night guard at the town museum, a loud lad who bets on everything, and straight, and says so. The name box stays, and the guild's quill always writes it **Danni**, with a heart over the i.
  - **Kessa Garrow, 34:** the Garter Guild's mistress. Leathers, a red braid, a sword she never draws, a ledger she always writes in. Futa, brisk, dry: "Recruited." "Hold still." "Good. Again."
  - **Mother Pyke:** the desk clerk, knitting, never looks up. "Sign there, dear."
  - **The partners:** the porter (the fish stall), the mercenary (the fountain), Sir Osric (the bathhouse), and Tolly and Rusk (the Drunken Wyvern).
  - **The crowds watch and never touch.**
- **The premise:**
  - The museum's carved oak door, *Door, provenance unknown*, opens at two in the morning. Kessa steps out and presses two fingers to his forehead: "Recruited."
  - He wakes in Lanternwick under the dormitory eaves, in a woman's body. On the table: a rank card with seven empty boxes, F E D C B A S. The cure waits at Rank S.
- **THE RANK CARD:** one quest a rung, stamped in pink ink the next morning, and nothing ever unstamps one. Every slip ends *Accepted by:*, and whose hand writes the name, and which name, is the meter. At rung 1 he writes DANNY in block capitals and the ink slides itself into *Danni* ("That's forgery, that is."). At rung 3 he writes *Danni* himself without noticing.
- **The body:** full TSF, from the first night (a pussy he's had for one night), up to Danni, stacked, in the guild's bikini armour.
- **Every quest's act and order:**
  - **F, SECRET TOUCHING:** groped in the noon crowd at the fish stall, the porter's fingers in her, his cock between her thighs ("a dare").
  - **E, EXHIBITION:** down the high street in the quest kit to the fountain, on her knees blowing the mercenary while the square watches ("a job").
  - **D, RANK-UP EXAMINATION:** bent over Kessa's desk, the first vaginal. Kessa stamps the card on her back mid-fuck ("a fitness test").
  - **C, THE BATHHOUSE ERRAND, MANDATORY:** on the bath's tiled edge, Sir Osric, the first anal ("the local custom"). **The flip** comes halfway.
  - **B, TAVERN SERVICE:** in the guild apron and nothing else, on the back table, Tolly and Rusk, swapping. She signed before she read it.
  - **A, then S:** Kessa on the guild hall's long table in front of the benches. The cure is a tiny pink bottle labelled *Cure*, and she rips up the card.
- **The gags:**
  - the tenner bet with the day guard;
  - the bikini armour's defence-rating card;
  - limbering up like a police fitness test;
  - "Sign here." with the towel;
  - the order she gets backwards.
- **One ending,** "Rank S", with the feat *Feminised Division*.
  - The epilogue: the card's pieces pinned to the board, "New card, dear?", and Kessa's "Hold still."
  - Then **Stay** ("The Garter Guild") or **Go** ("Back through the door", into the museum at two in the morning, where she pays the tenner).
- **Forbidden:**
  - No DP.
  - No tears, no menace or threats anywhere: the cure is a prize, never leverage. No pain.
  - No measuring: Kessa takes her measure by eye.
  - No beasts or monsters.
  - The route's forbidden words are kept out of prose.

## Consent: as built (owner, 2026-10-25: the misread, then she refuses the cure)

Redlightning's pattern, retuned. Every partner takes without asking, and **Danny never says no**, because he never reads it as sex he could refuse. It's a dare, a job, a test, the custom, and he's winning it. His protest is the label, and the body betrays it.

| Rung | Quest | Register |
|---|---|---|
| 1 | the fish stall | non-con under the misread, "a dare"; he comes still claiming it |
| 2 | the fountain | non-con under the misread, "a job"; he swallows and calls it done |
| 3 | Kessa's desk | non-con under the misread, "a fitness test"; he comes shouting that he passed |
| 4 | the bathhouse (MANDATORY) | non-con, then **flip** halfway: "Oh. OH. It's not the quest, is it. Don't you DARE stop." |
| 5 | the tavern | consensual |
| 6 | the guild hall | consensual: she rips up the card |

- **The PC's lines are the spec's misread pools,** with never a no in them (rungs 1-4), then eager and filthy (5-6).
- **The non-con house rules hold.** Pinning is fine, the partners never ask, and nobody threatens.

## How it plays (Ren'Py)

- **Linear, one quest a day:** the slip from the board, the quest, the night, and Mother Pyke's stamp the next morning. The HUD shows the rank (F, then E…) where other routes show the weekday, as moon's shows the phase (question 2).
- **The rank card and the quest slips are panels** (question 1):
  - the card has its seven boxes, the stamped ones in pink;
  - each slip has its title, its terms and *Accepted by:*, with the name as written that rung (DANNY, the ink sliding to *Danni*, and so on).
- **The director scenes are written out** as beats in the partners' lines, Kessa's "Hold still." "Good. Again." and Danni's misread commentary.
- **Every flavour choice in the twee stays.** The epilogue is marked gold.
- **Not ported** (as with Red Lightning): free play. That covers the weekly quest menu after Stay, the museum door both ways, and the guild hall hub.
- **Files:** branch `guild`, worktree `catalog-renpy-guild`, `game/guild/`; names prefixed `gld_` (three letters).
- **Checks:** lint and reading. Walks wait until the route has its art.

## Art (generated, Vanripper, free only; I pick, eye-check at full size; you review after)

- **PC sprites, 7 bodies:** Danny before (sandy hair, the night-guard uniform); the first morning's body; rungs 2-6.
  - **Outfits:** the guard uniform (too big on the first morning); the guild's plain dress; the bikini armour; the guild apron and nothing else; nude.
  - **Faces:** cocky, competitive, flustered, misreading-and-moaning, wrecked, delighted.
  - About 90 images.
- **Cast:** Kessa, 3 faces (brisk, amused, intent); Mother Pyke, 1; the porter, the mercenary, Sir Osric, Tolly and Rusk, 2 each.
- **Backgrounds (11):** the museum's back gallery at night (the door), the dormitory under the eaves, the guild hall (the board, Mother Pyke's desk, the long table), the fish stall at noon, the high street, the fountain square, Kessa's office, the bathhouse's men's side, the Drunken Wyvern's back table, and Lanternwick's streets.
- **Frames:** about 100.
- **Rulings that apply:**
  - Bikini armour, never school-coded.
  - Breasts inside the step-8 cap.
  - The crowds drawn as adults who watch.
  - Two partners at rung 5, one per hole, no DP.
  - Kessa drawn futa and plainly adult.
  - Adults only.
- **No Abarus set:** full TSF.
- **Cover:** a placeholder until the art runs.

## Added scenes

None new. One built scene needs your call (question 4): **the Wyvern's cellar** (owner, 2026-10-27: "I like tentacles"; 2026-10-28: "non-con at first, then give up resisting"). In the DoL route it's a repeatable post-ending slip on the board after Stay: the thing in the cellar, tentacles only, never called a creature. It grabs her, and she kicks and swears, and breaks on its third beat. Free play isn't ported, so as it stands it would be lost.

## Questions for you

1. **The rank card and the quest slips as panels on screen**? *Recommended: yes.*
2. **The rank in the HUD** in place of the weekday? *Recommended: yes.*
3. **The epilogue marked** as the choice that decides the ending? *Recommended: yes.*
4. **The Wyvern's cellar kept**, played once inside the Stay epilogue (grabbed, resisting, breaking on the third beat, "It's back on its pin. Of course it is.")? *Recommended: yes.*

## Signed off (owner, 2026-11-12, about 2:44 pm ET)

All as recommended: every question above is answered yes. The plan stands as written. Built on its
own branch and worktree; this file moves to `game/guild/PLAN.md` there.
