## harem: six chapters, six ranks. Each: the morning oiling (the chapter's body, worked in by hand), the gag with Orhan's
## near-miss, then the act (scenes.rpy), ending mid-act. Pass B: ch 1 and ch 4's acts forced, the flip at ch 5's bath.
## Production rewrite (2026-11-13, twinetesting-c9): the same plan, ending and pass, deepened: one label per beat, a picture
## per beat, choices that carry forward (route1, greet, help1, danceat, promise2, wave, talk3, jade3, fair, punish4, shout4,
## bet, tease5, toast6, secret6).

## ---- 1. The New Girl ---------------------------------------------------------------------------
label hrm_ch1:
    $ hrm.chapter = 1
    $ hrm.fit = "shirt"
    $ vn_enter(bg="hrm_rooftops", pc="grin", pc_tag="hrm_pc", cast=[], cg="hrm_window")
    "Night over Marazhan. A fat moon, a sea of domes, and a treasury window high up in the Saffron Palace that somebody forgot to bar."
    "You come out of it backwards, one leg and then the other, with the Sultan's ruby in your fist. It's the size of a hen's egg. It's warm from the velvet it was sleeping on."
    hrm_you "\"Hello, beautiful. You're coming to sea.\""
    vn_sfx "{i}Clang. Clang. CLANG.{/i}"
    "Somewhere below, a bell. Then a shout. Then the whole palace guard is shouting, and lamps are swinging in every courtyard at once."
    show cg hrm_chase onlayer cgl
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"STOP, THIEF! In the name of the Sultan!\""
    "Captain Brask of the palace guard, square-jawed, breastplate flashing in the moon, already on the roof two domes back and coming fast."
    hrm_you "\"Evening, Captain! Lovely night for it!\""
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"You'll be counting cobbles in the dungeon for this! I'll have you, thief!\""
    menu:
        "The roofs split ahead: a forest of washing lines one way, a long copper gutter the other."
        "Over the washing lines":
            $ hrm.route1 = "lines"
            show cg hrm_gutter onlayer cgl
            "You go over the washing lines hand over hand like rigging, sheets slapping your face, somebody's enormous pantaloons wrapping round your head for one bad second."
            "Behind you the captain gets a tablecloth in the face and swears like a sailor. Better than most sailors, honestly."
        "Down the gutter":
            $ hrm.route1 = "gutter"
            show cg hrm_gutter onlayer cgl
            "You sit down in the copper gutter and go, on your backside, the whole length of the east wing, faster than any horse, sparks coming off the rivets."
            "Behind you the captain tries it standing up. You hear the clatter, and the word he says, and you laugh the whole way down."
    hide cg onlayer cgl
    show cg hrm_brask_roof onlayer cgl
    "But he's good, Captain Brask. He's earnest and he's sweating and he jumps a gap you'd have thought twice about, and he's gaining."
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"There's nowhere to go, thief! Every gate's shut! I'll turn this palace inside out!\""
    "He's right. You're running out of roof. There's only one way left, and it's down."
    jump hrm_skylight

label hrm_skylight:
    $ vn_enter(bg="hrm_rooftops", pc="startled", pc_tag="hrm_pc", cast=[], cg="hrm_skylight")
    "A glass skylight, propped open on a stick, with steam pouring out of it into the cold."
    "So you do what any sensible sailor does. You go through it feet first."
    vn_sfx "{i}SPLOOSH.{/i}" with vnfx("shake")
    "Steam, blue tiles, and then hot water closing over your head."
    show cg hrm_tile onlayer cgl
    "You come up in a round hot pool in a great tiled bathhouse, coughing, your hair stuck to your face. Lamps. Marble slabs. Jars and jars of something that smells like roses."
    "There's a loose blue tile by your hand, at the pool's lip. The ruby goes under it before you've finished thinking about it, and you press the tile back down flat."
    hrm_you "\"Stay. Good girl.\""
    "Then footsteps, quick and brisk, and the jingle of a lot of keys."
    jump hrm_named

label hrm_named:
    $ vn_enter(bg="hrm_bathhouse", pc="startled", pc_tag="hrm_pc", cast=[("hrm_dilara", "brisk")], cg="hrm_dahlia")
    "A brisk grey-haired woman with a ring of keys at her belt bustles in, sees a wet stranger with long black hair climbing out of her hot pool in a soaked shirt, and does not scream."
    hrm_dilara "\"There you are! The new girl. You're late, and you're soaking, and you came in through the {i}roof?{/i} Never mind. Never mind. They said you were tall.\""
    "She takes your chin in her hand and turns your face to the lamp. Lanky. Weathered. Stubbled. Long black hair down your back in a sailor's tail, dripping."
    hrm_dilara "\"Hm. Well. We've worked with worse. I name every new girl for a flower.\""
    menu:
        "She's waiting. You should probably do something girlish."
        "Curtsey":
            $ hrm.greet = "curtsey"
            "You curtsey. You've seen it done on the docks, by the captains' wives. You get one foot behind the other, hold out a wet shirt-tail and dip."
            "It's the worst curtsey in the history of the sultanate. The matron sighs through her nose."
            hrm_dilara "\"We'll work on that.\""
        "Bow like a sailor":
            $ hrm.greet = "bow"
            "You bow like a sailor, from the waist, hand on your heart, the way you'd bow to a harbourmaster you were about to cheat."
            hrm_dilara "\"Girls {i}curtsey{/i}, flower. Where on earth did they find you?\""
            hrm_you "\"The sea, ma'am.\""
    hrm_dilara "\"Dahlia. Welcome to the Saffron Palace, Dahlia.\""
    "The Saffron Palace. The {i}harem{/i} of the Saffron Palace. You have dropped through the roof into the Sultan's harem."
    "The only men allowed past its gate are the eunuchs. Outside it, Captain Brask is turning the city over for a thief."
    vn_th "Nobody's going to search in here. Nobody {i}can{/i} search in here."
    hrm_you "\"Best hiding place in the world.\""
    show screen hrm_rank(1)
    "You say it under your breath. The matron writes something in a big book and doesn't ask what you said."
    hide screen hrm_rank
    jump hrm_orhan1

