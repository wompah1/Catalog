#!/bin/bash
# Run one Ren'Py testcase (game/tests/*.rpy) in a real window, with a deadline, writing the
# screen trace (game/catalog/vntrace.rpy) to $2. The game's own process is killed on the deadline
# (renpy.sh runs it as a child, which plain `timeout` leaves behind).
#
#   tools/rptest.sh redlightning_a trace/renpy-a.jsonl [seconds]
#
# SDL's dummy driver can't drive the test runner (the software renderer never ticks), so this
# opens a game window for the length of the run. Saves and persistent data go to a temporary
# folder, removed afterwards.
set -u
case_=${1:?testcase}
out=${2:?trace file}
secs=${3:-600}
here=$(cd "$(dirname "$0")/.." && pwd)
sdk="$here/../renpy-8.5.3-sdk"
rm -f "$out" "$here/traceback.txt"
# a throwaway save folder: a test walk never touches the player's saves or persistent data
# (completion marks, preferences), and two worktrees' tests can't collide
saves=$(mktemp -d -t catalog-renpy-test)
# Ren'Py also reads and writes the game folder's own saves (game/saves, always, beside --savedir):
# hold the player's copy aside for the run, throw away whatever the test writes there, put it back
# (on any exit, a killed run included)
held=""
if [ -d "$here/game/saves" ]; then
  held="$here/game/saves.held-$$"
  mv "$here/game/saves" "$held"
fi
restore() {
  rm -rf "$here/game/saves"
  [ -n "$held" ] && [ -d "$held" ] && mv "$held" "$here/game/saves"
  rm -rf "$saves"
}
trap restore EXIT
VN_TRACE="$(cd "$(dirname "$out")" && pwd)/$(basename "$out")" "$sdk/renpy.sh" "$here" --savedir "$saves" test "$case_" > "$out.log" 2>&1 &
pid=$!
end=$((SECONDS + secs))
while kill -0 "$pid" 2>/dev/null; do
  if [ $SECONDS -ge $end ]; then
    echo "deadline: killing the run"
    pkill -P "$pid" 2>/dev/null
    kill "$pid" 2>/dev/null
    break
  fi
  sleep 2
done
wait "$pid" 2>/dev/null
status=$?
grep -E '^\[rpytest\] (Test cases|Status)|FAIL|Error' "$out.log" | head -8
[ -f "$here/traceback.txt" ] && { echo "--- traceback.txt"; grep -A4 'While running' "$here/traceback.txt" | head -8; }
echo "lines traced: $( [ -f "$out" ] && wc -l < "$out" || echo 0 )  exit: $status"

# The owner (2026-11-15): the person talking has the right picture in the box, checked on every walk. vn.rpy writes a
# speaker_miss row when a cast speaker's sprite isn't on stage and a face_miss row when a cast speaker over a CG has no
# face crop (faces.rpy needs `tools/sync_art.py <route> --faces-only`). Either fails the walk.
if [ -f "$out" ] && [ "$status" = 0 ]; then
  chk="$here/../route-covers/pipeline/runs/_c9/trace_speaker.py"
  if [ -f "$chk" ]; then
    res=$(python3 -I "$chk" "$out"); rc=$?
    echo "$res" | tail -12
    [ "$rc" = 0 ] || status=1
  else
    grep -q '"speaker_miss"' "$out" && { echo "speaker_miss rows in $out (the speaker's sprite isn't up)"; status=1; }
  fi
  if grep -q '"face_miss"' "$out"; then
    echo "face_miss: a cast speaker over a CG with no face crop (run tools/sync_art.py <route> --faces-only):"
    grep '"face_miss"' "$out" | head -8
    status=1
  fi
  [ "$status" = 0 ] || echo "walk FAILED the speaker check"
fi
exit "$status"
