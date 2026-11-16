## scales' director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, then the passage after,
## which lands the climax. Lines from scales.js's pools: setup.scalesLines (Long Qi's, banded early /
## middle / late / final) and .noncon (her taking lines: procedural, never cruel), and
## setup.slPcLines.scales with setup.scalesSaid (the household's protest, betray, break and flip, and
## the speech actions the player picked). Rungs 1-2 non-con, no flip; rungs 3-4 non-con that turn;
## consensual from rung 5 (owner, 2026-10-19/20). A speech menu in each, for flavour, never whether.

## Rung 1's optional round: she isn't finished; she takes your mouth again. Household doesn't
## decline. (rungs.twee :: Scales First Sex; lead Long Qi, oral, inside, noncon, pool scales)
label scl_first_sex:
    $ vn_enter(bg="scl_quarters_night", pc="protesting", pc_tag="scl_pc", cg="scl_first_again")
    "She pushes back in before you've got your breath. Her tail settles across your chest again and pins you flat."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Hold still. Good.\""
    scl_you "\"Lady— I'm here to SERVE— not— {i}mmph{/i}—!\""
    menu:
        "Her tail across your chest. Her cock on your tongue again."
        "Pull off and object":
            scl_you "\"I object— I OBJECT— enter it— enter it and {i}stop{/i}—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Your objection is entered. Breathe out.\""
            "Her hips don't slow."
        "Plead with her":
            scl_you "\"Please— not tonight— can't it go on the docket for— for {i}never{/i}—?\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
            "She says it to every no, and keeps going."
        "Mock her round it":
            scl_you "\"Noted, noted, noted. Is that the whole vocabulary, or do lords get more words?\""
            "She answers by going deeper, and the rest of the joke goes down your throat."
    show cg scl_first_again_mid onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Household does not decline.\""
    "Slow, deep, every ridge in turn. Your jaw aches with the size of her and your tongue keeps working under her anyway."
    scl_you "\"Stop— stop, my body's— why is it— {i}ahh{/i}— {i}ahh{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Breathe. Louder. Noted.\""
    "Under the blanket your small cock is hard again, and leaking, and nothing's touching it."
    show cg scl_first_again_peak onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"You are filed as mine. This is the filing.\""
    scl_you "\"I don't want— I don't— then why am I so {i}hard{/i}— {i}nngh{/i}—\"" with vnfx("shake")
    jump scl_mouth_after

## Rung 2: THE MANDATORY SCENE. The first anal on her pallet, your knees pressed back and held; you
## say no the whole way in. Non-con, no flip. (rungs.twee :: Scales Rung Two Sex; lead Long Qi,
## anal, missionary, lock, inside, noncon, pool scales)
label scl_rung_two_sex:
    $ vn_enter(bg="scl_pallet", pc="protesting", pc_tag="scl_pc", cg="scl_rung_two_open")
    "The head pushes. Your body holds for one long breath, and then it doesn't, and she's in you, the first ridge and then the next."
    scl_you "\"No— no, I didn't— I never {i}agreed{/i} to— {i}hngh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Breathe.\""
    "Her hand stays flat on the backs of your knees, holding them by your chest. She sinks in a ridge at a time, slow and inhumanly steady, until her scaled hips are flush against you."
    menu:
        "Your knees by your chest. Her weight in you."
        "Tell her to take it out":
            scl_you "\"Out— take it {i}out{/i}— I never signed for this—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Household serves at night. This is the night.\""
            "Deeper."
        "Beg her to let you work instead":
            scl_you "\"Lady, please— I came up the mountain to {i}work{/i}— let me just work—!\""
            "She starts to move. Out, slow, every ridge; in, slow, every ridge."
        "Shove at her hips":
            "You shove at her hips with both hands. It's like shoving the mountain."
            scl_you "\"Get— {i}off{/i}—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Hold still. Good.\""
    show cg scl_rung_two_mid onlayer cgl
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "She fucks you the way she does everything: steady, thorough, nothing skipped. The ridges drag over the place her fingers found, every stroke, and your little cock jumps against your stomach and leaks."
    scl_you "\"Don't— not there— not {i}there{/i}— {i}hhaa{/i}— that's cheating, Lady—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Your objection is entered.\""
    "You're still saying no. Your hips are rocking back to meet her on every word."
    scl_you "\"N-no— {i}no{/i}— {i}ohh{/i}—\""
    show cg scl_rung_two_peak onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Breathe. Louder. Noted.\""
    "She speeds up, just a little, and your voice goes up with her, high and cracked and loud enough for the whole gallery."
    scl_you "\"…Again. Lady. Please, again.\"" with vnfx("shake")
    "It's out of you before you can stop it. She doesn't remark on it. She gives you again."
    jump scl_first_after

