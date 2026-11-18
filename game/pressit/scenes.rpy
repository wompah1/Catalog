## pressit's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, your climax (its own
## frame), then the passage after. Lines from pressit.js's pools (setup.slCombatLines.Portia and
## .Travis, setup.slPcLines.pressit): Travis's taking lines and your sincere protest before a flip;
## the false-victim costume after it and in the consensual scenes; Portia's own lines, never a praise
## line. No DP, ever; nobody threatens anybody.

## Rung 5, optional: Travis again, his call, not yours. He's already in when it starts. Non-con with
## his taking lines and your sincere protest, and it flips on the second beat: you break faster the
## second time. (days-late.twee :: Press Stall Sex; lead Travis, vaginal, inside, flip 2)
label prs_stall_sex:
    $ vn_enter(bg="prs_stall", pc="furious", pc_tag="prs_pc", cg="prs_stall_sex_open")
    $ prs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg prs_stall_sex_open onlayer cgl
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Ha, yeah, okay— hold still— you're so {i}wet{/i}, Mahoney—\""
    "He's still in you. He just starts again."
    prs_you "\"Get OFF— I said that's {i}enough{/i}— I never SAID— get your hands OFF my— {i}hnngh{/i}—!\""
    "His hands lock on your hips."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude. You were {i}literally{/i}— dude.\""
    show cg prs_stall_sex_mid onlayer cgl
    prs_you "\"It's the SWITCH— she switched it ON— I didn't ask for— {i}ahh{/i}—!\""
    "Travis laughs, and doesn't slow down. He thinks it's a bit."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Yeah, yeah, coercion, totally—\""
    prs_you "\"Stop pushing BACK— that's not me, that's my HIPS doing that—\""
    show prs_pc costume
    show cg prs_stall_sex_peak onlayer cgl
    prs_you "\"Coercion— this is SO coercion— right THERE—!\"" with vnfx("shake")
    "You yell it at the tiles, and push back onto him, and that's the second time today you've stopped saying no."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Best shift ever. Best shift {i}anyone's{/i} ever—\""
    prs_you "\"Under protest— {i}ahh{/i}— I'm doing this under PROTEST— don't you dare slow down—\""
    show cg prs_stall_sex_cum onlayer cgl
    "You come round him with your cheek on the wet tiles, squealing, and he holds your hips through every pulse of it." with vnfx("flash")
    $ prs_enc.pc_orgasms = 1
    jump prs_stall_after

label prs_stall_after:
    $ vn_enter(bg="prs_stall", pc="costume", pc_tag="prs_pc", cast=[("prs_travis", "grin")], cg="prs_stall_sex_cum")
    show cg prs_stall_sex_cum onlayer cgl
    "He comes in you again with his face in your hair and his hands full of your tits, and it's even more than the first time." with vnfx("flash")
    prs_travis "\"Best shift ever. Best shift {i}anyone's{/i} ever had.\""
    "To the shower head.\n{size=-5}{color=#ff8fa3}▸ Out of the stall{/color}{/size}"
    $ vn_pass(10)
    jump prs_number

