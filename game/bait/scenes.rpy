## bait's encounters, ch 1-6. THE LURE ANSWERS: he calls them; he never agrees to what they do once they have
## him. Non-con ch 1-5 (no menace, no pain), ch 6 the break. The choice when he protests is what he says or does,
## never whether. All humanoid, grown, futa or male, bigger than him. He is the receptive one, every time.
## The production rewrite (2026-11-13): every encounter at full length, a picture every beat.

## ---- ch 1: the warg-woman. Wordless, knotting ------------------------------------------------------
label bai_warg:
    $ bai.fit = "trapper"
    $ vn_enter(bg="bai_forest", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_warg_arrive")
    "She comes out of the ferns on all fours and stands up: a warg-woman, wolf-eared, grey-furred at the forearms and shins, half again your height, a mane of tangled grey hair down her back."
    "She doesn't speak. She sniffs the air where you are, long and slow, and her eyes go half-shut, and her cock rises between her thighs, thick and dark and already wet at the tip."
    bai_you "\"Whoa— whoa, no, hang on— I didn't mean— I turned it DOWN—\""
    menu:
        "The warg-woman, close enough to touch."
        "Scramble backwards":
            $ bai.shout1 = "scramble"
            "You scramble backwards through the leaf litter on your elbows. She takes one step and you're under her."
        "Try to reason with her":
            $ bai.shout1 = "reason"
            bai_you "\"Look, I'm sure you're very nice, but this is a misunderstanding, I'm just—\""
            "She doesn't have words. She has a hand on the back of your neck."
    $ bai.fit = "nude"
    show cg bai_warg_strip onlayer cgl
    "She has the coat off you before you've worked out which way to run. The tee goes in one pull, the shorts in another, and the cold hits your whole body at once and doesn't matter, because the scent is still rolling off you and your cock is still aching hard."
    bai_you "\"Hey— those are my only— {i}no{/i}— get your hands—\""
    show cg bai_warg_pin onlayer cgl
    "Face-down in the leaves. Her weight comes down over you, a palm spread between your shoulders pressing you flat, her breath hot at your ear, and the slick heavy head of her cock slides down between your cheeks and stops."
    bai_you "\"No— no, no— that's not— you can't— it won't—\""
    "She pushes."
    bai_you "\"Wait— wait, at least— at least {i}slow{/i}— oh god, you're not going to slow down, are you—\""
    show cg bai_warg_open onlayer cgl
    "It goes in. It shouldn't, and it does, slow and thick and relentless, and the scent pouring off you seems to make your body give for her, as if it's been told to."
    bai_you "\"{i}Hahh{/i}— get OFF— get it {i}out{/i}— oh god, it's— it's all the way— {i}nnh{/i}—\""
    "Her hips settle against your ass. She's in to the root. She waits there a moment, panting, like she's savouring it."
    bai_you "\"Okay. Okay. It's in. It's all in. You can stop now. You've— you've proven your point— {i}hahh{/i}—\""
    "She hasn't proven anything. She hasn't started."
    show cg bai_warg_mid onlayer cgl
    "Then she starts, and doesn't stop. Long hard strokes that drive you forward through the leaf litter bit by bit, her hand holding your shoulders down, her other arm braced in the dirt beside your face."
    "She's not cruel about it. She's not anything about it. She fucks you the way weather happens, steady and total, and the only sound she makes is her breath, rough and pleased, in your ear."
    bai_you "\"Slower— {i}slower{/i}— okay not slower, not {i}slower{/i}, just— I don't know, just— {i}nnh{/i}— stop being so {i}good{/i} at it—\""
    vn_th "(You said that out loud. You said that out loud to a wolf.)"
    vn_sfx "Thk. Thk. Thk."
    bai_you "\"Stop— stop— {i}ahh{/i}— oh god— don't— don't stop— NO— I mean STOP—\"" with vnfx("shake")
    vn_th "(That's the lure. That's not you. That's the dial talking with your mouth.)"
    "Your cock is grinding into the moss under you on every thrust, and it's leaking, and there's no hiding what it's doing."
    bai_you "\"Don't— don't make me— I'm not going to— {i}ahh{/i}— I'm NOT—\""
    "Her teeth close gently on the back of your neck, not biting, just holding, and your whole body goes slack and obedient under her, and you hate it, and you're louder than you've ever been."
    bai_you "\"{i}Ahh{/i}— {i}AHH{/i}— no— no no no— {i}fuck{/i}— {i}fuck{/i}, that's— right there— NO—\"" with vnfx("shake")
    show cg bai_warg_knot onlayer cgl
    "Then the knot. It swells at the base of her and pushes, and pushes, and slips in with a sound you'll never forget, and locks. She settles over you to wait, and you're tied to her on the forest floor."
    bai_you "\"What is— what's that— it's— {i}ahh{/i}— it's {i}stuck{/i}— it's too— {i}AHH{/i}—\""
    show cg bai_warg_peak onlayer cgl
    "Locked like that, every shift of her weight grinds the knot against something inside you that makes your vision go white at the edges, and she shifts, and shifts, and you come into the leaves with your face in your arms, shouting."
    bai_you "\"{i}AHH{/i}— {i}please{/i}— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    "She comes too, a long deep shudder over your back, and floods you, and the knot holds it all in."
    bai_you "\"It's— it's still— you're still coming— how are you still— {i}nnh{/i}— I'm so {i}full{/i}—\""
    vn_th "(Thirty minutes. You had a base for thirty minutes.)"
    show cg bai_warg_leave onlayer cgl
    "She stays a long time. When the knot finally lets go she slides out of you with a wet pull, licks the back of your neck once, and is gone into the ferns without looking back."
    "You lie there in the leaves, dripping, staring at the panel. It hasn't changed. It's still waiting for you to read it."
    jump bai_ch1_after

## ---- ch 2: the slime-woman. Engulfed, edged ---------------------------------------------------------
label bai_slime:
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_stream", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_slime_rise")
    "A woman made of clear living gel, humming, pale blue where the light comes through her, with a cock of the same gel and no edges anywhere. She rises out of the stream to her full height and tilts her head at you, curious."
    bai_you "\"Oh. Okay. Okay, that's a response. Note: aquatic. Note: very, um. Interested.\""
    "You turn the dial up a hair more, for science, and write it down."
    show cg bai_slime_hand onlayer cgl
    "She takes your hand. Then your wrist, gel flowing warm up your forearm. Then your arm to the shoulder, while you're still holding the stick."
    bai_you "\"Okay— okay, that's enough data— I've got the gist— let go now—\""
    "She doesn't let go. She doesn't have a shape to let go with. She simply flows round you, and you're inside her up to the chest."
    show cg bai_slime_engulf onlayer cgl
    "Filled from everywhere at once. Her gel in your mouth, round your cock, into your ass, pressing every inch of you with no edge anywhere, warm as bathwater and twice as patient."
    "Her face forms in the gel in front of yours, smiling, curious, watching your expression the way you'd been watching the stream."
    bai_you "\"Don't— don't {i}look{/i} at me like that, I'm the one taking notes— {i}mmph{/i}—\""
    bai_you "\"{i}Mmh{/i}— {i}mmph{/i}— stop— {i}hahh{/i}— too much— no edges, there's no— {i}ahh{/i}—\""
    menu:
        "Inside her."
        "Try to swim out":
            $ bai.shout2 = "swim"
            "You try to swim. There's nothing to push against. Every stroke she simply becomes wherever your hand was going."
        "Hold your breath and wait":
            $ bai.shout2 = "wait"
            "You hold your breath and wait it out. She waits longer. She has all day, and she's made of it."
    show cg bai_slime_fill onlayer cgl
    "She stretches you. Not hard: wide, and wider, and you feel yourself give and give and not tear, and that's somehow worse, because there's no point where it has to stop."
    bai_you "\"Elastic— that's— I'm elastic— {i}ohh{/i}, you're {i}teaching{/i} it to me— stop teaching— {i}AHH{/i}—\""
    "She hums approval through every inch of you, and the hum goes straight to your cock."
    bai_you "\"That's— that's not— how is that— {i}nnh{/i}— that's too {i}wide{/i}— I'm not built for— {i}ohh{/i}—\""
    show cg bai_slime_edge onlayer cgl
    "And she won't let you finish. Every time you're close, the gel round your cock goes slack and soft and still, and waits for you to come back down, and then starts again."
    bai_you "\"No— no, don't stop {i}there{/i}— I mean stop— I mean— {i}please{/i}— just let me—\""
    vn_th "(Hours. It's been hours. The sun's moved. She's edging you like it's a hobby.)"
    "Again she brings you right to the brink, all of her squeezing and rippling round your cock and inside you at once, and again she goes still at the last second, and you scream at the trees."
    bai_you "\"You're {i}doing{/i} that— you're doing that on {i}purpose{/i}— I'm writing you {i}up{/i}— {i}nngh{/i}— I'm giving you {i}one star{/i}—\""
    "She ripples, amused. It feels like a laugh going all the way through you."
    bai_you "\"Please— okay— please— I take it back— five stars— {i}please{/i} let me—\""
    show cg bai_slime_peak onlayer cgl
    "And then she doesn't stop, and the whole clear body of her squeezes at once, and you come so hard your back arches inside her and the stream sloshes over the bank."
    bai_you "\"No— no— {i}please{/i}— don't— don't stop— NO— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "She keeps going through it, gently, past it, into overstimulation, until you're twitching and gasping and too wrung out to say anything at all."
    show cg bai_slime_bank onlayer cgl
    "She puts you down on the bank, very gently, on your back on the warm rock, and pours back into the stream, and is just water again."
    jump bai_ch2_after

