## THE STORY: chapters 0-2 (PLAN.md). Spring Eve, the dance and the bargain; Saturday the wine-house cellar; Sunday Senna.
## dnc.held counts Aren's stands, dnc.asked the times he gives in; they only change a line or two.

## ---- 0. Spring Eve -------------------------------------------------------------------------------------------

label dnc_festival:
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_temple_hill", pc="stern", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer")], cg="dnc_spring_eve")
    "Spring Eve on Hollin hill."
    "The whole town has climbed up after dark with lanterns and wine-skins and blankets, and the slope below the Temple of the Veil is a field of little lights."
    "You're at the court gate in your white tabard with your sword on your hip, where a temple guard stands every Spring Eve, and you're not watching the crowd. You're watching her."
    "Lys. Twenty-two, the temple's dancer since she was nineteen, and the woman you've been working up the nerve to marry since the winter."
    "She's in the dancer's silks tonight: seven veils in seven shades of rose, bells at her ankles, her black curls pinned up off her neck, her brown shoulders bare to the cold."
    dnc_lys "\"Stop staring, Aren. You'll put me off my count.\""
    dnc_you "\"You've never lost your count in your life.\""
    dnc_lys "\"There's a first time for everything. Kiss me for luck.\""
    "You kiss her for luck, quick, in the shadow of the gate, and she tastes of the honey wine the merchants' guild sends up every year for the dancer. Corvin Hale's wine."
    "He sends the best."
    "Under the hill, everyone in Hollin knows, something sleeps. The old rolls call it Ysmeral."
    "Once a year the dancer dances the seven figures of the Sealing Dance on the stone court above it, and it sleeps another year, and the harvest comes in and nobody's daughter walks into the river with a strange look on her face."
    "That's the story. You've stood guard at it five times. You know every step of the dance by heart, from watching."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="dnc_dance_court", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer"), ("dnc_senna", "mage")], cg="dnc_first_figures")
    "The drums start at nine. The court is ringed with lamps, and in the ring stands the hired ward-mage from the capital, Senna Dray:"
    "twenty-six, tall, ash-blonde hair cropped short, a navy coat with silver at the cuffs, holding the ward line taut with both hands, so the hill's breath can't get out while the seal is open."
    "Lys dances. The first figure, the second, the third. The lamps burn steady and gold. The fourth."
    "The fifth, the hard one, the turn on one heel with all seven veils flying, and she makes it, and the crowd sighs."
    "Then she stumbles."
    "She puts a hand to her forehead. She looks at you across the court, puzzled, the way you look at someone when the floor tips."
    "And she goes down on the stone in a heap of rose silk, and the lamps flicker, and every flame in the ring turns blue."
    dnc_senna "\"The seal's open! Somebody has to finish it — the figures can't stop at five, it'll come up through the gap—\""
    "The ground hums under your boots. The crowd has gone silent. Lys is breathing, but her eyes are rolled up and her lips are sticky with wine."
    menu:
        "Two figures left, and you're the only one in Hollin who knows them besides her."
        "Take up her veils":
            "You don't think. You're across the court, kneeling, unwinding the veils from her shoulders, winding them round your own, pulling the bells off her ankles and onto yours."
        "Call for the priestess":
            "You shout for Mother Aud."
            "She's eighty-one and she's at the bottom of the hill, and she'll never get up it in time, and the ground hums louder, and you're already unwinding the veils from Lys's shoulders and onto your own before you've finished shouting."
    show cg dnc_aren_dances onlayer cgl
    "And you dance."
    "The sixth figure, the slow one: arms up, the veils lifting, a long turn round the court with your bare feet on the cold stones. You're too big for it."
    "Your shoulders are too wide for the silk and your feet are too heavy for the bells. But you know it, you know every step, and the blue lamps flicker back towards gold as you go."
    "The seventh figure. The kneel, the reach, the press of both palms flat to the stone over the thing under the hill."
    "The stone is warm. Then hot. And something under your hands says, in no voice at all, {i}a daughter of the Veil, a daughter of the Veil, this is not a daughter{/i}."
    vn_sfx "Vwoom."
    "Light goes up out of the court, rose-coloured, in a column, and comes down again on three people: on you, on Lys where she lies, and on Senna at the ward line."
    "{color=#ff5fb8}It lands low on your belly, under your tabard, under your navel, and it sinks in like heat into a stone, and when the light goes out you can feel it there: a mark, warm, alive, a sigil like a heart with thorned wings, glowing rose-gold through the cloth.{/color}"
    dnc_senna "\"It held. It's asleep. The seal held, but it — oh. Oh, no. Aren, lift your shirt.\""
    $ vn_set_time(23, 30)
    $ vn_enter(bg="dnc_temple_cell", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_bargain")
    "Later, they carry Lys to the infirmary, where she sleeps it off with the same mark on her own belly. Senna has one too."
    "She locks herself in the archive with the old rolls and won't come out."
    "And at half past eleven, there's a knock on the door of your cell in the guards' row, and it's Corvin Hale."
    "Forty-odd, grey at the temples, a neat grey beard, a plum doublet with good silver rings on every finger. Hollin's wine merchant. The man who sent the dancer's wine."
    dnc_corvin "\"Sword-brother Vale. May I come in? Thank you. What a night. I've never seen the sixth figure danced better, and I've seen thirty Spring Eves.\""
    dnc_you "\"You drugged her.\""
    dnc_corvin "\"I did, yes. I hoped the seal would fail. Instead you did something much more interesting. You see, there are a few of us in Hollin who'd rather the thing under the hill were awake.\""
    dnc_corvin "\"We call ourselves the Unveiled. We know its name. And you, sword-brother, are now wearing it.\""
    "He says it. Softly, like a man calling a dog."
    dnc_corvin "\"{b}Ysmeral.{/b}\""
    vn_sfx "Dokun."
    "{color=#ff5fb8}The mark on your belly flares hot, and your knees go, and you're on the floor of your own cell with your forehead nearly on his boots, and your whole body is one long ache, low and hungry, as if something in you has been empty all your life and only just noticed.{/color}"
    dnc_corvin "\"There it is. The crest answers whoever speaks the name. Yours, Senna's — and Lys's. The Unveiled will want a dancer, every night until the new moon, in my cellar.\""
    dnc_corvin "\"Who it is, I leave to you.\""
    menu:
        "Lys is asleep in the infirmary with the same mark on her. He's waiting."
        "Take her place":
            dnc_you "\"Me. You'll have me. Not her. You don't touch her. None of you touch her.\""
        "Draw your sword":
            "Your hand goes to the hilt. You get it half out of the scabbard before he says the name again, quietly, and your fingers open on their own, and the sword rings on the flagstones."
            $ dnc.held += 1
            dnc_you "\"...Me. Not her. You don't touch her.\""
    dnc_corvin "\"Done. Nobody lays a finger on her while the dancer keeps dancing. You've my word, and I keep it: it's good for business.\""
    dnc_corvin "\"And since you're the dancer, we might as well begin. {b}Ysmeral. Open your mouth.{/b}\""
    show cg dnc_first_kneel onlayer cgl
    "Your mouth opens."
    "He unlaces himself without hurry and feeds you his cock, thick and heavy and warm, and the crest burns brighter as it slides over your tongue, and the hunger under it says {i}yes, this, this is what the empty place is for{/i}."
    vn_sfx "Juppu. Juppu."
    "You've never done this. Your body does it anyway."
    "Your lips seal round him and your head bobs and your tongue works, and he holds your hair in his ringed fingers, and you can hear yourself, wet, eager, making sounds you've never made."
    dnc_you "\"Mmph♡— mmh— mmmh♡—\""
    dnc_corvin "\"Good. Very good. Swallow.\""
    vn_sfx "Dopyu."
    "And he comes, and you swallow, and the crest drinks it, you feel it drink, a hot bright pulse under your navel, and your own cock jerks in your breeches and you come too, untouched, kneeling on the stone with your mouth full."
    dnc_you "\"Hah♡— hahh♡—!\"" with vnfx("flash", "shake")
    dnc_corvin "\"Tomorrow, the cellar. Nine o'clock. Wear her veils.\""
    call dnc_cut(7, 1, "Saturday. The first morning.")
    jump dnc_saturday

## ---- 1. Saturday: the cellar ---------------------------------------------------------------------------------

label dnc_saturday:
    $ dnc.fit = "shift"
    $ dnc_grow(1)
    $ vn_enter(bg="dnc_temple_cell", pc="nervous", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_saturday")
    "{color=#ff5fb8}The shaving mirror is the first thing that's wrong. There's nothing to shave. Your jaw is smooth, all of it, and softer at the corners, and your lips are fuller than they were.{/color}"
    "{color=#ff5fb8}The hair's gone from your chest and your arms. Your shoulders sit narrower in your sleeping shift.{/color}"
    "{color=#ff5fb8}Your hair has grown over your ears overnight, dark brown, and at the roots, where it parts, it's turned a colour hair isn't supposed to be: rose gold, the colour of the crest.{/color}"
    "The crest's still there under your navel. Warm. Not glowing now. Waiting."
    $ vn_set_time(9, 30)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_archive", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_senna", "mage")], cg="dnc_archive_rolls")
    "Senna's in the archive with a dozen old rolls weighted open on the long table, and dark rings under her eyes."
    "She looks at your face for a long second when you come in, and then at your hair."
    dnc_senna "\"So it's started on you. It would, you'd be first. Sit down. Don't make me say it twice, I've barely slept.\""
    dnc_senna "\"The Sealing Dance is danced by a daughter of the Veil. That's the rite's own words.\""
    dnc_senna "\"You finished it, and you're not a daughter, so the seal took what it needed out of the overflow and wrote it on the dancers. It's making one. Out of you.\""
    dnc_senna "\"A step every time the crest is fed.\""
    dnc_you "\"Fed?\""
    dnc_senna "\"Every time you come, Aren. I'm sorry. I didn't write the thing.\""
    "Her ears are red. She's staring hard at the roll in front of her."
    dnc_senna "\"By the new moon, seven nights, it'll be finished. What it'll be finished as depends who holds the name. I'm looking for a way out. Give me time.\""
    $ vn_set_time(12, 0)
    $ vn_enter(bg="dnc_infirmary", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer")], cg="dnc_lys_wakes")
    "Lys is awake at noon, sitting up in the infirmary bed with a cup of broth, a hand pressed flat to her belly where her own crest is."
    dnc_lys "\"Aren. Senna says you danced the last two. In my veils.\" She looks at your face. \"Aren, what's happened to you?\""
    menu:
        "She's going to find out, one way or another."
        "Tell Lys the truth":
            "You tell her. All of it: the wine, Corvin, the name, the bargain, your knees on the floor of your cell. She listens with her hand over her mouth."
            dnc_lys "\"You traded yourself. For me. You idiot. You lovely idiot.\""
            dnc_lys "\"Then I'll be at the gate when you come back. Every night. And don't you dare be ashamed in front of me.\""
            $ dnc.held += 1
        "Hide it from Lys":
            dnc_you "\"It's the seal. Senna's working on it. Don't worry. Rest.\""
            "She looks at your soft jaw and your rose-gold roots and doesn't believe a word, and doesn't make you say it."
            dnc_lys "\"All right. But I'll be at the gate when you come back, wherever you're going.\""
    $ vn_set_time(21, 0)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_cellar", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant")], cg="dnc_cellar_dance")
    "The cellar under Corvin's wine house is long and low and vaulted, lined with barrels, lit with red-glassed lamps."
    "Seven men sit along the barrel-ends with cups: the cooper, the ferryman, the miller's two sons, men you've nodded to in the street every day for five years."
    "And you, in the middle of the floor, in Lys's seven veils, with her bells on your ankles. Nothing under them."
    dnc_corvin "\"The dancer, gentlemen. {b}Ysmeral. Dance.{/b}\""
    "{color=#ff5fb8}The crest lights up rose-gold through the silk, and your body dances. All seven figures, the whole sealing dance, in a wine cellar, for seven men. One veil comes off at every figure. Your hips are already rolling on the turns in a way they never did on the court.{/color}"
    "By the seventh figure you're naked but for the bells, and hard, and the crest is glowing so bright the men's faces are pink with it."
    show cg dnc_cellar_table onlayer cgl
    dnc_corvin "\"On the table, please. On your front.\""
    "The tasting table. Cool oak under your chest. Corvin's oiled thumb at your arse, circling, pressing, and the crest pulsing in time with it."
    menu:
        "He's going to take you, here, in front of all of them."
        "Fight the crest":
            "You fight it."
            "You plant your hands and try to push up off the table, and your arms shake with the effort, and Corvin says the name, gently, and your arms fold, and your hips tip up on their own to meet him."
            $ dnc.held += 1
        "Let it carry you":
            "You let the crest carry you. It's easier. It's so much easier. Your back arches and your knees part and you hear yourself moan before he's even inside."
            $ dnc.asked += 1
    vn_sfx "Zupuu."
    dnc_you "\"Ahh— AHH— it's— it's in— it's so thick—!\""
    "He goes in slow, all the way, and holds there, and the crest flares, and the stretch melts into heat. Then he starts to move. Long strokes. His ringed hands on your hips."
    "Every stroke grinds over a place deep inside you that makes the whole room go white at the edges."
    vn_sfx "Pan. Pan. Pan."
    dnc_you "\"Ah♡— ahh♡— there— why does it— why does that feel— ahh♡— AHH♡—!\""
    "The men are watching. You know they're watching. You can't stop being loud."
    dnc_you "\"I'm coming, I'm coming from— from your cock— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu."
    "He comes deep inside you, and your crest drinks that too, and you spill onto the tasting table without being touched, shaking, with seven men raising their cups."
    $ vn_set_time(23, 50)
    $ vn_enter(bg="dnc_temple_hill", pc="dazed", pc_tag="dnc_pc", cast=[("dnc_lys", "dancer")], cg="dnc_gate_lys")
    "Lys is at the court gate when you come back up the hill, with a lantern and a blanket, the way she said."
    "She wraps you in it without a word and walks you to your cell with her arm round your waist."
    call dnc_cut(7, 1, "Sunday. The second morning.")
    jump dnc_sunday

