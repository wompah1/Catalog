## THE SOURCE: collar's passages, rewritten for the VN (2026-11-11; PLAN.md). One label a passage
## of the original (main.twee, rungs.twee), written as beats; the director scenes are in
## scenes.rpy. The original is in catalog/docs/routes/vn-original/collar/.

## ---- the opening night (Collar Opening, Collar Intro, First Mirror, First Calls) ----------------

label co_opening:
    $ co_init()
    $ co.fit = None
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg="co_rent")
    show cg co_rent onlayer cgl
    "Rent is due on Friday. Your bank app says what it said last week, only smaller."
    "The voice-companion app you've been failing on all month has just sent you a cheerful little summary of exactly how badly it's going."
    "Three calls. Two hang-ups. One tip that wouldn't buy a bus fare."
    vn_th "(The women on it earn triple. The app keeps telling you. Like a gym trainer who thinks you're not trying.)"
    show cg co_catalog onlayer cgl
    "So, around midnight, with nothing left to lose but the price of a cheap catalog item, you scroll past the first page of adverts."
    "And you buy the one with the number on it.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ vn_until(18)
    jump co_parcel

label co_parcel:
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg="co_parcel")
    show cg co_parcel onlayer cgl
    "The parcel comes that evening: a padded envelope with no return address and a pink collar inside."
    "Wider than a choker. Stiff at the front. A little plastic card tucked under the buckle."
    $ _co_c = co_card(1)
    "You read it out loud, to nobody. [_co_c]"
    "It's the only line long enough to catch your eye. You skip the rest."
    "You shrug, and buckle it on."
    show cg co_click onlayer cgl
    vn_sfx "Click." with vnfx("shake")
    "The front presses up under your jaw, and your chin lifts with it, and keeps lifting."
    "Ceiling corner. Top of the doorframe. You try to bring your eyes down. It doesn't let you."
    co_voice "\"Huh.\""
    "That isn't your voice. It's a woman's: low and warm and a little husky, the kind that sells perfume on the radio."
    co_voice "\"Oh. {i}Oh{/i}, that's good.\""
    vn_th "(You didn't say that. You were going to. It just got there first.)"
    $ _co_feel = co_body(1)
    "Your face is warm. Your scalp prickles. Something is happening above the collar, all at once.\n{size=-5}{color=#ff8fa3}▸ Find a mirror{/color}{/size}"
    jump co_first_mirror

label co_first_mirror:
    $ vn_enter(bg="co_bathroom", pc="delighted", pc_tag="co_pc", cast=[], cg="co_first_face")
    show cg co_first_face onlayer cgl
    "The bathroom mirror hangs at head height, which, with your chin where the collar's put it, is the only height you can see anyway."
    "The face in it isn't yours."
    "{color=#ff5fb8}It's a woman's face: softer at the jaw, fuller at the mouth, lashes you'd swear weren't there this morning.{/color}"
    "{color=#ff5fb8}The hair has come down past your ears in loose, glossy waves. The eyes are the same colour. Everything around them has been very carefully improved.{/color}"
    "You tilt your head, which the collar allows, and the woman in the mirror tilts hers. You grin. She grins."
    "You push your fingers into the hair. Thick and soft, and it keeps going, curling round your knuckles."
    "You bite your bottom lip and she does it too, and it's so hot your cock twitches in your jeans."
    co_voice "\"Oh, she's {i}gorgeous{/i}.\""
    "Breathy. You laugh, and she laughs."
    "{color=#ff5fb8}[CO_FEEL[1]]{/color}"
    co_voice "\"Okay. That's great for business.\""
    "That, for now, is the entire extent of your reaction. There's an app to open.\n{size=-5}{color=#ff8fa3}▸ Open the app{/color}{/size}"
    $ vn_pass(10)
    jump co_first_calls

label co_first_calls:
    $ vn_enter(bg="co_bedroom", pc="delighted", pc_tag="co_pc", cast=[], cg="co_first_calls")
    show cg co_first_calls onlayer cgl
    "You lie back on the bed with the phone held up over your face. It's the only way to see the screen. You go live."
    vn_sfx "Ding."
    "The first tip comes inside a minute. After that it doesn't stop."
    "You say hello in the voice and men stay on the line. You laugh in the voice and the little coin animation goes off like a slot machine."
    "You don't even have to say anything clever. You just have to keep {i}talking{/i}, and the voice does the rest, breathy on the s's."
    "One caller stays on longer than the others. He doesn't talk much. He just tips, big and often, like he's feeding a meter."
    co_voice "\"You still there, big spender?\""
    "It purrs it before you've thought of it. You hear him breathe."
    "Then he goes quiet a long moment. When he speaks again, his voice has changed. Interested. Almost amused."
    co_caller "\"I can hear you through the floor.\""
    "And then, very clearly, from the hallway outside your door:"
    vn_sfx "Knock knock."
    "\n{size=-5}{color=#ff8fa3}▸ Answer the door{/color}{/size}"
    jump co_doorway

