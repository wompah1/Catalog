## The misclick's passages: THE SOURCE (written straight in Ren'Py, 2026-11-11; the catalog's twee is
## kept verbatim in catalog/docs/routes/vn-original/mistaken/ for reference). One label per scene.
## The register: reluctant, to keep the secret (route.rpy's header).

## ==== THE OPENING DAY: the misclick, the makeover, the audition, the signing (rung 1) ===========

label mk_opening:
    $ mk.fit = None
    $ vn_enter(bg="mk_flat", pc="nervous", pc_tag="mk_pc", cg="mk_open_misclick")
    "Two hundred applications in a fortnight."
    "Bar work. Dog walking. A man in a foam sandwich costume. You stopped reading the tops of the forms days ago."
    "You're twenty-five. An actor. Your last job was a cereal advert, and the cheque bounced."
    "Two in the morning. One more."
    "{color=#ff7aa8}Blaze Productions, Elk Street. Immediate pay! Showcase your star quality!{/color}"
    "Stage name? You start typing. Autocomplete finishes it for you."
    "{color=#ff7aa8}Alexis Star.{/color}"
    vn_sfx "Tab. Tab. Tab."
    "Selfie. Submit. You pass out on the sofa with the laptop on your chest."
    $ vn_set_time(9, 0)
    hide cg onlayer cgl
    show mk_pc neutral at vn_pc_slot
    vn_sfx "Ping!"
    "Nine o'clock."
    "{color=#5fd3c6}Hi Alexis! We LOVED your photo. Can you come in this afternoon? Two o'clock, Elk Street. Adults only, women only, bring ID. Can't wait to meet her!{/color}"
    show mk_pc shocked at vn_pc_slot
    "You scroll up. The top of the form. In bold."
    "{color=#ff7aa8}Women only.{/color}"
    mk_alec "\"Oh, no. No, no, no—\"" with vnfx("shake")
    vn_sfx "BANG."
    show cg mk_open_email onlayer cgl
    "The front door. Jessie Lane: twenty-six, your best mate since a fringe show six years ago, makeup artist, owner of a key to your flat."
    "Sunglasses. Two iced coffees. The big black case over her shoulder."
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"Coffee is salvation. Give me ten minutes before I care about your career, Alec.\""
    mk_alec "\"Jess. {i}Jess.{/i} Look.\""
    "She reads it over your shoulder."
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"{i}Alexis?{/i}\""
    mk_alec "\"Autocomplete!\""
    "She snorts. Then she stops. Then she grabs your chin and turns your face to the window."
    hide cg onlayer cgl
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"What does it pay?\""
    mk_alec "\"Jessie! It's porn! They'll want me {i}naked{/i}! Sucking cock! On {i}camera{/i}!\""
    mk_jessie "\"Rent's due Friday, babe.\""
    "It lands like a slap. Friday. The letter on the mat with red on it."
    "Two hundred applications. One reply."
    mk_alec "\"They'll know. The second I walk in, they'll {i}know{/i}.\""
    show mk_jessie smile at vn_cast_slot
    mk_jessie "\"Not if I'm doing your face. You've got cheekbones you've done absolutely nothing with.\""
    vn_th "(It's fraud. It's actual fraud. You'd be lying to a whole building.)"
    vn_th "(...It's also three weeks' rent for one afternoon.)"
    mk_alec "\"...Just the audition. I go, I get a no, I come home.\""
    mk_jessie "\"Sure, babe. Five hours. That's plenty.\""
    vn_sfx "Clack. Clack."
    show cg mk_case_open onlayer cgl
    "She thumps the case onto the coffee table. The lid comes up. The trays fold out like a staircase."
    $ _mk_trays = mk_tray_list(1)
    "[_mk_trays!c]. Everything a woman is, in a box."
    mk_jessie "\"What are we building today?\""
    "She grins at your face like it's a blank canvas."
    mk_jessie "\"All of her.\""
    jump mk_makeover

label mk_makeover:
    $ vn_enter(bg="mk_flatbath", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "neutral")])
    vn_sfx "Snap."
    "She snaps on latex gloves."
    mk_jessie "\"Strip. All of it. Razor and wax first. Alexis doesn't have a hair below the eyebrows.\""
    mk_alec "\"All of it? Jess, you've known me six years—\""
    mk_jessie "\"And I've seen worse at drag brunch. Off.\""
    show cg mk_mk_wax onlayer cgl
    vn_sfx "Rrrip!" with vnfx("shake")
    mk_alec "\"{i}Ahhn!{/i}\""
    "A hot jolt. Straight down. Straight to your cock."
    mk_jessie "\"Mm-hm.\""
    vn_sfx "Rrrip. Rrrip."
    "Legs. Arms. Chest. Then she has you spread your feet and shaves everything below the waist."
    "Quick. Businesslike. She moves your cock aside like it's furniture."
    vn_th "(Don't get hard. Don't get hard. Do NOT get—)"
    "You're rock hard by the end. She doesn't even look."
    $ mk_body(1)
    show cg mk_mk_smooth onlayer cgl
    "{color=#ff9ecb}Smooth. Pink. Bare all over.{/color}"
    "You run your hands down yourself. Shins. Thighs. Chest. Smooth as glass, your balls bare and tingling."
    mk_alec "\"Ohh— that's {i}weird{/i}— that's so {i}nice{/i}—\""
    "You can't stop stroking your own legs. You hate that you can't stop."
    show cg mk_mk_tape onlayer cgl
    mk_jessie "\"Now the tape.\""
    "She kneels. Folds your cock and balls back between your thighs, holds them flat with one palm, and tapes."
    vn_sfx "Shrrk. Shrrk. Shrrk."
    "Strip over strip. Tight."
    mk_jessie "\"Little by little. You're safe. Breathe.\""
    "You look down. Nothing there. A smooth flat front."
    vn_th "(Where did it go. Where did it GO.)"
    hide cg onlayer cgl
    show mk_jessie smile at vn_cast_slot
    mk_jessie "\"So. Who is she?\""
    menu:
        mk_jessie "\"Sweet? A brat? Or the kind of girl who walks in like she's already been on her knees in there?\""
        "Sweet. Nervous, and it shows.":
            $ mk.look = "sweet"
        "A brat. She bites back.":
            $ mk.look = "bratty"
        "Filthy. And she knows it.":
            $ mk.look = "filthy"
    jump mk_makeover_look

label mk_makeover_look:
    $ vn_enter(bg="mk_flat", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "smile")])
    if mk.look == "bratty":
        mk_jessie "\"A brat!\""
        "Jessie cackles."
        mk_jessie "\"Red mouth. Bitchy brows.\""
    elif mk.look == "filthy":
        mk_jessie "\"Ooh, {i}filthy{/i}. Dark red. Black eyes. Waterproof, babe. Trust me.\""
    else:
        mk_jessie "\"Sweet! Pink mouth. Big eyes. The crew'll want to make her tea.\""
    vn_th "(You picked a personality for a woman who doesn't exist. To go and lie to strangers. In a porn studio.)"
    show cg mk_mk_forms onlayer cgl
    "The forms. Two heavy silicone tits, warmed in her palms, glued on."
    vn_sfx "Shlk."
    "They {i}sway{/i}. You've got cleavage."
    mk_alec "\"Jess, they're— they {i}move{/i}—\""
    "Hip pads. Ass shaper."
    vn_sfx "Jiggle."
    mk_alec "\"It wobbles!\""
    mk_jessie "\"That's the point.\""
    hide cg onlayer cgl
    "Contour, carving your cheekbones. Lashes. Lips."
    "Her brush drags across them and it goes straight down into the tape."
    mk_alec "\"{i}Hnn{/i}—!\""
    "She doesn't look up. The wig: sleek chestnut, down past your shoulders."
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"Voice drills. {i}Ma-me-mi-mo-mu.{/i} Higher.\""
    mk_alec "\"{i}Ma-me-mi-mo-mu.{/i}\""
    mk_jessie "\"Now say {i}oh, Diego{/i}.\""
    mk_alec "\"Who's Diego?\""
    mk_jessie "\"Every studio's got one. Say it like you're cumming.\""
    mk_alec "\"...{i}Ohh, Diego~{/i}\""
    vn_sfx "Thump."
    "Jessie falls off the sofa laughing."
    "Last, her red dress. Lace underneath. Black stockings. Red heels."
    $ mk.fit = "dress"
    show cg mk_mk_mirror onlayer cgl
    "The mirror."
    "Chestnut hair. Red dress. Tits. Hips. An ass the dress clings to."
    "A girl."
    vn_th "(...Oh no. She's {i}pretty{/i}.)"
    if mk.look == "bratty":
        mk_alexis "\"Hi. I'm Alexis.\""
        "Your lip curls all on its own."
        mk_alexis "\"Don't stare, it's rude.\""
    elif mk.look == "filthy":
        mk_alexis "\"Hi. I'm Alexis.\""
        "You lick your lip. Slow. Where did that come from."
        mk_alexis "\"You can stare.\""
    else:
        mk_alexis "\"H-hi. I'm Alexis.\""
        "It comes out soft and shaky. That part isn't acting."
        mk_alexis "\"I'm new.\""
    vn_sfx "Pop."
    "Jessie's bubblegum."
    mk_jessie "\"Eminently fuckable. Let's go get you a job.\""
    vn_th "(Just the audition. They'll say no. They'll say no.)"
    $ vn_until(14)
    jump mk_audition

