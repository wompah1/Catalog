## THE SOURCE: wolfpack's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee), written as beats; days 4 to 7 and the ending are in
## late.rpy, the director scenes in scenes.rpy. The original is in catalog/docs/routes/vn-original/
## wolfpack/. Seven days, chained. The pack talks in clipped two- and three-word lines; the alpha is
## never named; Scrap is the newest, never the youngest.

## ---- DAY 1: the transect, carried, "Not pack."; rung 1 before dawn ---------------------------------

label wlf_opening:
    $ wlf.fit = "own"
    $ vn_enter(bg="wlf_transect", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_transect_walk")
    "The last leg of a solo transect, deep in the forest, and you're making good time."
    "[wlf_pc_name] Crane. Twenty-four. Contract wildlife surveyor. Lean, sunburnt, a field stubble you've decided suits you, and the cleanest numbers the agency's had all season. Boots holding up. Notebook in the crook of your arm. Headlamp on the strap."
    "Nothing out here has ever outranked you. Not a ridge. Not a river. Not the weather."
    show cg wlf_paced onlayer cgl
    "Then something starts pacing you."
    "Off the path. Behind you. {i}Upright{/i}: two feet, not four, you can hear that much. It matches your speed. It doesn't close. It doesn't drop back. For the whole last mile."
    wlf_you "\"Fine. Pace me. I'm faster.\""
    menu:
        "You tell the trees."
        "Walk faster":
            $ wlf.met = "faster"
        "Stop dead and turn round":
            $ wlf.met = "turn"
    $ vn_pass(20)
    jump wlf_carried

label wlf_carried:
    $ vn_enter(bg="wlf_transect", pc="furious", pc_tag="wlf_pc", cast=[], cg=None)
    if wlf.met == "turn":
        "You turn, and there's a chest in front of your face. A wall of one."
    else:
        "You don't get far. Footsteps, unhurried, and then a shadow drops across your shoulder."
    show cg wlf_carried onlayer cgl
    "Hands close on you."
    "Not claws. {i}Hands.{/i} Big and warm and dark-nailed, one round your ribs and one behind your knees, and the ground just leaves."
    "He picks you up like freight. Pack, boots, gear and all, slung against him without a squeeze or a shake. Not caught. {i}Carried.{/i}"
    wlf_you "\"Hey— put me— {i}hey!{/i}\""
    "He doesn't. He doesn't say a word. He walks: past the stream where it splits, past the lake flashing silver through the trunks, up a trail you've never mapped, and in under a ledge, into the mouth of a cave."
    $ vn_enter(bg="wlf_den", pc="furious", pc_tag="wlf_pc", cast=[], cg=None)
    "Warm air. Woodsmoke. Stone."
    show wlf_alpha flat at vn_cast_slot
    "He sets you down in the middle of the floor and steps back, and you finally get a look at him."
    "A man. Huge, the biggest body you've ever stood next to: black hair, a scar through one brow, gold eyes. And on top of his head, turning to follow you, a pair of black wolf ears. Behind him a heavy black tail sways once and goes still."
    hide wlf_alpha
    show cg wlf_pack_line onlayer cgl
    "There are more of them."
    "Grey-streaked hair and beard, gold eyes sharp as a hawk's, standing nearest the black one. A lean one with a split right ear, grinning at nothing. A crooked half-smile and burrs stuck in his hair and all down his tail. An old one, white-haired and stiff in the hips, feeding the fire at the back. And one shorter by a head than the rest, wiry, wound tight as a sprung trap, at the very end of the line."
    "All grown men, from the old one at the fire, sixty if he's a day, to the short one, who can't be far past his early twenties. Human faces. Human hands. Wolf ears, wolf tails, gold eyes, dark nails. When the split-eared one yawns, {i}fangs{/i}."
    hide cg onlayer cgl
    show wlf_alpha flat at vn_cast_slot
    "The black one looks you over. Once. Head to boots."
    wlf_alpha "\"[WLF_VERDICT[0]]\""
    hide wlf_alpha
    "Then he walks to the back of the den, lies down on the biggest pile of furs, and goes to sleep.\n{size=-5}{color=#ff8fa3}▸ Wait for whatever happens next{/color}{/size}"
    $ vn_pass(10)
    jump wlf_not_pack

label wlf_not_pack:
    $ vn_enter(bg="wlf_den", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_rack")
    "Nothing happens next."
    "That's the insult. Nobody touches you. Nobody looks at you. They go back to what they were doing: strips of dried meat off a rack by the fire, a clay bowl going hand to hand, talk in two-word grunts."
    "\"Rack's low.\""
    "\"Hunt tomorrow.\""
    "\"Fire wants wood.\""
    "You cough. Pointedly. You clear your throat."
    "Nothing."
    hide cg onlayer cgl
    show wlf_oldman flat at vn_cast_slot
    "Then the old one at the fire looks up, and holds your eye a moment longer than anybody else has, and says it."
    wlf_old "\"Pack takes nothing that doesn't present.\""
    hide wlf_oldman
    "That's all. He goes back to the fire."
    "You wait for the rest of it. There isn't any. Nobody explains, nobody translates, and nobody needs to, because you can read a room, and this one just handed you its whole operating manual in one sentence."
    "Not a threat. A {i}rule{/i}. Literal. Load-bearing. A system."
    show wlf_pc smug
    "And you've never met a system you couldn't climb.\n{size=-5}{color=#ff8fa3}▸ Make them look at you{/color}{/size}"
    $ vn_pass(30)
    jump wlf_stare

label wlf_stare:
    $ vn_enter(bg="wlf_den", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "Dominance display. Basic stuff. Eye contact, held."
    show wlf_grey flat at vn_cast_slot
    "You try the grey-bearded one first, when he lifts his head from the bowl. You catch his eye and {i}hold{/i} it, chin up, shoulders square."
    "He looks straight back at you. Bored. Then he reaches past you for the bowl."
    hide wlf_grey
    show cg wlf_yawn onlayer cgl
    "The one with the split ear next. You set your jaw in a shape nobody back home would mistake for anything but a challenge."
    "He meets your eyes, completely blank. Then he {i}yawns{/i}. Right at you. Jaws wide, fangs out, tongue curling, a yawn big enough to fit your whole fist in."
    show wlf_pc furious
    wlf_you "\"Oh, {i}fuck{/i} you.\""
    "He goes to sleep."
    hide cg onlayer cgl
    show wlf_pc proud
    "The third one you keep. You'll spend it later, somewhere it counts."
    $ vn_enter(bg="wlf_den_night", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_crescent")
    "Night comes down over the mouth of the cave. They lie down in order without a word about it: a loose crescent round the fire, heads to tails, the old one at the fire's edge, and the black one alone at the back, past the banked coals. Nobody goes near him."
    "Nobody comes near you either. Your kit's in the corner by the mouth. You sit down next to it on the bare stone.\n{size=-5}{color=#ff8fa3}▸ Lie down by your kit{/color}{/size}"
    $ vn_pass(60)
    jump wlf_night_one

## The toothache, notebook one, the plan, the night.
label wlf_night_one:
    $ vn_enter(bg="wlf_den_night", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "{color=#ff5fb8}It starts in the back of your jaw. Not a crack, not a filling. Deeper. A buzzing pressure right down in the roots, like something in there is turning over in its sleep.{/color}"
    "{color=#ff5fb8}You press your tongue to it. You press your thumb to your cheek. Nothing's swollen. Nothing's loose. It just {i}hums{/i}.{/color}"
    "Fine. Work through it."
    show cg wlf_notebook_lamp onlayer cgl
    "You thumb the headlamp down to its lowest setting and get the notebook out."
    show screen wlf_notebook(1)
    "You write it up."
    hide screen wlf_notebook
    hide cg onlayer cgl
    "You close the notebook. Then you lie there and plan."
    "Run for the mouth and go straight for the lake. Wait for daylight and slip out when they hunt. Wedge into a crack and watch how they sleep."
    "Every plan dies on the same rock: {i}he{/i} doesn't move. The black one sleeps across the only warm spot in the den, and the others sleep in order out from him, and the order doesn't change."
    "Order."
    "You sit up in the dark."
    "It's not a prison. It's a {i}ladder{/i}. A place for everyone and a ranking, every body in the room telling you who's where: who eats first, who sleeps nearest, who looks away. They've put you at the bottom. Below the bottom. Not on it at all."
    "And the old man already told you the one rule there is."
    show wlf_pc smug
    "Fine. You won't present. You're not a {i}specimen{/i}. Nobody in this cave is getting anything off [wlf_pc_name] Crane. You'll climb it the way you've climbed every ladder you've ever been put at the bottom of: out-work them, out-stare them, out-last them."
    "Your jaw thrums. You grin into the dark anyway, and it makes your teeth buzz right up into your ears."
    "You've never lost a hierarchy in your life."
    show cg wlf_headlamp_dot onlayer cgl
    "You fall asleep with the headlamp still on, a little red dot against the stone. Across the fire, the split-eared one is watching it like it's the best thing he's ever seen."
    show screen wlf_furs("night")
    "The fire ticks down.\n{size=-5}{color=#ff8fa3}▸ Wait for the light{/color}{/size}"
    hide screen wlf_furs
    call vn_night(4)
    jump wlf_back_of_den

## Rung 1, before dawn (non-con): you go to the back wall for your headlamp and bend for it, and the
## pack decides that counts. "Presented." The choice is how you fight, never whether.
label wlf_back_of_den:
    $ vn_enter(bg="wlf_den_night", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "Your jaw wakes you. It's still dark, just going blue at the mouth of the cave."
    show screen wlf_furs("wake")
    "You roll over on the stone."
    hide screen wlf_furs
    "The headlamp's gone."
    show cg wlf_lamp_in_furs onlayer cgl
    "You pat the stone. Your kit. Your pockets. Then you see it: a little red dot, blinking, right at the back of the den. In the black one's furs. The split-eared one must have had it in the night, and that's where he's left it."
    "Everybody's asleep. Bodies heaped in their crescent, breathing slow. Past the banked fire, the black one, alone on the deepest furs, in a space nobody else crosses."
    "You cross it. That's {i}your{/i} headlamp."
    show cg wlf_bend onlayer cgl
    "The furs at the back are thick and warm and they smell like him. The lamp's wedged down between two hides by his hip. You plant your hands, stick your ass out, and bend right over to dig for it."
    "His ear flicks."
    show cg wlf_nape onlayer cgl
    "A hand closes on the back of your neck."
    wlf_alpha "\"Presented.\""
    "Not a question. A {i}verdict{/i}."
    show wlf_pc furious
    wlf_you "\"What? No— {i}no{/i}, I'm getting my— I'm getting my {i}headlamp{/i}—\""
    "The hand on your nape pushes. Gently. Completely. Your cheek goes down into the furs and your ass stays up in the air exactly where you put it, and his other hand is already tugging your trousers down over your hips."
    menu:
        "His hand on your nape. Your cheek in his furs."
        "Kick back at him":
            $ wlf.how1 = "kick"
        "Swear at him, as loud as you can":
            $ wlf.how1 = "swear"
        "Claw at the furs and try to crawl out":
            $ wlf.how1 = "claw"
    $ vn_pass(5)
    jump wlf_rung_one

## Rung 1, non-con: the alpha, slow and enormous, his hand on your nape. You scream that you did NOT
## present the whole way, and the body betrays it. The knot presses and is never offered. Your third
## stare-down is a glare. You come in his fist; he fills you.
label wlf_rung_one:
    $ vn_enter(bg="wlf_den_night", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_r1_pinned")
    if wlf.how1 == "swear":
        wlf_you "\"Get OFF me, you— you overgrown— I did NOT present! I was getting my {i}HEADLAMP{/i}!\""
        "It bounces off the roof of the cave. Across the den nobody so much as twitches."
    elif wlf.how1 == "claw":
        "You get two fistfuls of fur and haul yourself forward, a foot, two. He takes your hips in both hands and drags you straight back, furs and all."
    else:
        "You kick back at him, hard, and catch nothing but thigh. It's like kicking a tree. He moves one knee and pins your ankle under it."
    "His weight comes down over you. Not crushing. Just {i}there{/i}, everywhere, so you can't get a knee under you. Hot breath on your nape."
    "Something hot and heavy and {i}enormous{/i} slides up between your bare cheeks."
    wlf_you "\"No— no no no, don't you {i}dare{/i}— that's not— I didn't {i}offer{/i}—\""
    "Slick fingers. A lot of slick, worked into you slow and thorough, two fingers, three, and you're swearing at him the whole time, and your hips are rolling back onto his hand anyway. Then the fat blunt head of him, pressing."
    show cg wlf_r1_in onlayer cgl
    "And {i}pushing{/i}."
    vn_sfx "{i}Squelch.{/i}" with vnfx("shake")
    show wlf_pc flushed
    wlf_you "\"{i}Ahh—!{/i} Ah— get it {i}out{/i}— oh fuck— oh {i}fuck{/i}—\""
    "He opens you up in one long, slow, unstoppable slide. Stretch, and stretch, and {i}more{/i}, so full your vision sparks, so deep you feel him in your stomach. Your cock bobs under you, hard, and it's {i}leaking{/i}, and you hate it."
    wlf_alpha "\"Breed you.\""
    "And he starts to move."
    vn_sfx "{i}Slap.{/i}"
    "Slow. Heavy. All the way out until just the head of him tugs at your rim, then all the way back in to the hilt. Every stroke shoves a noise out of you."
    wlf_alpha "\"Mine now.\""
    show wlf_pc furious
    wlf_you "\"I'm— {i}not{/i}— yours— {i}haa{/i}—\""
    "He shifts his hips. Changes the angle. And the next stroke drags the whole thick length of him straight across something inside you that whites out the world."
    show wlf_pc flushed
    wlf_you "\"{i}AHH—!{/i}\"" with vnfx("shake")
    "It has to carry all the way to the lake."
    wlf_alpha "\"Loud.\""
    "He says it approving, and hits it again."
    wlf_you "\"Stop— stop {i}finding{/i} it— {i}ahh{/i}— not there, not {i}there{/i}—\""
    "He doesn't stop. He works it. Long, deliberate drags right over that spot, over and over, his hand still on your nape, until you're making one continuous noise and slick is running down the backs of your thighs."
    wlf_alpha "\"Tight. Take more.\""
    wlf_you "\"I'm {i}not{/i} taking— I'm not— {i}nnhh{/i}—\""
    show cg wlf_r1_glare onlayer cgl
    show wlf_pc furious
    "Your knees skid wider in the furs. Nobody spread them. You twist your head round under his hand to glare at him, and you {i}lock eyes{/i}."
    "The third stare-down. The one you saved."
    "He stares right back. Gold eyes, flat, almost bored, except for the focus he puts into every single push. You glare murder at him. He doesn't look away. He just fucks you, slow and enormous and staring, and you're the one who moans."
    wlf_alpha "\"Mine. Breed you. Full soon.\""
    "On the deepest stroke yet he leans in, and you feel something new: a thick swell at the base of his cock, pressing at your rim. Hot. Huge. {i}Pressing.{/i}"
    wlf_you "\"What's— what is {i}that{/i}— don't— don't you put that—\""
    "He doesn't. It presses, and holds, and stays outside. And some part of you that isn't you at all is {i}disappointed{/i}, and you hate that most of all."
    show wlf_pc flushed
    wlf_you "\"I'm gonna— no— I'm {i}not{/i}— {i}harder{/i}— no, I didn't mean—\""
    show cg wlf_r1_cum onlayer cgl
    "His hand comes round under you and closes on your cock. Rough, quick, squeezing."
    wlf_you "\"{i}Ahh— ahh— AHH—!{/i}\"" with vnfx("shake")
    "You come so hard your knees go out. Spurt after spurt, all over his fist and the furs and the insides of your own thighs, yelling the whole time, clenching down on him so tight he grunts."
    "He drives in to the root and stays there, and you feel him go: thick, hot pulses, pumping deep, so much of it it feels like you'll never be empty again."
    wlf_alpha "\"Full.\""
    "Into your neck."
    wlf_you "\"You— you {i}bastard{/i}.\""
    "You pant it into the furs, wrecked, and it comes out sounding like a thank-you."
    menu:
        "He's still in you."
        "He's still hard, and he isn't pulling out":
            $ wlf.round1 = True
            jump wlf_round_one_sex
        "Let him do whatever he's doing to your neck":
            $ wlf.round1 = False
            $ vn_pass(30)
            jump wlf_low_pack

## The round's finish.
label wlf_round_one_after:
    $ vn_enter(bg="wlf_den_night", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_r1_round_cum")
    "He finishes deep again, a second flood on top of the first, and you feel it run out of you round him."
    wlf_you "\"That did not. {i}Count{/i}.\""
    "You croak it into the furs. Your hole clenches round him on the last word like it's disagreeing.\n{size=-5}{color=#ff8fa3}▸ Let him do whatever he's doing to your neck{/color}{/size}"
    $ vn_pass(20)
    jump wlf_low_pack

## The verdict at grey light: rank 1. Groomed, furious, asleep.
label wlf_low_pack:
    $ vn_enter(bg="wlf_den", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_groomed")
    "Grey light at the mouth."
    "He's licking the back of your neck. Long, slow, patient strokes of his tongue, up your nape and into your hair, the way the others did each other's ears last night."
    "{i}Grooming{/i} you."
    "It's the second most insulting thing that's ever happened to you, and the first was an hour ago. You open your mouth to tell him exactly what you're going to do to him."
    $ wlf_advance(1)
    wlf_alpha "\"[WLF_VERDICT[1]]\""
    "You shut your mouth."
    hide cg onlayer cgl
    show wlf_pc proud
    "Low pack. {i}Pack.{/i} On the board. Up from nothing in a single night."
    show wlf_pc furious
    "For {i}that{/i}. For bending over for a headlamp and getting held down and fucked stupid. That's what moves you up in here. Not work. Not nerve. {i}That.{/i}"
    "You're furious. You're filing it anyway. Data is data."
    show cg wlf_first_hide onlayer cgl
    "Over by the fire, the old man gets up, takes an old hide off the pile, and drops it at the mouth of the cave, past the end of the crescent. Then he goes back to the fire without a word."
    "You crawl to it, headlamp in your fist. It's yours."
    show screen wlf_furs("night")
    "You mean to stay furious about all of it. You're asleep before you've finished deciding to be.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen wlf_furs
    call vn_night(11)
    jump wlf_day_two

## ---- DAY 2: rung 1's body; the treeline; the wolfshrooms; the names; rung 2, the queue -------------

label wlf_day_two:
    $ vn_enter(bg="wlf_den", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "Late morning. Sunlight at the mouth of the cave, birdsong in the trees, half the pack still asleep."
    show screen wlf_furs("wake")
    "You stretch on your hide."
    hide screen wlf_furs
    $ wlf_body(1)
    show cg wlf_fangs onlayer cgl
    "{color=#ff5fb8}Your tongue finds it before you're even awake.{/color}"
    "{color=#ff5fb8}A point. Sharp. Right where your canine used to be. You run your tongue along and there's another, top and bottom, long and smooth and {i}wicked{/i}.{/color}"
    "{color=#ff5fb8}Fangs.{/color}"
    "{color=#ff5fb8}You sit bolt upright and shove your thumb in your mouth and bite down. {i}Hard.{/i} Just short of breaking the skin. They sink in like they were made for it.{/color}"
    show wlf_pc smug
    "{color=#ff5fb8}You laugh out loud. It comes out husky, rough round the new teeth, lower than it should be.{/color}"
    show cg wlf_smooth onlayer cgl
    "{color=#ff5fb8}Then you notice your thumb. Your hand. Your {i}arm{/i}. Smooth. The hair's gone. Not shaved: {i}gone{/i}, like it was never there. You drag your palm down your chest, your stomach, your legs. Smooth, smooth, smooth, warm as a stone in the sun, and soft in a way your skin's never been in your life.{/color}"
    "{color=#ff5fb8}Your jaw: no stubble. Your lashes, when you blink, feel heavier. Darker. Your lips are fuller under your thumb.{/color}"
    "{color=#ff5fb8}And your nipples. You brush one by accident and your whole body jumps.{/color}"
    show wlf_pc flushed
    wlf_you "\"Ah— {i}ah{/i}—\""
    "{color=#ff5fb8}Tender. Puffy-tender, buzzing. You pinch it, just to check, and a moan falls out of you before you can stop it. You pinch the other one. Your hips roll on their own, and they roll {i}differently{/i}: the line of them has gone a shade soft, a shade wider.{/color}"
    "{color=#ff5fb8}Your cock's hard against your stomach. Smaller than it was. Not by a lot. Enough that you notice, staring at it in the morning light, giving it a squeeze, and it throbs in your fist like it doesn't mind at all.{/color}"
    "{color=#ff5fb8}You lick your lips, and your whole mouth {i}lights up{/i}. Lips, tongue, the roof of it, buzzing, so sensitive the lick drags a moan straight out of you.{/color}"
    wlf_you "\"{i}Mmhh{/i}— oh, what the {i}fuck{/i}—\""
    "{color=#ff5fb8}You suck your thumb back in just to feel it again, and moan round it. And when you shift on the hide your ass {i}tingles{/i}, hot and twitchy, and you squirm and gasp out loud.{/color}"
    hide cg onlayer cgl
    show wlf_pc smug
    "You flash your fangs at the cave roof."
    wlf_you "\"{color=#f3c969}[WLF_WORD['fangs']]{/color}\""
    show wlf_pc proud
    "Your ass reminds you of last night every time you shift your weight, and every time it does, your back arches on its own, like your body learned the shape of him overnight. You tell it to stop. It doesn't."
    "Nothing ties you down. Nobody's at the mouth. Your kit's in the corner, boots upright, exactly where you left it.\n{size=-5}{color=#ff8fa3}▸ Walk out to the treeline, and keep walking{/color}{/size}"
    $ vn_pass(20)
    jump wlf_treeline

## The treeline: the pack is already sitting across the path. You walk back because they block it.
## Nobody touches you or looks at you there.
label wlf_treeline:
    $ vn_enter(bg="wlf_treeline", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "You pull your boots on, shoulder your kit, and walk straight out of the den into the sun."
    "Nobody stops you. Nobody gets up. You're across the ledge, and down through the ferns, and at the treeline, with the whole forest open in front of you and the lake shining somewhere below—"
    show cg wlf_path_blocked onlayer cgl
    "And they're already there."
    "The grey-bearded one, the burr-matted one, the split-ear, the short one. Sitting in the ferns right across the path. Chewing strips off the rack. Not looking at you."
    wlf_you "\"Excuse me.\""
    "Nobody moves. You go left, round the split-ear, and his tail's lying across the gap. You go right, and the burr-matted one stretches his legs out and crosses his ankles exactly where your foot was going. The grey-bearded one picks something out of his teeth."
    "Nobody touches you. Nobody so much as looks up. They just sit where the path is, and they keep sitting there, and the forest on the other side of them might as well be the moon."
    show wlf_pc furious
    wlf_you "\"Fine. {i}Fine.{/i}\""
    hide cg onlayer cgl
    "You spit into the leaves, square your shoulders, and walk back up the slope. Because they're {i}sitting on the path{/i}."
    "When you look back from the ledge, the ferns are empty."
    $ vn_enter(bg="wlf_mouth", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_mapping")
    "Then you sit at the mouth and watch them, and you map the den like a job."
    "Who wakes first: the burr-matted one, scratching. Who eats first: the black one, always, and nobody touches the rack till he's done. Grey-beard next, sitting close, the only one who talks back to him. The split-ear darting in for scraps, grinning. The old one by the fire with a chipped mug, eating whenever he likes, which tells you everything about where {i}he{/i} sits. And the short wiry one, last, at the edge, ears flat, eating what's left."
    "Order. Every body in the room knows its place."
    "Except yours. Yours is just past the end of the crescent, on one hide, and you don't intend to stay there.\n{size=-5}{color=#ff8fa3}▸ Find out what they eat out on the trail{/color}{/size}"
    $ vn_pass(60)
    jump wlf_trail

## The wolfshrooms: eaten by the handful because the pack eats them. Nobody offers, watches or
## comments, and nothing explains them.
label wlf_trail:
    $ vn_enter(bg="wlf_trail", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_shrooms")
    "The trail behind the den is beaten flat by big bare feet, and where the tracks crowd thickest, at the foot of an old windfall, you find them."
    "Mushrooms. Pale grey, fat, cold to the touch even in the sun, faintly shining where the shade's deepest. Wolfshrooms. And every cluster on the trail is picked over: nibbled, cleared, the stalks bitten off clean."
    "The fangs. The timing. Their diet."
    "It's not a riddle. It's {i}data{/i}."
    show cg wlf_shrooms_eat onlayer cgl
    "You check the wind. You check the trees. Nobody. You fill both hands and shove them in your mouth."
    "Bitter. Cold, like sucking wet iron. Then a fizz at the back of your teeth, a buzz that runs down your throat and spreads out low in your belly like a swallow of something strong."
    show wlf_pc flushed
    wlf_you "\"Mmh— oh, {i}that's{/i} nice.\""
    "Your cock stiffens in your trousers. You eat another handful. Then one more, for luck."
    show wlf_pc smug
    hide cg onlayer cgl
    "If they get to the top by eating this, you'll get there faster. Obviously.\n{size=-5}{color=#ff8fa3}▸ Back to the den at dusk{/color}{/size}"
    $ vn_until(19)
    jump wlf_names

## Dusk, day 2: the scalp itch, then you name the five. Then the spring.
label wlf_names:
    $ vn_enter(bg="wlf_den", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "{color=#ff5fb8}By dusk your scalp is on {i}fire{/i}.{/color}"
    "{color=#ff5fb8}Right above each ear, deep under the skin, an itch like nerves knitting. You rake your nails through your hair. It doesn't help. You grin anyway. Something's coming. You put it there yourself.{/color}"
    "The den's full, every one of them in, the fire up, the crescent forming. Nobody's in the warmest place yet but the black one."
    show cg wlf_naming onlayer cgl
    "You stand up in front of the other five, blocking the last of the light from the mouth, and you name them. Out loud. On purpose. You name what's below you."
    $ wlf_grey_name = "Grey"
    wlf_you "\"Grey.\""
    "The grey-bearded one, the one who sits closest."
    $ wlf_notch_name = "Notch"
    wlf_you "\"Notch.\""
    "The split ear. His ears perk right up."
    $ wlf_bramble_name = "Bramble"
    wlf_you "\"Bramble.\""
    "Burrs and a crooked grin."
    $ wlf_old_name = "Old Man"
    wlf_you "\"Old Man.\""
    "The fire-keeper. His face cracks into a smile over his mug."
    $ wlf_scrap_name = "Scrap"
    wlf_you "\"Scrap.\""
    "The short wiry one, at the very end, ears already flat."
    "Grey nods, once. Bramble grins wider. Scrap ducks his head, mortified to be called last. And Notch says it back under his breath, tasting it, and his tail thumps the stone."
    wlf_notch "\"Notch.\""
    show wlf_pc smug
    "Named. Filed. {i}Yours.{/i}"
    hide cg onlayer cgl
    "At the back, the black one doesn't open his eyes. You don't name him. You're not giving him the satisfaction."
    $ wlf.fit = "nude"
    $ vn_enter(bg="wlf_spring", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_spring_kneel")
    "Then you go out to the spring at the mouth to wash, because you smell of {i}him{/i} and you've been smelling it all day. You strip to the skin on the moss, kneel at the water, and lean right down to splash your face."
    "Behind you, the talk stops."
    wlf_alpha "\"Presented.\""
    "From the back of the den, without opening his eyes."
    show wlf_pc furious
    wlf_you "\"I'm {i}washing{/i}—\""
    show cg wlf_spring_hand onlayer cgl
    "Grey's hand lands on the small of your back, flat and heavy, and keeps you exactly where you are."
    menu:
        "Grey's hand on your back. The whole pack behind you."
        "Yell their names at them":
            $ wlf.how2 = "names"
        "Try to get up off your knees":
            $ wlf.how2 = "fight"
    $ vn_pass(10)
    jump wlf_queue

## Rung 2, non-con: kneeling at the spring counts as presenting. They queue by rank whether you call or
## not; you yell each man's name as a protest and it comes out as an order anyway. One at a time.
label wlf_queue:
    $ vn_enter(bg="wlf_spring", pc="furious", pc_tag="wlf_pc", cast=[], cg="wlf_queue_line")
    if wlf.how2 == "fight":
        "You get one foot under you. Grey takes your hip in his other hand and puts you back on your knees in the moss, like setting down a cup."
        wlf_grey "\"Queue. By rank.\""
        "Over his shoulder."
    else:
        wlf_you "\"Grey— {i}GREY{/i}— get your hand off me—\""
        wlf_grey "\"Queue. By rank.\""
        "Over his shoulder, like you'd called him up."
    "And they {i}queue{/i}."
    "In order. Strict order. Grey at the front, then Notch, then Bramble, then Old Man, then Scrap at the very back. And the ones waiting don't watch you. They turn to each other and start grooming: Bramble picking at Old Man's ear, Old Man dozing into it. Like it's any other evening."
    wlf_you "\"No. No queue. There is no— {i}Grey{/i}, I swear to—\""
    show cg wlf_queue_grey onlayer cgl
    "The fat hot head of his cock against your hole. Big hands on your thighs, spreading you. Then he pushes in, slow and {i}thorough{/i}, all the way, and doesn't stop till his hips are flush."
    show wlf_pc flushed
    wlf_you "\"{i}Nnnh{/i}— get it out— oh fuck, you're {i}thick{/i}—\""
    wlf_grey "\"Breed you. Take it.\""
    "He fucks like he's checking every inch of you off a list. Deep, deliberate, grinding at the bottom of every stroke. His hand slides to your hip and squeezes, and there's more there to squeeze than there was yesterday."
    wlf_grey "\"Mine now. Full.\""
    wlf_you "\"Ahh— {i}ahh{/i}— stop— {i}Grey{/i}—\""
    "It comes out of you like an order. It comes out like {i}harder{/i}. He goes harder."
    "Off to the side, Notch edges up a place in the queue. Grey snaps his teeth at him without missing a stroke. Notch drops back. Edges up again. {i}Snap.{/i} Drops back, and starts grooming Bramble's ear like he never moved."
    "You laugh, you actually laugh, wild and furious, and Grey slams in hard enough to turn it into a moan."
    "He goes rigid and buries himself. {i}Pulse.{/i} {i}Pulse.{/i} Thick and hot, deep inside you. He pulls out slow, and it runs."
    show wlf_pc furious
    wlf_you "\"Don't— {i}Notch{/i}, don't you {i}dare{/i}—\""
    show cg wlf_queue_notch onlayer cgl
    "You get as far as your elbows. Notch is behind you before you finish his name. Hands on your hips, rough and quick, and he's in you in one shove, sharp and eager."
    wlf_notch "\"My turn. {i}Mine.{/i} Take all. So tight—\""
    vn_sfx "{i}Slap-slap-slap-slap.{/i}"
    show wlf_pc flushed
    "He fucks fast and shallow, all hurry and no finesse, hips going like he's late for something. Your scalp burns, your cock bounces under you, leaking, and you're swearing and moaning at the same time and you can't tell which noise is winning."
    wlf_you "\"Get {i}off{/i}— Notch— {i}nnh{/i}— oh, come {i}on{/i}—!\""
    "He howls. He comes almost at once, a fast hot spurt you feel splash inside you, and pulls out half-hard and panting, and is gone into the dark at a run."
    "Cum runs down your thigh.\n{size=-5}{color=#ff8fa3}▸ The next one's already behind you{/color}{/size}"
    $ vn_pass(10)
    jump wlf_queue_two

## Rung 2, continued: the tribute, then Bramble endless, Old Man courteous, Scrap last and mortified.
label wlf_queue_two:
    $ vn_enter(bg="wlf_spring", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_queue_bramble")
    wlf_you "\"Bramble— {i}Bramble{/i}, no, I'm not—\""
    "Bramble takes his time getting into you. All the time in the world. He sinks through the mess the first two left, thick and deep and slow, and settles in like he lives there."
    wlf_bramble "\"Slow now. Make full.\""
    wlf_you "\"Haa— {i}haaah{/i}— don't— that's— that's {i}deep{/i}—\""
    "He rolls into you. Doesn't pound. {i}Rolls{/i}, long and heavy, hands flat on the small of your back keeping you down, waiting out every gasp and then giving you more."
    show cg wlf_tribute onlayer cgl
    "And Notch comes running back in out of the dark."
    "He's got the best cut off the smoking rack, still hot, fat dripping, and he lays it down on the moss right by your hands. Then he ducks his head and backs off to the end of the line."
    "Gifts go downward. You worked that out on day one, watching the rack."
    "Downward. To {i}you{/i}."
    wlf_you "\"Tribute. {i}Accepted.{/i}\""
    "It falls out of your mouth, with Bramble still rolling into you, half a moan. You rock back onto his cock and you can't stop it."
    "Notch's tail goes like mad."
    wlf_bramble "\"Breed you. Mine.\""
    "Slow, slow, slow, endless, until you're shaking and drooling on the moss and you've stopped saying no and started just saying his name, and when he finally comes it goes on and on, pulse after pulse, and he stays in you rocking till the last of it."
    "When he slides out it pours."
    show wlf_pc furious
    wlf_you "\"Old Man— no— not you {i}too{/i}—\""
    show cg wlf_queue_old onlayer cgl
    "Old Man gets up stiffly and comes over with more manners than anybody else in this cave has shown you. One hand guiding his cock, one hand steady on your hip."
    wlf_old "\"Breed. Courtesy.\""
    show wlf_pc flushed
    wlf_you "\"Oh, {i}courtesy{/i}. That's— {i}ahh{/i}— that's not what courtesy— {i}nnh{/i}—\""
    "You moan it, as he eases in at a careful angle. He's gentle, and steady, and he hits exactly the right spot every single time, and you're filthy about it out loud the whole way through and hating every word you hear yourself say. He finishes with a grunt, pats your thigh, and goes back to the fire."
    "Last. Always last."
    show wlf_pc furious
    wlf_you "\"{i}Scrap{/i}. Scrap, don't— don't you even—\""
    "You yell it at the moss."
    show cg wlf_queue_scrap onlayer cgl
    "Scrap comes up shaking, tail low, cock already slick, and hovers behind you like he's scared to touch."
    wlf_scrap "\"Let me.\""
    "A whisper. Not quite a question."
    "He doesn't wait for the answer. He pushes in. Whines at how wet and open you are."
    wlf_scrap "\"Sorry. Not sorry. So full— want this— {i}want this{/i}—\""
    "He's mortified, and he's rock hard, and he lasts about a heartbeat before he yelps and fills you, nails careful on your hips."
    show cg wlf_queue_cum onlayer cgl
    show wlf_pc flushed
    "And you come on him. On the {i}newest{/i} one. Loud enough to carry to the lake, cock spurting on the moss, clenching down on Scrap of all people." with vnfx("shake")
    "It's everywhere. Running down the backs of your thighs, dripping off your balls, smeared all over your ass. You're {i}soaked{/i} in pack, and you can't stop shaking."
    menu:
        "The moss under your knees. The queue shuffling behind you."
        "They queue up again":
            $ wlf.round2 = True
            jump wlf_queue_sex
        "Lie there dripping and wait for the verdict":
            $ wlf.round2 = False
            $ vn_pass(10)
            jump wlf_low_pack_again

label wlf_queue_after:
    $ vn_enter(bg="wlf_spring", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_queue_round_cum")
    "Another load, deep. The queue shuffles. Somebody's grooming somebody. You're on your face in the moss, hoarse from yelling, still twitching.\n{size=-5}{color=#ff8fa3}▸ Wait for the verdict{/color}{/size}"
    $ vn_pass(10)
    jump wlf_low_pack_again

## The verdict doesn't move ("Low pack." again), and you're irate. The furs move anyway.
label wlf_low_pack_again:
    $ vn_enter(bg="wlf_den_night", pc="furious", pc_tag="wlf_pc", cast=[], cg=None)
    "From the back of the den, the black one speaks for the first time all night. Sleepy. Unmoved. Eyes still shut."
    $ wlf_advance(2)
    wlf_alpha "\"[WLF_VERDICT[2]]\""
    "That's {i}it?{/i}"
    "The {i}whole pack{/i}. In order. In one night. Held down at the spring and taken by every one of them. And the word doesn't move."
    wlf_you "\"Are you {i}kidding{/i} me?\""
    "You twist round, dripping, glaring up the length of the den at him. He doesn't open his eyes."
    show cg wlf_hide_dragged onlayer cgl
    "Then Bramble gets up, picks your hide up off the stone at the mouth, and drags it, with you still half on it, all the way into the crescent. He drops it next to his own furs. He lies down on half of it. His arm goes over your hip like it's always gone there."
    "The word didn't move. The furs did."
    "You don't care. You're glaring at the back wall."
    wlf_you "\"If that's how it works in here, then I want six. Somebody's getting overtaken. Start fighting for it.\""
    "You tell the den, hoarse."
    "Nobody fights for anything. Bramble starts snoring into your neck."
    show screen wlf_furs("night")
    "You lie there and plot.\n{size=-5}{color=#ff8fa3}▸ Sleep, plotting{/color}{/size}"
    hide screen wlf_furs
    call vn_night(5)
    jump wlf_day_three

## ---- DAY 3: rung 2's body; Bramble woken your way; the tail; Gil once; rung 3, Grey ----------------

label wlf_day_three:
    $ vn_enter(bg="wlf_den_night", pc="proud", pc_tag="wlf_pc", cast=[], cg=None)
    "Before dawn. Dark, warm, heartbeats all round you, and Bramble's arm heavy over your hip."
    show screen wlf_furs("wake")
    "You stir under his arm."
    hide screen wlf_furs
    $ wlf_body(2)
    show cg wlf_ears onlayer cgl
    "{color=#ff5fb8}You reach up to scratch your scalp, and your fingers find fur.{/color}"
    "{color=#ff5fb8}Soft. Velvet-soft. High on your head, where the itch was. You follow it up: a tall, furred, pointed {i}ear{/i}. And another on the other side. They twitch under your fingers. They turn toward Bramble's breathing on their own.{/color}"
    show wlf_pc smug
    wlf_you "\"Oh. Oh, {i}yes{/i}.\""
    "{color=#ff5fb8}Your voice comes out light. Lighter than yesterday. Soft at the edges.{/color}"
    "{color=#ff5fb8}You squeeze the base of one ear and a shiver runs all the way down your spine and straight between your legs.{/color}"
    show cg wlf_chest_two onlayer cgl
    "{color=#ff5fb8}Then you take stock. Fast, greedy, hands everywhere.{/color}"
    "{color=#ff5fb8}Your chest: your nipples have gone {i}puffy{/i}, fat and swollen on a soft little swell that wasn't there yesterday. Barely a cup's worth, if it's anything, and it's definitely something. You squeeze, and they're {i}so{/i} sensitive you bite your lip on a moan.{/color}"
    "{color=#ff5fb8}Your waist dips in under your ribs. Your hips flare out under your palms, softer, wider. Your thighs press together all the way up, smooth on smooth. Your face, under your fingertips, is finer: the jaw narrower, the cheekbones sharper. Your hair brushes your collar.{/color}"
    "{color=#ff5fb8}And your cock. You find it hard against Bramble's thigh, and it's {i}tiny{/i}. A cute, stiff little thing that fits in your fist with room to spare. You squeeze it and it leaks.{/color}"
    show wlf_pc flushed
    wlf_you "\"Nnh— look at you. Look at {i}you{/i}.\""
    "You whisper it to yourself."
    "{color=#ff5fb8}And everything's {i}louder{/i}. You put a finger in your mouth without thinking and your mouth goes off like a nerve, hot and wet and greedy, and you moan round your own knuckle so loud Bramble stirs. Your nipples throb every time the furs brush them. Your ass clenches on nothing, hungry, twitching, wanting.{/color}"
    hide cg onlayer cgl
    show wlf_pc smug
    wlf_you "\"{color=#f3c969}[WLF_WORD['ears']]{/color}\""
    "You roll your hips back against Bramble and your ass just {i}opens{/i} for the idea of him, easy and hungry, like it's been doing this for years. Your body's figured out what it's for, and it's very, very good at it."
    "Bramble's hard against you in his sleep. Of course he is."
    menu:
        "Bramble, asleep, hard against you."
        "Wake him with your mouth":
            $ wlf.wake = "mouth"
        "Wake him with your hand":
            $ wlf.wake = "hand"
        "Wake him by grinding back on him":
            $ wlf.wake = "grind"
    $ vn_pass(15)
    jump wlf_wake_bramble

## Your own initiative, between rung 2 and rung 3: the corruption taking hold.
label wlf_wake_bramble:
    $ vn_enter(bg="wlf_den_night", pc="flushed", pc_tag="wlf_pc", cast=[], cg=None)
    if wlf.wake == "mouth":
        show cg wlf_wake_mouth onlayer cgl
        "You wriggle down under the furs in the dark and take him in your mouth."
        vn_sfx "{i}Glk. Glk.{/i}"
        "He's thick and heavy on your tongue, and he wakes up with a groan when you suck. You don't really know how to do this and it doesn't matter: you slobber all over him, hand round the root, lips stretched, moaning around his cock."
        wlf_bramble "\"Messy or clean?\""
        "He mumbles it, half asleep."
        wlf_you "\"Mmh-{i}mmh{/i}.\""
        "You tell him, around him, and he laughs, and comes all over your tongue and your chin and your lips."
    elif wlf.wake == "hand":
        show cg wlf_wake_hand onlayer cgl
        "You reach back under the furs and wrap your hand round him."
        "He wakes up with a rumble when you stroke. Slow, then faster, your thumb working the slick head, his hips jerking into your fist. You've never jerked anybody off but yourself in your life. Your hand learns him in about a minute flat."
        wlf_bramble "\"Messy or clean?\""
        "Into your hair."
        wlf_you "\"{i}Messy{/i}.\""
        "You roll onto your back, and he comes in thick hot ropes all over your stomach and up your chest."
    else:
        show cg wlf_wake_grind onlayer cgl
        "You push your ass back against him and grind. Slow circles. Rolling your soft new hips right into his cock."
        "He wakes up with his hands already on you, groaning into your neck, rutting between your thighs while you squeeze them round him."
        wlf_bramble "\"Messy or clean?\""
        wlf_you "\"Surprise me.\""
        "You moan it, and he comes between your thighs and all over the curve of your ass, hot and sticky."
    wlf_bramble "\"Morning.\""
    "And he goes back to sleep."
    hide cg onlayer cgl
    "You lie there sticky and grinning, and the light at the mouth goes from blue to grey, and something happens at the base of your spine.\n{size=-5}{color=#ff8fa3}▸ Roll over{/color}{/size}"
    $ vn_pass(20)
    jump wlf_tail

## Dawn, day 3: the tail. Two hours of knocking things over.
label wlf_tail:
    $ vn_enter(bg="wlf_den", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_tail")
    "{color=#ff5fb8}A tingle at the base of your spine. Then a {i}weight{/i}.{/color}"
    "{color=#ff5fb8}You roll onto your side and it rolls with you, a beat late: heavy, warm, thick at the root, sweeping out behind you across the furs and somebody's leg.{/color}"
    $ wlf_body("2t")
    "{color=#ff5fb8}A tail.{/color}"
    "{color=#ff5fb8}{i}Your{/i} tail. Brown, plush, a proper banner. It thumps the stone. You didn't tell it to.{/color}"
    wlf_you "\"Ohhh {i}fuck{/i}.\""
    "{color=#ff5fb8}You moan it, and reach back and grab it, and stroking it from root to tip is like stroking yourself, a long shiver right through your hips.{/color}"
    hide cg onlayer cgl
    show wlf_pc smug
    wlf_you "\"{color=#f3c969}[WLF_WORD['tail']]{/color}\""
    show cg wlf_tail_chaos onlayer cgl
    "Then you try to stand up."
    vn_sfx "{i}Whump.{/i}"
    "The tail catches Grey in the shin. You turn to apologise and it smacks Notch's foot. You turn back and it knocks a stone bowl of bones clean off the ledge. {i}Clatter.{/i} Old Man's hip. Scrap, square in the chest."
    show wlf_pc furious
    wlf_you "\"Sorry— sorry, it's— it's {i}new{/i}—\""
    "The black one doesn't wake up. He just reaches behind him and flicks it back at your legs."
    "It takes you all morning to stop knocking things over. Left: it hooks something. Right: it's under your feet. It hits the cave wall hard enough to ring. You swear at it with real feeling."
    hide cg onlayer cgl
    show wlf_bramble sleepy at vn_cast_slot
    "In the end Bramble sits up, takes it in his big hand, and runs his fingers down it, root to tip, slow, until it stops fluffing up."
    wlf_bramble "\"Keep it down. Break Old Man's hip.\""
    wlf_you "\"His hip was {i}already{/i}—\""
    wlf_bramble "\"Keep it down.\"\n{size=-5}{color=#ff8fa3}▸ Out to the ridge{/color}{/size}"
    $ vn_pass(120)
    jump wlf_ridge

## The ridge: heat lands (weather, from rung 3), and Gil offers the walk out (once of two). You
## hesitate: a long moment, then the flavoured no.
label wlf_ridge:
    $ wlf.fit = "own"
    $ vn_enter(bg="wlf_ridge", pc="proud", pc_tag="wlf_pc", cast=[], cg="wlf_ridge_view")
    "You run the day's survey line along the north side of the ridge out of pure habit, notebook in hand, tail swinging behind you, ears swivelling at every bird. Two handfuls of wolfshrooms from under a birch on the way up. They taste sharper today."
    "On the open top of the ridge you stop for the view: trees forever, and the lake far below, a silver knife."
    "And then it hits."
    show cg wlf_heat onlayer cgl
    show wlf_pc flushed
    "{color=#ff5fb8}No warning. Heat. It lands at the root of your spine like a punch and spreads, wet and hot and heavy, up through your belly and down between your legs. Your tiny cock goes rock hard in your trousers. Your ass {i}clenches{/i} on nothing. Sweat breaks out behind your new ears.{/color}"
    "It's not hunger. It's {i}weather{/i}. It doesn't tell you to do anything. It just makes every minute you spend away from that den {i}expensive{/i}."
    hide cg onlayer cgl
    "You're standing there panting when boots crunch on the needles behind you."
    show wlf_gil flat at vn_cast_slot
    wlf_gil "\"Crane? [wlf_pc_name] Crane?\""
    "A ranger. Thirties, cap in one hand, radio on his belt, valley-station badge. He takes in the ears, the tail, the fangs, the very obvious state of your trousers, and he doesn't blink."
    wlf_gil "\"Gil Merrow. Valley station. You missed your check-ins. You all right?\""
    wlf_you "\"Fine. Great. Never better.\""
    "In a voice that's a step too high."
    wlf_gil "\"I can walk you down to the station. There's a phone. It's no trouble.\""
    "You open your mouth to say no, and nothing comes out."
    show cg wlf_gil_moment onlayer cgl
    "A phone. A shower. A bed with nobody's arm over your hip. Nobody's hand on your nape. You look down the ridge, the way he came up, and you {i}stand there{/i}, and the heat sits in your belly, and you think about the hide by the fire with Bramble already lying on half of it."
    "It's a long, long moment."
    menu:
        "Gil, waiting. The way down behind him."
        "Tell him about the survey":
            $ wlf.gil1 = "survey"
            wlf_you "\"Can't. There's a breeding event on. If I pull out now the whole population shifts and I lose the data. I'm close. I'm {i}very{/i} close.\""
            "You tell him, sweating through it. Every word of it is true."
        "Just grin at him":
            $ wlf.gil1 = "grin"
            show wlf_pc smug
            "You just grin at him, fangs and all, ears up, tail going."
            wlf_gil "\"Right. That's a no.\""
        "Tell him straight":
            $ wlf.gil1 = "straight"
            wlf_you "\"No. I'm not done. I'm going back.\""
    hide cg onlayer cgl
    "Gil looks at you a moment longer. Not unkind."
    wlf_gil "\"You took a while there. In case you change your mind. The walk's open. Any time.\""
    "He fishes a battered card out of his shirt pocket and holds it out. You take it. It goes in your pocket."
    wlf_gil "\"Don't get eaten.\""
    hide wlf_gil
    "And he goes back down the ridge."
    show cg wlf_notebook_ridge onlayer cgl
    "You stand there, panting, tail stiff out behind you in the wind, and you get the notebook out with shaking hands."
    show screen wlf_notebook(2)
    "You write it up."
    hide screen wlf_notebook
    hide cg onlayer cgl
    show wlf_pc smug
    "Good. That'll read as professional."
    "And then, out of sheer bloody-mindedness, you finish what you came up here for before you go anywhere. The heat sits on you the whole time. You don't hurry. You have {i}standards{/i}.\n{size=-5}{color=#ff8fa3}▸ Walk back down on your own feet{/color}{/size}"
    $ vn_until(17)
    jump wlf_walk_back

label wlf_walk_back:
    $ vn_enter(bg="wlf_trail", pc="flushed", pc_tag="wlf_pc", cast=[], cg="wlf_walk_down")
    "Downhill. Your own pace. Your own feet."
    "The wind's in your new ears and the sun's on your sweat and every step down the slope makes the heat swing lower in your belly, and you don't run. You read the slope. You pick your footing. You take the switchbacks the long way, because you can."
    "By the time the den comes in sight you're dripping, and your hole's twitching on every step, and you've done the sums."
    show wlf_pc smug
    "Bent for a headlamp: low pack. Held down at the spring by all five: low pack, and the furs moved. Getting taken is the ladder. It's the {i}only{/i} ladder. Fine. Then you'll pick who, and when, and you'll go straight to second."
    hide cg onlayer cgl
    show wlf_grey flat at vn_cast_slot
    "Grey is the first to see you coming. He lifts his head from the fire. Gold eyes, fixed on you, not hurrying.\n{size=-5}{color=#ff8fa3}▸ Walk straight past the alpha, to Grey{/color}{/size}"
    $ vn_pass(10)
    jump wlf_second

## Rung 3, non-con to the break: you bolt for Grey BECAUSE being taken is rank, but he takes it out
## of your hands: face-down, his fist holding your tail aside, his pace. The break comes fast. Past it
## you ask for the knot, and he just looks at you.
label wlf_second:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_grey", "flat")], cg=None)
    "You walk straight in. Past the black one, lying on his furs with his eyes shut. Past Notch, past everybody, right up to Grey."
    wlf_you "\"Second takes first. That's the rule today. I'm on top, I set the pace, and you lie there and—\""
    "Grey stands up."
    $ wlf.fit = "nude"
    show cg wlf_second_down onlayer cgl
    "He takes you by the back of the neck and the waistband, turns you round, and puts you face-down on the hides. Your trousers go. Your boots go. One big fist closes round the root of your tail and holds it aside."
    wlf_grey "\"Presented.\""
    show wlf_pc furious
    wlf_you "\"I was {i}negotiating{/i}— Grey— let go of my {i}TAIL{/i}—!\""
    wlf_grey "\"Stop. Wriggling.\""
    show cg wlf_second_in onlayer cgl
    wlf_grey "\"Breed you.\""
    "He growls it, and he's in you, no preamble at all, one long hard shove to the root."
    wlf_you "\"{i}Hahh—!{/i} Fuck— {i}fuck{/i}— not like— I said {i}I'd{/i}—\""
    wlf_grey "\"Full already?\""
    wlf_you "\"Get— {i}off{/i}— {i}nnh{/i}—\""
    vn_sfx "{i}Slap.{/i}"
    "He doesn't. He fists his other hand in your hair at the nape and catches one of your ears in it, and you yelp and buck, and bucking only slams you back onto him."
    show wlf_pc flushed
    "The heat's {i}screaming{/i}. Every stroke puts it out for a second and lights it twice as high. You're yelling no into the hides and your hips are going back to meet him on every stroke, and the no runs out fast."
    wlf_you "\"Fine— {i}FINE{/i}— promote me, then— harder, you bastard—!\"" with vnfx("shake")
    "He goes harder."
    wlf_you "\"Bite me if you're claiming.\""
    show cg wlf_second_mark onlayer cgl
    "You snarl it, and he does: his teeth close on your shoulder, a mark, not a wound, and you come apart moaning, loud, louder, the whole den listening and none of them looking."
    show wlf_pc smug
    "You twist round to look at him."
    wlf_you "\"Knot me, Grey.\""
    "He looks at you."
    "Gold eyes, level, over your shoulder. And he keeps going. That's all. He doesn't say yes. He doesn't say no. He just looks at you, and fucks you, and the thick base of him stays outside."
    "You file that. You slam back onto him anyway."
    wlf_you "\"Come on— {i}come on{/i}, Grey— you want to keep second? {i}Earn{/i} it—\""
    "He snarls, speeds up, and slams in deep and stays, cock jerking, flooding you hot and thick. You clamp down and ride it out with your teeth bared."
    hide cg onlayer cgl
    "He lets go of your tail, drags one big hand down your spine, and steps back looking very satisfied with himself.\n{size=-5}{color=#ff8fa3}▸ Roll onto your back and point at Bramble{/color}{/size}"
    $ vn_pass(10)
    jump wlf_second_bramble

label wlf_second_bramble:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_bramble", "grin")], cg="wlf_second_bramble")
    "You roll over. Legs spread. Your little cock stiff and leaking, your hole wet with Grey."
    wlf_you "\"Bramble. You're next. Get your hands dirty.\""
    "Bramble kneels between your knees with his crooked grin and lays one big hand flat on your chest, feeling your heart go."
    wlf_bramble "\"Eager today. Messy or clean?\""
    wlf_you "\"Figure it out.\""
    "You hook your own knees and haul them up. He nudges your tail out of the way and slides in, long and curved, all the way, and starts to grind."
    wlf_bramble "\"So open. Take it. Mine now.\""
    wlf_you "\"Harder, Bramble— don't make me do it for you—\""
    show cg wlf_second_howl onlayer cgl
    show wlf_pc flushed
    "He wraps a fist round your tail and {i}tugs{/i} with every thrust, and the other hand palms your chest, and you're gone. You howl. Actually howl. Your tail's thrashing in his grip and your cock's dribbling all over your stomach and you can't stop making noise."
    wlf_bramble "\"Breed you. Fill you. So hot. {i}Take all of it.{/i}\""
    wlf_you "\"Bet you break before I do—\""
    "He breaks first. Slams in to the hilt and comes, groaning into your neck, and it's so much on top of Grey's that it squelches out round him.\n{size=-5}{color=#ff8fa3}▸ Snap your fingers at Scrap{/color}{/size}"
    $ vn_pass(10)
    jump wlf_second_scrap

## The verdict mid-ride: "Good pack." Third, you decide, behind Grey. "Tomorrow, second."
label wlf_second_scrap:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[("wlf_scrap", "shy")], cg=None)
    "Scrap's been watching from the edge with his cock in his fist and his face on fire."
    "You spread yourself with both hands. Cum drips onto the hides."
    wlf_you "\"You want it? Come and get it.\""
    show wlf_scrap eager
    wlf_scrap "\"Can— can I—\""
    wlf_you "\"{i}Do it.{/i}\""
    show cg wlf_second_scrap onlayer cgl
    "He sinks in, whimpering, and starts pounding like his life depends on it."
    wlf_scrap "\"Breed you, want this, so full, {i}yours{/i}—\""
    show cg wlf_ride_scrap onlayer cgl
    "It's not enough. You hook a leg round his back and {i}roll{/i} him, flat on his back in the furs, and come up on top without letting him slip out, and sink all the way down."
    wlf_you "\"{i}Ahhh—{/i} there— now {i}you{/i} stay still—\""
    "You ride him. Hard. Hands on his chest, hips slamming, tail lashing."
    wlf_you "\"Faster. No— I'm doing faster, {i}you{/i} hold on. Harder. Look at me. You getting off yet? Prove you belong in here, Scrap. {i}Fill me up.{/i}\""
    "He whines, high and helpless. His hips stutter up into you and he comes, spurt after spurt, both hands clamped on your soft hips while you ride him straight through it and grind down for more."
    "And from the back of the den, eyes shut, the black one rumbles:"
    $ wlf_advance(3)
    wlf_alpha "\"[WLF_VERDICT[3]]\""
    "A promotion. Plain as sunrise. Third, then. Behind Grey."
    wlf_you "\"Third's not good enough. Tomorrow, second. After that, first. I'm setting the schedule. Get ready.\""
    "You announce it to the whole den, still riding."
    show cg wlf_two_hides onlayer cgl
    "Grey gets up, takes a second hide off the pile, and drops it inside the crescent, between his furs and the fire. Right on top of yours."
    menu:
        "Your two hides by the fire. Grey, watching you."
        "Grey's got your tail in his fist again":
            $ wlf.round3 = True
            jump wlf_second_sex
        "Collapse on your new hides":
            $ wlf.round3 = False
            $ vn_pass(30)
            jump wlf_second_night

label wlf_second_after:
    $ vn_enter(bg="wlf_den", pc="smug", pc_tag="wlf_pc", cast=[], cg="wlf_second_round_cum")
    "One more load, and you're done, and you're {i}so{/i} done, and you're grinning.\n{size=-5}{color=#ff8fa3}▸ Collapse on your new hides{/color}{/size}"
    $ vn_pass(20)
    jump wlf_second_night

label wlf_second_night:
    $ vn_enter(bg="wlf_den_night", pc="smug", pc_tag="wlf_pc", cast=[], cg=None)
    "The heat goes out of you like a tide, slow, leaving you heavy and warm and pleased with yourself."
    "You called it. Onset with the tail. You'll call the next one too. And next time {i}you{/i} pick the pace."
    show screen wlf_furs("night")
    "You stretch out on both hides.\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    hide screen wlf_furs
    call vn_night(7)
    jump wlf_day_four
