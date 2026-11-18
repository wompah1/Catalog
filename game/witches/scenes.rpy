## witches' director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, then the passage after,
## which lands the climax one beat inside the act. Lines from witches.js's pools (setup.witchesLines:
## each witch's own; setup.slPcLines.witches1-6: his protest, betray and break). All six non-con
## and none ever flips (the owner, 2026-10-27): partners never ask, hands and ailments only, no
## threats, no tears, no pain. One struggle menu in each, for flavour, never whether.

## Rung 1, the ward bed: Bryony rides him; Charm pushes his hips up into her. (Witches Ward Four Sex;
## lead Bryony, straddle, missionary, noncon, pool witches1)
label wit_ward_four_sex:
    $ vn_enter(bg="wit_ward_four", pc="outraged", pc_tag="wit_pc", cg="wit_one_open")
    $ wit.fit = "nude"
    show cg wit_one_open onlayer cgl
    "\"Oh, bless him.\" Bryony rolls her hips, slow, and sinks all the way back down onto you. {i}Kii, kii,{/i} goes the old iron bed."
    wit_you "\"I'm ON SHIFT— get— OFF—!\""
    menu:
        "{i}Kii, kii.{/i}"
        "Grab the bedframe and haul yourself out":
            "You grab the iron bedframe over your head and haul. You get about an inch up the mattress. She sinks straight back down. {i}Kii, kii.{/i}"
        "Blow the whistle":
            "You get the whistle to your mouth and blow it, hard. {i}PHWEEEET.{/i} It rings down the whole length of Ward Four. Bryony claps."
            show wit_bryony amused at vn_cast_slot
            wit_bryony "\"Ooh. Again.\""
        "Read her her rights":
            wit_you "\"You do not have to— {i}ahh{/i}— this is a council SITE—\""
            "She nods along, riding you, delighted."
    show cg wit_one_mid onlayer cgl
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Charmed right through and still fighting it.\""
    "She strokes your cheek with one fingertip and rides you faster."
    wit_you "\"Northcott Security— you're— {i}ahh{/i}— trespassing—!\""
    "\"Look at your hips, lovely. They know where they're going.\" They push up into her, and she sighs, delighted."
    wit_you "\"Why are my— stop moving my HIPS—! That's not me— that's NOT me pushing up— that's the— {i}ahh{/i}— Charm—!\""
    show cg wit_one_peak onlayer cgl
    "Bryony blows you a kiss from right on top of you, and your hips jump up into her on their own. \"Ooh. There you go.\""
    wit_you "\"Stop— stop smiling at me— every time you smile my— {i}hnn{/i}— my HIPS—!\"" with vnfx("shake")
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"There's a lovely sound. Again.\""
    "She grinds down and holds you deep inside her."
    wit_you "\"get— OFF— {i}ahh{/i}— nnh— I'm on— SHIFT—!\""
    jump wit_ward_four_after

## Rung 2, the porter's chair: Rowena on his lap; Silence until the first moan breaks it; then no on
## every stroke, his own hands pulling her down. (Witches Linen Room Sex; lead Rowena, straddle,
## noncon, pools witches2s then witches2)
label wit_linen_room_sex:
    $ vn_enter(bg="wit_linen", pc="flushed", pc_tag="wit_pc", cg="wit_two_open")
    show cg wit_two_open onlayer cgl
    "\"Ooh, he's cooking.\" Rowena slams down into your lap, and the old porter's chair goes {i}creak, creak{/i}."
    "Your mouth works. Nothing comes out."
    menu:
        "Not a sound."
        "Shove at her shoulders":
            "You shove at her shoulders with both hands. She rocks back, laughing, and drops straight back into your lap. {i}Creak.{/i} \"Oi. Nobody said you could leave.\""
        "Try to shout for Rufus":
            "You try to shout for Rufus. Not a sound. Rowena shouts it for you, \"RUFUS!\", and cracks up."
        "Swear at her":
            "You try to swear. Silence. Rowena laughs for you."
    show cg wit_two_mid onlayer cgl
    "You yell \"GET OFF\" right in her face, and the only noise in the linen room is the chair."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Look at him go, he can't stop!\""
    "She laughs right in your face and rides you harder. Your mouth opens on a no and nothing comes out, not even breath. Your hips buck up into her anyway."
    "Your mouth is wide open and silent and your whole body is shaking under her."
    show wit_pc breaking
    show cg wit_two_peak onlayer cgl
    "—{i}AHH{/i}—!"
    "It rings off the shelves. The first moan, and it's broken the Silence clean in half." with vnfx("shake")
    wit_you "\"No— no— nnh—! No— get OFF— no— {i}no{/i}—!\""
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Still hard? Course you are.\""
    "She squeezes round you and laughs till she snorts. Her hat falls off. She leaves it."
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Hands on my hips, sweetheart. Oh, look, they already are.\""
    wit_you "\"Stop pulling her— hands, STOP—!\""
    jump wit_linen_room_after

