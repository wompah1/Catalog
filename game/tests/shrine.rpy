## I'm Possessed by a Horny Fox Goddess... played through by Ren'Py's test runner (tools/rptest.sh).
## Walk a takes every first choice (holding them still every round, so the solo runs its longest:
## three rounds won, never the scene; Slate slow; Stay); walk b every second (letting them, so the
## solo is shortest; Slate quick; Take the key); walk c every third, with the solo alternating hold
## and let. No DoL trace to check against: the route was rewritten straight in Ren'Py
## (game/shrine/PLAN.md). Not run until the route has its art (the owner, 2026-11-12: walks once a
## route has art).

testcase shrine_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['Horny Fox Goddess', 'Hold them still', 'Hold them still', 'Hold them still', 'Hold them still', 'Hold them still', 'Hold them still', 'Hold them still', 'Hold them still', 'Order them both off', 'Snarl round him', 'Fight her for your hips', 'Slate, slow', 'Mock him', 'Shout over her', 'Swear at her round him', 'Ride him harder', 'Stay at the shrine']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (shr.ending == "reins" and shr.epilogue == "stay" and shr.row == "7" and shr.reins == 7 and shr.she and shr.held == 3 and shr.turn == 8 and shr.slate == "slow")

testcase shrine_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['Horny Fox Goddess', 'Let them', 'Let them', 'Let them', 'Let them', 'Plead with them', 'Mock them', 'Order your tail down', 'Slate, quick', 'Clamp a hand', 'Pull off and give orders', 'Tease the gate', 'Take the key']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (shr.ending == "reins" and shr.epilogue == "go" and shr.held == 0 and shr.turn == 4 and shr.slate == "quick")

testcase shrine_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['Horny Fox Goddess', 'Hold them still', 'Let them', 'Hold them still', 'Let them', 'Hold them still', 'Let them', 'Scream for anybody', 'Apologise to the hill', 'Plead with Flint', 'Slate, slow', 'Beg somebody', 'Plead with Slate', 'Growl at the stars', 'Make him say yes', 'Stay at the shrine']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (shr.ending == "reins" and shr.epilogue == "stay" and shr.held == 3 and shr.turn == 6 and shr.say7 == "ask")
