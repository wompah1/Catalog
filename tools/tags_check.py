"""Story tags (game/catalog/tags.rpy) against the routes registered in this checkout.

  python3 tools/tags_check.py               # every registered route has a valid tags line
  python3 tools/tags_check.py --rev HEAD    # the same for a commit's tree (publish.sh runs this: it ships HEAD)
  python3 tools/tags_check.py --format ID   # the Story row's counted tags for a route's tags line

Owner, 2026-11-17: every story gets tags for the story menu's filter, and an untagged route doesn't publish.
"""
import glob, os, re, subprocess, sys, textwrap

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAGS = os.path.join(HERE, "game", "catalog", "tags.rpy")
REG = re.compile(r'vn_register_route\(\s*"([^"]+)"')


def git(*args):
    return subprocess.run(["git", "-C", HERE] + list(args), check=True, capture_output=True).stdout.decode("utf-8", "replace")


def load(rev=None):
    """tags.rpy's python block, run as plain Python (it uses nothing from Ren'Py but _())."""
    src = git("show", "%s:game/catalog/tags.rpy" % rev) if rev else open(TAGS, encoding="utf-8").read()
    body = src.split("init -55 python:", 1)[1]
    env = {"_": lambda s: s}
    exec(compile(textwrap.dedent(body), TAGS, "exec"), env)
    return env


def registered(rev=None):
    """{route id: its directory} for every route.rpy in game/ (alt cards in the same file included); with `rev`,
    the files in that commit's tree, so an untracked folder in the checkout doesn't count."""
    out = {}
    if rev:
        files = [f for f in git("ls-tree", "-r", "--name-only", rev, "--", "game").split("\n")
                 if re.match(r"^game/[^/]+/[^/]+\.rpy$", f)]
        read = lambda f: git("show", "%s:%s" % (rev, f))
    else:
        files = glob.glob(os.path.join(HERE, "game", "*", "*.rpy"))
        read = lambda f: open(f, encoding="utf-8", errors="replace").read()
    for f in sorted(files):
        for m in REG.finditer(read(f)):
            out.setdefault(m.group(1), os.path.dirname(os.path.join(HERE, f)))
    return out


def format_tags(d):
    text = "".join(open(f, encoding="utf-8", errors="replace").read() + "\n" for f in glob.glob(os.path.join(d, "*.rpy")))
    menus = len(re.findall(r"^\s*menu\b", text, re.M))
    endings = len(re.findall(r"ending\s*=\s*True", text))
    words = len(text.split())
    tags = (["branching"] if menus >= 12 else []) + (["multiple endings"] if endings >= 2 else [])
    tags += ["short"] if words < 7000 else (["long"] if words >= 15000 else [])
    return tags, menus, endings, words


def main(argv):
    rev = None
    if argv[:1] == ["--rev"]:
        rev, argv = argv[1], argv[2:]
    try:
        env = load(rev)
    except Exception as e:  # a bad line: vn_tags_check raised, or the file doesn't parse
        print("tags: %s" % e, file=sys.stderr)
        return 1
    table, reg = env["vn_route_tags"], registered(rev)
    if argv[:1] == ["--format"]:
        for rid in argv[1:]:
            if rid not in reg:
                print("tags: %s isn't registered in this checkout" % rid, file=sys.stderr)
                return 1
            tags, m, e, w = format_tags(reg[rid])
            print("%s: %s   (%d menus, %d endings, %d words)" % (rid, ", ".join(tags) or "(none)", m, e, w))
        return 0
    missing = sorted(set(reg) - set(table))
    if missing:
        print("tags: no tags line in game/catalog/tags.rpy for: %s" % " ".join(missing), file=sys.stderr)
        print("tags: add one per route (rules at the top of the file; --format ID prints its counted Story tags)", file=sys.stderr)
        return 1
    print("tags: %d registered routes tagged (%d lines)" % (len(reg), len(table)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
