#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
jdupes -1dNr submissions/
