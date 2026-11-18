## THE STORY: chapters 3-5, Tuesday to Thursday (PLAN.md). The cock is gone on Tuesday's first line; the pussy shows only after.
## Tuesday Chris's bed; Wednesday the forest loops and the punishment night (first vaginal: Kanon); Thursday Maron's day, where
## the narration follows Maron and Mitsuru speaks only between her moments.

## ---- 3. Tuesday: lost minutes ------------------------------------------------------------------------------

label mrn_tuesday:
    $ mrn.fit = "nude"
    $ mrn_grow(3)
    $ vn_enter(bg="mrn_guestroom", pc="dazed", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_tuesday")
    "You know before you look. You lie under the canopy with both hands flat on your belly, and then you slide them down, and there's nothing to stop them."
    "{color=#ff5fb8}It's gone. Smooth, soft, pale skin, and then a pussy, a neat closed slit with full soft lips, and when you press, it parts, and it's already wet.{/color}"
    "{color=#ff5fb8}Your hips have spread in the night; your thighs touch now when you stand. Your breasts are rounder and heavier, a real handful each, a C cup if you've ever seen one.{/color}"
    "{color=#ff5fb8}Your hair brushes your jaw, mostly chestnut now, only a few dark threads left in it like ink in water.{/color}"
    "{color=#ff5fb8}You're a head shorter than you were on Saturday. The mirror shows a pale grown woman with wide, frightened eyes, about your age, standing where you used to stand.{/color}"
    mrn_you "\"That's mine. That's {i}me.{/i} Oh God. Oh God, that's me.\""
    "One finger, just to know. It slides in, and it's hot and tight and slick, and your back arches off the bed so hard you hit your head on the post."
    vn_sfx "Kuchu."
    mrn_you "\"Ahh— hah— no— no, don't, don't do this, stop touching it— ahh♡—\""
    "You take your hand away. It takes a very long time."
    $ vn_set_time(10, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_hall", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_hall_tailoring")
    "Kanon takes the uniform in at breakfast, standing you on a footstool in the hall with pins in her mouth: the waist in, the hips out, the bust let out, the hem raised to keep it at mid-thigh on your shorter legs."
    mrn_kanon "\"Hold still. You've lost fifteen centimetres since Saturday. I'll be up all night with this dress.\""
    mrn_you "\"Kanon-neesan. Yesterday, after. I— I folded the sheets.\""
    mrn_kanon "\"You did. Beautifully.\""
    mrn_you "\"I don't remember folding the sheets.\""
    mrn_kanon "\"No. You wouldn't.\""
    $ vn_set_time(15, 20)
    $ vn_enter(bg="mrn_parlour", pc="dazed", pc_tag="mrn_pc", cast=[], cg="mrn_parlour_lost")
    "It happens again in the afternoon."
    "You're on your knees in the parlour with a brush and a pail, and the clock on the mantel says ten past two, and you blink, and it says twenty past three."
    "The floor's done. The brass on the fender's polished. There are fresh roses in the vase on the piano that you don't remember cutting."
    "Your knickers are wet through, and there's a sweet, slow, satisfied ache between your legs, as if somebody's been touching you."
    "Somebody has. Your own fingers are sticky."
    menu:
        "An hour of your life is gone, and your body enjoyed every minute of it."
        "Write your name":
            "You find a pen in the bureau and write it on the inside of your wrist, in small, hard capitals, where the cuff of the uniform will hide it."
            "{i}MITSURU YOKOMIZO. 23. YOKOHAMA.{/i}"
            "So you'll know. So whoever's holding the pen next time will know whose hand it is."
            $ mrn.held += 1
        "Ask Kanon":
            $ vn_enter(bg="mrn_kitchen", pc="nervous", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_kitchen_ask")
            mrn_you "\"Where do I go? When I lose time. Where am I?\""
            mrn_kanon "\"Same place I went. Behind the eyes, half asleep. And she's out front in your place, doing your work, being good.\""
            mrn_you "\"Who is she?\""
            mrn_kanon "\"Maron. Who else? Every time your body feels good, she gets a little stronger. You can't stop feeling good. So.\""
            "She shrugs and goes back to her pastry. She was lost in the snow once, too. You wonder what her name was."
    $ vn_set_time(23, 30)
    $ mrn.fit = "nightgown"
    $ vn_enter(bg="mrn_chris_room", pc="flustered", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_bed_chris")
    mrn_chris "\"{b}Take off the nightgown and get into my bed, imouto.{/b}\""
    "Chris's bed is enormous and cold and smells of roses."
    "She lies on her side facing you, in nothing, pale as a statue, her full breasts heavy against the sheet, her silver hair everywhere. She draws you in against her by the waist."
    mrn_chris "\"Let me see what you've made for me.\""
    "Her cool fingers trace down your belly, over the smooth place where your cock used to be, and then down, and part you."
    vn_sfx "Kuchu."
    mrn_you "\"Ahh—!\""
    mrn_chris "\"Oh, Maron. So wet already. You've been thinking about this all day, haven't you? Or she has.\""
    "And then her mouth on your throat and the bite and the pull, and her fingers slow and sure between your legs, circling, sliding in, curling, in time with every swallow."
    vn_sfx "Tsupu. Kuchu. Kuchu."
    mrn_you "\"Onee-sama— ahh— ahh— it's too much, both at once, it's too— hahh♡—\""
    menu:
        "Her thumb finds the little hood at the top of your slit and presses."
        "Hold still":
            "You hold still. You grip the sheet and lock your hips and refuse to move, refuse to help her, refuse to give her anything but your body."
            "And then you look down, and your hand is moving. Your own hand, on top of hers, pressing her fingers in deeper. You didn't tell it to. You're holding still. Your hand isn't."
            $ mrn.held += 1
        "Push into her hand":
            "You give up. You roll your hips up into her fingers, chasing them, and she laughs into your neck and gives you more."
    "Your legs part wider on their own. Your back arches on its own."
    "Your other hand goes to your breast and squeezes, and a voice comes out of your mouth that's higher and sweeter than yours."
    mrn_maron "\"Onee-sama♡— there— there, please, Onee-sama, deeper♡—\""
    mrn_you "\"No— that's not— ahh— hahh—\""
    mrn_maron "\"Please, please♡— don't stop drinking— take it all— take all of me— ahh♡— AHH♡—!\"" with vnfx("flash", "shake")
    "You come with her teeth in your throat and three of her fingers inside you, a huge rolling wave that lifts your whole body off the sheet and goes on and on, and somewhere in the middle of it you stop being the one who's coming."
    $ mrn.maron += 1
    $ vn_enter(bg="mrn_chris_room", pc="serene", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_bed_after")
    "When you can think again, you're curled against Chris's breast and your own mouth is kissing the two marks it's just left on her skin, gently, gratefully, and Chris is stroking your hair."
    mrn_chris "\"There. That was her, wasn't it? Nearly a whole minute that time.\""
    mrn_maron "\"Mm. He's still here, Onee-sama. He's watching.\""
    mrn_chris "\"I know. Let him watch. He'll get tired of it.\""
    call mrn_cut(8, 1, "Wednesday. The fourth morning.")
    jump mrn_wednesday

## ---- 4. Wednesday: the forest loops ------------------------------------------------------------------------

label mrn_wednesday:
    $ mrn.fit = "nude"
    $ mrn_grow(4)
    $ vn_enter(bg="mrn_guestroom", pc="nervous", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_wednesday")
    "{color=#ff5fb8}Heavier. That's the first thing, before you even open your eyes: a weight on your chest, rolling when you breathe.{/color}"
    "{color=#ff5fb8}Your breasts have filled out in the night into two round, full, heavy things, an E cup at least, spilling over your arms when you sit up.{/color}"
    "{color=#ff5fb8}Your thighs are thicker, soft and strong, pressed together under the sheet. Your hair falls to your shoulders, all chestnut now, every last dark thread gone.{/color}"
    "{color=#ff5fb8}On your wrist, if you wrote it, the ink is still there. But the hand it's on is small and soft, with a woman's slim fingers. You're the height of Kanon's shoulder now. Short and curved and soft all over, a short, pale woman built like an hourglass.{/color}"
    "Three more nights. Three more bites, and you'll be her. And then whatever you are now will be asleep behind her eyes for good."
    mrn_you "\"Tonight. It has to be tonight.\""
    $ vn_set_time(14, 0)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_kitchen", pc="serene", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_kitchen_maron")
    "You lose most of the day."
    "You come back to yourself at the kitchen table, peeling chestnuts, humming, with your knickers soaked, and Kanon watching you from the stove with a look you can't read."
    mrn_kanon "\"She's good company, you know. Better than you.\""
    mrn_you "\"I'm not staying.\""
    mrn_kanon "\"No? Well. The snow's that way.\""
    $ vn_set_time(1, 20)
    $ mrn.fit = "nightgown"
    $ vn_enter(bg="mrn_pines", pc="nervous", pc_tag="mrn_pc", cast=[], cg="mrn_pines_escape")
    "One-twenty in the morning."
    "Chris drank early and lightly tonight and went to her coffin, or her bed, or wherever she goes, and nobody told you to stay in your room, so the bond doesn't hold you there."
    "You stand at the back door in a white nightgown and bare feet with your heart going like a train."
    menu:
        "The pines are black. Somewhere out there, the snow line."
        "Run for the trees":
            "No coat, no boots, nothing. You just run, and the needles are soft and dry under your bare soles, and the moon runs alongside you through the trunks."
        "Take a coat first":
            "You take Kanon's long black coat from the hook by the door. It drags on the ground behind you like a train. It smells of her. You run."
            $ mrn.held += 1
    "You run downhill, the way you came. Ten minutes. Twenty."
    "Your breasts bounce painfully under the thin nightgown and your new hips throw your stride off and you run anyway, and the trees go on and on, and there's no edge, there's no snow, there's no wall of white roaring in the dark."
    "And then the trees open, and there's a clearing, and in the clearing there's a big Western house with a light in one window."
    "You turn round. You run uphill this time. Forty minutes, until your thighs burn and your lungs scream."
    $ vn_enter(bg="mrn_gate", pc="protesting", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_gate_caught")
    "The iron gate. The white gravel. Kanon, waiting on the step with a lamp, in her nightdress, looking bored."
    mrn_kanon "\"Every time. I did it too, you know. Four times. The forest's hers. Come in, you're letting the cold in.\""
    $ vn_set_time(2, 30)
    $ mrn.fit = "nude"
    $ vn_enter(bg="mrn_chris_room", pc="protesting", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_punish_kneel")
    "Chris is sitting up in bed when Kanon brings you in. She doesn't look angry. That's worse."
    mrn_chris "\"You ran from me, imouto.\""
    menu:
        "You're kneeling on her carpet. You don't remember kneeling."
        "Apologise":
            mrn_you "\"I'm sorry. I'm sorry, Onee-sama. I just— I had to see if—\""
            mrn_chris "\"I know you did. Everybody has to see. Kanon had to see four times.\""
        "Defy her":
            mrn_you "\"I'm not your imouto. I'm not your sister and I'm not your maid and I'm not Maron, and I'll run every night till one night it works.\""
            mrn_chris "\"Will you? Oh, I do hope so. It's so much nicer when you fight.\""
            $ mrn.held += 1
    mrn_chris "\"But a running maid gets punished. Those are the house's rules for its imouto, and you knew them. Kanon.\""
    mrn_kanon "\"Mistress.\""
    mrn_chris "\"She's got something new since Tuesday that nobody's had yet. I think you should be the first. {b}Lie back on the bed, Maron, and open your legs for your Kanon-neesan.{/b}\""
    hide cg onlayer cgl  # d1 6:42 am 11-18: no picture, punish-kanon failed v1 (QA), v4 and v5 (SCENES.md maron QA fixes)
    "Your body lies back on the bed and opens its thick soft thighs as wide as they'll go. Kanon lifts her nightdress off over her head."
    "She's beautiful, broad-shouldered and full-breasted, and her cock is hard and heavy and bobbing between her thighs, bigger than you remember."
    "Chris lies down beside you and turns your face towards her with one finger."
    mrn_chris "\"Look at me while she does it.\""
    "The head of Kanon's cock nudges your lips apart, slick and hot, and stops there, and holds."
    mrn_you "\"Kanon-neesan— don't— please don't, not there, not my— that's not mine, I didn't ask for it, please—\""
    mrn_kanon "\"Shh. Breathe out, imouto.\""
    "And she pushes in."
    vn_sfx "Zupuu."
    mrn_you "\"AHH— ahh— it's in— it's {i}inside{/i}— it's so deep, it's so big, it's stretching me— ahh♡— ahh♡—\""
    "It doesn't hurt. You'd almost have wanted it to."
    "It just fills you, inch by inch, a long thick hot slide all the way to the end of you, until her hips press flush against yours and you can feel her heartbeat inside you."
    "There's nothing in the world but the stretch and the fullness and Chris's red eyes, watching you take it."
    vn_sfx "Pan. Pan. Pan."
    "Kanon starts to fuck you."
    "Deep, steady, unhurried strokes that rock your whole soft body up the bed, your heavy new breasts bouncing on your chest, the bed creaking, the wet noise of it loud in the quiet tower."
    mrn_you "\"Ahh♡— ahh♡— hah— it's— it's so good— why is it so good— don't stop— I mean— I mean—\""
    mrn_chris "\"Mean whatever you like, darling. It's all the same to your body.\""
    show cg mrn_punish_thigh onlayer cgl
    "Chris slides down the bed, past your breasts, past your belly, and puts her mouth to the soft inside of your thigh, right where it meets the crease of your hip, a hand's width from where Kanon's splitting you open."
    vn_sfx "Tsupu."
    "The bite. The pull."
    "And a thousand times more than at your throat, because it's right there, right next to it, the heat of her drinking and the heat of Kanon fucking you meeting in the middle in one white-hot point."
    mrn_you "\"AHH♡— both— both at once— Onee-sama— Kanon-neesan— I'm going to— I'm— I'm— AHHH♡—!\"" with vnfx("flash", "shake")
    "You come."
    "Your new pussy clamps round Kanon's cock in long rippling pulses and your back arches and your toes curl and you scream it up at the canopy, and Chris drinks through it, and Kanon fucks you through it, and it doesn't stop."
    "It just turns into the next one."
    $ mrn.maron += 1
    mrn_maron "\"More♡— more, Kanon-neesan, please, harder♡— I've been so bad, I ran, I ran away from you, punish me, punish me♡—\""
    mrn_you "{i}That's not— that's not me, I'm not saying—{/i}"
    mrn_maron "\"Onee-sama, drink, drink more, take it all— I'm yours, I'm yours, I'm {i}yours♡{/i}— AHH♡—!\"" with vnfx("flash", "shake")
    vn_sfx "Dopyu. Dopyu. Dopyu."
    "Kanon groans and drives in to the hilt and comes inside you, and you feel every hot pulse of it fill you up, and the voice that's using your throat laughs with joy, a gasping, giddy joy, and keeps going."
    $ mrn.maron += 1
    "You don't know how many times. You lose count at four. Somewhere around five, you stop being the one counting."
    $ vn_set_time(5, 0)
    $ vn_enter(bg="mrn_chris_room", pc="blissful", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress"), ("mrn_kanon", "headmaid")], cg="mrn_punish_after")
    "When you come back it's nearly dawn and you're lying between them in the big bed, sticky and spent and glowing, and your own mouth is talking."
    mrn_maron "\"I won't run again, Onee-sama. I promise. I'll be so good.\""
    mrn_chris "\"I know you will, Maron. Is he still there?\""
    mrn_maron "\"A little. He's very quiet. I think he liked it.\""
    "You want to scream that you didn't. But your body's warm and full and sleepy, and you don't have the mouth to say it with."
    call mrn_cut(10, 1, "Thursday. The fifth morning.")
    jump mrn_thursday

## ---- 5. Thursday: Maron's day ----------------------------------------------------------------------------

label mrn_thursday:
    $ mrn.fit = "nude"
    $ mrn_grow(5)
    $ vn_enter(bg="mrn_maid_room", pc="serene", pc_tag="mrn_pc", cast=[], cg="mrn_mirror_thursday")
    "She wakes up first."
    "She's moved into the little maid's room at the top of the back stairs, the one with the iron bed and the rag rug and the window onto the roses. Kanon carried her there at dawn."
    "She stretches in the narrow bed like a cat and smiles at the ceiling."
    "{color=#ff5fb8}She gets up and looks in the little mirror on the washstand, and likes what she sees. She's shorter again: the washstand comes to her ribs now.{/color}"
    "{color=#ff5fb8}Her breasts are bigger, so heavy they sway when she turns, so full they press together into a deep soft cleft without any help.{/color}"
    "{color=#ff5fb8}Her hips are wide, her thighs thick, and her chestnut hair falls past her shoulders in soft waves.{/color}"
    mrn_maron "\"Good morning, me.\""
    "And somewhere behind her eyes, very small, you say:"
    mrn_you "{i}...Good morning.{/i}"
    mrn_maron "\"Oh! You're awake. I wasn't sure you would be.\""
    $ vn_set_time(9, 30)
    $ mrn.fit = "maid"
    $ vn_enter(bg="mrn_parlour", pc="serene", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_parlour_tea")
    "She does the tea. Assam, the pot warmed first, four minutes exactly, a curtsey from the hem, eyes down. She does it better than you ever did it."
    "Chris takes the cup and kisses the back of her hand."
    mrn_chris "\"Good morning, Maron.\""
    mrn_maron "\"Good morning, Onee-sama. Did you sleep well?\""
    mrn_chris "\"Like the dead. And how's our guest?\""
    mrn_maron "\"Grumpy.\""
    "Chris laughs, a real laugh, bright and young. You've never made her laugh. You've never even tried."
    $ vn_set_time(13, 0)
    $ vn_enter(bg="mrn_laundry", pc="moaning", pc_tag="mrn_pc", cast=[("mrn_kanon", "headmaid")], cg="mrn_laundry_maron")
    "Down in the laundry at one o'clock she finds Kanon at the copper, and she doesn't wait to be told."
    "She lifts her own short black skirt at the back and bends over the table, the same table, and looks back over her shoulder."
    mrn_maron "\"Kanon-neesan. You've been working so hard. Won't you take a rest?\""
    mrn_kanon "\"Cheeky.\""
    "But Kanon's already lifting her skirts."
    "And it's so different from the inside, now: you're there, behind the eyes, feeling every inch of it, the slow stretch, the fullness, the long thick slide all the way into a pussy that's wet and ready and {i}wants{/i} it, and you can't move a finger."
    vn_sfx "Zupuu. Pan. Pan. Pan."
    mrn_maron "\"Ahh♡— yes, yes, Kanon-neesan♡— right there, oh, right there, it's so deep— harder, please, make me loud, I love being loud for you♡—\""
    mrn_you "{i}Stop it. Stop. This is my body, this is—{/i}"
    mrn_maron "\"It's {i}our{/i} body, silly— ahh♡— feel it, feel how good— feel it with me— hahh♡— AHH♡—!\"" with vnfx("flash", "shake")
    "And you do. You feel it with her. That's the worst of it. You come when she comes, both of you at once, and it's the best thing you've ever felt, and she knows it."
    $ mrn.maron += 1
    $ vn_set_time(16, 30)
    $ vn_enter(bg="mrn_maid_room", pc="dazed", pc_tag="mrn_pc", cast=[], cg="mrn_maid_room_talk")
    "In the afternoon she sits on the iron bed with her knees drawn up and talks to you. Out loud, because there's nobody to hear, and it's easier."
    menu:
        "She waits for you to say something."
        "Tell her to give it back":
            mrn_you "{i}Give it back. My body. My life. I had a flat. I had a job. People will be looking for me.{/i}"
            mrn_maron "\"Will they? Who? Your boss? You hated him. Your mother? You call her at New Year. You walked up a mountain alone so somebody would notice you'd done something.\""
            mrn_you "{i}...{/i}"
            mrn_maron "\"I noticed. Onee-sama noticed. Kanon-neesan notices every single thing you do wrong, and she {i}tells{/i} you. Nobody ever noticed you before, did they?\""
            $ mrn.held += 1
        "Ask her who she is":
            mrn_you "{i}Who are you?{/i}"
            mrn_maron "\"I'm you. The you the bite makes. The you that was always under there, I think, under the cold and the suit and the being on your own. Onee-sama's blood just woke me up.\""
            mrn_you "{i}You're not me. I'd never say the things you say.{/i}"
            mrn_maron "\"You say them every time you come. I only say them louder.\""
            $ mrn.maron += 1
    mrn_maron "\"I'm not trying to get rid of you, you know. I like you. You're warm, in the back there. I just want you to stop pulling.\""
    $ vn_set_time(23, 30)
    $ mrn.fit = "nude"
    $ vn_enter(bg="mrn_bath", pc="blissful", pc_tag="mrn_pc", cast=[("mrn_chris", "heiress")], cg="mrn_bath_chris")
    "At half past eleven she bathes Chris, in the big tiled bathroom with the clawfoot tub and the steam on the black windows, both of them naked, her small soft body kneeling in the water between Chris's long pale legs, washing Chris's silver hair."
    "Chris bites her in the bath, with her heavy breasts floating in the water and Chris's fingers working between her thick thighs, and she comes so loudly the pipes ring."
    vn_sfx "Tsupu. Chapu. Chapu."
    mrn_maron "\"Onee-sama♡— Onee-sama♡— thank you, thank you, I love it, I love being yours— AHH♡—!\"" with vnfx("flash", "shake")
    $ mrn.maron += 1
    "You're there for it. You're always there for it now. Somewhere at the back of the bright warm room of her, curled up small, watching your own body be happy."
    call mrn_cut(10, 1, "Friday. The sixth morning.")
    jump mrn_friday
