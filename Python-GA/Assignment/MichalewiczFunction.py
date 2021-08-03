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
GENERATIONS = 1000
MUTRATE = 0.003
MUTSTEP = 1.0


def minimisation(individual):
    fitness = 0
    m = 10
    for i in range(1, N):
        fraction = (i * math.pow(individual.gene[i], 2)) / math.pi
        function = math.sin(individual.gene[i]) * (math.pow((math.sin(fraction)), (2 * m)))
        fitness += -function
    return fitness


def init_population():
    population = []
    for i in range(0, P):
        temp_gene = []
        for i in range(0, N):
            temp_gene.append(random.uniform(0.0, math.pi))  # a random gene between 0, pi

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
        total += abs(individual.fitness)

    offspring = []

    for i in range(0, P):
        selection_point = random.uniform(0.0, total)
        count_total = 0
        j = 0
        while count_total <= selection_point:
            count_total += abs(population[j].fitness)
            j += 1
            if(j == P):
                break
        offspring.append(copy.deepcopy(population[j-1]))

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

        for j in range(0, cross_point):
            head1.append(offspring[i].gene[j])
            head2.append(offspring[i + 1].gene[j])

        for j in range(cross_point, N):
            tail1.append(offspring[i].gene[j])
            tail2.append(offspring[i + 1].gene[j])

        off1.gene = head1 + tail2  # 1st gene be released after crossover
        off1.fitness = minimisation(off1)  # 1st gene be counted fitness
        cross_offsprings.append(off1)  # 1st gene be added to new population after crossover

        off2.gene = head2 + tail1  # 2nd gene be released after crossover
        off2.fitness = minimisation(off2)  # 2nd gene be counted fitness
        cross_offsprings.append(off2)  # 2nd gene be added to new population after crossover

    return cross_offsprings


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
                ALTER = random.uniform(-MUTSTEP, MUTSTEP)
                gene += ALTER
            if gene > math.pi:   # if gene value is larger than pi, reset set to pi
                gene = math.pi
            if gene < 0:   # if gene value is smaller than 0, reset it to 0
                gene = 0

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


# ---COMP
plt.title("Minimisation GA \n Tournament and Roulette Wheel Selection \n"
          + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))

population = init_population()

minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
minFit_data2, meanFit_data2 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)

plt.plot(minFit_data1, label="Tournament")
plt.plot(minFit_data2, label="Roulette Wheel")

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.03
# MUTSTEP = 1.0

# Min Fitness: -18.617601236562813
# Mean Fitness: -17.901356980791196

# Min Fitness: -18.26424914477288
# Mean Fitness: -13.832748953830267

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.003
# MUTSTEP = 1.0

# Min Fitness: -18.431833114975873
# Mean Fitness: -18.39843852568397
#
# Min Fitness: -18.291412061474283
# Mean Fitness: -17.835175486774343

# ----
# Best Fitness and Mean Fitness of TNS

# plt.title("Minimisation GA - Tournament Selection \n"
#             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
#
# # initialise original population
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Best Fitness")
# plt.plot(meanFit_data1, label="Mean Fitness")

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.03
# MUTSTEP = 1.0
#
# Min Fitness: -18.616924422344308
# Mean Fitness: -17.907136106502158

# -----
# Vary MUTRATE
# plt.title("Minimisation GA - Tournament Selection \n"
#             + "Vary Mutrates")
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

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.03
# MUTSTEP = 1.0

# Min Fitness: -14.882451986945927
# Mean Fitness: -5.675430000448016
#
# Min Fitness: -18.598858535803018      1
# Mean Fitness: -17.79270170632231
#
# Min Fitness: -18.449819806970083      2
# Mean Fitness: -18.354626096694574
#
# Min Fitness: -16.78878722459171
# Mean Fitness: -16.78878722459171

# -----
# Best Fitness and Mean Fitness of RWS
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "N = " + str(N) + " Mutrate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
#
# # initialise original population
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Best Fitness")
# plt.plot(meanFit_data1, label="Mean Fitness")

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.003
# MUTSTEP = 1.0

# Min Fitness: -18.08159341913373
# Mean Fitness: -17.97876736441279

# -----
# Vary MUTRATE
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "Vary Mutrates")
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

# P = 100
# N = 20
# GENERATIONS = 1000
# MUTRATE = 0.003
# MUTSTEP = 1.0

# Min Fitness: -13.688596807681837
# Mean Fitness: -5.549177313117643
#
# Min Fitness: -18.116985633620878      2
# Mean Fitness: -14.246975837831235
#
# Min Fitness: -18.284615108134084      1
# Mean Fitness: -17.84901954027082
#
# Min Fitness: -16.89765001891017
# Mean Fitness: -16.878234131046696


# DISPLAY PLOT
plt.legend(loc="upper right")
plt.show()
