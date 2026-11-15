# The Catalog in Ren'Py

The catalog's VN direction on a real VN engine instead of a skin over DoL (owner, 2026-11-11: "I
think ren'py is the way to go from now on"). Five routes so far, all played linear, as the DoL VN
plays them:

- **Red Lightning**, "My Rival Spikes My Sports Drink to Slow Me Down, and I Still Win by a Chest"
  (`game/redlightning/`, prefix `rl_`): the pilot.
- **Hypno**, "Open and Listen" (`game/hypno/`, prefix `hy_`), in two art sets: Vanripper and Abarus.
  Its **full regimen** (owner, 2026-11-11) is a branch at the Bloom consult: Emily asks for
  everything, and from the hinge the chest grows (rung 3 small to rung 6 large-plus) where the soft
  regimen holds it at buds. `hy.full`; the art is `pc-r<n>f-*` sprites and `<picture>-full.jpg`
  twins, shown in the soft pictures' place (route.rpy `_hy_full_of`); the gallery lists each twin
  after its picture.
- **Collar**, "I Bought a Voice Collar for the Tips, and It Won't Let Me Look Down" (`game/collar/`,
  prefix `co_`), Vanripper; its Abarus set is still to be drawn (the Art button falls back to
  Vanripper until it lands).
- **Neighbour**, "My Neighbour Grew a Cock and Only I Can Make It Go Down" (`game/neighbour/`,
  prefix `nb_`), Vanripper; its Abarus set is still to be drawn. One beat (skirt-cum) keeps the
  skirt-thighs frame up until a redraw passes.
- **Livestock**, "Marsh Farm Filed Me as a Heifer, So They Milk Me at Both Ends Until I Match the Paperwork"
  (`game/livestock/`, prefix `ls_`), Vanripper only (an animal-TF route, so no Abarus set).

`../catalog/` is only the art landing folder since the DoL games were retired (2026-11-15): `img/vn/`,
`img/scenes/` and `imagepacks/_custom/ui/route-covers/`, where `sceneart.py vnland` and the cover
landers write and `tools/sync_art.py` reads. The one-time migration tools that read the DoL game
(`tools/twee2rpy.py`, `tools/trace_dol.py`, `tools/check.py`'s DoL side) no longer run. The twee they
read is in `../story-archive/storylines/catalog/`.

## Play it

    ../renpy-8.5.3-sdk/renpy.sh .          # from this folder; or open renpy.app and pick the project

Ren'Py 8.5.3 SDK (checksum-verified) lives at `../renpy-8.5.3-sdk/`. Main menu: Start (the route
cards), Load, Gallery, Preferences (Effects > Shake and flash). In a story: the HUD (time, day, and
"Art:" for a route drawn in two styles), the quick menu (Back, History, Skip, Auto, Save...), which
fades out while the mouse rests and comes back when it moves. The text box is two lines tall and
grows for a third; a landscape frame (1216x832) sits above it at native size (2026-11-12).

## Disk

Each route worktree (`../catalog-renpy-<route>`) is a sparse checkout that leaves out the other
routes' art (`tools/slim_worktree.py`; 96 worktrees went from 21 GB to under 1 GB on 2026-11-12).
Run it on a new worktree after `git worktree add`; `--undo` restores a full checkout; see
CLAIMS.md "Worktrees are slimmed". `tools/orphan_art.py` lists art no script names (a report; the
templated names it flags "check by hand" are mostly in use).

