## I Went Undercover in the Pervert Tower played through by Ren'Py's test runner (tools/rptest.sh).
## Walk a takes the first scuffle move each Friday and goes up in the lift; walk b the second and
## hangs up the hood; walk c mixes the struggle menus. No DoL trace to check against: the route was
## rewritten straight in Ren'Py (game/boytoy/PLAN.md). Not run until the route has its art (the
## owner, 2026-11-12: walks once a route has art).

testcase boytoy_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['I Went Undercover', 'Sweep the leg', 'Shove off the wall', 'Vault the bar', 'Pull off to protest', 'Bolt for the lift', 'Push up off', 'Go for the sweep', 'Push the microphone', 'Armlock', 'Push at his chest', 'Put your fists down', 'Up in the lift']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (boy.ending == "mask" and boy.epilogue == "stay" and boy.row == "6" and boy.mask == "birdcage")

testcase boytoy_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['I Went Undercover', "Citizen's arrest", 'Read him his rights', 'waistcoat pocket', 'Push at his thighs', 'Absolutely not', 'Order her', 'Unmask the villain', 'sting', 'Go for the menu', 'VIPs are evidence', 'Put your fists down', 'Hang up the hood']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (boy.ending == "mask" and boy.epilogue == "go")

testcase boytoy_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 140.0
    $ renpy.session["vn_picks"] = ['I Went Undercover', 'Sweep the leg', 'Call for backup', 'Vault the bar', 'Glare up', 'Bolt for the lift', 'Kick at her', 'Go for the sweep', "Grab the chair", 'Armlock', 'Kick your heels', 'Put your fists down', 'Up in the lift']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (boy.ending == "mask" and boy.epilogue == "stay")
