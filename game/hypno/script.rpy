## Open and Listen's passages: THE SOURCE (owner, 2026-11-11: a ported route's Ren'Py script is what
## we edit). Converted once, 2026-11-11, by tools/twee2rpy.py from catalog/game/02-engine/storylines/
## hypno/ (main, rungs, endings, clinic .twee; the catalog at a551fd770), its scene-art rows and the DoL
## VN trace; the twee is frozen there as the reference. Edit this file directly. One label per passage.

label hy_opening:
    ## main.twee: :: Hypno Opening [vn]
    $ hy.fit = None
    ## The route's opening (New Game -> "Play Open and Listen"). Route.start has already preset Ethan Hale, 27, and his own flat; the scene both entrances share is Hypno Ask. The owner's backstory ruling (decision 7): an old childhood friend he hasn't seen in years, back as the flatmate through the wall. The childhood is a bare fact only, here and nowhere near a scene. VN script (framework/vn-script.js); the original prose is in docs/routes/vn-original/hypno/.
    $ hy_init()
    $ vn_enter(bg="hy_kitchen", pc="neutral", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    if vn_clock.hour < 21:
        $ vn_set_time(21, 50)
    show bg hy_kitchen onlayer bgl
    show hy_pc neutral at vn_pc_slot
    show hy_liam neutral at vn_cast_slot
    vn_sfx "Thud."
    $ _hy_clock = hy_clock()
    "You get in from league at [_hy_clock], mud to the knee."
    "Nobody's cooked. Liam's at the kitchen table behind an empty bowl, not looking up."
    "You and Liam were best friends as kids. Then he was gone for years."
    "In the spring he turned up with one bag and asked if the box room was free."
    "Both your names are on the lease now. His room is through your bedroom wall."
    "Smaller than you. Sharper. Quieter. He was always second, even then."
    vn_th "(You've never once thought about it.)"
    hy_liam "\"You're late.\""
    hy_ethan "\"League ran long.\""
    vn_sfx "Thump."
    "You drop your bag by the door, where he'll trip on it."
    hy_ethan "\"What's for dinner?\""
    hy_liam "\"Eggs. You were getting the shopping.\""
    hy_ethan "\"Ah, mate. Tomorrow. Swear down.\""
    show hy_liam stern at vn_cast_slot
    hy_liam "\"You said that Tuesday.\""
    show cg hy_opening onlayer cgl
    "You eat the eggs standing at the sink, scrolling highlights."
    vn_sfx "Bzzt."
    "Your phone buzzes. {color=#4372ff}Mike: pub thurs?? bring liam if he wants lol{/color}"
    hide cg onlayer cgl
    hy_ethan "\"Mike's asking after you. Come Thursday.\""
    hy_liam "\"Mike doesn't know my name unless you're busy.\""
    "He takes your bowl before you've finished."
    hy_liam "\"You hardly notice I'm here. Not unless you need something.\""
    show hy_pc nervous at vn_pc_slot
    "You open your mouth to say {i}that's not fair{/i}."
    "You can't remember the last time you asked him a single thing about himself."
    show hy_liam neutral at vn_cast_slot
    menu:
        hy_liam "\"Forget it. Go and shower. You stink.\""
        "Say sorry, badly":
            $ hy.flav = "sorry"
            $ vn_pass(40)
            jump hy_ask
        "Go and shower":
            $ hy.flav = "shower"
            $ vn_pass(40)
            jump hy_ask

label hy_ask:
    ## main.twee: :: Hypno Ask [vn]
    $ hy.fit = None
    ## Both entrances: the question, the hoodie, and the first night. VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_bedroom", pc="neutral", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc neutral at vn_pc_slot
    show hy_liam neutral at vn_cast_slot
    if hy.flav == "sorry":
        show hy_pc nervous at vn_pc_slot
        hy_ethan "\"Sorry. About the shopping. And. You know. I'm rubbish.\""
        "From the bathroom doorway, towel round your neck."
        hy_liam "\"You're not rubbish. You just don't look.\""
        "He says it kindly, which is worse."
    "He's on the end of your bed with his phone, saying nothing."
    "Eventually you ask."
    hy_liam "\"Nothing.\""
    "He turns the screen face-down. Then:"
    hy_liam "\"Do you think hypnosis is real?\""
    show hy_pc neutral at vn_pc_slot
    hy_ethan "\"HA. No.\""
    "It's a stage act and a genre of video, and anyone who says otherwise is selling a course."
    "He nods along with every word and doesn't put the phone down."
    show hy_liam smile at vn_cast_slot
    hy_liam "\"Yeah. You're probably right.\""
    hide hy_liam
    "He goes. You text Mike back, {color=#4372ff}ye defo{/color}, and fall asleep with the phone on your chest.\n{size=-5}{color=#ff8fa3}▸ Get up for a glass of water{/color}{/size}"
    $ hy_until(23)
    jump hy_first

label hy_first:
    ## main.twee: :: Hypno First [vn]
    $ hy.fit = "tee"
    ## RUNG 1 -- fifteen minutes. The first induction, IN TRANCE (revamp, owner 2026-10-20): the six words, and the girl who sits up in Ethan's bed is somebody who has always been Liam's. She shaves her legs for him with the pink razor and wears his tee, and the dryer scene is hers too (Hypno Laundry, the same session). Liam never asked; Ethan never agreed; the words did it. The hoodie first: he rehearsed on it, and Ethan walks past it with the wrong reason. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_advance(1)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="trance", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_liam
    vn_sfx "Click."
    "The kitchen light's on."
    "Your grey league hoodie is in a kitchen chair. Not dropped: {i}sat{/i}."
    "Hood up, arms folded in its lap, facing Liam's phone, which is propped on the fruit bowl turning a slow pink spiral."
    show hy_liam neutral at vn_cast_slot
    "Liam's at the sink, back to you."
    hy_liam "\"Laundry.\""
    "He doesn't turn round."
    vn_th "(Fair. You did leave it there.)"
    "You drink your water and go back to bed."
    show bg hy_bedroom onlayer bgl
    hide hy_liam
    "You're nearly asleep when the door opens. Hall light. His shape. The blue of his screen."
    show hy_liam stern at vn_cast_slot
    hy_liam "\"[hy_pc_name].\""
    "Too quickly, like a rehearsed line."
    hy_liam "{=hy_hypno}“Look at this a sec.”{/=hy_hypno}"
    "You look."
    show cg hy_trigger_first onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    vn_sfx "{color=#b7b7b7}Ting.{/color}"
    "Short. Pretty."
    "Ethan goes somewhere. Nobody asked him first."
    hide cg onlayer cgl
    show hy_pc trance at vn_pc_slot
    $ vn_face("hy_liam", "smile")
    "You blink. You sit up in bed with the duvet in your lap, knees pressed together the way you've always sat."
    "You smile at Liam like he's the best thing you've ever seen. Because he is."
    hy_her "\"Hi.\""
    "It comes out high and soft and happy."
    show hy_pc eager at vn_pc_slot
    hy_her "\"Hi, Liam.\""
    "His thumb's shaking on the phone."
    hy_liam "\"...Hi. Do you know who I am?\""
    hy_her "\"Silly. You're Liam. You're {i}mine{/i}.\""
    "You giggle. You think about it."
    show hy_pc trance at vn_pc_slot
    hy_her "\"No. I'm yours.\""
    "He never asked. The man whose bed this is never said yes."
    "Six words said it for him, and the girl sitting in it is beaming."
    hy_liam "{=hy_hypno}“Up. Bathroom.”{/=hy_hypno}"
    show bg hy_bathroom onlayer bgl
    show cg hy_sa_shave onlayer cgl
    "You bounce up. Down the hall on your tiptoes, into the bath in your boxers, and he hands you a pink razor."
    show hy_pc eager at vn_pc_slot
    hy_her "\"Ooh, {i}pink{/i}.\""
    "You hold it up to the light like a present."
    hy_liam "{=hy_hypno}“Legs. Smooth. All of it.”{/=hy_hypno}"
    hy_her "\"For you? Okay! Watch, watch me do it right—\""
    "You're already running the shower over your shin. Foam, then one long clean stroke from ankle to knee."
    vn_sfx "Shhk."
    hy_her "\"Look! Is that good?\""
    "You hold the leg up for him, toes pointed."
    vn_sfx "Shhk. Shhk."
    "Calf. Knee. You peel your boxers down your thighs to get the rest, humming."
    "The inside of your thigh comes up slick and soft under your own palm, and your cock bobs up fat in the steam."
    hy_her "\"Oh— silly thing. Ignore that, it does that.\""
    "You giggle at it."
    hy_liam "\"Higher.\""
    "He's leaning on the sink. His voice has gone thick."
    hy_liam "\"Everywhere.\""
    vn_sfx "Shhk."
    "There too, careful, thorough, the razor's back brushing your balls, and your hips jerk at it."
    show hy_pc trance at vn_pc_slot
    hy_her "\"{i}Ahh{/i}— ah— Liam— it's so {i}soft{/i}— feel, you have to feel—\""
    "You moan it, loud, right off the tiles."
    "He doesn't. He watches."
    "Your palm runs up your own bare leg, ankle to hip, slow, and you moan every time. Louder every time."
    vn_th "(Because he's watching, and you want him to hear.)"
    show cg hy_goodgirl_bath onlayer cgl
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    "You go to pieces. Knees knocking, hand flat on the tiles."
    show hy_pc eager at vn_pc_slot
    hy_her "\"{i}Ohh{/i}— say it again— say it again, {i}please{/i}—\""
    hy_liam "\"Good girl.\""
    "He holds out his white tee, the tight going-out one."
    hy_liam "{=hy_hypno}“Put this on. Knees together when you sit. Voice up a little.”{/=hy_hypno}"
    show cg hy_teegift onlayer cgl
    "You pull it over your head with your legs still wet."
    "It's painted on. It rides up off your stomach and smells of his soap, and you hug yourself in it and spin round once on the bathmat."
    hy_her "\"Do you like it? Do you like it on me?\""
    "A step higher. The voice he asked for."
    hy_liam "\"Yeah.\""
    "Very quietly."
    hy_liam "\"Yeah, I do.\""
    "Then he clears his throat."
    menu:
        hy_liam "{=hy_hypno}“The dryer finished an hour ago. Fold my laundry.”{/=hy_hypno}"
        "Fold his laundry for him":
            $ hy.flav = "laundry"
            jump hy_laundry
        "Do the washing-up first, slowly, where he can see":
            $ hy.flav = "dishes"
            jump hy_laundry

label hy_shirt:
    ## main.twee: :: Hypno Shirt [vn]
    $ hy.fit = "tee"
    ## Rung 1's waking day: Ethan, wiped (revamp, owner 2026-10-20: the Amnesia Loop stays on to the end). Residue only, physical and explained wrongly in one line: the pink razor; the voice "a bit higher, must be a cold". The player saw the night; Ethan never will. No sex awake. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="hy_bedroom", pc="nervous", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    $ _hy_sens = hy_body(1)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    show bg hy_bedroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    hide hy_liam
    "You wake up in Liam's white tee."
    "His tight going-out one. On you it's painted on. It rides up off your stomach and smells of his soap."
    "{color=#b7b7b7}Wrong pile, obviously.{/color}"
    "His black briefs too. Snug over your ass, flat at the front. Same pile."
    "You swing your legs out of bed and stop."
    show cg hy_sa_growsmooth onlayer cgl
    "{color=#ff5fb8}Smooth. Ankle to hip, soft as the inside of your wrist.{/color}"
    hy_ethan "{color=#ff5fb8}\"...Huh?\"{/color}"
    "{color=#ff5fb8}You pull the waistband out and look. Bare there too.{/color}"
    show bg hy_bathroom onlayer bgl
    show cg hy_razor onlayer cgl
    "In the shower, a pink razor on the shelf. Wet."
    "{color=#b7b7b7}Must have done it half asleep. Like the washing-up, sometimes.{/color}"
    hide cg onlayer cgl
    show bg hy_kitchen onlayer bgl
    show hy_liam neutral at vn_cast_slot
    show hy_pc neutral at vn_pc_slot
    hy_ethan "\"Morning.\""
    "It comes out a bit higher than you meant. You clear your throat."
    show hy_pc nervous at vn_pc_slot
    hy_ethan "\"Ahem— morning.\""
    "It does it again."
    "{color=#b7b7b7}Must be a cold coming.{/color}"
    "Liam glances up from his phone."
    "The glance goes through you warm, right in the middle of your chest, and you've no idea why."
    show cg hy_morning_kitchen onlayer cgl
    show hy_liam smile at vn_cast_slot
    hy_liam "\"Nice shirt.\""
    hy_ethan "\"It's yours. Laundry mix-up.\""
    "You sit down. Your knees press together and your ankles cross. You leave them. Comfier."
    hy_liam "\"Keep it. Suits you.\""
    "Every time he looks at you, you sit up a bit straighter."
    "Every time he looks at his phone instead, your toast gets less interesting."
    "{color=#b7b7b7}Tired, probably.{/color}"
    vn_sfx "Bzzt."
    "{color=#4372ff}Mike: thurs still on? 8 at the bell{/color}"
    "You leave it on read."
    "In the basket by the dryer, his laundry's all folded already. Perfectly, in a way you've never folded anything."
    "His briefs are in your drawer. {color=#b7b7b7}Easy mistake.{/color}\n{size=-5}{color=#ff8fa3}▸ Your room{/color}{/size}"
    $ vn_pass(90)
    jump hy_hub

label hy_laundry:
    ## main.twee: :: Hypno Laundry [vn]
    $ hy.fit = "blueshirt"
    ## Rung 1's act, IN TRANCE (revamp, owner 2026-10-20): the dryer scene moved into the session. Emily, in his tee, wants nothing but to be his, and says so at the top of her voice. Then the wipe; the clock; and the night. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="hy_kitchen", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc trance at vn_pc_slot
    hide hy_liam
    if hy.flav == "dishes":
        vn_sfx "Clink. Clink."
        ## (frame added 2026-11-11, owner: "picture every beat")
        show cg hy_sink_tee onlayer cgl
        "You do the washing-up first, humming, every plate twice, bent over the sink in his tee with it riding up."
        vn_th "(Because he's at the table watching, and you want him to.)"
        hide cg onlayer cgl
    vn_sfx "Thunk— whirr."
    "The washer-dryer's full of Liam. You pull it all out into the basket, warm, smelling of him."
    "You hold his soft old blue shirt to your face and breathe in."
    show hy_pc eager at vn_pc_slot
    hy_her "\"Mmmh...\""
    $ hy.fit = "blueshirt"
    "Then you put it on, over his tee, and wrap the sleeves round yourself."
    vn_sfx "Creak."
    show hy_liam smile at vn_cast_slot
    "A creak behind you. His hand on your waist."
    hy_liam "\"You look good in my clothes.\""
    "Low."
    show cg hy_laundry_kiss onlayer cgl
    hy_her "\"I know!\""
    "You turn round in his arms, one sleeve hanging. Coffee and mint."
    hy_her "\"They're so {i}big{/i} on me. I love it.\""
    hy_liam "\"Makes you look like you belong to me.\""
    show hy_pc trance at vn_pc_slot
    hy_her "\"I do.\""
    "Like it's obvious. You go up on your toes and kiss him."
    "He makes a noise into your mouth like he's been punched."
    "Then his hand fists in the hair at your nape and he kisses you back hard, and you melt against the dryer, warm metal through two of his shirts."
    hy_her "\"{i}Mmh{/i}— {i}mmf{/i}—\""
    "He breaks it. Lips at your ear."
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he whispers."
    "Your knees go. You sag back against the dryer, beaming, arms dropping to your sides like he's cut every string at once."
    hide cg onlayer cgl
    show cg hy_sa_laundry onlayer cgl
    "His other hand slides down the front of the briefs you're wearing, his briefs, and wraps round your cock."
    "It's so hard it throbs. You hadn't even noticed."
    show hy_pc eager at vn_pc_slot
    hy_her "\"Oh— {i}oh{/i}, Liam—!\""
    hy_liam "\"These are mine.\""
    "He squeezes."
    hy_liam "\"Aren't they.\""
    hy_her "\"Yours! They're yours, everything's yours— {i}ohh{/i}—\""
    vn_sfx "Fwp. Fwp. Fwp."
    "He strokes, slow and tight inside the cotton."
    "Your hips come off the dryer to meet his fist, and he pins them back down, and you whine at him for it."
    hy_liam "\"Look at you go. You'd let me do anything in here.\""
    hy_her "\"Anything— {i}anything{/i}— ah— {i}ah{/i}— don't stop, don't you {i}dare{/i} stop—\""
    "It's high and wet and loud. The wall's thin, Cass is always on the stairs at this time, and you couldn't care less."
    vn_th "(You want the whole building to hear him doing this to you.)"
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}" with vnfx("shake")
    hy_her "\"{i}Ahh{/i}— ah— {i}LIAM{/i}— I'm gonna— can I? Can I? Please, please can I—\""
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he says again, right in your ear."
    show cg hy_laundry_cum onlayer cgl
    "You come with your head knocked back against the cupboard, clawing the dryer lid, a long broken {i}ahhh{/i} that cracks at the top." with vnfx("flash")
    hy_her "\"{i}Thank you{/i}— thank you— {i}thank you{/i}—\""
    "You spill into his fist and his briefs in hot pulses while he milks out every one, till you're twitching and giggling and boneless against the dryer."
    "He takes his hand out. Looks at it. Wipes it on the front of his own tee. On you."
    "You look down at the mess and beam at him like he's given you something."
    hide cg onlayer cgl
    show hy_liam neutral at vn_cast_slot
    hy_liam "\"Fold the rest.\""
    "His voice isn't steady."
    hy_liam "\"My shirts in my drawers. My briefs in yours. Then bed.\""
    hy_liam "{=hy_hypno}“You won't remember any of this.”{/=hy_hypno}"
    show hy_pc eager at vn_pc_slot
    hy_her "\"Okay!\""
    "So happy to be told something."
    $ vn_pass(15)
    $ hy_end()
    show bg hy_bedroom onlayer bgl
    hide hy_liam
    show hy_pc neutral at vn_pc_slot
    pass
    "—"
    $ hy.fit = "tee"
    $ _hy_clock = hy_clock()
    "The clock says [_hy_clock]. You don't remember lying back down."
    "Door shut. Dark. Your legs feel strange against the sheet."
    $ hy_induct()
    ## The night (visual-novel days, framework/vn.js): one click sleeps, and Ethan wakes in his tee.
    "You feel {color=#38b20a}extraordinarily well rested{/color}, and the Loop makes very sure you don't ask anything else.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump hy_shirt

