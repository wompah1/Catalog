## bit's six Fridays. NOT A BIT: ch 1-2 forced, ch 3 the break, ch 4 the flip at the brunch, ch 5-6 consensual.
## Each chapter: the pinned list, the week's body, the act, the gag inside the act; every chapter ends mid-act.
## "It's a bit" once a chapter, ch 1-5. Miku talks in two and three words and is the filthiest in the room.

## ---- 1. Three in the Morning -------------------------------------------------------------------
label bit_ch1:
    $ bit.chapter = 1
    $ bit.fit = "own"
    $ vn_enter(bg="bit_karaoke", pc="sheepish", pc_tag="bit_pc", cast=[], cg="bit_banquette")
    "Three in the morning in a karaoke box. Trains dead, the fries gone cold, and you at the end of the banquette with four handbags at your feet. A year of carrying them."
    "Rena, the loud one: platform boots, doing all the talking, drunkest."
    "Saki, the camera, who sees the whole night through her phone screen."
    "Nono, the nervous one, already apologising for something."
    "Miku, the flat one: tanned, bleached, tall, who has never once laughed at anything, and hasn't moved from her seat all night."
    hide cg onlayer cgl
    $ vn_enter(bg="bit_karaoke", pc="flustered", pc_tag="bit_pc", cast=[("bit_rena", "loud")], cg="bit_makeover")
    bit_rena "\"I'm out of material. Three a.m., transformation time. Mori, show us your best gal. Dare. Nono, the face. Saki, the light.\""
    "Nono does the lashes, the lip, a long blonde wig off the box's costume rack, apologising the whole time. It's the first time in a year anybody has touched you on purpose."
    "Then she produces a packet of wax strips she apologises for owning."
    bit_rena "\"Wax him. Wax him everywhere.\""
    hide bit_rena
    show bit_nono sorry at vn_cast_slot
    bit_nono "\"Do you really want all of it gone? Sorry. Sorry.\""
    menu:
        "The wax strips."
        "\"It's a bit.\"":
            $ bit.wax = "bit"
            bit_you "\"It's a bit.\""
        "\"Go on, then.\"":
            $ bit.wax = "go"
            bit_you "\"Go on, then. It's a bit.\""
    $ bit_body(1)
    $ bit.fit = "kit"
    hide bit_rena
    show bit_nono sorry at vn_cast_slot
    bit_nono "\"Sorry, this will be cold— okay, um, one, two—\""
    "All of it, badly, one strip at a time: arms, legs, chest. Nobody comments on the result."
    hide bit_rena
    show bit_saki filming at vn_cast_slot
    bit_saki "\"Album: The Bit. Day one.\""
    hide bit_rena
    show bit_nono sorry at vn_cast_slot
    bit_nono "\"Sorry. It actually suits you.\""
    hide bit_nono
    hide bit_saki
    show bit_rena loud at vn_cast_slot
    bit_rena "\"There we go. Mori, stand up, do a turn. The group chat is going to lose its mind. The dare is complete!\""
    "Everyone laughs, and the dare is done, and you laugh too, two seconds late, and start pulling the wig off."
    show cg bit_phones onlayer cgl
    "Four phones are already up. Rena's for the group chat, Saki's for the album, Nono's because everyone else's is, and Miku's, held low at her hip, pointed at you, not filming anything, just pointed."
    hide bit_rena
    show bit_saki filming at vn_cast_slot
    bit_saki "\"Hold it. Don't take it off. The light's good. One more.\""
    hide cg onlayer cgl
    hide bit_rena
    jump bit_cmere

label bit_ch1_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bit_karaoke", pc="sheepish", pc_tag="bit_pc", cast=[("bit_miku", "flat")], cg="bit_walk_home")
    "Two in the morning, the last train gone, and Miku walks you to the taxi rank in silence with her hands in her jacket pockets, which she's never done. You've still got lipstick on. You can taste her and the lipstick and you can't tell which is which."
    bit_you "\"That was— it was a bit, right? Tonight. It was just a bit.\""
    bit_miku "\"Sure.\""
    "She puts you in a taxi and pays the driver through the window, which she's also never done, and walks off without looking back."
    "On the way home your phone goes forty times. The album has a name already. THE BIT. Forty-one pictures. You look at every one of them in the back of the taxi with your thumb over your mouth."
    hide cg onlayer cgl
    hide bit_miku
    call vn_night(14)
    jump bit_ch2

