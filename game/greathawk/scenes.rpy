## greathawk's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, then the passage after,
## which lands the climax. Lines from greathawk.js's pools: setup.greathawkLines.noncon (Kite's
## taking lines, banded landbound / mate / bred / wife and keyed by act) and setup.slPcLines.greathawk
## (protest, betray, break, and the speech actions the player picked: demand, plead, mock, scream).
## Every scene is non-con and none flips (owner, 2026-10-19/20). A speech menu in each, for flavour,
## never whether. Kite pins and holds; he never threatens, never cruel. Three to six words, present
## tense, no articles.

## Rung 3, the nest: "Mouth. Now." A fist in your hair. Nobody touches you between the legs.
## (rungs.twee :: Greathawk Mouth Sex; lead Kite, oral, inside, deny anal, noncon, pool greathawk)
label grh_mouth_sex:
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cg="grh_mouth_open")
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Mouth. Now.\""
    "His fist closes tighter in your hair and holds your head where he wants it. All the way down, and held."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Stay. Good.\""
    grh_you "\"{i}Mmph{/i}— Kite— {i}mmph{/i}— I said no last night and I'm saying it {i}now{/i}—!\""
    "It comes out round him, mangled. He doesn't need it to come out right."
    menu:
        "His fist in your hair. His cock in your throat."
        "Pull off to tell him to get off":
            "You get your mouth off him for one breath."
            grh_you "\"Get OFF me— I've got a ROPE— I'm {i}leaving{/i}—!\""
            "His hand brings your head straight back down, and the rest of it goes into his belly feathers."
        "Mock him round it":
            "You pull back just far enough to talk."
            grh_you "\"Say it with an ARTICLE for once, you— {i}hhah{/i}— you feathered {i}bastard{/i}—!\""
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Swearing round me. Good.\""
        "Yell for help":
            "You wrench your mouth off him and yell it at the open sky."
            grh_you "\"HELP— anybody— {i}HELP{/i}—!\""
            "It goes out over the moor, and nothing down there is close enough to hear. His fist brings you back down."
    show cg grh_mouth_mid onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Wriggle. Still mine.\""
    "You wriggle. You slap his hip again. He rocks into your mouth, slow and deep, and your throat opens for him because it's that or choke."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Throat open. Take more.\""
    grh_you "\"{i}Mmh{/i}— it's the {i}itch{/i}— it's just the itch— {i}ahh{/i}— stop making it—\""
    "His thumb is behind your ear again, right on the itch, and every stroke of it melts your jaw a bit wider."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Say no again. Mouth full. Good.\""
    grh_you "\"{i}N-nmmh{/i}— {i}no{/i}— {i}mmmh{/i}—\""
    "Your lips are buzzing. Your tongue's gone flat under him without you telling it to. You're breathing through your nose like you've done this a hundred times."
    show cg grh_mouth_peak onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Loud. Sky hears.\""
    "His hips start to give short, heavy bucks, and his fist holds you down for every one of them."
    grh_you "\"I hate you— I {i}hate{/i}— {i}mmh{/i}— why does it feel— {i}hahh{/i}—!\"" with vnfx("shake")
    jump grh_mouth_after

## Rung 4, the nest: THE MANDATORY SCENE. Face-down on knees and elbows, his wings pinning your
## shoulders; "landbound" turns to "mate" mid-scene, unremarked. Your tiny cock comes untouched.
## (rungs.twee :: Greathawk Mate Sex; lead Kite, anal, inside, doggy, lock, noncon, pool greathawk)
label grh_mate_sex:
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cg="grh_mate_open")
    "He pushes in. Slow. Huge. Your whole body goes rigid under the wings and then gives, an inch at a time, around him."
    grh_you "\"No— {i}NO{/i}— Kite— get— {i}out{/i}— that's too— {i}hhhah{/i}—!\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"No asking now.\""
    "He keeps going until his hips are flush against your arse and your tail's bent up over his belly, and he holds there."
    menu:
        "His wings over you. His weight in you."
        "Tell him to get his wings off":
            grh_you "\"Wings OFF. Now. Let me {i}go{/i}—!\""
            "His wings close down over you instead, and pin your shoulders to the straw."
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Stay under me.\""
        "Beg him":
            grh_you "\"Not again— not— {i}please{/i}, Kite, I said NO—!\""
            "He starts to move anyway, slow and deep, and doesn't answer."
        "Shove back at him":
            "You shove back with everything you've got. It drives you further onto him."
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Tight. Fighting me. Good.\""
    show cg grh_mate_mid onlayer cgl
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "His hips start up. Long and heavy, all the way out and all the way back in, and the nest crunches under your elbows on every one."
    grh_you "\"Don't— not there— not {i}there{/i}— {i}haa{/i}— that's not {i}fair{/i}—\""
    "{color=#ff5fb8}Under you, your tiny cock bounces on every thrust, a little pink nub, drooling on the straw. Nobody's touching it. Nobody needs to.{/color}"
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Little cock leaking. Says yes.\""
    grh_you "\"It doesn't— it {i}doesn't{/i}— you're still saying no, I'm still— {i}ohh{/i}—\""
    "You're still saying no. Your hips are pushing back on every word."
    show cg grh_mate_wings onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Mate looks perfect under me.\""
    "Flat. In the middle of it. Like the weather. You hear it land, and say nothing about it, because you're too busy making a noise you've never made."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Wriggle. Still mine.\""
    show cg grh_mate_peak onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Mate takes it all.\""
    "He's pounding you now, the wings shaking over you, and your voice has gone high and broken and loud, and somewhere in it the no's stopped coming."
    grh_you "\"Harder— {i}harder{/i}— I'm still knotting that rope— {i}harder{/i}—!\"" with vnfx("shake")
    jump grh_mate_after

