## THE SOURCE: boytoy's passages, rewritten for the VN (2026-11-12; PLAN.md). One label a passage of
## the original (main.twee, rungs.twee, rungs-late.twee, ending.twee), written as beats; the director
## scenes are in scenes.rpy. The original is in catalog/docs/routes/vn-original/boytoy/. Nobody
## explains the capsules; no blows land; nobody threatens; no heights; he/him to the last line.

## ---- WEEK 1, the door (Boytoy Rooftop, Intercom, Cloakroom, Foyer) -------------------------

label boy_rooftop:
    $ boy.fit = "hood"
    $ vn_enter(bg="boy_rooftop", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_rooftop_watch")
    show cg boy_rooftop_watch onlayer cgl
    "Sunday, nearly midnight, and the town is asleep. Except for you."
    "You're crouched on the parapet of a warehouse roof across the dock road, one boot up on the ledge, red hood up, black domino mask on, the wind off the water snapping the hood round your face. Below you the sodium lamps buzz. Across the road, the Gilded Cage glows."
    "Black brick. Every window lit gold. Gold lettering over the doors, a velvet rope, a queue of punters in sequins and good shoes. Music thumps out of it like a heartbeat. And right at the top, behind glass, a penthouse, lit soft and warm, where the shapes of people move about and never once come to the window."
    boy_you "\"Villainy. I can {i}smell{/i} it.\""
    "You tell the night. You can smell diesel, mostly. And chips. But also villainy."
    hide cg onlayer cgl
    "In the daytime you're [boy_pc_name] Penhallow, and you cut keys at a kiosk on the high street, and nobody looks at you twice. Slight and wiry, dark curls, dark eyes, a green apron and a brass key machine that goes {i}zzzhhh{/i}. You live in a bedsit over a launderette on Mer Street, where the floor is always warm from the dryers and the walls smell of fabric softener."
    "After midnight you're {b}Bantam{/b}."
    "The local paper loves you. BANTAM STRIKES AGAIN. MASKED HERO FOILS BIKE THIEF. WHO IS BANTAM? The police pretend you don't exist, which is fine, because you don't exist, officially, and you've never once needed them. You've never lost a fight. Not one. You're quick, and you're good, and you've got the best sweep on the south coast."
    show cg boy_corkboard onlayer cgl
    "And on the corkboard in the bedsit, joined up with red string, there are the posters. A scaffolder, big and cheerful in a hi-vis. A rugby prop forward with a broken nose and a gap-toothed grin. A delivery driver in his van's cap. MISSING, all of them. Last seen: the docks. Every bit of red string on that board runs to the same pin, and the pin is stuck in a photo of the tower in front of you."
    "The police say it's a licensed premises."
    "You say it's a case."
    hide cg onlayer cgl
    "You take out your phone, open the folder called CASE FILE, and hold down the record button."
    boy_you "{b}\"Bantam, field report.\"{/b} \"Target: the Gilded Cage. Going in.\""
    "Crisp and low. You stop the recording. You play it back once, to check the voice. Excellent voice. Very gravelly."
    show cg boy_pigeon onlayer cgl
    "Then, because it's a big night, and because a hero should, you stand up on the parapet with your fists on your hips and your hood blowing back, and address the town."
    boy_you "\"Citizens! Tonight, the night itself stands witness! Somewhere in that tower of gold and shame, good men are held against their will, and their {i}neighbours{/i} wonder. Their {i}employers{/i} have filed paperwork—\""
    "On the parapet beside you, a pigeon is listening. It's the only one who is. You turn to it, because a speech needs a face."
    boy_you "\"—and I say to the villains in their velvet: your reign of shame ends {i}tonight{/i}. Justice is patient. Justice is swift. Justice is—\""
    "The pigeon turns round, and walks off along the parapet, and drops off the end of it onto a skip."
    boy_you "\"—{i}wearing a hood{/i}.\""
    "You finish it, to nobody. The wind blows. A bus goes past, empty."
    "Fine. Fine. The pigeon was probably in on it."
    hide cg onlayer cgl
    $ boy.fit = "own"
    "You crouch down behind the parapet, take off the mask, and fold it in half, then in half again. You unlace your left boot, lift the insole, lay the mask flat in the bottom, and put the insole back over it. Snug. Undetectable. It squeaks a bit when you stand on it.\n{size=-5}{color=#ff8fa3}▸ Round the back{/color}{/size}"
    $ boy.mask = "boot"
    $ vn_pass(15)
    jump boy_intercom

label boy_intercom:
    $ vn_enter(bg="boy_staff_door", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "Round the back of the tower it's all bins and steam and a plain steel door with a little window, and in the window, the card. STAFF WANTED. ASK AT THE INTERCOM."
    "You straighten your collar. You hunch your shoulders a bit, to look like a man who needs a job and has never once in his life done a backflip off a bus shelter. You press the button."
    vn_sfx "{i}Bzzzt.{/i}"
    "A crackle. Then a man's voice, warm and unhurried and very amused, like he's been waiting for this exact buzz all evening."
    boy_voice "{b}\"Let him in.\"{/b}"
    vn_sfx "{i}Clunk.{/i}"
    show boy_gideon blank at vn_cast_slot
    "The lock goes. The door swings open on a wall."
    "The wall is a man. A broad man in a black suit with close-cropped black hair, a heavy brow, an earpiece curling into his collar, and a face that would be handsome if it ever moved. It doesn't. He looks at you the way a lamppost looks at the rain."
    boy_gideon "\"Name.\""
    "You give him your first name. He doesn't write it down. He just steps aside, and you go in."
    $ vn_enter(bg="boy_lift_hall", pc="heroic", pc_tag="boy_pc", cast=[("boy_gideon", "blank")], cg=None)
    "It's a back corridor, but it's the Cage's back corridor, so it's red flock wallpaper and brass light fittings and a carpet so thick your boots sink. At the end of it, a pair of brass lift doors. Over them, in curly gold letters, right across the wall:"
    "{b}{color=#e8c35a}{i}The Cage keeps what walks in.{/i}{/color}{/b}"
    boy_gideon "\"Doorman. Gideon. Read your card.\""
    "About himself. He hands you one."
    show screen boy_card("RECRUIT", ["{i}Beat the keeper, take the key. Lose, and go up anyway.{/i}"])
    "Thick cream card, gold edges, a little gold birdcage printed at the top. RECRUIT, it says, and under that, the house rules. You read it. You read it again. You turn it over to see if there's a catch on the back, and there's nothing on the back, so you read it a third time, slowly, with your lips moving."
    hide screen boy_card
    boy_you "\"What does {i}that{/i} mean?\""
    boy_gideon "\"Means what it says. Every floor's got a keeper. Keeper's got the key card for the next floor up. You want the next floor, you take it off him.\""
    "He presses the call button."
    boy_you "\"And if I lose?\""
    boy_gideon "\"Read the card.\""
    "Gideon looks at you. His face does nothing."
    vn_sfx "{i}Ding.{/i}"
    show screen boy_lift(1)
    "The brass doors slide open. Inside it's all mirrors and brass rails, and a panel of brass buttons by the doors, round and polished, and when Gideon swipes a gold card over it, one of them lights up."
    hide screen boy_lift
    boy_gideon "\"Ground floor's the door. Mine. Up there's the bar. Up there's the dressing room. Then the stage, then the VIPs. Cloakroom's yours this week. Kit's in there.\""
    "He doesn't say what's at the top. He doesn't even look at the top button."
    $ boy.fit = "k1"
    show cg boy_choker onlayer cgl
    "The kit is in there. A tight black vest. Black shorts, cut very high on the leg. A gold choker with a little brass tag on the front that says RECRUIT. You hold the choker up and look at Gideon, and Gideon looks back, and you put it on. It clicks shut at the back of your neck."
    "Your hoodie goes in a locker. Your boots stay on, with the mask flat under your left heel. The vest is so tight you can see your own ribs move."
    boy_you "\"This is an outrage. The {i}tailoring{/i}.\""
    "Under your breath, in your best Bantam voice."
    boy_gideon "\"Mm.\""
    show cg boy_capsules onlayer cgl
    show screen boy_card("", ["{i}Staff vitamins.{/i}"])
    "By the cloakroom door there's a shelf, and on the shelf a gold dish, and in the dish a heap of gold capsules, shiny as sweets. A little card propped against it, in neat gold script."
    hide screen boy_card
    boy_gideon "\"Every shift. Everybody.\""
    "You look at the dish. You look at Gideon. A real recruit would just take one. A real recruit wouldn't even think about it. Your cover is everything."
    "You take one. It goes down warm. It tastes of nothing at all, and then, at the back of your throat, faintly, of honey."
    boy_gideon "\"In you go.\"\n{size=-5}{color=#ff8fa3}▸ Friday{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(boy_to_weekday(5, 19))
    jump boy_cloakroom

## Rung 1's growth beat lands in the cloakroom, Friday: the body hair gone, the skin soft.
label boy_cloakroom:
    $ boy.fit = "k1"
    $ vn_enter(bg="boy_cloakroom", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "Friday night. The last shift of the week."
    "You've done a whole week in the cloakroom. Taking coats. Giving out tickets. Smiling at punters who don't look at you, and memorising every face that goes up in that lift. You've taken a capsule every shift, from the gold dish, for your cover, and you've learnt that the bar's on the next floor up, that the stage is loud, and that nobody, not once, has said a word about the men on your corkboard."
    "A woman in a fur stole hands you her coat. You turn, reach up for the high hook, and your vest rides up."
    $ boy_body(1)
    show cg boy_bare_arm onlayer cgl
    "{color=#ff5fb8}Your arm's bare.{/color}"
    "{color=#ff5fb8}Not bare like it's out of the sleeve. {i}Bare{/i}. The dark hair on your forearm is gone, every bit of it, and the skin under it is pale and smooth and soft as a lotion advert. You stare at it with the stole hanging off your hand.{/color}"
    boy_you "\"What.\""
    "{color=#ff5fb8}You shove the stole on the hook. You pull the vest up off your stomach and there's nothing there either: no trail, no fuzz, your chest bare and smooth as glass. You run a hand down your thigh below the shorts. Smooth. Smooth all the way down to your boots. You check down the front of the shorts with one finger, very quick, behind the counter, and it's gone down there too, all of it, and the skin's so soft your own fingertip makes you jump.{/color}"
    show boy_pc outraged
    boy_you "\"{i}Ahh{/i}— what— this is— this is TAMPERING—!\""
    "{color=#ff5fb8}Your thighs press together under the counter and the skin slides on skin, silky, warm, and that's so nice your knees go. They feel like they were made for squeezing something.{/color}"
    "{color=#ff5fb8}And your cock, under the shorts, has gone hard from your own fingertip. Just from that. It's straining the black shorts, sensitive as anything, and every time the fabric moves you have to grip the counter.{/color}"
    boy_you "\"Evidence. You are {i}evidence{/i}. Stand down.\""
    "You whisper it to it. It doesn't. Nothing else has changed: same face, same shoulders, same curls. Just smooth. Smooth all over, like somebody's polished you."
    hide cg onlayer cgl
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Hold still.\""
    "Gideon's behind the counter. You didn't hear him come in. He never makes a noise. He's got his hands up, the way he holds them for the end-of-shift search, when everybody gets patted down for tips and pens and anything they shouldn't be leaving with."
    boy_you "\"It's not the end of the shift.\""
    boy_gideon "\"Hold still.\""
    "He starts at your shoulders. Down your arms. He gets to your bare forearm and his thumb slides over the smooth skin there, slow, and stays."
    boy_gideon "\"Hm.\""
    boy_you "\"Citizen, that is my {i}arm{/i}.\""
    "Very stiffly."
    boy_gideon "\"Mm.\""
    "He moves on. Down your sides. He's very thorough, and he's very slow, and there's a queue of coats building up at the hatch, and he doesn't care at all. When the woman with the stole comes back for it, he hands it to her over your head without stopping."
    "In the end he steps back and nods."
    boy_gideon "\"Closing. Foyer.\"\n{size=-5}{color=#ff8fa3}▸ Closing time{/color}{/size}"
    $ vn_until(23)
    jump boy_foyer

## Rung 1, the scuffle and the foyer wall: the move caught; "Pay the floor."; Gideon's cock between his
## thighs from behind, his hand on Jago's cock. Non-con, no flip: a citizen's arrest, his rights
## read through moans.
label boy_foyer:
    $ vn_enter(bg="boy_foyer", pc="heroic", pc_tag="boy_pc", cast=[("boy_gideon", "blank")], cg=None)
    "The doors are shut. The last punters are gone. The foyer's empty: red flock walls, brass, a chandelier dimmed right down, the velvet rope coiled on its brass posts, the gold lettering over the lift catching the last of the light."
    "Gideon's search has started again."
    boy_gideon "\"Arms up.\""
    "You put your arms up. He pats your sides. Your ribs. The dip of your back. Then his hands go lower, and stop on your arse, both of them, a palm on each cheek through the black shorts, and stay there."
    "He squeezes."
    boy_you "\"Ahem.\""
    "He squeezes again, slow, like he's checking the fruit at a market."
    "That's it. That's enough. A week of coats and capsules and being looked through, and now {i}this{/i}, and somewhere above your head there are men on your corkboard who need a hero, and the key card to the next floor is in this man's top pocket. You saw him put it there."
    "You step back out of his hands. You plant your boots on the carpet, the mask squeaking under your heel, and bring your fists up, and drop into your stance, the one the bike thief saw, and the mugger behind the bingo hall, and that man on the pier with the stolen bagpipes."
    boy_you "{b}\"Citizen. Bantam doesn't lose.\"{/b}"
    "Gideon looks at your fists. His face does nothing."
    boy_gideon "\"Mm.\""
    menu:
        "\"Mm.\""
        "Sweep the leg":
            "You go low and fast, the way you always do, your best move, the sweep that took down the bagpipe man: one leg out, round, hooking for the back of his ankle—"
        "Citizen's arrest":
            boy_you "\"I am making a citizen's arrest!\""
            "And you go for his wrist, quick as anything, to turn it up behind his back the way the police do it on the telly—"
    hide boy_gideon
    show cg boy_foyer_catch onlayer cgl
    "He catches it."
    "He doesn't even move his feet. One big hand just {i}arrives{/i}, closes, and turns, and your own momentum takes you on round, a full half-turn, until your chest meets the wall."
    vn_sfx "{i}Fwump.{/i}" with vnfx("shake")
    "Red flock wallpaper, against your cheek. The velvet rope's brass post against your hip. Both your boots still flat on the carpet. And a hand, flat between your shoulder blades, holding you there, not hard, just completely."
    show boy_pc outraged
    boy_you "\"Hey—! That was— that was a {i}feint{/i}, that was all part of the—\""
    "You push back. You might as well push a bus."
    show boy_gideon blank at vn_cast_slot
    boy_gideon "{b}\"Pay the floor.\"{/b}"
    boy_you "\"Pay the WHAT—?\""
    show cg boy_foyer_wall onlayer cgl
    "His other hand hooks the waistband of your black shorts and draws them down your thighs to your knees. Cool foyer air on your bare arse. Then his palm, warm and dry, running slowly down the back of your thigh, over all that new smooth skin."
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Smooth as you like.\""
    boy_you "\"Right. {i}Right{/i}. Citizen. I am placing you under arrest.\""
    "Into the wallpaper. Your voice has gone up. You bring it back down."
    "Behind you, a zip goes down. Something hot and heavy lays itself along the crease of your arse, and then lower, and slides, slow and thick, into the gap at the top of your thighs."
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Clench.\""
    boy_you "\"I will NOT— you do not have to say anything—\"\n{size=-5}{color=#ff8fa3}▸ Read him his rights{/color}{/size}"
    "Your thighs clench on their own."
    jump boy_foyer_sex

label boy_foyer_after:
    $ vn_enter(bg="boy_foyer", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_foyer_cum")
    show cg boy_foyer_peak onlayer cgl
    boy_you "\"—anything you say— {i}ahh{/i}— may be given in— in {i}evidence{/i}—\""
    "His cock slides through your thighs, slow and heavy and hot, the fat head pushing out under your balls every time and dragging back, and his fist moves on your cock in exactly the same rhythm. He's not even quick. He's just completely sure. Your hips are pushing back into him on every stroke, and you didn't tell them to, and you are going to have {i}words{/i} with them later."
    boy_you "\"You're— nicked— you're {i}so{/i} nicked—\""
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Mm.\""
    "You're still reading him his rights when you come."
    show cg boy_foyer_cum onlayer cgl
    boy_you "\"—you do not have to— {i}AHH{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "It goes all over the wallpaper. Hot and white, spurting out of his fist in thick pulses right up the red flock, and your thighs clamp on his cock so hard he grunts, and your whole body shakes against the wall with his hand still flat between your shoulders."
    "And then he comes too. Hot and thick, between your clenched thighs, pumping out over the soft insides of them and dripping down to your knees, and he holds you there through all of it, still, patient, with his cock throbbing between your legs."
    boy_you "\"{i}Hhah{/i}— {i}hah{/i}— that's— that's assaulting an officer—\""
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"You're not an officer.\""
    "He steps back. He tucks himself away and does his zip up, and his hand comes off your back at last, and you stay where you are, face to the wallpaper, shorts round your knees, panting, with the wall in front of you dripping."
    "Something taps your throat. Gideon's finger, on the brass tag of the choker. He tucks something flat and stiff underneath it, against your skin, and steps away."
    hide cg onlayer cgl
    "When you finally pull your shorts up and turn round, he's gone. The foyer's empty. You put your fingers to your throat and slide it out from under the tag: a gold key card, warm from your skin. You know which button it lights."
    "You beat him. Obviously. Technically. You have the key."
    "You walk home along the docks with your thighs sticking together under your trousers and the mask squeaking in your boot, and you don't think about any of it at all, all weekend, except the whole time.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ vn_pass(boy_to_weekday(1, 9))
    jump boy_bedsit_two

## ---- WEEK 2, the bar (Boytoy Bedsit Two, Bar, Barback, Last Orders) ------------------------

label boy_bedsit_two:
    $ boy.fit = "own"
    $ vn_enter(bg="boy_bedsit", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "Monday morning in the bedsit over the launderette, and the floor is warm from the dryers downstairs, and the whole room hums."
    "You sit on the edge of the camp bed in your pants with your phone in your hand and the corkboard in front of you. The posters. The red string. The photo of the tower with the pin in it. The red hood hangs on its hook by the door, looking at you."
    show screen boy_lift(2)
    "You open CASE FILE. You hold down the button."
    boy_you "{b}\"Bantam, field report.\"{/b} \"Ground floor: cleared.\""
    hide screen boy_lift
    "You stop. You don't say how. You listen to it back, and it sounds a bit thin, so you hold the button down again."
    boy_you "\"Ground floor: cleared.\""
    "Deeper. Better. You listen to that one. You hold the button down again."
    boy_you "\"Ground floor: {i}cleared{/i}.\""
    "With feeling. You did clear it. You have the key card to prove it. It's tucked under the brass tag on the choker, which you haven't taken off, because you can't find the clasp, and because you haven't looked very hard."
    "You do it once more anyway, very low, with your eyes shut, and your thighs press together on the camp bed when you say it."
    boy_you "\"Ground floor... cleared.\""
    "Right. Shower."
    $ boy.fit = "nude"
    $ vn_enter(bg="boy_shower", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_shower_two")
    "The water comes on hot, and you put your face in it, and run your hands down your chest, and stop."
    $ boy_body(2)
    show cg boy_shower_two onlayer cgl
    "{color=#ff5fb8}Your chest is soft.{/color}"
    "{color=#ff5fb8}Not fat. {i}Soft{/i}. All the wiry muscle you built up on rooftops and fire escapes has gone smooth, like somebody sanded the edges off you in the night, and the skin over it is so silky the water just slides away. You grab your own stomach. Smooth. You grab your side, and it goes {i}in{/i}, a proper waist, curving under your hand, and then back {i}out{/i}, wider than it should, at your hips.{/color}"
    boy_you "\"No. No. Absolutely not. Stand {i}down{/i}—\""
    "{color=#ff5fb8}You tell your hips. They don't. They're only a touch wider, but you can feel it, the new swing in them when you turn under the water. Your curls are plastered over your ears, longer than Friday, dripping in your eyes.{/color}"
    "{color=#ff5fb8}And your lips. You lick them, and a shiver goes all the way down your spine and out between your legs.{/color}"
    show boy_pc flushed
    boy_you "\"{i}Ahh{/i}— what— my {i}mouth{/i}—!\""
    "{color=#ff5fb8}They've gone full. Pink and soft and puffy, like you've been kissing somebody all night, and they're sensitive enough that the shower spray on them makes your knees knock. You press a fingertip to your bottom lip, and your mouth just opens round it. On its own. Your tongue curls up under it. You suck.{/color}"
    boy_you "\"{i}Mmh{/i}— That is NOT— that is a {i}violation{/i}—!\""
    "{color=#ff5fb8}You yank the finger out. Your mouth wants it back. It wants something in it, warm and heavy, and it's very clear about the shape. Your thighs squeeze together under the water, silky on silky, and they want something too.{/color}"
    "Your cock's hard against your stomach, leaking into the shower. Nobody even touched it. You just licked your {i}lips{/i}."
    boy_you "\"Bantam is {i}investigating{/i} this.\""
    "You announce it to the tiles, very loudly."
    hide cg onlayer cgl
    $ boy.fit = "own"
    "You get dressed. Your jeans go on over your new hips and sit lower, and they pull across the back in a way they never did. You go to work at the key kiosk and cut keys all day with your lips buzzing, and customer after customer asks if you've had something done."
    boy_you "\"Yes. An {i}outrage{/i}.\""
    "They don't come back.\n{size=-5}{color=#ff8fa3}▸ The evening shift{/color}{/size}"
    $ vn_until(19)
    jump boy_bar

label boy_bar:
    $ vn_enter(bg="boy_bar", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "You swipe the gold card in the lift, and the next button up comes on."
    show screen boy_lift(2)
    vn_sfx "{i}Ding.{/i}"
    hide screen boy_lift
    "The doors open on the bar. It runs the whole length of the floor: a long brass bar top, polished so bright you can see your face in it, mirrored shelves of bottles going up to the ceiling, green-shaded lamps, deep red booths along the far wall full of punters laughing too loud. It smells of oranges and money."
    $ boy.fit = "k2"
    "The kit's in a staff cupboard behind the bar. A black waistcoat, cropped above your belly button, with nothing at all to go under it. Gold hot pants, shiny as a sweet wrapper, that cling to every bit of your new arse. The choker stays on."
    boy_you "\"This is a {i}dress-code violation{/i}.\""
    "You whisper it. It isn't. It's the kit. You hate it. You turn to check the back in the cupboard mirror, and turn again, and stop yourself."
    $ boy.mask = "hotpants"
    "The mask won't go in your boots now, because you're not in your boots much. You fold it flat, and tuck it down the back of the hot pants, flat against the base of your spine. Undetectable. If anybody pats you down, you'll just have to not let them."
    "By the staff door there's a gold dish. Gold capsules. The neat gold card: {i}Staff vitamins.{/i} You take one. For your cover. Honey, at the back of your throat."
    show boy_soren grin at vn_cast_slot
    boy_soren "\"There he is. The new one.\""
    "The barman's leaning on the brass at the far end, sleeves rolled to the elbow, a cocktail shaker in one hand that never stops going. Lean and blond and very pleased with himself, with a smile like he's already seen you naked and enjoyed it."
    boy_soren "\"Soren. I keep the bar. You're my new pair of hands, gorgeous. Lovely pair of hands. Lovely everything.\""
    "He looks you up and down, waistcoat to hot pants and back."
    boy_you "\"I am here to {i}work{/i}, citizen.\""
    boy_soren "\"Course you are. Like this. Wrists loose. Hips into it.\""
    show cg boy_shaker onlayer cgl
    "He comes up behind you, and puts the shaker in your hands, and puts his hands over yours. His chest is warm against your bare back where the waistcoat doesn't reach."
    vn_sfx "{i}Chk-chk-chk. Chk-chk-chk.{/i}"
    "His hands move yours. His hips move yours. The ice rattles. You can feel his breath on your ear."
    boy_soren "\"That's it, gorgeous. Natural.\""
    boy_you "\"I am {i}not{/i} natural. I'm— adequate.\""
    "You tell the shaker. Your voice goes up at the end. Your lips are buzzing again."
    boy_soren "\"You're lovely.\""
    "And he lets go, and pats your arse on the way past, right on the folded mask, and doesn't seem to notice it at all.\n{size=-5}{color=#ff8fa3}▸ Wednesday{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(boy_to_weekday(3, 21))
    jump boy_barback

label boy_barback:
    $ boy.fit = "k2"
    $ vn_enter(bg="boy_cellar", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "Wednesday night, and the bar's heaving."
    "You've learnt the bar. You can do a negroni, an old fashioned and a thing with egg white that Soren calls a {i}sour{/i} and you call evidence. You've worked out that the VIPs never come down here and that the punters always go up, and that nobody, not once, has said the word {i}missing{/i}."
    hide cg onlayer cgl  # ff 2:24 am: no picture, scaffolder failed 4 draws (SCENES.md boytoy v4)
    "You go to the back for ice, and there's the barback."
    "He's hauling a crate of mixers off a trolley. Gold hot pants like yours. No waistcoat at all. Clean-shaven, pink-cheeked, every bit of him hairless and smooth and gleaming under the cellar light, his hair grown out soft and shiny, his face gone so pretty you nearly walk past him."
    "You don't walk past him. You know that face. It's on your corkboard. The hi-vis is gone and the grin's the same."
    "It's the scaffolder."
    boy_you "\"{i}You{/i}. Listen to me very carefully, citizen. Don't look round. Don't make a sound. I'm {i}undercover{/i}. I'm here to get you {i}out{/i}.\""
    "You hiss it. You grab his arm and drag him behind the stack of crates. You tap the choker."
    "The scaffolder looks at you. He looks at your waistcoat, and your gold hot pants, and your new hips, and your lips. He beams. He's got a lovely smile now. Pink lip gloss."
    "The scaffolder" "\"Out? Oh, no, love. I've never been happier.\""
    boy_you "\"You— your {i}firm{/i} has filed paperwork—\""
    "The scaffolder" "\"Have they? Aw. You want ice?\""
    "He pats your cheek. His hands are soft as yours."
    boy_you "\"I— {i}what{/i}?\""
    "The scaffolder" "\"Ice. You came back for ice. It's lovely ice. Soren likes it crushed.\""
    "He holds up a gold bucket of it, helpfully."
    "You take the ice. You don't know what else to do. You stand there holding a bucket of crushed ice, in gold hot pants, behind a stack of tonic water, while the man you came to rescue bends over the trolley in front of you with his smooth round arse in the air, humming."
    "The scaffolder" "\"See you at last orders.\""
    "And he winks, and sashays off up the cellar steps with a crate on his hip."
    "You look down at the bucket. You've squeezed it so hard the ice is melting.\n{size=-5}{color=#ff8fa3}▸ Friday, last orders{/color}{/size}"
    hide cg onlayer cgl
    $ vn_pass(boy_to_weekday(5, 23))
    jump boy_last_orders

## Rung 2, the scuffle and behind the bar: the move caught and turned into a slide down the brass;
## on his knees, Soren's hand in his curls. Non-con, no flip, every protest muffled round him.
label boy_last_orders:
    $ boy.fit = "k2"
    $ vn_enter(bg="boy_bar", pc="heroic", pc_tag="boy_pc", cast=[("boy_soren", "grin")], cg=None)
    boy_soren "\"Last orders, gorgeous!\""
    "Soren sings it down the bar, and a cheer goes up from the booths, and the punters crowd the brass."
    "He's serving. He's laughing. He's shaking two things at once. And in the top pocket of his waistcoat, where he tucked it at the start of the shift, there's a gold key card, and the edge of it is glinting at you under the green lamp like a dare."
    "You've watched him all week. You know his rhythm. Pour, shake, turn, take the money. When he turns, the pocket's clear."
    "You put down the cloth. You roll your shoulders. You feel the folded mask at the base of your spine, flat under the gold hot pants, like a promise."
    boy_you "{b}\"Citizen. Bantam doesn't lose.\"{/b}"
    "Quietly, to the back of his head. Soren doesn't turn round. He just grins at the mirror."
    menu:
        "Soren grins at the mirror."
        "Vault the bar":
            "You go over the bar. Two hands on the brass and a clean vault, legs together, the way you go over railings on the seafront, straight at him from the punters' side—"
            "He catches your ankle."
            "One hand, mid-air, without even looking. He doesn't hold it, he just {i}turns{/i} it, and your vault isn't a vault any more. It's a slide."
        "Go for his waistcoat pocket":
            "You go for the pocket. Fast, across the brass, two fingers out, the way you lift a wallet back off a pickpocket—"
            "He catches your wrist."
            "One hand, without even looking. He doesn't hold it, he just {i}tugs{/i}, gently, and you're already leaning, and the brass is already polished, and your lunge isn't a lunge any more. It's a slide."
    hide boy_soren
    show cg boy_slide onlayer cgl
    vn_sfx "{i}Fwiiip.{/i}" with vnfx("shake")
    "You go down the length of the bar top on your own momentum, belly on the polished brass, past a row of drinks that Soren lifts out of your way one by one without spilling a drop, and off the end, and down, behind the bar, out of sight of every punter in the place, and land on your knees on the rubber mat with a soft {i}whump{/i}."
    "Soren's hand is already in your curls."
    show boy_soren grin at vn_cast_slot
    boy_soren "{b}\"Pay the floor.\"{/b} \"Sorry, love. Two negronis?\""
    "He says it pleasantly, over the top of your head, and turns to a punter."
    show cg boy_behind_bar onlayer cgl
    "You're on your knees behind the bar. Nobody can see you. Right in front of your face, Soren's black trousers, and his other hand on his flies, and the zip going down."
    "His cock comes out right in front of your face. Long and smooth and already hard, curving up, the tip shiny."
    show boy_pc outraged
    boy_you "\"Listen to me. I am a law-abiding {i}citizen{/i}, and I am—\""
    "You look at it. You draw yourself up on your knees, very dignified, behind a bar, and inform it."
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Look at those lips. Fuller every week.\""
    "Fondly, looking down. His thumb brushes your bottom lip, and your mouth opens on its own."
    "And he feeds it in.\n{size=-5}{color=#ff8fa3}▸ Mmph{/color}{/size}"
    jump boy_last_orders_sex

label boy_last_orders_after:
    $ vn_enter(bg="boy_bar", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_bar_swallow")
    vn_sfx "{i}Ding-ding-ding.{/i}"
    "Over your head, the bell goes for time. The punters groan."
    boy_other "\"Last one, gorgeous?\""
    "A woman's voice, asking the bar."
    show boy_soren grin at vn_cast_slot
    boy_soren "\"For you, always.\""
    "Soren's hips roll forward, slow, and his cock slides right to the back of your throat, and his hand in your curls holds you there. {i}Chk-chk-chk{/i}, over your head. The pour. The ice."
    boy_you "\"{i}Mmph{/i}— {i}mmmh{/i}— law— {i}abiding{/i}—\""
    show cg boy_bar_swallow onlayer cgl
    "He slides the last cocktail across the bar, and you swallow." with vnfx("flash")
    "You don't have a choice. He comes right as the glass leaves his hand, deep in your mouth, hot and thick and salty, pulse after pulse of it flooding over your tongue, and his fingers tighten in your curls, and you swallow, and swallow, and swallow, with your eyes screwed shut and your nose in his belly."
    boy_you "\"{i}Mmph{/i}— {i}glk{/i}— you're— {i}mmh{/i}— you're NICKED—\""
    "It comes out round his cock, wet, muffled, and very, very heroic."
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Thanks, gorgeous.\""
    "He tells the woman, and takes her money."
    "In the gold hot pants your own cock is straining so hard against the shiny fabric it's left a dark wet patch on the front, and nobody's touched it, and nobody's going to. It throbs when he pulls out of your mouth, slow, and wipes the tip on your bottom lip."
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Look at those lips.\""
    "Again, softly, and he tucks something flat and gold under the brass tag of your choker."
    hide cg onlayer cgl
    "You stay on your knees behind the bar for a long time after the lights come up, licking your lips. Every time you lick them you taste him, and every time you taste him you lick them again."
    "The scaffolder" "\"There you go, love.\""
    "He sweeps past with a broom and drops you a bag of crushed ice, for your knees."
    "You have the key card. You beat him, technically. You go home with it warm against your throat, and you don't take the choker off, and you don't take the hot pants off either, until morning.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ vn_pass(boy_to_weekday(1, 9))
    jump boy_bedsit_three

## ---- WEEK 3, the dressing room (Boytoy Bedsit Three, Dressing Room, Fitting, Dressing Table) -

label boy_bedsit_three:
    $ boy.fit = "nude"
    $ vn_enter(bg="boy_bedsit", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_three_wake")
    $ boy_body(3)
    show cg boy_three_wake onlayer cgl
    "{color=#ff5fb8}You wake up face down on the camp bed with your arse in the air.{/color}"
    "{color=#ff5fb8}Not on purpose. It just {i}is{/i} in the air, because there's more of it. You reach back, half asleep, and your hand fills up with soft round cheek, warm and heavy and wobbling, and you squeeze before you know you've done it.{/color}"
    boy_you "\"{i}Hnn{/i}—! What— what is {i}this{/i}—!\""
    "Your whole back arches."
    "{color=#ff5fb8}You roll over, and you roll over {i}differently{/i}. Your hips have flared out, properly, a real curve from your waist down, and your arse has gone round, a soft bubble that pushes you up off the mattress when you lie on it. Your thighs touch all the way up now, smooth and soft and pressed together, and when you rub them they slide like satin and your hole clenches on nothing.{/color}"
    boy_you "\"Stop that. Stop— {i}ahh{/i}— {i}clenching{/i}— that's an ORDER—!\""
    "{color=#ff5fb8}It doesn't stop. It clenches again, harder, and something deep inside you {i}throbs{/i}, and you grab the edge of the camp bed. It wants something. It's very clear what. It wants something in it, and it's never wanted anything in it in your life.{/color}"
    hide cg onlayer cgl
    "{color=#ff5fb8}You stumble up and the floor's warm and you stand in front of the window. Your curls hang to your jaw now, soft, framing a face that's gone— {i}pretty{/i}. There's no other word. Your cheekbones, your full pink lips, your dark eyes, softer, like somebody drew you again in a nicer pen.{/color}"
    boy_you "\"This is a {i}disgrace{/i}. Oh, {i}no{/i}.\""
    "{color=#ff5fb8}You tell the window, and your voice comes out light. Not high. Light. Like a nice voice.{/color}"
    "Your mouth's watering. You keep swallowing. You can still taste Friday on your tongue, and it makes your lips tingle so hard you have to press them together."
    "{color=#ff5fb8}And in your pants your cock's hard, and it's— a notch smaller. You stare at it. Definitely smaller. Hard, and leaking, and smaller than it was hard on Friday, and when you poke it, it twitches, and your arse clenches with it.{/color}"
    boy_you "\"I am NOT having that. I am filing a COMPLAINT.\""
    show screen boy_lift(3)
    "You sit down on the camp bed, which takes a moment now, and get your phone out. CASE FILE. The button."
    boy_you "{b}\"Bantam, field report.\"{/b} \"The barman put his hand in my—\""
    "You stop."
    "You look at the phone for a long time. Then you delete it. Then you hold the button down again, and look straight at the corkboard, and say it properly."
    boy_you "\"Floor one: cleared.\""
    hide screen boy_lift
    "You save that one."
    $ boy.fit = "own"
    "Getting dressed is a fight. Your jeans won't go over your arse, so you wear the gold hot pants, because they stretch. On the stairs down past the dryers they ride up, every step, right up into the crack, and the launderette lady watches you go past the frosted glass and raises her eyebrows."
    boy_you "\"Morning.\""
    "In your light new voice, and you go very red.\n{size=-5}{color=#ff8fa3}▸ The evening shift{/color}{/size}"
    $ vn_until(19)
    jump boy_dressing_room

label boy_dressing_room:
    $ boy.fit = "k2"
    $ vn_enter(bg="boy_dressing", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "The gold card. The panel. Another button comes on."
    show screen boy_lift(3)
    vn_sfx "{i}Ding.{/i}"
    hide screen boy_lift
    "The doors open on feathers."
    "The dressing room is the whole floor, and it's full: rails and rails of costumes, sequins and satin and leather and lace, feather boas hanging off every hook like sleeping birds of paradise. All along one wall there's a long dressing table under a row of mirrors framed in round bulbs, every bulb lit, and on the table a landslide of powder pots and brushes and lipsticks and pots of cold cream. In the corner a sewing machine rattles away on its own like it's late for something."
    show boy_cordelia brisk at vn_cast_slot
    "Behind it, a woman with a sharp black bob and red, red lipstick, and a mouthful of pins."
    boy_cordelia "\"Mmf. There you are. Soren's gorgeous. Gideon's smooth one. Cordelia. I dress the acts. Arms out.\""
    "She takes the pins out one at a time, and stabs them into the pincushion on her wrist."
    boy_you "\"I'd rather not, madam.\""
    boy_cordelia "\"Darling, nobody in this building would rather not. Arms out. Oh, there's going to be {i}so{/i} much to do with that.\""
    "She looks you up and down, waistcoat to hot pants to boots, and her eyes stop at your arse and light up."
    "By the door, a gold dish, gold capsules, and the card. {i}Staff vitamins.{/i} You take one. For your cover. Honey."
    "All week you're her runner. You carry feathers up to the stage and sequins down to the bar. You hold the end of things while she pins them. You sweep up sequins. And every time she holds something up against you, a corset, a basque, a sheer slip, you step back with your hands up."
    boy_you "\"Absolutely not, madam. I'm staff.\""
    boy_cordelia "\"Everybody's staff, darling. You'll come round.\""
    "She pins something to a mannequin instead, humming."
    boy_you "\"I will NOT come round.\""
    boy_cordelia "\"Breathe in.\""
    "To the mannequin, and laces it, {i}zzip{/i}, so fast you don't see her hands move.\n{size=-5}{color=#ff8fa3}▸ Wednesday{/color}{/size}"
    $ vn_pass(boy_to_weekday(3, 21))
    jump boy_fitting

label boy_fitting:
    $ boy.fit = "k2"
    $ vn_enter(bg="boy_dressing", pc="heroic", pc_tag="boy_pc", cast=[("boy_cordelia", "brisk")], cg=None)
    "Wednesday. Cordelia catches you at the end of the shift with a tape round her neck and a pencil behind her ear."
    boy_cordelia "\"Fitting. Friday's kit. Arms up, darling.\""
    boy_you "\"I'm not wearing—\""
    boy_cordelia "\"Arms {i}up{/i}, darling.\""
    "Your arms go up. You don't know why. It's the voice. She's got the waistcoat off you before you've finished deciding to keep it on, and her hands go round your waist, brisk, warm, all business, and down over your hips, and round the back, to the waistband of the gold hot pants."
    "Her fingers stop."
    hide boy_cordelia
    show cg boy_mask_found onlayer cgl
    "She draws it out from the base of your spine, slow, between two fingers, and unfolds it, and holds it up to the bulbs round the mirror. Black. Domino. Two eye holes. Neat stitches all round the edge, by hand, in thread you bought at the market, done one night on the camp bed with the telly on."
    "You stand there in your gold hot pants with your arms in the air and your heart going like a drum."
    "Cordelia turns the mask over. She runs her thumb along the stitching."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "{b}\"Hand-sewn? Lovely work, darling.\"{/b}"
    "And that's all she says. She doesn't ask. She doesn't look at you. She just folds it up again, neat, and turns to the dressing table, where Friday's kit is laid out on a velvet cloth: a black corset with gold lacing, black stockings and suspenders, black lace knickers, a pair of black heels. She picks up the left stocking, slides the mask under the top of the garter, smooths it flat, and lays the stocking back down."
    $ boy.mask = "garter"
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Friday. Off you go.\""
    hide cg onlayer cgl
    "You go. You go down in the lift with your arms still half up and nothing on above the hot pants, and you don't remember to put them down till you're on the docks.\n{size=-5}{color=#ff8fa3}▸ Friday night{/color}{/size}"
    $ vn_pass(boy_to_weekday(5, 23))
    jump boy_dressing_table

## Rung 3, MANDATORY: the scuffle (the waistband caught and the corset laced on before he's finished
## turning), then bent over the dressing table in the corset: his first anal. Non-con, no flip: no on
## every thrust, squeezed out of him by the corset; he comes from it.
label boy_dressing_table:
    $ boy.fit = "k2"
    $ vn_enter(bg="boy_dressing", pc="heroic", pc_tag="boy_pc", cast=[("boy_cordelia", "delighted")], cg=None)
    "Friday night, late, and the dressing room's empty but for the two of you. The acts are all on. The bulbs round the mirror are blazing. Cordelia's waiting by the dressing table with the velvet cloth, and the corset, and the stockings, and the mask tucked flat in the left garter where she put it."
    boy_cordelia "\"Kit, darling.\""
    boy_you "\"Absolutely not, citizen.\""
    boy_cordelia "\"Citizen?\""
    "She raises one perfect eyebrow."
    "You plant your boots. You bring your fists up. You've had enough: enough capsules, enough feathers, enough of your own arse following you round every room you walk into. The key card for the next floor is on a ribbon round her wrist with the pincushion. You've seen it all week."
    boy_you "{b}\"Madam. Bantam doesn't lose.\"{/b}"
    "Cordelia smiles. It's a very red smile."
    boy_cordelia "\"Oh, I {i}like{/i} that. Say it again in the corset.\""
    menu:
        "\"Say it again in the corset.\""
        "Bolt for the lift":
            "You bolt for the lift. You're fast, you're the fastest thing on the rooftops, and the doors are right there—"
        "Absolutely not, citizen":
            boy_you "\"I said absolutely NOT.\""
            "And you turn on your heel to march out with dignity, very fast—"
    hide boy_cordelia
    "She catches the waistband of your hot pants."
    show cg boy_corset_laced onlayer cgl
    "Two fingers, hooked in the back. She doesn't pull. She just {i}turns{/i}, and you're already going, so you go round, a full spin on your own heel, and by the time you've come back to face her something stiff and black is round your waist and her hands are at the back of it."
    vn_sfx "{i}Zzzip.{/i}" with vnfx("shake")
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Breathe in.\""
    "You breathe in. You don't decide to. The laces go tight, {i}tight{/i}, up your back in one long pull, and your waist goes in under the corset and your hips push out under it, and the breath comes out of you in a squeak."
    show boy_pc outraged
    boy_you "\"{i}Hhn{/i}— that is— that is an {i}assault{/i} on— on the {i}tailoring{/i}—\""
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"It's a lovely fit.\""
    $ boy.fit = "k3"
    "It's a flurry after that. Her hands are everywhere, brisk as a quick-change in the wings. The hot pants are gone. Lace knickers up your legs. Stockings, rolled up your smooth thighs and clipped to the suspenders, and the left one with the mask lying flat under the garter, warm against your skin. Your boots off and black heels on, and you wobble. A twist of her wrist, and her own red lipstick, quick and expert, on your mouth."
    "Then a hand, flat on your back, between the corset's laces."
    show cg boy_dressing_bent onlayer cgl
    "And you're bent over the dressing table."
    "Powder pots. Brushes. Your hands flat in a spill of loose powder. The row of bulbs blazing in your face, and in the mirror under them, red lips and dark curls and a black corset, and you look away so fast your neck clicks."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "{b}\"Pay the floor.\"{/b}"
    "She sounds delighted. Behind you, her skirt rustles. Something heavy and hot lays itself across your arse, over the lace, and you know exactly what it is, because it's {i}big{/i}, it's so big you can feel the weight of it from your tailbone down."
    boy_you "\"Madam—\""
    "Her fingers hook the lace knickers and pull them aside, and your own cock flops out of them, hard, because it doesn't fit in them, it never did. It bobs against the edge of the table and drips on a powder pot."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Oh, look at that.\""
    "Warmly, and she doesn't touch it."
    "A lid unscrews. Cold cream. Two fingers, cool and slick, between your cheeks, and right on your hole, and in."
    boy_you "\"{i}Ahh{/i}— no— NO— that is not— nobody has EVER—\""
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"There's that bum coming in.\""
    "Delighted, and she spreads you with her thumbs, and works the cream in, round and round, and your hole opens round her like it's been waiting all week."
    "Her fingers go. Something fat and slick and hot presses there instead."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Hands flat, darling.\""
    "And she pushes in.\n{size=-5}{color=#ff8fa3}▸ No{/color}{/size}" with vnfx("shake")
    jump boy_dressing_table_sex

label boy_dressing_table_after:
    $ vn_enter(bg="boy_dressing", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_dressing_cum")
    hide cg onlayer cgl  # ff 2:18 am: no picture, dressing-peak failed 4 draws (SCENES.md boytoy v4)
    boy_you "\"No— {i}hah{/i}— no— Cordelia— {i}ahh{/i}—\""
    "It's so big. It's so {i}full{/i}. She's all the way in, her hips flat to your arse, and the corset squeezes every breath out of you in a burst, and every burst is a no and a moan at once. Her hands are on your waist, on the laces, and she's fucking you into the dressing table, slow and deep and delighted, and the whole table shakes."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Listen to you, darling! The whole floor can hear you!\""
    boy_you "\"No— NO— {i}ahh{/i}— no—\""
    "Your small cock bobs out of the lace on every thrust, bouncing against the edge of the table, dribbling on the powder pots. Nobody's touching it. Nobody's been anywhere near it. She's just fucking your arse, and it's bouncing, and it's getting harder, and something deep inside you that she keeps rubbing on every stroke is going hot and tight and—"
    boy_you "\"No— no— I'm— {i}NO{/i}—\""
    show cg boy_dressing_cum onlayer cgl
    "The powder pots rattle, and you come."
    boy_you "\"{i}NO{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "From your arse. Only from your arse. It squeezes round her in long hard pulses, and your small cock just goes, spurting out of the lace all over the powder pots and the brushes and your own stockinged thigh, in thin hot ropes, while your heels skid on the floor and the corset creaks and you scream no at the bulbs."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"{i}Oh{/i}, darling.\""
    "And she drives in deep, and holds, and comes. Hot and thick and so much of it you can feel it fill you, pulse after pulse, deep inside you, your first time there."
    boy_you "\"No. No— {i}no{/i}—\""
    "You pant it, into the powder."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Breathe in.\""
    "Softly, and you do, and the corset creaks again. She doesn't pull out yet. She stays right there, all the way in, and reaches round, and taps the brass tag on your choker, and tucks the key card under it."
    hide cg onlayer cgl
    "When she does pull out, slow, it all comes with her, warm down the backs of your stocking tops. She smooths your curls. She fixes your lipstick with her thumb. She leaves the corset on."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Keep the kit on, darling. It's yours this week.\""
    "You walk home along the docks in your coat with the corset on under it, and the stockings, and the mask in the garter, and the knickers stuck to you, clenching on every step on nothing at all.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ vn_pass(boy_to_weekday(1, 9))
    jump boy_bedsit_four

## ---- WEEK 4, the stage (Boytoy Bedsit Four, Stage, Chorus Line, Spotlight) -----------------

label boy_bedsit_four:
    $ boy.fit = "k3"
    $ vn_enter(bg="boy_bedsit", pc="flushed", pc_tag="boy_pc", cast=[], cg=None)
    "You never took them off."
    "The corset. The stockings. The lace knickers. You walked home in them under your coat on Friday night, and you slept in them, and you lay on the camp bed all Saturday in them with the dryers rumbling under the floor, and you don't have a reason. You just didn't take them off."
    $ boy_body(4)
    show cg boy_four_wake onlayer cgl
    "{color=#ff5fb8}And now they don't fit the same.{/color}"
    "{color=#ff5fb8}You sit up and the corset creaks, because there's more of you under it. Your hips have gone {i}wide{/i}, really wide, curving out under the black lace so far the suspenders stand off them. And behind you, your arse: round, proper round, a big soft bubble butt that the lace knickers have given up on entirely, and when you shift on the camp bed it {i}wobbles{/i}, and you feel it wobble all the way up your spine.{/color}"
    boy_you "\"{i}Oh{/i}— oh, that's— that is NOT regulation—!\""
    "{color=#ff5fb8}You squeeze one cheek, to check. Your hole clenches so hard you gasp. It's been doing that all weekend, clenching on nothing, wanting what it had on Friday, and now it knows exactly how to want it, every muscle of it, like it practised.{/color}"
    "{color=#ff5fb8}Your thighs are soft. Not smooth now: {i}soft{/i}, plump at the tops of the stockings and pressed together all the way, and when you rub them it goes straight to your arse.{/color}"
    "{color=#ff5fb8}And your nipples. The corset's edge sits right under them, and they're puffy, swollen up pink and tender and sticking out, and every breath rubs them on the top of the boning.{/color}"
    boy_you "\"{i}Hnn{/i}— {i}ahh{/i}— stop— {i}stop{/i} catching on things—!\""
    "{color=#ff5fb8}They don't stop. You brush one with your thumb and moan out loud at the corkboard. Your dark curls are on your shoulders. They tickle. Your voice, when you yell at your nipples, comes out light and sweet, and you clap a hand over your mouth.{/color}"
    hide cg onlayer cgl
    show screen boy_lift(4)
    "You get your phone. CASE FILE. You hold down the button, and for some reason you whisper."
    boy_you "{b}\"{i}Bantam, field report.{/i}\"{/b} \"{i}The stockings are... they're very good stockings. They're the good kind. With the seam. And they don't fall down, because of the— the suspenders, which clip on, at the front and the back, and they pull a bit when you walk, which is... which is fine. Which is all fine. They're very well made.{/i}\""
    hide screen boy_lift
    "You stop. That's the whole report. You don't delete it."
    $ boy.fit = "own"
    "You put your jeans on over the stockings, which takes ages and doesn't work, so you wear your coat over the lot and go to work at the key kiosk with the suspenders pulling at every step.\n{size=-5}{color=#ff8fa3}▸ The evening shift{/color}{/size}"
    $ vn_until(19)
    jump boy_stage

label boy_stage:
    $ boy.fit = "k4"
    $ vn_enter(bg="boy_stage", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_leotard")
    show cg boy_leotard onlayer cgl
    "Cordelia meets you at the lift with a gold leotard over her arm and doesn't even ask about the stockings. She just nods at them, pleased, and helps you out of the corset."
    "The leotard's gold, and sheer, so sheer it's more of a shine than a fabric, and it's cut so high on the hip it goes up to your waist. There's a gold feather tail that clips on at the back and sticks up over your new arse like a peacock. Gold heels, high. Your own black stockings, with the mask in the garter, because you never took them off. Red lipstick, her thumb, quick."
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Breathe in. Oh, you don't need to any more, do you.\""
    "Out of habit, and she kisses you on the cheek and goes."
    hide cg onlayer cgl
    show screen boy_lift(4)
    vn_sfx "{i}Ding.{/i}"
    hide screen boy_lift
    "The doors open on the club. It's a big dark room full of round tables, each with its own lamp and its own bottle of something, and every table faces the same way: the stage. A real stage, with red curtains and a spotlight, and in the middle of it, all on its own, a big gilded chair with velvet arms, like a throne for a very camp king."
    "By the stage door, a gold dish. The card: {i}Staff vitamins.{/i} A capsule. Honey."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"The new one! Look at you! {i}Look{/i} at you!\""
    "A man in a gold tailcoat and a top hat comes striding out of the wings, a radio microphone clipped to his lapel, a showman's grin on his face. He takes both your hands and holds them out and turns you round, once, in your heels and your tail, like he's showing you off to an audience that isn't there yet."
    boy_caspian "\"Caspian. I keep the stage. And you, darling, are my headline act on Friday.\""
    boy_you "\"I am {i}staff{/i}. I'm here to— I'm on the chorus line.\""
    boy_caspian "\"Oh, you're on the chorus line this week. Everybody's on the chorus line. Friday, you're on {i}that{/i}.\""
    "He points at the gilded chair. The spotlight seems to point at it too."
    "So all week you rehearse with the chorus line. Kicks, turns, a shimmy that you refuse to do and then do, {i}clack-clack-clack{/i} across the boards in your gold heels, your feather tail bobbing, your arse bouncing so hard in the leotard you can feel the whole chorus line watching it."
    "Caspian watches from the wings with his arms folded, grinning. Every time you look over at the gilded chair, it's still there.\n{size=-5}{color=#ff8fa3}▸ Wednesday{/color}{/size}"
    $ vn_pass(boy_to_weekday(3, 21))
    jump boy_chorus_line

label boy_chorus_line:
    $ boy.fit = "k4"
    $ vn_enter(bg="boy_stage", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_chorus")
    "Wednesday's dress rehearsal, and the chorus line's in full kit for the first time: a row of gold leotards and feather tails under the lights, heels clacking on the beat."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"And KICK. And KICK. Lovely. And KICK—\""
    "From the wings. You kick. Somebody further down the line kicks higher. Much higher, straight up past their own ear, perfect, toes pointed, and the whole line goes {i}ooh{/i}."
    show cg boy_chorus onlayer cgl
    "You look down the line."
    "Smooth legs, no hair on them anywhere. A gold leotard on a pretty, soft, broad-shouldered body, a tail of white feathers, a face made up beautifully. And a nose that's been broken, and set, and broken again, and a big gap-toothed grin."
    "It's the prop forward. Off your corkboard. MISSING. Last seen: the docks."
    "He catches you staring, mid-kick, leg straight up in the air, and {i}waves{/i}. A finger-wave, delighted, with his leg still up by his ear."
    boy_you "\"I'm here to {i}rescue{/i} you.\""
    "You mouth it, across the line."
    "\"What?\" he mouths back, cheerful, and comes down out of the kick and goes straight into a turn, and he's beautiful at it. He's better than anybody. He was always going to be better than anybody at something, and it turns out it was this."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"And KICK!\""
    "The prop forward kicks. It's the highest kick you've ever seen. The chorus line applauds him, and he blows them a kiss."
    hide cg onlayer cgl
    "After rehearsal you catch him by the stage door. He's fixing his lipstick in a compact."
    boy_you "\"Your club's been looking for you. The whole {i}team{/i}—\""
    "You hiss it."
    "The prop forward" "\"Bless them. I'll send them tickets. Friday? Oh, you're the {i}headline{/i}. Break a leg, love.\""
    "He snaps the compact shut. He looks at you, and at the gilded chair on the stage behind you, and grins his gap-toothed grin.\n{size=-5}{color=#ff8fa3}▸ Friday night{/color}{/size}"
    $ vn_pass(boy_to_weekday(5, 22))
    jump boy_spotlight

## Rung 4: the scuffle turned into a dance dip; Caspian puts the mask on him for the act; his lap in
## the gilded chair, facing the club, in the spotlight. Non-con, no flip: no into the microphone,
## moaned, and he comes untouched.
label boy_spotlight:
    $ boy.fit = "k4"
    $ vn_enter(bg="boy_stage", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_spotlight_on")
    "Friday night, and the club's packed."
    "Every table's full. Every lamp's lit. People are standing at the back, and leaning on the bar, and sitting on each other. The chorus line's just finished and gone off to whistles, and now there's a drum roll, and the curtains open, and the spotlight comes on."
    show cg boy_spotlight_on onlayer cgl
    "On you." with vnfx("flash")
    "You're stood in the middle of the stage in your sheer gold leotard and your feather tail and your black stockings, next to the gilded chair, with the light so bright you can't see a single face, only the shine of the lamps and a lot of eyes."
    "The room goes quiet. Somebody whistles."
    "And Caspian strides on from the wings, top hat, gold tailcoat, the microphone in his hand, grinning like the cat that got the cream and the cow."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Ladies and gentlemen!\""
    "He's got the key card in his top hat's band. You can see it glint. This is it. You've had enough. A whole week of kicks and clacks and this ridiculous tail, and this man, this {i}villain{/i}, with his microphone, and the club full of punters who think this is a show."
    "You plant your heels on the boards. You bring your fists up. You drop into your stance, in the leotard, in front of everyone."
    boy_you "{b}\"Ladies and gentlemen. Bantam doesn't lose.\"{/b}"
    "As loud as you can, to the room. A pause. Then the club starts to clap. Slow, and then fast, and somebody cheers."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Oh, they {i}love{/i} you.\""
    menu:
        "\"Oh, they {i}love{/i} you.\""
        "Go for the sweep":
            "You go for the sweep. Low and fast, your best, right at his ankles—"
        "Unmask the villain":
            boy_you "\"Unmask the villain!\""
            "And you go for his top hat, quick as anything—"
    show cg boy_dip onlayer cgl
    "Caspian takes your hand."
    "He just takes it, like you offered it, and turns, and suddenly your move is a step, and the step is a turn, and the turn goes all the way round and down into a dip, your back arched over his arm and your heels still on the boards, your feather tail brushing the stage, his grin right above your face."
    "The club {i}erupts{/i}." with vnfx("shake")
    "He brings you up out of the dip and spins you, and spins you again, round and round on your own heels under the light, and stops you dead facing the room with one hand on your waist, and the club's on its feet, clapping the choreography."
    show boy_pc outraged
    boy_you "\"That wasn't— that was a {i}sweep{/i}—\""
    "Caspian's free hand goes down to your thigh. To the top of the left stocking. To the garter. And comes back up with the mask."
    $ boy.mask = "face"
    $ boy.fit = "k4m"
    show cg boy_mask_on onlayer cgl
    "He shakes it out. He holds it up to the light. Black, domino, hand-sewn. And before you can grab it, he puts it on you, over your eyes, and ties it at the back of your curls in one neat bow."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Ladies and gentlemen, the {i}Bantam{/i}!\""
    "He roars it into the microphone. The room goes mad. They're standing on chairs. They think it's the act. They think it's all the act, the stance, the sweep, the mask. A woman at the front is screaming. Somebody throws a flower."
    show cg boy_chair onlayer cgl
    "Caspian sits back in the gilded chair, spreads his knees, and tugs you down by the hips, and you sit, because your knees have gone, right in his lap, facing the room. The spotlight hits you full in the face, in the mask. Your legs fall open either side of his."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "{b}\"Pay the floor.\"{/b}"
    "He says it in your ear, off-mic. His fingers hook the crotch of the gold leotard and pull it aside. You feel the stage air on your bare arse, and his trousers open under you, and his cock, hot and hard, pushing up between your cheeks."
    boy_you "\"No—\""
    "He holds the microphone to your mouth."
    boy_you "\"{i}No{/i}—\""
    "It goes out across the club, through every speaker, and it comes out a moan, and the club {i}whoops{/i}."
    "His hands settle on your hips, and pull you down.\n{size=-5}{color=#ff8fa3}▸ No{/color}{/size}"
    jump boy_spotlight_sex

label boy_spotlight_after:
    $ vn_enter(bg="boy_stage", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_chair_cum")
    show cg boy_chair_peak onlayer cgl
    boy_you "\"No— {i}ahh{/i}— no— {i}NO{/i}—\""
    "Into the microphone, and the club cheers every one."
    "You're bouncing. You can't stop. His hands are just resting on your hips now, and your arse is going up and down on his cock on its own, sinking all the way to his lap and rising, your big round cheeks slapping on his thighs, your feather tail shaking, your heels scrabbling on the boards. Your small cock's bobbing in the sheer gold, tenting it, a wet patch spreading on the shine, and nobody's touching it, and nobody's going to."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Look at those hips, ladies and gentlemen! {i}Bounce{/i} for them!\""
    "You bounce for them."
    boy_you "\"No— no— {i}NOOOhh{/i}—\""
    show cg boy_chair_cum onlayer cgl
    "And it goes. Again. All on its own, from your arse, from his cock hitting that spot inside you on every drop, you come in the spotlight with the mask on and the microphone at your lips, your small cock jerking and spurting all over the front of the gold leotard, and you scream it straight into the mic, and the whole room hears it." with vnfx("flash", "shake")
    "The whole club is on its feet."
    "Caspian pulls you down to the root and holds you there, and comes, deep, his cock throbbing in you, so much of it you can feel it filling you up while the room screams and stamps and throws flowers, and he waves to them over your shoulder with his hat."
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"The {i}Bantam{/i}, ladies and gentlemen!\""
    boy_you "\"No.\""
    "You pant it, into the microphone, very quietly, and the room hears that too, and cheers it like an encore."
    "Caspian tucks a gold key card under the brass tag of your choker, in front of everyone, like a tip."
    hide cg onlayer cgl
    "They do the curtain call with you still in his lap. You don't remember getting off the stage. You remember the prop forward in the wings, blowing you a kiss, and a lot of flowers, and the mask still on your face, which nobody takes off you, and which you don't take off either, all the way home.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ vn_pass(boy_to_weekday(1, 9))
    jump boy_bedsit_five

## ---- WEEK 5, the VIP floor (Boytoy Bedsit Five, VIP Floor, Menu, Booth) --------------------

label boy_bedsit_five:
    $ boy.fit = "nude"
    $ boy.mask = "boot"
    $ vn_enter(bg="boy_bedsit", pc="flushed", pc_tag="boy_pc", cast=[], cg="boy_five_wake")
    "You wake up on your back with the duvet kicked off and the warm air from the dryers rising through the floorboards, and something on your chest is standing up."
    $ boy_body(5)
    show cg boy_five_wake onlayer cgl
    "{color=#ff5fb8}Two somethings.{/color}"
    "{color=#ff5fb8}You look down. Your nipples are standing straight up, pink and stiff in the warm air. And under them, round and soft and new, sitting up on your chest like they've always been there, are breasts. New ones. Perky. Perfect handfuls, high and firm, a proper A cup.{/color}"
    "..."
    "{color=#ff5fb8}You put your hand on one. It's warm. It's soft. It's {i}yours{/i}. You squeeze, and it squeezes back into your palm, and the feeling goes off in your chest like a firework and comes out of your mouth.{/color}"
    boy_you "\"{i}AHH{/i}— oh— oh, NO— that is— {i}hnn{/i}— that's a {i}FELONY{/i}—!\""
    "{color=#ff5fb8}You let go. You grab them again. Both of them. You can't help it. They're so {i}sensitive{/i}, way past the puffy nipples, all of them, every bit, and you roll your thumbs over the tips and arch right up off the camp bed.{/color}"
    boy_you "\"Stop— {i}stop{/i}— oh, that's— why are they so {i}good{/i}—!\""
    "{color=#ff5fb8}Your hair's past your shoulders now, a dark tumble of curls all over the pillow. You're soft all over, everywhere, your belly, your arms, your big round arse sunk into the mattress. You roll over to get up and your arse squeezes, and your hole clenches, deep and hungry, and you have to lie there a moment with your face in the pillow and your hips moving.{/color}"
    "{color=#ff5fb8}And your cock. It's lying on your thigh. Soft. Pink. Leaking a bit at the tip, and it doesn't get hard, not when you squeeze your tits, not when your arse clenches, not even when you moan. It just lies there and dribbles, like it's watching.{/color}"
    boy_you "\"You are a {i}disappointment{/i} to the force.\""
    "Breathless, you tell it."
    hide cg onlayer cgl
    show screen boy_lift(5)
    "You lie there for a long time with your hands on your tits. Then you get your phone. CASE FILE. The button."
    boy_you "{b}\"Bantam, field report.\"{/b} \"Floor three. They clapped.\""
    hide screen boy_lift
    "That's the whole note."
    "You look at the send button. The crime desk at the local paper. The case you were going to hand them, wrapped up with a bow."
    "You don't send it. You put the phone face down on the duvet and look at the ceiling, and your thumb finds your nipple again, all on its own.\n{size=-5}{color=#ff8fa3}▸ The evening shift{/color}{/size}"
    $ boy.fit = "own"
    $ vn_until(19)
    jump boy_vip_floor

label boy_vip_floor:
    $ vn_enter(bg="boy_lift_hall", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_hanger")
    show cg boy_hanger onlayer cgl
    "The kit for the next floor up is waiting in the lift on a gold hanger. A gold micro-bikini top, two triangles and some string. A gold thong, less than that. Gold heels. And a robe of sheer black chiffon that floats when you move and hides nothing at all."
    $ boy.fit = "k5"
    "You put it on. The triangles sit over your new tits and barely cover the nipples. You put the robe on over it, and it doesn't help, and you tie the belt tight, and that doesn't help either."
    show screen boy_card("", ["{i}The mask, please. The guests have paid for it.{/i}"])
    "And then there's a note on the hanger, in gold ink."
    hide screen boy_card
    $ boy.mask = "face"
    "You take it out of your boot. You put it on."
    hide cg onlayer cgl
    show screen boy_lift(5)
    "The gold card. The panel."
    vn_sfx "{i}Ding.{/i}"
    hide screen boy_lift
    $ vn_enter(bg="boy_vip", pc="heroic", pc_tag="boy_pc", cast=[("boy_ulric", "polite")], cg=None)
    "It's quiet up here. That's the first thing. No music, only a low hum of voices behind curtains. A long corridor of private booths, each one closed off with a heavy gold curtain on a brass rail, and through the gaps, glimpses of velvet sofas, candlelight, champagne on ice. It smells of lilies and leather."
    boy_ulric "\"Sir.\""
    "A man in an immaculate dinner jacket is standing at your elbow. You didn't hear him arrive. Neatly trimmed dark beard, perfectly straight bow tie, hands folded behind his back, and a small, perfect, professional smile."
    boy_ulric "\"Ulric. I host the VIP floor. Sir is very welcome. Sir will forgive me if I say that Sir is even lovelier than the poster.\""
    "With a little bow from the neck."
    boy_you "\"There's a {i}poster{/i}?\""
    boy_ulric "\"Sir's table is not yet ready. This week Sir will pour. If Sir would follow me.\""
    "Smoothly, as if you hadn't spoken. By the corridor's end, a gold dish on a marble stand. The card: {i}Staff vitamins.{/i} You take one. Honey. You don't think about it at all any more."
    "Ulric shows you the booths. All of them. He holds back every curtain with one gloved hand and tells you who sits there and what they drink and how they like it poured, and his manners are perfect, and his eyes, every time he holds a curtain back for you to go through first, go down the back of your sheer black robe to your arse, and stay there, and come back up to the mask, perfectly polite."
    boy_ulric "\"Sir pours beautifully. Sir does everything beautifully.\"\n{size=-5}{color=#ff8fa3}▸ Thursday{/color}{/size}"
    "At the end of the night."
    $ vn_pass(boy_to_weekday(4, 21))
    jump boy_menu

label boy_menu:
    $ boy.fit = "k5"
    $ vn_enter(bg="boy_vip", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    "Thursday, and you've been pouring champagne all week into glasses held by hands you never see the faces of, behind curtains, in candlelight. The VIPs say thank you. They say it very warmly. They look at your mask."
    "In a lull, you open the menu."
    "It's a heavy leather folder with a gold birdcage on the cover. Inside: champagne. Oysters. Cigars. A list of wines that cost more than your kiosk. And at the back, on its own page, a heading in gold script: {i}Specials.{/i}"
    show screen boy_card("SPECIALS", ["{i}The Bantam (masked){/i}", "A price, crossed out. A higher one over it, crossed out. A higher one again, squeezed in above, the ink still wet."])
    "Under it, one line. You stare at it."
    hide screen boy_card
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir has been very popular since Tuesday.\""
    "At your shoulder."
    boy_you "\"I am {i}not{/i} on the {i}menu{/i}—\""
    boy_ulric "\"Sir is on page— ah. Sir has been booked.\""
    "Ulric glances down at the folder in your hands, upside down, and reads the line without turning it round. He takes a slim gold pen from his inside pocket. He makes a small, neat note in a little leather book."
    boy_you "\"By WHO?\""
    "Ulric closes the little leather book and puts it away and smiles his small, perfect smile."
    boy_ulric "\"Friday. Sir's table will be ready.\"\n{size=-5}{color=#ff8fa3}▸ Friday night{/color}{/size}"
    $ vn_pass(boy_to_weekday(5, 22))
    jump boy_booth

## Rung 5: the scuffle reversed into a waltz that walks him back onto the sofa; legs up over Ulric's
## shoulders; non-con until halfway, then THE BREAK: "Don't stop. Don't— don't you dare stop—".
label boy_booth:
    $ boy.fit = "k5"
    $ vn_enter(bg="boy_booth", pc="heroic", pc_tag="boy_pc", cast=[("boy_ulric", "polite")], cg=None)
    "Friday night. Ulric meets you at the end of the corridor, in front of the last booth, the biggest, the one with the thickest curtain, and holds it back with one gloved hand."
    boy_ulric "\"Sir's table is ready.\""
    "Inside: candles. A bucket of champagne. A long, deep, curving velvet sofa the colour of red wine. Nobody else."
    boy_you "\"Where's the guest?\""
    boy_ulric "\"Sir is looking at him. I booked Sir myself. I hope Sir doesn't mind. The price was considerable.\""
    "Ulric lets the curtain fall closed behind you both."
    "The key card for the top floor is in his breast pocket. You know it is. You've seen him touch it, all week, like a man checking his wallet. It's the last one. After this there's only the button nobody looks at, and the man nobody names, and whatever's been happening to all of you, and an end to it."
    "You turn round in the candlelight, in your mask and your sheer black robe and your gold heels, and bring your fists up."
    boy_you "{b}\"Citizen. Bantam doesn't lose.\"{/b}"
    "Ulric inclines his head, very politely."
    boy_ulric "\"Of course, Sir.\""
    menu:
        "\"Of course, Sir.\""
        "Armlock":
            "You go for the armlock. It's a good one: his wrist, his elbow, a twist and step, the one that put the bike thief on his knees—"
        "Go for the menu":
            "You lunge past him for the leather menu on the side table, to rip the page out, to destroy the evidence—"
    hide boy_ulric
    show cg boy_waltz onlayer cgl
    "Ulric's hand is on your waist."
    "Very lightly. And his other hand has your hand, and somehow the twist you started is a turn, and the turn is a step, and the step is the next step, and he's walking you backwards across the booth, so gently it's almost a waltz, your heels following his shoes, your robe floating round you both, his eyes on yours through the mask, perfectly polite."
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir dances beautifully.\""
    "The sofa catches the backs of your knees."
    show cg boy_sofa onlayer cgl
    "You sit down. You don't mean to. Your knees just fold, and the velvet takes you, and Ulric's hand on your shoulder lays you back into it, slow, until you're looking up at him and the candlelight on the ceiling."
    show boy_ulric polite at vn_cast_slot
    boy_ulric "{b}\"Pay the floor.\"{/b}"
    "He says it softly. He undoes the belt of your robe with two fingers, and it falls open. He hooks the gold triangles of the bikini top and pushes them up, over your new tits, and they spill out into the candlelight, pink-tipped and perky, nipples standing straight up."
    "Ulric looks at them for a long moment."
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir has the most beautiful breasts on the floor. Perfectly made. A credit to the house.\""
    "He bends, and kisses one nipple, and then the other, slow and courtly, like he's kissing hands at a ball."
    show boy_pc outraged
    boy_you "\"{i}Ahh{/i}— no— citizen, that is— {i}hnn{/i}—\""
    "He takes your ankles, one and then the other, and lays them up over his shoulders. The gold thong goes aside. His trousers are open, and something big and hot and slick rests right against your hole."
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir will tell me if anything is not to Sir's liking.\""
    boy_you "\"{i}No{/i}—\""
    "He slides in. Slow.\n{size=-5}{color=#ff8fa3}▸ No, citizen{/color}{/size}" with vnfx("shake")
    jump boy_booth_sex

label boy_booth_after:
    $ vn_enter(bg="boy_booth", pc="begging", pc_tag="boy_pc", cast=[], cg="boy_sofa_cum")
    show cg boy_sofa_ankles onlayer cgl
    boy_you "\"Deeper— {i}ahh{/i}— {i}deeper{/i}— don't you STOP—\""
    "You haven't said no in ages. You can't remember the last one. Your legs have come down off his shoulders, and your ankles have hooked round him, and now they're dragging him in, and he's letting them."
    "Your ankles lock behind his back."
    boy_you "\"Again— {i}again{/i}— Ulric, AGAIN—\""
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Of course, Sir.\""
    "He gives it to you. Slow and deep and all of it, the velvet creaking under you, your new tits bouncing on every thrust, the candles guttering. Your small cock lies on your belly, soft, leaking in a long string onto your stomach, bouncing every time he bottoms out, and you don't even look at it. You're looking at him. You're begging him, loud, in your light sweet voice, through the mask."
    boy_you "\"Don't stop— don't— don't you {i}dare{/i}— I'm— {i}AHH{/i}—\""
    show cg boy_sofa_cum onlayer cgl
    "It goes off untouched. It just jerks on your belly and spurts, up over your stomach, up over your new tits, hot white drops on your pink nipples, and your arse clamps down on him so hard he stops, for once, mid-stroke, and closes his eyes." with vnfx("flash", "shake")
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"{i}Sir{/i}.\""
    "And he comes. Deep. Hot. Pulse after pulse, buried all the way in you, and you hold him there with your ankles locked behind his back and your heels digging in and moan right through it, every pulse, louder."
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir sings beautifully.\""
    "A touch breathless, which you didn't think he could be."
    boy_you "\"Don't stop.\""
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir would never dream of it.\""
    "He takes a gold key card from his breast pocket, the last one, and tucks it under the brass tag of your choker, and starts again."
    hide cg onlayer cgl
    "The mask stays on all night. Behind the gold curtain, the VIPs outside keep their glasses raised, and the champagne keeps going round, and somewhere above the ceiling, on the top floor, something hums.\n{size=-5}{color=#ff8fa3}▸ Monday{/color}{/size}"
    $ vn_pass(boy_to_weekday(1, 9))
    jump boy_bedsit_six

## ---- WEEK 6, the penthouse (Boytoy Bedsit Six, Penthouse) and THE ENDING ("Keep It") -------

label boy_bedsit_six:
    $ boy.fit = "nude"
    $ boy.mask = "boot"
    $ vn_enter(bg="boy_bedsit", pc="begging", pc_tag="boy_pc", cast=[], cg="boy_six_wake")
    $ boy_body(6)
    show cg boy_six_wake onlayer cgl
    "{color=#ff5fb8}You wake up warm, and soft, and wanting.{/color}"
    "{color=#ff5fb8}It's everywhere. Your hair's down your back, long dark curls spilling over your shoulders and down past your shoulder blades, and when you sit up they slide over your bare skin like a hand. Your tits are full and perky and so sensitive the air moves them. Your hips have gone wide and round, and behind you your arse is the roundest it's ever been, a big soft bubble butt you can feel all the way up your spine, and when you clench, your hole clenches too, deep, and {i}throbs{/i} for it.{/color}"
    boy_you "\"{i}Ahh{/i}—\""
    "{color=#ff5fb8}You run your hands down your body, slowly, all the way: soft tits, soft belly, wide hips, soft hairless thighs pressed together, and back up. Every bit of it answers. You moan at your own touch, out loud, in your light sweet voice, and you don't stop yourself, and you don't tell yourself off.{/color}"
    boy_you "\"Oh— oh, look at me— {i}look{/i} at me—\""
    "{color=#ff5fb8}Your mouth's watering. Your arse is throbbing. Your nipples are standing up so hard the air on them makes you gasp, and you pinch one, and arch, and moan so loud the launderette lady must hear it through the floor.{/color}"
    "{color=#ff5fb8}Down between your thighs your small cock's still there, soft, pink, leaking. It doesn't matter. You know where it all comes from now, and it isn't there.{/color}"
    boy_you "\"Oh, {i}please{/i}. Oh, please, {i}tonight{/i}—\""
    "You tell the ceiling, and you don't know who you mean."
    hide cg onlayer cgl
    show screen boy_lift(6)
    "You don't record anything."
    "You open CASE FILE, and look at it. It's full: notes you recorded and never sent, every Monday since the rooftop, one after another down the screen. You don't play them. You know what they say."
    hide screen boy_lift
    "You put the phone face down on the table, and leave it there, and go to work."
    $ boy.fit = "own"
    "You cut keys all day. You're very good at it. Customers stare at you, and you smile at them in your red lipstick from the night before that you didn't quite get off, and give them their change, and your hair swings down your back."
    "You still have the last key card under the brass tag. It's warm. It's been warm all day.\n{size=-5}{color=#ff8fa3}▸ Up in the lift{/color}{/size}"
    $ vn_until(21)
    jump boy_penthouse

## Rung 6: "Hello, Bantam." Dorian Wexley; the clippings, and the pigeon photo in the middle; "Nobody's
## missing. They just didn't go home." The fists come down; "Keep it, it's yours."; the birdcage
## shuts; "The Cage keeps what walks in." Then he rides him, eager. Consensual.
label boy_penthouse:
    $ boy.fit = "k6m"
    $ boy.mask = "face"
    $ vn_enter(bg="boy_lift_hall", pc="heroic", pc_tag="boy_pc", cast=[], cg=None)
    show screen boy_card("", ["{i}Come as you are. The stockings, if you like. And the mask, please.{/i}"])
    "There's no kit in the lift tonight. Just a note on the gold hanger, in a hand you haven't seen before, warm and looping."
    hide screen boy_card
    "So you come in the gold choker, and your black stockings, and the mask. Nothing else. Cordelia did your lipstick at the lift door, and kissed your cheek, and didn't say anything at all."
    show screen boy_lift(6)
    "You swipe the last gold card."
    vn_sfx "{i}Ding.{/i}"
    hide screen boy_lift
    $ vn_enter(bg="boy_penthouse", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_penthouse_view")
    show cg boy_penthouse_view onlayer cgl
    "The doors open on the sky."
    "The penthouse is all glass. Glass walls all the way round, and through them the whole town at night: the docks, the black water, the cranes, the lights of the high street, the rooftops you've run on, all of it laid out below like a model railway. Thick soft carpet. A big bed, huge and low, with gold sheets. A wall of screens, every one showing a floor of the Cage, carrying on below you: the foyer, the bar, the dressing room, the stage, the booths, all of them busy, all of them gold."
    "And on the sideboard, a gilded birdcage. Empty. Its door standing open."
    hide cg onlayer cgl
    show boy_dorian lazy at vn_cast_slot
    "By the window, with his back to the view and a drink in each hand, a man in shirtsleeves. Lean, dark hair swept back, a beautiful suit with the jacket off, the cuffs rolled. A lazy smile, warm all the way up to his eyes."
    boy_dorian "{b}\"Hello, Bantam.\"{/b}"
    "You know that voice. Warm and unhurried and very amused, through the crackle of an intercom, on your very first night."
    boy_you "\"It was you. On the door.\""
    boy_dorian "\"It was. Dorian Wexley. I own the Cage. I've known it was you since you pressed the buzzer. You stood up so straight.\""
    "He comes over and holds out one of the drinks. You don't take it. He doesn't seem to mind. Then he steps aside, and you see the wall behind him."
    show cg boy_clippings onlayer cgl
    "It's covered in frames. Gold frames, all sizes, floor to ceiling, and in every one, a clipping from the local paper. BANTAM STRIKES AGAIN. MASKED HERO FOILS BIKE THIEF. WHO IS BANTAM? BAGPIPES RECOVERED. Years of them. Every single one you ever cut out and pinned to your own wall, and a lot you never saw. And right in the middle, in the biggest frame, lit by its own little lamp, the photo. The famous one. The blurry one from the pier, the one that was meant to be you mid-leap, that everybody, the paper included, said was a pigeon."
    boy_dorian "\"That's my favourite.\""
    "Fondly."
    hide cg onlayer cgl
    "You bring your fists up. You do it in nothing but stockings and a choker and a mask, in a glass room on top of the town, and your hands are steady."
    boy_you "\"Where are they? The scaffolder. The prop forward. The driver. The men on my wall. Where {i}are{/i} they?\""
    "Dorian looks at you, warm, unhurried. He sips his drink."
    boy_dorian "\"Nobody's missing. They just didn't go home.\""
    "On the screens behind him the scaffolder's laughing behind the bar. The prop forward's kicking in the chorus line. The whole Cage is gold and busy and happy below your feet. And your fists are up, and your arse is throbbing, and your nipples are hard, and you know, the way you've known since the cloakroom, where the case has been going all along."
    menu:
        "Your fists are up."
        "Put your fists down":
            pass
    "You put your fists down."
    "It's the easiest thing you've ever done. They just come down. Dorian watches them go, and smiles."
    hide cg onlayer cgl  # ff 2:18 am: no picture, mask-off failed 4 draws (SCENES.md boytoy v4)
    "You reach up behind your curls, and untie the bow Caspian tied, and take off the mask."
    "It's warm from your face. Black. Domino. Hand-sewn, every stitch, on the camp bed with the telly on, a long time ago. You hold it in both hands for a moment, and look at it."
    "Then you hold it out to him."
    boy_you "{b}\"Keep it, it's yours.\"{/b}"
    show cg boy_birdcage onlayer cgl
    "Dorian puts his drinks down. He takes the mask from you very carefully, with both hands, the way you'd take something that matters. He turns, and walks to the sideboard, and lays it on the floor of the gilded birdcage, flat, smoothing it with one finger."
    $ boy.mask = "birdcage"
    $ boy.fit = "k6"
    "And he shuts the little door. {i}Click.{/i}"
    boy_dorian "{b}\"The Cage keeps what walks in.\"{/b}"
    hide cg onlayer cgl
    "He sits down on the edge of the big bed, in his shirtsleeves, and leans back on his hands, and waits. He doesn't ask. He never has."
    show cg boy_climb_on onlayer cgl
    "You go to him. You climb onto the bed, and into his lap, on your knees, your stockinged thighs either side of his, your tits right in his face, your long hair falling round both of you. You put your hands on his shirt, and undo it, button by button, and then you reach down and undo his trousers, and take his cock out yourself. It's big, and hot, and hard, and you hold it, and look at him."
    boy_you "\"Hello, Dorian.\""
    "In your light sweet voice."
    boy_dorian "\"There he is.\"\n{size=-5}{color=#ff8fa3}▸ Sink down onto him{/color}{/size}"
    jump boy_penthouse_sex

label boy_penthouse_after:
    $ vn_enter(bg="boy_penthouse", pc="begging", pc_tag="boy_pc", cast=[], cg="boy_ride_cum")
    show cg boy_ride_peak onlayer cgl
    boy_you "\"Harder— {i}ahh{/i}— Dorian— {i}harder{/i}—\""
    "You're riding him. You've been riding him for ages, and you're never going to stop. Up on your knees on the gold sheets and down, all the way, every time, till you're sat flat in his lap with his cock buried in you to the root, and up, and down, your long hair swinging down your back, your tits bouncing in his face, his mouth on them, his hands on your big round arse, squeezing, guiding nothing. You're doing it all yourself."
    show boy_dorian lazy at vn_cast_slot
    boy_dorian "\"Look at you. Look at you.\""
    "Into your chest, delighted."
    boy_you "\"Look at me— {i}ahh{/i}— look at me riding you— don't stop— don't you {i}dare{/i} let me stop—\""
    "The screens glow with every floor of the Cage. And on the sideboard, behind the little gold door of the birdcage, the mask lies flat, and watches."
    boy_you "\"More— {i}more{/i}— fill me up— please— {i}please{/i}, Dorian—\""
    show cg boy_ride_cum onlayer cgl
    "He does. He pulls you down by the hips, once, gently, and holds you there, and comes deep inside you, hot and thick, pulse after pulse, and you feel every one, and you beg for the next." with vnfx("flash", "shake")
    "And your small cock, trapped between your bellies, soft and leaking and untouched, just goes. All on its own. It jerks and spurts between you, hot on both your stomachs, while your arse clenches round him over and over, and you throw your head back and scream it at the glass ceiling, at the whole town lying lit up below you."
    boy_you "\"{i}AHHH{/i}— Dorian— {i}DORIAN{/i}—!\""
    show boy_dorian lazy at vn_cast_slot
    boy_dorian "\"There he is.\""
    "Softly, and he kisses you."
    $ boy.ending = "mask"
    $ achievement.grant("Bantam Loses")
    hide cg onlayer cgl
    "You don't stop. You ride him again, slower, and then faster, and he lets you, and lies back on the gold sheets with his hands on your hips and watches you do it like you're the best thing he's ever seen on any of his screens."
    "Below you, on every floor, the Cage carries on. Gold and busy and warm. Somewhere down there a scaffolder's pouring a negroni, and a prop forward's taking a bow, and Gideon's standing at the staff door, saying {i}Name{/i}."
    "Near morning you go home, the long way, along the docks, and fall into the camp bed in your stockings and your choker.\n{size=-5}{color=#ff8fa3}▸ Tuesday{/color}{/size}"
    call vn_night(9)
    jump boy_epilogue

## The epilogue, Tuesday morning: WHERE IS BANTAM?, the pigeon photo; the phone face down; the choker
## still on, and the key card that lights every button. Then Stay or Go: the choice that decides the
## ending.
label boy_epilogue:
    $ boy.fit = "k6"
    $ vn_enter(bg="boy_bedsit", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_paper")
    "Tuesday morning in the bedsit over the launderette. The floor's warm. The dryers are going round downstairs, and the whole room smells of fabric softener."
    show cg boy_paper onlayer cgl
    show screen boy_card("WHERE IS BANTAM?", ["{i}The town's masked hero has not been seen on the rooftops for over a month. The police decline to comment. Is the Bantam gone for good?{/i}"])
    "There's a newspaper on the mat. You pick it up in your stockings and your choker, with your long hair down your back, and it's folded open inside, the way it never comes, like somebody wanted you to see. And under the headline, the photo. The blurry one from the pier. The one everybody said was a pigeon."
    hide screen boy_card
    "You read it twice. You fold it up, and put it on the table, next to your phone."
    "Your phone's still face down, where you left it on Monday. CASE FILE is in there. Every note. You don't turn it over."
    hide cg onlayer cgl
    "On the hook by the door, the red hood hangs, the way it's hung all week. On the wall, the corkboard: the posters, the red string, the photo of the tower with the pin in it. You look at the scaffolder's grin, and the prop forward's broken nose, and the driver's cap."
    "The gold choker's still on. You haven't found the clasp. You haven't looked. Under the brass tag your fingers find the key card, and you know without trying it that it lights every button in the lift, all of them, all the way to the top."
    menu:
        "The red hood on its hook. The key card under the tag."
        "Up in the lift" (ending=True):
            jump boy_epilogue_stay
        "Hang up the hood" (ending=True):
            jump boy_epilogue_go

label boy_epilogue_stay:
    $ boy.epilogue = "stay"
    $ vn_enter(bg="boy_staff_door", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_epi_stay")
    "You put the paper in the bin."
    show cg boy_epi_stay onlayer cgl
    "That night you go back to the Cage, round the back, to the staff door. You don't press the intercom. You don't need to. Gideon opens it before you get there, and looks at you, and his face does nothing, and he steps aside."
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"In you go.\""
    "You stay. You keep the bedsit, and the key kiosk in the daytime, because you like cutting keys. But the nights are the Cage's."
    "Cordelia does your lipstick at the lift. Soren calls you gorgeous and lets you shake. The scaffolder brings you ice. The prop forward teaches you the high kick, and you get it, eventually, in your gold heels, and the chorus line cheers. Ulric takes your bookings, which are considerable."
    "And once a week, late, the lift goes all the way to the top for you. Sometimes it's the penthouse, and Dorian, on the gold sheets with the town lit up below. Sometimes it's the gilded chair, in the spotlight, with the club on its feet. Sometimes it's the velvet sofa behind the gold curtain, and Ulric, and the candles."
    "The kit comes home with you in a gold box: the choker, the stockings, the leotard, the micro-bikini. Never the mask. The mask stays in the birdcage on the sideboard, where you can see it every time you're up there, with its little door shut."
    "The paper never finds out where Bantam went.\n{size=-5}{color=#ff8fa3}▸ Out onto the docks{/color}{/size}"
    jump boy_route_return

label boy_epilogue_go:
    $ boy.epilogue = "go"
    $ vn_enter(bg="boy_bedsit", pc="heroic", pc_tag="boy_pc", cast=[], cg="boy_epi_board")
    show cg boy_epi_board onlayer cgl
    "You take the corkboard down."
    "The posters come off one at a time. The red string comes away in a long tangle and you wind it round your fingers and put it in a drawer. The photo of the tower goes in the drawer too, face down, with the pin still in it."
    "The red hood stays on its hook. You look at it for a long time. You don't take it down. You just leave it there, hanging, and you don't put it on."
    $ boy.fit = "own"
    show cg boy_epi_go onlayer cgl
    "Then you put on whatever fits, which isn't much, and the gold choker, because it doesn't come off, and you go out, down the stairs past the dryers, as you are."
    "Mer Street's busy. People look. You let them. You walk with your hips swinging and your long dark hair down your back and your small, useless cock tucked away and forgotten, and it's a nice morning, and nobody needs rescuing, and for the first time in years you don't check the rooftops once."
    "Down on the docks, the black-brick tower stands with its windows dark in the daylight, waiting for the evening. Somewhere at the top of it, on a sideboard, behind a little gold door, there's a mask."
    "It's in good hands.\n{size=-5}{color=#ff8fa3}▸ Down to Mer Street{/color}{/size}"
    jump boy_route_return
