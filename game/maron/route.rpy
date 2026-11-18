## Maron -- "Onee-sama's Maid" (adapted from *Chinmai Kyuuketsuki no Ojou-sama ni Torawareta Ore wa, Nyotaika Saserarete Juujun na
## Imouto Maid ni Choukyou Sareteshimau Sou Desu*, Studio Ubai Trans, via the owner's insperation.txt; the source's names Mitsuru,
## Chris, Kanon and Maron kept; written straight in Ren'Py by twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file,
## signed off by the owner about 8:42 pm ET: one bite a night for a week, eight chapters, two endings).
##
## AGED UP: the source is tagged loli; none of that survives. Mitsuru is 23; Chris and Kanon are centuries-old vampires with grown
## women's bodies. The imouto maid is a role between adults who aren't related (as in sister): blood-kin by the bite, not family.
##
## CONSENT, AS BUILT: the bite makes her Chris's thrall. An order Chris says aloud can't be refused, and Chris orders her to obey
## Kanon too, so every scene is non-con by the bond. Each climax lets the girl self, Maron, surface and drive the body a little
## longer. Loud and vocal; never tears, menace or pain. A refusal choice plays as obedience.
##
## THE WEEK: one body step and one hair step a night, black to chestnut, 175 cm down to a 145 cm short stack at the cap (huge,
## weighted up) on the last night. The cock is gone on the third morning; no pussy before it. Kanon is a futa; Chris is not.
## Bites leave two small marks and no gore. No pregnancy. All names carry mrn_.

init -10 python:
    MRN = "art/maron/"

    MRN_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def mrn_weekday():
        return MRN_DAYS[vn_clock.day % 7]

    vn_weekdays["maron"] = mrn_weekday

    def mrn_grow(n):
        mrn.body = max(mrn.body or 0, n)

    _mrn_have = {}

    def _mrn_has(n):
        if n not in _mrn_have:
            _mrn_have[n] = renpy.loadable(MRN + n + ".png")
        return _mrn_have[n]

    def mrn_pc_file(face):
        r, fit = "b%d" % max(0, min(7, mrn.body or 0)), mrn.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-nervous" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-nervous" % r]
        for n in names:
            if _mrn_has(n):
                return MRN + n + ".png"
        return MRN + names[-1] + ".png"

    def mrn_face_now():
        a = renpy.get_attributes("mrn_pc")
        return a[0] if a else "nervous"

    def _mrn_portrait(st, at):
        p = vn_art_file(mrn_pc_file(mrn_face_now()))
        crops = globals().get("maron_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["maron"] = lambda: DynamicDisplayable(_mrn_portrait)

    def mrn_night_file(name):
        return lambda f: MRN + "%s-n%d-%s.png" % (name, max(1, mrn.night or 1), f)

    vn_sprite_image("mrn_pc", ('nervous', 'flustered', 'protesting', 'moaning', 'dazed', 'serene', 'blissful'), mrn_pc_file, who="pc")

    vn_sprite_image("mrn_chris", ('heiress',), lambda f: MRN + "chris-" + f + ".png")
    vn_sprite_image("mrn_kanon", ('headmaid',), lambda f: MRN + "kanon-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(MRN) and _f.endswith(".jpg"):
            _n = _f[len(MRN):-4]
            vn_register_bg("mrn_" + _n.replace("-", "_"), _f)
            vn_register_cg("mrn_" + _n.replace("-", "_"), _f)

    vn_register_route("maron", "Onee-sama's Maid",
        "You're Mitsuru Yokomizo, twenty-three, a Yokohama office worker on your first solo winter hike, and the whiteout came down an hour ago. The trail's gone. Your phone's dead. Ahead of you the snow just stops, at a line of black pines, and beyond them there's a lit window.",
        MRN + "cover.jpg", "maron_start")

    achievement.register("Maron")
    achievement.register("Both of Us")

default mrn = VNState(body=0, fit="hiking", maron=0, held=0)
default mrn_pc_name = "Mitsuru"

define mrn_you = VNChar("[mrn_pc_name]", who="pc", plate="#9b2d4a")
define mrn_chris = VNChar("Chris", who="mrn_chris", plate="#3a0a1a")
define mrn_kanon = VNChar("Kanon", who="mrn_kanon", plate="#1a1426")
define mrn_maron = VNChar("Maron", who="pc", plate="#c8607a")

label maron_start:
    $ mrn = VNState(body=0, fit="hiking", maron=0, held=0)
    $ vn_clock = VNState(day=6, hour=16, minute=40)
    $ mrn_pc_name = "Mitsuru"
    if not renpy.session.get("vn_picks"):
        $ mrn_pc_name = renpy.input("Your name? (Mitsuru, unless you'd like another.)", default="Mitsuru", length=20).strip() or "Mitsuru"
    $ vn_route = "maron"
    jump mrn_whiteout

label mrn_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label mrn_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"maron"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#c0405e}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
