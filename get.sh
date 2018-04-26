#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode submission 1 -o submissions
~/loadrc/bashrc/jformat.sh
jdupes -1dNr submissions/
autopep8 --in-place --aggressive --aggressive -r submissions/