label mk_audition:
    $ vn_enter(bg="mk_reception", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "smile")])
    "Blaze Productions. A white desk. A black leather sofa. A visitors' book."
    "You sign it. {color=#ff7aa8}Alexis Star.{/color} Your hand shakes on the {i}x{/i}."
    mk_jessie "\"Chin up. Smile. Claim it.\""
    "She whispers it, and sits down on the sofa, and leaves you to the stairs."
    $ vn_enter(bg="mk_office", pc="nervous", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")])
    "Upstairs. Veronica Blaze: forty-six, black bob, red nails, owns the place."
    "A tripod in the corner. A salad on the desk."
    mk_veronica "\"Alexis Star?\""
    mk_alexis "\"Yes.\""
    "In Alexis's voice. It holds."
    "She looks at the dress. The tits. The waist."
    vn_th "(She's going to ask. She's going to ask for ID and look at it and look at you and—)"
    "She doesn't ask."
    mk_veronica "\"Walk for me.\""
    show cg mk_aud_walk onlayer cgl
    "Heel, toe, hips rolling. The forms bounce."
    "The tape squeezes every step, and something under it throbs."
    mk_veronica "\"Again. Slower.\""
    vn_sfx "Crunch."
    "A forkful of salad."
    mk_veronica "\"Now. Backstage at a party, some guy's flirting with you. Go.\""
    hide cg onlayer cgl
    if mk.look == "bratty":
        show mk_pc smirk at vn_pc_slot
        "You cock a hip."
        mk_alexis "\"Aww, that's {i}sweet{/i}. But I'm not here to play nice.\""
        "Lean in."
        mk_alexis "\"I bite back.\""
    elif mk.look == "filthy":
        show mk_pc smirk at vn_pc_slot
        "You look the air up and down like it's already yours."
        mk_alexis "\"Mm. Cute. But I bite back. Ask nicely and I'll show you where.\""
    else:
        show mk_pc nervous at vn_pc_slot
        "You tuck your hair behind your ear. Look up through your lashes."
        mk_alexis "\"Oh, that's so sweet... b-but I bite back.\""
    show mk_veronica smirk at vn_cast_slot
    "Veronica's mouth twitches."
    mk_veronica "\"Fine. Show me your mouth.\""
    show mk_pc shocked at vn_pc_slot
    vn_sfx "Thwup."
    "She pulls a silicone cock out of her desk drawer. Fat. Veiny."
    "Suction-cupped to the front of the desk at mouth height."
    vn_sfx "Click."
    "She flicks the camera on. Red light."
    mk_veronica "\"Knees. Take your time. I'm on my lunch.\""
    vn_th "(No. No no no. Say no. Say it's not— say—)"
    vn_th "(Say no and she'll look at you properly. Say no and she'll ask why.)"
    vn_th "(...Rent's due Friday.)"
    menu:
        "You get down on your knees on her carpet."
        "Slow, and pretty, for the lens":
            $ mk.tape = "pretty"
        "Sloppy. Let it get messy.":
            $ mk.tape = "sloppy"
        "Talk to the camera the whole time":
            $ mk.tape = "talk"
    jump mk_audition_tape

label mk_audition_tape:
    $ vn_enter(bg="mk_office", pc="flushed", pc_tag="mk_pc", cg="mk_aud_toy")
    "On your knees. Red dress. Mouth open. A woman eating a salad."
    if mk.tape == "sloppy":
        "You take it deep, right away. If you're doing this you're doing it fast."
        vn_sfx "Glk. Glk. Hlk."
        "Drool down the shaft, down your chin. It hits the back of your throat and you moan round it and keep going."
        vn_sfx "Shlrrp."
        mk_alexis "\"Mmf— {i}hah{/i}— it's so {i}big{/i}— I can't fit it— {i}glk{/i}—\""
        "Lipstick smeared, chin glossy. Grinning. You don't know why you're grinning."
    elif mk.tape == "talk":
        "Eyes on the red light. A long slow lick, base to tip."
        mk_alexis "\"You wanna watch me suck it?\""
        "Tip on your lip."
        mk_alexis "\"Tell me how deep.\""
        vn_sfx "Glk."
        "All the way. Hold. Eyes wide, staring down the lens."
        vn_sfx "Pop."
        mk_alexis "\"Like that? I want it like that. Fuck my mouth. {i}Please{/i}—\""
        vn_sfx "Glk glk glk."
        vn_th "(Who IS that. Who's saying that.)"
    else:
        "Hair over one shoulder. Kiss the tip. Just the head. Eyes up through your lashes."
        vn_sfx "Shlp. Shlp."
        "Deeper each time. Cheeks hollow."
        mk_alexis "\"Mmh— {i}mmnh{/i}~\""
        "The camera likes the noise. So you make more."
    "Your mouth knows the shape before you do. Lips over teeth, tongue flat. Nobody ever taught you that."
    show cg mk_aud_toy_peak onlayer cgl
    "And you're {i}so{/i} hard. Under the tape."
    "Throbbing against the strips, trapped, getting nowhere, leaking into the lace."
    mk_alexis "\"{i}Hah{/i}— {i}ahh{/i}— oh god— {i}mmmf{/i}—\""
    "You're humping the air on her carpet."
    vn_th "(Stop. Stop moving your hips. She'll see. She'll SEE—)"
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"You can stop whenever you like.\""
    "Mouth full of salad."
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"You can say no.\""
    vn_th "(You can't. You can't, and she doesn't know why, and that's the only thing keeping you safe.)"
    "You don't. Nose to the desk. Hold it."
    "Your trapped little cock pulses and pulses against the tape and you {i}moan{/i} round the silicone." with vnfx("shake")
    hide cg onlayer cgl
    show mk_pc flushed at vn_pc_slot
    show mk_veronica neutral at vn_cast_slot
    "You sit back on your heels. Spit down your throat. Face a ruin."
    vn_sfx "Click."
    "Red light off."
    mk_veronica "\"Trial contract.\""
    "She slides a sheet across the desk."
    mk_veronica "\"One month.\""
    jump mk_signing

label mk_signing:
    $ vn_enter(bg="mk_office", pc="nervous", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")], cg="mk_aud_sign")
    "Talent. Scene partner. Acts as agreed. And the dotted line, with a name typed under it."
    "{color=#ff7aa8}Alexis Star.{/color}"
    vn_th "(Sign it and it's real. Sign it and it's fraud with a signature on it.)"
    vn_th "(Don't sign it and walk out past her in a red dress with your mascara running, and she watches you go, and she {i}wonders{/i}.)"
    "You sign."
    $ mk.signed = True
    $ mk_advance(1)
    hide cg onlayer cgl
    "Veronica shakes your hand. Firm. Cool. A handshake: she never touches the talent."
    mk_veronica "\"Welcome to Blaze, Alexis. Wardrobe at nine. Crystal will find you.\""
    $ vn_enter(bg="mk_reception", pc="shocked", pc_tag="mk_pc", cast=[("mk_jessie", "neutral")])
    "Downstairs, Jessie's off the sofa."
    mk_jessie "\"Well?\""
    mk_alexis "\"I got it. Jess. I got the job.\""
    show cg mk_aud_hug onlayer cgl
    mk_jessie "\"{i}KYAAA!{/i}\"" with vnfx("shake")
    "She crushes you in a hug, forms and all."
    if mk.look == "filthy":
        "Your mascara holds. Waterproof, babe."
    else:
        "Your mascara runs."
    mk_alexis "\"She never asked. She never even {i}asked{/i}.\""
    mk_jessie "\"Why would she? Look at you.\""
    vn_th "(Now you have to come back tomorrow. And the day after. And keep being her.)"
    hide cg onlayer cgl
    $ vn_set_time(22, 0)
    $ vn_enter(bg="mk_flat", pc=None, pc_tag="mk_pc", cg="mk_unbuild")
    "That night at the kitchen table she takes Alexis off you."
    "Wig. Face. Forms, peeled off with a wet {i}shlk{/i}. Pads. Tape."
    "The red dress goes on a hanger."
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"Same again tomorrow. Sleep, Alec.\""
    vn_th "(Alec. Right. That's you. You'd nearly forgotten.)"
    $ mk.fit = None
    call vn_night(7)
    jump mk_morning

## ==== THE DAYS: mornings, the studio, the makeup room ======================================

## The night after a rung: the body for the next rung lands while you sleep (rungs 2-4), and the
## waking misreading is one spoken line. Then the day's call. Rung 5 lands on set, rung 6 mid-scene.
label mk_morning:
    $ _t = mk.tier or 0
    $ mk.fit = None
    if _t == 1:
        $ mk_body(2)
        $ mk.fit = "boxers"
        $ vn_enter(bg="mk_flat", pc="shocked", pc_tag="mk_pc", cg="mk_mor_hips")
        "You wake up in yesterday's lashes. The red dress hangs on the back of the door."
        "{color=#ff9ecb}You stretch. Your hands go to your waist, and keep going in. Slide down, and your hips come out to meet them.{/color}"
        "{color=#ff9ecb}A waist. Actual hips, flaring out under your palms. Your bum's rounder in your boxers, a soft little curve that wasn't there yesterday.{/color}"
        mk_alec "\"{i}Hah{/i}— what—\""
        "You grab a handful. It jiggles. You moan before you can stop yourself."
        mk_alec "\"Must be coming down with something.\""
        "It comes out a step lighter."
        vn_th "(Bloating. Water. Something. It doesn't matter. Nobody looks at Alec anyway.)"
        hide cg onlayer cgl
        "{color=#5fd3c6}Blaze: Wardrobe at nine, Alexis. Lingerie stills, then your first scene. Crystal will find you.{/color}"
        vn_th "(Your first {i}scene{/i}.)"
    elif _t == 2:
        $ mk_body(3)
        $ mk.fit = "tee"
        $ vn_enter(bg="mk_flat", pc="flushed", pc_tag="mk_pc", cg="mk_mor_nipples")
        "{color=#ff9ecb}Your nipples wake you up. Tingling. Puffy. Swollen up off your chest.{/color}"
        "Your T-shirt drags over them and you go {i}nnh{/i}."
        "You pinch one through the shirt."
        vn_sfx "Zing."
        mk_alec "\"{i}Nnh{/i}— fuck— {i}fuck{/i}—\""
        "Both hands. You roll them till your knees go."
        show cg mk_mor_lips onlayer cgl
        "{color=#ff9ecb}Mirror: a softer face, fuller lips, pink with nothing on them. Hair past your ears, coming in chestnut.{/color}"
        "Down there, everything's gone small and shy. You cup the lot and it hardly fills your fingers."
        mk_alec "\"Slept on my face.\""
        "In a voice that purrs."
        hide cg onlayer cgl
        "{color=#5fd3c6}Blaze: Makeup counter with Crystal first thing. Then your close-up. Diego again.{/color}"
        menu:
            "{color=#5fd3c6}Blaze: also, the catalogue lot need a girl for the morning, if you want the extra.{/color}"
            "Take the catalogue job first (the extra money)":
                jump mk_filler_catalogue
            "Straight to your call":
                pass
    elif _t == 3:
        $ mk_body(4)
        $ vn_enter(bg="mk_flat", pc="shocked", pc_tag="mk_pc", cg="mk_mor_hair")
        "{color=#ff9ecb}Hair on your shoulders. Chestnut. Same as the wig on the dresser.{/color}"
        "{color=#ff9ecb}Two soft little swells under your puffy nipples. They jiggle. You squish them together and get a tiny cleavage, and squeak at it.{/color}"
        vn_th "(That's not water. That's not bloating. That's {i}not{/i}—)"
        show cg mk_mor_ass onlayer cgl
        "Your weight's all wrong: hips, ass, thighs. Your jeans only go on lying down, and your ass sits up in the back of them."
        mk_alec "\"Ohh— {i}ohh{/i}— look at it—\""
        "You bounce it at the mirror. It keeps bouncing after you stop."
        "Down there: a soft pink little thing that'd fit in your palm with room to spare."
        mk_alec "\"I need a haircut.\""
        "You don't book one."
        hide cg onlayer cgl
        show mk_jessie neutral at vn_cast_slot
        mk_jessie "\"Morning, Alec. Morn— Alexis. Alec. God. Coffee.\""
        "Jessie, at your kitchen table. She stares at your hair a long time."
        "{color=#5fd3c6}Blaze: Rear-angle scene today. Veronica wants more. Diego.{/color}"
    elif _t == 4:
        $ vn_enter(bg="mk_flat", pc="flushed", pc_tag="mk_pc")
        "You wake face down. You stay face down."
        "Your ass tingles where he was. Deep. Full. Every time you shift, your belly goes warm and stupid, and you grin into the pillow."
        vn_th "(You shouldn't be grinning. You should be— you don't know what you should be.)"
        show cg mk_mor_fork onlayer cgl
        "You roll over. Two soft swells lift your T-shirt. The forms hardly fit over them yesterday."
        mk_alec "\"Pulled something.\""
        "You tell the kettle."
        hide cg onlayer cgl
        "{color=#5fd3c6}Blaze: THE MARQUEE. Today. Top of the sheet. Don't be late. — V{/color}"
        "{color=#5fd3c6}Jessie: we need to talk about the forms. at the counter.{/color}"
        menu:
            "{color=#5fd3c6}Gus: insert going before the marquee call. rear angle, Diego, no face. yours if you want it.{/color}"
            "Take Gus's insert before the call":
                jump mk_filler_rear
            "Straight to the marquee":
                pass
    elif _t == 5:
        if mk_femboy():
            $ vn_enter(bg="mk_flat", pc="smirk", pc_tag="mk_pc")
            "{color=#ff9ecb}Pink ridges on your chest where the forms' edges hugged you all night. Under them, your own chest: puffy. Not one bit more.{/color}"
            "{color=#ff9ecb}Platinum hair all over the pillow. Ass and thighs filling the bed.{/color}"
            "Under the sheet your cock's a soft little nub. It never got hard on set. It came anyway, drooling into the tape."
            "You flick it. Nothing. You giggle."
            mk_alexis "\"Useless.\""
            "You roll over onto your big new ass and press your chest flat."
            mk_alexis "\"Still got it.\""
        else:
            $ mk.fit = "nude"
            $ vn_enter(bg="mk_flat", pc="shocked", pc_tag="mk_pc")
            mk_alexis "\"Morning.\""
            "It isn't your voice. It's hers. Light, husky, a woman's morning voice."
            mk_alexis "\"...Morning.\""
            "Still hers."
            "{color=#ff9ecb}Your tits are heavy on your chest. They sway when you turn. Platinum hair everywhere.{/color}"
            "The tape's on the bathroom floor, and there was almost nothing under it."
            vn_th "(You could stop now. Walk into Blaze and say {i}actually{/i}— and say what? Look at you.)"
            vn_th "(...You don't want to stop. When did that happen.)"
            $ mk.fit = None
        "Nothing from Blaze. The sheet's up at the studio."
    elif _t == 6:
        if mk_femboy():
            $ vn_enter(bg="mk_flat", pc="smirk", pc_tag="mk_pc")
            "Brick dust on your palms. The taste of him. A slow warm glow deep in your ass."
            "{color=#ff9ecb}Your ass fills the bed. Your thighs won't stop touching.{/color}"
            "You tape up at the sink before the kettle boils. Hardly anything to tuck."
        else:
            $ mk.fit = "nude"
            $ vn_enter(bg="mk_flat", pc="flushed", pc_tag="mk_pc")
            "You wake up with your hand between your legs."
            "{color=#ff9ecb}Soft. Wet still. Two lips and a little nub that jumps when you touch it.{/color}"
            mk_alexis "\"{i}Hah{/i}— still there.\""
            "The tape's in your handbag. You throw it in the bin."
            $ mk.fit = None
        "Jessie will be at the studio already. With the case."
        if mk_femboy():
            jump mk_end_case
        jump mk_end_star
    jump mk_studio

## Sign the book: the day at Blaze. Who's about (by the rung), the billing, the case, the call.
label mk_studio:
    $ _due = (mk.tier or 0) + 1
    $ mk.fit = None
    $ vn_enter(bg="mk_reception", pc="nervous" if _due <= 4 else "neutral", pc_tag="mk_pc")
    "You sign the book: {color=#ff7aa8}Alexis Star{/color}."
    $ _hub = MK_HUB[min(_due - 1, 6)]
    if _hub:
        "[_hub]"
    $ _bill = MK_BILLING[min(_due - 1, 6)]
    "{color=#f3c969}On the call sheet:{/color} [_bill]."
    if _due == 6:
        "Nothing with your name on it. There's a note tucked in the frame of your mirror instead."
        "{color=#ff7aa8}Hey Star. Studio wrapped early. Drink at Octave tonight? Just us. — D{/color}"
        vn_th "(Just us. No lens. No boom. No Gus.)"
        $ vn_until(20)
        jump mk_octave
    $ _call = MK_CALLS[_due]
    "{color=#f3c969}Today's call:{/color} [_call]"
    $ _build = mk_building(_due)
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"What are we building today?\""
    "Jessie yells it from makeup."
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"[_build]\""
    jump mk_makeup

## The makeup room: the case on the counter, a tray going shut, and the get-ready choice. Rung 5
## goes on to the fork (mk_marquee) instead.
label mk_makeup:
    $ _due = (mk.tier or 0) + 1
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "neutral")])
    "Bulbs, mirrors, the chair. Jessie has the case open on the counter."
    if _due == 2:
        "She picks up the razor. Puts it back."
        mk_jessie "\"Nothing's grown back. Not a prickle. Huh.\""
        "She holds the hip pad against you and frowns."
        mk_jessie "\"It's gaping. Hold still.\""
        vn_sfx "Snick."
        "A safety pin at the waist."
        vn_th "(Gaping. Because your hips are filling it. Because—)"
        vn_th "(Don't. Don't think about it in here.)"
    elif _due == 3:
        "She lifts the contour brush. Looks at your face. Puts it down."
        mk_jessie "\"Nothing to carve.\""
        mk_alec "\"Morning, Crystal—\""
        "You call it down the corridor, and it comes out a {i}purr{/i}. Crystal stops dead and grins."
        "The voice drills stay shut. The wig cap goes on over hair that's yours now, soft at the nape."
    elif _due == 4:
        "The wig stays on its stand. Your own hair's on your shoulders, chestnut, the wig's exact shade."
        "She holds the ass shaper up against you and laughs. Nowhere for it to go."
        show mk_jessie worried at vn_cast_slot
        mk_jessie "\"It's just tape now.\""
        "She says it kneeling. There's hardly anything left for it to hold."
    elif _due == 5:
        "Jasmine Gold's in the next chair. This morning she got bumped off the marquee for Crystal. She knows who to blame."
        "Two trays left. The forms and the tape. Jessie's hand is on the forms."
        jump mk_marquee
    menu:
        "Jessie pats the chair."
        "Let Jessie build you":
            $ mk.ready = "build"
        "Go in as you are":
            $ mk.ready = "self"
    jump mk_ready

