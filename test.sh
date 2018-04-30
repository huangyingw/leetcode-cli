#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode test \
    ./submissions/104.maximum-depth-of-binary-tree.152193284.Wrong-Answer.leetcode.py \
    -t '[1,2,3,4,null,null,5]'
