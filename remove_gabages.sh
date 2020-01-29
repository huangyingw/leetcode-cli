#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

mkdir -p remove_comments
find ./submissions -type f -name \*.py | while read ss
do
    autopep8 --in-place "$ss"
    if $(~/loadrc/pythonrc/remove_comments.py "$ss")
    then
        mv -fv "$ss.strip" "$ss"
        sed -i.bak '/print.*(/d;/^_author_/d;/__main__/d;/ = Solution()/d;/^_project_/d;/\bprint\b/d;s/#--//g;s/##//g;s/ \/ /\/\//g;/^$/d;/^\s*$/d' "$ss"
        autopep8 --in-place "$ss"
    else
        rm "$ss.strip"
        mv -v "$ss" $(echo "$ss" | sed 's/submissions/remove_comments/g')
    fi
done
