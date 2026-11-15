## bait's eleven chapters. THE LURE ANSWERS: ch 1-5 non-con, 6 the break, 7 Maren (no sex), 8 the flip (he asks
## Sable), 9-11 consensual. Each chapter: the panel, the dial, what answers, the souvenir, the number. Doujin
## register, gleeful; he narrates it all as a survival problem with an exit.
## The production rewrite (2026-11-13, twinetesting-c9; the owner: "Rewrite it first"): the book's beats on the page,
## a picture every beat, the encounters at full length. Plan, recasts, non-con pass and ending unchanged.
## Choices that carry: the panic (ch 1 -> ch 9), the dial (ch 2 -> ch 3), the word he writes (ch 2 -> ch 9), the first
## thing he rules out (ch 3 -> ch 10), what he shouts at the harpy (ch 4 -> ch 10), the kobolds' door (ch 5 -> ch 11),
## what he asks Maren (ch 7 -> ch 11), how he asks Sable (ch 8 -> ch 10), the petitions (ch 11).

## ---- 1. [Bait] ---------------------------------------------------------------------------------
label bai_ch1:
    $ bai.chapter = 1
    $ bai.fit = "trapper"
    $ vn_enter(bg="bai_forest", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_wake")
    "Dirt in your teeth. Cold moss packed against your cheek. You roll over with a groan, and the air in your lungs is deep-forest cold: pine, loam, and nothing anybody built."
    "The canopy overhead is fir and something like ash, and the light coming through it is the wrong colour. Not morning. Not evening. Something else."
    "No cars. No hum. No trail, except the print of your own face in the dirt."
    show screen bai_panel(1)
    "And hanging in the air in front of your nose, a translucent blue panel, crisp as a pop-up on a phone. NAME: THEODORE MARSH. STATUS: ALIVE. CLASS: [[Bait]."
    bai_you "\"Christ. Isekai. Not even a 'welcome, hero'? Shit translation, too. Bait? Come {i}on.{/i}\""
    "You poke at a word. Nothing. You swipe for EXIT, or MENU, or at least an explanation. Your finger slices empty air, and the panel drifts politely along with your eyes wherever you look."
    vn_th "(Okay. Okay. You can panic later. Logistics first.)"
    hide screen bai_panel
    show cg bai_wake_inventory onlayer cgl
    "Inventory. A thin tee hanging off narrow shoulders. Cargo shorts on skinny smooth legs. One sock, rolled down. Pockets empty. Shoes absent. You'd gone to bed in this, and you've never once in your life looked like a man who could survive a forest."
    bai_you "\"Great. Great. Transported to a fantasy world in my {i}sleep{/i} shorts. Somewhere a god is laughing.\""
    "Water, shelter, heat, direction: the rulebook comes back from somewhere. You lick a finger, check the wind, and pick downhill."
    $ vn_enter(bg="bai_cabin", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_cabin_coat")
    "Thirty minutes of survival logistics. A stream, fast and cold as a slap. Further down, a dead trapper's shack: a tumble of logs, a caved-in roof, gnawed boots, a rust-patched knife."
    "And a coat, stuffed under the only beam still standing. Fur-lined, far too big for your skinny frame, reeking. You put it on anyway, and you feel like a man with a plan."
    bai_you "\"Knife. Coat. Stream. Look at me. Day one, and I've got a base.\""
    "The bread in the corner crumbles to spores when you touch it. You take that as a sign to leave."
    $ vn_enter(bg="bai_forest", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_dial_appear")
    "Out on the porch, something very large knocks through the underbrush, out of sight. You go flat against the outer beam, heart stuttering."
    "It's a long way off. It's coming closer. You can hear it breathing, which is impossible, and you can smell it, which is worse."
    "And the panel, which has been sulking at the edge of your eye all morning, sprouts a new line: LURE, and beside it a dial, glowing, set to nothing."
    vn_th "(A dial. A dial is a control. Controls are good. You can work with a control.)"
    "Whatever's out there is moving closer. You're shaking. You have no idea what a lure does, except that it's the only button you've been given."
    menu:
        "The dial, glowing at nothing."
        "Inch it up, carefully":
            $ bai.panic = "inch"
            "A notch. Another. You feel it like a hand on the back of your neck, warm and spreading. Another notch, and then something big snaps a branch right behind you, and your hand spasms."
        "Slam it, and hope":
            $ bai.panic = "slam"
            "You don't think. You shove it with your whole palm, the way you'd hit a panic button, as if loud could mean safe."
    show cg bai_dial_high onlayer cgl
    "All the way. The air changes."
    "A scent rolls off you like heat off a road, thick and sweet and animal, and it doesn't stay outside you. It goes in. Your knees go. Your cock goes hard so fast it's dizzying, and the cold is suddenly nowhere."
    bai_you "\"{i}Hahh{/i}— what— what is— turn it {i}off{/i}— turn it—\""
    show cg bai_dial_heat onlayer cgl
    "You're on your knees in the leaves, panting, fumbling at the panel. Deep in the woods something enormous lifts its head. You can feel it lift its head."
    "You claw the dial back down so hard you nearly break it, and the enormous thing settles, and doesn't come."
    "What does come is smaller. Still huge."
    hide cg onlayer cgl
    jump bai_warg

label bai_ch1_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_cabin", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_crawl")
    "You crawl to the shack on your elbows. You pull the reeking coat over yourself on the floor, and you sleep, badly, and dream of weight and heat and the forest floor pressing into your cheek."
    vn_th "(Survival problem. That's all it is. A very specific survival problem.)"
    $ bai.fit = "trapper"
    $ bai_body(1)
    $ vn_enter(bg="bai_stream", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_morning_ears")
    "{color=#9fd8ff}Morning. In the stream: wolf ears, grey as your hair has gone overnight, and a tail, and a nose that reads the wind like a page.{/color}"
    "You touch an ear. It flicks. You touch the tail. It wags, the traitor."
    bai_you "\"Oh, come {i}on.{/i}\""
    show cg bai_tail_test onlayer cgl
    "{color=#9fd8ff}You try a run along the bank, and the ground blurs. Faster. Tougher. Your lungs don't burn. You could run all day, and some part of you wants to.{/color}"
    show screen bai_panel(1)
    "The panel has updated. ASPECTS: WARG. Senses, scent, stamina. And a line on its own: CYCLE (INSTALLED)."
    bai_you "\"Cycle installed? What the hell's a cycle? I'm not— that's not a thing I can have.\""
    hide screen bai_panel
    "Your chest is sore under the tee. The fight, obviously. You were face-down in the dirt for most of an afternoon."
    vn_th "(It took something and left something. Ears for… that. Fair trade, if you're a sociopath.)"
    vn_th "(Fine. Then the rule is: get strong enough to walk out. Use the trades. Don't get taken twice by surprise.)"
    show screen bai_number(1)
    bai_you "\"Strong enough to get out of this forest. That's all. That's the number.\""
    hide screen bai_number
    "It is the lowest the number will ever be."
    hide cg onlayer cgl
    call vn_night(8)
    jump bai_ch2

## ---- 2. The Math -------------------------------------------------------------------------------
label bai_ch2:
    $ bai.chapter = 2
    $ vn_enter(bg="bai_stream", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_notes")
    "Deliberate, this time. Chosen ground, chosen hour. A flat rock by the stream, a scrap of hide, a burnt stick for notes, like a man running an experiment."
    bai_you "\"Hypothesis: scent output increases linearly. Response curve of the wildlife, to be determined.\""
    "You grin at the panel. It hangs there, blue and patient."
    bai_you "\"Let's see how you work.\""
    menu:
        "The dial."
        "A quarter turn, and wait":
            $ bai.dial = "low"
            "A quarter turn. You note the time by the sun. You wait."
        "Half, and see what happens":
            $ bai.dial = "half"
            "Half. Science demands it."
    show cg bai_dial_climb onlayer cgl
    "Warm first. Then sharper: every sound in the woods arrives louder, every scent closer. Your cock fills inside the shorts, slow and steady, and you write that down."
    bai_you "\"Arousal: linear. Senses: sharper. Wildlife response: none.\""
    "Nothing comes. You turn it up. You log it. Nothing comes. Up again."
    show cg bai_notes_heat onlayer cgl
    "By the fifth entry your handwriting has gone to pieces and you're sweating in the cold, the stick wobbling, one hand pressed hard into your lap."
    bai_you "\"Entry five. Heart rate: high. Senses: very high. Erection: present and— {i}hahh{/i}— accounted for. Wildlife: still nothing. Is everybody {i}asleep{/i}?\""
    vn_th "(Data. This is data. You are a scientist having a completely professional erection.)"
    "And then the stream rises out of itself and keeps rising."
    hide cg onlayer cgl
    jump bai_slime

label bai_ch2_after:
    hide cg onlayer cgl
    $ bai_body(2)
    $ bai.fit = "trapper"   # dressed again after the stream (the 2026-11-13 art walk: he'd stayed nude through ch 4)
    $ vn_enter(bg="bai_stream", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_stretch")
    "{color=#9fd8ff}Nothing in the reflection. No change at all. Except that you stretch, now, without tearing. You test it idly, an arm out and out and out, and don't find a limit, and shrug.{/color}"
    bai_you "\"Elasticity? Slime logic, I guess. Cheaper than forking out for potions.\""
    "{color=#9fd8ff}Your hips have started, a bit. Your chest is plainly there under the tee. Residue, you decide. It'll go down.{/color}"
    show screen bai_panel(2)
    "The panel says [[Bait]. It says it like it means it."
    hide screen bai_panel
    show cg bai_notes_two onlayer cgl
    "You pick the stick back up. The second entry is sloppier than the first, written with a hand that won't quite stop shaking."
    menu:
        "What you write under ELASTICITY."
        "\"Free.\"":
            $ bai.free = "free"
            "FREE, you write, and underline it twice. Power at zero cost."
        "\"Free (?)\"":
            $ bai.free = "query"
            "FREE (?), you write, and then look at the question mark for a long time, and leave it."
    show screen bai_number(2)
    "Getting out isn't enough. You need to survive the trip out."
    hide screen bai_number
    hide cg onlayer cgl
    call vn_night(8)
    jump bai_ch3

## ---- 3. Reading the Woods ----------------------------------------------------------------------
label bai_ch3:
    $ bai.chapter = 3
    $ bai.fit = "trapper"
    $ vn_enter(bg="bai_forest", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_tracks")
    "You wake sensitive. The tee chafes. You can hear a beetle three trees over. You start shopping."
    "Dens, tracks, scat, sign, each one priced like a stall at a market. A lamia's shed skin draped over a root, long enough to wrap a car. An arachne's line strung across a gully, thick as a rope."
    show cg bai_survey onlayer cgl
    "Kitsune prints, nine-tailed in the mud. An orc midden, loud even empty. You lie in the ferns above an orc camp for an hour, taking notes on who shouts at whom."
    bai_you "\"Orcs: loud, social, eat everything. Hard pass. Lamia: long. Arachne: legs. Kitsune: clever, probably cheats. Dryad: rooted, slow, apparently feeds things. Interesting.\""
    if bai.dial == "low":
        vn_th "(A quarter turn got you a stream with ideas. Better not find out what a full one gets you near an orc camp.)"
    else:
        vn_th "(Half got you a stream with ideas. Better not find out what full gets you near an orc camp.)"
    menu:
        "The first thing you rule out."
        "The orcs":
            $ bai.ruled = "orcs"
            "The orcs, obviously. Loud, many, and they'd want to keep you."
        "The lamia":
            $ bai.ruled = "lamia"
            "The lamia. Anything that long can't be reasoned with in one sitting."
        "The arachne":
            $ bai.ruled = "arachne"
            "The arachne. Eight legs is a hard no. It's a principle."
    "All considered, priced, and ruled out for now. You're seeding a list, though you don't know it."
    hide cg onlayer cgl
    $ vn_enter(bg="bai_forest", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_myconid_find")
    "In a glade of pale glowing caps, something sits up out of the moss and smiles at you with a face like soft bread: a myconid woman, gills fanned at her shoulders, a broad cap shading her eyes."
    "Her breath is a sweet gold perfume. You recognise what she's good for at once: control. Calm. A crowd that settles when you walk in. You need that."
    vn_th "(Just a nudge. Enough to make her curious, and then you leave with the aspect and your dignity.)"
    "Your thumb goes to the dial."
    hide cg onlayer cgl
    jump bai_myconid

label bai_ch3_after:
    hide cg onlayer cgl
    $ bai.fit = "trapper"
    $ vn_enter(bg="bai_stream", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_voice_high")
    show screen bai_panel(3)
    "{color=#9fd8ff}The lure spikes. It won't go back down past a new floor, glowing on the panel like a thermometer stuck in summer. You're louder than you've ever been, on purpose, for good.{/color}"
    hide screen bai_panel
    bai_you "\"Testing. Testing, one—\""
    "{color=#9fd8ff}Your voice has moved. It comes out higher, sweeter, a voice you'd turn round for in a pub. Your waist has gone in. The dead trapper's leathers sit wrong on hips that weren't there last week.{/color}"
    vn_th "(Warg, slime, bloom. Toughness, give, control. And every single thing in these woods can smell you from a mile off.)"
    show screen bai_number(3)
    bai_you "\"I am going to survive the trip out with margin.\" It comes out high and ridiculous. \"And I am going to need a new coat. Definitely a new coat.\""
    hide screen bai_number
    call vn_night(8)
    jump bai_ch4

## ---- 4. Carried --------------------------------------------------------------------------------
label bai_ch4:
    $ bai.chapter = 4
    $ bai.fit = "trapper"
    $ vn_enter(bg="bai_ridge", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_ridge_climb")
    "The slope fights you all morning. Ground things are closing in behind you, you can smell them, and the panel floats ahead of you up the hill like a sarcastic flag: MARSH, THEODORE. CLASS: [[Bait]."
    vn_th "(Nothing on the ground is taking you anywhere. So: up.)"
    "Every bestiary you ever skimmed says the same thing about harpies. Built to carry. Built to use what they carry. One of those you can work with."
    "You've seen what the ground has in it now. The orc camp. The lamia's skin. The arachne's line. Every one of them stays where it is and wants you to stay too."
    vn_th "(Wings don't stay. Wings leave. You want the one thing in these woods that leaves.)"
    show cg bai_lure_max onlayer cgl
    "On the bare top of the ridge you plant your feet, and turn the dial all the way, and stand there broadcasting like a lighthouse, panting, the scent pouring off you into the wind."
    bai_you "\"Come on. Come on. Somebody with wings. I'm a {i}great{/i} opportunity.\""
    show cg bai_harpy_descend onlayer cgl
    "It comes down out of the sun: a harpy, feathered from the elbows, taloned at the shins, a woman's face and a woman's chest and a cock that's very much not a bird's, already standing up for you."
    bai_you "\"Alright. Fly me out or eat me. I am open to either at this point.\" It comes out high and too bright. \"I don't suppose you could help a, uh. Girl. With a ride?\""
    "You hear yourself say girl and decide not to examine it."
    jump bai_harpy

label bai_ch4_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_forest", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_harpy_branch")
    "She sets you down. Not on the ridge, and not over it. On a fat branch halfway up a tree, exactly as far from anywhere as you started, and she preens once and is gone."
    $ bai_body(4)
    $ bai.fit = "scraps"
    show cg bai_front_heavy onlayer cgl
    "{color=#9fd8ff}Hollow bones. Lighter, rebuilt to be carried. Your face is softer when you catch it in a puddle on the way down. And your chest, climbing for four days, is heavy enough now to fight the lightness: you're front-loaded, your balance is wrong, and there's nothing left to call it.{/color}"
    bai_you "\"Oh no. Oh no no no. I'm a {i}carry-on.{/i} I've been redesigned as {i}luggage{/i}.\""
    "You rip the old tee into a wrap. It holds. Mostly."
    bai_you "\"Okay. Okay, balance. Centre of gravity is just a… suggestion now. Walk like you're carrying shopping. In front. All the time.\""
    "You take three steps and nearly go face-first into a fern, and laugh, high and helpless, at the sky."
    show screen bai_panel(4)
    "ASPECTS: WARG. SLIME. BLOOM. HARPY."
    hide screen bai_panel
    bai_you "\"Oh, you {i}could{/i} have got me out. You carried me high enough to show me exactly how nowhere I still am.\""
    "You cup your chest, bounce it experimentally, and snort at the wobble."
    bai_you "\"Definitely a new coat.\""
    "That joke is going to live a long, long time."
    show cg bai_solo_night onlayer cgl
    "That night, under the coat, you get yourself off, quick and practical, the way you always have. It works. It's unremarkable. You don't think about it again."
    show screen bai_number(4)
    "The harpy could have carried you over the ridge and didn't. So the real problem is you're not strong enough to make anything take you anywhere."
    hide screen bai_number
    hide cg onlayer cgl
    call vn_night(8)
    jump bai_ch5

## ---- 5. Held Out -------------------------------------------------------------------------------
label bai_ch5:
    $ bai.chapter = 5
    $ vn_enter(bg="bai_cabin", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_dial_down")
    "New plan: discipline. Four days, dial fully down. You'll prove you're in control of this, and you'll let your body settle while you're at it."
    show cg bai_discipline onlayer cgl
    "Day one, you sit cross-legged on the cot and breathe. Day two, you set snares and check them and eat what's in them. Day three, the swelling stops. Day three, you're extremely pleased with yourself."
    bai_you "\"Day three. Swelling: stopped. Lure: zero. Discipline: unbelievable. Note to self: you are, in fact, the main character.\""
    "You scratch it into the hide with the burnt stick, and underline {i}main character{/i}, and you mean it."
    vn_th "(See? Zero is zero. It's a dial. You're the one holding it.)"
    "The fourth night is very still. You lie back on the cot with your hands folded on your chest like a man in a painting, and the forest goes quiet around the shack."
    "And then, first a giggle. Then another. Then, outside the door: {i}skitter skitter.{/i}"
    hide cg onlayer cgl
    jump bai_kobolds

label bai_ch5_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_cabin", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_panel_tally")
    show screen bai_panel(5)
    "You dare a glance at the panel. ASPECTS: no change. They were too weak to leave anything behind."
    "{color=#9fd8ff}And your chest climbed anyway. The passive floor is higher. Charged in full, paid nothing.{/color}"
    hide screen bai_panel
    "That's the first time the arithmetic frightens you."
    "You sit on the floor with the hide and the stick and do it properly, for the first time. Warg, slime, bloom, harpy, kobolds. Every column different. One column the same."
    vn_th "(It isn't the partners. It's the role. Every time, you're the one underneath. And the body's catching up to what it's used for.)"
    bai_you "\"Next time, maybe I'll just fuck myself unconscious and call it research.\""
    "If nothing else, celibacy in these woods is a group sport."
    show screen bai_number(5)
    "The woods will come whether you like it or not. So you'd better be strong enough for whatever shows up."
    hide screen bai_number
    call vn_night(8)
    jump bai_ch6

## ---- 6. Fed ------------------------------------------------------------------------------------
label bai_ch6:
    $ bai.fit = "scraps"   # dressed walking in (the 2026-11-13 art walk)
    $ bai.chapter = 6
    $ vn_enter(bg="bai_oldgrowth", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_dryad_track")
    "Deeper. The trees get older and wider until the trunks are walls and the light is green and thick enough to drink. You're following signs: bark worn smooth at waist height, moss growing in rings, a sweetness in the air."
    "Lore says dryads feed things. You're hungry. Snares only go so far, and the kobolds' enthusiasm has left you running on empty."
    "Your clothes are past arguing with. The coat won't close. The wrap is a rumour. Every step is a negotiation between your hips and your chest about which one gets to lead."
    vn_th "(Food, and maybe an aspect. Margin. Margin is the whole game now.)"
    "Deep in the old growth something is rooted: a dryad, bark-skinned and green-haired and enormous, half fused to a log draped in moss, her breasts heavy and her cock heavier, a bead of sap at its tip."
    "Your lure is already blazing. You don't bother with stealth. You walk straight into her clearing."
    jump bai_dryad

label bai_ch6_after:
    hide cg onlayer cgl
    $ vn_clock.day += 1
    $ bai_body(6)
    $ vn_enter(bg="bai_cabin", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_milk_wake")
    "{color=#9fd8ff}Two days later you wake sore and swollen and don't understand it until it happens. A slow warm trickle down your front, and then another. They work now.{/color}"
    "{color=#9fd8ff}It builds until it's relieved, and you can't relieve it alone, and your clothes are past saving.{/color}"
    show cg bai_milk_try onlayer cgl
    "You try anyway, bent over the basin, squeezing with both hands, and get a dribble and a gasp and no relief at all."
    bai_you "\"Come on. Come {i}on.{/i} I'm a reasonable person, I'm asking nicely— {i}hahh{/i}— why does it only want {i}somebody else{/i}—\""
    vn_th "(It wants a mouth. Of course it wants a mouth. Everything in this forest wants something done to you.)"
    show screen bai_number(6)
    "You can't travel like this. Obviously you'll have to wait."
    hide screen bai_number
    hide cg onlayer cgl
    call vn_night(8)
    jump bai_ch7

## ---- 7. Maren ----------------------------------------------------------------------------------
label bai_ch7:
    $ bai.chapter = 7
    $ bai.fit = "scraps"
    $ vn_enter(bg="bai_forest", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_led")
    "The forest is listening to you now. You can feel it: a pointed attentiveness, a nudge between the shoulder blades, the trees leaning just slightly one way."
    "You follow it, waddling, leaking, the coat hanging open over a wrap that has given up. It brings you somewhere quiet."
    $ vn_enter(bg="bai_clearing", pc="cheerful", pc_tag="bai_pc", cast=[("bai_maren", "calm")], cg="bai_maren_clearing")
    "Something in the forest tells you where she is, which means the forest has been talking about you. You expect a ruin, or a queen, or a warning. You find a clearing, a small hut, and a woman in her thirties living small, patching a tent."
    bai_you "\"Uh. Hi.\""
    bai_maren "\"Hello. Best spot for company's that log. Watch your tail on the knives.\""
    show cg bai_maren_log onlayer cgl
    "You sit. The log is warm from the sun. She keeps sewing."
    bai_maren "\"You're leaking. You'll get over trying to hide it. Or you won't, but it won't matter either way. The forest told me you'd come. You made quite the entrance. Everything's been talking about you. Even the birds.\""
    bai_maren "\"How long have you been in?\""
    bai_you "\"A week? Two? I lost count. It's hard to tell night from day in this place.\" You watch her pull the needle, a clean silver arc through pale canvas. \"You know what I am, right?\""
    bai_maren "\"Mm. The forest told me.\""
    "You flush, absurdly, at the idea of the birds passing it round: new bait, west of the stream, first come first served."
    "She has deer ears and a soft heavy chest under a plain dress. Your lure reaches her; you watch it reach her; and she does nothing about it. For the whole conversation. You've never seen anything so strange."
    menu:
        "What you ask Maren."
        "How do I stop?":
            $ bai.maren = "stop"
            bai_you "\"How do I stop?\""
        "How did you stop?":
            $ bai.maren = "how"
            bai_you "\"How did you stop? You did, didn't you?\""
    show cg bai_maren_talk onlayer cgl
    bai_maren "\"You want to know how to quit. You stop now. That's all. Live small. Keep away. Don't throw lure. Don't go asking for more.\""
    bai_maren "\"Stay in one place. Accept what you've got. Let the forest forget you.\" A small shrug. \"It works. For some.\""
    bai_you "\"That's it? There's not a trick? No panel option, or quest, or—?\""
    bai_maren "\"That's it. The forest isn't a jail. Just an appetite. I stopped here, ages ago. I quit early enough to still be overlooked. How far can you turn your lure down now?\""
    bai_maren "\"Let myself get overlooked. You get small enough, you fade out.\""
    bai_you "\"Shit.\""
    bai_maren "\"Yeah.\""
    "You tug the coat closed over the wreck of your shirt, wobbling as your chest presses up against your ribs."
    bai_you "\"Am I too late to do that?\""
    bai_you "\"Not much. There's a floor. It climbs on its own. Even at zero, things come.\""
    bai_maren "\"So, yes. You're well past safe. The only protection left is up, not down. Bigger shadows chase away smaller ones. The exit's behind you. Nobody hid it. You just asked late.\""
    "She draws a small circle in the air with the needle."
    bai_maren "\"The crown, eventually, if you want it. Or just stay quick and keep putting on mass.\""
    "You look at her chest, and feel a flicker of relief that you've got room left. You notice yourself feel it."
    bai_maren "\"I've been settled for years. You'll pass me before a year's out. Probably less. Most do.\""
    bai_maren "\"I quit soon as I worked out the maths.\""
    vn_th "(You worked out the maths on day two. You just did different maths.)"
    vn_th "(Most do. So there are others. Or there were.)"
    show cg bai_maren_name onlayer cgl
    bai_maren "\"What's your name?\""
    "Nothing has asked you for anything in weeks. Everything has just taken."
    bai_you "\"Theo.\""
    bai_you "\"Theo. Marsh.\""
    "It comes out thready. It's been so long since anything needed it."
    bai_maren "\"Well, Theo. None of this will finish you. Not like the stories say. It just gets stranger, and heavier. More of it, always. You don't shrink. The forest only goes forward.\""
    bai_maren "\"You'll know when it's time. Enjoy the quiet while you have it.\""
    bai_you "\"I should—\" You gesture at nothing. \"There's always something.\""
    "She waves the scissors at you, goodbye and suit-yourself at once."
    "You sit there a while longer. She hands you a strip of clean linen without comment, and you bind your chest with it, and it's the kindest thing anybody has done for you since you woke up in the dirt."
    show cg bai_maren_leave onlayer cgl
    "She doesn't stop you, or warn you, or wish you luck. You walk out having decided, and the number doesn't go up, because you've stopped keeping one."
    "For the first time in days you feel like someone, and not something somebody's waiting for."
    hide cg onlayer cgl
    hide bai_maren
    call vn_night(8)
    jump bai_ch8

## ---- 8. Asked For ------------------------------------------------------------------------------
label bai_ch8:
    $ bai.chapter = 8
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_forest", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_alone")
    "Alone, behind a boulder, nobody watching for once: no beast, no kobold, no birds. You're going to prove Maren wrong with the one bit of evidence you own."
    "It doesn't work. Not size: wiring. Slow, hard, every trick you've ever known. The feeling's there and it won't resolve, like pressing a key that isn't connected to anything."
    bai_you "\"Come on. Come {i}on.{/i} You've done this a thousand times—\""
    show cg bai_alone_slip onlayer cgl
    "Then you shift, frustrated, and your hand slides lower without a decision behind it, into heat that's been building there for days, and it works at once and enormously."
    bai_you "\"{i}Oh.{/i} Oh— {i}oh{/i}— {i}there{/i}— {i}AHH{/i}—!\"" with vnfx("flash")
    "You finish with two fingers somewhere you didn't have a week ago, legs shaking, your back against the stone."
    show cg bai_alone_after onlayer cgl
    "Afterwards the thought you can't put down isn't that it happened. It's that it was better."
    vn_th "(Plumbing question. Not a moral one. Maintenance data. A point in your favour, even.)"
    $ bai_body(8)
    "{color=#9fd8ff}Your cock is in visible decline: smaller, quieter, a thing you have rather than a thing you use. Everything else isn't.{/color}"
    "And the heat doesn't go. It drops back a notch and sits there, waiting, patient as weather."
    show cg bai_sable_scent onlayer cgl
    "Later there's a new scent on the wind: wolf, but not the warg. Cleaner. Deliberate. Somebody who knows exactly where they live."
    "You stand up, and follow it, and go looking, and when you find her you ask."
    jump bai_sable

label bai_ch8_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_forest", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_sable_rest")
    show screen bai_panel(8)
    "{color=#9fd8ff}The cycle isn't a calendar any more. It's weather. It arrives, it drives, it takes over. ASPECTS: WEREWOLF. CYCLE: CONTINUOUS.{/color}"
    hide screen bai_panel
    "You fall asleep curled against her side in the ferns, and she lets you, and in the morning she's gone and has left you a skin of clean water by your hand."
    vn_th "(She thanked you. Something thanked you. You keep turning it over like a coin you found in the dirt.)"
    call vn_night(8)
    jump bai_ch9

## ---- 9. Oni ------------------------------------------------------------------------------------
label bai_ch9:
    $ bai.chapter = 9
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_forest", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_bestiary")
    "The heat comes back on the third day and it doesn't knock. You sit in the ferns with your scrap-hide notes spread out round you, your own bestiary in your own scrawl, and you run the numbers."
    "ONI: twice the height of a man, at least. Avoid direct mating."
    if bai.free == "free":
        vn_th "(And there it is, under ELASTICITY: FREE. Underlined twice. Day two. The acquisition you called free.)"
    else:
        vn_th "(And there it is, under ELASTICITY: FREE (?). Day two. You'd even left yourself the question mark.)"
    "You can survive it. Because of the slime. You've done the maths. You're almost sure you've done the maths."
    show cg bai_oni_call onlayer cgl
    "The biggest thing you've ever deliberately called, days after Maren, with full information."
    if bai.panic == "slam":
        "The first time you slammed this dial you did it in a panic. This time you mean it."
    else:
        "The first time you inched this dial up in a panic. This time you take it all the way, on purpose, in one smooth turn."
    "You turn the dial all the way up. The forest goes silent."
    hide cg onlayer cgl
    jump bai_oni

label bai_ch9_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_forest", pc="cheerful", pc_tag="bai_pc", cast=[], cg="bai_waddle")
    "{color=#9fd8ff}You get up eventually. It takes a while. Your hips are so wide you can barely see past your own breasts to where your feet are, and the old coat is a joke you're never going to stop telling.{/color}"
    bai_you "\"Throne hips. She said throne hips. Rude.\""
    "You walk out of the clearing awestruck, reshaped, waddling wide, laughing at nothing."
    show screen bai_panel(9)
    "Afterwards you check the panel for the first time in three days. It still says [[Bait]."
    "You scratch a last line onto the oni entry in your bestiary, under {i}avoid direct mating{/i}: {i}disregard.{/i}"
    hide screen bai_panel
    vn_th "(Still. After all that. It doesn't care how big the thing was. It only cares who was underneath.)"
    call vn_night(8)
    jump bai_ch10

## ---- 10. [Throne] ------------------------------------------------------------------------------
label bai_ch10:
    $ bai.chapter = 10
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_den", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_throne_panel")
    "You wake in the den clearing with no memory of walking there, heavy and still soaked from the oni, with a deep pleasant ache between your thighs."
    "The ferns round the clearing are flattened in a ring, as though something large has been circling it all night, patiently, waiting for you to wake up."
    show screen bai_panel(10)
    bai_sys "CLASS: [[Throne]. Runs on being ridden. Drains when it isn't. Abdication: available. If you abdicate, you'll be the softest, most saturated, most wanted thing in a hundred miles, with nothing protecting it."
    hide screen bai_panel
    "The panel's been accurate for nine days. You believe it instantly."
    vn_th "(Bigger shadows chase away smaller ones. She told you. You just didn't know you'd be the shadow.)"
    hide cg onlayer cgl
    jump bai_court

label bai_ch10_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bai_den", pc="regal", pc_tag="bai_pc", cast=[], cg="bai_court_end")
    "And an encounter ends, and nothing about you has changed. You check. The panel's counter is gone. The climb is over. You're finished."
    "The process that remade you is done with you, and it's a strange, quiet grief, and then it's just the evening."
    vn_th "(A temporary arrangement. Until you're strong enough to leave.)"
    "There's no number attached to it. You don't notice that either."
    call vn_night(8)
    jump bai_ch11

## ---- 11. Upkeep --------------------------------------------------------------------------------
label bai_ch11:
    $ bai.chapter = 11
    $ bai.fit = "mantle"
    $ vn_enter(bg="bai_den", pc="regal", pc_tag="bai_pc", cast=[], cg="bai_audience")
    "The clearing. No chair, no dais, no stone seat. The throne is her, and audience is conducted accordingly."
    "Somebody has made her a mantle of furs and a crown of woven branches. She wears both and nothing else, and the court sits in a ring round the moss, waiting."
    "She doesn't remember who. Someone in the court, overnight, while she slept on the furs. She woke wearing it. It fits perfectly."
    "Petitions are made during. Rank is measured in access: how often, how long, who's next."
    jump bai_petitions
