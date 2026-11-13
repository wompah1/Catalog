# broker in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"I Cleared My Debt One Body Part at a Time, and Now Six Women in Town Are Wearing What I Sold".
Rewritten straight in Ren'Py (it has no VN script in the catalog). The original is kept verbatim in
`catalog/docs/routes/vn-original/broker/` (twee, js, spec).

## What stays exactly as signed off (2026-10-25)

- Cast: Wes Corbin, 24 (the PC, a broke, cheerful trader; the name box changes the first name, and
  the sheet's signature always reads W. CORBIN); Delia Vail, 38, the broker, futa, the largest thing
  in the route, never misstates a term, never asks you to trade; Romy Ashdown, 22, the runner and
  the ledger, never in a scene; Petra Sorensen, 27, the dancer (your feet and calves); Camille
  Ordway, 31, wants a man's frame and never says why (your hips); Greta Feld, 29, futa, the chest
  twice; Leona Varga, 28, the bootcamp instructor (your seat and thighs), never in a scene; Sabine
  Aubrey, 26, takes the last of it, never in a scene.
- The premise: four thousand pounds short; Vail Brokerage on the market edge of Connudatus Street
  brokers parts, one part, one named woman, both signatures, permanent; she gets yours and you get
  hers. "Declining is free." "A trade will not take across a mismatched surface." The shop grooms
  you before a part moves, and bills you for it.
- The ladder (the holdings): feet and calves to Petra; hips to Camille; a first pass of the chest
  to Greta; a first pass of the seat and thighs to Leona, then below the line, the bulk of your cock
  to Romy for cash; the chest and thigh balances (the matched set, your arithmetic); the last of it
  to Sabine. The back of every receipt lists who holds what.
- **The sheet** is the metronome, verbatim every day, the balance moving in strict sequence:
  −£4,000.00 → −£3,150.00 → −£1,900.00 → −£600.00 → £0.00 → +£2,250.00 → +£9,000.00 → PAID OUT,
  COMPLETED SET. Money is the only number in the route; it prints only on the sheet and receipt.
- The service line (the shop matches the unsold regions): full-body grooming (1), the waist (2), the
  face (3), the hair to the shoulders (4), the voice (5); "Completed sets carry no service charge."
- The body: every hair below the eyebrows, then her calves; hips and waist; a B, the ass behind the
  hips, a softer jaw; the seat and thighs, then the cock drawn down small, hair to the shoulders;
  the full G, the thighs, the voice; the pussy, and the set settles to a J. He/him until the rung 5
  signature, she/her after, unremarked.
- Every scene's act and order: 1 Petra rides you against the barre (you top); 2 Camille on her
  kitchen table (you top); 3 Greta's titjob at the fit mirror, then you top her on the bench (the
  last time); 4 Delia's first anal in the back office; 5 all three, in turn and then not (Greta's
  titjob, Camille's strap-on, Petra calling the steps with your mouth on her); 6 Delia's titjob,
  the pussy, the first vaginal (the one mandatory scene).
- The canon lines and their owners: "Declining is free." (Delia, day 1; you, the epilogue); "A trade
  will not take across a mismatched surface."; "The market pays for a matched set."; the asymmetry,
  three sentences, once; "I paid you to shave me?"; "So what's it look like below the line?";
  "That's depreciation."; "completed set"; "Is there dental?"
- The column gag: days 1-2 your eye reads the price first; from day 3 the name; Romy says one line
  about it on day 5.
- One ending, "Completed Set", and its flavour epilogue: take the chair, or cash out the set.
- No numbers on the body (cup letters only); nobody explains anything; no buy-back, no regret; no
  school framing; no pain; no DP; never "on all fours"; Romy and Sabine never in a scene; your old
  cock never touches you; every partner a woman.

## Consent: the non-con pass (owner, 2026-11-11: "Restore the book's beats")

From the spec's "Non-con beats" (catalog 8ad708084). The book's own unwilling beats come back where
you turn receptive, and the flip is rung 6.