## ---- rung 1: calls only (Collar Doorway). The doorway handjob, compelled. ------------------

label co_doorway:
    $ vn_enter(bg="co_door", pc="shocked", pc_tag="co_pc", cast=[("co_cal", "grin")], cg="co_doorway_open")
    show cg co_doorway_open onlayer cgl
    "You open the door chin up, phone still in your hand, call still live."
    "There's a man in the hallway with his phone in his, call still live too, and for a second both your voices come out of both phones at once."
    "He's big. The collar puts your eyes level with his throat and you have to look up from there: broad shoulders, dark stubble, a grin like he's just won something."
    co_cal "\"Cal. Downstairs. I've been tipping you for an hour.\""
    co_voice "\"I know.\""
    vn_th "(I didn't— that wasn't—)"
    "His grin gets wider. His eyes do a slow, appreciative circuit of everything the collar won't let you see."
    show cg co_doorway_hand onlayer cgl
    "You don't decide to reach for him. Your hand is just there, on the front of his jeans, and he's hard already, thick and heavy under the denim."
    show co_pc protesting
    vn_th "(No. NO. Hand. Off. Now—)"
    "He goes still. Then he asks, low:"
    co_cal "\"Yeah?\""
    "You open your mouth to say no."
    co_voice "\"Yeah.\""
    "It comes out warm and sure and nothing like you. He hears a yes. Of course he does. It was one."
    "He undoes his own fly. Your hand closes round him, chin in the air, eyes locked on his face, because the collar allows nothing else."
    vn_sfx "Shlk. Shlk."
    "You can't watch your hand. So the voice tells him what it's doing instead, out loud: how hot he is, how heavy, how the head slides wet on your palm."
    vn_th "(Stop TALKING. The call's still live. Half the app can hear this.)"
    "You try to say {i}stop{/i}. It comes out as a purr. He groans like you've touched him somewhere else entirely."
    co_cal "\"Fuck. {i}Fuck{/i}, keep talking.\""
    show cg co_doorway_throat onlayer cgl
    "His free hand comes up under the edge of the collar. His thumb drags down your throat and out along your shoulder. Slows. Comes back. Does it again."
    co_cal "\"Your shoulders. They're narrow. Soft. That's not a man's neck under there.\""
    "A shiver goes all the way down you, and it isn't fear, and you hate that it isn't."
    co_voice "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    vn_th "(I don't want to know. I don't want to KNOW.)"
    "So he tells you, low and filthy, his hand on your throat while yours works his cock: the slope of your shoulders, the line of your neck into the collar, the face looking up at him."
    "Every word winds you tighter. Your cock is hard in your jeans and nobody asked it."
    co_cal "\"Chin up.\""
    "The voice laughs, because it already is. He laughs too. You don't."
    show cg co_doorway_cum onlayer cgl
    "Then he stops laughing, swears, and comes all over your hand and the front of your shirt in thick hot pulses, while both phones count the tips." with vnfx("flash")
    co_voice "\"{i}Mmh{/i}. There you go.\""
    "Your hand never lost the rhythm. Twist at the top, thumb under the head, all by feel."
    vn_th "(You've never done that in your life. Whose hand IS this?)"
    $ co_advance(1)
    show cg co_mirror_arrives onlayer cgl
    "Halfway through it, the full-length mirror you ordered with the first hour's tips arrives. You sign for it one-handed."
    "It goes in the hall, face to the wall, to hang later."
    hide cg onlayer cgl
    show co_cal grin at vn_cast_slot
    co_cal "\"Same time tomorrow?\""
    vn_th "(Don't come back. Please don't come back.)"
    co_voice "\"Call first.\""
    "And you both know he won't.\n{size=-5}{color=#ff8fa3}▸ Close the door and sleep{/color}{/size}"
    hide co_cal
    call vn_night(7)
    jump co_morning

## ---- the route's days (Collar Morning, Collar Hub, Collar Calls, Collar Benny) --------------------

