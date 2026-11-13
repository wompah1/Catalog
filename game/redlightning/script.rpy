## Red Lightning's passages: THE SOURCE (owner, 2026-11-11: the Ren'Py script is what we edit from
## now on). Converted once, 2026-11-11, by tools/twee2rpy.py from catalog/game/02-engine/storylines/
## redlightning/ (main.twee, rungs.twee; the catalog at 5195a927c), its scene-art rows and the DoL VN
## trace; the twee is frozen there as the reference. Edit this file directly. One label per passage.

label rl_opening:
    ## main.twee: :: Redlightning Opening [vn]
    $ rl.fit = None
    ## The route's opening (New Game -> "Play My Rival Spikes My Sports Drink..."). Route.start has already preset Rory and made Track Halls home. The opening sets the red hair and an ace's grade (the old athletics wall is passed by construction), takes the locks, issues the kit, and walks you down to the season opener. VN script (framework/vn-script.js); the original prose is in docs/routes/vn-original/redlightning/.
    $ vn_enter(bg="rl_corridor", pc="grin", pc_tag="rory", cast=[], cg=None)
    if vn_clock.hour < 9 or vn_clock.hour > 13:
        $ vn_set_time(12, 30)
    $ rl_init()
    $ rl_kit()
    show bg rl_corridor onlayer bgl
    show rory grin at vn_pc_slot
    vn_sfx "BANG." with vnfx("shake")
    "You bang out of your room in squad red, spikes slung round your neck by the laces."
    "Hair everywhere. Red, wild. A bonfire nobody put out."
    vn_sfx "Thmp. Thmp. Thmp."
    "Track Halls. The squad's corridor. Somebody's music through the wall, somebody's protein shaker rattling in the kitchen."
    "Straight across from your door: Miles Thorne's. Shut."
    "He's already gone down. He's always first down."
    "You're [rl_pc_name] [rl_pc_surname]. Twenty-one. The university's sprint ace."
    "Two seasons. Two titles. The squad calls you [rl_nick], because that's all anyone sees of you going past: a streak of red."
    "Miles is twenty-one too. Two seasons. Two silvers."
    "Every final, he's the shoulder at your shoulder. Every final, he's second."
    "You love him for it. Best rival a bloke could ask for."
    "Season opener this afternoon. You slap both your cheeks."
    vn_sfx "SMACK. SMACK." with vnfx("shake")
    rl_rory "\"LET'S GO!\"" with vnfx("shake")
    "At nobody. At the whole corridor."
    rl_unk "\"Oi! SHUT IT!\""
    "You take that as support.\n{size=-5}{color=#ff8fa3}▸ Down to the track{/color}{/size}"
    $ vn_until(14)
    jump rl_opener

label rl_opener:
    ## main.twee: :: Redlightning Opener [vn]
    $ rl.fit = None
    ## The season opener: your first race on the squad (free play) or the first of the season (the route). You win by a street. The locker room after: the towel, his space, "scheme something". Rung 0; rung 1 is the next day's session. VN script (framework/vn-script.js).
    $ rl_init()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "neutral")], cg=None)
    if not rl.opener:
        $ rl.opener = True
        $ rl.rung_day = vn_clock.day
        $ rl.session_day = vn_clock.day
    $ _ranWell = rl_run()
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "Gun."
    vn_sfx "BANG." with vnfx("shake")
    "You're gone."
    "Knees high. Elbows driving."
    "The world funnels down to the tape, the slap of your spikes, the roar off the bleachers climbing with you."
    "Miles is at your shoulder for exactly as long as it takes you to remember he's there."
    "Then he isn't."
    if _ranWell:
        "You come off the bend already clear and you keep pulling. Clean. Easy. Stupid easy."
    else:
        "It's not your prettiest. Your arms go wide off the bend."
        rl_rory "\"Arms— ARMS, you idiots—\""
        "You still pull clear."
    rl_lenny "\"BY A STREET! [rl_NICK] BY A STREEEET!\"" with vnfx("shake")
    "He's standing on the bench to scream it."
    show cg rl_opener_finish onlayer cgl
    "You thunder through the line with both arms up, spin a full circle, and whoop at the sky."
    rl_rory "\"WOOOOO!\""
    hide cg onlayer cgl
    show miles neutral at vn_cast_slot
    "Miles crosses second. Chin down. Jaw tight."
    "You jog straight back and throw an arm round his neck."
    rl_rory "\"Oi! Not bad, Thorne! Silver again! You'll have me next time.\""
    "You squeeze."
    rl_rory "\"Maybe.\""
    rl_miles "\"Says the bloke who wins by a street every time.\""
    "He mutters it into his own collarbone."
    rl_rory "\"It's all in the arse, mate!\""
    vn_sfx "SMACK."
    "You slap your own backside."
    rl_rory "\"Squats! Come and do extra sets with me!\""
    "Lenny hits you at a dead sprint and nearly takes you off your feet." with vnfx("shake")
    "Lenny Platt, twenty, second year. Your self-appointed hype man."
    rl_lenny "\"LEGEND. You're not human. I keep telling people you're not human.\""
    rl_rory "\"Hot blood and fast legs, Len!\""
    rl_coach "\"[rl_pc_surname]!\""
    "Coach Gilmour, from behind his clipboard. Gravel voice, cap low, fifty-eight and furious about it."
    rl_coach "\"You hijacked my opener. You're my ace. Don't you dare get cocky.\""
    rl_rory "\"Coach, I make cocky look GOOD.\""
    rl_imogen "\"Smile for the archive.\""
    "Imogen Shaw, twenty-two, team manager. Glasses, clipboard, the only sensible person on the squad."
    rl_imogen "\"And keep your shorts on this time.\""
    show rory shocked at vn_pc_slot
    rl_rory "\"That was ONE time!\""
    "Roxy Calder skips up: twenty-one, spiky hair, phone already up."
    rl_roxy "\"Nice tits, Lightning.\""
    "She squints at your chest."
    rl_roxy "\"Oh, wait. Not yet.\""
    show rory grin at vn_pc_slot
    rl_rory "\"Give me a month, Calder, and I'll put you to shame up top.\""
    "You flex at her. Both arms."
    rl_roxy "\"Promises, promises.\""
    hide miles
    show bg rl_locker onlayer bgl
    $ rl.fit = "towel"
    show cg rl_opener_locker onlayer cgl
    "The locker room after. Steam. Shouting."
    "You flop down on the bench dead centre in nothing but a towel that's given up on you."
    "It slips. You let it."
    "You sprawl, legs wide, water running down your chest from the bottle you've just emptied over your own head."
    "Miles is on the next bench. Towel knotted tight. Picking at his ankle tape."
    "You slide over until your knees knock."
    rl_rory "\"Thorne!\""
    vn_sfx "Smack."
    "Your hand lands on his bare back. It stays there."
    rl_rory "\"Did you see me wobble on the last step? Nearly ate the tartan.\""
    "His eyes go to your face. Then down."
    "The towel. Your hip. The freckles across your thigh."
    "Back up. Fast."
    rl_miles "\"Maybe next time the wind'll give me a break.\""
    rl_rory "\"Next time you'll have a secret weapon!\""
    "You squeeze his shoulder."
    rl_rory "\"Cycle of rivalry, mate. Else what's the fun?\""
    rl_miles "\"Yeah.\""
    "He doesn't smile."
    rl_miles "\"Maybe I'll scheme something.\""
    rl_rory "\"HA! Scheme away! You know I never lose!\"" with vnfx("shake")
    "You slap his back again and stand, towel nearly gone, and stroll off to the showers."
    "Behind you, the bench creaks as Miles sits very, very still."
    jump rl_hub

label rl_miles_door:
    ## main.twee: :: Redlightning Miles Door [vn]
    $ rl.fit = None
    ## Miles's door, across the corridor in Track Halls (a landing exit of the trackhalls home). A knock and a line for the rung you're on. VN script (framework/vn-script.js).
    $ _rlT = (rl.tier or 0)
    $ vn_enter(bg="rl_corridor", pc="grin", pc_tag="rory", cast=rl_door_cast(), cg=None)
    show rory grin at vn_pc_slot
    hide miles
    vn_sfx "Bang bang bang." with vnfx("shake")
    "You knock on his door like it owes you money."
    if _rlT == 0:
        show miles neutral at vn_cast_slot
        "He opens it a crack. His kit's laid out on the bed behind him in a neat row, folded."
        rl_miles "\"What.\""
        rl_rory "\"Fancy a pint? Celebrate my win? I'm buying!\""
        hide miles
        vn_sfx "Click."
        "He shuts the door. You hear him laugh behind it."
        vn_th "(Victory.)"
    elif _rlT == 1:
        show miles neutral at vn_cast_slot
        "He opens it, sees your bare arm on the frame, and stares at it."
        rl_miles "\"Is your skin— shining?\""
        rl_rory "\"Halls soap, mate! The good stuff!\""
        rl_miles "\"...Sure.\""
        "It comes out in a funny voice. He shuts the door slowly."
    elif _rlT == 2:
        show miles blush at vn_cast_slot
        "He opens it. You're in Roxy's top and nothing over it, because it's hot."
        "He looks at the ceiling for the entire conversation."
        rl_rory "\"Thorne. Feel this.\""
        show cg rl_door_feel onlayer cgl
        "You grab his wrist and plant his hand on your tit."
        rl_rory "\"That's not normal laundry, is it?\""
        vn_sfx "Squeeze."
        "His hand squeezes. Once. Twice. Your nipple pokes his palm through the top."
        show rory flushed at vn_pc_slot
        rl_rory "\"Hh— yeah. Do that.\""
        "He does that."
        hide cg onlayer cgl
        hide miles
        "Then he snatches his hand back like it's burnt and shuts the door."
        "You hear him slide down the back of it."
    elif _rlT == 3:
        show miles blush at vn_cast_slot
        "He opens it before you've finished knocking, like he was standing right behind it."
        rl_miles "\"Hey.\""
        "His eyes drop to your chest and stay."
        rl_miles "\"...Hey.\""
        rl_rory "\"You're weird lately, Thorne!\""
        "You poke him in the sternum. Your chest bumps his. He makes a sound like a kettle."
        show cg rl_door_kiss onlayer cgl
        "Then he grabs your hoodie strings, drags you in, and kisses you against the inside of his door."
        "Hard. Both hands full of your heavy tits."
        "You kiss him back, laughing into it, squeezing his arse."
        show rory flushed at vn_pc_slot
        rl_rory "\"Mmf— wrestling! Okay! I'm WINNING!\""
        vn_sfx "THUMP THUMP."
        "Somebody bangs on a wall down the corridor."
        "He shoves you back out, scarlet, and shuts the door."
    elif _rlT == 4:
        show miles hungry at vn_cast_slot
        "He opens it. You lean on the frame with your arms under your tits, grinning."
        rl_rory "\"Next colour?\""
        "He pulls you inside by the waistband and pins you to his wardrobe."
        "He sucks a mark into your neck while his hand kneads your arse."
        show rory flushed at vn_pc_slot
        rl_rory "\"Ahh— Thorne—\""
        rl_miles "\"Tomorrow.\""
        "Against your throat."
        rl_miles "\"You'll get it tomorrow.\""
        rl_rory "\"Promise?\""
        rl_miles "\"Promise.\""
        "He grinds his cock against your hip once, hard, and puts you back in the corridor."
        hide miles
        show rory grin at vn_pc_slot
        rl_rory "\"You're a STAR!\""
        "You tell his door."
    elif _rlT == 5:
        show miles hungry at vn_cast_slot
        "He opens it, pulls you in by the waistband, and shoves you face-first against the inside of his door."
        show rory flushed at vn_pc_slot
        "His hand goes down the back of your shorts. Two fingers, slick, straight into you. The way they went in at the shed."
        rl_rory "\"Hnnnh—!\""
        "You moan into the wood."
        rl_rory "\"Yes— {i}yes{/i}— Thorne, do it, I want—\""
        rl_miles "\"Tomorrow.\""
        "In your ear, wrecked, fingers curling."
        rl_miles "\"Stay tomorrow. All night.\""
        rl_rory "\"Promise—?\""
        rl_miles "\"Promise.\""
        "He pulls his fingers out, kisses your neck once, hard, and puts you back in the corridor."
        hide miles
        show rory grin at vn_pc_slot
        rl_rory "\"Hehe...\""
        "You stand there with your legs shaking, beaming."
    else:
        show miles blush at vn_cast_slot
        "He drags you in by your hoodie. His hoodie."
        "You don't come back out for a while."
    ## Visual-novel days: while the route runs, his door is the evening's flavour once the day's session has been had (the hub's link), and your door across the corridor is bed. Free play goes back out onto the landing (link markup: lint-age reads the landing's old passage name as prose anywhere else).
    "{size=-5}{color=#ff8fa3}▸ Back across the corridor, and bed{/color}{/size}"
    call vn_night(7)
    jump rl_wake

