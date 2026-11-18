## THE SOURCE: glutes' passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, rungs-late.twee), written as beats; the director scenes are
## in scenes.rpy. The original is in catalog/docs/routes/vn-original/glutes/. No numbers anywhere: no
## weights, weeks, doses or inches; cup letters only. Nobody calls Brady a woman or a girl.

## ---- the opening (Glutes Opening) -------------------------------------------------------------

label gl_opening:
    $ gl.fit = "gym"
    $ vn_enter(bg="gl_kitchen", pc="cheerful", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg="gl_program")
    show cg gl_program onlayer cgl
    "The program goes up on the fridge with a magnet on every corner, because Garrett doesn't do anything halfway."
    "You stand in the kitchen of the Domus Street two-bed in your tank top and gym shorts, a protein shake in one hand, reading it. Training split. Meals. Steps. Cardio. Sleep. Posing, later. Every line in Garrett's square capitals. At the bottom, underlined twice: {b}SHOW.{/b}"
    hide cg onlayer cgl
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Your first show. Starting now.\""
    "Rinsing his shaker behind you."
    gl_you "\"Starting {i}now{/i}.\""
    "You can't stop grinning. You flex at the fridge. Your reflection flexes back in the oven door: wide shoulders, a decent chest, a waist you're quite proud of, legs you mostly hide in shorts. Men's Physique. Obviously. Shorts hide the legs."
    gl_you "\"Look at that V-taper. That's a {i}stage{/i} V-taper.\""
    gl_garrett "\"That's a starting point.\""
    "He's dark and dry and built like a coat hanger made of cable, and the best coach in the gym, whatever anybody else in the gym thinks. He writes your program. He takes your check-in photos. He picks up the mail."
    "Prep means no going out, no drinking and no dating for the whole run of it, and the two of you solved that problem a long time ago and have never once talked about it since."
    gl_garrett "\"Check-ins are Sundays. Same corner, same lamp, same three poses. Photos Sunday.\""
    gl_you "\"Photos Sunday.\""
    gl_garrett "\"Shave everything before.\""
    gl_you "\"Everything everything?\""
    "He looks at you over the shaker. You laugh. Of course everything. Competitors shave. Every pro you follow is smooth as a plate."
    gl_you "\"Everything. Let's {i}go{/i}.\""
    "You drain the shake, and slap the fridge right on the word SHOW."
    hide gl_garrett
    show cg gl_shelf onlayer cgl
    "Down the hall the bathroom door's open, and on the shelf over the sink sits the pharmacy box, label facing out, where it's sat every week for years. Sunday's your shot day. Sunday's check-in day now, too. Sundays are going to be {i}busy{/i}."
    "You can't wait.\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 8))
    jump gl_one_shot

## ---- CHECK-IN 1, BASELINE (Glutes One Shot, One Shave, One Photos) -------------------------------

label gl_one_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_shot_1")
    "Sunday. Shot day. Check-in day. {i}Prep{/i} day."
    show cg gl_shot_1 onlayer cgl
    "You're at the bathroom counter in a towel with the tap running hot and your bleached platinum crop still sticking up from the shower, and your hands already know the whole thing. You've done it every Sunday for years. You could do it asleep. Some Sundays you nearly have."
    show screen gl_box(GL_LABEL["old"])
    "The label's right there, facing out, perfectly legible in the bathroom light. You don't read it. You never have. Reading was never part of the routine."
    "Cap off, fresh pin, draw to the usual line by feel, in, push, out, bandage, flex. The delt pops under the plaster. Lovely."
    hide screen gl_box
    gl_you "\"Prep. Day {i}one{/i}.\""
    "You point at the mirror. You drop the towel and get in the shower and turn it up as hot as it goes, and stand under it with your eyes shut, talking yourself through your whole peak week."
    hide cg onlayer cgl
    vn_sfx "Clink."
    "Somewhere behind the water, a clink from the shelf."
    "When you step out, everything's where it was. Box, label out. Razor. Foam."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Shave-down. I'll do your back.\"\n{size=-5}{color=#ff8fa3}▸ Open the door{/color}{/size}"
    $ vn_pass(10)
    jump gl_one_shave

label gl_one_shave:
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[("gl_garrett", "coaching")], cg="gl_shave")
    "Garrett comes in with his sleeves rolled and a fresh razor and the look he gets at the squat rack when somebody's about to do something stupid with their knees."
    gl_garrett "\"Arms up. Face the wall.\""
    show cg gl_shave onlayer cgl
    "You do the front yourself: legs, quads, the inside of the thighs, the abs, the trail, the pits, all of it, short strokes with the grain, foam and rinse. He does the back. His palm runs foam up your spine and the razor follows it, quick and sure, and then down, over the top of your glutes, into the crease."
    gl_you "\"You're doing that on purpose.\""
    gl_garrett "\"You want hair in your rear relaxed?\""
    gl_you "\"{i}No.{/i}\""
    gl_garrett "\"Then squeeze. Good. Heel up on the bath. Other side.\""
    "It takes a while. He doesn't miss a single hair, because he's Garrett. And when he towels you off and steps back, and you turn to the mirror—"
    show cg gl_lines onlayer cgl
    gl_you "\"{i}Look at those LINES—!{/i}\""
    $ gl_body(1)
    "{color=#ff5fb8}You're smooth. All over. Every bit of you, chest to ankles, slick and bare and gleaming under the bathroom light like somebody's oiled you for a stage already. You twist round to see your back in the mirror, and there it is, the whole map of it, every muscle with a hard bright edge on it.{/color}"
    gl_you "\"Oh, that's {i}separation{/i}. Garrett. Garrett, look at the {i}separation{/i}—!\""
    gl_garrett "\"I'm looking.\""
    gl_you "\"I look like a {i}diagram{/i}—!\""
    "{color=#ff5fb8}You rub your own pecs, your own belly, the backs of your own thighs, and your skin feels it twice as much as it used to. Your lips are tingling from the aftershave, and you can't stop licking them. And your grip knows his rhythm now; it knows it before you've thought about it.{/color}"
    gl_garrett "\"Good starting point.\""
    show cg gl_floor onlayer cgl
    "He drops the towel, and you're both kneeling on the bath mat before either of you has said anything about it, because that's how it goes and it always has."
    "His cock's already up. Yours gets there the second his hand's on it. He holds you the way he holds a bar, thumb wrapped, no wasted grip, and you take him the same way, and you both start stroking at the same tempo, because of course you do."
    gl_you "\"So peak week. Carbs back in on the Thursday?\""
    gl_garrett "\"Wednesday night. Water stays high till Friday.\""
    gl_you "\"Sodium?\""
    gl_garrett "\"Don't touch the sodium. Grip. Don't lose the grip.\""
    "His thumb rolls over the head of your cock and smears the precum down, and your hips jump."
    gl_you "\"I'm not losing the— {i}hhh{/i}— grip— posing when?\""
    "You twist on the upstroke the way he likes, and he breathes out through his nose, which from Garrett is a scream."
    gl_garrett "\"Later. You're not ready to pose.\""
    gl_you "\"I'm {i}so{/i} ready to pose— {i}ahh{/i}— look at me— I'm a {i}diagram{/i}—\""
    vn_sfx "Shlk. Shlk. Shlk."
    gl_garrett "\"Tempo.\""
    gl_you "\"Tempo, {i}tempo{/i}— oh fuck, Garrett— keep the tempo— I'm—\""
    show cg gl_floor_cum onlayer cgl
    "You go first. You always go first. You come all over his fist and your own belly, hard, shouting at the shower curtain, and he milks you through it till you're squirming, and then he goes, with one short grunt, across your chest and your smooth abs." with vnfx("flash")
    "You look down at yourself, glazed, gleaming, hairless, and start laughing."
    gl_you "\"First entry in the folder. {i}Look{/i} at that.\""
    gl_garrett "\"Shower again. Then photos.\""
    menu:
        "Shower again. Then photos."
        "Again, properly":
            jump gl_shave_sex
        "Shower and photos":
            jump gl_one_photos

label gl_shave_after:
    $ vn_enter(bg="gl_bathroom", pc="flushed", pc_tag="gl_pc", cast=[("gl_garrett", "satisfied")], cg="gl_shave_sex_cum")
    "He comes again, across your belly this time, and says \"Good,\" like you've hit a depth."
    gl_garrett "\"Shower. {i}Now.{/i}\"\n{size=-5}{color=#ff8fa3}▸ Shower and photos{/color}{/size}"
    jump gl_one_photos

label gl_one_photos:
    $ gl.fit = "suit"
    $ vn_pass(20)
    $ vn_enter(bg="gl_lamp", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg=None)
    show bg gl_lamp onlayer bgl
    "The corner of the living room. The lamp, which nobody moves. The board shorts, which Garrett hands you and you pull on and he pulls the drawstring of, hard, one tug, and ties off."
    gl_you "\"Men's Physique. Shorts hide the legs.\""
    gl_garrett "\"Shorts hide the legs.\""
    "He lifts his phone."
    show cg gl_checkin_1_front onlayer cgl
    "{i}Front relaxed.{/i} Lats out, abs tight, the shorts riding just low enough."
    vn_sfx "Click."
    show cg gl_checkin_1_rear onlayer cgl
    "{i}Rear relaxed.{/i} You turn. You spread your back. You squeeze your glutes through the board shorts so hard your calves shake."
    vn_sfx "Click."
    show cg gl_checkin_1_side onlayer cgl
    "{i}Side chest.{/i} Arm across, fist in palm, push."
    vn_sfx "Click."
    show cg gl_checkin_1_rear onlayer cgl
    gl_you "\"Let me see the rear relaxed. Let me {i}see{/i} it— oh, that's a {i}back{/i}. That's a stage back. I'd buy a ticket to that back.\""
    "You grab his phone. Your back, wide and bare and shining, every edge sharp under the lamp. And under the shorts, a nice hard pair of glutes."
    gl_garrett "\"Good starting point.\""
    gl_you "\"I look leaner already. Garrett. Do I look leaner already? Is that the shave?\""
    gl_garrett "\"That's just prep.\""
    "He writes the card, and hands it to you. You read it out loud, every line, like you're on a stage already."
    hide cg onlayer cgl
    show screen gl_card(1)
    gl_you "\"Baseline. {i}Baseline.{/i}\""
    "You announce it to the living room."
    hide screen gl_card
    "You stick it on the fridge under the program. Then you stand in front of it in the board shorts with your hands on your hips and read it again, the way some people read their horoscope. {i}Men's Physique.{/i}"
    "It's the class you've wanted since you first walked into a gym and saw a guy on a poster with a waist like a wasp and shorts like a sail. You can see yourself on that poster."
    gl_you "\"Shorts hide the legs.\""
    "Fondly. You give your own ass a slap through the board shorts on your way to bed."
    "The rest of the week is the program. Train when he says. Eat what he says. Sleep. The shave doesn't grow back, and you don't miss it.\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 8))
    jump gl_two_shot

