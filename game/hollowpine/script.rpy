## hollowpine's days: each one is the printout, the desk, the treatment (scenes.rpy), what it changes,
## and a gag. Six linear days at Hollow Pine. The card is the ladder; nobody lies to him.

## ---- DAY 1: Ellie, Party of Six ----------------------------------------------------------------
label hol_arrival:
    $ hol.fit = "street"
    $ vn_enter(bg="hol_carpark", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "warm")], cg="hol_drive_up")
    "Casey drives the whole way up with one hand on the wheel and the other out of the window, singing along to something you'd never admit you know the words to."
    "You've been in love with her for four years. She asked you on the girls' trip, and you said yes before she'd finished the sentence."
    hol_casey "\"You're going to love it. Honestly. It's very hands-on.\""
    hol_you "\"I love hands-on.\""
    "You have no idea what you mean by that. She laughs anyway, and you'd drive another four hours for it."
    hol_gate "\"Name, please?\""
    hol_casey "\"Reyner. Ellie, party of six.\""
    hol_gate "\"You're expected. Please proceed.\""
    hide cg onlayer cgl
    $ vn_pass(30)
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "warm")], cg="hol_desk_ellie")
    "Hollow Pine is all pale wood and steam and soft music, and a sign over the desk that says, in tasteful brass, WOMEN ONLY."
    "The woman at the desk looks up, and then at you, and then at Casey."
    hol_desk "\"Reservation for Reyner, Ellie, party of six?\""
    "She scans you as neutrally as groceries at a till. You open your mouth."
    hol_casey "\"That's us. Vance goes by Ellie this week, just for the record. All the paperwork's right.\""
    "Nobody blinks. Five women and you, and nobody at the desk so much as lifts an eyebrow."
    hol_desk "\"Perfect. Ellie, welcome to Hollow Pine. Ma'am.\""
    show hol_pc puzzled
    hol_you "\"I'm actually—\""
    "Everybody laughs, the desk and Casey and the three women behind you with the suitcases. It's a nice laugh. You let it go."
    hide cg onlayer cgl
    show cg hol_photo_wall onlayer cgl
    "By reception there's a wall of photographs: every group, every year, back and back. You glance at it on the way to the lockers. Nice frames."
    "You don't count them."
    hide cg onlayer cgl
    show cg hol_locker onlayer cgl
    "House rule: street clothes in a locker for the week, robes only. You fold your jeans and your hoodie into a neat square and post the key back through the slot."
    hol_desk "\"We'll launder everything before you leave, so you can pack cleanly.\""
    $ hol.fit = "robe"
    "The robe's enormous on you. Everything at Hollow Pine is a bit enormous on you."
    show cg hol_locker_tease onlayer cgl
    "Delaney's at the next locker, changing, with no particular interest in covering up. She's very tall and very naked and there's a great deal of her, all of it relaxed, including the part of her that makes you look at the floor."
    hide hol_casey
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"Eyes up, Ellie. Or don't. Nobody minds here.\""
    hol_you "\"I wasn't— I was looking at the— the tiles. Lovely tiles.\""
    hide hol_casey
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"They're grey.\""
    hol_you "\"Lovely grey.\""
    "She laughs, and pats you on the head, and goes out to the pool with her towel over her shoulder like a cape."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_tub", pc="flustered", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_tub_bench")
    "Then the hot tub, before dinner, with all five of them. You meet everybody properly up to your chin in water."
    "Delaney, who's very tall, and takes up most of one side, and doesn't seem to notice she's doing it."
    "June, who reads a magazine in the hot tub and keeps it dry."
    "Nadine, who asks what size robe you are and doesn't wait for the answer. Robin, who smiles at you like she knows something nice."
    menu:
        "Robin asks what you like to be called."
        "\"Elliot. Ellie's just the booking.\"":
            $ hol.name1 = "elliot"
            hol_you "\"Elliot. Ellie's just the booking. It's a whole mix-up, it's a funny story actually—\""
            hide hol_delaney
            show hol_robin kind at vn_cast_slot
            hol_robin "\"Ellie's fine here. Everyone's Ellie here, for a week.\""
        "\"Ellie's fine.\"":
            $ hol.name1 = "ellie"
            hol_you "\"Ellie's fine. For the week. When in Rome.\""
            hide hol_delaney
            show hol_robin kind at vn_cast_slot
            hol_robin "\"That's the spirit.\""
    hide hol_robin
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"You're smaller than I thought.\""
    "The bench is too high for you. Your toes don't reach the floor. Delaney stands up to get the towels and your eyes come level with her collarbone, and she reaches over your head for them like you're a shelf."
    hide cg onlayer cgl
    $ vn_until(20)
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "pleased")], cg="hol_toast")
    "Dinner. Candles. Casey raises her glass."
    hol_casey "\"Six on the reservation, six coming home.\""
    "Everybody drinks, and the chorus rolls round the table like an old routine: \"No casualties!\" \"Everyone makes checkout!\" \"No oopsies this year!\""
    "You drink. It's a joke. You laugh at it, because everybody does."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_room", pc="earnest", pc_tag="hol_pc", cast=[], cg="hol_card_night")
    show screen hol_card
    "On your nightstand there's a treatment card, printed on heavy cream paper. You read it cover to cover, sitting up in the enormous bed."
    "Silt Soak. Lymphatic Drainage. Hydration Therapy. Live Enzyme Infusion. Deep Conditioning. Postural Correction."
    "You don't understand any of it. You read it twice more, so you don't look stupid tomorrow."
    hide screen hol_card
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Treatment room in fifteen, Ellie! Better robe up.\""
    hol_you "\"You signed me up already?\""
    hol_casey "\"You know I handle it. Everyone soaks, everyone drains.\""
    hide hol_casey
    $ vn_clock = VNState(day=1, hour=21, minute=0)
    $ hol_book(2)
    jump hol_drainage

