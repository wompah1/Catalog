## The fights (main.twee :: Corps Morph / Stop / Loss / Demorph, and fights.twee): the alert's
## monster, the morph call, the read, the clash in the suit, the demorph and what it leaves. A read
## picks how the fight goes, never whether; "Stop fighting it" (in red) is the opt-in loss. The suit
## only holds a host who's fighting, so it drops you first: every loss plays in your own changing
## body, and nothing ever enters the suit. Nothing penetrates before rung 5 (the Bramblemaw's vines
## at rung 4 excepted, out of the suit). The losses never flip.

## ==== THE FIGHT LOOP ===========================================================================

## call cp_fight("zard"): every part of the day's monster, each with its own morph, read and demorph.
label cp_fight(key):
    $ cp.fight = key
    $ cp.part = 0
    $ cp.lost = False
    $ cp.surged = False
    $ cp.vines = False
    $ cp.morphs_today = CP_MONSTERS[key]["morphs"]
    label cp_fight_part:
        call cp_morph_call
        $ _m = cp_mon()
        $ vn_enter(bg=_m["bg"], pc="neutral", pc_tag="cp_pc")
        "{color=#f3c969}[_m['name']]{/color}"
        "[_m['gimmick']]"
        if _m.get("act"):
            call cp_bramble_bind
        $ _reads = _m["reads"]
        $ _pick = renpy.display_menu([(t, i) for i, (t, ok) in enumerate(_reads)] + [("{color=#ff5a5a}Stop fighting it{/color}", -1)])
        if _pick >= 0:
            $ cp.read, cp.right = _pick, _reads[_pick][1]
        else:
            $ cp.read, cp.right, cp.lost = None, False, True
        if cp.lost and not _m.get("act"):
            call cp_loss
        else:
            $ renpy.call("cp_clash_" + cp.fight)
        call cp_demorph
        if cp.part + 1 < cp.morphs_today:
            $ cp.part += 1
            $ cp.lost = False
            menu:
                "{i}It's not finished. You're going to have to go again.{/i}"
                "Morph again":
                    pass
            jump cp_fight_part
    $ cp.fight = None
    return

## The morph call: "IT'S MORPHING TIME — PINK RANGER, POWER UP!" The first one is the whole change;
## after that it takes less and less, because there's less and less for the Grid to change.
label cp_morph_call:
    $ _first = not cp.morphed_once
    $ cp.morphed_once = True
    $ cp_morph(True)
    if _first:
        $ vn_enter(bg="cp_flat", pc="shocked", pc_tag="cp_pc", cg="cp_morph_first")
        "{color=#ff7ab8}\"IT'S MORPHING TIME — PINK RANGER, POWER UP!\"{/color}" with vnfx("flash")
        "Light floods you from the skin in."
        "Your chest goes first. Pressure, heavy, swelling up under your shirt, {i}pushing{/i}, until—"
        vn_sfx "Pop. Pop." with vnfx("shake")
        "—two round heavy breasts burst out under the flannel, nipples so sensitive you yelp."
        cp_me "\"Oh— {i}fuck{/i}—!\""
        "Your waist cinches in like a fist closing. Your hips slide out. Your ass swells, round and bouncing, and your thighs fatten until they push your knees apart."
        show cg cp_morph_first_melt onlayer cgl
        "Then your cock goes hot. It pulses once, heavy— then {i}melts{/i}. Shrinks. Folds in."
        "Your fingers find fat soft lips and a slick, throbbing emptiness where it used to be, and a wave of hot dizzy {i}want{/i} goes straight up your spine."
        cp_me "\"Nnh— {i}ahh{/i}— what did you—\""
        show cg cp_morph_first_suit onlayer cgl
        vn_sfx "Shhhp."
        "The suit snaps on. Pink, seamless, tight as paint. It squeezes your new tits, slides up between your thighs, and your nipples poke straight through it, fat and obvious."
        "Your hair spills down past your shoulders, long and loose and pink."
        "One breath. That's all it took."
        show cg cp_morph_first_tv onlayer cgl
        "You catch yourself in the black TV screen. A girl. Big tits, wide hips, thighs that don't close. Gasping."
        cp_me "\"This isn't me.\""
        "It comes out a squeak. High and breathy."
        hide cg onlayer cgl
        "Static in your ear. A woman's voice, low and impatient."
        show cp_red neutral at vn_cast_slot
        cp_red "\"Pink! Are you online yet, Pink? Big lizard, the park. {i}Move.{/i}\""
        "Your body moves before you do. Out the window, two floors down, landing light, tits bouncing so hard you moan. Four bounds. A wall run. The park."
        return
    $ _r = min(6, cp.rung or 1)
    $ vn_enter(bg="cp_hub", pc="flushed", pc_tag="cp_pc", cg="cp_morph_r%d" % _r)
    "{color=#ff7ab8}\"IT'S MORPHING TIME — PINK RANGER, POWER UP!\"{/color}" with vnfx("flash")
    if cp.part > 0:
        "Again. Same afternoon. The Grid takes you apart and puts the girl back on before you've caught your breath from the last time."
        "Tits swell into the plates. Hips flare. Between your legs, slick and empty, already wet."
        "You moan into the comm and don't care who hears."
    elif _r <= 2:
        "The rush goes up your legs and doesn't stop. Your chest swells into the plates, heavy and throbbing. Your waist pinches. Your hips shove out."
        "Between your legs your cock melts away into slick, hungry nothing, and the suit's friction lights every new nerve at once."
        cp_me "\"Nnh— {i}ahh{/i}—\""
        "Every time. Every single time."
    elif _r <= 4:
        "It barely takes you apart any more."
        "The suit closes over a chest that's already halfway there, hips that already sway, and the slick heat between your legs arrives like it's been waiting."
        "The suit squeezes. You whimper. Then you're running."
    else:
        "There's hardly anything left for the Grid to change."
        "A last little swell in the plates, the empty slick heat between your thighs, and the suit sealing over a body it doesn't have to argue with any more."
        "You run. The tits bounce. You've stopped noticing."
    hide cg onlayer cgl
    return

## The demorph, on every exit: the suit off first, then what this demorph leaves, where the fight
## held you (each monster's "stays"). A loss or the vines already dropped the suit.
label cp_demorph:
    $ _m = cp_mon()
    $ _was = cp.morphed
    $ cp_morph(False)
    $ cp_body(_m["rung"])
    $ vn_enter(bg="cp_hub", pc="shocked", pc_tag="cp_pc")
    if cp.vines:
        "Zorp's portal yanks the lot of you back to the Hub in a burst of white. You're already demorphed. You've been demorphed since the vines."
    elif not _was:
        "Zorp's portal yanks the lot of you back to the Hub in a burst of white. You're already demorphed. You've been demorphed since the pavement."
    else:
        "Zorp's portal yanks the team back to the Hub in a burst of white. You pull the morpher off your wrist and think {i}demorph{/i} as hard as you can."
        "The armour goes. It always goes the same way. Light. Then no light. Then you, kneeling on the floor in your own clothes, ears ringing."
    $ renpy.call("cp_stays_" + cp.fight)
    if cp.surged:
        $ cp.surged = False
        "{color=#ff9ecb}The Grid takes longer over you this time.{/color} You feel it pause behind your sternum, like a hand over a shelf, deciding."
        "Then it takes everything the rung was going to take, all at once." with vnfx("shake")
        show cp_zorp neutral at vn_cast_slot
        cp_zorp "\"Adaptation yield elevated. Noted.\""
    hide cg onlayer cgl
    return

## "Who touched you?" -- Anya's next scene, after any loss (she heard it on the comm).
label cp_who_touched:
    if cp.touched:
        $ cp.touched = False
        show cp_anya hungry at vn_cast_slot
        cp_anya "\"Who touched you?\""
        cp_me "\"Nobody— it was— a Bogon. It doesn't matter—\""
        cp_anya "\"It matters to me.\""
        "She says it flat, and close, and you feel it all the way down."
    return

## ==== THE OPT-IN LOSS (every fight but Bramblemaw) ===============================================
## The suit drops you, the Bogons are already there, and one of them gets to you first; the others
## hang back to watch (one at a time, never a group). A man (decision 2): Leo stays into women and
## is made to admit men. Mouths and hands before rung 5; from rung 5, the lamp post. Resist, then
## break; it never flips. The three links are how you fight, and all three lose. (At least one
## written loss per rung, owner 2026-11-11.)

