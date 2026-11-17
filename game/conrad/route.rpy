## Conrad -- "My Sugar Daddy Found Out I'm Not a Girl and Had Me Made Properly" (rewritten straight in Ren'Py,
## 2026-11-12; the plan is PLAN.md beside this file, signed off by the owner). From the package (TheStoryNexusTauriApp/
## packages/sent/my-sugar-daddy-found-out-package.md), kept verbatim in catalog/docs/routes/vn-original/conrad/.
##
## THE NON-CON PASS, heavier (owner, 2026-11-12: "this one can we more heavily non-con"): the package's no-refusal
## rule is overturned for ch 1-4. Conrad never threatens and never uses the photos; he just doesn't stop, and books
## the appointments and injections without asking. Forced: ch 1 the catch (his first time), ch 2 the throat and
## "getting you ready", ch 3 the titjob after the pads go in the bin, ch 4 the device fitted over his no and the
## first anal. The flip is ch 5 at the out: Conrad deletes the photos and offers everything, and Devin refuses with
## four excuses and asks. Ch 6-7 consensual. No tears, no menace, no pain, no escape. Denial mode to the last line;
## he/him in narration throughout (the package).
##
## The kit is the ratchet (razor, pads, tape, padded shorts and contour, the voice, "nothing comes off"); the book
## (Gift / Value / Owed) is the quantity. Rows: 0 Devin in the kit; 3 the chest; 4 ass and thighs, the cock small;
## 5 the face and the voice; 6 complete, a pussy. Rose-gold hair (the owner's pick). All route-local names carry cnr_.

init -10 python:
    CNR = "art/conrad/"

    CNR_ROWS = ["0", "3", "4", "5", "6"]

    def cnr_body(row):
        row = str(row)
        if CNR_ROWS.index(row) > CNR_ROWS.index(cnr.row or "0"):
            cnr.row = row

    # THE BOOK: the spreadsheet on his phone.
    CNR_BOOK = {
        1: "THE BOOK.  Marcus: car, eleven months of dinners.  Terrence: four months of rent, a phone.  Neil: Cartier bracelet, Barcelona.  Owed: Conrad.",
        2: "THE BOOK.  Invoice sent: Marcus.  Requested: Terrence (rent).  Owed: Conrad.",
        3: "THE BOOK.  New column: Spent.  Pads (binned). Razor (binned). Appointment (asked for).",
        4: "THE BOOK.  Spent: every dress. Every pair of jeans. Every bra. (No line for the device.)",
        5: "THE BOOK.  Stale. Payout: declined.  Owed (Conrad's side): one procedure.",
        7: "THE BOOK.  Owed: Marcus, Terrence, Neil.  Settling up, line by line.",
    }

    _cnr_have = {}

    def _cnr_has(n):
        if n not in _cnr_have:
            _cnr_have[n] = renpy.loadable(CNR + n + ".png")
        return _cnr_have[n]

    def cnr_pc_file(face):
        r = cnr.row or "0"
        fit = cnr.fit or "kit"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-smug" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-smug" % r]
        for n in names:
            if _cnr_has(n):
                return CNR + n + ".png"
        return CNR + names[-1] + ".png"

    def cnr_face_now():
        a = renpy.get_attributes("cnr_pc")
        return a[0] if a else "smug"

    def _cnr_portrait(st, at):
        p = vn_art_file(cnr_pc_file(cnr_face_now()))
        crops = globals().get("conrad_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["conrad"] = lambda: DynamicDisplayable(_cnr_portrait)

    vn_sprite_image("cnr_pc", ("smug", "caught", "flushed", "begging", "greedy"), cnr_pc_file, who="pc")
    for _w, _faces in (("conrad", ("amused", "unhurried")), ("chloe", ("cackle",)), ("marcus", ("loud",)), ("terrence", ("eager",)), ("neil", ("soft",))):
        vn_sprite_image("cnr_" + _w, _faces, (lambda w: (lambda f: CNR + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(CNR) and _f.endswith(".jpg"):
            _n = _f[len(CNR):-4]
            vn_register_bg("cnr_" + _n.replace("-", "_"), _f)
            vn_register_cg("cnr_" + _n.replace("-", "_"), _f)

    vn_register_route("conrad", "My Sugar Daddy Found Out I'm Not a Girl and Had Me Made Properly",
        "Four sugar daddies, a padded bra, three hours of prep, and one rule: nothing comes off. A car, four months' rent, a Cartier bracelet, and a year of giving nobody anything. Then Conrad books a weekend you can't tease your way out of.",
        CNR + "cover.jpg", "conrad_start")

    achievement.register("Settled Up")

default cnr = VNState(row="0", fit="kit", chapter=0, invoice=None, gripe=None, excuse=None, ending=None, broke=False, asked=False)

define cnr_you = VNChar("Devin", who="pc", plate="#c08a8a")
define cnr_conrad = VNChar("Conrad", who="cnr_conrad", plate="#2a2a34")
define cnr_chloe = VNChar("Chloe", who="cnr_chloe", plate="#8a3a6a")
define cnr_marcus = VNChar("Marcus", who="cnr_marcus", plate="#6a4a2a")
define cnr_terrence = VNChar("Terrence", who="cnr_terrence", plate="#2a5a6a")
define cnr_neil = VNChar("Neil", who="cnr_neil", plate="#5a5a6a")

## THE BOOK.
screen cnr_book(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        xmaximum 1180
        padding (30, 16)
        background Frame(Solid("#0f2a1af0"), 0, 0)
        text CNR_BOOK[n] size 23 color "#dff0e0"

label conrad_start:
    $ cnr = VNState(row="0", fit="kit", chapter=0, invoice=None, gripe=None, excuse=None, ending=None, broke=False, asked=False)
    $ vn_clock = VNState(day=1, hour=17, minute=0)
    $ vn_route = "conrad"
    jump cnr_ch1

label cnr_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"conrad"}
    $ vn_route = None
    hide screen cnr_book
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#e0a0a0}Settled Up{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _cnr_trace():
        pc = cnr_pc_file(cnr_face_now()).rsplit("/", 1)[-1] if renpy.showing("cnr_pc") else None
        cast = None
        for _t in ("cnr_conrad", "cnr_chloe", "cnr_marcus", "cnr_terrence", "cnr_neil"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, cnr.fit

    vn_trace_routes["conrad"] = _cnr_trace
