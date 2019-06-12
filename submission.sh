#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
./restore.sh

doGet () {
    leetcode user -l
    leetcode submission "$1" -o submissions
}

while read -r line || [[ -n "$line" ]]
do
    doGet "$line"
done < problems.list
./remove_dup.sh
