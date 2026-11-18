## Kaoru played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/goesdark/PLAN.md). Walks run once its art lands.

testcase goesdark_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Before It Goes Dark', 'Tell him to shut up', 'Ask what it is first', 'Fight the arms', 'Brush him off', 'Get back up', 'Tell him to stop staring', 'Push him away', 'Fight through them', 'Hit him', 'Hold it in', 'Climb', 'Fight Rasetsu', 'Tell him no', "Promise her you'll run", 'Run for the gate']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase goesdark_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Before It Goes Dark', 'Play along', 'Grab the lantern', 'Stop fighting', 'Thank him', 'Stay down', 'Let him look', 'Kiss him back', 'Let them have you', 'Ask him why', 'Let it come', 'Stop climbing', 'Ask for her', 'Follow him', 'Tell her the truth', 'Stay by his fire']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase goesdark_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Before It Goes Dark', 'Tell him to shut up', 'Grab the lantern', 'Fight the arms', 'Thank him', 'Get back up', 'Let him look', 'Push him away', 'Let them have you', 'Hit him', 'Let it come', 'Climb', 'Ask for her', 'Tell him no', 'Tell her the truth', 'Run for the gate']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