label rl_morning:
    ## main.twee: :: Redlightning Morning [vn]
    $ rl.fit = {1: "towel", 3: "undies", 4: "bra"}.get(rl.tier, None)
    ## The morning after a rung: the change lands overnight, and you explain it in ONE spoken line (spec). Rungs 1, 3 and 4 land here; rung 2's morning runs straight on into its locker room, and rung 5's is in Miles's bed (rungs.twee). At home, wherever home is. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ rl_land()
    $ vn_enter(bg="rl_bedroom", pc="grin", pc_tag="rory", cast=[], cg=None)
    hide miles
    show rory grin at vn_pc_slot
    if rl.tier == 1:
        $ rl.fit = "towel"
        "Morning. Shower."
        vn_sfx "Shhhhhhh."
        "You grab the razor out of your washbag out of habit."
        "And stop."
        "Nothing to shave."
        show cg rl_sa_rlhair onlayer cgl
        "{color=#ff5fb8}Not your jaw. Not your legs. Not your chest, not your pits, not— you look down.{/color}"
        show rory shocked at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Not {i}anywhere{/i}...?\"{/color}"
        "{color=#ff5fb8}You run a hand down your stomach and it slides. Glass-smooth. Polished.{/color}"
        "{color=#ff5fb8}The water beads up on you and rolls off like you're a waxed car.{/color}"
        show rory grin at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Huh.\"{/color}"
        "{color=#ff5fb8}And you laugh. And the laugh comes out with a little lilt on the end, a little {i}la{/i}, bright and bouncy.{/color}"
        rl_rory "{color=#ff5fb8}\"Ha-ha-ha-{i}la{/i}. ...Yep. Lilt.\"{/color}"
        "{color=#ff5fb8}You run your palm down your chest again. Slower. Over a nipple.{/color}"
        vn_sfx "Zzzt."
        show rory flushed at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Oh. Oh, that's—\"{/color}"
        "{color=#ff5fb8}Smooth skin is {i}sensitive{/i}. Every drop of water's a fingertip.{/color}"
        "{color=#ff5fb8}You soap your chest and your nipples stand up under your palms.{/color}"
        "{color=#ff5fb8}Your cock's stiff before you've decided anything, slick and bobbing in the steam.{/color}"
        $ _rl_feel = rl_take_feel()
        if _rl_feel:
            "{color=#e40081}[_rl_feel]{/color}"
        "You grab it."
        show rory grin at vn_pc_slot
        rl_rory "\"Victory lap!\""
        "Announced to nobody."
        vn_sfx "Shlk. Shlk. Shlk."
        "Fist on your cock, other hand rubbing circles on your glassy chest, forehead on the tiles."
        show rory flushed at vn_pc_slot
        rl_rory "\"Mmmh— ahh— AHH—\""
        "Moaning loud enough for the whole corridor. It's never felt like this. Like your whole skin's one big nerve."
        rl_rory "\"Hah— hah— and he's into the straight— he's— {i}ahh{/i}—\""
        show cg rl_cum_shower onlayer cgl
        "You come up the tiles in thick ropes, knees shaking, laughing your new laugh." with vnfx("flash")
        rl_rory "\"Ha-{i}la{/i}... haaah...\""
        hide cg onlayer cgl
        show rory grin at vn_pc_slot
        "The razor goes back in the washbag. You won't need it again."
        "You don't think about that for even a second."
        "You wipe the steam off the mirror and flex at yourself."
        "Somehow you know exactly which angle makes you look best. You've never cared about angles in your life."
        ## What you blame is flavour; both lead on: down to the track while the route runs (visual-novel days), out into your day in free play.
        $ _rlS = rl_straight()
        ## Linear days (Redlightning.linear): either line goes straight on to today's rung, at the session.
        $ _rlOn = _rlS[0] if _rlS else "rl_hub"
        $ _rlMins = max(0, 14 * 60 - (vn_clock.hour * 60 + vn_clock.minute)) if _rlS else 2
        menu:
            "Then you tell your reflection what's going on:"
            "\"Gains. Obviously gains.\"":
                $ rl.blame = "gains"
                $ vn_pass(_rlMins)
                jump expression _rlOn
            "\"It's the good halls soap.\"":
                $ rl.blame = "soap"
                $ vn_pass(_rlMins)
                jump expression _rlOn
    elif rl.tier == 3:
        show cg rl_sa_rlheavy onlayer cgl
        $ rl.fit = "undies"
        "{color=#ff5fb8}You wake up and roll over and something heavy rolls over with you a beat late.{/color}"
        vn_sfx "Flump."
        "{color=#ff5fb8}You sit up. They sit up after you.{/color}"
        "{color=#ff5fb8}Full. Round. Real weight to them now, heavy enough to sway when you twist.{/color}"
        vn_sfx "Boing. ...Boing."
        "{color=#ff5fb8}You hop out of bed and they bounce, and then bounce again on their own.{/color}"
        show rory flushed at vn_pc_slot
        "{color=#ff5fb8}You hold them. Heft them. Squeeze.{/color}"
        rl_rory "{color=#ff5fb8}\"Nnnhhh...\"{/color}"
        "{color=#ff5fb8}A long moan falls out of you before you can catch it.{/color}"
        "{color=#ff5fb8}Your hips roll on their own, slow and dirty. The exact grind from last night. You never learned that. Your arse did.{/color}"
        show rory grin at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Okay. That's going to make the bend interesting.\"{/color}"
        "{color=#ff5fb8}Breathless.{/color}"
        "{color=#ff5fb8}Your hips are wider. You reach back and grab your arse: twice what it was, a big soft double handful that keeps wobbling after you let go.{/color}"
        show rory flushed at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"{i}Ohh{/i}— hello, squats—\"{/color}"
        vn_sfx "Swish. Swish."
        "{color=#ff5fb8}Your thighs brush when you walk to the mirror.{/color}"
        "{color=#ff5fb8}There's a blush across your freckles that wasn't there yesterday and won't wash off.{/color}"
        "{color=#ff5fb8}Your hair's hanging in your eyes, down past your ears, brushing your shoulders.{/color}"
        "{color=#ff5fb8}You shove your shorts down to change, and pause.{/color}"
        "{color=#ff5fb8}Smaller. Definitely smaller. A neat little thing tucked under there like it's shy.{/color}"
        show rory grin at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Less drag.\"{/color}"
        "{color=#ff5fb8}Your voice has gone lighter again. Not one bit quieter.{/color}"
        $ _rl_feel = rl_take_feel()
        if _rl_feel:
            "{color=#e40081}[_rl_feel]{/color}"
        "Then you tell the mirror, with total confidence:"
        rl_rory "\"Hormonal weather, apparently. The doctor said it, so.\""
        vn_sfx "Jiggle jiggle."
        $ _rlS = rl_straight()
        $ _rl_on = _rlS[1] if _rlS else "Down to the track"
        "You jiggle your tits at your reflection for luck and go and find breakfast.\n{size=-5}{color=#ff8fa3}▸ [_rl_on]{/color}{/size}"
        if _rlS:
            $ vn_until(14)
            jump expression _rlS[0]
        $ vn_pass(2)
        jump rl_hub
    elif rl.tier == 4:
        show cg rl_sa_mirror onlayer cgl
        $ rl.fit = "bra"
        "{color=#ff5fb8}The bra won't close.{/color}"
        "{color=#ff5fb8}You stand there in the morning with both hands behind your back, hooking and unhooking. The band just will not meet.{/color}"
        "{color=#ff5fb8}You give up and look down.{/color}"
        show rory shocked at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"...Whoa.\"{/color}"
        "{color=#ff5fb8}They're {i}enormous{/i}. Full, high, heavy, crowding together in the middle and spilling over the sides of Coach's sports bra like they're trying to escape it.{/color}"
        "{color=#ff5fb8}Your waist's nipped in under them. Your arse sticks out behind you like a shelf you could put a cup on.{/color}"
        "{color=#ff5fb8}Your hair's a red tangle round your shoulders.{/color}"
        "{color=#ff5fb8}Your lips feel fat and soft when you lick them, and your tongue runs slow over them like it knows exactly what they're for now.{/color}"
        show rory grin at vn_pc_slot
        rl_rory "{color=#ff5fb8}\"Testing.\"{/color}"
        "{color=#ff5fb8}Your voice comes out a step higher. Exactly as loud. Louder, maybe.{/color}"
        rl_rory "{color=#ff5fb8}\"TESTING.\"{/color}" with vnfx("shake")
        $ _rl_feel = rl_take_feel()
        if _rl_feel:
            "{color=#e40081}[_rl_feel]{/color}"
        vn_sfx "BANG BANG."
        "Somebody through the wall bangs on it."
        vn_sfx "BANG BANG." with vnfx("shake")
        "You bang back."
        "You know exactly what this is now."
        "You grin at the mirror, cup your tits in both hands, hoist them. Let them drop."
        vn_sfx "Bounce."
        show rory flushed at vn_pc_slot
        "You do it again. And again."
        "Then you're squeezing them, kneading them, thumbs circling, watching yourself do it, hips rolling against the edge of the sink."
        "Your little cock's hard and pressing the porcelain."
        "You turn round, look at your arse over your shoulder, and give it a slap."
        vn_sfx "Smack."
        "It wobbles."
        rl_rory "\"Ahhn—!\""
        rl_rory "\"He did ALL this— hahh— to slow me DOWN—\""
        "Breathless and delighted."
        rl_rory "\"Ah— ah— AHH—!\""
        show cg rl_cum_sink onlayer cgl
        "You come against the sink with a tit in each hand, laughing." with vnfx("flash")
        hide cg onlayer cgl
        $ _rlS = rl_straight()
        $ _rl_on = _rlS[1] if _rlS else "Down to the track"
        show rory grin at vn_pc_slot
        rl_rory "\"Spiked. Still winning.\"\n{size=-5}{color=#ff8fa3}▸ [_rl_on]{/color}{/size}"
        if _rlS:
            $ vn_until(14)
            jump expression _rlS[0]
        $ vn_pass(2)
        jump rl_hub
    else:
        "You wake up. You stretch."
        rl_rory "\"Mmmmh— BRILLIANT.\""
        $ _rlS = rl_straight()
        $ _rl_on = _rlS[1] if _rlS else "Down to the track"
        "You feel brilliant.\n{size=-5}{color=#ff8fa3}▸ [_rl_on]{/color}{/size}"
        if _rlS:
            $ vn_until(14)
            jump expression _rlS[0]
        $ vn_pass(2)
        jump rl_hub

label rl_wake:
    ## main.twee: :: Redlightning Wake [vn]
    $ rl.fit = None
    ## A morning with nothing to land (visual-novel days, framework/vn.js): where the hub's night wakes, after the opener's day and rung 2's locker room. One loud line for the body the last bottle left (setup.redlightningWakes), what today is (every day has its rung), then down to the track. VN script (framework/vn-script.js).
    $ vn_enter(bg="rl_bedroom", pc="grin", pc_tag="rory", cast=[], cg=None)
    hide miles
    show rory grin at vn_pc_slot
    $ _rl_wake = rl_wake()
    "[_rl_wake]"
    $ _rlWt = (rl.tier or 0)
    if _rlWt == 5:
        "Tonight you're staying at his."
        vn_th "(You've been grinning about it since you opened your eyes.)"
    elif _rlWt == 4:
        "The big meet's this afternoon."
        "You do a lap of your room just to get it out of your legs."
    else:
        "Big session this afternoon."
        "You can feel it in your legs already."
    $ _rlS = rl_straight()
    if _rlS:
        ## Linear days (Redlightning.linear): straight on to today's rung.
        "{size=-5}{color=#ff8fa3}▸ [_rlS[1]]{/color}{/size}"
        $ vn_until(14)
        jump expression _rlS[0]
    else:
        "{size=-5}{color=#ff8fa3}▸ Down to the track{/color}{/size}"
        $ vn_pass(2)
        jump rl_hub

label rl_end:
    ## main.twee: :: Redlightning End [vn]
    $ rl.fit = "greyhoodie"
    ## THE ENDING, "Dead Heat": the last lap, side by side, and Imogen calls it. One ending; its id is picked at rung 4 (decision 5): Keep quiet gives `reveal`, Tell gives `confront`. One feat per ending. The completion is written on the spot; the locks go, and the pronouns go back to the body's (she). Then the stay-or-go epilogue (decision 6), which earns nothing more. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ _rlEnd = "confront" if rl.told else "reveal"
    $ rl.ending = _rlEnd
    $ rl.ending = _rlEnd
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[], cg=None)
    if _rlEnd == "confront":
        $ vn_feat("Every Bottle After")
    else:
        $ vn_feat("Best Mates Forever")
    show rory flushed at vn_pc_slot
    hide miles
    rl_imogen "\"DEAD HEAT!\"" with vnfx("shake")
    "Clipboard over her head."
    rl_imogen "\"DEAD HEAT! I SAW IT! DEAD— {i}HEAT!{/i}\"" with vnfx("shake")
    vn_sfx "Hahh. Hahh. Hahh."
    "You're both on your backs on the tartan, heaving, hands still locked together from where you grabbed each other across the line."
    show rory grin at vn_pc_slot
    rl_rory "\"I never lose!\""
    "You gasp it at the sky, delighted."
    show cg rl_sa_rlend onlayer cgl
    "Miles rolls his head over to look at you. Red hair everywhere. Tits heaving. That grin."
    rl_miles "\"Neither do I.\""
    rl_miles "\"Now.\""
    if _rlEnd == "confront":
        rl_miles "\"You knew.\""
        "Still breathless."
        rl_miles "\"Since the orange one. You looked me in the eye and drank it.\""
        rl_rory "\"Every bottle after. Every single one.\""
        rl_rory "\"Next colour, Miles.\""
    else:
        rl_miles "\"You never said. Not till the shed. You let me keep handing them over.\""
        rl_rory "\"Best mates don't spoil a good scheme.\""
        "You squeeze his hand."
        rl_rory "\"Best mates FOREVER.\"" with vnfx("shake")
    vn_sfx "Pfft— HAHAHA!"
    "He laughs so hard he has to roll onto his side."
    "The squad pours onto the track."
    "Lenny's screaming. Roxy's filming until Imogen takes it off her."
    "Coach Gilmour stands over the pair of you with his cap off and says nothing at all. From him, that's a speech."
    "Same old you. Loudest thing on the track. Quickest thing on the track."
    menu:
        "Your best mate's girlfriend."
        "Another season in Track Halls" (ending=True):
            jump rl_epilogue_stay
        "A flat in town with both names on the door" (ending=True):
            jump rl_epilogue_go

label rl_epilogue_stay:
    ## main.twee: :: Redlightning Epilogue Stay [exitCheckBypass vn]
    $ rl.fit = "greyhoodie"
    ## exitCheckBypass: in a route save the last link is <<route_return>>'s "Choose another story", a link with no passage, which DoL's footer would report as "no usable links".
    ## Stay: another season. Home is Track Halls, Miles's room now. The same body either way. VN script (framework/vn-script.js).
    $ rl.epilogue = "stay"
    $ rl.home = "trackhalls"
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "Another season."
    show cg rl_movein onlayer cgl
    "You move across the corridor. It takes one trip."
    "Your spikes go on his radiator next to his. Your toothbrush goes in his cup."
    "Two toothbrushes."
    "Lenny tells the entire squad."
    hide cg onlayer cgl
    "You run anchor. You always run anchor."
    show cg rl_kitstore_sex onlayer cgl
    "Sometimes, before the relay, he pulls you into the kit store first."
    "Up against the hurdles, your shorts round your knees, his hand over your mouth because you're too loud."
    show rory flushed at vn_pc_slot
    rl_rory "\"Mmmf— mmmhh— MMMF—!\""
    "Fucking you fast and deep until your legs shake."
    rl_miles "\"For luck.\""
    "In your ear."
    "You run the anchor leg with your thighs still sticky and win anyway."
    show cg rl_drink_luck onlayer cgl
    "And before every race, at the blocks, Miles hands you a bottle."
    rl_miles "\"For luck.\""
    "You drink it in one go, looking right at him."
    ## After the epilogue, back to route select (owner, 2026-10-19; vn.twee's <<route_return>>). The storyline finishes here, as <<sl_exit>> did; a route save chooses another story, and free play goes on at the track.
    $ rl.done = True
    "Neither of you ever checks the colour.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump rl_route_return

