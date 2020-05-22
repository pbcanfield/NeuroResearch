import neuron
from neuron import h
import numpy as np
import pandas as pd
import sys
import random
  
def generate_noise(start,noise,number,interval,num_cells=1,tstop=100,cell_id_offset=0):
    TSTOP = tstop
    h("objref nil");
    
    netstims = []    
    netcons = []
    stims = []

    for i in range(num_cells):
        netstims.append(h.NetStim())
        netstims[i].start = start
        netstims[i].noise = noise
        netstims[i].number   = number 
        netstims[i].interval = interval

        netcons.append(h.NetCon(netstims[i], h.nil))
        stims.append(h.Vector())
        netcons[i].record(stims[i])

    h.finitialize()
    neuron.run(TSTOP)

    ret = None

    for i in range(num_cells):
        spikes = stims[i]
        spikes = np.array(spikes).reshape(-1,1)
        ids = (np.ones(len(spikes))*i+cell_id_offset).astype(int).reshape(-1,1)
        sid = np.concatenate((ids,spikes),axis=1)
        pdsid = pd.DataFrame(sid,columns=['node_ids','timestamps'])

        if ret is None:
            ret = pdsid
        else:
            ret = ret.append(pdsid, ignore_index=True)

    ret = ret.sort_values(by="timestamps")[["timestamps","node_ids"]]
    ret.node_ids = ret.node_ids.astype(int)
    return ret


def gen_exp0_noise(seed=479,ca3_cells=63,dg_cells=386,tstop=10000):

    random.seed(seed)
    
    #CA3
    start = 0
    noise = 1
    number = 1e100
    interval = 1000/1
    num_cells = ca3_cells
    stims = generate_noise(start,noise,number,interval,num_cells=num_cells,tstop=tstop)
    stims.to_csv('input/exp0_ca3_noise.csv',index=False,sep=' ')

    #DG
    start = 0
    noise = 1
    number = 1e100
    interval = 1000/3
    num_cells = dg_cells
    stims = generate_noise(start,noise,number,interval,num_cells=num_cells,tstop=tstop)
    stims.to_csv('input/exp0_dg_noise.csv',index=False,sep=' ')


if __name__ == '__main__':

    if len(sys.argv) == 2:
        gen_exp0_noise(int(sys.argv[1]))
    else:
        gen_exp0_noise()

