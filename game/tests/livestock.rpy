## Marsh Farm Filed Me as a Heifer played through by Ren'Py's test runner. Walk a: both optional "Again."
## scenes, Buttercup's trade, Marigold's taste, every chore and every fight and milking pick, Stay.
## Walk b: no optional scenes, the other picks, Go. Rewritten straight in Ren'Py: no DoL trace.

testcase livestock_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Marsh Farm Filed Me', 'Struggle', 'The mud pen', "She isn't asking", 'Swear', 'The ring walk', 'Struggle', 'Grit your teeth', 'Watching Marigold', 'Swear', 'Struggle', 'The mud pen', 'Grit your teeth', 'Swear', 'The ring walk', 'Struggle', 'Grit your teeth', "She doesn't let go", 'Your hips swing', 'Buttercup latches on', 'Struggle', 'She spreads your knees', 'Swear', 'Grit your teeth', 'Stay']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase livestock_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Marsh Farm Filed Me', 'Swear', 'Watching Marigold', 'She lets go of your jaw', 'Grit your teeth', 'The mud pen', 'Swear', 'Struggle', 'The ring walk', 'Grit your teeth', 'Swear', 'Watching Marigold', 'Struggle', 'Grit your teeth', 'The mud pen', 'Swear', 'Struggle', 'She lets go: wipe off', 'A moo gets out', 'The trailer rolls home', 'Swear', 'She lets you lie there', 'Grit your teeth', 'Struggle', 'Go']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