## ---- CHECK-IN 2, THE CUT (Glutes Two Shot, Garage, Mack, Car, Laser, Check-in) -------------------

label gl_two_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_shot_2")
    "Sunday. Grey sky through the bathroom window. Towel, tap, counter."
    show cg gl_shot_2 onlayer cgl
    show screen gl_box(GL_LABEL["box"])
    "Same box. Same shelf. Same three motions: swab, the usual line, the delt. You don't even look at your hands; you're looking at your own smooth chest in the mirror, because you can't stop."
    hide screen gl_box
    gl_you "\"Still nothing. Not one hair. All week.\""
    "You run a palm down your shin."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Base coat today. Mack's this morning. You build the colour.\""
    "From the kitchen. You knew that. Everybody knows that. You don't turn up at a show white as a fridge and spray it all on the morning of. You build it.\n{size=-5}{color=#ff8fa3}▸ Down Domus Street to Mack's garage{/color}{/size}"
    $ vn_pass(60)
    jump gl_garage

label gl_garage:
    $ vn_enter(bg="gl_garage", pc="cheerful", pc_tag="gl_pc", cast=[("gl_mack", "grin")], cg=None)
    show bg gl_garage onlayer bgl
    show gl_mack grin at vn_cast_slot
    "Mack's garage door is up. Inside: a folding booth like a shower curtain on a frame, a tarp on the concrete, a radio playing something with a lot of saxophone, and Mack himself, ginger and freckled and grinning, snapping on a pair of gloves."
    gl_mack "\"{i}Lowry{/i}. The roommate's project. Get your kit off, hot-ass, I haven't got all day. I've got all {i}morning{/i}, but not all day.\""
    "He reads it off his phone like it's a headline. You strip right there with the door up and step onto the tarp in nothing, because this is just a thing that happens to competitors. Mack doesn't blink either."
    gl_mack "\"I have seen {i}everything{/i}. Arms up.\""
    hide gl_mack
    show cg gl_booth onlayer cgl
    vn_sfx "Fsssht."
    "It's cold. Then it isn't. He sprays you in long even passes, chest, belly, the fronts of your legs, and talks the whole time: about the booth, about a bodybuilder who sneezed mid-coat, about a bloke on the next street who wants his whole back done in stripes, which he won't do, on principle."
    "Then he puts the can down and starts working it in with his gloved hands, and he doesn't stop talking, and he doesn't stop working."
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Hold still, you'll streak.\""
    $ gl_body(2)
    "{color=#ff5fb8}Under his palms your skin goes {i}soft{/i}. Not soft like a towel. Soft like butter left out. His glove slides down your side and it's like your whole side is the inside of your wrist, and you hear yourself make a noise you've never made in a garage before.{/color}"
    gl_you "\"Oooh. {i}Ohh{/i}— that's— Mack, is the tan supposed to feel like {i}that{/i}—?\""
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Takes beautifully. Look at that. No lines, no patches, even as you like. Turn round.\""
    show cg gl_booth_glutes onlayer cgl
    "You turn round, and he does your back, and the backs of your thighs, and then he gets to your ass and stops talking for a whole second."
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Well.\""
    "{color=#ff5fb8}You look over your shoulder. In the booth's little mirror your glutes are sitting up {i}higher{/i}: rounder, fuller at the bottom where they meet the hamstrings, a proper shelf to them under the tan.{/color}"
    gl_you "\"{i}Oh,{/i} hello— hello, look at that— that's the program, that's the {i}hinge{/i} work—! Is that a glute-ham tie-in? Mack. Is that a {i}tie-in{/i}?\""
    "You squeeze them for him. They squeeze {i}back{/i}, all the way through, heavy and hard."
    show gl_mack grin at vn_cast_slot
    gl_mack "\"That's a lot of tie-in.\""
    "He gives it a coat it doesn't strictly need. Your mouth's gone wet and loose, and you didn't do that. Your thighs keep pressing together, slick and strong, without asking you first."
    gl_you "\"Finally not covered in hair, that's all that is. Skin can breathe.\""
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Mm-hm.\""
    menu:
        "You file it, out loud."
        "It's the cut. It's just the cut.":
            $ gl.file2 = "cut"
        "It's the shave. Skin can finally breathe.":
            $ gl.file2 = "shave"
        "It's sleep. You've slept like a log all week.":
            $ gl.file2 = "sleep"
    jump gl_mack_tarp

## ---- rung 2: Mack on the tarp (Glutes Two Mack). Non-con, no flip. -------------------------------

label gl_mack_tarp:
    $ vn_enter(bg="gl_garage", pc="protesting", pc_tag="gl_pc", cast=[("gl_mack", "grin")], cg=None)
    show bg gl_garage onlayer bgl
    if gl.file2 == "sleep":
        gl_you "\"It's sleep. I've slept like a log all week. Skin repairs while you sleep. Everybody knows that.\""
    elif gl.file2 == "shave":
        gl_you "\"It's the shave. Skin can breathe now. It was suffocating under all that hair.\""
    else:
        gl_you "\"It's the cut. Lower body fat, everything's thinner on top. Skin included.\""
    gl_mack "\"Absolutely. Let it dry. Don't sit down, don't touch anything, don't touch {i}yourself{/i}.\""
    "He peels off his gloves. He's got a tent in his trackies the size of the booth. He isn't hiding it. He's been talking round it for half an hour."
    "You look at it. Then you look very hard at your own glossy brown arms, front and back, every last bit of you done, and wait for it to dry."
    gl_mack "\"Fair's fair. I did the whole back.\""
    gl_you "\"You— what?\""
    show cg gl_tarp_knees onlayer cgl
    gl_mack "\"The {i}whole{/i} back, hot-ass. Mind the tan. Don't put your hands down.\""
    "He's grinning. He gets a fist in your hair, gentle as anything, careful of the coat, and walks you down onto your knees on the tarp like he's posing you for the booth." with vnfx("shake")
    gl_you "\"Mack— the coat's {i}WET{/i}— I'm on a CUT, I didn't—\""
    "He's already got his trackies down. It's right there, thick and flushed and in front of your face. You've had one in your hand most Sundays for a long time. That's the arrangement. That's hands. Nobody ever said anything about your mouth."
    gl_mack "\"Hold still, you'll streak.\""
    "He holds your head still for you."
    gl_you "\"Mack, I'm not— {i}mmf{/i}—!\""
    show cg gl_tarp_mouth onlayer cgl
    vn_sfx "Shlrp."
    "It's heavy on your tongue and hot and salty, and you're trying to say {i}no{/i} round it, and your mouth goes and opens wider. You didn't tell it to. Your lips seal. You did {i}not{/i} tell them to."
    gl_mack "\"Oh, that's a pro. Look at that. That's a {i}pro{/i}.\""
    "His other hand lands in your hair too."
    gl_you "\"Mmf— {i}mmh{/i}— nnf— the {i}COAT{/i}—\""
    "You can't push him off without putting your hands on him, and you can't put your hands on him without wrecking the tan, so your hands just hang there, glossy and useless, while he takes you deeper, nose to his belly, and holds you there while he swears at his radio."
    vn_sfx "Glk. Glk. Glk."
    "He fucks your mouth slow and sloppy on your knees on the tarp, both fists in your hair, with the garage door wide open on Domus Street, and somebody walks past with their shopping and keeps walking."
    "Every slide of him over your tongue lands right in the middle of your brand-new mouth, and your cock's hard and bobbing over the tarp, and you hate it, and it doesn't care."
    gl_mack "\"I'm gonna— hot-ass, I'm—\""
    show cg gl_tarp_cum onlayer cgl
    "You try to pull off. He doesn't let you. He holds your head right where it is and comes on your tongue, in thick pulses, and there's nowhere for it to go, so you swallow, and swallow." with vnfx("flash")
    "He lets go of your hair. You sit back on your heels, gasping, mouth wet, the taste of him everywhere."
    gl_you "\"That was— that's {i}not{/i} what the base coat's for—\""
    gl_mack "\"Fair's fair.\""
    "Cheerfully. He wipes your bottom lip with his thumb."
    menu:
        "He's still in front of you."
        "\"Fair's fair,\" says Mack. He isn't finished.":
            jump gl_mack_sex
        "Mack lets you up":
            jump gl_car

label gl_mack_after:
    $ vn_enter(bg="gl_garage", pc="flushed", pc_tag="gl_pc", cast=[("gl_mack", "grin")], cg="gl_mack_sex_cum")
    "He goes again with one hand on the booth frame and the other in your hair, and the whole thing wobbles, and there's nowhere for it to go but down."
    hide cg onlayer cgl
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Ten minutes. Don't {i}touch{/i} anything.\""
    gl_you "\"I didn't {i}touch{/i} anything. That's the {i}point{/i}.\"\n{size=-5}{color=#ff8fa3}▸ Out to Garrett's car{/color}{/size}"
    hide gl_mack
    jump gl_car

## ---- rung 2: Garrett in the car (Glutes Two Car). Non-con, no flip; "Smudge it" is the break. ------

