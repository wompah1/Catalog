## My Sugar Daddy Found Out…, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every first
## choice, walk b every second. One ending (the package's).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase conrad_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["My Sugar Daddy Found Out I'm Not a Girl and Had Me Made Properly", 'Back toward the door', 'Invoice Marcus', 'Complain about the cost', 'Push his hand away', '"The other three would find out"']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cnr.chapter == 7 and cnr.ending == "settled" and cnr.broke and cnr.asked and cnr.row == "6" and cnr.invoice == "marcus")

testcase conrad_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["My Sugar Daddy Found Out I'm Not a Girl and Had Me Made Properly", 'Tell him the rule again', 'Ask Terrence for the rent', 'Complain about the dinners', 'Cover yourself', '"The clinic isn\'t finished"']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cnr.chapter == 7 and cnr.ending == "settled" and cnr.excuse == "clinic" and cnr.gripe == "dinners")
