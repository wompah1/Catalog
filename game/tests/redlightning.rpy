## Red Lightning played through, start to finish, by Ren'Py's own test runner (tools/rptest.sh).
## The two walks make the choices the DoL traces made (tools/trace_dol.py: "first" and "alt"), so
## tools/check.py can compare the two screens line by line. The choices come from a plan the choice
## screen takes by itself (vn_test_pick): no mouse clicks, which could miss a menu still settling or
## be thrown by a pointer over the window. The assert checks every planned choice was taken.

## Every run ends by closing the game, passed or failed (a failed run otherwise leaves the window
## standing on the last screen).
testsuite global:
    teardown:
        exit

testcase redlightning_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['My Rival Spikes', 'LAST ONE ROUND', 'Gains. Obviously', 'Go and demand', 'The power ballad', 'Tell him', 'Kneel for him', 'WATCH THIS', 'Flex both arms', 'Another season']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase redlightning_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['My Rival Spikes', 'TRY AND KEEP UP', "It's the good halls soap", 'Go and demand', 'The one about driving', 'Keep it quiet', 'Kneel for him', 'SEE YOU AT THE TAPE', 'Arm round Miles', 'A flat in town', 'Squeeze them round him']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
