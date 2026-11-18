## THE STORY: chapters 0-2 (PLAN.md). The guild; the gate and Mireille's heart-shot; floor 1, Glaze (SOFTENED); floor 2,
## Verbena (PARALYSED). One floor a day, one ailment a floor, the change shows that night (dbf_grow before the night's vn_enter).
## Status lines are gold ({color=#ffd36b}); changes are pink ({color=#ff5fb8}).

## ---- 0. Monday: the guild, the gate, floor one -------------------------------------------------------------------

label dbf_guild:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_guild", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_ottilie", "calm")], cg="dbf_appraisal")
    "The guild hall at nine in the morning smells of coffee, oiled leather and somebody's burnt toast."
    "You stroll in down the middle of it in your battle dress: white and violet, the bodice armoured, the skirt short enough to fight in, thigh boots, your rapier at your hip."
    "Every head in the hall turns. Every head always does."
    "Tirysia, twenty-two, the guild's best blade three years running."
    "You wear a dress because it looks better on you than on anyone, and you've beaten every adventurer in this hall who ever said a word about it."
    "Ottilie is at the appraisal desk: forty-odd, spectacles on a chain, a crystal lens the size of a dinner plate in front of her. She doesn't look up."
    dbf_ottilie "\"Hand.\""
    "You lay your palm on the lens. It lights up, and lines of gold script crawl across it."
    "{color=#ffd36b}TIRYSIA. LEVEL 41. STATUS: CLEAR.{/color}"
    dbf_ottilie "\"Clear. As always. You're the only adventurer I've ever appraised who's never once come back with an ailment.\""
    dbf_you "\"I don't catch them. They try. I shake them off by supper.\""
    dbf_ottilie "\"Mm.\" She pushes a sealed contract across the desk."
    dbf_ottilie "\"The Spire of Velune. Ten years unclimbed. Seven floors, seven guardians, a succubus at the top. Three parties have gone up. All three came down a week later, very happy and very quiet, and none of them has ever picked up a sword again.\""
    dbf_ottilie "\"Every guardian in there lands an ailment, Tirysia. And in that spire, they don't wear off.\""
    dbf_you "\"Then I'll just have to not get hit.\""
    $ vn_set_time(15, 0)
    $ vn_enter(bg="dbf_gate", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_mireille", "smirk")], cg="dbf_the_gate")
    "The Spire of Velune stands alone on a moor two hours out of town: pink stone, seven storeys, windows lit from inside though nobody lights them."
    "The gate is open. Above it, in the air, a woman appears: a shimmer at first, then solid enough to count the eyelashes. Curling horns. Bat wings folded like a cloak."
    "A spade-tipped tail swaying behind her. A body that makes you forget, for a second, what you came for."
    dbf_mireille "\"Oh, look at {i}you.{/i} The famous Tirysia. They didn't tell me you'd be so pretty.\""
    dbf_you "\"Mireille, I take it. I'm here for your spire.\""
    dbf_mireille "\"And I'm here for you, sweetheart. Seven floors. I'll be waiting at the top. Here: something to remember me by.\""
    show cg dbf_heart_shot onlayer cgl
    "She blows you a kiss. It leaves her lips as a heart: pink, glowing, the size of your palm, drifting toward you slow as a soap bubble."
    "You've seen a hundred spells. You've never seen one like this. It's almost {i}sweet.{/i}"
    menu:
        "The heart drifts closer."
        "Sidestep the heart":
            "You sidestep it, easy. It turns in the air and follows you. You step again; it follows again, lazy, patient. You laugh and duck under it and turn to say something clever to her—"
            "—and it touches the back of your neck, and bursts, warm as a mouthful of wine."
            $ dbf.wary += 1
        "Touch the heart, just to see":
            "You know better. You do. But you've never seen anything like it, and it's so slow, and it's so pink, and you just want to know what it {i}does.{/i}"
            "You reach out and touch it with one fingertip. It bursts, warm as a mouthful of wine, all the way up your arm."
            $ dbf.curious += 1
    "{color=#ffd36b}STATUS: CHARMED.{/color}"
    "That's all. A warm glow in your chest. A pleasant fizz behind your eyes. You've had worse from a strong cider."
    dbf_mireille "\"See you soon, Tirysia.\""
    "She's gone. You walk in through the gate. You meant to walk in anyway. You're fairly sure you meant to."
    $ vn_set_time(15, 30)
    $ vn_enter(bg="dbf_cistern", pc="curious", pc_tag="dbf_pc", cast=[("dbf_glaze", "smirk")], cg="dbf_glaze_rises")
    "Floor one is a cistern: a long vaulted hall, knee-deep in clear water, lit blue from somewhere under it."
    "The water in the middle rises up and up and becomes a woman: clear blue all through, curvy and glossy, her breasts and hips wobbling as she stretches, her face all cheerful bright eyes."
    dbf_glaze "\"Ooh! A new one! And a pretty one! I'm Glaze. Come here and let me look at you.\""
    "You draw your rapier. Your feet walk you toward her."
    "That's odd. You meant to circle. You meant to keep three paces off and wait for her to commit."
    "Instead you're wading straight up to her, step after step, and your heart's going, and she's {i}so{/i} pretty—"
    dbf_glaze "\"There we go. Mireille's charm. It walks you right to us. Isn't it lovely?\""
    show cg dbf_slime_swallow onlayer cgl
    "She opens her arms and folds you into her, and her body closes round you to the waist, cool and thick and slick, and slides under your skirt."
    "Then she's round your cock, all of it at once, a cool tight wet grip that {i}moves,{/i} and a slick tendril of her pressing between your cheeks and seeping in."
    vn_sfx "Gupu. Nuchu. Nuchu."
    dbf_you "\"Hah— wait— ahh♡— that's— oh, that's {i}inside—\""
    menu:
        "She's all round you."
        "Hack at the slime":
            "You stab her. You stab her again. Your rapier goes into her like a spoon into jelly and she giggles and closes over the blade and pulls it gently out of your hand."
            dbf_glaze "\"Aww. You're cute when you fight.\""
            $ dbf.fought += 1
        "Let it settle":
            "You mean to fight. You do. But she's cool and soft and she's doing something to your cock that nothing has ever done, and your sword arm just... lowers."
            dbf_glaze "\"Good. Just let me settle. I'll do all the work.\""
            $ dbf.gave += 1
    show cg dbf_slime_milk onlayer cgl
    "She works you: the grip round your cock pulsing, the tendril in your arse thickening and pushing deeper, slow, finding the spot inside that makes your knees go."
    "Her slime soaks your whole body under the dress, cool and tingling, seeping {i}into{/i} your skin."
    "{color=#ff5fb8}It tingles everywhere she touches. The hair on your arms and legs and belly dissolves away into her.{/color}"
    "{color=#ff5fb8}Your skin goes smooth, then smoother: glassy, soft, like the skin of someone who's never been in a fight. Your face warms, and rounds, just a touch, at the cheeks.{/color}"
    "{color=#ff5fb8}Your waist softens under her hands.{/color}"
    vn_sfx "Jupu. Jupu. Gupu."
    dbf_you "\"Ahh♡— ahh— don't— don't stop, don't stop— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come into her, hard, and she glows brighter blue round you and wobbles with delight, and for a long moment you forget there's a spire, or a sword, or a you."
    dbf_glaze "\"Mmm. Delicious. Okay! Off you go. Mireille wants you seasoned, not stuck.\""
    "She spits you out onto the steps at the far end, soaked and gasping."
    "You grab your rapier off the floor and give her one hard thrust on your way past, right through the middle, and she bursts into a splash and pools away into the water."
    "One down. You climb, legs shaking. You won that. You're nearly sure you won that."
    $ dbf_grow(1)
    $ dbf.fit = "torn"
    $ vn_set_time(21, 0)
    $ vn_enter(bg="dbf_waystone", pc="dazed", pc_tag="dbf_pc", cast=[], cg="dbf_first_waystone")
    "The landing above floor one has a waystone: a tall crystal, faintly humming, warm to the touch. Every floor has one, the old reports said. A place to rest."
    "The guardians can't cross onto the landings."
    "You strip off your soaked, torn dress and look at yourself in the crystal's polished face."
    "{color=#ff5fb8}Smooth. All of you, everywhere: no hair on your arms, your legs, your belly, nothing but skin like warm silk that shines in the crystal's light. Your face is a shade rounder, a shade softer at the cheek. Your waist dips in a touch more than it did this morning.{/color}"
    "{color=#ffd36b}STATUS: CHARMED. SOFTENED.{/color}"
    dbf_you "\"...Softened. Huh. It'll be gone by morning.\""
    "You lay the dress over the waystone and sleep against it. In the night the enchantment on the dress hums and knits it whole again, the way it always does."
    call dbf_cut(7, 1, "Tuesday. Floor two.")
    jump dbf_tuesday

## ---- 1. Tuesday: floor two, Verbena ---------------------------------------------------------------------------------

label dbf_tuesday:
    $ dbf.fit = "dress"
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_morning_one")
    "It isn't gone by morning."
    "Your skin is still silk. You run your palm down your own forearm three times before you make yourself stop."
    "The dress has mended, and it sits a hair tighter at the waist than it ever has, as if the enchantment's measured you again in the night."
    "{color=#ffd36b}STATUS: CHARMED. SOFTENED.{/color}"
    "And the charm's still there too: a warm fizz under your breastbone, and a pull toward the stairs up, like a hand on your back."
    dbf_you "\"Fine. Up we go. I was going up anyway.\""
    $ vn_set_time(10, 0)
    $ vn_enter(bg="dbf_garden", pc="cocky", pc_tag="dbf_pc", cast=[("dbf_verbena", "smirk")], cg="dbf_verbena_blooms")
    "Floor two is a hothouse: glass roof, steaming air, flowers the size of carriages. In the middle of it, the biggest flower of all opens its petals, and a woman rises out of its heart."
    "Pink-skinned, bare, full-breasted, her hair a mass of petals, her lower half lost in the flower. Vines coil round her and out across the floor."
    "Golden pollen drifts round her like smoke."
    dbf_verbena "\"Glaze said you were pretty. Glaze undersold it. I'm Verbena, darling. Come and smell the flowers.\""
    "She breathes out, slow, and a cloud of gold rolls toward you across the floor."
    menu:
        "The pollen's coming."
        "Hold your breath and charge":
            "You fill your lungs and charge, rapier out, straight through the cloud. It's a good plan. It's a very good plan, right up until a vine catches your ankle and you gasp."
            $ dbf.wary += 1
        "Take a curious sniff":
            "It smells like honey and summer and something under it you can't name. Just one sniff. You want to know what it is."
            "You find out."
            $ dbf.curious += 1
    "{color=#ffd36b}STATUS: CHARMED. SOFTENED. PARALYSED.{/color}"
    "Your arms go heavy. Then your legs. Then all of you, warm and slow and limp as a cat in a sunbeam, and your rapier slides out of your fingers and rings on the tiles."
    show cg dbf_vines_lift onlayer cgl
    "Her vines lift you off your feet and carry you to her, and lay you back across her petals with your thighs spread."
    "One slips up your skirt and round your cock, flowering open into soft wet petals that close round it and {i}suck.{/i} Another, thick and slick with nectar, presses into your arse and slides deep."
    vn_sfx "Nuru. Nuchu. Chupu."
    dbf_you "\"Ahh— ah♡— can't— can't move— ohh, that's deep— ahh♡—\""
    dbf_verbena "\"You don't need to move, darling. Flowers don't. Just open.\""
    menu:
        "You can still, just, move your fingers."
        "Tear the vines":
            "You get your fingers round a vine and pull. It's like pulling on a warm silk rope. She laughs and lets you, and slides another one in beside the first."
            $ dbf.fought += 1
        "Go limp in them":
            "You let your fingers go slack. It's so much easier. Everything is so warm and so slow and your arse is so full."
            dbf_verbena "\"There. Isn't that nicer?\""
            $ dbf.gave += 1
    show cg dbf_nectar onlayer cgl
    "She leans down over you and kisses you, slow, and her mouth is full of nectar, sweet and thick, and it runs over your lips and down your chin."
    "Two slim vines find your nipples through the bodice and latch on, sucking."
    "{color=#ff5fb8}Your lips tingle where the nectar touched them, then swell: fuller, softer, plump and pink.{/color}"
    "{color=#ff5fb8}Your nipples tingle under the vines' mouths and puff up, rounder, darker, more sensitive with every pull.{/color}"
    "{color=#ff5fb8}The vines round your hips squeeze, rhythmic, and your hips give under them, and flare out wider.{/color}"
    vn_sfx "Chuu. Chuu. Nuchu. Nuchu."
    dbf_you "\"Mmh♡— my lips— my— ahh, my nipples— AHHH♡— I'm— I'm going to—!\"" with vnfx("flash", "shake")
    "You come into her petals and they drink it all, and she sighs like a woman in a warm bath."
    dbf_verbena "\"Lovely. Off you go, then. Upstairs.\""
    "The pollen thins. Your arms come back, slow."
    "You get your rapier and you cut through the stem of her flower on your way to the stairs, clean, and she folds down into her petals with a sleepy laugh."
    "Two down."
    $ dbf_grow(2)
    $ dbf.fit = "torn"
    $ vn_set_time(21, 30)
    $ vn_enter(bg="dbf_waystone", pc="flustered", pc_tag="dbf_pc", cast=[], cg="dbf_second_waystone")
    "The second waystone. You peel off the dress and look."
    "{color=#ff5fb8}Your lips: full and pink and soft, a pout you didn't have yesterday, glossy as if you've just licked them.{/color}"
    "{color=#ff5fb8}Your nipples: puffy, swollen, standing up on your chest like a pair of ripe berries.{/color}"
    "{color=#ff5fb8}And your hips: the bones are where they were, but there's more of you over them, a soft new curve between your waist and your thighs.{/color}"
    "{color=#ffd36b}STATUS: CHARMED. SOFTENED. PARALYSED.{/color}"
    "You touch your lips with a fingertip, and the paralysis stirs: a warm heaviness in your arms, just for a breath, at your own touch."
    dbf_you "\"...That's going to be inconvenient.\""
    call dbf_cut(7, 1, "Wednesday. Floor three.")
    jump dbf_wednesday
