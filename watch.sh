#!/bin/bash -
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

/usr/bin/watch ~/loadrc/bashrc/check_running.sh ./submission.sh
