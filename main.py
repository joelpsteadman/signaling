from Population import Population
from Utilities import Logger

logger = Logger(debug=False)

POPULATION_SIZE = 1000
GENERATIONS = 2000

population = Population(POPULATION_SIZE)

for i in range(GENERATIONS):
    if not logger.show_debugging:
        logger.display_progress("Evolving: ", i, GENERATIONS)
    previous_generation = population.evolve()
    max_children_male = 0
    max_children_female = 0
    for male in previous_generation["males"]:
        if male.num_children > max_children_male:
            max_children_male = male.num_children
    for female in previous_generation["females"]:
        if female.num_children > max_children_female:
            max_children_female = female.num_children
    buffer = " "*len("Generation " + str(i))
    logger.debug("Generation", i, "max_children_male:  ", max_children_male)
    logger.debug(buffer, "max_children_female:", max_children_female)

    if logger.show_debugging:
        average_loyalty = 0
        average_true_signal = 0
        average_false_signal = 0
        average_trust = 0
        for male in population.males:
            average_loyalty += male.loyalty
            average_true_signal += male.true_signal
            average_false_signal += male.false_signal
            average_trust += male.trust
        for female in population.females:
            average_loyalty += female.loyalty
            average_true_signal += female.true_signal
            average_false_signal += female.false_signal
            average_trust += female.trust
        average_loyalty /= POPULATION_SIZE
        average_true_signal /= POPULATION_SIZE
        average_false_signal /= POPULATION_SIZE
        average_trust /= POPULATION_SIZE

        logger.debug(buffer, " average_loyalty      ", str(round(100*average_loyalty)), '%', delimiter='')
        logger.debug(buffer, " average_true_signal  ", str(round(100*average_true_signal)), '%', delimiter='')
        logger.debug(buffer, " average_false_signal ", str(round(100*average_false_signal)), '%', delimiter='')
        logger.debug(buffer, " average_trust        ", str(round(100*average_trust)), '%', delimiter='')

if not logger.show_debugging:
    logger.display_progress("Evolving: ", GENERATIONS, GENERATIONS, final=True)

average_loyalty = 0
average_true_signal = 0
average_false_signal = 0
average_trust = 0
for male in population.males:
    average_loyalty += male.loyalty
    average_true_signal += male.true_signal
    average_false_signal += male.false_signal
    average_trust += male.trust
for female in population.females:
    average_loyalty += female.loyalty
    average_true_signal += female.true_signal
    average_false_signal += female.false_signal
    average_trust += female.trust
average_loyalty /= POPULATION_SIZE
average_true_signal /= POPULATION_SIZE
average_false_signal /= POPULATION_SIZE
average_trust /= POPULATION_SIZE

logger.info(buffer, " average_loyalty      ", str(round(100*average_loyalty)), '%', delimiter='')
logger.info(buffer, " average_true_signal  ", str(round(100*average_true_signal)), '%', delimiter='')
logger.info(buffer, " average_false_signal ", str(round(100*average_false_signal)), '%', delimiter='')
logger.info(buffer, " average_trust        ", str(round(100*average_trust)), '%', delimiter='')
