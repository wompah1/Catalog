## The fortnight at Thornleigh House (main/days/finale.twee, rewritten straight in Ren'Py,
## 2026-11-11; the catalog's twee is kept verbatim in catalog/docs/routes/vn-original/venus/).
## Fourteen linear course days: Mia's knock at six, the call sheet in weekdays, the You/Them pair,
## then the day's beat (a rung scene on its rung's last day, a routine beat in between), then the
## night. The written scenes are scenes.rpy.

## ==== THE DAY MACHINERY =========================================================================

## Mia's knock, the call sheet, the two readings; on a rung's first morning the body lands.
label ve_morning(n):
    call vn_night(6)
    $ ve_day(n)
    $ ve.fit = "uniform" if ve.rung >= 2 else "own"
    $ vn_enter(bg="ve_twinroom", pc="neutral", pc_tag="ve_pc", cast=[("ve_mia", "neutral")])
    vn_sfx "Knock, knock, knock."
    ve_mia "\"Up, Chrissy! Shake's poured!\""
    $ _cs = ve_call_sheet(n)
    "The call sheet's under the door, printed in lavender. Somebody's drawn a heart over your name."
    "{color=#f3c969}CALL SHEET.{/color} {i}[_cs]{/i}"
    $ _rd = VE_READINGS[ve.rung]
    "{color=#ff9ed8}You:{/color} {i}[_rd[0]]{/i}   {color=#8fd3ff}Them:{/color} {i}[_rd[1]]{/i}"
    return

## ==== DAY 1: the sign, the form, the coach, intake (rung 1) =====================================

