## My Neighbour Grew a Cock played through by Ren'Py's test runner (tools/rptest.sh). Walk a: the TSF
## cut (rub it in), every optional visit and scene, moves in. Walk b: the femboy cut (wipe it off),
## no visits or optional scenes, keeps her own door. Rewritten straight in Ren'Py: no DoL trace.

testcase neighbour_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 150.0
    $ renpy.session["vn_picks"] = ['My Neighbour Grew', 'Peek', 'Keep your hands on her', 'Tessa, before your shift', 'Just reach for her', 'Already be kneeling', 'Let her keep going', 'Let her keep your throat', 'Tessa, before your shift', 'Ask her nicely', 'Rub it into your chest', 'Tessa, before your shift', 'Tell her to hurry up', 'Push back onto her', 'Grind on it first', 'Move in across the landing']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase neighbour_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 150.0
    $ renpy.session["vn_picks"] = ['My Neighbour Grew', 'Keep your eyes shut', 'Go and scrub it off', 'Off to the café', 'Bargain', 'Wipe your chin', 'Wipe your face', 'Off to the café', 'Wipe it off', 'Off to the café', 'Ask for more one more time', 'Make her wait for it', 'Keep your own door']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
