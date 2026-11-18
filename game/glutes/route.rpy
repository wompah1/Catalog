## Glutes -- "I Never Read the Label on My Sunday Shot, and My Coach Says My Glutes Are Finally
## Responding" (rewritten straight in Ren'Py, 2026-11-12; the plan is PLAN.md beside this file,
## signed off by the owner). From catalog/game/02-engine/storylines/glutes/ (glutes.js: the rungs,
## the card, the label, the suits, the lines; main.twee, rungs.twee, rungs-late.twee), kept verbatim
## in catalog/docs/routes/vn-original/glutes/.
##
## THE NON-CON PASS (owner, 2026-10-21: escalating corruption). The arrangement covers hands, and
## nobody renegotiates it; every act past hands at rungs 2-4 is taken. Brady protests frankly in gym
## terms; the framework line is his break and later his flip ("It's the pump", "hip mobility"). The
## shot changes the body, never the will. Rung 1 consensual; rungs 2-3 non-con, never flipped; rung
## 4 the turn (his own "That's just prep", the flip at the end of the assjob); 5 and 6 consensual.
## Misunderstanding mode: no reveal, ever. The off-season after the ending is free play, not ported.
##
## Six check-in Sundays and an epilogue Sunday; the week between is skipped (rung 4 has a Wednesday).
## All route-local names carry gl_.

init -10 python:
    GL = "art/glutes/"

    # THE CARD (setup.glutesCard): its fixed format, words only.
    GL_CARD = [None,
        dict(stage="BASELINE", cls="Men's Physique", note="V-taper. Shorts hide the legs.", fit="drawstring pulled", row="chest", chest="holding", notes="shave everything before photos"),
        dict(stage="THE CUT", cls="Classic Physique", note="scores the glute-ham tie-in", fit="seat snug", row="chest", chest="holding", notes="glutes are finally responding"),
        dict(stage="POSING", cls="Figure", note="shape over mass: shoulders, waist, sweep", fit="seat let out", row="chest", chest="watch it", notes="posing nightly"),
        dict(stage="THE SUIT", cls="Bikini", note="glutes, waist, presentation", fit="the set's the set", row="bust", chest="B", notes="hold the turns"),
        dict(stage="PEAK WEEK", cls="Wellness", note="scores the lower body heaviest", fit="seat let out again", row="bust", chest="D", notes="taper on schedule"),
        dict(stage="SHOW DAY", cls="Wellness", note="scored, placed", fit="the show suit", row="bust", chest="E", notes="off-season starts now"),
    ]
    GL_LABEL = {"old": "TESTOSTERONE · LOWRY · WEEKLY", "box": "ESTRADIOL · LOWRY · WEEKLY"}

    def gl_body(n):
        gl.body = max(gl.body or 0, n)

    # ---- the stage --------------------------------------------------------------------------
    # Rows 0-6 (0 before the shave). Outfits: "gym" (tank top and gym shorts), "hoodie" (rung 3's
    # gym), "suit" (the check-in suit for the row: board shorts, the trunks, the blue bikini, the
    # rung 5 bikini, the show suit), "bra" (rung 5's sports bra), "nude".
    _gl_have = {}

    def _gl_has(n):
        if n not in _gl_have:
            _gl_have[n] = renpy.loadable(GL + n + ".png")
        return _gl_have[n]

    def gl_pc_file(face):
        r, fit = max(0, min(6, gl.body or 0)), gl.fit or "gym"
        names = ["pc-r%d-%s-%s" % (r, fit, face), "pc-r%d-%s-cheerful" % (r, fit),
                 "pc-r%d-gym-%s" % (r, face), "pc-r%d-gym-cheerful" % r]
        for n in names:
            if _gl_has(n):
                return GL + n + ".png"
        return GL + names[-1] + ".png"

    def gl_face_now():
        a = renpy.get_attributes("gl_pc")
        return a[0] if a else "cheerful"

    def _gl_portrait(st, at):
        p = vn_art_file(gl_pc_file(gl_face_now()))
        crops = globals().get("glutes_face_crops", {})
        try:
            x, y, w, h = vn_face_crop(crops, p)
        except Exception:
            x, y, w, h = (0, 0, 200, 200)
        return Transform(Crop((x, y, w, h), p), xysize=(VN_FACE, VN_FACE)), None

    vn_portraits["glutes"] = lambda: DynamicDisplayable(_gl_portrait)

    # The calendar: day 1 is a weekday (the opening, a Wednesday), then each rung a Sunday a week on
    # (rung 4 adds its Wednesday at the gym), the epilogue the Sunday after the show. vn_clock.day
    # counts real days, so the weekday shown is the true one.
    GL_WD = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    def gl_weekday_name():
        return GL_WD[(3 + vn_clock.day - 1) % 7]    # day 1 is a Wednesday

    def gl_to_weekday(wd, h=8):
        """Minutes from now to the next weekday wd (0 Sunday) at hour h, at least a day on."""
        cur = (3 + vn_clock.day - 1) % 7
        days = (wd - cur) % 7 or 7
        return days * 24 * 60 + (h - vn_clock.hour) * 60 - vn_clock.minute

    vn_weekdays["glutes"] = gl_weekday_name

    vn_sprite_image("gl_pc", ("cheerful", "proud", "protesting", "flushed", "asking"), gl_pc_file, who="pc")
    vn_sprite_image("gl_garrett", ("dry", "coaching", "satisfied"), lambda f: GL + "garrett-" + f + ".png")
    vn_sprite_image("gl_mack", ("grin", "working"), lambda f: GL + "mack-" + f + ".png")
    vn_sprite_image("gl_kendra", ("warm", "coaching"), lambda f: GL + "kendra-" + f + ".png")

    for _f in renpy.list_files():
        if _f.startswith(GL) and _f.endswith(".jpg"):
            _n = _f[len(GL):-4]
            vn_register_bg("gl_" + _n.replace("-", "_"), _f)
            vn_register_cg("gl_" + _n.replace("-", "_"), _f)

    vn_register_art_sets("glutes", [("", "Vanripper"), ("abarus", "Abarus")])

    vn_register_route("glutes", "I Never Read the Label on My Sunday Shot, and My Coach Says My Glutes Are Finally Responding",
        "You're a gym regular on a prescription you've injected every Sunday for years, and this is the first Sunday of your first prep. Your roommate Garrett writes the program, takes the check-in photos and picks up the mail. The pharmacy box sits on the bathroom shelf, label out. You've never read it. Why would you? Everything's responding beautifully, and every bit of it is just prep.",
        GL + "cover.jpg", "glutes_start")

    achievement.register("That'll Respond")

