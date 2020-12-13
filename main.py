# STEPS:
# TERMINATION: 10,000 FITNESS EVALUATIONS
# SELECTION: BINARY TOURNAMENT
# RECOMBINATION: SINGLE-POINT CROSSOVER
# MUTATION: MULTI-GENE MUTATION MK
# REPLACEMENT: WEAKEST REPLACEMENT
# SOLUTION MEASUREMENT: HEAVIEST - LIGHTEST BIN
import random

class Solution:

    def __init__(self, b, items_count):
        self.chromosone = self.generate_chromosone(b, items_count)


    def generate_chromosone(self, b, items_count):
        chromosone = ''
        
        for i in range(items_count):
            chromosone += str(random.randrange(1, b+1))

        return chromosone


    def evaluate_solution(self):
        pass
    

def solve_bin_pack(b, i):
    pass


if __name__ == '__main__':

    # Create list [2, 4, 6, ..., 1000]
    i1 = list(map(lambda x: 2*x, list(range(1, 501))))
    
    # Create list [2, 8, 18, 32, ..., 500000]
    i2 = list(map(lambda x: 2*x**2 , list(range(1, 501))))

    solve_bin_pack(b=10, i=i1)
    # solve_bin_pack(b=100, i=i2)

