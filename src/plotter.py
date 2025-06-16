import matplotlib.pyplot as plt
from src import TSM


class Plotter:

    @staticmethod
    def get_canvas(x=3, y=2, figsize=(10, 8)):
        fig, ax = plt.subplots(x, y, figsize=figsize)
        return fig, ax

    @staticmethod
    def show_plot():

        plt.show()

    @staticmethod
    def plot_benchmark(data, config, save_img=False):
        fig, ax = Plotter.get_canvas(3, 2, figsize=(16, 10))

        note = ("⚙️ Benchmarking with standard parameters:\n"
                "population_size=50 | seed=None | elite_size_factor=0.1 |\n"
                "mutation_rate=0.1 | max_generations=1000 | crossover_rate=0.7 |\n"
                "mating_pool_size_factor=0.5")

        ax[0, 1].clear()             # Clear anything already plotted there
        ax[0, 1].axis('off')         # Hide all axes, ticks, labels, and spines

        ax[0, 1].text(
            0.5, 0.5, note,
            fontsize=12, fontweight='bold', color='navy',
            ha='center', va='center',
            bbox=dict(facecolor='lightgrey', alpha=0.5,
                      boxstyle='round,pad=0.5'),
            transform=ax[0, 1].transAxes,
            wrap=True  # makes text wrap inside axes boundaries
        )
        # Plot individual benchmarks
        Plotter.plot_diff_population_sizes(
            fig, ax[0, 0], data, config['POPULATION_SIZES']
        )

        Plotter.plot_diff_elite_size_factors(
            fig, ax[1, 0], data, config['ELITE_FACTORS']
        )

        Plotter.plot_diff_mutation_rates(
            fig, ax[1, 1], data, config['MUTATION_RATES']
        )

        Plotter.plot_diff_crossover_rates(
            fig, ax[2, 0], data, config['CROSSOVER_RATES']
        )

        Plotter.plot_diff_mating_pool_size_factors(
            fig, ax[2, 1], data, config['MATING_POOL_FACTORS']
        )

        fig.tight_layout(rect=[0, 0, 1, 0.95])  # leave space for suptitle
        Plotter.show_plot()

        if save_img:
            fig.savefig('benchmark_results.png', dpi=300, bbox_inches='tight')
            print("Benchmark results saved as 'benchmark_results.png'")

    @staticmethod
    def plot_diff_population_sizes(fig, ax, data, population_sizes):
        results = [TSM(data, population_size=ps).run()
                   for ps in population_sizes]
        costs = [result[1] for result in results]
        optimality_metric_cost = results[0][2]
        ax.plot(population_sizes, costs, marker='o',
                linestyle='-', color='tab:blue')
        ax.axhline(y=optimality_metric_cost, color='r', linestyle='--',
                   label='Optimality Metric Cost')
        ax.set_title('Population Size vs Cost')
        ax.set_xlabel('Population Size')
        ax.set_ylabel('Cost')
        ax.grid(True)

    @staticmethod
    def plot_diff_elite_size_factors(fig, ax, data, elite_factors):
        results = [TSM(data, elite_size_factor=ef).run()
                   for ef in elite_factors]
        costs = [result[1] for result in results]
        ax.plot(elite_factors, costs, marker='o',
                linestyle='-', color='tab:green')
        ax.set_title('Elite Size Factor vs Cost')
        ax.set_xlabel('Elite Size Factor')
        ax.set_ylabel('Cost')
        ax.grid(True)

    @staticmethod
    def plot_diff_mutation_rates(fig, ax, data, mutation_rates):
        results = [TSM(data, mutation_rate=mr).run() for mr in mutation_rates]
        costs = [result[1] for result in results]
        ax.plot(mutation_rates, costs,
                linestyle='-', marker='o', color='tab:red')
        ax.set_title('Mutation Rate vs Cost')
        ax.set_xlabel('Mutation Rate')
        ax.set_ylabel('Cost')
        ax.grid(True)

    @staticmethod
    def plot_diff_crossover_rates(fig, ax, data, crossover_rates):
        results = [TSM(data, crossover_rate=cr).run()
                   for cr in crossover_rates]
        costs = [result[1] for result in results]
        ax.plot(crossover_rates, costs, marker='o',
                linestyle='-', color='tab:purple')
        ax.set_title('Crossover Rate vs Cost')
        ax.set_xlabel('Crossover Rate')
        ax.set_ylabel('Cost')
        ax.grid(True)

    @staticmethod
    def plot_diff_mating_pool_size_factors(fig, ax, data, mating_pool_factors):
        results = [TSM(data, mating_pool_size_factor=mpf).run()
                   for mpf in mating_pool_factors]
        costs = [result[1] for result in results]
        ax.plot(mating_pool_factors, costs, marker='o',
                linestyle='-', color='tab:orange')
        ax.set_title('Mating Pool Size Factor vs Cost')
        ax.set_xlabel('Mating Pool Size Factor')
        ax.set_ylabel('Cost')
        ax.grid(True)
