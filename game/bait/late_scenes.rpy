## bait's encounters, ch 8-11: after the flip, all consensual. The court calls her by her class.
## The production rewrite (2026-11-13): every encounter at full length, a picture every beat.

## ---- ch 8: Sable. Spoken, polite, asked for ------------------------------------------------------
label bai_sable:
    $ vn_enter(bg="bai_forest", pc="flushed", pc_tag="bai_pc", cast=[("bai_sable", "polite")], cg="bai_sable_meet")
    "A sunlit glade, and in it a werewolf, the same animal as the first night two rungs up: tall, wolf-eared, black-haired, humanoid, hung. And she talks."
    bai_sable "\"Well, hello there, Bait. Took you long enough to find me.\""
    bai_you "\"You, uh... live here?\""
    bai_sable "\"Someone has to. The orcs keep tearing up the nice dens. If you're here for a reason, say so. Circling never got anyone fed.\""
    bai_you "\"I need... something. From someone who can talk. With hands. And patience. You.\""
    bai_sable "\"Of course you do. Heat's coming, isn't it? Warg's a calendar. Slime's a toy. But hunger always comes round.\""
    show cg bai_sable_ask onlayer cgl
    "Nothing in this forest has ever waited for you to say it. She waits. She actually waits, ears up, polite, until you do."
    menu:
        "How you ask."
        "Plainly":
            $ bai.ask = "plain"
            bai_you "\"I need to be fucked. Properly. By someone who understands what it's for. I'm asking.\""
        "Begging":
            $ bai.ask = "beg"
            bai_you "\"Please. {i}Please.{/i} I need you to fuck me. I've needed it for days, and nothing's {i}asked{/i}, and I'm asking, please—\""
    $ bai.asked = True
    bai_sable "\"Good, Bait. You're supposed to ask. The forest owes you that much. Take off your coat and come here. Say it again.\""
    bai_you "\"Please fuck me, Sable. I want it. I need it.\""
    show cg bai_sable_strip onlayer cgl
    "You drop the coat. You drop the wrap. You stand in front of her naked and leaking and ask a third time, because she likes it, and because you do."
    bai_sable "\"Good girl. Where first? Your heat's climbing.\""
    bai_you "\"Inside. Please. Knot me.\""
    show cg bai_sable_open onlayer cgl
    "She lays you down in the ferns on your hands and knees and kneels behind you, and asks, and you say yes, and she pushes into you slow and careful, bit by bit, checking."
    bai_sable "\"Tell me if it's too much. You can always ask me to wait.\""
    "No one in this forest has ever said the word {i}wait{/i} to you. You almost come from that alone."
    bai_you "\"It's not— it's not too much— more— please, more—\""
    show cg bai_sable_mid onlayer cgl
    "Negotiated, courteous, long. She asks before every change of position and thanks you after. She builds the pace up slowly until she's fucking you hard and steady, one hand in your hair, the other holding your hip."
    bai_sable "\"You're taking me so well, Bait. Is it enough? You can ask for whatever you want. The forest always answers need.\""
    bai_you "\"Harder— please— need it rough—\""
    "She gives you rough, and asks if it's right, and you shout that it's right, and she gives you more."
    bai_sable "\"Louder, Bait. Nobody here minds. The whole wood's been listening to you for days.\""
    bai_you "\"{i}AHH{/i}— good— so good— {i}Sable{/i}— don't stop— please don't stop— I'm {i}asking{/i}—\""
    bai_sable "\"That cock of yours is going quiet, isn't it? That's a good sign. Means you're almost through. Shh. Breathe.\""
    bai_you "\"Is it— is that bad— {i}ahh{/i}— should I— should I be {i}worried{/i}—\""
    bai_sable "\"Worried? No. You're becoming what you're for. Most things never get to.\""
    show cg bai_sable_knot onlayer cgl
    "She knots you the way the warg did, and talks you through it the whole time, her voice low in your ear, and it's the same thing, exactly the same thing, and it is nothing like it."
    bai_you "\"Again— please— again, all of it— {i}knot me{/i}— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg bai_sable_peak onlayer cgl
    "You come again and again on her knot, your cock barely there and dribbling, and when she finally empties into you it's so much you can feel it, overflowing round the knot and down your thighs."
    bai_you "\"{i}AHHHH{/i}— Sable— {i}SABLE{/i}—!\"" with vnfx("flash", "shake")
    bai_sable "\"It'll be different from now on. It's weather, not a calendar. Arrives, drives, takes you over. You'll need someone, every time.\""
    bai_you "\"I can ask? Every time?\""
    bai_sable "\"You're queen's fare, Bait. Asking's how it works. Thank you, Bait. For being honest.\""
    bai_you "\"Thank {i}you.{/i} For all of it. For answering.\""
    bai_sable "\"Any time. Now rest. Weather'll turn again soon.\""
    vn_th "(The most polite thing that's happened to you in this whole forest. It's absolutely the worst. You'd do it again tomorrow.)"
    jump bai_ch8_after