## ---- 2. Sunday: Senna -----------------------------------------------------------------------------------------

label dnc_sunday:
    $ dnc.fit = "shift"
    $ dnc_grow(2)
    $ vn_enter(bg="dnc_temple_cell", pc="flustered", pc_tag="dnc_pc", cast=[], cg="dnc_mirror_sunday")
    "{color=#ff5fb8}Your shift hangs differently. Your waist has come in, a curve now between ribs and hips, and when you touch your chest it isn't flat: there's a softness there, puffy and tender, a soft swell round each nipple that aches when the linen brushes it.{/color}"
    "{color=#ff5fb8}You make yourself look down. Your cock is smaller. Not much. Enough. Your hair brushes your chin now, and half of it's rose gold.{/color}"
    $ vn_set_time(8, 0)
    $ dnc.fit = "guard"
    $ vn_enter(bg="dnc_archive", pc="nervous", pc_tag="dnc_pc", cast=[("dnc_senna", "mage")], cg="dnc_senna_reveal")
    "Senna's waiting in the archive with the door bolted, and her navy coat buttoned to the throat, and her face bright red."
    dnc_senna "\"Don't laugh. I'm only showing you because you're the only person in Hollin who'll understand.\""
    "She unbuttons the coat. Under it, under her skirt, pushing up hard against the cloth: a cock. Long, thick, flushed, with her crest glowing just above it like a brand of rose light."
    dnc_senna "\"I woke up with it. I held the ward line, and the overflow came down on me too, and it decided — I don't know what it decided. It's been like this since five o'clock.\""
    dnc_senna "\"It won't go down. I can't think.\""
    menu:
        "She's shaking. She's trying very hard to sound like a professional."
        "Stay with Senna":
            "You sit down next to her on the archive bench and you don't look away, and you don't laugh. You just stay. After a while she stops shaking."
            dnc_senna "\"...Thank you. I'll find us a way out of this. Both of us. All three.\""
            $ dnc.held += 1
        "Give her privacy":
            "You turn your back and look at the shelves while she buttons up again with clumsy fingers. Neither of you says anything. It doesn't help, but it's kind."
    $ vn_set_time(21, 0)
    $ dnc.fit = "dancer"
    $ vn_enter(bg="dnc_wine_cellar", pc="flustered", pc_tag="dnc_pc", cast=[("dnc_corvin", "merchant"), ("dnc_senna", "mage")], cg="dnc_cellar_senna")
    "And at nine, when you come down the cellar steps in Lys's veils, Senna's already there."
    "Standing at the far end between the barrels in her navy coat, with her hands clenched at her sides and her face white."
    dnc_corvin "\"Our ward-mage came to tell me she'd find a way to break my crests. I thought she'd better see what they're for. {b}Ysmeral.{/b} Mage, the dancer. Take her.\""
    "{color=#ff5fb8}Both crests flare at once, yours and hers. You see her step forward with her eyes wide and her hands already at her buttons. You feel your own knees go, your body folding forward over the barrel in front of you, your arse lifting under the silk.{/color}"
    dnc_senna "\"I'm sorry— Aren, I'm so sorry, I can't— my hands won't—\""
    show cg dnc_senna_takes onlayer cgl
    "Her cock is hot and heavier than Corvin's, and she's never used it, and she pushes into you all at once with a cry that's half apology and half something else."
    vn_sfx "Zuchu."
    dnc_senna "\"Oh— oh gods— it's so tight— it's so warm, Aren, I'm sorry, it feels so— hahh♡—\""
    menu:
        "She's moving. She doesn't know how to stop. Neither do you."
        "Beg Senna to stop":
            dnc_you "\"Senna— Senna, stop— please, please stop, I— ahh♡— no, don't stop— don't— AH♡—\""
            "It turns over in your mouth halfway through the word. The crest turns it. You hear the men laugh."
            $ dnc.held += 1
        "Let Senna go on":
            dnc_you "\"It's all right— it's all right, Senna, it's not you— go on— ahh♡— go on, don't hold back—\""
            "She lets out a long, shaky breath, and lets go, and starts to thrust properly, hard and fast."
            $ dnc.asked += 1
    vn_sfx "Pan. Pan. Pan. Pan."
    dnc_senna "\"Aren— Aren, I'm going to— inside— I can't pull out— the crest won't let me—\""
    dnc_you "\"Do it♡— do it, I'm— I'm coming too— Senna♡— AHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu. Dopyu."
    "She comes buried in you with her forehead on your back, and you come against the barrel, and both crests drink."
    "Afterwards, she helps you up the hill, both of you limping. She doesn't speak until the court gate, where Lys is waiting with the lantern."
    dnc_senna "\"I'll find it. I swear I'll find it.\""
    call dnc_cut(6, 1, "Monday. The third morning.")
    jump dnc_monday
