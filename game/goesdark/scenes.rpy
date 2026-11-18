## THE STORY: days 4-7 (PLAN.md). Seiya taken, the storming and the reveal; the castle and the rules; the pit; Rasetsu's
## barracks. Seiya's fire is in the lantern from Friday: every orgasm in costume burns it lower (the lantern rows darken
## with gdk_grow).

## ---- 4. Thursday: the shadow castle --------------------------------------------------------------------------------------

label gdk_taken:
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_flat", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_pirika", "worried")], cg="gdk_green_letter")
    "Seiya doesn't answer his phone on Thursday. Not at lunch, not at six, not at seven. It just rings out."
    "At half past seven a letter slides under your door on its own. It's black paper, and the writing on it is a flame: thin green fire that doesn't burn the page."
    "{i}We have your friend. The castle over the river. Midnight. Come alone, lantern. — The Kurayami Society.{/i}"
    gdk_pirika "\"The shadow castle. It only comes up at night, over the Sumida, where the lanterns can't reach. Akari, it's a {i}trap.{/i}\""
    gdk_you "\"It's {i}Seiya.\"{/i}"
    $ vn_set_time(23, 55)
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_castle_gate", pc="stern", pc_tag="gdk_pc", cast=[("gdk_grunt", "leer")], cg="gdk_storming")
    "At five to midnight you're on the riverbank in silk and heels with your lantern lit, and the castle's hanging over the black water as if it had always been there."
    "It's a Japanese keep, five roofs high, the colour of soot. Green fire burns where the lamps should be."
    "The bridge to it is packed with grunts: fifty fox masks, oni masks, happi coats, all turning to look at you at once."
    gdk_grunt "\"She came! She actually came! Lads, the light's here!\""
    menu:
        "Fifty masks between you and the gate."
        "Fight through them":
            "You go through them like a firework, swinging the lantern, knocking masks flying. You get halfway across the bridge before there are too many hands."
            $ gdk.fought += 1
        "Let them have you":
            "You stop at the start of the bridge and lift your chin. If they want a taste, they'll have to take you to the gate to get it."
            $ gdk.gave += 1
    show cg gdk_bridge_hands onlayer cgl
    "Hands everywhere. They lift you over their heads and pass you along the bridge like a festival shrine, all of them groping you at once."
    "Hands in your sleeves, squeezing your breasts. A mouth on each nipple as your collar's tugged down. Fingers up under the split skirt, two, three, pumping into you."
    "Somebody sucks your toes through the thigh-highs. Somebody's tongue gets between your legs while you're held up in the air, and stays there."
    gdk_akari "\"Put me— put me DOWN— ohh♡— not there— not ALL of you— ahh♡— AHH♡—!\"" with vnfx("flash", "shake")
    "You come over their heads, and the lantern flares and knocks a ring of them flat. The rest keep passing you along. You come again at the gate, and the gate opens."
    $ vn_enter(bg="gdk_throne", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_reveal")
    "They tip you out onto black tatami at the foot of a dais."
    "Up on the throne, a man sits with one leg crossed over the other. He wears a black haori patterned with green flames."
    "Two black horns curl back from his hair, which never stays where he puts it. His eyes are lit green, and he's grinning like he knows something about you."
    gdk_lord "\"Hello, Kaoru. You came the long way.\""
    gdk_akari "\"...Seiya?\""
    gdk_lord "\"Lord of the Kurayami. Has been for, oh, a few centuries. The warehouse was a hobby.\" He stands up and comes down the steps."
    gdk_lord "\"You really never wondered why I never had a day job?\""
    menu:
        "Your best friend is standing over you with horns."
        "Hit him":
            "You swing the lantern at his head with everything you've got. He catches the pole in one hand, and the flame bends towards him as though it's pleased to see him."
            $ gdk.fought += 1
        "Ask him why":
            gdk_akari "\"Why? Why would you— three {i}years—\"{/i}"
            gdk_lord "\"Because the Society needed a light, and I wanted it to be you. I told you to go home through the lanterns. You always listen to me.\""
            $ gdk.gave += 1
    "He crouches and touches the brass clasp on your obi, and the costume lets go of you."
    vn_sfx "Kachi."
    "Silk turns back to shirt and jeans. You're on his floor as Kaoru, and he scoops you up, and you're too stunned to stop him."
    gdk_lord "\"Bedtime. We'll talk tomorrow.\""
    $ vn_set_time(23, 59)
    $ gdk_grow(3)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bedchamber", pc="dazed", pc_tag="gdk_pc", cast=[], cg="gdk_black_mirror")
    "His bedchamber has a mirror of polished black stone as tall as the wall. He sets you down in front of it and leaves you there."
    "{color=#ff5fb8}Your jeans won't do up any more. Your hips have spread, wide and soft, and your arse has rounded out so much that the denim's split at the seat.{/color}"
    "{color=#ff5fb8}Your thighs press together when you stand. Your hair falls to your shoulders, soft and brown, and frames a face that's prettier than it was this morning.{/color}"
    "Your cock's still there, pressing at the ruined jeans. It's the only thing in the mirror that's still entirely yours."
    call gdk_cut(21, 1, "Friday.")
    jump gdk_castle

## ---- 5. Friday: the rules -----------------------------------------------------------------------------------------------

label gdk_castle:
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bedchamber", pc="stern", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_rules")
    "You spend all of Friday in a room with no door. Food comes on lacquered trays carried by grunts who won't meet your eyes. Your phone has no signal. Pirika is nowhere."
    "At nine o'clock a door appears, and Seiya comes in through it."
    gdk_lord "\"Here's how it goes. I'm not going to lock you up. Doors here open for whoever I like, and I'll like you more every day.\""
    "He takes your lantern from the stand by the bed, where you didn't put it, and opens its paper door. He breathes on the flame, gently, and green creeps into it at the edges."
    gdk_lord "\"Your light burns my yokai. Fine. But it's burning on my fire now, too. Every time I make you come, it burns a bit lower. When it goes out, it lights again with mine.\""
    gdk_lord "\"And then you're my yokai, Kaoru. Mine. You'll never come out of costume again.\""
    gdk_you "\"And if I get out first?\""
    gdk_lord "\"Then you get out.\" He shrugs, smiling. \"Light the way, Akari.\""
    "You didn't say it. He did. The lantern does it anyway."
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_bedchamber", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_lord", "hungry")], cg="gdk_jade")
    "{color=#ff5fb8}The change pours through you, and it's different this time. Your hair spills down mint and darkens as you watch, to a deep jade green.{/color}"
    "{color=#ff5fb8}Your breasts swell bigger than before, so heavy that the indigo silk strains across them. Down at the hems, the cream of your sleeves has gone ash grey.{/color}"
    gdk_lord "\"There she is.\""
    show cg gdk_first_night onlayer cgl
    "He lays you back on black silk sheets and takes his time. He unwraps the obi bow, and parts the silk, and kisses your breasts until you're squirming."
    "He slides his fingers into you and crooks them, as though he's known your body for years. In a way he has."
    "When he pushes inside, he's bigger than the yokai, bigger than you'd ever have guessed, and his cock is hot all the way through."
    menu:
        "You can feel it building already."
        "Hold it in":
            "You grit your teeth and fist the sheets and hold it back, and back, and back, while he fucks you slow and deep and laughs softly against your neck."
            vn_sfx "Nuchu... nuchu..."
            gdk_lord "\"Go on. Hold it. I've got all night.\""
            $ gdk.fought += 1
        "Let it come":
            "You don't fight it. You wrap your legs round his waist and let it build."
            $ gdk.gave += 1
    vn_sfx "Pan. Pan. Pan."
    gdk_akari "\"Seiya— Seiya♡— I can't— it's too— ahh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come around him with your back arched off the bed. The lantern on the stand flares up white, then sinks."
    "It's lower than it was. A thin green thread runs round the edge of the flame."
    gdk_lord "\"One,\" he murmurs, and keeps going."
    call gdk_cut(6, 1, "Saturday.")
    jump gdk_pit

