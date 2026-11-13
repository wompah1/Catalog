## Open and Listen played through, start to finish, by Ren'Py's own test runner (tools/rptest.sh).
## The three walks make the choices the DoL traces made (tools/trace_dol.py hypno: "first", "alt",
## and "first" with the Go epilogue), so tools/check.py can compare the screens line by line. The
## plan's first snippet picks the route card by its title; the menus take the rest by themselves
## (vn_test_pick). The global teardown that closes the game is in redlightning.rpy.

testcase hypno_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Say sorry, badly', 'Fold his laundry for him', 'Sit on the end of the bed', 'Just a little', 'Sit on the end of the bed', 'Kneel on the carpet and wait', 'Keep them pushed together for him', 'Kneel on the carpet and wait', 'Take his arm', 'Stay on your knees for him', 'Kneel on the carpet and wait', 'Wake her. Tell her everything.', 'Stay']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

## Walk a's path in the Abarus art set (hypno.js artSets; the HUD's Art button): every picture on
## the way comes from art/hypno.abarus/ where it has one, so a missing or broken file fails here.
testcase hypno_a_abarus:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Say sorry, badly', 'Fold his laundry for him', 'Sit on the end of the bed', 'Just a little', 'Sit on the end of the bed', 'Kneel on the carpet and wait', 'Keep them pushed together for him', 'Kneel on the carpet and wait', 'Take his arm', 'Stay on your knees for him', 'Kneel on the carpet and wait', 'Wake her. Tell her everything.', 'Stay']
    run Start()
    advance until eval (store.vn_route == "hypno")
    $ store.vn_art = {"hypno": "abarus"}
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (store.vn_art.get("hypno") == "abarus" and vn_art_file("art/hypno/bedroom.jpg") == "art/hypno.abarus/bedroom.jpg")

testcase hypno_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Go and shower', 'Do the washing-up first', 'Keep scrolling your phone', 'Just a little', 'Keep scrolling your phone', 'Go to his door', 'Keep them pushed together for him', 'Go to his door', 'Walk half a step ahead', 'Stay on your knees for him', 'Go to his door', "Don't."]
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase hypno_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Say sorry, badly', 'Fold his laundry for him', 'Sit on the end of the bed', 'Just a little', 'Sit on the end of the bed', 'Kneel on the carpet and wait', 'Keep them pushed together for him', 'Kneel on the carpet and wait', 'Take his arm', 'Stay on your knees for him', 'Kneel on the carpet and wait', 'Wake her. Tell her everything.', 'Go, one door down the landing']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

## The full regimen (owner, 2026-11-11): walk a's and walk b's paths with Emily asking the Bloom for
## everything. No DoL trace to check them against (the branch is Ren'Py's own); the walks prove
## every passage plays, the branch holds to the end, and every picture shown has its full twin.
testcase hypno_d:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Say sorry, badly', 'Fold his laundry for him', 'Sit on the end of the bed', 'More. All of it.', 'Sit on the end of the bed', 'Kneel on the carpet and wait', 'Keep them pushed together for him', 'Kneel on the carpet and wait', 'Take his arm', 'Stay on your knees for him', 'Kneel on the carpet and wait', 'Wake her. Tell her everything.', 'Stay']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase hypno_d_abarus:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Say sorry, badly', 'Fold his laundry for him', 'Sit on the end of the bed', 'More. All of it.', 'Sit on the end of the bed', 'Kneel on the carpet and wait', 'Keep them pushed together for him', 'Kneel on the carpet and wait', 'Take his arm', 'Stay on your knees for him', 'Kneel on the carpet and wait', 'Wake her. Tell her everything.', 'Stay']
    run Start()
    advance until eval (store.vn_route == "hypno")
    $ store.vn_art = {"hypno": "abarus"}
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase hypno_e:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['Open and Listen', 'Go and shower', 'Do the washing-up first', 'Keep scrolling your phone', 'More. All of it.', 'Keep scrolling your phone', 'Go to his door', 'Keep them pushed together for him', 'Go to his door', 'Walk half a step ahead', 'Stay on your knees for him', 'Go to his door', "Don't."]
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