## The audition gate, as the ladder's proof: "as you are" is sent back early and passes late (the
## catalog's readings: under the bar at rungs 2-3, over it from rung 4).
label mk_ready:
    $ _due = (mk.tier or 0) + 1
    if mk.ready == "self":
        $ vn_enter(bg="mk_reception", pc="nervous", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")])
        "You walk out as you are. Your own clothes. No wig. No face."
        if _due >= 4:
            "Veronica's on the stairs. She looks up. She looks down. She keeps walking."
            "That's it. She doesn't send you back."
            vn_th "(She didn't— she looked right at you. At {i}you{/i}. And kept walking.)"
            mk_unk "\"Morning, Alexis.\""
            "The girl from wardrobe, arms full of lace. Nobody looks twice."
            "Behind you, Jessie lets out a breath she's been holding for weeks."
            $ mk.self_passed = (mk.self_passed or 0) + 1
            $ mk.fit = None
            jump expression MK_RUNG_LABEL[_due]
        "You get as far as the stage door."
        if _due == 2:
            mk_veronica "\"No. Makeup. I've got a woman on the sheet this morning. Go.\""
            "She doesn't look up."
        else:
            "Veronica looks at your face a beat too long."
            mk_veronica "\"Closer. Not yet. Makeup.\""
        vn_th "(Closer. Closer to {i}what{/i}.)"
        "Jessie just pats the chair. An hour in it."
        $ vn_pass(60)
    $ vn_enter(bg="mk_makeup", pc="neutral", pc_tag="mk_pc", cast=[("mk_jessie", "neutral")])
    "You sit. Jessie builds."
    if _due == 2:
        "Tape. Forms. Pinned hip pad. Shaper. Contour. Wig. {i}Ma-me-mi-mo-mu{/i} in the mirror. Most of the morning."
    elif _due == 3:
        "Tape. Forms. Shaper. Wig over your own hair. Done before the kettle boils."
    else:
        "Tape. Forms. Done in half a coffee."
    $ mk.fit = "dress"
    show mk_pc neutral at vn_pc_slot
    $ _lip = MK_LIPS[mk.look or "sweet"]
    "Alexis in the mirror. Red dress. [_lip] on her mouth."
    jump expression MK_RUNG_LABEL[_due]

## ==== RUNG 2: the stills, the first scene ===================================================

label mk_stills:
    $ mk.fit = "babydoll"
    $ vn_enter(bg="mk_pastelset", pc="nervous", pc_tag="mk_pc", cast=[("mk_crystal", "smile")])
    "Wardrobe hands you a pink negligee you can see straight through, lace panties, pink garter stockings, pink heels."
    "The panties stretch tight over the tape."
    vn_th "(Can they see it. Can they see the outline. Is there an outline—)"
    mk_crystal "\"Rule one, honey.\""
    "Crystal Summers: thirty-one, on camera since twenty-two, honey-blonde, stacked, robe hanging open. She's doing up your bows without asking."
    mk_crystal "\"Nobody's looking at you. They're looking at the light. You're a shape in a frame.\""
    show cg mk_stills_pose onlayer cgl
    "Faux-fur rug. Ring light. Jessie at the back, arms folded."
    "Back arched. Knees together."
    vn_sfx "Click."
    mk_unk "\"More pout.\""
    vn_sfx "Click click."
    "Knees apart. The lace stretches over your smooth taped front."
    vn_th "(Keep your knees— no, they want them apart, they want—)"
    vn_sfx "Click."
    "You squeeze the forms together."
    mk_unk "\"Yes, Alexis! Show me how much you want it!\""
    vn_sfx "Click click click."
    show cg mk_stills_tease onlayer cgl
    "Ten minutes in, you stop shaking."
    "Thirty in, you've got a finger hooked in your panties and your mouth open over your shoulder."
    mk_unk "\"{i}Gorgeous.{/i}\""
    vn_th "(It's easier if you don't think. It's so much easier if you just do what the voice says.)"
    show cg mk_stills_jasmine onlayer cgl
    "In the corner: Jasmine Gold. Twenty-four. On camera since twenty-one. Petite, pouty, arms crossed."
    "She's checking your hairline. The edge of the forms. Your throat."
    vn_th "(She knows. She knows she knows she—)"
    "She finds nothing. She glares like it's your fault."
    hide cg onlayer cgl
    mk_crystal "\"Ignore her. Pastel bedroom's next. You're with Diego.\""
    "Crystal murmurs it in your ear."
    $ vn_pass(60)
    jump mk_first_scene

label mk_first_scene:
    $ vn_enter(bg="mk_pastelset", pc="nervous", pc_tag="mk_pc", cast=[("mk_diego", "grin")])
    "Pastel sheets. Fake sun."
    mk_gus "\"Rolling in thirty.\""
    "Gus Ferris, fifty-two, behind the camera. Terry, on sound, forty-odd and silent, lifts the boom."
    "Diego Ramos. Twenty-nine. On camera since twenty-one. Dimples, abs, silk pyjama bottoms."
    "He takes your hand and helps you onto the bed."
    mk_diego "\"You look amazing. Follow my lead. We'll dance, that's all.\""
    "He murmurs it."
    vn_th "(He's going to touch you. He's going to touch you {i}there{/i} and feel tape and—)"
    mk_gus "\"Action.\""
    show cg mk_fs_straddle onlayer cgl
    "Strap off one shoulder. The other. You roll your hips at the lens and giggle. The giggle is the bravest thing you've ever done."
    "He lets you lead."
    "You straddle his thigh. He unties your bow and mouths the forms through the lace."
    "His hands slide up your stockings, under the negligee, between your legs—"
    show cg mk_fs_tape onlayer cgl
    "—and stop." with vnfx("shake")
    "He's found the tape. The smooth flat front. The hard little throb under it."
    "You freeze."
    vn_th "(That's it. That's it, he's going to stop, he's going to say— in front of everyone—)"
    "He doesn't. Easy grin. Low, under the boom:"
    mk_diego "\"Turn for me, Star. Give them your back.\""
    show cg mk_fs_thighs onlayer cgl
    "He rolls you onto your side, back to the lens. The camera gets your ass and your stockings and nothing else."
    "His cock slides out of the silk, hot and thick, and pushes between your thighs from behind, right under the tape."
    vn_sfx "Shlk. Shlk. Shlk."
    vn_th "(He's covering for you. He's— why is he covering for you—)"
    show cg mk_fs_thighs_mid onlayer cgl
    mk_alexis "\"Oh— {i}ohh{/i}—!\""
    "The fat head pokes out between your thighs in front, every thrust. You grab it, because Alexis would."
    mk_alexis "\"So {i}big{/i}— big boy, you're so big—\""
    mk_diego "\"Squeeze. Legs and hand.\""
    "You squeeze. Your thighs clamp and roll on their own, like you've done this a hundred times."
    "He groans. Every stroke rubs the tape from underneath and you squirm against it."
    mk_alexis "\"Ahh— {i}ahh{/i}— don't stop— fuck my thighs, Diego, fuck them, {i}please{/i}—!\"" with vnfx("shake")
    vn_th "(You don't mean that. You {i}don't{/i}. Your hips mean it.)"
    mk_diego "\"Close.\""
    "He grunts it, for Gus. He rolls you onto your back, kneels up, two strokes—"
    show cg mk_fs_cum onlayer cgl
    vn_sfx "Splrt! Splrt!" with vnfx("flash")
    "Hot ropes across the forms. Up your throat. Your chin. You arch into it, mouth open, gasping."
    mk_gus "\"Cut. Lovely.\""
    show cg mk_fs_secret onlayer cgl
    "Diego wraps you in a robe and thumbs a lash off your cheek."
    "Then, so only you can hear:"
    mk_diego "\"{color=#ff7aa8}Your secret's safe, Star.{/color}\""
    "That's all he ever says about it."
    vn_th "(Safe. For now. One man in this building knows, and you have no idea what he wants for it.)"
    hide cg onlayer cgl
    menu:
        mk_gus "\"Before we wrap, I want a second angle on the hands. Tight. If the lady's up for it.\""
        "Give Gus his second angle":
            jump mk_first_sex
        "That's a wrap":
            jump mk_first_wrap

label mk_first_wrap:
    $ mk_advance(2)
    $ mk.fit = "dress"
    $ vn_enter(bg="mk_makeup", pc="shocked", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")])
    mk_veronica "\"Well done, Alexis.\""
    "Veronica, passing. She doesn't stop."
    show mk_crystal smile at vn_cast_slot
    mk_crystal "\"Hardly anyone starts like that, honey.\""
    "Crystal hands you water."
    show cg mk_fs_wrap onlayer cgl
    hide mk_crystal
    hide mk_veronica
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"You were {i}her{/i}!\""
    "Jessie tackles you in the dressing room."
    mk_alexis "\"Diego. He— he felt the—\""
    hide mk_crystal
    hide mk_veronica
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"I saw his face. He won't say anything. Some people just don't.\""
    vn_th "(Some people. You hope he's some people.)"
    hide cg onlayer cgl
    $ vn_set_time(22, 0)
    $ vn_enter(bg="mk_flat", pc=None, pc_tag="mk_pc", cg="mk_unbuild")
    "That night she takes Alexis off you again."
    "She holds the hip pad up and frowns at the safety pin."
    $ mk.fit = None
    call vn_night(7)
    jump mk_morning

## The filler after rung 2 (owner: "you can keep some filler"): the catalogue shoot, paid, no sex,
## and a near miss.
label mk_filler_catalogue:
    $ mk.fit = "dress"
    $ vn_enter(bg="mk_reception", pc="nervous", pc_tag="mk_pc", cg="mk_fill_cat")
    "The catalogue studio is two floors up and twice as bright. White backdrop. A fan. Somebody else's lingerie."
    mk_unk "\"Hand on the hip, love. Big smile. Lovely.\""
    vn_th "(Lovely. Lovely. Nobody's looking at you. You're a shape in a frame.)"
    show cg mk_fill_cat2 onlayer cgl
    "Then the stylist leans in to fix your bra strap, and her knuckles brush the edge of the form."
    vn_th "(Don't move. Don't breathe. Silicone feels like silicone, she'll—)"
    mk_unk "\"There. Perfect.\""
    "She pats your shoulder and walks off. Your heart's going like the fan."
    hide cg onlayer cgl
    "Cash, in an envelope, at the end. More than the cereal advert. In a morning."
    vn_th "(...That's the trouble, isn't it. It's so much money.)"
    $ vn_pass(240)
    jump mk_studio

## ==== RUNG 3: the masterclass, the close-up =================================================

label mk_masterclass:
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_crystal", "smile")], cg="mk_mc_counter")
    "Crystal hops up onto the makeup counter and pats the spot beside her."
    mk_crystal "\"Masterclass, honey. Dirty talk. Filth is fun. The hottest girls laugh at their own filth.\""
    mk_crystal "\"Give me your naughtiest line.\""
    "Across the room Jasmine's pretending to read her phone."
    "No contour line to find. No wig edge at your nape. She frowns."
    menu:
        "Your naughtiest line."
        "\"Do you want to see how wet you make me?\"":
            $ mk.line = "wet"
        "\"Is all that for me, big boy?\"":
            $ mk.line = "bigboy"
        "\"Careful. I bite back.\"":
            $ mk.line = "bite"
    jump mk_closeup

label mk_closeup:
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_crystal", "smile")])
    if mk.line == "bigboy":
        mk_alexis "\"{i}Is all that for me, big boy?{/i}\""
    elif mk.line == "bite":
        mk_alexis "\"{i}Careful. I bite back.{/i}\""
    else:
        mk_alexis "\"{i}Do you want to see how wet you make me?{/i}\""
    "Flat. Like reading a bus timetable."
    mk_crystal "\"Yes! Now slower. Purr it. Look {i}through{/i} the camera, honey.\""
    "You try again. And your throat does it for you: low, smoky, a real purr."
    show mk_crystal neutral at vn_cast_slot
    mk_crystal "\"...Where's {i}that{/i} been?\""
    vn_th "(You don't know. You don't know where it came from and it scares you how good it sounds.)"
    $ vn_enter(bg="mk_pastelset", pc="nervous", pc_tag="mk_pc", cg="mk_cu_kneel")
    "Close-up. You on your knees at the foot of the bed in the red dress."
    "Diego in front of you, naked, hard. Gus's lens right at your face. Crystal on an apple box in the wings."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"Follow my lead.\""
    "Fingers in your hair."
    mk_gus "\"Rolling.\""
    vn_th "(It's real. It's a real one this time. Not silicone. Him.)"
    "You purr your line. Then you open wide."
    show cg mk_cu_suck onlayer cgl
    "He's {i}real{/i}. Hot. Salty. He throbs on your tongue. You suck the head and he groans."
    show mk_crystal neutral at vn_cast_slot
    mk_crystal "\"Eyes up, honey! Both hands on the rest!\""
    vn_sfx "Shlp. Shlp. Glk."
    "Both fists twisting, spit running over your knuckles. Your wrists turn on the upstroke all by themselves."
    mk_alexis "\"Mmh— {i}mmnh{/i}~!\""
    vn_sfx "Pop."
    "A string of spit from your lip to his tip."
    mk_alexis "\"God, I love your cock, big boy. I want it all over my face—\""
    vn_sfx "Glk glk glk."
    show mk_crystal neutral at vn_cast_slot
    mk_crystal "\"Filthy girl! Laugh, honey!\""
    "You laugh round his cock. He grabs your head and gasps."
    vn_th "(You're laughing. Why are you laughing. Because she said to. Because it's easier.)"
    "Under the dress your own little cock strains against the tape. There's less of it every day."
    "It throbs anyway, leaking, and every time he hits your throat it twitches."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"Close.\""
    mk_gus "\"Face. Chin up, lady.\""
    "Tongue out. Eyes half shut. He strokes fast—"
    show cg mk_cu_face onlayer cgl
    vn_sfx "Splt! Splt! Splrt!" with vnfx("flash")
    "Across your cheek. Your lips. Your tongue. Your lashes."
    "You hold still and take it, then lick your lips, slow, all the way round."
    mk_gus "\"Cut. Lovely.\""
    hide cg onlayer cgl
    show mk_diego neutral at vn_cast_slot
    menu:
        mk_diego "\"Again for the reverse? If you've got it in you.\""
        "You've got it in you":
            jump mk_closeup_sex
        "That's a wrap":
            jump mk_closeup_wrap

label mk_closeup_wrap:
    $ mk_advance(3)
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "neutral")], cg="mk_cu_wrap")
    "Jessie wipes your face in the chair. She stops at your lips and runs her thumb over them."
    mk_jessie "\"You don't need liner any more.\""
    mk_alexis "\"Is that bad?\""
    mk_jessie "\"Less to carry.\""
    "The liner goes in her pocket, not back in the case."
    vn_th "(Less to carry. Less to fake. More of it's just... you.)"
    hide cg onlayer cgl
    $ mk.fit = None
    call vn_night(7)
    jump mk_morning

