## womensbath's soaks and scenes. THE WATER HOLDS: the spring's change is forced through him, his legs won't
## carry him out; Iori carries on past his no, patient, never threatening. The choice when he protests is
## what he says, never whether. Ch 1-4 non-con, no flip; ch 5-6 break into begging; ch 7 on consensual.
## Production rewrite (2026-11-13, twinetesting-c9): every soak and scene run long, a picture per beat.

## ---- ch 1: the first soak. Solo, the change forced through him -------------------------------
label wom_first_soak:
    "Nothing. Hot water. A bit more mineral than yours, a bit softer. You sink to the shoulders on the polished ledge and feel slightly foolish, and very tired, and think about the valve."
    "Then the change creeps in under the skin before you register it as change at all. Warmth. Every fine hair on your arms standing up, then sinking away into velvet."
    show cg wom_change_hair onlayer cgl
    "You lift an arm out of the water to look. The hair's going. Not falling: going, drawing back into the skin like a tide, and the skin left behind is pale and fine and gleaming."
    wom_you "\"What—\""
    show cg wom_change_one onlayer cgl
    "Your nails sharpen, pale. Your chest trembles, then rushes forward all at once, flesh blooming into the weight of breasts, {i}your{/i} breasts, rising heavy above the water, the nipples tightening in the cold air of the bath hall."
    wom_you "\"No— no, no— what the—\""
    "You grab the edge to climb out."
    $ wom_soak(True)
    show cg wom_legs_fold onlayer cgl
    "Your legs fold. The water holds you down on the ledge like a hand, warm and heavy and absolutely patient, and your knees won't take your weight."
    menu:
        "The water won't let you up."
        "Shout for Iori":
            $ wom.shout1 = "iori"
            wom_you "\"Iori— IORI— it's doing something— get me OUT—\""
            "Your voice cracks halfway and comes out higher on the other side. Nobody comes. Nobody peeks."
        "Haul at the edge":
            $ wom.shout1 = "haul"
            "You haul at the polished edge with both hands. Your arms are slimmer than they were a second ago, and they slide."
            wom_you "\"Let go— let GO— I'm not— I don't want—\""
    show cg wom_change_hips onlayer cgl
    "Your waist cinches. Your hips round, pushing out under the water against the ledge. Your thighs flood out plush and soft, and your cock draws back in a slow tingling retreat under a soft new mound, and fades, and folds, and it's slick between your legs."
    "Red hair spills past your nipples, two ropes of it already gathering at your shoulders, a red nobody in your family ever had."
    wom_you "\"Give it back— give it {i}back—{/i}\""
    show cg wom_change_peak onlayer cgl
    "The heat sits deep between your new legs and pulses, slow, like a second heartbeat. Your hand goes there. You didn't send it."
    wom_you "\"Stop— stop it— that's not— {i}ahh{/i}—\"" with vnfx("shake")
    "One brush over the clit and your hips seize. It's nothing like anything. It's a hundred times too much, from everywhere at once. Your other hand cups a breast that fits too perfectly. The water holds your knees apart."
    vn_sfx "{i}Splsh... splsh...{/i}"
    wom_you "\"I'm not doing this— I'm not doing it, it's doing— {i}nnh{/i}— my hand won't—\""
    "Your fingers slide down and find the slick new opening and press in, and your whole body clenches round them, and your back arches off the ledge, and the sound you make echoes round a bath hall built for women."
    wom_you "\"No— no— {i}oh{/i}— don't— don't sto— no, I mean STOP— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg wom_change_after onlayer cgl
    "It breaks over you, everything inside clutching and fluttering, wave after wave, and you shout it into a wet shoulder that isn't the shape of yours."
    "Then the water lets go. Your legs work again. Your hands shake so badly you can barely stop the stopwatch, and when you look at it, it says you've been in for nine minutes."
    hide cg onlayer cgl
    jump wom_ch1_after