label hol_day_one_after:
    $ hol_body(2)
    $ vn_enter(bg="hol_room", pc="flustered", pc_tag="hol_pc", cast=[], cg="hol_smooth")
    "{color=#9fe3cf}By the time you get back to your room your legs feel strange in the robe. You look. They're bare. Smooth. Not a hair, anywhere: your shins, your arms, your chest, all of it, gone in an evening.{/color}"
    hol_you "\"Huh.\""
    "It'll be the mineral content. The leaflet said the silt was very high in minerals."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_tub", pc="flustered", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_tub_smooth")
    "In the hot tub later, everyone notices at once. Nadine runs a hand down your shin under the water and says \"ooh\" like she's testing a fabric."
    hol_delaney "\"Softer, smoother. You're going to break hearts in the locker room, Ellie.\""
    hol_you "\"The minerals here must be some kind of European secret.\""
    hol_delaney "\"Go with it. You want the good results, right?\""
    hol_you "\"Of course. If the protocol says smooth, I'll be the smoothest one here.\""
    hide hol_delaney
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[], cg="hol_upgrade_1")
    "On the way past the desk you stop and ask whether there's a better package. There is. It's an extended package. It's better value."
    menu:
        "The extended package."
        "Book it, it's better value":
            $ hol.up1 = "value"
            hol_you "\"I'll take the extended one, please. It's better value.\""
        "Ask what's in it, then book it":
            $ hol.up1 = "asked"
            hol_you "\"What's in the extended one?\""
            hol_desk "\"More of everything, ma'am.\""
            hol_you "\"Great. Yes. That one.\""
    $ hol.upgrades += 1
    hol_desk "\"That's wonderful, Ellie, and easily arranged. Extra hydration therapy, postural correction, daily deep conditioning. Premier rates on absorption.\""
    "You sign with a flourish. Ellie. It's easier. It feels official, even exciting."
    hol_desk "\"Welcome to the full programme.\""
    hide cg onlayer cgl
    call vn_night(8)
    jump hol_day_two

