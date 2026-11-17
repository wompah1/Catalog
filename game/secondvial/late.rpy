## secondvial, ch 8-10: after the flip, all consensual and gleeful, in the doujin register (the SOURCES row).
## The third vial is the cap: "huge, weighted up", and milk (the owner's ruling allows lactation).
## Production rewrite (2026-11-13, twinetesting-c9): every scene run long, a picture per beat.

## ---- ch 8: the third vial, drunk first ----------------------------------------------------------------
label svl_third:
    $ svl.fit = "nude"
    show cg svl_third_drink onlayer cgl
    "You knock the third back before he's got the first cork out, and grin at him over the empty glass."
    svl_you "\"Well? Pour the other two, then. Chop chop. We've got a south end to steal back.\""
    $ svl.asked = True
    "Caddic stares at you for a long second. In all these months you've never seen his face do anything. It does something now. Then he hands them over."
    $ svl_body("n5")
    show cg svl_third_swell onlayer cgl
    "{color=#e8a8c0}Everything at once. Your breasts swell out heavy and enormous, weighted down, the nipples dark and dripping. Your hips go wider than the barrel. Your ass, your thighs. And the dawn you used to go back to just isn't there any more. You can feel the door close.{/color}"
    svl_you "\"{i}Ohhh{/i}— oh {i}fuck{/i}— look at me— LOOK at me, Caddic— they're {i}leaking{/i}—!\""
    "You cup them and lift them and they spill over your hands, and milk runs down your wrists, and you laugh, a big loud dirty laugh that bounces off the barrels."
    svl_you "\"Ha! Never two, she said! Never two! Look at three!\""
    show cg svl_third_suck onlayer cgl
    "He's on his knees with his mouth on one before you've finished saying it, and milk runs down his chin into his beard, and you hold his head there by the hair and tell him to suck harder, because you can."
    svl_you "\"Harder. Both. Go on, they're paid for. Mine now, aren't they, Caddic? All of it's mine.\""
    show svl_caddic flat at vn_cast_slot
    svl_caddic "\"Mm.\""
    show cg svl_third_ride onlayer cgl
    "You push him onto his back on the cellar flags and climb on yourself, and set the pace, and laugh at the face he makes."
    vn_sfx "{i}Pap! Pap! Pap!{/i}"
    svl_you "\"There— {i}there{/i}— more— you wanted a mainstage, here's your {i}mainstage{/i}— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "You come, and it doesn't settle. It just starts building again."
    show cg svl_third_again onlayer cgl
    svl_you "\"Again. Don't you dare go soft on me, Caddic. Again. You wanted to turn the crowd? Turn {i}me{/i} over.\""
    "He turns you over on the cold flags, and you laugh into the stone with milk running down your ribs, and push back at him, and shout it loud enough to rattle the hatch."
    svl_you "\"Yes— yes— {i}that's{/i} the stuff— again— {i}AHH{/i}—!\"" with vnfx("flash", "shake")
    "You go up the cellar steps for opening already wanting the next one, and the one after that, and the whole south end of the city."
    jump svl_ch8_after

## ---- ch 9: the stage. Opening night of the converted house -----------------------------------------
label svl_stage:
    $ svl.fit = "apron"
    $ vn_enter(bg="svl_house", pc="gleeful", pc_tag="svl_pc", cast=[], cg="svl_stage_open")
    "Opening night. You're on the dais in the apron and nothing else, knees apart, kneading your breasts for the crowd, milk running down to your belly. The room is a wall of eyes and coin, all the way back to the door and out of it into the rain."
    svl_you "\"Well? Who's first? Don't all rush— no, {i}do{/i} all rush—\""
    show cg svl_stage_crowd onlayer cgl
    "They come in a surge. A mouth on each nipple. Someone between your thighs. A cock for your mouth, another for your hand, the mattress soaked through before the first bell."
    svl_you "\"Yes— yes— {i}more{/i}— is that all you've got— {i}AHH{/i}— next— NEXT—!\"" with vnfx("flash", "shake")
    show cg svl_stage_mirror onlayer cgl
    "The mirrors Caddic hung go all the way round the alcove, and every time you look up there are a hundred of you: a hundred huge-breasted, wide-hipped, ash-pink girls laughing with their mouths full and their legs in the air."
    "Not one of them is a man under a grain cart. Not one of them is the plain one with the washboard chest. You wave at them. They wave back."
    show cg svl_stage_brusk onlayer cgl
    if svl.brusk == "snap":
        "Brusk is in the crowd, at the front, red-faced. You told him once to keep his hands on his stew. You crook a finger at him now, and he comes, and you put his hands where you want them."
        svl_you "\"Not on the stew tonight, Brusk. Here. And here.\""
    else:
        "Brusk is in the crowd, at the front, red-faced. He pushed a copper between your fingers once, for nothing in your bodice. You take his hand now and fill it."
        svl_you "\"Not a tit to my name, was it, Brusk? Have two.\""
    "The room roars, the way it did the first time. It's a different roar."
    show cg svl_stage_queue onlayer cgl
    vn_sfx "{i}Clink. Clink. Clink.{/i}"
    "Caddic works the door with a strongbox under his arm, taking coin, and every coin that goes in the box you can hear from the dais, and every one of them makes you laugh."
    svl_you "\"Keep them coming, Caddic! I'm not even warm yet!\""
    "By dawn you're sprawled across the ruined mattress, and the line out of the door is still long."
    jump svl_ch9_after

