## A trace of what the screen shows, line by line, for the tests (tools/check.py): set VN_TRACE to
## a file path and every line of dialogue writes one JSON row (the label, the text, the background,
## the CG, the PC sprite file, the cast sprite, the outfit and the clock). Off without VN_TRACE.

init 100 python:
    import os as _vn_os
    import json as _vn_json

    _vn_trace_path = _vn_os.environ.get("VN_TRACE")
    # route id -> fn() returning (PC sprite file, "who face" of the cast sprite, outfit set);
    # routes register theirs at init 110 or later
    vn_trace_routes = {}

    def _vn_trace_label(name, abnormal):
        if not name.startswith("_"):
            store._vn_label = name

    # VN_SHOTS=<dir>: a screenshot of the screen while a line holding one of VN_SHOT_AT's
    # "|"-separated snippets is up. Taken as the NEXT line begins, when that line is drawn.
    _vn_shot_dir = _vn_os.environ.get("VN_SHOTS")
    _vn_shot_at = [x for x in _vn_os.environ.get("VN_SHOT_AT", "").split("|") if x]
    _vn_shot_next = [None]
    _vn_shot_n = [0]

    def _vn_shoot(what):
        if _vn_shot_next[0]:
            _vn_shot_n[0] += 1
            renpy.screenshot(_vn_os.path.join(_vn_shot_dir, "%02d-%s.png" % (_vn_shot_n[0], _vn_shot_next[0])))
            _vn_shot_next[0] = None
        for snip in _vn_shot_at:
            if what and snip in what:
                _vn_shot_next[0] = "".join(c if c.isalnum() else "_" for c in snip)[:40]
                _vn_shot_at.remove(snip)
                break

    def _vn_trace_cb(event, interact=True, what=None, **kw):
        if event != "begin":
            return
        if _vn_shot_dir and interact:
            _vn_shoot(what)
        def attrs(tag, layer=None):
            if not renpy.showing(tag, layer=layer):
                return None
            return " ".join(renpy.get_attributes(tag, layer=layer) or ())
        # the route's own sprites: (PC sprite file, "who face" of the cast sprite, outfit set), from
        # its vn_trace_routes entry; Red Lightning's are the fallback
        tr = vn_trace_routes.get(store.vn_route)
        if tr:
            pc, cast, fit = tr()
        else:
            pc = rl_pc_file(rl_face_now()).rsplit("/", 1)[-1] if renpy.showing("rory") else None
            cast = ("miles " + attrs("miles")) if renpy.showing("miles") else None
            fit = rl.fit
        row = {
            "label": getattr(store, "_vn_label", None),
            "caption": not interact,
            "what": what,
            "bg": attrs("bg", "bgl"),
            "cg": attrs("cg", "cgl"),
            "pc": pc,
            "cast": cast,
            "talk": store.vn_talk,
            "fit": fit,
            "day": vn_clock.day,
            "hour": vn_clock.hour,
        }
        with open(_vn_trace_path, "a") as f:
            f.write(_vn_json.dumps(row) + "\n")

    if _vn_trace_path:
        config.all_character_callbacks.append(_vn_trace_cb)
        config.label_callbacks.append(_vn_trace_label)
        # headless runs (SDL's dummy driver) draw with the software renderer: skip the
        # "your graphics are slow" check, which would stop the test on a dialog
        config.performance_test = False

## A test walk's choices, in order (game/tests/*.rpy sets renpy.session["vn_picks"]): each menu takes
## the first item whose caption holds the next snippet. Empty outside tests.
init python:
    def vn_test_pick(items):
        plan = renpy.session.get("vn_picks")
        if not plan or renpy.predicting():
            return None
        for i, it in enumerate(items):
            if plan[0] in it.caption:
                return i
        raise Exception("test plan: no choice holds %r (have %r)" % (plan[0], [it.caption for it in items]))

    def vn_test_route_pick():
        """The route select's card for the plan's next snippet (its label), or None."""
        plan = renpy.session.get("vn_picks")
        if not plan or renpy.predicting():
            return None
        for r in vn_routes:
            if plan[0] in r["title"]:
                return r["label"]
        raise Exception("test plan: no route card holds %r" % (plan[0],))

    def vn_test_picked():
        plan = renpy.session.get("vn_picks")
        if plan:
            plan.pop(0)
