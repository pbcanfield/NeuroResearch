import glob, os, re, sys

import h5py
import numpy as np
from numpy import genfromtxt
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

from bmtk.analyzer.cell_vars import plot_report


def original_connection_totals(synapses_file):
    data = genfromtxt(synapses_file,delimiter=' ')
    cell_types = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb']
    total_cell_types = len(cell_types)
    cell_nums = [30,63,8,8,384,32,32]
    cell_start = [sum(cell_nums[:i]) for i,v in enumerate(cell_nums)]

    e_matrix = np.zeros((total_cell_types,total_cell_types))
    for i, row in enumerate(data):
        e_matrix[int(row[1]),int(row[3])]+=1

    return e_matrix, cell_types

def original_percent_connectivity(synapses_file):
    conn_totals, cell_types = original_connection_totals(synapses_file)
    
    cell_nums = [30,63,8,8,384,32,32]
    total_cell_types = len(cell_nums)

    max_connect = np.ones((total_cell_types,total_cell_types),dtype=np.float)

    for a, i in enumerate(cell_nums):
        for b, j in enumerate(cell_nums):
            max_connect[a,b] = i*j
    ret = conn_totals/max_connect
    ret = ret*100
    ret = np.around(ret, decimals=1)

    return ret, cell_types

def original_connection_divergence_average(synapses_file,convergence=False):
    conn_totals, cell_types = original_connection_totals(synapses_file)
    
    cell_nums = [30,63,8,8,384,32,32]
    total_cell_types = len(cell_nums)

    e_matrix = np.ones((total_cell_types,total_cell_types),dtype=np.float)

    for a, i in enumerate(cell_nums):
        for b, j in enumerate(cell_nums):
            c = b if convergence else a
            e_matrix[a,b] = conn_totals[a,b]/cell_nums[c]

    ret = np.around(e_matrix, decimals=1)

    return ret, cell_types

def plot_connection_info(data, labels, title):

    fig, ax = plt.subplots()
    im = ax.imshow(data)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)


    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(labels)):
        for j in range(len(labels)):
            text = ax.text(j, i, data[i, j],
                        ha="center", va="center", color="w")
    ax.set_ylabel('Source')
    ax.set_xlabel('Target')
    ax.set_title(title)
    fig.tight_layout()
    plt.show()
    return

def plot_raster(seed, files_dir='legacy', file_regex='_SpikeTime[0-6].txt'):
    """
    Author: Tyler Banks
    Loop through all spike files, create a list of when each cell spikes, plot.
    """
    #seed will be 667 for example
    files = glob.glob(os.path.join(files_dir,'bmtk_'+seed+file_regex))
    data = None
    
    cell_types = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb']#,'CA3noise','DGnoise']
    cell_nums = [30,63,8,8,384,32,32]#,63,384]
    d = [[] for _ in range(sum(cell_nums))]
    
    color_picker=['red','orange','yellow','green','blue','purple','black']#,'orange','blue']
    colors = []
    offset=0
    files.sort() 
    for n, file in enumerate(files):
        data = genfromtxt(file,delimiter=',')
        for i, row in enumerate(data):
            d[int(row[0])+offset].append(row[1])
        offset+=cell_nums[n]-1
        
    for i, n in enumerate(cell_nums):
        for _ in range(n):
            colors.append(color_picker[i])
        
    fig, axs = plt.subplots(1,1)
    axs.eventplot(d,colors=colors)
    axs.set_title('bmtk_'+seed+file_regex)
    axs.set_ylabel('Cell Number')
    axs.set_xlabel('Time (ms)')
    axs.legend(cell_types[::-1])
    
    leg = axs.get_legend()
    for i,c in enumerate(color_picker):
        leg.legendHandles[-i-1].set_color(c)
    
    plt.savefig('raster.png')
    
    plt.show()
    
    return

def print_avg_frequencies(spikesfile='479_output/spikes.csv', population='hippocampus'):
    cell_names = ['EC','CA3e', 'CA3o', 'CA3b', 'DGg', 'DGh', 'DGb']
    cell_nums = [30,63,8,8,384,32,32]
    cell_start = np.cumsum(cell_nums)-cell_nums
    
    df = pd.read_csv(spikesfile,delimiter=' ')
    df = df[df['population'] == population]
    df = df[['timestamps','node_ids']]
    
    spikeraster = np.array(df)
    
    bins = np.append(cell_start, cell_start[-1]+cell_nums[-1])
    
    pltarr = plt.hist(spikeraster[:,1],bins=bins)
    freq = pltarr[0]/cell_nums
    
    print(dict(zip(cell_names,list(freq))))
    

