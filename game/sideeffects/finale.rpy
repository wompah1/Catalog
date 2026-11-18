## THE STORY: days 12-14 and the endings (PLAN.md). Friday: Ryouta (she starts it); Saturday: the Tachibana Club (the cap);
## Sunday: she gives in, and the last choice is marked as the ending. sef.held / sef.gave colour each epilogue
## (sef_thought_line).

## ---- 5. Friday: Ryouta --------------------------------------------------------------------------------------------

label sef_ryouta:
    $ sef.fit = "home"
    $ vn_enter(bg="sef_izakaya", pc="flustered", pc_tag="sef_pc", cast=[("sef_ryouta", "grin")], cg="sef_izakaya_booth")
    "Ryouta's the one person you've been afraid to see."
    "You've been best friends since you were both nineteen and working nights at the same warehouse in Saitama, loading lorries and eating convenience-store fried chicken at four in the morning."
    "He knows every stupid thing you've ever done."
    "You meet at your usual izakaya under the tracks. He walks straight past your booth twice before you call his name."
    sef_ryouta "\"No. No way. {i}Akira?{/i}\""
    "He sits down hard. He looks at your face, and your plum-tipped hair, and then, for a long helpless moment, at your chest, and then very determinedly at the menu."
    sef_ryouta "\"Sorry. Sorry, man. I'm not— I'm not looking.\""
    sef_you "\"Everyone looks. It's fine. You can look.\""
    "Three beers in, it's almost normal."
    "He's laughing at your story about the copier, and you're laughing too, and he keeps forgetting and calling you 'man', and every time he does you feel something warm and stupid in your chest."
    "Four beers in, his knee is against yours under the table, and neither of you has moved it."
    "Five beers in, you realise you've been staring at his mouth for a full minute while he talks."
    "The appetite's been building all day. Since the mirror. Since Hayami's strap-on. It sits low in your belly like a second pulse."
    "And Ryouta's the first man since the truck who's looked at you like he's {i}sorry{/i} for looking."
    $ vn_set_time(23, 30)
    $ vn_enter(bg="sef_ryouta_flat", pc="hungry", pc_tag="sef_pc", cast=[("sef_ryouta", "stare")], cg="sef_his_futon")
    "You walk him back to his flat, because he's drunker than you are, and at the door he turns round to say goodnight, and you don't let him."
    menu:
        "He's in the doorway."
        "Kiss him first":
            "You go up on your toes, which you've never had to do with him before, and kiss him."
            "He freezes. Then his hands land on your waist, very carefully, as if you might break, and he kisses you back."
            $ sef.gave += 1
        "Wait for him":
            "You don't move. You just stand there close enough to feel his breath, looking at him, until he makes a small helpless noise and bends down and kisses you."
            $ sef.held += 1
    sef_ryouta "\"Akira, we're— this is— are you sure? You're not— you'd tell me if—\""
    sef_you "\"Ryouta. I've had four men inside me this week and none of them asked. Shut up and take me to bed.\""
    "He takes you to bed."
    "He undresses you like it's a privilege."
    "When your breasts come free he says 'oh' out loud, just 'oh', the way you'd say it at a view, and fills both his hands and buries his face between them, and you laugh and pull him down."
    menu:
        "You're both naked on his futon."
        "Get on top":
            "You push him onto his back and straddle him. It's your first time choosing it. You take his cock in your hand and line it up and sink down on it, slow, all the way, watching his face."
            vn_sfx "Zupuuu..."
            $ sef.gave += 1
        "Pull him on top":
            "You pull him down on top of you and wrap your legs round him, and guide him in with your hand, and he groans into your neck as he slides home."
            $ sef.held += 1
    show cg sef_ryouta_together onlayer cgl
    vn_sfx "Zupu. Zupu. Nuchu."
    "It's different. It's completely different. It's still just as good; better, maybe, because nobody's taking anything."
    "Your hips move on their own and his hands are everywhere, on your breasts, your arse, your face, and he keeps saying your name."
    sef_ryouta "\"Akira— Akira— god— you're so— I can't—\""
    sef_you "\"Don't you dare pull out. Don't you {i}dare.{/i} Ahh♡— Ryouta— ahh♡— harder— there— {i}there♡—\""
    sef_you "\"Ryouta♡— Ryouta♡— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come on him with your nails in his shoulders, shouting his name, and he comes with you, deep, and holds on to you through all of it like you're the only solid thing in the world."
    "Afterwards he lies with his cheek on your breast and his arm across your belly, and says into your skin,"
    sef_ryouta "\"Was that weird? That was weird. Was it weird for you?\""
    sef_you "\"Ryouta. It's the best one I've had.\""
    "He doesn't say anything. But he holds on a bit tighter."
    $ vn_set_time(23, 59)
    $ sef_grow(5)
    $ vn_enter(bg="sef_mirror", pc="smug", pc_tag="sef_pc", cast=[], cg="sef_mirror_five")
    "You use Ryouta's bathroom mirror. It's smaller than yours, and you don't fit in it."
    "{color=#ff5fb8}They've grown again. A G cup now, heavy enough that you feel them pull when you lean forward, so full and round that your arms rest on the sides of them when you stand. They sway with every breath. They're the first thing anyone will ever see about you again.{/color}"
    "{color=#ff5fb8}Your hair's grown again too: past your shoulder blades now, halfway down your back, black at the roots, plum at the tips.{/color}"
    "You go back to bed and wake Ryouta up, and he doesn't complain."
    call sef_cut(19, 1, "Saturday.")
    jump sef_club

