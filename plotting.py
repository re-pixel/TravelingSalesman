import matplotlib.pyplot as plt
import numpy as np


POPULATION_SIZES = [10, 20, 50, 100, 200]
ELITE_FACTORS = [0.05, 0.1, 0.2]
MUTATION_RATES = [0.01, 0.05, 0.1]
CROSSOVER_RATES = [0.5, 0.7, 0.9]
MATING_POOL_FACTORS = [0.2, 0.5, 0.8]

def run_tsm_algorithm(data, population_size=100, elite_size_factor=0.1, mutation_rate=0.1,
                     crossover_rate=0.7, mating_pool_size_factor=0.5):
    from TSM import TSM


    travelling_salesman = TSM(data, population_size=population_size,
                              elite_size_factor=elite_size_factor,
                              mutation_rate=mutation_rate,
                              crossover_rate=crossover_rate,
                              mating_pool_size_factor=mating_pool_size_factor)

    best_path, cost = travelling_salesman.run()
    
    return {
        'population_size': population_size,
        'elite_size_factor': elite_size_factor,
        'mutation_rate': mutation_rate,
        'crossover_rate': crossover_rate,
        'mating_pool_size_factor': mating_pool_size_factor,
        'best_path': best_path,
        'cost': cost
    }

with open('data_tsp.txt', 'r') as f:
    data = f.read()

    data = data.split('\n')
    data = [line.split()[1:] for line in data if line.strip()] 
    data = [[float(num) for num in line] for line in data]




for population_size in POPULATION_SIZES:
    results = run_tsm_algorithm(data, population_size=population_size)
    print(results)

def plot_results(results):
    fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    fig.suptitle('TSM Algorithm Results')

    # Plot population sizes
    axs[0, 0].plot(POPULATION_SIZES, results['population_size'], marker='o')
    axs[0, 0].set_title('Population Size vs Cost')
    axs[0, 0].set_xlabel('Population Size')
    axs[0, 0].set_ylabel('Cost')

    # Plot elite size factors
    axs[0, 1].plot(ELITE_FACTORS, results['elite_size_factor'], marker='o')
    axs[0, 1].set_title('Elite Size Factor vs Cost')
    axs[0, 1].set_xlabel('Elite Size Factor')
    axs[0, 1].set_ylabel('Cost')

    # Plot mutation rates
    axs[1, 0].plot(MUTATION_RATES, results['mutation_rate'], marker='o')
    axs[1, 0].set_title('Mutation Rate vs Cost')
    axs[1, 0].set_xlabel('Mutation Rate')
    axs[1, 0].set_ylabel('Cost')

    # Plot crossover rates
    axs[1, 1].plot(CROSSOVER_RATES, results['crossover_rate'], marker='o')
    axs[1, 1].set_title('Crossover Rate vs Cost')
    axs[1, 1].set_xlabel('Crossover Rate')
    axs[1, 1].set_ylabel('Cost')

    # Plot mating pool size factors
    axs[2, 0].plot(MATING_POOL_FACTORS, results['mating_pool_size_factor'], marker='o')
    axs[2, 0].set_title('Mating Pool Size Factor vs Cost')
    axs[2, 0].set_xlabel('Mating Pool Size Factor')
    axs[2, 0].set_ylabel('Cost')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()