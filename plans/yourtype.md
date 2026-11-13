# yourtype in Ren'Py: the VN plan (draft for sign-off, 2026-11-12)

"My Best Friend Handed Me a Wish Ring and Only Ever Asked What My Type Was". Rewritten straight in
Ren'Py (it has no VN script in the catalog). The original is kept verbatim in
`catalog/docs/routes/vn-original/yourtype/` (twee, js, spec).

## What stays exactly as signed off (2026-10-25)

- Cast: Aaron Dorsey, 24 (the PC, a warehouse stock lead and an arguer; the name box stays, and the
  erasure takes whatever name you typed); Lyle Prewitt, 25, the best friend since the docks night
  shift, the only partner; Carly Briggs, 26, the stock cage, agrees with every cover story, never
  sexual; Kev Conway, 25, the pub, hits on you and leaves, touches nobody.
- The ring's two rules, from Lyle on day 1: wear it, picture yourself however you want, and that's
  what you are; it only works on whoever's wearing it. What he never says: the ring runs the picture
  whole, and changing back restores whatever you currently believe you are. Nobody explains either.
- The ladder (where "back to normal" restores to), in words every morning, never a number: smooth
  under your clothes; the jeans sit lower ("Dryer."); the top shelf needs the step; tanned, and
  Carly asks where you went; soft, small, wrong; *Normal: Brandi.*
- Lyle's asks, word for word, one a rung: none; "Don't you like busty girls?"; "I thought you liked
  the ditsy ones."; "Girls like you don't sit in the car."; "You don't have to keep switching back.";
  "It's up to you." And "So what's your type?", once a rung, mid-something-else.
- The cast's method: one link at rung 1 ("Just… a girl version of me"); the patch list at rungs
  2-3, in any order; "Just picture her." at rung 4; "Picture her. All of her." at rung 6.
- **The mind is never narrated.** It shows only in the probe answers, the alibi menus (three
  reasons it doesn't count, all that rung's), your lines shortening (the A/B/C pools) and the
  arguments you let go from rung 3.
- The name: "Brandi" from Lyle at rung 3, corrected twice, then not; the reach at rung 6, a letter
  at a time, until there's nothing to reach for. The old name never prints after it.
- The face: sworn off at rung 3 ("Not the face."), complimented at 5 ("I like that you kept it."),
  gone in the last cast at 6.
- The body: rung 1 plain (mousy brown, flat and puffy, the cock stays); 2 the chest, hips, waist, a
  fuller mouth; 3 the voice, smaller hands, blond, the tiny cock; 4 the whole picture, tan, and the
  front simply isn't in it (noticed after a full scene: "Huh. …Where'd— ha! Okay."); 5 the restore
  fails and you cast her back over it; 6 the face, the peak, nothing left to restore to.
- Every scene's act and order: 1 solo, twice, at the bathroom mirror; 2 his mouth on your cock after
  "Prove it, then."; 3 the first fuck, anal, your tiny cock bouncing; 4 after the pub, you ride him,
  the first vaginal; 5 after the truth, on your knees, then slow missionary; 6 the titjob, then bent
  over the kitchen counter by the key bowl (the one mandatory scene).
- One ending, "Your Type" (the traces, the probe, "You."), and its flavour epilogue: leave the ring
  on the nightstand, or put it in a drawer.
- Lyle never lies, never names a body part, never requests a change, never touches the ring after
  day 1, never asks for permanence. Lyle is the only partner. No ring lore, no hypnosis, no numbers
  (cup letters only), no dread or grief, no pain, never "on all fours".

## Consent: the non-con pass (owner, 2026-11-11: "manipulated by characters")

From the spec's "Non-con beats" (catalog 8ad708084). The force is Lyle, who wants his best friend a
slut because it's hot. The ring doesn't compel you; he works on you: the dares he turns round, the
questions he picks, the rules he never mentions. He talks you past every no, and **he still never
lies** (omission and framing only; his lint stands). Carly and Kev are levers he uses, never sexual.