label hrm_orhan1:
    $ vn_enter(bg="hrm_bathhouse", pc="startled", pc_tag="hrm_pc", cast=[("hrm_orhan", "jolly")], cg="hrm_orhan_pat")
    "Then a big jolly man fills the doorway: bald as an egg, round-faced, a rich purple robe, and a velvet case at his belt that he pats, lovingly, as if it were a cat."
    hrm_orhan "\"A new arrival! At this hour! Let's have a look at you, flower.\""
    "He comes forward, beaming, hands already out. The velvet case swings at his hip."
    vn_th "Don't look at the case. Whatever's in it, don't look at the case."
    hide hrm_orhan
    show hrm_dilara brisk at vn_cast_slot
    hrm_dilara "\"Not {i}now{/i}, Orhan, she's still being oiled. Look at her. She's half drowned. Shoo.\""
    hide hrm_dilara
    show hrm_orhan jolly at vn_cast_slot
    hrm_orhan "\"Of course, of course. Tomorrow, then. Or the day after. There's no hurry, flower. There's never any hurry.\""
    "He pats the velvet case again, very gently, smiling at you over it, and goes away humming."
    "You let out a breath you'd been holding since the skylight."
    hide cg onlayer cgl
    hide hrm_orhan
    $ vn_enter(bg="hrm_bathhouse", pc="startled", pc_tag="hrm_pc", cast=[("hrm_dilara", "brisk")], cg="hrm_trio")
    "The matron claps her hands, and three women drift in out of the steam in silk wraps, eyeing you."
    "Zarina, sharp-eyed, a heavy dark braid over one shoulder and a mouth that looks like it's about to say something wicked. Leyla, chestnut-haired, who giggles the second she sees you. Nasrin, black curls, the biggest breasts you've seen on land or sea, who yawns."
    hrm_dilara "\"The new girl. Dahlia. Oil her, girls. All of her. I want her soft by morning.\""
    hide hrm_dilara
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"She's so {i}tall!{/i}\""
    hide hrm_dilara
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"She's so wet.\""
    hide hrm_dilara
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"She's so {i}interesting.{/i}\""
    "And the matron leaves you with them, and her keys jingle away down the corridor, and the door swings shut."
    hide hrm_dilara
    jump hrm_pool

label hrm_ch1_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump hrm_ch2

## ---- 2. The Coin Belt --------------------------------------------------------------------------
label hrm_ch2:
    $ hrm.chapter = 2
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_oil_2")
    "The morning oiling. A marble slab, warm from the pool, and you on your back on it with nothing on, and Zarina, Leyla and Nasrin round you with their sleeves pushed up and a jar each."
    hide hrm_zarina
    show hrm_dilara brisk at vn_cast_slot
    hrm_dilara "\"Oil, girls. All of her.\""
    if hrm.greet == "curtsey":
        hide hrm_zarina
        show hrm_dilara brisk at vn_cast_slot
        hrm_dilara "\"And when you're done, Dahlia, we'll do that curtsey again. Properly.\""
    else:
        hide hrm_zarina
        show hrm_dilara brisk at vn_cast_slot
        hrm_dilara "\"And when you're done, Dahlia, no more sailor's bows. Girls curtsey.\""
    "The matron sits by the door with her big book, and the three of them keep their backs between her and the slab, and get to work. By hand. Everywhere."
    if hrm.help1 == "call":
        hide hrm_dilara
        show hrm_zarina wicked at vn_cast_slot
        hrm_zarina "\"Morning, flower. Going to shout for help again?\""
    else:
        hide hrm_dilara
        show hrm_zarina wicked at vn_cast_slot
        hrm_zarina "\"Morning, flower. Going to bite your lip again?\""
    hrm_you "\"{i}Shh!{/i}\""
    $ hrm_body(2)
    show cg hrm_oil_2_waist onlayer cgl
    "{color=#f0a0c0}The rose oil goes on warm and sinks in hot. Under six slick hands your skin goes soft, softer than any sailor's has a right to be, soft as the inside of a wrist all over. Your waist softens where Nasrin's palms go round it. You put a hand to your jaw and the stubble is gone, and it doesn't come back. It never will.{/color}"
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Look at that waist. Yesterday that was a plank.\""
    "And inside a minute you're hard. Rock hard and leaking on your own belly, in the Sultan's bathhouse, with the matron just across the room."
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Eep! Towel! {i}Towel!{/i}\""
    "Leyla giggles and drops a towel over it, which helps nobody, because it stands the towel up like a tent."
    menu:
        "Keeping it out of the matron's sight."
        "Press your thighs together":
            $ hrm.hide2 = "thighs"
            "You clamp your thighs shut and think about bilge water. It makes it worse. Zarina oils the insides of them anyway, slowly, smiling at you."
        "Turn to the wall":
            $ hrm.hide2 = "wall"
            "You roll over and face the tiles like a guilty man. Nasrin oils your backside instead, both hands, and laughs, low and lazy."
    hide hrm_dilara
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Hold still, Dahlia. You're being oiled.\""
    hide hrm_zarina
    show hrm_dilara brisk at vn_cast_slot
    hrm_dilara "\"Is she soft yet?\""
    hide hrm_dilara
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Getting there, Matron. Some parts are very {i}hard{/i} work.\""
    "Leyla has to put her face in a towel of her own."
    jump hrm_ch2_dress

