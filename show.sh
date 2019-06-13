#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find ~/.lc -type f -name problems.json -delete
rm ./show/*.py
leetcode show -a -gx -l python -o ./show/
