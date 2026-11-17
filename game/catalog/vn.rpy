## The catalog's VN layer, for every route (the Ren'Py pilot, 2026-11-11).
##
## The same screen as the DoL catalog's framework/vn-screen.js, on Ren'Py's own machinery:
##   - a background full-bleed (layer bgl), or a CG over it (layer cgl): the CG sits wholly above
##     the textbox (owner, 2026-11-10: "being able to better see the art"), a blurred copy of
##     itself filling the sides
##   - the PC sprite left, up to two cast sprites, right and centre (master layer; the cast stage
##     below); the speaker lit, the others dimmed
##   - the textbox: two lines tall, growing for a third (owner, 2026-11-12: smaller box, more
##     picture; the CG area is 832, so a landscape frame draws at native size); the name plate a
##     tab on its top edge in the speaker's colour; one beat per click; SFX lines big and centred;
##     thoughts in italic; growth beats in pink (the route's own markup)
##   - the PC's face as a portrait tab beside the box while a CG hides the sprites (owner,
##     2026-11-11; a tab rising above the box since 2026-11-12, so it keeps its size)
##   - the quick menu fades out while the mouse rests (screens.rpy, 2026-11-12)
##   - a picture missing from this checkout draws as a dark card (vn_pic; tools/slim_worktree.py)
##   - shake (impacts, yells) and a white flash (climaxes): `with vnfx("shake")` on the line;
##     off with the player's "Screen shake and flash" preference, or Ren'Py's Transitions: None
##   - a small HUD: the day and the time (vn_clock)
## Ren'Py supplies what the DoL screen built by hand: rollback, history, skip, auto, save slots.
##
## A route registers its sprites with vn_sprite_image() and its pictures with vn_bg()/vn_cg(), and
## starts every passage's label with vn_enter() (its stage row: background, faces, cast, CG).

init -100 python:
    renpy.add_layer("bgl", below="master")
    renpy.add_layer("cgl", above="master")

