## He's Been Making Me Into His Ex... played through by Ren'Py's test runner (tools/rptest.sh).
## Walk a takes every first choice, walk b every second, walk c every third where there is one.
## Each checks the whole six weeks ran: the name landed at week 4, Danny surfaced every Friday,
## broke at week 5 and asked at week 6. No DoL trace to check against: the route was written
## straight in Ren'Py (game/cleo/PLAN.md). Rebuilt for the production rewrite (2026-11-13). Not run until the route has its art (the owner,
## 2026-11-12: walks once a route has art).

testcase cleo_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Making Me Into His Ex', 'Jollof, the proper way', '"Hey, you."', 'Pull off and say his name', 'Put it gently', 'Let him win', '"Make a mess of me."', 'Tell him to get his hands off', 'Over the sink, not looking', '"Slower. Make it last."', 'Shout at him', 'Write to the landlord', 'Say it gently', 'Roll them up slowly for him', 'Tell him whose name it really is', 'Lay out the whole theory', 'Slippers', 'The lace set he bought', 'Tell him to let go', 'Take the photos down', 'Say it over breakfast', 'The woolly hat', 'Ask for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cle.week == 6 and cle.surfaced == 6 and cle.named and cle.broke and cle.asked and cle.row == "6" and cle.cook == "jollof" and cle.greet1 == "hey" and cle.halo == "let" and cle.talk2 == "mess" and cle.ask3 == "slow" and cle.jeans4 == "landlord" and cle.stock4 == "slow" and cle.photo6 == "hat" and cle.shout1 == "name" and cle.say_six == "ask")

testcase cleo_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Making Me Into His Ex', 'A big spag bol', '"Come here, then."', 'Push at his thighs', 'Just come out with it', 'Win, obviously', '"Harder, baby."', 'Try to get off the bed', 'Sit down across from him', '"Harder."', 'Beg him to look at you properly', 'Buy the next size up', 'Nudge him with your foot', 'Make him put them on you', 'Kick at him', 'Just the advice', 'Slippers', 'The silk slip', 'Grab the headboard to climb off', 'Take the photos down', 'Say it with the kettle in your hand', 'Asleep on the sofa', 'Ask him to hold you tighter']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cle.week == 6 and cle.surfaced == 6 and cle.named and cle.broke and cle.asked and cle.row == "6" and cle.cook == "bolognese" and cle.greet1 == "come" and cle.halo == "win" and cle.talk2 == "harder" and cle.ask3 == "hard" and cle.jeans4 == "size" and cle.stock4 == "him" and cle.photo6 == "sofa" and cle.wear5 == "slip" and cle.say5 == "advice" and cle.say_six == "tighter")

testcase cleo_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Making Me Into His Ex', 'Chicken soup', '"Come here, then."', 'Pull off and say his name', 'Just come out with it', 'Let him win', '"Harder, baby."', 'Tell him to get his hands off', 'Sit down across from him', '"Slower. Make it last."', 'Shout at him', 'Buy the next size up', 'Nudge him with your foot', 'Roll them up slowly for him', 'Tell him whose name it really is', 'Just the advice', 'Slippers', 'The stockings again', 'Tell him to let go', 'Take the photos down', 'Say it with the kettle in your hand', 'The woolly hat', 'Ask for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cle.week == 6 and cle.surfaced == 6 and cle.named and cle.broke and cle.asked and cle.row == "6" and cle.cook == "soup" and cle.wear5 == "stockings" and cle.say2 == "straight" and cle.say4 == "foot" and cle.greet1 == "come" and cle.halo == "let" and cle.jeans4 == "size")

## Walk d: walk a on 3a SOMETHING IN HER SIZE; walk e: walk a on 3b ASK HER TO STAY (the alternate routes, 2026-11-13).
testcase cleo_d:
    $ _test.transition_timeout = 0.05
    $ store.CLE_BRA_READY = True  # the lane is gated off until its art lands (nqalt/120-121); the walk opens it to keep the script checked
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Making Me Into His Ex', 'Jollof, the proper way', '"Hey, you."', 'Pull off and say his name', 'Put it gently', 'Let him win', '"Make a mess of me."', 'Tell him to get his hands off', 'Over the sink, not looking', '"Slower. Make it last."', 'Shout at him', 'Write to the landlord', 'Say it gently', 'Roll them up slowly for him', 'Tell him whose name it really is', 'Lay out the whole theory', 'A proper bra', 'The lace set he bought', 'Tell him to let go', 'Say it over breakfast', 'The woolly hat', 'Ask for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cle.lane == "bra" and cle.chest and cle.week == 6 and cle.surfaced == 6 and cle.asked and cle.row == "6")

testcase cleo_e:
    $ _test.transition_timeout = 0.05
    $ store.CLE_STAY_READY = True  # the lane is gated off until its art lands (nqalt/120-121); the walk opens it to keep the script checked
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Making Me Into His Ex', 'Jollof, the proper way', '"Hey, you."', 'Pull off and say his name', 'Put it gently', 'Let him win', '"Make a mess of me."', 'Tell him to get his hands off', 'Over the sink, not looking', '"Slower. Make it last."', 'Shout at him', 'Write to the landlord', 'Say it gently', 'Roll them up slowly for him', 'Tell him whose name it really is', 'Lay out the whole theory', 'Slippers', 'The lace set he bought', 'Tell him to let go', 'Ask her to stay', 'Say it over breakfast', 'Ask for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cle.lane == "stay" and cle.week == 7 and cle.surfaced == 6 and cle.asked and cle.photo6 is None)
