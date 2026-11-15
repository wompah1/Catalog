#!/usr/bin/env python3
"""Prose against picture, line by line, over rptest walk traces (owner, 2026-11-15: gradual TF, and the prose and the
sprite must agree at every line). For each traced line that describes the PC's hair colour, hair length or breast size
("your pink hair", "your hair is shoulder-length now", "your heavy breasts"), compare the claim with the prompt of the
picture on screen at that line: the CG when one is up, else the PC's sprite. The prompts come from the landed picks'
records, route-covers/vn/<route>[@<set>]/picks.json.

    python3 -I tools/trace_looks.py trace/hypno-a.jsonl [...] [--game game] [--strict]

A heuristic, so it reports and doesn't judge. A flag is worth a look, not a certain fault: past-tense lines ("your hair
used to be brown"), wigs and clip-ins, and another person's "your" all trip it. Comparatives ("longer", "fuller") are
not read as sizes. Lengths and breast sizes are flagged two or more steps apart (short vs long, small vs large), so a
neighbouring step (short vs shoulder-length) isn't. Exits 1 on any flag only with --strict.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PICKS = ROOT.parent / "route-covers" / "vn"

# hair colour words -> the prompt words that agree with them
FAMILIES = {
    "blonde": "blonde blond golden gold honey flaxen yellow straw platinum",
    "platinum": "platinum blonde blond silver white",
    "silver": "silver white platinum grey gray",
    "white": "white silver platinum",
    "grey": "grey gray silver white",
    "black": "black jet raven dark",
    "brown": "brown brunette chestnut chocolate mousy mousey dark auburn",
    "red": "red auburn ginger copper scarlet crimson strawberry",
    "pink": "pink rose bubblegum magenta salmon",
    "purple": "purple lavender violet plum lilac mauve",
    "blue": "blue cobalt navy teal aqua cyan sky",
    "green": "green mint teal emerald",
}
ALIASES = {"blond": "blonde", "golden": "blonde", "gold": "blonde", "honey": "blonde", "flaxen": "blonde",
           "straw": "blonde", "gray": "grey", "jet": "black", "raven": "black", "brunette": "brown",
           "chestnut": "brown", "chocolate": "brown", "mousy": "brown", "mousey": "brown", "auburn": "red",
           "ginger": "red", "copper": "red", "scarlet": "red", "crimson": "red", "rose": "pink",
           "bubblegum": "pink", "magenta": "pink", "lavender": "purple", "violet": "purple", "plum": "purple",
           "lilac": "purple", "mauve": "purple", "cobalt": "blue", "navy": "blue", "teal": "blue", "aqua": "blue",
           "cyan": "blue", "mint": "green", "emerald": "green"}
COLOURS = set(FAMILIES) | set(ALIASES)
HAIRWORD = r"(?:hair|twintails|twin tails|pigtails|ponytail|braids?|bob|curls|locks|fringe)"

LENGTHS = [  # (regex, step)
    (r"\b(?:shaved|buzz(?:ed|cut)?|crew cut|close-cropped)\b", 0),
    (r"\b(?:short|cropped|pixie)\b", 1),
    (r"\b(?:bob|chin-length|jaw-length|ear-length)\b", 1),
    (r"\b(?:medium|shoulder-length|to your shoulders|brushing your shoulders|collarbone)\b", 2),
    (r"\b(?:long|past your shoulders|down your back|between your shoulder blades)\b", 3),
    (r"\b(?:very long|waist-length|hip-length|to your waist|to your hips|absurdly long)\b", 4),
]
PROMPT_LENGTHS = [
    (r"\b(?:very short hair|buzz cut|shaved head)\b", 0), (r"\bshort hair\b|\bpixie cut\b|\bbob cut\b|\bbob\b", 1),
    (r"\bmedium hair\b|\bshoulder-length\b", 2), (r"\blong hair\b|\blong \w+ hair\b", 3),
    (r"\bvery long hair\b|\babsurdly long hair\b|\bwaist-length\b", 4),
]
BREASTS = [
    (r"\bflat\b", 0),
    (r"\b(?:tiny|budding|small|little|perky|a-cup|b-cup|an a|a b)\b|\ba handful\b", 1),
    (r"\b(?:medium|modest|c-cup|a c)\b", 2),
    (r"\b(?:large|big|heavy|full|generous|d-cup|dd|e-cup|a d|a dd)\b", 3),
    (r"\b(?:huge|enormous|massive|giant|gigantic|f-cup|g-cup|h-cup|an f|a g)\b", 4),
]
PROMPT_BREASTS = [(r"\bflat chest\b", 0), (r"\b(?:tiny|small) breasts\b", 1), (r"\bmedium breasts\b", 2),
                  (r"\blarge breasts\b", 3), (r"\b(?:huge|gigantic) breasts\b", 4)]
CHESTWORD = r"(?:breasts|tits|boobs|chest|cleavage)"
COMPARATIVE = re.compile(r"\b(?:longer|shorter|bigger|smaller|fuller|heavier|larger|lighter|darker|more|less)\b")
PAST = re.compile(r"\b(?:used to|once|before|had been|anymore|any more|was|were)\b")


def steps(text, table):
    return sorted({s for rx, s in table if re.search(rx, text)})


def prompt_colours(prompt):
    """Every colour word in a prompt phrase about hair: 'pink hair', 'dark brown hair dyed red halfway up', 'red tips'."""
    words = set()
    for seg in re.split(r"[,.;:]", prompt):
        if re.search(r"\b" + HAIRWORD + r"\b|\b(?:tips|roots|streaks?|highlights)\b", seg):
            words |= {w for w in re.findall(r"[a-z]+", seg) if w in COLOURS}
    return words


def clauses(text):
    return [c for c in re.split(r"(?<=[.!?;])\s+|\s+[-—]\s+", text) if c]


def claims(text):
    """(attribute, value, clause) the line asserts about the PC."""
    out = []
    for c in clauses(text.lower().replace("’", "'")):
        if "your" not in c:
            continue
        past = bool(PAST.search(c))
        for m in re.finditer(r"\byour\s+((?:[\w-]+[\s,]+){0,4}?)" + HAIRWORD + r"\b([^,.;!?]{0,60})", c):
            before, after = m.group(1), m.group(2)
            region = before + " " + (after if re.match(r"\s*(?:is|'s|has|have|goes|went|turns|turned|now|falls|hangs|comes|sits)\b", after) else "")
            for w in re.findall(r"[a-z]+", region):
                if w in COLOURS:
                    out.append(("hair colour", w, c, past))
            if not COMPARATIVE.search(region):
                for s in steps(region, LENGTHS):
                    out.append(("hair length", s, c, past))
        for m in re.finditer(r"\byour\s+((?:[\w-]+[\s,]+){0,3}?)" + CHESTWORD + r"\b([^,.;!?]{0,50})", c):
            before, after = m.group(1), m.group(2)
            region = before + " " + (after if re.match(r"\s*(?:are|is|'re|have|now|sit|hang|fill|strain)\b", after) else "")
            if not COMPARATIVE.search(region):
                for s in steps(region, BREASTS):
                    out.append(("breasts", s, c, past))
    return out


def route_of(label, game):
    for f in game.glob("*/*.rpy"):
        if re.search(r"^label\s+%s\s*:" % re.escape(label), f.read_text(errors="replace"), re.M):
            return f.parent.name
    return None


def picks(route):
    out = {}
    for d in [PICKS / route] + sorted(PICKS.glob(route + "@*")):
        p = d / "picks.json"
        if p.exists():
            for k, v in json.load(open(p)).items():
                if isinstance(v, dict) and v.get("prompt"):
                    # NovelAI's negative-weight blocks ("-1::gigantic breasts ::") name what the picture avoids
                    out.setdefault(k, re.sub(r"-\d+(?:\.\d+)?::.*?::", " ", v["prompt"].lower(), flags=re.S))
    return out


def shown(row, rp):
    """(what's on screen, its prompt) for the row: the CG if one is up and recorded, else the PC's sprite."""
    if row.get("cg"):
        key = re.sub(r"^[a-z0-9]+_", "", row["cg"]).replace("_", "-")
        if key in rp:
            return "CG " + key, rp[key]
    if row.get("pc"):
        key = row["pc"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
        if key in rp:
            return "sprite " + key, rp[key]
    return None, None


NAMES = {0: "shaved/very short", 1: "short", 2: "shoulder-length", 3: "long", 4: "very long"}
CUPS = {0: "flat", 1: "small", 2: "medium", 3: "large", 4: "huge"}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    game = ROOT / "game"
    if "--game" in sys.argv:
        game = pathlib.Path(sys.argv[sys.argv.index("--game") + 1]).resolve()
        args = [a for a in args if pathlib.Path(a).resolve() != game]
    flags = checked = 0
    cache = {}
    for path in args:
        rows = [json.loads(l) for l in open(path) if l.strip().startswith("{")]
        rows = [r for r in rows if "what" in r]
        if not rows:
            continue
        route = route_of(rows[0].get("label", ""), game)
        if not route:
            print(f"{path}: can't tell the route from label {rows[0].get('label')!r}; skipped")
            continue
        rp = cache.setdefault(route, picks(route))
        seen = set()
        for r in rows:
            what = r.get("what") or ""
            for attr, val, clause, past in claims(what):
                src, prompt = shown(r, rp)
                if not prompt:
                    continue
                checked += 1
                bad = None
                if attr == "hair colour":
                    pc = prompt_colours(prompt)
                    ok = set(FAMILIES.get(ALIASES.get(val, val), "").split()) | {val}
                    if pc and not (pc & ok):
                        bad = f"prose says {val}, picture has {'/'.join(sorted(pc))}"
                elif attr == "hair length":
                    ps = steps(prompt, PROMPT_LENGTHS)
                    if ps and min(abs(val - s) for s in ps) >= 2:
                        bad = f"prose says {NAMES[val]}, picture has {'/'.join(NAMES[s] for s in ps)}"
                else:
                    ps = steps(prompt, PROMPT_BREASTS)
                    if ps and min(abs(val - s) for s in ps) >= 2:
                        bad = f"prose says {CUPS[val]}, picture has {'/'.join(CUPS[s] for s in ps)}"
                if bad and (r.get("label"), what, attr) not in seen:
                    seen.add((r.get("label"), what, attr))
                    flags += 1
                    print(f"{pathlib.Path(path).name}  {r.get('label')}  {attr}: {bad}  [{src}]"
                          f"{'  (past tense?)' if past else ''}\n    | {what[:150]}")
    print(f"{checked} prose claims about the PC's looks checked against the picture shown, {flags} to look at")
    sys.exit(1 if strict and flags else 0)


if __name__ == "__main__":
    main()
