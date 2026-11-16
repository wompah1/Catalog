## Club -- "The Manager Wears the Skirt, and Every Alumna Is a Woman" (rewritten straight in Ren'Py,
## 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From
## catalog/game/02-engine/storylines/club/ (club.js: the rungs with their tellings, clipboard lines
## and mirror lines, the board, the S folder, the duty sheet, the fixture card, the wakes, the
## roster's and Rhys's lines and the PC's pool; main.twee, rungs.twee, ending.twee), kept verbatim
## in catalog/docs/routes/vn-original/club/.
##
## THE NON-CON PASS (owner, 2026-10-19/20, as signed off): through rung 4 the roster TAKES: "Next"
## is what they call over your objections, until you call it yourself at rung 4's flip ("Please
## form an orderly line."). Rhys is the one partner who asks ("Say if—" / "Continue."); every Rhys
## scene, the mandatory rung 5 and the balcony are consensual. Ken knows, and files it anyway.
##
## Nothing inside you but your mouth before the slump, and only Rhys ever: the first anal at rung 5
## (in your bed, mandatory), the first vaginal at rung 6. No DP. Iris, the alumnae and the coach
## never touch; the association never watches sex; no phone or camera during sex. Full TSF: the cock
## goes at the bottom of the nationals dogpile. She/her from the photo wall. No measuring (one cup
## letter a rung, on the slip), no school or youth framing. All route-local names carry clb_.

