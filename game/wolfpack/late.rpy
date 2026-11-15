## wolfpack, days 4 to 7, the ending and the epilogue (rungs.twee from Day Four, ending.twee),
## rewritten for the VN (2026-11-12; PLAN.md). Days 1 to 3 are in script.rpy, the scenes in scenes.rpy.

## ---- DAY 4: rung 3's body; the range; rung 4, THE KNOT (mandatory) -------------------------------

label wlf_day_four:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    show screen wlf_furs("wake")
    "You wake warm on both sides."
    hide screen wlf_furs
    $ wlf_body(3)
    show cg wlf_chest_three onlayer cgl
    "{color=#ff5fb8}Something soft shifts on your chest when you turn over.{/color}"
    "{color=#ff5fb8}You throw the furs off and look down.{/color}"
    "{color=#ff5fb8}{i}Tits.{/i} Small ones, but too full to be flat, round soft swells topped with fat pink nipples. You scoop them up. They {i}give{/i}. They {i}fill your hands{/i}.{/color}"
    show wlf_pc flushed
    wlf_you "\"Ohhh— oh, {i}look{/i} at you— {i}nnh{/i}— fuck, that's good— {i}that's{/i} good—\""
    "{color=#ff5fb8}You squeeze, greedy, and your nipples go hard against your palms and a hot snap runs straight down your spine. You can't stop squeezing. You don't try. They're so sensitive the fur sliding off them made you {i}squeal{/i}, and every pinch of a nipple goes off like a little orgasm.{/color}"
    "{color=#ff5fb8}Behind you, your ass has rounded out into something you have to look over your shoulder at: plump, heavy, bouncing when you shift. Your thighs are thicker, soft and full, rubbing when you move. Your lips feel swollen and pouty against your fangs. Your hair falls past your shoulders.{/color}"
    wlf_you "\"Morning.\""
    "{color=#ff5fb8}You try it, and it comes out a step higher again. Sweet. You do it again just to hear it.{/color}"
    "{color=#ff5fb8}And your cock's almost nothing now. A soft little nub of a thing, dribbling when you squeeze your tits, and you don't even look down at it.{/color}"
    hide cg onlayer cgl
    show wlf_pc smug
    wlf_you "\"{color=#f3c969}[WLF_WORD['chest']]{/color}\""
    "Your mouth still tastes like Bramble. Your hands still know the weight of him. You could do either again in your sleep, better."
    "And the heat's back. Right on schedule: the morning after the ears, building toward noon. You called it to the hour. You lie there smug as anything and let it climb."
    "Because you've worked out the last thing."
    "The knot. Shown to you twice, and held back every time. Every man in this den can breed you. Not one of them will {i}knot{/i} you."
    "Easy to decode. It's a {i}rank{/i}. A privilege for someone near the top: first picked, first filled, first in line. Second-in-command."
    "So you're going to qualify for it in front of all of them.\n{size=-5}{color=#ff8fa3}▸ Run the range with the pack{/color}{/size}"
    $ vn_pass(30)
    jump wlf_range