## ---- DAY 2: Hydration Therapy ------------------------------------------------------------------
label hol_day_two:
    $ hol.fit = "robe"
    $ vn_enter(bg="hol_dining", pc="puzzled", pc_tag="hol_pc", cast=[("hol_june", "reading")], cg="hol_printout_2")
    "A printout comes under your door at breakfast. You bring it down to the table, and June takes it out of your hand before you've sat down, and reads it aloud."
    show screen hol_printout(2)
    hol_june "\"Absorption: low. Retention: low. Note: guest is enthusiastic. Recommend hydration.\""
    hide screen hol_printout
    hol_june "\"Absorption rate, Ellie. Tut tut. You're letting the pack down.\""
    menu:
        "Low."
        "Argue with it":
            $ hol.print2 = "argue"
            hol_you "\"Low? I did the whole thing. I did all of it. How is that low?\""
            hol_june "\"You were very enthusiastic.\""
        "Ask how to improve it":
            $ hol.print2 = "improve"
            hol_you "\"How do I get it up? The absorption. Not— the number.\""
            hol_june "\"Ask the desk.\""
    if hol.name1 == "elliot":
        hol_june "\"And it's still got you down as Ellie, Elliot. The printer doesn't do mix-ups.\""
    show hol_robin kind at vn_cast_slot
    show cg hol_robin_ask onlayer cgl
    hol_robin "\"Some people adjust faster, that's all. Did they give you the leaflet, though? The one about what's actually in it?\""
    "You nod. You read the whole card twice. She lets it go."
    hide hol_robin
    hide hol_june
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Different baseline, Ellie. June just wants someone else to win this year's basket. Hydration therapy's good for that, I heard. It's all on the menu.\""
    "You go and ask the desk."
    hol_desk "\"Absolutely, that's our most effective protocol. Standard is once daily, but extended-package guests benefit from increased frequency. Three times daily is recommended. Oral administration only, of course, to ensure maximum enzyme delivery.\""
    show cg hol_consent onlayer cgl
    "The consent sheet says it too, in more ornate language: {i}Enzyme administration, high-volume, directed oral uptake, as per guest protocol.{/i} You sign for morning, afternoon and evening, proud of your proactivity."
    $ hol_book(3)
    jump hol_hydration

label hol_day_two_after:
    $ hol_body(3)
    $ vn_enter(bg="hol_changing", pc="flustered", pc_tag="hol_pc", cast=[("hol_june", "dry")], cg="hol_changing_room")
    "{color=#9fe3cf}In the changing room your skin's gone soft. Not just smooth: soft, like a peach. When you say \"oh\" at it, your voice comes out lighter than it went in, and your robe sits differently on your hips.{/color}"
    "Delaney doesn't cover up. She never covers up. You look, and keep looking, and walk into the bench."
    hol_june "\"Noticing changes is normal. The enzyme's designed for elastin uptake. Don't worry if things shift. That's all part of the programme.\""
    hol_you "\"Is this why my voice feels weird?\""
    hol_june "\"Could be. Usually that's hydration. Maybe a touch of conversion. You'll want to keep up the doses.\""
    hol_you "\"Right. Yes. Obviously.\""
    "You accept this. It's a resort. They'd know."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_nadine", "smile")], cg="hol_lunch_nadine")
    "Over lunch you explain the enzyme's benefits for skin elasticity to Nadine, at some length, with your hands."
    hol_nadine "\"You've really read up on it. So that's why your legs look so soft. It's working.\""
    hol_you "\"I read the whole card. Three times.\""
    hide cg onlayer cgl
    show hol_robin kind at vn_cast_slot
    hol_robin "\"Ellie. Have you read what the enzyme is?\""
    hol_you "\"Yes. It's on the card.\""
    "She looks at you for a moment. Then she smiles, and lets it go."
    hide hol_robin
    $ vn_until(20)
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "amused")], cg="hol_dinner_fish")
    "Dinner, and the restaurant does do the sea bass, with capers, and Delaney picks every caper off and lines them up round the rim of her plate like a clock."
    hol_delaney "\"How's the throat, Ellie?\""
    hol_you "\"Hydrated.\""
    "It comes out higher than you meant. Everybody hears it. Nobody says anything, except June, who writes something on the back of her napkin."
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"Voice resonance. Early. I'll mention it to the desk.\""
    hol_you "\"Is that good?\""
    hide hol_delaney
    show hol_june reading at vn_cast_slot
    hol_june "\"Everything's good here, Ellie.\""
    "You eat all your capers, and Delaney's, to show willing. Casey laughs at you across the candles, and you'd do all three sessions again for it. You would. You tell yourself you would."
    hide cg onlayer cgl
    hide hol_delaney
    call vn_night(8)
    jump hol_day_three