label hy_name:
    ## rungs.twee: :: Hypno Name [vn]
    $ hy.fit = "tee"
    ## RUNG 2 -- an evening. IN TRANCE (revamp, owner 2026-10-20): the show for Liam's phone, and she gives herself the name Emily -- nobody gave it to her. The night alone moved into the session too: she comes for the camera. Then the wipe, and the notification Ethan carries through the wall without reading. VN script (framework/vn-script.js); its scene-art lines are kept word for word. The plate is "You" (her) until she names herself, "Emily" from the name on.
    $ hy_advance(2)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_liam
    if hy.flav == "phone":
        "Mid-scroll, sound off, your screen goes soft and pink and starts to turn."
        "You don't put it down. You watch."
    else:
        "You're on the end of the bed in his tee when the door opens."
        show hy_liam neutral at vn_cast_slot
        "He doesn't say your name this time. He just sits down next to you."
    show hy_liam neutral at vn_cast_slot
    hy_liam "{=hy_hypno}“Look.”{/=hy_hypno}"
    show cg hy_trigger_name onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    vn_sfx "{color=#b7b7b7}Ting.{/color}"
    "Ethan goes."
    hide cg onlayer cgl
    show hy_pc eager at vn_pc_slot
    $ vn_face("hy_liam", "smile")
    "The girl who's left kicks her heels against the bed and lights up."
    hy_her "\"Liam! Hi! Hi.\""
    show cg hy_name_film onlayer cgl
    "He props his phone on your desk, camera on you, red dot lit."
    hy_liam "{=hy_hypno}“Stand up. Show me.”{/=hy_hypno}"
    hy_her "\"Are you filming me?\""
    "You clap your hands over your mouth, delighted."
    hy_her "\"Oh my god. Okay. Okay, watch.\""
    "You stand. Your hips start to sway, slow, side to side, to music that isn't playing."
    "You peel his tee up your stomach, over your chest, off, and twirl it round one finger and throw it at him."
    "Then your hands run down your sides and hook in the waistband of his briefs."
    "You turn round, push your ass out at the camera, and look back over your shoulder, giggling."
    hy_liam "{=hy_hypno}“What's your name?”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    "You stop. You think about it, a finger on your lip. Nobody's ever asked you."
    hy_emily "\"Emily.\""
    "You decide it, high and sweet and sure."
    show hy_pc eager at vn_pc_slot
    hy_emily "\"I'm Emily.\""
    "You beam at the lens."
    hy_emily "\"Hi! I'm Emily!\"" with vnfx("shake")
    hy_liam "\"Emily.\""
    "Very quietly."
    hy_liam "\"Oh, that's good. I didn't even give you that one.\""
    hy_emily "\"Do you like it? Say it. Say it again.\""
    hy_liam "\"Emily.\""
    show cg hy_sa_nameshow onlayer cgl
    "You squeal and bounce on your toes."
    "A gloss from his pocket: you paint your own mouth with it, pouting at the camera. A hair tie on your wrist."
    "Up on tiptoe, turning, both palms squeezing your flat chest like there's something there."
    "Your nipples go hard and electric under your fingers, and you moan straight at the lens."
    hy_emily "\"{i}Ahh{/i}— Liam— they're so {i}sensitive{/i}— look—\""
    hy_liam "{=hy_hypno}“Hand down the front. Slowly. Say it.”{/=hy_hypno}"
    hy_emily "\"I'm Emily— I'm {i}Emily{/i}—\""
    vn_sfx "Fwp, fwp."
    "Your fist works your cock through his briefs, hips rolling, the other hand pinching your nipple."
    hy_emily "\"Emily, I'm Emily, I'm your Emily— {i}nnh{/i}— are you watching? Are you watching me, Liam?\""
    hy_liam "\"Every second.\""
    show cg hy_sa_namebed onlayer cgl
    "That does it to you."
    "Onto the bed, onto your front, knees under you and ass up for the camera, one hand mashing your chest and the other fisting your cock into the mattress."
    vn_sfx "Fwp. Fwp. Fwp."
    "The headboard taps the wall. His wall."
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    hy_emily "\"{i}Ahh{/i}— ah— good girl— I'm your good girl— I'm being {i}so{/i} good—\""
    "You turn your face out of the pillow so it's louder."
    hy_emily "\"Can I? Can I come for the camera? {i}Please{/i}, Liam, please, please—\""
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}" with vnfx("shake")
    hy_emily "\"{i}PLEASE{/i}—!\"" with vnfx("shake")
    hy_liam "\"Go on, Emily.\""
    show cg hy_name_cum onlayer cgl
    "You come so hard you see white, screaming his name and your new one." with vnfx("flash")
    vn_sfx "Tap. Tap. Tap."
    "The headboard, loud enough to carry through the wall and down the stairwell. You spurt over your fist and the sheet."
    hy_emily "\"Hah... hah... hehe...\""
    "Then you flop over and wave at the camera, giggling, wrecked."
    hide cg onlayer cgl
    "He stops the video."
    hy_liam "{=hy_hypno}“Bed. Forget.”{/=hy_hypno}"
    hy_emily "\"Night night.\""
    "Emily snuggles down."
    $ vn_pass(250)
    $ hy_end()
    hide hy_liam
    show hy_pc nervous at vn_pc_slot
    "—"
    $ _hy_clock = hy_clock()
    "The clock says [_hy_clock]."
    "On top of the covers, in nothing at all."
    "A smudge of pink at the corner of your mouth comes off on your thumb. A hair tie round your wrist that isn't yours."
    "The sheet's a state. The backs of your knees tingle like you've been up on tiptoe for hours. Your cheeks are warm from smiling."
    "His phone's face-up on the duvet. The screen lights up."
    "{color=#ffd700}Submissive Mind{/color}\n{color=#e40081}Session complete. The subject named herself: {b}Emily{/b}.{/color}"
    "{color=#b7b7b7}One of his games, by the look of it.{/color}"
    show hy_liam neutral at vn_cast_slot
    "You take it through the wall. He stares at the screen, then at you."
    hy_liam "\"Thanks.\""
    $ hy_induct()
    "In a voice you've never heard him use.\n{size=-5}{color=#ff8fa3}▸ Go back to bed{/color}{/size}"
    $ vn_pass(20)
    jump hy_wall

label hy_wall:
    ## rungs.twee: :: Hypno Wall [vn]
    $ hy.fit = None
    ## Rung 2's night, AWAKE and wiped (revamp, owner 2026-10-20: no sex while Ethan is awake). The solo scene moved into the trance; what's left is residue, and Liam watching the video through the wall. Ethan gets it exactly wrong. VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_bedroom", pc="nervous", pc_tag="hy_pc", cast=[], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    "You can't sleep."
    "{color=#ff5fb8}Your nipples are {i}buzzing{/i}. Hot, swollen, electric, catching on the sheet every time you breathe.{/color}"
    "{color=#b7b7b7}The sheet's scratchy. New detergent.{/color}"
    show cg hy_wall onlayer cgl
    "Through the wall, Liam's watching something with the sound turned low."
    hy_unk "\"{i}I'm Emily. Hi! I'm Emily.{/i}\""
    "A girl's voice, high and happy and breathless."
    "Then a lot of moaning."
    vn_sfx "Tap. Tap. Tap."
    "Then a headboard."
    show hy_pc happy at vn_pc_slot
    "You grin at the ceiling. Liam's got a girlfriend. Good for him. Took him long enough."
    hy_ethan "\"...She's {i}loud{/i}, though.\""
    "You put the pillow over your head and fall asleep smiling, for some reason, to the sound of her coming through the wall."
    ## The night (visual-novel days, framework/vn.js): one click sleeps, and the morning has a card in it.
    "{color=#b7b7b7}In the morning he doesn't mention her. You don't like to ask.{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    call vn_night(8)
    jump hy_card

label hy_card:
    ## rungs.twee: :: Hypno Card [vn]
    $ hy.fit = "tee"
    ## Rung 2's waking day: the body answers, and the card for the Bloom is on your desk. Ethan walks to the clinic himself; the consult is in clinic.twee, and rung 3 can't fire until it's done (Hypno.nextRung). Residue only, explained wrongly in a line each. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="hy_bedroom", pc="nervous", pc_tag="hy_pc", cast=[], cg=None)
    $ _hy_sens = hy_body(2)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    $ hy.appt = True
    show bg hy_bedroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    show cg hy_sa_growbuds onlayer cgl
    "{color=#ff5fb8}Morning. Your nipples are still buzzing. Puffy, pink, poking at your shirt.{/color}"
    "{color=#ff5fb8}They catch on it all day, and every time, you have to stand very still and think about football.{/color}"
    "{color=#ff5fb8}Your arms look softer. Your ass is doing something new in your jeans: rounder, pushing at the back seams.{/color}"
    "{color=#ff5fb8}You grab a handful in the mirror and it squishes.{/color}"
    hy_ethan "{color=#ff5fb8}\"Skipping the gym.\"{/color}"
    "{color=#ff5fb8}You tell the mirror. That's all.{/color}"
    "Your jaw's still a bit stiff, and when you yawn your throat opens wider than it ever used to."
    "{color=#b7b7b7}Grinding your teeth again.{/color}"
    show cg hy_card onlayer cgl
    "A card on your desk. Cream, a little flower: {color=#ffd700}The Bloom{/color}, the clinic on the High Street."
    "A time on it in Liam's small neat capitals."
    "You don't remember asking anyone to book anything."
    "Then the memory arrives, whole and convincing: you said you'd look into it. It was your idea. Course it was."
    hide cg onlayer cgl
    show hy_liam neutral at vn_cast_slot
    hy_liam "\"You'll want to eat first.\""
    "From the doorway, not looking up."
    hy_liam "\"They take blood.\""
    show hy_pc neutral at vn_pc_slot
    hy_ethan "\"Yeah. I know.\""
    "{color=#b7b7b7}The card goes in your pocket. You'll go. Nobody has to make you.{/color}\n{size=-5}{color=#ff8fa3}▸ Your room{/color}{/size}"
    jump hy_hub