## ==== RUNG 4: the rear angle (the mandatory first anal) ======================================

label mk_rear_angle:
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")])
    "Veronica, in the doorway."
    mk_veronica "\"You're comfortable. Comfortable is where performers go to stop.\""
    "Tablet turned round."
    mk_veronica "\"More. Rear angle. You and Diego, from behind. All of it.\""
    "A beat."
    mk_veronica "\"You can say no.\""
    vn_th "(All of it. From behind. Inside you.)"
    vn_th "(Say no, and she asks why the girl who sucks on camera won't take it from behind. She asks, and she looks.)"
    mk_alexis "\"I'll do it.\""
    mk_veronica "\"Good. Gus wants you on set in an hour.\""
    show mk_jasmine sneer at vn_cast_slot
    show cg mk_ra_yank onlayer cgl
    "Jasmine Gold stops behind your chair. Narrows her eyes at your hair. Grabs a fistful at the root and {i}yanks{/i}."
    mk_alexis "\"{i}Hyaan!{/i}\"" with vnfx("shake")
    "It goes straight down your spine, hot. You bite your lip."
    "It's your hair. It's attached. Jasmine stares at the strands in her nails."
    mk_jasmine "\"...Sorry.\""
    "Not sorry. She stalks off."
    vn_th "(Your hair. Your own hair held. That should be good news.)"
    hide cg onlayer cgl
    $ mk.fit = "lingerie"
    $ vn_enter(bg="mk_rearset", pc="nervous", pc_tag="mk_pc", cast=[("mk_diego", "neutral")], cg="mk_ra_lingerie")
    "Black lace bra over the forms. Black lace panties over the tape. Garters. Platform heels."
    "Black sheet. Gus's camera rigged high behind the bed. Terry with the boom. Diego in a robe."
    "He looks you over, and once, quick, at the front of your panties."
    mk_alexis "\"It's just tape now.\""
    "You whisper it."
    mk_diego "\"It holds. And it stays out of the shot.\""
    "He tips your chin up."
    mk_diego "\"Slow. Then not. Follow my lead.\""
    vn_th "(He's done this a hundred times. You've done it never.)"
    mk_gus "\"Rolling.\""
    show cg mk_ra_fingers onlayer cgl
    "He peels your panties down off your ass. Just your ass."
    vn_sfx "Shlk."
    "Lube. One finger. Two."
    "You push your face into the sheet and pant. Your hips rock back onto his fingers before he asks. They just know."
    "Nothing's ever been in there. Then he curls his fingers and—"
    mk_alexis "\"{i}Hnnngh{/i}—!\"" with vnfx("shake")
    "Terry looks up from the boom."
    "Fingers out. You whine. The fat head of his cock presses against your hole. Slick. Waiting."
    vn_th "(Wait— wait, you're not— that's too big, that's—)"
    "Knees and elbows. Push back."
    jump mk_rear_sex

