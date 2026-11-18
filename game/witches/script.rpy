## THE SOURCE: witches' passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, rungs-late.twee, ending.twee), written as beats; the
## director scenes are in scenes.rpy. The original is in catalog/docs/routes/vn-original/witches/.
## Nobody explains anything; nobody threatens; he's outraged, never frightened, never in tears. No
## heights, no measuring, no size set against a partner's; he/him to the last line.

## ---- NIGHT 1, Charmed (Witches Opening, Corridor, Ward Four) -------------------------------

label wit_opening:
    $ wit.fit = "kit"
    $ vn_enter(bg="wit_hut", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_hut_night")
    show cg wit_hut_night onlayer cgl
    "The Northcott guard hut is a Portakabin with a kettle in it."
    "It sits just inside the back gate, under one buzzing floodlight, with the chain-link fence running off either side of it into the dark and a yellow sign every few yards: NORTHCOTT SECURITY. SITE PATROLLED. KEEP OUT. Behind it, filling the whole sky, is the old infirmary wing. Black brick. Tall windows. Not one light in any of them."
    hide cg onlayer cgl
    "Inside it's warm and smells of instant coffee. The duty supervisor sits by the window with a folded newspaper and a pen, doing the crossword. She doesn't look up when you come in. She doesn't look up when the door bangs shut behind you."
    wit_super "\"Kit's on the side.\""
    show cg wit_kit onlayer cgl
    "The kit's on the side. Three torches. Three radios. Three whistles on lanyards. Three hi-vis jackets with NORTHCOTT on the back. And three bags of rock salt from the council gritting store, the kind they throw on the roads in January, with the tops rolled down."
    wit_you "\"Salt.\""
    wit_super "\"Salt.\""
    "She writes in seven down."
    hide cg onlayer cgl
    "You put the hi-vis on over your polo shirt and zip it up. You clip the radio to your shoulder, hang the whistle round your neck with the lanyard, pick up a torch and click it on and off twice to check it, and pick up the salt."
    "[wit_pc_name] Kettering, twenty-four, Northcott Security, two years on nights, not one single incident on your record. Short dark hair, grey eyes, lashes your mum's friends used to coo about, and a face so pretty the lads at the depot have called you Pretty since your first week. You hate it. You have told them, in writing, that you hate it."
    "The night log's on a clipboard by the kettle. You sign yourself in, under the other two, in block capitals, pressing hard."
    show screen wit_log
    show wit_niall grin at vn_cast_slot
    wit_niall "\"Pretty's here. Now it's a party.\""
    hide screen wit_log
    "From the doorway, grinning. Niall's always grinning. He's got a grin for the bus driver and a grin for the woman at the chippy and a grin for the police, and as far as anybody at the depot knows he has never once in his life said no to anyone about anything."
    wit_you "\"Don't call me that.\""
    wit_niall "\"Pretty, Pretty, Pretty.\""
    hide wit_niall
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"Lads.\""
    "That's Rufus, ducking in under the door frame. Rufus is the team lead. He's big and steady and ex-army and nothing has ever flustered him, not the flood at the shopping centre, not the lorry fire on the bypass, nothing. He picks up his torch and his salt like they're the same weight."
    wit_rufus "\"Brief. Listen up.\""
    "The brief is short. Men go into the old infirmary wing after dark and don't come out. Drunks on a dare. Then a pair of council surveyors. Then a whole Northcott team last spring. The town says witches. The council says subsidence. Northcott has the contract to clear it, and tonight it's sent the three of you."
    wit_rufus "\"Torches on. Radios on channel one. Stay in contact. We go in together and we come out together.\""
    "He looks at each of you in turn. You stand up straight. You've got the clipboard under your arm. You've got the site rules laminated in your pocket."
    wit_you "{b}\"Nobody gets left in here.\"{/b}"
    "Niall laughs. Rufus doesn't. Rufus nods, once, like you've said exactly the right thing."
    hide wit_rufus
    wit_super "\"Back in at— oh, never mind.\""
    "To the crossword. She doesn't look up."
    show cg wit_curtain onlayer cgl
    "Outside the hut, up on the third floor of the wing, a curtain moves that has no business moving. Behind the fence, on the night air, there's a smell of lavender.\n{size=-5}{color=#ff8fa3}▸ Through the gate{/color}{/size}"
    $ vn_until(22)
    jump wit_corridor

label wit_corridor:
    $ vn_enter(bg="wit_corridor", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "The back door of the wing opens with a key on Rufus's ring and a long, low groan, and the three of you step into the dark."
    vn_sfx "{i}Tik, tik, tik.{/i}"
    "Corridors. Long ones. Green gloss paint peeling off the walls in strips, black-and-white floor tiles, and tall windows every few yards letting the moonlight in in long pale slabs across the floor. Your three torch beams wobble down it like drunks. Somewhere a pipe is dripping."
    "And lavender. Proper lavender, like your nan's knicker drawer, thick enough to taste, in a building that's been shut for years."
    show wit_niall grin at vn_cast_slot
    wit_niall "\"Smell that?\""
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"Subsidence.\""
    hide cg onlayer cgl  # ff 1:46 am ET 11-18: no picture, wit_corridor_sign failed 4 draws (SCENES.md witches v4)
    "At the end of the corridor there's a stairwell, a set of double doors, and a sign with an arrow, the old painted kind: WARDS ONE TO FOUR. ADMISSIONS. MATRON. Rufus stops under it and shines his torch on his map."
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"Right. We'll cover more ground if we split up.\""
    "You stare at him."
    wit_you "\"That's what they say in every single film. Every film, Rufus. Right before it all goes wrong.\""
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"It's a building, Kettering. It's not a film. Niall, ground floor and the east stairs. I'll take the first floor and Ward Two. Kettering, Ward Four. Radio check every ten.\""
    "He points with his torch."
    wit_you "\"Rufus—\""
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"Stay in contact.\""
    hide cg onlayer cgl
    "And he's gone up the stairs, two at a time, and Niall's gone through the double doors with a wave and a grin, and you're on your own in a green corridor full of moonlight and lavender with a bag of salt."
    wit_you "\"Every film.\""
    "You tell the corridor. You get as far as the next window."
    vn_sfx "{i}Kssht.{/i}"
    wit_radio "\"Em, there's a— oh. {i}Oh{/i}, hello. She's lovely—\""
    "Your radio. Niall, low and puzzled. A giggle. Not his. A woman's, soft and delighted, right up against his mic. Static."
    show wit_pc outraged
    wit_you "\"Niall? Niall, come in. NIALL. Niall, what's your position— Niall, respond, that's an order— I mean, it's not an order, I'm not the lead, but RESPOND—\""
    "You smack the radio."
    vn_sfx "{i}Kssht.{/i}"
    wit_radio "\"Kettering, don't come up to Ward Two. I've got— no. No, put that {i}down{/i}—\""
    "Rufus. Steady, the way Rufus always is. Static."
    "And then nothing. Just your own breathing, and the pipe going {i}tik, tik{/i}, and from somewhere above you, up through the ceiling, very faintly, a big steady man saying \"{i}oh{/i},\" in a voice you've never heard Rufus use."
    show cg wit_read_rules onlayer cgl
    "You stand in the moonlight with your torch shaking. Then you do the only thing you can think of. You key your radio, and you hold the laminated card up to your torch, and you read the site rules into it, loud and clear, for anyone in the building who's listening."
    wit_you "\"This is Northcott Security. This site is closed to the public. Unauthorised persons are trespassing and must leave the premises immediately. No smoking. No naked flames. No interfering with the fixtures and fittings. All visitors must sign in at the hut. That means YOU.\""
    "From up the stairs, somewhere in the dark, a whole roomful of women burst out laughing." with vnfx("shake")
    "You grip your salt. You go and find Ward Four.\n{size=-5}{color=#ff8fa3}▸ Up the stairs to Ward Four{/color}{/size}"
    $ vn_pass(5)
    jump wit_ward_four

## Rung 1: Ward Four. Morgause at the far end ("Another torch."), Bryony on the nearest bed, the salt
## licked, the kiss: Charmed. Daze takes the torch. Charm walks his legs to her bed; her palm puts him
## on his back; she sinks down.
label wit_ward_four:
    $ vn_enter(bg="wit_ward_four", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "Ward Four is the long kind. A Nightingale ward, the old sort, one huge room with tall windows down both sides and a row of iron beds under each, foot to the middle, stretching off into the dark further than your torch can reach. The mattresses are bare. The moonlight lies across them in stripes."
    "You sweep the beam down the ward. Bed. Bed. Bed. Bed."
    show cg wit_ward_morgause onlayer cgl
    "A woman."
    "Right at the far end, under the last window, standing quite still. Tall. A long black robe. Long black hair. Two dark horns swept back from her temples like a ram's. An old silver watch pinned to the front of her robe, the kind nurses used to wear, catching your torchlight. And her eyes, all the way down the ward, are violet, and they're looking at you, and she looks amused."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "{b}\"Another torch.\"{/b}"
    "She doesn't raise her voice. You hear it like she's standing next to you."
    hide cg onlayer cgl
    "Your beam jerks. When you swing it back, she's gone. Just the window and the moonlight and the last bare bed."
    wit_you "\"Right. {i}Right.{/i}\""
    "In a voice that comes out much higher than you'd like."
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Oh, don't mind her. She's like that with everyone.\""
    show cg wit_bryony_bed onlayer cgl
    "Someone's sitting on the nearest bed. Right next to you. Cross-legged on the bare mattress, as if she's been there the whole time."
    "She's pretty. That's the first thing. Honey-blonde curls spilling out from under a battered old witch's hat, pointed ears poking out through them, violet eyes, and a loose cream robe that's fallen open down the front so you can see she's not wearing a single thing under it. Soft round breasts. Soft round thighs. She's swinging one foot and smiling at you like you're the nicest surprise she's had all week."
    "You get your torch on her. You get your bag of salt up. You get your voice down to where it should be."
    wit_you "\"Northcott Security. You're trespassing.\""
    wit_bryony "\"Oh, {i}bless{/i} him.\""
    menu:
        "\"Oh, {i}bless{/i} him.\""
        "Fling the salt":
            wit_you "\"This site is closed to the public. I'm going to have to ask you to—\""
        "Read her the site rules first":
            wit_you "\"No smoking. No naked flames. No interfering with the fixtures and fittings. All visitors must sign in at the hut. And I'm going to have to ask you to—\""
            "She listens to every word, nodding along, delighted."
    show cg wit_salt_lick onlayer cgl
    "You dig your hand into the bag and fling a big handful of rock salt straight at her. It goes everywhere. It rattles off the iron bedframe and pings off the window and showers all over her robe and her curls and her lap."
    "She picks a bit off her thigh. Looks at it. Puts it on her tongue."
    wit_bryony "\"Mm. Salty.\""
    "Then she licks her fingertip clean, slowly, looking right at you, and kisses it, and blows the kiss at you across her palm."
    call wit_ting("Charmed")
    "It hits you in the chest like a warm hand."
    "Your fingers go soft. The torch slips out of them, bounces once on the tiles, and rolls away under the next bed, its beam spinning round the ceiling, and you just watch it go, because suddenly the most important thing in the whole world is how pretty she is. How {i}soft{/i} she looks. The way her curls bounce. The way she's smiling at you."
    show cg wit_charm_walk onlayer cgl
    "And your legs take a step towards her."
    wit_you "\"No. No. Stop that.\""
    "You tell them. They take another one."
    show wit_pc outraged
    wit_you "\"Legs. LEGS. I am telling you to STOP— I'm on shift. I am ON SHIFT, I am a Northcott Security officer and I am not walking towards the— {i}stop walking{/i}—\""
    "Another step. Your boots squeak on the tiles. Every time she smiles, you take a step. She keeps smiling. You keep stepping. You arrive at the side of her bed with your hands at your sides and your face on fire and your whole body leaning towards her like a plant towards a window."
    wit_bryony "\"There we go. I'm Bryony. Hello.\""
    wit_you "\"Don't— don't you {i}hello{/i} me—\""
    show cg wit_bryony_push onlayer cgl
    "She puts her palm flat on your chest. Just that. A soft warm hand on your hi-vis. And your knees fold and you sit down hard on the edge of the bed, and then she pushes, gently, and you go over onto your back on the bare mattress with the iron frame creaking under you and the moonlight on your face."
    wit_you "\"Off. Get OFF. I'm— that's assault on an officer, that is, that's—\""
    "She's unbuckling your belt. She's humming while she does it. She pops the button on your cargo trousers and draws the zip down, and reaches into your boxers, and wraps her soft hand round your cock, and it's already hard. It's been hard since the kiss. It's so hard it jumps in her hand."
    wit_bryony "\"Oh, bless him. Charmed right through and still fighting it.\""
    "Delighted."
    wit_you "\"I'm ON SHIFT—\""
    wit_bryony "\"I know, lovely. You keep saying.\""
    hide wit_bryony
    "She shrugs the robe off her shoulders. It slides down her back and pools on the mattress. She swings one soft thigh over your hips and kneels up over you, all curls and breasts and moonlight, and holds your cock straight up, and rubs the tip of it along her pussy, slow, so you feel how wet she is."
    wit_you "\"Get— don't you— {i}don't you dare{/i}—\""
    "Your hips push up. You didn't tell them to. She smiles at you, and they push up again."
    show cg wit_bryony_sink onlayer cgl
    "She sinks down. Slow. The head of you slips into her, hot and slick and tight, and she wriggles, and takes a bit more, and a bit more, watching your face the whole time with her lips parted, until with a happy little sigh she sits all the way down on you and you're inside her to the root."
    wit_you "\"{i}AHH{/i}— get— OFF—\"\n{size=-5}{color=#ff8fa3}▸ I'm on SHIFT{/color}{/size}" with vnfx("shake")
    jump wit_ward_four_sex

## Rung 1's last beat inside the act: he comes yelling that he's on shift, and the bed starts again.
label wit_ward_four_after:
    $ vn_enter(bg="wit_ward_four", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_one_cum")
    vn_sfx "{i}Kii, kii, kii, kii.{/i}"
    show cg wit_one_peak onlayer cgl
    "The old iron bed squeaks under the two of you like it's never been so busy. Bryony's bouncing on your cock with her hands flat on your chest and her curls flying and her hat still on, impossibly, and every time she comes down, your hips come up to meet her. Every single time. You're telling them not to. They don't care."
    wit_you "\"I'm on SHIFT— I'm ON— {i}ahh{/i}— get OFF—\""
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Shh, shh, lovely. Nearly.\""
    "She leans down and kisses the end of your nose. Charm goes through you like warm syrup, and your hips buck up so hard she squeaks and laughs."
    wit_you "\"That's— that's not ME— that's YOUR— {i}hnnngh{/i}—\""
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"I know. Isn't it lovely?\""
    "She squeezes. Right round you. Hot and wet and tight."
    "It builds in the bottom of your belly whether you like it or not. It builds and builds, and you can feel it coming, and you grab the iron bedframe over your head with both fists and yell at the ceiling of Ward Four."
    show cg wit_one_cum onlayer cgl
    "And you come, yelling that you're on shift."
    wit_you "\"I'm ON— SHIFT— {i}AHH{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You go off inside her in long hard pulses, your whole body arching up off the bare mattress, your boots kicking at the foot rail. Bryony moans, soft and pleased, and grinds right down onto you and holds you there while you pump into her, and rubs little circles on your chest with her thumbs like she's settling you down for the night."
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Oh, {i}there{/i} he is. Good lad. Bless him.\""
    "You lie there panting with the moonlight on your face and your cock still buried in her, still hard, still twitching, and the last thing you hear before the dark comes down over Ward Four is Bryony giggling, and the bed starting to squeak again.\n{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(6)
    jump wit_dawn_two

## ---- NIGHT 2, In heat (Witches Dawn Two, Fence Two, Linen Room) ----------------------------

## Dawn on the bench: the polo inside out; rung 2's growth beat; the report, the purple scribbled
## out and showing through; the Description of hostile read out; "Back in at ten, Kettering."
label wit_dawn_two:
    $ wit.fit = "kit"
    $ vn_enter(bg="wit_hut", pc="outraged", pc_tag="wit_pc", cast=[], cg="wit_bench_dawn")
    show cg wit_bench_dawn onlayer cgl
    "You wake up on the bench in the guard hut."
    "Grey light in the window. The kettle ticking as it cools. The supervisor in her chair with her crossword, exactly where she was. You're flat on your back on the hard wooden bench with your boots on and your torch lying on your chest, switched off, like somebody tucked you in with it."
    wit_you "\"Rufus. NIALL—\""
    "You sit bolt upright."
    wit_super "\"Not back.\""
    "She fills in a word."
    "Your polo shirt's on inside out. The label's sticking up under your chin. You stare down at it, and then at the window, at the wing, black against the dawn, with every door shut and not one light on, and nobody coming out of it."
    hide cg onlayer cgl
    "You take your polo off to turn it the right way round."
    $ wit_body(2)
    wit_you "{color=#ff5fb8}\"What— what the {i}hell{/i}—\"{/color}"
    "{color=#ff5fb8}Your chest is bare. Properly bare. That dusting of dark hair you've had for years, gone. The line of it down your stomach, gone. You rub your belly and your palm slides over skin as smooth as the inside of your arm, and it feels so {i}nice{/i} under your own hand that you do it again before you can stop yourself.{/color}"
    wit_you "\"No. No, no, no. Who's— who SHAVED me—\""
    "{color=#ff5fb8}You yank up the leg of your cargo trousers. Your shin's bare. Bare and pale and smooth as a leg in a razor advert. You yank up the other one. Same. Nobody shaved you. There's not a nick, not a bump, not a single hair from your neck to your toes. Just skin, soft and warm and smooth, all of it, and when you run your hand up your own thigh to check, your whole leg shivers.{/color}"
    wit_you "\"{i}Hah{/i}— that's— stop that—\""
    "{color=#ff5fb8}It's not just smooth. It's {i}soft{/i}. Your skin's gone soft all over, like you've been at your mum's moisturiser for a year, and it's sensitive. Your boxers brush the head of your cock when you shift on the bench, the lightest little rub of cotton, and your cock jumps and fills so fast you gasp out loud.{/color}"
    wit_you "\"{i}Ahh{/i}— oh, for God's {i}sake{/i}—\""
    "{color=#ff5fb8}You bite your lip to shut yourself up, and that's worse. Your lips are fuller. Plump and tender and tingling, and the press of your own teeth on them goes straight down your body like a plucked string, and a moan comes out of you, loud, in the guard hut, in front of the supervisor.{/color}"
    wit_you "\"{i}Mmh{/i}— I'm— that was a cough. That was a COUGH.\""
    "The supervisor fills in another word."
    show cg wit_window_two onlayer cgl
    "{color=#ff5fb8}You catch your reflection in the dark window. Your hair's longer. Dark and soft and falling over the tops of your ears where it was clipped short yesterday. And your lashes are darker, thick and black, like you've put mascara on, which you have NOT, and under them your grey eyes look enormous and startled and, there's no other word for it, pretty.{/color}"
    "{color=#ff5fb8}And your hips, while you sit there glaring at yourself, do a slow little roll on the bench. A smooth one. A practised one. Up and down, the exact way they bucked up into Bryony, like they've learned the rhythm and want you to know it. You clamp both hands on your thighs to stop them.{/color}"
    wit_you "\"No. Absolutely not.\""
    hide cg onlayer cgl
    "The incident report's on the clipboard by the kettle, the Northcott form, filled in already in a hand that isn't yours. And in the box marked {i}Officer's condition{/i}, in purple ink, in a big looping script with a flourish on the end, somebody has written a word."
    "You grab a biro. In {i}Action taken{/i} you write, hard enough to dent the paper: {i}Engaged hostile. Will clear tonight.{/i} Then you scribble the purple out. You scribble it out until the biro nearly goes through."
    show screen wit_report(2)
    "It shows straight through the biro. Every loop of it. Purple, under the blue, as if the ink's sitting on top of yours."
    wit_super "\"{i}Description of hostile.{/i} Female. Curly hair. Hat. Her thighs were very soft, like if a cloud was a thigh, and they were all warm when she sat on my—\""
    "She's got the clipboard. You didn't see her take it. She doesn't look up. Her voice is flat as a car park."
    wit_you "\"That's— give that BACK—\""
    wit_super "\"—and I keep thinking about them. Her thighs. They were the best thighs. Paragraph. Her thighs, continued.\""
    "She turns the page over."
    wit_you "\"I didn't WRITE that—\""
    wit_super "\"There's a small heart at the bottom, with an arrow through it.\""
    hide screen wit_report
    "She puts the clipboard on the side. She fills in fourteen across."
    wit_super "{b}\"Rufus and Niall still missing. Back in at ten, Kettering.\"{/b}"
    wit_you "\"Ten? Back in? We need the police, we need— somebody needs to go in there NOW and—\""
    wit_super "\"Police don't go in after dark.\""
    wit_you "\"Why not?\""
    "She doesn't answer. She fills in another word."
    "You stand there in the grey morning with your polo in your hands, smooth and soft all over, your lips buzzing, your cock half hard in your cargo trousers for no reason at all. Through the window, up on the wing, a curtain moves on the third floor."
    "And all you can think about, all you can think about, is Bryony's thighs."
    wit_you "\"For God's {i}sake{/i}.\""
    "You tell the kettle.\n{size=-5}{color=#ff8fa3}▸ Sleep through the day{/color}{/size}"
    $ vn_until(21)
    jump wit_fence_two

label wit_fence_two:
    $ vn_enter(bg="wit_fence", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    show screen wit_status(2)
    "Nine o'clock. The floodlight buzzing. The fence and its yellow signs going off into the dark either side of the hut, and the wing behind it, black, with that lavender smell drifting out through the chain-link."
    hide screen wit_status
    "You slept all day on the camp bed in the back of the hut. You dreamt about thighs."
    "The kit's on the side. Tonight it's a bigger bag of salt, the full-size council one with GRIT stencilled on it, and a second torch, which you tuck into your belt like a gun. You check both torches twice. You check the radio. Rufus's channel is dead air. Niall's is dead air."
    "You go to the gate and rattle it, for the form of the thing. Locked."
    wit_super "\"Gate's shut till your shift's done.\""
    "From inside the hut, not looking up."
    wit_you "\"I know. I'm going IN. I'm not trying to get OUT.\""
    "She turns a page of the paper."
    "You heft the salt onto your shoulder. You've got a plan this time. Tonight, you're not stopping to look at anybody.\n{size=-5}{color=#ff8fa3}▸ Through the gate{/color}{/size}"
    $ vn_until(22)
    jump wit_linen_room

## Rung 2: the linen room. Rowena on the trolley; Charm, and he digs his heels in; half the grit; she
## laughs till she snorts; the pink puff: In heat. Silence takes his voice. The porter's chair.
label wit_linen_room:
    $ vn_enter(bg="wit_linen", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "The linen room is on the first floor, at the end of a corridor full of moonlight. Shelves to the ceiling, every one stacked with old sheets gone yellow at the folds. A laundry trolley with a canvas sack on it. And in the corner, under the window, an old porter's chair, a big wooden one with arms, the leather seat worn shiny."
    show wit_rowena amused at vn_cast_slot
    show cg wit_rowena_trolley onlayer cgl
    "Somebody's sitting on the trolley, swinging her legs."
    "Red hair, loads of it, tumbling down her back. Freckles everywhere. Two small curled horns, and a witch's hat jammed on between them at an angle that defies physics. Violet eyes. A skirt hitched up over her knees. She's eating something out of a paper bag."
    wit_rowena "\"Evening, Pretty.\""
    wit_you "\"Don't call me— how do you know— that's not my NAME—\""
    "She grins. Your legs take a step towards her. Charm, sweet and stupid, filling you up from the toes, because she's smiling at you and she's {i}so{/i} pretty. Another step. Another."
    "You dig your heels in. You actually dig your heels in, the soles of your work boots squeaking on the lino, and you lean back like you're in a tug of war with nobody, and you stop."
    wit_you "\"HA. Didn't work. Northcott Security. You're trespassing.\""
    wit_rowena "\"Ooh, he's got a {i}big{/i} bag tonight.\""
    menu:
        "\"Ooh, he's got a {i}big{/i} bag tonight.\""
        "Empty half the bag at her":
            pass
        "Tell her you're armed first":
            wit_you "\"I'm armed. With GRIT. Council issue.\""
            wit_rowena "\"Ooh.\""
    show cg wit_grit onlayer cgl
    "You get the bag of grit off your shoulder, rip the top open, and empty half of it at her in one long white swing."
    "It goes everywhere. It pours over her hat and down her front and into the sack on the trolley and all over the floor, a little avalanche of salt, rattling on the lino for ages."
    hide cg onlayer cgl  # ff 1:46 am ET 11-18: no picture, wit_rowena_laugh failed 4 draws (SCENES.md witches v4)
    "She looks down at herself. She looks up at you. And she laughs. She laughs so hard she has to hold onto the trolley, she laughs till she snorts, and then she laughs at the snort, and wipes her eyes on her sleeve, and shakes salt out of her hat."
    wit_rowena "\"Oh, I {i}like{/i} you. I'm Rowena. Here. Have one of mine.\""
    "She wheezes it. She holds up her palm, flat, like she's offering you a sweet, and blows across it. A warm pink puff, soft as breath on a cold window, drifts across the linen room and right into your face."
    call wit_ting("In heat")
    wit_you "\"What was— that's an offence, that is, you can't just BLOW things at a—\""
    "You open your mouth to radio it in. You key the radio. You take a breath."
    "Nothing comes out."
    "Nothing at all. Your mouth moves, your throat works, you can feel yourself shouting, and there's not a sound in the room but the salt still trickling off the trolley. You try again. You try to swear. Silence. Rowena watches you do it, one hand over her mouth, shaking."
    show wit_pc flushed
    show cg wit_heat onlayer cgl
    "And then the heat hits." with vnfx("shake")
    "It comes up from your belly like somebody's opened an oven. It floods your face and your neck and the tips of your ears, and it goes {i}down{/i}, all of it, straight down, and your cock gets hard so fast it's like being punched. It strains up against your zip, throbbing, so hard it's almost funny, and your whole body's flushed and damp and buzzing with it, your knees shaking, your hands opening and closing on nothing."
    wit_rowena "\"Ooh. There it is.\""
    "Hopping down off the trolley. You back away. You back away silently, mouthing every swear word you know, and she just walks after you, laughing, and puts both hands on your chest, and shoves."
    hide wit_rowena
    show cg wit_chair_shove onlayer cgl
    "The porter's chair catches you behind the knees. You sit down in it hard. The old wood creaks."
    "She hitches her skirt up round her waist. She's not wearing anything under it either. None of them are, apparently. She climbs right into the chair with you, one knee either side of your hips on the worn leather, facing you, her freckled breasts in your face, and gets your belt open and your zip down with one hand, and your cock springs out, red and hard and leaking, and she wraps her fingers round it and looks at it and grins."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Ooh, he's {i}cooking{/i}. Look at him.\""
    "You mouth GET OFF at her. Not a sound."
    show cg wit_rowena_sink onlayer cgl
    "She sinks down.\n{size=-5}{color=#ff8fa3}▸ Not a sound{/color}{/size}"
    jump wit_linen_room_sex

## Rung 2's last beat inside the act: the voice back and saying no on every stroke, his own hands on
## her hips; he came long ago and didn't go soft; he comes in her again; she starts again.
label wit_linen_room_after:
    $ vn_enter(bg="wit_linen", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_two_hands")
    vn_sfx "{i}Creak, creak, creak, creak.{/i}"
    show cg wit_two_hands onlayer cgl
    wit_you "\"No— no— {i}no{/i}— nnh—\""
    "Your voice is back and it's saying no. One for every stroke. Rowena's bouncing in your lap so hard the old porter's chair is walking itself across the lino, a little hop at a time, and every time she comes down you say no, loud, right into her freckles."
    "And your hands are on her hips."
    "You didn't put them there. You look down at them like they belong to somebody else. Your own two hands, gripping her soft hips, pulling her down onto you every time she rises. Hard. Greedy."
    wit_you "\"No— hands— {i}stop{/i}— no—\""
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Look at him go! He can't stop!\""
    "Rowena throws her head back and cackles. Her hat falls off."
    "You came ages ago. You came the first time she sank all the way down, before your voice was even back, silently, your mouth wide open, pumping into her with your eyes rolled up, and it didn't make the slightest difference. You didn't go soft. You didn't even go a bit soft. The heat just kept you there, hard as a broom handle, flushed to the ears, and she just kept going."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Still hard? Course you are.\""
    "She squeezes round you."
    wit_you "\"No— no— {i}no{/i}—\""
    "It builds again. Faster this time. Your hands drag her down and hold her there and your hips grind up into her all on their own, and she grabs the back of the chair either side of your head and leans in and kisses you, open-mouthed, laughing right into your mouth, and that's it."
    show cg wit_two_cum onlayer cgl
    "You come inside her again, and you don't go soft."
    wit_you "\"Nnh— {i}NO{/i}— {i}mmmh{/i}—!\"" with vnfx("flash", "shake")
    "It goes on and on. You pump into her with your hands locked on her hips and her laughter in your mouth and the chair creaking like it's going to give up, and when it's over you're still hard. Still in her. Still flushed and buzzing and throbbing, exactly as hard as you were when she sat down."
    "Rowena shudders, and moans, long and loud and pleased, and comes all over your lap, squeezing you so tight your eyes cross. Then she sits back and looks at you, pink and sweaty and grinning, and pats your hot cheek."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Ooh, I'm going to win so much money on you.\""
    "And she starts again.\n{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(6)
    jump wit_dawn_three

## ---- NIGHT 3, Shrunk (Witches Dawn Three, Fence Three, Nurses Station) ---------------------

## Dawn: he wakes hard (In heat doesn't wear off); the hair at his jaw, the waist; "Withdrew."; the
## water pistol.
label wit_dawn_three:
    $ wit.fit = "kit"
    $ vn_enter(bg="wit_hut", pc="flushed", pc_tag="wit_pc", cast=[], cg="wit_bench_dawn")
    show cg wit_bench_dawn onlayer cgl
    "The bench. The kettle. The crossword. The torch on your chest. Your polo on inside out again."
    "You wake up hard."
    "Not morning hard. {i}Hard{/i} hard. Throbbing against the inside of your cargo trousers like it's been waiting for you to wake up so it can complain, and the moment you're awake the heat floods up into your face to match it."
    hide cg onlayer cgl
    wit_you "\"Oh, come {i}on{/i}—\""
    $ wit_body(3)
    "{color=#ff5fb8}You sit up, and your hair swings. It brushes your jaw. Soft dark hair, falling forward past your cheekbones, long enough to tuck behind your ear, which you do, without thinking, like you've been doing it for years. Then you realise what you've just done and yank your hand away.{/color}"
    "{color=#ff5fb8}You stand up, and your trousers sit differently. Your belt's on the same notch and there's a gap now, at the small of your back. Your waist's drawn in. Only a touch. Enough that when you put your hands on your hips to glare at the window, they sit in a curve that wasn't there yesterday.{/color}"
    wit_you "\"That's not— I don't HAVE a waist. Men don't HAVE waists—\""
    "{color=#ff5fb8}And your hips roll. Smooth, slow, practised, rocking forward and up, exactly the way they rocked up into Rowena in the porter's chair, like they've been practising all night without you. The motion drags your hard cock along the inside of your boxers and you have to grab the edge of the kettle counter.{/color}"
    wit_you "\"{i}Hah{/i}— {i}stop{/i} that— I'm not riding ANYTHING—\""
    show cg wit_kettle onlayer cgl
    "The heat doesn't go. You try a cold flannel. You try standing outside in the drizzle by the fence. You try thinking about your nan. Nothing. You're flushed all the way down your neck and hard in your cargo trousers and so short-tempered you snap at the kettle for taking too long to boil, and then you have to lean over it, both hands on the counter, breathing through your nose, because bending over to get the milk made your cock rub and you nearly came in your boxers."
    wit_super "\"Morning.\""
    wit_you "\"It's NOT.\""
    hide cg onlayer cgl
    "The incident report's on the clipboard. Another purple word under the first, looping, glossy."
    "You look at them for a long time. You don't scribble anything out. In {i}Action taken{/i}, very neatly, you write: {i}Engaged hostile. Withdrew.{/i}"
    show screen wit_report(3)
    wit_super "{b}\"Back in at ten, Kettering.\"{/b}"
    hide screen wit_report
    wit_super "\"Firm's sent an upgrade.\""
    "She doesn't look up. She nods at the side."
    show cg wit_water_pistol onlayer cgl
    "The upgrade is a water pistol. A big plastic one, the pump-action kind, lurid green, with a label on the tank in the Northcott office's handwriting: {i}BRINE{/i}."
    "You pick it up. It sloshes."
    wit_you "\"Right. {i}Right.{/i}\""
    "Through your teeth, still bent over the kettle.\n{size=-5}{color=#ff8fa3}▸ Sleep through the day{/color}{/size}"
    $ vn_until(21)
    jump wit_fence_three

label wit_fence_three:
    $ vn_enter(bg="wit_fence", pc="flushed", pc_tag="wit_pc", cast=[], cg=None)
    show screen wit_status(3)
    "You didn't sleep much. You slept face down on the camp bed with a pillow over your head, hard against the mattress, flushed, thinking about thighs and porter's chairs and how you are NOT going to think about thighs and porter's chairs."
    hide screen wit_status
    "Nine o'clock. The floodlight. The fence. The lavender coming through it."
    "You pump the water pistol till the tank's tight. You stick your torch in your belt. Your hi-vis is zipped up to the chin to hide how red your neck is, and your cock's still hard, and you've stopped expecting it not to be."
    wit_super "\"Gate's shut till your shift's done.\""
    wit_you "\"I KNOW.\"\n{size=-5}{color=#ff8fa3}▸ Through the gate{/color}{/size}"
    $ vn_until(22)
    jump wit_nurses_station

## Rung 3: the nurses' station. Cressida reading a chart; the brine pistol dribbles onto her boot;
## the wand on his nose: Shrunk, and the Shrink lands on the page, mid-fight. Slow. The desk.
label wit_nurses_station:
    $ vn_enter(bg="wit_nurses", pc="flushed", pc_tag="wit_pc", cast=[], cg=None)
    "The nurses' station is on the second floor, where four corridors meet: a big curved desk heaped with old paper charts in brown card folders, a swivel chair, and a clock on the wall above it that stopped at some point a long time ago."
    show wit_cressida amused at vn_cast_slot
    show cg wit_cressida_desk onlayer cgl
    "There's a witch behind the desk, reading a chart."
    "Dark hair scraped back in a bun. Pointed ears. Violet eyes behind a pair of spectacles on a chain. A black robe buttoned to the throat over the biggest, heaviest pair of breasts you have ever seen in your life, resting on the desk in front of her like she's put them down to read."
    "She turns a page."
    menu:
        "She turns a page."
        "Level the pistol, both hands":
            wit_you "\"Northcott Security. You're trespassing.\""
            "You level the water pistol at her with both hands, the way they do on telly."
        "Read her the site rules":
            wit_you "\"Northcott Security. You're trespassing. No smoking, no naked flames, no interfering with the fixtures and fittings—\""
            "You level the water pistol at her one-handed, reading the card with the other."
    wit_cressida "\"Mm.\""
    "She doesn't look up."
    wit_you "\"I'm armed.\""
    wit_cressida "\"Mm.\""
    show cg wit_pistol_dribble onlayer cgl
    "You pull the trigger."
    vn_sfx "{i}Pfft.{/i}"
    "A thin little stream of brine arcs out of it, wobbles, and dribbles onto the floor, just short of the desk, just far enough to land on the toe of her boot. {i}Plip.{/i}"
    "You both look at it."
    wit_cressida "\"Huh.\""
    "She closes the chart. She sighs, the long tired sigh of somebody who's been asked to do overtime, and stands up, and reaches over the desk with a slim black wand, and taps you, once, on the end of your nose."
    vn_sfx "{i}Boop.{/i}"
    call wit_ting("Shrunk")
    show cg wit_shrink onlayer cgl
    $ wit_body("3s")
    wit_you "{color=#ff5fb8}\"Wh— {i}whoa{/i}—\"{/color}"
    "{color=#ff5fb8}It goes through you like a shiver. Top to bottom. And everything goes {i}smaller{/i}.{/color}"
    "{color=#ff5fb8}Your belt gives first. One notch's worth of slack, then more, and your cargo trousers slide down off your waist and settle low on your hips, the waistband gaping. Your hi-vis goes loose on you all at once and hangs off your shoulders like a borrowed coat. Your polo collar gapes at your throat. Your boots go loose round your feet.{/color}"
    wit_you "\"No— no, no— what did you DO—\""
    "{color=#ff5fb8}You're slighter. Everywhere. Your shoulders narrower, your wrists finer, your hands neater round the water pistol. Softer, too, all over, a soft give under your skin where there used to be wiry nothing. Petite. That's the word that shoves itself into your head and you hate it. You're still you. You're still a grown man, twenty-four, with a job and a mortgage application in progress, just a slighter, softer, prettier one, standing in an empty hospital in a hi-vis that doesn't fit.{/color}"
    "{color=#ff5fb8}And your cock. It's smaller. You can feel it, a different weight against your thigh. Smaller, and every bit as hard as the heat's kept it all day, so hard it's sticking straight out of the gap in your sagging trousers and bobbing about in the air, red and stiff and ridiculous, in front of a witch.{/color}"
    "{color=#ff5fb8}It's more sensitive, too. The air on it. The hem of your polo brushing the tip. You gasp out loud.{/color}"
    wit_you "\"{i}Ahh{/i}— that's— no— that's even WORSE—\""
    "The witch looks at it, over her spectacles."
    wit_cressida "\"Mm.\""
    show cg wit_syrup onlayer cgl
    "You drop the water pistol. You grab your trousers in one fist and you turn and you run for the door."
    "Except you don't run. You move like you're wading through syrup. Every step takes about a year. Your foot lifts, and drifts, and comes down. Your hand reaches for the door frame and gets there sometime next week. You can see the corridor. You can see the stairs. You're going so {i}slowly{/i}."
    wit_you "\"Nnnnnooooo.\""
    "Very slowly."
    wit_cressida "\"Cressida.\""
    "Behind you, by way of introduction. She's not hurrying. She doesn't need to. She walks round the desk, takes you by the front of your hi-vis, and turns you round, and walks you backwards. One step. Two. Your heels bump the desk."
    hide wit_cressida
    show cg wit_desk_push onlayer cgl
    "She pushes you down onto your back on top of it. Charts slide out from under you and spill off the edge onto the floor in a slow brown flurry. You land among them with your trousers round your hips and your cock pointing at the stopped clock."
    wit_you "\"Put me— DOWN— I mean— get OFF me—\""
    "She climbs up onto the desk after you. She unbuttons her robe, top to bottom, unhurried, and her breasts come free, enormous and soft and heavy, pale in the moonlight. She takes both your wrists in one hand and pins them to the desk above your head, among the charts, and swings a knee over you, and sits up astride your hips."
    wit_you "\"No— no— I'm— on SHIFT—\""
    show cg wit_cressida_sink onlayer cgl
    "She takes your cock in her free hand. Smaller now, and still as hard as the heat keeps it, twitching against her palm. She lines it up and sinks down onto it, slow, slow as everything else tonight, hot and wet and squeezing, until she's sitting on you to the root."
    "Then she leans forward."
    "Your face goes into her breasts. Warm. Heavy. Soft. Everywhere. Your whole face pressed in between them, your nose, your mouth, your yelling."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Hold still, gorgeous. Slow suits you.\""
    "Flat as anything.\n{size=-5}{color=#ff8fa3}▸ Mmph{/color}{/size}"
    jump wit_nurses_station_sex

## Rung 3's last beat inside the act: every yell into her breasts comes out a moan; Slow makes even
## the climax slow; still hard; "Mm. Again."
label wit_nurses_station_after:
    $ vn_enter(bg="wit_nurses", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_three_peak")
    show cg wit_three_peak onlayer cgl
    wit_you "\"Mmph— {i}mmph{/i}— put me— DOWN—\""
    "It goes into her breasts and comes out a moan. Everything does. Every swear, every order, every no. You're yelling at the top of your lungs into the softest, warmest, heaviest pair of breasts in the world and it comes out {i}mmmh{/i}."
    "Cressida rides you at her own pace. Slow. Unbothered. Rolling her hips like a tide coming in. And you buck up into her, you can't help it, Charm and heat and the way she feels, except you buck {i}slowly{/i}, you buck like a film on half speed, your hips drifting up to meet her and drifting back down, and she meets every one with a lazy little squeeze that makes your toes curl in your loose boots."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Mm. There.\""
    wit_you "\"Mmnh— fhor God'sh— {i}shake{/i}—\""
    "Her hand's still round your wrists. She hasn't moved it once. Her other hand's in your hair now, stroking it, absent-minded, the way you'd stroke a cushion, while she rides you."
    "It comes up slow too. That's the worst part. You can feel it coming for ages, building and building at Slow's own pace, a long sweet heavy pull from the soles of your feet all the way up, and nothing you do can make it go faster or stop, and she just keeps rolling her hips, and you just keep yelling into her."
    show cg wit_three_cum onlayer cgl
    "You come yelling into her breasts."
    wit_you "\"{i}MMMPH{/i}— {i}mmmmh{/i}— {i}mmmmmh{/i}—!\"" with vnfx("flash", "shake")
    "It takes forever. Every pulse drawn out long and slow and shuddering, your hips stuck halfway up off the desk, your cock throbbing inside her for what feels like forever, by the stopped clock on the wall. Cressida rides you through it without changing pace at all."
    "When it's over you're still hard. The heat sees to that. You're still in her, and your face is still in her, and she's still rolling."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Mm. Again.\"\n{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(6)
    jump wit_dawn_four

## ---- NIGHT 4, Sensitive (Witches Dawn Four, Fence Four, Day Room, Exam Room) ---------------

## Dawn: slight shoulders, puffy nipples on a flat chest, the waist, the hips, the arse, the hair on
## his shoulders; "Engaged."; the women's-cut kit from the stores; the extinguisher.
label wit_dawn_four:
    $ wit.fit = "kit"
    $ vn_enter(bg="wit_hut", pc="outraged", pc_tag="wit_pc", cast=[], cg="wit_bench_dawn")
    show cg wit_bench_dawn onlayer cgl
    "The bench. The kettle. The crossword. The torch on your chest, and your polo on inside out, and this morning it's hanging off you like a tent."
    hide cg onlayer cgl
    wit_you "\"Oh, you are JOKING—\""
    $ wit_body(4)
    hide cg onlayer cgl  # ff 1:46 am ET 11-18: no picture, wit_four_polo failed 4 draws (SCENES.md witches v4)
    "{color=#ff5fb8}You sit up, and the polo slides off one shoulder. Your shoulders are slight now. Narrow and smooth and sloping, and the collar of your polo just falls off the edge of one like it's given up. You grab it and drag it back, and your fingertips brush your chest through the cotton.{/color}"
    wit_you "\"{i}Hnn{/i}—!\""
    "{color=#ff5fb8}Your nipples. You pull the polo up and look, and your chest is still flat, still a man's chest, smooth and flat, but your nipples have gone puffy. Pink and swollen and soft, standing up in two puffy pink points, like they're begging for something, and the cotton dragging over them felt like a tongue.{/color}"
    wit_you "\"No. No, no. Put them— put them BACK—\""
    show cg wit_four_trousers onlayer cgl
    "{color=#ff5fb8}You stand up and your cargo trousers fall down.{/color}"
    "{color=#ff5fb8}They just fall. Belt and all. Off your hips and round your ankles in one go, because your waist's gone narrow, properly narrow, a real curve in at the middle, and the hips under it have rounded out. Soft and round and wider than your waist now, so the line of you goes in and then out, and behind you, when you twist round to look, there's an arse. A soft, round, bitable arse in your Northcott boxers, the cotton pulled tight across it, wobbling when you twist.{/color}"
    wit_you "\"That's not— whose— I've never HAD an arse—\""
    "{color=#ff5fb8}Your hair's on your shoulders. Soft and dark and swinging. And your hips, while you stand there in your boxers yelling at your own reflection, do that roll again, that smooth practised rock, so neat and so sure you could do it on a stage, and your hard cock bobs in your boxers with it.{/color}"
    wit_you "\"Stop DOING that. I am not— I don't— {i}ahh{/i}—\""
    hide cg onlayer cgl
    "The incident report's on the clipboard. Another purple word at the bottom of the column, under the others, like a shopping list."
    "You read them out loud. Under your breath. Slowly. You don't know why you're doing it. It feels like the sort of thing you'd do at a bus stop if you'd gone a bit funny."
    show screen wit_report(4)
    "In {i}Action taken{/i} you write one word."
    hide screen wit_report
    hide cg onlayer cgl  # ff 1:46 am ET 11-18: no picture, wit_stores_kit failed 4 draws (SCENES.md witches v4)
    "None of your kit fits. The polo hangs off your shoulders, the trousers won't stay up even with the belt on its last notch, and the hi-vis is a tent. You go to the stores cupboard at the back of the hut and dig through the boxes, and the only things in your size are the women's cut: a black fitted polo, short in the sleeve, and black trousers, slim through the leg."
    "You stare at them for a long time."
    $ wit.fit = "women"
    "Then you put them on, because the alternative is going on shift in your boxers. The trousers go up over your new hips and sit snug and smooth over your arse like they were made for it. The polo hugs your narrow waist. It fits. It all fits perfectly. You look like a Northcott advert for a job you'd never apply for."
    hide cg onlayer cgl
    wit_super "{b}\"Back in at ten, Kettering.\"{/b}"
    "Not looking up."
    wit_you "\"Look at me. LOOK at me. Look at what they're DOING to—\""
    wit_super "\"Firm's sent an upgrade.\""
    "She fills in a word."
    hide cg onlayer cgl  # ff 2:36 am: no picture, extinguisher failed 4 draws (SCENES.md witches v5)
    "It's a fire extinguisher. A big red one, the proper kind, with a hose and a pin and a tag on the handle in the Northcott office's handwriting: {i}REFILLED: ROCK SALT{/i}."
    wit_you "\"Right. {i}Right.{/i}\""
    "You hug it to your chest.\n{size=-5}{color=#ff8fa3}▸ Sleep through the day{/color}{/size}"
    $ vn_until(21)
    jump wit_fence_four

label wit_fence_four:
    $ vn_enter(bg="wit_fence", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    show screen wit_status(4)
    "Nine o'clock. You've got the extinguisher on its strap over your shoulder, and it bumps your new hip every time you move, and every time it bumps your hip your hips roll with it, because that's what they do now."
    hide screen wit_status
    "Your women's-cut polo drags across your puffy nipples with every breath. You've been breathing very shallowly all day."
    "You march up to the gate. You pull the pin on the extinguisher, for practice, and put it back in."
    wit_super "\"Gate's shut till your shift's done.\""
    wit_you "\"Tonight, it's DIFFERENT.\""
    "You tell the wing, through the fence.\n{size=-5}{color=#ff8fa3}▸ Through the gate{/color}{/size}"
    $ vn_until(22)
    jump wit_day_room

## Rung 4: the day room. Rufus in blue pyjamas and a belled collar, content, with three other men in
## collars. "Go on without me, Em." "Nobody gets left in here." (Emrys's, exactly once at rung 4.)
label wit_day_room:
    $ vn_enter(bg="wit_day_room", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "On the ground floor, on your way in, there's a door you haven't tried before, with light coming under it and a sound you know."
    "The telly."
    "You shoulder the door open with the extinguisher up and ready, and stop dead."
    show cg wit_day_room_men onlayer cgl
    "It's the old day room. Big saggy armchairs in a half circle, the kind with wooden arms and flowery cushions. A rug. A standard lamp with a fringe on the shade. An old telly on a trolley in the corner, the big heavy kind, showing a quiz programme with the sound down low. On the coffee table, a plate of custard creams."
    "And in the armchairs, men."
    "Grown men, in soft pyjamas, curled up comfy with their feet tucked under them, watching the quiz. Every one of them has a soft leather collar on, with a little brass bell at the front. One of them's in a council surveyor's fleece over his pyjama top. One of them's in a Northcott hi-vis, a bit faded, like it's been here since last spring."
    "And in the biggest armchair, right in front of the telly, in blue pyjamas, with a custard cream in his hand and a brass bell on his collar, is Rufus."
    wit_you "\"RUFUS.\""
    hide cg onlayer cgl
    show wit_rufus content at vn_cast_slot
    wit_rufus "\"Em. You alright?\""
    "He looks up and smiles. A big soft calm smile you've never seen on him. His bell goes {i}ting{/i}."
    show wit_pc outraged
    wit_you "\"Am I— am I ALRIGHT— Rufus, get UP, get your boots on, we're going— where are your BOOTS—\""
    wit_rufus "\"Don't need them. Go on without me, Em. I'm alright here.\""
    "He settles deeper into the armchair. His bell tinkles. On the telly, somebody's won a caravan. The other men in the armchairs make a soft, pleased noise, all together."
    "You stand in the doorway in your women's-cut kit with the extinguisher in your arms and your face burning and your hair on your shoulders, and you look at him. Big, steady Rufus. Ex-army. Never flustered. Curled up in an armchair in his jim-jams with a bell on."
    wit_you "{b}\"No. No. Nobody gets left in here.\"{/b}"
    "Rufus smiles at you. Then he pats the seat of the armchair beside his, the empty one, twice, like he's saving it for you."
    "And turns back to the telly."
    hide wit_rufus
    "You stand there for a long moment. Then you back out of the door, and close it, very gently, and stand in the corridor with your forehead on the cold green paint."
    wit_you "\"Right. {i}Right.{/i} This is going in the REPORT.\""
    "You tell the paint.\n{size=-5}{color=#ff8fa3}▸ Up to the examination room{/color}{/size}"
    $ vn_pass(5)
    jump wit_exam_room

## Rung 4: the examination room. The whole extinguisher in a white roar; Elspeth with a salt
## moustache; the feather on his cheek: Sensitive. The ribbon (Bound); the couch; the feather on his
## nipples and he comes before she's on him; she climbs on facing away.
label wit_exam_room:
    $ vn_enter(bg="wit_exam", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "The examination room is up a short flight of stairs at the end of the corridor: a high padded couch with a metal rail along the top of it, a folding screen on wheels, a cabinet full of empty brown bottles, and a big round lamp on an arm, switched off. It smells of lavender and, very faintly, of biscuits."
    show cg wit_exam_screen onlayer cgl
    "There's somebody behind the screen. You can see her feet, swinging. You can hear her giggling."
    wit_you "\"Northcott Security. You're trespassing.\""
    "A giggle."
    wit_you "\"Come out with your hands where I can see them.\""
    "A bigger giggle."
    wit_you "\"Right. RIGHT.\""
    menu:
        "A bigger giggle."
        "Squeeze the handle as hard as you can":
            pass
        "Count her in first, properly":
            wit_you "\"I'm going to count to three. One. Two—\""
            "She giggles on two. That'll do."
    hide cg onlayer cgl  # ff 2:36 am: no picture, salt-cloud failed 4 draws (SCENES.md witches v5)
    "You yank the pin out of the extinguisher, aim the hose at the screen, and squeeze the handle as hard as you can."
    vn_sfx "{i}FWOOOOOOOSSSHHH.{/i}" with vnfx("shake")
    "It goes off like a jet engine. A great roaring white cloud of rock salt blasts out of the hose and hits the screen and knocks it flat and keeps going. It goes over the couch and up the walls and into the cabinet and across the ceiling. You hold the handle down with your teeth gritted and sweep it left and right and up and down until the extinguisher coughs and splutters and gives one last sad {i}pfft{/i} and stops."
    "The cloud settles. Slowly. Salt pattering down like snow."
    hide cg onlayer cgl  # ff 2:42 am: no picture, salt-moustache failed 4 draws (SCENES.md witches v6)
    "Everything in the room is white. The couch. The cabinet. The lamp. The walls. You. Your women's-cut kit. Your eyelashes."
    "Everything except the witch sitting cross-legged on the examination couch, untouched, freckled and stubby-horned and violet-eyed, with a quill tucked behind one ear, and a big white moustache of salt on her top lip."
    "She giggles so hard she falls over sideways on the couch."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Again! Do it AGAIN!\""
    wit_you "\"It's— it's EMPTY—\""
    wit_elspeth "\"Aww.\""
    "She sits up and wipes off the moustache with the back of her hand, still giggling, and hops down off the couch. She's quick, and before you can get the empty extinguisher up like a club she's right in front of you, and she takes the quill from behind her ear, and brushes your cheek with the very tip of the feather."
    wit_elspeth "\"I'm Elspeth!\""
    call wit_ting("Sensitive")
    show wit_pc flushed
    show cg wit_feather_cheek onlayer cgl
    wit_you "{color=#ff5fb8}\"{i}AHH{/i}—!\"{/color}" with vnfx("shake")
    "{color=#ff5fb8}The feather barely touched you. It barely touched your {i}cheek{/i}. And it went through your whole body like you'd been plugged into the mains.{/color}"
    "{color=#ff5fb8}Your cock jerks so hard in your slim black trousers that you yelp. It's throbbing. Just from that. From a feather on your face. The fabric of your boxers is suddenly the roughest, most unbearable, most incredible thing in the world, every thread of it, dragging on the head of you every time you breathe.{/color}"
    wit_you "\"Nnh— {i}ahh{/i}— my— why is it— why is it SO—\""
    "{color=#ff5fb8}And your nipples. The fitted polo, lying on them. Just {i}lying{/i} on them. Your puffy pink nipples are on fire under the cotton, buzzing, so sensitive that the next breath you take drags the polo across them and your knees nearly go.{/color}"
    wit_you "\"{i}Hah{/i}— don't— don't BREATHE— why can't I breathe without— {i}ahh{/i}—!\""
    "{color=#ff5fb8}Your new arse, in your snug trousers, tingles all over. The seam pressing up between your cheeks feels like a finger. You clench, and that's worse, that's so much worse, a hot throbbing shiver right at your hole that makes you rise up on your toes.{/color}"
    wit_you "\"Nnnh— NOT there— there's nothing THERE—\""
    "{color=#ff5fb8}And your lips. You lick them without thinking, and your own tongue on your own lips makes you moan like you've been kissed all night. Loud. In front of a witch.{/color}"
    wit_you "\"{i}Mmmh{/i}— oh, for— I did NOT just— {i}ahh{/i}—\""
    wit_elspeth "\"Ooh, {i}listen{/i} to him.\""
    "Clapping."
    hide wit_elspeth
    show cg wit_ribbon onlayer cgl
    "Something soft and purple drifts down out of nowhere. A ribbon. A wide silky purple ribbon, like off a birthday present, and it loops itself round your wrists, both of them, once, twice, and ties itself in a bow, and draws your hands up in front of you as gently as anything."
    vn_sfx "Clunk."
    "The extinguisher clunks on the floor."
    wit_you "\"No— hey— untie— UNTIE this, that's— that's restraint of an officer—\""
    show cg wit_couch_tie onlayer cgl
    "Elspeth takes you by the end of the ribbon and walks you backwards to the couch. Every step makes your trousers rub you. Every step makes you gasp. She pushes you down on your back on the padded couch, in the salt, and draws your bound wrists up over your head, and ties the end of the ribbon to the metal rail with a double knot."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"There! Snug as anything.\""
    wit_you "\"Untie it— UNTIE it—\""
    $ wit.fit = "nude"
    "She tugs your trousers down to your knees. Your cock springs up, smaller than it was, red and shining and so hard it's twitching against your belly. She doesn't touch it. She puts her fingertips on your hip instead. Just her fingertips. Just resting."
    wit_you "\"{i}Ahh{/i}— don't— that's TOO— that's too MUCH—\""
    "She pushes your polo up to your armpits. Your puffy nipples are standing up pink and swollen in the cold air of the examination room. She looks at them. She looks at the feather. She looks at you."
    wit_you "\"Don't. Don't you DARE. Don't you dare do the—\""
    show cg wit_feather_nipples onlayer cgl
    "She draws the feather once across your nipples. Left, then right. Barely touching."
    wit_you "\"{i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    "You come. Right there. Before she's even on you. Your back arches off the couch and your cock jerks against your belly with nobody touching it, nobody anywhere near it, and you spurt all over your own stomach in long hot ropes, yelling at the ceiling, your bound hands yanking at the rail."
    "Elspeth gasps, delighted. She does it again. The feather, left, right."
    "And you come {i}again{/i}." with vnfx("flash")
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Again? You've gone again!\""
    "She squeals it."
    wit_you "\"Nnh— {i}stop{/i}— stop the— the FEATHER—\""
    "You're panting. You're dripping. You're still hard. You haven't been soft since Rowena, and you aren't now. Your cock just stands there, wet and red and twitching, waiting for more."
    show cg wit_elspeth_sink onlayer cgl
    "Elspeth hitches up her robe and climbs onto the couch. She swings one leg over you, facing away, towards your feet, her round bum right in front of you, and looks back over her shoulder at you, giggling, and takes your cock in her hand, and sinks down onto it.\n{size=-5}{color=#ff8fa3}▸ No— not again—{/color}{/size}"
    jump wit_exam_room_sex

## Rung 4's last beat inside the act: a come on every touch; her finger, the first thing that's ever
## been there; the noes melting into one long broken moan; "Again?"
label wit_exam_room_after:
    $ vn_enter(bg="wit_exam", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_four_finger")
    show cg wit_four_finger onlayer cgl
    wit_you "\"No— nnh— not ag— {i}ahh{/i}—\""
    "Every touch. Every single touch. Elspeth's bouncing on your cock facing away from you, her round bum rising and falling, the couch squeaking, the salt crunching under you, and every time she comes down it's too much, and every time she brushes your thigh with the feather it's too much, and every time you say no you come."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Ooh, and again!\""
    wit_you "\"No— no— {i}don't{/i}— {i}ahhh{/i}—\""
    "You've lost count. You don't want to count. You're wet from your nipples to your knees and your bound hands are clutching at the rail and your hips just keep pushing up into her, and somewhere in the middle of it she slicked a finger in her mouth, giggling, and reached back between your legs, and pressed it to your arse."
    "The first thing that's ever been there."
    wit_you "\"No— not THERE— nobody's EVER— {i}hahh{/i}—\""
    "She pushed it in. Slow. Just the one finger, slick and warm, sliding into you to the knuckle while she rode you, and your whole body locked up and your eyes rolled back and the no came out of you as a long wobbling wail."
    "It's still in there. It's been in there for ages. Working in and out of you, curling, while she bounces, and every time it moves your cock jumps inside her, and every time your cock jumps she giggles."
    wit_you "\"No— nnnh— {i}ahh{/i}— {i}ahhh{/i}—\""
    "The noes are going. You can hear them going. They're melting, one into the next, into one long broken noise that doesn't have a no in it any more, just a moan, high and wavering and helpless, going on and on."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Shall I do the thing? I'm doing the thing.\""
    "Over her shoulder, pink-cheeked and delighted. Her finger crooks, and you come again."
    show cg wit_four_cum onlayer cgl
    wit_you "\"{i}AHHHHH{/i}—!\"" with vnfx("flash", "shake")
    "It goes off right behind your cock, like she's pressed a button, a deep hot throb that milks you from the inside, and you spurt into her so hard your heels drum on the couch. She squeals and comes too, squeezing down round you, and keeps her finger right there, pressed, crooked, so the throb just keeps going, and going, and you're moaning so loud the empty bottles rattle in the cabinet."
    "When it finally lets go of you, you're still hard. Of course you are."
    "Elspeth wiggles her finger. You squeak."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Again?\""
    "Thrilled.\n{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(6)
    jump wit_dawn_five

## ---- NIGHT 5, Obedient (Witches Dawn Five, Fence Five, Side Ward) --------------------------

## Dawn: his thighs touch; a lighter voice; wide hips, a heart-shaped arse; the hair past his
## shoulders; Action taken left blank, the doodled hat; the fertiliser spreader.
label wit_dawn_five:
    $ wit.fit = "women"
    $ vn_enter(bg="wit_hut", pc="outraged", pc_tag="wit_pc", cast=[], cg="wit_bench_dawn")
    show cg wit_bench_dawn onlayer cgl
    "The bench. The kettle. The crossword. The torch. You wake up with your polo on inside out and your hands tucked between your thighs."
    hide cg onlayer cgl
    $ wit_body(5)
    "{color=#ff5fb8}Your thighs are touching.{/color}"
    wit_you "\"No— {i}no{/i}— what's— oh, for God's {i}sake{/i}—\""
    "{color=#ff5fb8}Your own voice stops you. It came out light. Lighter than yesterday. Still yours, still a bloke's, just lighter and softer at the edges, like somebody's sanded it. You say \"for God's sake\" again to check, deeper, gruffer. It comes out the same. Lighter. Prettier.{/color}"
    show cg wit_five_hips onlayer cgl
    "{color=#ff5fb8}You stand up and your hips stand up with you. Wide, now. Wide and soft and rounded, wider for your frame than they've got any right to be, swaying out from your narrow waist. The women's-cut trousers are tight on them. Properly tight, the seams straining, and when you twist round to look, your arse is round and soft and heart-shaped in them, full at the bottom, pushing the fabric out, and it bounces. When you walk, it bounces.{/color}"
    wit_you "\"STOP— stop bouncing— I'm not even DOING anything—\""
    "{color=#ff5fb8}Your thighs rub together with every step. Soft against soft. The polo drags across your puffy nipples and you gasp, out loud, in your new light voice. Your hair falls past your shoulders, dark and glossy and swinging.{/color}"
    "{color=#ff5fb8}And your arse. Your hole, right there between your soft new cheeks. It clenches. On nothing. Slow, and then it relaxes, and then it clenches again, and you know, the way you know your own name, exactly how it would open, exactly how it would grip, like your body read up on it in the night.{/color}"
    wit_you "\"{i}Ahh{/i}— no. NO. That's— that's a no-go area, that is, that's a NO—\""
    hide cg onlayer cgl
    "You go to put the kettle on and swear at it when it's slow, and your swearing comes out so light and so sweet that the supervisor's pen pauses, for one second, over the crossword. Then carries on."
    "The incident report's on the clipboard. The purple column. The newest word at the bottom, fresh, the loops still glossy: the feather word, the touch word."
    "You pick up the biro to fill in {i}Action taken{/i}. You hold it over the box. You hold it there for a long time."
    "You put it down. You leave it blank."
    show screen wit_report(5)
    "There's a doodle in the margin. A little pointed witch's hat, in biro, with a star on the brim. In your handwriting. You don't remember drawing it."
    hide screen wit_report
    wit_super "{b}\"Back in at ten, Kettering.\"{/b}"
    show cg wit_spreader onlayer cgl
    "You sit on the bench all day with your hands in your lap and your thighs pressed together, gasping every time you breathe in, in your tight women's-cut kit, and the upgrade sits by the door waiting for you: a fertiliser spreader, the push-along kind with a hopper, full to the brim with rock salt, with a tag on the handle. {i}LAST ONE. GOOD LUCK.{/i}\n{size=-5}{color=#ff8fa3}▸ Sleep through the day{/color}{/size}"
    $ vn_until(21)
    jump wit_fence_five

label wit_fence_five:
    $ vn_enter(bg="wit_fence", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_spreader_drive")
    show screen wit_status(5)
    "Nine o'clock. The floodlight, the fence, the lavender."
    hide screen wit_status
    $ vn_until(22)
    show cg wit_spreader_drive onlayer cgl
    "The gate opens at ten, and you push the fertiliser spreader up the drive towards the wing like a lawnmower, hips swaying, arse bouncing, salt hissing out of the hopper in a neat white stripe behind you. The wheels squeak. Your thighs rub. Your nipples buzz under the polo. You keep going."
    wit_super "\"Gate's shut till your shift's done.\""
    "Calling it after you, not looking up."
    wit_you "\"Yes. I KNOW.\"\n{size=-5}{color=#ff8fa3}▸ Up to the top floor{/color}{/size}"
    "In your new light voice, through your teeth."
    jump wit_side_ward

## Rung 5: the side ward. Niall in a witch's robe with his old lanyard: "I said yes, Em." Morgause
## behind him: "Every one of us came in with a torch." Isolde snaps her fingers: Obedient. "Put that
## away." Kneel. Bend. Her robe open: futa, and big. His first, and he comes untouched.
label wit_side_ward:
    $ vn_enter(bg="wit_side_ward", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "The top floor is quieter. The corridors are narrower up here, the windows smaller, the moonlight thinner. At the far end of the last corridor there's a side ward, a narrow one, a handful of beds, with its door open and a lamp on inside."
    "Somebody's waiting in the doorway."
    show wit_niall witch at vn_cast_slot
    show cg wit_niall_door onlayer cgl
    "A witch. A pretty one. Long dark-blond hair falling loose past the shoulders, pointed ears poking through it, violet eyes. A plain dark robe. And round the neck, on its blue strap, a Northcott Security lanyard, the old ID card still clipped on the end, swinging."
    "And the grin."
    "You know that grin. You'd know that grin anywhere. You've seen it on the bus driver and the chippy woman and the police."
    wit_you "\"Niall?\""
    "Niall shrugs. Easy. Happy. The same way he's always shrugged."
    wit_niall "{b}\"I said yes, Em.\"{/b}"
    hide cg onlayer cgl  # ff 2:36 am: no picture, morgause-niall failed 4 draws (SCENES.md witches v5)
    "Behind him, in the doorway, the lamp goes dim, and someone's standing there who wasn't before. Tall. The horns. The violet eyes. The old silver watch pinned to her black robe. She puts one hand on Niall's shoulder, light, and looks at you over his head."
    hide wit_niall
    show wit_morgause amused at vn_cast_slot
    wit_morgause "{b}\"Every one of us came in with a torch.\"{/b}"
    hide wit_niall
    hide cg onlayer cgl
    "The lamp flickers. And they're both gone."
    "You stand there with your hands on the spreader's handle and your mouth open."
    show wit_isolde intent at vn_cast_slot
    "Someone steps out of the side ward."
    "Silver-blonde hair in one long plait over her shoulder. Pointed ears. Violet eyes, cool as anything. A high-collared grey robe buttoned all the way up. She looks at you, and at the spreader, and back at you, like you're a form that's been filled in wrong."
    menu:
        "Like a form that's been filled in wrong."
        "Take a run at her with the spreader":
            "You line the spreader up on her. You've practised this. You grip the handles and take a run at it, the hopper rattling, the salt hissing—"
        "Read her the site rules first":
            wit_you "\"Northcott Security. This site is closed to the public—\""
            "You line the spreader up on her while you say it. You've practised this. You grip the handles and take a run at it, the hopper rattling, the salt hissing—"
    "She snaps her fingers."
    call wit_ting("Obedient")
    "{color=#ff5fb8}Your knees go soft.{/color}"
    "{color=#ff5fb8}Not weak. Soft. Like they're waiting to be told what to do. Like your whole body's gone quiet inside and is standing to attention, listening, ears pricked, for the next thing anybody says. You can feel it. A warm, hollow, obliging feeling, all the way through you, settling in your belly and your thighs and the soft hot ring of your arse, which clenches, slow, and opens, like it's listening too.{/color}"
    wit_you "\"{i}Hah{/i}— no— what's— what did you— {i}ahh{/i}—\""
    "The witch in grey glances at the spreader."
    wit_isolde "\"Put that away.\""
    show cg wit_spreader_away onlayer cgl
    "And you do."
    "You turn the spreader round. You wheel it neatly back down the corridor, squeak, squeak, squeak. You open the cleaning cupboard at the end, the one with the mop and bucket. You park the spreader inside, carefully, handles towards the door so it's easy to get out next time. You shut the cupboard door. You turn round."
    "And you're halfway back up the corridor before you realise what you've done."
    wit_you "\"That didn't count.\""
    "You tell her, pointing."
    hide cg onlayer cgl
    wit_isolde "\"Kneel.\""
    show cg wit_kneel onlayer cgl
    "You kneel. Right there on the lino, in your tight trousers, hands on your thighs."
    wit_you "\"No— stop that— stop DOING that, that's— I'm not doing that, my KNEES are doing that—\""
    wit_isolde "\"Bend.\""
    hide wit_isolde
    show cg wit_bend_rail onlayer cgl
    $ wit.fit = "nude"
    "You get up. You walk past her into the side ward. You go to the iron bed by the window and stand at the foot of it, and you bend yourself over the cold iron rail, belly on the bar, and your own two hands go to the waistband of your trousers and push them down, and your boxers with them, all the way down past your soft heart-shaped arse, to your knees."
    wit_you "\"This is a VIOLATION of the site rules. Section— all the sections. ALL of them—\""
    "You tell the mattress. Behind you, buttons. One at a time. Unhurried."
    "You look back over your shoulder. You shouldn't. You do."
    show cg wit_isolde_robe onlayer cgl
    "Isolde has opened her robe. Underneath it she's all long pale legs and high round breasts and a flat stomach, and below that, hanging heavy between her thighs, a cock. A big one. Thick, and long, and already hard, rising as you watch, with a pussy tucked neatly under it."
    wit_you "\"No. No, no, no, no. That's— nobody said anything about— you've got a—\""
    "She slicks it. You hear it. Then her fingers, slick and cool, between your cheeks, pressing on your hole, and it opens for her. It just opens. Like it was told to."
    wit_you "\"{i}Ahh{/i}— don't— don't you DARE— I've never— nobody's EVER—\""
    "The head of her presses there. Fat and hot. And pushes."
    show cg wit_isolde_in onlayer cgl
    "Slow. So slow. Opening you round her a bit at a time, the stretch of it huge and full and hot and impossible, and there's nothing in it anywhere but {i}more{/i}, and more, and more, until her hips meet your arse and she's all the way in. All of her. In you. Your first." with vnfx("shake")
    "And you come."
    "Right then, the second she bottoms out. Your cock jerks against the iron rail with nothing and nobody touching it and spurts, hard, all over the bar, while your mouth hangs open over the bare mattress." with vnfx("flash")
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Hold.\""
    "And your body holds.\n{size=-5}{color=#ff8fa3}▸ Please—{/color}{/size}"
    jump wit_side_ward_sex

## Rung 5's last beat inside the act: "Beg." Please on every order, swearing between every please that
## he doesn't mean it; his cock spurting on the rail untouched; she comes deep. "Good." "Again."
label wit_side_ward_after:
    $ vn_enter(bg="wit_side_ward", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_five_peak")
    vn_sfx "{i}Pap. Pap. Pap. Pap.{/i}"
    show cg wit_five_peak onlayer cgl
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Beg.\""
    wit_you "\"Please— please— I don't mean it— {i}please{/i}—\""
    "It comes out of you every time she says it. Every single time. Your mouth just opens and the pleases fall out, loud, in your light new voice, while you're bent over the iron rail with your trousers round your knees and her cock driving into you, and in between every please you swear, as hard as you can, so she knows."
    wit_you "\"Please— that's NOT ME— please— I don't mean a WORD of it— please—\""
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Again.\""
    wit_you "\"{i}Please{/i}—\""
    "She holds your hips. That's all. She doesn't need to hold anything else. Your body does what it's told: arches when she says arch, holds when she says hold, pushes back onto her when she says nothing at all, because it's worked out what she likes. {i}Pap pap pap pap.{/i} The bed rail rattles. The bed's iron feet skid on the lino."
    "Your cock's bouncing against the rail. Untouched. Nobody's been near it. Nobody's going near it. It's dribbling on the cold iron, and every stroke she gives you pushes another spurt out of it, like she's pumping it from the inside."
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Louder.\""
    wit_you "\"{i}PLEASE{/i}—\""
    "She goes faster. Harder. Her hips smack your soft arse and it wobbles and you yell please at the window and the moon and the whole sleeping town, and then she grips you and pulls you back onto her, all the way, and holds you there."
    show cg wit_five_cum onlayer cgl
    "Isolde comes deep in your arse." with vnfx("flash", "shake")
    "You feel it. Hot and heavy and so much of it, pulse after pulse, flooding you, filling you up from the inside until you can feel the warmth of it spreading in your belly, and your cock goes off against the rail again from the feel of it alone, untouched, spurting, while you beg and beg and beg."
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Good.\""
    "It's the longest thing she's said all night. She doesn't pull out. She stays right where she is, buried in you, hard, and you feel her cock twitch inside you and not go soft at all."
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Again.\"\n{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    hide cg onlayer cgl
    call vn_night(6)
    jump wit_dawn_six

## ---- NIGHT 6, Witchmark (Witches Dawn Six, Fence Six, Matron) ------------------------------

## Dawn: the hair down his back, finished, the peak; he writes Obedient in the column himself before
## he looks; "Yes, ma'am," and a salute. No kit at all.
label wit_dawn_six:
    $ wit.fit = "women"
    $ vn_enter(bg="wit_hut", pc="outraged", pc_tag="wit_pc", cast=[], cg="wit_bench_dawn")
    show cg wit_bench_dawn onlayer cgl
    "The bench. The kettle. The crossword. You wake up on your side with your hair everywhere."
    hide cg onlayer cgl
    $ wit_body(6)
    wit_you "{color=#ff5fb8}\"{i}Ohh{/i}— oh, no— {i}no{/i}—\"{/color}"
    show cg wit_six_hair onlayer cgl
    "{color=#ff5fb8}It's down your back. Your hair. Long and dark and heavy and soft, spilling off the bench onto the floor, all the way down to the small of your back when you sit up, swinging against your arse. You pull a handful of it round in front of your face and stare at it. It's glossy. It smells of lavender.{/color}"
    "{color=#ff5fb8}You stand up and everything comes with you. Your puffy chest, your nipples standing up pink under the polo, buzzing. Your hips, wide and soft. Your arse, round and full and heavy, so full now the women's-cut trousers are a second skin over it, and it sways behind you when you take one step towards the kettle, sways and settles, sways and settles. Your soft thighs pressing together. Not one hair on you anywhere, neck to toe, just smooth soft skin that shivers every time the air moves.{/color}"
    "{color=#ff5fb8}And your cock. Smaller than it was. Still there. Still yours. Hard in your trousers, as always, and so sensitive now that the seam brushing it as you stand up makes you go up on your toes and squeak.{/color}"
    wit_you "\"{i}Hnn{/i}— {i}ahh{/i}— oh, that's— that's NOT fair—\""
    "{color=#ff5fb8}Your arse throbs. Deep inside, where she was. It clenches on nothing, warm and slick and greedy, and you know exactly how you'd open, exactly how you'd push back, exactly how you'd grip a cock and work it, like your arse has a qualification now, and the thought of it makes your knees go and you have to hold the counter.{/color}"
    wit_you "\"No— I don't KNOW that— I don't know how to do any of— {i}ahh{/i}—\""
    show cg wit_six_window onlayer cgl
    "You catch sight of yourself in the dark window, leaning on the counter with your hair down your back and your lips parted and your lashes low, and you catch yourself tilting your head. Just a bit. Looking up through your lashes at your own reflection. Wetting your lip. Like you're about to ask somebody to buy you a drink."
    wit_you "\"STOP that. Stop making EYES at yourself, you absolute—\""
    "Your nipples rub the polo. Your arse throbs. Your cock twitches. All at once, every bit of you lit up and humming, and a moan comes out of you, long and loud and light, in the middle of the guard hut, at six in the morning."
    wit_you "\"{i}Mmmmh{/i}— oh, for {i}God's{/i} sake—\""
    hide cg onlayer cgl
    "The incident report's on the clipboard. You pick up the biro. Before you even look, before you've thought about it at all, your hand writes a word in the column, neat and quick and obliging."
    "{i}Obedient.{/i}"
    show screen wit_report(6)
    "Then you look. The purple's already there, beside it. The whole column of it, looping, glossy. And your biro word next to the newest one, like an answer."
    hide screen wit_report
    "You put the biro down very carefully."
    wit_super "{b}\"Back in at ten, Kettering.\"{/b}"
    show cg wit_salute onlayer cgl
    wit_you "\"Yes, ma'am.\""
    "And you salute."
    "You've never saluted anybody in your life. Your hand's at your eyebrow, crisp and flat, before you know it's moving. You stand there in the guard hut with your hair down your back and your hand up, staring at it."
    "The supervisor fills in a word."
    "There's nothing on the side. No upgrade. No tag. No kit at all.\n{size=-5}{color=#ff8fa3}▸ Sleep through the day{/color}{/size}"
    $ vn_until(21)
    jump wit_fence_six

label wit_fence_six:
    $ vn_enter(bg="wit_fence", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_violet_window")
    show screen wit_status(6)
    "Nine o'clock. The floodlight. The fence. The yellow signs."
    hide screen wit_status
    show cg wit_violet_window onlayer cgl
    "No torch. No radio. No whistle. No salt. You stand at the gate with your empty hands at your sides and your long hair stirring in the breeze, and the lavender comes through the chain-link thick and sweet, and up on the top floor of the wing, for the first time, there's a light on. One window. Violet."
    "You don't know why you're going in. You know exactly why you're going in."
    wit_you "\"Rufus is in there. Nobody—\""
    "You tell the fence. And the rest of it doesn't come. You stand there with your mouth open and the words just aren't there any more."
    "At ten, the gate opens.\n{size=-5}{color=#ff8fa3}▸ Up to the light{/color}{/size}"
    $ vn_until(22)
    jump wit_matron

## Rung 6: the matron's office. The whole coven; Rufus with a tray of tea; the kit on the desk,
## labelled in purple like evidence. "Admitted." The hat and the collar on the hooks; Rowena's book,
## which is the rule. Fists up for form's sake; every ailment at once; her palm over his heart:
## Witchmark. Legs over her shoulders. "Look at me."
label wit_matron:
    $ vn_enter(bg="wit_matron", pc="dogged", pc_tag="wit_pc", cast=[], cg=None)
    "Up through the wing. Past the day room, where the telly's on low and the bells go {i}ting{/i} as you pass. Past the examination room, still white. Past the nurses' station and its stopped clock, past the linen room and the porter's chair, past Ward Four with its long rows of iron beds. Up the last stairs, to the top, to the door at the very end with the brass plate on it: MATRON."
    "It's open. It's warm inside. It's lamplit."
    "The matron's office. A big room under the roof, with a sloping ceiling and a thick rug and a fire going in a little iron grate. A heavy old desk. A row of brass hooks by the door. And taking up the whole far end, a bed. A huge old bed, the kind with four posts and a canopy, heaped with cushions and quilts, the curtains tied back."
    hide cg onlayer cgl  # ff 2:36 am: no picture, coven failed 4 draws (SCENES.md witches v5)
    "And the coven."
    "All of them. Bryony, curled up on a cushion by the fire, waving at you. Rowena, sitting on the desk, swinging her legs, with a notebook. Cressida in a wingback chair, reading. Elspeth, bouncing on her toes. Isolde, by the window, arms folded. And Niall in his robe, leaning in the corner, grinning, his old lanyard round his neck."
    "And by the door, in his blue pyjamas and his collar, holding a tray of tea, Rufus. His bell goes {i}ting{/i}. He smiles at you."
    show cg wit_kit_evidence onlayer cgl
    "On the desk, lined up in a neat row, is every piece of your kit. Your torch. Your second torch. Your radio. Your whistle. The empty grit bag, folded. The water pistol. The extinguisher. A little pile of rock salt. Every single one of them with a brown card label tied on with string, and on every label, in purple, in that looping hand, a word and a drawn star. Like evidence."
    hide cg onlayer cgl
    show wit_morgause amused at vn_cast_slot
    "On the bed, Morgause rises."
    "Her horns nearly brush the canopy. Her black robe falls open as she stands, and the old silver watch on it catches the lamplight. She looks at you with her violet eyes, amused, the way she looked at you from the end of Ward Four on the very first night, and she smiles."
    wit_morgause "{b}\"Admitted.\"{/b}"
    hide wit_morgause
    show cg wit_hooks onlayer cgl
    "On the hooks by the door, two things are hanging side by side."
    "A witch's hat. A proper one, black, pointed, with a wide soft brim, in your size."
    "And a collar. A soft leather collar, black, with a little brass bell on the front. Exactly like Rufus's. With a custard cream balanced on top of it."
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"I put that there.\""
    "Proudly, from the door."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Right! Book's open, ladies! Hat if he says yes, like our Niall! Bell if he never does, like Rufus! Place your bets!\""
    "Rowena hops off the desk, flipping her notebook open, licking her pencil."
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Hat.\""
    "Dreamily."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Bell.\""
    "Without looking up."
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"BOTH.\""
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"You can't have both. I'll put you down for hat.\""
    "Niall gives you a little wave and a thumbs-up. Isolde says nothing at all."
    hide cg onlayer cgl
    "You stand in the middle of the rug in your tight women's-cut kit with your long hair down your back and your empty hands, and you look at the hat, and you look at the bell. Then you look at Morgause."
    show cg wit_fists_up onlayer cgl
    "And you put your fists up."
    "For form's sake. You know it's for form's sake. Everyone in the room knows it's for form's sake. You put them up anyway, chin tucked, feet planted, the way the Northcott course showed you, and you say it, because somebody has to."
    wit_you "\"Northcott Security. You're trespassing.\""
    "Morgause smiles at you like that's the sweetest thing she's ever heard."
    "She flicks her fingers."
    call wit_ting("Charmed")
    call wit_ting("In heat")
    call wit_ting("Shrunk")
    call wit_ting("Sensitive")
    call wit_ting("Obedient")
    show wit_pc flushed
    "Every one of them at once. You feel them land like bells going off inside you, one after another, all through you, every one you've ever had. Your fists drop. Your knees go. Your cock throbs so hard you moan. Your whole body tips towards her, soft, obliging, hot, begging to be touched, and you'd walk to her if she smiled, and she's smiling."
    show cg wit_palm_heart onlayer cgl
    "She crosses the rug to you. She lays her palm flat on your chest, over your heart."
    "It lights up violet under her hand. A warm glow, right through your polo, right through you."
    call wit_ting("Witchmark")
    wit_you "\"Oh. Oh, {i}no{/i}.\""
    "Very quietly."
    $ wit.fit = "nude"
    show cg wit_matron_legs onlayer cgl
    "She walks you backwards to the big bed and lays you down on your back in the quilts and cushions, and undresses you, unhurried, the way you'd unwrap something you'd been looking forward to. The polo. The trousers. The boxers. She opens her robe. She's enormous between her thighs, the biggest cock in the wing, heavy and hard, and she kneels up between your legs and takes your ankles in her hands and lays your legs up over her shoulders."
    "You're open. Bare. On your back on the matron's bed with your legs up and your arse tilted up to her and your smaller cock lying hard and wet on your soft belly, and the whole coven watching."
    "The head of her presses against your hole, slick and hot."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"Look at me.\""
    "You look. You have to. Into her violet eyes."
    "She pushes into your arse. Slow. Deep. All the way."
    "{size=-6}{color=#b7b7b7}The ring closes on a yes: give in at the end and it closes. Fight to the last stroke and it never does.{/color}{/size}\n{size=-5}{color=#ff8fa3}▸ Look at her{/color}{/size}"
    jump wit_matron_sex

## Rung 6's last beat inside the act, and THE FORK: the coven calling the rings; Morgause comes deep;
## the last ring hangs, one stroke from closing; his own last move decides (the owner, 2026-11-12:
## a marked choice at the last stroke, in place of DoL's read of the combat moves).
label wit_matron_after:
    $ vn_enter(bg="wit_matron", pc="breaking", pc_tag="wit_pc", cast=[], cg="wit_six_cum")
    show cg wit_six_peak onlayer cgl
    wit_you "\"No— please— no, please, {i}please{/i}—\""
    "She's been inside you for ever. Slow. Deep. Unhurried. Your legs over her shoulders and her violet eyes on yours and the whole coven round the bed, leaning in, watching the violet come into your eyes ring by ring, calling it out like a race."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Nearly!\""
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Ooh, look, {i}look{/i}—\""
    "And you've been begging. Nobody told you to. Nobody's said beg tonight. It just comes out of you, no and please, no and please, in the same breath, over and over, and you don't know any more which one you mean."
    show cg wit_six_cum onlayer cgl
    "Morgause pushes in to the root and holds there, and her eyes close for the first time all night, and she comes." with vnfx("flash", "shake")
    "Deep. So deep. Hot and heavy and endless, pumping into your arse, and you feel every pulse of it, and your smaller cock jerks on your belly with nobody touching it and spurts, and spurts, all over your soft stomach, while you wail at the canopy."
    "The coven leans in. All of them. Bryony with her hands clasped. Rowena with her pencil in her teeth. Elspeth on tiptoe. Niall grinning. Even Cressida's put her book down."
    show cg wit_last_ring onlayer cgl
    "The violet's in your eyes. Ring after ring after ring of it, all the way in from the rim, nearly to the middle. All but one."
    "{b}The last ring hangs, one stroke from closing.{/b}"
    menu:
        "The last ring hangs, one stroke from closing."
        "\"Close your eyes and let it.\"" (ending=True):
            $ wit.fork = "witch"
            "And it comes out of you. Not because anybody asked. Nobody asked. Nobody's going to."
            wit_you "\"...yes. Yes. {i}Fine.{/i} YES—\""
            "You hear yourself say it. Morgause gives you one more stroke, slow and deep, the last one."
            vn_sfx "{i}Ting.{/i}" with vnfx("flash")
            "The last ring closes.\n{size=-5}{color=#ff8fa3}▸ There we are{/color}{/size}"
            jump wit_end_witch
        "\"Keep saying no.\"" (ending=True):
            $ wit.fork = "pet"
            "She gives you the last stroke, slow and deep, and you're still saying it."
            wit_you "\"No. No. {i}No{/i}.\""
            "You pant it up at her. The last ring stays open. A thin rim of grey, all the way round, under the violet. It doesn't close. It never closes.\n{size=-5}{color=#ff8fa3}▸ The bell, then{/color}{/size}"
            jump wit_end_pet

## ---- THE ENDINGS ---------------------------------------------------------------------------

## End Witch: violet eyes, his ears drawn to soft points; the hat ("There we are."); Rowena pays out;
## Rufus eats the custard cream; the robe. He/him to the last line.
label wit_end_witch:
    $ vn_enter(bg="wit_matron", pc="flushed", pc_tag="wit_pc", cast=[], cg="wit_end_ears")
    show cg wit_end_ears onlayer cgl
    "The violet closes over the last of the grey, and the whole room goes soft and bright and lovely at the edges, like a lamp's been turned up behind your eyes."
    "Your ears are warm. You reach up, slowly, and touch one. It goes up to a point. A soft, pretty point, poking out through your long dark hair, just like theirs."
    wit_you "\"Oh.\""
    show cg wit_hat_on onlayer cgl
    "Morgause slides out of you and gets up off the bed, unhurried, and crosses to the hooks by the door. She takes the witch's hat down. She comes back, and sits on the edge of the bed, and sets it on your head, and tips the brim up with one finger so she can see your eyes."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"There we are.\""
    "Behind her, the room erupts. Bryony squeals and claps. Elspeth jumps up and down. Niall whoops. Cressida turns a page and says \"Mm,\" which from her is a standing ovation. Isolde nods, once."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"HAT. Hat! Pay up, the lot of you! Cressida, that's a fiver, don't you look at me like that—\""
    "Flipping her notebook."
    "By the door, Rufus takes the custard cream off the collar on its hook, and looks at it, and eats it. His bell goes {i}ting{/i}."
    show wit_rufus steady at vn_cast_slot
    wit_rufus "\"Well done, Em.\""
    "With his mouth full, and means it."
    $ wit.fit = "witch"
    show cg wit_robe onlayer cgl
    "Somebody brings you a robe. Black and soft and floor-length, with purple at the cuffs. You put it on over your bare soft body, and it fits, and the hat fits, and you stand there in the middle of the matron's office, slight and pretty and long-haired, your cock still there under the robe, your violet eyes wide, your pointed ears pink, while the coven crowds round to look at you."
    wit_you "\"Northcott Security.\""
    "Faintly, out of habit."
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Not any more, lovely.\""
    "And she kisses your cheek."
    $ wit.ending = "witch"
    $ achievement.grant("Hat in His Size")
    hide cg onlayer cgl
    "{size=-5}{color=#ff8fa3}▸ A week on{/color}{/size}"
    call vn_night(9)
    $ vn_pass(6 * 1440 + 13 * 60)
    jump wit_epilogue_witch

## End Witch's epilogue, a week on at ten: a new Northcott team splits up; he blows the first one a
## kiss; ting; Morgause: "Another torch." (the bookend). Then Stay or Go.
label wit_epilogue_witch:
    $ wit.fit = "witch"
    $ vn_enter(bg="wit_ward_four", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_epi_ward")
    "A week on. Ten at night."
    "Down at the fence, the gate creaks. Torch beams come wobbling across the yard, and up the back steps, and in through the door, a whole new team of them, like drunks. New hi-vis jackets with NORTHCOTT on the back. Radios. Whistles. Bags of rock salt from the council gritting store with the tops rolled down."
    "Somebody new" "\"We'll cover more ground if we split up.\""
    "You hear it from Ward Four, through the open double doors, and you smile."
    show cg wit_epi_ward onlayer cgl
    "You're waiting on an iron bed halfway down the ward, cross-legged on the bare mattress, in the moonlight. Your black robe. Your hat, tipped back. Your long dark hair down your back and your soft thighs crossed and your cock and all, a slight pretty witch with violet eyes, swinging one foot."
    "One of them comes in on his own. Big and nervous, his torch going everywhere. It finds you."
    "The new man" "\"N-Northcott Security. You're— you're trespassing.\""
    wit_you "\"Oh, {i}bless{/i} him.\""
    show cg wit_epi_kiss onlayer cgl
    "And you kiss your fingertip, and blow it to him across your palm."
    vn_sfx "{i}Ting.{/i}" with vnfx("flash")
    "His torch slips out of his fingers and rolls away under the next bed, and his feet take a step towards you, and his mouth says \"no,\" and his feet take another."
    "At the far end of the ward, under the last window, someone tall with horns is standing quite still, watching, with an old silver watch pinned to her robe."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "{b}\"Another torch.\"{/b}"
    menu:
        "\"Another torch.\""
        "The coven's newest" (ending=True):
            jump wit_witch_stay
        "Days in town, nights in the wing" (ending=True):
            jump wit_witch_go

label wit_witch_stay:
    $ wit.epilogue = "stay"
    $ vn_enter(bg="wit_ward_four", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_epi_stay")
    show cg wit_epi_stay onlayer cgl
    "You stay."
    "You get an iron bed of your own in Ward Four, under the tall windows, with your hat on the rail at the foot of it. You get a hook in the matron's office. You get a quill from Elspeth, and Bryony shows you how to blow a kiss, which you didn't need, and a place by the fire, and a cup of tea from Rufus every night at nine, bell going {i}ting{/i}."
    "Rowena puts you in her book. You win her a lot of money."
    "Every night at ten the torches come wobbling across the yard. Every night you're waiting for them on a bed in the moonlight. You never once think about the hut, or the bench, or the clipboard, except to smile."
    "The supervisor's still in the hut, doing the crossword. She still doesn't look up. Some nights, when you're passing the fence in your robe and your hat, you'd swear she's filling in your name.\n{size=-5}{color=#ff8fa3}▸ Out through the gate{/color}{/size}"
    jump wit_route_return

label wit_witch_go:
    $ wit.epilogue = "go"
    $ vn_enter(bg="wit_fence", pc="dogged", pc_tag="wit_pc", cast=[], cg="wit_epi_go")
    show cg wit_epi_go onlayer cgl
    "You keep a place in town."
    "You walk out through the gate in the morning in a long coat over the robe, with your hat in a carrier bag, and your violet eyes behind a pair of sunglasses, and your long dark hair down your back. The supervisor doesn't look up. The gate's not shut any more. It opens when you push it."
    "In the daytime you're in town. You buy milk. You sit in the park. People look at you, the slight pretty man with the long hair and the odd pointed ears, and you smile at them, and their feet take a step towards you before they know they're doing it, and you laugh and let them go."
    "At night, at ten, you go back round the back of the hospital, past the bins, along the fence, and the gate swings open for you on its own, and the lavender comes out to meet you, and up on the top floor the violet light is on.\n{size=-5}{color=#ff8fa3}▸ Out through the gate{/color}{/size}"
    jump wit_route_return

## End Pet: the violet stops one ring short and settles back to grey with a thin violet rim; his ears
## stay his own; the collar, buckled on; Rufus gets his custard cream back; the pyjamas. One close.
label wit_end_pet:
    $ vn_enter(bg="wit_matron", pc="flushed", pc_tag="wit_pc", cast=[], cg="wit_end_grey")
    show cg wit_end_grey onlayer cgl
    "The violet stops. It just stops, one ring short, and slowly, slowly, it settles back. Your eyes go grey again. Your own grey. With a thin violet rim round the edge of each, like a ring left on a table by a cup."
    "Your ears stay your own."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"Oh.\""
    "Softly. Not cross. Not anything. Amused, the way she always is. She slides out of you and gets up, unhurried, and crosses to the hooks by the door."
    "She doesn't take the hat."
    show cg wit_collar_on onlayer cgl
    "She takes the collar. She brushes the custard cream off it and hands it to Rufus, who takes it back, delighted, and dunks it in his tea. Then she comes back and sits on the edge of the bed, and lifts your long hair off your neck, and buckles the soft leather collar on you."
    vn_sfx "{i}Ting.{/i}"
    "The little brass bell rests in the hollow of your throat. You swallow. It goes {i}ting{/i}."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"There.\""
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"BELL. Bell, bell, bell! Cressida, you absolute card—\""
    "Flipping her notebook."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Mm.\""
    "And she holds out her hand for her winnings."
    $ wit.fit = "pet"
    show cg wit_pyjamas onlayer cgl
    "Somebody brings you pyjamas. Soft blue ones, brushed cotton, like Rufus's. You put them on. They're the softest things you've ever worn. Your bell goes {i}ting{/i} when you do the buttons up."
    wit_you "\"Northcott Security.\""
    "Faintly, out of habit."
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Course you are, pet.\""
    "And she kisses your cheek."
    $ wit.ending = "pet"
    $ achievement.grant("A Custard Cream on the Collar")
    hide cg onlayer cgl
    "{size=-5}{color=#ff8fa3}▸ Lights out{/color}{/size}"
    call vn_night(20)
    jump wit_epilogue_pet

## End Pet's epilogue: the day room beside Rufus, the telly, the custard creams; every night one of the
## coven crooks a finger. You're never a witch. One close, no Go.
label wit_epilogue_pet:
    $ wit.fit = "pet"
    $ wit.epilogue = "pet"
    $ vn_enter(bg="wit_day_room", pc="dogged", pc_tag="wit_pc", cast=[("wit_rufus", "content")], cg="wit_epi_dayroom")
    show cg wit_epi_dayroom onlayer cgl
    "The day room. The armchairs in their half circle. The standard lamp. The old telly on its trolley with a quiz on, low."
    "You're curled up in the armchair next to Rufus's, in your soft blue pyjamas and your collar, with your feet tucked under you and your long dark hair over one shoulder, and a plate of custard creams on the arm between you. He takes one. You take one. Your bells go {i}ting{/i}, together."
    "On the telly, somebody wins a caravan. The whole room makes a soft, pleased noise. You make it too."
    "It's nice. It's warm. It's so nice."
    "Every night, one of the coven comes to the door of the day room and crooks a finger at you. Bryony, or Rowena, or Elspeth with her feather. Cressida, who never says anything. Isolde, who says one word. And most of all Morgause, who never says anything at all, only smiles, and you get up out of your armchair with your bell ringing and go to her, every time, saying no, please, no, all the way up the stairs."
    "You're never a witch. You're the coven's pet, in the day room, by the telly, with Rufus."
    hide cg onlayer cgl
    wit_rufus "\"Alright, Em?\""
    "Passing you the plate."
    "You take a custard cream. Your bell goes {i}ting{/i}.\n{size=-5}{color=#ff8fa3}▸ Out through the gate{/color}{/size}"
    jump wit_route_return