## ---- 2. Six Items ------------------------------------------------------------------------------
label bit_ch2:
    $ bit.chapter = 2
    $ vn_clock.day += 6
    $ bit_body(2)
    $ bit.fit = "kit"
    $ vn_enter(bg="bit_salon", pc="flustered", pc_tag="bit_pc", cast=[("bit_rena", "loud")], cg="bit_salon_day")
    "Friday you were twenty minutes early with all three things. The hair Nono waxed off hasn't grown back, anywhere. Nobody comments."
    "Saturday, the salon, sober, in daylight: nails done properly, your hair bleached and cut, ears pierced, your first heels. And a fitting for silicone breast forms at a shop counter, Rena discussing your size at volume."
    bit_rena "\"Your hands look fake.\""
    bit_you "\"Still a bloke under the base coat, aren't I.\""
    bit_rena "\"Only under the coat. Face next.\""
    bit_you "\"You want to plate me in chrome, just say it.\""
    hide bit_rena
    show bit_miku flat at vn_cast_slot
    bit_miku "\"More.\""
    "The assistant asks who the forms are for."
    hide bit_miku
    show bit_rena loud at vn_cast_slot
    bit_rena "\"It's a bit.\""
    "{color=#ffb0d8}Your skin's smooth. Your hands look slimmer under the technician's. Your face is softer in the salon mirror. Your chest is exactly as flat as it was; the forms go on over it.{/color}"
    hide cg onlayer cgl
    hide bit_rena
    $ vn_enter(bg="bit_flat", pc="flustered", pc_tag="bit_pc", cast=[("bit_miku", "flat")], cg="bit_flat_cage")
    "Then Miku's flat. She holds up a small steel cage."
    bit_miku "\"Sit. Chastity cage. I lock it.\""
    bit_you "\"No. That's not— that's not part of it. The list says six things, that's not one of them.\""
    jump bit_cage

label bit_ch2_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bit_flat", pc="flustered", pc_tag="bit_pc", cast=[], cg="bit_morning_cage")
    "You wake on Miku's sofa at noon under somebody's coat, and the first thing you feel is the cage. The second is everything else."
    "Miku's at the kitchen counter eating cereal out of the box. The key's on a ribbon round her neck. She looks at you over the box and holds up one finger and taps the key with it, twice, and goes back to her cereal."
    bit_you "\"I've got a seminar at two.\""
    show bit_miku flat at vn_cast_slot
    bit_miku "\"Go, then.\""
    "You go. You sit through the whole seminar with your legs crossed and your face hot and the cage under your jeans, and you don't take a word of it in, and when the lecturer asks you a question you say yes."
    call vn_night(14)
    jump bit_ch3

## ---- 3. Daylight -------------------------------------------------------------------------------
label bit_ch3:
    $ bit.chapter = 3
    $ vn_clock.day += 6
    $ bit_body(3)
    $ bit.fit = "kit"
    $ vn_enter(bg="bit_izakaya", pc="flustered", pc_tag="bit_pc", cast=[("bit_rena", "loud")], cg="bit_tights_split")
    "Friday night, the whole kit on in a place lit like daylight: an izakaya, one long table under one long tablecloth."
    "{color=#ffb0d8}You sit down and your tights split up both thighs. Nothing you own closes over them any more. Your ass and thighs have landed, hard, over the week.{/color}"
    bit_rena "\"Sit down, fuckwit. Let's see what splits first, those or the table. Fuck me! Is that your actual ass, or is there another one under there?\""
    hide bit_rena
    show bit_miku flat at vn_cast_slot
    bit_miku "\"Big ass. Like it?\""
    hide bit_miku
    show bit_rena loud at vn_cast_slot
    bit_rena "\"To our finest bit! Look at that ass. It ate his entire wardrobe and it's coming for the furniture next.\""
    "Rena comes back from the convenience store next door with the biggest tights they sell, extremely loud about the size."
    hide bit_miku
    show bit_rena loud at vn_cast_slot
    bit_rena "\"'XL. Tights for heroes!' Oh my god. That's you, hero ass. What's in yours, huh?\""
    "Then she goes through your bag."
    menu:
        "What you put in the bag that wasn't on the list."
        "The lube":
            $ bit.extra = "lube"
        "The spare panties":
            $ bit.extra = "panties"
    hide bit_miku
    show bit_rena loud at vn_cast_slot
    bit_rena "\"Who asked for this? He's packing a week's kit like an Olympic athlete. Ready for anything.\""
    bit_you "\"It's a bit.\""
    hide bit_rena
    show bit_saki filming at vn_cast_slot
    bit_saki "\"You want it now or after dessert?\""
    "Under the long tablecloth: Miku's hand and Nono's, up the new thighs and over the cage, unseen. Nobody at the next table looks over."
    hide bit_miku
    hide bit_saki
    show bit_rena loud at vn_cast_slot
    bit_rena "\"Can you get it on camera under there?\""
    hide bit_rena
    show bit_saki filming at vn_cast_slot
    bit_saki "\"Not without noise complaints. Four keys. Zero initiative.\""
    hide cg onlayer cgl
    hide bit_rena
    jump bit_cubicle

