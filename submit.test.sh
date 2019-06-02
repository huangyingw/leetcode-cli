#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

git co test/1001_Grid_Illumination.py 
leetcode submit -d ./test/1001_Grid_Illumination.py
