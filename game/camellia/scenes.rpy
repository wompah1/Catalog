## camellia's scenes. UNIFORM: Kurosawa's floor rules and the rig are the force; nobody threatens, nobody hurts,
## they just don't stop when Rina says no. Ch 1-2 non-con; ch 3's "lock the cage" is the flip; 4-5 consensual.
## No organic change at any point: the rig, then the cage, as costume. The choice when she protests is what
## she says, never whether. Production rewrite (2026-11-13, twinetesting-c9): each scene run long.

## ---- ch 1: the rig, and "a girl on my floor knows what she's for" ---------------------------------
label cam_rig:
    $ cam_body(1)
    $ cam.fit = "rig"
    $ vn_enter(bg="cam_dressing", pc="mortified", pc_tag="cam_pc", cast=[("cam_kurosawa", "cool")], cg="cam_corset")
    "The dressing room behind the women's floor: soft light, powder, racks of colour, a long mirror ringed with bulbs. Kurosawa picks each piece of the rig like a surgeon laying out instruments."
    cam_kuro "\"Shirt off. Arms up.\""
    "Black satin, steel boning. She laces it slow from behind, knot by knot, her knee in the small of your back for the last pulls, until your ribs give and you can't slouch if you try."
    cam_you "\"I can't— {i}hah{/i}— I can't breathe in this—\""
    cam_kuro "\"You can. Shallower. Girls breathe from the top. You'll get used to it by the second hour.\""
    show cg cam_forms onlayer cgl
    "Two silicone forms, heavy and cold, into the pockets of a black bra she fastens on you herself, adjusting them with her palms like fruit on a stall. Then the tape, under them, round them, so they sit like they grew there."
    "Then the wig, thick scarlet, in two long low tails at your shoulders. Then powder, liner, lashes she glues on one at a time with her face close to yours and her breath smelling of smoke. A red mouth, drawn with a brush."
    show cg cam_mirror_first onlayer cgl
    "She turns you to the bulbs. A tall slim woman with red hair and a red mouth looks back, startled, and blinks your blink."
    "It's humiliating how well it works."
    cam_kuro "\"You're Rina now. One more thing before the floor. A girl on my floor knows what she's for.\""
    cam_you "\"What's that supposed to—\""
    show cg cam_knees onlayer cgl
    "Her hand on your shoulder, and the corset makes you go down straight-backed, like a doll folding. She unzips."
    menu:
        "On your knees in the corset."
        "Say no":
            $ cam.shout1 = "no"
            cam_you "\"No. No, that's not the job. I agreed to the floor, I didn't agree to—\""
        "Turn your face away":
            $ cam.shout1 = "away"
            "You turn your painted face to the wall. She turns it back with two fingers, unhurried."
            cam_you "\"Don't. Kurosawa, don't—\""
    cam_kuro "\"Uniform, Rina. Open.\""
    "She's huge, and she doesn't rush. Her hand on the back of your wig, holding it on as much as holding you. The red lipstick smearing down her length. The corset making every breath shallow, so you breathe through your nose, and the smell of her and the powder and the smoke."
    vn_sfx "{i}Shlp. Shlp. Shlp.{/i}"
    cam_you "\"{i}Mmh{/i}— {i}mmnh{/i}— {i}mmh{/i}—!\""
    cam_kuro "\"Look up. Always look up at them. That's what they pay for, the looking up.\""
    show cg cam_knees_look onlayer cgl
    "You look up. Lashes that aren't yours, a mouth that isn't yours, stretched round her, and her face above, cool and assessing, the way she looked at you across the desk."
    "And the worst thing: your own cock is straining under the skirt, untouched, and every slow stroke into your mouth pulls it tighter against the knickers."
    cam_you "\"{i}Mmph{/i}— no— {i}mmh{/i}— I'm not— {i}mmph{/i}—\""
    show cg cam_knees_peak onlayer cgl
    cam_you "\"{i}Mmmh{/i}— {i}MMHH{/i}—!\"" with vnfx("flash", "shake")
    "You come in your knickers, untouched, with her in your mouth, and she comes a moment later down your throat, holding the wig on with one hand."
    cam_kuro "\"Good. Fix your lip. Five minutes.\""
    show cg cam_lip_fix onlayer cgl
    "You fix your lip in the bulb-lit mirror with a brush that shakes, kneeling, because you can't get up yet, and the girl in the mirror fixes hers with you, and her mascara's run a little at one corner and her knickers are wet and she's due on the floor in four minutes."
    cam_kuro "\"The other corner. There. You'll learn to do it in the dark.\""
    "She leans in the doorway, smoking, watching you do it, the way you'd watch someone learn to tie a tie."
    cam_you "\"Do they all— is this what you do to all of them?\""
    cam_kuro "\"Every girl on my floor knows what she's for, Rina. Now you do. Three minutes.\""
    jump cam_ch1_floor