label bit_ch3_after:
    hide cg onlayer cgl
    $ vn_enter(bg="bit_izakaya", pc="flustered", pc_tag="bit_pc", cast=[("bit_miku", "flat")], cg="bit_table_hand")
    "Back at the table, the yakitori gone cold, the others pretending they didn't hear. You sit down very carefully next to Miku, and under the tablecloth her hand finds your thigh, and stays there, warm and heavy, and doesn't move for the rest of the night."
    "Rena reads the list out again, to the table, to the waiter, to a man at the next table who didn't ask. Nine items. You laugh at all of them, on time for once."
    call vn_night(11)
    jump bit_ch4

## ---- 4. No Bit ---------------------------------------------------------------------------------
label bit_ch4:
    $ bit.chapter = 4
    $ vn_clock.day += 6
    $ bit_body(3)
    $ bit.fit = "kit"
    $ vn_enter(bg="bit_cafe", pc="sheepish", pc_tag="bit_pc", cast=[("bit_nono", "sorry")], cg="bit_brunch")
    "Brunch. Daylight, sober, and no phones on the table for the first time since the karaoke box."
    bit_nono "\"We should... this is just us, okay? We'll stop. All of it. The wig, the nails, we delete the album. You go back to carrying the bags and nobody ever mentions it again. We mean it.\""
    hide bit_nono
    show bit_rena loud at vn_cast_slot
    bit_rena "\"No more kit, no fucking list, no Friday. We'll even eat the receipts.\""
    "Saki turns her phone face down. \"Say the word, I'll burn the whole account. Forever.\" Miku says nothing and doesn't move."
    "It's a completely genuine offer. There's no bit in it anywhere."
    bit_you "\"No— I mean— no. No, I don't— I don't want you to stop.\""
    "It comes out mangled, so you say it again, clearly, in front of all four of them."
    bit_you "\"No. Don't stop.\""
    $ bit.asked = True
    hide bit_nono
    show bit_rena loud at vn_cast_slot
    bit_rena "\"You don't get to take it back.\""
    "She means it. Nono crumples in relief. Saki whoops."
    hide bit_nono
    show bit_rena loud at vn_cast_slot
    bit_rena "\"The boys are at the flat above the bar. Kaito, Sho, Daichi. Yes or no?\""
    bit_you "\"Yes. Take me up there. Take me to the flat.\""
    hide bit_nono
    show bit_rena loud at vn_cast_slot
    bit_rena "\"Can someone get this fucking legend a drink for courage?\""
    hide cg onlayer cgl
    hide bit_nono
    $ vn_enter(bg="bit_cafe", pc="giddy", pc_tag="bit_pc", cast=[("bit_rena", "loud")], cg="bit_forms_shop")
    "On the way, at the shop counter, Rena holds up a bigger pair of forms, the next size up, in their plastic tray."
    ## BET THEY GROW's fork (the alternate route; owner, 2026-11-13)
    menu:
        "The bigger forms, on the glass."
        "Let them buy the bigger forms" (ending=True):
            "{color=#ffb0d8}They buy you the bigger forms. Bigger forms. Nothing grew: your chest is exactly as flat as it was, under silicone. Your hips have widened, your waist drawn in. A skirt, size S.{/color}"
            "Rena posts it to the group chat: {i}Bigger forms. Nothing grew.{/i} It's the funniest line of the day."
        "Push them back: bet they grow" (ending=True):
            $ bit.bet = True
            show cg bit_bet_counter onlayer cgl
            "You push the tray back across the glass with one finger."
            bit_you "\"Don't need them. Bet you they grow.\""
            "Rena laughs so hard the assistant comes over to see if she's alright. Then she gets her phone out, opens the pinned list, deletes {i}bigger forms{/i} from item ten, and types it in, out loud, letter by letter."
            bit_rena "\"Item ten. B. E. T. Bet: no forms.\""
            "{color=#ffb0d8}No forms, then. Your chest is exactly as flat as it was, bare under the cropped top. Your hips have widened, your waist drawn in. A skirt, size S.{/color}"
            "Rena posts it to the group chat: {i}Bet: no forms. She says they'll grow.{/i} It's the funniest line of the day. Miku reads it, and looks at your chest, and doesn't laugh."
    hide bit_rena
    jump bit_boys

