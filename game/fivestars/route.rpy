## Five Stars -- "I Read the Tier Requirements on a Courier App, and Now the Uniform Has My Name
## Printed on the Seat" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this
## file, signed off by the owner). From catalog/game/02-engine/storylines/fivestars/ (fivestars.js:
## the rungs, the dashboard, the lines; main.twee, days-early.twee, days-late.twee), kept verbatim
## in catalog/docs/routes/vn-original/fivestars/.
##
## THE NON-CON PASS (owner, 2026-10-19/20: escalating corruption). Toby is a terms-reader, so his
## protest is the clause wording, argued out loud while it happens. Deb logs every protest and does
## nothing. The rating is structural only: nobody threatens a one-star. "What's the next tier
## need?" / "Put me down for it" is his one voluntary act. Rungs 1-2 never flip; rung 3 flips on
## the scanner's "Fit check passed"; rung 4 on "Appeal upheld"; Clive never; the thighs, the pallet,
## the doors and Deb's counter each flip inside their scene. The fit room and the manifest after
## the ending are free play, not ported.
##
## Seven linear days, one tier a day; the night is vn_night. All route-local names carry fs_.

init -10 python:
    FS = "art/fivestars/"

    # THE LADDER, rung by rung (setup.fivestarsRungs): the tier's name, the dashboard's next-tier
    # line, the gold in the fifth star, and what Regan issues.
    FS_RUNGS = [None,
        dict(tier="Contactless", next="hand-to-customer sign-off", star=0.1, uniform="a medium"),
        dict(tier="Hand to Customer", next="fit check", star=0.25, uniform="the medium"),
        dict(tier="Verified Fit", next="in-home certification", star=0.5, uniform="a large"),
        dict(tier="In-Home", next="returns sign-off", star=0.75, uniform="the large"),
        dict(tier="Returns", next="invite only", star=0.95, uniform="the largest Vellum stocks"),
        dict(tier="Ambassador", next="none", star=1.0, uniform="a cut made to order"),
    ]

    def fs_advance(n):
        """The tier lands (the dashboard's rung)."""
        fs.tier = max(fs.tier or 0, n)

    def fs_body(n):
        """The body takes rung n's row, toward it and never back."""
        fs.body = max(fs.body or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Rows: 0 Toby before intake; 1-6 the rungs. Outfits: "own" (the opening), "kit" (the Vellum
    # polo and cycle shorts, a size up as the rungs go), "split" (rung 5's largest, ruined on the
    # pallet), "prentice" (rung 6's cut), "nude".
    _fs_have = {}

    def _fs_has(n):
        if n not in _fs_have:
            _fs_have[n] = renpy.loadable(FS + n + ".png")
        return _fs_have[n]

    def fs_pc_file(face):
        """The sprite that exists: the outfit with this face, the outfit with the default face,
        the plain body with this face, the default."""
        r, fit = max(0, min(6, fs.body or 0)), fs.fit or "kit"
        names = ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-neutral" % (r, fit),
                 "pc-r%d-kit-%s" % (r, face), "pc-r%d-kit-neutral" % r]
        for n in names:
            if _fs_has(n):
                return FS + n + ".png"
        return FS + names[-1] + ".png"

    def fs_face_now():
        a = renpy.get_attributes("fs_pc")
        return a[0] if a else "neutral"

    def _fs_portrait(st, at):
        p = vn_art_file(fs_pc_file(fs_face_now()))
        crops = globals().get("fivestars_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["fivestars"] = lambda: DynamicDisplayable(_fs_portrait)

    # The calendar: one tier a day, seven days in a row; the prose names no weekday, so day 1 is
    # a Monday (a working week, the epilogue the Sunday morning).
    FS_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def fs_weekday_name():
        return FS_WD[(1 + vn_clock.day - 1) % 7]    # day 1 is a Monday

    vn_weekdays["fivestars"] = fs_weekday_name

    vn_sprite_image("fs_pc", ("neutral", "eager", "protesting", "flushed"), fs_pc_file, who="pc")
    vn_sprite_image("fs_regan", ("flat", "intent"), lambda f: FS + "regan-" + f + ".png")
    vn_sprite_image("fs_jodie", ("grin", "rating", "hungry"), lambda f: FS + "jodie-" + f + ".png")
    vn_sprite_image("fs_clive", ("sour", "grumbling"), lambda f: FS + "clive-" + f + ".png")
    vn_sprite_image("fs_kieran", ("grin", "talking"), lambda f: FS + "kieran-" + f + ".png")
    vn_sprite_image("fs_ade", ("grin", "talking"), lambda f: FS + "ade-" + f + ".png")
    vn_sprite_image("fs_rich", ("grin", "talking"), lambda f: FS + "rich-" + f + ".png")
    vn_sprite_image("fs_deb", ("bored", "intent"), lambda f: FS + "deb-" + f + ".png")

    # Every picture in the route's folder is a background and a CG by name ("bg fs_deck",
    # "cg fs_deck_open").
    for _f in renpy.list_files():
        if _f.startswith(FS) and _f.endswith(".jpg"):
            _n = _f[len(FS):-4]
            vn_register_bg("fs_" + _n.replace("-", "_"), _f)
            vn_register_cg("fs_" + _n.replace("-", "_"), _f)

    # Vanripper the default, Abarus by the HUD's Art button (owner, 2026-11-12: an Abarus set, as
    # every rewrite).
    vn_register_art_sets("fivestars", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("fivestars", "I Read the Tier Requirements on a Courier App, and Now the Uniform Has My Name Printed on the Seat",
        "You drive a van for Vellum, a little adult-apparel label with a same-day courier app, out of a warehouse on the docks. The app has six tiers, and every tier changes what's in the drop: a parcel on a step, then the hand-off, then you on the fit scanner, then you in the customer's front room. You're the only driver who ever read what they need. Dispatch is in your ear from six in the morning. The uniform keeps not fitting.",
        FS + "cover.jpg", "fivestars_start")

    achievement.register("Five Stars, No Notes")

default fs = VNState(tier=0, body=0, fit="own")
default fs_enc = VNState(partner_came=True, pc_orgasms=0)
default fs_pc_name = "Toby"
default fs_mail_lines = []

## The speakers. Deb is a voice in your ear (her own plate, no sprite) until the last door, where
## she's in the room as well; the scanner calls its verdicts in blue.
define fs_you = VNChar("[fs_pc_name]", who="pc", plate="#2f5f9b")
define fs_deb = VNChar("Deb, in your ear", who="deb_ear", plate="#3d6f7a", what_color="#d6eef2")
define fs_debx = VNChar("Deb", who="fs_deb", plate="#3d6f7a")
define fs_regan = VNChar("Regan", who="fs_regan", plate="#c77a1e")
define fs_jodie = VNChar("Jodie", who="fs_jodie", plate="#d4457f")
define fs_clive = VNChar("Clive", who="fs_clive", plate="#7a6a4f")
define fs_kieran = VNChar("Kieran", who="fs_kieran", plate="#4f8f5f")
define fs_ade = VNChar("Ade", who="fs_ade", plate="#5f6fb0")
define fs_rich = VNChar("Rich", who="fs_rich", plate="#9b5f3e")
define fs_scanner = VNChar("The scanner", who="scanner", plate="#2e6fd0", what_color="#9cc8ff")
define fs_cust = VNChar("The customer", who="cust", plate="#6b6b78")
define fs_driver = VNChar("A driver", who="driver", plate="#6b6b78")

## THE DRIVER DASHBOARD (vellum_dashboard): once a day, mid-act, a fixed format and no digits.
## Four gold stars and a fifth part-gold; the chest line identical every time.
screen fs_dash(n):
    zorder 60
    $ r = FS_RUNGS[max(1, min(6, n))]
    frame:
        xalign 0.5 ypos 60 xsize 760
        padding (30, 22)
        background Frame(Solid("#101826f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}VELLUM DRIVER — T. PRENTICE{/b}" size 26 color "#ffffff"
            text "TIER · {color=#e8b923}%s{/color}" % r["tier"] size 24 color "#d8dde8"
            hbox:
                spacing 4
                text "Rating" size 24 color "#d8dde8" yalign 0.5
                null width 8
                text "★★★★" size 30 color "#e8b923" yalign 0.5
                fixed:
                    xysize (32, 40)
                    text "★" size 30 color "#6b6b6b"
                    add Transform(Text("★", size=30, color="#e8b923"), crop=(0, 0, r["star"], 1.0), crop_relative=True)
            text "Route bonus: applied overnight" size 22 color "#d8dde8"
            text "Chest: within spec — no adjustment required" size 22 color "#d8dde8"
            text "Next tier: %s" % r["next"] size 22 color "#d8dde8"

## THE EMAILS (and Vellum's one reply): a phone card, quoted word for word.
screen fs_mail(lines):
    zorder 60
    frame:
        xalign 0.5 ypos 60 xsize 820
        padding (28, 20)
        background Frame(Solid("#f4f5f7f2"), 0, 0)
        vbox:
            spacing 10
            for t in lines:
                text t size 22 color "#22252b"

## THE MANIFEST on day 6: the next address ticked off a door at a time, never counted.
screen fs_manifest(left):
    zorder 60
    frame:
        xalign 0.97 ypos 60 xsize 420
        padding (24, 18)
        background Frame(Solid("#101826e8"), 0, 0)
        vbox:
            spacing 6
            text "{b}MANIFEST · AMBASSADOR{/b}" size 22 color "#e8b923"
            for done, addr in left:
                text (("{s}%s{/s}" % addr) if done else addr) size 20 color ("#7d8494" if done else "#ffffff")

## The scanner's verdict for one region (vellum_scan): never a figure. The chest is always within.
init python:
    def fs_scan(region, out=True):
        if out:
            return "“%s: outside spec — size up.”" % region
        return "“%s: within spec — no adjustment required.”" % region

## Route select's entry. Just before six on the first morning, in the van bay.
label fivestars_start:
    $ fs = VNState(tier=0, body=0, fit="own")
    $ fs_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=5, minute=45)
    ## the HUD and the box portrait key on vn_route
    $ vn_route = "fivestars"
    $ fs_pc_name = "Toby"
    ## the name box: Toby, unless you'd like another (the app always prints T. PRENTICE). A test
    ## walk keeps Toby.
    if not renpy.session.get("vn_picks"):
        $ fs_pc_name = renpy.input("Your name? (Toby, unless you'd like another.)", default="Toby", length=20).strip() or "Toby"
    jump fs_opening

## The end of the route: back to the route select.
label fs_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"fivestars"}
    $ vn_route = None
    hide screen fs_dash
    hide screen fs_mail
    hide screen fs_manifest
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e8b923}Five Stars, No Notes{/color}{/size}\n\n{i}The end.{/i}"
    jump start