label gl_car:
    $ gl.fit = "gym"
    $ vn_pass(20)
    $ vn_enter(bg="gl_car", pc="cheerful", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg=None)
    show bg gl_car onlayer bgl
    "Garrett drives you across town to the laser clinic and parks in its little car park, early, engine off, rain spitting on the windscreen. You're on a towel in the passenger seat in your gym shorts and nothing else, sitting very, very carefully."
    gl_garrett "\"We're early.\""
    gl_you "\"The tan can't be smudged. All day. No sweat, no water, no friction, no contact with fabrics.\""
    "The way you'd read off a care label."
    gl_garrett "\"No contact.\""
    gl_you "\"No {i}contact{/i}. That's the whole day. Nothing touches it.\""
    "You look out at the rain, very firmly. You've still got Mack on your tongue."
    gl_garrett "\"No contact on the front.\""
    "He reclines his seat."
    show gl_pc protesting
    gl_you "\"The— what? Garrett, that's not what I—\""
    show cg gl_car_pull onlayer cgl
    "He takes you by the hips, both hands flat on the gym shorts where there's no tan to spoil, and pulls you across the gearstick onto him like he's racking a plate." with vnfx("shake")
    gl_you "\"Garrett— it's a {i}care label{/i}, it's not a— {i}hey{/i}—!\""
    "It's a clumsy business in a hatchback. You end up across him on your front, gym shorts dragged down round your knees, and you can't grab anything, because everything you'd grab is fabric."
    "His cock's out, slick with spit, and he pushes it between your thighs from behind, high up, under your balls, and your brand-new slick thighs close round it. You didn't tell them to."
    gl_garrett "\"Squeeze. Don't lose the pinch.\""
    gl_you "\"I'm not squeezing— that's not a {i}squeeze{/i}— that's just my {i}legs{/i}— {i}ahh{/i}—\""
    vn_sfx "Slp. Slp. Slp."
    "He starts moving. His cock drags between your thighs and bumps the back of your balls every stroke, and the seat creaks, and you try to push up off him, and his hands land on your hips to hold you still. Right on the tan."
    gl_you "\"The— {i}Garrett{/i}— the tan—\""
    show cg gl_car_thumbs onlayer cgl
    gl_garrett "\"Hold still.\""
    "His thumbs sink into the base of your glutes, and the tan goes: two perfect thumbprints."
    gl_you "\"The TAN— that's {i}contact{/i}, Garrett, that's all contact, you said— {i}ahh{/i}—!\""
    "He doesn't say anything. He just keeps going, and the next noise out of you is so loud the windscreen fogs."
    "Your thighs are rubbing, slick and burning, and every thrust of him through them pushes your own cock against the gearstick cover, and you're leaking all over the towel. You don't want to be. It doesn't care."
    gl_garrett "\"Squeeze. {i}Squeeze.{/i}\""
    gl_you "\"Smudge it— smudge it, it's {i}fine{/i}, Mack can— {i}ahh{/i}— Mack can touch it up— don't stop— don't you {i}stop{/i}—!\""
    "You hear yourself go."
    show cg gl_car_cum onlayer cgl
    "He comes between your thighs, hot and thick, and pulls back so it spatters across the backs of them and the curve of your ass, right over the base coat. You lie across him panting, sticky, staring at the glovebox." with vnfx("flash")
    gl_you "\"Protein. Topical. That's— it's basically topical.\""
    "To the glovebox, eventually, because it has to be something."
    "He's still half-hard against you. You try to climb back over to your own seat, and his hands come back to your hips, and the clinic's door opens across the car park and a receptionist looks out at the rain."
    menu:
        "His hands are back on your hips."
        "\"We're early,\" says Garrett.":
            jump gl_car_sex
        "Garrett checks the time":
            jump gl_laser

label gl_car_after:
    $ vn_enter(bg="gl_car", pc="flushed", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg="gl_car_sex_cum")
    "He pulls out from between your thighs and finishes across your ass, and rubs it into the tan with his thumbs, like he's working in a coat."
    gl_you "\"Mack's going to kill you.\""
    "To the windscreen, still breathing hard. Garrett hands you the towel and checks the time.\n{size=-5}{color=#ff8fa3}▸ In for the consult{/color}{/size}"
    jump gl_laser

label gl_laser:
    $ vn_pass(20)
    $ vn_enter(bg="gl_clinic", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_laser")
    show cg gl_laser onlayer cgl
    "The laser clinic smells of hand gel and cucumber water. The technician has a little lamp on a stalk, and you lie on her paper sheet in your gym shorts while she moves it over your shins, your thighs, your chest, your arms."
    "She switches the lamp off."
    gl_other "\"Honestly, you're basically done already.\""
    gl_you "\"Done?\""
    gl_other "\"There's nothing coming back. Nothing for me to treat. Whatever you're doing, keep doing it.\""
    "You sit up so fast the paper sheet tears."
    gl_you "\"So I don't have to pay for the {i}course{/i}?\""
    gl_other "\"No course.\""
    gl_you "\"That's— that's the {i}whole course{/i} I'm not paying for— that's {i}supplements{/i}. That's chicken for {i}ages{/i}. Garrett. {i}Garrett.{/i} I'm basically done already!\""
    "You're out of the chair, you're shaking her hand, you're nearly hugging her. Garrett, in the waiting room, turns a page of a magazine about boats.\n{size=-5}{color=#ff8fa3}▸ Home for the check-in{/color}{/size}"
    $ vn_pass(60)
    jump gl_two_checkin

label gl_two_checkin:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_lamp", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg=None)
    show bg gl_lamp onlayer bgl
    "The corner. The lamp. And Garrett holds out a pair of black posing trunks, which aren't board shorts."
    gl_garrett "\"Classic. It scores the glute-ham tie-in. You've got the tie-in.\""
    gl_you "\"I've {i}got{/i} the tie-in.\""
    "You pull them up, and they go up fine, and then they get to your ass and have to be {i}coaxed{/i}. You hook your thumbs in the waistband and wiggle. The seat goes on snug across the bottom, the black stretched glossy over the tan."
    gl_garrett "\"Seat's snug.\""
    "He writes it down."
    show cg gl_checkin_2_front onlayer cgl
    "{i}Front relaxed.{/i}"
    vn_sfx "Click."
    show cg gl_checkin_2_rear onlayer cgl
    "{i}Rear relaxed.{/i} The trunks have ridden up into a smile on both cheeks, and you can see exactly where Garrett's thumbs went in the car, two pale ovals at the base, and you don't care, because look at the {i}shape{/i} of it."
    vn_sfx "Click."
    show cg gl_checkin_2_side onlayer cgl
    "{i}Side chest.{/i}"
    vn_sfx "Click."
    gl_garrett "\"That's just prep.\""
    "When you ask him if your ass has always sat that high. He writes the card, and hands it over."
    hide cg onlayer cgl
    show screen gl_card(2)
    gl_you "\"Notes. {i}Glutes are finally responding.{/i}\""
    "You stop. You read it again."
    gl_you "\"{i}Glutes are finally responding.{/i} Finally. Garrett. {i}Finally!{/i} You wrote finally!\""
    "You turn round and look at them in the dark window. You turn back."
    gl_garrett "\"They're responding.\""
    hide screen gl_card
    "You put the card on the fridge under the program, under a magnet, with that line facing out, and you squeeze your own glutes in the posing trunks, and they're responding, they're {i}so{/i} responding, and you go to bed with your hand on one.\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 8))
    jump gl_three_shot

## ---- CHECK-IN 3, POSING (Glutes Three Shot, Chest, Gym, Posing) -----------------------------------

label gl_three_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_shot_3")
    "Sunday. Dark out. Rain on the way. Towel, tap, counter."
    show cg gl_shot_3 onlayer cgl
    show screen gl_box(GL_LABEL["box"])
    "Swab, the line, the delt. The box goes back on the shelf, label out, where it lives. You're humming. Posing starts tonight. Posing is the fun part. Posing is the part where you get to {i}show{/i} it."
    hide screen gl_box
    "You drop the towel to get in the shower, and catch yourself side-on in the mirror, and stop.\n{size=-5}{color=#ff8fa3}▸ Look again{/color}{/size}"
    jump gl_three_chest

label gl_three_chest:
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_chest_3")
    show cg gl_chest_3 onlayer cgl
    "{color=#ff5fb8}Your nipples are puffy. Not cold-puffy. {i}Puffy{/i}: swollen up into soft little cones on your pecs, pink and tender, and when you poke one, carefully, with one finger, it goes straight through you.{/color}"
    gl_you "\"{i}Hnn{/i}—!\""
    "{color=#ff5fb8}You poke the other one. Same again. Your knees nearly go. A soft little swell under each, an AA at most, sitting up on top of the muscle where nothing used to sit.{/color}"
    $ gl.chest = 3
    "And you know exactly what this is. Every man at the gym knows what this is."
    gl_you "\"Gyno. Estrogen's up. Body fat drops, the aromatase goes haywire, your estrogen spikes, bang, puffy nips. Textbook. It's an estrogen thing. I {i}know{/i} it's an estrogen thing.\""
    hide cg onlayer cgl
    show bg gl_kitchen onlayer bgl
    show cg gl_peas onlayer cgl
    "You go to the freezer and get the peas."
    gl_you "\"No more soy milk.\""
    "You announce it to the kitchen, pouring the carton down the sink. Garrett, at the table, eats his oats. You hold the peas to your chest with both hands and sigh with relief."
    gl_you "\"There. {i}Handled{/i}.\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Handled.\""
    "And it is. You decide it is. You never think about it again.\n{size=-5}{color=#ff8fa3}▸ Leg day{/color}{/size}"
    $ vn_pass(90)
    jump gl_three_gym

label gl_three_gym:
    $ gl.fit = "hoodie"
    $ vn_enter(bg="gl_platform", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "coaching")], cg="gl_squat")
    "You train in a hoodie, zipped to the chin, because of the peas. It's handled. You're just not going to have it on the gym floor."
    show cg gl_squat onlayer cgl
    "Leg day. The platform at the back by the mirrors, Garrett on the clipboard, the bar on your back."
    gl_garrett "\"Hips back. Sit into it.\""
    "You sit into it, and your glutes are {i}there{/i}: hard and round and stacked under you like a shelf, catching the bar's weight at the bottom of every rep and driving it back up. Every hip hinge is a gift."
    gl_you "\"Ohhh, that's {i}glute{/i}. That's all glute. Garrett. Feel that. {i}Feel{/i} that—\""
    "He puts his palm on your hip at the bottom of the next rep."
    gl_garrett "\"Glute.\""
    show cg gl_squat_mirror onlayer cgl
    "Between sets you stand sideways at the mirror in your hoodie with your gym shorts stretched across your ass and just look at it. The shorts used to hang. They don't hang now. They're full."
    gl_you "\"The hinge work. Every program says the hinge work takes time. And then one day it just— {i}lands{/i}.\""
    "A guy at the next rack, mid-curl, looks at your ass, and then at the ceiling, and finishes his set."
    gl_garrett "\"Posing tonight.\"\n{size=-5}{color=#ff8fa3}▸ Home for posing{/color}{/size}"
    $ vn_until(19)
    jump gl_three_posing