label mk_rear_after:
    $ mk_advance(4)
    $ vn_enter(bg="mk_rearset", pc="flushed", pc_tag="mk_pc", cg="mk_rs_boom")
    mk_alexis "\"{i}Ahh{/i}— {i}AHH{/i}— Diego— big boy— I'm— I'm— {i}FUUUCK{/i}—!\"" with vnfx("shake")
    "So loud Terry drops the boom and rips his headphones off."
    "Gus doesn't call cut. He keeps rolling, totally serene."
    "You lie face down on the black sheet, shaking, Diego's weight on your back."
    "The lens sees your ass, his cock, and nothing you didn't want it to."
    mk_gus "\"Cut. Lovely. Terry, you all right?\""
    mk_terry "\"Ears are ringing.\""
    vn_th "(You came. From that. From him inside you. Nothing on your cock but tape.)"
    vn_th "(...And you're still a secret. You're still a secret, and you came.)"
    hide cg onlayer cgl
    show mk_veronica neutral at vn_cast_slot
    "Veronica watches the playback over Gus's shoulder."
    mk_veronica "\"Marquee's next. Don't get comfortable.\""
    "She tells the monitor."
    $ mk.fit = None
    call vn_night(7)
    jump mk_morning

## The filler after rung 4: Gus's rear-angle insert, before the marquee call (optional).
label mk_filler_rear:
    $ mk.fit = "lingerie"
    $ vn_enter(bg="mk_rearset", pc="nervous", pc_tag="mk_pc", cast=[("mk_diego", "grin")])
    "Gus's handwriting on the sheet: {i}rear angle, Diego, no face{/i}. A red lace set on the chair."
    mk_gus "\"Ten minutes. Twenty if he's showing off.\""
    "Diego's on the bed in a robe. One eyebrow up: {i}you want it?{/i}"
    vn_th "(You don't have to. It's an insert. It's extra.)"
    vn_th "(...Your ass clenched when he raised his eyebrow. You noticed. He noticed you notice.)"
    jump mk_work_sex