init -10 python:
    CLB = "art/club/"

    # THE TELLING (the hub's first line), THE CLIPBOARD (shorter every rung, one word at the end),
    # and THE MIRROR, by tier.
    CLB_TELLING = [
        "A notice on the board in the main corridor: {i}Men's volleyball needs a manager. No experience needed.{/i}",
        "A skirt in a box, and the coach's first words of the season: {i}\"Thirty years.\"{/i}",
        "Ollie, at full volume, paying out the board's first column: {i}\"The manager's WAIST!\"{/i}",
        "Iris Kendal, in a corridor at the qualifiers: {i}\"Outgrow the uniform, and they'll order you a prettier one.\"{/i}",
        "The photo wall: two photos a year for thirty years. A young man with a clipboard, and a radiant woman with the same clipboard. {i}\"How many of those are coaches now, do you think?\"{/i}",
        "Iris, at the semifinal, out loud: {i}\"Have you noticed?\"{/i}",
        "Madame Lacroix, into a microphone, at the banquet: {i}\"Our newest sister.\"{/i}",
    ]
    CLB_CLIPBOARD = [
        "",
        "Uniform: non-standard. Precedent: thirty years. Second course: hydration support, by rotation. Review cup placement. Filed under: team culture.",
        "First reorder. Cause: laundry. Board inside closet door: protein intake, presumably. Filed under: unrelated.",
        "Rival manager: advanced uniform, high contentment, similar methods. Ribbon received. Filed under: networking.",
        "Inspection passed. Excellent records; requested their filing system. Filed under: tradition.",
        "Special training: completed. No further notes.",
        "happy",
    ]
    CLB_LOOKS = [
        "",
        "Smooth everywhere. Not a hair below the eyebrows, and a gloss on your skin like you've been oiled.",
        "The waistband sits somewhere new. Hips under it, a round little ass, and nipples gone puffy against the blouse.",
        "Thighs that fill a seat. Small soft handfuls pulling the blouse's buttons. Wavy hair down to your shoulders, and a voice a step up from where it was.",
        "Real breasts, a C on the reorder slip. An ass like a shelf. Lashes, fuller lips, soft-brown hair at your shoulders.",
        "Heavy and high. Hips past the skirt's patience. Hair half-up in Iris's bow, and a cock that's barely a thumb.",
        "Stacked, honey-gold, finished. The association's brooch over your heart.",
    ]
    # The S folder: how thick it's got, never a count.
    CLB_FOLDER = [
        "The club's document box has an S folder. It's empty.",
        "The S folder holds a single leaflet. Unread.",
        "The S folder has a couple of leaflets in it now. Unread.",
        "The S folder is getting a respectable thickness. All unread.",
        "The S folder has gone fat. None of it read.",
        "The S folder won't shut without its elastic. You've never opened a leaflet.",
        "The S folder needs both hands. Every leaflet in it is pristine.",
    ]
    # The fixture card: the next event, by the tier you're at.
    CLB_FIXTURE = ["", "Camp. The minibus leaves %s.", "Qualifiers. The coach leaves %s.",
                   "The mid-season inspection. The association calls %s.", "League fixtures, starting %s.",
                   "Nationals. The coach leaves %s.", ""]
    # The mornings with nothing to land (Club Wake), by tier.
    CLB_WAKES = [
        "Your room at the top of the narrow house on Domus Street. The clipboard's on the desk where you left it.",
        "The uniform's on the chair where you folded it. You run a hand down your thigh under the duvet: silk, all the way up. Your cock stirs against your wrist. You file it under hydration.",
        "The skirt's on the chair, and your hips remember it. You squeeze your own ass under the duvet, both hands, for verification. {i}Hnn.{/i} Verified.",
        "Your thighs press together under the duvet, soft and heavy, and your little handfuls tingle in the blouse you slept in. You pinch a nipple to check it's still sensitive. \"{i}Ah{/i}—\" Still sensitive.",
        "Your tits are heavy on your chest before you're awake. You cup them because they're there, and your little cock leaks into the lace. \"Well-fitted,\" you tell the ceiling.",
        "His tracksuit jacket's on your chair. Your ass hums. The pillow smells like him, and you grin into it like an idiot. \"Recovery work,\" you remind it.",
        "Honey-gold hair all over your pillow. You stretch, and everything moves.",
    ]

    def clb_body(n):
        clb.row = str(max(int(clb.row or 0), n))

    def clb_due():
        """The rung that's due today (no downtime: the day after the last rung), or 0."""
        t = clb.tier or 0
        if t >= 6 or clb.ending:
            return 0
        if t == 0:
            return 1
        return t + 1 if vn_clock.day > (clb.rung_day or 0) else 0

    def clb_fixture():
        t = clb.tier or 0
        if t < 1 or t >= 6:
            return ""
        return CLB_FIXTURE[t] % ("today, after practice" if clb_due() else "tomorrow")

    def clb_did(duty):
        return (clb.did or {}).get(duty) == vn_clock.day

    def clb_mark(duty):
        d = dict(clb.did or {})
        d[duty] = vn_clock.day
        clb.did = d

    def clb_vocative():
        return "Rhys" if (clb.tier >= 5 or clb.slump) else "Captain"

    # ---- the stage --------------------------------------------------------------------------
    # Outfits: "own" (his own T-shirt and jeans, the opening), "u1" (the box: white blouse, long blue
    # cut skirt, blue ribbon tie, white socks, loafers), "u2" (the first reorder, the shorter skirt),
    # "u3" (u2 with Iris's red bow), "u4" (the second reorder: the short skirt, the ruffled blouse,
    # the bow), "dress" (the navy dress uniform, the brooch), "jacket" (the dress uniform under
    # Rhys's tracksuit jacket, the balcony on), "towel" (the camp bath), "nude".
    _clb_have = {}

    def _clb_has(n):
        if n not in _clb_have:
            _clb_have[n] = renpy.loadable(CLB + n + ".png")
        return _clb_have[n]

    def clb_pc_file(face):
        r, fit = clb.row or "0", clb.fit or "own"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-deadpan" % (r, fit),
                 "pc-r%s-u1-%s" % (r, face), "pc-r%s-u1-deadpan" % r]
        for n in names:
            if _clb_has(n):
                return CLB + n + ".png"
        return CLB + names[-1] + ".png"

    def clb_face_now():
        a = renpy.get_attributes("clb_pc")
        return a[0] if a else "deadpan"

    def _clb_portrait(st, at):
        p = vn_art_file(clb_pc_file(clb_face_now()))
        crops = globals().get("club_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["club"] = lambda: DynamicDisplayable(_clb_portrait)

    vn_sprite_image("clb_pc", ("deadpan", "flustered", "loud", "soft"), clb_pc_file, who="pc")
    for _w, _faces in (("rhys", ("composed", "red")), ("ollie", ("grin", "loud")), ("hugh", ("shy", "sincere")),
                       ("iris", ("serene", "smile")), ("lacroix", ("warm", "pleased")), ("coach", ("flat",))):
        vn_sprite_image("clb_" + _w, _faces, (lambda w: (lambda f: CLB + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(CLB) and _f.endswith(".jpg"):
            _n = _f[len(CLB):-4]
            vn_register_bg("clb_" + _n.replace("-", "_"), _f)
            vn_register_cg("clb_" + _n.replace("-", "_"), _f)

    vn_register_route("club", "The Manager Wears the Skirt, and Every Alumna Is a Woman",
        "You're twenty, a second-year, and your CV is a list of hobbies. The men's volleyball club needs a manager, and the coach has a box ready for you. The kit in it has a skirt. Tea service means kneeling. The second course means exactly what it looks like. Nobody hides a thing, and you file every bit of it under something boring.",
        CLB + "cover.jpg", "club_start")

    achievement.register("Association Member")

default clb = VNState(row="0", fit="own", tier=0, rung_day=0, did={}, boxes=0, leaflets=0)
default clb_pc_name = "Ken"

define clb_you = VNChar("[clb_pc_name]", who="pc", plate="#2a4a7a")
define clb_rhys = VNChar("Rhys", who="clb_rhys", plate="#1a3a6a")
define clb_ollie = VNChar("Ollie", who="clb_ollie", plate="#c86a1a")
define clb_hugh = VNChar("Hugh", who="clb_hugh", plate="#4a6a3a")
define clb_iris = VNChar("Iris", who="clb_iris", plate="#a01a2a")
define clb_lacroix = VNChar("Madame Lacroix", who="clb_lacroix", plate="#6a8ab8")
define clb_coach = VNChar("The coach", who="clb_coach", plate="#6b6b78")
define clb_roster = VNChar("The roster", who="other", plate="#3a4a6a")
define clb_other = VNChar("Somebody", who="other", plate="#6b6b78")

## THE CLUBROOM WALL: the latest telling, the duty sheet (the second course struck from the slump),
## and the fixture card. Never a number.
screen clb_room():
    zorder 60
    $ _t = max(0, min(6, clb.tier or 0))
    frame:
        xalign 0.5 ypos 46 xsize 980
        padding (30, 18)
        background Frame(Solid("#14203af0"), 0, 0)
        vbox:
            spacing 9
            text "{b}How plainly you've been told:{/b} %s" % CLB_TELLING[_t] size 22 color "#e8c35a"
            if _t >= 5 or clb.done:
                text "{b}The duty sheet:{/b} Tea service. {s}Second course: hydration support, by rotation.{/s} (a neat line, in the captain's pen.) Towel duty. Road duty (front seat, next to the captain)." size 21 color "#d8dce8"
            else:
                text "{b}The duty sheet:{/b} Tea service (kneeling; then {i}second course: hydration support, by rotation{/i}). Towel duty. Road duty (front seat). The inspection, with morale management after it." size 21 color "#d8dce8"
            text "%s" % CLB_FOLDER[max(0, min(6, clb.leaflets or 0))] size 21 color "#b8bcc8"
            if clb_fixture():
                text "{b}The fixture card:{/b} %s" % clb_fixture() size 21 color "#e8c35a"

## OLLIE'S BOARD, taped inside the closet door: columns headed with parts of you, names under each,
## never a figure; struck as each pays out. Then the new sheet, its heading folded over: WEDDING.
screen clb_board():
    zorder 61
    $ _t = max(0, min(6, clb.tier or 0))
    frame:
        xalign 0.5 ypos 70 xsize 640
        padding (30, 22)
        background Frame(Solid("#f4f1e8f2"), 0, 0)
        vbox:
            spacing 10
            if _t <= 4:
                text "{b}THE BOARD{/b}" size 22 color "#2a2a2a" xalign 0.5
                hbox:
                    spacing 60
                    xalign 0.5
                    for _i, _h in enumerate(("WAIST", "HIPS", "CHEST")):
                        vbox:
                            spacing 4
                            if _t >= _i + 2:
                                text "{s}%s{/s}" % _h size 26 color "#c01818"
                            else:
                                text "{b}%s{/b}" % _h size 26 color "#1a2a5a"
                            text "Ollie\nHugh\nMarcus" size 18 color "#4a4a4a"
                if _t >= 4:
                    text "{i}Laminated.{/i}" size 18 color "#6a6a6a" xalign 0.5
            elif _t == 5:
                text "A new sheet. Its heading is folded over, so you can't read it." size 22 color "#2a2a2a"
                text "{i}Long odds.{/i}" size 18 color "#6a6a6a"
            else:
                text "{b}{color=#e0408a}WEDDING{/color}{/b}" size 30 xalign 0.5
                text "A column of names under it. Long odds." size 18 color "#6a6a6a" xalign 0.5

## THE CLIPBOARD: the rung's line, shorter every rung; one word at the end.
screen clb_clipboard(n):
    zorder 61
    frame:
        xalign 0.5 ypos 80 xsize 620
        padding (34, 26)
        background Frame(Solid("#c8a878f2"), 0, 0)
        frame:
            xfill True
            padding (22, 18)
            background Frame(Solid("#fbf8f0"), 0, 0)
            text "{i}%s{/i}" % CLB_CLIPBOARD[max(1, min(6, n))] size 23 color "#1a2a4a"

## A slip or a card: the reorder slip, the notice, the regimen card.
screen clb_slip(title, lines):
    zorder 61
    frame:
        xalign 0.5 ypos 80 xsize 620
        padding (30, 22)
        background Frame(Solid("#eef2f8f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}%s{/b}" % title size 23 color "#1a3a6a"
            for _l in lines:
                text _l size 22 color "#2a2a2a"

label club_start:
    $ clb = VNState(row="0", fit="own", tier=0, rung_day=0, did={}, boxes=0, leaflets=0)
    $ vn_clock = VNState(day=1, hour=13, minute=0)
    $ vn_route = "club"
    $ clb_pc_name = "Ken"
    if not renpy.session.get("vn_picks"):
        $ clb_pc_name = renpy.input("Your name? (Ken, unless you'd like another. Doyle either way; Kenneth on the forms.)", default="Ken", length=20).strip() or "Ken"
    jump clb_opening

label clb_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"club"}
    $ vn_route = None
    hide screen clb_room
    hide screen clb_board
    hide screen clb_clipboard
    hide screen clb_slip
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}Association Member{/color}{/size}\n\n{i}The end.{/i}"
    jump start
