## The Pink Ranger played through, start to finish, by Ren'Py's own test runner (tools/rptest.sh).
## Walk a: a loss at every rung (the Monkey, Ironjaw, the Siren, the Serpent, Magnavore, the first
## Leviathan), the right reads elsewhere, the Bramblemaw's root, the Nova titjob, Stay and the
## lockers. Walk b: the wrong reads, "Stop fighting it" into the vines, the other flavour picks,
## the bra instead of the titjob, Go. The global teardown that closes the game is in redlightning.rpy.

testcase corps_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['My Pink Hair', "IT'S MORPHING TIME!", 'Draw the bow', 'Morph', 'Stop fighting it', 'Clamp your mouth shut', 'Morph', 'Contain the splinters', 'Morph again', 'Contain the splinters', 'Morph', 'Stop fighting it', 'Shove at him', 'Morph', 'Cut the anchor lines', 'Morph again', 'Cut the anchor lines', 'Morph', 'Stop fighting it', 'Glare up at him', 'Morph', 'Burn the root', 'The suit lets go', 'The vines go in', '...Fine.', 'Morph', 'Stop fighting it', 'Clamp your mouth shut', 'Morph', 'Blind the lens', 'Morph', 'Stop fighting it', 'Shove at him', 'Out the door', 'Scream it', 'Grab the sheets', 'Morph', "Do something you've never done", 'Grab the edge of the bench', 'Kiss the tip first', 'Morph', 'Stop fighting it', 'Glare up at him', 'Morph again', 'Pace it', 'Morph', 'Pace it', 'Morph again', 'Pace it', 'Breathe', 'Twist it free', 'Pull her joggers down', 'Stay on the roster', 'Hold on to the locker door']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase corps_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['My Pink Hair', "IT'S MORPHING TIME!", 'Shout at it', 'Morph', 'Chase it up the scaffold', 'Morph', 'Shatter it', 'Morph again', 'Wait for it to land', 'Morph', 'Overwhelm the plate', 'Morph', 'Cut yourself free', 'Morph again', 'Let it lift you', 'Morph', 'Cover your ears', 'Morph', 'Stop fighting it', 'The suit lets go', 'The vines go in', 'Snatch them', 'Morph', 'Break the coil at the head', 'Morph', 'Play to the camera', 'Morph', 'Hold the plate on', 'Out the door', 'Whisper it', 'Bite the pillow', 'Morph', 'Refuse to look at it', 'Kick at her shins', 'Look up at her', 'Morph', 'Hit it with everything', 'Morph again', 'Let the others carry', 'Morph', 'Hit it with everything', 'Morph again', 'Hit it with everything', 'Wrap your legs round her', 'Twist it free', 'Just make her buy you a bra', 'Go back to the bike shop']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
