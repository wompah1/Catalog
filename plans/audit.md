# audit in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"Wear This, or the Invoices Go to Head Office". Rewritten straight in Ren'Py from the DoL route (it
has no VN script in the catalog). The original is kept verbatim in
`catalog/docs/routes/vn-original/audit/` (twee, js, spec; catalog 387d2a23c). Ported in full: every
beat and line of the twee stays, and only DoL's plumbing goes.

## What stays exactly as signed off (2026-10-25)

- **Cast:**
  - Gareth Stanton, 31, the PC: assistant finance manager at Pryor and Beckett, fourth floor. For two years he's paid invoices to a supplier that doesn't exist, and the supplier is him. The name box stays. The cast call him Gareth through rung 2; Beckett calls him **Carys** from rung 3, and everyone does from rung 5.
  - **Julian Beckett, 41:** the branch director, smooth and never cruel. He's the unseen man of rungs 1-2, revealed at rung 3.
  - **Lucy Hartnell, 29:** his girlfriend, a nurse, bossy and giggly. She finds out at rung 5 and joins.
  - **Stuart Royle, 27:** sits opposite in accounts. He's the gag at rungs 1 and 4 and a partner at rung 6.
  - Walk-ons: the waiter at the Lockley and the fourth floor.
- **THE ENVELOPE:** one cream envelope a rung on the doormat, with one garment or set and one typed card. Who opens it, and how fast, is the corruption meter:
  1. the black lace set and a photocopied invoice, "Wear this. Six o'clock, the filing room…";
  2. stockings, a razor, the pink pills and a sleep mask;
  3. the black dress, heels, an auburn wig and makeup, "Tonight you are Carys";
  4. the women's skirt suit and the last strip of pills;
  5. the lanyard, "Carys Stanton, Finance", which Lucy reads out;
  6. nothing at all: "There's nothing left to make me wear."
- **The leverage**, "or the invoices go to head office", appears on the card at rungs 1, 2 and 4, and Beckett says it out loud once at the Lockley. It's never violence, never "or else", and never after rung 4.
- **The pills** are the only thing that changes the body. Nobody explains them.
- **The body:** full TSF.
  - Rung 1 is a man in black lace. At rung 2 the body hair goes in the bath, by his own razor, and the nipples go puffy.
  - Small real breasts at 3. At rung 4 the cock goes mid-act, over the desk.
  - By rung 5 she's stacked, with her own hair long and grown in auburn. Rung 6 is the peak.
  - He/him to the end of rung 4; she/her from the first line of rung 5.
- **Every scene's act and order:**
  1. The filing room in the dark: a hand through the lace, a finger.
  2. The shredder room, blindfolded: the blowjob.
  3. The Lockley: the reveal, then the first anal, face down in the dress.
  4. Over Beckett's desk, after hours, MANDATORY: anal (4A), then the cock goes. Then the first vaginal while he shreds the invoices, "You don't need these any more", and 4B, the flip.
  5. The walk-in shower with Lucy.
  6. The corner office, Beckett and Stuart, swapping: "Morning, Carys", and the peace sign.
- **The gags,** one a rung: the bra strap and "I'm FINE, mate"; shaving in the bath with Lucy knocking, "Work stuff!"; the waiter's "madam"; the jacket that won't button; "Are we binning these?"; Stuart's chat-up line.
- **One ending,** "Monday", with the feat *Head Office Never Heard*. The epilogue is a Tuesday with no envelope: **Stay** ("Carys Stanton, Finance": she keeps the job) or **Go** ("Hand in the lanyard").
- **Forbidden:**
  - The closed set: the unseen man (Beckett), Beckett, Lucy and Stuart.
  - No DP. Nothing vaginal before the shredder. Nobody touches his cock at rungs 2-4.
  - No tears, no threats beyond the card's one line, no pain.
  - No measuring, and no mirror scene.
  - The forbidden words are kept out of prose.

## Consent: as built (owner, 2026-10-25: escalating corruption, the leverage to rung 4, flipping at the shredder)

The route is already written non-con through rung 4, so the Ren'Py port keeps its consent exactly:

