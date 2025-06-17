import os
from src import Plotter, DataLoader, TSM
from args_parser import get_args, args_not_found
script_dir = os.path.dirname(os.path.abspath(__file__))

DATA_LOC = script_dir+'/data/data_tsp.txt'

if __name__ == "__main__":

    mode = get_args().mode
    if not mode:
        args_not_found()

    data = DataLoader.get_tsm_data(DATA_LOC)

    if mode == "benchmark":
        CONFIG_LOC = script_dir+'/config/benchmark_config.json'
        config = DataLoader.load_json(CONFIG_LOC)

        Plotter.plot_benchmark(data, config, save_img=True)
        print("Benchmarking completed. Check the saved image for results.")

    elif mode == "single":
        CONFIG_LOC = script_dir+'/config/solution_config.json'
        config = DataLoader.load_json(CONFIG_LOC)
        sol, cost, opt_cost, opt_gap = TSM(data=data, population_size=config['POPULATION_SIZE'],
                                           elite_size_factor=config['ELITE_SIZE_FACTOR'],
                                           mutation_rate=config['MUTATION_RATE'],
                                           crossover_rate=config['CROSSOVER_RATE'],
                                           mating_pool_size_factor=config['MATING_POOL_SIZE_FACTOR']).run()
        print("\nOptimal solution found:")
        print(f"Solution: {sol}")
        print(f"Cost of the solution: {cost:.2f}")
        print(f"Optimality metric cost: {opt_cost:.2f}")
        print(f"Optimality percentage gap: {opt_gap * 100:.2f}%")
        print("Check the config file for parameters used.\n")
    else:
        print("Invalid selection. Exiting.")
