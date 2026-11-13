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

if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
    echo "publish: commit or stash tracked changes first (the snapshot is HEAD's tree)" >&2; exit 1
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

if [ "$DRY" = 1 ]; then echo "publish: dry run, not pushing"; exit 0; fi
git push --force "$REMOTE" "refs/heads/$PUBLIC_BRANCH:refs/heads/$REMOTE_BRANCH"
echo "publish: pushed; GitHub Pages rebuilds from it"
