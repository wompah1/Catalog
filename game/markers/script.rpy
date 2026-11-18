## The House Settles Markers' passages: THE SOURCE (written straight in Ren'Py, 2026-11-11; the
## catalog's twee is kept verbatim in catalog/docs/routes/vn-original/markers/ for reference). One
## label per beat. The register: resist-then-break, and the gambler's arithmetic between (route.rpy).
## Seven nights: each runs the house room at three in the afternoon, the locker and the hook, the
## floor (a station, Tam's table, Simone's break), the night's beat, and Odette's reading.

## ==== NIGHT 1: the last chip, the marker, the back office (rung 1) ============================

label mr_opening:
    $ mr.fit = "own"
    $ mr.night = 1
    $ vn_enter(bg="mr_tamtable", pc="grin", pc_tag="mr_pc", cast=[("mr_tam", "neutral")], cg="mr_lastchip")
    "Four in the morning at the Golden Hare."
    "No windows. No clocks."
    "Green felt glowing in the gloom, the gold hare over the cage mid-leap, and a handful of night owls orbiting the roulette wheel like they've forgotten how to leave."
    "You've been at Tam's table for ten hours. Eyes red. Throat raw. Head still quick, though. That's all that counts."
    "One chip left."
    mr_vic "\"It's not a losing streak. It's a {i}slope{/i}. Slopes correct. It's just distribution.\""
    "Tam says nothing. Tam never says anything. He squares the shoe and looks at your last chip like it's a question he already knows the answer to."
    mr_vic "\"Last six shoes ran cold. Which means the next one runs hot. That's maths, Tam. That's just {i}maths{/i}.\""
    vn_sfx "Tk."
    "You push it out."
    hide cg onlayer cgl
    call mr_bj_hand("Tam")
    if mr_bj.result in ("natural", "win"):
        "Tam pays it. You look at the chips."
        mr_vic "\"Let it ride.\""
        "Because you're {i}hot{/i} now. Obviously."
        show cg mr_lasthand_sweep onlayer cgl
        "Tam deals again. The house's cards come up a picture and an ace, and the whole stack goes back across the felt in one slow sweep."
    elif mr_bj.result == "push":
        "A push. The chip comes back."
        mr_vic "\"Again.\""
        show cg mr_lasthand_sweep onlayer cgl
        "You push it straight out, and this time Tam's cards come up a picture and an ace, and the chip goes."
    else:
        show cg mr_lasthand_sweep onlayer cgl
        vn_sfx "Click."
        "Tam sweeps your last chip off the felt."
    "And that's it. Empty hands. Palms still itching like they're holding something."
    show mr_pc nervous at vn_pc_slot
    mr_vic "\"Okay. Okay. That's fine. That's just the bottom of the slope.\""
    jump mr_cage

