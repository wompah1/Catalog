## THE STORY: chapters 0-2, Saturday to Monday (written 2026-11-17; PLAN.md). One bite a night; one body step and one hair
## step each morning (mrn_grow before the morning's first vn_enter). Chapters 3-5 are in scenes.rpy; 6, 7 and the endings in
## finale.rpy. Second person. No pussy before Tuesday morning. Orders from Chris are in bold; the bond can't refuse them.
## Maron's own lines use mrn_maron (her plate), Mitsuru's use mrn_you; mrn.maron counts her surfacings, mrn.held his stands.

## ---- 0. Saturday: whiteout ------------------------------------------------------------------------------

label mrn_whiteout:
    $ mrn.fit = "hiking"
    $ vn_enter(bg="mrn_ridge", pc="nervous", pc_tag="mrn_pc", cast=[], cg="mrn_ridge_whiteout")
    "The ridge above Hakuba, the last Saturday before the lifts open, and the whiteout came down an hour ago like someone dropping a sheet over the world."
    "You're [mrn_pc_name] Yokomizo, twenty-three, two years into a desk job at a shipping firm in Yokohama, and this was supposed to be the trip that proved you could do something on your own."
    "One night in the hut. Back down by Sunday lunch."
    "The trail markers stopped three markers ago. Your phone died at minus nine."
    "Your boots are full of snow and your thighs have stopped shivering, which the guidebook said was the bad sign."
    vn_sfx "Fwoooo."
    mrn_you "\"Okay. Okay. Downhill. Just keep going downhill.\""
    "You keep going downhill. And then, between one step and the next, the wind stops."
    $ vn_set_time(17, 20)
    $ vn_enter(bg="mrn_pines", pc="dazed", pc_tag="mrn_pc", cast=[], cg="mrn_pines_edge")
    "The snow ends. Not thins out: ends, in a straight line at your feet, as if somebody had cut it with scissors."
    "Beyond it there's a forest of tall black pines, dry needles on the ground, the air soft and still and smelling of resin and something sweet, like roses left too long in a vase."
    "Behind you the whiteout roars on, a wall of white. In front of you, the moon's out. There was no moon a minute ago."
    "Through the trunks, a long way in, a window glows yellow."
    "Your legs decide before you do."
    $ vn_set_time(17, 50)
    $ vn_enter(bg="mrn_gate", pc="nervous", pc_tag="mrn_pc", cast=[], cg="mrn_gate_house")
    "A house."
    "A big Western house, the kind they built for foreign merchants in the Meiji years, three storeys of dark timber and pale stone with a slate roof and tall windows, sitting in a clearing in the pines as if it had always been there."
    "An iron gate, open. A path of white gravel. A front door with a brass knocker shaped like a bat with its wings folded."
    menu:
        "Your hands are too cold to feel the gate."
        "Knock":
            "You lift the bat and let it fall. The sound goes into the house and comes back a long time later, as if the house were much bigger inside."
            vn_sfx "Konk. Konk."
        "Shout for help":
            mrn_you "\"Hello? Hello! I'm lost, I'm— is anyone there? Please!\""
            "Your voice is thin and cracked and it doesn't echo. The pines eat it."
            $ mrn.held += 1
    "The door opens before you've finished."
    $ vn_enter(bg="mrn_gate", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_gate_kanon")
    "A woman stands in the doorway with a lamp. Tall, taller than you, in a long black maid's dress with a high white collar and an apron so white it looks blue in the moonlight."
    "Black hair in a heavy knot at the back of her neck."
    "A grown woman's face, calm and handsome and maybe twenty-eight, and eyes the colour of a glass of red wine held up to a candle."
    mrn_kanon "\"A traveller. In this weather. You'd better come in before you die on the step; the mistress hates a mess.\""
    mrn_you "\"Th— thank you. I'm sorry. I'm Yokomizo, I got lost on the—\""
    mrn_kanon "\"I'm Kanon. Boots off in the hall. Don't touch the roses.\""
    $ vn_set_time(18, 30)
    $ vn_enter(bg="mrn_hall", pc="flustered", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_hall_stairs")
    "The hall is warm."
    "Dark panelling, a staircase sweeping up into shadow, a fire in a stone fireplace big enough to stand in, and vases of deep red roses everywhere, every table, every sill."
    "And on the stairs, coming down slowly with one hand on the banister, the mistress of the house."
    "She's maybe twenty-five. Pale as milk, with long silver-blonde hair loose to her hips and a dress of wine-red velvet cut low and square across a full, high bust."
    "Her eyes are the same red as Kanon's, but brighter, like the wine has caught fire."
    mrn_chris "\"Kanon. You found me a present.\""
    mrn_kanon "\"It knocked, Chris. I only opened the door.\""
    mrn_chris "\"I'm Christiane von Ahrenfeld. Everyone calls me Chris, and so will you. And you're cold right through, poor thing. Kanon, a bath. Then dinner.\""
    "She stops on the bottom step, so her eyes are level with yours, and looks at your throat for a moment longer than she looks at your face."
    $ vn_set_time(20, 0)
    $ mrn.fit = "robe"
    $ vn_enter(bg="mrn_dining", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_dining_table")
    "An hour later you're warm for the first time since noon, in a borrowed black silk robe that's a little long in the sleeve, at the end of a dining table set for twelve, eating the best beef stew of your life."
    "Chris doesn't eat. She sits at the head of the table with a glass of something dark and watches you over the rim. Kanon stands behind her chair with her hands folded."
    mrn_you "\"Is there a phone? A road? I should let someone know I'm—\""
    mrn_chris "\"There's no road. The snow never comes into my forest, and nothing goes out of it unless I say. Have some more wine.\""
    mrn_you "\"Your forest?\""
    mrn_chris "\"For three hundred years, give or take. Kanon came in with the snow, too, in eighteen ninety-one. She looked a lot like you. Lost. Pretty under the frost.\""
    "Kanon doesn't smile, but something moves at the corner of her mouth."
    mrn_chris "\"I'll be honest with you, Yokomizo-san. I'm bored, and I'm thirsty, and you've walked a very long way to my door. Stay the winter.\""
    mrn_chris "\"I'll keep you warm and fed, and in return, you'll keep me company.\""
    menu:
        "Her eyes never leave your throat."
        "Accept her hospitality":
            mrn_you "\"That's— very kind. Just till the weather clears. Thank you, Chris-san.\""
            mrn_chris "\"Just Chris. And you're welcome. You've no idea how welcome.\""
        "Ask to leave at dawn":
            mrn_you "\"I'm grateful, really, but I'll go at first light. People will be looking for me.\""
            mrn_chris "\"Will they? How lovely for you.\""
            "She says it so kindly that it takes you a moment to understand it wasn't a question."
            $ mrn.held += 1
    $ vn_set_time(23, 55)
    $ mrn.fit = "nude"
    $ vn_enter(bg="mrn_guestroom", pc="dazed", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_guest_bite")
    "The guest room has a bed with four posts and a canopy, and you sleep the second your head touches the pillow, and you wake again at five to midnight because there's someone sitting on the edge of the bed."
    "Chris, in a white nightgown, her silver hair over one shoulder, her hand flat on your bare chest. Her hand is cool. Your heart's going so hard you're sure she can feel it."
    mrn_chris "\"Shh. Don't get up. Look at me.\""
    "You look at her. It's like falling into a glass of wine."
    mrn_chris "\"You're going to be mine, Mitsuru.\""
    mrn_chris "\"I'm going to drink a little of you every night, and every night a little more of you will be mine, and by next Saturday there'll be nothing left of that cold, lost salaryman that isn't mine.\""
    mrn_chris "\"Do you understand?\""
    mrn_you "\"N— no, I— what are you—\""
    "She leans down. Her hair falls across your face like a curtain. Her mouth finds the side of your throat."
    vn_sfx "Tsupu."
    "Two small, bright points of cold, and then heat."
    "Heat pouring out of you and into her, a long, slow, sweet pull, and every pull goes straight down your spine and between your legs. You're hard."
    "You're rock hard under the sheet, against her thigh."
    mrn_you "\"Ahh— what— ahh— that's— why does it feel—\""
    mrn_chris "\"Mm. Because you're mine now. It always feels good to give me what's mine.\""
    "She lifts her head, licks the two little marks closed with one stroke of her tongue, and tucks the sheet up under your chin like a nurse."
    mrn_chris "\"Sleep, Mitsuru. Tomorrow's your first day.\""
    "You sleep. You can't not."
    call mrn_cut(8, 1, "Sunday. The first morning.")
    jump mrn_sunday

## ---- 1. Sunday: the name -------------------------------------------------------------------------------------

label mrn_sunday:
    $ mrn.fit = "nude"
    $ mrn_grow(1)
    $ vn_enter(bg="mrn_guestroom", pc="nervous", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_sunday")
    "There's a long mirror on the wardrobe, and the man in it is wrong."
    "{color=#ff5fb8}Not by a lot. Your face is softer, the jaw rounder, your lashes longer and darker than they've ever been.{/color}"
    "{color=#ff5fb8}Your skin's gone pale as the moon, every hair on your arms and chest and legs simply gone in the night. Your shoulders are narrower.{/color}"
    "{color=#ff5fb8}Your black hair has grown down over your ears, and at the roots, where it parts, there's a warm brown, like chestnut.{/color}"
    "{color=#ff5fb8}Your borrowed pyjama bottoms pool round your feet. You've lost a hand's width of height overnight, you're sure of it: the door handle's higher than it was.{/color}"
    "{color=#ff5fb8}Between your legs everything's still there, and still yours, but it looks smaller than you remember, and very pale.{/color}"
    mrn_you "\"What did she do. What did she {i}do{/i} to me.\""
    "On your neck, two neat pink marks, already healing."
    $ vn_set_time(9, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_parlour", pc="protesting", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_parlour_uniform")
    "Your hiking clothes are gone from the chair."
    "In their place, laid out by somebody who knew your new size better than you do: a black maid's dress, short-sleeved, the skirt to mid-thigh, a white apron with a frilled hem, white stockings, a garter belt, a headband of white lace."
    "And a pair of silk knickers."
    "You put them on because there is nothing else in the room to put on, and you come downstairs holding the skirt down at the front with both hands."
    mrn_chris "\"Oh, look at you. Kanon, look. I told you it would fit.\""
    mrn_kanon "\"It fits. It'll need taking in by Tuesday.\""
    mrn_you "\"Give me my clothes back. I want my clothes and my boots, and I want to know what you did to me last night.\""
    mrn_chris "\"I made you my blood-kin. My blood's in you now, and yours is in me, and that makes you my sister, as far as anything in this forest is concerned. My imouto.\""
    mrn_chris "\"And since you're my imouto, you'll want a proper name.\""
    "She tilts her head and looks at the chestnut coming through your roots."
    mrn_chris "\"Maron. Like the chestnut. That's what you're turning into, imouto: something sweet under a shell.\""
    menu:
        "She's waiting for you to say it."
        "Say your real name":
            "You set your jaw. Two years of bad bosses and you never once said this to anyone's face."
            mrn_you "\"My name is Mitsuru Yokomizo. I'm not your sister and I'm not your maid and I'm not—\""
            mrn_chris "\"{b}Tell me your name.{/b}\""
            "It goes into you like the bite did. It doesn't hurt. It just takes hold, low in your chest, where the warm pull was last night, and turns you like a key."
            mrn_you "\"Maron.\""
            "You hear yourself say it. Your mouth's still open on the shape of it. {i}No. That's not— I didn't—{/i}"
            $ mrn.held += 1
        "Answer to Maron":
            "There's something low in your chest, warm, that wants you to say it. You don't know how you know. You only know it would feel very good to say it, and very bad not to."
            mrn_you "\"...Maron.\""
            mrn_chris "\"Good girl. That wasn't hard.\""
            "The warm thing in your chest purrs like a cat. You hate it."
    mrn_chris "\"That's the bond, Maron. When I tell you something out loud, you do it. You won't be able not to.\""
    mrn_chris "\"So I'll be careful what I say, and you'll be careful to be good, and we'll all be very happy. Now. {b}Obey Kanon as you'd obey me.{/b} She'll teach you the house.\""
    mrn_kanon "\"Kitchen. Now. Walk, don't stomp; you're a maid, not a bear.\""
    $ vn_set_time(11, 30)
    $ vn_enter(bg="mrn_kitchen", pc="flustered", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_kitchen_lesson")
    "Kanon is a hard teacher and a fair one. Black tea for the mistress: Assam, the pot warmed first, four minutes exactly."
    "Silver polished with a soft cloth in the direction of the grain. Floors on your knees, the brush in circles."
    "Every time you bend, the short skirt rides up over the white stockings and you feel the cold air of the house on the backs of your thighs."
    mrn_kanon "\"Curtsey. Hold the skirt at the hem, not the hips. Lower. Lower. Eyes down. Now say it.\""
    mrn_you "\"...Yes, Kanon-neesan.\""
    mrn_kanon "\"Better. You'll say it like you mean it by Wednesday.\""
    "She steps behind you to straighten your apron bow, and her hands linger on your waist, measuring it with her thumbs. She's very tall."
    "The front of her black dress brushes your back, and for a moment you could swear something under her skirt presses against you, heavy and warm, before she steps away."
    $ vn_set_time(23, 30)
    $ vn_enter(bg="mrn_chris_room", pc="moaning", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_lap_bite")
    "At half past eleven Kanon brings you to Chris's room, a big round room in the tower with a bed like a ship and red velvet everywhere, and leaves you there in your uniform."
    mrn_chris "\"{b}Come and sit in my lap, Maron.{/b}\""
    "You go and sit in her lap. Your legs carry you across the carpet and fold you down sideways across her knees, and you can't do anything but watch them do it."
    "She pushes the lace headband back off your hair and bares your neck with two fingers, gently, like turning the page of a book."
    "Her other hand settles on your thigh, above the stocking top, on bare skin."
    vn_sfx "Tsupu."
    "The bite, and the heat, and the pull."
    "And this time her hand moves while she drinks, up under the short black skirt, into the silk knickers, and finds your cock already hard and aching, smaller than yesterday, and wraps it in cool fingers."
    vn_sfx "Shk. Shk. Shk."
    mrn_you "\"Ahh— Chris— don't— ahh— not there, not while you're— hahh— hahh—\""
    "Every pull at your throat and every stroke of her hand meet somewhere in your belly and wind tighter and tighter. Your hips are moving. Your toes curl in the white stockings."
    mrn_you "\"I'm going to— I'm— please, I'm going to—\""
    mrn_chris "\"{b}Don't come.{/b}\""
    "Your body stops at the edge like a dog hitting the end of its leash. It doesn't go over. It can't."
    "The pleasure piles up and up against the order like water against a door, and she keeps stroking."
    mrn_you "\"Ahh— AHH— let me— oh God, let me, please, it's too much— please—\""
    menu:
        "Her hand doesn't slow down. Neither does her mouth."
        "Beg her":
            mrn_you "\"Please— Chris— please, please let me come, I'll do anything— anything—\""
            mrn_chris "\"That's not my name tonight, is it?\""
            mrn_you "\"...O— Onee-sama. Please, Onee-sama.\""
            mrn_chris "\"So sweet. No.\""
        "Grit your teeth":
            "You bite your lip and shut your eyes and hold on. You won't beg her. You won't give her that."
            "She laughs against your throat, a soft wet laugh, and slows her hand down to the cruellest crawl there is, and holds you there on the edge till your whole body is shaking in her lap."
            mrn_you "\"Hnn— hnnn— ahh— ahhh—!\""
            $ mrn.held += 1
    "She stops. She licks the marks closed. She takes her hand out of your knickers and wipes it, very daintily, on your apron."
    mrn_chris "\"There. That's what you'll be thinking about all night instead of the snow. Go to bed, imouto.\""
    "You lie in the dark in the big guest bed with your cock throbbing and your neck warm and the order still holding you, and every time your hand drifts down the bond says {i}don't{/i}, softly, like a hand on your wrist."
    call mrn_cut(8, 1, "Monday. The second morning.")
    jump mrn_monday

## ---- 2. Monday: duties ----------------------------------------------------------------------------------------

label mrn_monday:
    $ mrn.fit = "nude"
    $ mrn_grow(2)
    $ vn_enter(bg="mrn_guestroom", pc="flustered", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_monday")
    "{color=#ff5fb8}The mirror again. Another hand's width of height gone: your eyes are where your mouth used to be. Your hair's down to your chin now, black and chestnut together, like a fire burning through the dark. Your waist goes in. It never used to go in.{/color}"
    "{color=#ff5fb8}And your chest. Two soft swells, small, round, sitting high on your ribs, tipped with nipples that have gone pink and puffy and so sensitive the air makes you shiver.{/color}"
    "{color=#ff5fb8}You cup one and your knees go weak. Below, your cock's shrunk to the length of your thumb, soft and pale and almost hairless, like something left over.{/color}"
    mrn_you "\"Okay. Okay. Five more. Five more and then there's nothing left of me. That's what she said.\""
    "Your voice has gone up. Not much. Enough."
    $ vn_set_time(10, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_laundry", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_laundry_lesson")
    "The laundry is down in the cellar, stone-flagged, warm from the copper, full of steam and the smell of starch. Kanon has her sleeves rolled up. Her forearms are pale and strong."
    mrn_kanon "\"The mistress says today you learn the rest of your duties. The ones a maid does with her body.\""
    mrn_you "\"I'm not— I don't want to learn anything from—\""
    mrn_kanon "\"No, you don't. That's why she ordered you to obey me. {b}Strip, Maron. Uniform on the table, folded.{/b}\""
    "It isn't Chris's voice, but the bond doesn't care. You watch your hands untie the apron and unbutton the dress and fold them, neatly, the way she taught you yesterday."
    "You stand on the warm flags in the white stockings and nothing else, your hands trying to cover your new breasts and your shrunken cock at the same time."
    mrn_kanon "\"Hands at your sides. I said once; I won't say it twice.\""
    "Then she lifts her own long black skirt with both hands, and you see what was pressing against you yesterday."
    "Kanon is a woman, every inch of her, and between her strong pale thighs she has a cock."
    "A big one, long and thick and already half hard, heavy against her thigh, a grown man's cock on a grown woman's body, under a full black bush."
    mrn_kanon "\"Chris didn't do this to me. I came to the house with it. She liked it, so she kept me.\""
    menu:
        "It's twice the size yours ever was."
        "Look away":
            "You turn your face to the wall. Your cheeks are burning."
            mrn_kanon "\"Shy. That won't last.\""
            $ mrn.held += 1
        "Keep looking":
            "You can't stop looking. It's so much bigger than yours."
            "It's so much bigger than yours ever was, even before, and something low in your belly gives a slow, warm, shameful turn."
            mrn_kanon "\"Yes. Look all you like, imouto.\""
    show cg mrn_laundry_bent onlayer cgl
    mrn_kanon "\"{b}Bend over the table.{/b}\""
    "Your body bends over the laundry table, your cheek on the folded uniform, your new small breasts pressed flat on the starch. Kanon's oiled fingers are cool and patient."
    "One, slowly, into your arse, till you're gasping. Then two, curling, finding something inside you that makes your shrunken cock twitch and drip."
    vn_sfx "Nyuru. Nyuru."
    mrn_you "\"Ahh— ah— Kanon-neesan— what— what is that— ahh, don't, not there—\""
    mrn_kanon "\"That's where a maid gets taken until she has somewhere better. Breathe out.\""
    show cg mrn_laundry_anal onlayer cgl
    "Then the fingers are gone and the head of her cock is there instead, broad and hot and slick, and she pushes, slow and steady, and you open around her in one long, stretching, impossible slide."
    vn_sfx "Zupuu."
    mrn_you "\"AHH— it's— it's so big— it's all the way— it's {i}all the way in{/i}— ahh♡—\""
    "She starts to move. Long, slow strokes, all the way out and all the way in, her strong hands on your new waist, holding you down on the table."
    "Every stroke drags over that place inside you and your shrunken cock slaps soft and useless against the table edge."
    vn_sfx "Pan. Pan. Pan."
    mrn_you "\"Hah— hah— don't— don't stop— I mean— I mean stop— I mean— ahh♡— ahh♡—\""
    mrn_kanon "\"Listen to you. You don't know what you mean.\""
    "She speeds up. The table creaks. The steam from the copper hangs round the two of you and your noises bounce off the cellar's stone, higher and higher and louder."
    mrn_you "\"It's coming— something's coming— it's not like before, it's {i}different{/i}— Kanon-neesan— Kanon-neesan♡— AHH♡—!\"" with vnfx("flash", "shake")
    "It isn't coming. Not the way you knew it."
    "It starts deep inside, where she's pressing, and rolls outward in waves, and your shrunken cock just leaks a thin warm trickle onto the flags without ever getting hard."
    "Your whole body clenches round her and she groans and you feel her spill inside you, hot and thick, pulse after pulse."
    vn_sfx "Dopyu. Dopyu."
    $ mrn.maron += 1
    $ vn_enter(bg="mrn_laundry", pc="serene", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_laundry_after")
    "And while you're still shaking, still full of her, your mouth opens on its own."
    mrn_maron "\"Thank you, Kanon-neesan.\""
    "It's your voice. Sweet and soft and polite, a maid's voice, with a little curl of pleasure in it. You didn't say it. You were going to say something else. You don't remember what."
    mrn_kanon "\"Oh? Hello. There you are.\""
    "Kanon isn't talking to you. She's talking to whoever just said thank you."
    menu:
        "Something else is in your mouth. Your mouth is smiling."
        "Take your mouth back":
            "You push. You don't know how you know how, but you push, the way you'd shove a door shut on a wind."
            mrn_you "\"That— that wasn't me. That wasn't me who said that.\""
            mrn_kanon "\"It was. It was the next you. She's shy, the first time. She'll be back.\""
            $ mrn.held += 1
        "Let her talk":
            "You're too tired to push. You lie on the table and listen to your own mouth."
            mrn_maron "\"I'll fold the sheets now, Kanon-neesan. Shall I start with the mistress's?\""
            mrn_kanon "\"Good girl. Yes.\""
            "And your body gets up, a little unsteady, Kanon's seed trickling down the backs of the white stockings, and starts folding sheets."
            "You watch it from somewhere behind your own eyes. After a while it hums."
            $ mrn.maron += 1
    $ vn_set_time(23, 40)
    $ vn_enter(bg="mrn_chris_room", pc="dazed", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_bite_two")
    "That night Chris drinks from the other side of your neck, standing, your back against her bedpost, and she doesn't touch you at all. She doesn't need to."
    "You come from the bite alone, a long, dry, rolling shudder, your cock no bigger than the tip of your little finger now."
    vn_sfx "Tsupu."
    mrn_you "\"Ahh— ahh♡— Onee-sama— hahh—\""
    mrn_chris "\"Kanon tells me you said thank you.\""
    mrn_you "\"That wasn't me.\""
    mrn_chris "\"It was, darling. It was the you that's coming. I can taste her already. She tastes of chestnuts.\""
    "In the morning it'll be gone. You know it the way you know the bond. You lie awake with your hand over it, the last of you, small and soft and warm, and listen to the pines."
    call mrn_cut(8, 1, "Tuesday. The third morning.")
    jump mrn_tuesday
