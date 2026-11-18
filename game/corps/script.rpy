## The Pink Ranger's days (main/cast/rungs/ending.twee, rewritten straight in Ren'Py, 2026-11-11; the
## catalog's twee is kept verbatim in catalog/docs/routes/vn-original/corps/). Linear days, as the
## built route's visual-novel days: every morning a waking beat at home, Zorp's text, the Hub; every
## day has its event (an alert, or the scene that's due); the night follows the day's event.
## The fights are fights.rpy; the written scenes are scenes.rpy.

## ==== THE DAY MACHINERY =========================================================================

## The night, then the morning at home: the rung's waking beat and Zorp's text.
label cp_sleep(wake=7):
    call vn_night(wake)
    $ vn_clock.day = (vn_clock.day or 1) + 0
    return

label cp_morning(text=None, who="Zorp"):
    $ cp_morph(False)
    $ cp.fit = cp.fit if cp.fit in ("lily",) else "own"
    $ vn_enter(bg="cp_flat", pc="neutral", pc_tag="cp_pc")
    $ _ml = CP_MORNINGS[max(1, min(7, cp.body or 1))]
    "[_ml!i]"
    if text:
        vn_sfx "Bzzt."
        "Your phone."
        "{color=#f3c969}[who]:{/color} {color=#ff9ecb}[text!i]{/color}"
    else:
        vn_sfx "Bzzt."
        "Zorp, a thumbs-up emoji, and nothing else."
    return

## The Hub, the day's room: Zorp over the briefing table, the locus line, the locker.
label cp_hub(alert=None):
    $ vn_enter(bg="cp_hub", pc="neutral", pc_tag="cp_pc", cast=[("cp_zorp", "neutral")])
    "{color=#ff9ecb}[cp_locus()!i]{/color}"
    $ _lk = CP_LOCKER[max(0, min(6, cp.locker or 0))]
    "[_lk!i]"
    if alert:
        $ _m = CP_MONSTERS[alert]
        "{color=#ff5a5a}ALERT:{/color} {color=#f3c969}[_m['name']]{/color}"
        "[_m['gimmick']]"
        menu:
            "Morph":
                pass
    return

## Rung 1's monster of the day, with its morning and the Hub.
label cp_day(key, text=None):
    call cp_morning(CP_MONSTERS[key]["alert"])
    call cp_hub(key)
    call cp_fight(key)
    return

## ==== THE OPENING (rung 1) ======================================================================

label cp_opening:
    $ cp.fit = "own"
    $ vn_enter(bg="cp_flat", pc="neutral", pc_tag="cp_pc", cg="cp_opening_sofa")
    "Late. Your flat. Ramen going crusty on the coffee table. You're on the sofa in boxers and yesterday's flannel, scrubbing chain grease off your knuckles with a rag."
    "Your hair flops in your eyes. Bubblegum pink. It's always grown that way. Not a statement. Just what grows."
    "Your dead phone lights up on the counter."
    "Not the screen. The {i}air{/i} over it. Frost-white static rolls off the glass, pools in the middle of the room, and inflates."
    vn_sfx "Fwump." with vnfx("shake")
    show cg cp_opening_zorp onlayer cgl
    "A chrome head the size of a beach ball. Cookie-sized digital eyes. A grin like a game-show host. Your houseplant wilts."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"LEO BICKFORD! PLANETARY DEFENCE ALERT! Congratulations! You have been selected as this city's next PINK RANGER!\""
    cp_me "\"Nope.\""
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"I am Zorp, emissary of the Morphing Grid! The Pink template has one requirement. Pink. You are the only pink in the city. Statistically this is very funny.\""
    "It spins, delighted."
    cp_me "\"Wrong flat, man. It's just hair.\""
    "You point at your own head."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"It is precisely the hair.\""
    "A pause one beat too long."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"The Grid will adapt any minor discrepancies.\""
    cp_me "\"What discrepancies?\""
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Minor ones! Please hold the morpher and say the words.\""
    "A warm pink rectangle pops into the air between you and hums."
    "Then the window rattles. Somewhere across town, something the size of a bus {i}roars{/i}, and a car alarm starts screaming, and then a lot of car alarms." with vnfx("shake")
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Bog-Zard. In the park. Eating a bandstand.\""
    "Brightly."
    "You look at the morpher. You look at the window."
    cp_me "\"...Fuck it.\""
    "You grab it."
    hide cg onlayer cgl
    menu:
        "IT'S MORPHING TIME!":
            pass
    call cp_fight("zard")
    jump cp_first_morning

