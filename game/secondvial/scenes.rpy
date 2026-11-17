## secondvial's cellar, ch 3-6. PAID BEFORE OPENING: Caddic and the tasting customers never ask and never
## threaten; it's on the books, and they carry on past his no. The change is heat and too much sensation,
## never pain. Wren protests out loud, every time. The choice when he protests is what he says or does,
## never whether. Ch 3-5 non-con; ch 6 he breaks into begging partway.
## Production rewrite (2026-11-13, twinetesting-c9): every cellar scene run long, a picture per beat.

## ---- ch 3: caught mid-reversal. The first payment, on the barrels ---------------------------------
label svl_first_payment:
    $ svl.fit = "nude"
    $ vn_enter(bg="svl_cellar", pc="flushed", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_two_vials")
    "The wax won't come off for your shaking fingers. Caddic waits, thumbs in his belt, the lantern hissing. He doesn't help. He doesn't hurry you."
    "The first goes down like rainwater with a bitter punch, the second right behind it, and you stand there in the half-made body with both empties in your fists, waiting for the floor to tip."
    svl_caddic "\"Strip. It'll split the shirt otherwise. Shirts cost.\""
    "You do, because the change is already coming and the clothes won't hold it. The cellar's cold on skin that can't decide what it is."
    $ svl_body("n2")
    show cg svl_change_two onlayer cgl
    "{color=#e8a8c0}It comes hard. Heat floods your chest and it swells outward, past anything the cheap vial ever made: full, heavy, the nipples darkening as he watches. Your hips push wide. Your ass rounds out behind you. Between your legs it opens, slick at once, and it doesn't stop throbbing.{/color}"
    svl_you "\"Stop looking— stop— it's too much, it's too— {i}hah{/i}— what is this, the cheap one never—\""
    svl_caddic "\"The cheap one's a day's wage. Two's a different animal.\""
    "He walks round you once, slowly, the way he walks round a new barrel before he taps it."
    svl_caddic "\"Good. Now the other part. Payment.\""
    show cg svl_barrels onlayer cgl
    "He backs you against the kegs with a hand on each new hip and palms a breast, his thumb on the nipple, unhurried, like he's testing a fruit at market."
    menu:
        "Caddic, and the kegs at your back."
        "Push at his chest":
            $ svl.shout3 = "push"
            "You shove at his chest with both hands. It's like shoving a wall. He doesn't push back. He just doesn't move."
            svl_you "\"No— get off— I didn't agree to this, get OFF—\""
        "Clamp your thighs shut":
            $ svl.shout3 = "thighs"
            "You clamp your new thighs together. He sets his knee between them and waits until they give."
            svl_you "\"Don't— don't you dare— I said no—\""
    svl_caddic "\"First payment. Consider it rent.\""
    show cg svl_barrels_mouth onlayer cgl
    "He kneels on the cellar flags and puts his mouth on the new folds, broad and thorough, mapping you by what makes you jump. Then two thick fingers, slow, testing."
    "He works you the way he'd work a stuck tap: patient, unbothered, his one eye on your face to see what moves. The peppermint's cold on you. The vials are hot in you. Between the two you can't think."
    svl_you "\"I didn't— {i}hah{/i}— I didn't agree to {i}this{/i}, I agreed to the vials—\""
    svl_caddic "\"You agreed to the terms. This is the terms.\""
    "He says it into you, and doesn't stop. Your hand, which was in his hair to pull him off, stays in his hair."
    svl_you "\"Stop— {i}nnh{/i}— that's not— that's the vial, not me— {i}ahh{/i}— stop—\""
    show cg svl_barrels_in onlayer cgl
    "He stands, frees himself and lifts you onto the edge of a barrel, easily, the way he lifts the full ones. He pushes in, and the vial's heat answers him like it was waiting."
    vn_sfx "{i}Thunk. Thunk. Thunk.{/i}"
    "The barrel knocks the wall with every stroke. Dust comes down from the hatch. Upstairs somebody's dragging benches into place for opening, and doesn't hear a thing."
    svl_caddic "\"Made for it. The room'll fight to pay for a piece.\""
    svl_you "\"I'm not— {i}hahh{/i}— I'm not made for— oh— {i}oh{/i}— don't stop— NO— I mean STOP—\"" with vnfx("shake")
    show cg svl_barrels_peak onlayer cgl
    "Your body grinds down on him on its own, clutching, your new breasts bouncing against his chest, and it breaks over you all at once."
    svl_you "\"{i}AHH{/i}— no— {i}nooo{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "He finishes inside you with a grunt, steps back and tucks himself away as if he'd signed a delivery slip."
    show cg svl_barrels_after onlayer cgl
    "You sit on the barrel with your legs hanging and his cum running out of you onto the wood, and he takes a stub of chalk from his apron and makes a little mark on the barrel's lid, next to you."
    svl_caddic "\"Shift starts upstairs. Every night before opening. Don't be late.\""
    jump svl_ch3_after

## ---- ch 4: two vials, and the display he makes you give ----------------------------------------------
label svl_display:
    $ svl.fit = "nude"
    show cg svl_display_change onlayer cgl
    "Stripped on the patch of stone where the lantern catches every edge, you drink both. He sits on an upturned crate to watch, elbows on his knees, like a man at a cockfight."
    "At first nothing. Then pins and needles along your hips, and pressure under the skin, building, like a held breath."
    $ svl_body("n2")
    "{color=#e8a8c0}Your breasts fill out between your hands, heavier, pushing your fingers apart. Your hips flare. Your flat stomach goes soft. It runs past where it stopped this morning, and the throb between your legs turns from an itch into a hunger.{/color}"
    svl_caddic "\"Keep going, girl. Let's see you earn every coin.\""
    svl_you "\"I'm not doing anything! It's doing it! Stop {i}watching{/i}—\""
    svl_caddic "\"Hands on them. Show me the weight.\""
    show cg svl_display_weigh onlayer cgl
    "Your hands are already on them. You didn't put them there. You lift, because they're heavy and it's that or let them hang, and he nods, satisfied, the way he nods at a full measure."
    svl_caddic "\"Turn round.\""
    "You don't. You do. The vial does. You turn, and his eye goes over the new ass, the new hips, the backs of the new thighs, and he grunts."
    svl_caddic "\"On your knees.\""
    menu:
        "On your knees."
        "Refuse":
            $ svl.shout4 = "refuse"
            svl_you "\"No. I drank them. That's what you said. That's all you said.\""
            "He waits. The throb waits with him. Your knees go before you've decided anything."
        "Go down, and tell him exactly what you think of him":
            $ svl.shout4 = "tell"
            svl_you "\"You're a pig. You're a peppermint-stinking pig, and I hope your cellar floods.\""
            "He laughs, once, and unbuckles his belt."
    show cg svl_display_mouth onlayer cgl
    "His hand in your new hair. His cock at your lips."
    svl_you "\"{i}Mmh{/i}— {i}mmnh{/i}—!\""
    "The vial makes your mouth stupid for it: every slide over your tongue throbs straight down to your cunt. You hate it. Your tongue doesn't. Your tongue goes where it wants."
    svl_caddic "\"Slower. That's it. They'll pay double for that.\""
    show cg svl_display_tits onlayer cgl
    svl_caddic "\"Tits together. Make a show.\""
    "You press them together because your hands are already there. He fucks the valley between them, and every stroke drags your nipples against your own forearms."
    vn_sfx "{i}Shlick. Shlick. Shlick.{/i}"
    svl_you "\"Stop— {i}ahh{/i}— don't make me— don't— {i}hahh{/i}— I'm not— I'm NOT enjoying—\"" with vnfx("shake")
    "He comes across your breasts and chin with a grunt and tucks himself away. Your thighs are soaked, and nobody touched them."
    show cg svl_display_after onlayer cgl
    "You kneel on the cold stone with his cum cooling on your new breasts and look down at yourself in the lantern light. They're bigger than this morning. Bigger than the first payment. Bigger, you think, than anything the alchemist meant when she said {i}never two.{/i}"
    svl_you "\"That's not— that's not what one vial looks like.\""
    svl_caddic "\"No. That's what two looks like. That's what the room pays for. Clean up. Five minutes to the bell.\""
    jump svl_ch4_after

## ---- ch 5: the routine, and the private tastings --------------------------------------------------
label svl_tastings:
    show cg svl_tasting_stairs onlayer cgl
    "The first one comes down the stairs grinning, a silver already paid into Caddic's palm upstairs, a tankard still in his hand."
    svl_man "\"So this is the Bellhouse's best-kept barrel.\""
    svl_you "\"I'm not a barrel. I'm not on the menu. Go back up.\""
    "He doesn't go back up. Nobody ever does."
    menu:
        "The first of the night."
        "Keep the barrel between you":
            $ svl.shout5 = "barrel"
            "You keep the barrel between you for a full circuit of the cellar. He's in no hurry. The vial's heat is in even less of one."
        "Tell him the price is wrong":
            $ svl.shout5 = "price"
            svl_you "\"Whatever he charged you, it's not enough. Go and ask for your silver back.\""
            "He laughs and pays nothing more."
    show cg svl_tasting_barrel onlayer cgl
    "Bent over the barrel, skirt shoved up over the wide hips. He takes you from behind, and you shout no at the stone wall the whole time, and the body you're wearing pushes back onto him anyway."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    svl_man "\"Caddic said you'd say that. Said it's part of the tasting.\""
    svl_you "\"It's not part of— {i}nnh{/i}— I mean it— I mean every— {i}ahh{/i}—\""
    svl_you "\"No— no— get {i}off{/i}— {i}nnh{/i}— oh— don't— don't stop— no— STOP—\"" with vnfx("shake")
    show cg svl_tasting_after onlayer cgl
    "He leaves a coin on the barrel when he's done, the way you'd tip a girl for a good stew, and goes back up the steps whistling, and you hear the room cheer him at the top."
    svl_you "\"I'm not— I said no— I said it the whole time—\""
    "Nobody upstairs hears it. Caddic chalks the barrel with a mark, and the next one's already on the stairs."
    show cg svl_tasting_two onlayer cgl
    "Some nights there are two, laughing about who'll finish first, one at each end of you: one in your mouth with his hand in your ash-pink hair, one behind, and the barrel rocking between them."
    svl_man "\"First to finish buys the round!\""
    svl_you "\"{i}Mmph{/i}— {i}mmh{/i}— I'm not a— {i}mmph{/i}— a {i}game—{/i}\""
    show cg svl_tasting_milk onlayer cgl
    "Some nights it's your heavy breasts, a man's mouth on each, sucking like they've been told there's something in them, and one night, in the second month, there is: a bead of white at the nipple, and then more, and the man laughs and calls up the stairs for his friend."
    svl_you "\"What's— what is that— that's not— Caddic, what's it {i}doing—{/i}\""
    svl_caddic "\"Producing.\""
    "He says it from the hatch like a man noting a delivery. You protest every one of them, out loud, every time."
    show cg svl_tasting_peak onlayer cgl
    "And every time the vials' heat takes you over the edge, and you hate how loud it is."
    svl_you "\"{i}AHH{/i}— no— {i}please{/i}— no— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "Caddic chalks it in the ledger: a visitor's fee, a new debt for you."
    jump svl_ch5_after

## ---- ch 6: after the alchemist. He breaks into begging --------------------------------------------
label svl_break:
    $ svl.fit = "nude"
    $ vn_enter(bg="svl_cellar", pc="flushed", pc_tag="svl_pc", cast=[("svl_caddic", "flat")], cg="svl_six_vials")
    "Back to the cellar, because there's nowhere else. The alchemist's numbers on a scrap of paper in your pocket. Both vials. The fever rises, the hips prickle, the breasts swell tight and high against nothing."
    $ svl_body("n4")
    "Caddic's hands are on you before you're done undressing."
    svl_you "\"Not tonight. Please. Not tonight, I've had— I can't— she measured me, Caddic, she wrote it all down, she says it's not going back—\""
    svl_caddic "\"I know.\""
    "It's the first time he's ever said anything that wasn't terms. He doesn't say anything after it. His hands don't stop."
    show cg svl_six_bench onlayer cgl
    "He lays you on the cellar bench and pushes your knees up, and slides in, slow, slow the way he's never bothered to be, and the vial's heat meets him like an old friend."
    menu:
        "Caddic, on the bench."
        "Hold on to 'no'":
            $ svl.break6 = "hold"
            svl_you "\"No— no— I'm not saying it, I'm not—\""
            "You hold on to the word for as long as you can. It isn't very long."
        "Let it go":
            $ svl.break6 = "let"
            "Somewhere in the third stroke, the fight just goes out of you."
    show cg svl_six_slow onlayer cgl
    vn_sfx "{i}Creak. Creak. Creak.{/i}"
    "The bench creaks. The lantern swings. His big hands on your new hips, his thumbs in the soft new creases where the hips meet the thighs, holding you open, and the vial's heat building and building with nowhere left to go."
    svl_you "\"Caddic— {i}nnh{/i}— Caddic, don't— don't make it— {i}ahh{/i}— don't make it feel like—\""
    $ svl.broke = True
    show cg svl_six_peak onlayer cgl
    svl_you "\"{i}Ahh{/i}— more— don't stop— oh god, don't stop— {i}harder{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You hear yourself and don't stop. That's the worst part. The second worst is that it's the best you've felt in four months."
    show cg svl_six_after onlayer cgl
    "Caddic doesn't say anything about it. He doesn't gloat. He finishes, and sits on the end of the bench to get his breath, and looks at you, flushed and sprawled on the wood with your legs still open."
    svl_caddic "\"Hm.\""
    "That's all. He writes it in the ledger, a mark like all the others. You lie there and wish you could hate him properly, and can't, and hate that more."
    jump svl_ch6_after
