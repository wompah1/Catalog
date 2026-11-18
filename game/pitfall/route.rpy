## Aubin -- "Pitfall" (adapted from *Otokonoko na Saikyou Souryo-kun wa Kankaku Shadan Ana ni Ochiru* (The Strongest Priest Who
## Is a Cross-Dressing Boy Falls into a Sensory Deprivation Hole), RJ01577083, via the owner's insperation.txt; the pit as a living
## thing that feeds on holy power, its lures, the Order, the village and every escape attempt invented (the blurb gives only the
## premise); written straight in Ren'Py by twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file, signed off by the
## owner about 9:38 pm ET: feminization (he ends a femboy, still him), tentacles only, unaware but his thinking drifts, a massive ass
## by the end, a creative hair colour).
##
## AGED UP: the source is tagged loli; none of the age survives. Aubin is 22. The nun's habit is his own taste, an adult's. Nothing
## youth- or school-coded.
##
## CONSENT, AS BUILT: the pit's fluid shuts off his senses; he never agrees to any of it and doesn't know it's happening until the
## seventh morning. Non-con by the pit. His mouth is loud the whole week (he can't hear it); never tears, menace or pain.
##
## THE WEEK: one body step a morning, 168 cm down to 163 cm; honey-blond hair to the shoulders grows to the waist while luminous
## mint creeps up it from the tips; waist narrower, hips wider, a soft chest (no breasts), fuller lips, the cock smaller, and the
## ass rounder every day until it's massive. Two narrators: his own calm second person, and the pit's truth in third person (mint).
## All names carry pfl_.

init -10 python:
    PFL = "art/pitfall/"

    PFL_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def pfl_weekday():
        return PFL_DAYS[vn_clock.day % 7]

    vn_weekdays["pitfall"] = pfl_weekday

    def pfl_grow(n):
        pfl.body = max(pfl.body or 0, n)

    _pfl_have = {}

    def _pfl_has(n):
        if n not in _pfl_have:
            _pfl_have[n] = renpy.loadable(PFL + n + ".png")
        return _pfl_have[n]

    def pfl_pc_file(face):
        r, fit = "b%d" % max(0, min(7, pfl.body or 0)), pfl.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-serene" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-serene" % r]
        for n in names:
            if _pfl_has(n):
                return PFL + n + ".png"
        return PFL + names[-1] + ".png"

    def pfl_face_now():
        a = renpy.get_attributes("pfl_pc")
        return a[0] if a else "serene"

    def _pfl_portrait(st, at):
        p = vn_art_file(pfl_pc_file(pfl_face_now()))
        crops = globals().get("pitfall_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["pitfall"] = lambda: DynamicDisplayable(_pfl_portrait)

    def pfl_night_file(name):
        return lambda f: PFL + "%s-n%d-%s.png" % (name, max(1, pfl.night or 1), f)

    vn_sprite_image("pfl_pc", ('serene', 'smug', 'puzzled', 'shocked', 'flustered', 'moaning', 'dazed', 'blissful'), pfl_pc_file, who="pc")

    vn_sprite_image("pfl_reeve", ('calm', 'stare'), lambda f: PFL + "reeve-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(PFL) and _f.endswith(".jpg"):
            _n = _f[len(PFL):-4]
            vn_register_bg("pfl_" + _n.replace("-", "_"), _f)
            vn_register_cg("pfl_" + _n.replace("-", "_"), _f)

    vn_register_route("pitfall", "Pitfall",
        "You're Brother Aubin, twenty-two, the strongest priest the Order of the Lamp has had in a century, and you wear the Sisters' white habit because you like how it looks on you; nobody has ever dared say a word. Fallowmere's wood has gone bad, and the bounty would re-roof the Mother House. An afternoon's work. You've never once been careless.",
        PFL + "cover.jpg", "pitfall_start")

    achievement.register("Climbed Out")
    achievement.register("Sank Back")

default pfl = VNState(body=0, fit="habit", held=0, slipped=0, pride=0, grace=0)
default pfl_pc_name = "Aubin"

define pfl_you = VNChar("[pfl_pc_name]", who="pc", plate="#c79a3a")
define pfl_reeve = VNChar("Maud", who="pfl_reeve", plate="#6b7a3a")
define pfl_mother = VNChar("Mother Ysolde", who="pfl_mother", plate="#3fbf8f")

label pitfall_start:
    $ pfl = VNState(body=0, fit="habit", held=0, slipped=0, pride=0, grace=0)
    $ vn_clock = VNState(day=1, hour=14, minute=0)
    $ pfl_pc_name = "Aubin"
    if not renpy.session.get("vn_picks"):
        $ pfl_pc_name = renpy.input("Your name? (Aubin, unless you'd like another.)", default="Aubin", length=20).strip() or "Aubin"
    $ vn_route = "pitfall"
    jump pfl_fallowmere

label pfl_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label pfl_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"pitfall"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#5fd9a8}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
