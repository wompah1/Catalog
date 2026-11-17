## heirloom's fourteen weeks, one a chapter. IT HAS TO SET: ch 1-5 non-con, 6 the break, 7 the flip at the
## camp, 8-14 consensual. Rei's sheet is the ladder; the climb only goes up.

## ---- 1. The Trunk ------------------------------------------------------------------------------
label hrl_ch1:
    $ hrl.chapter = 1
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg="hrl_trunk_open")
    "March, and cold enough that the clubroom radiator is losing. Every stray spike and club jacket has been kicked aside to make room for the trunk: battered brass, an ornate latch, older than anyone in the room."
    "The women's track club of Seiran University in a semicircle. You on the bench in the middle, the one man who trains with them, sleeves shoved to the elbow, jaw set."
    hrl_miki "\"You lost the interval, Yuu. Loser wears the prize. Fair's fair.\""
    "Miki springs the latch with a flourish and heaves the lid up."
    "Inside, on padded velvet, lies the club's secret: a skin. Flesh-toned, seamless, waist to mid-thigh, lying flat and still holding the shape of someone too athletic to be real. The full curve of hips. A runner's ass. A mound so lifelike your eyes catch on it before you can stop them."
    hide hrl_miki
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Kaede's. Our legend. She left it behind when she graduated, the way a snake leaves a skin. The club's kept it ever since.\""
    hrl_you "\"That's a joke. Tell me that's a joke.\""
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Only one way to find out. Off with the shorts, rookie.\""
    menu:
        "The heirloom, on its velvet."
        "Tell them no":
            $ hrl.dare = "no"
            hrl_you "\"No. Absolutely not. I'll clean spikes for a month. I'll clean them for a year.\""
        "Head for the door":
            $ hrl.dare = "door"
            "You stand up and make for the door. Haruna is already leaning on it, arms folded, grinning."
            hrl_you "\"Move. I'm not doing this. Haruna, move.\""
    hide hrl_miki
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"It has to be you. The trunk doesn't open for just anyone, and it opened today.\""
    "Rei doesn't raise her voice. She just nods, and Miki and Haruna each take an arm."
    jump hrl_dare

label hrl_ch1_night:
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[], cg="hrl_alone")
    "Rei herds them out with a dry \"Give our recruit a moment,\" and the door shuts on their laughter."
    "Alone. Hoodie on, your running shorts dragged back up over a crotch that isn't yours any more."
    "You wait for it to stop. For the prank latex to peel, for some trick of the nerves to wear off. It doesn't. There's only heat, and wet, and an ache that climbs with every panicked breath."
    "You pace the locker rows. You sit. You stand. Every shift of your thighs moves the new flesh and spreads the wet thicker."
    hrl_you "\"I'm not touching it. I'm not. I'm going to sit here until it stops.\""
    "It doesn't stop. It gets worse. Like being hard and desperate, but turned inside out into hunger: an emptiness that burns to be filled."
    jump hrl_rei_returns

label hrl_ch1_after:
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_rei", "smirk")], cg=None)
    hrl_rei "\"That's once. Don't worry. The club will keep you busy.\""
    "She presses a kiss over the place the skin seals to your waist, as if she were signing it."
    hrl_rei "\"Welcome to Seiran, Yuu. From here on up, you belong to us.\""
    hrl_you "\"I'll stay like this. Whatever it is. It stops here.\""
    hrl_rei "\"That's what they all say.\""
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch2

## ---- 2. Setting the Anchor -----------------------------------------------------------------------
label hrl_ch2:
    $ hrl.chapter = 2
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_equipment", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_bench_wait")
    "The equipment room smells of mats and cut grass. The taping bench has been rolled into the middle of the floor, and the team is waiting around it. You were told it was a kit check."
    hrl_rei "\"Team. The anchor has to set, and there's no substitute for doing it properly. If he isn't thoroughly used, the next region never starts.\""
    hrl_you "\"I'm not here for this. I came for the kit check, I'm leaving.\""
    hrl_rei "\"It has to set, Yuu. It's for you. Every recruit gets set.\""
    show cg hrl_strap_box onlayer cgl
    "Miki's already got the club's box open on the floor: a battered plastic crate with SEIRAN TRACK on the lid in marker, and inside, in a neat row, harnesses. Toys. A bottle of lube the size of a water bottle."
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Club property! Signed out by the captain. Nobody's had these out since the last star.\""
    hrl_you "\"I'm not— that's not— I'm going back to the field house—\""
    "The anchor throbs at the sight of them. Hard, like a second pulse, and you feel yourself go slick under the skin and you hate it."
    jump hrl_setting

