## The Bit That Kept Running, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every first
## choice, walk b every second. One ending (the package's).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase bit_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["The Bit That Kept Running", '"It\'s a bit."', 'Laugh it off', 'Back away', 'The lube', "Hold on to 'no'", 'Let them buy the bigger forms', 'Answer her filthily']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (bit.chapter == 6 and bit.ending == "sixteen" and bit.broke and bit.asked and bit.row == "6" and bit_pc_name == "Hana" and bit.extra == "lube")

testcase bit_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["The Bit That Kept Running", '"Go on, then."', 'Say no, properly', '"It\'s not on the list!"', 'The spare panties', 'Let it go', 'Let them buy the bigger forms', 'Answer her filthier']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (bit.chapter == 6 and bit.ending == "sixteen" and bit.nono == "filthier" and bit.extra == "panties")

## Walk c: walk a on BET THEY GROW (the alternate route, 2026-11-13): the bet won by ch 6.
testcase bit_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["The Bit That Kept Running", '"It\'s a bit."', 'Laugh it off', 'Back away', 'The lube', "Hold on to 'no'", 'bet they grow', 'Answer her filthily']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (bit.bet and bit.grown == 2 and bit.chapter == 6 and bit.ending == "sixteen" and bit.asked)
