## Getting Bred Is Just How You Get Promoted Around Here, played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a takes every first choice (every optional round, Stay, the alpha at the
## back wall); walk b every second (no optional round, Go); walk c the third flavours, with the
## rounds taken and Old Man at the back wall. No DoL trace to check against: the route was rewritten
## straight in Ren'Py (game/wolfpack/PLAN.md). Not run until the route has its art (the owner,
## 2026-11-12: walks once a route has art).

testcase wolfpack_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Getting Bred', 'Walk faster', 'Kick back at him', "He's still hard", 'Order him off', 'Yell their names', 'They queue up again', 'Order them off', 'Wake him with your mouth', 'Tell him about the survey', "Grey's got your tail", "Tell him you're running", 'Shove up against', 'Order him deeper', 'Bramble, slow', 'Fold your hands', 'One more round', 'Give them orders', 'Kneel behind him', 'Let the whole forest', 'Stay. The den', 'The alpha, up from', 'Tell him harder']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wlf.ending == "den" and wlf.epilogue == "stay" and wlf.row == "6" and wlf.tier == 6 and wlf.she and wlf.bred and wlf.born and wlf.round1 and wlf.round2 and wlf.round3 and wlf.round5 and wlf.flip3 and wlf.wall == "Alpha")

testcase wolfpack_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Getting Bred', 'Stop dead', 'Swear at him', 'Let him do whatever', 'Try to get up', 'Lie there dripping', 'Wake him with your hand', 'Just grin', 'Collapse on your new hides', 'Tell him exactly whose pace', 'Tease him', 'Notch, fast', 'Grin at him with every fang', 'Let them carry you', 'Bend at the waist', 'Tell him all of it', 'Walk out on your own feet']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wlf.ending == "den" and wlf.epilogue == "go" and wlf.met == "turn" and not wlf.round1 and not wlf.round5 and wlf.flip3 is None and wlf.nights == "Notch")

testcase wolfpack_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ['Getting Bred', 'Walk faster', 'Claw at the furs', "He's still hard", 'Scream for anybody', 'Yell their names', 'They queue up again', 'Growl at them', 'Wake him by grinding', 'Tell him straight', "Grey's got your tail", 'Mock him', 'Shove up against', 'Let the moan out', 'Grey, because', 'Tell him about the survey, one last', 'One more round', 'Yell it at the roof', 'Kneel behind him', 'Ask for the knot', 'Stay. The den', 'Old Man', 'Let the moan out']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wlf.ending == "den" and wlf.epilogue == "stay" and wlf.wall == "Old Man" and wlf.how1 == "claw" and wlf.say7 == "moan" and wlf.gil2 == "survey")
