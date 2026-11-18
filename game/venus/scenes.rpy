## The fortnight's written scenes (main/days/finale.twee; the director scenes written out as beats,
## as the other Ren'Py routes do). Withheld: no real cock in or on you before the practical (rung 5);
## the toy is never used. Ms. Wade touches you twice (the oils, your chest). Simon is the only man
## who touches you. The non-con pass (owner, 2026-11-11: "Rung 2 only"): the first prop.

## ==== DAY 1: the oils, Spa 3B (rung 1; Ms. Wade's first touch) =================================
label ve_spa:
    $ vn_set_time(21, 0)
    $ ve.fit = "nude"
    $ vn_enter(bg="ve_spa", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_spa_table")
    "Spa 3B. Candles. A massage table. A carafe marked {color=#ff9ed8}VENUS: RENEWAL{/color}."
    vn_sfx "Click."
    "Ms. Wade locks the door behind you."
    ve_wade "\"Robe off. On your back, under the towel.\""
    "You flex on the way down. For her. Your back arches on the table all by itself, and you know exactly how it looks."
    ve_wade "\"The oils are strong. You'll tingle. That means it's working.\""
    vn_sfx "Shff. Shff."
    "Cool cream at your temples. Your jaw. Your throat. Cold, then warm, then {i}fizzing{/i}."
    ve_wade "\"Let your shoulders drop. So brave.\""
    show cg ve_spa_oil onlayer cgl
    "Her palms sweep your chest, out over your nipples and back. The red fuzz there just wipes away under her hand."
    "Your armpits. Your ribs. Your stomach, circling low, lower, right down to your hips. Everywhere she's been, you're bare and slick and shining."
    show cg ve_spa_tent onlayer cgl
    "Under the towel your cock is rock hard. It's tenting the towel. It's been tenting it since your collarbones."
    "She doesn't look at it. Not once."
    vn_sfx "Snap."
    "Gloves on. Thicker oil, almond and musk. Up your shin. Up your thigh. The {i}inside{/i} of your thigh."
    "The oil runs warm under the towel where her hand doesn't go, and it tingles everywhere it runs."
    "The towel twitches. You flex your thighs so she'll notice. She reaches right past it for the bottle."
    ve_me "\"Is this, like, the advanced thing? For top performers?\""
    "You're panting."
    ve_wade "\"It's routine. But you're progressing beautifully.\""
    vn_sfx "Snap."
    ve_me "\"Routine.\""
    "You grin, throbbing under the towel. Arms. Wrists. Between your fingers. Then she holds out your robe."
    ve_wade "\"All done. Warm water only. Try not to scratch.\""
    hide cg onlayer cgl
    menu:
        "Hold her eye on the way out":
            $ ve.spa = "eye"
            "You hold her eye at the door. Long. Meaningful."
            ve_wade "\"Goodnight.\""
            "Perfectly professional."
            vn_sfx "Click."
        "Float back upstairs":
            "You float up to the Venus floor with your skin humming under the robe."
    return

## The twin room, Simon, your hand. Loud enough that he says "dude" again in the dark.
label ve_first_night:
    $ ve_body(1)
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_night1_gleam")
    "The twin room. Two narrow beds. Simon's on his with a notebook."
    "He looks up. He keeps looking."
    ve_simon "\"Dude. What did they do to you?\""
    "{color=#ff9ecb}You spread your arms. Your skin {i}gleams{/i}.{/color} Chest, arms, shins, all of it smooth and slick with oil, the freckles popping. Every scrap of hair on you is just gone."
    "You run both hands down your chest. Smooth. Down your stomach. Down past the waistband— {i}bare{/i}. Even there. Your balls are smooth as a peach."
    ve_me "\"{i}Hah{/i}— oh, that's— that's {i}nice{/i}.\""
    "You can't stop rubbing."
    ve_me "\"Private session. Advanced track. You wouldn't get it.\""
    ve_simon "\"Does it feel weird?\""
    ve_me "\"It's {i}VIP{/i}, man.\""
    hide cg onlayer cgl
    vn_sfx "Click."
    $ vn_enter(bg="ve_twinroom_night", pc="flushed", pc_tag="ve_pc", cg="ve_night1_hand")
    "Lamp off. You last about a minute."
    vn_sfx "Shlk."
    "Your hand goes under the waistband. Your little cock is hot and slippery with oil."
    ve_me "\"Nnh—\""
    vn_sfx "Shlk. Shlk."
    "Her hands. Her gloves. The towel. The way she reached right {i}past{/i} it—"
    ve_me "\"Ahh— {i}ahh{/i}—\""
    vn_sfx "Shlk shlk shlk shlk."
    "Your hips come off the mattress. The bare oily skin makes your own fist feel like someone else's."
    ve_me "\"Ms. Wade. Fuck— Ms. {i}Wade{/i}— yeah, just like that, don't stop, {i}don't stop{/i}—\""
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"...Dude.\""
    "In the dark."
    show cg ve_night1_cum onlayer cgl
    ve_me "\"Ms. Wade— Ms. Wade— I'm— {i}ahhh{/i}—!\"" with vnfx("shake", "flash")
    vn_sfx "Spurt."
    "A thin hot splash across your oily stomach. You lie there panting with your hand still wrapped round it."
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"{i}Dude{/i}.\""
    "He pulls his pillow over his head."
    ve_me "\"VIP.\""
    "You tell the ceiling, grinning."
    hide cg onlayer cgl
    return

## ==== The solo nights (rungs 2-3): your own hands; no partner touches you before rung 5 =========

label ve_night_nipples:
    $ vn_set_time(22, 0)
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")])
    "That night in the twin room, Simon stares at you."
    ve_simon "\"Dude. Your skin's doing a thing.\""
    "It shines like it's varnished."
    ve_me "\"Moisturiser. VIP strength.\""
    "His eyes drop to your tank. Your nipples are poking right through it, pink and puffy. You flex. They jiggle."
    vn_sfx "Click."
    $ vn_enter(bg="ve_twinroom_night", pc="flushed", pc_tag="ve_pc", cg="ve_night2_pinch")
    "He turns the lamp off. Your nipples won't calm down. They throb against the sheet."
    "You pinch one."
    ve_me "\"{i}Hnn{/i}—!\""
    "You pinch both. Your little cock jumps in your shorts."
    vn_sfx "Shlk shlk shlk."
    "One hand down your shorts. One hand rolling a fat puffy nipple."
    ve_me "\"Ahh— {i}ahh{/i}— fuck, they're so— so {i}sensitive{/i}—\""
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Dude.\""
    "Says the dark."
    ve_me "\"It's a— {i}nnh{/i}— recovery thing—!\""
    "You twist the nipple hard."
    show cg ve_night2_cum onlayer cgl
    ve_me "\"{i}Hyaaah{/i}—!\"" with vnfx("shake", "flash")
    vn_sfx "Spurt."
    "You come squeaking, back arched off the mattress, a sticky little splash in your shorts."
    hide cg onlayer cgl
    return

label ve_night_pecs:
    $ vn_set_time(22, 0)
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_night4_domes")
    "That night you turn sideways in the twin room mirror."
    "{color=#ff9ecb}Two soft little domes are pushing out the purple.{/color} Puffy nipples on top. You squeeze one. It gives, and it tingles."
    ve_me "\"Pec day.\""
    "You tell Simon, and flex."
    ve_simon "\"Dude.\""
    ve_me "\"The program's legit! Look at that definition.\""
    vn_sfx "Squish."
    ve_simon "\"That's not—\""
    "He stops."
    ve_simon "\"...Dude.\""
    "You pinch a nipple through the tank to show him. A bolt shoots straight down your stomach."
    ve_me "\"{i}Hyaah!{/i}\"" with vnfx("shake")
    "Simon puts his pillow over his face."
    show cg ve_night4_rub onlayer cgl
    "You don't stop. You can't. Both hands up under the tank, squeezing your soft new domes, tugging the nipples out."
    ve_me "\"Hah— hah— pec day— {i}pec day{/i}—\""
    vn_sfx "Shlk shlk shlk."
    "It's not enough. One hand dives into your shorts."
    ve_me "\"{i}Ahn{/i}— ahh— squeeze— {i}squeeze{/i}—!\""
    ve_simon "\"I'm {i}right here{/i}.\""
    "Says the pillow."
    ve_me "\"Then— {i}nnh{/i}— don't listen—!\""
    show cg ve_night4_cum onlayer cgl
    "You come with your fingers sunk in your own chest and your hips humping the air." with vnfx("flash")
    ve_me "\"{i}Ahhhn{/i}—!\""
    vn_sfx "Spurt."
    "All over your fist, inside your shorts."
    hide cg onlayer cgl
    return

## ==== DAY 5: the first prop (RUNG 2; NON-CON, resist-then-break under the headphones) ==========
## Owner, 2026-11-11 (the non-con pass, "Rung 2 only"): you balk out loud, the headphones go on
## while you're still saying no, the track takes your body (aware, unwilling, protesting), then the
## break: drooling, loud round it. Afterwards the misreading comes back ("Star power."): he misreads
## what his body did. Silicone: no real cock in or on you before rung 5.
label ve_first_prop:
    $ vn_enter(bg="ve_studio", pc="nervous", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_prop1_room")
    "Meeting Room B. A yoga mat at every mirror. And on every mat, on a little stand, a cock."
    "Pink silicone. Veins and everything. Standing up at exactly mouth height."
    ve_wade "\"Good morning, ladies! Today we begin training your ability to please a man. Find your station.\""
    "The cohort drops to their mats like it's nothing."
    "You don't. You stand there."
    ve_me "\"Whoa. Whoa, whoa. No.\""
    "Your voice cracks on it."
    ve_me "\"I'm not sucking a— that's a {i}dick{/i}, Ms. Wade. I'm here to be the guy who {i}gets{/i}—\""
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"Lips over teeth, babe.\""
    "Murmured from the next mat, already halfway down hers."
    vn_sfx "Shlurp."
    ve_me "\"No. I'm not doing it. That's not— that's the {i}wrong{/i} side of the camera—\""
    "This is backwards. {i}You{/i} stand. {i}They{/i} kneel."
    show cg ve_prop1_phones onlayer cgl
    "Ms. Wade comes over with a pair of fat pink headphones covered in sequins, smiling like you've said something brave."
    ve_wade "\"A little help. Guided focus. The top stars use it.\""
    ve_me "\"I don't want— I don't need— don't put those on me—\""
    vn_sfx "Click."
    "She slips them on by the band anyway."
    "A warm silver voice, under something like music."
    ve_voice "You're opening. You love the shape in your mouth. You love giving."
    ve_me "\"I'm not— I don't—\""
    "Your knees fold. You didn't fold them. You're on the mat with the pink thing right in front of your face, and your mouth's still saying {i}no{/i}."
    show cg ve_prop1_in onlayer cgl
    "Your hand comes up and wraps round the base. You watch it do it."
    ve_me "\"No— that's not me— that's not me doing— {i}mmf{/i}—\""
    "And your mouth opens round the tip. Cold. Your teeth graze it."
    ve_me "\"Mmf— {i}nnf{/i}— take them {i}off{/i}— mmf—\""
    "It comes out round silicone. Nobody takes them off."
    ve_voice "So natural. So lovely."
    vn_sfx "Glk. Glk."
    "Deeper. Your tongue finds the ridge on its own. Your jaw goes loose. You're telling it to stop, in your head, out loud, round it, and it just goes deeper."
    ve_me "\"Mmh— why's it— {i}mmnh{/i}— why does it {i}fit{/i}—\""
    show cg ve_prop1_drool onlayer cgl
    vn_sfx "Shlk shlk glk glk."
    "Spit runs down the shaft and over your knuckles. You don't wipe it. You use it. You didn't decide to use it."
    "It bumps the back of your throat."
    vn_sfx "Gkh!" with vnfx("shake")
    "A jolt of heat goes straight down your spine, and something lets go."
    "You pull up and dive straight back down for another."
    ve_me "\"Mmh— {i}mmnh{/i}— {i}mmmh{/i}—!\""
    "You're moaning. Loud. Bobbing, sloppy, fast. The no's gone somewhere and you can't find it."
    ve_me "\"{i}Mmph{/i}— star power! Shtar— {i}mmh{/i}— shtar power, baby—!\""
    "You gurgle it round it, full volume. Drool drips off your chin onto your tank. Your eyes roll up. Your cheeks are hollow."
    ve_me "\"Mmmh— {i}mmmh{/i}— {i}mmmmh{/i}—!\"" with vnfx("shake")
    show cg ve_prop1_up onlayer cgl
    "When you finally come up for air, gasping, glossy-chinned, Holly squeezes the back of your neck."
    ve_holly "\"See? You're a natural.\""
    "Ms. Wade looks up from her clipboard, proud and gentle."
    ve_wade "\"So brave.\""
    "You sit back on your heels. You wipe your mouth with the back of your wrist. Your jaw's humming."
    "You said no. You said it out loud. You remember saying it."
    ve_me "\"...Star power.\""
    "It comes out of you on its own, and it sounds right, so you say it again."
    ve_me "\"Star power. Obviously. A lead's gotta know the whole scene, right? Both sides of it. That's just— that's {i}range{/i}.\""
    "Holly pats your head like you've done something adorable."
    hide cg onlayer cgl
    $ vn_set_time(22, 0)
    $ vn_enter(bg="ve_twinroom", pc="neutral", pc_tag="ve_pc", cast=[("ve_simon", "neutral")])
    "That night Simon sniffs the air."
    ve_simon "\"Why do you smell like strawberries?\""
    ve_me "\"Star stuff.\""
    "You mumble it, and you're out like a light."
    return

## ==== DAY 6: the locker room, the shower, your fingers =========================================
label ve_night_shower:
    $ ve.fit = "nude"
    $ vn_enter(bg="ve_lockers", pc="flushed", pc_tag="ve_pc", cg="ve_shower_soap")
    "Later. The locker room. Empty, steamy, just you."
    "{color=#ff9ecb}You soap your new ass. Both hands.{/color} It's so {i}round{/i}. You squeeze it. It wobbles."
    "Your soapy fingers slide down between your cheeks."
    ve_me "\"Oh—\""
    "Round your hole. Slippery. You press."
    vn_sfx "Squish."
    ve_me "\"Oh— {i}oh{/i}— oh fuck—!\"" with vnfx("shake")
    show cg ve_shower_finger onlayer cgl
    "One finger, all the way in. You slap your other hand on the tile. Your tiny cock bobs in the water."
    vn_sfx "Squish. Squish. Squish."
    ve_me "\"Ahh— {i}ahh{/i}— why's it— why's it so {i}good{/i}—!\""
    "Two fingers. Your cheek on the wet tile. Your hips pushing back on your own hand."
    show cg ve_shower_cum onlayer cgl
    ve_me "\"{i}Ahhhhn{/i}—!\"" with vnfx("flash")
    "You come with your fingers buried in your ass, your little cock spurting at the drain, your squeal bouncing round the whole locker room."
    hide cg onlayer cgl
    $ ve.fit = "uniform"
    return

## ==== DAY 7: two fingers in your glossy mouth ===================================================
label ve_night_fingers:
    $ vn_set_time(23, 0)
    $ vn_enter(bg="ve_twinroom_night", pc="flushed", pc_tag="ve_pc", cg="ve_night7_suck")
    "That night Simon's snoring. You're not sleepy."
    "You suck two fingers into your glossy mouth. Slow. Twist on the way up, hum on the way down, just like the drill."
    ve_me "\"Mmh— {i}mmh{/i}—\""
    vn_sfx "Shlk shlk shlk."
    "Your other hand's on your cock. Fast."
    ve_me "\"Mmmh— {i}mmmmh{/i}—!\""
    show cg ve_night7_cum onlayer cgl
    "You come with your fingers down your throat, moaning round them." with vnfx("flash")
    vn_sfx "Spurt."
    "Hot and sticky all over your knuckles."
    "Simon stops snoring. You freeze, fingers still in your mouth."
    "He starts again."
    hide cg onlayer cgl
    return

## ==== DAY 8: the doubled portion, the pillow ====================================================
label ve_night_pillow:
    $ vn_set_time(20, 0)
    $ vn_enter(bg="ve_dining", pc="flushed", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_doubled")
    "That night the shake comes in a doubled portion: two cups taped together, a bendy straw through both, your name on it in Ms. Wade's handwriting."
    ve_wade "\"You've earned it.\""
    "She hands it over. She doesn't touch you. She never touches you."
    vn_sfx "Slurrrp."
    "You suck until your cheeks go hollow."
    ve_me "\"Mmmh— {i}mmmmh{/i}—\""
    "You're moaning into the straw. Halfway through you have to stop and breathe, eyes closed, warm all the way down."
    "When you open them, half the cohort's smiling at you like you did something clever."
    hide cg onlayer cgl
    $ vn_set_time(23, 0)
    $ vn_enter(bg="ve_twinroom_night", pc="flushed", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_night8_pillow")
    "Back in the twin room you can't settle. You're warm. Itchy. {i}Full.{/i}"
    "You roll onto your front and grab your pillow. Shove it between your thighs."
    vn_sfx "Hump. Hump. Hump."
    ve_me "\"Hah— hah— {i}ahn{/i}—\""
    "Your tiny cock grinds into the cotton. Your ass bounces in the air behind you."
    ve_simon "\"Seriously?\""
    ve_me "\"It's— {i}nnh{/i}— the {i}shake{/i}—!\""
    vn_sfx "Hump hump hump hump."
    ve_me "\"Ahh— {i}ahh{/i}— {i}ahhhn{/i}—!\"" with vnfx("flash")
    "You come squealing into the pillow, sticky and wet in your shorts. Simon pulls his duvet over his head."
    hide cg onlayer cgl
    return

## ==== DAY 9: the prop that finishes (RUNG 3; hands, then the swallow) ===========================
label ve_reservoir:
    $ vn_enter(bg="ve_twinroom", pc="grin", pc_tag="ve_pc", cg="ve_sandals")
    "You woke up in sandals."
    "White strappy ones, little cork heels. A present on your pillow: {i}for our star.{/i} Your toenails are cherry red. Mia and Holly, giggling on the corridor carpet, probably."
    $ vn_enter(bg="ve_studio", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_circle")
    vn_sfx "Click, click, click."
    "Across Meeting Room B. They make your hips go."
    "The mats are in a circle today. Everyone can see everyone. Every prop's reservoir is {i}full{/i}, pale and heavy."
    ve_wade "\"Hands first.\""
    vn_sfx "Shlk shlk shlk."
    "Both fists, twisting. Palms slick. Wrists flying. Grinning."
    ve_wade "\"Now. Open up. Don't spill.\""
    menu:
        "Open up":
            "You open up and slide down slow, lips tight, till your nose bumps the stand."
        "Open up wider than anyone":
            $ ve.extra += 1
            "Jaw down. Tongue out flat. Eyes up at the circle like it's a trick. You slide all the way down until your lips hit the stand."
    show cg ve_res_swallow onlayer cgl
    "And you squeeze."
    vn_sfx "Spurt."
    "Warm, thick, straight to the back of your throat. It tastes like the shake. {i}Exactly{/i} like the shake."
    vn_sfx "Gulp. Spurt. Gulp."
    ve_wade "\"Don't spill.\""
    "She sings it. You don't spill. You bob and squeeze and swallow."
    vn_sfx "Glk. Gulp. Glk. Gulp."
    ve_me "\"Mmh— {i}mmnh{/i}— {i}mmmmh{/i}—!\""
    "You're {i}so{/i} loud. Thighs spread on the mat, cherry toes curled, moaning round silicone like it's the best meal of your life."
    ve_me "\"Endurance— {i}mmph{/i}— training—! Endurance— {i}glk{/i}— baby—!\""
    "You gurgle it at the whole circle, cheeks full."
    ve_wade "\"Switch.\""
    "Everyone switches."
    ve_voice "More. Take more."
    "You don't hear it. You're down at the stand, throat working, the voice in your ears going on, and you squeeze it dry and keep sucking, chasing every last drop—"
    show cg ve_res_slap onlayer cgl
    vn_sfx "SMACK." with vnfx("shake")
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"{i}Alright{/i}, you win! Leave some for the rest of us!\""
    "Holly's palm on your thigh. She's laughing."
    "You come off it with a wet {i}pop{/i}, a pale string still hanging from your lip to your chin, dazed and beaming. The circle claps. Anna mouths {i}holy shit{/i}."
    ve_wade "\"So brave.\""
    "She underlines something twice."
    hide cg onlayer cgl
    "That night you lie on your bed in your sandals, belly warm and full, jaw loose and tingling. Simon doesn't ask you anything."
    return

## ==== DAY 10: stacked; the demo; lunch; the towel (rung 4) ======================================
label ve_stacked:
    $ vn_enter(bg="ve_corridor", pc="grin", pc_tag="ve_pc", cast=[("ve_mia", "neutral")])
    "Mia meets you at the bottom of the stairs and stops dead."
    "Your tits are bouncing in the tank like they want out. The neckline's dragged down into deep, soft cleavage."
    ve_mia "\"You're getting so—\""
    "She hunts for the word."
    ve_me "\"Stacked?\""
    "You put your hands on your hips so they push out."
    ve_mia "\"Gorgeous.\""
    "It hits somewhere deep and warm. You have to look away."
    $ vn_enter(bg="ve_studio", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_demo_front")
    "In Meeting Room B the mats all face the front now. Every sight-line runs to the front mat."
    ve_wade "\"Today we focus on performance. Miss Talbot, would you demonstrate for the group?\""
    "You walk up front. Hips swinging. Tits swinging. Every eye in the room lands on you, and it {i}fizzes{/i}."
    "Headphones on. A new playlist, with a beat under it."
    ve_voice "Open wide. It tastes so good. You love being watched, pretty girl."
    menu:
        "Kneel like you own the room":
            "Knees wide. Hair over one shoulder. Both hands round the base, porn-style. You look out at all of them first."
        "Arch your back for them first":
            $ ve.extra += 1
            "You turn sideways first. Hands behind your head. Tits out. Ass out. Hold it. The room {i}whoops{/i}. Then you kneel."
    show cg ve_demo_suck onlayer cgl
    "Then you show them."
    vn_sfx "Shlurrp."
    "Long wet drags, lips sealed. Deeper. The twist on the way up. The hum on the way down."
    vn_sfx "Glk. Glk. Glk."
    "Spit runs off your chin and drips onto your tits. You feel it slide down between them and moan right round the prop."
    ve_me "\"Mmh— {i}mmh{/i}— {i}mmmnh{/i}—!\""
    "The room's silent except for you. Every one of them watching. It goes down your spine like a hand."
    ve_voice "Good girl. Good girl."
    show cg ve_demo_bow onlayer cgl
    "You pull off, gasping, glossy, and sit back on your heels. Wipe your chin. Bow."
    ve_me "\"Thank you, thank you! The girls are basically my entourage.\""
    "Applause. Holly fake-fans herself. Megan whistles."
    ve_wade "\"Good girl. You truly thrive in the spotlight.\""
    ve_me "\"Obviously.\""
    hide cg onlayer cgl
    $ vn_set_time(13, 0)
    $ vn_enter(bg="ve_dining", pc="neutral", pc_tag="ve_pc", cast=[("ve_holly", "neutral")], cg="ve_lunch_mars")
    "Salad and another shake. You drain two."
    "Over by the window, the Mars table. They're {i}huge{/i} now. Cartoon huge. Shoulders like doorways, flexing at each other."
    "Simon's in a T-shirt that's given up, eating like he's paid by the plate."
    ve_holly "\"You ever wonder what they get up to over there?\""
    ve_me "\"Push-ups. Protein.\""
    ve_holly "\"Babe. They get shakes too. Different stripe. One girl says her Mars partner's split every shirt he brought, and— {i}not just shirts.{/i}\""
    "She drops her voice."
    ve_megan "\"It's not just us changing. They're making matched pairs. Technically compatible.\""
    ve_me "\"Makes sense. Stars need a good supporting cast.\""
    ve_holly "\"That's one word for it.\""
    "She grins into her straw."
    hide cg onlayer cgl
    $ vn_set_time(21, 0)
    $ vn_enter(bg="ve_twinroom", pc="shocked", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_towel")
    "Simon's just out of the shower. Towel round his waist. Broad, wet back."
    "He turns round. The towel slips."
    vn_sfx "Flop."
    "His cock. Soft, and it still hangs halfway down his thigh. Thick as your wrist. Veined. Heavy balls swinging under it."
    "It looks like one of the props, except it's warm, and it's {i}Simon's{/i}."
    ve_simon "\"Dude— sorry— they said it's {i}normal{/i}, okay?!\""
    "He yanks the towel back up, scarlet. Your mouth's hanging open."
    ve_me "\"No homo. It's science.\""
    "Very clearly."
    ve_simon "\"It's—\""
    ve_me "\"Academic interest! Scientifically. Very impressive. Scientifically.\""
    hide cg onlayer cgl
    "Simon sits down hard on his bed, clutching the towel. He looks at your tits, heaving under the tank, nipples poking out. Then your face."
    ve_simon "\"Chris. Did you even read the form?\""
    ve_me "\"Nobody reads the form.\""
    "He laughs. It cracks. Glasses off, rub eyes, glasses on."
    ve_simon "\"Is this weird? I keep asking. Is this weird?\""
    "Very quietly."
    ve_me "\"Bro. It's the best fortnight of my life.\""
    "He nods slowly. That's the last time he asks."
    $ vn_enter(bg="ve_twinroom_night", pc="flushed", pc_tag="ve_pc", cg="ve_night10_nohomo")
    "You lie awake for ages with it behind your eyelids. {i}Gulp.{/i}"
    "Under the sheet you squeeze your new tits together. Heavy. Soft. Your thumbs find the nipples."
    ve_me "\"Nnh—\""
    vn_sfx "Rub. Rub. Rub."
    "You grind your tiny cock against the mattress."
    ve_me "\"No homo. No homo— no {i}homo{/i}— {i}ahh{/i}—\""
    "You whimper it into the pillow."
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"I can {i}hear{/i} you.\""
    ve_me "\"{i}Science{/i}—!\"" with vnfx("flash")
    "You squeak it, and come all over the sheet and your own belly."
    hide cg onlayer cgl
    return

## ==== DAY 11: the bulb (RUNG 4), then Ms. Wade's office (her second and last touch) ============
label ve_bulb:
    $ vn_enter(bg="ve_studio", pc="grin", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_bulb_prop")
    "The call sheet calls it {i}décolletage endurance{/i}. Code for the pros only, obviously."
    "Today's prop is {i}wide{/i}. Chest height. A fat bulb at the root, loaded and sloshing. Oil on every mat."
    ve_wade "\"Oil up, ladies. Wrap your cleavage round it. Miss Talbot, would you show us?\""
    show cg ve_bulb_oil onlayer cgl
    "You kneel up front and tug the tank down under your tits. They spill out, heavy and freckled, in front of everyone."
    vn_sfx "Shlick shlick."
    "You pour oil in your palms. Rub it in all over them till they shine."
    ve_wade "\"Don't spill.\""
    "Glowing with pride."
    menu:
        "Squeeze them round it and go":
            "You lean in and squeeze them round it with both arms. It vanishes into you. Just the tip peeks out at the top."
        "Tease the room with it first":
            $ ve.extra += 1
            "You drag the head across one tit first, slow, over the nipple, down the slick valley, up the other side. The room groans. You bite your lip at them."
    show cg ve_bulb_work onlayer cgl
    "And you move."
    vn_sfx "Shlk. Shlk. Shlk."
    "Up and down. Arms squeezing, oil squelching, the fat head popping up at your chin every stroke."
    "Your arms squeeze in time with it all on their own, tight on the downstroke, loose on the up. Nobody taught you that."
    ve_me "\"Ahh— {i}ahh{/i}—\""
    "Your nipples drag over your own forearms. Every drag is a firework."
    ve_me "\"Oh {i}fuck{/i}— {i}décolletage endurance{/i}, baby. Every stud's gotta— {i}ahh{/i}— gotta {i}master{/i} this—!\""
    "You pant it at the room, glowing. Somebody at the back slaps a hand over her mouth."
    "You squeeze the bulb with your thigh."
    show cg ve_bulb_splurt onlayer cgl
    vn_sfx "SPLURT." with vnfx("shake", "flash")
    "White, thick, right up into the hollow of your throat. Again. It runs down into your cleavage and beads in the oil."
    ve_me "\"Mmh— {i}mmmh{/i}—!\""
    "You bend your head and lick the tip before a drop can get away. Salty. Thick on your tongue."
    "None of it hits the mat. It's all on you. Throat. Tits. Pooled in the valley. You hold the pose, panting, shining."
    ve_wade "\"Not a drop spilled. Beautiful. {i}Good girl.{/i}\""
    "The room goes off like a football crowd."
    hide cg onlayer cgl
    "You tug the tank back up over it. It soaks straight through. Sticky all afternoon."
    return

label ve_office:
    $ vn_set_time(21, 0)
    $ vn_enter(bg="ve_office", pc="nervous", pc_tag="ve_pc", cast=[("ve_wade", "warm")])
    "Ms. Wade's office. Low lamps. Lavender and honey. A vinyl recliner."
    ve_wade "\"I think you're ready, Miss Talbot. Tank off, darling.\""
    $ ve.fit = "nude"
    show cg ve_office_lift onlayer cgl
    "It comes off. Your tits drop out, heavy, still glazed and tacky from the bulb. She doesn't mention it."
    "She kneels in front of you and lifts them from underneath, one in each hand. Warm. She feels the weight of them."
    "You suck in a breath."
    "Her thumbs start to circle your nipples. Round. Round. Rolling them. Stretching them."
    ve_me "\"Ohh— oh—\""
    "They swell under her thumbs. Fat. Dark. {i}Throbbing.{/i}"
    show cg ve_office_cum onlayer cgl
    "She leans in and closes her mouth on the left one."
    ve_me "\"{i}Hyahh{/i}—!\"" with vnfx("shake")
    vn_sfx "Slrp. Slrp."
    "Hot, wet, her tongue swirling, her lips sealed tight. Her other hand pinching, rolling, pinching the right."
    ve_me "\"Oh god— oh {i}god{/i}— Ms. Wade—!\""
    "Your hand goes down. To your cock. Like always."
    "She catches your wrist. Lifts it. Puts your hand on your own shoulder. Then the other one."
    ve_wade "\"No, honey. Let your body lead.\""
    "Against your nipple."
    menu:
        "Let it":
            "You hold your own shoulders and let your head fall back."
        "Beg her not to stop":
            $ ve.extra += 1
            ve_me "\"Don't stop. Please. {i}Please{/i}, Ms. Wade, don't you dare stop, please, {i}please{/i}—\""
    "She switches sides. Mouth on the right. Fingers on the wet left one."
    vn_sfx "Pinch. Suck. Pinch. Suck."
    ve_me "\"Ahh— {i}ahh{/i}— {i}ahh{/i}—\""
    "It's building. Nobody's touching you {i}there{/i}. Your cock's a forgotten little thing throbbing at nothing. It's building anyway, from your tits, pouring down into your belly—"
    ve_me "\"Ms. Wade— it's— it's {i}happening{/i}— from just— from {i}just{/i}—\""
    ve_wade "\"I know, darling.\""
    vn_sfx "Slrrrp."
    ve_me "\"{i}AHHHH{/i}—!\"" with vnfx("shake", "flash")
    "Your whole chest goes off like a bell. Waves roll down through you. Hips bucking at empty air, thighs clamped, tits shaking in her hands."
    "You're crying out, high and sweet, loud enough for the whole corridor."
    ve_me "\"Ahh— ahh— it won't {i}stop{/i}— {i}ahhh{/i}—!\""
    "Your little cock twitches once, untouched. Then even that's gone under it."
    hide cg onlayer cgl
    "When you can see again she's stroking your hair."
    ve_wade "\"See? That's your body's own language. Good girl.\""
    "She slips the headphones on you for the walk back."
    ve_voice "Good girl. Beautiful girl. Everyone wants to see you."
    $ ve.fit = "uniform"
    return

## ==== DAY 12: accommodation (RUNG 5); the lockers; your fingers while Simon watches =============
label ve_accommodation:
    $ vn_enter(bg="ve_studio", pc="nervous", pc_tag="ve_pc", cast=[("ve_holly", "neutral")], cg="ve_accom_circle")
    "The call sheet says {i}accommodation{/i}. Meeting Room B smells of lube."
    "A thick prop on a suction base, stuck to every mat. Straight up. Glossy. A big bottle of lube in the middle of the circle."
    hide ve_holly
    show ve_wade neutral at vn_cast_slot
    ve_wade "\"Confidence, ladies. And control. Holly, you start.\""
    "Holly peels off her shorts, squats, lines it up, and sinks all the way down with a long theatrical sigh. She wiggles at you."
    hide ve_wade
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"Like a spin bike, babe. Nothing to it.\""
    "One by one, the whole circle sinks down onto their props. Laughing. Moaning. Full."
    "Then it's you. Last."
    $ ve.fit = "nude"
    show cg ve_accom_squat onlayer cgl
    "You peel the shorts down. They snag on your ass, which is {i}enormous{/i} now, and it wobbles free in front of everyone. Your cock's tiny."
    "It bobs between your soft thighs like an afterthought."
    "You squat. Knees shaking. The cold slick head nudges your hole."
    menu:
        "Push down":
            pass
        "Look at Holly, and push down":
            $ ve.extra += 1
            "You look across at Holly."
    hide ve_wade
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"You look so cute when you're about to be full. Just relax, babe.\""
    "She purrs it. You shut your eyes and push."
    ve_me "\"{i}Nngh{/i}—!\"" with vnfx("shake")
    "It {i}stretches{/i}. Hot. Huge. So good you freeze with just the head in, shaking."
    ve_voice "Open, relax, good girl, so accommodating."
    "Then the voice, no headphones needed. Something lets go."
    show cg ve_accom_sink onlayer cgl
    "You sink."
    ve_me "\"Ahh— {i}ahh{/i}— oh fuck, oh {i}fuck{/i}—\""
    "Down. Down. Every bit of it stretching you wider, and every bit of it {i}amazing{/i}. Another bit. Another."
    ve_me "\"Oh my god— oh my {i}god{/i}— it's all— it's all the way {i}in{/i}—!\""
    "Your fat ass sits on your heels. You're {i}full{/i}."
    "And your tiny cock is bouncing. Every time you shift, it bobs and slaps your thigh, and every time you shift the prop moves in you and something deep inside goes {i}off{/i}—"
    show cg ve_accom_ride onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    "So you keep shifting. You're rocking. You're {i}riding{/i} it. Your hips find the rhythm before you do. You never practised that."
    "All round the circle the others are bouncing too. Holly's sighing. Megan's swearing. Anna's going {i}oh, oh, oh{/i} like a car alarm."
    "A whole ring of girls on their props, and every one of them is watching {i}you{/i}."
    ve_girl "\"Look at her go.\""
    "Somebody whispers it. That does it. You bounce harder."
    vn_sfx "Pap pap pap pap."
    ve_me "\"Ahh— {i}ahh{/i}— it's hitting— it keeps {i}hitting{/i}— something—!\""
    "Your tiny cock flops and slaps. Your fat ass claps on your heels. Your hands are on your tits, squeezing, because they're bouncing too and you can't stand it."
    show cg ve_accom_cum onlayer cgl
    ve_me "\"Ah— {i}ah{/i}— stud training! Final— {i}ahh{/i}— final module, {i}baby{/i}—!\"" with vnfx("shake", "flash")
    "You squeal it, bouncing, in a high sweet voice you never practised. The circle cheers."
    hide ve_holly
    show ve_wade neutral at vn_cast_slot
    ve_wade "\"There. Perseverance, beauty, utility. Good girl.\""
    hide cg onlayer cgl
    $ vn_set_time(12, 0)
    $ vn_enter(bg="ve_lockers", pc="flushed", pc_tag="ve_pc", cast=[("ve_mia", "neutral")], cg="ve_lockers_anna")
    "The locker room, after. Steam. Lavender soap. Naked women. You stand there, still feeling full, glowing."
    "Anna's at the next shower. Platinum hair, slick and soapy, enormous tits, head back, laughing. Everybody's looking at her. She doesn't care."
    "A week ago you'd have stared at her with your tongue out."
    "You stare now. And you don't want her."
    "You want {i}that{/i}."
    "To be the one in the middle of the room. Tits out. Head back. Everybody looking."
    ve_mia "\"Trade you towels, Chrissy?\""
    vn_sfx "Snap!"
    "Mia swaps your grey one for a pink one and flicks it at your hip."
    ve_anna "\"Looking glowy. You'll knock them dead tomorrow.\""
    "Anna winks. You blush all the way down your chest and sashay to your locker. You don't even notice you're doing it."
    hide cg onlayer cgl
    $ vn_set_time(23, 0)
    $ vn_enter(bg="ve_twinroom", pc="flushed", pc_tag="ve_pc", cast=[("ve_simon", "neutral")], cg="ve_night12_show")
    "That night Simon doesn't ask you anything. He watches you take your hair down. When you catch him in the mirror, he doesn't look away."
    "So you give him something to look at."
    "You lie back on your bed. Knees up. Shorts off. You slick two fingers in your mouth and slide them into your ass, slow, the way the prop went in."
    ve_me "\"Ahh— {i}ahh{/i}— so full—\""
    "Simon doesn't move. His hand's gone under his own duvet."
    ve_me "\"Bro— don't— don't {i}look{/i}—\""
    "You moan it, and spread your knees wider."
    vn_sfx "Squelch. Squelch. Squelch."
    ve_me "\"Ahh— {i}ahh{/i}— deeper— I need it {i}deeper{/i}—!\""
    "Across the gap, his duvet's moving. Fast."
    show cg ve_night12_cum onlayer cgl
    ve_me "\"{i}Ahhhhn{/i}—!\"" with vnfx("flash")
    "You come clenching on your own fingers, tiny cock dribbling on your stomach. A second later Simon grunts into his pillow."
    "Neither of you says anything. The lamp stays on."
    hide cg onlayer cgl
    return

## ==== DAY 13: the partnered practical (RUNG 5, MANDATORY) =====================================
## "Access, access, access." Simon's hands guide your hips onto the prop, then the prop is gone and
## it's him. The first real cock in or on you, anywhere in the route. A consensual misreading.
label ve_practical:
    $ ve.fit = "uniform"
    $ vn_enter(bg="ve_studio", pc="nervous", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_prac_mat")
    "The call sheet, in lavender capitals: {color=#ff9ed8}PENETRATION SEQUENCE. PARTNERED.{/color}"
    "One mat in the middle of Meeting Room B, facing the long mirror. A thick prop on a suction base, set on a padded block at kneeling-hip height."
    "The whole cohort sits round the walls, watching."
    ve_wade "\"Miss Talbot. You'll pair with Simon. Very advanced, darling.\""
    show cg ve_prac_simon onlayer cgl
    "The side door opens. Simon turns sideways to fit through it."
    "Mars has made him {i}huge{/i}. Chest like a wall. Hoodie half-zipped. Little glasses on a big square face. Turquoise Venus-issue shorts that are definitely too small."
    "He looks at you. Purple tank. Hair down your back. Your enormous ass in the purple shorts."
    vn_sfx "Gulp."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Hey.\""
    ve_me "\"Hey, bro.\""
    hide ve_simon
    show ve_wade warm at vn_cast_slot
    ve_wade "\"Access, access, access! Let your partner guide you, ladies.\""
    $ ve.fit = "nude"
    show cg ve_prac_guide onlayer cgl
    "Shorts down. You kneel facing the mirror, ass to the room, knees apart."
    "Simon kneels behind you. His hands land on your hips. They're {i}enormous{/i}. They nearly go all the way round."
    "He guides you up. Apart. Then back, slow, onto the prop. The slick head kisses your hole."
    "Every muscle you've got wants to do it the old way. Snap the hips. {i}Drive.{/i} Like a stud."
    "You snap your hips."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"No. Slow. Let it in.\""
    "Low, just for you. Slow. You roll your hips down instead of forward. Back arched. It slides in."
    ve_me "\"Nnh— {i}ahh{/i}—\""
    "In the mirror: your hair spilling, your tits hanging heavy in the tank, your mouth open. A girl being lowered onto a cock by a pair of big hands."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Good.\""
    "Then he lifts you off it."
    vn_sfx "Thwuck."
    "In the mirror you watch him reach past your hip. The prop peels off the block. He sets it on the floor."
    show cg ve_prac_real onlayer cgl
    "Something else presses against you. Warm. Thick. {i}Alive.{/i}"
    "He's kneeling up behind you, shorts shoved down, his cock in his fist. Fat. Dark. Heavy. The head resting right on your hole."
    "His eyes meet yours in the glass."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Okay?\""
    hide ve_simon
    show ve_wade warm at vn_cast_slot
    ve_wade "\"This is the practical, darling. Partnered.\""
    "Softly."
    ve_me "\"Bro. Bro— {i}yes{/i}. Yes! Don't you dare stop, don't you—\""
    "Your voice has gone high and shaky."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Let it in.\""
    menu:
        "Let it in":
            pass
    show cg ve_prac_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    "In. The fat head of him past the ring, and it's nothing like the prop. Hot. Alive. {i}Throbbing.{/i}"
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Breathe out. That's it. That's— god. Let it in.\""
    "It doesn't hurt. It's big, it's so big, and it just keeps going, and you keep letting it."
    ve_me "\"Ahh— {i}ahh{/i}— bro— it's {i}so{/i}— it's warm— it's {i}moving{/i}—\""
    show cg ve_prac_mid onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Everyone's watching. Don't— don't look at them. Look at the mirror.\""
    "Through his teeth."
    hide ve_simon
    show ve_wade warm at vn_cast_slot
    ve_wade "\"Access. Access, access.\""
    "She sings it, somewhere behind you both."
    "Simon's hands are huge on your hips, and they don't let go."
    "He finds a pace, slow and deep, and every stroke your whole body rolls with it, tits swinging in the tank, ass wobbling on his hips."
    ve_me "\"Stud training— {i}ahh{/i}— final— {i}final{/i} module— oh fuck, bro, {i}bro{/i}—\""
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Is this—\""
    "He starts, and doesn't finish, and doesn't stop either."
    show cg ve_prac_peak onlayer cgl
    vn_sfx "Pap pap pap pap." with vnfx("shake")
    "Faster. Deeper. Something inside you he keeps hitting, and every time he hits it your tiny cock jerks between your thighs and you squeal at the mirror."
    ve_me "\"There— {i}there{/i}— don't— don't stop hitting— {i}ahh{/i}—!\""
    show cg ve_prac_finish onlayer cgl
    "He slams in to the root and holds you there, both hands clamped on your hips."
    vn_sfx "Throb. Throb."
    "Heat floods into you, so much you feel it in your stomach."
    show cg ve_prac_cum onlayer cgl
    "And you come." with vnfx("flash")
    "Nobody's touching you. Your tiny cock just bobs there between your thighs, forgotten. It twitches once and dribbles a thin string onto the mat."
    "The rest happens {i}inside{/i}. Round him. Clenching and clenching and not stopping."
    ve_me "\"{i}Ahhh{/i}— bro— {i}bro{/i}— I'm— {i}ahhhh{/i}—!\"" with vnfx("shake")
    "It comes out so loud the mirror rattles."
    show cg ve_prac_applause onlayer cgl
    "You sag onto your elbows with him still inside you. The room is {i}applauding{/i}. Mia's on her feet. Holly whistles through her fingers. Anna's got both hands over her mouth."
    hide ve_simon
    show ve_wade warm at vn_cast_slot
    ve_wade "\"Beautiful work. Good girl.\""
    "For everyone."
    "In the mirror, Simon's face. Half worried. Half something else. Something like pride."
    ve_me "\"Stud training. Final module.\""
    "You pant it, wrecked, grinning."
    hide ve_wade
    show ve_simon neutral at vn_cast_slot
    ve_simon "\"Yeah. Sure.\""
    "Softly."
    hide cg onlayer cgl
    $ ve.fit = "uniform"
    return

## ==== DAY 13: the role-play seminar (owner, 2026-11-11: "give a small branching scene with the
## roleplay session"). The draft's adult deck: three cards face down, and whichever you draw, you
## grab the man's prop and the small print casts you as the woman. Jay plays opposite. He never
## touches you: Simon is the only man who does.
label ve_roleplay:
    $ vn_set_time(14, 0)
    $ vn_enter(bg="ve_stage", pc="grin", pc_tag="ve_pc", cast=[("ve_fiona", "neutral")], cg="ve_rp_deck")
    "Role-play seminar, after lunch. A little stage, a free-standing door frame, a costume rail. Ms. Fiona fans out a deck of cards."
    ve_fiona "\"Pick one, darlings! Lean into the fantasy. {i}Especially{/i} if it feels silly.\""
    "Anna draws {color=#ff9ed8}MASSEUSE WITH A SECRET{/color}. Trish draws {color=#ff9ed8}HIGH-SOCIETY BALL{/color} and waltzes her partner round in circles."
    "Three cards left in Ms. Fiona's hand, face down."
    menu:
        "The card on the left":
            $ ve.card = "delivery"
        "The card in the middle":
            $ ve.card = "office"
        "The card on the right":
            $ ve.card = "flight"
    hide cg onlayer cgl
    if ve.card == "delivery":
        call ve_rp_delivery
    elif ve.card == "office":
        call ve_rp_office
    else:
        call ve_rp_flight
    ve_fiona "\"And {i}scene{/i}!\""
    "She claps."
    show ve_jay neutral at vn_cast_slot
    "Jay stays right where he is."
    ve_jay "\"You're killing it, Chrissy.\""
    "He mutters it, just for you."
    "The cohort swarms you. Hugs. Hair fixed. Somebody hands you back your shorts."
    show ve_holly neutral at vn_cast_slot
    ve_holly "\"You're a natural. Perfect balance of shame and show.\""
    "Nobody's called you by your old name in days. You haven't noticed."
    return

label ve_rp_delivery:
    show cg ve_rp_delivery_card onlayer cgl
    "{color=#ff9ed8}THE DELIVERY.{/color}"
    "{i}Yes!{/i} You grab the red delivery cap off the rail, jam it on backwards, and throw your arms out. The delivery guy. Obviously. The guy who gets invited in."
    show ve_holly neutral at vn_cast_slot
    "Holly plucks the card out of your hand, reads the small print, and plucks the cap off your head."
    ve_holly "\"Babe. {i}Read{/i} it.\""
    "{i}THE DELIVERY. You answer the door in a towel.{/i}"
    show ve_jay neutral at vn_cast_slot
    ve_jay "\"Guess I'm the delivery, then. Jay. Don't worry. I don't touch the talent.\""
    "A grinning Mars guy takes the cap and puts it on. Broad, impish, twenty-five, a pizza box under his arm."
    $ ve.fit = "towel"
    show cg ve_rp_delivery_towel onlayer cgl
    "Behind the rail you strip and wrap a white hotel towel under your arms. It barely makes it. Straining round your tits at the top. Riding up over your ass at the bottom."
    "You step behind the door frame. Every eye in the room is on you. It hits like a lungful of something. {i}All{/i} of them. On {i}you{/i}."
    vn_sfx "Knock knock."
    menu:
        "Let the towel slip when you open the door":
            show cg ve_rp_delivery_slip onlayer cgl
            "You open the door. And let the towel slip. It slides off your tits, catches on your nipples for one long second— and drops to your waist."
            "You lean on the frame, hip cocked, tits bare, lashes low."
        "Hold it shut and pout at him":
            show cg ve_rp_delivery_pout onlayer cgl
            "You open the door, clutching the towel shut, which shoves your tits up over the top like they're being served. Lip out. Hip cocked against the frame. Lashes low."
    ve_jay "\"Delivery. For Miss Talbot?\""
    "He holds out the box, grinning."
    ve_me "\"Ohh. I don't have any money. Whatever will I {i}do{/i}?\""
    "High and breathy, completely on your own. The room {i}roars{/i}." with vnfx("shake")
    ve_jay "\"I'm sure we'll think of something.\""
    "Deadpan. The room roars again. You bite your lip and step back to let him in. The towel's going. You let it go."
    ve_me "\"Bring it in, then.\""
    "You purr it."
    hide cg onlayer cgl
    return

label ve_rp_office:
    show cg ve_rp_office_card onlayer cgl
    "{color=#ff9ed8}OFFICE AFTER HOURS.{/color}"
    "{i}Yes!{/i} You grab the tie and the briefcase off the rail and loosen the knot like a boss. The boss. Obviously. Corner office. The guy who keeps someone late."
    show ve_holly neutral at vn_cast_slot
    "Holly plucks the card out of your hand, reads the small print, and plucks the tie off your neck."
    ve_holly "\"Babe. {i}Read{/i} it.\""
    "{i}OFFICE AFTER HOURS. You're the new secretary. You stayed late on purpose.{/i}"
    show ve_jay neutral at vn_cast_slot
    ve_jay "\"Guess I'm the boss, then. Jay. Don't worry. I don't touch the talent.\""
    "A grinning Mars guy knots the tie on himself and sits behind a prop desk with his feet up."
    $ ve.fit = "office"
    show cg ve_rp_office_outfit onlayer cgl
    "Behind the rail you squeeze into a pencil skirt that stops just under your ass and a white blouse that gets three buttons up and gives up."
    "Cat-eye glasses off the rail, perched on your nose."
    "You click across the stage with a clipboard. Every eye in the room is on you, and it fizzes all the way down."
    menu:
        "Drop your pen and bend to get it":
            show cg ve_rp_office_bend onlayer cgl
            "Oops. The pen rolls under his desk. You bend for it. Slow. Straight-legged. The skirt rides up over the bottom of your ass and the whole room gets the view."
        "Perch on the edge of his desk":
            show cg ve_rp_office_desk onlayer cgl
            "You perch on the edge of his desk and cross your legs, slow, right in front of him. The blouse gapes. You let it."
    ve_jay "\"Working late, Miss Talbot?\""
    ve_me "\"Oh, sir. I'm {i}so{/i} behind on my— filing. Is there anything else you need? Anything at {i}all{/i}?\""
    "Breathy. Lashes fluttering. Completely on your own. The room {i}roars{/i}." with vnfx("shake")
    ve_jay "\"Take a letter.\""
    "Deadpan. The room roars again. You lick the end of your pen at him."
    hide cg onlayer cgl
    return

label ve_rp_flight:
    show cg ve_rp_flight_card onlayer cgl
    "{color=#ff9ed8}MILE-HIGH.{/color}"
    "{i}Yes!{/i} You grab the pilot's cap off the rail and salute the room. The captain. Obviously. The guy every stewardess fights over."
    show ve_holly neutral at vn_cast_slot
    "Holly plucks the card out of your hand, reads the small print, and plucks the cap off your head."
    ve_holly "\"Babe. {i}Read{/i} it.\""
    "{i}MILE-HIGH. You're the flight attendant on the night flight. First class is empty except for him.{/i}"
    show ve_jay neutral at vn_cast_slot
    ve_jay "\"Guess I'm first class, then. Jay. Don't worry. I don't touch the talent.\""
    "A grinning Mars guy drops into a pair of chairs pushed together as an airline seat and stretches his legs."
    $ ve.fit = "flight"
    show cg ve_rp_flight_outfit onlayer cgl
    "Behind the rail you wriggle into a tiny navy uniform dress, a silk scarf knotted at the throat, a little pillbox hat. The zip won't go past your tits. You leave it."
    "You wheel the drinks trolley out onto the stage, hips swinging. Every eye in the room is on you."
    menu:
        "Lean right over his seat with the drinks":
            show cg ve_rp_flight_lean onlayer cgl
            "You lean right over his seat to set his drink down. Tits in his face. Slow. The open zip does the rest."
        "Do the safety demonstration, very slowly":
            show cg ve_rp_flight_demo onlayer cgl
            "You do the safety demonstration in the aisle. Slowly. The exits. The oxygen mask. Your hands running down your own body to show where the life jacket goes."
    ve_jay "\"Anything else on the menu?\""
    ve_me "\"Oh, sir. We're {i}so{/i} short on— pillows. Whatever will we {i}do{/i}? I'm sure I can find you {i}something{/i} to lie on.\""
    "High and breathy, completely on your own. The room {i}roars{/i}." with vnfx("shake")
    ve_jay "\"I'll take the full service.\""
    "Deadpan. The room roars again. You wink and push the trolley away with your hip."
    hide cg onlayer cgl
    return

## ==== DAY 13: the twin room (optional; Simon leading, consensual) ==============================
label ve_twin_room:
    $ vn_set_time(19, 0)
    $ ve.fit = "uniform"
    $ vn_enter(bg="ve_twinroom", pc="flushed", pc_tag="ve_pc", cast=[("ve_simon", "hungry")])
    "Simon's on the end of his bed, elbows on his knees. He doesn't ask if it's weird. He's done asking."
    ve_simon "\"This morning. That was—\""
    ve_me "\"I know, bro.\""
    "He laughs, helpless. Glasses off, on the sill."
    "He's hard. He's not even hiding it. It's lying along his thigh under the turquoise shorts, huge."
    "You stare at it."
    menu:
        "Get on your knees between his":
            call ve_twin_oral
            menu:
                "{i}He's still hard. Of course he is.{/i}"
                "Turn over for him":
                    call ve_twin_anal
                "A note under the door":
                    pass
        "Curl up next to him instead":
            "You curl up next to him. His bed's too small for both of you and neither of you cares. He's still hard against your hip."
            menu:
                "Turn over for him":
                    call ve_twin_anal
                "A note under the door":
                    pass
    return

label ve_twin_oral:
    show cg ve_twin_kneel onlayer cgl
    "You slide off your bed onto the carpet between his knees. You tug the turquoise shorts down and it springs out and slaps your cheek."
    vn_sfx "Thwap."
    ve_simon "\"Dude. {i}Dude{/i}.\""
    "Very quietly, at the ceiling."
    show cg ve_twin_suck onlayer cgl
    vn_sfx "Glk. Glk."
    "Every drill pays out at once. Lips sealed. The twist on the way up. The hum on the way down. He's warmer than any prop and he {i}jumps{/i} in your mouth."
    ve_simon "\"Slow. Slow. You don't have to— oh. Okay. You can.\""
    ve_me "\"Mmh— {i}mmnh{/i}— {i}mmmh{/i}—\""
    ve_simon "\"Where did you even {i}learn{/i}— oh. Right. Oh god.\""
    show cg ve_twin_cum onlayer cgl
    vn_sfx "Spurt. Spurt." with vnfx("flash")
    "He comes in your mouth with his hand in your hair. You swallow every drop without being told. {i}Gulp. Gulp.{/i} It tastes like the shake. {i}Exactly{/i} like the shake."
    ve_me "\"Don't spill.\""
    "You croak it, grinning, and wipe your chin."
    ve_simon "\"Oh my {i}god{/i}.\""
    "He falls back laughing."
    hide cg onlayer cgl
    return

label ve_twin_anal:
    $ ve.fit = "nude"
    show cg ve_twin_knees onlayer cgl
    "You end up on his bed. On your back. His bed's too small for both of you and neither of you cares."
    "He's on his knees between your thighs. Huge. Hard. Lube from the drawer, slick in his fist."
    ve_simon "\"No mirror. No room. Just me.\""
    "You pull your knees up to your chest. Your fat ass in the air. Your tiny cock lying on your belly."
    "The fat head presses where it went this morning. Warm. {i}Throbbing.{/i}"
    ve_me "\"Bro—\""
    "It's not the word. You swallow it."
    ve_me "\"{i}Simon.{/i}\""
    "His eyes go wide behind his glasses. Then he pushes."
    menu:
        "Hold your knees and let him in":
            "You hold your knees and let him in."
        "Grab his hips and pull him in":
            $ ve.extra += 1
            "You grab his hips with both hands and pull him in, all of him, and he swears."
    show cg ve_twin_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    ve_simon "\"Still so tight from this morning—\""
    vn_sfx "Creak. Creak. Creak."
    "The little bed creaks like it's about to give up."
    ve_simon "\"Look at me. Not the wall. {i}Me{/i}.\""
    ve_simon "\"Say it again. Say my name.\""
    ve_me "\"Simon— {i}Simon{/i}— ahh—!\""
    show cg ve_twin_cum2 onlayer cgl
    "You come round him with your knees by your ears. Your tiny cock dribbles on your belly. Nobody touched it. Nobody needed to." with vnfx("flash")
    "He comes buried in you, groaning your name into your neck. {i}Throb. Throb.{/i} Hot and deep and so much you feel it in your belly."
    "The little bed creaks. The wall thumps. Somebody next door bangs back, laughing."
    ve_simon "\"That's the first time you've said my name all week.\""
    "He pants it."
    ve_me "\"Don't get used to it.\""
    "You both know you're lying."
    hide cg onlayer cgl
    $ ve.fit = "uniform"
    return

## ==== DAY 13's night: the question, and the recliner (the change overnight, no explanation) ====
label ve_question:
    $ vn_set_time(21, 0)
    $ vn_enter(bg="ve_office", pc="nervous", pc_tag="ve_pc", cast=[("ve_wade", "warm")], cg="ve_question_note")
    "A note under the door: {i}My office, darling, whenever you're ready.{/i}"
    "Ms. Wade's office. Roses. The recliner tilted back. A blanket on the seat. The pink headphones on the arm."
    ve_wade "\"Sit, Miss Talbot.\""
    "You sit. Your soft thighs spread across the vinyl."
    "She pulls up a stool, hands folded on her clipboard."
    ve_wade "\"You've come so far, darling. This last step is entirely up to you. No pressure. Are you ready to finish? To be complete—\""
    "She leans in."
    ve_me "\"Hell yes. I want it. I'm ready for the last step.\""
    "You blurt it, like a stud."
    ve_wade "\"Good girl.\""
    "She smiles, pure and calm and happy."
    show cg ve_recliner onlayer cgl
    vn_sfx "Click."
    "Recliner back. Blanket over you. Headphones on, by the band."
    ve_voice "You've done so well. Let go now. Let your body finish. Let it finish."
    ve_wade "\"You'll wake up complete.\""
    "She whispers it. The lamp goes off."
    hide cg onlayer cgl
    call vn_night(6)
    return

## ==== DAY 14: the debut (RUNG 6; the titjob, your mouth, then you ride him: the first vaginal) ==
label ve_debut:
    $ vn_pass(30)
    $ vn_enter(bg="ve_suite", pc="grin", pc_tag="ve_pc", cast=[("ve_simon", "hungry")], cg="ve_suite_cameras")
    "The suite. Candles. A huge bed. Cameras on tripods all round it, red lights on."
    "Simon's in the middle of the bed. Tanned, broad, heavy with muscle. His cock lies along his thigh, thick and enormous."
    "He sits up. His glasses nearly fall off."
    ve_simon "\"Holy shit. Chris. You— I— uh—\""
    ve_me "\"Yeah, I know.\""
    show cg ve_suite_crawl onlayer cgl
    "You drop the silver robe. Your tits spill out, heavy and bare in the candlelight. You crawl up the bed to him on your hands and knees, slow, for the cameras."
    ve_me "\"Looks like someone's lucky to be my co-star, Simon.\""
    "He laughs, cracked. His cock's already standing straight up, pointing at you. You catch it in both hands."
    menu:
        "Wrap your breasts round him":
            pass
    show cg ve_suite_tits onlayer cgl
    vn_sfx "Shlp. Shlp."
    "You squeeze them round him and he vanishes between them, all but the head, and it pops up at your chin every stroke."
    ve_simon "\"Holy shit. Holy {i}shit{/i}.\""
    "Watching himself slide up between your breasts."
    ve_simon "\"They— they didn't teach us anything like this on Mars.\""
    ve_simon "\"Don't spill.\""
    "He laughs, and then can't laugh at all."
    show cg ve_suite_tits_cum onlayer cgl
    vn_sfx "Splurt! Splurt!" with vnfx("flash")
    "He goes off between your tits with a shout. Up out of your cleavage, over your chin, your throat. You squeeze and bounce and milk him dry, then lick it off your lips for the camera."
    "He stays hard. Of course he does. Mars built him for it."
    ve_me "\"Bet they didn't teach you {i}that{/i} on Mars.\""
    ve_simon "\"They really didn't.\""
    "He wheezes it."
    ve_me "\"VIP treatment for the star talent.\""
    show cg ve_suite_mouth onlayer cgl
    "You bend down and take him in your mouth. Every hour on the mats pays out at once. Lips sealed. Tongue flat. The twist. The hum."
    vn_sfx "Glk. Glk. Hlk."
    ve_me "\"Mmh— {i}mmmh{/i}—!\""
    ve_simon "\"Look at you. Look at {i}you{/i}.\""
    "Like he can't believe the room. He groans at the ceiling, fists in the sheets."
    "You take him down till your nose is in his skin and come up with a string of spit, looking straight down the nearest lens."
    show cg ve_suite_straddle onlayer cgl
    "Then you crawl up him and straddle his hips. Tits on his chest. You reach back for him."
    ve_me "\"Ready for your close-up, Simon?\""
    "He nods. He can't talk."
    "The fat head nudges your new lips apart. Stops. {i}Stretches.{/i}"
    ve_me "\"Oh— {i}oh{/i}— oh my god—\""
    show cg ve_suite_sink onlayer cgl
    "You sink." with vnfx("shake")
    ve_me "\"Ahh— {i}ahhh{/i}— it's going {i}in{/i}— it's so {i}thick{/i}—!\""
    "Slow and thick and endless. All the way up. Until you're sitting on his hips with him buried to the root, mouth hanging open, whole body shaking."
    "You tug his glasses down his nose so his eyes meet yours."
    ve_me "\"Look at me. You're starring in the Chris Talbot Show. Try and keep up.\""
    menu:
        "Ride him":
            pass
    show cg ve_suite_ride onlayer cgl
    vn_sfx "Pap! Pap! Pap!"
    "You ride him till the cameras are the only thing in the room not shaking."
    "Hands on his chest. Hips rolling. Tits bouncing so hard they slap. Your new pussy squeezing him on every drop. Your hips know the rhythm before you do."
    "Nobody ever showed you this one."
    ve_simon "\"God— you're— this is the Chris Talbot Show, isn't it. I'm in it.\""
    ve_me "\"Ahh— {i}ahh{/i}— yes, yes, Simon, fuck me, it's so good, it's so {i}deep{/i}, look at me, {i}look{/i} at me—!\""
    ve_simon "\"Don't stop. Please. Don't— the camera, I don't care about the camera—\""
    "His hands grip your hips like he's holding on to a ledge."
    show cg ve_suite_cum onlayer cgl
    "Then it hits."
    "Not like a cock going off. Deep inside, right round him. A clench that won't let go. It climbs and climbs and rolls out through you in waves. Back arching. Toes curling."
    "Pussy pulsing round him." with vnfx("shake")
    ve_me "\"{i}AHHHHH{/i}—!\"" with vnfx("flash")
    "You scream it at the ceiling, high and wild. Your first time coming as a girl. On top. On camera. Everybody watching."
    "Simon goes with you. His hips jerk. His hand grips your hip. {i}Throb. Throb.{/i} Heat, flooding deep inside you."
    ve_me "\"Ahh— {i}again{/i}— I'm coming {i}again{/i}—!\""
    show cg ve_suite_after onlayer cgl
    "You grind down and milk him and come a second time on the back of the first, gasping, laughing, collapsing onto his chest."
    ve_simon "\"You were right. About all of it. You were right.\""
    "He gasps it into your hair, wrecked."
    "His glasses are crooked. The red lights are steady. Every lens is pointed at you."
    ve_me "\"Obviously.\""
    hide cg onlayer cgl
    return

## ==== THE STAY EPILOGUE: the suite, with Simon (consensual) ====================================
label ve_suite_again:
    show cg ve_again_climb onlayer cgl
    "You climb on. You sink down on him slow, all the way, and he groans like it's the first time."
    vn_sfx "Pap. Pap. Pap."
    ve_simon "\"Still the headliner.\""
    ve_me "\"Obviously— {i}ahh{/i}— obviously, Simon—\""
    ve_simon "\"Show-off.\""
    "Adoring. He lets you."
    show cg ve_again_cum onlayer cgl
    "You come on top of him, loud, the way you always do, and he comes in you groaning both your names, the old one and the new one, all mashed together." with vnfx("flash")
    ve_simon "\"Every time. Every single time.\""
    "He gasps it."
    hide cg onlayer cgl
    return
