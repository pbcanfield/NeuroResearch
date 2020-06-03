import glob, os, re, sys, math, random

import h5py
import numpy as np
from numpy import genfromtxt
import pandas as pd
import logging

def generate_exp0_input(input_dir='input',output_filename='exp0_input.csv', tstop=10000,
                        stim_interval=80, num_p1=10, num_p2=10):
    #https://github.com/tjbanks/bmtk/blob/develop/bmtk/utils/io/spike_trains.py
    stim_count = 16
    
    stim_space = tstop / stim_count 	#//625
    stim_dur_ratio = 250 / stim_space  	#//.4
    stim_space_ratio = stim_space / tstop 	#//0.0625
    
    stim_interval = 80
    # We want to apply the first set of stimulus to all cells in num_p1 and
    # apply the second set of stimulus to all cells in num_p2

    #for each j in stim_count
        #apply stim to each cell in num_p (if j<6 apply to cells 0-9, else cells 10-19)

    stim_number = (stim_space * stim_dur_ratio) / stim_interval
    stims = {}
    def apply_stim(stim_start, cell_ids):
        for cell in cell_ids:
            for spike_time in range(int(stim_start),int(stim_start+(stim_number*stim_interval)),int(stim_interval)):
                if not stims.get(cell):
                    stims[cell] = []
                stims[cell].append(spike_time)
                #spike_writer.add_spike(spike_time,cell)
        return

    for j in range(stim_count):
        stim_start = j * (stim_space)
        if j < 5:
            apply_stim(stim_start,[j for j in range(0,num_p1)])
        else:
            apply_stim(stim_start,[j for j in range(num_p1,num_p1+num_p2)])
    
    #spike_writer.to_csv(os.path.join(input_dir,output_filename),sort_order='gid')
    #Spikes must be in the format
    #gid spike-times
    #0 0,2,3,45,3
    #...
    #n 0
    #With all cell accounted for.

    with open(os.path.join(input_dir,output_filename),'w') as file:
        file.write('gid spike-times\n')
        for key, value in stims.items():
            file.write(str(key)+' '+','.join(str(x) for x in value)+'\n') 
    

def generate_exp0_input_new(input_dir='input',output_filename='exp0_input_new.csv', tstop=10000,
                        stim_interval=80, num_p1=10, num_p2=10):
    #https://github.com/tjbanks/bmtk/blob/develop/bmtk/utils/io/spike_trains.py
    stim_count = 16
    
    stim_space = tstop / stim_count 	#//625
    stim_dur_ratio = 250 / stim_space  	#//.4
    stim_space_ratio = stim_space / tstop 	#//0.0625
    
    stim_interval = 80
    # We want to apply the first set of stimulus to all cells in num_p1 and
    # apply the second set of stimulus to all cells in num_p2

    #for each j in stim_count
        #apply stim to each cell in num_p (if j<6 apply to cells 0-9, else cells 10-19)

    stim_number = (stim_space * stim_dur_ratio) / stim_interval
    stims = {}
    def apply_stim(stim_start, cell_ids):
        for cell in cell_ids:
            for spike_time in range(int(stim_start),int(stim_start+(stim_number*stim_interval)),int(stim_interval)):
                if not stims.get(cell):
                    stims[cell] = []
                stims[cell].append(spike_time)
                #spike_writer.add_spike(spike_time,cell)
        return

    for j in range(stim_count):
        stim_start = j * (stim_space)
        cell_set = [i for i in range(0,num_p1)]
        if j < 6:
            apply_stim(stim_start,cell_set)
        else:
            cell_set[:j-5] = [i for i in range(num_p1,num_p1+j-5)]
            apply_stim(stim_start,cell_set)
    
    #spike_writer.to_csv(os.path.join(input_dir,output_filename),sort_order='gid')
    #Spikes must be in the format
    #gid spike-times
    #0 0,2,3,45,3
    #...
    #n 0
    #With all cell accounted for.

    with open(os.path.join(input_dir,output_filename),'w') as file:
        file.write('gid spike-times\n')
        for key, value in stims.items():
            file.write(str(key)+' '+','.join(str(x) for x in value)+'\n') 

def generate_exp0_input_newest(input_dir='input',output_filename='exp0_input_newest.csv', tstop=10000,
                        stim_interval=80, num_p1=10, num_p2=10):
    #https://github.com/tjbanks/bmtk/blob/develop/bmtk/utils/io/spike_trains.py
    stim_count = 16

    stim_space = tstop / stim_count     #//625
    stim_dur_ratio = 250 / stim_space   #//.4
    stim_space_ratio = stim_space / tstop       #//0.0625

    stim_interval = 80
    # We want to apply the first set of stimulus to all cells in num_p1 and
    # apply the second set of stimulus to all cells in num_p2

    #for each j in stim_count
        #apply stim to each cell in num_p (if j<6 apply to cells 0-9, else cells 10-19)

    stim_number = (stim_space * stim_dur_ratio) / stim_interval
    stims = {}
    new_stims_list = []#{"timestamps":[],"node_ids":[]}
    
    def apply_stim(stim_start, cell_ids):
        for cell in cell_ids:
            for spike_time in range(int(stim_start),int(stim_start+(stim_number*stim_interval)),int(stim_interval)):
                if not stims.get(cell):
                    stims[cell] = []
                stims[cell].append(spike_time)
                spike = {"timestamps":spike_time,"node_ids":cell}
                new_stims_list.append(spike)
                #spike_writer.add_spike(spike_time,cell)
        return

    for j in range(stim_count):
        stim_start = j * (stim_space)
        cell_set = [i for i in range(0,num_p1)]
        if j < 6:
            apply_stim(stim_start,cell_set)
        else:
            cell_set[:j-5] = [i for i in range(num_p1,num_p1+j-5)]
            apply_stim(stim_start,cell_set)

    #spike_writer.to_csv(os.path.join(input_dir,output_filename),sort_order='gid')
    #Spikes must be in the format
    #gid spike-times
    #0 0,2,3,45,3
    #...
    #n 0
    #With all cell accounted for.

    #with open(os.path.join(input_dir,output_filename),'w') as file:
    #    file.write('gid spike-times\n')
    #    for key, value in stims.items():
    #        file.write(str(key)+' '+','.join(str(x) for x in value)+'\n')
    
    new_stims_df = pd.DataFrame(new_stims_list)
    new_stims_df = new_stims_df.sort_values(by=["timestamps"])[["timestamps","node_ids"]]
    
    path = os.path.join(input_dir,output_filename)
    new_stims_df.to_csv(path, index=False, sep=' ')

