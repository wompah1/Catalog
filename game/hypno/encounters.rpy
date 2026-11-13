## Open and Listen's five sex scenes, written out for the Ren'Py port (2026-11-11).
##
## In the DoL catalog these were director scenes: <<sl_sex>> handed the turn to DoL's combat
## engine, which wrote the prose (and printed its mechanics, and called Emily "good boy"). Ren'Py
## has no such engine, so each scene is its beats, frame by frame: open -> start -> mid -> peak ->
## Emily's climax (its own frame: owner, 2026-11-10) -> the passage after, whose frame is his.
## The DoL screen never got past the peak frames on the two rides (they start at full arousal);
## here they use all five.
##
## (Reviewed 2026-11-11: within one playthrough no pool line repeats across Stay, Master and Door;
## the two endings are alternatives and may share lines.)
## The spoken lines are the route's own pools wherever one fits (hypno.js: slCombatLines.Liam,
## slPcLines.hypno, Emily's voice, `{lead}` "sir" at the hinge and "Master" from rung 4). THE PAGE
## RULE (revamp, owner 2026-10-20) holds: every scene is in trance, as Emily, eager and loud; the
## violation is the premise, said in the prose around these scenes (Liam never asks, Ethan never
## agreed, the six words do it), never argued in her mouth. End Listen's ride is the one awake and
## asked for, with no trigger said. WITHHELD to rung 6: his cock in her ass (Stay, Master, Door
## never have it). The cock is kept, caged, and never touched.

## Rung 3, the hinge: the mandatory oral, kneeling in the powder-blue panties, the cage just on.
## Liam leads; "sir". (rungs.twee :: Hypno Stay Sex)
label hy_stay_sex:
    $ hy.fit = "panties"
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cg="hy_stay_open")
    $ hy_enc = VNState(ran=True, partner_came=True, pc_orgasms=0)
    "He threads his fingers into your tails and guides the head of him to your lips."
    hy_liam "\"Look up at me. Good girl. Keep your eyes on me while you do that.\""
    hy_emily "\"Mmh— {i}mmnh{/i}—!\""
    "You pull off just long enough to beam up at him."
    hy_emily "\"Sir, you taste so {i}good{/i}—\""
    "And you're straight back down."
    show cg hy_stay_start onlayer cgl
    vn_sfx "Glk. Glk. Glk."
    "You fold your hands behind your back like a good girl and take him deeper, slow, to where your throat opens for him."
    hy_liam "\"That's it. All the way down. You were made for this. You just didn't know it till the flat.\""
    show hy_pc trance
    hy_emily "\"Glk— {i}glk{/i}— mmh—!\""
    "You take him to the root on your own and hum, so proud of yourself it comes out a squeal."
    show cg hy_stay_mid onlayer cgl
    "His hand settles on the top of your head and holds you there."
    hy_liam "\"Listen to you. The whole landing can hear you choking on it, and you don't care.\""
    show hy_pc eager
    hy_emily "\"Use my mouth, sir— please, please, it's {i}yours{/i}— {i}mmf{/i}—!\"" with vnfx("shake")
    show cg hy_stay_peak onlayer cgl
    if hy.full:
        "Your tails swing with every stroke. Drool runs down your chin onto your breasts."
    else:
        "Your tails swing with every stroke. Drool runs down your chin onto your buds."
    hy_liam "\"Say it with your mouth full. Go on. Say what you are.\""
    hy_emily "\"Your girl— {i}mmh{/i}— your good girl—\""
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    "Low, and your whole body answers it before you do."
    show cg hy_stay_cum onlayer cgl
    "The cage throbs in the satin. Nobody's touching it. Nobody's going to."
    hy_emily "\"Cum in my mouth— I want it— {i}please{/i}, sir, I've been {i}so{/i} good—\""
    "Muffled, loud, and you mean every word."
    "You come first: caged, untouched, a thin hot dribble into the satin while you moan round him." with vnfx("flash")
    $ hy_enc.pc_orgasms = 1
    jump hy_stay_after