init -50 python:
    import math

    VN_W, VN_H = 1920, 1080
    VN_BOX_MIN = 130                    # the box: two lines of text (33 px + 8 spacing) with its padding; a
                                        # third line grows it (owner, 2026-11-12: a smaller box, more picture)
    VN_BOX_H = VN_BOX_MIN               # the old name, for a route that read it
    VN_BOX_GAP = 22                     # 2vh off the bottom
    VN_CG_H = 832                       # the CG's area: a 1216x832 landscape frame draws at native size; the box,
                                        # its plate tab and a third line all fit below (1080 - 22 - 171 - 32 = 855)
    VN_PLATE_OVER = 12                  # the name plate's tab overlaps the box's top edge by this
    VN_SPRITE_H = 994                   # 92vh
    VN_SIDE = 77                        # 4vw in from the edge
    VN_FACE = 216                       # the face portrait in the box (owner, 2026-11-11: bigger)

    class VNState(object):
        """A route's state: attributes default to None, so a flag never set reads false."""
        def __init__(self, **kw):
            self.__dict__.update(kw)

        def __getattr__(self, k):
            if k.startswith("__"):
                raise AttributeError(k)
            return None

    # ---- art sets (hypno.js artSets: one route drawn in two styles, a toggle per save) -----
    vn_art_sets = {}

    def vn_register_art_sets(route, sets):
        """sets: [(id, name)], the default first with id "" (its pictures in art/<route>/; a set's
        in art/<route>.<id>/, picked picture by picture where it has one; not "@", which Ren'Py
        reads as an image modifier)."""
        vn_art_sets[route] = list(sets)

    _vn_loadable = {}

    def vn_art_file(path):
        """The picture to show for `path` (art/<route>/<file>, or art/<route>/scenes/<file>): the
        chosen set's file of the same name if it has one, else the default's."""
        parts = path.split("/")
        if len(parts) < 3 or parts[0] != "art":
            return path
        route = parts[1]
        set_id = (store.vn_art or {}).get(route) if route in vn_art_sets else None
        if not set_id:
            return path
        alt = "art/%s.%s/%s" % (route, set_id, parts[-1])
        if alt not in _vn_loadable:
            _vn_loadable[alt] = renpy.loadable(alt)
        return alt if _vn_loadable[alt] else path

    def vn_art_cycle(route):
        sets = vn_art_sets.get(route) or [("", "")]
        ids = [i for i, _ in sets]
        cur = (store.vn_art or {}).get(route, "")
        nxt = ids[(ids.index(cur) + 1) % len(ids)] if cur in ids else ids[0]
        store.vn_art = dict(store.vn_art or {}, **{route: nxt})
        renpy.restart_interaction()

    def vn_art_name(route):
        cur = (store.vn_art or {}).get(route, "")
        return dict(vn_art_sets.get(route, [])).get(cur, "")

    def vn_face_crop(crops, path):
        """A sprite file's head crop: a set's own sprite has its own ("<set>:<stem>")."""
        stem = path.rsplit("/", 1)[-1][:-4]
        folder = path.split("/")[1] if path.count("/") >= 2 else ""
        key = (folder.split(".", 1)[1] + ":" + stem) if "." in folder else stem
        return crops.get(key) or crops.get(stem) or (0, 0, 200, 200)

    # ---- pictures -------------------------------------------------------------------------
    _vn_present = set()

    def vn_pic(path):
        """`path` when the file is in this checkout, else the dark "missing" card. A slimmed
        worktree (tools/slim_worktree.py) carries only its own route's art, and the persistent
        file is shared, so the gallery can list another route's pictures as seen."""
        if not isinstance(path, str) or path in _vn_present:
            return path
        if renpy.loadable(path):
            _vn_present.add(path)
            return path
        return "vn_missing"

    def vn_bg(path):
        return Transform(vn_pic(path), fit="cover", xysize=(VN_W, VN_H))

    def vn_cg(path):
        path = vn_pic(path)
        return Fixed(
            Transform(path, fit="cover", xysize=(VN_W, VN_H), blur=42, matrixcolor=TintMatrix("#3a3a44")),
            Transform(path, fit="contain", xysize=(VN_W, VN_CG_H), xalign=0.5, yalign=0.0),
            xysize=(VN_W, VN_H))

    def vn_figure(path):
        """A sprite at stage height with a soft drop shadow (the CSS drop-shadow)."""
        img = Transform(vn_pic(path), fit="contain", ysize=VN_SPRITE_H)
        shadow = Transform(img, matrixcolor=TintMatrix("#000000") * OpacityMatrix(0.55), blur=16)
        return Fixed(shadow, img, fit_first=True)

    VN_DIM = TintMatrix("#b8b8b8") * SaturationMatrix(0.85)

    def vn_dimmed(who):
        """The other sprites step back while someone with a sprite speaks: the PC's while a cast sprite
        talks, a cast sprite's while the PC or another cast sprite talks (owner, 2026-11-17: two cast
        sprites side by side, the one not talking dimmed)."""
        talk = store.vn_talk
        if talk is None or talk == who:
            return False
        if who == "pc":
            return renpy.showing(talk)
        return talk == "pc" or (talk in vn_sprite_resolvers and renpy.showing(talk))

    def _vn_sprite(st, at, resolve, who, face):
        d = vn_figure(vn_art_file(resolve(face)))
        if vn_dimmed(who):
            d = Transform(d, matrixcolor=VN_DIM)
        return d, None

    vn_sprite_resolvers = {}   # sprite tag -> resolve(face), for a cast speaker's face in the box (vn_cast_face)

    def vn_sprite_image(tag, faces, resolve, who=None):
        """Register `tag face` for each face; resolve(face) gives the file at show time, so a
        sprite follows the route's rung and outfit without a new show statement."""
        vn_sprite_resolvers[tag] = resolve
        for f in faces:
            renpy.image((tag, f), DynamicDisplayable(_vn_sprite, resolve, who or tag, f))

    # ---- the cast stage: two cast sprites side by side ------------------------------------
    # The owner (2026-11-17, via Supervisor): routes show each NPC `at vn_cast_slot` in turn and never hide the one
    # before, so they stacked on one spot. Now the two most recent cast sprites stand side by side: the first keeps the
    # right spot (vn_cast_slot), a newcomer takes the centre (vn_cast_mid), and nobody moves while they stay. A third
    # pushes out the one least recently shown or heard (the current speaker and the last other stay); it's parked
    # (vn_cast_park, invisible) rather than hidden, so it still counts as on stage (the speaker check, vn_face,
    # `show <tag> <face>`, the face tab over a CG) and comes back when it speaks or is shown again, in the spot the
    # one it replaces leaves. When one is hidden, the most recent parked one comes back. No route changes: the show
    # and hide statements go through config.show/config.hide below, and a renpy.show() at vn_cast_slot (wolfpack) is
    # sorted out when the next line starts.
    # Measured 2026-11-17 on the 11 routes that stack cast (every sprite pair at stage height): with the centre spot at
    # the screen's middle no face is ever crossed; 1% of pairs touch at an elbow or hair, by 18 px at most.
    # State lives in the store and the scene lists, so rollback and saves follow it.

    def _vn_cast_slots():
        return {"r": vn_cast_slot, "m": vn_cast_mid, "p": vn_cast_park}

    def vn_cast_slot_of(tag):
        """'r', 'm' or 'p' for a cast sprite on the master layer, else None (not showing, or not in a cast slot)."""
        at = renpy.get_at_list(tag, layer="master")
        if at is None:
            return None
        for s, t in _vn_cast_slots().items():
            if any(x is t for x in at):
                return s
        # a face change without `at` keeps the running transform (and empties the at list); after a load the list holds
        # copies: either way the spot last given
        return store.vn_cast_slots.get(tag)

    def _vn_cast_note(tag, slot):
        if store.vn_cast_slots.get(tag) != slot:
            d = dict(store.vn_cast_slots)
            d[tag] = slot
            store.vn_cast_slots = d

    def _vn_cast_bump(tag):
        store.vn_cast_order = [t for t in store.vn_cast_order if t != tag] + [tag]

    def _vn_cast_place(tag, slot):
        """Re-show a cast sprite in `slot`, with its face and any other transforms it had."""
        attrs = tuple(renpy.get_attributes(tag, layer="master") or ())
        slots = list(_vn_cast_slots().values())
        at = renpy.get_at_list(tag, layer="master") or []
        if any(x is t for x in at for t in slots):
            new = [_vn_cast_slots()[slot] if any(x is t for t in slots) else x for x in at]
        else:
            new = [_vn_cast_slots()[slot]]          # re-shown without `at`, or loaded from a save
        renpy.show((tag,) + attrs, at_list=new, layer="master")
        _vn_cast_note(tag, slot)

    def vn_cast_arrange(incoming=None):
        """Put the two most recent cast sprites in the right and centre spots and park the rest; `incoming` is a sprite
        about to be shown (the caller shows it). Returns incoming's spot."""
        showing = list(renpy.get_showing_tags("master", sort=True))     # back to front: shown first, first
        cur = {}
        for t in showing:
            if t in vn_sprite_resolvers:
                s = vn_cast_slot_of(t)
                if s is not None:
                    cur[t] = s
        if incoming is not None:
            cur[incoming] = cur.get(incoming) if incoming in showing else None
        order = [t for t in store.vn_cast_order if t in cur]
        order = [t for t in cur if t not in order] + order      # never bumped (old saves): oldest
        vis, parked = order[-2:], order[:-2]
        spots = {}
        for t in vis:
            if cur[t] in ("r", "m") and cur[t] not in spots.values():
                spots[t] = cur[t]
        for t in vis:
            if t not in spots:
                spots[t] = "r" if "r" not in spots.values() else "m"
        for t in parked:
            spots[t] = "p"
        for t, s in spots.items():
            if t != incoming and (s != cur[t] or store.vn_cast_slots.get(t) != s):
                if s != cur[t]:
                    _vn_cast_place(t, s)
                else:
                    _vn_cast_note(t, s)
        return spots.get(incoming)

    def vn_cast_show(name, at_list, layer=None, show=None, **kw):
        """Show a cast sprite asked for at vn_cast_slot in its spot on the cast stage."""
        nm = tuple(name.split()) if isinstance(name, str) else tuple(name)
        tag = kw.get("tag") or nm[0]
        _vn_cast_bump(tag)
        s = vn_cast_arrange(incoming=tag)
        at_list = [_vn_cast_slots()[s] if x is vn_cast_slot else x for x in at_list]
        (show or renpy.show)(name, at_list=at_list, layer=layer, **kw)
        _vn_cast_note(tag, s)

    def _vn_cast_asked(at_list, layer, what):
        return what is None and layer in (None, "master") and any(x is vn_cast_slot for x in (at_list or ()))

    _vn_show0 = config.show
    _vn_hide0 = config.hide

    def _vn_show(name, at_list=[], layer=None, what=None, **kw):
        nm = tuple(name.split()) if isinstance(name, str) else tuple(name)
        if nm[0] == "cg" and what is None and not renpy.has_image(nm, exact=True):
            # `show cg <key>` for a key with no picture landed: clear the old CG so the room
            # shows, never Ren'Py's "Image not found" text (QA camellia 2f90ff35)
            _vn_hide0("cg", layer)
            return
        if _vn_cast_asked(at_list, layer, what) and (kw.get("tag") or nm[0]) in vn_sprite_resolvers:
            return vn_cast_show(name, list(at_list), layer=layer, show=_vn_show0, what=what, **kw)
        return _vn_show0(name, at_list=at_list, layer=layer, what=what, **kw)

    def _vn_hide(name, layer=None):
        _vn_hide0(name, layer)
        tag = (tuple(name.split()) if isinstance(name, str) else tuple(name))[0]
        if layer in (None, "master") and tag in store.vn_cast_slots:
            vn_cast_arrange()

    config.show = _vn_show
    config.hide = _vn_hide

    # ---- the stage ------------------------------------------------------------------------
    def vn_enter(bg=None, pc=None, pc_tag=None, cast=(), cg=None, trans=True):
        """A passage's stage row, as framework/vn-screen.js resolves it: the background (or None),
        the PC's face on pc_tag, the cast (a list of (tag, face)), and the CG (or None)."""
        store.vn_talk = None
        # a CG key with no picture landed ("no picture" is a valid pick) shows the room, never
        # Ren'Py's "Image not found" text (QA camellia 2f90ff35)
        if cg and not renpy.has_image(("cg",) + tuple(cg.split()), exact=True):
            cg = None
        # a new place or picture dissolves in with the box out of the way (no empty box over the
        # old frame); the same place carries straight on, as the DoL screen does
        def _now(tag, layer):
            if not renpy.showing(tag, layer=layer):
                return None
            return " ".join(renpy.get_attributes(tag, layer=layer) or ())
        changed = (_now("bg", "bgl") != bg) or (_now("cg", "cgl") != cg)
        renpy.scene(layer="cgl")
        renpy.scene(layer="master")
        store.vn_cast_order = []
        store.vn_cast_slots = {}
        if bg:
            renpy.show("bg " + bg, layer="bgl")
        else:
            renpy.scene(layer="bgl")
        if pc and pc_tag:
            renpy.show(pc_tag + " " + pc, at_list=[vn_pc_slot])
        for tag, face in cast:
            vn_cast_show(tag + " " + face, [vn_cast_slot])
        if cg:
            renpy.show("cg " + cg, layer="cgl")
        if trans and changed and not renpy.is_skipping():
            _window_hide(None, auto=True)
            renpy.with_statement(Dissolve(0.25))

    # ---- CGs and the gallery ------------------------------------------------------------
    vn_cg_files = {}
    vn_gallery = {}

    def _vn_cg_dd(st, at, path):
        return vn_cg(vn_art_file(path)), None

    def _vn_bg_dd(st, at, path):
        return vn_bg(vn_art_file(path)), None

    def vn_register_cg(name, path):
        """`cg <name>`: the picture fitted above the box (vn_cg), from the chosen art set; its
        file, for the gallery."""
        vn_cg_files[name] = path
        renpy.image(("cg", name), DynamicDisplayable(_vn_cg_dd, path))

    def vn_register_bg(name, path):
        """`bg <name>`: the background full-bleed (vn_bg), from the chosen art set."""
        renpy.image(("bg", name), DynamicDisplayable(_vn_bg_dd, path))

    def vn_register_gallery(route, names):
        """A route's pictures in story order (its gallery.rpy, tools/gallery.py)."""
        vn_gallery[route] = [n for n in names if n in vn_cg_files]

    def vn_thumb(name, hover=False):
        """A gallery tile: the picture fitted inside 256x175 on a dark ground (a portrait one
        letterboxed, never cropped or spilling over)."""
        pic = Transform(vn_pic(vn_art_file(vn_cg_files[name])), fit="contain", xysize=(256, 175), xalign=0.5, yalign=0.5)
        if hover:
            pic = Transform(pic, matrixcolor=BrightnessMatrix(0.12))
        return Fixed(Solid("#14141b"), pic, xysize=(256, 175))

    def vn_cg_seen(name):
        return renpy.seen_image(("cg", name))

    def vn_cg_on():
        return renpy.showing("cg", layer="cgl")

    def vn_face(tag, face):
        """@face: a face change for a sprite that's on stage; one that isn't stays off."""
        if renpy.showing(tag):
            renpy.show(tag + " " + face)

    # ---- effects --------------------------------------------------------------------------
    vn_shake_t = Move((7, 3), (-6, -4), .06, bounce=True, repeat=True, delay=.28)
    vn_flash_t = Fade(.03, 0.0, .55, color="#fff")

    def vnfx(*kinds):
        """The transition for a line's shake/flash cue, or None when the player turned them off."""
        if persistent.vn_fx_off:
            return None
        if "flash" in kinds and "shake" in kinds:
            return MultipleTransition([False, vn_flash_t, True, vn_shake_t, True])
        if "flash" in kinds:
            return vn_flash_t
        if "shake" in kinds:
            return vn_shake_t
        return None

    # ---- the clock (the HUD and a route's "late") -----------------------------------------
    def vn_set_time(h, m=0):
        store.vn_clock.hour, store.vn_clock.minute = h, m

    def vn_pass(minutes):
        c = store.vn_clock
        t = c.hour * 60 + c.minute + int(minutes)
        c.day += t // (24 * 60)
        t %= 24 * 60
        c.hour, c.minute = t // 60, t % 60

    def vn_until(h):
        """Pass time to hour h today, or tomorrow if it's already past (redlightning_until)."""
        c = store.vn_clock
        if c.hour < h:
            vn_pass((h - c.hour) * 60 - c.minute)
        elif c.hour > h or c.minute > 0:
            vn_pass(((24 - c.hour) + h) * 60 - c.minute)

    def vn_sleep(wake=7):
        c = store.vn_clock
        c.day += 1
        c.hour, c.minute = wake, 0

    def vn_time_str():
        c = store.vn_clock
        return "%d:%02d" % (c.hour, c.minute)

    # A route that keeps a calendar registers its weekday (route -> a function returning "Tue"),
    # and the HUD shows it before the day (2026-11-12, hypno: the corner has to agree with the
    # story's Mondays and Fridays). A route that doesn't keeps plain "Day N".
    vn_weekdays = {}

    def vn_day_str():
        f = vn_weekdays.get(store.vn_route)
        day = "Day %d" % store.vn_clock.day
        return (f() + " · " + day) if f else day

    # ---- characters -----------------------------------------------------------------------
    def _vn_line_reset(event, interact=True, **kw):
        """Every say line starts with no speaker; a VNChar's own callback (which runs after this one) names it.
        So narration never inherits the last speaker's face (vn_talk stays as it was: it drives the dimming)."""
        if event == "begin":
            store.vn_line_who = None

    config.all_character_callbacks.insert(0, _vn_line_reset)

    def _vn_talk(event, interact=True, who=None, **kw):
        if event == "begin":
            store.vn_talk = who
            store.vn_line_who = who
            # a cast speaker steps forward: back from parked into the spot of the one least recently shown or heard
            if who and who != "pc" and who in vn_sprite_resolvers and vn_cast_slot_of(who) is not None:
                _vn_cast_bump(who)
                vn_cast_arrange()
            tp_ = getattr(store, "_vn_trace_path", None)
            # a cast speaker over a CG whose face can't be cut (no head crop: faces.rpy not regenerated) shows no tab
            if tp_ and who and who != "pc" and who in vn_sprite_resolvers and renpy.showing(who) and vn_cg_on() \
                    and vn_cast_face(who) is None:
                import json as _j
                with open(tp_, "a") as _f:
                    _f.write(_j.dumps({"face_miss": who, "label": getattr(store, "_vn_label", None),
                                       "what": (kw.get("what") or "")[:80]}) + "\n")
            # the speaker's sprite must be in the box (the owner, 2026-11-15): in a test walk (vntrace sets
            # _vn_trace_path) a cast speaker whose sprite isn't showing writes a speaker_miss row to the trace, which
            # runs/_c9/trace_speaker.py turns into a failure. The global trace callback runs before this one, so the
            # check lives here, where `who` is known.
            tp = getattr(store, "_vn_trace_path", None)
            # only a speaker with a registered sprite can be missing it (vote's "screen" or "man" voices have none)
            if tp and who and who != "pc" and who in vn_sprite_resolvers and not renpy.showing(who):
                import json as _j
                with open(tp, "a") as _f:
                    _f.write(_j.dumps({"speaker_miss": who, "label": getattr(store, "_vn_label", None),
                                       "what": (kw.get("what") or "")[:80]}) + "\n")

    def VNChar(name, who=None, plate="#6b6b78", **kw):
        """A speaker: a name plate in `plate`'s colour; `who` is the sprite tag that lights up."""
        kw.setdefault("what_style", "vn_what")
        kw.setdefault("who_style", "vn_plate_text")
        kw.setdefault("window_style", "vn_window")
        return Character(name, callback=renpy.curry(_vn_talk)(who=who), show_plate=plate, **kw)

    # ---- the face portrait: each route registers a resolver for its PC's current face -----
    vn_portraits = {}

    def vn_face_portrait():
        f = vn_portraits.get(store.vn_route)
        return f() if f else Null()

    def vn_face_ready():
        return store.vn_route in vn_portraits

    def vn_cast_face(tag):
        """A cast speaker's face for the box's tab while a CG is up (owner, 2026-11-15: the person talking has the right
        picture in the box): the head crop (tools/sync_art.py's <route>_face_crops) of the sprite they're showing.
        None when their sprite isn't up or the file has no crop: then no tab, never another character's face."""
        resolve = vn_sprite_resolvers.get(tag)
        attrs = renpy.get_attributes(tag) if resolve else None
        if not attrs:
            return None
        path = vn_art_file(resolve(attrs[0]))
        crops = getattr(store, (store.vn_route or "") + "_face_crops", None) or {}
        stem = path.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        folder = path.split("/")[1] if path.count("/") >= 2 else ""
        key = (folder.split(".", 1)[1] + ":" + stem) if "." in folder else stem
        c = crops.get(key) or crops.get(stem)
        if not c:
            return None
        return Transform(Crop(tuple(c), vn_pic(path)), xysize=(VN_FACE, VN_FACE))

    def vn_line_face():
        """The face for the box's tab on this line: a cast speaker's own; the PC's for the PC, thoughts and narration;
        None (no tab) for a speaker without a sprite."""
        who = store.vn_line_who
        if who and who != "pc":
            return vn_cast_face(who) if who in vn_sprite_resolvers else None
        f = vn_portraits.get(store.vn_route)
        return f() if f else None

    # ---- the route select: every route registers its card in its own route.rpy -----------
    vn_routes = []

    def vn_register_route(id, title, blurb, cover, label):
        """A card on the route select: the cover, the title, the blurb; Play jumps to `label`. Its tags and the day it
        was built come from game/catalog/tags.rpy (a route with no line there has no tags and sorts last by Newest)."""
        built, tags = vn_route_tags.get(id, ("", ""))
        vn_routes.append(dict(id=id, title=title, blurb=blurb, cover=cover, label=label,
                              tags=frozenset(vn_tag_split(tags)), built=built))

    # ---- the route select's tag filter (owner, 2026-11-17: "filter by tag and each story gets tags", "have a and
    # and or option"; 4:08 pm: nhentai's tags, a flat chip cloud by count; 4:13 pm: its consent tags are fine). The
    # picks, the match mode and the sort are kept in persistent. --------------------------------------------------
    VN_ROUTE_PAGE = 20      # cards drawn at once; "Show more" adds as many again (each card loads a cover)
    VN_TAG_TOP = 20         # chips shown before "More tags" (picked ones always show)
    VN_SORTS = [("new", _("Newest")), ("az", _("A–Z")), ("todo", _("Not finished"))]
    vn_route_yadj = ui.adjustment()     # the card list's scroll, back to the top when the filter changes

    def vn_tag_pick():
        """The picked tags (any no longer in tags.rpy's vocabulary dropped)."""
        return frozenset(t for t in (persistent.vn_tag_pick or ()) if t in VN_TAG_LABEL)

    def vn_tag_mode():
        return "any" if persistent.vn_tag_mode == "any" else "all"

    def vn_route_sort():
        return persistent.vn_route_sort if persistent.vn_route_sort in ("new", "az", "todo") else "new"

    def _vn_title_key(r):
        """A-Z ignores a leading The, A or An."""
        t = r["title"].lower()
        for art in ("the ", "an ", "a "):
            if t.startswith(art):
                return t[len(art):]
        return t

    def vn_routes_shown():
        """The cards the filter leaves, in the chosen order. All: a story has every picked tag; Any: at least one."""
        pick, mode, sort = vn_tag_pick(), vn_tag_mode(), vn_route_sort()
        if not pick:
            rs = list(vn_routes)
        elif mode == "all":
            rs = [r for r in vn_routes if pick <= r["tags"]]
        else:
            rs = [r for r in vn_routes if pick & r["tags"]]
        rs.sort(key=_vn_title_key)
        if sort != "az":
            rs.sort(key=lambda r: r["built"], reverse=True)     # stable: a day's routes stay A-Z
        if sort == "todo":
            done = persistent.catalog_done or ()
            rs.sort(key=lambda r: r["id"] in done)
        return rs

    def vn_tag_count(tag, shown):
        """The number on a chip. All: the stories in the list that have it (what picking it leaves). Any: every story
        that has it (what picking it adds)."""
        base = shown if vn_tag_mode() == "all" else vn_routes
        return sum(1 for r in base if tag in r["tags"])

    def vn_tag_cloud():
        """nhentai's tags that some story has, the most used first (ties A-Z): the filter's chips."""
        n = dict((t, 0) for t in VN_TAGS)
        for r in vn_routes:
            for t in r["tags"]:
                if t in n:
                    n[t] += 1
        return sorted((t for t in VN_TAGS if n[t]), key=lambda t: (-n[t], t))

    def vn_story_row():
        """The Story row's tags that some story has, in their own order."""
        return [(t, lab) for t, lab in VN_STORY_TAGS if any(t in r["tags"] for r in vn_routes)]

    def vn_tags_line(r):
        ## the dot holds to the tag before it (a no-break space), so a wrapped line never starts with one
        return "\u00a0·  ".join(VN_TAG_LABEL[t] for t in VN_TAG_ORDER if t in r["tags"])

    def vn_route_reset():
        """Back to the first page and the top of the list (the filter changed, or the screen opened)."""
        store.vn_route_limit = VN_ROUTE_PAGE
        vn_route_yadj.change(0)

    def vn_tag_toggle(tag):
        persistent.vn_tag_pick = set(vn_tag_pick() ^ {tag})
        vn_route_reset()

    def vn_tag_clear():
        persistent.vn_tag_pick = set()
        vn_route_reset()

    def vn_tag_set_mode(mode):
        persistent.vn_tag_mode = mode
        vn_route_reset()

    def vn_route_set_sort(sort):
        persistent.vn_route_sort = sort
        vn_route_reset()

    def vn_route_sort_cycle():
        keys = [k for k, lab in VN_SORTS]
        vn_route_set_sort(keys[(keys.index(vn_route_sort()) + 1) % len(keys)])

    def vn_route_more():
        store.vn_route_limit += VN_ROUTE_PAGE

    def _vn_main_bg(st, at):
        """The main menu's backdrop: the registered routes' covers in a row, dimmed, on the
        catalog's dark ground (grows as routes are added)."""
        covers = [Transform(vn_pic(r["cover"]), fit="contain", ysize=640) for r in vn_routes[:6]]
        row = HBox(*covers, spacing=28) if covers else Null()
        return Fixed(Solid("#0b0b10"),
                     Transform(row, xalign=0.72, yalign=0.5, matrixcolor=TintMatrix("#6a6a74") * SaturationMatrix(0.8)),
                     xysize=(VN_W, VN_H)), None

    # ---- feats ----------------------------------------------------------------------------
    def vn_feat(name):
        achievement.grant(name)
        renpy.notify("Feat: " + name)

