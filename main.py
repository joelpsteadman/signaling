from Population import Population
from Utilities import Logger
import csv
import matplotlib.pyplot as plt

logger = Logger(debug=True)

POPULATION_SIZE = 1000
GENERATIONS = 1000

population = Population(POPULATION_SIZE)

# name of csv file 
filename = "output.csv"
    
# writing to csv file 
with open(filename, 'w') as output_file: 

    headers = ['Signal', 'Trust']
    csv_writer = csv.writer(output_file) 
    csv_writer.writerow(headers)

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
        average_quality = 0
        average_true_signal = 0
        average_trust = 0
        for male in population.males:
            average_quality += male.quality
            average_true_signal += male.true_signal
            average_trust += male.trust
        for female in population.females:
            average_quality += female.quality
            average_true_signal += female.true_signal
            average_trust += female.trust
        average_quality /= POPULATION_SIZE
        average_true_signal /= POPULATION_SIZE
        average_trust /= POPULATION_SIZE

            
        # writing to csv file 
        with open(filename, 'a') as output_file: 
            row = [average_true_signal, average_trust]
            csv_writer = csv.writer(output_file) 
            csv_writer.writerow(row)

        logger.debug(buffer, " average_quality      ", str(round(100*average_quality)), '%', delimiter='')
        logger.debug(buffer, " average_true_signal  ", str(round(100*average_true_signal)), '%', delimiter='')
        logger.debug(buffer, " average_trust        ", str(round(100*average_trust)), '%', delimiter='')

if not logger.show_debugging:
    logger.display_progress("Evolving: ", GENERATIONS, GENERATIONS, final=True)

    average_quality = 0
    average_true_signal = 0
    average_trust = 0
    for male in population.males:
        average_quality += male.quality
        average_true_signal += male.true_signal
        average_trust += male.trust
    for female in population.females:
        average_quality += female.quality
        average_true_signal += female.true_signal
        average_trust += female.trust
    average_quality /= POPULATION_SIZE
    average_true_signal /= POPULATION_SIZE
    average_trust /= POPULATION_SIZE

    logger.info(buffer, " average_quality      ", str(round(100*average_quality)), '%', delimiter='')
    logger.info(buffer, " average_true_signal  ", str(round(100*average_true_signal)), '%', delimiter='')
    logger.info(buffer, " average_trust        ", str(round(100*average_trust)), '%', delimiter='')

logger.debug("Done!")

if logger.show_debugging:
    x = []
    # with open(filename, 'r') as data:
    #     # creating a csv reader object
    #     csv_reader = csv.reader(data)
        
    #     # extracting field names through first row
    #     fields = next(csv_reader)
    
    #     # extracting each data row one by one
    #     for row in csv_reader:
    #         x.append(list(row[0] for i in included_cols))
    #         content = list(row[i] for i in included_cols)
    #         print content

    trust_dist = []
    signal_dist = []
    for male in population.males:
        trust_dist.append(male.trust)
        signal_dist.append(male.true_signal)
    for female in population.females:
        trust_dist.append(female.trust)
        signal_dist.append(female.true_signal)

    plt.hist(trust_dist)
    plt.hist(signal_dist)
    # plt.show() 