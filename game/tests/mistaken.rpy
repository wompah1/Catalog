## The misclick played through, start to finish, by Ren'Py's own test runner (tools/rptest.sh).
## Walk a: the TSF branch (the forms retired), every optional scene, both filler days, "as you are"
## sent back at rung 3 and passing at rung 4, the proper contract. Walk b: the femboy branch (the
## forms on), every optional scene skipped, no filler, Jessie's build every day, the badge handed in.
## The plan's first snippet picks the route card by its title. The global teardown that closes the
## game is in redlightning.rpy.

testcase mistaken_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['I Misclicked', 'Sweet. Nervous', 'Slow, and pretty', 'Let Jessie build you', 'Give Gus his second angle', 'Take the catalogue job', 'Go in as you are', 'Do you want to see', "You've got it in you", 'Go in as you are', "Take Gus's insert", 'Leave the forms in the case', 'Sign the proper contract']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)

testcase mistaken_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 180.0
    $ renpy.session["vn_picks"] = ['I Misclicked', 'A brat', 'Sloppy', 'Let Jessie build you', "That's a wrap", 'Straight to your call', 'Let Jessie build you', 'Careful. I bite back', "That's a wrap", 'Let Jessie build you', 'Straight to the marquee', 'Put the forms on', 'Hand the badge in']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