## The morning: chin up, the rung's wake line, the card in the post, the mirrors. Then the day goes
## straight to the evening's calls, where the next rung is waiting ("no downtime").
label co_morning:
    $ co.fit = None
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg=None)
    show bg co_bedroom onlayer bgl
    "You wake on your back with your chin in the air, because the collar doesn't let you wake any other way. Ceiling corner. Top of the doorframe. Same view as always."
    if co.tier == 1:
        show cg co_wake_1 onlayer cgl
        co_voice "\"Mmh. {i}Morning{/i}.\""
        "It purrs at the ceiling, husky and warm, and your cock is hard under the sheet just from hearing it."
        "Your hand still remembers the weight of Cal's. It goes down without asking you. You let it, because you can't not."
        vn_th "(This isn't me. It's the collar. It's the stupid collar.)"
        "You stroke yourself to the memory, chin up, moaning in her voice."
    elif co.tier == 2:
        show cg co_wake_2 onlayer cgl
        "Your chest is tender. Your hand squeezes it through your shirt without you looking, because you can't."
        "The soft swell under your palm makes you moan out loud."
        co_voice "\"Still there. God, still {i}there{/i}.\""
        vn_th "(Stop SAYING things.)"
    elif co.tier == 3:
        show cg co_wake_3 onlayer cgl
        "Your ass aches, and your shirt is stretched tight across your tits. The whole building heard you on the stairs."
        co_voice "\"Good.\""
        "It tells the ceiling, and your hands squeeze until you're squirming."
        vn_th "(Not good. Not GOOD. ...Mostly not good.)"
    elif co.tier == 4:
        show cg co_wake_4 onlayer cgl
        "Your hair is all over the pillow. Your waist is a curve under the sheet that your hand can follow and your eyes can't."
        "Your tits roll heavy when you stretch."
        co_you "\"Ohh— {i}heavy{/i}—\""
        "That one's yours. Your hips lift off the mattress on their own, and you let them."
    else:
        show cg co_wake_5 onlayer cgl
        "The collar's on. It's always on now."
        co_you "\"Morning.\""
        "Husky and right. You never want to hear the other one again."
        "Your soft little cock lies useless against your thigh, and your ass is already aching for Cal."
    hide cg onlayer cgl
    ## the days of the same between rungs (CO_RUNG_DAY; 2026-11-12, the counter keeps the story's weeks)
    $ _co_gap = co_gap_days()
    if _co_gap > 0:
        $ _co_g = CO_GAP[co.tier]
        "{color=#b7b7b7}[_co_g]{/color}\n{size=-5}{color=#ff8fa3}▸ Days of the same{/color}{/size}"
        $ vn_pass(_co_gap * 1440)
    ## the card for the coming rung arrives with the post (cards four to six; seven and eight come in their own passages)
    if co.tier in (1, 2, 3):
        $ _co_n = co.tier + 1
        $ _co_c = co_card(_co_n)
        $ renpy.show("cg co_card_%d" % (_co_n + 2), layer="cgl")
        "A card on the mat with the post. You read it in the voice: [_co_c]"
        "Into the kitchen drawer with the others. You keep them because throwing them away feels like a decision."
        hide cg onlayer cgl
    show bg co_bathroom onlayer bgl
    "The bathroom mirror at head height: the face, the hair, the pink collar, and nothing below it."
    "The face is lovely. It's getting lovelier. You'll have to take Cal's word for the rest."
    show bg co_hall onlayer bgl
    show cg co_hall_mirror onlayer cgl
    "The full-length mirror leans in the hall, face to the wall, exactly where you put it."
    "You'd have to take the collar off to hang it properly. Then there's a call, or a knock, or something better."
    "Later."
    hide cg onlayer cgl
    "The callers come out at six. Something always gives when they do.\n{size=-5}{color=#ff8fa3}▸ Wait for the callers{/color}{/size}"
    $ vn_until(18)
    jump co_evening

## The evening: what you've ordered in (Benny), the shift on the app, and whatever brings the rung.
label co_evening:
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg=None)
    show bg co_bedroom onlayer bgl
    $ _co_s = co_status()
    "{color=#b7b7b7}[_co_s]{/color}"
    ## Benny on the intercom: one beat a rung. He never sees you; you never open the door while he's there.
    if 1 <= (co.tier or 0) <= 5:
        show cg co_intercom onlayer cgl
        vn_sfx "Bzzzt."
        co_benny "\"Delivery for— uh— flat three-oh—\""
        if (co.tier or 0) >= 4:
            co_you "{=co_hypno}“Just leave it by the door, sweetheart.”{/=co_hypno}"
        else:
            co_voice "{=co_hypno}“Just leave it by the door, sweetheart.”{/=co_hypno}"
        "There's a pause on the line long enough to drive a bus through."
        $ _co_b = CO_BENNY[co.tier]
        $ renpy.show("cg co_benny_%d" % co.tier, layer="cgl")
        "[_co_b]"
        "You never open the door while he's there. You never stop using the voice on him."
        hide cg onlayer cgl
    show cg co_calls onlayer cgl
    $ _co_l = co_calls_line()
    "[_co_l]"
    $ vn_pass(120)
    hide cg onlayer cgl
    if co.tier == 1:
        "Halfway through a call there's a knock, and it isn't a question.\n{size=-5}{color=#ff8fa3}▸ The door{/color}{/size}"
        jump co_couch
    elif co.tier == 2:
        "Your phone buzzes with a text that isn't a tip. {color=#4372ff}Come down. Stairs. Now.{/color}\n{size=-5}{color=#ff8fa3}▸ The stairwell{/color}{/size}"
        jump co_stairwell
    elif co.tier == 3:
        "{color=#4372ff}Roof,{/color} says the next text. {color=#4372ff}Bring the voice.{/color}\n{size=-5}{color=#ff8fa3}▸ Up to the roof{/color}{/size}"
        jump co_roof
    elif co.tier == 4:
        "You end the shift late and fall asleep with the phone on your chest.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
        call vn_night(7)
        jump co_shower
    else:
        "When you put the phone down, there's a box outside the door.\n{size=-5}{color=#ff8fa3}▸ Bring it in{/color}{/size}"
        jump co_item_eight

