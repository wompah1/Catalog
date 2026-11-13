## The storyline's hub at the track (main.twee :: Redlightning Hub), written by hand: linear days
## only (Redlightning.linear, the route as a VN). The readouts (the margin first, never a number),
## the day's line, and its one way on: the rung at the session, the night at his, his door in the
## evening, or bed. No flavour links on the line (Train and Find Thorne are free play).

init -5 python:
    # The day's line when a rung is due (the hub's <<switch _rls.tier>>).
    RL_HUB_RUNG = [
        "Miles is at the edge of the infield with something in his hand. It's pink. It's glowing. It's fizzing like it's angry about something.",
        "Coach has the stopwatch out. Miles has a bottle the colour of a swimming pool, and he's watching you warm up instead of warming up.",
        "Repeats today. Coach's favourite. Everyone else's least favourite. Your chest is already bouncing in your tank top just from the jog over.",
        "The squad's piling into the lounge after the session, and Lenny's been building up to something all week. Imogen has her clipboard pressed to her chest like a shield.",
        "The big meet. The rival university's coach is already in the car park. Imogen has restitched your kit twice this week and it's losing anyway.",
        "Miles caught your wrist on your way out of his room. Red to the ears. \"Stay at mine tonight.\"",
    ]

    def rl_hub_way():
        """(the day's line, (link text, how, label)): the hub's one way on (Redlightning.due and
        Redlightning.forward, linear days)."""
        t, due = rl.tier or 0, rl_due()
        on = None
        if due and t < 5 and rl_late():
            line = "The squad trains in the afternoon. Coach has gone home to shout at his telly."
        elif due == "rung":
            line = RL_HUB_RUNG[min(t, 5)]
            if t == 5:
                if vn_clock.hour >= 19:
                    on = ("Stay at Miles's tonight", "night", RL_RUNG_LABEL[6])
            else:
                on = ("The big meet" if t == 4 else "Afternoon session", 14, RL_RUNG_LABEL[t + 1])
        elif t == 0:
            line = "Coach wants you back tomorrow. \"Rest,\" he says. You don't know how."
        elif t == 5:
            line = "Miles keeps looking at you across the infield like he's working up to asking you something."
        else:
            line = "\"Big session tomorrow,\" Coach says. \"Rest.\" You do laps anyway."
        if on is None:
            f = rl_forward()
            if f == "sleep" and t < 6 and vn_clock.hour >= 6:
                # linear days: once the evening has his door, his door IS the evening
                on = ("Up to Track Halls: knock on Miles's door", 20, "rl_miles_door")
            elif isinstance(f, tuple):
                on = (f[2], f[1], "rl_hub")
            else:
                on = ("Back up to Track Halls, and bed", "night", "rl_wake")
        return line, on

label rl_hub:
    $ rl_init()
    $ rl.fit = None
    $ vn_enter(bg=rl_default_bg("track"), pc="grin", pc_tag="rory", cast=rl_hub_cast(), cg=None)
    $ _rl_status = rl_status()
    "[_rl_status]"
    $ _rl_line, _rl_on = rl_hub_way()
    "[_rl_line]\n{size=-5}{color=#ff8fa3}▸ [_rl_on[0]]{/color}{/size}"
    if _rl_on[1] == "night":
        call vn_night(7)
    else:
        $ vn_until(_rl_on[1])
    jump expression _rl_on[2]
