#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
rm  ./show/*.py
rm -fr ~/.lc/leetcode/cache/*.json

doShow () {
    leetcode show "$1" -gx -l python -o ./show/
}

while read -r line || [[ -n "$line" ]]
do
    doShow "$line"
done < problems.list
autopep8 --in-place -r show/
