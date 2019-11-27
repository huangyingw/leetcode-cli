#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./remove_prints.sh
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
find . -type f \( -name \*.orig -o -name \*.bak \) -delete
./backup.sh
jdupes -1dNr submissions/