## ---- rung 2: Cal indoors (Collar Couch). The couch, by feel; the chest arrives. Compelled. ------------

label co_couch:
    $ _co_feel = co_body(2)
    $ vn_enter(bg="co_lounge", pc="shocked", pc_tag="co_pc", cast=[("co_cal", "grin")], cg=None)
    show bg co_lounge onlayer bgl
    "Your shirts have started hanging differently. You haven't looked. You've been told."
    "Cal doesn't call first. That's the rung: one knock, the door, and he's in, past you and onto your couch like he pays rent, knees apart, grinning up at you."
    co_cal "\"Keep talking. I like it better in the room.\""
    vn_th "(Get out. Get OUT of my—)"
    co_voice "\"Then sit back, big spender.\""
    show cg co_couch_kneel onlayer cgl
    "Your knees go before you've decided anything. Down between his legs, which is easier than it sounds: the collar keeps your face tipped up, and his face is right there."
    show co_pc protesting
    "You get his jeans open by feel. You get his cock out by feel: heavy, hot, already leaking."
    vn_th "(Don't. Don't you DARE—)"
    "Your mouth takes him in without ever once seeing him, eyes locked on his."
    co_cal "\"{i}Fuck{/i}. You can't even look at it.\""
    co_voice "\"Mmh.\""
    "It agrees, round him. He swears again."
    vn_sfx "Glk. Glk."
    "You bob on him slow and sloppy, and every time you come up for air the voice keeps talking: how thick he is, how he tastes, how he twitches on your tongue."
    "Every time you go back down he groans like you've punched him. Every time, you were trying to say {i}no{/i}."
    show cg co_couch_chest onlayer cgl
    "His hands slide down the back of your neck, under your shirt, round to the front. And stop."
    co_cal "\"Hey. {i}Hey{/i}. That's new.\""
    "{color=#ff5fb8}His thumbs brush your chest and your whole body jolts. A soft swell under his palms that wasn't there last week, warm and give-y.{/color}"
    "{color=#ff5fb8}Your nipples have gone sensitive enough that his thumbs dragging over them make you moan round his cock.{/color}"
    "You pull off, gasping, a string of spit still between you."
    co_voice "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    co_cal "\"Chin up.\""
    "That makes him laugh, because it is. Then he tells you, in detail, cupping what isn't a handful yet."
    co_cal "\"The swell of it under your shirt. It fills my palms more every time I come up here.\""
    co_cal "\"Couple of weeks, you won't be able to hide it at all. Not a handful yet. It's going to be.\""
    vn_th "(It's GROWING. It's not just the face. It's not just the voice—)"
    "Your hand is under your own shirt before you can stop it. There they are. A soft little swell, warm, puffy at the nipple."
    "It squeezes, and a jolt goes straight to your cock."
    co_voice "\"Ohh— {i}fuck{/i}, Cal, I can {i}feel{/i} them—\""
    "Your hand squeezes again and you moan right into his thigh, and that part, the moan, is all yours. That's the worst of it."
    "You go back down on him like it's a reward. Your throat opens on its own, tongue flat, lips sealed. Your mouth acts like it's done this a hundred times."
    "When he comes it's in your mouth, deep, his hand in your hair, and you swallow with your eyes on his face because there's nowhere else they can go."
    show cg co_couch_fingers onlayer cgl
    "Then he pulls you up into his lap. His hand slides down the back of your jeans. His fingers find your ass."
    co_cal "\"Can I?\""
    vn_th "(No. No, no—)"
    co_voice "\"Yes.\""
    "Instantly. You didn't say it. You'd have said no."
    "His fingers push into you, slick and slow, and you make a noise into his neck you didn't know the voice could make."
    $ co_advance(2)
    menu:
        "He isn't finished. Neither is the voice."
        "The voice says keep going":
            jump co_couch_sex
        "The voice sends him home":
            jump co_couch_close

label co_couch_after:
    $ vn_enter(bg="co_lounge", pc="flushed", pc_tag="co_pc", cast=[("co_cal", "soft")], cg=None)
    show bg co_lounge onlayer bgl
    show co_cal soft at vn_cast_slot
    if co_enc.partner_came:
        co_cal "\"Same time tomorrow.\""
        "He's wrecked, sprawled across your couch."
    else:
        "Cal kisses the edge of the collar and says he'll be back, and you both know he means tomorrow."
    "The mirror is still face to the wall. You'll hang it after. He's still here after."
    vn_th "(Tomorrow. He's coming back tomorrow. And the voice will say yes.)"
    hide co_cal
    "\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump co_morning

