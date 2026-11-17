## Test walks only (tools/rptest.sh): open the game window on a chosen display.
##
## The owner (2026-11-17, via b0): "for walkthroughs, could it open deliberately on my second monitor". Ren'Py 8.5.3
## has no SDL_VIDEO_WINDOW_POS. It restores preferences.window_position when preferences.window_position_layout
## equals the display layout as the window opens, so this sets both before the window opens, plus a window size
## that fits that display (Ren'Py's own size is worked out for the main display). SDL's centred-on-display
## positions don't survive the restore; real coordinates do.
##
## None of it reaches the player's preferences: rptest.sh runs with a throwaway --savedir and holds game/saves
## aside for the run.
##
## RPTEST_DISPLAY (rptest.sh sets "second" unless the caller set it):
##   unset or ""   nothing happens (the player's game, the web build)
##   second        the first display that isn't the main one; nothing when there's only one
##   main          nothing happens: Ren'Py's own placement, on the main display
##   <n>           SDL display n (0 is the main display)
## The window is the largest 16:9 that fits the display below its menu bar and title bar, centred across it.

init 999 python hide:
    import os

    want = os.environ.get("RPTEST_DISPLAY", "").strip().lower()

    if want and want != "main" and not (renpy.emscripten or renpy.mobile):
        try:
            display = renpy.pygame.display
            # The same list Interface.get_display_layout() builds when the window opens. Video isn't up yet at
            # init without a presplash, so start it (SDL counts the init; Ren'Py's own call later is harmless).
            if not display.get_num_video_displays():
                display.init()
            layout = tuple(display.get_display_bounds(i) for i in range(display.get_num_video_displays()))

            if want == "second":
                index = 1 if len(layout) > 1 else None
            elif want.isdigit() and int(want) < len(layout):
                index = int(want)
            else:
                index = None

            if index is None:
                print("[rptest-window] RPTEST_DISPLAY=%s: no such display among %d; Ren'Py's own placement" % (want, len(layout)))
            else:
                x, y, w, h = layout[index]
                top, bottom, side = 64, 16, 32   # the menu bar plus the title bar; a margin below and at the sides
                scale = min((w - 2 * side) / float(config.screen_width), (h - top - bottom) / float(config.screen_height))
                size = (int(config.screen_width * scale), int(config.screen_height * scale))
                pos = (x + (w - size[0]) // 2, y + top)

                _preferences.fullscreen = False
                _preferences.maximized = False
                _preferences.physical_size = size
                _preferences.window_position = pos
                _preferences.window_position_layout = layout
                _preferences.restore_window_position = True
                print("[rptest-window] display %d %r: window %dx%d at %r" % (index, layout[index], size[0], size[1], pos))

        except Exception as e:
            print("[rptest-window] couldn't place the window (%r); Ren'Py's own placement" % (e,))
