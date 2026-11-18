## THE STORY: chapters 6-7 and the endings (PLAN.md). Floor 6, Corvina (ENTRANCED: the voice, the hair and its colours);
## floor 7, Mireille (ENTHRALLED: breasts at the cap, a woman's face, heart pupils; the cock stays); the deciding choice (both
## marked as endings): Break the charm -> A "Cleared", Walk to her -> B "Kept". dbf.curious / dbf.wary and dbf.gave /
## dbf.fought colour each epilogue (dbf_thought_line).

## ---- 5. Saturday: floor six, Corvina --------------------------------------------------------------------------------

label dbf_saturday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_morning_five")
    "The dress has made its peace with your new shape: the skirt flares out over your hips and sits short over the swell of your arse, the waist pinched to nothing, the bodice cupping your breasts high."
    "It's beautiful. It's a woman's dress now. It always nearly was."
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND.{/color}"
    "Two floors. You take the stairs with your hips swaying and your breasts bouncing and the charm humming you along."
    $ vn_set_time(9, 30)
    $ vn_enter(bg="dbf_aerie", pc="curious", pc_tag="dbf_pc", cast=[("dbf_corvina", "smirk")], cg="dbf_corvina_perches")
    "Floor six has no roof. The sky's right there, blue and windy, and the room is all perches and nests and loose feathers whirling."
    "On the highest perch, a harpy: a woman's lush body, bare, with great wings where her arms should be and feathered legs ending in soft talons."
    "Her plumage runs like a sunset: rose at her shoulders, amber down her wings, gold at the very tips. She drops off the perch and glides down to you."
    dbf_corvina "\"So you're the one they've all been whispering about! Oh, you're {i}lovely.{/i} I'm Corvina. Would you like to hear a song?\""
    dbf_you "\"No.\""
    dbf_corvina "\"Everyone always says that.\""
    "She opens her mouth and sings: one long rising note, pure and golden, that fills the whole sky."
    menu:
        "The song's in the air all round you."
        "Cover your ears":
            "You clap your hands over your ears. It comes through your hands. It comes through your bones. It comes up through the floor into your feet."
            $ dbf.wary += 1
        "Listen to the song":
            "It's the most beautiful sound you've ever heard. You want to hear how it ends. You stand quite still and listen."
            $ dbf.curious += 1
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED.{/color}"
    "Your thoughts go soft and slow and golden. You forget you're holding a rapier. You forget what a rapier's for. The song's the only thing there is."
    show cg dbf_wing_embrace onlayer cgl
    "She folds her wings round you and lays you back in the biggest nest, soft with down, and kneels between your thick thighs, still singing, and lifts your skirt."
    "Then she takes your cock into her mouth, and keeps singing round it."
    vn_sfx "Juru. Juru. Mmmmmm."
    "The song goes into you through your cock. It hums in your belly, your breasts, your teeth. It's the strangest, sweetest thing that's ever happened to you."
    dbf_you "\"Ahh♡— oh— ohh, it's {i}inside—{/i} the song's— ahh♡—\""
    menu:
        "You can feel a note rising in your own throat."
        "Shout her down":
            "You shout. You shout a war cry, the one you've used for three years, and it comes out— it comes out high. High and sweet and clear. Your war cry, in a voice like a bell."
            $ dbf.fought += 1
        "Sing with her":
            "You open your mouth and sing with her. You don't know the song. You find you know the song. Your voice rises with hers, higher and higher, sweet as hers."
            $ dbf.gave += 1
    "{color=#ff5fb8}Your voice climbs as she sings round you and doesn't come back down: lighter, higher, a soprano, the voice you'd hear and turn round for in a crowded street.{/color}"
    "{color=#ff5fb8}And your hair: it pours.{/color}"
    "{color=#ff5fb8}It runs down your back, past your shoulder blades, past your waist, down over the swell of your arse to your hips, and as it grows the colour floods into it from the roots: rose first, then amber flowing down the lengths, then gold at the very tips.{/color}"
    "{color=#ff5fb8}Her colours. Sunset, all the way down.{/color}"
    vn_sfx "Juru. Juru. Mmmmmm."
    dbf_you "\"Ahh♡— ahhh♡— AHHHHHHH♡—!\"" with vnfx("flash", "shake")
    "You come singing."
    "You come singing a note so high and pure the feathers lift off the floor round you, and Corvina swallows it all and joins the note and holds it with you until you both run out of breath."
    dbf_corvina "\"Oh, {i}listen{/i} to you. You'll make Mireille cry. Go on up.\""
    "You find your rapier in the nest. You prod her in the wing with it, quite gently, as she lifts off, and she laughs and spirals away into the sky."
    "Six down."
    $ dbf_grow(6)
    $ dbf.fit = "torn"
    $ vn_set_time(20, 30)
    $ vn_enter(bg="dbf_waystone", pc="dazed", pc_tag="dbf_pc", cast=[], cg="dbf_sixth_waystone")
    "The last waystone. Above it, one flight of stairs, lit pink."
    "{color=#ff5fb8}Hair to your hips, a waterfall of sunset: rose at the roots, amber through the lengths, gold at the tips, soft as down. Full pink lips, a soft rounded face.{/color}"
    "{color=#ff5fb8}Big round breasts, a pinched waist, wide hips, a big soft arse, thick thighs, smooth skin glowing in the crystal's light. Your cock, still there, half hard, between those soft thighs.{/color}"
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED.{/color}"
    dbf_you "\"Tomorrow I kill her. And it all comes off.\""
    "Your voice is a bell. You hum her song as you fall asleep. You don't notice you're doing it."
    call dbf_cut(7, 1, "Sunday. The top.")
    jump dbf_sunday

