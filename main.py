import random
import numpy as np


class Solution:
    """Object representing a candidate solution.

    Handles the encoding of chromosomes, calculation of fitness, and mutations.

    Attributes:
        items: The list of items used by the bin-packing problem

        bins_count: The number of bins in the bin-packing problme

        chromosome: DNA representing the solution's item-bin allocations

        fitness: The calculated fitness of the solution

        iter_count: The number of times the solution has been evaluated.
                    Used for stopping condition.

    """


    def __init__(self, bins, items, chromosome=None):
        """Initialise a solution. 

        Args:
            bins: The number of bins in the bin-packing problem

            items: The list of items to be bin-packed

            chromosome: Optional argument. If given, initialises solution with
                        the given chromosome. If not given, creates a random
                        chromosome.

        """
        self.items = items 
        self.bins_count = bins


        if chromosome is None:
            self.chromosome = self.generate_chromosome()
        else:
            self.chromosome = chromosome
        

        self.iter_count = 0
        self.evaluate_solution()


    def __repr__(self):
        return f"Solution(fitness={self.fitness})"


    def generate_chromosome(self):
        """Generate a random chromosome for the solution.

        Returns:
            Numpy array showing each item's initial bin allocation in the format
            [1, 2, 2] => bin1: item0; bin2: item1, item2. 

        """
        return np.random.randint(low=1, high=self.bins_count+1, size=len(self.items))


    def mutate(self, m):
        """Mutates the solution's chromosome by randomly changing m genes.
        
        Args:
            m: Integer stating the maximum number of genes to randomise.

        """
        for i in range(m):
            gene_index = random.randint(0, len(self.chromosome)-1)
            self.chromosome[gene_index] = random.randint(1, self.bins_count+1)
        self.evaluate_solution()


    def evaluate_solution(self):
        """Evaluate the solution's fitness.

        Evaluates the solution based on the maximum bin's weight minus the 
        minimum bin's weight. Lower fitness values are better. Store the new
        fitness value within the instance.

        """
        self.iter_count += 1

        bins = {}

        # Loop through chromosome to find each item's bin. 
        for i, gene in enumerate(self.chromosome):
            if gene not in bins:
                bins[gene] = 0
            
            # Add item's weight to the bin.
            bins[gene] += self.items[i]

        self.fitness = max(bins.values()) - min(bins.values())


def binary_tournament(population):
    """Complete a binary tournament to select a solution.

    Args:
        population: List consisting of all of the current solutions.
    
    Returns:
        The winner of a binary tournament.

    """
    # Select two random candidates
    candidates = random.choices(population, k=2)

    # Return the fittest candidate (the one with the lowest fitness)
    return min(candidates, key=lambda candidate: candidate.fitness)


def select_parents(population):
    """Select two parents from the population to be crossed.

    Args:
        population: List consisting of all current solutions.

    Returns:
        parent1, parent2: Two parents found from running two binary tournaments. 

    """
    parent1 = binary_tournament(population)
    parent2 = binary_tournament(population)

    return parent1, parent2


def single_point_crossover(parent1, parent2):
    """Generate two new children solutions from two parent solutions.

    Args:
        parent1: The first parent 
        
        parent2: The second parent

    Returns:
        (child1, child2): The two children generated from the parents

    """

    # Choose a random crossover point. Exclude possibilites that result in no change.
    crossover_point = random.randrange(1, len(parent1.chromosome)-2)

    a1 = parent1.chromosome[:crossover_point]
    a2 = parent1.chromosome[crossover_point:]
    
    b1 = parent2.chromosome[:crossover_point]
    b2 = parent2.chromosome[crossover_point:]

    # Create two new children from the crossover
    child1 = Solution(bins=parent1.bins_count, items=parent1.items, chromosome=np.hstack((a1, b2)))
    child2 = Solution(bins=parent1.bins_count, items=parent1.items, chromosome=np.hstack((b1, a2)))

    return child1, child2


def weakest_replacement(population, new_solution):
    """Perform weakest replacement upon a population.

    Args:
        population: List consisting of each solution
        
        new_solution: The new solution to consider introducing to the population

    """
    # Find the solution with the maximum fitness score, i.e the worst
    worst_solution = max(population, key=lambda solution: solution.fitness)

    # Even if the solution is equally fit, replace.
    if new_solution.fitness <= worst_solution.fitness:
        population.remove(worst_solution)
        population.append(new_solution)

    return population
    

def count_iterations(all_solutions):
    """From a list of solutions, count the number of times they have all been 
       evaluated.

    Args:
        all_solutions: List consisiting of every solution that has ever been
                       in the population.
        
    Returns:
        int: The sum of all iteration counts for each member of the list

    """

    return sum(solution.iter_count for solution in all_solutions)


def evolve_bin_packing_solution(b, i, m, p, crossover=True):
    """Run an evolutionary algorithm to find a solution to the binpacking problem.

    Args:
        b: The number of bins we are trying to fill

        i: The list of items to put into the bins

        m: The M parameter that affects the level of mutation

        p: The size of the population to maintain

        crossover: Whether to include crossover, or just mutation. Default True.

    Returns:
        best_solution: The solution produced by the algorithm with the best (lowest)
                       score.

    """
    
    # Generate initial population
    population = [Solution(bins=b, items=i) for x in range(p)]


    # Create a deep copy of the population. This list will contain all of the
    # solutions ever considered. Used to calculate number of iterations.
    all_solutions = population[:]

    while True:

        if count_iterations(all_solutions) >= 10000:
            break
        
        if crossover:
            parent1, parent2 = select_parents(population)

            child1, child2 = single_point_crossover(parent1, parent2)

            child1.mutate(m)
            child2.mutate(m)
            all_solutions += [child1, child2]

            population = weakest_replacement(population, child1)
            population = weakest_replacement(population, child2)

        else:
            # Instead of crossover, select one parent and apply mutation to a
            # copy of it. Use weakest replacement to decide if it is introduced.
            solution = binary_tournament(population)
            child = Solution(bins=b, items=i, chromosome=solution.chromosome)
            child.mutate(m)

            population = weakest_replacement(population, child)


    best_solution = min(population, key=lambda solution: solution.fitness)


    return best_solution


if __name__ == '__main__':

    # Create list [2, 4, 6, ..., 1000]
    i1 = list(map(lambda x: 2*x, list(range(1, 501))))
    
    # Create list [2, 8, 18, 32, ..., 500000]
    i2 = list(map(lambda x: 2*x**2 , list(range(1, 501))))

    solution = evolve_bin_packing_solution(b=10, i=i1, m=1, p=100)
    print(solution)
    # evolve_bin_packing_solution(b=100, i=i2)