## Rung 4: the titjob on the buds, the plug in. "Master", from here. Optional (Keep them pushed
## together for him). (rungs.twee :: Hypno Master Sex)
label hy_master_sex:
    $ hy.fit = "nude"
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cg="hy_master_open")
    $ hy_enc = VNState(ran=True, partner_came=True, pc_orgasms=0)
    if hy.full:
        "You hold your breasts pushed together round him, the plug shifting in you every time you move."
    else:
        "You hold your buds pushed together round him, the plug shifting in you every time you move."
    hy_liam "\"Your tits. Push them together for me, pet.\""
    hy_emily "\"Please, Master— please, please, I want it, I want it so {i}bad{/i}—\""
    "You're bouncing on your knees with it."
    show cg hy_master_start onlayer cgl
    vn_sfx "Shlk. Shlk."
    if hy.full:
        "They swallow him, soft on both sides, and he fucks them slow, the head bumping your chin every stroke."
    else:
        "Barely anything either side of him, and he fucks it anyway, slow, the head bumping your chin every stroke."
    hy_emily "\"Is it good? Am I doing it good? Tell me I'm good— {i}please{/i}—\""
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    show cg hy_master_mid onlayer cgl
    "You bend to him and catch the head on your tongue every time it reaches you."
    hy_liam "\"Look at you leaking in that cage. You can't even touch it. Good.\""
    show hy_pc trance
    hy_emily "\"Look, it's leaking through the cage— and it's not even {i}hard{/i}— I love it, I {i}love{/i} it—!\""
    show cg hy_master_peak onlayer cgl
    if hy.full:
        hy_liam "\"Squeeze them. Look at that. Look what you asked for.\""
    else:
        hy_liam "\"Squeeze them. Look at that. Just enough to tell everyone you're my girl. Never more.\""
    show hy_pc eager
    hy_emily "\"Ahh— it's so {i}hot{/i}— don't stop, don't {i}stop{/i}— I'm your girl, I'm your {i}girl{/i}—!\"" with vnfx("shake")
    hy_liam "\"Whose are you? Say it.\""
    hy_emily "\"I'm yours— I'm {i}yours{/i}— I've always been yours—!\""
    show cg hy_master_cum onlayer cgl
    if hy.full:
        "The plug, your breasts, his cock between them: it all goes off at once."
    else:
        "The plug, the buds, his cock between them: it all goes off at once."
    if hy.full:
        "You come caged and untouched again, the little thing dribbling through the plastic onto the sheet, squeezing your breasts round him through all of it." with vnfx("flash")
    else:
        "You come caged and untouched again, the little thing dribbling through the plastic onto the sheet, squeezing your buds round him through all of it." with vnfx("flash")
    hy_emily "\"Mmh— cum on me, Master— all over— I want to wear it—!\""
    $ hy_enc.pc_orgasms = 1
    jump hy_master_after

## Rung 5, home from the night out: on your knees against the flat door, his cock already in your
## mouth, Cass's flat right underneath. "Master". Optional (Stay on your knees for him).
## (rungs.twee :: Hypno Door Sex)
label hy_door_sex:
    $ hy.fit = "mini"
    $ vn_enter(bg="hy_hallway", pc="eager", pc_tag="hy_pc", cg="hy_door_open")
    $ hy_enc = VNState(ran=True, partner_came=True, pc_orgasms=0)
    "His fist round the base of one tail, steering. The door's cold against your shoulder blades."
    hy_liam "\"Louder, Emily. Let the landing hear whose girl you are.\""
    "You moan round him like it's the best thing that's ever happened to you, tails bouncing, drool on your chin."
    hy_emily "\"Mmh— {i}mmh{/i}—!\"" with vnfx("shake")
    show cg hy_door_start onlayer cgl
    vn_sfx "Glk. Glk. Glk."
    "His fists tighten in your tails."
    hy_liam "\"Stay right there. Swallow.\""
    hy_emily "\"Mmh— good girl— I'm your good girl— say it, say it again—!\""
    show cg hy_door_mid onlayer cgl
    "Slow and deep, nose in his stomach. The door rattles in its frame behind your head every time he pulls you down."
    hy_liam "\"That little thing's drooling again. Useless. I love it.\""
    show hy_pc trance
    "The cage swings under your skirt with every stroke, dripping. You pull off just to giggle at it."
    hy_emily "\"Useless! It's so {i}useless{/i}— {i}ahh{/i}—!\""
    show cg hy_door_peak onlayer cgl
    "He flicks the cage."
    hy_liam "\"Not even hard. You don't need it, do you, Emily?\""
    show hy_pc eager
    hy_emily "\"No, Master— it's not for anything— it's just for you to laugh at—!\""
    "Then straight back down, louder, because Cass's flat is right underneath and you hope she hears."
    show cg hy_door_cum onlayer cgl
    hy_emily "\"I'm gonna— Master, I'm gonna— can I? Can I? {i}Please{/i}—!\""
    "You come on your knees against the door, caged and untouched, dribbling onto the hall floor while you moan round him." with vnfx("flash")
    $ hy_enc.pc_orgasms = 1
    jump hy_door_after

