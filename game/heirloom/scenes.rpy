## heirloom's sessions, ch 1-7. IT HAS TO SET: the team, then Kaede, keep going past his no, never
## threatening, never hurting; it's tradition, it's for him, it has to set. The choice when he protests is
## what he says or does, never whether. Ch 1-5 non-con; ch 6 he breaks into begging; ch 7 the flip.

## ---- ch 1: the dare. They pull it on him -----------------------------------------------------
label hrl_dare:
    show cg hrl_pulled_on onlayer cgl
    "Miki has your left arm, Haruna your right. Nao kneels and tugs your shorts and boxers down past your knees, apologising the whole time, and the cold March air hits everything."
    hrl_you "\"Hey— HEY— let go— this isn't funny any more—\""
    "Rei lifts the skin out of the trunk. It's heavy and warm, and it moves in her hands like it's breathing."
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Foot.\""
    hrl_you "\"No!\""
    "She doesn't argue. She waits until your weight shifts, threads it over one foot, then the other, and draws it up your calves. It clings like nothing synthetic ever has: soft, close, almost human."
    "Up your thighs. Over your knees. The girls lift you by the arms so she can work it over your hips, and the opening slides round your waist and lies flush against your belly."
    $ hrl_body(1)
    show cg hrl_seal onlayer cgl
    "Someone whistles. They see the seal take before you feel it: the line round your waist vanishing, the seams smoothing into you, the surface sculpting itself tight below the hipbones."
    "Then it presses your cock and balls flat, and with a dizzy shiver draws them away inside, as if they'd never been there."
    hrl_you "\"What the— what did you— get it OFF—\"" with vnfx("shake")
    "They let go of your arms. Your hand goes straight to your crotch. Nothing there. Smooth, right down to a slit, wet folds parting under your fingertips."
    "An impossible pulse clenches up through you and wetness runs over your wrist. The team cheers. Miki gets one photo before Rei captain-voices the phone away."
    "You claw at the waistband that isn't there any more. It won't come away. It's sealed like it grew on you."
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"It's stuck? Guess it fits!\""
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"Yuu? Are you okay?\""
    hrl_you "\"No! I'm not okay! Take it off me!\""
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Take your time. We'll see how long you last.\""
    jump hrl_ch1_night

## ---- ch 1: Rei comes back. The first time -------------------------------------------------------
label hrl_rei_returns:
    "There's a click at the door."
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg=None)
    "Rei, in the doorway, with that calm captain's smile. She shuts the door and sits beside you on the bench, her knee against yours."
    hrl_rei "\"It's not a prank. Not really. That's the club's real ritual.\""
    hrl_rei "\"The skin picks someone every few years, and it grows around them. From the anchor up. Hips, belly, tits, all of it, one region at a time. But first the anchor has to set, and it only sets by being used.\""
    hrl_you "\"Then I won't use it. I'll wait it out.\""
    hrl_rei "\"You'll last an hour. Less. Hold off and it gets hungrier.\""
    "Her hand goes to your knee. Then the inside of your thigh."
    menu:
        "Rei's hand."
        "Tell her to stop":
            $ hrl.shout1 = "stop"
            hrl_you "\"Don't. Rei, stop, I didn't say you could—\""
        "Close your knees":
            $ hrl.shout1 = "knees"
            "You clamp your knees together. She draws them apart again with one hand, unhurried, like stretching a teammate's hamstring."
            hrl_you "\"Rei— no— I said no—\""
    show cg hrl_rei_lockers onlayer cgl
    hrl_rei "\"It has to be used, Yuu. That's all this is.\""
    "She takes both your wrists in one hand and pins them to the locker door over your head. Not hard. Just certain."
    "Two fingers slide into the new folds, and your whole body jumps."
    hrl_you "\"{i}Hah{/i}— no— take it out— Rei, take it— {i}nnh{/i}—\""
    "She sets a slow rhythm and curls up to stroke something inside that makes your thighs shake. Her thumb finds your clit and circles it."
    hrl_rei "\"Listen to you. It's taking to you so fast.\""
    hrl_you "\"It's not— I'm not— {i}ahh{/i}— stop— don't stop— no— I mean STOP—\"" with vnfx("shake")
    show cg hrl_rei_peak onlayer cgl
    "Her palm grinds down. Your hips buck off the bench into her hand, and the lockers ring with it."
    hrl_rei "\"Good girl.\""
    hrl_you "\"{i}AHH{/i}— Rei— {i}Rei{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You come so hard the new cunt clamps round her fingers and pulses, gushing over her hand and the bench. Rei holds you through every wave of it, and when it's done she doesn't let go of your wrists until you stop shaking."
    "And the hunger isn't gone. It's already knotting up again, emptier than before."
    jump hrl_ch1_after

