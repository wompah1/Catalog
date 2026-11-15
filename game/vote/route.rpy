## Vote -- "Best Girl? Teal or Red" (a new route, written straight in Ren'Py, 2026-11-12, from the
## paired packages beside this file, PACKAGE-teal.md and PACKAGE-red.md; the plan is PLAN.md, signed
## off by the owner). Shelf: TSF (full). One shared first night; the vote picks the path; two
## endings: teal "Now I Say Please to Men", red "Now Guys Can't Keep Up".
##
## THE NON-CON PASS (the owner, 2026-11-12: "do what you see fit, you have more free reign to
## actually rewrite this story as needed as its a package"). THE BODY MOVES FIRST (neckdown's
## pattern): rungs 1-2 solo, as packaged; rungs 3-4, the first men, his body acts on the urge while
## his head protests out loud (he's straight, he likes Jesse, he doesn't do this), the partner
## answers the body, and the chorus line at the peak is the break. Rung 5 the flip, "ahead of her":
## the act is his own. Rung 6 consensual. He never connects any of it to the videos and loves every
## change to his body. No dread, no pain, no menace, no tears.
##
## THE LADDER is the timing, seen only by the reader: a day behind, hours behind, while it plays, in
## sync, ahead of her, the upload is him. The chorus is the device: sung once in the upload, said
## once by him at the peak. The comment section sees everything (screen vt_phone).
##
## The phone's title cards use 【】, which DejaVuSans lacks: SourceHanSansLite.ttf (from the SDK's
## sdk-fonts, the SIL Open Font License; Adobe's Source Han Sans) carries those two glyphs only, in
## a font group over DejaVuSans.
##
## All names carry vt_.

