## Venus and Mars played through, start to finish, by Ren'Py's own test runner (tools/rptest.sh). Every pick is
## covered across the walks, both endings, and every branch of the production-pass state (2026-11-13): ve.extra
## (the showier option, nine times: Holly's tally on day seven, Wade on day fourteen), the wink (Mia's scissors),
## the spa door, the plait or updo (the wrap), and the door watched after Simon (the stairwell).
## Walk a: extra 1, the spa eye, winked at Holly, the plait, the door not watched, Stay (the delivery card).
## Walk b: extra 7, floated upstairs, winked at Mia, the updo, the door watched, Go with Simon (the office card).
## Walk c: as walk a's state, the flight card, Stay.
## the suite. The global teardown that closes the game is in redlightning.rpy.

testcase venus_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['Porn Star Training', 'Bag the back seat', 'Swagger through', 'Hold her eye', 'Down it in one', 'Wink at Holly', 'Hold your cup out', 'Ask Mia for a plait', 'Lick it off', 'Kick your feet', 'Open up wider', 'Kneel like you own', 'Squeeze them round it', 'Let it', 'Push down', 'Let it in', 'The card on the left', 'Let the towel slip', 'Get on your knees', 'Turn over for him', 'Hold your knees', 'Wrap your breasts', 'Ride him', 'headliner, obviously', 'Stay for the next intake', 'Climb on']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (ve.extra == 1 and ve.spa == "eye" and ve.wink == "holly" and ve.hair == "plait" and not ve.door)

testcase venus_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['Porn Star Training', 'Take the window seat', 'Wink at her', 'Float back upstairs', 'Raise it to the table', 'Wink at Mia', 'Lick the rim', 'Ask Mia to put it up', 'Leave it.', 'Watch the door', 'Open up', 'Arch your back', 'Tease the room', 'Beg her not to stop', 'Look at Holly', 'Let it in', 'The card in the middle', 'Drop your pen', 'Curl up next to him', 'A note under the door', 'Wrap your breasts', 'Ride him', 'seen, wanted, first', 'Go with Simon']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (ve.extra == 7 and not ve.spa and ve.wink == "mia" and ve.hair == "up" and ve.door)

testcase venus_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 240.0
    $ renpy.session["vn_picks"] = ['Porn Star Training', 'Bag the back seat', 'Swagger through', 'Hold her eye', 'Down it in one', 'Wink at Holly', 'Hold your cup out', 'Ask Mia for a plait', 'Lick it off', 'Kick your feet', 'Open up wider', 'Kneel like you own', 'Squeeze them round it', 'Let it', 'Push down', 'Let it in', 'The card on the right', 'Do the safety', 'Get on your knees', 'A note under the door', 'Wrap your breasts', 'Ride him', "stacked, starring, Simon's", 'Stay for the next intake', 'Kiss him and save it']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (ve.extra == 1 and ve.spa == "eye" and ve.wink == "holly" and ve.hair == "plait" and not ve.door)