## After the Zard: the first night home. Body hair goes first.
label cp_first_morning:
    $ vn_set_time(2, 30)
    $ vn_enter(bg="cp_flatbath", pc="nervous", pc_tag="cp_pc", cg="cp_first_mirror")
    "Home. Bathroom. The middle of the night."
    "You pull your shirt off in front of the mirror and stare."
    "Flat chest. {i}Your{/i} chest. A few stubborn chest hairs, like always. Your nipples look... puffier? No. It's late. You poke one."
    vn_sfx "Zzt."
    cp_me "\"Hhn—!\"" with vnfx("shake")
    "You grab the sink."
    cp_me "\"It's fine. Minor discrepancies.\""
    "You go to bed. The sheet brushes your chest every time you breathe, and you lie very, very still."
    call cp_sleep(8)
    $ cp.fit = "nude"
    $ vn_enter(bg="cp_flat", pc="shocked", pc_tag="cp_pc", cg="cp_first_smooth")
    "{color=#ff9ecb}In the morning the chest hairs are gone.{/color} All of them. Your legs are smooth. You look down the front of your boxers, and you're smooth there too, like you've been waxed."
    "You run a palm down your stomach. Over your hip. Down your thigh. Nothing catches. Just skin, slick and soft as the inside of a wrist."
    cp_me "\"Oh— {i}oh{/i}, that's—\""
    "Your hand does it again. Goosebumps chase it all the way down."
    cp_me "\"Why is that so {i}nice{/i}—\""
    "Your cock twitches in your boxers. You yank your hand away like it's hot."
    cp_me "\"Minor discrepancies. {i}Sure{/i}.\""
    "You tell the ceiling."
    $ cp.fit = "own"
    $ cp_locker(1)
    vn_sfx "Bzzt."
    "{color=#f3c969}Zorp:{/color} {color=#ff9ecb}{i}[CP_MONSTERS['monkey']['alert']]{/i}{/color}"
    call cp_hub("monkey")
    call cp_fight("monkey")
    call cp_audit(1)
    call cp_first_night
    jump cp_rung2

## ==== RUNG 2 ====================================================================================

label cp_rung2:
    $ cp.rung = 2
    call cp_sleep(8)
    call cp_day("shardwing")
    call cp_top
    call cp_sleep(8)
    call cp_day("ironjaw")
    call cp_audit(2)
    call cp_fitting
    jump cp_rung3

## ==== RUNG 3 ====================================================================================

label cp_rung3:
    $ cp.rung = 3
    call cp_sleep(8)
    call cp_day("widow")
    call cp_sleep(8)
    call cp_day("siren")
    call cp_audit(3)
    call cp_channel
    jump cp_rung4

## ==== RUNG 4 ====================================================================================

label cp_rung4:
    $ cp.rung = 4
    call cp_sleep(8)
    call cp_day("bramblemaw")
    call cp_panties
    call cp_sleep(8)
    call cp_day("serpent")
    call cp_sleep(8)
    call cp_day("lensfang")
    call cp_audit(4)
    jump cp_rung5

## ==== RUNG 5 ====================================================================================

label cp_rung5:
    $ cp.rung = 5
    call cp_sleep(8)
    call cp_morning()
    call cp_patch_up
    call cp_audit(5)
    call cp_hub("magnavore")
    call cp_fight("magnavore")
    call cp_coffee
    call cp_sleep(9)
    call cp_lily_day
    call cp_lily_morning
    call cp_hub("echoplasm")
    call cp_fight("echoplasm")
    call cp_changing_room
    call cp_knees
    jump cp_rung6

## ==== RUNG 6 ====================================================================================

label cp_rung6:
    $ cp.rung = 6
    call cp_sleep(8)
    call cp_morning("girls night. my flat. you're coming, lily. no excuses", "Vee")
    call cp_girls_night
    call cp_sleep(8)
    call cp_day("leviathan1")
    call cp_sleep(8)
    call cp_day("leviathan2")
    call cp_braid
    call cp_sleep(8)
    call cp_last_piece
    call cp_audit(6)
    jump cp_nova

## ==== ZORP'S AUDITS: the Tuesday meeting, the scan pad =========================================
## You on the pad in front of the team; Zorp reads the rung's euphemism aloud, plus a cup letter,
## never a figure; the pad's calibration pulse makes you lock your knees (a tease, not the rung's
## act); then the locus line; then Tobi's wrong explanation, one beat late.

