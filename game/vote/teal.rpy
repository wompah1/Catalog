## THE TEAL PATH: "I Voted Teal in the Comments, and Now I Say Please to Men" (PACKAGE-teal.md),
## rungs 2-6 and their scenes. Shy is how you talk, not how the prose reads. The body moves first
## at rungs 3-4 (Darren answers the body; the chorus is the break); rung 5 the flip; rung 6
## consensual. Darren never sucks or strokes your cock. No toys, no DP, no audience, no group beyond
## the rung-6 threesome.

## ---- rung 2: HOURS BEHIND (Bubble Bath Apology) ------------------------------------------------

label vt_teal_two:
    call vt_gap("A week.", 9, 8)
    $ vt_grow(2)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bathroom", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_t2_tips")
    "{color=#ff5fb8}Morning, the mirror. The tips of your hair have come in teal. A bright, clean teal, like somebody dipped the ends of your dark hair in a swimming pool.{/color}"
    vt_you "\"Sick.\""
    "{color=#ff5fb8}Your skin is soft. Softer than yesterday. Your nipples are puffy and tender, two little swollen peaks that sting sweetly when the towel goes over them. And your work jeans, when you pull them on, are snug across an ass that's rounder than it was, and hips that are wider.{/color}"
    "You turn side-on to the mirror and look at it and grin."
    $ vt.fit = "work"
    $ vn_until(10)
    $ vn_enter(bg="vt_kiosk", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg=None)
    "You show Jesse the hair over the counter."
    vt_jesse "\"You dyed it?\""
    vt_you "\"It just did that.\""
    vt_jesse "\"It suits you. God, it really suits you.\""
    "All day you apologise to customers too much. Sorry, it'll be an hour. Sorry, that's the price. Sorry. You cover your mouth when you laugh. You stand at the counter with your knees together. You don't notice any of it."
    "Your voice is smoother now. Sweeter. You don't notice that either."
    $ vn_until(19)
    jump vt_teal_two_upload

label vt_teal_two_upload:
    $ vn_enter(bg="vt_kitchen", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_t2_card")
    "Evening. The kitchen counter, a pot noodle, your phone. A new upload went up at three this morning and you've saved it like a pudding."
    show screen vt_phone("t2")
    "Just Mio, this time."
    hide screen vt_phone
    show cg vt_t2_bath onlayer cgl
    "Mio in a bubble bath, pink to the ears, apologising to the camera for being {i}like this{/i}. Her chest is bigger than last week. The bubbles cling to it."
    "She soaps her breasts slowly, both hands, lips parted. Then she turns away from the camera."
    show cg vt_t2_fingers onlayer cgl
    "Low angle. Bubbles sliding down her back. She reaches behind herself and works two soapy fingers into her ass, and whispers to the steam:"
    vt_mio "\"♪ Sorry, I just want it ♪\""
    "The comments load."
    show screen vt_phone("t2")
    "You've got your hand on the front of your jeans."
    hide screen vt_phone
    call vt_again
    $ vn_until(22)
    jump vt_teal_two_bath

## Rung 2's act: the bath, alone, hours behind. As packaged.
label vt_teal_two_bath:
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bathroom", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_t2_run")
    "Before bed you run a bath. To relax. You haven't had a bath in years. You don't have bubble bath, so you squirt in a load of the washing-up liquid and swish it about until it foams."
    "You get in. It's lovely. You soap your chest."
    show cg vt_t2_soap onlayer cgl
    "Your puffy nipples are so sensitive under the soap that you gasp out loud, and your hand stays there, circling, and then it drifts lower. Down your soft belly. Past your cock, which is hard and bobbing under the bubbles, and which your hand goes right past as if it isn't there."
    "Between your cheeks. One soapy finger, circling. Then in."
    vt_you "\"Oh— oh, sorry— {i}sorry{/i}—\""
    "Who are you apologising to? Nobody. The ceiling. Your own cock. You don't know. It feels so good you want to say sorry for it."
    show cg vt_t2_two onlayer cgl
    "Two fingers. Slippery, slow, then not slow. You're whispering {i}sorry, sorry, sorry{/i} with your head back on the rim of the bath and your hips lifting out of the water to meet your hand."
    "Nobody touches your cock, you included."
    call vt_voice(2)
    vn_sfx "Knock. Knock. Knock."
    "Three knocks on the wall. 4C."
    vt_you "\"Sorry!\""
    "It comes out high and sweet, in a voice that isn't quite yours. There's a pause on the other side of the wall."
    vt_wall "\"...No worries?\""
    show cg vt_t2_cum onlayer cgl
    "You bite your lip. You crook your fingers. And at the very top of it, you whisper:"
    vt_you "\"Sorry, I just want it.\""
    "You come untouched, clenching on your own fingers, your cock spurting under the bubbles, and your voice glitches at the top like a synth on a bad note." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    "The bathwater slops over the side onto the lino."
    $ vn_enter(bg="vt_bathroom", pc="moaning", pc_tag="vt_pc", cast=[], cg="vt_t2_end")
    "And you don't stop. Two fingers back in, and a third pressing at them. Another one already building, and you're apologising to the bathroom ceiling, sorry, sorry, sorry, while the water sloshes over the rim.\n{size=-5}{color=#ff8fa3}▸ Ten days{/color}{/size}"
    jump vt_teal_three

