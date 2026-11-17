## THE SOURCE: greathawk's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage
## of the original (main.twee, rungs.twee, bred.twee, ending.twee), written as beats; the director
## scenes are in scenes.rpy. The original is in catalog/docs/routes/vn-original/greathawk/. Eight
## days, one rung each, chained: dawn (the song, the row that landed), morning (the gift), noon (the
## pool), dusk (the piece knotted, counted aloud and tested at the lip), night (the nest). No way
## down until the ending. Kite speaks in three to six words, present tense, no articles.

## ---- DAY 1: the road, the snatch, the tower; rung 1 (Greathawk Opening, Snatch, Wake, Drop) ----

label grh_road:
    $ grh.fit = "own"
    $ vn_enter(bg="grh_moor_road", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_road")
    "The moor road. Heather on both sides, sky on top, and nobody."
    "Everything you own is on your back, in one rucksack stuffed fat at every seam. The lease ran out. The job hasn't started. In between: this."
    "You say it out loud, because it's the best news you've had all year."
    grh_you "\"[grh_pc_name] Reeve, nobody's expecting you anywhere.\""
    show cg grh_shadow onlayer cgl
    "A shadow slides over you. Low. Blade-shaped."
    "You look up. Cloud. Sky. The moor tilting away on every side."
    "A second shadow, lower. Your pulse jumps and you duck, like an idiot, alone on a road in good boots."
    grh_you "\"...Cloud. Weird cloud.\""
    "You tell nobody.\n{size=-5}{color=#ff8fa3}▸ Keep walking{/color}{/size}"
    jump grh_snatch

label grh_snatch:
    $ vn_enter(bg="grh_moor_road", pc="furious", pc_tag="grh_pc", cast=[], cg="grh_snatch")
    vn_sfx "{i}WHUMP.{/i}" with vnfx("shake")
    "Wind slams down on you from above and flattens the heather in a ring. Something grabs the rucksack's straps and the back of your belt at the same time, and the road just... drops away."
    grh_you "\"WHAT— hey— {i}HEY{/i}—!\""
    show cg grh_carried onlayer cgl
    "Your boots kick at nothing. The moor spins and goes small. Wingbeats right over your head, huge and slow, {i}whumm, whumm, whumm{/i}, and the wind screaming in your ears, and you're yelling every word you know and a few you're inventing."
    "Then the cold takes your breath. The sky goes white."
    hide cg onlayer cgl
    scene black onlayer bgl
    "Then it goes black.\n{size=-5}{color=#ff8fa3}▸ Open your eyes{/color}{/size}"
    $ vn_pass(60)
    jump grh_wake

label grh_wake:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "Cold stone under your back."
    "A square of sky, framed by broken walls. No roof. Wind."
    "You roll and come up on your knees with your fists up, ready for anything."
    "A roofless chamber at the top of a tower. Straw heaped deep against one wall, shaped into a nest by somebody who meant it. Your rucksack dumped in the corner. A stone stair climbing the wall, and stopping. In mid-air. Nothing past it but sky."
    show cg grh_kite_back onlayer cgl
    "And on the broken parapet, his back to you: a man. A huge one. Twice your size, shoulders like a door, and off those shoulders, folded high, a pair of wings. Dark. Enormous. Where his feet should be, black talons hook the stone."
    "He turns round."
    hide cg onlayer cgl
    show grh_kite flat at vn_cast_slot
    "A man's face. A hooked nose, hard cheekbones, dark feathers growing back through black hair like a crest. Eyes gold as a new coin, each with a black slit down the middle."
    grh_kite "\"Landbound. Good.\""
    "His voice rings, like two notes at once."
    show grh_pc furious
    grh_you "\"Good? {i}Good?{/i} Where the fuck— what— you— {i}put me back!{/i}\""
    "He tilts his head. Listens. Doesn't move."
    show grh_pc stubborn
    "So you do what you always do. You take stock. Rucksack: yes. Weapons: no. Stairs: no. Way down: ..."
    "Cloth. You've got cloth. Shirts tear into strips. Strips knot into rope. You eyeball the drop past the lip, and the straps on your bag, and do the sums twice. Seven pieces. Seven good pieces would reach the ground."
    grh_you "\"Right. {i}Right.{/i}\"\n{size=-5}{color=#ff8fa3}▸ Go to the lip{/color}{/size}"
    jump grh_drop

label grh_drop:
    $ vn_enter(bg="grh_lip", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_drop")
    "The lip is where the stairs used to come up. Now it's an edge, and past it, wind, and far, far below, a yard of rubble the size of a handkerchief."
    "You look at it for a long time. Then you tell it, flat, like an engineer reporting a failed test:"
    grh_you "\"Not yet.\""
    hide cg onlayer cgl
    "Behind you the harpy's shadow stretches across the flagstones. He's watching. Not hungry, not angry. Just watching."
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_scope")
    "On the perch there's a telescope: brass, green at the joints, older than both of you. You spit on the lens, rub it on your shirt and jam your eye to it."
    show cg grh_scope_road onlayer cgl
    "The road. {i}Your{/i} road, a grey thread stitched across the heather, all the way to a farm the size of a comma. You follow it out. You follow it back. You check it again in case something's changed."
    "Nobody on it. No search party. No van. Nobody."
    grh_you "\"Great. Love that.\""
    hide cg onlayer cgl
    "You tell the brass. When you turn round, the harpy's still watching you, head tilted. You go and sit on the rucksack in the corner, with the sun on your back, and start thinking about rope.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_first_gift

label grh_first_gift:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "At noon he goes off the parapet like a dropped knife, and he's gone."
    "You use the time. Every wall, every crack, every corner of the straw: no rope, no ladder, no trapdoor, nothing. A few squashed cereal bars in the rucksack. Half a bottle of water."
    vn_sfx "{i}Whumm.{/i}"
    show grh_kite flat at vn_cast_slot
    show cg grh_gift_ham onlayer cgl
    "He's back. He sets something at your feet with both hands, careful as a waiter with the special: [GRH_GIFTS[1]['gift']], the string still on it."
    menu:
        "He steps back. Head on one side. Waiting."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"Oh, {i}thanks{/i}. Brilliant. Kidnapped {i}and{/i} catered.\""
            show grh_kite pleased
            "He doesn't hear the knife in it. He hears {i}thanks{/i}. And he opens up like noon: the wings loosen, the shoulders drop, something easy comes into the whole huge shape of him. He goes back to the perch and hums, low, like wind across a bottle."
            "You don't touch the ham. Obviously."
        "Scold him":
            $ grh.gift = "scold"
            show grh_pc furious
            "You pick the ham up by its string, march to the lip and fling it off the tower."
            grh_you "\"I'm not your— whatever this is! I want to go {i}down!{/i} Down! Are you listening to me? Do you even—\""
            "He's listening. To every word. Head tilted, wings at rest, gold eyes on your mouth while you run through everything you've got."
            "When you run out of breath, he kneels behind you and combs his fingers through your hair. Slow. Careful. Unhurried."
            grh_you "\"Don't.\""
            "He keeps going. You let him, purely out of exhaustion, seething the whole time."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look straight through it. Straight through him."
            "He waits. The ham waits. You study the wall like it owes you money."
            "After a while he goes and sits on the perch with his wings folded and his back to you."
            grh_kite "\"Sky is too big alone.\""
            "Then he's gone, and back, and there's [GRH_GIFTS[1]['crack']] by your knee."
            grh_you "\"Thanks.\""
            "It comes out of you. Too high. You hate that it did."
    hide cg onlayer cgl
    show cg grh_gift_pile onlayer cgl
    "All afternoon they keep coming. A pie still in its tin. A bag of oatcakes. A whole picnic hamper with a checked cloth inside, raided off some farmhouse table. He sets each one down in a neat pile by the nest, and nudges the pile tidier, and looks at you."
    "You fold your arms and starve beside it on principle.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_one

label grh_dusk_one:
    $ vn_enter(bg="grh_perch", pc="furious", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_song")
    "At dusk he sings."
    "On the perch, wings half open, throat working, and the sound goes through your skull like wire. Bright, wild notes, up and down and round, nothing you could ever hum. It's like having a kettle installed behind your eyes. A kettle with opinions."
    "You jam your fingers in your ears and turn your back on him."
    hide cg onlayer cgl
    show cg grh_cuff onlayer cgl
    "Then you get to work. The cuff of your shirt, between your teeth."
    vn_sfx "{i}Rrrrrip.{/i}"
    $ grh_rope(1)
    "You twist it, fold it and knot it hard, and you say it out loud, because a count that's said out loud is real."
    show screen grh_rope(1)
    grh_you "\"[GRH_ROPE[1]['count']]\""
    hide screen grh_rope
    "At the lip you hold it out over the drop. [GRH_ROPE[1]['reach']]"
    "That's fine. That's day one. You stuff it deep under the straw, where your hand can find it in the dark.\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_one

## Rung 1: "Touch you now." "No." "Tomorrow, then." (Non-con beats: he doesn't stop, he postpones.)
## Then alone in the straw, out of spite, loud anyway.
label grh_night_one:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "The cold comes up off the moor like water. You last an hour against the wall, teeth going. Then you get in the nest, as far from him as the straw goes. An arm's length."
    show cg grh_hand_hip onlayer cgl
    "He lies on his side with one wing over himself like a blanket. His gold eyes open in the dark. His hand comes across the straw and stops a finger's width off your hip."
    grh_kite "\"Touch you now.\""
    "Flat. Not a question. Like he's telling you the time."
    "Your heart does something traitorous."
    show grh_pc furious
    grh_you "\"{i}No.{/i} No. Absolutely not. Never. Get your— {i}no{/i}.\""
    "You slap the hand away. He looks at the hand. He looks at you. He takes it back, unhurried, like a man putting a tool down where he can find it again."
    grh_kite "\"Tomorrow, then.\""
    hide cg onlayer cgl
    "Then he folds his arms, closes his eyes and goes to sleep like a man off a double shift. No sulk. No argument. Gone."
    grh_you "\"{i}Tomorrow?{/i} Tomorrow I'll be {i}gone{/i}. Tomorrow I'll be halfway down that wall.\""
    "You hiss it at the back of his head. He snores. Once. Like a full stop."
    "You lie there with your jaw locked, wide awake, wired, starving, furious."
    show grh_pc flushed
    "And hard. Rock hard, in your jeans, an arm's length from him."
    menu:
        "You hold out as long as you can stand it. It isn't long."
        "Fuck your fist out of spite":
            $ grh.mood = "spite"
        "Edge it, just to prove you can":
            $ grh.mood = "edge"
    show cg grh_alone onlayer cgl
    "You spit in your palm, shove your hand down your jeans and grab yourself."
    grh_you "\"{i}Fuck.{/i}\""
    "It's into the blanket. It's still loud."
    "Cold fingers, your own cock, everything where it should be and working and {i}furious{/i}. You grip it like you hate it and start pumping, hips jerking into your fist, the straw crackling under you like a bonfire."
    if grh.mood == "edge":
        "You get right to the edge, thighs shaking, and {i}stop.{/i} Squeeze the base. Hold it. Out of pure spite. Because he's right there, and you're not giving him, or the tower, or the whole stupid sky, the satisfaction."
        grh_you "\"Not— {i}now{/i}— fuck— not for {i}you{/i}—\""
        "Then you pick the pace straight back up. And stop again. And again. Precum all over your knuckles, smeared down your shaft, {i}shlick shlick shlick{/i} in the dark, obscene."
    else:
        "You fuck your own fist like it owes you money. Fast and mean, root to tip, thumb grinding over the slit on every upstroke until your heels dig trenches in the nest."
        grh_you "\"Fuck you— fuck this— {i}fuck{/i} your tower—\""
        "Precum wells up over your knuckles. You use it. Wetter. Filthier. {i}Shlick shlick shlick{/i}, right there in the hush, an arm's length from him."
    grh_you "\"Nnh— {i}nnnh{/i}— {i}tomorrow{/i}— tomorrow my {i}arse{/i}— shit— {i}shit{/i}—\""
    "You bite the blanket. You bite your own knuckles. You groan into the straw anyway, louder than you meant, louder than you've ever been alone in your life."
    show cg grh_alone_kite onlayer cgl
    "He sleeps. Huge and still, his face tucked under a curve of wing. Somehow smug even unconscious."
    "The knotted cuff digs into your hip through the straw. You glare at him over it and fuck your fist harder, right at the edge, and then over it—"
    show grh_pc overwhelmed
    show cg grh_alone_peak onlayer cgl
    grh_you "\"{i}Ahh— fuck— FUCK—!{/i}\"" with vnfx("shake")
    "You come all over your own belly, hot, rope after rope, hips humping up off the nest, a long ragged yell muffled into the blanket and not muffled nearly enough. It splashes your stomach and sticks the straw to you."
    "You lie there panting, sticky, shaking."
    hide cg onlayer cgl
    "He doesn't even twitch."
    "{color=#ff5fb8}Your hand knows the way now: grip, twist, the thumb under the head. Spite's a hell of a coach.{/color}"
    call vn_night(6)
    jump grh_dawn_two

## ---- DAY 2: the coat, the name, the pool; rung 2 ------------------------------------------

## Row 1 landed overnight: body hair in the straw by the handfuls, and the sight.
label grh_dawn_two:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_dawn_song")
    "The song again, at first light. Straight through your skull. You pull the blanket over your head, and it comes through the blanket."
    hide cg onlayer cgl
    "When you sit up, there's hair in the straw."
    $ grh_body(1)
    show cg grh_moult onlayer cgl
    "{color=#ff5fb8}Handfuls of it. Dark and curly and {i}yours{/i}. Off your forearms. Off your shins. The thin mat off your chest and the trail under your navel, all of it just lying there in the straw like you've moulted.{/color}"
    "{color=#ff5fb8}You rub your jaw. The stubble's gone. Smooth. {i}Soft.{/i}{/color}"
    "{color=#ff5fb8}You run a palm down your bare forearm and the skin's like the inside of a wrist, and the touch goes straight down your spine and makes your cock twitch in your jeans.{/color}"
    show grh_pc flushed
    grh_you "\"{i}Nnh{/i}— what the— why does that feel so— {i}fuck{/i}—\""
    "{color=#ff5fb8}You do it again. Slower. Goosebumps everywhere. You lick your lips without thinking, and moan out loud, right there in the straw. Your {i}mouth{/i}. Since when is your mouth like that?{/color}"
    "You kick the clumps under the straw."
    show grh_pc stubborn
    grh_you "\"Stress.\""
    hide cg onlayer cgl
    show cg grh_sight onlayer cgl
    "You announce it. And your eyes are doing something. Past the parapet, out on the far road, a van is crawling along, and you can read the badge on its grille. Clear as print. You couldn't read a badge across a car park before."
    "Adrenaline. Obviously."
    hide cg onlayer cgl
    "Also: you're {i}starving{/i}. Somewhere in the night the hunger stopped being a principle and started being shakes. You crawl to the pile and eat oatcakes with both hands, moaning at the salt."
    show grh_kite flat at vn_cast_slot
    "He watches you from the perch."
    grh_kite "\"Eat. Good.\""
    grh_you "\"{i}Shut{/i} up.\""
    "You say it with your mouth full, and eat another one.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(9)
    jump grh_coat

## Whatever you do with the coat, you name him today, out of need.
label grh_coat:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_coat")
    "Mid-morning he drops [GRH_GIFTS[2]['gift']] at your feet."
    "It might have been navy once. The moor has worn it grey and slick. It's dripping. And the stink hits the chamber like a slap: rain, mud, rot, and something you don't want to name."
    menu:
        "He steps back. Head cocked. Hopeful."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"...Thanks.\""
            "Through your teeth. For a coat that smells like a drain."
            show grh_kite pleased
            "And there it is again: he opens up like noon. Shoulders down, wings easy, the gold of his eyes gone warm. He hums on the perch all morning, flutes and stones and wind, on and on."
            "It's unbearable. You need to call him {i}something{/i}, just to tell him to stop."
            grh_you "\"Hey. You. Oi— {i}Kite!{/i}\""
            "It just comes out of you."
        "Scold him":
            $ grh.gift = "scold"
            show grh_pc furious
            grh_you "\"Are you {i}kidding{/i} me?\""
            "It cracks round the chamber like a rifle shot."
            grh_you "\"{i}That's{/i} what you bring me? {i}That?{/i} What am I supposed to do with it? Wear it? It'd kill me! Can you even understand me? Can you even— {i}Kite!{/i} Listen to me!\""
            "The word just comes out of you, sharp and ringing, like a curse you made up on the spot."
            "He listens to the whole rest of it. Every word. Hands loose, wings at rest, the feathers settling at his nape. And when you've shouted yourself hoarse, he kneels behind you and grooms you: fingers through your hair, along your shoulders, down your back. Unhurried. For ages."
            "You could bite him for the patience. You don't. By the end your scalp's tingling and the rage has all gone to steam."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look through the coat. You look through him."
            "He waits. Then he goes and sits on the perch with his back to you."
            grh_kite "\"Sky is too big alone.\""
            "Then he's gone, and back, and there's [GRH_GIFTS[2]['crack']] by your knee. Split down one side. Useless. Offered with both hands."
            grh_you "\"Thanks.\""
            "It comes out of you, too high. You clear your throat. If this is going to keep happening, you need something to call him."
            grh_you "\"...Kite. You're Kite.\""
    $ grh_kite_name = "Kite"
    $ grh.named = True
    show grh_kite flat
    "He blinks. Once. Twice. Tries it."
    grh_kite "\"Kite.\""
    "A dip of his head. Again, tasting it."
    grh_kite "\"Kite.\""
    "Good. Fine. Kite. The coat's still disgusting. You drag it to the far side of the chamber anyway, because it's cloth.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_pool_two

## Rung 2, the pool at noon, authored and taken. Row 2 lands in the still water: gold eyes, the
## mark under each eye, the down, puffy nipples.
label grh_pool_two:
    $ vn_enter(bg="grh_pool", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_pool_noon")
    "At noon the sun gets into the corner of the chamber where the rainwater pool is: a stone cistern, brimming and gold. Kite goes down into it like a man running a chore, shaking his wings out, combing the leaves off the top with his hands."
    "You smell like the coat. You smell like four days in the same jeans."
    grh_kite "\"Come in? Water good.\""
    "You do the maths. You stink. It costs you nothing."
    hide cg onlayer cgl
    $ grh.fit = "nude"
    "You strip and step down in."
    grh_you "\"{i}Fuck{/i}, that's cold—\""
    "Cold enough to bite. You stand there in goosebumps up to your neck, and while the water stills, you look down at yourself in it."
    $ grh_body(2)
    show cg grh_reflection_eyes onlayer cgl
    "{color=#ff5fb8}Your eyes are wrong.{/color}"
    "{color=#ff5fb8}Gold. Your eyes are {i}gold{/i}, gold like his, and while you stare the colour shifts and the black in the middle pulls long and thin into a slit. Under each eye there's a dark mark now, fine as a pencil line, feathered.{/color}"
    grh_you "\"That's the light.\""
    "{color=#ff5fb8}You tell the water. It isn't the light.{/color}"
    "{color=#ff5fb8}Low on your belly, where the trail of hair used to be, there's down. Pale and fine and soft as dandelion fluff.{/color}"
    hide cg onlayer cgl
    show cg grh_pool_wings onlayer cgl
    "Kite wades in behind you. You hear the water slop over the lip of the cistern, feel the size of him at your back, and then his wings come round. Both of them, wet and heavy, closing in front of your chest like a pair of doors."
    show grh_pc furious
    grh_you "\"Oi— hey— {i}out{/i}— open those, I'm not—\""
    "They don't open. He washes you inside them. Long, even strokes: your arms, your shins, your thighs, the back of your neck. Over the down without slowing. Then his palms come round to your chest, and his thumb brushes your nipple."
    vn_sfx "{i}Pop.{/i}"
    show grh_pc flushed
    "{color=#ff5fb8}It goes off like a firecracker. Your nipples are {i}puffy{/i}, both of them, swollen soft and pink and standing out like they've been sucked on all night, and his thumb on one of them is the loudest thing that has ever happened to you.{/color}"
    grh_you "\"{i}Ahh{/i}— hah— {i}cold water!{/i} It's the water, all right? It's cold! It's a shock—\""
    grh_kite "\"Sensitive now.\""
    "He observes it. He circles it again. Your whole body jerks."
    grh_kite "\"Tender. Good.\""
    grh_you "\"Shut up about them— {i}nnh{/i}— get your {i}thumb{/i} off— shut {i}up{/i}—\""
    "{color=#ff5fb8}You try to step out of range. A wing shifts and the range goes with you. You arch instead, which is worse, and your own hand comes up and pinches the other one before you can stop it, and you moan, out loud, in the water. You bite your lip to shut yourself up, and that's worse too: your lip buzzes, hot, all the way down.{/color}"
    "{color=#ff5fb8}In his hands your hips have gone a shade soft. In the ripples your face is smooth all over, like a model's on a billboard, and your hair's grown out shaggy over your ears and drips in your eyes.{/color}"
    "His hands work lower. Over your stomach. Low under your navel, right where the hair used to be, and they stop there. Fingers splayed wide. Heavy."
    grh_kite "\"Touch you now.\""
    menu:
        "Not a question. Last night's, with the full stop still on it."
        "Swear at him till you run out of words":
            $ grh.no = "swear"
            show grh_pc furious
            grh_you "\"No. {i}No.{/i} Don't you— you feathered— you {i}overgrown pigeon{/i}, you— get your hand {i}off{/i} my—\""
        "Shove back at his chest":
            $ grh.no = "shove"
            "You drive your elbow back into his chest, hard, and then both shoulders. It's like shoving the tower. The wings just close tighter."
        "Lock your jaw and say nothing":
            $ grh.no = "silent"
            "You lock your jaw. You say nothing. You stare at the far wall and give him nothing at all, not a sound, not a twitch. You last about a breath."
    show cg grh_pool_hand onlayer cgl
    "His hand slides down and closes round your cock and lifts it out of the water."
    "{color=#ff5fb8}It looks smaller than it should. Lost in that huge callused fist, pale, flushed red at the tip. It was never this small. Was it? It wasn't.{/color}"
    grh_you "\"Cold water. That's— the cold, that's all it is—\""
    "Your cock doesn't care about the cold. It thickens at the first pull and goes hard in his hand."
    grh_you "\"No— no, {i}don't{/i}— that's not— it's not {i}for{/i} you—\""
    "And Kite narrates. He narrates {i}everything{/i}, in the same flat voice he uses for the weather."
    grh_kite "\"Grip. Good. Up. Down. Thumb here.\""
    "His thumb presses under the head and circles. You swear. You twist. His other arm comes across your chest and holds you back against him, easy, and the wings stay shut, and the thumb keeps circling."
    grh_kite "\"Leaking.\""
    grh_you "\"It's {i}not{/i}— {i}nngh{/i}— it's the water, it's pool water, it's—\""
    grh_kite "\"Leaking. Hard. Says yes.\""
    show grh_pc overwhelmed
    grh_you "\"It doesn't get a {i}vote{/i}— {i}ahh{/i}— {i}ahh{/i}— Kite, I swear to god—\""
    show cg grh_pool_wrist onlayer cgl
    "Water slaps your ribs. His knee nudges between yours and spreads you wide in the water, and the size of him behind you, the size of his hand on you, sets fire to every nerve the shame can't reach. {i}Shlk, shlk, shlk.{/i} Your hips are jerking into his fist. You can feel them doing it. You can't make them stop."
    grh_you "\"Stop— {i}stop{/i}— fucking— shit— {i}Kite{/i}—\""
    "You grab his wrist with both hands to haul it off you. You pull. You've got both hands round one wrist and you pull with everything you've got."
    "It doesn't budge. It just keeps going, {i}shlk shlk shlk{/i}, with your hands clamped round it riding along."
    grh_kite "\"Almost. Good.\""
    grh_you "\"{i}Don't{/i}— don't you— {i}don't{/i}— {i}ahhh{/i}—!\"" with vnfx("shake")
    show cg grh_pool_peak onlayer cgl
    "His fist closes tight, and you come screaming, hips bucking, spurting hot through his fingers and up across your own belly, the whole sky gone white, still hanging off his wrist with both hands."
    "Kite says it the way he'd say it about the weather:"
    grh_kite "\"Leaking. Healthy.\""
    hide cg onlayer cgl
    show grh_pc furious
    "The wings open. Just like that. You stagger forward through the water, red to the ears, still twitching, swearing at him at the top of your voice, and he goes back to washing his own arms like nothing happened."
    "{color=#ff5fb8}You know a lot more about hands than you did this morning. Where to hold. How hard. When. Even with yours wrapped round his wrist the whole time.{/color}"
    $ grh.fit = "own"
    "You get your clothes back on, wet, and don't look at him.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_two

label grh_dusk_two:
    $ vn_enter(bg="grh_perch", pc="flushed", pc_tag="grh_pc", cast=[], cg="grh_scope_farm")
    "All afternoon you sit at the telescope with your face burning."
    "The farm. A couple of figures the size of commas walk from a shed to a garden and back. Washing on a line. A van. Nobody looks up. Nobody ever looks up."
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_sorting")
    "Back inside, you catch yourself sorting his gift pile by how it would tear. The velvet: too rotten to hold a knot. The jacket: one good sleeve, and not much else. You stop. You look at your hands. You keep sorting."
    hide cg onlayer cgl
    "At dusk he sings. It still goes through your skull like wire. You only put one finger in one ear."
    $ grh_rope(2)
    show cg grh_knot_coat onlayer cgl
    "Then the coat. You wrench two long strips off it, crusted with moor muck, wrap them round your bare foot to pull them tight, and knot them onto the cuff. Out loud:"
    show screen grh_rope(2)
    grh_you "\"[GRH_ROPE[2]['count']]\""
    hide screen grh_rope
    "At the lip, you hold it up against yourself. [GRH_ROPE[2]['reach']]"
    "Under the straw it goes.\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_two

label grh_night_two:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "The nest. Kite settles an arm's length away with a wing over himself."
    "He doesn't reach for you tonight. He just looks at you once, gold in the dark, the way he looked at that hand last night, and closes his eyes."
    show grh_pc flushed
    "You lie there with your new soft skin prickling against the straw, all of it awake, your puffy nipples rubbing on the blanket every time you breathe."
    vn_sfx "{i}Rrsh.{/i}"
    "You roll over. {i}Rrsh.{/i} You roll back. Every time, the blanket drags across them and sends a little hot spark straight down between your legs."
    grh_you "\"{i}Nnh{/i}— stupid— {i}stupid{/i} blanket—\""
    "You end up on your back with the blanket shoved down to your waist and the night air on your chest, which is worse, because now you can feel them standing up in the cold."
    "He'd do it again. You know he would. He wouldn't even ask. He'd just say it, in that voice, and do it, and narrate it."
    "You are not thinking about that. You are a man with a rope, two pieces long."
    "You absolutely do not think about his hand."
    "You think about his hand until you fall asleep."
    call vn_night(6)
    jump grh_dawn_three

## ---- DAY 3: the authored Ignore day, the itch, waiting for the song, your mouth; rung 3 --------

label grh_dawn_three:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "You wake up with a plan. A good one."
    "If thanking him does something, and shouting at him does something, then {i}nothing{/i} does nothing. Total indifference. He gets no thanks, no scolding, not even a look."
    "It's an excellent plan."
    "You reach under the straw for the rope, and something on your chest bounces."
    $ grh_body(3)
    show cg grh_swell onlayer cgl
    "{color=#ff5fb8}You stop. You look down your shirt.{/color}"
    "{color=#ff5fb8}A swell. Small and soft, under each puffy nipple: a little mound that moves when you move. You reach again, on purpose. It bounces again.{/color}"
    show grh_pc flushed
    grh_you "\"{i}No.{/i} {i}Ohh{/i}— nnh— no, no, {i}no{/i}—\""
    "{color=#ff5fb8}You poke it. Soft. Warm. Like dough. You squeeze, and a hot zing shoots from your nipple straight down to your cock. You squeeze again. Then the other one. You're kneeling in the straw at sunrise groping your own chest with both hands and moaning about it.{/color}"
    "{color=#ff5fb8}Your jeans hang loose at the waist now, and when you crouch they bite tight across your seat, where your hips have started to round out.{/color}"
    hide cg onlayer cgl
    show cg grh_reflection_crown onlayer cgl
    "{color=#ff5fb8}In the pool your jaw's narrower. Your lips are fuller, pinker, and when you lick them you shiver all over: they feel swollen. {i}Hungry.{/i} Your hair's grown past your ears, and at the crown, threaded through it, there are feathers. Small, dark, glossy. {i}Yours.{/i}{/color}"
    show grh_pc furious
    grh_you "\"{i}KITE!{/i}\"" with vnfx("shake")
    "{color=#ff5fb8}You yell it, and your voice cracks clean in half and shoots up high. You grab your throat.{/color}"
    "{color=#ff5fb8}Under the down your cock's so small now you'd have to dig for it. You stop digging.{/color}"
    "{color=#ff5fb8}And there's an itch, at the small of your back and the nape of your neck, that no scratching touches.{/color}"
    grh_you "\"It's the itch. It's {i}swelling{/i}. From the itch.\""
    hide cg onlayer cgl
    show grh_pc stubborn
    "You say it in the squeaky voice. Indifference. Starting now.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(9)
    jump grh_gift_three

## Rung 3 is the authored Ignore day: you try indifference on purpose and last two gifts. The choice
## is how you ignore him.
label grh_gift_three:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_pie")
    "He comes back with [GRH_GIFTS[3]['gift']] and sets it at your feet, still warm."
    menu:
        "You do nothing. Not a flicker. Hands in your lap."
        "Stare at the wall":
            $ grh.gift = "wall"
            "You stare at the wall. You give the wall your full attention. It's a great wall. Best wall you've ever seen."
        "Count your knots instead":
            $ grh.gift = "knots"
            "You feel under the straw for the rope and count the knots by touch. Two. Two. Still two."
        "Whistle at the sky":
            $ grh.gift = "whistle"
            "You whistle at the sky, badly, through your teeth, like a man waiting for a bus."
    hide cg onlayer cgl
    "He waits. Nothing. So he goes to the perch and sits with his wings folded tight, looking out at the empty moor, and says it to nobody at all."
    grh_kite "\"Sky is too big alone.\""
    "You don't react. You're {i}great{/i} at this."
    show cg grh_keyring onlayer cgl
    "Late in the morning he comes back with the second one: [GRH_GIFTS[3]['crack']], filthy and sun-bleached and sodden with bog water, some cartoon thing with one stitched ear hanging off by a thread. He sets it down very gently, wings hunched in, head dipped. Hoping."
    "You last about a breath and a half."
    grh_you "\"{i}Thanks{/i}.\""
    "You blurt it. Too high. Too soft."
    show grh_kite pleased
    "And whatever was holding up the barricade just gives. You sit down hard in the straw. His eyes light up, a notch less alone."
    "A pie and a keyring. That's all you had in you.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_noon_three

label grh_noon_three:
    $ vn_enter(bg="grh_pool", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_pool_dry")
    "Noon. Kite in the pool, wings spread to dry over the warm stones."
    "The itch is worse. Small of your back, nape of your neck, and it {i}pulls{/i}: it pulls you toward him like a rope round your middle."
    "You sit on the edge of the cistern, and before you've thought about it you've shuffled back, and back, until his wet hands are in reach."
    show cg grh_itch onlayer cgl
    "His fingers find the itch at your nape and dig in."
    show grh_pc flushed
    grh_you "\"{i}Ohhhh{/i}— right— {i}there{/i}— don't you dare move—\""
    "It's electric. Your scalp crawls, your back arches, your eyes roll up."
    grh_kite "\"Here. Good.\""
    "He scratches down your spine to the small of your back."
    grh_you "\"That's— that's the {i}itch{/i}, that's only the itch, don't get {i}ideas{/i}— {i}ohh{/i}—\""
    "You're backing into his hands. Like you want it. You don't. It's the {i}itch{/i}.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_three

label grh_dusk_three:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_sleeve")
    "All afternoon you go through the pile. The velvet: rotten. The keyring: squelches. The jacket: one good sleeve, and you take it off at the shoulder with your teeth and both hands, swearing the whole time."
    $ vn_enter(bg="grh_lip", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_lean_song")
    "At dusk you go to the lip."
    "You're halfway out over the drop, neck craned, mouth open, before you notice what you're doing."
    "You're waiting for the song."
    "You've been waiting for it for days, now you count back. Which is only sense. It's the only clock in the tower. A man needs to know when the food comes."
    "Then it starts, and you lean out over nothing and listen to the whole thing."
    hide cg onlayer cgl
    $ grh_rope(3)
    "You knot the sleeve on and count it out loud."
    show screen grh_rope(3)
    grh_you "\"[GRH_ROPE[3]['count']]\""
    hide screen grh_rope
    "It cracks high on the second word. The cold."
    "[GRH_ROPE[3]['reach']]\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_three

## Rung 3's lead-in (Non-con beats): "Mouth. Now." and a hand in your hair. Nobody touches you between
## the legs tonight; nothing inside you but his cock in your mouth.
label grh_night_three:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "The nest is warmer tonight: straw and heather and a hiker's fleece he brought up, and the heavy musk he leaves wherever he lies too long."
    show cg grh_fist_hair onlayer cgl
    "Kite folds his wings and looks at you. Very direct. Then he sits up, and his hand goes into your hair."
    "Not a grab. He just closes it. A whole fist of your hair, and the feathers at your crown, held."
    grh_kite "\"Mouth. Now.\""
    show grh_pc furious
    grh_you "\"Excuse {i}me?{/i}\""
    menu:
        "He's already drawing your head down toward his lap. Slow. Even. Like lowering a bucket down a well."
        "\"No. Fuck off. NO.\"":
            $ grh.no = "swear"
            grh_you "\"No. Fuck {i}off{/i}. {i}No.{/i} I'm not— I'm not doing— you can't just {i}say{/i} that and—\""
        "Shove at his thighs with both hands":
            $ grh.no = "shove"
            "You plant both hands on his thighs and shove. You might as well shove the floor. Your arms lock, and bend, and your face keeps going down."
        "Clamp your lips shut":
            $ grh.no = "silent"
            "You clamp your lips shut so hard your jaw creaks. Not a word. Not a sound. Nothing gets in."
    show cg grh_lap onlayer cgl
    "The scale of him resets everything all over again: sprawled in the nest, talons braced in the straw, wings tucked tight to the stone, and between his thighs—"
    "His cock is big. Smooth and dark and heavy, already slick at the tip, and his hand brings your face down right onto it."
    "It rests on your lips. Hot. Salt."
    grh_kite "\"Open.\""
    grh_you "\"{i}Mm-mm{/i}—\""
    "You shake your head against it. That only smears him across your mouth."
    "He waits. His fist doesn't loosen. His thumb strokes once, behind your ear, right on the itch at your nape—"
    show grh_pc overwhelmed
    grh_you "\"{i}Ohh{/i}— {i}glk{/i}—!\""
    "And you're open, and he's in. Over your tongue, stretching your lips, and your jaw goes wide around him because there's nowhere else for it to go."
    grh_kite "\"Warm mouth. Good. Take more.\""
    "He takes more for you. His hand brings your head down, and down, until your nose is in the soft feathers of his belly and he's all the way down your throat, and holds you there."
    grh_kite "\"Tight. Wet. Good grip.\""
    grh_you "\"{i}Mmmmh{/i}—!\""
    "You slap his hip. You slap it again. Spit runs down your chin."
    show cg grh_pop onlayer cgl
    "He lifts you off by the hair. You come off him with a loud wet {i}pop{/i}, gasping, strings of spit from your lips to his cock, and the first thing out of you, as reasonable as a human being has ever been in a nest, is:"
    show grh_pc stubborn
    grh_you "\"You can't— you can't just {i}do{/i} that— and while we're on it, purely for the record— has anything about me struck you, at all, in any way, lately, as... {i}different?{/i}\""
    "Kite considers this. Seriously. He blinks slow. He draws one thumb along your jaw."
    grh_kite "\"Eyes are better. Suits you.\""
    "That is technically an answer."
    "Then the fist in your hair brings your head back down.\n{size=-5}{color=#ff8fa3}▸ {i}Mmph{/i}—!{/color}{/size}"
    jump grh_mouth_sex

label grh_mouth_after:
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_mouth_end")
    "He comes with your nose in his feathers and his fist in your hair, hips giving one short buck, and holds you there while it pumps down your throat. You swallow because the only other choice is drowning, swearing round him, moaning round him, loud. When he finally lets you off he's still leaking, and the last of it stripes your lips and chin."
    grh_kite "\"Swallowing me down. Good mouth. Greedy now.\""
    "He says it a bit late, flat as ever."
    show grh_pc furious
    grh_you "\"{i}Greedy?{/i} I was saying {i}no!{/i} I was saying no the whole— the {i}entire{/i}—\""
    hide cg onlayer cgl
    "You croak it, wiping your chin with the back of your hand. He's already lying back down."
    "Nobody touched you between the legs. Not once. You're twitching and wide awake under the down anyway, and your lips are buzzing, and you lie there furious at all of it."
    "{color=#ff5fb8}Your mouth figured him out fast. Too fast. Tongue flat, throat open, breathe through your nose. Apparently you're good at this, whether you're saying yes or not.{/color}"
    show cg grh_groom onlayer cgl
    grh_kite "\"Good. Stay still. Hair softer. More feathers.\""
    "He grooms you afterwards for what could be an hour or a year, one wing pinning you to his side: your hair, the feathers at your crown, the itch at your nape. You swear at him until you can't, and then you go boneless and sleep like the dead."
    call vn_night(7)
    jump grh_dawn_four

## ---- DAY 4: the tail, the real swell, the ruff; the MANDATORY first anal; rung 4 ------------

label grh_dawn_four:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "You wake up warm and late, buried in fleece, with Kite long gone."
    "You try to sit up. You can't."
    "Something's rooted at the small of your back, caught under your hip."
    $ grh_body(4)
    show cg grh_tail onlayer cgl
    "{color=#ff5fb8}You reach behind you. Feathers. Broad and dark and long, drying at the tips.{/color}"
    show grh_pc furious
    grh_you "\"{i}WHAT{/i}—\""
    vn_sfx "{i}CLANG.{/i}" with vnfx("shake")
    "{color=#ff5fb8}You scramble onto your knees and the thing whips left and wipes out half the gift pile. You twist, and it whips right and takes the telescope clean off its stand. It rolls away across the flagstones.{/color}"
    "{color=#ff5fb8}It's a tail. You have a {i}tail{/i}. It comes out of you just above your arse, and it twitches on its own, and it's kinked up tight like a question mark.{/color}"
    grh_you "\"Muscle spasm. You slept funny.\""
    hide cg onlayer cgl
    show grh_pc flushed
    "{color=#ff5fb8}You inform it. And under the shirt there's a real swell now. You can feel it before you look: {i}weight{/i}. Soft, heavy handfuls pulling the shirt tight across your chest, the buttons straining, your nipples poking through the cloth.{/color}"
    "{color=#ff5fb8}You grab them. You can't not. They fill your palms.{/color}"
    grh_you "\"{i}Ohh{/i}— fuck— they're— {i}nnh{/i}—\""
    "{color=#ff5fb8}You squeeze, and moan, and squeeze again, and the new tail flicks up behind you on its own like it's cheering you on.{/color}"
    "{color=#ff5fb8}Your hips have gone out. Wide. The jeans fight you all the way up, and the seat's stretched drum-tight over an arse that's round now, {i}properly{/i} round, soft as anything when you grab a handful of it, and the grab goes off like a live wire. You moan with your mouth hanging open, and even the air on your tongue feels like something. Your thighs touch when you stand. They rub when you walk. Your waist dips in between, and when you put your hands on it, your fingers nearly meet.{/color}"
    "{color=#ff5fb8}In the pool your face has gone soft, the jaw delicate, and your hair hangs to your jaw now, dark feathers all through it.{/color}"
    show grh_pc stubborn
    grh_you "\"Diet. All the fat's going to the chest. That's the oatcakes.\""
    "You announce it, in a voice that's gone light, and stays there."
    show cg grh_sitting onlayer cgl
    "Sitting turns out to be a whole new skill. Flat down: tail squashed. Cheat to one side: tail caught under your hip and your thighs off at an angle. You lose most of the morning to it, and the doorway, and the telescope again.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(10)
    jump grh_gift_four

label grh_gift_four:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_webbing")
    "He comes in off the parapet with [GRH_GIFTS[4]['gift']], torn off some hiker's pack, buckle and all, and drops it in front of you."
    menu:
        "Cloth. Strong, long, {i}knottable{/i} cloth."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"Thanks.\""
            "It's {i}easy{/i}, which is worse."
            show grh_kite pleased
            "He opens up like noon and hums on the perch, and your tail swishes in the straw in time with it, and you sit on it."
        "Scold him":
            $ grh.gift = "scold"
            grh_you "\"What is this? Is this a {i}strap?{/i} What do you think I'm going to do with a— actually. Actually, give me that.\""
            "You stop. You scold him anyway, for form's sake, all the way through. He listens to every word, head tilted. Then he kneels and grooms the base of your new tail, slow, unhurried, and your knees go out from under you."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look straight through it."
            grh_kite "\"Sky is too big alone.\""
            "He sits on the perch with his back to you. Then [GRH_GIFTS[4]['crack']], dropped by your knee, offered with both hands."
            grh_you "\"{i}Thanks{/i}.\""
            "Too high. Everything you say is high now."
    "You tear the webbing into a strip with your teeth.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_noon_four

label grh_noon_four:
    $ grh.fit = "nude"
    $ vn_enter(bg="grh_pool", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_tail_float")
    "The pool, at noon. You climb in after him, tail and all, and the tail floats out behind you and won't sink, and you swear at it."
    show cg grh_pool_lift onlayer cgl
    "Kite washes you. Your new tits, slow, both hands, cupping them, lifting them out of the water and letting them drop back with a little {i}plip{/i}, until you're panting."
    grh_kite "\"Heavier. Good.\""
    show grh_pc flushed
    grh_you "\"They're {i}not{/i}— that's the water— {i}ahh{/i}— don't pinch—\""
    "He pinches. You arch. He moves on, unhurried: your hips, both palms spread over the new width of them. The round of your arse, a handful each side, squeezed like he's checking fruit. Then the base of your tail, right where it comes out of you, and his thumb strokes down, just once, between your cheeks."
    grh_you "\"{i}Hah{/i}—!\"" with vnfx("shake")
    show cg grh_tail_smack onlayer cgl
    "Your whole body clenches. Your tail shoots straight up out of the water and smacks him in the face."
    "He takes his hand away. He looks at the base of your tail, and at you."
    grh_kite "\"Tonight.\""
    show grh_pc furious
    grh_you "\"{i}Tonight{/i} nothing. Tonight I'm knotting rope.\""
    hide cg onlayer cgl
    $ grh.fit = "own"
    "You snap it, face burning. You're shaking for the rest of the afternoon. Your tiny cock's hard under the water the whole time and you can't even find it to do anything about it.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_four

label grh_dusk_four:
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "By evening your throat itches. You scratch, and your fingers come away with fluff."
    $ grh_body("4r")
    show cg grh_ruff onlayer cgl
    "{color=#ff5fb8}A ruff of short dark plumage has come up round your neck, collar-high. It puffs out when you swallow. It stands straight up when you swear. You stroke it, and the shiver goes all the way down to the tip of your tail.{/color}"
    grh_you "\"Straw rash.\""
    show grh_kite pleased at vn_cast_slot
    "You tell it. Kite comes in off the parapet, sees it, and smooths it flat with one knuckle, delighted."
    grh_kite "\"Throat pretty now. Good.\""
    hide cg onlayer cgl
    show cg grh_lip_listen onlayer cgl
    "At dusk he sings, and you sit on the lip and listen to every note."
    $ grh_rope(4)
    "Then the webbing, knotted on hard with your teeth, and out loud:"
    show screen grh_rope(4)
    grh_you "\"[GRH_ROPE[4]['count']]\""
    hide screen grh_rope
    "[GRH_ROPE[4]['reach']]\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_four

## Rung 4: THE MANDATORY SCENE. "Open for me." is a statement; every choice is how you refuse, into
## it; there is no way round it. Mantled face-down, pinned under his wings; "mate" lands mid-scene.
label grh_night_four:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_groom_tail")
    "In the nest he grooms you for a long time, one wing heavy over your back. Your hair. The new ruff. The base of your tail. Every stroke of his fingers goes straight between your legs, and you lie there rigid and tell him so, and he keeps going."
    "Then his hand stops on the small of your back, right where the tail comes out of you, and his thumb strokes down. Between your cheeks. Slow."
    grh_kite "\"Open for me.\""
    menu:
        "No question mark. Like he's reading it off a list."
        "\"No. Not that. Not THERE.\"":
            $ grh.no = "swear"
            show grh_pc furious
            grh_you "\"No. {i}No.{/i} Not that. Not {i}there{/i}, Kite, I swear to god—\""
            "And his palm between your shoulders puts you face-down in the straw in the middle of it."
        "Twist round and shove his chest":
            $ grh.no = "shove"
            "You twist round and shove his chest with both hands. He lets you. Then he takes both your wrists in one hand, turns you back over like a pancake, and you're face-down in the straw."
        "Grab two fistfuls of straw and say nothing":
            $ grh.no = "silent"
            "You grab two fistfuls of straw and say nothing. Not a word. He takes your hips in his hands and lifts, and you're face-down in the straw with your fists still full."
    $ grh.fit = "nude"
    show cg grh_mantle onlayer cgl
    "Knees and elbows. Arse up in the air, round and new. And your tail, the traitor, kinks up high out of his way all on its own, like it knows exactly what's happening."
    grh_kite "\"Tail says yes.\""
    grh_you "\"The tail doesn't {i}speak{/i} for— {i}hey{/i}—\""
    "Behind you, he spreads his wings. They come down round you like a tent, the long feathers settling over your shoulders and pinning them to the straw, and the nest goes dark and warm and smells of him. You buck once. The wings don't."
    grh_kite "\"Stay. Good.\""
    show cg grh_fingers onlayer cgl
    "He spits in his palm. His fingers are huge. The first one presses at your hole, slow, slick, and sinks in."
    show grh_pc flushed
    grh_you "\"{i}Hahh{/i}— fuck— {i}out{/i}— that's— that's {i}big{/i}, that's just your {i}finger{/i}— get it {i}out{/i}—\""
    grh_kite "\"Open. Good.\""
    "A second one. He works them in and out, unhurried, stretching you, and your whole body goes loose and hot round his hand while your mouth keeps saying no into the straw."
    "{color=#ff5fb8}Under you, your cock hangs between your thighs. Tiny now. Hard as it'll ever get, a little pink nub bobbing every time his fingers push in, dripping on the straw. Your balls have drawn up to nothing behind it.{/color}"
    grh_you "\"Don't look at it. Don't you dare look at it, it's {i}useless{/i}, it's not— it doesn't {i}mean{/i} anything—\""
    "You moan it into the straw. His fingers slide out. Something much bigger and blunter takes their place, pressing, hot."
    grh_kite "\"Inside now.\"\n{size=-5}{color=#ff8fa3}▸ \"No— Kite— NO—\"{/color}{/size}"
    jump grh_mate_sex

## "Mate" landed mid-scene; from here it's his name for you. Tiny-cock anal, cumming untouched.
label grh_mate_after:
    $ grh.called = "mate"
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_mate_end")
    "He comes buried to the hilt, wings clamped round the both of you, and you feel every hot pulse of it, deep inside."
    "You lie pinned under him in the dark while it plays back on its own: his hips slapping your arse, {i}pap, pap, pap{/i}, his wings over you like a roof, and your own voice the whole time, high and broken and {i}loud{/i}. No, and no, and get off, and then somewhere in there it stopped being no. Your tiny cock bouncing under you on every thrust, untouched, drooling on the straw, until it just twitched and spilled on its own and you didn't even notice, because the only thing making you come was him."
    "And somewhere in the middle of it, he said it. Flat as the weather."
    grh_kite "\"Mate looks perfect under me.\""
    "{i}Mate.{/i}"
    "You heard it land. You didn't say a thing about it. You were too busy shoving back onto him and yelling {i}harder{/i} into the straw, and you'd like that struck from the record."
    "You're still not saying a thing about it. You're lying here leaking him, with your own mess drying on your belly and your tail flopped over his arm, not saying a thing about it."
    show grh_pc stubborn
    grh_you "\"Rope. Four pieces. Still counting.\""
    "You croak it, at last, into the straw. His wing settles heavier over you."
    grh_kite "\"Good.\""
    "{color=#ff5fb8}Your hips found his rhythm on their own: back onto him, roll, squeeze. And your mouth's been watering for him all day. Nobody taught you any of it, and you never said yes to a second of it.{/color}"
    "He grooms you to sleep, wing and all, and you let him only because you can't lift it."
    call vn_night(3)
    jump grh_small_hours

## ---- DAY 5: the shift in the small hours, the clothes fail, the pool; rung 5 ------------------

## The cock is gone, found by hand in the night. A few flat lines and back to sleep. Still "he": the
## pronoun waits for "Wife." (rung 7).
label grh_small_hours:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "Half asleep. Dreamless. The quiet after the last song."
    "Your hand goes down to scratch, to adjust, the way it always has."
    "There's nothing under the down. Nothing there at all. Smooth and soft and warm, like there never was."
    grh_you "\"...Huh.\""
    "You go back to sleep."
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    $ vn_until(6)
    pause 0.35
    window auto
    jump grh_dawn_five

## Row 5 lands at waking: the woman's body comes in hard, the shirt and the jeans fail, the flannel.
label grh_dawn_five:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "You wake up hungry and functional. You get dressed. You go to button your shirt."
    $ grh_body(5)
    show cg grh_buttons onlayer cgl
    "{color=#ff5fb8}It won't.{/color}"
    "{color=#ff5fb8}Your tits are in the way. Real ones. They fill your hands when you cup them and spill over your fingers when you squeeze, heavy and warm and soft, the nipples fat and pink and standing up hard in the morning air.{/color}"
    show grh_pc flushed
    grh_you "\"{i}Ohhh{/i}— oh, {i}fuck{/i}— why are they so— {i}nnh{/i}— so {i}good{/i}—\""
    "{color=#ff5fb8}You squeeze. You moan. You can't stop squeezing.{/color}"
    vn_sfx "{i}Pok. Pok.{/i}"
    "{color=#ff5fb8}You yank the shirt shut over them anyway. Buttons go flying across the chamber, the back splits from collar to hem, and that's the end of the shirt.{/color}"
    "{color=#ff5fb8}The jeans are worse. Your hips have gone {i}wide{/i}, really wide, and your arse is... You get the jeans up past your thighs, thick and soft and pressed together all the way up, and haul them over a round, heavy arse that wobbles when you jump, and—{/color}"
    vn_sfx "{i}Shrrrrk.{/i}" with vnfx("shake")
    $ grh.fit = "nude"
    show cg grh_wreck onlayer cgl
    "{color=#ff5fb8}The seat goes. All of it. What's left is two tubes and a waistband.{/color}"
    "{color=#ff5fb8}You stand there in the wreck and look down. Under the pale down, between your thick thighs: a cunt. Soft lips, slick already, a little pink nub at the top. Just there. Like it always was. You brush it once with your fingertips and your knees go, and you sit down hard in the straw with your mouth open, moaning at nothing.{/color}"
    "{color=#ff5fb8}Your waist's pulled in tight between those hips and those tits. In the pool, your face is a woman's from the front: full lips, soft jaw, gold eyes under feathered hair that's reached your shoulders.{/color}"
    show grh_pc stubborn
    grh_you "\"Porridge. It's all the porridge.\""
    hide cg onlayer cgl
    "You say it in a voice that's light and clear and isn't going anywhere."
    $ grh.fit = "flannel"
    show cg grh_flannel onlayer cgl
    "There's a flannel shirt in the gift pile, blue and green checks, too big to wear. You tie it round your hips by the sleeves. It hangs like a skirt over the new swell of you, and you decide not to have an opinion about that.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(9)
    jump grh_gift_five

label grh_gift_five:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_scarf")
    "He drops [GRH_GIFTS[5]['gift']] on the edge of the nest. The scarf's long and striped and blessedly clean. The fleece goes straight into the nest: he packs it in round the hollow where you sleep, and stands back to look at it, and packs it in again."
    menu:
        "He looks at you, and at the nest, and at you."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"Thanks. Good one. Long.\""
            show grh_kite pleased
            "He opens up like noon. He hums on the perch and keeps looking over at you, and every time he looks, your nipples go hard under nothing at all."
        "Scold him":
            $ grh.gift = "scold"
            grh_you "\"Do you know how hard it is to knot {i}fleece?{/i} No? Because you've never had to make a— never mind. Give me the scarf.\""
            "You stop. He listens to all of it, head tilted. Then he grooms your ruff, slow, with one knuckle, until it's lying flat and so are you."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look straight through him, tits out, arms folded under them."
            grh_kite "\"Sky is too big alone.\""
            "He says it to the perch. Then [GRH_GIFTS[5]['crack']], set down by your foot."
            grh_you "\"{i}Thanks{/i}.\""
            "You squeak it."
    "The scarf goes under the straw with the rest.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_noon_five

## Rung 5's act: the pool at noon, and he takes you in it. "Touch first." and "Inside now." are
## statements; every choice is how you refuse. Never flipped. Conception at the finish, never named.
label grh_noon_five:
    $ vn_enter(bg="grh_pool", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "Noon. The water's warm today. The sun's been on the cistern all morning and the stones round it breathe heat."
    "You're not going in. You've decided. You sit on the far side of the chamber with the flannel tied tight round your hips and your arms folded over your new tits, and you glare at the pool like it's the one who did this."
    "Kite climbs in, dunks his head and shakes out his wings, wild and easy. Then he climbs back out, dripping, and comes across the flagstones to you."
    grh_kite "\"Pool.\""
    show grh_pc furious
    grh_you "\"No.\""
    show cg grh_carried_pool onlayer cgl
    "He picks you up. Just like that, one arm under your knees and one behind your back, your thick thighs and your tail and all of you, like a sack of shopping."
    grh_you "\"{i}Put me down!{/i} Kite! I said no, I said— {i}put me DOWN{/i}—\""
    $ grh.fit = "nude"
    show cg grh_pool_five onlayer cgl
    "He does. In the water. The flannel's gone somewhere on the way, and you're in up to your tits, warm water all round you and his chest at your back and his wings coming round, closing, both of them, like the first day at the pool."
    "You know exactly what that means now."
    grh_you "\"No. {i}No.{/i} Not— Kite, it's new, it's— I've had it a {i}morning{/i}—\""
    "His hands go wide on your thighs under the water, talons braced on the stone, thumbs sweeping arcs over the wet skin. Spreading them."
    menu:
        grh_kite "\"Touch first.\""
        "\"Don't you DARE—\"":
            $ grh.no = "swear"
            grh_you "\"Don't you {i}dare{/i}— don't you {i}dare{/i}, you feathered— I will {i}bite{/i} you—\""
        "Shove off the side to get out":
            $ grh.no = "shove"
            "You plant your feet on the cistern wall and shove off it to get out. A wing comes down in front of you like a gate. You bounce off it, straight back into his arms."
        "Clamp your thighs shut and say nothing":
            $ grh.no = "silent"
            "You clamp your thighs shut and say nothing. His hands just wait there between them. Then his thumbs press, slow and even, and your thighs come open like a door with a bad latch."
    grh_kite "\"Soft. Thighs thick. Good.\""
    show cg grh_pool_five_touch onlayer cgl
    "He slides two fingers down your slit, slow, tracing. You jerk. His other arm comes across your waist and holds you still against him."
    show grh_pc flushed
    grh_you "\"Get— {i}out{/i}— don't— {i}ahh{/i}—\""
    "One finger sinks in, then two."
    grh_you "\"{i}Ahh{/i}— fuck— take them— take them {i}out{/i}— no, not— don't {i}twist{/i} them— don't—\""
    grh_kite "\"Open more. Slick already. Squeezing hard.\""
    "He twists them."
    grh_you "\"That's the {i}water{/i}, that's— {i}nngh{/i}— shut up— shut {i}up{/i}— stop it— stop— {i}stop{/i}—\""
    "And your hands are on your own tits, squeezing, pinching, rolling the fat nipples, and you don't remember putting them there."
    "He draws his fingers out, slick with you and the water both, and reaches down to guide himself. Thick and dark and nothing shy about it, the head pressing blunt against you under the water."
    grh_kite "\"Inside now.\"\n{size=-5}{color=#ff8fa3}▸ \"Kite— no— NOT INSIDE—\"{/color}{/size}"
    jump grh_pool_five_sex

## Rung 5's climax: "Filling you. Mine." Your orders are break-begging now. His palm on your belly.
label grh_pool_five_after:
    $ vn_enter(bg="grh_pool", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_ledge_end")
    "Somewhere in the middle of it he hauled you up out of the water onto the warm stone ledge: you on your back, spread wide, his hands pinning your thick thighs open, Kite over you like a wall of feathers with his wings rattling in the sun. You gave orders the whole way. {i}Get off. Get out. Stop.{/i} He didn't do a single one. And then the orders changed, somewhere you didn't notice, and you were still shouting them, just different ones. {i}Harder. Deeper. Don't stop.{/i} He did every one of those, in order, and told you so."
    grh_kite "\"Coming. Filling you. Mine.\""
    "He says it flat as ever, and jerks hard into you. And you go with him, hips pitching up off the stone, your cunt milking him, your nails dug into the base of his wings."
    grh_you "\"Fill me— I {i}HATE{/i} you— don't stop— {i}don't stop{/i}— fill me till it runs out of me—\"" with vnfx("shake")
    "It does. It runs out of you, hot, down onto the stone."
    show cg grh_palm_belly onlayer cgl
    "His palm spreads on your belly. And stays there."
    "You lie on the hot stone, panting, and shove it off. It comes back. You shove it off again."
    show grh_pc stubborn
    grh_you "\"I'm leaving. Five pieces tonight. I'm still {i}leaving{/i}.\""
    "You tell the sky. The palm comes back."
    hide cg onlayer cgl
    "{color=#ff5fb8}Your new cunt learned to milk him on the very first try, with your mouth shouting no the whole time.{/color}"
    $ grh.fit = "flannel"
    "You get the flannel back round your hips with your hands shaking.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_five

label grh_dusk_five:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_rucksack")
    "In the afternoon you check on the rucksack. Still packed. The job's address still in the front pocket. You give it a pat, and leave it in its corner."
    hide cg onlayer cgl
    "At dusk he sings, and you hum along with the low part, under your breath, so he won't hear."
    $ grh_rope(5)
    "The scarf goes on, knot over knot, and you say it."
    show screen grh_rope(5)
    grh_you "\"[GRH_ROPE[5]['count']]\""
    hide screen grh_rope
    "[GRH_ROPE[5]['reach']]\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_five

label grh_night_five:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "The nest's different tonight. Or you are. You don't fit the hollow you've been sleeping in: your hips catch on one side and your tits on the other, and you have to turn and turn, swearing, like a man fighting a sleeping bag, until the straw gives."
    show grh_pc flushed
    "You lie on your back and look at the stars and feel it all. The weight on your chest, rising and falling. The new soft heat between your thighs, still slick, still tender-in-a-good-way, still full of noon. You press your thighs together and a little aftershock rolls up through you and you bite your lip on a moan."
    grh_you "\"{i}Mmh{/i}...\""
    "In his sleep, Kite rolls toward the sound. His big palm finds your belly and spreads there, warm and heavy, and stays."
    "You pick it up by one finger and drop it off you. It comes back. You're too wrecked to do it twice."
    call vn_night(6)
    jump grh_dawn_six

## ---- DAY 6: bred; the back itch, the washing line, on top of him at night; rung 6 -------------

label grh_dawn_six:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "Kite's palm is on your belly when you wake up. All morning it keeps finding its way back there."
    $ grh_body(6)
    show cg grh_heavy onlayer cgl
    "{color=#ff5fb8}You roll over and your tits roll with you. {i}Heavy.{/i} Swaying. Big enough now that they swing when you bend and slap together when you sit up fast.{/color}"
    show grh_pc flushed
    "{color=#ff5fb8}Nothing up here would close over them. You don't even try. You just hold them, both hands, heavy and warm, thumbs on the nipples, and moan into the morning.{/color}"
    grh_you "\"{i}Mmmmh{/i}— god, {i}look{/i} at them—\""
    "{color=#ff5fb8}Your hips are thick. Your arse is thicker: a soft round shelf of it behind you, and your tail rides right on top. You reach back and grab a cheek and it spills out of your hand, and you squeeze it, and moan at your own grip.{/color}"
    grh_you "\"Oh, {i}fuck{/i}— that's— that's {i}mine?{/i}—\""
    "{color=#ff5fb8}Your thighs rub together all the way down when you walk, soft on soft, every single step. You walk to the pool and back just to feel them do it. You walk it again.{/color}"
    "{color=#ff5fb8}Your face in the pool is full-lipped and soft and nobody's but a woman's, and your hair's spilled past your shoulders now, black curls and dark feathers down your back. When you swear at it, your voice comes out light and husky.{/color}"
    "{color=#ff5fb8}Everything's turned up again. Your nipples throb under your own thumbs, your arse tingles where it sits on the stone, your cunt's slick from nothing, and your lips feel so fat and tender you keep licking them and moaning.{/color}"
    show grh_pc stubborn
    grh_you "\"Pool water. It's the pool water.\""
    hide cg onlayer cgl
    "You decide it. And between your shoulders: an itch. Deep, under the blades. It doesn't let up all day.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(9)
    jump grh_gift_six

label grh_gift_six:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_quilt")
    "He drops [GRH_GIFTS[6]['gift']]. The quilt goes in the nest, obviously. The jacket's lined with blue wool, thick and soft, and you can already see the strip you'd tear out of it."
    menu:
        "He waits, head on one side."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"Thanks.\""
            "It comes out with no knife in it at all. You hear it. You hate it."
            show grh_kite pleased
            "He opens up like noon. He hums all morning. You sit on the rope's corner of the nest with your arms folded and pretend nothing happened."
        "Scold him":
            $ grh.gift = "scold"
            grh_you "\"{i}Another{/i} quilt? We've got {i}loads{/i} of quilts! Where do you think it's all {i}going?{/i}\""
            "He listens to every word. Then he grooms you, slow, right where the itch is, between the shoulder blades, and you forget what you were shouting about."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look through it."
            grh_kite "\"Sky is too big alone.\""
            "He tells the perch. Then [GRH_GIFTS[6]['crack']] in your lap."
            grh_you "\"{i}Thanks{/i}.\""
            "Too high, mouth already full."
    "The jacket goes on the pile by the rope's corner.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_noon_six

label grh_noon_six:
    $ grh.fit = "nude"
    $ vn_enter(bg="grh_pool", pc="flushed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_pool_six")
    "Noon, the pool. Kite washes you, slow, all of you. Your heavy tits float on the water and bob against his forearms, and he washes under them, round them, over the fat nipples until you're squirming."
    grh_you "\"{i}Mmh{/i}— stop— not there— not— {i}there{/i}— I said not there—\""
    "He doesn't do what you say. He never does. He washes where he likes. And his hands keep ending up on your belly. Both palms. Spread wide. Like he's keeping it warm."
    show grh_pc stubborn
    grh_you "\"It's flat. It's a flat stomach. Look. Flat.\""
    grh_kite "\"Good.\""
    "He agrees, and doesn't move his hands."
    show cg grh_scratch onlayer cgl
    "Then the itch hits between your shoulder blades and you scratch your back on the cistern's edge like a man with sunburn, rubbing up and down the stone with your tits slapping the water, moaning about it, loudly. He watches you do it with a look you don't want to read."
    hide cg onlayer cgl
    $ grh.fit = "flannel"
    "You climb out and tie the flannel back on.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_six

label grh_dusk_six:
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_scope_washing")
    "In the afternoon you take the telescope to look for the road, and you end up on a farmhand's washing line instead."
    "White shirts. A flannel. A towel. You go along them one at a time."
    grh_you "\"That one'd tear lovely. Long seams. That one's a blend, useless, it'd just stretch. That one— oh, that {i}sleeve{/i}—\""
    hide cg onlayer cgl
    "You catch yourself. You've been grading strangers' laundry for a solid quarter of the afternoon. You snap the telescope shut and stomp off, flannel skirt flicking."
    "At dusk he sings."
    $ grh_rope(6)
    "The blue wool comes out of the jacket in one long strip, and you knot it on, and you say it out loud."
    show screen grh_rope(6)
    grh_you "\"[GRH_ROPE[6]['count']]\""
    hide screen grh_rope
    "[GRH_ROPE[6]['reach']]\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_six

## Rung 6's act: bred, on top. The first night's line comes back as a statement, and this time "No."
## gets "No asking now." He lifts you onto him and holds your hips down. Never flipped.
label grh_night_six:
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "In the nest, he looks at you exactly the way he did that first night."
    grh_kite "\"Touch you now.\""
    "You roll over, heavy tits swinging, and look him dead in the eye."
    show grh_pc furious
    grh_you "\"No.\""
    grh_kite "\"No asking now.\""
    menu:
        grh_you "\"You {i}never{/i} asked! You've never asked once! You just say it like the {i}forecast{/i}—\""
        "Keep shouting at him":
            $ grh.no = "swear"
            grh_you "\"—and another {i}thing{/i}—\""
            "You're saying it when his hands close round your waist, and lift."
        "Shove his chest and roll away":
            $ grh.no = "shove"
            "You shove his chest and roll. You get about half a roll. His hands close round your waist and lift you out of it."
        "Turn your back on him and say nothing":
            $ grh.no = "silent"
            "You turn your back on him and say nothing at all. His hands close round your waist from behind, and lift."
    $ grh.fit = "nude"
    show cg grh_ride_lift onlayer cgl
    "And then you're on top of him. Straddling his hips, thighs spread wide over him, tail up, tits hanging heavy right over his face, and his hands clamped on your hips holding you there."
    grh_you "\"Off— let me {i}off{/i}—\""
    "You push up on his chest. His hands push down on your hips. His win."
    "His cock's already up hard against your arse. He rocks you on it, slow, the whole length of it sliding hot along your slit, back and forth, and you're so wet it's obscene, {i}shlk, shlk{/i}, dripping on his belly feathers."
    show grh_pc flushed
    grh_you "\"That's— {i}don't{/i}— you're {i}moving{/i} me—\""
    "One hand lets go of your hip to fill itself with your tit. All of it, and still spilling. He weighs it. He squeezes. You grab his wrist to pull it off, the way you did at the pool, and it goes about as well."
    grh_you "\"{i}Ohhh{/i}— no— {i}no{/i}— don't squeeze them— don't— {i}harder{/i}— no, I didn't— {i}nnh{/i}—\""
    grh_kite "\"Heavy.\""
    "He says it, approving, and rolls the nipple between finger and thumb. Then the palm slides down and spreads over your belly. And stays there."
    grh_kite "\"Mate is bred. Good.\""
    "His other hand finds your hip again. Both of them, now. He lifts you, lines you up, and starts bringing you down.\n{size=-5}{color=#ff8fa3}▸ {i}Hnnngh{/i}—!{/color}{/size}"
    jump grh_ride_sex

label grh_ride_after:
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "pleased")], cg="grh_ride_end")
    "When he comes, his palm presses flat on your belly and his other hand holds your hip down on him, all the way, and fills you while you grind and moan and bounce through the last of it, still telling him to let you up."
    "When he finally lets you climb off, it runs down the insides of your thighs, warm and slow."
    grh_kite "\"Mate is bred.\""
    "He says it again, very satisfied, to the stars."
    show grh_pc stubborn
    grh_you "\"Six pieces. One to go.\""
    hide cg onlayer cgl
    "You tell the stars back, hoarse."
    "{color=#ff5fb8}Riding, squeezing him with your thighs, your tits shoved into his hands: your body knows every move now. Nobody asked it.{/color}"
    call vn_night(6)
    jump grh_dawn_seven

## ---- DAY 7: the wings and "Wife.", the knapsack, seven pieces, the lip; rung 7 ----------------

label grh_dawn_seven:
    $ grh.fit = "flannel"
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_hum")
    "The song at dawn, and you hum along under your breath. Badly. On purpose, so it doesn't count."
    "He hears anyway. His head tips toward you on the perch, and he holds one long note an extra beat, like he's waiting for you to catch up. You stop humming. He keeps holding it. You start again, furious, and he goes on."
    hide cg onlayer cgl
    "The itch between your shoulders is so bad this morning that you scrape your back up and down the flagstones like a man with the worst sunburn of his life, groaning."
    grh_kite "\"Itch.\""
    grh_you "\"{i}Thank{/i} you, Kite.\"\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    $ vn_until(9)
    jump grh_gift_seven

label grh_gift_seven:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_gift_velvet")
    "He comes up out of the sky with [GRH_GIFTS[7]['gift']], half-rotten, smelling of somebody's attic, and starts stuffing it into the nest before he's even landed properly."
    menu:
        "He packs it in round the hollow, and looks at you."
        "Thank him":
            $ grh.gift = "thank"
            grh_you "\"Thanks. It's horrible. Thanks.\""
            show grh_kite pleased
            "He opens up like noon and hums at the nest while he packs it."
        "Scold him":
            $ grh.gift = "scold"
            grh_you "\"It's {i}rotten{/i}. It's falling apart in your {i}hands{/i}. The nest doesn't need any more— the nest is {i}huge{/i}—\""
            "He listens, nodding, and keeps packing it in. Then he grooms your itching back, both hands, slow, until you're face-down in the velvet moaning."
        "Ignore it":
            $ grh.gift = "ignore"
            "You look through it."
            grh_kite "\"Sky is too big alone.\""
            "Then [GRH_GIFTS[7]['crack']], polished on his forearm, set down by your hand."
            grh_you "\"{i}Thanks{/i}.\""
    "The velvet's too rotten for a knot. You don't even look at it for the rope.\n{size=-5}{color=#ff8fa3}▸ Noon{/color}{/size}"
    $ vn_until(12)
    jump grh_noon_seven

label grh_noon_seven:
    $ grh.fit = "nude"
    $ vn_enter(bg="grh_pool", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "At the pool the itch has gone deep. The muscles under your shoulder blades clench on their own and let go, clench and let go, and every time they do, Kite looks up from the water."
    "You sink in up to your chin to make it stop. It doesn't. It goes on, a deep rolling pull under your skin like something stretching in its sleep."
    grh_you "\"What. {i}What.{/i} What are you looking at.\""
    grh_kite "\"Back.\""
    grh_you "\"What about my back?\""
    show grh_kite pleased
    "He doesn't say anything else. He just looks very, very pleased, and hums the first bar of the dusk song, early."
    $ grh.fit = "flannel"
    "You get out, and tie the flannel on, and glare at him.\n{size=-5}{color=#ff8fa3}▸ Afternoon{/color}{/size}"
    $ vn_until(15)
    jump grh_wings

## Row 7 lands: the wings, and the woman's body to match. "Wife." is the "she" beat, and the
## misreadings stop here.
label grh_wings:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "In the middle of an ordinary afternoon it happens like a trap going off backwards."
    "The itch builds and builds, and the muscles under your shoulder blades clench, and clench, and then let go all at once—"
    $ grh_body(7)
    vn_sfx "{i}FWUMP.{/i}" with vnfx("shake")
    show cg grh_wings_burst onlayer cgl
    "{color=#ff5fb8}Wings. {i}Your{/i} wings. They burst out of your back, huge, dark on top and going grey at the long flight feathers, and they sweep the whole chamber in one go: every gift pile flat, the telescope sideways, straw everywhere.{/color}"
    "{color=#ff5fb8}You stand there braced on the broken wall with your mouth open, and they move on their own, breathing with you, the long feathers rattling.{/color}"
    "{color=#ff5fb8}And the rest of you's been going all day under the itch. Your tits are big now, high and heavy, swinging when you turn. Your hips are wide, and your arse has gone round and heavy enough to sway behind you on its own. Your hair falls long and feathered down your back, and under it the face in the pool is a woman's, every bit of it, with gold eyes. Low under your navel there's a softness. Round and warm, when you put your hand there.{/color}"
    show grh_pc overwhelmed
    grh_you "\"{i}Fuck{/i}. {i}FUCK.{/i} Look at— look at {i}me{/i}— oh god. Oh {i}god{/i}, look at me—\""
    "{color=#ff5fb8}It's a woman's voice saying it. Hands on your tits, on your hips, on that soft low swell, on the new heavy wings at your back. And all of it's louder: your lips, your nipples, your cunt, the round of your arse. The draught off the wings across your bare skin nearly makes you come on the spot.{/color}"
    hide cg onlayer cgl
    show grh_kite flat at vn_cast_slot
    "Kite lands across from you. No fuss, no song. Just a long, calm look. The face, the gold eyes, the hair. The tits and the hips and the round arse and the soft low belly. And the wings, framing all of it."
    show grh_kite pleased
    "He nods once. Deeply satisfied."
    grh_kite "\"Wife.\""
    $ grh.called = "wife"
    show grh_pc stubborn
    "You blink at him. Then you look past your own tail at the wreck the wings have made of everything."
    grh_kite "\"Strong. Grown well. Fliers' bones.\""
    "He tests one of them with his hand, shoulder to tip. You swear at the mess in a woman's voice, light and husky, and for the next hour every turn you make knocks something else flat."
    $ vn_enter(bg="grh_perch", pc="flushed", pc_tag="grh_pc", cast=[("grh_kite", "pleased")], cg="grh_flight_lesson")
    "Then he's on the perch, already teaching. Wings beating in slow motion. Thunder. All lift."
    "You climb up after him and try it. It's carnage. Your wings flail and slap the flagstones and smack him in the flank so hard he grunts, and then he's laughing, head down, feathers shaking. You bring both down at once, feel a lift, and go straight over backwards onto your tail."
    grh_you "\"It's the {i}wind!{/i} The wind's wrong!\"\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_dusk_seven

label grh_dusk_seven:
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_duet_try")
    "At dusk he takes his place on the perch and starts the song. You climb up beside him, feeling reckless, and join in."
    "It's appalling. A cracked, wobbling honk, all throat and none of the right notes, sliding off every one of them. You flap for emphasis. It gets worse."
    "Kite doesn't miss a note."
    grh_kite "\"Good try. Loud. Sky hears you.\""
    "You stick your tongue out at him."
    hide cg onlayer cgl
    show cg grh_knapsack onlayer cgl
    "Then he drops a gift on the parapet: a knapsack, torn open, liner and all. White canvas. Strong and long and unbroken. Exactly what you've been waiting for."
    $ grh_rope(7)
    "You split it down its length, work the strip into the rope under the straw and tie it off with a double knot, fingers sure. You say it out loud before you can stop yourself."
    show screen grh_rope(7)
    grh_you "\"[GRH_ROPE[7]['count']]\""
    hide screen grh_rope
    $ vn_enter(bg="grh_lip", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_rope_down")
    "You run the whole thing through your hands, knot by knot. At the lip, you let it all down into the dark."
    "[GRH_ROPE[7]['reach']]"
    "Your heart thuds like you've won something."
    "You haul it back up and coil it and push it under the straw, untouched, ready."
    "The wind's howling straight up the drop into your face. Wrong. It'd slam anybody back into the rock."
    "You say it to the wind, eyes shut."
    grh_you "\"Not yet.\""
    "It's true. The wind is wrong. It rattles the old stones to prove it.\n{size=-5}{color=#ff8fa3}▸ Night{/color}{/size}"
    $ vn_until(21)
    jump grh_night_seven

## Rung 7's act: the lip, the wrong wind. He catches you at the lip with the rope in your hands and
## bends you over the edge, face toward the yard the rope now reaches. Never flipped. The rope stays
## an escape plan.
label grh_night_seven:
    $ vn_enter(bg="grh_lip_night", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_lip_rope")
    "Night. He's out on his night flight, and the wind's still howling up the drop, and you're at the lip with the rope."
    "Not going. The wind's wrong. You're just checking. You let it down into the dark one more time and feel it go slack when it touches the yard, and you lie on your belly on the broken stone with the rope in both fists and your new wings folded tight, looking down at where it ends."
    "Seven pieces. All the way down."
    vn_sfx "{i}Whumm.{/i}"
    hide cg onlayer cgl
    show grh_kite flat at vn_cast_slot
    "He comes up out of the dark with the wind tearing at his feathers and lands right behind you. You scramble up onto your knees and get the rope behind your back, like a shoplifter."
    "He looks at the rope. He looks at the yard. He looks at you."
    grh_kite "\"Rope is long. Not long enough.\""
    show grh_pc furious
    grh_you "\"It {i}touches{/i}. It touches the ground. I'm going the second this wind—\""
    "His hand closes in your long feathered hair."
    menu:
        grh_kite "\"Mouth first. Then here. Now.\""
        "\"Not HERE— not at the edge—\"":
            $ grh.no = "swear"
            grh_you "\"Not {i}here{/i}— not at the edge, Kite, not with the— are you {i}listening{/i}—\""
        "Shove his chest and hang onto the rope":
            $ grh.no = "shove"
            "You shove his chest with one hand and hang onto the rope with the other. Neither does anything."
        "Glare up at him and say nothing":
            $ grh.no = "silent"
            "You glare up at him and say nothing. You can do nothing for a whole breath, nearly."
    $ grh.fit = "nude"
    show cg grh_lip_mouth onlayer cgl
    "His fist brings you down onto your knees on the broken stone and his cock across your lips, and you're swearing round it before it's even in."
    grh_you "\"{i}Mmmmf{/i}— {i}mmh{/i}—!\""
    "The wind whips your hair across his thighs. He holds your head and fucks your mouth slow and deep until he's iron on your tongue, about a breath, and you're drooling down your tits and still trying to say no round him."
    show cg grh_lip_bent onlayer cgl
    "Then he lifts you, turns you, and bends you over the lip."
    "Broken stone under your thighs. Nothing under your face but air and dark and the wind coming up it like a train. And there, straight below you, the rope: your rope, seven pieces, hanging down the wall, white canvas at the bottom, touching the yard. Your wings fling open for balance all on their own."
    show grh_pc overwhelmed
    grh_you "\"Kite— {i}Kite{/i}— not over the— I can {i}see{/i} it, I can see the—\""
    grh_kite "\"Look down. Rope is there. Wife is here.\""
    "His forearm locks across your waist and holds you on the edge."
    "His fingers spread you. You're soaking. You hate that you're soaking. His thumb finds your clit and rubs tight little circles, and your hips jerk back against his hand, and you swear at the yard."
    grh_kite "\"Open. Good. Wet. Wife is ready.\""
    grh_you "\"I'm {i}not{/i}— I'm not ready, I'm not— {i}don't{/i}—\"\n{size=-5}{color=#ff8fa3}▸ \"DON'T— don't you—\"{/color}{/size}"
    jump grh_lip_sex

label grh_lip_after:
    $ vn_enter(bg="grh_lip_night", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_lip_end")
    grh_kite "\"Wife— open— take it—\""
    "At the end he holds your whole weight on one forearm on the crumbling edge like it's nothing. And you scream. Your wings snap wide and catch so much wind you pitch back into his arms, and he hauls you in tight and keeps going, and going."
    "It's running down your thighs. Hot. Down the backs of your knees and onto the stone."
    grh_kite "\"Wife takes it all.\""
    grh_you "\"Don't— you— {i}dare{/i}— stop—\""
    "It comes out of you, which is not what you were trying to say at all. You were trying to say get off. You were trying to say it the whole time."
    "He doesn't stop."
    hide cg onlayer cgl
    show cg grh_coil onlayer cgl
    "After, when he's asleep, you crawl back to the lip on your knees and haul the rope up, hand over hand, and coil it, and push it back under the straw. Seven pieces. Ready. The wind can't be wrong forever."
    hide cg onlayer cgl
    "{color=#ff5fb8}Down on your knees and then bent over the edge: your mouth and your cunt both know him by heart now. Neither of them asked you.{/color}"
    call vn_night(6)
    jump grh_dawn_eight

## ---- DAY 8: the ending, "Not Yet" ----------------------------------------------------------

## Dawn at her biggest (row 8, the growth climax and the route's one cup letter).
label grh_dawn_eight:
    $ grh.fit = "nude"
    $ vn_enter(bg="grh_tower", pc="overwhelmed", pc_tag="grh_pc", cast=[], cg=None)
    "You wake at dawn and there is just so {i}much{/i} of you."
    $ grh_body(8)
    show cg grh_biggest onlayer cgl
    "{color=#ff5fb8}Your tits first. Huge. Heavy. Squashed into your arms where you slept on them: one mashed against your bicep, the other spilling off the edge of the straw with its nipple cold in the air. You try to roll over. You can't. Your chest gets there first and pins you, arse up, tail flopped, wings everywhere, a whole quilt of feathered hair across your face.{/color}"
    grh_you "\"{i}Mmmmf{/i}— oh my {i}god{/i}—\""
    "{color=#ff5fb8}You heave yourself up with both hands. Your hips are so wide you have to throw them forward just to get going. Your arse is enormous, round and soft and heavy, and sinks half the nest every time you shift your weight. Your thighs are enormous, pressed together all the way down, soft on soft, hot.{/color}"
    "{color=#ff5fb8}And in the middle of all of it, your waist's pinched in so tight that the old belt off your jeans goes round it with half its length flapping spare. Under your navel, low, there's a swell. Tight and round and warm. Your hands go to it on their own.{/color}"
    "{color=#ff5fb8}Your hair's long enough to sit on. Black curls and dark feathers, everywhere.{/color}"
    "{color=#ff5fb8}You grab your tits with both hands. They overflow everything: your palms, your fingers, your wrists. Somewhere past a J, if anyone up here sold bras, and so {i}sensitive{/i} that squeezing them makes your thighs clench—{/color}"
    show grh_pc flushed
    grh_you "\"{i}Ahhh{/i}— fuck, fuck, look at them, look at {i}me{/i}— I'm so {i}big{/i}— {i}Kite!{/i} Kite, {i}look{/i} at me—!\""
    "{color=#ff5fb8}You squeeze and moan, and your voice rings off the walls, clear, a woman's, with nothing left of the old one in it. Your lips are so swollen and tender that the dawn air on them feels like a kiss, and when you squeeze your thighs together your cunt throbs so hard you moan again.{/color}"
    "{color=#ff5fb8}Behind you your wings stretch out, full-grown. Higher than the parapet.{/color}"
    hide cg onlayer cgl
    show grh_kite flat at vn_cast_slot
    "Kite looks. He looks for a long time."
    show grh_kite pleased
    grh_kite "\"Wife is big. Good.\"\n{size=-5}{color=#ff8fa3}▸ The wind{/color}{/size}"
    $ vn_until(9)
    jump grh_flight

## The wind is right: one launch, round the moor, and the wind turns head-on. You come back because
## the wind turns and the belly drags, not because you chose to.
label grh_flight:
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "The wind's changed."
    "It's coming up the side of the spur soft and steady, warm off the moor, lifting your feathers before you've even moved."
    "It's {i}right{/i}. You can feel that it's right, the way you can feel your own hand."
    show cg grh_launch onlayer cgl
    "You climb up onto the perch, spread your wings as wide as they'll go, and jump."
    $ vn_enter(bg="grh_sky", pc="flushed", pc_tag="grh_pc", cast=[], cg="grh_flying")
    "One launch. Strong as hell. The air catches under you like a hand and throws you up, and up, and the tower drops away under your feet, and there's the moor rolling out below you: purple and brown, green in the hollows, the road, the farm, the whole enormous sky."
    "You're flying."
    grh_you "\"{i}HAHAHA{/i}— oh my god— {i}OH MY GOD{/i}—\""
    "You circle the moor once. Wide. The ruined farmhouse, the grey road, the far smudge of the town. Your tits bounce, your hair streams out behind you, your tail steers all on its own."
    "Then you point yourself at the town and {i}go{/i}."
    grh_you "\"{i}Bye!{/i} {i}BYE, KITE!{/i} Keep the {i}rope!{/i}\""
    "You yell it back at the spur. And the wind turns."
    show cg grh_headwind onlayer cgl
    "Just like that, halfway across the heather. It swings round and comes at you head-on, and you beat into it, and beat, and the low round weight under your navel drags at you like a full shopping bag, and the town gets no closer. Your wings shake. You drop. You beat. The road under you crawls backwards."
    show grh_pc furious
    grh_you "\"No— no, {i}no{/i}, come {i}on{/i}— you were {i}right{/i} a second ago—\""
    "The wind doesn't care. It shoves you round in a long slow curve, and the only thing in front of you with the wind at its back is the spur."
    $ vn_enter(bg="grh_perch", pc="furious", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_landing")
    "You come down on the perch in a heap of feathers, panting, every muscle in your back singing, swearing at the sky in a woman's voice at the top of your lungs."
    "Kite's on the parapet. He doesn't say anything. His eyes are very bright."
    grh_you "\"Don't. Don't you {i}dare{/i}. The wind turned. It {i}turned{/i}.\"\n{size=-5}{color=#ff8fa3}▸ Afternoon{/color}{/size}"
    $ vn_until(13)
    jump grh_unpick

## The rope's only use: the nest needs lining for her heavy body. Then the telescope's last sweep and
## the rucksack: "Not yet." -- said as defiance, not affection. You are still leaving.
label grh_unpick:
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[], cg=None)
    "Your body's too heavy for the nest now. You sink straight through it to the stone. It needs lining."
    "You look round the tower for something soft. Every shirt, every scrap of fleece, every quilt, every armful of velvet he ever carried up here: it's all in the nest already."
    "There's one thing left."
    show cg grh_unpick onlayer cgl
    "You drag the rope out from under the straw."
    $ grh.unpicked = True
    "You unpick every piece of it. And every double knot, every stupid tight double knot you ever tied with your teeth: you swear at it."
    show grh_pc furious
    grh_you "\"Why did I tie it so {i}tight?{/i} Who was I {i}expecting?{/i} Fine. {i}Fine.{/i} I'll knot a better one. I've got wings now, I don't even {i}need{/i} one—\""
    show cg grh_lined onlayer cgl
    "You pry. You chew. You swear. The cuff. The coat. The sleeve, the webbing, the scarf, the blue wool, the white canvas. Back into strips, every one, and round the bowl of the nest, twice over, soft and warm, and when you sink into it, it holds you."
    hide cg onlayer cgl
    show grh_pc stubborn
    "You announce to nobody that you're starving, and go and eat a whole pie."
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_scope_sky")
    "Then the telescope. One sweep: the road, the farm, the washing line, the far edge of the moor. Nothing you want. You leave it pointing at the sky."
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_rucksack_feathers")
    "The rucksack's in its corner. Still packed. The job's address still in the front pocket, and a few dark feathers stuck to the canvas now."
    "You look at it for a good long while. Kite's watching you from the perch; you can feel it on the back of your neck."
    hide cg onlayer cgl
    "You turn round so he can see your face when you say it. Out loud, as clear as you can say it, straight at him:"
    grh_you "\"Not yet.\""
    "Not {i}never{/i}. Not yet. The next right wind, you're gone. Let him chew on that.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump grh_duet

## The ending's act: dusk, the perch. "Here or nest." is his choice, not yours; every choice is how
## you refuse. Never flipped: the duet is torn out of you at the climax.
label grh_duet:
    $ vn_enter(bg="grh_perch_dusk", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg=None)
    "Dusk. You're on the perch with your arms folded over your huge tits, watching the wind, waiting for it to turn back. Kite hasn't started the song yet."
    "He comes up behind you. You feel the size of him at your back, then his hands on your hips, then his wings coming round."
    grh_kite "\"Wife.\""
    show grh_pc furious
    grh_you "\"No.\""
    "His gold eyes catch the last of the light. He looks at the nest, and at the parapet, and decides. You can watch him decide."
    menu:
        grh_kite "\"Here or nest.\" A dip of his head. \"Here.\""
        "\"I'm not your WIFE—\"":
            $ grh.no = "swear"
            grh_you "\"I'm not your {i}wife{/i}— I never said {i}anything{/i}— I'm going the {i}second{/i} that wind turns back, you hear me? The {i}second{/i}—\""
        "Shove his chest and try for the edge":
            $ grh.no = "shove"
            "You shove his chest and lunge for the edge, wings half open. His wing comes down across the gap like a barrier arm. You hit it, and bounce, and you're back in his hands."
        "Stare out at the moor and say nothing":
            $ grh.no = "silent"
            "You stare out at the moor and say nothing. The moor says nothing back. His hands slide round from your hips to your belly."
    show cg grh_parapet onlayer cgl
    "He backs you up against the lowest block of the parapet, big hands on your hips, and pins you there with his body. Your wings jerk open behind you on their own and hit the stone."
    "He kneads your arse, spreads you wide, then slides his hands up and cups your tits, a whole palm each and still spilling, and lets the weight rest there. Squeezes until you gasp."
    grh_kite "\"Wife is big tonight. Full hands. Made for me.\""
    grh_you "\"Made for {i}flying away{/i}— {i}ahh{/i}—\""
    show cg grh_nipple onlayer cgl
    "He bends and takes your nipple in his mouth and {i}sucks{/i}, hard, his thumb flicking the other one."
    show grh_pc flushed
    grh_you "\"{i}Ahh{/i}— fuck— {i}Kite{/i}— get your mouth— get {i}off{/i}— that's not— I'm {i}pulling{/i}— I'm pulling you {i}off{/i}—\""
    "Your hand goes into the feathers at the back of his head to drag him away, and grabs, and holds him there instead."
    "He lets go with a wet {i}pop{/i}. One thick thigh goes up round his hip in his hand. The head of him presses blunt and hot against you."
    grh_kite "\"Inside now.\""
    grh_you "\"Don't— don't, not tonight, not {i}here{/i}, the whole moor can— {i}don't{/i}—\"\n{size=-5}{color=#ff8fa3}▸ \"KITE—\"{/color}{/size}"
    jump grh_duet_sex

## The duet: at her climax the dusk song comes up out of her right for the first time, his voice
## locks under it, and the whole moor shuts up to listen. Torn out of her, not offered.
label grh_duet_after:
    $ vn_enter(bg="grh_perch_dusk", pc="overwhelmed", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_duet")
    "At the very top of it, he angles in and hits something deep inside you, and everything locks."
    "And what comes out of your chest isn't the no you've been shouting."
    "It's the song."
    "The dusk song, {i}his{/i} song, ripped up out of you, up through your breastbone and out of your open throat, huge and wordless, and you didn't decide it, and you can't stop it, and for the first time ever it comes out {i}right{/i}. Every note you've honked and mangled on the perch lands square on his."
    "And Kite's voice locks in under yours and holds."
    "He's coming in you, deep, hot, pulse after pulse, and singing, and you're coming round him and singing, and it doesn't stop."
    show cg grh_moor_listens onlayer cgl
    "It rolls out over the whole moor. Over the heather and the road and the farm and the far edge of the town. Everything out there with feathers or ears just stops what it's doing, and goes quiet, and listens."
    show cg grh_duet onlayer cgl
    "It's the biggest thing that's ever come out of you. It's {i}enormous{/i}. It throws you into it, wings wide, tits heaving in his hands, and neither of you stops."
    "You come and come. Your cunt keeps clamping down on him in long rolling squeezes, your thighs shaking round his hips, your tail lashing, your nails in the base of his wings, and every squeeze pushes another note out of you, and every note is right, and in between them you're still trying to swear at him."
    grh_you "\"{i}Haaaah{/i}— {i}aaah{/i}— I {i}hate{/i}— Kite— {i}KITE{/i}—\"" with vnfx("shake")
    grh_kite "\"Wife sings. Good.\""
    "He says it into your hair, between notes, flat and delighted."
    hide cg onlayer cgl
    "When it finally fades, the moor stays quiet for a long time after, like it's waiting to see if you'll do it again. You're slumped against the parapet, wrecked, and he's slipping out of you, and it runs down out of you, hot, onto the old stone."
    show grh_pc stubborn
    grh_you "\"That didn't count. That was {i}him{/i}. That didn't {i}count{/i}.\""
    "You croak it at the moor. The moor doesn't argue."
    "{color=#ff5fb8}You know him now: your mouth, your cunt, your arse, your tits. Every way there is. All of it, by heart, and not one bit of it with your say-so.{/color}\n{size=-5}{color=#ff8fa3}▸ Let the moor go quiet{/color}{/size}"
    jump grh_not_yet

## The ending, "Not Yet": the feat, the keeper (his feathers, double-knotted), then the epilogue.
## The two choices decide the ending (owner, 2026-11-11: mark them).
label grh_not_yet:
    $ grh.ending = "not-yet"
    $ achievement.grant("Not Yet")
    $ vn_enter(bg="grh_nest_night", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_lined_nest")
    "Night on the spur."
    "The nest is lined with seven pieces of unpicked rope, and you're sunk deep in the middle of it, too big to roll over, Kite's wing over the both of you like a roof."
    "The rucksack's still in its corner. Still packed."
    "You still haven't said you're staying. You haven't said anything about it at all."
    $ vn_enter(bg="grh_tower", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "pleased")], cg="grh_necklace")
    grh_kite "\"Wear. Wings stay.\""
    "In the morning Kite drops one more gift in your lap: a string of his own dark feathers, knotted, of course, with a double knot."
    hide cg onlayer cgl
    menu:
        "The string of feathers in your lap. The rucksack in its corner."
        "\"Not yet.\"" (ending=True):
            jump grh_epilogue_stay
        "Fly the rucksack to town" (ending=True):
            jump grh_epilogue_rucksack

label grh_epilogue_stay:
    $ grh.epilogue = "stay"
    $ vn_enter(bg="grh_perch", pc="stubborn", pc_tag="grh_pc", cast=[("grh_kite", "flat")], cg="grh_epi_song")
    "The days on the spur go the way days go up here."
    "The song at dawn, and you sing it with him now. Badly, mostly. Right, sometimes. A gift every morning, and you thank him, or you shout at him, and either way he comes and grooms you after. The pool at noon. The perch at dusk."
    "In a few nights the swell under your navel will be gone, the way the stairs went: there one day, and then not."
    show cg grh_epi_fly onlayer cgl
    "Some mornings you fly. Out over the moor and round, and back. Always back."
    show cg grh_rucksack_feathers onlayer cgl
    "The rucksack stays in its corner, still packed, with the job's address in the front pocket and more feathers stuck to it every week."
    "You still haven't said you're staying. You haven't said anything about it at all.\n{size=-5}{color=#ff8fa3}▸ Up onto the perch{/color}{/size}"
    jump grh_route_return

label grh_epilogue_rucksack:
    $ grh.epilogue = "rucksack"
    $ vn_enter(bg="grh_sky", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_epi_carry")
    "You fly the rucksack to town."
    "It's a long way with it hanging off your arm, and the moor goes by under you, and then the roofs. You find the job's address from the front pocket. A grey door with a card in a little window."
    $ vn_enter(bg="grh_town_step", pc="stubborn", pc_tag="grh_pc", cast=[], cg="grh_epi_step")
    "You leave the rucksack on the step. Packed. Feathers and all."
    $ vn_enter(bg="grh_park", pc="flushed", pc_tag="grh_pc", cast=[], cg="grh_epi_park")
    "Then you land in the Park, in a whump of wings that flattens a whole flowerbed, and stand on the grass for a moment getting your breath back: the tits, the hips, the wings, the tail, the gold eyes, all of it, out in town in broad daylight."
    "You stick your tongue out at the whole town."
    hide cg onlayer cgl
    "The spur's a flight away. It always will be. Kite's on the perch, and he'll be singing at dusk, and you'll hear it from anywhere on the moor."
    "In a few nights the swell under your navel will be gone, the way the stairs went: there one day, and then not.\n{size=-5}{color=#ff8fa3}▸ Walk out of the Park{/color}{/size}"
    jump grh_route_return
