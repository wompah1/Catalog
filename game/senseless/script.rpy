## THE STORY: chapters 0-2 (PLAN.md) and the two shared pieces: the morning rune (sns_rune) and the part of the evening hour
## that follows it (sns_hour_part). sns.brat counts Rook's mouth, sns.soft the times he lets it go; the five part counters count
## the runes; sns.today is this morning's. None of it changes the body art (one fixed ladder; owner).

## ---- the morning rune ---------------------------------------------------------------------------------------

label sns_rune(q):
    menu:
        "[q]"
        "The chest rune":
            $ sns.today = "chest"
            $ sns.chest += 1
        "The nipple rune":
            $ sns.today = "nips"
            $ sns.nips += 1
        "The hip rune":
            $ sns.today = "hips"
            $ sns.hips += 1
        "The cock rune":
            $ sns.today = "cock"
            $ sns.cock += 1
        "The mouth rune":
            $ sns.today = "mouth"
            $ sns.mouth += 1
    vn_sfx "Tink."
    "You press it with your thumb. The rune lights violet under the dust, and somewhere under the floor, under you, something shifts and settles. You can't feel what."
    "You can't feel anything down there. That's the whole problem."
    return

## ---- the part of the hour the rune decided -----------------------------------------------------------------------

label sns_hour_part:
    if sns.today == "chest":
        if sns.chest == 1:
            "{color=#ff5fb8}Your chest. That's where they've been all day.{/color}"
            "{color=#ff5fb8}You feel it now all at once: a dozen soft tentacles wound round your ribs and over your pecs, kneading, squeezing, pulling, and under them your chest isn't flat. It's soft.{/color}"
            "{color=#ff5fb8}It's swelling into their coils, and every squeeze lands like a hand on a bruise that feels good.{/color}"
            sns_you "\"Wh— my chest— what are you doing to my chest— ahh♡—\""
            "They don't answer. They squeeze, slow and rhythmic, milking at nothing, and each squeeze goes straight down your spine and out through your cock."
        else:
            "{color=#ff5fb8}The chest again. You know the feeling now and it's worse, better, heavier: your breasts sit in the tentacles' coils like fruit in a net, full and soft and swaying, and every squeeze makes them heavier still.{/color}"
            sns_you "\"Not— not again— they're so heavy— squeeze them— ahh, squeeze them harder♡—\""
            "You hear yourself say it. You don't take it back."
    elif sns.today == "nips":
        if sns.nips == 1:
            "{color=#ff5fb8}Your nipples. Two tentacles end in soft, wet mouths, and they've been fastened on your nipples since dawn, sucking. You feel a whole day of it in one jolt.{/color}"
            "{color=#ff5fb8}Your nipples are swollen, puffy, twice the size they were, and so sensitive that the suck alone makes your hips buck.{/color}"
            sns_you "\"My— my nipples— why are they— hhah♡— stop sucking— don't stop sucking—\""
            "They tug, and let go, and fasten again, and you come from your nipples alone. You didn't know you could do that."
        else:
            "{color=#ff5fb8}Nipples again. They're fat and tender now and the mouths know exactly how hard to pull. Every tug is a shock straight to your cock and your arse at once.{/color}"
            sns_you "\"Suck them— suck them— AHH♡— I'm coming from my tits again, I'm— I'm—♡\""
    elif sns.today == "hips":
        if sns.hips == 1:
            "{color=#ff5fb8}Your hips. Your arse. Thick tentacles have been kneading your backside all day, spreading it, squeezing it, and it's softer, rounder, wider than it was; you feel your hips flare out against the coils that hold them.{/color}"
            "And one has been inside you the whole time. Slow. Patient. Opening you an inch an hour. You feel every inch of it land in one second."
            sns_you "\"It's— there's something in my— AHH♡— it's been in there all day— oh gods, oh gods♡—\""
        else:
            "{color=#ff5fb8}Hips again. Your arse is round and heavy in the coils, wide, soft, jiggling when they spank it, and they spank it. The one inside is thicker than yesterday's and you're open for it.{/color}"
            sns_you "\"Fill it— fill my arse— it's so big now, my arse is so big, fuck it♡—\""
    elif sns.today == "cock":
        if sns.cock == 1:
            "{color=#ff5fb8}Your cock. A sleeve of a tentacle has had it all day, wet and ridged inside, sucking and stroking, and your cock feels... less. Smaller in its grip. And ten times as sensitive, so tender the first stroke is nearly too much.{/color}"
            sns_you "\"My cock— it's— it's smaller— why is it— AHH♡— don't stroke it, it's too much, it's too much♡—\""
            "It strokes. You come in about four seconds, and it keeps stroking."
        else:
            "{color=#ff5fb8}Your cock again, smaller again, a soft sensitive thing the tentacle swallows whole. It milks it like it's trying to wring you out, and you let it.{/color}"
            sns_you "\"It's so small— it's so sensitive— milk it— milk me out♡—\""
    else:
        if sns.mouth == 1:
            "{color=#ff5fb8}Your mouth. That one you've felt all day, because it's above the collar. Your lips have been tingling since noon, fuller, softer, and your tongue feels everything: the air, your teeth, your own breath.{/color}"
            "Now a tentacle slides up through the gap at the collar's rim, slick and violet, and nudges your lips, and you open them before you've decided to."
            sns_you "\"Mmh— mmmh♡—\""
            "It fills your mouth and slides back along your tongue, and your tongue is so sensitive that it's like being fucked somewhere new. You come with it in your throat."
        else:
            "{color=#ff5fb8}Your mouth again. Your lips are plump and wet and they open for it on their own. Your throat takes it like it was built for it.{/color}"
            sns_you "\"Mmmh♡— mmh— mmmmh♡—\""
    return