## ---- ch 2: setting the anchor. The all-hands on the bench -----------------------------------------
label hrl_setting:
    show cg hrl_bench_strip onlayer cgl
    "Miki's behind you before you can turn. Your shirt is up over your head, your arms caught in it, and Nao's hands are at your waistband."
    hrl_you "\"Hey— HEY— cut it out—\""
    "Shorts gone. Nao sits on the bench behind you and pulls you back into her lap, her arms round your chest, her knees hooked inside yours so your legs stay open."
    hide hrl_rei
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"Shh. Just relax. You can take it, okay?\""
    hrl_you "\"I don't want to take it! Nao, let me up—\""
    menu:
        "Nao's arms."
        "Fight her grip":
            $ hrl.shout2 = "fight"
            "You heave. She's a long-jumper; her legs are stronger than yours ever were, and she just holds on, warm and patient, until you're out of breath."
        "Plead with Rei":
            $ hrl.shout2 = "plead"
            hrl_you "\"Rei. Rei, come on. Call it off. You're the captain, call it off.\""
            hide hrl_nao
            show hrl_rei calm at vn_cast_slot
            hrl_rei "\"I am the captain. That's why it's being done properly.\""
    show cg hrl_bench_fingers onlayer cgl
    "Rei kneels between your thighs. \"Miki, lube.\" The bottle's already open. Rei's fingers slide in slick and slow, and Miki's join them, and you lose count of how many."
    hrl_you "\"Stop— stop it— {i}hah{/i}— that's too— {i}nnh{/i}— get OUT—\""
    "Miki's mouth replaces Rei's hand: broad greedy strokes over your clit, her nose pressed to the mound."
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"He loves it.\""
    hrl_you "\"I don't! I don't— {i}ahh{/i}— I don't—\""
    show cg hrl_bench_strap onlayer cgl
    "A bright pink harness comes out of the club's box. Miki buckles it on with a sprinter's speed, and the toy juts glossy and proud."
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Been waiting all afternoon for this, rookie.\""
    hrl_you "\"No— Miki— not that— don't you DARE—\""
    "She presses the tip to you and feeds it in, careful and teasing, shallow, then deep. You've never felt anything like it: stretched, filled, everything inside you clutching at it."
    hrl_you "\"{i}Ohh{/i}— no— take it— take it out— {i}hahh{/i}—\""
    "Miki ruts you with an athlete's rhythm. Rei guides her hips and keeps your knees wide. Nao kisses your ear and tells you you're doing so well."
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"He's clamping like a vice! Come on, take it. It's not set unless we really use you.\""
    hrl_you "\"I'm not— {i}nnh{/i}— I'm not— oh god— don't stop— NO— I mean—\"" with vnfx("shake")
    "You come with a wail that rings off the gear racks, clamping down so hard Miki grunts."
    show cg hrl_bench_rounds onlayer cgl
    "They don't let you recover. Nao, slower, softer. Haruna, quick snaps of her hips. Miki again. Then Rei herself, straddling you and holding your hips down."
    hrl_team "\"That's it, again— He's not going anywhere— Listen to him—\""
    "Somewhere in the third round the protesting changes. You don't notice when. Nobody remarks on it."
    hrl_you "\"{i}Ahh{/i}— Rei— please— please— {i}more{/i}— {i}RE-I{/i}—!\"" with vnfx("flash", "shake")
    show cg hrl_bench_set onlayer cgl
    "When it's over you're boneless on the mat. Rei kneels and runs a finger round your swollen folds with a coach's pride."
    hide hrl_miki
    hide hrl_nao
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"It's set. I can see it.\""
    "And you can feel it: the place where the new skin meets yours, buzzing, like a border that won't stay where it's put."
    hide hrl_miki
    hide hrl_nao
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Kaede comes back next month to claim you properly. For now, job done.\""
    jump hrl_ch2_after