label cp_loss:
    $ _m = cp_mon()
    $ _r = cp.rung or 1
    $ cp_morph(False)
    $ cp_body(_m["rung"])
    $ cp.fit = "own"
    $ vn_enter(bg=_m["bg"], pc="shocked", pc_tag="cp_pc", cg="cp_loss_drop")
    "You stop fighting it."
    "And the suit lets go. It only holds a host who's fighting."
    "Light. Then no light. Then you, on your knees on wet pavement, in your own clothes, in your own changing body, panting."
    "The [_m['name']] is somewhere behind you, smashing things. You don't care. Because the Bogons are already here."
    show cp_bogon grin at vn_cast_slot
    "Its foot soldiers. Man-shaped, bog-green, big, [_m['material']]. Three of them, closing in. One of them gets to you first and the others hang back to watch."
    "You try to get up. He grabs your hair. Pulls your face up. Grins."
    cp_bogon "\"{i}Pink{/i}.\""
    "Like it's funny. He's already got his cock out. It's thick and bog-green and it's right in front of your mouth. It smells like the swamp and like sweat and like {i}man{/i}."
    $ renpy.call("cp_loss_r%d" % min(6, _r))
    $ cp.touched = True
    $ cp.surged = True
    hide cp_bogon
    $ vn_enter(bg=_m["bg"], pc="flushed", pc_tag="cp_pc", cast=[("cp_red", "neutral")], cg="cp_loss_red")
    cp_red "\"PINK!\"" with vnfx("shake")
    "Red hits him like a train. He goes flying. Blue and Black are already on the other two, and Red hauls you up off the pavement one-handed and holds you against her side."
    cp_red "\"I've got you. I've got you.\""
    "The team finishes the [_m['name']] without you. It doesn't take long."
    "You still clock Yellow's legs as she jogs past. That part's still yours. It's just not the only part any more."
    hide cg onlayer cgl
    return

## How you fight it: three links, all of them lose.
label cp_loss_fight:
    menu:
        "Clamp your mouth shut":
            $ cp.loss_how = "mouth"
            "You clamp your mouth shut so hard your teeth click. He just waits, rubbing it on your lips, slow, patient, like he's got all day."
        "Shove at him with both hands":
            $ cp.loss_how = "hands"
            "You shove at his thighs with both hands. He catches them. Both of them, in one big bog-green fist, and wraps them round his cock under his own."
        "Glare up at him and tell him where to go":
            $ cp.loss_how = "glare"
            cp_me "\"Go to hell. Go back to the swamp and drown in it, you ugly—\""
            "Your mouth's open. That was the mistake. He's in it before you finish the word."
    return

## Rung 1: still a guy, and it's the nipples that set it off.
label cp_loss_r1:
    cp_me "\"Get that away from me— I'm not— I'm not into {i}guys{/i}—\""
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Mouth says no.\""
    "He rubs the fat head across your lips. Back. Forth. Leaving them slick. You twist your face away and his fist in your hair turns it straight back."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Rest of you's shaking.\""
    "It is. Your nipples are hard through your T-shirt. Your cock is hard in your jeans. You hate both of them."
    call cp_loss_fight
    show cg cp_loss_r1_mouth onlayer cgl
    vn_sfx "Glk. Glk."
    "Then he's in your mouth. Thick. Salty. Swamp-heavy on your tongue. He holds your head and rocks in, slow, shallow, and the other two whistle from the kerb."
    cp_me "\"Mmf— {i}mmmf{/i}— nnh—\""
    "Every thrust drags your T-shirt across your nipples. Every drag is a spark. Straight down."
    cp_me "\"Mmh— why is it— {i}mmf{/i}— I don't even LIKE—\""
    "He reaches down and flicks one nipple through the cotton. Just once."
    show cg cp_loss_r1_cum onlayer cgl
    "Your cock goes off in your jeans. Nobody touched it. You moan round him, loud, wet, and you can't make it stop." with vnfx("flash")
    cp_me "\"{i}Mmmmh{/i}— mmf— {i}MMMH{/i}—!\""
    "He comes a second later, grunting, holding you down on it. {i}Glk. Glk. Glk.{/i} It's on your lips and your tongue and running down your chin, and you're still gulping."
    "He wipes himself off on your cheek, slow, like he's signing it."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    "\"No.\" He tugs. \"{i}No{/i}— it's not—\" Your voice cracks."
    cp_me "\"...Okay! It was good! Okay?! Let {i}go{/i}!\""
    return

## Rung 2: the chest and the cock together; you can't tell which.
label cp_loss_r2:
    "His other hand shoves up under your T-shirt and finds them. The new ones. Small, heavy, hot."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Look at these. Pink's growing.\""
    cp_me "\"Get your hand OFF— they're not— I'm not into {i}guys{/i}—\""
    call cp_loss_fight
    show cg cp_loss_r2_hand onlayer cgl
    vn_sfx "Shlk. Shlk."
    "He makes you stroke him. Your hands round his cock under his big one, fast and tight, slick and squelching, while his other hand kneads your new tits like dough."
    cp_me "\"Stop— stop it— {i}hah{/i}— why is it {i}good{/i}—\""
    "You can't tell where it's coming from. His thumb on your nipple. His cock in your fists. Your own cock straining your fly. All of it, one hot knot."
    cp_me "\"That's not— that's the {i}suit{/i}— {i}ahh{/i}—\""
    "The suit's been gone for a minute. You both know it."
    show cg cp_loss_r2_cum onlayer cgl
    "He pinches. Hard. And you come, both ends at once, cock jerking in your jeans and your nipples throbbing in his fingers, yelling it at the pavement." with vnfx("flash")
    cp_me "\"Okay— {i}okay{/i}— it's good— it's good, it's GOOD, just— {i}ahh{/i}—!\""
    "Your hands are still flying on him. He swells in your grip and goes off all over you. Your hands. Your face. Your open mouth. Rope after rope."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    cp_me "\"...It was good. Don't— don't tell Red.\""
    return

## Rung 3: the chest alone. The cock barely stirs.
label cp_loss_r3:
    "He hauls your T-shirt up to your collarbones. They spill out. Round now, and full, nipples dark and puffy, and the other two Bogons stop whistling to look."
    cp_me "\"Don't— {i}don't{/i} look at them— get OFF me—\""
    "He squeezes one like he's checking it's real."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Not a dude any more, Pink.\""
    call cp_loss_fight
    show cg cp_loss_r3_mouth onlayer cgl
    vn_sfx "Glk. Glk. Hlk."
    "He fucks your mouth like he owns it, fist in your hair, and the whole time his thumb rolls your nipple. Round. Round. Round."
    cp_me "\"Mmf— {i}nnh{/i}— mmmf—!\""
    "Your cock doesn't even get hard. It just lies there in your jeans. All of it's in your chest. All of it."
    cp_me "\"Why is it— {i}hmmf{/i}— it's only my {i}tits{/i}—\""
    show cg cp_loss_r3_cum onlayer cgl
    "And you come from them. Just from them. A hot crashing wave from under his thumb, and you moan round his cock so loud the street hears it." with vnfx("flash")
    cp_me "\"{i}MMMMH{/i}— mmf— {i}MMH{/i}—!\""
    "He comes down your throat, holding you there, and pulls out to paint the last of it across your tits."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    cp_me "\"I don't— I—\""
    "He waits."
    cp_me "\"I like it.\" It comes out tiny. Then louder, because he's still waiting. \"I like it. I like his cock. I {i}like{/i} it. Now get {i}off{/i} me.\""
    return

## Rung 4: hands-free, in public. The street watches.
label cp_loss_r4:
    "His other hand shoves up under your top and grabs a tit. Squeezes."
    cp_me "\"Ahh— {i}don't{/i}— get your hand off— I don't like guys—\""
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Don't need to.\""
    "He pinches your nipple and your whole body jolts. People are coming out of the shops. Phones up. Grown men in work jackets, a woman with a dog, all of them stopping."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Look at you. Audience, Pink.\""
    "He slaps his cock against your cheek. {i}Thwap.{/i}"
    call cp_loss_fight
    show cg cp_loss_r4_mouth onlayer cgl
    vn_sfx "Glk. Glk. Glk."
    "He takes your mouth in the middle of the street. Slow and deep and then fast, and every phone on the pavement has you."
    cp_me "\"Mmf— nnf— {i}don't film{/i}— {i}mmf{/i}—\""
    "Nobody's touching you anywhere but your mouth. It doesn't matter. The heat comes up from under your top like it's been waiting for an audience."
    cp_me "\"Why is it— they're {i}watching{/i}— {i}hmmh{/i}—\""
    show cg cp_loss_r4_cum onlayer cgl
    "You come. Hands-free. On your knees in the street with a Bogon's cock in your mouth, shaking, in front of all of them." with vnfx("flash")
    cp_me "\"{i}MMMMH{/i}— mmh— {i}mmmh{/i}—!\""
    "He holds your head down while he finishes. Somebody on the pavement actually claps."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    cp_me "\"I like it. I like his cock. I {i}like{/i} it.\""
    cp_me "\"...Now get {i}off{/i} me.\""
    return