label cp_audit(n):
    $ cp.rung = max(cp.rung or 1, n)
    $ vn_enter(bg="cp_hub", pc="nervous", pc_tag="cp_pc", cast=[("cp_zorp", "grin")], cg="cp_audit_%d" % n)
    if n == 1:
        cp_zorp "\"Template compliance audit: {i}Welcome Edition!{/i} Pink Ranger, please stand on the measurement pad. This is completely routine!\""
        "Zorp spins over the briefing table, thrilled."
        "The pad's a glowing circle in the corner of the main room. The whole team's standing round it with mugs."
        "You step on."
        "It hums up through your soles. Warm. It climbs your legs, your stomach, and then it finds your new puffy nipples and {i}pulses{/i}."
        cp_me "\"Hhn—!\"" with vnfx("shake")
        "You lock your knees. Everybody sees you do it."
        cp_zorp "\"Pectoral sensitivity: elevated! Hand breadth: trending narrow! Body hair: discontinued! Cup designation: pending!\""
        "Bright as a quiz show. Kyle whistles at the ceiling. Mira writes something down. Anya doesn't pretend to look anywhere else."
        "{color=#ff9ecb}\"[CP_LOCUS[1]]\"{/color}"
        cp_me "\"Locus of {i}what?{/i}\""
        cp_zorp "\"Regulation.\""
        "Warmly."
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Locus. Like the bug. They swarm. He's saying you're gonna swarm.\""
        "He nods, satisfied. Nobody corrects him."
    elif n == 2:
        "The pad again. The mugs again."
        "You step on in a hoodie zipped to the chin. It doesn't help."
        "The pulse comes up through you and lands in two places at once: your tits, round and heavy under the zip, and your cock, twitching in your jeans."
        "You can't tell which one makes you gasp."
        cp_me "\"Ahh— {i}hh{/i}—\"" with vnfx("shake")
        "Knees locked. Hands fisted in your sleeves."
        cp_zorp "\"Anterior mass development: within projections! Waist: reduced! Voice resonance: elevated! Cup designation: C!\""
        "Mira crosses out the {i}B{/i} on Tobi's betting sheet and writes {i}C{/i}. Tobi groans and hands her a chocolate bar."
        "{color=#ff9ecb}\"[CP_LOCUS[2]]\"{/color}"
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Shared. Like a flat. Your nipples have got a flatmate.\""
        cp_me "\"That's not—\""
        show cp_anya neutral at vn_cast_slot
        "Anya's already standing. She looks at the hoodie straining over your chest. She snaps her fingers."
        cp_anya "\"Bra shopping. Now.\""
    elif n == 3:
        cp_zorp "\"Gluteo-femoral redistribution proceeding nominally! Phonation: updated! Keratin: updated! Cup designation: D, firm!\""
        "The moment you're on the pad."
        "The pulse comes up. It goes straight past your cock. Your cock barely twitches. It goes into your tits instead and stays there, humming, like the Siren's ghost."
        cp_me "\"Mmh— {i}mmnh{/i}—\""
        "You lock your knees so hard they shake. Somebody's mug clinks."
        "{color=#ff9ecb}\"[CP_LOCUS[3]]\"{/color}"
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Anterior. Front. Front-loaded. It's a car thing.\""
        "He's thought about it."
        show cg cp_audit_3_screen onlayer cgl
        "Then the debrief. Zorp throws the Siren footage up on the big screen: the tower, the note, the girl's voice going out over the whole city."
        show cp_kyle neutral at vn_cast_slot
        cp_kyle "\"Who took point on the tower?\""
        "He knows. He wants someone to say it."
        show cp_anya neutral at vn_cast_slot
        cp_anya "\"She took point.\""
        "Just that. She doesn't look at you when she says it."
        "A beat. Then the whole table goes with it."
        cp_kyle "\"She was amazing.\""
        "Going red."
        cp_tobi "\"She sang the whole tower down.\""
        show cp_mira neutral at vn_cast_slot
        "Mira leans over on your way off the pad, eyes on the soft pink fluff growing back over your ear."
        cp_mira "\"I'll show you how to braid. When you're ready.\""
        "Nobody says {i}he{/i} again. Not at the table. Not after."
        $ cp_name("Lily")
    elif n == 4:
        show cp_vee neutral at vn_cast_slot
        "There are two new faces at the table: the rookies, Vee and Naomi. They've only ever known Lily."
        cp_zorp "\"Involuntary morale spike: logged! Facial geometry: updated! Cup designation: E!\""
        "Vee whoops. Naomi claps."
        "Then the pulse comes up, and it doesn't stop at a tease this time."
        "It lands in your tits and {i}rolls{/i}, wave after wave, and you're standing on a pad in the middle of the Hub with your knees locked and your mouth open and you're going to—" with vnfx("shake")
        cp_me "\"Nnh— Zorp— turn it— {i}turn it off{/i}—\""
        cp_zorp "\"Calibration complete!\""
        "It stops. You're shaking. You nearly came on the pad. In front of everyone. Hands-free."
        "{color=#ff9ecb}\"[CP_LOCUS[4]]\"{/color}"
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Broadcast. 'Cause of the telly thing. The filter.\""
        show cp_naomi neutral at vn_cast_slot
        "Naomi catches your eye across the table and grins like she knows exactly what nearly happened. She does."
    elif n == 5:
        cp_zorp "\"Regulation four-one requires demorphed verification. The Grid cannot certify adaptation it has not measured.\""
        cp_me "\"Measured where?\""
        cp_zorp "\"Here!\""
        $ cp.fit = "nude"
        show cg cp_audit_5 onlayer cgl
        "So you stand on the pad in the middle of the meeting in the mandated undergarments. Pink lace panties. A white bra that's already losing."
        show cp_anya smirk at vn_cast_slot
        "Anya authorises each step like she owns you."
        cp_anya "\"Arms up.\""
        "You lift your arms."
        cp_anya "\"Turn.\""
        "You turn."
        cp_anya "\"Good.\""
        cp_zorp "\"Cup designation: E, trending F! Hip spread: generous! Residual masculinity: trending down!\""
        "The pulse comes up. It skips your cock completely. Your cock is a little soft nothing in the lace and it doesn't even twitch."
        "The pulse goes up your thighs and into your {i}ass{/i}, a deep warm throb right inside, and you clench on it and gasp."
        cp_me "\"Ah— {i}ahh{/i}—!\"" with vnfx("shake")
        "Everybody watches. Nobody mentions it."
        "{color=#ff9ecb}\"[CP_LOCUS[5]]\"{/color}"
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Posterior. Like the back. The back of...\""
        "He stops."
        "He looks at you on the pad. He looks at Anya. He looks at you."
        cp_tobi "\"Wait. {i}WAIT.{/i}\"" with vnfx("shake")
        "He's the last man on the team to get there. By weeks. Mira gently pushes his mug back across the table to him."
        cp_zorp "\"Red Ranger, your audit is also due—\""
        show cp_anya neutral at vn_cast_slot
        cp_anya "\"Declined. On grounds of rank.\""
        "The console makes a small sad noise and loses power."
        $ cp.fit = "own"
    else:
        $ cp.fit = "lily"
        "The last meeting."
        "You step on the pad in a bralette and a skirt, and the pulse comes up, and it goes straight between your legs. Into your new pussy."
        "Your clit throbs so hard you grab the edge of the table."
        cp_me "\"Ahh— {i}oh{/i}— oh, that's— {i}nnh{/i}—\"" with vnfx("shake")
        cp_zorp "\"Template conformance: complete! Cup designation: H! All adaptations: permanent and certified! Congratulations!\""
        "Overjoyed. Vee and Naomi cheer. Kyle cheers, genuinely. Mira closes her pool book with a soft, satisfied slap."
        "{color=#ff9ecb}\"[CP_LOCUS[6]]\"{/color}"
        show cp_tobi neutral at vn_cast_slot
        cp_tobi "\"Template. Like a form. A... tax form?\""
        "Everybody looks at him."
        show cg cp_audit_6_board onlayer cgl
        "Then the board lights up red across every sector at once, and Zorp's grin goes very thin." with vnfx("flash")
        cp_zorp "\"The Shadow Tyrant has been located. All rangers. Tomorrow.\""
    hide cg onlayer cgl
    return

