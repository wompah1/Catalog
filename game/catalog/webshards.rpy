## Connected art repos (owner's storage plan, 2026-11-15; tools/shards.py). A GitHub Pages site holds at most
## 1 GB, so some routes' pictures are published from art-only sites beside the game's, all on one origin
## (wompah1.github.io). The Pages workflow writes game/catalog/webshards.json, {"<route>": "../<repo>/"}; when
## it's there, the web build's picture downloads for those routes fetch from that site instead, and are still
## written to the same path in the game's file system, so nothing else in the game knows. Ren'Py 8.5.3's own
## RenPyWeb.dl_new (renpy/webloader.py) is copied below with only the URL changed. Desktop builds, local web
## builds and a build with no shards redirect nothing.
init -998 python:
    if renpy.emscripten:
        import json as _ws_json
        try:
            _ws_map = _ws_json.loads(renpy.file("catalog/webshards.json").read())
        except Exception:
            _ws_map = {}
        if _ws_map:
            import emscripten as _ws_em
            _ws_em.run_script(r"""(function () {
    var MAP = %s;
    function url(path) {
        // game/art/<route>[.<set>]/<file>: a sharded route's picture, except its cover (the cards draw every cover)
        var m = /^game\/art\/([^\/.]+)(\.[^\/]+)?\/(.+)$/.exec(path);
        if (!m || !MAP[m[1]] || (!m[2] && m[3] === "cover.jpg")) return path;
        return MAP[m[1]] + path;
    }
    function patch() {
        if (typeof RenPyWeb === "undefined") { setTimeout(patch, 20); return; }
        RenPyWeb.dl_new = function (path) {
            var xhr = new XMLHttpRequest();
            xhr.responseType = 'arraybuffer';
            xhr.onerror = function () { console.log("Network error", xhr); };
            xhr.onload = function () {
                if (xhr.status == 200 || xhr.status == 304 || xhr.status == 206 || (xhr.status == 0 && xhr.response)) {
                    try { FS.unlink(path); } catch (error) {}
                    FS.writeFile(path, new Uint8Array(xhr.response), {canOwn: true});
                } else {
                    console.log("Download error", xhr);
                }
            };
            xhr.open('GET', url(path));
            xhr.send();
            RenPyWeb.xhrs[RenPyWeb.xhr_id] = xhr;
            var ret = RenPyWeb.xhr_id;
            RenPyWeb.xhr_id++;
            return ret;
        };
        console.log("webshards: " + Object.keys(MAP).length + " routes' pictures come from their art sites");
    }
    patch();
})();""" % _ws_json.dumps(_ws_map))
