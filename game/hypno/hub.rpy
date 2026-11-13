## Open and Listen's hub, your room (main.twee :: Hypno Hub), and the session dispatcher
## (:: Hypno Session), written by hand: linear days only (Route.linear: the Bell, sitting with Liam
## and the vanity are free play's). The clock is the first line, every visit, and nothing lowers
## it. NO REFUSAL (owner decision 5): when a session is due, the only choices are flavour, and
## they all lead into it. Liam never asks.

init -5 python:
    # The day's line between sessions (the hub's <<switch _hs.tier>>).
    HY_HUB_DAY = [
        "Liam asked if hypnosis was real. You said no. He hasn't mentioned it since.",
        "Mike's texted about Thursday. You keep meaning to answer. Liam's in the kitchen, cheerful, banging the kettle about.",
        "You missed league on Tuesday. You don't remember deciding to. Liam brought you tea in bed instead, and you went warm and soft all over. {color=#b7b7b7}Coming down with something.{/color}",
        "The cage sits snug under your boxers. The Bloom gave it you, you're fairly sure: something about the pills. {color=#b7b7b7}Medical.{/color} The platinum tails at your temples are a bet you lost. Liam says they suit you.",
        "Liam's door is shut. \"Friday,\" he says through it, when you knock to ask about the bins. Your knees go funny. {color=#b7b7b7}Skipped lunch.{/color}",
        "Your work shirts don't fit across the hips any more. {color=#b7b7b7}Squats.{/color} Mike's last text: {color=#4372ff}u alright mate? havent seen u{/color}. You keep meaning to answer.",
        "You're under. You don't know it. Liam is on the floor beside your bed.",
    ]
    # The days of the same between two rungs (HY_RUNG_DAY; 2026-11-12, the counter has to agree with
    # the story): one line on the morning after a rung, and the hub sleeps through to the next rung's
    # first day. In the hub's grey, explained wrongly, like the residue.
    HY_HUB_GAP = {
        2: "A week of days the same. Work. Home. Most evenings an hour goes missing on the end of your bed, and you put it down to being tired. Your nipples won't settle down. Tuesday comes and goes.",
        3: "Days of the same. The pills, with the tea. Work, in shirts that have started to pull. Evenings go missing, and you don't mind as much as you should.",
        5: "A week of the same. Work. Home. Your own hair comes in long and brown, faster than hair should, and the platinum extensions go in a drawer. The pills, probably.",
    }
    # The approach when a session is due (tiers 3-5 have their own; the first nights a bank line).
    HY_HUB_DUE = {
        3: "Your phone chimes once, a pretty little sound. Through the wall, Liam's chair scrapes back. You find you've sat up very straight.",
        4: "The weekend, at last, for some reason. The chime comes through the wall and your pulse jumps. You've no idea why.",
        5: "The chime comes through the wall. Your knees like the carpet lately. You don't think about it.",
    }

    def hy_room():
        t = hy.tier or 0
        return HY_ROOM[t] if 1 <= t < len(HY_ROOM) else ""