## ---- DAY 3: Live Enzyme Infusion ---------------------------------------------------------------
label hol_day_three:
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_june", "reading")], cg="hol_printout_3")
    show screen hol_printout(3)
    hol_june "\"Absorption: improving. Retention: fair. Note: oral route is inefficient. Recommend infusion.\""
    hide screen hol_printout
    hol_june "\"Improving! You'll have a six in every column before the week's up. Don't go stealing the metrics prize from us veterans.\""
    hide hol_june
    show hol_casey warm at vn_cast_slot
    hol_casey "\"Not a race.\""
    show hol_delaney idle at vn_cast_slot
    hol_delaney "\"The real race is whether hydrating that much finally gives you a real ass.\""
    hide hol_delaney
    $ vn_enter(bg="hol_desk", pc="puzzled", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg="hol_eyeline")
    "Delaney's at the desk ahead of you. When you come up beside her your eyes land just under her collarbone, which is wrong; they landed on it on Saturday."
    hol_you "\"Were these chairs lower yesterday? I swear I used to fit under your chin.\""
    hol_delaney "\"Probably the table. Or you're shrinking. You should ask about it at the desk.\""
    hol_desk "\"Oral route is popular, but not optimal for full enzyme uptake. Greater bioavailability is achieved with internal application.\""
    show cg hol_leaflet onlayer cgl
    "A leaflet from a perspex stand: LIVE ENZYME INFUSION, in a calm seafoam font, and a diagram. You read the diagram six times, tracing the tidy arrow from intake to diffusion. You understand that it's a diagram."
    hol_desk "\"Technician application. Would you like to select from your group, or take whom we assign? Lubrication is provided. Rest at least ten minutes after infusion to maximise uptake.\""
    hol_you "\"Delaney's been extremely helpful. That route, please.\""
    hide cg onlayer cgl
    menu:
        "Internal application."
        "Book one infusion":
            $ hol.book3 = "one"
            hol_you "\"Just the one, please. To start.\""
        "Book one, ask about a discount":
            $ hol.book3 = "discount"
            hol_you "\"One. Is there a discount if I book more later?\""
            hol_desk "\"There's always more later, ma'am.\""
    $ hol_book(4)
    jump hol_infusion

label hol_day_three_after:
    $ hol_body(4)
    $ vn_enter(bg="hol_pool", pc="flustered", pc_tag="hol_pc", cast=[("hol_nadine", "smile")], cg="hol_pool_sell")
    "{color=#9fe3cf}Your robe won't close at the back any more. Your arse has arrived: round, soft, high, and your thighs press together all the way up. Your cock looks smaller in the steam. Water retention, obviously.{/color}"
    "At the pool you corner Nadine and recommend the infusion to her. Unprompted. At length. You draw her the diagram on a napkin."
    menu:
        "Selling Nadine on the infusion."
        "Draw her the diagram":
            $ hol.sell3 = "diagram"
            "You draw her the diagram on a napkin with the hotel pen, intake, arrow, diffusion, and label it, and underline the label."
            hol_you "\"Nadine, you have to try the live enzyme infusion. The absorption is insane. Internal application, see, here, the uptake is immediate and the results are— the results are {i}visible.{/i}\""
        "Just show her":
            $ hol.sell3 = "show"
            hol_you "\"Nadine, you have to try the live enzyme infusion. The absorption is insane. The internal application, there's a diagram, the uptake is immediate and the results are—\" You slap your own arse for emphasis. \"I mean, {i}look!{/i}\""
    hol_nadine "\"I'll take it under advisement, curve girl.\""
    hide cg onlayer cgl
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[("hol_robin", "worried")], cg="hol_upgrade_3")
    "On the way to dinner you stop at the desk and upgrade again: full scheduled infusions, just to ensure consistency with group protocol."
    hol_desk "\"You're already cleared for seven a week. Shall I add the double slot?\""
    $ hol.upgrades += 1
    hol_robin "\"Ellie, can I ask... have you really read what the enzyme is?\""
    hol_you "\"Cover to cover. The diagram's super clear. Internal route, bioavailability, optimised uptake. I'm all in, Robin.\""
    hol_robin "\"I believe you.\""
    "You have read it. You didn't understand it. She lets it go."
    hide hol_robin
    $ vn_until(20)
    $ vn_enter(bg="hol_dining", pc="flustered", pc_tag="hol_pc", cast=[("hol_robin", "kind")], cg="hol_lanterns")
    "The place on the square with the lanterns, at eight, in the private room. You sit on two cushions, because one isn't comfortable any more, for reasons you're attributing to the hot tub's jets."
    "Robin sits next to you. She's quiet, mostly. She cuts up the aubergine for both of you without asking."
    hol_you "\"You came here before, didn't you? Casey said. A few years back.\""
    hol_robin "\"Three years ago. I was the new one.\""
    hol_you "\"Did you like it?\""
    "She thinks about it for a long time, with her fork in the air."
    hol_robin "\"I came back.\""
    "She says it like that's an answer. You nod like it's an answer. Across the table Casey raises her glass, and the chorus goes round again, {i}no casualties, everyone makes checkout,{/i} and Robin drinks to it with everybody else, looking at you over the rim."
    hide cg onlayer cgl
    hide hol_robin
    call vn_night(8)
    jump hol_day_four

