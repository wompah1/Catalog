## cleo, the two alternate routes (owner, 2026-11-13 about 1:37 pm ET, signed off from twinetesting-c9's proposal):
##   3a SOMETHING IN HER SIZE (cle.lane "bra", a tits route): week 5's advice adds a proper bra in her size; Nate applies it
##      to Friday like all of Danny's advice, and Danny keeps what Friday kept: from week 6's Saturday he has Cleo's chest, and then some: the house cap,
##      huge (the owner's ruling, 2026-11-15: alt tits lanes end at the cap). Cleo's own Fridays stay her canon size.
##      He never finds out. Femboy kept.
##   3b ASK HER TO STAY (cle.lane "stay", TSF): week 6's last advice is "ask her to stay the weekend"; Nate asks, she says
##      yes, and on Saturday it's Cleo at the counter. Danny surfaces once, lets go, and doesn't come back. The cock she
##      never uses is gone by Sunday night. Monday, her first time with a pussy, consensual. Vanripper only (a TSF lane).
## Cleo's weekend outfits: "gown", "capron" (Danny's apron, on her, over the gown), "nude".
## The swapped lines sit in script.rpy and scenes.rpy under `if cle.lane == ...`. Alternate-route art is queued last.

## ---- 3a: week 6, Saturday, the kettle -----------------------------------------------------------------
label cle_bra_kettle:
    $ cle.chest = True
    show cg cle_bra_kettle onlayer cgl
    "{color=#c8b4f0}And there's a chest on you. You look down at it in the kitchen with the kettle in your hand: breasts, huge and round and heavy, sitting up under your T-shirt like they've always lived there, stretching the print on it sideways.{/color}"
    cle_you "\"Huh.\""
    "It's Nate's cooking. It has to be. All those thirds of toast had to go somewhere, and apparently somewhere is here. You give one an experimental prod. It's very convincing."
    cle_you "\"Bulking. I'm bulking. That's what this is.\""
    "You put the kettle on. They come with you."
    return

## ---- 3a: week 6, the bathroom: the other bra in the box ----------------------------------------------
label cle_bra_mirror:
    $ vn_enter(bg="cle_bathroom", pc="flushed", pc_tag="cle_pc", cast=[], cg="cle_bra_mirror")
    "The box from the shop is still on the hall table, with the tissue paper folded back in. There were two in it. Cleo took one. The other's still there, lace, with the tags on."
    "You try it on in the bathroom, as a joke. You're going to send Nate a photo of you in it, as a joke."
    "It isn't a joke. It's a farce. You spill out over the lace on every side, and the band won't meet behind your back by a hand's width. It was bought for Cleo, and Cleo, it turns out, has a lot less going on up top than you do."
    cle_you "\"...Okay. Okay, I'm going to need a bigger bra.\""
    "You don't send the photo. On Wednesday you buy a sports bra at the big Tesco, the biggest they've got, for running. \"For running,\" you tell the woman on the till, who didn't ask, and you do go running in it, once, round the block, and it's brilliant."
    hide cg onlayer cgl
    return

## ---- 3a: the coda, after the last Friday ----------------------------------------------------------------
label cle_bra_coda:
    $ cle.on = False
    $ cle.fit = "apron"
    $ vn_enter(bg="cle_kitchen", pc="cheerful", pc_tag="cle_pc", cast=[], cg="cle_bra_coda")
    "Saturday. You're at the counter in your apron with the sports bra on under your T-shirt, doing the jollof your mum's way, and singing to the radio in your lighter voice, and getting the words wrong."
    "You still haven't worked out where the bulk went. You've stopped minding. It suits you, honestly. Everything does lately."
    "Behind you the fridge is all her. Cleo in a woolly hat. Cleo asleep on the sofa. Cleo pulling a face at the toaster. You'd love to meet her properly one day. You've got a feeling you'd get on."
    hide cg onlayer cgl
    return

