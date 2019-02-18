#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

cd ./submissions
if [ -n "$(git status --porcelain)" ]
then
    echo -e "${red}the git repository is unclean, please check it before continuing... ${NC}"
    exit 1
fi
cd -

./remove_prints.sh
~/loadrc/bashrc/jformat.sh
autopep8 --in-place -r submissions/
find . -type f \( -name \*.orig -o -name \*.bak \) -delete
./backup.sh
jdupes -1dNr submissions/
