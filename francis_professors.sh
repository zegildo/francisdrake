#!/bin/bash
if ! [ -x "$(command -v parallel)" ]; then
  echo 'Error: parallel is not installed.' >&2
  exit 1
fi

echo "\e[1;31m Normal professors catching... \e[0m"
cat inputs/departaments | time parallel --colsep ',' -j+0 --progress python scripts/professors_information.py {1} > output/professors_information.csv
echo "\e[1;31m Very Very special professors catching... \e[0m"
echo "\e[1;31m #############             (66%)\r \e[0m"
time python scripts/special_professors_information.py >> output/professors_information.csv
echo "\e[1;31m #######################   (100%)\r \e[0m"
echo "\e[1;31m Done! \e[0m"