## ---- DAY 4: Deep Conditioning ------------------------------------------------------------------
label hol_day_four:
    $ vn_enter(bg="hol_room", pc="puzzled", pc_tag="hol_pc", cast=[("hol_nadine", "brisk")], cg="hol_nadine_clothes")
    show screen hol_printout(4)
    "{i}Absorption: very good. Retention: poor. Note: guest is leaking. Recommend conditioning.{/i} You read it yourself this time, sitting on the edge of the bed, while Nadine holds things up against you."
    hide screen hol_printout
    "And a fresh line under {i}metrics to watch{/i}: Chest development (initial). Further growth not included in current package."
    "Nothing you brought fits. Nothing of theirs fits either. So Nadine has been buying you things, from the resort shop, practical and generous, and you're dressed entirely by her now and nobody's asked you anything."
    menu:
        "What Nadine's holding up."
        "The soft wrap dress":
            $ hol.wear4 = "wrap"
            "A soft wrap dress that ties at the side. It's the only thing that goes over your hips."
        "The leggings and the long jumper":
            $ hol.wear4 = "leggings"
            "Leggings and a long jumper that comes to mid-thigh. The leggings are a fight. Nadine wins it."
    $ hol.fit = "nadine"
    hol_nadine "\"There. You look lovely.\""
    hide cg onlayer cgl
    $ vn_enter(bg="hol_desk", pc="flustered", pc_tag="hol_pc", cast=[("hol_nadine", "smile")], cg="hol_shop")
    "Then the resort shop, off the lobby, because Nadine says one outfit is a crisis and two is a wardrobe. She holds things up against you and puts most of them back."
    hol_nadine "\"Not that. Not that. That, if you want people to walk into doors.\""
    hol_you "\"I don't want people to walk into doors.\""
    hol_nadine "\"You will anyway. Arms up.\""
    "A bralette, because June says the chest is a metric now and metrics need support. Two pairs of shorts in a size you've never been. A soft cardigan that falls off one shoulder however you wear it. She signs them all to her room."
    hol_you "\"Nadine, you can't buy me all this—\""
    hol_nadine "\"I'm not. The package is. It's on the card, apparently. Clothing allowance.\""
    "You check. It is. In small print, under Postural Correction: {i}garments as required.{/i}"
    hide cg onlayer cgl
    hide hol_nadine
    show hol_june reading at vn_cast_slot
    hol_june "\"Good morning, chest.\""
    "Deep conditioning is twice daily now, slotted between meals like appointments: morning and evening. Retention improves results, the leaflet says. You're keeping it in. You're being diligent."
    show hol_delaney amused at vn_cast_slot
    hol_delaney "\"You are absolutely the only person I have ever seen read the protocol sheet all the way through and then call out retention as a win.\""
    hide hol_delaney
    hide hol_june
    show hol_nadine brisk at vn_cast_slot
    hol_nadine "\"Honestly, it's impressive. Most of us just let the enzyme handle things. You're practically on the platinum tier.\""
    hide hol_delaney
    $ hol_book(5)
    jump hol_conditioning

label hol_day_four_after:
    $ hol_body(5)
    $ hol.fit = "nude"
    $ vn_enter(bg="hol_room", pc="puzzled", pc_tag="hol_pc", cast=[], cg="hol_chest")
    "{color=#9fe3cf}In the mirror your chest has come up. Two small soft swells, puffy at the tips, there when you weren't looking. Your cock's smaller again, small and neat. You wait for the chest to do more. It doesn't.{/color}"
    hide cg onlayer cgl
    $ hol.fit = "nadine"
    $ vn_enter(bg="hol_desk", pc="puzzled", pc_tag="hol_pc", cast=[("hol_delaney", "idle")], cg=None)  # ff 3:12 am: no picture, desk-sudoku failed 4 draws (SCENES.md hollowpine v6)
    "The woman on the desk tonight has blue nails and is halfway through a sudoku. You complain, hushed, that your chest has plateaued."
    hol_desk "\"For full chest development you'll want one of the Expansion Packages. Deluxe, or Contour Plus. Your current package maximises lower-body shaping, smoothness, thigh and ass mass, and small chest definition. You're already at the upper end of that spec. Chest upgrades are for a different experience.\""
    hol_you "\"Do I need to upgrade for... group consistency?\""
    hol_desk "\"Not at all. Your metrics are right on track for your booking category. Your performance is top decile.\""
    "Your fingers hover over the pen."
    ## THE DELUXE's fork (the alternate route; owner, 2026-11-13): deluxe.rpy
    menu:
        "The pen, in its tray."
        "Book the Deluxe" (ending=True):
            jump hol_dx_book
        "Stay on the current protocol" (ending=True):
            pass
    "For the first time all week, you set it back in the tray."
    hol_you "\"Okay. I think I'll just stay on the current protocol. See how it resolves.\""
    hol_desk "\"Of course. No pressure.\""
    "You don't book it. You don't think about why. It's the first thing all week you haven't booked, and nobody says a word about it."
    show cg hol_marker onlayer cgl
    "Back at the table Nadine hands you a new pair of shorts, \"for when these split up the side, probably before lunch,\" and June uncaps a marker and draws a dot on your bralette. \"Chest status: Ellie's Deluxe.\""
    "Delaney's beside you. Your eyes are on the top of her sternum now."
    hide hol_delaney
    show cg hol_photo_wall onlayer cgl
    "You walk past the photo wall on the way out. You don't count."
    hide cg onlayer cgl
    call vn_night(8)
    jump hol_day_five

