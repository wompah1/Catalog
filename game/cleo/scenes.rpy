## cleo's sessions: her half of each chapter, from the scene break after "It's Friday" to the end
## of the week, mid-act. Her POV: "you" is her, and the narration never calls her Danny or he, and
## gives her no name before Nate says "Cleo" in week 4. THE WRONG LINE: Danny surfaces when Nate
## holds her (cle_under, her plate, his words, italic); weeks 1-2 Nate corrects it as a line Steph
## never said, from week 3 he hears Cleo's new way of talking. Non-con weeks 1-4, no flip; week 5
## breaks into begging mid-ride; week 6 he asks. The choice when he surfaces is what comes out,
## never whether. No tears, no menace, no pain, no escape. Nate is the only partner; nobody watches.
## Production rewrite (2026-11-13): each session run long from the book, a picture per beat, and a
## choice of hers that carries (greet1, talk2, ask3, stock4).

## ---- WEEK 1: an exact copy. Her mouth, kneeling on Steph's side of the bed ---------------------
label cle_session_one:
    $ cle.fit = "steph"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "sad")], cg="cle_one_room")
    "Warm lamplight, and the quilt mussed where you kneel, settled on her side of the bed with your knees in the same hollow they always find."
    "Nate's room, still arranged for her. Her side turned down. Her things on the dresser: a hairbrush, a tube of hand cream, a bottle of the perfume she wore, a hair tie round the neck of it."
    "You're in her grey cardigan, and her camisole under it, and your bob swings at your jaw when you turn your head, lavender, exactly the way it should. It's a room arranged for you. You feel it the way you always do: a small, comfortable certainty."
    "The door, and his trainers kicked against the skirting. He stops. His eyes don't quite find you."
    cle_nate "\"Steph.\""
    menu:
        "He's here. Say hello."
        "\"Hey, you.\"":
            $ cle.greet1 = "hey"
            cle_she "\"Hey, you.\""
            "That's how she said it. You know it's how she said it, because it's how you say it."
        "\"Come here, then.\"":
            $ cle.greet1 = "come"
            cle_she "\"Come here, then.\""
            cle_nate "\"That's not how she— she'd just say {i}hey, you.{/i}\""
            cle_she "\"Hey, you.\""
            "Warm and easy, his way, and he breathes out like he's been holding it a month."
    "He sits heavy on the edge of the bed, on the side where the sheets still hold the shape of her feet, and he looks at you the way a man looks at a photograph he half remembers."
    show cg cle_one_kneel onlayer cgl
    "Then his hand comes, slow, and strokes along your hair, and you lean into it greedily. He undoes his jeans one-handed, not quite looking at you, and draws you down into his lap."
    "His cock comes out heavy into your hand, half hard and getting there. You nuzzle his thigh, breathe hot along him, and take the head of him between your lips."
    "Slow. Wet. All the way down until your nose is in his hair and he makes a small broken sound, and then back up, your fist working the base, your tongue flat under him, the way he likes it."
    vn_sfx "{i}Shlk. Shlk.{/i}"
    cle_nate "\"Fuck.\""
    "His hand settles in your hair. He isn't looking at you. He's looking at the ceiling, at four years of ceiling."
    show cg cle_one_lines onlayer cgl
    "You pull off, a string of spit from your lip to the tip of him, and you say one of her lines, warm."
    cle_she "\"You want me to make you come in my mouth, baby?\""
    cle_nate "\"That's not how she said it.\""
    "His voice is very tired. His fingers tighten at the root of your hair."
    cle_nate "\"Just say, 'Come on, baby, fill my mouth.' Like that.\""
    cle_she "\"Come on, baby, fill my mouth.\""
    "A hot thrill at the correction. You say it his way, warm, filthy, delighted, without a question in your head, and you take him back into your mouth."
    show cg cle_one_deep onlayer cgl
    "You work him deeper. Slow, unhurried, cheeks hollowed, spit gathering on your chin and running down onto your knuckles. One hand cupping his balls. The other at his root, twisting. The rhythm is hers, deep and patient, tongue firm on the vein."
    "You pull off with a soft pop, wipe your chin with the back of your wrist, and nose along his thigh."
    cle_she "\"You going to make a mess for me?\""
    "Another of her lines, spun out for him, voice turned up just enough."
    cle_nate "\"Not quite.\""
    "He says it distracted, his gaze somewhere a long way off, and pulls you back up by your hair, gently, and guides your mouth onto him again."
    cle_she "\"{i}Mmh.{/i} Tell me how you want it.\""
    cle_nate "\"Just keep going, Steph.\""
    "It's sad. You can feel how sad it is for him, in the way he breathes. You keep it slow for him. You keep it warm. His thighs are shaking under your palms."
    cle_she "\"Want to fill me up, Nate?\""
    cle_nate "\"Yeah— fuck, just—\""
    show cg cle_one_cum onlayer cgl
    "You go down slow and let him push all the way along your tongue, and his hips jerk, and his fist closes in your hair and holds you to the root."
    cle_nate "\"Ah— fuck—\""
    vn_sfx "{i}Gulp. Gulp.{/i}"
    "He comes over your tongue, hot, filling your mouth, running down your chin, and you swallow and swallow and don't let him slip out."
    "He stays hard on your tongue. His hand in your hair doesn't loosen. It presses, slow and sad, asking for more, and you give it, sucking him wet and deep again, milking the last of him up the shaft and working him straight back toward the edge."
    show cg cle_one_hold onlayer cgl
    "Then his fingers close in your hair. Not hard. Just holding. Holding you down on him."
    "And somebody else is in your mouth with you."
    $ cle.surfaced += 1
    menu:
        "Somebody's in here. Somebody who isn't meant to be."
        "Pull off and say his name":
            $ cle.shout1 = "name"
            show cg cle_one_surface onlayer cgl
            "You get your mouth off him somehow, gasping, chin wet."
            cle_under "\"Nate— Nate, it's me, it's— get off— I'm not her—\""
        "Push at his thighs":
            $ cle.shout1 = "push"
            show cg cle_one_surface onlayer cgl
            "Your hands shove at his thighs, hard, and do nothing at all, because they're her hands and they're stroking him."
            cle_under "\"Let go of my— let GO— what is this, what's happening, stop—\""
    "It comes out in her voice. Of course it does. Soft and low and hers."
    cle_nate "\"That's not how she said it. She'd say, 'Missed this, didn't you?' All smug.\""
    "He says it with his eyes shut. Patient. Like a man correcting a line in a play."
    "And your mouth, her mouth, says it his way."
    cle_she "\"Missed this, didn't you?\""
    "Smug and warm and exactly his way. And sinks back down onto him."
    show cg cle_one_end onlayer cgl
    cle_under "\"Mmph— no— nnh— not— please, please let me— {i}mmph{/i}—!\"" with vnfx("shake")
    "Your throat opens for him on its own. Your fist works the base on its own. Your tongue knows exactly where she used to put it, and it goes there, and his hips jerk, and the sound you make round him isn't a no any more, it's just loud, wet and loud, spit running down your chin—"
    cle_under "\"Please— {i}please{/i}— don't— don't sto— no— I meant STOP— {i}mmmh{/i}—!\""
    "His hand stays in your hair. Gentle. Holding you on him."
    "And then whoever it was is gone again, somewhere under the warm, and it's only you, on your knees in the hollow on her side of the bed, with his cock in your mouth, sucking him slow the way she did."
    call cle_week_end
    jump cle_week_two

