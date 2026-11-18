## Hollowpine -- "She Booked Me Into the Women-Only Resort as Ellie" (rewritten straight in Ren'Py,
## 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From the shelf book
## ca44ecf5 (M19), whose export isn't on this machine: the source is its package, The Full Package,
## kept verbatim in catalog/docs/routes/vn-original/hollowpine/package.md.
##
## THE NON-CON PASS, "It's on the card" (owner, 2026-11-12, as signed off): every day the treatment
## goes one step past what Elliot thought he booked, and he says no. Nobody is cruel: the staff and the
## women are honest and unbothered ("It's on the card, ma'am"), and carry on, because it's the
## treatment; his body is "responding well". Days 1-3 non-con, no flip; day 4 breaks into begging; day
## 5 non-con, then the walk-out, and coming back in is his own (the flip); day 6 consensual, booked by
## him. No tears, no menace, no pain, no escape; nobody threatens; the card is the only force.
##
## The book's rules kept: the menu is the ladder and nobody lies to him; the printout in words, never a
## number; the photo wall; he upgrades himself; femboy: his cock stays small, the chest stops small, no
## vaginal change, he/him to the last line; the height gap is in the prose (his eyeline on Delaney),
## and in the art he's short but clearly adult. All route-local names carry hol_.
##
## THE DELUXE (an alternate route; owner, 2026-11-13 about 1:37 pm ET, signed off from c9's proposal):
## at day 4's night desk, where the canon puts the pen back, he can book the Expansion Package, Deluxe
## ("This choice decides your ending"). It adds the Upper Contour Infusion to every card left: the same
## enzyme, applied topically, Delaney and June finishing on his chest and Fox working it in under a warm
## compress. He reads "volume" as gym volume. The chest: small at day 4 (the plateau), medium-large on
## day 5's morning (hol.grown 1), large from day 5's statement on (hol.grown 2), and at the ending the house
## cap, huge, an H-cup (the owner's ruling, 2026-11-15: alt tits lanes end at the cap). The cock stays small,
## femboy, he/him. Its pictures are twins (art/hollowpine/<name>-dx.jpg, shown in place while
## hol.deluxe) plus its own beats (hol_dx_*), and its sprites are rows 5d, 6d, 7d. The owner's same
## message: alternate routes come last in the image queue.

