## THE SOURCE: livestock's passages, rewritten for the VN (2026-11-11; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, ending.twee), as beats; the director scenes are in scenes.rpy.

## ---- day 1: the intake (Livestock Opening, Intake, Trough One) ---------------------------------------------

label ls_opening:
    $ ls_init()
    $ ls.fit = "own"
    $ vn_enter(bg="ls_farmers_centre", pc="defiant", pc_tag="ls_pc", cast=[], cg="ls_clipboard")
    show cg ls_clipboard onlayer cgl
    "The farmers' centre on Harvest Street, first thing. Feed sacks. Wellies. A corkboard of jobs."
    "Your rent was due last week. Your card says {i}declined{/i}. Your landlord says worse."
    "One card on the board has a clipboard nailed under it. {color=#ffd700}SEASONAL HELP — MARSH FARM — ROOM AND BOARD — TRANSPORT PROVIDED{/color}"
    "Room. Board. {i}Free.{/i} There's a page of small print under it. You don't read the small print. There's one box left at the bottom, and it says {color=#ffd700}STOCK{/color}, so that's where you sign."
    ls_counter "\"That'll be the lorry.\""
    "Without looking up."
    show cg ls_lorry onlayer cgl
    "Outside, a stock lorry idles at the kerb. Slatted sides. Straw on the floor. The tailgate's down."
    "You climb in. The straw's warm. The engine hums. You're asleep before the edge of town.\n{size=-5}{color=#ff8fa3}▸ Climb in the back{/color}{/size}"
    $ vn_until(13)
    jump ls_intake

label ls_intake:
    $ ls.fit = "blanket"
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_straw")
    show cg ls_wake_straw onlayer cgl
    "You wake up in straw."
    "Warm straw, in a hay-padded stall, behind wooden rails. Rows of stalls down a long barn. Somebody nearby chewing. Somebody else mooing, soft and lazy."
    "Your left ear throbs. You touch it. A plastic tag, punched clean through."
    "And your clothes are gone. All of them. There's a blanket."
    show cg ls_card_struck onlayer cgl
    show ls_hester flat at vn_cast_slot
    "A card hangs on the gate. {color=#ffd700}MARSH FARM — INTAKE. CLASS: HEIFER. SEX: FEMALE.{/color}"
    ls_you "\"Heifer?\""
    "The woman with the clipboard is at the rail. Rubber boots. Hawk nose. Fifty-odd and unimpressed by everything. She looks you over, and then she looks right at your crotch."
    "She takes the card down. Strikes out FEMALE, one neat line. Writes underneath, in capitals."
    $ ls_advance(1)
    show screen ls_card
    ls_you "\"There's been a mistake. I signed up for seasonal help, I'm not—\""
    ls_hester "\"Transit's paid. Forms are final once the tag's punched.\""
    vn_sfx "Click."
    ls_hester "\"I don't do refunds.\""
    hide screen ls_card
    "She hangs the card back on the gate."
    ls_hester "\"Hester Marsh. My farm. Rules are simple. All stock milks at nine p.m. Both ends. No exceptions.\""
    ls_you "\"Both—\""
    ls_hester "\"{i}Ends.{/i}\""
    hide ls_hester
    "And she's gone down the aisle."
    show ls_buttercup grin at vn_cast_slot
    "Over the partition a head pops up. Honey-blonde hair, a garland of clover round two pretty curved horns, soft cow ears, chewing. Tall. Very tall. Very, {i}very{/i} stacked."
    ls_buttercup "\"Don't mind Hester, sugar. She means it, but she means it nicely. I'm Buttercup. Discrepancy! Ooh. You'll be fun.\"\n{size=-5}{color=#ff8fa3}▸ Eat your mash{/color}{/size}"
    hide ls_buttercup
    jump ls_trough_one

label ls_trough_one:
    $ vn_enter(bg="ls_long_barn", pc="defiant", pc_tag="ls_pc", cast=[], cg="ls_trough")
    show cg ls_trough onlayer cgl
    "The trough runs the length of the barn, warm mash heaped down the middle, and the herd's already at it. Cow-girls. Pink, curly-tailed sow-girls. Faces in the feed."
    "You go to scoop some with your hand."
    vn_sfx "Slap."
    show ls_petal bossy at vn_cast_slot
    ls_petal "\"No hands, sugar. Petal. Mash room. Faces in. Go on.\""
    "A pink hand smacks your wrist. Curly hair, a curly tail, a bossy grin."
    hide ls_petal
    "Buttercup kneels next to you and shows you: chest up, lips loose, a long flat lick through the mash."
    vn_sfx "Shlllk."
    ls_buttercup "\"Like that. Don't bite. Breathe through your nose.\""
    "You put your face in the trough. It's sweet. Creamy-sweet, warm, and it slides down your throat like it's been waiting for you. You go back in before you've decided to."
    "By the third mouthful you've got mash on your nose and your cock is half hard under the blanket and you have {i}no{/i} idea why."
    ls_petal "\"Ooh. Somebody likes breakfast.\""
    ls_you "\"I don't— that's not—\""
    ls_buttercup "\"Sugar, nobody here minds. Wait till nine. You'll see.\""
    "She licks her lips clean, slow, and stretches, and her tits roll under her smock like two warm hams."
    ls_you "\"What happens at nine?\""
    "The two of them look at each other, and grin, and say nothing at all."
    hide cg onlayer cgl
    "The afternoon goes slow. Straw. Dozing. Moos. Down the far end a cow-girl moans in her sleep, long and happy, and you lie there with your face hot listening to her."
    "Then the light goes gold through the slats, and every head in the barn comes up at once.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

## ---- the nine o'clock milking, every night (Livestock Bell, the <n> Milking, Livestock Night) ------------

label ls_bell:
    $ ls.fit = "nude"
    $ _ls_r = ls.tier
    $ vn_enter(bg="ls_milking_frame", pc="shocked", pc_tag="ls_pc", cast=[], cg=None)
    show bg ls_milking_frame onlayer bgl
    if _ls_r == 1:
        vn_sfx "DONG. DONG. DONG." with vnfx("shake")
        "A brass bell on the crossbeam. The whole barn gets up and files down the aisle, cups clinking. You stay put. Petal takes one of your arms and Buttercup takes the other, and your heels plough two lines in the straw all the way to the far end."
        ls_you "\"Hey— {i}hey{/i}— I didn't agree to any—\""
        show cg ls_frame onlayer cgl
        "The frame. A padded bench on a haybale, a bar with leather straps on it, steel cups on hoses, and a back line with a long silicone plug on the end of it. Two tanks behind it all, glass, one for each line."
        "Hester pulls on a glove."
    elif _ls_r == 7:
        show bg ls_trailer onlayer bgl
        "The fair's bell rings nine over the showground. In the trailer the portable frame's already out, chrome and padded leather, straps open, and the other farms crowd the door to watch. Marigold steers you to it by the bell."
    elif _ls_r == 8:
        vn_sfx "DONG. DONG. DONG."
        "The herd parts for you down the aisle. Marigold's hand is on the back of your neck the whole way. Hester's already at the frame, and there's something different about it tonight."
    else:
        vn_sfx "DONG. DONG. DONG."
        "Nine o'clock. The herd files down the aisle. You dig your heels in, and Petal's hand in the small of your back walks you there anyway. Your body knows the way now, even if you don't."
        if _ls_r == 2:
            "Your hole twitches when you see the plug on its hook. Your mouth waters when you see the back tank."
        elif _ls_r == 3:
            "Your puffy nipples are standing straight out before you've even reached the bench. The bell on your collar tinks all the way down the aisle."
        elif _ls_r == 4:
            "Your new tits bounce with every step and the cow-girls in the line nudge each other and grin."
        elif _ls_r == 5:
            "You walk it with the cage between your legs and your tits so full they're shining. There's a milk glass on the shelf behind Hester. You've never seen the glass before."
        else:
            "You're leaking before the bell's even finished. Hester has to step round the drips."
    $ _ls_v = LS_VESSEL[_ls_r]
    menu:
        "Hester sets [_ls_v] under your chest line."
        "Struggle":
            $ ls.take = "struggle"
        "Swear":
            $ ls.take = "swear"
        "Grit your teeth":
            $ ls.take = "grit"
    $ _ls_t = ls_take_line(_ls_r)
    "[_ls_t]"
    $ renpy.jump("ls_milking_%d" % _ls_r)

label ls_night:
    $ _ls_r = ls.tier
    $ vn_enter(bg="ls_stall", pc="flushed", pc_tag="ls_pc", cast=[], cg=None)
    show bg ls_stall onlayer bgl
    if _ls_r == 1:
        "Back in your stall, shaking. Hester writes on her clipboard on the way past and doesn't stop."
        "Buttercup's arm comes over the partition and pats your head."
        ls_buttercup "\"Every night, sugar. You'll stop shaking by Thursday.\""
    elif _ls_r == 2:
        "Hester takes the card off your gate, writes, puts it back. You read it upside down. {i}Double mash.{/i}"
        ls_you "\"I'm not eating it.\""
        "You tell the rafters. Your mouth waters anyway."
    elif _ls_r == 3:
        "You lie in the straw and touch your nipple, and your finger comes away wet. The bell on your collar tinks every time you breathe."
        ls_you "\"[ls_pc_name]. My name's {i}[ls_pc_name]{/i}.\""
        ls_buttercup "\"Night, Cherry.\""
        "Over the partition, and your nipples go hard at it."
    elif _ls_r == 4:
        "Out in the yard the twins are scrubbing the gutters in the dark, and grumbling, and you can hear every word."
        ls_you "\"Good. {i}Good.{/i}\""
        "Your hole twitches at their voices anyway."
        ls_billy "\"Worth it.\""
        ls_bart "\"{i}So{/i} worth it.\""
    elif _ls_r == 5:
        "The cage sits cold between your legs and your tits are full again already, heavy and throbbing. You fall asleep with one hand on each."
        "{i}She.{/i} You keep hearing it. Hester said it like it was a column on a form."
        ls_cherry "\"{i}He.{/i}\""
        "Out loud, to nobody. It comes out high and soft, and your tits leak at the sound of it."
    elif _ls_r == 6:
        "You can't sit down properly. You lie face-down in the straw with your ass in the air and your tits pillowing your cheek, swearing at the rafters, and your hole won't stop clenching on the memory of him."
        "Outside the snow comes down. Inside the barn's warm with bodies, and Angus's slow deep snore comes down the aisle like the sea."
    elif _ls_r == 7:
        show bg ls_trailer onlayer bgl
        "The trailer rocks you home in the dark, your ribbon on your chest, Buttercup's head on your shoulder."
        ls_buttercup "\"Blue ribbon. First go. Nobody does that.\""
        "Half asleep. She pats your tit like a pillow and goes back to sleep on it."
    else:
        "You sleep in Marigold's stall tonight. You try for your own gate twice, and twice her arm comes over you, heavy and warm, and hauls you back into the straw."
        ls_marigold "\"Mine now, Cherry. Sleep.\""
        "Her tits leak on your back, and yours leak on the straw. Your hand keeps drifting down between your legs. Just to check. Every time, it's still there, wet and soft, and every time you moan into her arm, and every time she chuckles."
    show screen ls_card
    "{color=#b7b7b7}The card on the gate.{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen ls_card
    call vn_night(6)
    $ renpy.jump("ls_day_%d" % (_ls_r + 1))

## The morning chore, days 2-6: flavour, one of three.
label ls_chore:
    $ _ls_d = ls.tier + 1 if (ls.tier or 0) < 6 else 6
    menu:
        "{color=#ffd700}Morning chores.{/color}"
        "The mud pen with Petal":
            $ _ls_c = "mud"
        "The ring walk with Buttercup":
            $ _ls_c = "ring"
        "Watching Marigold milked":
            $ _ls_c = "watch"
    $ renpy.show("cg ls_chore_%s_%d" % (_ls_c, max(2, min(6, ls.tier + 1))), layer="cgl")
    $ _ls_ct = LS_CHORES[_ls_c][1][max(2, min(6, ls.tier + 1))]
    "[_ls_ct]"
    hide cg onlayer cgl
    return

