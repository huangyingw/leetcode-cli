#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

if [ $(uname) == "Darwin" ]
then
    echo -e "${red}It could only run in Linux... ${NC}"
    exit 1
fi

./remove_prints.sh
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
find . -type f -name \*.orig -delete
./backup.sh
jdupes -1dNr submissions/