init -10 python:
    HOL = "art/hollowpine/"

    # THE CARD: the treatments, in the order they're booked, each with its wellness line.
    HOL_CARD = [
        ("Silt Soak", "A mineral soak to draw out impurities."),
        ("Lymphatic Drainage", "Manual drainage, below the waist. Results collected for analysis."),
        ("Hydration Therapy", "Oral administration, three times daily."),
        ("Live Enzyme Infusion", "Internal application for superior bioavailability. See diagram."),
        ("Deep Conditioning", "Morning and evening. Retention improves results."),
        ("Postural Correction", "Supervised realignment. See chart."),
        ("The Full Package", "Everything on the card. All day."),
    ]

    # THE PRINTOUT: one line a morning, in words. June reads it aloud.
    HOL_PRINTOUT = [None,
        "Absorption: none recorded. Retention: none recorded. Note: guest arrived late.",
        "Absorption: low. Retention: low. Note: guest is enthusiastic. Recommend hydration.",
        "Absorption: improving. Retention: fair. Note: oral route is inefficient. Recommend infusion.",
        "Absorption: very good. Retention: poor. Note: guest is leaking. Recommend conditioning.",
        "Absorption: excellent. Retention: excellent. Note: posture still guarded.",
        "Absorption: complete. Retention: complete. Note: none required.",
    ]

    # Where his eyes come to on Delaney, a day at a time (the book's other progress bar). He blames the
    # massage table.
    HOL_EYELINE = [None, "her collarbone", "her collarbone", "just under her collarbone", "the top of her sternum",
                   "her sternum", "her sternum"]

    # The Deluxe's printout lines, from day 5 (the chest is a metric now).
    HOL_PRINTOUT_DX = {
        5: "Absorption: excellent. Retention: excellent. Upper contour: responding very well. Note: posture still guarded.",
        6: "Absorption: complete. Retention: complete. Upper contour: complete. Note: none required.",
    }

    def hol_printout_line(n):
        return HOL_PRINTOUT_DX.get(n) if (hol.deluxe and n in HOL_PRINTOUT_DX) else HOL_PRINTOUT[n]

    def hol_body(row):
        """Elliot's body takes the day's row, toward it and never back."""
        hol.row = str(max(int(hol.row or 1), int(row)))

    def hol_book(n):
        """A treatment ticked on the card."""
        hol.booked = max(hol.booked or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Rows 1-6 (the day's body). Outfits: "robe" (the resort's white robe), "street" (day 1's jeans and
    # hoodie, before the locker), "nadine" (from day 4: the things Nadine buys him), "nude".
    _hol_have = {}

    def _hol_has(n):
        if n not in _hol_have:
            _hol_have[n] = renpy.loadable(HOL + n + ".png")
        return _hol_have[n]

    def hol_pc_file(face):
        r, fit = hol.row or "1", hol.fit or "robe"
        # the Deluxe's grown body (rows 5d-7d) first, then the canon row's
        rows = [r + "d", r] if (hol.deluxe and hol.grown) else [r]
        names = []
        for k in rows:
            names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-earnest" % (k, fit),
                      "pc-r%s-robe-%s" % (k, face), "pc-r%s-robe-earnest" % k]
        for n in names:
            if _hol_has(n):
                return HOL + n + ".png"
        return HOL + names[-1] + ".png"

    def hol_face_now():
        a = renpy.get_attributes("hol_pc")
        return a[0] if a else "earnest"

    def _hol_portrait(st, at):
        p = vn_art_file(hol_pc_file(hol_face_now()))
        crops = globals().get("hollowpine_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["hollowpine"] = lambda: DynamicDisplayable(_hol_portrait)

    # The calendar: day 1 is a Saturday (the drive up), a treatment day each day after.
    HOL_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def hol_weekday_name():
        return HOL_WD[(6 + vn_clock.day - 1) % 7]    # day 1 is a Saturday

    vn_weekdays["hollowpine"] = hol_weekday_name

    vn_sprite_image("hol_pc", ("earnest", "puzzled", "flustered", "begging"), hol_pc_file, who="pc")
    for _w, _faces in (("casey", ("warm", "pleased")), ("delaney", ("idle", "amused")), ("june", ("reading", "dry")),
                       ("nadine", ("brisk", "smile")), ("robin", ("kind", "worried")), ("tech", ("bored",))):
        vn_sprite_image("hol_" + _w, _faces, (lambda w: (lambda f: HOL + w + "-" + f + ".png"))(_w))

    # The Deluxe's twin of a picture: <name>-dx.jpg, shown in its place while hol.deluxe is on (the hypno
    # full regimen's way). A picture with no twin is the same on both.
    _hol_twin = {}

    def _hol_dx_of(path):
        if not hol.deluxe:
            return path
        if path not in _hol_twin:
            t = path[:-4] + "-dx.jpg"
            _hol_twin[path] = t if renpy.loadable(t) else None
        return _hol_twin[path] or path

    # ff 3:12 am 11-18: Deluxe twins that failed 4 draws (SCENES.md hollowpine v6). Under the Deluxe these
    # show no picture rather than the base, whose PC has the small chest the Deluxe prose has outgrown.
    HOL_DX_NONE = {"chart", "correction-robin", "correction-swap", "full-evening", "full-kiss", "full-pin",
                   "group-photo", "full-cum"}

    def _hol_cg_dd(st, at, path):
        if hol.deluxe and path[len(HOL):-4] in HOL_DX_NONE:
            return Null(), None
        return vn_cg(vn_art_file(_hol_dx_of(path))), None

    def _hol_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_hol_dx_of(path))), None

    for _f in renpy.list_files():
        if _f.startswith(HOL) and _f.endswith(".jpg"):
            _n = _f[len(HOL):-4]
            if _n.endswith("-dx"):
                continue
            _k = "hol_" + _n.replace("-", "_")
            vn_cg_files[_k] = _f
            renpy.image(("cg", _k), DynamicDisplayable(_hol_cg_dd, _f))
            renpy.image(("bg", _k), DynamicDisplayable(_hol_bg_dd, _f))

    vn_register_art_sets("hollowpine", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("hollowpine", "She Booked Me Into the Women-Only Resort as Ellie",
        "You've been in love with Casey for four years, so when she asks you on the girls' trip you say yes before she finishes the sentence. A week at Hollow Pine with her and four of her friends. Hollow Pine is women-only. The booking says Ellie, party of six. Nobody at the desk blinks. There's a treatment card on your nightstand, and you read every word of it.",
        HOL + "cover.jpg", "hollowpine_start")

    achievement.register("Six Coming Home")
    achievement.register("Ellie's Deluxe")

default hol = VNState(row="1", fit="street", booked=0, upgrades=0, said_no=0, broke=False, walked=False, deluxe=False, grown=0)
default hol_pc_name = "Elliot"

define hol_you = VNChar("[hol_pc_name]", who="pc", plate="#3a8a7a")
define hol_casey = VNChar("Casey", who="hol_casey", plate="#b06a4a")
define hol_delaney = VNChar("Delaney", who="hol_delaney", plate="#4a4a6a")
define hol_june = VNChar("June", who="hol_june", plate="#6a3a5a")
define hol_nadine = VNChar("Nadine", who="hol_nadine", plate="#8a7a3a")
define hol_robin = VNChar("Robin", who="hol_robin", plate="#5a7a9a")
define hol_tech = VNChar("Fox", who="hol_tech", plate="#7a7a84")
define hol_renee = VNChar("Renee", who="desk", plate="#7a7a84")
define hol_gate = VNChar("The gate", who="desk", plate="#7a7a84")
define hol_desk = VNChar("The front desk", who="desk", plate="#7a7a84")

## THE CARD: the treatment card, the booked lines ticked. Never a price in numbers on screen.
screen hol_card():
    zorder 60
    frame:
        xalign 0.5 ypos 50
        xmaximum 1180
        padding (34, 22)
        background Frame(Solid("#13201cf0"), 0, 0)
        vbox:
            spacing 6
            text "{color=#9fe3cf}HOLLOW PINE · GUEST TREATMENTS · ELLIE{/color}" size 24
            for i, (name, line) in enumerate(HOL_CARD):
                text ("{color=#9fe3cf}✓{/color} " if i < (hol.booked or 0) else "   ") + "{b}" + name + "{/b}  {i}" + line + "{/i}" size 22 color "#e8e4dc"
            if hol.deluxe:
                text "{color=#9fe3cf}✓{/color} {b}Expansion Package: Deluxe{/b}  {i}Upper Contour Infusion. Topical application with warm compress, twice daily. Volume.{/i}" size 22 color "#e8e4dc"

## THE PRINTOUT: the morning's line, slid under the door.
screen hol_printout(n):
    zorder 60
    $ _n = max(1, min(6, n))
    frame:
        xalign 0.5 ypos 60
        xmaximum 1100
        padding (34, 22)
        background Frame(Solid("#f4f1e8f2"), 0, 0)
        vbox:
            spacing 8
            text "HOLLOW PINE · GUEST METRICS · ELLIE" size 22 color "#3a3a3a"
            text hol_printout_line(_n) size 26 color "#1a1a1a"

label hollowpine_start:
    $ hol = VNState(row="1", fit="street", booked=0, upgrades=0, said_no=0, broke=False, walked=False, deluxe=False, grown=0)
    $ vn_clock = VNState(day=1, hour=15, minute=0)
    $ vn_route = "hollowpine"
    $ hol_pc_name = "Elliot"
    if not renpy.session.get("vn_picks"):
        $ hol_pc_name = renpy.input("Your name? (Elliot, unless you'd like another. Ellie on the booking either way.)", default="Elliot", length=20).strip() or "Elliot"
    jump hol_arrival

label hol_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"hollowpine"}
    $ vn_route = None
    hide screen hol_card
    hide screen hol_printout
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#9fe3cf}Six Coming Home{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The screen trace (game/catalog/vntrace.rpy, for the walks).
init 110 python:
    def _hol_trace():
        pc = hol_pc_file(hol_face_now()).rsplit("/", 1)[-1] if renpy.showing("hol_pc") else None
        cast = None
        for _t in ("hol_casey", "hol_delaney", "hol_june", "hol_nadine", "hol_robin", "hol_tech"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
        return pc, cast, hol.fit

    vn_trace_routes["hollowpine"] = _hol_trace
