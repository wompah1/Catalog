## Vote played through by Ren'Py's test runner (tools/rptest.sh). Two walks a path: a takes the first
## of every menu, b the others. No DoL trace to check against: the route was written straight in
## Ren'Py from its two packages (game/vote/PLAN.md).

testcase vote_teal_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Best Girl', 'Watch it again', 'mind his own', 'teal', 'Watch it again', 'Apologise', 'Watch it again', 'Apologise', 'Watch it again', 'Apologise', 'Apologise', 'Watch it again', 'Apologise']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase vote_teal_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Best Girl', 'Close the app', 'Say sorry', 'teal', 'Close the app', 'Ask nicely', 'Close the app', 'Thank him', 'Watch it again', 'Ask nicely', 'Thank him', 'Close the app', 'Thank him']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase vote_red_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Best Girl', 'Watch it again', 'Say sorry', 'red', 'Watch it again', 'Trash-talk', 'Watch it again', 'Trash-talk', 'Watch it again', 'Trash-talk', 'Trash-talk', 'Watch it again', 'Trash-talk']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase vote_red_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Best Girl', 'Close the app', 'mind his own', 'red', 'Close the app', 'Demand', 'Close the app', 'Grin', 'Close the app', 'Demand', 'Grin', 'Watch it again', 'Grin']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