## ---- DAY 5: Itemized ---------------------------------------------------------------------------
label hol_day_five:
    $ hol.fit = "nadine"
    if hol.deluxe:
        call hol_dx_wake
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_nadine", "brisk")], cg="hol_shorts_5")
    show screen hol_printout(5)
    if hol.deluxe:
        "{i}Absorption: excellent. Retention: excellent. Upper contour: responding very well. Note: posture still guarded.{/i}"
    else:
        "{i}Absorption: excellent. Retention: excellent. Note: posture still guarded.{/i}"
    hide screen hol_printout
    "At breakfast Nadine clucks over your shorts. \"You're one breakfast away from indecent exposure.\" Robin sets down a glass of juice laced with enzyme, and you take it in both hands."
    if hol.deluxe:
        "June leans across with her marker and draws a second dot on your cardigan, beside the first. She doesn't say anything. She doesn't need to."
        call hol_dx_shop
    "You've decided. Today you're going to tell Casey. Four years. You've practised it in the hot tub."
    $ vn_enter(bg="hol_room", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "warm")], cg="hol_casey_door")
    "You knock on her door, and she opens it in her robe, with her hair wet, and smiles at you, and you open your mouth."
    menu:
        "Casey, in the doorway."
        "Tell her all four years":
            $ hol.confess5 = "years"
            "You say it, all of it, the whole four years of it, in your new light voice: the first lecture, the bus, the night of her birthday, every time you didn't say it."
        "Just ask her out":
            $ hol.confess5 = "ask"
            hol_you "\"Casey. Will you go out with me? Properly. A date. When we're home. I've wanted to ask for— for a while.\""
            "It comes out in your new light voice, all in one go, and you stand there in Nadine's shorts and wait."
    jump hol_correction