## ==== THE CAST'S BEATS ==========================================================================

## After the Shardwing: Anya's white compression top on your bench. She demorphs facing the wall.
label cp_top:
    $ cp_locker(2)
    $ vn_enter(bg="cp_lockers", pc="nervous", pc_tag="cp_pc", cg="cp_top_bench")
    "Next training, there's something on your bench."
    "A white compression top. Folded. Your size. No note."
    show cg cp_top_wall onlayer cgl
    "You look round. The team's gearing up. Kyle's doing stretches. Tobi's arguing with Mira about the betting sheet. And Anya's in the corner, demorphing."
    "Facing the wall."
    "She never used to do that. She used to just drop the suit in the middle of the room, swear, and get on with it."
    "Now her back's to everyone, shoulders tight, and she's tugging her shirt down low over her hips before she turns round."
    hide cg onlayer cgl
    "You put the top on. It squeezes. It {i}holds{/i}. For the first time in days you can breathe without your nipples dragging cotton."
    show cp_anya neutral at vn_cast_slot
    cp_me "\"Anya—\""
    cp_anya "\"Don't.\""
    "She doesn't look up from her boots."
    cp_me "\"I was just going to say—\""
    cp_anya "\"Nobody showed me.\""
    "She yanks a lace tight."
    cp_anya "\"When it started on me. Nobody showed me anything. I bound with tape in the toilets.\""
    "Then she looks up, and her eyes go to your chest, and stay there."
    cp_anya "\"So I'm showing you.\""
    "She walks past and tugs the hem of the top straight over your ribs on her way. Her knuckles brush the underside of your tits."
    cp_anya "\"Better.\""
    return

## Rung 5 opens: Kyle's patch-up, the almost-moment; the door; Anya.
label cp_patch_up:
    $ vn_enter(bg="cp_patchup", pc="nervous", pc_tag="cp_pc", cast=[("cp_kyle", "neutral")], cg="cp_patch_kyle")
    "Lensfang left scrapes all down your ribs, under where the plate tore. They need dressing."
    cp_kyle "\"I'll do it.\""
    "Too fast. Nobody else in the doorway says anything at all."
    "The patch-up room. You on the table, shirt rucked up under your tits. Kyle with the antiseptic, breath held, hands shaking so badly he has to stop and start again."
    "He works it along your ribs with a pad of gauze, careful, reverent, and so careful never to let his fingers touch your skin that it takes forever."
    "He apologises for things that didn't hurt."
    cp_me "\"You can press harder.\""
    cp_kyle "\"I know.\""
    "He doesn't press harder."
    "The gauze stops, just under the curve of your breast. His fingers hover. Neither of you says anything. The whole room leans about a degree toward something."
    show cg cp_patch_door onlayer cgl
    vn_sfx "Click."
    "The door opens. Anya. She doesn't knock. She takes the whole thing in, one flat second, and the room goes cold."
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Debrief. Now.\""
    "Kyle caps the antiseptic and goes."
    "You sit there with your shirt still up and think, uncharitably and truthfully, that if she'd come in a little later she'd have had a lot more to be angry about."
    hide cg onlayer cgl
    return

## After Magnavore: Kyle's coffee, which he never gets. "Lily's booked." Tomorrow, on the leverage.
label cp_coffee:
    $ vn_enter(bg="cp_park", pc="nervous", pc_tag="cp_pc", cast=[("cp_kyle", "neutral")])
    "Kyle catches you by the maintenance door on the way out. He's been working up to it all afternoon; you can see it on him."
    cp_kyle "\"Hey. Lily.\""
    "He rubs the back of his neck."
    cp_kyle "\"Would you— do you want to get coffee? Or lunch. Just us. Not— not a team thing.\""
    "You open your mouth. You're going to say yes. You really are."
    show cp_anya smirk at vn_cast_slot
    cp_anya "\"Lily's booked.\""
    "From nowhere, too sweet. Her hand lands on the small of your back and steers you away, and Kyle just stands there with his mouth half open."
    show cg cp_coffee_wall onlayer cgl
    "Round the corner she stops you against the wall. Close."
    cp_anya "\"I know what you sound like at night. On the channel. In the vines.\""
    "Low. Her thumb strokes your hip, over the lace she makes you wear."
    cp_anya "\"Unless you want Tobi to know what you did in that fitting room, you'll be at my door at ten.\""
    "She puts a bag in your hands."
    cp_anya "\"Demorphed. You wear what's in there.\""
    cp_me "\"Anya, I was going to say {i}yes{/i} to him— I was just going to get a {i}coffee{/i}—\""
    cp_anya "\"Ten, Lily.\""
    cp_me "\"That's not— you can't just—\""
    cp_anya "\"Ten.\""
    "She kisses your forehead and walks off, and you stand there holding the bag."
    hide cg onlayer cgl
    return

