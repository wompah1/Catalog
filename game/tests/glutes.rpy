## I Never Read the Label played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes
## every optional scene and stays for the off-season; walk b lets every lead call it off and takes
## the box home; walk c mixes the flavour lines. No DoL trace to check against: the route was
## rewritten straight in Ren'Py (game/glutes/PLAN.md).

testcase glutes_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Never Read the Label', 'Again, properly', 'just the cut', "He isn't finished", "We're early", 'Hold the pose', 'Post the rear', 'Snap it round', 'Hold the turn', 'carbs', 'Tits first', 'rear relaxed from today', 'Hold rear relaxed', 'Off-season']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (gl.ending == "placed" and gl.epilogue == "stay" and gl.body == 6)

testcase glutes_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Never Read the Label', 'Shower and photos', 'shave. Skin', 'Mack lets you up', 'checks the time', 'not POSING', 'Post the side', 'Slow it down', 'Hold the turn', 'water', 'Garrett, behind', 'side chest from', 'Hold rear relaxed', 'Take the box']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (gl.ending == "placed" and gl.epilogue == "go" and gl.body == 6)

testcase glutes_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Never Read the Label', 'Again, properly', 'sleep', "He isn't finished", 'checks the time', 'his wrist', 'Post the front', 'Hold it at the back', 'Hold the turn', 'program', 'Both of you', 'first board shorts', 'Hold rear relaxed', 'Off-season']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (gl.ending == "placed" and gl.epilogue == "stay")
