## I Hid in the Sultan's Harem…, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every first
## choice, walk b every second. One ending (the package's). Rebuilt for the production rewrite (2026-11-13).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase harem_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 200.0
    $ renpy.session["vn_picks"] = ["I Hid in the Sultan's Harem to Keep My Balls, and Now the Sultan Keeps the Key", 'Over the washing lines', 'Curtsey', 'Try to lift her off', 'Shout for help', 'Press your thighs together', 'Work the hips', 'Dance at the Sultan', '"Ladies, one at a time, there\'s plenty!"', '"Same again tomorrow night!"', 'Wave at the captain', 'Join in about his velvet case', '"Yes. Do it. Please."', '"Fair."', 'Try to explain', '"Make him scrub the floors!"', 'Bet on Nasrin', '"Tell me how much you want it."', '"To the thief!"', '"Surprise, my sultan."']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hrm.chapter == 6 and hrm.ending == "key" and hrm.broke and hrm.broke4 and hrm.asked and hrm.she and hrm.row == "6" and hrm.shout1 == "lift" and hrm.fair == "fair" and hrm.route1 == "lines" and hrm.greet == "curtsey" and hrm.help1 == "call" and hrm.danceat == "sultan" and hrm.promise2 == "tomorrow" and hrm.talk3 == "case" and hrm.jade3 == "ask" and hrm.punish4 == "floors" and hrm.tease5 == "tell" and hrm.toast6 == "thief" and hrm.secret6 == "surprise")

testcase harem_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 200.0
    $ renpy.session["vn_picks"] = ["I Hid in the Sultan's Harem to Keep My Balls, and Now the Sultan Keeps the Key", 'Down the gutter', 'Bow like a sailor', 'Beg her to keep quiet at least', 'Bite your lip and hold still', 'Turn to the wall', 'Shimmy the coins', 'Dance at Zarina', '"Form a queue, ladies!"', '"Every night!"', 'Blow the captain a kiss', "Tell him a sailor's story", '"Bet you can\'t make me come with that."', '"...Fair enough."', 'Turn your face away', '"Make him dance in a coin belt!"', 'Bet on Leyla', '"Don\'t you dare look away."', '"To the captain!"', '"Keep it, then."']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hrm.chapter == 6 and hrm.ending == "key" and hrm.broke and hrm.broke4 and hrm.hide2 == "wall" and hrm.dance == "shimmy" and hrm.wave == "kiss" and hrm.shout4 == "turn" and hrm.bet == "leyla" and hrm.route1 == "gutter" and hrm.greet == "bow" and hrm.help1 == "bite" and hrm.danceat == "zarina" and hrm.plenty2 == "queue" and hrm.promise2 == "every" and hrm.talk3 == "story" and hrm.jade3 == "dare" and hrm.punish4 == "belt" and hrm.tease5 == "look" and hrm.toast6 == "captain" and hrm.secret6 == "keep")
