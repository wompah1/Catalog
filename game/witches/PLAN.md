# witches in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"I Was Sent In to Clear the Witches Out of the Old Infirmary, and Every Night One More Ailment Sticks". It's rewritten straight in Ren'Py, since it has no VN script in the catalog. The original is kept verbatim in `catalog/docs/routes/vn-original/witches/` (the twee, js, tools and spec).

## What stays exactly as signed off (2026-10-27)

- **Adaptation rules:** it's adapted from the package, not a port of the game. Every character is an adult with a stated age, and there's no school framing anywhere.
- **The cast:**
  - **Emrys Kettering, 24**, the PC. A slight, pretty night guard for Northcott Security. The depot lads call him Pretty, which he hates. He's dogged and comic: he reads the site rules out loud to witches. He's he/him to the last line of both endings, and keeps his cock.
  - **The coven** (violet eyes; horns or pointed ears):
    - **Bryony, 27:** sweet. She leads rung 1.
    - **Rowena, 29:** brash, and runs a book on everything. Rung 2.
    - **Cressida, 35:** dry, with spectacles on a chain. Rung 3.
    - **Elspeth, 25:** giggly, with a quill. Rung 4.
    - **Isolde, 33:** futa, speaks in one-word commands. Rung 5.
    - **Morgause, 41:** futa, the head of the coven, with horns and a matron's silver watch. Rung 6, mandatory.
  - **Prose only:**
    - **Rufus, 31:** the team lead. He turns up content in a belled collar at rung 4.
    - **Niall, 26:** a witch at rung 5. *"I said yes, Em."*
    - **The duty supervisor:** never looks up from her crossword.
- **The premise:** the old infirmary wing behind the hospital on Nightingale Street, where men go in after dark and don't come out. Every night Emrys loses one fight. Most of the ailments are gone by dawn; **one sticks for good**, on top of every one before it. Every dawn he wakes on the bench in the guard hut, and the coven has written that night's word in purple in the *Officer's condition* box of his incident report.
- **The ladder (the ailments that stick):**

  | Rung | Ailment | Witch | The night's kit (it fails) | The act |
  |---|---|---|---|---|
  | 1 | Charmed | Bryony | torch, radio, whistle, rock salt | she rides him on an iron ward bed |
  | 2 | In heat | Rowena | more salt, a second torch | she rides him in the porter's chair, past his first orgasm |
  | 3 | Shrunk | Cressida | a brine water pistol | on the nurses' desk, wrists pinned, his face in her breasts |
  | 4 | Sensitive | Elspeth | an extinguisher full of salt | facing away on the exam couch, his wrists ribboned, her finger in him |
  | 5 | Obedient | Isolde | a fertiliser spreader | bent over the bed rail: his first anal, and he comes untouched |
  | 6 | Witchmark | Morgause | nothing | the matron's canopy bed, his legs on her shoulders; the fork |

- **The body (Fem shelf, the cock kept, never a pussy):**
  - **rung 1:** himself;
  - **rung 2:** hairless from the neck down, soft skin, fuller lips;
  - **rung 3:** a little shorter and softer, the kit hanging off him, the cock a little smaller;
  - **rung 4:** slight shoulders, a narrow waist, a round arse, puffy nipples on a flat chest, hair to the shoulders;
  - **rung 5:** wide hips for his frame, thighs that touch, a lighter voice;
  - **rung 6:** long dark hair down his back, a puffy chest, and violet coming into his grey eyes ring by ring in the scene, his ears drawing to soft points.

  The Shrink rules hold: never carried or lifted, never "tiny", never a size comparison with a partner. No cup letters.
- **The canon lines and their owners:**
  - *"Another torch."* is Morgause's, at rung 1 and in End Witch's epilogue.
  - *"Nobody gets left in here"* is Emrys's (exactly once at rung 4, to Rufus).
  - *"Back in at ten, Kettering"* is the supervisor's, at each dawn from 2 to 6.
  - *"I said yes, Em"* is Niall's; *"Every one of us came in with a torch"* is Morgause's (both rung 5).
  - *"Admitted."* is Morgause's, at rung 6.
- **Two endings, decided by his last move in the last fight:**
  - **End Witch:** the ring closes. A hat in his size and the robe. A week on, a new Northcott team comes in and he blows the first one a kiss: *"Another torch."* Then Stay ("The coven's newest") or Go ("Days in town, nights in the wing").
  - **End Pet:** the ring never closes. The belled collar and pyjamas, in the day room beside Rufus. One close, no Go.