label hrl_ch2_after:
    hide cg onlayer cgl
    $ vn_until(7)
    $ hrl_body(2)
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_dorm", pc="flustered", pc_tag="hrl_pc", cast=[], cg="hrl_mirror_hips")
    "By dawn there's a new ache. You stumble to the mirror expecting nothing, and stop."
    "{color=#c58ab8}Your hips, which always ran narrow, flare. A delicate, unmistakable swell, the same fullness you've seen in Kaede's old meet photos on the clubroom wall. The skin has climbed past where it sealed.{/color}"
    "And the anchor is still there, as desperate as ever, clenching at nothing."
    hide cg onlayer cgl
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg=None)
    show screen hrl_sheet(1)
    "Rei's sheet is pinned on the whiteboard: ANCHOR MAINTENANCE. One box ticked."
    hide screen hrl_sheet
    show screen hrl_pool(2)
    hrl_miki "\"Pool's open! Next region: waist, tits or face? What sprouts first?\""
    hide screen hrl_pool
    menu:
        "Miki's chalkboard."
        "Put a hundred yen on 'it stops here'":
            $ hrl.pool = "stops"
            "You chalk your own name beside IT STOPS HERE and slap a hundred-yen coin on the tray. Miki laughs so hard she has to sit down."
        "Refuse to bet on your own body":
            $ hrl.pool = "refuse"
            "You won't touch the chalk. Miki puts a hundred yen on 'stops here' in your name anyway, \"so you've got skin in the game.\""
    hrl_you "\"It's not going any further. I'll stay like this.\""
    "Miki shrieks. Rei says \"Uh huh\" without looking up. Nao just smiles. Nobody believes you, least of all the heat in your hips."
    hide hrl_miki
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch3

## ---- 3. Hips and Ass -----------------------------------------------------------------------------
label hrl_ch3:
    $ hrl.chapter = 3
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_schedule")
    "It's worse every day. The skin clasps high over your hips now and crests the small of your back. Every morning there's more curve under the hoodie and more bounce in your stride."
    "Rei's schedule goes up on the whiteboard: {i}Post-drills block, before showers: Takase. Bench.{/i}"
    menu:
        "Your name, on the schedule."
        "Tear it down":
            $ hrl.sched = "tore"
            "You rip it off the board, screw it into a ball and drop it in the bin while the whole room watches."
            hrl_rei "\"I printed six.\""
        "Ignore it":
            $ hrl.sched = "ignored"
            "You don't look at it. You don't look at it all through warm-ups, which is its own way of looking at it."
    hrl_you "\"I'm not turning up to that.\""
    hrl_rei "\"You don't have to turn up. We know where you are.\""
    hide hrl_rei
    jump hrl_hips_bench

label hrl_ch3_after:
    hide cg onlayer cgl
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "smirk")], cg="hrl_shorts_fight")
    show screen hrl_pool(3)
    "Your old running shorts won't go back on. The waistband bites before it's past your thighs."
    hide screen hrl_pool
    hrl_rei "\"Someone admit defeat.\""
    "She tosses you a bundle from the trunk's tray: the club's own kit, the women's cut, with room at the hips and the seat. The spandex shapes your ass round and lifted, and Miki gives you two thumbs up."
    hrl_you "\"I'm not losing the top half. The hoodie holds the line.\""
    hrl_rei "\"We'll see.\""
    $ hrl.fit = "hoodie"
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch4