## ---- ch 2: the dohan. Miyamoto's "after-hours" -----------------------------------------------------
label cam_hotel:
    $ cam.fit = "dress"
    $ vn_enter(bg="cam_hotel", pc="mortified", pc_tag="cam_pc", cast=[("cam_miyamoto", "leer")], cg="cam_hotel_door")
    "A love hotel: red neon, chrome, a round bed, a mirror on the ceiling, a vending machine in the corner that sells things you don't want to look at. He shuts the door and turns the lock."
    cam_you "\"It's only dinner. That's the dohan. Saki said it's only dinner—\""
    cam_miya "\"Dinner was dinner. This is after-hours.\""
    if cam.order == "shochu":
        "The shochu's still in you, warm and stupid, and the room tilts when you turn."
    else:
        "The shochu he ordered for you sits sour in your stomach, and the room tilts when you turn."
    menu:
        "Miyamoto, and the locked door."
        "Push him off":
            $ cam.shout2 = "push"
            "You push his hands off your hips. He puts them back."
            cam_you "\"No. Stop. I'm going back to the club.\""
        "Tell him what's under the dress":
            $ cam.shout2 = "tell"
            cam_you "\"You don't want this. I'm not— there's nothing under here you want. I'm a man.\""
            cam_miya "\"I know what the women's floor is, sweetheart.\""
    show cg cam_hotel_bed onlayer cgl
    "He pushes you down on the round bed and shoves the skirt up round the corset, and pulls the bra down so the forms spill out, and fucks the silicone valley while you say no, panting into your face."
    cam_miya "\"Squeeze them. Go on. Squeeze them for me.\""
    cam_you "\"Get off— that's not— {i}stop{/i}—\""
    "Your own hands are pressing them together. You don't know when that happened."
    show cg cam_hotel_in onlayer cgl
    "Then he rolls you onto your front, a sachet of lube from the bowl by the bed, and his fingers, and then him, slow, into your ass, with his hand on the back of the red wig."
    cam_you "\"No— no— {i}hahh{/i}— take it out— {i}nnh{/i}— don't— don't stop— no— I mean STOP—\"" with vnfx("shake")
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "Above you, in the ceiling mirror, a red-haired girl in a black corset face-down on a round bed with a salaryman on top of her. Her skirt round her waist. Her mouth open. You watch her because you can't watch anything else."
    "Your cock is hard under you against the sheets. Every stroke drags it."
    show cg cam_hotel_peak onlayer cgl
    cam_you "\"{i}AHH{/i}— no— {i}please{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "He tips the taxi fare and a little extra onto the pillow, and pats the wig, and goes to the shower whistling."
    show cg cam_taxi onlayer cgl
    "The taxi back across the city at half past two, the fare paid, the driver not looking in the mirror, the neon going past in stripes across your knees."
    "You sit with your knickers in your bag and the wig crooked and Miyamoto's aftershave on your neck, and look out of the window at the love-hotel district going by, a whole street of rooms with ceiling mirrors, a whole street of girls in them."
    "Your phone buzzes. Saki. {i}How was dinner?{/i} And then, before you can answer: {i}Kurosawa's waiting up. Go in the back.{/i}"
    jump cam_ch2_cage