label co_couch_close:
    $ vn_enter(bg="co_lounge", pc="protesting", pc_tag="co_pc", cast=[], cg="co_couch_close")
    show cg co_couch_close onlayer cgl
    co_voice "\"Go on home, big spender. You've earned it.\""
    "He goes home grinning. You lie on the couch with your chin in the air and your hand on your own chest, feeling the new softness through your shirt."
    "You can't see it. You don't need to."
    "{color=#ff5fb8}Your hand squeezes. Kneads. Your nipples are so sensitive the cotton makes you gasp.{/color}"
    co_voice "\"Mmh— they're {i}growing{/i}—\""
    "It tells the ceiling, and your hand keeps squeezing until your hips are rocking off the cushions."
    vn_th "(They're growing. And you can't even look.)\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump co_morning

## ---- rung 3: the stairwell (Collar Stairwell). First anal over the rail: resist, then break. MANDATORY. ---

label co_stairwell:
    $ _co_feel = co_body(3)
    $ vn_enter(bg="co_stairwell", pc="shocked", pc_tag="co_pc", cast=[], cg="co_stairs_top")
    show cg co_stairs_top onlayer cgl
    "Your legs are on the stairs before you've decided anything. You tell them to turn round. They don't."
    "{color=#ff5fb8}None of your shirts fit any more. You've been buying new ones over the phone, guessing, in the voice, while the shop assistants flirt with you.{/color}"
    "{color=#ff5fb8}On the top step your hands come up and cup them through the shirt, both hands. A real weight now: a B cup at least, soft and warm, and your jeans are snug across a rounder ass.{/color}"
    co_voice "\"Mmh— feel {i}that{/i}.\""
    "It purrs it at nobody. Your knees go weak, and you hate them for it."
    if _co_feel:
        "{color=#ff5fb8}[_co_feel]{/color}"
    "The stairwell is cold and echoing, and every door on every floor can hear it. You've never once used the voice outside your own front door."
    show cg co_stairs_rail onlayer cgl
    show co_cal hungry at vn_cast_slot
    "Cal's waiting on the half-landing between your floor and his, leaning on the rail."
    "He watches you come down: chin up, collar on, shirt strained across something that definitely wasn't there a fortnight ago. His mouth goes slack."
    co_cal "\"Turn around. Hands on the rail. If that's okay.\""
    show co_pc protesting
    vn_th "(It's NOT okay. Say it. Say it in any voice at all—)"
    co_voice "\"It's okay.\""
    "And the stairwell carries it up three floors.\n{size=-5}{color=#ff8fa3}▸ Your hands find the rail{/color}{/size}"
    hide co_cal
    jump co_stairwell_sex

label co_stairwell_after:
    $ vn_enter(bg="co_stairwell", pc="flushed", pc_tag="co_pc", cast=[], cg="co_stairs_after")
    show cg co_stairs_after onlayer cgl
    $ co_advance(3)
    if co_enc.partner_came:
        "Cal finishes buried deep, groaning into the back of your neck, and you feel every hot pulse of it while you cling to the rail."
    else:
        "You cling to the rail, shaking, stuffed full of him, until the stairwell stops ringing."
    "His hands are still round the front of you. They've been there the whole time."
    co_voice "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    "It gasps it, and he tells you."
    co_cal "\"Your chest is full now. Real handfuls. Spilling out of my grip, soft and heavy, bouncing every time I went in.\""
    "He says it into your ear while he's still inside you, and you clench on him so hard he laughs."
    co_cal "\"And this.\""
    "One hand drops to your ass and squeezes."
    co_cal "\"Rounder every time. Look at it. It's getting {i}fat{/i}.\""
    "You moan so loud the stairwell rings with it. That moan was you."
    "Your body knew how to take him the whole way. Breathe out, open, squeeze on the way back. You never practised that."
    show cg co_stairs_door onlayer cgl
    "Two floors down, a door opens. Somebody stands there, listening."
    "You couldn't lower your voice if you tried. It isn't yours to lower."
    co_voice "{=co_hypno}“Again. Chin up. Again.”{/=co_hypno}"
    vn_th "(That wasn't me. ...Was it?)\n{size=-5}{color=#ff8fa3}▸ Climb back upstairs and sleep{/color}{/size}"
    call vn_night(7)
    jump co_morning

## ---- rung 4: the roof (Collar Roof). Riding him under the sky: THE FLIP. From here it's yours. ------

