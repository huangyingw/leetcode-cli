#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

backup="../leetcode-cli.orig/submissions/"
mkdir -p "$backup"
rsync -aHv --progress \
    --ignore-existing \
    --exclude-from=./excludeFile \
    ./submissions/ \
    "$backup"