## ---- rung 1's milking (Livestock One Milking) ---------------------------------------------------------------

label ls_milking_1:
    show cg ls_milk_1_strap onlayer cgl
    ls_hester "\"Bench. Face down.\""
    ls_you "\"No. {i}No.{/i} I'm not getting on that—\""
    "Petal and Buttercup put you on it. Face down on the padded bench, on the haybale, blanket gone, knees in the straw. Hester buckles a leather strap round one wrist on the bar."
    vn_sfx "Snk. Snk."
    "Then the other. You yank. The bar doesn't care."
    ls_you "\"Let me {i}up{/i}— this is— you can't just—\""
    "She fits the cups over your nipples. Cold. {i}Thnk-thnk-thnk{/i}, and they suck. There's nothing there to suck. Flat chest, little pink nipples, tugged out and let go, tugged out and let go."
    "Then cold lube, right on your hole."
    ls_you "\"Wh— hey— {i}HEY{/i}— not there— don't you {i}dare{/i}—\""
    ls_hester "\"Breathe out.\""
    show cg ls_milk_1_plug onlayer cgl
    "She doesn't wait for you to. You thrash, and she holds your hip down with one rubber glove like she's done it a thousand times, and the plug pushes in, fat and smooth and slick, and it slides and slides and seats, and the tip of it sits right on—"
    ls_you "\"{i}Ohhh{/i}—! No— get it {i}out{/i}— get it—\"" with vnfx("shake")
    vn_sfx "Vrrrrmm."
    "The machine starts. The plug pulses, right {i}there{/i}, on a spot you didn't know you had, over and over and over. Your cock's hard in no time at all. Bouncing under you. Untouched."
    ls_you "\"Wait— wait wait wait— {i}stop{/i}— I'm— {i}nobody's even touching it{/i}—!\""
    show cg ls_milk_1_cum onlayer cgl
    ls_you "\"No no no no— {i}ahhh{/i}—!\""
    "You go off. Howling. Your whole body locks against the straps and your cock spurts into the tray under you, rope after rope, untouched, and the back line sucks it all up the hose, {i}shlp shlp shlp{/i}, into the glass tank behind you." with vnfx("flash")
    ls_you "\"Turn it {i}off{/i}— turn it— {i}ahh{/i}— {i}AHH{/i}—\""
    "The plug doesn't stop. You go off again. Thinner. Dribbling. Your toes curl in the straw and you're screaming like nobody's listening, and the whole barn is listening."
    show cg ls_saucer_dry onlayer cgl
    "The cups on your chest go {i}thnk, thnk, thnk{/i}, sucking at nothing. Hester taps the saucer under your chest line. {i}Tink.{/i} Dry."
    ls_hester "\"Not a saucer's worth.\""
    show cg ls_marigold_rail onlayer cgl
    show ls_marigold fond at vn_cast_slot
    "A shadow falls over the rail. A {i}big{/i} one. A woman a head and a half taller than anybody: brown skin dappled cream down her thighs, heavy curved horns, soft cow ears, a tufted tail swishing."
    "Tits like nothing you've ever seen, enormous, leaking two wet streaks down her apron. And under the apron, swinging heavy, a thick ridged cock."
    "She reaches over the rail and tips your jaw up with one finger, so you're looking at the dry saucer with her."
    ls_marigold "\"Discrepancy, huh.\""
    ls_you "\"Get me— {i}hah{/i}— get me {i}out{/i} of this—\""
    "She smiles, slow, fond, like you're a gate that sticks. Lets go. Walks off down the line."
    hide ls_marigold
    ls_buttercup "\"That's Marigold. Boss of the line. Oooh, she {i}looked{/i} at you.\"\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 2: her contribution (Livestock Day Two, Mash Room, Two Tap, Two Tap After, Two Milking) ---------

label ls_day_2:
    $ ls_body(1)
    $ ls.fit = "blanket"
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_2")
    show cg ls_wake_2 onlayer cgl
    "You wake up and the blanket feels {i}wrong{/i}."
    "{color=#ff5fb8}Too smooth. You run a hand down your shin. Nothing. Your arm. Nothing. Your chest, your belly, the little trail down to your cock. Gone. Every bit of you, smooth as the inside of your wrist.{/color}"
    "{color=#ff5fb8}Your skin's gone soft. And your nipples. Pink and tender, and when your thumb brushes one—{/color}"
    ls_you "\"{i}Hah{/i}—!\""
    "You do it again. And again. Your cock twitches up hard under the blanket. From {i}nipples.{/i}"
    ls_you "\"It's the feed.\""
    "You tell the ceiling. You lick your lips after you say it, and your own tongue on your own lips feels like a kiss."
    hide cg onlayer cgl
    show bg ls_long_barn onlayer bgl
    "Breakfast is the trough. Faces in. Petal smacks your hand away before it's even moving."
    show ls_buttercup grin at vn_cast_slot
    ls_buttercup "\"Now the important bit. {i}Mmmmooooo.{/i}\""
    "She leans in and lets one out, low and round and long, right from her chest. Her tits jiggle with it."
    ls_buttercup "\"Your go.\""
    ls_you "\"I'm not—\""
    ls_petal "\"Moo for it.\""
    "Petal holds up a candied apple slice. You want the apple slice. You want it a ridiculous amount."
    ls_you "\"Mm— {i}mmh{/i}— mm—\""
    "It comes out strangled, half a moo, half a cough. Petal laughs so hard she snorts. Buttercup claps."
    ls_buttercup "\"Close! Give it a week.\""
    hide ls_buttercup
    call ls_chore
    jump ls_mash_room

label ls_mash_room:
    $ ls_advance(2)
    $ vn_enter(bg="ls_mash_room", pc="shocked", pc_tag="ls_pc", cast=[("ls_petal", "bossy")], cg="ls_jar")
    show cg ls_jar onlayer cgl
    "Petal drags you into the mash room by the wrist. Steam, a big steel mixer, sacks of grain, and a shelf of glass jars."
    "She hefts one down. Thick and white and swirly, sloshing. The label says {color=#ffd700}BARN CONTRIBUTIONS.{/color}"
    ls_petal "\"Back tank goes in here. Whole herd's. Every night. That one's yours.\""
    ls_you "\"Wait, is that— is that {i}cum{/i}?\""
    ls_petal "\"Protein's protein.\""
    "She ladles a big white glop of it into the mash, and stirs. That's why it was so sweet. That's why you went back for more."
    ls_you "\"No. {i}No.{/i} I'm not eating that. I'm not eating {i}my own{/i}—\""
    show cg ls_bowl onlayer cgl
    "Petal puts the bowl on the floor, puts a hand on the back of your head, and puts your face in it."
    vn_sfx "Splt."
    ls_you "\"Mmf— {i}mmnf{/i}—!\""
    "You push up. She leans. You're stronger than a sow-girl. You're not stronger than a sow-girl who's leaning."
    "Salty-sweet and thick and warm, on your lips, on your tongue, and your mouth starts lapping before you've told it anything. You moan into the bowl. You lick it clean. You hate every lick and you don't stop."
    ls_petal "\"Second helping's pride. Or it should be.\""
    "Letting go, wiping your chin with her thumb. In the afternoon Marigold sends for you. Petal takes your wrist again.\n{size=-5}{color=#ff8fa3}▸ Dragged to Marigold's stall{/color}{/size}"
    $ vn_until(14)
    jump ls_two_tap

label ls_two_tap:
    $ vn_enter(bg="ls_marigold_stall", pc="defiant", pc_tag="ls_pc", cast=[("ls_marigold", "fond")], cg="ls_tap_sit")
    show cg ls_tap_sit onlayer cgl
    "Marigold's stall is the big one at the end, deep in clean straw. She sits on a hay bale with her knees apart and her apron folded up, and her cock lies along her thigh, thick and heavy, the ridged head catching the light."
    ls_marigold "\"Sit.\""
    ls_you "\"I'll stand, thanks—\""
    "Petal's hand on your shoulder sits you. In the straw, between Marigold's knees. Your face is right there. Petal goes, and the stall gate clicks."
    ls_marigold "\"Petal showed you the jar. Why wait for the mash? Straight from the tap, then.\""
    "She lifts her cock in one big hand. It's longer than your forearm and it's getting harder."
    ls_you "\"No— no way— I'm not—\""
    show cg ls_tap_jaw onlayer cgl
    "Her other hand takes your jaw. Big, warm, gentle, and it doesn't move when you pull. Her thumb presses in at the hinge, and your mouth comes open."
    ls_marigold "\"There. It's for your own good, sweetheart. You're not eating enough.\""
    "She feeds it to you slow. The ridged head fills your mouth and keeps coming, hot and heavy on your tongue, and her hand slides round to cup the back of your head, and holds."
    ls_you "\"Mmf— {i}mmnf{/i}— {i}mmh{/i}—!\""
    ls_marigold "\"Easy. Easy. Give me the honest noise.\""
    "You shove at her thighs. It's like shoving a hay bale. You give her the honest noise, all of it, muffled no after muffled no, drool down your chin, and every no comes out round her cock like a moan."
    "Your own cock's standing straight up between your knees, untouched, leaking on the straw. You hate it. It doesn't care."
    "She doesn't hurry. She rocks. Slow, deep, the ridges dragging over your tongue, and your traitor {i}tongue{/i} goes flat and starts to work."
    ls_marigold "\"There. There it is.\""
    show cg ls_tap_cum onlayer cgl
    "She swells. She holds your head. \"{i}Mmh{/i},\" she says, almost lazy, and floods you." with vnfx("flash")
    "It's {i}so much.{/i} Hot and thick and sweet, rope after rope, and she holds you there till you swallow, and swallow, and it spills out round her cock and runs down your chin."
    ls_you "\"{i}Hhah{/i}— {i}hah{/i}— you— you can't just— that's—\""
    "You lick your lips. You didn't mean to lick your lips. Marigold watches you do it, and her cock twitches against your cheek, and she laughs, low and fond."
    ls_marigold "\"Again.\""
    menu:
        "It isn't a question either."
        "“Again.” She isn't asking":
            jump ls_two_tap_sex
        "She lets go of your jaw":
            $ vn_until(21)
            jump ls_bell

label ls_two_tap_after:
    $ vn_enter(bg="ls_marigold_stall", pc="flushed", pc_tag="ls_pc", cast=[], cg=None)
    show bg ls_marigold_stall onlayer bgl
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    if ls_enc.partner_came:
        "Again. And she gives you again like she gave you the first: slow, heavy, all of it, her big hand holding your head the whole time, till you've swallowed every drop and moaned for the last of it."
    else:
        "She lets you go, eventually, and pats your cheek."
        ls_marigold "\"Save some room.\""
    "You lie in her straw afterwards, coughing, swearing at the rafters, your belly warm and your mouth tingling and your cock still dripping, untouched. She strokes your hair like you're something she owns."
    ls_marigold "\"Bell's at nine. Don't be late, ma'am's little discrepancy.\"\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_2:
    show cg ls_milk_2 onlayer cgl
    "Bench. Bar. Cups. The plug slides in like it lives there."
    vn_sfx "Vrrrm."
    "You don't last any longer this time. Then you're coming, hips jerking on the bench, cock spurting into the tray, and the back line drinks it up, {i}shlp, shlp{/i}, and the tank behind you is brimming." with vnfx("flash")
    ls_hester "\"Tomorrow's mash.\""
    "Tapping the glass. Your mouth waters. Your {i}mouth waters.{/i}"
    ls_you "\"{i}Hhah{/i}— again— it's going again—\""
    "Up front, the cups pull and pull at your tender pink nipples. They're so sensitive tonight every tug goes straight to your cock. But the saucer's dry."
    show ls_marigold fond at vn_cast_slot
    ls_marigold "\"Still nothing up front, ma'am's little discrepancy? Never mind. Back end's working for both of you.\""
    "At the rail again, arms folded on it, chin on her arms. Watching. Her cock's lifting her apron."
    ls_you "\"{i}Nnh{/i}— don't— don't {i}watch{/i}—\""
    ls_marigold "\"I'll watch.\""
    "Comfortable, and she does, all the way through your next one. Hester sighs, the way you'd sigh at a tractor that won't start. She takes your card down and writes.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    hide ls_marigold
    jump ls_night

