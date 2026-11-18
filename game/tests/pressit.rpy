## I Got Caught Peeping played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes the
## first flavour line everywhere, Travis's second round, and "Press it again."; walk b calls it
## blackmail, skips the second round and peels it; walk c mixes the rest. No DoL trace to check
## against: the route was rewritten straight in Ren'Py (game/pressit/PLAN.md). Not run until the
## route has its art (the owner, 2026-11-12: walks once a route has art).

testcase pressit_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Got Caught Peeping', 'Keeper with a bullet', 'Hold still', 'Push your knees', 'Grab her wrist', "Don't stop", 'again', 'Kick', 'now', 'Shove back', 'says Travis', 'what time', 'Shove at her', "Don't listen", 'Press it again']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (prs.ending == "pocketed" and prs.epilogue == "stay" and prs.body == 7 and prs.she and prs.on)

testcase pressit_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Got Caught Peeping', 'Frame that one', 'blackmail', 'Grab her wrists', 'Shove at her shoulder', 'Try to stop', 'do it', 'Grab the waistband', 'please', 'Grab for the door', 'shorts up', 'when', 'Twist out', "Door's open", 'Peel it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (prs.ending == "pocketed" and prs.epilogue == "go" and prs.peeled and prs.office == "blackmail")

testcase pressit_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Got Caught Peeping', 'whistle', 'Hold still', 'Swear at her', 'Grab her wrist', "Don't stop", 'again', 'Kick', 'now', 'Shove back', 'shorts up', 'what time', 'Shove at her', "Don't listen", 'Press it again']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (prs.ending == "pocketed" and prs.epilogue == "stay" and prs.rate == "whistle")
