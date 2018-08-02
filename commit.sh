#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

git co ./submissions/
./remove_dup.sh
git add ./submissions/
~/loadrc/gitrc/g.sh
./restore.sh