## Rung 6 opens: Kyle bows out, Vee moves your locker, and girls' night at Vee's. Look, never touch.
label cp_girls_night:
    $ cp_locker(6)
    $ vn_enter(bg="cp_hub", pc="neutral", pc_tag="cp_pc", cast=[("cp_kyle", "neutral")])
    "Kyle finds you in the corridor first."
    cp_kyle "\"Hey.\""
    "He's smiling, a bit sad, completely sincere."
    cp_kyle "\"You and Anya. I get it. I'm— I'm really happy for you, Lily. I mean it.\""
    "He holds out a fist."
    cp_kyle "\"Still on my team, though. Always.\""
    "You bump it. He means every word, and he goes on meaning it, and he's the best friend you've got by the end of the week."
    $ vn_enter(bg="cp_lockers", pc="shocked", pc_tag="cp_pc", cast=[("cp_vee", "neutral")], cg="cp_locker_moved")
    "Then your locker's gone."
    "Vee carried it across the corridor to the women's side. Contents and all. Wrote {i}LILY{/i} on it in marker."
    cp_vee "\"You're one of us. Keep up.\""
    "When you stand there gaping."
    $ vn_set_time(20, 0)
    $ cp.fit = "lily"
    $ vn_enter(bg="cp_veeflat", pc="grin", pc_tag="cp_pc", cast=[("cp_vee", "neutral")])
    "Friday's at her flat."
    "It's meant to be a bra-fitting night. It turns into show and tell in about a minute."
    cp_vee "\"The Grid gave you {i}those?{/i} No way. Show us. Come {i}on{/i}.\""
    "She's sprawled on her sofa with a wine glass."
    show cg cp_girls_show onlayer cgl
    "So you pull your top up. Scarlet to the collarbones. Your tits bounce out, heavy, round, bigger than any of theirs."
    "The room {i}screams{/i}." with vnfx("shake")
    cp_vee "\"Oh my god—\""
    hide cp_vee
    show cp_naomi neutral at vn_cast_slot
    cp_naomi "\"They're so {i}perky{/i}—\""
    hide cp_vee
    show cp_mira neutral at vn_cast_slot
    cp_mira "\"Lily, I hate you, that's not fair—\""
    "Nobody touches. They look and they shriek and they make you turn round so they can see your ass in the skirt, and you're giggling, high and helpless, and you can't stop."
    show cg cp_girls_anya onlayer cgl
    "Anya's in the armchair in the corner. Wine. Legs crossed. Watching. She doesn't join in and she doesn't leave."
    "Truth or dare. The dares are all show, never touch. Walk the hallway to the bins in nothing but a towel. Read out your last audit line in Zorp's voice."
    "Tell the room what Anya calls you."
    cp_me "\"Her pretty girl.\""
    "You mumble it into your wine. The room loses it."
    "Naomi tries one dare that goes a step further. Anya shakes her head, once. Naomi laughs and takes it back. Nobody touches what's hers."
    hide cg onlayer cgl
    show cp_mira neutral at vn_cast_slot
    "Then Mira, cross-legged on the rug, deadpan, quiet."
    cp_mira "\"Truth. Does it still work?\""
    "The room goes still. Everyone knows what she means."
    cp_me "\"No.\""
    "Out loud. For the first time."
    "And nobody laughs. Vee puts her hand on her heart. Naomi says \"Aw, babe.\" Mira nods, like you've passed something. It feels like being let in."
    hide cp_mira
    hide cp_vee
    show cp_naomi neutral at vn_cast_slot
    cp_naomi "\"Lovebirds.\""
    "Naomi sing-songs it, when Anya gets up at midnight to collect you."
    show cp_anya neutral at vn_cast_slot
    "Anya doesn't argue. She puts her coat round your shoulders and walks you out with her hand on the back of your neck."
    return

## ==== THE LILY DAY (rung 5's lead-in), on her leverage ==========================================

