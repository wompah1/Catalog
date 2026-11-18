## boytoy's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, then the passage after,
## which lands the climax. Lines from boytoy.js's pools (setup.boytoyLines: each keeper's own;
## setup.slPcLines.boytoy1, boytoyMuffled, boytoy3, boytoyMic, boytoy5, boytoy6: the hero voice's
## protest, betray and break, the break line at rung 5, the eager rung 6). Rungs 1-4 non-con and
## never flip; rung 5 breaks halfway; rung 6 consensual. A struggle menu in each non-con scene, for
## flavour, never whether. Nobody asks, threatens or lifts him; no size set against anyone's.

## Rung 1, the foyer wall: Gideon's cock between his thighs from behind, his hand on Jago's cock; a
## citizen's arrest, his rights read through moans. (main.twee :: Boytoy Foyer Sex; lead Gideon,
## thighs, doggy, lock, noncon, pool boytoy1)
label boy_foyer_sex:
    $ vn_enter(bg="boy_foyer", pc="outraged", pc_tag="boy_pc", cg="boy_foyer_open")
    show cg boy_foyer_open onlayer cgl
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Hold still.\""
    "His hand stays flat between your shoulder blades, and his cock slides through your clenched thighs, slow."
    boy_you "\"Unhand me, citizen— {i}ahh{/i}— you're NICKED—!\""
    menu:
        "His hand flat between your shoulder blades."
        "Shove off the wall":
            "You shove off the wall with both palms. You might as well shove the building. His hand doesn't move."
        "Read him his rights, properly":
            boy_you "\"You do not have to say— {i}ahh{/i}— anything— but it may harm your— {i}hnn{/i}— your DEFENCE—\""
            "He says nothing at all while you read him his rights. He just keeps fucking your thighs, slow and heavy, until you lose your place."
        "Call for backup":
            boy_you "\"BACKUP— I need— {i}nngh{/i}— backup in the FOYER—\""
            show boy_gideon blank at vn_cast_slot
            boy_gideon "\"Mm.\""
    show cg boy_foyer_mid onlayer cgl
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Smooth as you like.\""
    "His palm runs down the back of your bare thigh, and his fist moves on your cock in time."
    boy_you "\"This is a CITIZEN'S ARREST— {i}nngh{/i}—! I am placing you under— {i}hnn{/i}— under ARREST— get your hand OFF it—!\""
    "\"Mm.\" Nothing else. His hips roll, and his thumb rubs the wet tip of you against the wallpaper."
    boy_you "\"Why are my hips— stop that, hips— that's an ORDER—!\""
    "They push back into him anyway."
    show cg boy_foyer_peak onlayer cgl
    show boy_gideon blank at vn_cast_slot
    boy_gideon "\"Hold still.\""
    "His fist tightens on your cock, and your hips push back into him all on their own."
    boy_you "\"It is NOT leaking— that is EVIDENCE— {i}ahh{/i}— don't touch the evidence—!\"" with vnfx("shake")
    boy_you "\"Anything you say may be— {i}ahh{/i}— may be— {i}AHH{/i}—!\""
    jump boy_foyer_after

## Rung 2, behind the bar: on his knees out of the punters' sight, Soren's hand in his curls; every
## protest muffled round him. (rungs.twee :: Boytoy Last Orders Sex; lead Soren, oral, inside, noncon,
## pool boytoyMuffled)
label boy_last_orders_sex:
    $ vn_enter(bg="boy_bar", pc="outraged", pc_tag="boy_pc", cg="boy_behind_bar")
    show cg boy_behind_bar onlayer cgl
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Good, gorgeous.\""
    "His hand in your curls brings you straight back down the second you pull off."
    boy_you "\"{i}Mmph{/i}— law-abiding— {i}mmph{/i}— CITIZEN—\""
    menu:
        "His hand in your curls."
        "Pull off to protest":
            boy_you "\"You're— {i}glk{/i}— NICKED—\""
            "You pull off to say it, and he feeds it straight back in."
        "Push at his thighs":
            "You push at his thighs. His hips roll into your mouth anyway, slow, and his hand doesn't move."
        "Glare up at him":
            "You glare up at him with your mouth full. He strokes your curls like you've said something sweet."
    show cg boy_bar_mid onlayer cgl
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Last orders, gorgeous.\""
    "Down the bar, over your head, and his hips roll into your mouth."
    vn_sfx "{i}Chk-chk-chk.{/i}"
    "He shakes one-handed. The other hand is in your hair."
    boy_other "\"Where's the new one got to?\""
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Downstairs.\""
    "A punter leans on the brass, and Soren pushes your head down."
    boy_you "\"{i}Mmh{/i}— {i}mmnh{/i}— (why's it LEAKING)—\""
    "Your cock strains the gold hot pants, and you can't do a thing about it."
    show cg boy_bar_peak onlayer cgl
    show boy_soren grin at vn_cast_slot
    boy_soren "\"Look at those lips.\""
    "He pulls you off by the curls to look, and feeds it straight back in."
    boy_you "\"{i}Mmph{/i}— I am NOT— {i}glk, glk{/i}— sucking— I am RESISTING—\"" with vnfx("shake")
    boy_you "\"{i}Mmmh{/i}— {i}mmh{/i}— {i}MMH{/i}—!\""
    "Your head's bobbing on its own, and you're still trying to say no."
    jump boy_last_orders_after