label hrm_ch2_dress:
    $ hrm.fit = "veils"
    $ vn_enter(bg="hrm_bathhouse", pc="grin", pc_tag="hrm_pc", cast=[("hrm_dilara", "brisk")], cg="hrm_veils")
    "Afterwards Matron Dilara looks you over, soft and shining and smelling of roses, and makes up her mind."
    hrm_dilara "\"Good hips. Long legs. You'll dance.\""
    "Veils of rose-pink gauze, a short sheer skirt, and a belt of gold coins that she ties round your hips herself, low, tugging it into place."
    show screen hrm_rank(2)
    hrm_dilara "\"A dancer. The Sultan's court sees the dancers this afternoon. Don't fall over.\""
    hide screen hrm_rank
    show cg hrm_belt_jingle onlayer cgl
    "You try a step. The coins go {i}shhing{/i}. You try another, and Zarina walks past in the doorway, and you think about the night before, and the coins go {i}shhing-shhing-shhing{/i} all on their own."
    vn_sfx "{i}Shhing. Shhing.{/i}"
    hide hrm_dilara
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"It jingles when she's hard! Zarina! It {i}jingles{/i} when she's—\""
    hide hrm_dilara
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"I heard, Leyla. The whole palace heard.\""
    "Forty women in this harem, the rose oil every morning, and a sultan who summons one of them a month. And three of them have found the only cock in the palace, and it rings like a shop bell."
    jump hrm_ch2_dance

label hrm_ch2_dance:
    $ vn_enter(bg="hrm_dancecourt", pc="grin", pc_tag="hrm_pc", cast=[], cg="hrm_dance")
    "The dance for the court, in the tiled courtyard by the fountain. Drums, a pipe, a lot of silk cushions and a lot of bored courtiers on them."
    "And on the biggest cushions, under an awning, Sultan Kasim himself: handsome, black-bearded, a gold circlet, a cup of wine, the air of a man who has never once been in a hurry."
    "It turns out you're good at the hips. Years and years of decks rolling under you."
    menu:
        "The drums pick up."
        "Work the hips":
            $ hrm.dance = "hips"
            "You roll your hips like a deck in a swell, slow and deep, and the whole court sighs."
        "Shimmy the coins":
            $ hrm.dance = "shimmy"
            "You shimmy, shoulders to knees, and every coin on the belt sings at once."
    menu:
        "Who do you dance at?"
        "Dance at the Sultan":
            $ hrm.danceat = "sultan"
            "You dance straight at the awning, hips first, because if you're going to hide in the man's harem you might as well be the best thing in it."
            show cg hrm_sultan_yawn onlayer cgl
            "Sultan Kasim watches you over his cup for a while with a lazy smile. Then he yawns, enormously, and flicks a gold coin onto the tiles at your feet."
            show hrm_kasim lazy at vn_cast_slot
            hrm_kasim "\"The jingling one. Charming.\""
        "Dance at Zarina":
            $ hrm.danceat = "zarina"
            "You dance at Zarina, who's at the edge of the line with her braid over her shoulder, watching you like a cat watches a fish."
            show cg hrm_sultan_yawn onlayer cgl
            "She mouths something at you. You're fairly sure it's {i}tonight.{/i} On his cushions, Sultan Kasim yawns, enormously, and doesn't see any of it."
    "The trouble is the coin belt jingles whenever you get hard. And with the oil in you and Zarina dancing past, you're hard the whole way through, and you jingle the whole way through. Every beat. Every turn."
    vn_sfx "{i}Shhing-shhing-shhing-shhing.{/i}"
    jump hrm_ch2_inspect

