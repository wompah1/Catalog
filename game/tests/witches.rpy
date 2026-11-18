## I Was Sent In to Clear the Witches Out played through by Ren'Py's test runner (tools/rptest.sh).
## Walk a gives in at the last stroke and stays in the wing; walk b keeps saying no (End Pet); walk c
## gives in and keeps a place in town. No DoL trace to check against: the route was rewritten
## straight in Ren'Py (game/witches/PLAN.md). Not run until the route has its art (the owner,
## 2026-11-12: walks once a route has art).

testcase witches_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Was Sent In', 'Fling the salt', 'Grab the bedframe', 'Empty half', 'Shove at her shoulders', 'Level the pistol', 'Pull your wrists', 'Squeeze the handle', 'Yank at the ribbon', 'Take a run', 'Push up off', 'Try to look away', 'Close your eyes', "The coven's newest"]
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wit.ending == "witch" and wit.epilogue == "stay" and wit.row == "6" and wit.fit == "witch")

testcase witches_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Was Sent In', 'Read her the site rules first', 'Blow the whistle', 'armed first', 'shout for Rufus', 'Read her the site rules', 'Kick the desk', 'Count her in', 'Order her', 'Read her the site rules first', 'Swear at her', 'Shove at her shoulders', 'Keep saying no']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wit.ending == "pet" and wit.epilogue == "pet" and wit.fit == "pet")

testcase witches_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 120.0
    $ renpy.session["vn_picks"] = ['I Was Sent In', 'Fling the salt', 'Read her her rights', 'Empty half', 'Swear at her', 'Level the pistol', 'Yell for Rufus', 'Squeeze the handle', 'Kick your heels', 'Take a run', 'Shout the site rules', "trespassing", 'Close your eyes', 'Days in town']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wit.ending == "witch" and wit.epilogue == "go")
