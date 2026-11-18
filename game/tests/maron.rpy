## Maron played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/maron/PLAN.md). Walks run once its art lands.

testcase maron_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Onee-sama's Maid", 'Knock', 'Accept her hospitality', 'Say your real name', 'Beg her', 'Look away', 'Take your mouth back', 'Write your name', 'Hold still', 'Run for the trees', 'Apologise', 'Tell her to give it back', 'Hold the reins', 'Let go']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase maron_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Onee-sama's Maid", 'Shout for help', 'Ask to leave at dawn', 'Answer to Maron', 'Grit your teeth', 'Keep looking', 'Let her talk', 'Ask Kanon', 'Push into her hand', 'Take a coat first', 'Defy her', 'Ask her who she is', 'Let her ask', 'Stay with her']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase maron_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Onee-sama's Maid", 'Knock', 'Ask to leave at dawn', 'Say your real name', 'Grit your teeth', 'Look away', 'Let her talk', 'Write your name', 'Push into her hand', 'Run for the trees', 'Defy her', 'Ask her who she is', 'Hold the reins', 'Stay with her']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
