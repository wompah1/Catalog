## THE RED PATH: "I Voted Red in the Comments, and Now Guys Can't Keep Up" (PACKAGE-red.md), rungs
## 2-6 and their scenes. Brat is a voice and it never shuts up; you're always the one getting
## fucked. The body moves first at rungs 3-4 (Nico and Rafe take the protests for the brat bit and
## answer the body; the chorus is the break); rung 5 the flip; rung 6 consensual. The toy is rung 2
## only; the DP rung 6 only, exactly Nico and Rafe; the only audiences Jesse (4) and the club crowd
## (5), who watch and never touch. Nobody sucks or strokes your cock.

## ---- rung 2: HOURS BEHIND (Personal Best) -------------------------------------------------------

label vt_red_two:
    call vt_gap("A week.", 9, 7)
    $ vt_grow(2)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bathroom", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r2_tips")
    "{color=#ff5fb8}Morning, the mirror. The tips of your dark hair have come in red. A loud, clean, fire-engine red, like you dipped your head in a tin of paint.{/color}"
    vt_you "\"Sick.\""
    "{color=#ff5fb8}Your skin's soft. Your nipples are puffy and tender, two swollen little peaks that sting when your work shirt goes on over them. And your jeans are snug across an ass that's started, very definitely, to round.{/color}"
    $ vt.fit = "work"
    $ vn_set_time(7, 40)
    $ vn_enter(bg="vt_kitchen", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_r2_card")
    "Breakfast. Cereal. Your phone propped on the milk. A new upload went up at three."
    show screen vt_phone("r2")
    "Just Kiki."
    hide screen vt_phone
    show cg vt_r2_gym onlayer cgl
    "Kiki in an empty gym after hours. Sweaty, a cropped top, tiny shorts, her ass bigger than last week. She suction-cups a fat toy to a weight bench, slaps it, peels her shorts aside, and sinks onto it facing the camera, grinning with the fang, bouncing, trash-talking it the whole way:"
    vt_kiki "\"♪ Is that all you've got ♪\""
    "The comments load."
    show screen vt_phone("r2")
    "You're hard over your cereal."
    hide screen vt_phone
    call vt_again
    $ vn_until(10)
    $ vn_enter(bg="vt_kiosk", pc="smirk", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg=None)
    "You show Jesse the hair over the counter."
    vt_jesse "\"You dyed it?\""
    vt_you "\"It just did that.\""
    vt_jesse "\"It suits you. It really, {i}really{/i} suits you.\""
    "All day you're mouthy without noticing. A lad brings in a screen he's put his knee through and you tell him it looks like he fought it and lost. You grin with too many teeth. You sit on the kiosk stool with your knees wide apart. Your voice is bright, and husky, and loud."
    $ vn_until(13)
    $ vn_enter(bg="vt_adult_shop", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r2_shop")
    "Lunch break. The adult shop on the centre's lower level, the one with the frosted window. You've never been in. You walk straight to the back, pick up a suction-cup toy, a fat one, and slap it down at the till, grinning."
    vt_you "\"For fun.\""
    $ vn_until(22)
    jump vt_red_two_floor

## Rung 2's act: the toy on the bathroom floor, alone, hours behind. As packaged.
label vt_red_two_floor:
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bathroom", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r2_tile")
    "That night. The bathroom floor. You suction-cup the toy to the tile, slap it so it wobbles, slick it up, and squat over it."
    vt_you "\"Right. Let's see what you've got.\""
    show cg vt_r2_sink onlayer cgl
    "You sink down onto it. Your first time, by yourself. It opens you up, fat and slow, and you don't go quiet about it. You're loud. You're telling it off the whole way down."
    vt_you "\"Come on. Come {i}on{/i}. Is this it? You're supposed to be the big one—\""
    vn_sfx "Shlk. Shlk. Shlk."
    "Nobody touches your cock, you included. Your hands are on your knees and you're bouncing, and it's bouncing, slapping your belly, ignored."
    call vt_voice(2)
    show cg vt_r2_pop onlayer cgl
    vn_sfx "THWOP."
    "The suction cup pops off the tile mid-ride and you go down on your arse on the floor with it still in you."
    vt_you "\"Oi! {i}Oi!{/i} Don't you dare. Don't you {i}dare{/i} quit on me. You owe me {i}money{/i}—\""
    "You slap it back down on the tile. It sticks. You get back on."
    show cg vt_r2_peak onlayer cgl
    "Faster. Harder. Grinning at it, snarling at it, and at the very top of it you snarl:"
    vt_you "\"Is that all you've got?\""
    show cg vt_r2_cum onlayer cgl
    "You come untouched, all over the bathmat, and your voice glitches at the top of it like a synth on a bad note." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_bathroom", pc="moaning", pc_tag="vt_pc", cast=[], cg="vt_r2_end")
    "You don't get off it. You bounce harder, the toy stuck back to the tile, the next one already coming, and you're telling it to keep up, keep {i}up{/i}, you lazy thing.\n{size=-5}{color=#ff8fa3}▸ Nine days{/color}{/size}"
    jump vt_red_three

## ---- rung 3: WHILE IT PLAYS (Bad Habit) ----------------------------------------------------------

label vt_red_three:
    call vt_gap("Nine days. Friday, three in the morning.", 18, 3)
    $ vt.fit = "home"
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_r3_card")
    "You set an alarm for it now."
    show screen vt_phone("r3")
    hide screen vt_phone
    show cg vt_r3_bar onlayer cgl
    "Kiki at a club bar. A bartender, cropped above the mouth, sets a drink down, and she grabs him by the belt across the bar and drags him off, into the bathroom, laughing. She drops to her knees. She smirks up at him."
    vt_kiki "\"♪ Shut up and give it to me ♪\""
    "It ends on her deepthroating him. The comments load."
    show screen vt_phone("r3")
    hide screen vt_phone
    call vt_again
    $ vt_grow(3)
    $ vn_set_time(9, 0)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bedroom", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r3_handfuls")
    "{color=#ff5fb8}Friday morning. Your ass is round. Properly round, in your jeans. Your thighs are thicker. There are small soft handfuls on your chest, and you squeeze them in bed and laugh out loud.{/color}"
    "{color=#ff5fb8}Your hair's at your shoulders now, red from halfway down to the ends. And one of your canines has sharpened. A small fang, poking out over your lip when you grin. You grin at it in the mirror for a long time.{/color}"
    "{color=#ff5fb8}Your lips are fuller. Your cock, when you check, is smaller. You shrug. Still works. And your mouth. Brushing your teeth feels unbelievable, the bristles on your tongue, the roof of your mouth. You stand at the sink with your knees going.{/color}"
    $ vt.fit = "work"
    show cg vt_r3_earbud onlayer cgl
    "The song's on loop in one earbud all day. At the kiosk. On the bus. It plays and plays."
    $ vn_until(21)
    jump vt_red_three_bar