## ---- WEEK 2: sweeter. Her mouth, then her oiled thighs from behind ----------------------------
label cle_session_two:
    $ cle.fit = "steph"
    $ vn_enter(bg="cle_nate_room", pc="laughing", pc_tag="cle_pc", cast=[("cle_nate", "dry")], cg="cle_two_joke")
    "The bed's as familiar as your own laugh. You pull your hair free of its band on her side, the quilt soft under your knees, and Nate stands at the foot with his hands in his pockets, watching you with that look: hungry, a knot of nerves behind the almost-smile."
    if cle.greet1 == "come":
        cle_she "\"Hey, you.\""
        "His way, from last week, and he smiles at it."
    else:
        cle_she "\"Hey, you.\""
    cle_she "\"You gonna make me beg for it tonight, or should I start now?\""
    cle_nate "\"Don't tempt me. I can resist anything except temptation. And custard creams.\""
    "The old one. The one he's been dragging out for years, the one she always met with a flat look at the ceiling."
    "And you laugh. Really laugh, head back, a hand on his knee. Higher and brighter than she ever did. It bubbles out of you, sweet to the root."
    cle_she "\"Oh my God. That's terrible. Do it again.\""
    "He stares at you. Then he grins, for the first time in a long time, and does it again, worse."
    cle_nate "\"You're awfully cheerful tonight.\""
    show cg cle_two_tease onlayer cgl
    cle_she "\"Yeah? Maybe I just really like you.\""
    "You crawl up the bed toward him on your hands and knees, giving him the full view: the cardigan sliding off one shoulder, the camisole, the bra she loved and he never threw out."
    cle_she "\"Plan to actually kiss me tonight, or is this another mouth-only week?\""
    cle_nate "\"Go on, then. What do you want?\""
    "You stick your tongue out at him. Then, in a deliberately syrupy voice:"
    cle_she "\"Give it to me, baby. I want every drop.\""
    cle_nate "\"That's not how she said it.\""
    "He rolls his eyes, smiling anyway, and you giggle, actually giggle."
    cle_she "\"Fine, fine, Mr Fussy. Whatever you want, just ask.\""
    show cg cle_two_mouth onlayer cgl
    "He leans back against the headboard and opens his legs, and you kiss him, and slide down him, and take him in your mouth. Sweet with it. Slow and sweet and sloppy, humming round him, peeking up at him through your fringe."
    cle_nate "\"Bit faster.\""
    "So you go faster. Lips tight round the head, then all the way down in one long practised slide, your tongue broad and hot under him."
    "And then he laughs, at himself, at you, and doesn't correct anything else. He forgets to."
    cle_nate "\"Christ. You're too good at that.\""
    cle_she "\"Guess you missed me.\""
    cle_nate "\"Yeah. I did. Not yet, though. Want something else tonight.\""
    "He goes bashful. Genuinely, sheepish, his lashes low."
    cle_nate "\"Just— wanna fuck your thighs.\""
    cle_she "\"Fuck, that's {i}filthy.{/i} You know how to ask a girl nicely, or are you just gonna bend me over and take it?\""
    cle_nate "\"Turn over.\""
    show cg cle_two_oil onlayer cgl
    "You go gladly, onto her side of the bed, up on your elbows, your arse lifted and your thighs pressed tight with your cock tucked neat between them. You look back at him over your shoulder, sweet as pudding."
    cle_she "\"Is this what you want, baby?\""
    cle_nate "\"Yeah. Stay just like that.\""
    "He's got oil from the bedside drawer, and he pours it down the backs of your thighs and works it in with both hands, slow, all the way up, till your thighs are slick and shining."
    cle_nate "\"Squeeze them together. Like that. God.\""
    show cg cle_two_squeeze onlayer cgl
    "He pushes his cock between them from behind, under your arse, the head of it sliding out the front between your thighs, and you squeeze, and he groans into your shoulder."
    vn_sfx "{i}Shlick. Shlick. Shlick.{/i}"
    cle_she "\"You like that?\""
    cle_nate "\"Yeah. Fuck, yes. Don't move. Right there.\""
    menu:
        "He wants you to talk."
        "\"Make a mess of me.\"":
            $ cle.talk2 = "mess"
            cle_she "\"Want you to make a mess of me, Nate. Want it all over my thighs. Every drop.\""
        "\"Harder, baby.\"":
            $ cle.talk2 = "harder"
            cle_she "\"Harder, baby. I want to feel you lose control. I can take it, can't I?\""
    show cg cle_two_cum onlayer cgl
    cle_nate "\"Fuck— Steph— Jesus—\""
    vn_sfx "{i}Splurt. Splurt.{/i}"
    "He comes between your thighs with a groan that's almost a laugh, hot over the insides of them and the quilt under you, and he doesn't pull back. He's still hard. He pushes the mess through your slick thighs with the next stroke, and the next, and it's dirtier, and he groans again."
    if cle.talk2 == "mess":
        cle_she "\"There it is. Every drop. Now do it again.\""
    else:
        cle_she "\"There it is. Now harder. Do it again.\""
    show cg cle_two_hips onlayer cgl
    "His hands close on your hips. Tight. Holding you back onto him."
    "And somebody else is under them with you."
    $ cle.surfaced += 1
    menu:
        "His hands on your hips. Somebody's in here who shouldn't be."
        "Tell him to get his hands off":
            $ cle.shout2 = "hands"
            cle_under "\"Get your hands off me— Nate, get OFF— this isn't— I don't want this—\""
        "Try to get off the bed":
            $ cle.shout2 = "bed"
            "You try to crawl forward off the bed, off him. Your knees press back instead. Your thighs squeeze tighter round him."
            cle_under "\"Why can't I— let me UP— let me up, I'm not— I'm not her, I'm not—\""
    "It comes out sweet. Her voice, softer than she ever had it."
    cle_nate "\"That's not how she said it.\""
    "He laughs into your neck as he says it, and doesn't wait for you to say it right. He doesn't care, tonight."
    cle_nate "\"You're so much nicer than she was.\""
    "He's enjoying it. You can feel how much he's enjoying it, hot and hard and slick between your thighs, faster now, the head of him bumping the soft underside of your arse every stroke."
    show cg cle_two_terrible onlayer cgl
    cle_nate "\"You're too good to me, Steph. You know that? I'm a terrible person. I'm actually a terrible person.\""
    "He presses his face into your neck, laughing with real, shocked delight, like he's hearing your laugh for the first time, and he doesn't stop. He calls himself a terrible person, and doesn't stop."
    vn_sfx "{i}Shlick-shlick-shlick-shlick.{/i}"
    show cg cle_two_end onlayer cgl
    cle_under "\"Stop— nnh— stop it— {i}ahh{/i}— my legs won't— why are they SQUEEZING—!\"" with vnfx("shake")
    "Your thighs clamp on him every time he pulls back, like they want to keep him. Your hips push back into his. Your own cock's throbbing between your legs, untouched, dripping on the quilt. Your mouth's open, panting, loud."
    cle_under "\"Please— please, Nate— don't— {i}don't stop{/i}— no— no, I meant STOP— {i}ahh{/i}—!\""
    if cle.talk2 == "mess":
        "And then he's gone again, whoever he was, and it's only you, laughing breathlessly, asking for the mess, his cock sliding through your slick thighs on her side of the bed, Nate grinning into your shoulder, calling himself a terrible person, and not stopping."
    else:
        "And then he's gone again, whoever he was, and it's only you, laughing breathlessly, asking for it harder, his cock sliding through your slick thighs on her side of the bed, Nate grinning into your shoulder, calling himself a terrible person, and not stopping."
    call cle_week_end
    jump cle_week_three

