## Tirysia -- "Debuffed" (adapted from *Tirishia -Otoko no Ko ga Jotai Ijode Hamerare Okasareru Action Game-* (Tirysia ~Trapped and
## Ravished by Status Ailments Action Game~), RJ01593277, via the owner's insperation.txt line 47; kept: a femboy hero, monster
## girls, the heart-shot he touches out of curiosity, the charm that walks him to each enemy, ailments that cling after he escapes;
## invented: the Spire of Velune, its seven guardians and which change each ailment makes, the guild and its appraiser, both
## endings; written straight in Ren'Py by twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file, signed off by the owner
## about 10:52 pm ET: soft TSF, the girls fit the changes, breasts end at the cap, a seventh girl, endings my call).
##
## AGES: Tirysia is 22; every guardian is an adult monster girl; Ottilie the appraiser is in her 40s. Nothing youth- or
## school-coded. Morwen's drain takes his muscle and height down to 163 cm, an ordinary woman's height.
##
## CONSENT, AS BUILT: each guardian rapes him (the source's "reverse rape"); the charm walks him to them and his thoughts melt.
## Loud and vocal, never tears, menace or pain. He keeps his cock (soft TSF), so no vaginal sex anywhere: slime, vines, tails,
## breasts, mouths and hands.
##
## THE WEEK: one floor a day, one ailment a floor, one body step a night (rows b0-b7). Each ailment stays on his status bar
## (gold) and the changes are pink. All names carry dbf_.

init -10 python:
    DBF = "art/debuffed/"

    DBF_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def dbf_weekday():
        return DBF_DAYS[vn_clock.day % 7]

    vn_weekdays["debuffed"] = dbf_weekday

    def dbf_grow(n):
        dbf.body = max(dbf.body or 0, n)

    _dbf_have = {}

    def _dbf_has(n):
        if n not in _dbf_have:
            _dbf_have[n] = renpy.loadable(DBF + n + ".png")
        return _dbf_have[n]

    def dbf_pc_file(face):
        r, fit = "b%d" % max(0, min(7, dbf.body or 0)), dbf.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-cocky" % (r, fit)]
        # a body with no sprite in this fit yet (a redraw pending) wears the same body's dress row, never a missing file
        names += ["pc-%s-dress-%s" % (r, face), "pc-%s-dress-cocky" % r]
        names += ["pc-%s-%s" % (r, face), "pc-%s-cocky" % r]
        for n in names:
            if _dbf_has(n):
                return DBF + n + ".png"
        return DBF + names[-1] + ".png"

    def dbf_face_now():
        a = renpy.get_attributes("dbf_pc")
        return a[0] if a else "cocky"

    def _dbf_portrait(st, at):
        p = vn_art_file(dbf_pc_file(dbf_face_now()))
        crops = globals().get("debuffed_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["debuffed"] = lambda: DynamicDisplayable(_dbf_portrait)

    def dbf_night_file(name):
        return lambda f: DBF + "%s-n%d-%s.png" % (name, max(1, dbf.night or 1), f)

    vn_sprite_image("dbf_pc", ('cocky', 'curious', 'shocked', 'flustered', 'moaning', 'dazed', 'charmed', 'blissful'), dbf_pc_file, who="pc")

    vn_sprite_image("dbf_glaze", ('smirk', 'hungry'), lambda f: DBF + "glaze-" + f + ".png")
    vn_sprite_image("dbf_verbena", ('smirk', 'hungry'), lambda f: DBF + "verbena-" + f + ".png")
    vn_sprite_image("dbf_morwen", ('smirk', 'hungry'), lambda f: DBF + "morwen-" + f + ".png")
    vn_sprite_image("dbf_holda", ('smirk', 'hungry'), lambda f: DBF + "holda-" + f + ".png")
    vn_sprite_image("dbf_sessaly", ('smirk', 'hungry'), lambda f: DBF + "sessaly-" + f + ".png")
    vn_sprite_image("dbf_corvina", ('smirk', 'hungry'), lambda f: DBF + "corvina-" + f + ".png")
    vn_sprite_image("dbf_mireille", ('smirk', 'hungry'), lambda f: DBF + "mireille-" + f + ".png")
    vn_sprite_image("dbf_ottilie", ('calm', 'stare'), lambda f: DBF + "ottilie-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(DBF) and _f.endswith(".jpg"):
            _n = _f[len(DBF):-4]
            vn_register_bg("dbf_" + _n.replace("-", "_"), _f)
            vn_register_cg("dbf_" + _n.replace("-", "_"), _f)

    vn_register_route("debuffed", "Debuffed",
        "You're Tirysia, twenty-two, the guild's best blade, and you fight in a white battle dress because it looks better on you than on anyone. The Spire of Velune has stood unclimbed for ten years: seven floors, seven guardians, a succubus at the top. Status ailments? You've never caught one you couldn't shake off by supper.",
        DBF + "cover.jpg", "debuffed_start")

    achievement.register("Cleared")
    achievement.register("Kept")

default dbf = VNState(body=0, fit="dress", curious=0, wary=0, fought=0, gave=0)
default dbf_pc_name = "Tirysia"

define dbf_you = VNChar("[dbf_pc_name]", who="pc", plate="#9b7fd9")
define dbf_glaze = VNChar("Glaze", who="dbf_glaze", plate="#5fc8e8")
define dbf_verbena = VNChar("Verbena", who="dbf_verbena", plate="#e86fa8")
define dbf_morwen = VNChar("Morwen", who="dbf_morwen", plate="#9fb4c8")
define dbf_holda = VNChar("Holda", who="dbf_holda", plate="#c89a6a")
define dbf_sessaly = VNChar("Sessaly", who="dbf_sessaly", plate="#4fb87a")
define dbf_corvina = VNChar("Corvina", who="dbf_corvina", plate="#e8964f")
define dbf_mireille = VNChar("Mireille", who="dbf_mireille", plate="#d94f8f")
define dbf_ottilie = VNChar("Ottilie", who="dbf_ottilie", plate="#8a8f6a")

label debuffed_start:
    $ dbf = VNState(body=0, fit="dress", curious=0, wary=0, fought=0, gave=0)
    $ vn_clock = VNState(day=1, hour=9, minute=0)
    $ dbf_pc_name = "Tirysia"
    if not renpy.session.get("vn_picks"):
        $ dbf_pc_name = renpy.input("Your name? (Tirysia, unless you'd like another.)", default="Tirysia", length=20).strip() or "Tirysia"
    $ vn_route = "debuffed"
    jump dbf_guild

label dbf_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label dbf_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"debuffed"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#ff7ad9}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