label hrm_ch2_inspect:
    $ vn_enter(bg="hrm_dancecourt", pc="startled", pc_tag="hrm_pc", cast=[("hrm_orhan", "jolly")], cg="hrm_inspect_2")
    "When the drums stop, Orhan lines the dancers up along the fountain for inspection. Hands behind his back. Velvet case at his belt. Beaming."
    hrm_orhan "\"Lovely. Lovely. Lift your veil, flower, let's see. Lovely.\""
    "He works his way down the line, girl by girl, closer and closer. Your coins are jingling like a tambourine in a high wind."
    hrm_orhan "\"Ah! The new girl! The {i}jingling{/i} girl! Marvellous jingling, Dahlia. Truly. I've never heard the like. Now let's just have a look under—\""
    "His hand is at the hem of your sheer skirt. The velvet case is right there at his hip."
    vn_th "This is it. Not even a day. A personal best."
    hide hrm_orhan
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Orhan! Wine!\""
    "The Sultan, from under the awning, holding up an empty cup."
    hide hrm_kasim
    show hrm_orhan jolly at vn_cast_slot
    hrm_orhan "\"Majesty! At once!\""
    "And Orhan pats your cheek, and pats the velvet case, and hurries off to find the wine, and forgets you entirely."
    hide hrm_orhan
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Lucky.\""
    hrm_you "\"I'm the luckiest man— the luckiest {i}girl{/i} in the world.\""
    hide hrm_orhan
    jump hrm_three

label hrm_ch2_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump hrm_ch3

## ---- 3. The Jade -------------------------------------------------------------------------------
label hrm_ch3:
    $ hrm.chapter = 3
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_oil_3")
    "The morning oiling. You don't even pretend to mind any more. You climb onto the warm slab on your own and lie back and let six oiled hands go everywhere."
    if hrm.promise2 == "every":
        hide hrm_zarina
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"You promised {i}every{/i} night, Dahlia. Every! I'm holding you to it.\""
    else:
        hide hrm_zarina
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"You said {i}same again tonight{/i}, Dahlia. I'm holding you to it.\""
    hrm_you "\"Have I ever let you down, Leyla?\""
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"You've known me two days!\""
    $ hrm_body(3)
    "{color=#f0a0c0}The oil burns sweet, and under their hands your chest goes soft and full: two soft swells where it was flat, rising into Zarina's palms, with puffy nipples that stand right up. Your hips push out wider under Nasrin's hands. Your ass rounds. And your cock, hard and leaking in Zarina's slick fist, is smaller than it was yesterday.{/color}"
    hide hrm_leyla
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"It's shrinking, Dahlia. Look at it. Still leaking, though. Still {i}so{/i} keen.\""
    "She pinches your new nipple, just to watch, and you leak like a squeezed lemon, and Leyla applauds."
    hrm_you "\"{i}Hah{/i}— that's— those are new—\""
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"They suit you.\""
    show cg hrm_oil_3_hips onlayer cgl
    "Nasrin takes your hips in both hands and rocks them, side to side, lazily, considering."
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Wider. You'll need new silks.\""
    jump hrm_ch3_move

