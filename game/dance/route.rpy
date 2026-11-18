## Aren -- "The Sealing Dance" (adapted from *Fuuin no Mai: Nyotaika shita Boku to Nakama ga Inmon ni Okasarete Yararehoudai*
## (Dance of Enslavement), TANUKIHOUSE, via the owner's insperation.txt; names invented (the blurb names nobody); written straight in
## Ren'Py by twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file, signed off by the owner about 9:04 pm ET: the MC is
## the one primarily fucked, Senna is the futa, pure TSF, gradual over a week, two endings).
##
## AGED UP: the source is tagged loli; none of that survives. Aren and Lys are 22, Senna 26, Corvin in his forties. Nothing
## youth- or school-coded.
##
## CONSENT, AS BUILT: the crest answers whoever speaks the demon's name aloud, and Aren has traded himself to Corvin's Unveiled
## every night so Lys isn't touched. Every scene with them is non-con by the crest and the bargain. Loud and vocal; never tears,
## menace or pain. A refusal choice plays as the crest winning.
##
## THE WEEK: one body step and one hair step a night, dark brown to rose gold, 180 cm down to 165 cm, chest to a big F on the last
## night. The cock goes on the fifth morning; no pussy before it. Senna's crest gives her a cock (futa); Lys's only makes her
## ache, and nobody but Aren touches her. The crest is a glowing womb crest (the owner's standing tattoo exception). No pregnancy.
## All names carry dnc_.

init -10 python:
    DNC = "art/dance/"

    DNC_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def dnc_weekday():
        return DNC_DAYS[vn_clock.day % 7]

    vn_weekdays["dance"] = dnc_weekday

    def dnc_grow(n):
        dnc.body = max(dnc.body or 0, n)

    _dnc_have = {}

    def _dnc_has(n):
        if n not in _dnc_have:
            _dnc_have[n] = renpy.loadable(DNC + n + ".png")
        return _dnc_have[n]

    def dnc_pc_file(face):
        r, fit = "b%d" % max(0, min(7, dnc.body or 0)), dnc.fit
        names = []
        faces = [face, "stern", "nervous", "flustered", "dazed", "moaning", "blissful"]
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, f) for f in faces]
        names += ["pc-%s-%s-%s" % (r, o, f) for f in faces for o in ("shift", "dancer", "guard", "nude") if o != fit]
        names += ["pc-%s-%s" % (r, face), "pc-%s-stern" % r]
        for n in names:
            if _dnc_has(n):
                return DNC + n + ".png"
        return DNC + names[-1] + ".png"

    def dnc_face_now():
        a = renpy.get_attributes("dnc_pc")
        return a[0] if a else "stern"

    def _dnc_portrait(st, at):
        p = vn_art_file(dnc_pc_file(dnc_face_now()))
        crops = globals().get("dance_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["dance"] = lambda: DynamicDisplayable(_dnc_portrait)

    def dnc_night_file(name):
        return lambda f: DNC + "%s-n%d-%s.png" % (name, max(1, dnc.night or 1), f)

    vn_sprite_image("dnc_pc", ('stern', 'nervous', 'flustered', 'protesting', 'moaning', 'dazed', 'blissful'), dnc_pc_file, who="pc")

    vn_sprite_image("dnc_lys", ('dancer',), lambda f: DNC + "lys-" + f + ".png")
    vn_sprite_image("dnc_senna", ('mage',), lambda f: DNC + "senna-" + f + ".png")
    vn_sprite_image("dnc_corvin", ('merchant',), lambda f: DNC + "corvin-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(DNC) and _f.endswith(".jpg"):
            _n = _f[len(DNC):-4]
            vn_register_bg("dnc_" + _n.replace("-", "_"), _f)
            vn_register_cg("dnc_" + _n.replace("-", "_"), _f)

    vn_register_route("dance", "The Sealing Dance",
        "You're Aren Vale, twenty-two, sworn sword of the Temple of the Veil, and tonight is Spring Eve: the night the temple's dancer dances the demon under the hill back to sleep for another year. This year the dancer is Lys, the woman you're going to marry. You've stood guard at the dance every spring for five years. You know every step of it. You've never once thought you'd need to.",
        DNC + "cover.jpg", "dance_start")

    achievement.register("Sealed")
    achievement.register("Enslaved")

default dnc = VNState(body=0, fit="guard", held=0, asked=0)
default dnc_pc_name = "Aren"

define dnc_you = VNChar("[dnc_pc_name]", who="pc", plate="#b76e79")
define dnc_lys = VNChar("Lys", who="dnc_lys", plate="#6b3a5a")
define dnc_senna = VNChar("Senna", who="dnc_senna", plate="#2a3a5a")
define dnc_corvin = VNChar("Corvin", who="dnc_corvin", plate="#4a1a1a")

label dance_start:
    $ dnc = VNState(body=0, fit="guard", held=0, asked=0)
    $ vn_clock = VNState(day=5, hour=19, minute=30)
    $ dnc_pc_name = "Aren"
    if not renpy.session.get("vn_picks"):
        $ dnc_pc_name = renpy.input("Your name? (Aren, unless you'd like another.)", default="Aren", length=20).strip() or "Aren"
    $ vn_route = "dance"
    jump dnc_festival

label dnc_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label dnc_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"dance"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#d4877f}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
