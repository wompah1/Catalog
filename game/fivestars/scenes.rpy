## fivestars' director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, your climax (its own
## frame), then the passage after. The lines come from fivestars.js's pools (setup.slCombatLines,
## setup.slPcLines.fivestars): the leads' taking lines and Toby's protest, betray and break before
## a flip; the act lines and the courier patter after it. Deb is in every one, in your ear.
## The non-con pass (route.rpy header): rungs 1-2 never flip; the fit check flips on "Fit check
## passed". Nothing in your ass on day one; your small cock goes inside nobody, ever.

## Rung 1, the deck again: her cock in your mouth, her fist on yours. Optional; non-con, no flip.
## (days-early.twee :: Vellum One Deck Sex; lead Regan, opener oral, anal denied)
label fs_deck_sex:
    $ vn_enter(bg="fs_deck", pc="protesting", pc_tag="fs_pc", cg="fs_deck_sex_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_deck_sex_open onlayer cgl
    if fs.deck == "pallet":
        "You grab the pallet edge to haul yourself back. Her fist in your hair doesn't move, and the pallet comes a little way with you, and that's all."
    elif fs.deck == "clock":
        fs_you "\"I'm OFF the clock, Regan— the shift's {i}over{/i}— the tier doesn't—\""
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Complaint noted. Open.\""
    else:
        "You shove at her thighs with both hands. She moves them to the base of her cock, one and then the other."
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Use it.\""
    "Her fist in your collar keeps your head exactly where she wants it, and she feeds it back in."
    fs_you "\"{i}Mmf{/i}— I read the terms— I {i}READ{/i} them— it doesn't {i}SAY{/i} this—\""
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Spit. More.\""
    "Her fist pumps your small cock in time, whatever you're trying to say round her."
    show cg fs_deck_sex_mid onlayer cgl
    fs_deb "\"Complaint noted.\" Keys clicking. \"Logged.\""
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Throat.\""
    "Her hand goes flat on the back of your head."
    show fs_regan flat at vn_cast_slot
    fs_regan "\"That's spec.\""
    vn_sfx "Glk. Glk. Glk."
    fs_you "\"{i}Glk{/i}— that noise isn't a {i}REVIEW{/i}— don't {i}RATE{/i} that— {i}mmf{/i}—\""
    fs_deb "\"Rating's live. It's going up, if you were wondering. Logged.\""
    vn_th "(Why's it going UP. Stop going UP.)"
    show cg fs_deck_sex_peak onlayer cgl
    "Your hips buck into her fist. Your jaw finds the angle again on its own, wider, and your throat lets her in, and the noise you make rings off the roller door."
    fs_you "\"{i}Mmhh{/i}— fine— {i}fine{/i}— log it, log {i}all{/i} of it— {i}glk{/i}—\"" with vnfx("shake")
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Hold that.\""
    show cg fs_deck_sex_cum onlayer cgl
    "You come in her fist, shouting the tier name round her cock, and she comes a beat after, straight down your throat, holding you there." with vnfx("flash")
    $ fs_enc.pc_orgasms = 1
    $ fs_enc.partner_came = True
    jump fs_deck_after

## Rung 2, Jodie again: her pink strap-on, on your back on her rug, already in. Optional; non-con,
## no flip. (days-early.twee :: Vellum Two Jodie Sex; lead Jodie, strap-on, missionary, inside)
label fs_jodie_sex:
    $ vn_enter(bg="fs_jodie_room", pc="protesting", pc_tag="fs_pc", cg="fs_jodie_sex_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_jodie_sex_open onlayer cgl
    if fs.rug == "rug":
        "You grab fistfuls of her rug to drag yourself out from under her. It comes with you. So does she."
    elif fs.rug == "clause":
        fs_you "\"Jodie, the clause says {i}PARCEL{/i}— it says the {i}PARCEL{/i}—\""
        show fs_jodie grin at vn_cast_slot
        fs_jodie "\"Hand to customer. I'm the customer. This is my hand.\""
        "It's round your cock."
    else:
        "You kick at the sofa to push off. She catches the backs of your knees and pins them back again."
        show fs_jodie grin at vn_cast_slot
        fs_jodie "\"Customer's allowed. Says so right there.\""
    "The strap goes back in to the base."
    show fs_jodie grin at vn_cast_slot
    fs_jodie "\"I tipped, Toby. Tip's in the terms.\""
    vn_sfx "Slap. Slap."
    show cg fs_jodie_sex_mid onlayer cgl
    fs_you "\"That's NOT what hand-to-customer— it means the {i}PARCEL{/i}— the clause says {i}PARCEL{/i}— {i}hnngh{/i}—!\""
    show fs_jodie grin at vn_cast_slot
    fs_jodie "\"One star for wriggling. Five for the noise. Keep wriggling.\""
    fs_deb "\"That's a clause query. I'll log it as a clause query.\""
    "Your small cock's dripping on your belly while you yell the clause at her, and the stars keep landing."
    fs_you "\"I'm not pushing {i}BACK{/i}— I'm {i}not{/i}— that's not in the— {i}ohh{/i}—\""
    show fs_jodie grin at vn_cast_slot
    fs_jodie "\"Four stars for the protest. It's {i}very{/i} convincing.\""
    vn_sfx "Slap."
    show cg fs_jodie_sex_peak onlayer cgl
    "She fucks you harder, her fist in time, and the thing inside you that gave way before gives way again."
    fs_you "\"Please— {i}please{/i}— whatever the clause says, I'm {i}IN{/i} it— {i}AHH{/i}—!\"" with vnfx("shake")
    show cg fs_jodie_sex_cum onlayer cgl
    "You come all over your own belly, screaming the clause and then screaming her a five." with vnfx("flash")
    $ fs_enc.pc_orgasms = 1
    jump fs_jodie_after

## Rung 3, THE FIT CHECK: Regan in you on the scanner platform. MANDATORY; non-con, flips on the
## scanner's "Fit check passed". (days-early.twee :: Vellum Three Platform Sex; lead Regan, anal,
## doggy, lock, inside; Jodie's mouth comes after the flip, in fs_platform_after)
label fs_platform_sex:
    $ vn_enter(bg="fs_fitroom", pc="protesting", pc_tag="fs_pc", cg="fs_platform_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_platform_open onlayer cgl
    if fs.fit_choice == "stop":
        "You get one hand off the rail and stretch for the red stop button on the arch. Your fingertips are on its edge when she catches your wrist, and puts your hand back on the rail, and keeps it there under hers."
    elif fs.fit_choice == "protest":
        fs_you "\"That is NOT a fit check— that's NOT a fit check— it says {i}SCANNED{/i}—\""
    else:
        "Your knuckles go white on the rail. You hang on to it like it's the clause."
    "She pushes in. The fat head of her opens you wider than Jodie's toy ever did, and keeps going, and keeps {i}going{/i}, so big and so full you can't do anything but hang on the rail with your mouth open." with vnfx("shake")
    $ _fs_s = fs_scan("Seat")
    fs_scanner "[_fs_s]"
    fs_you "\"{i}AHHH{/i}— she's {i}in{/i}— she's IN— Deb— {i}DEB{/i}— that's NOT a fit check—!\""
    fs_deb "\"Yes. We can all hear that. Logged.\""
    show fs_jodie grin at vn_cast_slot
    fs_jodie "\"Five stars. Customer's allowed to watch.\""
    "She hasn't moved off her stool. Both hands round her coffee."
    show cg fs_platform_mid onlayer cgl
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Hold still. Stock doesn't negotiate.\""
    "Her hands lock on your hips and haul you back onto her."
    vn_sfx "Slap. Slap. Slap."
    fs_you "\"I'm the {i}DRIVER{/i}— I deliver the {i}STOCK{/i}— I'm not the— {i}ah{/i}— not the {i}STOCK{/i}—!\""
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Clause says fit. This is the fit. Open.\""
    $ _fs_s = fs_scan("Thigh")
    fs_scanner "Blue light down your thighs, under her hands. [_fs_s]"
    fs_deb "\"Objection logged. Window's still open.\""
    fs_you "\"Why am I {i}HARD{/i}— it's the shorts— it's the {i}shorts{/i}— {i}hhnn{/i}— get off—!\""
    "Your hips are pushing back onto her on their own, and you're yelling at them to stop it."
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Volume, not depth.\""
    "She gives you depth anyway, all of it, while you yell the section number at her."
    $ _fs_a, _fs_c = fs_scan("Seat"), fs_scan("Chest", False)
    fs_scanner "Another pass. [_fs_a] [_fs_c]"
    "Nobody looks up."
    show cg fs_platform_peak onlayer cgl
    "Every stroke drags the clause out of you longer and higher, and every stroke hits that place, and something's coming loose."
    fs_you "\"Rate it— just {i}RATE{/i} it— five, make it {i}FIVE{/i}, I'll sign for {i}ANYTHING{/i}—!\"" with vnfx("shake")
    vn_sfx "Ding."
    "The screen on the wall goes green."
    fs_scanner "{b}“Fit check passed.”{/b}"
    "And something in you just lets go."
    show fs_pc flushed
    fs_you "\"...Passed. I {i}passed{/i}. Window met— window {i}MET{/i}— Regan, {i}HARDER{/i}—!\""
    "You shove back onto her."
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Seat's taking it. Log it.\""
    "She drives in to the root and stays there."
    show cg fs_platform_cum onlayer cgl
    "She comes in you on the platform, deep, so much and so hot you feel it fill you up, and the scanner sweeps over you while she does." with vnfx("flash")
    $ fs_enc.partner_came = True
    jump fs_platform_after

## Rung 4, Kestrel Court again: all three, one at a time, face-down on the carpet. Optional;
## non-con, flips on the third turn. No DP. (days-late.twee :: Vellum Four Kestrel Sex; lead Kieran,
## crew Ade and Rich, anal, doggy, doubleanal denied)
label fs_kestrel_sex:
    $ vn_enter(bg="fs_kestrel", pc="protesting", pc_tag="fs_pc", cg="fs_kestrel_sex_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_kestrel_sex_open onlayer cgl
    if fs.carpet == "claw":
        "You claw at the carpet to drag yourself out from under Rich. You get about as far as the rug's edge."
    elif fs.carpet == "item":
        fs_you "\"It said every {i}ITEM{/i}— every {i}ITEM{/i}— I'm not an {i}ITEM{/i}—\""
    else:
        "You crawl for the coffee table, on your elbows, with Rich still in you."
        show fs_ade grin at vn_cast_slot
        fs_ade "\"Grab his ankle, he's crawling—\""
    show fs_kieran grin at vn_cast_slot
    fs_kieran "\"Says in-home, mate. We paid for in-home.\""
    "Kieran holds your hips down on the carpet and keeps going, and Ade's hand goes flat on your back."
    show cg fs_kestrel_sex_mid onlayer cgl
    show fs_rich grin at vn_cast_slot
    fs_rich "\"Is this the certification bit? He says it isn't.\""
    show fs_ade grin at vn_cast_slot
    fs_ade "\"He would say that, he's staff—\""
    fs_you "\"Please— it says {i}ITEMS{/i}— every {i}ITEM{/i}— I'm not an {i}ITEM{/i}— {i}please{/i}—\""
    show fs_kieran grin at vn_cast_slot
    fs_kieran "\"Did you sign for it? He has to sign for it.\" \"He's saying no.\" \"Is no a signature?\""
    "Nobody stops to check."
    fs_deb "\"Dispatch can't action that.\""
    vn_sfx "Slap. Slap. Slap."
    "All three talking at once, nobody listening to a word you say, one after another in you."
    show cg fs_kestrel_sex_peak onlayer cgl
    "By the third of them your hips are rolling back on their own, and the carpet's wet under your small cock, and you stop fighting it."
    show fs_pc flushed
    fs_you "\"...Okay. {i}OKAY{/i}. Signed for— {i}signed for{/i}— keep it {i}COMING{/i}— certify it— certify it {i}again{/i}—!\"" with vnfx("shake")
    show fs_rich grin at vn_cast_slot
    fs_rich "\"He {i}is{/i} signing for it, listen to him—\""
    show cg fs_kestrel_sex_cum onlayer cgl
    "They finish one after another, all three talking the whole time, and you come on the carpet under them, untouched, moaning the review back to them." with vnfx("flash")
    $ fs_enc.pc_orgasms = 1
    $ fs_enc.partner_came = True
    jump fs_kestrel_after

## Rung 5, the pallet again: Regan, already in. Optional; non-con, flips on the second turn. Her
## pallet lines, not the scanner's. (days-late.twee :: Vellum Five Pallet Sex; anal, doggy, inside)
label fs_pallet_sex:
    $ vn_enter(bg="fs_pickface", pc="protesting", pc_tag="fs_pc", cg="fs_pallet_sex_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_pallet_sex_open onlayer cgl
    if fs.pallet == "brace":
        "You brace both hands on the shrink-wrap to push yourself up."
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Brace on the shrink-wrap. Stock doesn't move.\""
        "She hauls your hips back onto her."
    elif fs.pallet == "staff":
        fs_you "\"I'm {i}STAFF{/i}, Regan— staff aren't in the catalogue— I'm on the {i}rota{/i}—\""
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Complaint's logged.\""
        "She writes it down with one hand."
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Wider.\""
    else:
        "You twist half off the pallet. She puts you back on it by the split waistband without looking up."
        show fs_regan flat at vn_cast_slot
        fs_regan "\"Hold that.\""
    "She's back in you before you've finished, all of her."
    vn_sfx "Slap. Slap."
    show cg fs_pallet_sex_mid onlayer cgl
    fs_you "\"That's a {i}misreading{/i}— that's a {i}MISREADING{/i} of the clause— let {i}go{/i}—!\""
    fs_deb "\"Objection logged. Window's still open.\""
    "The pallet creaks. Somewhere in the pick face a scanner beeps at nothing."
    "And your ass rolls back onto her the way it learned this morning, and you stop pretending it isn't."
    show fs_pc flushed
    fs_you "\"...Again. {i}Again{/i}, then— to {i}order{/i}— make it to {i}order{/i}— {i}ahh{/i}—!\""
    show fs_regan flat at vn_cast_slot
    fs_regan "\"Seat's taking it. Log it.\""
    show cg fs_pallet_sex_peak onlayer cgl
    "She drives in to the root and stays there, and the shrink-wrap squeals under your puffy nipples, and you come over the pallet again, untouched." with vnfx("shake")
    $ fs_enc.pc_orgasms = 1
    show cg fs_pallet_sex_cum onlayer cgl
    "She fills you again, so much it runs out round her and down the backs of your thick thighs." with vnfx("flash")
    $ fs_enc.partner_came = True
    jump fs_pallet_after

## Rung 6, door six: the thighjob in full, a broad man rating it out loud. Non-con, flips on the
## second turn into "Plush cut". (days-late.twee :: Vellum Six Door Six Sex; opener thighs, lock)
label fs_door_six_sex:
    $ vn_enter(bg="fs_armchair_room", pc="protesting", pc_tag="fs_pc", cg="fs_door6_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_door6_open onlayer cgl
    if fs.door6 == "knees":
        "You clamp your knees together to shut him out. There's no gap to shut. You just squeeze him tighter, and he groans."
    elif fs.door6 == "protest":
        fs_you "\"It says {i}AMBASSADOR{/i}, not— it's a {i}representative{/i} role— I {i}represent{/i} the range—\""
    else:
        "You push up off the armchair on both hands. His hand on your back puts you down again."
    fs_cust "\"Four.\""
    "Thrust."
    show cg fs_door6_mid onlayer cgl
    fs_you "\"Seamless inner leg is the {i}shorts{/i}— it's the {i}shorts'{/i} feature— let {i}go{/i}—\""
    fs_deb "\"Customer's rating as he goes.\""
    "He is. Out loud. And every thrust drags along your small cock in the pouch, and your thighs start to grip him on their own."
    "You stop clamping to get him out and start clamping to keep him in."
    show fs_pc flushed
    fs_you "\"Plush cut— ask for it by {i}NAME{/i}— squeeze them, I'm {i}IN{/i} the range—!\""
    show cg fs_door6_peak onlayer cgl
    fs_you "\"Soft-touch inner leg— you can {i}FEEL{/i} it— rate them, go {i}ON{/i}—!\"" with vnfx("shake")
    fs_cust "\"Five. {i}Five.{/i}\""
    jump fs_door_six_after

## The finale: Deb, her black strap-on, over her kitchen counter, already in. Non-con, flips on
## the second turn, on the dashboard's last line. (days-late.twee :: Vellum Six Deb Sex; anal,
## doggy, inside; the authored climax is fs_ambassador)
label fs_deb_sex:
    $ vn_enter(bg="fs_deb_kitchen", pc="protesting", pc_tag="fs_pc", cg="fs_deb_open")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg fs_deb_open onlayer cgl
    if fs.counter == "grip":
        "You grip the counter edge so hard the laptop jumps."
    elif fs.counter == "questions":
        fs_you "\"Deb, I'm asking you {i}QUESTIONS{/i}— how long have you— why did you— {i}Deb{/i}—\""
    else:
        "You grab for the headset. She catches your wrist and puts your hand flat on the counter next to the laptop, and leaves hers on top of it."
    show fs_deb bored at vn_cast_slot
    fs_debx "\"Dispatch can't action that.\" \"Dispatch can't action that.\""
    "In your ear, then out loud, a half-beat late."
    vn_sfx "Slap. Slap."
    show cg fs_deb_mid onlayer cgl
    show fs_deb bored at vn_cast_slot
    fs_debx "\"Logged. Hold the counter.\" \"Hold the counter.\""
    "Her hand flat between your shoulder blades holds you on it."
    fs_you "\"Deb— {i}DEB{/i}— this is NOT in my route notes—!\""
    show fs_deb bored at vn_cast_slot
    fs_debx "\"It's on the manifest, Prentice.\" \"You're the manifest.\""
    "She drives in on the second one."
    show cg fs_deb_peak onlayer cgl
    "She reads you the last line off the laptop, in your ear and then out loud."
    show fs_deb bored at vn_cast_slot
    fs_debx "\"Next tier: none.\" \"Next tier: none.\""
    show fs_pc flushed
    fs_you "\"...None. There's {i}NONE{/i}— that's the {i}TOP{/i}— put me down for it— Deb, {i}HARDER{/i}—!\"" with vnfx("shake")
    jump fs_ambassador
