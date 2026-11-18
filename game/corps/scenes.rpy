## The Pink Ranger's written scenes (rungs.twee and ending.twee; the director scenes written out as
## beats, as the other Ren'Py routes do: open, mid, peak, your climax (its own frame), hers). The
## consent table is the spec's Non-con beats (owner, 2026-10-19/20): the fitting room, the channel
## and the claiming are non-con, and only the claiming flips (Anya is the only partner Leo comes to
## want); the changing room never flips; the knees, the counter, the Nova and after-hours are
## consensual. Anya never asks. No tears; the only threat is the team hearing.

## ==== RUNG 1: the first night (solo) ============================================================
## The nipples won't stop. The old way, and your other hand on your chest sets it off.
label cp_first_night:
    $ vn_set_time(23, 0)
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_flat", pc="flushed", pc_tag="cp_pc", cg="cp_night1_bed")
    "Bed. Lights off. T-shirt off, because the T-shirt is torture."
    "It doesn't help. The {i}air{/i} is torture. Your nipples are puffy and hot and throbbing, two little points of want, and every time you breathe they throb."
    "Fine. The old way."
    "You shove your boxers down and grab your cock. Stroke. It's hard in seconds. It's good. It's normal. It's..."
    "Not enough."
    show cg cp_night1_touch onlayer cgl
    "Your other hand drifts up. Not on purpose. Just to... rub. Just once. Your fingertip brushes one nipple."
    cp_me "\"{i}Ohh{/i}—\""
    "Your cock jumps in your fist. You do it again. Then you pinch."
    cp_me "\"Ahh— {i}ahh{/i}— what— what the {i}fuck{/i}—\"" with vnfx("shake")
    "You can't stop. Stroke and pinch. Stroke and pinch. Your hips come off the mattress. The noises coming out of you are high and wet and nothing like you."
    "Your fingers know exactly how hard to pinch. Nobody ever taught you that."
    "You let go of your cock to see what happens. Just the nipple. Just rolling it."
    "Your cock jerks on its own, untouched, leaking all over your stomach."
    cp_me "\"Oh {i}no{/i}. Oh no, oh no, that's— {i}ahh{/i}—\""
    "You grab it again, fast, frantic, pumping like you can drown the other thing out. One hand on your cock. The other one won't leave your chest."
    cp_me "\"Fuck— {i}fuck{/i}, yes— why does that— why does that feel— {i}ahh{/i}—!\""
    show cg cp_night1_cum onlayer cgl
    "You roll the nipple hard between your fingers and that's it. That sets it off. You come from your cock, hard, rope after rope up your stomach, moaning at the ceiling loud enough for the neighbours." with vnfx("shake", "flash")
    cp_me "\"{i}Nnnh— ahhh{/i}—!\""
    "And then you're lying in it, panting, and your hand's still on your chest. Still rubbing. Little circles. You tell it to stop."
    cp_me "\"Stop. {i}Stop{/i}— nnh—\""
    "It doesn't stop. Neither do you. Not for a long time."
    hide cg onlayer cgl
    $ cp.fit = "own"
    return

## ==== RUNG 2: the fitting room (non-con, "That's one") ===========================================
## Chest and cock together, under her hands, and you can't tell which. Anya stays dressed.
label cp_fitting:
    $ vn_enter(bg="cp_mall", pc="nervous", pc_tag="cp_pc", cast=[("cp_anya", "neutral")])
    call cp_who_touched
    "Anya frog-marches you through the shopping centre by the elbow. Past the food court. Past a hen party."
    "Straight into a lingerie shop full of lace and grown women who look up and smile at you."
    cp_anya "\"You're at least a C. You'll outgrow it fast.\""
    "She looks at your hoodie like it's sheet metal. She shoves an armful of bras at you and pushes you into a fitting room, and comes in after you, and snaps the curtain shut."
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_fitting", pc="shocked", pc_tag="cp_pc", cast=[("cp_anya", "smirk")])
    cp_anya "\"Top off.\""
    "You peel off the hoodie. The T-shirt. You stand there with your tits out under the shop lights, round and heavy, nipples puffy and dark."
    cp_anya "\"Arms up.\""
    show cg cp_fit_band onlayer cgl
    "You put your arms up. She steps behind you and wraps the band round you and hooks it at the back. Practical. Fast."
    "Then her hands stay."
    "Her thumbs drag up under the cups. She lifts. Weighs. Squeezes, not at all practical."
    cp_me "\"Oi— that's not— {i}nnh{/i}—\""
    "You grab her wrists and push. It's like pushing a car. Her hands don't move off your tits an inch."
    cp_anya "\"Hands down, Leo.\""
    cp_me "\"Anya— get {i}off{/i}—\""
    show cg cp_fit_bite onlayer cgl
    "In the mirror, her eyes find yours. She hooks one finger in the cup and rolls it down, slow, and your nipple pops out, swollen and pink. You're still pulling at her wrist."
    "She leans in and sinks her teeth into your neck."
    cp_me "\"{i}Ahh{/i}—!\"" with vnfx("shake")
    cp_anya "\"This is what you're becoming. Not a costume. You.\""
    "Into your skin."
    show cg cp_fit_hand onlayer cgl
    "She peels your hand off her wrist. Puts it on your own tit. Holds it there with hers and {i}squeezes{/i}."
    cp_anya "\"Feel that? Your hand. Your tit.\""
    cp_me "\"No— I don't— Anya, the {i}CLERK{/i}— she's right {i}there{/i}—!\""
    cp_anya "\"Then keep your voice down.\""
    "You don't. You can't. She works your fingers round the nipple. Rolls it. Pinches it with your own fingertips."
    vn_sfx "Tweak."
    "Your cock is rock hard in your boxers and grinding back against her jeans, and you're telling it to stop, and you're telling her to stop, and your chest is on fire and you can't tell which one is making you moan."
    cp_me "\"Stop— {i}stop{/i}— ahh— {i}ahh{/i}— I don't want to— I'm gonna— Anya, I'm gonna—\""
    "She slides her free hand up and presses her palm flat on your breastbone. Right over your heart. Pins you back against her by it."
    cp_anya "\"Go on, then.\""
    cp_me "\"No— {i}no no no{/i}—\""
    show cg cp_fit_cum onlayer cgl
    "You come. In your boxers. Standing up. Her hand flat on your chest and your hand trapped on your own tit and your mouth wide open, and it's {i}loud{/i}." with vnfx("shake", "flash")
    cp_me "\"{i}Ahhhh— nnnh— ANYA{/i}—!\""
    vn_sfx "Knock knock."
    cp_clerk "\"Need another size in there?\""
    cp_anya "\"We're fine.\""
    "She calls it back. She tugs the cup back up over your nipple, smooths it, pats it."
    cp_anya "\"That's one.\""
    "Just for you. Then she walks out, slow, not looking back."
    hide cg onlayer cgl
    $ cp.fit = "own"
    "You leave the shop wearing the bra."
    $ vn_set_time(23, 0)
    $ vn_enter(bg="cp_flat", pc="nervous", pc_tag="cp_pc", cg="cp_fit_bag")
    "That night there's a second bag on your bed. You don't remember her putting it there."
    "Inside: panties. Pink lace. Your size. She picked them."
    "You put them on. Just to see. Your cock tucks into the lace like it's been doing it for years, and the elastic sits on your new hips exactly right."
    cp_me "\"It's fine.\""
    "You tell the mirror. Your voice wobbles."
    hide cg onlayer cgl
    return