label co_roof:
    $ _co_feel = co_body(4)
    $ vn_enter(bg="co_roof", pc="shocked", pc_tag="co_pc", cast=[], cg=None)
    show bg co_roof onlayer bgl
    "{color=#ff5fb8}Your trousers needed a belt this week, then a tighter belt, then no belt at all, because something has happened to your waist that Cal has explained to you twice, in bed, with his hands.{/color}"
    "The roof is wind and gravel, and the whole town laid out below you in lights."
    show cg co_roof_lap onlayer cgl
    show co_cal hungry at vn_cast_slot
    "Cal sits back against the parapet and holds a hand out."
    co_cal "\"C'mere. Can I?\""
    co_voice "\"Yes.\""
    "Before you can open your mouth. Of course."
    hide co_cal
    "He pulls you down into his lap, and you sink onto his cock in the open air, slow, with a long moan the wind carries off over the rooftops."
    "The collar tips your head right back. Your throat is bare to the sky, and Cal's mouth lives there: your neck, the edge of the collar, the soft skin under your jaw."
    show cg co_roof_ride onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    "And somewhere between one bounce and the next, you notice the collar isn't doing it."
    "Your hips are. Lift, drop, roll. Nobody ever showed you that, and nobody's making you do it now."
    vn_th "(Oh. Oh, no. Oh, {i}yes{/i}.)"
    show co_pc flushed
    co_you "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    "That one is yours. The first one. You pant it at the stars, bouncing on him, and you want the answer."
    co_cal "\"Your waist. Look at this. My hands nearly meet.\""
    co_cal "\"You've got a waist like a pin-up and tits bouncing in my face, and you can't see any of it.\""
    "His grip tightens and he drags you down onto him, hard."
    co_cal "\"{i}Chin up{/i}.\""
    show cg co_roof_tits onlayer cgl
    "{color=#ff5fb8}You grab your own tits mid-bounce. They overflow your hands now, a D, heavy and swinging, nipples hard as stones in the wind.{/color}"
    co_you "\"Ahh— they're so {i}big{/i}— Cal, they're so big and I can't even {i}see{/i} them—\""
    "You squeeze and ride and squeeze. Your hair whips round your face, long enough to get in your mouth."
    if _co_feel:
        "{color=#ff5fb8}[_co_feel]{/color}"
    "Your cock is still there, hard, trapped between your bellies, dragging against his abs every time you rise and fall. Nobody touches it. Not him. Not you."
    show cg co_roof_cum onlayer cgl
    co_you "\"I'm— Cal, I'm— {i}ahhh{/i}—!\"" with vnfx("shake")
    "You come from being fucked, your cock spurting untouched between you while you clench and cry out at the sky." with vnfx("flash")
    "He's still hard. You rise up off him, slick and shaking, and hover there in his lap with the head of him nudging you."
    $ co_advance(4)
    menu:
        "Your choice, now. Your first."
        "Keep riding him":
            jump co_roof_sex
        "Lie back on the gravel and breathe":
            jump co_roof_close

label co_roof_after:
    $ vn_enter(bg="co_roof", pc="flushed", pc_tag="co_pc", cast=[], cg="co_roof_after")
    show cg co_roof_after onlayer cgl
    "Afterwards you lie against his chest with the town below you. Cal offers, again, to hang the mirror for you."
    co_you "\"After.\""
    "\n{size=-5}{color=#ff8fa3}▸ Back down to bed{/color}{/size}"
    call vn_night(7)
    jump co_shower

label co_roof_close:
    $ vn_enter(bg="co_roof", pc="flushed", pc_tag="co_pc", cast=[], cg="co_roof_after")
    show cg co_roof_after onlayer cgl
    "You lie back on the gravel and breathe, and the stars breathe with you."
    "Cal offers, again, to hang the mirror for you."
    co_you "\"After.\""
    "He laughs into your hair.\n{size=-5}{color=#ff8fa3}▸ Back down to bed{/color}{/size}"
    call vn_night(7)
    jump co_shower

## ---- rung 5: never off indoors (Collar Shower, Collar Whole Day). Consensual. ----------------------

label co_shower:
    $ co.fit = "towel"
    $ vn_enter(bg="co_bathroom", pc="content", pc_tag="co_pc", cast=[], cg=None)
    show bg co_bathroom onlayer bgl
    $ _co_c = co_card(5)
    "Card seven is waiting on the mat. [_co_c] The drawer."
    show cg co_shower_off onlayer cgl
    "You take the collar off to shower. Your chin drops for the first time in days, and you keep your eyes on the tiles out of pure habit."
    "Under the water, you say something to yourself."
    "It comes out in your own voice."
    show co_pc shocked
    "It sounds {i}wrong{/i}. Rough and flat, like somebody else's. A man doing an impression of you."
    "You stand there dripping and listen to the echo of it, and you don't like it at all."
    $ _co_feel = co_body(5)
    if _co_feel:
        "{color=#ff5fb8}[_co_feel]{/color}"
    show cg co_shower_buckle onlayer cgl
    "You buckle the collar back on wet."
    vn_sfx "Click."
    "Chin up."
    show co_pc content
    co_you "\"Better.\""
    "It is."
    "It doesn't come off indoors again."
    vn_sfx "Knock knock."
    "\n{size=-5}{color=#ff8fa3}▸ Answer the knock{/color}{/size}"
    jump co_whole_day