## ---- rung 3: posing goes over (Glutes Three Posing). MANDATORY; non-con, never flips. ------------

label gl_three_posing:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_living_mirror", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "coaching")], cg="gl_pose_rear")
    "Posing. The living room, the coffee table pushed back, the long mirror off the wardrobe door propped against the wall, and you in the black trunks and nothing else, oiled, under the lamp."
    gl_garrett "\"Rear pose. Feet. Turn. Open them, hold it, and breathe.\""
    show cg gl_pose_rear onlayer cgl
    "You turn your back to the mirror. Feet in. Lats open. You look back over your shoulder at yourself—"
    gl_you "\"Oh {i}fuck{/i}, that's the rear relaxed—!\""
    $ gl_body(3)
    "{color=#ff5fb8}Your glutes have {i}landed{/i}: two big hard round cheeks, high and full and sitting right up off the backs of your thighs, the black trunks stretched to a shine across them and riding up the middle. Under them your hamstrings, thick, swept, flaring out in a curve that comes all the way in again at the knee.{/color}"
    gl_you "\"Look at the {i}sweep{/i}— look at the hamstrings, Garrett, look at the tie-in—! I'm all {i}back end{/i}!\""
    "{color=#ff5fb8}Your hips move when you shift your weight now, and they keep moving after you've stopped. They've learned how to {i}open{/i}, how to tip back and give.{/color}"
    "{color=#ff5fb8}You glance down the front of the trunks to fix the pouch. There's not much to fix. Your cock's sitting smaller in there than it used to, tucked up soft and neat.{/color}"
    gl_you "\"Depletion. Low body fat does that.\""
    "You fix the pouch anyway, and turn back to the mirror, because the glutes are the story."
    gl_garrett "\"Again. Open them, hold it, and breathe.\""
    "You do it again. And again. He sets your hips with both hands, presses the small of your back, nudges your feet apart with his foot. His hands linger every time. He's checking the tie-in a lot."
    gl_garrett "\"Hold it. Hold it.\""
    "Right behind you. You hold it. He's hard against the back of your trunks. You can feel exactly how hard. In the mirror your face is pink under the tan."
    gl_you "\"Garrett. That's— you're on my—\""
    gl_garrett "\"Session's going over.\""
    show gl_pc protesting
    show cg gl_pose_aside onlayer cgl
    "He pulls the back of the trunks aside."
    gl_you "\"Garrett— that's not POSING— posing's {i}POSING{/i}—\""
    "His thumb's slick with posing oil. It presses at your hole, slow, and stays there, and you try to step forward and there's only mirror to step into."
    gl_garrett "\"Breathe. Open them, hold it, and breathe.\""
    "He doesn't change his voice at all."
    gl_you "\"That's my {i}ASS{/i}, that's not a pose, that's my— {i}hnn{/i}—!\""
    "His thumb slides in to the knuckle, and then out, and then it's two fingers, oil everywhere, working, and you're braced on the mirror with both palms and your forehead, watching your own glutes in the glass split round his hand."
    gl_you "\"{i}Ohhh{/i}— no— out— that's not on the {i}PROGRAM{/i}—\""
    gl_garrett "\"Feet. Lats. Good. There. That's where you hold it.\""
    "His fingers curl inside you, and something lights up behind your balls so bright you yelp at the mirror."
    gl_you "\"{i}There{/i}— don't— Garrett, what {i}is{/i} that, that's not a muscle I've {i}trained{/i}—\""
    gl_garrett "\"You're training it now. Breathe out. Don't brace. Let it open.\""
    "You don't let it open. It opens anyway. Your ass is so big in the glass that his hand looks small against it, and every time his fingers spread you, you watch it happen and moan out loud, and hate how it sounds."
    gl_you "\"Garrett— Garrett, I didn't {i}call{/i} for a spot— {i}rack{/i} it—\""
    gl_garrett "\"Hips back.\""
    "The fingers go, and the fat blunt head of his cock is there instead, pressing, and your hips tip back for it, and you did {i}not{/i} tell them to—"
    gl_you "\"No— not my— that's my {i}ASS{/i}—!\""
    "And he pushes."
    menu:
        "He's pushing in. The mirror's in front of you."
        "Hold the pose":
            $ gl.grab3 = "pose"
        "\"That's not POSING—\"":
            $ gl.grab3 = "posing"
        "Reach back for his wrist":
            $ gl.grab3 = "wrist"
    jump gl_three_sex

label gl_three_post:
    $ vn_enter(bg="gl_living_mirror", pc="flushed", pc_tag="gl_pc", cast=[], cg="gl_pose_after")
    if gl.grab3 == "wrist":
        "You got a hand back to his wrist, right at the start. He took it off without looking and put it flat on the glass beside your face, and held it there, and went on."
    elif gl.grab3 == "posing":
        "\"That's not POSING,\" you'd told him, right at the start, and he'd said \"Breathe,\" and gone on."
    else:
        "You held the pose. You don't know why. Your palms are still flat on the glass, and you can't make them come off it."
    show cg gl_pose_after onlayer cgl
    "You came untouched. You don't know exactly when. Somewhere around him telling you to breathe, your cock just went off in the pouch, hard and leaking and twitching, while you were still shouting {i}no{/i} at the mirror, and then not shouting no, and then shouting the rear relaxed."
    "He doesn't pull out yet. He stays in you, buried, his hands spread on your glutes, and looks at them in the mirror over your shoulder the way he looks at a check-in photo."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Breathe.\""
    "You breathe. Your whole seat rises and falls with it, heavy and slick, and he watches that too."
    gl_you "\"Prostate. That's— that was the prostate. That's just anatomy. Everybody's got one.\""
    "Hoarse, to the glass."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Again tomorrow.\""
    "You don't say anything to that. You're still filing the last thing. When he finally slides out of you, a noise comes out of you at the mirror that you'd never make on purpose."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"That was posing. Every night now.\""
    gl_you "\"That wasn't—\""
    "He's already writing it down."
    hide cg onlayer cgl
    "He lets you get your breath. Then he lets out the seat of the trunks with a seam ripper, because it's split down one side, and you stand under the lamp in them, still oiled, still leaking, for the photos."
    show cg gl_checkin_3_front onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_3_rear onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_3_side onlayer cgl
    vn_sfx "Click."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Post one. Let people see the work.\""
    menu:
        "Which one do you post?"
        "Post the rear relaxed":
            $ gl.posted = "rear"
        "Post the side chest":
            $ gl.posted = "side"
        "Post the front relaxed":
            $ gl.posted = "front"
    jump gl_three_comments

label gl_three_comments:
    $ vn_enter(bg="gl_couch", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg="gl_comments")
    if gl.posted == "side":
        "You post the side chest. It's a good side chest. The chest is puffy, a bit, but the arm's across it, and the angle's mostly hip anyway."
    elif gl.posted == "front":
        "You post the front relaxed. Clean, symmetrical, lats out, the trunks just showing at the sides."
    else:
        "You post the rear relaxed. Obviously. Look at it."
    show cg gl_comments onlayer cgl
    "It does numbers. You lie on the couch on your front in the split trunks with your phone and read every single comment out loud to Garrett."
    gl_you "\"{i}Those glutes are unreal.{/i} Thank you! {i}The shelf on that.{/i} It's the hinge work. {i}Bro what are you running for legs.{/i} Garrett's program. {i}Need that tie-in in my life.{/i} Me too, mate. Me {i}too{/i}.\""
    gl_you "\"They're all about the glutes. Every one of them. Garrett. Every single one is about the glutes. Is that weird? It's a bit weird.\""
    gl_garrett "\"That's just prep. Glutes are the story right now.\""
    "They {i}are{/i} the story right now. You read the next comment, and the next, and he writes the card while you're still reading, and hands it down to you on the couch."
    hide cg onlayer cgl
    show screen gl_card(3)
    gl_you "\"Figure. Shape over mass. Shoulders, waist, sweep.\""
    "You twist round to look at your sweep."
    gl_you "\"{i}Chest, watch it.{/i} I'm watching it. It's handled. {i}Posing nightly.{/i}\""
    hide screen gl_card
    "Posing nightly. Every night that week. Every night it goes over.\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 8))
    jump gl_four_shot

## ---- CHECK-IN 4, THE SUIT (Glutes Four Shot, Parcel, Kendra, Floor, Suit) ---------------------

label gl_four_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_shot_4")
    "Sunday. Sun on the bathroom tiles. Towel, tap, counter."
    show cg gl_shot_4 onlayer cgl
    show screen gl_box(GL_LABEL["box"])
    "Swab, the line, the delt, bandage, flex. You've stopped needing the mirror for it; you watch your glutes in it instead, side-on, while your hands do the rest."
    hide screen gl_box
    vn_sfx "Clack."
    "The letterbox goes. Garrett picks up the mail. He always picks up the mail."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Parcel. Your competition trunks.\"\n{size=-5}{color=#ff8fa3}▸ Rip it open{/color}{/size}"
    $ vn_pass(10)
    jump gl_four_parcel

label gl_four_parcel:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_kitchen", pc="protesting", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg="gl_parcel")
    show cg gl_parcel onlayer cgl
    "Proper competition trunks. Glossy. Stiff with newness. You step into them in the hallway and pull them up, and they come up your thighs fine, and then they meet your glutes and {i}stop{/i}."
    "You pull. You hop. You wiggle. They go on in the end, sort of, the way a sock goes on a ham. The seam across the back is cutting you in half. Two whole round cheeks are hanging out the bottom of them like they're trying to get away."
    gl_you "\"The {i}cut's{/i} wrong. They've cut the back wrong. Who cuts a back like that? There's no {i}room{/i} in it—\""
    hide cg onlayer cgl
    show gl_garrett dry at vn_cast_slot
    "Garrett has the catalogue open on the counter. He turns it round, turns a page, and taps."
    gl_garrett "\"Other page. That one's cut for your structure.\""
    "You look. It's the same catalogue, the same maker, the same glossy fabric. It just has more back in it. And a top. Tops are part of some sets. Everybody knows that."
    gl_you "\"Fine. Fine. Other page. But I'm eating the {i}shipping{/i} on this, Garrett. And the {i}seam{/i}. Who signs off a seam like that?\""
    "You peel the trunks off your ass with a noise like a plaster."
    gl_garrett "\"Order it express. Kendra's at the posing corner Wednesday. She'll want to see your turns.\"\n{size=-5}{color=#ff8fa3}▸ Wednesday{/color}{/size}"
    hide gl_garrett
    $ vn_pass(gl_to_weekday(3, 17))
    jump gl_four_kendra