## The sprite slots. Sprites come and go instantly, as on the DoL screen. (An ease-in on show
## was tried and dropped, 2026-11-11: rollback and every passage's stage re-show the sprites, so
## it replayed on each Back press and blinked at scene boundaries.)
transform vn_pc_slot:
    xanchor 0.0 xpos VN_SIDE yanchor 1.0 ypos VN_H + 22

transform vn_cast_slot:
    xanchor 1.0 xpos VN_W - VN_SIDE yanchor 1.0 ypos VN_H + 22 alpha 1.0

## the cast stage's second spot (a newcomer while the first stays right) and a parked third (vn_cast_arrange). Each
## sets every property, since a re-show carries the old transform's state into the new one.
transform vn_cast_mid:
    xanchor 0.5 xpos VN_W // 2 yanchor 1.0 ypos VN_H + 22 alpha 1.0

transform vn_cast_park:
    xanchor 1.0 xpos VN_W - VN_SIDE yanchor 1.0 ypos VN_H + 22 alpha 0.0

image vn_black = Solid("#000")
image vn_main_bg = DynamicDisplayable(_vn_main_bg)
## a picture this checkout doesn't have (vn_pic): a dark card, so a slimmed worktree never crashes
image vn_missing = Fixed(Solid("#1b1b23"), Text("?", size=120, color="#3a3a46", xalign=0.5, yalign=0.5), xysize=(1216, 832))