label hrm_ch3_move:
    $ hrm.fit = "silks"
    $ vn_enter(bg="hrm_chamber", pc="grin", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_handmaiden")
    "Zarina asks the matron for a handmaiden, and points at you, and the matron writes it in her book without looking up."
    show screen hrm_rank(3)
    "Zarina's handmaiden. You move into her rooms: cushions, lamps, a low bed, a carved screen, and a chest of her cast-off silks, wine-red and loose."
    hide screen hrm_rank
    "They fit better than they should. The top sits on your new chest like it was cut for it. The trousers sit on your hips like they missed them."
    show cg hrm_zarina_rooms onlayer cgl
    hrm_zarina "\"Turn round. Again. Mm. You're mine now, handmaiden. You fetch, you carry, you do what I say.\""
    hrm_you "\"And what do you say?\""
    hrm_zarina "\"Tonight? I say we turn it round.\""
    "She doesn't explain that. She smiles at you like a cat with the cream, and goes out to bathe."
    hrm_you "\"Climbing the ranks, ladies.\""
    jump hrm_ch3_gate

label hrm_ch3_gate:
    $ vn_enter(bg="hrm_gate", pc="grin", pc_tag="hrm_pc", cast=[("hrm_brask", "earnest")], cg="hrm_gate_wave")
    "At midday there's shouting at the harem gate. You go out on Zarina's balcony to look, in her silks, with a bowl of figs."
    "Captain Brask, sweating in his breastplate, and Orhan, very large and very calm, filling the gateway."
    hrm_brask "\"I'll find him, Majesty! He's in the palace, I know he is! I want to search the harem!\""
    hide hrm_brask
    show hrm_orhan jolly at vn_cast_slot
    hrm_orhan "\"No man enters the harem, Captain. Not one. Not ever.\""
    if hrm.route1 == "lines":
        hide hrm_orhan
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"He went over the washing lines like a monkey! He could be anywhere! He could be in the {i}laundry!{/i}\""
    else:
        hide hrm_orhan
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"He went down the east gutter on his backside! He could be anywhere! He could be in the {i}drains!{/i}\""
    hide hrm_brask
    show hrm_orhan jolly at vn_cast_slot
    hrm_orhan "\"Then search the laundry and the drains, Captain. Not my ladies.\""
    show cg hrm_brask_look onlayer cgl
    "The captain looks up, at last, red-faced, and sees a tall girl on the balcony above the gate in wine-red silks, eating a fig."
    menu:
        "From the balcony in Zarina's silks."
        "Wave at the captain":
            $ hrm.wave = "wave"
            "You wave down at him, sweetly, fingers fluttering. The captain, sweating, waves back without thinking, and then looks at his own hand like it's betrayed him."
        "Blow the captain a kiss":
            $ hrm.wave = "kiss"
            "You blow him a kiss, a big one, both hands. He goes red to the ears, nearly drops his sword, and has to be helped back down the corridor by a guard."
    vn_th "An arm's length from the man, and he's blushing."
    jump hrm_ch3_orhan

label hrm_ch3_orhan:
    $ vn_enter(bg="hrm_chamber", pc="startled", pc_tag="hrm_pc", cast=[("hrm_orhan", "jolly")], cg="hrm_talk_out")
    "Then, in the afternoon, Orhan comes to inspect the handmaidens. He finds you in Zarina's rooms folding silks, and rubs his hands."
    hrm_orhan "\"Ah! Zarina's new handmaiden! Now, flower, let's just have that look we never—\""
    "Zarina, Leyla and Nasrin come through the screen at once, as if they'd been waiting behind it, which they had, and crowd round him and talk."
    hide hrm_orhan
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Orhan, the matron's out of the good oil again—\""
    hide hrm_orhan
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Orhan, there's a {i}cat{/i} in the bathhouse, a real one, a big orange one—\""
    hide hrm_orhan
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Orhan. Is that a new robe.\""
    menu:
        "Orhan's eyes are sliding back to you over their heads."
        "Join in about his velvet case":
            $ hrm.talk3 = "case"
            hrm_you "\"Orhan, I've been meaning to ask: that case. Is it {i}real{/i} velvet? The stitching's beautiful.\""
            "His whole face lights up. He unhooks it and holds it out for you to admire, without opening it, and talks about its stitching for a very long time."
        "Tell him a sailor's story":
            $ hrm.talk3 = "story"
            hrm_you "\"Orhan, did I ever tell you about the time I saw a sea serpent off the Pearl Coast? Big as a palace. Eyes like lamps.\""
            "He sits down on the end of the bed to hear it. It gets longer. It acquires a mermaid. Then a second mermaid, and a storm."
    "By the time the four of you are done, he's forgotten why he came. He gets up, puzzled and pleased, and goes to the door."
    hide hrm_leyla
    hide hrm_nasrin
    hide hrm_zarina
    show hrm_orhan jolly at vn_cast_slot
    hrm_orhan "\"Well! I'll come back another day. There's no hurry. There's never any hurry.\""
    "He pats the velvet case on his way out, and smiles at you over it."
    hide hrm_orhan
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Close. Too close. We'll have to keep him busy.\""
    hrm_you "\"Till when?\""
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Till we're bored of you, flower. Don't hold your breath.\""
    jump hrm_jade

label hrm_ch3_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump hrm_ch4

## ---- 4. We'll Start Small ----------------------------------------------------------------------
label hrm_ch4:
    $ hrm.chapter = 4
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_nasrin", "lazy")], cg="hrm_oil_4")
    "The morning oiling. You're on the slab before they've got the lids off the jars."
    hrm_nasrin "\"My turn.\""
    "Nasrin gets your chest this morning, which she announces like a claim on a gold field, and oils it with both hands, slow, round and round."
    $ hrm_body(4)
    "{color=#f0a0c0}And under her hands it fills. Small full breasts now, a real handful each, round and high and soft, that she weighs and squeezes and lifts. Your hips are wide under Leyla's oil. Your ass is round under Zarina's. Your thighs thicken where their palms go. And your cock is small, small and stiff and leaking, poking up at the steam like it's asking a question.{/color}"
    show cg hrm_oil_4_weigh onlayer cgl
    hrm_nasrin "\"A B. Nearly. Look at that. Leyla, feel.\""
    hide hrm_nasrin
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Oh, they're {i}heavy!{/i} Dahlia, you're getting {i}heavy!{/i}\""
    hrm_you "\"{i}Hah{/i}— Nasrin— if you keep doing that I'm going to—\""
    "She keeps doing it until you whimper, then wanders off satisfied, wiping her hands on Leyla."
    jump hrm_ch4_sheer

label hrm_ch4_sheer:
    $ hrm.fit = "sheer"
    $ vn_enter(bg="hrm_chamber", pc="grin", pc_tag="hrm_pc", cast=[], cg="hrm_sheer")
    "Promoted again. Matron Dilara looks at your chest and your hips for a long moment and writes it down."
    show screen hrm_rank(4)
    "A concubine. Sheer gold-trimmed silks you can see everything through, every curve, every nipple, except the one thing, which you keep turned to the wall."
    hide screen hrm_rank
    "You look at yourself in Zarina's mirror. Smooth all over. Breasts. Hips. That hair, black and glossy and down past your shoulder blades now."
    vn_th "The lads on the {i}Gull{/i} wouldn't know me. I barely know me. I look {i}expensive.{/i}"
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Don't get comfortable. Concubines get Orhan's full inspection.\""
    hrm_you "\"How full?\""
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"All the way full.\""
    jump hrm_ch4_inspect

label hrm_ch4_inspect:
    $ vn_enter(bg="hrm_chamber", pc="startled", pc_tag="hrm_pc", cast=[("hrm_orhan", "jolly")], cg="hrm_inspect_line")
    "The new concubines in a row, in a quiet room, and Orhan going down it with his warm dry hands. No court to call him away. No wine. No cat."
    "Zarina, Leyla and Nasrin try. Leyla tries the cat again. Nasrin tries the robe. Orhan smiles at them both and shuts the door."
    if hrm.talk3 == "case":
        hrm_orhan "\"Dahlia! You were very kind about my case. Very kind. Now, flower, hold still.\""
    else:
        hrm_orhan "\"Dahlia! The serpent girl! Two mermaids, I said to the matron, two! Now, flower, hold still.\""
    show cg hrm_case_open onlayer cgl
    "Hands-on, under the silks. He finds it."
    "He doesn't shout. He doesn't drop anything. He looks at you, for a long moment, kindly, the way a man looks at a dog that's eaten a shoe."
    "Then he unhooks the velvet case and opens it on his knee. Inside, on white silk, lie a pair of golden shears and a small golden cage."
    vn_th "Oh. Oh, that's what's in the case."
    "He considers them, kindly, one and then the other. He picks up the shears. He looks at them. He puts them back."
    hrm_orhan "\"We'll start small.\""
    show cg hrm_cage_on onlayer cgl
    vn_sfx "{i}Click.{/i}"
    $ hrm_body("4c")
    "{color=#f0a0c0}He fits the small golden cage on your small cock, neat as a jeweller, and locks it with a dainty golden key. It sits snug and warm and it doesn't let you get hard, not properly, just press and throb against the bars.{/color}"
    "He hangs the key on his belt, pats your cheek, and says nothing to anyone. He never will."
    menu:
        "You look down at it."
        "\"Fair.\"":
            $ hrm.fair = "fair"
            hrm_you "\"Fair.\""
            hrm_orhan "\"I thought so too, flower.\""
        "\"...Fair enough.\"":
            $ hrm.fair = "enough"
            hrm_you "\"...Fair enough, really. All things considered.\""
            hrm_orhan "\"All things considered, flower, yes.\""
    hide hrm_orhan
    show cg hrm_cage_women onlayer cgl
    "When he's gone, the three of them come through the screen and kneel round you to look."
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"It's so {i}shiny!{/i}\""
    "She taps it. It goes {i}ting.{/i} You leak through the bars, and Nasrin laughs so hard she has to lie down."
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Well. That's the cock gone, then.\""
    hrm_you "\"It's not {i}gone{/i}, it's—\""
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Busy. It's busy, Dahlia. We'll think of something else.\""
    jump hrm_ch4_note

label hrm_ch4_note:
    $ vn_enter(bg="hrm_chamber", pc="startled", pc_tag="hrm_pc", cast=[("hrm_dilara", "brisk")], cg="hrm_summons_note")
    "At dusk a lamp at the door, and Matron Dilara with a folded note, flustered for the first time since you met her."
    hrm_dilara "\"The Sultan wants the new concubine. Tonight. Now. Hair, girls! Oil! The good jar!\""
    "There's a stampede. Your hair's brushed by three people at once. The good oil goes on every inch of you that shows, which in sheer silks is every inch."
    vn_th "No. No, no. Not him. He'll see. Anyone who gets that close will see."
    hide hrm_dilara
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Keep the silks down at the front, and lie on your belly, and he'll never look. Men like him never look.\""
    hrm_you "\"I can't— Zarina, I can't go, I'm not—\""
    hide hrm_zarina
    show hrm_dilara brisk at vn_cast_slot
    hrm_dilara "\"Nobody {i}can't{/i} go, flower. Off you go.\""
    hide hrm_dilara
    jump hrm_summons

label hrm_ch4_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump hrm_ch5

## ---- 5. The Favourite's Bath -------------------------------------------------------------------
label hrm_ch5:
    $ hrm.chapter = 5
    $ hrm.she = True
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_oil_5")
    "Dahlia lies back on the oiling slab, stretches like a cat, and lets them."
    "The matron doesn't even pretend to watch any more. Since the summons, the new concubine has been sent for nearly every night, and the matron has started calling her {i}the favourite{/i} in front of the others."
    $ hrm_body(5)
    "{color=#f0a0c0}Big breasts now, under the women's hands, big enough to fill both of Nasrin's and spill: heavy and soft and swaying when she breathes. A waist going in where it never used to, an hourglass forming under Leyla's palms. A big round ass. Thick soft thighs. Long glossy black hair down to her waist, that Zarina oils strand by strand. And the small golden cage, shining with rose oil.{/color}"
    hrm_dahlia "\"{i}Mmh.{/i} Harder on the left, Nasrin.\""
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Bossy.\""
    hrm_dahlia "\"Favoured.\""
    jump hrm_ch5_check

label hrm_ch5_check:
    $ vn_enter(bg="hrm_bathhouse", pc="smug", pc_tag="hrm_pc", cast=[("hrm_orhan", "jolly")], cg="hrm_orhan_check")
    "Orhan looks in on his rounds, as he does every morning now. He bends over the slab, checks the cage with one finger, turns it to the light, and pats it."
    hrm_orhan "\"Very nice. Very nice. All in order, flower.\""
    hrm_dahlia "\"Thank you, Orhan.\""
    "He goes away humming, satisfied, the key on his belt."
    jump hrm_ch5_milk

label hrm_ch5_milk:
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_milking")
    "Then the oiling ends the new way."
    if hrm.jade3 == "ask":
        hrm_zarina "\"On your knees, favourite. You asked for this once, remember? Now you get it every morning.\""
    else:
        hrm_zarina "\"On your knees, favourite. You dared me once, remember? Now I win every morning.\""
    "Dahlia rolls over onto her hands and knees on the slab, ass up, breasts hanging heavy, and Zarina's oiled fingers slide into her, two of them, and curl, and press."
    "And press. And press, slow and deliberate, right on the spot, until Dahlia's mouth falls open and her thighs shake and she leaks through the bars of the cage, a thin warm string of it, and Leyla catches it in a small silver dish."
    hrm_dahlia "\"{i}Ahh{/i}— Zarina— {i}ahh{/i}— oh, it's {i}coming{/i}—\""
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Got it! Got it all!\""
    show cg hrm_dish_feed onlayer cgl
    "Leyla holds the dish to Dahlia's lips."
    hide hrm_leyla
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Open your mouth. Swallow.\""
    hrm_dahlia "\"{i}Mmh{/i}— yes, ma'am—\""
    "She drinks it down off the silver, every drop, and licks the rim, and grins up at them."
    jump hrm_ch5_game

label hrm_ch5_game:
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_nasrin", "lazy")], cg="hrm_game")
    "It becomes the women's new game at the morning milking: who can milk the caged girl fastest. Leyla keeps time by counting out loud. Zarina keeps the dish."
    menu:
        "The milking race."
        "Bet on Nasrin":
            $ hrm.bet = "nasrin"
            "You bet on Nasrin. Nasrin wins, lazily, without even sitting up, two fingers and a yawn, and Dahlia's leaking into the dish before Leyla's got to ten."
        "Bet on Leyla":
            $ hrm.bet = "leyla"
            "You bet on Leyla. Leyla tries so hard her tongue sticks out. Nasrin wins anyway, lazily, without sitting up."
    show cg hrm_game_rematch onlayer cgl
    hide hrm_nasrin
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Rematch! I want a rematch! She wasn't {i}ready!{/i}\""
    hrm_dahlia "\"I'm always ready, Leyla— {i}ahh{/i}— oh, you're doing it {i}now{/i}— {i}ahh{/i}—\""
    "Leyla gets her rematch, and loses it, and gets another, and Dahlia leaks into the dish three times before breakfast and drinks every one."
    jump hrm_ch5_jewels

label hrm_ch5_jewels:
    $ hrm.fit = "jewels"
    $ vn_enter(bg="hrm_chamber", pc="smug", pc_tag="hrm_pc", cast=[("hrm_dilara", "brisk")], cg="hrm_jewels")
    "Matron Dilara dresses the favourite herself. Gold chains over the shoulders and between the breasts. Bangles to the elbow. A jewelled girdle that sits low on the hips and hides exactly one thing."
    show screen hrm_rank(5)
    hrm_dilara "\"The Sultan's favourite. In my book, in ink. Don't let it go to your head.\""
    hide screen hrm_rank
    hrm_dahlia "\"Matron. Tonight, when he sends for me. I want Zarina with me.\""
    hrm_dilara "\"Zarina? He hasn't sent for Zarina in a year.\""
    hrm_dahlia "\"That's why.\""
    "The matron looks at her for a long moment. Then she writes it in the book."
    hrm_dilara "\"The favourite asks. The favourite gets.\""
    hide hrm_dilara
    $ vn_enter(bg="hrm_chamber", pc="smug", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_zarina_ask")
    "Zarina is on the low bed, eating figs, when Dahlia tells her. She stops with a fig halfway to her mouth."
    hrm_zarina "\"You did {i}what?{/i}\""
    hrm_dahlia "\"You're coming to the private bath. Tonight. With me. Wear the red.\""
    "For the first time since the hot pool, Zarina has nothing wicked to say. She puts the fig down. She looks at Dahlia like she's seeing her for the first time."
    hrm_zarina "\"...The red's at the cleaner's.\""
    hrm_dahlia "\"Then wear nothing.\""
    hide hrm_zarina
    jump hrm_bath

label hrm_ch5_after:
    hide cg onlayer cgl
    call vn_night(7)
    jump hrm_ch6

## ---- 6. My Favourite Has a Secret --------------------------------------------------------------
label hrm_ch6:
    $ hrm.chapter = 6
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_bathhouse", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_leyla", "giggle")], cg="hrm_oil_6")
    "The morning oiling, for the festival. Every lamp in the bathhouse lit, the good jars open, petals on the water."
    $ hrm_body(6)
    "{color=#f0a0c0}And Dahlia at her biggest. Huge breasts, heavy and high, spilling through the women's fingers however they hold them, rolling when she laughs. A true hourglass, the waist small between the wide hips. A big round ass that Zarina slaps for the sound of it. Thick soft thighs. Long glossy black hair pooled on the marble. And the small golden cage, gleaming.{/color}"
    hide hrm_leyla
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Biggest yet.\""
    hrm_dahlia "\"Biggest {i}ever.{/i}\""
    show cg hrm_oil_6_milk onlayer cgl
    "Then the milking, and for the festival they milk her twice for luck: Zarina's fingers and then Nasrin's, and Dahlia on her knees on the slab leaking twice into the silver dish, moaning both times, and twice Leyla feeds it to her."
    hide hrm_nasrin
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Twice for luck! Open up, Dahlia!\""
    hrm_dahlia "\"{i}Mmh{/i}— lucky— {i}ahh{/i}— so lucky—\""
    if hrm.bet == "leyla":
        hide hrm_nasrin
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"And I was faster that time. Nasrin, say I was faster.\""
        hide hrm_leyla
        show hrm_nasrin lazy at vn_cast_slot
        hrm_nasrin "\"You were faster.\""
        hide hrm_nasrin
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"Thank you!\""
    else:
        hide hrm_leyla
        show hrm_nasrin lazy at vn_cast_slot
        hrm_nasrin "\"Still faster.\""
        hide hrm_nasrin
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"Nobody {i}asked{/i}, Nasrin.\""
    jump hrm_ch6_court

