#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./remove_gabages.sh
find . -type f \( -name \*.orig -o -name \*.bak \) -delete
./backup.sh
jdupes -1dNr submissions/