## ---- day 3: claimed (Livestock Day Three, Three Bell, Three Stall, Claimed After, Three Milking). MANDATORY. --

label ls_day_3:
    $ ls_body(2)
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_3")
    show cg ls_wake_3 onlayer cgl
    "You wake up with your hands on your chest. You don't remember putting them there."
    "{color=#ff5fb8}Your nipples are {i}puffy.{/i} Swollen up soft and pink, sitting on two little swells that weren't there yesterday. You squeeze. They give.{/color}"
    ls_you "\"{i}Nnnh{/i}— oh— oh fuck—\""
    "{color=#ff5fb8}Your waist dips in where it didn't before. Your hips have gone soft and round under your palms. Your lips are fat and so sensitive that licking them makes you whimper out loud.{/color}"
    "{color=#ff5fb8}Your hair's down past your ears. You push it back and your fingers catch on something hard on your head. Two of them. Two hard little nubs, one each side, under the hair.{/color}"
    ls_you "\"Hay does that.\""
    ls_buttercup "\"Does it, sugar.\""
    "Over the partition, chewing. At the trough you lap your mash and think about Marigold's cock the whole time."
    show ls_buttercup soft at vn_cast_slot
    "Buttercup reaches over and parts your hair with two fingers, and finds the nubs, and coos."
    ls_buttercup "\"Ohhh, look at you. Horns coming. They're sensitive at first. Mine were. Don't let the twins grab them.\""
    ls_you "\"Why would the twins grab th—\""
    "She just smiles and goes back to her mash."
    hide ls_buttercup
    hide cg onlayer cgl
    call ls_chore
    jump ls_three_bell

label ls_three_bell:
    $ vn_enter(bg="ls_stall", pc="defiant", pc_tag="ls_pc", cast=[("ls_hester", "flat")], cg="ls_bell_collar")
    show cg ls_bell_collar onlayer cgl
    "Hester's waiting at your stall gate with something in her hand. A leather collar with a brass bell on it."
    ls_you "\"Don't— I don't want that—\""
    "She buckles it round your neck anyway, the way you'd buckle a halter on something that kicks."
    vn_sfx "Tink."
    "Every time you breathe. {i}Tink, tink.{/i}"
    $ ls.belled = True
    $ ls_advance(3)
    "Then she takes the card down, crosses out your name, and writes in capitals. {color=#ffd700}CHERRY.{/color}"
    show screen ls_card
    ls_hester "\"Name corrected.\""
    ls_you "\"That's not my— my name is {i}[ls_pc_name]{/i}—\""
    ls_hester "\"It's on the card.\""
    vn_sfx "Click."
    hide screen ls_card
    hide ls_hester
    show ls_marigold fond at vn_cast_slot
    ls_marigold "\"Cherry. Come on, then, Cherry.\""
    "That's not Hester. That's Marigold, leaning on the end of the stall, enormous, apron off, her tits bare and leaking and her cock already half up and swinging."
    ls_you "\"No.\""
    "She hooks one finger through the ring of your bell, and walks. You go with it or you go on your face. You go with it, swearing, the bell tinking every step, the whole line watching you towed past their stalls.\n{size=-5}{color=#ff8fa3}▸ Towed by the bell{/color}{/size}"
    hide ls_marigold
    jump ls_three_stall

label ls_three_stall:
    $ vn_enter(bg="ls_marigold_stall", pc="defiant", pc_tag="ls_pc", cast=[], cg="ls_stall_down")
    show cg ls_stall_down onlayer cgl
    "Her stall. Deep straw. The smell of her, clover and heat."
    ls_marigold "\"Knees and elbows. In the straw.\""
    ls_cherry "\"No— I'm not— {i}hey{/i}—!\""
    "One big hand between your shoulder blades, and you're down. Knees. Elbows. Your face in the hay and your ass up. Your bell tinks against the straw."
    "She kneels behind you. She's so {i}big.{/i} Her thighs bracket yours and pin them. Her cock lies along the crack of your ass, hot and heavy, and it goes right up your back."
    ls_cherry "\"Ma'am— ma'am, {i}don't{/i}— please— I'm not a—\""
    ls_marigold "\"Easy.\""
    "A big hand spreads on the small of your back and holds you flat. Oil, warm. Her thumb circles your hole, slow, and slips in, and the no comes out of you as a moan, straight into the straw."
    ls_marigold "\"There's the honest noise.\""
    "The ridged head of her cock presses where her thumb was. And pushes. You clench. It doesn't matter. Your hole opens round it, slick and greedy, the traitor."
    ls_cherry "\"{i}Ohhhh{/i}— no— {i}NO{/i}— take it out—!\""
    menu:
        "She doesn't."
        "Struggle":
            $ ls.fight = "struggle"
        "Swear":
            $ ls.fight = "swear"
        "Grit your teeth":
            $ ls.fight = "grit"
    jump ls_three_claimed

label ls_claimed_after:
    $ vn_enter(bg="ls_marigold_stall", pc="broken", pc_tag="ls_pc", cast=[], cg="ls_claimed_after")
    show cg ls_claimed_after onlayer cgl
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    if ls_enc.partner_came:
        "She finishes buried to the root, groaning low in your ear, and you feel every hot heavy pulse of it fill you up."
    else:
        "She stays buried in you, both of you shaking, her chest heaving on your back."
    "You're screaming. You've been screaming the whole time. Your face is in the straw and your cock is drooling a long clear string onto the hay under you, untouched, twitching, and you can't stop clenching on her."
    "She doesn't pull out."
    ls_marigold "\"Again.\""
    ls_cherry "\"No— ma'am— {i}ma'am{/i}— not again— {i}ahh{/i}— {i}ahhh{/i}—!\""
    vn_sfx "Pap. Pap. Pap."
    "Slow. Huge. All the way in, all the way out, the ridged head catching on your rim every time, and every stroke drags across that spot until your eyes roll back and the no falls out of your mouth and doesn't come back."
    ls_cherry "\"Don't— don't stop— {i}why{/i} am I— don't {i}stop{/i}— ma'am— {i}please{/i}—!\"" with vnfx("shake")
    "You come with nobody touching your cock. It just spills, in pulses, while she fucks you through it, and she groans and grinds in deep and floods you again." with vnfx("flash")
    ls_marigold "\"Mine. Cherry.\""
    "Patting your ass."
    ls_cherry "\"...Not. Not yours.\""
    "You pant it into the hay. Your hole's still twitching. It knows the shape of her now, and it's already sulking that she's gone.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_3:
    show cg ls_milk_3 onlayer cgl
    "You're still loose from her. The plug goes in with a wet {i}shlk{/i} and you whimper at the bar."
    "The cups latch onto your puffy nipples, and suck. They're so {i}full{/i} feeling. Hot. Tight. Like something behind them wants out. The cups pull, and pull, and pull—"
    show cg ls_first_drops onlayer cgl
    vn_sfx "Plip."
    "A drop. White. On the saucer."
    vn_sfx "Plip."
    "Another. You stare at it. Your whole chest is throbbing. The plug pulses on your spot and you're coming into the tray again, but you can't stop looking at the saucer." with vnfx("flash")
    ls_cherry "\"...The mash didn't do {i}that{/i}.\""
    "Hester bends down and looks at the saucer for a long moment. Then she writes something."
    "Behind you the back tank's full. In front of you there are white drops on a saucer, and they're the only thing you can see.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 4: the fence rail (Livestock Day Four, Four Rail, Four Rail After, Four Milking) -----------------