label mk_work_after:
    $ vn_enter(bg="mk_rearset", pc="flushed", pc_tag="mk_pc", cg="mk_fr_cum")
    mk_gus "\"Lovely.\""
    "Flat as a pancake."
    "You came on him with the tape still on. Untouched. So loud Terry took his headphones off."
    vn_th "(You said yes to that one. Nobody made you. Nobody would have looked.)"
    hide cg onlayer cgl
    "Veronica's envelope is in your pigeonhole. Thicker than last week's."
    $ vn_pass(60)
    jump mk_studio

## ==== RUNG 5: the marquee (THE FORK, at the forms) ===========================================

label mk_marquee:
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "worried")], cg="mk_mq_tray")
    "Jessie's hand is flat on the forms tray. She doesn't open it."
    mk_jessie "\"So.\""
    "Under your T-shirt, two soft puffy swells. The forms have been squashing them flat for days."
    mk_alexis "\"They don't fit any more.\""
    mk_jessie "\"No. They're sitting on something.\""
    "Her hand stays put."
    mk_jessie "\"I can make them fit. Forever, if you want. Or you go out there as you are, and we see what you are.\""
    vn_th "(For four weeks every choice was {i}don't get caught{/i}.)"
    vn_th "(This one isn't. Nobody's waiting to find you out. This one's just— yours.)"
    hide cg onlayer cgl
    menu:
        "Jessie waits."
        "Leave the forms in the case" (ending=True):
            $ mk.branch = "tsf"
        "Put the forms on" (ending=True):
            $ mk.branch = "femboy"
    jump mk_marquee_makeup

label mk_marquee_makeup:
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_jasmine", "sneer")])
    if mk_femboy():
        mk_alexis "\"Forms.\""
        "She warms them in her palms and presses them down over your puffy little chest. Glue. No seam."
        "They squash you flat underneath. Tight. Good."
        show cg mk_mqf_forms onlayer cgl
        "Jasmine leans over from the next chair and grabs a handful of your tit."
        vn_sfx "Squeeze."
        "Silicone. Heavy. Cold. Her eyes go wide—"
        hide mk_jasmine
        show mk_crystal neutral at vn_cast_slot
        mk_crystal "\"Everyone on this floor has something in a case, honey.\""
        "Crystal, from the doorway."
        hide mk_jasmine
        show mk_crystal neutral at vn_cast_slot
        mk_crystal "\"Some of us have two. Hands to yourself.\""
        "Jasmine lets go and sulks off."
        vn_th "(Crystal knew. Crystal {i}knew{/i}, and said it like it was nothing. Like it was normal.)"
    else:
        mk_alexis "\"Leave them.\""
        vn_sfx "Clack."
        "Jessie slides the tray back into the case."
        hide mk_jasmine
        show mk_jessie neutral at vn_cast_slot
        mk_jessie "\"Retired.\""
        show cg mk_mq_real onlayer cgl
        "Jasmine leans over from the next chair and grabs a handful of your tit."
        vn_sfx "Squeeze."
        "Small. Soft. Warm. {i}Yours.{/i}"
        mk_alexis "\"{i}Hyaan!{/i}\"" with vnfx("shake")
        "Your nipple goes hard in her palm."
        hide mk_crystal
        hide mk_jessie
        show mk_jasmine sneer at vn_cast_slot
        mk_jasmine "\"...they're real.\""
        mk_alexis "\"Yep. Hands to yourself.\""
        "She never looks for a seam again."
    hide cg onlayer cgl
    show cg mk_mq_bleach onlayer cgl
    "Then Jessie bleaches your hair. Door shut. No peeking. She spins the chair round."
    "Platinum blonde."
    $ mk.platinum = True
    hide mk_jasmine
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"Marquee.\""
    "She squeezes your shoulders."
    hide mk_jasmine
    show mk_jessie neutral at vn_cast_slot
    mk_jessie "\"Go.\""
    $ vn_pass(120)
    jump mk_marquee_set

