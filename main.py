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
