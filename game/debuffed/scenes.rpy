## THE STORY: chapters 3-5 (PLAN.md). Floor 3, Morwen (DRAINED: a level each time he comes; muscle and height); floor 4,
## Holda (MILK-DRUNK: breasts); floor 5, Sessaly (BOUND: waist cinched, hips and ass). Same shape every day: the morning's
## waystone, the floor, the ailment (first choice), the scene (second choice), his one hit, the night's waystone and the change.

## ---- 2. Wednesday: floor three, Morwen ------------------------------------------------------------------------------

label dbf_wednesday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_morning_two")
    "The dress has mended again."
    "It's let itself out at the hips overnight, and taken itself in at the waist, and the bodice sits differently on your swollen nipples: you can feel them rub with every breath."
    "{color=#ffd36b}STATUS: CHARMED. SOFTENED. PARALYSED.{/color}"
    "Three. You've never had three of anything. You've never had {i}one.{/i}"
    dbf_you "\"Doesn't matter. Up. Kill the succubus, and all of it comes off. That's how curses work.\""
    "You're fairly sure that's how curses work."
    $ vn_set_time(10, 30)
    $ vn_enter(bg="dbf_crypt", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_morwen", "smirk")], cg="dbf_morwen_wakes")
    "Floor three is cold. A crypt: low vaults, grey stone, candles that burn without melting. In the middle of it, on a carved stone bed, a woman sits up."
    "Grey-pale skin, long silver hair, a white silk gown that clings to a long, full body. Her eyes are pale as frost. She looks you over the way a woman looks over a menu."
    dbf_morwen "\"Another one. Hello. I'm Morwen. Do you know what I do, adventurer?\""
    dbf_you "\"You drain levels. I've read the bestiary.\""
    dbf_morwen "\"Then you know not to let me touch you.\""
    "Your feet are already walking you to her. The charm hums, warm, in your chest. She raises one cool grey hand."
    menu:
        "Her hand's coming for your face."
        "Ward off her hand":
            "You bring your rapier up between you, guard high, perfect form, and your arm goes heavy as lead the moment her fingertips brush your wrist. The paralysis."
            "Your own ailment, working for her."
            "Her hand slides past your guard and cups your cheek."
            $ dbf.wary += 1
        "Let her cold hand land":
            "You want to know. Is it like ice? Is it like a draught? Does it hurt? You've read about it all your life. Just this once, you want to {i}feel{/i} it."
            "You let her cup your cheek."
            $ dbf.curious += 1
    "It doesn't hurt. It's cold, and then it isn't. It's like something being poured out of you, warm and slow, into her palm."
    "{color=#ffd36b}LEVEL 40. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED.{/color}"
    dbf_morwen "\"There's a way to do this faster. Every time you come, I take a level. Shall we?\""
    show cg dbf_cold_hands onlayer cgl
    "She draws you down onto the stone bed beside her and lifts your skirt, and her cool hand wraps round your cock and strokes, slow and expert, and her other hand slides under you and two cold fingers press into your arse."
    vn_sfx "Shiko. Shiko. Nuchu."
    dbf_you "\"Ahh— cold— it's— ahh♡— oh, that's good, that's {i}good—\""
    menu:
        "You can feel it building."
        "Clench and hold it back":
            "You clench everything. You've got discipline; you've got three years of it."
            "You hold it back, and back, gasping, shaking, and she watches you with frank interest and doesn't hurry at all."
            dbf_morwen "\"Mm. Stubborn. I have all the time in the world.\""
            "It takes her an hour. It takes her an hour, and when it comes it's twice as hard for the wait."
            $ dbf.fought += 1
        "Let her take the level":
            "It's only one level. You've got forty. And her hand is so good."
            dbf_morwen "\"Sensible.\""
            $ dbf.gave += 1
    dbf_you "\"Ahh♡— ahh— AHHH♡—!\"" with vnfx("flash", "shake")
    "{color=#ffd36b}LEVEL 39.{/color}"
    show cg dbf_level_drain onlayer cgl
    "And again. Her mouth, this time: cold lips sliding down your cock, her cold tongue, the fingers in your arse curling. And again. And again."
    vn_sfx "Juru. Juru. Chuu."
    "{color=#ffd36b}LEVEL 37. LEVEL 36. LEVEL 35.{/color}"
    "{color=#ff5fb8}Every level she takes, she takes more of the body you built with it. The hard muscle in your sword arm softens and thins until your arm is slender and smooth.{/color}"
    "{color=#ff5fb8}Your shoulders draw in, narrower. The muscle in your belly and thighs melts into soft flesh.{/color}"
    "{color=#ff5fb8}And you sink, a level at a time. Your feet on the stone feel further away and then nearer.{/color}"
    "{color=#ff5fb8}When it stops, you're seven centimetres shorter than you were this morning: a hundred and sixty-three, an ordinary woman's height.{/color}"
    dbf_you "\"Ahh♡— again— I'm— AHHHHH♡—!\"" with vnfx("flash", "shake")
    "{color=#ffd36b}LEVEL 34.{/color}"
    dbf_morwen "\"That will do. Mireille wants you soft, not empty.\""
    "She lies back on her stone bed and closes her eyes. You pick up your rapier. It's heavy now: really heavy, two-handed heavy."
    "You drive it down into the stone beside her, and she sighs, sounding very contented, and falls asleep."
    "Three down."
    $ dbf_grow(3)
    $ dbf.fit = "torn"
    $ vn_set_time(21, 0)
    $ vn_enter(bg="dbf_waystone", pc="shocked", pc_tag="dbf_pc", cast=[], cg="dbf_third_waystone")
    "The third waystone is taller than you. The others weren't."
    "{color=#ff5fb8}A hundred and sixty-three centimetres. Slender arms with not a cord of muscle in them. Narrow, rounded shoulders. A soft belly. Soft thighs.{/color}"
    "{color=#ff5fb8}Your full pink lips, your puffy nipples, your smooth glowing skin, and that new curve at the hips, all on a smaller, softer frame that looks like it's never swung a sword in its life.{/color}"
    "{color=#ff5fb8}Your ash-silver hair has grown to your shoulders.{/color}"
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED.{/color}"
    dbf_you "\"Seven levels. Seven {i}centimetres.{/i} That's— I'll get them back. Levels come back. It's just grinding.\""
    "You say it to the waystone twice, to be sure."
    call dbf_cut(7, 1, "Thursday. Floor four.")
    jump dbf_thursday

## ---- 3. Thursday: floor four, Holda ---------------------------------------------------------------------------------

label dbf_thursday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_morning_three")
    "The dress has shrunk itself to fit you overnight. The sleeves end at your slender wrists. The hem sits higher on your soft thighs. The bodice hugs a body you're still learning."
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED.{/color}"
    "You carry your rapier in both hands up the stairs. The charm hums you up them faster than you'd go."
    $ vn_set_time(11, 0)
    $ vn_enter(bg="dbf_dairy", pc="curious", pc_tag="dbf_pc", cast=[("dbf_holda", "smirk")], cg="dbf_holda_greets")
    "Floor four smells of hay and warm milk."
    "A great barn of a hall under a painted summer sky, straw on the floor, churns in a row along one wall, and in the middle of it all a woman rising from a bed of straw with a sleepy smile."
    "Tall. Curving horns, soft cow's ears, a long tufted tail. Thick thighs, wide hips."
    "And breasts: enormous, heavy, round, straining a loose milkmaid's blouse that's lost the battle at the top."
    dbf_holda "\"Oh, you poor thing, look at you. Three floors already and not a bite to eat. I'm Holda. Come here, love, and have some milk.\""
    "She lifts a brimming wooden cup. Your feet carry you to it."
    show cg dbf_the_cup onlayer cgl
    "She tips it to your lips before you've decided anything. Warm, sweet, creamy, and so rich it's almost heady."
    menu:
        "Your mouth's full of it."
        "Spit it out":
            "You spit it out across the straw. Most of it. A mouthful went down before you caught yourself, warm, and it's spreading through your chest like brandy."
            $ dbf.wary += 1
        "Swallow":
            "It's delicious. It's the best thing you've ever tasted. You swallow, and you want to know what the second mouthful tastes like, so you drink that too."
            $ dbf.curious += 1
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK.{/color}"
    "The hall tilts, warm and pleasant. You're giggling. You don't know why. Your rapier's on the straw; you don't remember putting it down."
    dbf_holda "\"That's my milk. Makes everyone so happy. Now come and have some from the source.\""
    show cg dbf_nursing onlayer cgl
    "She sits you in her lap like a sack of flour and tugs her blouse down, and one heavy breast swings free, and she guides your mouth onto the nipple. You suckle."
    "You can't help it. Warm milk floods your mouth, sweet and endless, and her hand slides under your skirt and strokes your cock, unhurried, in time with your swallowing."
    vn_sfx "Chuu. Chuu. Gokun. Shiko. Shiko."
    dbf_you "\"Mmh♡— mmh— hahh— it's so— it's so {i}warm—\""
    "{color=#ff5fb8}It goes straight to your chest. Every swallow, a warm swelling under your puffy nipples, under your bodice. You can feel the dress's laces creak. Then pop.{/color}"
    "{color=#ff5fb8}Then two soft round breasts rising under them, then bigger, filling your hands when you put your hands there, then overflowing them: full, heavy, bouncing when Holda jogs her knee.{/color}"
    dbf_holda "\"There we are. Look how lovely you've grown. Now let me give you a proper cuddle.\""
    menu:
        "She's laying you back in the straw."
        "Push her off":
            "You push at her chest with both slender hands. It's like pushing a warm feather bed. She laughs, delighted, and settles down onto you anyway."
            $ dbf.fought += 1
        "Sink into her":
            "You sink into her. Warm, soft, smelling of milk. Why would anyone fight this? You can't remember why."
            $ dbf.gave += 1
    show cg dbf_holda_paizuri onlayer cgl
    "She kneels over your hips and folds those vast breasts round your cock, and it vanishes between them, and she squeezes them together with both hands and works them up and down, slick with her own milk, warm and soft and overwhelming."
    "Your own new breasts bounce on your chest with every stroke."
    vn_sfx "Tapun. Tapun. Nuchu. Nuchu."
    dbf_you "\"Ahh♡— Holda— Holda— so soft— I'm— AHHHHH♡—!\"" with vnfx("flash", "shake")
    "You come between her breasts, and she laughs and squeezes until you're dry and then kisses your forehead."
    dbf_holda "\"Good. Off you pop. Sessaly's next, and she'll want you nice and cuddly.\""
    "You get your rapier. You stagger. You poke her once in the side as you go past, and she says {i}oof!{/i} very kindly and rolls over in the straw and pretends to faint."
    "Four down. You're fairly sure that one counted."
    $ dbf_grow(4)
    $ dbf.fit = "torn"
    $ vn_set_time(21, 0)
    $ vn_enter(bg="dbf_waystone", pc="dazed", pc_tag="dbf_pc", cast=[], cg="dbf_fourth_waystone")
    "The milk wears off at sunset, mostly. The giggle doesn't, quite."
    "{color=#ff5fb8}Breasts.{/color}"
    "{color=#ff5fb8}You have breasts: big, round, heavy, sitting high and full on your slender frame, swaying when you move, your puffy nipples crowning them like they were always meant to be there.{/color}"
    "{color=#ff5fb8}You cup them. They fill your hands and spill out between your fingers. Your hair's grown past your shoulders, ash-silver, brushing the tops of them.{/color}"
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK.{/color}"
    dbf_you "\"...They're heavy. Nobody ever {i}said{/i} they were heavy.\""
    "You fall asleep with your hands still on them."
    call dbf_cut(7, 1, "Friday. Floor five.")
    jump dbf_friday

## ---- 4. Friday: floor five, Sessaly ---------------------------------------------------------------------------------

label dbf_friday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_morning_four")
    "The dress has given itself a new bodice in the night: cups, boned and lifted, cut low. The enchantment has opinions."
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK.{/color}"
    "Five. You stop counting them at the waystone and start counting floors instead. Three to go. Then you kill her and it all comes off."
    $ vn_set_time(10, 0)
    $ vn_enter(bg="dbf_baths", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_sessaly", "smirk")], cg="dbf_sessaly_coils")
    "Floor five is a bathhouse: white marble, green-tiled pools, steam rolling over the water."
    "And coiled round the biggest pool, a lamia: a woman to the hips, bare and lush and lazily beautiful, and below the hips a tail, green-scaled, thick as your waist and longer than the room."
    dbf_sessaly "\"Ssso. Holda's been feeding you. You look delicious. I'm Sessaly.\""
    "Her eyes are gold with slit pupils. She smiles slowly, and the tail starts to move."
    "Your feet start to walk toward her. The tail sweeps round the floor toward your feet."
    menu:
        "The tail's coming at your ankles."
        "Leap the tail":
            "You leap it. Cleanly, the old way, rapier high."
            "You land, and your new breasts land a second after you, and the shift of weight throws you sideways, and the tail catches you on the way down."
            $ dbf.wary += 1
        "Let it wrap you":
            "You've always wondered what it feels like, a lamia's coils. Everybody has. You stand still and let it come."
            $ dbf.curious += 1
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND.{/color}"
    show cg dbf_bound onlayer cgl
    "Her coils wrap you from the knees to under your breasts, warm and smooth and dry, loop on loop, and lift you off the floor, and draw you to her."
    "She holds your face in her hands and studies it."
    dbf_sessaly "\"Pretty. Now let's give you a waisst.\""
    "The coils squeeze."
    vn_sfx "Gyuu. Gyuu. Gyuuu."
    menu:
        "The coils are tightening round your middle."
        "Brace against her":
            "You brace. You push out against her with everything, every muscle you've got left. You haven't got many. She tightens, patient, a breath at a time, and waits for you to run out."
            $ dbf.fought += 1
        "Breathe out for her":
            "You breathe out. All the way. And she takes up the slack, smooth and sure, and it feels like being held. It feels like being hugged by the whole world."
            $ dbf.gave += 1
    "{color=#ff5fb8}Your waist goes in under her coils like a corset drawn tight, narrower, narrower.{/color}"
    "{color=#ff5fb8}And everything she squeezes out of it goes somewhere: down, into your hips, which spread out wide and round below the coils, and into your arse, which swells behind you, fuller, rounder, bigger, until it's pushing out against her scales.{/color}"
    "{color=#ff5fb8}Your thighs thicken, soft and heavy, pressing together.{/color}"
    show cg dbf_tail_tip onlayer cgl
    "Then the tip of her tail, slim and slick, slides up between your new cheeks and into your arse, and starts to thrust, and her hand wraps round your cock below the coils."
    vn_sfx "Nuchu. Nuchu. Pan. Pan. Shiko."
    dbf_you "\"Ahh♡— ahh— so tight— everywhere— Sessaly— ahh♡— AHHHHH♡—!\"" with vnfx("flash", "shake")
    "You come with every coil round you squeezing in time, and it goes on and on, and she holds you through all of it with her cheek on your hair."
    dbf_sessaly "\"There. Corvina next. She'll want to hear you sing.\""
    "She lowers you to the tiles and uncoils, loop by loop."
    "You get your rapier and slap the flat of it hard across her tail on the way to the stairs, and she hisses, laughing, and slides under the water."
    "Five down."
    $ dbf_grow(5)
    $ dbf.fit = "torn"
    $ vn_set_time(21, 30)
    $ vn_enter(bg="dbf_waystone", pc="dazed", pc_tag="dbf_pc", cast=[], cg="dbf_fifth_waystone")
    "You look over your shoulder at the waystone and stare."
    "{color=#ff5fb8}A waist you could nearly close your own two hands round.{/color}"
    "{color=#ff5fb8}And under it, hips wide and round as a vase, and an arse that's big now, truly big, two full soft globes that sway when you shift your weight and shiver when you breathe.{/color}"
    "{color=#ff5fb8}Thick soft thighs that touch all the way down. Big round breasts above. Ash-silver hair to the middle of your back.{/color}"
    "{color=#ff5fb8}A body made of curves, every one of them pressed into you by something that wanted you that way.{/color}"
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND.{/color}"
    "The squeeze is still there, ghostly, round your middle. You can't stand straight without your hips swaying out to one side."
    dbf_you "\"Two more floors. Two more, and I kill her, and it all comes off.\""
    "You don't say it to the waystone twice tonight. You find you don't want to hear what it sounds like."
    call dbf_cut(7, 1, "Saturday. Floor six.")
    jump dbf_saturday