label ls_day_4:
    $ ls.fit = "nude"
    $ vn_enter(bg="ls_long_barn", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_montage_4")
    show cg ls_montage_4 onlayer cgl
    "{color=#b7b7b7}Days of the same: trough, chores, nine o'clock. Trough, chores, nine o'clock. The summer goes gold at the edges.{/color}"
    ## the counter keeps the montage's weeks (2026-11-12: the day has to agree with the story)
    $ vn_pass(21 * 1440)
    $ ls_body(3)
    show bg ls_stall onlayer bgl
    show cg ls_wake_4 onlayer cgl
    "And one morning you sit up and something {i}bounces.{/i}"
    "{color=#ff5fb8}Tits. Small ones. Real ones. Two soft round handfuls, and when you grab them they {i}squish{/i}, and your nipples poke out between your fingers, puffy and dark and wet at the tips.{/color}"
    ls_cherry "\"{i}Ahh{/i}— oh— they're— oh my god they're {i}tits{/i}—\""
    "You squeeze. Milk beads out."
    ls_cherry "\"{i}Nnnhh{/i}—!\""
    "{color=#ff5fb8}You twist round. Your ass has gone round and high and soft, two plump cheeks that fill your hands. Your thighs press together when you stand, smooth all the way up.{/color}"
    "You say \"what\" and your voice comes out light. Lighter. Your face in the trough water is finer, softer at the jaw, and your hair's grown down to meet it, brushing your cheeks."
    "{color=#ff5fb8}And your cock. Smaller. Definitely smaller, sitting tiny and pink between your smooth thighs, and it's {i}hard{/i}, and you can't stop squeezing your tits.{/color}"
    "Your ass still clenches every time you think of Marigold. Your mouth too. Both of them hungry, both of them good at it now."
    "And both of them so {i}sensitive.{/i} You suck a smear of mash off your finger and your knees go."
    ls_cherry "\"{i}Mmmmnh{/i}—!\""
    "You sit down on the straw and squeak, because your ass felt {i}that{/i} too."
    show ls_buttercup grin at vn_cast_slot
    ls_buttercup "\"Well {i}hello.{/i}\""
    "Over the partition, staring frankly at your chest."
    ls_cherry "\"Don't look at them!\""
    ls_buttercup "\"Sugar, they're tits. On a dairy line. Everybody's going to look at them.\""
    show cg ls_peach onlayer cgl
    "She reaches over and gives one a friendly squeeze, like testing a peach. Milk beads out."
    ls_buttercup "\"Oh, that's {i}lovely.{/i} Hester'll be pleased.\""
    ls_cherry "\"{i}Mmh{/i}—\""
    "Your knees go. Your cock throbs, small and stiff and useless against the straw."
    hide ls_buttercup
    hide cg onlayer cgl
    call ls_chore
    jump ls_four_rail

label ls_four_rail:
    $ ls_advance(4)
    $ vn_enter(bg="ls_yard", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_rail_grab")
    show cg ls_rail_grab onlayer cgl
    "You're carrying a pail of mash along the yard fence, tits bouncing, when two sets of arms grab you from behind."
    ls_billy "\"Got her!\""
    ls_bart "\"{i}We{/i} got her!\""
    "The Haskett twins. Billy and Bart, the yard hands. Same curly horns, same short tails, same gap-toothed grin. You still can't tell which is which."
    show cg ls_rail_over onlayer cgl
    "They haul you up and over the top rail, belly down on wood rubbed glassy smooth by years of bellies, ass up, the pail rolling away in the mud."
    ls_cherry "\"Hey— {i}hey!{/i} Put me {i}down{/i}— get your hands off—!\""
    "You kick. One of them catches your ankle, cheerful as anything, and tucks it under his arm. The other one's got both your wrists on the far side of the rail."
    ls_billy "\"Look at {i}that.{/i}\""
    vn_sfx "Smack."
    "He smacks your ass. It jiggles. They both whoop."
    ls_bart "\"She's coming on lovely!\""
    ls_billy "\"Me first, I grabbed her!\""
    ls_bart "\"You grabbed her {i}arm!{/i}\""
    ls_cherry "\"I'll tell Hester— I'll tell {i}Hester{/i}—!\""
    "\"Hester's up the top field!\" they chorus, delighted."
    "Overalls drop. Something hot and hard slaps on your ass cheek. Your hole twitches. It {i}twitches{/i}, the traitor, like nobody told it what you just said."
    menu:
        "\"Barn-broke, this one'll be.\""
        "Struggle":
            $ ls.fight = "struggle"
        "Swear":
            $ ls.fight = "swear"
        "Grit your teeth":
            $ ls.fight = "grit"
    jump ls_four_rail_sex

label ls_four_rail_after:
    $ vn_enter(bg="ls_yard", pc="flushed", pc_tag="ls_pc", cast=[], cg="ls_rail_swap")
    show cg ls_rail_swap onlayer cgl
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    ls_billy "\"Swap! Swap swap swap!\""
    "One pulls out of your ass with a wet pop and comes round the front, and the other one goes round the back, and they're laughing the whole time like it's a three-legged race."
    ls_cherry "\"No— not my {i}mouth{/i}— don't you— {i}mmf{/i}—!\""
    "Cock in your mouth. Cock in your ass. Both at once. The rail creaks."
    vn_sfx "Squeak, squeak, squeak."
    ls_bart "\"Barn-broke, this one!\""
    ls_billy "\"Told you she'd take to it!\""
    ls_cherry "\"{i}Mmf{/i}— I'm {i}not{/i}— {i}mmnf{/i}—!\""
    "You're stuffed at both ends and your tiny cock is rubbing on the wood and leaking all over it and your new tits are squashed on the rail and squirting, and you're still trying to say no round him, and the twin behind you hits {i}that{/i} spot, and something comes up out of your chest instead—"
    show cg ls_rail_moo onlayer cgl
    ls_cherry "\"{i}Mmmmmmooooooo{/i}—!\"" with vnfx("shake")
    "Long and low and loud. A real one. Your first real one, forced out of you round a goat-man's cock."
    "Both twins freeze."
    ls_bart "\"...Did she just—\""
    ls_billy "\"She {i}mooed!{/i}\""
    "And they go at you twice as hard, cackling, and the moos keep coming, one every thrust, and the no's stop coming at all."
    ls_cherry "\"{i}Mmmoo{/i}— {i}mmmmoooo{/i}—!\""
    "You're pushing back on the one behind. You're sucking the one in front. You can't stop either."
    show cg ls_rail_cum onlayer cgl
    "They both go off at once, one down your throat and one deep in your ass, and you come on the fence rail with a mouthful of goat-man and your eyes rolled back, mooing." with vnfx("flash")
    "They pull out together. It spills out of your mouth down your chin, and out of your ass down your thighs."
    show cg ls_rail_hester onlayer cgl
    show ls_hester flat at vn_cast_slot
    ls_hester "\"{b}GENTLEMEN.{/b}\""
    "Hester. Behind the tool shed. Clipboard. The twins vault the fence and vanish into the long grass, overalls round their knees."
    ls_hester "\"Gutter duty! All week!\""
    "Calling after them. She looks at you, draped over the rail, dripping at both ends, mooing faintly. She writes something."
    ls_hester "\"Fence isn't for that.\""
    hide ls_hester
    "And goes.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_4:
    show cg ls_milk_4 onlayer cgl
    "The cups go on your new tits and suck, and it's not drops tonight."
    vn_sfx "Pssh. Pssh."
    "It {i}sprays.{/i} Two thin white jets into the line, and your whole body jerks on the bench." with vnfx("shake")
    ls_cherry "\"{i}Mmmmmooooooo{/i}—!\""
    "It comes out of you before you can think. A full one, at the frame, with the whole line listening. Buttercup moos back from the next bench. Then the one past her. Then the whole barn, rolling down the line like thunder."
    "The plug pulses. You come into the tray, but less. Thinner. The back tank's only half up tonight."
    show cg ls_saucer_over onlayer cgl
    "The saucer fills. It fills, and it runs over the rim, and white drips off the edge onto the straw."
    show ls_marigold pleased at vn_cast_slot
    ls_marigold "\"{i}There{/i} she goes.\""
    show cg ls_marigold_lick onlayer cgl
    "From the rail, low and pleased. She reaches through and runs one finger round the saucer's wet rim, and puts it in her mouth, and holds your eyes while she sucks it clean."
    "You come again. Just from that. Your tiny cock twitches and dribbles in the tray, and your tits squirt in the cups, both ends at once." with vnfx("flash")
    hide ls_marigold
    "Hester looks at it for a long moment. Then she goes and gets a teacup, and sets it on the shelf, ready."
    "{i}Responsive,{/i} she writes.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 5: letdown, then the cage (Livestock Day Five, Five Bench, Five Bench After, Five Cage, Five Milking) --

label ls_day_5:
    $ ls_body(4)
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_5")
    show cg ls_wake_5 onlayer cgl
    "Something flicks by your head and you swat at it."
    "{color=#ff5fb8}It's your {i}ear.{/i} Soft. Long. Floppy. Smooth and pink inside, flicking every time you hear the barn creak. Cow ears, one each side, where your ears used to be.{/color}"
    "{color=#ff5fb8}You grab your chest to steady yourself and your hands are {i}full.{/i} Perky, round, bouncing. A C cup at least, sitting high and proud with the nipples pointing up, wet already.{/color}"
    ls_cherry "\"{i}Haah{/i}— oh, they're so— {i}mmh{/i}— so {i}heavy{/i}—\""
    "{color=#ff5fb8}Your hips have gone wide. Your waist's tucked in. You run your palms down and they curve in and then right back out, and you moan, and the moan comes out a girl's moan, high and breathy.{/color}"
    "In the trough water: your hair's down to your chin, brown, and white right at the roots, like frost."
    "Your hole clenches thinking of the rail, and a squeaky little \"{i}nnh{/i}—!\" jumps out of you. Your mouth waters thinking of the rail. You're getting very good at both ends."
    show cg ls_ears_scratch onlayer cgl
    show ls_petal grin at vn_cast_slot
    "Petal sees the ears and squeals. Buttercup reaches over the partition and scratches behind one, and your knees give out."
    hide ls_petal
    hide cg onlayer cgl
    call ls_chore
    jump ls_five_bench

label ls_five_bench:
    $ ls_advance(5)
    $ vn_enter(bg="ls_dairy_bench", pc="defiant", pc_tag="ls_pc", cast=[("ls_marigold", "fond")], cg="ls_bench_wait")
    show cg ls_bench_wait onlayer cgl
    "The dairy bench. Padded, wide, with steamed glass panels either side. Marigold's sitting on it, waiting for you. She pats her thigh."
    ls_marigold "\"Not the machine today. Mouth first. Machine's for after.\""
    ls_cherry "\"No. Not— I'm not lying on—\""
    show cg ls_bench_lap onlayer cgl
    "She reaches out, takes you by the bell, and lays you back across her lap like a sack of feed. One big arm goes across your hips. The other hand gathers both your wrists over your head and pins them to the bench."
    "Your tits sit up, full and tight, the nipples dark and dripping. She looks at them for a long, hungry moment."
    ls_cherry "\"Ma'am— let go— {i}ma'am{/i}—\""
    ls_marigold "\"Marigold. From today.\""
    ls_cherry "\"I don't {i}care{/i} what you're called, get your mouth— don't— {i}don't{/i}—\""
    "She bends her big head, horns and all, and her lips close over your nipple."
    menu:
        "\"Hush. Stock doesn't vote.\""
        "Struggle":
            $ ls.fight = "struggle"
        "Swear":
            $ ls.fight = "swear"
        "Grit your teeth":
            $ ls.fight = "grit"
    jump ls_five_bench_sex

label ls_five_bench_after:
    $ vn_enter(bg="ls_dairy_bench", pc="flushed", pc_tag="ls_pc", cast=[], cg="ls_letdown")
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    "She keeps sucking. Broad tongue, slow pulls, patient as weather, your wrists still pinned in her fist, and your chest is so full it's going to {i}burst{/i}—"
    ls_cherry "\"No— no, {i}stop{/i}— something's— Marigold, {i}stop{/i}, something's coming—\""
    show cg ls_letdown onlayer cgl
    "And it lets down." with vnfx("flash")
    "All at once. A hot rush through both tits, and milk {i}pours{/i}, a real rope of it, straight into her mouth, and the other nipple sprays all over her cheek."
    ls_cherry "\"{i}NO{/i}— no no no— {i}ahhhhh{/i}— Marigold— {i}Marigold{/i}— it's coming— it's {i}coming{/i}—!\"" with vnfx("shake")
    "And so are you. Hands-free, back arched across her lap, yelling no at the rafters with every pull, milk pouring, cock twitching, coming harder than you've ever come in your life."
    show cg ls_bench_drink onlayer cgl
    "She swallows. And swallows. She groans round your nipple and her hips start rocking, and her cock's grinding hot and slick up your belly, and she switches tits and drinks from the other one and grinds faster—"
    ls_cherry "\"Don't— {i}don't{/i}— oh god don't stop— {i}mmmoooo{/i}—!\""
    ls_marigold "\"Good girl. {i}Good{/i} girl.\""
    show cg ls_bench_paint onlayer cgl
    "And she cums all up your stomach, hot and thick, in long lazy spurts that pool in your belly button." with vnfx("flash")
    "She lets your wrists go. You lie there leaking from both nipples, panting, painted. Your hands drift to your tits on their own and squeeze, and milk runs over your fingers, and you know exactly how to do it now. Thumb, fingers, roll. You didn't tell your hands to. They do it anyway."
    ls_marigold "\"There. Now the machine'll have something to do.\""
    "And she licks her lips.\n{size=-5}{color=#ff8fa3}▸ After lunch{/color}{/size}"
    jump ls_five_cage

label ls_five_cage:
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[("ls_hester", "flat")], cg="ls_cage_show")
    show cg ls_cage_show onlayer cgl
    $ vn_until(13)
    "Hester finds you after lunch. She holds up a little steel cage. Plain. Flat. Tiny."
    ls_hester "\"Front's not producing. Nothing wasted. Doesn't pay to dilute the effort when there's only one front line moving.\""
    ls_cherry "\"Oh, no. No, you are {i}not{/i} putting that on—\""
    show cg ls_cage_click onlayer cgl
    "She hooks a boot behind your knee, sits you down in the straw, and kneels and fits it over your little cock while you're still swearing. Cold. Snug."
    vn_sfx "Click."
    $ ls.caged = True
    "The lock. You look down. Your cock's a little steel nub between your thighs. It throbs against the bars, trying to get hard, and can't."
    ls_cherry "\"Take it {i}off{/i}— take it— oh, that's— {i}nnh{/i}—\""
    "It's throbbing. It's leaking through the bars. It's doing absolutely nothing useful."
    ls_hester "\"Bell's at nine.\""
    hide ls_hester
    "Pocketing the key.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_5:
    show cg ls_milk_5 onlayer cgl
    "The cups go on. They suck. And it {i}comes.{/i}"
    vn_sfx "Pssh, pssh, pssh."
    "Hot and steady, both tits, streaming down the line. The teacup fills before you've finished your first moo. Hester takes it away and puts down a milk glass."
    ls_cherry "\"{i}Mmmmoooo{/i}— ohh— {i}mmmmoooooo{/i}—\""
    "The plug pulses in your ass. Your caged cock twitches and drips one sad little dribble onto the pad. That's all. That's all it does now."
    show cg ls_glass_full onlayer cgl
    "The glass fills. To the top. Right to the top, white and frothy, and you're moaning and shaking on the bench and the cups are still pulling."
    show ls_hester smile at vn_cast_slot
    "Hester looks at the glass. And she smiles. A real one. Just for a second."
    "She takes your card down and writes. {i}Front: non-producing, caged. Milking as female.{/i} Then she turns to Petal, who's mopping up spills down the line."
    ls_hester "\"Petal. Her mash goes on the dairy line from tomorrow.\""
    "She jerks her chin at you."
    ls_hester "\"She's moving.\""
    hide ls_hester
    "{i}She.{/i}"
    show ls_petal grin at vn_cast_slot
    ls_petal "\"Welcome to the line, Cherry.\""
    "Grinning at you over the mop."
    hide ls_petal
    show cg ls_glass_toast onlayer cgl
    "Marigold leans over the rail and lifts the full glass to the lamp, white and frothy, like a toast. She drinks half of it. Not a drop of hers has ever touched your tongue, and here she is, drinking yours."
    ls_marigold "\"Good girl.\""
    "Milk on her lip. You moo so hard the cups slip.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 6: the stud's privilege (Livestock Day Six, Six Pen, Six Pen After, Six Milking) --------------------

label ls_day_6:
    $ vn_enter(bg="ls_yard", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_montage_6")
    show cg ls_montage_6 onlayer cgl
    "{color=#b7b7b7}Days of the same: trough, chores, nine o'clock. The cold snap comes in overnight and the yard goes white.{/color}"
    ## summer to the first snow: the montage's months on the counter too
    $ vn_pass(84 * 1440)
    $ ls_body(5)
    show bg ls_stall onlayer bgl
    show cg ls_wake_6 onlayer cgl
    "You wake up warm anyway. And {i}wet.{/i}"
    "{color=#ff5fb8}Your tits have leaked all over the straw. They're {i}huge.{/i} Full and heavy, a DD and dripping, sitting on your chest like two warm loaves, and when you sit up they {i}sway.{/i}{/color}"
    ls_cherry "\"Oh— {i}oh{/i}— they're— {i}mmmh{/i}—\""
    "You grab them and squeeze and milk squirts across the stall."
    ls_cherry "\"{i}Haaah{/i}—!\""
    "{color=#ff5fb8}Your ass is plump and heavy when you kneel. It spreads on your heels. Your face in the trough water is soft and round-cheeked and pretty, framed in hair to your shoulders. And when you moan, the voice that comes out is a woman's. Almost. Nearly all of it.{/color}"
    "Between your legs, the cage. Your cock's just a nub in it now. A useless little nub that drips when you squeeze your tits."
    show cg ls_self_milk onlayer cgl
    "You milk yourself into the trough before breakfast without even thinking about it. Two hands, one each side, roll and pull. Your hands are good at it. Your hands are {i}really{/i} good at it."
    show ls_buttercup soft at vn_cast_slot
    ls_buttercup "\"Look at you. Self-sufficient.\""
    "Proud. She leans over to kiss your cheek good morning, catches the corner of your mouth, and you moan into it so loud and so long that she laughs against your lips."
    ls_buttercup "\"Sensitive mouth. That's the good stuff coming in.\""
    hide ls_buttercup
    hide cg onlayer cgl
    call ls_chore
    jump ls_six_pen

label ls_six_pen:
    $ ls_advance(6)
    $ vn_enter(bg="ls_yard", pc="shocked", pc_tag="ls_pc", cast=[("ls_hester", "flat")], cg="ls_pen_walk")
    show cg ls_pen_walk onlayer cgl
    $ vn_until(17)
    "Hester walks you to the bull pen at dusk with a hand on your bell. Snow in the yard, squeaking under your bare feet. Your tits bounce and steam in the cold, nipples hard as nails, leaking white trails that freeze on your belly."
    ls_cherry "\"Where are we— Hester, where are we {i}going{/i}—\""
    "The whole line watches you go. Buttercup waves. Petal makes a crude gesture with a fist and a finger and cackles."
    ls_hester "\"Custom. New dairy stock gets the stud's privilege. Every season.\""
    hide ls_hester
    show bg ls_bull_pen onlayer bgl
    show cg ls_pen_angus onlayer cgl
    "She opens the gate, puts you through it, and latches it behind you."
    show ls_angus still at vn_cast_slot
    "Angus is sitting on a bale. He's a {i}slab.{/i} Shoulders like a barn door, heavy horns curving out wide, a jaw like a gatepost. Forty-odd and quiet as a hill."
    "He looks at you. Your tits, leaking. Your hips. Your little steel cage. He stands up, and his cock comes up with him, and it's—"
    ls_cherry "\"...Oh. Oh, {i}no{/i}, that won't— no. No. Absolutely not.\""
    "You back into the gate. It's latched."
    ls_angus "\"It will.\""
    hide ls_angus
    show cg ls_pen_down onlayer cgl
    "Calm as weather. He crosses the straw in two steps, takes your horns, one in each fist, and steers you down. Not hard. Just all the way. Knees in the straw, elbows in the straw, your face in the straw, your ass up."
    ls_angus "\"Still.\""
    menu:
        "He says it like a fact."
        "Struggle":
            $ ls.fight = "struggle"
        "Swear":
            $ ls.fight = "swear"
        "Grit your teeth":
            $ ls.fight = "grit"
    jump ls_six_pen_sex

label ls_six_pen_after:
    $ vn_enter(bg="ls_bull_pen", pc="flushed", pc_tag="ls_pc", cast=[], cg="ls_pen_again")
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    if ls_enc.partner_came:
        "He comes like the rest of him moves: slow, heavy, enormous, a long deep throb you feel all the way up in your belly."
    else:
        "He holds still in you, deep, while you shake."
    show cg ls_pen_again onlayer cgl
    "And he doesn't stop. He takes your horns, one in each fist, and steers you back onto him."
    ls_cherry "\"Sir— {i}sir{/i}— no more— it's so {i}big{/i}— I'm so {i}full{/i}— I can't—\""
    ls_angus "\"Still.\""
    vn_sfx "Splt. Splt."
    "He stretches you wide and keeps you there. It's so big it's stupid. It's so big you can feel it in your {i}throat{/i}, and every slow stroke pushes the milk out of your tits onto the straw, and your caged nub leaks a steady drip through the bars the whole time, useless, forgotten."
    ls_cherry "\"Sir— {i}ahh{/i}— sir— don't— don't {i}stop{/i}— why did I— don't {i}stop{/i}—!\"" with vnfx("shake")
    ls_angus "\"Good. Leaking through the cage. Good stock.\""
    ls_cherry "\"{i}Mmmmmmooooooo{/i}—!\""
    show cg ls_pen_flood onlayer cgl
    "He pulls you back by the horns until you're flush on his hips and holds you there and floods you again. You feel it go in. You feel it fill you. When he finally pulls out, it gushes out of you and runs down your thighs in thick hot streams." with vnfx("flash")
    "You can't feel your knees. You can feel {i}everything{/i} else. Your ass gapes and clenches on nothing, and you swear at it, and it clenches again."
    ls_angus "\"Mm.\""
    "He pats your head, and sits back down on his bale.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_6:
    show cg ls_milk_6 onlayer cgl
    "You walk to the frame bow-legged and the whole line grins at you."
    "The plug barely has to work. You're still so loose from Angus that it slides in and sits there humming, and your caged nub gives one bead. One. Onto the pad. The back tank doesn't even move."
    "The front does."
    show cg ls_jug onlayer cgl
    vn_sfx "Pssh-pssh-pssh."
    "Hester sets a jug under the line and your tits fill it, a steady white stream, and you moo the whole time, long and low, your forehead on the bar."
    show ls_marigold fond at vn_cast_slot
    "Marigold leans on the rail and watches the jug fill, and her cock lifts her apron."
    ls_marigold "\"Gossip says it was textbook. Stud's seal shows on the yield.\""
    hide ls_marigold
    "Hester writes. {i}Stud-privileged.{/i}\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 7: the county fair (Livestock Day Seven, Seven Polish (+ After), Seven Dress, Seven Fair, Seven Ring,
## Seven Trailer, Seven Buttercup, Seven Milking) -----------------------------------------------------------------

label ls_day_7:
    $ ls_body(6)
    $ ls.fit = "nude"
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_7")
    show cg ls_wake_7 onlayer cgl
    "Your lower back's tingling when you wake up. Then something swishes against your ankle."
    "{color=#ff5fb8}A tail. {i}Your{/i} tail. Long and smooth with a soft tuft at the end, swishing on its own whenever something feels good, and something feels {i}very{/i} good, because—{/color}"
    "{color=#ff5fb8}Your tits. You fold your arms under them and they {i}rest{/i} on your forearm, heavy and huge, an F and leaking twice as much as yesterday, two white trickles down your belly.{/color}"
    ls_cherry "\"No— {i}no{/i}— {i}ohhh{/i}— {i}mmmh{/i}— look at them— {i}look{/i} at them—\""
    "{color=#ff5fb8}Your thighs are thick. Soft and thick and pressed together all the way up. You squeeze them together and moan.{/color}"
    show cg ls_braid onlayer cgl
    show ls_buttercup soft at vn_cast_slot
    "{color=#ff5fb8}And your hair. Long, down your back, and it's gone {i}white.{/i} Snow white on one side, jet black on the other, a Holstein split.{/color} Buttercup's already behind you, plaiting it into one fat show braid."
    ls_buttercup "\"Fair's today. Marigold wants you on the bench first.\""
    "She ties it off with a blue ribbon."
    ls_cherry "\"I'm not going to any fair. I'm not going on any {i}bench.{/i}\""
    hide ls_buttercup
    "When you stand up your ass shifts heavy and your hole tightens, remembering Angus, and the thought comes before you can stop it: {i}it'd take that again.{/i} It would. Easily. You hate that it would."
    "Your new tail swishes across your ass cheeks."
    ls_cherry "\"{i}Ohhh{/i}—!\""
    "Just that. Just the tuft brushing your ass, and you're up on your toes, moaning. Petal's at the gate with her hand out for your wrist.\n{size=-5}{color=#ff8fa3}▸ Walked to the bench{/color}{/size}"
    jump ls_seven_polish

label ls_seven_polish:
    $ ls_advance(7)
    $ vn_enter(bg="ls_dairy_bench", pc="defiant", pc_tag="ls_pc", cast=[("ls_marigold", "fond")], cg="ls_polish_kneel")
    show cg ls_polish_kneel onlayer cgl
    "The dairy bench. Marigold kneels in front of it with her cock in her fist, oiled and gleaming."
    ls_marigold "\"Show polish. Ribbons get earned right here. Knees together. Tail up.\""
    ls_cherry "\"I'm not polishing anything—\""
    "Petal sits you on the bench and leaves. Marigold takes your hands, both of them, and puts them on your own tits, and closes her big hands over them, and pushes. There's a deep soft valley between them now."
    show cg ls_polish onlayer cgl
    "She slides her cock into it."
    ls_cherry "\"No— get it out of my— {i}mmh{/i}—\""
    vn_sfx "Shlk. Shlk."
    "Hot. Heavy. The ridges drag up your breastbone and the head pops out the top, right under your chin. She rocks. Your nipples rub her thighs and squirt."
    ls_marigold "\"Shoulders back. Let them see.\""
    "You don't. Her thumb presses between your shoulder blades and they go back anyway. Your tits push out round her cock. She groans."
    ls_marigold "\"Good girl. Chin up. Give me a pretty noise.\""
    ls_cherry "\"Fuck {i}off{/i}— {i}mmmmooo{/i}—\""
    "She fucks your tits faster. Your milk slicks everything. The head of her cock bumps your chin every stroke and your tongue comes out and licks it before you can stop it, and she growls, and squeezes your tits over your hands, and—"
    show cg ls_polish_cum onlayer cgl
    "She cums all over you. Ropes of it, up your chest, across your throat, a hot splash on your chin and your cheek, pooling white in your cleavage with your own milk." with vnfx("flash")
    ls_marigold "\"That's show polish. Every morning till they hang a ribbon on you.\""
    ls_cherry "\"{i}Hah{/i}— {i}hah{/i}— never— never again—\""
    "Your tits know how to hold a cock now. How to squeeze, how to roll, how to milk it. Nobody asked them. Marigold's still holding your hands on them."
    ls_marigold "\"Again.\""
    menu:
        "Her hands don't move."
        "“Again.” She doesn't let go":
            jump ls_seven_polish_sex
        "She lets go: wipe off and get ready":
            jump ls_seven_dress

label ls_seven_polish_after:
    $ vn_enter(bg="ls_dairy_bench", pc="flushed", pc_tag="ls_pc", cast=[("ls_marigold", "pleased")], cg=None)
    show bg ls_dairy_bench onlayer bgl
    if ls_enc.partner_came:
        "Practice makes perfect. She finishes in your cleavage again, groaning, and rubs it in like lotion while you swear at her."
    else:
        "She rests her cock between your tits, throbbing, and laughs."
        ls_marigold "\"Save some for the trailer.\""
    ls_marigold "\"{i}Now{/i} you're polished.\"\n{size=-5}{color=#ff8fa3}▸ Get ready{/color}{/size}"
    jump ls_seven_dress

label ls_seven_dress:
    $ ls.fit = "show"
    $ vn_enter(bg="ls_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_dress")
    show cg ls_dress onlayer cgl
    "Buttercup and Petal get you ready. A cow-print bra that your tits spill out of. Cow-print panties, tiny, your cage a little steel bump in the front. Cow-print socks up to your thick thighs."
    show ls_petal grin at vn_cast_slot
    "Petal does your face. Pink lips, blue lids, rosy cheeks, black lashes."
    ls_petal "\"For the judges.\""
    "And she kisses your nose."
    hide ls_petal
    "Buttercup polishes your bell till it shines."
    show cg ls_mirror_cow onlayer cgl
    "In the cracked mirror by the gate there's a cow-girl. Holstein braid. Horns. Ears. Tail. Huge leaking tits in a cow-print bra. Pink pouty lips. She looks at you, and her mouth falls open."
    "It's you.\n{size=-5}{color=#ff8fa3}▸ Into the trailer{/color}{/size}"
    $ vn_until(13)
    jump ls_seven_fair

label ls_seven_fair:
    $ vn_enter(bg="ls_fair_ring", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_fair")
    show cg ls_fair onlayer cgl
    "The county fair. Bunting, diesel, popcorn, a crowd three deep at the show ring fence. Farms from all over: the Saltspring trailer, the Bellweather float, and more down the row."
    "\"Marsh Farm, dairy heifer division!\""
    show cg ls_ring_walk onlayer cgl
    "The ring master waves his crook and Buttercup leads the Marsh line in, then you, Marigold's hand on your bell, then Marigold behind like a wall. Sawdust under your bare feet. Half the county looking at your tits."
    ls_cherry "\"Help— I'm not— I signed a {i}form{/i}—\""
    "At the fence. The front row cheers. They think it's part of the act."
    "Your tail swishes. Your nipples go hard. You start to leak, right there, two white lines down your cow-print bra. The crowd {i}loves{/i} it."
    menu:
        "In the ring."
        "Your hips swing the way Buttercup drilled them":
            $ ls.ring = "hips"
        "Your chest pushes out on its own":
            $ ls.ring = "chest"
        "A moo gets out of you":
            $ ls.ring = "moo"
    jump ls_seven_ring

label ls_seven_ring:
    if ls.ring == "hips":
        show cg ls_ring_hips onlayer cgl
        "You try to walk it stiff. You can't. Heel to toe, hips rolling, tail swaying, ass bouncing in the tiny panties, every step Buttercup drilled into you. Somebody at the fence wolf-whistles and you go red to the ears, and your hips swing harder."
    elif ls.ring == "chest":
        show cg ls_ring_chest onlayer cgl
        "You try to hunch. Your shoulders go back on their own. Chin up. Tits out. They bounce with every step and leak with every bounce, and the front row goes quiet the way men go quiet."
    else:
        show cg ls_ring_moo onlayer cgl
        "You clamp your mouth shut. It opens."
        ls_cherry "\"{i}Mmmmmmmoooooo{/i}—!\"" with vnfx("shake")
        "Long and loud, right at the stands. They moo back. Half the county, mooing at you. Your knees nearly go."
    show cg ls_judges onlayer cgl
    "The judges come down the line. Women in striped coats and a man with hands like shovels. They feel Buttercup's horns. They feel your {i}tits.{/i}"
    "Hands everywhere. Weighing them. Squeezing."
    ls_cherry "\"Hey— hands— don't— {i}ahh{/i}—\""
    "A thumb on your nipple, and it squirts, right on a judge's sleeve."
    ls_cherry "\"{i}Mmh{/i}— stop— {i}ahh{/i}—\""
    "\"Excellent letdown,\" she says, writing."
    "One of them runs her hand down your belly toward the little bump in your panties. Stops. Taps your bell instead, and listens to it ring."
    "\"Marsh's mystery heifer,\" she says to the crowd, and they cheer."
    show cg ls_saltspring onlayer cgl
    "The Saltspring show cow, tall and smug, is waiting for the ribbon with her chest out. Brown hair, a gold bell, tits like two prize pumpkins. She looks you up and down."
    "\"Marsh is showing {i}that?{/i}\" she says. \"She's not even finished.\""
    "Your tits squirt at her. Both of them. Right across her shiny gold bell. You didn't mean to. You're not sorry. The front row howls."
    show cg ls_ribbon onlayer cgl
    "\"Blue ribbon, dairy heifer division...\" The ring master holds it up. \"{b}Marsh Farm's Cherry!{/b}\"" with vnfx("flash")
    "The crowd goes mad. Buttercup screams. Marigold whoops and lifts you right off the sawdust."
    show ls_hester smile at vn_cast_slot
    "Hester walks over, unhurried, and pins the blue ribbon on your cow-print bra, right between your tits."
    $ ls.ribbon = True
    ls_hester "\"For the records.\""
    "And then, quieter."
    ls_hester "\"Knew you'd get there.\""
    hide ls_hester
    "{size=-5}{color=#ff8fa3}▸ Back to the trailer{/color}{/size}"
    $ vn_pass(240)
    jump ls_seven_trailer

label ls_seven_trailer:
    $ vn_enter(bg="ls_trailer", pc="shocked", pc_tag="ls_pc", cast=[("ls_marigold", "pleased")], cg="ls_trailer_crowd")
    show cg ls_trailer_crowd onlayer cgl
    "The trailer's packed. Ribbons on the window ledges, a trough of creamed mash for the winners, and the other farms crowding the door to get a look at the mystery heifer."
    ls_marigold "\"Let's give them something to gossip about.\""
    "She pulls you into her lap."
    ls_cherry "\"Not here— not in front of— Marigold, {i}no{/i}—\""
    show cg ls_trailer_polish onlayer cgl
    "She does it right there, in front of everybody. Her cock between your tits, her hands over yours pushing them round it, your blue ribbon bouncing on top. The Saltspring girls cheer. The Bellweather girls cheer louder. Somebody starts a chant and everybody joins in."
    ls_marigold "\"Shoulders back, Cherry. Let them {i}see.{/i}\""
    ls_cherry "\"Don't look— don't {i}look{/i} at me— {i}mmmmooo{/i}— {i}mmmmmmoooooo{/i}—\""
    show cg ls_trailer_cum onlayer cgl
    "She cums up your chest in front of the whole trailer and they {i}applaud.{/i}" with vnfx("flash")
    "The Saltspring cow's at the front of the crowd with her arms folded. She watches you try to wipe it off. She watches your fingers rub it into your tits instead, and go to your mouth. Her own nipples are poking right through her show top."
    "\"...Fine,\" she says. \"{i}Fine.{/i} She's finished.\""
    show ls_buttercup soft at vn_cast_slot
    "Buttercup squeezes in beside you after, flushed, her own tits heaving and leaking."
    ls_buttercup "\"Ribbon cows trade. It's tradition.\""
    "In a whisper. She's already pulling you down onto the feed mats."
    menu:
        "Buttercup, on the feed mats."
        "Buttercup latches on":
            jump ls_seven_buttercup
        "The trailer rolls home for nine":
            hide ls_buttercup
            $ vn_until(21)
            jump ls_bell

label ls_seven_buttercup:
    $ vn_enter(bg="ls_trailer", pc="flushed", pc_tag="ls_pc", cast=[], cg="ls_bc_trade")
    show cg ls_bc_trade onlayer cgl
    "She lies down head to toe with you on the feed mats, takes your nipple in her mouth, and pushes hers against your lips."
    ls_cherry "\"Buttercup— wait— I didn't say— {i}mmf{/i}—\""
    "Her milk floods your tongue. Warm. Creamy. {i}Sweet.{/i} She sucks yours at the same time, and you moan into her tit, and the whole trailer goes \"{i}aww.{/i}\""
    ls_cherry "\"{i}Mmmh{/i}— Buttercup— {i}mmmh{/i}—\""
    "You stop pushing at her. You start drinking. You drink till you're dizzy. She drinks till you're empty on one side, and switches."
    show ls_buttercup grin at vn_cast_slot
    ls_buttercup "\"Told you you'd be fun.\""
    hide ls_buttercup
    "Milk on her chin.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_7:
    show ls_marigold stern at vn_cast_slot
    ls_marigold "\"Dairy lead goes first.\""
    "Marigold straps you in herself."
    hide ls_marigold
    show cg ls_milk_7 onlayer cgl
    vn_sfx "Ssssh-ssssh-ssssh."
    "The cups latch, and you {i}gush.{/i} Both tits at once, thick white streams, so hard you can hear it hit the pail."
    ls_cherry "\"{i}Mmmmmmooooooooo{/i}—!\"" with vnfx("shake")
    "The other farms crowd the door to watch. Somebody whistles. Buttercup moos along from the next frame."
    "The plug hums in your ass and your caged nub doesn't even twitch. The back line sucks at nothing. Dry."
    show cg ls_pail_over onlayer cgl
    "The pail fills, and fills, and slops over the top."
    ls_hester "\"Show record. Write it up.\""
    "And for once she doesn't sound bored at all.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 8: the heat (Livestock Day Eight, Eight Drink, Eight Heat, Eight Taste, Eight Milking) ---------------

label ls_day_8:
    $ ls_body(7)
    $ ls.fit = "nude"
    $ vn_enter(bg="ls_marigold_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_8")
    show cg ls_wake_8 onlayer cgl
    "You can't see your feet."
    "{color=#ff5fb8}You look down and it's all tits. {i}Huge{/i} ones, an H. They've filled out overnight into two enormous soft heavy globes that sit on your belly and spill out to the sides, and when you breathe they {i}wobble.{/i}{/color}"
    ls_cherry "\"Oh my god— oh my {i}god{/i}—\""
    "You heave them up in both arms and they overflow your arms."
    ls_cherry "\"{i}Mmmmh{/i}— so {i}big{/i}—\""
    "{color=#ff5fb8}Your hips have gone wide. Proper wide. You'd have to turn sideways for the stall gate. Your braid's down to your ribs, white and black, swinging.{/color}"
    "{color=#ff5fb8}And your horns. You reach up and they've grown out and curled, a smooth pretty sweep each side of your head. Like Buttercup's. Like a {i}show{/i} cow's.{/color}"
    show bg ls_long_barn onlayer bgl
    hide cg onlayer cgl
    "You cradle your tits on the walk to the trough and they leak on your arms the whole way. You try to walk it like a man. Your shoulders go back. Your hips roll. {i}Let them see.{/i} Your chest knows every trick Marigold taught it, and your mouth knows the rest."
    show ls_marigold fond at vn_cast_slot
    "Marigold's waiting at the end of the aisle."
    ls_marigold "\"Come here, Cherry. Your turn to drink.\""
    ls_cherry "\"I'm fine here.\""
    hide ls_marigold
    show cg ls_carried onlayer cgl
    "She comes to you instead. She scoops you up like a bale, tits and all, and carries you back to her stall.\n{size=-5}{color=#ff8fa3}▸ Carried to her straw{/color}{/size}"
    jump ls_eight_drink

label ls_eight_drink:
    $ ls_advance(8)
    $ vn_enter(bg="ls_marigold_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_drink")
    show cg ls_drink onlayer cgl
    "She sits in her straw with you in her lap, sideways, your head in the crook of her arm like she's going to feed you. She is going to feed you."
    "Her nipple's right there. Big and dark and dripping. She guides it to your lips."
    ls_cherry "\"No— I'm not— I'm not drinking from— {i}mmf{/i}—\""
    "She presses it in. Her hand comes round the back of your head, and holds, gentle and total, and your face is in her tit and her nipple's on your tongue."
    "You've never tasted her. Not once. Not in all of it."
    ls_marigold "\"It's for your own good, Cherry. Drink.\""
    show cg ls_drink_deep onlayer cgl
    "Her milk floods your mouth, thick, rich, sweeter than the mash, sweeter than anything, and you swallow because you have to, and then you {i}moan{/i}, and then—"
    ls_cherry "\"{i}Mmf{/i}— no— {i}mmmh{/i}—\""
    "You're sucking harder."
    ls_marigold "\"That's it. Drink up.\""
    "You drink like you were born to, swearing into her tit between pulls. Long pulls, throat working, your tongue flat on her nipple the way she did yours. She hums."
    "And then the heat comes."
    "It starts low, in your belly, and rolls out through your hips like warm syrup. Then it's not warm. It's {i}hot.{/i} Your thighs fall open on their own. Your caged nub throbs so hard against the steel you whimper round her nipple."
    ls_marigold "\"Mm. There it is.\""
    ls_cherry "\"{i}Mmmh{/i}— what's— what did you— what's {i}happening{/i}—\""
    ls_marigold "\"Keep drinking.\""
    "Her hand on your head doesn't move.\n{size=-5}{color=#ff8fa3}▸ She holds you on it{/color}{/size}"
    jump ls_eight_heat

label ls_eight_heat:
    show cg ls_heat onlayer cgl
    "The heat doesn't stop. It builds. You're writhing in her lap, milk on your chin, hips grinding on nothing, and you can't close your legs. You can't. They won't."
    ls_cherry "\"{i}Haaah{/i}— make it stop— Marigold— {i}Marigold{/i}— it's so {i}hot{/i}—\""
    show cg ls_heat_herd onlayer cgl
    "The herd's at the stall rail. Buttercup. Petal. The Marsh line, all of them, crowding in, horns and ears and tails, watching."
    ls_cherry "\"Don't— don't {i}watch{/i}—\""
    "Somebody hums. Somebody else moos, soft, and then they're all mooing, low, like they're singing you through it."
    "Marigold's big hand slides down your belly, over your thighs, to the cage. She rests her palm on it. It pulses. Everything between your legs pulses, like a heartbeat, harder and harder and—"
    vn_sfx "Click." with vnfx("flash")
    $ ls.caged = False
    $ ls_body(8)
    show cg ls_cage_empty onlayer cgl
    "The cage falls into her palm. She holds it up, between two fingers, for the herd to see."
    "It's {i}empty.{/i} The whole stall roars."
    "{color=#ff5fb8}You look down. Your cock's gone. Your balls are gone. There's just smooth plump skin and a pair of wet swollen lips, pink and shiny, and they're {i}throbbing.{/i}{/color}"
    ls_cherry "\"No— {i}no{/i}— where is it— give it {i}back{/i}—\""
    "{color=#ff5fb8}Your hips have spread wider still, cradled in her lap. Your tits swell one more time against her arm, heavier, fuller, an I. Your braid slides warm down your back.{/color}"
    "Your hand goes down. You don't tell it to. You touch it."
    ls_cherry "\"{i}AHHH{/i}—!\"" with vnfx("shake")
    "Wet. So wet. Slick and hot and so sensitive, and your fingers slide right between the lips and find a little hard nub at the top and you—"
    show cg ls_heat_cum onlayer cgl
    ls_cherry "\"{i}Oh{/i}— {i}oh god{/i}— {i}ohh my god{/i}— it's— I've got a— {i}ahhhhh{/i}—!\"" with vnfx("flash")
    "You come in her lap with your fingers on your new clit, legs kicking, squirting milk and slick everywhere, mooing at the rafters while the whole herd moos back."
    show ls_hester flat at vn_cast_slot
    "Hester's at the rail with your card from your gate. She reads the old line. She crosses it out. Writes."
    show screen ls_card
    "{color=#ffd700}DISCREPANCY — RESOLVED. FEMALE.{/color}"
    ls_hester "\"That's that.\""
    hide screen ls_card
    hide ls_hester
    ls_cherry "\"It's not— it's {i}not{/i}— {i}mmmh{/i}—\""
    "Your mouth's still sweet with Marigold's milk. You lick your lips and moan like you're tasting her all over again; your mouth's as sensitive as your new pussy now. Your tongue knows exactly how."
    show ls_marigold pleased at vn_cast_slot
    "Marigold kisses your forehead and her eyes go dark."
    ls_marigold "\"Now let me have a taste of what you've got.\""
    menu:
        "Her hands on your knees."
        "She spreads your knees":
            hide ls_marigold
            jump ls_eight_taste
        "She lets you lie there till nine":
            hide ls_marigold
            $ vn_until(21)
            jump ls_bell

label ls_eight_taste:
    show cg ls_taste onlayer cgl
    "She lays you back in the straw, pushes your knees apart with both big hands, and holds them there, and puts her big head between your thighs."
    ls_cherry "\"Wait— not there— not {i}there{/i}, it's— it's {i}new{/i}— Marigold—\""
    vn_sfx "Shlllk."
    "Her tongue. Broad and hot and flat, one long slow lick from the bottom of your new pussy to the top."
    ls_cherry "\"{i}Ahhhhhh{/i}—!\""
    show cg ls_taste_deep onlayer cgl
    "Again. And she pushes it {i}in{/i}, inside you, and curls it, and you grab her horns with both hands to shove her off, and scream, and don't shove."
    ls_cherry "\"Marigold— {i}Marigold{/i}— your tongue— it's {i}in{/i} me— get it— {i}don't{/i}— {i}ahh{/i}— {i}ahhh{/i}—!\""
    "She eats you like she drinks you: slow and patient and like she owns it. Her lips on your clit. Her tongue deep. Your hips grinding on her face now, your thighs clamped round her ears, your tits squirting all over her horns."
    ls_cherry "\"Don't stop— {i}don't stop{/i}— please— {i}please{/i}—!\"" with vnfx("shake")
    show cg ls_taste_cum onlayer cgl
    "You come on her tongue. Then again. The third time you just moo, long and helpless, and she laughs into you." with vnfx("flash")
    ls_marigold "\"Sweet. Saving the rest for the herd.\""
    "Licking her lips.\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_bell

label ls_milking_8:
    show cg ls_plug_shelf onlayer cgl
    "The plug's on the shelf. Hester's put it away. Washed and dried and put away."
    ls_hester "\"No need.\""
    show cg ls_milk_8 onlayer cgl
    "Just the cups tonight. Just the front. You lie on the bench with your knees spread and your new pussy dripping on the pad, and the cups go on, and Hester rolls the churn under the line."
    "{i}The churn.{/i}"
    vn_sfx "SSSSHH."
    "And you fill it. Thick white streams, both tits, roaring into it, and every pull goes straight down to your clit. You're grinding on the bench. You're mooing so loud the rafters ring."
    ls_cherry "\"{i}Mmmmmmmmmmmoooooooooo{/i}—!\"" with vnfx("shake")
    show cg ls_milk_8_cum onlayer cgl
    "You come from your tits. Just your tits. Your new pussy clenches on nothing and gushes, and the churn keeps filling." with vnfx("flash")
    "Hester doesn't write anything. She just watches it fill, with her pen in her hand.\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    jump ls_night

## ---- day 9: the herd night (ending.twee: Livestock Day Nine, Herd Night, Herd After, Herd Churn) -------------

label ls_day_9:
    $ ls.fit = "nude"
    $ vn_enter(bg="ls_marigold_stall", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_wake_9")
    show cg ls_wake_9 onlayer cgl
    "You wake up in Marigold's straw with her arm over you and your new pussy wet against her thigh."
    show bg ls_long_barn onlayer bgl
    show cg ls_bunting onlayer cgl
    "The barn's loud. Hammers. Ladders. Petal's up a ladder hanging bunting along the crossbeams, feed-sack colours, and the twins are stacking hay bales into a dais in the middle of the aisle, and for once nobody's yelling at them."
    show ls_buttercup grin at vn_cast_slot
    ls_buttercup "\"Herd night. When a heifer resolves, the herd sees her done proper.\""
    "Leaning on the stall. She's got ribbons in her horns already."
    ls_cherry "\"Done proper.\""
    hide ls_buttercup
    "Marigold's hand squeezes your hip. You feel her cock stir against your ass, and your pussy clenches on nothing, and you get it."
    ls_cherry "\"{i}Oh.{/i} No. No, no, absolutely not, not in front of— not {i}that{/i}—\""
    ls_marigold "\"Shh. Forms are final, Cherry.\""
    "Into your hair, fond."
    $ ls.fit = "show"
    show cg ls_herd_dress onlayer cgl
    "All day they get you ready, and you argue through all of it. Buttercup brushes your braid out and plaits it again, tighter, white and black. Petal sits on your legs and does your face, pink and blue and rosy, and kisses your nose."
    "The cow-print set again, the bra cupping what it can, the panties stretched tight over your new pussy. Your ribbon. Your bell, polished."
    "And your hand keeps going between your legs. You pull it away. It goes back. Nobody tells you to stop, and you can't."
    show cg ls_herd_trough onlayer cgl
    "At the trough the whole herd makes room for you in the middle. Cow-girls either side, warm shoulders, swinging tits, everybody's tails going. Petal ladles the creamed mash, the good stuff, into your bit first."
    ls_petal "\"Ribbon cow eats first. That's the rule.\""
    "You put your face in it. It's sweet. You moo into it without meaning to, and the cow-girls either side moo back, and it goes down the line, and you've got mash on your nose and your face is burning."
    "The Hasketts come past with a bale each and both of them stop dead and stare at the panties."
    ls_billy "\"Is that—\""
    ls_bart "\"It {i}is!{/i}\""
    "\"Congratulations!\" they chorus, beaming, and walk straight into a post.\n{size=-5}{color=#ff8fa3}▸ Evening{/color}{/size}"
    $ vn_until(20)
    jump ls_herd_night

label ls_herd_night:
    $ vn_enter(bg="ls_herd_dais", pc="shocked", pc_tag="ls_pc", cast=[], cg="ls_herd_lanterns")
    show cg ls_herd_lanterns onlayer cgl
    "Lanterns everywhere. The whole herd in the aisle in their show ribbons, cow-girls and sow-girls and the Hasketts in clean shirts, Angus at the back with his arms folded, a table of creamed mash. Everybody's looking at you."
    "Buttercup and Petal walk you up onto the dais of bales, one at each elbow, your tail swishing and your tits leaking through the cow-print and your thighs slick."
    show cg ls_herd_card onlayer cgl
    show ls_hester flat at vn_cast_slot
    "Hester steps up beside you with the card."
    ls_hester "\"Intake. Heifer. Female.\""
    "She looks at the herd over her glasses."
    ls_hester "\"Female struck. Discrepancy, monitor.\""
    "Laughter."
    $ _ls_i = 2
    while _ls_i <= 8:
        $ _ls_line = LS_CARD[_ls_i]
        ls_hester "\"[_ls_line]\""
        $ _ls_i += 1
    "Every line gets a cheer. \"Stud-privileged\" gets a roar and a slap on Angus's back. \"Blue ribbon\" gets everybody mooing."
    ls_hester "\"Resolved. Female.\""
    "She lowers the card."
    ls_hester "\"Marigold.\""
    hide ls_hester
    show cg ls_herd_marigold onlayer cgl
    "Marigold steps up onto the bales. Apron off. Horns garlanded. Her tits heave and leak. Her cock stands up from her hips, huge and ridged and dripping, and she looks at you like she's waited all season for this. She has."
    ls_marigold "\"Lie back, Cherry. Let them see.\""
    "So the whole barn hears."
    ls_cherry "\"No. {i}No.{/i} Not in front of everyone— not {i}there{/i}— Marigold, I'm {i}not{/i}—\""
    show cg ls_herd_open onlayer cgl
    "She lays you back on the bales herself. One big hand on your chest, gentle, total. She takes your knees and opens them, and holds them open, slick and shining, and the whole herd leans in."
    ls_marigold "\"It's for your own good, Cherry.\""
    "Fond as anything. She kneels between them. The fat ridged head of her cock rubs up and down your wet new lips, once, twice, and you buck, and it doesn't matter, and then it presses in, and your pussy opens round it, and the head slips inside you in front of everybody."
    ls_cherry "\"{i}Ahhhhh{/i}— no— take it {i}out{/i}— Marigold— {i}Marigold{/i}—!\"" with vnfx("shake")
    menu:
        "In front of everybody."
        "Struggle":
            $ ls.fight = "struggle"
        "Swear":
            $ ls.fight = "swear"
        "Grit your teeth":
            $ ls.fight = "grit"
    jump ls_herd_sex

label ls_herd_after:
    $ vn_enter(bg="ls_herd_dais", pc="broken", pc_tag="ls_pc", cast=[], cg="ls_herd_deeper")
    show cg ls_herd_deeper onlayer cgl
    $ _ls_f = ls_fight_line()
    "[_ls_f]"
    if ls_enc.partner_came:
        "She cums buried to the root in your brand-new pussy, the first one ever, and you feel every hot pulse of it fill you right up."
    else:
        "She's buried to the root in your brand-new pussy, the first cock ever in it, and she isn't done."
    ls_cherry "\"No more— no more— not in front of them—\""
    "And she keeps going. She hooks your knees over her arms and fucks you deeper, slow and heavy, in front of everybody, and something in you {i}gives.{/i}"
    $ ls_body(9)
    show cg ls_herd_grow onlayer cgl
    "{color=#ff5fb8}Your tits swell. Right there, under her, they swell up and up, huge and round and full, past anything, past {i}Buttercup's{/i}, a J, and the cow-print bra gives up and they spill free, squirting milk up Marigold's chest every time she thrusts.{/color}"
    ls_cherry "\"{i}AHHH{/i}— they're— they're {i}growing{/i}— stop— {i}Marigold{/i}—!\""
    vn_sfx "Rrrip."
    "{color=#ff5fb8}Your hips spread wide on the bales. Your ass swells heavy and round and the cow-print panties split right up the seam, and the herd cheers.{/color}"
    "{color=#ff5fb8}Your horns, your ears, your tail, all of it hot and tingling and {i}finished.{/i}{/color}"
    "And when you open your mouth to scream no, what comes out is one long, deep, shameless—"
    ls_cherry "\"{i}MMMMMMMMMOOOOOOOOOOOOO{/i}—!\"" with vnfx("shake")
    "The whole barn moos back. It shakes the lanterns."
    "Your new pussy grips her like it's been doing it for years. Squeezing. Milking her. Rolling up to meet every stroke. You didn't tell it to. You can't make it stop."
    ls_marigold "\"Gonna fill you. In front of all of them.\""
    "Growling it in your ear."
    ls_cherry "\"Don't— don't— {i}mmmoo{/i}— don't stop— {i}please{/i}— fill me— oh god {i}fill me{/i}— {i}mmmmoooo{/i}—!\""
    show cg ls_herd_flood onlayer cgl
    "She slams home and holds and floods you. Hot. Thick. So much it gushes out round her cock and runs down your thighs onto the hay, and you come so hard you black out for a second, mooing, begging, tits pouring." with vnfx("flash")
    show cg ls_herd_kiss onlayer cgl
    "When you come back, she's kissing you. The herd's still cheering. Your tits are still pouring. You're still moaning {i}more{/i} into her mouth, and you don't remember starting."
    ls_marigold "\"There. {i}Now{/i} you're done proper.\"\n{size=-5}{color=#ff8fa3}▸ Nine o'clock{/color}{/size}"
    $ vn_until(21)
    jump ls_herd_churn

label ls_herd_churn:
    $ ls_advance(9)
    $ ls.fit = "nude"
    $ vn_enter(bg="ls_milking_frame", pc="broken", pc_tag="ls_pc", cast=[], cg="ls_churn_carry")
    vn_sfx "DONG. DONG. DONG."
    show cg ls_churn_carry onlayer cgl
    "They carry you to the frame. You couldn't walk if you tried. Cum still running down your thighs, your tits so full they're shining."
    show cg ls_churn onlayer cgl
    "The cups go on. And you {i}pour.{/i}"
    ls_cherry "\"{i}Mmmmmmmmmmmmmmoooooooooooooo{/i}—\"" with vnfx("shake")
    "It roars into the churn, both tits, endless, and every pull goes straight through you and you come on the bench, and come again, and the churn fills—"
    "—and fills—"
    show cg ls_churn_over onlayer cgl
    "—and runs over. Milk spills down the sides of the churn, across the floor, round everybody's feet. Petal shrieks and gets a bucket. Buttercup laughs and laughs. Marigold's hand is on your belly the whole time, proud." with vnfx("flash")
    show ls_hester smile at vn_cast_slot
    "Hester looks at the churn overflowing for a long, long moment. Then she writes on your card, in big blocky capitals, and holds it up for the herd."
    show screen ls_card
    "{color=#ffd700}COW. DAIRY PRIME.{/color}\n{size=-5}{color=#ff8fa3}▸ Go on{/color}{/size}"
    hide screen ls_card
    hide ls_hester
    $ vn_pass(30)
    jump ls_blue_ribbon

## ---- the ending (Livestock Blue Ribbon, Epilogue Stay, Epilogue Go) ---------------------------------------------

label ls_blue_ribbon:
    $ vn_enter(bg="ls_marigold_stall", pc="broken", pc_tag="ls_pc", cast=[], cg="ls_blue_ribbon")
    show cg ls_blue_ribbon onlayer cgl
    $ achievement.grant("Blue Ribbon")
    "You lie in the straw with the herd round you, warm and full and empty all at once."
    "Horns. Ears. A tail. Huge tits, leaking. Wide hips. A pussy still dripping Marigold. A bell on your collar and a blue ribbon on your chest."
    "The card on the gate says {color=#ffd700}COW. DAIRY PRIME.{/color} It's right. It was always going to be right."
    ls_hester "\"Forms are final.\""
    "On her way past."
    menu:
        "Stay, or go."
        "Stay" (ending=True):
            $ ls.ending = "stay"
            jump ls_epilogue_stay
        "Go" (ending=True):
            $ ls.ending = "go"
            jump ls_epilogue_go

label ls_epilogue_stay:
    $ vn_enter(bg="ls_yard", pc="broken", pc_tag="ls_pc", cast=[], cg="ls_stay_lorry")
    ## winter to spring
    $ vn_pass(90 * 1440)
    $ vn_set_time(10, 0)
    show cg ls_stay_lorry onlayer cgl
    "Spring."
    "The stock lorry pulls into the yard and the tailgate drops, and a man climbs out blinking. Skinny, city haircut, a tag through his ear. He's holding his intake form like it's a summons."
    "\"There's been a mistake,\" he says. \"I signed up for seasonal help—\""
    show ls_hester flat at vn_cast_slot
    "Hester doesn't even look up. She holds the pen out to you."
    hide ls_hester
    show cg ls_stay_welcome onlayer cgl
    "You take it. You don't have to be asked. You read his card. {color=#ffd700}HEIFER, FEMALE.{/color} Your pussy clenches, and your tits let down a little, just reading it."
    "Under {i}Annotations{/i} you write one word, and hang it on his gate."
    "{color=#ffd700}Welcome.{/color}"
    "You mean it. You mean every letter. You know exactly what's coming for him, every night of it, and you can't wait for him to have it."
    ls_cherry "\"Eat your mash.\""
    "Warm as Marigold, and your tail swishes, and your tits bounce, and he stares at them all the way to the trough."
    show cg ls_stay_trough onlayer cgl
    "He tries to use his hands. You smack his wrist."
    vn_sfx "Slap."
    ls_cherry "\"No hands, sugar.\""
    "It comes out in Petal's voice, and Petal, mopping down the line, snorts."
    "You kneel next to him and show him. Chest up. Lips loose. One long flat lick through the mash. Your tits hang down either side of your arms while you do it and he can't look anywhere else."
    "He puts his face in. He goes back for more. His cock's tenting the blanket."
    ls_cherry "\"Ooh. Somebody likes breakfast.\""
    show bg ls_milking_frame onlayer bgl
    show cg ls_stay_bell onlayer cgl
    "At nine the bell rings, and you're first in line, cups on before it's finished ringing, moaning for them before they even latch, and the churn roars full."
    ls_cherry "\"{i}Mmmmoooo{/i}— yes— {i}milk me{/i}—\""
    "You hear him at the end of the line, swearing at the plug, and you moo for him, loud and happy, so he knows it's going to be all right. It is. It's going to be the best thing that ever happened to him."
    show bg ls_marigold_stall onlayer bgl
    show cg ls_stay_again onlayer cgl
    "After, Marigold's stall. You're there before she is, on your back in the deep straw with your knees open, and when she climbs in you pull her down onto you by the horns."
    ls_cherry "\"Again. Again, Marigold, {i}again{/i}—\""
    "Her arms, her cock, her milk. Every night. Yours."
    jump ls_route_return

label ls_epilogue_go:
    $ ls.fit = "sundress"
    $ vn_enter(bg="ls_yard", pc="flushed", pc_tag="ls_pc", cast=[], cg="ls_go_gate")
    ## the morning after the herd night
    $ vn_until(9)
    show cg ls_go_gate onlayer cgl
    "Hester finds you a sundress in the lost-property box. It's never going to close over your tits. You wear it anyway."
    show ls_hester flat at vn_cast_slot
    "She hands you a spare cow bell at the gate, and taps the one on your collar."
    ls_hester "\"Keep that on in town. Off the farm, the horns forget.\""
    "At the gate she stops you with her clipboard."
    ls_hester "\"Nine o'clock. You'll feel it.\""
    hide ls_hester
    "Buttercup moos goodbye over the fence. Marigold doesn't say anything. She doesn't have to. Your pussy clenches just looking at her."
    show cg ls_go_road onlayer cgl
    "You walk down the farm road toward town, tits bouncing, tail swishing under the hem, bell going {i}tink, tink, tink.{/i}"
    $ vn_until(21)
    show bg ls_town_street onlayer bgl
    show cg ls_go_nine onlayer cgl
    "And that night, in town, at nine o'clock exactly, you feel it."
    "It starts in your tits. A hot tight swell, and then the letdown, all at once, right through the sundress, two big wet patches, and your knees buckle on the pavement and you moan out loud." with vnfx("shake")
    ls_cherry "\"{i}Mmmmmoooo{/i}—\""
    "A man at the bus stop stares. You stare back, and squeeze, and milk runs down your belly under the dress."
    "Hester was right. You'll feel it every night. Wherever you are."
    jump ls_route_return