## ---- ch 3: hips. Over the bench, between drills ---------------------------------------------------
label hrl_hips_bench:
    $ vn_until(18)
    $ vn_enter(bg="hrl_equipment", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg=None)
    "Post-drills. You head for the showers the long way round. Miki and Nao head you off at the field-house door, one on each arm, and steer you into the equipment room."
    hrl_you "\"I'm not on your schedule. I'm going home.\""
    hrl_miki "\"Bench, rookie. Let's see how close we are to winning Rei's pool.\""
    show cg hrl_hips_bench onlayer cgl
    "Sitting down is different now: there's more of you to sit on. Nao settles behind you and holds you by the new hips, her thumbs tracing circles. Miki nudges your knees apart and works your shorts down past a curve they weren't cut for."
    "What was left of your flat runner's ass is gone: a flush of muscle and plush skin, flared hips, dimples where thigh meets cheek."
    hrl_miki "\"You're leaking on my shoes.\""
    menu:
        "Miki, between your knees."
        "Shove at her head":
            $ hrl.shout3 = "shove"
            "You shove at her head. Nao gathers your wrists and folds them gently across your own chest."
            hide hrl_miki
            show hrl_nao gentle at vn_cast_slot
            hrl_nao "\"Let her have you.\""
        "Try to stand":
            $ hrl.shout3 = "stand"
            "You try to stand. Nao's arms lock round your waist and sit you back down."
            hrl_you "\"Let me UP— I'm not doing this every day—\""
    show cg hrl_hips_tongue onlayer cgl
    "Miki's tongue spreads you open and you thump your head back against Nao's collarbone."
    hrl_you "\"No— no, no— {i}hahh{/i}— I said— {i}nnh{/i}—\""
    "Two fingers, then three. She works you like a drill set, fast and precise, and the bench creaks with it."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Look at that, you've got Kaede's hips already.\""
    hide hrl_miki
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"That's a compliment, Yuu.\""
    hrl_you "\"It's NOT— {i}ahh{/i}— stop— Miki, stop— please— don't— don't stop— no— STOP—\"" with vnfx("shake")
    show cg hrl_hips_peak onlayer cgl
    "Nao's hand slides down your belly to your clit and circles it fast, and the new ass flexes, lifting off the bench to chase Miki's hand."
    hrl_you "\"{i}AHH{/i}— {i}Miki{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "It drags your hips taut to the bench and goes on and on, the anchor fluttering and refusing to let go."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"That's a conversion if ever I saw one.\""
    jump hrl_ch3_after