label gl_four_kendra:
    $ gl.fit = "gym"
    $ vn_enter(bg="gl_posing_corner", pc="proud", pc_tag="gl_pc", cast=[("gl_kendra", "warm")], cg=None)
    show bg gl_posing_corner onlayer bgl
    show gl_kendra warm at vn_cast_slot
    "The posing corner behind the curtain, late in the afternoon: the long mirror, the square of carpet. Kendra Vickers is already there in her gym crop and leggings, blonde ponytail, a Bikini competitor a few shows deep, warm and blunt and twice as loud as you."
    gl_kendra "\"Okay, Garrett's prep. Turn for me.\""
    "She walks round you once. You turn for her: your rear pose, the one you've been drilling every night."
    gl_kendra "\"Okay. So that's fine. But your structure's going to show {i}way{/i} better if you learn the quarter-turns. Feet like this. Hips like this. Look back over the shoulder, not up. Let the glutes do the talking.\""
    show cg gl_turns onlayer cgl
    "She shows you. She plants one foot, cocks a hip, and turns her back to the mirror in one smooth twist, and her glutes catch the light in a way yours have only ever done by accident."
    gl_you "\"{i}Oh{/i}. Oh, that's a better angle.\""
    gl_kendra "\"Right? Your structure's made for it.\""
    "You try it. It's harder than it looks. Your hips don't want to stop. Your ass keeps going after the rest of you's arrived. Kendra puts a hand flat on your waist to show you where to stop."
    gl_kendra "\"Waist's tiny. That's good. That's what scores.\""
    "Matter-of-fact. In the mirror the front of your tank top is sitting out. Not puffy. Out. You touch your chest and it's soft and full and warm under your hand."
    gl_you "\"Holding water. The taper'll pull it. Garrett's got the sodium dialled in.\""
    gl_kendra "\"Oh, totally. Peak week takes all that right off. You'll be shocked. Honestly? Your glutes are the story.\""
    gl_you "\"{i}Glutes are finally responding{/i}. That's what he wrote. On the card. {i}Finally.{/i}\""
    gl_kendra "\"They really are.\""
    "She means it. She walks round you again, slower, and adjusts you without asking: your chin down a touch, your shoulders back, your weight onto the back foot. She lifts your ribcage with two fingers under your sternum, right where your tank top's sitting out."
    gl_kendra "\"Breathe up into here. Not down into your belly. Up. Lift it. Show it.\""
    "You breathe up into it. Your chest lifts, soft and full, and the tank top rides up on it."
    gl_kendra "\"Good. That's what they want to see. Again. Show me the turn.\""
    menu:
        "Show her the turn."
        "Snap it round, fast and sharp":
            $ gl.turn = "snap"
        "Slow it down and let the glutes roll":
            $ gl.turn = "roll"
        "Hold it at the back and look over your shoulder":
            $ gl.turn = "hold"
    jump gl_four_floor

label gl_four_floor:
    $ vn_enter(bg="gl_gym_floor", pc="proud", pc_tag="gl_pc", cast=[("gl_kendra", "coaching")], cg=None)
    show bg gl_posing_corner onlayer bgl
    if gl.turn == "snap":
        "You snap it round so fast you nearly give yourself whiplash, and your glutes land a whole beat after the rest of you, bounce, and settle."
        gl_kendra "\"Okay, you're a {i}natural{/i}.\""
    elif gl.turn == "roll":
        "You take it slow. You let your hips swing round and your glutes roll through the turn and arrive, heavy, last. Kendra presses a hand to her mouth."
        gl_kendra "\"Okay, {i}that's{/i} the turn.\""
    else:
        "You hold it at the back, glutes squeezed, and look over your shoulder the way she showed you. Kendra just nods, slowly."
        gl_kendra "\"Hold that on stage and they'll give you the class.\""
    gl_kendra "\"Quarter-turns. Every night. With your posing.\""
    hide gl_kendra
    show bg gl_gym_floor onlayer bgl
    show cg gl_kindness onlayer cgl
    "You walk out onto the floor afterwards glowing."
    "The guy who's spotted your bench for as long as you've trained here doesn't offer to load your bar. He just nods, very kindly, and goes back to his own set. {i}Respect{/i}, you think. He can see you're deep in prep."
    "At the front desk on the way out, the guy on the desk doesn't ask for your card. He smiles, and buzzes you through, and says \"Have a good one,\" softer than usual. {i}Respect{/i}."
    "On the stretching mats a lifter in a crop top glances up, and shuffles her mat over to make room for yours, and smiles at you like you're on the same team. You smile back. You {i}are{/i} on the same team. Team Prep."
    hide cg onlayer cgl
    gl_you "\"They're all being so {i}nice{/i}. Everyone. It's the prep. They can tell.\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"They can tell.\""
    "On the walk home. His phone buzzes."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Suit's landed.\"\n{size=-5}{color=#ff8fa3}▸ Home for the fitting{/color}{/size}"
    $ vn_until(19)
    jump gl_four_suit

label gl_four_suit:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_lamp", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "coaching")], cg="gl_suit_fit")
    "The parcel's on the counter, opened, and the suit's laid out on the tissue paper. Blue. Top and bottoms, because that's how the set comes. The set's the set."
    gl_garrett "\"Fitting.\""
    show cg gl_suit_fit onlayer cgl
    "The corner. The lamp. You step into the bottoms and pull them up, and you tie the top on behind your back because the set's the set, and you turn to the mirror—"
    gl_you "\"Oh, {i}that's{/i} a fit—!\""
    $ gl_body(4)
    "{color=#ff5fb8}The top's {i}full{/i}. Your chest sits up in it, soft and round and heavy, real handfuls, a B cup's worth in each triangle and the blue stretched tight over it. You bounce on your toes and it bounces with you.{/color}"
    gl_you "\"{i}Ahh{/i}— look at the {i}pump{/i} on that—!\""
    "{color=#ff5fb8}And your waist has come in. Your hands go to it on their own, and they nearly meet. Under it your hips flare out wide, and the bottoms are losing: the seat climbing up into your crack and your glutes coming out of the sides of it, enormous, round and tanned and gleaming under the lamp.{/color}"
    gl_you "\"Look at the {i}waist{/i}— look at the hip-to-waist, Garrett, that's {i}presentation{/i}—!\""
    show cg gl_checkin_4_front onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_4_rear onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_4_side onlayer cgl
    "{i}Side chest.{/i} You put your arm across. There's a lot more chest to put it across."
    vn_sfx "Click."
    hide cg onlayer cgl
    "Garrett writes the card and hands it over without comment."
    show screen gl_card(4)
    gl_you "\"Bikini. Glutes, waist, presentation. {i}Fit: the set's the set.{/i} Bust: B. {i}Hold the turns.{/i}\""
    hide screen gl_card
    "You look at yourself in the mirror, in the blue, with your chest sitting up and your ass coming out of the back of it."
    gl_you "\"That's just prep.\""
    "Garrett doesn't react."
    show cg gl_suit_turn onlayer cgl
    "You turn your back to the mirror and do Kendra's turn for him, and stop, and hold it, and look back over your shoulder, and your glutes are right there at his belt, and his hands land on them."
    gl_garrett "\"Rear relaxed. Open them, hold it, and breathe.\""
    "He's out of his joggers. He lays his cock down along the crack of your ass, over the blue string, and squeezes your cheeks together round it with both hands, and starts to move."
    show gl_pc protesting
    gl_you "\"The suit's {i}NEW{/i}, Garrett, it's not even— {i}hnn{/i}—\""
    vn_sfx "Slp. Slp. Slp."
    "He slides up and down between your glutes, slick with posing oil, his thumbs digging in. In the mirror over your shoulder: his cock vanishing between two huge tanned cheeks and sliding back out, the blue string pushed aside, your whole seat shaking."
    gl_garrett "\"Every check-in, you bring me a bigger target.\""
    "Low, behind you."
    gl_you "\"{i}Bigger{/i}— that's the {i}program{/i}, it's not a— {i}ahh{/i}— it's not a {i}target{/i}—\""
    "Your glutes clamp round him, hard, and he groans."
    menu:
        "His hands on your glutes. The mirror over your shoulder."
        "Hold the turn":
            jump gl_four_sex

label gl_four_after:
    $ vn_enter(bg="gl_lamp", pc="flushed", pc_tag="gl_pc", cast=[], cg="gl_four_after")
    show cg gl_four_after onlayer cgl
    "He pulls out of you and comes all over your glutes, across the blue, down the cleft, and you reach back and rub it in like posing oil."
    gl_you "\"Holding water. That's all the— {i}hhh{/i}— that's all the chest is.\""
    "Into the carpet."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Taper'll pull it.\""
    "He doesn't let you up. He tugs the bottoms aside again with one finger, and spreads you with the other hand, and you're so loose and slick you just open for him, and he sinks back in."
    gl_you "\"{i}Ahh{/i}— again— {i}same set{/i}— don't rack it, don't you {i}dare{/i} rack it—\""
    vn_sfx "Slap. Slap. Slap."
    "Your ass bounces back off his hips on every stroke. Your new chest swings in the blue top, heavy. Your cock, sitting smaller in the bottoms, is drooling all over the inside of the pouch, and nobody, not even you, so much as looks at it."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Hold the turn.\""
    gl_you "\"{i}Holding{/i}— I'm holding— Garrett, I'm {i}holding the turn{/i}—!\""
    "He gets a fistful of the blue string at the back of the bottoms and pulls, like reins, and your whole ass rolls up to meet him, and you see it happen in the dark window. It's the best rear relaxed you've ever seen."
    gl_you "\"Look at it. Garrett— {i}Garrett{/i}— look at the {i}seat{/i} on it— keep {i}going{/i}— {i}more{/i}—\"\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 8))
    jump gl_five_shot