## Rung 6, THE MANDATORY SCENE: her cock in your pussy, asked for in plain words. No way round it and
## no asking to stop. Doggy, from behind on her bed; it opens with her pushing in. Consensual: her own
## lines carry every beat, and you're loud always. (days-late.twee :: Press Ask Sex; lead Portia,
## vaginal, doggy, lock, inside, vocal always)
label prs_ask_sex:
    $ vn_enter(bg="prs_flat", pc="wanting", pc_tag="prs_pc", cg="prs_ask_open")
    $ prs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg prs_ask_open onlayer cgl
    "Portia drives in to the root and holds there." with vnfx("shake")
    show prs_portia amused at vn_cast_slot
    prs_portia "\"There it is. That's what you asked for, [prs_pc_name].\""
    prs_you "\"{i}AHH{/i}— it's IN— it's {i}in{/i}, oh god, oh god, it's finally— don't you {i}move{/i}— no, MOVE—\""
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Louder. You asked in plain words. Moan in plain words too.\""
    show cg prs_ask_mid onlayer cgl
    "Her hips slap your ass and the whole bed jumps."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Still the subject. Still mine.\""
    prs_you "\"It's the switch, it's not ME— fuck, right THERE—\""
    "She leans over your back and bites the nape of your neck, still moving."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Nobody's making you. Push back.\""
    "You push back."
    prs_you "\"This is SO not consensual— again, AGAIN—!\""
    show cg prs_ask_peak onlayer cgl
    "Slow, all the way out, all the way in."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"That one counts. Feel it count.\""
    "She stops dead inside you, and waits, and smiles while you beg."
    show prs_portia amused at vn_cast_slot
    prs_portia "\"Ask properly, [prs_pc_name].\""
    prs_you "\"Put it in my— it's IN, I know it's in— {i}move{/i}— I have NO choice here— deeper, DEEPER—\"" with vnfx("shake")
    show cg prs_ask_climax onlayer cgl
    "You come on her cock the second she moves again, clamping down on her so hard she swears, gushing round her onto the sheets, and the heat goes out of you like a tide going out, and comes straight back in." with vnfx("flash", "shake")
    $ prs_enc.pc_orgasms = 1
    jump prs_finding

## Rung 7, THE FINALE: Travis leads, four more in their twenties (extras with no lines), already in
## when it starts. Consensual: you run the room. No DP of one hole. Portia doesn't join; she watches
## with the phone in her pocket. (days-late.twee :: Press Finale Sex; lead Travis, extras 4, vaginal,
## doggy, inside)
label prs_finale_sex:
    $ vn_enter(bg="prs_changing", pc="wanting", pc_tag="prs_pc", cg="prs_finale_open")
    $ prs_enc = VNState(partner_came=True, pc_orgasms=0)
    show cg prs_finale_open onlayer cgl
    "Travis grabs your hips and slams in like he's scared you'll vanish." with vnfx("shake")
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Dude. {i}Dude{/i}.\""
    prs_you "\"I want it on record that I— {i}ahh{/i}— that I OBJECT— harder—\""
    "The first of the four is in front of you with his hoodie half off. You take him in your mouth without looking up."
    show cg prs_finale_mid onlayer cgl
    show prs_travis grin at vn_cast_slot
    prs_travis "\"You're not even fighting, man. You're not even {i}pretending{/i}.\""
    "He sounds thrilled about it."
    prs_you "\"{i}Mmf{/i}— this is coercion— {i}glk{/i}— this is {i}totally{/i} coercion—\""
    "Round a mouthful of somebody whose name you'll never know. Two more of them have a hand each on your swinging tits. The fourth is waiting his turn with his fist round his cock, and you crook a finger at him over your shoulder anyway."
    show prs_travis grin at vn_cast_slot
    prs_travis "\"This is the best shift I've ever had. This is the best shift {i}anyone's{/i} ever had.\""
    show cg prs_finale_peak onlayer cgl
    show prs_travis grin at vn_cast_slot
    prs_travis "\"You're so wet, dude— how are you this {i}wet{/i}—\""
    prs_you "\"This is coercion— DON'T you stop—!\""
    show prs_travis grin at vn_cast_slot
    prs_travis "\"Yeah? Yeah?\""
    "He has no idea what he's agreeing with. He agrees harder."
    prs_you "\"Again— AGAIN— all of you, come {i}on{/i}—\"" with vnfx("shake")
    show cg prs_finale_climax onlayer cgl
    "You come on Travis's cock with somebody else's in your mouth, screaming round it, shaking so hard the bench rattles against the lockers, and on the end of the bench Portia uncrosses her legs, and crosses them the other way." with vnfx("flash", "shake")
    $ prs_enc.pc_orgasms = 1
    jump prs_finale_after