| Rung | Scene | Register |
|---|---|---|
| 1 | Petra at the barre | as built (you top) |
| 2 | Camille's kitchen table | as built (you top) |
| 3 | Greta's titjob at the fit mirror | as built |
| 4 | Delia's first anal | non-con: you say *"Not yet"* (the book's line) and she doesn't wait |
| 5 | all three, in turn and then not | non-con: held by the throat (the book's chapter 5) |
| 6 | the first vaginal (mandatory) | **flip**: you ask for it |

- House rules: at rungs 4-5 you protest out loud, the body betrays you, and you're loud and begging
  by each scene's end. No tears, no menace, no pain; pinning is fine.
- **The throat hold** is a hand round your throat that holds you in place and never squeezes: no
  pressure, no breath, no choke (the route's "no pain" stands). It's Camille's, during the strap-on.
- Delia stays herself: dry, warm, obscene, never misstating a term. At rung 4 she hears "Not yet"
  and answers the body under her hand instead ("Your sheet says otherwise.", worded at build, never
  a threat). The authored "Say it clearly" ask is retired at rung 4 and comes back, yours, at rung 6.
- Art: the PC sprites add a **protesting** face (rungs 4-5).

## How it plays (Ren'Py)

- **Linear days, a rung a day, seven days**, as the route plays now: each opens on the walk to the
  shop (a holder seen in town), the counter and the sheet, the trade (three ways to sign: "Sign",
  "Sign fast", "Read the counterparty line twice"), the growth beat, the scene, and the receipt
  with the holdings on its back.
- **The sheet and receipt are their own panel:** a paper slip over the scene (a small Ren'Py screen
  in the route's folder, monospace, the only place a figure prints), shown at the counter and at the
  day's close.
- **The director scenes are written out** as beats (open, mid, peak, your climax, hers) from
  broker.js's pools (each woman's lines and your trader's mouth); rung 6's in full.
- **The skips go** (see question 2): DoL offered an authored skip past each long combat scene; the
  written scenes are short, so each rung's scene simply plays.
- **Not ported (as Red Lightning):** free play (the Connudatus Street door, the chair's daily shift,
  Delia's office after hours, the shop-window sightings after the ending, money in the HUD).
- **Files:** branch `broker`, worktree `catalog-renpy-broker`, `game/broker/`; names prefixed `br_`.
  Merged to main when its walks pass.

## Art (generated, Vanripper, free only; I pick, eye-check at full size; you review after)

- **PC sprites, 7 bodies:** Wes before the grooming; rungs 1-6 (rung 6 after the settle). Outfits:
  his own scruffy clothes, Romy's women's jeans and tank top (from day 2), the bathrobe (after the
  jeans split, day 5-6), the blouse and pencil skirt (the epilogue's counter), nude for the grooming
  and the growth beats. Faces: cheerful, stunned, protesting, begging, smug. About 90.
- **Cast:** Delia, 3 faces (dry, warm, hungry); Romy, 2 (gum, reading the balance), and her body
  after the cock trade drawn only as she stands (never in a scene); Petra, Camille and Greta, 2
  faces each, staged where their trade shows (Camille's square hips, Greta's chest going flat);
  Leona and Sabine, 1 each.
- **Backgrounds (12):** the bedsit, Connudatus Street and the market, the shop counter, the grooming
  side room, Petra's studio and the barre, Camille's kitchen, the women's rack, the fit-mirror room,
  the coffee cart, the market square (Leona's bootcamp), Delia's back office, the shop after hours.
- **Frames, about 105:** the debt on the phone; each day's sighting (5); the grooming (3); each
  trade's band and signatures (6); each growth beat (8); the barre (5); the kitchen table (5); the
  rack and Romy's three guesses (2); the fit mirror (5) and the bench; the zero and below the line
  (3); Delia's office (5); the jeans splitting; the group (6); the audit; Sabine's signature;
  Delia's titjob and the settle (4); the first vaginal (5); PAID OUT and the chair; both epilogues.
- **Rulings that apply:** no pussy or vaginal before rung 6, the cock drawn small at 4-5 and gone
  only in the settle; J at rung 6 is a cup letter in the prose, and the picture sits inside your
  step-8 cap; the group frames draw everyone in them; no red hair, no twin tails; the throat hold is
  drawn as a hand resting round the throat, never a grip.

## Added scenes

None proposed. Every beat the VN needs is already in the story.

## Questions for you

1. **The throat hold at rung 5** as a hand that holds and never squeezes (no choke, no breath
   play)? *Recommended: yes; it keeps the book's beat inside the no-pain rule.*
2. **Drop the per-rung skips** (the written scenes always play)? *Recommended: drop them.*
3. **The sheet as a paper-slip panel**, the only place figures print? *Recommended: yes.*
4. **An Abarus alternate set** and **the epilogue marked** as the choice that decides the ending?
   *Recommended: both, as for the others.*

## Signed off (owner, 2026-11-12, about 1:24 am ET)

Every question above is answered as recommended:

- broker: the throat hold at rung 5 holds and never squeezes (no pressure, no breath play, no
  choke); the per-rung skips dropped; the sheet as a paper slip, the only place figures print.
- moon: the hand on the back of the neck at rungs 1 and 3 (no throat grip anywhere); the moon phase
  in the HUD.
- corner and moon: the optional scenes at the non-con rungs are theirs to take.
- All three: an Abarus alternate set; the epilogue marked as the choice that decides the ending.
- Art waits: this chat is third in line for NovelAI, so the script comes first (pictures named in
  the script, a placeholder cover).

The plan stands otherwise as written. Built on its own branch and worktree; this file moves to
`game/broker/PLAN.md`.
