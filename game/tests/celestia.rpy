## A Catgirl Drafted Me as the Town's Magical Girl played through by Ren'Py's test runner. Walk a: every fork
## "Make it shine" (Nightshade stays guttering), the optional loft visits on days 3 and 5, the showdown, Keep
## the cape. Walk b: every fork "Let it go to him" (the dark ending), the other flavour picks, the loft visits
## on days 4 and 6, Go home to Pippa. Rewritten straight in Ren'Py: no DoL trace.

testcase celestia_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['A Catgirl Drafted Me', 'Hand on your hip', 'Make it shine', "Pippa's loft", 'Make it shine', 'Catch the night bus', 'Get OFF me', 'Plead with them', 'Make it shine', "Pippa's loft", 'Fight it', 'Make it shine', 'Walk out onto the lawn', 'Make them stare', 'Keep the cape']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (store.ce.ending == "showdown" and store.ce.epilogue == "keep" and store.ce.power == 0)

testcase celestia_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['A Catgirl Drafted Me', 'Squeeze them together', 'Let it go to him', 'Order them off', 'Breathe it', 'Let it go to him', 'Mock him', "Pippa's loft", "Don't you DARE", 'Scream for Luna', 'Let it go to him', 'Go to the Elk Street', 'Yell at him', 'Let it go to him', "Pippa's loft", 'Kneel for it', 'Go home to Pippa']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (store.ce.ending == "dark" and store.ce.epilogue == "home" and store.ce.power == 100)

## Walk c, the threshold: only the lair let go (it counts double: 40, below 60), so the showdown still
## comes; no loft visits; Grin at him; Hang it up.
testcase celestia_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['A Catgirl Drafted Me', 'Hand on your hip', 'Make it shine', 'Breathe it', 'Make it shine', 'Catch the night bus', 'Get OFF me', 'Plead with them', 'Make it shine', 'Go to the Elk Street', 'Fight it', 'Let it go to him', 'Walk out onto the lawn', 'Grin at him', 'Hang it up']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (store.ce.ending == "showdown" and store.ce.epilogue == "hang" and store.ce.power == 40)

## Walk d, over the threshold by the streets alone: court, club and bus let go (60), the lair shines: dark.
testcase celestia_d:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['A Catgirl Drafted Me', 'Hand on your hip', 'Let it go to him', 'Mock them', 'Breathe it', 'Let it go to him', 'Demand he let go', 'Catch the night bus', 'Get OFF me', 'Plead with them', 'Let it go to him', 'Go to the Elk Street', 'Fight it', 'Make it shine', 'Go anyway', 'Take the crown', 'Stay his']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (store.ce.ending == "dark" and store.ce.epilogue == "stay" and store.ce.power == 60)
