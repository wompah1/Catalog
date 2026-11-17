## heirloom, ch 8-14: after the flip, all consensual (8-13), and the epilogue's recruit set in full under the
## house rules (owner's pick at sign-off). she/her from the face (ch 9); the name Yuuka from the roster (ch 12).
## The book's team grows cocks in ch 8 and 10; here the team's are the club's harnesses and Kaede's is the
## only one, and ch 8's oral round is him going down on the team, then Kaede's cock for the throat.

## ---- 8. Throat and Voice -------------------------------------------------------------------------
label hrl_ch8:
    $ hrl.chapter = 8
    $ hrl_body(6)    # the voice: drawn as the full-chest row
    $ hrl.fit = "bra" if hrl.top == "bra" else "kit"
    $ vn_enter(bg="hrl_clubroom", pc="deadpan", pc_tag="hrl_pc", cast=[], cg="hrl_voice_alone")
    "A too-bright Monday between the camp and the term's real rush. You're alone at the manager's desk over Rei's schedule: weights, plyos, {i}USE YUU (MANDATORY), noon{/i}."
    hrl_you "\"I guess it's still me under all—\""
    "{color=#c58ab8}Your own voice cuts you open. Sweet. Effortless. Higher than yesterday, higher than five minutes ago, and full where it used to be flat.{/color}"
    hrl_you "\"...Hello?\""
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg="hrl_voice_miki")
    hrl_miki "\"Oh, that's climbing! Say something long. Give me a race count, manager! On your marks!\""
    hrl_you "\"I'm not giving you a—\""
    "It skates up the scale on every word. Nao leans in the doorway with a towel round her neck, starstruck."
    hide hrl_miki
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"It's so sweet. Yuu, let me hear?\""
    hide hrl_nao
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Means it's time. Tradition. Everyone helps set the throat. Desk's the best height.\""
    hide hrl_miki
    jump hrl_voice_desk

label hrl_ch8_after:
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "smirk")], cg="hrl_phone")
    "The clubroom's ancient wall phone rattles. Rei holds out the receiver without looking up."
    hrl_rei "\"For you. Coach wants your sizing for the meet list.\""
    show screen hrl_pool(8)
    "Everyone goes quiet. Miki's chalkboard has odds on it."
    hide screen hrl_pool
    menu:
        "The phone, held out."
        "Take it":
            $ hrl.phone = "took"
            hrl_you "\"Hello?\""
            "Honeyed. High. You try dropping it to the old deadpan, and it sounds like a girl doing an impression of a boy."
            hide hrl_rei
            show hrl_ida nod at vn_cast_slot
            hrl_ida "\"...Yuu?\""
            hrl_you "\"Uh— yes, Coach.\""
            "You get through the numbers somehow. Behind you Miki is hammering a locker in silent hysterics. You hang up too fast."
            hrl_you "\"Never. Pick up. The phone. Again.\""
        "Let it ring":
            $ hrl.phone = "rang"
            "You shake your head. Rei answers it herself: \"She can't come to the phone, Coach. Voice is setting.\" A pause. \"Yes. That's what I said.\""
            hrl_you "\"I'm not a she yet!\""
            "It comes out so sweet that the whole room cheers."
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_dorm", pc="dazed", pc_tag="hrl_pc", cast=[], cg="hrl_humming")
    "That night in your dorm bed you catch yourself humming, high and true, and feel every note go straight down to the anchor."
    "You try a sentence into the dark. {i}My name is Yuu Takase. I run the ten thousand.{/i} It comes out like a girl reading a line in a play about a boy. You try it again, lower. Lower is worse: lower is a woman being husky."
    "You give up and hum instead, and your hand drifts down under the duvet without asking, and the anchor's already wet and waiting for it."
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch9

