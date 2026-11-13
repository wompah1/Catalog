## The web build's picture downloads, made to survive a bad connection (2026-11-13, twinetesting-c9). The owner,
## playing collar on a phone: "OSError: Download error: network error ('art/collar/stairs-open.jpg' ...)". The file
## was on the site; one XHR had failed. Ren'Py 8.5.3's renpy/webloader.py raises on any failed progressive download,
## and that's an uncaught exception mid-scene. This wraps process_downloaded_resources: before Ren'Py looks at the
## queue, a finished image request whose file never arrived is taken out and asked for again after a short wait
## (1, 2, 4, 8, 16 s), and after six failures it's dropped quietly (the low-quality placeholder stays on screen and the
## next show of that picture asks again). Only the web build (renpy.emscripten) is touched.

init -999 python:
    if renpy.emscripten and not getattr(renpy.webloader.process_downloaded_resources, "_vnw", False):
        import os as _vnw_os
        import time as _vnw_time
        import renpy.webloader as _vnw_wl

        _vnw_orig_process = _vnw_wl.process_downloaded_resources
        _vnw_tries = {}       # relpath -> failures so far
        _vnw_waiting = []     # [(due time, ReloadRequest)]

        def _vnw_process_downloaded_resources():
            now = _vnw_time.time()
            with _vnw_wl.queue_lock:
                # failed image requests out of the queue, before Ren'Py would raise on them
                keep = []
                for rr in _vnw_wl.queue:
                    if rr.rtype == "image" and rr.download_completed():
                        full = _vnw_os.path.join(renpy.config.gamedir, rr.relpath)
                        if not _vnw_os.path.exists(full):
                            n = _vnw_tries.get(rr.relpath, 0) + 1
                            _vnw_tries[rr.relpath] = n
                            if n <= 6:
                                _vnw_waiting.append((now + min(16, 2 ** (n - 1)), rr))
                                print("webretry: %s failed (%d), asking again" % (rr.relpath, n))
                            else:
                                print("webretry: %s failed six times, dropped" % rr.relpath)
                                _vnw_tries.pop(rr.relpath, None)
                            continue
                        _vnw_tries.pop(rr.relpath, None)
                    keep.append(rr)
                _vnw_wl.queue[:] = keep
                # the ones whose wait is up go back in with a fresh request
                still = []
                for due, rr in _vnw_waiting:
                    if due <= now:
                        try:
                            rr.xhr = _vnw_wl.XMLHttpRequest(rr.relpath)
                            _vnw_wl.queue.append(rr)
                        except Exception as e:
                            print("webretry: couldn't re-request %s: %r" % (rr.relpath, e))
                    else:
                        still.append((due, rr))
                _vnw_waiting[:] = still
            return _vnw_orig_process()

        _vnw_process_downloaded_resources._vnw = True
        _vnw_wl.process_downloaded_resources = _vnw_process_downloaded_resources