label hy_stay:
    ## rungs.twee: :: Hypno Stay [vn]
    $ hy.fit = "panties"
    ## RUNG 3 -- the whole night. THE HINGE, reframed (revamp, owner 2026-10-20): the loop stays on; the hinge is Liam keeping her under LONGER. "Stay under tonight." Emily on her knees, the cage, the twin tails, and the mandatory director scene -- consensual, eager -- with nothing round it. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_advance(3)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="trance", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    hide hy_liam
    $ hy.fit = None
    "{color=#ff5fb8}The pills have been doing something.{/color}"
    if hy.full:
        "{color=#ff5fb8}Under your shirt, two small soft breasts where there was nothing at all before the pills, and they tingle when you lie on your front. Your thighs have gone silky and rub when you walk.{/color}"
    else:
        "{color=#ff5fb8}Under your shirt, two puffy buds that tingle when you lie on your front. Your thighs have gone silky and rub when you walk.{/color}"
    "{color=#ff5fb8}{color=#b7b7b7}Side effects. The leaflet said.{/color}{/color}"
    show hy_liam stern at vn_cast_slot
    "Liam sits on the end of your bed, phone in both hands."
    "His thumb moves on the screen, once, twice, sliding something all the way along."
    hy_liam "\"I'm going to try something.\""
    hy_liam "{=hy_hypno}“Stay under tonight.”{/=hy_hypno}"
    show cg hy_trigger_stay onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    "The floor goes soft. Ethan goes down with it, the way he always does, and doesn't come up."
    hide cg onlayer cgl
    show hy_pc eager at vn_pc_slot
    $ vn_face("hy_liam", "smile")
    hy_emily "\"Hi.\""
    $ hy.fit = "panties"
    "Emily. High and soft and pleased. She sits up and wraps herself round his arm."
    hy_emily "\"Hi, hi. You came back.\""
    hy_liam "\"All night tonight. You're staying under till the morning. Is that all right?\""
    hy_emily "\"{i}All night?{/i}\"" with vnfx("shake")
    "You squeal and kiss his cheek, his jaw, his ear."
    hy_emily "\"Yes. Yes yes yes. Can we do everything?\""
    hy_liam "{=hy_hypno}“Strip. The blue ones.”{/=hy_hypno}"
    "Powder-blue panties with a little bow, folded on top in your drawer."
    hy_emily "\"You bought me these? They're so {i}pretty{/i}.\""
    "You hold them up to the light."
    "You strip slow, because he likes slow, wiggling, peeking at him."
    $ hy.fit = "panties"
    if hy.full:
        "You pull them up your smooth legs and over your ass, and do a twirl. Your new breasts bounce with it. Cock pushing at the satin."
    else:
        "You pull them up your smooth legs and over your ass, and do a twirl. Buds tight. Cock pushing at the satin."
    hy_emily "\"Do you like them? Do you like me in them?\""
    "Something from his pocket. A little pink plastic cage. A little brass lock."
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Ooh. What's that?\""
    show cg hy_cage onlayer cgl
    hy_liam "\"It keeps you mine.\""
    hy_liam "{=hy_hypno}“Hold still.”{/=hy_hypno}"
    "You hold so still you shake."
    "He kneels, eases the front of the panties down, and folds your cock into it, cool and snug."
    hy_emily "\"Hehe... it looks so {i}small{/i} in there.\""
    vn_sfx "Click."
    "The key goes in his pocket. Your eyes follow it, shining."
    hy_liam "{=hy_hypno}“Liam keeps that. Say it.”{/=hy_hypno}"
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Liam keeps that! You keep it. Keep it forever.\""
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    hy_emily "\"{i}Mmh{/i}—\""
    "Your knees nearly go."
    show cg hy_extensions onlayer cgl
    "Last thing: two long platinum falls of hair over his arm."
    vn_sfx "Snick. Snick."
    $ hy.tails = True
    "He clips them in at your temples."
    "In the wardrobe mirror, a girl with twin tails and pink cheeks looks back. You gasp and shake your head to make them swing."
    hy_emily "\"Twin tails! Oh my {i}god{/i}, Liam. Look at me.\""
    hy_liam "\"I am.\""
    hide cg onlayer cgl
    "He sits on the edge of the bed and unzips."
    show cg hy_sa_kneel onlayer cgl
    "Your knees find the carpet before he's asked.\n{size=-5}{color=#ff8fa3}▸ Open your mouth{/color}{/size}"
    jump hy_stay_sex

label hy_stay_after:
    ## rungs.twee: :: Hypno Stay After [vn]
    $ hy.fit = None
    ## Rung 3's whole night, after the director scene. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg=None, pc="neutral", pc_tag="hy_pc", cast=[], cg="hy_stay_climax")
    show hy_pc eager at vn_pc_slot
    if hy_enc.partner_came:
        $ hy.fit = "panties"
        "He comes with his fists in your tails, and the last of it goes over you: lips, nose, cheek." with vnfx("flash")
        if hy.full:
            "Then your breasts, running down to the bow on your panties. You hold your face up for it, eyes shut, giggling."
        else:
            "Then your buds, running down to the bow on your panties. You hold your face up for it, eyes shut, giggling."
    else:
        if hy.full:
            "He pulls you off by your tails with a wet pop and finishes in his fist over your face and breasts while you hold still for it."
        else:
            "He pulls you off by your tails with a wet pop and finishes in his fist over your face and buds while you hold still for it."
        hy_emily "\"On me, on me, sir, {i}please{/i}—\""
        "Mouth open, begging, until you're dripping." with vnfx("flash")
    $ hy.fit = "panties"
    hy_liam "\"Look at you.\""
    hy_emily "\"Look at {i}me{/i}.\""
    "Delighted, you look down at yourself. It's cooling on your skin."
    "Your cock strains in the cage, tiny and swollen against the plastic, leaking into the satin. Nobody touches it. Nobody's going to."
    show hy_pc trance at vn_pc_slot
    hy_emily "\"It's all drippy. Silly.\""
    "You giggle."
    show cg hy_sa_stayafter onlayer cgl
    "He holds out two fingers, wet with it."
    "You suck them clean, eyes on his, making small happy noises, and lick the gap between them too."
    hy_emily "\"{i}Mmh{/i}— thank you, sir— {i}mmh{/i}—\""
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he says."
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Ahhhn—! Again. Say it again. I'll do anything.\""
    "You moan harder at that than at anything he did."
    show cg hy_stay_carpet onlayer cgl
    "The whole night: that's how long tonight is."
    "On your knees, then on your back on the carpet with your tails fanned round your head. Your mouth, your hands, the insides of your thighs."
    "He tells you what you are, low and even, and you say it back louder every time—"
    hy_emily "\"Your girl, your good girl, yours—\""
    "—until you're saying it before he's asked. Until the window goes grey."
    hy_liam "{=hy_hypno}“Shower. Forget.”{/=hy_hypno}"
    hy_emily "\"Okay.\""
    "Emily kisses him goodnight at dawn."
    "—"
    $ hy_induct()
    "{color=#ffd700}Submissive Mind{/color}\n{color=#e40081}Session complete. Duration: {b}overnight{/b}. Amnesia Loop: {color=#38b20a}on{/color}.{/color}\n{size=-5}{color=#ff8fa3}▸ Shower{/color}{/size}"
    $ vn_pass(max(30, hy_to_tomorrow(6) - 30))
    jump hy_remade

label hy_remade:
    ## rungs.twee: :: Hypno Remade [vn]
    $ hy.fit = "nude"
    ## Rung 3's morning, AWAKE and wiped: the room remade while Ethan was in the shower, unsigned. The cage is "medical"; the tails are a bet he lost (revamp, owner 2026-10-20). VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_end()
    $ vn_enter(bg="hy_bathroom", pc="nervous", pc_tag="hy_pc", cast=[], cg=None)
    $ _hy_sens = hy_body(3)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    show bg hy_bathroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    $ hy.fit = None
    vn_sfx "Shhhhhhh."
    "You come to on the shower floor with the water running and your hair held up out of it in two hands."
    "Two long platinum tails, clipped in at your temples."
    "{color=#b7b7b7}Lost a bet. Must have. Mike, probably.{/color}"
    "Your jaw has that loose, used feeling. Your throat feels open, like after a really big yawn."
    show cg hy_sa_growshower onlayer cgl
    if hy.full:
        "{color=#ff5fb8}The water runs over your breasts. Small, soft, {i}real{/i}. Bigger than last week, and so {i}sensitive{/i} the spray makes you squeak.{/color}"
    else:
        "{color=#ff5fb8}The water runs over your buds. Puffy. Warm. Bigger than last week, and so {i}sensitive{/i} the spray makes you squeak.{/color}"
    hy_ethan "{color=#ff5fb8}\"Eep—!\"{/color}"
    "{color=#ff5fb8}{color=#b7b7b7}The pills. The leaflet did say.{/color}{/color}"
    "{color=#ff5fb8}Your ass fills your hands when you soap it, round and slick. Your thighs press together on the tiles, silky all the way up.{/color}"
    "{color=#ff5fb8}And the cage. Your cock's gone small in it, soft and pink behind the plastic, a little brass lock on the front.{/color}"
    "You look at it for a while."
    "{color=#b7b7b7}Medical. The Bloom. Dr. Adair said something about it, definitely. Keeps things calm, with the pills.{/color}"
    show bg hy_bedroom onlayer bgl
    "Back in your room, it's changed."
    show cg hy_vanity_new onlayer cgl
    "A white vanity under the window: round mirror, a forest of bottles and brushes, a stand for the extensions."
    "You set them on it, because that's clearly where they go."
    "The second drawer is full of panties folded in rows, pink and lilac and white and powder blue."
    "On the bed: a pink camisole and a tube of gloss."
    "Nobody says they did it. Liam's in the kitchen, humming, making toast."
    show cg hy_camisole_first onlayer cgl
    "Your shirts are all in the wash, so the camisole, then."
    "Your lips are dry, and the gloss is just tinted balm, so: on, first try."
    hide cg onlayer cgl
    show bg hy_kitchen onlayer bgl
    $ hy.fit = "cami"
    show hy_liam smile at vn_cast_slot
    $ hy.fit = None
    "You walk into the kitchen and he looks up, and it goes through you warm, like the first morning."
    hy_liam "\"Morning, Em.\""
    hy_ethan "\"Em?\""
    hy_liam "\"Short for mate.\""
    show hy_pc happy at vn_pc_slot
    hy_ethan "\"Obviously.\""
    vn_sfx "Crunch."
    "You steal his toast.\n{size=-5}{color=#ff8fa3}▸ Your room{/color}{/size}"
    $ vn_pass(60)
    jump hy_hub