label vt_red_three_bar:
    $ vn_enter(bg="vt_lowend_bar", pc="smirk", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg="vt_r3_lowend")
    "That night Jesse takes you to The Low End: a bar with a little stage at one end, fairy lights, sticky tables, too loud."
    "You flirt with her at the bar. Your hand on her thigh, really on it. You're really into her. You always have been."
    $ vn_enter(bg="vt_lowend_bar", pc="smirk", pc_tag="vt_pc", cast=[("vt_nico", "grin")], cg="vt_r3_nico")
    "The bartender sets your drinks down. Late twenties, an easy grin, quick hands, a bar towel over his shoulder. His badge says NICO."
    show cg vt_r3_belt onlayer cgl
    "And your hand shoots out across the bar and grabs him by the belt before you've decided anything at all."
    vt_you "\"Wait— no— that's not— I didn't mean—\""
    "Your hand doesn't let go. It pulls. Nico laughs, surprised, and lets himself be pulled, round the end of the bar."
    vt_nico "\"Alright, alright, I'm coming—\""
    vt_you "\"No, you're— I'm not— Jesse, I'm not doing this—\""
    "You're dragging him to the bathroom by his belt. You're telling him, the whole way, that you're not."
    hide vt_nico
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"Go on, [vt_pc_name]!\""
    jump vt_red_three_scene

