## THE STORY: day 8 (PLAN.md, the owner's added part). A day on parole: the mega femboy at work with Seiya's collar under
## his shirt; Kurose; the flat and Pirika; nothing stops him running, and by night he goes back by himself.

label gdk_parole:
    $ gdk.fit = "street"
    $ vn_enter(bg="gdk_flat", pc="flustered", pc_tag="gdk_pc", cast=[], cg="gdk_nothing_fits")
    "At seven on Monday morning a door opens in the black wall, and on the other side of it is your own hallway, with your shoes on the mat and the gas bill on the floor."
    "Pirika isn't there. There's a note on the kitchen table in very small handwriting: {i}gone to find help!! back tonight!! DON'T GO BACK.{/i}"
    "Nothing fits."
    "Your work trousers won't come up past your thighs. Your shirts strain at the buttons over your chest and hang off your waist like tents."
    "In the end it's your stretchiest black trousers, and your biggest white shirt tucked in hard. The trousers grip your arse so tightly you can feel the air on every curve of it."
    "You tie your hair back. It still reaches the middle of your back. The black collar sits at your throat under the shirt collar, and the brass charm is warm against your skin."
    "Nobody's stopping you. Your phone's got signal. There's a train to Osaka in an hour, and nobody there knows your face."
    "You go to work."
    $ vn_set_time(9, 0)
    $ vn_enter(bg="gdk_office", pc="flustered", pc_tag="gdk_pc", cast=[("gdk_kurose", "leer")], cg="gdk_parole_office")
    "The room goes quiet when you walk in. It stays quiet all the way to your desk, and you can feel every pair of eyes on the back of your trousers."
    "The women from accounts are at your desk by half past nine."
    "They want your moisturiser, your hairdresser, and the name of whoever did your lips, and they keep touching your hair as they ask."
    "Your section chief clears his throat at you three times before lunch and can't seem to finish a sentence."
    "And Kurose doesn't even pretend. He sits on the edge of your desk all morning with his coffee, looking down your shirt at the puffy swell of your chest."
    gdk_kurose "\"Shiraishi-kun. Shiraishi-{i}chan.{/i} What have you been {i}doing{/i} with yourself?\""
    gdk_you "\"Gym.\""
    gdk_kurose "\"Gym,\" he repeats, delighted, looking at your hips. \"Listen. I need a hand with the sample boxes in the stockroom. After six, when it's quiet. Just you.\""
    menu:
        "He's holding the stockroom key out on one finger."
        "Tell him no":
            gdk_you "\"No. Absolutely not. Get off my desk.\""
            "He shrugs and puts the key in his shirt pocket and goes."
            "At ten past six you're standing outside the stockroom door. You tell yourself it's for the sample boxes."
            $ gdk.fought += 1
        "Follow him":
            "At six he gets up and walks to the stockroom, and you get up and follow him, and the whole office pretends not to see."
            $ gdk.gave += 1
    $ vn_set_time(18, 10)
    $ vn_enter(bg="gdk_stockroom", pc="hungry", pc_tag="gdk_pc", cast=[("gdk_kurose", "leer")], cg="gdk_boxes")
    "The stockroom is a narrow room of steel shelving stacked with envelope boxes. It smells of cardboard, and the only light is a buzzing tube."
    "Kurose locks the door behind you and pushes you face-first against a stack of A4 boxes, and his hands go straight to your arse."
    gdk_kurose "\"God. Look at this. You've been hiding this under suits for two years?\""
    gdk_you "\"It wasn't— it wasn't like this two years ago— ahh♡—\""
    "He peels the trousers down over your hips, which takes some doing. Your arse spills out into his hands, and he groans as if somebody's punched him."
    "Then he sees the collar, and the brass lantern charm on it, and grins."
    gdk_kurose "\"Oh, you've got a {i}man.{/i} Does he share?\""
    "You don't know. You don't care. You push back against him."
    vn_sfx "Zupu. Pan. Pan. Pan."
    "He isn't Seiya. He's quick and greedy and too rough with his hands, and it's still so good you bite your own sleeve."
    "Your fat arse claps against his hips, the shelves rattle, and the envelope boxes come down round your feet."
    gdk_you "\"Harder— don't stop— Kurose-san— ahh♡— AHHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Byuru! Dopu, dopu."
    "You come all over a box of window envelopes. He comes inside you with a grunt and leans on you, panting."
    gdk_kurose "\"Same time tomorrow?\""
    "You do your trousers back up over his cum and don't answer. You know you won't be here tomorrow, and for a second you aren't sure which way you mean it."
    $ vn_set_time(21, 0)
    $ vn_enter(bg="gdk_flat", pc="stern", pc_tag="gdk_pc", cast=[("gdk_pirika", "worried")], cg="gdk_pirika_kitchen")
    "Pirika's on the kitchen table when you get home, sitting on the sugar bowl, glowing a sad, low yellow."
    gdk_pirika "\"Kaoru! You're— oh. Oh, look at you.\""
    gdk_you "\"Yeah.\""
    gdk_pirika "\"I went to the shrine at the top of the festival street. The priestess there can hide you. Under the big lantern, where the Society can't come.\""
    gdk_pirika "\"She says if you stay out of costume until the flame's had time to come back, a month, maybe two, it might—\" She stops, because you're touching the collar."
    gdk_pirika "\"Kaoru. How low is it?\""
    gdk_you "\"One flicker.\""
    gdk_pirika "\"Then one more and it goes out. You can't go back. Promise me.\""
    menu:
        "She's looking up at you from the sugar bowl."
        "Promise her you'll run":
            gdk_you "\"I promise. The shrine. Tomorrow.\""
            "She glows a bit brighter. You wait until she's asleep in the teacup she sleeps in."
            $ gdk.fought += 1
        "Tell her the truth":
            gdk_you "\"I think I want to go back.\""
            gdk_pirika "\"...I know. I could see it on you when you came in.\""
            "She doesn't argue. She just glows, very softly, and flies up and kisses the tip of your nose."
            $ gdk.gave += 1
    "At midnight you stand in your hallway with your hand on the brass charm at your throat."
    gdk_you "\"Light the way.\""
    "A door opens in your hallway wall onto black tatami and green fire. On the far side of the room, Seiya looks up from a book. He doesn't look surprised at all."
    $ vn_enter(bg="gdk_throne", pc="stern", pc_tag="gdk_pc", cast=[("gdk_lord", "smirk")])
    gdk_lord "\"Welcome home.\""
    call gdk_cut(21, 1, "Tuesday.")
    jump gdk_gate