label cp_lily_day:
    $ vn_set_time(10, 0)
    $ vn_enter(bg="cp_anyaflat", pc="nervous", pc_tag="cp_pc", cast=[("cp_anya", "smirk")])
    call cp_who_touched
    "Anya's flat, ten in the morning. On the dot. You stood at the end of her street for twenty minutes telling yourself you weren't going, and here you are."
    "She opens the door and looks you up and down, hoodie and all, and then at the bag, still unopened in your fist."
    cp_anya "\"You were meant to come in it. Bathroom. Now.\""
    $ cp.fit = "lily"
    $ vn_enter(bg="cp_anyabath", pc="shocked", pc_tag="cp_pc", cg="cp_lily_mirror")
    "Inside: a cropped pink sweater. No bra. A white miniskirt. White thigh-highs. Wedge sandals."
    "You put it all on. You look."
    "The mirror's got a girl in it. Plush and soft and obvious. Your tits fill the sweater, no bra, nipples poking right through. The skirt barely covers your ass."
    "The stockings squeeze your thighs so they bulge a little over the bands."
    "Months ago you'd have stared at a girl like that on the bus."
    cp_me "\"Oh no.\""
    "A whisper."
    $ vn_enter(bg="cp_anyaflat", pc="nervous", pc_tag="cp_pc", cast=[("cp_anya", "hungry")])
    "You come out. Anya's eyes go everywhere, slow."
    cp_anya "\"There she is. Lily.\""
    cp_me "\"It's—\""
    cp_anya "\"{i}Lily{/i}.\""
    menu:
        "Out the door":
            pass
    $ vn_pass(30)
    $ vn_enter(bg="cp_salon", pc="neutral", pc_tag="cp_pc", cg="cp_lily_salon")
    "The salon first."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"The full treatment. For Lily.\""
    "Lashes. Gloss. A blow-out that takes your pink hair and turns it into long, loose, bouncing waves round your shoulders. The stylist keeps calling you {i}hon{/i}."
    "\"Your girlfriend's hair is gorgeous,\" she tells Anya. \"Is the colour natural?\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Completely.\""
    "She runs her fingers through it like she owns it."
    "Your nipples are poking through the sweater the whole time. Nobody mentions it. Everyone notices."
    $ vn_pass(90)
    $ vn_enter(bg="cp_town", pc="grin", pc_tag="cp_pc", cg="cp_lily_crepe")
    "She parades you through the whole town and introduces you everywhere as Lily, and every single person just... believes her."
    "Crepes. She feeds you a bite and there's cream on your lip, and she leans in and licks it off in the middle of the street. You squeak."
    $ vn_enter(bg="cp_arcade", pc="flushed", pc_tag="cp_pc", cg="cp_lily_arcade")
    "The arcade. You bend over the claw machine and her hand slides up under the back of your skirt. Over the lace."
    "Rubbing the tiny soft bump of your cock through the panties, slow."
    cp_me "\"Anya— {i}people{/i}—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Then be quiet.\""
    "You are not quiet."
    cp_me "\"Hhn— {i}mmh{/i}— ahh—\""
    "The claw drops. Misses. You're wet through the lace, a damp spot on the white, and you're right on the edge when she takes her hand away."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Oh, unlucky.\""
    "About the claw."
    $ vn_enter(bg="cp_town", pc="nervous", pc_tag="cp_pc", cg="cp_lily_tea")
    "Tea, knees together, both hands round the cup, shaking."
    "The bookshop. She buys you a romance novel with a pink cover and a man with no shirt on it, and tucks it in your bag without a word."
    "\"Your girlfriend's adorable,\" the woman at the till says."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Isn't she.\""
    $ vn_pass(180)
    $ vn_set_time(19, 0)
    $ vn_enter(bg="cp_bench", pc="flushed", pc_tag="cp_pc", cg="cp_lily_bench")
    "Dusk. A bench in the park. Joggers going past. Couples."
    "She pulls you onto her lap, sideways, your legs across hers, and her hand goes up your skirt and doesn't stop."
    "Two fingers on the lace. Circling. Pressing. Your little cock is nothing, a soft bump, and she's rubbing behind it, underneath, right where it makes you shake."
    cp_me "\"Ahh— {i}ahh{/i}— Anya— someone's going to—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Say it.\""
    "She murmurs it."
    cp_me "\"S-say what—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Do you like it? Being Lily?\""
    cp_me "\"I— {i}ahh{/i}—\""
    "She presses harder. Circles faster."
    "A jogger goes right past the bench and you bury your face in her neck and {i}whine{/i}, and your hips are rocking on her hand, and the lace is soaked, and you're going to— you're going to—"
    "Her fingers go still. Right on the edge."
    cp_me "\"Nnh— {i}no{/i}— Anya, please, I was so close—\""
    show cg cp_lily_wrist onlayer cgl
    "Your own hand shoves down under your skirt to finish it. She catches your wrist before it gets there and holds it up in the air between you, like evidence."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Touch yourself and it's a costume party for the whole team. Tobi in charge of the theme.\""
    "Pleasant."
    cp_me "\"You— you {i}wouldn't{/i}— {i}ahh{/i}—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"I know.\""
    "She kisses your temple. She pins your wrist to her shoulder and starts again. Slow. She takes you right back up to the edge, and stops. And again."
    "And again, until you're shaking all over and the sky's gone dark blue."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Say it.\""
    menu:
        "Whisper it":
            cp_me "\"I love it.\""
            "A whisper."
        "Scream it":
            cp_me "\"I LOVE IT—!\"" with vnfx("shake")
            "Right into the park. A jogger trips."
            cp_me "\"I love it, I love it, I {i}love{/i} it—\""
        "Beg it":
            cp_me "\"I love it— I love it, please, please, Anya, I love it—\""
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Good girl.\""
    "She takes her hand out from under your skirt. You whine."
    show cp_anya hungry at vn_cast_slot
    cp_anya "\"Not yet.\""
    "She walks you home to her flat with her hand on the back of your neck. You can barely walk."
    jump cp_lily_door

## ==== THE NOVA (the ending) =====================================================================

