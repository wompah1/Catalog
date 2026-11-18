## THE SOURCE: pressit's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (days-early.twee, days-late.twee, main.twee), written as beats; the director scenes
## are in scenes.rpy. The original is in catalog/docs/routes/vn-original/pressit/. No numbers: the
## louvre ratings are words, the card is fit words, cup letters only. Nobody explains the Contour, the
## heat, or why Portia is futa. Nobody gives you a girl's name.

## ---- DAY 1, the late shift (Press Opening) --------------------------------------------------

label prs_opening:
    $ prs.fit = "kit"
    $ vn_enter(bg="prs_pool", pc="smug", pc_tag="prs_pc", cast=[], cg="prs_chair_night")
    show cg prs_chair_night onlayer cgl
    vn_sfx "{i}Phweeet.{/i}"
    prs_you "\"Wall lane, that's you, OUT. Pool's closing. I don't care, OUT.\""
    "You're up on the lifeguard chair at the deep end of the university pool, red board shorts, yellow staff t-shirt, cobalt-blue hair still damp from your own lengths, whistle between your teeth, and you are, as always, the best thing in the building. You're twenty-one. You've got the chair, the whistle, and the only plant-room key the duty manager ever bothered to hand out. Life is good."
    "The last of the regulars drags himself up the ladder. The women's swim club has finished evening training and gone in to change. You can hear them through the wall: lockers banging, showers starting, somebody laughing."
    "You grin at the wall."
    hide cg onlayer cgl
    hide cg onlayer cgl  # ff 2:27 am: no picture, closing failed 4 draws (SCENES.md pressit v4)
    "You climb down. You do the closing round the way you always do it: lane ropes coiled, kickboards stacked, the poolside squeegeed in long lazy strokes, the duty manager's office light off, because he went home at eight like he always does."
    "Over the front doors, in big brushed-steel letters, it says THE VERRICK POOL. Somebody's family paid for the whole place. You've never cared who."
    prs_you "\"Keys.\""
    "You tell the empty hall, and jingle them."
    $ vn_enter(bg="prs_plant", pc="smug", pc_tag="prs_pc", cast=[], cg=None)
    "The plant room's down a short corridor behind the deep end: a steel door, PLANT ROOM — STAFF ONLY, and behind it the warm wet roar of the pumps and a wall of blue chlorine drums. Behind the chlorine drums, if you know where to squeeze, there's a louvre. Slatted. Old. Painted over on the other side by somebody who never checked. And on the other side of the louvre is the women's changing room."
    "You've known about it since forever. You've used it since forever. It's the best perk of a job that's mostly perks."
    "You let yourself in, and lock the door behind you, out of habit, and don't hear it click.\n{size=-5}{color=#ff8fa3}▸ Squeeze in behind the drums{/color}{/size}"
    $ vn_pass(10)
    jump prs_louvre

## Rung 1: the louvre. You rate in words, out loud, and say the line: "That's all they're for." (yours,
## the only time). She's behind you, delighted. The swim club is prose only and never sees anything.
label prs_louvre:
    $ vn_enter(bg="prs_plant", pc="smug", pc_tag="prs_pc", cast=[], cg="prs_louvre")
    show cg prs_louvre onlayer cgl
    "The drums are warm. The air back here tastes of chlorine and hot metal. You crouch, put one eye to the gap between two slats, and settle in."
    "Steam. Tiles. A long row of lockers, and the swim club peeling out of wet costumes and into towels."
    prs_you "\"Keeper.\""
    "A tall one with a swimmer's shoulders and a towel round her hips, stretching for the top shelf."
    prs_you "\"Pass.\""
    "Somebody's friend, shy about the mirror."
    prs_you "\"Pass, pass. Too much talking.\""
    "A redhead in the shower row, hands in her hair, back arched. You lick your lips."
    menu:
        "A redhead in the shower row."
        "\"Oh, keeper. Keeper with a bullet.\"":
            $ prs.rate = "bullet"
            prs_you "\"{i}Keeper{/i}. Oh, keeper. Keeper with a bullet.\""
        "\"Keeper. Obviously. Frame that one.\"":
            $ prs.rate = "frame"
            prs_you "\"{i}Keeper{/i}. Obviously. Somebody frame that one and hang it in the staff room.\""
        "Just whistle, low":
            $ prs.rate = "whistle"
            "You whistle, low, through your teeth. You don't even need a word for that one."
    "Your hand's on the front of your board shorts. It usually is, back here. You give yourself a slow, smug squeeze and keep up the commentary, because the commentary's half the fun."
    prs_you "\"Nice. Nice. Pass. Keeper. Look at that. Look at {i}that{/i}.\""
    "You snort."
    prs_you "\"And they all think they're here to swim.\""
    "The redhead turns round under the water. You stop breathing for a second."
    prs_you "{b}\"Yeah. That's all they're for.\"{/b}"
    "Low and pleased with yourself."
    hide cg onlayer cgl
    show cg prs_behind onlayer cgl
    "Somebody" "\"Say it again.\"" with vnfx("shake")
    show prs_pc furious
    "You go stiff. All of you. Not the good kind."
    "Somebody's standing behind you, between the drums and the door you locked. You twist round so fast you bang your head on a pipe."
    "It's a woman. A dark high ponytail, still damp. An expensive team jacket zipped to the chin, VERRICK down the sleeve in white letters. Hands in her pockets. Smiling."
    "Not angry. Not shocked. {i}Delighted{/i}. Like she's waited a long time for something and it's finally been delivered."
    "You know her. Everybody who works here knows her. Twenty-one, same as you, rich as anything, bored as anything. She swims lengths before your shift, every single day, and she has keys to everything, because her family's name is over the front doors."
    prs_you "\"Portia. Hi. Hey. This is— I was checking the—\""
    hide cg onlayer cgl
    show prs_portia amused at vn_cast_slot
    prs_portia "\"The louvre. Yes. I know. I've known for a while.\""
    "She tips her head at the gap you were glued to."
    prs_portia "\"Keeper, pass, keeper. You do it out loud. You really do it out loud.\""
    "She sounds thrilled about it."
    prs_portia "\"Come on. Office.\""
    hide prs_portia
    "She turns and walks out. She doesn't look back to see if you're following."
    "You are.\n{size=-5}{color=#ff8fa3}▸ Follow her to the office{/color}{/size}"
    $ vn_pass(5)
    jump prs_office

