#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find ./submissions/ -type f -print0 | xargs -0 sed -i.bak '/print.*(/d;/^\s*$/d;/\bprint\b/d' 