label bit_ch4_after:
    hide cg onlayer cgl
    call vn_night(14)
    jump bit_ch5

## ---- 5. Key Deposit ----------------------------------------------------------------------------
label bit_ch5:
    $ bit.chapter = 5
    $ vn_clock.day += 6
    $ bit_body(5)
    $ bit.fit = "kit"
    $ vn_enter(bg="bit_karaoke", pc="giddy", pc_tag="bit_pc", cast=[("bit_kaito", "cheerful")], cg="bit_routine_box")
    "Week five, back at the karaoke box, and it's routine: the same room, the same drinks, the kit bag packed the night before with one thing over, a plug nobody put on the list."
    "{color=#ffb0d8}Thicker again. You can't sit in the booth the way you sat in it five weeks ago. Your voice has gone lighter, your mouth softer.{/color}"
    if bit.bet:
        $ bit.grown = 1
        "{color=#ffb0d8}And under the cropped top, where there hasn't been a form for a week, something. Two soft round breasts, puffy at the tips, real, and already a medium, the size Rena's always claimed she is. Nobody did anything. It was on the list.{/color}"
        "Rena posts it before you've finished taking your jacket off: {i}No forms. Something grew.{/i} Then she goes into the list and types WON after item ten."
    "The boys come as a matter of course. Nono has stopped apologising. The door's locked."
    show cg bit_key_jar onlayer cgl
    "On the table by the song book there's a jam jar with a ribbon in it, and on the ribbon, the key. Rena's idea. KEY DEPOSIT, on a sticky label in her handwriting. Anybody can open it. Nobody has, for five weeks."
    bit_kaito "\"Hana. Is that the key? To the—\""
    bit_you "\"It's a bit, Kaito.\""
    "It's the fifth time you've said it, and the first time you don't mean it at all, and everybody in the box hears the difference, and nobody says so."
    hide bit_kaito
    jump bit_key

label bit_ch5_after:
    hide cg onlayer cgl
    call vn_night(14)
    jump bit_ch6

## ---- 6. Fifth ----------------------------------------------------------------------------------
label bit_ch6:
    $ bit.chapter = 6
    $ vn_clock.day += 6
    $ bit_body(6)
    $ bit.fit = "kit"
    $ vn_enter(bg="bit_salon", pc="giddy", pc_tag="bit_pc", cast=[("bit_rena", "loud")], cg="bit_skirt_l")
    "That afternoon, a changing room in the shopping centre, and the skirt in size S that went on last month doesn't go past your thighs. Rena, outside the curtain, can hear you swearing."
    bit_rena "\"Is it the S? Is the S dead?\""
    bit_you "\"The S is dead.\""
    bit_rena "\"Saki! Camera! The S is dead!\""
    if bit.bet:
        $ bit.grown = 2
        "And the top in size S won't go past your chest. Not even close. You stand there with it stuck under your arms."
        bit_you "\"Both S's are dead, Rena.\""
        bit_rena "\"BOTH?\""
    "Saki gets a picture of you through the curtain gap with the skirt stuck halfway and your face red, and it's in the album before you've got it off."
    hide cg onlayer cgl
    hide bit_rena
    $ vn_enter(bg="bit_karaoke", pc="giddy", pc_tag="bit_pc", cast=[], cg="bit_drinks")
    "Week six. Nobody plans it any more. She arrives first, gets the room, orders for everyone at the counter, and has the drinks on the table before the rest are up the stairs. It's the only thing she's openly proud of."
    if bit.bet:
        "{color=#ffb0d8}The biggest change of the six weeks. The skirt in S won't go past her thighs. The booth isn't wide enough. And her chest isn't flat: huge and heavy and real now, the top in L and the L straining, and no forms since week four. It's the first thing everybody says when they walk in, and everybody's perfectly clear about why. It was on the list.{/color}"
    else:
        "{color=#ffb0d8}The biggest change of the six weeks. The skirt in S won't go past her thighs. The booth isn't wide enough. It's the first thing everybody says when they walk in. Her chest is flat under the same forms she's worn since week four, and everybody's perfectly clear about why.{/color}"
    hide cg onlayer cgl
    jump bit_finale
