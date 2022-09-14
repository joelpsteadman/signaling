from numpy import random

# COST_OF_CHILD = 0.5

class Individual:
    def __init__(self, mother = 0, father = 0):
        if mother == 0:
            self._init_no_parents()
        else:
            self._init_with_parents(mother, father)
        self.num_children = 0

    def _init_no_parents(self):
        self.sex = random.choice(['M', 'F'])
        self.quality = random.uniform(0.01, 0.99)
        self.true_signal = random.uniform(0.01, 0.99)
        self.false_signal = random.uniform(0.01, 0.99)
        self.trust = random.uniform(0.01, 0.99)

    def _init_with_parents(self, mother, father):
        self.sex = random.choice(['M', 'F'])
        self.quality = self._inherit_trait(mother.quality, father.quality)
        self.true_signal = self._inherit_trait(mother.true_signal, father.true_signal)
        self.false_signal = self._inherit_trait(mother.false_signal, father.false_signal)
        self.trust = self._inherit_trust(mother.trust, father.trust)

    def _inherit_trait(self, mother_trait, father_trait):
        trait = (mother_trait + father_trait + random.uniform(-0.1, 0.1)) / 2
        trait = max(0.01, trait) # don't go below 0.01
        trait = min(0.99, trait) # don't go above 0.99
        return trait

    def _inherit_trust(self, mother_trait, father_trait):
        trait = (mother_trait + father_trait + random.uniform(-0.5, 0.5)) / 2
        trait = max(-0.99, trait) # don't go below -0.99
        trait = min(0.99, trait) # don't go above 0.99
        return trait

    def calculate_signal_and_value(self):
        value = self.quality
        # value = value * (1 - COST_OF_CHILD)**self.num_children
        signal = value**2 * self.true_signal
        value -= signal
        if self.false_signal <= value:
            signal += self.false_signal
            value -= self.false_signal
        else:
            signal += value
            value = 0
        return signal, value
