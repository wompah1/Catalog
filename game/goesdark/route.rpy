## Kaoru -- "Before It Goes Dark" (adapted from *I'm a Magic Girl ~Kidnapped and Impregnated by the Demon Lord (my buddy)~*,
## RJ260967, QRoss, via the owner's insperation.txt line 52; kept: an ordinary guy made a magical girl by mistake, the demon lord's
## army, the kidnapping, the demon lord who is his best friend, being kept; changed by the owner (2026-11-17 ~11:20-11:50 pm ET):
## corruption for the impregnation (the blacklist), female when transformed and a mega femboy out of costume, a day on parole, and
## a lantern-and-yokai design so she doesn't repeat celestia or costume; invented: the lantern and Pirika, the Kurayami Society as
## yokai, Rasetsu, the shadow castle, Kurose and the office, the day-by-day order, both endings; written straight in Ren'Py by
## twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file).
##
## AGES: Kaoru and Seiya are 22 (friends since nineteen, on the same warehouse night shift); Kurose 34; Rasetsu centuries old;
## Pirika an adult firefly sprite who's never in a sex scene. No family, no school, nothing youth-coded.
##
## CONSENT, AS BUILT: most of it is non-con or coerced (the yokai, Rasetsu, the grunts, the pit, the castle), as in the source;
## Seiya and Kurose lean toward Kaoru's own wanting. Loud and vocal, never tears, menace or pain. Akari, the transformed form, is
## a woman with no cock, so vaginal sex is hers; Kaoru keeps his cock, so his scenes are anal only. No pregnancy, ever: the
## source's impregnation is the lantern's flame burning lower.
##
## THE BODY: two fits. street = Kaoru, a femboy a step further every night (rows b1-b5: smooth, lips and waist, hips and arse,
## chest and waist, the mega femboy; brown hair, length only). lantern = Akari (mint hair darkening jade, pine, darkest pine,
## colour only; breasts 6 to the cap; b6 is the yokai ending). Changes are pink. All names carry gdk_.

init -10 python:
    GDK = "art/goesdark/"

    GDK_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def gdk_weekday():
        return GDK_DAYS[vn_clock.day % 7]

    vn_weekdays["goesdark"] = gdk_weekday

    def gdk_grow(n):
        gdk.body = max(gdk.body or 0, n)

    _gdk_have = {}

    def _gdk_has(n):
        if n not in _gdk_have:
            _gdk_have[n] = renpy.loadable(GDK + n + ".png")
        return _gdk_have[n]

    def gdk_pc_file(face):
        r, fit = "b%d" % max(0, min(6, gdk.body or 0)), gdk.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-stern" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-stern" % r]
        for n in names:
            if _gdk_has(n):
                return GDK + n + ".png"
        return GDK + names[-1] + ".png"

    def gdk_face_now():
        a = renpy.get_attributes("gdk_pc")
        return a[0] if a else "stern"

    def _gdk_portrait(st, at):
        p = vn_art_file(gdk_pc_file(gdk_face_now()))
        crops = globals().get("goesdark_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["goesdark"] = lambda: DynamicDisplayable(_gdk_portrait)

    def gdk_night_file(name):
        return lambda f: GDK + "%s-n%d-%s.png" % (name, max(1, gdk.night or 1), f)

    vn_sprite_image("gdk_pc", ('stern', 'shocked', 'flustered', 'moaning', 'dazed', 'hungry', 'blissful', 'smug'), gdk_pc_file, who="pc")

    vn_sprite_image("gdk_seiya", ('grin', 'smirk'), lambda f: GDK + "seiya-" + f + ".png")
    vn_sprite_image("gdk_lord", ('smirk', 'hungry'), lambda f: GDK + "lord-" + f + ".png")
    vn_sprite_image("gdk_pirika", ('bright', 'worried'), lambda f: GDK + "pirika-" + f + ".png")
    vn_sprite_image("gdk_rasetsu", ('grin', 'leer'), lambda f: GDK + "rasetsu-" + f + ".png")
    vn_sprite_image("gdk_grunt", ('leer', 'grin'), lambda f: GDK + "grunt-" + f + ".png")
    vn_sprite_image("gdk_kurose", ('smile', 'leer'), lambda f: GDK + "kurose-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(GDK) and _f.endswith(".jpg"):
            _n = _f[len(GDK):-4]
            vn_register_bg("gdk_" + _n.replace("-", "_"), _f)
            vn_register_cg("gdk_" + _n.replace("-", "_"), _f)

    vn_register_route("goesdark", "Before It Goes Dark",
        "You're Kaoru Shiraishi, twenty-two, an office worker with a best friend who always buys the second round. One drunk walk home through the lantern festival, one panicking firefly, and you're Akari, a magical girl with a paper lantern, fighting a society of yokai who all seem to know exactly what makes you come.",
        GDK + "cover.jpg", "goesdark_start")

    achievement.register("One flicker left")
    achievement.register("Lit by his fire")

default gdk = VNState(body=0, fit="street", fought=0, gave=0)
default gdk_pc_name = "Kaoru"

define gdk_you = VNChar("[gdk_pc_name]", who="pc", plate="#a8927a")
define gdk_seiya = VNChar("Seiya", who="gdk_seiya", plate="#5a6f9a")
define gdk_lord = VNChar("Seiya", who="gdk_lord", plate="#5fe0a0")
define gdk_pirika = VNChar("Pirika", who="gdk_pirika", plate="#d8e86a")
define gdk_rasetsu = VNChar("Rasetsu", who="gdk_rasetsu", plate="#d9584f")
define gdk_grunt = VNChar("Fox mask", who="gdk_grunt", plate="#8a8a9a")
define gdk_kurose = VNChar("Kurose", who="gdk_kurose", plate="#7a8fb0")

label goesdark_start:
    $ gdk = VNState(body=0, fit="street", fought=0, gave=0)
    $ vn_clock = VNState(day=1, hour=20, minute=0)
    $ gdk_pc_name = "Kaoru"
    if not renpy.session.get("vn_picks"):
        $ gdk_pc_name = renpy.input("Your name? (Kaoru, unless you'd like another.)", default="Kaoru", length=20).strip() or "Kaoru"
    $ vn_route = "goesdark"
    jump gdk_izakaya

label gdk_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label gdk_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"goesdark"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#5fe0a0}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