label ve_opening:
    $ vn_enter(bg="ve_danube", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_open_sign")
    "A sign in the Dollhouse window."
    "{color=#ff9ed8}VENUS & MARS. A fortnight's residential performer intensive. Coaching, nutrition, spa, one-to-ones. Country hotel. Course coach from this kerb at noon. Adults 21+. Pairs preferred.{/color}"
    ve_me "\"Simon. {i}Simon.{/i} Look at this.\""
    "Simon Hartley looks. He's twenty-three, glasses, reads the small print on everything. Best friends since you were both nineteen and pulling pints at the same bar."
    "He has never once let you sign anything unread."
    ve_simon "\"Performer. Intensive.\""
    ve_me "\"Porn, Simon. It's a {i}porn course.{/i}\""
    vn_sfx "Slap."
    "You slap the glass."
    ve_me "\"A fortnight in a hotel, and at the end you're {i}in{/i}. {i}Pairs preferred.{/i} That's us!\""
    ve_simon "\"Chris.\""
    ve_me "\"I'm twenty-two. I'm in my prime.\""
    "You rake a hand through your short red hair."
    ve_me "\"The face. The mouth. The attitude. I'm gonna be the guy, man. The lead. The one everybody watches.\""
    "Simon sighs. He's already lost."
    ve_simon "\"...Is there a form?\""
    show cg ve_open_form onlayer cgl
    "There's a form. Two clipboards on the Dollhouse counter, four pages each."
    ve_me "\"I'll do both. You'll read it and we'll miss the coach.\""
    ve_simon "\"I {i}want{/i} to read it—\""
    vn_sfx "Scribble scribble."
    "Over twenty-one: yes. Intense situations: yes. Select all that apply: ALL. Tick, tick, tick."
    "You don't read page four."
    ve_me "\"Done! Four minutes. Both of us.\""
    "The woman at the counter flips to your last page. Stops. Looks up at you, all soft and kind."
    ve_counter "\"Oh. Good for you, honey.\""
    vn_sfx "Stamp. Stamp."
    hide cg onlayer cgl
    ve_me "\"Hear that? {i}Good for you, honey.{/i} They can tell already. Star quality.\""
    "You crow it on the pavement."
    ve_simon "\"Tell {i}what{/i}?\""
    menu:
        "Bag the back seat of the coach":
            $ ve.mood = "swagger"
        "Take the window seat":
            $ ve.mood = "eager"
    $ vn_set_time(12, 0)
    $ vn_enter(bg="ve_coach", pc="grin", pc_tag="ve_pc", cg="ve_coach_ride")
    "The coach is full. Mars on the left: big shoulders, tank tops, knees wide. Venus on the right: slip dresses, sunglasses, perfect lipstick."
    if ve.mood == "swagger":
        "You take the whole back seat, arms spread, legs wide. Simon perches next to you with both bags on his lap."
    else:
        "You grab the window and press your face to it. Simon squeezes in with both bags on his lap."
    "A Venus girl turns round, looks at you, and smiles like she's proud of you. You wink. She giggles."
    ve_me "\"VIP.\""
    "A whisper."
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"She was being {i}nice{/i}, man.\""
    ve_me "\"That's what VIP {i}looks{/i} like.\""
    show cg ve_hotel_arrive onlayer cgl
    "Hedges. Fields. A long drive. A beige country hotel with a banner over the door."
    "{color=#f3c969}THORNLEIGH HOUSE WELCOMES VENUS & MARS.{/color}"
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"It looks like a wedding venue.\""
    ve_me "\"It looks like a {i}launch{/i}, bro.\""
    hide cg onlayer cgl
    jump ve_intake

label ve_intake:
    $ vn_pass(60)
    $ vn_enter(bg="ve_lobby", pc="grin", pc_tag="ve_pc", cast=[("ve_fiona", "neutral")], cg="ve_badge")
    "Two tables in the lobby. A steel-blue arch for Mars. Lavender doors for Venus."
    "Simon's badge is red. {color=#ff6b6b}MARS: SIMON HARTLEY, HE/HIM.{/color}"
    "Yours is purple."
    "{color=#c48cff}VENUS: CHRISTINE TALBOT, SHE/HER.{/color}"
    hide cg onlayer cgl
    ve_fiona "\"Miss Talbot? Welcome to Venus & Mars, darling! Lavender doors, just through there.\""
    "The coordinator beams at you: silver bob, shell-pink lips, a pink suit. Ms. Fiona, fifty-two, and not a flicker."
    ve_me "\"Thanks!\""
    "You hang it round your neck like a medal."
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Dude. Dude. You hit She/Her.\""
    "A whisper."
    vn_sfx "Tap tap."
    ve_me "\"That stuff's there to keep the posers out, man. I blew right through it. {i}Purple.{/i} Purple's the fast lane.\""
    "You flick the badge so it spins."
    "Simon opens his mouth. A Mars guy the size of a wardrobe claps his shoulder and drags him off."
    ve_simon "\"See you on the other side?\""
    ve_me "\"Don't get lost on the rookie tour!\""
    hide ve_simon
    "At the lavender doors, a tall girl with a throaty voice taps your badge with one nail."
    ve_girl "\"Cute badge, hon. You're braver than I was.\""
    ve_me "\"VIP.\""
    "She laughs like that's adorable."
    menu:
        "Swagger through the lavender doors":
            $ ve.mood = "swagger"
        "Wink at her on the way past":
            $ ve.mood = "wink"
    $ vn_pass(20)
    $ vn_enter(bg="ve_studio", pc="grin", pc_tag="ve_pc", cast=[("ve_fiona", "neutral")], cg="ve_mirror_room")
    "Meeting Room B: a ring of mirrors, a ring light on each, an orchid in a glass at every stool. A room full of women. All of them on their own."
    if ve.mood == "wink":
        "The throaty one takes the stool beside you. You wink in the mirror. She winks back, slow."
    else:
        "You take the stool in the middle. Middle's where the lead goes."
    ve_fiona "\"Welcome to the Venus track, ladies! Look in your mirror. Three words on your card. Not what you're working on. What you {i}adore{/i}.\""
    "The girl beside you writes {i}soft, glowing, ready.{/i} A blonde writes {i}curvy{/i} and underlines it twice."
    show cg ve_mirror_card onlayer cgl
    "A skinny freckled guy squints back at you from the mirror."
    "{color=#ff9ed8}{i}curious, bright, odd.{/i}{/color}"
    "Ms. Fiona collects them and gives your shoulder a squeeze."
    ve_fiona "\"Keep these first words. Well— {i}I'll{/i} keep them, darlings. You'll have them back at the wrap.\""
    hide cg onlayer cgl
    "Then posture. Chest up. Walk to the window and back while everybody watches."
    "You give them the swagger. It comes out swishy. Two girls giggle behind their hands."
    ve_fiona "\"Beautiful!\""
    show ve_mia neutral at vn_cast_slot
    "A curly-haired girl grabs your hand."
    ve_mia "\"You did {i}great!{/i} I'm Mia, twenty-four, totally terrified. And I'm doing your hair tomorrow. That's a crime, that is.\""
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"Holly. You're on the mat next to me. Don't hog the lube.\""
    "The one beside her, dark bob, sharp eyeliner, twenty-six."
    ve_me "\"Ladies.\""
    "With the grin. They grin back."
    $ vn_pass(30)
    $ vn_enter(bg="ve_studio", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")])
    "You hang back when the others go."
    ve_wade "\"Miss Talbot? How did the mirror feel?\""
    "Teal blouse. Pencil skirt. Honey-blonde coil, cat-eye glasses, a clipboard. {color=#5fd3c6}MS. WADE, VENUS INSTRUCTOR.{/color} Forty-one, and she stands like a dancer."
    ve_me "\"Honestly? Ready to dive in. Whatever gets me to the front of the line.\""
    "You roll your shoulders and give her your best stud look."
    ve_wade "\"You're progressing so quickly. I think you'd benefit from the advanced track. Spa. Nutrition. Bodywork. One-to-ones with me.\""
    ve_wade "\"It's entirely up to you, and nobody would think any less—\""
    "Softly, like she's moved."
    ve_me "\"Yes.\""
    ve_wade "\"...Yes?\""
    ve_me "\"Sign me up! Whatever you've got. I can take it.\""
    ve_wade "\"Oh, darling. That's so brave.\""
    vn_sfx "Scribble."
    show cg ve_postit onlayer cgl
    "She peels off a hot-pink Post-it and sticks it on your form. You read it upside down."
    "{color=#ff9ed8}COMPLETE FEMTRACK INTAKE CANDIDATE.{/color}"
    ve_me "\"Femtrack. Obviously. VIP onboarding, right?\""
    "Nodding hard."
    ve_wade "\"Exactly right. Spa 3B, after dinner. Just the two of us.\""
    "Her eyes are shining."
    "Out in the corridor, two Venus girls squeal under their breath."
    ve_girl "\"She's {i}here!{/i}\""
    hide cg onlayer cgl
    call ve_spa
    call ve_first_night
    jump ve_day2

## ==== DAYS 2-5 (rung 2) =========================================================================

label ve_day2:
    call ve_morning(2)
    $ ve_body(2)
    $ vn_enter(bg="ve_twinroom", pc="shocked", pc_tag="ve_pc", cg="ve_r2_mirror")
    "Mia tosses you a uniform: purple tank top, purple gym shorts. You pull it on, catch the mirror, and stop."
    "{color=#ff9ecb}Your skin's {i}glossy{/i}.{/color} Your nipples have gone puffy and pink, poking right out through the tank. When the fabric drags over them— {i}zing{/i}, straight to your toes."
    "Your waist's pinched in a little."
    "You turn round. The shorts are snug over your butt. Rounder. A little peach where there used to be nothing."
    "You cup your chest through the tank and squeeze. The puffy nipples squish under your palms."
    ve_me "\"{i}Hnn{/i}— fuck— they're so {i}sensitive{/i}—!\"" with vnfx("shake")
    ve_me "\"Glow-up.\""
    "You tell the mirror, and flex."
    hide cg onlayer cgl
    $ vn_enter(bg="ve_lawn", pc="neutral", pc_tag="ve_pc", cast=[("ve_mia", "neutral")], cg="ve_yoga")
    "Dawn yoga on the back lawn. The whole Venus cohort in purple, butts in the air."
    ve_mia "\"Hips up, Chrissy! Breathe!\""
    "Every time the tank drags over your nipples you wobble. {i}Zing.{/i}"
    "Across the lawn, Mars does relays, shirtless, roaring. Simon runs at the back in his glasses. You wave. He runs into a cone."
    $ vn_enter(bg="ve_dining", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_shake_cup")
    "Then the shake table. Pink blenders. A row of cups, already poured, pale pink and frothy."
    "Ms. Wade picks out a cup with your name on the lid and holds it out, beaming."
    ve_wade "\"Especially you, honey. So brave, yesterday.\""
    menu:
        "Down it in one":
            vn_sfx "Gulp gulp gulp. Slam."
            "Head back. One go. The table cheers."
        "Raise it to the table first":
            $ ve.extra += 1
            ve_me "\"To Venus!\""
            vn_sfx "Gulp gulp gulp."
            "The whole table toasts you back."
    "Thick. Sweet. Then something salty underneath that coats your tongue and stays there all day."
    ve_me "\"Mm! Recovery fuel. Pro stuff.\""
    "You announce it, smacking your lips."
    show ve_mia neutral at vn_cast_slot
    ve_mia "\"It's your favourite. I can tell.\""
    "Mia giggles."
    hide cg onlayer cgl
    call ve_night_nipples
    jump ve_day3

label ve_day3:
    call ve_morning(3)
    $ vn_enter(bg="ve_lawn", pc="neutral", pc_tag="ve_pc", cast=[("ve_holly", "neutral")], cg="ve_ankle")
    "You go back for seconds. Nobody tells you to. You just stand there with the empty cup until Mia fills it from hers."
    ve_holly "\"That's the appetite. Sit. Ankle.\""
    "She pats the grass. She kneels and tapes your ankle, round and round, gossiping. The Mars guys are on {i}different{/i} shakes. One of them's had to buy new shirts."
    "She tears the tape with her teeth."
    vn_sfx "Smack!"
    "She slaps your thigh."
    ve_holly "\"Off you go, gorgeous.\""
    hide cg onlayer cgl
    "Sprints. Every stride the tank rubs your nipples. {i}Zing. Zing. Zing.{/i} By the end you're running with your arms crossed over your chest and a stupid grin on your face."
    menu:
        "Wink at Holly on the way past":
            $ ve.wink = "holly"
            ve_holly "\"Down, girl.\""
            "Holly rolls her eyes. That's flirting. Definitely."
        "Wink at Mia on the way past":
            $ ve.wink = "mia"
            show ve_mia neutral at vn_cast_slot
            "Mia goes pink and waves at you with both hands. That's flirting. Definitely."
    $ vn_set_time(22, 0)
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")])
    ve_me "\"Harem's forming. Mia does my hair, Holly does my ankle. They've got a {i}rota{/i}, man.\""
    "That night, hands behind your head."
    "Simon sits on the edge of his bed. Looks at your bare shining shins. The tape."
    ve_simon "\"Is this weird? Be honest. Is this weird?\""
    ve_me "\"It's VIP.\""
    ve_simon "\"...Right.\""
    jump ve_day4

label ve_day4:
    call ve_morning(4)
    $ vn_enter(bg="ve_dining", pc="grin", pc_tag="ve_pc", cast=[("ve_mia", "neutral")], cg="ve_blender")
    "You don't bother with a cup any more."
    vn_sfx "Glug glug glug."
    "You drink yours. You drink Mia's. Then you grab the blender jug in both hands and tip it back. Pink runs down your chin."
    "The whole Venus end of the table giggles. You lower the jug, lips glossy pink, and grin at them."
    "Mia takes it off you and makes another batch without a word."
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"That's the appetite. You'll be beating them off with a stick.\""
    ve_me "\"I know.\""
    "You mean the women."
    menu:
        "Hold your cup out for the next batch too":
            "Mia fills your cup again. You sip this one slow, eyes closed."
            ve_me "\"Mmmm.\""
        "Lick the rim of the jug clean":
            $ ve.extra += 1
            vn_sfx "Slrrp."
            "You run your tongue all the way round the rim. Half the table watches, chins in their hands."
    hide cg onlayer cgl
    call ve_night_pecs
    jump ve_day5

label ve_day5:
    call ve_morning(5)
    call ve_first_prop
    jump ve_day6

## ==== DAYS 6-9 (rung 3) =========================================================================

label ve_day6:
    call ve_morning(6)
    $ ve_body(3)
    $ vn_enter(bg="ve_twinroom", pc="shocked", pc_tag="ve_pc", cg="ve_r3_mirror")
    "The shorts won't sit right. They ride up. You've got {i}hips{/i}. A real ass pushing out the purple. Fuller lips. Hair curling at your collar."
    "And your chest. Not just nipples now. Two soft little A-cup handfuls under the tank. You grab them. They {i}give{/i}."
    ve_me "\"Ahh— {i}hah{/i}— what the—\"" with vnfx("shake")
    "You squeeze again. And again. Your hips roll against nothing."
    vn_sfx "Smack."
    "You slap your own new ass. It jiggles. You moan at it."
    "You laugh. It comes out higher than it went in."
    ve_me "\"Gains.\""
    "It sounds like a girl doing an impression of you."
    $ vn_enter(bg="ve_corridor", pc="neutral", pc_tag="ve_pc", cast=[("ve_mia", "neutral")], cg="ve_hair_brush")
    "Mia sits you on the bottom stair with a brush."
    ve_mia "\"Hold {i}still{/i}. It's at your collar now and it's doing a thing. People pay for this colour, Chrissy!\""
    if ve.wink == "mia":
        ve_mia "\"And don't wink at me while I've got scissors. You did it on Wednesday and I nearly walked into a door.\""
    else:
        ve_mia "\"Holly says you winked at her on Wednesday. Rude. I'm the one doing your hair.\""
    vn_sfx "Brush. Brush."
    "You sit there with your knees pressed together, eyes half shut. It's the best thing that's ever happened to you."
    hide cg onlayer cgl
    "In the session the props are bigger. Veined. A squeezy reservoir in every base."
    "You put the headphones on yourself now. It'd feel wrong not to."
    "The shake's a treat now. You toast Megan across the table before you drink. {i}Gulp gulp.{/i}"
    ve_me "\"Mmm!\""
    menu:
        "Ask Mia for a plait":
            $ ve.hair = "plait"
            "A tight plait down your back, tied with a purple band from Mia's wrist. You swing it in every mirror you pass."
        "Ask Mia to put it up":
            $ ve.hair = "up"
            "Up off your neck, pinned, a couple of curls left loose round your ears."
            ve_mia "\"{i}Perfect{/i}!\""
    $ vn_set_time(21, 0)
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")])
    "That night Simon watches you cross the twin room. The shorts riding up. The roll in your hips you didn't put there."
    ve_simon "\"Chris. Did you even read the form?\""
    ve_me "\"Nobody reads the form.\""
    ve_simon "\"I read the form. I read {i}my{/i} form.\""
    "He pushes his glasses up."
    ve_simon "\"You did both. You did mine in about a minute. Did you read {i}yours{/i}?\""
    "You flop on your bed. Your new ass bounces. You stretch, arms up, tank riding high."
    ve_me "\"It got me in the fast lane, didn't it? Look at me. I'm {i}thriving{/i}.\""
    "Simon looks. For a long time."
    ve_simon "\"...Yeah. You are.\""
    call ve_night_shower
    jump ve_day7

label ve_day7:
    call ve_morning(7)
    $ vn_enter(bg="ve_studio", pc="flushed", pc_tag="ve_pc", cg="ve_hand_drill")
    "Hand drills. The whole cohort kneeling up at their props, both fists working."
    vn_sfx "Shlk shlk shlk shlk."
    "The room sounds obscene."
    ve_voice "Let your hands show how eager you are."
    "You're eager. Twist on the upstroke. Squeeze the reservoir at the bottom with your pinkie. Your wrists find the rhythm on their own. You never practised that."
    "A pearl of something pale wells up at the tip. You catch it with your thumb. You suck your thumb clean. {i}Mm.{/i}"
    show ve_wade warm at vn_cast_slot
    ve_wade "\"So brave.\""
    "Passing behind you."
    $ vn_enter(bg="ve_dining", pc="grin", pc_tag="ve_pc", cast=[("ve_holly", "neutral")], cg="ve_residue")
    "At lunch Holly points her fork at your face."
    ve_holly "\"You've got a line, babe. Right there. It's been there all morning.\""
    "You touch the corner of your mouth. A dried pale streak, down towards your chin."
    menu:
        "Lick it off, slowly, at her":
            vn_sfx "Slrrp."
            "You lick it off. Slow. Right at her. Holly cracks up and slaps the table."
            ve_holly "\"{i}That's{/i} the appetite!\""
            "The whole table cheers."
        "Leave it. It's a look.":
            $ ve.extra += 1
            ve_me "\"It's a look.\""
            "Holly laughs so hard she drops her fork. Mia wipes it off you with a napkin anyway."
    if ve.extra >= 2:
        ve_holly "\"Every single day you do the extra bit. The toast, the jug, this. I'm starting a tally.\""
    hide cg onlayer cgl
    "In the afternoon somebody slips a tube of lip gloss into your shorts pocket with a note: {i}show off that smile!{/i}"
    $ vn_enter(bg="ve_lockers", pc="grin", pc_tag="ve_pc", cg="ve_gloss")
    vn_sfx "Pop."
    "You put it on in the locker room mirror. Plump, glossy lips."
    ve_me "\"Entourage.\""
    "You tell the mirror, and pout. Mia brushes the hair out of your eyes on her way past without even looking."
    hide cg onlayer cgl
    call ve_night_fingers
    jump ve_day8

label ve_day8:
    call ve_morning(8)
    $ vn_set_time(13, 0)
    $ vn_enter(bg="ve_twinroom", pc="neutral", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_too_far")
    "Lunch break. You're on your bed doing your lip gloss, legs crossed at the knee. When did you start crossing them at the knee?"
    "Simon shuts the door."
    ve_simon "\"Is this weird? Be honest. Is {i}any{/i} of this weird?\""
    ve_me "\"Nope.\""
    ve_simon "\"You don't have body hair. Anywhere. You've got— {i}hips{/i}, dude. And your ass—\""
    "He goes red."
    ve_simon "\"Don't you think they're going a bit far?\""
    vn_sfx "Snap."
    "Cap back on the gloss. You roll onto your front, ass up, and pick up your phone."
    ve_me "\"Bro, you're just jealous.\""
    ve_simon "\"Of—\""
    ve_me "\"Front row seats to the glow-up of the century, and you're stuck doing push-ups. I know you wish you'd got this invite.\""
    "You kick your feet in the air."
    "He's bigger, you notice. His shoulders fill the doorway. His hoodie's tight across his chest."
    ve_simon "\"Okay. Okay, Chris.\""
    "He goes back to Mars."
    hide cg onlayer cgl
    menu:
        "Kick your feet and get back to your phone":
            "You kick your feet and scroll and hum the tune from the headphones."
        "Watch the door after it shuts":
            $ ve.door = True
            "You watch the door a little too long. Then you shake it off."
    call ve_night_pillow
    jump ve_day9

label ve_day9:
    call ve_morning(9)
    call ve_reservoir
    jump ve_day10

## ==== DAYS 10-11 (rung 4) =======================================================================

label ve_day10:
    call ve_morning(10)
    $ ve_body(4)
    $ vn_enter(bg="ve_twinroom", pc="shocked", pc_tag="ve_pc", cg="ve_r4_mirror")
    "When you sat up this morning, your chest came with you a second later."
    vn_sfx "Boing." with vnfx("shake")
    "Tits. Real ones. Full, round, a C cup at least, straining the tank so hard it's ridden up off your stomach. They sway when you breathe. Your thighs press together."
    "You shove the tank up. They {i}drop{/i}. Heavy. Bouncing. You grab both and squeeze, and soft tit spills out between your fingers."
    ve_me "\"Ahh— {i}ahhn{/i}— they're so {i}heavy{/i}— oh fuck, they're {i}mine{/i}—!\""
    "Your ass is fatter in the shorts. Your hair's brushing your shoulders. Down in the shorts your cock's shrunk to a soft little thing, tucked up tight. You poke it. It twitches."
    "Your tits jiggle when it does."
    ve_me "\"...Pec day.\""
    "You cup them. They spill over your hands."
    call ve_stacked
    jump ve_day11

label ve_day11:
    call ve_morning(11)
    call ve_bulb
    call ve_office
    jump ve_day12

## ==== DAYS 12-13 (rung 5) =======================================================================

label ve_day12:
    call ve_morning(12)
    $ ve_body(5)
    $ vn_enter(bg="ve_twinroom", pc="shocked", pc_tag="ve_pc", cg="ve_r5_mirror")
    "The shorts don't fit any more. Your ass and thighs overflow them, purple stretched shiny and digging in, everything wobbling when you step."
    "Plump lips. A soft, pretty face. Your cock's so tiny you can barely find it, so you stop looking."
    "Your tits are heavier again. D cups, bulging over the top of the tank. Your hair's halfway down your back."
    "You grab two big handfuls of ass and squeeze. Soft. Endless."
    ve_me "\"Ohh— {i}ohhh{/i}—\""
    "You bounce on your toes just to feel all of it wobble."
    ve_me "\"Bulking.\""
    "It comes out sweet and breathy and high. You clap a hand over your mouth. Then you say it again just to hear it."
    ve_me "\"Bulking!\""
    hide cg onlayer cgl
    call ve_accommodation
    jump ve_day13

label ve_day13:
    call ve_morning(13)
    call ve_practical
    call ve_roleplay
    call ve_twin_room
    call ve_question
    jump ve_day14

## ==== DAY 14 (rung 6): complete, the debut, the wrap ===========================================

label ve_day14:
    $ ve_day(14)
    $ ve_body(6)
    $ ve.fit = "nude"
    $ vn_enter(bg="ve_office", pc="shocked", pc_tag="ve_pc", cg="ve_complete_wake")
    "Morning. The headphones have gone quiet."
    "{color=#ff9ecb}You're {i}heavy{/i}.{/color} Your chest sways when you breathe. Your hips press the arms of the recliner."
    "Your hand slides under the blanket. Down your belly. Between your legs. To where it always is—"
    "It isn't."
    "No cock. No balls. Just smooth— then a seam. Two plump soft lips. Your fingertip brushes between them."
    ve_me "\"{i}Hnn!{/i}\"" with vnfx("shake")
    "Your whole body jumps."
    "One choked little noise comes out of you. Then a giddy, wobbly giggle."
    show cg ve_complete_mirror onlayer cgl
    "Then you see the mirror on her wall."
    "Strawberry-blonde waves past your shoulders. Heavy, freckled tits with fat pink nipples. A tiny waist, wide hips, and an ass you can see from the {i}front{/i}. Cheekbones."
    "A plump pink mouth."
    $ ve.me = "Chrissy"
    ve_me "\"...Hello?\""
    "Sweet. Husky. {i}Yours.{/i}"
    "The grin comes back. The same old grin. It's just found a better face."
    show cg ve_complete_grab onlayer cgl
    "You throw the blanket off and grab them. Both hands. G cups, freckled, so heavy they fill your arms and still spill everywhere."
    ve_me "\"Ahh— {i}ahhh{/i}— oh my {i}god{/i}— look at them— {i}look{/i} at them—!\""
    vn_sfx "Smack."
    "You twist on the vinyl. Your ass spills off the seat, fat and round, wobbling."
    ve_me "\"{i}Hyaan{/i}—!\""
    "Your fingers go back between your legs. Two soft lips. Slick already. You rub once and your whole body bucks off the recliner."
    ve_me "\"Nnh— {i}ahh{/i}— it's so {i}wet{/i}— it's {i}mine{/i}— it's all {i}mine{/i}—!\"" with vnfx("flash")
    ve_me "\"Obviously they fast-tracked me. {i}Obviously.{/i}\""
    "You tell the mirror."
    show cg ve_complete_toy onlayer cgl
    "On the side table: a little pink toy with a white ribbon tied round it in a bow, like a bouquet. You snort and leave it exactly where it is."
    hide cg onlayer cgl
    show ve_wade warm at vn_cast_slot
    "Ms. Wade comes in, clipboard first, and lights up."
    ve_wade "\"Good morning, Miss Talbot. How are you feeling?\""
    ve_me "\"Like I slept for a year and woke up famous.\""
    ve_wade "\"Radiant. Good girl.\""
    if ve.extra >= 5:
        ve_wade "\"You took every extra step we offered, darling, and invented a few. The staff have a word for you. It's {i}keen{/i}.\""
    if ve.spa == "eye":
        "She holds your eye over the clipboard, long, the way you held hers at the spa door on the first night. Perfectly professional."
    "She laughs and signs the last box."
    ve_wade "\"You'll have wondered why it's called Venus {i}and{/i} Mars.\""
    ve_me "\"I mean—\""
    ve_wade "\"Every attendee is half of a pair. It all builds to one last session: a scene, filmed, with your partner. Your debut. Your partner is Simon.\""
    "Her eyes shine."
    ve_me "\"...{i}Simon.{/i}\""
    ve_wade "\"He's been waiting all morning. It's your show, darling. You're the star.\""
    call ve_debut
    jump ve_wrap

label ve_wrap:
    $ ve.fit = "robe"
    $ vn_enter(bg="ve_corridor", pc="grin", pc_tag="ve_pc", cast=[("ve_mia", "neutral")], cg="ve_wrap_cohort")
    "The whole cohort's waiting in the corridor. They {i}clap{/i}. Megan wolf-whistles. Anna throws you a fresh robe."
    "Mia's in tears. Both arms round your neck."
    ve_mia "\"You were {i}amazing{/i}! I'm so {i}proud{/i} of you!\""
    if ve.hair == "plait":
        ve_mia "\"And the plait held! Through all of that! I'm putting it on my portfolio.\""
    else:
        ve_mia "\"And the updo held! Through all of that! I'm putting it on my portfolio.\""
    show ve_holly neutral at vn_cast_slot
    "Holly is pretending she isn't. Eyeliner running down her face."
    ve_holly "\"It's the lilies. I'm allergic.\""
    vn_sfx "Slap."
    "On your thigh, gentle."
    ve_holly "\"Not bad, Chrissy.\""
    show cg ve_wrap_envelope onlayer cgl
    show ve_wade warm at vn_cast_slot
    "Ms. Wade hands you the envelope: thick and cream, a gold V on the back. The same envelope everybody gets."
    "She doesn't hug you. Twice in a fortnight, and not a third time now. She just says it, eyes wet behind the cat-eye glasses."
    ve_wade "\"Good girl.\""
    show cg ve_wrap_cards onlayer cgl
    show ve_fiona neutral at vn_cast_slot
    "Ms. Fiona puts a card in your hand."
    "{color=#ff9ed8}{i}curious, bright, odd.{/i}{/color}"
    "A guy's lopsided capitals. Somebody you used to know."
    "Then a blank card on top, and a pen."
    ve_fiona "\"Three new ones, darling. Whatever you adore.\""
    menu:
        "headliner, obviously, right":
            $ ve.words = "headliner, obviously, right"
        "stacked, starring, Simon's":
            $ ve.words = "stacked, starring, Simon's"
        "seen, wanted, first":
            $ ve.words = "seen, wanted, first"
    "You write it in your new handwriting, round and loopy."
    "{color=#ff9ed8}{i}[ve.words].{/i}{/color}"
    hide cg onlayer cgl
    $ vn_feat("Venus and Mars")
    $ vn_enter(bg="ve_corridor", pc="flushed", pc_tag="ve_pc", cg="ve_end_window")
    "Out the stairwell window, the Mars men are loading the coach. Big arms. Tank tops. One bends over for a holdall and you watch his ass the whole way down and back up."
    "You lick your lips."
    "You came here for the women. You're not looking at the women."
    "Everything else? You were right. They spotted you the first morning. Advanced track. The lead. The whole building agrees with your maths."
    hide cg onlayer cgl
    show ve_simon grin at vn_cast_slot
    "Simon comes up the stairs with both your bags and his glasses crooked."
    if ve.door:
        "On the eighth night you watched the door a little too long after he left. You're watching him now, the same way, and this time you don't shake it off."
    else:
        "You never once watched a door after him. You're watching him now, up every stair, and you can't think why you never did."
    ve_simon "\"So. What now?\""
    menu:
        "Stay for the next intake" (ending=True):
            jump ve_epilogue_stay
        "Go with Simon" (ending=True):
            jump ve_epilogue_go

label ve_epilogue_stay:
    $ ve.epilogue = "stay"
    $ ve.done = True
    $ vn_enter(bg="ve_lobby", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")])
    "You stay."
    ve_wade "\"The new intake needs a demonstrator. Someone to show them how it's done. Entirely up to—\""
    ve_me "\"Yes.\""
    ve_wade "\"Of course.\""
    "She laughs."
    show cg ve_stay_coach onlayer cgl
    "Simon stays too. He hangs your Venus badge on the twin room door like a medal. On Monday you watch the new coach roll up the drive, his chin on top of your head."
    "A skinny guy hops off with a purple badge and a huge grin and swaggers towards the lavender doors."
    ve_me "\"Oh. He's {i}adorable{/i}!\""
    "You squeal it."
    hide cg onlayer cgl
    $ vn_enter(bg="ve_suite", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "hungry")])
    "That night. The suite. Cameras off. Simon on the bed, already hard just from you walking in."
    ve_simon "\"Morning, headliner.\""
    "Whatever time it is."
    "You drop the robe."
    menu:
        "Climb on":
            call ve_suite_again
        "Kiss him and save it for tomorrow":
            "You kiss him, slow, and curl up on his chest, and save it for tomorrow. There's always tomorrow now."
    jump ve_route_return

label ve_epilogue_go:
    $ ve.epilogue = "go"
    $ ve.done = True
    $ vn_enter(bg="ve_lobby", pc="grin", pc_tag="ve_pc", cast=[("ve_fiona", "neutral")])
    "You go."
    "Ms. Fiona blows you a kiss from the desk. The lavender doors swing shut behind you."
    $ vn_enter(bg="ve_coach", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "grin")], cg="ve_go_coach")
    "At the coach door Simon looks you up and down, all the way to the end, like small print. Then he takes your hand."
    ve_me "\"Come on. We've got an industry to conquer.\""
    "You haul him up the step."
    $ vn_enter(bg="ve_danube", pc="grin", pc_tag="ve_pc", cg="ve_go_kerb")
    "The coach drops you on the kerb outside the Dollhouse. There's a new intake date in the window already."
    jump ve_route_return