## Rung 5: the ass, untouched, on his cock. The lamp post.
label cp_loss_r5:
    show cg cp_loss_r5_post onlayer cgl
    "He hauls you up by the hair and spins you round and shoves you against a lamp post, ass out. His cock slides hot and heavy up the crack of your ass through your clothes."
    cp_me "\"Hhh— {i}ahh{/i}— no— get off— I'm Red's— I'm—\""
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Red's not here.\""
    "He grinds. Your hips jerk back on it and you hate them for it."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"This what you stopped fighting for?\""
    call cp_loss_fight
    "He yanks your jeans down over the big round ass the Grid's been building. The cold air hits it. Then he does."
    show cg cp_loss_r5_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    cp_me "\"Not— NOT there— get it out— I'm not into— {i}hnngh{/i}—!\""
    "It doesn't hurt. That's the worst part. It's big and slick and stretching and it slides in like you were made for it."
    vn_sfx "Pap. Pap. Pap."
    "He drills you against the lamp post, every thrust knocking a squeal out of you, and the others whistle from the kerb."
    cp_me "\"I'm not pushing back— I'm NOT— {i}ahh{/i}— why am I— {i}hah{/i}—\""
    "Your tiny cock just hangs there. Nobody touches it. Nobody needs to."
    show cg cp_loss_r5_cum onlayer cgl
    "It comes up from where he is, from somewhere deep, and you come untouched, screaming at the lamp post." with vnfx("flash")
    cp_me "\"I hate it— I {i}hate{/i} it— {i}nnngh{/i}— more— {i}more{/i}—!\""
    "He comes grunting in your ear, hips mashed to your ass, pulse after hot heavy pulse. You feel every throb. You moan with every one."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    cp_me "\"I like cock.\" Through your teeth. \"I like it. Happy? Don't— don't tell Red.\""
    return

## Rung 6: nearly finished; still no cunt (it comes overnight after the last Leviathan).
label cp_loss_r6:
    show cg cp_loss_r6_post onlayer cgl
    "He drags you up by the hair and bends you over the harbour railing. Your huge soft tits squash on the cold metal. Your ass is out, fat and round, trembling."
    cp_me "\"No— not again— I'm Red's— I'm {i}hers{/i}—\""
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Red's in the water. You're up here.\""
    call cp_loss_fight
    "He doesn't bother with your mouth first. He just spreads your cheeks with his thumbs."
    show cg cp_loss_r6_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    cp_me "\"Get OUT— {i}ahh{/i}— get it OUT— somebody— {i}RED{/i}—!\""
    "Red's three streets away and up to her waist in the harbour."
    vn_sfx "Pap. Pap. Pap."
    "He fucks you slow over the railing, and every stroke your whole body rolls, tits to ass to thighs, and under your tiny half-sunk cock the skin's gone soft and puffy and hot, and every stroke presses it."
    cp_me "\"Stop— stop, I'm not— {i}hah{/i}— why is it {i}good{/i}— why's it good THERE—\""
    show cg cp_loss_r6_cum onlayer cgl
    "You come so hard your knees go. He holds you up by the hips and keeps going through it, and you keep coming, loud, over the water." with vnfx("flash")
    cp_me "\"Don't tell Red— don't tell Red— {i}mmh{/i}— don't stop—\""
    "He finishes deep and pulls out and lets you slide down the railing onto the wet boards."
    hide cp_red
    show cp_bogon neutral at vn_cast_slot
    cp_bogon "\"Say it.\""
    cp_me "\"I like cock. I like it. I like sucking it.\" You can't look at him. \"...Happy?\""
    return

## ==== RUNG 1 ====================================================================================

label cp_clash_zard:
    if cp.read == 1:
        show cg cp_zard_kick onlayer cgl
        "You charge. The suit knows how even if you don't. Your hips pivot, your leg whips round, and your heel cracks across its jaw. Your tits bounce so hard you moan."
        cp_me "\"Oh— {i}oh{/i}, fuck—\""
        "You hit it again. And again. Every kick, the suit drags tight between your legs, slick against that new wet nothing."
        cp_me "\"Nnh—!\""
        "The Bog-Zard goes over backwards into the fountain and bursts. Confetti. Greasy smoke." with vnfx("shake")
    elif cp.read == 2:
        show cg cp_zard_shout onlayer cgl
        cp_me "\"HEY! UGLY!\""
        "It comes out high and squeaky. A girl's voice. The Bog-Zard stops chewing the bandstand and tilts its huge head, baffled."
        "While it's working that out, there's a bow in your hands. Pink energy, humming. Your hips set themselves."
        "Your left tit squashes up against the string and the suit grinds right over the nipple."
        cp_me "\"Ahh— {i}hhn{/i}—\""
        "You let go. The arrow punches through its open mouth and it bursts. Confetti. Greasy smoke." with vnfx("shake")
    else:
        show cg cp_zard_bow onlayer cgl
        "The bow's in your hands before you've thought about it. Pink energy, humming against your fingers."
        "Your hips set. Your back arches. Your left tit presses into the string and the suit grinds tight over your nipple, and a hot spark shoots straight down between your legs."
        cp_me "\"Nnh—!\""
        hide cp_bogon
        show cp_red neutral at vn_cast_slot
        cp_red "\"On my mark, Pink! ...Mark!\""
        "You let go. The arrow hits the Bog-Zard dead centre and it bursts like a balloon full of mud. Confetti. Greasy smoke." with vnfx("shake")
    show cg cp_team_drop onlayer cgl
    "Then four more rangers drop out of the sky around you. Red, Blue, Black, Yellow. Visors all turned your way."
    hide cp_red
    show cp_kyle neutral at vn_cast_slot
    cp_blue "\"Wait. We got a new Pink? And—\""
    "Blue's voice cracks."
    hide cp_red
    show cp_kyle neutral at vn_cast_slot
    cp_blue "\"Wait. They got a {i}dude{/i} for Pink?\""
    hide cp_red
    show cp_mira neutral at vn_cast_slot
    cp_yellow "\"Grid's got a sense of humour. Look at {i}those{/i}.\""
    hide cp_red
    show cp_tobi neutral at vn_cast_slot
    cp_black "\"Think it's defective denim, or bonus perks?\""
    "You wrap your arms round yourself. It does nothing. If anything it shoves them up."
    hide cg onlayer cgl
    show cp_red neutral at vn_cast_slot
    "Red steps in front of the others. Tall. Hands on hips."
    cp_red "\"Pink. Welcome to the team.\""
    "Her visor tips down your body and back up, slow."
    cp_red "\"We didn't get your name.\""
    "You open your mouth to say your name. What comes out, high and small, is:"
    cp_me "\"Um. Lily?\""
    cp_red "\"Lily it is.\""
    "A shimmering portal pops open in the alley like a disco ball. Zorp's in the middle of it."
    hide cp_red
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Excellent work! Return to base, rangers!\""
    return

label cp_stays_zard:
    show cg cp_stays_zard onlayer cgl
    "For a second nothing happens. Then a big cold rush, and your body pulls back in. The tits go. The hips go."
    "The wet heat between your legs folds back into your cock, and your cock feels... small. Ordinary. Disappointing, somehow."
    "You lick your dry lips and it zings right down your spine."
    cp_me "\"{i}Hah{/i}—\""
    "Your nipples zing back."
    hide cg onlayer cgl
    "You're on the floor of a white room full of consoles. Five rangers are taking their helmets off around you."
    show cg cp_anya_helmet onlayer cgl
    "Red's is last. A red braid drops out of it, thick, down to her shoulder blades. She's tall, older than you, all shoulders, with a mouth that looks like it's laughing at something."
    hide cg onlayer cgl
    show cp_anya smirk at vn_cast_slot
    cp_anya "\"Anya. Enjoyed your first day, Pink?\""
    "She offers you a hand up."
    cp_me "\"No.\""
    cp_anya "\"It gets weirder.\""
    "She doesn't let go of your hand straight away."
    show cp_zorp grin at vn_cast_slot
    cp_zorp "\"Side effects for nonstandard hosts are to be expected, and will in all likelihood persist!\""
    "Everyone very carefully doesn't look at your chest."
    return

label cp_clash_monkey:
    if cp.right:
        show cg cp_monkey_high onlayer cgl
        "You go up the market scaffolding before it does. The suit throws you up the poles like you weigh nothing."
        "The Bog-Monkey drops onto the spot where you were standing. Nothing there. It looks up. You're right above it."
        "You drop. Thighs-first. Your new thighs clamp round its sticky neck and the suit rides right up between your legs, tight, slick, and you {i}moan{/i}—"
        cp_me "\"Ahh— {i}nnh{/i}—!\""
        "—and put the bow against its skull and let go."
        vn_sfx "Splat." with vnfx("shake")
        hide cp_anya
        hide cp_bogon
        hide cp_kyle
        hide cp_mira
        hide cp_tobi
        hide cp_zorp
        show cp_red neutral at vn_cast_slot
        cp_red "\"Clean.\""
        "A pause."
        hide cp_anya
        hide cp_bogon
        hide cp_kyle
        hide cp_mira
        hide cp_tobi
        hide cp_zorp
        show cp_red neutral at vn_cast_slot
        cp_red "\"Loud. But clean.\""
    else:
        show cg cp_monkey_drop onlayer cgl
        "It drops on you."
        "Right on your chest. Sticky, heavy, stinking of bog. Its sticky hands land on your tits and it {i}squeezes{/i}, curious, like it's never seen a pair before."
        cp_me "\"Hey— hey, {i}no{/i}— ahh— get {i}off{/i}—!\""
        "It squeezes again. Your nipples throb through the suit. The noise you make goes out on every channel."
        hide cp_anya
        hide cp_bogon
        hide cp_kyle
        hide cp_mira
        hide cp_tobi
        hide cp_zorp
        show cp_red neutral at vn_cast_slot
        cp_red "\"Pink! MOVE!\""
        "You don't. You can't. Red takes it off you with one swing of her sword, and Black and Blue finish it on the pavement while you lie there panting, both arms over your chest."
        show cp_red neutral at vn_cast_slot
        "Red stands over you. Her visor tips down."
        cp_red "\"You good?\""
        cp_me "\"...Yeah.\""
        "It's a squeak."
    return

