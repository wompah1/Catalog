## THE STORY: days 1-6 (PLAN.md). Rent day and the crossing; waking at Hayami's clinic (the first exam); home, and Gonda's
## offer (the title line). The change shows each night in the bathroom mirror (sef_grow before the night's vn_enter).
## Changes are pink ({color=#ff5fb8}).

## ---- 0. Monday: rent day ----------------------------------------------------------------------------------------

label sef_rentday:
    $ sef.fit = "suit"
    $ vn_enter(bg="sef_doorway", pc="stern", pc_tag="sef_pc", cast=[("sef_natsuki", "worried"), ("sef_gonda", "leer")], cg="sef_rent_day")
    "Half past six on the last Monday of the month, and you can hear Gonda on the stairs before you've got your key out."
    "You're Akira Sena, twenty-four, a logistics clerk in a grey suit that cost less than your phone."
    "You share a two-room flat in Nakano with Natsuki, and for a year and a half you've kept the landlord off her."
    "Tonight he's beaten you home."
    "He's in the doorway with one arm up on the frame, a big soft man in his fifties in a cardigan, and Natsuki's in the hall in her bakery apron, holding the door half shut."
    sef_gonda "\"Two months, Natsuki-chan. Two months. I'm a patient man, but I'm not a charity.\""
    sef_natsuki "\"I'll have it on the fifteenth. I told you. They cut my shifts, that's all—\""
    sef_gonda "\"There are other ways to pay rent, you know. A pretty thing like you. I'd take it in kind. Gladly.\""
    "His eyes go down her apron and back up. She goes red to the ears."
    menu:
        "He's leaning in."
        "Step between them":
            "You put yourself between them, shoulder first, so he has to take a step back onto the landing."
            sef_you "\"She said the fifteenth. You'll get it on the fifteenth. Goodnight, Gonda-san.\""
            $ sef.held += 1
        "Shut the door on him":
            "You reach past Natsuki and push the door until it meets his arm, and keep pushing, politely, until the arm goes away."
            sef_you "\"The fifteenth. Goodnight.\""
            $ sef.gave += 1
    sef_gonda "\"Always the gallant, Sena-kun.\" He chuckles through the gap. \"One of these days you won't be here.\""
    "The door clicks. Natsuki lets out a breath and sags against the wall."
    sef_natsuki "\"Thank you. Again. I'll pay you back too, I swear.\""
    sef_you "\"Pay him first. I'm going to get us dinner. Curry?\""
    sef_natsuki "\"Katsu curry. You're a saint.\""
    $ vn_set_time(19, 10)
    $ vn_enter(bg="sef_crossing", pc="stern", pc_tag="sef_pc", cast=[], cg="sef_headlights")
    "It's raining by the time you come out of the curry shop, a fine grey rain that turns the crossing outside the station into a sheet of reflected neon."
    "The man is green. You step off the kerb with the bag in one hand and your phone in the other, already thinking about the fifteenth and how you'll cover it if she can't."
    "Headlights. Very big, very white, very close. A horn."
    "Then nothing at all."
    call sef_cut(10, 3, "Thursday.")
    jump sef_clinic

## ---- 1. Thursday: the clinic ----------------------------------------------------------------------------------------

