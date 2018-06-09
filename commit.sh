#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

~/loadrc/gitrc/grsh.sh
./backup.sh
./remove_dup.sh
git add ./submissions/
~/loadrc/gitrc/g.sh
./restore.sh
