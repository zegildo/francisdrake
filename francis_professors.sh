#!/bin/bash
if ! [ -x "$(command -v parallel)" ]; then
  echo 'Error: parallel is not installed.' >&2
  exit 1
fi
cat inputs/departaments | time parallel --colsep ',' -j+0 --progress python scripts/professors_information.py {1} > output/professors_information.csv