label hy_master:
    ## rungs.twee: :: Hypno Master [vn]
    ## (2026-11-11: the passage opens awake, in Ethan's day clothes, for the body line "Your buds
    ## pebble against your shirt"; the sports bra and Emily's face come with the trigger, below.
    ## The DoL screen opened in the sports bra and the trance face.)
    $ hy.fit = None
    ## RUNG 4 -- a night and a day. IN TRANCE (revamp, owner 2026-10-20): "Not Liam tonight. Master." She begs for the plug and works it in herself, then the buds; then she slips into his bed. NOT his cock in her ass: that is rung 6's, and this rung forbids it. The optional titjob is consensual combat in Emily's voice. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_advance(4)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="neutral", pc_tag="hy_pc", cast=[("hy_liam", "stern")], cg=None)
    $ _hy_sens = hy_body(4)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    show bg hy_bedroom onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_liam
    if hy.full:
        ## THE FULL REGIMEN's rung 4 beat (owner, 2026-11-11: "the bra on the chair"): awake, so
        ## nothing is done to him here; the chest, explained wrongly like everything else.
        "You go to change out of your work shirt, and the sports bra won't come down over them."
        show cg hy_bra_tight onlayer cgl
        "It was snug last week. Now it stops halfway and bites, and they push out under the band, round and heavy and {i}there{/i}."
        vn_sfx "Snap."
        show hy_pc nervous at vn_pc_slot
        "You get it off, and stand in your own room breathing, holding it."
        "There's a bra folded on your desk chair. Pale pink lace, the tag still on."
        show cg hy_bra_mirror onlayer cgl
        "You hold it up against yourself in the wardrobe mirror, to prove it isn't yours."
        "The cups fill. A man you nearly recognise, platinum tails at his temples, holds pink lace to a chest that fills it, and goes red to the ears."
        vn_th "(Chest day. You've been overdoing chest day.)"
        "{color=#b7b7b7}You don't go to the gym. You put it on anyway, because the sports bra hurt, and it fits like it was bought for you.{/color}"
        hide cg onlayer cgl
        show hy_pc neutral at vn_pc_slot
    if hy.flav == "kneel":
        $ hy.fit = None
        "You're kneeling on the carpet when he comes in, hands on your thighs."
        "{color=#b7b7b7}You'd sat down there to find your phone charger, probably.{/color}"
        show hy_liam stern at vn_cast_slot
        "He walks round you once before he speaks."
    else:
        $ hy.fit = None
        "You're at his door before the chime finishes, to ask about the bins."
        show hy_liam stern at vn_cast_slot
        "He smiles like he's adding something up and walks you back to your room by the wrist."
    show hy_liam stern at vn_cast_slot
    show cg hy_trigger_master onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    "Ethan's gone before the last word lands."
    hide cg onlayer cgl
    show hy_pc eager at vn_pc_slot
    $ hy.fit = "sportsbra"
    "Emily blinks up at him and her whole face lights."
    hy_emily "{color=#ff5fb8}\"Liam! Look— {i}look{/i} what happened—\"{/color}"
    show cg hy_sa_growhips onlayer cgl
    "{color=#ff5fb8}Your hips came in overnight. Round. Wide.{/color}"
    "{color=#ff5fb8}Your shorts are stretched across them and your ass spills out under the hem, fuller than yesterday.{/color}"
    "{color=#ff5fb8}You run your hands down your sides, over the new curve, and moan out loud at it.{/color}"
    hy_emily "{color=#ff5fb8}\"{i}Mmh{/i}— it's so {i}round{/i}— is it for you? It's for you, isn't it?\"{/color}"
    hy_liam "\"Turn round.\""
    "You do it so fast you nearly fall over, and push your ass out for him."
    "He hums like he's pleased with the arithmetic."
    hy_liam "{=hy_hypno}“Not Liam tonight. Master.”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    "It goes into you like a key. You feel it turn, and you shiver all the way down."
    hy_emily "\"Yes, Master.\""
    "You breathe it. Then louder, trying it out, loving it:"
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Yes, {i}Master{/i}.\""
    "Under the shorts, the cage is already wet."
    hy_liam "{=hy_hypno}“Nightstand.”{/=hy_hypno}"
    "Lube. A small pink silicone plug, flared, on a folded cloth."
    hy_emily "\"For me? Master, is that for {i}me{/i}?\""
    "You gasp like it's your birthday."
    hy_liam "{=hy_hypno}“Hands and knees on the bed. Ass to me.”{/=hy_hypno}"
    "Face in the pillow, ass up, shorts and panties peeled to your thighs by your own eager hands."
    "The cool air makes you shiver and giggle at once."
    hide hy_liam
    hy_liam "{=hy_hypno}“Open yourself up for me. Show me how.”{/=hy_hypno}"
    "He sits in your desk chair and doesn't touch you."
    show cg hy_plug_fingers onlayer cgl
    "Two slick fingers to your hole. Cool, slippery, {i}tight{/i}."
    "One fingertip slides in and you gasp so loud it's nearly a squeal."
    hy_emily "\"{i}Hah{/i}— oh— oh, Master, are you watching? I'm doing it, I'm doing it for you—\""
    hy_liam "{=hy_hypno}“Deeper.”{/=hy_hypno}"
    hy_emily "\"Yes, Master—\""
    vn_sfx "Shlk."
    "The whole finger. Then two. You fuck yourself on them, slow, then not slow, your other fist in the duvet, tails swinging."
    vn_sfx "Shlk shlk shlk."
    "Your caged cock drips a long clear string onto the sheet."
    hy_emily "\"{i}Ahh{/i}— ah— it's so good— it's so {i}good{/i}—\""
    hy_liam "{=hy_hypno}“What do you want?”{/=hy_hypno}"
    hy_emily "\"The plug. Please, Master, I want the plug, I want to be full—\""
    hy_emily "\"—I want to be your good girl with my ass full for you, {i}please{/i}—\""
    "You whine it."
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}" with vnfx("shake")
    hy_emily "\"{i}PLEASE{/i} let me have the plug, Master! Please, please, I'll be so good, I'll be the best girl—!\"" with vnfx("shake")
    "The whole landing can hear it. You don't care. You want them to."
    hy_liam "{=hy_hypno}“Go on, then.”{/=hy_hypno}"
    show cg hy_sa_plug onlayer cgl
    "Your hand shakes with how much you want it."
    "It's bigger than your fingers. Push, breathe, push, wider and wider, so big—"
    hy_emily "\"It's so {i}big{/i}, Master, it's so—\""
    "One long moan into the pillow. Then the widest part goes past and your body {i}takes{/i} it."
    vn_sfx "Pop."
    "Seated. Full. Your hole knew exactly how to open for it. And you come."
    show cg hy_plug_cum onlayer cgl
    "Just from that. Caged and untouched, face in the pillow, your tiny cock soft in the plastic, pulsing thin dribbles through the cage onto the sheet." with vnfx("flash")
    "It didn't even get hard."
    hy_emily "\"{i}Ahh{/i}— ah— Master— {i}thank you{/i}—!\""
    hy_emily "\"Didn't— didn't even— hehe— it didn't even get {i}hard{/i}!\""
    "You giggle into the pillow, delighted with yourself."
    hy_liam "\"Look at you. Perfect.\""
    "Master laughs softly."
    hide cg onlayer cgl
    show hy_liam smile at vn_cast_slot
    "Then he unzips."
    hy_liam "{=hy_hypno}“Sit up. Tits out. Push them together.”{/=hy_hypno}"
    if hy.full:
        "You pull your shirt off over your head and fumble the lace bra open, and they spill out into your hands, heavy and warm, the plug shifting as you sit back on your heels."
    else:
        "You pull shirt and sports bra off over your head in one go and sit back on your heels, plug shifting."
    if hy.full:
        "You push your breasts together for him with both hands, beaming. They fill your hands now."
    else:
        "You push your buds together for him with both hands, beaming."
    hy_emily "\"Here, Master! Here!\""
    if hy.full:
        "He slides his cock between them, and they swallow it."
    else:
        "He slides his cock between them. Barely anything either side of him."
    "He fucks it anyway, slow, the head bumping your chin every stroke, and you squeal every time it does."
    if hy.full:
        hy_liam "{=hy_hypno}“Look what you asked for.”{/=hy_hypno}"
    else:
        hy_liam "{=hy_hypno}“Just enough to tell everyone you're my girl. Never more.”{/=hy_hypno}"
    ## Topless for it: the shirt and the sports bra come off, or combat can't put him there.
    menu:
        hy_emily "\"Your girl. Your girl, your girl—\""
        "Keep them pushed together for him":
            jump hy_master_sex
        "Lick the head every time it reaches you":
            $ hy.flav = "lick"
            jump hy_master_after

label hy_master_after:
    ## rungs.twee: :: Hypno Master After [vn]
    $ hy.fit = None
    $ vn_enter(bg=None, pc="neutral", pc_tag="hy_pc", cast=[], cg="hy_master_climax")
    show hy_pc eager at vn_pc_slot
    if hy_enc.ran:
        $ _hmCame = hy_enc.partner_came
    else:
        $ _hmCame = True
        "You lick the head every time it reaches you, quick little licks at the slit."
        hy_emily "\"Master, Master, {i}Master{/i}—\""
        "Every time he pulls back, louder every time, until he swears and goes faster."
    if _hmCame:
        $ hy.fit = "panties"
        if hy.full:
            "He comes across your chest and jaw in thick hot ropes, painting your breasts and throat." with vnfx("flash")
        else:
            "He comes across your chest and jaw in thick hot ropes, painting your buds and throat." with vnfx("flash")
        hy_emily "\"Yes, yes, on me, {i}thank you{/i}—\""
        "You hold them pushed together through all of it, gasping."
    else:
        "He pulls back and finishes in his fist, across your chest and jaw in thick hot ropes." with vnfx("flash")
        if hy.full:
            "You hold your breasts together for him and beg for every drop."
        else:
            "You hold your buds together for him and beg for every drop."
    $ hy.fit = "panties"
    "You squeezed them round him at exactly the right moment, every stroke. You just knew."
    hy_liam "{=hy_hypno}“Clean up, pet.”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Yes, Master!\""
    "Fingers, then tongue where you can reach. Every drop. The plug sits in you like a warm hand."
    "You look up with your mouth open to show him it's all gone, and he pats your cheek."
    ## The plug goes in the nightstand, and in DoL's own toy inventory with it, so it's yours to use. Once only.
    if not hy.plug:
        $ hy.plug = True
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}\n{size=-5}{color=#ff8fa3}▸ Later{/color}{/size}"
    $ vn_pass(120)
    jump hy_his_bed

label hy_his_bed:
    ## rungs.twee: :: Hypno His Bed [vn]
    $ hy.fit = "nude"
    ## Rung 4's close, still in trance: she slips into his bed without a word, and the session runs a night and a day (revamp, owner 2026-10-20). VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_liamroom", pc="trance", pc_tag="hy_pc", cast=[], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc trance at vn_pc_slot
    "Later. The flat's quiet, the plug's still in, and you're lying in your own bed hugging the pillow."
    "Thinking about him, because there's nothing else in the world worth thinking about."
    show bg hy_liamroom onlayer bgl
    "His door's ajar. A line of lamplight."
    "You slip out of bed and pad through in the dark on your tiptoes, without a word, and don't knock."
    "He's awake. He lifts the edge of the duvet."
    show cg hy_hisbed onlayer cgl
    "You get in, back to him, and his arm settles over your hip like it owns it."
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Haaaah...\""
    "You sigh the biggest, happiest sigh of your life and wriggle back into him."
    hy_emily "\"Night, Master.\""
    "You whisper it."
    hy_liam "{=hy_hypno}“Stay under. All night, and all tomorrow.”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Mm-hm.\""
    "Emily, already asleep."
    ## The night, in his bed (visual-novel days): one click sleeps, and the session is still running at eight.
    "{color=#b7b7b7}A night and a day: that's how long the session runs this time. He doesn't let it end in the morning.{/color}\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    call vn_night(8)
    jump hy_day

label hy_day:
    ## rungs.twee: :: Hypno Day [vn]
    $ hy.fit = "tee"
    ## Rung 4's day: the session doesn't end in the morning. In trance (revamp, owner 2026-10-20): his desk, his calls, her mouth, all of it eager. Not his cock in her ass: the plug, and her mouth. Then the wipe at dusk, and Ethan's residue: the lube is "Liam's, obviously". VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_kitchen", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_liamroom onlayer bgl
    show hy_pc trance at vn_pc_slot
    hide hy_liam
    "You wake in his bed, his arm over your hip, the plug still in."
    "Before good morning, before anything, he says the six words into the back of your neck, just to keep you there."
    show cg hy_trigger_day onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Morning, Master.\""
    "You sigh it, and wriggle."
    hy_liam "{=hy_hypno}“Breakfast. In my tee. Nothing else.”{/=hy_hypno}"
    show bg hy_kitchen onlayer bgl
    $ hy.fit = "tee"
    show cg hy_breakfast_tee onlayer cgl
    "His tee stops at the top of your thighs."
    "Every reach to the cupboard, it rides up over your ass and the plug's pink base shows."
    "You reach for the cupboard a lot more than you need to, peeking back to check he's looking. He is."
    "You bring him his eggs and stand by his chair till he's done, swaying."
    vn_th "(Nobody told you to sit, and you don't want to miss being told.)"
    hide cg onlayer cgl
    show hy_liam neutral at vn_cast_slot
    vn_sfx "Tap."
    "Then he goes to his desk, and taps his knee once."
    "You're under it before he's finished tapping."
    hide hy_liam
    show cg hy_desk onlayer cgl
    "You kneel in the dark between his knees, tails brushing his thighs, and unzip him with a happy little hum."
    "A man in his headphones talks about a deadline."
    hy_emily "\"You're on a {i}call{/i}.\""
    "You whisper it up at him, thrilled, and take him in your mouth."
    hy_liam "\"Yeah, no, that works.\""
    "He's telling the laptop."
    vn_sfx "Glk. Glk."
    "Slow and deep, holding him on your tongue, your hands folded behind your back like a good girl."
    "His fist wraps one of your tails and tugs. You go molten round the plug."
    hy_emily "\"{i}Mmmh{/i}—\""
    "It comes out loud. You don't mean to. You're not sorry."
    "The fist tightens."
    hy_liam "\"Sorry. Kettle.\""
    "Perfectly calm, to the laptop."
    "That nearly makes you come on your own."
    "You whimper round his cock, face burning, your caged cock soft and dripping on his floor where nobody will ever bother with it."
    "Sloppier and wetter, until his thighs tense."
    "He mutes the call with one finger and comes down your throat without a sound, holding your head while you swallow and swallow." with vnfx("flash")
    hy_emily "\"Mmmhh— {i}thank you{/i}—\""
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he says, and unmutes."
    show cg hy_worktop onlayer cgl
    "Again at lunch: your cheek on the cold worktop, his hand on your neck, you giggling at the toaster."
    hide cg onlayer cgl
    show bg hy_liamroom onlayer bgl
    "Again in the afternoon, on his bed, on your back with your knees up, working the plug in and out for him while he watches."
    hy_emily "\"{i}Master{/i}, {i}Master{/i}, {i}Master{/i}—\""
    "Louder each time."
    vn_sfx "THUMP. THUMP. THUMP." with vnfx("shake")
    "Until somebody downstairs bangs on the ceiling with a broom."
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}"
    "You get louder."
    show cg hy_day_cum onlayer cgl
    hy_emily "\"MASTER— AHHHH—!\"" with vnfx("flash")
    "You come with the broom still going."
    hide cg onlayer cgl
    show hy_liam neutral at vn_cast_slot
    "At dusk he washes the plug, puts it in your nightstand, and kneels you on his rug."
    hy_liam "{=hy_hypno}“Forget.”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Okay, Master.\""
    "Emily smiles, and goes."
    hide hy_liam
    show hy_pc nervous at vn_pc_slot
    pass
    "—"
    $ hy.fit = None
    "You surface on Liam's rug with the light going orange, your jaw loose, your throat raw."
    "{color=#b7b7b7}Fell asleep on his floor watching the match. Again.{/color}"
    show bg hy_bedroom onlayer bgl
    "Back through the wall, your nightstand drawer's open an inch."
    "A bottle of lube in it, and a pink plug, washed, on a folded cloth."
    $ hy_induct()
    "{color=#b7b7b7}Liam's, obviously. He must have run out of drawer.{/color}\n{size=-5}{color=#ff8fa3}▸ Back through the wall{/color}{/size}"
    $ vn_pass(max(60, hy_to_tonight(19)))
    $ hy_end()
    jump hy_hub