## ---- ch 9: the oni. Size he survives because of the slime; the change completes -------------------
label bai_oni:
    $ vn_enter(bg="bai_forest", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_oni_arrive")
    "She comes through the trees the way weather does: an oni, red-skinned and horned, twice your height, a club over one shoulder that she leans against a tree like an umbrella. Her cock is already out, and it's the size of your forearm."
    "\"Bait,\" she rumbles: a warning and a greeting. \"You call, I answer. Gods, you're smaller than I thought.\""
    bai_you "\"I can take it. Survival. Science. Call it whatever you want. Give me everything.\""
    "\"I've snapped sturdier. But you asked.\""
    bai_you "\"That's how the class works. Function follows use. I've done the maths.\""
    "You haven't. The tremor in your thighs says so."
    show cg bai_oni_test onlayer cgl
    "She picks you up like a parcel and lays you on your back in the ferns, and spreads your thighs with one hand, and tests you with two thick fingers, curious, and then three."
    "\"Huh. Stretchy thing, aren't you.\" She grins. \"The slime's, is it? Clever Bait.\""
    bai_you "\"Don't— {i}hahh{/i}— don't {i}inventory{/i} me, that's {i}my{/i} job—\""
    "\"Ready?\" Her voice vibrates through your ribs. Nothing has ever asked if you were ready before."
    bai_you "\"Ready. Yes. {i}Please.{/i}\""
    show cg bai_oni_take onlayer cgl
    "Size you shouldn't survive. The slime's gift opens for her and holds, nothing torn, and you can't believe it's working, and it works, and your belly rises with the shape of her."
    "\"Look at that.\" She lays her huge palm over the bulge of herself in your stomach, delighted. \"All the way. Nobody's ever taken all the way.\""
    bai_you "\"I— I'm taking— {i}hahh{/i}— I'm taking all of it— look at me— {i}look{/i}— I'm {i}doing{/i} it—\""
    bai_you "\"{i}OHH{/i}— it fits— it FITS— oh god, look at— {i}hahh{/i}—\""
    "\"Good. Good Bait. Takes every inch. Stretches for me, grows for me. Take your queen's due.\""
    bai_you "\"More— give me more— I called you, didn't I— {i}hahh{/i}— I called the biggest thing in the forest and it {i}fits{/i}— give me {i}all{/i} of it—\""
    "\"Greedy Bait.\" She laughs, a sound like rockfall, and gives you all of it."
    show cg bai_oni_mid onlayer cgl
    $ bai_body(9)
    "{color=#9fd8ff}She pounds you into the ferns, and with every thrust your hips go wider under her, structurally, because the geometry demands it, your pelvis remaking itself around her as you watch.{/color}"
    bai_you "\"My hips— they're— {i}ahh{/i}— are they {i}moving{/i}— oh god, they're {i}moving{/i}— don't stop— {i}don't stop{/i}—\""
    "\"Wider. That's it. Make room for your court.\""
    show cg bai_oni_change onlayer cgl
    "{color=#9fd8ff}And somewhere in the middle of it you notice there's nothing there any more, between your legs: only wet, and opening, and slick round the base of her. You're far too busy to grieve it.{/color}"
    vn_th "(Gone. Filed. Later. Much later.)"
    show cg bai_oni_peak onlayer cgl
    bai_you "\"{i}AHHHH{/i}— I'm alive— I'm ALIVE— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    "She fills you to the brim and past it, and your chest spills milk down your sides as you come and come under her."
    show cg bai_oni_leave onlayer cgl
    "She pats your hips, huge and reverential. \"Throne hips, Bait. Mark my words.\""
    "\"Queen's fare, you are. Gods. You'll have half the forest at your door by morning.\""
    bai_you "\"Not {i}queen{/i} yet.\""
    "\"Tell that to the court.\" And she shoulders her club and is off through the trees, her stride shaking the ground."
    jump bai_ch9_after

## ---- ch 10: the court arrives and queues; the first no -------------------------------------------
label bai_court:
    $ vn_enter(bg="bai_den", pc="flushed", pc_tag="bai_pc", cast=[], cg="bai_court_queue")
    "They come: the lamia, coiled; the arachne, delicate on eight legs; an orc band; a kitsune with nine tails; the harpy from the ridge; Sable, smiling. And they don't fight each other. They queue."
    if bai.ruled == "orcs":
        vn_th "(The orcs. The first thing you ever ruled out. Standing in a neat line with their hands clasped.)"
    elif bai.ruled == "lamia":
        vn_th "(The lamia. The first thing you ever ruled out. First in the queue.)"
    else:
        vn_th "(The arachne. Eight legs, a hard no, a principle. Waiting her turn with her hands folded.)"
    bai_you "\"Um. I guess I... operate on a first-come basis?\""
    show cg bai_court_lamia_ask onlayer cgl
    "The lamia tastes the air and slides forward, her hands cupped as if in proposal, her cock already sliding out of its slit."
    "\"Queensright. May I?\""
    bai_you "\"Okay. Yes. Please.\""
    show cg bai_court_first onlayer cgl
    "She coils round your hips, yards of her, warm and heavy, and her cock slides into the new place for the first time, and you cry out at how much better it is."
    "\"I will gorge myself on you, my Queen.\""
    "Her coils tighten round your waist in long slow waves, and you can feel every muscle of her moving, and it's like being held by the whole river."
    bai_you "\"{i}Ahh{/i}— there— oh, {i}there{/i}— why didn't anyone— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg bai_court_lamia_milk onlayer cgl
    "She milks your breasts while she fucks you, slow and thorough, her coils tightening in time, and you beg her not to stop, and then not to give you to anyone else, and then that you didn't mean that."
    bai_you "\"Next, please.\""
    show cg bai_court_arachne onlayer cgl
    "The arachne is at your side in a blink, eight eyes hungry with the intent to worship. \"Permission?\" You nod, and she flips you onto your front and binds your arms in silk, softly, and takes you hard."
    "\"Our Queen. Our Queen.\" She says it like a prayer, every thrust, her six red eyes half-shut."
    bai_you "\"{i}Ahh{/i}— yes— say it— say it again— {i}AHH{/i}—\""
    bai_you "\"{i}Hahh{/i}— oh god, it's {i}ridged{/i}— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    show cg bai_court_orcs onlayer cgl
    "The orc band next, all of them at once, filling you everywhere, calling you Queen like a chant, swapping places with clumsy enormous reverence."
    "\"QUEEN. QUEEN. QUEEN.\" They stamp it. The ground shakes. Somebody's crying, but it's an orc, and it's from joy, and you decide that's allowed."
    "Somewhere in the third of them, one reaches out of turn."
    bai_you "\"{i}Ahh{/i}— yes— all of you— {i}QUEEN{/i}— I'm— {i}ahh{/i}— I'm your {i}queen{/i}—\""
    "You've never said it before. It comes out at the top of your lungs, and every orc in the clearing roars."
    menu:
        "The orc, out of turn."
        "\"No.\"":
            bai_you "\"No. Wait your turn.\""
        "\"Not you. Not yet.\"":
            bai_you "\"Not you. Not yet. Back of the line.\""
    show cg bai_court_no onlayer cgl
    "It obeys. At once, entirely, like a dog on a command it's always known."
    "Sable smiles, as if she knew. \"Your word has weight. Use it as you please.\""
    "And you feel the crown drop a notch, for having spent authority instead of earning it. The position's a debt."
    show cg bai_court_harpy onlayer cgl
    if bai.shout4 == "down":
        "The harpy from the ridge lands beside you with a thump. \"Still want down, Bait?\" She doesn't wait for an answer."
    else:
        "The harpy from the ridge lands beside you with a thump. \"Quiet one. You held on so nicely.\" She doesn't wait for an answer."
    "She fucks you hard and fast, marking your shoulders with her teeth, milking your breasts in her taloned hands."
    "\"I remember these tits. Used to be you bounced. Now you anchor.\""
    bai_you "\"{i}Hahh{/i}— you {i}dropped{/i} me on a {i}branch{/i}— {i}ahh{/i}— harder—\""
    if bai.ask == "beg":
        show bai_sable polite at vn_cast_slot
        bai_sable "\"You begged so prettily the first time. Ask again.\""
    else:
        show bai_sable polite at vn_cast_slot
        bai_sable "\"You asked so plainly the first time. Ask again.\""
    "Sable is next, and asks, and you say yes."
    "\"Do you wish more, my Queen?\" she asks, later, her hand on your thigh."
    bai_you "\"No. Not there, not yet. My—\""
    "She stops instantly. The crown wobbles, another notch, and then settles as she bends and takes your breast in her mouth instead, and you feel it fill back up."
    show cg bai_court_many onlayer cgl
    "And then the kitsune, all nine tails, worshipping you and then taking your ass, and the last orc, and the next, and the next."
    "\"Queen first,\" the kitsune murmurs, and kisses every part of you she can reach before she takes anything, nine tails wrapping you like a fur blanket."
    bai_you "\"{i}Ahh{/i}— oh, you're {i}soft{/i}— why is everything so {i}soft{/i} now— {i}AHH{/i}—\""
    bai_you "\"Next— next— whoever's next— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    jump bai_ch10_after

## ---- ch 11: the petitions, then the last one granted to several at once ------------------------------
label bai_petitions:
    show cg bai_petition_sable onlayer cgl
    "Sable is first, always. She kneels, and petitions for joint patrol rights on the north ridge with the werewolves, and nurses from your breast while she makes her case."
    "You grant it. Your milk runs down her chin. She thanks you."
    show cg bai_petition_lamia onlayer cgl
    "Sirissa the lamia, next, for her share of the stream, grinding against you, and then sliding into you, coiling round your hips, negotiating as she fucks you."
    "\"The harpy took two intervals last dusk and did not relinquish the nest. I require compensation.\""
    bai_you "\"You'll have her scheduled for the next dusk. No double sessions without accounting in advance. {i}Ahh{/i}— there— right {i}there{/i}—\""
    "\"I accept the compensation, my Queen.\""
    "\"Half the stream, Queen. The upper half. Mm. You stretch so beautifully.\""
    "You grant her the upper half, and gasp the terms."
    show cg bai_petition_harpy onlayer cgl
    "The harpy, with a grievance about the kobolds, nuzzling and feeding at your breast."
    "\"Counter-petition. The southern storms ruined the old nests, and the kobolds moved into the ridge while I rebuilt. I require one interval for reconstruction, undisturbed.\""
    menu:
        "The harpy's grievance: the kobolds are nesting in her ridge."
        "Rule for the harpy":
            $ bai.ruling2 = "harpy"
            "The ridge is the harpy's. The kobolds will move. She preens, delighted, and drinks."
        "Rule for the kobolds":
            $ bai.ruling2 = "kobolds"
            if bai.shout5 == "bar":
                "The kobolds can stay. They'll only lean on the door until it opens anyway. You remember."
            else:
                "The kobolds can stay. They walked straight through your zero, once. It seems a waste to argue with that kind of commitment."
    show cg bai_petition_dryad onlayer cgl
    "The dryad, for her tithe of sunlight in the old growth, feeding you sap with one hand while the other works you open, and then mounting you with her sap-dripping cock, announcing her border plans as she stretches you wide."
    "\"I am owed the tithe of milk for the lower groves, and a ruling on the boar dispute. Shall I take both now?\""
    bai_you "\"The boars will be moved to the lower meadow, and the burden shared between the orcs and the kobold band. {i}Nnh{/i}— capacity is— {i}ahh{/i}— capacity is guaranteed—\""
    "\"By Her Majesty's elasticity,\" the dryad finishes for you, kindly, and slides in."
    show cg bai_petition_orcs onlayer cgl
    "The orcs seek audience next. Two are granted the interval: one eats your cunt with enormous dedication, the other takes your breasts."
    "\"Queen first,\" grunts the bigger one, solemnly, and kneels between your thighs, and gets to work with a dedication you'd find touching if you could think."
    bai_you "\"{i}Ahh{/i}— very— very {i}diplomatic{/i}— the crown— {i}nnh{/i}— the crown recognises— {i}AHH{/i}— your {i}service{/i}—\""
    "And then the arachne, with her request."
    menu:
        "The arachne's request: the whole of tomorrow night."
        "Grant it":
            $ bai.ruling = "grant"
            "She grants it. The arachne bows all eight legs."
        "Deny it":
            $ bai.ruling = "deny"
            "She denies it. The arachne bows anyway, and the crown holds, because she earned that one."
    jump bai_convergence

label bai_convergence:
    show cg bai_convergence onlayer cgl
    "The last petition is granted to several at once, and the queue collapses. Everything in use at the same time."
    "The back holds because of the slime. The front exists because the tally finished. The chest is in use because of the dryad. The hips hold because of the oni. The scent that brought them all is the bloom's. It's the bill, and it all comes due at once."
    "The oni beneath her, the lamia behind, the kitsune at her mouth, the arachne at her breasts, the dryad's vines everywhere else, the orcs stamping in a ring."
    bai_you "\"{i}Mmh{/i}— yes— all at once— nobody wait— {i}nobody wait{/i}— the queen {i}says{/i}— {i}ahh{/i}—\""
    "\"Best Queen,\" someone says, and someone else, \"All mine,\" and the court argues happily about it with its hands full."
    bai_you "\"{i}Ahh{/i}— all of you— yes— the queen's— the queen's {i}open{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    show cg bai_convergence_peak onlayer cgl
    "She comes, and comes, laughing, and the court comes with her, and the moss is soaked, and nobody stops for a long, long time."
    show cg bai_schedule onlayer cgl
    "Afterwards, still being ridden, she sits up on her furs, adjusts her crown, and conducts the forest's business competently and at length."
    bai_you "\"Tomorrow's docket is full. Sable first. The arachne's night is as ruled. The orcs will form one line, not three.\""
    bai_you "\"If I need to leave, you'll have days' notice. Administrative absence only for cause. And if you want me gone for good—\""
    "\"—you'll have to elect a new throne,\" says Sable, smiling, and the whole court laughs, and nobody moves to elect anything."
    "And she closes the session by explaining to the court, patiently, as a matter of administration, the conditions under which she'll be leaving."
    "Nobody argues. It isn't a coronation. It's a schedule."
    show cg bai_epilogue onlayer cgl
    if bai.maren == "stop":
        "Somewhere in a small clearing, a woman with deer ears is sewing, and doesn't look up. You asked her how to stop. She told you. You didn't."
    else:
        "Somewhere in a small clearing, a woman with deer ears is sewing, and doesn't look up. You asked her how she stopped. She told you. You went the other way."
    "The forest grew itself a queen on purpose, and always meant to."
    hide cg onlayer cgl
    $ bai.ending = "court"
    $ vn_feat("Throne")
    jump bai_route_return
