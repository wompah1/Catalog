## Aubin played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/pitfall/PLAN.md). Walks run once its art lands.

testcase pitfall_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Pitfall', 'Take half now', 'Run it down', 'The Lamp of Saint Orrin', 'Correct the thought', 'Purify the air', 'Hold your breath', 'Ask for help', 'Ask her to come for you', 'Say them slowly', 'Start again', 'Pray to the Light', 'Call it the Hollow', 'Stop your ears', 'Sing Matins over it', 'Climb out']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase pitfall_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Pitfall', "Pay me when it's done", 'Follow it softly', 'The Dawn Canticle', 'Let it be pleasant', 'Purify yourself', 'Breathe it in', "Say you're fine", 'Do as she says', 'Say them as they come', 'Leave it there', 'Pray to the warmth', 'Call it Mother', 'Listen', 'Hum along with it', 'Sink back']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase pitfall_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Pitfall', 'Take half now', 'Follow it softly', 'The Dawn Canticle', 'Correct the thought', 'Purify yourself', 'Breathe it in', 'Ask for help', 'Do as she says', 'Say them slowly', 'Leave it there', 'Pray to the warmth', 'Call it the Hollow', 'Listen', 'Sing Matins over it', 'Climb out']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