## Rung 3, MANDATORY: bent over the dressing table in the corset, his first anal; no on every thrust,
## squeezed out of him by the corset. (rungs.twee :: Boytoy Dressing Table Sex; lead Cordelia, anal,
## inside, doggy, lock, noncon, pool boytoy3)
label boy_dressing_table_sex:
    $ vn_enter(bg="boy_dressing", pc="outraged", pc_tag="boy_pc", cg="boy_dressing_open")
    show cg boy_dressing_open onlayer cgl
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"Breathe in.\""
    "Cordelia gives the corset's lacing a tug, and the moan comes out of you squeezed."
    boy_you "\"No— {i}hah{/i}— no— Cordelia— {i}ahh{/i}—!\""
    menu:
        "A hand flat on your back."
        "Push up off the table":
            show boy_cordelia brisk at vn_cast_slot
            boy_cordelia "\"Hands flat, darling.\""
            "A hand flat on your back holds you down among the powder pots, and she drives in deep."
        "Order her to stop":
            boy_you "\"Get it— OUT— no— {i}ahh{/i}— no— you're NICKED—!\""
            show boy_cordelia brisk at vn_cast_slot
            boy_cordelia "\"Listen to you! The whole floor can hear you.\""
            "She sounds thrilled about it."
        "Kick at her shins":
            "You kick back at her shins in your heels, and wobble, and grab the table. She snaps a suspender against your thigh and keeps going."
            show boy_cordelia brisk at vn_cast_slot
            boy_cordelia "\"Look at those stockings on you.\""
    hide cg onlayer cgl  # ff 2:43 am: no picture, dressing-mid failed 4 draws (SCENES.md boytoy v5)
    boy_you "\"No— citizen— this is NOT a FITTING— {i}hah{/i}— no—!\""
    show boy_cordelia brisk at vn_cast_slot
    boy_cordelia "\"There's that bum coming in.\""
    "She squeezes it, both hands, and fucks into it harder."
    boy_you "\"No— why's it— {i}hahh{/i}— no—!\""
    "Your small cock bobs out of the lace and drips on the powder pots."
    # ff 2:18 am: dressing-peak failed 4 draws (SCENES.md boytoy v4); dressing-mid stays up
    "The powder pots rattle on every thrust. A puff of powder goes up off the table, and Cordelia laughs."
    boy_you "\"No— {i}ahh{/i}— it's so FULL— no— NO—!\"" with vnfx("shake")
    boy_you "\"No— no no no— Bantam doesn't— {i}hnnngh{/i}— NO—!\""
    jump boy_dressing_table_after

## Rung 4, the gilded chair: on Caspian's lap facing the club, masked, in the spotlight; no into the
## microphone, moaned. (rungs-late.twee :: Boytoy Spotlight Sex; lead Caspian, ride, noncon, pool
## boytoyMic)
label boy_spotlight_sex:
    $ vn_enter(bg="boy_stage", pc="outraged", pc_tag="boy_pc", cg="boy_chair_open")
    show cg boy_chair_open onlayer cgl
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Ladies and gentlemen!\""
    "Caspian's hands on your hips pull you down onto his cock, and the club roars." with vnfx("shake")
    boy_you "\"No— {i}ahh{/i}— don't CLAP— no—!\""
    "Straight into the microphone."
    menu:
        "The microphone at your lips."
        "Push the microphone away":
            "You shove the microphone away. Caspian brings it back, gently, like a man returning a dropped glove."
            show boy_caspian showman at vn_cast_slot
            boy_caspian "\"Into the microphone, darling, they paid for this.\""
        "Tell the club it's a sting":
            boy_you "\"This is a STING— {i}hnn{/i}— no— this is NOT the ACT—!\""
            "The club laughs, delighted, and claps the line."
        "Grab the chair's arms":
            "You grab the velvet arms of the chair to lift yourself off. Caspian's hands on your hips pull you straight back down to the root, and the club whistles."
    show cg boy_chair_mid onlayer cgl
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Look at those hips, ladies and gentlemen! Bounce for them!\""
    "He bounces you, and they whistle."
    boy_you "\"No— stop BOUNCING me— I'm not— {i}ahh{/i}— no—!\""
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Let's hear it for the Bantam!\""
    "The whole room applauds. His cock pushes up into you on the beat."
    show cg boy_chair_peak onlayer cgl
    boy_you "\"No— it's leaking on the LEOTARD— {i}ahh{/i}— nobody LOOK— no—!\""
    show boy_caspian showman at vn_cast_slot
    boy_caspian "\"Isn't he marvellous?\""
    "The club agrees, at volume, and he bounces you again."
    boy_you "\"No— no— {i}NOOOhh{/i}—!\"" with vnfx("shake")
    "Into the microphone, for the whole club."
    jump boy_spotlight_after

