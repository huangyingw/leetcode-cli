#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode user -l

doTag () {
    leetcode list -q L -t "$1" > tags/"$1".md
}

while read -r line || [[ -n "$line" ]]
do
    doTag "$line"
done < companies.list

while read -r line || [[ -n "$line" ]]
do
    doTag "$line"
done < tags.list