## ---- 6. Sunday: floor seven, Mireille -------------------------------------------------------------------------------

label dbf_sunday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="cocky", pc_tag="dbf_pc", cast=[], cg="dbf_morning_six")
    "The dress has outdone itself. White and violet still, but cut for you now, every line of it: the low bodice, the pinched waist, the flared short skirt over your hips."
    "Your sunset hair spills down the back of it to your hips."
    "You lift your rapier in both hands, and climb the last stairs."
    $ vn_set_time(10, 0)
    $ vn_enter(bg="dbf_throne", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_mireille", "smirk")], cg="dbf_mireille_waits")
    "Floor seven is a throne room in pink stone, all silk and candlelight."
    "Mireille lounges across the throne with one leg over the arm, and she's even more than she was over the gate: the horns, the wings, the tail swaying, breasts and hips that make the whole room lean toward them."
    dbf_mireille "\"{i}Look{/i} at you. Oh, they've done such a good job. Come here, sweetheart. Let me see.\""
    dbf_you "\"I'm here to kill you.\""
    "It comes out as a sweet high bell. She smiles."
    dbf_mireille "\"Of course you are. Go on, then.\""
    "You charge."
    "You charge as well as you can on those hips with that weight on your chest and that sword in two slender hands, and she lifts a hand and fires: hearts, a dozen of them, a swarm of pink light."
    menu:
        "A dozen hearts, coming at you."
        "Dodge the hearts":
            "You dodge."
            "You weave through them the way you used to weave through arrows, and your body is wrong for it, all curves and weight, and the third heart takes you in the chest and the rest follow it in."
            $ dbf.wary += 1
        "Open your arms to them":
            "You know exactly what they do now. And you open your arms anyway, because you want to feel a dozen of them land at once."
            "They land."
            $ dbf.curious += 1
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED. ENTHRALLED.{/color}"
    "The world goes pink at the edges. Your rapier rings on the floor. Your feet walk you up the steps of the throne, and you climb into her lap, and she gathers you in."
    show cg dbf_throne_lap onlayer cgl
    dbf_mireille "\"Good girl.\""
    "You shiver all the way down."
    "She lays you across the throne and tugs your bodice down, and presses her breasts to yours, and slides your cock between her thighs, and her spade-tipped tail curls up under your skirt and between the cheeks of your big soft arse, slick, and pushes in."
    vn_sfx "Nuchu. Nuchu. Pan. Pan."
    dbf_you "\"Ahh♡— Mireille— ahh, her tail— so deep— ahh♡—\""
    menu:
        "Her tail's fucking you open, slow and deep."
        "Fight it":
            "You fight it. Somewhere under the pink, there's still the guild's best blade, and she claws at the charm from inside, and squirms, and pants, and fights."
            dbf_mireille "\"Mm. There's my hero. Keep fighting, sweetheart. I love it when they fight.\""
            $ dbf.fought += 1
        "Ask for more":
            dbf_you "\"More— please— more, Mireille, deeper—\""
            dbf_mireille "\"{i}Such{/i} a good girl.\""
            $ dbf.gave += 1
    show cg dbf_pegged onlayer cgl
    "Her tail thrusts deep and steady, and her hands go to your breasts and squeeze, and pink light spills out from under her palms into you."
    $ dbf_grow(7)
    "{color=#ff5fb8}Your breasts swell in her hands: bigger, heavier, fuller, until they're huge, weighted, round and heavy on your chest, spilling over her fingers.{/color}"
    "{color=#ff5fb8}Your face warms, and the last of the old shape softens out of it: the jaw, the brow, the nose, a woman's face now, soft and lovely, with your full pink lips.{/color}"
    "{color=#ff5fb8}Your violet eyes go hazy, and in the middle of each, the pupil turns to a pink heart. Your cock stays, smaller and smooth and pink, aching, trapped between her thighs.{/color}"
    vn_sfx "Pan. Pan. Pan. Nuchu."
    dbf_you "\"AHHH♡— Mireille— I'm— I'm— AHHHHHHH♡—!\"" with vnfx("flash", "shake")
    "You come so hard the candles gutter."
    "You come with her tail deep in you and your new breasts in her hands and your bell of a voice ringing off the pink stone, and for a long, long moment there is nothing in the world but her."
    $ vn_set_time(11, 0)
    $ vn_enter(bg="dbf_throne", pc="charmed", pc_tag="dbf_pc", cast=[("dbf_mireille", "hungry")], cg="dbf_the_choice")
    "When you come back, you're lying across her lap, and she's stroking your sunset hair."
    "Your rapier is on the floor below the throne. You can see it. If you rolled off her lap, you'd land beside it."
    dbf_mireille "\"You can, you know. Pick it up. I won't stop you. That's the game.\""
    dbf_mireille "\"Or you can stay.\""
    if dbf.curious > dbf.wary:
        "You've touched every heart, every cup, every song on the way up, just to see. You know which one you want to touch now."
    else:
        "Under the pink, very small and very hard, there's still the blade you were on Monday. It's waiting for you to pick it up."
    menu:
        "The rapier, or her."
        "Break the charm" (ending=True):
            jump dbf_end_cleared
        "Walk to her" (ending=True):
            jump dbf_end_kept

## ---- the line the week earns ----------------------------------------------------------------------------------------

label dbf_thought_line:
    if dbf.gave > dbf.fought:
        "You stopped fighting them somewhere around the fourth floor. You've never been sorry."
    elif dbf.fought > dbf.gave:
        "You fought every one of them, all the way up. You still think you'd do it again. You still think you'd lose again, too, and you're glad."
    else:
        "Some of them you fought and some you didn't. They all won anyway. You think that was the point."
    return

## ---- Ending A: Cleared ----------------------------------------------------------------------------------------------

label dbf_end_cleared:
    "You roll off her lap. You land beside the rapier. Your hand closes round the hilt."
    "The charm screams at you to put it down."
    "Every ailment you've got pulls at once: the paralysis heavy in your arms, the milk warm in your head, the song humming you sweet and slow."
    "You pick it up anyway, in two slender hands, the way you've picked it up every morning for three years."
    show cg dbf_the_thrust onlayer cgl
    "Mireille smiles at you from the throne the whole way."
    dbf_mireille "\"There she is.\""
    "You drive it home. She bursts into pink light, laughing, and the light fills the room and goes out."
    dbf_mireille "\"{size=-8}Come back and visit, sweetheart...{/size}\""
    "The candles go out all down the spire. Floor by floor, the lights go out."
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED. ENTHRALLED.{/color}"
    "Nothing comes off."
    $ vn_clock.day += 1
    $ vn_set_time(10, 0)
    $ vn_enter(bg="dbf_guild", pc="flustered", pc_tag="dbf_pc", cast=[("dbf_ottilie", "stare")], cg="dbf_return")
    "You walk into the guild hall at ten on Monday morning in your white-and-violet dress, with your sunset hair to your hips and your hips swaying and your breasts bouncing and Mireille's throne-room banner rolled over your shoulder as a trophy."
    "The hall goes completely silent."
    "Ottilie looks up at you over her spectacles for a very long time."
    dbf_ottilie "\"...Hand.\""
    "You lay your palm on the lens."
    "{color=#ffd36b}TIRYSIA. LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED. ENTHRALLED. ALL PERMANENT. SPIRE OF VELUNE: CLEARED.{/color}"
    dbf_ottilie "\"Cleared. Well. That's a first.\""
    dbf_ottilie "\"Eight ailments. That's also a first.\""
    dbf_you "\"I'll shake them off by supper.\""
    "It comes out a bell. Ottilie, who has never once smiled at you in three years, smiles."
    dbf_ottilie "\"I'm sure you will.\""
    "She pays you the bounty in full. Every adventurer in the hall watches you count it."
    $ vn_clock.day += 30
    $ vn_set_time(16, 0)
    $ vn_enter(bg="dbf_throne", pc="blissful", pc_tag="dbf_pc", cast=[("dbf_mireille", "hungry")], cg="dbf_cleared_visit")
    "A month later."
    "Succubi come back. Mireille took three days. The guardians took less."
    "You've cleared four dungeons this month at level thirty-four, in your dress, with your sunset hair tied up and every one of your eight ailments slowing you down."
    "You've taken to it. Ottilie says you've a following."
    "And on your days off, you walk out across the moor to the pink spire, and climb it. Every floor. Every guardian. Every ailment, landed fresh and sweet."
    show cg dbf_cleared_night onlayer cgl
    "And at the top, Mireille, every time, on her throne, with her arms open."
    vn_sfx "Nuchu. Pan. Pan. Pan."
    dbf_you "\"Ahh♡— Mireille— more— I climbed all the way up again— ahh♡— AHHHHHH♡—!\"" with vnfx("flash", "shake")
    dbf_mireille "\"I know, sweetheart. Good girl.\""
    "You always win, at the end. You always pick up the rapier. She always lets you."
    call dbf_thought_line
    call dbf_route_return("Cleared")

## ---- Ending B: Kept -------------------------------------------------------------------------------------------------

label dbf_end_kept:
    "You look at the rapier for a long moment."
    "Then you turn over in her lap, and put your arms round her neck, and kiss her."
    dbf_mireille "\"{i}There's{/i} my good girl.\""
    "{color=#ffd36b}LEVEL 34. STATUS: CHARMED. SOFTENED. PARALYSED. DRAINED. MILK-DRUNK. BOUND. ENTRANCED. ENTHRALLED.{/color}"
    "And then, one by one, the words on your status bar fade out, and something else writes itself across all of them in pink."
    "{color=#ff7ad9}STATUS: HERS.{/color}"
    $ vn_set_time(20, 0)
    $ vn_enter(bg="dbf_throne", pc="blissful", pc_tag="dbf_pc", cast=[("dbf_mireille", "hungry"), ("dbf_holda", "hungry")], cg="dbf_all_seven")
    "That night they all come up the stairs. Glaze, wobbling and cheerful. Verbena, trailing vines. Morwen, cool and polite. Holda with a jug of milk."
    "Sessaly, uncoiling across the floor. Corvina, gliding in through the window, singing."
    dbf_mireille "\"Everyone, meet our new seventh-floor guardian.\""
    show cg dbf_kept_group onlayer cgl
    "And they take you, all of them, all at once. Sessaly's coils round your waist. Glaze round your cock. Mireille's tail deep in your arse."
    "Holda's breast at your lips and Verbena's vines at your nipples and Morwen's cold hands everywhere and Corvina's song in your ears."
    vn_sfx "Gupu. Nuchu. Chuu. Pan. Pan. Pan."
    dbf_you "\"Ahh♡— everyone— all of you— ahh♡— yes— I'm yours, I'm yours, I'm— AHHHHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byururu."
    $ vn_clock.day += 60
    $ vn_set_time(15, 0)
    $ vn_enter(bg="dbf_throne", pc="charmed", pc_tag="dbf_pc", cast=[], cg="dbf_kept_epilogue")
    "Two months later."
    "The guild lists Tirysia as missing in the Spire of Velune. Ottilie didn't write the word {i}dead.{/i} She knew better."
    "A party comes up the spire in the spring: four of them, a swordsman, a mage, a priest and a lancer, all very serious and well armed."
    "They lose the mage on floor two and the priest on floor four, both very happily. The swordsman and the lancer make it to the top."
    "Before Mireille's throne, a new guardian is waiting for them:"
    "a woman in a white-and-violet battle dress with sunset hair to her hips, huge breasts, a pinched waist, a big soft arse, pink hearts in her violet eyes,"
    "and something under her skirt they don't expect."
    dbf_you "\"Ooh. Two of you. And you're both so {i}pretty.{/i}\""
    "You blow them a kiss. It leaves your lips as a pink heart, the size of a palm, drifting toward them slow as a soap bubble."
    "The swordsman looks at it, curious. He's never seen anything like it. He reaches out one finger, just to see."
    call dbf_thought_line
    call dbf_route_return("Kept")
