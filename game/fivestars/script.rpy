## THE SOURCE: fivestars' passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage
## of the original (main.twee, days-early.twee, days-late.twee), written as beats; the director
## scenes are in scenes.rpy. The original is in catalog/docs/routes/vn-original/fivestars/.
## No digits anywhere: stars in glyphs and words, sizes as words, the manifest never counted.

## ---- DAY 1, CONTACTLESS (Vellum Opening, One Intake, One Route) -------------------------------

label fs_opening:
    $ fs.fit = "own"
    $ vn_enter(bg="fs_vanbay", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_opening_van")
    show cg fs_opening_van onlayer cgl
    "The van bay, just before six. The roller door's up, the docks are grey and cold beyond it, and your van sits in its bay with the side door open and VELLUM down the flank in navy."
    "You're sitting in the open door with your legs swinging and your phone in both hands, reading the terms. Again. All of them."
    "Six tiers, and every one says what it needs in plain words: Contactless. Hand to Customer. Verified Fit. In-Home. Returns. Ambassador."
    "Every requirement, every sign-off, every clause, laid out like a recipe. You're pretty sure nobody else at this depot has ever scrolled this far."
    "You've made a spreadsheet. It's a {i}good{/i} spreadsheet: colour-coded, a tab for each tier, a column for what it needs and a column for how fast you can get it."
    "The column for how fast is all green. You've been up since before dawn making it greener."
    "Down the bay the other drivers drift in with their hoods up, yawning, thumbing their phones to the delivery screen and nothing else."
    fs_driver "\"Nobody reads that, mate.\""
    fs_you "\"{i}I{/i} read it! Twice! Tier six is called {i}Ambassador{/i}!\""
    "He's already gone."
    vn_sfx "Click."
    "The clock flicks over. Your earpiece clicks."
    fs_deb "\"Dispatch, go ahead.\""
    "A woman's voice. Crisp. Bored. Nothing but business."
    fs_you "\"Prentice, checking in! Morning! Van's ready, I'm ready, I've read the—\""
    fs_deb "\"Good for you. Intake's on the dock. The warehouse lead runs it. Don't keep her waiting.\""
    fs_you "\"What's your name?\""
    fs_deb "\"Deb. Dispatch. I'm in your ear from now until you clock off. I count your windows, I read your ratings, I tell you where to go. You don't ring me for directions and you don't ring me for chat.\""
    fs_you "\"Got it! Deb, quick question about tier two—\""
    fs_deb "\"That was chat. Go.\"\n{size=-5}{color=#ff8fa3}▸ Into the warehouse for intake{/color}{/size}"
    $ vn_pass(15)
    jump fs_intake

label fs_intake:
    $ vn_enter(bg="fs_deck", pc="eager", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg=None)
    show bg fs_deck onlayer bgl
    show fs_regan flat at vn_cast_slot
    "The warehouse is one long steel shed: racks of flat grey boxes to the roof, a pick face lit like an operating theatre, and a dock with a black rubber mat, a chrome rail and a scanner arch."
    "A woman in hi-vis is waiting on the mat. Buzzed hair, a clipboard, a badge that says REGAN and nothing else. Tall, and built like she lifts the pallets herself."
    fs_regan "\"Intake.\""
    "Not to you. To the clipboard."
    fs_regan "\"Shoes. Then strip.\""
    fs_you "\"All of it?\""
    fs_regan "\"All of it.\""
    $ fs.fit = "nude"
    hide fs_regan
    show cg fs_intake_scan onlayer cgl
    "You strip: shoes, shirt, shorts, briefs, into a grey bin. You stand on the mat with your hands at your sides and your small cock twitching in the cold, grinning, because this is {i}step one{/i} and step one is always the best bit."
    "She sweeps a wand down you, blue light top to toe, and the scanner arch talks in a calm woman's voice."
    fs_scanner "“Arms: within spec.” “Legs: within spec.” “Torso: flagged. Body hair. Unable to read.”"
    $ _fs_s = fs_scan("Chest", False)
    fs_scanner "[_fs_s]"
    vn_sfx "Ding."
    "The arch gives a happy little ding. Nobody says anything about it."
    fs_regan "\"Removal.\""
    "She points at a door marked FIT ROOM."
    show cg fs_gel onlayer cgl
    "Inside it's white tiles, a misting station and a cartridge of pale gel. She works fast, with flat palms and no conversation: arms, chest, belly, legs, round your balls and your cock like she's done every driver who ever walked in and they were all boring."
    "Then the mist comes down and rinses it off."
    show cg fs_smooth onlayer cgl
    "And you look down."
    $ fs_body(1)
    "{color=#ff5fb8}Nothing. Not one hair anywhere. Your forearms, your shins, your belly, the whole lot round your cock, bare and pale and gleaming under the strip lights.{/color}"
    "{color=#ff5fb8}You run a hand down your chest and your palm just {i}glides{/i}.{/color}"
    fs_you "\"Oh, that's— I'm {i}SLICK{/i}—\""
    "You rub your thigh. Your other thigh. Your belly, both hands, round and round."
    fs_you "\"Oh, feel that— no, don't, you're working— {i}ohh{/i}, it's so {i}smooth{/i}—\""
    "{color=#ff5fb8}Your lips buzz from the mist, fat and tingly, like you've been sucking a mint for an hour. You lick them and moan out loud in a tiled room.{/color}"
    "{color=#ff5fb8}And your jaw keeps working on its own, open, shut, open, practising an angle it hasn't been shown yet. Your fingers flex. They feel quick. Clever. Like they already know a grip.{/color}"
    show fs_regan flat at vn_cast_slot
    fs_regan "\"It doesn't grow back.\""
    "That's all she says about it. It never does."
    fs_you "\"Doesn't— oh, good— {i}good{/i}— look at it! It's so {i}clean{/i}! Regan, it looks {i}new{/i}!\""
    "You've got both hands on your bare belly and your small cock's stood straight up between them, pink and smooth and twitching, and you're laughing at it."
    fs_deb "\"Is intake always this loud?\""
    fs_regan "\"No.\""
    $ fs_advance(1)
    show cg fs_kit_medium onlayer cgl
    "She drops a bundle on the rail without looking up: a navy polo, black cycle shorts, a black jockstrap."
    fs_regan "\"Medium.\""
    "Vellum's whole line is cut for your cock. It says so on the label. The pouch at the front fits you exactly, snug, like it was waiting."
    $ fs.fit = "kit"
    hide fs_regan
    menu:
        "The manifest's on your phone. You get to choose the order."
        "Plan the manifest round the road closures":
            $ fs.routing = "closures"
        "Plan the manifest round the best tippers":
            $ fs.routing = "tippers"
    $ vn_pass(60)
    jump fs_route_one

label fs_route_one:
    $ vn_enter(bg="fs_cab", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_route_step")
    show bg fs_cab onlayer bgl
    "The van's white and new and smells of cardboard. The manifest glows on your phone, every address in blue, in the order you picked."
    if fs.routing == "tippers":
        "You've put the big tippers first and the hills last. It's a {i}beautiful{/i} manifest. You could frame it."
    else:
        "You've threaded it round every road closure in town. It's a {i}beautiful{/i} manifest. You could frame it."
    show cg fs_route_step onlayer cgl
    "First door. You set the parcel on the step, square to the mat, logo out. Knock. Step back. The door opens a crack on a man in a bathrobe."
    fs_you "\"Vellum, contactless preferred.\""
    "You smile like a brochure. He waves. Door shut. Your phone buzzes: a star. Then another."
    fs_deb "\"Window met. Ahead of schedule. Next drop.\""
    "A woman in a towel takes one look at the van and shuts the door before you've stepped back. Star. Nobody home at the next. Star. A man on a ladder shouts \"ON THE STEP\" without turning round. Star."
    fs_deb "\"Early on every one. Stop it, you're making the others look bad.\""
    fs_you "\"Sorry!\""
    fs_deb "\"You're not.\""
    fs_you "\"I'm not!\""
    show cg fs_route_shorts onlayer cgl
    "It goes like that all morning. Step, knock, step back, smile. Nobody touches you. Nobody even sees the shorts."
    "Your cock sits snug in the pouch, and every time you jump down out of the van it rubs, and you grin at the dashboard and pretend it didn't."
    "It doesn't stop rubbing. Down from the cab, {i}rub{/i}. Up the path, {i}rub{/i}. Bend to square a parcel on a mat, and the jockstrap's straps pull tight under your bare smooth cheeks, and the Lycra slides over your shaved skin like a hand."
    "You have to stand very still on a stranger's step with your eyes shut."
    fs_you "\"{i}Hhn{/i}— okay— delivered—\""
    fs_deb "\"Prentice. Why are you breathing like that on a doorstep?\""
    fs_you "\"The shorts are {i}very{/i} well made!\""
    fs_deb "\"They're cycle shorts.\""
    fs_you "\"They're {i}very{/i} well made cycle shorts!\""
    "By the next stop there's a damp spot on the front of the pouch, and your lips are still buzzing from the fit room mist, and you keep licking them at red lights."
    "A star lands every time you get back in the van. You read every one out loud to the empty cab."
    fs_you "\"Four stars. Four stars. {i}Four{/i} stars. Ooh, a five—\""
    fs_deb "\"I can hear you.\""
    fs_you "\"I know!\""
    show cg fs_sandwich onlayer cgl
    $ vn_until(11)
    "Mid-morning you're parked up eating a sandwich over the steering wheel, and you can't stand it any more."
    fs_you "\"Deb. What's the next tier need?\""
    fs_deb "\"Hand to customer. Ratings at the line, a run of drops, and a hand-to-customer sign-off from a regular, which nobody's ever—\""
    fs_you "\"Put me down for it.\""
    "A pause on the channel."
    fs_deb "\"Logged. Next drop.\"\n{size=-5}{color=#ff8fa3}▸ Back to the van bay at dusk{/color}{/size}"
    $ vn_until(19)
    jump fs_deck

## ---- rung 1: the loading deck (Vellum One Deck, One Deck Two). Non-con, no flip. -----------------

label fs_deck:
    $ vn_enter(bg="fs_deck", pc="neutral", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_deck_regan")
    show cg fs_deck_regan onlayer cgl
    "Dusk. The roller door's all the way up, and the van bay's full of orange light off the water. You back the van in on the last of the manifest, every drop delivered, every window met."
    "Regan's on the deck stacking empties. She doesn't look up."
    fs_regan "\"Returns in the bin. Then here.\""
    "You put the returns in the bin. Then you're here."
    "She's sitting on a stack of pallets with her hi-vis open and her work trousers open, and she's hard."
    "She's a futa, and she's enormous. That's a fact, like the time or the weather. Her cock lies up her belly past her navel, thick and dark and heavy, and her balls sit fat on the pallet under it."
    fs_you "\"Oh— sorry— I'll come back when you're—\""
    fs_regan "\"Knees.\""
    fs_you "\"I'm sorry?\""
    show fs_pc protesting
    show cg fs_deck_knees onlayer cgl
    "She reaches out without getting up, takes a fistful of your polo collar, and pulls. Down." with vnfx("shake")
    "Your knees hit the rubber mat with a thump, and your face is level with the root of her."
    fs_you "\"Regan— Regan, I'm {i}Contactless{/i}— my tier's Contactless, it's in the terms, nobody touches the driver—\""
    fs_regan "\"Complaint noted. Open.\""
    fs_you "\"It's literally the {i}name{/i} of the— {i}mmf{/i}—!\""
    show cg fs_deck_mouth onlayer cgl
    "She feeds it in while your mouth's still open on the clause. Your lips stretch round the head and keep stretching, and your fat buzzing lips {i}sing{/i}, and the noise that comes out of you echoes off the roller door."
    fs_you "\"Mmmhh— {i}mmf{/i}— mmh-{i}MMH{/i}—!\""
    fs_deb "\"Complaint about what?\""
    fs_you "\"{i}Mmf— cnnt-ctlss{/i}—!\""
    fs_deb "\"Noted.\""
    vn_sfx "Click. Click."
    fs_deb "\"Logged.\""
    fs_regan "\"Spit. More.\""
    "You don't. She waits, holding your collar, until the spit comes anyway, running out round her."
    vn_sfx "Shlrp."
    vn_th "(Your jaw's doing it. The angle from the fit room. You didn't ask it to.)"
    "It opens wider without asking you, and her cock slides in deeper than anything ever has."
    "Her big hand goes down between your legs and wraps round your small cock through the shorts. Then inside the shorts. Fist round it, pumping, flat and steady, like she's counting stock."
    "Her whole fist swallows you. There's nothing left showing above it. She doesn't comment. She just keeps pumping, and the pouch of the medium stretches round her wrist, and you're hard in it, rock hard, and you shout round her cock about it."
    fs_you "\"{i}Hhnn{/i}— {i}glk{/i}— nmt— {i}mmf{/i}— not— hand to— {i}glk{/i}—\""
    "You get both palms on her thighs to push off."
    fs_regan "\"Hands.\""
    "She moves them to the base of her cock, one and then the other, and holds them there."
    fs_regan "\"Use them.\""
    "And your fingers {i}do{/i}. They twist, quick and slick, the way they were twitching to in the fit room, while you're still trying to pull them away."
    "For the first time all day Regan makes a sound: one short breath through her nose."
    fs_regan "\"Lips over teeth. Tongue flat. Down.\""
    "Her hand on the back of your head takes you down. Your nose doesn't get anywhere near her belly. There's just more of her."
    "Your throat opens on its own and lets the head in and you gag, wet and loud. She lets you up a breath and takes you straight back down, and you're drooling all over her balls."
    fs_you "\"{i}Glk{/i}— {i}hhk{/i}— {i}mmhh{/i}—!\""
    fs_regan "\"Again. Deeper. Hold it.\""
    "Her fist keeps pumping your cock the whole time, thumb rolling over the wet tip on every upstroke like she's checking a seal. Your hips jerk into it. You can't make them stop."
    fs_deb "\"I can hear that, you know.\""
    fs_you "\"Mmh— {i}Deb{/i}— mmf—!\""
    fs_deb "\"That's not a word. Your complaint's on file. Keep going.\""
    show cg fs_deck_dash onlayer cgl
    "Your phone's propped on a parcel by your knee, still on the dashboard. It's lit up. You read it with your nose in Regan's belly."
    show screen fs_dash(1)
    "The rating's ticking up."
    hide screen fs_dash
    "You pull off with a long wet {i}shlp{/i}, a string of spit from your lip to her cock, and grab the phone."
    fs_regan "\"Hold that.\""
    "She pushes your head back down."
    show cg fs_deck_email onlayer cgl
    "So you type with her in your mouth. One thumb. Polite, because you're always polite."
    $ fs_mail_lines = ["{b}To: Vellum{/b}", "Dear Vellum, I'd like to raise a concern regarding the Contactless tier. On my first shift I was asked to perform a hand-off of a kind I don't believe the tier covers. Please could you clarify the scope of \"contactless\"?", "P.S. Quick question: what is the route bonus? It says it's applied overnight but not what it is."]
    show screen fs_mail(fs_mail_lines)
    "Your thumb hovers over the sign-off."
    menu:
        "How do you sign it?"
        "Sign it \"Kind regards\"":
            $ fs.sign1 = "Kind regards"
        "Sign it \"Many thanks in advance!\"":
            $ fs.sign1 = "Many thanks in advance!"
    jump fs_deck_two

label fs_deck_two:
    $ fs_mail_lines = fs_mail_lines + ["{i}%s, T. Prentice.{/i}" % fs.sign1]
    show screen fs_mail(fs_mail_lines)
    vn_sfx "Whoosh."
    "Send."
    hide screen fs_mail
    "Nobody replies."
    show cg fs_deck_mouth onlayer cgl
    "Regan takes the phone out of your hand and puts it back on the parcel, and puts your hand back on her. Fist round the root, her hand on the back of your head for the rest, bobbing you fast and sloppy, spit running down your chin onto the deck."
    fs_you "\"{i}Glk{/i}— {i}glk{/i}— {i}mmhh{/i}—\""
    fs_regan "\"Throat.\""
    "She takes you down into it. Your eyes roll. Her fist speeds up on your cock and your hips buck into it and you moan right down the length of her."
    vn_th "(That's not a protest any more. You know it isn't. You can't stop it.)"
    fs_regan "\"Off.\""
    "She pulls you off by the collar."
    fs_you "\"Regan— that's {i}not{/i}— the clause says— {i}ahh{/i}—\""
    show cg fs_deck_face onlayer cgl
    "She takes herself in one fist and points it at you like a hose."
    vn_sfx "Splt. Splt."
    "Across your cheek. Your nose, your open mouth, your tongue, mid-word. Down your chin, onto your polo, onto the deck in a long white streak. There's so {i}much{/i}." with vnfx("flash")
    "And her other fist never stops, and you come right in the middle of the objection, untouched by anything but that flat steady pumping, your small cock spitting a thin dribble onto the rubber mat."
    $ fs_enc.pc_orgasms = 1
    fs_you "\"—says {i}contactless{/i}— {i}ahh{/i}— {i}AHH{/i}— oh, I'm— {i}ahhh{/i}—!\""
    fs_regan "\"Deck.\""
    show cg fs_deck_wipe onlayer cgl
    "The nearest cloth is a Vellum sample, a lace thong still in its bag. She hands it to you. You tear it open and wipe the deck with it on your knees, cum dripping off your chin."
    fs_deb "\"Five stars, no notes.\""
    fs_you "\"Deb, I made a {i}complaint{/i}—\""
    fs_deb "\"It's logged. So's the rating.\""
    show cg fs_deck_again onlayer cgl
    "Regan's still hard. She hasn't even softened. She takes a fistful of your hair, not hard, just a handle, and lays the fat wet head of her cock on your lip."
    fs_regan "\"Again.\""
    "In your ear, Deb stops reading you numbers and starts telling you exactly what she can hear."
    menu:
        "Regan's hand in your hair. Her cock on your lip."
        "Grab the pallet edge":
            $ fs.deck = "pallet"
            jump fs_deck_sex
        "\"I'm OFF the clock, Regan—\"":
            $ fs.deck = "clock"
            jump fs_deck_sex
        "Shove at her thighs":
            $ fs.deck = "shove"
            jump fs_deck_sex
        "Regan zips up":
            jump fs_deck_close

label fs_deck_close:
    $ vn_enter(bg="fs_drivers_room", pc="flushed", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_drivers_room onlayer bgl
    "She looks at the time, and lets go of your hair."
    "Later you're up the steel stairs to the drivers' room over the bay, your lips still buzzing, still tasting her.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(5)
    jump fs_morning_two

label fs_deck_after:
    $ vn_enter(bg="fs_deck", pc="flushed", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_deck_sex_cum")
    if fs_enc.partner_came:
        "She goes again without a sound, straight down your throat, her hand flat on the back of your head, and you swallow and swallow because there's nowhere else for it to go."
    else:
        "She pulls out and finishes herself across your face again, steady as a stapler, while you're still mid-sentence."
    if fs_enc.pc_orgasms:
        "You came again in her fist, shouting the tier name at the roller door."
    else:
        "You're shaking on your knees, hard and dripping in the pouch, still saying \"contactless\" like it's going to start working."
    hide cg onlayer cgl
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Done.\""
    "She zips up, and goes back to stacking empties."
    fs_deb "\"Second complaint, same shift. Logged.\"\n{size=-5}{color=#ff8fa3}▸ Up to the drivers' room{/color}{/size}"
    hide fs_regan
    call vn_night(5)
    jump fs_morning_two

## ---- DAY 2, HAND TO CUSTOMER (Vellum Two Morning, Two Route) ------------------------------------

label fs_morning_two:
    $ fs_advance(2)
    $ vn_enter(bg="fs_drivers_room", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_wake_2")
    show cg fs_wake_2 onlayer cgl
    "You wake in the drivers' room over the van bay, with the roller door rumbling up under the floor and the kettle already on."
    "Your phone's lit up on the pillow. A new badge. Gold."
    "{color=#e8b923}TIER · Hand to Customer{/color}"
    fs_you "\"Ha! {i}HA!{/i}\""
    "You sit bolt upright. The second the earpiece is in:"
    fs_deb "\"Dispatch, go ahead.\""
    fs_you "\"Did you see it? Deb, did you see the—\""
    fs_deb "\"Nobody at this depot's ever done it. Including you, until last night. Van.\""
    show cg fs_mirror_2 onlayer cgl
    "You're in the van bay before the roller door's halfway up. You lean into the wing mirror to check your teeth."
    "And stop."
    $ fs_body(2)
    "{color=#ff5fb8}Your skin's {i}glowing{/i}: smooth and clear and soft-looking, like you've slept for a week. Your face has gone softer somehow, your jaw a bit rounder, your mouth a bit fuller.{/color}"
    "{color=#ff5fb8}You hold your hands up. They're slimmer. Finer. Long-fingered.{/color}"
    fs_you "\"Oh, that's— {i}look{/i} at that— ohh, it's so {i}soft{/i}—\""
    "You stroke your own cheek and moan, right there in the bay."
    "{color=#ff5fb8}You pull the cycle shorts up. They close. Just. Snug at the seat, the black Lycra pulled tight and round over your ass, and when you bend to check the tyres you can feel every thread of it hug you.{/color}"
    fs_you "\"{i}Mmh{/i}— oh, the {i}seat{/i}— that's snug— that's {i}really{/i} snug—\""
    "Your ass clenches on nothing while you stand there, and keeps doing it, like it's rehearsing for something. Your lips part on their own. Your fingers keep finding the waistband and toying with it, quick and clever."
    "Every time the Lycra shifts over your cheeks you feel it right down to your toes, so sensitive back there you have to grab the wing mirror."
    fs_you "\"{i}Hhh{/i}— okay— okay, that's new, that's {i}very{/i} new—\""
    fs_deb "\"Are you moaning at a van?\""
    fs_you "\"Checking the tyres!\"\n{size=-5}{color=#ff8fa3}▸ Load up{/color}{/size}"
    $ vn_pass(60)
    jump fs_route_two

label fs_route_two:
    $ vn_enter(bg="fs_doorstep_day", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_route2_turn")
    show bg fs_doorstep_day onlayer bgl
    "Hand to customer means hand to customer. You walk the parcels up to the doors now, and wait, and they open, and people {i}look{/i} at you."
    "One old account still has the box ticked. You set it on the step, knock, step back."
    fs_you "\"Vellum, contactless preferred.\""
    "The door doesn't even open. The star comes anyway. That's the last time you'll say it."
    "Everyone else wants it in their hands. And when they take it they look at the polo, and the shorts, and the shorts again, and the stars land before you're back in the van."
    show cg fs_route2_turn onlayer cgl
    "A woman in a dressing gown takes her box and doesn't shut the door."
    fs_cust "\"Is that the shorts from the site? The black ones?\""
    fs_you "\"Vellum's own. Snug at the seat. Soft-touch.\""
    fs_cust "\"Turn round.\""
    fs_you "\"That's— I think that's more of a modelling thing—\""
    "She twirls her finger. You turn, because she's holding the parcel and the rating at the same time."
    "The Lycra hugs your ass so tight you can feel her eyes on every thread, and your small cock jumps in the pouch, and your new soft cheeks go hot."
    vn_sfx "Bzzt."
    "Five stars before you're down her path."
    show cg fs_route2_catalogue onlayer cgl
    "A man at the next door signs on your phone and keeps hold of it a bit too long, looking at your new soft hands. A couple at the one after that both come to the door, take the box together, and ask if you're in the catalogue."
    fs_you "\"I'm the {i}driver{/i}. The catalogue's online.\""
    fs_deb "\"Customers are asking if you're in the catalogue. Logged.\""
    fs_you "\"Why are you logging {i}that{/i}? Deb. What's the next tier need?\""
    fs_deb "\"Fit check. On the scanner, at the depot, in front of whoever's on—\""
    fs_you "\"Put me down for it.\""
    fs_deb "\"You can't be put down for a fit check, it's a—\" A stop. \"Fine. Logged.\""
    "You've routed it so the last address is Jodie Calloway's. Jodie orders something every week, and she always picks hand-to-customer. You've read her notes on the account."
    "{i}Driver to model the item, please. Thanks!!{/i}\n{size=-5}{color=#ff8fa3}▸ Jodie's, last on the manifest{/color}{/size}"
    $ vn_until(18)
    jump fs_jodie

## ---- rung 2: Jodie's front room (Vellum Two Jodie). Non-con, no flip; first anal. -------------

label fs_jodie:
    $ vn_enter(bg="fs_jodie_room", pc="neutral", pc_tag="fs_pc", cast=[("fs_jodie", "grin")], cg="fs_jodie_door")
    show cg fs_jodie_door onlayer cgl
    "Jodie opens the door before you knock. Red hair up in a clip, a big soft jumper, bare legs, and a grin like she's been waiting at the window."
    fs_jodie "\"{i}Finally.{/i} Come in, come in. Box on the sofa. Lose the shorts.\""
    fs_you "\"Sorry?\""
    fs_jodie "\"It's mesh sets. You can't model mesh over cycle shorts. Shorts, polo, all of it. Four stars for punctuality, by the way.\""
    show fs_pc protesting
    fs_you "\"Hand to customer means I hand you the {i}parcel{/i}. That's the clause. The parcel goes into your hands. That's the whole—\""
    fs_jodie "\"And the note says driver to model the item.\""
    "She takes the parcel, drops it on the sofa, and gets both hands in the waistband of your shorts."
    fs_jodie "\"I tipped, Toby. Tip's in the terms.\""
    fs_you "\"That's not how tips— {i}hey{/i}—!\""
    $ fs.fit = "nude"
    show cg fs_jodie_mesh onlayer cgl
    "Shorts round your ankles. Polo over your head while your arms are still tangled in it. You end up on her rug in your bare smooth skin with your small cock bobbing, one hand over it, quoting the tier description at her while she holds the first set up against you."
    fs_jodie "\"Oh, {i}yes{/i}. Arms up.\""
    "She doesn't wait for your arms; she lifts them. She dresses you herself: black mesh first, a little top that stops under your nipples and shorts with no back to them at all. She turns you round by the hips."
    fs_jodie "\"Walk to the window. Now back. Now bend and pick up the box.\""
    "You don't. She bends you by the back of the neck, and holds you there, and makes a noise like a kettle."
    fs_jodie "\"Four stars. The seat's doing a lot of work for you.\""
    fs_you "\"Jodie, I'm going to have to log this with dispatch—\""
    fs_deb "\"It's logged.\""
    "Pink mesh. She snaps the waistband on your hip and you yelp."
    fs_jodie "\"Three. Too sweet. You look like a sample.\""
    "White mesh. You can see everything through it. {i}She{/i} can see everything through it."
    "And your small cock is stiff and pink and pushing the mesh out in front, wet already at the tip, and you didn't tell it to be. She walks all the way round you twice."
    fs_jodie "\"Hmm. Nearly. Lips.\""
    fs_you "\"Lips? No— that's not modelling, that's—\""
    show cg fs_jodie_gloss onlayer cgl
    "She uncaps a gloss and does your mouth with her thumb on your chin, holding your jaw still. Pink, glossy, sticky."
    fs_jodie "\"There. Five stars for lips.\""
    $ fs.gloss = True
    show cg fs_jodie_walk onlayer cgl
    "Her hand goes straight down the front of the white mesh and wraps round your cock."
    fs_jodie "\"And what's this. Hmm. Three stars for size. Five for {i}enthusiasm{/i}. Look at it {i}drip{/i}.\""
    fs_you "\"{i}Ahh{/i}— customer— the customer's handling the {i}stock{/i}— that's not in the— get your {i}hand{/i}—\""
    fs_jodie "\"Customer's allowed. It's in the terms.\""
    fs_you "\"It is {i}not{/i} in the—\""
    "She doesn't let go. She walks you round her front room by it, slow, to the window and back, like she's walking a sample down a catwalk, and turns you at each end."
    fs_jodie "\"Four stars for the walk. The seat's carrying it. Again.\""
    fs_you "\"{i}Hhh{/i}— hand to customer— {i}ahh{/i}— hand to customer means the {i}PARCEL{/i}—\""
    fs_jodie "\"This is {i}very{/i} hand to customer.\""
    fs_deb "\"Your delivery window closed a while ago.\""
    fs_you "\"Deb, she's— {i}hhn{/i}— Deb, can you {i}action{/i} this—\""
    fs_deb "\"Dispatch can't action that.\""
    show cg fs_jodie_strap onlayer cgl
    "Then Jodie's on her knees by the sofa digging in a drawer, and she comes up with a harness and a fat, glossy pink strap-on, grinning so hard her eyes have gone."
    fs_you "\"No. {i}No{/i}. Jodie, that's— I've never— that is {i}not{/i} modelling the item—\""
    fs_jodie "\"Rug.\""
    "She hooks your ankle with her foot while she's still buckling, and you go down on your back on her rug." with vnfx("shake")
    show cg fs_jodie_rug onlayer cgl
    "She's on you before you can roll. Her hands go under the backs of your knees and push them up and back, and her weight comes down on them, and they stay."
    fs_you "\"Jodie— Jodie, {i}wait{/i}, I've never had {i}anything{/i}—\""
    fs_jodie "\"Ooh. Five stars for that.\""
    "She lubes it with a lot of lube. She lubes {i}you{/i} with two slick fingers, slow, and you squeal at the first one, and the second makes your back arch off the rug on its own."
    fs_jodie "\"Four stars for prep.\""
    "She pushes in."
    "It's {i}big{/i}. It keeps coming, stretching you open and full, fuller, the whole slick pink length of it sliding in until her hips are against your ass." with vnfx("shake")
    fs_you "\"{i}AHHH{/i}— oh— it's {i}in{/i}— get it {i}out{/i}— it's all the way— {i}ohh{/i}—!\""
    fs_jodie "\"Five stars for the noise.\""
    "She starts to fuck you, delighted."
    vn_sfx "Slap. Slap. Slap."
    "Her thighs on your ass. Her fist round your cock, pumping in time. Your head thrown back on the rug, your glossy mouth wide open, every stroke dragging over something inside you that makes your toes curl."
    fs_you "\"Ahh— {i}ahh{/i}— hand— to— {i}customer{/i}— means— {i}ahh{/i}—\""
    fs_jodie "\"Four stars for the angle. Five for your face. Five. Five.\""
    show cg fs_jodie_onestar onlayer cgl
    "The open channel crackles in your ear, and Deb's voice changes. The broadcast voice."
    fs_deb "\"All drivers. Rating in for T. Prentice. One star. Clive Ormsby writes: {i}The fabric pills. I washed it once. It pills. One star.{/i}\""
    "The whole driver channel bursts out laughing. Your first one-star, on the open channel, with Jodie balls-deep in you."
    fs_you "\"Nooo— that's the {i}fabric{/i}— that's not {i}me{/i}—!\""
    fs_jodie "\"Shush.\""
    "She fucks you harder, and your phone slides off the sofa arm onto the rug by your head, face up, still on the dashboard."
    show screen fs_dash(2)
    "The rating's climbing with every stroke."
    hide screen fs_dash
    show cg fs_jodie_cum onlayer cgl
    "And it's the stroke after that. Her fist, her hips, the angle. Something gives way in you all at once, and you come so hard your back comes off the rug, your small cock spurting in her fist and splattering your own belly." with vnfx("flash")
    $ fs_enc.pc_orgasms = 1
    fs_you "\"{i}Ahhhh{/i}— make it a five— make it a {i}five{/i}— just {i}rate{/i} it, make it a five, I'll sign for {i}anything{/i}—!\""
    "Jodie, still in you, still moving, picks up her phone with her free hand. Taps. Your phone buzzes on the rug."
    "{color=#e8b923}★★★★★{/color}"
    fs_deb "\"Five stars, no notes.\""
    "Jodie doesn't pull out. She grins down at you, gets a fresh grip under your knees, and rolls her hips."
    menu:
        "She's still in you."
        "Grab the rug":
            $ fs.rug = "rug"
            jump fs_jodie_sex
        "\"Jodie, the clause says PARCEL—\"":
            $ fs.rug = "clause"
            jump fs_jodie_sex
        "Kick at the sofa":
            $ fs.rug = "kick"
            jump fs_jodie_sex
        "Jodie lets you up":
            jump fs_jodie_close

label fs_jodie_close:
    $ vn_enter(bg="fs_jodie_room", pc="flushed", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_jodie_room onlayer bgl
    "She checks the time on her phone, and pulls out with a pop, and lets you find your shorts.\n{size=-5}{color=#ff8fa3}▸ Home to the drivers' room{/color}{/size}"
    $ fs.fit = "kit"
    call vn_night(5)
    jump fs_morning_three

label fs_jodie_after:
    $ vn_enter(bg="fs_jodie_room", pc="flushed", pc_tag="fs_pc", cast=[("fs_jodie", "rating")], cg="fs_jodie_sex_cum")
    if fs_enc.pc_orgasms:
        "You came again, all over your own belly, screaming the clause and then screaming her a five."
    else:
        "She finishes you with her fist anyway, holding your knees down with the other hand, and you spray your own belly mid-protest, and she rates it out loud."
    hide cg onlayer cgl
    show fs_jodie rating at vn_cast_slot
    fs_jodie "\"I'm ordering again next week. I'm ordering {i}everything{/i}.\""
    fs_deb "\"Customer's ordering again. Logged.\"\n{size=-5}{color=#ff8fa3}▸ Home to the drivers' room{/color}{/size}"
    hide fs_jodie
    $ fs.fit = "kit"
    call vn_night(5)
    jump fs_morning_three

## ---- DAY 3, VERIFIED FIT (Vellum Three Morning, Three Depot, Three Platform) -------------------

label fs_morning_three:
    $ fs_advance(3)
    $ vn_enter(bg="fs_drivers_room", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_wake_3")
    show bg fs_drivers_room onlayer bgl
    "You wake in the drivers' room over the van bay with the roller door rumbling up under the floor."
    fs_deb "\"Dispatch, go ahead.\""
    "Before you've got your socks on."
    fs_you "\"Fit check today.\""
    fs_deb "\"I'm aware. You booked it every way the app allows.\""
    show cg fs_wake_3 onlayer cgl
    "You pull the cycle shorts up. They stop."
    $ fs_body(3)
    "{color=#ff5fb8}They stop halfway up your thighs, because your thighs are {i}in the way{/i}.{/color}"
    "{color=#ff5fb8}You look down. Your thighs are thick: round and full and pressed together all the way down, soft on the inside, the black Lycra rolled tight round the middle of them like a tourniquet.{/color}"
    "{color=#ff5fb8}You haul. You hop. You get them over your ass with a snap, and your ass just keeps {i}going{/i}, big and round and high, the shorts stretched so thin over it they've gone grey.{/color}"
    "The waistband won't close. There's a gap at the back you could post a letter through."
    fs_you "\"{i}Oh{/i}— oh, look at— {i}look{/i} at it—! It's {i}HUGE{/i}— it won't close— Deb, my shorts won't {i}close{/i}—!\""
    "You twist to see it in the mirror and your own ass fills the mirror. You grab it with both hands and it fills your hands and then some, and you squeal."
    fs_deb "\"Is that a fit check problem or a you problem?\""
    "You give it a slap just to see. It wobbles. The {i}feeling{/i} goes right through you, so strong back there your knees buckle and you have to hold the door frame."
    fs_you "\"{i}Ahh{/i}— oh, it's so {i}sensitive{/i}— oh, everything back there's— {i}hhh{/i}—\""
    show cg fs_seat_3 onlayer cgl
    "Your hips sway when you walk to the van. Your ass knows how to move now, roll and push back and squeeze, like it's had a week of lessons overnight. Your lips are fatter than yesterday, and they {i}tingle{/i}."
    "In the van you run the driver's seat all the way back to fit your ass and thighs in. It's still wrong."
    "You drive to the depot perched on the very edge of it with your thighs spread, moaning every time you go over a bump.\n{size=-5}{color=#ff8fa3}▸ Into the depot{/color}{/size}"
    $ vn_pass(20)
    jump fs_depot_three

label fs_depot_three:
    $ vn_enter(bg="fs_pickface", pc="eager", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg=None)
    show bg fs_pickface onlayer bgl
    show fs_regan flat at vn_cast_slot
    "Regan's at the pick face with her clipboard. You walk up with the shorts split open at the back and your ass hanging half out of them. She doesn't look up."
    fs_regan "\"Large.\""
    show cg fs_depot_large onlayer cgl
    "She drops a bundle on the rail, and writes something on the pick list. You lean over to read it. It just says {i}SEAT — size up{/i}, underlined twice."
    fs_driver "\"Who used up the mediums?\""
    fs_regan "\"Prentice.\""
    hide fs_regan
    show cg fs_jodie_stool onlayer cgl
    show fs_jodie grin at vn_cast_slot
    "And Jodie's here. In the depot, at the crack of dawn, in a coat over a pink jumper, sitting on a tall stool by the fit room door with a coffee and a huge grin."
    fs_you "\"What are {i}you{/i} doing here?\""
    fs_jodie "\"Customers can watch a fit check. It's in the terms.\""
    "She waggles her phone."
    fs_jodie "\"I read them. You're not the only one.\""
    fs_deb "\"She's right. It's in the small print. I'm not saying it's a good clause.\""
    fs_jodie "\"It's a {i}great{/i} clause.\""
    "She can't hear Deb, and doesn't need to."
    "You pick up the large. It's heavier than the medium. More fabric. You hold the shorts up against yourself, and they still look narrow, and you laugh out loud at the pick face."
    fs_you "\"Regan. Regan, what if the large doesn't—\""
    fs_regan "\"Then it's on the pick list.\""
    fs_you "\"And what if the—\""
    fs_regan "\"Then it's on the pick list.\""
    "On the open channel somebody asks who's been eating the mediums, and somebody else says it's the new driver who reads the terms, and three drivers laugh at once in your ear. You wave at the ceiling like they can see you."
    fs_you "\"Hi! It's me! I read the terms!\""
    fs_deb "\"They know. Everyone knows. Fit room. Your slot's open and Regan doesn't wait.\""
    "Jodie slides off her stool and follows you to the door with her coffee, eyes on your ass the whole way, typing on her phone."
    fs_you "\"What are you writing?\""
    fs_jodie "\"Notes. For the review. Walk slower.\"\n{size=-5}{color=#ff8fa3}▸ Onto the scanner platform{/color}{/size}"
    hide fs_jodie
    $ vn_pass(10)
    jump fs_platform

label fs_platform:
    $ vn_enter(bg="fs_fitroom", pc="neutral", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_platform_scan")
    show cg fs_platform_scan onlayer cgl
    "The scanner platform's a round steel plate in the middle of the fit room, with the arch over it and a screen on the wall. You step up in the large."
    "It won't close either. The shorts sit open at the back, the waistband cutting across the middle of your ass, the rest of it spilling out."
    "The arch hums. Blue light sweeps down you."
    $ _fs_a, _fs_b, _fs_c = fs_scan("Seat"), fs_scan("Thigh"), fs_scan("Chest", False)
    fs_scanner "[_fs_a] [_fs_b] [_fs_c]"
    fs_regan "\"Again.\""
    "The arch sweeps again, and says the same three things, and nobody looks at the chest line."
    fs_jodie "\"Four stars for the seat. Five. Sorry. {i}Five{/i}.\""
    show cg fs_platform_squat onlayer cgl
    fs_regan "\"Turn.\""
    "You turn on the plate."
    fs_regan "\"Squat.\""
    "You squat, and the open shorts creak, and your thighs spread wide and soft over your heels, and Jodie makes the kettle noise again."
    fs_regan "\"Up. Again. Slower.\""
    "You go slower: all the way down, all the way up, every eye in the room on your ass. Your small cock bobs in the pouch. It's dripping, and you hate that it's dripping."
    "The arch sweeps you again like a big blue mirror that only ever tells you you're too big for the clothes."
    fs_regan "\"Fit check needs a full range of motion. Load-bearing.\""
    "She puts the clipboard down on the rail. It's the first time you've ever seen her put it down."
    fs_regan "\"Bend.\""
    show fs_pc protesting
    fs_you "\"Bend {i}where{/i}? The fit check's the {i}scanner{/i}. It says so. 'Driver is scanned on the depot platform.' Scanned. That's the verb. That's the whole—\""
    show cg fs_platform_bent onlayer cgl
    "She takes your polo collar in one fist and folds you over the arch rail by it. Face-down, hands slapping the chrome, knees on the steel plate, your huge ass up and out of the open shorts." with vnfx("shake")
    "Her other hand clamps on your hip and keeps it there."
    fs_you "\"Regan— {i}Regan{/i}— load-bearing means the {i}garment{/i}—\""
    "You hear her zip. You feel the heavy hot weight of her cock land on your ass and lie there, all the way up your crack and past the small of your back."
    fs_you "\"Oh— oh, no, no, that's— that's {i}all{/i} of it? Regan, that won't— that's not a {i}fit{/i}—\""
    fs_regan "\"Volume, not depth. Breathe out.\""
    "She lubes you with two fingers and a lot of lube, holding you down on the rail by the back of the collar."
    fs_you "\"I'm not breathing {i}anything{/i}—\""
    "You breathe out anyway, because your body does it for you."
    menu:
        "She's lined up behind you. The scanner hums."
        "Grip the rail":
            $ fs.fit_choice = "rail"
        "\"That is NOT a fit check—\"":
            $ fs.fit_choice = "protest"
        "Reach for the scanner's stop":
            $ fs.fit_choice = "stop"
    jump fs_platform_sex

label fs_platform_after:
    $ vn_enter(bg="fs_fitroom", pc="flushed", pc_tag="fs_pc", cast=[], cg="fs_platform_green")
    if fs.fit_choice == "stop":
        "You'd had your fingertips on the edge of the red stop button when she caught your wrist, and put your hand back on the rail, and kept it there under hers the whole way."
    elif fs.fit_choice == "protest":
        "You'd said it was NOT a fit check so many times the words had stopped sounding like words."
    else:
        "Your knuckles had gone white on the rail, and you'd hung on to it like it was the clause."
    "She doesn't stop. She doesn't soften. She keeps going, long and slow, all the way out and all the way in, and the screen on the wall has been green since you broke."
    show screen fs_dash(3)
    "It flips straight to your dashboard, huge, on the fit room wall."
    hide screen fs_dash
    show cg fs_platform_jodie onlayer cgl
    "And Jodie's off her stool. She crawls across the fit room floor, under the arch, onto the platform, and sits back on her heels in front of you, under you, and looks up at your small cock bouncing in the open shorts."
    fs_jodie "\"Mine.\""
    "She takes it in her mouth."
    fs_you "\"{i}Hhhaaah{/i}— yes— {i}yes{/i}— both of you— {i}ahh{/i}—!\""
    "Regan in your ass. Jodie on your cock. The arch sweeping blue down your back on every pass."
    fs_jodie "\"Four stars for the seat. Five for the squeal. Do it again.\""
    "She mumbles it round you, pulls off with a wet pop, jerks you while she talks, and sucks you back in. You squeal again, louder, for the rating."
    "Regan picks up the pace. Long, heavy strokes, every one dragging out of you to the tip and slamming home to the root, her hips smacking your huge new ass so hard it ripples. The platform rings under your knees."
    fs_you "\"Oh— oh, the {i}seat{/i}— it's all seat— Regan, I'm all {i}seat{/i}— don't stop, don't you {i}dare{/i} stop—!\""
    fs_regan "\"Noted.\""
    fs_you "\"Passed— {i}passed{/i}— I passed— oh, I'm coming— Jodie, I'm—\""
    "Jodie just sucks harder. You come in her mouth with Regan buried to the root in your ass, screaming at the arch, and Jodie swallows it all and pulls off and licks her lips." with vnfx("flash")
    fs_jodie "\"Five. Obviously.\""
    show cg fs_platform_email onlayer cgl
    "Your phone's in your hand. You don't remember picking it up. You're typing."
    "Regan's still in you, still moving, and you're typing a second email to Vellum, longer and more polite than the first, with headings, and the spreadsheet of your ratings attached."
    $ fs_mail_lines = ["{b}To: Vellum{/b}  {size=-4}(attachment: ratings.xlsx){/size}", "Dear Vellum, following up on my previous message. I'd like to raise a second concern, regarding the Verified Fit tier. The terms say the driver is \"scanned on the depot platform\". Please see section two of the attached for the events of today's scan, which I don't believe the wording supports. I'd be grateful for a clarification of \"load-bearing\".", "P.S. I still don't know what the route bonus is."]
    show screen fs_mail(fs_mail_lines)
    menu:
        "How do you sign it?"
        "Sign it \"Warm regards\"":
            $ fs.sign2 = "Warm regards"
        "Sign it \"With thanks, and see attached!\"":
            $ fs.sign2 = "With thanks, and see attached!"
    jump fs_three_sent

label fs_three_sent:
    $ fs_mail_lines = fs_mail_lines + ["{i}%s T. Prentice.{/i}" % fs.sign2]
    show screen fs_mail(fs_mail_lines)
    "Send."
    hide screen fs_mail
    "Nothing."
    fs_deb "\"Tier confirmed. Verified Fit. Five stars, no notes.\""
    "Regan's still in you. She hasn't said a word since \"Noted.\" She shifts her grip on your hips and keeps going, and the arch keeps sweeping, and you hang on the rail moaning into the steel."
    fs_you "\"Deb— Deb— {i}hhn{/i}— what's the next tier need?\""
    fs_deb "\"In-home certification. A customer's front room, a full fitting, and—\""
    fs_you "\"Put me down for it— {i}ahh{/i}—!\""
    fs_deb "\"You're not even off the platform.\""
    fs_you "\"{i}Ahh{/i}— log it— {i}log{/i} it—!\""
    fs_deb "\"Logged.\""
    hide cg onlayer cgl
    $ vn_until(20)
    "It's dark when you finally climb the stairs to the drivers' room, walking very carefully.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(5)
    jump fs_demotion

## ---- DAY 4, IN-HOME (Vellum Four Demotion, Four Appeal) ------------------------------------------

label fs_demotion:
    $ fs_advance(4)
    $ vn_enter(bg="fs_drivers_room", pc="eager", pc_tag="fs_pc", cast=[], cg="fs_demotion")
    show cg fs_demotion onlayer cgl
    vn_sfx "Bzzt."
    "It's still dark. Your phone's buzzing on the pillow. You squint at it."
    "{color=#ff5f5f}{b}TIER REMOVED · Verified Fit.{/b}{/color} {i}An in-home fitting was logged outside its window. Policy breach. This decision was made automatically.{/i}"
    "You sit up. You read it again. You start to grin."
    fs_you "\"Oh, it's {i}on{/i}.\""
    "Outside window. {i}Outside window.{/i} You've never been outside a window in your life."
    "You scroll back through yesterday on the app, and there it is: the fit check, logged as an in-home fitting, because somebody at Vellum filed the depot's fit room under customer addresses. Jodie's stool counted as a front room."
    fs_you "\"That's not a {i}breach{/i}. That's a {i}clerical error{/i}. That's a {i}categorisation{/i} problem.\""
    "You roll out of bed and your ass gets there first. It hits the mattress edge, heavy, and bounces, and you yelp and laugh and grab it. Still huge. Still yours."
    "You stand there in the dark in nothing but the jockstrap, one hand full of your own seat and the other holding the phone up to your face, reading the policy by its glow."
    "Section on automatic decisions. Section on appeals. Section on appeals of automatic decisions, with its own sub-heading, which nobody has ever opened, because the page loads with a little spinning wheel like it's surprised to be asked."
    fs_you "\"Oh, I {i}love{/i} you.\""
    "There's an appeal button. Of course there's an appeal button. You've read the terms."
    menu:
        "You hit it before your feet are even cold."
        "Appeal it by the book, every clause cited":
            $ fs.appeal = "book"
        "Appeal it with the spreadsheet and a smiley face":
            $ fs.appeal = "cheeky"
    $ vn_pass(20)
    jump fs_appeal

label fs_appeal:
    $ vn_enter(bg="fs_drivers_room", pc="eager", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_drivers_room onlayer bgl
    if fs.appeal == "cheeky":
        "The appeal's done before the kettle is: the spreadsheet attached, every rating highlighted gold, and a smiley face at the bottom."
    else:
        "The appeal's done before the kettle is: every clause of the terms cited by name, in order, with headings."
    fs_deb "\"Dispatch, go ahead.\""
    "On the dot."
    fs_you "\"Deb! Deb, have you seen it? They took Verified Fit! Automatically! Before {i}six{/i}!\""
    fs_deb "\"I've seen it.\""
    fs_you "\"It's {i}wonderful{/i}. I've never appealed anything. I've got sub-headings.\""
    fs_deb "\"Of course you have.\""
    fs_you "\"Deb. I need a co-signature. On the open channel, so it's logged.\""
    fs_deb "\"Absolutely not.\""
    fs_you "\"Deb. Deb. {i}Deb.{/i} It's an {i}automatic{/i} decision, it's a {i}policy{/i} breach, they can't— Deb, I have the spreadsheet open—\""
    "A long sigh. Then the click of the open channel, and three other drivers suddenly listening."
    fs_deb "\"Dispatch co-signs Prentice's appeal. For the record.\""
    fs_you "\"Thank you!\""
    "She keeps the channel closed a second longer than she needs to."
    fs_deb "\"I get a bonus on every tier my drivers clear. You've made me more this month than the rest of the roster put together. Don't get demoted.\""
    vn_sfx "Click."
    fs_deb "\"First drop's Kestrel Court. In-home certification. Afternoon window.\""
    "That's all she ever says about it. You don't care either way. You're grinning."
    $ vn_enter(bg="fs_fitroom", pc="eager", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_rescan_4")
    show cg fs_rescan_4 onlayer cgl
    "Regan wants a re-scan for the appeal file. You step up onto the platform in the large."
    $ fs_body(4)
    "{color=#ff5fb8}And the large is {i}tight{/i}.{/color}"
    "{color=#ff5fb8}Not just the seat now. Your hips. They've gone {i}wide{/i} overnight, flaring out from a waist that's pulled in narrow, so narrow the polo hangs loose there and then grips you hard round the hips.{/color}"
    "{color=#ff5fb8}You put your hands on your waist and your fingers nearly meet. You slide them down and your hips just keep curving out under them.{/color}"
    fs_you "\"Oh— {i}oh{/i}— I've got a {i}waist{/i}— Regan, look, I've got a—\""
    "Regan doesn't look."
    "{color=#ff5fb8}And your nipples. They've gone puffy: soft and swollen and pink, pushing two little peaks into the front of the navy polo, so sensitive that the fabric shifting over them makes you gasp.{/color}"
    "You pinch one through the shirt. Your knees go."
    fs_you "\"{i}Hhaah{/i}— oh, they're— they're so {i}puffy{/i}— they're all— {i}mmh{/i}—\""
    "The scanner sweeps blue light down your front."
    $ _fs_a, _fs_b, _fs_c = fs_scan("Hip"), fs_scan("Seat"), fs_scan("Chest", False)
    fs_scanner "[_fs_a] [_fs_b] [_fs_c]"
    "A little AA on your chest, puffy and pink and begging to be touched, and the scanner says within spec. Nobody blinks."
    "Your ass rolls when you shift your weight, all on its own. And your hands keep going back to your nipples and your hips and your ass, quick and greedy, like they've been shown exactly where to go."
    fs_regan "\"Large. Still.\"\n{size=-5}{color=#ff8fa3}▸ Kestrel Court, afternoon window{/color}{/size}"
    $ vn_until(14)
    jump fs_kestrel

## ---- rung 4: Kestrel Court (Vellum Four Kestrel). Non-con, flips on "Appeal upheld". -----------

label fs_kestrel:
    $ vn_enter(bg="fs_kestrel", pc="neutral", pc_tag="fs_pc", cast=[("fs_kieran", "talking"), ("fs_ade", "grin"), ("fs_rich", "grin")], cg="fs_kestrel_door")
    show cg fs_kestrel_door onlayer cgl
    "Kestrel Court is a terrace house with three bikes in the hall and three names on one account. The door opens on all of them at once."
    fs_kieran "\"Is that the Vellum— it's the Vellum guy—\""
    fs_ade "\"Did someone order the in-home thing—\""
    fs_rich "\"{i}I{/i} ordered it—\" \"You did {i}not{/i}—\""
    "Kieran is skinny and quick. Ade is tall with a beard. Rich is broad and smiling. They all talk at the same time, none of them listen to the others, and they all look at you like the plumber's arrived."
    fs_you "\"Right. In-home certification. I fit the items in your front room, you sign off on the—\""
    fs_deb "\"Certification requires a full fitting. Every item, every customer.\""
    fs_you "\"Every {i}item{/i}. On every customer. That's what it—\""
    fs_kieran "\"She said every customer. Did you hear her? I heard her through his ear.\""
    fs_ade "\"Is that in the terms?\" \"It's in the terms.\" \"We paid for in-home—\""
    show fs_pc protesting
    fs_you "\"It means the {i}items{/i}—\""
    fs_deb "\"Every item, every customer.\""
    "Flat, louder, so it carries out of your earpiece into the hall."
    $ fs.fit = "nude"
    show cg fs_kestrel_peel onlayer cgl
    "Rich takes the box off you. Ade takes your elbow. Kieran gets the waistband of the large and pulls, and it peels down over your hips and catches on your new wide flare."
    "He has to wriggle it, side to side, your ass bouncing free one cheek at a time, smooth and pale and round, the jockstrap straps framing it."
    fs_you "\"Oi— {i}oi{/i}— the clause is about the {i}garments{/i}— you fit the {i}garments{/i} on the {i}customer{/i}—\""
    fs_rich "\"Oh, mate.\" \"Oh, {i}mate{/i}.\" \"Is that— are we meant to—\""
    fs_you "\"You're meant to try the {i}shorts{/i} on!\""
    fs_kieran "\"Says in-home, mate. We paid for in-home.\""
    "He peels the polo up over your puffy nipples, and their three heads tilt the same way at once."
    fs_ade "\"Me first—\" \"No, me—\" \"It's my account—\" \"It's {i}all{/i} our account—\""
    fs_deb "\"Alphabetical.\""
    fs_you "\"Deb, don't {i}help{/i} them—\""
    fs_deb "\"By whoever's got his trousers off. Your complaint's logged.\""
    "Kieran's got his trousers off."
    show cg fs_kestrel_carpet onlayer cgl
    "Then you're on their front-room carpet on your knees and elbows with your huge ass in the air, Ade's big hand flat between your shoulder blades holding you down, Kieran behind you, and Rich on the sofa narrating."
    fs_deb "\"One at a time. Certification's per customer.\""
    fs_you "\"It's per {i}item{/i}— it's per— {i}ahh{/i}—!\""
    "Kieran pushes in. Not huge, but quick and eager and right, and you yell into the carpet so loud Rich jumps." with vnfx("shake")
    fs_rich "\"Is he alright?\" \"He's fine, listen to him—\" \"Is that the noise they make? Do they all make that noise?\""
    fs_you "\"{i}Ahh{/i}— it's NOT— the clause— the {i}clause{/i}— {i}hhn{/i}—!\""
    vn_sfx "Slap. Slap. Slap."
    fs_kieran "\"Is this right? Is this how it— is this what certified feels like? It feels {i}certified{/i}—\""
    "He fucks you fast, all elbows, gabbling the whole time."
    fs_you "\"It's not— {i}ahh{/i}— it's not {i}certified{/i}— oh, why's it— {i}ahh{/i}—\""
    fs_deb "\"Certification requires the customer to finish.\""
    fs_kieran "\"Oh, it's {i}required{/i}—\""
    "He heard that too, and does, with a squeak, buried in you, and pulls out."
    show cg fs_kestrel_ade onlayer cgl
    "Ade swaps places with him without letting go of you, sliding into the mess he left, longer, slower, his big hands on your waist like he's checking the fit."
    fs_ade "\"Huh. Everything in the range is padded anyway. Chest line hasn't moved since intake.\""
    "Everyone stops talking for a second. Then Rich laughs so hard he falls off the sofa."
    fs_you "\"{i}Hhh{/i}— {i}stop{/i}— {i}stop{/i} fitting me— I'm the— {i}ahh{/i}— I'm the {i}driver{/i}—\""
    vn_sfx "Bzzt."
    "Your phone buzzes on the carpet under your face."
    fs_deb "\"{i}Appeal upheld.{/i} Verified Fit restored.\""
    show fs_pc flushed
    "It goes through you like a dropped parcel. The tier's back. The stars are on the screen."
    "And Ade's cock is dragging over that place on every stroke, and your hips have been pushing back onto him for a while now, and you just stop telling them not to."
    fs_you "\"...Upheld. {i}Upheld{/i}. Oh— {i}oh{/i}— {i}YES{/i}— upheld— don't stop, don't you {i}stop{/i}—!\"" with vnfx("flash")
    "You're coming, just from that: Ade's cock and the word {i}upheld{/i}. Your small cock dribbles on their carpet, untouched, useless, and you shove back onto him for more."
    show screen fs_dash(4)
    "The screen flips to the dashboard."
    hide screen fs_dash
    fs_ade "\"Cheers, mate.\""
    "He finishes in you with a long low groan, like you've passed him the salt."
    show cg fs_kestrel_rich onlayer cgl
    "Then Rich is in you. Biggest of the three, slow and heavy, his belly on your ass, grinding in deep and staying there. Every stroke shoves you forward on the carpet. Your puffy nipples drag on the pile and you squeal every time."
    fs_rich "\"Oh, he {i}likes{/i} that.\""
    "He does it more, pleased."
    fs_you "\"{i}Ahh{/i}— in-home— in-{i}HOME{/i}— certify it— certify {i}all{/i} of it—!\""
    show cg fs_kestrel_faces onlayer cgl
    "Kieran and Ade kneel up either side of your face with their cocks in their fists, hard again already, still arguing."
    fs_kieran "\"Is this certification?\" \"This is definitely certification.\" \"Do we sign something—\""
    "They come across your face together, one each side: hot and thick across your cheeks, your lips, into your open mouth while you're still moaning, while Rich is still buried in you and still moving." with vnfx("flash")
    fs_you "\"Mmhh— {i}certified{/i}— mmh—\""
    fs_deb "\"Kestrel Court has left a review. Five stars. {i}Seat: plush cut. Thigh: plush cut. Waist: small. Delivery: excellent. Would order again.{/i} Five stars, no notes.\""
    "You lick your lips. Rich is still in you."
    fs_you "\"Deb— what's the next tier need—?\""
    fs_deb "\"Returns sign-off. You'll hate it.\""
    fs_you "\"Put me down for it—!\""
    fs_rich "\"Is that the next one? Is there a next one?\" \"There's always a next one—\" \"Rich, you're not {i}done{/i}, are you?\" \"I'm not done.\""
    "Rich isn't done. He gets a fresh grip on your hips. Kieran gets a hand back on your shoulders."
    menu:
        "Rich isn't done. Neither are the other two."
        "Claw at the carpet":
            $ fs.carpet = "claw"
            jump fs_kestrel_sex
        "\"It said every ITEM—\"":
            $ fs.carpet = "item"
            jump fs_kestrel_sex
        "Crawl for the coffee table":
            $ fs.carpet = "crawl"
            jump fs_kestrel_sex
        "Kestrel Court argues itself out":
            jump fs_kestrel_close

label fs_kestrel_close:
    $ vn_enter(bg="fs_kestrel", pc="flushed", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_kestrel onlayer bgl
    "They lose the thread arguing whose turn it is, and you get your shorts back on in the hall.\n{size=-5}{color=#ff8fa3}▸ Home to the drivers' room{/color}{/size}"
    $ fs.fit = "kit"
    call vn_night(5)
    jump fs_morning_five

label fs_kestrel_after:
    $ vn_enter(bg="fs_kestrel", pc="flushed", pc_tag="fs_pc", cast=[("fs_kieran", "talking")], cg="fs_kestrel_sex_cum")
    if fs_enc.partner_came:
        "They finish one after another, all three talking the whole time, and you lie on the carpet full of all of them, moaning the review back to them."
    else:
        "They finish across your back and your ass, all three, still arguing about whose turn it was."
    hide cg onlayer cgl
    show fs_kieran talking at vn_cast_slot
    fs_kieran "\"Same time next week?\" \"Can we book him?\" \"You can't book a {i}person{/i}—\" \"It's in the terms—\""
    fs_deb "\"Customer's asking to book you. Logged.\"\n{size=-5}{color=#ff8fa3}▸ Home to the drivers' room{/color}{/size}"
    hide fs_kieran
    $ fs.fit = "kit"
    call vn_night(5)
    jump fs_morning_five

## ---- DAY 5, RETURNS (Vellum Five Morning, Five Clive) --------------------------------------------

label fs_morning_five:
    $ fs_advance(5)
    $ vn_enter(bg="fs_pickface", pc="eager", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_drivers_room onlayer bgl
    "You wake in the drivers' room over the van bay with the roller door rumbling up under the floor."
    fs_deb "\"Dispatch, go ahead.\""
    fs_you "\"Returns sign-off. How do I get it?\""
    fs_deb "\"Returns processing. At Vellum that means you take every returned item back to the customer and demonstrate the defect. On yourself.\""
    fs_you "\"Every one?\""
    fs_deb "\"Clive Ormsby alone has a backlog you could build a house out of.\""
    fs_you "\"Put the whole backlog on my run.\""
    fs_deb "\"...Fine.\""
    show bg fs_pickface onlayer bgl
    show fs_regan flat at vn_cast_slot
    "Regan's at the pick face. She looks at the large splitting on you, and then not at you, and drops a new bundle on the rail."
    fs_regan "\"Largest we stock.\""
    fs_you "\"Who used up the larges?\""
    fs_regan "\"You did.\""
    show cg fs_largest onlayer cgl
    "It goes on. Just. It's loose at the waist and tight everywhere else, and it holds."
    "You do a turn in the pick face anyway, because nobody's stopping you. The shorts ride up your seat with every step. The waistband gapes at the back over the small of your waist and then bites hard into your hips."
    "Your thighs rub together all the way down now, the Lycra hissing where they meet, and every time they meet you feel it in your cock."
    fs_you "\"Is it holding? Regan, is it holding?\""
    fs_regan "\"Today.\""
    "She writes {i}largest — today{/i} on the pick list, and underlines {i}today{/i}."
    hide cg onlayer cgl
    "The returns bay behind her is stacked to the roof: grey Vellum bags, every one with a reason printed on the label. Waistband. Seam. Fabric. Fabric. Gusset. Fabric. Half of them have the same name on the address line."
    fs_you "\"Is that all {i}him{/i}?\""
    fs_regan "\"Most of it.\""
    fs_deb "\"Loading the backlog onto your van. You'll want to drive carefully. It's heavy, and so are you.\""
    fs_you "\"Deb!\""
    fs_deb "\"I'm talking about the {i}seat setting{/i}, Prentice.\""
    fs_you "\"Deb. What's the next tier need?\""
    fs_deb "\"Invite only. Nobody's been invited. Ever.\""
    fs_you "\"Put me down for it.\""
    fs_deb "\"You can't be put down for an {i}invitation{/i}—\""
    "You're already in the van.\n{size=-5}{color=#ff8fa3}▸ The returns run{/color}{/size}"
    hide fs_regan
    $ vn_pass(90)
    jump fs_clive

## ---- rung 5, Clive (Vellum Five Clive). Non-con, never flips; the largest step begins. --------

label fs_clive:
    $ vn_enter(bg="fs_clive_hall", pc="neutral", pc_tag="fs_pc", cast=[("fs_clive", "sour")], cg="fs_clive_door")
    show cg fs_clive_door onlayer cgl
    "Clive Ormsby lives in a flat full of Vellum boxes. Half of them are open. All of them are going back."
    "He's a thin, tidy man in a cardigan with a face like a complaint. He looks at you in the largest stock in the doorway, drizzle on your shoulders."
    fs_clive "\"The waistband rolls.\""
    "That's his hello."
    fs_you "\"I'm here to demonstrate the defect. On the garment. I put the garment on, I show you it rolling, you sign the—\""
    fs_clive "\"Good. It rolls. And so do you. Defective. Look at it. I'm returning that as well.\""
    show fs_pc protesting
    fs_you "\"You can't return the {i}driver{/i}—\""
    fs_deb "\"Waistband: rolls.\""
    "Reading off the returns list."
    show cg fs_clive_pile onlayer cgl
    "He takes you by the back of the neck, the way he'd pick up a garment by the label, and bends you over his returns pile, face-down in a heap of cellophane bags." with vnfx("shake")
    "He pulls the shorts down to your thighs and pushes into you, and complains the whole time."
    fs_clive "\"See? Rolls. {i}Rolls.{/i} Look at it.\""
    fs_you "\"{i}Ahh{/i}— get {i}out{/i}— returns means the {i}garment{/i}— I demonstrate the {i}garment{/i}—!\""
    fs_clive "\"And the seam. Feel the seam.\""
    fs_you "\"I'm not feeling the— {i}hhn{/i}— Deb— {i}Deb{/i}—!\""
    fs_deb "\"Complaint noted. Seam: puckered.\""
    fs_clive "\"And the leg. The leg opening's too high. Look at that. That's not a leg, that's an {i}invitation{/i}.\""
    fs_you "\"It's— {i}ahh{/i}— it's meant to be— the high-cut leg— it's the {i}flattering{/i} leg— get {i}off{/i} me—\""
    vn_sfx "Slap."
    fs_clive "\"Flattering to {i}whom{/i}. I've worn it twice. Nobody was flattered.\""
    fs_you "\"Clive— {i}Clive{/i}— this is not a— {i}return{/i}— {i}ahh{/i}—\""
    fs_clive "\"I didn't {i}order{/i} an invitation.\""
    "He fucks you harder to make his point, his bony hips smacking your ass, his hand on your neck keeping your face in the cellophane, and you yell into it so loud it fogs."
    fs_deb "\"Next return. Gusset: inadequate.\""
    show cg fs_clive_grow onlayer cgl
    $ fs_body(5)
    "{color=#ff5fb8}And somewhere around the gusset, you {i}feel{/i} it.{/color}"
    "{color=#ff5fb8}Your ass swells, right there under Clive's hands. It pushes back against him, bigger, rounder, heavier, filling out until the largest stock is creaking across your cheeks and his hands are full and then overflowing.{/color}"
    "{color=#ff5fb8}Your thighs thicken against each other, soft and huge, squeezing his legs.{/color}"
    fs_you "\"{i}Oh{/i}— no— no, it's {i}growing{/i}— it's growing {i}now{/i}— Clive, stop, the {i}seat{/i}, look at the {i}seat{/i}—!\""
    fs_clive "\"The seat was always inadequate.\""
    "He fucks you harder."
    fs_you "\"{i}Ahh{/i}— {i}stop{/i}—!\""
    "{color=#ff5fb8}And your voice comes out {i}wrong{/i}. High. Light and breathy, a soft moan in your own throat that isn't the one you came in with.{/color}"
    "You clap a hand over your mouth and moan through it anyway."
    fs_you "\"Oh— oh, listen to me— {i}listen{/i} to it—\""
    "Everything back there is lit up. Every slap of his hips on your ass rings through you like a bell. Your nipples are rubbing the cellophane, and you can feel every crinkle."
    "And your body just {i}knows{/i} now: how to roll back onto a cock, how to squeeze on the pull-out, how to pop your hips so your thighs grip. You're yelling no into the cellophane and your ass is doing all three, and you can't make it stop."
    fs_deb "\"Next return. Fabric. Pills.\""
    fs_clive "\"It {i}pills{/i}. Defective. I'm sending it all back.\""
    fs_you "\"Just— just {i}finish{/i}— finish and sign it {i}off{/i}— sign the return, Clive, {i}please{/i}, sign it—!\""
    "He comes in you, still complaining, and you come with him, untouched, shouting {i}please{/i} into his returns, and none of it was a yes." with vnfx("flash")
    fs_clive "\"Defective. Returned.\""
    "He signs the form on your back, writing."
    fs_deb "\"All returns noted. Your complaint too.\"\n{size=-5}{color=#ff8fa3}▸ On to Kestrel Court{/color}{/size}"
    $ vn_pass(60)
    jump fs_kestrel_five

label fs_kestrel_five:
    $ vn_enter(bg="fs_kestrel", pc="neutral", pc_tag="fs_pc", cast=[("fs_kieran", "talking"), ("fs_ade", "grin"), ("fs_rich", "grin")], cg="fs_van_slide")
    show cg fs_van_slide onlayer cgl
    "You can't get out of the van the way you used to. You have to swing your legs out together and slide, and your ass catches on the seat, and you pop out onto the pavement like a cork."
    "Kestrel Court. All three. Talking."
    fs_kieran "\"He's bigger—\" \"He's {i}definitely{/i} bigger—\" \"Is that allowed? Is that in the—\""
    fs_you "\"Returns. You sent back the shorts. I put the shorts on, I show you the fault, you sign—\""
    fs_ade "\"They didn't fit Rich.\" \"They didn't fit {i}anyone{/i}—\" \"They'd fit him—\""
    show cg fs_thighs_rich onlayer cgl
    "The largest stock creaks on you, stretched so tight across your seat the logo's gone wide."
    "Rich, flat on his back on the sofa, reaches up, gets you by the hips and pulls you down onto his lap facing away from him." with vnfx("shake")
    "His cock slides up between your thick thighs. Not in you; {i}between{/i} them. And his big hands come round and clamp your thighs shut round it."
    show fs_pc protesting
    fs_you "\"Rich— Rich, the {i}shorts{/i}— returns means the {i}shorts{/i}—\""
    fs_rich "\"Oh. Oh, {i}mate{/i}.\""
    "He fucks your thighs. Up and down, his cock sliding through the soft heavy squeeze of them, his hands holding them shut, the head popping out between them on every stroke."
    "Every stroke drags along your small useless cock in its pouch, rubbing it, rubbing it."
    fs_you "\"{i}Hhn{/i}— let {i}go{/i} of them— that's not a— {i}ahh{/i}— that's not demonstrating, that's—\""
    "And your thighs squeeze. On their own. Tighter than his hands are holding them. He groans like he's dying, and the noise goes straight through you, and something gives."
    show fs_pc flushed
    fs_you "\"...Oh. {i}Oh{/i}. Plush cut— it's the {i}plush cut{/i}— soft-touch inner leg— you can feel the fabric— you can feel {i}me{/i}—!\""
    "You clamp down on purpose, and grind back, and Rich's hands let go, because they don't need to hold anything any more."
    fs_ade "\"Best thighjob in company history.\""
    "From the armchair, very seriously."
    fs_kieran "\"Is there a company history?\" \"There is now—\""
    "Kieran's on the floor at your feet with the returns form, reading it aloud."
    fs_kieran "\"{i}Reason for return: didn't fit.{/i} Didn't fit {i}who{/i}, though? Look at it now. It fits {i}this{/i}.\""
    fs_ade "\"It doesn't fit this. Nothing fits this. That's the point of the—\""
    fs_you "\"Ahh— soft-touch— {i}hhn{/i}— Rich, {i}harder{/i}, I'm demonstrating—!\""
    "Rich grabs the fronts of your thighs again, just to feel them, and squeezes them tighter round himself, and you squeal, and squeeze back."
    fs_rich "\"Is he meant to be enjoying it this much?\" \"It's a {i}return{/i}—\" \"I'd return it again—\""
    fs_you "\"Return it— {i}ahh{/i}— return it as often as you {i}like{/i}—!\""
    fs_deb "\"That is not company policy.\""
    fs_you "\"It— {i}is{/i} now—!\""
    show cg fs_thighs_cum onlayer cgl
    "Rich comes between your thighs, and it slicks them all the way down to your knees." with vnfx("flash")
    fs_deb "\"Next return— next— where was I.\""
    "She's lost her place. She's lost her voice a bit too."
    fs_deb "\"Next return, Prentice.\"\n{size=-5}{color=#ff8fa3}▸ Back to the warehouse{/color}{/size}"
    $ vn_pass(60)
    jump fs_pallet

## ---- rung 5's end, the pallet (Vellum Five Pallet, Five Sent). Non-con, flips on "Nothing off
## the rack". -------------------------------------------------------------------------------------

label fs_pallet:
    $ vn_enter(bg="fs_pickface", pc="neutral", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg=None)
    show bg fs_pickface onlayer bgl
    show fs_regan flat at vn_cast_slot
    "Back at the warehouse you can barely walk through the pick face. Your hips catch the racks."
    "Regan's waiting at a pallet, shrink-wrapped flat, at waist height. She points at it."
    fs_regan "\"Over.\""
    show fs_pc protesting
    fs_you "\"Regan, I've got a returns report to file, I've got— I'm {i}not{/i} going over a—\""
    hide fs_regan
    show cg fs_pallet_split onlayer cgl
    "She takes your collar and puts you over it. Face-down on the shrink-wrap, her palm flat between your shoulder blades, your huge ass up." with vnfx("shake")
    vn_sfx "Rrrrip."
    "And the largest stock Vellum carries gives up. Right down the seat, the whole back of it splitting open, your ass bursting out through the gap."
    $ fs.fit = "split"
    fs_you "\"Oh— oh, it {i}split{/i}— Regan, let me {i}up{/i}—\""
    fs_regan "\"Hold that.\""
    "She doesn't let you up. She pushes into you instead."
    fs_you "\"{i}AHHH{/i}— Regan— {i}Regan{/i}— get {i}out{/i}— that's the {i}sample{/i}, you're splitting your own {i}sample{/i}—!\""
    "Your new breathy voice cracks right up. She's so big, and your ass swallows her down to the root while you yell at it not to."
    vn_sfx "Slap. Slap. Slap."
    "The pallet creaks. The shrink-wrap squeaks under your puffy nipples. Your thighs are so thick they're pressed together round her, and she has to drive in between them, and every time she does, the split shorts tear a little further."
    fs_regan "\"Specials. Seat, special. Thigh, special. Waist, standard. Chest, standard.\""
    fs_you "\"I'm not a— {i}ahh{/i}— I'm not a special {i}order{/i}— I'm {i}staff{/i}—\""
    fs_deb "\"Logged.\""
    show cg fs_pallet_photo onlayer cgl
    vn_sfx "Click. Click."
    "Regan has her phone out in her free hand: the split uniform, your ass in it, with her in it, from the side."
    fs_regan "\"Special order.\""
    "She puts the phone away and takes your hip again."
    fs_regan "\"Nothing off the rack.\""
    "And it lands. Nothing on any shelf in this warehouse is big enough for you, and she's going to make something that is, and your ass clenches on her so hard she grunts."
    show fs_pc flushed
    fs_you "\"...To order. Make it to {i}order{/i}— oh— {i}oh{/i}— Regan— don't stop— make me to {i}order{/i}—!\""
    fs_regan "\"Stock problem. Hold still. You're splitting my sample.\""
    "She hauls your hips back onto her by the split waistband, and the split runs further."
    "You don't hold still. You can't. Your huge new ass rolls back onto her on purpose now, the way it learned at Clive's this morning: squeezing on the pull-out, swallowing her on the push."
    "The pallet rocks. Somewhere down the racks a forklift reverses, beeping, and nobody comes round the corner, and you moan so loud the beeping stops."
    fs_you "\"{i}Hhaah{/i}— write it down— write it {i}all{/i} down—!\""
    "She does. With one hand. Still fucking you."
    fs_deb "\"Next return— {i}God{/i}— whichever one. Just. Keep going.\""
    "Your phone's on the pallet by your face, buzzing."
    show screen fs_dash(5)
    "The dashboard."
    hide screen fs_dash
    "And under it, an email, half-written since this morning. The longest yet. The most polite yet. Paragraphs."
    $ fs_mail_lines = ["{b}To: Vellum{/b}  {size=-4}(attachment: ratings.xlsx, a tab for each tier){/size}", "Dear Vellum, I hope this finds you well. Further to my previous two messages, I'd like to raise a third concern, regarding the Returns tier: the terms ask the driver to \"demonstrate the defect\", and today I was returned, as a defect, by a customer. Please see the attached, which now has a tab for each tier.", "P.S. As per my previous two emails regarding the route bonus..."]
    show screen fs_mail(fs_mail_lines)
    menu:
        "How do you sign it?"
        "Sign it \"Yours faithfully\"":
            $ fs.sign3 = "Yours faithfully"
        "Sign it \"Looking forward to your reply!!\"":
            $ fs.sign3 = "Looking forward to your reply!!"
    jump fs_five_sent

label fs_five_sent:
    $ fs_mail_lines = fs_mail_lines + ["{i}%s T. Prentice.{/i}" % fs.sign3]
    show screen fs_mail(fs_mail_lines)
    "Send."
    hide screen fs_mail
    "Nothing comes back. Instead the phone starts buzzing and doesn't stop."
    vn_sfx "Bzzt. Bzzt. Bzzt."
    "{color=#e8b923}Re-purchased.{/color} {color=#e8b923}Re-purchased.{/color} Every return you demonstrated today, bought straight back, one after another, the phone dancing across the shrink-wrap."
    fs_you "\"Oh— they're {i}buying it back{/i}— they're all buying it back— {i}ahh{/i}—!\""
    fs_deb "\"Keep— {i}keep{/i} going, that's another one, that's another—\""
    "In your ear Deb isn't even pretending any more."
    show cg fs_pallet_cum onlayer cgl
    "You come. Nobody's touching your cock. It just goes, small and stiff and useless, bouncing against the pallet, spurting over the shrink-wrap while Regan pounds you through it. You scream the warehouse down." with vnfx("flash")
    "Regan comes in you, deep, and pulls out, and finishes across your ass, over the split seat, steady as ever."
    fs_deb "\"Five stars, no notes.\""
    "Very quietly, in your ear."
    "Regan wipes herself on a sample. She doesn't look at you. She's still hard. She lays it on your ass, heavy, and her palm comes back down flat between your shoulder blades."
    fs_regan "\"Again.\""
    fs_you "\"Regan— I've only just— I can't {i}again{/i}—\""
    menu:
        "Her palm between your shoulder blades. Her cock on your ass."
        "Brace on the shrink-wrap":
            $ fs.pallet = "brace"
            jump fs_pallet_sex
        "\"I'm STAFF, Regan—\"":
            $ fs.pallet = "staff"
            jump fs_pallet_sex
        "Twist off the pallet":
            $ fs.pallet = "twist"
            jump fs_pallet_sex
        "Regan goes back to the clipboard":
            jump fs_pallet_close

label fs_pallet_close:
    $ vn_enter(bg="fs_pickface", pc="flushed", pc_tag="fs_pc", cast=[], cg=None)
    show bg fs_pickface onlayer bgl
    "The forklift beeps somewhere down the racks, and she looks at her clipboard, and takes her hand off your back.\n{size=-5}{color=#ff8fa3}▸ Up to the drivers' room{/color}{/size}"
    call vn_night(5)
    jump fs_morning_six

label fs_pallet_after:
    $ vn_enter(bg="fs_pickface", pc="flushed", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_pallet_sex_cum")
    if fs_enc.partner_came:
        "She fills you again, so much it runs out round her and down the backs of your thick thighs."
    else:
        "She pulls out and paints your ass again, and photographs it for the file."
    hide cg onlayer cgl
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Done.\"\n{size=-5}{color=#ff8fa3}▸ Up to the drivers' room{/color}{/size}"
    hide fs_regan
    call vn_night(5)
    jump fs_morning_six

## ---- DAY 6, AMBASSADOR (Vellum Six Morning, Six Depot) -------------------------------------------

label fs_morning_six:
    $ fs_advance(6)
    $ fs.fit = "nude"
    $ vn_enter(bg="fs_drivers_room", pc="flushed", pc_tag="fs_pc", cast=[], cg="fs_wake_6")
    show cg fs_wake_6 onlayer cgl
    "You wake in the drivers' room over the van bay with the roller door rumbling up under the floor."
    $ fs_body(6)
    "{color=#ff5fb8}And you can feel it before you open your eyes.{/color}"
    "{color=#ff5fb8}Your ass is {i}enormous{/i}. You're lying on your front and it's a hill under the sheet, heavy and round and high, and when you roll over it lifts you half off the mattress.{/color}"
    "{color=#ff5fb8}Your thighs are so thick they press together all the way to your knees, soft as pillows. Your hips are wider than your shoulders. You've got a waist you could put your hands round.{/color}"
    fs_you "\"Oh— {i}oh{/i}— oh, that's the {i}biggest{/i}— that's the biggest it's {i}ever{/i}—!\""
    "You grab two handfuls of your own ass and moan so loud someone downstairs drops something. It's so {i}sensitive{/i}. Your whole body is. Your lips are fat and glossy and they buzz all on their own, hungry."
    "{color=#ff5fb8}Your hair's soft and blond and swinging round your jaw in a bob. You push it back. It falls forward again. You don't remember it growing. You don't care.{/color}"
    show cg fs_walk_6 onlayer cgl
    "You stand up and the room has to make space. Your thighs meet before your knees do, soft and heavy, and when you take a step they roll against each other, and the roll goes all the way up into your ass and sets it swaying behind you."
    "You do it again on purpose. You do a lap of the room on purpose, moaning, palms flat on your hips."
    fs_you "\"Oh, the {i}walk{/i}— I've got a {i}walk{/i} now— oh, that's so {i}much{/i}—\""
    "Your puffy nipples are standing up in the cold, pink and swollen and tingling. Still small. Still exactly what they were yesterday. You pinch one anyway and squeal."
    "And you {i}know{/i} things: how to arch, how to look over your shoulder, how to squeeze your thighs and roll your hips and smile at someone so they know exactly what's on offer. Your whole body knows the job now."
    "You try the largest stock. It won't go over your thighs. It just won't. You stand there with it rolled round your knees, laughing."
    fs_deb "\"Dispatch, go ahead.\""
    fs_you "\"Deb. Nothing fits.\""
    fs_deb "\"I know. Check your app.\""
    "{color=#e8b923}INVITATION · Ambassador.{/color} {i}Report to the depot for the overnight manifest.{/i}"
    fs_you "\"Overnight?\""
    fs_deb "\"Overnight. Get some rest. You'll need it.\"\n{size=-5}{color=#ff8fa3}▸ The depot, after dark{/color}{/size}"
    $ vn_until(21)
    jump fs_depot_six

label fs_depot_six:
    $ vn_enter(bg="fs_pickface_night", pc="eager", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg=None)
    show bg fs_pickface_night onlayer bgl
    show fs_regan flat at vn_cast_slot
    "The depot's dark except for the pick face and the van bay, and the sky over the water is thick with stars."
    "Regan's at the rail. She drops a bundle on it without looking up: black cycle shorts, the softest you've ever touched, and on the inside of the waistband, a woven label."
    show cg fs_prentice_label onlayer cgl
    "{b}PRENTICE{/b}"
    "And when you turn them round, it's printed on the seat too. Your name. Across the back."
    fs_regan "\"Nothing off the rack.\""
    $ fs.fit = "prentice"
    show cg fs_prentice_on onlayer cgl
    "You pull them on. They slide up over your thighs like butter and settle round your huge ass like they were poured on, and the pouch at the front holds your small cock snug, and you just stand there in the pick face, stroking your own hips, grinning."
    fs_you "\"They're {i}perfect{/i}— Regan, they're perfect—\""
    "Regan hands you a little zip bag. Gloss. Mascara."
    fs_regan "\"Ambassador kit.\""
    "She goes back to her clipboard. You do it in the wing mirror: pink gloss, black lashes. You blow yourself a kiss."
    "Regan looks at you in it. Actually looks, for the first time, up and down, from your bob to your thighs. Then back at her clipboard."
    fs_regan "\"Fits.\""
    "It's the nicest thing anyone's ever said to you. You tell her so. She doesn't look up again."
    hide fs_regan
    show cg fs_arch_6 onlayer cgl
    "You walk the length of the pick face to the van in them just to feel it: past the racks, past the returns bay, past the scanner arch, which wakes up as you go by and sweeps a lazy blue line across you."
    $ _fs_s = fs_scan("Seat", False)
    fs_scanner "[_fs_s]"
    fs_you "\"Regan. {i}Regan.{/i} It said within spec. The seat. It said my {i}seat{/i} was within—\""
    fs_regan "\"Made to order. It's the spec now.\""
    fs_you "\"Oh— oh, it {i}likes{/i} me— it finally {i}likes{/i} me— {i}ahh{/i}—\""
    "You do a full turn under the arch, arms out, ass swinging, and it sweeps you again and says the same thing, and you squeal at it like it's proposed."
    show cg fs_van_empty onlayer cgl
    "The van's empty. The racks in the back are bare. No parcels. No boxes. Nothing."
    fs_you "\"Where's the stock?\""
    fs_deb "\"At Ambassador, the product is you.\""
    "That's all anyone says about it. You climb up into the driver's seat in your PRENTICE cut, the seat all the way back, your thighs spilling over both sides of it, and the manifest lights up on your phone."
    fs_you "\"Deb. What's after Ambassador?\""
    fs_deb "\"Nothing's after Ambassador.\""
    fs_you "\"Put me down for it.\""
    "A long silence on the channel. Then, for the first time ever, Deb laughs."
    fs_deb "\"First address.\"\n{size=-5}{color=#ff8fa3}▸ The first address{/color}{/size}"
    $ fs.doors = 0
    $ vn_pass(20)
    jump fs_door_one

## ---- THE MANIFEST (Vellum Six Door One to Seven): each door reads the Ambassador listing as a
## sale and takes you at the door; one beat of protest, then the flip. The upselling is after. --

init python:
    FS_DOORS = ["A flat over a launderette", "Jodie Calloway, off Connudatus Street", "The flats on Domus Street",
                "Clive Ormsby", "Kestrel Court", "A house up the hill", "Off Harvest Street", "A rowhouse off the docks"]

    def fs_manifest_rows():
        return [(i < fs.doors, a) for i, a in enumerate(FS_DOORS)]

label fs_door_one:
    $ vn_enter(bg="fs_doorstep", pc="neutral", pc_tag="fs_pc", cast=[], cg="fs_door1_chair")
    show screen fs_manifest(fs_manifest_rows())
    "A flat over a launderette. A dark-haired woman in a silk robe opens the door, looks at your thighs, looks at your face, and steps back to let you in."
    fs_cust "\"Ambassador. Says the product is you.\""
    "She reads it off her phone, and points at the arm of her chair."
    fs_cust "\"Sit.\""
    show fs_pc protesting
    fs_you "\"It means I {i}represent{/i} the— I'm the face of the—\""
    show cg fs_door1_chair onlayer cgl
    "She sits you on it herself, a hand on your shoulder. Your ass swallows it. She's got a glossy black plug in one hand and a bottle of lube in the other, and she doesn't ask."
    fs_cust "\"Up a bit.\""
    fs_you "\"That's not what Ambassador— {i}ohh{/i}—\""
    "She lifts you by the waistband and it slides in, big and smooth and cold, then warm, and you clench round it and yelp, and she twists it, slow, and you grab the back of her chair, and the protest just goes out of you in one long breath."
    show fs_pc flushed
    fs_you "\"...{i}Mmh{/i}— Vellum's own— the plush range— ask for it by— {i}ahh{/i}—\""
    fs_cust "\"Talk me through it. The product.\""
    fs_you "\"It's— {i}ahh{/i}— flared base, for— for comfort— {i}mmh{/i}— body-safe— oh, {i}twist{/i} it again—\""
    "She twists it again. You lose the rest of the sales pitch."
    "She works it in and out of you while she watches your face. Your small cock tents the PRENTICE cut and leaks a dark spot into it. She rates you on her phone with her other thumb before you've even come."
    vn_sfx "Bzzt."
    "{color=#e8b923}★★★★★{/color}"
    fs_cust "\"Off you go.\""
    "She leaves the plug in."
    $ fs.doors = 1
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. Off Connudatus Street.\"\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(40)
    jump fs_door_two

label fs_door_two:
    $ vn_enter(bg="fs_jodie_room", pc="neutral", pc_tag="fs_pc", cast=[("fs_jodie", "hungry")], cg="fs_door2_sofa")
    show screen fs_manifest(fs_manifest_rows())
    "Jodie's door. She's in the doorway in nothing but the harness, the pink strap-on bobbing, before you're out of the van."
    fs_jodie "\"Ambassador. Oh, I {i}knew{/i} it. Get in here. Five stars for the shorts. Five stars for the {i}name{/i}.\""
    show fs_pc protesting
    fs_you "\"Jodie, Ambassador's a {i}representative{/i} role, it doesn't—\""
    show cg fs_door2_sofa onlayer cgl
    "She pulls the plug out of you with a wet pop and has the strap-on in you before it's hit the floor. Bent over her sofa arm by the waistband, your PRENTICE cut round your knees, your name on the seat of them staring up at her." with vnfx("shake")
    fs_you "\"{i}AHH{/i}— Jodie— it doesn't {i}say{/i}— oh— oh, {i}Jodie{/i}—!\""
    "And that's as far as the clause gets. Your ass knows her. It opens for her like it's been waiting all day, and you hear yourself go high and happy."
    show fs_pc flushed
    fs_you "\"{i}Jodie{/i}— yes— {i}yes{/i}—!\""
    fs_jodie "\"Five for the noise. Five for the seat. Five for the {i}everything{/i}— I'm going to need more stars—\""
    "Her hands on your hips, then on your ass, two big handfuls, squeezing, spreading you, watching herself slide in and out."
    fs_jodie "\"Oh, look at it {i}take{/i} it. Remember when it couldn't? Remember the first time on my rug? {i}Five stars for growth.{/i}\""
    fs_you "\"{i}Ahh{/i}— Jodie— the plush cut— ask for it by— {i}name{/i}—!\""
    vn_sfx "Slap."
    fs_jodie "\"I'll ask for it by name. Prentice. {i}Prentice.{/i}\""
    "She comes grinding against the base of it, rating herself, and fucks you through your own orgasm, your cock spattering her sofa cushion." with vnfx("flash")
    $ fs.doors = 2
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. The flats on Domus Street.\"\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(40)
    jump fs_door_three

label fs_door_three:
    $ vn_enter(bg="fs_doorstep", pc="neutral", pc_tag="fs_pc", cast=[], cg="fs_door3_mat")
    show screen fs_manifest(fs_manifest_rows())
    "A blonde, barefoot, a glass of wine in her hand. She looks at the dark spot on the front of your shorts and laughs."
    fs_cust "\"Is that the sample?\""
    fs_you "\"It's display stock. It doesn't do anything. It's not part of the—\""
    fs_cust "\"Let's see.\""
    show cg fs_door3_mat onlayer cgl
    "She puts the wine down, kneels on her doormat, hooks your shorts down before you can step back, and swallows your small cock whole. Balls and all. Her nose in your smooth belly."
    show fs_pc protesting
    fs_you "\"Hey— that's not— {i}ohhh{/i}— oh, that's— that's the whole— {i}mmh{/i}—!\""
    "Then she looks up at you, with all of you in her mouth, and her eyes are laughing, and your hands go into her hair to pull her off and end up holding her on."
    show fs_pc flushed
    "She sucks, slow and lazy, her tongue rolling the whole of you round her mouth like a sweet. Her hands come up and take two big handfuls of your ass and pull you forward onto her face, and your thighs fold round her shoulders, soft and heavy."
    fs_you "\"{i}Mmh{/i}— customer's— {i}ahh{/i}— handling the stock— the whole— the {i}whole{/i} stock—\""
    fs_deb "\"Are you narrating again?\""
    fs_you "\"She {i}asked{/i} for the product— {i}hhn{/i}— talk-through—!\""
    "She didn't. She just pops off for a breath, laughing, your small cock bobbing wet and pink in front of her nose."
    fs_cust "\"Keep talking, though.\""
    "She swallows it again, and hums. It's the best thing you've ever felt on your cock, and it lasts about as long as you'd expect."
    "You come in her mouth with your thighs shaking and your hands in her hair, babbling about the soft-touch range, and she swallows and pulls off and wipes her lip." with vnfx("flash")
    fs_cust "\"Doesn't do anything.\""
    "She agrees, and rates you, and shuts the door."
    $ fs.doors = 3
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. You'll know it.\"\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(40)
    jump fs_door_four

label fs_door_four:
    $ vn_enter(bg="fs_clive_hall", pc="neutral", pc_tag="fs_pc", cast=[("fs_clive", "grumbling")], cg=None)
    show bg fs_clive_hall onlayer bgl
    show fs_clive grumbling at vn_cast_slot
    show screen fs_manifest(fs_manifest_rows())
    "Clive. In his cardigan. With a box."
    fs_you "\"There's no box. It's Ambassador. There's no stock.\""
    fs_clive "\"Then what am I returning?\""
    "He looks at you, all of you, and then at the name on your seat."
    fs_clive "\"Hm. The label's crooked.\""
    show fs_pc protesting
    fs_you "\"It isn't. And you can't return me {i}twice{/i}, Clive, I'm not—\""
    hide fs_clive
    show cg fs_door4_pile onlayer cgl
    "He takes you by the back of the neck, same as yesterday, and bends you over his returns pile. The same heap, every bag back in it, reordered."
    "Your ass goes up and up, and up, and Clive stands behind it for a long moment and says nothing at all, which is the most anyone's ever heard him say."
    fs_clive "\"The waistband's sitting fine. Why is the waistband sitting {i}fine{/i}.\""
    "He sounds personally betrayed."
    fs_you "\"Made to order. So you can let go of my—\""
    fs_clive "\"Hm.\""
    "He hooks a finger in it and peels the PRENTICE cut down just far enough, and lines himself up, and pushes in, and complains about the stitching on every stroke."
    fs_clive "\"Crooked. {i}Crooked.{/i} One star for the stitching.\""
    fs_you "\"Clive— Clive, it's {i}straight{/i}— {i}ahh{/i}—\""
    show fs_pc flushed
    "And it's yesterday's angle, and your ass already knows it, and it rolls back onto him before you've finished the sentence."
    fs_you "\"{i}Ahh{/i}— oh, Clive— you came {i}back{/i} for it— you {i}ordered{/i} me—!\""
    vn_sfx "Slap. Slap."
    fs_clive "\"I ordered a {i}replacement{/i}. For the shorts. Which were inadequate. This is also inadequate. This is {i}far{/i} too much seat for one garment.\""
    fs_you "\"{i}Ahh{/i}— it's straight— it's {i}straight{/i}— rate the {i}delivery{/i}—!\""
    fs_deb "\"Customer reports: stitching.\""
    "She's laughing. You can hear it."
    fs_deb "\"Noted.\""
    fs_you "\"{i}Hhn{/i}— you're {i}laughing{/i}—\""
    fs_deb "\"I'm noting.\""
    "He comes across your ass, over your name, and wipes it with a return." with vnfx("flash")
    fs_clive "\"Four stars. Delivery's fine. It's the fabric.\""
    $ fs.doors = 4
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. Kestrel Court.\"\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(50)
    jump fs_door_five

label fs_door_five:
    $ vn_enter(bg="fs_kestrel", pc="neutral", pc_tag="fs_pc", cast=[("fs_kieran", "talking"), ("fs_ade", "grin"), ("fs_rich", "grin")], cg="fs_door5_carpet")
    show screen fs_manifest(fs_manifest_rows())
    "Kestrel Court, the middle of the night, every light on. All three in the hall."
    fs_kieran "\"It's him—\" \"It's the Ambassador—\" \"Did you book him?\" \"I booked him—\" \"I booked him {i}first{/i}—\""
    show fs_pc protesting
    fs_you "\"One at a {i}time{/i}— wait— Ambassador's a {i}representative{/i}—\""
    show cg fs_door5_carpet onlayer cgl
    "They've got you down on their carpet before the door's shut, knees and elbows, Ade's hand flat on your back. Kieran first, gabbling, fast and eager, his hands lost in your ass." with vnfx("shake")
    fs_kieran "\"It's {i}bigger{/i}— it's bigger than last {i}time{/i}—\" \"It was {i}yesterday{/i}—\" \"It's bigger than whenever it {i}was{/i}—\""
    show fs_pc flushed
    fs_you "\"It's a— {i}ahh{/i}— representative— oh— oh, {i}fine{/i}— Ambassador— Ambassador {i}range{/i}— {i}keep going{/i}—!\""
    "Then Ade, slow, his big hands round your waist again, checking the fit."
    fs_ade "\"Fits better than the shorts did.\""
    "To Rich, like you're not there, and you moan your thanks into the carpet."
    "They're quicker tonight. They know where everything is. Ade comes in you and pulls out and Rich slides in after him, slow and heavy."
    show cg fs_door5_mail onlayer cgl
    vn_sfx "Bzzt."
    "And your phone buzzes on the floor under your face. An email. From Vellum. A reply, at last, to three polite complaints and a spreadsheet."
    fs_you "\"{i}Deb{/i}— Deb, they {i}replied{/i}— they finally—\""
    fs_deb "\"Read it.\""
    $ fs_mail_lines = ["{b}From: Vellum{/b}", "{i}Thank you for your email. I am currently out of the office with no access to email. I will respond on my return.{/i}"]
    show screen fs_mail(fs_mail_lines)
    "You read it out to the whole channel with Rich still in you."
    fs_rich "\"Is that it?\" \"That's it?\" \"That's an out-of-office—\" \"That's {i}definitely{/i} an out-of-office—\""
    hide screen fs_mail
    fs_you "\"Oh— {i}oh{/i}— it's an out-of-office— {i}ahh{/i}— Rich, {i}harder{/i}—!\""
    fs_deb "\"Complaints closed. Logged.\""
    "Rich comes in you. Kieran and Ade finish down the back of your neck and over your bob, still arguing about whose booking it was." with vnfx("flash")
    $ fs.doors = 5
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. Bring the thighs.\""
    "Deb has stopped being professional some time ago.\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(50)
    jump fs_door_six

label fs_door_six:
    $ vn_enter(bg="fs_armchair_room", pc="neutral", pc_tag="fs_pc", cast=[], cg="fs_door6_arm")
    show bg fs_armchair_room onlayer bgl
    show screen fs_manifest(fs_manifest_rows())
    "A broad man with a shaved head and a phone already in his hand. He's read the account notes."
    fs_cust "\"Says here: best thighjob in company history.\""
    show fs_pc protesting
    fs_you "\"That's— that was a {i}review{/i}, it's not a {i}service{/i}, Ambassador doesn't—\""
    show cg fs_door6_arm onlayer cgl
    "He turns you round by the shoulders and walks you into his front room and bends you over the arm of his armchair, one big hand on your back." with vnfx("shake")
    fs_cust "\"Prentice.\""
    "He reads your seat out loud. Then he puts his other palm flat on the backs of your thighs and pushes, and watches the softness give and roll back."
    fs_cust "\"Huh. Plush.\""
    fs_you "\"Plush {i}cut{/i}— it's the name of the {i}shorts{/i}— let me {i}up{/i}—\""
    fs_cust "\"I know what it's called, I've read the reviews. Company history. Let's see it.\""
    "You hear his belt. He's out of his trousers and pushing his cock into the soft squeeze between your thighs while you're still talking, and there's no gap at all, from the top of them to your knees, and he just shoves through."
    fs_you "\"Hey— {i}hey{/i}— that's not— {i}ahh{/i}—\""
    "He groans so loud the neighbours bang on the wall."
    fs_deb "\"Customer's rating as he goes.\""
    fs_cust "\"One star for the wait. Two. Three— {i}Christ{/i}—\""
    menu:
        "He's between your thighs, rating as he goes."
        "Clamp your knees together":
            $ fs.door6 = "knees"
        "\"It says AMBASSADOR, not—\"":
            $ fs.door6 = "protest"
        "Push up off the armchair":
            $ fs.door6 = "push"
    jump fs_door_six_sex

label fs_door_six_after:
    $ vn_enter(bg="fs_armchair_room", pc="flushed", pc_tag="fs_pc", cast=[], cg="fs_door6_cum")
    show screen fs_manifest(fs_manifest_rows())
    "And then you're the one doing it. You turn your head on the armchair and look back at him over your shoulder and squeeze, on purpose, from the top of your thighs to your knees, and offer him the lot."
    fs_you "\"Company history. Go {i}on{/i}, then. Rate it.\""
    show cg fs_door6_cum onlayer cgl
    "He comes between your thighs, shouting \"{i}Five!{/i}\", hot and thick, all the way down to your knees." with vnfx("flash")
    fs_cust "\"Five. Best in company history. Confirmed.\""
    "He types it in. You stay bent over his armchair for a moment, thighs glazed and shaking, your small cock dripping a thin string onto his rug, panting your own review back to him."
    fs_you "\"Plush— cut— thank you for— {i}choosing{/i}— Vellum—\""
    "He pats your ass twice, like a van he's just bought."
    $ fs.doors = 6
    show screen fs_manifest(fs_manifest_rows())
    fs_deb "\"Next address. Off Harvest Street.\"\n{size=-5}{color=#ff8fa3}▸ The next address{/color}{/size}"
    $ vn_pass(40)
    jump fs_door_seven

label fs_door_seven:
    $ vn_enter(bg="fs_bedroom_cust", pc="neutral", pc_tag="fs_pc", cast=[], cg="fs_door7_bed")
    show bg fs_bedroom_cust onlayer bgl
    show screen fs_manifest(fs_manifest_rows())
    "A brunette in a big T-shirt and nothing else, sleepy-eyed, who opens the door and says \"Oh, {i}thank{/i} God,\" and pulls you in by the waistband."
    "She stops in her hallway and just looks at you: the bob, the gloss, the puffy points in your polo, the thighs. She puts both hands flat on them and squeezes, and her eyes go wide."
    fs_cust "\"Are they {i}real{/i}?\""
    show fs_pc protesting
    fs_you "\"They're— yes— I'm only meant to be {i}representing{/i} the—\""
    show cg fs_door7_bed onlayer cgl
    "She doesn't hear the end of it. She tows you to her bed by the waistband and pushes you down on your back and straddles your thick thigh and rides it, grinding wet and hot along it, while she works slick fingers into your ass and her other hand round your small cock."
    fs_you "\"Hey— hey, that's— {i}ohh{/i}—\""
    show fs_pc flushed
    "Her fingers curl, and the end of the sentence goes somewhere else."
    fs_you "\"...Plush cut. Ask for it— {i}ahh{/i}— by {i}name{/i}—\""
    fs_cust "\"Oh my God, it's so {i}soft{/i}. It's like riding a {i}pillow{/i}. It's like a {i}sofa{/i}. Why is it so {i}soft{/i}—\""
    fs_you "\"Soft-touch— {i}ahh{/i}— soft-touch {i}range{/i}— it's in the— {i}mmh{/i}— the {i}name{/i}—\""
    "Her fingers curl again. You arch right off the bed, your whole huge ass lifting her with it, and she squeals and grinds harder."
    fs_cust "\"Does this— {i}ah{/i}— does this do anything?\""
    "She's squeezing your cock."
    fs_you "\"Nothing at all— {i}ahh{/i}— it's purely decorative—!\""
    fs_cust "\"Good.\""
    "She fingers you harder, and grinds harder, and comes on your thigh with a squeal, and makes you come all over your own belly with her fingers curled up inside you." with vnfx("flash")
    "She rates you lying on her back, laughing, and falls asleep before you've found your shorts."
    $ fs.doors = 7
    show screen fs_manifest(fs_manifest_rows())
    "In your ear, Deb reads the last address on the manifest. You've never been sent there before. It's a little rowhouse at the end of a street off the docks."
    fs_you "\"Whose is it?\""
    fs_deb "\"Last drop. Go.\"\n{size=-5}{color=#ff8fa3}▸ The last address{/color}{/size}"
    $ vn_pass(30)
    jump fs_deb_door

## ---- the last door: Deb (Vellum Six Deb). Non-con, flips on "Next tier: none." -------------------

label fs_deb_door:
    $ vn_enter(bg="fs_deb_kitchen", pc="neutral", pc_tag="fs_pc", cast=[("fs_deb", "bored")], cg=None)
    show bg fs_deb_kitchen onlayer bgl
    show screen fs_manifest(fs_manifest_rows())
    "You knock."
    fs_deb "\"Door's open.\""
    "And then, half a beat later, through the door:"
    fs_debx "\"Door's open.\""
    "You stop with your hand on the handle."
    hide screen fs_manifest
    show fs_deb bored at vn_cast_slot
    show cg fs_deb_reveal onlayer cgl
    "She's in her kitchen. Dark hair scraped back, a headset on, the mic at her mouth, a laptop open on the counter showing the dispatch board with one van left on it. Yours."
    "She's a woman you've never seen in your life, and you've had her voice in your ear every hour of every day for a week."
    fs_debx "\"Hi.\""
    "Into the mic. Then out loud."
    fs_debx "\"Hi.\""
    fs_you "\"{i}Deb?{/i}\""
    fs_debx "\"You're late.\" \"You're late.\" \"Counter.\""
    "She's wearing a harness: a thick black strap-on, standing out from her hips, glistening. She's been ready a while."
    fs_you "\"You were on the manifest the whole time. The {i}whole time{/i}. Every complaint I made— you {i}logged{/i} them, and you were—\""
    fs_debx "\"Since it was cut. Counter, Prentice.\""
    fs_you "\"Did you {i}listen{/i}? All week? While they—\""
    fs_debx "\"Prentice. I've had my hand in my knickers since the fit check. Counter.\""
    "In your ear and out loud, twice. You stare at her. At the mic. At the screen with your van on it, the only dot left on the board. At the second chair pulled up to the counter with a spare headset on it and a mug gone cold."
    fs_you "\"You routed it. The whole manifest. You put yourself {i}last{/i}.\""
    fs_debx "\"Optimal route. You'd know. You've got a spreadsheet.\""
    show fs_pc protesting
    fs_you "\"Deb, I'm not— I'm not doing a {i}last drop{/i}, I want to talk about the—\""
    fs_debx "\"It's routing. Counter, Prentice. I'm not saying it a third time.\""
    hide fs_deb
    show cg fs_deb_counter onlayer cgl
    "She doesn't. She comes round the counter, puts her hand flat between your shoulder blades and bends you over it." with vnfx("shake")
    "Your huge ass up, your PRENTICE cut round your thighs where she pushes it, your name on the seat right in front of her. Her voice in your ear and then over your shoulder, a half-beat apart, both at once."
    fs_debx "\"Ambassador.\" \"Ambassador.\""
    fs_you "\"Deb— {i}Deb{/i}, wait, I've got {i}questions{/i}—\""
    fs_debx "\"Logged.\" \"Logged.\""
    "She pushes in. All the way. Your mouth falls open on the counter."
    fs_you "\"{i}AHHH{/i}— Deb— it's {i}you{/i}— it's {i}actually{/i} you— {i}wait{/i}—!\""
    fs_debx "\"It's actually me.\" \"It's actually me.\""
    menu:
        "She's in you, bent over her counter. Her voice in your ear and over your shoulder."
        "Grip the counter edge":
            $ fs.counter = "grip"
        "\"Deb, I'm asking you QUESTIONS—\"":
            $ fs.counter = "questions"
        "Grab for the headset":
            $ fs.counter = "headset"
    jump fs_deb_sex

## ---- THE ENDING, "Ambassador" (Vellum Ambassador) --------------------------------------------------

label fs_ambassador:
    $ vn_enter(bg="fs_deb_kitchen", pc="flushed", pc_tag="fs_pc", cast=[], cg="fs_deb_dash")
    show cg fs_deb_dash onlayer cgl
    if fs.counter == "headset":
        "You'd got two fingers on her headset before she took your wrist and put your hand flat on the counter next to the laptop, and left hers on top of it."
    "She reaches past your head and turns the laptop so you can see it. Your dashboard. Full screen."
    show screen fs_dash(6)
    "And she reads it. All of it. In your ear and over your shoulder, every line twice, a thrust on each."
    fs_debx "\"{i}VELLUM DRIVER, T. PRENTICE.{/i}\" \"{i}VELLUM DRIVER, T. PRENTICE.{/i}\""
    fs_debx "\"{i}Tier, Ambassador.{/i}\" \"{i}Tier, Ambassador.{/i}\""
    fs_debx "\"{i}Rating.{/i} Five full stars.\" \"Five full stars.\""
    "She leans on you."
    fs_debx "\"{i}Route bonus. Applied overnight.{/i}\" \"{i}Applied overnight.{/i}\""
    fs_debx "\"{i}Chest.{/i}\""
    "Her hand slides up under your polo and finds your puffy nipple and pinches it, and you scream."
    fs_debx "\"{i}Within spec. No adjustment required.{/i}\" \"{i}No adjustment required.{/i}\""
    fs_debx "\"{i}Next tier.{/i}\""
    "She drives in to the hilt and holds it there."
    fs_debx "\"{i}None.{/i}\" \"{i}None.{/i}\""
    hide screen fs_dash
    show cg fs_deb_cum onlayer cgl
    "You come so hard you see stars. All five. Your small cock spurts uselessly against her cabinet door and your ass clamps on her and your new light voice cracks right through the kitchen ceiling, and she keeps going through it." with vnfx("flash")
    fs_deb "\"Five stars, no notes.\""
    fs_debx "\"Five stars, no notes.\""
    "In your ear, and then the same again, right against it, out loud."
    show cg fs_deb_standing onlayer cgl
    "She doesn't stop. She hauls you up off the counter by the hips and fucks you standing, your back to her front, her hand flat on your belly holding you on, her mouth at your ear, the mic at your ear, her voice in both."
    "Your thighs shake. Your small cock bobs and drips, useless, untouched, and she doesn't so much as glance at it."
    fs_debx "\"Every drop this week.\" \"Every drop this week.\" \"I heard every one.\" \"I heard every one.\""
    fs_you "\"{i}Ahh{/i}— Deb— you {i}heard{/i}— {i}ahh{/i}— all of it—\""
    vn_sfx "Slap. Slap. Slap."
    fs_debx "\"All of it.\" \"All of it.\" \"The deck. The rug. The platform. The carpet. The pallet.\""
    "Twice. Twice. Twice. She pulls your bob back in her fist so your mouth is by her mic."
    fs_debx "\"That's the last drop.\" \"That's the last drop.\" \"Now beg for tomorrow's.\" \"Now beg for tomorrow's.\""
    fs_you "\"{i}Please{/i}— Deb— put me— on tomorrow's— {i}ahh{/i}—!\""
    fs_debx "\"Every night.\" \"{i}Every night.{/i}\" \"On this counter, with your name on your arse, until the app runs out of stars.\" \"Until the app runs out of stars.\""
    $ fs.ending = "ambassador"
    $ achievement.grant("Five Stars, No Notes")
    hide cg onlayer cgl
    "You don't remember the drive back. You remember the stars, and her voice in your ear the whole way, saying nothing at all, just breathing.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(5)
    jump fs_epilogue

## ---- DAY 7, the epilogue (Vellum Epilogue, Epilogue Stay, Epilogue Go) ---------------------------

label fs_epilogue:
    $ fs.fit = "prentice"
    $ vn_enter(bg="fs_vanbay", pc="flushed", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg="fs_epi_yard")
    show cg fs_epi_yard onlayer cgl
    "The yard, before six. Grey sky over the water, the roller door going up, your van in its bay with nothing in the back."
    "You're in your PRENTICE cut with a coffee, walking very carefully, still full of last night. Your earpiece clicks."
    fs_deb "\"Dispatch, go ahead.\""
    "Deb. Bored. Crisp. Exactly like the first morning, like you weren't bent over her counter a few hours ago with her reading your chest line into both your ears."
    fs_you "\"Morning, Deb.\""
    fs_deb "\"Morning. You've a manifest tonight if you want it.\""
    fs_you "\"Deb. Last night. Your {i}counter{/i}—\""
    fs_deb "\"Your first window's after dark. Seat all the way back. Kit's in the van.\""
    fs_you "\"You read my {i}chest line{/i} into my {i}ear{/i}—\""
    fs_deb "\"And I'll read it again tonight if you're on the manifest.\""
    "A pause exactly as long as it needs to be."
    fs_deb "\"Are you on the manifest?\""
    hide cg onlayer cgl
    show bg fs_pickface onlayer bgl
    show fs_regan flat at vn_cast_slot
    "Regan's at the pick face. She doesn't look up. She drops a fresh PRENTICE cut on the rail, folded, and writes something on the pick list."
    "You lean over to read it. {i}PRENTICE — standing order.{/i} Underlined once."
    hide fs_regan
    show cg fs_epi_drivers onlayer cgl
    "The other drivers are drifting in with their hoods up, same as the first morning. They stop when they see you."
    "One of them, the one who laughed at you reading the terms, looks at your thighs, and your bob, and the name on your seat, and opens the app on his phone, and starts scrolling. Slowly. From the top."
    menu:
        "Deb's waiting. So's the van."
        "\"Put me down for it.\"" (ending=True):
            jump fs_epilogue_stay
        "Hand in the van keys" (ending=True):
            jump fs_epilogue_go

label fs_epilogue_stay:
    $ fs.epilogue = "stay"
    $ vn_enter(bg="fs_doorstep", pc="flushed", pc_tag="fs_pc", cast=[], cg="fs_epi_stay")
    fs_you "\"Put me down for it.\""
    fs_deb "\"Already did.\""
    $ vn_until(22)
    show cg fs_epi_stay onlayer cgl
    "That night the van's empty again, and the manifest lights up with one address, and you drive it with the seat all the way back and your thighs spilling over both sides of it, singing."
    "A man in a dressing gown opens the door. He looks at your thighs. He looks at the name on your seat when you turn round."
    fs_cust "\"Oh. You're the {i}Ambassador{/i}.\""
    fs_you "\"Vellum Ambassador. Plush cut. Ask for it by name.\""
    "You bend over his hall table, and push your shorts down."
    show cg fs_epi_stay_hall onlayer cgl
    "He's in you before the door's shut behind you, the hall table rattling, your hands on the wall, his dressing gown open and his belly slapping your ass. Your name's printed on the seat of the shorts round your thighs, and he's reading it out loud."
    fs_cust "\"Pren— {i}tice{/i}— Pren— {i}tice{/i}—\""
    fs_you "\"Ask for it— {i}ahh{/i}— ask for it by {i}name{/i}—!\""
    "He asks for it by name. Loudly. Every stroke. You moan the range back at him item by item, and Deb reads his rating into your ear before he's even finished."
    "When he comes in you, you're already asking her for the next address." with vnfx("flash")
    "The fifth star stays full. It always does now.\n{size=-5}{color=#ff8fa3}▸ Out onto the docks{/color}{/size}"
    jump fs_route_return

label fs_epilogue_go:
    $ fs.epilogue = "go"
    $ vn_enter(bg="fs_pickface", pc="neutral", pc_tag="fs_pc", cast=[("fs_regan", "flat")], cg=None)
    show bg fs_pickface onlayer bgl
    show fs_regan flat at vn_cast_slot
    "You put the van keys on the rail by Regan's clipboard."
    "She looks at them. She doesn't look at you."
    fs_regan "\"Shorts.\""
    fs_you "\"I'm keeping the shorts.\""
    fs_regan "\"Fine. They're your size. Nobody else's.\""
    "She writes something on the pick list."
    fs_deb "\"Logged.\""
    "And then, before she cuts the channel, just once:"
    fs_deb "\"Five stars.\""
    hide fs_regan
    show bg fs_vanbay onlayer bgl
    show fs_jodie grin at vn_cast_slot
    "On your way out Jodie's at the roller door with a coffee for you, because of course she is."
    fs_jodie "\"I heard. Five stars for quitting. I'm still ordering. You'll have to come and model it anyway.\""
    fs_you "\"Is that in the terms?\""
    fs_jodie "\"It's in {i}my{/i} terms.\""
    hide fs_jodie
    show cg fs_epi_go onlayer cgl
    "You walk out of the van bay onto the docks in your PRENTICE cut with your hips swinging and your bob in your eyes, and every docker on the quay stops to watch you go, and you wave at all of them."
    $ vn_until(23)
    show cg fs_epi_go_night onlayer cgl
    "That night your phone buzzes on the pillow. You don't even have the app open."
    "{color=#e8b923}Route bonus: applied overnight.{/color}"
    "You lie there and wait for something to happen. Nothing moves. Nothing needs to. You fall asleep with both hands full of your own ass, grinning.\n{size=-5}{color=#ff8fa3}▸ Out onto the docks{/color}{/size}"
    jump fs_route_return
