import seed_sweep

os.system("./biophys_components/mechanisms/nrnivmodl")
for i in range(10):
    run_seed(random.randrange(10000),"0", "simulation_config.json", False)