default vn_talk = None
default vn_line_who = None   # this line's speaker tag (None for narration); the box's face follows it
default vn_cast_order = []   # cast sprite tags, least recently shown or heard first (the cast stage)
default vn_cast_slots = {}   # cast sprite tag -> the spot last given: "r", "m" or "p" (parked)
default vn_clock = VNState(day=0, hour=12, minute=0)
default vn_route = None
default vn_art = {}
default persistent.vn_fx_off = False
default persistent.vn_tag_pick = set()     # the route select's filter (vn_routes_shown)
default persistent.vn_tag_mode = "all"
default vn_tag_more = False                 # the filter's More tags open
default persistent.vn_route_sort = "new"
default vn_route_limit = VN_ROUTE_PAGE

define narrator = VNChar(None)
define vn_th = VNChar(None, what_italic=True, what_color="#e6e6efd9")
define vn_sfx = VNChar(None, what_style="vn_sfx_what")

## The night (vn.twee's <<route_sleep>>: Route Sleep passes by itself): the box goes, the screen
## goes dark, morning.
label vn_night(wake=7):
    window hide
    show vn_black onlayer cgl with Dissolve(0.6)
    $ vn_sleep(wake)
    pause 0.35
    window auto
    return

## The say window is a transparent holder sized by what's in it: the portrait tab, the name plate's
## tab and the box (screens.rpy, screen say). The box itself is vn_box: two lines by default, a
## third when a beat needs it (owner, 2026-11-12: "smaller text boxes to better see the art").
style vn_window is window:
    xalign 0.5
    xsize VN_W - 116
    ysize None
    yalign 1.0
    yoffset -VN_BOX_GAP
    padding (0, 0, 0, 0)
    background None

