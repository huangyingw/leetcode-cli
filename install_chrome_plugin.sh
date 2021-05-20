#!/bin/zsh -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

# ./bin/leetcode plugin -D cookie.chrome
./bin/leetcode plugin -i cookie.chrome
