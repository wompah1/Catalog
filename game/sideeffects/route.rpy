## Akira -- "Side Effects" (adapted from *Seitenkan ~Ore no Naka de Ikeba Ii Daro!?~* (The Sex Change ~You can cum inside me!?~),
## Dieselmine 2014, via the owner's insperation.txt line 50; the source is loli, set at a boys-only prep school, and its main plot is
## father incest, so the owner had it reworked with adults (2026-11-17 ~11:04 pm ET); kept: a traffic accident that wakes him a
## woman, taking someone's place with an old lech to spare her, the train molester, the best friend, the pervert female doctor, the rich
## old men, "done by everyone in her life" until she gives in and becomes a pervert too, the title line; invented: Natsuki the
## flatmate and Gonda the landlord (for the sister and the father), the office (for the school), the clinic's pills and their side
## effects (breasts that keep growing, owner's ask), the club, the day-by-day order, both endings; written straight in Ren'Py by
## twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file, signed off by the owner about 11:12 pm ET).
##
## AGES: Akira is 24; Natsuki 23; Ryouta 24; Ooba 27; Tsuge in his 40s; Dr Hayami in her 30s; Gonda in his 50s; the Tachibana
## Club's members in their 60s. No family, no school, nothing youth-coded.
##
## CONSENT, AS BUILT: most of it is coerced or non-con (the landlord's rent, the groper, the boss's review, the club), as in the
## source; the doctor and Ryouta lean toward her own wanting. Loud and vocal, never tears, menace or pain. The accident takes the
## cock (full TSF), so vaginal sex is fine; creampies yes, and pregnancy is never mentioned.
##
## THE BODY: she wakes a woman (a sudden change: the accident and the surgery), breasts at step 3; the pills' side effects grow them
## a step every night or two to the cap (step 8) and the hair a step at a time, black to plum at the tips (rows b0-b6). Changes are
## pink. All names carry sef_.

init -10 python:
    SEF = "art/sideeffects/"

    SEF_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def sef_weekday():
        return SEF_DAYS[vn_clock.day % 7]

    vn_weekdays["sideeffects"] = sef_weekday

    def sef_grow(n):
        sef.body = max(sef.body or 0, n)

    _sef_have = {}

    def _sef_has(n):
        if n not in _sef_have:
            _sef_have[n] = renpy.loadable(SEF + n + ".png")
        return _sef_have[n]

    def sef_pc_file(face):
        r, fit = "b%d" % max(0, min(6, sef.body or 0)), sef.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-stern" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-stern" % r]
        for n in names:
            if _sef_has(n):
                return SEF + n + ".png"
        return SEF + names[-1] + ".png"

    def sef_face_now():
        a = renpy.get_attributes("sef_pc")
        return a[0] if a else "stern"

    def _sef_portrait(st, at):
        p = vn_art_file(sef_pc_file(sef_face_now()))
        crops = globals().get("sideeffects_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["sideeffects"] = lambda: DynamicDisplayable(_sef_portrait)

    def sef_night_file(name):
        return lambda f: SEF + "%s-n%d-%s.png" % (name, max(1, sef.night or 1), f)

    vn_sprite_image("sef_pc", ('stern', 'shocked', 'flustered', 'moaning', 'dazed', 'hungry', 'blissful', 'smug'), sef_pc_file, who="pc")

    vn_sprite_image("sef_natsuki", ('worried', 'smile'), lambda f: SEF + "natsuki-" + f + ".png")
    vn_sprite_image("sef_gonda", ('leer', 'grin'), lambda f: SEF + "gonda-" + f + ".png")
    vn_sprite_image("sef_hayami", ('calm', 'smirk'), lambda f: SEF + "hayami-" + f + ".png")
    vn_sprite_image("sef_ooba", ('grin', 'leer'), lambda f: SEF + "ooba-" + f + ".png")
    vn_sprite_image("sef_tsuge", ('stern', 'leer'), lambda f: SEF + "tsuge-" + f + ".png")
    vn_sprite_image("sef_grey", ('leer', 'grin'), lambda f: SEF + "grey-" + f + ".png")
    vn_sprite_image("sef_ryouta", ('grin', 'stare'), lambda f: SEF + "ryouta-" + f + ".png")
    vn_sprite_image("sef_tachibana", ('leer', 'grin'), lambda f: SEF + "tachibana-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(SEF) and _f.endswith(".jpg"):
            _n = _f[len(SEF):-4]
            vn_register_bg("sef_" + _n.replace("-", "_"), _f)
            vn_register_cg("sef_" + _n.replace("-", "_"), _f)

    vn_register_route("sideeffects", "Side Effects",
        "You're Akira Sena, twenty-four, a logistics clerk in Tokyo who shares a flat with Natsuki and keeps the landlord off her. One traffic accident later, you wake in a private clinic as a woman, with two pills a day for life and a list of side effects the doctor is very keen to monitor.",
        SEF + "cover.jpg", "sideeffects_start")

    achievement.register("Paid in full")
    achievement.register("Under observation")

default sef = VNState(body=0, fit="suit", held=0, gave=0)
default sef_pc_name = "Akira"

define sef_you = VNChar("[sef_pc_name]", who="pc", plate="#b06fae")
define sef_natsuki = VNChar("Natsuki", who="sef_natsuki", plate="#e8b05f")
define sef_gonda = VNChar("Gonda", who="sef_gonda", plate="#8a7a5a")
define sef_hayami = VNChar("Dr Hayami", who="sef_hayami", plate="#5fb8c8")
define sef_ooba = VNChar("Ooba", who="sef_ooba", plate="#6a8fd9")
define sef_tsuge = VNChar("Tsuge", who="sef_tsuge", plate="#7a7f8a")
define sef_grey = VNChar("The man in grey", who="sef_grey", plate="#9a9a9a")
define sef_ryouta = VNChar("Ryouta", who="sef_ryouta", plate="#d9784f")
define sef_tachibana = VNChar("Tachibana", who="sef_tachibana", plate="#b89a4f")

label sideeffects_start:
    $ sef = VNState(body=0, fit="suit", held=0, gave=0)
    $ vn_clock = VNState(day=1, hour=18, minute=30)
    $ sef_pc_name = "Akira"
    if not renpy.session.get("vn_picks"):
        $ sef_pc_name = renpy.input("Your name? (Akira, unless you'd like another.)", default="Akira", length=20).strip() or "Akira"
    $ vn_route = "sideeffects"
    jump sef_rentday

label sef_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label sef_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"sideeffects"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#d96fd0}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