## Rung 3's optional round: she bends you over the cushions again before you've caught your breath.
## It opens non-con and turns at the break, as the lap did. (rungs.twee :: Scales Pearls Sex; lead
## Long Qi, anal, doggy, noncon, pool scales, flip at the break)
label scl_pearls_sex:
    $ vn_enter(bg="scl_cushions", pc="protesting", pc_tag="scl_pc", cg="scl_pearls_again")
    "She turns you over the cushions, knees and elbows, and her tail wraps your ankles again."
    scl_you "\"Lady, wait— {i}wait{/i}— household does the floors, the dockets— not {i}this{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Household serves at night. This is the night.\""
    "She pushes in through the mess she left, all the way, and her claws trace the pearls on your spine."
    menu:
        "Her claws on your pearls. Her cock in you again."
        "Demand she stop":
            scl_you "\"Stop! The court didn't send me up here for {i}this{/i}—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
        "Yell for the gallery":
            scl_you "\"Help— HELP— is anyone on the gallery— {i}HELP{/i}—!\""
            "Everyone on the gallery hears. Nobody comes. Somewhere a door closes, tactfully."
        "Mock her":
            scl_you "\"File it, then. File it under {i}he said no{/i}.\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Filed.\""
            "She doesn't slow at all."
    show cg scl_pearls_again_mid onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Show yourself as I allow.\""
    "Her claws rake down the row, and every pearl goes off like a struck bell, straight into the ridges dragging through you."
    scl_you "\"I hate this— I {i}hate{/i}— {i}mmh{/i}— why does it feel— {i}ahh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Don't hide. Can't, anyway.\""
    show cg scl_pearls_again_turn onlayer cgl
    scl_you "\"Don't— don't stop filing me—!\"" with vnfx("shake")
    "You push your ass back onto her, all the way to the root, on purpose."
    scl_you "\"{i}Harder{/i}, Lady—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good girl.\""
    "She doesn't remark on it. She just keeps going, harder."
    show cg scl_pearls_again_peak onlayer cgl
    scl_you "\"Okay— okay, yours— household's yours— just {i}keep going{/i}—!\""
    jump scl_pearls_after

## Rung 4's optional round: it opens non-con and turns fast, on the third stroke -- you hold them up
## before she says to. (rungs.twee :: Scales Pool Sex; lead Long Qi, titjob, noncon, pool scales,
## flip on turn 3)
label scl_pool_sex:
    $ vn_enter(bg="scl_black_pool", pc="protesting", pc_tag="scl_pc", cg="scl_pool_again")
    "Her tail tightens round your waist and brings you down between her thighs again, onto your knees on the wet black stone."
    scl_you "\"Lady— again? They're still— {i}ahh{/i}— they're still so {i}tender{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Hold them together. Harder.\""
    menu:
        "Her cock against your chest. Your tits still slick with her."
        "Object":
            scl_you "\"Lady— is there a form for no? Give me the form for {i}no{/i}—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
        "Beg":
            scl_you "\"Please, Lady— my village sold its harvests for a {i}servant{/i}— not for— {i}nngh{/i}—!\""
            "Her cock slides up between them anyway."
        "Say nothing and glare":
            "You glare up at her through the steam and say nothing at all. She looks back, perfectly patient, and waits."
    show cg scl_pool_again_turn onlayer cgl
    "One stroke. Two. And then you don't wait for her. You cup your tits and hold them up round her before she says a word."
    scl_you "\"Here— {i}here{/i}, Lady— use them—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good girl.\""
    "Her cock slides up between them, slick and hot."
    show cg scl_pool_again_mid onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Dragon's colour. Proper badge.\""
    "She says it looking at your hair, and thrusts up through your cleavage. The rim of the pool shows you doing it, red and wet and eager."
    scl_you "\"Mmh— there— right there, Lady— {i}ohh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Squeeze. Good.\""
    show cg scl_pool_again_peak onlayer cgl
    scl_you "\"Don't stop— don't you dare stop— {i}harder{/i}— {i}hhaaa{/i}—!\"" with vnfx("shake")
    jump scl_pool_after