## ---- 6. Saturday: the Tachibana Club ----------------------------------------------------------------------------

label sef_club:
    $ sef.fit = "dress"
    $ vn_enter(bg="sef_flat", pc="stern", pc_tag="sef_pc", cast=[("sef_gonda", "grin")], cg="sef_gonda_offer")
    "Gonda's waiting on the landing when you get home on Saturday afternoon, with a dress bag over his arm and a smile you don't like."
    sef_gonda "\"Natsuki-chan's rent. Every month from now to next spring. Paid in full, in advance, by me.\" He holds up the bag."
    sef_gonda "\"If you come to a club I know tonight and make some friends of mine very happy.\""
    "Natsuki is behind the door. You can hear her not breathing."
    sef_you "\"What club?\""
    sef_gonda "\"The Tachibana Club. Akasaka. Very exclusive. Members only. They'll love you, Sena-chan. They love anything new.\""
    "You think of Natsuki doing her sums at the kitchen table at two in the morning. You think of the pills. Of the appetite, sitting low in you, already warm at the idea."
    sef_you "\"Give me the dress.\""
    $ vn_set_time(21, 0)
    $ vn_enter(bg="sef_club", pc="flustered", pc_tag="sef_pc", cast=[("sef_tachibana", "leer")], cg="sef_members_room")
    "The Tachibana Club is three floors up behind an unmarked door: leather armchairs, a low lacquered table, whisky in heavy glasses, and three men in their sixties in good suits, who stand up when you come in, as if you were somebody."
    "The dress is black and short and cut so low that it's mostly a frame for your breasts. You're not wearing anything under it. Gonda insisted."
    sef_tachibana "\"So this is the one. Gonda-san wasn't exaggerating.\""
    "Tachibana is the oldest: silver hair, a gold watch, the slow voice of a man who's never had to raise it."
    "The other two are a heavy one with a moustache and a lean one who doesn't stop smiling."
    sef_tachibana "\"A week, I'm told. A week ago, you were a man. Remarkable. Let us see the rest of the miracle.\""
    menu:
        "Three men are looking at you."
        "Look at the floor":
            "You look at the carpet. Deep red, very thick. You hear them breathe as you pull the straps off your shoulders and let the dress fall."
            $ sef.held += 1
        "Look at them":
            "You look straight at them while you pull the straps down. You want to see their faces. You do; they're worth it."
            $ sef.gave += 1
    show cg sef_three_members onlayer cgl
    "Then they're round you. Six old hands on you at once, weighing, squeezing, spreading."
    "One sucks a nipple and another pulls your head round to kiss you, whisky on his breath, and a third has two fingers inside you already and pulls them out shining and shows the others, and they laugh."
    sef_tachibana "\"On the table, I think.\""
    "They lay you across the lacquered table on your back with your head hanging over one end. The heavy one fills your mouth."
    "Tachibana takes his time between your legs, and then takes his time pushing in."
    vn_sfx "Juppu. Juppu. Pan. Pan."
    "The lean one kneels on the table and fucks your breasts, pushing them together round his cock with both hands, panting."
    "Every time one of them finishes, another takes his place. They have all night. They tell you so."
    menu:
        "The second round is starting."
        "Hold out":
            "You tell yourself you're doing it for Natsuki. You tell yourself it for a whole round."
            "Then the heavy one slides into your pussy from behind while you're still twitching from Tachibana, and you stop telling yourself anything."
            vn_sfx "Nupu. Zupu, zupu."
            $ sef.held += 1
        "Beg":
            "Tachibana's pulling out, and your body follows him, hips lifting off the table."
            sef_you "\"No— don't— more— someone put it back— please♡— please, I need it—\""
            sef_tachibana "\"Gentlemen. You heard the lady.\""
            $ sef.gave += 1
    "Something in you lets go."
    "It's the pills, it's the appetite, it's a week of men; it's all of it. You stop being Akira who came here for her flatmate's rent."
    "You're just a body on a table being filled, and loving it, and saying so."
    sef_you "\"More— more♡— fill me up— inside, cum inside— all of you, inside♡—\""
    vn_sfx "Dobyu! Dopu, dopu."
    sef_you "\"I'm cumming— again— I'm— AHHH♡— AHHHH♡—!\"" with vnfx("flash", "shake")
    "{color=#ff5fb8}And while you come, you feel it happening: a heat in your chest, a deep slow swell, like a breath that keeps going in.{/color}"
    "{color=#ff5fb8}Your breasts get heavier under the lean one's hands, rounder, fuller, until he can't push them together any more for the sheer size of them. He gasps. They all stop to watch.{/color}"
    sef_tachibana "\"Oh, look. Look at that. She's still {i}growing.{/i}\""
    "They take turns till three in the morning. You lose count of the men and then of the times you came."
    "At the end you're lying across the table dripping from everywhere, with whisky in your hair, smiling at the ceiling."
    sef_tachibana "\"Every Friday,\" Tachibana says, buttoning his jacket. \"If you like. Gonda-san can bring you. Or you can come by yourself.\""
    $ vn_set_time(23, 59)
    $ sef_grow(6)
    $ vn_enter(bg="sef_mirror", pc="blissful", pc_tag="sef_pc", cast=[], cg="sef_mirror_six")
    "{color=#ff5fb8}They're at the limit now: huge, heavy, the kind of breasts men stop in the street for.{/color}"
    "{color=#ff5fb8}Round and full and set high on your chest, each one more than a big handful for three old men at once. You'll need bras from the special shop.{/color}"
    "{color=#ff5fb8}You'll need everything from the special shop.{/color}"
    "{color=#ff5fb8}And the plum has climbed your hair, halfway up from the tips, a slow dark wine colour flowing down your back into the black. In the bathroom light you look like someone you'd stop in the street for, too.{/color}"
    "Two pills. You take the evening one, and smile at yourself, and go to bed without washing."
    call sef_cut(11, 1, "Sunday.")
    jump sef_sunday

