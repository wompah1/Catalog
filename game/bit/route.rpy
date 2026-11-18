## Bit -- "The Bit That Kept Running" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file,
## signed off by the owner). From the package (TheStoryNexusTauriApp/packages/sent/the-bit-that-kept-running-package.md),
## kept verbatim in catalog/docs/routes/vn-original/bit/.
##
## THE NON-CON PASS, "Not a bit" (owner, 2026-11-12, as signed off): the package forbids refusals; this pass
## overturns that for the first chapters. Ch 1 the first incident (Miku's "C'mere" over his no; he'd laughed the
## dare off); ch 2 the cage locked over his no and the first anal, forced; ch 3 the izakaya cubicle starts forced and
## breaks into begging; ch 4 the flip, the package's own turn: sober, in daylight, they offer to stop and he says no
## to stopping, out loud, then asks to be taken to the flat; ch 5-6 consensual. No tears, no menace, no pain, no
## escape; never cruel. FEMBOY, NOT TSF: the cock stays and is used; the chest never grows (forms); the ass and
## thighs are the ladder (ch 3, ch 5, the biggest in ch 6). The mechanism never explained. Japanese names (the
## package; the owner's pick over the SOURCES row's Western names); a university circle, never "student", no school.
## The album renamed HANA mid-act in ch 4: she/her from that line. Bleached blonde. All route-local names carry bit_.
##
## BET THEY GROW (an alternate route; owner, 2026-11-13 about 1:37 pm ET, signed off from c9's proposal): at ch 4's shop
## counter Hana pushes the bigger forms back and bets they'll grow ("This choice decides your ending"). Rena pins it to
## the list, and whatever goes on the list comes true (never explained). No forms from there; ch 5 a real medium
## (bit.grown 1, sprites 5g), ch 6 the house cap, huge (2, 6g; the owner's ruling, 2026-11-15: alt tits lanes end at
## the cap); before that flat with no forms (3n). Twins art/bit/<name>-g.jpg,
## shown in place while bit.bet. The cock stays, femboy. Alternate-route art is queued last.

