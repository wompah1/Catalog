#!/bin/bash
# Publish the catalog to GitHub as one anonymous snapshot commit per run.
#
# The development history stays on this machine. Each run takes the current HEAD's tree, makes a
# commit of it on the local branch `public` (author and committer are the GitHub account's noreply
# identity, dates in UTC, no trailers), and force-pushes that branch to origin's main, which is what
# GitHub Pages builds. Nothing from the local commits (names, emails, messages) reaches GitHub.
#
# Before pushing, the tree is grepped for the patterns in ~/.config/catalog-publish-deny.txt (one
# regex per line, case-insensitive; the file is private and never committed). Any hit aborts.
#
#   tools/publish.sh            # snapshot HEAD and push
#   tools/publish.sh --dry-run  # build the snapshot and run the checks, push nothing
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

REMOTE=origin
REMOTE_BRANCH=main
PUBLIC_BRANCH=public
IDENT_NAME=wompah1
IDENT_EMAIL=wompah1@users.noreply.github.com
DENY=${CATALOG_PUBLISH_DENY:-$HOME/.config/catalog-publish-deny.txt}
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1

# One publish at a time (C9, 2026-11-18 2:45 pm ET: six publishes from different worktrees in ten minutes raced on
# the shared public / public-art-N refs, and an art push lost to another's mid-upload). Every worktree shares the
# lock in the common git dir; a lock whose process is gone is cleared. A dry run takes it too (it moves the refs).
LOCK="$(cd "$(git rev-parse --git-common-dir)" && pwd)/publish.lock"
waited=0
until mkdir "$LOCK" 2>/dev/null; do
    holder=$(cat "$LOCK/pid" 2>/dev/null || true)
    if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then
        echo "publish: clearing a stale lock (pid $holder is gone)" >&2; rm -rf "$LOCK"; continue
    fi
    [ "$waited" = 0 ] && echo "publish: waiting for pid ${holder:-?} ($(cat "$LOCK/who" 2>/dev/null || echo starting))" >&2
    if [ "$waited" -ge 1800 ]; then echo "publish: still locked after 30 min ($LOCK); giving up" >&2; exit 1; fi
    sleep 10; waited=$((waited + 10))
done
echo $$ > "$LOCK/pid"; echo "$(pwd) since $(date -u +%H:%M:%SZ)" > "$LOCK/who"
trap 'rm -rf "$LOCK"' EXIT

if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
    echo "publish: commit or stash tracked changes first (the snapshot is HEAD's tree)" >&2; exit 1
fi

# A stale checkout must not roll the site back: HEAD has to contain the commit the last publish was made from
# (refs/published/source, set after each successful push). Otherwise routes published since would come off.
LAST_SRC=$(git rev-parse -q --verify refs/published/source 2>/dev/null || true)
if [ -n "$LAST_SRC" ] && ! git merge-base --is-ancestor "$LAST_SRC" HEAD; then
    echo "publish: HEAD $(git rev-parse --short HEAD) doesn't contain the last published commit $(git rev-parse --short "$LAST_SRC"): merge main (or that commit) first, or the site loses what was published since" >&2
    [ "$DRY" = 1 ] || exit 1
fi

# Owner, 2026-11-17: every story gets tags for the story menu's filter. A route with no line in
# game/catalog/tags.rpy (or a bad one) doesn't publish; tools/tags_check.py --format <route> helps write one.
if ! python3 -I tools/tags_check.py --rev HEAD; then
    if [ "$DRY" = 1 ]; then echo "publish: a real publish stops here (story tags)"; else
        echo "publish: not publishing: add the route's tags line to game/catalog/tags.rpy" >&2; exit 1; fi
fi

# Owner, 2026-11-15: "walk throughs should be done after redraws to ensure quality". Every route whose art changed since
# the last publish (a redraw, a re-encode, a reused room) gets the full play-order walk first: walksheet in play order,
# every frame against its line, plus its rptest walks. This lists them; it can't check that the walks were done.
# main as it was at the last publish (origin/main itself leaves the art-repo routes out, so it can't be diffed)
LAST=$(git log -1 --format=%ct refs/remotes/origin/main 2>/dev/null || true)
BASE=$(git rev-list -1 --first-parent --before="@${LAST:-0}" HEAD 2>/dev/null || true)
CHANGED=$([ -n "$BASE" ] && git diff --name-only "$BASE" HEAD -- game/art | cut -d/ -f3 | sort -u | tr '\n' ' ')
if [ -n "$CHANGED" ]; then
    echo "publish: art changed since the last publish: $CHANGED"
    echo "publish: each walked in play order since its last redraw (walksheet + rptest walks)? If not, stop here."
    # Owner, 2026-11-16: a chat other than the builder walks every route before it publishes, and each such route
    # needs "passed at <commit>" in ../route-covers/pipeline/REVIEWS.md for the route as it is in HEAD.
    if ! python3 -I tools/review_gate.py $CHANGED; then
        if [ "$DRY" = 1 ]; then echo "publish: a real publish stops here (review gate)"; else
            echo "publish: not publishing: a route above hasn't passed review at this commit (route-covers/pipeline/REVIEWS.md)" >&2; exit 1; fi
    fi
fi

# A route published for the first time gets its connected art repo (tools/shards.py assign); the
# assignment is committed so the snapshot, and the web build's redirect map, carry it.
if [ "$DRY" = 1 ]; then
    python3 -I tools/shards.py assign --dry-run | sed 's/^/publish: would assign /'