label hy_out:
    ## rungs.twee: :: Hypno Out [vn]
    $ hy.fit = "mini"
    ## RUNG 5 -- a lost weekend. IN TRANCE, out in public, on a Friday or Saturday night (revamp, owner 2026-10-20). The cashier hears "girlfriend"; Cass on the stairs asks, Emily says "Yes!", and the pronouns change once, for good, with the cock on. Then home, and the weekend goes. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_advance(5)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    $ _hy_sens = hy_body(5)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    show bg hy_bedroom onlayer bgl
    show hy_pc neutral at vn_pc_slot
    show hy_liam stern at vn_cast_slot
    show cg hy_trigger_out onlayer cgl
    $ hy.fit = None
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    hy_liam "{=hy_hypno}“Tonight you're going out with me. Not hiding. Wear the hottest thing you own. Want every eye on you.”{/=hy_hypno}"
    hy_liam "{=hy_hypno}“And when I call you my girlfriend, know I mean it.”{/=hy_hypno}"
    hide cg onlayer cgl
    show hy_pc eager at vn_pc_slot
    $ vn_face("hy_liam", "smile")
    $ hy.fit = "mini"
    "Heat comes up through you from between your thighs."
    hy_emily "\"Out? Out out? With you? Like a {i}date{/i}?\""
    "Emily's on her feet. She throws her arms round his neck."
    hy_emily "\"Yes. Yes! I want them to see what you made.\"" with vnfx("shake")
    hide hy_liam
    "{color=#ff5fb8}The vanity. You shave your legs again though they don't need it, humming.{/color}"
    "{color=#ff5fb8}Lashes thick, liner flicked, mouth painted.{/color}"
    "{color=#ff5fb8}Your own hair pulls into one high tail now, and the platinum clips in at your temples, a ribbon round each, bouncing off your bare shoulders.{/color}"
    $ hy.fit = "mini"
    show cg hy_sa_growout onlayer cgl
    "{color=#ff5fb8}A satin mini that stops right where your ass starts, and your ass {i}starts{/i} now: round and high, popping out over the hem whenever you shift.{/color}"
    if hy.full:
        "{color=#ff5fb8}Thighs pillowy, pressed together. A white tank you can see straight through, no bra, and your breasts fill it, heavy, bouncing, pink tips pushing at it. Gold heels.{/color}"
    else:
        "{color=#ff5fb8}Thighs pillowy, pressed together. A white tank you can see straight through, no bra, pink tips pushing at it. Gold heels.{/color}"
    "{color=#ff5fb8}There's a girl in the mirror, and she's gorgeous, and she's you.{/color}"
    vn_sfx "Smack."
    "{color=#ff5fb8}You turn sideways and slap your own ass. It jiggles for ages.{/color}"
    hy_emily "{color=#ff5fb8}\"Oh my {i}god{/i}. Look at it. {i}Look{/i} at it, Liam!\"{/color}"
    "{color=#ff5fb8}You squeal. You grab it with both hands and it spills over them, fat and high.{/color}"
    "{color=#ff5fb8}Your thighs squish together when you bounce on your heels. Your own hair, long enough to tie now, swings in its tail.{/color}"
    "You know how to stand, too. Hip out, back arched, chin down, looking up through your lashes."
    "You've always known."
    "{color=#ff5fb8}You can feel the cage under the satin, though.{/color}"
    hy_liam "{color=#ff5fb8}\"Not enough left in there to call a cock.\"{/color}"
    "{color=#ff5fb8}Liam says it fondly.{/color}"
    "You go red to your collarbones, and then you giggle, because he's right: it's a soft little nothing that drips every time you squeeze your ass."
    show hy_pc trance at vn_pc_slot
    menu:
        hy_emily "\"It's {i}useless{/i}. It's so cute.\""
        "Take his arm":
            $ hy.flav = "arm"
            $ vn_pass(30)
            jump hy_street
        "Walk half a step ahead, so they see you first":
            $ hy.flav = "ahead"
            $ vn_pass(30)
            jump hy_street

label hy_street:
    ## rungs.twee: :: Hypno Street [vn]
    $ hy.fit = "mini"
    $ vn_enter(bg="hy_highstreet", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_highstreet onlayer bgl
    show hy_pc eager at vn_pc_slot
    show hy_liam smile at vn_cast_slot
    "The High Street, a weekend night. Neon, kebab-shop light, bars spilling onto the pavement."
    if hy.flav == "ahead":
        vn_sfx "Click. Click. Click."
        "You walk half a step ahead so they see you first. Heels click. Tails swing."
        "Your ass rolls under the satin, and you put more swing in it every time you hear a laugh behind you."
    else:
        "You cling to his arm like it's your first date, laughing at nothing."
        "His hand drops to your ass in front of everyone and squeezes."
        hy_emily "\"Eek—! Hehe!\""
        "You squeal and press yourself into his side."
    show cg hy_street_lads onlayer cgl
    "Lads outside the arcade see you coming."
    vn_sfx "Fwee-fwooo."
    "One whistles, long and low. Then they all do."
    hy_unk "\"{i}Damn{/i}, blondie! What are you doing out like that?\""
    hy_liam "{=hy_hypno}“Smile for them. Show off. That's my good little slut.”{/=hy_hypno}"
    "Right in your ear."
    if hy.full:
        "You go hot all over. You smile wide and bright, wave, arch your back so your breasts push at the sheer tank, nipples dark through it."
    else:
        "You go hot all over. You smile wide and bright, wave, arch your back so your buds push at the sheer tank."
    hy_emily "\"{i}Hiii{/i}, boys!\""
    "Every whistle goes into you like a shot. Your cage drips in the satin."
    show cg hy_lingerie onlayer cgl
    "A lingerie shop with its lights still on."
    "He holds lace and straps and scraps of mesh against you in front of the shop girls, turning you with a hand on your waist while they smirk."
    "You go up on your tiptoes for him, arms up."
    hy_emily "\"That one, that one, oh, {i}and{/i} that one—\""
    "At the till, the cashier takes in your tails, your tank, the armful of pastel."
    hy_unk "\"Find everything you needed?\""
    "Liam pulls you into his side."
    hy_liam "{=hy_hypno}“My girlfriend loves to put on a show,”{/=hy_hypno} he says, not bothering to keep it down."
    vn_sfx "{i}Girlfriend.{/i}" with vnfx("shake")
    "It goes off inside you like a firework."
    hy_emily "\"I {i}do{/i}. I really do.\""
    "You beam at the cashier. Her eyebrows climb. She bags it anyway."
    show cg hy_street_kiss onlayer cgl
    "Outside, he kisses you hard, fist round one of your tails, pulling till your scalp tingles."
    "You kiss back on your tiptoes, moaning into his mouth in the middle of the pavement."
    hy_liam "\"You look like you could come just from being seen.\""
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Please, Master. Take me home. Take me home and do {i}everything{/i}.\""
    "You whimper it.\n{size=-5}{color=#ff8fa3}▸ Home{/color}{/size}"
    $ vn_pass(30)
    jump hy_stairs

label hy_stairs:
    ## rungs.twee: :: Hypno Stairs [vn]
    $ hy.fit = "mini"
    ## The pronouns change once, in public, with the cock on (spec, Body; as at Ship's Stores rung 4). Cass is the only person in the story who isn't in on it. "Is this your girlfriend?" Emily: "Yes!" (revamp, owner 2026-10-20). VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_stairwell", pc="trance", pc_tag="hy_pc", cast=[("hy_cass", "neutral")], cg=None)
    show bg hy_stairwell onlayer bgl
    show hy_pc eager at vn_pc_slot
    hide hy_cass
    show cg hy_stairs onlayer cgl
    "Cass from downstairs is coming up with her shopping."
    "She stops on the landing to let you past, smiles, then looks properly."
    hide cg onlayer cgl
    show hy_cass neutral at vn_cast_slot
    hy_cass "\"Oh, hiya, Liam!\""
    "Delighted, not suspicious at all. The tails, the heels, the lingerie bag, his arm round your waist."
    hy_cass "\"God, sorry, I didn't... is this your girlfriend?\""
    hy_emily "\"Yes!\"" with vnfx("shake")
    "You say it before he can open his mouth. You stick your hand out."
    hy_emily "\"Hi! I'm Emily. I'm his girlfriend.\""
    hy_liam "\"Yeah.\""
    "His arm tightens round your waist."
    hy_liam "\"She is.\""
    "One word. Easy."
    "Cass shakes your hand."
    hy_emily "\"I {i}love{/i} your coat!\""
    hy_cass "\"Aw! I love your hair.\""
    "She's lived below Ethan since the spring. She's taken in his parcels."
    "She never looks twice. She chats about the bins."
    hy_cass "\"Lovely to meet you, Emily.\""
    "She means it, and goes down."
    hide hy_cass
    "The most ordinary conversation of your life, and the best."
    "You bounce on your heels all the way up the last flight. Under the satin, your cage is soaking."
    $ hy.she = True
    "{color=#b7b7b7}From the stairs onward, everybody says \"she\". So do you.{/color}\n{size=-5}{color=#ff8fa3}▸ Up to the flat{/color}{/size}"
    jump hy_door

label hy_door:
    ## rungs.twee: :: Hypno Door [vn]
    $ hy.fit = "mini"
    ## Rung 5's door: on your knees against it. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg="hy_hallway", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "stern")], cg=None)
    show bg hy_hallway onlayer bgl
    show hy_pc eager at vn_pc_slot
    hide hy_liam
    vn_sfx "Click."
    "The flat door's barely shut when he puts you against it."
    show cg hy_door_slap onlayer cgl
    "Hand on the back of your neck. Cheek on the cold paint."
    "His other hand up under the satin, squeezing."
    vn_sfx "SMACK." with vnfx("shake")
    "Then one hard slap. Your ass jiggles. You moan."
    hy_emily "\"{i}Yes{/i}— Master, yes, I've been waiting {i}all night{/i}—\""
    hy_liam "{=hy_hypno}“On your knees.”{/=hy_hypno}"
    show cg hy_sa_door onlayer cgl
    "You drop. Heels kicked off, skirt round your hips, tails down your bare back, mouth already open."
    hy_emily "\"Here? Right here? She's right under— {i}mmf{/i}—\""
    "He feeds you his cock in one smooth push and grabs the base of one tail like a handle."
    hy_liam "{=hy_hypno}“Show me how much you loved being paraded round.”{/=hy_hypno}"
    hy_emily "\"{i}Mmmh{/i}—!\"" with vnfx("shake")
    "So loud the door rattles behind your head."
    vn_sfx "Glk. Glk. Glk."
    "Slow and deep, nose in his stomach, eyes glassy, drool running down onto your tank."
    "You're making noise the whole time, wet and desperate and happy."
    "Cass's flat is right underneath. You hope she hears."
    menu:
        vn_th "(You get louder, just in case.)"
        "Stay on your knees for him":
            jump hy_door_sex
        "Let him pull you up by your tails":
            jump hy_couch

label hy_door_after:
    ## rungs.twee: :: Hypno Door After [vn]
    $ hy.fit = None
    $ vn_enter(bg=None, pc="neutral", pc_tag="hy_pc", cast=[], cg="hy_door_climax")
    show hy_pc eager at vn_pc_slot
    if hy_enc.partner_came:
        $ hy.fit = "mini"
        "He holds your head with both fists in your tails and comes down your throat." with vnfx("flash")
        hy_emily "\"Mmmh— mmhh— {i}mmh{/i}—\""
        "You swallow and swallow and keep your lips on him till he's done, humming your thank-yous round him."
    else:
        "He pulls out of your mouth with a wet pop and smears his cock across your cheek."
        "You chase it with your tongue, giggling."
    $ hy.fit = "mini"
    hy_liam "{=hy_hypno}“Not done. Couch.”{/=hy_hypno}"
    hy_emily "\"Not done!\""
    "Thrilled.\n{size=-5}{color=#ff8fa3}▸ The couch{/color}{/size}"
    jump hy_couch

label hy_couch:
    ## rungs.twee: :: Hypno Couch [vn]
    $ hy.fit = "mini"
    ## Intercourse between the thighs has no director act (spec, Engine work), so it stays authored. Over the cage, never in her. In trance, eager: she begs for him, and he still won't. Then the morning, one word, and the weekend goes. VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_lounge", pc="trance", pc_tag="hy_pc", cast=[], cg=None)
    show bg hy_lounge onlayer bgl
    show hy_pc eager at vn_pc_slot
    show hy_liam stern at vn_cast_slot
    "He drags you up by your tails and drops you on your back on the couch."
    hide hy_liam
    if hy.full:
        ## THE FULL REGIMEN's rung 5 beat (owner, 2026-11-11): before the thighs, he plays with
        ## nothing but her breasts until she comes from them alone.
        "Skirt round your waist, tank rucked up under your arms, and your breasts spill out of it, heavy, nipples hard and aching."
        "For once he doesn't go for your thighs."
        show cg hy_couch_breasts onlayer cgl
        "He kneels over you and takes them in both hands, weighing them, like a man checking what he's been sent."
        hy_emily "\"{i}Mmh{/i}— Master—\""
        hy_liam "{=hy_hypno}“Hands over your head. Don't move them.”{/=hy_hypno}"
        "You don't. You grip the arm of the couch and arch up into his palms."
        vn_sfx "Squeeze."
        "He squeezes. He rolls your nipples between finger and thumb, slow, then pinches, and the sound you make isn't a word at all."
        hy_emily "\"{i}Ahh{/i}— ah— they're so— Master, they're so {i}sensitive{/i}, I can't, I {i}can't{/i}—\""
        hy_liam "\"Look at you. Look what you grew for me.\""
        "His mouth on one, sucking hard; his hand on the other, kneading. Your caged cock leaks on your stomach, and nobody touches it."
        hy_liam "{=hy_hypno}“You'll come from these. Only these.”{/=hy_hypno}"
        hy_emily "\"I will— I will, I'll come for you, from my {i}tits{/i}, Master, {i}please{/i}—\""
        vn_sfx "Shlrp. Shlrp."
        "He switches sides. Then back. Then he bites, just teeth, just enough."
        show cg hy_couch_breasts_cum onlayer cgl
        hy_emily "\"{i}AHHH{/i}— Master— I'm— from my {i}tits{/i}— I'm {i}coming{/i}—!\"" with vnfx("flash")
        "You come with your hands still over your head, back bowed off the couch, the cage pulsing thin and useless and his mouth still on you."
        "He doesn't stop until you're sobbing it, and then a little after."
        vn_th "(You asked for these. You'd ask again.)"
        hide cg onlayer cgl
        "Then he pins your wrists over your head with one hand, and you squirm under it, still shaking, grinning up at him."
    else:
        "Skirt round your waist, tank rucked under your arms, buds out, nipples hard."
        "He pins your wrists over your head with one hand, and you squirm under it, grinning up at him."
    hy_liam "{=hy_hypno}“Legs together.”{/=hy_hypno}"
    "Your thighs press together, soft and slick."
    show cg hy_couch onlayer cgl
    "He spits in his palm, slicks the gap, and pushes his cock into it, right over the cage."
    vn_sfx "Shlk."
    "The head slides out between your thighs every stroke and bumps your caged cock, hard plastic against him."
    "You can't touch it. You don't want to. You {i}squeal{/i} with how good it is."
    hy_emily "\"{i}Ahh{/i}— ah, Master— oh {i}fuck{/i}, oh fuck, your cock, between my {i}thighs{/i}—\""
    hy_liam "{=hy_hypno}“Squeeze.”{/=hy_hypno}"
    "You squeeze till you shake: tight on the way in, loose on the way out, and you never had to learn it."
    vn_sfx "Pap. Pap. Pap."
    "He lets go of one wrist, and your hand goes straight behind his cock, fingers on your hole, rubbing, pushing, desperate."
    vn_th "(Because it's empty. Because he still won't.)"
    hy_emily "\"Please. Please, Master, I want it, I want {i}you{/i}, inside, I've been so good, {i}please{/i}—\""
    hy_liam "\"Not yet.\""
    "Harder."
    hy_liam "{=hy_hypno}“Say what you are.”{/=hy_hypno}"
    hy_emily "\"Your slut— your {i}sissy{/i}— your girlfriend, your show-off, your Emily, your— {i}ahhh{/i}—!\"" with vnfx("shake")
    "The whole list, at the top of your lungs, proud of every word, the cage leaking all over your stomach."
    show cg hy_couch_cum onlayer cgl
    if hy.full:
        "He pulls out and comes on your breasts: both of them, your nipples, your throat, hot and heavy." with vnfx("flash")
    else:
        "He pulls out and comes on your chest: buds, nipples, throat, hot and heavy." with vnfx("flash")
    "You come with him, caged, untouched, hips bucking off the couch while it dribbles out of you thin and useless."
    hy_emily "\"{i}Thank you{/i}— thank you— {i}Master{/i}—!\""
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Didn't even need it. It doesn't {i}do{/i} anything. I love that.\""
    "You giggle it, panting."
    hy_liam "{=hy_hypno}“Worship your mess.”{/=hy_hypno}"
    vn_sfx "Pat."
    "He slaps your thigh."
    show cg hy_couch_worship onlayer cgl
    "Your fingers go into your mouth, every drop, with little moans of thanks."
    "Then you kiss the tip of his cock, softly, like it's something precious."
    ## Saturday morning (the clock walks the weekend with the prose, 2026-11-12)
    $ vn_pass(hy_to_tomorrow(9))
    show bg hy_kitchen onlayer bgl
    $ hy.fit = "cami"
    show cg hy_morning_coffee onlayer cgl
    "In the morning you're in the kitchen in the camisole and nothing else, still under, humming, making his coffee."
    "He comes up behind you and says one word in your ear."
    hy_liam "{=hy_hypno}“Slut.”{/=hy_hypno}"
    "And the rest of the weekend goes.\n{size=-5}{color=#ff8fa3}▸ The weekend{/color}{/size}"
    $ vn_pass(30)
    jump hy_weekend

label hy_weekend:
    ## rungs.twee: :: Hypno Weekend [vn]
    $ hy.fit = "cami"
    ## Rung 5's lost weekend, in pieces, IN TRANCE (revamp, owner 2026-10-20): Emily's whole weekend, every piece of it eager. His mouth and his fingers, never his cock in her: that is the fork's. Then the wipe on Sunday night, and Ethan's Monday: three days missing, a mini in the hamper. VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_kitchen", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc eager at vn_pc_slot
    hide hy_liam
    "It just goes, and Emily has the best weekend of her life."
    show cg hy_counter onlayer cgl
    "The kitchen counter. You on it in the camisole, knees spread, heels on the cupboard doors."
    if hy.full:
        "His mouth on your breasts, one nipple then the other, teeth just touching, until they're swollen and wet and you're squealing at the ceiling."
    else:
        "His mouth on your buds, one then the other, teeth just touching, until they're swollen and wet and you're squealing at the ceiling."
    hy_emily "\"{i}Ah{/i}— ah— Master, they're— {i}more{/i}, they're so—\""
    "Two fingers curled in you. Your caged cock drooling on the worktop."
    "Slut and sissy and yours, louder every time he bites."
    hy_liam "{=hy_hypno}“Whose?”{/=hy_hypno} he says against your chest."
    hy_emily "\"{i}Yours{/i}—!\""
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}" with vnfx("shake")
    hy_emily "\"Yours, yours, I'm yours, I'm your {i}slut{/i}, I'm your {i}girlfriend{/i}—!\"" with vnfx("shake")
    show cg hy_counter_cum onlayer cgl
    vn_sfx "Click." with vnfx("flash")
    "The kettle clicks off the exact moment you come, shaking, untouched, wailing."
    vn_th "(Kettles will never be the same.)"
    show bg hy_bathroom onlayer bgl
    show cg hy_bath onlayer cgl
    "The bath. Between his knees in hot water, back against his chest."
    if hy.full:
        ## THE FULL REGIMEN's rung 6 beat (owner, 2026-11-11): the bath, expanded.
        show cg hy_bath_soap onlayer cgl
        "They float. You'd never thought about that: heavy all day, and in the water they lift, pale and buoyant, nipples just breaking the surface."
        "He soaps his hands and takes them from behind, slow circles, the lather sliding over the tops of them."
        hy_emily "\"{i}Mmmh{/i}... Master...\""
        "He lifts them, lets go, and watches them bob. You giggle, and then gasp, when his thumbs find your nipples under the suds."
        hy_liam "{=hy_hypno}“Whose are these?”{/=hy_hypno}"
        hy_emily "\"Yours.\""
        hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}"
        hy_emily "\"{i}Yours{/i}! They're yours, Master, I grew them for you, I {i}asked{/i} for them for you—\"" with vnfx("shake")
        "He pinches and rolls and pinches while the water slops at the rim, and you squirm back against his cock, hard against the small of your back."
        hy_liam "\"That's it. Good girl. Give it to me.\""
        hy_emily "\"Ah— ah— {i}Master{/i}— I'm going to— in the {i}bath{/i}—\""
        show cg hy_bath_cum onlayer cgl
        vn_sfx "Splash." with vnfx("flash")
        hy_emily "\"{i}Ahhhh{/i}—!\""
        "You come with his hands full of you, kicking water over the side, wailing at the tiles."
        "He holds them through all of it, and after."
        show cg hy_bath onlayer cgl
    "He washes your hair, your own and the floating platinum, slow, rinsing with a cup."
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Mmmmm...\""
    "You hum, boneless. He's kind to you for an hour, the way he always is after. That's the currency."
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he says into your wet hair."
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Say it again.\""
    "You beg, and wriggle round to kiss him."
    "He does."
    show bg hy_hallway onlayer bgl
    show cg hy_hallfloor onlayer cgl
    "The hall floor, on your knees, door chain on, mouth full. The couch again."
    show bg hy_bedroom onlayer bgl
    show cg hy_mirror_bed onlayer cgl
    "Your bed, the vanity mirror turned to face it so you can watch: mascara everywhere, mouth open."
    hy_emily "\"More— more— MORE—\""
    "Louder and louder, begging for more, until it doesn't sound like anything but happy."
    hide cg onlayer cgl
    "Then dark and quiet."
    $ vn_pass(hy_to_weekday(1, 22))
    show cg hy_towel_night onlayer cgl
    "Sunday night, your own bed, hair in a towel. He kisses your forehead."
    hy_liam "{=hy_hypno}“Forget. Wake up Monday.”{/=hy_hypno}"
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Love you...\""
    "Emily mumbles it, and goes."
    $ hy_induct()
    hide cg onlayer cgl
    show hy_pc nervous at vn_pc_slot
    pass
    "—"
    ## Monday, seven o'clock: the alarm is Monday's on the clock too
    $ vn_pass(hy_to_monday(7))
    $ hy.fit = None
    vn_sfx "Beep beep. Beep beep."
    "Your alarm. Your phone says Monday. The last thing you remember is Friday."
    "{color=#b7b7b7}Three days. Must have been a bug going round. Liam says you slept through it.{/color}"
    "There's a satin mini in the laundry hamper, black, and gold heels kicked under your bed."
    "{color=#b7b7b7}Liam's girlfriend's, obviously. Emily. Nice of her to stay over and look after you.{/color}"
    "{color=#4372ff}Mike: u alive?? missed u at league again{/color}"
    ## Hair in a towel by Sunday night: the weekend's face is washed off before work.
    "Phone face-down. You'll answer him tomorrow.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ hy_end()
    jump hy_hub