## ---- ch 3: the night soak. Solo, longer --------------------------------------------------------
label wom_night_soak:
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_private_bath", pc="uneasy", pc_tag="wom_pc", cast=[], cg="wom_private_soak")
    "The private bath is cedar and lamplight and a small window full of dark pines. You only meant to get in and get it over with: change, settle, whatever settle means, out."
    "It takes you faster than before, each change sharper and more sensual than the last: the hair going, the breasts, the hips, the wet heat between your legs, the red hair floating out round you on the water."
    wom_you "\"Just— just the change. That's all I need. Just the change, and out.\""
    show cg wom_private_hold onlayer cgl
    "You try to stand. The water holds your hips to the bench, the way it did that first night, and this time it doesn't feel like a hand. It feels like a lap."
    menu:
        "The water holds you."
        "Talk to it":
            $ wom.shout3 = "talk"
            wom_you "\"I'm just here for the shift— I'm just— {i}nnh{/i}— stop it, stop—\""
        "Grab the lip of the tub":
            $ wom.shout3 = "grab"
            "You grab the cedar lip. The heat between your legs climbs instead, and your back arches off the bench."
            wom_you "\"Not again— not AGAIN— let me OUT—\""
    show cg wom_private_touch onlayer cgl
    "Your own fingers find you. Your other hand is on your breast, rolling the nipple, and you didn't send that either. Your hips rock for your fingers, slow, in the water, like they've been doing it all their life."
    wom_you "\"I don't— {i}hah{/i}— I don't want— I'm not even— {i}nnh{/i}—\""
    "The first one comes fast and hard and you think, {i}there, done,{/i} and the water rolls through you again before you've breathed out."
    show cg wom_private_again onlayer cgl
    vn_sfx "{i}Splsh. Splsh. Splsh.{/i}"
    "It's longer this time, so much longer. Every time you think it's done, the water rolls through you again, and your fingers start again, deeper, three of them now, and the cedar creaks under your heels."
    wom_you "\"{i}Ahh{/i}— no— no more— please— {i}please{/i}— no, I meant— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You lose count. Four. Five. The lamp gutters. Somewhere outside an owl. You lie half-floating with your hair all round you like weed, and your hands finally still."
    show cg wom_folded_clothes onlayer cgl
    "When it lets you go you dress in the women's clothes Iori left folded on the bench, a soft knit and a skirt, because yours won't do up over the hips, and you don't argue with them. You haven't got the breath."
    hide cg onlayer cgl
    jump wom_ch3_after

## ---- ch 4: noon. Iori, in the steam, his first time with her ----------------------------------
label wom_noon_bath:
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_women_bath", pc="uneasy", pc_tag="wom_pc", cast=[("wom_iori", "patient")], cg="wom_noon_iori")
    "Iori's in the water when you get there, at ease in her body the way you aren't in yours, her hair down for once, black and long on the surface. The bath's closed for cleaning between sittings. Just the two of you and the steam."
    "You change on the steps, fast now, and sit as far from her as the bath allows."
    wom_iori "\"Come here. I need to see how it's settling.\""
    "She doesn't wait for you to come. She comes to you, through the water, unhurried."
    show cg wom_noon_touch onlayer cgl
    "Her hands on your new shoulders. Your new waist. Under your breasts, weighing them, curious, tender, thorough, like she's checking a delivery against a list."
    wom_iori "\"Heavier than last week. The voice stayed?\""
    wom_you "\"Iori— that's— you can stop now, you've seen—\""
    wom_iori "\"It settles better if you're touched. That's all this is.\""
    "Her thumb brushes your nipple, idly, and your whole spine answers it."
    show cg wom_noon_hand onlayer cgl
    "Her hand slides down your belly, under the water, between your thighs."
    menu:
        "Iori's hand."
        "Tell her to stop":
            $ wom.shout4 = "stop"
            wom_you "\"Stop— Iori, stop, I didn't— {i}hah{/i}— I didn't come for this—\""
        "Grab her wrist":
            $ wom.shout4 = "wrist"
            "You grab her wrist. She lets you hold it. She doesn't move it."
            wom_you "\"Please— take your hand— {i}nnh{/i}— take it away—\""
    wom_iori "\"Shh. I know.\""
    "Patient. Never once a threat. She just keeps going, slow, two fingers in the slick new folds and her thumb on your clit, and your thighs open in the water on their own."
    wom_iori "\"It was the same for me. The first touch. It feels like it's not yours. It is. All of it.\""
    wom_you "\"It's not— it's {i}not{/i} mine, I want— {i}nnh{/i}— I want it back—\""
    show cg wom_noon_hold onlayer cgl
    "She tips your head onto her shoulder with her other hand and holds you there, in the steam, and works you, and talks to you the whole time, low and level, like a nurse."
    wom_iori "\"Your body knows. Let it. There's no hurry. There's never any hurry here.\""
    vn_sfx "{i}Splsh. Splsh.{/i}"
    "And under the water, pressed against your hip, something hard and heavy and very large, that she doesn't mention, and doesn't use."
    show cg wom_noon_peak onlayer cgl
    wom_you "\"No— no— Iori— {i}ohh{/i}— don't— don't stop— no— I mean STOP—\"" with vnfx("shake")
    "She doesn't stop. She curls her fingers, once, and holds them there."
    wom_you "\"{i}AHH{/i}— {i}Iori{/i}—!\"" with vnfx("flash", "shake")
    "You come on her hand with your face in her neck and your new voice cracking on her name, and she keeps her fingers in you until the last of it's gone."
    show cg wom_noon_after onlayer cgl
    "Afterwards she holds you against her in the steam, and all the questions about how long it lasts seem to matter less, and you hate that they do."
    wom_iori "\"Noon tomorrow.\""
    "It isn't a question. You don't answer it. You're there at noon."
    hide cg onlayer cgl
    jump wom_ch4_after

