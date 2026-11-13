## The catalog's VN layer, for every route (the Ren'Py pilot, 2026-11-11).
##
## The same screen as the DoL catalog's framework/vn-screen.js, on Ren'Py's own machinery:
##   - a background full-bleed (layer bgl), or a CG over it (layer cgl): the CG sits wholly above
##     the textbox (owner, 2026-11-10: "being able to better see the art"), a blurred copy of
##     itself filling the sides
##   - the PC sprite left, one cast sprite right (master layer); the speaker lit, the other dimmed
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
        """The other sprite steps back while someone with a sprite speaks."""
        talk = store.vn_talk
        if talk is None or talk == who:
            return False
        if who == "pc":
            return renpy.showing(talk)
        return talk == "pc"

    def _vn_sprite(st, at, resolve, who, face):
        d = vn_figure(vn_art_file(resolve(face)))
        if vn_dimmed(who):
            d = Transform(d, matrixcolor=VN_DIM)
        return d, None

    def vn_sprite_image(tag, faces, resolve, who=None):
        """Register `tag face` for each face; resolve(face) gives the file at show time, so a
        sprite follows the route's rung and outfit without a new show statement."""
        for f in faces:
            renpy.image((tag, f), DynamicDisplayable(_vn_sprite, resolve, who or tag, f))

    # ---- the stage ------------------------------------------------------------------------
    def vn_enter(bg=None, pc=None, pc_tag=None, cast=(), cg=None, trans=True):
        """A passage's stage row, as framework/vn-screen.js resolves it: the background (or None),
        the PC's face on pc_tag, the cast (a list of (tag, face)), and the CG (or None)."""
        store.vn_talk = None
        # a new place or picture dissolves in with the box out of the way (no empty box over the
        # old frame); the same place carries straight on, as the DoL screen does
        def _now(tag, layer):
            if not renpy.showing(tag, layer=layer):
                return None
            return " ".join(renpy.get_attributes(tag, layer=layer) or ())
        changed = (_now("bg", "bgl") != bg) or (_now("cg", "cgl") != cg)
        renpy.scene(layer="cgl")
        renpy.scene(layer="master")
        if bg:
            renpy.show("bg " + bg, layer="bgl")
        else:
            renpy.scene(layer="bgl")
        if pc and pc_tag:
            renpy.show(pc_tag + " " + pc, at_list=[vn_pc_slot])
        for tag, face in cast:
            renpy.show(tag + " " + face, at_list=[vn_cast_slot])
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
    def _vn_talk(event, interact=True, who=None, **kw):
        if event == "begin":
            store.vn_talk = who

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

    # ---- the route select: every route registers its card in its own route.rpy -----------
    vn_routes = []

    def vn_register_route(id, title, blurb, cover, label):
        """A card on the route select: the cover, the title, the blurb; Play jumps to `label`."""
        vn_routes.append(dict(id=id, title=title, blurb=blurb, cover=cover, label=label))

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
    xanchor 1.0 xpos VN_W - VN_SIDE yanchor 1.0 ypos VN_H + 22

image vn_black = Solid("#000")
image vn_main_bg = DynamicDisplayable(_vn_main_bg)
## a picture this checkout doesn't have (vn_pic): a dark card, so a slimmed worktree never crashes
image vn_missing = Fixed(Solid("#1b1b23"), Text("?", size=120, color="#3a3a46", xalign=0.5, yalign=0.5), xysize=(1216, 832))

default vn_talk = None
default vn_clock = VNState(day=0, hour=12, minute=0)
default vn_route = None
default vn_art = {}
default persistent.vn_fx_off = False

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
screen vn_face():
    fixed:
        xysize (VN_FACE + 8, VN_FACE + 8)
        yalign 1.0
        add vn_face_portrait() xysize (VN_FACE, VN_FACE) xalign 0.5 yalign 0.5
        add "gui/vn/face_frame.png" xysize (VN_FACE + 8, VN_FACE + 8)

## The route select (DoL's New Game cards): the cover left of the title, the blurb and Play.
screen vn_route_select():
    add Solid("#0b0b10")
    ## a test walk's plan picks the card by its title (game/catalog/vntrace.rpy)
    $ _vn_route_pick = vn_test_route_pick()
    if _vn_route_pick is not None:
        timer 0.05 action [Function(vn_test_picked), Return(_vn_route_pick)]
    vbox:
        xalign 0.5
        ypos 56
        spacing 30
        text _("Choose a story") size 56 color "#f2f2f6" xalign 0.5
        viewport:
            xsize 1580
            ysize 900
            mousewheel True
            draggable True
            ## a scrollbar only once the cards run past the screen (two fit)
            scrollbars ("vertical" if len(vn_routes) > 2 else None)
            vbox:
                spacing 26
                for r in vn_routes:
                    button:
                        xsize 1540
                        padding (24, 22, 30, 22)
                        background Frame("gui/vn/card.png", 18, 18)
                        hover_background Frame("gui/vn/card_hover.png", 18, 18)
                        action Return(r["label"])
                        ## the cover in a fixed box, so the text column always fits the card and wraps
                        ## inside it (2026-11-13: the new landscape covers, 1216x832, came out 585 wide at
                        ## this height and pushed an 1150-wide column past the card's right edge):
                        ## 1540 - 24 - 30 padding - 560 cover - 34 spacing = 892
                        hbox:
                            spacing 34
                            fixed:
                                xysize (560, 400)
                                add Transform(vn_pic(r["cover"]), fit="contain", xysize=(560, 400)) align (0.5, 0.5)
                            vbox:
                                spacing 18
                                xsize 892
                                text r["title"] size 38 bold True color "#ffffff"
                                if r["id"] in (persistent.catalog_done or ()):
                                    text _("✓ Finished") size 24 color "#7fd08a"
                                text r["blurb"] size 26 color "#d4d4dc" line_spacing 7
                                text _("▸ Play") size 32 color "#ff8fa3"

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