## ---- ch 3: the myconid. Saturated, most of a day -----------------------------------------------
label bai_myconid:
    $ bai.fit = "trapper"   # dressed until she undresses him at the glade (the 2026-11-13 art walk)
    $ vn_enter(bg="bai_forest", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_myconid_spores")
    "A nudge. Just a nudge. And her breath goes gold, and the whole glade fills with it, a slow sweet cloud of spores drifting down through the light like pollen."
    "Every breath you take of it makes your knees softer. You sit down without deciding to."
    bai_you "\"Okay. That's— that's potent. That's very— I'm going to just. Leave. In a minute.\""
    $ bai.fit = "nude"
    show cg bai_myconid_glade onlayer cgl
    "She kneels over you and lays you back in the moss as if you were something she'd grown, and takes your clothes off with soft careful fingers, and you watch her do it."
    bai_you "\"I was only— looking— I wasn't calling you— {i}hahh{/i}— I didn't turn it up—\""
    "You did. You don't remember doing it. The dial on the panel is glowing well past where you left it."
    show cg bai_myconid_hold onlayer cgl
    "Her cock is pale and slow and huge, and she slides it into you a fraction at a time, letting the spores do the work, your body opening for her on every breath."
    bai_you "\"Let me up— I have to— {i}nnh{/i}— I have things to— oh— {i}ohh{/i}— don't— no—\""
    "She hums. She doesn't hurry. She has nowhere else to be, and neither, it turns out, do you."
    "Gold dust settles on your eyelashes. You blink it away and breathe in more. You can't stop breathing in."
    bai_you "\"Stop breathing on me— no, don't stop— that's the spores talking— {i}nnh{/i}— that's not me—\""
    show cg bai_myconid_mid onlayer cgl
    "She keeps you there most of a day. Her cock moving slow and deep, her soft hands on your chest, your hips, your swelling chest, the light going amber and then dim, the spores settling on your skin like gold dust."
    "She talks, now and then, in a voice like pages turning: \"Still. Breathe. Root.\" It's the only advice anybody's given you in this forest, and it's terrible, and you take it."
    bai_you "\"Root— root where— {i}ohh{/i}— that's not a place, that's a— {i}hahh{/i}— a verb—\""
    bai_you "\"How long— how long have we— {i}mmh{/i}— I'm not— I'm not enjoying this, this is the spores, this is chemical—\""
    show cg bai_myconid_edge onlayer cgl
    "She holds you right at the edge. For an hour. You can feel it building in your chest and your hips as much as your cock, a pressure that has nowhere to go."
    "Her soft hands knead your swelling chest while she holds you there, and every squeeze pushes the pressure higher, and your nipples are so hard they ache in the gold air."
    bai_you "\"Don't— don't touch those— they're new— they're {i}new{/i}, they're not meant to— {i}ahh{/i}— why are they so {i}sensitive{/i}—\""
    "\"Root,\" she murmurs, and squeezes, and you moan so loudly that something in the trees takes off in fright."
    bai_you "\"Please— please let me— no— don't let me— I don't know what I'm saying—\""
    show cg bai_myconid_peak onlayer cgl
    "She lets you. You come once, shouting at the canopy, and before you've come down she starts again and you come twice."
    bai_you "\"{i}AHH{/i}— again— no— not again— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg bai_myconid_dusk onlayer cgl
    "By dusk you're coated gold from head to foot, lying in the moss where she left you, and you smell like a prize."
    "You pass out before you can write anything down."
    jump bai_ch3_after

## ---- ch 4: the harpy. Taken aloft ----------------------------------------------------------------
label bai_harpy:
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_ridge", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_harpy_dive")
    "She doesn't land. She takes you by the hips with her talons on the way past, and the rock falls away under your feet."
    bai_you "\"Over the ridge! THAT way! That's— no, that's up, that's just up— that's a LOT of up—\""
    "The coat tears off somewhere over the first stand of trees. She doesn't go back for it."
    show cg bai_harpy_aloft onlayer cgl
    "Mid-air, held by the hips, the wind roaring past, and she pulls you back against her and her cock slides into you with the ground a very long way down."
    bai_you "\"Not— not up {i}here{/i}— are you insane— {i}hahh{/i}— we're in the {i}sky{/i}—\""
    menu:
        "Mid-air."
        "\"Put me down!\"":
            $ bai.shout4 = "down"
            bai_you "\"Put me DOWN! Put me— no, not like that, don't DROP me— {i}hahh{/i}—\""
            "She tightens her grip, which is not what you meant, and is somehow exactly what you meant."
            "Her laugh is a shriek. Her wings beat once, hard, and you go up a whole wingbeat on her cock and come back down on it so deep you see stars."
        "Hold on and say nothing":
            $ bai.shout4 = "hold"
            "You hold on to her ankles and say nothing at all, because you can't think of anything that helps, this high up."
            "She seems to take the silence as a compliment. Her wings beat harder. You go higher."
    show cg bai_harpy_mid onlayer cgl
    "She fucks you hard, the way she flies: in great beating strokes, her wings booming, each thrust lifting you higher on the up-draft and dropping you back onto her on the down."
    bai_you "\"Every time you— every time you flap— {i}ahh{/i}— you go {i}deeper{/i}— who designed this— {i}AHH{/i}—\""
    "The forest wheels under you, all of it, endless in every direction. There's no edge. There's no road. You can see that very clearly from up here, which is the worst possible moment to learn it."
    bai_you "\"There's no— there's no {i}end{/i} to it— {i}nnh{/i}— it just goes on— oh {i}god{/i}, so do you—\""
    bai_you "\"Stop— {i}nnh{/i}— stop it up here— {i}ahh{/i}— don't— don't stop— NO—\"" with vnfx("shake")
    vn_th "(You wanted to be carried. Technically this is being carried.)"
    show cg bai_harpy_peak onlayer cgl
    "You come in her talons high over the forest, shouting into the wind, your cock spurting into empty air, and she shrieks and floods you and keeps beating her wings."
    bai_you "\"{i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "She doesn't stop at one. The ridge goes past twice more before she's done with you."
    jump bai_ch4_after