## ==== RUNG 3: the open channel (non-con, her voice, "That's two") ================================
## The comm won't mute; the drawer doesn't help; she talks you over the edge twice while you tell
## her to stop. You come from your chest alone.
label cp_channel:
    $ vn_set_time(23, 0)
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_flat", pc="flushed", pc_tag="cp_pc", cg="cp_chan_bed")
    "Bed. Bra off. Hands on your chest before the light's even out."
    "It's the only way that works now. You know it. You stopped pretending a week ago. Your cock's a soft little thing in your panties that barely notices."
    "The morpher's on the nightstand. Its comm light is on."
    "It's always on."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Sweetheart.\""
    "You freeze. Both hands full of tit."
    show cp_red neutral at vn_cast_slot
    cp_red "\"I see you.\""
    "Anya's voice, low, a little rough, right in the room."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Well. I hear you. Every night, Lily. Every single night.\""
    cp_me "\"You— you can {i}hear{/i}—\""
    call cp_who_touched
    show cg cp_chan_mash onlayer cgl
    "You yank your hands off your chest. Grab the morpher. Mash the comm button."
    vn_sfx "Click. Click. Click."
    "The light stays on."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Doesn't mute, Lily. Red's channel. Regulation.\""
    cp_me "\"Then turn it {i}off{/i}— Anya, turn it off, I'm not doing this with you {i}listening{/i}—\""
    vn_sfx "Slam."
    "You shove it in the nightstand drawer and slam it. Her voice comes straight through the wood like she's lying next to you."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Both hands. Cup them. Like I showed you.\""
    cp_me "\"No.\""
    show cp_red neutral at vn_cast_slot
    cp_red "\"Squeeze.\""
    show cg cp_chan_squeeze onlayer cgl
    cp_me "\"I said {i}no{/i}—\""
    "Your hands are back on your tits. You didn't put them there. Your chest put them there; it's been dragging them back all week. You squeeze."
    cp_me "\"Hhn— {i}dammit{/i}—\""
    show cp_red neutral at vn_cast_slot
    cp_red "\"Thumbs on the nipples. Slow circles. Slower.\""
    cp_me "\"Stop {i}talking{/i}— stop telling me—\""
    "Your thumbs are already doing it. Slow. Slower. Exactly the speed she said."
    cp_me "\"Ahh— Anya— {i}ahh{/i}— shut {i}up{/i}—\""
    show cp_red neutral at vn_cast_slot
    cp_red "\"Now pinch.\""
    cp_me "\"I'm {i}not{/i}— {i}nnh{/i}—!\""
    vn_sfx "Tweak." with vnfx("shake")
    "Your back comes off the mattress."
    show cp_red neutral at vn_cast_slot
    cp_red "\"You feel that? Get used to it.\""
    "She sounds like she's smiling."
    "It builds. Nowhere near your cock."
    "All of it in your chest, in your nipples, rolling and swelling under your fingers, and her voice coming through the drawer telling you {i}harder{/i}, {i}don't you dare stop{/i}, {i}good girl{/i}."
    cp_me "\"I'm not— your {i}girl{/i}— Anya, stop, I don't want to come for you— I don't— from my— just from my— {i}ANYA{/i}—!\""
    show cg cp_chan_cum onlayer cgl
    "You come. From your tits alone. Back arched, heels dug into the mattress, screaming her name into her channel. Your cock doesn't even twitch." with vnfx("shake", "flash")
    "She listens to all of it."
    "You lie there panting. Your nipples are still throbbing. Your fingers are still going, little circles, and every circle makes you twitch."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Again.\""
    cp_me "\"No— no, I can't— it's too— leave me {i}alone{/i}—\""
    show cp_red neutral at vn_cast_slot
    cp_red "\"Again, Lily.\""
    cp_me "\"It's {i}LEO{/i}—\""
    "Squeeze. Roll."
    cp_me "\"{i}Ahh{/i}—\""
    show cg cp_chan_curl onlayer cgl
    "So it happens again. Slower this time, because she makes it slower. Squeeze. Roll. Pinch and hold."
    "She counts your breaths for you in her low voice and tells you exactly when to tug, and you tell her to stop on every count, and your fingers tug on every count."
    "The second one comes up even bigger than the first, a deep shuddering ache that curls you up on your side with both hands crushed to your chest."
    cp_me "\"Stop— stop— {i}ahh{/i}— Anya— Anya, {i}please{/i}— please let me— {i}please{/i}—\""
    show cp_red neutral at vn_cast_slot
    cp_red "\"Let me hear it.\""
    cp_me "\"{i}AHHH{/i}—!\"" with vnfx("shake", "flash")
    "She hears it. So, probably, do the neighbours."
    show cp_red neutral at vn_cast_slot
    cp_red "\"That's two. Good girl. Go to sleep.\""
    "The comm light stays on."
    hide cg onlayer cgl
    $ cp.fit = "own"
    return

