import copy
import math
import matplotlib.pyplot as plt
import random


class Individual:
    gene = []
    fitness = 0

    def __str__(self):
        return "Gene string " + "".join(str(i) for i in self.gene) + " - fitness: " + str(self.fitness) + "\n"

P = 10000
N = 20
MUTRATE = 0.03
MUTSTEP = 1.0
GENERATIONS = 200

def minimisation(individual):
    fitness = 0
    for i in range(1, N-1):
        fitness += 100 * (individual.gene[i + 1] - (individual.gene[i] ** 2)) ** 2 + (1 - individual.gene[i]) ** 2
    return fitness

    # for i in range(0, N-1):
    #     part1 = individual.gene[i+1] - math.pow(individual.gene[i], 2)
    #     part2 = math.pow((1 - individual.gene[i]), 2)
    #     fitness += 100 * math.pow(part1, 2) + part2
    # return fitness


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
        # cross_point = random.randint(1, N - 1)
        #
        # off1 = offspring[i]
        # off2 = offspring[i + 1]
        #
        # off1.gene[cross_point:], off2.gene[cross_point:] = off2.gene[cross_point:], off1.gene[cross_point:]
        #
        # off1.fitness = minimisation(off1)  # 1st gene be counted fitness
        # cross_offsprings.append(off1)  # 1st gene be added to new population after crossover
        #
        # off2.fitness = minimisation(off2)  # 2nd gene be counted fitness
        # cross_offsprings.append(off2)  # 2nd gene be added to new population after crossover

        off1 = Individual()
        off2 = Individual()

        # 2 heads and 2 tails
        head1 = []
        tail1 = []
        head2 = []
        tail2 = []

        cross_point = random.randint(1, N - 1)

        for j in range(0, cross_point):  # head from 0 to crosspoint
            head1.append(offspring[i].gene[j])
            head2.append(offspring[i + 1].gene[j])

        for j in range(cross_point, N):  # tail from crosspoint to N
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

            MUTPROB = random.randint(0, 100)
            if MUTPROB < (100*MUTRATE):
                ALTER = random.uniform(-MUTSTEP, MUTSTEP)
                gene += ALTER
            if gene > 100.0:   # if gene value is larger than 100, reset set to 100
                gene = 100.0
            if gene < -100.0:   # if gene value is smaller than -100, reset it to -100
                gene = -100.0

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
#           + "N = " + str(N) + " Murate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
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
# P = 10000
# N = 20
# MUTRATE = 0.0003
# MUTSTEP = 1.0
# GENERATIONS = 200

# Min Fitness: 78.31927185964604
# Mean Fitness: 101.71897116614554
#
# Min Fitness: 151.26305008747423
# Mean Fitness: 369.87538648495854

# P = 10000
# N = 20
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 200
# Min Fitness: 27.591053695200497
# Mean Fitness: 228.45224573431537
#
# Min Fitness: 76.502688372997
# Mean Fitness: 210.17364114130427

# Best Fitness and Mean Fitness of TNS---------------[2]

# plt.title("Minimisation GA - Tournament Selection \n"
#             + "N = " + str(N) + " Murate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Best Fitness")
# plt.plot(meanFit_data1, label="Mean Fitness")

#test-/ok/
# P = 10000
# N = 20
# MUTRATE = 0.0003
# MUTSTEP = 1.0
# GENERATIONS = 200

# Min Fitness: 10.728584107123625
# Mean Fitness: 28.29276389860461

# Vary MUTRATE of TNS -----------------------------[3]
plt.title("Minimisation GA - Tournament Selection \n"
            + "Different Murates")
population = init_population()

minFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, 0.3, MUTSTEP)
minFit_data2, meanFit_data2 = genetic_algorithm(population, TNS, 0.03, MUTSTEP)
minFit_data3, meanFit_data3 = genetic_algorithm(population, TNS, 0.003, MUTSTEP)
minFit_data4, meanFit_data4 = genetic_algorithm(population, TNS, 0.0003, MUTSTEP)

plt.plot(minFit_data1, label="Murate 0.3")
plt.plot(minFit_data2, label="Murate 0.03")
plt.plot(minFit_data3, label="Murate 0.003")
plt.plot(minFit_data4, label="Murate 0.0003")

#test-/ok/
# P = 10000
# N = 20
# MUTRATE = 0.0003
# MUTSTEP = 1.0
# GENERATIONS = 200

# Min Fitness: 164.26974305491723
# Mean Fitness: 2922.486428496854
#
# Min Fitness: 15.07615279119221
# Mean Fitness: 70.89329100566503
#
# Min Fitness: 9.925435907803415
# Mean Fitness: 61.060128798622685
#
# Min Fitness: 1.0931306661966769
# Mean Fitness: 41.03454054402083



# Best Fitness and Mean Fitness of RWS----------------------[4]

# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "N = " + str(N) + " Murate = " + str(MUTRATE) + " Mutstep = " + str(MUTSTEP))
#
# # initialise original population
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)
#
# plt.plot(minFit_data1, label="Best Fitness")
# plt.plot(meanFit_data1, label="Mean Fitness")

#test-/???/
# P = 10000
# N = 20
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 200

# Min Fitness: 16.578748874229433
# Mean Fitness: 67.95332476214645

# Vary MUTRATE of RWS-------------------------------------[5]
# plt.title("Minimisation GA - Roulette Wheel Selection \n"
#             + "Different Murates")
# population = init_population()
#
# minFit_data1, meanFit_data1 = genetic_algorithm(population, RWS, 0.3, MUTSTEP)
# minFit_data2, meanFit_data2 = genetic_algorithm(population, RWS, 0.03, MUTSTEP)
# minFit_data3, meanFit_data3 = genetic_algorithm(population, RWS, 0.003, MUTSTEP)
# minFit_data4, meanFit_data4 = genetic_algorithm(population, RWS, 0.0003, MUTSTEP)
#
# plt.plot(minFit_data1, label="Murate 0.3")
# plt.plot(minFit_data2, label="Murate 0.03")
# plt.plot(minFit_data3, label="Murate 0.003")
# plt.plot(minFit_data4, label="Murate 0.0003")

#test-/ok/
# P = 10000
# N = 20
# MUTRATE = 0.03
# MUTSTEP = 1.0
# GENERATIONS = 200

# Min Fitness: 73.46755762426778
# Mean Fitness: 1983.9591058328283
#
# Min Fitness: 20.266701396311174
# Mean Fitness: 81.06278248561028
#
# Min Fitness: 115.67697663885667
# Mean Fitness: 205.45933017629116
#
# Min Fitness: 87.50641216266413
# Mean Fitness: 164.58661751072412

# DISPLAY PLOT
plt.legend(loc="upper right")
plt.show()