label vt_red_three_scene:
    $ vn_enter(bg="vt_lowend_loo", pc="protesting", pc_tag="vt_pc", cast=[("vt_nico", "grin")], cg="vt_r3_kneel")
    "The bathroom. You drop to your knees on the tiles."
    vt_nico "\"You sure?\""
    vt_you "\"{i}No!{/i} I mean— don't— I don't do this, I'm not into— I've never—\""
    "Your hands are opening his jeans while you say it."
    vt_nico "\"Could've fooled me.\""
    "He's grinning. He thinks it's a bit. He thinks you, on your knees, telling him no while you get his cock out, are the funniest flirt he's ever had. His cock comes out in your hand, and your mouth goes on it."
    show cg vt_r3_open onlayer cgl
    vt_you "\"Mmf— this isn't— {i}mmf{/i}—\""
    vn_sfx "Glk. Glk."
    "And your mouth. Your turned-up, unbelievable mouth. He's heavy on your tongue and it's like your whole head lights up, and you nearly come from it. From sucking. Alone."
    show cg vt_r3_mid onlayer cgl
    "You can't stop the trash talk either. It comes out round him, in between the protests, the protests and the trash talk all knotted together."
    vt_you "\"Stop— stop being so {i}polite{/i} about it— no, I mean stop— mmf—\""
    "Your fang grazes him. Nico hisses, and laughs, and loves it."
    vt_nico "\"Christ, the {i}teeth{/i} on you.\""
    call vt_voice(3)
    vn_sfx "Bang bang bang."
    hide vt_nico
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"[vt_pc_name]! Are you in there with the {i}bartender{/i}?\""
    vt_you "\"Busy!\""
    "Your mouth's full. It comes out as {i}bmmf{/i}. Jesse cackles through the door."
    "Nico doesn't touch your cock. Nobody does. It's small and hard and straining in your jeans and you couldn't care less about it."
    hide vt_jesse
    show vt_nico grin at vn_cast_slot
    vt_nico "\"I'm close. Where d'you want—\""
    show cg vt_r3_peak onlayer cgl
    "You pull off. You grin up at him, fang and all, spit on your chin. And what comes out isn't a protest."
    vt_you "\"Shut up and give it to me.\""
    show cg vt_r3_cum onlayer cgl
    "Back on. He comes down your throat." with vnfx("flash")
    vn_sfx "Glk. Glk. Glk."
    "You hold him by the belt so he can't back off, and swallow, and come untouched in your jeans while you do, your voice glitching up round his cock:"
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_lowend_loo", pc="smirk", pc_tag="vt_pc", cast=[("vt_nico", "dazed")], cg="vt_r3_end")
    "You pull off, open your mouth, and show him the cum on your tongue. Then you swallow it, and grin, and tug his belt."
    vt_you "\"Next one. Come on. Next.\"\n{size=-5}{color=#ff8fa3}▸ Saturday week{/color}{/size}"
    jump vt_red_four

## ---- rung 4: IN SYNC (Two Can Play) --------------------------------------------------------------

