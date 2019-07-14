#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

cat files.proj | grep \/submissions\/.*.py | sed "s/\"//g" > files.proj.sort

IFS=$'\r\n' GLOBIGNORE='*' command eval  'files=($(cat files.proj.sort))'

for f in "${files[@]}"
do
    echo $(gstat -c %w -- "$f")$'\t'"$f"
done | sort -nk1,1
