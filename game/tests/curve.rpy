## The Compound Only Binds During Orgasm, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes
## every first choice, walk b every second. One ending (the package's).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase curve_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["The Compound Only Binds During Orgasm", 'Refuse', 'Argue the sleep schedule', "Tell her you'll report her", 'Grip the bench and refuse', 'Try to say "drug"', 'Read them out loud']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (crv.chapter == 6 and crv.ending == "yours" and crv.row == "6" and crv_pc_name == "Callie" and crv.term == "sleep" and crv.dean == "drug")

testcase curve_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["The Compound Only Binds During Orgasm", 'Try to bargain', 'Argue the wardrobe', 'Just say no', "Tell her it won't fit", 'Try to say "Greer"', 'Look away']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (crv.chapter == 6 and crv.ending == "yours" and crv.rows == "away" and crv.shout3 == "fit")