## ---- 0. Saturday: Quist's Folly -----------------------------------------------------------------------------------

label sns_folly:
    $ sns.fit = "delver"
    $ vn_enter(bg="sns_ruin_gate", pc="smug", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_gate_race")
    "Quist's Folly sits in a fold of the hills two hours out of Brackwater: a squat tower of green-black stone, half swallowed by ivy, with a door nobody has opened in eighty years."
    "The Hall's had it on the board since spring. Nobody's had the nerve."
    "You've got the nerve."
    "You've also got Hesper Vane's survey of the place, more or less, because you copied it off her table at the Delvers' Hall last week while she was at the bar."
    "You're three pins into the lock when she comes up the path at a run: tall, freckled, red in the face, copper braid half undone, long leather coat flapping round her boots."
    sns_hesper "\"Ashdown. You absolute— that's my survey. I spent a month on that survey.\""
    sns_you "\"And it was a lovely survey, Vane. Very neat. Afternoon, by the way. You're so slow I lose track of the hours.\""
    sns_hesper "\"Quist wasn't a treasure-hoarder, you idiot. He was an alchemist. He made things that 'improve' people.\""
    sns_hesper "\"Half the notes the Hall has on him are about what happened to the people.\""
    sns_you "\"So you read his notes and I'll read his treasure.\""
    "The fourth pin. The fifth. The lock goes {i}clunk{/i}, and the door swings in on a stair that smells of dust and something sweet underneath it, like overripe plums."
    menu:
        "Two years of beating her to every find in the hills, and here she is again, a step behind."
        "Blow her a kiss":
            "You blow her a kiss over your shoulder and take the stair two at a time."
            sns_hesper "\"One day, Rook. One day something's going to bite you, and I am going to {i}laugh{/i}.\""
            $ sns.brat += 1
        "Hold the door for her":
            "You hold the door for her, with a bow. She narrows her eyes at it like it might be a trap, which is fair, considering."
            sns_hesper "\"After you. You've never once gone second in your life and I'm not falling for it now.\""
            "Fine. You go first."
            $ sns.soft += 1
    $ vn_set_time(15, 30)
    $ vn_enter(bg="sns_cradle_room", pc="smug", pc_tag="sns_pc", cast=[], cg="sns_cradle_room_first")
    "The stair comes out in a round room at the top of the tower. Dust. Old lamps. A ring of pale stone set in the middle of the floor, a yard across, with five worn runes round its rim."
    "And on a plinth on the far side of it, in a shaft of light from a slit window, a glass flask full of something that glows violet."
    "That's the one. You can feel it. That's the thing the Hall's been too scared to fetch for eighty years, and it's {i}yours{/i}."
    "You step over the ring."
    "You step {i}onto{/i} the ring."
    vn_sfx "Klunk."
    $ vn_enter(bg="sns_cradle_room", pc="shocked", pc_tag="sns_pc", cast=[], cg="sns_the_fall")
    "The stone goes out from under you like a trapdoor. You drop, straight down, and the ring closes round you as you fall."
    "It catches you under the arms and stops you dead, and it tightens, smooth and snug, round the top of your chest."
    "Your head and shoulders and arms are in the room. The rest of you is somewhere under the floor."
    "And then the rest of you goes away."
    "Not numb. Not cold. Gone. You can't feel your legs, your belly, your hips, your cock, your feet, anything below the stone. You can't tell if you're standing or hanging."
    "It's like the whole bottom of the world got cut off."
    sns_you "\"Okay. Okay. Stuck-trap. Classic. Seen a hundred of them. Give me a minute.\""
    "You give it ten. You push, you twist, you swear. The stone doesn't move, and you can't even tell whether your legs are kicking."
    "It doesn't hurt, though. That's something. It doesn't feel like anything at all."
    $ vn_set_time(16, 15)
    $ vn_enter(bg="sns_cradle_room", pc="angry", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_hesper_finds")
    "Footsteps on the stair, and Hesper's face appearing at the top of it, and then her whole face changing as she takes it in: Rook Ashdown, the Hall's darling, stuck in the floor up to his chest like a cork in a bottle."
    "She laughs so hard she has to sit down on the top step."
    sns_you "\"Yes. Thank you. Very good. Get me out.\""
    sns_hesper "\"Oh, I'm going to. Give me a— hah— give me a second, I'm saving this. I'm going to be telling this one at the Hall till I'm ninety.\""
    "Then she wipes her eyes and kneels at the rim and looks at the runes properly, and she goes quiet."
    sns_hesper "\"It's Quist's cipher. 'The Cradle.' It holds... whatever falls in. Until the work is done.\""
    sns_you "\"What work?\""
    sns_hesper "\"It doesn't say.\""
    "She's reading something else, though. You can see her eyes going along the line and back. You can't read Quist's cipher. Nobody at the Hall can, except her."
    "She's never let you forget that either."
    sns_hesper "\"There'll be a way in from below. Foundations, drains, something. Stay there.\""
    sns_you "\"Very funny.\""
    "She takes her lamp and goes down the stair. You hear her boots go round the tower, and a door, and then nothing for a long time."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_cradle_room", pc="shocked", pc_tag="sns_pc", cast=[], cg="sns_first_hour")
    "At nine o'clock the stone round your chest chimes, one soft note, like a finger on a wineglass."
    "And everything comes back."
    "All at once, every sense below the collar, like a door kicked open. You're naked down there: your trousers are gone, your boots are gone, your shirt's gone below the ribs."
    "You're hanging in warm, wet, plum-sweet air. And there are things holding you."
    "Smooth. Warm. Slick. As thick as your wrist and thicker."
    "Coiled round your thighs and your ankles and your waist, holding you up, holding you open, moving all the time, slow, the way seaweed moves in a current."
    sns_you "\"Wh— what— there's something— there's {i}lots{/i} of something—\""
    "One of them slides up the inside of your thigh, unhurried, and wraps round your cock, and squeezes."
    vn_sfx "Nuru."
    sns_you "\"Hey— HEY— don't you— don't you {i}dare{/i}— ahh— ahh, what the— what the {i}fuck{/i}—♡\""
    "It strokes."
    "Up and down, slick, ridged, with a grip that tightens on the upstroke, and you've been hard for who knows how long without knowing it, and you're so close so fast it's embarrassing."
    sns_you "\"No no no no— I'm not— I am {i}not{/i} coming for a— for a— AHH♡— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru."
    "You come into the dark, gasping, shaking in the collar, and the tentacle milks you through it and keeps stroking after, gentle, almost thoughtful, like it's taking notes."
    "At ten the stone chimes again, and everything goes away."
    $ vn_set_time(22, 10)
    $ vn_enter(bg="sns_cradle_room", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_hesper_lamp")
    "Hesper comes up the stair with her lamp, quick, out of breath."
    sns_hesper "\"Rook? I heard you from the courtyard. You were... loud. What was that?\""
    menu:
        "Your face is burning. She's looking right at it."
        "Tell her it was nothing":
            sns_you "\"Cramp.\""
            sns_hesper "\"A cramp.\""
            sns_you "\"In my leg. Which I can't feel. It's complicated. Go to sleep, Vane.\""
            "She looks at your face a long while. She doesn't laugh. Somehow that's worse."
            $ sns.brat += 1
        "Tell her the truth":
            sns_you "\"There's something down there. Lots of somethings. They've got me. They— one of them—\""
            "You can't say it. She doesn't make you. She goes very still, and very thoughtful, and something moves behind her eyes that you don't have a name for."
            sns_hesper "\"I'll find the way in first thing. I promise.\""
            $ sns.soft += 1
    "She lays her coat round your shoulders, the only part of you that can feel the cold, and she sleeps against the wall by the stair with her boots on. You don't sleep much."
    call sns_cut(8, 1, "Sunday. The first morning in the Cradle.")
    jump sns_sunday

## ---- 1. Sunday: the runes -------------------------------------------------------------------------------------------

label sns_sunday:
    $ sns.fit = "nude"
    $ sns_grow(1)
    $ vn_enter(bg="sns_cradle_room", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_notebook")
    "Hesper's been up since dawn. She's got a book in her lap, a fat one in a cracked green binding, open on her knees."
    sns_hesper "\"Quist's daybook. It was on the landing of the lower stair. Listen. 'Five keys to the Cradle, for the five works. One each morning, and the seal grows thinner.\""
    sns_hesper "\"On the seventh morning it opens of itself.'\""
    sns_you "\"So it opens. Good. Seven days. I can do seven days standing on my head.\""
    sns_hesper "\"You're not standing on anything, as far as I can tell. But yes. One rune a morning. Pressing them 'thins the seal'.\""
    "She shows you the page. It's just shapes to you. You nod like it isn't."
    "She holds up her hand mirror, so you can see yourself, and frowns at it, and so do you."
    "{color=#ff5fb8}Your stubble's gone. Not shaved: gone, like it was never there. Your jaw looks softer, your lashes darker. You look like your own prettier twin.{/color}"
    sns_you "\"...It's the air in here. It's a sweet air. It does things to your skin.\""
    sns_hesper "\"Mm. Of course.\""
    call sns_rune("Five runes round the rim, under your hands. Hesper holds out the daybook. \"Your trap, Ashdown. You're the expert. Pick.\"")
    $ vn_set_time(13, 0)
    $ vn_enter(bg="sns_cradle_room", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_feeding")
    "She goes down for the afternoon, \"looking at the foundations\", and comes back up at one with bread and cheese and a waterskin."
    "Your arms are free, technically."
    "But you're wedged so tight your elbows can't bend far enough to reach your own mouth, and your hands are shaking from the strain of holding yourself up all morning."
    "You've been holding yourself up with your arms because you can't feel whether anything else is."
    menu:
        "She's holding out the bread. You'd have to lean to it like a horse."
        "Make her feed you":
            sns_you "\"Well? I'm not going to bite you. Probably.\""
            "She snorts, and tears off a piece, and holds it to your lips, and you eat out of her hand and you make her do every single bite, and you make a great show of not minding."
            sns_hesper "\"You're impossible.\""
            sns_you "\"I'm {i}stuck{/i}. There's a difference.\""
            $ sns.brat += 1
        "Say thank you":
            sns_you "\"...Thanks. Really. You didn't have to stay.\""
            "She looks at you like you've grown a second head. Then she feeds you, bite by bite, and her fingers brush your lips, and neither of you says anything about it."
            $ sns.soft += 1
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_cradle_room", pc="moaning", pc_tag="sns_pc", cast=[], cg="sns_hour_sunday")
    "Nine o'clock. The chime. You've been dreading it all day and you've been waiting for it all day, and you don't want to think about which one wins."
    "Everything comes back."
    call sns_hour_part
    "{color=#ff5fb8}And there's more than the rune. There's all of you: no hair anywhere, skin smooth as a polished stone; your waist a hair narrower in the coils; a soft puffiness to your chest, your nipples swollen and tender. They've been at all of you, all day, gently.{/color}"
    show cg sns_first_anal onlayer cgl
    "And something is inside your arse. Not starting. Inside."
    "It's been in there all day, a slender, slick tentacle sliding in and out so slowly you'd never have known, and now you feel all of it, all twelve hours, at once."
    vn_sfx "Zuru. Zuru. Nuchu."
    sns_you "\"It's— it's in— it's {i}in my arse{/i}— get it OUT— AHH— no— no, don't, don't get it out, don't stop, oh gods♡—\""
    "It finds a place inside you that makes your whole body jolt, and it presses there, slick and patient, and then it fattens, slow, until you're stretched round it, and starts to fuck."
    vn_sfx "Juppu. Juppu. Juppu."
    sns_you "\"Ahh♡— ahh♡— it's fucking me— a fucking tentacle is fucking me and I— and I— AHHHH♡—!\"" with vnfx("flash", "shake")
    "You come so hard you see violet. It doesn't stop. It's got another fifty minutes."
    call sns_cut(8, 1, "Monday. The second morning.")
    jump sns_monday

## ---- 2. Monday: let her hear --------------------------------------------------------------------------------------

label sns_monday:
    $ sns.fit = "nude"
    $ sns_grow(2)
    $ vn_enter(bg="sns_cradle_room", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_second_morning")
    "Hesper's mirror again, first thing, because you asked for it, because you need to know."
    "{color=#ff5fb8}Your face is rounder in the cheek, your lips fuller, your hair half an inch longer than yesterday, curling over your ears. Down there, you know from last night, your chest is soft and small and round, like the start of breasts, and your waist is narrower.{/color}"
    sns_you "\"It's doing something to me. Hesper. It's {i}changing{/i} me.\""
    sns_hesper "\"Quist's daybook says it's harmless. 'The works are gentle.' It says that a lot, actually.\""
    sns_you "\"Gentle. Right.\""
    "She doesn't look at you while she says it. She's looking at the runes, and the corner of her mouth keeps doing something."
    call sns_rune("\"Thinner every morning,\" she says. \"Which one today?\"")
    $ vn_set_time(14, 0)
    $ vn_enter(bg="sns_cradle_room", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_afternoon_talk")
    "The afternoon is long. You talk because there's nothing else to do. About the Hall. About old finds."
    "About the barrow at Tolley's Cross, two years ago, when you came out the front with the silver and she came out the back with nothing, and you laughed at her in front of everyone, and she threw a pint at you."
    sns_hesper "\"You deserved that pint.\""
    sns_you "\"I deserved that pint.\""
    "She smells sweet today. Plum-sweet, like the air under the floor. You think about asking where she spends her afternoons \"looking at foundations\", and you don't."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_cradle_room", pc="moaning", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_hour_monday")
    "Tonight she doesn't go down. She sits against the wall across from you with her knees up, and her lamp, and her eyes on your face. At nine the stone chimes."
    menu:
        "Everything's about to come back, and she's going to watch."
        "Bite it back":
            "You bite your lip hard. You are not going to give Hesper Vane the satisfaction. You are a delver of the Hall. You are going to keep your mouth shut."
            $ sns.brat += 1
        "Let her hear":
            "You can't stop it, so you don't try. You look at her and let her see it coming."
            $ sns.soft += 1
    call sns_hour_part
    show cg sns_milked onlayer cgl
    "{color=#ff5fb8}Your chest is soft. Small, round, real: two handfuls the tentacles cup and squeeze. And your cock, wrapped in its sleeve, is smaller than it was on Saturday. You can feel the difference in the grip. Smaller, and tender as a nerve.{/color}"
    "Two of them in your arse now, twisting round each other. One on your cock, milking. Mouths on your nipples. All of it at once, a whole day's worth, and your mouth is open."
    vn_sfx "Nuchu. Juppu. Chuu."
    if sns.brat > sns.soft:
        "You hold it for nearly a minute. It's the best minute of your life as a delver. Then the one in your arse presses {i}there{/i}."
    sns_you "\"Hh— hhh— AHH♡— Hesper— Hesper, don't look— don't— they're inside me, they're milking me, I can't— I can't hold it— ahh♡ ahh♡—\""
    sns_hesper "\"I'm looking.\""
    sns_you "\"AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Byuru."
    "She watches the whole hour. She doesn't laugh once."
    "When it's over and you're slack in the collar, breathing hard, she gets up and puts her coat round your shoulders, and her hands aren't steady."
    sns_hesper "\"Goodnight, Rook.\""
    "Her voice isn't steady either."
    call sns_cut(8, 1, "Tuesday. The third morning.")
    jump sns_tuesday
