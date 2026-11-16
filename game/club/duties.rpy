## THE CLUBROOM and its duties (main.twee :: Club Room, Club Tea Service, Club Road Duty, Club
## Towels, Club Regimen, Club Practice, Club Cafe, Club Walk Home), rewritten for the VN
## (2026-11-12; PLAN.md: the duties as a daily menu, once each a day, any order, all skippable,
## written per rung). The day's rung is its own choice; once it's been had, the night is.

label clb_hub:
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    show screen clb_room
    $ _d = clb_due()
    $ _h = vn_clock.hour
    if _d == 2:
        $ _cap = "The minibus to camp leaves at two, straight after practice. Ollie's already been in twice to yell your name about it. Well. Yell {i}Sweetheart{/i}."
    elif _d == 3:
        $ _cap = "The coach to the qualifiers leaves at two. The front seat's saved. It's always saved. It's yours."
    elif _d == 4:
        $ _cap = "There's a powder-blue handbag on the low table, and the smell of good perfume. The association is here."
    elif _d == 5:
        $ _cap = "The league's started. The roster's in the hall, and nobody's shouting."
    elif _d == 6:
        $ _cap = "The coach to nationals leaves at two. The whole roster's kit is already stacked by the door, and the front seat has a cushion on it now, with your name on."
    else:
        $ _cap = "The clubroom: benches, a kettle, the low table, and the uniform closet with thirty years of skirts in it in order of prettiness. Nobody's ever explained the order."
    $ _go = None
    menu:
        "[_cap]"
        "Tea service" if not clb_did("tea"):
            $ _go = "clb_tea"
        "Towel duty" if not clb_did("towels"):
            $ _go = "clb_towels"
        "The regimen" if not clb_did("regimen"):
            $ _go = "clb_regimen"
        "Road duty (an away fixture)" if clb.tier >= 2 and not clb_did("road") and 9 <= _h < 18 and _d != 3:
            $ _go = "clb_road"
        "Practice with the captain" if clb.tier >= 2 and not clb_did("practice") and _h < 21:
            $ _go = "clb_practice"
        "Tea with Iris, at the café" if clb.tier >= 3 and not clb_did("iris") and 9 <= _h < 19:
            $ _go = "clb_cafe"
        "Open the closet door (the board)":
            $ _go = "clb_closet"
        "Get on the minibus (camp)" if _d == 2:
            $ _go = "clb_camp"
        "Road duty (the qualifiers)" if _d == 3:
            $ _go = "clb_qualifiers"
        "The inspection" if _d == 4:
            $ _go = "clb_inspection"
        "The slump" if _d == 5:
            $ _go = "clb_slump"
        "Nationals" if _d == 6:
            $ _go = "clb_nationals"
        "Walk home with Rhys" if clb.tier >= 5 and not _d and _h >= 16:
            $ _go = "clb_walk_home"
        "Home for the night" if not _d:
            $ _go = "clb_home_night"
    hide screen clb_room
    if _go in ("clb_camp", "clb_qualifiers", "clb_inspection", "clb_slump", "clb_nationals"):
        if vn_clock.hour < 14:
            $ vn_until(14)
    jump expression _go

label clb_home_night:
    "You lock up. Down the hill to Domus Street, and the narrow stairs, and your room at the top of the house."
    call vn_night(7)
    jump clb_wake

label clb_closet:
    show screen clb_board
    if clb.tier >= 6:
        "The new sheet's heading: you unfolded it once. You folded it back."
    elif clb.tier == 5:
        "The board's come down. A new sheet is taped up in its place, and its heading has been folded over so you can't read it."
    elif clb.tier >= 4:
        "Somebody has laminated it."
    elif clb.tier == 3:
        "Somebody's written {i}CALLED IT{/i} under the second one."
    elif clb.tier == 2:
        "A red line through the first column, with a star drawn next to it."
    else:
        "Three columns, the roster's names under each. Protein intake, presumably."
    hide screen clb_board
    jump clb_hub

## ---- TEA SERVICE (rungs 1-4: the second course, by rotation, non-con; the captain last, and he
## asks. From the slump it's just tea.) -----------------------------------------------------

