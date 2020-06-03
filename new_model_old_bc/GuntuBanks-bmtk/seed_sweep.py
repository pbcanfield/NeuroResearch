import build_network
import update_config
import run_bionet
import generate_legacy_output

import os
import sys

import numpy as np
import random

import logging
logging.getLogger().setLevel(logging.INFO)

def run_seed(seed=479,experiment="0",simulation_config="simulation_config.json",skip_build=False):

    base_config = simulation_config
    spikes_file = "spikes.csv"
    legacy_outdir = 'legacy'

    logging.info("Running seed " + str(seed))
    network_dir = str(seed)+"_network"
    output_dir = str(seed)+"_output"
    sim_config = str(seed)+"_simulation_config.json"
    net_config = str(seed)+"_network_config.json"

    logging.info("Building Network")
    if not skip_build:
        build_network.build_hippocampus(output=network_dir,seed=seed,experiment=experiment)

    logging.info("Creating config files")
    update_config.update_config(base_config,
            new_simulation_config=sim_config,
            new_network_config=net_config,
            output=output_dir,network=network_dir)

    logging.info("Running simulation")
    try:
        run_bionet.run(sim_config,seed=seed,output=output_dir,Experiment=experiment)
    except SystemExit:
        pass

    spikes = os.path.join(output_dir,spikes_file)
    prefix = 'bmtk_'+str(seed)+"_"

    logging.info("Writing legacy output into dir\""+legacy_outdir+"\"")
    generate_legacy_output.generate_hummos_output(spikes,legacy_outdir,output_prefix=prefix)
    logging.info("Done")
    # From MATLAB run >> Correlation('bmtk_*_','../HummosBanks-bmtk/legacy/')
    # Stability({'bmtk_3001_'},'../HummosBanks-bmtk/legacy/') # OR SOMETHING SIMILAR

if __name__ == '__main__':
    if len(sys.argv)==5:#Really terrible, fix sometime
        run_seed(int(sys.argv[1]),sys.argv[2],sys.argv[3],skip_build = True)
    elif __file__ != sys.argv[-1]:
        run_seed(int(sys.argv[1]),sys.argv[2],sys.argv[3])
    else:
        run_seed()
