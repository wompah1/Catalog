## ledger's director scenes, written out for Ren'Py (2026-11-12). In the DoL catalog these were
## <<sl_sex>> rows; here each is its beats, frame by frame: open, mid, peak, the climax, then the
## passage after. Lines from ledger.js's pools (setup.ledgerLines: Bai Lian's taking lines, her
## early, offering and late bands; setup.slPcLines.ledger and ledgerMirror: the haggler's protest,
## betray, break and flip). The non-con pass as ruled (owner, 2026-10-19/20): the alcove's hands and
## the gallery's mouth never flip; the first offering flips at the break; the knock, the unlacing
## and the rooms are consensual. The paperwork is the coercion, never a threat.

## Rung 1, optional: the other half of the appraisal, her hands over his round her cock. Non-con,
## no flip. (rungs.twee :: Ledger Alcove Sex; lead Bai Lian, hand, noncon, pool ledger)
label led_alcove_sex:
    $ vn_enter(bg="led_alcove", pc="outraged", pc_tag="led_pc", cg="led_alcove_hands")
    show cg led_alcove_hands onlayer cgl
    if led.alcove == "haggle":
        led_you "\"Fine— {i}fine{/i}— at what rate? Per stroke? I want a {i}rate{/i}—\""
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Grip. Haggle with the other hand if you like.\""
    else:
        "You pull. Her hands close tighter over yours and don't let them go anywhere."
        show led_bailian dry at vn_cast_slot
        led_bailian "\"Both hands. It's on the intake register. You signed it.\""
    "She closes your fingers round her cock with her own hand over them and works them."
    led_you "\"That's NOT in the— I sold the VESSEL, not— {i}hnngh{/i}— not THIS—!\""
    show cg led_alcove_hands_mid onlayer cgl
    "She pins your free wrist to the mirror."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"This part must be accounted for, too.\""
    led_you "\"Show me the clause— show me where it {i}says{/i}— {i}ahh{/i}— Senior Sister, STOP—!\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Haggle all you want. The ink's dry.\""
    led_you "\"Why is the— why does a PROVISION feel— {i}AHH{/i}—\""
    show cg led_alcove_hands_peak onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Slow.\""
    "She says it, and doesn't stop."
    led_you "\"That's— that's worth a {i}discount{/i}, at least— I want a discount for— {i}hahh{/i}—\"" with vnfx("shake")
    jump led_alcove_after

## Rung 2, optional: the gallery mirror again, her fist in his hair. Non-con, no flip; the haggling
## comes out round her cock. (rungs.twee :: Ledger Mirror Sex; lead Bai Lian, oral, noncon, pool
## ledgerMirror)
label led_mirror_sex:
    $ vn_enter(bg="led_gallery", pc="outraged", pc_tag="led_pc", cg="led_gallery_mouth")
    show cg led_gallery_mouth onlayer cgl
    "You try to get up. Her fist tightens in your hair and holds you on her."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Breathe out. Through the nose. It's already filed.\""
    led_you "\"Mmf— {i}mmmf{/i}— nnt in the— {i}mmf{/i}— not in the GALLERY—!\""
    "It comes out round her cock as mush. You push at her thighs. Her fist in your hair holds you exactly where you are."
    show cg led_gallery_again onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Tongue. You don't have to like it. It's a provision.\""
    led_you "\"Ghk— th's nt— {i}mmf{/i}— that's not in the TERMS—\""
    vn_sfx "{i}Glk.{/i}"
    "Your tongue's working her. You didn't tell it to."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"The Hall's walking past, Jiu. Let it see you take it.\""
    "The forms jostle on every stroke and the jade throbs and gets nowhere."
    led_you "\"{i}Mmmf{/i}— mmh—! {i}Mmmmh{/i}— mmf— {i}MMMH{/i}—!\"" with vnfx("shake")
    "It was meant to be an objection. It comes out a moan, loud, and a Blossom walking past giggles."
    jump led_mirror_after

