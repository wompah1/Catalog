## shrine's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, a speech choice, mid, peak, then
## the passage after, which lands the climax. Lines from shrine.js's pools: the guardians'
## (SHRINE_FLINT_NC, SHRINE_SLATE_NC, setup.slCombatLines) and the PC's (setup.slPcLines.shrine,
## shrineHips, shrineVoice, shrineEnd), keyed by act. Rungs 2 to 6 are non-con by compulsion and none
## flips: the choice is what you shout, never whether. The ending's scene is the route's one flip.
## Flint pins and holds; nobody threatens.

## ---- RUNG 1: the solo scene, as a Hold-it-still loop ------------------------------------------
## (main.twee :: Shrine Hands Solo, DoL's possessed masturbation.) Each round: one of her lines, one
## of yours, and the choice. She winds you up a step every round whatever you do; letting her winds
## you another. Holding can win a round (SHR_WILL of them), never the scene: at SHR_HEAT_TOP the only
## way on is the finish.
label shr_hands_solo:
    $ shr.turn = 0
    $ shr.heat = 0
    $ shr.will = SHR_WILL
    $ shr.held = 0
    $ shr.let = 0
    $ vn_enter(bg="shr_room", pc="possessed", pc_tag="shr_pc", cast=[], cg="shr_solo_slow")

label shr_hands_round:
    $ shr.turn += 1
    $ _lady = SHR_HANDS_LADY[(shr.turn - 1) % len(SHR_HANDS_LADY)]
    $ _you = SHR_HANDS_PC[(shr.turn * 3) % len(SHR_HANDS_PC)]
    if shr.heat >= 6:
        show cg shr_solo_close onlayer cgl
        $ _cap = "You're close. They know it. She knows it."
    elif shr.heat >= 3:
        show cg shr_solo_slick onlayer cgl
        $ _cap = "Both hands now, slick and quick. Both hers."
    else:
        $ _cap = "Your right hand round your cock, slow. Hers."
    shr_lady "[_lady]"
    show shr_pc furious
    shr_you "[_you]"
    menu:
        "[_cap]"
        "Hold them still":
            $ shr.heat += 1
            if shr.will > 0:
                $ shr.will -= 1
                $ shr.held += 1
                show cg shr_solo_held onlayer cgl
                if shr.held == 1:
                    "You lock every muscle you've got. Your right hand stops, mid-stroke, shaking, for one whole breath. You did that. You {i}won{/i} that."
                    shr_lady "\"Oh, well done.\""
                    "Then your left hand takes over."
                elif shr.held == 2:
                    "You clamp your wrist against your thigh. It stops. It actually stops, and you laugh out loud at it, breathless—"
                    shr_lady "\"Mm. Cute.\""
                    "—and your thumb starts circling the head instead, which is worse."
                else:
                    "You hold it still. You hold it so still your arm cramps, and for a whole long breath nothing moves but your cock, twitching on its own in your fist."
                    shr_lady "\"It doesn't need your hand, darling. Look at it.\""
            else:
                show shr_pc possessed
                if shr.turn % 3 == 0:
                    "You hold. They don't. {i}Shlk. Shlk.{/i}"
                elif shr.turn % 3 == 1:
                    "You try to hold them still. They're not even listening any more."
                else:
                    "You haul on your arm with everything you've got, and your arm keeps stroking, slow, and you're the only one getting tired."
        "Let them":
            $ shr.heat += 2
            $ shr.let += 1
            show shr_pc flushed
            if shr.let == 1:
                "You let them. Just for one stroke. Just to get your breath back."
                "One stroke turns into ten."
            elif shr.let == 2:
                "You stop fighting. Only for a second."
                shr_lady "\"Oh, {i}there{/i} you are.\""
            else:
                "You yell at your own wrists. Your wrists don't care. {i}Shlk. Shlk. Shlk.{/i}"
    if shr.heat >= SHR_HEAT_TOP:
        show shr_pc possessed
        "You're there. You're right there, and your hands won't stop, and she won't {i}let{/i} them stop.\n{size=-5}{color=#ff8fa3}▸ Come{/color}{/size}"
        jump shr_hands_finish
    jump shr_hands_round

