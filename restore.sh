#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rsync -aHv --progress \
    --ignore-existing \
    --exclude-from=./excludeFile \
    ./downloads/ \
    ./submissions/
