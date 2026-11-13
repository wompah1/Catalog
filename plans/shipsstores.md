# shipsstores in Ren'Py: the VN plan (signed off 2026-11-12, about 3:59 pm ET)

Owner, 2026-11-12, about 3:59 pm ET: "Approve the plan"; Stay and Go: "Both get a scene".

"Ship's Stores" (adapted from the package `sent/ships-stores-package.md`, on DoL's own pirate ship;
every character is an adult). Rewritten straight in Ren'Py; it has no VN script in the catalog. The
original is kept verbatim in `catalog/docs/routes/vn-original/shipsstores/` (twee, js, spec; catalog
58c776017). Claimed by twinetesting-32 in `CLAIMS.md` (492eecf), prefix `shp_` (three letters).

## What stays exactly as signed off (2026-10-13; non-con beats 2026-10-19/20)

- **Cast (all 19+):**
  - Jonah Creed, 24: the PC, a cheerful, shameless deckhand. Goes over the side of the *Patience*
    in a squall and is fished out by the wrong ship. The name box changes the first name. The crew
    call you *girl* from the deck on.
  - Captain Roke: big, grey-eyed, an iron-grey square beard, a flat-brimmed hat and a long black
    coat. Short flat lines; keeps every rule he says out loud. Thrown exactly once, at his table in
    rung 6.
  - Guillam: cook and surgeon; sits on the slop-chest in the bilge; sells, takes payment, never
    explains anything.
  - The five: Delph (bosun, watches your feet; the decent one), Harrow (topman, leaps), Coil
    (gunner, punches), Trask (helm, fakes: "Oldest one there is"), Ned (gangly, sweet; over the
    rail in rung 1, saved off the snapped spar in rung 5).
  - The passengers and the stage's MC: never named.
- **The two metronomes:** Roke speaks your rank aloud once per rung, and the purse is stated at the
  close of every rung. The goal is £15,000 for a mate's berth. Takings rise every rung; savings
  peak at rung 4 and fall after, and nothing on the page remarks on it.
- **Guillam's slop-chest, the reinvestment ladder:** you buy every change yourself, with stage
  money, and he never explains what anything is: the paint and the laces (£50), the salve (£250),
  the flask (£500), the last bottle (£700).
- **The ladder:**

| Rung | Rank (title card) | Noon | Act | Body |
|---|---|---|---|---|
| 1 | Wretched Scum | none | the gauntlet: four clean dodges, then Roke; the deck (**mandatory**) | nothing; *girl* from the deck on |
| 2 | Worthless Scum | four levels | the raid; then the crew in the bilge | the paint and the laces (presentation only) |
| 3 | Endearing Scum | six levels | the raid: the dancing round, the sun-cream round | hips, arse, thighs |
| 4 | Scum No Longer | ten out of ten | the raid, three at once at the top; Roke's gun and the gold compass | the chest; "she" from here, the cock still on |
| 5 | A Scummy Mate | the quiet ransack, no wages | the spar; Delph's berth, deliberately the flattest sex in the route | the cock goes: four flat lines |
| 6 | Stores | the boat again | Roke's table; all six in the bilge, by name, one at a time, Roke last | everything at its peak |

- **The purse after each rung:** £0, £350, £700, £1,200, £500, spent (each raid pays £100 a level,
  paid in your hand on the stage by Roke).
- **The forbids:** no tears, crying or sobbing anywhere; no menace; no pain; no denial monologues or
  shame spirals; no architect (nobody proposes a purchase or comments on one); the hole punishment
  stays cut; no red hair, no twin tails; no numbers in prose but the purse, the pay, the prices and
  the count (the package's metronome).

## Consent: already ruled (2026-10-19/20, escalating corruption)

| Rung | Scene | Register |
|---|---|---|
| 1 | Roke on the deck (mandatory) | non-con, no flip |
| 2 | the raid at four; the crew in the bilge | non-con, no flip |
| 3 | the raid at six | non-con (the body plays to the count while the mouth says no) |
| 4 | the raid at ten | non-con, flips at the break with the flip line ("Count it— COUNT it— that's TEN, you bastards—!"); the trio after it consensual |
| 5 | Delph's berth | consensual |
| 6 | all six by name; the noon bell | consensual |

THE LINE ("never trapped, never degraded") is struck: "scum can go over the rail any night" is an
empty boast in your protest lines; Roke's rule speech and the walk still say it, and in the walk you
get one leg over the rail and take it back down. No eager word in a non-con stage (the 2026-10-22
rule): before a flip the slips are corrected ("don't stop— no— I meant STOP—").

## How it plays (Ren'Py)

**Linear days, one per rung**, each opening on the rank as its title card. Free play (the deck, the
bilge hub, the Pirate Bed, the figurehead, the town door) is not ported.

**The raids** are written out round by round from the route's own texts (`setup.ssRounds`,
`ssRoundsResist`, `ssMoments`, `ssStageLines`, `ssCrowdLines`, `ssCut`): the boarding (stripped,
rowed out, cut loose, the liner's shadow, hauled up), the stage and its MC, the rounds and their acts,
then the gun, Roke's payout and the boats home. Each raid hits its mark first try. **The count** rises
on a scoreboard card on screen; **the purse** is a card at each rung's close.

**Every flavour choice stays:** all the gauntlet dodges (Delph, Harrow, Coil, Trask, Ned, and the six
ways to lose to Roke); the deck's two links; "Tell him no, nicely" / "Tell him where he can put it";
Bite / Go limp; play to the crowd / play it cool, and which man first, at the raids; "Let him go
again" / "Let him sleep" at the berth.

**Files:** branch `shipsstores`, worktree `catalog-renpy-shipsstores`, folder `game/shipsstores/`,
prefix `shp_`.

## Art (generated, Vanripper only; I pick and check every image at full size)

**No Abarus set:** the catalog ending is `tsf`. Bodies by rung from `routes/shipsstores.json`
(rungs 1–3 a man, rung 3 wide-hipped and flat; rung 4 she with the breasts and the cock; 5–6 a
woman), black hair throughout, long only at rung 6. Rung 6 is drawn at the breast cap (step 8,
"huge, weighted up"), not past it. The paint (a red mouth, smudged black eyes) from rung 2, the black
corset written into each prompt that has it, the gold compass from rung 4. Multi-person acts draw
everyone in the act (watchers left out).

**PC sprites:** Jonah in a deckhand's shirt and canvas trousers (rungs 1–3), the corset and the paint
over the trousers (rungs 2–5), and the paint and the compass (rung 6).

**Cast sprites:** Roke (two faces), Guillam, Delph, Harrow, Coil, Trask, Ned.

**Backgrounds:** the squall at sea; the deck in rain and in sun; the ring round the mast; the bilge
(dark, and all lamps lit); the slop-chest corner; the liner's stage; the boat in the liner's shadow;
the galley; the helm; Roke's quarters; the mate's berth; the beach at dawn; the town harbour; a
day-cruise liner's deck.

**When:** after my ace passes. The script comes first.

## Added scenes

None in the story. **Stay and Go each play a scene** after the ending (owner, 2026-11-12: "Both get
a scene"), both consensual:
- **Stay ("Stay as stores"):** a later noon as stores: the boat, the stage, the count, Roke saying
  "Stores" instead of paying, and home to the bilge, where somebody is always awake.
- **Go ("One night, over the rail, home to town"):** the swim home; then, new writing: weeks later
  she buys a day-cruise ticket out of the harbour, the black ship comes at noon, and she walks up onto
  the stage herself.