## ---- 3b: the weekend she stays. Consensual -------------------------------------------------------------
label cle_stay_weekend:
    $ cle.week = 6
    $ cle.on = True
    $ cle_her_name = "Cleo"
    $ vn_clock = VNState(day=37, hour=9, minute=0)
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_wake")
    "You wake up in Nate's bed on Saturday morning, and you're still you."
    "Grey light through the curtains he never opens. His arm heavy over your waist. Your hair all over his pillow. Somewhere a bus, and the radiator ticking, and nothing pulling at you from underneath. Nobody waiting to come back up."
    "You lie there and listen for it, a bit, the way you'd listen for someone on the stairs. There's nothing."
    "So you get up."
    show cg cle_stay_slippers onlayer cgl
    $ cle.fit = "gown"
    "The pink slippers are under the bed where you knew they'd be. The dressing gown's on the back of the door. You put both on, and they're yours, and you pad out into the hall in them."
    hide cg onlayer cgl
    $ cle.fit = "capron"
    $ vn_enter(bg="cle_kitchen", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_apron")
    "The apron's on its hook by the fridge. You tie it on over the gown without thinking, and it sits right on you, and your hands know where everything is: the big pan, the good knife, the spice tin with the lid that sticks."
    if cle.cook == "jollof":
        "Jollof. Your hands do it the proper way, smoky at the bottom of the pan, the way somebody's mum does it. You don't know whose mum. It doesn't matter. It's going to be good."
    elif cle.cook == "bolognese":
        "A spag bol, a massive one, enough to freeze half. Your hands know exactly how much. It's going to be good."
    else:
        "Chicken soup. Nobody's ill. It's just that soup is what this kitchen makes when it's looking after someone, and your hands know that."
    show cg cle_stay_doorway onlayer cgl
    "Nate comes in rubbing his eyes, in his clean T-shirt, and stops in the doorway, and looks at you at his counter in the apron, stirring."
    show cle_nate sad at vn_cast_slot
    cle_nate "\"You stayed.\""
    cle_she "\"You asked.\""
    show cle_nate sad at vn_cast_slot
    cle_nate "\"I did. I— yeah. I did.\""
    "He comes and stands behind you and puts his chin on your shoulder and looks into the pan, and you feed him a spoonful off the wooden spoon, and he burns his mouth, and you both laugh."
    hide cg onlayer cgl
    show cg cle_stay_fridge onlayer cgl
    "The fridge still has a little of Steph on it: one photo, down at the bottom by the handle, her on a beach, squinting. You take it down yourself. You don't ask. You put it in a shoebox, and the shoebox on top of the wardrobe, and come back."
    "What goes up in its place is one of the two of you, from his phone, last night, blurry, both laughing. You put it in the middle."
    show screen cle_fridge(6)
    "All her. All you."
    hide screen cle_fridge
    hide cg onlayer cgl
    jump cle_stay_room

## Saturday afternoon: the other room. Danny surfaces once, and lets go
label cle_stay_room:
    $ vn_clock = VNState(day=37, hour=15, minute=0)
    $ cle.fit = "gown"
    $ vn_enter(bg="cle_hall", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_dannyroom")
    "In the afternoon you find yourself outside the other bedroom. The door's shut."
    show cle_nate sad at vn_cast_slot
    cle_nate "\"Dan's away this weekend, I think. His door's been shut since Friday.\""
    "You open it anyway. A single bed, made badly. A cookbook face down on the duvet, open at a page with a stain on it. A jacket on the chair. Trainers. A whiteboard with \"BUY: rice, onions, scotch bonnets, SLIPPERS?\" on it in green pen."
    "You sit down on the edge of the bed, in your dressing gown, and look at the whiteboard for a long time."
    show cg cle_stay_surface onlayer cgl
    "Nate's in the doorway. He looks worried, a bit. He's sweet when he's worried."
    show cle_nate sad at vn_cast_slot
    cle_nate "\"You alright?\""
    "And something comes up from underneath, the way it used to on Fridays. Not fighting. Just surfacing, warm and slow, to the top of you, for a look round."
    cle_under "\"You need to talk to somebody about this.\""
    "It comes out of your mouth in your voice, and it isn't your line. It's his. You both hear it."
    show cle_nate sad at vn_cast_slot
    cle_nate "\"I am. I'm talking to you.\""
    "Under the warm, somebody who used to live in this room hears that. And he nods, the way you'd nod at a mate across a pub when you've seen he's alright, and he lets go, like letting go of a rope in warm water."
    "He doesn't come back up. You can feel that he won't. It doesn't feel like losing anything. It feels like someone leaving a party at the right time."
    cle_she "\"I'm fine. Come here.\""
    "Nate sits down beside you on the single bed, and you lean on him, and you look at the whiteboard together. SLIPPERS?, in green pen. You laugh. You're not sure why. He laughs because you do."
    hide cg onlayer cgl
    jump cle_stay_sofa

## Saturday night: the sofa. What she never uses
label cle_stay_sofa:
    $ vn_clock = VNState(day=37, hour=22, minute=0)
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_living", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_stay_sofa")
    "Saturday night on the sofa with the telly on and neither of you watching it. Your dressing gown on the floor. You on his lap."
    cle_she "\"I've been thinking about this since breakfast.\""
    cle_nate "\"Since breakfast?\""
    cle_she "\"Since the spoon.\""
    show cg cle_stay_sofa_ride onlayer cgl
    "You sink down onto him, slow, all the way into your arse, and stay there, and grind, and his hands go where you put them."
    "His hand drifts to your cock, the way it does, and you catch it by the wrist and move it off, onto your hip. You don't want it touched. You don't want it at all, if you think about it. It's just there, small and soft between your legs, bobbing, like a bit of the sofa."
    cle_she "\"Not that. Here. Hold me here.\""
    cle_nate "\"Yes, Cleo.\""
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    cle_she "\"Harder— yeah— Nate, {i}there{/i}— {i}there{/i}— don't you stop— {i}ahh{/i}—!\"" with vnfx("flash", "shake")
    show cg cle_stay_sofa_cum onlayer cgl
    "You come on him untouched, loud, your hands on the back of the sofa, and he comes in you with your name in his mouth, and afterwards you lie there tangled up on the cushions with the telly still going, and when you look down, it's smaller. You're sure it's smaller."
    "You're not worried. You don't use it. Things you don't use go."
    hide cg onlayer cgl
    hide cle_nate
    jump cle_stay_sunday

## Sunday: the bath, the bread, and what's gone by night
label cle_stay_sunday:
    $ vn_clock = VNState(day=38, hour=11, minute=0)
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_bathroom", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_bath")
    "Sunday, a long bath, the window steamed up. You look down through the water at yourself."
    "{color=#c8b4f0}Smaller again. Barely anything: a little soft nub, tucked up, like it's shy. Your thighs press together over it and it's gone from sight.{/color}"
    "You lie back with your hair floating and your knees up and think about bread."
    hide cg onlayer cgl
    $ cle.fit = "capron"
    $ vn_enter(bg="cle_kitchen", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_stay_bread")
    "You bake the weird rye thing properly, from your starter. Not flat on one side this time. You stand over it while it cools like it's going to run off."
    cle_nate "\"That's a proper loaf.\""
    cle_she "\"Don't say anything about the shape.\""
    cle_nate "\"I wasn't going to say anything about the shape.\""
    cle_she "\"You were thinking it.\""
    "He laughs so hard he has to sit down."
    hide cg onlayer cgl
    hide cle_nate
    $ vn_clock = VNState(day=38, hour=23, minute=0)
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_sunday_night")
    "Sunday night in bed, the lamp off, his breathing slow behind you. Your hand goes down between your legs, idly, the way a hand does in the dark."
    $ cle.week = 7
    "{color=#c8b4f0}There's nothing there to find. Smooth. Soft. Then, under your fingers, a little lower, something new: a slit, soft and warm and a bit wet, that wasn't there this morning, that you somehow knew would be.{/color}"
    "You lie very still with your fingers on it, and smile in the dark."
    hide cg onlayer cgl
    jump cle_stay_monday

## Monday: the first time with it. Consensual
label cle_stay_monday:
    $ vn_clock = VNState(day=39, hour=7, minute=30)
    $ cle.fit = "nude"
    $ vn_enter(bg="cle_nate_room", pc="warm", pc_tag="cle_pc", cast=[("cle_nate", "happy")], cg="cle_stay_monday")
    "Monday morning. His alarm. He groans and rolls over and kisses your shoulder, and then the back of your neck, and you take his hand and put it between your legs."
    cle_nate "\"Cleo— oh. Oh.\""
    cle_she "\"Yeah.\""
    "He doesn't ask. Nate never asks what changed; he just meets what's there. His fingers find you, slow, and you open your knees for him, and he makes a sound like the bread came out right."
    cle_nate "\"It's Monday.\""
    cle_she "\"It's Monday. Be late.\""
    show cg cle_stay_first onlayer cgl
    "You pull him over on top of you and guide him in, yourself, slow, the head of him pressing at something that's never been touched, and then in, and in, and you hold your breath the whole way."
    cle_she "\"Oh— oh, {i}Nate{/i}— that's— that's {i}new{/i}— don't move, don't move yet—\""
    cle_nate "\"I'm not moving. Tell me.\""
    cle_she "\"Now. Slow. Slow— {i}yes{/i}—\""
    show cg cle_stay_first_mid onlayer cgl
    "He goes slow, the way you ask, and then less slow, the way you ask, and it's nothing like before and exactly like before, the full deep ache of him, from a whole new angle, and your heels go into the backs of his thighs and pull."
    vn_sfx "{i}Pap. Pap. Pap.{/i}"
    cle_she "\"Harder— oh God, harder— it's so {i}good{/i}— Nate— I'm gonna— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg cle_stay_first_cum onlayer cgl
    "You come round him, squeezing, a whole new kind of squeezing, and he comes in you, deep, with your name in his mouth, and his alarm goes off again on the bedside table, and neither of you reaches for it."
    cle_nate "\"Cleo.\""
    cle_she "\"Hi.\""
    hide cg onlayer cgl
    $ cle.fit = "capron"
    $ vn_enter(bg="cle_kitchen", pc="warm", pc_tag="cle_pc", cast=[], cg="cle_stay_after")
    "He's late for work. You're at the counter in the apron afterwards, with tea, and the fridge all her and the one photo of the two of you in the middle, and the slippers on."
    "The flat's two people. It always was."
    $ vn_feat("It's Monday")
    hide cg onlayer cgl
    call cle_week_end
    jump cle_route_return
