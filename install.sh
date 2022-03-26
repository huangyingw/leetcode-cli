#!/bin/zsh -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rm -fr ~/.lc/
. ~/.nvm/nvm.sh
nvm install 13
./build.sh
./install_chrome_plugin.sh
leetcode user -l
