## Akira played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/sideeffects/PLAN.md). Walks run once its art lands.

testcase sideeffects_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Side Effects', 'Step between them', 'Tell her to stop', 'Make him promise first', 'Bite your lip', 'Elbow him', 'Shove him off', 'Refuse to sign', 'Grip the table', "Ask what's happening to you", 'Wait for him', 'Pull him on top', 'Look at the floor', 'Hold out', 'Stay in the flat']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase sideeffects_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Side Effects', 'Shut the door on him', 'Let her keep going', 'Just get it over with', 'Let it out', 'Stand still', 'Let him finish', 'Ask what he wants', 'Push back on him', 'Ask for more of it', 'Kiss him first', 'Get on top', 'Look at them', 'Beg', 'Go to the clinic']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase sideeffects_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Side Effects', 'Step between them', 'Let her keep going', 'Make him promise first', 'Let it out', 'Elbow him', 'Let him finish', 'Refuse to sign', 'Push back on him', "Ask what's happening to you", 'Kiss him first', 'Pull him on top', 'Look at them', 'Hold out', 'Go to the clinic']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
