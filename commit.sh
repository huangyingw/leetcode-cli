#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./remove_dup.sh
cd ./submissions/
~/loadrc/gitrc/gci.sh
cd -
./restore.sh