## Rung 1: the duty office. The offer: walk out and she says nothing, or hold still. No threat. Both
## links take the Contour; the second is you calling it blackmail out loud.
label prs_office:
    $ vn_enter(bg="prs_office", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    "The duty office is a desk, a filing cabinet, a kit cupboard with STAFF ONLY on it, and a window onto the dark pool. Portia unlocks it with her own key and switches the light on and sits on the edge of the desk, legs crossed, one trainer swinging."
    prs_portia "\"Here's the thing, [prs_pc_name]. I'm going to offer you something, and you can say no.\""
    prs_you "\"I didn't— look, you can't prove—\""
    prs_portia "\"I'm not going to prove anything. I'm not going to tell anybody anything.\""
    "She means it. You can hear that she means it, which is worse."
    prs_portia "\"That's the first option. You walk out of that door, you hand in your plant-room key on your way, and I never say a word. Not to the manager, not to the swim club. Nothing.\""
    "You stare at her."
    prs_portia "\"Or, you hold still.\""
    show cg prs_office_disc onlayer cgl
    "She takes something out of her jacket pocket. It's a little thing, a flat, smooth, skin-coloured disc, about the size of the pad of her thumb, with a hairline seam round the edge. She turns it over in her fingers so you can see it. There's nothing written on it. Of course there isn't."
    prs_you "\"For what? Hold still for {i}what{/i}?\""
    prs_portia "\"For this.\""
    "She smiles."
    prs_portia "\"On your hip. It's a Verrick Contour. I run it from my phone.\""
    prs_you "\"What does it do?\""
    prs_portia "{b}\"Hold still and find out.\"{/b}"
    "Your mouth opens. Nothing comes out. Your eyes go to the door, and back to the little disc, and back to her face, which is perfectly calm and perfectly pleased, and you realise she's already sure. She knew which one you'd pick before she came down the corridor."
    "Your cock's still half hard from the louvre. It hasn't got the message at all."
    menu:
        "The door. The little disc. Her face."
        "Hold still":
            $ prs.office = "hold"
        "\"So it's blackmail.\" (hold still)":
            $ prs.office = "blackmail"
    $ vn_pass(5)
    jump prs_kit_one

## Rung 1: the Contour goes on (the answer to "So it's blackmail." is "It isn't."), the rule said
## honestly while you're ranting, the strip, and the first fitting.
label prs_kit_one:
    $ vn_enter(bg="prs_office", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    if prs.office == "blackmail":
        prs_you "\"So it's blackmail. This is blackmail. You're blackmailing me. That's what this is.\""
        "Loudly. Like saying it loudly makes it true."
        prs_portia "\"It isn't.\""
        prs_you "\"It's {i}totally{/i}—\""
        prs_portia "\"You can still walk out.\""
        "She nods at the door. You don't move."
        prs_portia "\"See? It isn't.\""
    else:
        "You hold still."
        prs_portia "\"Good.\""
    hide prs_portia
    show cg prs_disc_on onlayer cgl
    "She slides off the desk and crouches in front of you, tugs the waistband of your board shorts down a little on the left side, over the jut of your hip bone, and presses the disc to your skin with her thumb."
    "It's warm. It sinks. It doesn't do anything you can feel, except that when she takes her thumb away, it's flush with your skin, like it grew there."
    prs_you "\"This is coercion. I want that noted. You've got me cornered in an office at night and you're—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "{b}\"It comes off in my hands or it doesn't come off.\"{/b}"
    "Very clearly, straight to your face, while you're still talking over her."
    prs_you "\"—and I'm only doing this because— what? What did you say?\""
    hide cg onlayer cgl
    show prs_portia intent at vn_cast_slot
    prs_portia "\"Strip.\""
    "She's already at the kit cupboard with her back to you."
    prs_portia "\"Everything. You're being fitted.\""
    prs_you "\"{i}Fitted?{/i}\""
    prs_portia "\"For the run. You're the subject.\""
    "She says it like it's obvious."
    prs_portia "\"Strip, subject.\""
    $ prs.fit = "nude"
    "You strip. You do it angrily, so it doesn't count. T-shirt, board shorts, all of it, onto the floor, and you stand there in the duty office naked and hard with your arms folded, glaring."
    hide prs_portia
    show cg prs_fit_one onlayer cgl
    "She comes back with the kit: a fresh pair of red board shorts and a yellow staff t-shirt out of the cupboard, still folded. She holds the shorts up against your hips. She pulls the t-shirt over your head herself and tugs it straight on your shoulders, and smooths it down your chest with both palms, slow, and her thumbs drag over your nipples on the way, and you hate how much you notice."
    $ prs.fit = "kit"
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Fits.\""
    "She has you step into the shorts and ties the cord herself, snug."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Fits.\""
    "She takes a plain white card out of her jacket and a pen, and writes. You crane to see."
    hide cg onlayer cgl
    show screen prs_card(1)
    prs_you "\"That's it? That's the whole— you're writing down that my shorts fit?\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Every time.\""
    hide screen prs_card
    "She tucks the card away."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Every time, until the run's over. Sit on the desk.\"\n{size=-5}{color=#ff8fa3}▸ Sit on the desk{/color}{/size}"
    $ vn_pass(5)
    jump prs_baseline

## RUNG 1, the first switch-on and the scene: compelled solo, non-con, no flip. The office offered the
## disc, never this: she presses it mid-sentence, holds your knees open, and the heat puts your hand
## there over your "I'm NOT—". To "You're making me" she says "Yes." Nothing goes inside the pussy.
label prs_baseline:
    $ vn_enter(bg="prs_office", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    "You sit on the desk. She sits on the other end of it, cross-legged, with her phone in one hand and the card on her knee."
    prs_you "\"Right. Right. So I've held still, and you've stuck your little thing on me, and I've had a {i}fitting{/i}, which is insane, and now I'm going home, and tomorrow we never talk about any of—\""
    "She presses the screen."
    hide prs_portia
    show cg prs_one_on onlayer cgl
    call prs_contour(True)
    call prs_heat_beat(1)
    show prs_pc flushed
    prs_you "\"Wh— WHAT—\""
    "You've got both hands down the front of your board shorts before you've decided to. There's nothing there. There's {i}nothing there{/i}, there's smooth skin and then soft lips and a little hard nub at the top that makes you yelp when your fingertip catches it."
    prs_you "\"What did you DO— where's my— what is THIS—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Shorts off.\""
    prs_you "\"I'm NOT—\""
    $ prs.fit = "nude"
    "She leans over, hooks two fingers in the waistband, and drags them down your thighs while you grab at them. They go over your knees. They go over your feet. She drops them on the floor."
    show cg prs_one_knees onlayer cgl
    "You sit there on the edge of the desk with your knees jammed together and your hands clamped between your thighs, staring down at yourself. A pussy. Pink, plump, completely bare, glistening already. Yours. On you. Instead of you."
    prs_you "\"This is insane. This is completely— you can't just— this is {i}coercion{/i}—\""
    show cg prs_one_open onlayer cgl
    "Portia puts the card down. She slides off her end of the desk and stands in front of you, puts one palm flat on each of your knees, and pushes them apart."
    menu:
        "Her palms on your knees."
        "Push your knees back together":
            "You push back. They open anyway, wide, and she holds them there, her thumbs on the insides, not hard, just {i}there{/i}, and you can't close them."
        "Grab her wrists":
            "You grab her wrists, both of them, and pull. Her wrists don't move. Your knees open anyway, wide, and she holds them there, her thumbs on the insides, not hard, just {i}there{/i}, and you can't close them."
        "Swear at her":
            prs_you "\"Get your— get your fucking HANDS off—\""
            "Your knees open anyway, wide, and she holds them there, her thumbs on the insides, not hard, just {i}there{/i}, and you can't close them."
    prs_you "\"Get OFF— let go of my— I didn't say you could—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Start.\""
    prs_you "\"I'm NOT— I'm not doing that, I'm not doing {i}anything{/i} in front of—\""
    "The heat comes up through you like a wave, and your hand goes down between your thighs on its own."
    prs_you "\"No— no, that's not— I'm not DOING this—\""
    "Your middle finger slides up through the wet, from the bottom to the top, and finds that nub, and—"
    prs_you "\"{i}Hhah{/i}—!\"" with vnfx("shake")
    "You nearly fall off the desk. It's nothing like a cock. It's like somebody plugged your whole spine straight into the end of your finger. You yank your hand away. The heat puts it straight back. You do it again, slower, and your hips jerk up off the desk into it on their own."
    prs_you "\"Stop it— make it STOP— it's the switch, it's doing it, it's not ME—\""
    show cg prs_one_mid onlayer cgl
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I know.\""
    "She lets go of one knee to pick up her pen. The knee doesn't close. It can't. She writes something on the card."
    prs_you "\"What are you WRITING—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Keep going.\""
    prs_you "\"I'm not— {i}ahh{/i}— I'm not KEEPING anything—\""
    vn_sfx "Shlk. Shlk. Shlk."
    "You keep going. Two fingers now, flat, rubbing circles over the hood, and you didn't tell them to, and the sound it makes is {i}obscene{/i}, wet and loud in the little office. Your knees spread wider under her hand. Your other hand finds the lips and pulls them open so the cool office air hits everything, and you moan out loud at that alone, and hate it."
    prs_you "\"You're making me. This doesn't— {i}ahh{/i}— this doesn't COUNT—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "{b}\"Yes.\"{/b}"
    "That's all. {i}Yes.{/i} She doesn't pretend anything. Her palm's warm on your knee and her eyes are on your fingers like she's watching a heat on the big screen, and she isn't going to stop it, and she isn't going to say it's your fault, either."
    hide cg onlayer cgl  # ff 2:27 am: no picture, one-peak failed 4 draws (SCENES.md pressit v4)
    "You go faster. You don't mean to. Your thighs are shaking. Your heels are up on the edge of the desk now, wide open, nothing hidden, and you're grinding up into your own hand and making noises you've never made in your life, high, breathy, ridiculous noises, and you can't stop."
    prs_you "\"I hate this— I HATE this— don't— {i}don't{/i} you write that down—\""
    "She writes it down."
    "Every time you slow, the heat climbs up through you and puts your hand back to work. Your fingertips slide down over your lips, all the way to the bottom, where it's hottest and wettest, and they hover there, right on the edge of slipping in—"
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Outside. Just outside, tonight.\""
    "Not looking up."
    "You whine. You actually whine. Your hand drags back up to the nub and rubs it like you're angry at it, and maybe you are."
    "Out through the office window, across the dark water, the pool's big lights are on their timer. You know that timer. You've watched it click off from the chair more times than you can remember."
    prs_you "\"Oh— oh no— oh no, it's— I'm gonna— this is coercion— DON'T you stop—!\""
    "It's out before you hear it. {i}Don't you stop.{/i} To your own hand. To {i}her{/i}."
    vn_sfx "{i}Chk.{/i}"
    "The first bank of lights clicks off. The far end of the pool goes black."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Now.\""
    show cg prs_one_cum onlayer cgl
    prs_you "\"{i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "It goes off like a fist opening. Your back arches clean off the desk. Your thighs try to clamp shut round your own hand and her palm on your knee keeps them open, and you're bucking, squirting, a hot clear splash across the inside of your thighs and the desk and the card— no, she lifts it out of the way just in time— and you're yelling something that isn't a word, and the second bank of lights goes off, and the third, and the pool goes dark, and you're still coming, twitching, gasping, slick to the knees."
    "It goes on for a long time. Longer than it has any right to."
    "When you can see again, she's let go of your knee, and she's capping her pen."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Good. That's round one.\""
    "She writes one more word."
    "You lie there on her desk with your thighs wet and your fingers wet and your face burning, {i}furious{/i}, and you think: {i}round one?{/i} And then you think: {i}whatever.{/i} You came. You came like a freight train, and you never said yes to any of it. She can write down whatever she likes. You got through it. You got away with it.\n{size=-5}{color=#ff8fa3}▸ Sit up{/color}{/size}"
    $ vn_pass(10)
    jump prs_release

## Rung 1's end: off, rung 1's growth inside the dormant check, then she keeps her word: she peels the
## Contour off while you're switched off and hands you the card. Then the skip to Tuesday evening.
label prs_release:
    $ vn_enter(bg="prs_office", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg="prs_one_off")
    show cg prs_one_off onlayer cgl
    call prs_contour(False)
    prs_you "\"Oh, thank GOD.\""
    "You grab it with both hands. It's there. Your cock. Small, a bit sticky, completely ordinary, completely {i}yours{/i}."
    prs_you "\"Thank god, thank god, thank—\""
    "And then you stop, because your hand's sliding over your belly on the way down, and it's sliding too easily."
    $ prs_body(1)
    "{color=#ff5fb8}There's no hair. None. Not on your belly, not round your cock, not on your thighs. You run a palm up your forearm. Smooth. Your shins. Smooth. Your chest. Smooth as the inside of a shell, and {i}soft{/i}, softer than any skin you've ever had, like the whole of you has been sanded down and oiled.{/color}"
    prs_you "\"Where's my— it didn't come BACK—! The hair didn't come BACK—!\""
    prs_portia "\"No.\""
    "Agreeing. Interested."
    show cg prs_one_nipples onlayer cgl
    "{color=#ff5fb8}You look down at your chest, and your nipples look back up at you, puffy, dark, sitting up off your chest like they've been sucked, each one on a soft little swell that wasn't there this morning, a puffy AA, and when your thumb brushes one you nearly come off the desk all over again.{/color}"
    prs_you "\"{i}Hhn{/i}— don't— what's wrong with my {i}nipples{/i}— why does that feel like— why does {i}everything{/i} feel like—\""
    "{color=#ff5fb8}You lick your lips and that's {i}loud{/i} too, your mouth all buzzing and swollen, and when you press your knees together the smooth insides of your thighs slide against each other and you have to grab the desk.{/color}"
    "{color=#ff5fb8}And your hand. Your right hand is sitting in your lap, fingers curled, and you realise it still knows exactly where to go. The angle. The pressure. The little circle. {i}Your fingers already know where it's best{/i}, and you haven't even got anything for them to go to any more.{/color}"
    hide cg onlayer cgl
    show screen prs_dormant(1)
    prs_portia "\"Interesting.\""
    hide screen prs_dormant
    show cg prs_peel onlayer cgl
    "She crouches in front of you again and puts her thumb on the disc on your hip, and pinches, and peels. It comes away in her fingers like nothing, a little flat warm thing, and she drops it in her jacket pocket."
    prs_portia "\"There. Off. I said I'd let you go.\""
    "She hands you the card."
    prs_portia "\"Yours. Keep it.\""
    "You stare at her. You stare at the card."
    prs_you "\"That's it?\""
    prs_portia "\"That's it.\""
    prs_you "\"I can just— {i}go{/i}?\""
    prs_portia "\"You can just go.\""
    "She holds the office door for you."
    prs_portia "\"Goodnight, [prs_pc_name].\""
    $ prs.fit = "kit"
    $ vn_pass(15)
    $ vn_enter(bg="prs_street_night", pc="smug", pc_tag="prs_pc", cast=[], cg="prs_walk_one")
    show cg prs_walk_one onlayer cgl
    "You go. You go fast. You're out of the side door and halfway down the road in the dark with your hair-free legs prickling in the night air before you start laughing, high and stupid and relieved. Some smooth skin. Some {i}nipples{/i}. Big deal. You got away with it. You got away with {i}everything{/i}."
    "The card's in your pocket. You keep putting your hand on it.\n{size=-5}{color=#ff8fa3}▸ Days of thinking about the card{/color}{/size}"
    call vn_night(8)
    $ vn_pass(prs_to_weekday(2, 8))
    jump prs_back

## ---- DAY 2, Tuesday evening (Press Back, Terms, Knees, Kit Two, Left) ------------------------

label prs_back:
    $ prs.fit = "own"
    $ vn_enter(bg="prs_room", pc="furious", pc_tag="prs_pc", cast=[], cg="prs_card_bed")
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost."
    show cg prs_card_bed onlayer cgl
    "You've had days to think about it. You've thought about it in the shower, which is a problem now, because there's no hair to hide behind and every {i}bit{/i} of you is so smooth the water slides off like oil. You've thought about it in bed, with your hand down your shorts, rubbing your nipples instead of your cock and pretending you weren't. You've read the card till the edges went soft. RED BOARD SHORTS: FITS. STAFF T-SHIRT: FITS."
    "You've told yourself you're never going back in the plant room."
    $ vn_until(20)
    $ prs.fit = "kit"
    $ vn_enter(bg="prs_plant", pc="furious", pc_tag="prs_pc", cast=[], cg="prs_back_louvre")
    "Tuesday evening you're on the chair, and the swim club finishes training, and you blow the whistle for closing, and you do the round, and your feet walk you down the short corridor to the steel door. You let yourself in. You don't lock it."
    show cg prs_back_louvre onlayer cgl
    "You squeeze in behind the drums. You put your eye to the louvre."
    "You're not even looking. That's the thing. Steam, towels, the redhead from the other night, and you're not even rating. Your hand's not on your board shorts. It's on the card in your pocket."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You came back.\""
    hide cg onlayer cgl
    show prs_portia amused at vn_cast_slot
    "She's behind you. Of course she is. Same jacket, same ponytail, same smile."
    prs_you "\"I was {i}working{/i}. This is my— I have a key, I'm allowed in here, I was checking the—\""
    prs_portia "\"The louvre.\""
    prs_you "\"The {i}pumps{/i}.\""
    "Portia looks at the louvre. She looks at you. She looks at your hand in your pocket on the card, and you take it out fast."
    prs_portia "\"Come and sit down.\"\n{size=-5}{color=#ff8fa3}▸ Sit on a chlorine drum{/color}{/size}"
    $ vn_pass(5)
    jump prs_terms

## Rung 2: her canon lines, the app, a fresh Contour. No second offer: she presses it in over his
## "Absolutely not", her hand flat on his chest against the pipework, and to "You're making me" says
## "Yes."
label prs_terms:
    $ vn_enter(bg="prs_plant", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    "You sit on a drum. She leans on the pipework opposite, phone in her hand."
    "She says it first, before anything else."
    prs_portia "{b}\"I let you go to see if you'd come back.\"{/b}"
    prs_you "\"I didn't come {i}back{/i}, I came to {i}work{/i}—\""
    prs_portia "\"You're my first long-term subject.\""
    "She turns the phone round so you can see the screen. It's an app with nothing on it but a single round button, grey, in the middle, and one word under it."
    show screen prs_app(False)
    prs_portia "\"Everybody else, it was one evening and done. You're the first one I get to keep running.\""
    hide screen prs_app
    prs_you "\"Everybody {i}else{/i}?\""
    prs_portia "\"There's a drawer of other prototypes at home.\""
    "She waves that away like it's boring."
    prs_portia "\"This is the one I like. I need the run to continue.\""
    "She takes another disc out of her jacket. Skin-coloured. A hairline seam round the edge."
    prs_you "\"No. No way. Absolutely not. Last time I had to—\""
    "You can't say it."
    prs_you "\"In front of you. I lost all my— my {i}nipples{/i} are— absolutely {i}not{/i}—\""
    hide prs_portia
    show cg prs_pinned onlayer cgl
    "She steps off the pipework and puts her hand flat in the middle of your chest, and pushes, and you go back off the edge of the drum against the warm pipes behind it, and she leans on you there."
    menu:
        "Her hand flat on your chest."
        "Grab her wrist":
            "You grab her wrist. It doesn't move."
        "Shove at her shoulder":
            "You shove at her shoulder with the heel of your hand. She doesn't move. She doesn't even lean back."
    prs_you "\"Get OFF— I said no— I said {i}absolutely not{/i}—\""
    "She tugs your waistband down on the left with her other hand, and presses the disc in with her thumb, and it sinks, warm, and it's flush. Like it never left."
    prs_you "\"You're making me.\""
    "You spit it."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Yes. Get used to that bit.\""
    "Very kindly. She takes her hand off your chest."
    hide cg onlayer cgl
    show prs_portia intent at vn_cast_slot
    prs_portia "\"You can't peel it, by the way. Don't try. It comes off in my hands, and I'm not taking it off again. Not this time.\""
    prs_you "\"So when—\""
    prs_portia "\"Not this time.\""
    "She puts her thumb on the round grey button. It goes pink. The word under it changes."
    show screen prs_app(True)
    "{size=-5}{color=#ff8fa3}▸ Brace yourself{/color}{/size}"
    hide screen prs_app
    jump prs_knees

## RUNG 2, your mouth on her, in heat, on your knees on the plant-room floor. Her cock stays unseen:
## the towel stays over your head and her hand holds it there. She comes; you don't. Non-con, no
## flip: down off the drum by the shoulder, her hand holding your head, your hands shoving at her
## thighs and getting nowhere. "Noted." (she means the card).
label prs_knees:
    $ vn_enter(bg="prs_plant", pc="flushed", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg="prs_two_on")
    show cg prs_two_on onlayer cgl
    call prs_contour(True)
    call prs_heat_beat(2)
    prs_you "\"Oh— oh {i}no{/i}— oh, it's {i}worse{/i}, why is it WORSE than last—\""
    "It is worse. Last time it was warm. Now it's wet, wet straight through, wet through the board shorts in one hot rush like you've sat in the pool, and your hips are rocking on the drum before you can stop them, grinding the seam of your shorts up into the new lips."
    prs_portia "\"Off the drum.\""
    prs_you "\"No— I'm not— I'm not getting off ANYTHING—\""
    "She takes you by the shoulder and pulls, and your legs are jelly with the heat, and you slide off the drum and land on your knees on the plant-room floor. The concrete's warm from the pumps. You try to get up. Her hand on your shoulder keeps you down."
    hide cg onlayer cgl  # ff 2:27 am: no picture, towel failed 4 draws (SCENES.md pressit v4)
    "She hooks her thumbs in the waistband of her joggers, and then stops, and pulls a pool towel off the pipe beside her instead, a big white one, and drops it over your head."
    prs_portia "\"Eyes shut, subject.\""
    prs_you "\"Get this OFF me— Portia— what are you—\""
    "In the white dark under the towel you hear her joggers come down. Then her hand's on the back of your head through the towel, holding it closed round you, and pulling you forward, and your face is pressed between her thighs, and she's warm and soft and slick and she smells like chlorine and woman and {i}sex{/i}."
    prs_you "\"No— no, I didn't agree to— get OFF— {i}mmf{/i}—\""
    "You shove at her thighs with both hands. They don't move. She just pulls your head in tighter."
    prs_portia "\"Tongue out.\""
    prs_you "\"I'm NOT— {i}mmf{/i}— I'm not putting my—\""
    show cg prs_two_mid onlayer cgl
    "Your tongue comes out. You didn't send it. It finds her. And something happens in your mouth that has never happened before in your life: it just {i}knows{/i}. The flat of your tongue, slow, from the bottom all the way up. The tip, flicking. Your lips closing round the little hard bud of her clit and {i}sucking{/i}."
    prs_portia "\"{i}Oh{/i}. Look at that. You learned me in one go.\""
    "Surprised and pleased."
    prs_you "\"I'm— {i}mmh{/i}— I'm not DOING this— my mouth's doing it, it's not ME—\""
    "You tell her pussy."
    prs_portia "\"Keep protesting. Lower— there. Mm. {i}There{/i}.\""
    vn_sfx "Shlrp. Shlrp."
    "You're eating her out in a towel tent on your knees on a plant-room floor with both your hands shoving uselessly at her thighs, and your own new pussy is clenching on nothing, gushing into your board shorts, so hot and so empty you're grinding your thighs together and whining into her."
    prs_portia "\"You're dripping. I can hear you dripping on the floor. Do you know that? Does it feel like that from in there?\""
    "Conversationally, above you."
    prs_you "\"Shut {i}up{/i}— {i}mmh{/i}—\""
    prs_portia "\"Faster.\""
    "She pulls your head in tight."
    prs_portia "\"Your mouth's better than your manners. I'd never have guessed. All that commentary through a slat and the whole time you had {i}this{/i} in you.\""
    prs_you "\"Nnf— this is— this is {i}coercion{/i}—\""
    prs_portia "\"Noted.\""
    "You can hear she means it for the card. She grinds down on your face, slow, slick."
    prs_portia "\"Suck. Harder. That's it. That's {i}it{/i}, subject.\""
    show cg prs_two_peak onlayer cgl
    "You suck. You don't want to and you suck, and then you're licking her like you're starving. Every time she moans the heat in you climbs another notch and your hips jerk at nothing. Your hands stop shoving. They're just holding on to her thighs now, and you notice, and you can't make them let go. You squirm and you moan into her and you lick and lick and lick."
    prs_you "\"Why's it— why does it— {i}mmh{/i}— stop making it feel GOOD—\""
    prs_portia "\"Oh— oh, there, don't stop, don't you {i}dare{/i}—\""
    "She comes on your face. Her thighs clamp round your head through the towel, locking you in, and her hand fists in it, and she rides your mouth through it, slow hard grinds, wet everywhere, gasping, laughing a little at the end, and you keep your tongue going the whole time because you can't make it stop." with vnfx("shake")
    "Then she lets go."
    show cg prs_two_after onlayer cgl
    "The towel comes off your head. She's already pulling her joggers up. Her cheeks are pink and her ponytail's coming loose and she looks {i}extremely{/i} pleased with herself."
    "You're still on your knees with your mouth wet and your chin wet and your board shorts soaked dark between your legs, panting, throbbing, so turned on you can't see straight."
    prs_you "\"What about— what about {i}me{/i}— please— you can't just— PLEASE—\""
    prs_portia "\"What about you?\""
    "She tucks her phone away."
    prs_portia "\"Kit cupboard. You need a fitting.\"\n{size=-5}{color=#ff8fa3}▸ Stagger after her{/color}{/size}"
    $ vn_pass(10)
    jump prs_kit_two

## Rung 2's fitting, still in heat: the same kit, FITS, written. Then she sends you out to clear the
## learner pool, and the whistle comes out high.
label prs_kit_two:
    $ vn_enter(bg="prs_cupboard", pc="flushed", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    "The duty office. The kit cupboard. You stand in front of it with your thighs pressed together and your soaked shorts clinging, while she takes a fresh pair of red board shorts off the shelf and a fresh yellow t-shirt."
    prs_portia "\"Change.\""
    prs_you "\"I'm still— it's still {i}on{/i}—\""
    prs_portia "\"I know. Change.\""
    hide prs_portia
    $ prs.fit = "nude"
    show cg prs_fit_two onlayer cgl
    "You change in front of her. Your shorts peel off you with a wet sound. She watches the new pussy, pink and swollen and shining, the way you'd watch a lane you were timing. She holds the fresh shorts up and you step into them and she ties the cord, and it pulls snug against the wet, and you moan out loud at the cord."
    $ prs.fit = "kit"
    "She smooths the t-shirt down your chest. Your nipples catch on the cotton. You moan at that too."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Fits. Fits.\""
    hide cg onlayer cgl
    show screen prs_card(2)
    "She looks out of the office window. There's somebody still in the learner pool, two of the regulars, splashing about long after closing."
    hide screen prs_card
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Go and clear them.\""
    prs_you "\"Like {i}this{/i}?\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You're the lifeguard.\""
    $ vn_enter(bg="prs_pool", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_whistle")
    show cg prs_whistle onlayer cgl
    "You go out onto the poolside with your thighs rubbing and your face burning, and you put the whistle in your mouth and blow it, and stick out your arm, and shout the thing you've shouted every shift of your life."
    vn_sfx "{i}Phweeeeet.{/i}"
    prs_you "\"No RUNNING— oh, that's NOT my voice—\"" with vnfx("shake")
    "It isn't. It comes out of you high and bright and girlish and it echoes all round the tiles, and both the regulars stop splashing and look at you."
    "You stand there with the whistle in your hand."
    prs_you "\"Pool's— closed. Out. Please. {i}Out{/i}.\""
    "High. Higher. It's not going back {i}down{/i}.\n{size=-5}{color=#ff8fa3}▸ Back to the office{/color}{/size}"
    $ vn_pass(10)
    jump prs_left

## Rung 2's end: off, unannounced, still wound; rung 2's growth inside the dormant check. Travis, on
## the next shift, asks why you've stopped shouting from the chair: his one line before rung 5.
label prs_left:
    $ vn_enter(bg="prs_pool", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_two_off")
    "You're halfway back across the poolside when it goes."
    show cg prs_two_off onlayer cgl
    call prs_contour(False)
    prs_you "\"No— no no no, NOW? You do it {i}now{/i}? I'm still— I'm still {i}totally{/i}—\""
    "You're still totally. Your cock's back, small and hard and aching in the wet shorts, and the heat hasn't gone with the pussy. It's just sitting there, wound up tight, with nowhere to go."
    "{color=#ff5fb8}And your voice didn't come back down.{/color}"
    prs_you "\"Testing. Testing. {i}Testing{/i}.\""
    "High. Sweet. A girl's voice, out of your mouth."
    prs_you "\"Oh my GOD. Oh my god, that's not— say something normal, say something— {i}pool's closed{/i}—\""
    "Higher, if anything."
    prs_you "\"It's STAYING—!\""
    show cg prs_reflection onlayer cgl
    $ prs_body(2)
    "{color=#ff5fb8}You catch yourself in the dark glass of the office window. Your face looks back at you, and it's your face, it's definitely your face, but the edges have gone soft. The jaw. The brow. Like somebody's taken a thumb to the corners of you and smudged them.{/color}"
    "{color=#ff5fb8}And your board shorts have gone tight round the back. You put a hand there. Your seat's rounder. Fuller. It pushes back into your palm when you squeeze, and the squeeze goes straight through to the front, and you whimper. In the new voice.{/color}"
    "{color=#ff5fb8}Your mouth's still full of her. Your tongue keeps doing the thing, the flat slow lick, against the back of your teeth, all by itself. {i}You learned her in one go{/i}, and it won't forget. Your lips are so sensitive the air on them makes you shiver, and down below, smaller and harder than ever in the shorts, your cock pulses at nothing and you can feel {i}every{/i} pulse.{/color}"
    hide cg onlayer cgl
    show screen prs_dormant(2)
    "Portia's in the office doorway with the card. She doesn't come out. She just watches you stand there, wound up and wobbling, and smiles, and goes back inside."
    hide screen prs_dormant
    $ vn_enter(bg="prs_staffroom", pc="flushed", pc_tag="prs_pc", cast=[("prs_travis", "grin")], cg=None)
    "On your way out past the staff room the next shift's lifeguard is coming in, a big blond lifeguard called Travis Boone, twenty-one, who's never once looked at you twice."
    prs_travis "\"Hey, Mahoney. Why've you stopped shouting from the chair?\""
    "You don't answer. You can't. You just walk faster."
    $ vn_pass(30)
    $ vn_enter(bg="prs_room", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_bed_night")
    show cg prs_bed_night onlayer cgl
    "You walk home to Domus Street with your shorts still wet and your cock still hard, and lie on your bed in the dark rubbing your nipples, trying to say \"pool's closed\" deep, over and over, until you give up."
    hide cg onlayer cgl
    call vn_night(12)
    jump prs_chair

## ---- DAY 3, Wednesday, light rain (Press Chair, Stall, Door, Nothing, Kit Three) --------------

## The day shift: she presses it from the gallery and walks out; the high chair; you soak through;
## the climb down past everyone.
label prs_chair:
    $ prs.fit = "kit"
    $ vn_enter(bg="prs_room", pc="furious", pc_tag="prs_pc", cast=[], cg=None)
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost. Rain on the window. You've swapped onto the afternoon shift so you won't be anywhere near the plant room at closing. You're very proud of that."
    $ vn_pass(60)
    $ vn_enter(bg="prs_pool", pc="furious", pc_tag="prs_pc", cast=[], cg="prs_gallery")
    "By lunchtime you're up on the chair. Red board shorts, yellow t-shirt, whistle, the afternoon crowd: lane swimmers, a couple of aqua-fit ladies, the usual lads cannonballing in the deep end."
    "You use hand signals. You haven't blown the whistle once."
    show cg prs_gallery onlayer cgl
    "And up in the spectators' gallery, behind the glass, there's a dark high ponytail. She's sitting in the front row with her phone in her lap. She lifts it, so you can see it."
    prs_you "\"Don't. Don't you DARE—\""
    "You mouth it at her."
    "She presses it. She stands up. She walks out of the gallery without looking back."
    show cg prs_chair_wet onlayer cgl
    call prs_contour(True)
    show prs_pc flushed
    prs_you "\"{i}Hhh{/i}—\""
    "You grab both arms of the chair."
    "It's worse than last time. It's always going to be worse than last time, isn't it. It hits you up there on the chair in front of the whole afternoon crowd like a hand pressed flat between your legs, and you're wet through the shorts in seconds, a dark patch blooming on the red, spreading, and the chair's high and white and everybody in the pool is {i}below{/i} you looking up."
    call prs_heat_beat(3)
    "You cross your legs. You uncross them. You grind down on the seat of the chair and bite your lip so hard you taste it, and the lane swimmers go up and down, up and down, and you watch them with your thighs shaking and your hand on the whistle you can't blow."
    "You last a long time. Longer than anyone could."
    show cg prs_climbdown onlayer cgl
    "Then you climb down."
    "Down the ladder of the high chair, rung by rung, with the wet patch on the back of your shorts at everybody's eye level. Past the deep end. Past the cannonball lads, who stop cannonballing. Past the aqua-fit ladies. Past the lane swimmers, who stop at the wall to watch you go. The whole length of the poolside, squelching, with your arms crossed over your nipples and your face on fire."
    prs_you "\"Toilet break. Cover the— somebody cover the—\""
    "You squeak it at nobody."
    "Nobody's listening. Everybody's looking.\n{size=-5}{color=#ff8fa3}▸ The staff shower stall{/color}{/size}"
    $ vn_pass(5)
    jump prs_stall

## RUNG 3, nobody: you, the staff shower stall, all afternoon, held to a full scene's length. Your hand
## works and the heat doesn't move; the shower jet; your own fingers in your ass (the first thing
## ever inside you, and nothing); someone in the next stall. Nothing inside the pussy.
label prs_stall:
    $ vn_enter(bg="prs_stall", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_stall_one")
    "The staff showers are a row of stalls in a tiled room behind the first-aid room. You get into the end one and slam the bolt across and rip your shorts down to your ankles."
    $ prs.fit = "nude"
    prs_you "\"Okay. Okay. Okay. You know how this goes. One go. One good go, and it stops.\""
    "You tell yourself."
    show cg prs_stall_one onlayer cgl
    "You know how this goes. You did it on her desk. You lean back against the cold tiles and spread your feet and put your hand down there and it's like putting your hand in hot syrup, and you find the nub, and {i}rub{/i}."
    prs_you "\"{i}Hhn{/i}— there— there, {i}yes{/i}—\""
    "It works. Oh, it works. You come in no time at all, banging the back of your head on the tiles, your knees folding, a hot little gush down the insides of your thighs." with vnfx("flash")
    prs_you "\"Ha. Ha. {i}Ha{/i}. See? Easy.\""
    "And then you wait for it to stop."
    "It doesn't stop."
    "It doesn't even dip. You're standing there with your hand still between your legs and the heat's exactly where it was. Like you didn't do anything. Like you came in somebody else's body."
    prs_you "\"Oh, come {i}on{/i}.\""
    show cg prs_stall_again onlayer cgl
    "Again, then. Faster. Two fingers, then three, flat, scrubbing. You come again, harder, with a squeal that bounces off the tiles. You wait." with vnfx("shake")
    "Nothing. Warm, wet, wanting, exactly the same."
    prs_you "\"This is— this is {i}broken{/i}— this is a {i}broken{/i} one—\""
    "Again. Again. You lose count on purpose. You come standing up and you come sitting on the tiled bench and you come crouched in the corner with your forehead on the wall. It turns into troubleshooting. You try slow, like she likes it when she's licked. You try fast. You try pinching your nipples at the same time, which makes you come so hard you see stars, and doesn't make one bit of difference afterwards. You try {i}not{/i} touching it, for as long as you can stand, which isn't long."
    prs_you "\"Okay. Okay. Water. Water, water, water.\""
    hide cg onlayer cgl  # ff 2:27 am: no picture, jet failed 4 draws (SCENES.md pressit v4)
    "You turn the shower on and unscrew the head off its clip and point the jet straight at yourself."
    prs_you "\"{i}OH{/i}—\"" with vnfx("shake")
    "That's new. That's very new. The jet drums right on the nub, hard and hot and relentless, and your thighs start shaking and won't stop, and you come with the shower head clamped between your legs and the water spraying up your belly and into your face, gasping, spluttering, laughing at how good it is."
    "And afterwards it's still there."
    prs_you "\"I'm going to drown in here. I'm going to drown in a staff shower and they'll find me with a {i}shower head{/i}—\""
    show cg prs_fingers onlayer cgl
    "You're desperate now. You're properly desperate. You put one foot up on the bench and reach round behind yourself, and you've never, ever done this, and you're doing it. One wet finger, circling your ass. Pressing. Slipping in."
    prs_you "\"{i}Hah{/i}— oh— that's— {i}weird{/i}— that's—\""
    "It's the first thing that's ever been inside you. One finger. Then two, slow, the water helping. You rock back on them. It's full and strange and good in a dull deep way that doesn't touch the heat at all. Not even a flicker. The pussy just keeps aching, empty and slick, while you fuck your own ass in a shower stall, and it does {i}nothing{/i}."
    prs_you "\"Doesn't— doesn't even— doesn't COUNT?\""
    "You do it anyway, for a while. Because it's something."
    vn_sfx "Bang."
    "The outer door bangs."
    "You freeze, fingers in your ass, the shower head dangling."
    "Somebody comes in. Somebody goes into the stall next to yours. The bolt clacks across. Their shower starts, and they start whistling, some tuneless thing, one thin {i}wall{/i} away from you."
    menu:
        "One thin wall away."
        "Don't stop":
            "You don't stop."
        "Try to stop":
            "You try to stop. You hold still for one breath, and two, and on the third your fingers are moving again."
    show cg prs_neighbour onlayer cgl
    "You can't stop. You stand there with your forehead pressed to the tiles and your mouth clamped shut and your fingers still moving behind you and your other hand back between your thighs, and you rub, very very slowly, with your eyes squeezed shut, while they whistle on the other side of the wall. You come like that. Silently. Shaking all over. A tiny strangled noise in your throat that you swallow."
    "The whistling stops for a second."
    "Then it starts again."
    show cg prs_stall_floor onlayer cgl
    "They leave. You slide down the tiles onto the floor of the stall and sit in the puddle under the running water with your legs out in front of you. {i}Spent{/i}. Arms like string. Out of gas. You've done everything. You've done everything there is to do."
    "And down there, under the water, you're as hot as you were on the chair. You're as hot as you were on her desk. It's going to be like this all afternoon, and you know it."
    prs_you "\"You're making me.\""
    "You croak it at the shower head. It doesn't argue.\n{size=-5}{color=#ff8fa3}▸ Get as far as the door{/color}{/size}"
    $ vn_pass(120)
    jump prs_door

## Rung 3: you get as far as the poolside door to ask someone, and don't. Nobody does anything.
label prs_door:
    $ prs.fit = "kit"
    $ vn_enter(bg="prs_pooldoor", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_door_window")
    "You get dressed. Wet shorts. T-shirt stuck to your back. You walk out of the staff showers with your thighs pressed together and go and stand at the door onto the poolside, and look out through the little wired window."
    show cg prs_door_window onlayer cgl
    "The afternoon crowd. Somebody's covered the chair. The cannonball lads are still in the deep end, big, loud, splashing, completely uninterested in anything but each other."
    "Any one of them."
    "That's the thought. It comes up out of you whole, like you've had it before. {i}Any one of them{/i}. You could push the door open. You could walk out there in your wet shorts and crook a finger at the biggest one and say—"
    "Say what?"
    "Your hand's on the push bar. Your heart's going like you've swum a length underwater. You can feel how wet you are. You can feel your own pulse {i}down there{/i}."
    prs_you "\"Excuse me. Excuse me, could you— would you mind—\""
    "You practise, under your breath, in the new high voice."
    "One of the lads looks over at the window. Right at you."
    "You let go of the bar and walk away very fast.\n{size=-5}{color=#ff8fa3}▸ Find a mirror{/color}{/size}"
    $ vn_pass(30)
    jump prs_nothing

## Rung 3's end: off, unannounced; the mirror, nothing changed: "...Seriously? NOTHING?" Rung 3's row
## is rung 2's body; the dormant check reads nothing new.
label prs_nothing:
    $ vn_enter(bg="prs_toilet", pc="furious", pc_tag="prs_pc", cast=[], cg="prs_mirror")
    "The staff toilet has a long mirror. You're standing in front of it with your shorts round your knees, checking, when it goes."
    $ prs.fit = "nude"
    show cg prs_mirror onlayer cgl
    call prs_contour(False)
    "No warning. No text. She just switched it off, wherever she is."
    "Your cock. Small, hard, exactly the same. You stand there and look at the rest of you in the mirror. Smooth all over. The puffy nipples. The soft edges on your face. The round seat in the mirror when you turn. Everything that was there this morning."
    "And not one thing more."
    "You turn. You turn back. You lean right in to the glass."
    prs_you "{b}\"...Seriously? NOTHING?\"{/b}" with vnfx("shake")
    "A whole afternoon. All of it. The chair and the stall and the shower head and your {i}fingers{/i}, and the mirror's exactly the same as it was at lunch. You did everything, and it didn't take."
    $ prs_body(3)
    "Your hands know it, though. They know every trick a stall has: the angle against the tiles, the jet, the slow rub that keeps quiet, the two fingers behind. {i}You know every trick a stall has.{/i} Your ass is still warm and loose from them, and you clench round nothing and gasp at how much you feel it."
    hide cg onlayer cgl
    show screen prs_dormant(3)
    "{size=-5}{color=#ff8fa3}▸ The kit cupboard, at closing{/color}{/size}"
    hide screen prs_dormant
    $ vn_until(21)
    jump prs_kit_three

## Rung 3's fitting, in the evening: NO CHANGE. She reads back through the card, sees nothing earlier
## has ever come back, stops, gets visibly turned on, and says "Thursday". The rain hides the wet.
label prs_kit_three:
    $ prs.fit = "kit"
    $ vn_enter(bg="prs_office", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    "She's in the duty office at closing with the card on the desk in front of her, waiting."
    prs_portia "\"Kit.\""
    prs_you "\"There's no {i}point{/i}. Nothing {i}happened{/i}. I sat in a shower all afternoon and nothing {i}happened{/i}—\""
    "Your voice cracks up high on the last word."
    prs_portia "\"Kit.\""
    "Fresh red board shorts, fresh yellow t-shirt. She ties the cord. She smooths the shirt. She stands back."
    prs_portia "\"No change. No change.\""
    show screen prs_card(3)
    "She writes it. Then she doesn't put the pen down. She turns the card over and reads back up it, from the bottom, slowly. FITS. FITS. NO CHANGE. Then she looks at you. Then she looks at the card again."
    hide screen prs_card
    prs_portia "\"The hair didn't come back. The voice didn't come back. The seat didn't come back. Nothing that went has ever come back.\""
    "Not to you. To herself."
    prs_you "\"Yeah, I {i}noticed{/i}—\""
    prs_portia "\"But today didn't move anything.\""
    "She taps the card."
    prs_portia "\"Nobody touched you today.\""
    show prs_portia soft
    show cg prs_portia_pink onlayer cgl
    "She stops talking. She just stops. She's looking at you, and her cheeks have gone pink, and her lips are parted, and she crosses her legs on the desk, slowly, tightly, the way you've been crossing yours all day."
    prs_you "\"Portia?\""
    prs_portia "\"Thursday. Come to mine on Thursday.\""
    "Her voice has gone low."
    $ vn_pass(30)
    $ vn_enter(bg="prs_street_rain", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_rain_walk")
    show cg prs_rain_walk onlayer cgl
    "You walk home to Domus Street in the rain with your shorts soaked through, and the rain's soaked everything else through too, so nobody can tell. You're grateful for that. You're grateful for that the whole way home."
    hide cg onlayer cgl
    call vn_night(9)
    jump prs_ambient

## ---- DAY 4, Thursday (Press Ambient, Flat, Toy, Kit Four) ----------------------------------

## Switched on without warning on the chair, MORE on in the café queue and in the kit cupboard; the
## tracksuit over the kit; hand signals; and once on purpose, alone: you text her, and she presses it.
label prs_ambient:
    $ prs.fit = "own"
    $ vn_enter(bg="prs_room", pc="furious", pc_tag="prs_pc", cast=[], cg=None)
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost."
    "Thursday."
    $ vn_pass(60)
    $ prs.fit = "track"
    $ vn_enter(bg="prs_cupboard", pc="furious", pc_tag="prs_pc", cast=[], cg=None)
    "You dig the black staff tracksuit out of the back of the kit cupboard and zip it on over the board shorts and the t-shirt, right up to the chin, before you go anywhere near the chair. It's warm on the poolside. You don't care."
    $ vn_pass(30)
    $ vn_enter(bg="prs_pool", pc="furious", pc_tag="prs_pc", cast=[], cg="prs_track_chair")
    show cg prs_track_chair onlayer cgl
    "You don't blow the whistle. You haven't blown it since Tuesday. You point. You beckon. You do a flat chopping thing with your hand that means {i}no diving{/i} and a rolling thing that means {i}get out{/i}. The regulars think you've got laryngitis."
    "Mid-morning, up on the chair, with the tracksuit zipped and your thighs crossed—"
    call prs_contour(True)
    show prs_pc flushed
    prs_you "\"{i}Nnh{/i}—!\"" with vnfx("shake")
    "You nearly go off the back of the chair. There's nobody in the gallery. She's not even {i}here{/i}. She's somewhere in town with her phone in her hand and you're up a ladder in front of the whole morning session with a brand new pussy gushing into your board shorts."
    call prs_heat_beat(4)
    "You don't climb down. You sit it out. You sit on it, grinding the seam into yourself in tiny secret circles, and wave the lane swimmers up and down with a hand that won't stop shaking."
    $ vn_until(13)
    $ vn_enter(bg="prs_cafe", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_cafe_queue")
    "At lunch you queue in the café for a sandwich, and the woman in front of you is taking forever over the crisps—"
    show cg prs_cafe_queue onlayer cgl
    call prs_contour(True)
    "—and you grab the counter with both hands and bite down on a squeal, and the woman with the crisps turns round, and you smile at her with your face on fire and your thighs clamped and your knees knocking."
    prs_you "\"Cramp.\""
    "You squeak it."
    $ vn_until(15)
    $ vn_enter(bg="prs_cupboard", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_cupboard_floor")
    "In the afternoon you go into the kit cupboard for more kickboards and pull the door to behind you—"
    show cg prs_cupboard_floor onlayer cgl
    call prs_contour(True)
    "—and end up on the floor of it, in the dark, among the floats, with your tracksuit bottoms round your knees and your hand down your shorts, rubbing and rubbing and getting {i}nowhere{/i}, because it never goes anywhere, does it, not on your own, you {i}learned{/i} that—"
    prs_you "\"You're making me. This is {i}coercion{/i}, this is—\""
    "You hiss it at the cupboard door."
    "The cupboard door doesn't say anything."
    $ vn_until(17)
    $ vn_enter(bg="prs_toilet", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_toilet_text")
    show cg prs_toilet_text onlayer cgl
    "After your shift you lock yourself in the staff toilet and sit on the lid and get your phone out and look at her name for a long time."
    menu:
        "Her name on the screen."
        "Type {i}again{/i}":
            $ prs.text4 = "again"
        "Type {i}do it{/i}":
            $ prs.text4 = "do it"
    $ _prs_t = prs.text4
    show screen prs_phone([(None, _prs_t)])
    "Then you type {i}[_prs_t]{/i}, and send it."
    hide screen prs_phone
    call prs_contour(True)
    "You put your head between your knees and moan into your own tracksuit, alone, on purpose, and grin about it, and hate that you're grinning."
    show screen prs_phone([(None, _prs_t), ("PORTIA", "Tonight. Top flat, the villa on Danube Street. Bring the kit.")])
    "Your phone buzzes."
    hide screen prs_phone
    "You're already going.\n{size=-5}{color=#ff8fa3}▸ Danube Street, the top flat{/color}{/size}"
    $ vn_until(19)
    jump prs_flat

## Rung 4: her flat at the top of a villa on Danube Street, and the kit holdall she signs out.
label prs_flat:
    $ vn_enter(bg="prs_flat", pc="flushed", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    "The villa's big and white and old and has a gravel drive. The top flat has its own door at the top of its own staircase, and she opens it before you knock."
    prs_portia "\"You brought the kit.\""
    prs_you "\"I brought the kit. It's been on all {i}day{/i}, Portia. All day. You can't just— people {i}saw{/i}—\""
    "You hold up the holdall from the pool, the one she signs out of the kit cupboard with her own name."
    prs_portia "\"Nobody saw anything.\""
    "She takes the holdall."
    prs_portia "\"Come in.\""
    "It's an enormous room. Big windows, big pale rugs, a big low bed, and nothing out of place anywhere, like nobody really lives in it. There's a team photo of the swim club on one wall, and her, front and centre, with a medal."
    hide prs_portia
    show cg prs_holdall onlayer cgl
    "She puts the holdall on the bed and unzips it. Board shorts. T-shirt. And, folded at the bottom, something red and shiny you can't see properly."
    "She puts something else on the bed next to it. Pink, smooth, silicone, gently curved."
    prs_you "\"What's {i}that{/i}.\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Testing.\"\n{size=-5}{color=#ff8fa3}▸ Testing what{/color}{/size}"
    jump prs_toy

## RUNG 4, her toy, "testing". Her cock stays hidden: she's behind you, her hand in her own joggers,
## out of sight. Switched off first: the toy in your ass, your small cock bouncing useless, nothing.
## Then she switches you on mid-stroke and moves the toy: the first penetration of the pussy, and the
## first relief. Non-con, flipping at "And the heat moves." "Switch it" is the break (he begs for the
## switch, never the use); "I have no CHOICE— don't you STOP—" is the costume's first appearance.
label prs_toy:
    $ vn_enter(bg="prs_flat", pc="flushed", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    prs_portia "\"Shorts off. Face down. Knees and elbows.\""
    prs_you "\"No. No, I'm not doing anything face down, I'm not doing {i}anything{/i}, I came here to tell you to switch it OFF—\""
    "She presses the phone."
    call prs_contour(False)
    show screen prs_dormant(3)
    prs_you "\"What? No— {i}off{/i}? Why {i}off{/i}— I've been on all day, I'm— you can't just—\""
    hide screen prs_dormant
    hide prs_portia
    show cg prs_toy_neck onlayer cgl
    "She takes you by the back of the neck. Not hard. Just all the way round, warm and certain, and she walks you two steps to the bed and bends you down over it, and your face goes into her duvet, and she holds it there."
    prs_you "\"Get OFF— Portia— get your hand off my NECK—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Knees and elbows, subject.\""
    $ prs.fit = "nude"
    "She drags your shorts down with her free hand."
    menu:
        "Your shorts going."
        "Kick":
            "You kick. They come off anyway."
        "Grab the waistband":
            "You grab the waistband with both hands. She peels your fingers off it one at a time, and they come off anyway."
    "Her hand moves from your neck to the small of your back and presses, flat, and your knees fold under you, and you're face down on her big pale bed, knees and elbows, ass up, your little cock hanging hard and stupid between your thighs. You push up against her palm. It doesn't move. It doesn't move for the rest of it."
    "The heat hasn't gone with the switch. It never does any more. It's just sitting in you, with nothing to sit {i}in{/i}."
    vn_sfx "Click."
    "You hear a cap click. Something cold and slick drips down the crack of your ass. Her fingers spread it."
    prs_you "\"Don't— don't you DARE— I never said you could touch my—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Oh, you've done this.\""
    "Pleased. Her fingertip slips in, easy."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You've done this {i}alone{/i}. In the stall?\""
    prs_you "\"Shut up— shut {i}up{/i}— nobody's done anything— take it OUT—\""
    show cg prs_toy_anal onlayer cgl
    "The toy's tip presses where her finger was. Slides in. Slow. Deeper than your fingers ever went, smooth and fat and curved, and you push your face into her duvet and yell into it." with vnfx("shake")
    prs_you "\"{i}Ohhh{/i}— no— get it OUT— I didn't say ANY of—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I'm testing.\""
    "She fucks you with it. Slow, steady, deep, all the way in and almost all the way out, and it's full, it's so full, and you hate it, and your hips start rocking back onto it anyway, every time, and your small cock bounces under you with every push, slapping your belly, leaking strings onto her duvet. Nobody touches it. She doesn't even look at it. It's just there, bobbing, useless."
    prs_you "\"Stop pushing BACK— that's not me— that's my HIPS doing that— that one doesn't count and you KNOW it—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I know.\""
    prs_you "\"It's not even— why is it even BACK—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Is that helping? The heat. Is it doing anything?\""
    "Curious."
    prs_you "\"{i}No{/i}— no, it's not doing— {i}ahh{/i}— it's not doing {i}anything{/i}— it feels {i}amazing{/i} and it's not doing ANYTHING—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Mm. Interesting.\""
    "She keeps it going. Long strokes."
    "You're begging. You don't notice when you started."
    prs_you "\"Please— please, I can't— switch it— Portia, please, switch it—\""
    "She doesn't stop. With the toy all the way in you, she reaches past your hip for the phone on the bed."
    show cg prs_toy_switch onlayer cgl
    call prs_contour(True)
    prs_you "\"{i}HAAH{/i}—\"" with vnfx("shake")
    "Under you your cock folds away to nothing mid-bounce, and there's a pussy, and it's already {i}streaming{/i}, and she's pulling the toy out of your ass in one long slide and moving it down, and its slick round tip finds your lips, and parts them, and pushes."
    show cg prs_toy_in onlayer cgl
    "In."
    "It goes {i}in{/i}. Into you. Into the new part of you, for the first time ever, slow and thick and all the way, stretching you open round it, filling you up so full you can't breathe."
    prs_you "\"Oh— oh {i}god{/i}— oh god oh god oh {i}god{/i}—\""
    "{b}And the heat moves.{/b}"
    "For the first time since her desk, since the chair and the stall and the cupboard and the café, it {i}moves{/i}. It drops. It breaks. Like cold water on a burn. You actually laugh out loud with relief, a big happy hiccup of a noise, and push back onto the toy so hard your knees slide on the duvet."
    show prs_pc costume
    show prs_portia amused at vn_cast_slot
    prs_portia "\"That is the difference.\""
    "Her voice has gone low and rough."
    show cg prs_toy_peak onlayer cgl
    vn_sfx "Shlk shlk shlk shlk."
    "She fucks you with it properly now. Not testing. Hard, fast, wet, the noise of it filling her big quiet room, and you're coming, you're coming on it already, clamping down on it, gushing round it onto her hand." with vnfx("flash")
    prs_you "\"I have— I have no CHOICE— don't— don't you STOP—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Wasn't going to.\""
    "Behind you, you hear her breath change. The toy keeps going in one hand, steady, relentless, and something else is going on behind you with the other, fast, a rustle of joggers, a wet sound that isn't you. You can't see. You don't turn round. You're too busy coming again."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Look at you. {i}Look{/i} at you.\""
    "She breathes it."
    show cg prs_toy_cum onlayer cgl
    "And she comes. Behind you, out of sight, with a sound you've never heard her make, a raw, shaky moan right through her teeth, her hand on the toy going ragged and deep and shoving it into you as she does, so hard it knocks you flat onto your belly, and you come a third time under her, squealing into her pillow." with vnfx("flash", "shake")
    "It's not like the plant room. The plant room was your mouth doing a job. This is her using you to get herself off, and doing it, and not hiding that she did."
    "She leaves the toy in you. Her hand's on the small of your back, hot and a little shaky. You lie there twitching round it."
    "Then she switches you off."
    call prs_contour(False)
    "The toy slides out of you as the pussy folds away, and your cock's back, small and stiff and flat to her duvet, and—"
    show cg prs_four_growth onlayer cgl
    $ prs_body(4)
    prs_you "{color=#ff5fb8}\"{i}Wait{/i}. Wait, wait, what's— oh. Oh, my {i}HIPS{/i}—\"{/color}"
    "{color=#ff5fb8}They're coming out. Right now, under her hand. Your hips swell out to either side of you like they're being poured, wide and soft and round, and your ass comes up with them, big, heavy, a whole new handful each side lifting off the backs of your thighs, and your waist pulls in tight under her palm so the curve from your ribs to your hips is suddenly, ridiculously {i}dramatic{/i}.{/color}"
    prs_you "\"My HIPS— she bought those, she— again, do it AGAIN—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I didn't buy anything.\""
    "Fascinated. She squeezes. You yelp. It's so {i}sensitive{/i}. The whole ass. Every squeeze goes straight down your thighs and back up through the middle of you."
    "{color=#ff5fb8}And your chest. You push up on your arms and it sways. Not much. Soft. Two little soft swells where your flat chest was, enough to shift when you move, enough to fill a palm. An A. You put a hand on one, and moan, and take it off fast.{/color}"
    "{color=#ff5fb8}And your hair's grown out, past your ears, down to your jaw.{/color}"
    "{color=#ff5fb8}And your ass knows what a toy is now, and your new pussy knows what being filled is, and both of them are aching for it again already, deeper than any ache you've had.{/color}"
    hide cg onlayer cgl
    show screen prs_dormant(4)
    "{size=-5}{color=#ff8fa3}▸ The holdall{/color}{/size}"
    hide screen prs_dormant
    $ vn_pass(20)
    jump prs_kit_four

## Rung 4's fitting, out of the kit holdall: the board shorts WON'T CLOSE; the women's swimsuit FITS.
## She says it and doesn't write it. Then she switches you back on, and leaves it on overnight.
label prs_kit_four:
    $ vn_enter(bg="prs_flat", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    "She has you stand at the foot of the bed while she gets the kit out."
    hide prs_portia
    show cg prs_fit_four_shorts onlayer cgl
    "The red board shorts go up your legs, and stop. Over the new hips they go, just, and the cord won't meet across your belly. She pulls. It doesn't meet. She tries the other way. It doesn't meet."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Won't close.\""
    "She drops them. She takes out the red shiny thing at the bottom of the holdall and shakes it out, and it's a women's swimsuit. A one-piece. The pool's own, the one the swim club trains in."
    prs_you "\"No.\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Step in.\""
    prs_you "\"No. No way. You can't make me— I'm not wearing a— that's a {i}women's{/i}—\""
    $ prs.fit = "suit"
    show cg prs_fit_four_suit onlayer cgl
    "You step in. She draws it up your legs and over the hips, and it hugs them, and over the soft little chest, and settles the straps on your shoulders, and smooths it flat over your belly with both hands, and the material's so thin and so tight you can see your own cock through it, small and squashed flat to one side, the shape of it right there in red."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Fits.\""
    "She takes the card out of her jacket. She uncaps the pen."
    "And she doesn't write it."
    "She just looks at you. Pen in her hand. Card on her knee. You in the red swimsuit at the foot of her bed. After a while she caps the pen again and puts the card away."
    hide cg onlayer cgl
    show screen prs_card(4)
    "You noticed. She saw you notice. Neither of you says a word about it."
    hide screen prs_card
    $ prs.fit = "track"
    "She zips you into the black staff tracksuit, over the swimsuit, all the way to the chin, and stands back."
    show prs_portia amused at vn_cast_slot
    "And presses the phone."
    call prs_contour(True)
    show prs_pc flushed
    prs_portia "\"Go home. Leave it on.\""
    prs_you "\"All {i}night{/i}?\""
    prs_portia "\"All night.\""
    $ vn_pass(30)
    $ vn_enter(bg="prs_street_night", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_walk_four")
    show cg prs_walk_four onlayer cgl
    "You walk home to Domus Street in the dark with your thighs slicking together inside the swimsuit. You lie in bed with the tracksuit still on, and it doesn't stop. It's still going when you close your eyes."
    hide cg onlayer cgl
    call vn_night(7)
    jump prs_morning

## ---- DAY 5, Friday, heavy cloud (Press Morning, Shift, Stall Five, Script, Number) -----------

## You wake switched on, and go in like that.
label prs_morning:
    $ prs.fit = "track"
    $ vn_enter(bg="prs_room", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_morning_wet")
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost."
    show cg prs_morning_wet onlayer cgl
    "And it's on. It's been on all night. You can tell before you open your eyes, because the sheets are soaked and your hand's already between your legs, rubbing slowly through the swimsuit, and you don't remember starting."
    call prs_heat_beat(4)
    prs_you "\"Off. Off. {i}Off{/i}.\""
    "You tell the ceiling. It doesn't care what you tell it."
    "You could text her. You could text her and beg."
    prs_you "\"You're making me.\""
    "You tell her name on the screen, and put the phone face down."
    hide cg onlayer cgl
    "You get up instead. You pull the tracksuit straight over the swimsuit, still damp, and zip it to the chin, and go in to work like that. Grey sky over the pool roof. Grey light through the high windows. You in black to the chin, with a pussy, in heat, under a red one-piece, up a ladder, all morning."
    "Nobody can tell. That's what you tell yourself. Nobody can tell.\n{size=-5}{color=#ff8fa3}▸ The afternoon session{/color}{/size}"
    $ vn_until(16)
    jump prs_shift

## Rung 5: the chair in a one-piece under the tracksuit, and at the end of the shift she switches you
## off from wherever she is: the cock back, useless, and the heat stays.
label prs_shift:
    $ vn_enter(bg="prs_pool", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_shift_chair")
    show cg prs_shift_chair onlayer cgl
    "The afternoon session's packed. Friday. Lane swimmers, aqua-fit, the cannonball lads, half the swim club doing extra lengths. You sit on top of it all in your tracksuit with your knees jammed together and the red swimsuit riding up into you every time you breathe."
    "It's tight in the hips now. The tracksuit, the swimsuit, everything. You can feel the new shape of yourself pushing out at every seam, and when you shift on the seat your ass spreads on it like it's somebody else's."
    "One of the swim club women looks up at you from the deep end, and looks for a while. You look anywhere else."
    "Hand signals. No diving. Get out. Walk. Your hands are shaking so much the signals come out like you're conducting."
    "At the end of the shift, climbing down the ladder—"
    show cg prs_ladder_fall onlayer cgl
    call prs_contour(False)
    "—and you miss a rung and land on the poolside on your new ass, and your cock's back in the swimsuit, squashed small and hard against the red, a stupid little bulge, and the heat hasn't gone anywhere at all." with vnfx("shake")
    prs_you "\"It's not even— why is it even BACK—\""
    hide cg onlayer cgl
    show screen prs_dormant(4)
    "{size=-5}{color=#ff8fa3}▸ After the pool shuts{/color}{/size}"
    hide screen prs_dormant
    $ vn_until(21)
    jump prs_stall_five

## Rung 5: after your shift, the staff stall, switched on ON PURPOSE (you text her; you can't press it
## yourself until rung 7). The door opens: Travis.
label prs_stall_five:
    $ vn_enter(bg="prs_stall", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_stall_text")
    "The pool shuts. The staff showers are empty. You get into the end stall and slide the bolt, and it doesn't catch, it never has, and you're too far gone to get up and fix it."
    $ prs.fit = "nude"
    show cg prs_stall_text onlayer cgl
    "You peel the tracksuit off and hang it on the hook. You peel the swimsuit down to your waist. You stand there in the stall with your soft little A-cups out and your cock sticking up hard out of the bunched red material, and your phone in your hand."
    menu:
        "Your phone in your hand."
        "Type {i}now{/i}":
            $ prs.text5 = "now"
        "Type {i}please{/i}":
            $ prs.text5 = "please"
    $ _prs_t = prs.text5
    show screen prs_phone([(None, _prs_t)])
    "You type {i}[_prs_t]{/i}."
    "You send it."
    hide screen prs_phone
    call prs_contour(True)
    call prs_heat_beat(5)
    prs_you "\"{i}Hhhah{/i}—\""
    "You drop the phone on the bench and shove the swimsuit the rest of the way off and hang it on the hook too, and slump back against the tiles with your hand already working, both hands, rubbing, spreading, desperate, and it's useless, it's always useless, and you're doing it anyway, moaning out loud in the empty showers—"
    show cg prs_travis_door onlayer cgl
    "The stall door swings open." with vnfx("shake")
    "Travis Boone is standing there with a towel round his neck, staring at you."
    "You stare back. Naked. Legs open. Two fingers buried in the lips of a soaking pussy. Tits— little tits— out."
    "Travis's eyes go all the way down you, and all the way back up."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude.\"\n{size=-5}{color=#ff8fa3}▸ Freeze{/color}{/size}"
    jump prs_script

## RUNG 5, Travis in the staff stall, fast and graceless: your first cock. Non-con, then the flip.
## Travis MISREADS: the open door, the state of you, and your protest bounces off him because he
## thinks it's a bit. No threat, no phone, no leverage. The break as the head catches ("lower,
## LOWER"); the flip when the heat drops like a stone. Rung 5's growth lands mid-act (the chest, B,
## under his hands; your shoulders narrow; you drop a head against him). He comes in you.
label prs_script:
    $ vn_enter(bg="prs_stall", pc="furious", pc_tag="prs_pc", cast=[("prs_travis", "stunned")], cg=None)
    "Travis looks at your face. Travis looks at your pussy. Travis looks at your face."
    prs_travis "\"Mahoney?\""
    "You can't speak."
    show prs_travis grin
    "And then Travis Boone, twenty-one, the least curious man you've ever met, breaks into a slow, delighted grin."
    prs_travis "\"Door was open, dude. Door was {i}wide{/i} open.\""
    "He steps into the stall."
    prs_you "\"Get OUT— Travis, get {i}out{/i}— this isn't— I'm not— I didn't— the bolt's BROKEN—\""
    prs_travis "\"Ha. Yeah. Okay. Sure it is.\""
    "He hangs his towel on the hook over your swimsuit, like that settles it."
    hide prs_travis
    show cg prs_script_tiles onlayer cgl
    "He takes you by the hips and turns you round, easy, like he's turning a kickboard, and your hands slap flat on the wet tiles to stop your face hitting them."
    prs_you "\"Get OFF— this is coercion— this is {i}actual{/i} coercion—!\""
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Ha, yeah, okay.\""
    "Happily. His shorts hit the stall floor."
    "His cock slaps against your ass. It's big. It's thick and hot and heavy and the first one that's ever been anywhere near you, and you feel the whole weight of it laid along your crack."
    prs_you "\"I never SAID— I didn't say ANY of— get your hands OFF my— {i}hnngh{/i}—!\""
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude. You were {i}literally{/i}— dude.\""
    "He laughs."
    menu:
        "His whole weight behind you."
        "Shove back with your elbow":
            "You shove back at him with your elbow. He just leans in and pins you to the tiles with his whole chest, and the shove turns into your ass grinding back along his cock, and you didn't tell it to, and the heat {i}roars{/i}."
        "Grab for the door":
            "You get a hand off the tiles and grab for the stall door. He reaches past you and pushes it wide open, helpfully, and pins you to the tiles with his whole chest, and your ass grinds back along his cock, and you didn't tell it to, and the heat {i}roars{/i}."
    prs_you "\"Stop— why's it— why's it going QUIET— don't let it feel GOOD—\""
    "He slides it down. It bumps your ass, your perineum, slips through the wet, and the fat head catches on your lips and stops there, and every bit of you that's been burning since this morning screams for it."
    prs_you "\"I have NO choice here— lower, LOWER—\""
    show prs_travis grin at vn_cast_slot
    prs_travis "\"There?\""
    prs_you "\"{i}There{/i}— do it, do it, I've got no CHOICE—\""
    "He pushes."
    show cg prs_script_in onlayer cgl
    prs_you "\"{i}HAAAH{/i}—!\"" with vnfx("flash", "shake")
    "Your first cock. It spreads you open and it's nothing like the toy, it's {i}alive{/i}, hot and throbbing and jerking inside you, and he doesn't do slow, he doesn't know how, he just grabs your new hips in both hands and slams it home, all the way, his belly smacking your ass."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude. {i}Dude{/i}.\""
    "{b}And the heat drops. Like a stone.{/b} It falls straight out of you the second he's in, and you bang your forehead on the tiles and laugh out loud with relief."
    show prs_pc costume
    prs_you "\"Don't— don't stop— this is SO not consensual— again, AGAIN—!\""
    vn_sfx "Slap slap slap slap."
    "He goes again. He goes like a jackhammer. No rhythm, no finesse, nothing but greed, fast and graceless and exactly what the heat wanted, fucking you into the wall of the staff shower with the bolt hanging open and the door wide, and you're pushing back on every thrust, pulling him in by the wrist, rolling your hips the way the toy taught them—"
    show prs_travis grin at vn_cast_slot
    prs_travis "\"You're not even fighting, man. You're not even— you're {i}helping{/i}—\""
    "Panting, thrilled."
    prs_you "\"Shut UP and keep— {i}ahh{/i}— keep GOING—\""
    "His hands slide up from your hips, round your ribs, onto your chest, and squeeze."
    show cg prs_script_grow onlayer cgl
    $ prs_body(5)
    "{color=#ff5fb8}And they {i}grow{/i}.{/color}"
    "{color=#ff5fb8}Under his palms. Right there. Your soft little swells swell, push out, fill, rounding out into his hands until they're spilling between his fingers, until they're {i}tits{/i}, small and unmistakable and bouncing, a C, with nipples like bullets that he catches between his knuckles.{/color}"
    prs_you "\"Are you— they're GROWING, stop STARING, keep GOING—\""
    show prs_travis grin at vn_cast_slot
    prs_travis "\"They're— dude, they're getting {i}bigger{/i}—\""
    prs_you "\"I SAID keep GOING—\""
    "{color=#ff5fb8}And your shoulders roll in under his chin, narrowing, and you drop against him, a whole head's worth, so that suddenly he's big all round you and his chin's on top of your head and you're tucked under him against the wall, small, held, and he's fucking up into you from below now and it hits somewhere new and your eyes roll back.{/color}"
    "{color=#ff5fb8}Your hips know how to take him. Your pussy grips him in pulses it worked out on the toy. And your chest is so sensitive, every squeeze of his hands, every time it bounces against the tiles, that you're coming just from that, coming and coming round his cock while he gropes your brand new tits.{/color}" with vnfx("flash")
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Gonna— Mahoney, I'm gonna—\""
    prs_you "\"{i}In{/i}— in— I've got no choice— {i}IN{/i}—\""
    show cg prs_script_cum onlayer cgl
    "He comes. Deep. With a long, cracked groan into your hair, pulsing, flooding, so much it squelches out round him and runs down the insides of both your thighs while you shake and squeal and milk him." with vnfx("flash", "shake")
    "For a while it's just breathing. His. Yours. The drip of the shower."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Honestly? I could show people this and nobody'd believe me.\""
    "To the ceiling."
    prs_you "\"That's— no. That's it. That's {i}enough{/i}, Travis, I'm—\""
    "You look at him over your shoulder."
    "You can still feel him twitching inside you. He's already getting hard again. He isn't listening."
    menu:
        "He isn't listening."
        "\"Again,\" says Travis":
            jump prs_stall_sex
        "Travis pulls his shorts up":
            $ vn_pass(10)
            jump prs_number

## Rung 5's end: Travis photographs the swimsuit on its hook (a trophy, never evidence) and asks for
## your number; you give it to him; you write the real complaint and don't send it. Then she switches
## you off from wherever she is, and the dormant check reads rung 5 back.
label prs_number:
    $ vn_enter(bg="prs_stall", pc="flushed", pc_tag="prs_pc", cast=[("prs_travis", "grin")], cg=None)
    "Travis is pulling his shorts back on. He stops. He looks at the hook on the stall door, where your red swimsuit's hanging, damp, dripping onto the tiles."
    hide prs_travis
    show cg prs_hook_photo onlayer cgl
    "He gets his phone out, and takes a photo of it."
    vn_sfx "Click." with vnfx("flash")
    "Just the swimsuit. On the hook. With the flash."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"For the album. Gotta remember it.\""
    "Very seriously."
    "It is the stupidest photograph anyone has ever taken."
    hide cg onlayer cgl
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Can I get your number? For the, uh. Next time.\""
    "You give him your number. He types it in with his tongue between his teeth, and saves it under something you can't see, and grins at you, and goes. Whistling. The outer door bangs."
    hide prs_travis
    "You sit down on the bench in the stall, naked, sticky, stacked— well, {i}sort{/i} of stacked— and open a new message to him, and type with both thumbs, furious:"
    show screen prs_phone([(None, "This is NOT okay. You didn't even ASK. I said no the whole time. You didn't even")], draft=True)
    "You read it. You read it again."
    "You don't send it. You leave it there, in the box, unsent, and put the phone face down."
    hide screen prs_phone
    call prs_contour(False)
    "And there's your cock, back in your lap, and the rest of you is still exactly what Travis left."
    show screen prs_dormant(5)
    "{size=-5}{color=#ff8fa3}▸ Home{/color}{/size}"
    hide screen prs_dormant
    $ prs.fit = "track"
    $ vn_pass(30)
    $ vn_enter(bg="prs_street_night", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_walk_five")
    show cg prs_walk_five onlayer cgl
    "You walk home to Domus Street with the tracksuit zipped over your new tits and your thighs still wet, and fall asleep with the unsent text open on your phone."
    hide cg onlayer cgl
    call vn_night(11)
    jump prs_summons

## ---- DAY 6, Saturday (Press Summons, Kit Six, Dormant, Wrong Hole, Ask, Finding, Not This Part)

## Her text: "Flat."
label prs_summons:
    $ prs.fit = "track"
    $ vn_enter(bg="prs_room", pc="furious", pc_tag="prs_pc", cast=[], cg=None)
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost."
    "Your phone buzzes on the pillow."
    show screen prs_phone([("PORTIA", "Flat.")])
    "That's it. That's the whole text."
    "You type {i}no{/i}. You delete it. You type {i}why{/i}. You delete it. You type {i}I'm busy{/i}, which is a lie, and delete it, and lie there with the phone on your chest, and your chest is a {i}chest{/i} now, and the phone sits in the dip between your tits like it lives there."
    hide screen prs_phone
    menu:
        "The phone in the dip between your tits."
        "Type {i}what time{/i}":
            $ prs.text6 = "what time"
        "Type {i}when{/i}":
            $ prs.text6 = "when"
    $ _prs_t = prs.text6
    show screen prs_phone([("PORTIA", "Flat."), (None, _prs_t), ("PORTIA", "Evening.")])
    "You type {i}[_prs_t]{/i}.\n{size=-5}{color=#ff8fa3}▸ Danube Street, the top flat{/color}{/size}"
    hide screen prs_phone
    $ vn_until(18)
    jump prs_kit_six

## Rung 6's fitting, which is the argument: "You're up a cup since Thursday." The swimsuit WON'T GO
## OVER; a bikini. Portia believes him, laughs at Travis, not at him, and reads the stall off the
## body: "And that's what it bought." The one thing she points at is the number he gave Travis.
label prs_kit_six:
    $ vn_enter(bg="prs_flat", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    "She opens her door, looks at you for one second, and says:"
    prs_portia "{b}\"You're up a cup since Thursday.\"{/b}"
    prs_you "\"Hi to you too.\""
    prs_portia "\"Since {i}Thursday{/i}. Thursday you were an A. I fitted you. I had my hands on them. Today they're— take the jacket off.\""
    "She shuts the door behind you."
    $ prs.fit = "suit"
    "You take the jacket off. She looks. She looks for a long time, with her arms folded."
    prs_portia "\"Who.\""
    prs_you "\"Nobody! It was— a guy walked in on me, the bolt's broken, he just— I said NO, I said it the whole—\""
    prs_portia "\"Who.\""
    prs_you "\"Travis. From the late shift.\""
    "You mumble it."
    show prs_portia amused
    prs_portia "\"Travis Boone.\""
    "Portia laughs. Not at you. At him."
    prs_portia "\"Travis Boone can't find the deep end.\""
    show prs_portia intent
    "Then she stops laughing, and looks at your chest the way she looks at the card."
    prs_portia "\"He didn't ask.\""
    prs_you "\"NO. He didn't. He thought it was a— he thought I was {i}joking{/i}—\""
    prs_portia "\"No. Travis never asks anybody anything.\""
    "She tilts her head."
    prs_portia "\"And afterwards you gave him your number.\""
    "You open your mouth. Nothing comes out."
    prs_portia "\"And {i}that's{/i} what it bought.\""
    "She points at your chest."
    prs_portia "\"Kit.\""
    hide prs_portia
    show cg prs_fit_six_suit onlayer cgl
    "The red one-piece from the holdall won't go up past your hips. It gets as far as the new curve of your ass and stops dead. She pulls. You suck in. It doesn't go."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Won't go over.\""
    $ prs.fit = "bikini"
    show cg prs_fit_six_bikini onlayer cgl
    "She doesn't get the card out. She doesn't even pretend to. She digs in the holdall and throws you a red bikini, top and bottoms, the kind the swim club wears to train in the sun."
    "You get into the bottoms. They're tiny, and they cup the new ass, and the front is so small your cock's going to have nowhere to go. You get the top on and the triangles don't cover enough of you at all."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Fits. Fits.\""
    hide cg onlayer cgl
    show screen prs_card(6)
    prs_you "\"You're not even writing it down any more.\""
    hide screen prs_card
    show prs_portia soft at vn_cast_slot
    prs_portia "\"No. I'm not.\""
    "She zips the staff tracksuit jacket back up over the bikini, to just under your chin, and her knuckles brush your throat.\n{size=-5}{color=#ff8fa3}▸ Her bed{/color}{/size}"
    jump prs_dormant

## RUNG 6, stage one: switched off (since rung 5's end). Her cock, for the first time, between your
## thighs beside your useless one; only one of them works. Nobody remarks on it, and nobody explains
## it. Non-con, never flips: she pins you under her, and you protest it out loud. "Switch it" is the
## switch, never the use.
label prs_dormant:
    $ vn_enter(bg="prs_flat", pc="furious", pc_tag="prs_pc", cast=[("prs_portia", "intent")], cg=None)
    "She puts you on your back on her big bed, in the bikini, with the jacket open. You're switched off. You have been since last night, since the stall."
    hide prs_portia
    show cg prs_six_bikini_bed onlayer cgl
    "Your cock's in the front of the bikini, small and hard, pushing the scrap of red out in a stupid little point. It looks ridiculous. You know it looks ridiculous."
    prs_you "\"Don't look at it.\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I'm not.\""
    "She isn't. She's undoing her joggers."
    hide cg onlayer cgl  # ff 2:27 am: no picture, six-cock failed 4 draws (SCENES.md pressit v4)
    "And then her cock's out."
    "It's {i}enormous{/i}. Long and thick and heavy and already hard, swaying as she kneels up on the bed, flushed dark at the head, veins down the length of it, and it makes yours look like a {i}button{/i}."
    prs_you "\"Oh. Oh, {i}fuck{/i}.\""
    $ prs.fit = "nude"
    "She pulls the bikini bottoms down to your knees."
    prs_you "\"Wait— wait, I didn't— Portia, I didn't SAY—\""
    show cg prs_six_thighs onlayer cgl
    "She lies down on top of you, all her weight, and her cock slides between your thighs, slick, hot, right up underneath your balls, and lies there alongside your little cock, belly to belly, both of them trapped between you."
    menu:
        "All her weight on you."
        "Shove at her shoulders":
            "You shove at her shoulders. She catches your wrists and puts them on the pillow above your head and leaves her hand there."
        "Twist out from under her":
            "You twist, and get a hip off the bed, and get nowhere. She catches your wrists on the way past and puts them on the pillow above your head and leaves her hand there."
    prs_you "\"Get OFF— I never said you could— get your hands OFF my—\""
    "She squeezes your thighs together round hers with her knees. And moves."
    prs_you "\"{i}Hah{/i}— no— ah— oh, that's— that's so {i}big{/i}, why is it so—\""
    "Slow, long thrusts between your thighs, the fat head of her cock pushing out above them every time and sliding along the underside of yours, dragging it, rubbing it, and yours is hard and twitching and leaking and it doesn't {i}do{/i} anything. It's like rubbing a stone. It's there. It feels. It's just {i}nothing{/i} next to hers. Hers is fucking your thighs and making you moan, and yours is just along for the ride."
    prs_you "\"It's not even— why is it even BACK—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Because I switched it off.\""
    "She keeps going."
    prs_you "\"I hate it— I {i}hate{/i} it— it doesn't {i}work{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"It works fine. It works exactly like it always did.\""
    "She thrusts. Your cock bounces off her belly."
    prs_you "\"That's what I {i}mean{/i}—\""
    show cg prs_six_writhe onlayer cgl
    "You're writhing under her, wrists pinned. Your heels are digging into her bed. The heat's been sitting in you all night and all day and now it's roaring, and it doesn't care that the pussy's gone, it's right there in your belly anyway, burning, wanting, and her cock's rubbing right through the place where it ought to be and you can't take it."
    prs_you "\"Please— please, Portia, switch it— I'll— please, just {i}switch{/i} it—\""
    "She stops. Leans on her elbows over you. Smiles."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Turn over.\"\n{size=-5}{color=#ff8fa3}▸ Turn over{/color}{/size}"
    jump prs_wrong_hole

## RUNG 6, stage two: switched on, and she takes your ass (it doesn't count, and she knows it, and uses
## it deliberately). She comes in you; nothing moves. Non-con, and it NEVER flips: anal never touches
## the heat. The break is "the other— the other—", straight into the ask.
label prs_wrong_hole:
    $ vn_enter(bg="prs_flat", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_six_knees")
    show cg prs_six_knees onlayer cgl
    "You turn over. Knees and elbows. She presses the phone."
    call prs_contour(True)
    call prs_heat_beat(6)
    prs_you "\"Yes— {i}yes{/i}— thank you, thank— {i}what{/i}— what are you— that's the—\""
    "Her cock's not at your pussy. It's at your ass."
    prs_you "\"No— NOT that— that's the WRONG— Portia, that's the wrong—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Doesn't count.\""
    show cg prs_six_anal onlayer cgl
    "She pushes in." with vnfx("shake")
    prs_you "\"{i}AHHH{/i}— get it OUT— I didn't say ANY of—\""
    "It's so much bigger than the toy. It goes and goes and goes, the whole fat length of it sliding into your ass, stretching you open round her, slow, steady, until her hips are pressed flush to your new round cheeks and you're so full you can't think."
    "And your pussy, {i}right{/i} below it, is streaming. Empty. Untouched. Clenching on nothing."
    prs_you "\"That one doesn't count and you KNOW it— take it OUT—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I know.\""
    "She doesn't slow down."
    "She fucks your ass. Long, deep, patient strokes, and every one of them feels incredible and every one of them does {i}nothing{/i}, nothing for the heat, and you knew that, you found that out on your own on a shower floor, and she's doing it on purpose. You know she's doing it on purpose. She knows you know."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You found this out in a stall, didn't you. Alone. And you never told me.\""
    "Conversational, deep inside you."
    prs_you "\"Doesn't— {i}ahh{/i}— doesn't matter, doesn't COUNT— stop pushing BACK, stupid HIPS—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"No. It doesn't.\""
    "She pulls almost all the way out. Pushes all the way back in. You howl into her pillow."
    show cg prs_six_anal_peak onlayer cgl
    "She can go forever. That's the thing you're learning. She's not even breathing hard. She fucks your ass on her big pale bed with the window going dark behind her and her hand flat on the small of your back, steady as a metronome, and you come from it, you come twice, gushing out of the pussy she won't touch onto her sheets, and the heat doesn't move. It climbs. It climbs and climbs." with vnfx("flash")
    prs_you "\"Please—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Please what?\""
    prs_you "\"Please— the other— the {i}other{/i}—\""
    show cg prs_six_anal_cum onlayer cgl
    "She comes in your ass instead. Deep, hot, pulsing, with a long low groan against your shoulder blade, and stays in you, and doesn't soften at all." with vnfx("flash", "shake")
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Doesn't count.\""
    "Into your neck.\n{size=-5}{color=#ff8fa3}▸ Beg{/color}{/size}"
    jump prs_ask

## RUNG 6, the ask: three or four tries until she accepts the plain words. THE TURN. "Nobody's making
## you" is true for the first time, because for the first time somebody waits: her hand off your back,
## the phone on the duvet. The mandatory scene after it is consensual.
label prs_ask:
    $ vn_enter(bg="prs_flat", pc="costume", pc_tag="prs_pc", cast=[], cg="prs_ask_rest")
    "She pulls out of your ass. Slowly. It takes a long time."
    show cg prs_ask_rest onlayer cgl
    "And then the fat wet head of her cock slides down, and settles against the lips of your pussy, and rests there. Not pushing. Just resting. Throbbing against you."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Ask.\""
    prs_you "\"Fuck me.\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"No.\""
    prs_you "\"What do you mean {i}no{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I mean ask properly.\""
    "You're shaking. You're pushing back against her and she's moving with you so it never goes in."
    prs_you "\"Fuck— the other one. The front. Do the {i}front{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"The front of what?\""
    prs_you "\"You KNOW what—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Ask properly, [prs_pc_name].\""
    "You put your face in the pillow and scream into it. Then you lift it out."
    prs_you "\"Fuck my pussy. Please. Fuck my—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Closer.\""
    show cg prs_ask_phone onlayer cgl
    "She takes her hand off the small of your back. She puts the phone down on the duvet, out of her reach."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"All week it's been {i}coercion{/i} and {i}no choice{/i}. And it was. This one's yours. Say the plain one. Nobody's making you.\""
    "She's very still behind you."
    "{i}Nobody's making you.{/i}"
    "And that's what does it. Not her cock. Not the heat. That. Because for the first time all week it's true. Nobody's holding you. Nobody's pressing anything. She's just there, resting against you, waiting, and nobody's ever waited before."
    show prs_pc wanting
    prs_you "{b}\"Put it in my cunt.\"{/b}"
    "It comes out flat. Plain. Clear. Your own voice, the high one, saying it like a fact."
    "Portia's breath goes out of her in one long shaky rush."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Yes.\"\n{size=-5}{color=#ff8fa3}▸ Arch back for her{/color}{/size}"
    jump prs_ask_sex

## Rung 6's recap, after the mandatory scene: the first time she isn't clinical. Rung 6's growth lands
## while she's still in you (DD; the face finished; hair past your shoulders). Then off: the heat is
## still there, the dormant check lists it. "I stopped taking notes on Thursday."
label prs_finding:
    $ vn_enter(bg="prs_flat", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_ask_cum")
    show cg prs_ask_cum onlayer cgl
    "She comes in you. Your pussy. Deep. And she doesn't stop moving while she does it, slow and hard, her forehead between your shoulder blades, her breath shaking out of her in pieces." with vnfx("flash")
    "And that's the thing. She keeps going."
    show cg prs_finding_hold onlayer cgl
    "She isn't clinical. Not now. She's got both arms round you, under your chest, holding you up against her, and she's fucking you slow and deep with her mouth on your neck, and she's {i}making noises{/i}, little ones, the whole time, and you don't think she knows."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Say it again.\""
    "She whispers it."
    prs_you "\"Put it in my— it's {i}in{/i}— it's IN—\""
    show cg prs_six_growth onlayer cgl
    $ prs_body(6)
    "{color=#ff5fb8}And with her still in you, still moving, it hits.{/color}"
    "{color=#ff5fb8}Your chest. Her arms are wrapped right under it and you feel it swell up over her forearms, heavy, soft, full, pouring out and out until her arms can barely hold it, until it's swinging under you with every thrust, slapping together, enormous. A DD. Two big round heavy tits, all yours, bouncing on her arms.{/color}"
    prs_you "\"Look at them— LOOK at them—!\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I'm looking. I'm {i}looking{/i}.\""
    "She groans it."
    "{color=#ff5fb8}And your face. You can feel it, against her pillow: your jaw slimming, your cheeks softening, your lips plumping, the last hard edge of you smoothed away. And your hair spills forward over your shoulders, down past them, into your eyes, long and dark and tangling in her fingers when she grabs it.{/color}"
    "{color=#ff5fb8}Everything's tender. Everything's lit up. Your new tits ache to be squeezed; your ass, still slick from her, clenches on nothing and you {i}feel{/i} it; your pussy is so sensitive round her cock that every stroke is a little orgasm of its own. Your hips have learned her, your ass learned her first, and your chest's going to learn whatever anybody gives it.{/color}" with vnfx("flash")
    "It goes on a long time. Longer than anything you've ever done. She comes in you again. You stop counting your own."
    show cg prs_finding_after onlayer cgl
    "Afterwards she lies on her back with you on top of her, your enormous new tits squashed on her chest, her cock still half in you. She reaches over for the phone."
    call prs_contour(False)
    "Her cock slips out of you as your pussy folds away, and your own cock's back, small, pressed against her belly. On a body with DD tits and long dark hair and a face you haven't seen yet."
    "And the heat doesn't go."
    "It doesn't even dip. You're switched off and it's right there, the same as when you were on, burning in your belly, wanting."
    prs_you "\"It's still— it's still {i}on{/i}. Portia, it's switched off and it's still—\""
    "You whisper it."
    hide cg onlayer cgl
    show screen prs_dormant(6)
    call prs_heat_beat(6)
    hide screen prs_dormant
    show prs_portia soft at vn_cast_slot
    "She looks at you. You watch it land on her. You watch her understand that this one's out of her hands too, and you watch her decide not to do anything about it, again, and get turned on by deciding it."
    prs_portia "{b}\"I stopped taking notes on Thursday.\"{/b}"
    "Portia lets out a long breath, and says it.\n{size=-5}{color=#ff8fa3}▸ Get dressed and go outside{/color}{/size}"
    $ vn_pass(30)
    jump prs_not_this_part

## Rung 6's end: Travis outside on Danube Street: "you know we don't have to keep doing this part". The
## consensual costume, about the "no" part, never a photo, evidence or leverage. You argue him back
## into it, and get his catchphrase back, deep and bored and fond.
label prs_not_this_part:
    $ prs.fit = "track"
    $ vn_enter(bg="prs_street", pc="wanting", pc_tag="prs_pc", cast=[("prs_travis", "stunned")], cg=None)
    "Travis is on the pavement at the bottom of her drive, leaning on a lamp post, scrolling. You texted him the address. You don't remember deciding to."
    "He looks up. He looks at your tits, which are doing a great deal under the zipped tracksuit. He looks at your hair. He looks at your face, for a while."
    prs_travis "\"Whoa. Okay. Hey.\""
    prs_you "\"Hey.\""
    show prs_travis grin
    prs_travis "\"So, uh. You know we don't have to keep doing this part.\""
    "He puts his phone away."
    prs_you "\"What part.\""
    prs_travis "\"The— the no thing. Where you yell no, and I pretend I can't hear you. It's kind of a lot of yelling, man. I'll just come over. You want to, I want to. We can skip the part where you yell.\""
    "He shrugs, big, easy."
    "You stare at him."
    show prs_pc costume
    prs_you "\"No.\""
    prs_travis "\"No?\""
    prs_you "\"No, we {i}can't{/i} skip it. That's the— that's how it {i}works{/i}, Travis. You don't just {i}come over{/i}. You walk in, and I say no, and you don't listen. I {i}yell{/i}. That's my {i}part{/i}.\""
    "You poke him in the chest."
    prs_travis "\"Your part's the yelling.\""
    prs_you "\"My part's the yelling. Say it.\""
    "You grab his jacket."
    prs_travis "\"Dude—\""
    prs_you "\"The thing you said. In the stall. Say {i}I could show people this{/i}.\""
    "Travis looks at you for a long moment. Then he sighs, and grins, and leans in."
    prs_travis "\"I could show people this.\""
    "Deep and bored and fond."
    prs_you "\"{i}Thank{/i} you. Tomorrow. The pool. After closing. I'll text you.\""
    "You let go of his jacket."
    prs_travis "\"You'll text me.\""
    prs_you "\"Because I {i}have{/i} to. You're making me.\""
    "You're already walking."
    hide prs_travis
    $ vn_pass(30)
    $ vn_enter(bg="prs_street_night", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_walk_six")
    show cg prs_walk_six onlayer cgl
    "You walk home to Domus Street with your new tits bouncing under the jacket and your long hair blowing in your mouth, burning, and you're grinning the whole way."
    hide cg onlayer cgl
    call vn_night(19)
    jump prs_arranged

## ---- DAY 7, Sunday, a clear evening (Press Arranged, Wrong Side, Three, Still Going, Offer, Call,
## the finale, Name) --------------------------------------------------------------------------

## You arranged it: the women's changing room after closing, the plant-room door propped the way it
## was on day 1. "Put it in my cunt." is the first thing you say (the second and last time).
label prs_arranged:
    $ prs.fit = "track"
    $ vn_enter(bg="prs_room", pc="wanting", pc_tag="prs_pc", cast=[], cg=None)
    "You wake in your room in the flatshare on Domus Street, with your flatmates' voices through the wall and your whistle on the bedpost. It's evening. You slept through Sunday. You've been texting since you woke, lying in bed in your tracksuit jacket and nothing else, with the heat burning, arranging it."
    menu:
        "To Travis."
        "{i}Don't listen to a word I say.{/i}":
            $ prs.text7 = "Don't listen to a word I say."
        "{i}Door's open. Ignore me.{/i}":
            $ prs.text7 = "Door's open. Ignore me."
    show screen prs_phone([(None, "To Portia: The pool. Closing. The changing room. Bring your phone."), (None, "To Travis: The pool. Closing. " + prs.text7), (None, "To the duty manager: I'll lock up.")])
    "To Portia. To Travis. To the duty manager."
    hide screen prs_phone
    $ vn_pass(60)
    $ vn_enter(bg="prs_pool", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_closing_seven")
    show cg prs_closing_seven onlayer cgl
    "It's a clear evening. You walk to the pool in the jacket and the bikini bottoms and the tracksuit trousers that won't do up over your ass any more. You do the closing round. Lane ropes, kickboards, squeegee, lights. The swim club's long gone home."
    show cg prs_plant_propped onlayer cgl
    "Then you go down the short corridor behind the deep end, and unlock the plant room, and prop the door open with a chlorine drum, exactly the way it was the first night. You can see the drums. You can see the gap behind them."
    "Then you go round the other way. Out past the staff room. Down the women's corridor. Through the door that says WOMEN."
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[("prs_portia", "amused"), ("prs_travis", "grin")], cg=None)
    "Portia's already there, sitting on the long bench in the middle of the changing room, in her team jacket, with her phone on her knee. Travis is leaning on the lockers with his hands in his pockets, trying to look like he's just walked in on something."
    "They both look up when you come in."
    prs_you "{b}\"Put it in my cunt.\"{/b}"
    "Instead of hello.\n{size=-5}{color=#ff8fa3}▸ Look up at the louvre{/color}{/size}"
    jump prs_wrong_side

## Rung 7: walking in on the wrong side of the louvre. You strip yourself here. Nobody glosses the
## callback.
label prs_wrong_side:
    $ vn_enter(bg="prs_changing", pc="flushed", pc_tag="prs_pc", cast=[], cg="prs_wrong_side")
    "You find it straight away. You'd know it anywhere."
    show cg prs_wrong_side onlayer cgl
    "High on the wall above the shower row: a little slatted louvre, painted over the same cream as the tiles, so you'd never notice it if you didn't know. Behind it, a dark gap. And behind the dark gap, if you squint, the curve of a blue drum."
    "You stand under it in the middle of the women's changing room. Steam's still hanging off the showers. The lockers bang when the air conditioning kicks in. Your face is burning. Your tits are heaving under the jacket."
    prs_you "\"Oh. Oh, {i}no{/i}.\""
    "Nobody says anything. Portia's watching you. Travis is watching Portia, trying to work out who she is."
    $ prs.fit = "nude"
    show cg prs_under_louvre onlayer cgl
    "You unzip the jacket. You drop it on the bench. You push the tracksuit trousers down over your hips and step out of them, and then the bikini bottoms, and stand there under the louvre, naked, big-tittied and soft and round and smooth all over, with your little cock hanging hard between your thick thighs."
    "You turn round once, slowly, under the slats. For the gap. For whoever's not behind it."
    "Then you sit down on the bench between them and spread your legs.\n{size=-5}{color=#ff8fa3}▸ Hold your hand out for the phone{/color}{/size}"
    jump prs_three

## RUNG 7, the three of you: Portia switches you on (you can't yet), and you run the room out loud:
## Portia in your pussy on the bench, Travis in your mouth; then they swap. Consensual.
label prs_three:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[("prs_portia", "amused")], cg=None)
    "Portia doesn't give you the phone. She just presses it."
    call prs_contour(True)
    prs_you "\"{i}Finally{/i}— oh, finally, {i}finally{/i}—\""
    show prs_travis stunned at vn_cast_slot
    prs_travis "\"Is that— did your dick just—\""
    "Travis has come off the lockers."
    prs_you "\"Don't ask questions. You never ask. That's your whole thing. Get your cock out and get over here.\""
    "He gets his cock out and gets over here."
    hide prs_travis
    hide prs_portia
    show cg prs_three_bench onlayer cgl
    "You get down off the bench onto your knees on the wet tiles and pull Portia to the edge of the bench by her jacket, and she lets you, and you get her joggers down, and her cock springs up in your face, huge and dark and already wet at the tip."
    prs_you "\"Travis. Behind me. No— Portia. {i}Portia{/i} behind me. Travis, front. Come {i}on{/i}, come on, I haven't got all night—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You've got all night.\""
    prs_you "\"Then I want ALL of it—\""
    hide cg onlayer cgl  # ff 2:27 am: no picture, three-in failed 4 draws (SCENES.md pressit v4)
    "You put her behind you. You put your hands on the bench and your ass in the air and look back over your shoulder at her, and she kneels up behind you on the tiles and lines up, and pushes, and slides into your pussy in one long wet stroke, and you scream it off the changing-room ceiling." with vnfx("shake")
    prs_you "\"{i}YES{/i}— oh, yes, YES— Travis, mouth, {i}mouth{/i}—\""
    "Travis stands in front of you with his cock in his fist. You lean in and swallow it."
    vn_sfx "{i}Glk.{/i}"
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude.\""
    "Faintly."
    hide cg onlayer cgl  # ff 2:27 am: no picture, three-spit failed 4 draws (SCENES.md pressit v4)
    "Portia fucks you from behind, hard and deep, her hands on your big new hips, her balls slapping your clit with every stroke. Travis fucks your mouth from the front, clumsy, eager, his hands in your long hair. Your tits swing under you between them, slapping together, slapping the edge of the bench. The noise is {i}huge{/i}. It echoes off every tile in the place."
    "And you're running it. You pull off Travis every few strokes to give orders, spit stringing from your lips."
    prs_you "\"Faster, Portia. {i}Faster{/i}. Travis, deeper, I can take it, I can take {i}more{/i} than that—\""
    "And back down on him, moaning round him, and they both do exactly what you say."
    prs_you "\"Swap.\""
    "You gasp it."
    show cg prs_three_swap onlayer cgl
    "They swap. Travis gets behind you and rams in with no finesse at all, and Portia stands up on the bench in front of you, holding the lockers, and feeds you her cock, so big it fills your whole mouth and makes your eyes roll back."
    prs_you "\"{i}Mmmh{/i}— {i}mmf{/i}— {i}glk{/i}— {i}glk{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Look at you. Look at you running this.\""
    "She breathes it, from above."
    show cg prs_three_cum onlayer cgl
    "Travis comes first. Of course he does. He comes in you with a shout, hips stuttering, flooding your pussy, and keeps going, because you don't let him stop." with vnfx("flash")
    "Portia comes in your mouth. Thick, hot, so much you can't keep it all, and it spills out of the corners of your lips and down your chin onto your tits, and you swallow what you can and moan for more." with vnfx("flash", "shake")
    prs_you "\"Again. Both of you. Again.\""
    "Wiping your chin.\n{size=-5}{color=#ff8fa3}▸ Again{/color}{/size}"
    $ vn_pass(40)
    jump prs_still_going

## Rung 7: they're spent; you aren't, and you're using them.
label prs_still_going:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_spent")
    "They go again. They go again after that."
    show cg prs_spent onlayer cgl
    "And then they're done. Travis is sitting on the wet floor with his back to the lockers and his cock lying soft on his thigh, staring at the ceiling, breathing like he's swum the length underwater. Portia's on the bench with her jacket open and her head back against the wall, flushed to the collarbone, her cock wet and finally, {i}finally{/i} going soft."
    "You're not done."
    "You're nowhere near done. The heat's exactly where it started. Higher. You're dripping on the tiles. You're shaking with it."
    show cg prs_ride_travis onlayer cgl
    "You climb onto Travis on the floor and grind your soaking pussy down on his soft cock until it isn't quite so soft, and ride it, slow, while he groans and laughs and pushes weakly at your hips."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude, I can't— I physically {i}can't{/i}—\""
    prs_you "\"You're making me.\""
    "You pant it, and keep going, and laugh, because it's so stupid now, because it was always so stupid."
    show cg prs_thigh_portia onlayer cgl
    "You get off him and crawl up onto the bench and straddle Portia's thigh and rub yourself on it, on the smooth muscle of it, back and forth, wet, gasping, your tits in her face. She doesn't stop you. She puts her hands on your hips and helps."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Still going.\""
    "Very quietly."
    prs_you "\"Still— {i}ahh{/i}— still going. I can't— it won't— I need—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I know what you need.\""
    "She takes her hands off your hips. She picks up her phone.\n{size=-5}{color=#ff8fa3}▸ Watch her thumb{/color}{/size}"
    jump prs_offer

## Rung 7: THE OFFER. She switches you off and offers to peel it: you'd stay like this (a woman with a
## cock, in heat, for good). "It comes off in my hands or it doesn't come off." (hers, the second and
## last time). You take the phone, switch yourself ON, and hand it back. She pockets it. THE "SHE"
## BEAT: nobody names you anything.
label prs_offer:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[("prs_portia", "soft")], cg=None)
    call prs_contour(False)
    show screen prs_dormant(7)
    "You're on her lap with your cock back. Small. Hard. Pressed against her belly. Under your enormous tits, on a body that's all hips and ass and long dark hair, it looks like a {i}joke{/i}."
    hide screen prs_dormant
    "And the heat's still there. Of course it is. Switched off is just the same, with less to do it with."
    hide prs_portia
    show cg prs_offer_pinch onlayer cgl
    "Portia holds up her thumb and forefinger. She puts them on the disc on your left hip, the way she did the first night, ready to pinch."
    show prs_portia amused at vn_cast_slot
    prs_portia "{b}\"It comes off in my hands or it doesn't come off.\"{/b}"
    show prs_portia amused at vn_cast_slot
    prs_portia "\"So. I can take it off now. Right now. And it'll lock what you are, right now. This. Like this. For good.\""
    "She glances down at your cock between you."
    "You look down at yourself. A woman, top to bottom, all curves, all heat. And that. Useless. And nothing ever, ever going to touch the heat again."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Your call.\""
    "She means it. She always means it."
    show cg prs_offer_phone onlayer cgl
    "You take the phone out of her other hand."
    "She lets you."
    show screen prs_app(False)
    "The grey button. The word under it. You look at it. Travis has sat up on the floor to watch."
    "You press it."
    hide screen prs_app
    show screen prs_app(True)
    call prs_contour(True)
    $ prs.she = True
    hide screen prs_app
    prs_you "\"{i}Hhhaaah{/i}—\""
    show cg prs_offer_back onlayer cgl
    "And you hand it back to her."
    "Portia takes it. Looks at the pink button. Looks at you. And slips the phone into her jacket pocket, and zips the pocket shut."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Okay.\""
    call prs_heat_beat(7)
    show prs_travis grin at vn_cast_slot
    prs_travis "\"She just— did she just—\""
    "From the floor, to nobody."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Yeah. She did.\""
    "You don't even hear it. You're already reaching for your own phone.\n{size=-5}{color=#ff8fa3}▸ Text Travis's group{/color}{/size}"
    jump prs_call

## Rung 7: your text to Travis's group from five-a-side. Four men in their twenties arrive; they know
## nothing and need no excuse. Portia stays on the bench with the phone in her pocket and watches. The
## lead-in ends with Travis pushing in from behind (the finale opens inside).
label prs_call:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[("prs_travis", "stunned")], cg=None)
    "You take Travis's phone off the floor, because he's in a group chat with everybody he's ever met, and you find the one that's his five-a-side mates, and type:"
    show screen prs_phone([(None, "Pool. Women's changing room. Side door's open. Now. Bring yourselves.")])
    "You send it from his phone. Travis watches you do it and doesn't argue. He's past arguing."
    hide screen prs_phone
    prs_travis "\"They're gonna think it's a prank.\""
    prs_you "\"Then they'll come and see.\""
    hide prs_travis
    show cg prs_four_arrive onlayer cgl
    "They come and see."
    "Four of them, in their twenties, big lads from five-a-side in hoodies and trainers, coming round the end of the lockers in a bunch, laughing, and then stopping laughing."
    "You're in the middle of the changing room on the long bench, on your knees, facing them, naked and enormous-chested and shining with cum and sweat, with your legs spread, rubbing yourself with both hands."
    "Nobody asks anything. Nobody needs to. You don't give anybody anything to ask about."
    prs_you "\"Well? Come {i}on{/i}.\""
    show cg prs_portia_watch onlayer cgl
    "Portia's on the end of the bench with her jacket zipped and her legs crossed and her hand resting on the pocket with the phone in it. She doesn't move. She doesn't join in. She just watches, with that look on her face, the one from the first night. Delighted."
    "Travis is behind you before the others have their belts open. You feel him line up, and look back at him over your shoulder, and push back."
    "He's in."
    prs_you "\"Yes— {i}yes{/i}— all of you, come on, I want ALL of you—\"\n{size=-5}{color=#ff8fa3}▸ The room{/color}{/size}"
    jump prs_finale_sex

## Rung 7's growth climax, all at once, in the middle of the room: H, the widest hips, the thickest
## thighs, the biggest ass, hair down your back. And the line: "That's all I'm for." (yours, the only
## time).
label prs_finale_after:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_room_next")
    show cg prs_room_next onlayer cgl
    "Travis comes in you again, and pulls out, and somebody else is in you before his cum's even started running down your thighs."
    "And it doesn't stop. You don't let it."
    show cg prs_room_many onlayer cgl
    "One after another. Two at a time. A cock in your mouth and a cock in your pussy and hands everywhere, on your hips, in your hair, on your tits, and you're coming so much you've stopped knowing where one ends and the next starts. You're running it out loud the whole time."
    prs_you "\"You— there. You— my mouth. You— {i}wait{/i}, wait your turn, no, don't wait, {i}come here{/i}—\""
    show cg prs_seven_growth onlayer cgl
    $ prs_body(7)
    "{color=#ff5fb8}And in the middle of the room, in the middle of all of them, with somebody pounding into you from behind and somebody else in your mouth, it all comes at once.{/color}"
    "{color=#ff5fb8}Your tits swell up out of the hands holding them. Out, and out, and out, heavy and huge and soft, spilling over every palm in the room, until they're hanging under you so big they drag on the bench, enormous, an H, bouncing with every thrust like they're trying to get away.{/color}"
    "{color=#ff5fb8}Your hips push out wider than you'd have believed, as wide as they'll ever go. Your thighs thicken under the hands spreading them, soft and strong and huge. Your ass swells up behind you into the hips of whoever's fucking you, so big and so round he has to grab two handfuls just to hold on. And your hair pours down your back in a dark wave to your waist.{/color}"
    prs_you "\"MORE— that's all I'm— MORE—!\"" with vnfx("shake")
    "{color=#ff5fb8}Every bit of you is lit. Your mouth. Your tits. Your ass. Your pussy. All of it, every touch, every slap, every cock, so sensitive you're screaming, coming on all of them, coming on every one of them. Your hips know every rhythm in the room. Your mouth knows every cock. You catch somebody's eye over your shoulder and he's in you a second later, because you only had to look.{/color}"
    prs_you "{b}\"That's all I'm for.\"{/b}" with vnfx("flash")
    "You say it out loud, in the middle of the room, full of strangers, with your face up and your mouth open and your enormous tits swinging. You say it like it's the best news you ever had."
    show cg prs_room_cum onlayer cgl
    "They come in you. They come on you. On your face, in your mouth, over your tits, across your ass, in your hair. You don't keep track. You don't need to." with vnfx("flash", "shake")
    "{size=-5}{color=#ff8fa3}▸ Still going{/color}{/size}"
    $ vn_pass(60)
    jump prs_name

## THE ENDING ("Pocketed"). The four are done; you're still going; Portia says your first name and
## isn't writing anything. Then the night.
label prs_name:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_name")
    "The four of them are done. They're done in a heap by the showers, done on the floor, done leaning on the lockers. Travis is asleep. Actually asleep, sitting up."
    "You're still going."
    show cg prs_name onlayer cgl
    "You're on the bench on your back with your knees up and your hand between your legs, slowly, happily, in the middle of a changing room that smells of chlorine and sex, with your huge tits rolling on your chest and your long hair hanging off the end of the bench to the floor. The heat's still there. It's always going to be there. You don't mind at all."
    "Portia's sitting at the end of the bench by your head. She's got her phone in her zipped pocket and the card in her other pocket, and she isn't writing anything. She's just looking at you, upside down, from above."
    show prs_portia amused at vn_cast_slot
    prs_portia "{b}\"[prs_pc_name].\"{/b}"
    "You grin up at her."
    $ prs.ending = "pocketed"
    $ achievement.grant("That's All I'm For")
    $ prs.fit = "track"
    hide cg onlayer cgl
    "You don't remember the walk home. You remember the night air on your bare legs, and your enormous chest under the zipped jacket, and the heat, and grinning.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    call vn_night(8)
    $ vn_pass(5 * 60)
    jump prs_epilogue

## ---- THE EPILOGUE, Monday's chair (Press Epilogue, Stay, Go) --------------------------------

## The cold open: Monday's chair, the heat at always, and Travis's schedule in your phone. Then stay
## or go: the choice that decides the ending.
label prs_epilogue:
    $ prs.fit = "track"
    $ vn_enter(bg="prs_pool", pc="wanting", pc_tag="prs_pc", cast=[], cg=None)
    "Monday. The chair."
    hide cg onlayer cgl  # ff 2:27 am: no picture, epi-chair failed 4 draws (SCENES.md pressit v4)
    "You're up it in the black staff tracksuit, which zips to just under your enormous chest and stops there, because it physically can't go any further. Your hair's in a ponytail down your back. Under the jacket the red bikini top is doing absolutely nothing. Under everything, the heat is just on. It's on the way the pool lights are on. It's on the way the water's wet."
    "The afternoon regulars look up at you. You look down at them. Some of them are keepers. You notice that about yourself, and grin."
    show screen prs_phone([("TRAVIS", "his shifts this week, every one of them"), ("TRAVIS", "door's open?"), ("TRAVIS", "a picture of a swimsuit on a hook")])
    "Your phone buzzes in your pocket. Travis, with a list."
    hide screen prs_phone
    "You put the whistle in your mouth and blow it, and it comes out high and bright and loud, and you don't care at all."
    vn_sfx "{i}Phweeet.{/i}"
    prs_you "\"No RUNNING!\""
    hide cg onlayer cgl  # ff 2:27 am: no picture, epi-gallery failed 4 draws (SCENES.md pressit v4)
    "Portia's in the gallery. Front row. Phone on her knee, the one with the pink button on it. She holds it up so you can see it."
    menu:
        "Portia in the gallery, the phone held up."
        "\"Press it again.\"" (ending=True):
            jump prs_epilogue_stay
        "\"Peel it. Switched on.\"" (ending=True):
            jump prs_epilogue_go

## Stay: "Press it again." She keeps the phone.
label prs_epilogue_stay:
    $ prs.epilogue = "stay"
    $ vn_enter(bg="prs_pool", pc="wanting", pc_tag="prs_pc", cast=[], cg="prs_epi_stay")
    prs_you "\"Press it again.\""
    "You mouth it up at her."
    "She presses it."
    show cg prs_epi_stay onlayer cgl
    call prs_contour(True)
    "All of it at once, up on the chair in front of the whole afternoon session, and you grab the arms of the chair and moan out loud, and the lane swimmers stop at the wall to look."
    "You don't cross your legs. You don't zip anything. You sit there and let them look."
    "Portia puts the phone back in her pocket, and zips the pocket, and pats it. It's hers. It stays hers."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Evenings. My flat. Once a week. I'll text.\""
    "She calls it down."
    prs_you "\"You'll {i}text{/i}. You'll just {i}text{/i}, and I'll just {i}come{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Yes.\""
    prs_you "\"Because I don't have a {i}choice{/i}—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"You've got every choice.\""
    "And goes back to watching.\n{size=-5}{color=#ff8fa3}▸ Back out onto the poolside{/color}{/size}"
    jump prs_route_return

## Go: "Peel it. Switched on." She keeps her word: the Contour comes off in her hands and locks what you
## are. There's nothing left to switch, the heat stays, and she still books you.
label prs_epilogue_go:
    $ prs.epilogue = "go"
    $ prs.peeled = True
    $ vn_enter(bg="prs_pool", pc="wanting", pc_tag="prs_pc", cast=[("prs_portia", "soft")], cg=None)
    prs_you "\"Peel it. Switched on.\""
    "You mouth it up at her."
    "She looks at you for a while. Then she comes down out of the gallery, and down the poolside in her trainers past all the regulars, and climbs the ladder of the high chair, and crouches on the rung below you."
    prs_portia "\"You're sure.\""
    prs_you "\"Peel it.\""
    hide prs_portia
    show cg prs_epi_peel onlayer cgl
    "She tugs the tracksuit down off your hip. She puts her thumb and finger on the little disc. She pinches."
    "It comes off. Just like that, the way it did the first night. A little flat warm thing, in her fingers."
    "And nothing changes. You're exactly what you were a moment ago. Tits, hips, hair, pussy, heat. All of it, for good. There's nothing left to switch. There's nothing left to {i}press{/i}."
    show cg prs_epi_go onlayer cgl
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Huh.\""
    "She turns the disc over in her fingers and drops it in her pocket next to the phone, which doesn't do anything any more. She looks a little disappointed and a lot turned on."
    "The heat's still there. Of course it is."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Evenings. My flat. Once a week.\""
    "Climbing down."
    prs_you "\"But there's nothing to—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"I'm not booking the Contour. I'm booking you.\""
    "From the bottom of the ladder.\n{size=-5}{color=#ff8fa3}▸ Back out onto the poolside{/color}{/size}"
    jump prs_route_return
