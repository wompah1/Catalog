## THE STORY: chapters 6-7 and the endings (PLAN.md). Friday Quist's last page and the long hour; Saturday the Cradle opens
## and asks, and the deciding choice (both marked as endings): Climb out -> A "Climbed Out", Stay in -> B "Stayed In".
## The rune he picked most gives each epilogue one line (sns_part_line).

## ---- 6. Friday: the last page -----------------------------------------------------------------------------------

label sns_friday:
    $ sns.fit = "nude"
    $ sns_grow(6)
    $ vn_enter(bg="sns_cradle_room", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_last_page")
    "{color=#ff5fb8}Your hair falls to the middle of your back now, black and violet, and it pools round the rim of the collar when you bow your head.{/color}"
    "{color=#ff5fb8}Your face in the mirror is soft and full-lipped and lovely, and it's still yours.{/color}"
    "{color=#ff5fb8}Hesper says your breasts are big now, heavy and round, swaying every time you breathe; your hips wide, your arse full, your thighs soft.{/color}"
    "{color=#ff5fb8}And your cock small and smooth and pink, so sensitive the air down there makes it twitch.{/color}"
    "Hesper's got the daybook open at the last page. She's been saving it."
    sns_hesper "\"'On the seventh morning the work is finished, and the Cradle opens of itself and asks the one within what they want. And whatever the answer, the Cradle gives it.'\""
    sns_you "\"What does that mean?\""
    sns_hesper "\"It means tomorrow you get to choose. Out, or in. I've read all of it this time. That's really all it says.\""
    "She takes the key ring off her belt, finds the sixth key, the lever key, and holds it up between you."
    sns_hesper "\"Or tonight. I can pull it tonight, before the last work's done. You'd walk out of here a bit less than finished. Say the word.\""
    "You look at the key a long while. You look at her."
    sns_you "\"...Press the rune, Vane.\""
    call sns_rune("She puts the key away, and smiles, and doesn't hide it. \"Which one?\"")
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_pit", pc="moaning", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_hour_friday")
    "The last hour. Nine o'clock, and everything comes back, and she's down there with you with her lamp and her glass cock strapped on and every key on the ring."
    call sns_hour_part
    show cg sns_double onlayer cgl
    "The tentacles lift you and spread you, your heavy breasts swaying in their coils, and she pushes into your arse, slow, all the way."
    "And then, alongside her, slick and patient, a tentacle pushes in too."
    vn_sfx "Zupuu. Nuchu."
    sns_you "\"Two— two— Hesper there's two— you and it— both— I'm so full— so full♡—\""
    menu:
        "Stretched round her and round it at once, wide open, everything."
        "Beg her for more":
            sns_you "\"More— please— everything, Hesper, all the keys, all of them, use all of me— please♡—\""
            sns_hesper "\"All of them, then.\""
            vn_sfx "Click. Click. Click."
            $ sns.soft += 1
        "Dare her to do worse":
            sns_you "\"Is that— is that all you've got, Vane? Hah— two? I've had— hhh♡— I've had three— you're losing your touch—\""
            sns_hesper "\"Oh, you're going to regret that.\""
            vn_sfx "Click. Click. Click."
            "You don't regret it. Not once in the whole hour."
            $ sns.brat += 1
    vn_sfx "Pan. Pan. Juppu. Pan. Chuu."
    "Every key. The suckers on your nipples. The coils on your breasts. The sleeve on your cock. Her and the tentacle in your arse, moving together, one in as the other comes out."
    "You scream, and the tower rings with it."
    sns_you "\"Hesper— Hesper— Hesper♡— I'm coming— I'm coming so hard— AHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Byuru. Dopyu."
    "She comes too, grinding the glass cock into you, with her forehead against your back. You feel that. Gods, you feel that."
    call sns_cut(5, 1, "Saturday. The seventh morning.")
    jump sns_saturday

## ---- 7. Saturday: the Cradle asks -----------------------------------------------------------------------------

