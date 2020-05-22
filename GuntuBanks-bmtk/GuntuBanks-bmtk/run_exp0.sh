#!/bin/bash
RANDOM=$$
for i in $(seq 10)
do
    python seed_sweep.py $RANDOM 0 simulation_config.json
done
