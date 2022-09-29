from Models.Individual import Individual
import random

SAMPLE_SIZE = 10 # number of men that each woman considers

class Population:
    def __init__(self, size):
        self.size = size
        self.females = []
        self.males = []
        for i in range(size):
            child = Individual()
            if child.sex == 'F':
                self.females.append(child)
            elif child.sex == 'M':
                self.males.append(child)
            else:
                raise Exception("Individual's sex is not set")

    def evolve(self):
        next_generation = []
        while len(next_generation) < self.size:
            female = self.females.pop(0)
            child, male = self._pick_male(female)
            fitness = male.value # thus, when the father's value is .7, the child has .7 likelihood of getting into next gen
            if fitness >= random.random():
                next_generation.append(child)
                female.num_surviving_children += 1
                male.num_surviving_children += 1
            self.females.append(female)
        previous_generation = {"males": self.males, "females": self.females}

        self.females = []
        self.males = []
        for child in next_generation:
            if child.sex == 'F':
                self.females.append(child)
            elif child.sex == 'M':
                self.males.append(child)
            else:
                raise Exception("Individual's sex is not set")
        random.shuffle(self.females)

        return previous_generation

    def _pick_male(self, female):
        # A trust of .7 gives a .7 likelihood of using signaling as a measure of value
        # Above the .1 or .9 threasholds, trust is never or always used respectively
        if female.trust > random.uniform(.1,.9):
            while True:
                male = random.choice(self.males)
                if male.signal >= random.uniform(0,1): # therefore a signal of strength .7 has a .7 chance of being picked
                    child = Individual(female, male)
                    female.num_children += 1
                    male.num_children += 1
                    return child, male
        else: # otherwise, pick someone random
            male = random.choice(self.males)
            child = Individual(female, male)
            female.num_children += 1
            male.num_children += 1
            return child, male

    def _pick_male_from_group(self, female):
        males = random.sample(self.males, SAMPLE_SIZE)
        # A trust of .7 gives a .7 likelihood of using signaling as a measure of value
        # Above the .1 or .9 threasholds, trust is never or always used respectively
        if female.trust > random.uniform(.1,.9):
            signals = []
            values = []
            perceived_values = []
            for male in males:
                signals.append(male.signal)
                values.append(male.value)
            for i in range(len(signals)):
                perceived_values.append(female.trust * signals[i])
            max_perceived_value = max(perceived_values)
            max_index = perceived_values.index(max_perceived_value)
            selected_male = males[max_index]
        else: # otherwise, pick someone random
            selected_male = random.choice(males)
        child = Individual(female, selected_male)
        female.num_children += 1
        selected_male.num_children += 1
        return child, selected_male