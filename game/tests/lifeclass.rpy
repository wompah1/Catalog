## Whatever the Life Class Draws played through by Ren'Py's test runner (tools/rptest.sh). Walk a
## takes every optional scene and keeps your name on the schedule; walk b turns every one down and
## sits for Dario; walk c mixes the flavour lines; walk d is walk a on PIN ONE BACK UP (the alternate route,
## 2026-11-13): the sheet pinned, the chest grown three times. No DoL trace to check against: the route was
## rewritten straight in Ren'Py (game/lifeclass/PLAN.md).

testcase lifeclass_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Whatever the Life Class Draws', 'Shirt first', 'not done with the underside', 'timed properly', 'On the stool, knees apart', 'Milo first', 'Close it. Please', 'Grab the stool legs', 'Hand it to Roz', "Bjorn's thighs first", 'Squeeze him', 'Keep your name']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lc.ending == "notforsale" and lc.epilogue == "stay" and lc.body == 6)

testcase lifeclass_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Whatever the Life Class Draws', 'Everything at once', 'Get dressed', 'Dot calls time', 'Leaning back', 'Home in a drop cloth', 'agency', 'WAIT', 'Hand it to Roz', 'Home in the rain', 'Squeeze him', 'Sit for Dario']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lc.ending == "notforsale" and lc.epilogue == "go" and lc.body == 6)

testcase lifeclass_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Whatever the Life Class Draws', 'fall over', 'underside', 'Dot calls time', 'Side-on', 'Milo first', 'ASKING', 'Bite the drop', 'Hand it to Roz', 'Home in the rain', 'Squeeze him', 'Keep your name']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lc.ending == "notforsale" and lc.epilogue == "stay")

testcase lifeclass_d:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Whatever the Life Class Draws', 'Shirt first', 'not done with the underside', 'timed properly', 'On the stool, knees apart', 'Milo first', 'Close it. Please', 'Grab the stool legs', 'Pin it back up', "Bjorn's thighs first", 'Squeeze him', 'Keep your name']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lc.ending == "notforsale" and lc.epilogue == "stay" and lc.body == 6 and lc.pinned and lc.grown == 3)