## ---- WEEK 3: patient, and the way she says his name. Her first anal, face to face ---------------
label cle_session_three:
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_three_name")
    "Nate's room, and he isn't in a hurry. He's never been this patient. He undresses you like there's no clock anywhere in the world, the cardigan, the camisole, all of it, kissing whatever he uncovers."
    cle_nate "\"Hey, you.\""
    cle_she "\"Hey yourself.\""
    cle_nate "\"You know, I've been thinking about this all week.\""
    cle_she "\"Couldn't wait?\""
    cle_nate "\"No. Wanted to do this right. You want it?\""
    cle_she "\"Yeah. Want you to take your time. Want you to open me up. Face to face, Nate.\""
    cle_she "\"Na-ate.\""
    "Two notes, up at the end. That isn't how she said it. He doesn't correct it. He smiles like you've given him something."
    cle_nate "\"Say that again.\""
    cle_she "\"Na-ate.\""
    show cg cle_three_tongue onlayer cgl
    "He lays you on your back on her side of the bed and opens you up slow. His tongue first, flat and wet and patient, until your knees fall open on their own."
    cle_she "\"Oh— oh, that's— {i}mm{/i}— that's new—\""
    cle_nate "\"Yeah?\""
    cle_she "\"I like new.\""
    cle_nate "\"She would have hated that. God, I love that.\""
    "He says it delighted. Like it's the best news he's had all year."
    show cg cle_three_fingers onlayer cgl
    "Then a finger, slick. Then two. Plenty of lube, cold and then warm, and he takes his time, all the time there is, curling, stretching, watching your face."
    cle_she "\"Like that. Slow— God, Nate, open me up, I want all of it.\""
    cle_nate "\"Tell me if it's too much.\""
    cle_she "\"It won't be. Want you to fuck my ass, Nate. Want to feel you. All of you.\""
    show cg cle_three_in onlayer cgl
    "He comes up over you, face to face, and lines up, and pushes in. Slow. So slow you feel every bit of him open you, the head and then the rest, deeper, until he's all the way in and his forehead's on yours."
    cle_she "\"{i}Ohh.{/i} That's perfect, Nate. Feels so good.\""
    cle_nate "\"You feel incredible. You always do, but— fuck. Like this. You're perfect.\""
    menu:
        "He's moving in you, so slowly."
        "\"Slower. Make it last.\"":
            $ cle.ask3 = "slow"
            cle_she "\"Slower. Make it last. I want to remember this.\""
            "He goes slower. You didn't know he could. Every stroke a long, long pull and a long, long push."
        "\"Harder.\"":
            $ cle.ask3 = "hard"
            cle_she "\"Harder. Fuck me. I want to remember this.\""
            "He gives you harder, still face to face, still forehead to forehead, his breath coming short against your mouth."
    show cg cle_three_slow onlayer cgl
    cle_nate "\"You're so good, Steph. God, I needed this. Didn't want anybody but you.\""
    "Your hands go flat on his back. His mouth finds yours. Your cock lies trapped between your bellies, leaking, sliding in the sweat every time he moves."
    vn_sfx "{i}Pap... pap... pap...{/i}"
    show cg cle_three_hold onlayer cgl
    "His hands slide under your shoulders and hold you. Hold you still, under him."
    "And somebody else is in here with you, under all of it."
    $ cle.surfaced += 1
    menu:
        "He's holding you down. Somebody's waking up in the middle of it."
        "Shout at him":
            $ cle.shout3 = "shout"
            cle_under "\"Nate— NATE— get out— get it OUT— that's my— you're in my— oh God, get OUT of me—!\""
        "Beg him to look at you properly":
            $ cle.shout3 = "look"
            cle_under "\"Look at me— look at my FACE, it's me, it's— you know me, you KNOW me— stop—\""
    "It comes out in a voice that isn't hers and isn't yours. Lighter. Up at the end."
    "Nate laughs. Happy. He doesn't correct a word of it."
    cle_nate "\"I love it when you talk like that. That's so {i}you.{/i}\""
    "He moves. Slow and patient and deep. You can feel him, all of him, in a place nothing's ever been."
    show cg cle_three_cum onlayer cgl
    cle_under "\"Nnh— no— no, no, no— why does it— {i}ahh{/i}— why does it feel—!\"" with vnfx("shake")
    "Your hands are in his hair. Your hands. Pulling him down to you. Your heels are on the backs of his thighs. Your arse clenches round him every time he draws back, like it's trying to keep him in."
    cle_nate "\"Want my cum inside you? Tell me.\""
    cle_under "\"No— don't— don't you— {i}ahh{/i}—\""
    cle_she "\"Want all of you, baby. Want your cum inside me.\""
    "It's her voice that wins. It always is."
    vn_sfx "{i}Splurt.{/i}"
    "He comes in you with his forehead on yours and his eyes open, saying her name and then not her name, just a sound, and you clench round him and shake, and your own cock jerks between your bellies untouched."
    show cg cle_three_end onlayer cgl
    cle_under "\"Please— please— Nate— don't— {i}don't stop{/i}— no— I meant STOP— I meant— {i}ahhh{/i}—!\""
    "He doesn't stop. He's still hard, he's still slow, and he keeps going."
    cle_nate "\"She would have hated that. Christ, I love it.\""
    "And whoever he was is gone again, under the warm. And it's only you, with Nate deep in your arse, slow and patient, your hands in his hair. You say his name the new way, up at the end, and Nate laughs out loud, happy, and keeps going."
    call cle_week_end
    jump cle_week_four

