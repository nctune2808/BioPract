import copy
import math
import matplotlib.pyplot as plt
import random


class Individual:
    gene = []
    fitness = 0

    def __str__(self):
        return "Gene string " + "".join(str(i) for i in self.gene) + " - fitness: " + str(self.fitness) + "\n"


P = 100
N = 20
MUTRATE = 0.03
MUTSTEP = 1.0
GENERATIONS = 250


# # calculate individual's fitness
# def maximisation(individual):
#     fitness = 0
#     for i in range(0, N):
#         # if individual.gene[i] == 1:
#         fitness = fitness + individual.gene[i]
#     return fitness
#
# # calculate population's fitness
# def total_fitness(population):
#     total_fitness = 0
#     for individual in population:
#         total_fitness += individual.fitness
#     return total_fitness


def minimisation(individual):
    fitness = 10 * N
    for i in range(0, N):
        squared = math.pow(individual.gene[i], 2)
        cos = 10 * math.cos(individual.gene[i] * (2 * math.pi))
        fitness += squared - cos
    return fitness


def init_population():
    population = []
    for i in range(0, P):
        temp_gene = []
        for i in range(0, N):
            temp_gene.append(random.uniform(-5.12, 5.12))  # random gene between -5.12, 5.12
            # temp_gene.append(random.uniform(0.0, 1.0))    # random gene between 0.0, 1.0
        new_ind = Individual()
        new_ind.gene = temp_gene.copy()  # copy the gene from temp_gene and assign to gene of new individual
        new_ind.fitness = minimisation(new_ind)
        # print(temp_gene, " -> ", new_ind.fitness)
        population.append(new_ind)

    return population


# TNS
# def TNS_max(population):
#     offspring = []
#     for i in range(0, P):
#         parent1 = random.randint(0, P - 1)
#         off1 = population[parent1]
#         parent2 = random.randint(0, P - 1)
#         off2 = population[parent2]
#         if off1.fitness > off2.fitness:  # add to temp offspring
#             offspring.append(off1)
#         else:
#             offspring.append(off2)
#     return offspring


def TNS_min(population):
    offsprings = []
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        parent2 = random.randint(0, P - 1)

        off1 = population[parent1]
        off2 = population[parent2]

        if off1.fitness > off2.fitness:  # add to temp offsprings
            offsprings.append(off2)
        else:
            offsprings.append(off1)
    return offsprings


# RWS
# def RWS_max(population):
#     initial_fits = total_fitness(population)
#     offspring = copy.deepcopy(population)
#     for i in range(0, P):
#         selection_point = random.uniform(0.0, initial_fits)
#         running_total = 0
#         j = 0
#         while running_total <= selection_point:
#             running_total += population[j].fitness
#             j += 1
#             if j == P: break
#         offspring[i] = population[j - 1]
#     return offspring


def RWS_min(population):
    total = 0
    for individual in population:
        total += 1 / individual.fitness
    offspring = []
    for i in range(0, P):
        selection_point = random.uniform(0.0, total)
        running_total = 0
        j = 0
        while running_total <= selection_point:
            running_total += 1 / population[j].fitness
            j += 1
            if j == P: break
        offspring.append(copy.deepcopy(population[j - 1]))
    return offspring


# one point crossover
def crossover(offspring):
    cross_offsprings = []
    for i in range(0, P, 2):
        off1 = Individual()
        off2 = Individual()

        # 2 heads and 2 tails
        head1 = []
        tail1 = []
        head2 = []
        tail2 = []

        cross_point = random.randint(1, N - 1)

        for j in range(0, cross_point):  # head from 0 to cross_point
            head1.append(offspring[i].gene[j])
            head2.append(offspring[i + 1].gene[j])
        for j in range(cross_point, N):  # tail from cross_point to N
            tail1.append(offspring[i].gene[j])
            tail2.append(offspring[i + 1].gene[j])

        off1.gene = head1 + tail2  # 1st gene be released after crossover
        off1.fitness = minimisation(off1)  # 1st gene be counted fitness
        cross_offsprings.append(off1)  # 1st gene be added to new population after crossover

        off2.gene = head2 + tail1  # 2nd gene be released after crossover
        off2.fitness = minimisation(off2)  # 2nd gene be counted fitness
        cross_offsprings.append(off2)  # 2nd gene be added to new population after crossover
    return cross_offsprings


# print(crossover(TNS(init_population())))