## ---- 6. Saturday: the pit ------------------------------------------------------------------------------------------------

label gdk_pit:
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_well", pc="stern", pc_tag="gdk_pc", cast=[], cg="gdk_well_down")
    "At dawn he's asleep, with one arm over his face. You get up, quietly, still in costume, and the door is there."
    "The castle's quiet in the mornings. You follow the river smell down and down, through cellars and store-rooms, to a stone well in the floor of the lowest one."
    "You can hear water at the bottom. The river. The way out."
    "You climb down. At the bottom, it isn't the river."
    show cg gdk_pit onlayer cgl
    "It's a pit, warm and dark, and it's full of tentacles: soft, slick, ink-black arms that wake up all at once, as if they'd been waiting for you."
    "They wind round your ankles and up your thighs. They slide inside your sleeves."
    vn_sfx "Nyuru. Nyururu."
    "Two of them peel the silk off your breasts and coil round each one and squeeze, and another drapes itself across your mouth, sweet-tasting and slippery."
    menu:
        "The well's mouth is a grey circle far above you."
        "Climb":
            "You get a heel in a gap in the stones, then a hand, then another. You get a whole body-length up the wall before they pull you back down into them, slowly, like a tide."
            $ gdk.fought += 1
        "Stop climbing":
            "You let go of the wall and fall back into them, and they catch you."
            $ gdk.gave += 1
    "One of them pushes inside you, and then another one alongside it, stretching you wide. A third finds your arse and squirms in, and then they all move together."
    vn_sfx "Nuchu. Gupo. Nuchu."
    gdk_akari "\"Ahh♡— no— not all— not ALL of them— ohhh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "The lantern flares. They don't let go. They make you come again, and again. Each time the light's weaker, until on the fourth or fifth time there's no flare at all."
    "Then the silk melts away like sugar in water."
    "You come out of costume in the dark, in the middle of the pit, as Kaoru. The tentacles pause, curious, as though they've never seen a cock before."
    "Then they lose interest and lower you gently onto the stones."
    "Footsteps on the stair above. A green light coming down."
    $ vn_set_time(9, 0)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bath", pc="flustered", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_bath_seiya")
    "He carries you up to a stone bath full of hot water and washes the pit off you himself. He's laughing at you, gently."
    gdk_lord "\"The well. Everyone tries the well.\""
    gdk_you "\"Shut up.\""
    "He doesn't. He pulls you onto his lap in the water, with your back to his chest, and his cock slides between your round cheeks."
    "You groan, because it's been a whole night, and your body wants it."
    vn_sfx "Zupu. Chapu. Chapu."
    gdk_you "\"In the bath— you're doing this in the {i}bath— ahh♡— Seiya♡—\""
    "He fucks you slowly, bouncing you on his lap. The hot water slaps over the stone edge."
    "He strokes your cock under the water in time with his thrusts, and he whispers in your ear."
    gdk_lord "\"You know what I like best? You don't even have to be Akari. Every bit of her you bring back, I get to keep. Look at you.\""
    gdk_you "\"I'm— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    $ vn_set_time(23, 50)
    $ gdk_grow(4)
    $ vn_enter(bg="gdk_bedchamber", pc="dazed", pc_tag="gdk_pc", cast=[], cg="gdk_mirror_four")
    "That night the black mirror shows you the rest of what the pit left behind."
    "{color=#ff5fb8}Your chest has gone soft. Not breasts, but plump and puffy, with nipples swollen and pink and sensitive to the air. Your waist has drawn in tight above the wide new hips. Your hair's past your shoulders, brown and glossy and heavy as silk.{/color}"
    "In the lantern on its stand, the flame's down by a third. Its edges are green all the way round."
    call gdk_cut(13, 1, "Sunday.")
    jump gdk_barracks

