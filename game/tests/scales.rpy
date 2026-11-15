## The Beast Court Files Humans as Furniture... played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a takes every optional round and a day beat on most days, writes two
## terms and writes home; walk b skips the rounds, writes one term, grinds first and goes home for
## the autumn; walk c mixes them and takes the seal night. No DoL trace to check against: the route
## was rewritten straight in Ren'Py (game/scales/PLAN.md). Not run until the route has its art (the
## owner, 2026-11-12: walks once a route has art).

testcase scales_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['The Beast Court', 'She pushes back in', 'Pull off and object', 'Dust the perch', 'Wait for dusk', 'Tell her to take it out', 'The steam vents', 'Wait for dusk', 'She bends you over again', 'Demand she stop', 'Hold the docket case', 'Lie down for the night', 'Wait for dusk', 'Hold them up for her again', 'Object', 'Wait for dusk', 'Your name in the contract', 'The registry notified', 'Fold it up', 'Sink down on her', 'Tell her what you want', 'The drawer of unfinished', 'Wait for dusk', 'Ask for harder', 'Plainly', 'Let the day go by', 'Write home']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (scl.ending == "one-name" and scl.epilogue == "letter" and scl.row == "7" and scl.tier == 6 and scl.done and scl.terms == ["name", "registry"])

testcase scales_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['The Beast Court', 'She draws out', 'The steam vents', 'Wait for dusk', 'Beg her to let you work', 'Dust the perch', 'Wait for dusk', 'She lets you lie in her arms', 'Lie down for the night', 'Wait for dusk', 'Let her pull you into her lap', 'The steam vents', 'Wait for dusk', 'Space, sometimes', 'Fold it up', 'Grind on the head first', 'Tease her', 'Wait for dusk', 'Tell her not to slow down', 'Defiantly', 'Let the day go by', 'Go home for the autumn']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (scl.ending == "one-name" and scl.epilogue == "autumn" and scl.petition == "defiant")

testcase scales_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['The Beast Court', 'She pushes back in', 'Mock her round it', 'Wait for dusk', 'Shove at her hips', 'Duties and dockets', 'Wait for dusk', 'She bends you over again', 'Mock her', 'The steam vents', 'Dust the perch', 'Lie down for the night', 'Wait for dusk', 'Hold them up for her again', 'Say nothing and glare', 'Hold the docket case', 'Wait for dusk', 'The right to refuse display', 'Fold it up', 'Sink down on her', 'Beg her', 'Hold the docket case', 'Wait for dusk', 'Just moan for her', 'Tenderly', 'Her quarters, that night', 'Pull her down by the tail', 'Write home']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (scl.ending == "one-name" and scl.epilogue == "letter" and scl.petition == "tender")
