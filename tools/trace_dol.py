#!/usr/bin/env python3
"""Trace the DoL catalog's VN screen through one route, page by page.

The Ren'Py pilot's reference: for every page the current VN shows (catalog/ "DoL Engine Plus.html",
framework/vn-screen.js) it records the passage, the page's lines, and what the stage shows -- the
background, the PC sprite file (rung, outfit and face, which DoL's wardrobe decides implicitly),
the cast sprite and the CG. Encounters are clicked through as the VN does (the box takes the turn).

    python3 tools/trace_dol.py redlightning --out trace/redlightning-a.json
    python3 tools/trace_dol.py redlightning --pick alt --out trace/redlightning-b.json

--pick picks the choices: "first" (the first link of every choice) or "alt" (the second, where
there is one); --take PASSAGE=LINK (repeatable) overrides one passage's pick. Each route's stop
passages, always-taken links and state key are in ROUTES. Read-only: it plays a fresh game in
headless Chrome and changes nothing.
"""
import argparse
import json
import pathlib
import sys

CATALOG = pathlib.Path(__file__).resolve().parents[2] / "catalog"
sys.path.insert(0, str(CATALOG / "devTools" / "engine-strip"))
import dolkit  # noqa: E402

PAGES = """(KEY)=>{const P=VN.pager, st=document.getElementById('vn-stage');
  const base=s=>s?String(s).split('?')[0].split('/').pop():null;
  const img=sel=>{const i=st&&st.querySelector(sel); return i&&!i.hidden&&i.getAttribute('src')?base(i.getAttribute('src')):null};
  const line=b=>{const out=[]; const ls=b.querySelectorAll('.vn-line');
    if(ls.length){ls.forEach(l=>out.push({who:l.dataset.who||null, face:l.dataset.face||null,
      kind:[...l.classList].filter(c=>c!=='vn-line').join(' '), text:(l.querySelector('.vn-text')||l).textContent.trim()}));}
    else {const t=b.textContent.replace(/\\s+/g,' ').trim(); if(t) out.push({who:null, face:null, kind:'prose', text:t});}
    return out};
  const n=P.pages.length, out=[];
  for(let k=0;k<n;k++){P.show(k); const f=VN.frame||{};
    out.push({k, bg:img('.vn-bg'), pc:img('.vn-pc'), cast:img('.vn-cast'), cg: base(f.cg),
      face: (()=>{const e=document.querySelector('#story .vn-face'); return e&&!e.hidden ? base((e.style.backgroundImage||'').replace(/^url\\("?|"?\\)$/g,'')) : null})(),
      fx: P.pages[k].flatMap(b=>[...b.querySelectorAll('.vn-dir[data-k=fx]')].map(x=>x.dataset.v)),
      lines: P.pages[k].flatMap(line)});}
  P.show(n-1);
  const links=[...document.querySelectorAll('#passages a, #passages button')].filter(e=>e.offsetParent!==null||e.getClientRects().length)
     .map(e=>(e.innerText||'').replace(/^\\((?:(?:Shift|Ctrl|Alt) \\+ )?\\d+\\)\\s*/,'').trim()).filter(Boolean);
  const V=SugarCube.State.variables, s=(V.storylines||{})[KEY]||{};
  return {passage:SugarCube.State.passage, script:P.script, combat:document.body.classList.contains('vn-combat'),
    day:Time.days, hour:Time.hour, minute:Time.minute, weekday:Time.weekDay, tier:s.tier||0, landed:s.landed||0, pages:out, links}}"""

TURN = """()=>{const st=document.getElementById('vn-stage'); const base=s=>s?String(s).split('?')[0].split('/').pop():null;
  const f=VN.frame||{}; const story=document.getElementById('story');
  return {passage:SugarCube.State.passage, cg:base(f.cg), cum:VN.cumNow,
    text:(story?story.innerText:'').replace(/\\s+\\n/g,'\\n').trim().slice(0,1500)}}"""

# Per route: the passages the walk stops at (the route is over), the links it always takes (the
# alternatives skip an encounter), and its $storylines key.
ROUTES = {
    "redlightning": {"stop": {"Redlightning Epilogue Stay", "Redlightning Go Sunday"},
                     "always": ("Go and demand your rematch", "Kneel for him", "Squeeze them round him")},
    "hypno": {"stop": {"Hypno Epilogue Stay", "Hypno Epilogue Go", "Hypno Never Close"},
              "always": ("Keep them pushed together for him", "Stay on your knees for him")},
}
# Links never taken (the route's exits, or the classic view's buttons).
SKIP = ("Classic view", "Menu", "Choose another story", "Return", "Art:")


def box_click(g):
    box = g.page.evaluate("()=>{const r=document.getElementById('story').getBoundingClientRect(); return [r.left, r.top]}")
    g.page.mouse.click(box[0] + 200, box[1] + 20)
    g.page.wait_for_timeout(350)


def walk(rid, pick, cap, take=None):
    cfg = ROUTES[rid]
    STOP, ALWAYS, take = cfg["stop"], cfg["always"], take or {}
    trace = []
    with dolkit.game() as g:
        g.start_route(rid)
        g.page.wait_for_timeout(900)
        for _ in range(cap):
            g.dismiss_interrupts()
            if g.passage_name() == "Route Sleep":
                g.page.wait_for_timeout(1200)
                continue
            snap = g.page.evaluate(PAGES, rid)
            if snap["combat"]:
                turns, start = [], snap["passage"]
                for _t in range(40):
                    if g.passage_name() != start:
                        break
                    turns.append(g.page.evaluate(TURN))
                    box_click(g)
                snap["turns"] = turns
                trace.append(snap)
                print(f"  {start}: encounter, {len(turns)} turns -> {g.passage_name()}", flush=True)
                continue
            trace.append(snap)
            print(f"  {snap['passage']}: {len(snap['pages'])} pages, day {snap['day']} {snap['hour']}:00, "
                  f"links {snap['links']}", flush=True)
            if snap["passage"] in STOP:
                break
            links = [x for x in snap["links"] if not any(x.startswith(s) for s in SKIP)]
            if not links:
                box_click(g)   # the VN's last-page click follows a lone link, or Route Sleep passes
                continue
            choice = links[1] if pick == "alt" and len(links) > 1 else links[0]
            # the alt walk still plays every encounter (its alternatives skip them)
            choice = next((x for x in links if x in ALWAYS), choice)
            if snap["passage"] in take:
                choice = next(x for x in links if take[snap["passage"]] in x)
            snap["took"] = choice
            before = g.passage_name()
            if not g.click(choice, settle=900):
                raise RuntimeError(f"could not click {choice!r} on {before}")
        print(f"  errors: {g.errors[:5]}" if getattr(g, "errors", None) else "  no console errors")
    return trace


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("route")
    ap.add_argument("--pick", choices=["first", "alt"], default="first")
    ap.add_argument("--out", required=True)
    ap.add_argument("--cap", type=int, default=400)
    ap.add_argument("--take", action="append", default=[], help="PASSAGE=LINK text to pick on that passage")
    a = ap.parse_args()
    take = dict(x.split("=", 1) for x in a.take)
    trace = walk(a.route, a.pick, a.cap, take)
    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(trace, indent=1, ensure_ascii=False))
    print(f"wrote {out}: {len(trace)} passages, {sum(len(t['pages']) for t in trace)} pages")


if __name__ == "__main__":
    main()
