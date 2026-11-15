## My Class Is [Bait]…, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every first choice,
## walk b every second. One ending (the package's court). Rebuilt for the production rewrite (2026-11-13).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase bait_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 200.0
    $ renpy.session["vn_picks"] = ["My Class Is [[Bait]…", 'Inch it up, carefully', 'Scramble backwards', 'A quarter turn, and wait', 'Try to swim out', '"Free."', 'The orcs', '"Put me down!"', 'Bar the door', "Hold on to 'no'", 'How do I stop?', 'Plainly', '"No."', 'Rule for the harpy', 'Grant it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (bai.chapter == 11 and bai.ending == "court" and bai.broke and bai.asked and bai.row == "9" and bai.ruling == "grant" and bai.panic == "inch" and bai.free == "free" and bai.ruled == "orcs" and bai.ask == "plain" and bai.ruling2 == "harpy")

testcase bait_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 200.0
    $ renpy.session["vn_picks"] = ["My Class Is [[Bait]…", 'Slam it, and hope', 'Try to reason with her', 'Half, and see what happens', 'Hold your breath and wait', '"Free (?)"', 'The lamia', 'Hold on and say nothing', 'Point at the dial', 'Let it go', 'How did you stop?', 'Begging', '"Not you. Not yet."', 'Rule for the kobolds', 'Deny it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (bai.chapter == 11 and bai.ending == "court" and bai.dial == "half" and bai.maren == "how" and bai.ruling == "deny" and bai.panic == "slam" and bai.free == "query" and bai.ruled == "lamia" and bai.ask == "beg" and bai.ruling2 == "kobolds")
