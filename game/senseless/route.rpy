## Rook -- "Senseless" (adapted from *Kankaku Shadan Mesu-Ka Trap!* (Sensory Deprivation Feminization Trap!), Yo No Yugure Doki,
## via the owner's insperation.txt; the cast, the rivalry and the ruin invented (the blurb names nobody); written straight in Ren'Py by
## twinetesting-a1, 2026-11-17; the plan is PLAN.md beside this file, signed off by the owner about 9:21 pm ET: soft TSF, one fixed body
## ladder, separate from line 45, the rival at the desk, tentacles first).
##
## AGED UP: the source is tagged shota and mesugaki; none of the age survives. Rook is 21, Hesper 24. His brat streak is an adult's
## mouth. Nothing youth- or school-coded.
##
## CONSENT, AS BUILT: the collar holds him and cuts his senses below it; the tentacles under it develop him; Hesper works their desk
## while telling him she's digging him out. Non-con by the trap and her lie. Loud and vocal; never tears, menace or pain.
##
## THE WEEK: one body step a morning, 178 cm down to 168 cm, short black hair to waist-long black with a violet sheen, chest to a
## big F, round hips and ass. SOFT TSF: the cock stays (smaller, very sensitive). The daily rune (chest, nipples, hips, cock,
## mouth) picks where the tentacles work hardest that day; it changes the scenes and the epilogue, never the body art. All names
## carry sns_.

init -10 python:
    SNS = "art/senseless/"

    SNS_DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def sns_weekday():
        return SNS_DAYS[vn_clock.day % 7]

    vn_weekdays["senseless"] = sns_weekday

    def sns_grow(n):
        sns.body = max(sns.body or 0, n)

    _sns_have = {}

    def _sns_has(n):
        if n not in _sns_have:
            _sns_have[n] = renpy.loadable(SNS + n + ".png")
        return _sns_have[n]

    def sns_pc_file(face):
        r, fit = "b%d" % max(0, min(7, sns.body or 0)), sns.fit
        names = []
        if fit:
            names += ["pc-%s-%s-%s" % (r, fit, face), "pc-%s-%s-smug" % (r, fit)]
        names += ["pc-%s-%s" % (r, face), "pc-%s-smug" % r]
        for n in names:
            if _sns_has(n):
                return SNS + n + ".png"
        return SNS + names[-1] + ".png"

    def sns_face_now():
        a = renpy.get_attributes("sns_pc")
        return a[0] if a else "smug"

    def _sns_portrait(st, at):
        p = vn_art_file(sns_pc_file(sns_face_now()))
        crops = globals().get("senseless_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["senseless"] = lambda: DynamicDisplayable(_sns_portrait)

    def sns_night_file(name):
        return lambda f: SNS + "%s-n%d-%s.png" % (name, max(1, sns.night or 1), f)

    vn_sprite_image("sns_pc", ('smug', 'angry', 'shocked', 'flustered', 'moaning', 'dazed', 'blissful'), sns_pc_file, who="pc")

    vn_sprite_image("sns_hesper", ('delver',), lambda f: SNS + "hesper-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(SNS) and _f.endswith(".jpg"):
            _n = _f[len(SNS):-4]
            vn_register_bg("sns_" + _n.replace("-", "_"), _f)
            vn_register_cg("sns_" + _n.replace("-", "_"), _f)

    vn_register_route("senseless", "Senseless",
        "You're Rook Ashdown, twenty-one, the best ruin-delver in Brackwater, and everybody knows it because you tell them. For two years you've beaten Hesper Vane to every find worth having and laughed about it at the Delvers' Hall after. Today it's Quist's Folly, an alchemist's ruin nobody's opened in eighty years, and you're half an hour ahead of her. Nothing in there you can't handle.",
        SNS + "cover.jpg", "senseless_start")

    achievement.register("Climbed Out")
    achievement.register("Stayed In")

default sns = VNState(body=0, fit="delver", brat=0, soft=0, chest=0, nips=0, hips=0, cock=0, mouth=0, today="")
default sns_pc_name = "Rook"

define sns_you = VNChar("[sns_pc_name]", who="pc", plate="#7a4fb0")
define sns_hesper = VNChar("Hesper", who="sns_hesper", plate="#a0451f")
# Hesper heard from under the floor at the desk (the hours): a voice with no sprite, like boy_voice
define sns_hesper_below = VNChar("Hesper", who="sns_hesper_below", plate="#a0451f")

label senseless_start:
    $ sns = VNState(body=0, fit="delver", brat=0, soft=0, chest=0, nips=0, hips=0, cock=0, mouth=0, today="")
    $ vn_clock = VNState(day=6, hour=15, minute=0)
    $ sns_pc_name = "Rook"
    if not renpy.session.get("vn_picks"):
        $ sns_pc_name = renpy.input("Your name? (Rook, unless you'd like another.)", default="Rook", length=20).strip() or "Rook"
    $ vn_route = "senseless"
    jump sns_folly

label sns_cut(wake, days=1, card=None):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    if card:
        centered "{i}[card]{/i}"
    $ vn_clock.day += days
    $ vn_set_time(wake, 0)
    pause 0.35
    window auto
    return

label sns_route_return(title):
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"senseless"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#9b7fd4}[title]{/color}{/size}\n\n{i}The end.{/i}"
    jump start
