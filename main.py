# STEPS:

import random
import numpy as np

class Solution:

    def __init__(self, b, i, chromosome=None):
        self.items = i 
        self.bins_count = b

        if chromosome is None:
            self.chromosome = self.generate_chromosome()
        else:
            self.chromosome = chromosome
        
        self.fitness = self.evaluate_solution()


    def __repr__(self):
        return f"Solution(fitness={self.fitness})"


    def generate_chromosome(self):
        return np.random.randint(low=1, high=self.bins_count+1, size=len(self.items))


    def mutate(self, m):
        for i in range(m):
            gene_index = random.randint(0, len(self.chromosome)-1)
            self.chromosome[gene_index] = random.randint(1, self.bins_count+1)


    def evaluate_solution(self):
        global iter_count
        iter_count += 1
        bins = {}

        for i, gene in enumerate(self.chromosome):
            if gene not in bins:
                bins[gene] = 0
            bins[gene] += self.items[i]

        self.fitness = max(bins.values()) - min(bins.values())

        return self.fitness

def binary_tournament(population):
    candidates = random.choices(population, k=2)
    return min(candidates, key=lambda candidate: candidate.fitness)


def select_parents(population):
    parent1 = binary_tournament(population)
    parent2 = binary_tournament(population)
    return parent1, parent2


def single_point_crossover(parent1, parent2):
    crossover_point = random.randrange(1, len(parent1.chromosome)-2)

    a1 = parent1.chromosome[:crossover_point]
    a2 = parent1.chromosome[crossover_point:]

    b1 = parent2.chromosome[:crossover_point]
    b2 = parent2.chromosome[crossover_point:]

    child1 = Solution(b=parent1.bins_count, i=parent1.items, chromosome=np.hstack((a1, b2)))
    child2 = Solution(b=parent1.bins_count, i=parent1.items, chromosome=np.hstack((b1, a2)))

    return child1, child2


def solve_bin_pack(b, i, m, p):
    global iter_count 
    iter_count = 0
    # Generate initial population
    population = [Solution(b, i) for x in range(p)]
    starting_avg = sum(sol.fitness for sol in population) / p
    print("Starting Average: ", starting_avg)
    flag_stop = False

    while not flag_stop:

        if iter_count >= 10000:
            flag_stop = True 
            break

        parent1, parent2 = select_parents(population)

        child1, child2 = single_point_crossover(parent1, parent2)
        child1.mutate(m)
        child2.mutate(m)
        
        population = weakest_replacement(population, child1)
        population = weakest_replacement(population, child2)

    ending_average = sum(sol.fitness for sol in population) / p
    print("Ending Average: ", ending_average)
    print(iter_count)


def weakest_replacement(population, new_solution):

    worst_solution = max(population, key=lambda solution: solution.fitness)

    if new_solution.fitness < worst_solution.fitness:
        population.remove(worst_solution)
        population.append(new_solution)
    return population
    

if __name__ == '__main__':

    # Create list [2, 4, 6, ..., 1000]
    i1 = list(map(lambda x: 2*x, list(range(1, 501))))
    
    # Create list [2, 8, 18, 32, ..., 500000]
    i2 = list(map(lambda x: 2*x**2 , list(range(1, 501))))

    solve_bin_pack(b=10, i=i1, m=1, p=100)

    # solve_bin_pack(b=100, i=i2)

