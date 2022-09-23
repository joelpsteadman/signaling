from Individual import Individual
import random

class Population:
    def __init__(self, size):
        self.size = size
        self.females = []
        self.males = []
        self.sample_size = 10 # number of men that each woman considers
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
                perceived_values.append(female.trust * signals[i])# + random.uniform(-0.1, 0.1))
            max_perceived_value = max(perceived_values)
            max_index = perceived_values.index(max_perceived_value)
            # male = males[max_index]
            individual = Individual(female, males[max_index])
            signal, value = individual.calculate_signal_and_value()
            female.num_children += 1
            males[max_index].num_children += 1
            fitness = (values[max_index] + female.quality) / 2
            # fitness = values[max_index]
            if fitness >= random.random(): # thus, an individual with fitness .7 has .7 likelihood of getting into next gen
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
                raise Exception("Individual's sex is not set")
        random.shuffle(self.females)

        return previous_generation