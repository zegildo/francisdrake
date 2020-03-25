#!/bin/bash
if ! [ -x "$(command -v parallel)" ]; then
  echo 'Error: parallel is not installed.' >&2
  exit 1
fi

echo "\e[1;31m Normal professors catching... \e[0m"
cat inputs/departaments | time parallel --colsep ',' -j+0 --progress python3 scripts/professors_information.py {1} > output/professors_information.csv
echo "\e[1;31m Very Very special professors catching... \e[0m"
time python3 scripts/special_professors_information.py >> output/professors_information.csv
echo "\e[1;31m Atualizando SIAPES... \e[0m"
time awk -F"," '{print $1}' output/professors_information.csv | python3 scripts/update_siapes.py
echo "\e[1;31m Arquivo de Siapes Atualizado! \e[0m"
echo "\e[1;31m Done! \e[0m"
