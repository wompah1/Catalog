## The Manager Wears the Skirt, and Every Alumna Is a Woman played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a does duties most days and takes every optional round, then next season;
## walk b goes straight to each day's rung, skips the rounds and hands in the file; walk c mixes the
## duties and the objections. No DoL trace to check against: the route was rewritten straight in
## Ren'Py (game/club/PLAN.md). First run 2026-11-15 once the art was in: the plans gained the rung-6 balcony menu, and walk
## c's tea_pour check reads the second tea service (Keep your mouth shut), which overwrites the first.

testcase club_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Manager Wears', 'That is NOT', 'Tea service', 'Keep your mouth shut', 'Pull off and demand', 'Towel duty', 'The regimen', 'Get on the minibus', 'Grip the stone', 'Practice with the captain', 'Home for the night', 'Road duty (the qualifiers)', 'Reciprocal', "Tell him it's an instruction", 'Tea with Iris', 'The inspection', 'There is NO round two', 'Demand they let go', 'The slump', 'Hands in his hair', 'Tell him to keep going', 'Yes.', 'Ask for rougher', 'Road duty (an away fixture)', 'Practice with the captain', 'Stay after, with him', 'Give him an instruction', 'Home for the night', 'Nationals', 'filing system', 'Tell him not to stop', 'Next season']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (clb.ending == "banquet" and clb.epilogue == "stay" and clb.row == "6" and clb.tier == 6 and clb.speech == "filing")

testcase club_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Manager Wears', 'filing a COMPLAINT', 'Get on the minibus', 'NOT page five', 'Towel duty', 'Home for the night', 'Road duty (the qualifiers)', 'Fix your skirt', 'The inspection', "You're last", 'The slump', 'Hands on the net post', 'Just moan', 'Yes.', 'Push back on him', 'Home for the night', 'Nationals', 'For the buffet', 'Tell him to look at you', 'Hand in the file']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (clb.ending == "banquet" and clb.epilogue == "go" and clb.speech == "line")

testcase club_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Manager Wears', 'Get OUT of the', 'Tea service', 'Keep pouring', 'Mock them', 'Get on the minibus', 'Grip the stone', 'Road duty (an away fixture)', 'Home for the night', 'Practice with the captain', 'Road duty (the qualifiers)', 'Reciprocal', 'Just say it', 'Tea service', 'Keep your mouth shut', 'Object by section', 'The inspection', 'There is NO round two', 'Scream an objection', 'The slump', 'Hands in his hair', 'Just moan', 'Yes.', 'Ask for a time-out', 'Tea with Iris', 'Towel duty', 'Home for the night', 'Nationals', 'thank the laundry', 'Tell him to look at you', 'Next season']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (clb.ending == "banquet" and clb.epilogue == "stay" and clb.speech == "laundry" and not clb.tea_pour)
