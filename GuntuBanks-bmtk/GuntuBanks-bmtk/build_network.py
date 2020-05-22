"""
Author: Tyler Banks
Date: 3/9/2019

"""
import cell_positions as p
import synapses

from bmtk.builder.auxi.edge_connectors import distance_connector, connect_random
from bmtk.builder.networks import NetworkBuilder
import math
import numpy as np
import random

def build_hippocampus(output='network', seed=None, experiment="0"):
    
    seed_default =2001 #Not variable anymore to prevent bad networks (Feng recommended)
    
    random.seed(seed_default)
    #np.random.seed(seed_default)

    #initialize the networks
    net = NetworkBuilder('hippocampus')
    exp0net = NetworkBuilder('exp0input')
    
    ###########################################################
    # Build node locations
    ###########################################################
    
    #define cell numbers
    inpTotal = 30 # EC
    excTotal = 63 # CA3 principal
    CA3oTotal = 8
    CA3bTotal  = 8
    DGexcTotal = 384 
    DGbTotal = 32
    DGhTotal = 32

    #get cell positions
    p_EC = p.pos_EC()
    p_CA3e = p.pos_CA3e()
    p_CA3o = p.pos_CA3o()
    p_CA3b = p.pos_CA3b()
    p_DGg = p.pos_DGg()
    p_DGh = p.pos_DGh()
    p_DGb = p.pos_DGb()

    #verify cell numbers match cell position list sizes
    assert len(p_EC) == inpTotal
    assert len(p_CA3e) == excTotal
    assert len(p_CA3o) == CA3oTotal
    assert len(p_CA3b) == CA3bTotal
    assert len(p_DGg) == DGexcTotal
    assert len(p_DGh) == DGhTotal
    assert len(p_DGb) == DGbTotal

    ###########################################################
    # Experiment Logic
    ###########################################################

    build_node = {}
    build_edge = {}
    nodes = []
    edges = []

    # NODES TO BE BUILT
    build_node['EC'] = False
    build_node['CA3e'] = False
    build_node['CA3o'] = False
    build_node['CA3b'] = False
    build_node['DGg'] = False
    build_node['DGh'] = False
    build_node['DGb'] = False
    build_node['exp0pat1'] = False
    build_node['exp0pat2'] = False
    build_node['bgnoisenodesCA3'] = False
    build_node['bgnoisenodesDG'] = False
    build_node['bgnoisenodesEC'] = False
    
    #EDGES TO BE BUILT
    build_edge['EC->CA3e'] = False
    build_edge['EC->CA3b'] = False
    build_edge['DGg->CA3b'] = False
    build_edge['CA3e->CA3e'] = False
    build_edge['CA3e->CA3b'] = False
    build_edge['CA3o->CA3e'] = False
    build_edge['CA3b->CA3e'] = False
    build_edge['CA3b->CA3o'] = False
    build_edge['EC->DGg'] = False
    build_edge['EC->DGb'] = False
    build_edge['DGg->DGb'] = False
    build_edge['DGh->DGg'] = False
    build_edge['DGb->DGg'] = False
    build_edge['DGb->DGh'] = False
    build_edge['CA3e->CA3o'] = False #RECURRENT
    build_edge['DGg->DGh'] = False #RECURRENT
    build_edge['DGg->CA3e'] = False #MOSSY FIBERS

    build_edge['bgnoisenodesCA3->CA3e'] = False
    build_edge['bgnoisenodesDG->DGg'] = False
    build_edge['bgnoisenodesEC->EC'] = False
    build_edge['bgnoisevirtCA3->CA3e'] = False

    build_edge['exp0pat1->EC'] = False
    build_edge['exp0pat2->EC'] = False

    #EXPERIMENTS - Add the nodes and edges you want for each experiment
    if experiment == "0": #DEFAULT EXPERIMENT WITH ALL (main) NODES
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC','bgnoisevirtCA3']
        edges = [
                 'EC->CA3e','EC->CA3b',                     #EC -> CA3
                 'DGg->CA3b',                               #DGg
                 'CA3e->CA3e','CA3e->CA3b',                 #CA3e
                 'CA3o->CA3e',                              #CA3o
                 'CA3b->CA3e','CA3b->CA3o',                 #CA3b
                 'EC->DGg','EC->DGb',                       #EC -> DG
                 'DGg->DGb',                                #DGg
                 'DGh->DGg',                                #DGh
                 'DGb->DGg','DGb->DGh',                     #DGb
                 'CA3e->CA3o',                              #CA3 RECURRENT
                 'DGg->DGh',                                #DG RECURRENT
                 'DGg->CA3e',                               #DG CA3 MOSSY FIBERS
                 'bgnoisenodesCA3->CA3e',                   #CA3e background noise (INTEGRATE AND FIRE)
                 'bgnoisenodesDG->DGg',                     #DGg background noise (INTEGRATE AND FIRE)
                 'exp0pat1->EC',                            #Pattern separation completion nodes to EC pat1
                 'exp0pat2->EC',                            #Pattern separation completion nodes to EC pat2
                 'bgnoisenodesEC->EC',                      #EC background noise (INTEGRATE AND FIRE)
                 'bgnoisevirtCA3->CA3'                      #CA3 input directly from virtual cells, not integrate and fire
        ]


    #SFN19 Experiments figure 2 of the the poster, keep EC in all experiments to keep CA3e cell numbers consistent, EC unused in some.
    if experiment == "SFN19-A":
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC']
        edges = [
                 'bgnoisenodesCA3->CA3e'                    #CA3e background noise
                ]
    
    if experiment == "SFN19-B":
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC']
        edges = [
                 'EC->CA3e',                                #EC -> CA3
                 'bgnoisenodesEC->EC'                       #EC background noise
                ]

    if experiment == "SFN19-C":
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC']
        edges = [ 
                 'CA3e->CA3e',                              #CA3e
                 'bgnoisenodesCA3->CA3e'                    #CA3e background noise
                ]

    if experiment == "SFN19-D":
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC']
        edges = [
                 'CA3o->CA3e',                              #CA3o
                 'CA3e->CA3o',                              #CA3 RECURRENT
                 'bgnoisevirtCA3->CA3e'                     #CA3e background noise
                ]

    if experiment == "SFN19-E":
        nodes = ['EC','CA3e','CA3o','CA3b','DGg','DGh','DGb','exp0pat1','exp0pat2','bgnoisenodesCA3','bgnoisenodesDG','bgnoisenodesEC']
        edges = [
                 'CA3e->CA3b',                              #CA3e
                 'CA3b->CA3e',                              #CA3b
                 'bgnoisenodesCA3->CA3e'                    #CA3e background noise
                ]

    #MERGE -- nodes and edges specified will be built
    build_node.update(dict.fromkeys(nodes, True))
    build_edge.update(dict.fromkeys(edges, True))

    ###########################################################
    # Build nodes
    ###########################################################

    #Add noteds to the network
    if build_node['EC']:
        net.add_nodes(N=inpTotal, pop_name='EC', pop_group='EC',
                    positions=p_EC,
                    model_type='biophysical',
                    model_template='hoc:IzhiCell_EC2',
                    morphology='blank.swc'
                    )

    if build_node['CA3e']:
        net.add_nodes(N=excTotal, pop_name='CA3e', pop_group='CA3',
                    positions=p_CA3e,
                    model_type='biophysical',
                    model_template='hoc:CA3PyramidalCell',
                    morphology='blank.swc'
                )

    if build_node['CA3o']:
        net.add_nodes(N=CA3oTotal, pop_name='CA3o', pop_group='CA3',
                positions=p_CA3o,
                model_type='biophysical',
                model_template='hoc:IzhiCell_OLM',
                    morphology='blank.swc'
                    )

    if build_node['CA3b']:
        net.add_nodes(N=CA3bTotal, pop_name='CA3b', pop_group='CA3',
                    positions=p_CA3b,
                    model_type='biophysical',
                    model_template='hoc:IzhiCell_BC',
                    morphology='blank.swc'
                    )

    if build_node['DGg']:
        net.add_nodes(N=DGexcTotal, pop_name='DGg', pop_group='DG',
                    positions=p_DGg,
                    model_type='biophysical',
                    model_template='hoc:DGCell',
                    morphology='blank.swc'
                    )

    if build_node['DGh']:
        net.add_nodes(N=DGhTotal, pop_name='DGh', pop_group='DG',
                positions=p_DGh,
                    model_type='biophysical',
                    model_template='hoc:IzhiCell_OLM',
                    morphology='blank.swc'
                    )

    if build_node['DGb']:
        net.add_nodes(N=DGbTotal, pop_name='DGb', pop_group='DG',
                    positions=p_DGb,
                    model_type='biophysical',
                    model_template='hoc:IzhiCell_BC',
                    morphology='blank.swc'
                    )
    if build_node['exp0pat1']:
        exp0net.add_nodes(N=10, model_type='virtual', pat='pat1',exp="0",pop_name='exp0pat1', pop_group='exp0pat1')
    if build_node['exp0pat2']:
        exp0net.add_nodes(N=10, model_type='virtual', pat='pat2',exp="0",pop_name='exp0pat2', pop_group='exp0pat2')


    if build_node['bgnoisenodesCA3']: #TWO SETS OF NODES NEEDED
        net.add_nodes(N=excTotal, model_template='nrn:IntFire1', model_type='point_process',
            dynamics_params="background2CA3_IntFire1Netstim.json", pop_name='bgnoisenodesCA3', pop_group='bgnoisenodesCA3')

        exp0net.add_nodes(N=excTotal, model_type='virtual', pop_name='bgnoisevirtCA3', pop_group='bgnoisevirtCA3')

    if build_node['bgnoisenodesDG']: #TWO SETS OF NODES NEEDED
        net.add_nodes(N=DGexcTotal, model_template='nrn:IntFire1', model_type='point_process',
            dynamics_params="background2DG_IntFire1Netstim.json", pop_name='bgnoisenodesDG', pop_group='bgnoisenodesDG')   

        exp0net.add_nodes(N=DGexcTotal, model_type='virtual', pop_name='bgnoisevirtDG', pop_group='bgnoisevirtDG') 

    if build_node['bgnoisenodesEC']:
        net.add_nodes(N=inpTotal, model_template='nrn:IntFire1', model_type='point_process',
            dynamics_params="background2CA3_IntFire1Netstim.json", pop_name='bgnoisenodesEC', pop_group='bgnoisenodesEC')

        exp0net.add_nodes(N=inpTotal, model_type='virtual', pop_name='bgnoisevirtEC', pop_group='bgnoisevirtEC')


    ###########################################################
    # Build custom synapses
    ###########################################################
    #See https://github.com/AllenInstitute/bmtk/blob/develop/bmtk/simulator/bionet/default_setters/synapse_models.py

    synapses.load()
    syn = synapses.syn_params_dicts()
    syn_list = []

    ###########################################################
    # Build custom connection rules
    ###########################################################
    #See bmtk.builder.auxi.edge_connectors
    def hipp_dist_connector(source, target, con_pattern, ratio=1, gaussa=0, min_syn=1, max_syn=1):
        """
        :returns: number of synapses per connection

        #Original Hoc Code:

        dx = Locs.o(postArea).x[0][m] - Locs.o(preArea).x[0][b]
        dy = Locs.o(postArea).x[1][m] - Locs.o(preArea).x[1][b]
        
        if ((Locs.o(preArea).nrow + Locs.o(postArea).nrow) > 5) {
            dz = Locs.o(postArea).x[2][m] - Locs.o(preArea).x[2][b]
            dist = sqrt(dx^2 + dy^2 + dz^2) 
            distxy = sqrt(dx^2 + dy^2)
        } else {
            dist = sqrt(dx^2 + dy^2)
            distxy = dist
        }

        // Lamellar. 
            //prob = prob =	 par.x(4) /(1+(1-exp(-abs(dx)^2/3)))	
        // pyr-int feedback loop. Has to be the same loop. Or the same seed? Theoritically I can connect pyr to int, same #the seed and then go through the same seed and loop to connect int to pyr.  
            // it shoudl be based off of interneuron axonal plexus.
        // Random. Turn off the dist component.
            //prob = par.x(4)
        // Mossy  (If 30 of CA3 cells are active, then a recruited gc have a 50% chance of recruiting a new CA3 neuron)
        // within axonal plexus.
        // prob = par.x(4)/dist
                calc dist 
        if (ConPattern == Lamellar) {
            prob =	 par.x(4)/ (exp( ((abs(dx) -0)^2)/ (2 * (3^2)))) //par4 is ratio
        }
        if (ConPattern == Homogenous) {
            prob =	 par.x(4) 			//par4 is ratio 	
        }
        if (ConPattern == IntPyrFeedback || ConPattern == AxonalPlexus) {
            c = par.x(4)
            a = par.x(29) //par29 is GaussA
           
           prob =	 a /(exp( ((abs(distxy) -0)^2)/ (2 * (c^2))))	
        """
        ratio = float(ratio)
        gaussa = float(gaussa)

        Lamellar = "0"
        Homogenous = "1"
        AxonalPlexus = "2"
        IntPyrFeedback = "3"
        
        x_ind,y_ind = 0,1
        dx = target['positions'][x_ind] - source['positions'][x_ind]
        dy = target['positions'][y_ind] - source['positions'][y_ind]
        distxy = math.sqrt(dx**2 + dy**2)
        prob = 1

        if con_pattern == Lamellar:
            prob = ratio/(math.exp(((abs(dx)-0)**2)/(2*(3**2))))
        if con_pattern == Homogenous:
            prob = ratio
        if con_pattern == IntPyrFeedback or con_pattern == AxonalPlexus:
            c = ratio
            a = gaussa
            prob = a /(math.exp(((abs(distxy)-0)**2)/(2*(c**2))))

        if random.random() < prob:
            #Since there will be recurrect connections we need to keep track externally to BMTK
            #BMTK will call build_edges twice if we use net.edges() before net.build()
            #Resulting in double the edge count
            syn_list.append({'source_gid':source['node_id'],'target_gid':target['node_id']})
            return random.randint(min_syn,max_syn)
        else:
            return 0

    ###########################################################
    # Build individual edge properties
    ###########################################################
    #Individual edge properties (See bmtk.docs.tutorials.NetworkBuilder_Intro.ipynb)

    def syn_dist_delay(source, target, base_delay, dist_delay=None):#, min_weight, max_weight):
        """
        Original Code:
        distDelay = 0.1* (0.5*dist + rC.normal(0,1.5)*(1-exp(-dist^2/3)) ) 
        """
        base_delay = float(base_delay)
        if dist_delay:
            dist_delay = float(dist_delay)

        if dist_delay: #An override of sorts
            return base_delay + dist_delay

        x_ind,y_ind,z_ind = 0,1,2
        
        dx = target['positions'][x_ind] - source['positions'][x_ind]
        dy = target['positions'][y_ind] - source['positions'][y_ind]
        dz = target['positions'][z_ind] - source['positions'][z_ind]

        dist = math.sqrt(dx**2 + dy**2 + dz**2)
        distDelay = 0.1* (0.5*dist + np.random.normal(0,1.5,1)[0]*(1-math.exp(-dist**2/3)) ) 
        return float(base_delay) + distDelay

    def syn_dist_delay_section(source, target, base_delay, dist_delay=None, sec_id=0, sec_x=0.9):
        return syn_dist_delay(source, target, base_delay, dist_delay), sec_id, sec_x

    ###########################################################
    # Build connections
    ###########################################################
    #sec_id, sec_x -> https://github.com/tjbanks/bmtk/blob/develop/docs/examples/bio_450cells_exact/build_network.py

    #Connect EC->CA3e Excitatory
    if build_edge['EC->CA3e']:
        dynamics_file = 'EC2CA3e.exc.json'
        conn = net.add_edges(source={'pop_name': 'EC'}, target={'pop_name': 'CA3e'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        #The following runs into issues... There seems to be a problem calling add_properties twice
        #conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])
        #conn.add_properties('delay', 
        #            rule=syn_dist_delay,
        #            rule_params={'base_delay':syn[dynamics_file]['delay']},
        #            dtypes=np.float)
        #Fix by calling one function to return all you need
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect EC->CA3b Excitatory
    if build_edge['EC->CA3b']:
        dynamics_file = 'EC2CA3b.exc.json'
        conn = net.add_edges(source={'pop_name': 'EC'}, target={'pop_name': 'CA3b'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGg->CA3b Excitatory
    if build_edge['DGg->CA3b']:
        dynamics_file = 'DGg2CA3b.exc.json'
        conn = net.add_edges(source={'pop_name': 'DGg'}, target={'pop_name': 'CA3b'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect CA3e->CA3e Excitatory
    if build_edge['CA3e->CA3e']:
        dynamics_file = 'CA3e2CA3e.exc.json'
        conn = net.add_edges(source={'pop_name': 'CA3e'}, target={'pop_name': 'CA3e'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect CA3e->CA3b Excitatory
    if build_edge['CA3e->CA3b']:
        dynamics_file = 'CA3e2CA3b.exc.json'
        conn = net.add_edges(source={'pop_name': 'CA3e'}, target={'pop_name': 'CA3b'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect CA3o->CA3e Inhibitory
    if build_edge['CA3o->CA3e']:
        dynamics_file = 'CA3o2CA3e.inh.json'
        conn = net.add_edges(source={'pop_name': 'CA3o'}, target={'pop_name': 'CA3e'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect CA3b->CA3e Inhibitory
    if build_edge['CA3b->CA3e']:
        dynamics_file = 'CA3b2CA3e.inh.json'
        conn = net.add_edges(source={'pop_name': 'CA3b'}, target={'pop_name': 'CA3e'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect CA3b->CA3o Inhibitory
    if build_edge['CA3b->CA3o']:
        dynamics_file = 'CA3e2CA3e.inh.json'
        conn = net.add_edges(source={'pop_name': 'CA3b'}, target={'pop_name': 'CA3o'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect EC->DGg Excitatory
    if build_edge['EC->DGg']:
        dynamics_file = 'EC2DGg.exc.json'
        conn = net.add_edges(source={'pop_name': 'EC'}, target={'pop_name': 'DGg'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect EC->DGb Excitatory
    if build_edge['EC->DGb']:
        dynamics_file = 'EC2DGb.exc.json'
        conn = net.add_edges(source={'pop_name': 'EC'}, target={'pop_name': 'DGb'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGg->DGb Excitatory
    if build_edge['DGg->DGb']:
        dynamics_file = 'DGg2DGb.exc.json'
        conn = net.add_edges(source={'pop_name': 'DGg'}, target={'pop_name': 'DGb'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGh->DGg Inhibitory
    if build_edge['DGh->DGg']:
        dynamics_file = 'DGh2DGg.inh.json'
        conn = net.add_edges(source={'pop_name': 'DGh'}, target={'pop_name': 'DGg'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGb->DGg Inhibitory
    if build_edge['DGb->DGg']:
        dynamics_file = 'DGb2DGg.inh.json'
        conn = net.add_edges(source={'pop_name': 'DGb'}, target={'pop_name': 'DGg'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGb->DGh Inhibitory
    if build_edge['DGb->DGh']:
        dynamics_file = 'DGb2DGh.inh.json'
        conn = net.add_edges(source={'pop_name': 'DGb'}, target={'pop_name': 'DGh'},
                    connection_rule=hipp_dist_connector,
                    connection_params={'con_pattern':syn[dynamics_file]['con_pattern'],
                                    'ratio':syn[dynamics_file]['ratio'],
                                    'gaussa':syn[dynamics_file]['gaussa']},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9},
                    dtypes=[np.float, np.int32, np.float])

    ###########################################################
    # Build recurrent connection rules
    ###########################################################
    def hipp_recurrent_connector(source,target,all_edges=[],min_syn=1, max_syn=1):
        """
        General logic:
        1. Given a *potential* source and target
        2. Look through all edges currently made
        3. If any of the current edges contains 
            a. the current source as a previous target of 
            b. the current target as a prevous source
        4. Return number of synapses per this connection, 0 otherwise (no connection)
        """
        for e in all_edges:
            #if source['node_id'] == e.target_gid and target['node_id'] == e.source_gid:
            if source['node_id'] == e['target_gid'] and target['node_id'] == e['source_gid']:
                return random.randint(min_syn,max_syn)

        return 0

    ########################################################### 
    # Build recurrent connections
    ###########################################################

    #Connect CA3e->CA3o Excitatory
    if build_edge['CA3e->CA3o']:
        dynamics_file = 'CA3e2CA3o.exc.json'

        if experiment == "SFN19-D": #Weight of the synapses are set to 6 from max weight of 2
            dynamics_file = 'CA3e2CA3o.exc.sfn19exp2d.json'

        conn = net.add_edges(source={'pop_name': 'CA3e'}, target={'pop_name': 'CA3o'},
                    connection_rule=hipp_recurrent_connector,
                    connection_params={'all_edges':syn_list}, #net.edges()},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'dist_delay':0.1, 'sec_id':0, 'sec_x':0.9}, #Connect.hoc:274 0.1 dist delay
                    dtypes=[np.float, np.int32, np.float])

    #Connect DGg->DGh Excitatory
    if build_edge['DGg->DGh']:
        dynamics_file = 'DGg2DGh.exc.json'
        conn = net.add_edges(source={'pop_name': 'DGg'}, target={'pop_name': 'DGh'},
                    connection_rule=hipp_recurrent_connector,
                    connection_params={'all_edges':syn_list}, #net.edges()},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'dist_delay':0.1, 'sec_id':0, 'sec_x':0.9}, #Connect.hoc:274 0.1 dist delay
                    dtypes=[np.float, np.int32, np.float])
    
    ###########################################################
    # Build strict connection rules
    ###########################################################
    def hipp_MF_connector(source,targets,min_syn=1, max_syn=1):
        """
        Exactly 2 connections from source to target
        Pick a random in the target area
        /docs/tutorial/04_multi_pop.ipynb:384:    
        "To tell the builder to use this schema, we must set iterator='all_to_one'
         in the add_edges method. (By default this is set to 'one_to_one'. You can
         also use 'one_to_all' iterator which will pass in a single source and all
         possible targets)."
        """
        
        total_targets = len(targets)
        syns = np.zeros(total_targets)
        x_ind = 0
        n = 0
        while n < 2:
            target_index = random.randint(0,total_targets-1)
            target = targets[target_index]
            dx = target['positions'][x_ind] - source['positions'][x_ind]

            #prob =	 1/ (exp( ((abs(dx) -0)^2)/ (2 * (2^2)))) // Standard deviation of 2 compared to 3 in pp projections More limited longitudianal spread
            prob = 1/(math.exp(((abs(dx)-0)**2)/(2*(2**2))))
            if random.random() < prob:
                n=n+1
                syns[target_index] = random.randint(min_syn,max_syn)

        return syns

    ########################################################### 
    # Build strict connections
    ###########################################################

    #Connect DGg->CA3e Excitatory (Exactly 2 connections allowed) NOTICE: iterator is 'one_to_all'
    if build_edge['DGg->CA3e']:
        dynamics_file = 'DGg2CA3e.exc.json'
        conn = net.add_edges(source={'pop_name': 'DGg'}, target={'pop_name': 'CA3e'},
                    iterator='one_to_all',
                    connection_rule=hipp_MF_connector,
                    connection_params={},
                    syn_weight=1,
                    dynamics_params=dynamics_file,
                    model_template=syn[dynamics_file]['level_of_detail'],
                    distance_range=[0.0, 300.0],
                    target_sections=['soma'])
        conn.add_properties(names=['delay', 'sec_id', 'sec_x'],
                    rule=syn_dist_delay_section,
                    rule_params={'base_delay':syn[dynamics_file]['delay'], 'sec_id':0, 'sec_x':0.9}, #Connect.hoc:274 0.1 dist delay
                    dtypes=[np.float, np.int32, np.float])
    
    ###########################################################
    # Create External Networks
    ###########################################################
    targets_used = []

    def hipp_external_connector(source,targets,min_syn=1, max_syn=1):
        """
        For each source external cell, randomly pick one target cell as long as
        it hasn't been targeted previously.
        
        Return: List of synapses to target cells, with only one element set to 1
        """
        total_targets = len(targets)
        syns = np.zeros(total_targets)

        target_found = False
        while not target_found: #Inf loops are bad
            target_index = random.randint(0,total_targets-1)
            if not target_index in targets_used:
                syns[target_index] = 1
                targets_used.append(target_index)
                target_found = True       
        
        return syns

    # We need an external netstim-like input to our nodes
    """
    StimuliTwoPatterns.hoc (Original code explanation)

    Create a pool obj with numbers 0 thru 29 (may be for number of cells in the cell EC)
    Create a Stims list obj
    objref stim, nc[inpTotal * 20], netsyn[inpTotal * 20]

    objref Pat1, Pat2, Pat3 //Picked cells to recieve the pattern
    Pat1 = GenerateVector(length = 10)
        create a picked vector of length 10
        for each in the vector 
            pick a random cell number from the pool
            add that cell to the picked and remove from the pool
        return picked cells
        

    Experiment 0
        tstop = 10000
        StimCount = 16
        StimSpace = tstop / StimCount 		//625
        StimDurRatio = 250 / StimSpace  	//.4
        StimSpaceRatio = StimSpace / tstop 	//0.0625
        
        for j in StimCount (loop StimCount times)
            create s stim object
            that starts j * StimSpace
            
            if j < 6
                applyStim(stim, Pat1, 15) //Apply the stimulus created to the Pat1 set of cells, with a initweight and weightmax of 15 in the pyr2pyr
            else
                applyStim to second set of randomly picked cells
    """

    

    if build_edge['exp0pat1->EC']:
        #See StimuliTwoPatterns.hoc:31 for connection params
        conn = exp0net.add_edges(target=net.nodes(pop_name='EC'),
                        source={'pat':'pat1'},
                        iterator='one_to_all',
                        connection_rule=hipp_external_connector,
                        connection_params={},
                        dynamics_params='NetCon2EC.exc.json',
                        model_template='pyr2pyr',
                        delay=0,
                        syn_weight=1,
                        target_sections=['soma'],  # target soma
                        distance_range=[0.0, 300]
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])
        
    if build_edge['exp0pat1->EC']:    
        conn = exp0net.add_edges(target=net.nodes(pop_name='EC'),
                        source={'pat':'pat2'},
                        iterator='one_to_all',
                        connection_rule=hipp_external_connector,
                        connection_params={},
                        dynamics_params='NetCon2EC.exc.json',
                        model_template='pyr2pyr',
                        delay=0,
                        syn_weight=1,
                        target_sections=['soma'],  # target soma
                        distance_range=[0.0, 300]
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])

    
    
    def target_ind_equals_source_ind(source, targets, offset=0, min_syn=1,max_syn=1):
        # Creates a 1 to 1 mapping between source and destination nodes
        try:
            total_targets = len(targets)
            syns = np.zeros(total_targets)
            target_index = source['node_id']
            syns[target_index-offset] = 1   
        except Exception:
            import pdb
            pdb.set_trace()
        return syns
        

    ###########################################################
    # Theta Network Background Noise
    ###########################################################


    # Connect LIF neurons to Hippocampal regions
    # Create virtual nodes
    # Connect virtual (spike event accepting) nodes to the LIF neurons

    if build_edge['bgnoisenodesCA3->CA3e']:
        conn = net.add_edges(target={'pop_name':'CA3e'},
                            source={'pop_name':'bgnoisenodesCA3'},
                            iterator='one_to_all',
                            connection_rule=target_ind_equals_source_ind,
                            connection_params={"offset":557},
                            dynamics_params='background2CA3.bg2pyr.json',
                            model_template='bg2pyr',
                            syn_weight=1, #threshold =1?
                            target_sections=['soma'],
                            distance_range=[0.0,9999])
        conn.add_properties(['delay','sec_id','sec_x'],rule=(1,0, 0.9), dtypes=[np.float,np.int32,np.float])

        #See StimuliTwoPatterns.hoc:31 for connection params
        conn = exp0net.add_edges(target=net.nodes(pop_name='bgnoisenodesCA3'),
                        source={'pop_name':'bgnoisevirtCA3'},
                        iterator='one_to_all',
                        connection_rule=target_ind_equals_source_ind,
                        connection_params={'offset':inpTotal},
                        dynamics_params='instanteneousExc.json',
                        delay=0,
                        syn_weight=1,
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])
    elif build_edge['bgnoisevirtCA3->CA3e']:
        conn = exp0net.add_edges(target=net.nodes(pop_name='CA3e'),
                        source={'pop_name':'bgnoisevirtCA3'},
                        iterator='one_to_all',
                        connection_rule=target_ind_equals_source_ind,
                        connection_params={'offset':inpTotal},
                        dynamics_params='NetCon2EC.exc.json',
                        model_template='pyr2pyr',
                        delay=0,
                        syn_weight=1,
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])

    if build_edge['bgnoisenodesDG->DGg']:
        conn = net.add_edges(target={"pop_name":'DGg'},
                            source={'pop_name':'bgnoisenodesDG'},
                            iterator='one_to_all',
                            connection_rule=target_ind_equals_source_ind,
                            connection_params={"offset":557+excTotal},
                            dynamics_params='background2DG.bg2pyr.json',
                            model_template='bg2pyr',
                            syn_weight=1, #threshold =1?
                            target_sections=['soma'],
                            distance_range=[0.0,9999])
        conn.add_properties(['delay','sec_id','sec_x'],rule=(1,0, 0.9), dtypes=[np.float,np.int32,np.float])

        conn = exp0net.add_edges(target=net.nodes(pop_name='bgnoisenodesDG'),
                        source={'pop_name':'bgnoisevirtDG'},
                        iterator='one_to_all',
                        connection_rule=target_ind_equals_source_ind,
                        connection_params={'offset':inpTotal+excTotal+CA3oTotal+CA3bTotal},
                        dynamics_params='instanteneousExc.json',
                        delay=0,
                        syn_weight=1,
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])

    if build_edge['bgnoisenodesEC->EC']:
        conn = net.add_edges(target={"pop_name":'EC'},
                            source={'pop_name':'bgnoisenodesEC'},
                            iterator='one_to_all',
                            connection_rule=target_ind_equals_source_ind,
                            connection_params={"offset":557+excTotal+DGexcTotal},
                            dynamics_params='background2CA3.bg2pyr.json',#TODO revisit may need an 2EC file
                            model_template='bg2pyr',
                            syn_weight=1, #threshold =1?
                            target_sections=['soma'],
                            distance_range=[0.0,9999])
        conn.add_properties(['delay','sec_id','sec_x'],rule=(1,0, 0.9), dtypes=[np.float,np.int32,np.float])

        conn = exp0net.add_edges(target=net.nodes(pop_name='bgnoisenodesEC'),
                        source={'pop_name':'bgnoisevirtEC'},
                        iterator='one_to_all',
                        connection_rule=target_ind_equals_source_ind,
                        connection_params={'offset':inpTotal+excTotal+DGexcTotal}, #Why is this 447? TODO MAGIC!!
                        dynamics_params='instanteneousExc.json',
                        delay=0,
                        syn_weight=1,
                        )
        conn.add_properties(['sec_id','sec_x'],rule=(0, 0.9), dtypes=[np.int32,np.float])
        

    ###########################################################
    # Build networks
    ###########################################################
    net.build()
    net.save(output_dir=output)    
    
    exp0net.build()
    exp0net.save(output_dir=output)
    
if __name__ == "__main__":
    build_hippocampus()
