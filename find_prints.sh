#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

xargs grep -inH -- "print.*(" < ./files.proj | grep "./submissions/" | sed "s/:.*//g" | sort -u > ./find_prints.sh.bak
comm -23 <(sort ./find_prints.sh.bak) <(sort ./find_prints.ignore)