| Rung | Scene | Register |
|---|---|---|
| 1 | the filing room | non-con: pinned to the shelves in the dark; he comes saying no |
| 2 | the shredder room | non-con: the hand at the back of his head; he swallows saying no |
| 3 | the Lockley | non-con: laid face down; he comes untouched, still shouting no |
| 4A | over the desk (MANDATORY) | non-con |
| 4B | the shredder, the new pussy | **flip** on its second beat: "Don't— don't stop— don't you DARE stop—" |
| 5 | the shower with Lucy | consensual |
| 6 | the corner office | consensual: she undoes Stuart's belt herself |

- **Every line he says in a scene through 4A is a no,** cut into by moans, while his body tells on him. The PC lines are the spec's pools (audit1-audit4), written out.
- **No optional scenes to recast:** the route has none before rung 5.

## How it plays (Ren'Py)

- **Linear, one envelope a rung.** The HUD shows the weekday, as hypno's does, because the route names its days: Thursday, Friday, Sunday, then the Monday after.
- **The envelope is a panel:** a small route-local screen with the typed card in a typewriter face, and the paper-clipped invoice at rung 1 (question 1).
- **The three ways of opening it stay** as each rung's choice: flavour of going, never whether (for example *Swear, and get dressed* / *Read the card again* / *Bin it, then fish it out*).
- **The unseen man** at rungs 1-2 has no sprite and no lines; the frames show him as a shape in the dark, with a hand and a sleeve (question 2). He laughs once at rung 1.
- **The director scenes are written out** as beats. Beckett's lines: "Hips up, Carys." "Again." "Look at you." "Good." Lucy: "Louder." "Say my name." "Good girl." Stuart: "No WAY." "Best new starter we've ever had."
- **The epilogue is marked gold** as the choice that decides the ending.
- **Not ported** (as with Red Lightning): free play. That covers the office-lobby door, the weekly after-hours menu after Stay, and the wardrobe release.
- **Files:** branch `audit`, worktree `catalog-renpy-audit`, `game/audit/`; names prefixed `aud_` (three letters).
- **Checks:** lint and reading. Walks wait until the route has its art.

## Art (generated, Vanripper, free only; I pick, eye-check at full size; you review after)

- **PC sprites, 8 bodies:** Gareth before; rungs 1-3; rung 4 before and after the shift; rungs 5 and 6.
  - **Outfits:** his good suit; the suit over the lace; the suit over the stockings; the black dress with the auburn wig; the skirt suit; the bathrobe; the cream blouse and pencil skirt; nude.
  - **Faces:** cocky, sweating, protesting, wrecked, delighted, peace-sign grin.
  - About 110 images.
- **Cast:** Beckett, 3 faces (amused, intent, satisfied); Lucy, 2 (giggling, hungry); Stuart, 2 (gobsmacked, grinning).
- **Backgrounds (11):** the hallway and doormat, the Danube Street flat (the bread bin, the bath, the walk-in shower), the fourth floor, the filing room (dark), the shredder room, the Lockley's dining room, the room upstairs, Beckett's office after hours, the corner office by day, and the office lobby.
- **Frames:** about 120.
- **Rulings that apply:**
  - No pussy drawn before rung 4's shift.
  - Breasts inside the step-8 cap.
  - Rung 6 draws all three, with no DP.
  - The rung 1-2 frames never show the man's face.
  - Adults only.
- **No Abarus set:** full TSF.
- **Cover:** a placeholder until the art runs.

## Added scenes

None.

## Questions for you

1. **The envelope's typed card as a panel on screen**? *Recommended: yes.*
2. **The unseen man drawn faceless** (a shape in the dark, a hand, a sleeve) at rungs 1-2? *Recommended: yes.*
3. **The weekday in the HUD**? *Recommended: yes.*
4. **The epilogue marked** as the choice that decides the ending? *Recommended: yes.*

## Signed off (owner, 2026-11-12, about 2:44 pm ET)

All as recommended: every question above is answered yes. The plan stands as written. Built on its
own branch and worktree; this file moves to `game/audit/PLAN.md` there.