## End Listen's climax: AWAKE and asked for, no trigger said. You on top; his cock in your ass, at
## last. Emily's voice because she chose to be her; awake faces, no glow. "Master".
## (endings.twee :: Hypno Listen Sex)
label hy_listen_sex:
    $ hy.fit = "cami"
    $ vn_enter(bg="hy_bedroom", pc="happy", pc_tag="hy_pc", cg="hy_listen_open")
    $ hy_enc = VNState(ran=True, partner_came=True, pc_orgasms=0)
    "You sink. Slow. The head of him opens you, and then the rest, inch by inch, while you watch his face."
    hy_emily "\"Ahh— {i}ahh{/i}— it's inside— you're {i}inside{/i} me, Master— oh my {i}god{/i}—!\""
    hy_liam "\"Down. All the way. Look at me while you take it.\""
    show cg hy_listen_start onlayer cgl
    vn_sfx "Shlk... shlk..."
    "You lift and drop, careful at first, learning him. Awake. Every second of it yours."
    "His hands sink into your hips."
    hy_liam "\"Since the flat. I've wanted this since the flat.\""
    hy_emily "\"I know. I {i}know{/i}. I asked.\""
    show cg hy_listen_mid onlayer cgl
    "Faster. Your tails swing against his cheeks, the cage bouncing soft on his stomach."
    hy_emily "\"Ahh— {i}ahh{/i}— look at me, Master— I'm riding you— I'm {i}riding{/i} you—!\""
    hy_liam "\"That's my good girl. Ride it. Show me what you are.\""
    show cg hy_listen_peak onlayer cgl
    hy_emily "\"So deep— it's so {i}deep{/i}— I'm yours, I'm all yours— {i}haa{/i}—!\"" with vnfx("shake")
    "You bounce on him and squeal at the top of your lungs."
    hy_liam "\"Louder. I want the whole building to know whose you are.\""
    hy_emily "\"Keep it locked, Master— keep it {i}locked{/i}— I don't need it, I've got {i}you{/i}—!\""
    show cg hy_listen_cum onlayer cgl
    "The first one takes you by surprise: your hole clenches round him and the cage just spills, a thin hot spurt onto his stomach, untouched." with vnfx("flash")
    hy_emily "\"Thank you— thank you, Master— {i}haa{/i}— thank you—!\""
    "You don't stop moving. You've barely started."
    $ hy_enc.pc_orgasms = 1
    jump hy_listen_after

## End Never's climax, inside the session that doesn't end: in trance, she rides him. His cock in
## her ass, at last. "Master". (endings.twee :: Hypno Never Sex)
label hy_never_sex:
    $ hy.fit = "cami"
    $ vn_enter(bg="hy_bedroom", pc="eager", pc_tag="hy_pc", cg="hy_never_open")
    $ hy_enc = VNState(ran=True, partner_came=True, pc_orgasms=0)
    "You sink down on him, slow, looking back at his face the way you love to, already moaning."
    hy_emily "\"Ahh— {i}ahh{/i}— it's inside— you're {i}inside{/i} me, Master— oh my {i}god{/i}—!\""
    hy_liam "\"There it is. That's mine now. Squeeze.\""
    show cg hy_never_start onlayer cgl
    vn_sfx "Shlk. Shlk."
    show hy_pc trance
    hy_emily "\"Harder— {i}harder{/i}— I can take it, I can take it for you—!\""
    hy_liam "\"Good girl. Take it. You've been begging for this since the flat.\""
    show cg hy_never_mid onlayer cgl
    "Your ass claps down on him every drop, round and heavy, tails swinging."
    hy_emily "\"Am I good? Am I your good girl? Tell me— {i}ahh{/i}— tell me I'm good—!\""
    hy_liam "{=hy_hypno}“Good girl.”{/=hy_hypno}"
    show cg hy_never_peak onlayer cgl
    show hy_pc eager
    hy_emily "\"Fill me up— please, Master, fill me {i}up{/i}— I've wanted this {i}forever{/i}—!\"" with vnfx("shake")
    "His hands sink into your hips."
    hy_liam "\"Since the flat. I've wanted this since the flat.\""
    hy_emily "\"It doesn't do anything— it doesn't {i}do{/i} anything— and I don't care— {i}ahh{/i}—!\""
    show cg hy_never_cum onlayer cgl
    "The first one goes through you with him buried to the root: untouched, the cage spilling, your hole fluttering round him." with vnfx("flash")
    hy_emily "\"Louder? I can be louder— {i}ahh{/i}— {i}AHH{/i}—!\""
    "You don't care who hears. You want them to."
    $ hy_enc.pc_orgasms = 1
    jump hy_never_after