## ---- 9. Face and Hair ----------------------------------------------------------------------------
label hrl_ch9:
    $ hrl.chapter = 9
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_bath", pc="dazed", pc_tag="hrl_pc", cast=[], cg="hrl_bath_hair")
    "The club bath, empty for once. Your hair tickles your nape on Monday, brushes your neck on Wednesday, lies on your shoulders by Friday: deep plum, glossy, nothing like the black mop you grew up with."
    "In the fogged mirror over the taps your face is going. Cheekbones softening, the jaw smoothing, lips filling. Every morning there's less of the old slant of your mouth to find."
    "The team chat buzzes: {i}DINNER. RAMEN. MANDATORY. NO HOODIES.{/i}"
    hide cg onlayer cgl
    $ vn_until(19)
    $ hrl.fit = "kit"
    $ vn_enter(bg="hrl_ramen", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_rei", "smirk")], cg="hrl_dinner")
    "The team tee, the sports bra, the only shorts that still go over the hips. The ramen place Rei picked for its private room, the whole club round one low table, Kaede at the end."
    "The room goes silent when you walk in, and then it erupts."
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Who's THAT? Star power!\""
    "Hands reach for you from every side: tracing your jaw, tucking hair behind your ear. Kaede pushes her bowl aside."
    hide hrl_rei
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"I told you. The skin remembers. Bring a mirror, Rei.\""
    "Rei flicks open a compact. In the little silver circle is a face that is yours, if you had been born a woman: your own eyes, deepened, lashes longer, a mouth made for the voice that comes out of it."
    hrl_you "\"It's not that different.\""
    hide hrl_rei
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"It's beautiful. You're beautiful.\""
    hide hrl_kaede
    hide hrl_miki
    hide hrl_nao
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"To our star.\""
    "Halfway through the first bowl it happens: the last edge of your chin softens, your lower lip tingles and swells, and Nao's thumb stops on your cheek."
    hide hrl_rei
    show hrl_nao gentle at vn_cast_slot
    hrl_nao "\"It's setting.\""
    $ hrl_body(8)
    $ hrl.she = True
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"Right, I'm not waiting. Table's closed for the night.\""
    hide hrl_rei
    jump hrl_face_store

label hrl_ch9_after:
    hide cg onlayer cgl
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_storeroom", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_ida", "nod")], cg="hrl_ida_uniform")
    "The storeroom door opens and Coach Ida fills it, arms loaded. She looks at the new face and hair for a long moment, nods once, and drops the club manager's uniform in your lap: white, gold piping, newly tailored."
    hrl_ida "\"Hm.\""
    "There are no more questions. The face is set, and every one of them sees her as theirs."
    show screen hrl_pool(9)
    "Back at the clubroom, Miki pays out to the whole team."
    hide screen hrl_pool
    hide cg onlayer cgl
    hide hrl_ida
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch10

## ---- 10. The Meet --------------------------------------------------------------------------------
label hrl_ch10:
    $ hrl.chapter = 10
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_meet", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_meet_trackside")
    "The exhibition meet. She walks the infield in the sun in the white manager's uniform, clipboard in hand, plum ponytail swinging, calling the start orders in a voice that turns heads at the first syllable."
    "A rival coach stops mid-sentence to stare. The commentator, scrambling for a name, says \"The Seiran star is back—\" and trails off."
    "Across the rail Kaede watches her own figure walk again on someone else, and grins."
    hrl_rei "\"Miki's in the hundred. It's your turn, manager. Tent.\""
    hide cg onlayer cgl
    hide hrl_rei
    jump hrl_meet_tent

label hrl_ch10_after:
    hide cg onlayer cgl
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_meet", pc="bright", pc_tag="hrl_pc", cast=[], cg="hrl_meet_awards")
    "Seiran sweeps the relay, Miki finishing the last leg with her arms up. The manager stands in the awards line with her hips swaying and her thighs still sticky, and coaches who knew Kaede look at her like they've seen a ghost."
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_meet", pc="bright", pc_tag="hrl_pc", cast=[("hrl_nao", "gentle")], cg="hrl_bus_home")
    "The bus home, everybody sunburnt and hoarse. Nao falls asleep on her shoulder within ten minutes. Miki's counting her winnings at the back. Rei's doing next week's schedule on her knee with a pencil."
    "She looks at her own reflection in the dark window: the plum ponytail, the soft mouth, Nao's head on her shoulder, the white uniform with the gold piping. She looks for a long time for the man who used to sit at the back with headphones in and his hood up."
    "He isn't there. She finds she doesn't miss him the way she thought she would. She puts her cheek on top of Nao's head and watches the motorway go by."
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch11

