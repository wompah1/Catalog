## THE SOURCE: club's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, ending.twee), written as beats; the director scenes are in
## scenes.rpy, the clubroom and its duties in duties.rpy. The original is in
## catalog/docs/routes/vn-original/club/. Eight days, one event each: the box; camp; camp's
## return; the qualifiers and the night bus; the inspection; the slump; the slump's morning and the
## semifinal; nationals, the banquet and the balcony. The clubroom offers the day's duties (once
## each a day, flavour) before the day's rung, or before the night.

## ---- DAY 1: the CV, the noticeboard, the box (Club Opening) -------------------------------

label clb_opening:
    $ clb.fit = "own"
    $ vn_enter(bg="clb_domus_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_cv")
    "Your room at the top of a narrow house on Domus Street. A single bed. A desk. A kettle. Your CV on the screen."
    "{color=#e8c35a}[clb_pc_name] Doyle. Twenty. Second-year.{/color} Under {i}Experience{/i}: nothing. Under {i}Interests{/i}: a list of hobbies."
    "You stare at it. It stares back."
    clb_you "\"Unacceptable.\""
    hide cg onlayer cgl
    $ vn_enter(bg="clb_corridor", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "You tell it. Up the hill to campus. The main corridor. The noticeboard, under a fire extinguisher. Society fairs. A lost umbrella. And, in a font you approve of:"
    show screen clb_slip("MEN'S VOLLEYBALL CLUB NEEDS A MANAGER.", ["No experience needed. Enrolment not required; the club has never once checked.", "Ask for the coach. Sports hall, any afternoon."])
    "Logistics. Schedules. Kit. A line on the CV with a verb in it."
    hide screen clb_slip
    clb_you "\"Perfect.\""
    "You say it out loud, in the corridor. A passing student edges round you.\n{size=-5}{color=#ff8fa3}▸ The sports hall{/color}{/size}"
    $ vn_pass(30)
    jump clb_box

## ---- RUNG 1: the box, "Thirty years.", the regimen, tea service (non-con), the captain -------

label clb_box:
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The sports hall. Squeaking trainers, the {i}thwack{/i} of a ball on a forearm, the smell of floor polish and effort."
    show clb_coach flat at vn_cast_slot
    "The coach is by the door. Sixty if he's a day. Grey tracksuit zipped to the chest, the whistle cord looped round his neck three times like a medal. He takes your CV, looks at it once, and passes it over his shoulder to the roster."
    clb_other "\"Oh, he's {i}keen{/i}.\""
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"So you're our new manager? Ollie. Vice-captain. Twenty-one. I run the board.\""
    "A grinning one, all hair and knees, bouncing on the spot."
    clb_you "\"What board?\""
    clb_ollie "\"Don't worry about the board.\""
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Hugh. Middle blocker. I'm twenty-one too.\""
    "Behind him, a wall of a man waves shyly. And the roster behind him: nineteen to twenty-three, sweaty, curious, every pair of eyes going up and down you."
    show clb_rhys composed at vn_cast_slot
    "The captain doesn't wave. Tall, composed, upright, a towel round his neck. Rhys Langford, twenty-two, ace. He nods at you once, like he's either approving or mourning something."
    show clb_ollie grin at vn_cast_slot
    show cg clb_the_box onlayer cgl
    clb_ollie "\"Club tradition! Open it! Gotta check the size!\""
    "Ollie shoves a box into your arms. Big. Tied with ribbon. Heavier than it looks. You open it."
    "White blouse. Ribbon tie. Socks. Loafers. And folded on top, pressed flat, a shade deeper than the court lines: a skirt."
    "You turn it over. New. Tagged. Exactly your size."
    clb_you "\"Ah.\""
    hide cg onlayer cgl
    show clb_coach flat at vn_cast_slot
    "The coach clears his throat. Everybody goes quiet. He speaks for the first time."
    clb_coach "\"{color=#ff8fb8}Thirty years.{/color}\""
    "And that settles it. You'll find, over the season, that it settles everything.\n{size=-5}{color=#ff8fa3}▸ Put it on in the equipment room{/color}{/size}"
    $ vn_pass(10)
    jump clb_box_dressed

label clb_box_dressed:
    $ vn_enter(bg="clb_equipment_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The equipment room has a lock. The clubroom doesn't. That distinction will stop mattering fast."
    $ clb.fit = "u1"
    "Blouse. Tie. Socks. Loafers. Plain white panties, folded in the bottom of the box, because the box is thorough. The skirt zips at the hip and swings when you turn."
    "It fits. Of course it fits."
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_applause")
    "You step out. The roster stops dead."
    "Then Ollie starts clapping. The clapping isn't sarcastic, which is somehow much worse. Everybody joins in. Hugh's clapping so hard the benches rattle."
    "The captain doesn't clap. His ears have gone brick-red and he's looking very hard at the floor."
    show clb_ollie loud
    clb_ollie "\"{color=#ff8fb8}SWEETHEART!{/color} That's you! Club name! The manager's always Sweetheart!\""
    "Arms wide."
    clb_you "\"Manager's fine.\""
    clb_roster "\"Sweetheart.\""
    "Says the whole roster, warmly, at once. Your name is Sweetheart now."
    hide cg onlayer cgl
    clb_ollie "\"FIT CHECK!\""
    show cg clb_fit_check onlayer cgl
    "Suddenly there are hands everywhere. Tugging the hem straight. Smoothing the blouse down your back. A palm on your hip, checking the zip. A squeeze of your ass, through the skirt, very professionally."
    show clb_pc flustered
    clb_you "\"That's— hands— the zip's on the {i}other{/i} side—\""
    "You swat a wrist away. Two more take its place."
    clb_ollie "\"Just checking it all over, Sweetheart.\""
    "Another squeeze, slower. Somebody straightens your tie and their knuckles brush your nipple through the cotton, and it goes stiff, and you go pink, and the roster goes \"{i}ohhh{/i}\"."
    show clb_hugh sincere at vn_cast_slot
    clb_hugh "\"Fits. Fits perfect.\""
    hide cg onlayer cgl
    "Hugh announces it, solemnly, with both hands on your waist.\n{size=-5}{color=#ff8fa3}▸ Somebody important just walked in{/color}{/size}"
    jump clb_box_regimen

## Madame Lacroix and the regimen: complimentary, as it has been for thirty years. The first leaflet
## goes under S, unread.
label clb_box_regimen:
    $ clb.boxes = 1
    $ clb.leaflets = 1
    $ clb_mark("regimen")
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    vn_sfx "{i}Click. Click. Click.{/i}"
    show clb_lacroix warm at vn_cast_slot
    "Heels on the sports hall floor. Powder-blue suit. Pearls. Silver at the temples, a smile like a warm bath and eyes like a filing cabinet. Fifty-one, and she runs half the alumni office by accident on her lunch breaks."
    hide clb_lacroix
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Madame Margot Lacroix. Alumnae president.\""
    "Ollie whispers it, reverent."
    show clb_lacroix pleased
    clb_lacroix "\"So this is our new manager. Oh, it fits beautifully.\""
    "She looks you over, hem to tie, and seems enormously pleased about something."
    clb_you "\"It's very practical. Good airflow.\""
    clb_lacroix "\"Isn't it. The sponsor's conditioning regimen. For the manager. One sachet a day, the schedule's on the card. It's complimentary. As it has been for thirty years.\""
    show cg clb_regimen_box onlayer cgl
    "From her handbag: a box in sponsor blue, tied with a ribbon. A tiny, friendly pause. A laminated card. Sachets in rows. And a leaflet folded under the card."
    "You read the card, because the card is operational. You read the leaflet as far as {color=#e8c35a}complimentary{/color}."
    "That's all you need. Free things are good logistics."
    show cg clb_folder_s onlayer cgl
    "The leaflet goes in the club's document box. Under S."
    "You won't read it. Not once, all season. It's not that you decide not to. It just never becomes the most useful thing to do next.\n{size=-5}{color=#ff8fa3}▸ Tea service{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(60)
    jump clb_box_tea

## Rung 1's dominant act: your mouth, the roster one at a time, non-con. "Next" stops being
## permission: THEY call it, over your objections. Hugh first, Ollie narrating.
label clb_box_tea:
    $ clb_mark("tea")
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "After practice. The clubroom. The duty sheet is pinned by the kettle, and you read it like a contract."
    "{color=#e8c35a}Tea service.{/color} Kneeling, at the low table. You can do that."
    show cg clb_kneel_pour onlayer cgl
    "You kneel. The skirt folds under your knees. You pour: cups in a row, lemon for the big one, two sugars for Ollie, who claims he takes none. The roster sprawls on the benches, steaming, watching your hands."
    "Then the second line. Same font as the bus rota."
    "{color=#ff8fb8}{i}Second course: hydration support, by rotation.{/i}{/color}"
    "You read it twice. It means exactly what it looks like. Hugh's already kneeling opposite you, untying his drawstring with enormous care."
    show clb_pc flustered
    clb_you "\"No. No. That is a typo. That is a {i}clerical{/i}—\""
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Thank you, manager.\""
    "You haven't done anything yet."
    clb_you "\"I haven't agreed to— Hugh. {i}Hugh.{/i} Put that— put that {i}away{/i}—\""
    show cg clb_hugh_head onlayer cgl
    "He doesn't. It's out, thick and flushed and right in front of your face, and his big hand settles on the back of your head. Very gentle. Completely immovable."
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Look at that FORM. Hold him, Hugh— there we go. Breathe through your nose, Sweetheart.\""
    "Ollie says it from the bench, and gets up, and kneels behind you, and takes both your wrists in one hand."
    clb_you "\"I am NOT— this is NOT an approved— {i}mmph{/i}—!\""
    vn_sfx "{i}Glk.{/i}"
    show cg clb_first_mouth onlayer cgl
    "Heavy. Hot against your tongue. He smells like the shower he hasn't had yet. You shove back and Ollie's hand on your wrists doesn't move and Hugh's hand on your head doesn't move and Hugh's cock moves, in, out, slow, polite."
    clb_hugh "\"Thank you— thank you, manager— {i}oh{/i}—\""
    show clb_pc loud
    "Every word you've got comes out a wet hum round him. {i}Glk. Glk.{/i} Your eyes go wide. Your face goes hot. And under the skirt your cock goes hard, all at once, like it read a different sheet."
    clb_ollie "\"Ohh, LOOK at that. He says no, gentlemen, but the skirt says—\""
    "Ollie, delighted, glancing down."
    clb_you "\"{i}Mmmf{/i}—!\""
    "Hugh comes fast and apologetic, both hands on your head like it's the trophy. {i}Hot.{/i} {i}Thick.{/i} He holds you there till you swallow, because there's nowhere else for it to go."
    hide cg onlayer cgl
    clb_you "\"That— {i}hah{/i}— that was NOT— on the SHEET—\""
    "You pull off gasping."
    clb_hugh "\"It's on the sheet.\""
    "Sorrowfully, pointing at the sheet."
    show clb_ollie loud
    clb_ollie "\"NEXT! You heard the manager! Orderly line!\""
    menu:
        clb_you "\"I did NOT say—\""
        "\"That is NOT— on the SHEET—\"":
            $ clb.call = "next"
            clb_you "\"That is NOT— on the SHEET—\""
            clb_roster "\"{i}NEXT!{/i}\""
            "Says the whole roster, warmly, at once. Two of them get up at once and have a brief, polite shoving match over who."
        "\"I am filing a COMPLAINT—\"":
            $ clb.call = "line"
            clb_you "\"I am filing a COMPLAINT, in TRIPLICATE—\""
            clb_ollie "\"Noted! Complaint noted! NEXT!\""
            "Somebody behind him is already stepping up."
        "\"Ollie. Get OUT of the—\"":
            $ clb.call = "ollie"
            clb_you "\"Ollie. Get OUT of the—\""
            clb_ollie "\"I'm NEXT, is why.\""
            "He's already got it out, and he's already got your ribbon tie wrapped twice round his fist."
    jump clb_box_rotation

label clb_box_rotation:
    $ vn_enter(bg="clb_clubroom", pc="loud", pc_tag="clb_pc", cast=[("clb_ollie", "loud")], cg="clb_ollie_tie")
    "Ollie, then. He hauls you forward by the tie and doesn't stop talking the whole time."
    clb_ollie "\"And the manager OBJECTS, folks— objection noted— ohh, there's the tongue— the crowd goes— {i}fuck{/i}, Sweetheart—\""
    vn_sfx "{i}Slrp. Glk. Glk.{/i}"
    "You grab his hips to push him off and he takes it as a handle and fucks your mouth, quick and bouncy, trying to high-five somebody mid-thrust. You pinch his thigh. He yelps and keeps going."
    clb_ollie "\"Page five, Sweetheart. Shh. Ohh, carry ON— ten points a— {i}hhnnh{/i}—!\""
    "He cums in about the time it takes to say \"ten points a set\", which he tries to."
    clb_ollie "\"NEXT!\""
    clb_you "\"I didn't— {i}hah{/i}— I didn't SAY— {i}mmph{/i}—\""
    show cg clb_rotation onlayer cgl
    "Then the next. And the next. One at a time, and none of them waiting for you."
    "A setter with a nervous laugh, who wraps your ribbon tie round his fist and comes the second your tongue flicks the underside, trying to say no round him. \"Sorry— sorry— {i}oh{/i}—\""
    "A libero who says \"sorry\" twice and means neither, holds your ears, and fucks your mouth in short greedy jabs. {i}Glk glk glk.{/i} Your eyes go glassy. You hold onto his thighs to shove him off, and your hands forget halfway, and just hold on."
    "An outside hitter so big you can only fit the head. Somebody puts your hands on the rest. Somebody moves them for you, up and down, until your hands keep moving without them, and he makes a noise like a kettle."
    "A quiet one who strokes your hair the whole time and says \"good, good, that's good\" while you say {i}no, no, no{/i} round him, and the no's come out sounding exactly like moans."
    clb_ollie "\"NEXT. NEXT. Hydration support! Hydration! Support!\""
    "Says Ollie, every time. Every one of them on your tongue. Hot and salty and thick. Your jaw's loose and buzzing. Your chin's wet. Your cock is hard as a rail inside the plain white panties, tenting the skirt, leaking a wet patch through the cotton, and nobody's touched it, and you didn't tell it to."
    clb_you "\"Mmh— {i}mmnh{/i}— this is NOT— {i}hah{/i}— throughput is— why is throughput— {i}mmMMH{/i}—!\""
    show cg clb_rotation_last onlayer cgl
    "By the last one you're not pushing anybody. You're sucking. Moaning round him, loud, wet, your own hips rocking against nothing, and when he pulls out you chase him with your mouth open before you catch yourself."
    clb_you "\"{i}Hah{/i}— {i}hah{/i}— that's— {i}please{/i}— somebody— my— {i}hnnngh{/i}—\""
    "You don't know what you're asking for. Your cock knows. Nobody's on the sheet for that."
    clb_ollie "\"Tick it, Sweetheart.\""
    "Ollie picks up your clipboard and puts it in your shaking hands. You tick a box. Your handwriting's all over the place.\n{size=-5}{color=#ff8fa3}▸ Wait for the room to clear{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(30)
    jump clb_box_captain

## The captain last, slow, the one who waits; and he asks. Rung 1 lands here.
label clb_box_captain:
    $ clb.tier = max(clb.tier, 1)
    $ clb.rung_day = vn_clock.day
    $ vn_enter(bg="clb_clubroom", pc="loud", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg=None)
    "The room clears. Showers hiss down the corridor. Somebody's singing."
    "The captain's still on the bench."
    "He comes over and kneels where Hugh knelt, and doesn't touch his drawstring. He looks at your wrists, pink where Ollie held them, and at your chin, and his jaw goes tight."
    clb_rhys "\"You don't have to. Not for me. Say no and I'll go and shower.\""
    "Low. Nobody's asked you anything all afternoon. You stare at him."
    show clb_pc soft
    clb_you "\"...It's on the sheet, Captain. And you asked.\""
    show clb_rhys red
    clb_rhys "\"Right. Right.\""
    show cg clb_captain onlayer cgl
    "His ears go brick-red. He unties. He's slow. Nothing like the others. His hand on the back of your head is barely there. He watches your face the whole time, like he's taking notes. When you take him deep he makes a noise like he's been punched."
    "He's bigger than Hugh. You didn't think that was possible. You can't get him all the way, so you do what you can: lips stretched round the head, tongue working the underside, one hand pumping the rest, slick with your own spit."
    vn_sfx "{i}Slrrp. Glk.{/i}"
    clb_rhys "\"You're— you're {i}really{/i} good at this.\""
    "Sounding personally betrayed. You pull off with a wet pop."
    clb_you "\"I have notes.\""
    clb_rhys "\"{i}God{/i}.\""
    "He puts his hand over his face, and you take him back in."
    show clb_pc loud
    clb_you "\"{i}Mmh{/i}— mmnh— {i}mmmh{/i}—!\""
    "You're louder for him than for any of them. You don't know why. You'll look into it."
    clb_rhys "\"Steady. Steady, Sweetheart—\""
    "He comes holding perfectly still. You take all of it." with vnfx("shake")
    hide cg onlayer cgl
    "Then he wipes your chin with his thumb, and leans down, and kisses your forehead."
    clb_rhys "\"No further notes.\""
    hide clb_rhys
    "He goes to shower. You sit back on your heels. Your mouth tastes of all of them, and mostly of him. Your jaw hums. Your lips feel swollen and hot, and when you lick them they're softer than they were this morning."
    "Your cock throbs in your panties, ignored, a wet patch spreading through the plain white cotton where it's been leaking the whole time. You press the heel of your hand on it, once, hard, to make it behave. It doesn't. You leave it."
    show clb_pc deadpan
    "You pick up the clipboard."
    show screen clb_clipboard(1)
    "{i}[CLB_CLIPBOARD[1]]{/i}\n{size=-5}{color=#ff8fa3}▸ Home for the night{/color}{/size}"
    hide screen clb_clipboard
    call vn_night(7)
    jump clb_morning

## The morning after a rung's night: the body change that lands overnight, and one spoken
## misreading. (Rungs 1, 3 and 4.)
label clb_morning:
    $ vn_enter(bg="clb_domus_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    if clb.tier == 1:
        "You reach for the razor out of habit."
        $ clb_body(1)
        show cg clb_dry_razor onlayer cgl
        "{color=#ff5fb8}Dry. Nothing to shave. Not on your jaw. Not on your legs, your arms, your chest, down there. Smooth everywhere, like you've been sanded, and there's a gloss on your skin like you've been oiled.{/color}"
        "{color=#ff5fb8}You run a hand down your stomach. {i}Slick.{/i} Your nipples go tight. Lower. Your cock. Your balls. Not a hair on them. You cup them and they're {i}silk{/i}, and your cock jumps up hard against your wrist.{/color}"
        show clb_pc flustered
        clb_you "\"{i}Hhn{/i}—! {i}Hah{/i}— {i}hah{/i}—\""
        "{color=#ff5fb8}Both hands up your thighs. Inside, outside, round over your ass. Smooth, smooth, smooth. You can't stop stroking. Your hips push forward into nothing.{/color}"
        hide cg onlayer cgl
        "Your tongue runs along the back of your teeth on its own. A ridge, a slow lick, a swallow, like it's going over yesterday's order of service. You never practised that."
        "{color=#ff5fb8}Your lips tingle when the kettle steam touches them. Inefficient. You lick them anyway.{/color}"
        show clb_pc deadpan
        clb_you "\"Sponsor's very serious about hydration.\""
        $ clb.fit = "u1"
        "You tell the mirror. The uniform's on the chair where you folded it. You put it on without thinking about it."
    elif clb.tier == 3:
        "You slept in the blouse. Iris's red ribbon is on the bedside table, next to the clipboard."
        "There's a pale ghost on the inside of your knee, where his thumb was. You touch it. Your cock twitches."
        "Your thighs press together under the duvet, soft and heavy. Your chest is two small soft handfuls, and the nipples are puffy and tingling from the blouse rubbing them all day. You press one with a fingertip. {i}Nnh.{/i}"
        clb_you "\"Bus seats.\""
        "You say it, in a voice a step higher than yesterday's, and go and find something else to do."
    else:
        "Your chest tingles. Heavy, warm, good. Your nipples are puffy and buzzing and the ruffled blouse is on the chair, a little crumpled where you got it off in a hurry."
        show clb_pc flustered
        "You cup them. They fill your hands. Soft and heavy and {i}yours{/i}. You squeeze, the way they did, one after another, and remember every one of them, and the \"next\" you started calling yourself, somewhere in the middle, and your little cock twitches in your panties and leaks."
        "The roster's handprints are a bit pink on your chest still. You trace one. That one's Ollie's. You'd know it anywhere."
        show clb_pc deadpan
        clb_you "\"Well-fitted.\""
        "You say it to nobody, and go and make tea."
    "Up to campus.\n{size=-5}{color=#ff8fa3}▸ Up to campus{/color}{/size}"
    $ vn_pass(20)
    jump clb_hub

## A morning with nothing to land: one line for the body the season's left you, the fixture card
## from memory, and up the hill.
label clb_wake:
    $ vn_enter(bg="clb_domus_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    $ renpy.say(None, CLB_WAKES[max(0, min(6, clb.tier))])
    $ _fx = clb_fixture()
    if _fx:
        "{color=#e8c35a}The fixture card, from memory:{/color} [_fx]\n{size=-5}{color=#ff8fa3}▸ Up to campus{/color}{/size}"
    else:
        "The fixture card has nothing on it you haven't already logged.\n{size=-5}{color=#ff8fa3}▸ Up to campus{/color}{/size}"
    $ vn_pass(20)
    jump clb_hub

## ---- RUNG 2: camp, the bath (non-con), the futons; camp's return and WAIST -----------------

label clb_camp:
    $ vn_enter(bg="clb_minibus", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg=None)
    "The minibus. The front seat, which is a tradition, which means it isn't a request."
    "Ollie navigates from the row behind you. Badly. Loudly. Hugh shares his crisps. The captain sits at the back and looks out of the window and, every time you check the mirror, isn't looking at you."
    $ vn_enter(bg="clb_lodge", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_lodge_step")
    "Up into the hills. A lodge with two gables and a curl of steam off the back of it."
    clb_ollie "\"Bathhouse.\""
    "With deep satisfaction. You do tea on the lodge step. Kneeling on the top stair, the skirt round your knees, cups up to the roster one at a time as they climb out with the bags. Cold noses. \"Thanks, Sweetheart.\" \"Thanks, Sweetheart.\" The coach takes his last and nods at you."
    hide cg onlayer cgl
    "Then the handbook. Page four. {i}The manager bathes with the roster. Tradition.{/i}"
    "You read it twice. The alternative is making a thing of it. Making a thing of it would be worse.\n{size=-5}{color=#ff8fa3}▸ The bath{/color}{/size}"
    $ vn_pass(60)
    jump clb_camp_bath

## Rung 2's dominant act: the roster's hands on you under the water, Ollie's round your cock; non-con,
## the book's own camp groping restored. Hands only; nothing goes in you.
label clb_camp_bath:
    $ clb.fit = "towel"
    $ vn_enter(bg="clb_bath", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_bath_in")
    "Steam. Cedar. A big stone bath and the whole roster already in it, shoulder to shoulder, grinning."
    "You come in with a towel round your waist and a clipboard you leave on the bench. Every head turns."
    clb_roster "\"SWEETHEART'S HERE!\""
    clb_ollie "\"In you come! Best spot's between me and the captain!\""
    "You sink in between them. Ollie's shameless shoulder on one side. On the other, the captain, very still, very upright, gripping his own towel like it's a railing."
    show cg clb_shampoo onlayer cgl
    "It starts with your hair."
    clb_ollie "\"Shampoo tradition.\""
    "Three of them are at it before you can ask what page that's on. Fingers in your scalp. Suds down your neck. Somebody's thumbs working your shoulders."
    clb_you "\"That's— that's not on the— actually that's quite efficient.\""
    "You admit it, which is the last thing you'll admit all evening. Then somebody's hand on your thigh. Under the water. Kneading."
    clb_ollie "\"Your skin's insane, Sweetheart. Like— {i}silk{/i}. That's the regimen, that. Marcus, feel this, verify it—\""
    show clb_pc flustered
    clb_you "\"Hands— {i}off{/i}— there is nothing to {i}verify{/i}— for verification of {i}WHAT{/i}—\""
    "You grab a wrist. It doesn't come off."
    clb_ollie "\"For VERIFICATION.\""
    show cg clb_soap_chest onlayer cgl
    "Ollie agrees, and squeezes higher. Somebody soaps your chest. Slow circles, round and round, thumbs dragging over your nipples every pass, and they go tight and puffy under the suds, and you make a small high noise you didn't authorise."
    clb_roster "\"Ohh.\""
    clb_ollie "\"Sensitive. Very sensitive. Again, Marcus.\""
    "Marcus does it again. And again. Pinches, this time, gently, rolling them, and your whole body jerks in the water."
    clb_you "\"{i}Hah{/i}— that's— that's not on the—\""
    clb_ollie "\"It's in the handbook. Page five.\""
    clb_you "\"There's no page five.\""
    clb_ollie "\"There is now.\""
    "More hands. Your knees, your calves, up the backs of your thighs. A hand on your stomach. The towel is migrating. You grab for it. Somebody's faster. You grab for {i}that{/i} hand and somebody else takes your wrist and lays it back along the stone, friendly, and holds it there."
    clb_you "\"That's MY— that is club PROPERTY— give that—\""
    $ clb.fit = "nude"
    show cg clb_periscope onlayer cgl
    clb_other "\"Ohh, he's {i}hard{/i}.\""
    "Somebody says it, delighted, and the towel's gone completely, flung onto the bench. Your cock is standing up out of the suds like a periscope. Every eye in the bath goes to it."
    clb_you "\"That is— a circulatory— that's the WATER TEMPERATURE—\""
    clb_roster "\"MORALE!\""
    menu:
        "The bath decides it."
        "Grip the stone":
            "You grip the edge of the stone with both hands, knuckles white, and shove yourself up to get out. Four hands put you straight back down. Somebody peels your fingers off the stone and holds them there, spread, along the edge, like you're on display."
        "\"That's NOT page five—\"":
            clb_you "\"That's NOT page five— that's not ANY page— I have READ the handbook, there is no—\""
            clb_ollie "\"Shh, Sweetheart.\""
            "Two of them take an arm each and lay them out along the edge of the stone, and hold them there."
    jump clb_camp_hands

label clb_camp_hands:
    $ vn_enter(bg="clb_bath", pc="loud", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_bath_hands")
    "Ollie's hand closes round your cock."
    clb_you "\"{i}Ah{/i}—! Ollie— {i}OLLIE{/i}— hands OFF the—\""
    clb_ollie "\"There we go.\""
    "Like he's tuning an engine. {i}Shlk. Shlk.{/i} Slow and slippery in the bathwater, thumb over the head every time."
    "You try to close your knees. Hands on your inner thighs pull them apart again, and hold them, wide, under the water. Somebody's at your nipples. Hugh, very politely, has your feet in his lap and won't give them back. Fingers on your stomach, your hips, the crease of your thigh, everywhere, everywhere, hands and more hands."
    clb_you "\"Section four— section {i}four{/i}— conduct in shared facilities— {i}nnh{/i}— get {i}OFF{/i}—\""
    clb_ollie "\"Nobody's read section four, Sweetheart.\""
    vn_sfx "{i}Shlk. Shlk.{/i}"
    clb_you "\"Appendix— {i}hah{/i}— appendix THREE says— {i}ahh{/i}— says the manager is— is NOT to be— {i}nnnh{/i}—\""
    "Your hips jerk up into his fist. You didn't tell them to. You tell them to stop. They don't."
    clb_you "\"Ollie— this is NOT— why is throughput— why is it— {i}stop{/i}— {i}don't{/i}— {i}hah{/i}—\""
    "He slows down. Right at the edge. Just to watch you squirm in all the hands."
    clb_you "\"Ollie— {i}Ollie{/i}— you've— {i}you've stopped{/i}—\""
    "And then you hear what you just said, and go scarlet to the ears."
    clb_ollie "\"Say it. Say the word, Sweetheart.\""
    clb_you "\"I will NOT—\""
    clb_roster "\"MO-RALE. MO-RALE. MO-RALE.\""
    "Chants the bath, slapping the water."
    clb_you "\"{i}No{/i}— no— I'm NOT— {i}hnnh{/i}— ...{i}morale{/i}.\""
    show cg clb_bath_peak onlayer cgl
    "He squeezes. You gasp it, hating it, and he starts again, faster. {i}Shlk shlk shlk shlk.{/i} The water slops over the edge. Your hips jerk up into his fist. Somebody's pinching your nipples in time. Somebody's thumb is pressing your perineum through the water, rubbing, and your thighs try to close and four hands hold them open. Your voice cracks on the ceiling and comes back down off the cedar."
    clb_you "\"Stop— {i}stop{/i}— I'm going to— {i}don't{/i} make me— not in front of the whole— {i}please{/i}— oh god— oh {i}god{/i}— {i}don't stop{/i}— morale is {i}EXCELLENT{/i}— morale— {i}MORALE{/i}— {color=#ff8fb8}MORAAALE{/color}—!\"" with vnfx("shake")
    "You come so hard your back comes off the stone. {i}Spurt. Spurt. Spurt.{/i} Up out of the water in ropes, across your own stomach, across Ollie's wrist."
    "The bath {i}cheers.{/i} Actual cheering. Somebody whistles. Hugh claps, wet, delighted."
    hide cg onlayer cgl
    show clb_rhys red at vn_cast_slot
    "And the captain stands up. Water sheets off him. His ears are scarlet. He doesn't look at anybody."
    clb_rhys "\"{color=#ff8fb8}Enough.{/color}\""
    $ clb.fit = "towel"
    show cg clb_towel_fix onlayer cgl
    "Silence. He wades over, and the hands on you let go one by one as he passes. He takes your towel off the bench, and wraps it round your waist himself. He tucks it with excessive precision. Then again. Then a third time, until it's perfect."
    clb_ollie "\"Ooh. Captain's privilege.\""
    clb_rhys "\"Shut up, Ollie.\""
    hide cg onlayer cgl
    "He climbs out.\n{size=-5}{color=#ff8fa3}▸ Futons{/color}{/size}"
    $ vn_pass(90)
    jump clb_camp_futons

## The futon rows. His fingers find yours in the dark, and that's all.
label clb_camp_futons:
    $ clb.fit = "u1"
    $ vn_enter(bg="clb_futons", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The common room: futons in rows, wall to wall. You draw the sleeping plan on the clipboard. Manager in the middle. Tradition. Appendix three."
    "They pile on you anyway. Ollie draped across your legs. Somebody brushing your hair dry, very gently, with his own brush. Goodnight squeezes all round. A kiss on your cheek from Hugh, who goes bright red and apologises to the ceiling."
    "In the dark, a goodnight squeeze from Ollie, under the blanket, on your cock. Just a squeeze. Then another. Then a slow, friendly stroke through your panties, like he's tucking you in."
    clb_you "\"{i}Ollie{/i}—\""
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Goodnight tradition. Squeeze for luck. Squeeze for morale.\""
    "He whispers it. {i}Squeeze.{/i} {i}Squeeze.{/i}"
    show clb_pc flustered
    clb_you "\"Nnh— that's— {i}hah{/i}— you're making that up—\""
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"Ollie.\""
    "From your other side, flat as a floorboard. The hand goes."
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Night, Captain.\""
    "Innocent as anything, and he's snoring inside a minute. Then lights off. Snoring. Ollie on one side of you, already gone. On the other side, the captain. On his back. Wide awake. You can hear it."
    show clb_rhys composed at vn_cast_slot
    clb_rhys "\"You alright?\""
    show clb_pc deadpan
    clb_you "\"No damage sustained. Morale excellent.\""
    show cg clb_fingers_lace onlayer cgl
    "A long, long breath out. You can feel the heat off him from here. You can hear him swallow. Under the blankets, his fingers find yours. Lace through. Hold on. His thumb strokes the back of your hand, slow, over and over, and your whole body hums from it, more than from any of the hands in the bath."
    "That's all. That's all night.\n{size=-5}{color=#ff8fa3}▸ The minibus home{/color}{/size}"
    call vn_night(12)
    jump clb_camp_home

## Back at the clubroom: the waistband cuts in somewhere new (rung 2's body), the first reorder ("the
## laundry"), and Ollie pays out WAIST at full volume. Rung 2 lands here.
label clb_camp_home:
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "Back at the clubroom. Kit bags everywhere. You go to tuck your blouse in and stop."
    $ clb_body(2)
    show cg clb_waistband onlayer cgl
    "{color=#ff5fb8}The skirt's waistband is cutting in somewhere new. Higher. Tighter. Like there's suddenly a {i}waist{/i} for it to find.{/color}"
    "{color=#ff5fb8}And under it: hips. Soft, round, filling the skirt out sideways. You turn. Your ass pushes the hem up at the back. Your nipples are puffy little points against the blouse, and the cotton drags on them when you breathe.{/color}"
    "{color=#ff5fb8}Both hands on your new hips. You squeeze. They {i}give{/i}, soft and round, and push back into your palms. Round to your ass: a real handful each side, shoving the hem up. You squeeze that too, and your knees go.{/color}"
    show clb_pc flustered
    clb_you "\"{i}Hah{/i}— {i}nnh{/i}— {i}ahh{/i}—\""
    "{color=#ff5fb8}A thumb across one puffy nipple, through the blouse. Swollen. Sensitive. It tingles all the way down to your cock, which goes hard against the waistband, and your mouth waters at the same time. Your hair's tickling your collar. It wasn't on Friday.{/color}"
    hide cg onlayer cgl
    show clb_pc deadpan
    "The industrial machine runs hot. Everybody knows it runs hot. There's a note about it on the equipment board, in your own handwriting."
    show screen clb_slip("REORDER", ["Skirt: next size, different cut.", "{i}Cause: laundry.{/i}"])
    "So: shrinkage. You fill in the reorder slip."
    hide screen clb_slip
    show clb_hugh sincere at vn_cast_slot
    clb_hugh "\"Already?\""
    "From the doorway, beaming like it's your birthday. Your eyes drop to his shorts and your mouth floods. You swallow twice. You file it under hydration."
    show clb_ollie loud at vn_cast_slot
    "Then Ollie sees you. He goes very still. Then he flings open the closet door, where the board is taped, and grabs the red marker, and turns to the room with his arms in the air."
    clb_ollie "\"GENTLEMEN. The first column pays out. Ladies and gentlemen— well, gentlemen— {color=#ff8fb8}THE MANAGER'S WAIST!{/color}\""
    vn_sfx "{i}SKRRK.{/i}"
    $ clb.tier = max(clb.tier, 2)
    $ clb.rung_day = vn_clock.day
    show screen clb_board
    "A red line through {b}WAIST{/b}. Uproar. Notes change hands. Hugh hugs somebody."
    hide screen clb_board
    show cg clb_lap_of_honour onlayer cgl
    "Then they grab you. Lap of honour. Up on their shoulders, round the clubroom, hands all over your new hips holding you up, under your thighs, on your ass, somebody's palm flat on your stomach feeling the waist like it's a trophy."
    clb_roster "\"Feel that! FEEL that!\""
    show clb_pc flustered
    clb_you "\"Put me— {i}down{/i}— this is— {i}hah{/i}— unsafe lifting practice—\""
    hide cg onlayer cgl
    "They put you down on the bench and every one of them pats the waistband on the way past. For luck. Your cock is hard again under the skirt and they all see it and they all grin at it, because it gives you away every time."
    show clb_pc deadpan
    show clb_rhys composed at vn_cast_slot
    clb_you "\"Protein intake.\""
    "You say it to the captain."
    clb_rhys "\"...Yeah. Yeah. That.\""
    $ clb.fit = "u2"
    "Looking at your waist. The reorder arrives in the afternoon post, because the association is very efficient. The new skirt's shorter. It fits. It fits perfectly."
    show screen clb_clipboard(2)
    "{i}[CLB_CLIPBOARD[2]]{/i}"
    hide screen clb_clipboard
    jump clb_hub

## ---- RUNG 3: the qualifiers, the lucky hands (non-con); Iris and her ribbon; the night bus ---

label clb_qualifiers:
    $ vn_enter(bg="clb_domus_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "That morning, in the mirror, you stop with the blouse half on."
    $ clb_body(3)
    show cg clb_mirror_handfuls onlayer cgl
    "{color=#ff5fb8}Two soft little handfuls on your chest. A B, easy. Puffy pink tips. You cup one and it {i}fills{/i} your palm, warm, heavy enough to feel. You squeeze.{/color}"
    show clb_pc flustered
    clb_you "\"{i}Hnnh{/i}—!\""
    "{color=#ff5fb8}Your thighs press together, soft all the way down. Your ass sits rounder in the panties than it did on Monday. Your hair's gone wavy, down to your shoulders.{/color}"
    "{color=#ff5fb8}Your hand slides into the panties. Your cock's hard, and it's {i}smaller{/i}. It fits in your fist with room to spare. Your fist moves on it, slow at the root, a twist at the head, and you've never touched yourself like that. Your hand just knows. The other hand's squeezing your tit. You moan at the mirror like a fire drill.{/color}"
    show clb_pc deadpan
    clb_you "\"Shrinkage.\""
    hide cg onlayer cgl
    "You tell it, and button the blouse over the lot. You bite your pen on the way out and your whole mouth goes hot."
    clb_you "\"{i}Mmh{/i}— that's a pen. That's just a PEN.\""
    $ vn_enter(bg="clb_coach_bus", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_front_seat")
    "The coach to the qualifiers. Front seat."
    "{color=#ff5fb8}Your thighs fill it. They didn't used to fill it. They press together, soft and warm, all the way down to your knees, and the shorter skirt rides up when you sit. The blouse's buttons pull across your chest. Small soft handfuls. When you lean to check the route, they sway.{/color}"
    clb_you "\"Morning.\""
    "To the driver. It comes out a step higher than it used to."
    clb_other "\"Morning, Sweetheart.\""
    hide cg onlayer cgl
    "Says the driver, who isn't even in the club."
    $ vn_enter(bg="clb_venue", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_timeout_tea")
    "The venue: banners, rival kits, a gym three times the size of yours, and stands full of people. You set up the tea service at the end of the bench. Kneeling. Every timeout. Cups up the line."
    "It works. It works so well it's embarrassing. Every time you pour, they win the next point. The bench decides it's luck. Then they decide {i}you're{/i} luck."
    clb_other "\"Lucky touch!\""
    "A hand on your knee as a sub sits down. \"Lucky touch!\" A hand on your thigh. Ollie flips your hem up at the back as he jogs past, in front of the whole stand."
    show clb_pc flustered
    clb_you "\"{i}Ollie.{/i} Hands— that is NOT a— {i}hands{/i}—\""
    clb_other "\"Service ace!\""
    "Somebody yells it, from the court. It is."
    show cg clb_lucky_hands onlayer cgl
    "After that it's every point, and you stop getting to say anything about it. Hands on your hem. Hands on your thighs. A squeeze of your ass when they jog on, a pat when they jog off, big callused palms all the way up under the skirt, in front of everyone, and every one of them followed by a point."
    "The second timeout, you're kneeling, pouring, and three of them at once. A hand flat on your inner thigh. A hand on your ass, under the skirt, kneading the cheek through your panties. Somebody's knuckles, brushing your cock through the cotton, for luck."
    hide clb_ollie
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Lucky touch.\""
    "Apologetically, cupping it."
    clb_you "\"Hugh— get your hand OFF my— not in front of the {i}STANDS{/i}—\""
    "He doesn't. Somebody else catches your free wrist and puts the teapot back in it. You keep pouring, because the alternative is dropping it. Your hand's shaking. The tea goes in the cups. Mostly."
    clb_you "\"{i}Hhn{/i}— cups— cups up the line, please— {i}Hugh{/i}—\""
    hide clb_ollie
    show clb_hugh shy at vn_cast_slot
    clb_hugh "\"Thank you, manager.\""
    "He squeezes. Your hips buck. The stand cheers, because the stand thinks it's about the score."
    clb_you "\"Nnh— stop— this is— statistically— {i}Ollie, that's my{/i}— {i}stop{/i}— statistically significant—\""
    show clb_ollie loud
    clb_ollie "\"TEN POINTS A SET!\""
    hide cg onlayer cgl
    "Ollie roars it at the stands. The stands roar back. The captain plays out of his mind. Every kill, his eyes go to the bench. To you. Every single time."
    "Straight sets.\n{size=-5}{color=#ff8fa3}▸ Refill the kettle{/color}{/size}"
    $ vn_pass(120)
    jump clb_corridor

## Iris Kendal, Kingsmere's manager: the rung 3 telling, and her ribbon. She never touches you.
label clb_corridor:
    $ vn_enter(bg="clb_venue_corridor", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The corridor sink. You're filling the kettle when someone stops beside you."
    show clb_iris serene at vn_cast_slot
    "A manager. Kingsmere University's colours. A blouse with a ruffle at the throat, a skirt cut shorter and prettier than anything in your closet, heels a touch higher than practical. Long glossy hair, a red ribbon tied in it. She moves like water."
    clb_iris "\"You're the new one. Iris. Kendal. Twenty-three. I've been doing this three seasons.\""
    clb_you "\"Logistics. Kit, schedules, tea service—\""
    clb_iris "\"I know. They'll expect tea every timeout.\""
    "She looks at you. Hem. Thighs. The blouse's buttons. Your hair, wavy now, at your shoulders. Kindly, entirely."
    clb_you "\"Already policy. Point differential's up. Not conclusive, but trending.\""
    show clb_iris smile
    "Iris laughs. Soft, like the end of a compliment."
    show cg clb_ribbon onlayer cgl
    clb_iris "\"Win streaks are dangerous. {color=#ff8fb8}Outgrow the uniform, and they'll order you a prettier one.{/color}\""
    "She reaches up and unties the red ribbon from her own hair."
    clb_you "\"Laundry shrinkage is already a budget line.\""
    clb_iris "\"That's how it starts. Mine. From my first season. Tradition.\""
    "She holds the ribbon out. You take it. It's warm."
    clb_iris "\"It goes half-up. When you're ready.\""
    hide cg onlayer cgl
    hide clb_iris
    "And she's gone, heels clicking, before you can file it.\n{size=-5}{color=#ff8fa3}▸ Road duty{/color}{/size}"
    $ vn_pass(240)
    jump clb_night_bus

## The night bus home: the front seat, the roster asleep, the captain beside you. His hand on your
## cock is his first touch: "Say if—" "Continue." Consensual.
label clb_night_bus:
    $ vn_enter(bg="clb_coach_night", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The coach home. Dark. Motorway lights sliding over the ceiling. The whole roster asleep behind you, piled on each other like laundry. Ollie snoring with his mouth open."
    "The front seat. Road duty."
    show clb_rhys composed at vn_cast_slot
    "The captain sits down next to you. He's never sat in the front."
    clb_you "\"Good match.\""
    clb_rhys "\"Yeah. You were— yeah.\""
    "He looks straight ahead."
    show cg clb_thumb_knee onlayer cgl
    "His hand on your knee. Thumb. Small circles. Under the hem."
    "You don't move. You can feel your pulse in your thigh. In your ears. In your cock, which is suddenly very awake."
    "His thumb goes higher. And higher. Up the inside of your thigh, soft and smooth now all the way up, and the skirt slides back over his wrist, and he stops a hair from the edge of your panties."
    clb_rhys "\"Say if—\""
    show clb_pc soft
    clb_you "\"Continue.\""
    show cg clb_bus_hand onlayer cgl
    "His hand slides into your panties and closes round your cock."
    clb_you "\"{i}Hhn{/i}—!\""
    clb_rhys "\"Shh.\""
    clb_you "\"Sorry— sorry, Captain—\""
    clb_rhys "\"Don't be. Don't you ever be sorry for that noise.\""
    "His lips are right at your ear. He strokes you slow under the skirt. His hand's huge and warm and he's breathing like he's the one being touched. He's careful. He's so careful. Thumb over the slit, smearing the wet round, then down, then up again."
    clb_rhys "\"Is this—\""
    clb_you "\"Continue. Continue. Continue. {i}Please{/i} continue.\""
    "{i}Shlk. Shlk.{/i} Every streetlight lights up his face and his jaw's clenched and his eyes are on you, only you."
    clb_rhys "\"Steady.\""
    show clb_pc loud
    clb_you "\"I am— {i}nnh{/i}— steady— I'm very— {i}hah{/i}— very steady—\""
    "You're not. You're shaking. You're biting your own wrist. It does nothing."
    clb_you "\"Nnh— nnh— Captain— {i}Captain{/i}— I'm— road— {color=#ff8fb8}{i}ROAD DUTY{/i}{/color}—!\"" with vnfx("shake")
    "{i}Spurt.{/i} Into his palm. {i}Spurt. Spurt.{/i} Your hips jerk off the seat and your voice goes off like a car alarm."
    "Behind you, somebody stops snoring. Then starts again. Very deliberately."
    hide cg onlayer cgl
    "The captain holds you through it. Then he takes his hand out of your panties and looks at it like it's a trophy."
    "His other hand's in his lap. Holding very still over something very hard."
    show clb_pc soft
    menu:
        "Something very hard, and very still."
        "\"Reciprocal. Basic team management.\"":
            clb_you "\"Reciprocal. Basic team management.\""
            "You whisper it."
            jump clb_night_bus_sex
        "Fix your skirt":
            "You fix your skirt. He looks out of the windscreen with his ears on fire for the rest of the motorway."
            $ vn_pass(60)
            jump clb_depot

label clb_night_bus_after:
    $ vn_enter(bg="clb_coach_night", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_bus_reciprocal_end")
    "He comes under his own jacket with his head back on the seat, jaw locked, not making a sound. Hot, over your knuckles, thick, a lot of it. You make enough noise for both of you."
    "You look at your hand. You look at him. You lick your knuckles clean, one at a time, because there's nothing to wipe them on and you're not putting it on the upholstery."
    "The captain makes a sound like a man falling down a staircase."
    "Behind you, a seat creaks. Somebody's definitely awake. Somebody's definitely pretending not to be. The captain glares into the dark of the coach, and the creaking stops."
    clb_you "\"Team— managed.\""
    "You whisper it. Too loud."
    clb_rhys "\"Shh.\""
    "But he's smiling at the windscreen.\n{size=-5}{color=#ff8fa3}▸ The depot{/color}{/size}"
    $ vn_pass(60)
    jump clb_depot

## The depot: he's captain-neutral again. Iris's bow goes in your hair, and Ollie, awake, calls HIPS.
## Rung 3 lands here.
label clb_depot:
    $ vn_enter(bg="clb_depot", pc="deadpan", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg=None)
    "The depot. The middle of the night. Sodium lights. The roster stumbles off the coach in a heap."
    clb_rhys "\"Good work, everyone. Sleep. Practice is at two.\""
    "The captain hands down the bags. Captain-neutral. He doesn't look at you. His ears are on fire."
    "But when he hands down your kit bag, his thumb strokes the back of your hand. Once. Slow. Exactly the way it stroked the inside of your thigh an hour ago, and your knees nearly go."
    $ clb.fit = "u3"
    show cg clb_bow_tie onlayer cgl
    "You tie Iris's ribbon in your hair under the streetlight. It holds, just."
    show clb_ollie loud at vn_cast_slot
    clb_ollie "\"OI. {color=#ff8fb8}HIPS.{/color} I'm striking it Monday. Nobody touch the board. Called it. CALLED IT.\""
    "Ollie, half asleep, pointing at you. Pointing at your hips."
    clb_you "\"It's the bus seat.\""
    clb_ollie "\"It's the HIPS, Sweetheart.\""
    hide cg onlayer cgl
    $ clb.tier = max(clb.tier, 3)
    $ clb.rung_day = vn_clock.day
    show screen clb_clipboard(3)
    "{i}[CLB_CLIPBOARD[3]]{/i}\n{size=-5}{color=#ff8fa3}▸ Home for the night{/color}{/size}"
    hide screen clb_clipboard
    call vn_night(9)
    jump clb_morning

## ---- RUNG 4: the inspection, the photo wall ("she"), morale management (non-con, corrupting) --

label clb_inspection:
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_second_reorder")
    "The second reorder came this morning, in a box with a bow on it."
    "It can't be the laundry. You replaced the machine. You have the invoice. It's in the folder under M."
    $ clb_body(4)
    "{color=#ff5fb8}And yet: the blouse wouldn't button. Your chest is {i}real{/i} now. Round and soft and heavy, swaying when you walk, nipples pushing at the cotton.{/color}"
    show screen clb_slip("REORDER", ["Blouse, skirt, underthings.", "{color=#e0408a}{b}C{/b}{/color}, underlined. {i}(Madame Lacroix's hand.){/i}"])
    "The reorder slip, in Madame Lacroix's handwriting, says it, and underlines it."
    hide screen clb_slip
    $ clb.fit = "u4"
    hide cg onlayer cgl
    "So: the new kit. A ruffled blouse that sits open at the throat. A short cut skirt that barely covers your ass, which is a shelf now, round and high. Lace panties, in association blue, folded in tissue."
    show cg clb_closet_mirror onlayer cgl
    "{color=#ff5fb8}In the closet mirror: lashes. Fuller lips. Soft-brown hair to your shoulders, lighter than it was, with Iris's ribbon in it.{/color}"
    "{color=#ff5fb8}And them. You get both hands under them before you've decided to. They spill over your fingers, warm and heavy. You squeeze, and your nipples swell up hard between your knuckles.{/color}"
    show clb_pc flustered
    clb_you "\"{i}Ahh{/i}— oh— {i}oh{/i}, that's—\""
    "{color=#ff5fb8}Again. You push them together, and your hands know the exact squeeze, the exact angle, the slick gap right there in the middle. Nobody taught you that grip. You let go. They {i}bounce{/i}.{/color}"
    "{color=#ff5fb8}Behind you, an ass like a shelf, the short skirt riding up it. You smack it once, to check. It wobbles. Your little cock goes stiff in the lace and leaks. The new blouse rubs your nipples with every breath, and your lips are swollen and buzzing.{/color}"
    show clb_pc deadpan
    clb_you "\"Excellent tailoring.\""
    hide cg onlayer cgl
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_hall_reaction")
    "You tell the mirror. You go out to the hall with your clipboard. Ollie walks into a door. Hugh drops a ball cart. The captain looks at you once and then serves straight into the ceiling."
    hide cg onlayer cgl
    vn_sfx "{i}Click. Click. Click.{/i}"
    show clb_lacroix warm at vn_cast_slot
    "Madame Lacroix, in powder blue. Two alumnae behind her: a tall silver-haired woman, sixty-four, with eyes like a checklist; and a petite one, twenty-seven, bright-eyed, carrying a clipboard thicker than yours."
    clb_lacroix "\"Our manager. Shall we?\""
    show cg clb_deportment onlayer cgl
    "Deportment. You walk the length of the sports hall and back. \"Lovely.\" You kneel at the low table and rise without your hands. \"Lovely.\" The silver-haired one asks for a turn, and you turn, the skirt held just so between finger and thumb, the way you've seen in the photos."
    clb_other "\"Oh. Oh, {i}yes{/i}.\""
    "Says the petite one, softly. Nobody brings out a tape. Nobody writes down a figure. They just look."
    clb_lacroix "\"Regimen compliance?\""
    clb_you "\"Perfect. Not a sachet missed.\""
    show clb_lacroix pleased
    clb_lacroix "\"Perfect.\""
    hide cg onlayer cgl
    "She agrees, and writes something down that isn't a number.\n{size=-5}{color=#ff8fa3}▸ The association room{/color}{/size}"
    $ vn_pass(20)
    jump clb_photo_wall

## The rung 4 telling: the photo wall. Thirty years, two photos a year: the arrival and the banquet.
## "She" from here, with the cock still on.
label clb_photo_wall:
    $ clb.she = True
    $ vn_enter(bg="clb_association_room", pc="deadpan", pc_tag="clb_pc", cast=[("clb_lacroix", "warm")], cg=None)
    "The association room, down the corridor from the clubroom. Carpet. Good chairs. A whole wall of dark wood, and on it, in rows: photos."
    show cg clb_photo_wall onlayer cgl
    "Two a year. Thirty years of them."
    "The first of each pair: {i}the arrival.{/i} A young man with a clipboard and a box under his arm, in front of the sports hall, looking faintly put out."
    "The second of each pair: {i}the banquet.{/i} A radiant woman in a navy dress uniform, a brooch over her heart, holding the same clipboard."
    "Every year. Every single year."
    show cg clb_photo_lacroix onlayer cgl
    "You walk the wall. Your heels click. Near the start, thirty years back, a young man with a clipboard looks out at you with Madame Lacroix's eyes."
    clb_lacroix "\"Isn't it a lovely tradition.\""
    hide cg onlayer cgl
    "The petite alumna leans close to you. Doesn't touch. Just leans."
    clb_other "\"{color=#ff8fb8}How many of those are coaches now, do you think?{/color}\""
    "You look at the wall. You look at it properly. Arrival, banquet. Arrival, banquet. Arrival, banquet."
    clb_you "\"Their records are immaculate. Do you think they'd share their filing system?\""
    show clb_lacroix pleased
    "The three of them go very still. Then all three smile at once."
    clb_lacroix "\"Oh, we'd {i}love{/i} to.\""
    "On the way out, she says it to the silver-haired one, low, like you can't hear:"
    clb_lacroix "\"She'll do beautifully.\""
    clb_other "\"She will.\""
    "The silver-haired one agrees. {i}She.{/i} You file it. Probably the ruffles.\n{size=-5}{color=#ff8fa3}▸ Morale management{/color}{/size}"
    $ vn_pass(30)
    jump clb_morale

## Rung 4's dominant act: your new chest, the roster one at a time, Ollie first, the captain last.
## Non-con that corrupts: Hugh holds you, they take, and by the end you're calling "Next" yourself.
## Nothing goes in you: the chest and mouths only.
label clb_morale:
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "The association's heels fade down the corridor."
    show clb_ollie loud at vn_cast_slot
    "The clubroom door bursts open. The whole roster, at once, in a heap."
    clb_roster "\"DID SHE PASS?\""
    clb_ollie "\"She passed. SWEETHEART PASSED! She passed, gentlemen! Tradition says—\""
    "Ollie reads your face, and the room goes up like a goal."
    clb_you "\"What does tradition say.\""
    "You're already reaching for the clipboard."
    clb_ollie "\"Tradition says we celebrate when the manager passes. Morale. Management.\""
    "He points at the duty sheet. Under {b}The inspection{/b}: {i}Morale management.{/i} Same font."
    show clb_pc flustered
    clb_you "\"No. Absolutely not. The inspection is {i}over{/i}. Nothing on that sheet says— Hugh, why are you behind me—\""
    show clb_hugh shy at vn_cast_slot
    show cg clb_wrists_behind onlayer cgl
    "Hugh's behind you. Hugh's big hands close round your wrists, gently, and bring them down behind your back, and hold them there in one palm."
    clb_hugh "\"Sorry, manager. Thank you, manager.\""
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"Look at that FORM. Hold him, Hugh— her— hold {i}her{/i}, Hugh— test run for the upgraded holders!\""
    "Already dropping his shorts."
    clb_you "\"They are NOT holders— Ollie, don't you {i}dare{/i}— those buttons are association property—\""
    show cg clb_buttons onlayer cgl
    "He undoes the ruffled blouse, button by button, while you object to every one by name. They spill out. Heavy and round, pink-tipped, a C on the slip and you can feel every bit of it bouncing free in front of the whole room."
    "The whole room makes the same noise."
    show cg clb_ollie_titjob onlayer cgl
    "Ollie kneels up, spits in your cleavage, pushes your tits together round his cock with both hands. Hot, slippery, sliding up between them. {i}Shlp. Shlp.{/i}"
    clb_you "\"This is NOT— an approved— DUTY— {i}hnngh{/i}—!\""
    clb_ollie "\"Oh, look at that FORM. Ten points— ten points a SET— Sweetheart, they're so {i}soft{/i}—\""
    show clb_pc loud
    "He moans it. He fucks up into your cleavage with his head back, narrating to the ceiling, his thumbs rolling your nipples on every stroke, and your nipples stand out like rivets. \"{i}Ahh{/i}— stop— stop {i}touching{/i} the— {i}nnh{/i}—\" He comes almost at once, across your chest, up your throat, a splash on your chin. The room cheers."
    clb_ollie "\"NEXT!\""
    clb_you "\"There is NO next— {i}mmph{/i}—\""
    show cg clb_hugh_chest onlayer cgl
    "Hugh trades your wrists to somebody else and comes round the front. Shy, huge, red to the ears. He's so big he pokes out the top of your cleavage, every stroke, right under your chin, and somebody tips your head down onto it, and you lick the tip because it's in your mouth."
    clb_hugh "\"Thank you, manager. {i}Thank you{/i}— thank you, manager—\""
    show cg clb_morale_line onlayer cgl
    "Then the setter. Then the libero, who holds your tits together in his own hands and fucks them like he's in a hurry. Then the outside hitter, and nobody has to tip your head down this time. {i}Shlp. Shlp. Glk.{/i}"
    "\"Next,\" says somebody. \"Next,\" says somebody else. And then—"
    show cg clb_next_yourself onlayer cgl
    clb_you "\"{i}Next{/i}.\""
    "It's your voice. Your mouth. Nobody's holding your wrists any more, and you didn't notice when they stopped, because your hands are full of your own chest, pushing it together for the next man."
    clb_you "\"Next. {i}Next.{/i}\""
    "You say it again, hoarse, and they cheer like it's a match point. Every one of them on your chest. Splashes on your collarbone, your chin, warm ropes sliding down between your breasts into the ruffles. Your nipples are bright pink and so hard they tingle. Your cock is leaking a wet patch through the association's lace, and nobody's even touched it."
    clb_you "\"Nnh— {i}mmh{/i}— morale is— very high— very— {i}very{/i}— high—\""
    "You pant it, tits slick and bouncing in your own hands, and you can't remember the last thing you objected to."
    hide cg onlayer cgl
    clb_ollie "\"Round two!\""
    menu:
        "Already hard again, and Hugh's hands find your wrists."
        "\"There is NO round two—\"":
            jump clb_morale_sex
        "\"Captain. You're last.\"":
            jump clb_rhys_last

label clb_inspection_after:
    $ vn_enter(bg="clb_clubroom", pc="loud", pc_tag="clb_pc", cast=[("clb_ollie", "loud")], cg="clb_round_two_end")
    "One at a time, they finish on you. Every one of them. You're a mess of it, sliding down into the ruffles. Ollie narrates every one. Hugh says thank you before, during and after."
    clb_you "\"{i}Ahh{/i}— upgraded— {i}upgraded holders{/i}— performing— above— {i}specification{/i}—!\""
    "You announce it, at a volume, and the roster gives you a standing ovation with its shorts round its ankles."
    "You stopped saying no somewhere in the middle of round two. You know exactly where. You'll file it."
    clb_you "\"Next. {color=#ff8fb8}Please form an orderly line.{/color}\""
    "You rasp it. And then, louder, to the whole room, in your best clipboard voice. They cheer. Nobody's left in the line. Nobody but the captain.\n{size=-5}{color=#ff8fa3}▸ \"Captain. You're last.\"{/color}{/size}"
    jump clb_rhys_last

## The captain last: "This should not be legal." He asks; "Continue." Rung 4 lands; Ollie strikes CHEST.
label clb_rhys_last:
    $ clb.tier = max(clb.tier, 4)
    $ clb.rung_day = vn_clock.day
    $ vn_enter(bg="clb_clubroom", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg=None)
    "The room clears. It always clears for him."
    "The captain kneels in front of you, close, and just looks. At your chest, slick and heavy. At your face. At the ribbon in your hair."
    clb_rhys "\"{color=#ff8fb8}This should not be legal.{/color}\""
    clb_you "\"It's on the sheet, Captain.\""
    clb_rhys "\"I know it's on the sheet. I know. That's not— you can say no to me. Me, you can always say no to.\""
    "His voice cracks. You look at him for a long moment, with the whole roster's mess sliding down your chest."
    clb_you "\"Continue.\""
    show cg clb_rhys_chest onlayer cgl
    "He stands. You take him in your hands first, then between your tits, and squeeze. He's thick and hot and so hard he's shaking."
    "He's slow. He's always slow. He fucks your cleavage like it's something he's been thinking about for weeks, one hand on your cheek, thumb at the corner of your mouth. You tip your head and take the head of him in your mouth every stroke."
    clb_rhys "\"You're so soft. You're so— everything about you's gone so {i}soft{/i}—\""
    clb_you "\"Regimen.\""
    "You mumble it round him. He laughs, helplessly, and it turns into a groan halfway."
    show clb_pc loud
    clb_you "\"Mmh— {i}mmmh{/i}— Captain— {i}Captain{/i}— ahh— your— {i}ahh{/i}— morale—\""
    "Louder for him. Always louder for him."
    clb_rhys "\"Steady.\""
    "He breathes it, and comes, right there, across your tits and up your throat, holding still, saying nothing, saying everything with his face." with vnfx("shake")
    hide cg onlayer cgl
    show clb_pc soft
    "Then he does your blouse up for you. Every button. And kisses your forehead."
    vn_sfx "{i}SKRRK.{/i}"
    hide clb_rhys
    show clb_ollie grin at vn_cast_slot
    clb_ollie "\"{color=#ff8fb8}CHEST!{/color} That's the set! That's the whole BOARD!\""
    show screen clb_board
    "From the corridor. Ollie, at the closet door."
    hide screen clb_board
    show clb_pc deadpan
    clb_you "\"Protein.\""
    "You call it back."
    show screen clb_clipboard(4)
    "{i}[CLB_CLIPBOARD[4]]{/i}\n{size=-5}{color=#ff8fa3}▸ Home for the night{/color}{/size}"
    hide screen clb_clipboard
    call vn_night(7)
    jump clb_morning

## ---- RUNG 5: the slump; "I'm done going last."; his mouth; your bed (MANDATORY); consensual ---

label clb_slump:
    $ vn_enter(bg="clb_domus_room", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "That morning, in the mirror:"
    $ clb_body(5)
    $ clb.fit = "u4"
    show cg clb_mirror_heavy onlayer cgl
    "{color=#ff5fb8}Heavy and high. Your tits sit up on their own and sway when you breathe. Your hips have gone past the skirt's patience. Your hair's long enough to put half-up, so you do, in Iris's ribbon, exactly how she said.{/color}"
    "{color=#ff5fb8}You lift them. Both hands, and they still spill out over your fingers. Heavier than the C ever was. A D, the new slip says. You squeeze, and your knees buckle, and you catch yourself on the sink.{/color}"
    show clb_pc flustered
    clb_you "\"{i}Hahh{/i}— {i}mmh{/i}— heavy— they're so {i}heavy{/i}—\""
    "{color=#ff5fb8}Your thighs rub, soft and slick, all the way to your knees. Your ass sits out behind you, round and full. You rock against the edge of the sink, slow, and your hips find a rhythm on their own. Back. Down. Roll. Nobody ever taught you that.{/color}"
    "{color=#ff5fb8}Under the lace: a little soft thing. Barely a thumb. You pinch it between finger and thumb. It twitches, and drools, and that's all it does now. You don't think about it. You haven't thought about it in weeks.{/color}"
    show clb_pc deadpan
    clb_you "\"Efficient.\""
    hide cg onlayer cgl
    $ vn_enter(bg="clb_sports_hall", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_losing")
    "You tell the mirror, in a light, breathy voice. Then the league."
    "They lose."
    "They lose again."
    "They lose a third time, at home, in front of their own stand, and the sports hall goes quiet in a way you've never heard. Ollie stops narrating. Hugh sits with his head in a towel. The captain's serve goes long, and long, and into the net."
    hide cg onlayer cgl
    "So you fix it. The only way you know how."
    show cg clb_field_hospital onlayer cgl
    "Person by person. Tea, the right way, for each of them. Hugh's knee, re-taped. Ollie's terrible joke, laughed at, properly. Fresh towels, warm. A word for everybody. A hand on every shoulder. You go down the bench like a field hospital."
    "It takes all evening. By the end they're all smiling again, a little."
    hide cg onlayer cgl
    "They go to shower. The lights click off at the far end."
    "The captain stays.\n{size=-5}{color=#ff8fa3}▸ Stay behind{/color}{/size}"
    $ vn_pass(30)
    jump clb_slump_rhys

label clb_slump_rhys:
    $ clb.slump = True
    $ vn_enter(bg="clb_sports_hall_night", pc="deadpan", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg=None)
    "The empty sports hall. Just the two of you and the hum of the lights."
    clb_rhys "\"[clb_pc_name].\""
    "You stop. Your name. Nobody's said your name since the box."
    clb_rhys "\"You do all of it. The tea. The towels. The— the {i}second course{/i}, every one of them, and you log it, and you thank {i}them{/i}, and you don't even— you don't even {i}know{/i}—\""
    "He isn't composed. His hands are shaking."
    clb_you "\"Know what?\""
    clb_rhys "\"I'm done. {color=#ff8fb8}I'm done going last.{/color}\""
    show cg clb_first_kiss onlayer cgl
    show clb_pc flustered
    "He kisses you."
    "Hard, then soft, then hard again, both hands in your hair, Iris's ribbon slipping. You make a noise into his mouth you've never made. Your knees go."
    "He catches you. Backs you into the net post. His thigh between yours, pushing up under your skirt, and your little cock rubs against it through the lace and you whimper into his mouth. His hands are on your tits, finally, both of them, squeezing, thumbs rolling your nipples through the blouse like he's been thinking about exactly this since the inspection."
    clb_rhys "\"Every time. Every time, I went last, and I had to {i}watch{/i}—\""
    clb_you "\"Rhys.\""
    "First time. It tastes good."
    clb_rhys "\"Say that again.\""
    clb_you "\"Rhys.\""
    hide cg onlayer cgl
    show cg clb_rhys_knees onlayer cgl
    "He drops to his knees on the sports hall floor. Pushes your skirt up. Hooks the lace panties down to your thighs."
    "Your little cock. Barely a thumb. Soft, pink, twitching."
    "He doesn't laugh. He looks at it like it's the trophy. Then he looks up at you."
    menu:
        clb_rhys "\"Can I.\""
        "Hands in his hair":
            $ clb.hands = "hair"
        "Hands on the net post behind you":
            $ clb.hands = "post"
    jump clb_slump_suck

label clb_slump_suck_after:
    $ vn_enter(bg="clb_sports_hall_night", pc="loud", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_suck_end")
    "He doesn't let you off. Slow, slow, his tongue under the head, until it's too much, and you come in his mouth with a noise that bounces off the far wall."
    clb_you "\"{i}Ahh{/i}— Rhys— {i}RHYS{/i}— that's— that's a— {i}completely{/i} different— {i}ahh{/i}—!\""
    "He swallows. Wipes his mouth. Licks you clean anyway, slow, the little soft thing twitching on his tongue, until you push his head away, giggling and gasping."
    clb_you "\"{i}Sensitive{/i}— Rhys, I'm— that's very— {i}sensitive{/i}—\""
    hide cg onlayer cgl
    "He stays on his knees, looking up at you, ears scarlet, smiling like an idiot."
    menu:
        clb_rhys "\"Walk you home?\""
        "\"Yes.\"":
            pass
    $ vn_pass(40)
    jump clb_your_bed

## Your bed: "Recovery work." He laughs for the first time all season. The only way on is into the
## mandatory scene.
label clb_your_bed:
    $ vn_enter(bg="clb_domus_room_night", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg=None)
    "He walks you home, down the hill to Domus Street and up the narrow stairs to your room at the top of the house, carrying your kit bag."
    "He has to duck under the door frame."
    "He takes his tracksuit jacket off and folds it, neatly, on your chair. Captain to the last."
    clb_you "\"Recovery work.\""
    "You tell him, very seriously, and sit on the bed."
    show clb_rhys red
    "Rhys laughs. Out loud. Head back. The first time you've heard him laugh all season. It's a great laugh."
    "Then he's on you."
    $ clb.fit = "nude"
    show cg clb_unbutton onlayer cgl
    "He undresses you like he's unpacking something fragile. The ribbon tie. Every button of the ruffled blouse, one at a time, kissing the skin under each. Your tits spill out into his hands and he just holds them for a second, heavy and warm, and closes his eyes."
    clb_rhys "\"I've wanted to do that since the inspection. Since {i}before{/i} the inspection.\""
    show cg clb_face_down onlayer cgl
    "Your blouse open. His mouth on your tits, sucking a nipple hard enough to make you arch. Your skirt rucked up to your waist. The lace panties gone somewhere. You end up face down, on your knees and elbows, ass up, cheek on your own pillow, and his hands spread you open."
    "Your little cock hangs between your thighs, ignored, dripping on the sheet. Nobody touches it. Nobody needs to."
    "He kisses the backs of your thighs. The curve of your ass. Then his tongue, right there, hot and flat, and you nearly come off the bed."
    show clb_pc flustered
    clb_you "\"{i}Rhys{/i}— what are you— that's— {i}that's not hygienic{/i}—\""
    clb_rhys "\"Shower. Before. I'm thorough.\""
    "He says it into you. And licks again, slow, circling, pushing in."
    show clb_pc loud
    clb_you "\"{i}Ahhh{/i}— {i}ahh{/i}— oh {i}god{/i}— oh that's— that's very— {i}thorough{/i}—!\""
    "You grab fistfuls of pillow and push back on his face, and you don't even decide to. Your voice goes up and up and somebody next door turns their telly up."
    "Nothing's ever been in there. Spit. His thumb. Slow circles. Then one finger. {i}Shlk.{/i} Then two, and he curls them, and—"
    clb_you "\"{i}Hnnngh{/i}—!\""
    clb_rhys "\"Steady.\""
    "Low, and it isn't captain's voice at all. Fingers out. You whine. Then the fat hot head of his cock, pressing right there. Waiting."
    clb_rhys "\"Say if—\""
    clb_you "\"{i}Continue.{/i}\"\n{size=-5}{color=#ff8fa3}▸ Knees and elbows. Push back.{/color}{/size}"
    hide cg onlayer cgl
    jump clb_slump_sex

label clb_slump_after:
    $ clb.tier = max(clb.tier, 5)
    $ clb.slump = False
    $ vn_enter(bg="clb_domus_room_night", pc="loud", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_slump_end")
    "He comes buried to the root, holding you back onto him by the hips, his forehead on your spine. Every pulse, hot, deep."
    "And you came. Untouched. Nothing on your little cock but the sheet, and it went off anyway, from deep inside where he was pressing."
    clb_you "\"{i}Ahh{/i}— {i}AHH{/i}— {color=#ff8fb8}— RHYS —{/color}!\"" with vnfx("shake")
    "Somebody next door bangs on the wall. Neither of you cares."
    "You lie there with his weight on your back and his cock still in you, shaking. He kisses the back of your neck. Your shoulder. Your ear."
    "Then he moves again. Just a little. Just to see."
    clb_you "\"{i}Hah{/i}— Rhys— I'm— it's too— I just—\""
    clb_rhys "\"Say if.\""
    clb_you "\"...{i}Continue.{/i}\""
    show cg clb_slump_again onlayer cgl
    "Slow. Deep. His hand flat on the small of your back holding you down on the bed. He fucks you through the aftershocks until you're babbling into the pillow and your little cock dribbles again onto the sheet without ever getting hard, and he comes a second time with his teeth in your shoulder."
    clb_you "\"{color=#ff8fb8}— RHYS —{/color}\""
    "You wail it, again, because apparently it's the only word you have left."
    clb_rhys "\"I've got you.\""
    hide cg onlayer cgl
    "{color=#ff5fb8}You sit up, later, and your ass {i}throbs{/i}, deep, and your mouth floods.{/color}"
    clb_you "\"{i}Ohh{/i}— recovery. Logged. LOGGED.\""
    call vn_night(7)
    jump clb_slump_morning

label clb_slump_morning:
    $ vn_enter(bg="clb_domus_room", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_wake_together")
    "You wake up with his arm over you and his face in your hair."
    "Your ass hums. Deep, full, warm. Every time you shift, your belly goes stupid and you grin into the pillow."
    "He's already awake. He's been watching you sleep, which is inefficient of him."
    clb_rhys "\"Morning, [clb_pc_name].\""
    clb_you "\"Pulled something.\""
    "You tell him, and he laughs again. Twice in a row. A record."
    "Then his hand, on your hip. His cock, hard again, pressed against the back of your thigh."
    clb_rhys "\"Again? Slow. If it's too much—\""
    "Into your neck."
    clb_you "\"Too much is a scheduling issue. Continue.\""
    show cg clb_spoon onlayer cgl
    "On your sides, spooned, his arm under your head. He pushes in slow. So slow. You're still slick and open from the night, and he slides in like he belongs there, all the way, until his hips are flush with your ass and you can feel him breathing against your back."
    clb_you "\"{i}Hhhah{/i}—\""
    clb_rhys "\"I've got you.\""
    "He barely moves. Little rolls of his hips, deep, deep, like the tide. His hand comes round and plays with your tits, lazy, heavy in his palm. Your little cock bobs against the sheet with every roll."
    show clb_pc loud
    clb_you "\"Rhys— {i}Rhys{/i}— that's— {i}mmh{/i}— morning conditioning— that's— {i}ahh{/i}— {i}AHH{/i}—!\"" with vnfx("shake")
    "You come first, untouched again, shaking in his arm. He follows you with a groan into your hair, deep inside, and holds you there until your breathing slows."
    hide cg onlayer cgl
    $ clb.fit = "u4"
    show clb_pc soft
    "He makes the tea with your kettle. He gets it wrong. You drink it anyway.\n{size=-5}{color=#ff8fa3}▸ The semifinal{/color}{/size}"
    $ vn_pass(120)
    jump clb_semifinal

## The board comes down; the second course comes off the sheet in the captain's pen; and the rung 5
## telling: Iris, at the semifinal, out loud.
label clb_semifinal:
    $ vn_enter(bg="clb_clubroom", pc="deadpan", pc_tag="clb_pc", cast=[("clb_ollie", "grin")], cg="clb_board_down")
    "At the clubroom, before the coach leaves, Ollie takes the board down."
    "He just does it. Peels the tape off the closet door, folds the whole thing up, and tucks it in his kit bag. Then he tapes up a fresh sheet in its place and folds its heading over so you can't read it."
    clb_ollie "\"Don't look. It's a new pool. Long odds.\""
    hide cg onlayer cgl
    show clb_rhys composed at vn_cast_slot
    show cg clb_line_through onlayer cgl
    "Rhys takes the duty sheet down off its pin. Draws one neat line through {i}Second course: hydration support, by rotation.{/i} Pins it back up."
    "Nobody says anything. Hugh pats Rhys on the shoulder, very solemnly. Ollie grins like he's won the pool."
    hide cg onlayer cgl
    $ vn_enter(bg="clb_semifinal_court", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_semifinal")
    "Then the semifinal. And they're {i}back{/i}. Every block lands. Every serve. Rhys plays like he's got something to prove to exactly one person, and every point he wins, he looks at the bench."
    $ vn_enter(bg="clb_venue_corridor", pc="deadpan", pc_tag="clb_pc", cast=[("clb_iris", "serene")], cg=None)
    "In the corridor after, by the sink, Iris Kendal."
    "She looks at you. At the bow, half-up. At how you're standing, a bit carefully. At the mark on your neck under your collar."
    clb_iris "\"{color=#ff8fb8}Have you noticed?{/color}\""
    "Out loud. Plain as anything. You hear yourself answer."
    clb_you "\"The third reorder's pending. The supplier's slow, so I've moved the fitting to after nationals, which isn't ideal, but the alternative was a split delivery, and with the coach booking—\""
    "You're giving her a logistics report. You can hear yourself giving her a logistics report."
    show clb_iris smile
    "Iris listens to the whole thing. Every word. Then she smiles."
    clb_iris "\"That's what I said too.\""
    $ clb.rung_day = vn_clock.day
    show screen clb_clipboard(5)
    "{i}[CLB_CLIPBOARD[5]]{/i}\n{size=-5}{color=#ff8fa3}▸ Back to the clubroom{/color}{/size}"
    hide screen clb_clipboard
    $ vn_pass(120)
    jump clb_hub

## ---- RUNG 6: nationals, the dogpile (the cock goes), the banquet, the balcony ---------------

label clb_nationals:
    $ vn_enter(bg="clb_arena", pc="deadpan", pc_tag="clb_pc", cast=[], cg="clb_arena_bench")
    "The arena. Banners from every decade in the rafters. A whole stand in the club's colours. A court so bright it dazzles."
    "You kneel at the end of the bench with the tea service, the skirt pooled round your knees, your tits straining the ruffled blouse. Every eye in the building finds you once and comes back twice."
    "It goes the distance. Every set. Point for point."
    "Every timeout, you pour. Every timeout, they come off court and take the cups from your hands like communion. Ollie can barely speak. Hugh says \"thank you, manager\" and means everything."
    hide cg onlayer cgl
    show clb_rhys red at vn_cast_slot
    "Before the deciding set, Rhys kneels in front of you for his cup, in front of the whole arena."
    clb_you "\"You've been looking at the stand. Their libero's weak on the left. Their back row—\""
    clb_rhys "\"I haven't been looking at the stand. {color=#ff8fb8}I only ever look at you.{/color}\""
    "His ears go red, in front of everybody."
    show clb_coach flat at vn_cast_slot
    "By the bench, a journalist asks the coach what's different this season. The coach looks at the reporter. Then at you. And speaks for the second time all year."
    clb_coach "\"{color=#ff8fb8}A cherished manager is worth ten points a set.{/color}\""
    "The journalist writes it down. Underlines it."
    show cg clb_match_point onlayer cgl
    "Match point. The setter puts it up. Rhys goes up for it like he's going to the moon."
    vn_sfx "{i}THWACK.{/i}" with vnfx("flash")
    hide cg onlayer cgl
    "{size=-5}{color=#ff8fa3}▸ Onto the court{/color}{/size}"
    jump clb_dogpile

## The cock goes at the bottom of the nationals dogpile; then rung 6's body, everything at once.
## Something gives, low down, and you file it under team-spirit overload.
label clb_dogpile:
    $ vn_enter(bg="clb_arena", pc="loud", pc_tag="clb_pc", cast=[], cg="clb_tossed")
    "The arena {i}explodes.{/i}"
    "The roster comes off the court and grabs you off the bench. You're up. You're flying. Tossed hand to hand, Hugh to Ollie to a setter to a libero, your skirt up round your waist, your tits bouncing, everybody screaming your name. Well. {i}Sweetheart.{/i}"
    show cg clb_dogpile onlayer cgl
    "Then they all go down at centre court. The whole roster. And you're at the bottom of it."
    "Crushed. Hot. Laughing. A knee here, an elbow there, Ollie screaming \"TEN POINTS A SET\" directly into your ear, Hugh bellowing with joy somewhere above you, everybody's weight pressing down on you at once, on your chest, your hips, between your legs—"
    "—and something {i}gives.{/i}"
    "{color=#ff5fb8}Low down. Under the lace. The little thing that was barely a thumb goes warm, and soft, and pulls in. Smaller. Smaller. Sinking into you.{/color}"
    clb_you "\"{i}Hnn{/i}— wait— inventory— {i}INVENTORY DISCREPANCY{/i}—!\""
    $ clb_body(6)
    "{color=#ff5fb8}And {i}opens.{/i}{/color}"
    "{color=#ff5fb8}Two soft lips, swelling apart. Slick. Hot. Wet already, soaking the lace, slick running down your thighs. A little nub at the top that throbs every time somebody shifts on top of you, and somebody always is—{/color}"
    clb_you "\"{i}HYAAN—!{/i}\"" with vnfx("shake")
    "{color=#ff5fb8}And it doesn't stop there. Everything goes at once. Your tits {i}swell{/i}. Past the D. Past anything on the reorder form. {i}Tik.{/i} A button pings off the ruffled blouse. {i}Tik. Tik.{/i} Two more. They surge out of it, huge and heavy and hot, a J at least, and somebody's hand lands on one, and you {i}squeal{/i}.{/color}"
    clb_you "\"{i}AHN{/i}— my— my {i}CHEST{/i}— they're still— {i}hhaaah{/i}—!\""
    "{color=#ff5fb8}You get a hand free and grab one. It overflows your whole hand. Your fingers sink in. The nipple's fat and stiff against your palm, and when you squeeze, it jolts straight down into the new wet place, and that clenches, and drools, and you squeeze again because you can't not.{/color}"
    clb_you "\"{i}Hyaan{/i}— {i}mmh{/i}— {i}MORALE{/i}—!\""
    "{color=#ff5fb8}Your hips spread under the weight of all of them. Your ass rounds out against the court. Your thighs thicken, slick and soft, clamping on somebody's knee. Your face finishes itself, cheekbones, lips, lashes. Your hair pours loose out of Iris's ribbon, long and honey-gold, all over the floor.{/color}"
    "{color=#ff5fb8}And your voice, when it comes out, is a woman's. Every part of you is lit up at once: lips, tits, ass, and the slick new heat between your thighs.{/color}"
    clb_you "\"{i}AHN{/i}— everything— all of it— {i}full marks{/i}—! ...Team-spirit overload.\""
    hide cg onlayer cgl
    "You gasp it, to somebody's armpit."
    show clb_rhys red at vn_cast_slot
    show cg clb_dug_out onlayer cgl
    "Then hands. Digging. Rhys, hauling people off you one by one by the back of their shirts, until he finds you at the bottom, and pulls you up into his arms."
    "He looks at you. All of you. He doesn't say anything."
    "He kisses you, in the middle of the court, in front of the whole arena, and the arena loses its mind.\n{size=-5}{color=#ff8fa3}▸ The banquet{/color}{/size}"
    hide cg onlayer cgl
    $ vn_until(19)
    $ vn_pass(60)
    jump clb_banquet

## The banquet: the dress uniform; the association in navy, every one with the brooch; the welcome
## ceremony is yours. "Our newest sister." The arithmetic arrives in one line: "Oh. Thirty years."
label clb_banquet:
    $ clb.fit = "dress"
    $ vn_enter(bg="clb_ballroom", pc="deadpan", pc_tag="clb_pc", cast=[], cg=None)
    "A hotel ballroom. Chandeliers. Round tables. The roster in borrowed suits, Ollie's tie already round his head."
    "You're in the dress uniform. Navy. A fitted jacket that holds your tits up like an offering, a skirt that hugs your hips and your ass and stops at the knee. The association sent it this afternoon. It fits. It fits like it was made for exactly this body, which you didn't have this morning."
    show cg clb_association onlayer cgl
    "And the association is {i}here.{/i} All of it. Women in navy blazers at every table, every age, every one of them with the same brooch over her heart. They turn and smile at you as you come in. All of them. Iris among them, in navy too, the brooch on her blazer."
    hide cg onlayer cgl
    show clb_lacroix warm at vn_cast_slot
    "Madame Lacroix taps the microphone."
    clb_lacroix "\"Tonight is more than a celebration. Tonight is a welcome. Will the manager come up?\""
    "She looks straight at you. You go up. Your heels click. Your new hips sway, and you can feel them sway, heavy, every step. Your tits bounce in the fitted jacket. Your thighs brush, soft and slick, and between them, under the lace, the new place throbs every time they do. It clenches, and lets go, and clenches, slow, like it already knows what it's for. You've never been taught that. The whole room watches."
    show cg clb_brooch onlayer cgl
    "She takes a small box from her handbag. The brooch. She pins it over your heart with fingers that don't shake at all, and kisses your cheek. Once."
    "Then, into the microphone:"
    clb_lacroix "\"Ladies. {color=#ff8fb8}Our newest sister.{/color}\""
    $ clb.tier = max(clb.tier, 6)
    hide cg onlayer cgl
    "The association stands. Every woman in the room in navy, clapping. Thirty years of them."
    "You look at them. At their brooches. At the photo wall in your head: arrival, banquet, arrival, banquet. A young man with a clipboard. A radiant woman with the same clipboard."
    "You look down at your own brooch. At your chest. At your hands."
    show clb_pc soft
    clb_you "\"{color=#ff8fb8}Oh. Thirty years.{/color}\""
    show clb_iris serene at vn_cast_slot
    "Iris is beside you, somehow. She squeezes nothing, touches nothing. She just leans in."
    clb_iris "\"It goes better if you don't overthink it.\""
    show cg clb_frame_filled onlayer cgl
    "By the stage there's an easel, and on it, the empty frame from the end of the photo wall. A flash. It's got its photo now."
    hide cg onlayer cgl
    show clb_lacroix pleased at vn_cast_slot
    menu:
        "Madame Lacroix holds the microphone out to you."
        "\"Thank you. I'll need your filing system.\"":
            $ clb.speech = "filing"
            clb_lacroix "\"Of course, darling.\""
            "Into the microphone, and the whole association applauds your filing."
        "\"Please form an orderly line. For the buffet.\"":
            $ clb.speech = "line"
            "The room laughs so hard the chandeliers shake. Ollie actually forms a line for the buffet. Half the association joins it."
        "\"I'd like to thank the laundry.\"":
            $ clb.speech = "laundry"
            "There's a pause. Then Madame Lacroix laughs, really laughs, and the association with her, and Iris hides her face in her napkin."
    $ vn_pass(60)
    jump clb_balcony

## The balcony: "I'm in love with you." / "I thought we were already dating." His hand finds what the
## dogpile left: "Oh." "Logged." The first vaginal, against the rail. The association never watches.
label clb_balcony:
    $ clb.fit = "jacket"
    $ vn_enter(bg="clb_balcony", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg=None)
    "Later, the balcony. Cold air. The town lit up below. The party behind the glass, muffled, warm, gold."
    show cg clb_jacket_shoulders onlayer cgl
    "Rhys comes out after you and puts his tracksuit jacket round your shoulders. It swamps you. It smells like him."
    "He stands there. Ears red. Hands in his pockets, then out of them."
    clb_rhys "\"{color=#ff8fb8}I'm in love with you.{/color}\""
    "You blink at him."
    clb_you "\"I thought we were already dating. Since the slump. There's an overnight guest column.\""
    hide cg onlayer cgl
    "He stares at you. Then he puts his forehead on yours and laughs, helplessly, for a long time."
    show cg clb_balcony_hand onlayer cgl
    "Then his hand slides under the dress skirt. Up your thigh. Up. And finds what the dogpile left there. Soft. Bare. Wet already."
    clb_rhys "\"{color=#ff8fb8}Oh.{/color}\""
    clb_you "\"{color=#ff8fb8}Logged.{/color}\""
    "His fingers slip between your new lips. {i}Shlk.{/i} Easy. Wet. Somewhere nothing's ever been."
    show clb_pc flustered
    clb_you "\"Rhys— {i}Rhys{/i}— oh {i}god{/i}, that's— that's a— {i}completely{/i}—\""
    "Two fingers. Slow. Curling. His thumb finds the little nub at the top and circles it, and your whole body goes off like a flare."
    show clb_pc loud
    clb_you "\"{i}Ahh{/i}— {i}AHH{/i}— what is— what {i}is{/i} that— oh my {i}god{/i}—\""
    clb_rhys "\"It's yours. It's all yours.\""
    "Into your ear, a bit wondering. You come on his fingers. Just from that. Standing on a balcony in a dress uniform, with the party behind the glass, clutching his shirt and wailing into his collar." with vnfx("shake")
    show cg clb_rail onlayer cgl
    "He lifts you by the ass onto the cold stone rail. Your legs go round his waist. His belt. His cock, hot and heavy against your belly. Then lower. The fat head nudging your new lips apart."
    clb_rhys "\"Say if—\""
    clb_you "\"{i}Continue.{/i}\"\n{size=-5}{color=#ff8fa3}▸ Against the rail{/color}{/size}"
    hide cg onlayer cgl
    jump clb_balcony_sex

label clb_balcony_after:
    $ vn_enter(bg="clb_balcony", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "red")], cg="clb_balcony_end")
    "Behind the glass, the music stops for a second. Then somebody turns the band up. Way up."
    clb_you "\"They heard.\""
    "You whisper it."
    clb_rhys "\"Everyone heard.\""
    "He kisses you. He doesn't pull out. He stays right there, inside you, holding you on the rail with your legs round him and his jacket round your shoulders, and you feel him twitch, and you clench round him on purpose just to hear him gasp."
    clb_you "\"Again.\""
    clb_rhys "\"Give me a minute.\""
    clb_you "\"I've scheduled a minute.\""
    "He laughs into your neck, and you can feel it everywhere.\n{size=-5}{color=#ff8fa3}▸ The clipboard{/color}{/size}"
    $ vn_pass(30)
    jump clb_end

## ---- THE ENDING, "Club Banquet": the clipboard's last line; the stay-or-go epilogue ----------

label clb_end:
    $ clb.ending = "banquet"
    $ clb.done = True
    $ achievement.grant("Association Member")
    $ clb.fit = "jacket"
    $ vn_enter(bg="clb_ballroom_late", pc="soft", pc_tag="clb_pc", cast=[], cg="clb_stage_edge")
    "Late. Rhys asleep in a chair in the corner of the ballroom with his tie undone. Ollie asleep under a table. The association gone home in twos and threes, every one of them kissing the air by your cheek on the way out."
    "You sit on the edge of the stage with your shoes off and the clipboard on your knee. Rhys's jacket round your shoulders. Your thighs still sticky under the navy skirt. The brooch over your heart."
    "Your body, all of it, soft and heavy and golden in the chandelier light. You look down at it for a while. Your tits, filling the dress jacket. Your hips. The lace, and nothing under it but what the dogpile left."
    clb_you "\"Huh.\""
    "Quietly, to nobody."
    show screen clb_clipboard(1)
    "The first page: a paragraph. Process. Precedent. Headings."
    hide screen clb_clipboard
    show screen clb_board
    "Ollie's new sheet is in your handbag. He gave it to you at the buffet, heading still folded over, and ran away. You unfold it."
    "A column of names under it. Long odds."
    hide screen clb_board
    "You fold it back."
    "You turn the pages. Every entry's shorter than the last. A line. Half a line. {i}No further notes.{/i}"
    "You click the pen. You write the last entry of the season."
    show screen clb_clipboard(6)
    "{color=#ff8fb8}{i}happy{/i}{/color}"
    "Then you sit and look at it for a long time."
    hide screen clb_clipboard
    hide cg onlayer cgl
    menu:
        "{color=#e8c35a}Nobody hid a thing. Every step was handed to you in daylight, by somebody smiling.{/color}"
        "Next season" (ending=True):
            jump clb_epilogue_stay
        "Hand in the file" (ending=True):
            jump clb_epilogue_go

## Stay: next season. A new notice, a nervous first-year (nineteen), the box, and the S folder with
## every leaflet still unread. "Mostly paperwork."
label clb_epilogue_stay:
    $ clb.epilogue = "stay"
    $ clb.fit = "dress"
    $ vn_enter(bg="clb_corridor", pc="soft", pc_tag="clb_pc", cast=[], cg=None)
    "Spring. A new notice on the board in the main corridor, under the fire extinguisher. Your font."
    show screen clb_slip("MEN'S VOLLEYBALL CLUB NEEDS A MANAGER.", ["No experience needed."])
    "A first-year reads it twice. Nineteen, all elbows, a CV under his arm that you can tell from here is a list of hobbies."
    hide screen clb_slip
    show cg clb_next_manager onlayer cgl
    "He turns to you, because you're standing next to it in a navy skirt with a brooch on."
    clb_other "\"What does the manager actually do?\""
    "You hand him the box. Tied with ribbon. The S folder's in the bottom of it, fat as a brick, every leaflet in it pristine."
    clb_you "\"Mostly paperwork.\""
    "And you smile at him exactly the way Iris smiled at you."
    hide cg onlayer cgl
    $ vn_enter(bg="clb_domus_room_night", pc="soft", pc_tag="clb_pc", cast=[], cg="clb_two_toothbrushes")
    "That night, home: the room at the top of the narrow house on Domus Street. Your clipboard on the desk. Rhys's toothbrush in the cup by the sink, next to yours, like it's always been there."
    "{color=#e8c35a}The clubroom's still yours: tea, towels, practice, and the captain to walk you home.{/color}\n{size=-5}{color=#ff8fa3}▸ Home{/color}{/size}"
    jump clb_route_return

## Go: hand in the file. The best handover the club has had in thirty years; you keep the uniform,
## the ribbon and the body; Rhys carries the box home.
label clb_epilogue_go:
    $ clb.epilogue = "go"
    $ clb.fit = "dress"
    $ vn_enter(bg="clb_association_room", pc="soft", pc_tag="clb_pc", cast=[("clb_lacroix", "pleased")], cg="clb_handover")
    "You write the handover. It runs to several pages, with tabs."
    "It's the best document the club has had in thirty years. Madame Lacroix says so. Then she reads it again and says so again."
    "You keep the uniform. You keep Iris's ribbon. You keep the body, which wasn't on the inventory, and which nobody asks for back."
    "The clipboard's last page you write out in full sentences, for once. It is a very good record of a season. It is a truly terrible record of a year."
    $ vn_enter(bg="clb_hill_night", pc="soft", pc_tag="clb_pc", cast=[("clb_rhys", "composed")], cg="clb_box_home")
    "Rhys carries the box home. He doesn't ask whose home. He just walks next to you, with your hand in his free one, all the way.\n{size=-5}{color=#ff8fa3}▸ Home{/color}{/size}"
    jump clb_route_return