init -10 python:
    BIT = "art/bit/"

    BIT_ROWS = ["0", "1", "2", "3", "5", "6"]

    # BET THEY GROW's list: item 10 is the bet, and item 11 gains the top.
    BIT_LIST_BET = {
        4: "1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. BET: no forms 11. skirt (S) 12. wipes",
        5: "1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. BET: no forms (WON) 11. skirt (S), top (S) 12. wipes 13. plug 14. hair oil 15. no key ♡",
        6: "1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. BET: no forms (WON) 11. skirt (L), top (L) 12. wipes 13. plug 14. hair oil 15. no key ♡",
    }

    def bit_list_line(n):
        return BIT_LIST_BET.get(n) if (bit.bet and n in BIT_LIST_BET) else BIT_LIST[n][0]

    def bit_body(row):
        row = str(row)
        if BIT_ROWS.index(row) > BIT_ROWS.index(bit.row or "0"):
            bit.row = row

    # THE PINNED LIST, verbatim, and the album line.
    BIT_LIST = {
        1: ("1. wig 2. lashes 3. nails", "ALBUM: THE BIT — WEEK 1 · 47 photos"),
        2: ("1. wig 2. lashes 3. nails 4. heels 5. forms 6. key", "ALBUM: THE BIT — WEEK 2 · 130 photos"),
        3: ("1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties", "ALBUM: THE BIT — WEEK 3 · 264 photos"),
        4: ("1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. bigger forms 11. skirt (S) 12. wipes", "ALBUM: HANA — WEEK 4 · 411 photos"),
        5: ("1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. bigger forms 11. skirt (S) 12. wipes 13. plug 14. hair oil 15. no key ♡", "ALBUM: HANA — WEEK 5 · 602 photos"),
        6: ("1. wig 2. lashes 3. nails 4. heels 5. forms 6. key 7. tights 8. lube 9. spare panties 10. bigger forms 11. skirt (L) 12. wipes 13. plug 14. hair oil 15. no key ♡", "ALBUM: HANA — WEEK 6 · 838 photos"),
    }

    _bit_have = {}

    def _bit_has(n):
        if n not in _bit_have:
            _bit_have[n] = renpy.loadable(BIT + n + ".png")
        return _bit_have[n]

    def bit_pc_file(face):
        r = bit.row or "0"
        fit = bit.fit or "own"
        # Bet they grow: no forms (3n), then the real chest (5g, 6g), then the canon row's
        rows = [r + ("g" if bit.grown else "n"), r] if bit.bet else [r]
        names = []
        for k in rows:
            names += ["pc-r%s-%s-%s" % (k, fit, face), "pc-r%s-%s-sheepish" % (k, fit), "pc-r%s-nude-%s" % (k, face), "pc-r%s-nude-sheepish" % k]
        for n in names:
            if _bit_has(n):
                return BIT + n + ".png"
        return BIT + names[-1] + ".png"

    def bit_face_now():
        a = renpy.get_attributes("bit_pc")
        return a[0] if a else "sheepish"

    def _bit_portrait(st, at):
        p = vn_art_file(bit_pc_file(bit_face_now()))
        crops = globals().get("bit_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["bit"] = lambda: DynamicDisplayable(_bit_portrait)

    vn_sprite_image("bit_pc", ("sheepish", "flustered", "begging", "giddy", "filthy"), bit_pc_file, who="pc")
    for _w, _faces in (("miku", ("flat",)), ("rena", ("loud",)), ("saki", ("filming",)), ("nono", ("sorry",)), ("kaito", ("cheerful",))):
        vn_sprite_image("bit_" + _w, _faces, (lambda w: (lambda f: BIT + w + "-" + f + ".png"))(_w))

    # Bet they grow's twin of a picture: <name>-g.jpg, shown in its place while bit.bet (the hypno full regimen's way).
    _bit_twin = {}

    def _bit_g_of(path):
        if not bit.bet:
            return path
        if path not in _bit_twin:
            t = path[:-4] + "-g.jpg"
            _bit_twin[path] = t if renpy.loadable(t) else None
        return _bit_twin[path] or path

    def _bit_cg_dd(st, at, path):
        return vn_cg(vn_art_file(_bit_g_of(path))), None

    def _bit_bg_dd(st, at, path):
        return vn_bg(vn_art_file(_bit_g_of(path))), None

    for _f in renpy.list_files():
        if _f.startswith(BIT) and _f.endswith(".jpg"):
            _n = _f[len(BIT):-4]
            if _n.endswith("-g"):
                continue
            _k = "bit_" + _n.replace("-", "_")
            vn_cg_files[_k] = _f
            renpy.image(("cg", _k), DynamicDisplayable(_bit_cg_dd, _f))
            renpy.image(("bg", _k), DynamicDisplayable(_bit_bg_dd, _f))

    vn_register_route("bit", "The Bit That Kept Running",
        "A year orbiting a gyaru circle at Kitanomiya: four handbags, half the karaoke bill, laughing two seconds late. At three in the morning, out of material, they make you over as a dare. The dare should have ended that night.",
        BIT + "cover.jpg", "bit_start")

    achievement.register("Item Sixteen")
    achievement.register("Bet Won")

default bit = VNState(row="0", fit="own", chapter=0, wax=None, extra=None, nono=None, ending=None, broke=False, asked=False, bet=False, grown=0)
default bit_pc_name = "Tatsuya"

define bit_you = VNChar("[bit_pc_name]", who="pc", plate="#d8b04a")
define bit_miku = VNChar("Miku", who="bit_miku", plate="#6a3a1a")
define bit_rena = VNChar("Rena", who="bit_rena", plate="#c03a6a")
define bit_saki = VNChar("Saki", who="bit_saki", plate="#3a5a8a")
define bit_nono = VNChar("Nono", who="bit_nono", plate="#7a8a5a")
define bit_kaito = VNChar("Kaito", who="bit_kaito", plate="#4a4a4a")
define bit_boys = VNChar("Sho and Daichi", who="boys", plate="#5a5a5a")

## THE PINNED LIST.
screen bit_list(n):
    zorder 60
    frame:
        xalign 0.5 ypos 40
        xmaximum 1200
        padding (30, 16)
        background Frame(Solid("#1a1420f0"), 0, 0)
        vbox:
            spacing 4
            text "PINNED — FRIDAY KIT" size 24 color "#ffb0d8" bold True
            text bit_list_line(n) size 22 color "#f4e8f0"
            text BIT_LIST[n][1] size 22 color "#b8d8ff"

label bit_start:
    $ bit = VNState(row="0", fit="own", chapter=0, wax=None, extra=None, nono=None, ending=None, broke=False, asked=False, bet=False, grown=0)
    $ vn_clock = VNState(day=1, hour=3, minute=0)
    $ vn_route = "bit"
    $ bit_pc_name = "Tatsuya"
    jump bit_ch1

label bit_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"bit"}
    $ vn_route = None
    hide screen bit_list
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#ffb0d8}Item Sixteen{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _bit_trace():
        pc = bit_pc_file(bit_face_now()).rsplit("/", 1)[-1] if renpy.showing("bit_pc") else None
        cast = None
        for _t in ("bit_miku", "bit_rena", "bit_saki", "bit_nono", "bit_kaito"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, bit.fit

    vn_trace_routes["bit"] = _bit_trace