label sef_clinic:
    $ sef_grow(1)
    $ sef.fit = "gown"
    $ vn_enter(bg="sef_ward", pc="dazed", pc_tag="sef_pc", cast=[("sef_hayami", "calm")], cg="sef_waking")
    "White ceiling. A soft hum. A smell of lemons and something medical underneath."
    "You're in a bed in a quiet room with a window full of grey sky, in a pale blue gown, and your body feels as if somebody's been rearranging the furniture in it."
    "There's a woman at the foot of the bed with a tablet: thirty-something, a white coat over a black dress, her hair pinned up, red-framed spectacles, the calmest face you've ever seen."
    sef_hayami "\"Good morning, Sena-san. I'm Dr Hayami. You're at my clinic in Meguro. You've been asleep since Monday night.\""
    sef_you "\"Monday... the truck—\""
    "That's when you hear your own voice. It's high and soft and breathy, a woman's voice, and it came out of your mouth."
    sef_hayami "\"Yes. The truck. It did a great deal of damage, and there wasn't enough left to put back the way you were. So I put you back the way I could.\""
    "She turns the tablet round. On it is a photo of a woman asleep in this bed: a heart-shaped face, soft full lips, black hair spread on the pillow."
    "You put a hand up to your face. Your fingers find a jaw that isn't yours and hair that comes down to your shoulders. Your hand is small. Your wrist is narrow."
    "{color=#ff5fb8}Under the gown, your chest lifts when you breathe: two round soft weights, a full handful each, that sway as you sit up. Your hips are wide against the mattress.{/color}"
    "{color=#ff5fb8}Between your legs there's nothing at all where your cock was: only soft smooth folds, and a strange new warmth.{/color}"
    sef_you "\"You— you made me a {i}woman?{/i}\""
    sef_hayami "\"A very good one, if I say so myself. A hundred and fifty-eight centimetres, every system working. Your company's been told you had emergency surgery.\""
    sef_hayami "\"Your papers say Akira Sena, female. My clinic is very good at paperwork.\""
    "She sets a white pill box on the blanket. Two compartments for every day of the week."
    sef_hayami "\"Two a day, morning and night, for the rest of your life. They keep everything I built working the way I built it.\""
    sef_hayami "\"Side effects may include growth, sensitivity and appetite. I'll be monitoring all three. Speaking of which, it's time for your first examination.\""
    $ vn_set_time(11, 0)
    $ vn_enter(bg="sef_exam", pc="flustered", pc_tag="sef_pc", cast=[("sef_hayami", "smirk")], cg="sef_first_exam")
    "The examination room has a padded table with stirrups, a bright lamp on an arm, and a tray of instruments you don't look at too closely."
    "She has you lie back with the gown open and your heels in the stirrups, and she pulls on a pair of black gloves with a snap."
    sef_hayami "\"Sensitivity first. Tell me what you feel. Out loud, please; I'm taking notes.\""
    "She cups one of your breasts in a gloved hand and weighs it, then rolls the nipple between her finger and thumb."
    "It goes hard at once and a bolt of heat shoots straight down between your legs."
    sef_you "\"Hah— that's— it's—\""
    sef_hayami "\"Out loud, Sena-san.\""
    sef_you "\"It's {i}hot—{/i} it goes all the way down—\""
    sef_hayami "\"Good. Very good.\" She types something, one-handed. \"Now the important part.\""
    show cg sef_exam_fingers onlayer cgl
    "Two gloved fingers part your new folds, slow, and slide over something small and swollen at the top that makes your whole body jump on the table."
    sef_you "\"AH— what— what {i}is—{/i}\""
    sef_hayami "\"Your clitoris. Everything that used to be in your cock is in there now, packed tight. Let's see how it works.\""
    menu:
        "Her fingers are circling it."
        "Tell her to stop":
            sef_you "\"Doctor— stop— this isn't— hah— this isn't an {i}exam—\""
            sef_hayami "\"Everything I do is an exam, Sena-san. And you're dripping on my table. I'd say the results are in.\""
            "She doesn't stop. Your heels stay in the stirrups."
            $ sef.held += 1
        "Let her keep going":
            "You mean to say something. What comes out of you instead is a long shaky moan, and your knees fall open on their own."
            sef_hayami "\"There. Good patient.\""
            $ sef.gave += 1
    "She slides two fingers inside you."
    "You've never had anything inside you there, because there's never been a there, and it's so slick and so full and so {i}right{/i} that you grab the sides of the table."
    vn_sfx "Kuchu. Kuchu. Kuchu."
    "She crooks them up against a spot that makes your vision go white, and bends, and puts her mouth on your clit, and sucks."
    sef_you "\"Oh— oh god— doctor— Doctor♡— it's— something's coming, something's— AHHH♡—!\"" with vnfx("flash", "shake")
    "It isn't like coming used to be. It doesn't stop."
    "It rolls through you in waves, your new pussy clenching round her fingers again and again, and your hips lifting off the table, and your own voice ringing off the white walls."
    "When it lets go of you, you're limp in the stirrups, gasping, and she's writing on the tablet with a damp glove."
    sef_hayami "\"Sensitivity: excellent. Forty seconds, multiple contractions, very vocal. I'll see you again on Wednesday.\" She smiles, for the first time. \"Take your pills.\""
    call sef_cut(9, 2, "Saturday.")
    jump sef_home

## ---- 2. Saturday: home, and Gonda --------------------------------------------------------------------------------