label cp_stays_monkey:
    show cg cp_stays_monkey onlayer cgl
    "{color=#ff9ecb}Your chest doesn't go back flat.{/color}"
    "You notice when your T-shirt drags across it. {i}Zzt.{/i} A spark straight down to your balls. You look down."
    "Two puffy nipples, darker than they should be, poking through the cotton like you're cold."
    "You're not cold."
    "You pinch one through the cotton. Just to check."
    cp_me "\"{i}Hhn{/i}—!\"" with vnfx("shake")
    "Your knees knock. It's like a wire runs from the nipple straight to your cock."
    cp_me "\"Okay. Okay. Not doing that again.\""
    "You do it again."
    cp_me "\"{i}Ahh{/i}—\""
    "You flex your hands. The fingers are longer. Thinner. Less knuckle."
    hide cg onlayer cgl
    show cp_kyle neutral at vn_cast_slot
    cp_kyle "\"Yo, Pink!\""
    "Blue, the one called Kyle, freckled and grinning, winks."
    "When you pull your hoodie off over your head, the T-shirt rides up over your nipples, and a noise comes out of you. High. Breathy. The whole room hears it."
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Um. Defective uniform? It's chafing. Chafing's a thing.\""
    "Black, the one called Tobi, into the silence."
    show cp_zorp grin at vn_cast_slot
    cp_zorp "\"Pink Ranger! Your Welcome Edition audit is ready!\""
    return

## ==== RUNG 2 ====================================================================================

label cp_clash_shardwing:
    if cp.part == 0:
        if cp.right:
            show cg cp_shard_herd onlayer cgl
            "You don't break it. You herd it."
            "Arms wide, chest out, driving the glass needles back down the riverside into the old fountain basin. Every sweep of your arms grinds the plates across your nipples."
            "Every sweep."
            cp_me "\"Nnh— {i}ahh{/i}— get {i}in{/i} there—\""
            show cp_tobi neutral at vn_cast_slot
            cp_black "\"That's genuinely clever.\""
            "Black, like a man changing his mind about something."
            "The Shardwing is a pile of furious glitter in a stone box. For about a minute."
            vn_sfx "Crack."
            "Then the basin cracks."
        else:
            show cg cp_shard_cloud onlayer cgl
            "You hit it. It shatters. Glitter everywhere." with vnfx("shake")
            "And the glitter {i}moves{/i}. It whips round you in a cloud, a million glass needles scraping the suit, across your tits, across your ass, between your thighs. Not cutting. Just {i}scraping{/i}."
            cp_me "\"Ahh— {i}ahh{/i}— Red— it's everywhere—!\""
            "Red wades into the cloud and drags you out by the arm. Behind you the needles are already knitting themselves back into a bird."
        show cp_red neutral at vn_cast_slot
        cp_red "\"It's coming back together. Demorph. Breathe. Go again.\""
    else:
        if cp.right:
            show cg cp_shard_cover onlayer cgl
            "Second morph. Same afternoon. The suit closes over tits that are still tingling from the first one."
            "You do it again. Arms wide. Chest out. The grinding. The {i}noises{/i}. You drive it into the basin again, and this time Red's waiting with a manhole cover and slams it down on top."
            vn_sfx "Clang." with vnfx("shake")
            "It stays down."
            show cp_tobi neutral at vn_cast_slot
            cp_black "\"Second time's still clever.\""
        else:
            show cg cp_shard_railing onlayer cgl
            "Second morph. Same afternoon. It's bigger now, angrier. It slams you into the riverside railings and pins you there, glass needles pressing your tits flat against the metal." with vnfx("shake")
            cp_me "\"Nnh— hhh— can't— {i}move{/i}—\""
            "Red's sword comes down through it. Blue and Black sweep up the pieces into a bin, and Yellow sits on the lid."
    return

label cp_stays_shardwing:
    if cp.part == 0:
        show cg cp_stays_buds onlayer cgl
        "Your chest is tingling. You pull your T-shirt out and look down."
        "{color=#ff9ecb}Buds.{/color} Two puffy little swells under the nipples, sensitive and hot. Not muscle. Not anything a man has."
        "You press one with two fingers. It's soft. It gives. It {i}throbs{/i}, sweet and hot, right down to your balls."
        cp_me "\"Nnh— {i}oh{/i}— oh, that's—\""
        "You press again. Harder. Your mouth falls open."
        cp_me "\"{i}Ahh{/i}—\""
        cp_me "\"It's fine. It's swelling. From the glass.\""
        "You tell nobody. You bite your lip to keep quiet. It's worse. Your lips are as bad as your nipples now."
        cp_me "\"{i}Mmnh{/i}—\""
        hide cg onlayer cgl
        "Zorp logs it without comment, which is somehow worse."
    else:
        show cg cp_stays_breasts onlayer cgl
        "You look down. You keep looking down."
        "{color=#ff9ecb}Breasts.{/color} Small. Heavy. {i}Real.{/i} They sit up under your T-shirt on their own and wobble when you breathe, nipples puffy and dark."
        "You walk home. Every step, the cotton drags across them. Every step, a spark. By the time you get your key in the door you're half hard and shaking."
        "You cup them. Just to check. Your own hands. Your knees nearly go."
        cp_me "\"Oh {i}fuck{/i}— they're {i}real{/i}— they're so {i}soft{/i}—\""
        "You squeeze. They squish up between your fingers, warm and heavy, and your cock throbs in your jeans."
        cp_me "\"{i}Hhnn{/i}— I've got {i}tits{/i}—\""
        "You make yourself stop. That's worse."
        hide cg onlayer cgl
        $ vn_enter(bg="cp_hub", pc="nervous", pc_tag="cp_pc", cast=[("cp_kyle", "neutral")])
        "Next morning at the Hub, Kyle squints at you."
        cp_kyle "\"You been working out or something?\""
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"It's the glass. Refraction. It makes everything look bigger. It's the light.\""
        "Total confidence. He's already writing your name at the top of a betting sheet."
        show cp_mira neutral at vn_cast_slot
        "Mira takes the pen off him and writes {i}B{/i} beside it."
    return

label cp_clash_ironjaw:
    if cp.right:
        show cg cp_iron_splits onlayer cgl
        "The front's a wall. The joints aren't."
        "It swings. You drop. All the way down, the splits, right under its arm. Your new hips just {i}go{/i}, easy, and your crotch hits the tarmac through the suit with a slick grinding drag."
        cp_me "\"Ah—!\""
        "Up. Knee. You put the bow through the joint behind its knee and it folds. The rest is bookkeeping." with vnfx("shake")
        hide cp_kyle
        hide cp_mira
        hide cp_tobi
        show cp_red neutral at vn_cast_slot
        cp_red "\"Nice splits.\""
        "You can hear her grinning."
    else:
        show cg cp_iron_jaw onlayer cgl
        "You hit the front. It's like punching a fridge."
        "It grabs your face. Chrome fingers round your jaw, squeezing. It lifts you off your feet and drags you in against its chest, your tits squashed flat on the cold plate, your legs kicking."
        cp_me "\"Mmf— {i}nnh{/i}— let— go—\""
        "It squeezes your jaw harder, like it's trying to change the shape of it."
        "Red takes its arm off at the elbow. You drop. Black and Blue bring the rest of it down on top of a parked tram." with vnfx("shake")
    return

label cp_stays_ironjaw:
    show cg cp_stays_ironjaw onlayer cgl
    "In the locker mirror, your face is wrong."
    "Softer at the jaw. The stubble you forgot to shave this morning is just... gone. Your lips are fuller."
    "Your collarbones stand out delicate under your T-shirt, and below them your chest sits round and full, and below {i}that{/i} your waist dips in where it never did."
    "You grab your waist. Your fingers nearly meet."
    "You slide your hands down and your hips flare out under them, and your jeans are snug across a butt that wasn't there this morning."
    "You bite your lip. It's soft. Plump. You bite it again and a little noise slips out."
    cp_me "\"{i}Mmh{/i}—\""
    cp_me "\"Shit. Shit, shit, shit.\""
    "It comes out a step higher than it should. Your fringe flops in your eyes, longer than you buzzed it."
    hide cg onlayer cgl
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Armour padding. The suit pads Pink. It's a pink thing. Washes out.\""
    "He's announcing it from the bench, pulling off his boots."
    show cp_anya neutral at vn_cast_slot
    "Behind him Anya says nothing. She looks at your chest for a long second. Then she looks at your face, like she's measuring something."
    return

