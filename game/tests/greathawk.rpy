## My Escape Rope Was Finished... played through by Ren'Py's test runner (tools/rptest.sh). Walk a
## takes every first choice (Thank him each morning, swearing at him, "Not yet."); walk b every
## second (Scold him, shoving, flying the rucksack to town); walk c every third (Ignore it, going
## silent, "Not yet."). No DoL trace to check against: the route was rewritten straight in Ren'Py
## (game/greathawk/PLAN.md). Not run until the route has its art (the owner, 2026-11-12: walks once a
## route has art).

testcase greathawk_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['My Escape Rope', 'Thank him', 'Fuck your fist', 'Thank him', 'Swear at him till', 'Stare at the wall', 'Fuck off. NO', 'Pull off to tell him', 'Thank him', 'Not that. Not THERE', 'Tell him to get his wings', 'Thank him', "Don't you DARE", 'Order him off', 'Thank him', 'Keep shouting', 'Push up off', 'Thank him', 'Not HERE', 'Tell him to let you go', "I'm not your WIFE", "Shout that you're leaving", 'Not yet.']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (grh.ending == "not-yet" and grh.epilogue == "stay" and grh.row == "8" and grh.rope == 7 and grh.unpicked and grh.called == "wife")

testcase greathawk_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['My Escape Rope', 'Scold him', 'Edge it', 'Scold him', 'Shove back at his chest', 'Count your knots', 'Shove at his thighs', 'Mock him round it', 'Scold him', 'Twist round', 'Beg him', 'Scold him', 'Shove off the side', 'Plead with him', 'Scold him', 'Shove his chest and roll', 'Mock him', 'Scold him', 'Shove his chest and hang', 'Mock him', 'Shove his chest and try', 'Plead with him', 'Fly the rucksack']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (grh.ending == "not-yet" and grh.epilogue == "rucksack" and grh.mood == "edge")

testcase greathawk_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['My Escape Rope', 'Ignore it', 'Fuck your fist', 'Ignore it', 'Lock your jaw', 'Whistle at the sky', 'Clamp your lips', 'Yell for help', 'Ignore it', 'Grab two fistfuls', 'Shove back at him', 'Ignore it', 'Clamp your thighs', 'Scream at the road', 'Ignore it', 'Turn your back', 'Beg him to let you go', 'Ignore it', 'Glare up at him', 'Flap your wings', 'Stare out at the moor', 'Bite his shoulder', 'Not yet.']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (grh.ending == "not-yet" and grh.epilogue == "stay" and grh.no == "silent")
