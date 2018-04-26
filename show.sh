#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh

doShow () {
    leetcode show "$1" -gx -l python -o ./show/
}

while read -r line || [[ -n "$line" ]]
do
    doShow "$line"
done < problems.list
