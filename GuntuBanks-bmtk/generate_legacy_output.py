import pandas as pd
import numpy as np
import os,pdb

def generate_hummos_output(filename,outdir,output_prefix='bmtk_'):
    
    cell_nums = [30,63,8,8,384,32,32]
    region = 'hippocampus'

    df = pd.read_csv(filename, delimiter=' ',)
    #df.rename(index=str, columns={0: "time", 2: "cell"},inplace=True)
    #df=df.reindex(columns=['cell','time'])
    df=df[df['population'] == region]
    df=df[["node_ids","timestamps"]]

    cell_start = np.cumsum(cell_nums)-cell_nums

    for i,start in enumerate(cell_start):
        begin = start
        if i+1 < len(cell_start):
            end = cell_start[i+1]
        else:
            end = cell_start[i]+cell_nums[-1] 

        df_sub = df[(df['node_ids'] >= begin ) & (df['node_ids'] < end )]

        df_sub['node_ids'] = df_sub['node_ids'] - start

        df_sub.sort_values(['timestamps'],inplace=True)
        df_sub.timestamps = df_sub.timestamps.round(1)
        
        outname = output_prefix + 'SpikeTime' + str(i) + '.txt'
        outpath = os.path.join(outdir,outname)
        df_sub.to_csv(outpath,header=None,index=False)

if __name__ == '__main__':
    generate_hummos_output('output/spikes.csv','legacy')
    # From MATLAB run Correlation('bmtk_','../HummosBanks-bmtk/legacy/')
    # in the original Hummos directory