label hol_day_five_after:
    $ hol_body(6)
    if hol.deluxe:
        $ hol.grown = 2
    $ vn_enter(bg="hol_room", pc="puzzled", pc_tag="hol_pc", cast=[], cg="hol_statement")
    "The checkout paperwork comes early. An itemized statement, on the heavy cream paper, every treatment under its wellness name with the price written beside it in words."
    "{i}Hand extraction. Oral supplement, three sessions, technician D. Cobb. Partnered infusion. Conditioning, with emollient. Correctional therapy.{/i} You run your thumb down the frank column and stop, and count backwards."
    if hol.deluxe:
        "Six signatures. Ellie, Ellie, Ellie, Ellie, Ellie, Ellie. Four of them are upgrades you asked for yourself."
        "And one line on its own at the bottom, under a rule: {i}Expansion Package: Deluxe. Upper contour. Volume.{/i} You read {i}volume{/i} again, and this time you read it the way the desk said it."
        "{color=#9fe3cf}Somewhere in the middle of the correction your chest went up again. You can feel it every time you breathe: large now, full and heavy, sitting out over your ribs, and the bra Nadine fitted this morning is already the wrong size.{/color}"
    else:
        "Five signatures. Ellie, Ellie, Ellie, Ellie, Ellie. Three of them are upgrades you asked for yourself."
    hol_you "\"Is it itemized because the enzyme therapy's billed separately?\""
    "It is. It says so at the bottom: different line, different rate."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_desk", pc="puzzled", pc_tag="hol_pc", cast=[], cg="hol_photo_count")
    "You go down to reception and look at the photo wall, and this time you count."
    "Six. Six. Six. Every group, every year, going back and back. Six, and always one small one in front."
    "Three years ago, front and centre, short, beaming: Robin."
    "And June's voice from the first night, the whole table clinking. {i}No casualties. Everyone makes checkout. No oopsies this year.{/i}"
    hide cg onlayer cgl
    $ vn_enter(bg="hol_dining", pc="puzzled", pc_tag="hol_pc", cast=[("hol_casey", "pleased")], cg="hol_toast_hear")
    hol_casey "\"Six on the reservation, six coming home.\""
    "Everybody drinks. This time you hear it."
    hide hol_casey
    $ vn_enter(bg="hol_carpark", pc="puzzled", pc_tag="hol_pc", cast=[], cg="hol_carpark_walk")
    "You put your glass down and walk out through the lobby and the front doors and into the car park."
    "Nobody stops you. Nobody follows you. Nobody raises their voice. The door's open the whole time; it was always open."
    if hol.deluxe:
        "You stand by Casey's car in the dark with your new hips and your heavy new chest and Nadine's cardigan on, which won't close over it, and the pine trees creak."
    else:
        "You stand by Casey's car in the dark with your new hips and your small soft chest and Nadine's clothes on, and the pine trees creak."
    show cg hol_carpark_think onlayer cgl
    "You think about the card. Every line of it. Silt Soak, Lymphatic Drainage, Hydration Therapy. You read it three times on the first night so you wouldn't look stupid, and every single word on it was true."
    "You think about the photo wall. Six, and one small one in front, every year, all the way back. Robin, smiling, short, front and centre. Robin saying {i}I came back.{/i}"
    if hol.deluxe:
        "You think about your own six signatures, Ellie, Ellie, Ellie, and how you upgraded yourself at the desk every day like a man filling his trolley at a sale, and how the last one was the neatest."
    else:
        "You think about your own five signatures, Ellie, Ellie, Ellie, and how you upgraded yourself at the desk every day like a man filling his trolley at a sale."
    "Nobody lied to you. Not once. That's the thing you keep coming back to, in the cold, with your arms round yourself. Nobody lied, and nobody stopped, and you're standing in a car park with the door open, and nobody's coming to get you."
    "Your thighs are cold. Your arse is cold. Your chest is cold. All of it's yours."
    $ hol.walked = True
    menu:
        "The car park. The open door."
        "Go back inside":
            $ hol.back = "soon"
            "You go back inside on your own feet."
        "Sit in the car a while longer":
            $ hol.back = "later"
            "You sit on the bonnet for a long while, and look at the lit windows, and think about the card."
            "Then you go back inside on your own feet."
    hide cg onlayer cgl
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_june", "dry")], cg="hol_back_in")
    "Dinner's still going. Delaney's telling a story. June's turning a page. Nobody looks up."
    "Nobody had noticed you were gone."
    hide hol_june
    call vn_night(8)
    jump hol_day_six