## ---- WEEK 4: the name, and the non-decision. In the stockings --------------------------------
label cle_session_four:
    $ cle.fit = "steph"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_four_box")
    "There's a box on the bed. Black tissue paper."
    cle_nate "\"I got you something, Steph. I don't know if— just. See.\""
    "Black stockings, sheer. A black garter belt. She never owned anything like them, not once in four years."
    cle_she "\"Oh, you {i}dirty{/i} man.\""
    cle_nate "\"Never thought I'd see you in these.\""
    cle_she "\"Maybe you just never got brave enough to ask.\""
    menu:
        "Stockings on. How?"
        "Roll them up slowly for him":
            $ cle.stock4 = "slow"
            show cg cle_four_roll onlayer cgl
            "You put them on for him on the edge of the bed, slowly, one leg and then the other, toes pointed, rolling them up your calves, over your knees, snug at the thigh, clipping the garters on with your tongue between your teeth."
            cle_she "\"All for you.\""
        "Make him put them on you":
            $ cle.stock4 = "him"
            show cg cle_four_roll onlayer cgl
            "You lie back and hold one foot out to him, pointed, and wait. He kneels, hands not quite steady, and rolls them up your legs one at a time, slow, kissing each knee on the way past, and fumbles the garters until you laugh and do the last clip yourself."
            cle_she "\"Good man. All for you.\""
    $ cle.fit = "stockings"
    show cle_pc laughing
    cle_nate "\"Fuck. Look at you, Steph.\""
    cle_nate "\"She would have hated that.\""
    "He says it like it's the best thing in the world. He's looking at you like you're the best thing in the world."
    show cg cle_four_turn onlayer cgl
    cle_nate "\"Turn over for me?\""
    cle_she "\"Like this?\""
    cle_nate "\"Perfect.\""
    "On your hands and knees in the stockings, your arse up, the garter straps framing it. He kneels behind you, and doesn't do anything at all for a while."
    cle_she "\"Are you just going to stare?\""
    "He slicks himself and pushes into you from behind, slick and easy now, all the way, and holds your hips."
    cle_nate "\"Good girl, Steph.\""
    cle_she "\"Harder. Hold my hips. Let me feel it.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    cle_nate "\"Fuck, that's it— work for it, baby—\""
    show cg cle_four_legs onlayer cgl
    "Then he turns you over again and puts your stockinged legs up over his shoulders and pushes back in, and fucks you like that. The garters snap on every stroke. The stocking tops bite into your thighs and his hands are on the bare skin just above them, squeezing."
    vn_sfx "{i}Snap. Snap. Snap.{/i}"
    cle_nate "\"Steph— God— Steph—\""
    show cg cle_four_name onlayer cgl
    cle_nate "\"Cleo.\""
    "He hears himself. You see him hear himself."
    "He doesn't take it back."
    $ cle.named = True
    $ cle_her_name = "Cleo"
    cle_she "\"Mm. Right here. Don't you dare slow down.\""
    cle_nate "\"God, you sound so fucking good, Cleo. The view alone— fuck. Cleo. Best money I ever spent.\""
    "You answer to it like you always have. Of course you do. It's your name."
    show cg cle_four_hold onlayer cgl
    "He pins your ankles to his shoulders with both hands and leans his whole weight in, holding you folded under him."
    "And Cleo isn't the only one in here."
    $ cle.surfaced += 1
    menu:
        "Folded under him, held. Somebody else wakes up in the stockings."
        "Tell him whose name it really is":
            $ cle.shout4 = "name"
            cle_under "\"That's not my— that's NOT my name— my name's— Nate, my name's—\""
            "It won't come. The name. It's right there and it won't come out of her mouth."
        "Kick at him":
            $ cle.shout4 = "kick"
            "You try to kick him off. Your stockinged feet curl over his shoulders instead and stay there."
            cle_under "\"Get off— get OFF me— take these off me, get them OFF—\""
    cle_nate "\"Say it like that again. Cleo. Say anything.\""
    "He's so happy. He's never once been this happy."
    cle_nate "\"You like the stockings?\""
    cle_she "\"Look at me in these. Fuck me in them.\""
    show cg cle_four_cum onlayer cgl
    cle_nate "\"Yeah, that's it, come on— let me hear it—\""
    "You let him hear it. Loud, his name, her name, the garters snapping, and he comes deep in your arse with your stockinged calves crossed behind his neck, and your own cock spurts across your belly and the black lace at your hips."
    vn_sfx "{i}Splurt.{/i}"
    show cg cle_four_look onlayer cgl
    "Later, slow, he pulls out and kneels up between your legs and looks down at you, at all of you, in the stockings and the garter belt."
    "He looks for a long moment."
    "Then he bends and puts his mouth on the inside of your thigh, just above the stocking top, warm, and stays there."
    cle_she "\"Get back up here. Need you inside me. Now.\""
    show cg cle_four_end onlayer cgl
    "And then he's back inside you, all the way, and your stockinged legs lock round his waist."
    cle_under "\"Nnh— no— no, that's— {i}ahh{/i}— don't— don't say it— don't say that NAME—!\"" with vnfx("shake")
    "Your legs pull him in. Your arse grips him. Your mouth's at his ear."
    cle_nate "\"Cleo. You're perfect. So fucking good, Cleo.\""
    cle_under "\"Again— say it again— no— no, I meant— {i}ahhh{/i}—\""
    "And then he's gone, and it's only Cleo, with her stockinged legs locked round Nate's waist and Nate saying her name into her neck."
    cle_nate "\"Cleo— don't ever stop. Need you, Cleo.\""
    cle_she "\"That's me. Say it again.\""
    call cle_week_end
    jump cle_week_five

