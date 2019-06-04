#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
./restore.sh
leetcode submission -a -o submissions
./remove_dup.sh