# bit-wise mutation
def mutation(cross_offsprings, MUTRATE, MUTSTEP):
    mut_offsprings = []
    for i in range(0, P):
        new_ind = Individual();
        new_ind.gene = []
        for j in range(0, N):
            gene = cross_offsprings[i].gene[j]
            MUTPROB = random.uniform(0.0, 100.0)
            if MUTPROB < (100 * MUTRATE):
                ALTER = random.uniform(0.0, MUTSTEP)
                if random.randint(0, 1) == 1:
                    gene += ALTER
                else:
                    gene -= ALTER
            if gene > 5.12:  # if gene value is larger than 1.0, reset it to 1.0
                gene = 5.12
            if gene < -5.12:  # if gene value is smaller than 0.0, reset it to 0.0
                gene = -5.12
            new_ind.gene.append(gene)  # add gene to new individual
        new_ind.fitness = minimisation(new_ind)  # count its fitness
        mut_offsprings.append(new_ind)  # add new release to new population after mutation
    return mut_offsprings


def sorting(population):
    population.sort(key=lambda individual: individual.fitness, reverse=True)
    return population


# optimisation
def optimising(population, new_population):
    # sorting descending fitness
    population = sorting(population)

    # # take two instances with the worst fitness in the old population at index -1 and index -2
    worstFit_old_1 = population[-1]
    worstFit_old_2 = population[-2]
    # bestFit_old_1 = population[0]
    # bestFit_old_2 = population[1]

    # overwrite the old population with mutate_offspring
    population = copy.deepcopy(new_population)

    # sorting descending fitness again
    population = sorting(population)

    # after deepcopy new pop to old one
    # take the two instance with the best fitness in the new population at index 0 and index 1
    bestFit_new_1 = population[0]
    bestFit_new_2 = population[1]
    # worstFit_new_1 = population[-1]
    # worstFit_new_2 = population[-2]

    # compare the fitness
    if bestFit_new_1.fitness > worstFit_old_1.fitness:
        population[0].fitness = worstFit_old_1.fitness
        population[0].gene = worstFit_old_1.gene
    if bestFit_new_2.fitness > worstFit_old_2.fitness:
        population[1].fitness = worstFit_old_2.fitness
        population[1].gene = worstFit_old_2.gene
    # if bestFit_old_1.fitness > worstFit_new_1.fitness:
    #     population[-1].fitness = bestFit_old_1.fitness
    #     population[-1].gene = bestFit_old_1.gene
    # if bestFit_old_2.fitness > worstFit_new_2.fitness:
    #     population[-2].fitness = bestFit_old_2.fitness
    #     population[-2].gene = bestFit_old_2.gene
    return population


def genetic_algorithm(population, selection, MUTRATE, MUTSTEP):
    # storing data to plot
    meanFitness_values = []
    # maxFitness_values = []
    minFitness_values = []

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
        Fitness = []
        for ind in population:
            Fitness.append(minimisation(ind))

        # maxFitness = max(Fitness)
        minFitness = min(Fitness)  # min fitness among Fitness Array
        meanFitness = sum(Fitness) / P  # sum all the fitness and divide by Population size

        # maxFitness_values.append(maxFitness)
        minFitness_values.append(minFitness)
        meanFitness_values.append(meanFitness)


    # print("Max Fitness: " + str(maxFitness) + "\n")
    print("Min Fitness: " + str(minFitness))
    print("Mean Fitness: " + str(meanFitness) + "\n")

    return minFitness_values, meanFitness_values
    # return maxFitness_values, meanFitness_values


plt.ylabel("Fitness")
plt.xlabel("Number of Generation")

#  Storing
minFitness_data1, minFitness_data2, minFitness_data3, minFitness_data4 = []
# maxFitness_data1, maxFitness_data2, maxFitness_data3, maxFitness_data4 = []
meanFitness_data1, meanFitness_data2, meanFitness_data3, meanFitness_data4 = []