## The range run: you call the line and the pack closes ranks behind you. No prey, no tracking,
## nothing smelled out: a run of their range, and you at the front of it.
label wlf_range:
    $ vn_enter(bg="wlf_transect", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_range_run")
    "The whole pack goes out at once, out of the den and down through the ferns at a lope, and you take point beside Grey."
    "For the first time, nobody cuts in front of you."
    "You flick your tail left at the fork and Bramble falls in behind you. You wave Notch through the bracken and the whole string of them follows you over the stream and up through the tight cover. At the next crossing Grey stops, looks at you, and lets {i}you{/i} call it."
    "You call it."
    show cg wlf_range_heads onlayer cgl
    "They run the boundary of their range all morning, the lake, the ridge, the long slope above the valley, and every time the pack pauses, the heads turn. Not to the black one."
    "To you."
    "The talk stops and they wait for the next word, and you give it. It stops again. You give it again. Elbows on your knees, tits out, heat thrumming in your belly, ordering a pack of wolf-men round the forest in clipped little sentences of your own."
    show wlf_pc smug
    wlf_you "\"Left. Lake.\""
    wlf_you "\"Up. Now.\""
    "They go."
    hide cg onlayer cgl
    "You walk back at the front. Every step says it: you've earned the next mark.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(18)
    jump wlf_knot_me

## Rung 4, THE MANDATORY SCENE. You present and ask for the knot: your own ambition. What you didn't
## ask for is being held flat, at his pace, and the shift under the knot. The choice is how you fight
## his hand; both go into the scene.
label wlf_knot_me:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_den_orange")
    "Dusk. The den goes orange in the last of the light."
    "The pack's spread out: Grey and Notch out on the ledge, Bramble and Scrap down at the spring. Old Man at the far end, up by the mouth, fussing with a pile of hides with his back turned to the whole cave."
    hide cg onlayer cgl
    show wlf_alpha flat at vn_cast_slot
    "The black one sits against the rock at the back wall. Arms folded. Waiting. Like he's been waiting since you walked in the first night."
    "You stand over him and bare your fangs, so he sees exactly what you came for."
    show cg wlf_present_ask onlayer cgl
    "Then you present. Bare from the waist down, tail up, heat running down the insides of your thighs, your tiny cock half-hard and your hole slick and twitching. Proud as a challenge."
    "In his own register. Short."
    wlf_you "\"Knot me.\""
    show wlf_alpha dark
    "His eyes go dark. He gets up, and up, until he's over you like a wall."
    wlf_you "\"On top. My pace. You lie back and you {i}give{/i} it to me, and then—\""
    show cg wlf_knot_flat onlayer cgl
    "His hand closes on the back of your neck."
    wlf_alpha "\"Presented.\""
    "And he puts you down flat on his furs, cheek to the hide, ass in the air, the way {i}he{/i} wants it. His knee nudges yours apart. His weight settles over your back, and you can't get up."
    show wlf_pc furious
    wlf_you "\"No— no, I {i}asked{/i}— that's not how I— {i}alpha{/i}—!\""
    menu:
        "His hand on your nape. His furs under your cheek."
        "Shove up against his hand":
            $ wlf.how4 = "shove"
        "Tell him exactly whose pace this is":
            $ wlf.how4 = "tell"
    jump wlf_knot_sex

## The authored knot: it batters, stretches, pops in, and under it the room makes itself. The cock and
## balls go, and THAT is the part you didn't ask for: loud, pinned through it, his hand never leaving
## your nape. A cunt clamps round the knot, load after load, and it takes. Then the middle of the lock.
label wlf_knot:
    $ vn_enter(bg="wlf_den", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_knot_thud")
    wlf_you "\"Harder. Deeper. {i}All{/i} of it.\""
    "He gives you all of it."
    vn_sfx "{i}Thud.{/i} {i}Thud.{/i}"
    "The knot's there, swelling at the base of him, slamming against your rim on every stroke. Fat and hot and bigger every time. Stretching you. Holding you right at the edge."
    wlf_you "\"You holding out on me? {i}Alpha.{/i} Don't you— {i}don't you dare{/i}—\""
    wlf_alpha "\"Take it. Breed you.\""
    "He pulls back, and drives in, and you shove back to meet him, yelling, and the stretch goes wider, and wider, so full your whole body is just {i}stretch{/i}, a huge, hot, overwhelming fullness—"
    show cg wlf_knot_pop onlayer cgl
    vn_sfx "{i}POP.{/i}" with vnfx("shake", "flash")
    wlf_you "\"{i}AHHHH—!{/i}\""
    "It's in. Locked. Him and you, tied, and the pleasure goes off in you like a flare. You got it. You {i}got{/i} it—"
    show cg wlf_knot_shift onlayer cgl
    "{color=#ff5fb8}And then something {i}moves{/i}.{/color}"
    "{color=#ff5fb8}Under the knot, deep inside, everything goes hot and slick and {i}shifts{/i}.{/color}"
    show wlf_pc furious
    wlf_you "\"Wait. {i}WAIT{/i}— what's— what's happening— that's NOT the— I didn't ask for—\""
    "His hand closes on your nape again and holds you right where you are. You buck. You claw the furs. You can't go anywhere: you're tied to him, and he doesn't let go, and it doesn't stop."
    "{color=#ff5fb8}The room that isn't there makes itself, pulse by pulse, around him. Your cock, stiff and bouncing under you, goes hot, and tight, and then it's just— not. Your balls draw up and keep drawing, up and in and {i}gone{/i}.{/color}"
    wlf_you "\"No— {i}no{/i}, put it {i}back{/i}— that's {i}mine{/i}— alpha, {i}stop{/i}, stop, it's—\""
    $ wlf.shifted = True
    $ wlf_body("3f")
    "{color=#ff5fb8}And in their place, wrapped round the knot, clenching on it, a {i}cunt{/i}.{/color}"
    "{color=#ff5fb8}Hot. Wet. Hungry. Fitted to him exactly, so tight round the knot it can't budge.{/color}"
    show wlf_pc flushed
    wlf_you "\"Oh— oh {i}fuck{/i}— oh {i}FUCK{/i}—\""
    "{color=#ff5fb8}Every nerve in it lights up at once, and the no goes out of you in one long, wrecked, howling moan.{/color}"
    show cg wlf_knot_fill onlayer cgl
    "He pumps into you."
    "Not into your ass. Into {i}that{/i}. Brand new and clamped round him, and it ripples, and {i}swallows{/i}, and he keeps coming. Load after load, thick hot pulses, the knot holding every drop in."
    wlf_alpha "\"Full. Breed you. Full.\""
    "Into your ear."
    "And you {i}know{/i}. Flat and certain as a compass bearing."
    $ wlf.bred = True
    "It took."
    show wlf_pc smug
    "And it's {i}rank{/i}. Bigger than any you've had. You can feel that too, flat and certain. The pride hits you hotter than the cum. You come so hard on it you see white, clenching on the knot, yelling a laugh into his furs." with vnfx("shake")
    "And he doesn't stop."
    "He can't pull out. He doesn't try. He rocks, tiny shallow rolls of his hips with the knot lodged deep, and every one of them grinds it against something in your new cunt that makes your toes curl."
    show wlf_pc flushed
    wlf_you "\"{i}Hahh{/i}— oh— oh that's— don't— {i}don't{/i} stop doing that—\""
    wlf_alpha "\"Take it.\""
    wlf_you "\"Again. Tight. {i}More.{/i}\""
    "You order him, in his own register."
    wlf_alpha "\"Breed you. Full.\""
    "He pushes forward even though the knot can't go any further, and it {i}stretches{/i}, and you scream into the furs and come again, clenching so hard on him he groans out loud. Cum and slick drool out round the knot and down the insides of your thighs."
    wlf_you "\"You don't stop. You keep me like this. Knot me forever. Breed me {i}deep{/i}. Deeper. {i}Good.{/i} Fuck. {i}Keep going.{/i}\""
    "You've stopped making sense. You don't care. You're full of him, locked on him, wet and stretched and dripping, every twitch of the knot sending you up again, and you can hear yourself, loud, louder, telling the whole den exactly what's being done to you and how much you love it."
    "Nobody in the den has ever been quiet about anything. You're the loudest of the lot."
    show cg wlf_knot_groom onlayer cgl
    "Locked, the whole middle of it goes slow. He grooms you through it, his tongue up your spine, his fingers combing your hair and tugging your ears, a big hand palming your little tits, squeezing your nipples till you squirm on the knot."
    wlf_alpha "\"Mine now. Keep you. Take it.\""
    show cg wlf_old_back onlayer cgl
    "Up at the mouth, Old Man is untangling a hide. Very carefully. With his back to you."
    show wlf_pc furious
    wlf_you "\"Nobody {i}said{/i} the promotion gate was the knot! You could've {i}told{/i} me, Old Man!\""
    "You yell it down the length of the den, cheek squashed on the furs."
    "Old Man keeps his back turned. Not a flick of an ear."
    hide cg onlayer cgl
    "The knot throbs in you. You're still locked. He's still hard.\n{size=-5}{color=#ff8fa3}▸ Keep going{/color}{/size}"
    jump wlf_knot_locked_sex

## The verdict, locked on the knot: "First pack." You take it as second-in-command.
label wlf_first_pack:
    $ vn_enter(bg="wlf_den", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_knot_hold")
    "Another flood, deep in your new cunt, held in by the knot. You moan like you're being paid for it."
    wlf_you "\"Hold me.\""
    "You order him, half broken."
    "He crushes you in against his chest, mouth at your ear, and says it, deep and sure."
    $ wlf_advance(4)
    wlf_alpha "\"[WLF_VERDICT[4]]\""
    show wlf_pc smug
    wlf_you "\"…First pack. FIRST. Again.\""
    "You say it back, then louder, to the whole den, and grind back on the knot."
    "It hits like oxygen."
    "{i}First pack.{/i} Second-in-command. Bred and knotted and promoted, the rank you clawed your way up for. You arch back into him and squeeze down and grin like a lunatic while he combs his claws through your hair."
    wlf_you "\"Keep going.\""
    "You growl it, loud enough for Old Man to pretend not to hear.\n{size=-5}{color=#ff8fa3}▸ Fall asleep on the knot{/color}{/size}"
    $ vn_pass(60)
    jump wlf_first_pack_night

label wlf_first_pack_night:
    $ vn_enter(bg="wlf_den_night", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_carried_back")
    "At some point the knot lets you go. At some point he lifts you, like he did the first day, like freight, and lays you down in his own furs at the back wall, and lies down round you."
    show screen wlf_furs("night")
    "You're asleep before you can be smug about it. You're smug about it in your sleep.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen wlf_furs
    call vn_night(7)
    jump wlf_day_five

## ---- DAY 5: rung 4's body (a woman's); the tree ("she"); the days after; most nights -------------

label wlf_day_five:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    show screen wlf_furs("wake")
    "You wake at the back wall."
    hide screen wlf_furs
    $ wlf_body(4)
    show cg wlf_woman onlayer cgl
    "{color=#ff5fb8}You stretch, and everything you've got {i}moves{/i}.{/color}"
    "{color=#ff5fb8}Your tits are {i}heavy{/i}. Full, round, spilling over your arms when you hug yourself, bouncing when you sit up. You grab them both and squeeze and moan out loud in the alpha's furs.{/color}"
    "{color=#ff5fb8}Your hips have flared out wide. Your waist is cinched in under your ribs like somebody pulled a drawstring. Your hands run down the curves and don't want to stop. Your face, under your fingers, is soft now. Soft cheeks, soft mouth, everything rounded and pretty. Your hair spills down your back to the middle of it.{/color}"
    show wlf_pc flushed
    wlf_you "\"Oh. Oh, {i}hello{/i}.\""
    "{color=#ff5fb8}It's a {i}woman's{/i} voice. Low and husky and all yours.{/color}"
    "{color=#ff5fb8}And between your legs: wet. Swollen. Still full of him. You slide your fingers down and they sink right in, and you gasp, and your hips buck on their own.{/color}"
    "{color=#ff5fb8}Everything down there is {i}live{/i}. Your new cunt throbs at the lightest touch, your ass clenches every time you move, and you writhe in his furs moaning at absolutely nothing.{/color}"
    wlf_you "\"{i}Ahh{/i}— I can't— I can't even {i}sit{/i}—\""
    hide cg onlayer cgl
    show wlf_pc smug
    "You know how to take him now, front and back, without even thinking. Your body worked it all out on the knot.\n{size=-5}{color=#ff8fa3}▸ Go out to the tree{/color}{/size}"
    $ vn_pass(10)
    jump wlf_tree

## The "she" beat: four flat lines at the tree, filed as streamlining. Nobody remarks on it.
label wlf_tree:
    $ vn_enter(bg="wlf_tree", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    $ wlf.she = True
    "You stand at the tree in the ordinary way and reach down to aim."
    "There's no cock."
    "There are no balls."
    "You reconsider the mechanics, and squat."
    show wlf_pc smug
    wlf_you "\"{color=#f3c969}[WLF_WORD['tree']]{/color}\""
    "You flash your fangs at the morning and go back inside.\n{size=-5}{color=#ff8fa3}▸ Back into the den{/color}{/size}"
    $ vn_pass(10)
    jump wlf_days_after

## The days after: the den reorganises, the belly rounds (size and weight only), rung 5's body lands
## over the days. Somebody's in you most nights: whose is your call.
label wlf_days_after:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_first_cut")
    "The den reorganises round you without a word."
    "You eat first. Bramble brings you the best cut off the rack before it's light. Nobody touches the rack till you're done. Grey gets up off the warm spot by the fire one morning and lies down somewhere else, and doesn't say why, and you take it. Notch changes the ferns under your furs every day."
    $ wlf.fit = "jacket"
    show cg wlf_jacket_buttons onlayer cgl
    "Scrap brings your jacket and fusses with the buttons in his big clumsy hands until you laugh and wear it open for his sake."
    "Nobody runs the range without looking at you first."
    "Hierarchy. Made flesh. You read every inch of it, and you're right."
    $ wlf_body(5)
    show cg wlf_belly_round onlayer cgl
    "{color=#ff5fb8}And the days go by, and you {i}grow{/i}.{/color}"
    "{color=#ff5fb8}Your belly first. It rounds. Every morning a little more, firm and high and heavy, until the jacket won't close over it and you stop trying. You walk with a hand on it. You sit back and stroke it and moan at how {i}big{/i} you're getting.{/color}"
    "{color=#ff5fb8}Your tits go with it. Heavy and full and aching to be touched, nipples dark and fat, swelling and spilling everywhere. You can't put your arms anywhere without them in the way, and you don't want to.{/color}"
    "{color=#ff5fb8}Your hips go {i}wide{/i}. Your ass goes plush and soft and bounces when you walk. Your thighs rub, thick and smooth, and every step is a sway. Your hair's down past your shoulder blades and still going.{/color}"
    show wlf_pc flushed
    "{color=#ff5fb8}And you're {i}so{/i} sensitive. A breath across your nipples sets you off. Your cunt is swollen and slick all day, and you come from Bramble just {i}leaning{/i} on you, loud enough to wake Old Man.{/color}"
    show wlf_pc smug
    wlf_you "\"Look at me. {i}Look{/i} at me.\""
    "You tell the den, both hands on your belly."
    "They look. They're delighted."
    hide cg onlayer cgl
    "And somebody's in you most nights. Your new cunt learns every one of them, and gets very, very good at it."
    menu:
        "Whose turn it is is {i}your{/i} call."
        "Bramble, slow, on his side behind you":
            $ wlf.nights = "Bramble"
        "Notch, fast, before he can get overexcited":
            $ wlf.nights = "Notch"
        "Grey, because he moved off the warm spot":
            $ wlf.nights = "Grey"
    $ vn_pass(60)
    jump wlf_most_nights

label wlf_most_nights:
    $ vn_enter(bg="wlf_den_night", pc="flushed", pc_tag="wlf_pc", cast=[], cg=None)
    if wlf.nights == "Notch":
        show cg wlf_nights_notch onlayer cgl
        wlf_you "\"Notch. Here.\""
        "You lie back and spread your knees round the belly, and he's on you in a heartbeat, sliding into your cunt with a happy groan."
        wlf_notch "\"Take all. So tight. {i}So tight.{/i}\""
        wlf_you "\"Slow {i}down{/i}— no— don't— {i}ahh{/i}—\""
        "He's fast and eager and grinning, his hands careful on the belly, his hips not careful at all, and you're squealing and laughing and coming on him before he does."
    elif wlf.nights == "Grey":
        show cg wlf_nights_grey onlayer cgl
        wlf_you "\"Grey.\""
        "You hold out a hand. He takes it, and lies down behind you, and slides into your cunt from behind, slow, one arm under the belly holding the weight of it."
        wlf_grey "\"Full already?\""
        wlf_you "\"Never.\""
        "You moan it, and push back on him, and he fucks you deep and steady while his hand cups the belly, until you're shaking and squeezing on him."
    else:
        show cg wlf_nights_bramble onlayer cgl
        wlf_you "\"Bramble.\""
        "He's already there, already curled behind you, already hard. He slides into your cunt like he's coming home, and rocks."
        wlf_bramble "\"Slow now. Make full.\""
        wlf_you "\"{i}Mmhhh{/i}— yes— like that—\""
        "Slow and endless, his arm round the belly, his breath in your ear, until you come in long, rolling shudders that don't stop."
    "He finishes deep, holding still, and it's warm in you all night."
    hide cg onlayer cgl
    show screen wlf_furs("night")
    "The fire ticks down.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen wlf_furs
    call vn_night(7)
    jump wlf_day_six

## ---- DAY 6: the belly huge, the milk in; Gil twice; rung 5, "I call the order" --------------------

label wlf_day_six:
    $ vn_enter(bg="wlf_den", pc="flushed", pc_tag="wlf_pc", cast=[], cg=None)
    show screen wlf_furs("wake")
    "You wake at the back wall."
    hide screen wlf_furs
    $ wlf_body("5m")
    $ wlf.milk = True
    show cg wlf_milk onlayer cgl
    "{color=#ff5fb8}You wake up {i}sticky{/i}.{/color}"
    "{color=#ff5fb8}Your chest. Your belly. The furs under you. Wet and warm and sweet-smelling, and you reach up and squeeze one heavy tit to see, and—{/color}"
    "{color=#ff5fb8}It {i}streams{/i}.{/color}"
    wlf_you "\"Oh— oh {i}fuck{/i}— {i}ahh{/i}— haa— oh, that's— oh my {i}god{/i}—\""
    "{color=#ff5fb8}Milk. Thick and white, spurting out of your nipple in a hot little jet across the furs. You squeeze again and it comes again, and the feeling goes straight down to your cunt. You can't stop. You milk yourself, both hands, moaning, drenching your own chest.{/color}"
    show cg wlf_belly_huge onlayer cgl
    "{color=#ff5fb8}And the belly. {i}Huge{/i}, now. Round and hard and high, so heavy you have to roll to get up. You can't see your own feet. You don't care about your feet. You lie there with both hands on it and let it be enormous.{/color}"
    hide cg onlayer cgl
    show wlf_pc smug
    wlf_you "\"{color=#f3c969}[WLF_WORD['belly']]{/color}\""
    "Your tits know what hands are for now, and mouths, and you know exactly how to give them both something to do."
    show wlf_bramble grin at vn_cast_slot
    "You can't get up on your own. Bramble's there before you've finished trying, an arm under your back, and he appoints himself to it without asking.\n{size=-5}{color=#ff8fa3}▸ Out onto the ledge in the sun{/color}{/size}"
    $ vn_pass(120)
    jump wlf_gil_again

## Gil comes back (twice of two): "Is this what you want?" At rung 3 you hesitated; now you laugh. The
## card goes in the fire; notebook three.
label wlf_gil_again:
    $ vn_enter(bg="wlf_mouth", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_ledge_sun")
    "You're on the ledge in the sun, propped on furs, belly high, jacket open, milk beading on your nipples and running down, the pack bustling round you, when boots come up the slope."
    hide cg onlayer cgl
    show wlf_gil flat at vn_cast_slot
    "Gil Merrow stops halfway up. He takes it all in: the ears, the tail, the belly, the wolf-men round you, the milk. He holds his hands open where everyone can see them."
    "The pack looks at {i}you{/i} before anybody moves."
    wlf_gil "\"[wlf_pc_name]. Is this what you want?\""
    "Kind. Straight."
    menu:
        "Gil on the slope. The pack, waiting on you."
        "Fold your hands on the belly":
            $ wlf.gil2 = "belly"
        "Grin at him with every fang":
            $ wlf.gil2 = "grin"
        "Tell him about the survey, one last time":
            $ wlf.gil2 = "survey"
    show cg wlf_laugh onlayer cgl
    "You laugh."
    "You can't help it. It comes up out of you from somewhere under the belly, loud and delighted, and it rolls round the ledge, and two of the pack look up and grin with you without knowing why. The first time, up on the ridge, you couldn't even get the word out."
    if wlf.gil2 == "grin":
        "You grin at him so wide it shows every fang you've got."
    elif wlf.gil2 == "survey":
        wlf_you "\"Survey's done. Turns out I'm the result.\""
        "And then, because he deserves it straight:"
    else:
        "You fold both hands over the belly."
    wlf_you "\"Got everything I need, Gil. Thanks for asking. Don't wait for me.\""
    hide cg onlayer cgl
    "That's all he needed. He holds your eye a moment, nods, and goes back down the slope."
    hide wlf_gil
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_card_fire")
    "That evening the card goes in the fire without any ceremony at all. It curls, and goes black, and that's that."
    "You get the notebook out one last time. Your writing's terrible now. Your hands are full of other things."
    show screen wlf_notebook(3)
    "You write it up.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    hide screen wlf_notebook
    $ vn_until(18)
    jump wlf_my_pack

## Rung 5's verdict at dusk: his hand on the belly, "My pack.", and he goes out with Grey. Then the
## order is yours.
label wlf_my_pack:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    "Dusk, blue and low. The den is warm."
    show wlf_alpha flat at vn_cast_slot
    "The black one comes in from the ledge and walks the length of the den to you: big, silent, impossible to miss. He looks you over. Ears, tail, heavy dripping tits, the belly, your cunt slick and needy where you sit propped on the furs."
    show cg wlf_hand_belly onlayer cgl
    "You tip the belly up to him."
    "He crouches and lays one big hand on it."
    $ wlf_advance(5)
    wlf_alpha "\"[WLF_VERDICT[5]]\""
    "It goes through you like a drum. Another step up."
    hide cg onlayer cgl
    "He gives a short, approving huff, and goes back out into the dark, and Grey goes with him."
    hide wlf_alpha
    "That leaves Notch, Bramble and Scrap. And Old Man at the far end, snoring by the fire. They're all looking at you for the next word."
    "You let it stretch."
    wlf_you "\"Line up. I call the order.\"\n{size=-5}{color=#ff8fa3}▸ Point at Scrap{/color}{/size}"
    $ vn_pass(5)
    jump wlf_order

## Rung 5, consensual: "I call the order." Scrap first, promoted on the spot, missionary with the
## belly between you, his mouth on your nipple.
label wlf_order:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_scrap", "shy")], cg=None)
    wlf_you "\"Scrap. You first.\""
    show wlf_scrap eager
    "You watch him understand it. The newest in the den, called up ahead of Notch and Bramble by your own mouth. Promoted on the spot. His ears go straight up."
    wlf_you "\"Knees. Don't make me wait.\""
    hide wlf_scrap
    show cg wlf_order_scrap onlayer cgl
    "You spread yours wide round the belly, and show him your cunt. He kneels between your legs, shaking. He nuzzles the belly first, then lower, and his tongue drags hot and flat up your slit, and you {i}yell{/i}."
    show wlf_pc flushed
    wlf_you "\"Not {i}that{/i}— {i}in{/i}— get {i}in{/i} me—\""
    "You guide him with your hand. He sinks in slow, so slow, careful of the belly between you, one big hand under it holding the weight."
    wlf_you "\"{i}Ahhh{/i}— yes— {i}Scrap{/i}—\""
    wlf_scrap "\"Let me. Want this. {i}First tonight.{/i}\""
    "He gasps it, already in to the root."
    show cg wlf_order_scrap_milk onlayer cgl
    "He rocks into you, slow and shallow and reverent, and then he leans down and closes his mouth on your nipple, and {i}sucks{/i}."
    "Milk spurts. Hot, straight into his mouth, running down your tit, and the pull of it goes right down into your cunt."
    wlf_you "\"Oh {i}god{/i}— yes— {i}drink{/i}— don't you {i}dare{/i} stop—\""
    wlf_scrap "\"Breed you. Mine now. Breed you.\""
    "He pants it round your nipple."
    wlf_you "\"Louder, Scrap. Tell them you're {i}first{/i}. Tell all of them.\""
    "He groans it, and thrusts harder, careful of the belly and nothing else, and you milk his cock with your cunt and your tit gushes into his mouth and you come, shouting, belly jolting, legs locked round him." with vnfx("shake")
    "He comes with you. Deep. Shaking. Every pulse of it."
    "When he finally slips out he lies down by your side with his eyes shut, licking milk off your shoulder, the happiest man in the forest.\n{size=-5}{color=#ff8fa3}▸ Split-ear. Here.{/color}{/size}"
    $ vn_pass(15)
    jump wlf_order_notch

label wlf_order_notch:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_notch", "grin")], cg=None)
    wlf_you "\"Split-ear. Here. On your knees, mouth open, and don't get greedy till I say.\""
    "Notch snorts with pleasure and does exactly that."
    hide wlf_notch
    show cg wlf_order_notch_lick onlayer cgl
    "You spread yourself wider round the belly, milk smeared all over your tits, and he dives in. Tongue flat and hot and fast through your slit, lapping up Scrap's mess, licking you like he's starving. His hands spread round the curve of the belly, reverent."
    show wlf_pc flushed
    wlf_you "\"Ahh— {i}ahh{/i}— oh, {i}Notch{/i}—\""
    "Milk runs down your side. He catches it on his tongue. Moves up, licks your nipple, scrapes it with a fang, just enough to make you jump."
    "You grab his head and haul his face up to yours."
    show wlf_pc smug
    wlf_you "\"Cock. In. Now.\""
    show cg wlf_order_notch onlayer cgl
    "He fumbles. He obeys. He's in you in one slick shove, hissing."
    wlf_notch "\"Take all. {i}Take all.{/i} So tight.\""
    wlf_you "\"Full. {i}Hard.{/i} You want a real turn, you fill me.\""
    "Every word's a crack of the whip, and he gives you everything, wild, fast, hands wide and braced either side of the belly so he never knocks it, tail going like mad."
    "You squeeze your own tit and milk spurts straight up into his face. He moans like you've shot him."
    wlf_notch "\"Mine now. Squeeze it. Wet cunt. {i}Full—{/i}\""
    show wlf_pc flushed
    "His teeth close on your nipple and he sucks a mouthful of milk and comes, emptying into you, and the pull of his mouth sets you off again, arching, gushing milk, coming round his cock." with vnfx("shake")
    "You hold him in as long as you can. Then you swat him aside, laughing.\n{size=-5}{color=#ff8fa3}▸ Burr-brain. Your turn.{/color}{/size}"
    $ vn_pass(15)
    jump wlf_order_bramble

## Rung 5, last: Bramble lifts you into his lap. Milk everywhere. Everyone careful with the belly
## without being asked. Then the bed they build you at the back wall.
label wlf_order_bramble:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_bramble", "grin")], cg=None)
    wlf_you "\"Burr-brain. Your turn.\""
    hide wlf_bramble
    show cg wlf_order_bramble_lap onlayer cgl
    "You hold your arms up. You're too heavy to get up on your own and you don't care. Bramble scoops you up, one arm under your knees and one under your back, and settles you in his lap, legs spread over his thighs, belly proud, tits heavy over it."
    "He kisses the belly, just above your navel. Slow. Then he looks up at you."
    wlf_you "\"Inside. Deep. No teasing. I'm not delicate.\""
    "You order him, spreading your cunt with your fingers, slick with all of them."
    "He grins his crooked grin and sinks you down onto him."
    show wlf_pc flushed
    wlf_you "\"{i}Haaaah{/i}—\""
    wlf_bramble "\"Breed you. Mine now. Full.\""
    wlf_you "\"Harder— I want to feel it {i}everywhere{/i}—\""
    show cg wlf_order_bramble onlayer cgl
    "He bounces you. Every thrust squashes the belly between you and squeezes your tits and milk spatters all over his chest. He leans down and sucks it off you. You throw your head back and {i}yell{/i}, proud and wordless, and bite his ear hard enough to mark him."
    wlf_you "\"Faster. {i}More.{/i} I want it running out of me.\""
    "He lifts you by the hips and thrusts up into you so deep you see stars, milk and cum and belly all at once, until you come again, shuddering, and he follows, groaning your name into your shoulder, filling you up." with vnfx("shake")
    "It runs out of you. Exactly like you ordered."
    show cg wlf_order_heap onlayer cgl
    "Scrap and Notch crawl up on either side and start licking the milk off your arms and your neck. Bramble keeps you on his lap, rocking you slow."
    show wlf_pc smug
    wlf_you "\"Don't stop. Keep me up. Slow. All of you, hands on me. Every place I've earned.\""
    "They do."
    menu:
        "Three of them round you, careful of the belly."
        "One more round, all three":
            $ wlf.round5 = True
            jump wlf_order_sex
        "Let them carry you to bed":
            $ wlf.round5 = False
            $ vn_pass(30)
            jump wlf_order_night

label wlf_order_after:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_order_round_cum")
    "Another load, warm and deep, and three pairs of hands careful on the belly the whole time.\n{size=-5}{color=#ff8fa3}▸ Let them carry you to bed{/color}{/size}"
    $ vn_pass(20)
    jump wlf_order_night

label wlf_order_night:
    $ vn_enter(bg="wlf_den_night", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_bed_built")
    "They've built you a bed at the back wall while you weren't looking. The best furs in the den, piled deep, and Notch's ferns under them, still green."
    "Bramble lays you down in it. Somebody tucks the jacket over the belly. Somebody else licks the last of the milk off your collarbone."
    show screen wlf_furs("night")
    "You fall asleep giving orders.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen wlf_furs
    call vn_night(7)
    jump wlf_day_seven

## ---- DAY 7: the birth passed off the page; the ending ("The Den Is Yours") ----------------------

## The birth has passed in the night: one oblique waking line, no offspring words. The alpha keeps
## away all day.
label wlf_day_seven:
    $ wlf.born = True
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    show screen wlf_furs("wake")
    "You wake in the bed they built you."
    hide screen wlf_furs
    $ wlf_body("5b")
    "Old Man went down to the lower den before light. The belly's gone soft; your tits haven't got the message."
    show cg wlf_den_busy onlayer cgl
    "From dawn to dusk the den is busy at your edges. Grey in and out. Bramble with the best cut, still hot. Notch with a clean pelt to tuck round you. Scrap at your side, anxious, sneaking looks at you and then bounding off when you laugh at him."
    "You lie at the back wall and watch them run the place round you. Your tail, your ears, your fangs, all of it reflected back at you in theirs. Every move in the den bends toward the back wall."
    hide cg onlayer cgl
    "The alpha keeps away all day. Not once through the den. Not even his shadow on the floor."
    "You mark that. It means something. You're going to collect.\n{size=-5}{color=#ff8fa3}▸ Dusk{/color}{/size}"
    $ vn_until(19)
    jump wlf_den_is_yours

## The ending's verdict: he lies down across the mouth, facing out, in the guard's place. You walk the
## length of the den and present behind him: a gift, not a plea.
label wlf_den_is_yours:
    $ vn_enter(bg="wlf_mouth", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_guard_place")
    "At twilight, the alpha walks to the mouth of the cave."
    "He lies down across it. Head high, big hands loose on the stone in front of him, the black tail sweeping across the way out. Facing out, at the trees. Right where your first hide was."
    "The guard's place. The lowest post in the den."
    "He doesn't look in at you. One ear flicks at the last of the birdsong. And he says it."
    $ wlf_advance(6)
    wlf_alpha "\"[WLF_VERDICT[6]]\""
    "It rings off the stone."
    "Better than the knot. Better than all of it. The top of the den, by open declaration."
    hide cg onlayer cgl
    show cg wlf_walk_length onlayer cgl
    "You get up. In nothing but the open jacket, every line of you on show: wide hips, heavy tits, the soft new curve of your belly, your tail sweeping the floor like a flag. You walk the whole length of the den toward the gold at the mouth and the black shape lying across it, slow, every step a statement, feeling your hips sway."
    "You stop right behind him."
    "The first time, you bent for a headlamp and he called it presenting. This time you're going to {i}present{/i}, and you're going to mean every inch of it."
    menu:
        "The black shape across the mouth. Your den behind you."
        "Kneel behind him and open yourself with your fingers":
            $ wlf.how_end = "fingers"
        "Bend at the waist, tail aside, and wait for him to turn":
            $ wlf.how_end = "bend"
    jump wlf_gift_sex

## The knot, given at last; the last row lands on it (the growth climax); you start the howl and five
## voices come in under yours. End on the noise.
label wlf_howl:
    $ vn_enter(bg="wlf_mouth", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_gift_knot")
    "And then the knot."
    "Not battering. Not withheld. {i}Offered.{/i} Pressing, thick and slow and hot, right at your entrance, and waiting."
    "You push back, and take it."
    vn_sfx "{i}Pop.{/i}" with vnfx("shake")
    wlf_you "\"{i}Ahhhhh—!{/i}\""
    "Locked. Given. And it sets off {i}everything{/i}."
    $ wlf_body(6)
    show cg wlf_gift_grow onlayer cgl
    "{color=#ff5fb8}Your tits swell into his hands, heavy, huge, so full of milk it sprays out of you when he squeezes. Your hips surge wide.{/color}"
    $ wlf.fit = "nude"
    "{color=#ff5fb8}Your ass and thighs swell so plush and thick they split what's left of the jacket clean off you. Your face goes lush, your lips fat and soft round your fangs. Your hair spills down your back and past your waist, and keeps spilling, all over the stone.{/color}"
    "{color=#ff5fb8}And your voice.{/color}"
    "{color=#ff5fb8}It opens.{/color}"
    "{color=#ff5fb8}The orgasm starts in your thighs and rolls out through every inch of you, clamping on the knot, your vision breaking into stars, and you tip your head all the way back and let it out:{/color}"
    show cg wlf_howl onlayer cgl
    "{color=#ff5fb8}the loudest howl you've ever given.{/color}"
    vn_sfx "{i}Aaaooooooo—{/i}" with vnfx("shake", "flash")
    "First. Before anyone. Higher and longer than anything you were ever allowed."
    show cg wlf_chorus onlayer cgl
    "And under it, the pack comes in."
    "Grey. Bramble. Notch. Scrap. Old Man. Five voices, taking the note under yours and holding it."
    "But yours is first. And highest. Out over the ledge and the pines and the lake, so every living thing on this side of the forest knows exactly whose den this is."
    "He stays locked in you, driving you through it, and you don't stop. Not when the echo comes back. Not when the chorus swells."
    "You keep it going until your throat burns and the whole valley knows.\n{size=-5}{color=#ff8fa3}▸ The den is yours{/color}{/size}"
    $ vn_pass(60)
    jump wlf_ending

## THE ENDING, "The Den Is Yours": the feat. Then stay or go; the two choices decide the ending
## (owner, 2026-11-11: mark them).
label wlf_ending:
    $ wlf.ending = "den"
    $ vn_feat("The Den Is Yours")
    call vn_night(7)
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_morning_gold")
    "Morning comes up gold at the mouth of the cave."
    show screen wlf_furs("wake")
    "You stretch at the back wall."
    hide screen wlf_furs
    "You lie in your bed at the back wall, sticky and hoarse and enormous with pride, and you look down the length of your den."
    "You came in here not pack. Carried, like freight, and dumped on the floor."
    "Now everything in this cave turns toward you when you breathe."
    "You were right the whole time. Every promotion was real. You climbed the ladder all the way up."
    hide cg onlayer cgl
    "You just thought \"alpha\" was the top of it."
    menu:
        "Your den. The forest past the mouth."
        "Stay. The den is yours." (ending=True):
            jump wlf_stay
        "Walk out on your own feet, because you can" (ending=True):
            jump wlf_go

## Stay: the den stays home. Its one back-wall night: any of the six.
label wlf_stay:
    $ wlf.epilogue = "stay"
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_kit_trophy")
    "You stay."
    "Of course you stay. You run the place."
    "Your kit's still in the corner by the mouth: boots, headlamp, the notebook. You leave it there. It's a trophy."
    "The pack eats when you've eaten. They run the range when you've said so. The alpha sleeps across the mouth with his back to you, in the guard's place, and he's never once looked happier."
    "And every night the back wall is yours, and whoever you call up to it."
    $ vn_enter(bg="wlf_den_night", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    menu:
        "You lie back in the best furs at the back wall, the den quiet round you, and decide who's getting called up tonight."
        "The alpha, up from the mouth":
            $ wlf.wall = "Alpha"
        "Grey":
            $ wlf.wall = "Grey"
        "Notch":
            $ wlf.wall = "Notch"
        "Bramble":
            $ wlf.wall = "Bramble"
        "Old Man":
            $ wlf.wall = "Old Man"
        "Scrap":
            $ wlf.wall = "Scrap"
    jump wlf_back_wall

label wlf_back_wall:
    $ vn_enter(bg="wlf_den_night", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_wall_present")
    if wlf.wall == "Alpha":
        "You say it once, not loud. The alpha gets up from across the mouth and walks the whole length of the den to you, and kneels at the edge of your furs like he's asking."
        "You roll over and give him your back. Tail aside. Wet already."
    elif wlf.wall == "Grey":
        wlf_you "\"Grey.\""
        "He comes straight over, gold eyes bright, and you turn and present for him, face-down, tail high."
        wlf_grey "\"Full already?\""
        "You laugh into the furs."
    elif wlf.wall == "Notch":
        wlf_you "\"Notch.\""
        "He's there before you've finished saying it, grinning, tail going, and you go down for him on your elbows and wiggle."
        wlf_notch "\"So tight.\""
        "He breathes it, before he's even touched you."
    elif wlf.wall == "Old Man":
        wlf_you "\"Old Man.\""
        "He gets up from the fire slowly, and comes over with every courtesy, and you present for him like a lady."
        wlf_old "\"Breed. Courtesy.\""
        "You snort."
    elif wlf.wall == "Scrap":
        wlf_you "\"Scrap.\""
        "His ears shoot up. He comes over like he's been promoted all over again, and you present for him and look back and wink."
        wlf_scrap "\"Let me.\""
        "Still. After everything."
    else:
        wlf_you "\"Bramble.\""
        "He's already halfway over, burrs and all, and you roll onto your knees and present for him with a long, lazy stretch."
        wlf_bramble "\"Messy or clean?\""
        wlf_you "\"{i}Messy.{/i}\""
    "You push back onto him.\n{size=-5}{color=#ff8fa3}▸ Push back onto him{/color}{/size}"
    jump wlf_back_wall_sex

label wlf_back_wall_after:
    $ vn_enter(bg="wlf_den_night", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_wall_knot")
    "At the end of it he presses in deep and the knot swells and you take it, {i}pop{/i}, tied, moaning into the furs, his load pumping into you with nowhere to go."
    "You lie locked together at the back wall, his arm over your hip, until it lets you go."
    show screen wlf_furs("night")
    "The den is yours. So is everyone in it.\n{size=-5}{color=#ff8fa3}▸ Into your den{/color}{/size}"
    hide screen wlf_furs
    jump wlf_route_return

## Go: you walk out on your own (Gil's card is ash). The den will be right where you left it.
label wlf_go:
    $ wlf.epilogue = "go"
    $ vn_enter(bg="wlf_treeline", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_walk_out")
    "You walk out."
    "On your own. In daylight. Down the ledge, through the ferns, past the lake, nobody following, nobody stopping you. Gil's card is ash in the fire behind you. You don't need it. You know the way."
    show cg wlf_look_back onlayer cgl
    "At the treeline you stop, the way you did the first morning, and look back."
    "The whole pack is on the ledge, watching you go. Not one of them moves to follow. They're waiting to see what you want."
    "You'll be back. Whenever you like. The den will be right where you left it, and the pack will get out of your way.\n{size=-5}{color=#ff8fa3}▸ Into town{/color}{/size}"
    jump wlf_route_return