## ---- rung 3: WHILE IT PLAYS (Practice Kiss) -----------------------------------------------------

label vt_teal_three:
    call vt_gap("Ten days. Saturday, three in the morning.", 19, 3)
    $ vt.fit = "home"
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_t3_card")
    "You set an alarm for it now. Three a.m., the phone lighting up on the pillow."
    show screen vt_phone("t3")
    hide screen vt_phone
    show cg vt_t3_booth onlayer cgl
    "Mio alone in an animated recording booth, practising kisses on her microphone. Little pecks first. Then her lips, open, wet. Then her tongue. Then, eyes shut, scarlet, the whole mic in her mouth."
    show cg vt_t3_boyfriend onlayer cgl
    "Then, for the first time, somebody steps into frame. A boyfriend, cropped above the mouth, no face at all. Mio sinks to her knees in front of him. She covers her mouth. She blushes. And she asks:"
    vt_mio "\"♪ Is it okay if I taste you ♪\""
    "It ends on her deepthroating him. The comments load."
    show screen vt_phone("t3")
    "You read them all twice."
    hide screen vt_phone
    call vt_again
    $ vt_grow(3)
    $ vn_set_time(9, 0)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bedroom", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_t3_handfuls")
    "{color=#ff5fb8}You wake up with tits. Small soft handfuls, one each side, sitting up on your chest where there was nothing yesterday. You squeeze them in bed, delighted, and laugh into your hand.{/color}"
    "{color=#ff5fb8}Your hair's at your shoulders, teal halfway up from the ends. Your lips are fuller. Your cock, when you check, is smaller. You shrug. It still works.{/color}"
    "{color=#ff5fb8}And your mouth. Brushing your teeth feels unbelievable. The brush on your tongue, on the roof of your mouth, makes your knees go. You stand at the sink for a long time.{/color}"
    $ vt.fit = "home"
    show cg vt_t3_speaker onlayer cgl
    "You put the song on your speaker on loop and leave it running all day while you clean the flat. It plays and plays."
    $ vn_until(19)
    jump vt_teal_three_door

label vt_teal_three_door:
    $ vn_enter(bg="vt_doorway", pc="shy", pc_tag="vt_pc", cast=[("vt_darren", "calm")], cg="vt_t3_knock")
    vn_sfx "Knock. Knock. Knock."
    "Three knocks. On your door, not the wall."
    "You open it in an old T-shirt that your new chest is very visible through. A man in the hall: big, calm, kind-faced, a headset round his neck. 4C."
    vt_darren "\"Hi. Sorry. Darren, from across the hall. I work from home, and the walls are, er— it's the same song. It's been the same song since ten.\""
    vt_you "\"Oh my God, sorry. Sorry! I'll turn it down.\""
    "You don't. You stand in the doorway and talk to him. He's nice. He's very nice. He hears everything through the wall, he says, and then goes red, and so do you."
    "You keep looking at his mouth. Then lower."
    show cg vt_t3_kneel onlayer cgl
    "And then you're on your knees, in your own doorway, before you've decided anything at all."
    vt_you "\"Sorry— sorry! I don't know why I— my legs just—\""
    vt_darren "\"Are you okay? Did you faint?\""
    "Your hands go to his belt. You watch them do it."
    vt_you "\"No, sorry, that's not— I don't— I'm not like that, I like girls, I swear I like {i}girls{/i}—\""
    vt_darren "\"[vt_pc_name]. Your hands are—\""
    vt_you "\"I know! I know, sorry, I'm not doing it on purpose—\""
    "The belt's open. The button. Your hands pull his jeans down, and his cock's right there in front of your face, and your mouth opens."
    vt_darren "\"Do you want me to go?\""
    vt_you "\"I— no— yes— I don't—\""
    "Your mouth's open on the head of him before you finish. Darren puts one hand flat on the doorframe and breathes out, slow, like a man stepping into cold water."
    vt_darren "\"Okay. Okay. Jesus.\""
    jump vt_teal_three_scene