## ---- ch 4: the waist. The locked room, unlocked ---------------------------------------------------
label hrl_waist_mouth:
    $ vn_enter(bg="hrl_equipment", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_nao", "worried")], cg=None)
    "Nao steps in with her kit bag, worried. Miki's behind her twirling the spare key on one finger."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Rei's got a meeting all night. Track's empty. Thought you'd want company, now you've got a cute waist too.\""
    hrl_you "\"I don't. I locked the door for a reason. Get out, both of you.\""
    show cg hrl_waist_mouth onlayer cgl
    "Nao comes round behind you anyway and wraps her arms round your middle, and her palms find the new inward curve of your waist. Miki kneels and peels your shorts down."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"New skin's climbing, isn't it? All that's left down here is this tummy.\""
    menu:
        "Miki's mouth, a breath away."
        "Push her away":
            $ hrl.shout4 = "push"
            "You push at her shoulders. Nao catches your hands and holds them flat against your own belly."
            hrl_you "\"I came in here to wait it out! Not this!\""
        "Grip the bench and refuse":
            $ hrl.shout4 = "grip"
            hrl_you "\"I'm not saying it. I'm not asking you. Whatever you do, I'm not asking.\""
            hide hrl_nao
            show hrl_miki grin at vn_cast_slot
            hrl_miki "\"Didn't ask you to ask.\""
    "Miki licks a slow line from your entrance to your clit, and your hips jerk forward into her mouth on their own."
    hrl_you "\"No— {i}ah{/i}— that's not me, that's— the skin— {i}hahh{/i}— stop—\""
    hide hrl_miki
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"You're changing so beautifully. We're so proud of you.\""
    show cg hrl_waist_peak onlayer cgl
    "Miki seals her lips round your clit and pushes two fingers in, curling up, and doesn't let up when you buck. Nao's hand on your belly feels the waist draw in under it."
    hrl_you "\"Please— please stop— {i}nnh{/i}— please— don't— don't you dare stop— NO— I mean—\"" with vnfx("shake")
    hrl_you "\"{i}AHH{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You squirt. You can feel it go, all over Miki's chin and palm, and she giggles in triumph and doesn't slow down."
    "A second one rolls in behind the first, and this time you feel the muscle above your hips draw tight and settle, the waist smaller, the belly smoothing soft."
    "By the third you're not making words. They lower you onto the mat."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Region set. Pay up, Nao: fifteen hundred yen. I said midweek.\""
    jump hrl_ch4_after

## ---- ch 5: Kaede's claiming ----------------------------------------------------------------------
label hrl_kaede_claim:
    $ vn_until(21)
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_equipment", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_kaede", "smirk")], cg=None)
    "The team files out after dinner, glancing back. Rei squeezes your shoulder and shuts the door, and leaves you with Kaede and the smell of chalk."
    hrl_kaede "\"Lose the hoodie.\""
    hrl_you "\"No.\""
    "She smiles, crosses the room in three strides and lifts it off you herself, the way she'd strip a wet jacket off a teammate after a downpour. Your shorts sit wrong now, stretched over hips far too round for your frame."
    hrl_kaede "\"Spread for me, recruit. I want to feel you remember.\""
    hrl_you "\"I'm not a recruit and I don't remember anything. I didn't sign up for you.\""
    hrl_kaede "\"You didn't have to. The skin signed up years ago.\""
    show cg hrl_kaede_mouth onlayer cgl
    "She sits you on the end of the padded bench and drops to her knees between your legs. Her palms run up your hips like she's checking her own handiwork."
    "Her mouth on the fabric where you press out, and the wet heat of her tongue through the stretch. Wetter than any hand has ever made you."
    hrl_kaede "\"Ahh. Still dripping at the sound of my voice. Feel it climb? Closer to the ribs every second I play you.\""
    menu:
        "Kaede, on her knees."
        "Kick away from her":
            $ hrl.shout5 = "kick"
            "You try to kick back along the bench. One broad hand spans both your hips and holds you exactly where you are."
            hrl_you "\"Let go of me— get your hands off—\""
        "Tell her it won't work":
            $ hrl.shout5 = "deny"
            hrl_you "\"It's not climbing. It's not doing anything. You can stop, it's not going to work on me.\""
            hrl_kaede "\"Look down, then.\""
    "She peels the shorts down without pausing when they catch on your hips, and her tongue splits you like someone tasting her own ghost."
    "Above you she murmurs, \"Look down. Watch the star come back,\" and you look, and you can see it: the line where hers joins yours, flexing, crawling upward."
    hrl_you "\"No— no, it's moving— make it stop— {i}hahh{/i}—\""
    show cg hrl_kaede_takes onlayer cgl
    "Kaede rises and frees her cock: thick, heavy, dark against her thighs. She strokes it once, unhurried."
    hrl_kaede "\"You need this deeper than you think, sweet thing. That's how it climbs hardest.\""
    hrl_you "\"Don't— Kaede, don't— that's too big, I don't want—\""
    "Her palm on your breastbone presses you flat on the bench. She lines up and pushes in, slow and inexorable as the tide, thicker and longer than anything the team strapped on."
    hrl_you "\"{i}OHH{/i}— no— no— it's too— {i}hahh{/i}— get it out—\"" with vnfx("shake")
    "The spread turns explosive. You feel it: a pulse between belly and chest, the seam going liquid and rising on every stroke."
    show cg hrl_kaede_pin onlayer cgl
    "She hooks your legs over her shoulders and drives deeper. Your hands go to your own chest without you sending them, as if they expect breasts there already. She catches your wrists and pins them above your head."
    hrl_kaede "\"Want it set? Want me to fuck you till you're her?\""
    hrl_you "\"NO— no— I don't— {i}ahh{/i}— don't stop— no— I mean STOP— {i}nnh{/i}— please—\""
    hrl_kaede "\"Then come for me, star. Push it up your body.\""
    show cg hrl_kaede_peak onlayer cgl
    hrl_you "\"{i}AHH{/i}— {i}KAEDE{/i}— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    "You break first, hips snapping up, screaming. She buries herself to the root and comes deep inside you, heat flooding you as if she's sealing a contract."
    "And you feel it go up. Ribs softening, muscle shifting, something rising in you like it's laughing."
    hrl_kaede "\"You're almost there. I'm not going anywhere till you're finished. Every stage, all of it.\""
    hrl_you "\"I can still pass.\""
    "She laughs, deep and certain, and you feel the truth seeping up through your ribs."
    jump hrl_ch5_after