## ---- 11. Shoulders and Frame ---------------------------------------------------------------------
label hrl_ch11:
    $ hrl.chapter = 11
    $ hrl.fit = "bra"
    $ vn_enter(bg="hrl_clubroom", pc="dazed", pc_tag="hrl_pc", cast=[], cg="hrl_hands")
    "She looks at her hands in her lap. Slim wrists tapering into long fingers; no hint of the blunt knuckles from last year's relays; nails pale and neat as if they'd never touched a lane marker."
    "In the locker mirror her collarbones are finer and her shoulders are drawing in: not weaker, honed, a sprinter's shoulders on a woman. The frame is the last of him, and it's going."
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="flustered", pc_tag="hrl_pc", cast=[("hrl_kaede", "hungry")], cg="hrl_wrists")
    hrl_kaede "\"Still growing in? Almost there.\""
    hide hrl_kaede
    show hrl_rei calm at vn_cast_slot
    hrl_rei "\"Let us see.\""
    "Rei draws the top up over her breasts and off. Kaede takes both her wrists in one big hand and lifts them, and spreads her other palm over the new slope of her shoulder."
    hide hrl_rei
    show hrl_kaede smirk at vn_cast_slot
    hrl_kaede "\"Smooth. Almost the exact print. You know there's only one way to finish it.\""
    hrl_you "\"I know. I want it.\""
    hide hrl_kaede
    jump hrl_frame_both

label hrl_ch11_after:
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="dazed", pc_tag="hrl_pc", cast=[("hrl_rei", "soft")], cg="hrl_rei_thigh")
    "She lies with her head on Rei's bare thigh, flexing her new shoulders and rolling her new wrists, and reaches for something of the old him. An echo. Anything."
    "There's nothing there but want, and it doesn't frighten her."
    hrl_you "\"More.\""
    hrl_rei "\"Soon. We'll finish it soon.\""
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch12

## ---- 12. The Star Reborn -------------------------------------------------------------------------
label hrl_ch12:
    $ hrl.chapter = 12
    $ hrl_body(9)
    $ hrl.fit = "nude"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[], cg="hrl_finished")
    "It happens in the night, quietly. A tingling burn up the bones of her arms, a prickle through the shoulders and wrists. By dawn every last rough edge is gone."
    "{color=#c58ab8}She stands and stretches, and her body rises in one long athletic line: Kaede's figure at twenty-one, built over her own, every muscle long, every proportion tuned for speed and hunger.{/color}"
    hide cg onlayer cgl
    $ hrl.fit = "bra"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "soft")], cg="hrl_morning_star")
    hrl_rei "\"Morning, star. How does it feel?\""
    hrl_you "\"Done. There's nothing left of— Is it weird that I'm almost—\""
    hrl_rei "\"That's exactly the point.\" She lifts your chin. \"Ready? Everyone's waiting.\""
    "Rei takes the old men's-team hoodie off the hook where it's hung all term and folds it, neatly, in quarters, the way she folds kit at the end of a season, and puts it on the bench."
    hrl_rei "\"You won't need this.\""
    hrl_you "\"I know.\""
    "It's the first time you've said it without arguing. Rei looks at you a long moment, and then she smiles, the real one, the one she saves for meets."
    hide hrl_rei
    jump hrl_consecration

label hrl_ch12_after:
    hide cg onlayer cgl
    $ hrl.fit = "bra"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "soft")], cg="hrl_roster")
    "Rei is waiting with the club roster and a new marker."
    hrl_rei "\"It's time.\""
    show screen hrl_sheet(7)
    "Every box on the sheet is ticked. She takes the marker and writes a new line at the bottom of the roster, bold and final: her own name, with the ending it was always missing."
    hide screen hrl_sheet
    $ hrl_pc_name = "Yuuka"
    hrl_rei "\"Yuuka.\""
    hrl_you "\"Yuuka.\""
    "The hoodie hangs forgotten on a hook. The team piles round her, cheering."
    hide cg onlayer cgl
    hide hrl_rei
    $ hrl_next_week()
    call vn_night(7)
    jump hrl_ch13