## ---- ch 2: the cage, and settling it over the dressing table --------------------------------------
label cam_cage:
    show cg cam_cage_fit onlayer cgl
    "Cool hands tuck you down into a steel-and-acrylic cage, cock and balls, a ring and a tube, and the padlock closes with a crisp click."
    vn_sfx "{i}Click.{/i}"
    $ cam_body(3)
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Chastity isn't punishment. It's the uniform. The girls on my floor all have a line. That's yours.\""
    cam_you "\"Take it off. I didn't agree to this. Take it off me.\""
    "She holds up the key between two fingers, so you can see it, and puts it in her waistcoat pocket, and pats the pocket."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"And now we settle it.\""
    show cg cam_table onlayer cgl
    "She walks you through to the dressing room by the wrist and bends you over the dressing table, the bulbs round the mirror blazing, your painted face right there in it, and the smeared lipstick from the hotel."
    menu:
        "The dressing table, and the mirror."
        "Grip the table and refuse":
            $ cam.shout2b = "grip"
            cam_you "\"I'm not doing this. I don't care what the uniform is. No.\""
        "Tell her to stop":
            $ cam.shout2b = "stop"
            cam_you "\"Stop. Kurosawa. Please stop.\""
    "She doesn't argue. She lifts the skirt, slicks herself, and sinks into you, slow, all of her, and makes you watch it in the mirror."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Eyes up. Watch.\""
    cam_you "\"{i}Ohh{/i}— no— it's so— {i}hahh{/i}— stop—\""
    show cg cam_table_cage onlayer cgl
    "The cage strains with nowhere to go. Every stroke presses on something inside that makes it leak, a thin clear string from the tip of the tube onto the dressing table, onto the powder puffs and the lash glue."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Look at you. Built for my floor.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    cam_you "\"I'm not— built for— {i}nnh{/i}— I'm not anything, I'm a host, I'm a—\""
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"You're the second on my board. In a fortnight. Hush.\""
    show cg cam_table_peak onlayer cgl
    cam_you "\"I'm not— {i}nnh{/i}— don't— don't stop— NO— {i}AHH{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You come through the cage, dripping onto the dressing table, with nothing touching it. She finishes inside you and fixes her cuffs, and hands you a tissue for the table, not for you."
    show cg cam_cage_mirror onlayer cgl
    "When she's gone you stay bent over the dressing table for a long time, looking at the girl in the mirror, and then you lift the skirt and look at the cage in the glass: steel and acrylic, a small padlock, and you, inside it, small and soft and leaking."
    "The key's in her waistcoat pocket. Her waistcoat's in her office. Her office is just down the corridor. You don't go."
    "You tidy the dressing table instead. You wipe it down. You put the powder puffs back in a row. It's the most uniform you've ever been."
    jump cam_ch2_after

## ---- ch 3: the desk. "Lock it" -------------------------------------------------------------------
label cam_desk:
    show cg cam_desk onlayer cgl
    "Kurosawa is round the desk before the word's finished. The jacket comes off at last, and the waistcoat, and the key falls out of the pocket onto the blotter between you and neither of you picks it up."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Say it again.\""
    if cam.real:
        cam_you "\"Make it real. Make it so I can't leave. Keep me.\""
    else:
        cam_you "\"Lock it. Keep it locked. Keep me.\""
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Hold them together.\""
    "You press the forms together for her and she slides between them, and you watch her lose her composure for the first time since you've known her: her mouth open, her hand braced on the desk, the cigarette burning down unnoticed in the ashtray."
    cam_you "\"There— yes— use them— {i}use me{/i}—\""
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Rina—\""
    show cg cam_desk_kiss onlayer cgl
    "She kisses you. She's never kissed you. Smoke and whisky and red lipstick, and her hand in the wig, and then she takes the wig off, gently, and puts it on the desk, and kisses you again with your own short hair under her fingers."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Both of you. I want both of you.\""
    show cg cam_desk_over onlayer cgl
    "Then over the desk, the papers going everywhere, the board's printouts and the bills and the folder with your name on it, and she takes you hard, and you push back onto her and beg for it, loud enough for the empty club to hear."
    vn_sfx "{i}Pap! Pap! Pap!{/i}"
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"No apologies, Rina. Not for this. You belong right here.\""
    cam_you "\"Harder— don't stop— the cage, it's— {i}ahh{/i}— it's leaking on your desk— don't stop—\""
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Let it.\""
    cam_you "\"{i}Yes{/i}— lock it— lock me in— {i}AHH{/i}— {i}KUROSAWA{/i}—!\"" with vnfx("flash", "shake")
    show cg cam_desk_after onlayer cgl
    "Afterwards you lie on her desk on the scattered papers with your wig off and your short hair a mess, and she sits in her chair with her shirt open and smokes and looks at you, and doesn't say anything for a whole cigarette."
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"Masaki used to sit there. On that corner. He'd tell me about the women he'd been with that night. I used to like it.\""
    cam_you "\"Do you want me to tell you?\""
    hide cam_miyamoto
    show cam_kurosawa cool at vn_cast_slot
    cam_kuro "\"No. I want you to stay.\""
    "She says it to the ashtray. You pretend you didn't hear how it came out, and she pretends she didn't say it, and the storm comes in at four."
    jump cam_ch3_after

