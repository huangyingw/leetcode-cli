#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./backup_orig.sh
./remove_gabages.sh
find . -type f \( -name \*.orig -o -name \*.bak \) -delete
jdupes -1dNr submissions/
./backup.sh