## ==== RUNG 3 ====================================================================================

label cp_clash_widow:
    if cp.part == 0:
        if cp.right:
            show cg cp_widow_lines onlayer cgl
            "You go for the anchor lines first."
            vn_sfx "Snap. Snap."
            "The web sags."
            "It lunges anyway. Gets a hand round your waist on the way down. Squeezes. Hips first, like it's weighing you."
            cp_me "\"Hhh—!\""
            "You put an arrow through it from point-blank. It drops into the freight yard with nothing left to hang you from." with vnfx("shake")
            "You feel that hand on your hips for a long time after."
        else:
            show cg cp_widow_haul onlayer cgl
            "It grabs you by the waist and {i}hauls{/i}."
            "Up. Through the air. Swinging between the cranes on a line of web with its fist locked round your hips."
            "Every swing, its grip grinds the suit tight into your ass and between your legs."
            cp_me "\"Ahh— {i}ahh{/i}— put me {i}down{/i}— nnh—\""
            "You're wet. You're so wet inside the suit. It just keeps swinging you."
            "Red cuts the line and catches you on the way down. She doesn't put you down for a second too long."
        hide cp_anya
        hide cp_red
        hide cp_tobi
        show cp_mira neutral at vn_cast_slot
        cp_yellow "\"There's another one. Behind the containers. Demorph and go again.\""
    else:
        if cp.right:
            show cg cp_widow_grind onlayer cgl
            "Second Widow. Same trick. You're quicker this time."
            vn_sfx "Snap, snap, snap."
            "It still gets you by the hips on the last swing. Of course it does. It pulls you in against it, hips to hips, and grinds once before you shoot it."
            cp_me "\"Ahh—! You— {i}prick{/i}—\""
        else:
            show cg cp_widow_upside onlayer cgl
            "The second Widow webs your thighs together and hangs you upside down from a crane. Hips in the air. Ass up."
            "It turns you slowly, like it's showing you off to the whole freight yard."
            cp_me "\"Don't— {i}don't{/i} look—!\""
            "Everyone looks. Red cuts you down, and Black and Yellow finish it in the containers."
    return

label cp_stays_widow:
    if cp.part == 0:
        show cg cp_stays_hips onlayer cgl
        "{color=#ff9ecb}Your hips are wider.{/color} Not a bit. A size."
        "Right where it held you. Your jeans are suddenly tight at the hips and loose at the waist, and when you walk, something back there {i}sways{/i}."
        "You reach back. Grab. A double handful of round soft ass, spilling out of your palms."
        cp_me "\"{i}Ohh{/i}— what— {i}ahh{/i}—\""
        "You squeeze. A hot little throb answers, right between the cheeks."
        cp_me "\"That's {i}mine{/i}?\""
        "You squeeze again. You can't stop. Your cock's pushing at your fly."
        "Your mouth's watering. Your nipples are rock hard in your shirt. Nobody's touching any of it."
        cp_me "\"{i}Ahh{/i}— why's {i}everything{/i}—\""
        hide cg onlayer cgl
        "You've got a few minutes before you have to morph again."
    else:
        show cg cp_stays_jeans onlayer cgl
        "That evening you swing off your bike outside the Park, in front of the whole team, and your last pair of jeans splits right up the back."
        vn_sfx "Rrrrip." with vnfx("shake")
        "Your ass is out. Round and pale and {i}big{/i}, and the pink lace waistband of the panties from Anya's bag sitting right on top of it."
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"{i}Structural denim failure!{/i}\""
        "Tobi howls. Kyle looks away so fast he walks into a lamp post. Mira writes something in her book."
        show cg cp_stays_jacket onlayer cgl
        "Anya pulls off her jacket and ties it round your waist. She knots it hard. Her thumb presses into your new hip like a stamp."
        hide cg onlayer cgl
        $ vn_enter(bg="cp_flat", pc="flushed", pc_tag="cp_pc", cg="cp_stays_mirror_ass")
        "Later, at home, the mirror gives you a silhouette that reads {i}girl{/i} from every angle. Thighs that touch all the way up. An ass so round it sticks out past your hips."
        "You twist to look over your shoulder. You smack it, once, just to see."
        vn_sfx "Smack."
        "It {i}jiggles{/i}. It keeps jiggling."
        cp_me "\"{i}Hhn{/i}—! Oh my {i}god{/i}—\""
        "You grind your palm against yourself through the panties, and you're hard almost at once, and you hate how fast that was."
    return

label cp_clash_siren:
    if cp.right:
        show cg cp_siren_sing onlayer cgl
        "So you sing."
        "You open your mouth and the frequency comes out of you, high and pure, and the Siren's hum comes back down the tower and straight through your chestplate."
        "Into your tits."
        vn_sfx "Mmmmmmmm."
        "A buzz with nowhere to go, right in your nipples, on and on."
        "You keep singing. You have to. Your voice holds the note because the suit holds it for you. Your thighs are pressed together so tight they shake."
        "One moan gets out mid-note. On open comms."
        show cp_tobi neutral at vn_cast_slot
        cp_black "\"Pink? You hit?\""
        cp_me "\"Nnh— {i}no{/i}— keep— singing—\""
        "The tower goes quiet. The Siren drops off the top like a dead bird. The whole city, listening on every open channel, has just heard a girl's voice save it." with vnfx("flash")
    else:
        show cg cp_siren_knees onlayer cgl
        "You cover your ears and charge the tower."
        "It doesn't matter. The stolen voices get in anyway. Every one of them is saying your name. Every one of them is a girl."
        "Then it hums. Low. Right at you."
        vn_sfx "Mmm. Mmm. Mmm."
        "Your knees buckle and your nipples throb in time with it, and you're on the stairs on your knees, moaning into the comm."
        cp_me "\"Ahh— it— it's in my— {i}ahh{/i}—\""
        "Yellow cuts the tower's power. Red goes up the outside of it and drags the Siren off the top by its throat." with vnfx("shake")
    return

label cp_stays_siren:
    show cg cp_stays_voice onlayer cgl
    cp_me "\"Oh, come on.\""
    "On the Hub floor. And stop. And say it again."
    cp_me "\"Come on. Come {i}on{/i}.\""
    "It's not a step up this time. It's a whole register. A girl's voice. It doesn't come back down."
    "Your hands are finished, too. Slim fingers, tapered. Your nails are glossy, like they've been done, and they haven't."
    "And your chest. Heavier. Rounder. It sits up full under your T-shirt and bounces when you stamp your foot."
    cp_me "\"Come {i}on{/i}—\""
    "You grab them, both hands. It turns into a moan halfway, in the girl's voice."
    cp_me "\"{i}Mmmh{/i}—\""
    hide cg onlayer cgl
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Vocal warfare technique! Pink's got {i}range{/i}!\""
    "Both finger-guns, pointed at you."
    $ vn_enter(bg="cp_flat", pc="flushed", pc_tag="cp_pc", cg="cp_stays_siren_night")
    "At home you try to jerk off, just to prove something. Your cock barely stirs. It's smaller in your hand than it was. Shorter. Softer."
    "It takes forever, and your other hand keeps sneaking up to your nipples, and the second it gets there your cock finally jumps."
    cp_me "\"No— not like— {i}ahh{/i}—\""
    "Your nipples are aching for that hum to come back."
    return

## ==== RUNG 4: Bramblemaw, the rung's act -- the bind, then the vines ===========================

## The bind plays BEFORE the read: the vines have you whatever you pick. Nothing enters the suit.
label cp_bramble_bind:
    show cg cp_bramble_bind onlayer cgl
    "You don't get to pick. The vines pick."
    vn_sfx "Shhk-shhk-shhk."
    "They come up out of the flowerbeds all at once. Round your ankles. Your wrists. Your waist. They haul you off your feet and pin you spread in the air like a starfish."
    "Then they tighten. Across your chest."
    "The plate grinds. Down. Up. Down. Right over your nipples, slow and heavy, like it's {i}looking{/i} for them."
    cp_me "\"Nnh— no— not— {i}not there{/i}—\""
    "It finds them. It keeps grinding."
    cp_me "\"Ahh— {i}ahh{/i}— Red— Red, it's— I can't—\""
    "Your cock isn't even there. Nothing's touching you anywhere but your tits."
    "Doesn't matter. The heat comes up from under the plate like a wave and you can't stop it and you can't hide it and your comm is {i}open{/i}—"
    show cg cp_bramble_ffah onlayer cgl
    cp_me "\"FFAAAAAH—!\"" with vnfx("shake", "flash")
    "You come. Hands-free. Strung up in a park. Shaking in the vines, tits throbbing, on every channel in the city."
    "Silence on comms."
    show cp_tobi neutral at vn_cast_slot
    cp_black "\"Pink with the audio crowd control!\""
    "Tobi, delighted."
    show cp_red neutral at vn_cast_slot
    cp_red "\"We'll talk.\""
    "Just that."
    "You're still hanging there. Still twitching. You have to get out of this."
    return

