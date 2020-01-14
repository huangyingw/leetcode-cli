#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find ./submissions/ -type f -name \*.py | while read ss
do
    ~/loadrc/pythonrc/remove_comments.py "$ss"
    mv -fv "$ss.strip" "$ss"
    autopep8 --in-place "$ss"
    sed -i.bak '/print.*(/d;/^_author_/d;/^_project_/d;/\bprint\b/d;/\s*#/d;/^$/d;/^\s*$/d' "$ss"
done
