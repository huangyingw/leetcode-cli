#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find ~/.lc -type f -name problems.json -delete
./backup.sh
./restore.sh

doGet () {
    leetcode user -l
    leetcode submission "$1" -o submissions
}

for (( c=1; c<=1500; c++ ))
do
    doGet "$c"
done
./remove_dup.sh
