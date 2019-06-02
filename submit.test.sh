#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

git co test/1001_Grid_Illumination.py 
git co test/1342343283_Grid_Illumination.py 
git co submissions/101.symmetric-tree.204254047.Wrong-Answer.leetcode.py
leetcode submit -d ./test/1001_Grid_Illumination.py 
leetcode submit -d ./test/1342343283_Grid_Illumination.py 
leetcode submit -d ./submissions/101.symmetric-tree.204254047.Wrong-Answer.leetcode.py
