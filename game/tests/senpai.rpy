## Senpai played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/senpai/PLAN.md). Walks run once its art lands.

testcase senpai_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Senpai's Favourite", 'Ask what it costs', 'Just do it', 'Let him', 'Ask what he likes about you', 'Look at Daigo', 'Put it on', 'Kiss him instead', 'Say nothing']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase senpai_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Senpai's Favourite", 'Just sign', 'Tell Ryota no', 'Tell him to stop', 'Ask what he thinks of Shun', 'Say no to Ryota', 'Refuse the bikini', 'Whisper who you are', 'Tell him who you really are']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase senpai_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ["Senpai's Favourite", 'Ask what it costs', 'Tell Ryota no', 'Let him', 'Ask what he thinks of Shun', 'Look at Daigo', 'Refuse the bikini', 'Kiss him instead', 'Tell him who you really are']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
