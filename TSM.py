with open('data_tsp.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
data = [line.split()[1:] for line in data if line.strip()] 
data = [[float(num) for num in line] for line in data]

import random

class TSM:
    def __init__(self, data, population_size=100, seed=None, elite_size_factor=0.1, mutation_rate=0.1, 
                max_generations=1000, crossover_rate=0.7, mating_pool_size_factor=0.5):
        
        self.data = data
        self.n_of_points = len(data)

        self.population_size = population_size
        self.seed = seed
        self.best_solution = None
        self.elite_size = int(elite_size_factor * self.population_size)
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.crossover_rate = crossover_rate
        self.mating_pool_size = int(population_size * mating_pool_size_factor)

        self.distances = [[-1] * self.n_of_points for _ in range(self.n_of_points)]
        self.__calculate_distances__()
        self.population = []
        self.fitness = []
        self.__initialize_population__()

    def __get_data__(self):
        return self.data

    def __calculate_distance__(self, point1, point2):
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1] ** 2)) ** 0.5

    def __calculate_distances__(self):
        for i in range(self.n_of_points):
            for j in range(i + 1, self.n_of_points):
                distance = self.__calculate_distance__(self.data[i], self.data[j])
                self.distances[i][j] = distance
                self.distances[j][i] = distance

    def __calculate_fitness__(self, solution):
        total_distance = 0
        for i in range(len(solution) - 1):
            total_distance += self.distances[solution[i]][solution[i + 1]]
        total_distance += self.distances[solution[-1]][solution[0]]
        return total_distance
    
    def __calculate_population_fitness__(self):
        self.fitness = [self.__calculate_fitness__(solution) for solution in self.population]
        self.best_solution = min(self.population, key=self.__calculate_fitness__)
    
    def __initialize_population__(self):
        self.population = []
        for _ in range(self.population_size):
            individual = list(range(self.n_of_points))
            random.shuffle(individual)
            self.population.append(individual)
        self.__calculate_population_fitness__()

    def __select_parents__(self):
        total_fitness = sum(self.fitness)
        probabilities = [f / total_fitness for f in self.fitness]
        parents = random.choices(self.population, weights=probabilities, k=2)
        return parents
    
    def __select_parents_from_mating_pool__(self):
        self.__sort_population__()
        mating_pool = self.population[:self.mating_pool_size]
        total_fitness = sum(self.fitness[:self.mating_pool_size])
        probabilities = [f / total_fitness for f in self.fitness[:self.mating_pool_size]]
        parents = random.choices(mating_pool, weights=probabilities, k=2)
        return parents
    
    def __mutate__(self, individual):
        for i in range(self.n_of_points):
            if random.random() < self.mutation_rate:
                j = random.randint(0, self.n_of_points - 1)
                individual[i], individual[j] = individual[j], individual[i]
        return individual
    
    def __crossover__(self):
        parent1, parent2 = self.__select_parents__()

        point1 = random.randint(0, self.n_of_points - 1)
        point2 = random.randint(point1 + 1, self.n_of_points)
        child = [-1] * self.n_of_points
        child[point1:point2] = parent1[point1:point2]
        
        p2_index = 0
        for i in range(self.n_of_points):
            if child[i] == -1:
                while parent2[p2_index] in child:
                    p2_index += 1
                child[i] = parent2[p2_index]
        
        child = self.__mutate__(child)
        return child
    
    def __sort_population__(self):
        self.population = sorted(self.population, key=self.__calculate_fitness__)

    def run(self):
        random.seed(self.seed)
        for _ in range(self.max_generations):
            new_population = []
            self.__calculate_population_fitness__()
            self.__sort_population__()

            new_population.extend(self.population[:self.elite_size])

            while len(new_population) < self.population_size:
                if random.random() < self.crossover_rate:
                    child = self.__crossover__()
                    new_population.append(child)
                else:
                    parent, _ = self.__select_parents_from_mating_pool__()
                    new_population.append(self.__mutate__(parent.copy()))

            self.population = new_population

        self.__calculate_population_fitness__()
        return self.best_solution, self.__calculate_fitness__(self.best_solution)