label clb_tea:
    $ clb_mark("tea")
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_kneel_pour")
    if clb.tier >= 5:
        "You kneel at the low table and pour. Cups in the order they like them. Lemon for Hugh. Two sugars for Ollie, who says he takes none."
        show clb_hugh shy at vn_cast_slot
        clb_hugh "\"Thank you, manager.\""
        "The second course has a neat line through it on the duty sheet. Nobody's asked. Nobody's going to. Ollie looks at the line, and at Rhys, and grins into his cup like he won something."
        show clb_rhys red at vn_cast_slot
        clb_rhys "\"Thanks, [clb_pc_name].\""
        "Rhys takes his last. His fingers stay on yours round the cup."
        $ vn_pass(20)
        jump clb_hub
    "The tray. The low table. You kneel, the skirt folded under your knees, and pour. Lemon for Hugh. Two sugars for Ollie. The roster sprawls on the benches, sweaty, steaming, watching your hands."
    "Then the second item on the sheet. Same font as the bus rota."
    "{color=#ff8fb8}{i}Second course: hydration support, by rotation.{/i}{/color}"
    if clb.tier == 1:
        "You've done this once. You have notes. {i}Second course: NOT AGREED.{/i} Underlined twice. Nobody's read your notes."
    elif clb.tier == 2:
        "The skirt's tighter round your hips when you kneel now, and it rides up the back. Ollie notices. Ollie notices out loud. \"Gentlemen, the {i}view{/i} from the cheap seats—\""
    elif clb.tier == 3:
        "Lucky hands, now, even here. A palm on your thigh as somebody sits down on the bench behind you. A squeeze of your ass through the skirt. \"For luck, Sweetheart.\" Ten points a set."
    else:
        "You kneel, and your tits sway in the ruffled blouse, and the whole bench goes quiet. Somebody actually says \"wow\" out loud, and then apologises, and then says it again."
    show clb_hugh shy at vn_cast_slot
    "Hugh's first. Hugh's always first. He kneels opposite you, huge, careful, shorts already tented, and unties the drawstring like he's opening a present."
    clb_hugh "\"Thank you, manager.\""
    "Before you've even started."
    show clb_pc flustered
    clb_you "\"Hugh. I have not agreed to the second course. I have {i}never{/i} agreed to the second—\""
    if clb.tier >= 4:
        "Somebody behind you is already undoing the ruffled blouse; you slap at his hands, and he does the next button anyway. \"Morale, Sweetheart.\" Ollie takes your clipboard out of your hands and puts it on the bench."
    else:
        "Somebody behind you loosens your tie and tucks it into your blouse for you, so it won't get in the way. \"Page five, Sweetheart.\" Ollie takes your clipboard out of your hands and puts it on the bench."
    "He's out. Thick, flushed, a bead at the tip already, right at your lips. He smells like effort. Your mouth waters, and you file that under the kettle being on, and you clamp it shut."
    "Hugh's hand settles on the back of your head. Gentle. Immovable."
    show clb_ollie grin at vn_cast_slot
    menu:
        clb_ollie "\"Look at that FORM. Hold him, Hugh.\""
        "Keep your mouth shut":
            $ clb.tea_pour = False
        "Keep pouring with one hand, out of spite":
            $ clb.tea_pour = True
    jump clb_tea_sex

