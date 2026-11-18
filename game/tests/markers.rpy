## The House Settles Markers played through, start to finish, by Ren'Py's own test runner
## (tools/rptest.sh). Walk a: every floor extra (Tam's table every night, a second hand on night 3,
## Simone's break every night from night 3: oral, titjob, anal, anal), the Stay epilogue and its
## break over the crates. Walk b: the extras skipped, the other flavour picks, the Go epilogue.
## A test walk's hands are dealt with no natural, so each one meets one "Stand". The plan's first
## snippet picks the route card by its title. The global teardown is in redlightning.rpy.

testcase markers_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['The House Settles', 'Stand', 'block capitals', 'Haggle the rate', 'Take it smug',
        'Run drinks', "Sit in at Tam's table", 'Stand', 'Back to your station', 'Play the wheel', 'Take it giddy',
        'Work the roulette rail', "Simone's break", 'Haggle', "Sit in at Tam's table", 'Stand', 'Another hand', 'Stand', 'Back to your station', 'Take the dice', 'Let it ride', 'Press it', 'Let it ride', 'Press it', 'Shove at her hips', 'Take it filthy',
        'Work the craps rail', "Simone's break", 'Grab for the pipes', "Sit in at Tam's table", 'Stand', 'Back to your station', 'Sit in at the poker pit', 'Hand back the pen', 'Not my ass', 'Take it smug',
        'Stand', 'Run drinks', "Simone's break", "That's NOT the rate", "Sit in at Tam's table", 'Stand', 'Back to your station', 'Work the floor till close', 'Take it giddy',
        'Run drinks', "Simone's break", 'Haggle', "Sit in at Tam's table", 'Stand', 'Back to your station', 'Go to the baccarat table', 'Grab the edge of the felt', 'Take it filthy',
        'Even money', "Pull against Simone's grip", 'Stay: a fresh line', 'over the crates', 'Haggle']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)

testcase markers_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['The House Settles', 'Stand', "winner's flourish", 'Try for the door', 'Take it filthy',
        'Work the craps rail', 'Play the wheel', 'Take it smug',
        'Run drinks', 'Take the dice', 'Press it', 'Press it', 'Press it', 'Press it', 'Haggle', 'Take it giddy',
        'Work the roulette rail', 'Sit in at the poker pit', 'Push the book back', 'Haggle', 'Take it filthy',
        'Stand', 'Work the craps rail', 'Work the floor till close', 'Take it smug',
        'Work the roulette rail', 'Go to the baccarat table', "That's NOT the rate", 'Take it giddy',
        'Long odds, his way', "That's NOT the rate", 'Go: the walk']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