label cp_nova:
    call cp_sleep(8)
    call cp_morning("ALL RANGERS. The plaza. Today. This is the big one.")
    "Thunder somewhere over the city."
    $ cp_morph(True)
    $ cp_body(6)
    $ vn_enter(bg="cp_plaza", pc="neutral", pc_tag="cp_pc", cg="cp_nova_tyrant")
    call cp_who_touched
    "Thunder over the plaza. Rain coming down sideways. Every window for a mile blown in." with vnfx("shake")
    "And in the middle of it, the Shadow Tyrant. Tall as a tower block and made of nothing, a hole in the storm with a crown on it."
    "The thing behind every Bogon, every monster, every morph."
    "{color=#ff7ab8}\"IT'S MORPHING TIME — PINK RANGER, POWER UP!\"{/color}" with vnfx("flash")
    "It doesn't even feel like being taken apart any more. It feels like the last bit of a stretch. The suit closes over you and there's almost nothing for it to change."
    "The team's in tatters round the edges of the plaza. Black limping. Yellow and Blue holding each other up. Vee and Naomi pinned behind a burning bus."
    show cg cp_nova_red onlayer cgl
    "Red lands next to you. Bleeding from the hairline. Grinning at you through it."
    show cp_red neutral at vn_cast_slot
    cp_red "\"Ready, Lily?\""
    cp_me "\"Ready.\""
    "You put your morpher against hers. Pink against red. They lock with a sound like a bell."
    show cg cp_nova_strike onlayer cgl
    cp_me "\"HEARTSTRIKE—\"" with vnfx("shake")
    show cp_red neutral at vn_cast_slot
    cp_red "\"—NOVA!\"" with vnfx("flash")
    "Pink and red light goes up out of the two of you like a column, up into the dark, and comes down through the Shadow Tyrant's crown, and it cracks from the inside out, and it {i}screams{/i}, and then there's just rain."
    "Just rain, and the six of them whooping, and Red's arm round your waist so tight you can't breathe."
    show cg cp_nova_morphers onlayer cgl
    "Zorp's portal opens in the middle of the plaza, quietly, for once."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Rangers. The war is over. Permanently. The Grid thanks you.\""
    "A little pause."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"Please return your morphers.\""
    "One by one, they hand them over. Blue. Black. Yellow. The rookies. Red, last but one, with a long look at you."
    "You hold yours."
    "You hold it too long. Everyone's watching. Your fingers won't open. If it goes, does she go? Does Lily go?"
    "Zorp's voice slips into your head on a channel nobody else is on."
    show cp_zorp neutral at vn_cast_slot
    cp_zorp "\"You won't lose what matters. Consider it a commemorative retention bonus.\""
    menu:
        "Twist it free":
            pass
    $ cp_morph(False)
    $ cp_body(7)
    $ cp.rung = 7
    $ cp.fit = "lily"
    $ vn_enter(bg="cp_plaza", pc="shocked", pc_tag="cp_pc", cg="cp_nova_surge")
    "You twist the morpher free and drop it in Zorp's portal."
    "The suit goes. Light, then no light."
    "Then you, standing in the rain, in your own clothes, in your own body. All of it. It stayed."
    "{color=#ff9ecb}And then it {i}surges{/i}.{/color}" with vnfx("shake")
    "It starts behind your breastbone like a held breath going out. Your tits swell. Past where they were this morning. Past where the suit ever had them."
    show cg cp_nova_burst onlayer cgl
    vn_sfx "Pop!" with vnfx("shake")
    "Your bra creaks. Strains. And bursts its seams with a pop you hear over the rain, and they spill out heavy and soaked and enormous in front of the whole team."
    cp_me "\"{i}Ahhh{/i}—!\""
    "You grab them. You can't help it. Both arms full of tit and still overflowing, slick with rain, swelling {i}into{/i} your hands."
    cp_me "\"Oh— oh {i}fuck{/i}— they're still— {i}still going{/i}— {i}ahhh{/i}—!\"" with vnfx("flash")
    "A J. They have to be. Nobody makes bras for this."
    "Your hips push out. Your ass rounds and lifts. Your thighs thicken until they squeeze. Your face goes soft and pretty under the rain. Your braid slithers down past your waist."
    "When you gasp, it's in the sweetest voice you've ever heard come out of anyone."
    "You squeeze your own ass in front of everyone. You lick the rain off your lips and it nearly takes your knees out. You moan, loud, and you don't care who hears."
    cp_me "\"More. {i}More{/i}—\""
    "You beg the sky. You arch your back for the whole plaza without thinking. Your body knows exactly how to be looked at now."
    hide cg onlayer cgl
    "The team stares. Tobi's mouth is open. Kyle's got a hand over his."
    show cp_zorp grin at vn_cast_slot
    cp_zorp "\"Commemorative.\""
    "It winks out with the morphers."
    show cp_anya hungry at vn_cast_slot
    "Anya takes your face in both hands."
    cp_anya "\"Lily.\""
    "Not a question."
    "It hasn't been a question for months, and you notice, standing in the plaza with the rain coming down, that you can't remember the last time it made you flinch."
    "Then she looks down at your chest, bare and dripping and spilling everywhere, and her eyes go dark."
    cp_anya "\"Shop. Now.\""
    $ vn_pass(40)
    $ vn_enter(bg="cp_fitting", pc="grin", pc_tag="cp_pc", cast=[("cp_anya", "smirk")], cg="cp_nova_fitting")
    "The same lingerie shop. The same fitting room. The same curtain, snapped shut behind you both."
    "Not the same bra. Nothing on the rack goes high enough. Anya holds the biggest one they've got up against you and laughs out loud."
    cp_anya "\"It won't go round. Look at you. Nothing fits you, Lily.\""
    "You look in the mirror. Soaked. Flushed. Tits out, heavy and huge, braid stuck to your back."
    "You start giggling. You can't help it."
    "And you're on your knees in front of her before you've decided to be, looking up, and her joggers are tented right in your face."
    menu:
        "Pull her joggers down":
            call cp_nova_titjob
        "Just make her buy you a bra":
            "You make her buy you a bra. The biggest one they do, and it still only just closes, and you walk out of the shop in it giggling, holding her hand."
    jump cp_toast

