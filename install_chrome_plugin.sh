#!/bin/zsh -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

leetcode plugin -D cookie.chrome
leetcode plugin -i cookie.chrome
