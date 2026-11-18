## THE STORY: days 1-3 (PLAN.md). Drinks with Seiya, the lantern festival, Pirika's mistake and the first henshin; the
## office, the patrol and Rasetsu; Seiya at the flat. The change shows each night in the bathroom mirror (gdk_grow before
## the night's vn_enter). Changes are pink ({color=#ff5fb8}). Akari speaks as gdk_akari; Kaoru as gdk_you.

define gdk_akari = VNChar("Akari", who="pc", plate="#7fd6c0")

## ---- 1. Monday: the festival --------------------------------------------------------------------------------------------

label gdk_izakaya:
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_izakaya", pc="smug", pc_tag="gdk_pc", cast=[("gdk_seiya", "grin")], cg="gdk_second_round")
    "Eight o'clock on a Monday, and Seiya's already ordered the second round before you've finished the first."
    "You're Kaoru Shiraishi, twenty-two, a junior clerk at a paper-goods wholesaler in Asakusa, and every Monday since you were nineteen you've drunk with Seiya Kurogane in this exact izakaya, at this exact corner of the counter, under the same yellowed menu."
    "You met on the night shift at a warehouse in Koto: two idiots in hi-vis vests racing pallet jacks at three in the morning."
    "He's got black hair that never stays where he puts it, a grin like he knows something about you, and a job he's never once explained."
    gdk_seiya "\"You know the lantern festival's on tonight? Up the hill. Whole street's lit up. Very romantic.\""
    gdk_you "\"Then go and be romantic at somebody.\""
    gdk_seiya "\"I'm trying.\" He clinks his glass on yours. \"Honestly, Kaoru. Lashes like yours, you're wasted on men's suits. If you were a woman I'd have married you years ago.\""
    "It's the oldest joke he's got. He's been telling it since the warehouse. It still makes your ears go hot, which is annoying."
    menu:
        "He's grinning at you over the glass."
        "Tell him to shut up":
            gdk_you "\"Shut up and drink.\""
            gdk_seiya "\"Yes, darling.\""
            $ gdk.fought += 1
        "Play along":
            gdk_you "\"You couldn't afford me.\""
            gdk_seiya "\"Oh, I could,\" he says, very quietly, and then laughs, and the moment goes."
            $ gdk.gave += 1
    "He pays, as usual. He walks you to the corner, as usual, and then he stops under the streetlight and looks back at the hill, where the festival glows orange over the roofs."
    gdk_seiya "\"Go home the long way. Through the lanterns. Trust me.\""
    gdk_you "\"Why?\""
    gdk_seiya "\"Because it's pretty.\" He's already walking off with his hands in his pockets. \"Night, Kaoru. Be careful out there.\""
    $ vn_set_time(22, 40)
    $ vn_enter(bg="gdk_festival", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_pirika", "worried")], cg="gdk_firefly")
    "So you go the long way, slightly drunk, through the lantern festival."
    "The street up the hill is hung with paper lanterns from end to end, red and white and persimmon orange, strung on wires between the shops. The stalls are shutting."
    "The crowd has mostly gone home. Your shadow goes long and short and long again under every lantern."
    "Then the lanterns start going out. One after another, up the street towards you, as if something were walking under them."
    "Something is. It comes down the middle of the street like a spill of ink: black, soft, no face, and far too many arms. Each one ends in a long, soft, grabbing hand."
    "Something small and bright smacks into your chest."
    gdk_pirika "\"Ow! Sorry! Sorry, sorry— you! You can see it? You can see it! Oh, thank goodness. Hold this!\""
    "It's a woman about the size of your palm, with gauzy wings and a round, lit-up tail like a firefly's. She's dragging a paper lantern on a black pole about as long as your arm."
    "Its flame is the only light left on the street."
    gdk_pirika "\"I'm Pirika, I'm a firefly, I was meant to find the festival's magical girl and I've been looking all night and she isn't anywhere and that thing's coming and you're the only one awake— please hold the lantern!\""
    menu:
        "The arms are reaching for the last lantern on the street."
        "Ask what it is first":
            gdk_you "\"What does it {i}do?{/i}\""
            gdk_pirika "\"No time! Hold it and say 'Light the way'!\""
            $ gdk.fought += 1
        "Grab the lantern":
            "You grab the pole without thinking. It's warm."
            $ gdk.gave += 1
    gdk_you "\"Light... the way?\""
    show cg gdk_henshin onlayer cgl
    vn_sfx "Fwoosh."
    "The flame jumps up the pole and into your hand and everywhere at once."
    "{color=#ff5fb8}It runs through you like a hot bath. Your shirt and jeans go up in soft orange light and come down as silk.{/color}"
    "{color=#ff5fb8}Your chest swells, high and round and heavy, and you feel each breast settle and sway. Your waist draws in. Your hips spread.{/color}"
    "{color=#ff5fb8}Between your legs your cock just isn't there any more: there's soft, wet heat instead, and it {i}aches.{/i}{/color}"
    "{color=#ff5fb8}Your hair pours down past your shoulders, pale mint, and ties itself up in a high side ponytail with a cord and a red tassel. You're shorter. Your voice, when you gasp, is high and bright.{/color}"
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_festival", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_pirika", "bright")], cg="gdk_akari_first")
    "You're standing in the middle of the street in a short kimono dress, indigo with cream sleeves that swing to your knees and a huge persimmon bow at your back."
    "The skirt is split to the hip. You've got cream thigh-highs and lacquered sandals with heels, and a brass lantern-clasp on your obi where your belt buckle was."
    gdk_pirika "\"Oh. Oh, that's {i}lovely.{/i} Hello, Akari! That's your name now. It means the light.\""
    gdk_akari "\"I'm a {i}WOMAN!?{/i}\""
    gdk_pirika "\"In costume! Only in costume! Look out!\""
    $ vn_enter(bg="gdk_festival", pc="flustered", pc_tag="gdk_pc", cast=[], cg="gdk_yokai_arms")
    "The arms get you before you've learned how to swing a lantern."
    "One round each ankle, one round your waist, two more round your wrists. They're cool and soft and they don't hurt at all."
    "They lift you right off the ground and hold you spread in the middle of the street, your sleeves hanging, your sandals kicking."
    "More hands come. They slide inside your sleeves and over your breasts, kneading, and your nipples go hard against the silk."
    vn_sfx "Muni. Muni."
    "One slips up under your split skirt, and finds nothing there to stop it."
    gdk_akari "\"Hey— HEY— that's— ahh♡— where are you—\""
    menu:
        "The soft fingers are spreading you open."
        "Fight the arms":
            "You twist and kick and swing the lantern, and the arms just hold you tighter and keep going, patient as anything."
            $ gdk.fought += 1
        "Stop fighting":
            "It's too good. You stop kicking, and your thighs fall open on their own."
            $ gdk.gave += 1
    "A thicker arm pushes up into you, slow and slick and cool. It feels completely new and somehow it's {i}right{/i}, the way a key's right in a lock."
    vn_sfx "Nuchu. Nuchu."
    gdk_akari "\"Ohh♡— it's— inside me— I've got an {i}inside—{/i} ahh♡— ahh♡—\""
    "It fucks you right there under the dead lanterns. It's deep and steady while the fingers roll your nipples and pinch your clit, and you're louder than you've ever been in your life."
    "Your new voice rings off the shutters."
    gdk_akari "\"I'm— something's coming— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come so hard the lantern in your fist blazes up white. The arms flinch from it as if it's burned them, and the whole yokai unravels into smoke and is gone."
    "You drop to the street in a heap of silk and wobbly legs. Pirika lands on your knee."
    $ vn_enter(bg="gdk_festival", pc="flustered", pc_tag="gdk_pc", cast=[("gdk_pirika", "bright")])
    gdk_pirika "\"You won! Um. In a way. Your first fight!\""
    gdk_akari "\"Pirika. What. Was. That.\""
    gdk_pirika "\"The Kurayami Society. They're yokai. They come up at night and put the lanterns out, and they— well, you saw what they do. And when they make a magical girl come, she glows.\""
    gdk_pirika "\"That's the light. It burns them.\""
    gdk_akari "\"So I win by...\""
    gdk_pirika "\"Yes.\""
    $ vn_set_time(23, 50)
    $ gdk_grow(1)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bathroom", pc="shocked", pc_tag="gdk_pc", cast=[("gdk_pirika", "worried")], cg="gdk_mirror_one")
    "At home the costume lets go of you the second you shut the door. Silk turns back to shirt and jeans. Your cock's back, and your flat chest, and your height."
    "Most of you, anyway."
    "{color=#ff5fb8}In the bathroom mirror your legs are smooth from ankle to thigh. So are your arms, and your chest, and everywhere else. Every hair is gone, and your skin is soft as the silk was. Your lashes are long and dark. Your hair's grown over your ears overnight.{/color}"
    gdk_pirika "\"Oh. Hm. It leaves a bit behind, sometimes. Coming out of it.\""
    gdk_you "\"{i}Sometimes?{/i}\""
    gdk_pirika "\"It's not a very well-documented lantern.\""
    call gdk_cut(8, 1, "Tuesday.")
    jump gdk_office

