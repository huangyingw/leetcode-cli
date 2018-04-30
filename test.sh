#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode test \
    /Users/huangyingw/Dropbox/myproject/git/interview/skygragon/leetcode-cli/show/104.maximum-depth-of-binary-tree.leetcode.py \
    -t '[1,2,3,4,null,null,5]'