## ---- 7. Sunday: giving in, and the ending --------------------------------------------------------------------------

label sef_sunday:
    $ sef.fit = "home"
    $ vn_enter(bg="sef_flat", pc="blissful", pc_tag="sef_pc", cast=[("sef_natsuki", "smile")], cg="sef_sunday_morning")
    "Natsuki's made breakfast. Natsuki never makes breakfast."
    sef_natsuki "\"Gonda left an envelope under the door. It's a receipt. Until April. Paid in full. Akira, what did you—\""
    sef_you "\"Don't worry about it.\""
    sef_natsuki "\"I {i}do{/i} worry about it. That's my rent, and you're... you've been doing all this, all week, haven't you. For me.\""
    "You think about it honestly, because she deserves that."
    sef_you "\"I started for you. I don't think I'm doing it for you any more.\""
    "She looks at you for a long moment: the robe that won't close, the plum hair, the bruise of a kiss on your throat."
    sef_natsuki "\"Are you happy?\""
    "Your phone buzzes on the table. Tsuge: 'Monthly review moved up."
    vn_sfx "Buuun. Buuun."
    "Monday, 6 pm.' Then Ooba: 'copier's free at lunch ;)' Then a number you don't know: 'Same carriage tomorrow.' Then Ryouta: 'last night, can we do it again. I mean."
    "If you want.'"
    "Then Dr Hayami: 'Sena-san. Your results are extraordinary. I'd like to monitor you around the clock. I have a room at the clinic. It has a very large bed and an excellent lock, and I have the only key."
    "Consider it.'"
    "You put the phone down. Two pills a day, for the rest of your life. Somewhere in this week you stopped hating them."
    sef_you "\"Yeah. I think I am.\""
    menu:
        "Where does Akira Sena go from here?"
        "Stay in the flat" (ending=True):
            jump sef_end_paid
        "Go to the clinic" (ending=True):
            jump sef_end_observed

