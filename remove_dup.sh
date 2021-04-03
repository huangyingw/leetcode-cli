#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

# ./restore.sh
while true
do
    ./remove_gabages.sh
    find . -type f \( -name \*.orig -o -name \*.bak \) -delete
    jdupes -1dNr submissions/
done
