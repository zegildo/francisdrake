#!/bin/bash
if ! [ -x "$(command -v parallel)" ]; then
  echo 'Error: parallel is not installed.' >&2
  exit 1
fi

cat inputs/siapes | time parallel -j+0 --progress python scripts/professors_schedule.py {} 2> output/siapes_error > output/horarios_ufersa.csv