label clb_tea_after:
    $ vn_enter(bg="clb_clubroom", pc="loud", pc_tag="clb_pc", cast=[], cg="clb_tea_end_%d" % max(1, min(4, clb.tier)))
    "They finish the way they started: in order, one at a time, every one of them on your tongue and down your throat, a hand on your head for each. {i}Glk. Glk.{/i} You swallow between each, because they wait until you do."
    if clb.tier <= 2:
        "Your jaw's loose and warm. Your chin's a mess. Your cock is a hard, ignored throb in your panties, tenting the skirt, and every single one of them looks at it on the way past and grins, because it gives you away every time."
    elif clb.tier == 3:
        "There were hands the whole time. On your thighs, up under the hem, squeezing your ass while they moved your head for you. Somebody palmed your cock through your panties for luck, and you moaned so loud round Ollie that he cheered."
        "The lace is soaked through at the front now. You didn't even come. It's just leaking."
    else:
        "The ruffled blouse was open the whole time, and every one of them stared at your tits while you swallowed. You lick your lips, and catch yourself squeezing them together for the last man in line, and stop, and don't stop."
        "The whole bench groans."
    if clb.tea_pour:
        "And you never spilled a drop of the tea. You poured every cup one-handed, out of pure spite, with a hand on your head and a cock in your mouth, and the cups are lined up on the tray in order. Ollie actually applauds."
    if clb.tier >= 4:
        clb_you "\"...Next.\""
        "You rasp it, before you can stop it. You hear it. Ollie hears it, and cheers."
    else:
        clb_you "\"That was NOT— on the— {i}sheet{/i}—\""
        show clb_ollie grin at vn_cast_slot
        clb_ollie "\"Next!\""
        "Says Ollie, over you, out of habit."
    hide cg onlayer cgl
    "There isn't one. Everybody's done. Everybody except the captain."
    show clb_rhys composed at vn_cast_slot
    "Rhys waits until the room's cleared. Always. He kneels where Hugh knelt and doesn't untie anything for a long moment. He looks at your chin, and at your hands, still shaking, and his jaw goes tight."
    clb_rhys "\"You don't have to. Say no, and I go and shower.\""
    show clb_pc soft
    clb_you "\"It's on the sheet, Captain. ...And you asked.\""
    show clb_rhys red
    show cg clb_tea_captain onlayer cgl
    "Because he's the only one who ever asks. His ears go brick-red. He unties. Slow. Nothing like the others. His hand on the back of your head is barely a hand at all. He watches your face the whole time."
    if clb.tier >= 4:
        "You take him between your tits first, because they're there and he can't stop looking at them, and squeeze, and lick the tip every time it pushes up through."
        clb_rhys "\"{i}Fuck{/i}.\""
        "Very quietly, which is the only time you've heard him swear."
    else:
        "You take him deep, slow, the way he likes, and he makes a noise like he's been punched."
    "When he comes it's with your name caught in his teeth, unspoken, and he holds still and lets you take all of it. Thick and hot on the back of your tongue. More than any of them. You swallow twice and it still runs out of the corner of your mouth."
    show clb_pc loud
    clb_you "\"Mmh— {i}mmnh{/i}— hydration— {i}hydration{/i}—\""
    hide clb_rhys
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"TEN POINTS!\""
    hide cg onlayer cgl
    "You gurgle it round him, louder than you meant. Ollie, from the corridor. Rhys wipes your chin with his thumb. Then he kisses your forehead."
    hide clb_ollie
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"No further notes.\""
    hide clb_rhys
    "He goes to shower."
    "{color=#9a9aa6}The clipboard, that evening: {i}Second course: completed. Captain last.{/i}{/color}"
    $ vn_pass(20)
    jump clb_hub

## ---- TOWEL DUTY (the duty that is just a duty, until rung 3) --------------------------------

