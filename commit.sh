#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./backup.sh
./restore.sh
./remove_dup.sh
git add ./submissions/
~/loadrc/gitrc/g.sh