## ---- ch 4: Domoto, number one's buy-out ------------------------------------------------------------
label cam_domoto_hotel:
    $ vn_enter(bg="cam_womens_floor", pc="bright", pc_tag="cam_pc", cast=[("cam_domoto", "hungry")], cg="cam_domoto_tape")
    if cam.name1 == "yours":
        cam_domoto "\"Number one girl, huh? My girl's number one. What do we win?\""
    else:
        cam_domoto "\"Number one girl, huh? Rina, number one. What do we win?\""
    cam_you "\"Whatever you buy.\""
    "His fingers find the tape where the forms meet skin. He's always wanted the artifice, the seams. He runs a thumb along the edge of it like a man reading Braille."
    cam_domoto "\"At least you get to take it off when the lights go down.\""
    menu:
        "Domoto's fingers on the tape."
        "\"Maybe I like that it doesn't come off.\"":
            $ cam.domoto = "stays"
            cam_you "\"Maybe I like that it doesn't come off.\""
            cam_domoto "\"That's so dirty.\""
        "\"It comes off. You'll never see it.\"":
            $ cam.domoto = "never"
            cam_you "\"It comes off. You'll never see it.\""
            cam_domoto "\"Buy-out, then. Now.\""
    hide cg onlayer cgl
    hide cam_domoto
    $ vn_enter(bg="cam_hotel", pc="bright", pc_tag="cam_pc", cast=[("cam_domoto", "hungry")], cg="cam_domoto_forms")
    "The love hotel, the red neon, the same round bed, the same ceiling mirror, and this time you lock the door yourself, and put the key on the vending machine where he can't reach it without walking past you."
    if cam.real:
        ## MAKE IT REAL's ch 4 hotel: the forms off for the first time
        show cg cam_real_domoto onlayer cgl
        "Then, for the first time, you peel the forms off yourself, in front of him, and the tape after them, slowly, and let him see what's under it: small and new and puffy and real, breathing, the way Saki said."
        cam_domoto "\"Those are— those aren't— Rina, are those {i}real{/i}?\""
        cam_you "\"Mine. Not bought. Grown. Be gentle with them, they're new.\""
        "He's very gentle with them, for about a minute, with his mouth. Then he fucks the little valley between them with his trousers round his knees, babbling, and you push them together round him with your palms and talk him through it, the way Saki taught you to talk a man through a second bottle."
        cam_domoto "\"Your real tits— oh fuck— your real fucking tits—\""
        cam_you "\"Mine. All mine. Like you. Faster.\""
    else:
        cam_you "\"Mess them up for me. I want to walk back on that floor sticky.\""
        "He fucks the forms with his trousers round his knees, babbling, and you rock your chest into every stroke and talk him through it, the way Saki taught you to talk a man through a second bottle."
        cam_domoto "\"Your fake tits— oh fuck— your fake fucking tits—\""
        cam_you "\"Mine. Bought and paid for. Like you. Faster.\""
    show cg cam_domoto_cage onlayer cgl
    "Then he lifts your skirt and finds the cage, and stops dead, and goes red to the ears, and you laugh at him, the three-note laugh, and turn over on the bed and show him the rest."
    if cam.domoto == "stays":
        cam_you "\"I told you. It doesn't come off. The key's in Kurosawa's waistcoat.\""
    else:
        cam_you "\"You'll never see it, I said. And here you are. Lucky you.\""
    cam_domoto "\"That's— that's the dirtiest thing I've ever—\""
    cam_you "\"Then fuck it.\""
    "He does. You watch yourself in the ceiling mirror: the red tails spread out on the sheet, the cage swinging, the forms bouncing, your own mouth open. You choose every second of it."
    show cg cam_domoto_peak onlayer cgl
    cam_you "\"Yes— all of it— all over— want them to see who had me— {i}ahh{/i}— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    if cam.real:
        "You walk back onto the floor with the forms back on over it, and it drying underneath on your own skin, and the whole room not knowing, and Domoto knowing."
    else:
        "You walk back onto the floor with it drying on the silicone and the whole room knowing."
    show cg cam_walk_back onlayer cgl
    "Back on the floor in the red dress, the forms sticky and the wig fixed and the cage swinging under the slit, and you walk the length of the room past every table, Saki's walk, slowly, so they can all see."
    "Saki watches you go by from her booth with her glass halfway to her mouth. Kurosawa watches from the bar with her arms folded. Men watch from every table, and two of them reach for their wallets before you're past."
    hide cam_domoto
    show cam_saki sly at vn_cast_slot
    cam_saki "\"Show-off.\""
    cam_you "\"Number one.\""
    jump cam_ch4_after

