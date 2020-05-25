#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find ~/.lc -type f -name problems.json -delete

doGet () {
    leetcode user -l
    leetcode submission "$1" -o downloads
}

while true
do
    for (( c=1; c<=1500; c++ ))
    do
        doGet "$c"
    done
    ./restore.sh
done
