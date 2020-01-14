#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

cd remove_comments
~/loadrc/gitrc/grsh.sh
find . -type f -name \*.py | while read ss
do
    ~/loadrc/pythonrc/remove_comments.py "$ss"
    mv -fv "$ss.strip" "$ss"
    autopep8 --in-place -r "$ss"
    sed -i.bak '/print.*(/d;/^_author_/d;/^_project_/d;/\bprint\b/d;/^$/d;/^\s*$/d' "$ss"
done
git add .
