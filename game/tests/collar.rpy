## I Bought a Voice Collar played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes
## every optional scene and hangs the mirror; walk b sends him home, lies back on the gravel, lets
## the day end and leaves the mirror facing the wall. No DoL trace to check against: the route was
## rewritten straight in Ren'Py (game/collar/PLAN.md).

testcase collar_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Bought a Voice Collar', 'The voice says keep going', 'Keep riding him', 'Bend back over the counter', 'Hang the mirror']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase collar_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Bought a Voice Collar', 'The voice sends him home', 'Lie back on the gravel', 'Let the day end', 'Leave it facing the wall']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