label mk_marquee_set:
    $ mk.fit = "bikini"
    $ vn_enter(bg="mk_marqueeset", pc="nervous", pc_tag="mk_pc", cast=[("mk_crystal", "smirk")])
    "White satin bed. Rose petals. You in a white string bikini that's mostly string, and white heels."
    "On the call sheet by the door, {i}Jasmine Gold{/i} is crossed out and {i}Crystal Summers{/i} is written over it."
    "Crystal drops her robe. Naked, stacked, grinning. Diego's on the bed."
    "The whole crew's watching. Veronica's at the back, arms folded."
    mk_gus "\"Rolling.\""
    "Crystal pulls you up onto your knees between her and Diego and uncaps the oil."
    if mk_femboy():
        show cg mk_mqf_grow onlayer cgl
        "Warm oil over the forms. They shine under the lights like the real thing. Under them, your own puffy nipples throb."
        "{color=#ff9ecb}Then her slick hands go lower, and you feel it. Your hips push out under her palms.{/color}"
        $ mk_body(5)
        "{color=#ff9ecb}Your ass swells back into her hands, heavier, rounder, until the bikini strings dig in. Your thighs thicken and squeeze together. Your waist pinches in.{/color}"
        mk_alexis "\"Ahh— {i}ahh{/i}— my ass— it's {i}growing{/i}, Crystal— it's growing in your {i}hands{/i}—!\"" with vnfx("shake")
        "You grind it back into her palms. The platinum hair slides down past your shoulder blades."
        mk_crystal "\"Look at this {i}ass{/i}, honey! Look what Jessie built!\""
        "Crystal gives it a double-handed squeeze for the lens."
        "Jessie didn't build that. You don't correct her."
        "Under the bikini string your tiny taped cock gives one sad little twitch and drools into the tape."
        mk_crystal "\"Forget that, honey. That's not what they're here for.\""
        mk_alexis "\"I know. It doesn't even {i}do{/i} anything!\""
        "Gleeful. And it's the first time you've meant a line on set."
    else:
        show cg mk_mq_grow onlayer cgl
        "Warm oil straight onto your small soft tits. Both her hands, round and round."
        "{color=#ff9ecb}And under her hands, your chest comes in.{/color}"
        $ mk_body(5)
        "{color=#ff9ecb}A warm, heavy swell, pushing up into her palms. Filling them. Overflowing them. The little bikini triangles slide off the fronts like stickers.{/color}"
        "{color=#ff9ecb}Your hips flare. Your ass rounds out into the satin.{/color}"
        mk_alexis "\"Ahh— {i}ahhh{/i}— they're {i}growing{/i}— Crystal, don't stop rubbing— {i}don't stop{/i}—!\"" with vnfx("shake")
        "Full D cups, bouncing every time you gasp. You grab them over her hands and squeeze with her."
        mk_crystal "\"There she is. {i}There{/i} she is, honey.\""
        "She breathes it, staring."
        "Nobody on the crew says a word. Diego's kneeling in front of you, cock in hand, mouth open."
        vn_th "(Nobody's hiding anything now. They can all see. And all they see is her.)"
    hide cg onlayer cgl
    mk_crystal "\"Squeeze them together for him, honey. Tight. Look up at him. Let's give them the marquee.\""
    "Crystal's behind you, one arm round your waist, her other hand sliding down between your thighs and pressing."
    "Your arms press them together before she's finished saying it. Nobody ever taught you that."
    jump mk_marquee_sex

label mk_marquee_after:
    $ mk_advance(5)
    if mk_femboy():
        $ vn_enter(bg="mk_marqueeset", pc="flushed", pc_tag="mk_pc", cg="mk_mqf_applause")
        "The lens loves the forms and can't leave your ass alone. Nobody can tell which part of you is Jessie's."
    else:
        $ vn_enter(bg="mk_marqueeset", pc="flushed", pc_tag="mk_pc", cg="mk_mq_applause")
        "The lens loves your tits. Real, heavy, glazed with him, heaving as you pant."
        "Crystal holds them up like a prize. No forms. Never again."
    mk_gus "\"Cut.\""
    vn_sfx "Clap. Clap clap clap."
    "And the crew applauds."
    "They {i}never{/i} do that. Terry's clapping with the boom under his arm. Gus is clapping, deadpan."
    "At the back, Veronica unfolds her arms."
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"{i}That{/i} is the marquee.\""
    vn_th "(...They're clapping for you. For Alexis. For— for you.)"
    hide cg onlayer cgl
    $ mk.fit = None
    call vn_night(7)
    jump mk_morning

## ==== RUNG 6: off camera (Octave, the alley) ===================================================

label mk_octave:
    $ mk.fit = "dress"
    $ vn_enter(bg="mk_makeup", pc="nervous", pc_tag="mk_pc", cast=[("mk_jessie", "smile")])
    if mk_femboy():
        "Jessie does your face after everyone's gone. Tape. Forms. The red dress, zipped up your back."
    else:
        "Jessie does your face after everyone's gone. Just the tape; there's almost nothing for it to hold."
        "The red dress won't close over your tits. She lets the seams out with a needle while you stand there."
    mk_jessie "\"Octave? Fancy.\""
    "She tucks Diego's note back in the mirror."
    mk_jessie "\"Go on. I'll lock up.\""
    if mk_femboy():
        $ vn_enter(bg="mk_octave", pc="nervous", pc_tag="mk_pc", cg="mk_ocf_booth")
    else:
        $ vn_enter(bg="mk_octave", pc="nervous", pc_tag="mk_pc", cg="mk_oc_booth")
    "Octave: dim, velvet booths, amber light. Diego's at the bar. He watches you walk the whole way over."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"Alexis Star herself. Thought you'd be too famous for me.\""
    "A corner booth. Knees touching. You tell him about the cereal advert; he laughs so hard the barman stares."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"You fit at Blaze. Off set too.\""
    "Quieter. Thumb circling the back of your hand."
    mk_alexis "\"I thought it was an act.\""
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"Is it?\""
    mk_alexis "\"...Not any more.\""
    vn_th "(That's true. When did that get true.)"
    "His hand slides under the table. Up your thigh. Under the dress. It stops right at the edge of the tape."
    "He raises an eyebrow."
    mk_alexis "\"Let's get out of here.\""
    "You breathe it. And for the first time since the misclick, nobody's making you."
    $ vn_pass(30)
    jump mk_alley

label mk_alley:
    $ vn_enter(bg="mk_alley", pc="flushed", pc_tag="mk_pc")
    "Bins. Brick. Pink neon on wet ground, a fine rain coming down through it."
    "No lens. No boom. No Gus."
    if mk_femboy():
        show cg mk_alf_wall onlayer cgl
        vn_sfx "Thud."
        "Your back hits the wall. His mouth's on yours. His hand's on your tit, the form heavy in his palm, your own puffy nipple pressing up from underneath."
        "He's rock hard against your belly."
        show mk_diego neutral at vn_cast_slot
        mk_diego "\"Nobody's filming.\""
        mk_alexis "\"I know— I know— {i}I know{/i}—\""
        "He spins you round. Palms on the brick."
        vn_sfx "Clink."
        "His belt. He shoves the red dress up over your ass. He doesn't touch the front of you. He knows what's taped there, and he leaves it."
        mk_alexis "\"Don't bother with it. It doesn't do anything anyway. Just— {i}this{/i}—\""
        "You pant it, wiggling back at him."
        show mk_diego neutral at vn_cast_slot
        mk_diego "\"Hands on the brick, Star. Follow my lead.\""
        jump mk_alley_taped_sex
    show cg mk_al_wall onlayer cgl
    vn_sfx "Thud."
    "Your back hits the wall. His mouth's on yours. His hand's on your tit, your real one, too big for his hand, his thumb rolling the nipple hard."
    "He's rock hard against your belly."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"Nobody's filming.\""
    mk_alexis "\"I know— I know— {i}I know{/i}—\""
    show cg mk_al_knees onlayer cgl
    "You drop to your knees on the wet concrete. Fumble his belt. His cock springs out into your hand, hot and heavy, wet at the tip."
    mk_alexis "\"Big boy.\""
    "You moan it, and swallow him."
    jump mk_alley_mouth

label mk_alley_shift:
    $ vn_enter(bg="mk_alley", pc="flushed", pc_tag="mk_pc", cg="mk_al_peel")
    "Back against the wall. His hand up your dress. He finds the tape."
    "He peels it. Strip. By strip. Eyes on yours."
    vn_th "(This is it. This is the last thing. The last bit of Alec, under a strip of tape, in an alley.)"
    show cg mk_al_shift onlayer cgl
    "Last strip off. His fingers cup what's under it—"
    "—and it's not there."
    "{color=#ff9ecb}Warm. Melting. The little thing in his palm goes soft and pulls back, smaller, smaller, sinking into you—{/color}"
    show cg mk_al_open onlayer cgl
    $ mk_body(6)
    "{color=#ff9ecb}—and {i}opens{/i}.{/color}" with vnfx("flash")
    "{color=#ff9ecb}Two soft lips, swelling apart against his palm. Slick. Hot. A little nub at the top that throbs under his fingertip—{/color}"
    mk_alexis "\"{i}HYAAAN!{/i}\"" with vnfx("shake")
    show cg mk_al_grow onlayer cgl
    "{color=#ff9ecb}And it doesn't stop there. Your tits {i}swell{/i} against his chest, huge and heavy, popping Jessie's stitches.{/color}"
    vn_sfx "Tik. Tik. Tik."
    "{color=#ff9ecb}They spill out of the neckline. Your hips spread. Your ass balloons out against the brick, soft and wide. Thick slick thighs. Platinum hair pouring down your back.{/color}"
    mk_alexis "\"Ahh— {i}AHH{/i}— they're {i}huge{/i}— Diego, feel them, {i}feel{/i} them—!\""
    "You shove his free hand onto one. Big, heavy, overflowing his palm."
    mk_alexis "\"More— oh god, it's still {i}going{/i}—!\""
    "Two of his fingers slip inside you."
    vn_sfx "Shlk."
    "Easy. Wet. Somewhere nothing's ever been."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"...Star.\""
    "Just that."
    mk_alexis "\"Don't stop. Don't stop, Diego, please. I want you {i}in{/i} me. {i}There.{/i} Please—\""
    vn_th "(Nobody asked. Nobody made you. You want it.)"
    "He lifts you by the ass, your back on the brick. Your legs wrap his waist."
    "The fat head of his cock nudges your new lips."
    jump mk_alley_sex