## The read, morphed. Whichever you pick, the suit lets go: it only holds a host who's fighting.
## "Stop fighting it" comes here too (owner, 2026-11-08): the fight runs out of you, never a yes.
label cp_clash_bramblemaw:
    if cp.lost:
        "You stop fighting it."
        "Not because you want this. You don't. The plate's been grinding your tits for so long that your body's gone over without you, and the fight just runs out."
        "Your arms go slack in the vines. Your legs stop kicking."
        cp_me "\"No— I didn't— I didn't mean {i}stop{/i} stop— Red— {i}RED{/i}—\""
        show cp_red neutral at vn_cast_slot
        cp_red "\"Pink? Pink, talk to me.\""
    elif cp.right:
        show cg cp_bramble_root onlayer cgl
        "You wrench one arm free. The bow comes. You don't aim at the vines. You aim down, through the flowerbed, at the fat black root in the soil."
        vn_sfx "Thwip."
        "The whole Bramblemaw shudders. It's hit. It's dying. It's just taking its time about it, and it doesn't let go of you while it does."
        "It squeezes. Across your chest. Again."
        cp_me "\"No— no, I {i}got{/i} it, I got the root, you're supposed to let {i}go{/i}— {i}hnngh{/i}—\""
    elif cp.read == 1:
        "You saw at the creepers with the edge of the bow. Every one you cut, two more wrap your chest and grind."
        cp_me "\"Ah— {i}ah{/i}— again— no— not again—\""
        "You're cutting slower. Then you're not cutting at all. You're just hanging there, panting, with the bow dangling off your wrist."
    else:
        "You hang on. You grit your teeth and hang there over the roses and wait for Red."
        cp_me "\"Red— Red, any time now— {i}hnngh{/i}— any {i}time{/i}—\""
        "The vines grind. You just take it. Hanging on isn't fighting."
    "And the suit only holds a host who's fighting."
    show cg cp_bramble_flicker onlayer cgl
    "It flickers. Pink light crawls over your skin like static, and the chestplate goes thin as paper under the vines."
    cp_me "\"No— no no no, not {i}now{/i}— not {i}here{/i}—\""
    menu:
        "The suit lets go":
            pass
    jump cp_bramble_drop

## The suit lets go: the vines play in your own body, the cock still on. They strip you and take
## their seats -- the wrists, the waist, round your tits, the nipples, round your cock, your arse.
label cp_bramble_drop:
    $ cp_morph(False)
    $ cp_body(4)
    $ cp.vines = True
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_gardens", pc="shocked", pc_tag="cp_pc", cg="cp_bramble_drop")
    "Light. Then no light."
    "The armour's gone. You're still up there, wrists and ankles and waist, strung out over the roses."
    "But it's your own T-shirt now. Your own jeans. Your own body: the tits the Grid keeps leaving you, the hips, the thighs, and your cock, soft in your jeans."
    "On your wrist, the morpher's comm light is still on. Every channel."
    "The vines go still. They've noticed."
    if cp.lost:
        "They noticed the fight go out of you before you did. Your body's already halfway over the edge, shaking, nipples aching, and you're still saying no out loud on every channel."
    "Then they all move at once."
    show cg cp_bramble_strip onlayer cgl
    vn_sfx "Rrrip." with vnfx("shake")
    "Your T-shirt goes up over your head and away."
    "Your jeans and boxers get dragged down your thighs and off over your boots, and you're hanging there naked in the botanical gardens with the sun on your tits."
    cp_me "\"Hey— HEY— those are my {i}clothes{/i}— put me DOWN—\""
    show cg cp_bramble_seats onlayer cgl
    "A thick vine coils round your tits and squeezes them together. Two thin ones find your nipples and curl round them, slow, warm with sap."
    cp_me "\"{i}Ahh{/i}— don't— don't you {i}dare{/i}— {i}ahh{/i}—\""
    "One winds up between your thighs and wraps round your cock. All of it. Wet and warm and squeezing."
    cp_me "\"Let GO of that— that's {i}mine{/i}— {i}hnngh{/i}—\""
    "And one slides up between your cheeks, slick with sap, and presses right against your hole. A push away from in."
    cp_me "\"No. No no no. Red— {i}RED{/i}— it's going to go {i}in{/i}—\""
    menu:
        "The vines go in":
            pass
    jump cp_bramble_vines

## The vines (non-con, never a flip): your voice protest, then betray, then break; one line a beat
## from the comm or the gardens. Your ass goes to the vines first, quietly. On "Stop fighting it"
## the break arrives early: the voice is past protest from the start.
label cp_bramble_vines:
    show cg cp_vines_in onlayer cgl
    vn_sfx "Shlrrk." with vnfx("shake")
    "It goes in."
    "Slow. Slick with sap. Thick as two fingers and then thicker, and it doesn't hurt, it just {i}fills{/i}, deeper than anything's ever been, and keeps going."
    if cp.lost:
        cp_me "\"Why is it— why's it {i}good{/i}— it's a PLANT— {i}ahh{/i}— it's a stupid {i}PLANT{/i}—!\""
    else:
        cp_me "\"Get OUT— get it OUT of my— RED— it's in my {i}ASS{/i}—!\""
    "Static in your ear. Then Mira, very carefully."
    show cp_mira neutral at vn_cast_slot
    cp_yellow "\"Pink, your vitals are— oh. Oh. Okay.\""
    show cg cp_vines_milk onlayer cgl
    vn_sfx "Shlk. Shlk. Shlk."
    "The vine round your cock starts to move. Squeezing up. Squeezing down. Milking. The two on your nipples tighten and {i}pull{/i}, little sucking tugs, warm with sap."
    if cp.lost:
        cp_me "\"Stop sucking on— {i}hahh{/i}— stop making my nipples— {i}AHH{/i}— stop it—!\""
    else:
        cp_me "\"Don't you DARE wrap round my— {i}ahh{/i}— it's wrapping round it— LET GO of it—!\""
        "You kick at nothing. The vine in you just keeps going."
        cp_me "\"Let GO— let go let go {i}let GO{/i}—!\""
    show cp_tobi neutral at vn_cast_slot
    cp_black "\"Is that— is she still—\""
    "Tobi, on the comm, half strangled. Somebody mutes him."
    show cg cp_vines_pump onlayer cgl
    vn_sfx "Shlrk. Shlrk."
    "The one in your ass starts to pump. Slow and deep. Every push presses on something inside you and your cock throbs in the one round it."
    cp_me "\"I'm not pushing back on it— I'm NOT— {i}nnngh{/i}— that's the VINES moving me—!\""
    "Every channel in the city carries it. Somewhere a taxi driver turns his radio up."
    cp_me "\"Don't milk it— don't— {i}ohh{/i}— why's it {i}leaking{/i}— I didn't say it could—\""
    "The whole Bramblemaw creaks round you, slow and pleased, and the roses shiver. Sticky sap beads everywhere the vines grip you, warm and sweet-smelling."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Hold on, Pink. Hold ON.\""
    show cg cp_vines_peak onlayer cgl
    cp_me "\"{i}AHHH{/i}— too much— it's everywhere at {i}ONCE{/i}— {i}AHHH{/i}—!\"" with vnfx("shake")
    cp_me "\"Nnh— {i}NNH{/i}— it's hitting— it keeps HITTING it— {i}AHH{/i}—!\""
    cp_me "\"Red— don't listen— nobody LISTEN— I'm gonna— I'm {i}gonna{/i}— {i}AAAH{/i}—!\""
    show cg cp_vines_cum onlayer cgl
    "It all hits at once. The vine in your ass, pumping slow and deep. The one round your cock, squeezing, milking. The two on your nipples, sucking."
    "The one round your tits, holding them up to the whole sky."
    "No hands. Nobody's even touching you. Just vines."
    cp_me "\"AAAHHH— it's IN me— it's in me and I'm— I'm {i}COMING{/i}— RED, DON'T LISTEN—!\"" with vnfx("shake", "flash")
    "Your cock spurts round the vine. Your ass clenches on the other one, again and again and again, and it just keeps pumping."
    "Strung up in the roses, full of vines, on every channel in the city."
    if cp.right:
        show cg cp_vines_root onlayer cgl
        "Then the root you shot gives out."
        "The whole Bramblemaw shudders and dies, slowly, still wrapped round you. The vines go soft one by one."
        "The one in your ass slides out last, slick and slow, and you moan at how empty it leaves you."
        cp_me "\"Hhn— {i}hhh{/i}—\""
        "You drop into the roses. You lie there. Your tits are still throbbing."
    else:
        show cg cp_vines_burn onlayer cgl
        "Then fire, all along the flowerbed. Red's found the root and burned it."
        "The vines go slack all at once. Everything slides out of you, slick and slow, and you drop."
        "Red's there before you hit the roses. She catches you under the arms, stands you on your feet, and doesn't let go of your arm."
    $ cp.fit = "own"
    "Your clothes are all over the roses. You get them back on somehow."
    "Anya keeps a hand on the small of your back the whole way back to the portal."
    if cp.lost:
        $ cp.surged = True
    return

