## The Rule Was One Vial a Day. He Supplies the Second., played through by Ren'Py's test runner (tools/rptest.sh).
## Walk a takes every first choice, walk b every second, walk c alternates. One ending (the book's).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase secondvial_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Rule Was One Vial a Day. He Supplies the Second.", 'Take the copper and say nothing', 'Ask if you can sit', 'Push at his chest', 'Refuse', 'Keep the barrel between you', 'A reversal', "Hold on to 'no'", 'Try the street']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (svl.chapter == 10 and svl.ending == "house" and svl.broke and svl.asked and svl.row == "n5" and svl_pc_name == "Serah" and svl.brusk == "silent" and svl.ask == "reversal")

testcase secondvial_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Rule Was One Vial a Day. He Supplies the Second.", 'Tell him where to put it', 'Count your coins alone', 'Clamp your thighs shut', 'Go down, and tell him exactly what you think of him', 'Tell him the price is wrong', 'A cheaper dose, one a day again', 'Let it go', 'Watch from the window']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (svl.chapter == 10 and svl.ending == "house" and svl.brusk == "snap" and svl.supper == "alone" and svl.break6 == "let" and svl.dayoff == "window")

testcase secondvial_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Rule Was One Vial a Day. He Supplies the Second.", 'Take the copper and say nothing', 'Count your coins alone', 'Push at his chest', 'Go down, and tell him exactly what you think of him', 'Keep the barrel between you', 'A cheaper dose, one a day again', "Hold on to 'no'", 'Watch from the window']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (svl.chapter == 10 and svl.shout3 == "push" and svl.shout4 == "tell" and svl.shout5 == "barrel")
