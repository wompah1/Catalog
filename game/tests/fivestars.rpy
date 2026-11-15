## I Read the Tier Requirements played through by Ren'Py's test runner (tools/rptest.sh). Walk a
## takes every optional scene and stays on the manifest; walk b lets every lead call it off and
## hands in the keys; walk c mixes the struggle lines and stays. No DoL trace to check against: the
## route was rewritten straight in Ren'Py (game/fivestars/PLAN.md).

testcase fivestars_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Read the Tier Requirements', 'road closures', 'Kind regards', 'Grab the pallet edge', 'Grab the rug', 'Grip the rail', 'Warm regards', 'by the book', 'Claw at the carpet', 'Yours faithfully', 'Brace on the shrink-wrap', 'Clamp your knees', 'Grip the counter', 'Put me down for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (fs.ending == "ambassador" and fs.epilogue == "stay" and fs.body == 6)

testcase fivestars_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Read the Tier Requirements', 'best tippers', 'Many thanks', 'Regan zips up', 'Jodie lets you up', "scanner's stop", 'With thanks', 'smiley face', 'argues itself out', 'Looking forward', 'clipboard', 'AMBASSADOR, not', 'headset', 'Hand in the van keys']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (fs.ending == "ambassador" and fs.epilogue == "go" and fs.body == 6)

testcase fivestars_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Read the Tier Requirements', 'road closures', 'Kind regards', 'OFF the clock', 'clause says PARCEL', 'NOT a fit check', 'Warm regards', 'by the book', 'every ITEM', 'Yours faithfully', 'STAFF, Regan', 'Push up off', 'QUESTIONS', 'Put me down for it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (fs.ending == "ambassador" and fs.epilogue == "stay")