## Rung 4, THE MANDATORY SCENE: the first offering on the registry mat, wrists pinned to the small of
## his back. Non-con, and it flips at the break: "...Fine. FINE. Senior Sister— again. Log it TWICE."
## (rungs.twee :: Ledger Offering Sex; lead Bai Lian, anal, doggy, lock, inside, noncon, pool ledger,
## flip break)
label led_offering_sex:
    $ vn_enter(bg="led_registry", pc="outraged", pc_tag="led_pc", cg=None)
    hide cg onlayer cgl  # ff 2:01 am: no picture, offering-open failed 5 draws (SCENES.md ledger v5)
    "You breathe out. She pushes in. Slow." with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Breathe out. It's already filed.\""
    led_you "\"I want it struck from the— {i}nnh{/i}— I object— I {i}object{/i}, write that DOWN—!\""
    menu:
        "Her hand pins your wrists to the small of your back."
        "Twist against her grip":
            "You twist against her grip. It doesn't move an inch."
            led_you "\"Renegotiate— I want to RENEGOTIATE—!\""
        "Demand the clause again":
            led_you "\"Read it back— read the CLAUSE back— it says {i}pace{/i}, it doesn't say—\""
            show led_gu pleasant at vn_cast_slot
            led_gu "\"{i}At the First Flower's pace.{/i}\""
            "Gu reads it back, helpfully."
        "Glare at Gu in the mirror":
            "You glare at Gu in the registry mirrors. Gu, writing, doesn't look up."
            show led_gu pleasant at vn_cast_slot
            led_gu "\"Objection noted.\""
    show cg led_offering_mid onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Slow. You don't have to like it. It's a provision.\""
    led_you "\"I signed for {i}holding{/i}— nobody said— {i}hah{/i}— nobody said it'd be THIS—!\""
    "She pins both your wrists to the mat with one hand."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Objection noted. Gu wrote it down.\""
    led_you "\"It's not— this isn't the deal— {i}ohh{/i}— don't do that again— don't— {i}ahh{/i}— again—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"It's entered, Jiu. One offering, appointment seven.\""
    led_you "\"I still object— I {i}still{/i}— {i}nnngh{/i}— why am I pushing BACK—\""
    hide cg onlayer cgl  # ff 2:01 am: no picture, offering-peak failed 5 draws (SCENES.md ledger v5)
    show led_bailian dry at vn_cast_slot
    led_bailian "\"The register doesn't have a column for asking.\""
    led_you "\"Enter it— ENTER it— Grandad's interest, PAID, just don't stop—!\"" with vnfx("shake")
    show led_pc wanting
    show cg led_offering_flip onlayer cgl
    "It comes up out of you from where she is, and you come untouched, shouting at the registry mirrors." with vnfx("flash", "shake")
    led_you "{b}\"...Fine. FINE. Senior Sister— again. Log it TWICE.\"{/b}"
    "Hoarse. You shove back onto her, and this time you mean it."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"There. That's what the oil was for.\""
    led_you "\"Fine— {i}fine{/i}— put it on the account— put ALL of it on the account— {i}ahh{/i}— more—!\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Open. Good. Again.\""
    jump led_offering_after

## Rung 5, the knock: asked for. Consensual from the first stroke. (rungs.twee :: Ledger Knock Sex;
## lead Bai Lian, anal, doggy, lock, inside)
label led_knock_sex:
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cg="led_knock_open")
    show cg led_knock_open onlayer cgl
    "She pushes in, all the way, in one long stroke, and you scream it into her sheets." with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Louder.\""
    led_you "\"{i}YES{/i}— Bai Lian— yes, {i}yes{/i}, that's it, that's what I asked for—\""
    hide cg onlayer cgl  # ff 3:47 am: no picture, knock-mid failed 4 draws (SCENES.md ledger v8)
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Not slow. Not today.\""
    led_you "\"Harder— don't you DARE go slow— I asked— I {i}asked{/i}—\""
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Your little cock's dripping again. Good. Let it.\""
    "She doesn't touch it."
    hide cg onlayer cgl  # ff 3:46 am: no picture, knock-peak failed 4 draws (SCENES.md ledger v7)
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Mine. Say it louder than that.\""
    led_you "\"{i}Yours{/i}— yours, yours, I'm YOURS— {i}ahh{/i}—\"" with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Yang in a box, everything else to me. That's the whole refinement.\""
    jump led_knock_after

## Rung 6, optional: the real chest round her again. Consensual. (rungs.twee :: Ledger Unlaced Sex;
## lead Bai Lian, titjob)
label led_unlaced_sex:
    $ vn_enter(bg="led_dressing", pc="wanting", pc_tag="led_pc", cg=None)
    hide cg onlayer cgl  # ff 2:01 am: no picture, unlaced-tits failed 5 draws (SCENES.md ledger v5)
    "You squeeze them round her again, and she's still hard, and she laughs."
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Junior sister.\""
    led_you "\"They're {i}mine{/i}— look— no squeak— no {i}silk{/i}—\""
    show cg led_unlaced_again onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Don't come until I say. ...Now. Say it.\""
    led_you "\"{i}Mine{/i}— {i}ahh{/i}—\"" with vnfx("shake")
    jump led_unlaced_after

## Rung 6, the rooms: face to face for the first time. Consensual. (rungs.twee :: Ledger Rooms Sex;
## lead Bai Lian, anal, missionary)
label led_rooms_sex:
    $ vn_enter(bg="led_flower_rooms", pc="wanting", pc_tag="led_pc", cg="led_rooms_open")
    show cg led_rooms_open onlayer cgl
    "You pull her in. She slides into you face to face, slow, all the way, and she watches you take it." with vnfx("shake")
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Look at me.\""
    led_you "\"I'm {i}looking{/i}— Bai Lian— I'm looking—\""
    show cg led_rooms_mid onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Junior sister.\""
    "Your wings beat the sheets. Your tail's round her calf. Your tits bounce against her with every stroke."
    led_you "\"Don't call me that— don't— {i}ahh{/i}— do, do call me that—\""
    show cg led_rooms_peak onlayer cgl
    show led_bailian dry at vn_cast_slot
    led_bailian "\"Forget the jade. I have.\""
    led_you "\"What jade— {i}ahh{/i}— {i}ahhh{/i}—\"" with vnfx("shake")
    jump led_rooms_after