## ---- 2. Tuesday: the office and Rasetsu ---------------------------------------------------------------------------------

label gdk_office:
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_office", pc="flustered", pc_tag="gdk_pc", cast=[("gdk_kurose", "smile")], cg="gdk_desk")
    "The office is a long room of grey desks and stacked sample boxes above a stationery shop. By ten o'clock two of the women in accounts have asked about your skincare."
    "By eleven Kurose's on the edge of your desk. He's thirty-four, from sales, in a shirt a size too small, with the kind of aftershave you can taste."
    gdk_kurose "\"Shiraishi-kun. Something's different. Did you get your eyebrows done? Your skin's like a—\" He reaches out, and you lean back. \"Like a peach. What's the secret?\""
    menu:
        "His hand's still hanging in the air near your cheek."
        "Brush him off":
            gdk_you "\"Sleep. Lots of sleep. Can I help you with something?\""
            $ gdk.fought += 1
        "Thank him":
            gdk_you "\"Oh. Um. Thanks.\""
            gdk_kurose "\"Anytime,\" he says, and looks at your mouth a moment too long."
            $ gdk.gave += 1
    "You spend the afternoon pretending to proofread a catalogue of envelopes, and not touching your own smooth wrist under the desk."
    $ vn_set_time(21, 30)
    $ gdk.fit = "lantern"
    $ vn_enter(bg="gdk_rooftops", pc="stern", pc_tag="gdk_pc", cast=[("gdk_pirika", "bright"), ("gdk_rasetsu", "grin")], cg="gdk_patrol")
    "Pirika says a magical girl patrols."
    "So at half past nine you say \"Light the way\" in your bathroom, and come out on the roofs of Asakusa in silk and heels with a paper lantern on a pole."
    "{color=#ff5fb8}The change goes through you faster the second time. Breasts, hips, the wet heat between your thighs. The mint hair pours down and ties itself up. You can't stop touching the ponytail.{/color}"
    "Two grunts in fox masks and black happi coats are snuffing out the lanterns on the shrine path. You knock them both off a roof with one swing. It's {i}fun.{/i} You're laughing."
    "Then the roof shakes, and the third one isn't a grunt."
    "She's two metres and then some: red-skinned, two curved horns, black hair in a thick braid, muscles like a statue's."
    "She carries an iron club on one shoulder and wears a tiger-skin wrap that's hardly doing anything. Under the wrap, swinging heavily as she walks, is a cock as thick as your wrist."
    gdk_rasetsu "\"You're the new light? Ha! The lord said you'd be a pretty one. I'm Rasetsu, general of the Kurayami. Shall we?\""
    show cg gdk_rasetsu_club onlayer cgl
    vn_sfx "Bonk."
    "She doesn't even use the club. She flicks the lantern out of your hand with two fingers and tips you over onto the roof tiles on your back, and sits down astride your thighs."
    menu:
        "You're flat on the tiles under an oni's weight."
        "Get back up":
            "You buck and shove at her stomach. It's like shoving a wall. She laughs, delighted."
            gdk_rasetsu "\"Oh, good, a fighter.\""
            $ gdk.fought += 1
        "Stay down":
            "You lie there with your chest heaving and look up at her. She grins."
            gdk_rasetsu "\"Oh, good, a sensible one.\""
            $ gdk.gave += 1
    "She flips your skirt up with one finger. She looks at what's under it, and her cock stiffens all the way up against your belly, hot and heavy and huge."
    gdk_akari "\"That won't— there's no way that— ohh♡— OHH♡—!\""
    vn_sfx "Zunn. Pan. Pan. Pan."
    "It does. Inch after hot inch, she spreads you around her until your eyes cross."
    "Then she fucks you into the roof tiles, slow at first and then hard, and every thrust knocks a high shout out of you that carries across half of Asakusa."
    gdk_rasetsu "\"Listen to you! You'll wake the whole ward!\""
    gdk_akari "\"Don't— stop— don't STOP— ahh♡— ahh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come with your heels drumming on the tiles and the lantern blazes, but it's lying out of reach in the gutter and the light goes straight up into the sky."
    "Rasetsu groans, buries herself to the hilt, and fills you full."
    vn_sfx "Dopyu. Dopu, dopu."
    gdk_rasetsu "\"Good. Very good. The lord's going to enjoy you.\""
    "She pats your cheek, picks up her club, and walks off along the ridge of the roof, whistling."
    $ vn_set_time(23, 40)
    $ gdk_grow(2)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_bathroom", pc="dazed", pc_tag="gdk_pc", cast=[("gdk_pirika", "worried")], cg="gdk_mirror_two")
    "You come out of costume on your own bathroom floor, still sore and slick, and drag yourself up to the mirror."
    "{color=#ff5fb8}Your lips are fuller. Soft and pouting, as if you've been kissing all night. Your waist's narrower, so your jeans hang loose at the hips. Your hair's down to your jaw now, soft and brown. When you push it back it falls forward again into your face, like a woman's.{/color}"
    gdk_pirika "\"It's... it's leaving more of her each time, isn't it.\""
    gdk_you "\"Do something.\""
    gdk_pirika "\"I'm a {i}firefly.\"{/i}"
    call gdk_cut(19, 1, "Wednesday.")
    jump gdk_seiya_flat

