#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

cd ./submissions/
git co .
./remove_dup.sh
git add .
~/loadrc/gitrc/g.sh
cd -
./restore.sh
