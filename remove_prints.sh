#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

resultFile="find_prints.sh.findresult"
xargs grep -inH -- "print.*(" < ./files.proj | grep "./submissions/" | sed "s/:.*//g" | sort -u | tee "$resultFile"

while read ss
do
    ss=$(echo $ss | sed  -e "s/\//\\\\\//g")
    sed -i.bak "/$ss/d" "$resultFile"
done < find_prints.ignore