## ---- ch 5: the kobold band. Uncalled ------------------------------------------------------------------
label bai_kobolds:
    $ bai.fit = "scraps"   # in the coat and wrap until they strip him (the 2026-11-13 art walk)
    $ vn_enter(bg="bai_cabin", pc="alarmed", pc_tag="bai_pc", cast=[], cg="bai_kobolds_arrive")
    "A knock. Then the door. Six kobold women, scaled, horned, tails swishing, grown and grinning and absolutely thrilled to be here, every one of them hard."
    "\"She's here, she's here!\" \"Smells so good, look, she's got the tail and ears already!\" \"Kobold queen. She's really here.\""
    bai_you "\"Oh, fucking hell. I turned it {i}off.{/i} The dial's at zero. Look. Zero. You can all go home.\""
    "They can smell you through the walls. Zero isn't zero any more."
    menu:
        "The kobold band, in the doorway."
        "Bar the door":
            $ bai.shout5 = "bar"
            "You get the door half shut. Six of them lean on it, giggling, and the door wins the argument for them."
        "Point at the dial":
            $ bai.shout5 = "dial"
            bai_you "\"ZERO. See? Zero! That means no! It's on the panel!\""
            "\"Pretty panel,\" says one, admiringly, and walks straight through it."
    $ bai.fit = "nude"
    show cg bai_kobolds_strip onlayer cgl
    "They're on you in a giggling heap, small clever hands everywhere, the coat off, the wrap off, your chest out and squeezed and admired."
    "\"Look at them!\" \"Bigger than the dryad's!\" \"Not yet. Not yet. Give her a week.\""
    bai_you "\"Hands off— stop— that's my— those aren't for— {i}hey{/i}—\""
    show cg bai_kobolds_hands onlayer cgl
    "Two of them at your chest, mouths on your nipples, sucking hard. One with her hand round your cock, pumping it. One already lining up behind you, rubbing herself in the slick the warg left you with."
    bai_you "\"No— not all at— there's {i}six{/i} of you— {i}nnh{/i}— I'm one person—\""
    show cg bai_kobolds_gang onlayer cgl
    "Most of the night. One in your mouth, one behind, two at your chest, the others waiting their turn and cheering each other on like it's a sport."
    "\"She's so warm inside!\" \"My turn, my turn!\" \"You just {i}had{/i} a turn!\" \"She doesn't mind! Do you mind, queen?\""
    bai_you "\"I mind— {i}mmph{/i}— I mind {i}enormously{/i}— {i}hahh{/i}— get your {i}tail{/i} out of my— oh god, is that a {i}tail{/i}—\""
    "It's not a tail. It's the second one, behind the first, and the first one hasn't finished."
    bai_you "\"{i}Mmh{/i}— no— that's— {i}hahh{/i}— six is TOO MANY— {i}nnh{/i}— stop—\""
    show cg bai_kobolds_relay onlayer cgl
    "They take turns in a giggling relay. When one finishes in you, another's already there. When the one in your mouth pulls out, the next one's cock is at your lips before you can get a word out."
    "\"Queen's turn!\" \"No, my turn, I've been so good—\" \"She's so {i}stretchy{/i}—\""
    "\"Look at her hold it all.\" \"Like she was made for us.\" \"She was made for us, silly, that's the whole point.\""
    bai_you "\"I'm not— I'm not your— {i}mmph{/i}— queen— {i}ahh{/i}—\""
    show cg bai_kobolds_chest onlayer cgl
    "One of them climbs up and ruts between your swelling breasts, squeezing them round her cock with both hands, and comes across your chin, and the others cheer."
    bai_you "\"Get— get off my— {i}mmph{/i}— that's not a— those aren't a {i}toy{/i}—\""
    "\"They're {i}our{/i} toy,\" she says, happily, and squeezes harder."
    vn_th "(You lost count. Somewhere around the fourth one you lost count of them and of yourself.)"
    show cg bai_kobolds_dawn onlayer cgl
    bai_you "\"{i}Ahh{/i}— no— not another— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "At dawn they leave a neat heap of shiny stones on the table, as a thank-you, and file out the door arguing happily about who was best."
    "You lie on the floor drenched, too wrung out to move, and laugh at the ceiling."
    jump bai_ch5_after