def generate_exp3_input(input_dir='input',CA3_filename='exp3_input_poisson_CA3.csv',
                        DG_filename='exp3_input_poisson_DG.csv',
                        EC_filename='exp3_input_EC.csv',
                        tstop=15000, stim_interval=80, num_EC=30, num_CA3=63, num_DG=384):
    CA3_stims = {}
    DG_stims = {}
    EC_stims = {}

    StimFreq = 12 #(Hz)
    StimCount = 30
    StimSpace = tstop / StimCount
    StimDurRatio = 0.5

    cells = [i for i in range(30)]
    random.shuffle(cells)


    input_pairs = [{"output_filename":CA3_filename, "stims":CA3_stims, "num_cells":num_CA3, "poisson":True},
                {"output_filename":DG_filename, "stims":DG_stims, "num_cells":num_DG, "poisson":True},
                {"output_filename":EC_filename, "stims":EC_stims, "num_cells":num_EC, "poisson":False}
    ]

    def gen_poisson(lambda_, T):
        train = []
        time = 0

        while (time < T):
            isi = - math.log( random.uniform(0,1) ) / lambda_
            time = time + isi
            if time < T:
                train.append(time)
        
        return train
    

    for pair in input_pairs:
        if pair["poisson"]:
            for ind in range(pair["num_cells"]):
                pair["stims"][ind] = gen_poisson(0.5/1000, tstop)
        else: # Increasing input section
            for j in range(StimCount):
                start = j * (StimSpace +1)
                for cell in cells[:j+1]:
                    if not pair["stims"].get(cell):
                        pair["stims"][cell] = []
                    pair["stims"][cell].append(start)

        with open(os.path.join(input_dir,pair["output_filename"]),'w') as file:
            file.write('gid spike-times\n')
            for key, value in pair["stims"].items():
                file.write(str(key)+' '+','.join(str(x) for x in value)+'\n')

    return

def generate_random_ec_input():
    '''
    For test to see EC response to random poison input at 15 hz
    '''

    from bmtk.utils.reports.spike_trains import PoissonSpikeGenerator
    
    psg = PoissonSpikeGenerator(population='hippocampus')
    psg.add(node_ids=range(0,30),  # Have nodes to match mthalamus
            firing_rate=15.0,    # 15 Hz, we can also pass in a nonhomoegenous function/array
            times=(0.0, 10.0))    # Firing starts at 0 s up to 10 s
    psg.to_sonata('ec_spikes.h5')
    logging.info("ec_spikes.h5 written")

def generate_sfn2019_input():
    from bmtk.utils.reports.spike_trains import PoissonSpikeGenerator

    psg = PoissonSpikeGenerator(population='hippocampus')
    for i in range(30):
        rate = abs(float(int(np.random.normal(50,40,1)[0])))+1
        print("Cell " + str(i) + " at rate " + str(rate))
        psg.add(node_ids=[i],
                firing_rate=rate,
                times=(0.0,3.0))
    psg.to_sonata('input/ec_gaus_50m_40s_hz.h5')
    print('input/ec_gaus_50m_40s_hz.h5 written')

    
    psg = PoissonSpikeGenerator(population='hippocampus')
    for i in range(30,93):
        rate = abs(float(int(np.random.normal(50,40,1)[0])))+1
        print("Cell " + str(i) + " at rate " + str(rate))
        psg.add(node_ids=[i],
                firing_rate=rate,
                times=(0.0,3.0))
    psg.to_sonata('input/ca3e_gaus_50m_40s_hz.h5')
    print('input/ca3e_gaus_50m_40s_hz.h5 written')

    psg = PoissonSpikeGenerator(population='hippocampus')
    rate = 15
    psg.add(node_ids=range(30,93),
            firing_rate=rate,
            times=(0.0,3.0))
    psg.to_sonata('input/ca3e_poisson_15hz.h5')
    print('input/ca3e_poisson_15hz.h5 written')    

    psg = PoissonSpikeGenerator(population='hippocampus')
    rate = 15
    psg.add(node_ids=range(0,29),
            firing_rate=rate,
            times=(0.0,3.0))
    psg.to_sonata('input/ec_poisson_15hz.h5')
    print('input/ec_poisson_15hz.h5 written')

if __name__ == '__main__':
    #generate_exp0_input()
    #generate_exp0_input_new()
    #generate_exp0_input_newest()
    #generate_exp3_input()
    #generate_random_ec_input()
    generate_sfn2019_input()