## ==== RUNG 4: the panties (the blackmail, finished out loud; you never say yes) ================
label cp_panties:
    $ vn_enter(bg="cp_lockers", pc="nervous", pc_tag="cp_pc", cast=[("cp_anya", "neutral")])
    call cp_who_touched
    "\"We'll talk\" is the locker room, after everyone else has gone."
    "Anya shuts the door with her heel. Leans on it. She doesn't say anything for a while. She just looks at you, the way she looked at you in the vines."
    show cg cp_panties_hold onlayer cgl
    "Then she holds something out. Pink. Lace. Tiny."
    cp_me "\"No.\""
    "Before she's even opened her mouth."
    cp_anya "\"You wear these. Every day. Or the whole team hears about your little accidents.\""
    cp_me "\"My— my {i}what{/i}—\""
    cp_anya "\"The fitting room. In your boxers, with the clerk at the curtain.\""
    "She ticks them off on her fingers."
    cp_anya "\"Every night on my channel. Twice, last Thursday. The vines, but the whole city's had that one.\""
    "She smiles."
    cp_anya "\"Tobi would {i}love{/i} the fitting room. He'd have a theory by lunch.\""
    "Your face goes hot all the way down your neck."
    menu:
        "\"...Fine.\"":
            cp_me "\"...Fine.\""
            "You mutter it at the floor."
            cp_anya "\"Fine what?\""
            cp_me "\"...Fine. I'll wear them.\""
        "Snatch them out of her hand":
            vn_sfx "Thwip."
            "You snatch them out of her hand so hard the lace snaps against your fingers."
            cp_anya "\"Good girl.\""
            "Like you've said thank you."
        "\"You wouldn't—\"":
            cp_me "\"You wouldn't—\""
            show cg cp_panties_phone onlayer cgl
            "Anya pulls her phone out and opens the team chat. Her thumb starts typing."
            vn_sfx "Tap tap tap."
            "{b}So the fitting room on Saturday—{/b}"
            cp_me "\"OKAY. Okay! Give them {i}here{/i}—\""
            "She deletes it one letter at a time, watching you, and holds them out."
    cp_anya "\"Now. Here. Where I can see.\""
    cp_me "\"Anya—\""
    cp_anya "\"Little accidents, Lily.\""
    show cg cp_panties_on onlayer cgl
    "So you do it in front of her. Jeans down. Boxers down. Your little cock out under the strip light while she watches, arms folded."
    "Then the lace, slow, up your thighs, over the new hips, thumbs hooked in it, and it hugs everything and tucks your cock away like it's been doing it for years."
    "You hate how it feels. Your nipples go hard at how it feels."
    cp_anya "\"Turn round.\""
    "You turn round. She looks at your ass in them for a long, long time."
    cp_anya "\"Every day. I'll check.\""
    hide cg onlayer cgl
    "When she turns to go, you notice what she's wearing. Cargo pants. Baggy, heavy, nothing like the skinny jeans she's always lived in."
    show cp_tobi neutral at vn_cast_slot
    cp_tobi "\"Whoa, Red. Tactical wardrobe upgr—\""
    "In the corridor, Tobi notices too. Anya looks at him. Just looks."
    cp_tobi "\"—never mind.\""
    "He goes very interested in a vending machine."
    $ vn_enter(bg="cp_hub", pc="neutral", pc_tag="cp_pc", cast=[("cp_vee", "neutral")], cg="cp_rookies")
    "That afternoon two new rangers report to the Hub. Rookies. Vee, all shoulders and grin, and Naomi, sharp and amused."
    cp_vee "\"Oh my god, you're Lily. From the news. The tower! The {i}singing{/i}!\""
    "They've never met anyone called Leo. As far as they're concerned there's never been anyone here but Lily."
    hide cg onlayer cgl
    return