# ====================MAX======================
# # TNS vs RWS
# plt.title("Maximisation GA \n Tournament and Roulette Wheel Selection \n"
#           + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# population = init_population()
#
# maxFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_max, MUTRATE, MUTSTEP)
# maxFitness_data2, meanFitness_data2 = genetic_algorithm(population, RWS_max, MUTRATE, MUTSTEP)
#
# plt.plot(maxFitness_data1, label="Tournament")
# plt.plot(maxFitness_data2, label="Roulette Wheel")
#
# # Test/ok/
# # P = 50
# # N = 50
# # MUTRATE = 0.03
# # MUTSTEP = 1.0
# # GENERATIONS = 100
#
# # Max Fitness: 50.0
# # Mean Fitness: 49.326010267863715
# #
# # Max Fitness: 48.24569602940331
# # Mean Fitness: 45.10896051943288
#
#
# #TS
# # plt.title("Maximisation GA - Tournament Selection \n"
# #             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# # population = init_population()
# # maxFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_max, MUTRATE, MUTSTEP)
# # plt.plot(maxFitness_data1, label="Best Fitness")
# # plt.plot(meanFitness_data1, label="Mean Fitness")
#
# # Test/ok/
# # P = 50
# # N = 50
# # MUTRATE = 0.03
# # MUTSTEP = 1.0
# # GENERATIONS = 100
# #
# # Max Fitness: 50.0
# # Mean Fitness: 49.381515968760844
#
# # TNS MUTRATE
# # plt.title("Maximisation GA - Tournament Selection \n"
# #             + "Different Mutrates")
# # population = init_population()
# #
# # maxFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_max, 0.3, 1.0)
# # maxFitness_data2, meanFitness_data2 = genetic_algorithm(population, TNS_max, 0.03, 1.0)
# # maxFitness_data3, meanFitness_data3 = genetic_algorithm(population, TNS_max, 0.003, 1.0)
# # maxFitness_data4, meanFitness_data4 = genetic_algorithm(population, TNS_max, 0.0003, 1.0)
# #
# # plt.plot(maxFitness_data1, label="Mutrate 0.3")
# # plt.plot(maxFitness_data2, label="Mutrate 0.03")
# # plt.plot(maxFitness_data3, label="Mutrate 0.003")
# # plt.plot(maxFitness_data4, label="Mutrate 0.0003")
#
# # Test/ok/
# # P = 50
# # N = 50
# # MUTRATE = 0.03
# # MUTSTEP = 1.0
# # GENERATIONS = 100
# #
# # Max Fitness: 44.23095743208713
# # Mean Fitness: 36.62964274901356
# #
# # Max Fitness: 50.0
# # Mean Fitness: 49.51962818765733
# #
# # Max Fitness: 48.36366092343277
# # Mean Fitness: 47.88051521022532
# #
# # Max Fitness: 43.90732577140833
# # Mean Fitness: 43.54204858848547
#
# #RWS
# # plt.title("Maximisation GA - Roulette Wheel Selection \n"
# #             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# # population = init_population()
# # maxFitness_data1, meanFitness_data1 = genetic_algorithm(population, RWS_max, MUTRATE, MUTSTEP)
# # plt.plot(maxFitness_data1, label="Best Fitness")
# # plt.plot(meanFitness_data1, label="Mean Fitness")
#
# # Test/ok/
# # P = 50
# # N = 50
# # MUTRATE = 0.03
# # MUTSTEP = 1.0
# # GENERATIONS = 100
#
# # Max Fitness: 47.87198046449989
# # Mean Fitness: 44.23571700425208
#
#
# # RWS MUTRATE
# # plt.title("Maximisation GA - Roulette Wheel Selection \n"
# #             + "Different Mutrates")
# # population = init_population()
# #
# # maxFitness_data1, meanFitness_data1 = genetic_algorithm(population, RWS_max, 0.3, 1.0)
# # maxFitness_data2, meanFitness_data2 = genetic_algorithm(population, RWS_max, 0.03, 1.0)
# # maxFitness_data3, meanFitness_data3 = genetic_algorithm(population, RWS_max, 0.003, 1.0)
# # maxFitness_data4, meanFitness_data4 = genetic_algorithm(population, RWS_max, 0.0003, 1.0)
# #
# # plt.plot(maxFitness_data1, label="Mutrate 0.3")
# # plt.plot(maxFitness_data2, label="Mutrate 0.03")
# # plt.plot(maxFitness_data3, label="Mutrate 0.003")
# # plt.plot(maxFitness_data4, label="Mutrate 0.0003")
#
# # Test/ok/
# # P = 50
# # N = 50
# # MUTRATE = 0.03
# # MUTSTEP = 1.0
# # GENERATIONS = 100
#
# # Max Fitness: 43.03879566926029
# # Mean Fitness: 32.297198247448485
# #
# # Max Fitness: 46.758083258026545
# # Mean Fitness: 44.14796497635577
# #
# # Max Fitness: 42.55325028047419
# # Mean Fitness: 40.99085004425824
# #
# # Max Fitness: 38.27404822946088
# # Mean Fitness: 37.82836279483741


# ================ MIN ==============

