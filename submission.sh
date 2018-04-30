#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l

doGet () {
    leetcode submission "$1" -o submissions
}

while read -r line || [[ -n "$line" ]]
do
    doGet "$line"
done < problems.list
#~/loadrc/bashrc/jformat.sh
#autopep8 --in-place -r submissions/
#jdupes -1dNr submissions/