label hrm_ch6_court:
    $ hrm.fit = "collar"
    $ vn_enter(bg="hrm_throneroom", pc="smug", pc_tag="hrm_pc", cast=[("hrm_kasim", "lazy")], cg="hrm_collar")
    "The court. The throne room hung with silk, the whole harem lined up before the steps in their festival best, and Sultan Kasim, for once, sitting up straight."
    hrm_kasim "\"My flower. Come here.\""
    "Dahlia goes up the steps, every eye in the hall on her hips. He stands, and fastens a gold collar at her throat with his own hands."
    show screen hrm_rank(6)
    hrm_kasim "\"First of the harem. Over every woman in the Saffron Palace. Let it be written.\""
    hide hrm_kasim
    show hrm_dilara brisk at vn_cast_slot
    hrm_dilara "\"It is written, Majesty.\""
    hide screen hrm_rank
    if hrm.greet == "curtsey":
        "Dahlia curtseys, perfectly, and the matron, at the end of the line, presses a hand to her heart. All that practice."
    else:
        "Dahlia bows from the waist like a sailor to a harbourmaster, and the whole harem laughs, and the matron puts her face in her book."
    show cg hrm_court_ruby onlayer cgl
    hide hrm_dilara
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"And a gift. My captain found it only this morning, can you believe it? Under a loose tile in the bathhouse.\""
    "He hangs it round her neck on a gold chain: a ruby the size of a hen's egg, warm from his hand. {i}The{/i} ruby. The very one."
    hide hrm_dilara
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Under a {i}blue tile{/i}, by the hot pool. The thief must have dropped it running. Where he went after, nobody knows!\""
    "Dahlia laughs. She tries not to. She laughs so hard she has to sit down on the steps of the throne, the ruby bouncing between her breasts, laughing till she can't breathe."
    "Captain Brask, by the throne in his best breastplate, has no idea why the favourite is laughing."
    menu:
        "The Sultan calls for wine. Every cup in the hall goes up. Dahlia lifts hers."
        "\"To the thief!\"":
            $ hrm.toast6 = "thief"
            hrm_dahlia "\"To the thief!\""
            hide hrm_dilara
            show hrm_kasim lazy at vn_cast_slot
            hrm_kasim "\"Ha! Wicked girl! To the thief, and may I catch him!\""
        "\"To the captain!\"":
            $ hrm.toast6 = "captain"
            hrm_dahlia "\"To the captain, who found it!\""
            "The captain goes red to his ears again."
    jump hrm_ch6_brask