label rl_epilogue_go:
    ## main.twee: :: Redlightning Epilogue Go [vn]
    $ rl.fit = "squadtee"
    ## Go: off campus at the end of the season (was the "halted" ending, decision 5). A flat in town with both names on the door; the bottles stop, and the last one sits in the fridge door. The first Sunday: burnt toast, then him home with the shopping and you on the counter -- an optional director scene, the titjob. You still run every morning. VN script.
    $ rl.epilogue = "go"
    $ rl.home = "ownflat"
    $ vn_enter(bg="rl_flat", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    show cg rl_flatdoor onlayer cgl
    "End of the season."
    "A flat in town, third floor, with both names on the door: his tidy handwriting and your big messy capitals."
    "The bottles stop."
    "The last one sits in the fridge door. Unopened. Neither of you mentions it."
    hide cg onlayer cgl
    $ rl.fit = "squadtee"
    "First Sunday. You're making toast in his old squad tee and nothing else."
    show cg rl_toast onlayer cgl
    vn_sfx "BEEP BEEP BEEP BEEP." with vnfx("shake")
    "The toast is on fire. The smoke alarm is screaming."
    show rory shocked at vn_pc_slot
    rl_rory "\"SHUT UP! SHUT UP SHUT UP SHUT UP—\""
    "You're screaming back at it, swatting it with a tea towel, tits bouncing out the sides of the tee."
    vn_sfx "Click."
    "The door opens. Miles, with the shopping."
    "He looks at the smoke. He looks at you on your tiptoes on a chair, his tee riding up over your arse."
    vn_sfx "Thud."
    "The shopping hits the floor."
    show rory grin at vn_pc_slot
    rl_rory "\"Morning! I made breakfast. It died.\""
    hide cg onlayer cgl
    show miles hungry at vn_cast_slot
    "He lifts you off the chair and sits you on the counter. His hands go under the tee."
    $ rl.fit = "nude"
    "You haul it off over your head for him, grab your own tits and squeeze them together, grinning down at him."
    show rory flushed at vn_pc_slot
    rl_rory "\"Go on, then. Right here.\""
    menu:
        rl_rory "\"GO ON.\""
        "Squeeze them round him":
            jump rl_go_counter_sex
        "Kiss him, and open the window first":
            jump rl_go_sunday

label rl_go_counter_after:
    ## main.twee: :: Redlightning Go Counter After [vn]
    $ rl.fit = "greyhoodie"
    $ vn_enter(bg=None, pc="grin", pc_tag="rory", cast=[], cg="rl_gocounter_climax")
    show rory flushed at vn_pc_slot
    if rl_enc.partner_came:
        "He comes with a groan between your tits. Up your chest. A hot splash on your chin." with vnfx("flash")
        "You lick it off your lip and laugh."
    else:
        "He pulls you off the counter and onto him instead, and you finish it against the fridge door."
        vn_sfx "Rattle rattle rattle."
        "The last bottle rattles in its rack until he comes in you with a groan."
    show rory grin at vn_pc_slot
    rl_rory "\"Breakfast of champions.\""
    "He kisses you, slow, and slides two fingers into you on the counter while you're still laughing."
    show rory flushed at vn_pc_slot
    "You stop laughing."
    rl_rory "\"Ohh— oh— Miles— MILES—\""
    show cg rl_cum_counter onlayer cgl
    "You grab the worktop and ride his hand until you come, heels drumming the cupboard doors, the last bottle rattling in the fridge." with vnfx("flash")
    rl_rory "\"AHHH—!\""
    show rory grin at vn_pc_slot
    rl_rory "\"Okay. NOW it's breakfast of champions.\""
    "You pant it.\n{size=-5}{color=#ff8fa3}▸ Sunday{/color}{/size}"
    jump rl_go_sunday

label rl_go_sunday:
    ## main.twee: :: Redlightning Go Sunday [exitCheckBypass vn]
    $ rl.fit = "nude"
    ## exitCheckBypass: <<route_return>>'s route link has no passage (see the Stay epilogue). VN script.
    $ vn_enter(bg="rl_flat", pc="grin", pc_tag="rory", cast=[("miles", "neutral")], cg=None)
    show rory grin at vn_pc_slot
    show miles neutral at vn_cast_slot
    "The alarm finally shuts up."
    "You eat the shopping off the floor, on the floor, legs over his lap."
    rl_miles "\"Run tomorrow?\""
    rl_rory "\"Every morning. Race you.\""
    rl_miles "\"You'll lose.\""
    rl_rory "\"I've NEVER lost.\""
    show miles blush at vn_cast_slot
    rl_miles "\"Dead heat. I was there.\""
    vn_sfx "Splat."
    ## After the epilogue, back to route select (<<route_return>>; see the Stay epilogue).
    $ rl.done = True
    "You throw a tomato at him.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump rl_route_return

label rl_pink:
    ## rungs.twee: :: Redlightning Pink [vn]
    $ rl.fit = None
    ## RUNG 1 -- the pink bottle (margin: by a street, Lenny). Covert: he hands it over, you drink it in one go because someone called you the ace, and on the two-man tempo the flush hits and you come in your shorts at full stride, untouched. You still cross first. Authored (solo). Body 1 (body hair gone, glass skin, a lilt) lands overnight. VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(1)
    $ rl_kit()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "neutral")], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "Afternoon session. Sun baking the tartan."
    "You're doing high knees on the spot. And commentating on them."
    rl_rory "\"And [rl_nick] warms up, and the crowd goes WILD—\""
    rl_imogen "\"There's no crowd.\""
    "She doesn't look up from her clipboard."
    rl_rory "\"The crowd's in my HEART, Imo.\""
    show miles neutral at vn_cast_slot
    "Miles. At your elbow, out of nowhere."
    "He's holding a bottle. Clear plastic. No label."
    "Inside: pink. Not sweet-shop pink."
    "Warning pink."
    vn_sfx "Fsssssss."
    "Neon, glowing, fizzing so hard the bottle rattles in his hand."
    rl_miles "\"Thirsty?\""
    "Careful voice. Too careful."
    rl_miles "\"Mixed it myself. Recharge formula.\""
    rl_miles "\"......\""
    rl_miles "\"For the ace.\""
    "The ace."
    vn_sfx "Krk!"
    "You've got the cap off with your teeth before he's finished the word."
    show cg rl_drink_pink onlayer cgl
    vn_sfx "Glk. Glk. Glk. Glk. Glk."
    "Gone. One go."
    vn_sfx "THUNK." with vnfx("shake")
    "You slam the empty into his chest and gasp."
    hide cg onlayer cgl
    show rory shocked at vn_pc_slot
    rl_rory "\"HAAAH. That's RANK.\"" with vnfx("shake")
    rl_rory "\"That's— it tastes like a fairground exploded and got banned.\""
    "You wipe your mouth on your wrist. Your lips come away stained pink."
    show rory grin at vn_pc_slot
    rl_rory "\"What's it meant to do, Thorne?\""
    "You grab your own pecs in both hands and jiggle them at him."
    rl_rory "\"Grow me a pair of tits to match my ego?\""
    "His eyes drop to your hands. To your chest."
    "They stay there."
    rl_miles "\"Maybe.\""
    show miles hungry at vn_cast_slot
    rl_miles "\"Give it a minute.\""
    rl_rory "\"HA! Bring it on!\""
    "You bounce them again for the squad. Lenny howls."
    rl_lenny "\"That's not a colour, mate.\""
    "He jabs a finger at the empty."
    rl_lenny "\"That's a warning. That's what they paint things that kill you.\""
    rl_roxy "\"He'd drink bleach if you called him the ace.\""
    rl_rory "\"Only if it came with a medal!\""
    rl_coach "\"Two-man tempos! [rl_pc_surname], Thorne, you're together. MOVE IT.\"" with vnfx("shake")
    $ vn_face("miles", "neutral")
    "Shoulder to shoulder on the line. He's close. Deep heat and clean laundry."
    "He doesn't look at you once. He doesn't need to."
    show rory flushed at vn_pc_slot
    "Something warm is spreading out from your stomach."
    vn_th "(Sugar rush. Has to be.)"
    menu:
        "You bounce on your toes and yell down the track:"
        "\"LAST ONE ROUND BUYS THE PINTS!\"":
            $ rl.yell = "pints"
            jump rl_pink_tempo
        "\"TRY AND KEEP UP, THORNE!\"":
            $ rl.yell = "keepup"
            jump rl_pink_tempo

label rl_pink_tempo:
    ## rungs.twee: :: Redlightning Pink Tempo [vn]
    $ rl.fit = None
    ## Rung 1's tempo: the flush hits at full stride. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    vn_sfx "Fweeet."
    "You go."
    "First stride: fine."
    show rory flushed at vn_pc_slot
    "Second stride: {i}hot{/i}."
    "It comes up out of your stomach like somebody poured sunlight down your throat. Up your chest. Up your neck. Into your face."
    "Your nipples pull tight and tingle against the tank top, and every stride drags the fabric across them."
    vn_sfx "Zzzt. Zzzt. Zzzt."
    rl_rory "\"Hah— what— {i}hah{/i}—\""
    "And lower down. In the cycle shorts."
    vn_th "(Oh. Oh, {i}hello{/i}.)"
    "You're hard. Rock hard, at full stride, trapped flat up your belly in tight black lycra."
    "Every footfall drags the head against the seam. Up. Down. Up. Down. Like a hand that won't let go."
    "You don't slow down. You've never slowed down in your life."
    "Into the bend. Thorne at your shoulder, breathing hard. You can feel him looking."
    "Your thighs pump. Your cock throbs. The waistband grips the head on every stroke."
    "{=vn_sfx_i}Slap, slap, slap{/=vn_sfx_i} go your spikes."
    "{=vn_sfx_i}Zzzt, zzzt{/=vn_sfx_i} go your nipples."
    "Something's winding up low and tight and stupid, and you're laughing, because it's ridiculous, and you start calling it in your head like it's on telly—"
    "{color=#ec3535}{i}AND IT'S [rl_NICK] OFF THE BEND— HE'S CLEAR— HE'S PULLING AWAY— HE'S— HE'S—{/i}{/color}"
    rl_rory "\"Ohh— oh fuck— oh {i}FUCK{/i}—\""
    vn_sfx "BANG." with vnfx("shake", "flash")
    show cg rl_sa_tempo onlayer cgl
    "You come in your shorts at full stride."
    "Untouched. Hips jerking, rhythm shot to pieces, hot and wet and pulsing into the lycra in thick throbs—"
    vn_sfx "splrt, splrt, splrt"
    rl_rory "\"HAAAAHHH—!\""
    "Your legs keep going, because your legs don't know how to do anything else. The whole infield hears you. The hurdlers turn round."
    "You still cross first."
    rl_lenny "\"BY A STREET! [rl_NICK] BY A STREEEET!\"" with vnfx("shake")
    "Up on the bench, screaming."
    hide cg onlayer cgl
    "You stagger to a stop, hands on your knees, heaving. A dark wet patch spreading down the front of your shorts."
    show rory grin at vn_pc_slot
    "Grinning like a lunatic."
    if rl.yell == "pints":
        rl_rory "\"PINTS— ON— THORNE! And oh my GOD— that was the best rep— of my LIFE!\""
    else:
        rl_rory "\"TOLD YOU— KEEP UP! And oh my GOD— that was the best rep— of my LIFE!\""
    rl_roxy "\"We saw.\""
    "She's crying with laughter. Imogen writes something down without looking up from her clipboard."
    show miles blush at vn_cast_slot
    "Miles has stopped dead behind the line."
    "He's staring at your shorts. Red to the ears. Fists."
    rl_rory "\"THORNE!\"" with vnfx("shake")
    "You throw a sweaty arm round his neck and haul him in. The wet patch presses into his hip."
    rl_miles "\"Hngk—\""
    rl_rory "\"Whatever's in that, mate, it's rocket fuel. I was FLYING. Make me another!\""
    show miles hungry at vn_cast_slot
    rl_miles "\"Yeah.\""
    "Very quietly."
    rl_miles "\"I will.\""
    hide miles
    show bg rl_locker onlayer bgl
    "In the locker room you peel the sticky shorts off right there on the bench and wave them over your head at Lenny like a flag."
    rl_rory "\"ROCKET FUEL!\"" with vnfx("shake")
    "Your cock's still half-hard, slick, bobbing."
    "Miles takes one look and walks straight into the shower fully dressed.\n{size=-5}{color=#ff8fa3}▸ Hit the showers and sleep like the dead{/color}{/size}"
    call vn_night(7)
    jump rl_morning

label rl_blue:
    ## rungs.twee: :: Redlightning Blue [vn]
    $ rl.fit = None
    ## RUNG 2 -- the blue bottle (margin: by daylight, Coach). Covert; Imogen fishes the empty out of the bin and says nothing. The chest arrives overnight (it leads: the spec's deviation, because the comedy runs on it), so this rung runs across the night: the session and the bottle today, then the morning (body 2 lands), Roxy's top FOR SUPPORT, and the locker room with the new chest (Redlightning Blue Morning, Blue Locker). Optional director: your hand on him in the showers. VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(2)
    $ rl_kit()
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "Flying starts in the sun."
    "Your arms are catching the light all the way down, like somebody glazed you."
    rl_roxy "\"Oi. Hold still.\""
    "She grabs your wrist mid-drill and turns it over."
    rl_roxy "\"What are you {i}using{/i}? That's not soap. Nobody's soap does that.\""
    if rl.blame == "soap":
        rl_rory "\"Halls soap, Calder! The GOOD halls soap!\""
    else:
        rl_rory "\"Gains, Calder. Obviously gains.\""
    "You flex. Your laugh comes out with its new little lilt on the end."
    rl_rory "\"Ha-ha-{i}la{/i}!\""
    "Nobody else seems to hear it."
    show miles blush at vn_cast_slot
    "Miles does."
    "You win the flying starts. You win them all."
    rl_coach "\"By daylight.\""
    "Coach doesn't even look up. He grunts it into the clipboard. Writes it down."
    rl_coach "\"Again.\""
    hide miles
    show bg rl_locker onlayer bgl
    "Locker room after."
    show miles neutral at vn_cast_slot
    "Miles holds out a bottle. Electric blue. The blue of a swimming pool somebody's put too much chlorine in."
    rl_miles "\"Hydrate before you dehydrate.\""
    show cg rl_drink_blue onlayer cgl
    rl_rory "\"Mate. You're a STAR.\""
    vn_sfx "Glk glk glk glk."
    "Gone."
    rl_rory "\"Ooh, that one's like licking a battery!\""
    hide cg onlayer cgl
    $ vn_face("miles", "hungry")
    rl_miles "\"Mm.\""
    "His eyes are on your nipples, poking out through your damp tank top like you're cold."
    "You're not cold."
    rl_miles "\"You're shiny.\""
    rl_rory "\"Told you! The soap!\""
    rl_miles "\"Sure.\""
    "He smiles. You don't notice the smile at all."
    vn_sfx "Clunk."
    "You lob the empty at the bin. In."
    rl_rory "\"THREE POINTS!\"" with vnfx("shake")
    hide miles
    "Imogen walks past, fishes it straight back out, and puts it in her bag."
    "She says nothing."
    show bg rl_lounge onlayer bgl
    show rory flushed at vn_pc_slot
    "Your nipples buzz all evening."
    "You rub them through your shirt in front of the telly and decide it's chafing."
    "It feels nice. You keep rubbing. Little circles."
    rl_rory "\"Mmh... hhn...\""
    "Your cock stirs in your shorts. You rub harder, mouth open—"
    "Until somebody walks past, and you pretend you're scratching."
    show rory shocked at vn_pc_slot
    rl_rory "\"Chafing! Bad chafing.\"\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(7)
    jump rl_blue_morning

label rl_blue_morning:
    ## rungs.twee: :: Redlightning Blue Morning [vn]
    $ rl.fit = "undies"
    ## Rung 2's morning: the chest lands. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ rl_land()
    $ vn_enter(bg="rl_bedroom", pc="grin", pc_tag="rory", cast=[], cg=None)
    hide miles
    show rory flushed at vn_pc_slot
    "You wake up because your nipples are buzzing."
    vn_sfx "Bzzzzt."
    "{color=#ff5fb8}{i}Buzzing{/i}. Swollen and electric, so sensitive that the sheet sliding off them makes you gasp out loud at the ceiling.{/color}"
    rl_rory "{color=#ff5fb8}\"Hah—!\"{/color}"
    "{color=#ff5fb8}You look down.{/color}"
    show rory shocked at vn_pc_slot
    "{color=#ff5fb8}There's a chest there. Not pecs. A {i}chest{/i}.{/color}"
    "{color=#ff5fb8}Two small soft handfuls sitting up on their own, nipples fat and pink and standing out like they want attention.{/color}"
    "{color=#ff5fb8}You grab one.{/color}"
    show rory flushed at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"Hhh— {i}oh{/i}—\"{/color}"
    vn_sfx "Zzzt."
    "{color=#ff5fb8}Straight down to your cock. You grab the other one to be fair. Same again.{/color}"
    "{color=#ff5fb8}You sit there squeezing for a while.{/color}"
    show cg rl_sa_bluemorning onlayer cgl
    "{color=#ff5fb8}Squeezing turns into kneading. Kneading turns into rolling your nipples between your fingers, flat on your back, hips lifting off the mattress.{/color}"
    rl_rory "{color=#ff5fb8}\"Hhh— {i}hhh{/i}— that's— okay, that's a LOT—\"{/color}"
    "{color=#ff5fb8}Your cock's hard in your boxers. You don't touch it. You don't need to.{/color}"
    "{color=#ff5fb8}You pinch both nipples at once and tug, and it goes down your spine like a starting gun.{/color}"
    rl_rory "{color=#ff5fb8}\"Oh— oh fuck— from my TITS? From my— {i}AH{/i}—\"{/color}"
    show cg rl_cum_bluemorning onlayer cgl
    vn_sfx "Bang." with vnfx("flash")
    "{color=#ff5fb8}You come in your boxers, flat on your back, hands full of your own chest, mouth open, heels drumming the bed.{/color}"
    show rory grin at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"...Best alarm clock EVER.\"{/color}"
    "{color=#ff5fb8}You lie there panting at the ceiling.{/color}"
    hide cg onlayer cgl
    "{color=#ff5fb8}Waist: in. Arse: rounder. It fills your palm when you slap it.{/color}"
    vn_sfx "Smack."
    "{color=#ff5fb8}It {i}jiggles{/i}. You slap it again just to watch.{/color}"
    rl_rory "{color=#ff5fb8}\"HA! Look at THAT—\"{/color}"
    "{color=#ff5fb8}Your hair flops in your eyes. Longer than yesterday, a red mop past your ears.{/color}"
    "{color=#ff5fb8}And the front of your boxers looks... tidier. Less going on down there.{/color}"
    "{color=#ff5fb8}You shove a hand in. Smaller. Still hard, mind, and so sensitive you squeal.{/color}"
    show rory flushed at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"Eep—! ...Less drag.\"{/color}"
    show rory grin at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"{i}Hhn{/i}— aerodynamic.\"{/color}"
    $ _rl_feel = rl_take_feel()
    if _rl_feel:
        "{color=#e40081}[_rl_feel]{/color}"
    "You stand at the mirror with a tit in each hand, grinning at yourself."
    "Your voice has crept up half a note overnight. It hasn't got one bit quieter."
    rl_rory "\"Laundry's shrinking everything except where it counts.\""
    show bg rl_locker onlayer bgl
    show rory grin at vn_pc_slot
    "At the track there's a top in your locker with a sticky note on it."
    "FOR SUPPORT. Roxy's handwriting."
    "Squad red. Thick and snug, and there's something moulded inside the front you don't look at too hard."
    "You pull it on in the changing room. It squeezes everything up and together and holds it there."
    "It feels {i}great{/i}."
    rl_rory "\"CHEERS, CALDER!\"" with vnfx("shake")
    "You yell it across the infield and slap your own chest."
    vn_sfx "Boing."
    "She salutes you with two fingers and doesn't stop laughing for ages.\n{size=-5}{color=#ff8fa3}▸ Train all afternoon in it{/color}{/size}"
    $ vn_until(17)
    jump rl_blue_locker