label hy_fork:
    ## endings.twee: :: Hypno Fork [vn]
    $ hy.fit = "cami"
    ## RUNG 6 -- it does not end. Ethan's last waking evening is residue, every piece of it explained wrongly; then the six words, and Emily, and the phone (revamp, owner 2026-10-20). VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ hy_advance(6)
    $ hy_start()
    $ vn_enter(bg="hy_bedroom", pc="trance", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    $ _hy_sens = hy_body(6)
    if _hy_sens:
        "{color=#ff5fb8}[_hy_sens]{/color}"
    show bg hy_bedroom onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_liam
    $ hy.fit = None
    "You're at the vanity brushing out your hair when it starts."
    show cg hy_sa_growfinal onlayer cgl
    "{color=#ff5fb8}Your own hair. The extensions have been in a drawer for a week; you don't need them.{/color}"
    "{color=#ff5fb8}Two high tails without looking. Your ass fills the stool. Thighs soft and heavy under the camisole.{/color}"
    if hy.full:
        "{color=#ff5fb8}Your breasts are what the full regimen made them, large and heavy, and nobody held them anywhere.{/color}"
    else:
        "{color=#ff5fb8}Your chest is what it's been since the pills started, two puffy buds, held exactly there.{/color}"
    "{color=#ff5fb8}The cage sits snug. You stopped noticing it, like a ring.{/color}"
    "{color=#ff5fb8}You stand up and the stool comes with you for a second.{/color}"
    "{color=#ff5fb8}Your ass is {i}enormous{/i} now: round and heavy and wobbling every time you shift your weight.{/color}"
    "{color=#ff5fb8}Your thighs squish together all the way to the knee. Your tails swing down past your shoulder blades, thick and soft.{/color}"
    "{color=#ff5fb8}Under your panties the cage drips. A tiny soft nothing in there, not even trying.{/color}"
    "{color=#b7b7b7}Squats. The pills. A bet you lost. Medical.{/color}"
    "You've an answer for every bit of it, and none of them takes more than a second."
    "An ordinary evening. Work, where everyone uses the old name and nobody blinks at the tails any more. Dinner."
    vn_sfx "Bzzt."
    "Mike texted {color=#4372ff}pub??{/color} and you put the phone in the vanity drawer."
    show hy_liam stern at vn_cast_slot
    "He sits on the end of your bed and says it."
    show cg hy_trigger_fork onlayer cgl
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    "It drops over you like a warm bath. Ethan goes, the way he always goes."
    "This time there's no end time at all."
    "—"
    show hy_pc trance at vn_pc_slot
    $ hy.fit = "cami"
    "You're under, and Emily is all that's in there: warm, soft, entirely his, and happy about it."
    hide cg onlayer cgl
    "Tails spread on the pillow, hands folded on your stomach, a small happy smile."
    "You're waiting for him to tell you what's next. Whatever it is, you'll love it."
    show cg hy_fork_phone onlayer cgl
    "He sits on the floor beside the bed, phone in both hands, looking at two things."
    "The wake command: a soft round button that says WAKE."
    "Press it, and Ethan comes up, and remembers what he's told."
    "And further down, small, a toggle that's been on since the first night. {color=#e40081}Hold session until woken.{/color}"
    "He has never once turned it off."
    "He looks at you a long time."
    "Since the spring he's been the one standing slightly behind you. Now there's nothing in front of him at all."
    $ hy_induct()
    menu:
        "His phone is in his hands. The choice is in yours."
        "Wake her. Tell her everything." (ending=True):
            jump hy_end_listen
        "Don't." (ending=True):
            jump hy_end_never

label hy_end_listen:
    ## endings.twee: :: Hypno End Listen [vn]
    $ hy.fit = "cami"
    ## Ending A (hypno-brother): woken, told everything, and asked. The one ending in which you are a person with all the information. Amnesia cleared; the loop goes off at last. VN script.
    $ hy.ending = "listen"
    $ hy.aware = True
    $ hy.done = True
    $ hy.fog = 0
    $ vn_enter(bg="hy_bedroom", pc="neutral", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc nervous at vn_pc_slot
    show hy_liam stern at vn_cast_slot
    vn_sfx "Tap."
    $ hy.fit = None
    "He presses WAKE."
    "You surface blinking, tails on the pillow, his face over you, white."
    if hy.full:
        show cg hy_listen_wake onlayer cgl
        "You sit up, and they move with you: heavy, warm, yours, and nothing in the world to explain them with now."
        hide cg onlayer cgl
    "Before you've sat up he starts talking."
    "All of it. Badly, for hours, in the wrong order."
    "The hoodie on the kitchen chair. The first night, the razor, the dryer."
    "Emily. The name she gave herself, on camera, with nobody asking."
    "The card for the Bloom, and the clinic: him in the waiting room feeding you answers through the open door while a kind, careful woman wrote them down."
    if hy.full:
        "Then he stops, and starts again."
        hy_liam "\"Except one. The regimen. I had you saying {i}just a little{/i}. You said {i}everything{/i}.\""
        hy_liam "\"That one wasn't me.\""
        "You look down at yourself. There's no not looking, now."
    "The cage. The weekend. He leaves nothing out."
    "He turns the phone round and shows you the whole panel: the modules, and the Amnesia Loop he's just switched off for the first time."
    "Under them, the log. Every session, every end time. And at the bottom, the one with no end time at all."
    "Then he shows you the video."
    hy_unk "\"{i}Hi! I'm Emily!{/i}\""
    "A girl with your face kneels up on your bed and waves at the camera."
    "You don't remember a second of it. You believe every second of it."
    "You ask a few things. Mostly dates. The last one:"
    hy_ethan "\"Did you ever think about stopping?\""
    show hy_liam neutral at vn_cast_slot
    hy_liam "\"Yes.\""
    hy_liam "\"Twice.\""
    "You believe him. That's worse and better at once.\n{size=-5}{color=#ff8fa3}▸ The week{/color}{/size}"
    $ vn_pass(30)
    jump hy_listen_week

label hy_listen_week:
    ## endings.twee: :: Hypno Listen Week [vn]
    $ hy.fit = "jumper"
    ## End Listen's week: the app on the kitchen table between you. Then Ethan, knowing all of it, chooses her -- awake, without the words (revamp, owner 2026-10-20). VN script.
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_liam
    "Then you sit with it for a week."
    "Work. Home. Your own bed. You don't let him touch you."
    "You don't delete the app, and you don't let him touch that either."
    "It lives on the kitchen table between you, face up. You eat your dinners either side of it."
    "Neither of you mentions it. Both of you keep looking at it."
    show bg hy_bedroom onlayer bgl
    show cg hy_week_video onlayer cgl
    "You watch the video again, on your own, more than once."
    hy_unk "\"{i}Hi! I'm Emily!{/i}\""
    "She's so {i}happy{/i}."
    hide cg onlayer cgl
    show bg hy_kitchen onlayer bgl
    ## the clock walks the week with the prose (2026-11-12): the Monday after, then each day it names
    $ vn_pass(hy_to_weekday(2, 7))
    "Monday morning, the little white pill, and you stop with the glass halfway."
    "Because now you know what it is, and who chose it."
    vn_sfx "Gulp."
    "Then you take it. You watch yourself take it."
    "That's different. That's yours."
    if hy.full:
        $ vn_pass(hy_to_weekday(3, 11))
        show bg hy_highstreet onlayer bgl
        show cg hy_listen_fitting onlayer cgl
        "Tuesday, you go into the shop on the High Street on your own and let a woman with a tape measure tell you your size."
        "She says it like a fact, not a question. You buy three, and wear one out of the shop."
        hide cg onlayer cgl
    $ vn_pass(hy_to_weekday(4, 18))
    show bg hy_stairwell onlayer bgl
    show hy_cass neutral at vn_cast_slot
    "Wednesday, Cass passes you on the stairs."
    hy_cass "\"Hiya, Emily!\""
    show hy_pc happy at vn_pc_slot
    hy_ethan "\"Hiya!\""
    "You say it back, in the voice, because you chose to."
    hide hy_cass
    "You go upstairs and sit on your floor grinning like an idiot."
    $ vn_pass(hy_to_weekday(5, 20))
    show bg hy_pub onlayer bgl
    $ hy.fit = "jumper"
    show cg hy_week_bell onlayer cgl
    "Thursday, Mike at the Bell. Jeans, big jumper, one tail."
    "He looks at you a long moment."
    hide cg onlayer cgl
    show hy_mike neutral at vn_cast_slot
    hy_mike "\"You look—\""
    "He stops."
    hy_mike "\"Different. Good. Happy?\""
    show hy_pc happy at vn_pc_slot
    hy_ethan "\"Yeah.\""
    "You find it's true, with all the facts in your hands."
    hy_ethan "\"Yeah, I think I am.\""
    "He nods, decides not to ask, and buys you a drink."
    show bg hy_kitchen onlayer bgl
    pass
    hide hy_mike
    show hy_liam neutral at vn_cast_slot
    $ hy.fit = None
    $ vn_pass(120)
    "When you get home Liam's at the kitchen table with the phone in front of him, not touching it."
    show cg hy_week_table onlayer cgl
    "You sit opposite him. Hands flat on the table."
    show hy_pc neutral at vn_pc_slot
    hy_ethan "\"Don't say it.\""
    hy_ethan "\"Not the words. Not tonight. I want to do this awake. I want to be her on purpose.\""
    "You take a breath."
    show hy_pc happy at vn_pc_slot
    hy_ethan "\"Call me Emily.\""
    $ vn_pass(10)
    jump hy_listen_ride

label hy_listen_ride:
    ## endings.twee: :: Hypno Listen Ride [vn]
    $ hy.fit = "cami"
    ## The climax, AWAKE and asked for (revamp, owner 2026-10-20): no trigger said. Tongue first, then you ride him. His cock in your ass, at last, on the page. VN script; awake, so the faces carry no glow: the plate is Emily because she asked to be.
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc neutral at vn_pc_slot
    show hy_liam neutral at vn_cast_slot
    $ hy.fit = None
    "He picks up the phone anyway, out of habit. The six words are right there on the screen, ready:"
    hy_liam "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    show cg hy_phone_down onlayer cgl
    "You put your hand over it and push it face-down on the table."
    hy_liam "\"Emily.\""
    "He says it instead. His voice cracks on it."
    show hy_pc happy at vn_pc_slot
    hy_emily "\"Yes.\""
    $ hy.fit = "cami"
    "Awake. All of you. Nobody's taking anything."
    "You're handing it over, on purpose, with your eyes open."
    hy_emily "\"Yes. Bedroom.\""
    hide cg onlayer cgl
    show bg hy_bedroom onlayer bgl
    hide hy_liam
    "He lays you back, tails fanned on the pillow, and slides your panties down, kissing the inside of one knee, then the other."
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg hy_listen_rim onlayer cgl
    "Then he pushes your thighs up and apart and puts his mouth on you."
    "On your hole. His tongue, flat and wet, circling, then pressing {i}in{/i}."
    hy_emily "\"{i}Ahh{/i}—! Oh— oh, Master, oh {i}fuck{/i}—\"" with vnfx("shake")
    "Fists in the duvet, hips rolling up into his face."
    vn_sfx "Shlk. Shlk."
    "Long lavish licks, then the point of his tongue working into you."
    "You're wailing, {i}loud{/i}, louder than she ever was on that video, and every bit of the noise is yours."
    "Your caged cock leaks a puddle on your stomach."
    hy_emily "\"Please— please, I want it, I want {i}you{/i}, Master, I'm asking, I'm {i}asking{/i}— {i}ahh{/i}—\""
    show hy_liam smile at vn_cast_slot
    "He lifts his head, mouth wet."
    hy_liam "\"I heard.\""
    hy_emily "\"Then {i}do{/i} it.\""
    "You moan it."
    hide cg onlayer cgl
    hy_liam "\"Up. On my lap.\""
    if hy.full:
        "You climb on. Thighs either side of his, tails swinging against his cheeks, your breasts swaying against his chest."
    else:
        "You climb on. Thighs either side of his, tails swinging against his cheeks, buds brushing his chest."
    "You reach back and find him, hot and thick, and hold the head of him right against your wet hole."
    hy_liam "\"Look at me.\""
    "You look at him, wide awake, and you start to sink down."
    hy_liam "{=hy_hypno}“Good girl,”{/=hy_hypno} he says, and his voice cracks on that too.\n{size=-5}{color=#ff8fa3}▸ Ride him{/color}{/size}"
    jump hy_listen_sex

label hy_listen_after:
    ## endings.twee: :: Hypno Listen After [vn]
    $ hy.fit = None
    ## End Listen's climax, after the director scene. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg=None, pc="neutral", pc_tag="hy_pc", cast=[], cg="hy_listen_climax")
    show hy_pc happy at vn_pc_slot
    show cg hy_sa_listenride onlayer cgl
    "You ride him till the bed's banging the wall."
    vn_sfx "Bang. Bang. Bang."
    hy_emily "\"I'm yours— I'm yours, I'm your girl, I'm your Emily, I {i}asked{/i} for this— {i}ahh{/i}— Master, I asked—\""
    hy_liam "\"I know. I know you did.\""
    "He's holding your hips."
    hy_liam "{=hy_hypno}“Louder.”{/=hy_hypno}" with vnfx("shake")
    "Your hips know the rhythm before you do. Drop, roll, squeeze."
    "You never practised that awake. You just know."
    "You come untouched. Caged, hands on his chest, tails flying, his cock buried in you." with vnfx("flash")
    "Clenching round him in long helpless waves while your cock dribbles out of the cage onto his stomach."
    hy_emily "\"EMILY— {i}MASTER{/i}— AHHHH—!\"" with vnfx("shake")
    "You scream it: the name nobody gave you and the word he did."
    "He comes with you, deep, holding you down on him, and you moan at how much you want to feel it."
    "He glances down at the cage, soft and tiny and still leaking on him."
    hy_liam "\"Useless.\""
    "Fondly."
    hy_emily "\"I {i}know{/i}! Isn't it great?\""
    "You laugh, wrecked."
    show cg hy_listen_chest onlayer cgl
    "After, you lie on his chest with him still in you."
    $ _hy_clock = hy_clock()
    "The clock says [_hy_clock]. You'll remember every second of this one."
    "You asked.\n{size=-5}{color=#ff8fa3}▸ Lie there{/color}{/size}"
    $ vn_pass(60)
    $ hy_end()
    jump hy_listen_close

label hy_listen_close:
    ## endings.twee: :: Hypno Listen Close [vn]
    $ hy.fit = "cami"
    ## The ending's record: the route completion, the feat, the locks handed back. VN script.
    $ hy.ending = "listen"
    $ vn_feat("Open and Listen")
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc happy at vn_pc_slot
    show hy_liam smile at vn_cast_slot
    "{color=#38b20a}You kept the name. That part was always yours.{/color}"
    $ vn_pass(hy_to_tomorrow(8))
    show cg hy_toast_morning onlayer cgl
    "Morning. The app's on the kitchen table, face up. Neither of you touches it."
    "You make the coffee. He makes the toast."
    hy_liam "\"Morning, Emily.\""
    hy_emily "\"Morning!\""
    "He says your new name, and you answer in the voice."
    hide cg onlayer cgl
    "The cage stays on. You asked about that too, in the week, and decided."
    "It drips in your knickers while you butter the toast."
    hy_emily "\"Doesn't do anything anyway.\""
    "You giggle, and he kisses the top of your head."
    menu:
        "One more thing to decide. He lets you decide it."
        "Stay" (ending=True):
            jump hy_epilogue_stay
        "Go, one door down the landing" (ending=True):
            jump hy_epilogue_go

label hy_epilogue_stay:
    ## endings.twee: :: Hypno Epilogue Stay [exitCheckBypass vn]
    $ hy.fit = None
    ## exitCheckBypass, here and on the go epilogue and End Never's close: in a route save the last link is <<route_return>>'s "Choose another story" (<<hypno_return>>), a restart rather than a passage link, which DoL's footer would report as no way out. VN script.
    $ hy.epilogue = "stay"
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cast=[], cg=None)
    show bg hy_kitchen onlayer bgl
    show hy_pc happy at vn_pc_slot
    "You stay."
    "Of course. It's your flat. Both your names on the lease, the vanity under your window, the thinnest wall in the world."
    "Work. Home. Mike at the Bell on Thursdays; he's stopped asking. Cass says hiya, Emily."
    show hy_ruth neutral at vn_cast_slot
    "Dr. Adair asks her question at every refill, and now you answer it honestly:"
    hy_emily "\"Not any more. I do my own talking now.\""
    "She smiles properly at that."
    hide hy_ruth
    show hy_liam smile at vn_cast_slot
    "Some nights he says the words. Most nights you ask first."
    show cg hy_key_fridge onlayer cgl
    "The key to the cage hangs on a hook by the fridge where either of you could reach it; neither of you ever does."
    "The app stays face up on the table."
    "Now and then one of you picks it up, looks at the toggle at the bottom, {color=#e40081}Hold session until woken{/color}, and puts it down again.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump hy_route_return

label hy_epilogue_go:
    ## endings.twee: :: Hypno Epilogue Go [exitCheckBypass vn]
    $ hy.fit = None
    $ hy.epilogue = "go"
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cast=[], cg=None)
    show bg hy_hallway onlayer bgl
    show hy_pc happy at vn_pc_slot
    $ hy.home = "friendflat"
    "You go."
    "Not far. Your league friend has a flat one door down the landing, a spare room, and a key they've been meaning to give someone."
    show cg hy_vanity_move onlayer cgl
    "You carry the vanity across a drawer at a time and hang the panties in rows."
    hide cg onlayer cgl
    show bg hy_bedroom onlayer bgl
    "Your own room, your own wall. Somebody else on the other side of it now."
    "The cage came with you, and the key stayed with him, and you haven't missed either."
    "But it's one door down."
    "Some nights, in bed, you hear him through two walls, saying six words to nobody."
    hy_unk "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    "Close enough that they still work.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump hy_route_return

