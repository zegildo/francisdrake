#!/bin/bash
if ! [ -x "$(command -v parallel)" ]; then
  echo 'Error: parallel is not installed.' >&2
  exit 1
fi
cat inputs/siapes | time parallel -j+0 --progress python scripts/professors_schedule.py {} > output/horarios_ufersa.csv