label clb_towels:
    $ clb_mark("towels")
    $ vn_enter(bg="clb_locker_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    if clb.tier <= 2:
        "Towels. Folded. Warm. Handed over before the hand is out. You've got the rotation down to a system: front row warm, spares in the bench crate, the captain's kept separate because he goes through two."
        clb_roster "\"Thanks, Sweetheart. Thanks, Sweetheart. Thanks, Sweetheart.\""
        "Call and response. Nobody taught it to them."
        show clb_rhys composed at vn_cast_slot
        "Rhys takes his without looking. He knows it'll be there. You built that."
        clb_rhys "\"Thanks. ...Manager.\""
        "Too quiet for the others."
    elif clb.tier == 3:
        "Towels. The roster towels off in front of you like you're furniture. Then, lately, not like you're furniture at all: Ollie flicks his at your skirt, Hugh holds his out for you to dry his back, and you do, because it's quicker."
        show clb_hugh shy at vn_cast_slot
        "Then his front. He turns round. He's hard. He's very hard, and very sorry about it."
        clb_you "\"Towel duty.\""
        "Firmly, meaning {i}the towel{/i}. You hold it out."
        clb_hugh "\"Thank you, manager. Cleaning up. It's on the sheet.\""
        show cg clb_towel_hugh onlayer cgl
        show clb_pc flustered
        "He takes your hand instead, towel and all, and wraps it round himself, and his huge hand closes over yours and doesn't let go."
        clb_you "\"It is NOT— Hugh— that's not what {i}cleaning up{/i}— {i}Hugh{/i}—\""
        "Slick, quick, a twist at the top, his hand working yours, until he comes into the towel with his forehead on the lockers going \"thank you, thank you, manager, {i}thank you{/i}—\""
        hide cg onlayer cgl
        "He lets go. You drop the towel in the basket, and your hand's still curled the shape of him. Ollie whistles."
        "Rhys drops his towel. Twice. Picks it up, both times, with his ears on fire."
    elif clb.tier == 4:
        "Towels. Bending for the bench crate is a whole event now. There's a silence behind you every time, and then a lot of loud talking about the weather."
        clb_hugh "\"Thank you, manager.\""
        "Says Hugh, to your chest."
        show clb_ollie grin at vn_cast_slot
        "Ollie's turn. You towel his hair, his shoulders, and your tits press into his chest while you reach round for his back, and he just stands there and lets it happen with his eyes shut."
        clb_ollie "\"I'm going to need cleaning up again. Look. Look what you've done.\""
        clb_you "\"No. I've done your {i}hair{/i}—\""
        show cg clb_towel_knees onlayer cgl
        show clb_pc flustered
        "Two hands on your shoulders, pressing, friendly, and your knees hit the floor. It's on the sheet, apparently. \"Hold her, Hugh.\" Your blouse comes open. Ollie's fist round himself, your tits pushed together under the head by somebody else's hands, {i}shlk shlk shlk{/i}, while you tell him precisely what towel duty means, and somewhere in the middle of the definition you start moaning instead, and he comes across your cleavage."
        hide cg onlayer cgl
        "Somebody hands you the towel. You towel that off too. Mostly."
        show clb_rhys composed at vn_cast_slot
        "Rhys takes his towel and holds yours out to you, folded, warm. Nobody's ever done that."
    else:
        show clb_rhys composed at vn_cast_slot
        show cg clb_towel_rhys onlayer cgl
        "Towels. Rhys takes yours off you at the end and does the drying himself: your hair, the back of your neck, slow."
        show clb_ollie grin at vn_cast_slot
        clb_ollie "\"Get a room.\""
        "Delighted."
        clb_rhys "\"We have one. It's hers.\""
        hide cg onlayer cgl
    $ vn_pass(30)
    jump clb_hub

## ---- THE REGIMEN (the card, the sachet, the leaflet into S, unread) ------------------------

label clb_regimen:
    $ clb_mark("regimen")
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    if (clb.boxes or 0) < max(1, clb.tier) and not clb.done:
        $ clb.boxes = max(1, clb.tier)
        $ clb.leaflets = min((clb.leaflets or 0) + 1, 6)
        show cg clb_regimen_box onlayer cgl
        show screen clb_slip("", ["{i}Complimentary. As always.{/i}"])
        "A new box on the low table, in sponsor blue, tied with a ribbon. A card on top in Madame Lacroix's handwriting."
        hide screen clb_slip
        "Inside: sachets in rows, a laminated schedule, and a leaflet folded under the schedule."
        "You read the schedule, because the schedule is operational. You read as far as {color=#e8c35a}complimentary{/color} on the leaflet."
        show cg clb_folder_s onlayer cgl
        "Then it goes in the document box. Under S."
        $ _fold = CLB_FOLDER[clb.leaflets]
        "[_fold]"
        hide cg onlayer cgl
    else:
        "Today's sachet, at the time on the card. Chalky, sweet, faintly floral. You drink it standing at the kettle and rinse the glass."
        "It does nothing. It never does anything on the day."
    jump clb_hub

## ---- ROAD DUTY (from rung 2: an away fixture, the front seat; hands, by rotation, through rung 4;
## from the slump, the captain's seat and only his, and consensual) ---------------------------

label clb_road:
    $ clb_mark("road")
    $ vn_enter(bg="clb_coach_bus", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "An away fixture. The coach. The front seat. You've got the route on the clipboard, the snacks in a bag by your feet, and the tea in a flask between your knees."
    if clb.tier == 2:
        show clb_ollie grin at vn_cast_slot
        "Ollie leans over the back of your seat the whole way, narrating the motorway to the driver. Every so often a hand comes over the headrest and squeezes your shoulder, or tugs your hair, or rubs the back of your neck. \"For luck, Sweetheart.\" \"Morale, Sweetheart.\""
        clb_you "\"Hands off the manager's neck, it's a {i}moving vehicle{/i}—\""
        "More hands, for luck. They win by a mile. On the way home Hugh falls asleep with his head on your shoulder from the seat behind, and drools on your blouse, and you let him."
    elif clb.tier <= 4:
        "The seat next to the manager goes by rotation now. Nobody wrote that down. Everybody knows it."
        $ _part = "tit" if clb.tier >= 4 else "thigh"
        "First leg, a setter, whose hand creeps onto your thigh at the first roundabout. You lift it off. It comes back, higher, and stays there, warm, kneading, while you tell him about seatbelt regulations. Second leg, Hugh, who asks first, very formally, doesn't wait for the answer, and then holds your [_part] like it might break."
        show clb_ollie grin at vn_cast_slot
        show cg clb_road_jacket onlayer cgl
        "Third leg, Ollie. Ollie puts his jacket over his lap and takes your hand and puts it under the jacket, and keeps his own hand wrapped over yours."
        clb_ollie "\"Road duty.\""
        "Very seriously."
        show clb_pc flustered
        clb_you "\"Road duty is the {i}ROUTE{/i}, Ollie, it's the— let go of my— {i}Ollie{/i}—\""
        "It's hot and hard in your hand. He moves your fist on it under the jacket while the coach eats up the motorway, quick, his thumb pushing yours over the head, until your hand knows the stroke and his hand can just rest on top. He bites his own sleeve and comes in your fist at a service station sign."
        clb_ollie "\"Ten points a set.\""
        hide cg onlayer cgl
        "He whimpers it."
        if clb.tier >= 4:
            "On the way back two of them reach over the seat at once and get a handful each through the ruffled blouse, squeezing. You slap at them. They squeeze through the slapping. You keep reading the route out loud to the driver in a voice that keeps going up."
        else:
            "On the way back somebody's hand comes over the seat and down your blouse, just to feel the new softness there. You pull it out. It goes back in. You keep reading the route out loud to the driver in a voice that keeps going up."
        clb_you "\"Left— {i}left{/i} at the— hands {i}OFF{/i}— {i}hah{/i}— at the lights—\""
        show clb_rhys composed at vn_cast_slot
        "The captain takes the last leg. Last, always. He sits next to you and doesn't touch you at all, the whole way, except his little finger, which lies against yours on the armrest, and is somehow the worst of all of it."
    else:
        show clb_rhys composed at vn_cast_slot
        "The seat next to yours is the captain's now. Nobody else sits in it. Nobody's asked them not to."
        show cg clb_road_rhys onlayer cgl
        "His jacket over both your laps. His hand under it, under your skirt, up between your thighs, slow, the whole way there."
        if clb.tier >= 6:
            "Two fingers in you by the motorway. His thumb on your clit. Slow circles, the whole way home from the services, until you're clutching the flask so hard it creaks."
            show clb_pc loud
            clb_you "\"Nnh— {i}Rhys{/i}— that's— ahh— road— {color=#ff8fb8}ROAD DUTY{/color}—!\""
            "You come on his fingers in the front seat with the whole roster asleep behind you. Mostly asleep. Ollie gives you a thumbs-up in the mirror without opening his eyes."
        else:
            "His fingers slide round the back, under the lace, and find where he's been. Press. Circle. Slip in, one, just to the knuckle, and stay there, rocking, while the motorway lights slide over you."
            clb_you "\"Nnh— {i}Rhys{/i}— not on the— {i}hah{/i}— not on the coach—\""
            clb_rhys "\"Say if.\""
            show clb_pc loud
            clb_you "\"...Continue.\""
            "You breathe it, and push back onto it. You come on his finger in the front seat with your little cock leaking into the lace, biting your own wrist. It doesn't help. Ollie gives you a thumbs-up in the mirror without opening his eyes."
        hide cg onlayer cgl
    "{color=#9a9aa6}The clipboard: {i}Road duty: completed.{/i}{/color}"
    $ vn_pass(180)
    jump clb_hub

## ---- PRACTICE WITH THE CAPTAIN (from rung 2; from the slump, after practice can be a scene,
## optional, Rhys and only Rhys) --------------------------------------------------------------

label clb_practice:
    $ clb_mark("practice")
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg=None)
    if clb.tier == 2:
        "He stays for his jump serve. You stay because somebody has to shag the balls. Neither of you says this is a standing arrangement."
        show cg clb_jump_serve onlayer cgl
        "{i}Thwack.{/i} {i}Thwack.{/i} The ball hits the far line, again and again. He talks more when it's just the two of you. Not much. He can't cook. He thinks Ollie's a menace and would die for him."
        hide cg onlayer cgl
        "You hold out the towel. He takes it. His fingers stay a second too long on yours."
        clb_rhys "\"Thanks, manager.\""
    elif clb.tier == 3:
        "He serves into the net. Twice. You're in his eyeline, which is a problem, because you're in his eyeline for two hours a day."
        clb_rhys "\"Is the regimen— alright? Are they looking after you?\""
        clb_you "\"It's complimentary.\""
        clb_rhys "\"Right. Yeah. No, I know.\""
        "He stands there holding a ball for slightly too long."
    elif clb.tier == 4:
        show cg clb_bench_close onlayer cgl
        "You sit on the bench with two cups of the tea you made an hour ago. He sits next to you. Close. The specific close that people sit when the sitting's the point."
        clb_rhys "\"You know everyone thinks we're together.\""
        "He tells the far wall."
        clb_you "\"Mm.\""
        "You tell your cup. Neither of you says the thing. His knee presses yours, and stays there, and that's the whole practice."
        hide cg onlayer cgl
    else:
        "It's not really practice any more. He serves. You catch them in the basket. A few. Fewer. Then he takes the basket off you and puts it down and puts his hands on your waist, and the sports hall's enormous empty noise goes on around the two of you."
        clb_rhys "\"[clb_pc_name].\""
        show cg clb_net_post onlayer cgl
        show clb_pc flustered
        "Just to say it. He kisses you against the net post. Your tits squash against his chest. His hands slide down over your hips and grab your ass, both hands, and lift, and you go up on your toes with a squeak."
        clb_you "\"The equipment room has a lock.\""
        "You point it out, into his mouth."
        clb_rhys "\"I know. I've been thinking about that lock since the box.\""
        hide cg onlayer cgl
        menu:
            "The equipment room, and its lock."
            "Stay after, with him":
                jump clb_practice_sex
            "Back to the clubroom":
                pass
    $ vn_pass(60)
    jump clb_hub

label clb_practice_after:
    $ vn_enter(bg="clb_equipment_room", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_crash_mat_end")
    "He comes holding you down into the crash mat by the hips, groaning into the back of your neck. Every pulse."
    if clb.tier >= 6:
        "You lie on the crash mats with your skirt round your waist and your legs still open, his cum leaking out of you onto the vinyl, your pussy still fluttering round nothing. Your tits heave. He puts his hand flat on your belly, low, like he's checking you're real."
    else:
        "You lie face down on the crash mats with your skirt round your waist, his cum leaking out of your ass, your little cock a sticky soft thing in a puddle of your own. He kisses all the way down your spine, one kiss per bump, and you giggle into the mat."
    show clb_pc loud
    clb_you "\"{i}Ahh{/i}— Rhys— that's— that counts as— {i}conditioning{/i}—!\""
    "You yell it at the equipment room ceiling. The volleyballs in the cage rattle."
    clb_rhys "\"It's on the sheet now. I wrote it on.\""
    "He says it into your hair."
    $ vn_pass(90)
    jump clb_hub

## ---- TEA WITH IRIS (from rung 3), at the café between the two campuses: the mirror ---------

label clb_cafe:
    $ clb_mark("iris")
    $ vn_enter(bg="clb_cafe", pc="deadpan", pc_tag="clb_pc", cast=[("clb_iris", "serene")], cg=None)
    "Iris Kendal takes her tea at a little place halfway between the two campuses. Kingsmere's manager. Twenty-three. Three seasons in. Serene, finished, moving like water, and pouring for both of you before you've sat down."
    if clb.tier == 3:
        "You ask about the regimen. Whether hers was the same. Whether there's a schedule."
        clb_iris "\"Mm.\""
        "She pours. She asks about your captain's jump serve instead. And your bus rota. And whether the association's done the inspection yet."
        "Every question is exactly what you'd ask. It takes you until the walk back to notice she answered nothing."
    elif clb.tier == 4:
        "She looks at the reorder slip sticking out of your clipboard. The C. She doesn't say anything."
        clb_you "\"Supplier's slow. I've put the fitting after the league starts. Not ideal, but—\""
        clb_iris "\"Mm. Is he still going last?\""
        "She refills your cup."
        clb_you "\"The captain? Always. Captain's privilege.\""
        show clb_iris smile
        "Iris smiles into her tea like you've told her the end of a film she's seen."
    elif clb.tier == 5:
        "She notices your bow. Her bow. Half-up, just how she'd do it."
        clb_iris "\"It suits you. It suited me too.\""
        clb_you "\"It's a practical—\""
        show clb_iris smile
        clb_iris "\"I know. I said that too.\""
        "Kindly. She looks at the mark on your neck. She doesn't ask. She asks instead whether he walks you home, and whether he carries the bag, and whether he makes the tea wrong."
        clb_you "\"Yes. Yes. Yes. How did—\""
        clb_iris "\"Mine still does.\""
        "She pours."
    else:
        show cg clb_cafe_brooches onlayer cgl
        "She clinks her cup against yours. Her brooch catches the light, the same as yours."
        clb_iris "\"Welcome. ...Does he leave his toothbrush at yours?\""
        "You don't answer. She smiles exactly the way you've started smiling."
        clb_iris "\"Kingsmere's new manager starts in the spring. Twenty. Very organised. He's already asked me about the regimen.\""
        clb_you "\"What did you tell him?\""
        clb_iris "\"That it's complimentary.\""
        hide cg onlayer cgl
        "Says Iris, and pours."
    $ vn_pass(40)
    jump clb_hub

## ---- WALK HOME WITH RHYS (from rung 5): he walks you home every night; it's the night ------

label clb_walk_home:
    $ vn_enter(bg="clb_hill_night", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg=None)
    "Rhys carries your kit bag. He carries it every night now. You stopped arguing on the second night, because it was inefficient."
    "The long way, down the hill to Domus Street and up the narrow stairs to your room at the top of the house. His hand finds yours on the hill and stays there. Neither of you looks at it."
    show cg clb_doorstep onlayer cgl
    if clb.tier >= 6:
        "On the step he kisses you, and slides a hand under your skirt like he's checking something's still there. It is. Soft, bare, and wet the second his fingers get there. You shiver."
        clb_you "\"Logged.\""
        "He laughs into your mouth, and his middle finger slips in, just to the knuckle, just once, and you grab his collar."
        clb_you "\"{i}Hah{/i}— not on the {i}step{/i}—\""
        clb_rhys "\"Not on the step.\""
        "He agrees, and takes it out, and licks it, looking at you."
    else:
        "On the step he kisses you, slow, one hand on your ass, the other on the back of your head, until a light goes on across the street. His hand slides down the back of your skirt and squeezes, and his fingertips find the lace, and press, right there, where he was."
        clb_you "\"{i}Nnh{/i}— I can still feel you in there.\""
        clb_rhys "\"Good?\""
        clb_you "\"Recovery work. Tomorrow. Scheduled.\""
        clb_rhys "\"I'll bring the towels.\""
    hide cg onlayer cgl
    call vn_night(7)
    jump clb_wake
