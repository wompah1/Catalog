## Womensbath -- "The Women's Bath Makes You One, and It's the Half That Earns" (rewritten straight in
## Ren'Py, 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From the shelf book
## 9b2c2d55, The Women's Side, kept verbatim in catalog/docs/routes/vn-original/womensbath/.
##
## THE NON-CON PASS, "The water holds" (owner, 2026-11-12, as signed off): in the early soaks the spring's
## change is forced through him and his legs won't carry him out; Iori never asks and never threatens,
## she is patient, says it's how it settles, and carries on past his no. Ch 1-4 non-con, no flip; ch 5-6
## break into begging; ch 7 he goes looking for her and asks (the flip); ch 8-12 consensual, him leading
## from ch 8. No tears, no menace, no pain, no escape.
##
## The book's rules kept: the grace period is the ladder and it keeps a residue; the timer on his phone
## until he stops checking it; Gorou's ledger at ch 8; the choice at ch 10 (marked: Close, the book's;
## Restore, new writing); the red hair in two long low tails, never high twintails; he/him until the
## "return" never comes (ch 7), she/her after. The Japanese names and the onsen inn, in the town's spa
## district. Iori is futa and changes on her own ratchet. All route-local names carry wom_.

init -10 python:
    WOM = "art/womensbath/"

    # THE TIMER: what the phone says after each soak, in words; from ch 7 there's nothing to time.
    WOM_TIMER = [None,
        "Twenty minutes.", "Forty minutes.", "An evening, and the hair doesn't come back.", "Half a day, and the voice doesn't come back.",
        "A night, and the chest doesn't go.", "Two days.", "Nothing. No return.", "You don't start it.", "You don't open the app.",
        "You've deleted the app.", "There's nothing left to wear off.", "There's nothing left to time.",
    ]

    # THE POOL: the staff betting board in the back office (Nao's), one line a week.
    WOM_POOL = [None, None, None,
        "Nao's board, back office: HOW LONG DOES THE BOSS LAST? A column of names. Nobody has picked under an evening.",
        "The board again. Somebody has crossed out 'evening' and written 'lunch' beside your name.",
        "The board: 'BRA BY FRIDAY'. Three ticks. Nao's handwriting.",
        "The board: 'REQUESTED BY NAME'. Hazuki's name, underlined twice.",
        "The board: the pool closes. Nao has written WINNER: NOBODY. SHE NEVER WENT BACK.",
    ]

    WOM_ROWS = ["0", "3", "4", "5", "6", "7", "11", "12"]

    def wom_body(row):
        """The residue body (out of the water) takes the row, toward it and never back."""
        row = str(row)
        if WOM_ROWS.index(row) > WOM_ROWS.index(wom.row or "0"):
            wom.row = row

    def wom_soak(on):
        """In the water she's the whole woman, whatever the residue; out of it, the residue."""
        wom.wet = on

    # ---- the stage --------------------------------------------------------------------------
    # The residue rows (0 a man, 3 hairless, 4 the voice, 5 the chest stays, 6 hips and thighs, 7 the
    # return never comes, 11 the last change, 12 the spring's last push) and the soak body "w" (the
    # whole woman in the water, rows 0-6 only; from 7 she is the woman out of it too). Outfits: "own"
    # (his own clothes), "yukata" (the inn's), "uniform" (the women's side staff uniform), "bought" (the
    # clothes from two towns over), "nude".
    _wom_have = {}

    def _wom_has(n):
        if n not in _wom_have:
            _wom_have[n] = renpy.loadable(WOM + n + ".png")
        return _wom_have[n]

    def wom_pc_file(face):
        r = "w" if (wom.wet and wom.row in ("0", "3", "4", "5", "6")) else (wom.row or "0")
        fit = wom.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-uneasy" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-uneasy" % r]
        if r == "w":
            # ff 2:49 am 11-18 (QA e170df44 block 1): no pc-rw-* sprite was ever drawn. The soak body is
            # the stacked red-haired woman, which the r11/r12 nude sprites already are; use them.
            names += ["pc-r11-nude-%s" % face, "pc-r11-nude-proud", "pc-r12-nude-%s" % face,
                      "pc-r12-nude-begging"]
        for n in names:
            if _wom_has(n):
                return WOM + n + ".png"
        # never a missing file: the nearest lower row of the same outfit (a nude only at its own row,
        # never across the cock/pussy line at row 11)
        rows = [0, 3, 4, 5, 6, 7, 11, 12]
        top = int(r) if r.isdigit() else 0
        for rr in [x for x in rows if x <= top and (x >= 11) == (top >= 11)][::-1]:
            for f in ((fit,) if fit != "nude" else ()) + (("nude",) if (rr == top or fit == "nude") else ()):
                for fc in (face, "uneasy", "flushed", "proud", "stubborn", "begging"):
                    n = "pc-r%d-%s-%s" % (rr, f, fc)
                    if _wom_has(n):
                        return WOM + n + ".png"
        return WOM + names[-1] + ".png"

    def wom_face_now():
        a = renpy.get_attributes("wom_pc")
        return a[0] if a else "uneasy"

    def _wom_portrait(st, at):
        p = vn_art_file(wom_pc_file(wom_face_now()))
        crops = globals().get("womensbath_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["womensbath"] = lambda: DynamicDisplayable(_wom_portrait)

    WOM_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def wom_weekday_name():
        return WOM_WD[(1 + vn_clock.day - 1) % 7]    # day 1 is a Monday

    vn_weekdays["womensbath"] = wom_weekday_name

    vn_sprite_image("wom_pc", ("uneasy", "stubborn", "flushed", "begging", "proud"), wom_pc_file, who="pc")
    for _w, _faces in (("iori", ("dry", "patient", "soft")), ("nao", ("grin", "flat")), ("hazuki", ("charmed", "sly"))):
        vn_sprite_image("wom_" + _w, _faces, (lambda w: (lambda f: WOM + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(WOM) and _f.endswith(".jpg"):
            _n = _f[len(WOM):-4]
            vn_register_bg("wom_" + _n.replace("-", "_"), _f)
            vn_register_cg("wom_" + _n.replace("-", "_"), _f)

    vn_register_route("womensbath", "The Women's Bath Makes You One, and It's the Half That Earns",
        "You've inherited half of the Fuyusaka, a hot-spring inn in the spa district, from an uncle nobody liked. Your half is the men's side, and it loses money every month. The women's side is booked till next spring. The okami who runs it says, if you want to know why, go and use the women's bath yourself. After closing. Time yourself.",
        WOM + "cover.jpg", "womensbath_start")

    achievement.register("One Bath")
    achievement.register("A Clean Inn")

default wom = VNState(row="0", fit="own", wet=False, chapter=0, broke=False, asked=False, ending=None)
default wom_pc_name = "Tsubaki"

define wom_you = VNChar("[wom_pc_name]", who="pc", plate="#b0303a")
define wom_iori = VNChar("Iori", who="wom_iori", plate="#2a2a3a")
define wom_nao = VNChar("Nao", who="wom_nao", plate="#7a6a3a")
define wom_hazuki = VNChar("Hazuki", who="wom_hazuki", plate="#5a3a6a")
define wom_guest = VNChar("A guest", who="guest", plate="#6b6b78")

## THE TIMER: the phone after a soak.
screen wom_timer(n):
    zorder 60
    $ _n = max(1, min(12, n))
    frame:
        xalign 0.5 ypos 60
        padding (34, 20)
        background Frame(Solid("#101418f0"), 0, 0)
        text ("{color=#ff8a7a}Grace period:{/color} " + WOM_TIMER[_n]) size 28 color "#e8e4dc"

## THE POOL: Nao's board.
screen wom_pool(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 20)
        background Frame(Solid("#f2efe4f2"), 0, 0)
        text WOM_POOL[n] size 26 color "#1a1a1a"

label womensbath_start:
    $ wom = VNState(row="0", fit="own", wet=False, chapter=0, broke=False, asked=False, ending=None)
    $ vn_clock = VNState(day=1, hour=21, minute=0)
    $ vn_route = "womensbath"
    $ wom_pc_name = "Tsubaki"
    if not renpy.session.get("vn_picks"):
        $ wom_pc_name = renpy.input("Your name? (Tsubaki, unless you'd like another. Fuyusaka either way.)", default="Tsubaki", length=20).strip() or "Tsubaki"
    jump wom_ch1

label wom_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"womensbath"}
    $ vn_route = None
    hide screen wom_timer
    hide screen wom_pool
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    if wom.ending == "close":
        centered "{size=+10}{color=#ff8a7a}One Bath{/color}{/size}\n\n{i}The end.{/i}"
    else:
        centered "{size=+10}{color=#ff8a7a}A Clean Inn{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _wom_trace():
        pc = wom_pc_file(wom_face_now()).rsplit("/", 1)[-1] if renpy.showing("wom_pc") else None
        cast = None
        for _t in ("wom_iori", "wom_nao", "wom_hazuki"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
        return pc, cast, wom.fit

    vn_trace_routes["womensbath"] = _wom_trace
