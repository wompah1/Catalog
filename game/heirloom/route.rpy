## Heirloom -- "The Club Heirloom Only Seals Once Someone Fucks It Into Place" (rewritten straight in Ren'Py,
## 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From the shelf book 1c3ad5d9,
## Team Heirloom, kept verbatim in catalog/docs/routes/vn-original/heirloom/.
##
## THE NON-CON PASS, "It has to set" (owner, 2026-11-12, as signed off): the team, then Kaede, and the
## anchor's hunger. Nobody threatens him and nobody hurts him; they tell him it has to set, that it's for
## him, that it's tradition, and they keep going past his no. Ch 1 the first incident (he refuses the dare,
## they pull the skin on him; Rei finishes him when he says stop); ch 2-5 forced; ch 6 breaks into begging;
## ch 7 at the camp he crawls down the futon row and asks (the flip); ch 8-14 consensual. The epilogue's
## recruit (recast: a man of twenty-four) is set in full on screen by Yuuka, under the same house rules.
## No tears, no menace, no pain, no escape.
##
## The book's knots, resolved at sign-off: the heirloom is the skin Kaede SHED when she graduated (never
## cut); it climbs him into her figure at twenty-one, not her face; Kaede now wears her hair cropped short
## and silver; the roster name is Yuuka, his own name with the feminine ending. Everyone is 21 or over; the
## team are seniors, never "first-years". Plum hair (the star's long ponytail). he/him until the face sets
## (ch 9), she/her after. All route-local names carry hrl_.

