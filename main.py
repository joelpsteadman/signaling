from Population import Population
from Utilities import Logger

logger = Logger(debug=True)

POPULATION_SIZE = 1000
GENERATIONS = 1000

population = Population(POPULATION_SIZE)

for i in range(GENERATIONS):
    logger.display_progress("Evolving: ", i, GENERATIONS)
    population.evolve()
logger.display_progress("Evolving: ", GENERATIONS, GENERATIONS, final=True)

average_quality = 0
average_true_signal = 0
average_false_signal = 0
average_trust = 0
for male in population.males:
    average_quality += male.quality
    average_true_signal += male.true_signal
    average_false_signal += male.false_signal
    average_trust += male.trust
for female in population.females:
    average_quality += female.quality
    average_true_signal += female.true_signal
    average_false_signal += female.false_signal
    average_trust += female.trust
average_quality /= POPULATION_SIZE
average_true_signal /= POPULATION_SIZE
average_false_signal /= POPULATION_SIZE
average_trust /= POPULATION_SIZE

# TODO factor quality into ability to add to the next gen if that isn't done already

logger.info("average_quality      ", str(round(100*average_quality)), '%', delimiter='')
logger.info("average_true_signal  ", str(round(100*average_true_signal)), '%', delimiter='')
logger.info("average_false_signal ", str(round(100*average_false_signal)), '%', delimiter='')
logger.info("average_trust        ", str(round(100*average_trust)), '%', delimiter='')