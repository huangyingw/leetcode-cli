#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

cat files.proj | grep \/submissions\/.*.py | sed "s/\"//g" > files.proj.sort
xargs ls -altr < files.proj.sort
