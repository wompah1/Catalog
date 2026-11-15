## THE STORY, shared: rung 1 (Turn Me Up), the same on both paths up to the vote (2026-11-12;
## PLAN.md). After the vote the paths never cross: teal.rpy and red.rpy. Second person, as every
## catalog VN. The narration never draws the comparison: the reader sees the match because the
## details repeat.

label vt_one_kiosk:
    $ vt_init()
    $ vt.fit = "work"
    $ vn_enter(bg="vt_kiosk", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_kiosk_screen")
    "The Eastgate shopping centre, upper level, half four on a Tuesday. A phone-repair kiosk outside the hobby shop: a stool, a glass counter of cases and chargers, a heat gun, a tray of tiny screwdrivers, and you."
    "[vt_pc_name] Archer. Twenty-three. You fix cracked screens all day. Your own phone's screen protector has been cracked corner to corner since March, because you never fix your own."
    "You're prising a shattered screen off somebody's mobile with a suction cup when yours buzzes on the counter."
    $ vn_enter(bg="vt_kiosk", pc="grinning", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg="vt_link")
    "Jesse, from the hobby shop, sends you a link from about four metres away, behind her own counter: a lanyard of con badges round her neck, a half-painted miniature in front of her, grinning at you over the top of it."
    "{i}you'll hate this. it's so dumb{/i}"
    vt_jesse "\"Watch it tonight. Tell me if you hate it.\""
    vt_you "\"What is it?\""
    vt_jesse "\"A channel. Two singers. They're not real, they're, like, animated. There's a teal one and a red one.\""
    "Jesse hooks up with you now and then, when neither of you has anything better on. She's funny, forward, unshockable, with a laugh you can hear from the car park. You'd watch anything she sent you."
    vt_you "\"I'll hate it.\""
    vt_jesse "\"You'll hate it {i}so{/i} much.\""
    $ vn_until(23)
    $ vt.fit = "home"
    $ vn_pass(240)
    jump vt_one_upload

label vt_one_upload:
    $ vn_enter(bg="vt_bedroom_night", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_duet_card")
    "Three in the morning. You can't sleep. Your flat, 4B, on the fourth floor of a block on the ring road. The phone's the only light in the room."
    "You open the link. A new upload, posted ten minutes ago."
    show screen vt_phone("duet")
    "The channel's called nightshiftP. That's all it says about itself."
    hide screen vt_phone
    show cg vt_duet_open onlayer cgl
    "Two girls on a little animated stage under pink lights."
    "The red one is Sawane Kiki: long red hair in two huge drill twin tails, red eyes, a wide grin with one fang poking out of it, a black choker with a silver mic-jack charm, a cropped black jacket over a red tube top that her big tits are straining, a red leather miniskirt over a huge round ass, fishnet thigh-highs and platform boots. She's loud. She grins through every line like she's picking a fight."
    "The teal one is Shizune Mio: long teal twin tails tied with black ribbons, a headset with heart-shaped earcups, a white sleeveless blouse with a high collar and a teal ribbon at the throat, straining over huge soft tits, black detached sleeves, a short pleated black skirt, black thigh-high boots. She blushes through her verses. She keeps covering her mouth."
    show cg vt_duet_dance onlayer cgl
    "They dance in matching skirts that flip. The chorus they sing together:"
    vt_duet "\"♪ Turn me up, turn me on ♪\""
    show cg vt_duet_bonus onlayer cgl
    "After the credits, a bonus scene. Kiki arches at the camera with her skirt up, grinning back over her shoulder. Mio, scarlet, presses the back of one hand to her mouth to muffle a moan, and pinches her own nipple through the blouse with the other."
    "Then it stops. The comments load."
    show screen vt_phone("duet")
    "Above them all, the pinned comment."
    hide screen vt_phone
    call vt_again
    $ vn_pass(20)
    jump vt_one_wank

label vt_one_wank:
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_one_wank")
    "You jerk off to it. Like any fan. Phone propped on the pillow, the bonus scene on loop, a normal grunt, a normal mess in a tissue, your ordinary voice."
    vn_sfx "Knock. Knock. Knock."
    "Three knocks on the wall. The neighbour in 4C. You've never met him. You turn the volume down and lie there, grinning at the ceiling, a bit embarrassed."
    call vt_sleep_till(8)
    jump vt_one_morning

label vt_one_morning:
    $ vt.fit = "nude"
    $ vn_enter(bg="vt_bathroom", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_one_shower")
    "Morning. The shower."
    $ vt_grow(1)
    "{color=#ff5fb8}Your hand goes over your chest with the soap and there's nothing there. No hair. You look down. Your chest is bare. Your belly. Your arms. Your legs, both of them, smooth as polished stone, all the way down. Even the thatch over your cock is gone.{/color}"
    "{color=#ff5fb8}You run your hands all over yourself under the water. Smooth. Everywhere. Soft as anything.{/color}"
    vt_you "\"Free wax.\""
    "You grin at the tiles. Sick."
    $ vt.fit = "work"
    $ vn_until(10)
    jump vt_one_kiosk_two

label vt_one_kiosk_two:
    $ vn_enter(bg="vt_kiosk", pc="grinning", pc_tag="vt_pc", cast=[("vt_jesse", "grinning")], cg=None)
    "The kiosk. Wednesday. You're telling a woman that her screen will be ready in an hour when your voice cracks in the middle of the word {i}hour{/i}, high and bright, like a kettle coming to the boil."
    "You cough. Carry on. Twenty minutes later it does it again."
    "Jesse leans over from the hobby shop counter."
    vt_jesse "\"Did you watch it?\""
    vt_you "\"It was dumb.\""
    "You're grinning. She can tell you watched it twice."
    vt_jesse "\"Who's best girl?\""
    vt_you "\"Haven't decided.\""
    $ vn_enter(bg="vt_kiosk", pc="grinning", pc_tag="vt_pc", cast=[], cg="vt_customer")
    "A bloke in a suit slaps his mobile on the counter, a spiderweb across it, and while you're quoting him a price your voice goes up again."
    vt_customer "\"Are you doing a voice?\""
    menu:
        "Your voice cracks on the way out."
        "Tell him to mind his own business":
            vt_you "\"Mind your own business.\""
            "It's out of your mouth before you've decided anything. He blinks. You've no idea why you said it. You quote him double."
        "Say sorry":
            vt_you "\"Sorry!\""
            "You say it before you've decided anything, high and bright, with your hand over your mouth. He blinks. You've no idea why you apologised. You quote him half."
    $ vn_until(23)
    $ vt.fit = "nude"
    jump vt_one_night

## Rung 1's act: alone, no video on, a day behind. As packaged.
label vt_one_night:
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_one_night_open")
    "The next night. Bed. You're horny before you've even lain down, hard against the duvet, and you don't put the video on. You don't need to. You just want to."
    "You get your hand round yourself. And your other hand goes up your smooth chest, and finds your nipple, and pinches it."
    show cg vt_one_nipple onlayer cgl
    "Oh."
    "That's new. That's {i}nice{/i}. That goes straight down to your cock like a wire, and you pinch it again, harder, and your hips jerk."
    "You've never done that in your life. It's very, very sensitive. You roll it between your fingers and your mouth falls open on a noise you don't want the neighbour to hear."
    show cg vt_one_hand onlayer cgl
    "So you press the back of your free hand to your mouth to keep quiet, which means letting go of your cock, which means it's just your nipple, pinched and twisted, and your hips arching up off the mattress at nothing, at the air, at nobody."
    vt_you "\"Mmh— mmmh—\""
    "Must be pent up. Must be really pent up. Good night, this. Really good night."
    "You get your hand back on your cock and you're so close so fast it's stupid."
    show cg vt_one_cum onlayer cgl
    "It's the hardest you've ever come in your life." with vnfx("flash")
    "It rips up out of you, and the moan that comes out with it isn't your moan. It's high and bright, it goes up and up, and at the top of it your voice glitches like a synth hitting a bad note:"
    vt_you "\"A-a-a-ah—!\"" with vnfx("shake")
    "And in the middle of it, to the ceiling, you hear yourself say:"
    vt_you "\"Turn me up, turn me on.\""
    "You don't know you said it."
    "You're still hard."
    $ vn_enter(bg="vt_bedroom_night", pc="horny", pc_tag="vt_pc", cast=[], cg="vt_one_pinned")
    "So you go again, straight away, with your phone in your other hand, thumbing back to the channel, the video, the comments, scrolling to the top. The pinned one."
    show screen vt_phone("duet", reply="|")
    "{i}best girl? teal or red{/i}. Your thumb's on the reply box. You're close again already."
    ## the phone goes before the menu: drawn over the choices it covered "teal" and the ending line
    ## (owner, 2026-11-15 1:33 pm ET); it comes back with the answer typed in
    hide screen vt_phone
    menu:
        "You type it with your thumb."
        "teal" (ending=True):
            $ vt.path = "teal"
        "red" (ending=True):
            $ vt.path = "red"
    hide screen vt_phone
    $ _vt_v = vt.path
    show screen vt_phone("duet", reply=_vt_v)
    "You hit send as you come for the second time, glitching, the phone slipping out of your hand onto the pillow." with vnfx("flash")
    vt_you "\"A-a-ah—!\""
    hide screen vt_phone
    if vt.path == "teal":
        jump vt_teal_two
    jump vt_red_two