label hrm_ch6_brask:
    $ vn_enter(bg="hrm_throneroom", pc="smug", pc_tag="hrm_pc", cast=[("hrm_brask", "earnest")], cg="hrm_brask_bow")
    hide hrm_brask
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"And for finding it, Captain, an honour no man has ever had. A night in the harem. In the great bath. With my favourite.\""
    "A gasp all down the line of women. Orhan drops his wine. Captain Brask goes white, then red, then white."
    hide hrm_kasim
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"Majesty— I— thank you, Majesty. Thank you.\""
    if hrm.route1 == "lines":
        hide hrm_kasim
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"I only wish I'd caught him. Over the washing lines like a monkey, he went. I'll never forget it.\""
    else:
        hide hrm_kasim
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"I only wish I'd caught him. Down the east gutter on his backside, he went. I'll never forget it.\""
    if hrm.wave == "wave":
        hide hrm_kasim
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"And then there was a girl on the harem balcony, waving at me, and I lost my place in the whole—\""
    else:
        hide hrm_kasim
        show hrm_brask earnest at vn_cast_slot
        hrm_brask "\"And then there was a girl on the harem balcony, blowing me a kiss, and I lost my place in the whole—\""
    hrm_dahlia "\"Was she pretty, Captain?\""
    hide hrm_kasim
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"...Very, my lady.\""
    "Dahlia has to sit down on the steps again."
    hide hrm_brask
    jump hrm_festival
