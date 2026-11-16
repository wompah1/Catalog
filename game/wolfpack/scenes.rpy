## wolfpack's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats: open, a speech choice, mid, peak, then the passage after.
## Lines from wolfpack.js's pools: the pack's (setup.slCombatLines, their noncon taking lines and
## act lines) and the PC's (setup.slPcLines.wolfpack for rungs 1-2, wolfpackSecond for rung 3,
## wolfpackKnot for the knot's first stage; the consensual speech actions after the flips). Rungs 1
## and 2 never flip; rung 3 and the knot's first stage flip at the break; everything after is
## consensual. The choice is what you say, never whether. One cock in you at a time.

## ---- RUNG 1's optional round: the alpha, still in you (non-con, no flip) -------------------------
label wlf_round_one_sex:
    $ vn_enter(bg="wlf_den_night", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_r1_round")
    "He never pulled out. He just starts again, slow, the whole thick length of him dragging back through the mess he made."
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Hold.\""
    "His weight comes down across your back, and you can't get your knees under you."
    wlf_you "\"Let go of my neck— {i}let go{/i}— I'm not low ANYTHING—!\""
    menu:
        "His weight on your back. His hand on your nape."
        "Order him off":
            $ wlf.say1 = "demand"
            wlf_you "\"Get OFF me— that's an ORDER— I outrank every one of you—!\""
            show wlf_alpha flat at vn_cast_slot
            wlf_alpha "\"Loud. Good.\""
            "He drives into the same spot, unhurried."
        "Mock him":
            $ wlf.say1 = "mock"
            wlf_you "\"That's IT? That's the big bad pack? I've had rougher {i}surveys{/i}—!\""
            show wlf_alpha flat at vn_cast_slot
            wlf_alpha "\"Hold. Take it.\""
            "His palm flattens you back down onto the furs."
        "Scream for anybody":
            $ wlf.say1 = "scream"
            wlf_you "\"SOMEBODY— anybody— get this— get him {i}OFF{/i} me—!\""
            "The cave throws it straight back at you."
            show wlf_alpha flat at vn_cast_slot
            wlf_alpha "\"Loud.\""
            "He says it approving, while you swear at him at the top of your lungs."
    show cg wlf_r1_round_mid onlayer cgl
    vn_sfx "{i}Slap. Slap.{/i}"
    show wlf_pc flushed
    wlf_you "\"This isn't— this doesn't COUNT for rank— does it count— {i}hahh{/i}—\""
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Wet. Mine.\""
    "His teeth rest on your nape. Not biting. Just there."
    "Your hips push back onto him on their own."
    wlf_you "\"That's— that's a reflex— {i}hah{/i}— that doesn't {i}count{/i}—\""
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Full soon.\""
    "The thick base of him presses at your rim, and stays outside."
    show cg wlf_r1_round_peak onlayer cgl
    wlf_you "\"I'm still— I'm still saying no— {i}ohh{/i}— I'm saying it— {i}louder{/i}—\""
    wlf_you "\"Fine— FINE— promote me, then— harder, you bastard—!\"" with vnfx("shake")
    jump wlf_round_one_after

## ---- RUNG 2's round again: the queue (non-con, no flip) -----------------------------------------
label wlf_queue_sex:
    $ vn_enter(bg="wlf_spring", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_queue_again")
    "They queue up again. Same order. Grey's hand is already back on the small of your back."
    show wlf_grey flat at vn_cast_slot
    wlf_grey "\"By rank. Take it.\""
    wlf_you "\"Don't you {i}dare{/i} call that presenting— I was WASHING—!\""
    menu:
        "The queue behind you. Grey's hand holding you down in the moss."
        "Order them off":
            $ wlf.say2 = "demand"
            wlf_you "\"Let me UP. I'm not asking. Let me— {i}nngh{/i}— {i}UP{/i}—!\""
            show wlf_grey flat at vn_cast_slot
            wlf_grey "\"Second.\""
            "His hand on your nape keeps your cheek on the moss."
        "Plead with them":
            $ wlf.say2 = "plead"
            wlf_you "\"Alright— alright, you made your point— get {i}off{/i}— please— get {i}off{/i}—!\""
            show wlf_grey flat at vn_cast_slot
            wlf_grey "\"Full already?\""
            "He doesn't wait for an answer."
        "Growl at them":
            $ wlf.say2 = "growl"
            wlf_you "\"Grrh— {i}off{/i}—\""
            "It comes out through your new teeth, and he takes it as a compliment."
    show cg wlf_queue_again_mid onlayer cgl
    vn_sfx "{i}Slap. Slap. Slap.{/i}"
    show wlf_pc flushed
    "One at a time. Grey, thorough, until he's done; then Notch, all hurry, grinning."
    show wlf_notch grin at vn_cast_slot
    wlf_notch "\"My turn. {i}Mine{/i}.\""
    "He grins and doesn't let go of your hips."
    wlf_you "\"Stop finding it— stop {i}finding{/i} that— {i}ahh{/i}— I'm going to {i}kill{/i} you—\""
    "Your tiny cock's leaking all over the moss."
    wlf_you "\"That's— that's not {i}me{/i}— {i}nnh{/i}— that's not—\""
    show wlf_bramble grin at vn_cast_slot
    wlf_bramble "\"Make full.\""
    show cg wlf_queue_again_peak onlayer cgl
    show wlf_scrap shy at vn_cast_slot
    wlf_scrap "\"Sorry.\""
    "He doesn't stop."
    show wlf_scrap shy at vn_cast_slot
    wlf_scrap "\"Not sorry.\""
    wlf_you "\"Don't stop— I hate you— don't you {i}stop{/i}— fill it— {i}fill{/i} it—!\"" with vnfx("shake")
    jump wlf_queue_after

## ---- RUNG 3's round again: Grey takes it out of your hands, and it flips at the break -----------
label wlf_second_sex:
    $ vn_enter(bg="wlf_den", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_second_again")
    show wlf_grey flat at vn_cast_slot
    wlf_grey "\"Stop. Wriggling.\""
    "His fist closes round the root of your tail and holds it aside, and he's back in you before you've finished turning over."
    wlf_you "\"Not like— not like THIS— I was going to {i}ride{/i} you—!\""
    "His fist on your tail doesn't budge."
    menu:
        "Grey's fist on your tail. His pace."
        "Tell him you're running this":
            $ wlf.say3 = "protest"
            wlf_you "\"I'm running this— I'm {i}running{/i} this, Grey— let me UP—!\""
            show wlf_grey flat at vn_cast_slot
            wlf_grey "\"Stop. Wriggling.\""
            "He leans his weight on your hips until you do."
        "Grab for your tail":
            $ wlf.say3 = "tail"
            wlf_you "\"Get your hand off my— that's MY tail— {i}mine{/i}—!\""
            "You get your fingers on it. He just holds it higher."
        "Mock him":
            $ wlf.say3 = "mock"
            wlf_you "\"Two words at a time— is that all the brain you lot— {i}nngh{/i}— can manage—?\""
            show wlf_grey flat at vn_cast_slot
            wlf_grey "\"Second.\""
            "Like it settles something."
    show cg wlf_second_again_mid onlayer cgl
    show wlf_pc flushed
    wlf_you "\"Stop holding it— stop— {i}ahh{/i}— why does it feel better when you {i}hold{/i} it—\""
    "The heat swallows the next no whole."
    wlf_you "\"{i}Mmhh{/i}— Grey— no— {i}Grey{/i}—\""
    wlf_you "\"Keep it— keep my tail— {i}keep{/i} it— just don't stop—!\""
    show cg wlf_second_again_flip onlayer cgl
    show wlf_pc smug
    $ wlf.flip3 = True
    wlf_you "\"…Low pack? I'll show you low pack.\""
    "You slam back onto him."
    wlf_you "\"Again. {i}AGAIN{/i}.\""
    show wlf_grey flat at vn_cast_slot
    wlf_grey "\"Tight. Good.\""
    "When Grey's done, Bramble's next, and Scrap after him with his face on fire, one at a time, and you call each of them up yourself."
    show wlf_bramble grin at vn_cast_slot
    wlf_bramble "\"Messy or clean?\""
    wlf_you "\"{i}Ahh{/i}— yes— right there— that's rank, that is— that's {i}rank{/i}—!\"" with vnfx("shake")
    jump wlf_second_after

## ---- RUNG 4, stage A: THE KNOT, non-con, flipping at the break ----------------------------------
## You asked for the knot, not to be held flat at his pace. The "NOT the—" lands in the authored knot.
label wlf_knot_sex:
    $ vn_enter(bg="wlf_den", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_knot_open")
    if wlf.how4 == "shove":
        "You shove up against his hand with everything you've got. His weight doesn't shift."
        wlf_you "\"Off— I'll take it sitting up— I'll take it on TOP— {i}alpha{/i}—!\""
    else:
        wlf_you "\"My pace— it was supposed to be MY pace— get your hand off my {i}neck{/i}—!\""
        "He doesn't answer. His hand stays exactly where it is."
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Hold.\""
    "He pushes in. Slow. Enormous. Exactly as slow as he wants, and not one inch faster."
    wlf_you "\"I said KNOT me— I didn't say hold me DOWN— let me {i}up{/i}—!\""
    show cg wlf_knot_mid onlayer cgl
    vn_sfx "{i}Slap.{/i}"
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Take it.\""
    "His hand spreads flat on the small of your back."
    show wlf_pc flushed
    wlf_you "\"I asked— I {i}asked{/i} for it— that doesn't mean you get to— {i}NNGH{/i}—!\""
    wlf_you "\"It's too— it's too {i}much{/i}— why does it— why's it so {i}good{/i} pinned—\""
    "The knot thumps your rim and your whole body answers it."
    wlf_you "\"Don't— {i}don't{/i}— oh, do it— {i}don't{/i}—\""
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Breed you.\""
    "He doesn't speed up. He doesn't need to."
    show cg wlf_knot_break onlayer cgl
    wlf_you "\"Fine— FINE— knot me, then— {i}knot{/i} me, you bastard—!\"" with vnfx("shake")
    jump wlf_knot

## ---- RUNG 4, stage B: locked on the knot, in the cunt; consensual --------------------------------
label wlf_knot_locked_sex:
    $ vn_enter(bg="wlf_den", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_locked")
    "Still tied. Still hard. He rolls his hips, and the knot tugs inside your new cunt, and you push back for more."
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Wet. Tight. Mine.\""
    menu:
        "Locked on the knot, at the back wall."
        "Order him deeper":
            $ wlf.say4 = "demand"
            wlf_you "\"Deeper. I said {i}deeper{/i}. Do I have to say it twice?\""
            show wlf_alpha flat at vn_cast_slot
            wlf_alpha "\"Slow. There. There.\""
        "Tease him":
            $ wlf.say4 = "tease"
            wlf_you "\"You're shaking already? Go on. Earn it.\""
            show wlf_alpha flat at vn_cast_slot
            wlf_alpha "\"Loud.\""
            "You already are."
        "Let the moan out":
            $ wlf.say4 = "moan"
            wlf_you "\"Mmh— {i}mmhh{/i}— deeper— the whole den should hear this— {i}louder{/i}—!\""
    show cg wlf_locked_mid onlayer cgl
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Good pack.\""
    "His thumb rubs the root of your tail."
    wlf_you "\"Hahh— that's it— breed it— breed it {i}properly{/i}—!\""
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Take it. All.\""
    show cg wlf_locked_peak onlayer cgl
    wlf_you "\"Don't stop— don't you {i}dare{/i} stop— I'm— {i}AHH{/i}— fill it— {i}fill{/i} it—!\"" with vnfx("shake")
    jump wlf_first_pack

## ---- RUNG 5's one more round: all three, consensual ---------------------------------------------
label wlf_order_sex:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_order_round")
    "Scrap first again, because you say so, kneeling between your knees, careful of the belly and nothing else."
    show wlf_scrap shy at vn_cast_slot
    wlf_scrap "\"First tonight. First.\""
    "He can't get over it."
    menu:
        "Three of them, one at a time, in the order you call."
        "Give them orders":
            $ wlf.say5 = "demand"
            wlf_you "\"Harder. That's an order. Rank says harder.\""
        "Tease them":
            $ wlf.say5 = "tease"
            wlf_you "\"Come on. Show the den what rank looks like.\""
        "Yell it at the roof":
            $ wlf.say5 = "scream"
            "You throw your head back and yell it at the roof of the cave, loud enough to carry to the lake."
            wlf_you "\"{i}YES{/i}—!\""
    show cg wlf_order_round_mid onlayer cgl
    show wlf_notch grin at vn_cast_slot
    wlf_notch "\"Good pack. So tight.\""
    "Notch, when you swap them, fast and grinning, hands braced wide of the belly."
    show wlf_bramble grin at vn_cast_slot
    wlf_bramble "\"Good pack. Slow.\""
    "Bramble last, slow and endless, rocking you."
    show cg wlf_order_round_peak onlayer cgl
    wlf_you "\"Again— {i}again{/i}— louder— let the whole forest know who's getting promoted—!\"" with vnfx("shake")
    jump wlf_order_after

## ---- THE ENDING's scene: the gift. The alpha, gentle; you run it. Consensual. -------------------
label wlf_gift_sex:
    $ vn_enter(bg="wlf_mouth", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_gift_open")
    if wlf.how_end == "bend":
        "You bent for him at the mouth of his own den, and he turned, and he came up on his knees behind you like it was the only thing left in the world to do."
    else:
        "You knelt behind him and opened yourself with your own fingers, wet and waiting, and he turned, and he came up on his knees behind you like it was the only thing left in the world to do."
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Mine.\""
    "Low. His mouth at your throat."
    wlf_you "\"No. Mine. Slow if you want. But {i}all{/i} of it.\""
    "You tell him, and roll your hips back onto him, slow."
    show cg wlf_gift_mid onlayer cgl
    "He's the gentlest he's ever been. He lets you run it. Every stroke is yours: you rock back and he fills you, you hold and he holds, his palms spread under your belly, his thumb in slow circles on your clit."
    show wlf_alpha flat at vn_cast_slot
    wlf_alpha "\"Easy. Slow. There.\""
    menu:
        "Your den. Your pace. Him, holding still for you."
        "Let the whole forest hear":
            $ wlf.say6 = "moan"
            show wlf_pc flushed
            wlf_you "\"{i}Mmmhh{/i}— there— fuck me slow— I want the whole forest to hear what this sounds like—\""
        "Tell him all of it":
            $ wlf.say6 = "demand"
            wlf_you "\"Don't you dare go easy on me. Again. {i}Again{/i}.\""
            "He doesn't go easy. He goes slow, which is worse, and better."
        "Ask for the knot":
            $ wlf.say6 = "plead"
            wlf_you "\"Please— fill it— I want it, I want {i}all{/i} of it—!\""
            "He presses closer, and the thick base of him nudges you, and waits."
    jump wlf_howl

## ---- STAY's back-wall night: whoever you called up, consensual ----------------------------------
label wlf_back_wall_sex:
    $ vn_enter(bg="wlf_den_night", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_wall_sex")
    python:
        _who = dict(Alpha=wlf_alpha, Grey=wlf_grey, Notch=wlf_notch, Bramble=wlf_bramble, Scrap=wlf_scrap)
        _who["Old Man"] = wlf_old
        _who = _who.get(wlf.wall, wlf_bramble)
        _lines = dict(Alpha=("\"Slow. There. There.\"", "\"Mine now. Full.\""),
                      Grey=("\"Good pack. Take it.\"", "\"Breed you.\""),
                      Notch=("\"Wet. Fast. Mine.\"", "\"Squeeze it. Squeeze.\""),
                      Bramble=("\"Slow now. Make full.\"", "\"Breed you. Mine.\""),
                      Scrap=("\"Want this. Want this.\"", "\"Good pack. So good.\""))
        _lines["Old Man"] = ("\"Easy. Good pack.\"", "\"Steady. Take it.\"")
        _w1, _w2 = _lines.get(wlf.wall, _lines["Bramble"])
        # the speaker's sprite in the box (owner, 2026-11-15): the wolf the PC called to the back wall
        _spr = {"Alpha": ("wlf_alpha", "flat"), "Grey": ("wlf_grey", "snarl"), "Notch": ("wlf_notch", "grin"),
                "Bramble": ("wlf_bramble", "grin"), "Scrap": ("wlf_scrap", "eager"), "Old Man": ("wlf_oldman", "kind")}
        _spr = _spr.get(wlf.wall, _spr["Bramble"])
    "He's in you on the first push, deep, and you rock back to meet him."
    $ renpy.show(_spr, at_list=[vn_cast_slot])
    $ renpy.say(_who, _w1)
    menu:
        "The back wall. Whoever you called."
        "Tell him harder":
            $ wlf.say7 = "demand"
            wlf_you "\"Harder. Pin me. Pin me like you {i}mean{/i} it.\""
        "Tease him":
            $ wlf.say7 = "tease"
            wlf_you "\"Is that all? I've outranked better. Again.\""
        "Let the moan out":
            $ wlf.say7 = "moan"
            wlf_you "\"Oh— {i}oh{/i}— good— so {i}good{/i}— don't you slow down on me—!\""
    show cg wlf_wall_mid onlayer cgl
    $ renpy.show(_spr, at_list=[vn_cast_slot])
    $ renpy.say(_who, _w2)
    wlf_you "\"Don't stop— don't you {i}dare{/i} stop— fill it— {i}fill{/i} it—!\"" with vnfx("shake")
    jump wlf_back_wall_after