label sef_thought_line:
    if sef.gave > sef.held:
        "You don't remember the last time you said no to anything. You don't miss it."
    elif sef.held > sef.gave:
        "You held out at every turn, at the start. You don't remember why, now. You only remember how good it felt when you stopped."
    else:
        "Some days you fought it and some days you didn't. It never made any difference. The pills always win, and you've stopped wanting them not to."
    return

label sef_end_paid:
    $ sef.fit = "office"
    $ vn_set_time(7, 42)
    $ vn_enter(bg="sef_train", pc="smug", pc_tag="sef_pc", cast=[("sef_grey", "grin")], cg="sef_end_carriage")
    "You stay."
    "Monday morning you're in the same carriage, at the same door, in a blouse two sizes too small on purpose and no knickers at all."
    "When the hand lands on your arse you push back into it."
    sef_you "\"You're late,\" you tell the man in grey, and he laughs into your hair."
    "Lunch is the copy room. Six o'clock is Tsuge's monthly review, which becomes weekly, which becomes whenever he likes."
    "Fridays are the Tachibana Club, and you go by yourself in a taxi, and the members stand up when you walk in."
    $ vn_set_time(22, 0)
    $ vn_enter(bg="sef_gonda", pc="hungry", pc_tag="sef_pc", cast=[("sef_gonda", "leer")], cg="sef_end_rent")
    "And on the last day of every month, you go downstairs to Gonda's flat in your dressing gown with nothing on under it, and knock."
    sef_gonda "\"Sena-chan. Rent's paid till April, you know. You don't have to—\""
    sef_you "\"I know.\" You drop the gown. \"Cum inside me anyway.\""
    vn_sfx "Pan. Pan. Pan."
    sef_you "\"Ahh♡— yes— there— AHHH♡—!\"" with vnfx("flash", "shake")
    "Natsuki never pays rent again. Ryouta comes round on Sundays and stays till Monday. Dr Hayami sees you once a week and writes down every number with a smile."
    "Side effects may include growth, sensitivity and appetite. You've got all three. You wouldn't give back any of them."
    call sef_thought_line
    call sef_route_return("Paid in full")

label sef_end_observed:
    $ sef.fit = "gown"
    $ vn_set_time(20, 0)
    $ vn_enter(bg="sef_ward", pc="blissful", pc_tag="sef_pc", cast=[("sef_hayami", "smirk")], cg="sef_end_room")
    "You go to the clinic."
    "The room is at the top of the building: a very large bed, a window over the Meguro river, cameras in two corners with their red lights on, and an excellent lock to which Dr Hayami has the only key."
    sef_hayami "\"Welcome home, Sena-san. Gown off. Let's begin.\""
    "She gives you your pills by hand now, morning and night, and watches you swallow."
    "She measures you every morning, and writes the numbers down, and every evening she straps on the pale pink cock she made for you and tests your sensitivity until you can't count."
    show cg sef_end_visitors onlayer cgl
    "And she has visitors. Colleagues, she calls them. Donors to the clinic."
    "Gentlemen from the Tachibana Club, who pay very well for an hour of observation and are allowed to participate. Ryouta, who comes on Sundays and is allowed to stay."
    "Ooba, once, by appointment, who couldn't stop apologising until you shut him up."
    vn_sfx "Nuchu. Pan. Pan. Pan."
    sef_you "\"More, Doctor— write it down— ahh♡— write {i}all{/i} of it down— AHHH♡—!\"" with vnfx("flash", "shake")
    sef_hayami "\"I am, Sena-san. Every single one.\""
    "You never go back to the office. You never take the 7:42 again. Natsuki gets a postcard of the Meguro river with a kiss on it in plum lipstick, and the receipt for the rest of the year."
    "The cameras watch. The lock stays locked. The appetite never stops growing."
    call sef_thought_line
    call sef_route_return("Under observation")
