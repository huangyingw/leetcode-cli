#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode submission 1 -o submissions
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