## Rung 5, the velvet sofa: on his back, legs up over Ulric's shoulders, the mask on; non-con until
## halfway, then THE BREAK, once: "Don't stop. Don't— don't you dare stop—", then begging.
## (rungs-late.twee :: Boytoy Booth Sex; lead Ulric, anal, inside, missionary, lock, noncon, pool
## boytoy5, flip break)
label boy_booth_sex:
    $ vn_enter(bg="boy_booth", pc="outraged", pc_tag="boy_pc", cg="boy_sofa_open")
    show cg boy_sofa_open onlayer cgl
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir sings beautifully.\""
    "Ulric fucks you slow and deep, your legs up over his shoulders."
    boy_you "\"No, citizen— no—!\""
    menu:
        "Your legs over his shoulders."
        "Push at his chest":
            "You push at his chest. He kisses one nipple, then the other, and doesn't stop moving."
            show boy_ulric polite at vn_cast_slot
            boy_ulric "\"Sir is most welcome.\""
        "Tell him the VIPs are evidence":
            boy_you "\"No— this is a STING— the VIPs are— {i}ahh{/i}— no—!\""
            show boy_ulric polite at vn_cast_slot
            boy_ulric "\"Again, Sir? Of course.\""
            "He draws nearly all the way out and gives you the whole length again."
        "Kick your heels":
            boy_you "\"No— {i}mmh{/i}— why are my legs— no—!\""
            "Your ankles have hooked behind his neck all on their own."
    show cg boy_sofa_mid onlayer cgl
    "The gold curtain sways. Ulric presses your knees back and sinks in to the root, and murmurs, \"Sir sings beautifully.\""
    boy_you "\"No— it's not even HARD— why's it— {i}ahh{/i}— no—!\""
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir's new figure is a credit to the house.\""
    "His thumb circles your nipple, slow, while he fucks you."
    boy_you "\"No— {i}ahh{/i}— no— {i}AHH{/i}— no—!\""
    show boy_pc begging
    show cg boy_sofa_break onlayer cgl
    boy_you "{b}\"Don't stop. Don't— don't you {i}dare{/i} stop—\"{/b}" with vnfx("flash", "shake")
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"There it is, Sir.\""
    "He gives you all of it."
    boy_you "\"Deeper— {i}ahh{/i}— DEEPER—! Harder, citizen— that's an ORDER— {i}ahh{/i}—!\""
    show boy_ulric polite at vn_cast_slot
    boy_ulric "\"Sir may have whatever Sir likes.\""
    "Deeper, harder, exactly as asked."
    jump boy_booth_after

## Rung 6, the big bed: he rides Dorian face to face, eager and filthy from the first touch.
## Consensual. (rungs-late.twee :: Boytoy Penthouse Sex; lead Dorian, ride, pool boytoy6)
label boy_penthouse_sex:
    $ vn_enter(bg="boy_penthouse", pc="begging", pc_tag="boy_pc", cg="boy_ride_open")
    show cg boy_ride_open onlayer cgl
    "You sink down onto him, all the way, slow, and your eyes roll back." with vnfx("shake")
    show boy_dorian lazy at vn_cast_slot
    boy_dorian "\"There he is.\""
    "Dorian's hands settle on your bubble butt and squeeze while you ride him."
    boy_you "\"All of it— I want all of it—!\""
    show cg boy_ride_mid onlayer cgl
    show boy_dorian lazy at vn_cast_slot
    boy_dorian "\"Years I've watched you on those rooftops. Look at you now.\""
    "He smiles up at you."
    boy_you "\"Look at me— look at me riding you—!\""
    show boy_dorian lazy at vn_cast_slot
    boy_dorian "\"Take your time. All the time you want.\""
    "His mouth finds your nipple, and you sink down harder."
    "Your small cock bounces between you, soft and leaking, and you don't even look at it."
    show cg boy_ride_peak onlayer cgl
    "Behind you the wall of screens flickers with the floors below. Dorian doesn't look at them once. He looks at you."
    boy_you "\"Deeper— {i}deeper{/i}— don't you dare let me stop—!\"" with vnfx("shake")
    jump boy_penthouse_after