## Rung 5, the pool, then the warm stone ledge: first vaginal, on the morning the cunt arrived. Your
## orders turn from "get off" to break-begging. Never flipped. (bred.twee :: Greathawk Pool Five Sex;
## lead Kite, vaginal, inside, missionary, lock, noncon, pool greathawk)
label grh_pool_five_sex:
    $ vn_enter(bg="grh_pool", pc="overwhelmed", pc_tag="grh_pc", cg="grh_pool_five_open")
    "He pushes in under the water, the head of him first, blunt and thick, and then the rest, slow and steady, opening something you've had for a morning."
    grh_you "\"{i}NO{/i}— not— not {i}inside{/i}— Kite— it's {i}new{/i}— {i}ahh{/i}—!\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Saying no. Squeezing yes.\""
    "His wings stay shut in front of you. His arm stays locked round your waist. The water slaps your tits."
    menu:
        "His arm round your waist. The wings shut in front of you."
        "Order him off":
            grh_you "\"Put me DOWN. Put me down on the {i}ground{/i}, you overgrown {i}pigeon{/i}—!\""
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Wriggle. Still mine.\""
        "Plead with him":
            grh_you "\"Kite— please— not tonight— let me {i}down{/i}—!\""
            "It isn't even night. He doesn't point that out."
        "Scream at the road":
            grh_you "\"Somebody— the ROAD— somebody on the road— {i}HELP{/i}—!\""
            "Nobody on the road. Nobody ever looks up."
    show cg grh_ledge onlayer cgl
    "He lifts you out of the water in one go, still inside you, and lays you on your back on the warm stone ledge, and pins your thick thighs open with his hands."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Stay. Taking you.\""
    "Over you like a wall of feathers, his wings rattling in the sun, and he starts to fuck you properly."
    grh_you "\"Get off— get {i}out{/i}— {i}stop{/i}— stop, I don't— then why am I— {i}nngh{/i}— so {i}wet{/i}—\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Hate me loud. Good.\""
    "You do. You hate him at the top of your voice, and your new cunt clamps down on him on every word."
    show cg grh_ledge_mid onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Keep it in. Good.\""
    grh_you "\"It's the— it's the cold water— {i}ahh{/i}— why's it—\""
    "The water's warm. The stone's warm. Nothing's cold anywhere. Your orders are changing, and you can hear them change."
    show cg grh_ledge_peak onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Fill you full.\""
    grh_you "\"Fuck— FUCK— fill me, then— I'm still leaving— don't STOP—!\"" with vnfx("shake")
    jump grh_pool_five_after

## Rung 6, the nest: bred, on top. He lifts you onto him and holds your hips down; "Climbing off? No."
## (bred.twee :: Greathawk Ride Sex; lead Kite, ride, noncon, pool greathawk)
label grh_ride_sex:
    $ vn_enter(bg="grh_nest_night", pc="overwhelmed", pc_tag="grh_pc", cg="grh_ride_open")
    "He brings you down onto him. All the way. His hands don't stop until you're sitting on his hips with all of him inside you."
    grh_you "\"{i}Hnnngh{/i}— off— let me {i}off{/i}— get your {i}hands{/i}—\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Stay down. Good.\""
    "His hands clamp your hips and hold you down on him, and your tail lashes, and your heavy tits swing over his face."
    menu:
        "His hands clamped on your hips."
        "Push up off his chest":
            "You push up off his chest with both hands. You get about an inch."
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Climbing off? No.\""
            "And you're back down on him, all the way."
        "Mock him":
            grh_you "\"Big scary hawk. Can't get a single {i}yes{/i} out of me. Pathetic.\""
            "He lifts you by the hips and drops you back on him."
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Bounce. Louder.\""
        "Beg him to let you go":
            grh_you "\"Please— let me go— I won't even touch the rope— {i}please{/i}—!\""
            "His thumbs stroke your hipbones. His hands don't move."
    show cg grh_ride_mid onlayer cgl
    "He starts lifting you. Up, and down, his hands doing all of it, your thighs spread wide over him, {i}shlk, shlk, shlk{/i}."
    grh_you "\"Don't— you're {i}moving{/i} me— don't squeeze them— {i}ahh{/i}— {i}harder{/i}— no, I didn't—\""
    "His palm spreads over your belly."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Mine. All mine.\""
    grh_you "\"I'm not— I'm not your— whatever this is— I'm not— {i}hngh{/i}—!\""
    show cg grh_ride_peak onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Keep it in. Good.\""
    "You're bouncing on your own now. You can feel your thighs doing it. You can't make them stop, and you're too busy shouting to try."
    grh_you "\"More— {i}more{/i}— fine— FINE— just keep— {i}ahh{/i}— {i}ahh{/i}—!\"" with vnfx("shake")
    jump grh_ride_after