## ---- ch 5: the night bath. Iori starts it; he breaks into begging -----------------------------
label wom_night_iori:
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_private_bath", pc="flushed", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_five_bath")
    "That night Iori's in the private bath when you get there. Your private bath. Your key on its red tag. She's already in the water, waiting, and she pulls you into her lap before you've sat down."
    wom_you "\"Wait— not tonight— I've had a day, I've been two towns over, I've— Iori—\""
    wom_iori "\"I know. I saw the bag.\""
    show cg wom_five_lap onlayer cgl
    "She turns you round in the water so your back's to her chest, and her mouth goes to your neck, and then round, and down, to your breast. And her fingers are back inside you. And something hard and very large rests against the small of your back."
    menu:
        "Iori's mouth, her hands."
        "Push away":
            $ wom.shout5 = "push"
            wom_you "\"No— get off— {i}hah{/i}— I said not tonight—\""
        "Hold still and endure it":
            $ wom.shout5 = "endure"
            wom_you "\"I'm not— I'm just going to— sit here— {i}nnh{/i}— and not—\""
    wom_iori "\"You can say no all night. I'll still be here.\""
    show cg wom_five_breast onlayer cgl
    "She sucks your nipple slow, the way you'd savour something, and her fingers move in you to the same rhythm, and the big shape of her slides along the cleft of your arse under the water, not in, just there, warm and patient."
    wom_you "\"Iori— {i}ohh{/i}— that's— I don't— I'm not going to— {i}nnh{/i}—\""
    "Your hips are moving. On her fingers. Back against her. You didn't decide that."
    show cg wom_five_grind onlayer cgl
    vn_sfx "{i}Splsh. Splsh. Splsh.{/i}"
    "And then, halfway through, the fight just goes out of you. Like a plug pulled. You feel it go, and you can't find it again, and you stop looking."
    $ wom.broke = True
    show cg wom_five_beg onlayer cgl  # ff 2:13 pm 11-18: v4 gen-962609108 landed (QA checker 2:10 pm)
    wom_you "\"Don't— don't stop— Iori— {i}please{/i}— more, please, more—!\"" with vnfx("flash", "shake")
    "You beg her through it, loud, the way you'd never let yourself in the daytime, grinding down on her fingers, your hand over hers on your breast, and she gives you every bit, and another, and another."
    wom_iori "\"There you are.\""
    wom_you "\"{i}Hah{/i}— don't— don't say it like that—\""
    wom_iori "\"There you are, Tsubaki.\""
    "She says it like a woman finding someone at a station."
    hide cg onlayer cgl
    jump wom_ch5_after

