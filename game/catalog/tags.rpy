## Story tags: the route select's filter.
##   owner, 2026-11-17 3:25 pm ET: "filter by tag and each story gets tags"; 3:31 pm: "have a and and or option";
##   4:08 pm: "are milfs not women? also lets use the nhentai tag system"; 4:13 pm: "consent tags like nhentais is fine".
##
## One line per route id: ("the day the route was built", "tag, tag, ..."), commas between tags (nhentai's tags have
## spaces in them). The date drives the Newest sort. An id that isn't registered in this checkout is ignored, so a
## route can be tagged before it merges; a registered route with no line shows only while no filter is on, and
## tools/publish.sh refuses to publish it (tools/tags_check.py).
##
## The rules, for every chat adding a route:
## - tags are nhentai's own ("tags" namespace), spelt as nhentai spells them, lowercase, from VN_TAGS below. A tag
##   that isn't there yet: add it to VN_TAGS (nhentai's exact name) in the same commit;
## - nhentai's consent and situation tags are fine where the route has them (rape, blackmail, drugs, sleeping...):
##   go by the route's own consent note, not by one line of protest;
## - never anything on the content blacklist (memory: dol-content-blacklist: no impregnation, no piercings...), nothing
##   youth- or school-coded (no lolicon, shotacon, school uniform, schoolgirl, teacher, student), and no "small
##   breasts" or "flat chest";
## - who's in it: sole female (the PC is the only woman, partners men), sole male (the PC is the only man, partners
##   women or futa), females only / yuri (a female PC with women), males only (a male PC with men), plus group,
##   harem, futanari (a partner with a cock and breasts on the page), milf (an older woman partner, or a PC who
##   becomes one), monster;
## - the change, by how the route ends (owner 2026-11-17: "replace gender bender with TSF, also use the custom soft
##   tsf tag"): tsf (ends a woman, the cock gone), soft tsf (ends with a woman's body and the cock kept),
##   feminization / trap (ends a femboy, still him). A route that can end more than one way takes each;
## - then the Story row, after the nhentai tags: at most one of gradual / sudden (how the change comes; none for a
##   route with no transformation), and branching, multiple endings, short, long, which are counted, not judged:
##   `python3 tools/tags_check.py --format <route>` prints them (branching: 12+ menus; multiple endings: 2+
##   `ending=True`; short: under 7,000 words of script; long: 15,000 or more).
## The nhentai tagging (07, 2026-11-17) is a draft: the rows the owner should look at are in
## twineTesting/STORY-TAGS-CHECK.md.

