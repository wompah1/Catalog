## The route's five sex scenes, written out for the Ren'Py pilot (2026-11-11).
##
## In the DoL catalog these were director scenes: <<sl_sex>> handed the turn to DoL's combat
## engine, which wrote the prose (and the VN screen hid its menus and clicked the box for you).
## Ren'Py has no such engine, so each scene is its beats, frame by frame, as the VN paced them:
## open -> mid -> peak -> the PC's climax (its own frame: owner, 2026-11-10, "anytime mc cums
## should have its own art") -> the passage after, whose frame is his climax.
##
## The spoken lines are the route's own pools wherever one fits (redlightning.js:
## redlightningLines for Miles, slPcLines.redlightning for Rory: protest / betray / flip while it's
## non-con, then the consensual moans, demands and pleas). The narration between is written from
## the scene's lead-in and its frames. Kept from each director row: the act, the position, the
## vocative (Thorne until rung 6), deny anal before rung 5, consent "noncon" with the flip at the
## break (Blue, Stretches, Shed), Shed mandatory. Before rung 6 Rory has a cock: no pussy, no
## vaginal (the frames were drawn to that rule).

## Rung 2, the showers: your hand on him, his fist over it. Non-con, misread as a grip contest,
## flips at the break. (rungs.twee :: Redlightning Blue Sex)
label rl_blue_sex:
    $ vn_enter(bg="rl_locker", pc="shocked", pc_tag="rory", cg="rl_blue_open")
    $ rl_enc = VNState(partner_came=True, pc_orgasms=0)
    vn_sfx "Shlk. Shlk. Shlk."
    "His fist pumps yours up and down him. Root to tip. Your knuckles squeak on wet skin."
    rl_rory "\"Rematch— fine, rematch, but you can't just— {i}hah{/i}— grab a man's—\"" with vnfx("shake")
    rl_miles "\"Stop squirming.\""
    rl_rory "\"Two-handed hold! That's illegal! Ref! {i}REF{/i}—!\""
    show cg rl_blue_mid onlayer cgl
    show rory flushed
    "He shoves your wet shorts down with his free hand and takes you in his fist. Same grip. Same pace. Like he's teaching you."
    "Then his mouth comes down on your new tit."
    vn_sfx "Zzzt."
    rl_rory "\"Why is this— why does WRESTLING feel like— {i}nnngh{/i}—\""
    rl_miles "\"You really don't get it, do you.\""
    rl_rory "\"I'm winning— I'm still winning— {i}ahh{/i}— why are my legs—\""
    show cg rl_blue_peak onlayer cgl
    "Chest to chest under the spray. Your fist on him, his fist on you, both of you going faster."
    rl_rory "\"...Oh. {i}OH{/i}. Is THAT what this— okay. OKAY. Don't you DARE stop.\"" with vnfx("shake")
    rl_miles "\"You drive me insane. You know that? Insane.\""
    rl_rory "\"Ohh— yeah— YEAH, like that, Thorne— I'm winning this one too—!\""
    rl_miles "\"Let me—\""
    show cg rl_blue_cum onlayer cgl
    "He hauls you back against his chest and lifts you half off the tiles, his fist flying on you."
    rl_rory "\"I'm gonna— {i}hah{/i}— I'm gonna WIN— don't stop— don't {i}stop{/i}—!\""
    "You come up the shower wall in hot ropes, hips bucking, howling it at the tiles." with vnfx("flash")
    $ rl_enc.pc_orgasms = 1
    jump rl_blue_after