## ---- WEEK 5: things Steph never had. She starts it, and rides him -----------------------------
label cle_session_five:
    $ cle.fit = "gown"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_five_gown")
    "There's a drawer that's yours now. A mug. Your toothbrush in its own cup. A dressing gown on the back of the door, pink, yours, and slippers under the bed that you'll be putting on in the morning."
    menu:
        "What's on under the dressing gown?"
        "The lace set he bought":
            $ cle.wear5 = "lace"
            "Under it, the lace set he bought you. Black. Not much of it."
        "The silk slip":
            $ cle.wear5 = "slip"
            "Under it, the silk slip he bought you, lavender, like your hair."
        "The stockings again":
            $ cle.wear5 = "stockings"
            "Under it, the stockings. You liked the stockings."
    if cle.lane == "bra":
        ## 3a's week 5 beat: the bra he bought in her size
        show cg cle_five_bra onlayer cgl
        "And over it, under the gown, the new bra, lace, in your size. The first thing anybody's bought for your chest and not for hers. It fits like it was measured, because it was."
        "Nate stands behind you and undoes it slowly, one hook at a time, and catches the weight of you in both hands as it comes away, and breathes out against your neck."
        cle_nate "\"Keep it. It's yours.\""
        cle_she "\"Everything in this room's mine.\""
    show cg cle_five_climb onlayer cgl
    "For the first time, you don't wait for him. Before he's done anything at all you've got a hand flat on his chest and you've pushed him down on his back on the bed, and you're climbing on."
    cle_she "\"No more waiting, Nate. Get on your back. My turn. I've wanted this all week.\""
    cle_nate "\"Cleo—\""
    "He reaches for your hips. You catch his wrists and put them down on the pillow by his head."
    cle_she "\"Uh-uh. You're not driving tonight. Hands off the wheel.\""
    cle_nate "\"Yes, Cleo.\""
    show cg cle_five_ride onlayer cgl
    "You sink down onto his cock, your way. Slow. All the way down into your arse till you're sitting on him, and then you stay there and grind, because you like that, and nobody gave you that, it's just yours."
    cle_she "\"God, you're big tonight. Fuck, that's good. You feel it?\""
    cle_nate "\"Yeah, Cleo. You're incredible. So fucking hot.\""
    "You put his thumb in your mouth and suck it. You put his hands exactly where you want them, one on your hip and one on your thigh, and he leaves them there."
    cle_she "\"You hold me here. No squirming. Slow first. Then hard. Don't you dare go hard till I say.\""
    cle_nate "\"She would have hated that.\""
    cle_she "\"Good.\""
    show cg cle_five_beg onlayer cgl
    "You ride him slow, so slow, lifting almost all the way off and sinking all the way back down, until his head's back on the pillow and his jaw's clenched."
    cle_she "\"You want it faster, Nate? Or you want me to milk you just like this? Do I get to make you beg tonight?\""
    cle_nate "\"You can have anything. Just don't stop— fuck, Cleo, don't stop—\""
    cle_she "\"Beg, then.\""
    cle_nate "\"Please. Cleo. {i}Please.{/i} Fuck, please move, I'll do anything, tell me what you want next—\""
    cle_she "\"That's a good start. Say my name again.\""
    cle_nate "\"Cleo. Cleo, please—\""
    show cg cle_five_hold onlayer cgl
    "And he can't help it. His hands leave where you put them. He grips your hips and pulls you down onto him, once, deep, holding you there."
    "And somebody wakes up on top of him."
    $ cle.surfaced += 1
    menu:
        "Somebody's in here, riding him, and can't stop."
        "Tell him to let go":
            $ cle.shout5 = "letgo"
            cle_under "\"Let go— Nate, let go of me— I'm not— why am I ON you— get me OFF—\""
        "Grab the headboard to climb off":
            $ cle.shout5 = "headboard"
            "You grab the headboard to haul yourself off him. Your hips roll down onto him instead, harder."
            cle_under "\"Off— OFF— why won't they STOP— my hips won't— {i}ahh{/i}—\""
    cle_nate "\"God, I love it when you get like this.\""
    show cg cle_five_break onlayer cgl
    "Your hips don't stop. They lift and drop, lift and drop, faster, and the noise of it's wet and loud, and somewhere in the middle of all your noes his cock hits the place inside you that the noes can't reach—"
    cle_under "\"No— no— oh— {i}oh{/i}— don't— don't you— don't you dare stop—\"" with vnfx("shake")
    "It doesn't get corrected. He doesn't take it back."
    $ cle.broke = True
    cle_under "\"Don't stop. Don't— don't you {i}dare{/i} stop— harder, Nate, {i}harder{/i}, please, please, please—!\"" with vnfx("flash", "shake")
    "He goes harder. You ride him through it, begging, loud enough for the whole street, your hands on his chest and your head thrown back, and he lets you have every last bit of it."
    cle_nate "\"Fuck, Cleo, I'm gonna—\""
    cle_she "\"No. Not yet. You're giving me all of it.\""
    "And he holds on, for you, shaking, while you ride him hard and then slow again, when you say so."
    show cg cle_five_reverse onlayer cgl
    "Then you turn round on him, without letting him slip out, and ride him facing away, your hands on his knees, your arse rising and falling for him to watch."
    cle_she "\"Look at it. Look what's yours. You don't get to come yet. You lie there and you take it.\""
    cle_nate "\"Fuck. Okay. Okay, Cleo.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    cle_nate "\"Cleo, Cleo, Christ, Cleo—\""
    cle_she "\"Then hard. Then slow again, when I say so.\""
    "Hard, then. Your hair bouncing on your back, the bed knocking the wall, Nate swearing at the ceiling. Then slow, when you say so, and slower, till he's begging again, and you turn back round to watch his face."
    show cg cle_five_cum onlayer cgl
    cle_she "\"Now. Inside me. In my ass, every drop. That's how I want it.\""
    cle_nate "\"Cleo— {i}Cleo—{/i}\""
    vn_sfx "{i}Splurt. Splurt.{/i}"
    "He comes in you with your name in his mouth, and you sit down on him and feel every pulse of it, and your own cock spurts untouched across his belly, and you laugh."
    cle_nate "\"Cleo— fuck, you're perfect, you know? She would have hated that.\""
    show cg cle_five_end onlayer cgl
    "And then whoever woke up is gone, under the warm, and it's only Cleo on top, riding Nate's cock again at her own pace, with his hands where she put them."
    cle_she "\"Slow, this time. Hands right there. Don't you move them. And when I say so, you come in my ass again, and I feel every drop.\""
    cle_nate "\"Yes, Cleo.\""
    call cle_week_end
    jump cle_week_six

