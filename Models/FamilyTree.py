class FamilyTree:
    def __init__(self, population_size):
        self.POPULATION_SIZE = population_size
        self.__generations = []

    def __getitem__(self, index):
        return self.__generations[index]

    def add_generation(self, generation):
        new_generation = []
        for male in generation['males']:
            new_generation.append(male)
        for female in generation['females']:
            new_generation.append(female)
        self.__generations.append(new_generation)

    def show(self, num):
        for generation in self.__generations:
            i = 0
            while i < num:
                print(generation[i].num_children, end=' ')
                i += 1
            print()