## ---- 13. Full Recruit ----------------------------------------------------------------------------
label hrl_ch13:
    $ hrl.chapter = 13
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_uniform_fit")
    "Rei holds up the white uniform like a ceremony: feminine-cut, banded at the waist, gold piping, YUUKA stitched above the breast. She buttons it on Yuuka herself and kneels to smooth the skirt down her thighs."
    hrl_rei "\"Manager. From today you're responsible for the roster, the equipment, the hydration, and—\" a glance at Kaede \"—keeping morale dangerously high.\""
    hide hrl_rei
    show hrl_miki grin at vn_cast_slot
    hrl_miki "\"That last one's the main job!\""
    hrl_you "\"What's first, Captain?\""
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_track", pc="bright", pc_tag="hrl_pc", cast=[("hrl_miki", "tease")], cg="hrl_manager_day")
    "It takes exactly one sunrise for the new normal to set. Nao in the bath at dawn. Miki groping her through breakfast. Rei handing her the day's duties, typed: hydration charts, kit checks, and {i}Afternoon: anchor maintenance (compulsory, full roster).{/i}"
    "She runs water and hugs up and down the track all practice, fending off hands that keep slipping up her skirt, and she loves every bit of it."
    hide cg onlayer cgl
    hide hrl_miki
    jump hrl_roster_session

label hrl_ch13_evening:
    hide cg onlayer cgl
    $ vn_until(20)
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_kaede", "smirk")], cg="hrl_kaede_door")
    "Evening, and Kaede's send-off. She fills the clubroom doorway in a half-buttoned shirt, palms the trunk like a talisman and sits on its edge."
    hrl_kaede "\"Come here. Let me see what I'm passing on.\""
    jump hrl_sendoff

label hrl_ch13_after:
    hide cg onlayer cgl
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_rei", "calm")], cg="hrl_trunk_again")
    "When Kaede has gone, Rei unlocks the trunk to put the old hoodie away in it."
    "The skin is lying on the velvet. New, warm, seamless, holding its shape, as if it had never left."
    hrl_rei "\"It always comes home once a star's finished. Kaede's did.\""
    hrl_you "\"So next year—\""
    hrl_rei "\"Next year.\""
    "Yuuka locks the trunk herself, and keeps the key."
    hide cg onlayer cgl
    hide hrl_rei
    $ vn_clock.day += 330
    call vn_night(7)
    jump hrl_ch14

## ---- 14. Next Year's Trunk -----------------------------------------------------------------------
label hrl_ch14:
    $ hrl.chapter = 14
    $ hrl.fit = "uniform"
    $ vn_enter(bg="hrl_clubroom", pc="bright", pc_tag="hrl_pc", cast=[("hrl_miki", "grin")], cg="hrl_recruit_week")
    show screen hrl_pool(14)
    "Recruitment week, a year on. Flyers on every field-house door, bouquets on the old bench. Miki stuffing ballots for FIRST TO SET into a new envelope."
    hide screen hrl_pool
    show cg hrl_shun_window onlayer cgl
    "And outside the office window, the one the club has been watching: Shun, twenty-four, a tall quiet engineer who walked on in April, trains with the women because the men's squad had no distance runners, and lost the interval to Miki this afternoon by a stride."
    "The anchor tingles in Yuuka's pelvis, the same brisk hungry hum it once ached with for her."
    "She watches him stretch against the fence, long and quiet and determined, the way she must have looked to them. A man who thinks the worst thing that can happen this year is losing an interval."
    hrl_miki "\"Look at him. He's got no idea.\""
    hrl_you "\"Neither did I.\""
    hrl_miki "\"You had {i}some{/i} idea. You saw the trunk.\""
    hrl_you "\"I saw a box. I thought it was spikes.\""
    "Miki laughs so hard she has to hold the window frame. Out on the track, Shun looks up at the noise, and sees two women at the office window, and goes back to stretching, a bit red."
    hide hrl_miki
    jump hrl_next_recruit
