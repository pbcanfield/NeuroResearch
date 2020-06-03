#!/bin/bash

if [ -z $1 ]; then
  echo ""
  echo "Use: ./sfn2019.sh [ABCDEF]"
  echo "Ex: ./sfn2019.sh A"
  echo ""
  echo "Experiment not specified, exiting."
  echo "A - CA3 disconnection, input supplied directly"
  echo "B - EC->CA3e case, input supplied to EC"
  echo "C - CA3e connected to one another, input supplied directly"
  echo "D - CA3e connected to OLM cells, input supplied directly"
  echo "E - CA3e connected to BC cells, input supplied directly"
  exit 0
fi

if [ -z $2 ]; then
  export SEED=100
else
  export SEED=$2
fi

echo "Using seed: $SEED"
echo ""

if [ $1 ==  "A" ]
  then
    echo "A - Executing CA3e pyramidal disconnection case"
    echo "All pyramidal cells are disconnected from everything"
    echo "Input is supplied directly to the pyramidal cells for analysis"
    python seed_sweep.py $SEED SFN19-A simulation_config_bg_ca3e_sfn.json 
    echo "Analysis (MATLAB from matlab_scripts folder): lfp('../$SEED""_output/ecp.h5',1)" 
    echo "Spike Spike based lfp -- lfpspk('../$SEED""/spikes.h5','hippocampus',1024)"
fi

if [ $1 ==  "B" ]
  then
    echo "B - Executing CA3e pyramidal and EC connection case"
    echo "EC is connected to CA3e pyramidal cells, pyramidal cells are disconnected from all"
    echo "Input supplied to EC"
    python seed_sweep.py $SEED SFN19-B simulation_config_bg_ec_sfn.json
    echo "Analysis (MATLAB from matlab_scripts folder): lfp('../$SEED""_output/ecp.h5',1)"
    echo "Spike Spike based lfp -- lfpspk('../$SEED""/spikes.h5','hippocampus',1024)"
fi

if [ $1 ==  "C" ]
  then
    echo "C - Executing CA3e pyramidal disconnection case"
    echo "Same as case A except CA3e pyramidal cells are connected to one another"
    echo "Input supplied to CA3e"
    python seed_sweep.py $SEED SFN19-C simulation_config_bg_ca3e_sfn.json
    echo "Analysis (MATLAB from matlab_scripts folder): lfp('../$SEED""_output/ecp.h5',1)"
    echo "Spike Spike based lfp -- lfpspk('../$SEED""/spikes.h5','hippocampus',1024)"
fi

if [ $1 ==  "D" ]
  then
    echo "D - Executing CA3e pyramidal connected to OLM cells, input supplied to CA3e"
    python seed_sweep.py $SEED SFN19-D simulation_config_bg_ca3e_sfn.json
    echo "Analysis (MATLAB from matlab_scripts folder): lfp('../$SEED""_output/ecp.h5',1)"
    echo "Spike Spike based lfp -- lfpspk('../$SEED""/spikes.h5','hippocampus',1024)"
fi

if [ $1 ==  "E" ]
  then
    echo "E - Executing CA3e pyramidal disconnection case"
    echo "E - Executing CA3e pyramidal connected to BC cells, input supplied to CA3e"
    python seed_sweep.py $SEED SFN19-E simulation_config_bg_ca3e_sfn.json
    echo "Analysis (MATLAB from matlab_scripts folder): lfp('../$SEED""_output/ecp.h5',1)"
    echo "Spike Spike based lfp -- lfpspk('../$SEED""/spikes.h5','hippocampus',1024)"
fi