## Rung 7, the lip: bent over the broken edge in the wrong wind, face to the yard the rope reaches.
## (bred.twee :: Greathawk Lip Sex; lead Kite, vaginal, inside, doggy, lock, noncon, pool greathawk)
label grh_lip_sex:
    $ vn_enter(bg="grh_lip_night", pc="overwhelmed", pc_tag="grh_pc", cg="grh_lip_open")
    "He pushes into you from behind, over the edge, with the wind screaming up the drop into your face."
    grh_you "\"DON'T— don't you— {i}Kite{/i}— not over the— {i}aaah{/i}—!\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Stay. Wife stays.\""
    "His forearm locks across your waist and holds you on the edge. Nothing under your face but air."
    menu:
        "The rope below you. His arm across your waist."
        "Tell him to let you go":
            grh_you "\"Get OFF me— I've got a ROPE— I'm {i}leaving{/i}—!\""
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Look down. Rope is there.\""
            "It is. All the way to the yard."
        "Mock him":
            grh_you "\"Is that it? I've had more out of the {i}wind{/i}—!\""
            "He gives you more than the wind. A lot more."
        "Flap your wings to get free":
            "Your wings beat, wild, and catch the wind, and drag the both of you back from the edge."
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Wings flapping. Still mine.\""
    show cg grh_lip_mid onlayer cgl
    "He fucks you over the lip, long and deep, the wind tearing at both of you. Every thrust pushes your face out over the drop and your rope."
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Swearing at me. Squeezing me. Good.\""
    grh_you "\"Stop— stop, I don't— then why am I— {i}nngh{/i}— so {i}wet{/i}—\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Wife takes it all.\""
    show cg grh_lip_peak onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Fill you full, wife.\""
    grh_you "\"Don't stop— Kite— don't you {i}dare{/i} stop— I still hate you—!\"" with vnfx("shake")
    jump grh_lip_after

## The ending's act, the perch at dusk: against the parapet, her thigh up round his hip; the duet
## torn out of her at the climax (in the passage after). (ending.twee :: Greathawk Duet Sex; lead
## Kite, vaginal, inside, missionary, noncon, pool greathawk, never flipped)
label grh_duet_sex:
    $ vn_enter(bg="grh_perch_dusk", pc="overwhelmed", pc_tag="grh_pc", cg="grh_duet_open")
    "He pushes in, holding your thigh up round his hip, and pins you to the parapet with all of him."
    grh_you "\"{i}KITE{/i}— not here— not {i}here{/i}— the whole moor— {i}ahh{/i}—!\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Loud. Sky hears.\""
    "Your wings are flat against the stone behind you. His are open over you both, black against the last of the light."
    menu:
        "Pinned to the parapet. The moor below, listening."
        "Shout that you're leaving":
            grh_you "\"Next right wind— I'm {i}gone{/i}— you hear me— {i}gone{/i}—!\""
            show grh_kite flat at vn_cast_slot
            grh_kite "\"Wife is here.\""
        "Plead with him":
            grh_you "\"Kite— please— not tonight— let me {i}down{/i}—!\""
            "He doesn't let you down. He lifts your other thigh too."
        "Bite his shoulder":
            "You bite his shoulder, hard, through the feathers. He makes a pleased sound and goes deeper."
    show cg grh_duet_mid onlayer cgl
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Wife takes it all.\""
    "He fucks you against the stone, slow and deep, his hands under your huge thighs, your tits heaving against his chest."
    grh_you "\"I hate you— I {i}hate{/i}— {i}mmh{/i}— why does it feel— {i}hahh{/i}—!\""
    show grh_kite flat at vn_cast_slot
    grh_kite "\"Swearing at me. Squeezing me. Good.\""
    show cg grh_duet_peak onlayer cgl
    "And something's building in your chest. Not a scream. Something with notes in it."
    grh_you "\"Don't— don't {i}stop{/i}— no— I didn't mean— I'm still LEAVING— {i}AHH{/i}—!\"" with vnfx("shake")
    jump grh_duet_after