style vn_box is default:
    xfill True
    yminimum VN_BOX_MIN
    padding (38, 26, 38, 22)
    background Frame("gui/vn/box.png", 16, 16)

style vn_what is say_dialogue:
    xpos 0
    ypos 0
    xsize None
    xfill True
    size 33
    line_spacing 8
    color "#f2f2f6"
    outlines [(1, "#00000066", 0, 1)]

style vn_sfx_what is vn_what:
    size 58
    bold True
    italic True
    kerning 2
    text_align 0.5
    xalign 0.5
    color "#ff6b8b"
    outlines [(0, "#00000099", 0, 3)]

style vn_sfx_i:
    bold True
    italic True
    color "#ff6b8b"

style vn_plate_frame is default:
    padding (16, 4, 16, 6)

style vn_plate_text is default:
    size 28
    bold True
    color "#ffffff"
    outlines [(0, "#00000073", 0, 1)]

style vn_hud_text is default:
    size 24
    color "#f0f0f4"

## The PC's face beside the box over a CG: the route's portrait displayable (vn_face_portrait). A
## tab standing on the box's bottom edge and rising above it, so it keeps its size (216) while the
## box is shorter than it (2026-11-12).
screen vn_face(face=None):
    fixed:
        xysize (VN_FACE + 8, VN_FACE + 8)
        yalign 1.0
        add (face if face is not None else vn_face_portrait()) xysize (VN_FACE, VN_FACE) xalign 0.5 yalign 0.5
        add "gui/vn/face_frame.png" xysize (VN_FACE + 8, VN_FACE + 8)

