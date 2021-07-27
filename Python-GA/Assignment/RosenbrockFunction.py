import copy
import math
import matplotlib.pyplot as plt
import random


class Individual:
    gene = []
    fitness = 0

    def __repr__(self):
        return "Gene string " + "".join(str(i) for i in self.gene) + " - fitness: " + str(self.fitness) + "\n"

P = 5000
N = 10
MUTRATE = 0.3
MUTSTEP = 0.9
GENERATIONS = 500

def minimisation(individual):
    fitness = 0
    # for i in range(0, N-1):
    #     fitness += 100 * (individual.gene[i + 1] - (individual.gene[i] ** 2)) ** 2 + (1 - individual.gene[i]) ** 2
    # return fitness

    for i in range(0, N-1):
        part1 = individual.gene[i+1] - math.pow(individual.gene[i], 2)
        part2 = math.pow((1 - individual.gene[i]), 2)
        fitness += 100 * math.pow(part1, 2) + part2
    return fitness


def init_population():
    population = []
    for i in range(0, P):
        temp_gene = []
        for i in range(0, N):
            temp_gene.append(random.uniform(-100.0, 100.0))  # a random gene between -100, 100

        new_ind = Individual()  # initialise new instance
        new_ind.gene = temp_gene.copy()  # copy the gene from temp_gene and assign to gene of individual
        new_ind.fitness = minimisation(new_ind)  # initialise instance's fitness

        # print(temp_gene, " -> ", new_ind.fitness)
        population.append(new_ind)

    return population


# tournament selection
def TNS(population):
    offsprings = []
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, P - 1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:  # if one's fitness higher then add to temp offsprings
            offsprings.append(off2)
        else:
            offsprings.append(off1)
    return offsprings


# roulette wheel selection
def RWS(population):
    # total fitness of initial pop
    total = 0
    for individual in population:
        total += 1 / individual.fitness

    offspring = []
    # Roulette Wheel Selection Process
    # Select two parents and recombine pairs of parents
    for i in range(0, P):
        selection_point = random.uniform(0.0, total)
        running_total = 0
        j = 0
        while running_total <= selection_point:
            running_total += 1 / population[j].fitness
            j += 1
            if(j == P):
                break
        offspring.append(copy.deepcopy(population[j-1]))

    return offspring


# one point crossover
def crossover(offspring):
    cross_offsprings = []

    for i in range(0, P, 2):
        cross_point = random.randint(1, N - 1)

        off1 = offspring[i]
        off2 = offspring[i + 1]

        off1.gene[cross_point:], off2.gene[cross_point:] = off2.gene[cross_point:], off1.gene[cross_point:]

        off1.fitness = minimisation(off1)  # 1st gene be counted fitness
        cross_offsprings.append(off1)  # 1st gene be added to new population after crossover

        off2.fitness = minimisation(off2)  # 2nd gene be counted fitness
        cross_offsprings.append(off2)  # 2nd gene be added to new population after crossover

    return cross_offsprings

# print(crossover(RWS(init_population())))


# bit-wise mutation
def mutation(cross_offsprings, MUTRATE, MUTSTEP):
    mut_offsprings = []

    for i in range(0, P):
        new_ind = Individual();
        new_ind.gene = []
        for j in range(0, N):
            gene = cross_offsprings[i].gene[j]

            MUTPROB = random.uniform(0.0, 100.0)
            if MUTPROB < (MUTRATE):
                ALTER = random.uniform(0.0, MUTSTEP)
                if random.randint(0, 100) < 50:  # if random num is 1, add ALTER
                    gene += ALTER
                else:            # if random num is 0, minus ALTER
                    gene -= ALTER
            if gene > 100:   # if gene value is larger than pi, reset set to pi
                gene = 100
            if gene < -100:   # if gene value is smaller than 0, reset it to 0
                gene = -100

            new_ind.gene.append(gene)  # add gene to new individual
        new_ind.fitness = minimisation(new_ind)  # count its fitness
        mut_offsprings.append(new_ind)  # add new release to new population after mutation

    return mut_offsprings