## ---- CHECK-IN 5, PEAK WEEK (Glutes Five Shot, Bag, Turns, Tan): consensual from here ------------

label gl_five_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_shot_5")
    "Sunday. Peak week. Towel, tap, counter."
    show cg gl_shot_5 onlayer cgl
    show screen gl_box(GL_LABEL["box"])
    "Swab. The usual line. The delt. You're so good at this now you could do it in the dark with your eyes shut, singing, which you are: the singing, at least, at the top of your voice."
    hide screen gl_box
    gl_you "\"Peak {i}week{/i}. Carbs back in Wednesday night. Water high till Friday. Don't touch the sodium.\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Don't touch the sodium.\""
    "Through the door.\n{size=-5}{color=#ff8fa3}▸ Pack your gym bag{/color}{/size}"
    $ vn_pass(15)
    jump gl_five_bag

label gl_five_bag:
    $ gl.fit = "gym"
    $ vn_enter(bg="gl_bedroom", pc="proud", pc_tag="gl_pc", cast=[], cg="gl_bag")
    "You tip your gym bag out on the bed and start getting dressed for the gym. Gym shorts. Your {i}good{/i} gym shorts. You step into them and pull them up, and they come up as far as the tops of your thighs, and stop."
    show cg gl_bag onlayer cgl
    "{color=#ff5fb8}Your thighs have {i}arrived{/i}. They're huge. They press together all the way up, thick and soft and smooth and tanned, and when you take a step they rub, slick, all the way along the inside, and it feels so good you take another step just to feel it again.{/color}"
    "{color=#ff5fb8}And above them your glutes are bigger than they were on Wednesday. Bigger than they were {i}last night{/i}. Two great round heavy cheeks sitting up off the backs of your thighs, so full they wobble when you so much as breathe.{/color}"
    gl_you "\"{i}Oh{/i}— oh, look at the {i}seat{/i} on that—!\""
    "You try the old training shorts. Nope. The old joggers. They go up over your ass like cling film over a melon. The spare posing trunks from the first week laugh at you from the bottom of the bag."
    hide cg onlayer cgl
    gl_you "\"Nothing fits. {i}Nothing in my bag fits.{/i}\""
    "To Garrett, in the doorway, triumphant, in the joggers."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Good.\""
    gl_you "\"That's a good problem! For my division, that's the {i}best{/i} problem!\""
    menu:
        "You file it, out loud."
        "It's the carbs going back in. Glycogen.":
            $ gl.file5 = "carbs"
        "It's the water. The water's going in the muscle.":
            $ gl.file5 = "water"
        "It's the program. The program's working.":
            $ gl.file5 = "program"
    $ vn_pass(60)
    jump gl_five_turns

label gl_five_turns:
    $ gl.fit = "bra"
    $ vn_enter(bg="gl_posing_corner", pc="proud", pc_tag="gl_pc", cast=[("gl_kendra", "coaching")], cg=None)
    show bg gl_posing_corner onlayer bgl
    show gl_kendra coaching at vn_cast_slot
    if gl.file5 == "water":
        gl_you "\"It's the water. It's going in the muscle. That's what peak week's for.\""
    elif gl.file5 == "program":
        gl_you "\"It's the program. Garrett's program. It just works.\""
    else:
        gl_you "\"It's the carbs. Glycogen. Everything's filling out.\""
    gl_kendra "\"Totally. Here. For the taper. You don't want it bouncing all over the place when you're trying to hit your turns.\""
    "She hands you a sports bra out of her bag."
    gl_you "\"That's sensible.\""
    "You put it on under your tank, and it is. Everything's {i}held{/i}. You do a test hop. Nothing moves that shouldn't."
    gl_kendra "\"The quarter-turns. From the top.\""
    show cg gl_turns_last onlayer cgl
    "Front. A quarter. Side. A quarter. Back, and the hold, and the look over the shoulder, and your glutes arrive a beat after you, enormous, and settle. She doesn't let you off a single one. She's never soft about it."
    "Then she stops, and looks at you in the mirror for a long second."
    gl_kendra "\"You're going to do well.\""
    "She means it. You go so pink under the tan you can feel it in your ears."
    gl_you "\"Thank you. Thank you. Honestly. Thank you—\""
    gl_kendra "\"Hold your turns on stage.\""
    "She hugs you, sports bra to sports bra.\n{size=-5}{color=#ff8fa3}▸ Home for the show tan{/color}{/size}"
    hide gl_kendra
    $ vn_until(15)
    jump gl_five_tan

label gl_five_tan:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_kitchen", pc="asking", pc_tag="gl_pc", cast=[("gl_mack", "working")], cg="gl_tan_5")
    "Mack's booth is folded up in your kitchen with the tarp under it and the radio on the fridge, playing saxophone."
    gl_mack "\"Show tan. Coat on coat on coat. Kit off, hot-ass.\""
    "Kit off. Sports bra off. You step onto the tarp."
    gl_mack "\"{i}Well{/i}.\""
    show cg gl_tan_5 onlayer cgl
    vn_sfx "Fsssht."
    $ gl_body(5)
    "{color=#ff5fb8}He goes down the front of you in long even passes. He does your chest from the side and it {i}bounces{/i}, from the spray alone, two heavy soft tits swinging under the cold mist, and he lowers the can.{/color}"
    gl_mack "\"Arms up. Arms {i}up{/i}, I need to get the underside.\""
    "{color=#ff5fb8}Very professionally. You put your arms up, and your tits lift, full and round and heavy, and settle back, a C cup's worth each, brown and gleaming under the first coat with the nipples standing right up.{/color}"
    gl_you "\"{i}Ohh{/i}— they're— Mack, is it the spray, are they always this {i}sensitive{/i}—\""
    gl_mack "\"I've sprayed a lot of chests. I've sprayed a {i}lot{/i} of chests.\""
    "{color=#ff5fb8}He does the back. He gets to your ass and has to step back to fit all of it in the spray. It's {i}enormous{/i}: a shelf you could stand a drink on, and your thighs so thick under it they rub together all the way to the knee.{/color}"
    gl_you "\"The {i}seat{/i}— Mack, have you ever seen a seat like this on a {i}man{/i}—\""
    gl_mack "\"No. No I have not.\""
    "{color=#ff5fb8}Your lips feel full and soft under the tan. And when you glance down past your own chest, your cock's sitting there in the spray tiny now, soft, a little pink button of a thing in a smooth brown crotch.{/color}"
    gl_you "\"Depleted. Peak week. Everything's depleted.\""
    "Fondly. And you're on to your ass again in the same breath, because look at it."
    show gl_garrett dry at vn_cast_slot
    gl_mack "\"Okay. Professionally. I need to see how that holds up under pressure.\""
    "After another coat, he puts the can down, and unzips."
    gl_you "\"Under pressure.\""
    "Breathless. You look over at Garrett, leaning in the kitchen doorway with his arms folded and his joggers tented, watching the way he watches a squat."
    hide gl_garrett
    show cg gl_tan_tits onlayer cgl
    "Mack steps up onto the tarp. His cock's out, red and thick, and he lays it right down the middle of your chest, between your tits, hot against your sternum."
    gl_mack "\"For the tan. Professionally. I need to see if it transfers.\""
    gl_you "\"For the {i}tan{/i}.\""
    "You put your hands on the outsides of your own tits, and push. They close round him, all of him, soft and heavy and slick with the spray, and he groans at your kitchen ceiling like a man who's just seen his own bank balance."
    gl_mack "\"Oh, it {i}transfers{/i}. Oh, it transfers {i}everywhere{/i}—\""
    gl_you "\"Pump's in. Pump's {i}in{/i}, use it, Mack— {i}use{/i} it—\""
    menu:
        "What do you ask for first?"
        "Tits first, Mack. Do the tits.":
            $ gl.ask5 = "tits"
        "Garrett, behind. Mack, in front.":
            $ gl.ask5 = "behind"
        "Both of you. Now. Everything.":
            $ gl.ask5 = "both"
    jump gl_five_sex

label gl_five_folder:
    $ vn_enter(bg="gl_kitchen", pc="flushed", pc_tag="gl_pc", cast=[], cg="gl_five_after")
    if gl.ask5 == "behind":
        "\"Garrett— behind— Mack, in front, {i}in front{/i}—\" you'd begged, and they'd done exactly that, one at each end of you on the kitchen tarp, and you'd told them what to do the whole way."
    elif gl.ask5 == "both":
        "\"Both of you— {i}everything{/i}—\" you'd begged, and they'd given you everything, and you'd named every bit of it out loud as you got it."
    else:
        "\"Tits first— Mack, {i}do the tits{/i}—\" you'd begged, and he had, slow and slippery, before anybody did anything else."
    show cg gl_five_after onlayer cgl
    "It had gone on for ages. Oil everywhere: Mack had got the posing oil out \"to see how the coat held\" and then just poured it, and the kitchen tarp was a slick brown lake, and you'd skidded on it twice. The tarp's a ruin, and so's the tan."
    "You came untouched. Again. Somewhere in the middle of it your tiny cock went off in the oil on its own, while you were asking Mack, by name, to hold your tits together tighter, and nobody noticed, least of all you."
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Again from the top.\""
    "Cheerfully, shaking the can."
    hide cg onlayer cgl
    show bg gl_couch onlayer bgl
    "Later, re-coated and dry and on the couch on your front, because you can't sit on the tan, you get Garrett's phone and open the folder."
    show screen gl_folder
    "Every check-in. Same corner. Same lamp. Same three poses. You scroll it from the top, out loud."
    gl_you "\"Baseline. Board shorts. Look at me, hairy as a doormat. Shaved. There— the shave, that's the first entry, that's the lines coming through.\""
    gl_you "\"The cut. Base coat, that's why I'm brown. Skin's better, because the hair's gone, it can breathe. Glutes coming up— that's the hinge work. {i}Glutes are finally responding.{/i} He {i}wrote{/i} that.\""
    gl_you "\"Posing. Puffy nips, that's the estrogen thing, handled. Glutes— oh, {i}there{/i} they are. That's the program, landing.\""
    gl_you "\"The suit. That's water. Holding water in the chest, all of that's water, it comes off in the taper. Waist's down— that's the cut. Hips are just structure, you can't change structure.\""
    gl_you "\"And today. Depleted. Glycogen loaded. Peak week. That's just prep.\""
    "You get to the end. You've explained all of it. Every single change, filed, by variable, and every one of them correct."
    "You scroll back up to the top and do it again, faster, like a flipbook, and watch yourself change in the same corner under the same lamp: the board shorts, the trunks, the blue, the teal. The chest coming. The waist going. And the glutes, Sunday after Sunday, until by the bottom of the folder they're the whole picture."
    gl_you "\"That's a {i}progress{/i} post. That's a progress post if ever I saw one. The program, start to finish. Garrett, you should sell this program. Right?\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Right.\""
    "You scroll back. You can't help it. There's one you keep stopping on."
    menu:
        "Which one do you stop on?"
        "The rear relaxed from today":
            $ gl.stop5 = "rear"
        "The side chest from the suit fitting":
            $ gl.stop5 = "side"
        "The very first board shorts":
            $ gl.stop5 = "first"
    hide screen gl_folder
    jump gl_five_checkin

