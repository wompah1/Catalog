## She Booked Me Into the Women-Only Resort as Ellie, played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a takes every first choice, walk b every second. Each checks the six days ran:
## the card fully booked, a no said every day to 5, the break at day 4, the walk-out at day 5, and the
## upgrades. Walk c is walk a on THE DELUXE (the alternate route, 2026-11-13): the sixth upgrade, the
## Upper Contour's no, the chest grown twice. Rebuilt for the production rewrite (2026-11-13). Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase hollowpine_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Resort as Ellie', '"Elliot. Ellie\'s just the booking."', 'Explain it clinically', "Book it, it's better value", 'Argue with it', "Ask how far it's meant to go", 'Say it round her', 'Book one infusion', "Tell her it's a mistake", 'Draw her the diagram', 'The soft wrap dress', 'Tell her you said skip', 'Stay on the current protocol', 'Tell her all four years', 'Ask them to stop', 'Go back inside', 'Tell her the truth']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hol.booked == 7 and hol.said_no == 5 and hol.broke and hol.walked and hol.row == "7" and hol.upgrades == 2 and hol.back == "soon" and hol.frank == "truth" and hol.name1 == "elliot" and hol.hyd2 == "ask" and hol.sell3 == "diagram" and hol.confess5 == "years" and not hol.deluxe)

testcase hollowpine_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Resort as Ellie', '"Ellie\'s fine."', 'Grab the edge of the table', "Ask what's in it, then book it", 'Ask how to improve it', 'Just go for it', 'Push at her thighs', 'Book one, ask about a discount', 'Try to get off the table', 'Just show her', 'The leggings and the long jumper', 'Clamp your thighs to stop her', 'Stay on the current protocol', 'Just ask her out', 'Ask for Casey only', 'Sit in the car a while longer', 'Tell her the truth, and upgrade']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hol.booked == 7 and hol.said_no == 5 and hol.broke and hol.upgrades == 3 and hol.back == "later" and hol.wear4 == "leggings" and hol.shout5 == "casey" and hol.name1 == "ellie" and hol.hyd2 == "go" and hol.sell3 == "show" and hol.confess5 == "ask" and not hol.deluxe)

testcase hollowpine_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 220.0
    $ renpy.session["vn_picks"] = ['Resort as Ellie', '"Elliot. Ellie\'s just the booking."', 'Explain it clinically', "Book it, it's better value", 'Argue with it', "Ask how far it's meant to go", 'Say it round her', 'Book one infusion', "Tell her it's a mistake", 'Draw her the diagram', 'The soft wrap dress', 'Tell her you said skip', 'Book the Deluxe', 'Tell her all four years', 'Ask them to stop', 'Go back inside', 'Tell her the truth']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hol.deluxe and hol.grown == 2 and hol.booked == 7 and hol.said_no == 6 and hol.broke and hol.walked and hol.row == "7" and hol.upgrades == 3 and hol.frank == "truth" and hol.confess5 == "years")
