#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

if [ $(uname) == "Darwin" ]
then
    echo -e "${red}It could only run in Linux... ${NC}"
    exit 1
fi

cd ./submissions
git diff --quiet || exit 1
cd -

./remove_prints.sh
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
find . -type f \( -name \*.orig -o -name \*.bak \) -delete
./backup.sh
jdupes -1dNr submissions/