label hy_hub:
    $ hy_init()
    $ hy.fit = None
    $ vn_enter(bg="hy_bedroom", pc="neutral", pc_tag="hy_pc", cast=[], cg=None)
    $ _hy_rank = HY_RANKS[min(hy.tier or 0, 6)]
    "{color=#ffd700}Sessions run:{/color} {color=#e40081}[_hy_rank]{/color}"
    ## the VN route takes the Bloom's pill for you, once a day, on the first hub of the day after
    ## the clinic (owner, 2026-11-10); its picture is up from that line to "Your room"
    if not hy.done and hy_pill():
        show cg hy_pill onlayer cgl
        if vn_clock.hour < 12:
            if hy.full:
                "Little white pill, first thing, with the tea; its twin waits by your toothbrush for tonight. You've swallowed it before you notice you've picked it up. A warm little flush of {color=#e40081}pride{/color} that isn't yours."
            else:
                "Little white pill, first thing, with the tea. You've swallowed it before you notice you've picked it up. A warm little flush of {color=#e40081}pride{/color} that isn't yours."
        else:
            if hy.full:
                "Little white pill, with the tea; its twin waits by your toothbrush for tonight. You've swallowed it before you notice you've picked it up. A warm little flush of {color=#e40081}pride{/color} that isn't yours."
            else:
                "Little white pill, with the tea. You've swallowed it before you notice you've picked it up. A warm little flush of {color=#e40081}pride{/color} that isn't yours."
        hide cg onlayer cgl
    $ _hy_room = hy_room()
    if _hy_room:
        "Your room. His room is through the wall.\n{color=#e40081}[_hy_room]{/color}"
    else:
        "Your room. His room is through the wall."
    if hy_due():
        ## the approach: Ethan's last waking minute of the evening, and nothing that says no
        if (hy.tier or 0) in HY_HUB_DUE:
            $ _hy_line = HY_HUB_DUE[hy.tier]
        else:
            $ _hy_line = "{color=#b7b7b7}" + hy_session_line() + "{/color}"
        if (hy.tier or 0) >= 3:
            menu:
                "[_hy_line]"
                "Kneel on the carpet and wait":
                    $ hy.flav = "kneel"
                "Go to his door":
                    $ hy.flav = "door"
        else:
            menu:
                "[_hy_line]"
                "Sit on the end of the bed":
                    $ hy.flav = "sit"
                "Keep scrolling your phone":
                    $ hy.flav = "phone"
        jump hy_session
    if vn_clock.day - (hy.last_dose if hy.last_dose is not None else -9) <= 1:
        $ _hy_res = hy_residue()
        if _hy_res:
            "{color=#b7b7b7}[_hy_res]{/color}"
    ## the days of the same (HY_RUNG_DAY): from a morning hub, sleep through to the next rung's day
    if vn_clock.hour >= 5 and not hy_evening():
        $ _hy_gap = hy_gap_days()
        if _hy_gap > 0:
            $ _hy_gapline = HY_HUB_GAP[hy.tier]
            if hy.tier == 5:
                $ hy.own_hair = True
            "{color=#b7b7b7}[_hy_gapline]{/color}\n{size=-5}{color=#ff8fa3}▸ Days of the same{/color}{/size}"
            $ vn_pass(_hy_gap * 1440)
            $ vn_set_time(8, 0)
            jump hy_hub
    $ _hy_day = HY_HUB_DAY[min(hy.tier or 0, 6)]
    if (hy.tier or 0) >= 6:
        "[_hy_day]\n{size=-5}{color=#ff8fa3}▸ Liam, on the floor beside your bed{/color}{/size}"
        jump hy_fork
    if hy.appt and not hy.rx and vn_clock.hour >= 5 and not hy_evening():
        ## the errand, as the route's own link: you still go yourself; that's the point of it
        "[_hy_day]"
        "{color=#ffd700}An appointment card on your desk, in his handwriting: The Bloom, the clinic on the High Street.{/color} \"Eat first,\" Liam says from the doorway. \"They take blood.\""
        "You pocket the card and walk to the Bloom yourself, down the High Street. Nobody has to make you.\n{size=-5}{color=#ff8fa3}▸ Keep the appointment Liam booked{/color}{/size}"
        $ vn_pass(60)
        jump hy_bloom_consult
    if vn_clock.hour >= 5 and not hy_evening():
        "[_hy_day]\n{size=-5}{color=#ff8fa3}▸ Wait for the evening{/color}{/size}"
        $ vn_until(19)
        jump hy_hub
    ## the night, from your room: one click sleeps, and you wake back in here at eight. At tier 4
    ## the lost weekend waits for a Friday or Saturday night, so a weekday night sleeps through.
    $ _hy_skip = hy_weekend_skip_days()
    if _hy_skip > 0:
        "[_hy_day]"
        "{color=#b7b7b7}The week drags. Work. Home. His door, shut, and your knees aching for the carpet in front of it. \"Friday,\" through the wood, every night.{/color}\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
        $ vn_pass(_hy_skip * 1440)
    else:
        "[_hy_day]\n{size=-5}{color=#ff8fa3}▸ Sleep{/color}{/size}"
    if vn_clock.hour < 8:
        ## past midnight: the night ends at eight this morning
        $ vn_set_time(8, 0)
        $ vn_pass(-1440)
    call vn_night(8)
    jump hy_hub

## Tonight's session is a new rung, or (only while the consult waits, which a linear day never
## reaches) another evening under the loop.
label hy_session:
    $ _hy_n = hy_next_rung()
    if _hy_n:
        jump expression HY_RUNG_LABEL[_hy_n]
    ## the interim session is free play's (the linear day goes to the Bloom first)
    jump hy_hub