label cp_stays_bramblemaw:
    show cg cp_stays_bramble onlayer cgl
    if cp.lost or cp.vines:
        "The suit's long gone. The tingle isn't."
    else:
        "The armour goes. Your chest doesn't."
    "It's bigger. Right where the vines ground it. Fuller, rounder, heavier, swollen and hot, and your nipples stand up through your T-shirt like they're still being rubbed."
    "You cup them. They fill your hands now. Fill them and then some. You squeeze, just a little, and they're so swollen and so good your eyes roll back."
    cp_me "\"{i}Ahhh{/i}— oh, fuck, they're {i}bigger{/i}— they're still {i}growing{/i}—\""
    "Your cock is small and quiet in your jeans. It didn't do anything. It wasn't even {i}involved{/i}."
    hide cg onlayer cgl
    show cp_zorp grin at vn_cast_slot
    cp_zorp "\"Involuntary morale spike. Logged!\""
    "It reads it off the console."
    return

label cp_clash_serpent:
    if cp.right:
        show cg cp_serpent_tail onlayer cgl
        "The tail. Always the tail. It can't coil what it can't anchor."
        "You pin it to the lock gate with an arrow. It thrashes. Its coils go slack round nothing. You walk up its length and finish it, tits bouncing every step." with vnfx("shake")
        hide cp_zorp
        show cp_red neutral at vn_cast_slot
        cp_red "\"Clean. Very clean, Pink.\""
    else:
        show cg cp_serpent_coil onlayer cgl
        "You go for the head. It goes for your chest."
        "One coil round your ribs. Then another. Tighter. Every coil squeezes your tits up and out of the plates until they're bulging over the top, nipples straining the suit."
        cp_me "\"Hhh— so— {i}tight{/i}— ahh—\""
        "Tighter."
        cp_me "\"Nnh— {i}nnnh{/i}—!\""
        "Red severs the tail. The coils fall off you like wet rope, and you drop to your knees on the towpath, gasping, holding them." with vnfx("shake")
    return

label cp_stays_serpent:
    $ vn_enter(bg="cp_flatbath", pc="shocked", pc_tag="cp_pc", cg="cp_stays_bra")
    "You go to bed in the bra Anya bought you."
    "You wake up and it's {i}losing{/i}. The band's straining tight round your ribs. The cups are overflowing, spilling, soft flesh bulging over lace it was never sized for."
    "{color=#ff9ecb}An E. At least.{/color}"
    "You unhook it. They drop. {i}Heavy.{/i} They swing and settle and keep wobbling, pink lace-prints fading across the soft undersides."
    "You rub the lace-prints. Your palms slide up, over the nipples—"
    cp_me "\"{i}Nnnh{/i}—\""
    "You're squeezing. You didn't decide to squeeze."
    cp_me "\"Oh god. Oh god, they're so {i}heavy{/i}—\""
    show cg cp_stays_leo onlayer cgl
    "You stand in front of the bathroom mirror with the bra hanging off one arm, breasts heavy and flushed, and say it out loud."
    cp_me "\"I'm still Leo.\""
    "The mirror says it back in a girl's voice."
    hide cg onlayer cgl
    $ vn_enter(bg="cp_hub", pc="nervous", pc_tag="cp_pc", cast=[("cp_tobi", "neutral")])
    "At the Hub, Tobi spots the bra strap straining at your collar."
    cp_tobi "\"Constriction swelling. Snakes do that. Totally temporary.\""
    "He nods wisely."
    return

label cp_clash_lensfang:
    show cg cp_lens_corner onlayer cgl
    "It corners you downtown. A cyborg with a camera lens for a face, and every screen in the city showing what it sees."
    "What it sees is you. It zooms. On your tits. On your ass. On your mouth."
    if cp.right:
        show cg cp_lens_billboard onlayer cgl
        "You go for the lens first. It costs you the left side of your chestplate."
        vn_sfx "Krrrk." with vnfx("shake")
        "The plate tears off, and for a long, long moment every billboard downtown is a close-up of one round pink-suited tit and a nipple poking straight through."
        "And under the burning shame, something hot. A coal. It {i}likes{/i} being looked at. You like it."
        cp_me "\"Ahh—!\""
        "You put your fist through the lens. The screens go black." with vnfx("shake")
    else:
        show cg cp_lens_zoom onlayer cgl
        "You fight it fast. The feed doesn't drop. It gets in close, the lens filling with your face, your parted lips, your eyes. It almost gets under your hair. Almost."
        "And a little hot part of you leans into the zoom. Arches. Gives it a better angle."
        cp_me "\"Nnh— stop {i}looking{/i}—\""
        "Red smashes the lens with the flat of her sword. The screens go to static." with vnfx("shake")
    "By evening there are fan accounts. Frame by frame."
    return

label cp_stays_lensfang:
    $ cp_locker(4)
    show cg cp_stays_news onlayer cgl
    "You shaved your head this morning. Clippers, close, like always."
    "On the evening news your hair is curling past your jaw. Pink. Soft. Before-and-after collages are everywhere by midnight: the girl in pink at noon, the girl in pink at dusk."
    show cg cp_stays_lens onlayer cgl
    "In the Hub mirror your face is rounder. Your nose is smaller. Your lashes are long and dark, like you're wearing mascara, and you aren't."
    "Your jeans won't button. You haul them up and they stop at your hips. Your ass is too big for them now, round and high, and your hips curve out like a cartoon."
    "You shove a hand down the front to fix yourself and freeze. Your cock's shrunk again. A soft little thing you can cup in your palm."
    cp_me "\"{i}Ahh{/i}— no— that's—\""
    "You squeeze. It barely twitches. Your nipples do instead."
    cp_me "\"{i}Hhn{/i}— that's not {i}fair{/i}—\""
    show cg cp_clippers_bin onlayer cgl
    "You take the clippers out of your locker and drop them in the bin."
    vn_sfx "Clunk."
    hide cg onlayer cgl
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Beauty filter. Lensfang runs a filter. Everyone knows that.\""
    "He's scrolling the collages on his phone."
    "That night Mira sends you a folder of links titled {i}unisex basics{/i}. Every single one is women's clothes."
    return

## ==== RUNG 5 ====================================================================================

label cp_clash_magnavore:
    if cp.right:
        show cg cp_magna_plate onlayer cgl
        "You pop the chestplate's catches yourself and let it fly."
        vn_sfx "Klang."
        "It's the right call. It's also the most naked you've ever been in front of the team."
        "Just the suit's thin underlayer, stretched over your tits, barely holding them, every bounce on display."
        "Magnavore drags at every buckle you've got left. You fight soft. Close. Fast."
    else:
        show cg cp_magna_rip onlayer cgl
        "You hold the plate on. Magnavore pulls."
        vn_sfx "KRRANG." with vnfx("shake")
        "It rips the chestplate straight off you. The underlayer splits down the middle."
        "You're fighting with one arm clamped over your tits to hold them in, and they're spilling out over it anyway."
        cp_me "\"Don't— {i}don't look{/i}—!\""
    call cp_magna_belt
    return

## Anya's belt: the whole team gets a long, silent look. (Seen from the pavement on a loss.)
label cp_magna_belt:
    show cg cp_magna_belt onlayer cgl
    "Then it turns on Red."
    "It drags at her belt line. Hard. Her suit pulls taut across her hips, and the whole team gets a long, silent look at what's under there."
    "Thick. {i}Long{/i}. Lying down her thigh. Something her suit stopped being able to hide a while ago."
    "Nobody breathes."
    hide cp_tobi
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Red Ranger, a payload accommodation patch is available. Requisition form seven-C.\""
    "Zorp, unflappable, over comms."
    "Red puts her sword through Magnavore's core so hard it comes out the other side." with vnfx("shake")
    "You can't stop looking. At her belt. At it."
    return

label cp_stays_magnavore:
    if not _was:
        "You saw it from the pavement, before Red got to you. Magnavore turning on her, dragging at her belt line."
        call cp_magna_belt
    show cg cp_stays_magna onlayer cgl
    if _was:
        "The armour goes. Your T-shirt is suddenly too small."
    else:
        "Your T-shirt is suddenly too small."
    "{color=#ff9ecb}Bigger. Right where the plate tore off.{/color} Heavy and soft and spilling over the bra's cups. An F. Your bra is already a lie."
    "You tug your T-shirt out at the neck and look down. Cleavage. Deep, soft, {i}yours{/i}, swelling up out of the cups."
    "You catch them through the cotton and lift. Your fingers sink in."
    cp_me "\"Oh— {i}oh{/i}— they just— they keep— {i}mmh{/i}— why does that feel so {i}good{/i}—\""
    "And your ass clenches on nothing, hot and hungry, and your mouth goes wet thinking about Anya's belt."
    cp_me "\"{i}Hnnh{/i}—!\""
    hide cg onlayer cgl
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Magnets. Magnets make stuff look bigger. That's science.\""
    show cp_anya hungry at vn_cast_slot
    "Nobody's listening to him. Everyone is very carefully not looking at Anya's belt, and Anya is looking straight at you."
    return