label vt_red_four:
    call vt_gap("Saturday week. Three in the morning.", 26, 3)
    $ vt.fit = "home"
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_r4_card")
    show screen vt_phone("r4")
    hide screen vt_phone
    show cg vt_r4_couch onlayer cgl
    "Kiki at a house party, on all fours on a couch, two faceless guys, one at each end of her, and she's mouthing off round the cock in her mouth:"
    vt_kiki "\"♪ Don't you dare go easy ♪\""
    "It ends as she comes, her voice glitching. You're watching it in bed with your hand already moving."
    show screen vt_phone("r4")
    hide screen vt_phone
    call vt_again
    $ vt_grow(4)
    $ vn_set_time(9, 0)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bedroom", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r4_jeans")
    "{color=#ff5fb8}Your jeans won't button over your ass any more. They won't go near it. You stand there with them round your thighs, laughing.{/color}"
    "{color=#ff5fb8}Your chest has outgrown your shirts. Your waist has pulled in. Your thighs are thick. Your hair's long now, red right up to the roots, and it's curling into drills on its own, two big red spirals either side of your face. Your cock is tiny. Your voice is nearly not yours.{/color}"
    "You put on the spare leggings Jesse left at yours. They're obscene on you. You love it."
    $ vt.fit = "work"
    $ vn_until(13)
    $ vn_enter(bg="vt_lingerie", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r4_fitting")
    "On your break you march into the lingerie shop on the upper level and make the fitter measure you up with the curtain half open, because you can't be bothered to shut it."
    vt_clerk "\"You're a D. Easily a D. Are you— is this for a costume?\""
    vt_you "\"It's for {i}me{/i}.\""
    "You buy a bra that fits. You wear it out of the shop."
    $ vt.fit = "bra"
    "Nico texts you. You gave him your number in the loo, apparently. {i}party at mine and rafe's tonight. bring your mate{/i}"
    $ vn_until(21)
    jump vt_red_four_party

## Rung 4, part one: Jesse on the party couch. His own; he wants her.
label vt_red_four_party:
    $ vn_enter(bg="vt_party", pc="smirk", pc_tag="vt_pc", cast=[("vt_jesse", "flushed")], cg="vt_r4_jesse")
    "Nico and Rafe's flat. A house party: music, crisps, cans, a big telly on the wall, a lot of people out on the balcony smoking."
    "On the couch you make out with Jesse. You're so into her. You pull her leggings down right there and eat her out, loud, laughing into her, until she comes on your face with her hands in your drills."
    vt_jesse "\"Oh my— {i}God{/i}, [vt_pc_name]—\""
    "Your tiny cock's hard in your leggings. Nobody's paying it any attention."
    show cg vt_r4_tv onlayer cgl
    "Jesse, laughing, wiping her eyes, grabs the remote and puts the new upload on the big telly."
    vt_jesse "\"For the party!\""
    jump vt_red_four_couch

label vt_red_four_couch:
    $ vn_enter(bg="vt_party", pc="protesting", pc_tag="vt_pc", cast=[("vt_rafe", "laugh")], cg="vt_r4_allfours")
    "Everyone else is out on the balcony. Only Jesse stays, curled in the armchair with a can."
    "The video plays. And on the screen Kiki gets onto all fours on a couch—"
    "—and you're on all fours on the couch, before you've decided anything."
    vt_you "\"Wait— what am I— no, I'm not— Jesse, turn it {i}off{/i}—\""
    hide vt_rafe
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"Ha! Go on!\""
    "She thinks it's your bit. Nico's flatmate comes in from the balcony: big, loud, a backwards cap. Rafe. He looks at you on all fours, at the telly, at you, and bursts out laughing."
    hide vt_jesse
    show vt_rafe laugh at vn_cast_slot
    vt_rafe "\"Is this a dare? You doing the video?\""
    vt_you "\"I'm not doing anything! It's not— I don't—\""
    $ vn_enter(bg="vt_party", pc="protesting", pc_tag="vt_pc", cast=[("vt_nico", "grin")], cg="vt_r4_nico")
    "Nico's behind you. He's got his hand on your hip."
    vt_nico "\"You want this?\""
    vt_you "\"No. No, don't you— I don't—\""
    "And your hips push back into his hand, hard, and your hand reaches back on its own and pulls your leggings down."
    vt_nico "\"Your hips say different, mate.\""
    jump vt_red_four_scene

label vt_red_four_scene:
    $ vn_enter(bg="vt_party", pc="protesting", pc_tag="vt_pc", cast=[("vt_rafe", "laugh")], cg="vt_r4_open")
    "Rafe's in your mouth. Nico's in your ass. Your first time with a man, there, on the couch, with the telly on."
    vt_you "\"Mmf— get— get {i}out{/i}— mmf—\""
    vn_sfx "Pap. Pap. Pap."
    "It doesn't hurt. It's huge and hot and it fills you to the teeth, and on the screen the faceless guy behind Kiki moves, and Nico moves, on the beat, the same beat."
    show cg vt_r4_mid onlayer cgl
    "Every beat. When the guy on the screen thrusts, Nico thrusts. When Kiki arches, you arch. Your tiny cock swings under you, useless, slapping, and nobody touches it."
    "You mouth off round Rafe's cock between strokes. You can't help it. It starts as {i}stop{/i} and comes out as something else."
    vt_you "\"You call that— mmf— is that the best you two— {i}mmf{/i}—\""
    vt_rafe "\"Ha! He's {i}trash-talking{/i} us!\""
    call vt_voice(4)
    show cg vt_r4_duet onlayer cgl
    "Autoplay rolls on. Somebody's phone on the coffee table starts a Mio video, the teal one, all soft blushing."
    vt_you "\"Skip it! Red's better!\""
    "Rafe laughs so hard he nearly falls off the couch. Jesse skips it."
    "Back on the telly: Kiki, getting close. Nico's getting close. You're getting close."
    show cg vt_r4_peak onlayer cgl
    "You pull off Rafe. You look back over your shoulder, into Nico's face, and say it to him. Not to the screen. To him."
    vt_you "\"Don't you dare go easy.\""
    show cg vt_r4_cum onlayer cgl
    "You come when Kiki comes. Exactly when. Untouched, screaming, your voice glitching on a bad note." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_party", pc="smirk", pc_tag="vt_pc", cast=[("vt_nico", "dazed")], cg="vt_r4_end")
    "The video loops back to its start. Both of them are still in you. You grin round at them, fang out, drills everywhere."
    vt_you "\"Again. On the beat. Come on, idiots. {i}Again.{/i}\"\n{size=-5}{color=#ff8fa3}▸ The week nothing uploaded{/color}{/size}"
    jump vt_red_five

## ---- rung 5: AHEAD OF HER (The Week Nothing Uploaded) -- THE FLIP ------------------------------

label vt_red_five:
    call vt_gap("The week nothing uploaded.", 35, 10)
    $ vt.fit = "work"
    $ vn_enter(bg="vt_kiosk", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r5_refresh")
    "There's no new upload. Three in the morning comes and goes, and the channel sits there. You refresh it at the kiosk all week, between screens. Nothing."
    show screen vt_phone("r5")
    "Under the old video, people are asking."
    hide screen vt_phone
    $ vn_clock.day = 38
    $ vn_set_time(20, 0)
    $ vt.fit = "cos"
    $ vn_enter(bg="vt_lowend_bar", pc="smirk", pc_tag="vt_pc", cast=[("vt_jesse", "cos")], cg="vt_r5_cosplay")
    "Thursday. The Low End's virtual-singer night. Jesse's cosplaying Mio, a teal wig and a heart-eared headset. And she's brought a spare Kiki outfit for you."
    $ vt_grow(5)
    "{color=#ff5fb8}It fits you better than it ever fitted her. The red tube top's barely holding a big chest, really big now. The leather mini doesn't cover your huge ass at all. Fishnets on thick thighs. Platform boots. The choker with the mic-jack charm.{/color}"
    "{color=#ff5fb8}No wig. Your own red hair is already in drills. Your eyes have gone red. Properly red. And across your lower back, above the skirt, there's a red mark: a waveform, faint, like a watermark.{/color}"
    vt_jesse "\"Did you {i}draw that on{/i}? The waveform? You're so committed.\""
    show cg vt_r5_kiki onlayer cgl
    "All night people call you {i}Kiki{/i}. You grin at them with the fang and love it. Your face is softer. When you yell, the voice is hers."
    jump vt_red_five_stage

label vt_red_five_stage:
    $ vn_enter(bg="vt_lowend_stage", pc="smirk", pc_tag="vt_pc", cast=[("vt_nico", "grin")], cg="vt_r5_dj")
    "The DJ's playing the channel's songs. The old videos are on the screen behind the little stage."
    "You climb onto the stage. Nobody makes you. You want to, so you do."
    show cg vt_r5_finger onlayer cgl
    "You point at Nico, behind the bar. You crook one finger."
    "He vaults the bar. The crowd whoops."
    vt_nico "\"Here?\""
    vt_you "\"Yes.\""
    "You say it before he's finished asking."
    jump vt_red_five_scene

label vt_red_five_scene:
    $ vn_enter(bg="vt_lowend_stage", pc="moaning", pc_tag="vt_pc", cast=[("vt_nico", "dazed")], cg="vt_r5_open")
    "He bends you over a monitor speaker at the front of the stage and fucks you in front of everyone. Your ass. Your skirt up round your waist."
    vt_crowd "\"{i}Woooo!{/i}\""
    "They watch. They cheer. Nobody in the crowd touches you. They don't need to. You've got all of them anyway."
    vn_sfx "Pap. Pap. Pap."
    show cg vt_r5_change onlayer cgl
    "{color=#ff5fb8}And there, on the stage, it goes. Your tiny cock shrinks the last of the way, drawing up and in, a nub, then nothing, and where it was the skin parts, soft and wet, folding open into lips, a slick little slit, a pussy, yours, over the monitor speaker in front of everyone.{/color}"
    "{color=#ff5fb8}It feels like a laugh. Like a drum fill landing.{/color}"
    vt_nico "\"[vt_pc_name]—\""
    "His hand's on it. He's felt it."
    vt_you "\"Keep going, idiot.\""
    vt_nico "\"Can I—?\""
    vt_you "\"{i}Yes.{/i}\""
    show cg vt_r5_vaginal onlayer cgl
    "He pulls out of your ass and pushes into your pussy, and it's your first time again, a new one, so wet he slides home in one go, and you yell so loud the speaker under you feeds back."
    call vt_voice(5)
    vn_sfx "BWOOOM."
    vt_dj "\"Give it up for {i}Kiki{/i}!\""
    "The DJ cranks the bass without missing a beat. The whole floor jumps."
    show cg vt_r5_peak onlayer cgl
    "You turn your face to Nico, over your shoulder, and nobody's ever sung what you yell next. It's yours."
    vt_you "\"Make me louder!\""
    show cg vt_r5_cum onlayer cgl
    "You come screaming, your voice glitching through the monitor speaker, so the whole room hears it." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_lowend_stage", pc="smirk", pc_tag="vt_pc", cast=[("vt_nico", "dazed")], cg="vt_r5_end")
    "Nico doesn't stop. He fucks your new pussy over the monitor speaker with the crowd chanting {i}KI-KI, KI-KI{/i}, and you're yelling over your shoulder that he can go a lot harder than that, idiot.\n{size=-5}{color=#ff8fa3}▸ Three in the morning{/color}{/size}"
    jump vt_red_six

## ---- rung 6: THE UPLOAD IS HIM (Encore, Then Again) ----------------------------------------------

label vt_red_six:
    call vt_gap("Three in the morning.", 39, 3)
    $ vt.fit = "home"
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_r6_card")
    "The late upload finally drops."
    show screen vt_phone("r6a")
    hide screen vt_phone
    show cg vt_r6_encore onlayer cgl
    "Kiki on a club stage. She drags her bartender up out of the crowd and he bends her over a monitor speaker while the crowd chants, and she yells:"
    vt_kiki "\"♪ Make me louder ♪\""
    "You watch it in bed, thrilled, horny."
    vt_you "\"Best one yet.\""
    show screen vt_phone("r6a")
    hide screen vt_phone
    call vt_again
    $ vt_grow(6)
    $ vn_set_time(10, 0)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bedroom", pc="smirk", pc_tag="vt_pc", cast=[], cg="vt_r6_morning")
    "{color=#ff5fb8}Morning. Your ass has swollen huge overnight. The biggest jump yet: enormous, round, heavy, so big Jesse's leggings go see-through stretched over it, and your waist above it is tiny.{/color}"
    "{color=#ff5fb8}Your chest is bigger again, spilling out of the bra. Your face is nearly hers. The fang's sharp. Your eyes are red. Your drills are nearly her full length. The waveform on your back is darker. Your voice is entirely hers.{/color}"
    "Nico texts. {i}after party tonight at mine. andre's coming{/i}"
    "You text Jesse. {i}come. bring snacks{/i}"
    "She does."
    $ vn_until(22)
    jump vt_red_six_scene

## Rung 6: the after-party. Consensual.
label vt_red_six_scene:
    $ vn_enter(bg="vt_afterparty", pc="smirk", pc_tag="vt_pc", cast=[("vt_andre", "quiet")], cg="vt_r6_titjob")
    "Nico and Rafe's flat, late, the lights low. Nico's friend Andre: quiet, hasn't said ten words all night, and the biggest hands you've ever seen."
    "Those hands are on your tits now, pressing them together round his cock, and you're on your knees on the rug trash-talking him."
    vt_you "\"That all? Those hands and {i}that's{/i} all you're doing with them? Squeeze, idiot—\""
    vn_sfx "Shlp. Shlp. Shlp."
    "He squeezes. He doesn't say anything. He doesn't need to."
    call vt_voice(6)
    show cg vt_r6_tits_cum onlayer cgl
    "Andre comes across your tits and your chin." with vnfx("flash")
    "Jesse leans in from the couch and licks it off you, your tits, your chin, slow, and kisses you, and pushes it into your mouth with her tongue."
    $ vn_enter(bg="vt_afterparty", pc="moaning", pc_tag="vt_pc", cast=[("vt_nico", "dazed")], cg="vt_r6_dp")
    "Then the couch. You climb onto Nico and sink down on him, his cock in your pussy, and Rafe gets behind you, and pushes into your ass, and you're full, both of them, at once, the first time ever."
    vt_you "\"{i}Ohhh{/i}— yes— both— {i}both{/i}— fuck—\""
    "Jesse sits up on the back of the couch, legs either side of your head, and you get your mouth on her and eat her out through it. Still into her. Loud about it, between licks."
    vt_you "\"Jesse— you taste so— {i}mmf{/i}— I'm still— I still want {i}you{/i}—\""
    hide vt_nico
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"I know, babe. I know.\""
    vn_sfx "Pap. Pap. Pap."
    show cg vt_r6_face onlayer cgl
    "{color=#ff5fb8}And it happens on the couch, with both of them in you. Your jaw softens. Your nose. Your eyes. Your lips. Your face finishes, and it's hers. Your drills spring out to her full length, bouncing. The waveform on your lower back goes dark red. And your yell comes out, and it's wholly hers.{/color}"
    hide vt_nico
    show vt_andre quiet at vn_cast_slot
    vt_andre "\"Is she always like this?\""
    hide vt_andre
    hide vt_jesse
    show vt_nico grin at vn_cast_slot
    vt_nico "\"Yes.\""
    hide vt_nico
    show vt_rafe laugh at vn_cast_slot
    vt_rafe "\"Yes.\""
    vn_sfx "Bzzt."
    show cg vt_r6_phone onlayer cgl
    "Jesse's phone, on the cushion, lights up. A notification."
    show screen vt_phone("r6b")
    "Jesse's a fan. She plays it."
    hide screen vt_phone
    "The audio is a loud girl yelling, bright, raspy, glitching, in Kiki's voice. It's the yelling in this room. Right now. Nobody notices."
    show cg vt_r6_peak onlayer cgl
    "Nico and Rafe are close. She's closer. The phone on the cushion sings, and so does she, the same line, the same breath."
    $ vn_feat("Now Guys Can't Keep Up")
    vt_red_end "\"♪ Again, again, again! ♪\"" with vnfx("flash")
    call vt_route_return("Now Guys Can't Keep Up")
