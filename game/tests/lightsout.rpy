## Sleepover Rules All Weekend…, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every first
## choice, walk b every second. One ending (the package's).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase lightsout_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Sleepover Rules All Weekend, or the Photos Go Out", 'Try to stand', 'Get up', 'Steer toward Jo', 'Wake Jo', '"Thank you!"']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lto.chapter == 6 and lto.ending == "weekend" and lto.broke and lto.asked and lto.row == "6" and lto.woke == "jo")

testcase lightsout_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Sleepover Rules All Weekend, or the Photos Go Out", 'Keep negotiating', 'Stay where you are', "Steer toward 'whoever's closest'", 'Wake Dani', 'Say nothing and hurry past']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (lto.chapter == 6 and lto.ending == "weekend" and lto.dare == "closest" and lto.maam == "hurry")