## ==== RUNG 5: the claiming (MANDATORY; non-con, flipping when you come untouched) ===============
## Her door, her bed, her fingers while you say no ("That's three"), the reveal, and she doesn't
## ask. It opens non-con and flips at the break: "...Don't stop. Don't you DARE stop."
label cp_lily_door:
    $ vn_enter(bg="cp_anyaflat", pc="flushed", pc_tag="cp_pc", cast=[("cp_anya", "hungry")], cg="cp_door_kiss")
    vn_sfx "Click."
    "Her door clicks shut. You lean back against it, dizzy."
    cp_me "\"It's Leo. My name's—\""
    "It comes out tiny."
    cp_anya "\"Lily suits you.\""
    "She pins you to the door and kisses you. Hard. Hungry."
    "Her tongue in your mouth and her thigh between your legs and both her hands up under the sweater, mapping every curve that's been taunting her all day." with vnfx("shake")
    cp_me "\"Mmh— {i}mmnh{/i}— Anya— wait— I only said I {i}liked{/i}—\""
    cp_anya "\"All day. I've watched you be Lily all day. Bedroom.\""
    "She growls it against your lips."
    cp_me "\"I didn't say— Anya— I didn't say {i}bedroom{/i}—\""
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_anyabed", pc="shocked", pc_tag="cp_pc", cg="cp_claim_bed")
    "She strips you on the way anyway. Skirt. Sweater. You grab at the panties and she peels them down your thighs round your fingers, damp lace and all."
    "She pushes you back on her bed in nothing but the white stockings."
    "Then she stops, and looks."
    "The tits. The hips. The thick soft thighs. And between them, your cock. Tiny. Soft. Tucked into the crease of your thighs like it's embarrassed."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"That? Not interested. Roll over.\""
    "She shrugs. You don't. She flips you over by the hip herself."
    show cg cp_claim_fingers onlayer cgl
    "Face-down. She hauls your knees up under you. Ass in the air. You try to drop it flat and her palm lands on the small of your back and holds it there."
    "Her spit, warm, and two fingers pressing in."
    cp_me "\"Ahh— Anya— no— {i}no{/i}, not— not {i}there{/i}—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Keep those hips up, Lily.\""
    "She scissors you open. Slow. Your tits drag on her sheets with every push of her hand, and that's somehow worse, sparks right down to where her fingers are."
    cp_me "\"Nnh— {i}hhh{/i}— stop— it's so weird— it's so {i}weird{/i}— take them out—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"No.\""
    "Deeper. Curls. Finds something inside you that makes your whole body jolt."
    cp_me "\"{i}OH{/i}— oh, what— what is— {i}ahh{/i}— don't— don't touch {i}that{/i}—!\"" with vnfx("shake")
    show cg cp_claim_fingercum onlayer cgl
    "She touches that. She curls again. And again. And you come."
    "Just like that, on her fingers, face mashed in her pillow, still saying no into it, your tiny cock dribbling helplessly onto her sheets. You didn't even feel it coming." with vnfx("flash")
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"That's three.\""
    "She doesn't stop. Behind you there's a zip. Fabric."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Look.\""
    show cg cp_claim_reveal onlayer cgl
    "You look back over your shoulder."
    "She's naked. And between her legs is a cock. Huge. Flushed. Thick as your wrist and heavy, veined, the head dark and glistening. She lets it slap down into her palm."
    vn_sfx "Thwap."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"You're not the only one the Grid's been adapting. Every morph, it gets bigger. That's the only thing the Red suit changes.\""
    "She strokes it, once, slow."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Matched pair, Lily. You get greedier. I get more to give.\""
    cp_me "\"No— Anya, no, that won't— that won't {i}fit{/i}—\""
    "She kneels up behind you. Her hand pins the back of your neck to the pillow. The fat head of it rests against your hole, hot and slick."
    "She doesn't ask."
    menu:
        "Grab the sheets":
            "You grab the sheets in both fists like they'll hold you up the bed."
        "\"Anya, WAIT—\"":
            cp_me "\"Anya, WAIT—\""
            "She doesn't."
        "Bite the pillow":
            "You bite the pillow. You bite down hard and it doesn't help at all."
    show cg cp_claim_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    "In. The fat head of her pops past the ring and your whole body jolts on the sheets."
    cp_me "\"Anya— Anya, NO— not in— {i}hnngh{/i}— not THERE—!\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Hips up. I didn't ask.\""
    "Her palm on the small of your back, holding it down. Inch by inch she sinks in. It doesn't hurt. It's big, stretching, {i}full{/i}, so full your mouth hangs open, and it doesn't hurt at all."
    cp_me "\"Get off— Anya, get {i}off{/i}— it's too big, it doesn't {i}go{/i} there—!\""
    show cg cp_claim_mid onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    "She starts to move. Slow, deep strokes, and every one drags your tits across her sheets."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Tell the team, then. Go on. Tell them how wet you are.\""
    cp_me "\"I'm not— I'm not your girl— I'm {i}LEO{/i}—\""
    "She pushes deeper."
    cp_me "\"{i}Ahh{/i}—!\""
    "You claw at her sheets and try to crawl up the bed. She hauls you back by the hips."
    vn_sfx "Shlk."
    cp_me "\"N-{i}no{/i}—!\""
    "It's hitting something. Every stroke. The thing her fingers found."
    cp_me "\"Why is it— why is it HER cock that— {i}AHH{/i}—!\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Stop squirming, Lily. You'll come from my cock or not at all.\""
    cp_me "\"It's not— this isn't— {i}ohh{/i}— don't hit that again— don't— {i}ahh{/i}— again—\""
    "Your tiny cock is dribbling on her sheets and nobody's touched it."
    cp_me "\"That's not— that's not {i}me{/i}— {i}hah{/i}—\""
    show cg cp_claim_peak onlayer cgl
    vn_sfx "Pap pap pap pap." with vnfx("shake")
    "She pins both your wrists to the small of your back with one hand."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"There. Now you can't lie about it.\""
    cp_me "\"Don't— don't tell them— I'll wear ANYTHING— just don't STOP—\""
    cp_me "\"Anya— Anya, I'm gonna— from my {i}ass{/i}— I'm gonna come from my {i}ASS{/i}—!\""
    show cg cp_claim_cum onlayer cgl
    "It comes up from nowhere, from where she is, and you come untouched, screaming into her pillow." with vnfx("shake", "flash")
    "It goes on and on. And when it lets go of you, the no's gone with it."
    cp_me "\"...Don't stop.\""
    "You hear yourself say it. Then louder, into the pillow, shoving back on her."
    cp_me "\"Don't you DARE stop.\""
    show cg cp_claim_finish onlayer cgl
    "She comes with a growl, hips mashed to your ass, pulse after hot pulse, and she holds you pinned by the hips until she's finished."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Feel that? That's where you live now. You'll come from my cock alone.\""
    "In your ear."
    "And she doesn't stop."
    show cg cp_claim_fold onlayer cgl
    "She rolls you over and folds you in half, your knees by your ears, and slides back in, watching your tits bounce."
    cp_me "\"Ahh— {i}ahh{/i}— it's so {i}deep{/i}— Anya, it's so deep like this—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Look at you. Look how the Grid built you. Look how you take it. You were made for this, Lily. You were made for {i}me{/i}.\""
    "She's talking the whole time now, low, never stopping."
    show cg cp_claim_edge onlayer cgl
    vn_sfx "Pap, pap, pap." with vnfx("shake")
    "She drags you to the edge of the bed and takes you from behind with a fist in your hair. The headboard bangs the wall. Somewhere through it a neighbour bangs back."
    "Neither of you cares."
    "Your hips find her rhythm before you do. You never practised that. You're shoving back on every thrust like you were built knowing how."
    cp_me "\"Okay— OKAY— yours— I'm YOURS, just— harder—!\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Who said anything about telling? Little accidents, Lily. This one's mine.\""
    "She laughs into your hair."
    "She pinches your nipples while she's buried in you and you come again, screaming, from that, from {i}her{/i}, and your cock just twitches and drools on her sheet like it isn't even part of this." with vnfx("flash")
    "She gathers your hair up in her fist, all of it, the salon waves, and holds you up by it."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"By the time this grows out, you won't remember how to say {i}Leo{/i}. Say you're mine.\""
    cp_me "\"I'm yours— I'm {i}yours{/i}— {i}ahhh{/i}—!\""
    "She comes again, buried to the hilt, and it floods you so hot you feel it squelch out round her. So do you." with vnfx("flash")
    show cg cp_claim_ride onlayer cgl
    "Then she gets you on top of her and holds your hips and moves you on her, slow, while she sucks on your tits, and you come again just from that and collapse on her chest, laughing and moaning at once, still twitching round her."
    "By the time the window goes grey you've lost count. She hasn't."
    hide cg onlayer cgl
    call vn_night(8)
    return

