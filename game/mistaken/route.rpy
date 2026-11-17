## I Misclicked a Women-Only Casting Call and My Body Keeps Filling In the Padding -- the catalog's
## `mistaken` route, rewritten straight in Ren'Py (2026-11-11; owner: "start getting art and doing
## rewrites for the next routes (keep a backup of the original story for reference)"). The DoL
## catalog's version is kept verbatim in catalog/docs/routes/vn-original/mistaken/ (twee, js, spec);
## this is not a conversion of it, it's a rewrite from it, faithful to the signed-off spec.
##
## THE REGISTER (owner, 2026-11-11): "he desperately needed a job, so he applied, realized his
## mistake, and tried to hide he was a man as to not get in trouble, reluctantly consenting as to not
## get his identity exposed." Alec goes along because no is the one answer that gets him found out.
## Rungs 1-4: loud for the lens (the house's loud PC), the thought lines panicking, the body betraying
## him. The rung 5 fork is the first choice that's his. Rung 6, off camera, nobody filming, is the
## first time he wants it. Veronica's "You can say no" is the trap: no means being exposed.
##
## THE LADDER (the spec's): how much of Alexis still comes out of Jessie's case. Every rung a tray
## goes shut because the body filled it in. Rung 5 forks at the forms: retired (TSF, "Alexis Star")
## or kept on (femboy, "Still in the Case"). Linear days, as the other routes; two optional filler
## days (owner: "you can keep some filler"). The ending choices are marked (ending=True).
## All route-local names carry the mk_ prefix.