## The toast, the ending, the feat. Then stay or go.
label cp_toast:
    $ vn_set_time(22, 0)
    $ vn_enter(bg="cp_hub", pc="grin", pc_tag="cp_pc", cast=[("cp_tobi", "neutral")], cg="cp_toast")
    "That night the Hub is a party. Every light on. Music off somebody's phone. Vee on the briefing table. Mira running a pool on who passes out first."
    "You're on the sofa with Anya's arm round you and your head on her shoulder, in a bra that finally fits."
    "Tobi climbs onto a chair. Taps his bottle with a fork."
    cp_tobi "\"Okay. Okay! Shut up!\""
    "He raises it. He's very drunk and very sincere."
    cp_tobi "\"To the best ranger I ever had the honour of— of being confused by.\""
    "Everyone laughs. He waits."
    cp_tobi "\"To Lily.\""
    "\"{i}To Lily!{/i}\"" with vnfx("flash")
    "Kyle shouts it loudest."
    $ vn_feat("Heartstrike Nova")
    hide cg onlayer cgl
    show cp_anya smirk at vn_cast_slot
    "Later, when the music's quiet, Anya tucks your braid over your shoulder."
    cp_anya "\"So. What now, Pink?\""
    menu:
        "Stay on the roster" (ending=True):
            jump cp_epilogue_stay
        "Go back to the bike shop" (ending=True):
            jump cp_epilogue_go

label cp_epilogue_stay:
    $ cp.epilogue = "stay"
    $ cp.done = True
    $ vn_enter(bg="cp_lockers", pc="grin", pc_tag="cp_pc", cg="cp_stay_locker")
    "You stay."
    "There's no war. There's still a roster."
    "Your locker stays on the women's side with {i}LILY{/i} on it in Vee's marker, and Anya's brush on the shelf, and a bra in there for emergencies, because there are always emergencies."
    show cg cp_stay_tuesday onlayer cgl
    "Tuesdays there's still a meeting. Nobody stands on the pad any more. Tobi brings doughnuts. Kyle saves you the seat by the window."
    "Anya sits beside you and hooks her ankle round yours under the table."
    "The Hub's always open. You're always welcome."
    hide cg onlayer cgl
    $ vn_set_time(21, 0)
    $ vn_enter(bg="cp_lockers", pc="neutral", pc_tag="cp_pc", cast=[("cp_anya", "hungry")])
    "One evening. Everyone's gone home. The Hub hums. You're at your locker on the women's side, hunting for your brush."
    vn_sfx "Click. Click."
    "The door to the corridor clicks shut behind you. Then the lock."
    cp_anya "\"Lily.\""
    "Anya, leaning on the lockers, arms folded, her braid over one shoulder. Her joggers are already tented."
    cp_me "\"The war's over.\""
    cp_anya "\"Mm.\""
    "She pushes off the lockers and walks you backwards into yours."
    vn_sfx "Clang." with vnfx("shake")
    "Her mouth on your neck. Her hand up your skirt, two fingers sliding through you, and you're already wet, you're always wet for her now."
    cp_me "\"Ahh— {i}Anya{/i}—\""
    cp_anya "\"I never said it was about the war.\""
    "She hooks your knee up over her hip."
    menu:
        "Hold on to the locker door":
            call cp_after_hours
        "Kiss her and say \"later\"":
            "You kiss her, slow, and say {i}later{/i} against her mouth."
            cp_anya "\"Later, then.\""
            "She lets you go, and you both know she'll collect."
    jump cp_route_return

label cp_epilogue_go:
    $ cp.epilogue = "go"
    $ cp.done = True
    $ vn_enter(bg="cp_lockers", pc="neutral", pc_tag="cp_pc", cg="cp_go_locker")
    "You go back to the bike shop."
    "You clear your locker on a Monday. The brush. The bra. The pink lace you'll never admit you kept."
    "You hug everyone, and Tobi makes a speech nobody asked for, and Kyle hugs you a second time."
    show cg cp_go_door onlayer cgl
    "Anya walks you up to the maintenance door and kisses you against it, long and slow."
    show cp_anya neutral at vn_cast_slot
    cp_anya "\"Mine.\""
    "And lets you go."
    "The door shuts behind you."
    $ vn_enter(bg="cp_bikeshop", pc="grin", pc_tag="cp_pc", cg="cp_go_shop")
    "On Tuesday your phone buzzes."
    vn_sfx "Bzzt."
    "{color=#f3c969}Zorp:{/color} {color=#ff9ecb}{i}Status inquiry: none required.{/i}{/color}"
    "You laugh, high and sweet, under a bike on your back in the shop, with grease on your fingers and a braid down to your waist."
    jump cp_route_return