## ---- ch 6: the club bath. He breaks partway through ---------------------------------------------
label hrl_bath_buds:
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_bath", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_nao", "gentle")], cg="hrl_bath_reveal")
    "Steam. The team peeling out of kit in practical silence. You hold out a beat too long, then strip the hoodie off with your arms locked round your chest."
    "They see straight away. Faint swellings, pink-capped, pushing forward under your nipples and jiggling with every breath."
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Oh holy— he's BUDDING! Rei, you owe me five hundred!\""
    "Hands close on you from behind, pinning your elbows and turning you to the light. Across the bath Kaede lounges on the bench, towel gone, grinning."
    hrl_you "\"Don't look— stop looking— let go of my arms—\""
    hide hrl_nao
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"It's really climbing.\""
    "Rei runs her thumb under the new fold of flesh. You shudder so hard your hips jerk forward, and the anchor floods."
    show cg hrl_bath_mouths onlayer cgl
    "Nao kneels and her mouth closes on your right nipple. Miki takes the left without a word. Rei holds you up from behind, her hands under your ribs."
    hrl_you "\"No— not there— {i}hahh{/i}— it's wired to— {i}ahh{/i}— it goes straight down— stop—\""
    "It is. Every flick of a tongue fires straight to your cunt. Nao's fingers slide in below and you clench round them on every suck."
    hide hrl_miki
    hide hrl_rei
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"Sensitive? You get wet every time I do this?\""
    menu:
        "Two mouths, Nao's hand."
        "Hold on to 'no'":
            $ hrl.break6 = "hold"
            hrl_you "\"No— no— I'm not— I'm not saying it—\""
            "You hold on to the word for as long as you can. It's not very long."
        "Let it go":
            $ hrl.break6 = "let"
            "Somewhere between one suck and the next, the fight just goes out of you."
    $ hrl.broke = True
    hrl_you "\"{i}Ahh{/i}— Nao— do that again— please— {i}please{/i}—\""
    "The rest close in: a tongue in the crease under one breast, fingers rolling the other, someone at your hip. Your knees go and Rei and Nao hold you up so the others can keep at you."
    hrl_you "\"Please— someone— s'too much— Nao— need you, need you inside, please—\""
    show cg hrl_bath_peak onlayer cgl
    "Nao sinks between your thighs and buries her mouth in you, and reaches up to pinch both nipples in time."
    hide hrl_nao
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Let them have you. The club only blooms when you do.\""
    hrl_you "\"{i}AHH{/i}— {i}yes{/i}— {i}yes{/i}— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    "You lose count after that. When they finally let you slump, your left breast has gone from a bud to a full handful, and the right is catching up as you watch."
    jump hrl_ch6_after

## ---- ch 7: the camp. The relay; on the fourth night, he asks -------------------------------------
label hrl_camp_relay:
    $ hrl.fit = "yukata"
    $ vn_enter(bg="hrl_lodge_room", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_futon_rows")
    "After the bath the futons go down in the old two-row sprawl. Rei dims the lights and announces: \"Rotation.\""
    "You lie at the far end and tell them you're going to sleep. Nao and Miki come down the row anyway, every night, and every night you say no and every night it lasts a little less long."
    show cg hrl_relay_nao onlayer cgl
    "Nao behind you, her hand under your yukata stroking the soft belly and lower. Miki between your legs, tasting what Nao's fingers bring up."
    hrl_you "\"Not again— I'm so— {i}nnh{/i}— oh— {i}oh{/i}— fine— fine— don't stop—\""
    "On the second night it's Kaede, straddling you in the dark, and you only say her name."
    show cg hrl_relay_kaede onlayer cgl
    hide hrl_rei
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"Look at you. Two more nights and you'll fill out that club jacket.\""
    hrl_you "\"{i}Ahh{/i}— Kaede— {i}KAEDE{/i}—!\"" with vnfx("flash", "shake")
    hide cg onlayer cgl
    "On the fourth night nobody comes down the row. Rei's clipboard says rest."
    "You lie awake in the dark with the anchor aching and your new breasts heavy under the yukata, listening to them breathe."
    menu:
        "The futon row, in the dark."
        "Crawl to Nao":
            $ hrl.camp = "nao"
            $ vn_enter(bg="hrl_lodge_room", pc="begging", pc_tag="hrl_pc", cast=[("hrl_nao", "gentle")], cg="hrl_futon_ask_nao")
            "You crawl down the row on your hands and knees and slide in under Nao's quilt. She wakes with a hum."
            hrl_you "\"Nao. Please. I want it. I'm asking. I want you to.\""
            hrl_nao "\"I know. I've been waiting for you to say it.\""
        "Crawl to Rei":
            $ hrl.camp = "rei"
            $ vn_enter(bg="hrl_lodge_room", pc="begging", pc_tag="hrl_pc", cast=[("hrl_rei", "soft")], cg="hrl_futon_ask_rei")
            "You crawl down the row on your hands and knees to the captain's futon. Rei's awake. Of course she's awake."
            hrl_you "\"Rei. Put me on the schedule. Tonight. I'm asking.\""
            hrl_rei "\"You've been on it since March. But say it again.\""
            hrl_you "\"Please. I want it.\""
    $ hrl.asked = True
    "It's slow, and it's the first time you've said yes out loud, and you don't stop saying it."
    hrl_you "\"Yes— yes— {i}there{/i}— don't stop— don't you {i}dare{/i} stop— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    hide cg onlayer cgl
    jump hrl_ch7_after
