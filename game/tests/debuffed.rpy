## Tirysia played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/debuffed/PLAN.md). Walks run once its art lands.

testcase debuffed_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Debuffed', 'Sidestep the heart', 'Hack at the slime', 'Hold your breath and charge', 'Tear the vines', 'Ward off her hand', 'Clench and hold it back', 'Spit it out', 'Push her off', 'Leap the tail', 'Brace against her', 'Cover your ears', 'Shout her down', 'Dodge the hearts', 'Fight it', 'Break the charm']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase debuffed_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Debuffed', 'Touch the heart, just to see', 'Let it settle', 'Take a curious sniff', 'Go limp in them', 'Let her cold hand land', 'Let her take the level', 'Swallow', 'Sink into her', 'Let it wrap you', 'Breathe out for her', 'Listen to the song', 'Sing with her', 'Open your arms to them', 'Ask for more', 'Walk to her']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase debuffed_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Debuffed', 'Touch the heart, just to see', 'Hack at the slime', 'Take a curious sniff', 'Tear the vines', 'Let her cold hand land', 'Clench and hold it back', 'Swallow', 'Push her off', 'Let it wrap you', 'Brace against her', 'Listen to the song', 'Shout her down', 'Open your arms to them', 'Fight it', 'Break the charm']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