## ---- ch 9: the bath, with Mira and Sabine -------------------------------------------------------------
label svl_bath:
    $ svl.fit = "nude"
    $ vn_enter(bg="svl_bath", pc="dazed", pc_tag="svl_pc", cast=[("svl_sabine", "warm")], cg="svl_bath_scrub")
    "Sabine hauls you up off the mattress with one arm over her shoulders and drops you in the big tub, and scrubs you down like a spilled cask."
    svl_sabine "\"First night's the worst. Or the best, depending.\""
    svl_you "\"Best. Definitely best.\""
    "Mira comes in with towels and sits on the edge of the tub with her skirt hitched up and her feet in the water, and looks at you for a long time."
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"You think you're the first, darling? Why d'you think we've stayed?\""
    "It takes you a moment. Then you look at them properly, for the first time since the floor: Mira's hips like a river bend; Sabine's whisper, which makes men pay without knowing why."
    svl_you "\"You— both of you? The vials?\""
    hide svl_mira
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"Me first. Then Mira. Then some girls who didn't stay. Then you.\""
    show cg svl_bath_tell onlayer cgl
    "Sabine tells you how it goes: the reversal stops, and after a while you'd fight to keep it. Keep what you can. Build your own patrons. Learn where he keeps the ledger."
    if svl.supper == "asked":
        svl_you "\"You told me to find some courage first, then a sandwich.\""
        hide svl_mira
        show svl_sabine sly at vn_cast_slot
        svl_sabine "\"And you did. Look at the size of it.\""
    else:
        svl_you "\"You never asked me to sit. Not once. I ate in the yard for a month.\""
        hide svl_sabine
        show svl_mira wry at vn_cast_slot
        svl_mira "\"We were waiting to see if you'd last. Girls who eat with us and then don't last, that's worse.\""
    show cg svl_bath_both onlayer cgl
    "Then Mira's fingers slide into you under the hot water and Sabine's mouth closes on a nipple, and milk clouds the bathwater, and the two of them laugh at it."
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"Look at her. Like a dairy.\""
    hide svl_mira
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"Hold still, dairy.\""
    svl_you "\"{i}Ahh{/i}— oh, you {i}two{/i}— why didn't you ever let me sit with you— {i}ahh{/i}— Mira, there— {i}AHHH{/i}—!\"" with vnfx("flash", "shake")
    "Afterwards the three of you sit with your foreheads together in the cooling water."
    show cg svl_bath_plan onlayer cgl
    hide svl_mira
    show svl_sabine sly at vn_cast_slot
    svl_sabine "\"He keeps it under the bar at night and in the pantry by day. The key's on his belt. He sleeps with the belt on.\""
    hide svl_sabine
    show svl_mira wry at vn_cast_slot
    svl_mira "\"He's kept us on wages and trust for six years. Me eight. Every girl he ever had, he had on the books.\""
    svl_you "\"Then the books are the thing.\""
    "Mira looks at you, properly, and smiles, sharp as a knife."
    svl_you "\"So. Let's see what he owes us.\""
    jump svl_ch9_end

## ---- ch 10: festival night on the main table ---------------------------------------------------------
label svl_table:
    $ svl.fit = "nude"
    $ vn_enter(bg="svl_house", pc="gleeful", pc_tag="svl_pc", cast=[], cg="svl_table_festival")
    "Festival night. Lanterns in every window down Spindlemarket and the house heaving, and you with a shallow glass of wine, climbing onto the main table: the same scarred oak plank where you once wiped spills and took the jokes."
    show cg svl_table_strip onlayer cgl
    "You strip on it, slowly, for the room, the velvet falling off you one piece at a time, and the room counts down with you and cheers on the last one."
    "The customers are a roster now. Faces from the days when you hoped not to be touched at all. The man from the first tasting. The two who raced. Brusk, drunk and gentle-handed, who takes his turn at the end of the night and calls you ma'am."
    show cg svl_table_all onlayer cgl
    "You lie back with your arms over your head and your legs wide, and invite anyone, everyone."
    svl_you "\"Come on, then! The house is open! Every hour, every way, twice if you like— {i}AHH{/i}— yes— {i}YES{/i}—!\"" with vnfx("flash", "shake")
    show cg svl_table_mira onlayer cgl
    "Mira climbs up with you at midnight, because it's a festival, and kisses you upside down over the edge of the table while a man fucks you, and Sabine pours wine into both your mouths from a height and misses, gloriously."
    show svl_mira wry at vn_cast_slot
    svl_mira "\"Boss. Look at the door.\""
    "The line goes out of the door and round the corner, past the Gilded Tun, which is dark."
    svl_you "\"Ha! Ha— {i}ahh{/i}— serves them right— {i}AHHHH{/i}—!\"" with vnfx("flash", "shake")
    hide cg onlayer cgl
    $ vn_enter(bg="svl_office", pc="gleeful", pc_tag="svl_pc", cast=[], cg="svl_count")
    show screen svl_purse(10)
    "When the last customer staggers out and dawn comes gold through the curtains, you climb down, wipe your thighs, stretch, and go and count the coins. Into your own strongbox. In your own office. With your own key."
    hide screen svl_purse
    "You pay Mira. You pay Sabine. You pay the girl on the door and the girl in the kitchen, in coin, at the end of the shift, after you've checked the tally. Nobody's tips are held in trust."
    "You belong to nobody but your own appetite. And the city lines up, paid in full, to welcome you home."
    hide cg onlayer cgl
    $ vn_feat("I Am the Contract")
    jump svl_route_return