# descending sorting
def sorting(population):
    #  descending sorting based on  individual's fitness
    population.sort(key=lambda individual: individual.fitness, reverse=True)
    return population


# optimisation
def optimising(population, new_population):
    # sorting instance with descending fitness
    population = sorting(population)

    # take two instances with the worst fitness in the old population at index -1 and index -2
    worstFit_old_1 = population[-1]
    worstFit_old_2 = population[-2]

    # overwrite the old population with mutate_offspring
    population = copy.deepcopy(new_population)

    # sorting instance with descending fitness
    population = sorting(population)

    # after deepcopy new pop to old pop
    # take the two instance with the best fitness in the new population at index 0 and index 1
    bestFit_new_1 = population[0]
    bestFit_new_2 = population[1]

    # compare the fitness btw the ones in the old pop and the ones in the new pop
    # replace the two worst fitness/gene by the two best fitness/gene at specific index in the new population
    if bestFit_new_1.fitness > worstFit_old_1.fitness:
        population[0].fitness = worstFit_old_1.fitness
        population[0].gene = worstFit_old_1.gene
    if bestFit_new_2.fitness > worstFit_old_2.fitness:
        population[1].fitness = worstFit_old_2.fitness
        population[1].gene = worstFit_old_2.gene

    return population


def genetic_algorithm(population, selection, MUTRATE, MUTSTEP):
    # storing data to plot
    meanFit_values = []
    minFit_values = []

    for gen in range(0, GENERATIONS):
        # TNS / RWS process
        offsprings = selection(population)
        # crossover process
        cross_offsprings = crossover(offsprings)
        # mutation process
        mut_offsprings = mutation(cross_offsprings, MUTRATE, MUTSTEP)
        # optimising
        population = optimising(population, mut_offsprings)

        # calculate Min and Mean Fitness
        # storing fitness in a list
        Fit = []
        for ind in population:
            Fit.append(minimisation(ind))
        # print(Fit)

        minFit = min(Fit)  # take out the min fitness among fitness in Fit
        meanFit = sum(Fit) / P  # sum all the fitness and divide by Population size

        # append maxFit and meanFit respectively to MaxFit_values and MeanFit_values
        minFit_values.append(minFit)
        meanFit_values.append(meanFit)

        # display
        # print("GENERATION " + str(gen + 1))
    print("Min Fitness: " + str(minFit) + "\n")
    print("Mean Fitness: " + str(meanFit) + "\n")

    return minFit_values, meanFit_values


# plotting
plt.ylabel("Fitness")
plt.xlabel("Number of Generation")

#  Storing
minFit_data1 = []
minFit_data2 = []
minFit_data3 = []
minFit_data4 = []

meanFit_data1 = []
meanFit_data2 = []
meanFit_data3 = []
meanFit_data4 = []


# Compare TNS & RWS-----------------------------[1]

# plt.title("Minimisation GA \n Touranment and Roulette Wheel Selection \n"
#           + "N = " + str(N) + " MUTRATE = " + str(MUTRATE) + " MUTSTEP = " + str(MUTSTEP))
#
# # initialise original population
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
# minFit_data2, meanFit_data2 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Tournament")
# plt.plot(minFit_data2, label="Roulette Wheel")

#test-/ok/
# P = 5000
# N = 10
# MUTRATE = 0.3
# MUTSTEP = 0.9
# GENERATIONS = 500
# Min Fitness: 0.5054779077535237
# Mean Fitness: 3.6535281336775123
# Min Fitness: 6.343367994319884
# Mean Fitness: 7.659454092537506

# Best Fitness and Mean Fitness of TNS---------------[2]