label cp_lily_morning:
    $ cp_locker(5)
    $ vn_enter(bg="cp_anyabed", pc="flushed", pc_tag="cp_pc", cg="cp_morning_spoon")
    "You wake up stretched and glowing and full of her, in her bed, with her arm across your waist and her cock hard against your ass."
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Morning.\""
    "Into your neck. She slides into you. Still slick from last night. Easy."
    cp_me "\"Ahh— {i}Anya{/i}— I'm still so {i}full{/i}—\""
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"I know. Go back to sleep if you want.\""
    "She rocks, slow and lazy, spooned up behind you, one hand cupping your tit."
    "You don't want."
    "You push back on her, whimpering, and she takes you like that, slow, until you come again with your face in her pillow and she comes in you with a long, satisfied groan." with vnfx("flash")
    show cg cp_morning_brush onlayer cgl
    "She sits you up between her knees and brushes your hair out. Long strokes. All the salon waves gone soft and tangled."
    cp_me "\"Mmh.\""
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Hold still.\""
    "She keeps going until it shines. Then she puts the brush in your hand and closes your fingers round it."
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Keep it. In your locker. Where the clippers used to live.\""
    hide cg onlayer cgl
    $ cp.fit = "lily"
    return

## ==== RUNG 5: the changing room (non-con, her hand over your mouth, NO flip) ==================
## After Echoplasm. She's still burning over Kyle's patch-up. The team's the other side of the door.
## (The built route's decline link went with the non-con beats, 2026-10-19/20: it always plays.)
label cp_changing_room:
    $ cp.fit = "lily"
    $ vn_enter(bg="cp_lockers", pc="nervous", pc_tag="cp_pc", cast=[("cp_anya", "hungry")])
    call cp_who_touched
    "The changing room. Everyone else is still in the corridor, laughing about the double."
    "Anya isn't laughing. She's got you backed up against the lockers."
    cp_anya "\"He doesn't get to touch you like that.\""
    cp_me "\"Who— Kyle? He didn't even—\""
    cp_anya "\"He doesn't get to {i}want{/i} to.\""
    show cg cp_change_bench onlayer cgl
    "She spins you round by the hips and bends you over the bench. Yanks your skirt up. Your panties down."
    cp_me "\"Anya— Anya, not {i}here{/i}— they're right {i}there{/i}—\""
    "Out in the corridor Tobi's doing an impression of the double. Everybody's howling."
    "In here, Anya's spitting in her hand. Slicking her cock."
    "Pressing two wet fingers into you, quick and rough, while you push up off the bench and she pushes you straight back down by the nape."
    cp_me "\"Stop— I'm serious— Vee's {i}right outside{/i}— {i}mmh{/i}—\""
    cp_anya "\"Every time he looks at you, you think about this. Got it?\""
    "Low, working you open."
    cp_me "\"No— I'm not— {i}ahh{/i}—\""
    "Her other hand comes round and clamps over your mouth. Her cock nudges against you, hot and heavy and huge."
    menu:
        "Bite down on her fingers":
            "You bite down on her fingers. She just presses them in harder."
        "Grab the edge of the bench":
            "You grab the edge of the bench and hang on."
        "Kick at her shins":
            "You kick back at her shins. She steps between your feet and spreads them wider."
    show cg cp_change_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    "In. All of her, in one long push, and the bench creaks."
    cp_me "\"Mmf— {i}mmmf{/i}— Anya— nnf— {i}not HERE{/i}—!\""
    "It comes out through her fingers as mush."
    vn_sfx "Creak. Creak."
    "The bench creaks under you on every thrust."
    "Your tits are squashed flat on the wood and dragging, back and forth, and every drag sends a spark straight to where she's buried in you."
    cp_me "\"Mmh— they'll— {i}mmf{/i}— they'll HEAR—!\""
    "You twist your face against her palm. Her hand clamps tighter."
    cp_anya "\"Shh. They'll hear you. Good girl. {i}Quiet{/i}.\""
    "In your ear. Out in the corridor someone asks where Lily's got to. Anya fucks you harder."
    cp_me "\"Mmmh— {i}mmnh{/i}—!\""
    "It was meant to be no. It comes out a moan, wet, into her palm."
    "Out in the corridor Tobi gets a laugh. In here you moan so loud behind her hand the bench shakes."
    show cg cp_change_peak onlayer cgl
    "Your hips push back. You didn't tell them to."
    cp_me "\"Hhnf— {i}hnnf{/i}— {i}mmmmh{/i}— mmf— {i}MMMH{/i}—!\""
    "Nothing but noise through her fingers now, loud, begging. You're sucking on her fingers. You don't know when that started."
    show cg cp_change_cum onlayer cgl
    "You come untouched. Into her palm, practically, screaming behind her hand. Your cock's a soft afterthought. Your tits did all of it, crushed on the bench." with vnfx("flash")
    "She comes grinding hard against you with her teeth in your shoulder, while Vee laughs at something just the other side of the door."
    "Every noise you made started as {i}no{/i}. None of them came out as one."
    hide cg onlayer cgl
    "She takes her hand off your mouth at last."
    cp_me "\"I said not {i}here{/i}.\""
    "You hiss it, and your voice comes out wrecked."
    cp_anya "\"I heard.\""
    "She pulls your panties back up, smooths your skirt, and walks out into the corridor. You follow, legs shaking."
    show cp_kyle neutral at vn_cast_slot
    "She wipes a smear of soot off your cheek with her thumb, in front of everyone."
    cp_anya "\"Good girl.\""
    "Just loud enough. Nobody comments. Kyle finds somewhere else to look."
    return

