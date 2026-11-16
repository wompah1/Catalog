## THE SOURCE: scales' passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, ending.twee), written as beats; the director scenes are in
## scenes.rpy. The original is in catalog/docs/routes/vn-original/scales/. One rung a day: a rung's
## night sleeps into its morning, where the body lands; the hub (her quarters) offers the day beat
## and dusting the perch, both flavour; the plate warms at dusk and the next rung plays. The red is
## the one gap the story needs. Rung 5's two days in the kitchens are the rung's own story.

## ---- DAY 1: the road, the gatehouse, "Mine.", the plate, the quarters (Scales Opening, Mine) --

label scl_road:
    $ scl.fit = "village"
    $ vn_enter(bg="scl_road", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_road_climb")
    "Three harvests."
    "That's what you cost. Your uncle's barley. Your mother's yams. The millet off the drying lines. Three harvests in bribes, to envoys and intermediaries and clerks, so you could climb this road and come home as {i}something{/i}."
    "Your root is metal-water-earth. Thin as string. The village priest wouldn't read it out loud."
    "You climb anyway."
    hide cg onlayer cgl
    "The road is cut stone, switching back and forth up the face of the Coiling Fang, wide enough for something much bigger than a cart. Steam curls out of vents in the rock. At the top: a gatehouse. A clerk. A ledger."
    $ vn_enter(bg="scl_gatehouse", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_passing_beast")
    "And something coming down the road. Two legs, horns out, taller than any man, not even trying to look human about it."
    vn_sfx "{i}THUD.{/i}" with vnfx("shake")
    show scl_pc protesting
    "Your knees hit the stone before your brain gets a vote. Forehead down. Palms flat. Heart slamming."
    "It doesn't stop. It doesn't even look."
    hide cg onlayer cgl
    scl_clerk "\"First time? Name.\""
    "The clerk doesn't look up either."
    show scl_pc stubborn
    scl_you "\"[scl_full_name]. I'm twenty. I've come to—\""
    "You get up, dusting off your knees."
    scl_clerk "\"Contract a beast. You and everyone.\""
    vn_sfx "{i}Scratch, scratch.{/i}"
    scl_clerk "\"Household intake, second arch. Somebody will be along.\"\n{size=-5}{color=#ff8fa3}▸ Wait by the second arch{/color}{/size}"
    $ vn_pass(40)
    jump scl_mine

## "Mine." The plate, cut from her forearm scale.
label scl_mine:
    $ vn_enter(bg="scl_gatehouse", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "Somebody is along inside the hour."
    show cg scl_longqi_steam onlayer cgl
    "She walks out of the steam like it belongs to her. It does."
    "A woman's shape, and nobody would ever mistake it for human. Horns curving back, copper-bright. Red-gold scales worn open along her forearms and hips like pins of rank. Gold slit eyes. A tail, swaying. And hair the red of burning pine pitch, falling in two heavy tails past her shoulders."
    vn_sfx "{i}THUD.{/i}"
    show scl_pc protesting
    "Your knees again."
    hide cg onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_clerk "\"Long Qi. Fourth of the nine.\""
    "The clerk tells her ledger. She reads your form. Then she reads you, and takes longer over that."
    scl_longqi "\"Mine.\""
    "To the clerk. Then, down at you:"
    scl_longqi "\"Stand, household. You'll be fed, housed and documented. That last isn't a formality. Everything on this mountain is a document. Hold still.\""
    show cg scl_plate_cut onlayer cgl
    "She takes a scale off her own forearm."
    vn_sfx "{i}Tik.{/i}"
    "Like a coin dropped on stone."
    show cg scl_plate onlayer cgl
    "By sunset it's a plate on a cord around your neck, {i}[scl_full_name]{/i} cut deep into it, and her seal on the back. It sits on your sternum and goes warm for a heartbeat. Like it noticed you."
    hide cg onlayer cgl
    hide scl_longqi
    show scl_ahning grin at vn_cast_slot
    scl_ahning "\"Don't lose that. That's how she finds you. Anywhere on the mountain. I'm Ah-Ning. Twenty-seven, six years household. Welcome to the bottom of the ledger.\""
    "A woman at your elbow, grinning. Plain clothes, sleeves rolled, bun coming down.\n{size=-5}{color=#ff8fa3}▸ Into the household{/color}{/size}"
    $ vn_pass(30)
    jump scl_quarters

label scl_quarters:
    $ scl.fit = "robe"
    $ vn_enter(bg="scl_quarters", pc="stubborn", pc_tag="scl_pc", cast=[("scl_ahning", "grin")], cg=None)
    "Long Qi's quarters run half a gallery, high on the south face. The stone is hot as a kiln under your bare feet. Bedding is piled on levels, silk and fur and shed red scales, all cut for her size."
    show cg scl_perch onlayer cgl
    "At the far end: a perch. Carved stone, inset with copper and jade, a blanket folded across it. Dusted. Never sat on. The household steps round it without letting a sleeve brush the edge."
    scl_ahning "\"Dust that. Every day.\""
    scl_you "\"What is it?\""
    scl_ahning "\"Dust it.\""
    hide cg onlayer cgl
    "She says it again, cheerfully, and shows you a bedding roll ten steps from it."
    "Rice. Weak wine. A folded robe. Through the hangings you can see Long Qi at her desk, signing, the scratch of her brush quick and steady, her tail swaying in time.\n{size=-5}{color=#ff8fa3}▸ Lie down on the hot stone{/color}{/size}"
    $ vn_until(22)
    jump scl_first_night

## ---- RUNG 1: "Household. Mouth." (non-con: she takes; you protest round her) ---------------

label scl_first_night:
    $ vn_enter(bg="scl_quarters_night", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "You sleep."
    "Then the stone gets hotter. A weight comes down across your chest, heavy and smooth and warm, and pins you flat to the bedding roll. Scale scrapes on slate."
    "You try to sit up. You can't. Your eyes come open."
    show cg scl_first_pin onlayer cgl
    show scl_pc protesting
    "A tail. Red-gold, thick as your thigh, laid across your chest and pinning both your arms under the blanket. And Long Qi, crouched over your face. Red twin tails falling either side of you. Horns black against the lamp. Robe open to the waist."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Household. Mouth.\""
    "Not cruel. Not a question either. The voice of a clerk reading out the next line of a form."
    "She's hard. Thick, heavy at the root, arching up out of a brush of copper scales between her thighs. Faint ridges run down the underside and catch the lamplight every time it twitches. A clear bead rolls off the tip and lands on your lip."
    scl_you "\"Lady— wait— I'm here to {i}serve{/i}, I'll do the floors, the— {i}mmph{/i}—!\""
    show cg scl_first_mouth onlayer cgl
    "The head of it is on your mouth before you've finished the word. Hot as a coal. It smells like hot metal and salt and smoke. Her claws tip your chin up, and your jaw opens because the hinge of it is in her hand."
    show scl_pc flushed
    "Under the blanket, your own small cock has gone stiff and aching just from the smell of her. You didn't tell it to. Your face burns."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Breathe, household.\""
    "She slides in."
    "No ceremony. Your lips stretch round her. The first ridge drags over your tongue, {i}bump{/i}, then the next. Her fist closes in your hair and tilts your head open, and her tail stays exactly where it is."
    vn_sfx "{i}Glk.{/i}"
    scl_you "\"Mmf— {i}mmnh{/i}— Lmmf— {i}Lady{/i}—!\""
    "You're loud from the first ridge. It's meant to be a no. It comes out round her cock as a long muffled moan, and the gallery carries it, and she doesn't care in the slightest."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Louder.\""
    "She observes it. It isn't an order. You were already louder."
    vn_sfx "{i}Glk. Glk. Hlk.{/i}"
    "You buck. The tail doesn't move. You twist your head and her hand turns it straight back. Spit runs off your chin onto her scales. She rocks, slow, relentless, a little deeper every time, until a ridge catches at the back of your throat and {i}pops{/i} past."
    scl_you "\"Hhngh— {i}mmmh{/i}— {i}mmmmh{/i}—!\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good.\""
    "Simple. Satisfied. The voice of an account that balanced."
    "She pulls back. All the way, till only the head rests on your tongue, and lets you breathe. One gasp. Two. A string of spit from your lip to her tip."
    scl_you "\"Hah— {i}hah{/i}— Lady— I didn't— I'm not— that's not what household's {i}for{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Household serves at night. This is the night.\""
    "Then back in. Slower. Every ridge, one at a time. {i}Bump. Bump. Bump.{/i} Your tongue finds the soft place under her head, and you didn't send it there, and she breathes out through her nose, long, and a thick pulse of pre-cum runs straight down your throat."
    "And your mouth sucks. You don't decide to. Your cheeks hollow round her all on their own, and the noise you make is wet and greedy and loud enough to wake the gallery, and inside your head you're still saying {i}no{/i}."
    scl_you "\"It's the— {i}mmf{/i}— it's the {i}steam{/i}— {i}glk{/i}—\""
    "Somewhere down the hall, a door closes, tactfully."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Louder.\""
    "She says it again, idly. You are."
    "Under your blanket your cock's leaking now. Small, and hard, and aching, and nothing's touching it. She notices. She notices everything. Her hips push in."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Household is eager.\""
    "You shake your head round her. No. No. Your hips are rolling up under the blanket the whole time."
    show cg scl_first_flood onlayer cgl
    "She swells on your tongue. A low grunt, the only sound she's made. She holds your nose flush to her scales and comes."
    "It floods you. Thick, hot, salty, {i}so much{/i}. Your cheeks bulge. You swallow because the only other choice is drowning, and swallow, and it keeps coming, spilling out of the corners of your mouth and running down your chin."
    vn_sfx "{i}Gulp. Gulp. Gulp.{/i}"
    "She keeps you there till you've taken every drop."
    show scl_pc soft
    "And under the blanket you come too. Untouched. Just from her in your throat. You moan it into her scales, loud, and you hate how loud." with vnfx("shake")
    menu:
        "Her tail still across your chest. Her cock still on your tongue."
        "She pushes back in":
            jump scl_first_sex
        "She draws out":
            jump scl_first_rest

label scl_mouth_after:
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cast=[], cg="scl_first_again_end")
    "She comes again with a low grunt, her claws tight in your hair, and you swallow all of it because she doesn't let you do anything else. It's thicker the second time."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good.\""
    "You came again. Under the blanket, untouched, just from her in your throat. It's a mess. She looks down at the damp patch, and at your face, and doesn't say anything at all. Her tail curls a little."
    scl_you "\"Hah— {i}hah{/i}— I said— Lady, I {i}said{/i}—\""
    "Your jaw's loose and warm. Your lips are puffy and slick. You can taste her everywhere."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Noted.\"\n{size=-5}{color=#ff8fa3}▸ Lie back down{/color}{/size}"
    jump scl_first_rest

label scl_first_rest:
    $ scl.tier = max(scl.tier, 1)
    $ scl.rung_day = vn_clock.day
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cast=[], cg="scl_first_rest")
    "She wipes your chin with her thumb. Then sucks the thumb clean."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good.\""
    "This time there's something under it. Approval."
    "You think she'll go. She doesn't. She lies down on your bedding roll, which is nowhere near big enough for her, and gathers you in. Her arm across your shoulders. Her cock resting hot against your cheek. Her tail draped heavy over your hip, so you aren't going anywhere."
    scl_you "\"Lady— I can serve— other ways— I can do the {i}floors{/i}—\""
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"You will. In the morning.\""
    "She agrees. Her cock twitches against your mouth. Your tongue comes out and licks it. Once. You didn't send it. You clamp your lips shut, face on fire, and she makes a small pleased sound into your hair."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"{i}Mm{/i}. You've tasted me. Now rest.\""
    "Her fingers slide into your hair. Not pushing. Just there."
    "You fall asleep like that, pinned under her tail, with her taste at the back of your throat."
    call vn_night(6)
    jump scl_first_morning

## Row 1 lands: body hair gone everywhere, found in the vents. The vents excuse: "It's the steam."
label scl_first_morning:
    $ vn_enter(bg="scl_vents", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "The steam vents, before dawn. The household bathes in the pools under them because nobody has ever told it not to."
    $ scl.fit = "nude"
    "You strip. You step into the shallowest pool. You look down."
    $ scl_body(1)
    show cg scl_smooth onlayer cgl
    "{color=#ff5fb8}Nothing.{/color}"
    "{color=#ff5fb8}No hair. Not on your legs. Not on your arms, or under them, or on your stomach. Not round your cock. Smooth everywhere, smooth as a polished bowl, and warm, and soft. Your nipples tingle in the heat. Your hips look a shade softer than you remember.{/color}"
    "{color=#ff5fb8}You run a palm down your own thigh. It {i}glides{/i}. Up your stomach. Over a nipple.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Hah{/i}—! Oh— oh, that's— {i}so{/i} soft—\""
    "{color=#ff5fb8}Everything's bare and it all lands on the nerve. Your cock jumps up stiff in the water, smooth and pink, and you can't stop stroking your own shins like an idiot. Wet hair drips on your neck. It's past your ears now. It wasn't yesterday.{/color}"
    "Your tongue keeps tracing the roof of your mouth, ridge, ridge, ridge, the shape of her. You never practised that."
    scl_you "\"{i}Mmh{/i}— why is my {i}mouth{/i}—\""
    "{color=#ff5fb8}And your lips are tender. The water lapping at them is enough to make you moan out loud in the pool.{/color}"
    hide cg onlayer cgl
    "You duck under the water and stay there. Longer than you should. It feels right down there."
    show scl_ahning grin at vn_cast_slot
    scl_ahning "\"Sleep with your mouth open again? ...You look {i}peeled{/i}.\""
    "Ah-Ning slides in next to you and stops. Squints."
    show scl_pc stubborn
    scl_you "\"It's the steam.\""
    "Your voice comes out hoarse. Soft. From last night."
    show scl_ahning quiet
    scl_ahning "\"Mm.\""
    "Says Ah-Ning, who has been here six years. She opens her mouth. She shuts it. She passes you the soap.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(60)
    jump scl_hub

## ---- THE HUB: Long Qi's quarters, the perch end (The Household) ---------------------------
## The posture line, the perch and the plate; the day beat (once a rung, flavour); dusting the
## perch (daily, until rung 5, when you stop sweeping near it); the way on, one link.

label scl_hub:
    $ _d = scl_due()
    if _d == "pearls":
        jump scl_pearls
    if _d == "red":
        jump scl_red
    $ vn_enter(bg="scl_quarters", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    show screen scl_status
    if vn_clock.hour >= 22 or vn_clock.hour < 6:
        "Long Qi's quarters: half a gallery, cut for her. Hot stone. Piled silk. Her shed scales glinting in the bedding. She's asleep in the piled silk, one arm flung out, tail twitching at a dream."
    else:
        "Long Qi's quarters: half a gallery, cut for her. Hot stone. Piled silk. Her shed scales glinting in the bedding. She's at her desk, brush going, horns bent over a docket, tail curled round a leg of the table."
    $ _go = None
    $ _cap = "The plate is cool. It'll warm at dusk." if _d == "rung" else "The plate is cool. Not tonight."
    if scl_beat_open():
        $ _cap += " The household's work never runs out, if you want some first."
    menu:
        "[_cap]"
        "Duties and dockets in the galleries" if scl_beat_open():
            $ scl.day_kind = "duties"
            $ _go = "scl_day"
        "The steam vents with Ah-Ning" if scl_beat_open():
            $ scl.day_kind = "vents"
            $ _go = "scl_day"
        "Hold the docket case at court" if scl_beat_open() and scl.tier >= 3:
            $ scl.day_kind = "court"
            $ _go = "scl_day"
        "The drawer of unfinished letters home" if scl_beat_open() and scl.tier >= 5:
            $ scl.day_kind = "letters"
            $ _go = "scl_day"
        "Dust the perch" if scl.tier < 5 and scl.dusted_day != vn_clock.day:
            $ _go = "scl_dust"
        "Wait for dusk" if _d == "rung":
            $ _go = "scl_summons"
        "Lie down for the night" if _d == "night":
            $ _go = "scl_hub_night"
    hide screen scl_status
    if _go:
        jump expression _go
    jump scl_hub

label scl_hub_night:
    "The day goes by in dockets and linen and hot stone. The plate never warms. At night you lie down on the bedding roll, ten steps from the perch."
    call vn_night(6)
    jump scl_hub

## Dusting the perch: what it says is what you know about it.
label scl_dust:
    $ scl.dusted_day = vn_clock.day
    $ vn_enter(bg="scl_quarters", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_dust")
    if scl.tier <= 1:
        "You dust the perch. Stone, copper, jade, the folded blanket. Nobody has sat on it. Nobody lets a sleeve brush it."
        "You don't ask what it's for. You fold the blanket back exactly how it was."
    elif scl.tier == 2:
        "You dust the perch. A scribe passing with a stack of dockets glances at it, then at you."
        scl_other "\"Contract perch. Every other lord's is occupied.\""
        "He doesn't stop walking."
    elif scl.tier == 3:
        "You dust the perch and think of Tie Shan's voice across the terrace. {i}Eleven years, fourth sister.{/i}"
        "{i}Noted.{/i}"
        "You fold the blanket very carefully."
    else:
        "You dust the perch. Somewhere on the roll there's a line for it, and the line is blank."
        "You dust it anyway. Harder than it needs."
    $ vn_pass(15)
    jump scl_hub

## The day beat: one short, optional beat on a rung's day; the lord who passes demonstrates the
## posture line. Once per rung.
label scl_day:
    $ scl.beat_tier = scl.tier
    $ _t = max(1, min(5, scl.tier))
    if scl.day_kind == "vents":
        $ scl.fit = "nude"
        $ vn_enter(bg="scl_vents", pc="stubborn", pc_tag="scl_pc", cast=[("scl_ahning", "grin")], cg=None)
        if _t == 1:
            "The vents. Ah-Ning, waist-deep, filthy and cheerful: who's sleeping with which overseer, which general can't hold his wine, what the fox lord said at court and to whom."
            scl_ahning "\"And the Lady. First night, was it? Mouth?\""
            show scl_pc flushed
            "She slides a look at you. You go red to the ears."
            scl_ahning "\"Thought so. She always starts with the mouth. Breathe through your nose, that's my advice. You'll thank me.\""
            "You keep ducking under. You stay down longer every time. It feels right down there."
        elif _t == 2:
            "Ah-Ning catches your wrist in the steam and turns it. Your skin shimmers, little rainbows running up your arm."
            scl_ahning "\"Soft as silk. That's how it st—\""
            show scl_ahning quiet
            "She stops. Passes you the soap. Then, because she can't help herself:"
            show scl_ahning grin
            scl_ahning "\"Walking a bit funny this morning, aren't we?\""
            scl_you "\"I'm walking fine.\""
            scl_ahning "\"You're walking like someone who got {i}very{/i} thoroughly filed.\""
            "She cackles. Half the pool cackles with her."
        elif _t == 3:
            vn_sfx "{i}Smack.{/i}"
            scl_ahning "\"Look at {i}that{/i}. The Lady's feeding you well.\""
            "Ah-Ning slaps your ass under the water."
            scl_you "\"Ah-{i}Ning{/i}—\""
            scl_ahning "\"What? I'm admiring. Everyone in the gallery heard you last night, by the way. 'Lady, Lady, don't you {i}dare{/i} stop.' Very inspiring. Half the laundry had to go and lie down.\""
            "She does your voice, high and breathy."
            show scl_ahning quiet
            "Then her eyes slide to the pearls on your hip and she goes quiet for the length of a breath."
        elif _t == 4:
            scl_ahning "\"Red looks better on someone who doesn't flinch.\""
            "She flicks water at your tails. You sink lower. Your tits float. She laughs until she coughs."
            scl_ahning "\"Does she do that thing with the tail? Where it goes round your thigh and pulls your legs open? The overseers say she does that.\""
            show scl_pc flushed
            "You go so red you match your hair."
            scl_ahning "\"She does. Oh, she {i}does{/i}.\""
        else:
            "Ah-Ning washes your back for you, careful round the base of your tail. Her cloth slips once, right over the root of it, and you yelp and nearly come off the bench."
            scl_ahning "\"Sensitive. Noted.\""
            show scl_ahning quiet
            "Her impression of the Lady is perfect. Then she doesn't make a single joke for the rest of the bath. That's how you know."
        $ scl.fit = "robe"
    elif scl.day_kind == "court":
        $ vn_enter(bg="scl_terrace", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_court_docket")
        if _t == 3:
            "You hold the docket case at court. Nine lords on the terrace, far off, huge, smoking and glittering. Merit read out loud, like a tax roll."
            show scl_tieshan booming at vn_cast_slot
            scl_tieshan "\"Eleven years, fourth sister! It's not a criticism, it's an {i}accounting{/i} problem!\""
            "Tie Shan, the boar lord, booms it across the stone."
            hide scl_tieshan
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
            "She doesn't look at you. She very carefully doesn't look at you."
        elif _t == 4:
            "The docket case on your hip, your twin tails down your back. Tie Shan again:"
            hide scl_longqi
            show scl_tieshan booming at vn_cast_slot
            scl_tieshan "\"Eleven years, fourth sister.\""
            hide scl_tieshan
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
            "A scribe's eyes slide from the blank line on the roll to you. And back."
        else:
            "You hold the case with your tail tucked tight against your leg."
            hide scl_longqi
            show scl_tieshan booming at vn_cast_slot
            scl_tieshan "\"Eleven years.\""
            hide scl_tieshan
            show scl_longqi calm at vn_cast_slot
            scl_longqi "\"Noted.\""
            show scl_boyan delighted at vn_cast_slot
            "Across the terrace, Bo Yan looks straight at you and smiles."
    elif scl.day_kind == "letters":
        $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_letters")
        "The drawer by your bedding roll is full of them. Letters home."
        "Every one stops in the same place: the sentence where you have to say what you're becoming as if it's good news."
        "{i}Dear Mother. I am fed and housed and{/i}—"
        "You stop. It goes in the drawer with the others."
    else:
        $ vn_enter(bg="scl_galleries", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
        if _t == 1:
            "Dockets to Registry Two. Linen the size of sails. Trays up stairs cut for legs twice as long as yours."
            show cg scl_boards onlayer cgl
            "On the gallery wall there's a board of merit accounts and a board of household posts. They don't share a column."
        elif _t == 2:
            "Dockets, linen, ink. Your hands slide on the tray handles: the calluses are gone, and your skin catches the light in little rainbows when you turn your wrist."
            "A scribe watches your wrist instead of his docket."
        elif _t == 3:
            "Dockets to the registry. Every time you bend, your robe drags over the pearls at your hip and you have to stop and breathe through it."
            "Your ass fills your trousers out now. A steward's eyes follow it all the way down the gallery."
        elif _t == 4:
            "You carry her dockets with your twin tails swinging, red as a warning, the horns throbbing warm at your temples."
            "Nobody could mistake whose you are. The scribes stop writing when you pass."
        else:
            "Nothing fits. Your robe gapes over your tits and strains over your hips, and your tail drags the hem up behind you."
            show cg scl_registry onlayer cgl
            "Registry Two goes silent when you walk in with the dockets. A scribe drops his brush. When you bend to pick it up for him, the whole back of your robe rides up over your ass, and the silence gets louder."
            "You can smell her on yourself. So can all of them."
        hide cg onlayer cgl
    $ _p = SCL_PASSING[_t]
    $ vn_enter(bg="scl_galleries", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_passing_%d" % _t)
    "[_p[0]]"
    $ renpy.say(None, _p[1][0])
    if len(_p[1]) > 1:
        $ renpy.say(None, _p[1][1])
    $ vn_pass(120)
    jump scl_hub

## The plate warms at dusk: the summons, and the next rung.
label scl_summons:
    $ vn_until(19)
    $ vn_enter(bg="scl_quarters_night", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_plate_warm")
    "Her lamp's still lit at the far end. The brush has stopped. She's waiting."
    "The plate goes warm against your sternum. Not hot. Warm, like a palm pressed there."
    "That's the summons. It's how she sends for you.\n{size=-5}{color=#ff8fa3}▸ Go to her{/color}{/size}"
    $ renpy.jump(["", "scl_rung_two", "scl_rung_three", "scl_rung_four", "scl_rung_five", "scl_rung_six"][scl.tier])

## ---- RUNG 2: "Come here, Chuan." The first anal, MANDATORY; non-con, no flip ---------------

label scl_rung_two:
    $ vn_enter(bg="scl_desk", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg="scl_desk_dispatch")
    "She's at her desk when you come in. Dispatches in one hand. Her split skirt has fallen open, and her cock is swelling out from under it, heavy and half-hard, ignored, while she reads."
    scl_longqi "\"Come here, [scl_pc_name].\""
    "Your name. In her mouth. The first time."
    "Your legs go before you've decided to move them. That's the mountain, not you. You plant your heels on the stone and it doesn't help at all."
    show scl_pc protesting
    scl_you "\"Lady, I— the floors are done, the dockets are filed, I can—\""
    hide cg onlayer cgl
    $ vn_enter(bg="scl_pallet", pc="protesting", pc_tag="scl_pc", cast=[("scl_longqi", "intent")], cg=None)
    "She stands. Hands on your shoulders. She walks you back to her pallet and pushes until you sit. Then she strips you, slow, the way she'd open an envelope: robe, undershirt, all of it. You grab at the robe. She takes it out of your fingers like a pen."
    $ scl.fit = "nude"
    "Her palm slides over your chest. Your stomach. Your thighs. Smooth everywhere. She stops where your hair used to be, and smirks."
    scl_longqi "\"Steam must be running hot this season.\""
    vn_sfx "{i}Thwap.{/i}"
    show cg scl_skirt_drop onlayer cgl
    "Her skirt drops. Her cock springs up against her stomach, flushed dark, ridged along the underside, beading at the tip. Thicker than your wrist. You can smell it from here."
    scl_you "\"No— Lady, no, that won't— that's not going {i}anywhere{/i} on me—\""
    show cg scl_knees_back onlayer cgl
    "She pushes you onto your back. Spreads your thighs. Presses your knees back to your chest with one hand, easy, like folding a robe, and holds them there. You push against her palm with everything you've got. It doesn't move. Your little cock twitches against your stomach, smooth and pink, tiny under the shadow of hers."
    "Her tongue drags up your balls. One long wet stripe."
    scl_you "\"{i}Ah{/i}—!\""
    "Without the hair, everything's bare. Every touch lands right on the nerve. She noses the base of your cock and makes a small, satisfied sound, the sound she makes when a column adds up."
    "Her tongue goes lower."
    scl_you "\"Lady— wait— not {i}there{/i}— that's— {i}ahh{/i}—!\""
    show scl_pc flushed
    "Hot and flat and slow, right over your hole. Once. Twice. Then the tip of it, pressing, and your heels kick at the air and your little cock jumps against your stomach and dribbles."
    scl_you "\"Hhh— {i}hhaah{/i}— stop— oh fuck— oh {i}fuck{/i}— stop it, Lady—\""
    "She doesn't hurry. She eats you out the way she reads a docket: every line, all the way down, nothing skipped. By the time she lifts her head you're soaked with her spit and shaking all over, and you haven't stopped saying no once."
    "A finger. Oiled. It slides in, and your whole body clenches round it."
    scl_you "\"Out— take it {i}out{/i}—\""
    scl_longqi "\"Breathe out.\""
    "She waits. You don't. She waits anyway, and your body gives up before you do. A second finger joins it, and she curls them, and something inside you lights up white."
    scl_you "\"{i}AH{/i}— what— what was— {i}don't{/i}— don't do that ag— {i}ahh{/i}—!\"" with vnfx("shake")
    "She does it again. And again. Slow, steady, inhuman, while you squirm on her fingers and say no in a voice that keeps cracking into something else."
    "Then her fingers are gone, and the sound you make is a whine, and you hate it."
    show cg scl_oil onlayer cgl
    "She kneels up between your legs. Oil from a jar, poured down her length, glistening over every ridge. The fat head of her cock settles against your hole, slick and hot and so much bigger than two fingers."
    show scl_pc protesting
    scl_you "\"Lady— Lady, {i}please{/i}, I'm not— I didn't come up the mountain for—\""
    "She doesn't ask. Household isn't asked. Her knee settles on the pallet, and her weight comes down, and the head starts to push."
    scl_longqi "\"Breathe.\"\n{size=-5}{color=#ff8fa3}▸ Breathe{/color}{/size}"
    jump scl_rung_two_sex

label scl_first_after:
    $ scl.tier = max(scl.tier, 2)
    $ scl.rung_day = vn_clock.day
    $ vn_enter(bg="scl_pallet", pc="flushed", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg="scl_first_after")
    "She shoves deep and stays there, your knees pinned by your ears, and comes. It pumps into you, thick and hot and so much it leaks out round her with every flex. She grinds in until the last pulse is gone."
    "You came. With her inside you and nothing on your cock, a thin little splash up your stomach, and your ass is still fluttering round her. She hums."
    scl_longqi "\"Good household. You take me well.\""
    "She doesn't pull out yet. She rolls her hips, slow, once, twice, and every ridge drags over the place her fingers found."
    scl_you "\"{i}Hhnn{/i}— Lady— I said— I {i}said{/i}— {i}ahh{/i}—\""
    scl_longqi "\"Noted. Feel it.\""
    "You feel it. All of it. Her, still thick inside you. Her cum, hot and heavy, packed in deep. Your hole stretched wide round her root, so full it's stupid. Your cock twitching against your stomach in a puddle of its own."
    scl_you "\"Ahh— {i}ahh{/i}— so full— Lady, I'm so {i}full{/i}— {i}again{/i}— no— {i}yes{/i}— {i}ahh{/i}—\""
    scl_longqi "\"Yes.\""
    "She agrees. She pulls out slow. Ridge. Ridge. Ridge. Your hole flutters after every one, chasing her. Then the head pops free and it runs out of you, hot, down onto her pallet, and you moan at that too."
    show cg scl_palm_knot onlayer cgl
    "She wipes you down with the edge of your own robe. Businesslike. Thorough. Then she presses her palm flat on your stomach, just under your navel."
    "You feel it there. Under her hand. A knot of heat that isn't going anywhere. Heavy. Foreign. It doesn't melt into you the way it should."
    "You put your own hand over hers without meaning to."
    scl_you "\"Ahh— Lady— what is—\""
    "She doesn't answer. She bends and licks a stripe up your stomach through the mess you made, slow, and you shiver all the way down to your toes."
    scl_longqi "\"Tidy yourself.\""
    hide cg onlayer cgl
    "She's already reaching for the next dispatch.\n{size=-5}{color=#ff8fa3}▸ Back to your bedding roll{/color}{/size}"
    call vn_night(6)
    jump scl_rung_two_morning

## Row 2 lands: the sheen, the calluses gone, puffy nipples, fangs and gold eyes. A lazy handjob
## while she reads a dispatch: she holds your hand on her until it keeps going by itself.
label scl_rung_two_morning:
    $ scl.fit = "robe"
    $ vn_enter(bg="scl_desk", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "Dawn. You're dusting her outer desk when your sleeve slides back, and the lamp catches your arm."
    $ scl_body(2)
    show cg scl_shimmer onlayer cgl
    "{color=#ff5fb8}It {i}shimmers{/i}.{/color}"
    "{color=#ff5fb8}Little rainbows run up the bone when you turn your wrist. You press your thumb into your palm. The calluses are gone. Years of hoe handles and baskets and frost, polished out overnight.{/color}"
    "{color=#ff5fb8}Your nipples rub your shirt and you gasp. You pull the cloth out and look. Puffy. Swollen. Two soft pink cones that weren't there yesterday.{/color}"
    "{color=#ff5fb8}You pinch one. Just to check.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Nnh{/i}— oh— {i}oh{/i}—\""
    "{color=#ff5fb8}Your knees knock the desk. Your cock's stiff in your trousers in a heartbeat. Your waist dips in where it never did. Your trousers sit tight across your ass, round where it was flat, and your thighs slide smooth against each other when you walk. You grab a handful of your own ass and squeak out loud.{/color}"
    "{color=#ff5fb8}Hair tickles your jaw when you turn your head. Longer again.{/color}"
    "{color=#ff5fb8}And the galleries are bright. They were never lit. You just {i}see{/i} now. Your tongue finds two new points in your mouth. Fangs. Small and sharp and yours. You run your tongue over them and shiver all the way down to your cock.{/color}"
    hide cg onlayer cgl
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Prettier every night.\""
    "Long Qi says it from the bedding, not opening her eyes. Then:"
    scl_longqi "\"Come here.\""
    show cg scl_hand_held onlayer cgl
    "You come. The mountain brings your feet. She doesn't sit up. She takes your wrist and puts your hand on her cock, morning-hard under the silk, and holds it there, and goes back to reading the dispatch in her other hand."
    show scl_pc protesting
    scl_you "\"Lady— I've got the outer desk to— Lady, I don't— {i}let go{/i}—\""
    "She lets go. Your hand stays where it is."
    show cg scl_handjob onlayer cgl
    "You stroke her. Both hands. Up, slow, your new soft palms gliding over every ridge, down to the root. {i}Shlk. Shlk.{/i} She turns a page. You stroke faster, and her breath changes, and you feel stupidly proud of that."
    "Your wrist twists at the head on every upstroke. You never learned that twist. Your hands just know it."
    show scl_pc flushed
    scl_you "\"Mmh— Lady— is this—\""
    scl_longqi "\"Good.\""
    "She turns another page. She comes over your hands and wrists, hot and thick, without looking up from the dispatch. You lick your fingers clean before you've decided to. She notices that. Her tail flicks."
    scl_you "\"{i}Hah{/i}— everything's so {i}loud{/i} this morning—\""
    "{color=#ff5fb8}Her taste on your fingers makes your whole mouth fizz. Then you sit down on her stool, and your ass, still full of last night, hums so hard you squeak.{/color}"
    hide cg onlayer cgl
    hide scl_longqi
    $ vn_enter(bg="scl_galleries", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_contract_beast")
    "In the corridor, Tie Shan's contract beast comes the other way: a huge woman, boar-tusked and broad-hipped, wrapped in fur. She stops. She looks you over, brow to belly, slow."
    "Then she grunts. Short. Approving. And walks on."
    hide cg onlayer cgl
    scl_you "\"The water up here is strange.\""
    "You tell nobody. Your voice is lighter than it was.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ vn_pass(60)
    jump scl_hub

## The morning of rung 3's day: scale-pearls in rows along the hips and spine; you pick one and
## bleed, once.
label scl_pearls:
    $ scl.pearls_seen = True
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_vents", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "The vents. You slide in, and your hip catches on something."
    show cg scl_pearls onlayer cgl
    "{color=#ff5fb8}A lump. Hard. Smooth. Under the skin, over the bone. Gold-white when you twist to look.{/color}"
    "{color=#ff5fb8}Then another. And another. A row of them along your hip and up beside your spine. Little hard pearls, half out of the skin.{/color}"
    "You dig your nail under one."
    show scl_pc protesting
    scl_you "\"{i}Ah{/i}—!\""
    show scl_pc flushed
    "It bleeds. Pink curls through the water. And it feels {i}good{/i}, a hot bright jolt like a pinched nipple, and then something else, something that shoots straight down your spine and into your cock."
    scl_you "\"{i}Ohh{/i}— oh, that's— {i}ohh{/i}—\""
    hide cg onlayer cgl
    show scl_ahning grin at vn_cast_slot
    scl_ahning "\"If you're going to grow scales, do it where we can watch.\""
    show scl_ahning quiet
    "Ah-Ning calls it across the pool. Then she sees the blood."
    scl_ahning "\"Don't poke at it, idiot. You'll make it worse.\""
    $ scl.fit = "robe"
    "You clamp your palm over it and keep your back to the wall all day.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ vn_pass(60)
    jump scl_hub

## ---- RUNG 3: the pearls. Non-con, then it turns: "Don't— don't stop filing me—!" -----------

label scl_rung_three:
    $ vn_enter(bg="scl_cushions", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg=None)
    "You go up with your robe pulled tight and your hand over your hip, where the pearl you dug at this morning is still throbbing."
    "She's sprawled on her cushions. Robe parted. One gold-dusted thigh bare, and the root of her cock lying heavy against it."
    scl_longqi "\"Strip.\""
    "You don't. You stand there with your hand clamped over your hip."
    $ scl.fit = "nude"
    show cg scl_tail_belt onlayer cgl
    "Her tail does it for you. It hooks the belt of your robe and pulls, and the robe slides off your shoulders onto the stone. Your hands hover over your hip."
    scl_longqi "\"Come here.\""
    "The tail brings you. Round your waist, unhurried. Her thumb goes straight to the pearl. Right on the one you dug at. She presses."
    show scl_pc protesting
    scl_you "\"{i}Hhh{/i}—!\""
    scl_longqi "\"Explain.\""
    scl_you "\"I slipped. On the stone, I—\""
    show scl_longqi intent
    scl_longqi "\"Don't insult me. You clawed at it.\""
    "Her thumb rolls over the tender edge. Your face burns. She takes both your wrists in one hand and holds them at the small of your back."
    scl_longqi "\"Listen. Among beasts, scale is insignia. You don't pick at it. You don't hide it.\""
    "Her palm flattens along the row."
    scl_longqi "\"You hide for shame, not for pride. Show yourself as I allow.\""
    scl_you "\"Let go of my— Lady, I'm not showing anyone {i}anything{/i}—\""
    "Her grip doesn't change. Her thumb slides up the row, pearl to pearl. When it rolls over the biggest one, the world goes white."
    scl_you "\"{i}AH{/i}—!\"" with vnfx("flash")
    scl_longqi "\"Sensitive. Let's find out how much.\"\n{size=-5}{color=#ff8fa3}▸ She pulls you across her lap{/color}{/size}"
    hide cg onlayer cgl
    jump scl_pearls_lap

label scl_pearls_lap:
    $ vn_enter(bg="scl_cushions", pc="protesting", pc_tag="scl_pc", cast=[("scl_longqi", "intent")], cg="scl_lap")
    "She pulls you face-down across her lap by your wrists. Your knees in the cushions, your ass up, her cock hot and hardening under your stomach. You kick. Her tail wraps both your ankles and that's the end of the kicking."
    scl_you "\"Lady— let me {i}up{/i}— I'll stop picking, I'll stop, just let me—\""
    "Her breath on your nape. Teeth, light. Then her tongue on the top pearl."
    scl_you "\"{i}Hah{/i}— {i}ah{/i}— no— don't—\""
    show cg scl_lick_row onlayer cgl
    "She licks down. Slow. Broad. Pearl. Pearl. Pearl. Each one fires straight down your spine into your cock, and your hips buck against her thigh."
    scl_longqi "\"Don't move.\""
    "You move. You can't not. She licks the next one, then closes her lips over it and {i}sucks{/i}, like it's a nipple."
    show scl_pc flushed
    scl_you "\"{i}AHH{/i}— Lady— {i}Lady{/i}— stop— oh fuck— oh {i}fuck{/i}— that's not {i}fair{/i}—!\""
    "You howl. There's no other word for it. Your little cock drools on her thigh. Her hand slides under and cups it, rolls it between slick fingers, while her mouth works on down the row."
    "Then her fingers find your hole. Still slick from last time. Two fingers, in, easy."
    scl_longqi "\"Still full. Good girl.\""
    show scl_pc protesting
    scl_you "\"I'm not your— {i}hhn{/i}— don't call me—\""
    "It goes through you like the pearl did."
    show cg scl_mirror onlayer cgl
    "She lifts you by the hips and settles you back against her, your back to her chest, your wrists still pinned behind you between your bodies, both of you facing the big bronze mirror. The fat head of her cock nudges your hole."
    scl_you "\"Wait— wait, Lady, not again, not like— {i}this{/i}—\""
    "She lowers you onto it. And you sink."
    scl_you "\"Nnnh— {i}hhaah{/i}— no— so big— it's so {i}big{/i}—\""
    "In the bronze you see yourself. Mouth open. Eyes glazed. Skin shining. A row of gold pearls glinting at your hip. Her cock disappearing into you a ridge at a time."
    "You shut your eyes."
    scl_longqi "\"Look. Look at yourself.\""
    "Her hand at your throat, turning your face to it."
    scl_you "\"I don't {i}want{/i} to look—\""
    scl_longqi "\"Noted. Look.\""
    show cg scl_mirror_fuck onlayer cgl
    "You look. She fucks you slow. Deep. Every stroke grinds her belly over the pearls on your spine. Her claws rake down the row and you see stars."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    show scl_pc flushed
    "\"Ah— {i}ah{/i}— no— {i}ah{/i}—\" One on every stroke. The no's getting shorter. You can hear yourself. You can see yourself, in the bronze, bouncing on her lap with your mouth hanging open and your little cock bobbing stiff."
    scl_you "\"It's the steam— it's the {i}steam{/i}— why is it the steam—\""
    scl_longqi "\"Don't hide. Can't, anyway.\""
    "She says it against your ear. She speeds up. Her hands clamp your hips and drag you down onto her, hard, faster, the ridges hammering the spot inside you, her tail curling up round your thigh and pulling your legs wider so the mirror can see everything. Your pearls blaze hot and sweet where her belly grinds them."
    vn_sfx "{i}Pap-pap-pap-pap.{/i}"
    "And then your hips are moving. Down to meet her. Not because she's pulling. Because you are."
    show cg scl_mirror_turn onlayer cgl
    scl_you "\"Don't— don't stop filing me—!\"" with vnfx("shake")
    "It's out before you can catch it. In the bronze you watch yourself say it. You watch yourself mean it."
    scl_you "\"Fuck— {i}fuck{/i}— it's so {i}deep{/i}— Lady— {i}Lady{/i}— don't stop, don't you {i}dare{/i} stop—!\""
    "She lets go of your wrists. You don't use them to get away. You grab her thighs and ride down onto her."
    scl_you "\"Lady— {i}Lady{/i}— I'm— I'm gonna— just from your {i}cock{/i}—!\""
    scl_longqi "\"Then do.\""
    show scl_pc soft
    "You come untouched. A thin string from your cock onto your own fingers, and the real thing crashing up through your ass, clenching on her so hard she grunts. She fucks you through it without slowing. She watches your face in the bronze the whole time."
    scl_longqi "\"Good girl.\""
    "She slams deep and comes. Hot. Thick. Flooding you. You feel every pulse of it."
    show cg scl_pearls_shine onlayer cgl
    "When she pulls out it runs down your thighs. She scoops it up in her palm and smooths it over the pearls, round and round, until they shine."
    scl_longqi "\"Let the court see it.\""
    "She kisses your spine."
    menu:
        "Her palm on your pearls. Her cock still hard against you."
        "She bends you over again":
            jump scl_pearls_sex
        "She lets you lie in her arms":
            jump scl_pearls_rest

label scl_pearls_after:
    $ vn_enter(bg="scl_cushions", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_pearls_again_end")
    "She comes again, her claws dragging down your pearls, and you scream into the cushions. It's the second load tonight, and you feel all of it, hot, running down the backs of your thighs."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Good girl.\""
    "She says it again, and it lands in your stomach like the knot does."
    "You don't argue. You can't. You lie face-down in her cushions with your ass in the air and her cum leaking out of you and your pearls shining, and you make a small, happy, wrecked noise into the silk.\n{size=-5}{color=#ff8fa3}▸ Lie in her arms{/color}{/size}"
    jump scl_pearls_rest

label scl_pearls_rest:
    $ scl.tier = max(scl.tier, 3)
    $ scl.rung_day = vn_clock.day
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_pearls_rest")
    "She takes every blanket and keeps you anyway. Her tail across your waist. Her palm on your stomach, low, over the knot."
    "It's harder tonight. Heavier. Like a stone that's warm all the way through."
    "She's still half-hard against your ass. Some time after the lamp gutters she slides back into you, slow, without a word, and just stays there, and you fall asleep stuffed full of her with your pearls throbbing against her stomach."
    "For the second night, she doesn't send you away."
    call vn_night(6)
    jump scl_rung_three_morning

## Row 3 lands: a soft swell, the hair to the collar with auburn streaks, the cock smaller. Ah-Ning
## on inner and outer; then Long Qi at her desk: "That is the mechanism and the filing."
label scl_rung_three_morning:
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_vents", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "The vents at dawn. You look down."
    $ scl_body(3)
    show cg scl_swell onlayer cgl
    "{color=#ff5fb8}Your chest. It's not flat. A soft little swell on each side, puffy nipples on top. Barely an A-cup. It barely passes for breasts. It {i}passes{/i}.{/color}"
    "{color=#ff5fb8}You cup them. Both hands. They just fill your palms, soft and warm, and you squeeze.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Ahh{/i}— oh fuck— oh, they're {i}real{/i}—\""
    "{color=#ff5fb8}Your ass has rounded out under the water. Your hips push out wider either side of it. Your thighs are thicker, pressed together. Your lips feel full when you bite them. Your hair's grown to your collar overnight, black, with streaks of auburn through it.{/color}"
    "{color=#ff5fb8}Then you look lower. Your cock's smaller. Shrunk in the night, a little pink thing bobbing in the water. You poke it. It twitches, stiff and tiny, and the jolt goes straight up into the knot.{/color}"
    scl_you "\"Hah— it's {i}shrinking{/i}—\""
    "{color=#ff5fb8}You don't sound upset. You sound breathless. You bite your lip to keep quiet and it goes through you like a lick. The new swell on your chest tingles every time the water moves.{/color}"
    scl_you "\"{i}Ahh{/i}— even {i}biting{/i} feels—\""
    hide cg onlayer cgl
    show scl_pc stubborn
    scl_you "\"Ah-Ning says the mountain does it to everyone.\""
    "You tell the water."
    show scl_ahning quiet at vn_cast_slot
    scl_ahning "\"I said that.\""
    "Ah-Ning agrees, sliding in. She's quiet a moment. Then:"
    scl_ahning "\"You think a contract makes you outer post, don't you.\""
    scl_you "\"It does. Everyone knows. You contract a beast, you go home with standing—\""
    scl_ahning "\"Household is inner post. Comfort. Hands. Heat. A bed close to power.\""
    "She ticks it off on wet fingers."
    scl_ahning "\"Outer posts need a core. A real demon core, in here. Humans haven't got one. Can't grow one. Not on their own.\""
    "She taps your stomach, just under your navel."
    "Not on their own."
    "The knot under her finger throbs."
    "She opens her mouth. She shuts it. She passes you the soap.\n{size=-5}{color=#ff8fa3}▸ Ask Long Qi{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(60)
    jump scl_mechanism

label scl_mechanism:
    $ vn_enter(bg="scl_desk", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg=None)
    "She's at her desk, brush moving, horns gleaming with oil."
    scl_you "\"Permission to speak.\""
    scl_longqi "\"Household requesting clarity. Go on.\""
    "She doesn't look up."
    scl_you "\"After a contract. Does the court enter a human as outer post?\""
    scl_longqi "\"The seal binds through a demon core seated in the dantian. Outer posts must hold a core. A contract that can't be sealed that way is filed for comfort. Inner post.\""
    "Her brush doesn't pause. A line of perfect characters."
    scl_longqi "\"That is the mechanism and the filing.\""
    scl_you "\"And if someone grew one?\""
    scl_longqi "\"The registry would record it. Was there anything else, household?\""
    "Another line. There isn't. There's only the knot in your stomach, warm under your robe, and the way her tail has gone very still."
    "And something hot and ugly climbing up your throat.\n{size=-5}{color=#ff8fa3}▸ Permission to serve, Lady{/color}{/size}"
    jump scl_spite

## The source's spite scene, softened: she corrects, she never sneers. "Spite" is planted here so
## rung 5's "Spite burns out. Want endures." lands.
label scl_spite:
    $ vn_enter(bg="scl_pallet", pc="protesting", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg=None)
    scl_you "\"Permission to serve, Lady.\""
    "It comes out cold enough to frost the air."
    "She looks up from the docket. Gold eyes. A long look."
    scl_longqi "\"As you wish.\""
    "One claw curls."
    $ scl.fit = "nude"
    show cg scl_spite_pin onlayer cgl
    "You strip like you're throwing the clothes at her. She doesn't react. Her robe drops, and her cock's already rising, heavy and ridged, swinging as she stands."
    "She pins you to the bedding with one palm flat on your chest, right on the soft new swell, and your pearls grind into the silk."
    scl_longqi "\"You're angry.\""
    scl_you "\"I'm not.\""
    scl_longqi "\"Then open.\""
    "You glare at her and spread your thighs. Your hole's already wet. It always is now. You hate how fast."
    "She pushes in. Slow. Steady. All the way to the root."
    scl_you "\"Nnh— {i}ahh{/i}— I'm still— I'm still {i}angry{/i}—\""
    scl_longqi "\"Noted. Be angry, then. Louder.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    show cg scl_spite_legs onlayer cgl
    show scl_pc flushed
    "You fight it for a while. You really do. Then your legs are round her waist and your heels are in her back and you're moaning into her shoulder, and the anger's still there but it's a long way down, under everything else."
    "Your hips roll up to meet her, clench on the way out, loosen on the way in. Nobody taught you that. Your ass just knows the rhythm now."
    scl_you "\"Lady— {i}Lady{/i}— harder— {i}harder{/i}— I hate— I don't— {i}ahh{/i}—!\"" with vnfx("shake")
    "She gives you harder. Her ridges hammer the spot inside you until you come on her cock with a wail, your nub spitting a thin mess between your bellies, and she follows you over, deep, flooding you, grinding in until the last pulse."
    hide cg onlayer cgl
    show scl_pc soft
    "Afterwards she stays inside you and brushes the auburn-streaked hair off your face with one claw. She doesn't say a single word about the registry.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(30)
    jump scl_hub

## ---- RUNG 4: red overnight; the black stone pool; non-con that turns fast -----------------

## The morning of rung 4's day: RED OVERNIGHT. Hair blood-red, falling into two tails by itself;
## small breasts; horn-buds, finned ears. The vents excuse dies here, in the mirror.
label scl_red:
    $ scl.red_seen = True
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_black_pool", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    $ scl_body(4)
    show cg scl_red_hand onlayer cgl
    "{color=#ff5fb8}Your scalp tingles. You scratch, and your hand comes away full.{/color}"
    "{color=#ff5fb8}Hair. Heavy and cool and long. {i}Red.{/i} Not auburn streaks any more. Blood red. Dragon red. Her red.{/color}"
    show cg scl_red_bronze onlayer cgl
    "You stumble to the polished bronze by her bathing pool."
    "{color=#ff5fb8}It's fallen into two tails on its own. Parted clean at the crown, like someone combed it while you slept. Two heavy red ropes down over your chest. Her signature, on your head.{/color}"
    "{color=#ff5fb8}Over your temples, under the skin, two hard knots. Horn-buds. You touch one, and a hot rush of pleasure goes through you so sharp your knees fold. Your ears have gone long and swept back, finned like hers.{/color}"
    "{color=#ff5fb8}And under the red, on your chest: tits. Small. Real. A C-cup, round and high, enough to cup, enough to squeeze together. Your nipples stand up dark and puffy in the steam.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Hhn{/i}— {i}ahh{/i}— they grew— they {i}grew{/i} again—\""
    "{color=#ff5fb8}You grab them. Squeeze. They push up soft between your fingers. You twist to look behind you. Your ass is rounder too, high and soft, and it bounces when you turn. You turn again just to watch it.{/color}"
    scl_you "\"{i}Hhh{/i}— {i}everything{/i}—\""
    "{color=#ff5fb8}Your new tits are so tender the steam on them feels like a hand. You turn, and your ass brushes the cool bronze, and you moan so loud it echoes off the pool.{/color}"
    show scl_pc stubborn
    scl_you "\"...Steam didn't do this.\""
    "You tell the bronze."
    show scl_longqi warm at vn_cast_slot
    scl_longqi "\"No.\""
    "Behind you, from the bedding, Long Qi laughs. Low. She gets up. She stands behind you in the bronze, tall and red, and lays her thumbs on your horn-buds."
    scl_longqi "\"Itches the first week. Then it feels like this.\""
    show cg scl_horn_buds onlayer cgl
    "She presses. Circles."
    show scl_pc flushed
    scl_you "\"{i}Hhh{/i}— {i}ahh{/i}— Lady— {i}Lady{/i}— what are you— {i}ohh{/i}—\""
    "Pleasure, sharp and bright, so bright your knees buckle and she catches you against her with one arm. She keeps rubbing. Slow circles. Your nipples go hard. Your nub drips. You're grinding your ass back against her thighs without meaning to, panting, and in the bronze your face is a mess."
    scl_longqi "\"Red horns will suit.\""
    "She judges it, and lets go. You sag against her, shaking, wet, nowhere near done."
    hide cg onlayer cgl
    scl_longqi "\"Tonight.\"\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(30)
    jump scl_hub

label scl_rung_four:
    $ vn_enter(bg="scl_black_pool", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg="scl_pool_edge")
    "She's on the edge of her black stone pool. Steam boiling up round her. Her twin tails over her bare shoulders, her tail lashing slow on the wet stone, and her cock already out and thickening in the haze."
    scl_longqi "\"Strip and come here.\""
    show scl_pc protesting
    scl_you "\"Lady, I— can it be the floors tonight? Just the floors?\""
    scl_longqi "\"Strip, and come here.\""
    "She says it again, exactly the same."
    $ scl.fit = "nude"
    hide cg onlayer cgl
    "You do, because your hands are already on your belt. Your red tails slide down over your shoulders. Your new tits bounce when you kneel, and you cover them with both arms."
    show cg scl_tail_wrists onlayer cgl
    "Her tail lifts your wrists off them, one and then the other, and lays them at your sides."
    "She looks at you for a long moment through the steam. Your horn-buds. Your red. Your nipples, already hard. Your nub of a cock, hiding between your thighs."
    "Her cock jerks up off her thigh. That's all the reaction you get. It's enough to make your face burn."
    "She pats her shaft."
    scl_longqi "\"Up.\""
    scl_you "\"Lady?\""
    scl_longqi "\"Let's see those new tits in action.\"\n{size=-5}{color=#ff8fa3}▸ She lifts you onto her knee{/color}{/size}"
    hide cg onlayer cgl
    jump scl_pool

label scl_pool:
    $ vn_enter(bg="scl_black_pool", pc="protesting", pc_tag="scl_pc", cast=[("scl_longqi", "intent")], cg="scl_knee")
    "She doesn't wait for you. She catches you under the arms and lifts you up onto her knee, easy, and looks."
    scl_you "\"Lady— wait— they're {i}new{/i}— they're not for— don't—\""
    show cg scl_nipple_mouth onlayer cgl
    "She bends her head and takes one of your new nipples in her mouth."
    scl_you "\"{i}Ahh{/i}— no— Lady— oh— {i}oh{/i}—!\""
    show scl_pc flushed
    "Hot. Wet. Her tongue flicks it, slow, and then she sucks, hard, and it goes through you like lightning, straight down into your stomach and your nub of a cock. Your hands fly to her horns to shove her off. They grab on instead."
    scl_you "\"Hhh— {i}hhaa{/i}— stop— I didn't know they'd— {i}ahh{/i}— the other one— the other one, {i}please{/i}—\""
    "You hear it come out of your mouth. So does she."
    vn_sfx "{i}Slrp.{/i}"
    "She switches. Her teeth graze. You arch so hard you nearly fall off her knee and her tail catches you round the waist and puts you back."
    "When she lets go, both your nipples are swollen and shining and aching in the steam."
    scl_longqi "\"Now.\""
    show cg scl_titjob onlayer cgl
    "She sets you back on your knees between her thighs. And you're already doing it. Before she says squeeze. Before she says anything. Your hands come up under your new tits and lift them, and hold them open for her, and her cock is hot as an ember between them."
    scl_you "\"{i}Hah{/i}— I— I didn't— {i}ahh{/i}—\""
    scl_longqi "\"No. You did.\""
    "She agrees. You didn't know they'd feel like that. Every brush of her shaft over the soft skin goes straight to your nipples."
    scl_longqi "\"Squeeze them together.\""
    "You already are. Tight. Your hands trembling. You start to move, up, down, her pre-cum running down into your cleavage and making it slick."
    vn_sfx "{i}Shlk. Shlk. Shlk.{/i}"
    "Your tits start rolling round her in a slow wave, left, right, left. Nobody showed you that. Your body just does it."
    scl_you "\"Mmh— {i}ah{/i}— Lady, they're so— they're so {i}sensitive{/i}—\""
    show cg scl_rim_reflection onlayer cgl
    scl_longqi "\"Look.\""
    "Her fingers wind into your hair and tip your head down. The wet black rim of the pool is a mirror. You see yourself doubled in it. Red twin tails. Horn-buds at your temples. Puffy nipples, flushed tits, and her fat red cock sliding up and down between breasts that were a flat chest last week."
    scl_longqi "\"There's my household. Dragon's colour. Proper badge.\""
    "Low and rough."
    scl_you "\"{i}Ahh{/i}—\""
    "She starts fucking up into your cleavage. Her tail wraps your waist and pulls you tighter onto her. The head of her cock slaps your collarbone on every thrust, smearing pre up your throat."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    scl_longqi "\"Harder. Hold them.\""
    scl_you "\"Yes— {i}yes{/i}— Lady, use them, use my tits, please—\""
    "She swells in your cleavage. Her cock jumps."
    scl_longqi "\"Mine.\""
    show cg scl_titjob_end onlayer cgl
    "She growls it, and comes. It splashes up your throat, your chin, your lips, thick and hot, rope after rope, painting your new tits white." with vnfx("shake")
    show scl_pc soft
    "You open your mouth without thinking and the next rope lands on your tongue. You swallow it. You lean down and lick the head of her cock clean while it's still pulsing, and she groans, the first real groan you've ever got out of her."
    "She drags her cock through the mess, slow, spreading it over your nipples."
    "Your own little cock drips onto the black stone. Nobody looks at it. Not even you."
    scl_longqi "\"See the mark, household? No refiling it.\""
    "Her thumb smears her cum over the swell of your breast. In the stone your reflection is red and wet and painted."
    menu:
        "Her cock still between your tits. The steam on your wet skin."
        "Hold them up for her again":
            jump scl_pool_sex
        "Let her pull you into her lap":
            jump scl_pool_rest

label scl_pool_after:
    $ vn_enter(bg="scl_black_pool", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_pool_again_end")
    "She comes across your tits again, groaning, and rubs it in with her palm, round and round, until your nipples are slick with it and you're whimpering."
    scl_longqi "\"Proper badge.\"\n{size=-5}{color=#ff8fa3}▸ Sit in her lap{/color}{/size}"
    jump scl_pool_rest

label scl_pool_rest:
    $ scl.tier = max(scl.tier, 4)
    $ scl.rung_day = vn_clock.day
    $ vn_enter(bg="scl_black_pool", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_pool_lap")
    "She pulls you into her lap, sticky and dripping, her cock pressed up between your tits like a signature. Her arms go round you. You collapse against her in the steam."
    "She bends her head and takes your nipple in her mouth again, lazily, licking her own cum off it. You whimper and squirm and she holds you still with her tail and does the other one too."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Mine.\""
    scl_you "\"Yours.\""
    "You hear yourself say it, and you don't even flinch."
    call vn_night(6)
    jump scl_rung_four_morning

## Rung 4's morning: the cock almost nothing, weighed in her palm. "Men? Is it men you serve for at
## night?" Then knees and elbows; it opens with a protest and turns at once.
label scl_rung_four_morning:
    $ vn_enter(bg="scl_quarters", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "You wake under a fall of red hair, hers and yours, tangled together."
    "You slide out from under her arm and look down at yourself."
    "{color=#ff5fb8}Your cock is almost nothing. A little pink nub, all but lost between your soft new thighs. Your balls have drawn up tight. You touch it, and a tiny bright shiver runs all the way up into the knot, and you whimper.{/color}"
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"You found it, then.\""
    "She's awake, watching. She hooks a claw behind your neck, draws you to her knee, and slips a hand under your robe. She weighs it in her palm. Hums."
    scl_longqi "\"Even less than I expected. Good.\""
    scl_you "\"I— most men—\""
    show scl_longqi intent
    scl_longqi "\"Men? Is it men you compare yourself to? Is it men you serve for at night?\""
    "One brow goes up. Your knees want to fold. She doesn't let them. She keeps you standing by her knee, junior, unfinished, upright, and you understand that's what she wants."
    scl_you "\"No, Lady.\""
    scl_longqi "\"No. Since you're awake. Face down for me.\""
    show scl_pc protesting
    scl_you "\"Lady, it's barely— I've only just—\""
    $ scl.fit = "nude"
    show cg scl_face_down onlayer cgl
    "Her hand on the back of your neck puts you there. Knees and elbows on the scale-strewn mat. Your red tails pooling on the floor either side of your face. Your ass up. She spits into her palm, and then her fingers are in you, slick and patient, stretching you round last night's cum."
    scl_you "\"{i}Hhh{/i}— {i}ahh{/i}—\""
    scl_longqi "\"Breathe out.\""
    show scl_pc flushed
    "You do. The fat head of her cock replaces her fingers, and she sinks in, slow, ridge after ridge, till her scaled hips are flush against your ass."
    scl_you "\"Ohh— {i}ohh{/i}— so deep— it's so {i}deep{/i} this way—\""
    scl_longqi "\"Feel that? That's where the work happens.\""
    "She rolls her hips. Something inside you lights up."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    "She fucks you slow and heavy. Your little nub swings uselessly under you and drips on the mat. You don't care. You can't care. Everything that feels good has moved, and it's all where her cock is, pounding into you, and up into the knot in your stomach."
    scl_you "\"Lady— {i}Lady{/i}— I'm— from my {i}ass{/i}— I'm gonna—\""
    scl_longqi "\"Then do.\""
    "You come harder than you've ever come in your life. Not from the nub. From her. It shudders up through your ass into your stomach and the knot {i}clenches{/i}, actually clenches, round the heat of her as she fills you." with vnfx("shake")
    hide cg onlayer cgl
    scl_longqi "\"There. Didn't need the old thing anyway. The pleasure's where I want it now.\""
    "She leans down to your ear, still buried in you.\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(60)
    jump scl_hub

## ---- RUNG 5: what the fox says; her door; two days in the kitchens; the terms; the ride -----
## Consensual from here, as signed off: the first time you come to her.

label scl_rung_five:
    $ vn_enter(bg="scl_colonnade", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "The plate's warm. You take the long way up, through the painted colonnade over the audience stairs."
    "The fox is waiting."
    show scl_boyan delighted at vn_cast_slot
    show cg scl_boyan_lounge onlayer cgl
    "Bo Yan lounges on the balustrade like a monument to boredom. In court shape he looks about thirty, which is a joke he's been telling for centuries. White robes open at the throat. Nine silky tails spread over the stone. He watches you come, and his face lights up like you're the best thing that's happened all week."
    scl_boyan "\"Oh, {i}look{/i} at you. Sit. I've come to be entertained.\""
    hide cg onlayer cgl
    "He pats the stone. You sit as far away as the balustrade allows. Your knees are shaking."
    show scl_boyan bored
    scl_boyan "\"You know what she's doing to you? No. Of course not. Dragons only talk in rules. So I'll save you some months. Household is inner: comfort, proximity, no command. Every post with standing is outer, and outer wants a demon core, sat right in the dantian. Humans are born without one. Can't grow one.\""
    "He spreads elegant fingers. A beat."
    scl_boyan "\"Alone.\""
    "The knot in your stomach turns over."
    show scl_boyan delighted
    scl_boyan "\"Every time she fills you, it nests there and sets a little harder. You've noticed you can't come properly any more? The centre's moved. She's been growing a core in you for months. Rather thoroughly, from what the gallery hears.\""
    "He smiles, all teeth."
    show scl_pc soft
    scl_you "\"...She never said.\""
    show scl_boyan bored
    scl_boyan "\"No. Now, the ugly cousin of what she's doing has a name too, and nobody at court will say it to your face, so I will. {i}Plunder cultivation.{/i} It's what this mountain has always done to household who were never going to qualify. Take, and take, and file the rest.\""
    "He lets it sit, then lifts one finger."
    scl_boyan "\"That is not what is happening to you. I'm cruel, but I'm never inaccurate.\""
    show cg scl_fox_palm onlayer cgl
    "He leans in and lays his palm flat on your stomach, right over the knot. Warm. Light. The only hand on this mountain that isn't hers."
    scl_boyan "\"Fire and stone. Nearly done.\""
    hide cg onlayer cgl
    show scl_boyan delighted
    scl_boyan "\"And her perch has been waiting for whoever offers. Eleven years of whoever. Isn't that {i}funny{/i}?\""
    "He takes his hand back, and swirls off down the colonnade, tails and amber, laughing.\n{size=-5}{color=#ff8fa3}▸ Go on to her door{/color}{/size}"
    $ vn_pass(10)
    jump scl_her_door

label scl_her_door:
    $ vn_enter(bg="scl_her_door", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_door_walk")
    "Her door. Dragon script on the threshold. The pull of her through the stone, scale and musk and heat, dragging at your stomach."
    "Your knees don't go."
    "Your hands are shaking so hard you have to make fists. But you're on your feet. You walk past her door without kneeling."
    "And you keep walking. Past the perch, which you dust every day, and which you suddenly understand is waiting for somebody."
    "You don't go in. Not tonight.\n{size=-5}{color=#ff8fa3}▸ Down to the kitchens{/color}{/size}"
    $ vn_pass(20)
    jump scl_kitchens

label scl_kitchens:
    $ vn_enter(bg="scl_kitchens", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "Two days."
    "You scrub pots. You haul water. You keep to the kitchens, where the stone's cold and the work never stops and nobody important ever comes. You walk the long way round the perch. You stop sweeping near it at all."
    "The knot doesn't like it."
    show scl_pc flushed
    "It throbs. Then it nags. Then it's {i}hunger{/i}, low behind your navel, a hunger no rice touches. Every bucket you lift, it clenches. Every time you hear her step on the stone overhead, your hole clenches with it, empty, and your nub of a cock twitches like a ghost."
    $ vn_pass(24 * 60)
    show cg scl_jugs onlayer cgl
    "On the second morning you round a corner with an armful of wine jugs and walk straight into Bo Yan's procession."
    vn_sfx "{i}THUD.{/i}" with vnfx("shake")
    show scl_pc protesting
    "You're down. Both knees. Forehead to the stone. Jugs rolling everywhere. It's never been this bad, not since the first day. Without her filling you, whatever you had just runs out of you."
    "He doesn't stop. You catch a gleam of gold eye going past, and a flick of a smile. {i}See how thin it runs?{/i}\n{size=-5}{color=#ff8fa3}▸ Hide in the storeroom{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(24 * 60)
    jump scl_storeroom

label scl_storeroom:
    $ vn_enter(bg="scl_storeroom", pc="flushed", pc_tag="scl_pc", cast=[], cg=None)
    "Behind the millet sacks. Rice dust and candle wax. You pull your robe open."
    "Your tits heave when you breathe. Your cock's a nub, soft and useless between thighs gone round and heavy. You touch it. Almost nothing. A dull throb that runs straight back to the knot."
    scl_you "\"Nnh— come on— {i}come on{/i}—\""
    show cg scl_storeroom_alone onlayer cgl
    "You pinch a nipple instead. {i}That{/i} fires. You rub your nub and twist your nipple and think about her, her weight on your back, her ridges dragging, her cum flooding you so full it leaks—"
    "You get two fingers in your mouth, wet them, reach back. Push them into your hole. It's not enough. It's nowhere near enough. You fuck yourself on them anyway, face down on the millet sacks, ass up, tailbone throbbing, biting your own arm so the kitchens won't hear."
    scl_you "\"Mmf— {i}mmmf{/i}— not enough— it's not {i}enough{/i}— {i}ahh{/i}— Qi— {i}Qi{/i}—!\""
    "You come with a whimper. A dribble of clear on your thigh. It's over in a heartbeat."
    hide cg onlayer cgl
    "And the hunger's still there. Worse. Gnawing. It wants one thing and it isn't your hand."
    "The knot says it for you, low behind your navel, over and over, in a voice that's yours and isn't:"
    "{i}{color=#ff8fb8}Fill it. Fill it. Fill it.{/color}{/i}"
    "That night, in the kitchens, you borrow a brush and a scrap of paper, and you write.\n{size=-5}{color=#ff8fa3}▸ Write out your terms{/color}{/size}"
    jump scl_terms

## The conditions list: which terms you write is flavour. Each read aloud gets "Continue."
label scl_terms:
    show screen scl_paper
    menu:
        "Conditions. If she's going to do this. If you're going to let her."
        "Your name in the contract" if "name" not in scl.terms:
            $ scl.terms = scl.terms + ["name"]
        "The registry notified" if "registry" not in scl.terms:
            $ scl.terms = scl.terms + ["registry"]
        "The right to refuse display" if "display" not in scl.terms:
            $ scl.terms = scl.terms + ["display"]
        "Space, sometimes" if "space" not in scl.terms:
            $ scl.terms = scl.terms + ["space"]
        "Fold it up and go to her" if scl.terms:
            hide screen scl_paper
            $ vn_pass(30)
            jump scl_asking
    jump scl_terms

label scl_asking:
    $ scl.fit = "robe"
    $ vn_enter(bg="scl_desk", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg=None)
    vn_sfx "{i}Tap. Tap-tap.{/i}"
    "You knock. One short tap, two quick. Forms are all you've got."
    "Every other night, the plate warmed and she sent for you, or she came down the room and took you where you slept. Nobody sent for you tonight. You came up on your own feet. It's the first time."
    scl_longqi "\"Enter.\""
    "She's at her desk. She doesn't look up."
    scl_longqi "\"Household. You're late.\""
    scl_you "\"I have conditions.\""
    "Your voice cracks on it. The paper's damp in your fist."
    scl_longqi "\"State them.\""
    "She sets the brush down."
    if "name" in scl.terms:
        scl_you "\"My name in the contract. Mine. Not just household.\""
        scl_longqi "\"Continue.\""
    if "registry" in scl.terms:
        scl_you "\"The registry notified. My village's line, at least. They paid for me.\""
        scl_longqi "\"Continue.\""
    if "display" in scl.terms:
        scl_you "\"The right to refuse display. Like the other contract beasts.\""
        scl_longqi "\"Continue.\""
    if "space" in scl.terms:
        scl_you "\"And space. Sometimes. Some days I'm just me.\""
        scl_longqi "\"Continue.\""
    "You wanted a fight. Something to kick against. There's only that dark, patient gold."
    scl_you "\"I want it to be— I want a say. I want it to be {i}mutual{/i}.\""
    show scl_longqi intent
    scl_longqi "\"Mutual. Name it.\""
    "Her head tilts. The knot in your stomach roars. The paper crumples."
    show scl_pc flushed
    scl_you "\"I want— I don't want to want this. And I do. I {i}do{/i}. Please. I can't— just— please—\""
    show cg scl_robe_falls onlayer cgl
    "She stands. All the way up, to her full height, the air humming. She files the paper in her desk without reading it again."
    "Then her robe falls."
    "Scales blazing red-gold at her hips. Heavy breasts. And her cock, rising, ridged and dark, swinging heavy as she walks round the desk. The smell of her hits you and your knees nearly go, and your mouth floods, and the knot in your stomach clenches so hard you whimper out loud."
    scl_longqi "\"Two days. You smell starving.\""
    scl_you "\"I {i}am{/i}— Lady, I am, I'm so—\""
    hide cg onlayer cgl
    "She takes your wrist and walks you to the bedding."
    scl_longqi "\"Spite burns out. Want endures. File that.\"\n{size=-5}{color=#ff8fa3}▸ Climb on top of her{/color}{/size}"
    jump scl_ride

label scl_ride:
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_quarters_night", pc="flushed", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_ride_watch")
    "She lies back in the silk and doesn't move."
    "Her cock stands up off her stomach, ridged and red and leaking. Her hands rest on the bedding. Her tail lies still. She just watches you."
    scl_longqi "\"Show me how much you want it.\""
    "You straddle her. Your thighs, so soft now, spread wide over her hips. Your tits swing. Your tailbone tingles."
    "Her cock lies up between your cheeks, hot, throbbing against your hole without going in. You rock on it. Just rock. The ridges drag up and down the crack of your ass and you whimper every time one catches your rim."
    scl_you "\"Hhh— {i}Lady{/i}— I—\""
    "She just watches. Her hands don't move from the bedding."
    show cg scl_ride_kiss onlayer cgl
    "The knot in your stomach is screaming. Two days of nothing. You lean down and kiss her, clumsy, desperate, your tits squashed on her chest, and she lets you, and that's somehow worse."
    "You sit back up. You reach back, take her cock in both hands, slick it through the wet she always leaves you with, and fit the fat head to your hole."
    scl_longqi "\"Ask me properly.\""
    scl_you "\"Please— please— {i}Qi{/i}— please let me—\""
    "It's out before you can stop it. Her name. Not Lady. Her name, to her face, for the first time. Her eyes go dark."
    $ scl.qi = True
    menu:
        scl_longqi "\"Go on, then.\""
        "Sink down on her":
            jump scl_ride_sex
        "Grind on the head first":
            pass
    show cg scl_ride_grind onlayer cgl
    "You rock on the head of her, teasing your own rim with it, back and forth, until you're whining and she's breathing hard through her nose."
    "The tip pushes in. Just the tip. You lift off it. It pops free and you gasp. You sink back onto it. Pop. Gasp. Again. Again. Your thighs are trembling. Her pre-cum is running down the inside of your leg."
    scl_you "\"Hhh— {i}hhaa{/i}— I can't— I can't stand it—\""
    scl_longqi "\"You can. You're doing it.\""
    scl_you "\"{i}Qi{/i}—\""
    scl_longqi "\"Your pace. Yours.\""
    "Her hands stay on the bedding.\n{size=-5}{color=#ff8fa3}▸ Sink down on her{/color}{/size}"
    jump scl_ride_sex

label scl_ride_after:
    $ scl.tier = max(scl.tier, 5)
    $ scl.rung_day = vn_clock.day
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_ride_end")
    "She finally grabs your hips and slams you down onto her, all the way, and comes. It floods you, so hot and so much, and the knot in your stomach {i}drinks{/i} it."
    scl_you "\"{i}Ahh{/i}— Qi— {i}Qi{/i}— full— I'm so {i}full{/i}—\""
    "You came on her. Your nub of a cock spat a little clear onto her stomach, and your ass clenched round her so hard you saw white, and you're still twitching."
    "You don't stop. You can't. You keep grinding on her, slow, sloppy, her cum squelching out round her root every time you lift, and she lets you, her hands finally on your hips, not pulling, just holding."
    scl_longqi "\"Good girl. Your pace.\""
    "Very low."
    scl_you "\"Qi— Qi— {i}mmh{/i}— Qi—\""
    "It's the only word you've got left. You say it until it doesn't sound like a word."
    "You collapse onto her chest. She doesn't pull out. Her arms close round you, and her tail comes up over your hips."
    "For the first time in two days, the hunger's quiet.\n{size=-5}{color=#ff8fa3}▸ Stay on her{/color}{/size}"
    call vn_night(5)
    jump scl_tail

## Rung 5's dawn: the tail splits out at the base of the spine; her tail coils round it.
label scl_tail:
    $ vn_enter(bg="scl_quarters", pc="flushed", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg=None)
    "Just before sunrise, it starts."
    $ scl_body(5)
    show cg scl_tail_split onlayer cgl
    "{color=#ff5fb8}A hot, sweet itch at the base of your spine, under the pearls. You curl up on your side, moaning.{/color}"
    scl_longqi "\"Hush. Let it through.\""
    "She catches your face in both hands."
    scl_you "\"{i}Hhhh{/i}— {i}ahh{/i}—!\""
    "{color=#ff5fb8}The skin at your tailbone stretches, tingling, and something pushes out, hot, heavy, scales running liquid down its length and hardening as they go. It's huge, and it feels {i}amazing{/i}, like being filled from the inside out, and her hands are stroking your spine and her breath is in your hair.{/color}"
    "{color=#ff5fb8}Then it's there. Thick. Heavy. Alive from root to tip.{/color}"
    show cg scl_tails_coil onlayer cgl
    "You flick it. It {i}moves{/i}."
    "Long Qi laughs, delighted, and coils her tail round yours, tight. Then her hand finds it. Strokes the underside, root to tip, slow."
    scl_you "\"{i}AH{/i}— Qi— {i}Qi{/i}— that's— oh fuck— that's so—\""
    "It's like the pearls, only more. So much better. Every scale on the underside is a nerve. She strokes it again and your hips buck and your hole clenches on the last of her cum, and she does it again, and again, her thumb pressing into the soft root, until you're moaning into her shoulder and coming, just from that, just from her hand on your new tail." with vnfx("shake")
    scl_longqi "\"Good girl. Stay. Let it settle.\""
    hide cg onlayer cgl
    "Then the rest of it catches up with you."
    "{color=#ff5fb8}Your tits are heavy against her ribs. Heavier than last night. A full DD-cup, spilling soft over her arm when you roll. You grab one and squeeze and it overflows your hand.{/color}"
    scl_you "\"{i}Ohh{/i}— Qi— they're {i}bigger{/i}— feel— {i}feel{/i}—\""
    "{color=#ff5fb8}She feels. She weighs one in her claws, and hums. Your hips flare wide. Your ass has spread round and heavy, pressing back into her lap. Your thighs press together, plump and soft. Red hair spills down past your shoulder blades.{/color}"
    "{color=#ff5fb8}When you say her name, it comes out nearly a woman's voice. Your cock is a nub, smaller again, lost between your thighs, and you don't look for it.{/color}"
    "Your hips are still rolling against her, slow, the way you rode her last night. You never learned to ride. You just can now."
    show scl_pc soft
    "You're grinning into her collarbone like an idiot."
    scl_you "\"{i}Mmh{/i}— Qi— I can feel {i}everything{/i}—\""
    "{color=#ff5fb8}And every bit of you is turned up. Her breath on your mouth is a kiss. Her arm across your tits makes your nipples sing. Her lap under your ass makes you squirm.{/color}\n{size=-5}{color=#ff8fa3}▸ Next{/color}{/size}"
    $ scl.fit = "robe"
    $ vn_pass(120)
    jump scl_hub

## ---- RUNG 6: two valleys over; the core; the terrace; not yet ------------------------------

label scl_rung_six:
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_spoon")
    "She doesn't want you on your knees tonight."
    "She pulls you down into the silk on your side and fits herself behind you, her front to your back, her tail heavy over your new one. Her cock slides between your thighs and finds your hole, slick and easy now, and pushes in slow."
    scl_you "\"{i}Mmh{/i}— Qi—\""
    "No hurry. No rhythm to speak of. Just her, deep, rocking, her palm flat on your stomach over the knot, the way she always holds it."
    "Her other hand finds your tits. Squeezes one, then the other, rolls a nipple slow between finger and thumb. Her mouth is on the back of your neck. Her hips never stop: in, and in, and in, the ridges dragging slow through you, deep enough that you feel each one arrive."
    scl_you "\"So deep— it's so {i}deep{/i} like this— Qi, I can feel all of you—\""
    scl_longqi "\"Good girl.\""
    "Your tail curls back round her thigh by itself and pulls her in tighter. She laughs into your hair."
    "It's burning under her hand tonight. Not hungry. {i}Hot{/i}."
    scl_you "\"Nnh— it's— Qi, it's—\""
    scl_longqi "\"I know. Let it.\""
    "She says it into your hair. She comes in you without hurrying, and stays there, and the heat in your stomach takes it and closes round it like a fist."
    "You fall asleep with her inside you and the knot blazing like a coal."
    call vn_night(6)
    jump scl_core

## The core sets overnight and the cock is gone, found by hand at waking.
label scl_core:
    $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[], cg=None)
    "You wake up warm all the way through."
    $ scl_body(6)
    show cg scl_core onlayer cgl
    "{color=#ff5fb8}The knot's gone. In its place, low behind your navel, a heavy sphere, smooth and steady, beating like a second heart. Not hers. {i}Yours.{/i} Qi moves through you like breath for the first time in your life.{/color}"
    "{color=#ff5fb8}You stretch. Your body's wrong. No. Your body's {i}different{/i}. Heavy tits roll against your arm, bigger again: F-cups, spilling off your chest when you turn on your side. You heft one in your palm and moan out loud at the weight of it. Your waist tucks in to nothing. Your hips spread the bedding. Your ass is a soft, heavy cushion under you.{/color}"
    "You reach down to scratch."
    "{color=#ff5fb8}And there's nothing there.{/color}"
    "{color=#ff5fb8}Your hand slides over smooth skin, over soft folds, slick and swollen. No nub. Nothing at all. Gone. You pat round for it anyway, giddy, and find only folds, wet and puffy and {i}yours{/i}. Your fingers part the lips by themselves and slip into wet heat, and the jolt goes straight up into the new core.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Ah{/i}—!\""
    "{color=#ff5fb8}You're wet. You're {i}so{/i} wet. Your pussy clenches round your fingertip like it wants more. It's the most sensitive thing you've ever owned. Your own fingertip on it makes your whole body jolt, and your mouth goes hot and wet just thinking about hers.{/color}"
    scl_you "\"{i}Ahh{/i}— it's so {i}much{/i}—\""
    hide cg onlayer cgl
    show scl_longqi warm at vn_cast_slot
    scl_longqi "\"There. It's set.\""
    "Long Qi, behind you. She's been awake. Watching. Her hand slides over your hip, down your stomach, and covers yours. She presses your fingers deeper."
    scl_you "\"{i}Hhh{/i}— Qi—\""
    scl_longqi "\"Feel it properly.\""
    "Her own finger joins yours. Slides along the lips, slow, up to the hard little knot at the top, and circles it once."
    scl_you "\"{i}AH{/i}— {i}ahh{/i}— what— oh my— {i}Qi{/i}—!\""
    "Your hips jerk. Your thighs clamp on both your hands. She does it again, unhurried, and again, her mouth on the back of your neck, until you're panting and rocking into her palm and wet all the way down your thighs."
    "Then she stops, and takes her hand away, and you actually wail."
    scl_longqi "\"Later. Not like this. Not by accident.\"\n{size=-5}{color=#ff8fa3}▸ Turn round to her{/color}{/size}"
    jump scl_two_valleys

## At dawn she tells you. Her vow narrows to the seal alone: "I will not take your name."
label scl_two_valleys:
    $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_dawn_talk")
    "She's propped on an elbow, looking at you in the grey light. Not a dragon's look. Something plainer."
    scl_longqi "\"Do you know Huai Pass?\""
    scl_you "\"...Two valleys over. From mine. My father sent timber there.\""
    scl_longqi "\"That's the one. I was born in a hut by the pass, so close you could see the trade mules from the window. Same rocks as yours. Same thin soil.\""
    scl_longqi "\"A census came through in a thin year. The pass was in deficit; the quota had to balance. A form went out to every house with a girl of age, and the court sealed whichever one climbed first. I was fastest. I was twenty-two. Eleven years ago.\""
    "Her mouth twists. So she's thirty-three. You'd never once thought of her as having an age."
    scl_longqi "\"I had a valley name, and the roll has no column for it.\""
    scl_you "\"They sealed you.\""
    scl_longqi "\"In an afternoon. I woke up in true form with the seal shut round me and nine lords watching a vacancy get filled. Nobody asked. By the time I understood there was a question, it had been answered.\""
    "Her tail moves on the silk."
    scl_longqi "\"I serve, and I serve well. But nobody can ever say I asked.\""
    show cg scl_perch_look onlayer cgl
    "She looks down the room at the perch."
    scl_longqi "\"The court gave me household. I took household. Your mouth, the first night, before you were awake. Your knees on my pallet. Every night after. I take what the court gives me.\""
    "She says it the way she reads a docket, line by line, nothing skipped."
    hide cg onlayer cgl
    "Her claw touches your mouth."
    scl_longqi "\"I will not take your name. Not from you, [scl_full_name].\""
    "Your whole name. In full. In her mouth.\n{size=-5}{color=#ff8fa3}▸ Kiss your way down her{/color}{/size}"
    jump scl_given

## After her story: something that's yours to give. Your mouth on her, your pace.
label scl_given:
    $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_given")
    "You kiss her. Her mouth. Her throat. The red scales at her collarbone. You go down her body slowly, because you can, because she's letting you."
    "Her cock is already hard against her stomach when you get there. Ridged. Hot. Leaking."
    "You don't wait to be told. You take her in your mouth."
    scl_longqi "\"{i}Mm{/i}.\""
    "Very quietly. Her hand settles in your red hair and doesn't push."
    "It's yours. The pace is yours. You go slow, so slow, ridge by ridge, your tongue flat under her, your lips stretched round her, your new tits pressed against her thighs. {i}Slrp. Slrp.{/i} You pull off and lick the whole length of her, root to tip, and look up at her while you do it."
    "She's watching you with her lips parted."
    "You take her back in. Deeper. Your throat opens for her on its own, the way the dragon taught it, no gag left in you at all, and you hold her there, and hum, and feel her thighs shake."
    scl_longqi "\"[scl_pc_name].\""
    "She breathes it. It's the first time she's ever sounded anything but steady."
    "You bob faster. Spit everywhere. Your hand round what doesn't fit. Your tail lashing the silk behind you. You moan round her and you don't stop."
    "She comes with a low, rough sound, her claws tightening in your hair, and you swallow every pulse, {i}gulp, gulp, gulp{/i}, and keep sucking her gently through the end of it until she pulls you up by the shoulders and kisses you with the taste of herself still in your mouth."
    scl_you "\"Thank you.\""
    "You don't know what for. You mean all of it."
    scl_longqi "\"Only what's owed.\""
    "She doesn't let go of you for a long time.\n{size=-5}{color=#ff8fa3}▸ Get up{/color}{/size}"
    $ vn_pass(30)
    jump scl_knife

label scl_knife:
    $ scl.fit = "robe"
    $ vn_enter(bg="scl_quarters", pc="protesting", pc_tag="scl_pc", cast=[], cg=None)
    "{color=#ff5fb8}Nothing fits.{/color}"
    "{color=#ff5fb8}Your shirt won't close over your tits. Your trousers won't get past your hips.{/color} You're standing in the middle of her quarters with your tail lashing and your clothes strangling you when Ah-Ning ducks in with a basket."
    show scl_ahning grin at vn_cast_slot
    "She stops dead. Looks at you. Whistles, long and low."
    scl_ahning "\"Well. Morning, princess.\""
    scl_you "\"They don't {i}fit{/i}—\""
    scl_ahning "\"No shit. Arms up. Don't struggle unless you want splinters in your scales.\""
    "A folding knife flicks open."
    vn_sfx "{i}Snap.{/i}"
    $ scl.fit = "nude"
    show cg scl_knife onlayer cgl
    "The shirt splits straight down and your tits spill out, heavy, nipples beading hard in the air. Ah-Ning says \"{i}fuck{/i}\" under her breath, very respectfully. {i}Snap. Snap.{/i} The waistband. The seams over your hips. She tugs the ruined trousers out from under your ass, sees the slick on your thighs, and raises both eyebrows at you."
    scl_you "\"Don't.\""
    scl_ahning "\"I didn't say anything.\""
    "She peels the last rags off you and sits back on her heels."
    show scl_ahning quiet
    scl_ahning "\"You're outer now.\""
    "It isn't a joke. For once, it isn't a joke at all."
    hide cg onlayer cgl
    $ scl.fit = "court"
    "She finds you a robe from somewhere, open at the back for the tail, with loops for the horns."
    scl_ahning "\"Go and walk the gallery. They'll want to see if you can stand.\"\n{size=-5}{color=#ff8fa3}▸ Walk the gallery{/color}{/size}"
    $ vn_pass(30)
    jump scl_gallery

label scl_gallery:
    $ vn_enter(bg="scl_galleries", pc="stubborn", pc_tag="scl_pc", cast=[], cg=None)
    "Heads turn. Tongues go. Everyone can feel it on you now: the core's signature, sharp as cut metal, spiced through with dragon."
    "Then the floor goes warm under your feet. A weight comes down the gallery. Tusks. Bulk. Bristle."
    show scl_tieshan blunt at vn_cast_slot
    "Tie Shan. In his court shape he's a broad, loud man of fifty or so, and a few centuries more under it."
    "The pressure rolls out ahead of him, thick as fog. Your thighs tense to fold."
    show cg scl_stand onlayer cgl
    "Nothing happens."
    "Your spine stays straight. Your knees stay locked. You {i}stand{/i}."
    "A lord passes, and nothing happens to you at all."
    show scl_tieshan booming
    scl_tieshan "\"Well. The dragon finished her project. About time.\""
    "He half-turns, tusks lifting in surprise. A huge snort of a laugh. And he's gone, his own contract beast walking a step behind him."
    hide cg onlayer cgl
    "Your hands are shaking. Not from fear."
    scl_other "\"The fourth lord is called to the terrace. The registry wants you both.\""
    "An acolyte comes running down the gallery, bowing low.\n{size=-5}{color=#ff8fa3}▸ Go up to the terrace{/color}{/size}"
    $ vn_pass(30)
    jump scl_six_terrace

## The terrace at rung 6: the law read out, the cost stated, "The lord of the fourth perch will not
## request the seal." Tie Shan re-files your pronoun out loud. Nothing in view of the court.
label scl_six_terrace:
    $ vn_enter(bg="scl_terrace", pc="stubborn", pc_tag="scl_pc", cast=[("scl_longqi", "calm")], cg="scl_terrace_nine")
    "The Court Terrace. Polished stone broad enough for a serpent to coil on. Heat shimmering up off it. Perches in a spiral, sized for true forms, and the lords on them: fur smoking, scales blazing, far off and huge. Regalia. Long Qi stands beside you at the foot of the steps in the shape you know, and nobody touches you."
    hide cg onlayer cgl
    show scl_tieshan booming at vn_cast_slot
    scl_tieshan "\"Eleven years, fourth sister! Eleven, and your perch still empty! You've got a candidate standing right beside you. Are we to carry the blank another season?\""
    scl_longqi "\"Noted.\""
    scl_tieshan "\"Let's see the new one, then. Got spine enough to stand now. Household—\""
    "He leans down. He stops. Looks. The tits, the hips, the tail."
    show scl_tieshan blunt
    scl_tieshan "\"Household. Girl, now. File it.\""
    $ scl.she = True
    "He says it to the scribe, who corrects the docket. The court files your pronoun the way it files everything."
    show scl_boyan bored at vn_cast_slot
    scl_boyan "\"The seal makes its own law, does it not? Offered here. Offered aloud. Unforced. By the junior party, and only the junior party. List the cost, Tie Shan. Let her hear it.\""
    "Bo Yan drawls it, tails spilling off his plinth."
    show scl_tieshan blunt at vn_cast_slot
    scl_tieshan "\"The junior party speaks their name once, in open court. The roll takes it, and strikes it. The occupant is entered as the lord's. Standing reads from the perch. Their name never stands on its own again.\""
    "Tie Shan recites it. He shrugs his huge shoulders."
    scl_tieshan "\"That's the cost. It's not cruelty. It's precedent.\""
    show screen scl_roll(False)
    "The roll lies open on its stone. The line for the fourth perch is blank."
    "Long Qi's eyes stay on the far horizon. Her tail lies very still on the stone."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"Let the record note that the lord of the fourth perch will not request the seal. The perch stands empty until the junior party offers, of her own will, with her name in full. No coercion. No shame.\""
    "Flat and clear."
    scl_other "\"So noted. Vacancy marked. Court adjourns on the item.\""
    hide screen scl_roll
    "Her hand finds your wrist on the way out. She doesn't look at you. She doesn't let go until you're back in the shadow of the archway.\n{size=-5}{color=#ff8fa3}▸ Back to her quarters{/color}{/size}"
    $ vn_until(21)
    jump scl_six_night

label scl_six_night:
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg=None)
    "Neither of you eats much. Nothing on the docket between you. The law hangs in the air like steam."
    "She washes her hands at the basin. Her tail keeps wrapping round the post of the empty perch and unwrapping."
    "Then she pulls her court robe open with one tug. Heavy breasts. Red scales catching the lamp. Her cock already thickening against her thigh."
    $ scl.fit = "nude"
    show cg scl_tails_touch onlayer cgl
    "You meet her halfway across the bedding. Your tails touch first, and coil."
    "She kisses you. Not slow tonight. Hungry. Her hands are everywhere, on your tits, your hips, your ass, the new scales up your thighs, like she's reading the whole of you at once. You moan into her mouth and climb her, and her cock slides up wet between your thighs and drags right over your new pussy, ridge by ridge, and you both stop breathing."
    scl_you "\"{i}Hhh{/i}— Qi— {i}there{/i}— that's—\""
    scl_longqi "\"I know. I know.\""
    "She says it against your lips. She lays you back. Spreads your thighs with both hands, wide, and looks at your new pussy for a long time."
    scl_you "\"Qi— don't just {i}look{/i}—\""
    show cg scl_six_lick onlayer cgl
    "She bends down and licks it. One long, flat stripe, from the bottom of your slit to the top."
    scl_you "\"{i}AHH{/i}—!\""
    show scl_pc flushed
    "You've never felt anything like it. Nothing. Your hips come off the bedding and her hands push them back down. Her tongue parts your lips, slides through the wet, circles the little hard knot at the top, and your whole body locks."
    scl_you "\"Oh— oh {i}fuck{/i}— oh fuck, Qi, what {i}is{/i} that— don't stop— {i}don't stop{/i}—\""
    vn_sfx "{i}Slrp. Slrp.{/i}"
    "She doesn't stop. She licks you open the way she licked down your pearls, slow and thorough and merciless, her tongue pushing inside you, her lips sucking that hard little knot, until you're wailing and grinding your new pussy on her face and your tail is lashing the silk."
    "You come on her tongue. It's not like before. It doesn't stop at a dribble. It rolls through you, up from your pussy into the core and out to the tips of your horns, and you scream her name at the ceiling." with vnfx("shake")
    show cg scl_six_head onlayer cgl
    "She kneels up, licking her lips. Then she runs the fat ridged head of her cock up the slit of your new pussy, slow, gathering the wet, and you shake so hard your teeth click."
    scl_you "\"{i}Hhh{/i}— {i}Qi{/i}—\""
    scl_longqi "\"This is going to be a lot.\""
    "She warns you, and her tail squeezes yours. You nod. You can't do anything else.\n{size=-5}{color=#ff8fa3}▸ Open for her{/color}{/size}"
    jump scl_six_sex

label scl_six_after:
    $ scl.tier = max(scl.tier, 6)
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_six_end")
    "She comes groaning into your neck, hot and heavy, and you feel the core take the heat of it. You come again just from that, your new pussy fluttering, juices running down your ass."
    scl_you "\"{i}Ahh{/i}— Qi— {i}Qi{/i}— I don't— I don't want anyone else— {i}ever{/i}—\""
    "She doesn't stop. She pins your legs up over her shoulders and keeps going, slow and heavy and deep, her ridges dragging through your new pussy, her cum squelching out round her with every stroke."
    scl_you "\"{i}Hah{/i}— {i}hah{/i}— I'm gonna— {i}again{/i}— Qi, I'm gonna—\""
    scl_longqi "\"Then do.\""
    "You do. You clench round her and cry out and your juices flood the bedding, and she groans and fills you again on top of the first, so much it runs down the crack of your ass." with vnfx("shake")
    show cg scl_not_yet onlayer cgl
    "She stays inside you. Her forehead comes down to yours."
    scl_longqi "\"If you want to say it, say it. If not, we go as we have.\""
    "Very quietly. You open your mouth."
    "It won't come. Your name sits behind your teeth like a stone. You want it so badly you're shaking, and it won't come."
    scl_longqi "\"I will never ask you. If it takes forever, I'll wait.\""
    "Not yet. You fall asleep with her still inside you, your tails knotted, the word not said."
    call vn_night(5)
    jump scl_dawn

## ---- THE ENDING, "One Name" ----------------------------------------------------------------

## Dawn after rung 6's "not yet". Nobody sent for you; nobody could. Exactly one way on: offer your
## name.
label scl_dawn:
    $ scl.fit = "court"
    $ vn_enter(bg="scl_quarters", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_dawn_sleeping")
    "Grey light through the slits in the stone."
    "She's still asleep, one arm across the silk where you were. Her tail twitches at a dream."
    hide cg onlayer cgl
    "You get up without waking her. You put on Ah-Ning's robe. You touch the plate on its cord."
    "It's cool. Of course it's cool. Nobody's sending for you. Nobody can. That's the whole architecture of it."
    "The nine sit at dawn."
    show cg scl_perch onlayer cgl
    "You go past the perch on your way out. You've dusted it every day since you came up the mountain. You know now who it's been waiting for.\n{size=-5}{color=#ff8fa3}▸ Offer your name{/color}{/size}"
    $ vn_pass(15)
    jump scl_offering

label scl_offering:
    $ vn_enter(bg="scl_terrace_dawn", pc="stubborn", pc_tag="scl_pc", cast=[], cg="scl_terrace_walk")
    "The Court Terrace at dawn. Mist low on the stone. Gold light."
    "The nine in true form, in their spiral, enormous. Fur smoking. Scales blazing. Bo Yan's tails spilling off his plinth. Tie Shan's bulk under his banner. And at the fourth perch, red as the sunrise, a dragon, neck arched, gold eyes cool as copper."
    "She came up before you after all. She's watching you come."
    "The pressure rolls down off the terrace: dragon, fox, boar, all of it at once. An ocean of weight. It would have flattened you. It would have put your face in the stone before you'd thought a single thing."
    "Now it meets the core in your stomach, and stops."
    hide cg onlayer cgl
    "You walk to the foot of the steps. Not a knee on the stone. Your head up. Your tail heavy behind you. Your hands sweating."
    show scl_tieshan booming at vn_cast_slot
    scl_tieshan "\"Well? Who files a petition at this hour?\""
    menu:
        "Your mouth's dry. You open it."
        "Plainly":
            $ scl.petition = "plain"
            scl_you "\"I file to take the empty perch of the fourth court, by law. I know the cost. My name, once, and then struck. My standing read from hers. I want it anyway.\""
        "Defiantly":
            $ scl.petition = "defiant"
            scl_you "\"I file. I file to take the empty perch of the fourth court. Not because anyone asked me. Nobody asked me. Nobody ever will. I know what it costs. My name, struck. My standing, hers. I know {i}exactly{/i} what it costs, and I want it anyway, and I'm the one saying so.\""
            "Loud, so it bounces off the perches."
        "Tenderly":
            $ scl.petition = "tender"
            scl_you "\"I file. I file to take the empty perch of the fourth court. I came up this road to go home as something. I'd rather be hers. I know what it costs. I want it. I've wanted it for a while, and I couldn't say it, and I'm saying it.\""
            "It comes out soft. You don't fix it."
    "Bo Yan laughs, delighted, all the way down the balustrade. Tie Shan's head inclines."
    "The dragon at the fourth perch doesn't move for a long time."
    show scl_longqi calm at vn_cast_slot
    scl_longqi "\"If this is your will, then offer your name. The law will bind, or it will not.\""
    "Her voice is so low the stone hums. You climb onto the steps. The scribes lift their brushes."
    show cg scl_name onlayer cgl
    scl_you "\"[scl_full_name]. In open court, of sound mind, unforced.\""
    "Loud enough that the old stone catches every word."
    "The terrace leans in.\n{size=-5}{color=#ff8fa3}▸ Hold your feet{/color}{/size}"
    hide cg onlayer cgl
    jump scl_tribulation

## The tribulation, run backwards: it goes looking for whether anything underneath still answers to
## that name. There is. The body's last row lands; you keep your feet the whole time.
label scl_tribulation:
    $ vn_enter(bg="scl_terrace_storm", pc="protesting", pc_tag="scl_pc", cast=[], cg="scl_tribulation")
    "It comes down the mountain like a landslide."
    "Wind. Heat. Qi howling round you, whipping at your robe. A transformation tribulation, run backwards: it isn't stripping a shape off you. It's going looking. Down through everything. For whether there's anything underneath still willing to answer to that name."
    scl_you "\"{i}Hhhh{/i}— {i}AHH{/i}—!\"" with vnfx("flash")
    $ scl_body(7)
    show cg scl_tribulation_swell onlayer cgl
    "{color=#ff5fb8}The core in your stomach goes white-hot.{/color}"
    "{color=#ff5fb8}Your tits swell against the robe, heavier, fuller, pushing the cloth apart. Past F. Past anything you've got a word for. Heavy H-cups bursting the robe open, and your hands fly up to them and can't hold them, and they spill over your fingers.{/color}"
    scl_you "\"{i}Hhhah{/i}— they won't— they won't {i}stop{/i}—!\""
    "{color=#ff5fb8}Your hips surge out under you. Your waist pulls in tight between them. Your thighs thicken, your ass swells until the seams split down the back. Your lips go plump and hot. Your twin tails pour down past your waist. Scales race up your outer thighs in shining ladders, red-gold, and climb your brow and the line of your jaw. Your horns lengthen and curl back, long and heavy as iron. Your tail swells thick behind you and lashes the stone.{/color}"
    show scl_pc flushed
    scl_you "\"{i}Ahh{/i}— {i}AHH{/i}— it's— it's so {i}much{/i}—!\""
    "{color=#ff5fb8}Every change hits like a climax. Your nipples swell and throb and leak heat. Your pussy clenches on nothing in a slow, milking rhythm, like it already knows her by heart, and floods your thighs. The core blazes, and blazes, and you're screaming, and it's too much and it's so {i}good{/i}, the bright sweet thing underneath all of it, the thing that feels like her.{/color}"
    scl_you "\"{i}AHH{/i}— {i}everywhere{/i}—!\"" with vnfx("shake")
    "{color=#ff5fb8}And all of you is lit up to the top. The wind on your lips is a kiss. The wind on your nipples is a tongue. The wind between your thighs makes you scream.{/color}"
    "It digs. It asks."
    "{i}{color=#ff8fb8}Is there anyone in here? Does anyone still answer to that?{/color}{/i}"
    "Your knees bend."
    "They don't touch the stone."
    show scl_pc stubborn
    scl_you "\"I'm— {i}here{/i}— I'm still {i}here{/i}— it's {i}me{/i}—!\""
    "It finds you. Down at the bottom of everything, it finds you, and you answer, and it stops looking."
    show cg scl_column onlayer cgl
    "The storm breaks. Red light goes up off the terrace in a column and comes down as silence."
    hide cg onlayer cgl
    "You're standing. You kept your feet the whole time.\n{size=-5}{color=#ff8fa3}▸ Look up{/color}{/size}"
    jump scl_seal

## The seal: Long Qi comes down off her perch in the shape you know to touch her brow to yours.
## "Perch filled." "About time, neighbour." The occupant is entered as hers.
label scl_seal:
    $ scl.done = True
    $ scl.ending = "one-name"
    $ achievement.grant("One Name")
    $ vn_enter(bg="scl_terrace_dawn", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_descends")
    "The dragon comes down off the fourth perch."
    "Halfway down the steps she isn't a dragon any more. She's the shape you know: tall, horned, red twin tails, her tail swaying, her scales worn open like rank. Her bare feet on the stone."
    show cg scl_seal onlayer cgl
    "She stops in front of you. She bends, and touches her brow to yours."
    "That's all. That's the seal. Warm, and steady, and done."
    hide cg onlayer cgl
    show scl_boyan delighted at vn_cast_slot
    scl_boyan "\"Perch filled. After eleven quiet years, the registry thanks the dragon for closing her file.\""
    "Bo Yan calls it down, bright and wry."
    show scl_tieshan booming at vn_cast_slot
    scl_tieshan "\"About time, neighbour.\""
    show screen scl_roll(True)
    "The scribes' brushes move. The roll is amended in front of the nine."
    "Your name isn't on it. The roll records the fourth perch as occupied, and the occupant is entered as hers, in the court's own hand. You offered your name out loud once, and that was the only time it ever counted."
    hide screen scl_roll
    hide scl_tieshan
    "You stand beside her perch, in front of everyone, and you don't kneel. When the boar lord's procession passes, you incline your head first. On purpose. Because you chose to."
    show scl_longqi warm at vn_cast_slot
    show cg scl_earrings onlayer cgl
    scl_longqi "\"Off the mountain, scale forgets itself. Wear these in town.\""
    "Long Qi presses a pair of earrings into your palm on the way down."
    hide cg onlayer cgl
    menu:
        "The day ahead of you, and the night."
        "Her quarters, that night":
            $ vn_until(21)
            jump scl_perch_night
        "Let the day go by":
            $ vn_pass(120)
            jump scl_epilogue

label scl_perch_night:
    $ scl.fit = "nude"
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_on_perch")
    "She doesn't go to her desk."
    "She walks you down the room to the perch, yours now, and lays you back across the rumpled blanket on it, and spreads your thighs with both hands."
    scl_longqi "\"[scl_full_name].\""
    "Your whole name, the last time anyone will say it out loud."
    scl_you "\"Qi— {i}Qi{/i}— please—\""
    "She kisses you. Your mouth, your throat, the new scales along your jaw, the base of each horn, slow, like she's signing every one. Her hands fill themselves with your tits, heavier than this morning, spilling over her fingers. She squeezes, and you moan into her mouth."
    scl_longqi "\"Look at you. On my perch.\""
    "She murmurs it."
    scl_you "\"{i}Our{/i} perch— {i}mine{/i}— it's mine now— {i}ahh{/i}—\""
    "Her thumb finds your clit. Circles. You're so wet it's already running down onto the blanket. Your hips roll up into her hand, and your tail wraps round her waist and drags her down onto you."
    scl_longqi "\"Yours.\""
    "She agrees, and lines herself up.\n{size=-5}{color=#ff8fa3}▸ Take her{/color}{/size}"
    jump scl_perch_sex

label scl_perch_after:
    $ vn_enter(bg="scl_quarters_night", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_perch_end")
    "She comes with her forehead on yours again, hot and heavy, and the core in your stomach drinks the heat of it like it always has, except now it's yours doing the drinking. Your tails knot on the perch."
    scl_you "\"{i}Hah{/i}— {i}hah{/i}— Qi—\""
    scl_longqi "\"Good girl. Mine.\""
    scl_you "\"Yours.\""
    "It's easy now. It's the easiest thing in the world.\n{size=-5}{color=#ff8fa3}▸ Morning{/color}{/size}"
    call vn_night(8)
    jump scl_epilogue

## The epilogue: flavour; the body and the home are the same either way. The choice decides the
## ending (owner, 2026-11-11: mark it).
label scl_epilogue:
    $ scl.fit = "court"
    $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_drawer")
    "The drawer by your old bedding roll is still full of unfinished letters."
    menu:
        "The letters, and the road down the mountain."
        "Write home" (ending=True):
            jump scl_epilogue_letter
        "Go home for the autumn" (ending=True):
            jump scl_epilogue_autumn

label scl_epilogue_letter:
    $ scl.epilogue = "letter"
    $ vn_enter(bg="scl_quarters", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_letter_write")
    "You take out the top one. {i}Dear Mother. I am fed and housed and{/i}—"
    "It always stopped there. At the sentence about what you've become."
    "You dip the brush."
    "{i}—and I am a contract beast of the Coiling Fang, on the fourth perch, and it's mine. I have red hair now. You'd like it. I am not coming home as what you paid for. I am coming home as something.{/i}"
    "You sign it. You seal it. It goes down the mountain with the envoys' post."
    show cg scl_brazier onlayer cgl
    show scl_longqi calm at vn_cast_slot
    "The rest of the drawer you burn in her brazier, one by one, and she watches you do it from her desk, and doesn't say a thing.\n{size=-5}{color=#ff8fa3}▸ Out to the gate{/color}{/size}"
    jump scl_route_return

label scl_epilogue_autumn:
    $ scl.epilogue = "autumn"
    $ vn_enter(bg="scl_gatehouse", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg=None)
    scl_longqi "\"Take the low way. The high one floods in spring, and I shall worry.\""
    "Long Qi says it at the gate. It's autumn. You take the low way anyway."
    $ vn_enter(bg="scl_road", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_low_way")
    "Down the switchbacks. Through the forest. Two valleys, on foot, with your tail tucked under a travelling cloak that doesn't hide it at all."
    $ vn_enter(bg="scl_village", pc="soft", pc_tag="scl_pc", cast=[], cg="scl_mother")
    "Your mother is at the door. She stares. Not at the red. At the hips, the tits, the horns, the tail, the scales up the line of your jaw."
    "Over tea, she asks what you are now."
    show cg scl_plate_table onlayer cgl
    "You set the plate on the table between you. Her scale, sealed and lacquered."
    scl_you "\"A contract beast of the Coiling Fang.\""
    "She looks at it a long time. Then she pours you more tea."
    hide cg onlayer cgl
    $ vn_enter(bg="scl_gatehouse", pc="soft", pc_tag="scl_pc", cast=[("scl_longqi", "warm")], cg="scl_back_up")
    "You stay a while. Then you take the low way back up the road, and Long Qi is waiting at the gatehouse, and she doesn't say a thing about how long you were gone. She just puts her hand on the small of your back and walks you up to the household.\n{size=-5}{color=#ff8fa3}▸ Up to the household{/color}{/size}"
    jump scl_route_return
