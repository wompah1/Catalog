## Nobody in the Demon Sect Will Say "Cauldron" played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a takes every optional scene and stays; walk b skips them and goes down the
## stair; walk c mixes the flavour picks. The Hall's routine is a menu each day (renpy.display_menu).
## No DoL trace to check against: the route was rewritten straight in Ren'Py (game/ledger/PLAN.md).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase ledger_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Nobody in the Demon Sect', 'Haggle', 'other half', 'Haggle the rate', 'Smug', 'The steaming baths', 'Hips first', 'Try to get up', 'The drills', 'Smug', 'Wait for Second Bell', 'Take the biscuit', 'Grateful', 'Wait for Second Bell', 'Twist against', 'Filthy', 'Wait for Second Bell', 'Climb the walls', 'Climb the walls', 'Wait for dawn', 'Smug', 'Wait for Second Bell', 'Squeeze them', 'Wait for Second Bell', 'Your cousins first', 'Stay in the']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (led.ending == "laced" and led.epilogue == "stay" and led.row == "6" and led.she and led.burned)

testcase ledger_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Nobody in the Demon Sect', 'Hold your hand out', 'Get dressed', 'Grateful', 'Wait for Second Bell', 'The blossoms first', 'Strut till noon', 'Wait for Second Bell', 'Filthy', 'Wait for Second Bell', 'Take two', 'Smug', 'Wait for Second Bell', 'Glare at Gu', 'Grateful', 'Wait for Second Bell', 'Wait for dawn', 'Filthy', 'Wait for Second Bell', 'Into the Hall', 'Wait for Second Bell', 'Wanting all of it', 'Go down the stair']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (led.ending == "laced" and led.epilogue == "go" and led.reason == "want")

testcase ledger_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Nobody in the Demon Sect', 'Ask what a vessel', 'other half', 'Try to pull', 'Filthy', 'Wait for Second Bell', 'The seat pad first', 'Strut till noon', 'The steaming baths', 'Grateful', 'The dressing room', 'Take the biscuit', 'Smug', 'The drills', 'Demand the clause', 'Smug', 'Wait for Second Bell', 'Climb the walls', 'Wait for dawn', 'Grateful', 'Wait for Second Bell', 'Into the Hall', 'Wait for Second Bell', 'Her first', 'Stay in the']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (led.ending == "laced" and led.epilogue == "stay" and led.reason == "her")