def plot_positions(files_dir='Outputs', file_regex='008sepsLoc*.txt'):
    """
    Author: Tyler Banks
    """
    files = glob.glob(os.path.join(files_dir,file_regex))
    data = None
    
    cell_types = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','Feng']
    cell_nums = [30,63,8,8,384,32,32,27001]
    d = [[] for _ in range(sum(cell_nums))]
    
    color_picker=['red','blue','orange','yellow','green','black','purple','pink']
    colors = []
    offset=0
    
    fig = plt.figure()
    ax = Axes3D(fig)
    handles = []

    for n, file in enumerate(files):
        data = genfromtxt(file,delimiter=' ')
        handle = ax.scatter(data[:,0],data[:,1],data[:,2],color=color_picker[n],label=cell_types[n])
        handles.append(handle)
    
    plt.title('Hummos Hippocampus')
    plt.legend(handles=handles)
    plt.show()
    
    return

def plot_lfp(output_dir, lfp_file='ecp.h5',channel=0):

    ecp_path = os.path.join(output_dir,lfp_file)
    
    f = h5py.File(ecp_path)
    lfp = list(f['ecp']['data'])
    lfp_arr = np.asarray(lfp)

    plt.figure()
    plt.plot(lfp_arr[:,channel])
    plt.show()


def plot_firing_rates(seed, cellGroup, files_dir='legacy', num_bins=30):
    '''
    Author: Pete Canfield
    Generate some statistics about the firing rates of each cell in the network.

    Arguments:
        1) The seed that you want to analyze.
        2) What group of cells do you want to look at in the network
        3) The directory with the spiking information
        4) The file naming structure.
        5) The number of bins to use for generating the histogram.
    '''
    cellGroups = ['EC','CA3e', 'CA3o', 'CA3b', 'DGg', 'DGh', 'DGb']
    cell_nums = [30,63,8,8,384,32,32]
    groupIndex = cellGroups.index(cellGroup)


    #Get all the files from the directory.
    file = open(os.path.join(files_dir,'bmtk_'+str(seed)+'_SpikeTime'+str(groupIndex)+'.txt'))


    #First check to see if all the cells in that cell fire.

    data = genfromtxt(file,delimiter=',', dtype=None)

    dontFire = []
    for cellId in range(cell_nums[groupIndex]):
        allFire = False
        for i in range(data.size):
            if(data[i][0] == cellId):
                allFire = True
                break
        if(not allFire):
            dontFire.append(cellId)
    
    print("Cells in group " + cellGroup + " that do not fire: ")
    print(dontFire)
    fireTimes = [data[i][1] for i in range(data.size)]

    fig, ax = plt.subplots()


    n, bins, patches = ax.hist(fireTimes,num_bins)
    ax.plot()
    ax.set_xlabel("Time")
    ax.set_ylabel("Number of " + cellGroup + " cells active")
    ax.set_title("Firing times of " + cellGroup + " cells.")
    
    fig.tight_layout()
    plt.show()



if __name__ == '__main__':

    #Example plot report https://github.com/AllenInstitute/bmtk/blob/develop/bmtk/analyzer/cell_vars.py
    #plot_report(config_file=None, report_file=None, report_name=None, variables=None, node_ids=None):
    #plot_report(config_file='100_output/100_simulation_config.json',node_ids=0)

    ### Hummos model ###   
    #data,labels = original_connection_totals('./Outputs/008sepsConnections.txt')
    #plot_connection_info(data, labels, 'Hummos Model Connection Totals')

    #data,labels = original_percent_connectivity('./008sepsConnections.txt')
    #plot_connection_info(data, labels, 'Hummos Model Connection Percentage')

    #data, labels = original_connection_divergence_average('./Outputs/008sepsConnections.txt',convergence=False)
    #plot_connection_info(data, labels, 'Hummos Model Average Divergence')

    #data, labels = original_connection_divergence_average('./Outputs/008sepsConnections.txt',convergence=True)
    #plot_connection_info(data, labels, 'Hummos Model Average Convergence')


    seed = sys.argv[1]
    #output_dir = seed + "_output"
    #plot_raster(seed)
    

    group = sys.argv[2]
    bins = int(sys.argv[3])
    plot_firing_rates(seed, group, num_bins=bins)
    #plot_lfp(output_dir)
    #print_average_frequencies('./legacy/'+seed+'_output/spikes.csv')


    #plot_positions()