## Rung 4, the empty locker room: your mouth on him. Non-con, misread as an endurance round, flips
## at the break; the lead-in already has your lips round him. (rungs.twee :: Redlightning Stretches Sex)
label rl_stretches_sex:
    $ vn_enter(bg="rl_locker", pc="shocked", pc_tag="rory", cg="rl_stretches_open")
    $ rl_enc = VNState(partner_came=True, pc_orgasms=0)
    vn_sfx "Glk. Glk. Glk."
    "He holds your head and rocks in slow. Your lips stretch round him. You glare up the whole length of him."
    rl_miles "\"Two years. Two years of watching you. Hold {i}still{/i}.\""
    rl_rory "\"Mmf— {i}MMF{/i}—!\"" with vnfx("shake")
    vn_th "(Cheap shot— he's going DEEPER— I wasn't READY—)"
    "You hang on anyway. Endurance round. You are not tapping out first."
    show cg rl_stretches_mid onlayer cgl
    "You shove at his thighs. He doesn't budge. So you hold on to them instead. For balance. Obviously for balance."
    vn_sfx "Shlp. Shlp. Shlp."
    "Every stroke drags over your tongue and your whole mouth goes {i}zzzt{/i}, straight down your spine."
    show rory flushed
    rl_rory "\"Okay— okay you're good at this— you're TOO good at this— {i}hah{/i}—\""
    rl_miles "\"Breathe. Breathe, you menace. That's it.\""
    show cg rl_stretches_peak onlayer cgl
    "Your bra's gone somewhere. Your tits sway every time he pulls you down. Spit everywhere."
    rl_rory "\"Mmh— {i}mmh{/i}—?!\"" with vnfx("shake")
    vn_th "(Oh. OH. Is THAT what this—)"
    "It lands, mouth full. You stop shoving his thighs and grab them instead, and go down on him like it's a race."
    rl_miles "\"You idiot. Even now you're grinning round it—\""
    rl_miles "\"Look up. Look at me. Fuck.\""
    show cg rl_stretches_cum onlayer cgl
    "Your little cock's throbbing in your shorts, untouched, every time he hits the back of your throat."
    rl_rory "\"Mmmh— MMMHH— {i}MMMMFF{/i}—!\""
    "You come on your knees on the mat with your mouth full of him, shaking all over, and you don't let go." with vnfx("flash")
    $ rl_enc.pc_orgasms = 1
    jump rl_stretches_after

## Rung 5, behind the equipment shed: THE MANDATORY SCENE (decision 7), the first anal, against the
## wall. Non-con, misread as the last challenge, and it FLIPS at the break: the turning point of
## the route, where it lands and Rory says "GO ON". The lead-in has the head of him at your hole,
## so it starts already going. (rungs.twee :: Redlightning Shed Sex)
label rl_shed_sex:
    $ vn_enter(bg="rl_track_dusk", pc="shocked", pc_tag="rory", cg="rl_shed_open")
    $ rl_enc = VNState(partner_came=True, pc_orgasms=0)
    vn_sfx "Shlk—"
    "He pushes in."
    rl_rory "\"Oi— that's a FOUL, Thorne— that's a {i}foul{/i}—!\"" with vnfx("shake")
    "He doesn't stop. Slow and thick and all the way, your back on the siding, your legs locked round him because he put them there."
    rl_miles "\"Stop squirming.\""
    rl_rory "\"I'm not tapping— I'm NOT tapping out— get {i}off{/i}—!\""
    "You buck. He doesn't budge an inch."
    show cg rl_shed_mid onlayer cgl
    vn_sfx "Creak. Creak. Creak."
    "The shed wall rattles on every thrust. Your tit's out in the cold air, your shorts round one ankle."
    show rory flushed
    "You're still shoving him. Every shove rides you harder onto him."
    rl_rory "\"Th-that doesn't count— {i}ohh{/i}—\""
    rl_miles "\"Second place, my arse. Who's on top now?\""
    "Your tiny cock bounces between you, leaking, forgotten. He finds the spot his fingers found and hits it. And hits it."
    rl_rory "\"Is this— a special technique— Coach never taught us {i}THIS{/i}—!\""
    rl_miles "\"It's not a wrestling move, you idiot.\""
    show cg rl_shed_peak onlayer cgl
    show rory grin
    rl_rory "\"...Oh. {i}OH{/i}. Is THAT what— okay. OKAY.\"" with vnfx("shake")
    "You lock your legs round him."
    rl_rory "\"Anything for my best mate. Go on.\""
    "Louder."
    rl_rory "\"GO ON.\"" with vnfx("shake")
    rl_miles "\"Mine. Say it. You're— {i}mine{/i}—\""
    show rory flushed
    rl_rory "\"Haa— go on— GO ON— you call that a pace? {i}Faster{/i}—!\""
    rl_miles "\"So tight— you're so— fuck, you're perfect—\""
    show cg rl_shed_cum onlayer cgl
    rl_rory "\"Don't— don't you DARE stop— I mean— that's not what I— {i}AHH{/i}—!\""
    "You come untouched, your tiny cock spurting between you, your arse clamping down on him so hard he swears." with vnfx("flash")
    $ rl_enc.pc_orgasms = 1
    jump rl_shed_after