label vt_teal_three_scene:
    $ vn_enter(bg="vt_doorway", pc="protesting", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t3_open")
    "He's warm and heavy on your tongue, and your mouth, your turned-up, unbelievable mouth, goes off like a firework."
    vt_you "\"Mmh— mmf— sorry— I'm not— {i}mmh{/i}—\""
    vn_sfx "Shlk. Shlk."
    "You try to pull back. Your head goes forward. You try to say {i}stop{/i} and it comes out round his cock as a moan with a vibrato in it."
    show cg vt_t3_mid onlayer cgl
    "Darren's other hand comes down onto your hair. Not pushing. Just there, warm, and your mouth takes that as a yes and goes deeper."
    vt_darren "\"Fuck. [vt_pc_name]. You've— you've never done this?\""
    vt_you "\"Never— mmf— {i}never{/i}— sorry—\""
    "You nearly come from it. From sucking alone. Your mouth is so sensitive that every slide of him over your tongue goes straight down your spine, and your hips are rocking on your heels, and your small cock is straining in your shorts, and nobody's touching it."
    call vt_voice(3)
    "Somewhere behind you, on the hall floor where you dropped it, your phone lights up. Jesse. {i}pub later?{/i} You still want her, so much. Your mouth doesn't stop."
    show cg vt_t3_polite onlayer cgl
    "And somewhere in the middle of it the protests run out, and what comes out instead, in between, is polite."
    vt_you "\"Is this— am I doing it right? Sorry. Is this right? Can I have more of it? Please?\""
    vt_darren "\"You're doing it— yeah. Yeah, you're doing it right. Take it deeper. Good. God, that's good.\""
    vt_darren "\"I only came to ask you to turn it down.\""
    vt_you "\"Mmf— sorry—\""
    "You say it with your mouth full. He laughs, helpless, and his hips jerk."
    vt_darren "\"I'm— [vt_pc_name], I'm gonna—\""
    show cg vt_t3_ask onlayer cgl
    "You pull off. You look up at him with your lips wet. You cover your mouth with your hand, and blush, and ask:"
    vt_you "\"Is it okay if I taste you?\""
    vt_darren "\"...Yeah. Yes.\""
    show cg vt_t3_cum onlayer cgl
    "He comes across your tongue and your chin." with vnfx("flash")
    vn_sfx "Splt. Splt."
    "You catch what runs down your chin on your fingers and lick them clean, one at a time, and you come untouched in your shorts while you do it, your voice glitching up into a stutter:"
    vt_you "\"A-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_doorway", pc="shy", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t3_end")
    "You look up at him from the doormat, cum on your fingers, your shorts wet, your hand over your mouth."
    vt_you "\"Sorry. Could I— could I have more? If that's okay?\"\n{size=-5}{color=#ff8fa3}▸ Thursday{/color}{/size}"
    jump vt_teal_four

## ---- rung 4: IN SYNC (First Date Etiquette) ------------------------------------------------------

label vt_teal_four:
    call vt_gap("Thursday.", 24, 8)
    $ vt_grow(4)
    $ vt.fit = "work"
    $ vn_enter(bg="vt_kiosk", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg="vt_t4_shirt")
    "{color=#ff5fb8}Your chest has outgrown your shirts. Your work shirt's buttons are pulling into little gaping eyes all down the front, and your tits push out between them, round and soft, bigger than handfuls now.{/color}"
    "{color=#ff5fb8}Your waist has pulled in. Your thighs are thicker in your jeans, rubbing when you walk. Your hair is at mid-back, and it's all teal now, every strand. Your cock is tiny. Your voice is nearly not yours at all.{/color}"
    "Lunch. You watch the new one on your phone behind the counter, hard under your apron."
    show screen vt_phone("t4")
    hide screen vt_phone
    show cg vt_t4_date onlayer cgl
    "Mio on a date with the faceless boyfriend. Dinner, blushing over the candle. Then his flat. Then she's bent over the arm of his couch with her skirt flipped up, apologising, and he takes her ass for the first time while she begs:"
    vt_mio "\"♪ Please, I want you inside me ♪\""
    "It ends as she comes, her voice glitching. The comments load."
    show screen vt_phone("t4")
    hide screen vt_phone
    call vt_again
    $ vn_enter(bg="vt_kiosk", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg=None)
    "Jesse takes one look at you over the counter, at the buttons, and comes round and takes you by the wrist."
    vt_jesse "\"Stockroom. Now. I've got a spare in my bag.\""
    jump vt_teal_four_stockroom

## Rung 4, part one: Jesse in the stockroom. His own; he wants her.
label vt_teal_four_stockroom:
    $ vt.fit = "bra"
    $ vn_enter(bg="vt_stockroom", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "flushed")], cg="vt_t4_bra")
    "The hobby shop's stockroom: shelves of paint pots and model kits, one bare bulb. She digs a bra out of her bag and hands it to you."
    vt_jesse "\"It's a C. Should be a— oh. Oh my God. It fits.\""
    "It fits. It fits perfectly, and you both stare at it, and then she's laughing, delighted, and you're laughing with your hand over your mouth."
    vt_jesse "\"Let me see it properly.\""
    show cg vt_t4_jesse onlayer cgl
    "And then you're kissing her against the shelves, and you're so into her, you're really, really into her, hard for her in your jeans, tiny and hard. You get her jeans open and your own and try to fuck her, and it barely reaches."
    vt_you "\"Sorry— sorry, I don't know what's—\""
    vt_jesse "\"Shh. C'mere.\""
    "She laughs, kind, and rides your fingers instead, two of them, her forehead on your shoulder, and comes on them with a gasp into your neck. And you're close, so close, and you can't get there, however hard you rut against her hip."
    "Then she slips two fingers into your ass."
    show cg vt_t4_jesse_cum onlayer cgl
    "You come at once. Instantly. Like she flicked a switch." with vnfx("flash")
    vt_you "\"A-a-ah—!\"" with vnfx("shake")
    vt_jesse "\"Oh my God. That is the hottest thing I've ever seen in my {i}life{/i}.\""
    $ vn_until(21)
    jump vt_teal_four_sofa

