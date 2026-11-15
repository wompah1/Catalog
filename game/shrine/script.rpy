## THE SOURCE: shrine's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, rungs-late.twee, ending.twee), written as beats; the director
## scenes and the solo loop are in scenes.rpy. The original is in catalog/docs/routes/vn-original/
## shrine/. Seven days, one rung each, chained: dawn (the growth beat and the basin), the day (the
## maiden's chore, driven by whatever she has), dusk (the guardians step down) and night (the rung's
## scene). The gate turns you round until the ending. Flint says two words; Slate never stops.

## ---- DAY 1: the moor, the prayer, the robes; rung 1 (Shrine Opening, Pillar, Gate Turn) ----------

label shr_opening:
    $ shr.fit = "own"
    $ vn_enter(bg="shr_moor", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_vlog")
    "The moor is heather and wind and nothing else, all the way out to the sky."
    "You've got your phone up on a selfie stick and your hood up against the wind, and you're walking backwards up a hillock, talking."
    shr_you "\"—and THIS is the Pillar of the Heather. Locals say it's cursed. Locals say if you pray at it... something prays {i}back{/i}.\""
    "No locals said that. You made it up on the bus. The channel's called {i}Haunted Britain with [shr_pc_name] Kemp{/i}, nobody watches it, and every comment is your mum."
    show cg shr_gate_reveal onlayer cgl
    "At the top of the hillock there's a stone pillar, waist high, carved all over with writing nobody's read in ages. And behind it—"
    "You lower the stick."
    "Behind it there's a gate. A big red one: two posts, two crossbeams, the paint bright as a postbox, standing on its own on the hilltop. On top of each post sits a stone fox with its tail curled round its feet. The left one has a key in its teeth. The right one has a round stone jewel."
    "You'd swear it wasn't there from the road."
    shr_you "\"Okay. Okay, that's actually creepy. That's {i}content{/i}.\""
    "Through the gate a gravel path runs up to a little wooden shrine with a curved roof. A bell rope. A stone basin brimming with water. A paper lamp in a window. All of it swept and neat and completely empty."
    show cg shr_kneel_bit onlayer cgl
    shr_you "\"Right. The bit.\""
    "You prop the phone in the heather, angled up at you, and get down on your knees in front of the pillar with your hands pressed together and your best spooky face on."
    shr_you "\"O spirit of the hill. Grant this humble channel... {i}subscribers{/i}.\""
    "You crack up. You can't help it. You're still laughing when you close your eyes.\n{size=-5}{color=#ff8fa3}▸ Pray for the camera{/color}{/size}"
    $ vn_pass(5)
    jump shr_pillar

## Day 1, the prayer: the robes and the fox mask at the pillar's foot; "Oh, finally." She takes your
## hands, and they strip you from under the robes. Rung 1 lands then and there: the body hair.
label shr_pillar:
    $ vn_enter(bg="shr_moor", pc="furious", pc_tag="shr_pc", cast=[], cg=None)
    "The wind drops."
    "All of it, all at once. The heather stops hissing. Somewhere very close, a bell rings once, and nobody's touched the rope."
    show cg shr_robes_found onlayer cgl
    "When you open your eyes, there's a folded set of clothes at the foot of the pillar. A white top with wide sleeves, a red pleated skirt like trousers, folded square and neat as a shop's. On top of them sits a mask: a small white fox face, red paint at the cheeks and the brow, smiling a smile you don't like at all."
    shr_you "\"Ohhh, that's {i}perfect{/i}. Look at this. Shrine maiden robes. Nobody's going to believe this.\""
    "You tell the phone."
    hide cg onlayer cgl
    $ shr.fit = "robes"
    "You shake the robes out. They're warm, like somebody just took them off. You shrug them on over your hoodie, laughing, and tie the sash any old how, and you put the mask on your head, pushed up like a festival mask. It sits there as if it was made for your skull."
    show cg shr_mask_on onlayer cgl
    "You strike a pose. Peace sign."
    shr_you "\"Shrine maiden [shr_pc_name], reporting for d—\""
    shr_lady "\"Oh, {i}finally{/i}.\""
    hide cg onlayer cgl
    "You freeze."
    "That wasn't you. It wasn't the wind. It was a woman's voice, low and lazy and absolutely delighted, and it came from right behind your eyes."
    shr_lady "\"Oh, look at you. Look at all of you. Do you know how long it's been since anybody put that mask on? Ages, maiden. Ages and ages and {i}ages{/i}.\""
    shr_you "\"Who— who said that—\""
    "You spin round. Heather. The gate. Two stone foxes, very still."
    shr_lady "\"Don't be dull. I'm in {i}here{/i}.\""
    show cg shr_hands_sash onlayer cgl
    "And your hands move."
    "You didn't move them. They just go, up to the sash, and pick the knot apart, and you watch them do it like they belong to somebody standing behind you."
    shr_you "\"Hey. {i}HEY{/i}—\""
    $ shr_take(1)
    shr_lady "\"Oh, hands. I'd forgotten hands.\""
    "She sighs it, like somebody sinking into a hot bath."
    "Your hands slide in under the robe. They unzip your hoodie and peel it off your arms from inside the sleeves, slick as a conjuror, and drop it in the heather. Then they go for your belt."
    shr_you "\"Stop— STOP— those are my— get OFF my {i}BELT{/i}—!\""
    show cg shr_strip onlayer cgl
    vn_sfx "{i}Clink.{/i} Button. {i}Zzzip.{/i}"
    "Your jeans and your boxers go down together, and you hop, and your trainers come off, and your socks, and then you're standing on a hilltop in nothing but a shrine maiden's robes, with the wind up your skirt, screaming at your own wrists."
    shr_you "\"Give them BACK— they're MINE— give me my HANDS back—!\""
    shr_lady "\"Shh. Shh. Oh, you're so {i}loud{/i}. I like that.\""
    hide cg onlayer cgl
    show cg shr_shiver onlayer cgl
    "{color=#ff5fb8}Then the shiver hits.{/color}"
    $ shr_body(1)
    "{color=#ff5fb8}It starts at your scalp and pours all the way down to your toes, warm, like stepping into a bath, and everywhere it goes, the hair {i}goes{/i}. Your stubble sheds off your jaw into the robe's collar. The hair on your chest, your arms, your legs, the whole lot down there: it just lets go, all of it, in one long shudder, and the wind carries it off over the heather.{/color}"
    "{color=#ff5fb8}Your hands, hers, run over your bare jaw. Your bare chest. Your bare, smooth thighs, up under the skirt. Your skin's gone warm and tight and soft as the inside of a cup, and when her fingertips brush your nipples they're so {i}tender{/i} you yelp.{/color}"
    show shr_pc flushed
    shr_you "\"{i}Ahh{/i}— what did you— what did you DO— {i}ohh{/i}—\""
    shr_lady "\"Ugh, hair. Off.\""
    show shr_pc furious
    shr_you "\"It's the {i}cold{/i}! It's just the COLD!\""
    "You tell the whole moor, at the top of your voice."
    show shr_pc flushed
    "{color=#ff5fb8}Your own hands rub slow circles on your smooth chest until you're moaning out loud on the hilltop, and your lashes feel heavy when you blink, darker, long enough to see. Your lips are buzzing. You lick them, and the moan that comes out of you is so loud it echoes off the gate.{/color}"
    shr_lady "\"Mm. There. Now you're {i}soft{/i}.\""
    hide cg onlayer cgl
    "Then she lets go, and your hands drop to your sides, yours again, shaking."
    show shr_pc furious
    "You don't think. You bolt.\n{size=-5}{color=#ff8fa3}▸ Leg it down the hill{/color}{/size}"
    $ vn_pass(5)
    jump shr_gate_turn

## THE GATE: walk out between the stone foxes and you're walking back in. Tried on day 1, more and
## more furious, never offered again. The phone dies here and stays dead.
label shr_gate_turn:
    $ vn_enter(bg="shr_gate", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_gate_in")
    "You go down the hillock flat out, robes flapping round your bare legs, heather whipping your shins—"
    "—and you're walking in under the red gate."
    "Between the two stone foxes. Onto the gravel. Up the path to the shrine."
    "You stop dead. You turn round. The gate's behind you, open, and the moor's out there through it, heather all the way to the sky."
    shr_you "\"No. No, no, no.\""
    "You walk out through it. Carefully. One foot, then the other, right between the posts."
    "And you're walking in under the red gate. Onto the gravel. Up the path."
    shr_you "\"NO!\""
    show cg shr_gate_sprint onlayer cgl
    "You sprint at it. You go through it so fast your skirt flies up round your waist, and you're yelling the whole way, and you come out the other side—"
    "—{i}in{/i}. Onto the gravel. The bell rope sways, as if somebody's laughing."
    shr_lady "\"Ha! Oh, again. Do it again. Your face, maiden.\""
    shr_you "\"Let me OUT! This is— this is false imprisonment! I've got a CHANNEL!\""
    show cg shr_phone_dead onlayer cgl
    "Your phone's lying on the gravel by the basin, somehow, still recording. You snatch it up."
    shr_you "\"Look. LOOK at this, this is real, everyone's going to—\""
    vn_sfx "{i}Bloop.{/i}"
    "The screen goes black. You jab the button. You hold it down. You shake it. Nothing. Not even the empty battery."
    shr_lady "\"Oh, put the little lamp away. There's nobody in it.\""
    hide cg onlayer cgl
    "You stand on the gravel in your stolen robes with your dead phone in your hand, breathing hard."
    shr_you "\"Who ARE you?\""
    shr_lady "\"Oh, don't ask me that. Names are for things that can leave.\""
    show cg shr_foxes_still onlayer cgl
    "The two stone foxes sit on their posts above you. Big ones, now you're up close: bigger than a man crouching. The left one, with the key in its teeth, is all blunt grey weight. The right one, with the jewel, has its head cocked like it's about to say something smart."
    "They're very, very still."
    shr_lady "\"Don't stare, it's rude. They wake at dusk.\""
    shr_you "\"They {i}what{/i}—?\""
    hide cg onlayer cgl
    "She doesn't answer. She just hums, in your head, very pleased with herself, while the sun slides down the sky.\n{size=-5}{color=#ff8fa3}▸ Wait for dusk{/color}{/size}"
    $ vn_until(19)
    jump shr_hands

## Rung 1, the lead-in: the maiden's room, night 1. Not the guardians, not tonight. Then the robe, and
## her hands find your cock, and the possessed masturbation starts.
label shr_hands:
    $ vn_enter(bg="shr_gate_dusk", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_dusk_foxes")
    "Dusk. The sky goes red, then purple, then dark, and the stone foxes on the gate posts just sit there, black against it, very still."
    "You watch them for ages. Nothing."
    shr_lady "\"Not tonight. Tonight's for hands. I want to remember hands properly first.\""
    "She says it almost kindly."
    $ vn_enter(bg="shr_room", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_room_sit")
    "It's getting cold, and the robe's thin, and there's a lamp lit in the little room behind the worship hall that nobody lit. So you go in. A futon on clean boards. A paper lamp. A shelf with a cup of water on it. You sit on the edge of the futon with your knees together and your dead phone in your lap."
    shr_you "\"I'm not doing anything. I'm just going to sit here. I'm going to sit here till morning and then I'm going to walk out.\""
    shr_lady "\"Mm. Course you are.\""
    "Your hands put the phone down."
    shr_you "\"No— no, hang on—\""
    $ shr.fit = "open"
    show cg shr_hands_open onlayer cgl
    "They pick the sash open. They push the robe off your shoulders, slow, and lay it open down your front, and there you are in the lamplight, smooth all over, soft-skinned, your nipples tight, your cock already half-hard on your thigh and getting harder while you watch."
    show shr_pc flushed
    shr_you "\"Why is it— why's it doing {i}that{/i}—\""
    shr_lady "\"Because I'm looking at it. Oh, I'd forgotten these too.\""
    "She purrs it."
    show cg shr_hands_stroke onlayer cgl
    "Your right hand wraps round it."
    show shr_pc furious
    shr_you "\"{i}HEY{/i}—!\""
    show shr_pc possessed
    "Your hand gives it one long, slow, perfect stroke from the root to the tip, thumb dragging over the head, and your whole body jerks, and a moan comes out of you so loud the paper lamp shivers.\n{size=-5}{color=#ff8fa3}▸ Hold them still{/color}{/size}"
    jump shr_hands_solo

## The solo scene's finish: all over your own stomach, loud; "Oh, I'd forgotten that."
label shr_hands_finish:
    $ vn_enter(bg="shr_room", pc="possessed", pc_tag="shr_pc", cast=[], cg="shr_solo_cum")
    shr_you "\"No— no no NO— don't you— {i}don't you DARE{/i}— {i}AHH{/i}—!\"" with vnfx("shake")
    "Both your hands, hers, pump you through it fast and tight, and you arch right up off the futon, and you come so hard you shout the shrine down."
    vn_sfx "{i}Splt.{/i}"
    "Across your stomach. {i}Splt. Splt.{/i} Up your chest, hot and thick, pooling in your navel, and your hands just keep wringing it out of you, slow now, savouring, until you're twitching and gasping and there's nothing left."
    show shr_pc flushed
    shr_you "\"{i}Ahh{/i}— {i}ahh{/i}— stop— it's too— I've already— {i}ohh{/i}—\""
    "They don't stop. Not straight away. Your left hand cups your balls and squeezes, gently, and your right keeps stroking, slow and slippery, through every aftershock, your thumb rubbing circles under the head where you're so sensitive it's like being touched with a live wire."
    "You kick. You writhe. You moan into the lamplight with your back arched and your toes curled and your hips humping up into your own fist, and the last of it dribbles out over your knuckles."
    shr_lady "\"Mm. Every drop. Waste not.\""
    show cg shr_solo_after onlayer cgl
    "Your hand comes up off your cock, glistening, and turns itself over in front of your face so you can see. Then it smears the whole sticky mess slowly across your smooth chest, round and round your tender nipples, until you're shiny with it and whimpering."
    show shr_pc furious
    shr_you "\"You're— you're {i}disgusting{/i}—\""
    shr_lady "\"I'm thorough.\""
    hide cg onlayer cgl
    "Then they let go."
    show shr_pc dazed
    "Your arms flop down onto the futon. Yours again. You lie there in the lamplight with your robe open and your stomach a mess, panting at the ceiling."
    shr_lady "\"Ohhh. Oh, I'd forgotten {i}that{/i}.\""
    "She sighs it, long and low and blissed, right behind your eyes."
    shr_you "\"Get out. Get out of my head.\""
    "You croak it."
    shr_lady "\"No. Tomorrow, legs.\""
    "She sounds like she's stretching.\n{size=-5}{color=#ff8fa3}▸ Lie there{/color}{/size}"
    $ vn_pass(10)
    jump shr_night_one

label shr_night_one:
    $ shr.fit = "robes"
    $ vn_enter(bg="shr_room", pc="dazed", pc_tag="shr_pc", cast=[], cg="shr_night_one")
    "You don't wipe it off. You can't be bothered. You pull the robe shut over the mess and lie on your side, facing the paper door, and you swear at her, quietly, until you run out of words."
    "She hums in your head. A lullaby, maybe. Something very old."
    call vn_night(7)
    jump shr_dawn_two

## ---- DAY 2: rung 2, your legs (Shrine Dawn 2, Day 2, Legs) ---------------------------------------

## Row 2 at waking: nipples puffy over the start of a swell, the waist dipping, the voice lighter, the
## cock a size down; gold eyes and fangs. "It's the robes." The basin: her eyes behind yours.
label shr_dawn_two:
    $ vn_enter(bg="shr_room", pc="dazed", pc_tag="shr_pc", cast=[], cg=None)
    "You wake on the futon with the paper door glowing and the robe twisted round your waist, and for one lovely second you think you dreamed it."
    shr_lady "\"Morning, maiden.\""
    show shr_pc furious
    shr_you "\"Oh, {i}no{/i}.\""
    $ shr_body(2)
    show cg shr_dawn2_nipples onlayer cgl
    "{color=#ff5fb8}You sit up, and the robe drags across your chest, and you gasp.{/color}"
    "{color=#ff5fb8}Your nipples. They're {i}puffy{/i}. Swollen up soft and pink over the start of a little swell, a proper cup's worth of tender, and the rough cotton dragging over them sends a bolt straight down to your cock.{/color}"
    show shr_pc flushed
    shr_you "\"{i}Ahh{/i}— what— what is— {i}hnn{/i}— why are they so—\""
    "{color=#ff5fb8}You grab them to make them stop. That's worse. That's {i}so{/i} much worse. You squeeze and they squish, and you moan out loud in the little room, high and breathy, and you don't recognise the noise. Your voice has gone up. Lighter. Softer round the edges.{/color}"
    "{color=#ff5fb8}You shove the robe down to look. Your waist's dipped in, a little, like somebody pinched it. The line from your ribs to your hips has gone soft and curved. And your cock, lying on your thigh, is smaller. Definitely smaller. A whole size gone in the night.{/color}"
    shr_lady "\"Better. You were all elbows.\""
    show shr_pc furious
    shr_you "\"It's the {i}robes{/i}. It's these stupid robes rubbing!\""
    "You tell her, at full volume, in your new light voice."
    show cg shr_dawn2_fangs onlayer cgl
    "{color=#ff5fb8}You run your tongue over your teeth to steady yourself, and it catches. Two points, either side, sharp as pins. Fangs. You poke one with your tongue and squeak, and she laughs so hard in your head the lamp seems to flicker.{/color}"
    "{color=#ff5fb8}Your fingers, when you rub your face, are quick and clever, and your thighs press together under the robe on their own, like they've learned a trick. Your lips are so full and buzzing that every breath tingles on them.{/color}"
    $ vn_enter(bg="shr_basin", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_basin2")
    "Outside, the stone basin brims with water, flat as glass. You lean over it to splash your face, and stop."
    "Your face is finer. Smaller nose, softer chin, your mouth plumped up pink. Your eyes have gone gold, bright amber-gold, sharp at the edges. And behind them, under them, in the water, there's another pair of eyes. Red as lamp glass. Open. Looking up at you from inside your own reflection."
    "You jerk back. When you look again, they're still there."
    shr_lady "\"Don't splash me.\""
    show screen shr_basin(2)
    "The water holds still.\n{size=-5}{color=#ff8fa3}▸ Sweep the yard{/color}{/size}"
    hide screen shr_basin
    $ vn_until(9)
    jump shr_day_two

## The chore with her hands: sweeping, with hands that won't stop at the floor. At noon she takes
## your legs: "Walkies, maiden."
label shr_day_two:
    $ vn_enter(bg="shr_yard", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_sweep")
    "There's a broom by the worship hall's step, and the gravel's covered in leaves that weren't there last night. You don't decide to pick the broom up. Your hands do."
    shr_lady "\"A maiden sweeps. Every morning. Go on.\""
    vn_sfx "{i}Shff. Shff. Shff.{/i}"
    "Your hands sweep. Neatly, briskly, like they've done it every morning for ever. You just stand there and get dragged along behind the broom."
    shr_you "\"I'm not your maiden. I'm a {i}content creator{/i}.\""
    shr_lady "\"Mm.\""
    show cg shr_sweep_grope onlayer cgl
    "Then your left hand lets go of the broom, slides inside your robe, and squeezes your puffy nipple."
    show shr_pc flushed
    shr_you "\"{i}Ahh{/i}— hey— the FLOOR, the floor's down THERE—\""
    "It rolls the nipple between finger and thumb, slow, while your right hand keeps sweeping, perfectly calm, as if nothing's happening. You're making noises at the leaves. Your knees are shaking. Your cock's tenting the red skirt."
    shr_lady "\"I'm sweeping. Aren't you?\""
    "She says it innocently."
    "By the time the gravel's clean you've been groped in front of the basin, behind the bell rope and at the foot of the gate, under the blank stone eyes of both foxes, and you've moaned at every one of them. You lean on the broom panting, flushed to the ears, your little cock dribbling into the skirt."
    hide cg onlayer cgl
    "The sun climbs to the top of the sky."
    $ vn_until(12)
    $ shr_take(2)
    show cg shr_skip onlayer cgl
    "And your legs go."
    "Not out from under you. {i}Away{/i}. One knee lifts, then the other, and you're walking, and you didn't tell them to. You're walking round the worship hall. You're walking past the basin. You're walking at a {i}skip{/i}."
    shr_lady "\"Walkies, maiden.\""
    show shr_pc furious
    shr_you "\"Put me DOWN— stop— those are my LEGS— these are MY LEGS—!\""
    "Skip, skip, skip, round the shrine and down to the gate and up to the bell rope and round again, robe flapping, nipples rubbing bright pink on the cotton every bounce, you yelling the whole way and her humming a skipping song in your skull."
    shr_lady "\"Oh, I've {i}missed{/i} legs.\""
    hide cg onlayer cgl
    "She skips you all afternoon.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump shr_legs

## Rung 2, the lead-in: she walks you down to the gate; the stone warms and Flint and Slate step
## down. "Gate's shut." "Evening, Lady. Brought him down again?" Your hands go out to both of them.
label shr_legs:
    $ vn_enter(bg="shr_gate_dusk", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_gate_walk")
    "Dusk. Your legs walk you down the gravel to the gate, nice and slow, hips swaying, and stop you right between the posts."
    shr_lady "\"Walkies, maiden. Look up.\""
    "You look up."
    show cg shr_stone_warms onlayer cgl
    "The stone's going warm. You can see it happen: the grey blushing up from the posts like a fire's been lit inside them, the curl of the stone tails loosening, the carved ears twitching. The key in the left one's teeth clinks."
    "And they step down."
    hide cg onlayer cgl
    show cg shr_step_down onlayer cgl
    "Two men. Big men, barefoot on the gravel either side of you, in loose dark trousers and nothing else. Grey-streaked hair, gold eyes, human faces. And on top of their heads, fox ears, tall and grey, and behind them, swinging, two big grey fox tails."
    hide cg onlayer cgl
    show shr_flint flat at vn_cast_slot
    "The left one is huge and blunt and older, a man of about forty, built like the gate post he just got off. The key hangs round his neck on a red cord. He looks at you, all of you, robes and soft face and gold eyes, and says:"
    shr_flint "\"Gate's shut.\""
    hide shr_flint
    show shr_slate grin at vn_cast_slot
    "The right one's leaner, maybe thirty-five, with a crooked grin and the jewel on a cord round his throat. He leans on the post and looks you up and down, slow."
    shr_slate "\"Evening, Lady. Brought him down again?\""
    $ shr_lady_name = "The Lady"
    "Not to you. To her."
    shr_lady "\"Flint. Slate. Oh, look at you both. Oh, {i}two{/i}.\""
    "She's practically purring."
    shr_you "\"Who the hell are— are you— are you the STATUES—\""
    show cg shr_hands_both onlayer cgl
    "Your hands go out."
    "Both of them. One to each man. Your left hand lands flat on Flint's stomach and slides straight down the front of his trousers, and your right goes round Slate's hip and grabs his arse, and you're screaming at them, at her, at your own fingers."
    shr_you "\"That's not ME— I'm not doing this— those are MY HANDS, get them OFF him—!\""
    shr_slate "\"Don't look at me. She's the one doing it.\""
    "He says it cheerfully."
    "Flint's cock fills your left hand, heavy and hot and getting bigger, and your fingers close round it and start to stroke. Slow. Expert. Like they've done it before. Your hand barely fits round him."
    shr_lady "\"Oh, he's big. He was always big.\""
    "Slate steps in behind you. You feel the heat of him all down your back, and his hands on your hips, and then the red skirt's lifted at the back, and something thick and hot slides up between your bare thighs from behind, right under your balls."
    shr_you "\"{i}Hhh{/i}— no— NO— not there— get it OUT of my—\""
    "And your thighs squeeze."
    "You didn't do that. They just clamp, tight, soft, round his cock, and he groans into your neck, and your legs, hers, hold you right there."
    shr_slate "\"Look at that. She's got your legs now.\"\n{size=-5}{color=#ff8fa3}▸ Squeeze{/color}{/size}"
    jump shr_legs_sex

## Rung 2's finish: both finish on you. Back up onto the posts as flesh, watching all night.
label shr_legs_after:
    $ vn_enter(bg="shr_gate_dusk", pc="flushed", pc_tag="shr_pc", cast=[], cg="shr_legs_cum")
    "Slate comes with a laugh in his throat, grinding up between your squeezed thighs, and it pumps out hot under your skirt, all down the insides of your legs and up over your belly."
    show cg shr_legs_flint_cum onlayer cgl
    "And Flint, in your fist, just grunts. Once. Your hand speeds up on him, hers, wringing, and he comes all over your fingers, and keeps coming, thick and hot, dripping off your wrist into the gravel, and your other hand comes round to catch the rest."
    show shr_pc furious
    shr_you "\"Ugh— {i}ugh{/i}— it's all OVER me— it's on my {i}hands{/i}—\""
    show cg shr_legs_hands onlayer cgl
    "Your hands don't care. They come up in front of your face, dripping, and turn themselves over, slow, so you can see every sticky string between your fingers."
    show shr_pc flushed
    "Then your legs squeeze your thighs together on the wet Slate left there, and rub, and you moan at the slippery feel of it, and your own cock bobs under the skirt, so hard and so ignored that it's drooling."
    shr_you "\"Touch it. Just— just touch it, just once—\""
    "You beg her. You can't believe you're begging her."
    shr_lady "\"No. Not tonight. Tonight was for them.\""
    "She says it cheerfully. Then, blissed out:"
    shr_lady "\"Our hands. Oh, both of them. Good. Good lads.\""
    hide cg onlayer cgl
    "You stand between the gate posts in a dripping robe with your thighs sticky and your cock rock stiff and untouched, and your legs won't let you sit down."
    show shr_slate grin at vn_cast_slot
    "Slate kisses the back of your neck."
    shr_slate "\"Night, Lady. Night, him.\""
    hide shr_slate
    show shr_flint flat at vn_cast_slot
    "Flint takes your sticky wrist, turns it over, looks at it. Then at you."
    shr_flint "\"Gate's shut.\""
    "He says it again, and it sounds almost sorry."
    hide shr_flint
    show cg shr_posts_watch onlayer cgl
    "They climb back up onto the posts. They don't go back to stone; they just crouch up there in the dark, flesh, tails curled round their feet, gold eyes shining, watching you."
    "Your legs walk you back to the maiden's room at a skip.\n{size=-5}{color=#ff8fa3}▸ Back to the maiden's room{/color}{/size}"
    $ vn_pass(10)
    jump shr_night_two

label shr_night_two:
    $ vn_enter(bg="shr_room", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_night_two")
    "You lie on the futon with your sticky thighs pressed together and your hands, your own, clamped between them, because if you let go of them she'll use them."
    shr_lady "\"Tomorrow, I'd like your mouth.\""
    "She murmurs it."
    shr_you "\"No.\""
    shr_lady "\"I wasn't asking, sweetheart. I was telling you so you'd have something to think about.\""
    "You think about it. All night."
    call vn_night(7)
    jump shr_dawn_three

## ---- DAY 3: rung 3, your mouth (Shrine Dawn 3, Day 3, Mouth) --------------------------------------

## Row 3: small soft breasts that bounce, hips and arse rounding, hair to the shoulders and WHITE as
## hers, the voice up a step, the cock small; the fox ears. "It's HER." -- the last excuse.
label shr_dawn_three:
    $ vn_enter(bg="shr_room", pc="dazed", pc_tag="shr_pc", cast=[], cg=None)
    "Something tickles your neck. You swat at it in your sleep. It's hair."
    $ shr_body(3)
    show cg shr_dawn3_bounce onlayer cgl
    "{color=#ff5fb8}You sit bolt upright, and your chest {i}bounces{/i}.{/color}"
    show shr_pc flushed
    shr_you "\"{i}Ahh{/i}—!\""
    "{color=#ff5fb8}Breasts. Small, soft, round little breasts, sitting up high under the robe with your puffy nipples on top, and when you jerk they {i}jiggle{/i}, and the jiggle goes all the way down your spine. You grab them. They fill your palms, warm and squishy, and you moan so loud the paper door rattles.{/color}"
    shr_you "\"Oh god— oh {i}god{/i}— they're— {i}hnngh{/i}— they're SO—\""
    "{color=#ff5fb8}Your hips have gone round under your hands. Your arse is round, too, plump and high, filling the futon under you, and your thighs press together all the way up now, soft against soft. Your jaw, when you clutch your face, is smooth and soft and small.{/color}"
    show cg shr_dawn3_hair onlayer cgl
    "{color=#ff5fb8}And the hair. It's all round your shoulders, long and loose and silky. You pull a lock round in front of your eyes.{/color}"
    "{color=#ff5fb8}It's white. Snow white. Her white.{/color}"
    show cg shr_dawn3_ears onlayer cgl
    "{color=#ff5fb8}Something moves on top of your head.{/color}"
    "{color=#ff5fb8}You reach up, shaking, and touch it, and it flicks under your fingers. An ear. A big, soft, pointed ear, sticking up out of your white hair, and another one beside it, white-tipped and silky and twitching at every sound.{/color}"
    shr_lady "\"Ha! Oh, those are {i}sweet{/i}.\""
    "She laughs, and both your new ears flick at the noise of her."
    show shr_pc furious
    shr_you "\"It's HER. It's not the cold, it's not the robes, it's {i}HER{/i}, it's YOU, you DID this—!\""
    "You tell the room. Your voice cracks up another step, high and pretty."
    shr_lady "\"Yes.\""
    "She agrees happily."
    show shr_pc flushed
    "{color=#ff5fb8}You lick your lips. Your mouth's watering. It's been watering since you woke up, wet and hungry and so sensitive that your own tongue brushing your lips makes you shiver. Your fingers stroke your new ears without asking you, quick and sure. Under the skirt, your cock is small now, small and stiff and drooling, and nobody's looking at it but you.{/color}"
    hide cg onlayer cgl
    "You don't make any more excuses. There's no point. You know exactly who's doing it."
    $ vn_enter(bg="shr_basin", pc="dazed", pc_tag="shr_pc", cast=[], cg="shr_basin3")
    "At the basin you don't splash. You just look."
    "A white-haired face with gold eyes and a soft pink mouth and white fox ears. And behind it, rising over your ears, two more ears, white and tall, and her red eyes, smiling."
    show screen shr_basin(3)
    "The water holds still.\n{size=-5}{color=#ff8fa3}▸ The bell rope{/color}{/size}"
    hide screen shr_basin
    $ vn_until(9)
    jump shr_day_three

## The chore with her legs: the bell rope, at a skip.
label shr_day_three:
    $ vn_enter(bg="shr_yard", pc="furious", pc_tag="shr_pc", cast=[], cg=None)
    shr_lady "\"A maiden rings the bell. Every morning. So the hill knows she's here.\""
    shr_you "\"The hill doesn't care.\""
    shr_lady "\"The hill cares very much.\""
    show cg shr_bell onlayer cgl
    "And you're off. Skip, skip, skip, across the gravel, white hair flying, your new little breasts bouncing in the robe with every hop, {i}boing, boing, boing{/i}, all the way to the bell rope."
    show shr_pc flushed
    shr_you "\"Oh— no— {i}ahh{/i}— it's the BOUNCING— make it stop BOUNCING—!\""
    vn_sfx "{i}CLANG.{/i}" with vnfx("shake")
    "Your hands grab the rope. The bell goes off right over your head and your ears fold flat on their own."
    shr_lady "\"Again.\""
    show cg shr_bell_tongue onlayer cgl
    vn_sfx "{i}CLANG.{/i}"
    "Skip back to the basin. Skip back to the rope. {i}CLANG.{/i} Every skip jiggles your tits, every jiggle drags your nipples over the cotton, every drag goes straight down to your little cock, and before long you're ringing the bell with your tongue out, panting, moaning at the top of every hop."
    shr_lady "\"There. Now the hill knows.\""
    "Then she skips you round the shrine anyway, for fun. Up the steps of the worship hall and down again. Round the basin. Down to the gate and up to the gate and round the gate posts, in a circle, under the stone foxes, so close your new tits brush the warm red paint."
    "Your ears flop. Your skirt flies. Your little cock bounces and drips and you're moaning at every landing, and somewhere in the middle of it you notice your mouth's hanging open, wet and pink, and your tongue's out, and you can't remember putting it there."
    shr_lady "\"Oh, that's a good look. Remember that look. You'll want it tonight.\""
    hide cg onlayer cgl
    show cg shr_hall_step_flop onlayer cgl
    show shr_pc dazed
    "You flop down on the worship-hall step, flushed, sweating, your skirt tented, your ears drooping. The stone foxes on the gate posts sit up there in the sun with their blank grey eyes."
    shr_lady "\"Rest your mouth. You'll want it tonight.\""
    hide cg onlayer cgl
    "She says it sweetly.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump shr_mouth

## Rung 3, the lead-in: "Open." Your jaw drops on its own. Flint first.
label shr_mouth:
    $ vn_enter(bg="shr_gate_dusk", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_kneel_gate")
    "Dusk. Your legs skip you down to the gate before the sun's even gone, and kneel you on the gravel between the posts, and fold your hands in your lap like a good maiden."
    "The stone warms. The tails uncurl. They step down."
    hide cg onlayer cgl
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Maiden came down.\""
    hide shr_flint
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Maiden came down on his {i}knees{/i}. Evening, Lady. Look at him. You've been busy.\""
    "He grins at your white hair, your ears, the little swell of your tits in the robe."
    shr_you "\"Don't you DARE— don't come any closer— I'll— I'll {i}bite{/i}, I've got FANGS now—\""
    hide shr_slate
    $ shr_take(3)
    shr_lady "\"Open.\""
    show cg shr_jaw_open onlayer cgl
    show shr_pc possessed
    "Your jaw drops."
    "Just like that. Wide open, tongue out, like a door swinging on its hinge. You try to close it. You try so hard your whole face shakes. It stays open, and drool runs off your tongue down your chin."
    shr_you "\"{i}Haaah{/i}— haah— nnh— {i}NHH{/i}—!\""
    show cg shr_flint_cock onlayer cgl
    "Flint steps in close. His trousers come down, and his cock swings out right in front of your face, thick and grey-veined and heavy, already hard, so big it blocks out the gate behind him."
    shr_lady "\"Oh, I remember {i}that{/i}.\""
    shr_flint "\"Hold still.\""
    "He doesn't push. He doesn't have to. Your head goes forward on its own, your open mouth sliding down over the fat head of him, your tongue curling under it, your lips sealing round the shaft. Your mouth's so sensitive that the first touch of him on your tongue makes your eyes roll."
    shr_you "\"{i}Mmmf{/i}— MMF— {i}mmnnh{/i}—!\""
    vn_sfx "{i}Shlrp.{/i}"
    "You're swearing at him round his cock. Every filthy word you know. It comes out as wet, muffled moans, and your head keeps going, down, down, until your lips are stretched wide round the base of him and your nose is in his stomach.\n{size=-5}{color=#ff8fa3}▸ Glk{/color}{/size}"
    jump shr_mouth_sex

## Rung 3's finish: Flint, then Slate. The "thank you" is hers, in your own voice (she has your mouth,
## not yet your voice); the "you BASTARDS" is yours.
label shr_mouth_after:
    $ vn_enter(bg="shr_gate_dusk", pc="possessed", pc_tag="shr_pc", cast=[], cg="shr_mouth_cum")
    "Flint comes with a long, low grunt, his hand on the back of your head, and it floods your mouth, thick and hot and endless."
    shr_lady "\"Swallow.\""
    vn_sfx "{i}Gulp.{/i}"
    "Your throat does it. All of it. You can feel it going down, warm, and your mouth's still open after, panting, tongue out, glazed."
    shr_lady "\"Now the other one.\""
    shr_you "\"No— {i}no{/i}— I've done— I've DONE one—\""
    show cg shr_mouth_slate onlayer cgl
    "Your head turns. Your hand lets go of Slate's cock and guides it straight to your lips instead, and your mouth opens wide and takes him, all the way, in one long slurp, while Slate laughs, breathless, and holds your ears."
    shr_slate "\"Oh, these are {i}new{/i}. Look at that. She's got your mouth now.\""
    "He rubs them with his thumbs."
    vn_sfx "{i}Glk. Glk. Glk.{/i}"
    "Your head bobs on him, fast and sloppy, hers, not yours, and your mouth is so sensitive it's like being kissed everywhere at once, and you're moaning round him with your little cock dripping under the skirt, and you hate it, and your tongue swirls the head of him like it's starving."
    "He comes in your mouth. He comes on your tongue and your lips and your chin. You swallow it. You don't decide to."
    show cg shr_thank_you onlayer cgl
    "Then your lips close, and lick themselves, and open again, and your own voice, soft and sweet and polite, says to both of them:"
    shr_mouth "\"Thank you.\""
    "That was her. Every word. Your mouth, your tongue, your voice. Her words."
    show shr_pc furious
    show cg shr_bastards onlayer cgl
    shr_you "\"{i}You BASTARDS{/i}. You absolute— you BASTARDS—!\"" with vnfx("shake")
    "You scream it, a second later, all yours, cum on your chin."
    show shr_pc flushed
    "Your tongue licks your lips clean, slow, every drop, and you moan while it does it, because it tastes {i}good{/i}, and that's the worst part. Your mouth's so sensitive now that the taste of them lands like a hand between your legs, and your little cock twitches under the skirt and drips."
    shr_lady "\"Mm. You liked that.\""
    shr_you "\"I did NOT—\""
    shr_lady "\"Your mouth did.\""
    hide cg onlayer cgl
    "Slate's laughing so hard he has to sit on the gate step. Flint just strokes your white hair once, with one heavy hand."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Hold still.\""
    "You do. You don't know why.\n{size=-5}{color=#ff8fa3}▸ Back to the maiden's room{/color}{/size}"
    $ vn_pass(10)
    jump shr_night_three

label shr_night_three:
    $ vn_enter(bg="shr_basin", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_rinse")
    "You rinse your mouth at the basin over and over. You can still taste them. Your tongue keeps going back for it."
    shr_lady "\"Tomorrow, hips.\""
    shr_you "\"What does that MEAN?\""
    $ vn_enter(bg="shr_room", pc="furious", pc_tag="shr_pc", cast=[], cg=None)
    "She just laughs, and your ears flick, and you lie down on the futon facing the wall with your arms wrapped round your new tits."
    call vn_night(7)
    jump shr_dawn_four
