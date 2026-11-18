## THE STORY: chapters 0-2, Sunday to Tuesday (written 2026-11-17; PLAN.md). One body step and one hair step a morning.
## Chapters 3-5 are in scenes.rpy; 6, 7 and the endings are in finale.rpy. Second person. No pussy before Monday. No pregnancy.
## The curse: every no, stop or don't comes out as yes, more or do. A refusal choice plays as a yes (snp.yes counts them).

## ---- 0. Sunday: the club ----------------------------------------------------------------------------------

label snp_sunday:
    $ snp.fit = "kit"
    $ vn_enter(bg="snp_lockers", pc="nervous", pc_tag="snp_pc", cast=[("snp_ryota", "bully"), ("snp_oshiro", "bully")], cg="snp_lockers_bully")
    "Seiran University, western Tokyo, the football club's changing room after a two-nil loss."
    "You're [snp_pc_name] Nagai, twenty, a second-year full-back who came on for the last four minutes, and somehow it's your fault."
    snp_ryota "\"Oi. Nagai. You let their nine run straight past you.\""
    snp_you "\"I— he was offside, I thought—\""
    snp_oshiro "\"He thought.\""
    "Ryota grabs your kit bag off the bench and upends it into the shower bay. Your towel, your clean shirt, your phone in its case, all of it under the running water."
    "Oshiro laughs his big flat laugh."
    vn_sfx "Splsh."
    snp_ryota "\"And the boots. All of them. Everyone's. Before you go home. Spotless.\""
    "Twenty-two pairs of boots, caked in Sunday mud, lined up by the door. Nobody else says anything. Nobody else ever does."
    "Except."
    $ vn_enter(bg="snp_lockers", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace"), ("snp_ryota", "bully")], cg="snp_lockers_daigo")
    snp_daigo "\"Ryota. Leave him alone.\""
    "Daigo Kuroiwa, fourth-year, the club's ace, twenty-two goals last season."
    "He's tall and broad and tanned from the pitch, a towel round his neck, and when he walks between you and Ryota, Ryota steps back."
    snp_ryota "\"We're only having a laugh, Kuroiwa-san.\""
    snp_daigo "\"Have it somewhere else.\""
    "Ryota and Oshiro go. Daigo fishes your phone out of the shower bay, shakes it, and tosses it to you."
    snp_daigo "\"Still works. You alright, Nagai?\""
    snp_you "\"Yes. Thank you, senpai. Really. Thank you.\""
    snp_daigo "\"Don't mention it. Do my boots first, though, yeah? You do them better than anyone.\""
    "He grins and slaps your shoulder and you'd do his boots every day for the rest of your life."
    $ vn_set_time(19, 40)
    $ vn_enter(bg="snp_clubroom", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_clubroom_magazine")
    "The clubroom, after."
    "Daigo's sprawled on the old sofa under the poster, the one everybody knows: Mitsuki Amane, twenty-four, the gravure idol, in a white string bikini on a white beach, ash-pink hair to her waist, the curve of her hip like a dare."
    "He's got her new photo book open on his knee, the one with the purple cover. You're scrubbing his boots on the floor at his feet."
    snp_daigo "\"Look at her, Nagai. {i}Look{/i} at her. Page thirty-four.\""
    snp_you "\"She's... very pretty, senpai.\""
    snp_daigo "\"Pretty. Pretty, he says.\""
    "He tips his head back on the sofa and stares at the ceiling like a man at prayer."
    snp_daigo "\"One date. One day with a girl like that. Not even her, a girl {i}like{/i} her. Just once. I'd die happy.\""
    "You keep scrubbing. You think: I can't give him anything. Not a goal, not a girl. I can't give him anything at all."
    $ vn_set_time(21, 10)
    $ vn_enter(bg="snp_alley", pc="nervous", pc_tag="snp_pc", cast=[], cg="snp_alley_shop")
    "Your walk home goes through the old shopping street under the Odakyu line, and tonight, between the shut ramen place and the tatami-maker, there's an alley you've never noticed."
    "At the end of it, a lantern, and a sign in faded brush."
    "{i}Kagerou-dou. Curios. Wishes.{/i}"
    "You've walked this street five hundred times. It was not there yesterday."
    $ vn_enter(bg="snp_shop", pc="nervous", pc_tag="snp_pc", cast=[("snp_witch", "witch")], cg="snp_shop_counter")
    "Inside, it smells of camphor and old paper and something sweet and burnt. Shelves of jars. A clock with no hands."
    "Behind the counter, a small hooded woman, her face in shadow, her hands old and very still."
    snp_witch "\"Sit, Nagai-kun. You've a boot-polish smell and a wish on you.\""
    snp_you "\"How do you know my—\""
    snp_witch "\"A wish for somebody else, too. How rare. Tell me.\""
    "And you do. The boots. Ryota. Daigo stepping between you. Page thirty-four. {i}One day with a girl like that.{/i}"
    snp_witch "\"Then give him one. I can make you her, dear. Not the girl herself, but her double, to the last freckle. Seven mornings. A little more of her every time you wake.\""
    "She sets a paper on the counter. Old, soft as cloth, the brushwork faded brown."
    menu:
        "The contract lies between you. A brush, already wet."
        "Ask what it costs":
            snp_you "\"What does it cost?\""
            snp_witch "\"Sensible man. Two things. First, your refusal words. No, stop, don't, I won't. I'll keep them for you. For the week, you can only say the other thing.\""
            snp_you "\"Only... yes?\""
            snp_witch "\"Yes. More. Do. Please. A girl who can't say no gets her date, Nagai-kun. Second: he must love you by midnight on the seventh day. Love you. Not want. If he does, I give it all back.\""
            snp_witch "\"If he doesn't, you stay her.\""
            "Your hand is shaking. You think of his hand on your shoulder. {i}You do them better than anyone.{/i}"
            snp_you "\"He's a good man. He'll— he'll love her. Anyone would.\""
            snp_witch "\"Then sign.\""
        "Just sign":
            "You don't ask. You don't want to hear it. You pick up the brush."
            snp_witch "\"No questions? Not even the price?\""
            snp_you "\"He stood up for me. Whatever it is.\""
            snp_witch "\"Brave, or foolish. They're the same word in my trade. I'll tell you anyway, since you won't be able to say no to anything once it's dry. Your refusal words are mine for the week.\""
            snp_witch "\"And he must love you by the seventh midnight, or you stay her.\""
    show cg snp_shop_sign onlayer cgl
    "You write your name. The ink goes from black to brown to nothing, soaked into the paper like rain into dry earth."
    vn_sfx "Shff."
    snp_witch "\"Say no for me, Nagai-kun. One last time. Out loud.\""
    snp_you "\"N— no.\""
    "It comes out small and hoarse and the word feels loose in your mouth, like a tooth about to come out."
    snp_witch "\"Good. That's the last one. Go to bed.\""
    $ vn_set_time(23, 30)
    $ vn_enter(bg="snp_shun_room", pc="nervous", pc_tag="snp_pc", cast=[], cg="snp_room_sunday")
    "Your six-tatami flat, your futon, the window open on the train line. You lie awake for a long time with your hand on your flat chest."
    "Then you sleep, and you dream of white beaches."
    call snp_cut(7, 1, "Monday.")
    jump snp_monday

## ---- 1. Monday --------------------------------------------------------------------------------------------

label snp_monday:
    $ snp.fit = "nude"
    $ snp_grow(1)
    $ vn_enter(bg="snp_shun_room", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_mirror_monday")
    "You wake up wet."
    "Not sweat. Between your legs, a slick, warm, aching wet, and when you reach down under the duvet, your hand finds nothing where something has always been."
    "{color=#ff5fb8}Your cock is gone. Your balls are gone.{/color}"
    "{color=#ff5fb8}There's a pussy there instead, soft and closed and slippery, two small lips that part under your fingertip, and the jolt of it arches your back off the futon.{/color}"
    "{color=#ff5fb8}Your black hair has grown in the night, soft against your jaw, down to your chin.{/color}"
    snp_you "\"No— no, no, no, this isn't—\""
    snp_you "\"Yes— yes, yes, yes, this is—\""
    "The words turn over in your mouth like a coin. You clap your hand over your lips."
    snp_you "\"Y— yes. Yes.\" {i}No. I said no. I {b}meant{/b} no.{/i}"
    $ snp.yes += 1
    "Your voice is the same, mostly. It's only the words that won't come."
    show cg snp_mirror_explore onlayer cgl
    "You stand in front of the mirror on the wardrobe door, naked, your thin, flat-chested body and your new chin-length hair and between your legs that small neat slit, and you can't stop looking."
    "You can't stop touching."
    "One finger. Up the seam. The lips part and it's hot inside, hotter than your mouth, and you find the little hood at the top and press it, and your knees buckle."
    vn_sfx "Shlk."
    snp_you "\"Ahh— what— what is— {i}ahh{/i}—\""
    "You sit down hard on the edge of the futon with your legs open to the mirror and rub, the way you'd rub a cock, and it's wrong, and then you slow down and circle and it's {i}right{/i}, and the wet spreads down your fingers."
    vn_sfx "Shlk. Shlk. Shlk."
    snp_you "\"Oh— oh God— it's so— ahh— {i}ahh♡{/i}— there, there, {i}there♡{/i}—\""
    "You push one finger inside yourself. Tight, impossibly tight, gripping, and the noise you make bounces off the thin walls of the flat."
    snp_you "\"Inside— I'm {i}inside{/i} me— ahh♡— ahh♡— it's coming— something's coming— AHH♡—!\"" with vnfx("flash", "shake")
    "It isn't like coming. It's like falling."
    "It goes on and on, waves of it, your thighs clamped round your hand, and when it stops you're lying across the futon panting at the ceiling with your fingers soaked."
    "Second time, you don't even mean to. Your hand's just there."
    "You hump your own palm with your eyes shut and think of the poster, of a white string bikini, and it's not clear any more whether you're thinking of having her or being her."
    vn_sfx "Shlk. Shlk."
    snp_you "\"Mmh♡— mmh♡— again— {i}again♡{/i}—!\"" with vnfx("flash")
    $ vn_set_time(9, 30)
    $ snp.fit = "hoodie"
    $ vn_enter(bg="snp_pitch", pc="nervous", pc_tag="snp_pc", cast=[("snp_ryota", "bully"), ("snp_oshiro", "bully")], cg="snp_pitch_hoodie")
    "Monday morning practice. You go, because Shun Nagai always goes."
    "You wear your biggest hoodie over your training kit, and shorts long enough to hide that there's nothing in them, and nobody looks twice at you. Nobody ever does."
    snp_ryota "\"Nagai. Cones. Bibs. Balls. The ball bag, both water crates, and Oshiro's gloves. Go.\""
    "That's three trips' worth. Oshiro drops his gloves at your feet and grins."
    menu:
        "Ryota is waiting, arms folded."
        "Tell Ryota no":
            "You set your jaw. Not today. You're done with this. You look Ryota in the eye."
            snp_you "\"Yes. Gladly. Anything else?\""
            "Ryota blinks. Oshiro bursts out laughing."
            snp_oshiro "\"{i}Gladly!{/i} Did you hear him? Gladly!\""
            snp_ryota "\"Since you're so glad. Do the goal nets after.\""
            snp_you "\"Yes— yes, of course—\" {i}NO. No, no, no, I said NO.{/i}"
            $ snp.yes += 1
        "Just do it":
            "You pick up the gloves. It's easier. It's always been easier."
            snp_ryota "\"Good lad. And the goal nets after.\""
            "You try anyway, quietly, as a test. {i}No.{/i}"
            snp_you "\"...Yes.\""
            $ snp.yes += 1
    "You do all of it. Cones, bibs, balls, both crates, the nets."
    "Bending to collect cones, the new soft place between your legs rubs against the seam of your shorts, and by the last cone you're wet through your underwear and trying to walk normally."
    $ vn_enter(bg="snp_pitch", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_pitch_daigo")
    snp_daigo "\"Oi, Nagai. You're flushed. You feeling alright?\""
    snp_you "\"Yes, senpai. Just warm.\""
    snp_daigo "\"Your voice is weird today.\""
    snp_you "\"Is it?\""
    snp_daigo "\"Bit softer. Don't get ill on me, Nagai, the Tamagawa game's Saturday. Who'd do my boots?\""
    "He ruffles your new chin-length hair and jogs off. You stand on the touchline holding his water bottle and your heart goes {i}ba-dump{/i} like a heroine's in a romance manga."
    vn_sfx "Ba-dump."
    "Six more mornings. Six more of her, a piece at a time. Then he'll see her. Then he'll love her. Anyone would."
    $ vn_set_time(23, 0)
    $ snp.fit = "nude"
    $ vn_enter(bg="snp_shun_room", pc="moaning", pc_tag="snp_pc", cast=[], cg="snp_futon_monday")
    "That night you lie on your futon with Mitsuki's photo book open on the pillow at page thirty-four, which you bought on the way home with your face burning, and two fingers inside yourself, and you whisper into the dark."
    snp_you "\"Senpai— senpai— ahh♡— would you want me— {i}ahh♡{/i}— would you— AHH♡—!\"" with vnfx("flash")
    call snp_cut(7, 1, "Tuesday.")
    jump snp_tuesday

## ---- 2. Tuesday -------------------------------------------------------------------------------------------

label snp_tuesday:
    $ snp.fit = "nude"
    $ snp_grow(2)
    $ vn_enter(bg="snp_shun_room", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_mirror_tuesday")
    "{color=#ff5fb8}Two small soft swells on your chest, round and high, B cups, with puffy pink nipples that stiffen when the air touches them. The ends of your black hair have gone ash-pink overnight, as if someone dipped them in a rose-coloured dye.{/color}"
    "You cup them in the mirror and they're warm and heavy in a way nothing on you has ever been, and you squeeze, and the shock goes straight down between your legs."
    show cg snp_mirror_breasts onlayer cgl
    vn_sfx "Squsshh."
    snp_you "\"Breasts— I have {i}breasts{/i}— ahh♡— they're so— soft— ahh♡—\""
    "You pinch the nipples and the noise you make is a woman's noise. You do it again to hear it."
    "One hand on your chest and one between your legs, standing, swaying, watching the pink-tipped woman in the mirror come apart."
    vn_sfx "Shlk. Shlk."
    snp_you "\"Ahh♡— both— both at once— {i}AHH♡{/i}—!\"" with vnfx("flash", "shake")
    "No hoodie hides these. Shun Nagai doesn't go to practice today. Shun Nagai texts Ryota {i}sick{/i} and gets back {i}faker{/i}, and you pull on the hoodie anyway, no bra, and go out."
    $ vn_set_time(14, 0)
    $ snp.fit = "dress"
    $ vn_enter(bg="snp_boutique", pc="flustered", pc_tag="snp_pc", cast=[], cg="snp_boutique_dress")
    "A boutique in Shimokita, a white sundress on a mannequin, exactly the kind of thing on page twelve."
    "The woman at the counter takes one look at your hoodie and your bare chest moving under it."
    "\"Would you like to try it on? And a bra, maybe? We have a fitting service.\""
    "{i}No, thank you, just the dress.{/i}"
    snp_you "\"Yes, please. Both.\""
    $ snp.yes += 1
    "Her hands, measuring, brisk and professional round your new breasts. You bite your lip so hard it nearly bleeds."
    "She says {i}B, a full B{/i} and you say {i}yes, yes{/i}, and walk out in a white sundress and a pink bra with your old clothes in a paper bag."
    $ vn_set_time(19, 50)
    $ vn_enter(bg="snp_station", pc="hopeful", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_station_meet")
    "Kyodo Station, the north exit, ten to eight. Daigo comes this way every Tuesday after practice, to the gyoza place he likes."
    "You know because you've carried his bag here forty times."
    "You stand by the ticket gates in the white dress and pretend to read your phone. Your heart's going like a drum."
    "He comes through the gates in his club tracksuit with his bag on his shoulder. He looks at you. He stops."
    snp_daigo "\"...Woah.\""
    "He walks right up. He looks you up and down, slowly, from the pink tips of your hair to your bare knees and back, and stops at your chest, and stays there."
    snp_daigo "\"Has anyone ever told you you look like Mitsuki Amane?\""
    snp_you "\"I— no— I mean, yes, sometimes—\""
    snp_daigo "\"Sometimes. Right. You waiting for someone?\""
    snp_you "\"No. Just— by coincidence. I'm just here by coincidence.\""
    snp_daigo "\"Lucky coincidence. I'm Daigo. What's your name?\""
    snp_you "\"Shu— Shuna.\""
    snp_daigo "\"Shuna. Nah. I'm calling you Mitsuki-chan. Come on, Mitsuki-chan. Karaoke. My treat.\""
    "He puts his arm round your waist like he's already won something, and his hand slides down to your hip, and stays there, and he steers you across the road."
    "It's not the Daigo you know. It's not the hand on your shoulder in the changing room. It's a heavier hand."
    "And you can't say {i}no.{/i}"
    $ vn_set_time(20, 30)
    $ vn_enter(bg="snp_karaoke", pc="nervous", pc_tag="snp_pc", cast=[("snp_daigo", "ace")], cg="snp_karaoke_booth")
    "A karaoke booth on the fourth floor: purple light, a vinyl sofa, a screen playing a music video nobody's watching. He orders two highballs and doesn't pick a song."
    snp_daigo "\"So. Mitsuki-chan. You got a boyfriend?\""
    snp_you "\"No.\" {i}That one works. That's not a refusal, that's just true.{/i}"
    snp_daigo "\"Good.\""
    "His hand's on your knee. Then it's on your thigh, under the hem of the white dress, his palm hot and dry and broad."
    "He's watching your face the whole time, the way he watches a keeper before a penalty."
    snp_daigo "\"You're shaking. You nervous?\""
    snp_you "\"Yes.\""
    snp_daigo "\"Cute.\""
    "His hand goes higher."
    menu:
        "His fingers are at the edge of your knickers. The music video plays on."
        "Tell him to stop":
            "{i}Senpai, please stop. I came for a date. I came so you'd like me. Please stop.{/i} You take a breath and put your hand on his wrist."
            snp_you "\"Senpai— please— don't stop.\""
            "You hear it. He hears it. His grin goes wide and wolfish."
            snp_daigo "\"Senpai, is it? Yeah. I won't.\""
            $ snp.yes += 1
        "Let him":
            "You think: this is how you win him. You think: this is what she'd do. You let your knees fall apart."
            snp_daigo "\"There we go.\""
            "And when you try, a second later, to say {i}wait{/i}, it comes out {i}yes{/i}."
            $ snp.yes += 1
    $ snp.fit = "nude"
    show cg snp_karaoke_finger onlayer cgl
    "Two thick fingers slide your knickers aside and find you soaked, and he laughs low in his throat."
    snp_daigo "\"Fuck me. You're dripping, Mitsuki-chan. Bet you clocked me at the gates and went wet.\""
    vn_sfx "Shlk. Shlk. Shlk."
    snp_you "\"Ahh— senpai— that's— {i}ahh♡{/i}— in front of the camera— there's a camera—\""
    snp_daigo "\"It's broke. Has been for a year. Open your legs.\""
    "You open your legs."
    "He hooks his fingers inside you and rubs his thumb over your clit, rough, fast, not at all like you did it alone, and it's worse, and it's better, and you're arching off the vinyl."
    snp_you "\"Ahh♡— ahh♡— too much— more— {i}more{/i}—\" {i}I said too much, I said stop, I said—{/i}"
    snp_daigo "\"More, she says. Greedy.\""
    snp_you "\"Senpai— ahh♡— AHH♡—!\"" with vnfx("flash")
    "You come on his hand in under a minute with the white dress rucked up round your hips and the karaoke machine singing a love song at the empty room."
    show cg snp_karaoke_sex onlayer cgl
    "Then his tracksuit bottoms are down, and his cock's out, thick and dark and curved, bigger than yours ever was, and he pulls you into his lap facing him and lines it up."
    snp_you "\"Senpai— wait— I've never— I'm—\""
    snp_daigo "\"You want it?\""
    "{i}No.{/i}"
    snp_you "\"Yes.\""
    $ snp.yes += 1
    "He pulls you down onto it."
    vn_sfx "Zuuuuun."
    snp_you "\"{i}HAAAH—!{/i} It's— it's {i}huge{/i}— it's inside— senpai, it's all the way inside me—\"" with vnfx("shake")
    snp_daigo "\"Fuck. Tight. You really never? Fuck.\""
    "He grips your hips and bounces you, hard, and every time he drops you the whole length goes in and knocks something deep inside that makes your vision go white at the edges."
    "The vinyl squeaks. Your new breasts bounce in the pink bra."
    vn_sfx "Pan. Pan. Pan. Pan."
    snp_you "\"Ahh♡— ahh♡— senpai— senpai— {i}ahh♡{/i}— it's too deep— deeper— {i}deeper{/i}—\""
    snp_daigo "\"Louder. Nobody can hear in here. Sing for me, Mitsuki-chan.\""
    snp_you "\"AHH♡— ahh♡— I'm— I'm— it's happening again— on your cock— I'm gonna—\""
    snp_you "\"{i}HAAAAAH♡—!{/i}\"" with vnfx("flash", "shake")
    "You clamp down on him and he swears and drives up into you three more times and comes, pulled out at the last second, over your thigh and the white hem of the dress."
    show cg snp_karaoke_second onlayer cgl
    "Round two, he bends you over the karaoke table with your face by the song book and takes you from behind, his hand fisted in your pink-tipped hair, the mic stand rattling every time he slams in."
    vn_sfx "Pan. Pan. Pan."
    snp_you "\"Senpai♡— senpai♡— ahh♡— your cock— I can feel— {i}ahh♡{/i}— it's— AHH♡—!\"" with vnfx("flash")
    snp_daigo "\"Same time tomorrow. Skip lectures. Wear something shorter.\""
    "He puts your number into his phone as {i}Mitsuki ♡ karaoke{/i}, pays the booth, and goes off to his gyoza without you."
    $ vn_set_time(23, 0)
    $ snp.fit = "dress"
    $ vn_enter(bg="snp_shun_room", pc="dazed", pc_tag="snp_pc", cast=[], cg="snp_room_tuesday")
    "Home. The dress on the floor with his cum dried on the hem. You lie on your futon, sore and humming, and stare at the ceiling."
    "He didn't ask anything about you. Not one thing. He looked at your chest when he talked to you."
    "{i}He's a good man. He stood up for me.{/i}"
    "Five more mornings."
    call snp_cut(6, 1, "Wednesday.")
    jump snp_wednesday
