## THE SOURCE: celestia's passages, rewritten for the VN (2026-11-11; PLAN.md). One label a passage of the
## original (main.twee, rungs.twee, ending.twee, cast.twee), as beats; the director scenes are in scenes.rpy.
## Six days: the first shine; the food court; the club; the night bus; the warehouse; the park.

## ---- day 1: the first shine (Celestia Opening, First Shine, First Blast, First Change, First Night) ---------

label ce_opening:
    $ ce_init()
    $ ce.fit = "vest"
    $ vn_enter(bg="ce_flat", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_luna_blurays")
    "A full shift of HDMI cables and the ElectroMart pop loop. All you want is ramen and the sticky controller. You shoulder your door open."
    vn_sfx "CRASH."
    show cg ce_luna_blurays onlayer cgl
    "A figure sails past your ear, ShellyAstra, detachable lance and all, and bounces off the wall."
    "Your shelf is half down. Your chair is upside down. And sitting cross-legged on your stack of sealed Blu-rays, with the head of your best figure in her lap, is a catgirl."
    "Jet black from her ears to the tip of her tail. A crescent mark over one eye. A blue ribbon collar with a bell on it, and a black sweater miles too big for her."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Oh, good. You're late.\""
    "Deadpan."
    ce_you "\"What the {i}fuck.{/i}\""
    hide cg onlayer cgl
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Strong opener.\""
    "She holds up the head."
    ce_luna "\"Your Luminous Witch insulted me. I'm Luna. You're [ce_pc_name] Carter, too much sodium, too much isekai, and as of tonight, this town's magical girl.\""
    ce_you "\"I'm a {i}guy.{/i}\""
    ce_luna "\"Magical law is gender-agnostic. We fix that in post.\""
    "Her tail flicks. She hops down off the Blu-rays."
    vn_sfx "Tink."
    ce_luna "\"Short version. There's a sorcerer making this town want things. Badly. In public. The only thing that pushes back is a magical girl, the last one retired, and the Prism picked you. I've looked all week for a reason it's wrong.\""
    show ce_luna smug at vn_cast_slot
    "She sniffs."
    ce_luna "\"There isn't one. It's annoying.\""
    ce_you "\"Shouldn't you find, like. An actual girl?\""
    ce_luna "\"Do I look like a recruiter with options?\""
    "Luna points at the middle of your carpet."
    ce_luna "\"Stand there. Say it. {color=#ff8fc8}Celestial Prism, Make Me Shine.{/color} Out loud, if you please.\""
    ce_you "\"No.\""
    ce_luna "\"Out loud.\""
    "She sits on your desk, on your controller, on purpose."
    ce_luna "\"Or the next time I step in your laundry, I eat your soul.\"\n{size=-5}{color=#ff8fa3}▸ Say it. Out loud.{/color}{/size}"
    hide ce_luna
    jump ce_first_shine

label ce_first_shine:
    $ ce.sortie_day = vn_clock.day
    show ce_pc shocked at vn_pc_slot
    ce_you "\"{color=#ff8fc8}CELESTIAL PRISM, MAKE ME SHINE!{/color}\""
    $ ce_morph(1)
    show cg ce_shine_1 onlayer cgl
    vn_sfx "FWOOOOM." with vnfx("flash")
    "Light. Everywhere. A noise like somebody clubbing your eardrums with a transformation theme."
    "{color=#ff5fb8}It starts in your chest. Heat, fizzing, like a shot of pure sunlight. Your clothes go to ribbons. Your pecs swell. Round out. Get {i}heavy.{/i}{/color}"
    ce_you "\"Wh— {i}ahh{/i}— my {i}chest{/i}— what's happening to my—!\""
    "{color=#ff5fb8}They don't stop. Breasts. Huge ones, bouncing, the nipples stiff and buzzing like they're wired to the mains. Your hips crack out wide. Your ass balloons. Your waist pulls in.{/color}"
    show cg ce_shine_1_tails onlayer cgl
    "{color=#ff5fb8}Hair bursts out of your scalp and whips into crescent tails, long and glossy and black-blue, full of tiny moving stars.{/color}"
    "{color=#ff5fb8}White gloves slide up your arms. White boots up your thighs. A gold choker clicks shut round your throat. Then the leotard, white and gold, cut high on the hip and barely holding the chest in.{/color}"
    "{color=#ff5fb8}Between your legs, your cock's still there. Smaller. Rock hard. Mashed flat under the leotard and twitching.{/color}"
    show cg ce_shine_1_land onlayer cgl
    "The rush peaks, and it's like coming with your whole body. You cry out, high and sharp, and land on the futon with your legs everywhere." with vnfx("shake")
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Congratulations. You're the least subtle magical girl I've ever seen, and I once trained a pancake mascot.\""
    "You grab your chest. You can't not. Heavy. Soft. Hot. Your nipple drags across your gloved palm and your hips jerk off the mattress."
    ce_you "\"Nnh— what did you {i}do{/i} to me—\""
    ce_luna "\"Get up. Point at something. Blast it. You'll feel it.\""
    "She waves a hand. You feel it. A pressure behind your breastbone, packed tight and hot, pushing out into your nipples. Aching to go off."
    hide ce_luna
    menu:
        "Aching to go off."
        "Hand on your hip. Point.":
            $ ce.pose = "point"
        "Squeeze them together":
            $ ce.pose = "squeeze"
    jump ce_first_blast

label ce_first_blast:
    $ vn_enter(bg="ce_flat", pc="shining", pc_tag="ce_pc", cast=[], cg="ce_blast_1")
    if ce.pose == "squeeze":
        "You cup your new tits and push them together, and the pressure shoots straight to the tips."
    else:
        "One hand on your hip. The tails swing and nearly tip you over. You point at the stack of empty ramen cups on your desk."
    ce_you "\"{color=#ff8fc8}Ch-Charm Blast!{/color}\""
    show cg ce_blast_1 onlayer cgl
    vn_sfx "BZZZAAAAT—" with vnfx("flash")
    "It comes out of your chest as light, and it's an {i}orgasm.{/i}"
    ce_you "\"Ahh— {i}AHHH{/i}— oh fuck, oh {i}fuck{/i}—!\""
    vn_sfx "Pff, pff, pff."
    "A beam of starlight blasts out of your tits. Ramen cups everywhere. Every pulse of it is a contraction. Your nipples spasm. Your little cock jerks in the leotard, wet, again, again, again."
    ce_you "\"It won't— {i}stop{/i}— oh god it won't stop coming out—\"" with vnfx("shake")
    "It doesn't. You grab your tits to make it stop and that makes it worse, so much worse, your own gloved fingers squeezing out another pulse of light and another clench down below. Your knees give. You ride it out with your mouth open and your tails everywhere."
    show cg ce_blast_1_after onlayer cgl
    "You end up on your knees, shaking, the front of the leotard soaked through."
    show ce_luna smug at vn_cast_slot
    ce_luna "\"That was better than most of your browser history.\""
    ce_you "\"Change me back. Change me {i}back{/i}—\""
    ce_luna "\"As you wish, Sparkle Lord.\"\n{size=-5}{color=#ff8fa3}▸ Change me back!{/color}{/size}"
    hide ce_luna
    jump ce_first_change

label ce_first_change:
    $ ce_rung(1)
    $ ce.fit = "tee"
    $ ce_demorph(1)
    $ vn_enter(bg="ce_flat", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_demorph_1")
    show cg ce_demorph_1 onlayer cgl
    "Luna flicks her fingers. A ripple of light runs down your spine. The chest sucks back in. The tails pull back into your scalp. The leotard peels off into your own boxers and a stretched tee."
    "You're you. It's over. You survived. Then you look at your hands."
    show cg ce_hands onlayer cgl
    "{color=#ff5fb8}Slim. Long-fingered. Smooth knuckles. Nails buffed to a glossy shine you've never done in your life.{/color}"
    $ _ce_feel = CE_FEEL[1]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    ce_you "\"My {i}hands!{/i} Change them back!\""
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Oh. Did I not mention? Magic leaves marks. Every time.\""
    "From the windowsill. She curls up."
    ce_luna "\"Sucks to be you.\""
    ce_you "\"I have {i}work{/i} tomorrow!\""
    ce_luna "\"Then wear gloves. You've got some now.\"\n{size=-5}{color=#ff8fa3}▸ Shower{/color}{/size}"
    hide ce_luna
    jump ce_first_night

label ce_first_night:
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_flat_shower", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_shower")
    show cg ce_shower onlayer cgl
    "Hot water, late. You lean on the tiles and look down."
    "{color=#ff5fb8}Smooth.{/color}"
    "{color=#ff5fb8}Shins. Thighs. Arms. Chest. Armpits. Not shaved: like hair never happened. You look down past your stomach. Your cock and balls hang there bare as a peach.{/color}"
    "You run a palm up your thigh. Silk. You do it again, slower, and a shiver goes all the way up into your balls."
    ce_you "\"Oh— {i}oh{/i}— that's— {i}hhn{/i}—\""
    show cg ce_shower_touch onlayer cgl
    "Both hands now. Up your thighs. Over your hips. Across your bare chest, and your thumb finds your nipple and circles it, slow, perfect, like it's done it a hundred times."
    ce_you "\"{i}Ahh{/i}—!\""
    "Your cock jumps."
    ce_you "\"...Huh.\""
    "Breathless. It isn't a bad feeling. That's the bad part."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Bed. Big day tomorrow. Probably.\""
    "Through the door.\n{size=-5}{color=#ff8fa3}▸ Bed{/color}{/size}"
    call vn_night(8)
    jump ce_first_morning

## ---- day 2: the food court, then Pippa (First Morning, Stall, Court, Court Sex|Shine, Court Done, Show Me) ------

label ce_first_morning:
    $ ce.loft = max(ce.loft or 0, 1)
    $ ce.fit = "vest"
    $ vn_enter(bg="ce_shop", pc="snark", pc_tag="ce_pc", cast=[], cg=None)
    show bg ce_shop onlayer bgl
    $ _ce_v = ce_vest()
    "ElectroMart, first thing. [_ce_v]"
    show cg ce_blister onlayer cgl
    "You fight a Bluetooth speaker out of its blister pack with your new hands. They're so slim the plastic keeps winning."
    hide cg onlayer cgl
    show ce_dougie grin at vn_cast_slot
    "Dougie leans over the returns counter with a jiggling bag of gummy worms. He clocks your hands immediately."
    ce_dougie "\"Whoa, Carter. New product in the demo section? Hand spa? The Manicure Pro?\""
    ce_you "\"My hands have always looked like this.\""
    ce_dougie "\"Nah, dude. You got anime protagonist hands. All you need is little sparkles every time you point at stuff.\""
    "He waggles his stubby fingers. You throw a barcode scanner at his thigh."
    vn_sfx "Thunk."
    hide ce_dougie
    show ce_pruitt verdict at vn_cast_slot
    ce_pruitt "\"Are you using hand lotion now? Hands clean. Not sparkling. This isn't a spa.\""
    "Navy pantsuit, eyebrows already writing your review."
    hide ce_pruitt
    "Your phone buzzes. Pippa."
    "{color=#ff8fc8}PIPPA: omw w coffee{/color}"
    "{color=#ff8fc8}YOU: at work. hands are weird. don't ask{/color}"
    "{color=#ff8fc8}PIPPA: ??????{/color}"
    "{color=#ff8fc8}PIPPA: ok now im asking{/color}"
    "Then it buzzes again, and it isn't Pippa."
    $ _ce_t = CE_TEXTS[2]
    "{color=#ff8fc8}LUNA: [_ce_t]{/color}"
    "ElectroMart is in the Shopping Centre. The food court is just round the corner, and your break's coming up.\n{size=-5}{color=#ff8fa3}▸ Sign out for your break{/color}{/size}"
    $ vn_until(11)
    jump ce_stall

label ce_stall:
    $ ce.sortie_day = vn_clock.day
    $ ce.fit = "casual"
    $ vn_enter(bg="ce_toilets", pc="snark", pc_tag="ce_pc", cast=[], cg=None)
    show bg ce_toilets onlayer bgl
    "The Shopping Centre toilets, OUT OF ORDER taped on the door. Cracked tiles, orange cleaner, and something sweeter underneath, like perfume spilled on purpose."
    "Luna's in your bag. You lock yourself in the end stall."
    ce_you "\"Why the {i}mall?{/i} It's not even payday.\""
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"He feeds on wanting things in public. Phrase. Now. Unless you want the lingerie sale to end on the news.\""
    ce_you "\"Do I have to say the whole—\""
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Mutter it. It'll hear you.\""
    "You mutter it, into your collar."
    ce_you "\"Celestial prism, make me shine.\""
    $ ce_morph(2)
    show cg ce_shine_2 onlayer cgl
    vn_sfx "WHUMP." with vnfx("flash")
    "{color=#ff5fb8}It hits like a sledgehammer made of glitter. Your hips grind against the grab rail. Your nipples go so hard you gasp. Your chest surges out and shoves your jacket open, and the tails spill down to the floor.{/color}"
    "{color=#ff5fb8}Leotard. Boots. Choker. Your cock, small and hard, every humiliating contour showing through the white.{/color}"
    "Somebody rattles the stall door."
    ce_you "\"Occupied!\""
    "You squeak it. It comes out in a voice like a pop idol's. You clap a hand over your mouth and spend a long, shaking moment fighting the urge to jerk off right there."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Done? Good. Food court. Go.\""
    "Perched on the flush.\n{size=-5}{color=#ff8fa3}▸ Out into the food court{/color}{/size}"
    jump ce_court

label ce_court:
    $ vn_enter(bg="ce_food_court", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_court_fog")
    show cg ce_court_fog onlayer cgl
    "The food court's gone purple. Fog rolls out of the vents, low and sweet. Shoppers standing stock-still between the tables with glassy eyes. Staff leaning over their counters, breathing slow, all of them in time. A couple by the pretzel stand, faces blank, moving like somebody else is working their arms."
    "Then every head turns. At once. To you."
    ce_fog "\"It's her. Look at her.\""
    "A woman in frosted pink lipstick. Flat. Not her voice. Somebody else's words in her mouth."
    show cg ce_court_grab onlayer cgl
    "They come at you. All of them, grown adults on strings, and none of them blinking. A guy in a band tee grabs your left tail and {i}yanks{/i}, and the heat goes straight through your chest."
    ce_you "\"Hey! Those are my actual— {i}ahh{/i}— let GO—!\""
    "Two guys wind your right tail round their fists and haul you back. Hands on your hips. Hands on your ass. Hands on your {i}tits{/i}, squeezing through the leotard."
    ce_you "\"Get— OFF— I'm the magical girl, YOU'RE supposed to be the one getting blasted—!\""
    "You slap your palms over your chest. The pressure's right there."
    ce_you "\"{color=#ff8fc8}Charm Blast!{/color}\""
    show cg ce_court_blast onlayer cgl
    vn_sfx "BZZAAT." with vnfx("flash")
    "Light out of your chest, into a guy in dad sandals, and it's coming, it's {i}coming{/i}, your whole chest going off like a cock."
    ce_you "\"Hnnh— no— not {i}now{/i}— {i}ahhhh{/i}—!\""
    "He drops on a bench, strings cut, blinking at nothing. Your knees nearly go with him."
    "They keep coming. Every blast knocks one down and every one you knock down spikes it higher. A woman wrenches your tail and your head whips back. You fire again. Come again. Louder. You didn't want either."
    show cg ce_court_fleece onlayer cgl
    "A guy in a fleece drops to his knees in front of you, grabs your hips, and presses his face to the front of your leotard, right over your little cock, and breathes on it. Hot. Through the white."
    ce_you "\"Don't— don't {i}do{/i} that— get your face OFF my— {i}ahh{/i}—\""
    "He does it again. His eyes are empty. Your hips push into his face all on their own."
    ce_you "\"No— no, that wasn't me— {i}hips{/i}, stop it—!\""
    "Somebody behind you is kneading your ass with both hands like dough, spreading you, squeezing. The woman with the pink lipstick has your nipple between her finger and thumb through the leotard, rolling it, staring through your face."
    ce_fog "\"She's so loud. He likes loud.\""
    ce_you "\"Ahh— {i}ahh{/i}— stop {i}touching{/i} them— I said STOP— {i}nnnh{/i}—!\""
    show cg ce_court_bench onlayer cgl
    "By the last wave they've got you bent over a bench. A girl's got your tails in both fists like reins, pinning your face to the tabletop. A big guy's behind you, grinding his hard-on into your leotard, trying to dry-hump the transformation out of you."
    vn_sfx "Rub, rub, rub."
    ce_you "\"Nnh— not— not {i}there{/i}— get off— get {i}off{/i}— {i}ahh{/i}, that's— {i}that's{/i}—\""
    "His hands slide round. Squeeze your tits together. The pressure in your chest climbs and climbs. The big one. Right at the edge, and you can't stop it."
    "Somewhere in the fog, a voice you've never heard. Velvet. Bored. Delighted."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "{color=#c79bff}{i}\"Let it go, little star. Let it come to me.\"{/i}{/color}"
    menu:
        "The big one, right at the edge."
        "Let it go to him" (ending="counts"):
            $ ce_let_go(2)
            jump ce_court_sex
        "Make it shine" (ending="counts"):
            $ ce_shine(2)
            jump ce_court_shine

label ce_court_after:
    $ vn_enter(bg="ce_food_court", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_court_after")
    show cg ce_court_after onlayer cgl
    if ce_enc.partner_came:
        "The big guy goes first, groaning into your tails with that blank face, and hot spurts land across your leotard, your thighs, the underside of your tits. Then the others. You're dripping, and you're still yelling at them to stop."
    else:
        "The hands don't stop until the fog does."
    "It plays back in flashes. Fists in your tails, holding you down on the bench. A hand round your little cock through the leotard, jerking it, while another man pumped his own cock against your hip. Somebody's fingers shoved in your mouth, and you moaning round them, loud, because your stupid magic body thought that was {i}great.{/i}"
    ce_you "\"Mmf— get them— {i}out{/i}— {i}mmnh{/i}—\""
    ce_you "\"No— no— {i}don't{/i}— don't stop touching me— {i}why did I say that{/i}—\""
    "That was you. Out loud. In the food court. Both of those were you."
    show cg ce_court_letgo onlayer cgl
    "And you let go. All of it. It goes out of your chest in a long shuddering wave, and you scream it at the food court ceiling, and it doesn't land anywhere near you." with vnfx("flash")
    "It goes {i}somewhere.{/i} Across town, something is pleased.\n{size=-5}{color=#ff8fa3}▸ Slide off the bench{/color}{/size}"
    jump ce_court_done

label ce_court_shine:
    $ vn_enter(bg="ce_food_court", pc="shining", pc_tag="ce_pc", cast=[], cg="ce_court_bench")
    show cg ce_court_bench onlayer cgl
    ce_you "\"No. Not yours. {i}Mine.{/i}\""
    "You gasp it. The big guy's still grinding on you, blank-faced, holding you down. The girl hauls on your tails like reins and your back arches and your tits swing under you, heavy, throbbing, so full of light you can see it glowing through the leotard."
    ce_you "\"Ahh— {i}ahh{/i}— you want it? You want it? {i}Fine{/i}—\""
    "You twist an arm free, grab your own tits, shove them together, and fire it yourself."
    ce_you "\"{color=#ff8fc8}Triple— Charm— {i}COMBO!{/i}{/color}\""
    show cg ce_court_combo onlayer cgl
    vn_sfx "FWOOOOOM." with vnfx("flash")
    "Light detonates through the food court. It hits every string at once. Everyone in it comes, you loudest, a tidal wave of shudders rolling out over the tables, and then they all drop like somebody let go of them."
    ce_you "\"Ahhh— {i}AHHHH{/i}—!\"" with vnfx("shake")
    "The fog rips apart like wet paper.\n{size=-5}{color=#ff8fa3}▸ Slide off the bench{/color}{/size}"
    jump ce_court_done

label ce_court_done:
    $ ce_rung(2)
    $ ce.fit = "casual"
    $ ce_demorph(2)
    $ vn_enter(bg="ce_food_court", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_court_wake")
    show cg ce_court_wake onlayer cgl
    "You come to face-down on a sticky table. The fog's gone. Shoppers slumped everywhere, blinking, staring at their own hands, with no idea what those hands just did. Half a cinnamon bun stuck to your heel. Jacket, jeans: you're you again."
    hide cg onlayer cgl
    "{color=#ff5fb8}You touch your throat. Something's missing. The Adam's apple. Just smooth skin.{/color}"
    ce_you "\"Luna. My {i}neck.{/i}\""
    show ce_luna smug at vn_cast_slot
    ce_luna "\"Progress.\""
    "Licking her thumb."
    ce_you "\"My voice, why is it—\""
    "{color=#ff5fb8}It comes out higher. Lighter. A little husky. Your jeans sit wrong, too: your waist's gone in, like somebody pinched it.{/color}"
    show cg ce_hips_2 onlayer cgl
    "{color=#ff5fb8}You grab your waist. Your hands slide down onto hips that flare where they never did, and round the back, onto a butt that's suddenly {i}there{/i}, round and soft and filling out your jeans.{/color}"
    ce_you "\"Oh— {i}oh{/i}— what—\""
    "You squeeze. It squishes. A whimper comes out in the new voice."
    ce_you "\"{i}Nnh{/i}— that's so {i}soft{/i}—\""
    $ _ce_feel = CE_FEEL[2]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    ce_luna "\"Adorable. You sound like you're about to sell protein shakes online.\""
    if ce.forks.get(2) == "go":
        show ce_luna flat at vn_cast_slot
        "Then she looks at you properly, and the joke goes out of her face."
        ce_luna "\"One rule. I'll say it once. Every time you let it take you, he gets stronger. Every time.\""
    else:
        ce_luna "\"Clean. He went home with nothing.\""
        "Almost approving."
    ce_luna "\"I'm at the bandstand in the park, when you want me. When {i}I{/i} want you, you'll know.\""
    hide ce_luna
    $ _ce_p = ce_power_line()
    "[_ce_p]"
    "You can't go back to work sounding like this. There's only one person you can call about high-pitched magical voice syndrome.\n{size=-5}{color=#ff8fa3}▸ Go to Pippa's tonight{/color}{/size}"
    $ vn_until(19)
    $ ce_next_loft = "ce_show_me"
    jump ce_loft_door

## Mer Street, the old warehouse with the pink door: the night at Pippa's that a sortie owes.
label ce_loft_door:
    $ vn_enter(bg="ce_loft_stairs", pc="flushed", pc_tag="ce_pc", cast=[("ce_pippa", "soft")], cg=None)
    show bg ce_loft_stairs onlayer bgl
    "Mer Street, the old warehouse with the pink door. Up the spray-painted stairs."
    "Pippa opens it before you knock. Glasses, big sweater, black hair dyed pink at the tips, a paint smear on her cheek. She looks at your face."
    ce_pippa "\"Oh. Something happened. Get in here.\"\n{size=-5}{color=#ff8fa3}▸ Go in{/color}{/size}"
    $ renpy.jump(ce_next_loft)

label ce_show_me:
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[("ce_pippa", "grin")], cg=None)
    show bg ce_loft onlayer bgl
    "You've been best friends since a summer you both worked the shop floor at nineteen. She's seen you lose it at a cartoon finale. She's never seen you like this."
    "Big yellow sweater, paint on her leggings, glasses slipping. She drags you to the beanbag by your slim hand and doesn't let go."
    ce_you "\"So a talking catgirl broke into my flat and told me I have to save the town with my tits.\""
    "In your new voice. She doesn't laugh. She listens to all of it: the mall, the hands, the leotard, the blast. The coming."
    ce_pippa "\"Show me.\""
    ce_you "\"What?\""
    ce_pippa "\"You don't expect me to take catgirl sorcery on faith. Peer review, babe. Transform. Are you actually going to say no?\""
    "Her grin is pure goblin.\n{size=-5}{color=#ff8fa3}▸ Mutter it{/color}{/size}"
    jump ce_show_me_shine

label ce_show_me_shine:
    ce_you "\"Celestial prism, make me shine.\""
    $ ce_morph(2)
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_show_shine")
    show cg ce_show_shine onlayer cgl
    "You mutter it, and it listens. Light. Heat. Chest, hips, tails, leotard, and you hear yourself go \"{i}Aaahn—!{/i}\" in front of your best friend." with vnfx("flash")
    "Pippa's eyebrows go up into her hair. She circles you with her hands hovering, like the tits might go off."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh my god. Can I... touch them?\""
    ce_you "\"Be gentle. They're... booby traps. Scientifically.\""
    show cg ce_show_touch onlayer cgl
    "Her palms land on your breasts."
    ce_you "\"Ahh— {i}Pippa{/i}—!\""
    "Her thumbs circle your nipples through the leotard. It's like tiny orgasms waking up in each one. Then she buries her face between them, giggling, and kisses your left nipple through the fabric."
    ce_you "\"Pippaaa— {i}nnh{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"They're real. And they move. Look how they move!\""
    "A whisper. She jiggles them with both hands. Your cock goes half-hard under the leotard, small and obvious. She notices. Of course she does."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"We really need to talk about magical dicks at some point.\""
    "Her palm slides down over the front of the leotard and cups it, just for a second, just to feel it twitch."
    ce_you "\"Nnh— {i}Pippa{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Science.\""
    show cg ce_show_almost onlayer cgl
    "She doesn't let go. She leans in. Your faces close. Her tongue wets her lips. Your noses almost touch, and the light in your chest flutters—"
    vn_sfx "POP."
    $ ce_demorph(2)
    $ ce.fit = "casual"
    show ce_pc shocked at vn_pc_slot
    hide cg onlayer cgl
    ce_you "\"Sorry! Oh god, Pippa—\""
    "You're back. Sweater, jeans, and a voice that squeaks it in a register you'll never pass off as a cold again."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh my god, babe, your {i}voice!{/i} That's so cute!\""
    show cg ce_beanbag onlayer cgl
    "She pulls you down onto the beanbag and curls into your side."
    ce_pippa "\"It's okay. All of this. Talk, experiment, freak out. Whatever level you're at, I'm here.\"\n{size=-5}{color=#ff8fa3}▸ Stay the night on the beanbag{/color}{/size}"
    $ ce.loft = max(ce.loft or 0, 2)
    call vn_night(8)
    jump ce_training

## ---- day 3: training, then Club Orbit (Training, the day's beats, Orbit, Orbit Sex|Shine, Orbit Done, Lab) ---------

label ce_training:
    $ ce.fit = "sweater"
    $ vn_enter(bg="ce_loft", pc="snark", pc_tag="ce_pc", cast=[("ce_pippa", "grin")], cg=None)
    show bg ce_loft onlayer bgl
    "Pippa bursts in from the kitchen with iced coffees and markers in every pocket."
    ce_pippa "\"Training session!\""
    ce_you "\"What do you mean {i}training?{/i}\""
    ce_pippa "\"You need to master those powers. And your new, uh, assets. Mutter it, starlight.\""
    "She flops on the beanbag with her sketchbook. You mutter it. It goes off faster this time, like it was waiting."
    $ ce_morph(2)
    show ce_pc flushed at vn_pc_slot
    ce_pippa "\"Fuck. You're a {i}goddess.{/i}\""
    "Pippa's pencil hits the floor. She crawls over."
    ce_pippa "\"Can I?\""
    ce_you "\"Just— {i}gently{/i}—\""
    hide ce_pippa
    show cg ce_train_knead onlayer cgl
    "She isn't gentle for long. Both palms, kneading. Thumbs flicking your nipples till you squeal. Your cock tents the front of the leotard."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Your nipples are wired straight to your dick. Is that normal?\""
    ce_you "\"Ah— fuck, Pippa, do you {i}mind{/i}—\""
    "She pinches both at once, just to see. Your hips buck off the floor and a little spark of light pops off your chest, like a struck match."
    vn_sfx "Tsing."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh my god, it {i}sparks.{/i}\""
    "She does it again."
    vn_sfx "Tsing."
    ce_you "\"Ahh— Pippa— stop— don't stop—\""
    vn_sfx "Tsing."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I'm going to need so many sketches. Nope.\""
    show cg ce_train_titjob onlayer cgl
    "She pushes you onto your back and straddles your thighs."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Ever had a titjob?\""
    ce_you "\"We are {i}not{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"We are.\""
    "She tugs the leotard down. Your tits spill out, heavy, pink-tipped. Your little cock springs up after them."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Gonna need both hands for these.\""
    "She squeezes your own breasts together round your cock."
    ce_you "\"Ohh— {i}oh{/i}—!\""
    vn_sfx "Shlk."
    "Soft. Hot. Smothering. She spits between them and starts to pump. Up. Down. Your own tits fucking your own cock while she grins down at you."
    "Your hands go over hers and squeeze tighter, exactly right. Nobody taught you that."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Your tits are incredible. Or should I say Celestia's?\""
    "She dips her head and flicks her tongue across the tip every time it pops out of your cleavage."
    vn_sfx "Shlk. Lick. Shlk. Lick."
    ce_you "\"Pippa— I'm— {i}I'm{/i}—!\""
    show cg ce_train_cum onlayer cgl
    "You come all over your own chest. Ropes of it, up your cleavage, a spatter on your chin, and light bursting off you in little starry flares." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You're a work of art. We should sell prints.\""
    "She milks the last of it with a long slow squeeze, drags her fingers through the mess, and brings them up to your lips."
    ce_you "\"You're a {i}menace.{/i}\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Through every cup size.\""
    "She kisses your cheek. Then she licks her fingers, slowly, looking right at you."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Round two later? I want to see what happens when you come {i}and{/i} fire a Charm Blast.\""
    "Your cock twitches against your stomach. She sees. She grins."
    $ ce_demorph(2)
    hide cg onlayer cgl
    show ce_luna deadpan at vn_cast_slot
    "The window's open. Luna's on the sill, where she wasn't a minute ago."
    ce_luna "\"If you two stain the ceiling, I'm not cleaning it.\""
    "Your phone buzzes."
    $ _ce_t = CE_TEXTS[3]
    "{color=#ff8fc8}LUNA: [_ce_t]{/color}"
    ce_you "\"I'm right here. You could just say it.\""
    ce_luna "\"I could.\""
    "And doesn't."
    hide ce_luna
    jump ce_day

## ---- the day between sorties (Celestia Hub, as beats): the shift and the vest, the dark window, Luna at the
## bandstand and her answer, an optional visit to the loft, then the night's sortie when its window opens ------

label ce_day:
    $ _ce_n = min(6, (ce.tier or 0) + 1)
    $ vn_until(9) if vn_clock.hour < 9 else None
    call ce_shift
    call ce_mirror
    call ce_bandstand
    if _ce_n == 3:
        menu:
            "{color=#b7b7b7}The rest of the day.{/color}"
            "Pippa's loft, on Mer Street":
                call ce_loft_visit
            "Breathe it":
                pass
    elif _ce_n == 4:
        menu:
            "{color=#b7b7b7}The rest of the day.{/color}"
            "Pippa's loft, on Mer Street":
                call ce_loft_visit
            "Catch the night bus":
                pass
    elif _ce_n == 5:
        menu:
            "{color=#b7b7b7}The rest of the day.{/color}"
            "Pippa's loft, on Mer Street":
                call ce_loft_visit
            "Go to the Elk Street warehouse":
                pass
    elif ce_dark():
        menu:
            "{color=#b7b7b7}The rest of the day.{/color}"
            "Pippa's loft, on Mer Street":
                call ce_loft_visit
            "Go anyway":
                pass
    else:
        menu:
            "{color=#b7b7b7}The rest of the day.{/color}"
            "Pippa's loft, on Mer Street":
                call ce_loft_visit
            "Walk out onto the lawn":
                pass
    $ vn_until({3: 21, 4: 22, 5: 21, 6: 13}[_ce_n]) if vn_clock.hour < {3: 21, 4: 22, 5: 21, 6: 13}[_ce_n] else None
    if _ce_n == 3:
        jump ce_orbit
    elif _ce_n == 4:
        jump ce_bus
    elif _ce_n == 5:
        jump ce_warehouse
    elif ce_dark():
        jump ce_bandstand_dark
    else:
        jump ce_arena

## A shift at ElectroMart (Celestia Shift): the vest, the metronome.
label ce_shift:
    $ _ce_t = ce_vest_n()
    # stage 5 wears the vest open; stage 6 leaves it on the break-room hook (CE_VEST), so: your own clothes
    $ ce.fit = "casual" if _ce_t >= 6 else ("vest_open" if _ce_t == 5 else "vest")
    $ vn_enter(bg="ce_shop", pc="snark", pc_tag="ce_pc", cast=[], cg=None)
    show bg ce_shop onlayer bgl
    $ _ce_v = ce_vest()
    "ElectroMart. Strip lights, the pop loop, a wall of TVs all playing the same ad for the same TV."
    "[_ce_v]"
    if _ce_t == 2:
        show ce_pruitt verdict at vn_cast_slot
        ce_pruitt "\"You sick? Your voice is funny.\""
        "Squinting at you over her mug."
        ce_you "\"Allergies.\""
        "It comes out a step higher than you sent it."
        hide ce_pruitt
        show ce_dougie grin at vn_cast_slot
        ce_dougie "\"You sound like you're about to drop a dance single. Say {i}welcome to ElectroMart.{/i} Say it sexy.\""
        "Delighted."
        hide ce_dougie
    elif _ce_t == 3:
        show cg ce_vest_seam onlayer cgl
        "You bend for a box of surge protectors and the side seam goes, hip to armpit."
        vn_sfx "Rrrrip."
        show ce_pruitt verdict at vn_cast_slot
        "Ms. Pruitt doesn't say a word. She goes into the stockroom, comes back with the only spare, and hands it to you folded. It's a women's cut. It fits you better than the old one ever did."
        ce_pruitt "\"Inventory.\""
        "And walks off."
        hide ce_pruitt
        hide cg onlayer cgl
    elif _ce_t == 4:
        show bg ce_break_room onlayer bgl
        show ce_pruitt verdict at vn_cast_slot
        "Ms. Pruitt catches you in the break room and looks at you over her glasses for a long time. The chest. The hips. The hair at your collar."
        ce_pruitt "\"You've changed your hair.\""
        ce_you "\"Yes.\""
        ce_pruitt "\"And everything else.\""
        "You open your mouth. Nothing arrives. She taps the coffee machine where it sticks."
        ce_pruitt "\"Do the shifts, and I don't care.\""
        "It's the kindest thing anyone here has ever said to you, and she says it like a stock notice."
        hide ce_pruitt
    else:
        $ ce.fit = "casual"
        show ce_pc snark at vn_pc_slot
        show cg ce_vest_hook onlayer cgl
        "You work in your own top. Nobody says a thing about the vest on the hook."
        hide cg onlayer cgl
        show ce_dougie red at vn_cast_slot
        "Dougie brings you a coffee you didn't ask for and stands there like he wants to say something enormous."
        hide ce_dougie
        show ce_pruitt verdict at vn_cast_slot
        ce_pruitt "\"Do the shifts.\""
        "From the door, to both of you."
        hide ce_dougie
    "The shift ends. Ms. Pruitt signs your sheet without looking up."
    $ vn_pass(260)
    $ ce.fit = "casual"
    return

## The dark window by the bandstand (Celestia Mirror).
label ce_mirror:
    $ _ce_t = 6 if (ce.loft or 0) >= 5 else max(0, min(5, ce.tier or 0))
    $ vn_enter(bg="ce_dark_window", pc="snark", pc_tag="ce_pc", cast=[], cg="ce_mirror_%d" % _ce_t)
    $ renpy.show("cg ce_mirror_%d" % _ce_t, layer="cgl")
    if _ce_t == 2:
        "Your throat's smooth in the glass. No bump. You swallow and nothing moves."
        ce_you "\"Hello.\""
        "To check. The window says it back a step higher. Your waist goes in under the hoodie now, like somebody pinched it."
    elif _ce_t == 3:
        "Side-on, the hoodie has a shape at the front. Two soft little swells. Your hips push the jeans out, and your face is doing something soft round the jaw."
        "You pull the hoodie away from your chest. You let it go. It settles back over them."
    elif _ce_t == 4:
        "All curves. Hips the hoodie can't hide, an ass that fills the jeans, a chest that tents the zip, hair at your collar."
        "The guy in the window is a girl in a guy's hoodie. She's not bad. You check if anyone saw you think that."
    elif _ce_t == 5:
        "A girl in the dark glass. Flushed. Soft mouth, heavy chest, wide hips, the whole of her in your old hoodie like she stole it off a boyfriend."
        "You press your thighs together. Nothing's there to get in the way any more."
    else:
        "Celestia Star in the glass: starfield tails, violet eyes, a chest out to here. In a hoodie."
        "She looks exactly like the form, because she is the form. There's nothing left to change back from."
    $ vn_pass(15)
    return

## The bandstand (Celestia Hub's first lines, the sortie due, Celestia Luna).
label ce_bandstand:
    $ _ce_n = min(6, (ce.tier or 0) + 1)
    $ _ce_t = 6 if (ce.loft or 0) >= 5 else max(0, min(5, ce.tier or 0))
    $ vn_enter(bg="ce_bandstand", pc="snark", pc_tag="ce_pc", cast=[("ce_luna", "deadpan")], cg=None)
    show bg ce_bandstand onlayer bgl
    $ _ce_c = ce_cue()
    "{color=#ff8fc8}[_ce_c]{/color}"
    $ _ce_p = ce_power_line()
    "[_ce_p]"
    if _ce_n == 6:
        if ce_dark():
            show bg ce_bandstand_dark onlayer bgl
            "{color=#ff6b6b}The sky over the park has gone the colour of a bruise, and it isn't evening. Violet threads hang off every tree. He isn't waiting any more.{/color}"
            show ce_luna flat at vn_cast_slot
            ce_luna "\"You fed him every time you let go. There's a great deal of him now.\""
            "Luna doesn't look at you."
        else:
            show bg ce_arena onlayer bgl
            "{color=#ff8fc8}The far side of the park is wrong. The trees are shedding petals of light, and there are constellations over the bandstand in the middle of the day.{/color}"
            ce_luna "\"He's here. He's brought everyone. Go.\""
            "Luna's tail is fluffed out like a bottle brush."
    else:
        $ _ce_pl = CE_PLACE[_ce_n]
        ce_luna "\"[_ce_pl]. Now. I'll be on your shoulder, and then I won't be, because I don't watch.\""
        "Luna drops off the rail."
    "{color=#b7b7b7}You ask Luna something.{/color}"
    if ce_dark() and not ce.done:
        show ce_luna smug at vn_cast_slot
        ce_luna "\"Ask.\""
        "Before you've opened your mouth."
        ce_you "\"How bad is it?\""
        show ce_luna flat at vn_cast_slot
        ce_luna "\"Bad. Every time you let go, it went to him. I did tell you. I told you in a way that was very easy to ignore.\""
        "No lightness on it at all. Her ears go flat."
        ce_luna "\"Fine. That one's mine.\""
    elif _ce_t == 2:
        ce_luna "\"One rule, and I'll say it once, so listen. Every time you let it take you, he gets stronger. Every time. That's it.\""
        ce_you "\"Why?\""
        ce_luna "\"That's a second question. Second questions cost tuna.\""
    elif _ce_t == 3:
        ce_luna "\"You've stopped asking if it's permanent.\""
        ce_you "\"You never answered.\""
        ce_luna "\"I never lied, either. Those are different, and you'd be amazed how few people notice.\""
    elif _ce_t == 4:
        ce_luna "\"She's good for you. The one with the sketchbook. Don't tell her I said so. She'll make a poster.\""
        "Apropos of nothing."
    else:
        ce_luna "\"You're her all the time now. Good. Saves on the light show.\""
        "She looks you up and down."
    hide ce_luna
    $ vn_pass(20)
    return

## An ordinary night at Pippa's, when none is owed (Celestia Loft, by rung). Optional.
label ce_loft_visit:
    $ _ce_k = 6 if (ce.loft or 0) >= 5 else max(2, min(5, ce.tier or 2))
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[("ce_pippa", "soft")], cg=None)
    show bg ce_loft onlayer bgl
    "The loft: fairy lights, half-finished canvases, the smell of turpentine and instant coffee, and Pippa on the beanbag with her sketchbook."
    hide ce_pippa
    if _ce_k == 2:
        show cg ce_visit_2 onlayer cgl
        "She pats the beanbag. You sit. She climbs into your lap like it's a chair she owns and kisses you, slow, grinding down, until your hips are pushing up at her through your jeans."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Hi.\""
        ce_you "\"Hi—\""
        "Her hand's already on your fly. She gets you out and wraps her fist round your cock, and your new voice goes straight up an octave."
        ce_you "\"Ahh— Pippa— {i}slow{/i}—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Nope.\""
        vn_sfx "Shk, shk, shk."
        "She watches your face the whole time, grinning, thumb swiping the tip on every upstroke."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Your hands are prettier than mine now. That's so rude. Do you know how rude that is?\""
        ce_you "\"Nnh— sorry— {i}ahh{/i}—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Don't be sorry. Be loud.\""
        show cg ce_visit_2_cum onlayer cgl
        "You're loud. You come in her fist, bucking up off the beanbag, and she milks you through it like she's been practising." with vnfx("flash")
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Data point.\""
        "Murmuring it, and writing nothing down."
    elif _ce_k == 3:
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Hoodie. Up.\""
        show cg ce_visit_3 onlayer cgl
        "You pull it up. Two little swells, the puffy nipples standing out off them. She makes a noise like she's been handed cake. She gets her mouth on the left one and sucks."
        ce_you "\"{i}Ahh—!{/i}\""
        "So loud the radiator rattles."
        ce_you "\"Pippa— they're— they're so {i}sensitive{/i} now—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"I know.\""
        "Delighted, round your nipple, and does the other one. Her hand slides into your jeans and finds your cock, smaller than it was, hard as anything. She strokes it in time with her tongue."
        ce_you "\"Suck— {i}harder{/i}— ohh— {i}yes{/i}—\""
        show cg ce_visit_3_cum onlayer cgl
        "You come with her mouth on your chest and her hand down your jeans, and you don't even transform. You don't need to." with vnfx("flash")
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Data point.\""
        "Very pleased, wiping her hand on your hoodie."
    elif _ce_k == 4:
        show cg ce_visit_4 onlayer cgl
        "She paints you. Properly, on the big canvas, hoodie off, hips and chest and all. Halfway through she puts the brush down."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"I need to check something. For the painting.\""
        "Very serious. She kneels between your knees, pushes your tits together with both hands, and looks up at you over them."
        ce_you "\"Oh. Oh, you're going to—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"No light show. Just you.\""
        show cg ce_visit_4_titjob onlayer cgl
        "She tugs your jeans open, gets your tiny cock between your own breasts, and squeezes. They're big enough now. Out of the form. Just yours."
        vn_sfx "Shlk. Shlk. Shlk."
        ce_you "\"Ahh— Pippa— oh my god, they're {i}mine{/i}— they're actually—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Yeah, they are. Shine for me.\""
        "She licks the tip every time it pokes out of your cleavage."
        show cg ce_visit_4_cum onlayer cgl
        "You do, all over your own chest, moaning her name at the skylight." with vnfx("flash")
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"For reference.\""
        "And goes back to the canvas."
    elif _ce_k == 5:
        show cg ce_visit_5 onlayer cgl
        "She pulls you down on the beanbag, her thigh between yours, and kisses you until you're rocking against it and gasping into her mouth."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Still getting used to it?\""
        ce_you "\"Every— {i}ahh{/i}— every time—\""
        "Her hand slides down the front of your jeans. Her fingertips find your clit and circle it, slow, outside, never in. You arch up off the beanbag."
        ce_you "\"Pippa— {i}Pippa{/i}— right there— don't stop—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Shine for me.\""
        "And you do, shaking, clutching the back of her sweater, your thighs clamped round her wrist." with vnfx("flash")
    else:
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Today's the day, isn't it.\""
        "Not a question."
        show cg ce_visit_6 onlayer cgl
        "She pulls your hoodie up anyway. Gets both hands on your tits, huge and heavy now, and buries her face between them, and hums."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Mmph. For luck.\""
        ce_you "\"Pippa— {i}ahh{/i}— you're going to make me—\""
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Good. Go out there wet.\""
        "She kisses you like she's putting something in your pocket for later."
        show ce_pippa grin at vn_cast_slot
        ce_pippa "\"Go and be ridiculous. Come back to me after.\""
    hide cg onlayer cgl
    $ vn_pass(90)
    return

## ---- rung 3: Club Orbit (Celestia Orbit, Orbit Sex|Shine, Orbit Done) --------------------------------------

label ce_orbit:
    $ ce.sortie_day = vn_clock.day
    $ vn_enter(bg="ce_club", pc="snark", pc_tag="ce_pc", cast=[], cg="ce_orbit_door")
    show cg ce_orbit_door onlayer cgl
    "Club Orbit: a basement off Connudatus Street. Bass coming up through the pavement. Purple fog rolling out the door that isn't from any machine."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Subtlety. The hallmark of villainy.\""
    "On your shoulder."
    show cg ce_orbit_floor onlayer cgl
    "Inside it's hot and dark and everybody's touching somebody. Couples, knots of bodies, hands up shirts, someone getting fingered on the speaker stack, and every face the same: slack, glassy, nobody home. They sway on the beat like they're hung off it."
    ce_you "\"Sex dungeon with a cover charge.\""
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Toilets. End stall.\""
    show bg ce_toilets onlayer bgl
    hide cg onlayer cgl
    "You lean on the stall wall and breathe it, like your own name."
    ce_you "\"Celestial prism...\""
    "It's already happening."
    $ ce_morph(3)
    show cg ce_shine_3 onlayer cgl
    "{color=#ff5fb8}Light, slick and fast. The chest comes in bigger than last time, heavier, nipples ridged hard against the white. The tails brush your ass and make you shiver. Your cock's smaller. Pathetically small, against all that.{/color}" with vnfx("flash")
    show bg ce_club onlayer bgl
    show cg ce_orbit_spot onlayer cgl
    "You step out onto the floor, and the spotlight swings round, and there he is."
    show ce_nightshade bored at vn_cast_slot
    "Professor Nightshade. Willowy, porcelain-pale, midnight hair to his waist, ice-blue eyes, a beauty mark at the corner of his mouth. A high-collared black coat. He looks at the room's lust like it's store-brand ramen."
    show ce_nightshade hungry at vn_cast_slot
    "Then he looks at you, and he doesn't look bored at all."
    ce_nightshade "\"Celestia Star. Tonight, you feed me.\""
    "And he's at your ear, though he was across the room."
    ce_you "\"Can you monologue for a minute so I can punch you?\""
    hide ce_nightshade
    show cg ce_orbit_tails onlayer cgl
    "He smiles. Winds your left tail round his gloved wrist. Then the right. Lifts. Your arms go up with them. Your chest thrusts out for the whole floor."
    ce_you "\"Hey— HEY— let go of my hair, you overdressed— put me {i}down{/i}—!\""
    "You kick. Your boots skid on the floor. He doesn't even shift his weight."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You'll come for me when I tell you.\""
    ce_you "\"Like HELL I—\""
    "Every face in the club turns to you."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "{color=#c79bff}{i}\"Come.\"{/i}{/color}"
    show cg ce_orbit_come onlayer cgl
    vn_sfx "THUMP." with vnfx("flash")
    "Goes the bass, and you come. Out of your chest. On the beat. No warning, no build, just {i}gone.{/i}"
    ce_you "\"No— no no NO— {i}ahh{/i}— {i}AHHH{/i}—!\""
    "Light sprays off your nipples, and something wetter. He catches the shimmer in his palm and licks it off."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Delicious.\" {color=#c79bff}{i}\"Again.\"{/i}{/color}"
    vn_sfx "THUMP." with vnfx("flash")
    ce_you "\"Don't— don't you— {i}stop doing that{/i}— {i}ahhhh{/i}—!\""
    "You come again. On his word. Your legs shake. The floor howls along with you, every puppet in the room, on the same beat."
    show cg ce_orbit_circle onlayer cgl
    "He walks you round in a slow circle by your tails, showing you off. The dancers press in close, empty-eyed. Hands on your hips, your thighs, your ass. A girl in glitter licks a stripe up the side of your tit without blinking. Your little cock is leaking straight through the leotard."
    ce_you "\"Get them OFF me— this isn't— I'm not {i}doing{/i} this— {i}nnh{/i}— not again— not {i}again{/i}—\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You can. You will. Watch.\" {color=#c79bff}{i}\"Again.\"{/i}{/color}"
    vn_sfx "THUMP." with vnfx("flash")
    "It's knocked out of you with a squeal, overfull, too good, your little cock pulsing uselessly in the leotard."
    ce_you "\"{i}Ahhh{/i}— I hate you— I {i}hate{/i} you— {i}ahh{/i}—!\""
    show cg ce_orbit_kiss onlayer cgl
    "He turns your face by the chin and kisses you. You bite at him. He laughs into your mouth and steals the aftershocks right off your tongue anyway. His gloved hand slides down between your breasts and pushes them together round nothing."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Now be a good star and give me the rest. Or don't. I'm taking it either way.\""
    menu:
        "\"I'm taking it either way.\""
        "Let it go to him" (ending="counts"):
            $ ce_let_go(3)
            jump ce_orbit_sex
        "Make it shine" (ending="counts"):
            $ ce_shine(3)
            jump ce_orbit_shine

label ce_orbit_after:
    $ vn_enter(bg="ce_club", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_orbit_after")
    show cg ce_orbit_after onlayer cgl
    if ce_enc.partner_came:
        "He comes between your tits, long and slow and cold, and paints the underside of your chin with it, and the whole club gasps like it felt it."
    else:
        "He pulls back before he finishes. He doesn't need to. He has what he came for."
    "It replays while you kneel there panting. Your own tails still knotted round your wrists, holding your arms up out of the way. His gloved hands mashing your tits together round him, because you wouldn't. His cock sliding through your cleavage, pale and slick, up to your chin, down, up, bumping your mouth every time you opened it to yell at him."
    ce_you "\"Get it— {i}mmf{/i}— get it away from my— {i}ahh{/i}—\""
    "\"Again,\" he'd say, and squeeze them tighter round him. \"Again.\" And your hips would rock on nothing, and your little cock would twitch in the leotard, and the dance floor would moan along with you, every puppet on his beat."
    ce_you "\"Stop— stop making me— {i}nnnh{/i}— don't you DARE stop— {i}no{/i}— {i}ahhh{/i}—\""
    show cg ce_orbit_drink onlayer cgl
    "And you give him the rest. Your chest goes off one last time, the biggest yet, and it all pours out of you into his open hands." with vnfx("flash")
    "He drinks it. Visibly. Colour comes up into his porcelain cheeks."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Delicious.\""
    "And he's gone in a twist of violet mist.\n{size=-5}{color=#ff8fa3}▸ Stagger back to the toilets{/color}{/size}"
    jump ce_orbit_done

label ce_orbit_shine:
    $ vn_enter(bg="ce_club", pc="shining", pc_tag="ce_pc", cast=[], cg="ce_orbit_kiss")
    show cg ce_orbit_kiss onlayer cgl
    ce_you "\"Not on {i}your{/i} word.\""
    "Panting. He tugs your tails. Your back arches. His gloved thumb drags across your nipple and your whole body jolts like he flipped a switch."
    ce_you "\"Ahh— {i}stop{/i}— no— {i}ahh{/i}—\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You'll come when I tell you.\""
    ce_you "\"I'll come when {i}I{/i} tell me.\""
    "You get your hands on your own tits, squeeze them together under his chin, and say it yourself."
    ce_you "\"{color=#ff8fc8}Celestial— Charm— {i}BLAST!{/i}{/color}\""
    show cg ce_orbit_blast onlayer cgl
    vn_sfx "FWOOOM." with vnfx("flash")
    "It's yours. That's the difference, and it's everything. Light flares out of you and blows his grip off your tails, and you come so hard you scream, and the floor screams with you."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You held. How long can you keep doing that, I wonder?\""
    "He spins away into violet mist, laughing.\n{size=-5}{color=#ff8fa3}▸ Stagger back to the toilets{/color}{/size}"
    jump ce_orbit_done

label ce_orbit_done:
    $ ce_rung(3)
    $ ce_demorph(3)
    $ vn_enter(bg="ce_toilets", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_demorph_3")
    ce_you "\"Let me be me. Just for a minute.\""
    "A whisper, in the stall. The light boils off you. Hoodie, jeans. Something pulls at your chest. You lift the hoodie and look down."
    show cg ce_demorph_3 onlayer cgl
    "{color=#ff5fb8}Two small breasts. Soft little swells, the nipples hard. You cup one and gasp at the jolt.{/color}"
    ce_you "\"{i}Ahh{/i}— oh god— I've got {i}tits{/i}—\""
    "{color=#ff5fb8}You squeeze both. A soft little handful each, warm, bouncing back into your palms. A B. A whole B, in a club toilet.{/color}"
    ce_you "\"{i}Hhnn{/i}— they're {i}mine{/i}—\""
    "{color=#ff5fb8}Your hips push at your jeans. Your ass is fuller, heavier, the denim biting into it. And under your fly your cock's smaller. Tucked up soft where it used to sit heavy. The face in the mirror is softer round the jaw.{/color}"
    $ _ce_feel = CE_FEEL[3]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    hide cg onlayer cgl
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Don't pout. They suit you. Your girlfriend's waiting.\""
    "From the sink."
    ce_you "\"She's not my—\""
    hide ce_luna
    "Your phone buzzes."
    "{color=#ff8fc8}PIPPA: u alive?? you're TRENDING. #BimboMagicalGirl{/color}"
    "{color=#ff8fc8}PIPPA: come over. bring ur new boobs. i have snacks and my mouth{/color}"
    $ _ce_p = ce_power_line()
    "[_ce_p]\n{size=-5}{color=#ff8fa3}▸ Pippa's{/color}{/size}"
    $ ce_next_loft = "ce_lab"
    jump ce_loft_door

## ---- the lab (Celestia Lab, Lab Morning) ---------------------------------------------------------------------

label ce_lab:
    $ vn_enter(bg="ce_lab", pc="flushed", pc_tag="ce_pc", cast=[("ce_pippa", "bralette")], cg=None)
    show bg ce_lab onlayer bgl
    "The loft's been turned into a lab. Chalk circles on the floorboards. Post-its on the windows that say PHENOMENA? A bottle of lube, a pile of lingerie, a little dish shaped like a moon."
    "Pippa's in a pink-and-teal chemise and striped thigh socks and nothing else."
    ce_pippa "\"Welcome to the magical girl titty lab.\""
    "She holds up a white lace bralette with a big gold star on each cup."
    ce_pippa "\"Thrift store. It'll last as long as it takes me to look at it. Stand in the circle. Breathe it.\""
    "You breathe it. Like your name. It's on you before you've finished the thought."
    $ ce_morph(3)
    hide ce_pippa
    show cg ce_lab_bralette onlayer cgl
    "She slides the bralette on over the leotard. It doesn't stand a chance. The gold stars stretch to nothing over your tits." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Data point. Weaponised.\""
    "Breathing it."
    show cg ce_lab_suck onlayer cgl
    "She lays you back on the beanbag and tugs the bralette up. Your nipples spring out, already puffed and tight. She gets her mouth on the left one."
    ce_you "\"Ahh— {i}ahh{/i}— Pippa—!\""
    "Suck. Tongue. Teeth. She swaps sides and her glasses fog up. You arch up into her mouth at exactly the right angle, every time. Your body just knows now. You can't stop grinding your thighs together. Your little cock's drooling down the inside of the leotard."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I love how magic makes you blush.\""
    "And pinches the wet one."
    show cg ce_lab_titjob onlayer cgl
    "She squeezes your tits together and slots your cock between them, spits on it, and pumps them up and down round it with both hands, slow, while she sucks the tip every time it pops out of your cleavage."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Scientific measurement. How long until detonation—\""
    "Sing-song."
    ce_you "\"Pippa— don't you {i}dare{/i} count—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Fine. Final form: reverse cowgirl?\""
    ce_you "\"Yes— whatever that— {i}yes{/i}—\""
    show cg ce_lab_reverse onlayer cgl
    "She swings round, straddles your hips facing away, peels the leotard off your cock, and heaves your tits up and back over her own shoulders. They swallow her head. She squeezes them round your cock from behind and starts to bounce."
    vn_sfx "Shlk. Shlk. Shlk."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Your tits are eating my {i}head.{/i} Never been this jealous of a pair of boobs in my life—\""
    "She gasps it, laughing, grinding herself on your thigh. Your nipples drag on her bare shoulders every bounce. You can't talk. You're just noise."
    ce_you "\"Ahh— {i}ahh{/i}— {i}ahhh{/i}—!\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Come for me, babe. Show me how bright you shine—\""
    show cg ce_lab_cum onlayer cgl
    "You come up between your own tits, all over her back and her chemise, and the light strobes off you so hard the post-its flutter." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Data point. Peak output: critical. Be advised.\""
    "She collapses forward on her forearms, giggling."
    $ ce_demorph(3)
    $ ce.fit = "nude"
    show ce_pc shocked at vn_pc_slot
    show cg ce_lab_nipples onlayer cgl
    "You towel off with her paint rags, bare-chested, and freeze."
    "{color=#ff5fb8}Your nipples. Out of the form. Big, puffy, dark, sticking out off your little breasts, tingling every time the air moves.{/color}"
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"They've been puffy for days, genius. You just never look in a mirror.\""
    "Already grinning. She flicks one. You nearly jump out of your skin."
    hide cg onlayer cgl
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"If you're both done cross-contaminating the samples.\""
    "On the sill again, as if she'd never left.\n{size=-5}{color=#ff8fa3}▸ Stay the night{/color}{/size}"
    hide ce_luna
    $ ce.loft = max(ce.loft or 0, 3)
    call vn_night(8)
    jump ce_lab_morning

label ce_lab_morning:
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_lab_morning")
    show cg ce_lab_morning onlayer cgl
    "Morning. Pippa's sitting cross-legged on the bed, sketching your sleeping face, tongue between her teeth."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You snore cute now. That's new.\""
    "You put your hand on your chest under the sheet. Still there. Still puffy. Still yours."
    show cg ce_lab_morning_suck onlayer cgl
    "Pippa sees you checking. She puts the sketchbook down, crawls up the bed, pulls the sheet off you and closes her mouth over your left nipple."
    ce_you "\"Mmh— {i}morning{/i}— ahh—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Morning.\""
    "Round it, and she sucks until your toes curl. Her hand finds your cock under the sheet and strokes it, lazy, like she's got all day."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Data point. Still works without the costume.\""
    ce_you "\"Pippa— I'm gonna— {i}ahh{/i}—\""
    show cg ce_lab_morning_cum onlayer cgl
    "You come in her hand with her mouth on your chest and the morning light all over both of you." with vnfx("flash")
    "Your phone buzzes."
    $ _ce_t = CE_TEXTS[4]
    "{color=#ff8fc8}LUNA: [_ce_t]{/color}\n{size=-5}{color=#ff8fa3}▸ Back to the bandstand{/color}{/size}"
    jump ce_day

## ---- rung 4: the night bus, the mandatory scene (Celestia Bus, Bus Seat, Bus Sex, Bus After, Go|Shine, Done) --

label ce_bus:
    $ ce.sortie_day = vn_clock.day
    $ ce.fit = "casual"
    $ vn_enter(bg="ce_bus", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_bus_packed")
    show cg ce_bus_packed onlayer cgl
    "The last bus out of town. Every seat taken. The aisle packed shoulder to shoulder. The windows fogged violet from the inside."
    "You're you: hoodie zipped to the chin, jeans losing a war with your hips, your puffy nipples catching on the cotton every time the bus brakes."
    "The speakers crackle."
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Good evening, passengers. Tonight's star is on board.\"{/i}{/color}"
    "His voice. Every glassy head on the bus turns round at once, like one puppet on a lot of strings."
    ce_you "\"Oh no.\""
    show cg ce_bus_hand onlayer cgl
    "A whisper. A hand lands on your hip. Just a hand. Warm, heavy, a stranger's. And the light comes up in you on its own."
    ce_you "\"No— wait— I didn't {i}say{/i} it—\""
    $ ce_morph(4)
    show cg ce_shine_4 onlayer cgl
    vn_sfx "FWOOM." with vnfx("flash")
    "{color=#ff5fb8}Leotard. Boots. Tails. Your chest, bigger than ever, bursting the hoodie into ribbons of light. Your hips flare against the strangers either side. Your cock, tiny now, bounces in the front of the leotard where the whole aisle can see.{/color}"
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"There she is. Say it for them, Celestia.\"{/i}{/color}"
    "Purring. Hands. On your waist. On your ass. Somebody cups a tit from behind and squeezes, slow, with a face like a sleepwalker. You know exactly what he wants you to say. You are not saying it."
    menu:
        "You are not saying it."
        "\"Get OFF me—\"":
            $ ce.bus_tone = "loud"
        "\"Don't you DARE—\"":
            $ ce.bus_tone = "soft"
    jump ce_bus_seat

label ce_bus_seat:
    if ce.bus_tone == "loud":
        ce_you "\"Get OFF me! All of you, get {i}off{/i}— wake UP—!\""
        "You yell it at the speakers, at him, at the whole bus. Nobody wakes up. The hands just tighten."
    else:
        ce_you "\"Don't you {i}dare.{/i} Don't you DARE, you fog-brained—\""
        "You snarl it at the speaker grille."
        show ce_nightshade bored at vn_cast_slot
        ce_speaker "{color=#c79bff}{i}\"Oh, I dare.\"{/i}{/color}"
        "The hand on your hip squeezes."
    show cg ce_bus_seat onlayer cgl
    "They take you down the aisle by your arms and your tails. Bend you over a seat back and hold you there, a hand flat between your shoulder blades. Your tits spill over it into the laps of the people in the seat, who fill their hands with them, blank-eyed, squeezing them out of the leotard, rolling the nipples."
    ce_you "\"Ahh— {i}ahh{/i}— stop— everybody's— get your {i}hands{/i}—\""
    show cg ce_bus_window onlayer cgl
    "Somebody kneels in the aisle and runs their hands up the insides of your thighs, slow, and spreads them. Somebody else gets your tails in a fist and turns your face to the window, so you can see yourself: Celestia Star pinned over a bus seat, tits out, mouth open, glowing."
    ce_you "\"Nnh— they can— everybody can {i}see{/i}— let me UP—\""
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"That's the point.\"{/i}{/color}"
    show cg ce_bus_behind onlayer cgl
    "Behind you, a big guy hooks the leotard aside. Your ass bare to the whole bus. Your little cock dangling, hard and tiny, and you hate that it's hard."
    "His cock lands between your cheeks. Hot. Heavy. Slick with something. It slides up and down your crack, then stops, pressed right against your hole."
    ce_you "\"No— no no no, not THERE— I've never— don't you {i}dare{/i}—\""
    "His face in the window is empty. His hands on your hips aren't. The bus rocks. His hips nudge."
    vn_sfx "Push."
    "{size=-5}{color=#ff8fa3}▸ Pinned over the seat back{/color}{/size}"
    jump ce_bus_sex

label ce_bus_after:
    $ vn_enter(bg="ce_bus", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_bus_after")
    show cg ce_bus_after onlayer cgl
    if ce_enc.partner_came:
        "He finishes with a groan, hips jammed to your ass, and you feel every hot pulse of it. Your tiny cock bounces in the leotard and dribbles down the seat back, untouched, while the hands in the seat keep milking your tits."
    else:
        "He stays buried in you, both of you shaking, while the bus rocks round a corner."
    "It replays on its own: the slap of his hips, your tails in somebody's fist, your own voice the whole time, yelling at them to get off, high and wrecked and so loud the driver must have heard. Your first time. On a bus. Pinned. And your cock bounced the whole way, and it didn't matter at all."
    "And then the moment it went. Mid-thrust, with his voice in the speakers and your ass full and your tits in strangers' hands, you heard yourself say it. Out loud. To the whole bus."
    "{i}I surrender.{/i}"
    "And after that you weren't yelling {i}get off{/i} any more. You were yelling {i}harder.{/i}"
    "And you're still there. Right on the edge. The big one, packed into your chest, burning to go off."
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Come for me, little star. Come on my word.\"{/i}{/color}"
    menu:
        "\"Come on my word.\""
        "Let it go to him" (ending="counts"):
            $ ce_let_go(4)
            jump ce_bus_go
        "Make it shine" (ending="counts"):
            $ ce_shine(4)
            jump ce_bus_shine

label ce_bus_go:
    show cg ce_bus_go onlayer cgl
    "The guy behind you is still in you. He starts moving again, slow, and the hands on your tits squeeze in time with him. Somebody's thumb is rubbing the head of your tiny cock through the leotard."
    vn_sfx "Pap... pap... pap."
    ce_you "\"Nnh— {i}ahh{/i}— please— please let me—\""
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Beg properly.\"{/i}{/color}"
    ce_you "\"Please, Professor— let me come— let me {i}come{/i}—\""
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Come.\"{/i}{/color}"
    show cg ce_bus_go_cum onlayer cgl
    "You do. On his word, through a bus speaker, bent over a seat with your ass full and your tits in strangers' hands." with vnfx("flash")
    ce_you "\"Ahh— {i}AHHH{/i}— Professor— {i}Professor{/i}—!\"" with vnfx("shake")
    "The whole bus comes with you. A long, rolling wave of moans up and down the aisle. The guy behind you grinds in to the root and floods you with a grunt, hot, so much it runs down your thighs. And all of it, all of yours, goes out of you and up into the speakers like smoke up a chimney."
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Delicious.\"{/i}{/color}"
    "And clicks off.\n{size=-5}{color=#ff8fa3}▸ Sit up{/color}{/size}"
    jump ce_bus_done

label ce_bus_shine:
    show cg ce_bus_go onlayer cgl
    "The guy behind you starts up again, slow. Every thrust shoves your tits deeper into the strangers' hands. Every squeeze sends it shooting down to your tiny cock and back up into your chest."
    vn_sfx "Pap... pap... pap."
    show ce_nightshade bored at vn_cast_slot
    ce_speaker "{color=#c79bff}{i}\"Come for me.\"{/i}{/color}"
    ce_you "\"Not yours. {i}Mine.{/i}\""
    "You gasp it. You grab your tits off the strangers, mash them together, and fire it into the roof of the bus."
    ce_you "\"{color=#ff8fc8}Charm— {i}BLAAAST!{/i}{/color}\""
    show cg ce_bus_blast onlayer cgl
    vn_sfx "FWOOOOM." with vnfx("flash")
    "The speakers squeal and die. The fog blows out of every window at once. You come so hard you see stars, clenching round the guy behind you until he empties into you with a groan, and the whole bus sighs with you.\n{size=-5}{color=#ff8fa3}▸ Sit up{/color}{/size}"
    jump ce_bus_done

label ce_bus_done:
    $ ce_rung(4)
    $ ce.fit = "casual"
    $ ce_demorph(4)
    $ vn_enter(bg="ce_bus", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_demorph_4")
    show cg ce_demorph_4 onlayer cgl
    "{color=#ff5fb8}You change back on the back seat. Hoodie. Jeans that won't close over your hips any more. Your chest pushing the zip out. Your hair brushing your collar.{/color}"
    "{color=#ff5fb8}You tug the zip down a little and they surge out against it. Round. Full. A DD at least, heavy enough to {i}sway{/i} when the bus brakes.{/color}"
    "You grab them before you can stop yourself."
    ce_you "\"{i}Ohh{/i}— fuck, they're so {i}full{/i}—\""
    $ _ce_feel = CE_FEEL[4]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    hide cg onlayer cgl
    "The passengers sit slumped, strings cut, blinking at the windows. A woman looks at her own wet hands and doesn't know why. Nobody looks at you."
    "{color=#ff5fb8}Your cock's small. Really small. You check, under the hoodie, with the bus asleep round you. It barely fills your fingertips. You squeeze it and it does nothing.{/color} Your ass clenches instead, remembering, and your hips roll like they know the rhythm now."
    show ce_luna smug at vn_cast_slot
    ce_luna "\"Well. That was educational. Feeling more at home in there?\""
    "Her head pops up over the seat in front. A drawl."
    ce_you "\"I could get used to it.\""
    "And your hips do a little wiggle, all on their own."
    hide ce_luna
    $ _ce_p = ce_power_line()
    "[_ce_p]\n{size=-5}{color=#ff8fa3}▸ Pippa's{/color}{/size}"
    $ ce_next_loft = "ce_confessions"
    jump ce_loft_door

label ce_confessions:
    $ vn_enter(bg="ce_loft_night", pc="flushed", pc_tag="ce_pc", cast=[], cg=None)
    show bg ce_loft_night onlayer bgl
    "Late. Fairy lights. You can barely sit down on the beanbag in your jeans."
    ce_you "\"It's not going to stop until I'm her all the time. Is it?\""
    "To the lights, not to her."
    show ce_pippa soft at vn_cast_slot
    "Pippa doesn't laugh. She slides her arms round you."
    ce_pippa "\"Then maybe this version was always the right one out of the box.\""
    "She fits her fingers through yours."
    ce_pippa "\"I love both of you. All of you. Even the one who screamed when I offered to boop her new boobs.\""
    ce_you "\"You're {i}sick.{/i}\""
    ce_pippa "\"Only for magical girls.\""
    "She draws the curtains. Kneels in front of you. Puts her hand on your hip. You get as far as \"Celes—\" and the light's already up."
    $ ce_morph(4)
    hide ce_pippa
    show cg ce_conf_lap onlayer cgl
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Lie back, starlight.\"" with vnfx("flash")
    "She peels her sweater off. No bra. Freckles, pink-tipped nipples. She climbs into your lap and palms your tits, slow, drawing circles round your huge swollen nipples."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Promise you'll let yourself enjoy it this time. No apologising. No shrinking.\""
    ce_you "\"I— {i}ahh{/i}— promise—\""
    "Her mouth on your nipple. Teeth. You bury your hands in your own tails and tug them like ropes, just to hold on to something."
    ce_you "\"Ahh— {i}ahh{/i}— Pippa, they're— they're even bigger than last time—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I noticed. I notice everything about these. I'm obsessed. It's a problem.\""
    "And she switches sides, and sucks so hard your back comes off the beanbag."
    show cg ce_conf_titjob onlayer cgl
    "Then she slides down, gathers your tits in both hands, and squeezes them round your cock, so small now it's nearly lost between them. She sucks the tip where it peeks out."
    ce_you "\"Oh my god— Pippa— {i}ohh{/i}—\""
    "Slow. Maddening. Up, down, her tongue spiralling under the head, her eyes on yours the whole time."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You're allowed to love this. To love her. Shine for me, baby.\""
    ce_you "\"Pippa— I— {i}ahhhh{/i}—!\""
    show cg ce_conf_cum onlayer cgl
    "You come on her chin. It drips down into her cleavage, and she laughs, delighted, and milks out the last of it." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"God, you're gorgeous when you let go. Told you she was worth loving.\""
    "She crawls up and kisses you, and you taste yourself."
    $ ce_demorph(4)
    $ ce.loft = max(ce.loft or 0, 4)
    "{size=-5}{color=#ff8fa3}▸ Fall asleep tangled up in her{/color}{/size}"
    call vn_night(8)
    jump ce_curves

## ---- day 5: the curves, then the warehouse (Celestia Curves, Warehouse, Lair, Lair Peak, Go|Shine, Outside, Embrace)

label ce_curves:
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_curves")
    show cg ce_curves onlayer cgl
    "Morning, soft and gold. Your head's in Pippa's lap. You move, and everything moves with you."
    "{color=#ff5fb8}You're all curves now. Hips wide. Thighs pressed snug. Breasts heavy enough to feel every time you breathe. And down there, a small, sensitive cock that twitches when the sheet brushes it.{/color}"
    "You sit up, and you have to lift your breasts to see your own lap. Pippa makes a small noise behind you."
    show cg ce_curves_hold onlayer cgl
    "She slides her arms round you from behind and fills her hands with them. Weighs them. Squeezes. Thumbs your nipples until you're squirming back against her."
    ce_you "\"Ohh— Pippa— they're so {i}heavy{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I know.\""
    "She kisses your neck. One hand slides down your stomach, between your thighs, and wraps round your tiny cock, so sensitive now it makes you squeal. A handful of strokes is all it takes. You come in her fist, quick and shaking, with your head back on her shoulder." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You look perfect. Almost there, huh?\""
    "She kisses your forehead."
    ce_you "\"Yeah.\""
    "A whisper. It doesn't come out scared. Your phone buzzes."
    $ _ce_t = CE_TEXTS[5]
    "{color=#ff8fc8}LUNA: [_ce_t]{/color}"
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I'm coming. Don't even.\""
    "Pippa heard every word.\n{size=-5}{color=#ff8fa3}▸ Back to the bandstand{/color}{/size}"
    hide ce_pippa
    jump ce_day

label ce_warehouse:
    $ ce.sortie_day = vn_clock.day
    $ ce.fit = "casual"
    $ vn_enter(bg="ce_elk_street", pc="snark", pc_tag="ce_pc", cast=[("ce_pippa", "soft")], cg=None)
    show bg ce_elk_street onlayer bgl
    "Elk Street, under the rail bridge. Black velvet in every window. The door's unlocked. Of course it is."
    "Pippa squeezes your hand. Hoodie over paint-spattered leggings, stompy boots, rainbow laces."
    ce_pippa "\"Texting villains is tasteless.\""
    "A whisper."
    show bg ce_warehouse onlayer bgl
    hide ce_pippa
    show cg ce_wh_mirrors onlayer cgl
    "Inside: incense, black candles burning purple, mirrors on every wall. In every one, not you. Her. Celestia Star, all hips and chest and starfield tails, looking back at you."
    ce_you "\"Is that how I really look?\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"That's you, babe. And damn.\""
    show ce_nightshade smile at vn_cast_slot
    ce_nightshade "\"Looking for me, precious things?\""
    "Nightshade, on a dais at the far end, coat collar framing his face like black petals. The velvet comes alive."
    "Ribbons whip round Pippa's wrists and pin her to a pillar. Nothing else touches her."
    ce_you "\"Don't you {i}touch{/i} her—\""
    ce_nightshade "\"I wouldn't dream of it. She's the audience.\""
    "He snaps his fingers."
    vn_sfx "SNAP." with vnfx("flash")
    hide ce_nightshade
    $ ce_morph(5)
    show cg ce_shine_5 onlayer cgl
    "{color=#ff5fb8}The form takes you. No words. Not yours. Leotard, boots, gloves, tails, a chest so heavy the air on it makes you gasp. Your tiny cock already leaking under the crotch panel.{/color}"
    show cg ce_wh_velvet onlayer cgl
    "The velvet surges up off the floor. Round your arms, yanking them over your head. Round your thighs, spreading them wide, lifting you onto your toes. Round your chest, squeezing your tits together till they bulge out of the leotard."
    ce_you "\"Put me DOWN— let go— let {i}go{/i} of me, you overgrown curtain—!\""
    "In every mirror, Celestia Star, strung up and spread open, kicking at nothing."
    "A thick ribbon of it slides up between your thighs and presses the crotch panel flat against your tiny cock, and rubs. Slow. Firm. A thin one slips inside the neckline and coils round your nipple and {i}pulls.{/i}"
    ce_you "\"Ahh— {i}ahh{/i}— don't— stop it— Pippa's {i}watching{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Get your {i}rags{/i} off her! You hear me? Get OFF her!\""
    "Pippa's hauling on her pillar so hard the velvet creaks."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Resistance is charming. Surrender is {i}art.{/i} You'll give me both.\""
    "His gloved thumb circling your nipple, murmuring.\n{size=-5}{color=#ff8fa3}▸ The velvet moves{/color}{/size}"
    jump ce_lair

label ce_lair_peak:
    $ vn_enter(bg="ce_warehouse", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_lair_peak")
    show cg ce_lair_peak onlayer cgl
    "It's everywhere at once."
    "One in your ass, slick and thick, fucking you in slow measured pumps. One coiled round your little cock, milking it, up and down, up and down. More of them twisting your nipples till you see stars. You're drooling. You're yelling so loud the mirrors hum, and none of it is {i}stop{/i} any more, not cleanly."
    ce_you "\"Get— OUT— get out of my— {i}ahh{/i}— {i}ahhh{/i}— too much— it's— {i}nnnh{/i}—\""
    show ce_nightshade bored at vn_cast_slot
    "Nightshade watches your face. Patient. Beautiful. A little bored."
    ce_nightshade "\"Just surrender, Celestia. I'll fill you. Please you. Melt you down to moans. You're going to come either way. All that's left is who for.\""
    "His finger trails down your cheek."
    hide ce_nightshade
    "The big one's building in your chest, bigger than any of them. You can feel how much of him is in this room. Whatever goes to him here goes double. For one terrible instant his name's in your mouth—"
    show cg ce_lair_pippa onlayer cgl
    "And Pippa's eyes catch yours in the mirror. Flushed, furious, pinned to her pillar."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"{color=#ff8fc8}[ce_pc_name]— Celestia— {i}you get to choose!{/i}{/color}\""
    menu:
        "\"You get to choose!\""
        "Let it go to him" (ending="counts"):
            $ ce_let_go(5)
            jump ce_lair_go
        "Make it shine" (ending="counts"):
            $ ce_shine(5)
            jump ce_lair_shine

label ce_lair_go:
    show cg ce_lair_go onlayer cgl
    "You break."
    "The velvet feels it. The one in your ass shoves deeper and starts to pump faster. The one on your cock squeezes tight and strokes, base to tip, base to tip. They wrench your nipples out of the leotard and twist."
    vn_sfx "Shlk-shlk-shlk."
    ce_you "\"No— {i}no{/i}— okay— okay, FINE— fuck me, fuck me, I don't care any more— {i}ahhh{/i}— {i}yes{/i}—\""
    "Pippa's shouting your name. You can't hear the words over yourself. He leans in until his lips brush your ear."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Say it.\""
    ce_you "\"Take it. Professor— {i}take it{/i}— take it all— {i}TAKE IT{/i}—!\"" with vnfx("shake")
    "You moan it, and you hate it, and you say it louder."
    show cg ce_lair_go_cum onlayer cgl
    "You come. Everything. Out of your chest in a flood, out of your cock in the velvet's grip, round the thing in your ass, and every drop of it pours into his open hands. He drinks it like wine. The mirrors go violet, one after another, all the way round the room." with vnfx("flash")
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Oh, {i}delicious.{/i} Run along, little star. I have all I need.\""
    "Swelling with it, glowing. The release is yours, though. It always was. It goes off through the velvet like a firework, and the velvet goes to glitter, and you hit the floor."
    "Pippa yanks free and drags you to the door.\n{size=-5}{color=#ff8fa3}▸ Outside{/color}{/size}"
    jump ce_outside

label ce_lair_shine:
    show cg ce_lair_shine onlayer cgl
    "Choice. Not his. Yours. The moan in your mouth turns into a snarl."
    ce_you "\"Get. {i}Off.{/i} Me.\""
    "You don't fight the pleasure. You take it. All of it."
    ce_you "\"Harder. {i}Harder.{/i} Is that all you've got?\""
    "You snarl it at the velvet. It goes harder. In your ass. Your little cock stroked so fast you see white. Your nipples twisted till you scream. And every bit of it piles up behind your breastbone, white-gold and humming, yours, {i}yours.{/i}"
    vn_sfx "Shlk-shlk-shlk."
    ce_you "\"Ahh— {i}ahh{/i}— {i}AHHH{/i}—\""
    "Every pump in your ass, every squeeze on your cock, every twist on your nipples, and you turn it into starlight, and you fire it out through your chest."
    ce_you "\"{color=#ff8fc8}CHARM— {i}BLAAAAST!{/i}{/color}\""
    show cg ce_lair_blast onlayer cgl
    vn_sfx "FWOOOOOOM." with vnfx("flash")
    "Silver and gold. The tentacles shriek and dissolve into glitter. Nightshade's eyes go wide for the first time."
    "You crash to the floor, shaking, still coming. Pippa rips free and catches you, laughing and kissing you, and drags you to the door.\n{size=-5}{color=#ff8fa3}▸ Outside{/color}{/size}"
    jump ce_outside

label ce_outside:
    $ ce_rung(5)
    $ ce.cunt = True
    $ ce.fit = "casual"
    $ ce_demorph(5)
    $ vn_enter(bg="ce_elk_street", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_outside")
    "Lamplight. Elk Street. You sag against the wall in your hoodie, skin still fizzing, thighs sticky. Your ass is still clenching on nothing, greedy, like it learned something in there."
    show cg ce_outside onlayer cgl
    "{color=#ff5fb8}Something's different. Something's {i}missing.{/i} Your hand slides down the front of your jeans.{/color}"
    "{color=#ff5fb8}No cock. No balls. Just soft, swollen lips, slick and hot and so sensitive your knees buckle. A pussy. Yours.{/color}"
    "{color=#ff5fb8}And your hoodie's tight across a chest that's bigger again. You drag it up and they flop out heavy into the lamplight. An F. Easy.{/color}"
    ce_you "\"Oh my {i}god{/i}—\""
    "One hand between your legs, one hand full of tit, and you can't pick. Your hair's slipped loose halfway down your back. Your ass is so round it's pushing you off the wall."
    ce_you "\"{i}Ahh{/i}— everything— there's so much {i}more{/i}—\""
    $ _ce_feel = CE_FEEL[5]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    show ce_pippa flushed at vn_cast_slot
    "Pippa's eyes go round. She grabs your hips."
    ce_pippa "\"You— you're—\""
    ce_you "\"Fully. Completely. I'm— fuck, Pippa, I'm a {i}woman.{/i}\""
    "You croak it. Your voice comes out lighter than it's ever been."
    ce_pippa "\"You're beautiful. And you still kick tentacle ass.\""
    "She hugs you so hard you squeak. She doesn't let go. Her hand slides down over yours, over the front of your jeans, and presses, just there, and your knees give against the wall."
    ce_you "\"Ahh— Pippa— it's so— everything's so {i}close{/i} to the surface—\""
    ce_pippa "\"Home. Now. Before I do something on Elk Street.\""
    "Against your mouth."
    hide ce_pippa
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "{color=#c79bff}{i}\"Your next choice will be your last, Celestia Star...\"{/i}{/color}"
    "From somewhere deep inside the warehouse, his voice, stung and hungry."
    $ _ce_p = ce_power_line()
    "[_ce_p]\n{size=-5}{color=#ff8fa3}▸ Home with Pippa{/color}{/size}"
    jump ce_embrace

label ce_embrace:
    $ vn_enter(bg="ce_loft_night", pc="flushed", pc_tag="ce_pc", cast=[("ce_pippa", "soft")], cg=None)
    show bg ce_loft_night onlayer bgl
    "She doesn't put the lamp on. Lavender light from the windows, the fairy lights, your reflection in the glass. Not him. Never him again."
    ce_pippa "\"Say the name.\""
    ce_you "\"Pip—\""
    ce_pippa "\"Not mine.\""
    "The loft is very quiet."
    $ ce.named = True
    $ ce_plate = "Celestia"
    ce_you "\"Celestia.\""
    ce_pippa "\"Yeah. There she is.\""
    $ ce.fit = "nude"
    hide ce_pippa
    show cg ce_embrace_kiss onlayer cgl
    "Then she's kissing you, pulling your hoodie over your head, your jeans down your legs. She kneels and gets her mouth on your nipple, and your knees actually shake."
    ce_you "\"God, Pippa— I can feel it {i}everywhere{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Good. I want to see you lose it.\""
    show cg ce_embrace_lick onlayer cgl
    "She pushes you back on the bed. Kisses down your stomach. Spreads your thighs. Looks."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh, you're {i}soaked.{/i}\""
    "Her tongue goes flat on your clit, and everything goes white."
    ce_you "\"{i}Eeee{/i}— ahh— {i}ahhhh{/i}—!\""
    "You squeal. Actually squeal. She hums, delighted, licking slow up and down your lips, round and round your clit, making filthy happy noises like it's a tasting menu."
    ce_you "\"Don't stop— Pippa, fuck, I'm close, I'm so—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Not stopping. Just waiting for you to beg.\""
    "She pulls back, chin glistening."
    ce_you "\"{i}Please.{/i} Ride me. I want to come with you. Please—\""
    show cg ce_embrace_trib onlayer cgl
    "She climbs up your body in one slide and straddles your thigh, and her pussy's hot and slick, grinding on you. Her hands full of your tits. Her mouth on yours."
    vn_sfx "Shlk. Shlk. Shlk."
    "Your thigh between hers, hers between yours. Clit against skin. Faster. Her nails on your nipples."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Look at me. Don't look away. I want to see your face when you come.\""
    "You look at her. Flushed, glasses gone, pink-tipped hair stuck to her forehead, grinding on you like she's been waiting her whole life. You wind a lock of your own hair round her wrist, just to tie her to you, and she giggles through a moan."
    ce_you "\"You're insatiable.\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You turn me on more than anything in my life. And now you're stuck with me.\""
    "She rides harder."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"I'm coming.\""
    "Biting your shoulder."
    ce_you "\"Me too— {i}Pippa{/i}— {i}ahhhhh{/i}—!\"" with vnfx("shake")
    show cg ce_embrace_cum onlayer cgl
    "You come together, bucking, clutching, her wetness spilling down your thigh and yours down hers, and sparks of gold go up off your skin into the fairy lights." with vnfx("flash")
    show cg ce_embrace_after onlayer cgl
    "Afterwards, she's curled on your chest with her face between your breasts and a hand tangled in your hair."
    show ce_luna smug at vn_cast_slot
    ce_luna "\"Well. It's about time.\""
    "On the laundry pile at the foot of the bed, where she definitely wasn't.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide ce_luna
    $ ce.loft = max(ce.loft or 0, 5)
    call vn_night(8)
    jump ce_remade

## ---- day 6: remade (Celestia Remade), then the park ------------------------------------------------------------

label ce_remade:
    $ ce_body(6)
    $ ce.look = True
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_loft", pc="shocked", pc_tag="ce_pc", cast=[], cg="ce_remade")
    show cg ce_remade onlayer cgl
    "Sunlight through the fairy lights. You stretch, and everything moves."
    "{color=#ff5fb8}Breasts, enormous, so heavy you have to lift one to see past it, the nipples swollen and pink. Hips out wide. An ass that fills the whole bed. Thighs soft and lush and pressed together over your pussy.{/color}"
    "You grab them. Both hands, and they spill everywhere, over your fingers, over your wrists, so heavy they pin you to the mattress."
    ce_you "\"{i}Ohhh{/i}— oh my god— they're {i}enormous{/i}— {i}ahh{/i}—\""
    "{color=#ff5fb8}A J. All of the form's, and it's staying. You squeeze, and moan, and squeeze again, and they just keep giving.{/color}"
    "You roll onto your side and your ass rolls after you, heavy, jiggling long after you've stopped. Your thighs squish together and your pussy throbs between them."
    ce_you "\"{i}Mmmh{/i}— everything's so {i}much{/i}—\""
    show cg ce_remade_hair onlayer cgl
    "{color=#ff5fb8}And your hair. Spilling over the pillow, down the bed, off the edge: starfield crescent tails, black-blue and full of little moving stars.{/color}"
    "{color=#ff5fb8}You grab your phone and look. Violet eyes. Celestia Star. Not the form. Not a light show. You.{/color}"
    ce_you "\"There's nothing left to change back from.\""
    "And your voice rings like a bell."
    $ _ce_feel = CE_FEEL[6]
    "{color=#ff8fc8}[_ce_feel]{/color}"
    show cg ce_remade_pippa onlayer cgl
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Mm. If I pinch your nipple, do I get a wish?\""
    "Pippa wakes up with her hand already on your breast."
    ce_you "\"Careful. That's the emergency button.\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"A risk I'm willing to take.\""
    "She pinches. Your whole body pebbles. She rolls on top of you and gets her mouth on the other one, sucking, humming, her hips rocking slow against your thigh."
    "You arch into her mouth and roll your hips up to meet hers without thinking. Your whole body knows what it's for now."
    ce_you "\"Pippa— {i}ahh{/i}— they're even more— oh my {i}god{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Bigger and more sensitive. The dream.\""
    "Round your nipple, delighted. She pushes both your tits together and buries her face in them and blows a raspberry, and you shriek and laugh and arch up into her all at once."
    vn_sfx "Pbbbbt."
    "Your phone buzzes."
    $ _ce_t = CE_TEXTS[6]
    "{color=#ff8fc8}LUNA: [_ce_t]{/color}\n{size=-5}{color=#ff8fa3}▸ The bandstand{/color}{/size}"
    jump ce_day

## ---- the showdown (ending.twee: Celestia Arena, Showdown, Showdown End, Morning, Keep|Hang) ----------------------

label ce_arena:
    $ ce.sortie_day = vn_clock.day
    $ ce_morph(6)
    $ vn_enter(bg="ce_arena", pc="snark", pc_tag="ce_pc", cast=[], cg="ce_arena")
    show cg ce_arena onlayer cgl
    "The park's an arena. Petals of light falling off every tree. Grass rippling like water. Constellations wheeling over the bandstand in broad daylight."
    "And the whole afternoon crowd, standing in rows, glassy-eyed, mouths open, violet threads running out of his hands and into every one of them. You see Dougie in there in his vest. Ms. Pruitt, her bun coming loose. A jogger. A man with a pram full of shopping."
    "You don't say anything. You don't need to. You walk out onto the lawn, and the leotard's just on you. Gloves, boots, choker, tails. There was never anything to change back from."
    show ce_nightshade smile at vn_cast_slot
    "Nightshade's on the bandstand steps, coat flaring, silver threads at his cuffs."
    ce_nightshade "\"Celestia Star, at last. Are you ready to surrender, little starlight? My spell's in all of them. Too strong, even for you.\""
    "Every word slides over your skin like silk."
    ce_you "\"I was never your little anything.\""
    hide ce_nightshade
    show cg ce_arena_strings onlayer cgl
    "He flicks his wrist. The threads pulse. And then they're in {i}you{/i}: a dozen violet strands off his fingers, straight through the leotard, into your chest."
    ce_you "\"Hey— HEY— get those OUT of me— get your stupid strings {i}out{/i}—!\""
    "He tugs. Your hands come up and grab your own tits. Not you. {i}Him.{/i}"
    ce_you "\"Stop— stop it— those are MY hands— {i}nnh{/i}— {i}ahh{/i}—!\""
    "He tugs again, and your fingers pinch your own nipples, hard, for the whole park. A bloom of want rolls off the crowd and hits you, chest first, then your nipples, then between your legs, so hard your thighs clamp together."
    ce_you "\"No— not in front of— {i}ahh{/i}— Dougie's {i}right there{/i}— let GO of me—!\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"You see? You'll come for me here, on my strings, in front of everyone you know. Why fight it? Become what you were made to be.\""
    "He licks his lips. Your hips roll on their own. The leotard's soaked through. Your mouth's still yelling no, and your body's already halfway there."
    "Then you see it. Every string in you runs back to his hands. Every string in {i}them{/i} runs back to his hands. You think of Pippa. {i}You get to choose.{/i}"
    menu:
        "{i}You get to choose.{/i}"
        "Make them stare":
            $ ce.pose = "stare"
        "Grin at him":
            $ ce.pose = "grin"
    jump ce_showdown

label ce_showdown:
    $ vn_enter(bg="ce_arena", pc="shining", pc_tag="ce_pc", cast=[], cg="ce_showdown")
    if ce.pose == "grin":
        ce_you "\"You want me to lose control? Careful what you wish for, Professor.\""
        "You catch his eye and grin, as filthy and star-bright as you can."
    else:
        "You turn to the crowd. All of them. You let every one of them look."
        ce_you "\"Go on. Stare.\""
    show cg ce_showdown onlayer cgl
    "And you stop fighting the strings. You take hold of them. Every thread of his spell, through your chest, on purpose. Your hands are your own again, and you put them right back where he had them: palm your tits in front of the whole park and squeeze. Tease your own nipples. Grind your hips on nothing. Let them all see."
    ce_you "\"Ahh— {i}ahh{/i}— that's it— {i}more{/i}— give me {i}more{/i}—\""
    "He blinks. He sends more. Your sex, your ass, your nipples, all of it at once. It feels like mouths everywhere. It feels like being fucked from every side by nothing at all."
    ce_you "\"Ohh— {i}fuck{/i}— is that all— is that {i}all you've got{/i}, Professor—\""
    show cg ce_showdown_bare onlayer cgl
    "You laugh. You take it. You pull the leotard down off your tits for the whole park and pinch your own nipples, hard, and the crowd moans with you, every puppet on every string, one huge sigh across the grass."
    "It builds and builds behind your breastbone, brighter than anything he's ever pulled out of you. Then it hits you like a comet."
    ce_you "\"{color=#ff8fc8}CHARM— {i}BLAAAAAAST!{/i}{/color}\""
    show cg ce_showdown_blast onlayer cgl
    vn_sfx "FWOOOOOOOM." with vnfx("flash")
    "You come on the bandstand steps in front of everyone. Back arched, tails flared out in arcs of starlight, light forking out of your nipples in twin beams. It goes on and on, loud and glorious, and you don't care who's watching, because everyone is." with vnfx("shake")
    show cg ce_showdown_back onlayer cgl
    "The light doesn't fly at him. It runs down his own spell. Down every thread, back into his hands, round his wrists, round his head. For the first time, Nightshade looks shocked."
    "Then he moans. Across the whole park, long and shattering, every bit of the pleasure he ever pushed into anybody coming back to him at once. His knees go. The circle fizzles out. The threads snap.\n{size=-5}{color=#ff8fa3}▸ Land{/color}{/size}"
    jump ce_showdown_end

label ce_showdown_end:
    $ ce_rung(6)
    $ ce.ending = "showdown"
    $ ce.fit = "casual"
    $ ce_demorph(6)
    $ ce.done = True
    $ achievement.grant("Starlit Showdown")
    $ vn_enter(bg="ce_bandstand", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_showdown_land")
    show cg ce_showdown_land onlayer cgl
    "You land on both feet in the middle of the lawn. The light lets go of you, and you're standing on the grass in your own clothes, in the same body. The only one you've got."
    "The strings snap, and the crowd wakes up. Confusion, then awe, then a cheer that goes all the way to the gates. Somebody yells \"We love you, Celestia!\" Phones come up everywhere."
    show cg ce_luna_sits onlayer cgl
    "Nightshade's face-down on the grass, suddenly, ordinarily thirty-five, his coat gone to drifting sparks. Luna is sitting on his back with an expression of enormous satisfaction."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Congratulations, Princess. You weaponised the town's horniest costume malfunction. I'll want an autograph.\""
    show cg ce_pippa_first onlayer cgl
    "Pippa gets to you first. She always does. Glasses crooked, pink tips everywhere, she barrels into you so hard you nearly go over."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"That was the most ridiculous, gorgeous thing I've ever seen. It's you. All you, you beautiful shining disaster.\""
    "Into your chest. You kiss her in front of the whole park, and the whole park wolf-whistles.\n{size=-5}{color=#ff8fa3}▸ Go home with Pippa{/color}{/size}"
    call vn_night(8)
    jump ce_morning

label ce_morning:
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_loft", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_morning")
    show cg ce_morning onlayer cgl
    "Morning in the loft. Sunlight through the fairy lights. Pippa's welded to your side, one leg over yours, a hand cupping your breast like the last melon at the market."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Mm. If I pinch your nipple, do I get a wish?\""
    "Without opening her eyes."
    ce_you "\"That's the emergency button.\""
    "She pinches it. You gasp, too loud, too bright. Her hand slides down your stomach and between your thighs, and she cups you, and her fingers slip between your lips."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh, you're already wet. Superheroine.\""
    show cg ce_morning_finger onlayer cgl
    "Her finger slides inside you."
    ce_you "\"Ahh— {i}oh{/i}— Pippa— {i}inside{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"First one. How's that?\""
    "Against your neck, and she curls it."
    ce_you "\"Again— {i}again{/i}—\""
    "Another finger. Pumping. Her thumb on your clit. Her mouth closing on your nipple. Your hips come off the bed."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Go ahead, big girl. Let 'em hear it.\""
    ce_you "\"God, I love you.\""
    "You gasp it, throwing pride out of the window, pressing your hips into her hand, squirming for more."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Yeah, you do. Gonna come for me quick, superheroine?\""
    "And she gets her mouth back on your nipple, and squeezes your other tit until you whimper."
    ce_you "\"I— fuck, Pippa, {i}yes{/i}—\""
    show cg ce_morning_cum onlayer cgl
    "You do. Loud. The whole street hears it. You come round her fingers with your head thrown back, and gold sparks spatter across her cheek and the sheets." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Never getting tired of that.\""
    "Beaming, star-dusted."
    vn_sfx "Thump."
    show cg ce_envelope onlayer cgl
    "Luna lands on the end of the bed and punts a purple-marbled envelope up at you with one foot. Glitter shakes out of it."
    "{color=#c79bff}{i}Dears Celestia and Associates. Thank you for the exquisite fireworks. But alas, lust never truly dies. Consider this a cordial invitation to round two. Dress accordingly. Yours, presently bored, Professor Nightshade.{/i}{/color}"
    ce_you "\"Does this mean I'm famous or infamous?\""
    show ce_luna smug at vn_cast_slot
    ce_luna "\"Small-time celebrity. Big-time public safety hazard.\""
    hide ce_luna
    menu:
        "The cape."
        "Keep the cape" (ending=True):
            $ ce.epilogue = "keep"
            jump ce_keep
        "Hang it up" (ending=True):
            $ ce.epilogue = "hang"
            jump ce_hang

label ce_keep:
    $ ce_morph(6)
    $ vn_enter(bg="ce_loft_stoop", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_keep_stoop")
    show cg ce_keep_stoop onlayer cgl
    "You keep the cape."
    "Your old clothes go on Pippa's cosplay-materials pile. Your hoodie goes on her hook. You live here now, in the loft with the fairy lights and the canvases and a whole wall of her drawings of you."
    "The leotard is what you wear. It scandalises the council. It does great numbers online. You pin the tails with gold star barrettes and strike a pose on the stoop while Pippa takes photo after photo."
    show cg ce_keep_door onlayer cgl
    "Pippa catches you in the doorway on your way out, still in her sleep shirt. She checks the street's at least semi-clear, then gets a hand on your ass through the leotard and squeezes, and her other hand slides round and cups your breast, thumb circling the nipple through the white."
    ce_you "\"Mm— {i}Pippa{/i}— I'm on {i}duty{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Go get 'em, star-girl. Save me some for after.\""
    "Whispering it into your neck. An old lady cackles from a window. Phones come up across the street. You kiss Pippa anyway, long and messy, her hand never leaving your tit until you break away, giggling and flushed."
    show cg ce_keep_sign onlayer cgl
    "Down the street there's a guy with a sign that says MARRY ME, CELESTIA. It's Dougie. Of course it's Dougie."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"Try not to level the block before lunch.\""
    "On your shoulder, balanced on your chest like a shelf."
    ce_you "\"Only if the bad guys ask nicely.\""
    "There's purple fog curling round the river boardwalk already. Another day. Your body hums with starlight."
    "{color=#f3c969}Luna's at the bandstand whenever there's a patrol. There's always somebody on his strings somewhere.{/color}"
    jump ce_route_return

label ce_hang:
    $ vn_enter(bg="ce_loft", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_hang_dish")
    show cg ce_hang_dish onlayer cgl
    "You fold the leotard. Gloves, boots, the gold choker on top. It all goes in Pippa's moon dish on the sill, where the light catches it in the mornings."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"You can always get it down.\""
    ce_you "\"I know.\""
    $ ce.fit = "vest_open"
    show bg ce_shop onlayer bgl
    show cg ce_hang_vest onlayer cgl
    $ vn_pass(ce_to_weekday(6, 9))
    "On Saturday you take the vest down off the break-room hook. It doesn't button. You wear it open."
    "Dougie's holding a sign by the TVs that says MARRY ME, CELESTIA. Ms. Pruitt confiscates it without breaking stride."
    show ce_pruitt verdict at vn_cast_slot
    ce_pruitt "\"Do the shifts, and I don't care.\""
    "You do the shifts. Your tails swing behind you all day, and the customers ask for you by name."
    show bg ce_stockroom onlayer bgl
    show cg ce_hang_stockroom onlayer cgl
    $ vn_until(13)
    "At lunch, Pippa turns up with coffees and drags you into the stockroom by the vest."
    ce_you "\"Pippa— I'm at {i}work{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"So be quiet.\""
    "She pushes you back against a pallet of surge protectors, gets the vest open and your top up, and her mouth on your nipple. Her hand down the front of your work trousers. Two fingers, curling. You are not quiet."
    ce_you "\"Ahh— {i}ahh{/i}— Pippa— right {i}there{/i}—\""
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Ms. Pruitt's going to hear you.\""
    ce_you "\"I don't— {i}care{/i}—\""
    "You come against the surge protectors with her fingers inside you and your hand over your own mouth, and it doesn't help at all." with vnfx("flash")
    "When you come out, Dougie's at the till, bright red, and Ms. Pruitt doesn't look up from her clipboard."
    show ce_pruitt verdict at vn_cast_slot
    ce_pruitt "\"Do the shifts.\""
    jump ce_route_return

## ---- the dark ending (Celestia Bandstand, Crown, Crown Sex, Crown After, Dark End, Stay|Home) --------------------

label ce_bandstand_dark:
    $ ce.sortie_day = vn_clock.day
    $ ce_morph(6)
    $ vn_enter(bg="ce_bandstand_dark", pc="flushed", pc_tag="ce_pc", cast=[], cg="ce_throne")
    show cg ce_throne onlayer cgl
    "The sky's a bruise. Violet threads hang off every tree like wet ribbon. The whole park stands entranced, swaying, slow and dreamy."
    "On the bandstand there's a throne of black velvet. He's on it, glowing with everything you gave him."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Celestia. You came anyway.\""
    "Warm, like you're late for dinner. You don't say anything. The leotard's on you. It always is now."
    show ce_nightshade smile at vn_cast_slot
    "He comes down the steps. Up close he's beautiful in a way that makes your knees go."
    ce_nightshade "\"You can feel it, can't you? Every desire you never said out loud.\""
    hide ce_nightshade
    show cg ce_crown_offer onlayer cgl
    "He opens his hand. A crown of black light turns over above his palm."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Be adored. Be worshipped. Let the whole town run wild, with you as its queen of pleasure.\""
    "Your nipples are so hard they throb. Your pussy's soaking the leotard. And you {i}want{/i} it."
    menu:
        "The crown."
        "Take the crown":
            $ ce.pose = "take"
        "Kneel for it":
            $ ce.pose = "kneel"
    jump ce_crown

label ce_crown:
    $ ce.dark_form = True
    $ vn_enter(bg="ce_bandstand_dark", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_crown")
    if ce.pose == "kneel":
        "You kneel on the bandstand steps. He lowers the crown onto your head like he's been waiting his whole life to."
    else:
        "You take it out of his hand and put it on yourself. He laughs, delighted."
    show cg ce_crown onlayer cgl
    "The violet runs down into your hair. The leotard goes black from the choker down. Black boots. Black gloves. You look down at yourself and moan." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Oh, {i}wow.{/i}\""
    "She's at the bottom of the steps. She came anyway too. Glasses crooked, sketchbook clutched to her chest, grinning in spite of everything."
    ce_pippa "\"Black's good on you.\""
    hide ce_pippa
    show ce_luna flat at vn_cast_slot
    ce_luna "\"I'm not watching this.\""
    "Luna's on the bandstand rail. She looks at you, and at him, and turns her back on both of you, and doesn't."
    hide ce_luna
    show cg ce_crown_lap onlayer cgl
    "Nightshade sits back on the throne and opens his coat. His cock, long and hard and pale, standing up out of the velvet."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Your first, I think. In front of all of them.\""
    "You climb into his lap. Your knees either side of his hips on the velvet. He pulls the black leotard down off your tits and takes a nipple in his mouth, cool and slow, and you moan so loud the front row of the crowd moans with you."
    ce_you "\"Ahh— Professor— {i}please{/i}—\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Please what, my star?\""
    ce_you "\"Please let me— let me have it— I want it in me— I want {i}you{/i} in me—\""
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Then take it.\""
    "He smiles against your breast. You peel the black leotard aside, and the whole entranced park sighs. You line him up. The fat head of him, right at your lips, nudging. You're shaking, and it isn't fear.\n{size=-5}{color=#ff8fa3}▸ Sink down{/color}{/size}"
    jump ce_crown_sex

label ce_crown_after:
    $ vn_enter(bg="ce_bandstand_dark", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_crown_after")
    show cg ce_crown_after onlayer cgl
    if ce_enc.partner_came:
        "He comes with a long, satisfied sigh, holding your hips down on him, and you feel every cold, bright pulse. The violet in your hair flares up like a gas flame."
    else:
        "He holds you down on him and lets you grind out the last of it, slow, his hands spanning your hips."
    "It plays back in flashes: bouncing on his throne in front of the whole park, your tits flying, his voice telling you when, and you coming every time he said so, louder every time, glad, so {i}glad{/i}, and the crowd moaning with you like a choir."
    "\"Again,\" he'd say, and you'd grind down on him and come. \"Again,\" and you'd throw your head back and scream it at the bruise-coloured sky."
    ce_you "\"Professor— {i}Professor{/i}— more— it's so {i}deep{/i}— don't stop telling me—\""
    "And he didn't. Not for a long time."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"My star.\""
    "And kisses your throat. The fog doesn't lift. It settles over the town like a warm blanket. Couples on every bench. Nobody in a hurry to go home.\n{size=-5}{color=#ff8fa3}▸ Climb off the throne{/color}{/size}"
    jump ce_dark_end

label ce_dark_end:
    $ ce_rung(6)
    $ ce.ending = "dark"
    $ ce.fit = "casual"
    $ ce_demorph(6)
    $ ce.dark_hair = True
    $ ce.done = True
    $ achievement.grant("Black's Good on You")
    $ vn_enter(bg="ce_bandstand_dark", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_dark_end")
    show cg ce_dark_end onlayer cgl
    "The leotard lets go of you, and you're on the bandstand steps in your own clothes. The violet stays. Your tails are the colour of his fog now, and your eyes in the dark glass are bright and glad."
    "The park hums. The whole town hums. Nobody's hurting. Everybody's just... wanting, out loud, and getting it."
    show ce_luna deadpan at vn_cast_slot
    ce_luna "\"I'm still here. Somebody has to be.\""
    "Still on the rail with her back to you, to the trees."
    show ce_pippa soft at vn_cast_slot
    "Pippa sits down next to you on the step and bumps your shoulder with hers."
    ce_pippa "\"Are you okay?\""
    ce_you "\"Better than okay.\""
    "You mean it. You laugh, and it comes out a little bit his."
    hide ce_pippa
    menu:
        "Whose."
        "Stay his" (ending=True):
            $ ce.epilogue = "stay"
            jump ce_stay
        "Go home to Pippa" (ending=True):
            $ ce.epilogue = "home"
            jump ce_home

label ce_stay:
    $ ce_morph(6, dark=True)
    $ vn_enter(bg="ce_bandstand_dark", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_stay_evening")
    show cg ce_stay_evening onlayer cgl
    "You stay his."
    "The park stays violet. Velvet on the bandstand where the bunting used to be. Every evening the town drifts in to watch you, his star, in your black leotard, and every evening he tells you when. You're loud about it. You're {i}so{/i} happy about it."
    show cg ce_stay_steps onlayer cgl
    "Some nights it's his throne. Some nights it's the steps, on your knees, his hand in your violet tails, the whole lawn watching you take him in your mouth and moan round him like it's the best thing you've ever tasted. Some nights he just sits back and lets the fog have you: his puppets' hands from every side, on your tits, your ass, your pussy, and you laughing and coming and coming."
    show ce_nightshade bored at vn_cast_slot
    ce_nightshade "\"Again.\""
    "Every time."
    ce_you "\"Yes, Professor.\""
    "Every time, and you mean it."
    show cg ce_stay_sketch onlayer cgl
    "Pippa comes most nights with her sketchbook and draws you, mid-moan, from the front row. She's selling prints."
    "Luna stays. She never says why. She just sits on the rail with her back to it and her ears flat, and won't leave town, and every so often you catch her looking at you like she's waiting for something."
    jump ce_route_return

label ce_home:
    $ ce.fit = "nude"
    $ vn_enter(bg="ce_loft_night", pc="glad", pc_tag="ce_pc", cast=[], cg="ce_home")
    show cg ce_home onlayer cgl
    "You go home to Pippa. The loft, the fairy lights, her bed. She pulls your clothes off and looks at your violet tails on her pillow for a long time."
    "Then she slides her fingers inside you, slow, and watches your face."
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Are you still you?\""
    ce_you "\"{i}Louder.{/i}\""
    "You gasp it, and she laughs, and curls them, and you are."
    ce_you "\"Ahh— {i}ahh{/i}— Pippa— more— {i}more{/i}—\""
    show cg ce_home_cum onlayer cgl
    "Another finger. Her thumb on your clit. Her mouth on your nipple, sucking hard. You grind down on her hand with your violet tails all over her pillow and moan at her ceiling like you're still on the bandstand, and she grins against your breast." with vnfx("flash")
    show ce_pippa grin at vn_cast_slot
    ce_pippa "\"Yeah. Still you.\""
    show cg ce_home_crown onlayer cgl
    "In the morning there's violet in the corners of every window in town, and you live in the loft now, and you have a sorcerer's crown in Pippa's moon dish on the sill. You wear it some nights. She likes it when you do."
    jump ce_route_return
