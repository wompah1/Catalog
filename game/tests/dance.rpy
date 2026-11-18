## Aren played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/dance/PLAN.md). Walks run once its art lands.

testcase dance_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Sealing Dance', 'Take up her veils', 'Take her place', 'Tell Lys the truth', 'Fight the crest', 'Stay with Senna', 'Beg Senna to stop', 'Let Lys hold you', 'Count the strokes', 'Try the counter-ward', 'Say no', 'Close your eyes', 'Follow Lys', 'Dance with Lys']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase dance_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Sealing Dance', 'Call for the priestess', 'Draw your sword', 'Hide it from Lys', 'Let it carry you', 'Give her privacy', 'Let Senna go on', 'Pull away from Lys', 'Lose count', 'Hide in the temple', 'Say please', 'Look at the crowd', 'Take the lead', 'Dance for them']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase dance_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['The Sealing Dance', 'Take up her veils', 'Draw your sword', 'Hide it from Lys', 'Fight the crest', 'Give her privacy', 'Let Senna go on', 'Let Lys hold you', 'Lose count', 'Try the counter-ward', 'Say please', 'Look at the crowd', 'Follow Lys', 'Dance for them']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