label cp_clash_echoplasm:
    # no drawn CG (six passes never drew the copy): the suit sprite and its chrome twin (route.rpy, cp_echo_*)
    hide cp_pc
    show cp_echo_real at vn_pc_slot
    "It's a slick of chrome mirror-slime in the middle of the shopping centre. It touches your hip. It {i}pops{/i}."
    show cp_echo_chrome at vn_cast_slot
    with dissolve
    vn_sfx "Plip."
    "And there's another you."
    "Naked. Bigger. Tits like melons, hips like a cartoon, a pussy pink and glistening, smirking at you with your own face. It moans in your voice. It takes your bow stance."
    "Every phone in the shopping centre comes up. Every grown man and woman in the food court gets a long look."
    hide cp_echo_real
    hide cp_echo_chrome
    if cp.right:
        show cg cp_echo_shake onlayer cgl
        "It knows all your moves. So you do something you've never done."
        "You turn round and {i}shake your ass at it{/i}."
        "It copies. Of course it copies. It bends over, wobbling, moaning {i}\"ahh, look at me—\"{/i}, and loses its footing completely."
    else:
        show cg cp_echo_pin onlayer cgl
        "You out-fight it. You try. It knows every move. It pins you to the fountain, rubbing its huge wet tits on your suited ones, moaning in your ear in your own voice."
        "\"Mmh— {i}you love this{/i}—\""
        cp_me "\"I don't—!\""
        "You squeal it. Your hips are rocking."
    "Red doesn't let it touch her. She knows exactly what it would copy. She incinerates it mid-smirk, and the smirk's on your face, and it's looking at her." with vnfx("flash")
    return

label cp_stays_echoplasm:
    show cg cp_stays_echo onlayer cgl
    "{color=#ff9ecb}Everything lands a shade past the copy.{/color}"
    "A G. Your ass heavy and round, your thighs thick enough to squeak. Your face is finished: soft, pretty, a girl's. Your hair brushes your shoulders."
    "You grab your ass with both hands and it spills over them. You grab your tits and they spill over those too."
    cp_me "\"{i}Ohhh{/i}— oh, {i}fuck{/i}— more— there's so much {i}more{/i}—\""
    "You're squeezing everything. You can't pick."
    cp_me "\"Nnh— {i}ahh{/i}—\""
    "And your cock. You check. It's there. Tiny. Numb. Smaller than this morning. Like a thing someone left in your jeans by mistake."
    hide cg onlayer cgl
    "Everybody agrees the double's already out of date."
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"It was clearly padded. Clearly.\""
    "One beat late, to nobody."
    show cp_kyle neutral at vn_cast_slot
    "Kyle can't meet anyone's eyes."
    return

## ==== RUNG 6: the Leviathan, over two days ======================================================

label cp_clash_leviathan1:
    $ _cday = 1
    jump cp_clash_leviathan

label cp_clash_leviathan2:
    $ _cday = 2
    jump cp_clash_leviathan

label cp_clash_leviathan:
    if _cday == 1 and cp.part == 0:
        show cg cp_levi_rise onlayer cgl
        "The Bog-Leviathan rises out of the harbour like a hill with teeth." with vnfx("shake")
        show cg cp_levi_red onlayer cgl
        "Anya's binding herself for battle now. It barely helps."
        "Morphed, the Red suit rides her like a threat, and when she lands beside you there's a very obvious, very heavy shape down the inside of her thigh."
        hide cp_anya
        hide cp_kyle
        hide cp_tobi
        show cp_zorp neutral at vn_cast_slot
        cp_zorp "\"Red Ranger, please refrain from intimidating junior staff.\""
    if cp.right:
        if cp.part == 0:
            show cg cp_levi_pace onlayer cgl
            "You pace it. You trade ground you can afford for morphs you can't. Duck, dodge, a shot to the eye, back off. Duck, dodge. It takes all afternoon."
            "By the end your tits are throbbing from bouncing and your thighs are slick inside the suit, and it's still there. Wounded. But there."
        elif _cday == 2:
            show cg cp_levi_down onlayer cgl
            "It goes down on the second evening, in the shallows, with the whole roster on it."
            "Red and Blue on its head. Black and Yellow on its legs. Vee and Naomi pouring fire into its belly."
            "And you, standing on its back, drawing one last arrow, the string pressing your tit so hard you moan as you let go."
            vn_sfx "THOOM." with vnfx("shake", "flash")
            "It's over."
        else:
            show cg cp_levi_dusk onlayer cgl
            "Again. You pace it again. Your voice is hoarse from shouting and your nipples are buzzing from the suit and it's dark by the time it sinks back under the water, sulking."
            hide cp_anya
            hide cp_kyle
            hide cp_tobi
            show cp_red neutral at vn_cast_slot
            cp_red "\"Tomorrow. Go home. Eat. Sleep.\""
    else:
        show cg cp_levi_swat onlayer cgl
        "You hit it with everything you've got."
        "It swats you. A tail like a lorry catches you across the chest and flings you into the harbour. You go under, the suit dragging at every curve, and come up gasping." with vnfx("shake")
        cp_me "\"Hhh— {i}ahh{/i}—\""
        show cg cp_levi_fished onlayer cgl
        "Red fishes you out by the back of your suit and holds you against her, both of you soaked."
        hide cp_anya
        hide cp_kyle
        hide cp_tobi
        show cp_red neutral at vn_cast_slot
        cp_red "\"Pace it. I need you in one piece.\""
        "She growls it in your ear."
        if _cday == 2 and cp.part == 1:
            "The rest of the roster finishes it in the shallows, all of them at once, while you hang off Red's arm and watch."
    return

label cp_stays_leviathan1:
    $ _cn = cp.part + 1
    jump cp_stays_leviathan

label cp_stays_leviathan2:
    $ _cn = cp.part + 3
    jump cp_stays_leviathan

label cp_stays_leviathan:
    if _cn == 1:
        show cg cp_stays_levi1 onlayer cgl
        "You put both hands on your chest. They don't cover it. They don't come close. Your tits spill out round your fingers, soft and heavy and hot."
        "{color=#ff9ecb}An H.{/color} You don't need Zorp's pad to tell you."
        "You squeeze, and they swell out between your fingers like dough, and your knees just {i}go{/i}."
        cp_me "\"{i}Ahhh{/i}— oh god— they're {i}huge{/i}— I can't even {i}hold{/i} them—\""
        "You kneel there on the Hub floor, kneading, moaning, while the rest of the team talks very loudly about the weather."
    elif _cn == 2:
        $ vn_enter(bg="cp_flat", pc="grin", pc_tag="cp_pc", cg="cp_stays_levi2")
        "That night you sit down on your kitchen chair and your ass doesn't fit. It hangs off both sides. You laugh, high and giggly, and then you can't stop."
        "You stand up and grab it. Two big soft handfuls, and there's still more spilling past your fingers."
        cp_me "\"{i}Mmmh{/i}— it's so {i}fat{/i}— oh my god, look at it—\""
        "You twist round to see. You bounce on your heels just to watch it jiggle."
        "You sit back down on it, slow. It squishes. You moan out loud in your empty kitchen."
    elif _cn == 3:
        show cg cp_stays_levi3 onlayer cgl
        "Your voice finishes. You can hear it happen, on the Hub floor: a little lift and a little softness, and then it's just a voice. A woman's. Yours."
        "Your face does the same in the mirror. Done."
        "Your hair's longer again. Past your shoulder blades, heavy and pink, swinging when you turn your head."
        cp_me "\"Leo.\""
        "You tell the mirror. It comes out pretty. Breathy. You say it again just to hear it, and your hands are already sliding down over your tits, your waist, your hips. All of it."
        cp_me "\"{i}Mmh{/i}— oh, that's so {i}hot{/i}—\""
    else:
        show cg cp_stays_levi4 onlayer cgl
        "All those morphs, back to back. Your body hums like a struck bell."
        "You check, in the Hub toilets, with the door locked. Your cock is there. Barely. Tiny and numb, half sunk into you. A stranger. The Grid is plainly finishing it."
        "You touch it. Nothing. You touch {i}under{/i} it, where the skin's gone soft and puffy and hot, and your whole body jolts."
        cp_me "\"{i}Ahh{/i}—! Oh— oh, what's— {i}there{/i}—\"" with vnfx("shake")
        "You do it again. Your knees buckle against the door. It's {i}wet{/i} under there."
        hide cg onlayer cgl
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Water weight. From the harbour.\""
        "Tobi, outside the door, to somebody."
    return