## ---- ch 5, Sign: one year (the book's) -------------------------------------------------------------
label cam_sign:
    $ vn_enter(bg="cam_office", pc="bright", pc_tag="cam_pc", cast=[("cam_kurosawa", "raw")], cg="cam_contract")
    "You put Ichinose's card on her desk first, face up, so she can see whose it is. She looks at it for a long time without touching it."
    cam_you "\"I want a contract. One year, on paper. My name on the board. Signed.\""
    cam_kuro "\"We don't do contracts on the women's floor. You want to be caged that badly?\""
    cam_you "\"Yes. I want it written down. I want you to keep me.\""
    "For a moment the mask breaks."
    cam_kuro "\"You could have any life in the city. Even as Ryo. Look at that card. I'd give you a reference. Nobody should have to lock themselves in—\""
    cam_you "\"I want this. Here. With you.\""
    "A folder thick as a book, the Camellia's seal on every page like a marriage contract. You sign before she's finished saying read it. Rina. And under it, smaller, Ryo, because she asked for both."
    show cg cam_contract_desk onlayer cgl
    if cam.real:
        "And then the desk again, her hands under the forms, on what's under them now, her cock between them, the contract under your back, the ink still wet, smudging."
    else:
        "And then the desk again, her hands under the forms, her cock between them, the contract under your back, the ink still wet, smudging."
    cam_kuro "\"Mine. Mine. Mine.\""
    cam_you "\"Yours— {i}yes{/i}— one year— every night— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg cam_contract_card onlayer cgl
    "Afterwards she picks up Ichinose's card, and looks at it, and tears it in half, and in half again, and drops the pieces in the ashtray, and lights them with her cigarette."
    cam_kuro "\"One year. Every night. Like this.\""
    cam_you "\"One year.\""
    hide cg onlayer cgl
    $ vn_enter(bg="cam_womens_floor", pc="bright", pc_tag="cam_pc", cast=[("cam_saki", "sly")], cg="cam_contract_floor")
    "The board, the next night: RINA at the top in Kurosawa's own hand, and beside it, for the first time on the women's floor, a small printed card pinned under the name: CONTRACTED, ONE YEAR."
    cam_saki "\"Contracted. On the women's floor. She's never.\""
    cam_you "\"She has now.\""
    cam_saki "\"Then I'd better get my number back before your year's out, hadn't I.\""
    "She clinks her glass on yours, her way, wrist turned, and you clink back, and across the floor Domoto's at his table at half-past exactly, waving, and in the back office the light is on."
    hide cg onlayer cgl
    hide cam_saki
    show screen cam_board(5)
    "The board, every night after."
    hide screen cam_board
    if cam.real:
        call cam_real_year
        $ vn_feat("Made Real")
    $ vn_feat("Number One Girl")
    jump cam_route_return

## ---- ch 5, Take: the men's floor (new writing) -----------------------------------------------------
label cam_take:
    $ cam_pc_name = "Ryo"
    $ cam.fit = "suit"
    $ vn_enter(bg="cam_office", pc="poised", pc_tag="cam_pc", cast=[("cam_kurosawa", "cool")], cg="cam_key")
    if cam.real:
        "You go to the office anyway, to say it to her face, in Ryo's suit, which hangs off you now in odd places and won't sit flat across the chest any more, over the binder. You owe her that much."
    else:
        "You go to the office anyway, to say it to her face, in Ryo's suit, which hangs off you now in odd places. You owe her that much."
    cam_you "\"Ichinose. The Sanctuary. The men's floor, as Ryo.\""
    "She doesn't look up. She opens the drawer, takes out the small key and turns it in the cage's lock herself, without a word, the way she put it on. Then she sets the key down on the desk between you."
    cam_kuro "\"Every one of them.\""
    "That's all she says. She lights a cigarette off the last one and turns her chair to the window."
    hide cg onlayer cgl
    hide cam_kurosawa
    $ vn_enter(bg="cam_mens_floor", pc="poised", pc_tag="cam_pc", cast=[], cg="cam_sanctuary")
    show screen cam_board(6)
    "The Sanctuary's men's floor, three months on. Your name at the top, as yourself, in gold. Double the money. Women pick you every night; you know exactly what they want, because you've been it."
    hide screen cam_board
    "Nobody looks twice at you when you walk to the train. That was the point. You tell yourself that was the point."
    if cam.real:
        "The blister packs are still in your bathroom cabinet, a whole year of them, and you still take one every night with the last glass of water. You couldn't tell anyone why. Under the shirt, under the binder, it's still growing, slowly, the way the man on the fourth floor said, and nobody at the Sanctuary will ever see it."
    show cg cam_window onlayer cgl
    "Some nights you pass the Camellia and the light's on in the back office, and you stand across the street for a cigarette you don't smoke, and you don't go in."
    hide cg onlayer cgl
    $ vn_feat("Nobody Again")
    jump cam_route_return