## ==== RUNG 5: "On your knees, Li—" (consensual; the corruption landing) =========================
label cp_knees:
    $ vn_set_time(23, 0)
    $ vn_enter(bg="cp_anyaflat", pc="grin", pc_tag="cp_pc", cast=[("cp_anya", "smirk")])
    "You and Anya are \"dating\". That's the word. You pass it back and forth like a joke, and it runs your whole life."
    "Her sofa, late. Your head in her lap. Her fingers in your hair. The bulge under her joggers getting heavier against your cheek."
    cp_anya "\"On your knees, Li—\""
    show cg cp_knees_rug onlayer cgl
    "You're already off the sofa. Down on the rug between her thighs before she gets to the end of your name, and neither of you says anything about how fast that was."
    "She hooks a thumb in her waistband and tugs, and it springs out and slaps against her stomach."
    vn_sfx "Thwap."
    "Huge and flushed and already wet at the tip."
    cp_me "\"Hi.\""
    "You tell it, and giggle, and she laughs, low, and then stops laughing when you lick it from the root to the head."
    cp_anya "\"{i}Fuck{/i}. Again.\""
    menu:
        "Again":
            "Again. Root to head, slow, and she swears at the ceiling."
        "Kiss the tip first":
            "You kiss the tip first. Soft. Then you look up at her and open your mouth."
        "Look up at her and open wide":
            "You look up at her and open wide, and wait, and she groans like that's the worst thing you've ever done to her."
    show cg cp_knees_suck onlayer cgl
    vn_sfx "Glk. Glk."
    "You bob on her, slow, sloppy, both hands round the base because one doesn't close."
    "Every time you take her deeper she says your name, and every time she says your name you take her deeper."
    cp_anya "\"That's it. Throat open. There you go, pretty girl.\""
    cp_me "\"Mmh— {i}mmnh{/i}— {i}mmh{/i}—\""
    "You hum round her, loud, and her thighs clamp on your shoulders. Your throat opens on its own. You never practised that either."
    cp_anya "\"Look up at me. There. My pretty girl.\""
    "Her other hand's been on your chest the whole time. She squeezes."
    "Your tits spill over her fingers, and the spark goes straight down between your thighs, and you rock on your heels on the rug, moaning round her."
    show cg cp_knees_cum onlayer cgl
    "You come like that. On your knees, nothing touching you but her hand on your tit and her cock in your mouth, and you moan it round her so loud she swears." with vnfx("flash")
    show cg cp_knees_finish onlayer cgl
    "She comes with a hand on the back of your head, and you hold yourself there, and you gasp and gulp and look up at her dazed, sticky all over."
    cp_anya "\"You're gonna need another new bra.\""
    "Proud. Possessive. Like she grew them herself."
    hide cg onlayer cgl
    return