## The route select (DoL's New Game cards): the cover left of the title, the blurb, the tags and Play. The tag filter
## (owner, 2026-11-17) sits on the left; on a phone it's a full-screen panel behind a Filter button (vn_tag_panel).
## Twenty cards at a time, since each card loads a cover.
screen vn_route_select():
    add Solid("#0b0b10")
    on "show" action Function(vn_route_reset)
    on "hide" action Hide("vn_tag_panel")
    ## a test walk's plan picks the card by its title (game/catalog/vntrace.rpy); it searches every route, filter or not
    $ _vn_route_pick = vn_test_route_pick()
    if _vn_route_pick is not None:
        timer 0.05 action [Function(vn_test_picked), Return(_vn_route_pick)]
    $ shown = vn_routes_shown()
    frame:
        style "vnf_side"
        xpos 30
        ypos 30
        xsize 500
        ysize 1020
        viewport:
            mousewheel True
            draggable True
            scrollbars "vertical"
            side_spacing 6
            use vn_tag_filter(shown)
    text _("Choose a story") size 52 color "#f2f2f6" xpos 566 ypos 26
    use vn_route_list(shown, (560, 108, 1340, 952), 1300)

## the phone: the cards full width, bigger type, and a top bar with Filter, Sort and the count
screen vn_route_select():
    variant "small"
    add Solid("#0b0b10")
    on "show" action Function(vn_route_reset)
    on "hide" action Hide("vn_tag_panel")
    $ _vn_route_pick = vn_test_route_pick()
    if _vn_route_pick is not None:
        timer 0.05 action [Function(vn_test_picked), Return(_vn_route_pick)]
    $ shown = vn_routes_shown()
    $ _n = len(vn_tag_pick())
    hbox:
        xpos 40
        ypos 22
        spacing 22
        textbutton ((_("Filter · %d on") % _n) if _n else _("Filter")):
            style_prefix "vnf_chip"
            selected (_n > 0)
            action Show("vn_tag_panel")
        textbutton (_("Sort: %s") % dict(VN_SORTS)[vn_route_sort()]):
            style_prefix "vnf_chip"
            action Function(vn_route_sort_cycle)
        text (_("%d of %d") % (len(shown), len(vn_routes))) style "vnf_count" yalign 0.5
    use vn_route_list(shown, (40, 124, 1860, 946), 1810, small=True)

