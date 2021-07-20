import copy
import matplotlib.pyplot as plt
import random


class Individual:
    gene = []
    fitness = 0

    def __repr__(self):
        return "Gene string " + "".join(str(i) for i in self.gene) + " - fitness: " + str(self.fitness) + "\n"


P = 50
N = 50
GENERATIONS = 100
MUTRATE = 0.03
MUTSTEP = 0.9


# calculate individual's fitness
def gene_fitness(individual):
    fitness = 0
    for i in range(0, N):
        # if individual.gene[i] == 1:  # if gene at index i equals to 1
        fitness = fitness + individual.gene[i]
    return fitness


# calculate population's fitness
def total_fitness(population):
    total_fitness = 0
    for individual in population:
        total_fitness += individual.fitness
    return total_fitness


def init_population():
    population = []
    for i in range(0, P):
        temp_gene = []
        for i in range(0, N):
            temp_gene.append(random.uniform(0.0, 1.0))  # a random gene between 0.0 and 1.0

        new_ind = Individual()  # initialise new instance
        new_ind.gene = temp_gene.copy()  # copy the gene from temp_gene and assign to gene of individual
        new_ind.fitness = gene_fitness(new_ind)  # initialise instance's fitness

        print(temp_gene, " -> ", new_ind.fitness)
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
            offsprings.append(off1)
        else:
            offsprings.append(off2)
    return offsprings


# Roulette Wheel Selection Process
def RWS(population):
    # total fitness of initial pop
    initial_fits = total_fitness(population)

    offspring = copy.deepcopy(population)
    # Roulette Wheel Selection Process
    # Select two parents and recombine pairs of parents
    for i in range(0, P):
        selection_point = random.uniform(0.0, initial_fits)
        running_total = 0
        j = 0
        while running_total <= selection_point:
            running_total += population[j].fitness
            j += 1
            if(j == P):
                break
        offspring[i] = population[j-1]

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

        cross_point = random.randint(0, N - 1)

        for j in range(0, cross_point):  # head from 0 to crosspoint
            head1.append(offspring[i].gene[j])
            head2.append(offspring[i + 1].gene[j])

        for j in range(cross_point, N):  # tail from crosspoint to N
            tail1.append(offspring[i].gene[j])
            tail2.append(offspring[i + 1].gene[j])

        off1.gene = head1 + tail2  # 1st gene be released after crossover
        off1.fitness = gene_fitness(off1)  # 1st gene be counted fitness
        cross_offsprings.append(off1)  # 1st gene be added to new population after crossover

        off2.gene = head2 + tail1  # 2nd gene be released after crossover
        off2.fitness = gene_fitness(off2)  # 2nd gene be counted fitness
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
            ALTER = random.uniform(0.0, MUTSTEP)
            MUTPROB = random.randint(0.0, 100.0)
            if MUTPROB < (100 * MUTRATE):
                if random.randint(0, 1) == 1:  # if random num is 1, add ALTER
                    gene += ALTER
                else:            # if random num is 0, minus ALTER
                    gene -= ALTER
                if gene > 1.0:   # if gene value is larger than 1.0, reset it to 1.0
                    gene = 1.0
                if gene < 0.0:   # if gene value is smaller than 0.0, reset it to 0.0
                    gene = 0.0

            new_ind.gene.append(gene)  # add gene to new individual
        new_ind.fitness = gene_fitness(new_ind)  # count its fitness
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

    # take two instances with the best fitness in the old population at index 0 and index 1
    bestFit_old_1 = population[0]
    bestFit_old_2 = population[1]

    # overwrite the old population with mutate_offspring
    population = copy.deepcopy(new_population)

    # sorting instance with descending fitness
    population = sorting(population)

    # after deepcopy new pop to old pop
    # take the two instance with the worst fitness in the new population at index -1 and index -2
    worstFit_new_1 = population[-1]
    worstFit_new_2 = population[-2]

    # compare the fitness btw the ones in the old pop and the ones in the new pop
    # replace the two worst fitness/gene by the two best fitness/gene at specific index in the new population
    if bestFit_old_1.fitness > worstFit_new_1.fitness:
        population[-1].fitness = bestFit_old_1.fitness
        population[-1].gene = bestFit_old_1.gene
    if bestFit_old_2.fitness > worstFit_new_2.fitness:
        population[-2].fitness = bestFit_old_2.fitness
        population[-2].gene = bestFit_old_2.gene

    return population


def genetic_algorithm(population, selection, MUTRATE, MUTSTEP):
    # storing data to plot
    meanFit_values = []
    maxFit_values = []
    # ===========GENETIC ALGORITHM===============

    for gen in range(0, GENERATIONS):
        # TN / RW selection process
        offsprings = selection(population)

        # crossover process
        cross_offsprings = crossover(offsprings)
        # mutation process
        mut_offsprings = mutation(cross_offsprings, MUTRATE, MUTSTEP)
        # optimising
        population = optimising(population, mut_offsprings)

        # calculate Max and Mean Fitness
        # storing fitness in a list
        Fit = []
        for ind in population:
            Fit.append(gene_fitness(ind))
        # print(Fit)

        maxFit = max(Fit)  # take out the max fitness among fitnesses in Fit
        meanFit = sum(Fit) / P  # sum all the fitness and divide by Population size

        # append maxFit and meanFit respectively to MaxFit_values and MeanFit_values
        maxFit_values.append(maxFit)
        meanFit_values.append(meanFit)

        # display
        # print("GENERATION " + str(gen + 1))
        # print("Mean Fitness: " + str(meanFit))
        # print("Max Fitness: " + str(maxFit) + "\n")
    print("Max Fitness: " + str(maxFit) + "\n")
    print("Mean Fitness: " + str(meanFit) + "\n")

    return maxFit_values, meanFit_values


# plotting
plt.ylabel("Fitness")
plt.xlabel("Number of Generation")

#  Storing
maxFit_data1 = []
maxFit_data2 = []
maxFit_data3 = []
maxFit_data4 = []

meanFit_data1 = []
meanFit_data2 = []
meanFit_data3 = []
meanFit_data4 = []


# [----------------- UNCOMMENT THIS AND ALTER N TO TEST -----------------]
N = 50
plt.title("Maximisation GA \n Tournament and Roulette Wheel Selection \n"
            + "N = " + str(N) + " MUTRATE = " + str(MUTRATE) + " MUTSTEP = " + str(MUTSTEP))

# initialise original population
population = init_population()

maxFit_data1, meanFit_data1 = genetic_algorithm(population, TNS, MUTRATE, MUTSTEP)
maxFit_data2, meanFit_data2 = genetic_algorithm(population, RWS, MUTRATE, MUTSTEP)

plt.plot(maxFit_data1, label="Tournament")
plt.plot(maxFit_data2, label="Roulette Wheel")


# DISPLAY PLOT
plt.legend(loc="lower right")
plt.show()
