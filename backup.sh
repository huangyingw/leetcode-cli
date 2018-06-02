#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rsync -aHv --progress \
    --exclude-from=./excludeFile \
    ./submissions/ \
    ../leetcode-cli.bak/submissions/