label sef_home:
    $ sef.fit = "home"
    $ vn_enter(bg="sef_flat", pc="flustered", pc_tag="sef_pc", cast=[("sef_natsuki", "worried")], cg="sef_natsuki_door")
    "The clinic sends you home in a taxi in clothes from its own cupboard: a soft jumper that clings, a skirt, flat shoes, a bra the nurse had to show you how to fasten."
    "Natsuki opens the door, looks at you, and says politely,"
    sef_natsuki "\"Can I help you?\""
    "It takes you twenty minutes, your work ID, your phone, and a story about the night you both got locked out on the roof before she believes you."
    sef_natsuki "\"Akira. Oh my god. {i}Akira.{/i} You're... you're really pretty.\" She covers her mouth. \"Sorry. Sorry. Are you all right?\""
    sef_you "\"I'm alive. That's the main thing, apparently.\""
    "She makes you tea. Her hands shake. Then her phone buzzes on the table, and she reads it, and all the colour goes out of her face."
    vn_sfx "Bububu."
    sef_natsuki "\"It's Gonda. He says if I don't come down tonight and 'settle up', he's changing the locks on Monday. You weren't here, and I... I didn't have it, Akira.\""
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sef_gonda", pc="stern", pc_tag="sef_pc", cast=[("sef_gonda", "grin")], cg="sef_take_her_place")
    "You go down instead of her."
    "Gonda's flat smells of beer and pickles and the television's on loud. He opens the door in his cardigan, expecting Natsuki, and stops, and looks at you for a long time."
    "You tell him who you are. He laughs till he has to sit down."
    sef_gonda "\"Sena-kun! Sena-{i}chan,{/i} now. Look at you. Well, well, well. And here's me, out two months on the flat.\""
    sef_you "\"I'll cover her rent. Give me till the end of the month.\""
    sef_gonda "\"I've given her till the end of two months already.\" He looks you up and down, slow, the way he looks at Natsuki."
    sef_gonda "\"But you know what? I've got a better idea. You want to take her place?\""
    "There it is. You knew it was coming the moment he opened the door."
    menu:
        "He's waiting for an answer."
        "Make him promise first":
            sef_you "\"Her rent. Both months. Gone. And you leave her alone. Say it.\""
            sef_gonda "\"Both months, gone, and I'll be a perfect gentleman to Natsuki-chan. My word on it.\""
            $ sef.held += 1
        "Just get it over with":
            sef_you "\"Fine. Fine. Where?\""
            sef_gonda "\"Ohh, that's the spirit.\""
            $ sef.gave += 1
    "He takes you to the futon in the back room and strips you himself, slowly, like a present: the jumper over your head, the skirt down, the bra he fumbles with for a whole minute."
    "When your breasts come out of it he just looks at them, his big soft hands hovering, and then he grabs them both and squeezes, and you gasp."
    sef_gonda "\"Natsuki-chan's are nothing on these. Nothing. You were wasted as a man, Sena-chan.\""
    show cg sef_gonda_futon onlayer cgl
    "He pushes you down on your back and gets between your knees with his trousers round his thighs."
    "His cock is thick and dark and already wet at the tip, and he rubs it up and down your slit until you're slick, which happens much faster than you'd like."
    sef_gonda "\"I'll pull out. I'm a gentleman.\""
    "And somehow that's the worst of it: the idea of him dragging this out, stopping and starting, making it last."
    sef_you "\"Just cum inside me, then!? Get it {i}over{/i} with!\""
    sef_gonda "\"Ohh. Well, if you're asking.\""
    "He pushes in."
    vn_sfx "Zupu. Zupu. Pan. Pan."
    "Your first real cock, and it's {i}his.{/i} It stretches you open inch by inch and keeps going, and your new body grips it all the way down like it's been waiting for one, and a noise comes out of you that you didn't decide to make."
    menu:
        "He's fucking you on his futon."
        "Bite your lip":
            "You bite your lip and turn your face to the wall and count the cracks in the plaster. You get to nine before your hips start meeting his on their own."
            $ sef.held += 1
        "Let it out":
            "You stop trying to keep it in. It's too much, too full, too good, and your voice just goes."
            $ sef.gave += 1
    sef_you "\"Ahh— ahh♡— hah— you're— so {i}thick— ahh♡—\""
    sef_gonda "\"Listen to you. Listen to that. Sena-kun used to look down his nose at me on the stairs.\""
    "He speeds up, grunting, his belly slapping against yours, and every stroke drags across that spot Hayami found and your pussy clenches tighter and tighter round him."
    sef_you "\"I'm— no— not from {i}you—{/i} not from— AHHH♡—!\"" with vnfx("flash", "shake")
    sef_gonda "\"Here it comes, then. Just like you asked.\""
    "You come round his cock with your back arched off the futon, and he slams in to the hilt and holds there, and you feel him pump into you, hot, thick, again and again, filling you up while you're still clenching on him."
    vn_sfx "Dobyu! Byuru, byururu."
    "When he pulls out it runs down between your cheeks onto his futon. He pats your thigh."
    sef_gonda "\"Rent's paid. Two months. Pleasure doing business, Sena-chan.\""
    $ vn_set_time(23, 30)
    $ sef_grow(2)
    $ vn_enter(bg="sef_mirror", pc="dazed", pc_tag="sef_pc", cast=[], cg="sef_mirror_two")
    "Natsuki's asleep when you come up, or pretending to be. You shower for a long time and take your evening pill, because the box says to."
    "{color=#ff5fb8}In the bathroom mirror your breasts look bigger. They are bigger.{/color}"
    "{color=#ff5fb8}They were a full handful in the clinic; now they spill out of your hands, heavy and round and high, and the nipples are puffier and pinker than they were this morning.{/color}"
    "{color=#ff5fb8}The bra from the clinic cupboard doesn't close any more.{/color}"
    "Side effects may include growth."
    "And sensitivity: when you brush a nipple with your thumb, your knees go."
    "And appetite."
    "You stand there in the steam, with Gonda still dripping out of you, and your hand goes down between your legs, and you don't take it away until you've come again with your forehead on the cold glass."
    call sef_cut(7, 2, "Monday.")
    jump sef_commute