label mr_cage:
    $ vn_pass(5)
    $ vn_enter(bg="mr_cage", pc="neutral", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_cage_marker")
    "The pit boss is already at the cage when you get there. Tall, dark suit, ageless as the air in here. {i}Odette{/i}, the badge says."
    "She slides a slip of the house's cream letterhead across the counter. Gold hare at the top."
    "A marker."
    "You grab the pen."
    mr_odette "\"Do you read the back?\""
    "Her voice is flat as a weather forecast."
    show mr_pc grin at vn_pc_slot
    mr_vic "\"Does anyone?\""
    show cg mr_marker_back onlayer cgl
    "She turns it over for you anyway. Small print, the same neat type as the front. One line of it is bigger than the rest."
    "{color=#f3c969}{i}The house settles markers in whatever the debtor has.{/i}{/color}"
    mr_vic "\"Uh huh.\""
    "You wait a beat in case she wants to explain. She doesn't."
    mr_vic "\"So I just sign?\""
    mr_odette "\"You just sign.\""
    menu:
        "The pen's warm from your hand."
        "Sign it in block capitals":
            $ mr.signed = "block"
        "Sign it with a winner's flourish":
            $ mr.signed = "flourish"
    show cg mr_sign onlayer cgl
    if mr.signed == "flourish":
        "Your name goes down in a big loop and a slash, the signature of a man on the way up. VIC HOLLAN underneath, so they can read it."
    else:
        "The pen bites down. VIC HOLLAN, in ugly block capitals, the handwriting of mostly-winning."
    mr_vic "\"So what's 'whatever I have' mean?\""
    "Odette tears off her half of the marker."
    mr_odette "\"You'll see. This way.\""
    jump mr_back_office

label mr_back_office:
    $ vn_pass(5)
    $ vn_enter(bg="mr_backoffice", pc="neutral", pc_tag="mr_pc", cast=[("mr_simone", "smirk")], cg="mr_office_simone")
    "Through a door marked STAFF ONLY. Down a corridor that smells of lemons and old smoke."
    "A back office at the end: close, quiet, a little bar fridge humming on the carpet, and a black leather couch."
    "And a woman."
    "She's tall. Taller than you, and in flats. All hips and shoulders, black satin shirt open low, a lazy smile like she was posted here at exactly the right hour for exactly the right job."
    "And down the front of her tailored slacks, a bulge you can't stop looking at."
    hide mr_simone
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"First settlement.\""
    "Odette sets the slip on the desk like she's signing for a crate of gin, and goes."
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"Came up short, hm? Simone. I collect.\""
    "Her accent takes its time over every vowel."
    mr_vic "\"I'm good for it. You'll have it tomorrow.\""
    "She doesn't answer that. She unlocks a drawer and takes out a little red velvet pouch, and when she sets it down it {i}clinks{/i}. Glass on glass."
    "Ampoules. Tiny glass ampoules, stoppered with wax, each with a neat printed label."
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"House rule. The payment is real.\""
    "She sits next to you on the leather, close enough that her voice is only for you."
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"You can't settle all of it tonight. But you can pay what you owe. Piece by piece. And the first payment is always what's most ordinary.\""
    mr_vic "\"Ordinary like what?\""
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"Take your shirt off, cabrón. Makes things neater.\""
    "You strip to the waist. Pale. That straggle of chest hair you were never proud of. Her palm runs up through it, slow, and you get it all at once."
    show mr_pc shocked at vn_pc_slot
    mr_vic "\"We pay in {i}body hair{/i}?\""
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"Tonight, you do.\""
    mr_vic "\"Hang on. Hang {i}on{/i}. That's not a payment, that's a— no. No, I'll get you cash. Give me till the cage opens and I'll have—\""
    show cg mr_office_lick onlayer cgl
    "She leans in and licks one broad wet stripe straight down the middle of your chest. Slow. Tasting the sweat of a ten-hour night. Right over the top of your sentence."
    hide mr_odette
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"You signed the back, cabrón. The house collects.\""
    "And you're hard. Stupid hard, all at once, tenting your trousers like a flag, while your mouth is still saying {i}no{/i}."
    menu:
        "Her eyes are on yours from under her lashes."
        "Haggle the rate":
            $ mr.answer1 = "haggle"
        "Try for the door":
            $ mr.answer1 = "door"
    jump mr_ampoule

## Rung 1, her hand (non-con, authored): she shaves you down while you argue terms, and milks you
## into the glass mid-objection. The ampoule is the payment: no cum lands on you.
label mr_ampoule:
    $ vn_enter(bg="mr_backoffice", pc="nervous", pc_tag="mr_pc", cg="mr_office_straddle")
    if mr.answer1 == "door":
        "You're off the couch and two steps to the door before her hand closes on the back of your belt."
        vn_sfx "Fwump." with vnfx("shake")
        "Back down on the leather, flat on your back, and she's straddling you before you've bounced."
        show mr_simone neutral at vn_cast_slot
        mr_simone "\"Door's for staff, cabrón.\""
    else:
        mr_vic "\"Okay— okay, let's talk numbers. Hair's worth what, a fiver? I'll give you {i}double{/i} in cash, I swear, tomorrow—\""
        "Simone laughs, low and delighted, and pushes you flat on the leather with one palm."
        show mr_simone neutral at vn_cast_slot
        mr_simone "\"There's no doubling a coat of hair, cabrón.\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"All of it.\""
    "Belt. Button. Zip. You grab her wrist and she just keeps going, your hand riding along on hers like a passenger. Underwear round your knees."
    "Your cock bobbing out into the cool air of the office."
    mr_vic "\"Hey— {i}hey{/i}— I didn't say—\""
    "She looks it over once, slow, like she's pricing it. Then she straddles you properly, thighs thick as a stack of chips, and reaches for the desk."
    "A ceramic bowl. A brush. A straight razor that flashes in the lamplight."
    show cg mr_office_shave onlayer cgl
    "She lathers you. Chest, stomach, arms, legs, the scatter of hair above your cock. Then she shaves you in long slow bands, top to bottom, humming under her breath."
    vn_sfx "Shhhk. Shhhk."
    mr_vic "\"This is NOT a settlement— I want to see the terms— I want the {i}pit boss{/i}—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"She's busy.\""
    vn_sfx "Shhhk."
    "And every time the razor goes low, her other hand's already there. Fingers circling the base of your cock. Touching. Never stroking."
    "Rolling your balls in her palm while the blade glides over the skin beside them."
    mr_vic "\"Nnh— {i}stop{/i}— stop {i}that{/i}— {i}fuck{/i}—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"You're clearing a fair bit on that coat.\""
    mr_vic "\"That was the luckiest hair I {i}had{/i}—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"Not tonight.\""
    "Arms. Knuckles. Toes. She leaves your face and your brows and takes everything else."
    "When she wipes the last of the foam off you're bare as a showroom floor, twitching, a bead of pre-cum shining at your slit."
    "She catches it with her thumb. Shows it to you."
    mr_vic "\"That's just {i}pressure{/i}, that's not me—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"Now the house collects.\""
    show cg mr_office_mouth onlayer cgl
    "She pins both your wrists over your head in one big hand. You pull. Nothing moves but your hips."
    vn_sfx "Shlp."
    "Her mouth. Hot and wet, just for a moment, her tongue swirling the crown. Then off again, letting it cool and throb."
    mr_vic "\"Ahh— {i}ah{/i}— no— Simone, {i}no{/i}—\"" with vnfx("shake")
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"Shh. House rule. The payment is real.\""
    "She lets go of your wrists only to take an ampoule from the pouch and pop the wax with her thumbnail. Your hands stay up where she put them. You don't know why."
    mr_vic "\"I'm {i}objecting{/i}— this is me formally {i}objecting{/i}— {i}hah{/i}—\""
    show cg mr_ampoule_milk onlayer cgl
    "She holds the glass under your tip and milks you with her other hand. Not like a lover."
    "Like a dealer laying out the minimum: long, measured strokes, her thumb pressing in under the head, her eyes on yours the whole time."
    vn_sfx "Shlk. Shlk. Shlk."
    mr_vic "\"I {i}said{/i}— oh fuck— oh {i}fuck{/i}— don't you {i}dare{/i}— I'm gonna—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"Into the glass, cabrón.\""
    "You go off like a jackpot, mid-word. Hips jerking up off the leather, a long loud groan ripping out of you."
    vn_sfx "Splrt. Splrt." with vnfx("flash")
    mr_vic "\"{i}AHHHH{/i}— oh my god— {i}more{/i}— oh my {i}god{/i}—\"" with vnfx("shake")
    "She holds the ampoule tight under the head and strokes you through every spurt. It fills the glass and runs over her knuckles."
    show cg mr_ampoule_label onlayer cgl
    "She licks her knuckles clean like she's tasting a good wine. Corks the ampoule. Takes a pen from her shirt pocket and writes on the label in neat capitals."
    "{color=#f3c969}Hollan, V., first settlement.{/color}"
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"There. Your first settlement.\""
    "She tucks it in the pouch with the others."
    mr_vic "\"I didn't— that wasn't a {i}yes{/i}—\""
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"The book doesn't ask.\""
    show cg mr_simone_tent onlayer cgl
    "She stands up off you, slow. The front of her slacks is tented now, long and thick and heavy, and she doesn't hide it. She lets you look."
    "A preview of what the house collects with."
    "Then she tosses you a towel, and the razor and the bowl vanish, and the office is as tidy as the lobby."
    $ vn_until(5)
    jump mr_reading

## ==== SHIFT CLOSE: the book, every night ======================================================

## Odette reads the book in four fields (the readout). The night's rung is banked here; how you take
## it is flavour. Then the night: wake at three in the afternoon (night 4's sleep wakes at nine).
label mr_reading:
    $ _n = mr.night or 1
    $ mr.fit = mr.fit or "own"
    if _n == 1:
        $ vn_enter(bg="mr_backoffice", pc="neutral", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_1")
        "Odette's back in the office by the time you've got your shirt on, the book under her arm. She opens it. Uncaps a pen. Reads aloud, without one breath of humour."
    elif _n == 2:
        $ vn_enter(bg="mr_lounge", pc="flushed", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_2")
        "Shift close, in the little glass office off the staff lounge. You're still in the suit, arms a little out from your sides for the tail check, cum still tacky on your knees."
        "Odette reads."
    elif _n == 4:
        $ vn_enter(bg="mr_lounge", pc="flushed", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_4")
        "Shift close. Odette doesn't look up when you come in on wobbly legs, the empty ampoule's label still in your head. The column's already written. She reads it anyway."
        "She always reads it."
    elif _n == 5:
        $ vn_enter(bg="mr_lounge", pc="grin", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_5")
        "Shift close. Odette has the book open before you're through the door. She reads you the day off like a bar tab."
    elif _n == 6:
        $ vn_enter(bg="mr_lounge", pc="flushed", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_6")
        "Shift close. Odette's at the glass desk. A new column is inked in blue down the right-hand side of the page: {i}Nights{/i}. She reads the line, and taps the column, once."
    else:
        $ vn_enter(bg="mr_lounge", pc="grin", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_reading_3")
        "Shift close, in the little glass office off the staff lounge. Odette opens the book. She reads."
    if _n == 5:
        $ _line = MR_BOOK_DAYOFF
    else:
        $ mr_advance({1: 1, 2: 2, 3: 3, 4: 4, 6: 5}.get(_n, mr.tier or 0))
        $ _line = MR_BOOK[mr.tier or 1]
    mr_odette "{color=#f3c969}\"[_line]\"{/color}"
    vn_sfx "Smack."
    "She closes the book, as routine as dice."
    menu:
        "How do you take it?"
        "Take it smug":
            $ mr.take = "smug"
        "Take it giddy":
            $ mr.take = "giddy"
        "Take it filthy":
            $ mr.take = "filthy"
    $ _take = MR_TAKES[_n][mr.take]
    "[_take]"
    if _n == 1:
        mr_odette "\"Settle your marker, and the rate will improve. The house keeps a room upstairs for marker players.\""
        "She hands you a key on a gold hare fob."
        mr_odette "\"See you at the cage tomorrow.\""
    else:
        "Odette nods, clipped and professional."
        mr_odette "\"See you at the cage tomorrow.\""
    hide cg onlayer cgl
    $ mr.night = _n + 1
    $ mr.station_seen = None
    if _n == 4:
        call vn_night(9)
        $ vn_clock.day = mr.night
        jump mr_day_off
    call vn_night(15)
    $ vn_clock.day = mr.night
    jump mr_afternoon

## ==== THE AFTERNOONS: the house room, three o'clock ===========================================

## Every night after the first begins here. A night whose body moved while you slept prints its
## growth beat: rung 1 on night 2 (smooth), rung 5's first landing on night 6 (the hair, the face,
## the voice, the ears).
label mr_afternoon:
    $ _n = mr.night
    if _n == 2:
        $ mr_body(1)
        $ mr.fit = "nude"
        $ vn_enter(bg="mr_houseroom", pc="shocked", pc_tag="mr_pc", cg="mr_wake_smooth")
        "You wake upstairs at the Golden Hare. The room the house keeps for marker players: a wide bed, blackout curtains, a minibar nobody restocks."
        "The floor's hum comes up through the mattress like a heartbeat."
        "You throw the sheet off and stop."
        "{color=#ff9ecb}Smooth.{/color}"
        "{color=#ff9ecb}Not shaved-smooth. Not stubble-in-the-morning smooth. {i}Showroom{/i} smooth. Chest, stomach, arms, legs, between your toes. Not one hair left anywhere but your brows.{/color}"
        vn_sfx "Shhf."
        "You run a palm down your thigh and it glides, like silk over silk. There's a sheen on you, a soft gleam on the skin, like you've been oiled for a photo shoot."
        "Your cock's already stiff against your bare belly, twitching every time your fingers brush the skin around it. You cup your hairless balls and your hips jerk up off the bed."
        mr_vic "\"Ohh— {i}fuck{/i}— why is that so {i}sensitive{/i}—\"" with vnfx("shake")
        "You lick your lips and that tingles too, all the way down."
        mr_vic "\"Mmh— even my {i}mouth{/i}—\""
        hide cg onlayer cgl
        show mr_pc grin at vn_pc_slot
        "You catch your own eye in the mirror and grin at yourself like you're closing a sale. The grin works. You can tell it works."
        mr_vic "\"All that fur, gone, and the marker's lighter. I'll take that rate!\""
        $ mr.fit = "own"
        $ vn_set_time(19, 30)
        jump mr_staff_rate
    elif _n == 3:
        $ mr.fit = "own"
        $ vn_enter(bg="mr_houseroom", pc="grin", pc_tag="mr_pc")
        "You wake upstairs at the Golden Hare. The floor's hum comes up through the mattress like a heartbeat."
        "The suit's draped over the chair where you dropped it. The thighs of the fishnets still smell of last night."
        vn_th "(You lie there and do the arithmetic. The arithmetic says {i}tonight{/i}.)"
    elif _n == 4:
        $ mr.fit = "nude"
        $ vn_enter(bg="mr_houseroom", pc="grin", pc_tag="mr_pc", cg="mr_wake_tits")
        "You wake upstairs at the Golden Hare."
        "You roll over and your tits roll with you. Heavy. Real. Yours."
        "You lie there squeezing them, grinning at the ceiling, running last night's hot roll back point by point."
        mr_vic "\"Paid down. In {i}body{/i}. Best rate on the floor.\""
        hide cg onlayer cgl
    elif _n == 6:
        $ mr_body(5)
        $ mr.fit = "nude"
        $ vn_enter(bg="mr_houseroom", pc="shocked", pc_tag="mr_pc", cg="mr_wake_ears")
        "Something's tickling your face. Something's tickling your {i}everything{/i}."
        "{color=#ff9ecb}Hair. Your hair. It's {i}everywhere{/i}. It paid out overnight: glossy and black as a dealer's waistcoat, down to your shoulders, falling in big soft princess waves that pour over the pillow when you sit up.{/color}"
        mr_vic "\"What— {i}ahh{/i}—\""
        "And your voice. That's not rounder. That's not syrupy. That's {i}hers{/i}. A girl's voice, high and sweet, coming out of your mouth."
        "You stumble to the mirror. A woman's face looks back. Soft jaw, full lips, big dark eyes, the face finished like someone signed it off."
        "Your tits are heavier again, pushing out so far you can't see your feet."
        "{color=#ff9ecb}And on top of your head, poking up through the black waves, two long soft ears.{/color}"
        "Not the costume ones. Those are on the hook in the locker. These are {i}yours{/i}. Warm. Velvety. They twitch when you gasp."
        "You reach up and touch one and the feeling goes straight down your spine and pools hot between your legs."
        mr_vic "\"Oh my god— they're {i}real{/i}— they're {i}mine{/i}— {i}mmh{/i}—\"" with vnfx("shake")
        "You stroke them with both hands. They flick. You moan out loud, in that new high voice, and it sounds so good you do it again just to hear it."
        mr_vic "\"Staff rate. Even the {i}ears{/i} are comped.\""
        hide cg onlayer cgl
    elif _n == 7:
        $ mr.fit = "own"
        $ vn_enter(bg="mr_houseroom", pc="grin", pc_tag="mr_pc", cg="mr_envelope")
        "There's an envelope under the door. Cream letterhead, gold hare, and one line in Odette's hand."
        "{color=#f3c969}{i}Private room. Mr. Royce has asked.{/i}{/color}"
        "You lie back on the pillow and laugh, high and bright, because you ran the numbers last night and the numbers love you."
        hide cg onlayer cgl
    $ vn_set_time(19, 30)
    jump mr_locker

## ==== NIGHT 2: the staff rate (rung 2) ========================================================

label mr_staff_rate:
    $ vn_enter(bg="mr_cage", pc="neutral", pc_tag="mr_pc", cast=[("mr_odette", "neutral")])
    "You're perched by the pit in the dead middle of the night, nursing a free gin, stroking your own smooth wrist without noticing you're doing it, when Odette comes past with a marker slip for somebody else."
    "She doesn't stop. She just says it on the way by, flat as the felt."
    mr_odette "\"Staff get half house edge. Floor only, full dress. Rules posted by the cage.\""
    "Half house edge."
    "It goes into your head in gold leaf. Half the edge. On every spin. Probably with comped drinks."
    hide mr_odette
    show cg mr_poster onlayer cgl
    "The poster's by the cage. A floor girl in black vinyl, all legs and frills and a fluffy white tail, a pair of satin ears on her head."
    "{color=#f3c969}{i}Staff games. Staff rates. House edge cut down the line. Full dress required.{/i}{/color}"
    "You look at the poster. You look at the pit. You look at your own shoes. You picture the suit cutting a line over your hips, and the arithmetic does the rest."
    show mr_pc grin at vn_pc_slot
    mr_vic "\"Staff rate.\""
    "The forms are in plain English. {i}Hollan, V.: temporary employee, non-tipped.{/i} You sign before you've finished reading, the way you always do."
    $ vn_enter(bg="mr_locker", pc="neutral", pc_tag="mr_pc", cast=[("mr_costumer", "neutral")], cg="mr_costumer_rail")
    "The costumer is a woman in her fifties with a tape round her neck she never uses and a tailor's clip in her teeth."
    "She looks at you once, top to bottom, by eye, and pulls a suit off the rail without asking a single question."
    mr_costumer "\"It'll pinch if it's wrong. You don't want a pinch.\""
    "She holds the clip up."
    mr_costumer "\"I can let it out. If you thicken up.\""
    mr_vic "\"I'll go easy on the buffet.\""
    "She looks at your hips and doesn't laugh."
    hide cg onlayer cgl
    jump mr_locker

## ==== THE LOCKER: the book's line, the hook, and tonight ======================================

label mr_locker:
    $ _n = mr.night
    if _n == 2:
        $ mr.kit = max(mr.kit or 0, 1)
    elif _n == 4:
        $ mr.kit = max(mr.kit or 0, 3)
    elif _n >= 6:
        $ mr.kit = max(mr.kit or 0, 4)
    $ vn_enter(bg="mr_locker", pc="neutral", pc_tag="mr_pc")
    if mr.tier:
        $ _line = MR_BOOK_DAYOFF if _n == 6 else MR_BOOK[mr.tier]
        "{color=#f3c969}The book, last night: {i}[_line]{/i}{/color}"
    $ _hook = mr_hook_line()
    "{color=#f3c969}On the hook:{/color} [_hook]"
    if _n == 2:
        jump mr_first_zip
    elif _n == 3:
        $ mr.fit = "suit"
        $ vn_enter(bg="mr_locker", pc="nervous", pc_tag="mr_pc", cast=[("mr_costumer", "neutral")], cg="mr_locker_seam")
        "You go to zip up and the suit {i}pinches{/i}. Across the hips, across the thighs, the vinyl biting a line into skin that wasn't there to bite last night."
        "The costumer's in the doorway before you can swear. Clip in her teeth. She looks at you once, by eye, top to bottom."
        mr_costumer "\"Told you. Coming in faster than slots on payout day.\""
        "She lets the seam out a notch, and the thighs, and snaps the clip back on."
        mr_costumer "\"There.\""
        "You turn sideways in the mirror. Your ass rounds out the back of the leotard like it was cut for it. Your thighs whisper together every time you shift your weight."
        vn_sfx "Shff. Shff."
        show mr_pc grin at vn_pc_slot
        mr_vic "\"System's paying out.\""
        mr_costumer "\"Something is.\""
        "She goes."
        hide cg onlayer cgl
    elif _n == 4:
        $ mr_body(4)
        $ mr.fit = "suit"
        $ vn_enter(bg="mr_locker", pc="shocked", pc_tag="mr_pc", cg="mr_locker_r4")
        "You can feel it before you've got the suit off the hook. Last night's roll is still running."
        "{color=#ff9ecb}You pull the leotard up and it stops at your thighs. They're {i}huge{/i}. Plush and pale and pressed together so tight there's no gap at all, soft as dough when you squeeze.{/color}"
        "You wriggle the suit up over your ass a little at a time, and your ass {i}bounces{/i} back every time it snaps free, round and heavy and way too big for the seat."
        mr_vic "\"Nnh— come {i}on{/i}—\""
        "{color=#ff9ecb}Your hips have gone out past the cut of the suit on both sides. Your tits are heavier than last night, sitting high and fat in the cups. Your fingers on the zip look slim. Your face in the mirror is softer. Your hair brushes your shoulders when you shake your head.{/color}"
        "The vinyl drags over your ass and you moan out loud, because your ass is {i}so{/i} sensitive now the seat of the suit feels like a hand."
        mr_vic "\"{i}Mmh{/i}— my {i}mouth{/i}— everything's turned {i}up{/i}—\"" with vnfx("shake")
        "{color=#ff9ecb}And your cock. You look down. It's {i}tiny{/i}. A soft little thing, barely there, lost in the pouch of the suit with almost nothing to hold. You poke it and it just flops.{/color}"
        mr_vic "\"Oh my god. Look at me. {i}Look{/i} at me. That's the whole hot roll, right there, banked in {i}ass{/i}—\""
        "Your scalp prickles under the costume ears, a soft itch right where they sit. You rub at it and grin."
        show cg mr_costumer_end onlayer cgl
        "The costumer comes in, looks at you, and lets the clip out to the very end."
        "That's it. There's no more seam to give."
        hide cg onlayer cgl
    elif _n == 5:
        $ mr.fit = "suit"
        $ vn_enter(bg="mr_locker", pc="grin", pc_tag="mr_pc", cg="mr_locker_recut")
        "Dusk. Your locker. The suit's on the hook, pressed, and it's been recut while you were out: let out at the hips, the thighs, the chest, and taken in at the crotch."
        "Cut for the thicker you, and the tighter, smaller cock."
        "Nobody told the costumer you were taking a day off. Nobody needed to."
        "You pull it on. It closes round you like a hand. You turn in the mirror, and your ass rounds out the hem, and your tits wink at you over the neckline."
        hide cg onlayer cgl
        show mr_simone smirk at vn_cast_slot
        "Simone's leaning on the rail outside when you walk out. You wink at her. You flick her a chip you don't have."
        mr_vic "\"I'm back. Did you miss me?\""
        "She doesn't answer. She doesn't have to."
    elif _n == 6:
        $ mr.fit = "suit"
        $ vn_enter(bg="mr_locker", pc="neutral", pc_tag="mr_pc", cast=[("mr_costumer", "neutral")], cg="mr_carrot_pin")
        "You hang the costume ears on the hook. They don't go on over the real ones. You tried. The real ones just flick them off."
        "The costumer clips a little enamel carrot pin into your hair instead, above one ear, and steps back."
        mr_costumer "\"House colours. Don't lose it.\""
        hide cg onlayer cgl
        show mr_pc grin at vn_pc_slot
        "Black waves, red mouth, two soft ears straight up, the pin glinting. The suit holds you like it's proud of you."
    elif _n == 7:
        $ mr.fit = "suit"
        $ vn_enter(bg="mr_locker", pc="grin", pc_tag="mr_pc", cast=[("mr_simone", "hungry")])
        "The schedule's taped inside your locker door. Your name in print, and under it, tonight, in Odette's hand: {i}Private room.{/i}"
        "You do your face in the locker mirror. Red mouth. Black lashes. Your ears flick forward, eager."
        mr_simone "\"He's waiting, bunny.\""
        jump mr_private_room
    jump mr_floor

## Rung 2's body, at the first zip-up in the locker mirror. The suit doesn't make the shape; it shows
## it. "I'm due", the first of three. Simone calls you "bunny" from here.
label mr_first_zip:
    $ mr_body(2)
    $ mr.fit = "suit"
    $ vn_enter(bg="mr_locker", pc="shocked", pc_tag="mr_pc", cg="mr_firstzip")
    "Your locker has a strip of tape on it with your name. The hire hangs on the hook."
    "You step into the leotard and pull. It stops at your hips. You pull harder, and wriggle, and it goes, and you zip it up the back by feel."
    "And then you look in the mirror."
    "{color=#ff9ecb}It doesn't just fit. It {i}fits{/i}. The vinyl squeezes in hard at your waist and flares out over hips you didn't have yesterday. Your ass fills the seat of it, round and high, the little white tail perched right on top like it's pointing.{/color}"
    mr_vic "\"Huh.\""
    "You turn sideways."
    "{color=#ff9ecb}Your thighs press together under the fishnets. When you shift your weight they brush, soft and warm, and every brush sends a hot little tweak straight up the middle of you.{/color}"
    "{color=#ff9ecb}Your nipples are poking out against the vinyl. Puffy. Swollen. You press a fingertip to one through the suit and gasp out loud.{/color}"
    mr_vic "\"Nnh—!\"" with vnfx("shake")
    "{color=#ff9ecb}And the bulge in the front of the suit is smaller than it should be. Your cock's straining in there, hard, but it's a step down from yesterday, tucked up neat in the crotch, throbbing at every brush of the vinyl.{/color}"
    "You grab your own ass with both hands and squeeze, and it's plush, and it {i}bounces{/i}, and the squeeze goes right through you."
    mr_vic "\"Okay. Okay, that's— the suit's doing work—\""
    "The suit doesn't make the shape. It shows it. You look over your shoulder at the tail, and you feel the grin take over your whole face."
    show mr_pc grin at vn_pc_slot
    mr_vic "\"I'm due. I am {i}so{/i} due.\""
    hide cg onlayer cgl
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"Suit looks right. You fill it out, bunny.\""
    "Simone, leaning in the doorway, black satin, arms folded, taking a good long look at your ass."
    mr_vic "\"At the staff rate, it almost pays for itself.\""
    mr_simone "\"Almost.\""
    "The costumer does your face before she lets you out: red lips, black lashes, a smoky lid, a little blush high on the cheek. You don't argue. Full dress is full dress."
    jump mr_floor

## ==== THE FLOOR: a station, and the staff rate's extras ======================================

label mr_floor:
    $ _n = mr.night
    $ vn_enter(bg="mr_floor", pc="grin", pc_tag="mr_pc")
    if _n == 2:
        "The floor, in the suit. Heels clicking. Thighs brushing. Every step a little swing you didn't put there on purpose."
        "You catch yourself in the freezer glass behind the bar as you bend for a tray, and you have to look twice. That ass. Is that {i}your{/i} ass?"
    elif _n == 3:
        "The floor. You're a regular now, apparently. The bar staff call you \"bunny\" too. The punters look at your thighs, then up at your face, then back at your thighs."
    elif _n == 4:
        "The floor. The whole place is still talking about the hot roll. A table of suits raises their glasses at you when you go by."
        show mr_waitress neutral at vn_cast_slot
        "A cocktail waitress from the night shift falls in beside you with a tray of sours. Forties, sharp-eyed, been here forever."
        mr_waitress "\"You're up. You should walk, hon.\""
        mr_vic "\"Leaving while you're up {i}is{/i} the house edge. Every streak's got a middle. Walk at the middle and somebody else gets the late luck. That somebody's me.\""
        "You tip her a wink."
        mr_waitress "\"Die on your hill, then, hon.\""
        hide mr_waitress
    elif _n == 5:
        "The floor, at night, after a whole day of daylight. It's like climbing back into a warm bath."
    elif _n == 6:
        "The floor. Heads turn. Heads {i}keep{/i} turning. A man at the craps rail forgets to throw. Your ears swivel at every whistle, and every whistle is for you."
    menu:
        "Where do you want to work?"
        "Run drinks":
            $ mr.station = "drinks"
        "Work the roulette rail":
            $ mr.station = "roulette"
        "Work the craps rail":
            $ mr.station = "craps"
    $ vn_pass(30)
    jump mr_station

label mr_station:
    $ _n = mr.night
    $ vn_enter(bg={"roulette": "mr_floor", "craps": "mr_craps"}.get(mr.station, "mr_floor"), pc="neutral", pc_tag="mr_pc")
    if mr.station_seen != _n:
        $ mr.station_seen = _n
        if mr.station == "roulette":
            "You work the roulette rail: stacking, sweeping, leaning over the felt to push winnings across. Every lean puts your ass in somebody's face. Every somebody tips."
        elif mr.station == "craps":
            "You work the craps rail, handing back dice with a little bow. The shooters blow on them and then look at your mouth."
            "\"For luck,\" one says, and holds the dice up to your lips."
        else:
            "You run drinks. Tray up, hips swinging, heels clicking between the tables. Every time you bend to set a glass down, the whole table goes quiet."
    else:
        "Back at your station. The floor hums around you."
    if _n == 3:
        "The craps table at the back is calling for a shooter. Somebody's calling {i}you{/i}."
    elif _n == 4:
        "The high-stakes pit has a seat open, and your roll's still in your fingers."
    elif _n == 6:
        "A floor runner touches your elbow."
        "\"Mr. Royce asks for you at baccarat.\""
    menu:
        "Your shift."
        "Play the wheel at the staff rate" if _n == 2:
            jump mr_roulette
        "Take the dice" if _n == 3:
            $ mr.point = 0
            jump mr_hot_roll
        "Sit in at the poker pit" if _n == 4:
            jump mr_poker
        "Work the floor till close" if _n == 5:
            $ vn_until(4)
            jump mr_reading
        "Go to the baccarat table" if _n == 6:
            jump mr_baccarat
        "Sit in at Tam's table":
            jump mr_tam_table
        "Simone's break" if mr_break_open():
            jump mr_break

## Tam's table at the staff rate: a real hand that moves nothing. One book line in the current
## currency, from Odette, passing behind you.
label mr_tam_table:
    $ vn_enter(bg="mr_tamtable", pc="grin", pc_tag="mr_pc", cast=[("mr_tam", "neutral")])
    "Tam deals you in without a word. He never says anything. He just looks at your hand, and then, for half a second, at you."
    call mr_bj_hand("Tam")
    if mr_bj.result == "natural":
        show mr_pc grin at vn_pc_slot
        "A natural. You squeal and bounce on your stool, and half the table looks at what bounces."
    elif mr_bj.result == "win":
        mr_vic "\"Told you. {i}Hot.{/i}\""
        "Tam pays it."
    elif mr_bj.result == "push":
        "A push. Tam slides it back."
    else:
        show mr_pc nervous at vn_pc_slot
        "Tam sweeps it."
        mr_vic "\"Correction. Just a correction.\""
    $ _hl = mr_hand_line(mr_bj.result)
    "Odette, passing behind you with the book under her arm, doesn't stop. She doesn't need to. She just says it to the air."
    hide mr_tam
    show mr_odette neutral at vn_cast_slot
    mr_odette "{color=#f3c969}\"[_hl]\"{/color}"
    menu:
        "Tam squares the shoe."
        "Another hand":
            jump mr_tam_table
        "Back to your station":
            jump mr_station

## Rung 2's game: a run at roulette at the staff rate, then the zero. Corners and columns, never
## numbers. The voice goes rounder by the end of the shift.
label mr_roulette:
    $ vn_enter(bg="mr_floor", pc="grin", pc_tag="mr_pc", cg="mr_roulette_win")
    "Roulette at the staff rate. Half the house edge. You'd have married it if it asked."
    "You stalk the wheel. You learn its bounce."
    "You play corners and columns, chips tucked between your knuckles, a bunny-girl pinball in heels, and the croupier smiles every time your stack gets fatter."
    "And you {i}win{/i}."
    vn_sfx "Klak-klak-klak."
    "Red. Your corner. The ball drops right in."
    mr_vic "\"Get in while it's hot!\""
    "You slide a tip across with an exaggerated bounce of your hips."
    "Again. Your column. The table cheers."
    "Again. You shriek and hop on your heels and your ass jiggles under the tail, and a man at the rail actually drops his drink."
    "{color=#ff9ecb}You hear it before you feel it. Your voice. Every time you call a bet, it comes out a little rounder, a little sweeter, sliding up into a register you never had, like there's honey on the back of your throat.{/color}"
    mr_vic "\"Press it! Press it, come {i}on{/i}—!\"" with vnfx("shake")
    "Higher. Brighter. A girl's squeal at the top of it."
    "The heat's been building all night. The thighs rubbing. The suit biting. The tips. Your cock's rock hard in the hug of the vinyl and you're trying not to palm yourself at the felt."
    mr_vic "\"Let it ride. All of it. Let it {i}ride{/i}.\""
    "The ball goes round. Round. Round."
    show cg mr_roulette_zero onlayer cgl
    vn_sfx "Klak." with vnfx("flash")
    "The zero."
    "The whole stack goes in one sweep of the croupier's rake. You don't even flinch. There's a perfect little kernel of joy in it: the tip you just gave was from money you never had."
    mr_vic "\"Correction. Just a correction.\""
    $ vn_until(3)
    jump mr_corridor

## ==== NIGHT 3: the hot roll (rung 3) ==========================================================

## The chest grows on every point the table cheers (setup.markersRoll), the cup edge fails, the seam
## splits, one breast spills free. The stickman's calls are patter. Pressing or riding is flavour.
label mr_hot_roll:
    $ _p = mr.point or 0
    if _p == 0:
        $ vn_enter(bg="mr_craps", pc="grin", pc_tag="mr_pc", cg="mr_roll_buds")
        "Ivory clatter. The fat thud of dice on felt. Two dealers, a sleepy stickman, a crowd of floor staff at the rail with their uniforms tight at the hips."
        "And you, with the dice."
        "Your palms stick to them. Your skin's too smooth for friction. Every eye at the table is on you as you flick them out with a lazy little twist."
        mr_stick "\"Six, the hard way!\""
        "The table whoops."
        "{color=#ff9ecb}Heat. Right behind your nipples. A prickling, swelling heat, like someone rubbed something warm in under the edge of the suit. You look down. Two little buds have come up under the vinyl, soft and pointed and new.{/color}"
        mr_vic "\"{i}Oh{/i}—\""
        "Simone's leaning on the rail behind you. She winks, slow."
    elif _p == 1:
        show cg mr_roll_handfuls onlayer cgl
        mr_stick "\"Easy eight! Winner!\""
        "{color=#ff9ecb}It comes in a throb. The buds fill. Swell. Push out into the cups of the suit in soft warm mouthfuls until there's something there to {i}hold{/i}: real handfuls, round and heavy, bouncing when you shake the dice.{/color}"
        mr_vic "\"Ahh— {i}hah{/i}— they're— oh my {i}god{/i}—\"" with vnfx("shake")
        "You grab one with your free hand. It squishes. It's {i}real{/i}."
        "The table roars. Somebody slaps the rail. Somebody shouts \"Roll 'em, bunny!\""
    elif _p == 2:
        show cg mr_roll_tight onlayer cgl
        mr_stick "\"Hard ten! Pay the line!\""
        "{color=#ff9ecb}Bigger. You feel it with every breath, every breath squeezing you tighter into the suit. The cups were made for the poster girl and they're not enough. The edges dig. Your nipples are rock hard, grinding against the inside of the vinyl.{/color}"
        mr_vic "\"Nnh— it's tight— it's so {i}tight{/i}— {i}don't stop the roll{/i}—\""
        "Security's watching. That's a whole different flavour of adrenaline. Nobody stops you."
        show mr_simone neutral at vn_cast_slot
        mr_simone "\"You want to lock this in, bunny?\""
        "At your ear. Her eyes on your chest."
        mr_vic "\"Let it {i}RIDE{/i}!\"" with vnfx("shake")
    elif _p == 3:
        show cg mr_roll_surge onlayer cgl
        mr_stick "\"Nine! Nine, centre field!\""
        "{color=#ff9ecb}Your tits surge forward on one long exhale, so fast it almost tips you off your heels. The cup edges dig, then slip, then give up. Your nipples poke out against the thin vinyl in two obscene peaks.{/color}"
        "You squeeze your arms in to hold it all and it just bulges up between them, soft and enormous, wobbling."
        mr_vic "\"Look at them— {i}look{/i} at them— the table's paying out in {i}tits{/i}—\""
        "The whole casino seems to lean your way. Ten deep at the velvet ropes. Somebody's stacking purples with shaking hands."
    else:
        $ mr_body(3)
        show cg mr_roll_split onlayer cgl
        mr_stick "\"Winner, winner! Pay the line, pay the shooter!\""
        vn_sfx "Zzrrip!" with vnfx("flash")
        "{color=#ff9ecb}Something gives with a sound like a zip. The seam. It splits right down the side, and your right tit spills free, out into the casino air, heavy and round, the nipple fat and glossy and pink.{/color}"
        mr_vic "\"{i}Ahh{/i}— oh {i}fuck{/i}—!\"" with vnfx("shake")
        "{color=#ff9ecb}Everything goes at once. Your hips push out bolder, wider, the suit creaking over them. Your hair falls in your eyes, down to your jaw now. And your voice, when you shriek, is syrupy and high, pure sugar, a girl's voice at full volume over the whole pit.{/color}"
        "You look down past them. Past {i}them{/i}. Your cock's still hard in the crotch of the suit, and it looks so small down there now. Tiny, under all that."
        "You grab both tits and lift them and squeeze, and they spill over your fingers, and you moan out loud in front of everyone."
        mr_vic "\"{i}Mmmh{/i}— they're so {i}heavy{/i}— I {i}rolled{/i} for these—\""
        mr_stick "\"That is the roll people tell stories about.\""
        "The croupier hits the comp button, and her eyes slide right back to your chest."
        mr_croupier "\"Room upstairs. On the house.\""
        jump mr_suite
    menu:
        "The dice come back to you, warm."
        "Let it ride":
            pass
        "Press it":
            pass
    $ mr.point = _p + 1
    $ vn_pass(3)
    jump mr_hot_roll

## The replacement suit. Its tag is the route's one cup letter (DD). The split one is folded in your
## locker "for luck". The heels stop being something you think about.
label mr_new_suit:
    $ mr.kit = max(mr.kit or 0, 2)
    $ mr.fit = "suit"
    $ vn_pass(60)
    $ vn_enter(bg="mr_locker", pc="grin", pc_tag="mr_pc", cg="mr_newsuit")
    "The costumer has a new suit on your hook before you get back down. Same black vinyl, same tail, a whole size up in the chest and the hips."
    "You turn the tag over."
    "{color=#ff9ecb}DD{/color}, it says, in her handwriting."
    mr_vic "\"DD. That's {i}mine{/i}.\""
    "You squeeze yourself through the vinyl, and giggle."
    "The split one goes on the shelf in your locker, folded."
    mr_vic "\"In case the run continues.\""
    "The costumer doesn't argue."
    hide cg onlayer cgl
    "Your lips are still buzzing from the suite. You lick them on the stairs and moan out loud, right there, at nothing. Your mouth's so sensitive now it's like a second pair of nipples."
    "You walk back out onto the floor and your heels just... go. Click, click, click. You don't wobble. You don't think about them at all."
    "The hot roll is the only thing anybody at the bar can talk about. Half your next shift gets comped for the gossip."
    $ vn_until(4)
    jump mr_reading

## ==== NIGHT 4: one hand of poker (rung 4) =====================================================

## Ace-queen, three raises; queens to trips on the turn; the king on the river; king-king takes it.
## Cards are named, never counted.
label mr_poker:
    $ vn_enter(bg="mr_poker", pc="grin", pc_tag="mr_pc", cg="mr_poker_hole")
    "The high-stakes pit. Clover-green felt, the real money, the real silence."
    "You never play short-stack. Wager too little and the table knows you're about to leave."
    "Tonight you buy in with everything the hot roll paid you, every chip, all the way back, because tonight you're getting {i}free{/i}."
    vn_sfx "Thump."
    "Your tits settle on the rail. The whale three seats down can't stop looking. A pair of property guys can't stop looking. Good. They watch you, not your chips."
    "Simone leans on the rail behind the pit like a goddess waiting for tribute."
    "You look at your hole cards."
    "Ace. Queen."
    "A painting of a hand. A romance. You call one raise, then another, then a third, sliding columns of chips out with your slim new fingers."
    "The flop: king, queen, seven."
    "The whale bets. You call. The property guys fold. A quiet man in a grey suit stays in, eyes flat."
    "The turn: another queen."
    vn_th "(Trips.)"
    "Your nipples go tight in the suit. You bet more than you meant. The quiet man raises. You call, because what else do you do when the deck writes you a miracle."
    "The river: the king."
    "Check. Check. You shove the rest of it in with a little flourish, one arm squeezing your tits together so they wobble, your most perfect floor smile."
    "The whale thinks for a long time and calls. The quiet man pushes in behind him without a word."
    "Showdown."
    show cg mr_poker_river onlayer cgl
    "The quiet man turns over a king."
    "And another king." with vnfx("flash")
    "No outs. No future. A hand so clean it's almost beautiful, and the dealer sweeps your mountain of chips away like snow off a step."
    show mr_pc shocked at vn_pc_slot
    "Somewhere behind you, the measured click of flats on tile. Odette always shows up for the reading."
    jump mr_offer

## The book read at the table, and Odette's line: "You can always walk. The marker walks with you."
## It's a line, never a link, and the house never lies: walking clears nothing.
label mr_offer:
    $ vn_enter(bg="mr_poker", pc="nervous", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_offer")
    "Odette lifts the book. The whole table watches."
    mr_odette "{color=#f3c969}\"Game: poker. Stake: everything back. Result: lost in one hand. Balance after: everything, carried.\"{/color}"
    "She doesn't blink. Then her voice goes softer than you've ever heard it. No mockery in it at all. Just a fact, read out of the small print."
    mr_odette "\"You can always walk, Vic. The marker walks with you.\""
    "She holds the book out, pen uncapped."
    "For maybe the first time, you hesitate."
    vn_th "(You could walk. And the marker would come with you, carried forever, everything, in a column you can't play down from the street. In here, at least, there's a table."
    vn_th "Probability only works if you keep going.)"
    mr_vic "\"That's not a choice. That's a— that's a {i}trap{/i}, that's what that is.\""
    "Odette waits. The pen waits."
    menu:
        "The pen's uncapped in her hand."
        "Hand back the pen":
            $ mr.pen = "hand"
        "Push the book back across the felt":
            $ mr.pen = "push"
    jump mr_lounge

## ==== NIGHT 5: the day off (sign-off decision 10) =============================================

## "You can always walk. The marker walks with you" gnaws at you, so you try. It ends at the locker
## at dusk. No body change: the mirror shows rung 4's body.
label mr_day_off:
    $ mr.fit = "own"
    $ vn_enter(bg="mr_houseroom", pc="nervous", pc_tag="mr_pc")
    "Morning. Actual morning, with daylight in it, and for once you're awake for it."
    "You lie in the house room and stare at the ceiling."
    vn_th "({i}You can always walk. The marker walks with you.{/i} She meant it. The house would let you go, and the marker would come too.)"
    vn_th "(Well, then. You'll walk it. A day off. Proof of concept. Go to work like a normal person, play a hand like a normal person, and see how you feel.)"
    "Your own clothes are in the wardrobe. Your work shirt. Your trousers. Your good shoes."
    "You get the trousers up over your ass by lying on the bed and wriggling. You get the shoes on. You get the shirt on."
    show cg mr_dayoff_shirt onlayer cgl
    "The shirt won't button."
    "It goes round you and stops short, your tits pushing straight out through the gap. You pull. You suck in."
    "The buttons sit there on one side and the holes sit there on the other, never to meet."
    show mr_pc grin at vn_pc_slot
    mr_vic "\"Laundry. Shrank.\""
    "You put your jacket on over it and button that instead. It sort of holds."
    hide cg onlayer cgl
    $ vn_pass(60)
    $ vn_enter(bg="mr_showroom", pc="nervous", pc_tag="mr_pc", cg="mr_showroom_vic")
    "The showroom's in a strip mall out past the ring road. Beige tile. Sofas in rows. The coffee's the same as ever."
    "You stand by a corner unit with your tits pressing the buttons of your jacket and try to sell a recliner to a couple in their sixties. The husband can't look at you."
    "The wife can't look anywhere else."
    mr_vic "\"It's very— supportive.\""
    "It comes out high and sweet and nothing like your sales voice."
    "Every time you sit to demonstrate a sofa, your ass spreads out across the cushion. Every time you stand, it takes a second to follow you up."
    "Every time you bend to show them the footrest, the whole showroom goes quiet."
    "You don't sell the recliner."
    vn_th "(By lunch you've done the arithmetic: the commission against the staff rate at the Golden Hare. It's not even close. Honestly, it's embarrassing you ever came in.)"
    hide cg onlayer cgl
    $ vn_set_time(15, 0)
    $ vn_enter(bg="mr_punters", pc="grin", pc_tag="mr_pc", cg="mr_punters_hand")
    "The Golden Hare in the afternoon is a different animal. Half the tables under covers. Daylight in the lobby. The machines chiming to nobody."
    "You walk in through the front door in your own clothes, like a punter, and ask for a seat at the punters' table like it's your first time."
    "The pit boss on days gives you a knowing little nod and doesn't say a word about the marker."
    "You put your pocket money on the felt."
    hide cg onlayer cgl
    "The day dealer is quick and bored and completely fair."
    call mr_bj_hand("The dealer")
    if mr_bj.result in ("natural", "win"):
        "The dealer pays you. You look at the little stack."
        mr_vic "\"Let it ride.\""
        "Of course you do. The next one comes up a picture and an ace for the house, and the pocket money's gone."
    elif mr_bj.result == "push":
        mr_vic "\"Again.\""
        "A push, then the next one goes to the house, and so does the pocket money."
    else:
        "The dealer sweeps it. Pocket money, gone."
    "That took no time at all. You sit there with your hands flat on the felt and feel... fine. Great, actually. Like you finally got some air."
    mr_vic "\"Excuse me.\""
    $ vn_enter(bg="mr_punters", pc="shocked", pc_tag="mr_pc", cg="mr_mirror")
    "The washroom has a long mirror over the basins and very good light."
    "You take your jacket off to wash your hands, and you catch yourself."
    "Your tits fill the open shirt like they're trying to climb out of it. Huge. Glorious. Even fuller than you remember, as if popping all those buttons let them breathe."
    "Your hips stick out past your trousers on both sides. Your ass is a whole separate event behind you."
    "You turn sideways. You turn back. You put both hands under your tits and lift and let go and watch them bounce."
    mr_vic "\"Okay. Okay. That's— that's the house's money, that is. That's {i}banked{/i}.\""
    "And you know exactly where it's banked. Downstairs. On a hook. With your name on the door."
    "You don't even pretend to argue."
    hide cg onlayer cgl
    $ vn_set_time(19, 30)
    jump mr_locker

## ==== NIGHT 6: nights, at the staff rate (rung 5) =============================================

## Royce's baccarat table; Odette inks the new column; the printout ("Hollan, V. - Miss"); Royce
## reads it out: "Miss Hollan." The "she" beat, one beat before the cock goes.
label mr_baccarat:
    $ vn_enter(bg="mr_baccarat", pc="grin", pc_tag="mr_pc", cast=[("mr_royce", "smirk")], cg="mr_baccarat_royce")
    "Harlan Royce plays baccarat like a man who owns his own treasury."
    "Fifties, silver at the temples, a melting drink at his elbow, chip towers going up and toppling over in opposite directions."
    "He's rarely wrong about the cards and always wrong about the bets, and he loses like an emperor."
    "He claps you on the shoulder when you arrive, hard enough to make your ears flick."
    mr_royce "\"There she is. You've got the lucky hands. Ready to ruin my good run?\""
    mr_vic "\"Only if you can stand the volume. Staff rate, you know. You should ask for it. They'll only laugh at you twice.\""
    "The voice that comes out is all sugar."
    "He barks a laugh and shoves a stack onto the tie out of pure whimsy."
    mr_royce "\"If I could wear that suit, I would. Play me in.\""
    "You deal him a run that wins him nothing and loses him a fortune, and he's delighted."
    "Every time you lean to the shoe your tits tip forward over the felt, and every time, he looks, and smiles, and loses."
    show cg mr_nights_book onlayer cgl
    "On the third shoe, Odette stops behind you with the book."
    "She opens it on the rail. A new column, ruled down the edge of the page, inked in blue. One word at the top."
    "{color=#f3c969}{i}Nights.{/i}{/color}"
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"From tonight, the house quotes your marker in nights. At the staff rate. You're on the schedule until the balance is settled.\""
    show cg mr_printout onlayer cgl
    "She hands you a printout. Your schedule. Your name in block print at the top."
    "{color=#f3c969}{i}Schedule: Hollan, V. — Miss.{/i}{/color}"
    mr_vic "\"You're actually putting me on the schedule?\""
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"Staff must be printed. For insurance purposes.\""
    "Royce leans over and plucks it out of your fingers. Reads it. Reads it out loud, slowly, savouring every syllable."
    hide mr_odette
    show mr_royce smirk at vn_cast_slot
    mr_royce "\"Miss Hollan.\""
    vn_sfx "Click."
    "And that's just your name now. It lands in you like a chip on felt and stays there. Your ears go hot. Your thighs press together."
    hide mr_odette
    show mr_royce smirk at vn_cast_slot
    mr_royce "\"Nights, at the staff rate? That'll take you till Christmas, darling. Want me to buy you out?\""
    vn_th "(It doesn't scare you. It doesn't even sound funny. It just sounds like {i}maths{/i}.)"
    mr_vic "\"I'll run my own numbers. I've got an edge. Uniform edge. You should try it, Mr. Royce. You'd just have to wear the heels.\""
    "He laughs, and his smile warms all the way up."
    hide mr_odette
    show mr_royce smirk at vn_cast_slot
    mr_royce "\"All right, Miss Hollan. Run it up.\""
    "Odette uncaps her pen over the Nights column."
    jump mr_nights_column

## Rung 5's second landing, on the page: as Odette inks the column, the cock goes and the hips
## spread wider.
label mr_nights_column:
    $ vn_enter(bg="mr_baccarat", pc="shocked", pc_tag="mr_pc", cast=[("mr_royce", "smirk")], cg="mr_nights_ink")
    "The nib touches the page."
    "{color=#ff9ecb}And something between your legs {i}pulls{/i}.{/color}"
    show cg mr_cock_goes onlayer cgl
    "{color=#ff9ecb}A long, slow, sweet tug, drawing inward, up, in. You grab the edge of the table. Your tiny cock, already only a nub in the suit's pouch, draws up and in and up and {i}in{/i}, smaller, smaller, a soft little press, and then—{/color}"
    mr_vic "\"Oh— oh, {i}wait{/i}— oh my {i}god{/i}—\"" with vnfx("shake")
    "{color=#ff9ecb}—it's gone. Nothing there. The suit's crotch presses flat against you, and under it something's opening, plump and hot and slick, two soft lips parting round a hard little bud that throbs every time your heartbeat does.{/color}"
    "{color=#ff9ecb}And your hips. They spread. The bones shift and roll out wider under the suit until the vinyl stretches almost to splitting, your ass pushing back off the stool, your thighs going soft and heavy, your whole lower half settling into a shape it was always heading for.{/color}"
    mr_vic "\"{i}Hhhah{/i}— I can feel it— I can feel it {i}open{/i}— {i}ahh{/i}—\""
    "The little bud at the top of it throbs, and throbs, and every throb is like a tongue."
    mr_vic "\"It's so {i}sensitive{/i}— I can't— I can't sit {i}still{/i}—\"" with vnfx("flash")
    "You're wet. You're {i}so{/i} wet. You can feel it soaking into the suit, and you're squirming on the stool, and your clit grinds against the seam every time you move."
    "Odette finishes the line. Blots it. Doesn't look up."
    mr_royce "\"Well. That's the real comp tonight, isn't it.\""
    mr_vic "\"Comps just keep getting {i}tighter{/i}.\""
    jump mr_orientation

## After orientation: you argue the conversion and get worse terms; then, at closing, the pot. Kept
## (owner, 2026-10-19/20): staking himself is the gambler's last chase, the one thing Vic does on his
## own. What the pot buys is still collected by force.
label mr_the_pot:
    $ mr.schedule = True
    $ vn_pass(60)
    $ vn_enter(bg="mr_lounge", pc="grin", pc_tag="mr_pc", cast=[("mr_simone", "smirk")])
    "Later, in the staff lounge, you sit bare-assed on the couch with Simone sprawled beside you and the schedule tucked in the pocket of your suit. Your name in print."
    "Not a pound in sight."
    "Nights. That's the currency now."
    show mr_odette neutral at vn_cast_slot
    "You catch Odette by the manager's office, schedule in hand."
    mr_vic "\"Listen. You're running that conversion way too steep. The marker was written against table play, not wages. You're not even counting tips. Mr.\""
    mr_vic "\"Royce tipped the whole {i}pit{/i} for the show tonight—\""
    mr_odette "\"Conversion is reviewed quarterly. Tips are retained against comped meals.\""
    mr_vic "\"That's a racket!\""
    mr_odette "\"The house will permit overtime.\""
    vn_th "({i}Overtime.{/i})"
    mr_vic "\"So I can double-shift against the balance?\""
    mr_odette "\"On approval.\""
    "You whoop out loud, high and bright, and Simone, sprawled on the couch behind you, starts to laugh."
    show mr_simone smirk at vn_cast_slot
    mr_simone "\"That's the first time anyone's ever got {i}worse{/i} terms out of Odette. Congratulations, Miss Hollan. You're officially staff.\""
    $ vn_until(3)
    $ vn_enter(bg="mr_baccarat", pc="grin", pc_tag="mr_pc", cast=[("mr_royce", "neutral")], cg="mr_pot")
    "At closing, you go back out to the pit. Nobody steers you there. Nobody's hand is on the back of your neck. It's the one thing in this building you do all by yourself."
    "Royce is gathering his last chips. You lean right over the rail, your tits on the felt, your ears tipped forward."
    mr_vic "\"All chips, Mr. Royce. One hand. Winner takes all.\""
    "You smile."
    mr_vic "\"And I'm the pot.\""
    "He doesn't even pretend to think about it."
    mr_royce "\"Done.\""
    vn_th "(The edge is calculable. The book will clear. By your numbers it's freedom, and finality, and the best bet you ever made.)"
    "You go to Odette with the terms before he's out of his chair."
    $ vn_until(4)
    jump mr_reading

## ==== NIGHT 7: the private table (rung 6) =====================================================

## You're the stake; you don't touch the cards. Simone fucks your tits while Royce squeezes his, and
## you come from your chest alone: everything surges, and the cottontail is yours. Non-con: you
## staked yourself, but the collection is by force.
label mr_private_room:
    $ vn_pass(20)
    $ vn_enter(bg="mr_privateroom", pc="grin", pc_tag="mr_pc", cast=[("mr_royce", "smirk")], cg="mr_private_room")
    "The back of the Golden Hare. The part of the house you've never seen."
    "Polished floors. A baccarat table laid for four under one low gold lamp. A wall of mirrors behind the shoe."
    "Two senior server-bunnies in matching corsets, posture perfect, pouring gin at the edge of the light."
    "It smells of card ink and lacquer, and it's the quietest room in the building."
    "Royce is already in his chair, rolling a chip over his knuckles. Odette sits at the banker's place with the book open in front of her."
    "Simone stands by the wall in black satin, arms folded, a shape down the front of her slacks that's already heavy."
    "And you sit at the head of the table on a high padded chair, in the suit, with your hands flat in your lap."
    "That's the rules. Simone and Odette drew them up, a whole page of them, and slid it across with the pen."
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"Do you read the back?\""
    "You didn't. You don't touch the cards. You don't move, unless somebody moves you."
    hide mr_odette
    show mr_royce smirk at vn_cast_slot
    mr_royce "\"Ready, darling?\""
    mr_vic "\"Ready as the deck.\""
    vn_th "(The maths is the anchor. The maths says you win this.)"
    "One of the bunnies cracks the seal on a fresh deck. Odette shuffles, loads the shoe, burns the top card."
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"No more bets.\""
    "Two cards to Royce, face down. Two cards to the bank, face down, in front of your place. You don't touch them. Your thighs are pressed together so tight they're slippery."
    "Royce picks his up in his left hand and starts to squeeze. Slowly. One edge at a time."
    show cg mr_private_display onlayer cgl
    "And Simone steps up behind you and peels the top of your suit down to your waist."
    "Your tits fall out into the lamplight. The bunnies stop pouring. In the mirror, every eye in the room is on you."
    show mr_pc shocked at vn_pc_slot
    mr_vic "\"Hey— {i}hey{/i}— that's not in the— the stake's {i}me{/i}, not the— the hand's not even {i}played{/i}—\""
    "Simone holds them up from behind, one in each big hand, and turns you a little toward the table. {i}Showing.{/i} Presenting the house's property to the room."
    "Your nipples go tight in the cool air and you try to twist away, and her hands don't let you, and the rules don't let you, and your nipples only get tighter."
    show cg mr_private_titjob onlayer cgl
    "She spits in her palm. Slicks your cleavage. Steps round in front of you and lays her cock between your tits, hot and heavy, the head nudging your chin."
    mr_vic "\"No— Simone, {i}no{/i}, the hand's still— wait for the {i}hand{/i}—\""
    hide mr_royce
    show mr_simone neutral at vn_cast_slot
    mr_simone "\"You're on display, bunny. The house collects while it deals.\""
    vn_sfx "Pap. Pap. Pap."
    "She fucks them. Slow, deep, the underside of her cock dragging hot up through your cleavage on every stroke, your tits squeezed round her in her hands."
    "You watch it in the mirror. You watch Royce watching it, his cards half turned in his fingers."
    mr_vic "\"Stop— stop it— {i}nnh{/i}— not in front of— {i}ahh{/i}— {i}ahh{/i}— Simone—\"" with vnfx("shake")
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"No natural. Third card to player.\""
    "She flicks one out of the shoe. Royce squeezes it. His shoulders drop."
    "Simone changes her angle and the head of her cock grazes up under your chin, and the heat of her, and the room's eyes, and the rules, and you're still saying {i}no{/i} when you can't hold it."
    hide mr_royce
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"Bank stands. The house wins.\""
    $ mr_body(6)
    $ mr.kit = 5
    show cg mr_private_surge onlayer cgl
    "{color=#ff9ecb}You come from your chest alone. It rips through you from your nipples down, and as it hits, {i}everything{/i} goes.{/color}" with vnfx("flash")
    "{color=#ff9ecb}Your tits surge in Simone's hands, swelling out between her fingers, past her fingers, heavier and heavier until she can't hold them at all and they pour over her wrists.{/color}"
    "{color=#ff9ecb}Your hips roll out wide off the chair. Your ass spreads under you, huge, the seat of the suit creaking and giving way.{/color}"
    mr_vic "\"{i}Ahh{/i}— {i}AHH{/i}— it's all— it's all going— {i}look{/i} at me—\"" with vnfx("shake")
    "Everything's turned all the way up. Your lips tingle like they're being kissed. Your pussy clenches on nothing."
    "Your nipples are so sensitive the lamp's warmth on them makes you squeal."
    "{color=#ff9ecb}And at the base of your spine, a bump. A warm, round, fluffy bump, pushing out right where the suit's costume tail is pinned. It pushes the costume tail clean off. It rolls across the felt.{/color}"
    "{color=#ff9ecb}Your tail. A real cottontail, soft and white and {i}yours{/i}, twitching every time you clench.{/color}"
    mr_vic "\"Look at me— {i}LOOK{/i} at me—!\"" with vnfx("flash")
    "Everyone looks."
    "In the mirror the house's bunny looks back: black waves, ears straight up, tits spilling out of the ruined suit, hips that go on for days, a little white tail flicking on top of a mountain of ass."
    show cg mr_private_simone_cum onlayer cgl
    "Simone grabs a fistful of your hair to hold you up and drives up through your tits one last time, and comes."
    "Hot and thick across your collarbones, your chin, your tits, white streaks painting your throat."
    "The server-bunnies giggle behind their hands. Royce lets his cards flop face up on the felt. Odette makes two neat notes in the book."
    "Your chest knows how to do that now. Just that. Just your chest."
    mr_vic "\"That— that wasn't— I didn't—\""
    "And then the arithmetic comes back, the way it always does, and the arithmetic says you're still in the game."
    jump mr_prop_bet

## The prop you offer Royce. The pot is his either way: the prop is only the gambler's compulsion,
## making a book on his own collection. The odds are flavour, never a figure.
label mr_prop_bet:
    $ vn_enter(bg="mr_privateroom", pc="grin", pc_tag="mr_pc", cast=[("mr_royce", "smirk")], cg="mr_prop")
    "Royce stands up. He's won the pot. The pot is you. He's coming round the table to collect it, and you can't stop your mouth."
    mr_vic "\"Prop! Want a prop, Mr. Royce? Call it between draws. Do I hold out, or do I scream for it?\""
    "Your voice comes out cheerful and cracked. A bunny gasps."
    mr_royce "\"Darling, I'm collecting either way. But what odds?\""
    "Nothing in the rules says you can't offer odds."
    menu:
        "Royce spreads his hands."
        "Even money":
            $ mr.odds = "even"
        "Long odds, his way":
            $ mr.odds = "long"
        "Let him name the price":
            $ mr.odds = "his"
    jump mr_royce

## ==== THE ENDING: "House Bunny" ===============================================================

## The reading, then the amortisation pitch, and the last line, "I'm due" (the third of three).
## Then the stay-or-go epilogue, the choice marked (owner, 2026-11-11).
label mr_settled:
    $ mr_advance(6)
    $ mr.done = True
    $ mr.fit = "suit"
    $ vn_enter(bg="mr_privateroom", pc="grin", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_settled")
    "Odette clears her throat. She stands, with the book at her side, and reads the newest line with clerical finality."
    $ _line = MR_BOOK[6]
    mr_odette "{color=#f3c969}\"[_line]\"{/color}"
    "She closes the book."
    mr_odette "\"You belong to the house, Vic.\""
    $ vn_feat("House Bunny")
    vn_th "(That's it. The number went red, and then, beautifully, all the way back to black. {i}Staff asset.{/i} Permanent.)"
    "You turn round slowly, hauling all your new curves upright, cum drying on your neck and chest, your tail flicking, and grin."
    mr_vic "\"Best settlement rate I've ever had.\""
    show mr_royce smirk at vn_cast_slot
    mr_royce "\"And a magnificent payout for the table. Bravo.\""
    "You know exactly how to stand for a room now. Hip out, tits up, ears forward. Every eye in it on you, right where you want them."
    "You press your tits together so hard they nearly swallow your chin."
    mr_vic "\"So you'll deal me in for a rematch, right?\""
    show mr_odette neutral at vn_cast_slot
    mr_odette "\"You want to run it back already?\""
    "One eyebrow, dry as vermouth."
    mr_vic "\"Sure! Start a fresh line. Dealer's privilege. See, if you amortise tonight's write-down over projected hours, plus the uniform allowance, plus the service fees—\""
    "You tap the side of your tit for emphasis, and it wobbles. Odette waits. Simone buttons her jacket, ignoring the mess. Royce looks delighted."
    mr_vic "\"—so all told, my expected value is strictly {i}positive{/i}.\""
    show cg mr_fresh_shoe onlayer cgl
    "Your grin is unstoppable."
    mr_vic "\"Get me a fresh shoe. I'm due.\"" with vnfx("flash")
    hide cg onlayer cgl
    menu:
        "Odette holds the book. The house hums under your heels."
        "Stay: a fresh line" (ending=True):
            jump mr_stay
        "Go: the walk" (ending=True):
            jump mr_walk

## The stay (the retired storyline's House Bunny contract): Odette opens a new column and leaves the
## heading blank. Then one more of Simone's breaks, the act your pick (the built route's after-the-
## ending break, which played in free play; Ren'Py has no free play).
label mr_stay:
    $ vn_enter(bg="mr_lounge", pc="grin", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_stay_column")
    "Odette opens the book to a clean page. She rules a new column down the edge of it, in blue, and writes nothing at the top."
    mr_vic "\"What's it quoted in?\""
    mr_odette "\"We'll see.\""
    show cg mr_stay_room onlayer cgl
    "You stop going home at the end of shifts. There's nowhere to go home to that beats upstairs."
    "The room the house keeps for marker players is your staff room now, with the suit on the chair and the carrot pin on the nightstand and the floor's hum coming up through the bed like a heartbeat."
    "Every night you go down to the locker. Every night Tam deals you in without a word."
    "Every night, at shift close, Odette reads you the fresh line, and you do the arithmetic out loud, and the arithmetic says {i}tomorrow{/i}."
    "And every night Simone catches your wrist on her way past."
    hide cg onlayer cgl
    $ vn_enter(bg="mr_corridor", pc="nervous", pc_tag="mr_pc", cast=[("mr_simone", "hungry")])
    mr_simone "\"Break. Mine. You're the snack.\""
    menu:
        "She's already steering you into the service corridor."
        "Simone's break: over the crates":
            $ mr.break_act = "anal"
        "Simone's break: on her cock":
            $ mr.break_act = "vaginal"
    $ mr.break_night = None
    $ mr.after_ending = True
    jump mr_break

## The go (the retired storyline's Cashed Out): "You can always walk. The marker walks with you."
## You walk out the front at dawn in your own suit, which closes over nothing.
label mr_walk:
    $ mr.fit = "own"
    $ vn_set_time(6, 0)
    $ vn_enter(bg="mr_cage", pc="neutral", pc_tag="mr_pc", cast=[("mr_odette", "neutral")], cg="mr_walk_cage")
    "Odette counts your tips out of the cage drawer. She doesn't say how much. She doesn't need to."
    mr_odette "\"You can always walk. The marker walks with you.\""
    "You put your own suit on in the locker. Your work shirt, your trousers, your good shoes."
    "The shirt doesn't even pretend to close."
    "It just hangs open either side of your tits, and the trousers sit under your ass like a joke, and your ears stick straight up through your hair, and your tail pokes out over the waistband."
    "The carrot pin stays where the costumer clipped it. House colours. You're not taking those off."
    $ vn_enter(bg="mr_street", pc="grin", pc_tag="mr_pc", cg="mr_walk_dawn")
    "You walk out through the front doors of the Golden Hare at dawn."
    "The sky over Connudatus Street is pale and clean. Delivery vans. Pigeons. A street sweeper who takes one look at you and walks into a lamppost."
    "You stand on the step with the sun on your face and the house's whole floor humming behind you, and you breathe."
    mr_vic "\"Clean slate.\""
    "In a girl's voice. To nobody."
    "The door's still there behind you. It'll be there tonight, and tomorrow night. Simone's still at the back. Tam's still dealing."
    "You put your hands in your pockets and walk. You get almost all the way to the corner before you start running the numbers."
    jump mr_route_return
