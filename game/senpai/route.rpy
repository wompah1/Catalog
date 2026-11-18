## Senpai -- "Senpai's Favourite" (adapted from *An Odious Senpai and Feminized Me*, HELIOGABALUS, DLsite RJ01348229, via the
## owner's insperation.txt; original names, written straight in Ren'Py by twinetesting-a1, 2026-11-17; the plan is PLAN.md beside
## this file, signed off by the owner about 7:30 pm ET: one change a day for a week, eight chapters, two endings).
##
## AGED UP: the source's high-school football club is a university club. Everyone is 20 or older. No school anywhere.
##
## CONSENT, AS BUILT: the witch takes his refusal words. Every no, stop and don't comes out as yes, more and do, so every scene
## is non-con by the curse until Friday, when she starts meaning them (the mindbreak). Loud, begging, the body betrays her;
## never tears, menace or pain. A refusal choice plays as a yes: that is the source's self-picking choices.
##
## THE WEEK: one body step and one hair step a morning, black to ash-pink. Sunday's last change (face, voice) is prose only.
## No pregnancy anywhere (the source's impregnation is cut). The old woman is never sexual. Vanripper only. All names carry snp_.

init -10 python:
    SNP = "art/senpai/"

    SNP_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def snp_weekday():
        return SNP_DAYS[vn_clock.day % 7]

    vn_weekdays["senpai"] = snp_weekday

    def snp_grow(n):
        snp.body = max(snp.body or 0, n)

    _snp_have = {}

    def _snp_has(n):
        if n not in _snp_have:
            _snp_have[n] = renpy.loadable(SNP + n + ".png")
        return _snp_have[n]

    def snp_pc_file(face):
        r, fit = "b%d" % max(0, min(6, snp.body or 0)), snp.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-nervous" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-nervous" % r]
        for n in names:
            if _snp_has(n):
                return SNP + n + ".png"
        return SNP + names[-1] + ".png"

    def snp_face_now():
        a = renpy.get_attributes("snp_pc")
        return a[0] if a else "nervous"

    def _snp_portrait(st, at):
        p = vn_art_file(snp_pc_file(snp_face_now()))
        crops = globals().get("senpai_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["senpai"] = lambda: DynamicDisplayable(_snp_portrait)

    def snp_night_file(name):
        return lambda f: SNP + "%s-n%d-%s.png" % (name, max(1, snp.night or 1), f)

    vn_sprite_image("snp_pc", ('nervous', 'flustered', 'protesting', 'moaning', 'dazed', 'hopeful', 'blissful'), snp_pc_file, who="pc")

    vn_sprite_image("snp_daigo", ('ace',), lambda f: SNP + "daigo-" + f + ".png")
    vn_sprite_image("snp_ryota", ('bully',), lambda f: SNP + "ryota-" + f + ".png")
    vn_sprite_image("snp_oshiro", ('bully',), lambda f: SNP + "oshiro-" + f + ".png")
    vn_sprite_image("snp_witch", ('witch',), lambda f: SNP + "witch-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(SNP) and _f.endswith(".jpg"):
            _n = _f[len(SNP):-4]
            vn_register_bg("snp_" + _n.replace("-", "_"), _f)
            vn_register_cg("snp_" + _n.replace("-", "_"), _f)

    vn_register_route("senpai", "Senpai's Favourite",
        "You're Shun Nagai, twenty, a second-year at Seiran University and the football club's punching bag. Daigo Kuroiwa, the fourth-year ace, is the only one who ever stood up for you. He says one date with a girl like Mitsuki Amane and he'd die happy. On the way home there's a shop you've never seen before.",
        SNP + "cover.jpg", "senpai_start")

    achievement.register("Senpai's Girl")
    achievement.register("His Favourite")

default snp = VNState(body=0, fit="kit", yes=0)
default snp_pc_name = "Shun"

define snp_you = VNChar("[snp_pc_name]", who="pc", plate="#e0a8b8")
define snp_daigo = VNChar("Daigo", who="snp_daigo", plate="#1a1a2a")
define snp_ryota = VNChar("Ryota", who="snp_ryota", plate="#2a1a1a")
define snp_oshiro = VNChar("Oshiro", who="snp_oshiro", plate="#1a2a1a")
define snp_witch = VNChar("The old woman", who="snp_witch", plate="#2a0a2a")
define snp_guy = VNChar("A teammate", who="man", plate="#2a2a2a")

label senpai_start:
    $ snp = VNState(body=0, fit="kit", yes=0)
    $ vn_clock = VNState(day=7, hour=18, minute=30)
    $ snp_pc_name = "Shun"
    if not renpy.session.get("vn_picks"):
        $ snp_pc_name = renpy.input("Your name? (Shun, unless you'd like another.)", default="Shun", length=20).strip() or "Shun"
    $ vn_route = "senpai"
    jump snp_sunday

label snp_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label snp_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"senpai"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e0a8b8}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