init -10 python:
    HRL = "art/heirloom/"

    # THE SHEET: Rei's region sheet on the clubroom whiteboard, ticked as each one sets.
    HRL_REGIONS = ["Anchor", "Hips", "Waist", "Chest", "Voice", "Face", "Frame"]

    # THE POOL: Miki's chalkboard, one line a week.
    HRL_POOL = {
        2: "Miki's chalkboard: NEXT REGION? Waist, three to one. Tits, five to one. Face, twenty to one. 'IT STOPS HERE', a hundred to one: one taker.",
        3: "The chalkboard: HIPS: SET. Paid out. Somebody has drawn a hoodie with a question mark.",
        4: "The chalkboard: WAIST BY WEDNESDAY? Miki, smug. Nao owes fifteen hundred yen.",
        6: "The chalkboard: HOODIE WATCH, DAY FORTY. Under it, in Haruna's hand: 'not for long'.",
        8: "The chalkboard: CAN HE PASS ON THE PHONE? Yes, two to one. No, evens.",
        9: "The chalkboard: the pool closes. Miki has written WINNER: EVERYBODY BUT YUU.",
        14: "The chalkboard, a year on: FIRST TO SET? A new column of names, and Yuuka's handwriting at the top.",
    }

    # Body rows (what the art draws): 0 a man; 1 the anchor (his own body, sealed and sexed below);
    # 2 hips and ass; 3 waist and belly (and the ribs, ch 5); 5 the chest budding; 6 the full chest (and
    # the voice, ch 8); 8 the face and hair; 9 Yuuka complete (shoulders, hands, frame).
    HRL_ROWS = ["0", "1", "2", "3", "5", "6", "8", "9"]
    HRL_VISUAL = {0: "0", 1: "1", 2: "2", 3: "3", 4: "3", 5: "5", 6: "6", 7: "6", 8: "8", 9: "9"}

    def hrl_body(step):
        """The climb takes the next region, upward and never back. step is the ladder rung (0-9)."""
        row = HRL_VISUAL[int(step)]
        if HRL_ROWS.index(row) > HRL_ROWS.index(hrl.row or "0"):
            hrl.row = row
        hrl.step = max(hrl.step, int(step))

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "hoodie" (his hoodie over running shorts, rows 0-8), "kit" (the club's track kit: tee and
    # shorts, rows 0-3; a sports top and shorts from 5), "bra" (a sports bra and shorts, rows 5-9),
    # "uniform" (the club's white manager's uniform, rows 8-9), "yukata" (the lodge's, row 6), "nude".
    _hrl_have = {}

    def _hrl_has(n):
        if n not in _hrl_have:
            _hrl_have[n] = renpy.loadable(HRL + n + ".png")
        return _hrl_have[n]

    HRL_FACES = ("deadpan", "flustered", "dazed", "bright", "begging")
    HRL_FITS = ("hoodie", "kit", "bra", "uniform", "yukata", "nude")

    def hrl_pc_file(face):
        """The PC sprite for this row, fit and face. Not every row has every fit and face, so fall back to a file
        that exists: the same fit with another face, then the same fit a row or more down, then another fit in
        this row (nude last), then anything lower. Never a missing file."""
        r = hrl.row or "0"
        fit = hrl.fit or "hoodie"
        faces = (face,) + tuple(f for f in HRL_FACES if f != face)
        down = [x for x in reversed(HRL_ROWS[:HRL_ROWS.index(r) + 1])] if r in HRL_ROWS else [r]
        others = [f for f in HRL_FITS if f != fit]
        names = ["pc-r%s-%s-%s" % (r, fit, f) for f in faces]
        names += ["pc-r%s-%s-%s" % (x, fit, f) for x in down[1:] for f in faces]
        names += ["pc-r%s-%s-%s" % (x, o, f) for x in down for o in others for f in faces]
        for n in names:
            if _hrl_has(n):
                return HRL + n + ".png"
        return HRL + names[0] + ".png"

    def hrl_face_now():
        a = renpy.get_attributes("hrl_pc")
        return a[0] if a else "deadpan"

    def _hrl_portrait(st, at):
        p = vn_art_file(hrl_pc_file(hrl_face_now()))
        crops = globals().get("heirloom_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["heirloom"] = lambda: DynamicDisplayable(_hrl_portrait)

    def hrl_week_name():
        return "Week %d" % max(1, hrl.chapter)

    vn_weekdays["heirloom"] = hrl_week_name

    def hrl_next_week():
        """A chapter is a week: the night call adds the one day, this the other six."""
        store.vn_clock.day += 6

    vn_sprite_image("hrl_pc", ("deadpan", "flustered", "begging", "dazed", "bright"), hrl_pc_file, who="pc")
    for _w, _faces in (("rei", ("calm", "smirk", "soft")), ("miki", ("grin", "tease")), ("nao", ("gentle", "worried")),
                       ("kaede", ("smirk", "hungry")), ("ida", ("nod",)), ("haruna", ("grin",)), ("shun", ("nervous", "lost"))):
        vn_sprite_image("hrl_" + _w, _faces, (lambda w: (lambda f: HRL + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(HRL) and _f.endswith(".jpg"):
            _n = _f[len(HRL):-4]
            vn_register_bg("hrl_" + _n.replace("-", "_"), _f)
            vn_register_cg("hrl_" + _n.replace("-", "_"), _f)

    vn_register_route("heirloom", "The Club Heirloom Only Seals Once Someone Fucks It Into Place",
        "You lost the interval, and the women's track club at Seiran University says the loser wears the prize: the heirloom from the locked trunk, a skin from waist to mid-thigh that their graduated legend left behind. You say no. They don't ask twice.",
        HRL + "cover.jpg", "heirloom_start")

    achievement.register("Next Year's Trunk")

default hrl = VNState(row="0", step=0, fit="hoodie", chapter=0, she=False, pool=None, sched=None, top=None,
                      phone=None, camp=None, broke=False, asked=False, ending=None)
default hrl_pc_name = "Yuu"

define hrl_you = VNChar("[hrl_pc_name]", who="pc", plate="#6a2c5a")
define hrl_rei = VNChar("Rei", who="hrl_rei", plate="#2a3442")
define hrl_miki = VNChar("Miki", who="hrl_miki", plate="#b0552a")
define hrl_nao = VNChar("Nao", who="hrl_nao", plate="#4f6a4a")
define hrl_kaede = VNChar("Kaede", who="hrl_kaede", plate="#5a5a66")
define hrl_ida = VNChar("Coach Ida", who="hrl_ida", plate="#3a3a3a")
define hrl_haruna = VNChar("Haruna", who="hrl_haruna", plate="#7a3a3a")
define hrl_shun = VNChar("Shun", who="hrl_shun", plate="#3a4a6a")
define hrl_team = VNChar("The team", who="team", plate="#6b6b78")

## THE SHEET: Rei's region sheet, n regions set.
screen hrl_sheet(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        padding (34, 20)
        background Frame(Solid("#f4f4f0f2"), 0, 0)
        vbox:
            spacing 6
            text "ANCHOR MAINTENANCE: TAKASE" size 24 color "#1a1a1a" bold True
            hbox:
                spacing 26
                for _i, _r in enumerate(HRL_REGIONS):
                    text (("{color=#6a2c5a}✓{/color} " if _i < n else "□ ") + _r) size 24 color "#1a1a1a"

## THE POOL: Miki's chalkboard.
screen hrl_pool(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 20)
        background Frame(Solid("#1f2a24f2"), 0, 0)
        text HRL_POOL[n] size 26 color "#e8ece4"

label heirloom_start:
    $ hrl = VNState(row="0", step=0, fit="hoodie", chapter=0, she=False, pool=None, sched=None, top=None,
                    phone=None, camp=None, broke=False, asked=False, ending=None)
    $ vn_clock = VNState(day=1, hour=17, minute=0)
    $ vn_route = "heirloom"
    $ hrl_pc_name = "Yuu"
    jump hrl_ch1

label hrl_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"heirloom"}
    $ vn_route = None
    hide screen hrl_sheet
    hide screen hrl_pool
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#c58ab8}Next Year's Trunk{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _hrl_trace():
        pc = hrl_pc_file(hrl_face_now()).rsplit("/", 1)[-1] if renpy.showing("hrl_pc") else None
        cast = None
        for _t in ("hrl_rei", "hrl_miki", "hrl_nao", "hrl_kaede", "hrl_ida", "hrl_haruna", "hrl_shun"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, hrl.fit

    vn_trace_routes["heirloom"] = _hrl_trace
