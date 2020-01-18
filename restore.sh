#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rsync -aHv --progress \
    --exclude-from=./excludeFile \
    ../leetcode-cli.orig/submissions/ \
    ./submissions/