label vt_teal_four_sofa:
    $ vt.fit = "home"
    $ vn_enter(bg="vt_sofa", pc="shy", pc_tag="vt_pc", cast=[("vt_darren", "calm")], cg="vt_t4_tv")
    "Night. Darren's on your sofa. You asked him over. You wanted it normal: two neighbours, a couple of beers, and the thing in the doorway put away where it belongs."
    vt_you "\"We're cool, right? That was— that was a one-off. I'm not— I'm kind of seeing Jesse. Sort of.\""
    vt_darren "\"Yeah. Course. We're cool.\""
    vt_you "\"I'll show you the new one. It's so dumb. As a joke.\""
    "You put it on the TV. As a joke."
    "The dinner. The candle. His flat. Mio bent over the arm of the couch on the screen, and her skirt flipping up—"
    show cg vt_t4_lean onlayer cgl
    "—and you're bent over the arm of your own sofa, with your hands pushing your boxers down, before you've decided anything."
    vt_you "\"Sorry— sorry! That's not— my hands, I'm not doing that—\""
    vt_darren "\"[vt_pc_name]?\""
    vt_you "\"Don't look! Sorry. I don't know why it— I'm not—\""
    "On the screen, Mio apologises. In front of the screen, so do you."
    vt_darren "\"Do you want me to—?\""
    vt_you "\"No. No, I don't, I'm not—\""
    "Your hips push back. Your hand reaches back on its own and finds his belt and pulls."
    jump vt_teal_four_scene

