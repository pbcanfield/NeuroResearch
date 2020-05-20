import seed_sweep

if __name__ == '__main__':
    os.system("nrnivmodl ./biophys_components/mechanisms/")
    run_seed(9000,0,"simulation_config.json",skip_build = False)