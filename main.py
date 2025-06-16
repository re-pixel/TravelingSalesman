import os
from src import Plotter, DataLoader

script_dir = os.path.dirname(os.path.abspath(__file__))

DATA_LOC = script_dir+'/data/data_tsp.txt'
CONFIG_LOC = script_dir+'/config/evol_config.json'

if __name__ == "__main__":
    data = DataLoader.get_tsm_data(DATA_LOC)
    config = DataLoader.load_json(CONFIG_LOC)

    Plotter.plot_benchmark(data, config, save_img=True)
    print("Benchmarking completed. Check the saved image for results.")