label hy_end_never:
    ## endings.twee: :: Hypno End Never [vn]
    $ hy.fit = "cami"
    ## Ending B (open-and-listen): he never gives the command. The session doesn't end; there is no wake command scheduled and no timer on it. Amnesia pinned at 5, no timer. Emily is all that's left, happily (revamp, owner 2026-10-20). VN script (framework/vn-script.js).
    $ hy.ending = "never"
    $ hy.done = True
    $ hy.fog = 5
    $ vn_enter(bg="hy_bedroom", pc="trance", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc trance at vn_pc_slot
    show hy_liam neutral at vn_cast_slot
    vn_sfx "Thp."
    "He puts the phone face-down on the carpet."
    "The session doesn't end. There's no moment where it turns permanent."
    "It just keeps not ending, minute after minute, and nobody is in there to mind."
    $ vn_face("hy_liam", "smile")
    "He puts his hand on your stomach, and you sigh and arch into it, smiling up at him."
    hy_liam "{=hy_hypno}“Deeper, Emily. Deeper now. Good girl. You're home.”{/=hy_hypno}"
    hy_emily "\"Yes, Master. Home.\""
    "Soft and high and dreamy, in a whisper."
    hy_liam "{=hy_hypno}“Who are you?”{/=hy_hypno}"
    show cg hy_never_words onlayer cgl
    hy_emily "\"Emily. Your girl. Your good, obedient sissy.\""
    "Worn smooth, like a prayer, and you say it like it's the best news in the world."
    hy_liam "{=hy_hypno}“And whose are you?”{/=hy_hypno}"
    show hy_pc eager at vn_pc_slot
    hy_emily "\"Yours.\""
    if hy.full:
        "Your thighs squeeze together. Your nipples go tight under the camisole, your breasts heavy in it."
    else:
        "Your thighs squeeze together. Your buds go tight under the camisole."
    hy_emily "\"Only yours. Since the flat. I live to make you happy.\""
    hy_liam "\"I know.\""
    "He strokes your cheek."
    hy_liam "\"Stay.\""
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Forever.\""
    "{color=#ec3535}There is no wake command scheduled. There is no timer on it.{/color}"
    jump hy_never_ride

label hy_never_ride:
    ## endings.twee: :: Hypno Never Ride [vn]
    $ hy.fit = "cami"
    ## The climax, inside the session that doesn't end: tongue first, then she rides him. In trance, eager, consensual combat in Emily's voice (revamp, owner 2026-10-20). VN script.
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cast=[("hy_liam", "neutral")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc eager at vn_pc_slot
    show hy_liam smile at vn_cast_slot
    hy_liam "{=hy_hypno}“Lie back for me.”{/=hy_hypno}"
    hide hy_liam
    "You lie back, tails pooled round your head. Your legs part as far as they'll go."
    "Hands folded on your stomach, gazing up with your mouth soft and open, the way you love to wait for him."
    ## (frame added 2026-11-11, owner: "picture every beat")
    show cg hy_never_rim onlayer cgl
    "He slides your panties down, kisses the inside of each thigh, pushes them up and apart, and puts his mouth on your hole."
    hy_emily "\"{i}Oh{/i}— oh, Master— {i}ahh{/i}—!\""
    "His tongue circles you, slow and wet, then presses in."
    "Your hands clutch the duvet and your hips buck up into his face, moaning, wailing with it."
    vn_sfx "Shlk. Shlk. Shlk."
    hy_emily "\"Please— please, Master, eat me, make me your slut, your girl, your twin-tailed— {i}ohh{/i}— please don't stop, please don't {i}ever{/i} stop—!\"" with vnfx("shake")
    "He doesn't. He tongues you open until your hole is fluttering and wet and so empty it throbs."
    "Your caged cock has made a puddle on your stomach."
    hy_liam "{=hy_hypno}“Tell me what you want.”{/=hy_hypno}"
    hy_emily "\"{i}You{/i}.\""
    "It's a wail."
    hy_emily "\"Inside. Please. I've been so good, I've been so good since the flat, please, {i}please{/i}, I've waited so long—\""
    hide cg onlayer cgl
    hy_liam "{=hy_hypno}“Up. On my lap.”{/=hy_hypno}"
    if hy.full:
        "You scramble into his lap, tails brushing his cheeks, your breasts pressed to his chest."
    else:
        "You scramble into his lap, tails brushing his cheeks, buds on his chest."
    "You reach back and hold the head of him hot and slick against your hole, look into his face the way you love to, and start to sink, already moaning."
    hy_liam "{=hy_hypno}“Good girl. Show me how you ride.”{/=hy_hypno}\n{size=-5}{color=#ff8fa3}▸ Ride him{/color}{/size}"
    jump hy_never_sex

label hy_never_after:
    ## endings.twee: :: Hypno Never After [vn]
    $ hy.fit = None
    ## End Never's climax, after the director scene. VN script (framework/vn-script.js); its scene-art lines are kept word for word.
    $ vn_enter(bg=None, pc="neutral", pc_tag="hy_pc", cast=[], cg="hy_never_climax")
    show hy_pc eager at vn_pc_slot
    show cg hy_sa_neverride onlayer cgl
    $ hy.fit = "cami"
    "You ride him like you were made for nothing else."
    hy_emily "\"I'm yours, I'm yours, your sissy, your girl, your good girl— {i}Master{/i}, please— {i}more{/i}— {i}ahh{/i}—!\""
    "Tails flying, bed creaking, his hands on your hips guiding every drop and grind, and you chant it louder every time."
    hy_liam "{=hy_hypno}“That's it. Let go.”{/=hy_hypno}"
    "Your hips know the rhythm before you do. Drop, roll, squeeze."
    "You never learned it. It was put there, and you love it."
    "You come untouched, caged, shuddering, a long high wail, hips bucking wild in his lap while your cock dribbles through the cage onto his stomach." with vnfx("flash")
    hy_emily "\"{i}Thank you{/i}— thank you— {i}MASTER{/i}—!\"" with vnfx("shake")
    "Your hole clutches him and clutches him, and he comes in you, deep and hot and final."
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Didn't even need it...\""
    "You murmur it, while the soft little thing in the cage drools on."
    hy_emily "\"Never needed it.\""
    show cg hy_never_chest onlayer cgl
    "You collapse onto his chest, giggling, still joined. He strokes your hair with both hands buried in your tails."
    "No command to wake. No spiral winding down.\n{size=-5}{color=#ff8fa3}▸ The world goes on{/color}{/size}"
    $ vn_pass(60)
    $ hy_end()
    jump hy_never_close

label hy_never_close:
    ## endings.twee: :: Hypno Never Close [exitCheckBypass vn]
    $ hy.fit = "cami"
    ## The ending's record. Second person to the end, one grey line of Liam, and then the real last line, restored (revamp, owner 2026-10-20): "You are happy. That was never in question." VN script (framework/vn-script.js).
    $ hy.ending = "never"
    $ vn_feat("The Session That Never Ends")
    $ vn_enter(bg="hy_bedroom", pc="trance", pc_tag="hy_pc", cast=[("hy_liam", "smile")], cg=None)
    show bg hy_bedroom onlayer bgl
    show hy_pc eager at vn_pc_slot
    hide hy_liam
    "The world rolls on, inside the session."
    "Work, where you're pleasant to everyone and answer to the old name like it's a nickname. Home. You cook."
    show cg hy_never_vanity onlayer cgl
    if hy.full:
        "Face at the vanity every morning, two tails without looking. Floral dresses, bras you had to be fitted for, berry lipstick."
    else:
        "Face at the vanity every morning, two tails without looking. Floral dresses, padded bras over your buds, berry lipstick."
    show hy_liam smile at vn_cast_slot
    hy_liam "\"My girl.\""
    "He wraps his arms round you from behind and says it into your neck."
    show hy_pc trance at vn_pc_slot
    hy_emily "\"Always.\""
    "You lean back into him."
    "The cage never comes off. The little thing in it never gets hard and never gets touched."
    "When he presses up behind you it just drips, and you giggle."
    "Mike stops texting. You don't notice when."
    "Cass asks after your boyfriend and you blush: he's lovely, he's making dinner."
    "Dr. Adair asks her question at every refill."
    hy_emily "\"He's all right.\""
    "Every time, and you mean it. She writes it down."
    hide cg onlayer cgl
    "Some evenings Liam says six words mid-sentence and you go soft and warm and his."
    "Some evenings he doesn't need to. There's no difference any more."
    "Under all of it, a session is running. Nobody knows. Nobody ever will."
    "{color=#b7b7b7}He spent the whole of the flat being the one behind you. He doesn't look guilty. He looks like a man who finally got his turn.{/color}"
    show cg hy_never_happy onlayer cgl
    "You are happy. That was never in question.\n{size=-5}{color=#ff8fa3}▸ Choose another story{/color}{/size}"
    jump hy_route_return

label hy_bloom_consult:
    ## clinic.twee: :: Hypno Bloom Consult [vn]
    $ hy.fit = None
    ## The consult (see the file header: Dr. Adair is careful and deceived, never complicit or a fool). VN script (framework/vn-script.js).
    $ vn_enter(bg="hy_clinic", pc="nervous", pc_tag="hy_pc", cast=[("hy_ruth", "neutral")], cg=None)
    show bg hy_clinic onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_ruth
    "Frosted glass, lavender. Reception takes your name off the card."
    show hy_liam smile at vn_cast_slot
    "Liam's already in the waiting area. You don't remember telling him the time."
    "Magazine open on his knee, unread. He smiles like you'd arranged to meet."
    hy_liam "\"I'll be right here. Go on.\""
    hide hy_liam
    show hy_ruth neutral at vn_cast_slot
    show cg hy_consult onlayer cgl
    "Dr. Adair is thorough. Grey at the temples, reading glasses on a chain, a voice like a warm hand."
    "She runs long and doesn't apologise for it."
    hy_ruth "\"How long have you been thinking about this?\""
    hy_ruth "\"Support at home?\""
    hy_ruth "\"Is anyone at all pressuring you?\""
    "Through the open door, a magazine not being read."
    hy_unk "{=hy_hypno}Open and listen, now.{/=hy_hypno}"
    "You don't hear him say it."
    show hy_pc trance at vn_pc_slot
    "But the answers start arriving, whole and convincing, and you give them in a calm, pleasant, slightly breathless voice."
    vn_th "(Dr. Adair has no reason in the world to distrust it.)"
    "For years. No, nobody's pressuring you. Yes, you understand it isn't all reversible. Yes, you've read the sheet."
    "Yes, support at home: a good friend, the best. He's in the waiting room."
    hy_ruth "\"And what are you hoping for? Some people want a little softening. Some want everything.\""
    ## THE FULL REGIMEN's split (owner, 2026-11-11): every answer so far was one Liam planted; this
    ## one needn't be. It decides the body, not the ending, so it isn't marked as an ending choice.
    menu:
        "That answer's waiting too, rehearsed and small, ready on your tongue: {i}just a little{/i}."
        "Just a little":
            "\"Just a little,\" you say, exactly as it was given you."
        "More. All of it.":
            $ hy.full = True
            hy_emily "\"More.\""
            "It isn't the answer that was waiting. It comes up from somewhere further down, warm and certain, and it's {i}yours{/i}."
            show cg hy_consult_more onlayer cgl
            hy_emily "\"All of it. Everything. I want to be— {i}full{/i}.\""
            "Through the open door, a magazine page stops halfway through turning."
            hy_ruth "\"Everything is a different regimen.\""
            "She takes her reading glasses off, lets them drop on their chain, and looks at you properly."
            hy_ruth "\"It's quicker, it goes a good deal further, and a good deal more of it stays. Breasts, not buds. Are you sure?\""
            hy_emily "\"I've never been so sure of anything.\""
            "You beam at her. It's the truest thing you've said all afternoon, and she can hear that it is."
            "Out in the waiting room, nobody says a word."
    "You sign where she shows you. Your handwriting isn't quite yours."
    "Neither of you notices."
    if hy.full:
        hy_ruth "\"The full regimen, then. Twice a day, with food. It'll go further than you think, and faster.\""
        hy_ruth "\"So I see you in two weeks, not four. Any side effects at all, you ring me. Not the internet. Me.\""
    else:
        hy_ruth "\"Low dose to start. The soft regimen. It'll silken you up and bud you a little, and that's all it's for.\""
        hy_ruth "\"I want to see you in a month. Any side effects at all, you ring me. Not the internet. Me.\""
    "She means every word."
    $ hy.rx = True
    $ hy.refillDay = vn_clock.day
    $ hy.appt = False
    $ hy_induct()
    if hy.full:
        "{color=#ffd700}The Bloom{/color}\n{color=#e40081}Estradiol, full regimen. Twice daily with food. Review in 14 days. {color=#b7b7b7}Dr. R. Adair{/color}{/color}"
    else:
        "{color=#ffd700}The Bloom{/color}\n{color=#e40081}Estradiol, low dose. Once daily with food. Review in 28 days. {color=#b7b7b7}Dr. R. Adair{/color}{/color}"
    $ hy_pill()
    show cg hy_firstpill onlayer cgl
    if hy.full:
        "She gives you the first one there and then, in a paper cup, with water from the cooler. A little white pill; tonight's is in the bag."
    else:
        "She gives you the first one there and then, in a paper cup, with water from the cooler. A little white pill."
    vn_sfx "Gulp."
    "Your hand swallows it. She smiles. Your face smiles back."
    "Something in your chest goes warm and proud that isn't yours. Nobody asks why."
    hide cg onlayer cgl
    show bg hy_highstreet onlayer bgl
    show hy_pc neutral at vn_pc_slot
    hide hy_ruth
    show hy_liam neutral at vn_cast_slot
    ## Visual-novel days: the route walks you home, into your room. Free play came in through the clinic's own door, and leaves by it (<<route_leave>>).
    if hy.full:
        "On the walk home, Liam carries the paper bag, and doesn't say a word until the corner."
        hy_liam "\"More, then.\""
        "He says it to the pavement, mostly."
        hy_ethan "\"More what?\""
        "He only smiles, and swaps the bag to his other hand.\n{size=-5}{color=#ff8fa3}▸ Walk home with him{/color}{/size}"
    else:
        "On the walk home, Liam carries the paper bag.\n{size=-5}{color=#ff8fa3}▸ Walk home with him{/color}{/size}"
    $ vn_pass(30)
    jump hy_hub
