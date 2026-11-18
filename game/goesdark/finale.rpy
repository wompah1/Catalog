## THE STORY: day 9 (PLAN.md). The last flicker, the gate left open, the Night Parade gathering; the ending choice
## (marked as endings): "One flicker left" or "Lit by his fire" (the yokai, row b6). The closing thought follows the
## fought / gave counters (gdk_thought_line).

label gdk_gate:
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_castle_roof", pc="stern", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_last_flicker")
    "Tuesday night he takes you up to the top roof of the castle. Below you the whole city is lit up for the last night of the festival, a river of orange lanterns winding up the hill."
    "He says it for you again: \"Light the way.\""
    "{color=#ff5fb8}The change comes slow and heavy and sweet. Your hair pours down the darkest pine green, black until the light catches it.{/color}"
    "{color=#ff5fb8}Your breasts swell to their fullest yet, enormous and soft, spilling over the top of the indigo.{/color}"
    "{color=#ff5fb8}The obi has gone the green of a ghost-fire, and the ash-grey silk has darkened almost to charcoal.{/color}"
    "In the clasp at your waist, the flame is down to a single flicker. Green all over, with a pinprick of orange at its heart."
    "Down in the courtyard the yokai are gathering."
    "Grunts with fox masks and paper lanterns, Rasetsu with her club, the shadow yokai, the things from the pit, and a hundred others you haven't met: one-eyed, long-necked, many-armed."
    "They're lined up in a long procession at the gate."
    gdk_lord "\"The Night Parade. Once a year. We go down through the festival and every lantern on the street goes out as we pass.\" He's behind you, warm, his chin on your shoulder."
    gdk_lord "\"Somebody has to carry a light at the front. That's always been the job.\""
    gdk_akari "\"That's what you wanted me for.\""
    gdk_lord "\"I wanted you because you're you. The job's just a bonus.\" He nods down at the gate. It's wide open."
    gdk_lord "Beyond it the bridge runs over the black river to the festival street, and the shrine at the top. \"The gate stays open till dawn. You can walk out of it right now. I won't stop you.\""
    gdk_akari "\"And if I don't?\""
    gdk_lord "\"Then I make you come one more time.\""
    "His hand slides round your waist and rests just over the clasp, over the last flicker. You can feel its warmth through his palm."
    menu:
        "One flicker left. The gate is open."
        "Run for the gate" (ending=True):
            jump gdk_end_flicker
        "Stay by his fire" (ending=True):
            jump gdk_end_lit

label gdk_thought_line:
    if gdk.gave > gdk.fought:
        "You stopped fighting it a long time ago, somewhere between the festival and the barracks. You don't remember why you ever started."
    elif gdk.fought > gdk.gave:
        "You fought every step of the way. You're still not sure who won. Some nights you think it was the same thing all along."
    else:
        "Some nights you fought and some nights you didn't. The lantern burned the same either way."
    return

label gdk_end_flicker:
    $ vn_set_time(4, 50)
    $ vn_enter(bg="gdk_castle_gate", pc="stern", pc_tag="gdk_pc", cast=[], cg="gdk_end_bridge")
    "You run."
    "Out from under his hand, down the roofs in your heels, through the courtyard where the whole Parade turns its masks to watch you, and out of the open gate onto the bridge."
    "Nobody stops you. Nobody even follows."
    "Halfway across, you look back. He's still on the top roof with his haori blowing, watching you go. He lifts a hand."
    "The sun comes up over the Sumida, and the castle fades into the morning like smoke."
    $ vn_set_time(7, 0)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_flat", pc="smug", pc_tag="gdk_pc", cast=[("gdk_pirika", "bright")], cg="gdk_end_flat")
    "At home the costume lets go, and it's Kaoru in the mirror for good: the waist, the arse, the thighs, the hair down your back, the lips, the soft chest, and your cock between it all."
    "The lantern didn't take any of it back. You don't think it ever will."
    "Pirika glows so bright she sets off the smoke alarm. The priestess at the shrine gives you an amulet and a lot of advice."
    "You still patrol. Somebody has to. But one flicker is all you've got. Every fight with a yokai is a fight not to come in costume, and every time you very nearly do."
    "And every night a letter slides under your door on its own: black paper, green fire."
    "{i}The gate's still open. — S.{/i}"
    $ vn_set_time(23, 0)
    $ vn_enter(bg="gdk_bathroom", pc="hungry", pc_tag="gdk_pc", cast=[], cg="gdk_end_collar")
    "You keep the collar in a drawer."
    "On Friday nights you take it out and put it on and lie on your bed with your fingers buried in your arse and the brass lantern charm warm at your throat, and think of the castle."
    vn_sfx "Kuchu. Kuchu. Kuchu."
    gdk_you "\"Seiya♡— Seiya♡— ahh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "Afterwards you lie in the dark and listen for footsteps on the stairs. You don't know if you're hoping. You think you are."
    call gdk_thought_line
    call gdk_route_return("One flicker left")

label gdk_end_lit:
    $ vn_set_time(23, 30)
    $ vn_enter(bg="gdk_castle_roof", pc="moaning", pc_tag="gdk_pc", cast=[("gdk_lord", "hungry")], cg="gdk_end_roof")
    "You lean back into him and put your hand over his, over the clasp."
    gdk_akari "\"Make me.\""
    "He takes you right there on the top roof of the castle, with the whole city glowing below and the Parade waiting in the courtyard."
    "He puts your hands on the roof's gilded ridge and lifts your skirt and pushes into you from behind, slow and deep, both arms wrapped round your waist."
    vn_sfx "Pan. Pan. Pan."
    gdk_akari "\"Seiya♡— Seiya♡— I'm going to— it's going to go out— don't stop— DON'T STOP— AHHHH♡—!\"" with vnfx("flash", "shake")
    "The flicker goes out."
    "For one heartbeat everything is dark. Then the lantern lights again, green."
    $ gdk_grow(6)
    $ vn_enter(bg="gdk_castle_roof", pc="blissful", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")], cg="gdk_end_yokai")
    "{color=#ff5fb8}It lights in you, too. Cool green fire runs up your spine and out to your fingertips, and it doesn't hurt. It feels like coming home.{/color}"
    "{color=#ff5fb8}Your hair goes black, glossy and black with a green sheen, and the tips of your ponytail catch and burn with soft green flame that doesn't burn anything at all.{/color}"
    "{color=#ff5fb8}Your eyes light up green. The silk darkens to black and indigo, and the obi's bow flares the colour of ghost-fire. Wisps of green flame drift around you like fireflies. You can feel that this body isn't a costume any more. It's just you. You won't be coming out of it again.{/color}"
    "You're a yokai. His. And you've never felt so much like yourself."
    gdk_lord "\"There she is,\" he says, the same as the first night, and kisses the back of your neck. \"Ready?\""
    $ vn_set_time(23, 59)
    $ vn_enter(bg="gdk_festival", pc="smug", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk"), ("gdk_rasetsu", "grin")], cg="gdk_end_parade")
    "The Night Parade comes down through the lantern festival at midnight, and you walk at its head."
    "Your lantern burns green on its black pole. Every orange lantern on the street goes out as you pass under it, one after another, up the hill, until there's only your light left."
    "Behind you come the fox masks and the oni, Rasetsu whistling, and a hundred yokai, and the lord of the Kurayami with his hand at the small of your back."
    "Somewhere at the top of the hill, a small yellow light hovers by the shrine, watching. You lift your lantern to it, and it blinks twice and goes in."
    "Next year you'll walk at the front again. And the year after that, and every year after. Lighting the way."
    call gdk_thought_line
    call gdk_route_return("Lit by his fire")
