from evolution import evolve_bin_packing_solution


def run_binpacking_experiment(b1, i1, b2, i2, m, p, n_experiments=5, crossover=True):
    """Run the evolutionary algorithm a number of times, return the best results.
    
    Args:
        b1: The number of bins in the first bin packing problem
        i1: The set of items for the first bin packing problem
        b2: The number of bins for the second bin packing problem
        i2: The set of items for the second bin packing problem
        m: The 'm' parameter determining the rate of mutation
        p: The size of the population to maintain
        n_experiments: (optional): Number of experiments to run with the set parameters.
                                   Defaults to 5.
        crossover: (optional): Boolean determining whether crossover of parents 
                               should take place. Defaults to True.

    Returns:
        (list1, list2):
            list1: List consisting of the best solutions from the first bpp
            list2: List consisting of the best solutions from the second bpp
    """
    bpp1results = []
    bpp2results = []

    for i in range(n_experiments):
        bpp1results.append(evolve_bin_packing_solution(b1, i1, m, p, crossover))
        bpp2results.append(evolve_bin_packing_solution(b2, i2, m, p, crossover))

    return bpp1results, bpp2results


if __name__ == '__main__':

    # Create list [2, 4, 6, ..., 1000]
    i1 = list(map(lambda x: 2*x, list(range(1, 501))))
    
    # Create list [2, 8, 18, 32, ..., 500000]
    i2 = list(map(lambda x: 2*x**2 , list(range(1, 501))))

    experiments = []

    # Experiment 1: Crossover, M=1, p=10
    print("Starting experiment 1:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=1, p=10))

    # Experiment 2: Crossover, M=1, p=100
    print("Starting experiment 2:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=1, p=100))

    # Experiment 3: Crossover, M=5, p=10
    print("Starting experiment 3:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=5, p=10))

    # Experiment 4: Crossover, M=5, p=100
    print("Starting experiment 4:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=5, p=100))

    # Experiment 5: No Crossover, M=5, p=10
    print("Starting experiment 5:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=5, p=10, crossover=False))

    # Experiment 6: Crossover, M=0 (No mutation), p=10
    print("Starting experiment 6:")
    experiments.append(run_binpacking_experiment(10, i1, 100, i2, m=0, p=10))
