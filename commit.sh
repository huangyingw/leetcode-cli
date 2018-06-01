#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

~/loadrc/gitrc/gpl.sh
./backup.sh
./remove_dup.sh
~/loadrc/bashrc/cscope.sh
git add ./submissions/ files.proj
~/loadrc/gitrc/g.sh
./restore.sh