## ---- ch 6: Iori, bigger again, takes him fully ----------------------------------------------
label wom_iori_full:
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_private_bath", pc="uneasy", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_six_iori")
    "Iori's changed too. You see it the moment she stands up out of the water: more of her than there was, everywhere. Fuller breasts, wider hips, and her cock heavy and huge between her thighs, bigger than it was against your back last week."
    wom_iori "\"It does this to me too. Every time I'm in it beside you. It has for eleven years, bit by bit. Since you, it's not bit by bit.\""
    wom_you "\"Since me?\""
    wom_iori "\"Since you.\""
    show cg wom_six_edge onlayer cgl
    "She lays you back on the cedar edge and kneels up between your knees in the water, and the head of her presses against your new pussy, slick and blunt and enormous."
    wom_you "\"Iori— wait— not that, I've never— it's too much—\""
    wom_iori "\"I know. It's how it settles.\""
    menu:
        "She's pressing in."
        "Tell her it's too much":
            $ wom.shout6 = "much"
            wom_you "\"It's too big— Iori— wait— {i}wait{/i}—\""
            wom_iori "\"I'm waiting. Breathe.\""
            "She waits exactly one breath. Then she goes on."
        "Brace your hands on her shoulders":
            $ wom.shout6 = "brace"
            "You brace both hands on her shoulders to stop her. She leans into them, slow, and goes in anyway."
    show cg wom_six_in onlayer cgl
    "She sinks in, slow, so slow, and you feel every bit of it open you round her, the water lapping at the edge with each small push, until her hips are against yours and you're full of her to somewhere under your ribs."
    wom_you "\"No— no— {i}ahh{/i}— so full— Iori, it's so— {i}ohh{/i}—\"" with vnfx("shake")
    wom_iori "\"Look at you. Look how you take me.\""
    show cg wom_six_move onlayer cgl
    "She moves. Long, slow strokes, all the way out and all the way back, and every one of them drags a sound out of you that you'd never have made with your old throat."
    vn_sfx "{i}Splsh. Pap. Splsh. Pap.{/i}"
    wom_you "\"Stop— {i}ahh{/i}— Iori, stop, it's too— it's too {i}good{/i}— no— I mean—\""
    "And again the noes go somewhere you can't follow. You reach for them and they're gone, and there's only her, and the cedar under your back, and the water, and this."
    show cg wom_six_deep onlayer cgl
    wom_you "\"Deeper— don't stop— {i}please{/i}— Iori— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "She comes deep in you, holding you on the edge of the bath with your knees over her arms, and you come round her shouting at the cedar roof, and she holds you there through it, still inside, still hard, saying your name."
    hide cg onlayer cgl
    jump wom_ch6_after

## ---- ch 7: the flip. She goes looking for her, and asks ---------------------------------------
label wom_ask:
    $ wom.fit = "nude"
    $ wom_soak(True)
    $ vn_enter(bg="wom_private_bath", pc="begging", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_seven_ask")  # ff 2:13 pm 11-18: v3 gen-292034736 landed (QA checker 2:10 pm)
    "Daylight in the private bath. Nowhere to hide in it. Iori's in the water with a ledger on the edge, doing the morning's bookings with a pencil, and she looks up."
    "Tsubaki stands on the step with the red roots in her hair and nothing on, and makes herself say it, in the daylight, out loud."
    $ wom.asked = True
    wom_you "\"I want you to. All of it. Properly. I'm asking.\""
    wom_iori "\"Asking.\""
    wom_you "\"I'm asking. Nobody's holding me. The water isn't holding me. I'm asking you.\""
    "Iori puts the pencil down. Her smile breaks loose, outright, for once in eleven years."
    show cg wom_seven_kiss onlayer cgl
    "She comes up out of the water and kisses her, properly, for the first time: no settling, no patience, just a kiss, and Tsubaki kisses her back, and climbs into her arms."
    show cg wom_seven_claim onlayer cgl
    "She takes her on the cedar boards in the daylight, slow and then not slow, claiming every curve of her: the breasts that stayed, the hips, the thighs, the red hair spread out on the wood."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    wom_you "\"Yes— yes, Iori— harder— {i}yes{/i}— like that— don't stop, I mean it, I mean it this time—\""
    show cg wom_seven_ride onlayer cgl
    "Then Tsubaki rolls her over and rides her, because she wants to see what that's like, and it's like everything, and she says so, loud, without one single no."
    wom_iori "\"Tsubaki—\""
    wom_you "\"{i}Ahh{/i}— Iori— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "Afterwards she does the afternoon's work naked and glowing and laughing at the ledger, with Iori's pencil behind her ear, and she doesn't care who hears."
    hide cg onlayer cgl
    jump wom_ch7_after

## ---- ch 8: after the ledger. She leads --------------------------------------------------------
label wom_lead:
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_women_bath", pc="proud", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_eight_lead")
    "Tsubaki pushes Iori down onto the ledge this time, in the main bath, after closing, and climbs on, and takes her herself, slow, her hands on Iori's shoulders, deciding everything."
    wom_you "\"Stay there. Let me.\""
    wom_iori "\"Please.\""
    "It's the first time Iori's ever asked for anything. Tsubaki hears it, and takes her time about answering."
    show cg wom_eight_slow onlayer cgl
    "She rides her so slowly the water barely moves. Up, and all the way down, and stop. Up. Down. Stop. Until Iori's head is back against the stones and her hands are fists in the water."
    wom_you "\"Fifteen years. He ran it down for fifteen years. And you waited eleven.\""
    wom_iori "\"I'd have waited longer.\""
    wom_you "\"I know. You don't have to.\""
    show cg wom_eight_end onlayer cgl
    vn_sfx "{i}Splsh. Splsh. Splsh.{/i}"
    "Then she stops being slow. She rides her until the water slops over the edge, and Iori comes in her with her face in Tsubaki's neck, and Tsubaki comes with her, choosing it, every second of it."
    hide cg onlayer cgl
    jump wom_ch8_after