## ---- 4. Waist and Belly --------------------------------------------------------------------------
label hrl_ch4:
    $ hrl.chapter = 4
    $ hrl_body(3)
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_dorm", pc="deadpan", pc_tag="hrl_pc", cast=[], cg="hrl_mirror_waist")
    "Every morning you check. It was dread once. Now it's routine, which is worse."
    "{color=#c58ab8}This morning there's a line where there wasn't one: your waist, narrower, pinched in above the new hips. Your belly soft under your palm.{/color}"
    hide cg onlayer cgl
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_track", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_miki", "tease")], cg="hrl_track_hoodie")
    "Warm-ups are a thousand small humiliations. Every stride pulls the hoodie across new curves."
    hrl_miki "\"Oi, Yuu! Want me to guess what's under the hoodie today? Or do we need Rei's tape measure again?\""
    "The track laughs. You flip her off mid-stretch and the hoodie rides up, and you grab it down one-handed with the other clamped over your shorts."
    "Nobody asks why you've started running slower. Everyone can see."
    hide cg onlayer cgl
    hide hrl_miki
    $ vn_until(19)
    $ vn_enter(bg="hrl_equipment", pc="flustered", pc_tag="hrl_pc", cast=[], cg="hrl_eqroom_alone")
    "After cool-down you go straight past the team, through the back of the field house and into the equipment room, and you lock the door behind you."
    hrl_you "\"It'll pass. It passes if I wait. I'll just— wait—\""
    "You lean on the bench, shaking, soaked through your shorts. The key turns in the lock."
    hide cg onlayer cgl
    jump hrl_waist_mouth

label hrl_ch4_after:
    hide cg onlayer cgl
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_dorm", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_nao", "gentle")], cg="hrl_nao_dorm")
    show screen hrl_pool(4)
    "Miki chalks it up before you're off the mat."
    hide screen hrl_pool
    "Rumours run faster than a relay baton: the one in the hoodie, whatever the weather. Miki starts a daily HOODIE WATCH on the club's socials."
    "That night Nao is waiting outside your block, her kit bag over one shoulder."
    hrl_nao "\"I thought you'd need company.\""
    "You let her up. She doesn't touch anything but your hand, and the belly you guide her palm to, and she holds you until the hunger fades to something you can sleep on."
    "You hate that it helps. You hate that it's her."
    hide cg onlayer cgl
    hide hrl_nao
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch5

## ---- 5. The Alumna Returns -----------------------------------------------------------------------
label hrl_ch5:
    $ hrl.chapter = 5
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_kaede", "smirk")], cg="hrl_kaede_arrives")
    "Kaede stands in the clubroom like she owns it. Broad through the shoulders, a sprinter grown past every uniform the university makes, her silver hair cropped short. Her shorts barely make it past the base of what's in them."
    "The team clears a respectful berth without a word. Only Rei meets her eye."
    hrl_kaede "\"So. This year's recruit's already running out of her shorts.\""
    hide hrl_kaede
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"He's— I mean, she's—\""
    hide hrl_miki
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"She's exactly where you want her.\" She looks at you. \"You're the fourth, sweet thing. I've had every one. Feel it tingling when I'm close?\""
    "You do. The skin, {i}her{/i} skin, prickles where it seals to your belly."
    hrl_you "\"It's tight. That's all. Still getting used to it.\""
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_kaede_clothes")
    "Rei unlocks the trunk. From the very bottom Kaede lifts a folded bundle: a top, a sports bra, old shorts with a mascot patch, thin from a thousand washes. They smell of stored warmth."
    hrl_rei "\"She's yours tonight. The equipment room's set up.\""
    hrl_you "\"I'm not anybody's tonight.\""
    hide hrl_rei
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"I'm here to finish what started. The skin's mine. It likes being home.\""
    hide cg onlayer cgl
    hide hrl_rei
    jump hrl_kaede_claim

label hrl_ch5_after:
    hide cg onlayer cgl
    $ vn_until(7)
    $ hrl_body(3)    # the ribs: drawn as the waist row
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_dorm", pc="flustered", pc_tag="hrl_pc", cast=[], cg="hrl_mirror_ribs")
    "{color=#c58ab8}Morning. The line has jumped: the skin laps at your ribs now. Your belly has caved in to a waist like a pinched hourglass, and the ribs above it are flaring the wrong way, soft.{/color}"
    "Kaede's old shorts are folded on your chair. You don't remember bringing them home."
    hide cg onlayer cgl
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg=None)
    show screen hrl_sheet(3)
    "On the whiteboard, three boxes ticked. Rei has drawn an arrow from WAIST to CHEST and written {i}K. accelerated{/i} beside it."
    hide screen hrl_sheet
    hrl_rei "\"She's staying the season.\""
    hrl_you "\"I can still pass.\""
    hrl_rei "\"For now.\""
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch6