screen vn_route_list(shown, box, card_w, small=False):
    viewport:
        pos box[:2]
        xysize box[2:]
        yadjustment vn_route_yadj
        mousewheel True
        draggable True
        scrollbars "vertical"
        vbox:
            spacing 22
            for r in shown[:vn_route_limit]:
                use vn_route_card(r, card_w, small)
            if not shown:
                null height 40
                text (_("No story has all of these tags.") if vn_tag_mode() == "all" else _("No story has any of these tags.")) style "vnf_empty"
                textbutton _("Clear all") style_prefix "vnf_chip" action Function(vn_tag_clear)
            elif len(shown) > vn_route_limit:
                textbutton (_("Show more  (%d more)") % (len(shown) - vn_route_limit)):
                    style_prefix "vnf_chip"
                    xalign 0.5
                    action Function(vn_route_more)
                null height 20

## One card. The cover sits in a fixed box, so the text column always fits the card and wraps inside it
## (2026-11-13: the landscape covers, 1216x832, once pushed an over-wide column past the card's edge).
screen vn_route_card(r, card_w, small=False):
    $ _cov = (600, 410) if small else (440, 302)
    button:
        xsize card_w
        padding (24, 22, 30, 22)
        background Frame("gui/vn/card.png", 18, 18)
        hover_background Frame("gui/vn/card_hover.png", 18, 18)
        action Return(r["label"])
        hbox:
            spacing 30
            fixed:
                xysize _cov
                add Transform(vn_pic(r["cover"]), fit="contain", xysize=_cov) align (0.5, 0.5)
            vbox:
                spacing (16 if small else 12)
                xsize card_w - 54 - _cov[0] - 30
                text r["title"] style "vnf_card_title"
                if r["id"] in (persistent.catalog_done or ()):
                    text _("✓ Finished") style "vnf_card_done"
                text r["blurb"] style "vnf_card_blurb"
                if r["tags"]:
                    text vn_tags_line(r) style "vnf_card_tags"
                text _("▸ Play") style "vnf_card_play"

## The filter: the count and Clear all, Match All/Any, the sort (the phone's is in its top bar), then nhentai's tags
## by count and the Story row. A chip's number is what picking it would leave (All) or how many stories have it (Any); a chip that would
## leave nothing is greyed.
screen vn_tag_filter(shown, small=False):
    $ _pick, _mode = vn_tag_pick(), vn_tag_mode()
    vbox:
        style "vnf_vbox"
        if not small:
            hbox:
                spacing 14
                text (_("Showing %d of %d") % (len(shown), len(vn_routes))) style "vnf_count" yalign 0.5
                textbutton _("Clear all"):
                    style_prefix "vnf_chip"
                    sensitive bool(_pick)
                    action Function(vn_tag_clear)
        hbox:
            spacing 10
            text _("Match") style "vnf_head" yalign 0.5
            textbutton _("All") style_prefix "vnf_chip" selected (_mode == "all") action Function(vn_tag_set_mode, "all")
            textbutton _("Any") style_prefix "vnf_chip" selected (_mode == "any") action Function(vn_tag_set_mode, "any")
        text (_("Stories with every tag you pick") if _mode == "all" else _("Stories with at least one tag you pick")) style "vnf_hint"
        if not small:
            text _("Sort") style "vnf_head"
            hbox:
                spacing 10
                for _k, _lab in VN_SORTS:
                    textbutton _lab style_prefix "vnf_chip" selected (vn_route_sort() == _k) action Function(vn_route_set_sort, _k)
        ## nhentai's tags, the most used first; the top VN_TAG_TOP plus any picked, the rest behind More tags
        $ _cloud = vn_tag_cloud()
        $ _chips = _cloud if vn_tag_more else [t for i, t in enumerate(_cloud) if i < VN_TAG_TOP or t in _pick]
        text _("Tags") style "vnf_head"
        hbox:
            style "vnf_chips"
            for _t in _chips:
                $ _c = vn_tag_count(_t, shown)
                textbutton "%s  {alpha=*0.6}%d{/alpha}" % (VN_TAG_LABEL[_t], _c):
                    style_prefix "vnf_chip"
                    selected (_t in _pick)
                    sensitive (_t in _pick or _c > 0)
                    action Function(vn_tag_toggle, _t)
            if vn_tag_more:
                textbutton _("Fewer tags") style_prefix "vnf_chip" action SetVariable("vn_tag_more", False)
            elif len(_chips) < len(_cloud):
                textbutton (_("More tags (%d)") % (len(_cloud) - len(_chips))):
                    style_prefix "vnf_chip"
                    action SetVariable("vn_tag_more", True)
        ## the Story row: the change's pace and the counted format tags
        text _("Story") style "vnf_head"
        hbox:
            style "vnf_chips"
            for _t, _lab in vn_story_row():
                $ _c = vn_tag_count(_t, shown)
                textbutton "%s  {alpha=*0.6}%d{/alpha}" % (_lab, _c):
                    style_prefix "vnf_chip"
                    selected (_t in _pick)
                    sensitive (_t in _pick or _c > 0)
                    action Function(vn_tag_toggle, _t)

## the phone's filter panel, over the route select
screen vn_tag_panel():
    modal True
    zorder 50
    add Solid("#0b0b10")
    $ shown = vn_routes_shown()
    text _("Filter") size 64 bold True color "#f2f2f6" xpos 60 ypos 28
    viewport:
        xpos 60
        ypos 120
        xsize 1800
        ysize 800
        mousewheel True
        draggable True
        scrollbars "vertical"
        use vn_tag_filter(shown, small=True)
    hbox:
        xpos 60
        ypos 952
        spacing 30
        textbutton _("Clear all"):
            style_prefix "vnf_chip"
            sensitive bool(vn_tag_pick())
            action Function(vn_tag_clear)
        textbutton (_("Show 1 story") if len(shown) == 1 else _("Show %d stories") % len(shown)):
            style_prefix "vnf_chip"
            selected True
            action Hide("vn_tag_panel")

