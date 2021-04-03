#!/bin/zsh -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

rm -fr ~/.lc/
./build.sh
./install_chrome_plugin.sh