init -10 python:
    MK = "art/mistaken/"

    # The case's trays, the metronome (mistaken.js setup.mistakenCase): what still comes out of it.
    MK_TRAYS = {
        "wax": "the wax and the razor", "tape": "the tape", "forms": "the forms",
        "pads": "the hip pads", "shaper": "the ass shaper", "contour": "the contour palette",
        "wig": "the wig", "voice": "the voice drills",
    }
    MK_CASE = [
        [],
        ["wax", "tape", "forms", "pads", "shaper", "contour", "wig", "voice"],
        ["tape", "forms", "pads", "shaper", "contour", "wig", "voice"],
        ["tape", "forms", "shaper", "wig"],
        ["tape", "forms"],
        {"tsf": ["tape"], "femboy": ["tape", "forms"]},
        {"tsf": [], "femboy": ["tape", "forms"]},
    ]

    def mk_case(n=None):
        n = mk.tier if n is None else n
        row = MK_CASE[max(0, min(6, n))]
        if isinstance(row, dict):
            row = row.get(mk.branch or "tsf", [])
        return row

    def mk_tray_list(n=None):
        names = [MK_TRAYS[t] for t in mk_case(n)]
        if not names:
            return "nothing at all"
        return names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]

    # The call sheet, in words (mistaken.js): who's about when you sign in, your billing, the day's
    # call, and Jessie's answer to "What are we building today?". Indexed by the rung that's due.
    MK_HUB = [
        "A kettle going in the green room. \"Morning, babe,\" says the girl on reception, not looking up.",
        "Diego passes the end of the corridor and lifts his coffee to you. That's all. That's all he ever does.",
        "Jasmine Gold leans on the desk and watches you sign. Your hand. Your throat. She finds nothing.",
        "\"There she is!\" Crystal yells through the green-room wall. \"Morning, Alexis,\" says Terry, who never talks.",
        "Flowers on reception, your name on the card. \"From the crew.\" Jasmine walks past them twice.",
        "Gus, smoking on the front step: \"Star.\" First thing he's ever called you.",
        "",
    ]
    MK_BILLING = ["Alexis Star, new face", "Alexis Star, featured", "Alexis Star, featured, two set-ups",
                  "Alexis Star, second billing", "Alexis Star, top of the sheet", "Alexis Star, first up", "Alexis Star, first up"]
    MK_CALLS = ["", "",
        "Lingerie stills in the morning. Then the pastel bedroom: Alexis Star and Diego Ramos.",
        "The makeup counter with Crystal Summers. Then a close-up on the pastel bedroom: Alexis Star and Diego Ramos.",
        "A rear-angle scene. Alexis Star and Diego Ramos. A note in Veronica's pen beside it: {i}more{/i}.",
        "The marquee. Diego Ramos, Alexis Star, and a line through Jasmine Gold with Crystal Summers written over it.",
        "",
    ]
    MK_BUILDING = ["Everything.", "Everything. Alexis, from the skin out.", "Most of her.",
                   "Some of her. Less than yesterday.", "The chest and the tuck.",
                   {"tsf": "The tuck.", "femboy": "The chest and the tuck."},
                   {"tsf": "Nothing.", "femboy": "The chest and the tuck. Same as always."}]

    def mk_building(n):
        b = MK_BUILDING[max(0, min(6, n))]
        return b.get(mk.branch or "tsf") if isinstance(b, dict) else b

    MK_LIPS = {"sweet": "Light pink", "bratty": "Red", "filthy": "Dark red"}

    # Each rung's first scene, after the makeup room (rung 5 goes to the fork, rung 6 to Octave).
    MK_RUNG_LABEL = {2: "mk_stills", 3: "mk_masterclass", 4: "mk_rear_angle"}

    # ---- the ladder --------------------------------------------------------------------------
    def mk_advance(n):
        mk.tier = max(mk.tier or 0, n)
        store.mk_enc = VNState(partner_came=True, pc_orgasms=0)

    def mk_body(n):
        """The body lands (up only). Rung 5 lands on set, rung 6 mid-scene, the rest overnight."""
        mk.body = max(mk.body or 0, n)

    def mk_femboy():
        return mk.branch == "femboy"

    # ---- the stage -------------------------------------------------------------------------
    def mk_rung_label():
        r = max(1, min(6, mk.body or 1))
        return "%d%s" % (r, "f" if r >= 5 and mk_femboy() else "")

    _mk_have = {}

    def _mk_has(n):
        if n not in _mk_have:
            _mk_have[n] = renpy.loadable(MK + n + ".png")
        return _mk_have[n]

    def mk_pc_file(face):
        """The sprite that exists: the outfit set with this face, the outfit set's neutral, the own
        clothes with this face, the own clothes' neutral (the other routes' fallback chain)."""
        r, fit = mk_rung_label(), mk.fit
        names = []
        if fit:
            names += ["pc-r%s-%s-%s" % (r, fit, face), "pc-r%s-%s-neutral" % (r, fit)]
        names += ["pc-r%s-%s" % (r, face), "pc-r%s-neutral" % r]
        for n in names:
            if _mk_has(n):
                return MK + n + ".png"
        return MK + names[-1] + ".png"

    def mk_face_now():
        a = renpy.get_attributes("mk_pc")
        return a[0] if a else "neutral"

    def _mk_portrait(st, at):
        p = vn_art_file(mk_pc_file(mk_face_now()))
        x, y, w, h = vn_face_crop(mistaken_face_crops, p)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["mistaken"] = lambda: DynamicDisplayable(_mk_portrait)

    vn_sprite_image("mk_pc", ("neutral", "nervous", "flushed", "shocked", "smirk"), mk_pc_file, who="pc")
    vn_sprite_image("mk_jessie", ("neutral", "smile", "worried"), lambda f: MK + "jessie-" + f + ".png")
    vn_sprite_image("mk_veronica", ("neutral", "smirk"), lambda f: MK + "veronica-" + f + ".png")
    vn_sprite_image("mk_crystal", ("neutral", "smile", "smirk"), lambda f: MK + "crystal-" + f + ".png")
    vn_sprite_image("mk_diego", ("neutral", "grin", "hungry"), lambda f: MK + "diego-" + f + ".png")
    vn_sprite_image("mk_jasmine", ("neutral", "sneer"), lambda f: MK + "jasmine-" + f + ".png")

    # Every picture in the route's folder is a background and a CG by name ("bg mk_office",
    # "cg mk_aud_toy").
    for _f in renpy.list_files():
        if _f.startswith(MK) and _f.endswith(".jpg") and "/scenes/" not in _f:
            _n = _f[len(MK):-4]
            vn_register_bg("mk_" + _n.replace("-", "_"), _f)
            vn_register_cg("mk_" + _n.replace("-", "_"), _f)

    # Two art sets (owner, 2026-11-11: "agreed on having abarus alt version"); the Abarus set has
    # no backgrounds of its own ("they can be generic") and falls back to the Vanripper ones.
    vn_register_art_sets("mistaken", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("mistaken", "I Misclicked a Women-Only Casting Call and My Body Keeps Filling In the Padding",
        "Two hundred job applications in a fortnight, and you stopped reading the tops of the forms. One was for an adult studio on Elk Street. Women only. Rent's due Friday, your best mate Jessie has a case full of tape, forms and a chestnut wig, and nobody at Blaze ever asks. Every week there's less in the case to unpack.",
        MK + "cover.jpg", "mistaken_start")

    achievement.register("Alexis Star")
    achievement.register("Still In The Case")

default mk = VNState(tier=0, body=0)
default mk_enc = VNState(partner_came=True, pc_orgasms=0)

## The speakers. One person, two names: Alec at home, Alexis wherever the build is on (the
## studio's name for her, and the one on the contract). Jessie says "Alec" until rung 5.
define mk_alec = VNChar("Alec", who="pc", plate="#4a6fa5")
define mk_alexis = VNChar("Alexis", who="pc", plate="#d4314f")
define mk_jessie = VNChar("Jessie", who="mk_jessie", plate="#7a5a3a")
define mk_veronica = VNChar("Veronica", who="mk_veronica", plate="#2b2b33")
define mk_crystal = VNChar("Crystal", who="mk_crystal", plate="#d8a93a")
define mk_diego = VNChar("Diego", who="mk_diego", plate="#3d7a5a")
define mk_jasmine = VNChar("Jasmine", who="mk_jasmine", plate="#b8902a")
define mk_gus = VNChar("Gus", who="mk_gus", plate="#5b6270")
define mk_terry = VNChar("Terry", who="mk_terry", plate="#5b6270")
define mk_unk = VNChar("???", who="???", plate="#6b6b78")

## Route select's entry: two in the morning, the misclick.
label mistaken_start:
    $ mk = VNState(tier=0, body=0)
    $ mk_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=0, hour=2, minute=0)
    $ vn_route = "mistaken"
    jump mk_opening

## The end of the route ("Choose another story").
label mk_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"mistaken"}
    $ vn_route = None
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#d4314f}Alexis Star{/color}{/size}\n\n{i}The end.{/i}"
    jump start

## The test trace's view of the stage (game/catalog/vntrace.rpy).
init 110 python:
    def _mk_trace():
        pc = mk_pc_file(mk_face_now()).rsplit("/", 1)[-1] if renpy.showing("mk_pc") else None
        cast = None
        for tag in ("mk_jessie", "mk_veronica", "mk_crystal", "mk_diego", "mk_jasmine"):
            if renpy.showing(tag):
                cast = tag[3:] + " " + " ".join(renpy.get_attributes(tag) or ())
        return pc, cast, mk.fit

    vn_trace_routes["mistaken"] = _mk_trace
