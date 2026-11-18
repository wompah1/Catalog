## Rook played through by Ren'Py's test runner (tools/rptest.sh). Three walks, one per flavour set.
## Written straight in Ren'Py (game/senseless/PLAN.md). Walks run once its art lands.

testcase senseless_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Senseless', 'Hold the door for her', 'Tell her the truth', 'The chest rune', 'Say thank you', 'The chest rune', 'Let her hear', 'The hip rune', 'Ask her why', 'The chest rune', 'Call her name', 'The nipple rune', 'Tell her why you raced her', 'The chest rune', 'Beg her for more', 'Climb out']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase senseless_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Senseless', 'Blow her a kiss', 'Tell her it was nothing', 'The cock rune', 'Make her feed you', 'The mouth rune', 'Bite it back', 'The cock rune', 'Swear at her', 'The mouth rune', 'Call her a cheat', 'The cock rune', 'Keep it a joke', 'The hip rune', 'Dare her to do worse', 'Stay in']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))

testcase senseless_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['Senseless', 'Blow her a kiss', 'Tell her the truth', 'The mouth rune', 'Make her feed you', 'The hip rune', 'Let her hear', 'The nipple rune', 'Swear at her', 'The hip rune', 'Call her name', 'The mouth rune', 'Keep it a joke', 'The hip rune', 'Beg her for more', 'Stay in']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