# TNS vs RWS
plt.title("Minimisation GA \n Tournament and Roulette Wheel Selection \n"
          + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))

# initialise original population
population = init_population()

minFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_min, MUTRATE, MUTSTEP)
minFitness_data2, meanFitness_data2 = genetic_algorithm(population, RWS_min, MUTRATE, MUTSTEP)

plt.plot(minFitness_data1, label="Tournament")
plt.plot(minFitness_data2, label="Roulette Wheel")

# P = 100
# N = 10
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 100

# comp10
# Min Fitness: 0.43622644300060287
# Mean Fitness: 3.8197628268323847
#
# Min Fitness: 3.1828258887992433
# Mean Fitness: 8.16116104879124


# P = 100
# N = 20
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 250
#comp20
# Min Fitness: 0.6581927861139256
# Mean Fitness: 9.394424795143884
#
# Min Fitness: 2.170011820536276
# Mean Fitness: 10.86736630105411


# TNS
# plt.title("Minimisation GA - Tournament Selection \n"
#             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# population = init_population()
# minFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_min, MUTRATE, MUTSTEP)
# plt.plot(minFitness_data1, label="Best Fitness")
# plt.plot(meanFitness_data1, label="Mean Fitness")

# P = 100
# N = 10
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 300

# TNS
# Min Fitness: 0.007116915075881636
# Mean Fitness: 1.7091844175237383


# TNS MUTRATE
# plt.title("Minimisation GA - Tournament Selection \n"
#             + "Different Mutrates")
# population = init_population()
#
# minFitness_data1, meanFitness_data1 = genetic_algorithm(population, TNS_min, 0.3, 1.0)
# minFitness_data2, meanFitness_data2 = genetic_algorithm(population, TNS_min, 0.03, 1.0)
# minFitness_data3, meanFitness_data3 = genetic_algorithm(population, TNS_min, 0.003, 1.0)
# minFitness_data4, meanFitness_data4 = genetic_algorithm(population, TNS_min, 0.0003, 1.0)
#
# plt.plot(minFitness_data1, label="Mutrate 0.3")
# plt.plot(minFitness_data2, label="Mutrate 0.03")
# plt.plot(minFitness_data3, label="Mutrate 0.003")
# plt.plot(minFitness_data4, label="Mutrate 0.0003")

# P = 100
# N = 10
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 300

# TNS mutrates
# Min Fitness: 8.567393372281515
# Mean Fitness: 75.87173240801299
#
# Min Fitness: 0.029988624507156558     1
# Mean Fitness: 5.446061660223031
#
# Min Fitness: 2.480913224948752
# Mean Fitness: 2.5284094233411185
#
# Min Fitness: 5.511346570653178
# Mean Fitness: 5.51134657065318


# RWS
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# population = init_population()
# minFitness_data1, meanFitness_data1 = genetic_algorithm(population, RWS_min, MUTRATE, MUTSTEP)
# plt.plot(minFitness_data1, label="Best Fitness")
# plt.plot(meanFitness_data1, label="Mean Fitness")

# P = 100
# N = 10
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 300

# RWS
# Min Fitness: 0.02678613179945266
# Mean Fitness: 1.9721901844231733


# RWS MUTRATE
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "Different Mutrates")
# population = init_population()
#
# minFitness_data1, meanFitness_data1 = genetic_algorithm(population, RWS_min, 0.3, 1.0)
# minFitness_data2, meanFitness_data2 = genetic_algorithm(population, RWS_min, 0.03, 1.0)
# minFitness_data3, meanFitness_data3 = genetic_algorithm(population, RWS_min, 0.003, 1.0)
# minFitness_data4, meanFitness_data4 = genetic_algorithm(population, RWS_min, 0.0003, 1.0)
#
# plt.plot(minFitness_data1, label="Mutrate 0.3")
# plt.plot(minFitness_data2, label="Mutrate 0.03")
# plt.plot(minFitness_data3, label="Mutrate 0.003")
# plt.plot(minFitness_data4, label="Mutrate 0.0003")


# P = 100
# N = 10
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 300

# RWS mutrates
# Min Fitness: 8.567393372281515
# Mean Fitness: 75.87173240801299
#
# Min Fitness: 0.029988624507156558
# Mean Fitness: 5.446061660223031
#
# Min Fitness: 2.480913224948752
# Mean Fitness: 2.5284094233411185
#
# Min Fitness: 5.511346570653178
# Mean Fitness: 5.51134657065318

plt.legend(loc="upper right")
plt.show()