## ---- ch 9: Hazuki, then Iori --------------------------------------------------------------------
label wom_hazuki:
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_private_bath", pc="flushed", pc_tag="wom_pc", cast=[("wom_hazuki", "sly")], cg="wom_nine_hazuki")
    "Hazuki makes her intentions clear by the private bath door, with Iori's small approving nod from across the corridor."
    if wom.note6 == "wrote":
        wom_hazuki "\"You wrote back. Nobody writes back. I've read it about forty times.\""
    else:
        wom_hazuki "\"You kept the note. Nao told me. She tells me everything.\""
    wom_hazuki "\"I asked for you by name, you know.\""
    wom_you "\"I know. I've got the note.\""
    show cg wom_nine_kiss onlayer cgl
    "She's slow and curious and greedy with her: her mouth on Tsubaki's breasts, her fingers learning her, a thigh between hers in the warm water. Tsubaki lets her, and likes it, and says so."
    wom_you "\"Like that. {i}Mm.{/i} Slower. Like that.\""
    wom_hazuki "\"Bossy.\""
    wom_you "\"I run the place.\""
    show cg wom_nine_grind onlayer cgl
    "Hazuki laughs and grinds down on her thigh, and Tsubaki pulls her close by the hips and kisses her through it, and comes first, which she'd decided she would, and then makes very sure Hazuki does."
    hide cg onlayer cgl
    $ vn_enter(bg="wom_private_bath", pc="begging", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_nine_iori")
    "And afterwards, when Hazuki's gone off pink and humming to her room, Iori's waiting in the steam, and takes her the way only Iori does: deep and patient and huge, over the cedar edge, until the last of the uncertainty goes out of her."
    wom_iori "\"Jealous?\""
    wom_you "\"{i}Ahh{/i}— you sent her— you nodded—\""
    wom_iori "\"I did. Was it nice?\""
    wom_you "\"It was— {i}ahh{/i}— lovely— and this is— {i}AHH{/i}— Iori—!\"" with vnfx("flash", "shake")
    hide cg onlayer cgl
    jump wom_ch9_after

## ---- ch 10: the night before the choice ---------------------------------------------------------
label wom_ten_night:
    $ wom.fit = "nude"
    $ vn_enter(bg="wom_women_bath", pc="flushed", pc_tag="wom_pc", cast=[("wom_iori", "soft")], cg="wom_ten_night")
    "Nightfall, the empty onsen. Tsubaki finds Iori in the water, and holds onto her like she's the one keeping her afloat."
    "It's desperate, and it's trust, and Iori lets her set every bit of the pace: slow, in Iori's lap, face to face, barely moving, the lanterns swaying on the water."
    wom_you "\"Don't let go. Not yet.\""
    wom_iori "\"I'm not going anywhere. Neither are you, if you don't want to.\""
    show cg wom_ten_close onlayer cgl
    "They don't talk about the proposal on the desk. They don't talk about the men's side. Tsubaki holds Iori's face in both hands and moves on her until they're both shaking, and comes quietly, for once, into Iori's mouth, and stays there."
    wom_you "\"Whatever I choose.\""
    wom_iori "\"Whatever you choose.\""
    hide cg onlayer cgl
    jump wom_ch10_choice