label sns_saturday:
    $ sns.fit = "nude"
    $ sns_grow(7)
    $ vn_set_time(5, 40)
    $ vn_enter(bg="sns_pit", pc="dazed", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_cradle_opens")
    "At dawn the stone chimes, and doesn't stop chiming, and the ring round your chest goes soft as wax, and you slide down through it into the dark."
    "Down into the pit room, slow. The tentacles take you, and lower you, gentle as hands, and set your bare feet on the warm stone floor. And you can feel your feet."
    "You can feel all of you, and nothing's holding you, and nobody's hiding anything."
    "Hesper's there with the lamp. She doesn't say anything. She just turns you, by the shoulders, to face the tall mirror in its brass frame on Quist's wall."
    show cg sns_mirror onlayer cgl
    "{color=#ff5fb8}A hundred and sixty-eight centimetres. Black hair to your waist, falling in heavy waves, violet where the lamplight hits it. A soft, full-lipped face with your grey eyes in it.{/color}"
    "{color=#ff5fb8}Big, heavy breasts, round and high, the nipples dark and fat and tender.{/color}"
    "{color=#ff5fb8}A waist you could nearly circle with your hands, and hips that flare out from it, wide and soft, and a round, full arse.{/color}"
    "{color=#ff5fb8}Thick thighs. Smooth skin all over, without a single hair. And between your thighs your cock, small now, smooth and pink, still yours, and half hard just from being looked at.{/color}"
    sns_you "\"...That's me.\""
    sns_hesper "\"That's you.\""
    "Round the rim of the open collar above, the five runes are lit, and a sixth you've never seen, in the middle of the floor. Hesper reads it without being asked."
    sns_hesper "\"'What do you want?'\""
    "Up the stair, the door, and the morning, and Brackwater, and the Hall. Here, the warm dark, and the hour, and her hands on the keys."
    if sns.soft > sns.brat:
        sns_hesper "\"Whatever you pick, I'm not going anywhere. I want you to know that before you pick.\""
    else:
        sns_hesper "\"Well, Ashdown? You've never once in your life not known what you wanted.\""
    menu:
        "The Cradle waits. Hesper waits."
        "Climb out" (ending=True):
            jump sns_end_out
        "Stay in" (ending=True):
            jump sns_end_in

## ---- the line the most-pressed rune earns ---------------------------------------------------------------------------

label sns_part_line:
    if sns.chest >= max(sns.nips, sns.hips, sns.cock, sns.mouth):
        "Of everything the Cradle did, it's your breasts that never let you forget it: heavy, aching to be held, so sensitive that a brush of cloth over them stops you mid-sentence."
        "Hesper holds them when she sleeps."
    elif sns.nips >= max(sns.hips, sns.cock, sns.mouth):
        "Of everything the Cradle did, it's your nipples that never let you forget it: fat and dark and so sensitive that Hesper can make you come from them alone, and does, whenever you start to get mouthy."
    elif sns.hips >= max(sns.cock, sns.mouth):
        "Of everything the Cradle did, it's your arse that never let you forget it: round and soft and so wide your hips sway on their own, and always, always aching to be filled."
    elif sns.cock >= sns.mouth:
        "Of everything the Cradle did, it's your cock that never let you forget it: small and smooth and so sensitive that Hesper's fingertip on it makes your knees go, and it comes in seconds, and it never stops wanting to."
    else:
        "Of everything the Cradle did, it's your mouth that never let you forget it: lips plump and soft, a tongue that feels everything, and a throat that opens like it was made for it."
        "You kiss Hesper for hours. You can't help it."
    return

## ---- Ending A: Climbed Out -------------------------------------------------------------------------------------------

label sns_end_out:
    $ sns.fit = "shirt"
    $ vn_set_time(9, 0)
    $ vn_enter(bg="sns_ruin_gate", pc="flustered", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_out_daylight")
    "You climb out."
    "Up the pit-room stair, through the round room past the empty Cradle, down the tower, out of the door into daylight, in Hesper's spare shirt, which won't button over your breasts,"
    "and her spare trousers, which won't button over your hips, and your own boots, which are too big now."
    "At the gate you stop and look back at the plinth through the open door, the violet flask in its shaft of light."
    sns_hesper "\"You still want it?\""
    sns_you "\"...No. I've got what I came in for.\""
    "You mean her. She knows it. She goes red to her braid."
    $ vn_set_time(22, 0)
    $ sns.fit = "nude"
    $ vn_enter(bg="sns_inn_room", pc="blissful", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_out_inn")
    "The Lamp and Ladder, Brackwater, the best room, paid for with a month of Hesper's survey fees. A real bed. A real fire. Nothing below your chest you can't feel."
    show cg sns_out_ride onlayer cgl
    "She undresses you slowly, like she's still surveying, and lays you on your back, and climbs over you, and settles down on your small, sensitive cock, pinning it flat to your belly under her, slick and hot, and grinds."
    "It's the first time anyone's been on it instead of round it, and it's {i}so{/i} much."
    vn_sfx "Nuchu. Nuchu."
    sns_hesper "\"Look at you. Look at you, Rook. You're beautiful.\""
    sns_you "\"Hesper— it's too— it's so sensitive— you're so hot— ahh♡— don't stop, don't you dare stop♡—\""
    "She rides you slow and then not slow, with her hands on your big soft breasts, squeezing, the way the tentacles did, the way you told her you liked, and your hips buck up against her and your hair spills everywhere across the pillow."
    sns_you "\"I'm coming— Hesper, I'm coming already, I'm sorry, I'm— AHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru."
    "She doesn't let you go soft. She keeps riding, laughing, and you come twice more before she does, and when she does she says your name like it's the answer to a riddle."
    $ vn_set_time(19, 0)
    $ vn_clock.day += 30
    $ sns.fit = "delver"
    $ vn_enter(bg="sns_delvers_hall", pc="blissful", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_out_epilogue")
    "A month later, at the Delvers' Hall. There's a new name on the board, chalked up by the Hallmaster himself: {i}Ashdown and Vane{/i}. Nobody quite believed it at first."
    "Nobody quite believed a lot of things."
    "You've had your leathers let out. You still talk too much. You still take every stair two at a time."
    "But you go second now, behind Hesper, and nobody at the Hall has ever seen you look happier about anything."
    call sns_part_line
    if sns.brat > sns.soft:
        "Last week you beat her to a barrow at Gallow's Edge and laughed at her from the top of it. That night she tied you to the bed and made you take it back, one key at a time."
        "You beat her to the next one too."
    else:
        "She still reads you the daybooks. All the way to the end of the sentence, now."
    call sns_route_return("Climbed Out")

## ---- Ending B: Stayed In --------------------------------------------------------------------------------------------

label sns_end_in:
    $ sns.fit = "nude"
    $ vn_enter(bg="sns_pit", pc="blissful", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_in_answer")
    "You don't look at the stair."
    sns_you "\"In.\""
    sns_hesper "\"Rook—\""
    sns_you "\"In. Put me back in. I want the dark, and the hour, and you at the desk. I want you to come down every morning and ask me where. That's what I want.\""
    "The sixth rune flares, and goes out, and the tentacles take you, gentle, and lift you up, and the ring at the top of the room softens and takes you back in, and closes, warm and snug, round your chest."
    "And the rest of you goes away. And you smile."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sns_pit", pc="blissful", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_in_hour")
    "That night she rings every key on the desk at once."
    show cg sns_in_everything onlayer cgl
    "Her glass cock in your arse and a tentacle beside it. Another in your throat, up top. The coils round your heavy breasts, the mouths on your nipples, the sleeve on your cock."
    "Every inch of your finished body full or held or sucked or stroked, all at once, an hour of it, everything."
    vn_sfx "Pan. Pan. Juppu. Nuchu. Chuu."
    sns_you "\"Mmmh♡— mmh♡— MMMMH♡—\""
    "The tentacle pulls from your mouth just long enough."
    sns_you "\"Yours— I'm yours, Hesper, I'm the Cradle's, I'm yours, keep me, keep me in here, keep fucking me forever— AHHHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru. Byuru. Dopyu."
    $ vn_set_time(8, 0)
    $ vn_clock.day += 60
    $ vn_enter(bg="sns_cradle_room", pc="blissful", pc_tag="sns_pc", cast=[("sns_hesper", "delver")], cg="sns_in_epilogue")
    "Two months later. Quist's Folly is on the Hall's board again, with a new note under it in Hesper Vane's tidy hand: {i}Closed for excavation. Do not enter.{/i} Nobody does."
    "Nobody ever had the nerve."
    "Every morning at eight she comes up the stair with bread and the daybook and her coat over her arm, and kneels at the rim, and kisses you, and asks."
    sns_hesper "\"Where today?\""
    "And every morning you tell her."
    call sns_part_line
    if sns.brat > sns.soft:
        "You still give her lip about it. She says she wouldn't know what to do with you if you didn't."
        "Then she goes down the stair, and at nine o'clock she shows you exactly what she'd do."
    else:
        "Some mornings she climbs into the dark with you, and lies against the warm wall of the pit while the tentacles hold you both, and you talk all day about nothing, and you don't miss the sky."
    call sns_route_return("Stayed In")