label vt_teal_four_scene:
    $ vn_enter(bg="vt_sofa", pc="protesting", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t4_open")
    "He's slow. He's so slow and careful about it, and he asks again, and your mouth says {i}I don't know{/i} and your ass pushes back onto the head of him, and he answers your ass."
    vt_you "\"Oh— oh God, sorry, I'm— {i}ah{/i}—\""
    vn_sfx "Shllk."
    "In. Your first time. It doesn't hurt. It's big and warm and slow and it fills you up like a deep breath, and on the screen the boyfriend's hips meet Mio's, and Darren's hips meet yours, on the same beat."
    show cg vt_t4_mid onlayer cgl
    "Every beat. When he pulls back on the screen, Darren pulls back. When Mio arches, you arch. You don't look at the TV."
    vt_you "\"I'm sorry— please— I don't— this isn't—\""
    "Your tiny cock bounces under you, hard and useless, slapping your thigh. Darren never touches it."
    call vt_voice(4)
    vn_sfx "Pap. Pap. Pap."
    "You can't get the protest out any more. It keeps turning into his name."
    "On the screen Mio's getting close. You can hear it in her breath. You can hear it in yours."
    show cg vt_t4_peak onlayer cgl
    "And you look back over your shoulder, into Darren's face, and you say it to him. Not to the screen. To him."
    vt_you "\"Please, I want you inside me.\""
    show cg vt_t4_cum onlayer cgl
    "You come when Mio comes. Exactly when. Untouched, clenching on him, your voice glitching on a bad note." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_sofa", pc="moaning", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t4_duet")
    "The video ends. Autoplay rolls into the old duet: Mio and the red one, dancing."
    vt_darren "\"Who's the red one?\""
    "He's still inside you. He's asking you about it while he's still inside you."
    vt_you "\"She's fine. I voted teal.\""
    "And he laughs and starts going again, slow, to the duet's beat this time, and you push back into it and ask him, very politely, sorry, if it's not too much trouble, for it harder.\n{size=-5}{color=#ff8fa3}▸ The week nothing uploaded{/color}{/size}"
    jump vt_teal_five

## ---- rung 5: AHEAD OF HER (The Week Nothing Uploaded) -- THE FLIP ------------------------------

label vt_teal_five:
    call vt_gap("The week nothing uploaded.", 31, 10)
    $ vt.fit = "work"
    $ vn_enter(bg="vt_kiosk", pc="shy", pc_tag="vt_pc", cast=[], cg="vt_t5_refresh")
    "There's no new upload. Three in the morning comes and goes and the channel sits there. You refresh it at the kiosk all week, between screens. Nothing."
    show screen vt_phone("t5")
    "Under the old video, people are asking."
    hide screen vt_phone
    $ vn_clock.day = 33
    $ vn_set_time(11, 0)
    $ vt.fit = "cos"
    $ vn_enter(bg="vt_con_hall", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "cos")], cg="vt_t5_cosplay")
    "Saturday. Overclock Con, in the big hall at the leisure centre. Jesse's cosplaying Kiki: a red drill wig, a choker, a fang she's painted on. And she's brought a spare Mio outfit for you."
    $ vt_grow(5)
    "{color=#ff5fb8}It fits you better than it ever fitted her. The white high-collared blouse strains over your chest, big now, really big, the teal ribbon at the throat sitting on top of two heavy curves. The pleated skirt is short over your new ass. The thigh-high boots are tight on your thick thighs.{/color}"
    "{color=#ff5fb8}She doesn't bother with a wig. She ties your own long teal hair up into twin tails, one each side, and stands back.{/color}"
    vt_jesse "\"Oh my God. You drew the little note on? On your thigh?\""
    "{color=#ff5fb8}There's a small teal quaver high on your left thigh, above the boot. You didn't draw it. It's faint, like a watermark.{/color}"
    vt_jesse "\"Committed. You're so committed.\""
    show cg vt_t5_photos onlayer cgl
    "Darren came along to carry the bags. All day people call you {i}Mio{/i} and ask for photos, and you blush, and cover your mouth, and say sorry, and love it. Your face is softer. When you laugh, the laugh is hers."
    $ vn_until(20)
    jump vt_teal_five_hall

