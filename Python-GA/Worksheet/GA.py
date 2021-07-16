import random


class Individual:
    gene = []
    fitness = 0

    def __repr__(self):
        return "Gene string " + "".join(str(x) for x in self.gene) + " - fitness: " + str(self.fitness) +"\n"


P = 50
N = 10


def counting_ones(ind):
    fitness = 0
    for i in range(0, N):
        if ind.gene[i] == 1:  # if gene of an individual at index i equals to 1
            fitness = fitness + ind.gene[i]
    return fitness


def initialise_population():
    population = []
    for x in range(0, P):
        tempgene = []
        for x in range(0, N):
            tempgene.append(random.randint(0, 1))  # a random gene between 0.0 and 1.0(inclusive)

        newindi = Individual()  # initialise new instance
        newindi.gene = tempgene.copy()  # copy the gene from tempgene and assign to gene of individual
        newindi.fitness = counting_ones(newindi)  # initialise instance's fitness

        print(tempgene, " -> ", newindi.fitness)
        population.append(newindi)

    return population


def touranment_selection(population):
    offspring = []
    # Select two parents and recombine pairs of parents
    for i in range(0, P):
        parent1 = random.randint(0, P - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, P - 1)
        off2 = population[parent2]
        if off1.fitness > off2.fitness:  # if one's fitness higher then add to temp offsptring
            offspring.append(off1)
        else:
            offspring.append(off2)

    return offspring


print(touranment_selection(initialise_population()))