## ---- WEEK 6: nothing left to correct. Every position she asks for; he asks ---------------------
label cle_session_six:
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_six_room")
    "Nate's room. Her things are gone off the dresser. Yours are on it: your hairbrush, your mug of hair ties, a lipstick you picked."
    if cle.photo6 == "hat":
        "And a photo by the lamp, in a frame, of you in a woolly hat, pom-pom and all, laughing at him."
    else:
        "And a photo by the lamp, in a frame, of you asleep on the sofa, mouth open. You'll kill him for that one. Later."
    cle_nate "\"Got something for me tonight?\""
    cle_she "\"Everything. Come here.\""
    cle_nate "\"You know I can't stop thinking about you.\""
    "There's nothing left to correct. He doesn't try. He just says your name, over and over, like he's been saving it up."
    cle_nate "\"Cleo.\""
    cle_she "\"Hi.\""
    show cg cle_six_mouth onlayer cgl
    "You take him in your mouth first, because you want to, kneeling on the bed that's half yours now. Not her way. Yours: messy and grinning and humming, looking up at him the whole time, stopping to talk."
    cle_she "\"Missed this, didn't you?\""
    cle_nate "\"Every second of every day.\""
    "Nobody corrects anybody. You both laugh, and you go back down on him until he's swearing, and then you stop, because you've got other plans."
    if cle.lane == "bra":
        ## 3a's week 6 beat
        show cg cle_six_tits onlayer cgl
        "Like this one. You come up on your knees and take him between your breasts, and squeeze them round him with both hands, and look up at him over them, grinning."
        cle_she "\"Bet you didn't get this on a Friday before.\""
        cle_nate "\"Cleo— Christ— where did you learn—\""
        cle_she "\"Nowhere. I'm just good at things.\""
        vn_sfx "{i}Fwap. Fwap. Fwap.{/i}"
        "You work him up and down through them until he's gasping, and then you stop again, because you've still got other plans, and he groans at the ceiling, and you laugh."
    show cg cle_six_ankles onlayer cgl
    "On your back with your ankles on his shoulders first, because you ask. Slow, deep, lube everywhere, sweat on both of you."
    cle_she "\"Harder. Now harder.\""
    cle_nate "\"Cleo. Cleo. Christ, Cleo.\""
    show cg cle_six_top onlayer cgl
    "Then you're on top, because you ask, riding him with your hands on his chest and your hair falling round both your faces."
    cle_nate "\"She would have hated that.\""
    cle_she "\"I know. That's why I'm doing it. Kiss me.\""
    "He does. He kisses you all the way through it, up into your mouth, both of you laughing into it."
    show cg cle_six_side onlayer cgl
    "Then on your side, because you ask, his chest to your back, one of your legs hooked up over his arm, slow and deep and lazy, his mouth in your hair."
    cle_she "\"Now slow. Slower. Like that.\""
    show cg cle_six_front onlayer cgl
    "Then on your front, because you ask, and he's pressed all along your back, his mouth at your ear, fucking you down into the mattress, both of you talking the whole way, filthy and happy and stupid with it."
    vn_sfx "{i}Pap. Pap. Pap. Pap.{/i}"
    cle_nate "\"Cleo— gonna come in you— God, you feel so good—\""
    cle_she "\"Yeah, you're close. Do it. Fill me up. Give me every drop.\""
    vn_sfx "{i}Splurt.{/i}"
    "He comes in you, face in your hair, and stays in you, and stays hard, and starts again, slower, without being asked. You'd have asked."
    show cg cle_six_lap onlayer cgl
    "Then in his lap, because you ask, sitting up against the headboard with you astride him and him inside you, so slow you're barely moving, foreheads together, talking."
    cle_she "\"What did you do today?\""
    cle_nate "\"Thought about you. Burnt the toast. Thought about you some more.\""
    cle_she "\"Good. Do more of that.\""
    cle_nate "\"The toast?\""
    "You laugh, and it squeezes him, and he groans, and you both laugh at that, and it squeezes him again."
    cle_nate "\"Cleo. I'm serious. I don't know what I'd— I'm so glad you're here.\""
    cle_she "\"I know. I'm not going anywhere.\""
    "You lie down together on your sides after that, still joined, his chest to your back, and he wraps himself round you."
    show cg cle_six_hold onlayer cgl
    "His arms come round you and hold you, tight, from behind."
    "And somebody's there. Under the warm. Waking up."
    "Slowly. Not fighting it."
    $ cle.surfaced += 1
    menu:
        "He's here again. He knows this place now."
        "Ask for it":
            $ cle.say_six = "ask"
            cle_under "\"Nate. Nate— it's— don't stop. Please don't stop. I want it. I want this.\""
        "Ask him to hold you tighter":
            $ cle.say_six = "tighter"
            cle_under "\"Hold me— tighter— yeah, like that— don't let go of me. Please. I want it.\""
    $ cle.asked = True
    "Nobody's making him. He knows nobody's making him. He says it anyway, in her voice, in his own words, and he means every one."
    cle_nate "\"Cleo.\""
    show cg cle_six_end onlayer cgl
    cle_under "\"{i}Ahh{/i}— yes— yes, Nate— deeper— {i}please{/i}—!\"" with vnfx("shake")
    "He's deep inside you, saying your name into your hair, and you're coming on him untouched, shaking, loud, and he holds you through all of it."
    show cg cle_six_iam onlayer cgl
    cle_nate "\"Cleo. You need to talk to somebody about this.\""
    "He means it differently. He means it soft, laughing, his mouth at your ear. And you're still moving with him."
    $ vn_feat("I Am")
    cle_under "\"I am.\""
    if cle.lane == "stay":
        ## 3b: he asks her, the way Danny told him to
        cle_nate "\"Stay. Tonight, and tomorrow, and Sunday. Stay the weekend, Cleo. Please.\""
        cle_she "\"Yes.\""
        "It's the easiest word you've ever said."
        jump cle_stay_weekend
    call cle_week_end
    if cle.lane == "bra":
        call cle_bra_coda
    jump cle_route_return