else
    ASSIGNED=$(python3 -I tools/shards.py assign)
    if [ -n "$ASSIGNED" ]; then
        echo "$ASSIGNED" | sed 's/^/publish: assigned /'
        git commit -q -m "shards: $(echo "$ASSIGNED" | tr '\n' ';' | sed 's/;$//')" -- tools/shards.json
    fi
fi

TREE=$(git rev-parse 'HEAD^{tree}')
if [ -s "$DENY" ]; then
    hits=$(git grep -I -n -i -E -f "$DENY" "$TREE" -- . || true)
    if [ -n "$hits" ]; then
        echo "publish: identifying text in the tree, not pushing:" >&2
        echo "$hits" | sed "s#^$TREE:##" | cut -c1-200 >&2; exit 1
    fi
else
    echo "publish: no deny list at $DENY, skipping the text check" >&2
fi

# Connected art repos (tools/shards.json, 2026-11-15): a sharded route's art is published from its own
# art repo, so Catalog's snapshot leaves it out (covers stay). Each art repo gets an orphan snapshot (no
# parent: the repo stays the size of its content), pushed before Catalog's so the game never points at
# pictures that aren't up yet.
HEAD_TREE=$TREE
SHARD_LIST=$(python3 -I tools/shards.py list)
if [ -n "$SHARD_LIST" ]; then
    TREE=$(python3 -I tools/shards.py tree catalog "$HEAD_TREE")
fi

PARENT=$(git rev-parse -q --verify "refs/heads/$PUBLIC_BRANCH" 2>/dev/null || true)
if [ -n "$PARENT" ] && [ "$(git rev-parse "$PARENT^{tree}")" = "$TREE" ]; then
    echo "publish: tree unchanged since the last snapshot ($PARENT)"; COMMIT=$PARENT
else
    NOW="$(date -u +%s) +0000"
    COMMIT=$(GIT_AUTHOR_NAME=$IDENT_NAME GIT_AUTHOR_EMAIL=$IDENT_EMAIL GIT_AUTHOR_DATE="$NOW" \
             GIT_COMMITTER_NAME=$IDENT_NAME GIT_COMMITTER_EMAIL=$IDENT_EMAIL GIT_COMMITTER_DATE="$NOW" \
             git commit-tree "$TREE" ${PARENT:+-p "$PARENT"} -m "The Catalog, $(date -u +%Y-%m-%d)")
    git update-ref "refs/heads/$PUBLIC_BRANCH" "$COMMIT"
    echo "publish: snapshot $COMMIT on $PUBLIC_BRANCH"
fi
git log -1 --format='  %an <%ae>  %ad  %s' "$COMMIT"

while read -r N REPO KEY; do
    [ -n "$N" ] || continue
    STREE=$(python3 -I tools/shards.py tree "$N" "$HEAD_TREE")
    SPREV=$(git rev-parse -q --verify "refs/heads/public-art-$N" 2>/dev/null || true)
    if [ -n "$SPREV" ] && [ "$(git rev-parse "$SPREV^{tree}")" = "$STREE" ]; then
        echo "publish: art $N ($REPO) unchanged"
    else
        NOW="$(date -u +%s) +0000"
        SC=$(GIT_AUTHOR_NAME=$IDENT_NAME GIT_AUTHOR_EMAIL=$IDENT_EMAIL GIT_AUTHOR_DATE="$NOW" \
             GIT_COMMITTER_NAME=$IDENT_NAME GIT_COMMITTER_EMAIL=$IDENT_EMAIL GIT_COMMITTER_DATE="$NOW" \
             git commit-tree "$STREE" -m "The Catalog's art ($N), $(date -u +%Y-%m-%d)")
        git update-ref "refs/heads/public-art-$N" "$SC"
        echo "publish: art $N snapshot $SC for $REPO"
    fi
    if [ "$DRY" = 1 ]; then echo "publish: dry run, not pushing art $N"; continue; fi
    # leased on what this repo last pushed there: a push from anywhere else since stops the publish instead of
    # being overwritten. A failed art push stops before Catalog's, so the game never goes up without its art.
    APREV=$(git rev-parse -q --verify "refs/published/art-$N" 2>/dev/null || true)
    LEASE=--force; [ -n "$APREV" ] && LEASE="--force-with-lease=refs/heads/main:$APREV"
    if ! GIT_SSH_COMMAND="ssh -F /dev/null -i $KEY -o IdentitiesOnly=yes" \
        git push "$LEASE" "git@github.com:$REPO.git" "refs/heads/public-art-$N:refs/heads/main"; then
        echo "publish: art $N push failed; Catalog NOT pushed. If $REPO main moved since $APREV, someone published from elsewhere: check it (git ls-remote) before re-running" >&2
        exit 1
    fi
    # what the art site serves (public-art-N also moves on a dry run); sceneart.py prune reads it
    git update-ref "refs/published/art-$N" "refs/heads/public-art-$N"
done <<< "$SHARD_LIST"

if [ "$DRY" = 1 ]; then echo "publish: dry run, not pushing"; exit 0; fi
CPREV=$(git rev-parse -q --verify refs/published/catalog 2>/dev/null || true)
LEASE=--force; [ -n "$CPREV" ] && LEASE="--force-with-lease=refs/heads/$REMOTE_BRANCH:$CPREV"
if ! git push "$LEASE" "$REMOTE" "refs/heads/$PUBLIC_BRANCH:refs/heads/$REMOTE_BRANCH"; then
    echo "publish: Catalog push failed (the art repos are already up; re-run when fixed)" >&2; exit 1
fi
git update-ref refs/published/catalog "refs/heads/$PUBLIC_BRANCH"
git update-ref refs/published/source HEAD
echo "publish: pushed; GitHub Pages rebuilds from it"