label co_whole_day:
    $ co.fit = None
    $ vn_enter(bg="co_bedroom", pc="delighted", pc_tag="co_pc", cast=[("co_cal", "grin")], cg="co_day_bed")
    show cg co_day_bed onlayer cgl
    "Cal comes up in the morning and doesn't leave until the evening, and it's all one long scene: the bed, then the kitchen counter, then the bed again, the voice going the whole time."
    "You opened the door to him. You'd open it again."
    show bg co_kitchen onlayer bgl
    show cg co_day_counter onlayer cgl
    "He fucks you from behind on the counter with his hands full of your hips."
    "{color=#ff5fb8}And they're {i}hips{/i} now: wide and soft, an ass that fills his grip and jiggles every time he slams into it.{/color}"
    co_you "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    "You beg it, and he tells you about your ass in such detail you come halfway through the description."
    "{color=#ff5fb8}Your tits are squashed on the worktop, spilling out either side of you: a DD now, and heavier every day.{/color}"
    co_you "\"Ohh— {i}ohh{/i}, they're so heavy— harder, Cal, make them {i}bounce{/i}—\""
    "Your ass knows how to grip him, tight on the way out, loose on the way in. You never practised that either."
    show cg co_day_cock onlayer cgl
    "Then, for the first time, he reaches round and takes your cock in his hand."
    "{color=#ff5fb8}It's softer than it was. Slower to rise. It fits his fist with room to spare, a sweet little thing next to his.{/color}"
    co_cal "\"Look at that. It's getting so small. It's cute.\""
    "He strokes it fondly while he fucks you, and you make a noise in the voice like he's flipped a switch."
    co_cal "\"Chin up.\""
    show cg co_day_cum onlayer cgl
    "You laugh, and your cock spurts weakly in his hand while your ass milks him, and he comes with a groan, buried deep. You feel it flood you." with vnfx("flash")
    show cg co_day_schedule onlayer cgl
    "Midway through the afternoon, from the counter, you read him Benny's shift schedule out loud, in the voice, while he's still inside you."
    co_cal "\"Who's Benny?\""
    co_you "\"The intercom.\""
    $ co_advance(5)
    menu:
        "He's still in you. The afternoon's still going."
        "Bend back over the counter":
            jump co_whole_day_sex
        "Let the day end":
            jump co_whole_day_close

label co_whole_day_after:
    $ vn_enter(bg="co_bedroom", pc="flushed", pc_tag="co_pc", cast=[("co_cal", "soft")], cg=None)
    show bg co_bedroom onlayer bgl
    show co_cal soft at vn_cast_slot
    $ vn_until(19)
    "By the evening you can barely stand: the collar still on, Cal's hand still round your soft little cock."
    co_you "\"What's tomorrow's card going to be?\""
    "\n{size=-5}{color=#ff8fa3}▸ Let him go home{/color}{/size}"
    hide co_cal
    call vn_night(7)
    jump co_morning

label co_whole_day_close:
    $ vn_enter(bg="co_bedroom", pc="flushed", pc_tag="co_pc", cast=[("co_cal", "soft")], cg=None)
    show bg co_bedroom onlayer bgl
    show co_cal soft at vn_cast_slot
    $ vn_until(19)
    "By the evening you can barely stand."
    co_you "\"What's tomorrow's card going to be?\""
    "He doesn't know, and neither of you minds.\n{size=-5}{color=#ff8fa3}▸ Let him go home{/color}{/size}"
    hide co_cal
    call vn_night(7)
    jump co_morning

## ---- rung 6: never off, then off (Collar Item Eight, Look Down, First Vaginal). Consensual. ---------

label co_item_eight:
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg="co_item_eight")
    show cg co_item_eight onlayer cgl
    $ _co_c = co_card(6)
    "Card eight comes in the box. [_co_c]"
    "The enclosed is a collar: slim and black, barely wider than a ribbon, with a tiny electronic module at the front. The future version the first card promised."
    "You put the card in the drawer and the box on the bed."
    show cg co_flower onlayer cgl
    vn_sfx "Bzzzt."
    "The intercom. Benny, with a single flower and no food at all."
    co_you "\"It's lovely.\""
    "You tell him, in the voice, and you don't open the door."
    hide cg onlayer cgl
    "Then Cal comes up, and nobody mentions the mirror.\n{size=-5}{color=#ff8fa3}▸ Take him to bed{/color}{/size}"
    jump co_look_down