## ---- 3. Wednesday: Seiya at the flat ------------------------------------------------------------------------------------

label gdk_seiya_flat:
    $ vn_set_time(19, 30)
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_flat", pc="flustered", pc_tag="gdk_pc", cast=[("gdk_seiya", "grin")], cg="gdk_doorway_seiya")
    "Seiya turns up on Wednesday with a bag of beer and the second season of something on a stick, which he's done once a fortnight for three years."
    "He opens his mouth to say hello and doesn't."
    gdk_seiya "\"...Kaoru?\""
    gdk_you "\"Don't.\""
    gdk_seiya "\"I'm not saying anything.\" He comes in and puts the beer down and looks at you. At the hair on your jaw, at your mouth, at the way your jeans hang off your hips now."
    gdk_seiya "\"I'm absolutely not saying anything.\""
    "You get as far as the second episode. He's not watching it. He's watching you, sideways, every time you shift on the sofa."
    menu:
        "He's staring at your mouth again."
        "Tell him to stop staring":
            gdk_you "\"Stop {i}looking{/i} at me like that.\""
            gdk_seiya "\"Like what?\""
            gdk_you "\"Like I'm the takeaway.\""
            $ gdk.fought += 1
        "Let him look":
            "You let him look. You even tuck your hair behind your ear, slowly, and watch him swallow."
            vn_sfx "Gokuri."
            $ gdk.gave += 1
    gdk_seiya "\"I told you,\" he says. \"I told you for three years. Lashes like that.\""
    "He puts a hand on your knee, warm through the denim, and slides it up your thigh. Your smooth new thigh. You don't move it away."
    menu:
        "His face is very close."
        "Push him away":
            "You get a hand on his chest and push. He leans into it until your elbow folds, and kisses you anyway, and after a second you're kissing him back."
            $ gdk.fought += 1
        "Kiss him back":
            "He kisses you, and you kiss him back, at once and hungrily, as if you'd been waiting for him to do it since you were nineteen."
            $ gdk.gave += 1
    show cg gdk_sofa_seiya onlayer cgl
    "It isn't like the yokai, or Rasetsu. It's {i}Seiya:{/i} his mouth, his hands, the beer on his breath."
    "He tugs your jeans down to your knees, and laughs softly in your ear when your cock jumps up between you."
    gdk_seiya "\"Still got that. Good. I like that.\""
    "He turns you over the arm of the sofa. He kisses down your spine and spreads your arse with both hands, and licks you open until you're squirming and gasping into the cushion."
    "Then he slicks himself with something from his pocket, as if he'd come prepared."
    gdk_you "\"Seiya— we're— we're {i}friends—\"{/i}"
    gdk_seiya "\"We are,\" he agrees, and pushes in."
    vn_sfx "Zupu. Pan. Pan."
    gdk_you "\"Ahh♡— oh god— it's so— Seiya♡— SEIYA♡—\""
    "He fucks you over the arm of your own sofa with the TV still playing. He's slow and deep, and he knows exactly where to aim."
    "Every stroke rubs something inside you that makes your cock drip on the cushions."
    gdk_seiya "\"Look at you. Look at this arse. You were made for this. You know that, right?\""
    gdk_you "\"I'm— I'm gonna— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come untouched, all over the sofa, clenching on him, and he groans your name and comes deep inside you."
    "Afterwards he lies on top of you, heavy and warm, and plays with your hair."
    gdk_seiya "\"Be careful out there, Kaoru,\" he says, into the back of your neck. \"I mean it. Things are going to get strange.\""
    "You're too boneless to ask him what he means. Later you'll wish you had."
    call gdk_cut(18, 1, "Thursday.")
    jump gdk_taken
