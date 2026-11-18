## The Women's Bath Makes You One, played through by Ren'Py's test runner (tools/rptest.sh). Walk a takes
## every first choice and closes the men's side (the book's ending); walk b every second and restores it.
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase womensbath_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["Women's Bath Makes You One", 'Shout for Iori', "I didn't go.", 'Agree, flatly', 'Talk to it', "Pretend you didn't see it", 'Tell her to stop', 'Write "Voice: stays."', "They're for my girlfriend", 'Push away', 'Keep it', "Tell her it's too much", "I'm not leaving", 'Close it for good']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wom.chapter == 12 and wom.ending == "close" and wom.broke and wom.asked and wom.row == "12" and wom.bra == "girlfriend" and wom.tell2 == "lie" and wom.write4 == "voice" and wom.note6 == "kept")

testcase womensbath_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["Women's Bath Makes You One", 'Haul at the edge', 'Twenty minutes.', 'Agree, and set the timer first', 'Grab the lip of the tub', 'Put your own name down', 'Grab her wrist', 'Write nothing', 'Ask her to measure you', 'Hold still and endure it', 'Write back', 'Brace your hands on her shoulders', 'I keep thinking about leaving', 'Restore it, and break the cycle']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (wom.chapter == 12 and wom.ending == "restore" and wom.pool == "bet" and wom.ch8 == "never" and wom.shout6 == "brace" and wom.tell2 == "truth" and wom.write4 == "nothing" and wom.note6 == "wrote")
