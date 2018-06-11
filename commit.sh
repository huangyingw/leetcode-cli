#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./backup.sh
./remove_dup.sh
git co ./submissions/
git add ./submissions/
~/loadrc/gitrc/g.sh
./restore.sh