## Rung 3, the desk: wrists pinned in one hand, his face in her breasts; Slow makes even his bucking
## slow. (Witches Nurses Station Sex; lead Cressida, straddle, noncon, pool witches3)
label wit_nurses_station_sex:
    $ vn_enter(bg="wit_nurses", pc="outraged", pc_tag="wit_pc", cg="wit_three_open")
    show cg wit_three_open onlayer cgl
    "\"Hold still, gorgeous. Slow suits you.\" Cressida rolls her hips at her own slow pace, and your bucking comes up to meet her slow as syrup."
    wit_you "\"Mmph— put me— DOWN—!\""
    menu:
        "Her hand round your wrists."
        "Pull your wrists free":
            "You pull. Her hand round your wrists doesn't move. Her hips do. Slow. Slower. \"Mm.\""
        "Kick the desk":
            "You kick. Slowly. Your boot drifts up and taps the side of the desk sometime next week, and a chart slides off onto the floor."
            show wit_cressida amused at vn_cast_slot
            wit_cressida "\"Mm.\""
        "Yell for Rufus":
            wit_you "\"Mmph— RUFUSH— mmph—!\""
            "It goes into her breasts and stays there."
    show cg wit_three_mid onlayer cgl
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Mm. Yell into those, they don't mind.\""
    "Her breasts press down over your face, warm and heavy, and your yelling goes straight into them."
    wit_you "\"Mmf— get— OFF— mmph—! Nnf— I'm— on SHIFT— mmph—!\""
    "Old charts slide off the desk under you with every roll of her hips. Cressida doesn't look at them."
    wit_you "\"Mmph— shtop— shtop movin'— mmh—!\""
    "Your hips come up to meet her, slow as syrup."
    show cg wit_three_peak onlayer cgl
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"You're bucking, gorgeous. Very slowly.\""
    "She sounds almost impressed. Her spectacles swing on their chain and tap your forehead. {i}Tik. Tik.{/i} She rides you in time to them."
    wit_you "\"Mmmh— {i}mmmh{/i}— mmph—!\"" with vnfx("shake")
    "You're yelling into her breasts and it comes out a moan."
    jump wit_nurses_station_after

## Rung 4, the couch: wrists ribboned to the rail; Elspeth rides him facing away; a come on every
## touch; her finger in him from the third beat. (Witches Exam Room Sex; lead Elspeth, straddle,
## noncon, pool witches4)
label wit_exam_room_sex:
    $ vn_enter(bg="wit_exam", pc="flushed", pc_tag="wit_pc", cg="wit_four_open")
    show cg wit_four_open onlayer cgl
    "\"Again? You've gone again!\" Elspeth claps her hands and doesn't stop bouncing."
    wit_you "\"No— nnh— not ag— {i}ahh{/i}—!\""
    menu:
        "The ribbon round your wrists."
        "Yank at the ribbon":
            "You yank. The rail rattles. The bow holds, soft and snug as anything, and Elspeth wiggles on you, giggling, in time to the rattle."
        "Order her to untie it":
            wit_you "\"Untie me— that's an ORDER— untie— {i}ahh{/i}—!\""
            "\"Ooh, an order!\" She's so pleased she bounces."
        "Kick your heels":
            "You drum your heels on the couch. It shakes salt off the end of it. Elspeth giggles and brushes your hip with one fingertip, and you come apart again."
    show cg wit_four_mid onlayer cgl
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Shall I do the feather? I'm doing the feather.\""
    "The quill's feather drifts across your nipple, and your whole body jumps against the ribbon."
    wit_you "\"Don't— don't TOUCH— {i}ahh{/i}, I'm— again—!\""
    "She rides you facing away, her bum bouncing, and looks back over her shoulder, giggling. \"Your {i}face{/i}!\""
    show cg wit_four_peak onlayer cgl
    "\"In and out, in and out.\" Her slick finger works in your arse while she rides you, and she giggles every time you squeal."
    wit_you "\"No— not THERE— that's— nobody's EVER— {i}ahh{/i}—!\"" with vnfx("shake")
    "Her finger crooks inside you. \"Found it!\" She's so pleased with herself she bounces."
    wit_you "\"No— no— every— every TOUCH— {i}hnnngh{/i}—!\""
    jump wit_exam_room_after

