## Story tags: the route select's filter (owner, 2026-11-17 3:25 pm ET: "filter by tag and each story gets tags";
## 3:31 pm ET: "have a and and or option", "no consent tags").
##
## One line per route id: ("the day the route was built", "its tags"). The date drives the Newest sort. An id that isn't
## registered in this checkout is ignored, so a route can be tagged before it merges; a registered route with no line
## shows only while no filter is on, and tools/publish.sh refuses to publish it (tools/tags_check.py).
##
## The rules, for every chat adding a route:
## - exactly one tag from Transformation and one from Setting; any number from the other groups;
## - never a consent level, and nothing on the content blacklist (memory: dol-content-blacklist);
## - Format is counted, not judged: `python3 tools/tags_check.py --format <route>` prints it (branching: 12+ menus;
##   endings: 2+ `ending=True`; short: under 7,000 words of script; long: 15,000 or more);
## - futa: a partner with a cock and breasts on the page, not only a PC who keeps theirs;
## - milf: an older woman partner, or a PC who becomes one.
## The first tagging (07, 2026-11-17) is a draft: the rows the owner should look at are in twineTesting/STORY-TAGS-CHECK.md.

init -55 python:

    ## (group id, heading, one tag only?, [(tag id, chip label), ...]) in the order the filter shows them
    VN_TAG_GROUPS = [
        ("change", _("Transformation"), True, [
            ("no-tf", _("No TF")), ("gradual", _("Gradual")), ("sudden", _("Sudden"))]),
        ("kind", _("Themes"), False, [
            ("tsf", _("TSF")), ("feminization", _("Feminization")), ("femboy", _("Femboy")), ("bimbo", _("Bimbo")),
            ("breast-growth", _("Breast growth")), ("hypno", _("Hypno")), ("body-swap", _("Body swap & skinsuits")),
            ("animal", _("Animal & monster traits")), ("magical-girl", _("Magical girl & henshin"))]),
        ("partners", _("Partners"), False, [
            ("men", _("Men")), ("women", _("Women")), ("futa", _("Futa")), ("milf", _("MILFs")),
            ("creatures", _("Creatures")), ("group", _("Group"))]),
        ("setting", _("Setting"), True, [
            ("modern", _("Modern")), ("fantasy", _("Fantasy")), ("sci-fi", _("Sci-fi")),
            ("game-world", _("Game / VR world")), ("historical", _("Historical"))]),
        ("format", _("Format"), False, [
            ("branching", _("Branching")), ("endings", _("Multiple endings")), ("short", _("Short")), ("long", _("Long"))]),
    ]
    VN_TAG_LABEL = dict((t, lab) for g in VN_TAG_GROUPS for t, lab in g[3])
    VN_TAG_ORDER = [t for g in VN_TAG_GROUPS for t, lab in g[3]]

    vn_route_tags = {
        "ace": ("2026-11-12", "sudden tsf men modern branching endings long"),
        "afterhours": ("2026-11-12", "sudden feminization women futa modern branching"),
        "afterten": ("2026-11-12", "sudden tsf women futa modern"),
        "ambassador": ("2026-11-12", "gradual tsf women futa milf sci-fi short"),
        "amendment": ("2026-11-12", "gradual tsf hypno women futa milf modern branching"),
        "apprentice": ("2026-11-12", "gradual tsf men fantasy short"),
        "ashby": ("2026-11-12", "gradual tsf women futa modern short"),
        "ashcombe": ("2026-11-12", "no-tf feminization femboy men women futa milf modern branching endings long"),
        "askme": ("2026-11-13", "sudden tsf men modern branching"),
        "asleep": ("2026-11-16", "no-tf futa modern endings short"),
        "atelier": ("2026-11-14", "no-tf feminization femboy men women futa modern branching endings"),
        "audit": ("2026-11-12", "gradual tsf breast-growth men modern endings"),
        "bait": ("2026-11-12", "gradual tsf animal women futa creatures fantasy branching"),
        "baseline": ("2026-11-12", "sudden tsf men modern"),
        "bestman": ("2026-11-13", "gradual tsf breast-growth men women modern branching endings"),
        "betatester": ("2026-11-16", "sudden tsf men women creatures group game-world short"),
        "bit": ("2026-11-12", "no-tf feminization femboy men women modern endings short"),
        "bloodline": ("2026-11-16", "gradual tsf animal men women milf group modern endings"),
        "bloomwell": ("2026-11-13", "gradual feminization breast-growth men women modern short"),
        "booth": ("2026-11-13", "no-tf men women modern endings"),
        "borrowed": ("2026-11-12", "sudden tsf bimbo body-swap men women milf group modern branching endings long"),
        "bottle": ("2026-11-12", "gradual tsf men women modern"),
        "bounty": ("2026-11-15", "gradual tsf breast-growth men women creatures fantasy branching endings"),
        "boytoy": ("2026-11-12", "sudden feminization animal men modern branching endings long"),
        "bree": ("2026-11-12", "gradual tsf men modern branching endings long"),
        "broker": ("2026-11-12", "gradual tsf breast-growth body-swap women futa modern endings"),
        "burglar": ("2026-11-15", "gradual femboy animal men women futa modern branching endings"),
        "camellia": ("2026-11-12", "no-tf feminization femboy men women milf historical endings"),
        "celestia": ("2026-11-11", "sudden tsf magical-girl men women modern branching endings long"),
        "channel": ("2026-11-12", "gradual tsf breast-growth women modern branching endings long"),
        "chef": ("2026-11-13", "gradual tsf men women modern short"),
        "cleo": ("2026-11-12", "no-tf men modern branching endings long"),
        "clover": ("2026-11-13", "sudden feminization breast-growth hypno animal futa game-world branching short"),
        "club": ("2026-11-12", "gradual tsf feminization breast-growth men modern branching endings long"),
        "coach": ("2026-11-16", "gradual feminization breast-growth men modern endings"),
        "cockpit": ("2026-11-13", "gradual tsf breast-growth men futa creatures sci-fi branching endings"),
        "coco": ("2026-11-13", "sudden feminization men futa modern"),
        "collar": ("2026-11-11", "gradual tsf breast-growth men modern endings"),
        "combattrack": ("2026-11-12", "sudden tsf breast-growth men women futa modern branching endings"),
        "confirm": ("2026-11-12", "sudden tsf men modern"),
        "conrad": ("2026-11-12", "gradual tsf feminization femboy men modern short"),
        "corner": ("2026-11-12", "gradual feminization breast-growth men futa group modern branching endings"),
        "corps": ("2026-11-11", "gradual tsf breast-growth magical-girl men women creatures modern branching endings long"),
        "costume": ("2026-11-12", "sudden tsf magical-girl women creatures group modern"),
        "council": ("2026-11-12", "gradual tsf women futa modern short"),
        "cult": ("2026-11-16", "gradual tsf breast-growth women futa milf modern endings short"),
        "cure": ("2026-11-13", "gradual feminization men modern short"),
        "curses": ("2026-11-13", "gradual feminization men women modern"),
        "curve": ("2026-11-12", "gradual tsf women modern"),
        "dani": ("2026-11-12", "gradual feminization men women modern short"),
        "daria": ("2026-11-13", "gradual tsf breast-growth men women sci-fi branching endings"),
        "deepcover": ("2026-11-12", "gradual tsf feminization breast-growth men historical endings"),
        "delilah": ("2026-11-12", "sudden feminization femboy men women modern short"),
        "dollapp": ("2026-11-16", "no-tf feminization femboy hypno men modern endings short"),
        "duelist": ("2026-11-16", "gradual tsf breast-growth men women futa game-world branching endings long"),
        "equipslot": ("2026-11-12", "sudden tsf men futa game-world endings"),
        "escaperoom": ("2026-11-15", "no-tf femboy men futa modern branching endings"),
        "evidence": ("2026-11-13", "sudden tsf breast-growth men futa modern branching endings"),
        "fantasies": ("2026-11-12", "no-tf feminization femboy men modern short"),
        "fever": ("2026-11-13", "gradual tsf men futa modern short"),
        "fitting": ("2026-11-12", "gradual tsf feminization breast-growth men women group modern branching endings long"),
        "fivestars": ("2026-11-12", "gradual feminization women futa group modern branching endings long"),
        "flyer": ("2026-11-12", "no-tf hypno men women modern short"),
        "fullclear": ("2026-11-12", "sudden tsf hypno men women futa fantasy endings"),
        "fusion": ("2026-11-16", "gradual tsf breast-growth women modern endings short"),
        "gacha": ("2026-11-12", "sudden tsf femboy animal men women futa group modern branching endings"),
        "gains": ("2026-11-12", "sudden tsf women futa modern branching short"),
        "girlpill": ("2026-11-12", "sudden tsf men modern short"),
        "glutes": ("2026-11-12", "gradual feminization breast-growth men modern branching endings long"),
        "greathawk": ("2026-11-12", "gradual tsf breast-growth animal men creatures fantasy branching endings long"),
        "guild": ("2026-11-12", "sudden tsf breast-growth men women milf fantasy endings long"),
        "gyaru": ("2026-11-16", "gradual tsf hypno men women futa modern short"),
        "hairclip": ("2026-11-12", "no-tf men women modern short"),
        "halves": ("2026-11-15", "sudden tsf breast-growth men modern endings"),
        "harem": ("2026-11-13", "gradual feminization men women milf group fantasy branching"),
        "heat": ("2026-11-13", "sudden tsf men futa modern short"),
        "heirloom": ("2026-11-12", "sudden tsf body-swap men women modern branching"),
        "hen": ("2026-11-12", "sudden feminization men modern"),
        "hollowpine": ("2026-11-12", "no-tf hypno women futa modern branching endings"),
        "honeypot": ("2026-11-15", "sudden tsf men women modern branching endings short"),
        "honeystar": ("2026-11-13", "sudden tsf magical-girl women futa modern short"),
        "hunt": ("2026-11-15", "gradual tsf breast-growth animal men group modern branching endings"),
        "hypno": ("2026-11-11", "no-tf feminization femboy hypno men women modern endings long"),
        "institut": ("2026-11-14", "no-tf feminization femboy men women futa modern branching endings"),
        "island": ("2026-11-16", "gradual tsf breast-growth men women modern branching endings"),
        "jelly": ("2026-11-15", "gradual tsf breast-growth men women futa creatures fantasy branching endings"),
        "juice": ("2026-11-12", "gradual feminization breast-growth women futa group modern endings"),
        "keywords": ("2026-11-12", "gradual tsf men women modern short"),
        "lacey": ("2026-11-12", "no-tf feminization femboy men women milf modern short"),
        "ladiescar": ("2026-11-16", "gradual tsf breast-growth women futa modern endings short"),
        "laura": ("2026-11-12", "sudden tsf breast-growth animal men creatures fantasy branching endings long"),
        "ledger": ("2026-11-12", "gradual feminization breast-growth animal men women futa fantasy branching endings long"),
        "lifeclass": ("2026-11-12", "gradual feminization men women modern endings long"),
        "lightsout": ("2026-11-12", "no-tf futa modern short"),
        "livestock": ("2026-11-11", "gradual tsf breast-growth animal women futa group modern branching endings long"),
        "locktober": ("2026-11-12", "no-tf men group modern short"),
        "mal": ("2026-11-13", "sudden feminization breast-growth men women modern branching endings long"),
        "markers": ("2026-11-11", "gradual tsf breast-growth animal men women futa modern branching endings long"),
        "membership": ("2026-11-16", "gradual tsf hypno women futa modern short"),
        "mentorship": ("2026-11-12", "gradual tsf breast-growth hypno women futa milf group modern branching endings"),
        "meridian": ("2026-11-12", "gradual tsf hypno women futa modern"),
        "mistaken": ("2026-11-11", "sudden tsf femboy breast-growth men women modern endings"),
        "moon": ("2026-11-12", "gradual tsf breast-growth men group fantasy endings"),
        "moonflower": ("2026-11-16", "gradual feminization femboy breast-growth men women futa modern endings"),
        "neckdown": ("2026-11-12", "sudden tsf breast-growth body-swap women futa modern endings long"),
        "neighbour": ("2026-11-11", "gradual tsf breast-growth futa modern branching endings"),
        "nevercameup": ("2026-11-12", "gradual tsf breast-growth men modern branching endings"),
        "newgirl": ("2026-11-12", "no-tf men futa modern short"),
        "newmum": ("2026-11-15", "gradual tsf breast-growth men milf modern endings"),
        "nose": ("2026-11-12", "gradual tsf breast-growth animal men fantasy endings"),
        "notanlines": ("2026-11-12", "gradual tsf breast-growth men women futa group modern endings long"),
        "nyanko": ("2026-11-12", "gradual tsf animal men modern short"),
        "odette": ("2026-11-14", "no-tf feminization femboy hypno animal men women futa modern branching endings"),
        "oiran": ("2026-11-14", "gradual tsf breast-growth men women historical endings"),
        "otherwoman": ("2026-11-12", "gradual tsf women futa modern"),
        "patchnotes": ("2026-11-15", "sudden tsf breast-growth men women modern branching endings"),
        "pavilion": ("2026-11-12", "gradual feminization breast-growth women futa fantasy endings long"),
        "payback": ("2026-11-15", "gradual tsf breast-growth hypno men women modern endings"),
        "petticoat": ("2026-11-14", "no-tf feminization femboy men women futa historical branching endings"),
        "playlists": ("2026-11-12", "no-tf men women futa modern short"),
        "plug": ("2026-11-12", "gradual tsf animal women futa modern branching"),
        "poll": ("2026-11-12", "no-tf men women futa modern"),
        "practice": ("2026-11-12", "gradual tsf femboy breast-growth men women modern branching endings long"),
        "president": ("2026-11-16", "gradual feminization femboy breast-growth men women modern branching endings"),
        "pressit": ("2026-11-12", "sudden tsf breast-growth men women futa modern branching endings long"),
        "profile": ("2026-11-15", "no-tf feminization femboy men women futa modern branching endings short"),
        "qualifying": ("2026-11-12", "sudden tsf breast-growth men women futa modern endings"),
        "quota": ("2026-11-12", "sudden tsf breast-growth men modern endings"),
        "ranch": ("2026-11-12", "gradual tsf animal men women milf creatures modern short"),
        "rascal": ("2026-11-12", "gradual tsf breast-growth animal women futa modern branching endings long"),
        "receptionist": ("2026-11-15", "gradual tsf men women futa milf creatures fantasy"),
        "redlightning": ("2026-11-11", "gradual tsf breast-growth men modern endings long"),
        "relief": ("2026-11-15", "gradual tsf breast-growth men women group sci-fi endings long"),
        "rematch": ("2026-11-12", "gradual tsf men women futa creatures fantasy short"),
        "rendered": ("2026-11-12", "gradual tsf women game-world short"),
        "respec": ("2026-11-12", "gradual tsf men futa game-world short"),
        "returnrate": ("2026-11-12", "sudden tsf men modern"),
        "reward": ("2026-11-16", "gradual tsf men women futa modern short"),
        "rurika": ("2026-11-12", "gradual tsf femboy men women futa modern"),
        "rushhour": ("2026-11-15", "gradual tsf breast-growth men women modern endings"),
        "sabrina": ("2026-11-12", "gradual feminization breast-growth hypno men modern branching endings long"),
        "samebrand": ("2026-11-12", "gradual feminization men modern"),
        "saturday": ("2026-11-13", "gradual tsf breast-growth men women futa modern branching endings long"),
        "scales": ("2026-11-12", "gradual tsf breast-growth animal men women futa creatures fantasy branching endings long"),
        "scion": ("2026-11-15", "gradual tsf men women futa historical endings"),
        "screenaccurate": ("2026-11-12", "gradual tsf femboy hypno body-swap women futa modern endings"),
        "season": ("2026-11-13", "gradual tsf breast-growth men women historical branching endings"),
        "secondvial": ("2026-11-12", "sudden tsf men women fantasy"),
        "sexcross": ("2026-11-17", "gradual tsf men women futa modern short"),
        "shipsstores": ("2026-11-12", "gradual tsf breast-growth men group historical branching endings long"),
        "shrine": ("2026-11-12", "gradual tsf breast-growth animal men creatures modern endings long"),
        "silo": ("2026-11-13", "gradual feminization men modern short"),
        "sissyedition": ("2026-11-12", "gradual feminization femboy men women modern short"),
        "sister": ("2026-11-11", "gradual tsf breast-growth women futa modern endings long"),
        "sleeper": ("2026-11-15", "sudden tsf breast-growth men women modern branching endings"),
        "slimefruit": ("2026-11-13", "gradual feminization women modern short"),
        "slipper": ("2026-11-15", "sudden tsf breast-growth men women futa fantasy branching endings"),
        "smartdrug": ("2026-11-12", "gradual tsf men women futa milf modern short"),
        "snowedin": ("2026-11-12", "no-tf women futa modern short"),
        "spincycle": ("2026-11-12", "gradual tsf breast-growth women futa modern branching endings long"),
        "spinning": ("2026-11-15", "gradual tsf breast-growth animal men women historical branching endings"),
        "spotter": ("2026-11-12", "no-tf hypno women futa modern short"),
        "standin": ("2026-11-14", "sudden tsf breast-growth men women futa fantasy endings"),
        "stoppedtime": ("2026-11-12", "gradual tsf men futa modern"),
        "suggestible": ("2026-11-16", "gradual tsf breast-growth hypno men women modern branching endings"),
        "summoning": ("2026-11-12", "gradual tsf men futa modern short"),
        "swimmersear": ("2026-11-13", "gradual feminization men modern"),
        "sword": ("2026-11-13", "gradual tsf breast-growth men futa fantasy branching endings"),
        "tabitha": ("2026-11-12", "no-tf hypno women futa modern"),
        "templecat": ("2026-11-15", "gradual tsf breast-growth animal men women historical branching endings"),
        "tenant": ("2026-11-13", "gradual tsf men women futa creatures fantasy"),
        "terms": ("2026-11-12", "gradual tsf men women futa modern short"),
        "torishimari": ("2026-11-12", "sudden tsf breast-growth magical-girl men creatures group modern branching endings long"),
        "transplant": ("2026-11-16", "gradual tsf men women milf modern endings short"),
        "tribute": ("2026-11-12", "sudden feminization men group modern"),
        "twin": ("2026-11-12", "sudden tsf men modern short"),
        "velvet": ("2026-11-12", "gradual feminization men creatures sci-fi"),
        "venus": ("2026-11-11", "gradual tsf breast-growth men women modern branching endings"),
        "villa": ("2026-11-13", "no-tf feminization femboy men women futa modern branching endings"),
        "vote": ("2026-11-12", "gradual tsf men women group modern endings"),
        "wager": ("2026-11-12", "sudden tsf men modern"),
        "warlock": ("2026-11-16", "gradual tsf breast-growth animal women creatures fantasy branching endings"),
        "waterbuffs": ("2026-11-12", "sudden tsf breast-growth men modern branching endings long"),
        "witches": ("2026-11-12", "sudden feminization animal men women futa modern branching endings long"),
        "witness": ("2026-11-15", "gradual tsf hypno men women futa modern branching endings short"),
        "wizard": ("2026-11-16", "gradual tsf breast-growth men women futa fantasy endings short"),
        "wolfpack": ("2026-11-12", "gradual tsf breast-growth animal men creatures group modern branching endings long"),
        "womensbath": ("2026-11-12", "gradual tsf women modern branching endings"),
        "yinbody": ("2026-11-12", "gradual tsf breast-growth men women fantasy branching endings"),
        "yourtype": ("2026-11-12", "gradual tsf breast-growth men modern endings long"),
    }

    def vn_tags_check(table):
        """Every tag known, one each from the one-tag groups, a date that sorts. Raises ValueError (lint and
        tools/tags_check.py both run this), so a typo never reaches a player."""
        import re as _re
        for rid, (built, tags) in table.items():
            ts = tags.split()
            if not _re.match(r"^\d{4}-\d{2}-\d{2}$", built):
                raise ValueError("tags.rpy: %s: built %r isn't YYYY-MM-DD" % (rid, built))
            bad = [t for t in ts if t not in VN_TAG_LABEL]
            if bad:
                raise ValueError("tags.rpy: %s: unknown tag(s) %s" % (rid, " ".join(bad)))
            if len(set(ts)) != len(ts):
                raise ValueError("tags.rpy: %s: a tag twice" % rid)
            for gid, head, one, items in VN_TAG_GROUPS:
                n = sum(1 for t, lab in items if t in ts)
                if one and n != 1:
                    raise ValueError("tags.rpy: %s: needs exactly one %s tag, has %d" % (rid, gid, n))

    vn_tags_check(vn_route_tags)