## ---- DAY 6: Checkout ---------------------------------------------------------------------------
label hol_day_six:
    $ hol.fit = "nadine"
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[], cg="hol_full_slate")
    show screen hol_printout(6)
    if hol.deluxe:
        "{i}Absorption: complete. Retention: complete. Upper contour: complete. Note: none required.{/i}"
    else:
        "{i}Absorption: complete. Retention: complete. Note: none required.{/i}"
    hide screen hol_printout
    if hol.deluxe:
        "Last day. Nadine's shorts, broad enough for two, and the bra she fitted you with yesterday, which you have to leave unhooked at the bottom now, under a cardigan that's given up."
    else:
        "Last day. Nadine's shorts, broad enough for two, and one of her bralettes, because nothing else fits."
    show hol_june dry at vn_cast_slot
    hol_june "\"Was starting to think you'd sleep through your printout, Ellie.\""
    hol_you "\"Already peaked, apparently. Absorption: max. Retention: max.\""
    hide hol_june
    show hol_delaney amused at vn_cast_slot
    hol_delaney "\"And that's what a real enzyme circuit will do to you, baby doll.\""
    hide hol_delaney
    "You go down to the desk by yourself, and book the full slate. Every line on the card: THE FULL PACKAGE, top to bottom, group enzyme circuit and all."
    hol_you "\"All of it. The full package. All the lines. If there's a platinum plus, give me that too.\""
    hol_desk "\"For your skin, ma'am?\""
    menu:
        "For your skin?"
        "Tell her the truth":
            $ hol.frank = "truth"
            hol_you "\"No. Not for my skin. I just want it. All of it, all day.\""
        "Tell her the truth, and upgrade":
            $ hol.frank = "upgrade"
            hol_you "\"No. I want it. And put me down for whatever comes after it.\""
            $ hol.upgrades += 1
    "It's the first frank word you've said all week. She writes it down, unbothered, like everything."
    hol_desk "\"Ellie Vance: Full Package, Group Circuit, Same-day Retention Observation. Did I miss anything?\""
    hol_you "\"Oh— wait. Can I get extra postural correction at the end of the day?\""
    hol_desk "\"Booked.\""
    $ hol_book(7)
    hide cg onlayer cgl
    $ vn_enter(bg="hol_dining", pc="earnest", pc_tag="hol_pc", cast=[("hol_robin", "kind")], cg="hol_robin_six")
    "Robin's at breakfast on her own, with toast. You sit down beside her on your two cushions."
    hol_robin "\"Ellie. Have you read what the enzyme is?\""
    "The second time she's asked. You look at her properly."
    hol_you "\"Yes. Properly, this time. I know what it is. I know what all of it is.\""
    if hol.deluxe:
        hol_you "\"Even the Deluxe. It's volume. It means {i}volume{/i}.\""
    hol_robin "\"And?\""
    hol_you "\"And I've booked the full package.\""
    "She laughs, a real one, for the first time all week, and puts her hand over yours on the table."
    hol_robin "\"Faster than I did. You did it so much faster than I did.\""
    hide cg onlayer cgl
    hide hol_robin
    jump hol_full_package

label hol_ending:
    $ hol_body(7)
    # ff 1:57 pm 11-18: group-photo no picture (owner ~1:50 pm, "we can just put some sprites on the screen at once"):
    # the cast is staged in front of the photo wall when the photo goes up, below
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[("hol_casey", "pleased")])
    if hol.deluxe:
        "{color=#9fe3cf}Your arse and thighs have gone all the way: huge, soft, heavy, the robe gives up on them. Your chest went with them: huge now, an H-cup, round and heavy and sitting out over your ribs, Deluxe all the way to the label. Your cock is still there, small, exactly where it's always been, and nobody at Hollow Pine has ever once been bothered by it.{/color}"
    else:
        "{color=#9fe3cf}Your arse and thighs have gone all the way: huge, soft, heavy, the robe gives up on them. Your chest is still small. Your cock is still there, small, exactly where it's always been, and nobody at Hollow Pine has ever once been bothered by it.{/color}"
    show cg hol_photo_take onlayer cgl
    "A member of staff with a camera on a tripod by the photo wall, bored, honest, never surprised, arranging the six of you like flowers."
    hol_casey "\"Come on, Ellie. Up front.\""
    "Delaney behind you, your head well under her chin now, level with her sternum, where it's come to sit this week. June with her magazine. Nadine fixing your cardigan on your shoulder. Robin beside you, her shoulder against yours."
    "The camera clicks. Everybody smiles. You smile too. You find you mean it, which is the strangest part of the whole week."
    hide cg onlayer cgl
    hide hol_casey
    $ vn_enter(bg="hol_desk", pc="earnest", pc_tag="hol_pc", cast=[("hol_delaney", "amused"), ("hol_robin", "kind")])
    if hol.deluxe:
        "The group photo goes up on the wall by reception. Six. Five tall women at the back, and the short one in front, beaming, with the biggest chest on the whole wall."
    else:
        "The group photo goes up on the wall by reception. Six. Five tall women at the back, and the short one in front, beaming."
    hide hol_delaney
    hide hol_robin
    show cg hol_next_card onlayer cgl
    if hol.deluxe:
        "Then a card on the desk: next year's reservation. Six lines. Five names, and one blank, and beside your own name, in the desk's neat hand, one box already ticked: {i}Expansion Package: Deluxe.{/i}"
    else:
        "Then a card on the desk: next year's reservation. Six lines. Five names, and one blank."
    "Casey slides it over to you, and the pen, and doesn't say anything."
    "You take the pen. You're already thinking of someone: some nervous friend. You're already planning the explanation."
    "Checkout. So simple, really. Six on the reservation, six coming home. One short in front."
    $ vn_feat("Six Coming Home")
    if hol.deluxe:
        $ vn_feat("Ellie's Deluxe")
    hide cg onlayer cgl
    jump hol_route_return
