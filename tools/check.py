#!/usr/bin/env python3
"""Compare the Ren'Py screen with the DoL VN screen, line by line.

    python3 tools/check.py trace/redlightning-a.json trace/renpy-a.jsonl

The DoL side is tools/trace_dol.py's page trace; the Ren'Py side is game/catalog/vntrace.rpy's
line trace (tools/rptest.sh). Lines are matched by their text, in order. For each matched line it
compares what the player sees: the background (or the CG over it), the PC sprite file (rung,
outfit, face; under a CG, the face portrait), and the cast sprite. Lines only one side has (the
written-out sex scenes, DoL's combat prose and readouts) are counted, not compared.
Exit status 1 when any matched line differs.
"""
import collections
import json
import re
import sys


# Differences from the DoL screen that the port makes on purpose: (label, field) -> why.
EXPECTED = {
    # Red Lightning
    ("rl_blue_locker", "pc"): "outfit corrected to the prose (DoL showed the picture's tee all passage)",
    ("rl_blue_showers", "pc"): "outfit corrected to the prose (\"in your wet boxers\")",
    ("rl_girlfriend_room", "pc"): "the body changes at the shift line (DoL drew rung 6 from the first line)",
    # Open and Listen
    ("hy_laundry", "bg"): "the scene-art picture shows at its line (DoL's @cg off on the same page hid it)",
    ("hy_laundry", "cg"): "the scene-art picture shows at its line (DoL's @cg off on the same page hid it)",
    ("hy_laundry", "cast"): "the scene-art picture shows at its line (DoL's @cg off on the same page hid it)",
    ("hy_hub", "bg"): "the pill picture comes down at 'Your room' (DoL's pager kept it up the whole page)",
    ("hy_hub", "cg"): "the pill picture comes down at 'Your room' (DoL's pager kept it up the whole page)",
    ("hy_ask", "pc"): "a face cue on a line inside a branch applies (DoL's screen dropped it)",
    ("hy_master", "pc"): "the passage opens awake in day clothes for the body line (DoL opened in the sports bra, trance face)",
}


# Frames the port added where the DoL screen had none (owner, 2026-11-11: "picture every beat"):
# a line showing one of them differs from DoL in every field, on purpose.
ADDED_FRAMES = {"showers-grab", "doorway-kiss", "trophy-kiss", "kneel-slap", "gf-climb", "bleacher-kiss",
                "listen-rim", "never-rim", "sink-tee"}


def expected(label, field, cg=None):
    if cg in ADDED_FRAMES:
        return "a frame the port added (DoL showed no picture there)"
    if label and label.endswith("_sex"):
        return "a written-out sex scene: any match is with DoL's random combat prose"
    return EXPECTED.get((label, field))


def skel(s):
    s = re.sub(r"\{[^{}]*\}", "", s or "")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def norm(n):
    if not n:
        return None
    n = re.sub(r"\.(jpg|png)$", "", n.rsplit("/", 1)[-1])
    n = re.sub(r"^(rl|hy)_(sa_)?", "", n)
    return n.replace("_", "-").replace(" ", "-")


def dol_lines(path):
    out = []
    for p in json.load(open(path)):
        for pg in p["pages"]:
            cg = norm(pg.get("cg"))
            for ln in pg["lines"]:
                t = ln["text"]
                if ln["kind"] == "prose" and (re.match(r"^\(\d\)", t) or "Athletics:" in t):
                    continue
                out.append({"passage": p["passage"], "text": t, "skel": skel(t),
                            "bg": None if cg else norm(pg.get("bg")), "cg": cg,
                            "pc": norm(pg.get("face") if cg else pg.get("pc")),
                            "cast": None if cg else norm(pg.get("cast"))})
    return out


def renpy_lines(path):
    out = []
    for line in open(path):
        r = json.loads(line)
        what = (r.get("what") or "").split("\n{size=-5}")[0]
        cg = norm(r.get("cg"))
        out.append({"label": r.get("label"), "text": what, "skel": skel(what), "bg": None if cg else norm(r.get("bg")),
                    "cg": cg, "pc": norm(r.get("pc")), "cast": None if cg else norm(r.get("cast"))})
    return out


def main():
    dol, rp = dol_lines(sys.argv[1]), renpy_lines(sys.argv[2])
    i, matched, only_rp = 0, 0, collections.Counter()
    diffs = collections.defaultdict(list)
    used = set()
    for r in rp:
        if len(r["skel"]) < 4:
            continue
        hit = next((j for j in range(i, min(len(dol), i + 120)) if dol[j]["skel"] == r["skel"]), None)
        if hit is None:
            only_rp[r["label"]] += 1
            continue
        d = dol[hit]
        used.add(hit)
        i = hit + 1
        matched += 1
        for f in ("bg", "cg", "pc", "cast"):
            if d[f] != r[f]:
                diffs[f].append((r["label"], r["text"][:70], d[f], r[f], r["cg"]))
    only_dol = collections.Counter(d["passage"] for j, d in enumerate(dol) if j not in used and len(d["skel"]) >= 4)
    print(f"matched {matched} of {len(rp)} Ren'Py lines ({len(dol)} DoL lines)")
    print("Ren'Py only, by label:", dict(only_rp.most_common(12)))
    print("DoL only, by passage:", dict(only_dol.most_common(12)))
    bad = 0
    for f in ("bg", "cg", "pc", "cast"):
        ok = [r for r in diffs[f] if expected(r[0], f, r[4])]
        rows = [r for r in diffs[f] if not expected(r[0], f, r[4])]
        bad += len(rows)
        print(f"\n{f}: {len(rows)} lines differ" + (f" (+{len(ok)} expected)" if ok else ""))
        for label, why in sorted({(r[0], expected(r[0], f, r[4])) for r in ok}):
            print(f"  expected  {label}: {why}")
        by = collections.defaultdict(list)
        for row in rows:
            by[row[0]].append(row)
        for label, rs in by.items():
            kinds = collections.Counter((x[2], x[3]) for x in rs)
            print(f"  {label}: {len(rs)}  " + "; ".join(f"DoL {a} / Ren'Py {b} x{n}" for (a, b), n in kinds.most_common(4)))
            print(f"      first: {rs[0][1]!r}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
