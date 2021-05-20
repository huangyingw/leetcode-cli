#!/bin/zsh -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rm -fr ~/.lc/leetcode/cache
. ~/.nvm/nvm.sh
nvm install 14
./build.sh
./install_chrome_plugin.sh
leetcode user -l