## ==== RUNG 6: the braid ==========================================================================
## After the last Leviathan: the brush, then one braid to match hers. Worship from the chest alone.
## "Goodbye," out loud, to the last of the old body. "Soon."
label cp_braid:
    $ vn_set_time(22, 0)
    $ cp.fit = "lily"
    $ vn_enter(bg="cp_flat", pc="neutral", pc_tag="cp_pc", cast=[("cp_anya", "neutral")])
    call cp_who_touched
    "Your flat, late. Anya's been basically living here for weeks. Her boots are by your door. Her toothbrush is in your cup."
    show cg cp_braid_mirror onlayer cgl
    "She sits you down at your bedroom mirror and brushes your hair out. It falls halfway down your back now. Pink. Heavy. Soft."
    "Then she parts it, and starts to braid."
    "One braid. Thick, down your back. Exactly like hers."
    "She ties it off and puts her hands on your shoulders and looks at the two of you in the mirror. Red braid. Pink braid."
    cp_anya "\"My pretty girl.\""
    "It isn't a line any more. It's just true."
    show cg cp_braid_hands onlayer cgl
    "Then her hands slide down. Over your collarbones. Onto your tits."
    cp_anya "\"Watch.\""
    "You watch. Her hands on you, full of you, kneading. Her mouth on your neck. Her thumbs on your nipples, circling, slow."
    cp_me "\"Ahh— {i}ahh{/i}— Anya—\""
    show cg cp_braid_suck onlayer cgl
    "She turns the chair round. Kneels in front of you."
    "Takes one nipple in her mouth and {i}sucks{/i}, hard, while her fingers roll the other one, and you grab her braid with both hands and arch off the seat."
    cp_me "\"Oh {i}god{/i}— oh god, your mouth— don't stop— {i}don't stop{/i}—\""
    vn_sfx "Shlp."
    "She switches sides. Bites, gently. Licks it slow. Looks up at you with your tit in her mouth and her eyes laughing."
    cp_anya "\"Mirror. Look in the mirror, Lily.\""
    "Round it. You look. A girl with a pink braid, flushed to the collarbone, mouth open, tits wet and red and huge in a redhead's hands."
    show cg cp_braid_cum onlayer cgl
    "You come from that. Just that. In front of the mirror, in your own braid, her hands on your chest." with vnfx("shake", "flash")
    "And she doesn't stop, and you come again, and again, until you're screaming and limp in the chair and she's still going, fists wrapped in your braid, making you look."
    hide cg onlayer cgl
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_flat", pc="neutral", pc_tag="cp_pc", cg="cp_braid_goodbye")
    "Afterwards, in bed, you reach down. Your cock is there. Barely. A tiny numb nub, half sunk into you. A stranger."
    cp_me "\"Goodbye.\""
    "You say it to it. Out loud."
    "Anya holds you. Her cock's hard against your back, heavy and patient, and she doesn't do anything with it."
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Soon.\""
    "You fall asleep almost hoping."
    hide cg onlayer cgl
    return