**Picture format (2026-11-15): AVIF at quality 65, under each file's existing `.jpg`/`.png` name**
(`tools/artformat.py`). Ren'Py picks an image's decoder from its contents, not its name. That was tested
on desktop, in a web build, through progressive download (placeholder, then the file) and with sprite
alpha, and the web build decodes inside renpy.wasm, so a phone's own codecs don't matter. So no route's
code, gallery list, frames.json or slim pattern changes. A frame is about a fifth of its old JPEG and a
sprite a tenth of its PNG, with no visible difference at full size; the nine published routes went from
389 MB to 95 MB. `tools/sync_art.py` writes every new landing as AVIF. Art landed before the switch
converts with `python3 tools/convert_art.py <route>` (from the `../route-covers/vn/` originals where
they're the same picture; skips a folder with uncommitted changes; a second run changes nothing). Run
it on a route right after it merges to main. `file x.jpg` says "AVIF Image"; open pictures with PIL,
which reads them.

## Publish (GitHub Pages)

The public copy is `https://github.com/wompah1/Catalog` (remote `origin`, deploy key). Publish with

    tools/publish.sh            # tools/publish.sh --dry-run checks without pushing

which pushes one anonymous snapshot commit of HEAD's tree to origin's `main`; the local history is
never pushed, so don't `git push` by hand. Every push to that `main` runs `.github/workflows/pages.yml`,
which downloads the Ren'Py 8.5.3 SDK and its web package, runs `web_build`, and deploys the export to
`https://wompah1.github.io/Catalog/`. One-time on GitHub: Settings > Pages > Source = **GitHub
Actions**. The page is public to anyone with the link.

`progressive_download.txt` (project root, kept in git) decides what goes in `game.zip` and what the
browser fetches on demand: GUI images are packed, every other image and the audio stream in as a
scene needs them. That keeps `game.zip` near 10 MB with the art (about 284 MB) fetched per file,
so nothing goes near GitHub's 100 MB file cap.

**Connected art repos** (`tools/shards.json`, `tools/shards.py`, 2026-11-15). Pages rejects a site over
1 GB, and the whole catalog's art is more than that. So a route's art can be published from an art-only repo,
`wompah1/Catalog-art-<n>`, with its own Pages site on the same origin. A route listed under a shard has
`game/art/<route>/` (and `<route>.<set>/`) published there; its `cover.jpg` stays in Catalog because the
route cards draw every cover. `publish.sh` pushes each art repo an orphan snapshot first, then Catalog's
snapshot without that art. `pages.yml` fetches the art repos before `web_build` (so the download list
knows every picture's size), writes `game/catalog/webshards.json`, strips the sharded art from the
artifact and fails over 950 MB. In the web build, `game/catalog/webshards.rpy` sends those routes' picture
downloads to `../Catalog-art-<n>/`. **Two art repos exist (2026-11-15): `wompah1/Catalog-art-1` and `-2`.** The nine routes published before them stay in Catalog. Every route published from then on is placed by `publish.sh`, which runs `tools/shards.py assign`: at a route's first publish it takes the first art repo with room (750 MB each) and commits `tools/shards.json`. A route never moves once it's published. `python3 tools/shards.py sizes` says how full each site is. When both art repos near 750 MB, the owner makes `Catalog-art-3` once: create the public repo on wompah1, add its deploy key (write access), and after the first push creates `main`, turn on Pages (Deploy from a branch: `main`, `/`). Then add its entry to `tools/shards.json`. Keys live in `~/.ssh/id_ed25519_wompah1_catalog_art_<n>`.

Locally, with the web package unpacked at `../renpy-8.5.3-sdk/web/` (installed 2026-11-13):

    ../renpy-8.5.3-sdk/renpy.sh ../renpy-8.5.3-sdk/launcher web_build "$PWD" --destination /tmp/catalog-web
    (cd /tmp/catalog-web && python3 -m http.server 8765)   # then open http://127.0.0.1:8765/

Saves live in the browser's IndexedDB, so they stay per browser.

## What's where

    game/catalog/vn.rpy          the VN layer every route shares: layers (bgl, master, cgl), the CG fit
                                 above the box, sprites + dimming, name plates, SFX/thought lines,
                                 shake/flash (vnfx), the face portrait, the clock, the HUD, the route
                                 cards (vn_register_route), CGs (vn_register_cg), art sets
                                 (vn_register_art_sets, vn_art_file), the gallery
    game/catalog/vntrace.rpy     test support: the trace (VN_TRACE), screenshots (VN_SHOTS, VN_SHOT_AT),
                                 the walks' choice plans (renpy.session["vn_picks"])
    game/screens.rpy             Ren'Py's generated screens, restyled: the say screen is the VN box
    game/script.rpy              `start`: the route select (no route is named here)
    game/<route>/route.rpy       the route: state, the ladder's tables, the pacing rule, the sprite
                                 resolver (rung x outfit x face, the DoL screen's fallback chain), its card
    game/<route>/script.rpy      THE SOURCE: the passages, one label each (converted once from the twee)
    game/<route>/hub.rpy         the hub (linear days), by hand
    game/<route>/encounters.rpy  the sex scenes, written out (DoL's combat engine ran them)
    game/<route>/faces.rpy       GENERATED (tools/sync_art.py): the PC sprites' head crops
    game/<route>/gallery.rpy     GENERATED (tools/gallery.py): the route's pictures in story order
    game/art/<route>/            the route's art, copied from the catalog (tools/sync_art.py)
    game/art/<route>.<set>/      another art set (catalog/img/vn/<route>@<set>/; not "@" here, which
                                 Ren'Py reads as an image modifier)
    game/tests/<route>.rpy       full walks for Ren'Py's test runner
    trace/                       the DoL VN's page traces and the Ren'Py line traces
    tools/renforge-patches/      two local fixes to RenForge 0.7.3 (reapply after a reinstall)

## Decisions (owner, 2026-11-11)

- Ren'Py is the catalog's engine from now on.
- A ported route's Ren'Py script is its source: edit the .rpy; the twee stays in ../catalog as a
  frozen reference. `tools/twee2rpy.py` is a one-time migration and won't overwrite a converted route.
- Routes with no VN script yet are rewritten straight in Ren'Py (sign-off on the plan first, as now).
- **Claim a route in `CLAIMS.md` before starting it**, and keep its row current (owner, 2026-11-12).
- One route per git branch/worktree when two are worked on at once; route-local names carry the
  route's prefix; the shared files (game/catalog/, screens.rpy) change from one session at a time.

## Rebuild

    python3 tools/sync_art.py <route>      # art, other art sets, cover, head crops from catalog/img/
    python3 tools/gallery.py <route>       # the gallery order (after adding pictures)
    python3 tools/make_gui.py              # the VN box, plate, cards, portrait frame; the standard GUI images
    python3 tools/twee2rpy.py <route>      # one-time: a VN-scripted route's twee -> game/<route>/script.rpy

New art still comes from the scene-art pipeline (route-covers/pipeline/, NovelAI), landed into the
catalog as before; `sync_art.py` brings it over.

## Test

    tools/rptest.sh redlightning_a trace/renpy-a.jsonl        # each opens a game window for ~30 s
    tools/rptest.sh redlightning_b trace/renpy-b.jsonl
    tools/rptest.sh hypno_a trace/renpy-hy-a.jsonl            # and hypno_b, hypno_c
    tools/rptest.sh hypno_a_abarus trace/renpy-hy-abarus.jsonl   # walk a in the Abarus set
    tools/rptest.sh hypno_d trace/renpy-hy-d.jsonl            # the full regimen to End Listen; hypno_e to
                                                              # End Never, hypno_d_abarus in Abarus (no DoL twin)
    tools/rptest.sh collar_a trace/renpy-collar-a.jsonl       # and collar_b (the other ending)
    tools/rptest.sh neighbour_a trace/renpy-neighbour-a.jsonl # and neighbour_b (the femboy branch)
    tools/rptest.sh livestock_a trace/renpy-livestock-a.jsonl # and livestock_b
    python3 tools/check.py trace/redlightning-a.json trace/renpy-a.jsonl     # and the others
    ../renpy-8.5.3-sdk/renpy.sh . lint

`check.py` matches the two screens line by line (background, CG, PC sprite file, cast) and fails on
any difference not listed in its EXPECTED table. `tools/trace_dol.py` re-records the DoL side.
Every walk runs on a throwaway save folder and holds `game/saves` aside, so tests never touch the
player's saves, seen lines, gallery or completion marks. Headless doesn't work on this Mac (under
SDL's dummy driver Ren'Py falls back to its software renderer, which never ticks the test runner),
so the walks need a real window.

## Differences from the DoL VN, on purpose

- The sex scenes are written beats (open / mid / peak / the PC's climax / his climax), from the
  routes' own line pools; DoL generated them from its combat engine, with its mechanics in the text.
- DoL's mechanical lines are gone: "A surge of cum erupts...", "You fix your clothing", stat lines,
  the athletics readout, "Story complete".
- Red Lightning: Blue Locker and Blue Showers' outfits follow the prose; the Girlfriend Room's body
  changes at the shift line. Hypno: see its route.rpy header and check.py's EXPECTED.
- A lone link's label shows under the passage's last line (as the VN joins it); menus use the choice
  screen with the last line as its caption.
- Not ported: free play (the doors, training, flavour visits, After Hours/Afterwards), money in the HUD.