| Rung | Scene | Register |
|---|---|---|
| 1 | solo at the mirror | as built |
| 2 | "Prove it, then." | non-con: he turns your dare round and doesn't stop where it ended |
| 3 | the first anal | non-con: he talks you past every no, and you pin it on the mood setting |
| 4 | after Kev: you start it, you ride him | **flip** (my reading of your answer; correct it if it's wrong) |
| 5 | after the truth | consensual, knowing |
| 6 | the kitchen counter (mandatory) | consensual |

- House rules: you protest out loud at rungs 2-3 (it's an argument, as always, and he wins it); the
  body betrays you; you're loud and begging by each scene's end. No tears, no menace, no pain;
  pinning is fine. No escape from a story scene.
- Lyle's "Yeah?" check before a new act is retired at rungs 2-3: he asks something else instead, a
  question that turns your last no into a dare ("You said it doesn't count, so what's the
  problem?"), and never a lie.
- The links that read as your yes at rungs 2-3 ("Spread your knees", "Pull him in") become his
  moves in the prose; where a menu stays, it picks how you argue (the alibi), never whether.
- Art: the PC sprites add a **protesting** face (rungs 2-3), and those frames show you mid-argument
  while the body goes along.

## How it plays (Ren'Py)

- **Linear days, as the route plays now:** Friday (the demo, the night cast, solo twice, the
  restore, "?" / "told you"); Saturday (Lyle sees it, the patches, the dare); Wednesday (the cage,
  the takeaway, the patches and the mood, "Brandi", the anal, the face; you sleep in her); Thursday
  (the restore, Carly, "Absolutely not." twice, "Just picture her.", the car, the pub, Kev, home,
  the ride); Friday (soft, small, wrong, twice; you call in sick; the evidence; the truth; the
  missionary; the "she" beat); a few easy days; Day 6 (the question, the mirror, the last cast, the
  reach, Lyle back, the counter, the coda); Day 7 the epilogue.
- **The HUD shows the weekday** (twinetesting-92's opt-in HUD line, landing on main now), since
  the prose names the days.
- **The patch list** becomes a Ren'Py menu that removes each picked patch, so you click through all
  of them in any order and each lands its pink line; the last lays the whole rung.
- **The reach** is a looping menu: one choice, "Reach for it", with the name losing a letter each
  pick, until "Reach for—" finds nothing. Then the name is Brandi.
- **The readout** is the morning's first line, as now.
- **The director scenes are written out** as beats (open, mid, peak, your climax, his), from
  yourtype.js's line pools (Lyle's combat lines and the A/B/C pools); rung 6's in full.
- **Not ported (as Red Lightning):** free play (the Docks door, the post-ending touch-ups and
  Lyle's visits, money). The epilogue keeps both choices as pictures and a closing line.
- **Lyle's lint carries over:** a test greps every line Lyle speaks for the body-part list and
  fails on a hit, as `verify-yourtype.py` does; the old name never prints after the reach.
- **Files:** branch `yourtype`, worktree `catalog-renpy-yourtype`, `game/yourtype/`; names
  prefixed `yt_`. Merged to main when its walks pass.

## Art (generated, Vanripper, free only; I pick, eye-check at full size; you review after)

- **PC sprites, 9 bodies:** "normal" three times (Aaron; rung 4's smaller and tanned; rung 5's
  soft, small, wrong) and the cast six times (rungs 1-6). Outfits: his own tee and jeans, work gear
  for the cage (hi-vis), the pub (what the cast arrives in), nude for the casts and the mirror.
  Faces: arguing, flustered, protesting, eager, blissed. About 95.
- **The face (owner, 2026-11-12: "Softened faces"):** rungs 1-5 draw an androgynous, boyish face
  under the cast's hair, easy to generate; the mismatch lives mostly in the prose. Rung 6 is a
  face that was never his.
- **Cast:** Lyle, 3 faces (easy, hungry, jealous at the pub); Carly, 2 (cheerful, puzzled); Kev, 1.
  Lyle's ninety seconds as a woman on day 1 is a frame, not a sprite.
- **Backgrounds (7):** the flat's lounge and couch, the bedroom and nightstand, the bathroom mirror,
  the kitchen counter and key bowl, Gannet Freight's stock cage, the pub car park (Lyle's car), the
  pub's high table by the front window.
- **Frames, about 100:** the demo (3, with the tell); each cast (rung 1-6) and each restore; solo
  twice (4); the "?" text; the patches (2 per rung); the dare and his mouth (5); the cage with
  Carly (3); the takeaway; "Brandi"; the anal (5); the face sworn off; the pub with Kev (3); the
  ride (5) and the noticing; the wrong mornings (2); the badge photo and the sick text; the
  evidence; the truth; the knees and the missionary (6); the mirror and the last cast (4); the
  reach (2); the titjob and the counter (6); the coda (the fridge photo, the badge, "You."); the
  ending; both epilogues.
- **Rulings that apply:** the cast's front is drawn as written (the tiny cock at rung 3, no pussy
  before rung 4's cast); rung 6's J is a cup letter in the prose, and the picture sits inside your
  step-8 cap; no red hair, no twin tails; blonde, tan and stacked is kept off borrowed's Delaney
  (blond, not golden).

## Added scenes

None proposed. Every beat the VN needs is already in the story.

## Questions for you

1. **The flip at rung 4** (my reading of "manipulated by characters": Lyle works on you at 2-3, and
   from the pub on you start it)? *Recommended: yes.*
2. **Lyle's "Yeah?" retired at rungs 2-3**, replaced by questions that turn your no into a dare,
   never a lie? *Recommended: yes.*
3. **The face:** draw Aaron's face on the cast body through rung 5, as the route's mismatch? It's
   the harder picture (NovelAI pulls a girl's face onto a girl's body). *Recommended: yes, and if a
   candidate can't hold it, a softened version of his face rather than a stranger's.*
4. **An Abarus alternate set** and **the epilogue marked** as the choice that decides the ending,
   as for the five? *Recommended: both.*

## Signed off (owner, 2026-11-12, about 12:30 am ET)

Every question above is answered:

- The rung 4 flip: **as proposed** (neckdown and yourtype both; notanlines' was the owner's pick).
- Faces: **softened** (androgynous, boyish faces under the hair; the mismatch lives mostly in the
  prose), for yourtype and neckdown.
- Everything else **as recommended**: the non-con rewording, the days, the hub's places as beats,
  an Abarus alternate set, the epilogue marked as the choice that decides the ending.
- Art waits: this chat is third in line for NovelAI pictures, so the scripts come first (pictures
  named in the script, a placeholder cover), as collar's did.

The plan stands otherwise as written. Built on its own branch and worktree; this file moves to
`game/yourtype/PLAN.md`.