# plt.title("Minimisation GA - Touranment Selection \n"
#             + "N = " + str(N) + " MUTRATE = " + str(MUTRATE) + " MUTSTEP = " + str(MUTSTEP))
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Min Fitness")
# plt.plot(meanFit_data1, label="Mean Fitness")

#test-/ok/
# P = 5000
# N = 10
# MUTRATE = 0.3
# MUTSTEP = 0.9
# GENERATIONS = 500
# Min Fitness: 0.9791907504021441
# Mean Fitness: 4.006859488232009

# Vary MUTRATE of TNS -----------------------------[3]
# plt.title("Minimisation GA - Touranment Selection \n"
#             + "Vary MUTRATE")
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, 0.3, MUTSTEP)
# minFit_data2, meanFit_data2 = genetic_algorithm(population, TNS, 0.03, MUTSTEP)
# minFit_data3, meanFit_data3 = genetic_algorithm(population, TNS, 0.003, MUTSTEP)
# minFit_data4, meanFit_data4 = genetic_algorithm(population, TNS, 0.0003, MUTSTEP)
#
# plt.plot(minFit_data1, label="MUTRATE 0.3")
# plt.plot(minFit_data2, label="MUTRATE 0.03")
# plt.plot(minFit_data3, label="MUTRATE 0.003")
# plt.plot(minFit_data4, label="MUTRATE 0.0003")

#test-/ok/
# P = 50
# N = 10
# MUTRATE = 0.3
# MUTSTEP = 0.9
# GENERATIONS = 100
#
# Min Fitness: 99684281.9121107
# Mean Fitness: 101351012.17040497
#
# Min Fitness: 423728695.1664391
# Mean Fitness: 423728695.1664391
#
# Min Fitness: 274888852.56087416
# Mean Fitness: 274888852.56087434
#
# Min Fitness: 534119413.39533925
# Mean Fitness: 534119413.39533967


# Best Fitness and Mean Fitness of RWS----------------------[4]

plt.title("Minimisation GA - Roulette Wheel Selection \n"
            + "N = " + str(N) + " MUTRATE = " + str(MUTRATE) + " MUTSTEP = " + str(MUTSTEP))

# initialise original population
population = init_population()

minFit_data1, meanFit_data1 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)

plt.plot(minFit_data1, label="Min Fitness")
plt.plot(meanFit_data1, label="Mean Fitness")

#test-/???/
# P = 5000
# N = 10
# MUTRATE = 0.3
# MUTSTEP = 0.9
# GENERATIONS = 500
# Min Fitness: 213.80452061591197
# Mean Fitness: 233.26140452568404

# Vary MUTRATE of RWS-------------------------------------[5]
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "Vary MUTRATE")
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, RWS, 0.3, MUTSTEP)
# minFit_data2, meanFit_data2 = genetic_algorithm(population, RWS, 0.03, MUTSTEP)
# minFit_data3, meanFit_data3 = genetic_algorithm(population, RWS, 0.003, MUTSTEP)
# minFit_data4, meanFit_data4 = genetic_algorithm(population, RWS, 0.0003, MUTSTEP)
#
# plt.plot(minFit_data1, label="MUTRATE 0.3")
# plt.plot(minFit_data2, label="MUTRATE 0.03")
# plt.plot(minFit_data3, label="MUTRATE 0.003")
# plt.plot(minFit_data4, label="MUTRATE 0.0003")

#test-/ok/
# P = 50
# N = 10
# MUTRATE = 0.3
# MUTSTEP = 0.9
# GENERATIONS = 100

# Min Fitness: 139657598.7728544
# Mean Fitness: 143505973.93029332
#
# Min Fitness: 402117350.23294544
# Mean Fitness: 402187712.4785755
#
# Min Fitness: 263020568.9196346
# Mean Fitness: 263020568.91963443
#
# Min Fitness: 450578624.4577755
# Mean Fitness: 450578624.4577752

# DISPLAY PLOT
plt.legend(loc="upper right")
plt.show()
