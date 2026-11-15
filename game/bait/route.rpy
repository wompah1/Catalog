## Bait -- "My Class Is [Bait]…" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file,
## signed off by the owner). From the package Bait (TheStoryNexusTauriApp/packages/sent/bait-package.md), kept
## verbatim in catalog/docs/routes/vn-original/bait/.
##
## THE NON-CON PASS, "The lure answers" (owner, 2026-11-12, as signed off): he turns the dial; he never agrees to
## what answers once it has him. Ch 1 the first incident (the warg-woman); ch 2-5 forced (the slime-woman, the
## myconid, the harpy, the kobold band); ch 6 the dryad, he breaks into begging; ch 7 Maren, no sex; ch 8 the
## flip, he asks Sable out loud; ch 9-11 consensual. No tears, no menace, no pain (the oni works because of the
## slime's elasticity), no escape. The register comic and gleeful, never bleak.
##
## Recast as people (the SOURCES row): a feral humanoid warg-woman, a humanoid slime-woman, a humanoid myconid
## woman whose spores are only a perfume (nothing grows in him), a band of kobold women of grown size; the
## court's arachne kept (the owner). Every partner futa or male and bigger than him. The breasts stop at the
## house cap. Wolf-grey hair from the warg's souvenir on (the owner's pick); no red, no twin tails. he/him in
## narration to ch 10; the monsters and the panel use her/she from ch 4; she from ch 11. His name said once,
## by Maren. All route-local names carry bai_.

init -10 python:
    BAI = "art/bait/"

    BAI_ROWS = ["0", "1", "2", "4", "6", "8", "9"]

    def bai_body(row):
        row = str(row)
        if BAI_ROWS.index(row) > BAI_ROWS.index(bai.row or "0"):
            bai.row = row

    # THE PANEL: the CLASS line and what it has logged.
    BAI_PANEL = {
        1: ("[[Bait]", "Lure: active (passive floor: low).  Aspects: Warg."),
        2: ("[[Bait]", "Aspects: Warg. Slime."),
        3: ("[[Bait]", "Lure potency: HIGH.  Aspects: Warg. Slime. Bloom."),
        4: ("[[Bait]", "Aspects: Warg. Slime. Bloom. Harpy."),
        5: ("[[Bait]", "Passive floor: rising.  Aspects: (no change)."),
        6: ("[[Bait]", "Aspects: … Dryad."),
        8: ("[[Bait]", "Aspects: … Werewolf.  Cycle: continuous."),
        9: ("[[Bait]", "Aspects: … Oni."),
        10: ("[[Throne]", "Runs on being ridden. Drains when it isn't. Abdication: available."),
    }
    # THE NUMBER: his scrap of hide, crossed out and rewritten.
    BAI_NUMBER = {
        1: "Strong enough to get out.",
        2: "Strong enough to survive the trip out.",
        3: "Strong enough to survive the trip out, with margin.",
        4: "Strong enough to MAKE something carry me out.",
        5: "Strong enough for whatever shows up.",
        6: "Strong enough to travel like this. (wait)",
    }

    _bai_have = {}

    def _bai_has(n):
        if n not in _bai_have:
            _bai_have[n] = renpy.loadable(BAI + n + ".png")
        return _bai_have[n]

    def bai_pc_file(face):
        r = bai.row or "0"
        fit = bai.fit or "trapper"
        names = ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-cheerful" % (r, fit),
                 "pc-r%s-nude-%s" % (r, face), "pc-r%s-nude-cheerful" % r]
        for n in names:
            if _bai_has(n):
                return BAI + n + ".png"
        return BAI + names[-1] + ".png"

    def bai_face_now():
        a = renpy.get_attributes("bai_pc")
        return a[0] if a else "cheerful"

    def _bai_portrait(st, at):
        p = vn_art_file(bai_pc_file(bai_face_now()))
        crops = globals().get("bait_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["bait"] = lambda: DynamicDisplayable(_bai_portrait)

    vn_sprite_image("bai_pc", ("cheerful", "alarmed", "flushed", "begging", "regal"), bai_pc_file, who="pc")
    for _w, _faces in (("maren", ("calm",)), ("sable", ("polite",))):
        vn_sprite_image("bai_" + _w, _faces, (lambda w: (lambda f: BAI + w + "-" + f + ".png"))(_w))

    for _f in renpy.list_files():
        if _f.startswith(BAI) and _f.endswith(".jpg"):
            _n = _f[len(BAI):-4]
            vn_register_bg("bai_" + _n.replace("-", "_"), _f)
            vn_register_cg("bai_" + _n.replace("-", "_"), _f)

    vn_register_route("bait", "My Class Is [[Bait]…",
        "You wake face-down in the dirt of a forest that isn't on Earth. No summoner, no party, no explanation. Just a panel in the air, and under CLASS, one word. You assume it's a bad translation.",
        BAI + "cover.jpg", "bait_start")

    achievement.register("Throne")

default bai = VNState(row="0", fit="trapper", chapter=0, dial=None, maren=None, ruling=None, ruling2=None, ending=None, broke=False, asked=False, panic=None, free=None, ruled=None, shout1=None, shout2=None, shout4=None, shout5=None, break6=None, ask=None)

define bai_you = VNChar("Theo", who="pc", plate="#7a8088")
define bai_maren = VNChar("Maren", who="bai_maren", plate="#5a6a4a")
define bai_sable = VNChar("Sable", who="bai_sable", plate="#3a3a4a")
define bai_sys = VNChar("PANEL", who="panel", plate="#2a5a7a")

## THE PANEL.
screen bai_panel(n):
    zorder 60
    frame:
        xalign 0.5 ypos 50
        padding (34, 18)
        background Frame(Solid("#0c1a26e8"), 0, 0)
        vbox:
            spacing 6
            text ("CLASS:  " + BAI_PANEL[n][0]) size 32 color "#9fd8ff" bold True
            text BAI_PANEL[n][1] size 22 color "#cfe8f8"

## THE NUMBER: the scrap of hide.
screen bai_number(n):
    zorder 60
    frame:
        xalign 0.5 ypos 60
        padding (30, 16)
        background Frame(Solid("#6a4a2af0"), 0, 0)
        text ("The number:  " + BAI_NUMBER[n]) size 26 color "#f6ead2"

label bait_start:
    $ bai = VNState(row="0", fit="trapper", chapter=0, dial=None, maren=None, ruling=None, ruling2=None, ending=None, broke=False, asked=False, panic=None, free=None, ruled=None, shout1=None, shout2=None, shout4=None, shout5=None, break6=None, ask=None)
    $ vn_clock = VNState(day=1, hour=9, minute=0)
    $ vn_route = "bait"
    jump bai_ch1

label bai_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"bait"}
    $ vn_route = None
    hide screen bai_panel
    hide screen bai_number
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#9fd8ff}[[Throne]{/color}{/size}\n\n{i}The end.{/i}"
    jump start

init 110 python:
    def _bai_trace():
        pc = bai_pc_file(bai_face_now()).rsplit("/", 1)[-1] if renpy.showing("bai_pc") else None
        cast = None
        for _t in ("bai_maren", "bai_sable"):
            if renpy.showing(_t):
                cast = _t[4:] + " " + " ".join(renpy.get_attributes(_t) or ())
                break
        return pc, cast, bai.fit

    vn_trace_routes["bait"] = _bai_trace
