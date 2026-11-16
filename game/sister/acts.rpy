## sister's act menu (acts.twee): one optional chore a night (owner, 2026-11-11). Each is CALLED from
## si_chore_offer and returns. Its picture is drawn per the body Mae has that night ("will have to
## change cg based on rung"): cg si_act_<chore>_r<body>. All consensual, Mae eager.

label si_act_shown(key):
    $ renpy.show("cg si_act_%s_r%d" % (key, max(1, min(6, si.body or 1))), layer="cgl")
    return

label si_act_tea:
    call si_act_shown("tea")
    "Two mugs: the strawberry one for you, the chipped blue one for big sis, honey in hers, a biscuit balanced on each saucer because you're not an animal."
    "Then you fold onto the floor between her knees with the brush held up over your shoulder, and she takes it. She always does."
    "She's very good at it and very slow about it on purpose. You make a happy little noise every stroke and get called a cat for it."
    show si_paige warm at vn_cast_slot
    si_paige "\"You're a cat.\""
    si_mae "\"You're a cat.\""
    "It isn't a comeback. You both know it."
    if (si.body or 0) >= 4:
        "It takes ages now. Your hair pools red and heavy in her lap. She brushes it all out and plaits it into one fat braid over your shoulder, and you swing it round all evening like a rope."
    else:
        "She does what she can with what you've got, which isn't much yet, and promises it'll be long by spring. You believe her completely."
    hide cg onlayer cgl
    return

label si_act_bath:
    call si_act_shown("bath")
    "Bath night. The water exactly right, the bubbles ridiculous. You wash big sis's back, then her front, which takes a lot longer and comes with a running commentary on Denise and the font that neither of you is listening to."
    si_mae "\"Hold still. I'm being thorough.\""
    "Both soapy hands round her cock under the water."
    show si_paige warm at vn_cast_slot
    si_paige "\"You're being {i}something{/i}.\""
    vn_sfx "Shlk. Shlk."
    si_mae "\"Is that the spot? It's the spot. You did the face. Do the face again. Big sis, do the {i}face{/i}— come on, come {i}on{/i}, I want to see—\""
    "She comes with her toes curled over the edge and her hand on top of your head. You announce it to the bathroom like a goal. Then you have to run the water again, which is the best part." with vnfx("flash")
    hide cg onlayer cgl
    return

label si_act_morning:
    call si_act_shown("morning")
    "Kettle on. Two mugs. Her door, nudged open with your hip."
    show si_paige warm at vn_cast_slot
    si_paige "\"Sisters help sisters—\""
    si_mae "\"—with the morning problem!\""
    "In perfect deadpan unison, and you both dissolve into giggles. Then you get on with it. Both hands, slow first, twisting at the top the way she likes."
    si_mae "\"Morning! Good morning! Look at you, so grumpy, so {i}hard{/i}— faster? I'm going faster— do it, big sis, on my hands, I want it—!\""
    "You squeeze just under the head and she comes over your knuckles, thick and hot. You hold it up to show her like you've caught something." with vnfx("flash")
    si_mae "\"Ticked off!\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl.\""
    "Into the pillow. You glow all morning."
    hide cg onlayer cgl
    return

label si_act_laundry:
    call si_act_shown("laundry")
    "The official justification is {color=#ffd700}less laundry{/color}. It's been on the rota since the first morning, in big sis's handwriting, under the bins."
    "You kneel up between her knees on the sofa and take her in your mouth like it's the best thing that's happened all day. It is."
    vn_sfx "Gluk. Gluk."
    si_mae "\"{i}Mmh{/i}, you taste nice—\""
    "With genuine scientific interest, and straight back down before she can answer. You hum right at the base, nose in her, eyes glassy and happy."
    "She comes with both hands in your hair, a lot. You swallow every drop, lick her clean like you're tidying up after dinner, sit back on your heels, and open wide to show her." with vnfx("flash")
    si_mae "\"No laundry!\""
    hide cg onlayer cgl
    return

label si_act_share:
    call si_act_shown("share")
    "{i}Sisters share everything.{/i} It's on the rota. Natalie wanted it on a tote bag and was talked out of it, just about."
    "Face-down across the towel, a cushion under your hips, big sis behind you, slow and slick. You are not being quiet."
    si_mae "\"{i}Ah{/i}— big sis— oh, that's— all the way, all the way, don't you dare stop halfway—\""
    show si_paige warm at vn_cast_slot
    si_paige "\"Not stopping. God, you're {i}gorgeous{/i} like this.\""
    vn_sfx "Pap. Pap. Pap."
    si_mae "\"{i}Ahh{/i}— harder, big sis— sisters share {i}everything{/i}— give me {i}all{/i} of it—!\""
    "She finishes deep, groaning your name into the back of your neck. You shake apart round her a second later, moaning into the cushion, and lie under her weight afterwards, humming." with vnfx("flash")
    si_mae "\"Sharing.\""
    hide cg onlayer cgl
    return

label si_act_skincare:
    call si_act_shown("skincare")
    "Filed under {color=#ffd700}skincare{/color} on the rota. The jar over the bath still says {i}Sister Special{/i}, and it's still empty, because it's never needed to be anything else."
    "You kneel on the bathmat, eyes shut, face tipped back, hands on your knees, and talk the whole time she's stroking herself over you."
    si_mae "\"Is it soon? You're doing the breathing. Shushing me is very bad for my skin— {i}mmh{/i}— on my face, big sis, all of it, {i}please{/i}—\""
    "It lands hot and thick across your cheeks and lips and eyelids. You squeal and hold still while she smooths it in with her fingertips." with vnfx("flash")
    show si_paige warm at vn_cast_slot
    si_paige "\"Good girl. {i}Very{/i} good girl.\""
    si_mae "\"Is it good for my skin?\""
    show si_paige warm at vn_cast_slot
    si_paige "\"It's fantastic for your skin.\""
    si_mae "\"{i}Knew{/i} it.\""
    hide cg onlayer cgl
    return

label si_act_pride:
    call si_act_shown("pride")
    "This one was your idea. You bring it up constantly, and you will for years."
    si_mae "\"{i}I{/i} invented this. It's on the rota. It's got my name on it.\""
    "From her lap, breasts squeezed together round her cock, the head poking out of your cleavage at you. It has. Green pen. {i}Mae's idea.{/i}"
    vn_sfx "Fwp. Fwp. Fwp."
    si_mae "\"Look at it, it fits perfectly— {i}mm{/i}— big sis, you've gone so hard, you've gone so {i}red{/i}—\""
    "You're in charge of the rhythm for once, very pleased and very noisy, and big sis goes to pieces about it fast, all over your chest and your chin. You laugh and rub it in like lotion." with vnfx("flash")
    si_mae "\"Both problems. Solved.\""
    hide cg onlayer cgl
    return

label si_act_pace:
    call si_act_shown("pace")
    si_mae "\"Lie back. I'm setting the pace.\""
    show si_paige warm at vn_cast_slot
    si_paige "\"You always set the pace now.\""
    si_mae "\"Because I'm {i}good{/i} at it.\""
    "You climb on, thick soft thighs spread over her hips, skirt round your waist, and sink down onto her, slow, all of it."
    vn_sfx "Pap. Pap. Pap."
    si_mae "\"Look at me! Look at me, big sis, I'm riding you so {i}good{/i}— {i}pace!{/i}\""
    "You come first, clenching round her, shrieking at the ceiling. She comes right after, deep inside you, and you sit on her with your hair everywhere, gasping and grinning, enormously proud." with vnfx("flash")
    hide cg onlayer cgl
    return