label vt_teal_five_hall:
    $ vn_enter(bg="vt_con_hall", pc="shy", pc_tag="vt_pc", cast=[("vt_darren", "calm")], cg="vt_t5_dj")
    "The evening virtual-singer night, in the main hall. A DJ set of the channel's songs, the old videos on the big screen, the floor packed and jumping."
    "You take Darren's hand. Nobody makes you. You want to, so you do."
    show cg vt_t5_curtain onlayer cgl
    "You pull him through the crowd, behind the stage curtain, into a dim backstage corridor full of road cases, and you push him up against one, and you look up at him, and you ask, very politely, with your hand over your mouth."
    vt_you "\"Sorry. Can we?\""
    vt_darren "\"Here?\""
    vt_you "\"Please.\""
    "Nobody sees you. The bass thumps through the wall."
    jump vt_teal_five_scene

label vt_teal_five_scene:
    $ vn_enter(bg="vt_backstage", pc="moaning", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t5_open")
    "He lifts you onto a road case like you weigh nothing. Your skirt's round your waist and your boots are round his back and he's in your ass, the bass thumping through the case under you."
    vt_you "\"Oh— yes— sorry, I'm so loud— yes—\""
    vn_sfx "Pap. Pap. Pap."
    show cg vt_t5_change onlayer cgl
    "{color=#ff5fb8}And then, under you, between your legs, something gives. Your tiny cock shrinks. The last of it, drawing up and in, smaller, smaller, a little nub, and then nothing, and where it was the skin parts, soft and wet and opening, folding into lips, a slick little slit, a pussy, yours, right there on the road case.{/color}"
    "{color=#ff5fb8}It doesn't feel like losing anything. It feels like a sigh. Like something unclenching.{/color}"
    vt_darren "\"[vt_pc_name]—\""
    "His hand's on it. He's felt it."
    vt_you "\"Please. It's fine. Keep going.\""
    vt_darren "\"Can I—?\""
    vt_you "\"Yes. Please. Yes.\""
    show cg vt_t5_vaginal onlayer cgl
    "He pulls out of your ass and pushes into your pussy, slow, asking all the way, and it's your first time again, a new first time, so wet he slides in to the root in one go."
    vt_you "\"Oh— {i}oh{/i}— thank you— oh, thank you—\""
    call vt_voice(5)
    vt_darren "\"Your wig's amazing, by the way.\""
    vt_you "\"It's not a wig.\""
    show cg vt_t5_peak onlayer cgl
    "He's holding you up against the road case by your twin tails now, one in his fist, and you're going to come, and nobody has ever sung what you say next. It's yours."
    vt_you "\"Please don't stop, I'll sing louder.\""
    show cg vt_t5_cum onlayer cgl
    "You come on him with the bass in your spine, your voice glitching, and nobody hears it over the music." with vnfx("flash")
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    $ vn_enter(bg="vt_backstage", pc="moaning", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t5_end")
    "Darren doesn't stop. He fucks your new pussy against the road case with your twin tails in his fist, and you're begging him over the bass to keep going, keep going, please, and your voice is already glitching into the next one.\n{size=-5}{color=#ff8fa3}▸ Three in the morning{/color}{/size}"
    jump vt_teal_six

## ---- rung 6: THE UPLOAD IS HIM (Backstage, Then Play Me Again) ------------------------------------

label vt_teal_six:
    call vt_gap("Three in the morning.", 34, 3)
    $ vt.fit = "home"
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_t6_card")
    "The late upload finally drops."
    show screen vt_phone("t6a")
    hide screen vt_phone
    show cg vt_t6_backstage onlayer cgl
    "Mio at a con, in her own outfit, dragging her faceless boyfriend by the hand behind a stage curtain. A dim corridor. Road cases. He lifts her onto one, and the bass thumps, and she sings:"
    vt_mio "\"♪ Please don't stop, I'll sing louder ♪\""
    "You watch it in bed, thrilled, horny, your hand between your legs."
    vt_you "\"Best one yet.\""
    show screen vt_phone("t6a")
    hide screen vt_phone
    call vt_again
    $ vt_grow(6)
    $ vn_set_time(9, 0)
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bedroom", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_t6_morning")
    "{color=#ff5fb8}Morning. Your chest has swollen huge overnight. The biggest jump yet: two enormous soft tits, heavy, round, so big that Jesse's bra won't close round them at all, and your T-shirt rides up over them and stays up.{/color}"
    "{color=#ff5fb8}Your ass and thighs are full and soft, your waist tiny between. Your face in the mirror is nearly hers. Your voice is entirely hers. The quaver on your thigh is darker.{/color}"
    "You text Darren and Jesse the same message. Politely."
    "{i}would you both like to come over? sorry{/i}"
    "They both say yes in under a minute."
    $ vn_until(20)
    jump vt_teal_six_scene

## Rung 6: the threesome. Consensual.
label vt_teal_six_scene:
    $ vn_enter(bg="vt_bedroom", pc="shy", pc_tag="vt_pc", cast=[("vt_jesse", "flushed")], cg="vt_t6_titjob")
    "Your bed. Darren kneeling over you with his cock between your huge new tits, and Jesse kneeling beside you, holding them together round him with both hands, squeezing, narrating."
    vt_jesse "\"Look at that. He's disappearing. You can't even see him. [vt_pc_name], he's {i}gone{/i}.\""
    vt_you "\"Thank you— thank you both— sorry, is it too much? Are they too big? Sorry—\""
    hide vt_jesse
    show vt_darren calm at vn_cast_slot
    vt_darren "\"Don't you dare say sorry.\""
    vn_sfx "Shlp. Shlp. Shlp."
    "The head of him pops up between them at your chin every stroke, and you stick your tongue out for it, blushing, and say thank you every time."
    call vt_voice(6)
    show cg vt_t6_tits_cum onlayer cgl
    "Darren comes across your tits and your chin." with vnfx("flash")
    "Jesse leans down and licks it off you. Off your tits, off your chin, slow. Then she kisses you, and pushes it into your mouth with her tongue."
    $ vn_enter(bg="vt_bedroom", pc="moaning", pc_tag="vt_pc", cast=[("vt_darren", "dazed")], cg="vt_t6_bed")
    "Then Darren's between your legs, and in you, your pussy, slow and deep, and Jesse's lying beside you, kissing you, her hand down between you on your clit."
    vt_you "\"Jesse— I still— I want you, I still want {i}you{/i}—\""
    hide vt_darren
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"I know, babe.\""
    "She grins against your mouth."
    vn_sfx "Pap. Pap. Pap."
    show cg vt_t6_face onlayer cgl
    "{color=#ff5fb8}And it happens on the bed, while he's in you. Your jaw softens. Your nose. Your eyes, wider, lashes thick. Your lips. Your face finishes, and it's hers. Your hair pours out past the ends of the twin tails, longer, longer, to her full length, spilling off the bed. The quaver on your thigh goes dark teal. Your moan comes out, and it's wholly hers.{/color}"
    hide vt_darren
    show vt_jesse grinning at vn_cast_slot
    vt_jesse "\"Oh my God. Darren. Look at her.\""
    hide vt_jesse
    show vt_darren calm at vn_cast_slot
    vt_darren "\"I'm looking. God, she's— she's—\""
    vn_sfx "Bzzt."
    show cg vt_t6_phone onlayer cgl
    "Jesse's phone buzzes on the pillow. A notification."
    show screen vt_phone("t6b")
    "Jesse's a fan. She plays it."
    hide screen vt_phone
    "The audio is a shy girl's moans, high, sweet, glitching, in Mio's voice. It's the moans in this room. Right now. Nobody notices."
    vn_sfx "Knock. Knock. Knock."
    "Three knocks on the {i}other{/i} wall. The neighbour on the far side, about the noise."
    vt_you "\"Sorry!\""
    "In her new voice. She doesn't stop."
    show cg vt_t6_peak onlayer cgl
    "Darren's close. She's closer. She looks up into his face, and the phone on the pillow sings, and so does she, the same line, the same breath."
    $ vn_feat("Now I Say Please to Men")
    vt_teal_end "\"♪ Play me again. ♪\"" with vnfx("flash")
    call vt_route_return("Now I Say Please to Men")