## ---- ch 6: the dryad. Fed for hours; he breaks ---------------------------------------------------------
label bai_dryad:
    $ bai.fit = "nude"
    $ vn_enter(bg="bai_oldgrowth", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_dryad_meet")
    bai_you "\"Room for one more?\""
    "Her eyes open, green as new leaves. Her voice is honey and mulch, and it comes from the whole grove at once."
    "\"Hungry thing. Come here.\""
    "You kneel at her roots. She takes your face in a hand the size of a shovel, gently, and guides your mouth to her cock."
    bai_you "\"Wait— that's not— I meant food—\""
    show cg bai_dryad_sap onlayer cgl
    "\"It is food.\" And it is: the sap that beads at her tip is thick and sweet and the most nourishing thing you've tasted since you woke in the dirt. Your hunger eclipses everything. You drink."
    "\"Drink up, sweet thing. Hungry things get fed. Open up, Bait.\""
    bai_you "\"No— I'm not— I'm not hungry— {i}mmh{/i}— {i}mmph{/i}—\""
    "You are. You drink from her cock until your belly's warm and full, and a vine curls round your chest and toys with your swollen nipples while you do."
    show cg bai_dryad_feed onlayer cgl
    "Then she draws you up into her lap with roots like arms, and puts your mouth to her breast, and it's sweeter still, and her cock nudges up between your cheeks, slick with sap."
    "\"Starving thing. Good roots need good soil, don't they? Show me how you grow.\""
    bai_you "\"I'm not— I'm not soil— I'm a person— {i}mmh{/i}— with an exit strategy—\""
    "\"Mm. Soil says that, at first.\""
    show cg bai_dryad_impale onlayer cgl
    "She lowers you onto her, slow, patient, a root under each of your thighs, until you're sitting in her lap full of her, her milk in your mouth."
    bai_you "\"{i}Mmh{/i}— no— I came for— {i}hahh{/i}— not this— {i}ohh{/i}—\""
    menu:
        "In the dryad's lap."
        "Hold on to 'no'":
            $ bai.break6 = "hold"
            bai_you "\"No— {i}mmh{/i}— no, I'm not— I'm not saying it—\""
            "You hold on to the word as long as you can. It isn't very long."
        "Let it go":
            $ bai.break6 = "let"
            "Somewhere in the second hour, the fight just goes out of you, quietly, like a candle."
    show cg bai_dryad_mid onlayer cgl
    "She feeds you while she takes you, for hours. Sap-sweet milk in your mouth, her cock moving slow in you, branches bracing your back and fondling every part of you, the old trees creaking round you like a choir."
    "\"There. Taking root at last. Do you feel it? You were always going to come here, sweet thing. Everything comes to the old growth eventually.\""
    bai_you "\"I came for— {i}mmh{/i}— for food— {i}ahh{/i}— for {i}margin{/i}— I had a {i}plan{/i}—\""
    "\"And now you have a meal. Which is better than a plan.\" She rocks you in her lap like a cradle, slow, deep, and you can't argue, because your mouth is full of milk again."
    "She brings you to the edge, and holds you there, and refills your mouth every time you falter."
    bai_you "\"Please— no— please— I don't know which— {i}mmh{/i}— which one I mean any more—\""
    "\"Both, sweet thing. You mean both. Drink.\""
    show cg bai_dryad_edge onlayer cgl
    "\"Not yet. Drink. There. Good.\""
    bai_you "\"Please— please— I can't— I need—\""
    $ bai.broke = True
    show cg bai_dryad_peak onlayer cgl
    bai_you "\"{i}Ahh{/i}— more— don't stop— feed me— {i}fuck me{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "When it comes it's long and gushing and slow, and she fills you as deep as she can reach, and curls you into her lap afterwards still inside you, and nurses you softer."
    show cg bai_dryad_sleep onlayer cgl
    "The gentlest and longest of all of them. You sleep in her roots, full, with your mouth still at her breast."
    jump bai_ch6_after
