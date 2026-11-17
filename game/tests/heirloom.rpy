## The Club Heirloom Only Seals Once Someone Fucks It Into Place, played through by Ren'Py's test runner
## (tools/rptest.sh). Walk a takes every first choice, walk b every second, walk c alternates. One ending
## (the book's); the walks check the flavour choices land and the climb ends at Yuuka complete.
## Not run until the route has its art (the owner, 2026-11-12: walks once a route has art).

testcase heirloom_a:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Club Heirloom Only Seals Once Someone Fucks It Into Place", 'Tell them no', 'Tell her to stop', 'Fight her grip', "Put a hundred yen on 'it stops here'", 'Tear it down', 'Shove at her head', 'Push her away', 'Kick away from her', "Hold on to 'no'", 'Put the bra on', 'Crawl to Nao', 'Take it', 'Use your mouth']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hrl.chapter == 14 and hrl.ending == "trunk" and hrl.broke and hrl.asked and hrl.row == "9" and hrl_pc_name == "Yuuka" and hrl.camp == "nao" and hrl.top == "bra" and hrl.pool == "stops")

testcase heirloom_b:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Club Heirloom Only Seals Once Someone Fucks It Into Place", 'Head for the door', 'Close your knees', 'Plead with Rei', 'Refuse to bet on your own body', 'Ignore it', 'Try to stand', 'Grip the bench and refuse', "Tell her it won't work", 'Let it go', 'Hoodie, straight over the top', 'Crawl to Rei', 'Let it ring', 'Use your fingers']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hrl.chapter == 14 and hrl.ending == "trunk" and hrl.camp == "rei" and hrl.top == "hoodie" and hrl.phone == "rang" and hrl.pool == "refuse" and hrl.set14 == "fingers")

testcase heirloom_c:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 160.0
    $ renpy.session["vn_picks"] = ["The Club Heirloom Only Seals Once Someone Fucks It Into Place", 'Tell them no', 'Close your knees', 'Fight her grip', 'Refuse to bet on your own body', 'Tear it down', 'Try to stand', 'Push her away', "Tell her it won't work", "Hold on to 'no'", 'Hoodie, straight over the top', 'Crawl to Nao', 'Let it ring', 'Use your mouth']
    run Start()
    advance until eval (not renpy.session.get("vn_picks") and renpy.get_screen("vn_route_select") is not None)
    assert eval (not renpy.session.get("vn_picks"))
    assert eval (hrl.chapter == 14 and hrl.sched == "tore" and hrl.shout1 == "knees" and hrl.break6 == "hold" and hrl.set14 == "mouth")