init -55 python:

    ## nhentai's tags, in the order a card lists them. The filter shows the ones some story has, sorted by how many.
    VN_TAGS = [
        "tsf", "soft tsf", "feminization", "trap", "crossdressing", "transformation", "breast expansion",
        "bimbofication", "body swap", "skinsuit", "possession", "mind control", "corruption", "mind break",
        "magical girl", "time stop", "sole female", "sole male", "females only", "males only", "yuri", "group",
        "harem", "futanari", "milf", "monster", "tentacles", "slime", "orc", "elf", "demon girl", "vampire", "catgirl",
        "kemonomimi", "tail", "horns", "wings", "cowgirl", "witch", "miko", "idol", "gyaru", "nurse",
        "office lady", "dark skin", "huge breasts", "big breasts", "big ass", "big penis", "lactation", "tanlines",
        "anal", "blowjob", "paizuri", "nakadashi", "double penetration", "masturbation", "sex toys", "strap-on",
        "femdom", "bondage", "collar", "leash", "chastity belt", "exhibitionism", "humiliation", "prostitution",
        "ahegao", "x-ray", "virginity", "rape", "netorare", "cheating", "blackmail", "drugs", "sleeping", "chikan",
        "maid", "bunny girl", "kimono", "swimsuit", "bikini", "lingerie", "stockings", "pantyhose", "cosplaying"
    ]
    ## the Story row: not nhentai's; the change's pace, then the counted format tags
    VN_STORY_TAGS = [("gradual", _("gradual")), ("sudden", _("sudden")), ("branching", _("branching")),
                     ("multiple endings", _("multiple endings")), ("short", _("short")), ("long", _("long"))]
    VN_TAG_LABEL = dict([(t, t) for t in VN_TAGS] + VN_STORY_TAGS)
    ## the two TSF tags (owner 2026-11-17 ~4:50 pm ET) are the catalog's own words, not nhentai's, and show in capitals
    VN_TAG_LABEL.update({"tsf": "TSF", "soft tsf": "soft TSF"})
    VN_TAG_ORDER = VN_TAGS + [t for t, lab in VN_STORY_TAGS]

    def vn_tag_split(tags):
        """A tags line's tags: "a, b c, d" -> ["a", "b c", "d"]."""
        return [t.strip() for t in tags.split(",") if t.strip()]

    vn_route_tags = {
        "ace": ("2026-11-12", "tsf, sole female, huge breasts, anal, paizuri, rape, sudden, branching, multiple endings, long"),
        "afterhours": ("2026-11-12", "feminization, crossdressing, sole male, futanari, femdom, rape, sudden, branching"),
        "afterten": ("2026-11-12", "tsf, females only, yuri, futanari, big breasts, rape, sudden"),
        "ambassador": ("2026-11-12", "tsf, females only, yuri, futanari, milf, tentacles, anal, rape, gradual, short"),
        "amendment": ("2026-11-12", "tsf, mind control, females only, yuri, futanari, milf, blowjob, rape, gradual, branching"),
        "apprentice": ("2026-11-12", "tsf, sole female, rape, gradual, short"),
        "ashby": ("2026-11-12", "tsf, females only, yuri, futanari, rape, gradual, short"),
        "ashcombe": ("2026-11-12", "feminization, trap, crossdressing, futanari, milf, big penis, anal, rape, lingerie, stockings, pantyhose, branching, multiple endings, long"),
        "askme": ("2026-11-13", "tsf, sole female, rape, maid, cosplaying, sudden, branching"),
        "asleep": ("2026-11-16", "sole male, futanari, huge breasts, femdom, rape, drugs, sleeping, multiple endings, short"),
        "atelier": ("2026-11-14", "feminization, trap, futanari, leash, rape, lingerie, branching, multiple endings"),
        "audit": ("2026-11-12", "tsf, breast expansion, corruption, sole female, huge breasts, anal, rape, stockings, gradual, multiple endings"),
        "bait": ("2026-11-12", "tsf, transformation, yuri, futanari, monster, slime, orc, kemonomimi, tail, wings, lactation, rape, gradual, branching"),
        "baseline": ("2026-11-12", "tsf, sole female, anal, rape, sudden"),
        "bestman": ("2026-11-13", "tsf, breast expansion, huge breasts, anal, rape, gradual, branching, multiple endings"),
        "betatester": ("2026-11-16", "tsf, group, monster, orc, elf, anal, rape, sudden, short"),
        "bit": ("2026-11-12", "feminization, trap, crossdressing, sex toys, strap-on, chastity belt, rape, pantyhose, multiple endings, short"),
        "bloodline": ("2026-11-16", "tsf, transformation, group, milf, tail, horns, nakadashi, gradual, multiple endings"),
        "bloomwell": ("2026-11-13", "feminization, crossdressing, breast expansion, big breasts, rape, gradual, short"),
        "booth": ("2026-11-13", "rape, kimono, multiple endings"),
        "borrowed": ("2026-11-12", "tsf, bimbofication, skinsuit, corruption, group, milf, masturbation, rape, sudden, branching, multiple endings, long"),
        "bottle": ("2026-11-12", "tsf, sex toys, strap-on, rape, gradual"),
        "bounty": ("2026-11-15", "tsf, breast expansion, monster, huge breasts, anal, nakadashi, rape, gradual, branching, multiple endings"),
        "boytoy": ("2026-11-12", "feminization, crossdressing, transformation, males only, tail, wings, anal, rape, lingerie, stockings, sudden, branching, multiple endings, long"),
        "bree": ("2026-11-12", "tsf, sole female, huge breasts, big penis, anal, rape, gradual, branching, multiple endings, long"),
        "broker": ("2026-11-12", "tsf, breast expansion, body swap, females only, yuri, futanari, huge breasts, sex toys, strap-on, rape, gradual, multiple endings"),
        "burglar": ("2026-11-15", "trap, crossdressing, transformation, futanari, tail, rape, maid, gradual, branching, multiple endings"),
        "camellia": ("2026-11-12", "feminization, trap, crossdressing, milf, humiliation, rape, lingerie, multiple endings"),
        "celestia": ("2026-11-11", "tsf, corruption, magical girl, tentacles, catgirl, lactation, anal, paizuri, rape, sudden, branching, multiple endings, long"),
        "channel": ("2026-11-12", "tsf, soft tsf, breast expansion, corruption, females only, yuri, huge breasts, anal, bondage, exhibitionism, rape, maid, lingerie, gradual, branching, multiple endings, long"),
        "chef": ("2026-11-13", "tsf, blowjob, rape, gradual, short"),
        "cleo": ("2026-11-12", "males only, anal, nakadashi, rape, lingerie, stockings, branching, multiple endings, long"),
        "clover": ("2026-11-13", "feminization, transformation, breast expansion, mind control, sole male, futanari, cowgirl, big breasts, lactation, femdom, rape, sudden, branching, short"),
        "club": ("2026-11-12", "tsf, feminization, breast expansion, sole female, big breasts, anal, paizuri, rape, gradual, branching, multiple endings, long"),
        "coach": ("2026-11-16", "feminization, crossdressing, breast expansion, males only, big breasts, anal, sex toys, gradual, multiple endings"),
        "cockpit": ("2026-11-13", "tsf, breast expansion, futanari, monster, slime, huge breasts, anal, rape, gradual, branching, multiple endings"),
        "coco": ("2026-11-13", "feminization, futanari, chastity belt, exhibitionism, rape, sudden"),
        "collar": ("2026-11-11", "tsf, breast expansion, sole female, big breasts, anal, collar, rape, gradual, multiple endings"),
        "combattrack": ("2026-11-12", "tsf, breast expansion, futanari, big breasts, bondage, rape, kimono, sudden, branching, multiple endings"),
        "confirm": ("2026-11-12", "tsf, sole female, huge breasts, blowjob, bondage, rape, sudden"),
        "conrad": ("2026-11-12", "tsf, feminization, trap, sole female, rape, gradual, short"),
        "corner": ("2026-11-12", "soft tsf, feminization, crossdressing, breast expansion, group, futanari, big breasts, anal, blowjob, prostitution, rape, stockings, gradual, branching, multiple endings"),
        "corps": ("2026-11-11", "tsf, breast expansion, corruption, magical girl, monster, big breasts, anal, blowjob, rape, blackmail, gradual, branching, multiple endings, long"),
        "costume": ("2026-11-12", "tsf, magical girl, yuri, group, monster, tentacles, huge breasts, anal, paizuri, bondage, collar, rape, lingerie, stockings, sudden"),
        "council": ("2026-11-12", "tsf, females only, yuri, futanari, rape, gradual, short"),
        "cult": ("2026-11-16", "tsf, breast expansion, females only, yuri, futanari, milf, big breasts, lactation, rape, gradual, multiple endings, short"),
        "cure": ("2026-11-13", "feminization, crossdressing, males only, rape, gradual, short"),
        "curses": ("2026-11-13", "feminization, crossdressing, big breasts, exhibitionism, rape, lingerie, gradual"),
        "curve": ("2026-11-12", "tsf, females only, yuri, futanari, rape, gradual"),
        "dance": ("2026-11-17", "tsf, breast expansion, mind control, corruption, yuri, group, futanari, big breasts, big ass, anal, blowjob, nakadashi, double penetration, exhibitionism, virginity, rape, gradual, branching, multiple endings"),
        "dani": ("2026-11-12", "feminization, crossdressing, rape, gradual, short"),
        "daria": ("2026-11-13", "tsf, breast expansion, tentacles, big breasts, anal, bondage, rape, gradual, branching, multiple endings"),
        "deepcover": ("2026-11-12", "tsf, feminization, breast expansion, sole female, big breasts, rape, gradual, multiple endings"),
        "delilah": ("2026-11-12", "feminization, trap, crossdressing, rape, sudden, short"),
        "dollapp": ("2026-11-16", "feminization, trap, crossdressing, mind control, males only, anal, rape, multiple endings, short"),
        "duelist": ("2026-11-16", "tsf, breast expansion, futanari, tentacles, huge breasts, lactation, anal, sex toys, strap-on, rape, stockings, gradual, branching, multiple endings, long"),
        "equipslot": ("2026-11-12", "tsf, futanari, paizuri, rape, stockings, sudden, multiple endings"),
        "escaperoom": ("2026-11-15", "trap, crossdressing, futanari, rape, lingerie, stockings, branching, multiple endings"),
        "evidence": ("2026-11-13", "tsf, breast expansion, futanari, big breasts, rape, sudden, branching, multiple endings"),
        "fantasies": ("2026-11-12", "feminization, trap, crossdressing, males only, elf, rape, maid, bunny girl, short"),
        "fever": ("2026-11-13", "tsf, futanari, rape, gradual, short"),
        "fitting": ("2026-11-12", "tsf, feminization, breast expansion, corruption, group, tentacles, big breasts, big penis, rape, stockings, gradual, branching, multiple endings, long"),
        "fivestars": ("2026-11-12", "feminization, corruption, sole male, group, futanari, anal, sex toys, strap-on, femdom, rape, gradual, branching, multiple endings, long"),
        "flyer": ("2026-11-12", "mind control, rape, short"),
        "fullclear": ("2026-11-12", "tsf, mind control, futanari, idol, lactation, rape, sudden, multiple endings"),
        "fusion": ("2026-11-16", "tsf, breast expansion, females only, yuri, big breasts, rape, gradual, multiple endings, short"),
        "gacha": ("2026-11-12", "tsf, trap, transformation, possession, group, futanari, elf, kemonomimi, tail, rape, maid, bunny girl, cosplaying, sudden, branching, multiple endings"),
        "gains": ("2026-11-12", "tsf, females only, yuri, futanari, paizuri, rape, sudden, branching, short"),
        "girlpill": ("2026-11-12", "tsf, sole female, big penis, rape, sudden, short"),
        "glutes": ("2026-11-12", "soft tsf, feminization, crossdressing, breast expansion, corruption, males only, big breasts, big ass, anal, rape, gradual, branching, multiple endings, long"),
        "greathawk": ("2026-11-12", "tsf, transformation, breast expansion, sole female, monster, tail, wings, huge breasts, anal, rape, gradual, branching, multiple endings, long"),
        "guild": ("2026-11-12", "tsf, breast expansion, milf, tentacles, huge breasts, anal, nakadashi, rape, bikini, lingerie, sudden, multiple endings, long"),
        "gyaru": ("2026-11-16", "tsf, mind control, futanari, gyaru, huge breasts, gradual, short"),
        "hairclip": ("2026-11-12", "rape, short"),
        "halves": ("2026-11-15", "tsf, breast expansion, sole female, big breasts, nakadashi, rape, sudden, multiple endings"),
        "harem": ("2026-11-13", "feminization, group, harem, milf, dark skin, big breasts, lactation, blowjob, paizuri, nakadashi, rape, gradual, branching"),
        "heat": ("2026-11-13", "tsf, futanari, rape, sudden, short"),
        "heirloom": ("2026-11-12", "tsf, body swap, futanari, rape, kimono, sudden, branching"),
        "hen": ("2026-11-12", "feminization, crossdressing, males only, huge breasts, anal, blowjob, sex toys, rape, cheating, sudden"),
        "hollowpine": ("2026-11-12", "mind control, sole male, futanari, big breasts, femdom, rape, branching, multiple endings"),
        "honeypot": ("2026-11-15", "tsf, rape, sudden, branching, multiple endings, short"),
        "honeystar": ("2026-11-13", "tsf, magical girl, females only, yuri, futanari, exhibitionism, rape, sudden, short"),
        "hunt": ("2026-11-15", "tsf, transformation, breast expansion, sole female, group, tail, horns, big breasts, rape, gradual, branching, multiple endings"),
        "hypno": ("2026-11-11", "soft tsf, feminization, trap, crossdressing, mind control, anal, multiple endings, long"),
        "institut": ("2026-11-14", "feminization, trap, crossdressing, futanari, leash, rape, lingerie, stockings, branching, multiple endings"),
        "island": ("2026-11-16", "tsf, breast expansion, huge breasts, rape, gradual, branching, multiple endings"),
        "jelly": ("2026-11-15", "tsf, breast expansion, futanari, monster, slime, big breasts, blowjob, rape, gradual, branching, multiple endings"),
        "juice": ("2026-11-12", "soft tsf, feminization, crossdressing, breast expansion, sole male, group, futanari, huge breasts, blowjob, femdom, rape, gradual, multiple endings"),
        "keywords": ("2026-11-12", "tsf, tentacles, huge breasts, big penis, anal, nakadashi, rape, gradual, short"),
        "lacey": ("2026-11-12", "feminization, trap, crossdressing, milf, rape, short"),
        "ladiescar": ("2026-11-16", "tsf, breast expansion, females only, yuri, futanari, big breasts, nakadashi, rape, chikan, gradual, multiple endings, short"),
        "laura": ("2026-11-12", "tsf, transformation, breast expansion, sole female, monster, wings, huge breasts, anal, rape, sudden, branching, multiple endings, long"),
        "ledger": ("2026-11-12", "soft tsf, feminization, crossdressing, transformation, breast expansion, corruption, futanari, tail, horns, wings, big breasts, rape, gradual, branching, multiple endings, long"),
        "lifeclass": ("2026-11-12", "feminization, corruption, anal, sex toys, strap-on, rape, gradual, multiple endings, long"),
        "lightsout": ("2026-11-12", "sole male, futanari, anal, femdom, rape, short"),
        "livestock": ("2026-11-11", "tsf, transformation, breast expansion, corruption, females only, yuri, group, futanari, kemonomimi, tail, horns, cowgirl, big breasts, lactation, anal, paizuri, rape, gradual, branching, multiple endings, long"),
        "locktober": ("2026-11-12", "males only, group, anal, chastity belt, rape, swimsuit, short"),
        "mal": ("2026-11-13", "soft tsf, feminization, crossdressing, breast expansion, possession, big breasts, collar, humiliation, rape, sudden, branching, multiple endings, long"),
        "maron": ("2026-11-17", "tsf, breast expansion, mind control, corruption, females only, yuri, group, futanari, vampire, huge breasts, big ass, anal, paizuri, nakadashi, virginity, rape, maid, stockings, gradual, branching, multiple endings"),
        "markers": ("2026-11-11", "tsf, transformation, breast expansion, futanari, tail, big breasts, anal, rape, gradual, branching, multiple endings, long"),
        "membership": ("2026-11-16", "tsf, mind control, females only, yuri, futanari, drugs, gradual, short"),
        "mentorship": ("2026-11-12", "tsf, breast expansion, mind control, females only, yuri, group, futanari, milf, idol, big breasts, anal, rape, gradual, branching, multiple endings"),
        "meridian": ("2026-11-12", "tsf, mind control, females only, yuri, futanari, anal, rape, gradual"),
        "mistaken": ("2026-11-11", "tsf, trap, breast expansion, big breasts, anal, exhibitionism, bikini, lingerie, sudden, multiple endings"),
        "moon": ("2026-11-12", "tsf, breast expansion, sole female, group, big breasts, nakadashi, rape, gradual, multiple endings"),
        "moonflower": ("2026-11-16", "feminization, trap, crossdressing, breast expansion, futanari, idol, big breasts, anal, blowjob, sex toys, strap-on, lingerie, stockings, gradual, multiple endings"),
        "neckdown": ("2026-11-12", "tsf, breast expansion, body swap, females only, yuri, futanari, big breasts, anal, paizuri, rape, sudden, multiple endings, long"),
        "neighbour": ("2026-11-11", "tsf, breast expansion, females only, yuri, futanari, big breasts, paizuri, chastity belt, gradual, branching, multiple endings"),
        "nevercameup": ("2026-11-12", "tsf, breast expansion, sole female, big breasts, rape, gradual, branching, multiple endings"),
        "newgirl": ("2026-11-12", "futanari, rape, short"),
        "newmum": ("2026-11-15", "tsf, breast expansion, milf, big breasts, nakadashi, rape, gradual, multiple endings"),
        "nose": ("2026-11-12", "tsf, transformation, breast expansion, sole female, tail, big breasts, anal, nakadashi, rape, lingerie, gradual, multiple endings"),
        "notanlines": ("2026-11-12", "tsf, breast expansion, group, futanari, big breasts, tanlines, anal, blowjob, rape, gradual, multiple endings, long"),
        "nyanko": ("2026-11-12", "tsf, transformation, sole female, catgirl, tail, rape, gradual, short"),
        "odette": ("2026-11-14", "feminization, trap, transformation, mind control, futanari, wings, leash, rape, pantyhose, branching, multiple endings"),
        "oiran": ("2026-11-14", "tsf, breast expansion, big breasts, prostitution, rape, kimono, gradual, multiple endings"),
        "otherwoman": ("2026-11-12", "tsf, females only, yuri, futanari, rape, gradual"),
        "patchnotes": ("2026-11-15", "tsf, breast expansion, big breasts, bondage, rape, sudden, branching, multiple endings"),
        "pavilion": ("2026-11-12", "soft tsf, feminization, crossdressing, breast expansion, sole male, futanari, big breasts, anal, femdom, rape, gradual, multiple endings, long"),
        "payback": ("2026-11-15", "tsf, breast expansion, mind control, big breasts, leash, rape, lingerie, gradual, multiple endings"),
        "petticoat": ("2026-11-14", "feminization, trap, crossdressing, futanari, rape, maid, lingerie, stockings, branching, multiple endings"),
        "playlists": ("2026-11-12", "futanari, rape, short"),
        "plug": ("2026-11-12", "tsf, transformation, females only, yuri, futanari, tail, collar, leash, rape, gradual, branching"),
        "poll": ("2026-11-12", "futanari, sex toys, strap-on, rape"),
        "practice": ("2026-11-12", "tsf, soft tsf, trap, breast expansion, big breasts, anal, paizuri, rape, gradual, branching, multiple endings, long"),
        "president": ("2026-11-16", "soft tsf, feminization, trap, crossdressing, breast expansion, huge breasts, nakadashi, sex toys, strap-on, rape, blackmail, lingerie, stockings, gradual, branching, multiple endings"),
        "pressit": ("2026-11-12", "tsf, breast expansion, corruption, futanari, huge breasts, anal, rape, swimsuit, bikini, sudden, branching, multiple endings, long"),
        "profile": ("2026-11-15", "feminization, trap, crossdressing, futanari, rape, branching, multiple endings, short"),
        "qualifying": ("2026-11-12", "tsf, breast expansion, futanari, big breasts, rape, swimsuit, sudden, multiple endings"),
        "quota": ("2026-11-12", "tsf, breast expansion, sole female, huge breasts, paizuri, exhibitionism, rape, maid, pantyhose, sudden, multiple endings"),
        "ranch": ("2026-11-12", "tsf, transformation, milf, monster, kemonomimi, tail, huge breasts, lactation, paizuri, rape, gradual, short"),
        "rascal": ("2026-11-12", "tsf, transformation, breast expansion, females only, yuri, futanari, tail, huge breasts, sex toys, strap-on, rape, gradual, branching, multiple endings, long"),
        "receptionist": ("2026-11-15", "tsf, futanari, milf, monster, tentacles, orc, elf, huge breasts, rape, gradual"),
        "redlightning": ("2026-11-11", "tsf, breast expansion, sole female, big breasts, anal, paizuri, rape, gradual, multiple endings, long"),
        "relief": ("2026-11-15", "tsf, breast expansion, group, big breasts, anal, nakadashi, leash, rape, pantyhose, gradual, multiple endings, long"),
        "rematch": ("2026-11-12", "tsf, futanari, monster, rape, gradual, short"),
        "rendered": ("2026-11-12", "tsf, females only, yuri, rape, gradual, short"),
        "respec": ("2026-11-12", "tsf, futanari, rape, gradual, short"),
        "returnrate": ("2026-11-12", "tsf, sole female, rape, sudden"),
        "reward": ("2026-11-16", "tsf, futanari, big breasts, rape, kimono, pantyhose, gradual, short"),
        "rurika": ("2026-11-12", "tsf, trap, futanari, rape, cosplaying, gradual"),
        "rushhour": ("2026-11-15", "tsf, breast expansion, big breasts, nakadashi, rape, chikan, pantyhose, gradual, multiple endings"),
        "sabrina": ("2026-11-12", "soft tsf, feminization, crossdressing, breast expansion, mind control, males only, big breasts, anal, rape, gradual, branching, multiple endings, long"),
        "samebrand": ("2026-11-12", "feminization, crossdressing, males only, rape, drugs, gradual"),
        "saturday": ("2026-11-13", "tsf, breast expansion, futanari, big breasts, rape, gradual, branching, multiple endings, long"),
        "scales": ("2026-11-12", "tsf, transformation, breast expansion, corruption, futanari, monster, tail, horns, huge breasts, anal, rape, gradual, branching, multiple endings, long"),
        "scion": ("2026-11-15", "tsf, futanari, big breasts, blowjob, masturbation, prostitution, rape, gradual, multiple endings"),
        "screenaccurate": ("2026-11-12", "tsf, trap, body swap, mind control, females only, yuri, futanari, big breasts, paizuri, masturbation, sex toys, rape, lingerie, pantyhose, cosplaying, gradual, multiple endings"),
        "season": ("2026-11-13", "tsf, breast expansion, big breasts, rape, gradual, branching, multiple endings"),
        "secondvial": ("2026-11-12", "tsf, breast expansion, big breasts, lactation, rape, sudden"),
        "senpai": ("2026-11-17", "tsf, breast expansion, sole female, group, huge breasts, big ass, mind break, anal, blowjob, nakadashi, masturbation, virginity, exhibitionism, bikini, rape, gradual, multiple endings"),
        "sexcross": ("2026-11-17", "tsf, futanari, huge breasts, kimono, gradual, short"),
        "shipsstores": ("2026-11-12", "tsf, breast expansion, sole female, group, big breasts, anal, rape, lingerie, gradual, branching, multiple endings, long"),
        "shrine": ("2026-11-12", "tsf, transformation, breast expansion, possession, sole female, monster, kemonomimi, tail, miko, big breasts, anal, masturbation, rape, gradual, multiple endings, long"),
        "silo": ("2026-11-13", "feminization, males only, rape, gradual, short"),
        "sissyedition": ("2026-11-12", "feminization, trap, sex toys, strap-on, rape, drugs, gradual, short"),
        "sister": ("2026-11-11", "tsf, breast expansion, females only, yuri, futanari, big breasts, rape, gradual, multiple endings, long"),
        "sleeper": ("2026-11-15", "tsf, breast expansion, big breasts, rape, bikini, lingerie, sudden, branching, multiple endings"),
        "slimefruit": ("2026-11-13", "feminization, crossdressing, sole male, slime, femdom, rape, bikini, gradual, short"),
        "slipper": ("2026-11-15", "tsf, breast expansion, futanari, big breasts, rape, maid, sudden, branching, multiple endings"),
        "smartdrug": ("2026-11-12", "tsf, futanari, milf, rape, drugs, gradual, short"),
        "snowedin": ("2026-11-12", "sole male, futanari, anal, femdom, rape, short"),
        "spincycle": ("2026-11-12", "tsf, breast expansion, corruption, females only, yuri, futanari, huge breasts, blowjob, paizuri, sex toys, strap-on, rape, stockings, gradual, branching, multiple endings, long"),
        "spinning": ("2026-11-15", "tsf, transformation, breast expansion, wings, big breasts, rape, gradual, branching, multiple endings"),
        "spotter": ("2026-11-12", "mind control, sole male, futanari, femdom, rape, short"),
        "standin": ("2026-11-14", "tsf, breast expansion, futanari, big breasts, leash, rape, sudden, multiple endings"),
        "stoppedtime": ("2026-11-12", "tsf, time stop, futanari, blowjob, rape, gradual"),
        "suggestible": ("2026-11-16", "tsf, breast expansion, mind control, big breasts, sex toys, strap-on, lingerie, gradual, branching, multiple endings"),
        "summoning": ("2026-11-12", "tsf, futanari, rape, gradual, short"),
        "swimmersear": ("2026-11-13", "feminization, males only, rape, gradual"),
        "sword": ("2026-11-13", "tsf, breast expansion, futanari, big breasts, rape, gradual, branching, multiple endings"),
        "tabitha": ("2026-11-12", "mind control, sole male, futanari, femdom, rape"),
        "templecat": ("2026-11-15", "tsf, transformation, breast expansion, catgirl, kemonomimi, tail, dark skin, big breasts, rape, gradual, branching, multiple endings"),
        "tenant": ("2026-11-13", "tsf, futanari, monster, slime, rape, gradual"),
        "terms": ("2026-11-12", "tsf, futanari, rape, gradual, short"),
        "torishimari": ("2026-11-12", "tsf, breast expansion, magical girl, sole female, group, monster, tentacles, huge breasts, big penis, anal, paizuri, nakadashi, rape, stockings, sudden, branching, multiple endings, long"),
        "transplant": ("2026-11-16", "tsf, milf, huge breasts, masturbation, rape, gradual, multiple endings, short"),
        "tribute": ("2026-11-12", "feminization, males only, group, elf, big breasts, anal, blowjob, paizuri, rape, sudden"),
        "twin": ("2026-11-12", "tsf, sole female, rape, sudden, short"),
        "velvet": ("2026-11-12", "feminization, males only, monster, big breasts, anal, rape, stockings, gradual"),
        "venus": ("2026-11-11", "tsf, breast expansion, harem, big breasts, paizuri, rape, gradual, branching, multiple endings"),
        "villa": ("2026-11-13", "feminization, trap, futanari, rape, bikini, branching, multiple endings"),
        "vote": ("2026-11-12", "tsf, group, big breasts, anal, blowjob, rape, cosplaying, gradual, multiple endings"),
        "wager": ("2026-11-12", "tsf, sole female, paizuri, rape, sudden"),
        "warlock": ("2026-11-16", "tsf, transformation, breast expansion, yuri, monster, demon girl, tail, horns, wings, huge breasts, anal, masturbation, rape, gradual, branching, multiple endings"),
        "waterbuffs": ("2026-11-12", "tsf, breast expansion, sole female, big breasts, rape, sudden, branching, multiple endings, long"),
        "witches": ("2026-11-12", "feminization, crossdressing, transformation, futanari, wings, witch, anal, rape, sudden, branching, multiple endings, long"),
        "witness": ("2026-11-15", "tsf, mind control, futanari, rape, maid, gradual, branching, multiple endings, short"),
        "wizard": ("2026-11-16", "tsf, breast expansion, futanari, big breasts, rape, gradual, multiple endings, short"),
        "wolfpack": ("2026-11-12", "tsf, transformation, breast expansion, corruption, sole female, group, monster, kemonomimi, tail, big breasts, lactation, rape, gradual, branching, multiple endings, long"),
        "womensbath": ("2026-11-12", "tsf, females only, yuri, rape, gradual, branching, multiple endings"),
        "yinbody": ("2026-11-12", "tsf, breast expansion, huge breasts, masturbation, rape, gradual, branching, multiple endings"),
        "yourtype": ("2026-11-12", "tsf, breast expansion, sole female, big breasts, anal, rape, gradual, multiple endings, long"),
    }

    def vn_tags_check(table):
        """Every tag known, none twice, at most one pace, a date that sorts. Raises ValueError (lint and
        tools/tags_check.py both run this), so a typo never reaches a player."""
        import re as _re
        for rid, (built, tags) in table.items():
            ts = vn_tag_split(tags)
            if not _re.match(r"^\d{4}-\d{2}-\d{2}$", built):
                raise ValueError("tags.rpy: %s: built %r isn't YYYY-MM-DD" % (rid, built))
            bad = [t for t in ts if t not in VN_TAG_LABEL]
            if bad:
                raise ValueError("tags.rpy: %s: unknown tag(s) %s (commas between tags; add a new one to VN_TAGS)"
                                 % (rid, ", ".join(repr(t) for t in bad)))
            if len(set(ts)) != len(ts):
                raise ValueError("tags.rpy: %s: a tag twice" % rid)
            if "gradual" in ts and "sudden" in ts:
                raise ValueError("tags.rpy: %s: gradual or sudden, not both" % rid)

    vn_tags_check(vn_route_tags)
