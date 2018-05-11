#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./remove_dup.sh
~/loadrc/bashrc/cscope.sh
git add .
~/loadrc/gitrc/g.sh
