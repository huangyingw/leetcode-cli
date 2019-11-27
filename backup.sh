#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

backup="../leetcode-cli.bak/submissions/"
mkdir -p "$backup"
rsync -aHv --progress \
    --exclude-from=./excludeFile \
    ./submissions/ \
    "$backup" 