label gl_five_checkin:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_lamp", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg=None)
    show bg gl_couch onlayer bgl
    if gl.stop5 == "side":
        "The side chest from the suit fitting. Your arm across your chest, and your chest coming out over the top of your arm anyway. You zoom in on it. You zoom in on it for a long time."
    elif gl.stop5 == "first":
        "The very first board shorts. A nice back, hairy shins, a pair of glutes that looked like they were trying. You laugh at it so hard you nearly roll off the couch."
        gl_you "\"Look at that {i}beginner{/i} ass. Look at it {i}trying{/i}.\""
    else:
        "Today's rear relaxed. You put your thumb and finger on the screen and spread them, and the glutes fill it, and you just stay there, grinning, while Garrett reads the paper."
    show bg gl_lamp onlayer bgl
    "Then the new suit, which Garrett's had in a drawer: teal, top and bottoms, the seat already ruched. You put it on under the lamp, and it holds, just."
    gl_garrett "\"Seat's let out again.\""
    show cg gl_checkin_5_front onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_5_rear onlayer cgl
    vn_sfx "Click."
    show cg gl_checkin_5_side onlayer cgl
    vn_sfx "Click."
    hide cg onlayer cgl
    "He writes the card."
    show screen gl_card(5)
    gl_you "\"Wellness. Scores the lower body heaviest.\""
    "You look over your shoulder at the lower body. It's very heavy."
    gl_you "\"Bust: D. {i}Taper on schedule.{/i}\""
    hide screen gl_card
    "You put the card down, and pat your own seat, and sigh happily."
    gl_you "\"That's just prep.\""
    "Garrett says nothing. He hands you a protein shake and a hotel booking on his phone."
    gl_garrett "\"Show day. Next Sunday.\"\n{size=-5}{color=#ff8fa3}▸ Show day{/color}{/size}"
    $ vn_pass(gl_to_weekday(0, 6))
    jump gl_six_shot

## ---- SHOW DAY (Glutes Six Shot, Mirror, Registration, Backstage, Stage, Hotel) ---------------------

label gl_six_shot:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_hotel_bathroom", pc="proud", pc_tag="gl_pc", cast=[], cg="gl_shot_6")
    "Show day."
    show cg gl_shot_6 onlayer cgl
    "A hotel bathroom by the Convention Hall, all white tile and a buzzing strip light over the mirror. Your bag on the floor. Your show suit in its tissue paper on the towel rail. And the box, which travelled in the side pocket, out on the little glass shelf, label out, legible as anything under that light."
    show screen gl_box(GL_LABEL["box"])
    "You don't read it. You're reading your own reflection: the tan, dark and even; the shape of you, which you haven't stopped staring at since you woke up."
    hide screen gl_box
    "\n{size=-5}{color=#ff8fa3}▸ The mirror{/color}{/size}"
    $ vn_pass(10)
    jump gl_six_mirror

label gl_six_mirror:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_hotel_bathroom", pc="proud", pc_tag="gl_pc", cast=[], cg="gl_mirror_6")
    "You put the show suit on under the strip light. Purple. Crystals all over it, so it throws little bits of light round the bathroom when you breathe. And then you look."
    show cg gl_mirror_6 onlayer cgl
    gl_you "\"Oh. {i}Oh.{/i} Oh, {i}fuck{/i}—!\""
    $ gl_body(6)
    "{color=#ff5fb8}It all came in. The whole week of it, at once, overnight, and it's {i}massive{/i}.{/color}"
    "{color=#ff5fb8}Your chest: two big, soft, heavy, perfect tits, sitting up and out over the waist, a D cup each, the little crystal triangles of the top not even pretending to cover them. You lift them. They overflow your hands.{/color}"
    gl_you "\"Look at the {i}chest{/i}— look at the {i}side chest{/i} on that—!\""
    "{color=#ff5fb8}And behind you— you turn— your ass. It's enormous. It's the biggest thing in the room, two vast, round, gleaming cheeks that start right under your tiny waist and go out and out and down into thighs like pillars, and the crystal bottoms just vanish into it.{/color}"
    gl_you "\"Suck it, {i}Classic{/i}—! Suck it, Men's {i}Physique{/i}—!\""
    "{color=#ff5fb8}Your waist's gone to nothing between them. You put your hands round it and they meet. You turn to the side and the curve of you goes in, in, in, and then {i}out{/i}, so far out the mirror can't take it all.{/color}"
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Registration. Now, or we miss the line.\"\n{size=-5}{color=#ff8fa3}▸ Hoodie on, out the door{/color}{/size}"
    $ vn_pass(30)
    jump gl_six_registration

label gl_six_registration:
    $ gl.fit = "hoodie"
    $ vn_enter(bg="gl_hall", pc="cheerful", pc_tag="gl_pc", cast=[], cg="gl_line")
    show bg gl_hall onlayer bgl
    "The Convention Hall, early, already heaving. Banners. Tanned people in robes. A smell of oil and hairspray and nerves you could stand a spoon in."
    "The registration table has two queues. You join the short one, because it's short, and when you get to the front you give your name."
    gl_you "\"Lowry.\""
    show screen gl_roster
    "The volunteer with the clipboard runs her pen down the roster. Down. Down. She finds you. She looks at the roster, and then she looks at you, in your hoodie with your chest pushing the zip out and your ass behind you like a parked car, and she doesn't blink, and she points."
    gl_desk "\"Other line, hon.\""
    hide screen gl_roster
    gl_you "\"The— {i}that{/i} line? That line's {i}huge{/i}—\""
    gl_desk "\"Other line.\""
    "Kindly. She calls the next one."
    show cg gl_line onlayer cgl
    "You go to the other line. It's huge. It goes round a pillar. Everyone in it is tanned to a shine and wearing a robe, and nobody gives you a second look, because you look exactly like everyone else in it."
    gl_you "\"This is a {i}joke{/i}. We're going to be here all {i}morning{/i}. Who runs a registration like this? One table? For {i}this{/i} line? They should split it—\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Eat your rice cake.\""
    "Holding your bag. You eat your rice cake, and complain about the line all the way to the front. People nod along. Everyone in the line agrees the line is terrible. It's the friendliest you've ever felt in a queue."
    "At the front a different volunteer finds you on a different list, ticks you off without a flicker, and hands you a card to pin to your suit.\n{size=-5}{color=#ff8fa3}▸ Backstage{/color}{/size}"
    $ vn_pass(60)
    jump gl_six_backstage

label gl_six_backstage:
    $ gl.fit = "suit"
    $ vn_enter(bg="gl_backstage", pc="proud", pc_tag="gl_pc", cast=[("gl_mack", "working")], cg="gl_touchup")
    "Backstage is a corridor by the fire door with a row of booths down it, and the last booth along is Mack's, radio and all."
    gl_mack "\"Touch-up. Hoodie off, hot-ass. Arms up.\""
    show cg gl_touchup onlayer cgl
    vn_sfx "Fsssht."
    "One last coat, fast and even, all over, the darkest yet. Then he oils you, both hands: your shoulders, your back, your tits, thoroughly, your waist, and then he gets to your ass and stands back and just looks at it for a second like a man looking at a sunset."
    gl_mack "\"Best work I've ever done.\""
    "He oils it."
    hide cg onlayer cgl
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Sit. Stage face. You'll look like a ghost under those lights without it.\""
    "Kendra appears with a makeup bag the size of a toolbox. You sit, very carefully, on the very front of the stool."
    show cg gl_stage_face onlayer cgl
    "She does your face with quick sure fingers, talking the whole time about your turns: blush high on the cheekbones, a sweep of black on the lashes, and a deep red on your lips, which she blots, and does again."
    gl_kendra "\"Everyone wears it. Lights wash you out.\""
    gl_you "\"Everyone wears it.\""
    "Obviously everyone wears it. You've seen the photos. You pout at her hand mirror and your mouth is {i}huge{/i}, dark and glossy."
    gl_kendra "\"Hold your turns.\""
    "She squeezes both your hands.\n{size=-5}{color=#ff8fa3}▸ On stage{/color}{/size}"
    hide gl_kendra
    $ vn_pass(60)
    jump gl_six_stage

label gl_six_stage:
    $ vn_enter(bg="gl_stage", pc="proud", pc_tag="gl_pc", cast=[], cg="gl_stage_front")
    show cg gl_stage_front onlayer cgl
    "The lights. The heat. The panel, a row of shapes behind a table you can't see past the glare."
    "Front. You plant your feet and lift your chest, and your chest {i}lifts{/i}, and you hold it. Smile. Breathe."
    "Quarter-turn. Side. Hip cocked, tits out, waist in. Hold."
    show cg gl_stage_back onlayer cgl
    "Quarter-turn. Back. You plant, and twist, and hold, and look back over your shoulder, not up, exactly like Kendra showed you, and your glutes arrive a beat after the rest of you and {i}settle{/i}, enormous, gleaming, perfectly still, and somewhere out in the dark somebody whoops."
    "Side. Front. Every turn clean. Every hold steady. You don't wobble once."
    gl_other "\"Quarter-turn to the right.\""
    "You do it, and hold it, and they let you hold it. Back. You plant, and pop the hip, and let the glutes roll in last, and hold, and hold, and the voice doesn't call the next one for a long, long time."
    gl_other "\"Face the front.\""
    "You face the front. You've never been so pleased with your own feet."
    show cg gl_trophy onlayer cgl
    "They call the placings. They call your name, and you step forward, and you stand on the riser, and they hand you a trophy shaped like a gold figure mid-pose, and you hold it over your head, and the lights are so bright you can't see anything at all."
    "You hit every turn. That's the thing. You hit every single one.\n{size=-5}{color=#ff8fa3}▸ Back to the hotel{/color}{/size}"
    $ vn_until(21)
    jump gl_six_hotel