## Rung 5, the bed rail: bent over it, his trousers at his knees; he begs on her order, because
## Obedient makes him, swearing between every please that he doesn't mean it. (Witches Side Ward Sex;
## lead Isolde, anal, doggy, inside, noncon, pool witches5)
label wit_side_ward_sex:
    $ vn_enter(bg="wit_side_ward", pc="breaking", pc_tag="wit_pc", cg="wit_five_open")
    show cg wit_five_open onlayer cgl
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Beg.\""
    "And you do, out loud, before your mouth can stop it."
    wit_you "\"Please— please— I don't mean it— please—!\""
    menu:
        "Her hand flat between your shoulder blades."
        "Push up off the rail":
            show wit_isolde amused at vn_cast_slot
            wit_isolde "\"Hold.\""
            "Your body holds, bent over the rail, and takes the whole length of her."
        "Swear at her between the pleases":
            wit_you "\"Please— you absolute— please— you complete— {i}please{/i}—!\""
            show wit_isolde amused at vn_cast_slot
            wit_isolde "\"Again.\""
        "Shout the site rules":
            wit_you "\"SECTION FOUR— please— no interfering with the— please—!\""
            "Isolde's hand lies flat between your shoulder blades. {i}Pap. Pap. Pap.{/i} Nothing else."
    show cg wit_five_mid onlayer cgl
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Again.\""
    vn_sfx "{i}Pap pap pap.{/i}"
    "She drives into you over the rail."
    wit_you "\"Please— that's not ME saying— please—!\""
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Arch.\""
    "Your back arches. Her next stroke goes deeper."
    wit_you "\"Please— no— why is it— nobody's even TOUCHING it— please—!\"" with vnfx("shake")
    "Your cock spurts against the rail on its own."
    show cg wit_five_peak onlayer cgl
    show wit_isolde amused at vn_cast_slot
    wit_isolde "\"Louder.\""
    "Your voice goes up on its own."
    wit_you "\"PLEASE— I don't— mean a WORD— please—!\""
    jump wit_side_ward_after

## Rung 6, the matron's bed. MANDATORY: his legs over Morgause's shoulders, every ailment at once;
## "Look at me."; the violet comes in ring by ring while the coven calls it, and never touches; no and
## please in the same breath; the hold beat before the fork. (Witches Matron Sex; lead Morgause,
## anal, missionary, inside, noncon, pool witches6)
label wit_matron_sex:
    $ vn_enter(bg="wit_matron", pc="breaking", pc_tag="wit_pc", cg="wit_six_open")
    show cg wit_six_open onlayer cgl
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"Look at me.\""
    "You look. You have to. Her violet eyes, and in yours, the violet coming in."
    wit_you "\"No— please— no— {i}please{/i}—!\""
    $ _wit_r = WIT_RINGS[0]
    "{color=#c48cf0}[_wit_r]{/color}"
    menu:
        "Her violet eyes."
        "Try to look away":
            "You try. Your eyes stay right where she put them. \"There we are.\" She rolls into you, slow and deep, your legs up over her shoulders."
        "Shove at her shoulders":
            "You get both hands on her shoulders and shove. Your ankles are on them. Neither of them moves. She smooths your hair off your forehead with one warm hand and keeps going, slow, unhurried, all the way in."
        "Tell her she's trespassing":
            wit_you "\"Northcott— no— you're tres— {i}please{/i}—!\""
            show wit_morgause amused at vn_cast_slot
            wit_morgause "\"There we are.\""
    show cg wit_six_mid onlayer cgl
    $ _wit_r = WIT_RINGS[1]
    "{color=#c48cf0}[_wit_r]{/color}"
    show wit_rowena amused at vn_cast_slot
    wit_rowena "\"Halfway!\""
    "From the end of the bed."
    wit_you "\"No— no— please— I'm not— no—!\""
    $ _wit_r = WIT_RINGS[2]
    "{color=#c48cf0}[_wit_r]{/color}"
    show wit_elspeth amused at vn_cast_slot
    wit_elspeth "\"Ooh, his ears!\""
    "Bouncing on her heels."
    show wit_morgause amused at vn_cast_slot
    wit_morgause "\"Sing for the ward.\""
    "And you do, at the top of your voice."
    wit_you "\"No— {i}please{/i}— it's going off again and nobody's— no— please—!\"" with vnfx("shake")
    "Your cock spurts on your belly, untouched."
    show cg wit_six_peak onlayer cgl
    $ _wit_r = WIT_RINGS[3]
    "{color=#c48cf0}[_wit_r]{/color}"
    show wit_bryony amused at vn_cast_slot
    wit_bryony "\"Look how soft he's gone.\""
    "Hands clasped under her chin."
    show wit_cressida amused at vn_cast_slot
    wit_cressida "\"Mm. Nearly.\""
    "Dry, from the desk."
    show wit_niall grin at vn_cast_slot
    wit_niall "\"Told you, Em.\""
    "From the doorway, grinning his old grin."
    wit_you "\"Please— no— my EYES— no— {i}please{/i}—!\""
    $ _wit_r = WIT_RINGS[4]
    "{color=#c48cf0}[_wit_r]{/color}"
    "{color=#c48cf0}{b}The last ring hangs. It's waiting on you.{/b}{/color}"
    jump wit_matron_after