## ---- 7. Sunday: the barracks ----------------------------------------------------------------------------------------------

label gdk_barracks:
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_barracks", pc="stern", pc_tag="gdk_pc", cast=[("gdk_rasetsu", "grin"), ("gdk_grunt", "grin")], cg="gdk_barracks_door")
    "Sunday afternoon you try the other way: up, not down. Over the roofs to the outer wall, through the barracks."
    "{color=#ff5fb8}The change hits you in the corridor, and it's heavier again. Your hair comes down deep pine green now, nearly black in the shadows. The cream silk is ash grey all over. The persimmon of your obi has gone dull and greenish, like old copper.{/color}"
    "The barracks are a long hall of bunks, and every bunk has a grunt on it."
    "Rasetsu is at the far end on a stack of cushions with her club across her knees and a sake bottle in one hand. Her face lights up."
    gdk_rasetsu "\"Lantern! Come to visit?\""
    menu:
        "Rasetsu's between you and the wall."
        "Fight Rasetsu":
            "You go for her with the lantern. She lets you hit her twice, for fun, and then she takes it off you and hangs it on a hook on the wall, still burning, where you can see it."
            $ gdk.fought += 1
        "Ask for her":
            "You look at her: the red skin, the horns, the heavy weight swinging under the tiger-skin. You remember the roof."
            gdk_akari "\"...I came for you.\""
            gdk_rasetsu "\"Ha! The lord's going to be so jealous.\""
            $ gdk.gave += 1
    show cg gdk_barracks_spit onlayer cgl
    "She lays you face up across the cushions with your head hanging off the edge. She spreads your thighs and slides into you in one long, slow, enormous push."
    "You're still yelling about it when a grunt in a fox mask steps up at your head and gives your mouth something to do."
    "Then the rest of them come down off the bunks."
    vn_sfx "Pan. Pan. Juru. Pan."
    "Hands on your breasts. Hands on your thighs. Cocks pressed into each of your palms. Rasetsu fucks you so hard the cushions creep across the floor."
    "The grunt in your throat groans and pulls out and paints your face, and another one takes his place."
    gdk_akari "\"Mmh♡— more— Rasetsu— harder— ahh♡— ohh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "On the hook, the lantern flares and sinks. And again. And again. Every time Rasetsu fills you, every time the hall cheers, the flame drops down its wick."
    $ vn_set_time(23, 30)
    $ gdk_grow(5)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bedchamber", pc="dazed", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_mirror_five")
    "Seiya collects you from the barracks himself, around midnight, and carries you up wrapped in his haori."
    "When the costume finally lets go in front of the black mirror, you hardly recognise yourself."
    "{color=#ff5fb8}You're all hips and arse now: a huge, soft, heart-shaped arse that sways when you breathe, and thick thighs that fill the mirror.{/color}"
    "{color=#ff5fb8}Your waist is cinched in so tightly between them that his two hands nearly meet round it. Your chest is soft and puffy, your lips full, your lashes long.{/color}"
    "{color=#ff5fb8}Your brown hair falls to the middle of your back.{/color}"
    "{color=#ff5fb8}Between your legs your cock hangs where it always has, and it looks smaller than ever under all that body.{/color}"
    gdk_lord "\"Gorgeous.\" He kisses your shoulder. \"Tomorrow you're going home.\""
    gdk_you "\"...What?\""
    gdk_lord "\"For a day. Go to work. See your flat. See the firefly; she's been sitting on your sugar bowl all week, glowing at the door.\" He fastens something round your throat: a black silk collar with a brass lantern charm the size of a fingertip."
    gdk_lord "\"Wear this. Under your shirt. Come back when you want to.\""
    gdk_you "\"And if I don't?\""
    gdk_lord "\"Then you don't,\" he says. He doesn't sound worried at all."
    call gdk_cut(7, 1, "Monday.")
    jump gdk_parole
