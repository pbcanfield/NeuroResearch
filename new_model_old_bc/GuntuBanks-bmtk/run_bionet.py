# -*- coding: utf-8 -*-

"""Simulates an example network of 14 cell receiving two kinds of exernal input as defined in configuration file"""
import synapses

import os, sys, random
from bmtk.simulator import bionet
from bmtk.simulator.bionet.default_setters.cell_models import loadHOC
import numpy as np
from neuron import h

def run(config_file, seed=None, output=None, Experiment=0):
    seed_default = 43 
    
    if seed:
        seed_default = seed
    
    random.seed(seed_default)

    #This is not needed in newer versions of BMTK
    bionet.pyfunction_cache.add_cell_model(loadHOC, directive='hoc', model_type='biophysical')
    synapses.load()

    #BE SURE dL is appropriate (https://github.com/AllenInstitute/bmtk/blob/develop/bmtk/simulator/bionet/biocell.py#L80)
    # This will divide your segments up incorrectly and cause problems for hoc code
    conf = bionet.Config.from_json(config_file, validate=True)

    if output:
        conf.output['output_dir'] = output

    conf.build_env()

    graph = bionet.BioNetwork.from_config(conf)
    sim = bionet.BioSimulator.from_config(conf, network=graph)
   
    
    cvode = sim.h.CVode()
    def Commands():
        if Experiment == "0":
            #///Stims /////////
            tstop_ = 10000 #//Make sure this matches the tstop, TODO: pull from config file
            StimCount = 16
            StimSpace = tstop_ / StimCount
            StimDurRatio = 250 / StimSpace
            StimSpaceRatio = StimSpace / tstop_

            print("Setting neuron values")
            sim.h.execute("ACHlevel = 1")
            sim.h.execute("Mods2 = ACHlevel")

            sim.h.execute("ACHe = 2")
            sim.h.execute("ACHc = 2")
            sim.h.execute("Plasticity = 1")
            sim.h.execute("ACH2 =Mods2")
            sim.h.execute("Da2 =Mods2")
            sim.h.execute("ACH =2")
            sim.h.execute("Da = 2")

            sim.h.execute("ACH_pyr2pyr = ACH")
            sim.h.execute("DA_pyr2pyr = Da")
            sim.h.execute("ACH_mossy = ACH")
            sim.h.execute("DA_mossy = Da")
            sim.h.execute("ACH_inter2pyr = ACH")
            sim.h.execute("ACH_IZH = ACH")
            sim.h.execute("DA_inter2pyr = Da")
            sim.h.execute("DA_IZH = Da")

            sim.h.execute("wACH = .05")

            def exp0_events():
                print('CVode Event Activated')
                sim.h.execute("LearningShutDown_pyr2pyr = 0")
                sim.h.execute("LearningShutDown_inter2pyr = 0")
                sim.h.execute("LearningShutDown_mossy = 0")

                sim.h.execute("ACH_IZH = ACH2")
                sim.h.execute("ACH_pyr2pyr = ACH2")
                sim.h.execute("ACH_mossy = ACH2")
                sim.h.execute("ACH_inter2pyr = ACH2")

                sim.h.execute("DA_pyr2pyr = Da2")
                sim.h.execute("DA_inter2pyr = Da2")
                sim.h.execute("DA_mossy = Da2")
                return

            effectTime = StimSpace * 5
            cvode.event(effectTime , exp0_events)

        elif Experiment == "3":
            sim.h.execute("ACH = Mods2")
            sim.h.execute("LearningShutDown_pyr2pyr = 0")
            sim.h.execute("LearningShutDown_inter2pyr = 0")
        else:
            sim.h.execute("ACHlevel = 1")
            sim.h.execute("Mods2 = ACHlevel")
            sim.h.execute("LearningShutDown_pyr2pyr = 0")
            sim.h.execute("LearningShutDown_inter2pyr = 0")
            sim.h.execute("LearningShutDown_mossy = 0")
    #https://www.neuron.yale.edu/phpbb/viewtopic.php?f=2&t=2236
    fih = []
    fih.append(sim.h.FInitializeHandler(0, Commands))
    
    sim.run()
    bionet.nrn.quit_execution()

if __name__ == '__main__':
    if __file__ != sys.argv[-1]:
        run(sys.argv[-1])
    else:
        run('simulation_config.json')
