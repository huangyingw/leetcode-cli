#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

./build.sh
leetcode user -l
leetcode submission -a -o submissions
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
jdupes -1dNr submissions/