label gl_six_hotel:
    $ vn_enter(bg="gl_hotel_room", pc="asking", pc_tag="gl_pc", cast=[("gl_kendra", "warm")], cg="gl_hotel_kendra")
    "The hotel room, with the blinds open on the lights of the town, and the trophy on the nightstand, and all of you, and the show suit already halfway off you, oiled and glittering, on the bed."
    gl_you "\"I {i}placed{/i}. I {i}placed{/i}. In my first— Garrett, I {i}placed{/i}—\""
    hide gl_kendra
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"You placed.\""
    hide gl_kendra
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Celebration.\""
    "He shuts the curtain on one window, and leaves the other open."
    show cg gl_hotel_kendra onlayer cgl
    "Kendra's in her robe, kneeling up on the end of the bed. She puts one hand flat in the middle of your back and presses you down, face to the mattress, ass up, and holds you there."
    hide gl_garrett
    hide gl_mack
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Hold rear relaxed.\""
    gl_you "\"{i}Holding{/i}—\""
    "Garrett's behind you. His hands spread you open, both of them, so wide you feel the air on your hole, and you push back for him, shameless, wriggling, the crystal bottoms shoved off to one side."
    gl_you "\"Please— Garrett— {i}please{/i}, I placed, I {i}earned{/i} it—\""
    "The trophy's right there on the nightstand at the edge of your vision, gold and shining, a little figure mid-pose. You keep looking at it."
    hide gl_kendra
    show gl_mack grin at vn_cast_slot
    gl_mack "\"Look at that. Look at that, Garrett. That's my tan. That's my {i}best{/i} tan.\""
    hide gl_garrett
    hide gl_mack
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"That's a class winner.\""
    "Matter-of-fact. She pats it. It wobbles for a long time."
    "Mack's on his knees by your head with his cock in his fist, rubbing it on your dark red lips. Kendra's other hand slides under you and finds one of your nipples and {i}flicks{/i}."
    gl_you "\"{i}Ahh{/i}—!\""
    "And Garrett pushes in."
    menu:
        "Kendra's hand on your back. Garrett behind you."
        "Hold rear relaxed":
            jump gl_six_sex

## ---- THE ENDING, "Placed" (Glutes Six Season) ----------------------------------------------------

label gl_six_season:
    $ vn_enter(bg="gl_hotel_room", pc="flushed", pc_tag="gl_pc", cast=[], cg="gl_hotel_mack")
    "Nobody stops. Garrett just keeps going, slow and deep and steady, and you can hear it, wet and loud, and so can the open window. The show suit's bottoms are lost somewhere inside the curve of you. There's oil on the headboard, tan on every pillow in the room."
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Hold the turn.\""
    "You try. You plant your knees and arch your back and look over your shoulder at Garrett the way she taught you, and he drives in so hard your arms give out and you go face-first into the pillows, laughing, moaning, wrecked."
    gl_you "\"Again— {i}again{/i}— don't rack it— I placed, I {i}placed{/i}, I want {i}all{/i} of it—\""
    show cg gl_hotel_mack onlayer cgl
    "Mack rolls you half over and pushes your tits together with both oily hands and fucks between them, the fat head popping up under your chin every stroke, and you lick at it, and moan, and ask him for more, by name, loud enough for the open window."
    gl_you "\"Mack— {i}Mack{/i}— harder, use the {i}chest{/i}—\""
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Keep it, don't wipe it.\""
    "When he comes across your tits and up your neck and across your face. You don't wipe it. You couldn't. She's holding your wrists." with vnfx("flash")
    "Kendra lets go of your wrists to lick a streak of it off your cheek, businesslike, and then kisses you, hard, with it on her tongue."
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Prize for placing.\""
    gl_you "\"I {i}placed{/i}.\""
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"You placed. Chest out. Chest {i}out{/i}. They'll want to see that next season.\""
    "She goes back to your nipples, both of them now, rolling them, pinching, flicking, until you're squirming on Garrett's cock and squealing into the pillow."
    gl_you "\"Next {i}season{/i}— oh, fuck, Kendra— next season—\""
    show cg gl_hotel_pin onlayer cgl
    "Then you're face down again, and Garrett's back in you, slow, all the way, and Kendra's knee is in the small of your back, pinning you in the pose."
    show gl_kendra warm at vn_cast_slot
    gl_kendra "\"Hold rear relaxed.\""
    gl_you "\"{i}Holding{/i}—\""
    "She reaches under you and finds your tiny cock with two fingers, almost absently, while she pinches a nipple with the other hand, and you go off in a few flicks of her fingers, a sorry little ribbon on the sheet that nobody so much as looks at, while you scream into the mattress with Garrett buried in your ass." with vnfx("flash")
    "Mack's hard again. He kneels by your head. You open your mouth for him without being asked. Garrett leans over, still in you, and puts the card on the mattress in front of your face."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Read it.\""
    show screen gl_card(6)
    gl_you "\"{i}Mmh{/i}— show day— {i}Wellness{/i}— scored, placed— the show suit— bust— {i}mmf{/i}— E— {i}off-season starts now{/i}—\""
    "Round a mouthful of Mack, with Garrett fucking you in long slow strokes and Kendra's knee in your back."
    hide screen gl_card
    "Mack comes on your tongue. You swallow, and keep him in your mouth, and talk round him anyway, face in the mattress, glutes up, the trophy shining on the nightstand."
    gl_you "\"Off-season starts now— next season I'm bringing up my {i}chest{/i}, I already booked the show—\""
    "Garrett squeezes your thigh."
    show gl_garrett dry at vn_cast_slot
    gl_garrett "{b}\"That'll respond.\"{/b}"
    $ gl.ending = "placed"
    $ achievement.grant("That'll Respond")
    hide cg onlayer cgl
    "\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    call vn_night(8)
    $ vn_pass(gl_to_weekday(0, 9))
    jump gl_epilogue

## ---- the epilogue, the next Sunday (Glutes Epilogue, Stay, Go) ------------------------------------

label gl_epilogue:
    $ gl.fit = "nude"
    $ vn_enter(bg="gl_bathroom", pc="proud", pc_tag="gl_pc", cast=[], cg="gl_epi_shelf")
    "Sunday."
    show cg gl_epi_shelf onlayer cgl
    "The bathroom in the Domus Street two-bed. The steam on the mirror. Your trophy on the cistern, because there's nowhere else to put it. The box on the shelf, label out, where it always is."
    show screen gl_box(GL_LABEL["box"])
    "Swab, the usual line, the delt."
    hide screen gl_box
    "You flick the bandage on, flex at the mirror, and the mirror flexes back: the chest that fills the frame now, the waist you could lose a hand in, and behind you, filling the whole steamed-up bottom half of the glass, the glutes. {i}Your{/i} glutes. Placed, on a stage, under lights."
    gl_you "\"Off-season. Big plans.\""
    show gl_garrett dry at vn_cast_slot
    gl_garrett "\"Check-in's still Sunday.\""
    "From the kitchen. You grin. Of course it is. Then you look at your bag by the door, half unpacked from the hotel, and at the box on the shelf, and at the program on the fridge."
    menu:
        "The bag by the door. The box on the shelf."
        "Off-season with Garrett" (ending=True):
            jump gl_epilogue_stay
        "Take the box home" (ending=True):
            jump gl_epilogue_go

label gl_epilogue_stay:
    $ gl.epilogue = "stay"
    $ gl.fit = "gym"
    $ vn_enter(bg="gl_kitchen", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "satisfied")], cg="gl_epi_stay")
    show cg gl_epi_stay onlayer cgl
    "You unpack the bag. You put the trophy on the shelf beside the box, label out, both of them. You stick the new program on the fridge over the old one, a magnet on every corner. {b}OFF-SEASON.{/b} Underlined twice."
    gl_garrett "\"Food goes up. Volume goes up. Check-ins stay Sunday.\""
    "Reading it over your shoulder."
    gl_you "\"And the chest. We're bringing up the chest.\""
    gl_garrett "\"Bringing up the chest.\""
    "He pins the program flat with his palm."
    "Mack texts before lunch: a photo of his booth, folded, and {i}OFF-SEASON MAINTENANCE COAT? ;){/i} Kendra texts after: {i}don't you DARE lose those turns.{/i} You reply to both with the rear relaxed from the show, because you can."
    "That night, on the couch, Garrett's hand on the back of your thigh while you scroll the folder again, start to finish, you narrate the entire thing one more time, and he agrees with all of it.\n{size=-5}{color=#ff8fa3}▸ Out onto Domus Street{/color}{/size}"
    jump gl_route_return

label gl_epilogue_go:
    $ gl.epilogue = "go"
    $ gl.fit = "gym"
    $ vn_enter(bg="gl_hallway", pc="proud", pc_tag="gl_pc", cast=[("gl_garrett", "dry")], cg="gl_epi_go")
    "You pack the bag. The trophy goes in wrapped in your hoodie. The box goes in the side pocket, label out, because that's how it lives."
    gl_garrett "\"Taking the program?\""
    gl_you "\"I've got the program. It's {i}in{/i} me.\""
    "You tap your head. You tap your ass."
    show cg gl_epi_go onlayer cgl
    "He doesn't laugh. He does let you kiss him at the door, and squeeze his arse, and get a hand down the back of your shorts for the trouble, all of it in the hallway with the door open on Domus Street."
    gl_garrett "\"Check-ins are Sundays. I'll send the card.\""
    show cg gl_epi_go_shelf onlayer cgl
    "Your new bathroom has a shelf. The box goes on it, label out. Sunday, your phone buzzes with a card, the same format, the same three poses, and you read it out loud to an empty flat and grin the whole way through.\n{size=-5}{color=#ff8fa3}▸ Out onto Domus Street{/color}{/size}"
    jump gl_route_return