label rl_blue_locker:
    ## rungs.twee: :: Redlightning Blue Locker [vn]
    $ rl.fit = None
    ## Rung 2's second day: the afternoon's session was this one (Redlightning.useSession), so rung 3 is tomorrow's. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ rl.session_day = vn_clock.day
    $ vn_enter(bg="rl_locker", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "Locker room after. Steam. Shouting. Deep heat and somebody's criminal body spray."
    "You've trained all afternoon in Roxy's top and you're dripping."
    "You grab the hem and peel."
    "It sticks. It drags. It catches on your nipples on the way up—"
    show rory flushed at vn_pc_slot
    rl_rory "\"AH— ah— {i}hhh{/i}—\""
    $ rl.fit = "undies"
    "—and then it pops off over your head, and everything comes with it."
    vn_sfx "Boing."
    "Two soft round handfuls bounce free in the middle of the locker room. Pink. Flushed. Shiny with sweat. Nipples standing straight out at the room."
    vn_sfx "Thunk."
    "Everyone looks. Lenny drops a shoe."
    rl_roxy "\"Whoa. Lightning. Did you skip the gym and go straight to porn star?\""
    show rory grin at vn_pc_slot
    rl_rory "\"GAINS!\"" with vnfx("shake")
    "You grab them and jiggle."
    vn_sfx "Zzzt."
    "Your knees nearly go."
    show rory flushed at vn_pc_slot
    rl_rory "\"Hhn— god, they're sensitive. Anyone else's chest gone sensitive? Must be the laundry.\""
    rl_imogen "\"Nobody's laundry does that.\""
    "She's writing something down."
    show miles hungry at vn_cast_slot
    "Miles is on the far bench, half changed, frozen with his shirt in his hands."
    "Staring. Not annoyed. Not competitive. {i}Hungry{/i}."
    "You flex at him. Your tits wobble."
    show rory grin at vn_pc_slot
    rl_rory "\"Jealous, Thorne? One more of your funny drinks and you'll have a set too!\""
    "He doesn't answer."
    hide miles
    $ rl.fit = "tee"
    "You grab a fresh squad tee out of your bag and yank it on."
    "Wrong. Backwards, inside out, and somehow two sizes too small up top."
    "The neck catches your chin. The sleeves twist."
    "Your arms end up stuck straight up over your head, the shirt bunched round your wrists, your tits hoisted right out on show."
    show rory shocked at vn_pc_slot
    rl_rory "\"ACK. I'm stuck! I'm STUCK! Someone!\"" with vnfx("shake")
    vn_sfx "Tap. Tap. Tap."
    show cg rl_sa_locker onlayer cgl
    "Footsteps. Hands on your shoulders. Warm."
    show rory grin at vn_pc_slot
    rl_rory "\"Thorne! My hero! Get it off—\""
    "He takes hold of the bunched shirt. And he doesn't pull it off."
    "He {i}twists{/i} it, round your wrists, tight, and walks you forward until your back hits the lockers."
    vn_sfx "CLANG." with vnfx("shake")
    show rory shocked at vn_pc_slot
    rl_rory "\"Oi— OI— what's the—\""
    "You yank. Your arms don't move. He's got the whole knot of cotton in one fist, pinned over your head against the metal."
    rl_rory "\"Dogpile?! Is this a DOGPILE? That's two-on-one, that's not—\""
    rl_miles "\"Shut up.\""
    "Low. Not steady."
    "His free hand lands on your chest."
    vn_sfx "Zzzt."
    show rory flushed at vn_pc_slot
    rl_rory "\"HH—!\""
    "No brush. No accident. His palm, flat on your new tit, squeezing it like he's been waiting all session to."
    "His thumb finds your nipple and grinds it."
    rl_rory "\"AH— oi— that's a FOUL— no hands on the— {i}hah{/i}— that's— that's cheating, Thorne—!\""
    "You buck off the lockers to throw him." with vnfx("shake")
    "He leans in and puts his whole weight on you, and you go nowhere. Fastest man on the squad, and you can't shift him at all."
    show rory shocked at vn_pc_slot
    rl_rory "\"Get— get OFF— I'll have you, I swear I'll—\""
    "He switches hands. Pinches. Rolls. Kneads both handfuls, greedy, breathing hard against your ear while you thrash."
    show rory flushed at vn_pc_slot
    rl_rory "\"{i}Hhhnnn{/i}— stop— stop it, that's— they're all {i}raw{/i}, you can't just— {i}ahh{/i}—\""
    "Your hips jerk forward on their own."
    rl_rory "\"—t-tap out— I'm not tapping out— I'm NOT—\""
    rl_miles "\"Nobody asked you to.\""
    "Into your neck."
    "One hand leaves your chest. Slides down your side. Shoves into the back of your boxers."
    show rory shocked at vn_pc_slot
    rl_rory "\"WHOA— whoa whoa that's the BACK, Thorne, that's out of bounds—!\""
    "Bare palm on your bare arse. Squeezing. Kneading."
    "His fingers dip into the crease and stroke down, round, circling your hole. Pressing. Never in."
    "You twist to get away from it. It follows you."
    "You twist the other way, which grinds you straight back onto his fingers."
    show rory flushed at vn_pc_slot
    rl_rory "\"Oh— OH— okay that's— that's a dirty move— where'd you even {i}learn{/i}— {i}nngh{/i}—\""
    show rory shocked at vn_pc_slot
    rl_rory "\"Lenny! Roxy! He's cheating!\"" with vnfx("shake")
    rl_lenny "\"WOOOO!\""
    "Lenny just cheers. Roxy's phone is up. Nobody comes."
    show rory flushed at vn_pc_slot
    "Your cock's stiff and smaller than you remember, bumping the front of your boxers, leaking."
    "You're still fighting him. You think you're still fighting him. Your hips have stopped picking a side."
    rl_rory "\"I'm gonna— no— I'm NOT gonna— Thorne, don't you {i}dare{/i} make me— oh {i}FUCK{/i}—\""
    show cg rl_cum_locker onlayer cgl
    vn_sfx "Zzzt— POP." with vnfx("flash")
    "You come in your boxers. Hips bucking, back arched off the lockers, tits shoved into his hand."
    rl_rory "\"AAAAHHHHHH—!\""
    "One long loud wail bouncing off the tiles. Hot and wet and pulsing."
    "Your knees give. He holds you up by the knot of your own shirt."
    "Silence."
    rl_lenny "\"...Mate.\""
    "Very quietly."
    hide cg onlayer cgl
    show miles blush at vn_cast_slot
    "He lets go. You slide down the lockers onto your arse. Panting."
    show rory grin at vn_pc_slot
    "Grinning. Arms still stuck in the tee."
    rl_rory "\"Okay— okay, you win that one— {i}phew{/i}— cheap shot, mate, CHEAP. Whole body's tingling!\""
    "You wriggle your head free and beam up at him."
    rl_rory "\"Rematch. Relay. You and me. ATTACK FORMATION. Dibs on anchor!\"" with vnfx("shake")
    "Miles stares at you. Scarlet. His hand's shaking."
    hide miles
    "He turns and bolts for the showers."
    rl_rory "\"...Was it something I said?\""
    "You ask the room."
    menu:
        "Roxy is lying on the bench crying with laughter. Imogen has her face in her clipboard."
        "Go and demand your rematch":
            jump rl_blue_showers
        "Let him cool off":
            jump rl_hub

label rl_blue_showers:
    ## rungs.twee: :: Redlightning Blue Showers [vn]
    $ rl.fit = "undies"
    $ vn_enter(bg="rl_locker", pc="shocked", pc_tag="rory", cast=[("miles", "hungry")], cg=None)
    hide miles
    show rory grin at vn_pc_slot
    vn_sfx "Shhhhhhh."
    "Steam. One shower running."
    show miles hungry at vn_cast_slot
    "Miles is under it with both hands flat on the tiles and his head down."
    "His cock's hard and bobbing and he hasn't touched it."
    rl_rory "\"Thorne! You ran off! That was a cheap shot and I want my rematch—\""
    "He turns round. Looks at you, in your wet boxers, tits bouncing."
    "Something in his face just— goes."
    vn_sfx "Smack." with vnfx("shake")
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_showers_grab onlayer cgl
    "He grabs your wrist, yanks you in under the water and slams you into the tiles."
    show rory shocked at vn_pc_slot
    "Then he drags your hand down and wraps it round his cock, his fist clamped over yours."
    "Thick. Hot. Throbbing in your fist."
    rl_rory "\"Wh— Thorne— hey— let go of my—\""
    "You pull. He doesn't let you."
    "He pumps your own hand up and down him, root to tip, hard, and leans his forearm across your chest to keep you on the wall."
    rl_rory "\"Is this— is this a GRIP thing? Arm-wrestling? You can't just grab someone's hand and— that's not how you start a—\""
    rl_miles "\"You wanted a rematch.\""
    "Wrecked."
    rl_miles "\"Squeeze.\""
    show rory grin at vn_pc_slot
    rl_rory "\"...Oh, you're ON.\"\n{size=-5}{color=#ff8fa3}▸ Out-grip him{/color}{/size}"
    jump rl_blue_sex

label rl_blue_after:
    ## rungs.twee: :: Redlightning Blue After [vn]
    $ rl.fit = None
    $ vn_enter(bg=None, pc="grin", pc_tag="rory", cast=[], cg="rl_blue_climax")
    show rory flushed at vn_pc_slot
    if rl_enc.partner_came:
        "He comes over your fist and your stomach with a noise like he's been punched." with vnfx("flash")
        vn_sfx "Splt. Splt."
        "It runs down your belly under the shower."
    else:
        "He grabs your wrist and holds it still, shaking all over."
        "He comes anyway, in long throbs up your forearm." with vnfx("flash")
    "You don't let go."
    "You keep pumping him, slow, slippery, while he twitches and gasps and swears at the tiles."
    "You watch his face the whole time like it's a race replay."
    show rory grin at vn_pc_slot
    rl_rory "\"Oh, that's a good face. You should make that face at the finish line.\""
    "You beam at him through the steam."
    rl_rory "\"Good rep?\""
    rl_miles "\"You idiot.\""
    "Forehead on the tiles."
    rl_miles "\"Even now—\""
    rl_rory "\"Sounds like a challenge, mate. You know I never lose.\""
    jump rl_hub

label rl_green:
    ## rungs.twee: :: Redlightning Green [vn]
    $ rl.fit = None
    ## RUNG 3 -- the wipeout, the doctor, karaoke (margin: by a stride, called by you, flat on the tartan). Covert: the green bottle at the clinic, toasted to the quack; Imogen bans mystery drinks. That night the hoodie won't zip, and at the last key change you go down into his lap, know exactly what you've landed on, and grind it on purpose to a finish (authored: frottage has no director act). Body 3 lands overnight. VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(3)
    $ rl_kit()
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "Repeats. The honest ones. Too long to sprint, too short to settle."
    "The only way through is rhythm."
    "You don't have rhythm today."
    vn_sfx "Boing. Boing. Boing."
    "Your chest bounces on every stride, half a beat behind your legs, and Roxy's top can only do so much."
    "Your hips have started swinging, rolling your stride wide just when you need it narrow."
    "Third rep, back straight. The two arguments meet in the middle—"
    show cg rl_green_fall onlayer cgl
    "—and you go down tit-first on the tartan." with vnfx("shake")
    vn_sfx "SKRRRRT."
    "You skid on your front."
    vn_sfx "SMACK." with vnfx("shake")
    "Your chest slaps the track."
    "It doesn't hurt. It's the opposite of hurt. A white-hot jolt from your nipples straight down to your cock."
    show rory flushed at vn_pc_slot
    rl_rory "\"{i}Hhhnnnnnn{/i}...\""
    "You lie there face-down on the red rubber with your arse up in the air."
    hide cg onlayer cgl
    show rory grin at vn_pc_slot
    rl_rory "\"Slippy track! Track's SLIPPY!\""
    "You tell the sky, rolling over."
    "The track is not slippy."
    "Coach writes something down and says nothing at all, which from him is a shout."
    "Next rep. You get up. You go. Furious, filthy, laughing."
    "You come off the bend low and ugly and you will not, will not, WILL NOT lose—"
    show cg rl_green_starfish onlayer cgl
    "You cross first. Then you collapse flat on your back on the tartan, starfished, heaving, chest going up and down like the sea."
    rl_rory "\"BY A STRIDE! STILL GOT IT! BY A STRIIIIDE!\"" with vnfx("shake")
    "You yell it at the clouds."
    "Coach's shadow falls over you."
    rl_coach "\"Clinic.\""
    rl_coach "\"Now.\"\n{size=-5}{color=#ff8fa3}▸ Get dragged to the clinic{/color}{/size}"
    $ vn_pass(20)
    jump rl_clinic

label rl_clinic:
    ## rungs.twee: :: Redlightning Clinic [vn]
    $ rl.fit = None
    ## Rung 3's clinic: the quack, the green bottle, Imogen's ban. VN script (framework/vn-script.js).
    $ vn_enter(bg="rl_clinic", pc="grin", pc_tag="rory", cast=[("miles", "neutral")], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "Imogen marches you there by the wrist, at a pace that doesn't invite chat."
    "The sports clinic is a converted kit store at the back of the pavilion."
    "Filing cabinets. A dying pot plant. A beanbag. A poster about verrucas."
    vn_sfx "Squeeeak."
    "Dr. Marigold Fairweather spins round in her desk chair."
    "Sixty-one. Tie-dye lab coat. A cloud of grey frizz. A plastic giraffe dangling off her lanyard."
    rl_doc "\"Ooh! A runner! Sit, sit. Beanbag or table?\""
    rl_rory "\"Table!\""
    vn_sfx "Boing."
    "You hop up. Your tits bounce. She watches them bounce with professional delight."
    rl_imogen "\"Chest. Hips. He wiped out on the repeats because his chest is throwing his stride.\""
    "Imogen lays it out flat, because Imogen is the only one in the room who says things."
    rl_imogen "\"His skin's doing {i}that{/i}. All of it this month.\""
    "She points."
    "Fairweather listens with her chin in her hand. She puts the stethoscope on your earlobe."
    "Thinks about it. Moves it to the other earlobe."
    rl_doc "\"Any itching... in the antlers?\""
    rl_rory "\"Not yet, doc!\""
    rl_doc "\"Mm.\""
    "She taps the giraffe."
    rl_doc "\"There's a ley line under the stadium. Runs right under the home straight.\""
    rl_doc "\"Rhythmic footfall on a ley line stirs up the...\""
    "She waggles her fingers at you."
    rl_doc "\"Hormonal weather.\""
    "Imogen's face does something complicated."
    rl_rory "\"{i}Hormonal weather{/i}!\""
    "You repeat it, thrilled."
    rl_doc "\"Avoid left-handed magpies.\""
    "She's writing on a pad. You can see from here it's a doodle of a sun."
    rl_doc "\"Interpretive dance, facing magnetic north, whenever you feel a tingle in the chest. And above all—\""
    "She points the pen at you."
    rl_doc "\"—{i}hydrate{/i}.\""
    rl_rory "\"Doc, you're a national treasure.\""
    "Hand on your heart. On your boob."
    vn_sfx "Knock knock."
    show miles neutral at vn_cast_slot
    "A knock on the door frame. Miles. Holding a bottle."
    "Green. Virulent green. The green of something growing in a pipe."
    rl_miles "\"Thought you'd need this. Vitamin-enriched.\""
    "His eyes go to your chest."
    rl_miles "\"Doctor said fluids.\""
    rl_rory "\"She DID say fluids!\""
    "You grab it, twist the cap, and raise it to Fairweather."
    rl_rory "\"To hormonal weather!\"" with vnfx("shake")
    rl_doc "\"To hormonal weather!\""
    "She raises her mug."
    show cg rl_drink_green onlayer cgl
    vn_sfx "Glk glk glk glk."
    "Gone. Fizzing all the way down. Warm in your chest."
    show rory flushed at vn_pc_slot
    "Warm lower."
    hide cg onlayer cgl
    "Imogen takes the empty out of your hand. Very calmly."
    rl_imogen "\"No more mystery drinks.\""
    show rory grin at vn_pc_slot
    rl_rory "\"Imo! It's not a mystery! Thorne's are loaded with electrolytes!\""
    "Miles looks at the floor. Imogen looks at Miles."
    "The bottle goes in her bag.\n{size=-5}{color=#ff8fa3}▸ Karaoke tonight, the whole squad{/color}{/size}"
    $ vn_until(21)
    jump rl_karaoke

label rl_karaoke:
    ## rungs.twee: :: Redlightning Karaoke [vn]
    $ rl.fit = "redhoodie"
    $ vn_enter(bg="rl_karaoke", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    $ rl.fit = "redhoodie"
    show rory grin at vn_pc_slot
    hide miles
    "The squad hoodie won't zip."
    vn_sfx "Zzzip— zzzip— zzk."
    "You stand outside the karaoke bar yanking it. The zip climbs, and climbs, and stops dead halfway up your chest."
    "The teeth strain. Two soft round handfuls bulge out of the gap."
    rl_rory "\"Gains season!\""
    "You tell the street, and slap the zip. Everything wobbles."
    rl_roxy "\"One deep breath and that zip kills someone.\""
    "She's filming."
    "Inside. Neon. A booth the size of a bus. Cheap cider."
    "Coach at the far end by the taps, cap low, muttering about discipline. Lenny already wrestling a hurdler for the remote."
    show miles blush at vn_cast_slot
    "Miles slides in late, next to you. Pressed shirt. Pink cheeks."
    "When you lean across him for the remote, your boob squashes his elbow flat."
    "He doesn't move his elbow."
    "You get the remote. You get the mic. You stand on the seat."
    rl_rory "\"THORNE. You're my backing singer.\"" with vnfx("shake")
    rl_miles "\"I'm not—\""
    rl_rory "\"You ARE.\""
    menu:
        "You scroll. You pick:"
        "The power ballad with all the key changes":
            $ rl.song = "ballad"
            jump rl_karaoke_song
        "The one about driving all night with the top down":
            $ rl.song = "drive"
            jump rl_karaoke_song
        "The slow one everybody cries at":
            $ rl.song = "slow"
            jump rl_karaoke_song

label rl_karaoke_song:
    ## rungs.twee: :: Redlightning Karaoke Song [vn]
    $ rl.fit = "redhoodie"
    ## Rung 3's song: the lap, the grind. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="rl_karaoke", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    show miles blush at vn_cast_slot
    "You haul him onto the tiny stage by his collar."
    if rl.song == "drive":
        "Guitars. Big drums. A song about a car and a road and somebody's heart. Mostly the car."
        rl_rory "\"♪ DRIIIIVIN' ALL NIIIIGHT— ♪\""
        "You belt the first line so off-key the bar staff wince."
    elif rl.song == "slow":
        "Piano. Strings. The slow one. The whole bar groans."
        rl_rory "\"♪ And I— will ALWAAAYS— ♪\""
        "You sing it like it's the loudest song ever written. The way you sing it, it is."
    else:
        "Synths. Smoke machine. The power ballad with more key changes than sense."
        rl_rory "\"♪ TURN AROUND— ♪\""
        "You belt the first line at the whole bar, off-key, arms wide."
    "Chorus. You swing into his side, and your tits mash into his ribs and stay there."
    "He tries to sing harmony. He can't breathe."
    "His hands don't know where to go, so they clap, badly, trapped against all that softness."
    "Bridge. You spin. You catch your foot on the mic cable—"
    hide miles
    show cg rl_sa_karaoke onlayer cgl
    "—and go backwards, arse-first, straight down into his lap."
    vn_sfx "FWUMP." with vnfx("shake")
    "He catches you. His hands catch two full handfuls of tit through the gaping hoodie. And under your arse—"
    show rory shocked at vn_pc_slot
    "Hard. Thick. Twitching. Right up the crease of your shorts."
    "You try to bounce straight back up. You don't get to."
    "His arms lock round your waist. He hauls you back down, hard, and holds you there."
    rl_rory "\"Is that— HA!\""
    "You twist round, mic still in your fist."
    rl_rory "\"THORNE! Let me UP, you're cheating— this is a SOLO, you can't tackle the lead singer—\""
    rl_miles "\"Sing.\""
    "Into your back."
    rl_rory "\"I— let GO—\""
    "You shove at his arms. They're iron. The whole bar thinks it's a bit and cheers."
    show rory grin at vn_pc_slot
    rl_rory "\"Fine! FINE! You want a sing-off? Last key change, mate! Loser buys the round!\""
    "His hands slide up into the gaping hoodie and grab two full handfuls of tit. Squeeze."
    show rory flushed at vn_pc_slot
    rl_rory "\"OI— hands! Hands in the— that's a {i}foul{/i}, that's— {i}ahh{/i}—\""
    "And he grinds you."
    vn_sfx "Grind. Grind. Grind."
    "Slow and deep. He drags your hips back and forth down the whole length of him to the beat, throbbing every time he pulls you over it."
    "You try to stand. He yanks you down. You try to twist off sideways. He rolls you right back on."
    "Your tits are in his fists and you're still singing. Badly. Loudly. Into the mic."
    vn_th "(Because you are NOT losing a sing-off.)"
    rl_rory "\"You okay back there, Thorne?\""
    "You pant it into the mic, and the bar howls."
    rl_miles "\"Shut up and sing.\""
    rl_rory "\"Ohh— the lyrics have gone— stop— stop {i}moving{/i} me, I can't— {i}oh{/i}, that's— why is that GOOD—\""
    "His hips jerk up into you. He drags you down harder."
    "Your cock's stiff and small and rubbing the inside of your shorts on every roll, and his thumbs find your nipples through the hoodie."
    "You've stopped fighting the hips. You're riding it to the drums. And that's it—"
    vn_sfx "KEY CHANGE." with vnfx("shake")
    show cg rl_cum_karaoke onlayer cgl
    rl_rory "\"{i}AAAAAHHHH—{/i}\"" with vnfx("flash")
    "Not singing any more. Coming. Arched back over him, arse ground down hard on his cock where he's holding it."
    "Wailing into the mic at full volume while your shorts go hot and wet."
    vn_sfx "BANG."
    "The bar goes absolutely mental."
    "Under you he jerks, and grunts, and you feel him throb and go hot through two layers of shorts."
    rl_lenny "\"[rl_NICK]! BUY HIM DINNER FIRST!\"" with vnfx("shake")
    "He's on the table."
    hide cg onlayer cgl
    show rory grin at vn_pc_slot
    "The song ends. You stand up. You bow. You haul Miles up by the hand."
    rl_rory "\"Best duet partner EVER!\""
    rl_imogen "\"NO uploads.\""
    "Imogen vaults the booth, snatches Roxy's phone and pockets it."
    "Miles spends the rest of the night standing behind Lenny, holding a menu in front of his crotch."
    show miles hungry at vn_cast_slot
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_doorway_kiss onlayer cgl
    "On the walk home he catches your wrist, shoves you back into a shop doorway, and kisses you."
    "Hard. No warning. Both hands on your arse, hauling you up against him, his cock still half-hard against your hip through the wet shorts."
    show rory flushed at vn_pc_slot
    rl_rory "\"Mmf— Thorne— {i}mmh{/i}—\""
    "You shove his chest. He doesn't budge."
    "So you kiss him back like it's a race, because if it's a race you're winning it."
    rl_rory "\"Is this— is this a team thing?\""
    "You gasp it into his mouth."
    rl_miles "\"Yes.\""
    "He lies."
    show rory grin at vn_pc_slot
    rl_rory "\"BRILLIANT.\""
    "You grab his face and kiss him again."
    rl_lenny "\"GET A ROOM!\"\n{size=-5}{color=#ff8fa3}▸ Stagger home{/color}{/size}"
    call vn_night(7)
    jump rl_morning

label rl_orange:
    ## rungs.twee: :: Redlightning Orange [vn]
    $ rl.fit = None
    ## RUNG 4 -- discovery: mandatory, no opt-out (margin: by a step, Imogen). Coach orders the sports bra; the rumour mill in the lounge; Lenny asks for a bottle and Miles says no too fast; Imogen shows you the shelf. You get it in one look. Then flavour: Tell him or Keep it quiet, and both drink the orange, the first one you ask for (Redlightning Shelf). The `told` flag picks the route_end id. The evening's partner stretches; optional director: your mouth on him. VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(4)
    $ rl_kit()
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_lounge", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "Coach meets you at the gate and shoves a sports bra into your hands without looking at you."
    rl_coach "\"Orders. Can't have my ace going down tit-first on the home bend.\""
    rl_rory "\"Yes, COACH!\"" with vnfx("shake")
    "You put it on under the tank top right there. It's a fight."
    "You win. Just."
    "The session sprint."
    vn_sfx "Bounce. Swing. Clap."
    "Your tits bounce, your arse swings, your thighs clap, and you throw yourself at the line and just about get there first."
    rl_imogen "\"By a step.\""
    "She isn't watching the finish. She's watching Miles."
    "She's been watching Miles all week."
    show bg rl_lounge onlayer bgl
    "The lounge after. Sofas held together with tape. Ramen cups."
    "The rumour mill, running faster than you ever did."
    rl_roxy "\"Wider hips than any of the hurdlers. I'm just {i}saying{/i}.\""
    rl_lenny "\"Has anyone seen his bulge lately? Is it on holiday?\""
    rl_unk "\"Aliens.\""
    rl_unk "\"I heard he's growing BOOBS.\""
    "That one's a hurdler."
    vn_sfx "BANG." with vnfx("shake")
    "You kick the door open."
    rl_rory "\"I HEARD THAT.\""
    "Silence."
    rl_roxy "\"Settle it, then.\""
    show cg rl_orange_reveal onlayer cgl
    "You haul your shirt up to your neck."
    "Coach's sports bra, straining, two big soft tits crammed into it and spilling over the top."
    vn_sfx "Boing. Boing."
    "You bounce them."
    rl_rory "\"SPORTS BRA! For CHAFING. Coach's orders! That's GAINS, lads.\"" with vnfx("shake")
    vn_sfx "Smack."
    "You spin round and slap your own arse. It wobbles for a while after your hand's gone."
    rl_rory "\"And THAT'S squats.\""
    rl_lenny "\"That's not squats.\""
    "Faintly."
    rl_rory "\"Feel it, then! Solid muscle!\""
    "You grab his wrist and plant his hand on your arse cheek. He squeezes. His eyes go wide."
    rl_rory "\"See? SOLID.\""
    rl_lenny "\"That's— not— {i}solid{/i}—\""
    hide cg onlayer cgl
    vn_sfx "THWAP." with vnfx("shake")
    "Roxy snaps your bra strap."
    show rory shocked at vn_pc_slot
    rl_rory "\"OI! Calder!\""
    show cg rl_orange_hip onlayer cgl
    "And then there's a hand on your hip. Warm. Firm. Staying."
    "Miles. He's slid in beside you out of nowhere, thumb hooked in your waistband."
    "He isn't looking at you. He's looking at Lenny's hand on your arse."
    "Lenny takes his hand back very fast."
    rl_miles "\"It's a supplement. L-carnitine. BCAAs. I drink it too.\""
    rl_lenny "\"Then I want some. Give us a bottle, Thorne. Team spirit.\""
    rl_miles "\"No.\""
    hide cg onlayer cgl
    show miles blush at vn_cast_slot
    "Too fast. Way too fast. The whole room hears how fast."
    "Imogen stands up."
    rl_imogen "\"Kit store.\""
    "She says it to you."
    rl_imogen "\"Now.\"\n{size=-5}{color=#ff8fa3}▸ Follow her to the kit store{/color}{/size}"
    jump rl_shelf

label rl_shelf:
    ## rungs.twee: :: Redlightning Shelf [vn]
    $ rl.fit = None
    $ rl.knows = True
    $ vn_enter(bg="rl_kitstore", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "The kit store. Hurdles stacked against the wall. Starting blocks in a crate. Old rubber and deep heat."
    vn_sfx "Thunk."
    "Imogen shuts the door with her foot and points at a shelf."
    show cg rl_shelf onlayer cgl
    "On it, in a neat row, rinsed out, in order: every bottle he's ever handed you."
    "Pink. Blue. Green."
    "And in front of each one, something of yours."
    "In front of the pink: your razor, still in its washbag. Clean. Never used again."
    "In front of the blue: a squad tee, split down both side seams under the arms."
    "In front of the green: the hoodie, its zip burst clean out of the teeth."
    "That's all. Imogen doesn't say a word."
    "She folds her arms and waits for you to look."
    "You look."
    hide cg onlayer cgl
    show rory shocked at vn_pc_slot
    "It takes one second."
    "The bottle, then the next morning. The bottle, then the next morning. Every time."
    rl_rory "\"He's been trying to slow me down.\""
    "Slowly."
    rl_rory "\"With these.\""
    "Imogen nods."
    show cg rl_shelf_grin onlayer cgl
    "A grin starts. It spreads. It takes over your whole face."
    show rory grin at vn_pc_slot
    rl_rory "\"And I'm still WINNING.\"" with vnfx("shake")
    rl_imogen "\"That's— that's what you've taken from this?\""
    rl_rory "\"Imo! He's been SPIKING me! For WEEKS! To slow me DOWN!\""
    "You're laughing. You pick up the green empty and shake it at her."
    rl_rory "\"And I've won every single race! Every one! By less every time, fine, but EVERY ONE!\""
    rl_imogen "\"You're not angry.\""
    rl_rory "\"Angry? He's been working so HARD.\""
    "You put the bottle back in its place, very carefully, in the row."
    rl_rory "\"Where's the next one?\""
    hide cg onlayer cgl
    "Imogen closes her eyes."
    rl_imogen "\"His bag.\""
    menu:
        rl_imogen "\"It's orange.\""
        "Tell him" (ending=True):
            $ rl.told = True
            jump rl_orange_tell
        "Keep it quiet" (ending=True):
            $ rl.told = False
            jump rl_orange_quiet

label rl_orange_tell:
    ## rungs.twee: :: Redlightning Orange Tell [vn]
    $ rl.fit = None
    $ vn_enter(bg="rl_lounge", pc="grin", pc_tag="rory", cast=[("miles", "hungry")], cg=None)
    show rory grin at vn_pc_slot
    show miles neutral at vn_cast_slot
    "You march back into the lounge. Miles is on the sofa. His bag's at his feet."
    vn_sfx "Zzzzip."
    "You unzip it in front of everybody and take out the bottle."
    "Orange. Traffic-cone orange, glowing, fizzing."
    "He goes very, very still."
    vn_sfx "Krk."
    "You twist the cap off."
    show cg rl_drink_orange onlayer cgl
    "You look him dead in the eye. And you drink it."
    vn_sfx "Glk glk glk glk."
    "One go. You don't look away once."
    "You lower the empty. Wipe your mouth on your wrist. Grin."
    rl_rory "\"Next colour?\""
    hide cg onlayer cgl
    $ vn_face("miles", "blush")
    "Miles has stopped breathing."
    rl_miles "\"I— that's— how long have you—\""
    rl_rory "\"Kit store. Imo's got a shelf.\""
    "You flop down next to him, tits bouncing, and bump his shoulder with yours."
    rl_rory "\"Genuinely brilliant scheme, mate. Didn't work, though.\""
    "You lean in."
    rl_rory "\"I'm still winning.\""
    "He looks at you like you've hit him with a car. Then at your chest. Then back up."
    $ vn_face("miles", "hungry")
    "Something in his eyes goes dark and hot and starving."
    rl_miles "\"You knew what it was. And you drank it anyway.\""
    rl_rory "\"Course I did. It's a CHALLENGE.\""
    vn_sfx "CLINK-RATTLE." with vnfx("shake")
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_trophy_kiss onlayer cgl
    "He grabs your wrist, hauls you out into the corridor, pins you against the trophy cabinet, and kisses you so hard the cups rattle."
    show rory flushed at vn_pc_slot
    "His hands go straight up under your shirt. Both of them. Full of you."
    rl_rory "\"Mmh— Thorne— {i}mmh{/i}—\""
    "You kiss him back, grinning into it, pushing your chest into his palms."
    rl_rory "\"Is that a yes? To the next colour?\""
    rl_miles "\"That's a yes.\""
    "Against your mouth, squeezing until you moan."
    rl_rory "\"Ahhn—\""
    rl_miles "\"That's every yes.\"\n{size=-5}{color=#ff8fa3}▸ The empty locker room, later{/color}{/size}"
    $ vn_until(20)
    jump rl_stretches

label rl_orange_quiet:
    ## rungs.twee: :: Redlightning Orange Quiet [vn]
    $ rl.fit = None
    $ vn_enter(bg="rl_lounge", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show rory grin at vn_pc_slot
    show miles neutral at vn_cast_slot
    "You don't say a word."
    "You stroll back into the lounge and flop on the sofa next to him like nothing happened."
    rl_rory "\"Got anything for me, Thorne?\""
    vn_th "(First time you've ever asked.)"
    "He blinks. Then he unzips his bag and holds out a bottle."
    "Orange. Traffic-cone orange."
    rl_miles "\"Recovery. For the ace.\""
    "You take it from his hand, the way you always do."
    rl_rory "\"Cheers, mate.\""
    show cg rl_drink_orange onlayer cgl
    "And you drink it. One go."
    vn_sfx "Glk glk glk glk."
    "Watching him over the bottle the whole time."
    "He watches you swallow every drop. He has no idea you know. None."
    hide cg onlayer cgl
    $ vn_face("miles", "hungry")
    "You hand him back the empty with your biggest, dumbest smile."
    "He smiles back, relieved and hungry."
    "Behind him, Imogen puts her face in her hands."
    vn_th "(Best secret you've ever had.)\n{size=-5}{color=#ff8fa3}▸ The empty locker room, later{/color}{/size}"
    $ vn_until(20)
    jump rl_stretches

label rl_stretches:
    ## rungs.twee: :: Redlightning Stretches [vn]
    $ rl.fit = None
    ## Rung 4's evening: partner stretches. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="rl_locker", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    vn_sfx "Drip. Drip."
    "Late. The locker room's empty but for you, him, and a dripping shower."
    show miles neutral at vn_cast_slot
    "You sit on the mat, legs out, and reach for your toes."
    rl_rory "\"Push. Properly. You always push like I'm made of glass.\""
    "He kneels behind you. Hands on your back. He pushes like you're made of glass."
    rl_rory "\"HARDER. Come on.\""
    $ vn_face("miles", "hungry")
    "He leans his weight in. All of it."
    "You fold flat over your legs, and your tits squash down onto your own thighs, and he doesn't let up."
    "His chest on your back. His whole weight pinning you folded."
    show rory flushed at vn_pc_slot
    rl_rory "\"Oh— {i}ohh{/i}— okay— okay, that's deep enough— Thorne— that's enough—\""
    "He doesn't let up. The drag of the sports bra over your nipples makes you gasp out loud into your knees."
    rl_rory "\"I said— {i}hah{/i}— is this a contest? Who folds first? Because I'm not— I'm NOT folding—\""
    rl_miles "\"Then don't.\""
    hide miles
    "He hauls you back upright by the hips, straight into his lap. Your back to his chest. Your arse jammed down on him."
    "His arms lock round you before you can scoot off."
    if rl.told:
        rl_rory "\"Oi. You know I know about the bottles, Thorne. So you can stop pretending this is a—\""
        "You pant it, wriggling."
    else:
        show rory shocked at vn_pc_slot
        rl_rory "\"Oi— that's not a stretch— that's not a STRETCH, that's a hold—\""
    "His hands shove up under your shirt. Under the sports bra. Full handfuls. He groans into your neck."
    show rory shocked at vn_pc_slot
    rl_rory "\"HANDS— hands, that's— get your hands out of my—\""
    show cg rl_sa_stretches onlayer cgl
    "He shoves the bra up over your tits and they drop free, heavy, into his palms."
    "You grab his wrists to pull them off."
    "He bends his head round over your shoulder, and his mouth closes on your nipple."
    show rory flushed at vn_pc_slot
    rl_rory "\"HAH— {i}ahh{/i}— Thorne— that's— you can't BITE in a—\""
    vn_sfx "Suck. Lick."
    "Teeth. You grab his hair to drag his head off."
    "Your fist just— holds it there instead."
    rl_rory "\"S-stop— don't— {i}don't{/i}—\""
    "And under you: his cock. Hard as a bar through his shorts and yours, wedged up between your cheeks."
    "He hauls your hips back onto it and holds them there."
    rl_rory "\"Okay— OKAY— fine— you want to wrestle?\""
    "You try to buck him off, and buck right down onto his cock instead. He moans round your nipple."
    rl_rory "\"That's— that's a pin— that's not a fair pin—\""
    vn_sfx "Grind. Grind. Grind."
    "He's humping up into your arse through two pairs of shorts, mouth full of tit, both hands kneading, holding you down on him while you thrash."
    "Every thrash grinds you harder, faster, and you're calling it out loud like the home straight, because you don't know what else to call it—"
    rl_rory "\"No— no, he's— I'M— into the straight— {i}OHHH—{/i}\""
    show cg rl_cum_stretches onlayer cgl
    "You come grinding back on his cock, fist in his hair, his mouth sucking hard on your nipple." with vnfx("flash")
    vn_sfx "Zzzt— POP."
    "Long, shaking, loud, your little cock pulsing wet into your shorts."
    vn_sfx "BANG." with vnfx("shake")
    "The door bangs open."
    "Roxy. Kit bag. Frozen."
    "She sees it all: your tits out, his face in them, your arse in his lap."
    vn_sfx "Squeak!"
    "She U-turns so fast her trainers squeak."
    rl_roxy "\"I DIDN'T SEE A THING!\""
    vn_sfx "Slam."
    hide cg onlayer cgl
    show rory grin at vn_pc_slot
    show miles hungry at vn_cast_slot
    "You burst out laughing. He's panting into your chest."
    "He's still hard under you. He hasn't come."
    rl_rory "\"Ha— HA— you lost. You lost that, you're still— look at you, you didn't even finish—\""
    "He stands up, takes a fistful of your hair, and puts you on your knees on the mat."
    show rory shocked at vn_pc_slot
    rl_rory "\"OW— oi—!\""
    menu:
        rl_miles "\"Then I'll teach you to return the favour.\""
        "Kneel for him":
            jump rl_stretches_kneel
        "Twist free and hit the showers":
            call vn_night(7)
            jump rl_morning

label rl_stretches_kneel:
    ## rungs.twee: :: Redlightning Stretches Kneel [vn]
    $ rl.fit = None
    $ vn_enter(bg="rl_locker", pc="shocked", pc_tag="rory", cast=[("miles", "hungry")], cg=None)
    show rory shocked at vn_pc_slot
    show miles hungry at vn_cast_slot
    "Tits out. Bra rucked up round your collarbones. His fist in your hair."
    "He yanks his own waistband down."
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_kneel_slap onlayer cgl
    vn_sfx "Pap."
    "His cock springs out and slaps your cheek."
    rl_rory "\"Whoa— whoa, hang on, that's not— I didn't say I—\""
    "He drags your face onto it. The head pushes past your lips before you finish the word."
    rl_rory "\"Mmf— {i}MMF{/i}—!\""
    "You shove at his thighs. He holds your head still and rocks in, slow."
    show rory grin at vn_pc_slot
    "And somewhere in your head the competitive bit goes:"
    vn_th "({i}Oh. Endurance round.{/i})"
    "You glare up at him, mouth full. You are NOT tapping out first."
    rl_miles "\"Yes— Christ— {i}yes{/i}—\"\n{size=-5}{color=#ff8fa3}▸ Outlast him{/color}{/size}"
    jump rl_stretches_sex

label rl_stretches_after:
    ## rungs.twee: :: Redlightning Stretches After [vn]
    $ rl.fit = None
    $ vn_enter(bg=None, pc="grin", pc_tag="rory", cast=[], cg="rl_stretches_climax")
    show rory flushed at vn_pc_slot
    if rl_enc.partner_came:
        "He comes with his hand in your hair, hot and salty, all over your lips and chin." with vnfx("flash")
        "You lick, cough, swallow, and grin up at him with your chin wet."
    else:
        "He pulls out at the last second and comes across your tits instead, groaning, painting both of them." with vnfx("flash")
    show rory grin at vn_pc_slot
    "You sit back on your heels with your tits out and your mouth wet, and lick your lips. Thinking about it. Very seriously."
    rl_rory "\"Salty.\""
    rl_rory "\"Bit like the green one.\""
    "He makes a noise like a man falling down a staircase."
    rl_rory "\"How was that? Be honest. Was that a good rep?\""
    rl_miles "\"You idiot.\""
    "Staring down at you."
    rl_miles "\"Even now you're grinning.\""
    rl_rory "\"Sounds like a challenge. You know I never lose.\"\n{size=-5}{color=#ff8fa3}▸ Hit the showers and sleep it off{/color}{/size}"
    call vn_night(7)
    jump rl_morning

label rl_meet:
    ## rungs.twee: :: Redlightning Meet [vn]
    $ rl.fit = None
    ## RUNG 5 -- the big meet, then the shed (margin: by a chest, the announcer). Open: you take the pastel bottle before he offers. Roxy's verdict, the route's one cup letter. The gauntlet. At twilight by the equipment shed: the confession, best mates FOREVER, he snaps and takes you, it flips mid-scene, and the MANDATORY director scene: the first anal, against the shed wall. Body 5 lands overnight, in his bed. VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(5)
    $ rl_kit()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show bg rl_track onlayer bgl
    show rory grin at vn_pc_slot
    hide miles
    "The big meet."
    "The rival university's in matching navy. The bleachers are packed."
    "There's a journalist. There are cameras, and not one of them is pointed at the finish line."
    "Imogen's restitched your kit twice this week. It's losing anyway."
    "The tank top's a second skin across your tits. The cycle shorts have given up on your arse completely."
    "The walk to the blocks is a parade."
    "You wave at everyone. Everyone waves back."
    vn_sfx "Fwee-fwooo!"
    "Somebody whistles. You blow them a kiss."
    "Roxy circles you at the blocks with her head on one side."
    rl_roxy "\"That's an E.\""
    rl_roxy "\"That's an {i}E{/i}, Lightning.\""
    rl_rory "\"Is that good?\""
    rl_roxy "\"For a sprinter? It's a disaster.\""
    vn_sfx "Smack."
    "She slaps your arse."
    rl_roxy "\"Go get 'em.\""
    show miles blush at vn_cast_slot
    "Miles is at the next block, unzipping his bag."
    "Inside: a bottle. Pastel. Soft pink-lilac, like a sweet."
    "You reach in and take it before he can offer."
    "He freezes with his hand still in the bag."
    show cg rl_drink_lilac onlayer cgl
    "You crack it and drink it, one go, right there at the blocks in front of the cameras."
    vn_sfx "Glk glk glk glk."
    rl_rory "\"Ahh. Strawberry. Finally one that tastes nice.\""
    hide cg onlayer cgl
    "You hand him the empty."
    rl_rory "\"Cheers, mate.\""
    rl_unk "\"In lane four, the university's own— er— [rl_nick]!\""
    "That's the announcer."
    rl_unk "\"[rl_NICK]! [rl_NICK]!\"" with vnfx("shake")
    "The whole stand's chanting it."
    hide miles
    "You crouch into the blocks. Everything you've got squashes against your thighs."
    menu:
        "You yell down the track:"
        "\"WATCH THIS!\"":
            $ rl.yell = "watch"
            jump rl_meet_race
        "\"SEE YOU AT THE TAPE, THORNE!\"":
            $ rl.yell = "tape"
            jump rl_meet_race

label rl_meet_race:
    ## rungs.twee: :: Redlightning Meet Race [vn]
    $ rl.fit = None
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_track", pc="flushed", pc_tag="rory", cast=[("miles", "hungry")], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "Gun."
    vn_sfx "BANG." with vnfx("shake")
    "Everything goes. Everything."
    "Your tits go one way, your arse goes the other, your thighs clap, your hair whips your face."
    vn_sfx "Boing boing boing."
    "You run anyway. You've always run anyway."
    "Navy at one shoulder. Miles at the other."
    "Into the straight, the three of you dead level, and you throw yourself at the line chest-first—"
    "Photo finish."
    "The whole stadium holds its breath."
    vn_sfx "Bweep."
    "The board flashes."
    rl_unk "\"And the winner, by a chest— he— she— er— [rl_NICK]!\""
    "By a chest. Your chest crossed the line first. It's the only bit of you that could have."
    show rory flushed at vn_pc_slot
    "And the tape. The finish tape snapped tight across both your nipples at full speed, dragged, and let go."
    vn_sfx "ZZZT—"
    rl_rory "\"HNNNGH—!\""
    show cg rl_cum_meet onlayer cgl
    "Your knees go. You come in your shorts on the far side of the line, bent double, shaking, both arms wrapped round your tits." with vnfx("flash")
    vn_sfx "Bang. Bang. Bang."
    rl_rory "\"Ahh— AHHH— ahhhhh—\""
    "Moaning at the tartan, with the whole stadium on its feet for you."
    "Half the bleachers think you're crying with joy. You're thinking it's the best moment of your life."
    "It is."
    hide cg onlayer cgl
    show rory grin at vn_pc_slot
    if rl.yell == "tape":
        rl_rory "\"SAW YOU AT THE TAPE, THORNE!\"" with vnfx("shake")
    else:
        rl_rory "\"TOLD YOU! TOLD YOU TO WATCH!\""
    "You scream. You leap. You bounce. Everything bounces."
    "Then the gauntlet."
    "Roxy hits you first, face-first into your cleavage, screaming into it."
    show miles blush at vn_cast_slot
    "Miles next. You grab him and hug him so hard his face goes straight between your tits and stays there."
    rl_miles "\"Mmmf—\""
    "You don't let go. You squash him in tighter and rock him side to side."
    hide miles
    vn_sfx "SMACK." with vnfx("shake")
    "Lenny slaps your arse so hard it echoes."
    rl_lenny "\"LEGEND!\""
    rl_roxy "\"Mwah. For luck.\""
    "Roxy drops to a crouch and plants a big wet kiss on your arse cheek through your shorts."
    "And Imogen— Imogen, who has never once touched you— trips over a cone running across and lands in your arms."
    "A full-body hug, by accident. Her glasses steam up against your chest. She stands there frozen and fogged."
    rl_imogen "\"...Congratulations.\""
    "Muffled."
    "Then she backs away very carefully and spends ages cleaning her glasses."
    rl_rory "\"BY A CHEST! I WON BY A {i}CHEST{/i}!\"" with vnfx("shake")
    "You yell it at the sky."
    show miles hungry at vn_cast_slot
    "Across the infield, Miles has his hands on his knees."
    "He's looking at you like he's starving.\n{size=-5}{color=#ff8fa3}▸ Twilight, behind the equipment shed{/color}{/size}"
    $ vn_until(20)
    jump rl_shed

label rl_shed:
    ## rungs.twee: :: Redlightning Shed [vn]
    $ rl.fit = None
    ## Rung 5's confession and the snap. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="rl_track_dusk", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    vn_sfx "Clunk. ...Clunk. ...Clunk."
    "Twilight. The stadium lights clunking off one by one."
    "Behind the equipment shed the shadows are thick and warm."
    show miles neutral at vn_cast_slot
    "Miles is already there. Back to the wall. Hands jammed in his pockets."
    "A man walking to a gallows he built himself."
    if rl.told:
        "He knows you know. He's known since the orange bottle. Somehow that's worse for him."
        rl_miles "\"You've known. All this time. You drank them looking at me.\""
        rl_rory "\"Every one.\""
        rl_miles "\"{i}Why?{/i}\""
        rl_rory "\"Because you looked at me like THAT when I did.\""
        "You step in close. Your tits brush his chest."
        rl_rory "\"Go on. Say the thing. You've been building up to it for weeks.\""
    else:
        "You get there first."
        rl_rory "\"I've known since the kit store.\""
        rl_miles "\"You—\""
        "He goes white."
        rl_rory "\"Imo's got a shelf. Every bottle. In a row. Very tidy.\""
        "You grin."
        rl_rory "\"I kept drinking them, Thorne. I asked you for the orange one.\""
        "He stares at you like the ground's gone."
        rl_rory "\"Go on. Say the thing.\""
    "He takes a breath. It shakes."
    $ vn_face("miles", "blush")
    rl_miles "\"I like you.\""
    rl_miles "\"I want to be with you. Not as your rival. I want—\""
    "His jaw works."
    rl_miles "\"I want all of you.\""
    "Silence."
    "Your grin splits your face in half."
    vn_sfx "THUMP." with vnfx("shake")
    "You grab his arms and haul him into the biggest hug of your life. His back thumps the shed wall. Your tits squash flat against his chest."
    rl_rory "\"BEST MATES FOREVER!\"" with vnfx("shake")
    "Right into his ear."
    rl_miles "\"That's— not what I—\""
    rl_rory "\"BEST. MATES. {i}FOREVER.{/i}\"" with vnfx("shake")
    show miles hungry at vn_cast_slot
    rl_miles "\"God, you're dense.\""
    show cg rl_sa_shed onlayer cgl
    "And snaps."
    vn_sfx "WHAM." with vnfx("shake")
    "He spins you round and slams you face-first into the shed wall. The siding rattles."
    "His hand in your hair, holding your cheek to the boards. His mouth on your throat, biting."
    show rory shocked at vn_pc_slot
    rl_rory "\"OI— oi, what— wrestling move?! Now?!\""
    "You shove off the wall. He shoves you straight back into it."
    rl_rory "\"Thorne, I'm being NICE to you, I'm— that's a cheap— get OFF—\""
    rl_miles "\"It's not a—\""
    "He yanks your tank top down. Your tit springs out into the cold air and his hand clamps over it."
    show rory flushed at vn_pc_slot
    rl_rory "\"HANDS— no— {i}hahh{/i}— that's not— okay, okay, you want the rematch, fine, but not HERE—\""
    "He doesn't answer."
    "Both his hands drop to your arse. He shoves your cycle shorts down at the back and hikes you up onto your toes."
    "His fingers find your hole, slick with spit. Pressing."
    show rory shocked at vn_pc_slot
    rl_rory "\"WHOA— whoa whoa WHOA, that's— Thorne— that's NOT a legal—\""
    "One finger. In."
    show rory flushed at vn_pc_slot
    rl_rory "\"{i}HNNGH{/i}— out— take it out— {i}ohh{/i}—\""
    "You claw at the siding. You kick back at his shins, and he just leans his weight into you and pins your hips to the wall."
    "Fastest man on the squad. Can't move."
    rl_rory "\"This is— is this a FINALS thing? Is this how you— {i}ah{/i}—\""
    "Two. Stretching. Curling. Your tiny cock bounces against the boards, leaking, forgotten."
    "He crooks them. Something inside you lights up like the finish-line board."
    rl_rory "\"OH— oh, wh— what was— no— {i}no{/i}— don't do that again— don't—\""
    "He does it again. And again."
    vn_sfx "Creak. Creak. Creak."
    "You're still shoving back at him, still yelling, and every shove rides you down onto his hand, the siding creaking on every bounce."
    vn_sfx "Tap tap tap—"
    "Footsteps."
    "Imogen and Roxy, round the corner. Stopped dead."
    "They see it all: you pinned to the shed wall, tit out, shorts round your thighs, his fingers deep in your arse, you yelling."
    show rory shocked at vn_pc_slot
    rl_rory "\"IMO! ROXY! He's— he's CHEATING— get him OFF—\"" with vnfx("shake")
    rl_roxy "\"Is he seducing him or—\""
    rl_imogen "\"We are NOT seeing this.\""
    "Imogen hisses, and drags her away by the elbow."
    "Gone."
    "Miles pulls his fingers out. You sag against the wall, panting."
    vn_sfx "Shff."
    "You hear his shorts go."
    "Then something thick and hot and dripping nudges between your cheeks."
    rl_rory "\"Thorne. Thorne, mate. Wait. I didn't— I haven't even—\""
    "He turns you round, hoists you up the wall by your arse, and wraps your legs round his waist himself."
    "The fat head of his cock kisses your hole."
    rl_miles "\"You never wait for anything.\""
    "Into your mouth."
    rl_miles "\"Why should I?\"\n{size=-5}{color=#ff8fa3}▸ Fight him for it{/color}{/size}"
    jump rl_shed_sex

label rl_shed_after:
    ## rungs.twee: :: Redlightning Shed After [vn]
    $ rl.fit = None
    $ vn_enter(bg=None, pc="grin", pc_tag="rory", cast=[], cg="rl_shed_climax")
    show rory flushed at vn_pc_slot
    if rl_enc.partner_came:
        "He comes with his forehead on your shoulder, slamming you into the shed wall on every pulse." with vnfx("flash")
        vn_sfx "Throb. Throb. Throb."
        "You feel it. Hot. Throb after throb."
    else:
        "He stops buried to the root, shaking all over, and comes anyway without moving."
        "A slow, heavy pulse, deep inside you." with vnfx("flash")
    if rl_enc.pc_orgasms > 0:
        "You came too. Your tiny cock's still twitching between you, dribbling on his stomach."
        "Your arse is still squeezing him in little aftershocks."
    rl_miles "\"You idiot.\""
    "He gasps it into your neck."
    rl_miles "\"Even now—\""
    show rory grin at vn_pc_slot
    rl_rory "\"Best— celebration— EVER.\""
    "You pant it. Legs still locked round him. Sweat everywhere. Grinning."
    rl_rory "\"You really know how to celebrate a win, Thorne.\""
    rl_miles "\"If you won't get it with words, I'll show you.\""
    rl_miles "\"Every day. Until you do.\""
    rl_rory "\"Sounds like a challenge.\""
    vn_sfx "Mwah."
    "You kiss his nose."
    rl_rory "\"You know I never lose.\""
    "He laughs. It cracks in the middle. He doesn't put you down."
    "He carries you like that, still buried in you, two steps along the wall into the dark, and kisses you until you can't breathe."
    "You feel him start to soften inside you. Then, against all reason, not."
    show rory flushed at vn_pc_slot
    rl_rory "\"Again?\""
    "You whisper it into his mouth, thrilled, and squeeze him."
    rl_rory "\"Already?\""
    rl_miles "\"Not here.\""
    "Rough."
    rl_miles "\"Mine. Tonight. My room.\"\n{size=-5}{color=#ff8fa3}▸ His room, for the night{/color}{/size}"
    call vn_night(7)
    jump rl_shed_morning

label rl_shed_morning:
    ## rungs.twee: :: Redlightning Shed Morning [vn]
    $ rl.fit = "nude"
    ## Rung 5's morning, in his bed: body 5 lands. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ rl_land()
    $ vn_enter(bg="rl_miles_room", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    "You wake up in his bed."
    "He's asleep on his front, one arm thrown over you."
    "You wriggle out from under it and nearly fall off the mattress, because you've got a lot more to wriggle with than you had last night."
    "A {i}lot{/i} more."
    show rory shocked at vn_pc_slot
    "{color=#ff5fb8}Your tits are huge. They spill off your chest onto the sheet on either side.{/color}"
    "{color=#ff5fb8}Your hips are wider than any of the hurdlers'. Your arse juts. Your thighs are thick and soft and press together all the way up.{/color}"
    "{color=#ff5fb8}Your jaw's softer under your fingers. Your hair's past your shoulders, red, tangled all over his pillow.{/color}"
    "{color=#ff5fb8}You grab them. Both hands. They overflow your fingers and keep going, soft and heavy and hot.{/color}"
    show rory flushed at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"HOLY— {i}mmf{/i}—\"{/color}"
    "{color=#ff5fb8}You clap a hand over your mouth, because he's asleep, and squeeze with the other one anyway, and moan into your palm.{/color}"
    "{color=#ff5fb8}They're {i}massive{/i}. You jiggle them. They take forever to stop.{/color}"
    "{color=#ff5fb8}You reach round and grab your arse. A whole double handful, and still more of it.{/color}"
    rl_rory "{color=#ff5fb8}\"{i}Hhnn{/i}— ohh, that's so GOOD—\"{/color}"
    "{color=#ff5fb8}Between your legs: a tiny cock. Barely there. A little pink nub of a thing tucked up against you, smaller than last night.{/color}"
    "{color=#ff5fb8}You poke it. It barely twitches. Your arse clenches instead.{/color}"
    show rory grin at vn_pc_slot
    "{color=#ff5fb8}You find a rubber band on his desk and scrape the red up into a ponytail.{/color}"
    "{color=#ff5fb8}A sprinter's ponytail. It swings when you turn your head. You like it.{/color}"
    $ _rl_feel = rl_take_feel()
    if _rl_feel:
        "{color=#e40081}[_rl_feel]{/color}"
    show miles blush at vn_cast_slot
    "He wakes up. Looks at you. Doesn't say anything for a long time."
    rl_rory "\"Morning!\""
    "It comes out high and bright and louder than ever."
    rl_rory "\"He keeps changing the colour. I keep winning.\""
    hide miles
    "He pulls you back into bed."
    show cg rl_sa_spoon onlayer cgl
    "Spooned. His chest to your back. His cock, hard again, sliding up the crease of your arse, still slick from last night."
    show rory grin at vn_pc_slot
    rl_rory "\"Again? Go on, then. Slowly. I'm still full of you.\""
    show rory flushed at vn_pc_slot
    "He goes slowly. The fat head pushes in, and in."
    rl_rory "\"Mmmmnnh...\""
    "You moan into his pillow. He holds your tit in one hand like it's his, and rocks."
    vn_sfx "Shlk... shlk... shlk..."
    rl_rory "\"Mmh— {i}mmnh{/i}— Thorne— right there— {i}right{/i} there—\""
    "Your tiny cock bounces against the sheet on every stroke, dribbling. It's barely a cock any more. You don't care."
    "You push back onto him, grinding, and your hips find his rhythm before you do. You never practised that."
    "He groans into your ponytail and speeds up."
    rl_rory "\"Morning— session— best— one— YET—\""
    show cg rl_cum_spoon onlayer cgl
    "He comes deep in you with a long shudder. You come on his sheet, squeezing him, squeaking." with vnfx("flash")
    rl_rory "\"Eeeehhnn—!\""
    "Then he doesn't let you out till lunch."
    ## Visual-novel days: while the route runs, down to the track, where rung 6 (his "stay at mine tonight") is today's.
    "{size=-5}{color=#ff8fa3}▸ Down to the track, eventually{/color}{/size}"
    $ vn_pass(62)
    jump rl_hub

label rl_girlfriend:
    ## rungs.twee: :: Redlightning Girlfriend [vn]
    $ rl.fit = None
    ## RUNG 6 -- the girlfriend reveal, then the photo (margin: a dead heat, Imogen). No bottle, and there doesn't need to be. You wake in his bed; the squad declares you his girlfriend over two yogurts; "Will you be my girlfriend? For real?" / "Sure! Anything for my best mate. Keep up." In his room the last of it goes under his hands (Redlightning Girlfriend Room): cock to cunt in the lead-in, she/her from there, Remade. His mouth first, your first orgasm in the finished body; then him inside you, your first vaginal (director). VN script (framework/vn-script.js).
    $ rl_init()
    $ rl_advance(6)
    $ vn_enter(bg="rl_kitchen", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    show rory grin at vn_pc_slot
    hide miles
    show cg rl_gf_morning onlayer cgl
    "Sun through his curtains. Red hair all over his pillow. Silky. Shiny. Smelling of his shampoo."
    "You sit up and grab a fistful of it."
    rl_rory "\"Huh. Conditioner works if you use half the bottle!\""
    hide cg onlayer cgl
    show miles blush at vn_cast_slot
    "He's in the doorway with two mugs. He nearly drops both."
    vn_sfx "Knock knock BANG." with vnfx("shake")
    "Lenny's head round the door. His eyes go huge."
    "He spins on his heel and bellows down the corridor:"
    rl_lenny "\"OI! OIIIII! THORNE'S GIRLFRIEND IS UP!\"" with vnfx("shake")
    show bg rl_kitchen onlayer bgl
    hide miles
    "The squad kitchen. Everybody."
    "Imogen hands you a yogurt. You take two."
    rl_lenny "\"So you're definitely his girlfriend now. Right?\""
    "He points his spoon."
    rl_lenny "\"You stayed over. You've got—\""
    "He waves at all of you."
    rl_lenny "\"—{i}all of that{/i}.\""
    rl_rory "\"Girlfriend? HA! You lot are winding me up.\""
    "You laugh with your mouth full."
    show miles blush at vn_cast_slot
    "Under the table, a hand lands on your bare thigh. Miles, sitting down next to you. Close."
    show rory flushed at vn_pc_slot
    "His thumb strokes the soft inside of your thigh. Higher. Higher."
    rl_rory "\"Eep—!\""
    "You squeak into your yogurt."
    rl_lenny "\"You all right?\""
    show rory grin at vn_pc_slot
    rl_rory "\"Brilliant! Yogurt's brilliant!\""
    "Miles takes his hand back. He takes a breath."
    show cg rl_gf_ask onlayer cgl
    "He holds out his hand like he's asking you to dance."
    rl_miles "\"Will you be my girlfriend?\""
    rl_miles "\"For real?\""
    rl_rory "\"Sure!\""
    "Spoon in your mouth."
    rl_rory "\"Anything for my best mate.\""
    "You point the spoon at him."
    rl_rory "\"Keep up, though.\""
    hide cg onlayer cgl
    vn_sfx "WAAAAAHHH!" with vnfx("shake")
    "The kitchen explodes. Lenny on the table. Roxy whistling."
    "Imogen clapping, slowly, like she's just ticked the last box on a very long list."
    "Miles looks at you like you've handed him every medal you ever won.\n{size=-5}{color=#ff8fa3}▸ Back to his room{/color}{/size}"
    $ vn_pass(20)
    jump rl_girlfriend_room

label rl_girlfriend_room:
    ## rungs.twee: :: Redlightning Girlfriend Room [vn]
    $ rl.fit = "nude"
    ## Rung 6's change: cock to cunt under his hands, then his mouth. VN script (framework/vn-script.js); its scene-art lines are kept word for word. The three change frames are @cg cues. No vagina wording before <<pcAnatomyShift>> (verify-redlightning).
    $ vn_enter(bg="rl_miles_room", pc="grin", pc_tag="rory", cast=[], cg=None)
    show rory grin at vn_pc_slot
    show miles hungry at vn_cast_slot
    vn_sfx "Click."
    "He shuts the door. His hands on your waist."
    rl_rory "\"Last one undressed buys—\""
    "He's already peeling your top off."
    vn_sfx "Boing."
    "Your tits drop free, huge, bouncing, slapping softly together."
    hide miles
    "He sinks to his knees. Thumbs in your cycle shorts."
    "He tugs them down past your hips, slow, slow—"
    "—and stops."
    rl_rory "\"Something wrong?\""
    show rory flushed at vn_pc_slot
    show cg rl_tf_melt onlayer cgl
    "{color=#ff5fb8}Something's happening. Warm. Melting. Under his hands.{/color}"
    "{color=#ff5fb8}That tiny nub of a cock goes soft, then softer, then it's drawing back, sinking into you, and your balls tuck up after it and they're gone and—{/color}"
    if not rl.shifted:
        $ rl.shifted = True
        $ rl.sex = "f"
        $ rl.feel_pending = 6
        $ rl.landed = 6
    "{color=#ff5fb8}—and you {i}open{/i}.{/color}" with vnfx("flash")
    "{color=#ff5fb8}Two soft, puffy lips, pink, parting on their own, slick and hot. A little nub at the top, throbbing once, hard.{/color}"
    "{color=#ff5fb8}It doesn't feel like losing anything. It feels like a pop of warmth right in your middle, like the moment the gun goes.{/color}"
    "{color=#ff5fb8}Then wet, wet, {i}wet{/i}, slick running down the inside of your thigh while he stares.{/color}"
    rl_rory "{color=#ff5fb8}\"Hhh— {i}ohh{/i}— what's— that's— {i}tingly{/i}—\"{/color}"
    show cg rl_tf_bloom onlayer cgl
    "{color=#ff5fb8}And everything else goes with it.{/color}"
    "{color=#ff5fb8}Your tits swell heavier in his face. Your hips spread under his palms. Your arse rounds out behind you. Your waist pulls in tight.{/color}"
    "{color=#ff5fb8}Your face goes soft. Your hair slithers loose of the band and down your back, long and silky and red, past your shoulder blades.{/color}"
    show rory shocked at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"Oh!\"{/color}"
    "{color=#ff5fb8}It comes out higher, rounder, sweeter—{/color}"
    rl_rory "{color=#ff5fb8}\"OH!\"{/color}" with vnfx("shake")
    "{color=#ff5fb8}—and exactly as loud.{/color}"
    show cg rl_tf_pussy onlayer cgl
    "{color=#ff5fb8}You poke the place your cock used to be.{/color}"
    vn_sfx "Squish."
    "{color=#ff5fb8}Your new pussy squishes.{/color}"
    show rory grin at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"Guess THAT'S new!\"{/color}"
    "{color=#ff5fb8}You grin down at him.{/color}"
    rl_rory "{color=#ff5fb8}\"Supplements working OVERTIME!\"{/color}" with vnfx("shake")
    "{color=#ff5fb8}You grab your tits. Both hands. They're heavier than this morning, way heavier, spilling over your wrists, and they wobble for ages when you let go.{/color}"
    show rory flushed at vn_pc_slot
    rl_rory "{color=#ff5fb8}\"THORNE— look at them— they're {i}HUGE{/i}— {i}ahh{/i}—\"{/color}"
    "{color=#ff5fb8}You squeeze, and moan, and squeeze again.{/color}"
    "{color=#ff5fb8}You twist round to see your arse and it's rounder, softer, jiggling every time you breathe.{/color}"
    rl_rory "{color=#ff5fb8}\"Everything's MORE— everything's SO much more—\"{/color}"
    $ _rl_feel = rl_take_feel()
    if _rl_feel:
        "{color=#e40081}[_rl_feel]{/color}"
    "He makes a sound that's half laugh, half sob. His thumbs part you. He stares."
    rl_miles "\"I've wanted— I want {i}you{/i}.\""
    show rory grin at vn_pc_slot
    rl_rory "\"Teamwork, mate.\""
    "Hands on his shoulders."
    rl_rory "\"Go on, then.\""
    show cg rl_sa_girlfriend onlayer cgl
    "His tongue. Flat and wet, up the whole length of your new slit."
    show rory flushed at vn_pc_slot
    rl_rory "\"AH— HAH— oh that's WEIRD— good weird— GOOD WEIRD—\""
    vn_sfx "Shlp."
    "He finds your clit. Flicks it. Sucks it."
    "Your knees buckle. Your fingers knot in his hair."
    "You grind your brand-new cunt on his face, chasing it, clumsy as any new drill, shouting the whole time."
    rl_rory "\"More— MORE— there— THERE— oh god, it's coming from— from {i}inside{/i}— it's—\""
    vn_sfx "BANG." with vnfx("shake")
    show cg rl_cum_girlfriend onlayer cgl
    "The starting gun goes off inside you." with vnfx("flash")
    "Your hips slam forward. Your thighs clamp his head."
    rl_rory "\"AAAAAAHHHHHH—!\""
    "You scream at his ceiling. Your first one in this body, and it doesn't stop."
    "Wave after wave rolling out of you to your fingertips and your curling toes, your pussy pulsing on his tongue."
    hide cg onlayer cgl
    show miles hungry at vn_cast_slot
    "You collapse back onto his bed, hair fanned out, flushed, wild-eyed."
    rl_rory "\"Best protein I ever took...\""
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_gf_climb onlayer cgl
    "He climbs up over you, shoving his shorts down. His cock's hard and dripping."
    "He settles between your thighs. The head nudges your soaked new lips. His eyes on yours."
    rl_miles "\"Can I—\""
    show rory grin at vn_pc_slot
    rl_rory "\"Show me that finish-line speed.\""
    "Then, for the first time:"
    rl_rory "\"Miles.\""
    "He hears it.\n{size=-5}{color=#ff8fa3}▸ Pull him in{/color}{/size}"
    jump rl_girlfriend_sex

label rl_girlfriend_after:
    ## rungs.twee: :: Redlightning Girlfriend After [vn]
    $ rl.fit = None
    $ vn_enter(bg=None, pc="grin", pc_tag="rory", cast=[], cg="rl_girlfriend_climax")
    show rory flushed at vn_pc_slot
    if rl_enc.partner_came:
        "He comes groaning your name into your hair, hips jammed tight to yours, in long heavy throbs until he's got nothing left." with vnfx("flash")
    else:
        "He stops deep inside you, forehead on yours."
        "He comes without moving, slow and heavy, both of you shaking." with vnfx("flash")
    if rl_enc.pc_orgasms > 0:
        "You came again round him. Your new pussy's still squeezing him, little greedy flutters."
        "You're laughing breathlessly at the ceiling."
    rl_miles "\"Your hips know it already.\""
    "Wrecked."
    rl_miles "\"How do they know it already?\""
    "They do. Up, down, squeeze. First time, and you're {i}good{/i} at it."
    show rory grin at vn_pc_slot
    rl_rory "\"Natural talent, mate.\""
    rl_rory "\"Two in one morning. That's a PERSONAL BEST.\""
    rl_miles "\"You idiot.\""
    vn_sfx "Mwah."
    "He kisses you."
    rl_miles "\"My idiot.\""
    "He doesn't pull out. He rolls you on top of him, still inside you."
    "You sit up on him with his hands on your hips and your tits swaying over his face, and rock. Lazy. Just to feel it."
    vn_sfx "Shlk. Shlk."
    "He groans. You grin."
    rl_rory "\"Cool-down lap. Coach says always do your cool-down.\""
    vn_sfx "Bang bang." with vnfx("shake")
    rl_roxy "\"Practice in ten, lovebirds! Team photo!\""
    "Through the door.\n{size=-5}{color=#ff8fa3}▸ The team photo{/color}{/size}"
    $ vn_pass(20)
    jump rl_photo

label rl_photo:
    ## rungs.twee: :: Redlightning Photo [vn]
    $ rl.fit = "greyhoodie"
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "blush")], cg=None)
    $ rl.fit = "greyhoodie"
    show rory grin at vn_pc_slot
    hide miles
    "You walk down to the track in his hoodie."
    "It's huge on him. On you it stops at your hips and stretches across your tits like a drum."
    "Your ponytail swings. Your thighs brush. Every step's brand new."
    "Coach looks you up and down. All of you. For a long time."
    rl_coach "\"Girlfriend, huh. That's your business.\""
    rl_coach "\"Sports bra next time, or it's extra laps.\""
    rl_rory "\"Already on, Coach!\""
    "The team photo. The whole squad on the bleachers."
    "Sprinters, hurdlers, Lenny with a foam finger, Roxy pulling faces, Imogen handing out combs."
    show miles blush at vn_cast_slot
    "You dead centre. Miles beside you, his hand on your thigh."
    rl_unk "\"Big smiles! Ace, what are you doing?\""
    menu:
        "That's the photographer."
        "Flex both arms, like always":
            $ rl.pose = "flex"
            jump rl_photo_pose
        "Arm round Miles, cheek squashed to his":
            $ rl.pose = "arm"
            jump rl_photo_pose
        "Hands on your hips, chest out":
            $ rl.pose = "chest"
            jump rl_photo_pose

label rl_photo_pose:
    ## rungs.twee: :: Redlightning Photo Pose [vn]
    $ rl.fit = "greyhoodie"
    $ vn_enter(bg="rl_track", pc="flushed", pc_tag="rory", cast=[("miles", "hungry")], cg=None)
    show rory flushed at vn_pc_slot
    if rl.pose == "arm":
        show cg rl_photo_arm onlayer cgl
        "You throw an arm round Miles's neck and squash your cheek against his."
        "He goes red. You grin so hard your eyes shut."
    elif rl.pose == "chest":
        show cg rl_photo_chest onlayer cgl
        "Hands on your hips. Chest out."
        vn_sfx "Rrrip."
        "The hoodie gives up a zip's worth of seam somewhere. The photographer has to start again twice."
    else:
        show cg rl_photo_flex onlayer cgl
        "Both arms up. Biceps. Same as every photo since you were nineteen."
        "Everything under the hoodie bounces when you flex. The squad cheers."
    vn_sfx "Click. Click. Click."
    hide cg onlayer cgl
    show rory grin at vn_pc_slot
    show miles neutral at vn_cast_slot
    "Everyone piles off the bleachers. Miles catches your hand and pulls you aside. Serious."
    rl_miles "\"Can I ask?\""
    rl_miles "\"Are you really okay with this?\""
    rl_rory "\"With what? Us?\""
    "You laugh."
    rl_rory "\"You're such a sap. We're rivals. We're best mates. And now everyone says we're dating, which is hilarious—\""
    rl_rory "\"—because it means we've got the best teamwork EVER. Nobody's beating us. Not at running. Not at being weird.\""
    rl_miles "\"I mean with me. With what I—\""
    "You shrug."
    rl_rory "\"You've always been the best bit of getting faster. If you want me around, that's your own fault.\""
    "He laughs. Then he doesn't."
    show miles blush at vn_cast_slot
    rl_miles "\"Whatever shape you are, you're mine.\""
    rl_miles "\"All of them.\""
    rl_rory "\"Then you'd better keep up.\""
    "You walk the long way round the field together, behind the far bleachers. Long grass and cicadas."
    "You stop. Tug at the hoodie."
    rl_rory "\"Hey— can you help with this strap? It's halfway to my ear.\""
    "He steps in. You catch his hand and plant it, flat and broad, right on your tit."
    rl_rory "\"There. See? I can never get it straight.\""
    rl_miles "\"That's not a strap.\""
    "Faintly."
    show rory flushed at vn_pc_slot
    rl_rory "\"Are you fixing it or not?\""
    "You shift his hand so his thumb drags over your nipple. Your breath hitches."
    rl_rory "\"Ooh. Yeah. Fix it more.\""
    $ vn_face("miles", "hungry")
    "He gives up. Both hands come up under the hoodie, squeezing, kneading, rolling."
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg rl_bleacher_kiss onlayer cgl
    "He backs you into the bleacher struts and kisses you, deep and wet and hungry."
    "You hook a thick thigh round his and grind your new pussy on it through your shorts, moaning into his mouth."
    rl_rory "\"Mmmh— some warm-up—\""
    rl_miles "\"You drive me insane.\""
    show rory grin at vn_pc_slot
    rl_rory "\"Keep up, slowpoke.\""
    "You rock harder against his thigh."
    rl_rory "\"Or I'll leave you in the dust.\""
    hide cg onlayer cgl
    vn_sfx "Fweeet."
    rl_coach "\"Warm-up's over! Next lap's a race!\"" with vnfx("shake")
    "You look at Miles. Miles looks at you.\n{size=-5}{color=#ff8fa3}▸ Race him{/color}{/size}"
    jump rl_last_lap

label rl_last_lap:
    ## rungs.twee: :: Redlightning Last Lap [vn]
    $ rl.fit = "greyhoodie"
    $ _ranWell = rl_run()
    $ vn_enter(bg="rl_track", pc="grin", pc_tag="rory", cast=[("miles", "neutral")], cg=None)
    show rory grin at vn_pc_slot
    show miles neutral at vn_cast_slot
    "Side by side on the line. No bottle. There doesn't need to be."
    vn_sfx "Fweet."
    "You go. He goes."
    hide miles
    "Round the bend together."
    "Your tits bouncing, your ponytail whipping his shoulder, your thighs clapping, his breath at your ear."
    "Down the back straight together. You can't shake him. He can't shake you."
    "You're calling it out loud. Of course you are."
    rl_rory "\"AND IT'S [rl_NICK] AND THORNE INTO THE STRAIGHT— NOBODY'S GIVING ANYTHING— NOBODY—\"" with vnfx("shake")
    "He's laughing. You're laughing."
    "You grab his hand without thinking."
    "The line. You both throw yourselves at it."
    jump rl_end