## ---- 6. Chest Budding ----------------------------------------------------------------------------
label hrl_ch6:
    $ hrl.chapter = 6
    $ hrl_body(5)
    $ hrl.fit = "hoodie"
    $ vn_enter(bg="hrl_track", pc="flustered", pc_tag="hrl_pc", cast=[], cg="hrl_chest_drills")
    "It starts in drills: a dull heat high in your chest, behind the line Kaede pushed up. You duck into the equipment room and pull up your shirt."
    "{color=#c58ab8}The skin there is plumping. One side, then the other. Uneven, like a joke at your expense. Every brush of fabric sends a prickle straight down between your legs.{/color}"
    "After practice Rei nods toward the club bath. Coach Ida waves you all down the corridor, and doesn't look at you, and doesn't need to."
    jump hrl_bath_buds

label hrl_ch6_after:
    hide cg onlayer cgl
    $ hrl_body(6)
    $ vn_enter(bg="hrl_bath", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_rei", "soft")], cg="hrl_bath_bra")
    "Rei reaches into her bag and holds out a sports bra: white, racerback, brand new. The tag is already stitched with your surname."
    hrl_rei "\"For you. You're on the official uniform roster now.\""
    show screen hrl_pool(6)
    "Miki brandishes her phone: the chest pays out, and she's already taking bets on the voice."
    hide screen hrl_pool
    menu:
        "The bra, or the hoodie."
        "Put the bra on":
            $ hrl.top = "bra"
            $ hrl.fit = "bra"
            "You let them guide your arms through. The elastic settles under the new weight and the cups fill out faster than anyone expected. Miki sighs theatrically: \"There goes the hoodie era.\""
        "Hoodie, straight over the top":
            $ hrl.top = "hoodie"
            $ hrl.fit = "hoodie"
            "You pull the hoodie on over bare skin and zip it to the throat. Everyone watches the zip strain across the front. Rei just tucks the bra into your kit bag for later."
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_bath", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_kaede", "hungry")], cg=None)
    "Kaede comes over last, towel slung over one shoulder, and presses her palm flat to the middle of your new chest. The skin flickers under it like recognition."
    hrl_kaede "\"I can't wait to hear what you sound like when your throat joins the club.\""
    hide hrl_kaede
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch7

## ---- 7. Training Camp ----------------------------------------------------------------------------
label hrl_ch7:
    $ hrl.chapter = 7
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_minibus", pc="deadpan", pc_tag="hrl_pc", cast=[("hrl_nao", "gentle")], cg=None)
    "The club minibus up the mountain, wedged between Nao and Miki, Rei's printed schedule folded tight in your pocket. Kaede dozes across the back seat behind sunglasses."
    "The lodge sits above a curling road in the mist: a weathered porch, faded tatami, futon bins. There's no hiding what's changed, and no pretending it will end on the way down."
    "By the first dusk you've given up the hoodie altogether. A team tee and borrowed shorts that barely hold the hips; breasts that fill two hands now, high and athletic."
    hide hrl_nao
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_lodge_bath", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg="hrl_lodge_soak")
    "After the welcome dinner Rei herds everyone into the lodge's women's bath. You hesitate on the threshold out of years of habit, and then the heat takes you."
    "The bath's wide mirrors show it all back: a runner's hips, an ass full and high, a waist drawn tight, and a chest that is undeniably, bouncingly female."
    hrl_miki "\"Let's get this star polished up for the nightly relay!\""
    hide hrl_miki
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"Guess who's on anchor leg tonight.\""
    hide cg onlayer cgl
    hide hrl_miki
    jump hrl_camp_relay

label hrl_ch7_after:
    $ vn_clock.day += 2
    $ vn_until(9)
    $ hrl.fit = "yukata"
    $ vn_enter(bg="hrl_lodge_room", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "smirk")], cg="hrl_futon_morning")
    "You wake late on the sixth morning in a tangle of team: Nao's hand on your waist, Miki's head on your stomach, Rei at your knees, Kaede's broad palm low on your belly."
    "In the mirror across the room there's a girl with sleep-wild hair across her collarbones, and for the first time you let yourself grin at her."
    hrl_rei "\"You look smug. Something you want to tell us?\""
    hrl_you "\"Guess I'm not staying like this after all.\""
    "The team pounces: laughter, hands, Kaede pressing in behind you and Rei sliding between your knees. You don't beg for it to stop. You beg for more, and they give it, all the way down the mountain."
    hide cg onlayer cgl
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch8