## Rung 6, his room: him inside you, your first vaginal, after the shift. Consensual; she/her;
## "Miles" now. "Pull him in" is the pull. (rungs.twee :: Redlightning Girlfriend Sex)
label rl_girlfriend_sex:
    $ vn_enter(bg="rl_miles_room", pc="flushed", pc_tag="rory", cg="rl_girlfriend_open")
    $ rl_enc = VNState(partner_came=True, pc_orgasms=0)
    "He pushes in. Slow. All the way. Your first time, and your new pussy takes him like it's been waiting all week."
    rl_rory "\"Ohh— {i}ohh{/i}— Miles— MILES—\""
    rl_miles "\"Let me— let me feel all of it. All of you.\""
    show cg rl_girlfriend_mid onlayer cgl
    vn_sfx "Shlk. Shlk. Shlk."
    "He kisses you while he moves, deep and slow, like he's got all morning. He has."
    rl_rory "\"Harder, Miles. Come ON. I've seen you run faster than that.\""
    rl_miles "\"If you won't get it with words…\""
    "Slow, all the way in."
    rl_miles "\"…I'll keep showing you.\""
    show cg rl_girlfriend_peak onlayer cgl
    "Your hips find it before you do: up, down, squeeze. You've never done this in your life, and your body's known it for a week."
    rl_rory "\"Ahh— that's a personal best— that's a personal {i}BEST{/i}— again—!\""
    rl_miles "\"Every version of you. Every single one. Mine.\""
    rl_rory "\"Please— Miles— {i}please{/i}, more, I'll let you have the warm-up lap—!\""
    show cg rl_girlfriend_cum onlayer cgl
    rl_rory "\"{i}YES{/i}— YES— photo finish— {i}YESSS{/i}—!\"" with vnfx("shake")
    "You come round him with your heels locked in his back, the starting gun going off inside you again and again." with vnfx("flash")
    $ rl_enc.pc_orgasms = 1
    jump rl_girlfriend_after

## The Go epilogue's first Sunday, on the counter: the titjob. Consensual; "Miles".
## (main.twee :: Redlightning Go Counter Sex)
label rl_go_counter_sex:
    $ vn_enter(bg="rl_flat", pc="grin", pc_tag="rory", cg="rl_gocounter_open")
    $ rl_enc = VNState(partner_came=True, pc_orgasms=0)
    "You squeeze your tits together round him and grin up the whole length of him."
    rl_rory "\"Bit slow off the blocks this morning, Miles. Want a head start?\""
    rl_miles "\"Let me—\""
    show cg rl_gocounter_mid onlayer cgl
    vn_sfx "Squish. Squish. Squish."
    "He sits back on the counter and you bend to him, tits wrapped round his cock, the head popping up between them on every stroke."
    show rory flushed
    rl_rory "\"Look at you, all sweaty. Did I do that? I did that.\""
    "You crow it at him."
    rl_miles "\"You drive me insane. You know that? Insane.\""
    show cg rl_gocounter_peak onlayer cgl
    "Every stroke drags him over your nipples, and your whole chest goes {i}zzzt{/i}."
    rl_rory "\"Ohh— yeah— YEAH, like that, Miles— I'm winning this one too—!\""
    rl_miles "\"You idiot. Even now—\""
    rl_rory "\"Don't make me beg— okay, I'm begging— I'm BEGGING— {i}please{/i}—!\""
    show cg rl_gocounter_cum onlayer cgl
    rl_rory "\"Ohh— oh— my TITS— Miles, I'm gonna— {i}AHHH{/i}—!\"" with vnfx("shake")
    "You come with his cock between your tits and his arms locked round you, shaking, laughing, loud enough for the whole building." with vnfx("flash")
    $ rl_enc.pc_orgasms = 1
    jump rl_go_counter_after
