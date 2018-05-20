#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

~/loadrc/gitrc/gpl.sh
./remove_dup.sh
~/loadrc/bashrc/cscope.sh
git add .
~/loadrc/gitrc/g.sh