## ---- RUNG 2: your legs --------------------------------------------------------------------------
## (rungs.twee :: Shrine Legs Sex; lead Slate, crew Flint, thighs, lock, noncon, pool shrine; nothing
## in your mouth, no anal.) Slate between your squeezed thighs, Flint in your left hand.
label shr_legs_sex:
    $ vn_enter(bg="shr_gate_dusk", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_legs_open")
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Tighter, Lady? Tighter. Lovely.\""
    "Your thighs squeeze on him, and you yell at them."
    shr_you "\"Put me DOWN— that's my— that's my LEG— {i}hnngh{/i}—!\""
    "Your left hand keeps on at Flint, slow and expert, root to tip, thumb over the head, the way it did to you last night."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Hold still.\""
    menu:
        "Slate between your thighs. Flint in your fist. Your legs and your hands, hers."
        "Order them both off":
            $ shr.say2 = "demand"
            shr_you "\"Let GO of me— both of you— and you, get OUT of my head—!\""
            "Your thighs squeeze tighter. Your fist speeds up on Flint."
            show shr_slate grin at vn_cast_slot
            shr_slate "\"Don't look at me, she's the one doing it.\""
        "Plead with them":
            $ shr.say2 = "plead"
            shr_you "\"Make her stop— you can make her stop, can't you— {i}please{/i}—!\""
            "Flint looks at you for a long moment, your hand still working him."
            show shr_flint flat at vn_cast_slot
            shr_flint "\"Gate's shut.\""
        "Scream for anybody":
            $ shr.say2 = "scream"
            shr_you "\"SOMEBODY— anybody— there's a FOX in my— {i}ahh{/i}—!\""
            "The heather doesn't answer."
    show cg shr_legs_mid onlayer cgl
    vn_sfx "{i}Shlk. Shlk. Shlk.{/i}"
    "Slate rocks up between your thighs from behind, slick now, every stroke dragging along the underside of your balls, the head of him nudging out the front of your skirt."
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Evening, Lady. Brought him down again?\""
    "He laughs into your neck and keeps rocking."
    show shr_pc flushed
    shr_you "\"Why's it— why does it feel— stop MAKING it feel—!\""
    "Your thighs clamp on him again. You didn't do that."
    shr_lady "\"Oh, he's big. He was always big.\""
    shr_you "\"Why am I HARD— it's not me— it's NOT— {i}nnh{/i}—!\""
    "Your own cock bobs under the skirt, so hard it aches, and nobody touches it. Not him, not her, not you. Your hands are busy."
    show cg shr_legs_peak onlayer cgl
    "Slate's breath goes ragged in your ear. Flint's hips start to push into your fist. Your legs hold you there between them, braced, and your thighs squeeze in time."
    shr_you "\"Okay— okay okay okay— just let me— let me {i}come{/i}, you bloody— {i}AHH{/i}—!\"" with vnfx("shake")
    jump shr_legs_after

## ---- RUNG 3: your mouth -------------------------------------------------------------------------
## (rungs.twee :: Shrine Mouth Sex; lead Flint, crew Slate, oral, inside, noncon, pool shrine; no
## anal.) Flint in your mouth from the start, Slate in your hand.
label shr_mouth_sex:
    $ vn_enter(bg="shr_gate_dusk", pc="possessed", pc_tag="shr_pc", cast=[], cg="shr_mouth_open")
    vn_sfx "{i}Glk. Glk.{/i}"
    "A big hand cups the back of your head and keeps it there."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Hold still.\""
    "Your right hand finds Slate without asking you and wraps round him, stroking, while your head bobs on Flint."
    shr_you "\"{i}Mmf{/i}— {i}mmh{/i}— MMF—!\""
    "Your protests come out round him, wet and muffled."
    menu:
        "Flint in your mouth. Slate in your fist. Your jaw, hers."
        "Snarl round him":
            $ shr.say3 = "growl"
            "You get your mouth off him for one breath and snarl at the stars. Your fangs show. In your head, {shr}she's delighted{/shr}."
            shr_lady "\"Open.\""
            "Your jaw drops, and your head goes back down."
        "Mock them":
            $ shr.say3 = "mock"
            "You wrench your mouth back far enough to talk."
            shr_you "\"You're both— {i}hah{/i}— you're both carvings, you know that? Garden ornaments—!\""
            "Slate laughs so hard your fist slips on him. Flint's hand brings your head back down."
        "Apologise to the hill":
            $ shr.say3 = "apologise"
            "You pull off him, gasping."
            shr_you "\"Sorry— SORRY— I prayed for a LAUGH— I take it back—!\""
            shr_lady "\"Too late, maiden. Open.\""
            "You open."
    show cg shr_mouth_mid onlayer cgl
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Deeper.\""
    "He doesn't push. Your own neck does it for him."
    show shr_pc flushed
    shr_you "\"{i}Mmh{/i}— {i}nngh{/i}— {i}mmmh{/i}—\""
    "It's meant to be {i}that's not my noise{/i}. It comes out round him as a long wet moan, and your mouth's so sensitive that every inch of him on your tongue lands like a kiss somewhere much lower."
    shr_lady "\"Again.\""
    "Your body does it again, and you moan before you can swear."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Maiden came down.\""
    "He says it to the stars, not to you."
    show cg shr_mouth_peak onlayer cgl
    "Your little cock drips under the skirt. Your hand pumps Slate faster. Flint's hips give short, heavy bucks, his hand flat on the back of your head."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Gate's shut.\""
    vn_sfx "{i}Glk. Glk. Glk.{/i}"
    "It is. It really is."
    jump shr_mouth_after

## ---- RUNG 4: your hips; THE MANDATORY SCENE ---------------------------------------------------
## (rungs.twee :: Shrine Hips Sex; lead Flint, anal, doggy, lock, noncon, pool shrineHips.) No way
## round it and no asking to stop. Face-down on the worship-hall boards, your tail held up in your own
## fist; Flint holds your hips down when you win them back.
label shr_hips_sex:
    $ vn_enter(bg="shr_hall", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_hips_open")
    "He pushes in. Slow. Huge. Your whole body goes rigid on the boards and then gives, an inch at a time, around him."
    shr_you "\"I'm not presenting— I'm NOT presenting, that's HER presenting—!\""
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Take it.\""
    "Flat, like a fact. Your hips take it before you can argue."
    menu:
        "Flint in you. Your tail in your own fist. Your hips, hers."
        "Fight her for your hips":
            $ shr.say4 = "protest"
            shr_you "\"Get my KNEES back together— they're MINE— {i}hnngh{/i}—!\""
            "For a heartbeat you win your hips back. His hands on them settle it."
            show shr_flint flat at vn_cast_slot
            shr_flint "\"Hold still.\""
        "Order your tail down":
            $ shr.say4 = "tail"
            shr_you "\"My TAIL— why's my tail holding itself UP— put it DOWN—!\""
            "Your hand holds it higher, like a curtain, so the whole hall can see."
            shr_lady "\"There. That's how you present.\""
            shr_you "\"It is NOT—!\""
        "Plead with Flint":
            $ shr.say4 = "plead"
            shr_you "\"Please— just let me have my hands back— my hips— {i}please{/i}—!\""
            "His palm presses your shoulders to the boards, and your arse goes higher for it."
            show shr_flint flat at vn_cast_slot
            shr_flint "\"Down.\""
    show cg shr_hips_mid onlayer cgl
    vn_sfx "{i}Slap.{/i}"
    "He starts to move. Long and heavy, all the way out and all the way back in, and your hips push back to meet every one."
    show shr_pc flushed
    shr_you "\"I'm not pushing back, SHE'S pushing back—!\""
    shr_lady "\"Stop fighting, you're making my hips tired.\""
    shr_you "\"YOUR hips— they're MY hips— {i}ohh{/i}—!\""
    "{color=#ff5fb8}Under you, your useless little nub bounces on every thrust, drooling on the boards. Nobody's touching it. Nobody needs to.{/color}"
    shr_you "\"Why's it— why's my cock LEAKING— nobody's even TOUCHING it—!\""
    shr_you "\"Stop wagging— why's my tail wagging— I didn't— {i}ahh{/i}—!\""
    "Your tail's thrashing in your own fist. Your back's arched so deep your tits are flat to the floor."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Gate's shut.\""
    show cg shr_hips_peak onlayer cgl
    "His weight comes down on your back, a hand flat on your nape, and you hold still, and he gives it to you short and deep and heavy."
    shr_you "\"Deeper— no— {i}yes{/i}— don't let her stop— don't let ME stop—!\""
    shr_lady "\"Good maiden.\""
    shr_you "\"Shut UP— {i}ahh{/i}— again— AGAIN—!\"" with vnfx("shake")
    jump shr_hips_after

## Rung 4's second round, slow: Slate, already in you, doggy, non-con with the hips pool.
## (rungs.twee :: Shrine Hips Slate Sex.)
label shr_hips_slate_sex:
    $ vn_enter(bg="shr_hall", pc="flushed", pc_tag="shr_pc", cast=[], cg="shr_slate_slow_mid")
    "He goes in slow. So slow you feel every inch of him find where Flint's been, and your arse squeezes him all the way."
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Evening, Lady. Got him nice and ready for me, didn't you?\""
    shr_you "\"That's not— that's not my BACK doing that— {i}nnh{/i}— that's hers—!\""
    menu:
        "Slate in you, slow. Your tail in your fist. Your hips, still hers."
        "Mock him":
            $ shr.say4b = "mock"
            shr_you "\"Is that it? Is that— {i}ohh{/i}— is that ALL the guardian of the gate has got—?\""
            "He just goes slower."
            show shr_slate grin at vn_cast_slot
            shr_slate "\"Look at that.\""
        "Let the moan out":
            $ shr.say4b = "moan"
            "You moan so loud it rings off the gate posts. You didn't mean to. You did."
            show shr_slate grin at vn_cast_slot
            shr_slate "\"Look at that tail go.\""
        "Beg somebody to stop her":
            $ shr.say4b = "ask"
            shr_you "\"Stop— stop STOP— somebody stop her—!\""
            show shr_slate grin at vn_cast_slot
            shr_slate "\"Don't look at me, she's the one doing it.\""
            "You're the one pushing back. You know you're not."
    "He spreads you with his thumbs and watches himself go in."
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Look at that.\""
    show cg shr_slate_slow_peak onlayer cgl
    "Slow and slow and slow, until you're sobbing for breath into your folded hands and your hips are begging him on their own."
    shr_you "\"Fine— she wins— she WINS— just keep— {i}ohh{/i}— keep going—!\"" with vnfx("shake")
    jump shr_hips_slate_after

## ---- RUNG 5: your voice -------------------------------------------------------------------------
## (rungs-late.twee :: Shrine Voice Sex; lead Slate, vaginal, missionary, lock, noncon, pool
## shrineVoice.) The first vaginal, on the gate steps; every line split, yours then hers, in the same
## mouth, and she gets the end of the sentence.
label shr_voice_sex:
    $ vn_enter(bg="shr_steps", pc="furious", pc_tag="shr_pc", cast=[], cg="shr_voice_open")
    "He pushes in. All the way, slow, into the place you didn't have yesterday, and it's tight and slick and new and it takes him like it was made for it."
    shr_you "\"No— NO— {shr}fill me up, Slate{/shr}—\""
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Evening, Lady.\""
    "He kisses your mouth and can't tell which of you he's kissing."
    menu:
        "Slate in you, on the gate steps. Your mouth, both of yours."
        "Shout over her":
            $ shr.say5 = "shout"
            shr_you "\"Get OFF me— {shr}harder, Slate{/shr}— that wasn't ME— {shr}yes it was{/shr}—\""
        "Clamp a hand over your mouth":
            $ shr.say5 = "clamp"
            "You clamp your hand over your mouth. She talks through your fingers."
            shr_you "\"Stop USING my— {shr}mouth? Yes. Using it{/shr}—\""
        "Plead with Slate":
            $ shr.say5 = "plead"
            shr_you "\"Make her STOP— {shr}make me come{/shr}—\""
            show shr_slate grin at vn_cast_slot
            shr_slate "\"Which one of you said that? Say it again. Both of you.\""
    show cg shr_voice_mid onlayer cgl
    vn_sfx "{i}Slap. Slap.{/i}"
    show shr_pc flushed
    "He rolls into you, long and slow and curved, and every stroke drags the head of him across something inside you that makes your back come up off the stone."
    shr_you "\"It doesn't— {shr}it does. It feels perfect{/shr}—\""
    shr_you "\"I'm not wet, I'm— {shr}soaked, darling. Soaked through{/shr}—\""
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Look at that. Look at {i}you{/i}.\""
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Don't look at me, she's the one doing it.\""
    "Your legs lock round his back."
    shr_you "\"That's not my— {shr}it's mine now, and it likes you{/shr}—\""
    show cg shr_voice_peak onlayer cgl
    shr_you "\"Please— {shr}please{/shr}—\""
    "Both of you. The same word. The same mouth."
    shr_you "\"Inside— not inside— {shr}inside{/shr}— {i}AHH{/i}—\"" with vnfx("shake")
    jump shr_voice_after

## ---- RUNG 6: all of you ------------------------------------------------------------------------
## (rungs-late.twee :: Shrine All Sex; lead Flint, crew Slate, vaginal, doggy, lock, noncon, pool
## shrine; no anal, no DP.) Flint in your cunt from behind, Slate in your mouth.
label shr_all_sex:
    $ vn_enter(bg="shr_gate_dusk", pc="possessed", pc_tag="shr_pc", cast=[], cg="shr_all_mid")
    vn_sfx "{i}Slap. Slap. Slap.{/i}"
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Take it.\""
    "His fist in your hair, your face down on Slate, your tits swinging."
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Look at that mouth. Look at it go.\""
    shr_you "\"{i}Mmf{/i}— you bloody fox— {i}mmh{/i}— give it BACK— give me my {i}body{/i} back—!\""
    "It comes out round Slate as wet, furious noise."
    menu:
        "Flint behind you. Slate in your mouth. All of you, hers."
        "Swear at her round him":
            $ shr.say6 = "swear"
            "You call her every name you've got, round a mouthful of cock. Slate groans at the buzz of it."
            shr_lady "\"Oh, say it again.\""
        "Pull off and give orders":
            $ shr.say6 = "demand"
            "You get your mouth off Slate for one breath."
            shr_you "\"Put me down— put me DOWN, that's an order—!\""
            shr_mouth "\"Open.\""
            "You open."
        "Growl at the stars":
            $ shr.say6 = "growl"
            "You snarl at the stars round him. Your fangs show. In your head, {shr}she's delighted{/shr}."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Maiden came down.\""
    "He says it like a vow and buries himself."
    show shr_pc flushed
    shr_you "\"Stop squeezing— I'm not the one SQUEEZING— {i}ohh{/i}—!\""
    show shr_slate grin at vn_cast_slot
    shr_slate "\"Evening, Lady.\""
    "He says it to the top of your head."
    shr_you "\"That noise wasn't— {i}ahh{/i}— that wasn't ME, that was HER—!\""
    show cg shr_all_peak onlayer cgl
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Hold still.\""
    "One hand on your nape, and your whole body goes still under it, and he fucks you deep and steady through it, and Slate's hips start to jerk against your face."
    shr_you "\"I hate you— I HATE you— {i}harder{/i}— no, that was— {i}ahh{/i}—!\"" with vnfx("shake")
    jump shr_all_after

## ---- THE ENDING: the reins dropped ------------------------------------------------------------
## (rungs-late.twee :: Shrine Reins Sex; lead Flint, ride, pool shrineEnd.) The route's one flip:
## consensual. You ride him yourself, loud, in your own voice only.
label shr_reins_sex:
    $ vn_enter(bg="shr_steps", pc="flushed", pc_tag="shr_pc", cast=[], cg="shr_reins_open")
    "You sink down on him. All of it. Yourself."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Maiden came down.\""
    "He looks up at you, and for once it sounds like a question."
    shr_you "\"That's me— that's ME doing that— {i}ahh{/i}— Flint—!\""
    menu:
        "Flint under you on the gate steps. Nobody holding the reins."
        "Ride him harder":
            $ shr.say7 = "harder"
            shr_you "\"Up— push up— {i}harder{/i}, Flint—!\""
            show shr_flint flat at vn_cast_slot
            shr_flint "\"Hold still—\""
            "He starts, and you don't, and he groans and lets you."
        "Tease the gate":
            $ shr.say7 = "mock"
            shr_you "\"Is that all the gate's got? Come ON, Flint—!\""
            "He makes the noise like a laugh, deep in his chest, and pushes up into you."
        "Make him say yes":
            $ shr.say7 = "ask"
            shr_you "\"Again? Say yes. Say {i}yes{/i}, Flint—\""
            show shr_flint flat at vn_cast_slot
            shr_flint "\"Yes.\""
            "One word. The first one he's ever given you that wasn't an order."
    show cg shr_reins_mid onlayer cgl
    vn_sfx "{i}Slap. Slap. Slap.{/i}"
    "His big hands sit on your hips and don't push. They just hold on."
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Gate's open.\""
    shr_you "\"Nobody's holding the reins— nobody— it's just me— {i}ohh{/i}—!\""
    shr_you "\"Look at me, Flint— look— I'm doing it myself—!\""
    show shr_flint flat at vn_cast_slot
    shr_flint "\"Take it.\""
    "You do. All of it. Yourself."
    show cg shr_reins_peak onlayer cgl
    shr_you "\"It's my voice— it's mine— it just sounds like— {i}hahh{/i}— like HERS—!\""
    shr_you "\"Don't you dare go back to stone, Flint— not yet— not YET—!\"" with vnfx("shake")
    jump shr_reins_after