style vnf_side is default:
    background Frame("gui/vn/card.png", 18, 18)
    padding (22, 20, 10, 20)

style vnf_vbox is vbox:
    spacing 14
    xsize 440

style vnf_vbox:
    variant "small"
    spacing 24
    xsize 1740

style vnf_chips is hbox:
    box_wrap True
    spacing 10
    box_wrap_spacing 10
    xmaximum 440

style vnf_chips:
    variant "small"
    spacing 18
    box_wrap_spacing 18
    xmaximum 1740

style vnf_chip_button is default:
    padding (16, 7, 16, 9)
    background Frame(Transform("gui/vn/pill.png", matrixcolor=TintMatrix("#262632")), 10, 10)
    hover_background Frame(Transform("gui/vn/pill.png", matrixcolor=TintMatrix("#4a2c3a")), 10, 10)
    selected_background Frame(Transform("gui/vn/pill.png", matrixcolor=TintMatrix("#ff8fa3")), 10, 10)
    selected_hover_background Frame(Transform("gui/vn/pill.png", matrixcolor=TintMatrix("#ffb1c0")), 10, 10)
    insensitive_background Frame(Transform("gui/vn/pill.png", matrixcolor=TintMatrix("#191920")), 10, 10)

style vnf_chip_button:
    variant "small"
    padding (28, 14, 28, 16)

style vnf_chip_button_text is default:
    size 23
    color "#e6e6ee"
    hover_color "#ffffff"
    selected_color "#1c0f14"
    selected_hover_color "#1c0f14"
    insensitive_color "#5a5a66"

style vnf_chip_button_text:
    variant "small"
    size 40

style vnf_head is default:
    size 22
    bold True
    color "#9a9aa8"
    kerning 1

style vnf_head:
    variant "small"
    size 36

style vnf_hint is default:
    size 19
    italic True
    color "#7d7d8a"

style vnf_hint:
    variant "small"
    size 30

style vnf_count is default:
    size 26
    color "#f2f2f6"

style vnf_count:
    variant "small"
    size 40

style vnf_empty is default:
    size 34
    color "#d4d4dc"

style vnf_card_title is default:
    size 34
    bold True
    color "#ffffff"

style vnf_card_title:
    variant "small"
    size 50

style vnf_card_done is default:
    size 22
    color "#7fd08a"

style vnf_card_done:
    variant "small"
    size 34

style vnf_card_blurb is default:
    size 24
    color "#d4d4dc"
    line_spacing 6

style vnf_card_blurb:
    variant "small"
    size 36

style vnf_card_tags is default:
    size 20
    color "#8e8e9c"

style vnf_card_tags:
    variant "small"
    size 30

style vnf_card_play is default:
    size 28
    color "#ff8fa3"

style vnf_card_play:
    variant "small"
    size 44

## The gallery (main menu and game menu): each route's pictures in story order, the ones seen so
## far as thumbnails, the rest locked; a thumbnail opens the viewer.
screen vn_gallery():
    tag menu
    use game_menu(_("Gallery"), scroll="viewport"):
        vbox:
            spacing 34
            for r in vn_routes:
                $ _names = vn_gallery.get(r["id"], [])
                if _names:
                    $ _seen = [n for n in _names if vn_cg_seen(n)]
                    vbox:
                        spacing 14
                        text "%s  {size=-6}{color=#b7b7b7}%d of %d{/color}{/size}" % (r["title"], len(_seen), len(_names)) size 30 color "#f2f2f6"
                        hbox:
                            box_wrap True
                            spacing 14
                            box_wrap_spacing 14
                            xsize 1360
                            for n in _names:
                                if n in _seen:
                                    imagebutton:
                                        idle vn_thumb(n)
                                        hover vn_thumb(n, True)
                                        action Show("vn_gallery_view", names=_seen, i=_seen.index(n))
                                else:
                                    frame:
                                        xysize (256, 175)
                                        background Solid("#1b1b23")
                                        text "?" size 48 color "#3a3a46" align (0.5, 0.5)

## One picture at a time, full screen: click or right arrow for the next, left arrow for the last,
## right-click or Escape to close.
screen vn_gallery_view(names, i):
    modal True
    zorder 200
    add Solid("#000")
    add Transform(vn_pic(vn_art_file(vn_cg_files[names[i]])), fit="contain", xysize=(VN_W, VN_H)) align (0.5, 0.5)
    button:
        xysize (VN_W, VN_H)
        action (Show("vn_gallery_view", names=names, i=i + 1) if i + 1 < len(names) else Hide("vn_gallery_view"))
    key "K_RIGHT" action (Show("vn_gallery_view", names=names, i=i + 1) if i + 1 < len(names) else NullAction())
    key "K_LEFT" action (Show("vn_gallery_view", names=names, i=i - 1) if i > 0 else NullAction())
    key "game_menu" action Hide("vn_gallery_view")
    text "%d / %d" % (i + 1, len(names)) size 24 color "#b7b7b7" xalign 0.98 yalign 0.98

screen vn_hud():
    zorder 90
    if vn_route and not _menu:
        frame:
            xpos 24 ypos 18
            padding (18, 8, 18, 10)
            background Frame("gui/vn/chip.png", 12, 12)
            hbox:
                spacing 22
                text vn_time_str() style "vn_hud_text"
                text vn_day_str() style "vn_hud_text"
                if len(vn_art_sets.get(vn_route, ())) > 1:
                    textbutton ("Art: " + vn_art_name(vn_route)):
                        text_style "vn_hud_text"
                        text_hover_color "#ff8fa3"
                        padding (0, 0)
                        action Function(vn_art_cycle, vn_route)

init python:
    config.overlay_screens.append("vn_hud")
