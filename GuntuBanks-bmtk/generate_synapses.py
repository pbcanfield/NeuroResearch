#Convert Hummos Synapses.txt to BMTK JSONs
import json
import numpy as np
import pandas as pd
import os

synapse_hummos = '../HummosTheta/Inputs/Synapses.txt'
synapse_json_dir = './biophys_components/synaptic_models/'

s = pd.read_csv(synapse_hummos ,delimiter='\t',header=None)
src = s[:1].values.tolist()[0]
trg = s[1:2].values.tolist()[0]
z = []
for x,y in zip(src,trg):
    z.append(x+'2'+y)

s.loc[-1] = z  # adding a row
s.index = s.index + 1  # shifting index
s = s.sort_index()  # sorting by index

s = s.T #Transpose

new_head = s.iloc[0] # get first row
s = s[1:] #take data less the header row
s.columns = new_head # set header

#s.reindex(index=np.roll(s.index,3))


for index, row in s.iterrows():
    #Connect.hoc:50
    
    #exc
    esyn = {}
    esyn["level_of_detail"] = "pyr2pyr" #located on position 0.9 of the pre soma
    esyn["AlphaTmax_ampa"] = row[21+3]
    esyn["Beta_ampa"] = row[22+3]
    esyn["Cdur_ampa"] = row[23+3]
    esyn["gbar_ampa"] = row[24+3]
    esyn["Erev_ampa"] = row[16+3]
    esyn["AlphaTmax_nmda"] = row[25+3]
    esyn["Beta_nmda"] = row[26+3]
    esyn["Cdur_nmda"] = row[27+3]
    esyn["gbar_nmda"] = row[28+3]
    esyn["Erev_nmda"] = row[16+3]
    
    #inh    
    isyn = {}
    isyn["level_of_detail"] = "inter2pyr" #located on position 0.9 of the pre soma
    isyn["AlphaTmax_gabaa"] = row[21+3]
    isyn["Beta_gabaa"] = row[22+3]
    isyn["Cdur_gabaa"] = row[23+3]
    isyn["gbar_gabaa"] = row[24+3]
    isyn["Erev_gabaa"] = row[16+3]
    isyn["AlphaTmax_gabab"] = row[25+3]
    isyn["Beta_gabab"] = row[26+3]
    isyn["Cdur_gabab"] = row[27+3]
    isyn["gbar_gabab"] = row[28+3]
    isyn["Erev_gabab"] = row[16+3]  
         
    #syn common
    syn = {}
    syn["initW"] = row[0+3] #lsyn.initW = par.x(0) * rC.uniform(0.5,1.0)//rand.normal(0.5,1.5) //`rand.repick() 
    
    syn["Wmax"] = row[1+3] #lsyn.Wmax = par.x(1) * lsyn.initW
    syn["Wmin"] = row[2+3] #lsyn.Wmin = par.x(2) * lsyn.initW
    syn["delay"] = row[3+3] #delay = par.x(3) + delayDistance
    syn["con_pattern"] = row[5+3]

    #syn["netcon"] = row[0+3] #lcon = new NetCon(&v(0.5), lsyn, 0, delay, 1)
    
    syn["lambda1"] = row[6+3] #lsyn.lambda1 = par.x(6)
    syn["lambda2"] = row[7+3] #lsyn.lambda2 = par.x(7)
    syn["threshold1"] = row[8+3] #lsyn.threshold1 = par.x(8)
    syn["threshold2"] = row[9+3] #lsyn.threshold2 = par.x(9)
    syn["tauD1"] = row[10+3] #lsyn.tauD1 = par.x(10)
    syn["d1"] = row[11+3] #lsyn.d1 = par.x(11)
    syn["tauD2"] = row[12+3] #lsyn.tauD2 = par.x(12)
    syn["d2"] = row[13+3] #lsyn.d2 = par.x(13)
    syn["tauF"] = row[14+3] #lsyn.tauF = par.x(14)
    syn["f"] = row[15+3] #lsyn.f = par.x(15)
    
    syn["bACH"] = row[17+3] #lsyn.bACH = par.x(17)
    syn["aDA"] = row[18+3] #lsyn.aDA = par.x(18)
    syn["bDA"] = row[19+3] #lsyn.bDA = par.x(19)
    syn["wACH"] = row[20+3] #lsyn.wACH = par.x(20)

    syn["ratio"] = row[4+3]
    syn["gaussa"] = row[29+3]
    
    esyn.update(syn)#append common
    isyn.update(syn)#append common
    
    #Write to json files
    
    #excitatory
    filename = row[0] + '.exc.json'
    path = os.path.join('./biophys_components/synaptic_models',filename)
    with open(path, 'w') as fp:
        json.dump(esyn,fp,indent=4)
    
    #inhibitory
    filename = row[0] + '.inh.json'
    path = os.path.join('./biophys_components/synaptic_models',filename)
    with open(path, 'w') as fp:
        json.dump(isyn,fp,indent=4)
    

"""
Notes:
ConnectAreas given pre,post, pre2postindex_insynapses, type, ex=1inh=0
Totals = Number of neurons for each area
for each neuron in the pre area
    for each neuron in the post area
        find euclid distance between each cell
        based on connectionPattern chosen calculate a probability
        if random prob < prob
            calculate distance delay
            append delays to del array
            ConnectNeurons given preareaIndex,preCellindex,postAreaIndex,postCellindex,preCellObj,postCellObj,type(inh/exc),columnFromSynapse.txt,distdelay

ConnectNeurons
#All indices are shifted by +3 due to S2T,Source,Target at beginning of row
"""
