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

Nothing in `../catalog/` is changed: the tools only read it (twee, art, DoL traces).

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
templated names it flags "check by hand" are mostly in use). Later, when the merge wave is over:
WebP would take `game/art` from 238 MB to about 90 MB, but every route.rpy hardcodes `.png`/`.jpg`,
so it wants a central `vn_pic()`-by-stem and a `tools/convert_art.py`, one route at a time.

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
so nothing goes near GitHub's 100 MB file cap and the whole site stays under Pages' 1 GB.

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