label co_look_down:
    $ vn_enter(bg="co_bedroom", pc="flushed", pc_tag="co_pc", cast=[], cg="co_look_bed")
    show cg co_look_bed onlayer cgl
    "He fucks you on the bed: from behind first, your face in the pillow and your chin still up."
    "Then rolled onto your back with your knees by your ears and his cock buried in your ass, the voice spilling out of you in long, broken moans."
    show cg co_look_unbuckle onlayer cgl
    "The new collar is on the pillow beside your head. You reach up, mid-thrust, and unbuckle the posture collar to try the slim one."
    vn_sfx "Click."
    co_you "\"Oh.\""
    "It's the same voice. Exactly the same: low and warm and husky, with nothing round your neck at all. It's just yours now."
    co_cal "\"Chin up.\""
    "He says it by reflex. And the collar isn't holding it any more."
    "So you look down."
    show cg co_look_down onlayer cgl
    $ _co_feel = co_body(6)
    "{color=#ff5fb8}For the first time, you see it: the body he's been describing for weeks.{/color}"
    "{color=#ff5fb8}Breasts, full and heavy and {i}yours{/i}, swaying with every thrust. A waist that pinches in like a pin-up's. Hips flaring wide around him, soft thighs spread, his hands sinking into them.{/color}"
    show cg co_look_tits onlayer cgl
    co_you "\"Oh my— oh, look at them—\""
    "You grab them with both hands, and they're {i}huge{/i}, DDs spilling over your fingers, nipples fat and pink, and you can finally watch yourself squeeze."
    "You moan at the sight. You squeeze harder just to watch them bulge."
    co_you "\"Cal, look at my {i}tits{/i}—\""
    co_cal "\"I've been looking for weeks.\""
    "And he slams in."
    "And your cock."
    show cg co_look_shift onlayer cgl
    "{color=#ff5fb8}It's small, and soft, and as you watch, it gets smaller. It shrinks in on itself, stroke by stroke, while Cal fucks you: softening, drawing in, sinking down into your body.{/color}"
    show cg co_look_cunt onlayer cgl
    "{color=#ff5fb8}Until there's nothing left of it but a sensitive little nub, and then not even that: there's a slit, wet and pink and swollen, a cunt opening up under your own eyes where your cock used to be.{/color}" with vnfx("shake")
    $ co.shifted = True
    $ co_advance(6)
    if _co_feel:
        "{color=#ff5fb8}[_co_feel]{/color}"
    co_you "\"Oh my {i}god{/i}.\""
    "The voice. Hers. Yours."
    show cg co_can_i onlayer cgl
    "Cal's stopped moving. He's looking down too. His cock slides out of your ass, and the head of it settles, hot and slick, against your brand-new cunt."
    co_cal "\"Can I?\""
    "\n{size=-5}{color=#ff8fa3}▸ Say yes in your own voice{/color}{/size}"
    jump co_first_vaginal

label co_first_vaginal:
    $ vn_enter(bg="co_bedroom", pc="delighted", pc_tag="co_pc", cast=[], cg="co_vaginal_open")
    show cg co_vaginal_open onlayer cgl
    co_you "\"Yes. Yes, yes, please, {i}yes{/i}—\""
    "The first yes that was ever really yours, and she says it four times to make sure."
    "He pushes in."
    vn_sfx "Shlk."
    show cg co_vaginal_mid onlayer cgl
    "It's nothing like anything. Tight and wet and so {i}deep{/i}, a stretch that goes all the way up inside you."
    "You watch him sink into you, inch after thick inch, because you can. You don't ask him to tell you what he sees. You're looking."
    co_cal "\"Look at you. Look at my {i}girl{/i}.\""
    co_you "{=co_hypno}“Fuck me.”{/=co_hypno}"
    "Filthy and delighted, your hands on your own breasts, your eyes on where he disappears into you."
    co_you "\"Ahh— {i}ahh{/i}— fuck my pussy, Cal, fuck it, I can see {i}everything{/i}—\"" with vnfx("shake")
    show cg co_vaginal_peak onlayer cgl
    "He does, and your talking gets worse, and better, and louder, until the whole building can hear the voice that's only yours now, coming apart on his cock with nothing at all round her neck."
    "Your hips meet him every stroke like they've always known how."
    show cg co_vaginal_cum onlayer cgl
    co_you "\"I'm coming— Cal— I'm {i}coming{/i}—!\"" with vnfx("flash")
    "You come watching, every second of it, clenching on him, crying out at the ceiling you can finally look away from."
    "He comes buried to the root, groaning, and you watch that too: his hips jerking against yours, the flood of it warm and deep inside you."
    "\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    jump co_ending

label co_ending:
    $ vn_enter(bg="co_bedroom", pc="content", pc_tag="co_pc", cast=[], cg="co_ending_box")
    show cg co_ending_box onlayer cgl
    $ achievement.grant("Chin Up")
    "The slim collar stays in its box on the pillow the whole night. You don't need it."
    "You don't need the mirror either. But now you can look, and the question is whether you will."
    menu:
        "The mirror in the hall, face to the wall."
        "Hang the mirror" (ending=True):
            jump co_epilogue_mirror
        "Leave it facing the wall" (ending=True):
            jump co_epilogue_wall

label co_epilogue_mirror:
    $ co.ending = "mirror"
    $ vn_enter(bg="co_hall", pc="delighted", pc_tag="co_pc", cast=[("co_cal", "soft")], cg="co_epi_mirror")
    $ vn_until(9)
    show cg co_epi_mirror onlayer cgl
    "You hang it in the morning, with Cal holding it level."
    "Then you stand in front of it, chin wherever you like, and look at all of you for as long as you want."
    "It takes a while.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump co_route_return

label co_epilogue_wall:
    $ co.ending = "wall"
    $ vn_enter(bg="co_bedroom", pc="delighted", pc_tag="co_pc", cast=[("co_cal", "soft")], cg="co_epi_wall")
    show cg co_epi_wall onlayer cgl
    "You leave it where it is, face to the wall. Some things are better described."
    co_you "{=co_hypno}“Tell me what you see.”{/=co_hypno}"
    "You tell Cal that night, and he does, and you watch.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump co_route_return
