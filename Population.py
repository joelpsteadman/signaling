from Individual import Individual
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.females = []
        self.males = []
        self.sample_size = 30 # number of men that each woman considers
        for i in range(size):
            individual = Individual()
            if individual.sex == 'F':
                self.females.append(individual)
            elif individual.sex == 'M':
                self.males.append(individual)
            else:
                raise Exception("Individual's sex is not set")

    def evolve(self):
        next_generation = []
        while len(next_generation) < self.size:
            # num = len(self.females)
            female = self.females.pop(0)
            males = random.sample(self.males, self.sample_size)
            signals = []
            values = []
            perceived_values = []
            for male in males:
                signal, value = male.calculate_signal_and_value()
                signals.append(signal)
                values.append(value)
            for i in range(len(signals)):
                perceived_values.append(female.trust * signals[i] + random.uniform(-.01, 0.01))
            max_value = max(values)
            max_index = values.index(max_value)
            individual = Individual(female, males[max_index])
            # signal, value = individual.calculate_signal_and_value()
            female.num_children += 1
            males[max_index].num_children += 1
            if individual.quality >= random.random(): # thus, an individual with quality .7 has .7 likelihood of getting into next gen
                next_generation.append(individual)
            self.females.append(female)
        previous_generation = {"males": self.males, "females": self.females}

        self.females = []
        self.males = []
        for individual in next_generation:
            if individual.sex == 'F':
                self.females.append(individual)
            elif individual.sex == 'M':
                self.males.append(individual)
            else:
                raise Exception("Individual did not have a sex")

        return previous_generation