init -10 python:
    VT = "art/vote/"

    VT_FONT = FontGroup().add("vote/SourceHanSansLite.ttf", 0x3010, 0x3011).add("DejaVuSans.ttf", None, None)

    VT_DAYS = ("Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon")

    def vt_weekday():
        return VT_DAYS[(max(1, vn_clock.day) - 1) % 7]

    vn_weekdays["vote"] = vt_weekday

    # THE UPLOADS: the title card, then the comments, one paragraph each, no usernames. The chorus
    # is never here: it's sung once in the upload itself (the singer's line in the script).
    VT_UPLOADS = {
        "duet": dict(card="【Shizune Mio × Sawane Kiki】Turn Me Up【Original PV】", pinned="best girl? teal or red",
            comments=["the bonus scene. THE BONUS SCENE.",
                      "is it me or is the model thicker than last video",
                      "mio covering her mouth like that should be illegal"]),
        "t2": dict(card="【Shizune Mio】Bubble Bath Apology【Original PV】",
            comments=["she apologised more than she sang",
                      "her model got thicker again",
                      ";_; ;_; ;_; ;_; ;_;"]),
        "t3": dict(card="【Shizune Mio】Practice Kiss【Original PV】",
            comments=["FIRST BOYFRIEND APPEARANCE",
                      "the model is thicker again and I'm not complaining",
                      "she sounds like she's actually breathing",
                      "asdfghjkl;;;;"]),
        "t4": dict(card="【Shizune Mio】First Date Etiquette【Original PV】",
            comments=["she apologised to the couch",
                      "her model is thicker AGAIN",
                      "the way she says please"]),
        "t5": dict(card="【Shizune Mio】First Date Etiquette【Original PV】",
            comments=["is nightshiftP okay",
                      "where's Mio",
                      "two weeks without her I'm going insane"]),
        "t6a": dict(card="【Shizune Mio】Backstage【Original PV】",
            comments=["this one feels so real",
                      "MODEL UPDATE AGAIN",
                      "is it just me or is she actually breathing"]),
        "t6b": dict(card="【Shizune Mio】Play Me Again【Original PV】",
            comments=["her voice sounds so real now"]),
        "r2": dict(card="【Sawane Kiki】Personal Best【Original PV】",
            comments=["she's so rude and I love her",
                      "her model got thicker again",
                      "the bench is doing its best"]),
        "r3": dict(card="【Sawane Kiki】Bad Habit【Original PV】",
            comments=["SHE'S SO RUDE",
                      "her model got thicker AGAIN",
                      "the fang. the FANG",
                      "hfjdkslfhdjskl"]),
        "r4": dict(card="【Sawane Kiki】Two Can Play【Original PV】",
            comments=["she told them not to go easy and they listened",
                      "her model is thicker AGAIN",
                      "two of them and she's still the one talking"]),
        "r5": dict(card="【Sawane Kiki】Two Can Play【Original PV】",
            comments=["where's Kiki",
                      "nightshiftP is this a hiatus",
                      "I need her back I'm begging"]),
        "r6a": dict(card="【Sawane Kiki】Encore【Original PV】",
            comments=["this one feels so real",
                      "MODEL UPDATE AGAIN",
                      "is it just me or is she actually breathing"]),
        "r6b": dict(card="【Sawane Kiki】Again【Original PV】",
            comments=["her voice sounds so real now"]),
    }

    # THE IN-VOICE LINE: one in each scene, at the mid-point, in that rung's voice. Consent-split:
    # rungs 3-4 are the body-moves-first scenes, so their lines are the head's protest. Solo rungs
    # (2) are his own. Keys: (path, rung).
    VT_VOICE = {
        ("teal", 2): {"a": "\"Sorry— sorry, I'm so sorry, I'm being so loud—\"",
                      "b": "\"Can I— can I have one more finger? Just one? Sorry—\"",
                      "c": "\"Thank you— oh, thank you, oh God, thank you—\""},
        ("teal", 3): {"a": "\"Sorry— mmf— sorry, Darren, I don't— I'm not like this, I swear I'm not—\"",
                      "b": "\"Could you— could you hold my head still? So it stops? Please? It won't stop—\"",
                      "c": "\"Thank you— no, wait, why am I— mmf— thank you—\""},
        ("teal", 4): {"a": "\"Sorry, I'm sorry, my hands did that, I didn't— Darren, I didn't mean—\"",
                      "b": "\"Could you— please could you stop? Please— no, please don't— I don't know—\"",
                      "c": "\"Thank you— why do I keep— {i}ah{/i}— thank you—\""},
        ("teal", 5): {"a": "\"Sorry, I'm so wet— I'm so— is that okay? Sorry—\"",
                      "b": "\"Could you go harder? Please? If it's not too much trouble?\"",
                      "c": "\"Thank you for coming backstage. Thank you. {i}Thank{/i} you.\""},
        ("teal", 6): {"a": "\"Sorry they're so big— sorry, are they in the way? Sorry—\"",
                      "b": "\"Could you both— could you both not stop? Ever? Please?\"",
                      "c": "\"Thank you. Thank you both. You're so good to me—\""},
        ("red", 2): {"a": "\"Lazy. You're {i}lazy{/i}. I've had better from a {i}phone charger{/i}—\"",
                     "b": "\"Harder. I said harder. Do I have to do {i}everything{/i} myself?\"",
                     "c": "\"Heh— heh-heh— look at you. Look at you trying.\""},
        ("red", 3): {"a": "\"Mmf— you're not— this isn't— I'm not into blokes, idiot—\"",
                     "b": "\"Get off— no, don't get— mmf— what is my {i}mouth{/i} doing—\"",
                     "c": "\"Hah— hah, why am I grinning— stop making me grin, idiot—\""},
        ("red", 4): {"a": "\"Turn it off— Jesse, turn it {i}off{/i}— that's not me, I'm not doing that—\"",
                     "b": "\"Out. Get out. Don't you— don't you {i}dare{/i} stop— no, I mean get {i}out{/i}—\"",
                     "c": "\"Hah— you two are— this isn't— why am I {i}laughing{/i}—\""},
        ("red", 5): {"a": "\"Is that it? Is that all the bartender's got? In front of {i}everyone{/i}?\"",
                     "b": "\"Harder. Harder, idiot, they can't hear me yet.\"",
                     "c": "\"Hah— look at them. Look at them all watching you lose.\""},
        ("red", 6): {"a": "\"Is that all you lot have got? Three of you? I'm {i}bored{/i}—\"",
                     "b": "\"Harder. Both of you. I want to feel you bump into each other.\"",
                     "c": "\"Heh— Andre, your face— look at his {i}face{/i}—\""},
    }

    VT_VOICE_CAPS = {"teal": ("Apologise", "Ask nicely", "Thank him"),
                     "red": ("Trash-talk", "Demand", "Grin")}

    def vt_init():
        if vt.body is None:
            vt.body = 0

    def vt_grow(n):
        vt.body = max(vt.body or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # PC rows: c0 Colby, c1 hairless (shared); t2-t6 teal, r2-r6 red (rung 6 after the face
    # finishes). Outfits: "work" (shirt, jeans, kiosk apron), "home" (an old T-shirt and shorts),
    # "bra" (teal: Jesse's borrowed bra and jeans; red: the bought bra and Jesse's leggings), "cos"
    # (the con / club cosplay), "nude".
    _vt_have = {}

    def _vt_has(n):
        if n not in _vt_have:
            _vt_have[n] = renpy.loadable(VT + n + ".png")
        return _vt_have[n]

    def vt_row():
        b = max(0, min(6, vt.body or 0))
        if b < 2 or not vt.path:
            return "c%d" % min(b, 1)
        return ("t%d" if vt.path == "teal" else "r%d") % b

    def vt_pc_file(face):
        r, fit = vt_row(), vt.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-grinning" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-grinning" % r]
        for n in names:
            if _vt_has(n):
                return VT + n + ".png"
        return VT + names[-1] + ".png"

    def vt_face_now():
        a = renpy.get_attributes("vt_pc")
        return a[0] if a else "grinning"

    def _vt_portrait(st, at):
        p = vn_art_file(vt_pc_file(vt_face_now()))
        crops = globals().get("vote_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["vote"] = lambda: DynamicDisplayable(_vt_portrait)

    def vt_jesse_file(f):
        if f == "cos":
            f = "cos-kiki" if vt.path == "teal" else "cos-mio"
        return VT + "jesse-" + f + ".png"

    vn_sprite_image("vt_pc", ("grinning", "horny", "shy", "smirk", "protesting", "moaning", "glitch"), vt_pc_file, who="pc")
    vn_sprite_image("vt_jesse", ("grinning", "flushed", "cos"), vt_jesse_file)
    vn_sprite_image("vt_darren", ("calm", "dazed"), lambda f: VT + "darren-" + f + ".png")
    vn_sprite_image("vt_nico", ("grin", "dazed"), lambda f: VT + "nico-" + f + ".png")
    vn_sprite_image("vt_rafe", ("laugh", "dazed"), lambda f: VT + "rafe-" + f + ".png")
    vn_sprite_image("vt_andre", ("quiet",), lambda f: VT + "andre-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(VT) and _f.endswith(".jpg"):
            _n = _f[len(VT):-4]
            vn_register_bg("vt_" + _n.replace("-", "_"), _f)
            vn_register_cg("vt_" + _n.replace("-", "_"), _f)


    vn_register_route("vote", "Best Girl? Teal or Red",
        "You fix cracked screens at a kiosk in the Eastgate shopping centre. Jesse, from the hobby shop next door, sends you a link: you'll hate this, it's so dumb. An indie channel, two original virtual singers, shy teal Shizune Mio and loud red Sawane Kiki, and a lewder song every week at three in the morning. Under the newest one, the pinned comment asks: best girl? teal or red.",
        VT + "cover.jpg", "vote_start")

    achievement.register("Now I Say Please to Men")
    achievement.register("Now Guys Can't Keep Up")

default vt = VNState(body=0)
default vt_pc_name = "Colby"

## The speakers. You under your name; the singers, on screens only, in their colours; the rest in
## theirs.
define vt_you = VNChar("[vt_pc_name]", who="pc", plate="#7a7f8c")
define vt_jesse = VNChar("Jesse", who="vt_jesse", plate="#b0663a")
define vt_darren = VNChar("Darren", who="vt_darren", plate="#4f6a5a")
define vt_nico = VNChar("Nico", who="vt_nico", plate="#6a4a7a")
define vt_rafe = VNChar("Rafe", who="vt_rafe", plate="#7a5a3a")
define vt_andre = VNChar("Andre", who="vt_andre", plate="#3a5a7a")
define vt_mio = VNChar("Shizune Mio ♪", who="screen", plate="#2aa89a")
define vt_kiki = VNChar("Sawane Kiki ♪", who="screen", plate="#c8303a")
define vt_duet = VNChar("Mio × Kiki ♪", who="screen", plate="#7a6a8a")
define vt_teal_end = VNChar("[vt_pc_name] · the phone ♪", who="pc", plate="#2aa89a")
define vt_red_end = VNChar("[vt_pc_name] · the phone ♪", who="pc", plate="#c8303a")
define vt_customer = VNChar("A customer", who="man", plate="#6b6b78")
define vt_clerk = VNChar("The fitter", who="woman", plate="#8a6b7a")
define vt_dj = VNChar("The DJ", who="man", plate="#6b6b78")
define vt_crowd = VNChar("The crowd", who="room", plate="#6b6b78")
define vt_wall = VNChar("Through the wall", who="man", plate="#4f6a5a")

## THE PHONE: his cracked screen over the scene, the channel page: the title card, nightshiftP, the
## pinned comment (the duet), the comments one paragraph each with no usernames, and the reply box
## (the vote). The only place the comments print.
style vt_phone_card is text:
    font VT_FONT
    size 25
    bold True
    color "#f2f2f6"
style vt_phone_small is text:
    font "DejaVuSans.ttf"
    size 18
    color "#9a9aaa"
style vt_phone_text is text:
    font "DejaVuSans.ttf"
    size 21
    color "#e2e2ea"

screen vt_phone(key, reply=None):
    zorder 50
    $ up = VT_UPLOADS[key]
    frame:
        xalign 0.5
        ypos 46
        xsize 660
        padding (30, 26, 30, 26)
        background Solid("#0d0d12f6")
        vbox:
            spacing 12
            text up["card"] style "vt_phone_card" xsize 600
            text "nightshiftP" style "vt_phone_small"
            add Solid("#2a2a34") xsize 600 ysize 2
            if up.get("pinned"):
                hbox:
                    spacing 10
                    text "Pinned" style "vt_phone_small" color "#e8c15a"
                    text up["pinned"] style "vt_phone_text" bold True
            for c in up["comments"]:
                hbox:
                    spacing 14
                    add Solid("#3a3a48") xysize (34, 34)
                    text c style "vt_phone_text" xsize 540
            if reply is not None:
                add Solid("#2a2a34") xsize 600 ysize 2
                frame:
                    background Solid("#1c1c26")
                    padding (16, 10, 16, 10)
                    xsize 600
                    hbox:
                        text reply style "vt_phone_text" min_width 480
                        text "Send" style "vt_phone_small" color "#7fb0e8"
    ## the crack in the screen protector, across the top corner
    add Transform(Solid("#ffffff40", xysize=(260, 2)), rotate=-28) xpos 1180 ypos 70
    add Transform(Solid("#ffffff30", xysize=(150, 2)), rotate=12) xpos 1240 ypos 96

## Route select's entry. Tuesday afternoon, the kiosk.
label vote_start:
    $ vt = VNState(body=0, fit="work", path=None)
    $ vn_clock = VNState(day=1, hour=16, minute=20)
    $ vt_pc_name = "Colby"
    ## the name box: Colby, unless you'd like another. A test walk keeps Colby.
    if not renpy.session.get("vn_picks"):
        $ vt_pc_name = renpy.input("Your name? (Colby, unless you'd like another.)", default="Colby", length=20).strip() or "Colby"
    $ vn_route = "vote"
    jump vt_one_kiosk

## A gap between uploads: a title card in words, then the day.
label vt_gap(card, day, wake=8):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    centered "{i}[card]{/i}"
    $ vn_clock.day = day
    $ vn_set_time(wake, 0)
    window auto
    return

## A small-hours sleep: after a 3 am upload the morning is the same day (vn_night would add one).
label vt_sleep_till(wake=8):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

## "Watch it again": he always does; the other option gets there a beat later.
label vt_again:
    menu:
        "It ends. The comments load."
        "Watch it again":
            "You watch it again."
        "Close the app":
            "You close the app. You open the app. You watch it again."
    return

## The in-voice line, at a scene's mid-point (VT_VOICE).
label vt_voice(rung):
    $ _vt_c = VT_VOICE_CAPS[vt.path]
    $ _vt_v = VT_VOICE[(vt.path, rung)]
    if vt.path == "teal":
        menu:
            "Your mouth's your own for one breath."
            "Apologise":
                $ _vt_l = _vt_v["a"]
            "Ask nicely":
                $ _vt_l = _vt_v["b"]
            "Thank him":
                $ _vt_l = _vt_v["c"]
    else:
        menu:
            "Your mouth's your own for one breath."
            "Trash-talk":
                $ _vt_l = _vt_v["a"]
            "Demand":
                $ _vt_l = _vt_v["b"]
            "Grin":
                $ _vt_l = _vt_v["c"]
    vt_you "[_vt_l]"
    return

## The end of the route: back to the route select.
label vt_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"vote"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e6e6f0}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
