## Worst Host on the Men's Floor, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes every
## first choice and signs (the book's ending); walk b every second and takes the men's floor (new writing).
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase camellia_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Worst Host on the Men's Floor", 'Say no', '"Rina."', 'Do it her way', 'Order the shochu', 'Push him off', 'Grip the table and refuse', "\"If it's a cage, lock it.\"", 'Toast her sweetly', "\"Maybe I like that it doesn't come off.\"", 'Ask Kurosawa for a contract']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cam.chapter == 5 and cam.ending == "sign" and cam.asked and cam.row == "3" and cam_pc_name == "Rina" and cam.order == "shochu" and cam.name1 == "rina" and cam.drill2 == "hers")

testcase camellia_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Worst Host on the Men's Floor", 'Turn your face away', "\"Whatever you'd like it to be.\"", 'Do it your way', 'Order tea', "Tell him what's under the dress", 'Tell her to stop', "\"If it's a cage, lock it.\"", 'Toast the new number one', "\"It comes off. You'll never see it.\"", 'Call Ichinose']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cam.chapter == 5 and cam.ending == "take" and cam_pc_name == "Ryo" and cam.toast == "crown" and cam.domoto == "never" and cam.name1 == "yours" and cam.drill2 == "yours")

## Walks c and d: walks a and b on MAKE IT REAL (the alternate route, 2026-11-13): Sign a year on, and Take with a binder.
testcase camellia_c:
    $ _test.transition_timeout = 0.05
    $ store.CAM_REAL_READY = True  # the lane is gated off until its art lands (nqalt/130); the walk opens it to keep the script checked
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Worst Host on the Men's Floor", 'Say no', '"Rina."', 'Do it her way', 'Order the shochu', 'Push him off', 'Grip the table and refuse', 'make it so nobody can poach me', 'Toast her sweetly', "\"Maybe I like that it doesn't come off.\"", 'Ask Kurosawa for a contract']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cam.real and cam.grown == 2 and cam.ending == "sign" and cam.asked)

testcase camellia_d:
    $ _test.transition_timeout = 0.05
    $ store.CAM_REAL_READY = True  # the lane is gated off until its art lands (nqalt/130); the walk opens it to keep the script checked
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ["Worst Host on the Men's Floor", 'Turn your face away', "\"Whatever you'd like it to be.\"", 'Do it your way', 'Order tea', "Tell him what's under the dress", 'Tell her to stop', 'make it so nobody can poach me', 'Toast the new number one', "\"It comes off. You'll never see it.\"", 'Call Ichinose']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (cam.real and cam.grown == 1 and cam.ending == "take" and cam_pc_name == "Ryo")
