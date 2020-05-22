# GuntuBanks-bmtk

## Running GuntuBanks-bmtk

```
python seed_sweep.py 9000 0 simulation_config.json
```

Will run the entire simulation.


## Implementation Notes

1. Will likely use [HummosBanks-bmtk](../HummosBanks-bmtk) as a base
1. Analyze Hipp.hoc for changes, follow program flow, document

## Core differences (2014 v Theta)

- [X] The values for the synapse connections **are** different from the original [./Inputs/Synapses.txt](../HummosTheta/Inputs/Synapses.txt)
- [X] Will need to regenerate synapse json files (easy, this is scripted already)
- [X] New locations for DGinh and CA3i (Unused currently but there)
- [X] IzhiCell_CA3 was replaced with CA3PyramidalCell
- [X] IzhiCell_GC was replaced with DGCell
- [X] The following files were added. Netstims now supply background input.
    - [X] backgroundgen.hoc
    - [X] bg_template.hoc
    - [X] background2CA3.hoc
    - [X] background2DG.hoc
- [X] StimuliTwoPatters.hoc remains. Any differences? Experiment number is 1 for simulation