default gl = VNState(body=0, fit="gym")
default gl_enc = VNState(partner_came=True, pc_orgasms=0)
default gl_pc_name = "Brady"

define gl_you = VNChar("[gl_pc_name]", who="pc", plate="#b0662e")
define gl_garrett = VNChar("Garrett", who="gl_garrett", plate="#3f5f6f")
define gl_mack = VNChar("Mack", who="gl_mack", plate="#c27a3a")
define gl_kendra = VNChar("Kendra", who="gl_kendra", plate="#b0507f")
define gl_desk = VNChar("The registration table", who="desk", plate="#6b6b78")
define gl_other = VNChar("Somebody", who="other", plate="#6b6b78")

## THE BOX on the shelf (glutes_shot): the label in small caps, legible; you never look.
screen gl_box(label):
    zorder 60
    frame:
        xalign 0.5 ypos 80 xsize 560
        padding (28, 20)
        background Frame(Solid("#f2f2f0f2"), 0, 0)
        vbox:
            spacing 6
            text "{size=-4}PHARMACY{/size}" size 22 color "#6a6a6a"
            text "{b}%s{/b}" % label size 26 color "#1f2a44"

## THE CHECK-IN CARD (glutes_card): the fixed format, in Garrett's square capitals.
screen gl_card(n):
    zorder 60
    $ c = GL_CARD[max(1, min(6, n))]
    frame:
        xalign 0.5 ypos 60 xsize 760
        padding (30, 22)
        background Frame(Solid("#fbfaf4f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}CHECK-IN — %s{/b}" % c["stage"] size 26 color "#1a1a1a"
            text "class: %s  {size=-4}{i}(%s){/i}{/size}" % (c["cls"], c["note"]) size 22 color "#222222"
            text "fit: %s" % c["fit"] size 22 color "#222222"
            text "%s: %s" % (c["row"], c["chest"]) size 22 color "#222222"
            text "notes: %s" % c["notes"] size 22 color "#222222"
            text "photos: front relaxed / rear relaxed / side chest" size 22 color "#222222"

## THE ROSTER at registration: the division and your surname.
screen gl_roster():
    zorder 60
    frame:
        xalign 0.5 ypos 70 xsize 640
        padding (28, 20)
        background Frame(Solid("#f4f4f4f2"), 0, 0)
        vbox:
            spacing 8
            text "{b}ROSTER{/b}" size 26 color "#1a1a1a"
            text "WELLNESS · LOWRY" size 24 color "#7a2a5a"

## THE FOLDER (rung 5): every check-in's three poses, start to finish, the same corner and lamp.
screen gl_folder():
    zorder 60
    frame:
        xalign 0.5 ypos 40 xsize 1500
        padding (20, 16)
        background Frame(Solid("#141414ee"), 0, 0)
        vbox:
            spacing 10
            text "{b}CHECK-INS{/b}" size 24 color "#f3c969"
            grid 3 5:
                spacing 8
                for _r in range(1, 6):
                    for _p in ("front", "rear", "side"):
                        add Transform(vn_art_file(GL + "checkin-%d-%s.jpg" % (_r, _p)) if renpy.loadable(GL + "checkin-%d-%s.jpg" % (_r, _p)) else Solid("#333333"), xysize=(150, 104))

label glutes_start:
    $ gl = VNState(body=0, fit="gym")
    $ gl_enc = VNState(partner_came=True, pc_orgasms=0)
    $ vn_clock = VNState(day=1, hour=9, minute=0)
    $ vn_route = "glutes"
    $ gl_pc_name = "Brady"
    if not renpy.session.get("vn_picks"):
        $ gl_pc_name = renpy.input("Your name? (Brady, unless you'd like another. The card always says LOWRY.)", default="Brady", length=20).strip() or "Brady"
    jump gl_opening

label gl_route_return:
    $ persistent.catalog_done = (persistent.catalog_done or set()) | {"glutes"}
    $ vn_route = None
    hide screen gl_box
    hide screen gl_card
    hide screen gl_roster
    hide screen gl_folder
    window hide
    scene black onlayer bgl
    $ renpy.scene(layer="master")
    $ renpy.scene(layer="cgl")
    with Dissolve(0.8)
    centered "{size=+10}{color=#f3c969}That'll Respond{/color}{/size}\n\n{i}The end.{/i}"
    jump start