## Rung 5: the ride. Consensual, as signed off: the first time you came to her, and the first time
## you set the pace. "Spite burns out. Want endures." (rungs.twee :: Scales Ride Sex; lead Long Qi,
## ride, vocative Qi)
label scl_ride_sex:
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cg="scl_ride_open")
    "You sink down on her. All of her. Two days of nothing, and then every ridge at once, and the knot in your stomach lights up like a lamp."
    scl_you "\"{i}Ahh{/i}— Qi— yes— file it— file all of it—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Set the pace, then. I'm not moving.\""
    "Her hands rest on the bedding and do nothing at all. It's yours."
    menu:
        "Her hands still on the bedding. All of her in you."
        "Tell her what you want":
            scl_you "\"Again. All the way, Qi. To the root.\""
            "You lift, and drop, and give it to yourself."
        "Tease her":
            scl_you "\"Is that all the court gives me, Qi? I expected more {i}procedure{/i}—\""
            "Her eyes go darker. Her hands stay where they are. It's a dare, and you take it."
        "Beg her":
            scl_you "\"Please don't stop— please— I'm asking— I'm {i}asking{/i} this time—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Go on.\""
    show cg scl_ride_mid onlayer cgl
    "You ride her. Up, and down, your soft thighs spread over her hips, your tits swinging, the ridges dragging through you on every lift."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Spite burns out. Want endures. File that.\""
    "She watches you ride her."
    scl_you "\"Ahh— your ridges— I can feel every one— {i}every{/i} one— {i}mmh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Look at you up there. Good girl.\""
    show cg scl_ride_peak onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Louder.\""
    "You are. You were already."
    scl_you "\"Qi— {i}Qi{/i}— I'm going to— {i}please{/i}— {i}AHH{/i}—!\"" with vnfx("shake")
    jump scl_ride_after

## Rung 6: the first vaginal, missionary, the night after the terrace; then "not yet". Consensual.
## (rungs.twee :: Scales Six Sex; lead Long Qi, vaginal, missionary, inside, vocative Qi)
label scl_six_sex:
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cg="scl_six_open")
    "She pushes in. Slow. The fat head, then the first ridge, then the next, opening something that's never been opened, and your whole body arches off the bedding."
    scl_you "\"{i}Hhh{/i}— {i}Qi{/i}— oh— oh, that's— {i}ohh{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"[scl_full_name].\""
    "She says it like a line on the roll. Then she pushes in to the root."
    menu:
        "All of her, inside your new pussy."
        "Ask for harder":
            scl_you "\"Harder, Qi. Hold me down like you mean it.\""
            "She pins your wrists with one hand and gives you exactly that."
        "Tell her not to slow down":
            scl_you "\"Don't slow down— don't you {i}dare{/i} slow down—!\""
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Good girl. Take it. All of it.\""
        "Just moan for her":
            scl_you "\"Hhaa— it's not the steam— it was never the {i}steam{/i}— {i}ahh{/i}—!\""
    show cg scl_six_mid onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"There. There you are.\""
    "Her ridges drag through you, slow, and every one of them finds something new."
    scl_you "\"Mmh— {i}there{/i}— right there, Qi— {i}ohh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Louder, [scl_full_name].\""
    "You don't need telling."
    show cg scl_six_peak onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Squeeze. Good girl.\""
    scl_you "\"Fill me up— fill me {i}up{/i}, Qi— {i}please{/i}—!\"" with vnfx("shake")
    jump scl_six_after

## The seal night, optional: on the perch's side of the room, on your perch. Consensual.
## (ending.twee :: Scales Perch Sex; lead Long Qi, vaginal, inside, vocative Qi)
label scl_perch_sex:
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cg="scl_perch_open")
    "She pushes into you on the perch, slow, the rumpled blanket under your back and your tail wrapped round her waist."
    scl_you "\"{i}Ahh{/i}— Qi— yes— {i}yes{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Look at you, [scl_full_name].\""
    menu:
        "Your perch. Her in you."
        "Tease her":
            scl_you "\"You're breathing hard, Qi. Shall I enter that in the record?\""
            "She laughs, low, and gives you something else to record."
        "Say it in her voice":
            scl_you "\"Noted.\""
            "You say it in exactly her voice, and grin up at her. She kisses the grin off you."
        "Pull her down by the tail":
            "Your tail tightens round her waist and drags her deeper, and she lets it."
    show cg scl_perch_mid onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good girl. Your pace.\""
    "Your hips roll up to meet her, and the core in your stomach hums with every stroke."
    scl_you "\"Ahh— your ridges— I can feel every one— {i}every{/i} one— {i}mmh{/i}—!\""
    show cg scl_perch_peak onlayer cgl
    scl_you "\"{i}AHHH{/i}— yes— {i}YES{/i}—!\"" with vnfx("shake")
    "You scream it to the rafters, loud enough for the whole household corridor, and it isn't for help."
    jump scl_perch_after
