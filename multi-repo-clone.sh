#!/bin/bash
readarray array <<< "$( cat "$@" )"
DEV_ENV_PATH="D:\Work\HTWG Konstanz\Semester 6\Teamprojekt\Dev Space"
mkdir -p "$DEV_ENV_PATH" && cd "$DEV_ENV_PATH" || exit

for entry in "${array[@]}"
  do
    echo "cloning $entry"
    git clone $entry
  done
