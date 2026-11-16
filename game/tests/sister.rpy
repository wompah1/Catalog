## Little Sister Mode played through by Ren'Py's test runner. Walk a: Tell at rung 4, every optional
## scene, a chore every night, Keep it. Walk b: Quiet (the fridge), no optional scenes, no chores,
## Delete it. Rewritten straight in Ren'Py: no DoL trace.

testcase sister_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Little Sister Mode', 'Ten minutes. Then', 'Keep your hand moving', 'Make the tea', 'Flop down next to her', 'Go round again', 'Help with the morning problem', 'My turn to pick', 'Bath night with big sis', 'Flop down next to her', 'Ask for a second coat', 'Sisters share everything', 'Paige. What is this', 'Run it', 'Again, to be sure', 'Big sister', 'Sit down next to her', 'Again, slower', 'Set the pace', 'Keep it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase sister_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Little Sister Mode', 'Go on, then', 'Rinse her off', 'Not tonight', 'My turn to pick', 'Breakfast', 'Not tonight', 'Flop down next to her', 'Not tonight', 'Flop down next to her', 'Let her pat it in', 'Not tonight', 'Close it. Put it back', 'Write it on the rota', 'Not tonight', 'Run it', 'Stay on her chest', 'Not tonight', 'Delete it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