- **The rules:**
  - nobody explains anything (Morgause's one line at rung 5 is the whole truth);
  - nobody threatens and nobody's cruel;
  - the witches are delighted, and he's outraged, never frightened, never in tears;
  - no pain;
  - the blacklist holds;
  - the Witchmark is in his eyes and ears, never on his skin.

## Consent: the non-con pass (owner, 2026-10-27: non-con by magic, aware, resist-then-break, no flip)

The owner already ruled on this route, so the rewrite carries it as it stands. **The ailments are the force: his body betrays him, his will never does.** All six scenes are non-con, and **none ever flips**. What changes rung by rung is how much fight is left in the words:
1. furious and nonstop;
2. silent until the first moan breaks it;
3. muffled into her breasts;
4. no on every touch, a come on every touch;
5. begging because Obedient makes him;
6. no and please in the same breath.

Partners never ask. Hands and ailments only, no threats. And no amnesia: he remembers every night at dawn.

## How it plays (Ren'Py)

- **Six nights, one rung a night, no hub.** Each night:
  1. dawn on the bench at six: the report, the growth beat, *Action taken*, the supervisor;
  2. the day slept through;
  3. the fence at nine: the purple status line and that night's kit;
  4. the fight: the kit fails comically, *ting*, the word;
  5. the scene, then its last beat inside the act, then lights out.

  The day counter shows the real weekdays.
- **The lettered props are Ren'Py screens:**
  - **the incident report:** the purple column in a looping hand, one word under the last; *Action taken* in biro (scribbled out at 2, "Withdrew" at 3, "Engaged" at 4, blank with a doodled hat at 5, *Obedient* in his own hand at 6); and rung 2's *Description of hostile* for the gag;
  - rung 1's night log (KETTERING, 22:00);
  - the fence's purple status line;
  - **the ailment panel:** a *ting*, then the word alone. Rung 6 plays all five, then *Witchmark*.
- **The scenes are written out** as beats (open, mid, peak, his climax, theirs), with each witch's own lines and his rung's protest pool, and every gag kept. Rung 2's Silence is written in: no voice until the first moan.
- **The fork (DoL read it from his combat moves; Ren'Py has none):** a choice at the last stroke of rung 6, his own last move: *"Close your eyes and let it."* (End Witch) or *"Keep saying no."* (End Pet). It's marked as the choice that decides the ending. Rowena's book telegraphs it in the fiction (*"Hat if he says yes, like our Niall! Bell if he never does, like Rufus!"*), and *"The last ring hangs. It's waiting on you."* plays just before it. End Witch's Stay/Go is marked too.
- **Flavour choices**, which never decide whether:
  - one struggle menu in each scene (how he fights: shove, radio, site rules);
  - how he squares up at each fight;
  - what he writes under *Action taken* where the original lets him.
- **Not ported:** free play (the hospital notice, and the hut after the ending). The epilogues play as written and end the route.
- **Files:** branch `witches`, worktree `catalog-renpy-witches`, `game/witches/`; names prefixed `wit_`.

## Art (generated, Vanripper plus an Abarus set; free only; I pick, eye-check at full size; you review after)

- **The Abarus set is in** (your 1:56 pm rule: witches is a femboy route). Sprites, portraits and frames get one; backgrounds are shared.
- **PC sprites, 6 bodies** (one per rung), about 70:
  - **Outfits:**
    - the black Northcott kit (polo, cargo trousers, boots, the hi-vis), rungs 1–3;
    - the women's-cut kit, rungs 4–6;
    - nude;
    - End Witch's hat and robe;
    - End Pet's belled collar and pyjamas.
  - **Faces:** dogged, outraged, flushed, breaking.
  - **End Witch:** violet eyes and pointed ears. Everywhere else, grey eyes and his own ears.
- **Cast:** the six witches (2 faces each: amused, intent), Rufus in his collar, and Niall in his robe. 14 in all.
- **Backgrounds (10):**
  - the fence and the guard hut;
  - the corridor;
  - Ward 4;
  - the linen room;
  - the nurses' station;
  - the day room;
  - the exam room;
  - the side ward;
  - the matron's office;
  - the hut bench at dawn.
- **Frames, about 120:**
  - each fight's kit failing and its ailment landing;
  - each scene (4–5 frames);
  - each dawn's bench and report;
  - the Shrink beat in the kit;
  - Rufus in the day room;
  - Niall at the side ward door;
  - the hat and the collar on their hooks;
  - the violet coming in ring by ring;
  - both endings and the epilogue.
- **Rulings that apply:**
  - the shrink is drawn as a slight adult man, never small beside a partner;
  - no pussy, ever;
  - nothing inside him before rung 4's finger;
  - no futa cock on the page before Isolde opens her robe;
  - everyone has adult faces and bodies;
  - the infirmary is drawn as a derelict Victorian hospital wing, never a school.

## Added scenes

None proposed. Every beat the VN needs is already in the story.

## Questions for you

1. **Consent:** carry the 2026-10-27 pass as ruled (all six non-con, no flip)? *Recommended: yes.*
2. **The fork as a marked choice at the last stroke** (*"Close your eyes and let it."* / *"Keep saying no."*), in place of DoL's read of his combat moves? *Recommended: yes.*
3. **A flavour struggle menu in each scene** (how he fights, never whether)? *Recommended: yes.*
4. **The report, the night log, the status line and the ailment panel drawn by Ren'Py** as screens? *Recommended: yes.*
5. **Mark End Witch's Stay/Go** as an ending choice too? *Recommended: yes.*

## Signed off (owner, 2026-11-12, about 2:30 pm ET)

Every question above is answered with its recommendation ("All as recommended"): the 2026-10-27 pass as ruled (all six non-con, no flip); the fork as a marked choice at the last stroke; a flavour struggle menu in each scene; the props as Ren'Py screens; End Witch's Stay/Go marked. Vanripper plus an Abarus set.

Built on branch `witches` in `catalog-renpy-witches`; this file moves to `game/witches/PLAN.md`.