label mk_alley_after:
    $ mk_advance(6)
    $ vn_enter(bg="mk_alley", pc="flushed", pc_tag="mk_pc", cg="mk_al_secret")
    "Shaking. Legs round his waist. His breath in your hair. A taxi goes past on Elk Street."
    mk_alexis "\"Diego. My— you know. My secret—\""
    "He looks at you. All of you. He kisses you, slow, and smiles against your mouth."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"{color=#ff7aa8}What secret?{/color}\""
    hide cg onlayer cgl
    $ mk.fit = None
    call vn_night(9)
    jump mk_morning

label mk_alley_taped_after:
    $ mk_advance(6)
    $ vn_enter(bg="mk_alley", pc="flushed", pc_tag="mk_pc", cg="mk_alf_grow")
    "{color=#ff9ecb}And it's still going. Your ass swells into his hands while he's still in you, rounder, heavier, until the red dress's back seam goes {i}rrrip{/i}.{/color}"
    $ mk_body(6)
    "{color=#ff9ecb}Your thighs thicken till they press together all the way down. Platinum hair tumbles to the middle of your back.{/color}"
    mk_alexis "\"Ahh— {i}more{/i}— it's getting {i}bigger{/i}— squeeze it, Diego, {i}squeeze{/i} it—!\"" with vnfx("shake")
    "He does, both hands, and it spills between his fingers."
    show cg mk_alf_secret onlayer cgl
    "You turn round, back to the wall. The red dress strains over your ass, your hips, your thick soft thighs."
    "Over the smooth taped front. Over the forms, which haven't moved."
    mk_alexis "\"Diego. My— you know. My secret—\""
    "He smiles and kisses you."
    show mk_diego neutral at vn_cast_slot
    mk_diego "\"{color=#ff7aa8}What secret?{/color}\""
    hide cg onlayer cgl
    $ mk.fit = None
    call vn_night(9)
    jump mk_morning

## ==== THE ENDINGS ==============================================================================

## TSF: "Alexis Star". The case has nothing left to do, and it goes in the skip.
label mk_end_star:
    $ vn_enter(bg="mk_makeup", pc="smirk", pc_tag="mk_pc", cast=[("mk_jessie", "smile")], cg="mk_end_empty")
    $ vn_feat("Alexis Star")
    "The case is open on the counter. Every tray is empty."
    "In the mirror: platinum hair to the middle of your back. Big, heavy, real tits filling your T-shirt. Hips. Ass. Thighs."
    "Under your leggings, nothing to tape. Ever again."
    mk_jessie "\"What are we building today?\""
    "Out of habit."
    mk_alexis "\"Nothing.\""
    "You both crack up."
    vn_sfx "Clack. Clack. Clack."
    "She folds the trays shut, one by one."
    mk_alexis "\"How long have you known?\""
    mk_jessie "\"Ages. Since I pinned the hip pad.\""
    show cg mk_end_skip onlayer cgl
    "You pick up the case. Light as anything."
    "Past Crystal, who toasts you with her coffee. Past Jasmine, who opens her mouth and shuts it. Out the front door onto Elk Street."
    vn_sfx "THUNK." with vnfx("shake")
    "Into the skip."
    show cg mk_end_hand onlayer cgl
    "Jessie takes your hand. Four steps. Then she holds the door."
    mk_jessie "\"After you, Alexis.\""
    "{color=#f3c969}Nobody ever asked. There was never anything to ask about.{/color}"
    hide cg onlayer cgl
    jump mk_epilogue

## Femboy: "Still in the Case". Two trays every morning, for good.
label mk_end_case:
    $ vn_enter(bg="mk_makeup", pc="smirk", pc_tag="mk_pc", cast=[("mk_jessie", "smile")])
    $ vn_feat("Still In The Case")
    mk_jessie "\"What are we building today?\""
    mk_alexis "\"The chest and the tuck. Same as always.\""
    "She grins and folds out two trays."
    show cg mk_endf_tape onlayer cgl
    "Eleven minutes in the chair. It used to be all morning."
    "The tape: she kneels, tucks your tiny cock back between your thighs, and tapes it flat. Smooth. Gone."
    "It doesn't even stir in her fingers. It hasn't stood up in weeks. All it does now is drool when Diego's in your ass."
    mk_jessie "\"Poor little thing.\""
    mk_alexis "\"Who cares? I cum from the back now. It's just along for the ride.\""
    "You wiggle in the chair."
    show cg mk_endf_mirror onlayer cgl
    "The forms: warmed in her palms, pressed down over your own puffy little chest, edges glued. No seam."
    "In the mirror: Alexis Star. Platinum hair. Tiny waist. A huge, soft, real ass and thighs straining her skirt."
    "A chest that's half silicone and half you."
    mk_jessie "\"You good?\""
    mk_alexis "\"Yeah. Yeah, I'm good.\""
    "Under the forms your nipples press up into the silicone. You like that it's both."
    "She shuts the case with the last tray still open, ready for tomorrow."
    hide cg onlayer cgl
    show mk_jasmine neutral at vn_cast_slot
    "Jasmine walks past. Stares at your chest. Opens her mouth."
    hide mk_jasmine
    hide mk_jessie
    show mk_crystal neutral at vn_cast_slot
    mk_crystal "\"Everyone on this floor has something in a case, honey.\""
    "Jasmine shuts it."
    "{color=#f3c969}Nobody ever asked. Every morning there's something to ask about, and nobody ever will.{/color}"
    jump mk_epilogue

## The epilogue: stay or walk (either ending, the same body).
label mk_epilogue:
    $ vn_enter(bg="mk_reception", pc="neutral", pc_tag="mk_pc", cast=[("mk_veronica", "neutral")])
    "Veronica's on the stairs with a printed sheet."
    menu:
        mk_veronica "\"Well?\""
        "Sign the proper contract" (ending=True):
            jump mk_epilogue_stay
        "Hand the badge in" (ending=True):
            jump mk_epilogue_walk

label mk_epilogue_stay:
    if mk_femboy():
        $ vn_enter(bg="mk_office", pc="smirk", pc_tag="mk_pc", cg="mk_epf_contract")
    else:
        $ vn_enter(bg="mk_office", pc="smirk", pc_tag="mk_pc", cg="mk_ep_contract")
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"Contract. A proper one. Name at the top.\""
    "You write {color=#ff7aa8}Alexis Star{/color}."
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"Thursday. Don't be late. You're first up.\""
    "She files it."
    if mk_femboy():
        "Every morning: two trays, Jessie, eleven minutes, the studio."
        "The tape goes on over a cock that never gets hard any more, and nobody on set has touched it once."
    else:
        "Every morning: no case. Jessie comes anyway, with two coffees, and does your face for fun."
    "Best job you've ever had."
    jump mk_route_return

label mk_epilogue_walk:
    mk_alexis "\"I'm done.\""
    "You hand the badge in."
    show mk_veronica neutral at vn_cast_slot
    mk_veronica "\"Fine. You're good. I don't say that. Inside six months, I'll read you again. After that, I won't.\""
    if mk_femboy():
        $ vn_enter(bg="mk_busstop", pc="neutral", pc_tag="mk_pc", cg="mk_epf_walk")
        "Out on Elk Street it's raining. Taped flat under your T-shirt, ass swinging, platinum hair going dark in the rain."
        "Under the tape, nothing stirs. Nothing needs to."
    else:
        $ vn_enter(bg="mk_busstop", pc="neutral", pc_tag="mk_pc", cg="mk_ep_walk")
        "Out on Elk Street it's raining. T-shirt clinging to your tits, platinum hair plastered to your neck. Nothing under your leggings to hide."
    "Jessie's at the bus stop with two teas."
    "She hands you one. No questions. She gets on your bus, though it isn't hers."
    jump mk_route_return