## ==== RUNG 6: the last piece (the counter; first vaginal, consensual) ==========================
## The cock goes overnight, found in the bathroom in the morning. "Anya! I have a pussy now!"
label cp_last_piece:
    $ cp_body(6)
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_flatbath", pc="shocked", pc_tag="cp_pc", cg="cp_last_bath")
    "Morning. You pad to the bathroom half asleep, braid over your shoulder, and push your shorts down."
    "You reach down."
    "Smooth skin."
    "{color=#ff9ecb}And a soft little cleft.{/color}"
    "You go very still. You feel again. Lips. Soft, puffy lips, and between them warm and wet, and at the top a little nub that {i}throbs{/i} when your finger brushes it."
    cp_me "\"Hhn—!\"" with vnfx("shake")
    "Nothing else. Nothing. No cock. No balls. Just smooth skin where they hung. You feel everywhere. It's gone. It went in the night like a candle going out."
    "You slide one finger between the lips, just to check, and it slips in to the knuckle."
    cp_me "\"{i}Ohhh{/i}— oh my {i}god{/i}— it's {i}real{/i}— it's {i}in{/i}—\""
    $ vn_enter(bg="cp_kitchen", pc="grin", pc_tag="cp_pc", cast=[("cp_anya", "neutral")])
    "You go into the kitchen in your T-shirt and nothing else."
    cp_me "\"Anya! I have a {i}pussy{/i} now!\""
    "It comes out a note higher than yesterday."
    "She's at your counter with a coffee. She puts it down very slowly."
    show cp_anya hungry at vn_cast_slot
    "Then she grins. Wolfish. Delighted."
    cp_anya "\"I've been waiting for this day.\""
    show cg cp_last_fridge onlayer cgl
    "She's across the kitchen in two steps. Your back hits the fridge. Magnets go everywhere." with vnfx("shake")
    "She kisses you so hard your head spins, and her hand goes straight between your legs and finds it, and you {i}scream{/i}."
    cp_me "\"Ahh— {i}ahh{/i}— oh god, that's— that's—\""
    cp_anya "\"Wet. Look how wet you are.\""
    "Delighted."
    show cg cp_last_counter onlayer cgl
    "She lifts you onto the counter like you weigh nothing. Spreads your thighs. Looks."
    cp_anya "\"Oh, Lily.\""
    "She sounds like she's been given a present. She drags one finger up through your new lips, slow, and holds it up, glistening."
    cp_anya "\"Look at that.\""
    cp_me "\"Don't— don't {i}show{/i} me—\""
    "You squeal it, and then her finger's back, circling your clit, and you can't say anything at all."
    cp_me "\"Ahh— {i}ahh{/i}— what {i}is{/i} that— it's so— {i}ohh{/i}—\""
    "She drops her joggers."
    "Her cock springs up, huge, and she rubs the fat head of it up and down your new lips, slow, slick, over your clit, again and again, until you're grabbing the edge of the counter and pushing your hips at her."
    cp_anya "\"Breathe, Lily. I'll go slow.\""
    menu:
        "Breathe":
            "You breathe. In. Out. On the out, she pushes."
        "Wrap your legs round her":
            "You wrap your legs round her and pull, and she laughs into your mouth and lets you."
    show cg cp_last_in onlayer cgl
    vn_sfx "Shlk." with vnfx("shake")
    "The stretch is huge. And then it's {i}perfect{/i}."
    "Her in you. All the way in you, in the place that's been waiting for her, and every stroke drags across something new and you can't stop moaning."
    cp_anya "\"There she is. That's my Lily.\""
    cp_me "\"Ahh— {i}ahh{/i}— yes— Anya— it's so {i}deep{/i}— don't stop— don't you {i}dare{/i} stop—\""
    show cg cp_last_mid onlayer cgl
    vn_sfx "Pap. Pap. Pap."
    "Your hips roll up to meet her like they've done this a hundred times. They haven't. Not once."
    cp_anya "\"Squeeze me. Yeah. Like that, pretty girl.\""
    "She doesn't go slow, for long."
    cp_anya "\"Say you're mine. Say it with this.\""
    show cg cp_last_cum onlayer cgl
    "Then it hits you."
    "Not your cock. Not your tits. Somewhere deep, right round her, a clench that doesn't stop. It climbs. It rolls out through your belly, your tits, your thighs, your curling toes." with vnfx("shake")
    "Your new pussy squeezes her in long helpless pulses and you scream her name at your kitchen ceiling, wave after wave. Your first time coming as a girl." with vnfx("flash")
    cp_me "\"{i}ANYA{/i}— {i}AHHH{/i}— {i}yours{/i}—!\""
    show cg cp_last_finish onlayer cgl
    "She comes with you, hips jammed to yours, groaning your name, and you come again from {i}that{/i}, moaning her name, clinging to her neck."
    cp_anya "\"That's my Lily.\""
    "She murmurs it into your hair."
    "And the name settles. Just like that. Strange and sweet and right."
    hide cg onlayer cgl
    $ cp.fit = "lily"
    return

## ==== THE NOVA: the fitting room again (the optional titjob, consensual) ======================
label cp_nova_titjob:
    show cg cp_nova_tits onlayer cgl
    "You pull her joggers down, and she springs out, and you catch her between your new tits before she's even finished swearing."
    "You squeeze them round her cock and it disappears between them, all of it, and you giggle up at her while she groans and swears."
    "You hold them round her like you've done it forever."
    cp_anya "\"Look at you. Look at you {i}laughing{/i}.\""
    "She pants it."
    cp_me "\"It's {i}funny{/i}. You used to have to {i}reach{/i}—\""
    vn_sfx "Shlp. Shlp."
    "She rocks her hips. Fucks your tits, slow, then fast, the head popping up between them right under your chin every stroke, and you lick it every time it does."
    cp_me "\"Mmh— {i}mm{/i}— you taste like the rain.\""
    "You giggle it."
    cp_anya "\"Squeeze them round me. These are mine too, you know.\""
    cp_anya "\"Lily— {i}fuck{/i}— Lily—\""
    show cg cp_nova_tits_cum onlayer cgl
    "She comes all over them. Up your throat. On your chin. You lick your lips and take the head in your mouth for the last of it, and that's the one that makes her knees go." with vnfx("flash")
    vn_sfx "Knock knock."
    cp_clerk "\"Need another size in there?\""
    "\"Yes,\" you both say, at the same time, and you collapse against her thigh, laughing."
    hide cg onlayer cgl
    return

## ==== THE STAY EPILOGUE: Anya, by the lockers (consensual) =====================================
label cp_after_hours:
    show cg cp_after_locker onlayer cgl
    vn_sfx "Clang. Clang."
    "You hold on to the locker door, and she slides into you standing, your knee hooked over her hip, your name rattling on the door with every thrust."
    cp_me "\"Ahh— {i}Anya{/i}— the door— everyone'll— there's nobody {i}here{/i}— {i}ahh{/i}—\""
    cp_anya "\"There she is. That's my Lily.\""
    "Faster. Your back on the cold metal and her mouth on your neck and your nails in her shoulders."
    show cg cp_after_cum onlayer cgl
    "You come with her name in your mouth and your nails in her shoulders, loud enough to echo down the empty Hub." with vnfx("flash")
    "She comes pinning you to your own locker, your name rattling on the door with every thrust right up to the last one."
    cp_anya "\"Same time tomorrow.\""
    "She fixes your skirt, and kisses your forehead."
    hide cg onlayer cgl
    return
