## harem's acts. Pass B: ch 1 forced (Zarina never threatens, never calls the guard, just doesn't stop), ch 4 forced (the
## sultan doesn't hear no); ch 2-3 the package's gleeful rogue; the flip at ch 5's bath; ch 5-6 consensual. The choice when
## he protests is what he says or does, never whether. Every act ends mid-act. The cock is never used after ch 2; there is
## never a pussy; the jade is a toy in a hand. Loud farce; nobody wipes anything up. Production rewrite 2026-11-13: each act
## the longest block in its chapter, a picture per beat.

## ---- ch 1: the hot pool (forced) ----------------------------------------------------------------
label hrm_pool:
    $ hrm.fit = "shift"
    $ vn_enter(bg="hrm_bathhouse", pc="startled", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_oil_pool")
    "They put you in a thin white bath shift, which goes see-through the moment it touches the steam, and sit you on the edge of the hot pool with your legs in the water."
    "Leyla oils one of your arms for about as long as it takes to giggle twice. Nasrin oils your other arm for about as long as it takes to yawn once."
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Ugh, she's all {i}hairy.{/i} Like a goat! It'll take all night!\""
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"I need my own jar for that. Mine's in my room.\""
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Mine too! Back in a bit, Zarina!\""
    "And off they wander together, arm in arm, and the door swings shut behind them. Zarina doesn't move. Zarina kneels behind you on the wet tiles, and uncorks her jar, and smiles."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Just us, then, flower.\""
    show cg hrm_oil_hands onlayer cgl
    "She pours it into her palm, rose-pink and shining, and works it into your shoulders. Then your arms. Then, through the wet shift, your chest."
    "It goes on warm. It sinks in {i}hot.{/i} Like a swallow of strong spirits, but everywhere at once, spreading out under her hands and down, and down."
    vn_th "Oh no. Oh, no, no, not now. Think about the guard. Think about the dungeon. Think about {i}Captain Brask.{/i}"
    "It doesn't help. Under the water you're hard in seconds, as hard as you've ever been, throbbing with it. You press your thighs together under the water and sit very, very still."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Relax, Dahlia. You're stiff as a board.\""
    hrm_you "\"Ha. Ha. Yes. Long journey.\""
    show cg hrm_found onlayer cgl
    "Her oily hand slides down your chest, down your belly, down under the water, as casual as you like, to oil your thighs. And between them. And finds your cock."
    "She stops. Her fingers close round it under the water, slowly, measuring it from root to tip. She doesn't scream."
    "She grins."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"The only cock in the palace.\""
    hrm_you "\"No— no, listen, I can explain— I'm not— I just need to hide for a night, nobody can know I'm here, if anybody finds me they'll—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"The Sultan hasn't sent for me in a year, flower. A {i}year.{/i} And the oil's had me hot since dawn. It has all of us hot, all day, every day.\""
    "She doesn't say she'll tell anyone. She doesn't say she won't. She doesn't say anything else at all. She stands up in the pool, unties her wrap, lets it float off on the water, and climbs into your lap."
    hrm_you "\"Zarina— no, wait, I said {i}no{/i}— I can't— I can't be found, you don't understand—\""
    menu:
        "Zarina, naked, oiled, in your lap, the tip of you already pressed up against her."
        "Try to lift her off":
            $ hrm.shout1 = "lift"
            "You get your hands on her hips to lift her off. She's slippery with oil, and you're slippery with oil, and your hands just slide."
            "She sinks down onto you anyway, all the way, slowly, with your hands still on her hips like you're helping."
        "Beg her to keep quiet at least":
            $ hrm.shout1 = "quiet"
            hrm_you "\"At least keep— {i}hah{/i}— keep your voice down— somebody'll come— please, if you're going to—\""
            "She laughs out loud, a big wicked laugh that rings off every tile, and sinks down onto you, all the way."
    show cg hrm_ride_open onlayer cgl
    vn_sfx "{i}Shlorp.{/i}"
    hrm_you "\"{i}Hahh{/i}— no— Zarina, no— get off, I said no— {i}nnh{/i}—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"{i}Ohh.{/i} Oh, there it is. Oh, I'd forgotten. Oh, I'd {i}forgotten{/i} what one feels like.\""
    "She's hot inside. Hotter than the pool. Slick with the same oil, squeezing round you, and she just sits there on you for a second with her eyes closed and her mouth open, like someone tasting the first fig of summer."
    "Then she starts to ride you. Slow. Lazy. Up and down in the water, her oiled hands flat on your chest."
    vn_sfx "{i}Splosh. Splosh. Splosh.{/i}"
    menu:
        "Your mouth's open. You could shout."
        "Shout for help":
            $ hrm.help1 = "call"
            hrm_you "\"HEL—\""
            "And you stop. Because help, in this palace, tonight, is a guard. And a guard is Captain Brask. And Captain Brask is a dungeon with no window."
            hrm_you "\"...—lo. Hello. Hello there. {i}Nnh.{/i}\""
            hide hrm_leyla
            hide hrm_nasrin
            show hrm_zarina wicked at vn_cast_slot
            hrm_zarina "\"Hello yourself, flower.\""
        "Bite your lip and hold still":
            $ hrm.help1 = "bite"
            "You bite your lip and hold still, rigid, staring at the ceiling, and refuse to give her anything. Not a sound. Not a twitch."
            "She rolls her hips once, slow and deep, and a sound comes out of you anyway, high and long, round your bitten lip."
            hide hrm_leyla
            hide hrm_nasrin
            show hrm_zarina wicked at vn_cast_slot
            hrm_zarina "\"There. That's a nice noise. Give me another.\""
    show cg hrm_ride_smooth onlayer cgl
    $ hrm_body(1)
    "{color=#f0a0c0}And as she rides you, she works the oil in. Over your chest, your arms, your belly, your thighs, both hands, long hot strokes. And where her hands go, your body hair goes. All of it. It just lets go of you, the whole hairy chest, the forearms, the legs, swirling away on the water in dark wisps, and leaves your skin smooth and shining and pink where it was.{/color}"
    hrm_you "\"What— what's {i}happening{/i}— where's my— {i}hahh{/i}—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Rose oil, flower. You'll be soft as a peach by morning.\""
    "You watch it go, and you laugh, high and helpless and stupid, because it's the most ridiculous thing that's ever happened to you. And that's when your hips start meeting hers."
    hrm_you "\"That's not— {i}ahh{/i}— that's not funny— stop it— don't— {i}don't{/i}— oh, gods, don't {i}stop{/i}, I mean— {i}fuck—{/i}\""
    show cg hrm_ride_hard onlayer cgl
    "She rides you harder. The water slaps the tiles. Your hands, which were on her hips to push her off, are on her hips to pull her down."
    vn_sfx "{i}SPLOSH. SPLOSH. SPLOSH.{/i}"
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Look at you. {i}Look{/i} at you. Fucking up into me. Who said no?\""
    hrm_you "\"{i}Ahh{/i}— I did— I did, I meant it— {i}ahh{/i}— don't you {i}dare{/i} stop— don't you dare, Zarina—\""
    $ hrm.broke = True
    show cg hrm_ride_beg onlayer cgl
    hrm_you "\"Please— {i}please{/i}, right there— oh fuck, right there, harder— ride me harder, please, please, {i}please—{/i}\""
    "She does. Up and down and round, water going everywhere, her braid flying, her palms flat on your new smooth chest, and the oil burning hot in you, inside you, everywhere, like a fire somebody's poured down your throat."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Come on, then. The only cock in the palace. Show me what it does.\""
    show cg hrm_ride_cum onlayer cgl
    hrm_you "\"I'm— Zarina— I'm going to— {i}AHH{/i}— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    vn_sfx "{i}Splurt. Splurt.{/i}"
    "You come in her, hard, harder than you ever have on any shore, pumping up into her with your head thrown back against the tiles and your mouth wide open."
    "And you stay hard. Rock hard, still in her, throbbing like you never came at all. Because of the oil."
    show cg hrm_ride_again onlayer cgl
    "She doesn't even slow down."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Again.\""
    hrm_you "\"{i}Again?{/i} I can't— {i}hahh{/i}— how am I still— {i}ohh{/i}—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Rose oil, flower. You'll be hard like this all day. Every day. Isn't that {i}wonderful?{/i}\""
    "She rides you through it, slow and grinding now, and you hold on to her hips and moan up at the ceiling and buck up into her, because there's nothing else in the world you could possibly do."
    show cg hrm_ride_doorway onlayer cgl
    "Then the door. Leyla and Nasrin, back with their jars, walking in arm in arm. They stop dead in the doorway."
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"{i}Zarina!{/i} Is that— is the new girl— does the new girl have a—\""
    "They look. They look for a long time. Then, without a word to each other, they put the jars down and start untying their shifts."
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"My turn.\""
    hrm_you "\"Ladies— {i}hahh{/i}— ladies, one at a— Zarina, slow down— {i}AHH{/i}— I'm coming again— {i}AHHH{/i}—!\"" with vnfx("shake")
    jump hrm_ch1_after

## ---- ch 2: Zarina's bed, all three ---------------------------------------------------------------
label hrm_three:
    $ hrm.fit = "veils"
    $ vn_enter(bg="hrm_chamber", pc="grin", pc_tag="hrm_pc", cast=[("hrm_nasrin", "lazy")], cg="hrm_titjob_2")
    "Zarina's chamber, after the lamps go out. Cushions, a low bed, a carved screen across the door, and three women who have found the only cock in the palace."
    "You're still in the veils. They asked you to keep the coin belt on. They wanted to hear it."
    hrm_nasrin "\"My turn.\""
    "Nasrin first. She doesn't hurry. She pushes you back on the cushions with one hand, kneels between your legs, oils her breasts from the jar, slow, both of them, and leans down and wraps them round your cock."
    hrm_you "\"Oh— {i}oh{/i}— oh, {i}fuck{/i}, Nasrin—\""
    "They swallow it. All of it. Soft and heavy and slick and warm on both sides, and she squeezes them together with her hands and moves them, up, and down, lazy as the tide."
    vn_sfx "{i}Shlick. Shlick. Shlick.{/i}"
    hrm_nasrin "\"Mm. Good?\""
    hrm_you "\"Good? {i}Good?{/i} That's— that's the best thing that's ever happened to me in my {i}life{/i}— don't stop— oh, don't you stop—\""
    vn_sfx "{i}Shhing. Shhing. Shhing.{/i}"
    "The coin belt jingles every time your hips come up into her breasts, which is every time. Leyla, cross-legged on the cushions, laughs so hard she falls over."
    show cg hrm_face_sit onlayer cgl
    "Zarina laughs too, and stands, and steps over you, and sits on your face."
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Keep your mouth busy, flower. You've got a lot of thank-yous to say.\""
    hrm_you "\"{i}Mmph{/i}— {i}mmh{/i}— {i}mmmh{/i}—!\""
    "She's wet and hot and smells of roses, and you lick her like a man who's been at sea a year, and she grinds down on your mouth and grabs the carved headboard and swears, wickedly, in three languages."
    show cg hrm_nasrin_first onlayer cgl
    "Then Nasrin lets go of your cock with her breasts and climbs on instead, and sinks down on it, and rides you. Slow. Lazy. Thorough."
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Mm. Yes. {i}Yes.{/i} That's what I wanted.\""
    vn_sfx "{i}Pap. Pap. Pap. Shhing. Shhing.{/i}"
    show cg hrm_leyla_ride onlayer cgl
    "When she's done, shaking, she rolls off onto the cushions, and Leyla scrambles on, giggling, and gets you inside her on the second try, and rides you like a camel at a gallop, bouncing, squealing."
    hide hrm_nasrin
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Oh! Oh! Oh, it's {i}big!{/i} It's so big! Zarina, it's so {i}big!{/i}\""
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Don't flatter her, Leyla, she'll get ideas.\""
    menu:
        "Three of them. One of you. Somebody has to keep order."
        "\"Ladies, one at a time, there's plenty!\"":
            $ hrm.plenty2 = "plenty"
            hrm_you "\"{i}Mmh{/i}— ladies— ladies, one at a time, there's plenty— {i}mmh{/i}— there's {i}plenty—{/i}\""
            hide hrm_leyla
            hide hrm_zarina
            show hrm_nasrin lazy at vn_cast_slot
            hrm_nasrin "\"There'd better be.\""
        "\"Form a queue, ladies!\"":
            $ hrm.plenty2 = "queue"
            hrm_you "\"{i}Mmh{/i}— form a queue, ladies— an orderly queue— {i}mmh{/i}— everybody gets a turn—\""
            hide hrm_nasrin
            show hrm_zarina wicked at vn_cast_slot
            hrm_zarina "\"Is that how they do it at sea?\""
    "One at a time on your cock, your mouth on whichever one's on your face, the coins jingling every time your hips come up. Round and round. You lose count. You lose track of whose thigh is whose."
    $ hrm_body(2)
    "{color=#f0a0c0}They keep the jar going round, and oil you as they ride you, and under all those slick hands your hips round out a touch, soft at the sides where they were all bone, and the coin belt slides down and sits lower on them, snug.{/color}"
    hide hrm_leyla
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Hips. Look. She's getting {i}hips.{/i}\""
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Good. Something to hold on to.\""
    show cg hrm_leyla_cum onlayer cgl
    "Leyla's riding you when it happens. She's bouncing, and squeezing, and squealing your name, the wrong name, {i}Dahlia, Dahlia,{/i} and you can't hold it any more."
    hrm_you "\"{i}AHH{/i}— Leyla— I'm— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    vn_sfx "{i}Splurt. Splurt. Splurt.{/i}"
    "You come in Leyla, deep, hips jerking up, the coins going {i}shhing-shhing-shhing{/i} like a shop bell in an earthquake."
    show cg hrm_cum_kiss onlayer cgl
    "And Zarina goes straight down. She tips Leyla back on the cushions, puts her mouth between her thighs and sucks it all out of her, every drop."
    "Then she turns and kisses it into Nasrin's mouth. And Nasrin leans over you, lazy, and kisses it into yours."
    hrm_you "\"{i}Mmh{/i}— {i}mmh!{/i}— that's— {i}mmh{/i}—\""
    hide hrm_leyla
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Swallow. Good girl.\""
    "Nobody wipes anything up. Ever. You're starting to understand that's a rule in here."
    show cg hrm_zarina_ride onlayer cgl
    "And you're still hard, of course. The oil. Zarina climbs back on, slick and wicked, and takes you all the way in one long slide."
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Mine again.\""
    hrm_you "\"{i}Ahh{/i}— yours— all yours— {i}ahh{/i}— Zarina, you're so— {i}fuck{/i}—\""
    "She rides you hard and fast and mean, and you come again, in her this time, yelling, and she doesn't slow down for that either."
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Does it ever stop?\""
    hrm_you "\"I hope not— {i}ahh{/i}— I really hope not—\""
    show cg hrm_nasrin_ride onlayer cgl
    "Then Nasrin climbs back on, your own cum still on your lips from her kiss, and your mouth back on Zarina, and the coin belt jingling under them both."
    menu:
        "Leyla, in the corner, demanding to know when she's next."
        "\"Same again tomorrow night!\"":
            $ hrm.promise2 = "tomorrow"
            hrm_you "\"{i}Mmh{/i}— same again tomorrow night, Leyla— I promise— {i}mmh{/i}—\""
        "\"Every night!\"":
            $ hrm.promise2 = "every"
            hrm_you "\"{i}Mmh{/i}— every night, Leyla— every single night— {i}mmh{/i}—\""
    hide hrm_nasrin
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"I'm holding you to that!\""
    hrm_you "\"{i}Mmh{/i}— {i}AHH{/i}— Nasrin— I'm coming again— who's next— who's {i}next{/i}, ladies—!\"" with vnfx("shake")
    jump hrm_ch2_after

## ---- ch 3: the jade --------------------------------------------------------------------------------
label hrm_jade:
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_chamber", pc="flushed", pc_tag="hrm_pc", cast=[("hrm_zarina", "wicked")], cg="hrm_jade_show")
    "Zarina's chamber, that night. The three of them on the bed already when you come in from the bath, in nothing, sitting in a row like judges."
    "Zarina has something in her hand. A smooth jade toy, cool and green and polished like glass, a long rounded shape with a flared base. She turns it in the lamplight."
    hrm_zarina "\"The women decided. We're going to turn it round. You've had it all your own way, Dahlia.\""
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"All your own way! Every night!\""
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"Lie down.\""
    menu:
        "Zarina holds the jade up, waiting."
        "\"Yes. Do it. Please.\"":
            $ hrm.jade3 = "ask"
            hrm_you "\"Yes. Yes. Do it. {i}Please.{/i}\""
            hide hrm_leyla
            hide hrm_nasrin
            show hrm_zarina wicked at vn_cast_slot
            hrm_zarina "\"Listen to her. She's {i}asking.{/i} I love it here.\""
        "\"Bet you can't make me come with that.\"":
            $ hrm.jade3 = "dare"
            hrm_you "\"Bet you can't make me come with that, Zarina. Not without touching it.\""
            hide hrm_leyla
            hide hrm_nasrin
            show hrm_zarina wicked at vn_cast_slot
            hrm_zarina "\"Oh, flower. You're going to lose that bet so many times.\""
    show cg hrm_fingers onlayer cgl
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"On your back. Legs up. Hold them.\""
    "You lie back and pull your knees up, and Leyla and Nasrin take a thigh each and hold them open, wide, and Zarina kneels between them with the jar."
    "She oils your ass with the rose oil. It's cool for one heartbeat, and then it burns hot, inside, like it did on your skin but {i}deeper{/i}, and your whole body jerks."
    hrm_you "\"{i}Hahh{/i}— oh— oh, that's {i}hot{/i}— that's—\""
    "Then one finger. Slow. She opens you with it, round and round, patient. Then two. Slower. Curling."
    hrm_you "\"Oh— {i}oh{/i}— Zarina— what are you— {i}ahh{/i}— what's {i}that{/i}—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"That's the spot, flower. Every girl in this palace knows where it is on a man except the men.\""
    show cg hrm_jade_open onlayer cgl
    "Then the jade, held in her hand. Smooth and cool and slick, pressing, and then sliding in, slow, bit by bit, your first anything there."
    vn_sfx "{i}Shlup.{/i}"
    hrm_you "\"Oh— {i}oh{/i}— Zarina— that's— {i}fuck{/i}, that's deep— that's so {i}deep{/i}— don't stop— don't stop—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Look at her face. {i}Look{/i} at her face.\""
    show cg hrm_nipples onlayer cgl
    "Leyla and Nasrin bend down, still holding your thighs open, and each takes one of your new soft nipples in her mouth and sucks."
    hrm_you "\"{i}Ahh!{/i} {i}AHH!{/i} Both— oh, both at once— {i}ahh{/i}—\""
    "Your cock bounces against your belly, small and stiff and leaking a string of clear onto your skin. Nobody touches it. You reach for it."
    hide hrm_zarina
    show hrm_leyla giggle at vn_cast_slot
    hrm_leyla "\"Hands off! Hands {i}off{/i}, Dahlia!\""
    "She slaps your hand away. Nasrin pins your wrist to the cushion without even lifting her mouth from your nipple."
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"{i}Mm-mm.{/i}\""
    hrm_you "\"Please— {i}please{/i}, just once, just touch it—\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"No. You'll come from this or not at all.\""
    show cg hrm_jade_deep onlayer cgl
    $ hrm_body(3)
    "{color=#f0a0c0}Zarina works the jade into you slow, and then hard, pumping it, all the way in and nearly all the way out, the oil burning hotter with every stroke. And as it goes into you, your hips widen in their hands. You feel it: the bones easing, the flesh rounding, Leyla's and Nasrin's grips sliding outward on your thighs as they fill.{/color}"
    vn_sfx "{i}Shlup. Shlup. Shlup. Shlup.{/i}"
    hrm_you "\"{i}Ahh{/i}— {i}ahh{/i}— Zarina, something's— something's coming— nobody's even {i}touching{/i} it— how is it— {i}ahh—{/i}\""
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Come for me. Come on the jade, Dahlia. {i}Now.{/i}\""
    hrm_you "\"{i}AHH{/i}— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    vn_sfx "{i}Splurt. Splurt. Splurt.{/i}"
    "You come from your ass, untouched, your small cock jerking and spurting all over your own belly and your new chest, rope after rope, your whole body clenching round the jade."
    "And the three of them think it's the funniest and hottest thing they've ever seen. Leyla screams with laughter. Nasrin actually sits up."
    hide hrm_zarina
    show hrm_nasrin lazy at vn_cast_slot
    hrm_nasrin "\"{i}Again.{/i} Make her do that again.\""
    show cg hrm_feed onlayer cgl
    "Zarina scoops it up off your belly on two fingers, slow, and holds them over your mouth."
    hide hrm_leyla
    hide hrm_nasrin
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Open your mouth. Swallow.\""
    "You do. Warm and salty and sweet with rose oil, off her fingers, and you suck them clean, and grin up at her."
    hrm_you "\"{i}Mmh.{/i} More.\""
    show cg hrm_feed_again onlayer cgl
    "So they make you do it again. Zarina's jade, Leyla and Nasrin on your nipples, and you come untouched a second time inside of a few minutes, yelling, and Leyla scoops this one and feeds it to you and you lick her palm clean."
    if hrm.jade3 == "dare":
        hide hrm_leyla
        hide hrm_nasrin
        show hrm_zarina wicked at vn_cast_slot
        hrm_zarina "\"That's twice. What was the bet again, flower?\""
        hrm_you "\"I lose— {i}hahh{/i}— I lose, I lose, do it again—\""
    else:
        hide hrm_leyla
        hide hrm_nasrin
        show hrm_zarina wicked at vn_cast_slot
        hrm_zarina "\"That's twice. Still asking, flower?\""
        hrm_you "\"Still asking— {i}hahh{/i}— always asking— do it again—\""
    show cg hrm_jade_again onlayer cgl
    "The jade pumping deep in your ass in Zarina's hand. Leyla and Nasrin holding your thighs open. Your small cock bouncing untouched on your belly. Your own cum on your tongue."
    hrm_you "\"Again— {i}ahh{/i}— Zarina, don't you dare stop— don't you {i}dare{/i}— I'm coming again— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    jump hrm_ch3_after

## ---- ch 4: the summons (forced) -------------------------------------------------------------------
label hrm_summons:
    $ hrm.fit = "sheer"
    $ vn_enter(bg="hrm_bedchamber", pc="startled", pc_tag="hrm_pc", cast=[("hrm_kasim", "lazy")], cg="hrm_summons")
    "The Sultan's bedchamber: a great bed under a silk canopy, heaped silk cushions, lamps on chains, a smell of sandalwood. And Sultan Kasim, handsome and lazy and black-bearded, lying back with his robe open and a cup in his hand."
    if hrm.danceat == "sultan":
        hrm_kasim "\"The jingling one! I remember you. You danced at me. Nobody dances {i}at{/i} me. Come here, my flower.\""
    else:
        hrm_kasim "\"The new concubine. They tell me you dance. Come here, my flower.\""
    "You stay at the foot of the bed in your sheer silks with your hands folded very carefully at the front."
    hrm_you "\"Majesty— I'm— there must be some mistake. I'm not the one you— I've only just come, I'm not ready, I'm not— I'm really not what you think—\""
    hrm_kasim "\"Kneel.\""
    "He doesn't raise his voice. He doesn't need to. He just doesn't hear no, the way a man who's never once heard it doesn't. He sets the cup down and stands, and the robe falls open the rest of the way."
    show cg hrm_kneel onlayer cgl
    "Somehow you're on your knees on the silk rug in front of him. His cock is right there. It's big. Bigger than yours ever was, heavy and dark and already half hard, and his big warm hand comes down to rest on top of your head."
    menu:
        "On your knees before the Sultan."
        "Try to explain":
            $ hrm.shout4 = "explain"
            hrm_you "\"Majesty, I really have to— there's something you should know about me, I'm not— {i}mmph{/i}—\""
            "He guides it in while you're talking. It's very efficient."
        "Turn your face away":
            $ hrm.shout4 = "turn"
            "You turn your face away. His big hand turns it back, gently, unhurried, and his cock is at your lips, and he waits there, patient as a man waiting for a ferry, until you open."
    hrm_you "\"{i}Mmh{/i}— no— {i}mmph{/i}— Majesty— {i}mmh{/i}—\""
    hrm_kasim "\"There. There we are. Don't they teach you girls anything in there? Use your tongue, my flower.\""
    show cg hrm_kneel_deep onlayer cgl
    "He holds your head and rocks into your mouth, slow and lazy and deep, deeper, until your nose is in his belly and your eyes go wide."
    vn_sfx "{i}Shlp. Shlp. Shlp.{/i}"
    hrm_you "\"{i}Mmph!{/i} {i}Mmh{/i}— {i}mmph{/i}—\""
    "Your first. Your first cock, in your mouth, the Sultan's, the man you robbed. And the oil's in you from the morning, hot and humming, and something in you that should be sputtering is {i}sucking.{/i}"
    hrm_kasim "\"Ahh. There. You've a talent, my flower.\""
    show cg hrm_kneel_drool onlayer cgl
    "He pulls out of your mouth, slick and shining, and you gasp for air with a string of spit from your lip to the tip of him."
    hrm_you "\"Majesty— {i}hahh{/i}— please, I'm not— you don't know what I—\""
    hrm_kasim "\"Good. On the cushions now.\""
    show cg hrm_cushions onlayer cgl
    "He lays you over the heaped silk cushions face down, the way you'd lay out a fine cloth. You remember Zarina: {i}lie on your belly and he'll never look.{/i} You lie very flat. The cage presses into the silk under you."
    "He pours oil down the small of your back. It runs down, warm, and he works it into you with his thumb, and then he's there, the big blunt head of him, pressing."
    hrm_you "\"No— no, wait— Majesty, wait, that's— {i}hahh{/i}— please, I didn't— I can't—\""
    vn_sfx "{i}Shhlk.{/i}"
    "He slides in. Slow. All of it, slow, bit by endless bit, the oil burning hot and opening you up for him, until his hips are flush with your ass and you're full of him to the throat."
    hrm_you "\"{i}Ahh{/i}— {i}ahh{/i}— it's so {i}big{/i}— Majesty, it's all the way— {i}ahh{/i}—\""
    hrm_kasim "\"Shh. Shh. You were made for this, my flower. Listen to you.\""
    "His hands go to your new breasts and squeeze them. Then your hips. Then your breasts again. They never go lower. He never reaches round. He never notices the cage."
    "He starts to move. Slow, lazy, deep strokes, the way a man rows a pleasure boat."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    hrm_kasim "\"Do you know, my flower, a thief broke into my treasury not a week ago. Stole my ruby. My {i}favourite{/i} ruby.\""
    hrm_you "\"{i}Hahh{/i}— did he— {i}ahh{/i}— Majesty—\""
    hrm_kasim "\"He did! Over the roofs and gone! If I ever catch that thief, I'll have him counting my ceiling tiles for a year!\""
    "He says it inside the thief. Balls deep in the thief. You start to laugh, and the laugh comes out as a moan, long and high, and you can't stop it."
    menu:
        "The Sultan wants to know what you'd do with the thief."
        "\"Make him scrub the floors!\"":
            $ hrm.punish4 = "floors"
            hrm_you "\"Make him— {i}ahh{/i}— make him scrub the floors too, Majesty— on his knees— {i}ahh{/i}— all of them—\""
            hrm_kasim "\"Ha! Wicked! The ceiling {i}and{/i} the floors!\""
        "\"Make him dance in a coin belt!\"":
            $ hrm.punish4 = "belt"
            hrm_you "\"Make him— {i}ahh{/i}— make him dance for the court, Majesty— in a coin belt— {i}ahh{/i}— every night—\""
            hrm_kasim "\"Ha! In a coin belt! I'd {i}pay{/i} to see it!\""
    show cg hrm_cushions_deep onlayer cgl
    $ hrm.broke4 = True
    "{color=#f0a0c0}His oiled hands work your breasts as he fucks you, kneading, squeezing, lifting, and they swell into his palms, fuller and heavier with every squeeze, until they spill between his fingers.{/color}"
    hrm_kasim "\"Mm. They grow, in my hands. Do you feel that?\""
    hrm_you "\"I feel it— {i}ahh{/i}— Majesty, I feel everything— don't— {i}ahh{/i}— don't stop— oh, gods, {i}don't stop—{/i}\""
    show cg hrm_cushions_hard onlayer cgl
    "Then he stops being lazy. He gets a fist in your long black hair and fucks you hard into the cushions, the silk sliding, the bed creaking, the lamps swinging on their chains."
    vn_sfx "{i}PAP. PAP. PAP. PAP.{/i}"
    hrm_you "\"Yes— {i}yes{/i}— fill me up, my sultan— fill me up, all of it— please— I want it, I want all of it—\""
    hrm_kasim "\"A year, at least! Two!\""
    hrm_you "\"Make it three— {i}ahh{/i}— and the floors— {i}AHH{/i}— I'm— Majesty, I'm going to— nobody's touching it and I'm going to— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg hrm_cushions_drip onlayer cgl
    vn_sfx "{i}Splurt. Splurt.{/i}"
    "Sultan Kasim comes deep in your ass with his hands full of your breasts, groaning into your neck. Hot, and a lot of it, so much you feel it fill you up."
    "And under you, unseen, the small golden cage drips onto the silk. You come hands-free through the bars, your whole body clenching round him, leaking onto his cushions where he'll never look."
    hrm_kasim "\"Ahh. A year. At {i}least.{/i}\""
    hrm_you "\"I hope— {i}hahh{/i}— I hope you never catch that thief, Majesty— {i}ahh{/i}— don't pull out— don't you {i}dare{/i}—\"" with vnfx("shake")
    jump hrm_ch4_after

## ---- ch 5: the private bath (the flip) ------------------------------------------------------------
label hrm_bath:
    $ hrm.fit = "nude"
    $ vn_enter(bg="hrm_privatebath", pc="smug", pc_tag="hrm_pc", cast=[("hrm_kasim", "lazy")], cg="hrm_bathwash")
    "The Sultan's private bath: a warm marble slab, a sunken pool, jars of oil, steam rolling under the lamps. And this time Dahlia sends for him."
    "She brings Zarina with her, in nothing, as promised. Zarina, who hasn't been summoned in a year, and who walks in behind Dahlia with her chin up and her braid down and her hands shaking, very slightly."
    hrm_kasim "\"Zarina! I'd forgotten— I'd quite forgotten how— well. Well, well.\""
    hrm_dahlia "\"Majesty. Lie down. We're going to wash you.\""
    $ hrm.asked = True
    hrm_kasim "\"My favourite gives orders now?\""
    hrm_dahlia "\"Your favourite asks very nicely. Lie down.\""
    "He lies down on the slab, laughing. Dahlia pours the oil over her own breasts, and over Zarina's, and the two of them climb onto him."
    "They wash the Sultan with their oiled bodies: breasts and bellies and thighs, sliding over his chest and his arms and his legs, slow, warm, slick, two women gliding over him like seals over a rock."
    show cg hrm_bathwash_2 onlayer cgl
    if hrm.shout4 == "explain":
        hrm_kasim "\"Do you know, the first night, you tried to explain something to me. What was it?\""
    else:
        hrm_kasim "\"Do you know, the first night, you turned your face away from me. Why was that?\""
    hrm_dahlia "\"Nothing, Majesty. Nerves. Hold still.\""
    "She slides her breasts up his chest, slow, until they're in his face, and he forgets the question."
    menu:
        "The Sultan's cock is hard against Dahlia's belly."
        "\"Tell me how much you want it.\"":
            $ hrm.tease5 = "tell"
            hrm_dahlia "\"Tell me how much you want it, Majesty. Tell me. Or I'll stop.\""
            hrm_kasim "\"You {i}wouldn't.{/i}\""
            hrm_dahlia "\"Try me.\""
            hrm_kasim "\"...Very much. Very, very much. Wicked girl.\""
        "\"Don't you dare look away.\"":
            $ hrm.tease5 = "look"
            hrm_dahlia "\"Watch, Majesty. Don't you dare look away.\""
            hrm_kasim "\"I couldn't if you paid me.\""
    show cg hrm_titjob_5 onlayer cgl
    "Dahlia slides down him, kneels between his legs on the warm marble, and wraps her big oiled breasts round his cock."
    "It disappears. All of it, swallowed in soft heavy slick flesh, and she squeezes them together with both hands and works him between them, slow, up and down, watching his face the whole time."
    vn_sfx "{i}Shlick. Shlick. Shlick.{/i}"
    hrm_dahlia "\"Like this, my sultan? {i}Mmh.{/i} Like this? It's what Nasrin taught me. She'll be so proud.\""
    hrm_kasim "\"Ahh— gods— my favourite— {i}ahh{/i}—\""
    "Zarina, beside him, kisses his chest, and his neck, and his ear, and whispers something in it that makes him buck up into Dahlia's breasts."
    show cg hrm_titjob_5_cum onlayer cgl
    hrm_kasim "\"{i}Ahh{/i}— my flower— {i}AHH{/i}—!\"" with vnfx("flash")
    vn_sfx "{i}Splurt. Splurt. Splurt.{/i}"
    "He comes between her breasts, and over them, and up over her chin, hot and thick, a lot of it. Dahlia laughs, and doesn't wipe a drop."
    show cg hrm_lick onlayer cgl
    "And Zarina leans in and licks it off her. Slowly. Every drop, off both breasts, round each nipple, up the throat, off the chin, while the Sultan lies back and watches with his mouth open."
    hide hrm_kasim
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"{i}Mm.{/i} He tastes of wine.\""
    hrm_dahlia "\"Everything here tastes of wine.\""
    show cg hrm_lick_kiss onlayer cgl
    "Then Zarina kisses it into Dahlia's mouth, long and deep, the two of them tongue to tongue over the Sultan's thighs, and Dahlia swallows."
    hide hrm_zarina
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"I have been a {i}fool.{/i} A whole year. A {i}fool.{/i}\""
    hide hrm_kasim
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Yes, Majesty.\""
    "The Sultan, still hard, gets up. He lays Dahlia over the slab on her front, with her face between Zarina's thighs, and oils her ass, and pushes in."
    vn_sfx "{i}Shhlk.{/i}"
    hrm_dahlia "\"{i}Ahh{/i}— yes— oh, yes— all of it, my sultan— {i}mmh{/i}— all the way—\""
    "She eats Zarina while he fucks her, still very much into women: her mouth on Zarina's clit, her tongue working, Zarina's thighs clamping round her ears and her heels drumming on the marble."
    hide hrm_kasim
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Dahlia— {i}Dahlia{/i}— oh, you clever girl, {i}there—{/i}\""
    hide hrm_zarina
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"When I catch that thief—\""
    if hrm.punish4 == "floors":
        hide hrm_zarina
        show hrm_kasim lazy at vn_cast_slot
        hrm_kasim "\"The floors, you said! On his knees!\""
    else:
        hide hrm_zarina
        show hrm_kasim lazy at vn_cast_slot
        hrm_kasim "\"In a coin belt, you said! Every night!\""
    hrm_dahlia "\"Better— {i}mmh{/i}— make him serve in the harem, Majesty. Oiled every morning. Kept on his knees. {i}Forever.{/i}\""
    hide hrm_zarina
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Wicked girl! {i}Yes!{/i}\""
    show cg hrm_slab_deep onlayer cgl
    $ hrm_body(5)
    "{color=#f0a0c0}He holds her by the waist as he fucks her, oiled hands round it, and her waist cinches in his grip, smaller, tighter, curving in under his palms between those big hips. And her breasts, pressed against the warm marble, swell against it, spreading out round her ribs, heavier with every stroke.{/color}"
    vn_sfx "{i}Pap. Pap. Pap. Pap.{/i}"
    "The steam rolls over everything. It hides the small golden cage swinging between her thighs. He never looks down. He never sees it."
    hrm_dahlia "\"Harder, my sultan— {i}mmh{/i}— harder— I want to feel it in my {i}teeth{/i}—\""
    hide hrm_kasim
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Dahlia— I'm— {i}AHH{/i}—!\""
    hrm_dahlia "\"{i}Mmh{/i}— Zarina— {i}mmh{/i}— me too, me too— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "Sultan Kasim coming deep in Dahlia's ass with a groan you could hear in the kitchens, his cum still shining on her breasts. Zarina coming on her tongue and gripping her long black hair in both fists. And Dahlia coming hands-free in the cage, leaking on the marble, laughing into Zarina, and not letting either of them go."
    jump hrm_ch5_after

## ---- ch 6: the great bath ---------------------------------------------------------------------------
label hrm_festival:
    $ hrm.fit = "collar"
    $ vn_enter(bg="hrm_greatbath", pc="smug", pc_tag="hrm_pc", cast=[("hrm_brask", "earnest")], cg="hrm_great_bath")
    "Festival night in the harem's great bath. Steam under the dome, lamps floating on the water, and the whole harem in the pool, forty women, oiling each other and watching."
    "Dahlia on her knees on the warm tiles at the pool's edge, the gold collar at her throat, the ruby between her breasts, and nothing else."
    "Captain Brask, in the doorway, in his best breastplate, sweating like a man who's been told to walk into the sea."
    hrm_brask "\"Gods, she's— Majesty, thank you. {i}Thank{/i} you.\""
    hrm_dahlia "\"Come here, Captain. You've earned it.\""
    show cg hrm_brask_cock onlayer cgl
    "He comes. He takes the breastplate off with his hands shaking, and the sash, and the rest, and stands in front of her with his cock out, red to the ears, already hard as his sword."
    hrm_brask "\"My lady, I— I've never— not with a— the Sultan's {i}own—{/i}\""
    hrm_dahlia "\"Shh, Captain. Closer.\""
    "Behind her, Sultan Kasim drops his robe on the tiles, and kneels, and oils her ass with a whole jar, laughing."
    show cg hrm_spit onlayer cgl
    vn_sfx "{i}Shhlk.{/i}"
    "The Sultan sinks into her from behind, deep, all of it. And the captain steps in front, and Dahlia takes his cock in her mouth."
    "The man who chased the thief over the rooftops, sweating, thanking his sultan over her head, with the thief sucking him."
    hrm_brask "\"Majesty— {i}gods{/i}— she's— thank you, Majesty, thank you—\""
    hide hrm_brask
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Isn't she {i}wonderful?{/i}\""
    hrm_dahlia "\"{i}Mmh{/i}— {i}mmph{/i}— Captain— {i}mmh{/i}—\""
    "Zarina, Leyla and Nasrin wade up in the water round her, and reach up, and their hands are on her huge breasts: lifting, oiling, squeezing, pinching, six hands, while the Sultan rocks her onto the captain's cock and back onto his own."
    if hrm.bet == "leyla":
        hide hrm_brask
        show hrm_leyla giggle at vn_cast_slot
        hrm_leyla "\"First to make her leak! Nasrin, you're {i}not{/i} winning this one!\""
    else:
        hide hrm_brask
        show hrm_nasrin lazy at vn_cast_slot
        hrm_nasrin "\"First to make her leak. I'll win.\""
    "And all round the pool, forty women, watching, oiling each other, giggling, whispering behind their hands."
    vn_sfx "{i}Pap. Pap. Glk. Glk. Pap.{/i}"
    show cg hrm_secret onlayer cgl
    "Then the Sultan's hand slides round her hip, round and down, for the first time, to her belly, and lower. And finds the cage."
    "He stops. Dead. Balls deep in her. His fingers close round the small golden cage and turn it, slowly, the way Orhan does."
    "Then he laughs. Delighted, enormous, so loud it rings off the dome and stops every woman in the water."
    hide hrm_brask
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"My favourite has a secret.\""
    menu:
        "His hand on the cage. The captain's cock in her mouth. The whole harem holding its breath."
        "\"Surprise, my sultan.\"":
            $ hrm.secret6 = "surprise"
            "She lets the captain's cock slip out of her mouth for one second."
            hrm_dahlia "\"Surprise, my sultan.\""
            hide hrm_brask
            show hrm_kasim lazy at vn_cast_slot
            hrm_kasim "\"Surprise! {i}Ha!{/i} The best surprise of my life!\""
        "\"Keep it, then.\"":
            $ hrm.secret6 = "keep"
            "She lets the captain's cock slip out of her mouth for one second."
            hrm_dahlia "\"Keep it, then, Majesty. It's yours.\""
            hide hrm_brask
            show hrm_kasim lazy at vn_cast_slot
            hrm_kasim "\"Oh, I {i}shall.{/i}\""
    show cg hrm_key onlayer cgl
    hide hrm_brask
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Orhan! Orhan, come here!\""
    "Orhan comes, beaming, wading down the steps in his purple robe with the hem held up. The Sultan holds out a hand. Orhan unhooks the small gold key from his belt and lays it in the Sultan's palm, without a word."
    if hrm.fair == "fair":
        hide hrm_brask
        show hrm_orhan jolly at vn_cast_slot
        hrm_orhan "\"She said {i}fair{/i}, Majesty. When I put it on her. Just {i}fair.{/i}\""
    else:
        hide hrm_brask
        show hrm_orhan jolly at vn_cast_slot
        hrm_orhan "\"She said {i}fair enough{/i}, Majesty. When I put it on her. {i}Fair enough!{/i}\""
    "The Sultan hangs the key on a gold chain round his own neck. He doesn't unlock it. He pats the cage, once, exactly the way Orhan does."
    "Captain Brask, eyes shut, thanking his sultan, doesn't notice a thing."
    show cg hrm_milk_cage onlayer cgl
    "The Sultan goes back to fucking her ass, harder now, laughing. And Zarina ducks under the water, comes up beneath her, reaches between her thighs and milks the cage, fingers working, while Leyla and Nasrin hold the small silver dish under it."
    hide hrm_brask
    show hrm_zarina wicked at vn_cast_slot
    hrm_zarina "\"Leak for us, Dahlia. Leak for the whole harem.\""
    hrm_dahlia "\"{i}Mmph{/i}— {i}mmh!{/i}— {i}mmmh{/i}—!\""
    show cg hrm_spit_hard onlayer cgl
    $ hrm_body(6)
    "{color=#f0a0c0}And as the oil goes into her one last time, from every hand at once, her breasts and hips and ass ripen in their hands: the breasts heavier, rounder, spilling over Nasrin's fingers, the hips wider under the Sultan's grip, the ass fuller where he slams into it. The biggest she'll ever be. The biggest anyone in the palace has ever been.{/color}"
    vn_sfx "{i}PAP. PAP. PAP. GLK. GLK.{/i}"
    hide hrm_kasim
    hide hrm_leyla
    hide hrm_nasrin
    hide hrm_orhan
    hide hrm_zarina
    show hrm_brask earnest at vn_cast_slot
    hrm_brask "\"My lady— I'm going to— Majesty, may I—\""
    hide hrm_brask
    show hrm_kasim lazy at vn_cast_slot
    hrm_kasim "\"Over her face, Captain! It's a festival!\""
    hrm_dahlia "\"{i}Mmph{/i}— yes— yes, Captain— my sultan— {i}AHH{/i}— keep it, keep the key— keep me— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg hrm_finale onlayer cgl
    $ hrm.ending = "key"
    $ vn_feat("The Sultan Keeps the Key")
    vn_sfx "{i}Splurt. Splurt. Splurt.{/i}"
    if hrm.toast6 == "thief":
        "Sultan Kasim coming deep in Dahlia's ass and roaring {i}to the thief!{/i} with the key swinging on its chain against her back."
    else:
        "Sultan Kasim coming deep in Dahlia's ass and roaring {i}to the captain!{/i} with the key swinging on its chain against her back."
    "Captain Brask coming over her face with his eyes shut and no idea who she is. Zarina milking the small golden cage into the silver dish. The whole harem watching from the water, and cheering."
    "And Dahlia coming hands-free, leaking through the bars, laughing with her mouth open and the captain's cum on her tongue, with the Sultan's ruby bouncing between her breasts."
    jump hrm_route_return
